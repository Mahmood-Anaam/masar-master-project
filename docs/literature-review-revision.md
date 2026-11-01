# Literature review revision and Word synchronization

Revision date: 1 November 2026. Repository baseline: `8747ac3` on `main`. Working branch: `chapter/literaturereview`.

## Scope and academic alignment

The revision addresses **A Decision Support System for Business Continuity and Critical Service Recovery Prioritization**, a master's project in Information Systems. The repository structure, title page, introduction, bibliography, existing review, evidence records, and actual Word document were inspected before editing. The introduction identifies TDRP as the proposed configurable methodology and Masar as its web-based DSS. The revised review preserves that distinction and the project's service-first scope.

The baseline already contained a developed English review and an introductory overview in LaTeX. The current Word file, however, still contained the earlier Chapter 2 material, eight original Zotero citations, and a different citation in one introductory paragraph. The historical revision notes described a different Word filename and could not be used as evidence that the current file had been synchronized. This revision updates the actual `masar-master-project-report.docx`.

## Academic appraisal and complete rewrite

The previous review had a defensible broad-to-specific structure and appropriate caution about novelty. Its weaknesses were repetition of the project's limitations across several sections, uneven separation of assessment objects and decision outputs, and limited comparative coverage in the research table. The replacement rewrites the chapter throughout, retaining useful section labels and the established evidence base.

| Section | Revised contribution |
| --- | --- |
| 2.1 Business Continuity Management | Establishes organizational outcomes, governance, international guidance, and the Saudi service-oriented context. |
| 2.2 Business Impact Analysis and Recovery Requirements | Compares assessment objects, elicitation evidence, temporal resolution, incomplete observations, tolerability, and recovery targets. |
| 2.3 Service Criticality and Recovery Prioritization | Distinguishes classes and relative urgency; compares compensatory, fuzzy, probabilistic, and explicit temporal rules; separates ranking from scheduling. |
| 2.4 Dependencies and Supporting Resource Criticality | Separates recorded support, common exposure, propagation, inherited classes, and resource recovery deadlines. |
| 2.5 Decision Support Systems and Comparable Applications | Connects practitioner explanations to research prototypes and six documented continuity platforms. |
| 2.6 Research Methods and Evaluation Evidence | Relates design science to method specification, implementation correctness, sensitivity, usefulness, and transferability. |
| 2.7 Comparative Synthesis and Research Gap | Defines a bounded specification and evaluation contribution in light of close existing prior art. |
| 2.8 Chapter Summary | Consolidates the literature-derived basis for subsequent design and evaluation. |

The review does not claim that temporal BIA, configurable recovery calculations, or business-derived resource criticality are new. GlobalSuite and ServiceNow are close computational precedents. NIST supports business-derived criticality. The gap concerns the specification and evaluation of TDRP's particular service-level transformation, exceptional states, priorities, and dependency policy. Neither prototype correctness nor a user exercise is represented as evidence of improved performance during real incidents.

The editorial pass checked terminology, attribution, transitions, repetition, scope, and the distinction between reported evidence and project implications. The chapter consistently describes a master's project. No experiment, effect size, quotation, or DOI was invented. The QuantTM version is identified as a preprint. A focused narrative review is claimed; an exhaustive systematic search is not.

## Sources and bibliography

The existing 34-entry bibliography and citation keys are retained. The chapter uses the repository's accessible primary PDFs, relevant source passages, and existing access/appraisal records. The previously documented access limitations remain applicable: notably, the Torabi 2014 paper is retained in the introduction without reconstructing detailed findings from unread full text.

Targeted external checks on 1 November 2026 covered the official ISO 22301, ISO 22313, and ISO/TS 22317 catalogue records, the GlobalSuite Pre-BIA help page, ServiceNow's Yokohama RTO/RPO documentation, GRASP assessment documentation, and the verinice BCM description. These checks confirmed the bounded functional comparisons. They do not constitute new full-text reading of every cited work or a controlled product trial. Existing bibliography access dates describe the earlier source collection and are not silently relabeled.

LaTeX retains `IEEEtran` and uses `\cite{}`. Public catalogue records support scope statements rather than clause-level claims about paid standards. Provider pages support disclosed functions rather than independent effectiveness. Unreported functionality remains unverified rather than being labeled absent.

## Tables and figure

Four chapter tables remain separate `.tex` files under `tables/` and are included through `\input{}`. The research comparison, `lr_bia_studies.tex`, was redesigned as a four-column landscape page comparing eight studies by object, evidence/method, output, and evaluation. It uses `pdflscape` with a `longtable`, repeated headers, flexible row heights, and single spacing. This provides a landscape PDF page rather than requiring readers to rotate a portrait page manually. Other tables retain the existing portrait arrangement.

The author-created conceptual diagram is `figures/lr_decision_chain.png`, with an editable SVG and a reproduction script. It connects organizational policy and temporal service assessment to recovery requirements, relative service priority, and dependency criticality. Its caption explicitly identifies it as a synthesis, not empirical results. The same image and caption are transferred to Word. No decorative or externally copied imagery was added.

## Introduction

The existing overview was replaced with a clearer opening paragraph referring to the four introduction sections through `Section~\ref{}`. The remainder of the LaTeX introduction was preserved. The Word opening is generated from the same source. A pre-existing Word-only DGA mis-citation was corrected using the original DGA Zotero item; the remaining introductory prose was preserved.

## Word template and exact transfer

The source-derived transfer uses Pandoc's structured representation of the LaTeX paragraphs, headings, citations, captions, references, and external tables. It does not paraphrase the English text. The audit compares 224 nonempty paragraph/table-cell units with the DOCX. Citation numbers are checked against the compiled LaTeX bibliography.

University styles, numbering, font definitions, theme, headers, footer assets, and margins are preserved. The only added layout is an isolated landscape section for the research table, followed by portrait pages. The template's first-page header behavior is retained on the original first section rather than being repeated after each section break. Figure and table captions use the existing university styles. Table rows can expand and repeat their header across pages.

The only replaced existing DOCX archive parts are `word/document.xml`, `word/settings.xml`, `word/_rels/document.xml.rels`, and `[Content_Types].xml`; one PNG media part is added. Styles and numbering parts remain byte-for-byte unchanged. Native REF fields carry numeric section/table/figure references, and PAGEREF caches are updated from the rendered document. Contents, figure list, table list, and later chapter page references are updated accordingly.

## Zotero and ZoteroCiteLinker

The document retains IEEE Zotero preferences and contains 92 Zotero citation fields: eight original fields and 84 generated fields. Seven original payloads are unchanged; the DGA correction accounts for the eighth. Six original library items are reused. The other 28 references use embedded CSL item metadata with canonical DOI/source URIs. No personal Zotero library identifiers were fabricated, and no new items were imported into the user's Zotero library.

The [ZoteroCiteLinker README](https://github.com/sBaydin/ZoteroCiteLinker) was inspected. The document provides blue citation text and hyperlinks to bibliography bookmarks, alongside Zotero ADDIN citation and bibliography fields. Static checks confirm balanced field delimiters, unique bookmarks, valid hyperlink targets, and matching reference numbers.

**Desktop integration remains untested.** This environment cannot execute the installed Word macro or the desktop Zotero Refresh operation. Programmatically embedded citation fields are not proof of successful resolution to the user's live Zotero library. In a copy opened in desktop Word, use Zotero Refresh, resolve/import references if prompted, then run ZoteroCiteLinker Link All Citations and its blue-color command. Recheck bibliography, links, navigation, and pagination after Refresh, which can replace field results and links.

## Reproduction and checks

Use the original DOCX from baseline `8747ac3` as input; do not feed the generated document back as its own template. Required dependencies include the packaged Python runtime with `lxml`, `python-docx`, Matplotlib, and PyMuPDF; Pandoc with citeproc; the official IEEE CSL style; TeX packages including IEEEtran and pdflscape; and a DOCX renderer.

```bash
git show 8747ac3:masar-master-project-report.docx > /tmp/masar-template.docx
python scripts/draw_literature_figure.py
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=/tmp/masar-latex main.tex
python scripts/sync_literature_word.py --template /tmp/masar-template.docx --output masar-master-project-report.docx --csl /tmp/ieee.csl --audit /tmp/masar-transfer.json
# Render the document, preserving the DOCX as the editable deliverable.
python scripts/update_word_navigation.py masar-master-project-report.docx /tmp/rendered/masar-master-project-report.pdf
# Render again after updating cached page references.
python scripts/validate_literature_update.py --template /tmp/masar-template.docx --audit /tmp/masar-transfer.json --aux /tmp/masar-latex/main.aux
git diff --check
```

Final checks passed: the LaTeX review occupies 28 pages (PDF pages 18–45, printed pages 8–35); the Word review occupies 27 pages (rendered pages 15–41). The complete LaTeX and Word renders contain 49 and 50 pages respectively. Each has one landscape comparison page. LaTeX has no undefined citation/reference or overfull-box warnings; an existing lipsum language warning and pre-existing front-matter PDF warnings remain outside this change. The DOCX audit verifies 224 transferred units, 92 citation fields, 34 bibliography entries, 115 unique bookmarks, 181 valid internal hyperlinks, balanced field delimiters, and preserved styles/numbering. Rendering was repeated after page-reference updates; visual review covered layout, tables, figure, bibliography, cross-references, and navigation. An initial rendering failure on the untouched template was diagnosed from the renderer logs as an out-of-memory termination; rendering the completed document succeeded. The overall report still contains pre-existing abstract and later-chapter placeholders outside this task. Completion of the requested chapter does not certify those unrelated sections as submission-ready.
