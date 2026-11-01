#!/usr/bin/env python3
"""Transfer the LaTeX review into the existing university DOCX without restyling it.

Requires pandoc and lxml. The IEEE CSL file is supplied as --csl. Work on an
unmodified template via --template; never use the output as the input template.
Only document.xml and the updateFields setting are patched. New references use
embedded CSL metadata and canonical source URIs, not fabricated Zotero item IDs.
"""
import argparse, copy, hashlib, json, re, subprocess, tempfile
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
from lxml import etree as E

W='http://schemas.openxmlformats.org/wordprocessingml/2006/main'
NS={'w':W}
def el(tag, **attrs):
    x=E.Element('{'+W+'}'+tag)
    for k,v in attrs.items():x.set('{'+W+'}'+k,str(v))
    return x

def run(text='', color=None, bold=False):
    r=el('r')
    if color or bold:
        p=el('rPr');r.append(p)
        if color:p.append(el('color',val=color))
        if bold:p.append(el('b'))
    t=el('t');t.set('{http://www.w3.org/XML/1998/namespace}space','preserve');t.text=text;r.append(t)
    return r

def field_part(kind):
    r=el('r');r.append(el('fldChar',fldCharType=kind));return r

def instruction(text):
    r=el('r');t=el('instrText');t.set('{http://www.w3.org/XML/1998/namespace}space','preserve');t.text=text;r.append(t);return r

def para(style='NormalCoEKSU'):
    p=el('p');pr=el('pPr');pr.append(el('pStyle',val=style));p.append(pr);return p

def text_of(x):
    return ''.join(x.xpath('.//w:t/text()',namespaces=NS))

def pandoc(src, fmt='latex'):
    return json.loads(subprocess.check_output(['pandoc','-f',fmt,'-t','json'],input=src.encode()))

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--template',required=True);ap.add_argument('--output',required=True);ap.add_argument('--csl',required=True);ap.add_argument('--audit',required=True);a=ap.parse_args()
    root=Path(__file__).resolve().parents[1]
    with ZipFile(a.template) as z:parts={n:z.read(n) for n in z.namelist()}
    doc=E.fromstring(parts['word/document.xml']);body=doc.find('w:body',NS)
    intro=(root/'chapters/introduction.tex').read_text();chapter=(root/'chapters/literaturereview.tex').read_text()
    def expand(s):return re.sub(r'\\input\{([^}]+)\}',lambda m:(root/(m[1]+'.tex')).read_text(),s)
    expanded=expand(intro+'\n'+chapter)
    # Continuation headers are layout-only repetitions, not additional data rows.
    expanded=re.sub(r'\\endfirsthead.*?\\endhead', '', expanded, flags=re.S)
    expanded=expanded.replace(r'\bottomrule'+ '\n' +r'\endfoot','')
    ast=pandoc(expanded);blocks=ast['blocks']
    refs=json.loads(subprocess.check_output(['pandoc',str(root/'references.bib'),'-f','biblatex','-t','csljson']))
    refs={x['id']:x for x in refs}
    order=[]
    for group in re.findall(r'\\cite\{([^}]+)\}',expand(intro+'\n'+chapter)):
        for key in group.split(','):
            if key not in order:order.append(key)
    numbers={k:i+1 for i,k in enumerate(order)}
    existing={}
    for t in doc.xpath('//w:instrText/text()',namespaces=NS):
        if 'ZOTERO_ITEM CSL_CITATION' in t:
            for item in json.loads(t[t.index('{'):])['citationItems']:
                data=item['itemData']
                for k,v in refs.items():
                    if data.get('DOI') and data.get('DOI')==v.get('DOI') or data.get('title','').lower()==v.get('title','').lower():existing[k]=copy.deepcopy(item)
    assert len(existing)==6, 'Expected six existing Zotero sources'
    bibmarks={}
    for p in body.findall('w:p',NS):
        t=text_of(p)
        if re.match(r'^\[\d+\]',t):
            n=int(re.match(r'^\[(\d+)\]',t)[1]);marks=p.xpath('.//w:bookmarkStart/@w:name',namespaces=NS)
            if marks:bibmarks[order[n-1]]=next((m for m in marks if m.lower().startswith('cite_')),marks[0])
    original_marks=doc.xpath('//w:bookmarkStart/@w:name',namespaces=NS)
    original_targets=doc.xpath('//w:hyperlink/@w:anchor',namespaces=NS)
    for k,item in existing.items():
        matches=[m for m in original_marks+original_targets if m.lower().startswith('cite_id'+str(item['id'])+'_')]
        if matches:bibmarks[k]=matches[0]
    for k in order:bibmarks.setdefault(k,'Cite_'+hashlib.sha256(k.encode()).hexdigest()[:24])
    bid=max([int(x) for x in doc.xpath('//w:bookmarkStart/@w:id',namespaces=NS)]+[0])+1
    def bookmark(p,name):
        nonlocal bid
        start=el('bookmarkStart',id=bid,name=name);end=el('bookmarkEnd',id=bid);bid+=1
        p.insert(1 if p.find('w:pPr',NS) is not None else 0,start);p.append(end)
    labelnums={};labelmarks={};ch=sec=sub=tab=0
    def scan(bs):
        nonlocal ch,sec,sub,tab
        for b in bs:
            if b['t']=='Header':
                level,attr,_=b['c'];key=attr[0]
                if level==1:ch+=1;sec=sub=0;num=str(ch)
                elif level==2:sec+=1;sub=0;num=f'{ch}.{sec}'
                else:sub+=1;num=f'{ch}.{sec}.{sub}'
                labelnums[key]=num;labelmarks[key]='Masar_'+hashlib.sha256(key.encode()).hexdigest()[:20]
            elif b['t']=='Div':
                attr,children=b['c']
                if any(v['t']=='Table' for v in children):
                    tab+=1;labelnums[attr[0]]=f'{ch}.{tab}';labelmarks[attr[0]]='Masar_table_'+str(tab)
    scan(blocks)
    # Correct an existing Word-only mislink: the DGA paragraph cites NRC in the
    # template, while the authoritative LaTeX correctly cites dga2025bcm.
    for ip in body.findall('w:p',NS):
        if text_of(ip).startswith('Assessing the consequences of an interruption'):
            ins=ip.find('.//w:instrText',NS);raw=ins.text;data=json.loads(raw[raw.index('{'):]);data['citationItems']=[copy.deepcopy(existing['dga2025bcm'])];data['properties']['formattedCitation']='[2]';data['properties']['plainCitation']='[2]';ins.text=' ADDIN ZOTERO_ITEM CSL_CITATION '+json.dumps(data,ensure_ascii=False,separators=(',',':'))+' '
            for h in ip.findall('.//w:hyperlink',NS):
                if text_of(h)=='[1]':
                    h.set('{'+W+'}anchor',bibmarks['dga2025bcm'])
                    for t in h.findall('.//w:t',NS):t.text=t.text.replace('[1]','[2]')
    citation_count=0
    caption_specs=[]
    def citation(p,keys):
        nonlocal citation_count
        citation_count+=1;keys=sorted(keys,key=numbers.get)
        display=', '.join(f'[{numbers[k]}]' for k in keys)
        items=[]
        for k in keys:
            if k in existing:items.append(copy.deepcopy(existing[k]))
            else:
                d=copy.deepcopy(refs[k]);d['id']='masar/'+k
                uri='https://doi.org/'+d['DOI'] if d.get('DOI') else d.get('URL')
                assert uri, k
                items.append({'id':d['id'],'uris':[uri],'itemData':d})
        data={'citationID':hashlib.sha256(f'masar-review-{citation_count}'.encode()).hexdigest()[:10], 'properties':{'unsorted':False,'formattedCitation':display,'plainCitation':display,'noteIndex':0},'citationItems':items,'schema':'https://github.com/citation-style-language/schema/raw/master/csl-citation.json'}
        p.append(field_part('begin'));p.append(instruction(' ADDIN ZOTERO_ITEM CSL_CITATION '+json.dumps(data,ensure_ascii=False,separators=(',',':'))+' '));p.append(field_part('separate'))
        for i,k in enumerate(keys):
            if i:p.append(run(', ',color='0000FF'))
            link=el('hyperlink',anchor=bibmarks[k],history='1');link.append(run(f'[{numbers[k]}]',color='0000FF'));p.append(link)
        p.append(field_part('end'))
    def inline(p,vals,bold=False):
        for x in vals:
            t=x['t'];c=x.get('c')
            if t=='Str':p.append(run(c,bold=bold))
            elif t in ('Space','SoftBreak'):p.append(run(' '))
            elif t=='LineBreak':r=el('r');r.append(el('br'));p.append(r)
            elif t=='Cite':citation(p,[v['citationId'] for v in c[0]])
            elif t in ('Strong','Emph','SmallCaps','Superscript','Subscript'):inline(p,c,bold=bold or t=='Strong')
            elif t=='Span':inline(p,c[1],bold)
            elif t=='Quoted':p.append(run('“'));inline(p,c[1]);p.append(run('”'))
            elif t=='Link':
                attr,content,target=c;label=target[0][1:]
                if label in labelnums:
                    link=el('hyperlink',anchor=labelmarks[label],history='1');link.append(run(labelnums[label]));p.append(link)
                else:inline(p,content,bold)
            elif t=='RawInline':raise ValueError('Unconverted LaTeX inline '+str(c))
            else:raise ValueError('Unhandled inline '+t)
    expected=[]
    def remember(p):expected.append(text_of(p))
    def make_blocks(bs):
        out=[]
        for b in bs:
            t=b['t'];c=b.get('c')
            if t=='Header':
                level,attr,vals=c;p=para('Heading'+str(level));inline(p,vals)
                # Hyperlinked numeric cross-references keep the LaTeX-derived display text.
                bookmark(p,labelmarks[attr[0]]);out.append(p);remember(p)
            elif t in ('Para','Plain'):
                p=para();inline(p,c);out.append(p);remember(p)
            elif t=='Div':
                attr,children=c
                for child in children:
                    if child['t']!='Table':out.extend(make_blocks([child]));continue
                    _,caption,colspec,head,bodies,foot=child['c']
                    p=para('TableCaptionCoEKSU');p.append(run('Table 2.'));p.append(field_part('begin'));p.append(instruction(' SEQ Table \\* ARABIC \\s 1 '));p.append(field_part('separate'));p.append(run(labelnums[attr[0]].split('.')[-1]));p.append(field_part('end'));p.append(run(': '))
                    for cb in caption[1]:inline(p,cb['c'])
                    bookmark(p,labelmarks[attr[0]]);p.find('w:pPr',NS).append(el('keepNext'));out.append(p);remember(p)
                    caption_specs.append((labelmarks[attr[0]],text_of(p)))
                    tbl=el('tbl');pr=el('tblPr');pr.append(el('tblStyle',val='PhDTable'));pr.append(el('tblW',w=8504,type='dxa'));pr.append(el('tblLayout',type='fixed'));pr.append(el('tblLook',val='04A0',firstRow='1',lastRow='1',noHBand='1',noVBand='1'));tbl.append(pr)
                    widths=[1500,2400,3104,1500] if len(colspec)==4 else [1600,3452,3452]
                    grid=el('tblGrid')
                    for width in widths:grid.append(el('gridCol',w=width))
                    tbl.append(grid)
                    rows=[(r,True) for r in head[1]]
                    for tb in bodies:rows.extend((r,False) for r in tb[2]+tb[3])
                    rows.extend((r,False) for r in foot[1])
                    for row,ishead in rows:
                        tr=el('tr');trpr=el('trPr');trpr.append(el('cantSplit'))
                        if ishead:trpr.append(el('tblHeader'))
                        tr.append(trpr)
                        for idx,cell in enumerate(row[1]):
                            tc=el('tc');tcp=el('tcPr');tcp.append(el('tcW',w=widths[idx],type='dxa'));tc.append(tcp)
                            for cb in cell[4]:
                                if cb['t'] not in ('Plain','Para'):raise ValueError(cb['t'])
                                cp=para('Normal');inline(cp,cb['c'],bold=ishead);tc.append(cp);remember(cp)
                            if not tc.findall('w:p',NS):tc.append(para('Normal'))
                            tr.append(tc)
                        tbl.append(tr)
                    out.append(tbl)
            else:raise ValueError('Unhandled block '+t)
        return out
    # Identify existing chapter boundaries by their template heading style.
    headings=[p for p in body.findall('w:p',NS) if p.xpath('./w:pPr/w:pStyle[@w:val="Heading1"]',namespaces=NS)]
    intro_heading=next(p for p in headings if text_of(p)=='Introduction')
    lr_heading=next(p for p in headings if text_of(p)=='Literature Review')
    next_heading=headings[headings.index(lr_heading)+1]
    # Add section bookmarks to unchanged introduction headings.
    intro_headers=[b for b in blocks if b['t']=='Header' and b['c'][1][0].startswith('sec:')][:4]
    for b in intro_headers:
        title=''.join(v.get('c','') if v['t']=='Str' else ' ' for v in b['c'][2])
        hp=next(p for p in body.findall('w:p',NS) if text_of(p)==title)
        bookmark(hp,labelmarks[b['c'][1][0]])
    bookmark(intro_heading,labelmarks['ch:introduction'])
    opening=blocks[1];p=make_blocks([opening])[0];intro_heading.addnext(p)
    start=next(i for i,b in enumerate(blocks) if b['t']=='Header' and b['c'][1][0]=='ch:literaturereview')
    new=make_blocks(blocks[start+1:])
    bookmark(lr_heading,labelmarks['ch:literaturereview'])
    i=body.index(lr_heading)+1;j=body.index(next_heading)
    # Preserve the original explicit page break before the following chapter.
    old=list(body)[i:j];breaks=[p for p in old if p.xpath('.//w:br[@w:type="page"]',namespaces=NS)]
    for x in old:body.remove(x)
    for x in new:body.insert(i,x);i+=1
    if breaks:body.insert(i,copy.deepcopy(breaks[-1]))
    else:
        bp=para();rr=el('r');rr.append(el('br',type='page'));bp.append(rr);body.insert(i,bp)
    # Add cached TOC entries using the university's existing TOC2 formatting.
    toc_template=next(p for p in body.findall('w:p',NS) if p.xpath('./w:pPr/w:pStyle[@w:val="TOC2"]',namespaces=NS) and 'Motivation and Scope' in text_of(p))
    toc_lr=next(p for p in body.findall('w:p',NS) if p.xpath('./w:pPr/w:pStyle[@w:val="TOC1"]',namespaces=NS) and 'Literature Review' in text_of(p))
    def nav_paragraph(style_pr,anchor,title):
        np=el('p');np.append(copy.deepcopy(style_pr));link=el('hyperlink',anchor=anchor,history='1');link.append(run(title));rr=el('r');rr.append(el('tab'));link.append(rr);link.append(field_part('begin'));link.append(instruction(' PAGEREF '+anchor+' \\h '));link.append(field_part('separate'));link.append(run('00'));link.append(field_part('end'));np.append(link);return np
    pos=body.index(toc_lr)+1
    for b in blocks[start+1:]:
        if b['t']=='Header' and b['c'][0]==2:
            key=b['c'][1][0];title=''.join(v['c'] if v['t']=='Str' else ' ' for v in b['c'][2]);np=nav_paragraph(toc_template.find('w:pPr',NS),labelmarks[key],labelnums[key]+'  '+title);body.insert(pos,np);pos+=1
    lot=next(p for p in body.findall('w:p',NS) if text_of(p)=='No table of figures entries found.' and p.getprevious() is not None and text_of(p.getprevious())=='List of Tables')
    pos=body.index(lot);lotpr=copy.deepcopy(lot.find('w:pPr',NS));body.remove(lot)
    for idx,(anchor,title) in enumerate(caption_specs):
        np=nav_paragraph(lotpr,anchor,title)
        if idx==0:
            np.insert(1,field_part('begin'));np.insert(2,instruction(' TOC \\h \\z \\c "Table" '));np.insert(3,field_part('separate'))
        if idx==len(caption_specs)-1:np.append(field_part('end'))
        body.insert(pos,np);pos+=1
    # Generate cached IEEE references from the same BibTeX source.
    with tempfile.TemporaryDirectory() as td:
        inp=Path(td)/'in.md';inp.write_text('\n\n'.join('[@'+k+']' for k in order))
        bj=json.loads(subprocess.check_output(['pandoc',str(inp),'--citeproc','--bibliography='+str(root/'references.bib'),'--csl='+a.csl,'-t','json']))
    bibdiv=next(b for b in bj['blocks'] if b['t']=='Div' and b['c'][0][0]=='refs')
    rendered={b['c'][0][0][4:]:b['c'][1] for b in bibdiv['c'][1]}
    bibhead=next(p for p in body.findall('w:p',NS) if text_of(p)=='References')
    append=next(p for p in body.findall('w:p',NS) if text_of(p)=='Appendices')
    i=body.index(bibhead)+1;j=body.index(append)
    tail=list(body)[i:j];breaks=[p for p in tail if p.xpath('.//w:br[@w:type="page"]',namespaces=NS)]
    # Keep original bibliography paragraph properties, including hanging indent.
    oldbib=next(p for p in tail if p.xpath('./w:pPr/w:pStyle[@w:val="Bibliography"]',namespaces=NS))
    for x in tail:body.remove(x)
    for idx,k in enumerate(order):
        p=para('Bibliography');p.remove(p[0]);p.insert(0,copy.deepcopy(oldbib.find('w:pPr',NS)));p.find('w:pPr',NS).append(el('keepLines'))
        if idx==0:p.append(field_part('begin'));p.append(instruction(' ADDIN ZOTERO_BIBL {"uncited":[],"omitted":[],"custom":[]} CSL_BIBLIOGRAPHY '));p.append(field_part('separate'))
        for b in rendered[k]:inline(p,b['c'])
        bookmark(p,bibmarks[k])
        if idx==len(order)-1:p.append(field_part('end'))
        body.insert(i,p);i+=1
    if breaks:body.insert(i,copy.deepcopy(breaks[-1]))
    else:
        bp=para();rr=el('r');rr.append(el('br',type='page'));bp.append(rr);body.insert(i,bp)
    # Existing TOC field can be refreshed in Word without altering template styles.
    settings=E.fromstring(parts['word/settings.xml']);up=settings.find('w:updateFields',NS)
    if up is None:up=el('updateFields');settings.append(up)
    up.set('{'+W+'}val','true')
    parts['word/document.xml']=E.tostring(doc,xml_declaration=True,encoding='UTF-8',standalone=True)
    parts['word/settings.xml']=E.tostring(settings,xml_declaration=True,encoding='UTF-8',standalone=True)
    with ZipFile(a.output,'w',ZIP_DEFLATED) as z:
        for n,v in parts.items():z.writestr(n,v)
    Path(a.audit).write_text(json.dumps({'citations_added':citation_count,'references':len(order),'existing_zotero_sources':len(existing),'new_embedded_sources':len(order)-len(existing),'transferred_text':expected,'label_numbers':labelnums},ensure_ascii=False,indent=2))
    print(f'Transferred {len(new)} blocks; {citation_count} citation fields; {len(order)} references.')

if __name__=='__main__':main()
