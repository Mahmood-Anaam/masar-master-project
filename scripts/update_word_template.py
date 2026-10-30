#!/usr/bin/env python3
"""Transfer Chapters 1-2 into the university DOCX while preserving Zotero fields."""

from __future__ import annotations

import copy
import json
import os
import re
import shutil
import subprocess
import tempfile
import uuid
import zipfile
from pathlib import Path

from lxml import etree


ROOT = Path(__file__).resolve().parents[1]
DOCX = ROOT / "masar-master-project.docx"
W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
R = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
A = "http://schemas.openxmlformats.org/drawingml/2006/main"
XML = "http://www.w3.org/XML/1998/namespace"
NS = {"w": W, "r": R}


def run(args, *, cwd=ROOT, env=None, input_text=None):
    result = subprocess.run(
        args,
        cwd=cwd,
        env=env,
        input=input_text,
        text=True,
        check=False,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    if result.returncode:
        raise RuntimeError(f"Command failed ({result.returncode}): {' '.join(map(str, args))}\n{result.stderr}")
    return result.stdout


def qn(ns, name):
    return f"{{{ns}}}{name}"


def expand_inputs(text: str) -> str:
    pattern = re.compile(r"\\input\{([^}]+)\}")

    def repl(match):
        target = ROOT / match.group(1)
        if target.suffix == "":
            target = target.with_suffix(".tex")
        if target.exists() and "tables" in target.parts:
            return expand_inputs(target.read_text(encoding="utf-8"))
        return match.group(0)

    return pattern.sub(repl, text)


def label_numbers() -> dict[str, str]:
    aux = (ROOT / "main.aux").read_text(encoding="utf-8", errors="ignore")
    return dict(re.findall(r"\\newlabel\{([^}]+)\}\{\{([^}]*)\}", aux))


def make_figure(tmp: Path) -> Path:
    tex = tmp / "temporal_figure.tex"
    tex.write_text(
        "\\documentclass{standalone}\n"
        "\\usepackage{tikz}\n"
        "\\usepackage{xcolor}\n"
        "\\begin{document}\n"
        f"\\input{{{(ROOT / 'figures/lr_temporal_parameters.tex').as_posix()}}}\n"
        "\\end{document}\n",
        encoding="utf-8",
    )
    env = os.environ.copy()
    env["TEXINPUTS"] = "/workspace/texlive-local/root/usr/share/texlive/texmf-dist//:"
    run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error", tex.name], cwd=tmp, env=env)
    png = tmp / "temporal_figure.png"
    run(["pdftoppm", "-png", "-r", "180", "-singlefile", str(tex.with_suffix('.pdf')), str(png.with_suffix(''))], cwd=tmp)
    return png


def prepare_latex(tmp: Path, figure: Path) -> Path:
    intro = (ROOT / "chapters/introduction.tex").read_text(encoding="utf-8")
    review = expand_inputs((ROOT / "chapters/literaturereview.tex").read_text(encoding="utf-8"))
    text = intro + "\n" + review

    labels = label_numbers()
    text = re.sub(r"\\ref\{([^}]+)\}", lambda m: labels.get(m.group(1), "??"), text)
    text = re.sub(r"\\label\{[^}]+\}", "", text)
    text = re.sub(
        r"\\cite\{([^}]+)\}",
        lambda m: "CITESTART" + "|".join(x.strip() for x in m.group(1).split(",")) + "CITEEND",
        text,
    )
    fig_pat = re.compile(r"\\begin\{figure\}.*?\\caption\{(.*?)\}.*?\\end\{figure\}", re.S)
    text = fig_pat.sub(
        lambda m: f"\\includegraphics[width=0.9\\textwidth]{{{figure.as_posix()}}}\n"
        + "\\paragraph{Figure: " + m.group(1) + "}",
        text,
    )
    text = re.sub(r"\\begin\{(?:sidewaystable|table)\}(?:\[[^]]*\])?", "", text)
    text = re.sub(r"\\end\{(?:sidewaystable|table)\}", "", text)
    text = re.sub(r"\\caption\{(.*?)\}", r"\\paragraph{Table: \1}", text, flags=re.S)
    text = text.replace("\\linewidth", "\\textwidth")
    out = tmp / "chapters12.tex"
    out.write_text(text, encoding="utf-8")
    return out


def paragraph_text(p):
    return "".join(p.xpath(".//w:t/text()", namespaces=NS))


def style_id(p):
    node = p.find("./w:pPr/w:pStyle", namespaces=NS)
    return node.get(qn(W, "val")) if node is not None else ""


def new_run(text, *, blue=False):
    r = etree.Element(qn(W, "r"))
    if blue:
        rpr = etree.SubElement(r, qn(W, "rPr"))
        etree.SubElement(rpr, qn(W, "color")).set(qn(W, "val"), "0000FF")
    t = etree.SubElement(r, qn(W, "t"))
    if text.startswith(" ") or text.endswith(" "):
        t.set(qn(XML, "space"), "preserve")
    t.text = text
    return r


def citation_field(keys, numbers, items):
    shown = ", ".join(f"[{numbers[k]}]" for k in keys)
    citation_items = []
    for key in keys:
        item = copy.deepcopy(items[key])
        item["id"] = numbers[key]
        citation_items.append({"id": numbers[key], "uris": [], "itemData": item})
    payload = {
        "citationID": uuid.uuid4().hex[:8],
        "properties": {"unsorted": False, "formattedCitation": shown, "plainCitation": shown, "noteIndex": 0},
        "citationItems": citation_items,
        "schema": "https://github.com/citation-style-language/schema/raw/master/csl-citation.json",
    }
    out = []
    r = etree.Element(qn(W, "r"))
    etree.SubElement(r, qn(W, "fldChar")).set(qn(W, "fldCharType"), "begin")
    out.append(r)
    r = etree.Element(qn(W, "r"))
    instr = etree.SubElement(r, qn(W, "instrText"))
    instr.set(qn(XML, "space"), "preserve")
    instr.text = " ADDIN ZOTERO_ITEM CSL_CITATION " + json.dumps(payload, separators=(",", ":"), ensure_ascii=False) + " "
    out.append(r)
    r = etree.Element(qn(W, "r"))
    etree.SubElement(r, qn(W, "fldChar")).set(qn(W, "fldCharType"), "separate")
    out.append(r)
    out.append(new_run(shown, blue=True))
    r = etree.Element(qn(W, "r"))
    etree.SubElement(r, qn(W, "fldChar")).set(qn(W, "fldCharType"), "end")
    out.append(r)
    return out


def replace_citations(root, numbers, items):
    marker = re.compile(r"CITESTART([A-Za-z0-9_|.-]+)CITEEND")
    for p in root.xpath(".//w:p", namespaces=NS):
        text = paragraph_text(p)
        if "CITESTART" not in text:
            continue
        ppr = p.find("./w:pPr", namespaces=NS)
        for child in list(p):
            if child is not ppr:
                p.remove(child)
        pos = 0
        for match in marker.finditer(text):
            if match.start() > pos:
                p.append(new_run(text[pos:match.start()]))
            keys = match.group(1).split("|")
            for node in citation_field(keys, numbers, items):
                p.append(node)
            pos = match.end()
        if pos < len(text):
            p.append(new_run(text[pos:]))


def bib_order_and_text():
    bbl = (ROOT / "main.bbl").read_text(encoding="utf-8", errors="ignore")
    matches = list(re.finditer(r"\\bibitem\{([^}]+)\}", bbl))
    order, entries = [], []
    for i, match in enumerate(matches):
        key = match.group(1)
        end = matches[i + 1].start() if i + 1 < len(matches) else bbl.find("\\end{thebibliography}", match.end())
        block = bbl[match.end():end]
        plain = run(["pandoc", "-f", "latex", "-t", "plain"], input_text=block)
        plain = " ".join(plain.replace("\u00a0", " ").split())
        order.append(key)
        entries.append(f"[{i + 1}] {plain}")
    return order, entries


def csl_items():
    raw = run(["pandoc", str(ROOT / "references.bib"), "-t", "csljson"])
    items = {}
    allowed = {
        "id", "type", "title", "author", "editor", "container-title", "publisher", "publisher-place",
        "issued", "volume", "issue", "page", "DOI", "URL", "number", "genre", "note", "event-title",
    }
    for item in json.loads(raw):
        items[item["id"]] = {k: v for k, v in item.items() if k in allowed and v not in (None, "", [])}
    return items


def bibliography_paragraph(text, *, begin=False, end=False, bookmark_id=None, bookmark_name=None):
    p = etree.Element(qn(W, "p"))
    ppr = etree.SubElement(p, qn(W, "pPr"))
    etree.SubElement(ppr, qn(W, "pStyle")).set(qn(W, "val"), "Bibliography")
    if begin:
        r = etree.SubElement(p, qn(W, "r"))
        etree.SubElement(r, qn(W, "fldChar")).set(qn(W, "fldCharType"), "begin")
        r = etree.SubElement(p, qn(W, "r"))
        instr = etree.SubElement(r, qn(W, "instrText"))
        instr.set(qn(XML, "space"), "preserve")
        instr.text = ' ADDIN ZOTERO_BIBL {"uncited":[],"omitted":[],"custom":[]} CSL_BIBLIOGRAPHY '
        r = etree.SubElement(p, qn(W, "r"))
        etree.SubElement(r, qn(W, "fldChar")).set(qn(W, "fldCharType"), "separate")
    if bookmark_id is not None:
        b = etree.SubElement(p, qn(W, "bookmarkStart"))
        b.set(qn(W, "id"), str(bookmark_id))
        b.set(qn(W, "name"), bookmark_name)
    p.append(new_run(text))
    if bookmark_id is not None:
        b = etree.SubElement(p, qn(W, "bookmarkEnd"))
        b.set(qn(W, "id"), str(bookmark_id))
    if end:
        r = etree.SubElement(p, qn(W, "r"))
        etree.SubElement(r, qn(W, "fldChar")).set(qn(W, "fldCharType"), "end")
    return p


def main():
    order, ref_text = bib_order_and_text()
    numbers = {key: i + 1 for i, key in enumerate(order)}
    items = csl_items()
    missing = [key for key in order if key not in items]
    if missing:
        raise RuntimeError(f"Missing CSL data for: {missing}")

    with tempfile.TemporaryDirectory(prefix="masar-word-") as tmp_name:
        tmp = Path(tmp_name)
        figure = make_figure(tmp)
        source = prepare_latex(tmp, figure)
        fragment = tmp / "fragment.docx"
        run([
            "pandoc", str(source), "-f", "latex", "-t", "docx", "--reference-doc", str(DOCX),
            "--resource-path", f"{ROOT}:{tmp}", "-o", str(fragment),
        ])

        with zipfile.ZipFile(DOCX) as zin:
            original = {name: zin.read(name) for name in zin.namelist()}
        with zipfile.ZipFile(fragment) as zin:
            frag_parts = {name: zin.read(name) for name in zin.namelist()}

        doc = etree.fromstring(original["word/document.xml"])
        frag = etree.fromstring(frag_parts["word/document.xml"])
        rels = etree.fromstring(original["word/_rels/document.xml.rels"])
        frag_rels = etree.fromstring(frag_parts["word/_rels/document.xml.rels"])
        body = doc.find("./w:body", namespaces=NS)
        frag_body = frag.find("./w:body", namespaces=NS)

        existing_ids = {rel.get("Id") for rel in rels}
        image_map = {}
        for rel in frag_rels:
            if not rel.get("Type", "").endswith("/image"):
                continue
            old_id = rel.get("Id")
            suffix = Path(rel.get("Target")).suffix or ".png"
            target = f"media/lr_temporal_figure{suffix}"
            new_id_number = 1
            while f"rId{new_id_number}" in existing_ids:
                new_id_number += 1
            new_id = f"rId{new_id_number}"
            existing_ids.add(new_id)
            new_rel = copy.deepcopy(rel)
            new_rel.set("Id", new_id)
            new_rel.set("Target", target)
            rels.append(new_rel)
            source_name = "word/" + rel.get("Target").lstrip("/")
            original["word/" + target] = frag_parts[source_name]
            image_map[old_id] = new_id

        children = list(body)
        start = next(i for i, el in enumerate(children) if el.tag == qn(W, "p") and style_id(el) == "Heading1" and paragraph_text(el).strip() == "Introduction")
        stop = next(i for i, el in enumerate(children) if i > start and el.tag == qn(W, "p") and style_id(el) == "Heading1" and paragraph_text(el).strip().startswith("Methodology"))
        for el in children[start:stop]:
            body.remove(el)

        insert_at = start
        for el in list(frag_body):
            if el.tag == qn(W, "sectPr"):
                continue
            inserted = copy.deepcopy(el)
            for blip in inserted.xpath(".//a:blip", namespaces={"a": A}):
                old_id = blip.get(qn(R, "embed"))
                if old_id in image_map:
                    blip.set(qn(R, "embed"), image_map[old_id])
            body.insert(insert_at, inserted)
            insert_at += 1

        replace_citations(doc, numbers, items)

        children = list(body)
        ref_heading = next(i for i, el in enumerate(children) if el.tag == qn(W, "p") and paragraph_text(el).strip() == "References")
        for el in children[ref_heading + 1:]:
            if el.tag == qn(W, "sectPr"):
                break
            body.remove(el)
        for i, text in enumerate(ref_text):
            body.insert(ref_heading + 1 + i, bibliography_paragraph(
                text,
                begin=i == 0,
                end=i == len(ref_text) - 1,
                bookmark_id=5000 + i,
                bookmark_name=f"Cite_{order[i]}",
            ))

        original["word/document.xml"] = etree.tostring(doc, xml_declaration=True, encoding="UTF-8", standalone="yes")
        original["word/_rels/document.xml.rels"] = etree.tostring(rels, xml_declaration=True, encoding="UTF-8", standalone="yes")

        backup = DOCX.with_suffix(".before-literature-review.docx")
        if not backup.exists():
            shutil.copy2(DOCX, backup)
        out = DOCX.with_suffix(".updated.docx")
        with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as zout:
            for name, data in original.items():
                zout.writestr(name, data)
        out.replace(DOCX)

    print(f"Updated {DOCX}")
    print(f"Inserted {len(order)} Zotero-linked sources and {len(ref_text)} IEEE bibliography entries")


if __name__ == "__main__":
    main()
