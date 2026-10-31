#!/usr/bin/env python3
"""Update cached PAGEREF results from a rendered PDF, retaining Word fields/styles."""
import argparse,re
from zipfile import ZipFile, ZIP_DEFLATED
from lxml import etree as E
import fitz
W='http://schemas.openxmlformats.org/wordprocessingml/2006/main';NS={'w':W}
def norm(s):return ' '.join(s.split()).casefold()
def main():
 ap=argparse.ArgumentParser();ap.add_argument('docx');ap.add_argument('pdf');a=ap.parse_args()
 pdf=fitz.open(a.pdf);outlines=pdf.get_toc();pages=[norm(p.get_text()) for p in pdf]
 with ZipFile(a.docx) as z:parts={n:z.read(n) for n in z.namelist()}
 doc=E.fromstring(parts['word/document.xml']);mapping={}
 for bm in doc.xpath('//w:bookmarkStart',namespaces=NS):
  p=bm.getparent()
  if p.tag!='{'+W+'}p':continue
  title=norm(''.join(p.xpath('.//w:t/text()',namespaces=NS)));anchor=bm.get('{'+W+'}name')
  hits=[pg for _,t,pg in outlines if norm(t)==title or norm(t).endswith(' '+title)]
  if title.startswith('table 2.'):
   prefix=title.split(':')[0]+':'
   hits=[i+1 for i,p in enumerate(pages) if prefix in p]
  if hits:mapping[anchor]=hits[-1]
 count=0
 for ins in doc.xpath('//w:instrText',namespaces=NS):
  m=re.match(r'\s*PAGEREF\s+(\S+)',ins.text or '')
  if not m:continue
  anchor=m[1]
  if anchor not in mapping:raise ValueError('Missing page target: '+anchor)
  r=ins.getparent();separated=False
  for nxt in r.itersiblings():
   chars=nxt.xpath('.//w:fldChar/@w:fldCharType',namespaces=NS)
   if 'separate' in chars:separated=True;continue
   if 'end' in chars:break
   if separated:
    ts=nxt.findall('.//w:t',NS)
    if ts:ts[0].text=str(mapping[anchor]);count+=1;break
 parts['word/document.xml']=E.tostring(doc,xml_declaration=True,encoding='UTF-8',standalone=True)
 with ZipFile(a.docx,'w',ZIP_DEFLATED) as z:
  for n,v in parts.items():z.writestr(n,v)
 print('Updated',count,'cached page references; PDF pages:',len(pdf))
 print('Chapter boundaries:',[v for v in outlines if v[0]==1])
if __name__=='__main__':main()
