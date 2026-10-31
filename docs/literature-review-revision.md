# Literature review revision and Word synchronization

Revision date: 31 October 2026. Base commit: `6d76db5c8bae3979186e22a16fa8138f705b36d0`.

## Scope and alignment

The revision addresses the thesis **A Decision Support System for Business Continuity and Critical Service Recovery Prioritization**. The introduction, title page, existing bibliography, chapter structure, source material, and Word template informed the work. TDRP is treated as the proposed configurable decision procedure and Masar as its software realization. The review does not attribute incident simulation, autonomous recovery decisions, or resource-constrained scheduling to the proposed system.

The repository contains `masar-master-project.docx`, not the `Egypt-master-project.docx` named in the request. The existing repository document was therefore updated in place.

## Problems addressed

The previous chapter contained developed opening sections followed by incomplete sections and prospective descriptions of material still to be written. It did not provide a completed progression from foundational BCM literature to methods, dependency analysis, comparable systems, evaluation, and a defensible research gap. The replacement develops critical comparisons rather than presenting a sequence of source summaries.

The review avoids claiming that temporal impact assessment, configured recovery calculations, or business-derived dependency criticality are absent from existing work. GlobalSuite, ServiceNow, and NIST provide particularly relevant prior art. The resulting gap is an artifact-specific specification and evaluation problem, not a claim that no comparable software exists.

## Chapter structure and substantive changes

| Section | Purpose and contribution |
| --- | --- |
| 2.1 Business continuity management | Establishes continuity objectives, governance, and the roles and limits of standards and government guidance. |
| 2.2 Business impact analysis and recovery requirements | Distinguishes impact, risk, tolerability, MTPD, and RTO; evaluates temporal assessment and supporting BIA studies. |
| 2.3 Service criticality and recovery prioritization | Compares classification, aggregation, ranking, and scheduling; examines assumptions and exceptional inputs. |
| 2.4 Dependency modeling and supporting-resource criticality | Distinguishes recorded relationships, inherited significance, causal propagation, and restoration constraints. |
| 2.5 Decision support systems and comparable applications | Connects DSS foundations and research prototypes to six documented continuity products. |
| 2.6 Research methods and evaluation evidence | Discusses design science, correctness, consistency, sensitivity, practitioner usefulness, transferability, and operational effectiveness. |
| 2.7 Comparative synthesis and research gap | Synthesizes established contributions and defines the bounded contribution proposed for TDRP and Masar. |
| 2.8 Chapter summary | Consolidates implications for subsequent design and evaluation without reporting unperformed experiments. |

The chapter distinguishes researcher inference from reported findings, product documentation from independent evaluations, and proposed evaluation requirements from completed thesis results. A preprint is identified as such. Single-case evidence is not generalized into universal effectiveness claims. Missing product detail is treated as unverified, not as proof that a feature is absent.

## Tables and references

All four tables are included through `\input{}` and reside in `tables/`:

- `lr_standards_comparison.tex`: retained standards and guidance comparison.
- `lr_bia_studies.tex`: rewritten comparison of six research contributions and their limits.
- `lr_tools_comparison.tex`: new comparison of six continuity applications.
- `lr_synthesis.tex`: new synthesis of six decision areas and implications for the project.

Multi-page tables repeat their headers. Column widths were checked in both formats; no table cell content is intentionally hidden. Explicit LaTeX paragraph-column definitions support faithful conversion.

The existing 34-entry bibliography is retained; no fabricated references or DOI values were introduced. Citation keys remain stable. Internal research-workflow notes were replaced with bibliographic or access information. The PRECESION key `elshekeil2017precesion` remains unchanged for compatibility, but its publication data now identify the final 2018 article, volume 4, issue 1, pages 39–47, rather than the 2017 in-press version. Final publication metadata were checked against Crossref.

Evidence work used the repository's primary-source PDFs and research notes, targeted primary-source retrieval, and Paperguide discovery/metadata checks. The GlobalSuite Pre-BIA documentation was checked directly during this revision and its access date updated to 31 October 2026. Existing 29 October access dates remain associated with the earlier source collection; they do not imply that every page was newly retrieved on the revision date. ISO catalogue records are identified as catalogue records, not represented as access to paid full standards. This is a focused narrative review, not a systematic review with a claimed exhaustive search or PRISMA screening process.

LaTeX retains the project's IEEEtran bibliography configuration and uses `\cite{}` for citations. The rewritten chapter contains no `\emph` commands or drafting placeholders.

## Introduction change

An opening overview paragraph was inserted immediately after the chapter label. It introduces the chapter's four sections using `Section~\ref{}` references. The remaining LaTeX introduction text is unchanged.

## Word transfer and template preservation

The transfer script reads the LaTeX content and table inputs through Pandoc's structured representation. It creates Word paragraphs, headings, captions, tables, citations, and cross-references without rewriting the chapter prose. A source-derived audit records the transferred paragraph and table-cell sequence; all 209 nonempty units match the generated Word document.

Existing university styles, numbering definitions, themes, headers, footers, and section properties were preserved. Only `word/document.xml` and `word/settings.xml` change inside the DOCX archive. The transfer uses the existing `NormalCoEKSU`, heading, table, caption, contents, and bibliography styles. Pagination controls keep table rows and bibliography entries together; the next chapter and appendices start on new pages. Contents and table-list entries and their cached page references were updated.

One pre-existing citation error was corrected: the Word introduction paragraph beginning “Assessing the consequences” cited the National Risk Council although the corresponding LaTeX paragraph cites DGA. Its existing citation field now uses the original DGA library item and displays `[2]`. Apart from this citation correction and the requested opening paragraph, the existing introduction prose is preserved.

## Zotero fields and citation linking

The Word document retains the IEEE Zotero document preferences. It contains 102 Zotero citation fields: the eight original fields and 94 new fields. Seven original field payloads remain unchanged; the eighth is the DGA correction described above. Six existing Zotero library records are reused. The additional 28 references carry embedded CSL item data and canonical DOI or source-URL identifiers; the script does not invent Zotero user-library item identifiers.

The [ZoteroCiteLinker repository](https://github.com/sBaydin/ZoteroCiteLinker) was examined. The delivered document implements its visible citation-linking convention: blue citation text linked to the corresponding bibliography bookmarks. There are 109 unique bookmarks and 188 internal hyperlinks, all with valid targets. Citation numbers agree with the 34-entry LaTeX bibliography.

This is a programmatic construction of Zotero-compatible embedded citation fields and internal links. Zotero's integration source supports embedded item-data fallback when a reference is not resolved to a library record. Nevertheless, neither the desktop Zotero Refresh operation nor the installed ZoteroCiteLinker Word macros could be executed in this environment. The additional references have not been imported into the user's personal Zotero library. These distinctions matter: static field/link validation is not a substitute for testing the user's desktop integration.

Before university submission, open a copy in desktop Word, refresh citations with Zotero using IEEE style, resolve or import additional references if prompted, and verify the bibliography. Then run the installed ZoteroCiteLinker linking and blue-color commands and update the contents and table-list fields. Refresh may rewrite citation field results or links. Recheck pagination after this operation; Word and LibreOffice can paginate differently.

## Validation and academic review

- LaTeX compiled successfully through `latexmk`, including BibTeX and repeated cross-reference passes. No undefined citations/references or overfull-box warnings remained. An existing lipsum language warning is unrelated to the rewritten chapter.
- The LaTeX literature review occupies 29 pages (PDF pages 18–46; printed pages 8–36), within the requested 20–30-page range. The complete current LaTeX build has 50 pages.
- The Word render has 54 pages. The literature review occupies 28 pages (PDF pages 18–45), with Chapter 3 starting on page 46. Word's existing front matter and later chapter placeholders account for differences from the current LaTeX build.
- The chapter file has 7,360 whitespace-separated tokens including LaTeX commands, excluding the external table bodies. This is an indicative source count, not an exact prose word count.
- Automated checks verify content-transfer equality, preserved template parts and section properties, citation numbering, balanced field delimiters, unique bookmarks, valid internal link targets, resolved LaTeX labels and citation keys, and absence of known drafting placeholders.
- Rendered pages were visually reviewed for headings, table continuation, complete cells, citations, contents, bibliography, and page breaks. Final checks covered the corrected introduction citation and revised bibliography/appendix pagination.
- Academic review tightened unsupported novelty claims, distinguished ranking from scheduling and inherited class from propagation, and bounded claims about compliance, transferability, and real-incident effectiveness.

The requested chapter has been completed and reviewed. This work does not certify the entire thesis as submission-ready: unrelated front-matter and later-chapter template placeholders remain, and desktop Zotero integration requires the check above.

## Reproduction

The scripts are specific to this repository's template and citation structure, not general-purpose converters. Requirements: Python 3, `lxml`, `PyMuPDF` (navigation updates), Pandoc with citeproc, a TeX distribution providing the project's packages and IEEEtran, and a DOCX renderer such as LibreOffice. Supply the official IEEE CSL style from [citation-style-language/styles](https://github.com/citation-style-language/styles/blob/master/ieee.csl).

Use an unmodified Word file from the base commit as the template; do not pass the generated output back as its own template. Keep intermediate files outside the repository.

```bash
git show 6d76db5c8bae3979186e22a16fa8138f705b36d0:masar-master-project.docx > ../original.docx
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=../latex-build main.tex
python scripts/sync_literature_word.py --template ../original.docx --output masar-master-project.docx --csl ../ieee.csl --audit ../word-transfer.json
# Render the DOCX to ../rendered/masar-master-project.pdf with a DOCX renderer.
python scripts/update_word_navigation.py masar-master-project.docx ../rendered/masar-master-project.pdf
# Render again and verify page references and layout after updating their caches.
python scripts/validate_literature_update.py --template ../original.docx --audit ../word-transfer.json --aux ../latex-build/main.aux
git diff --check
```

In the editing environment, missing `algorithm.sty` and `IEEEtran.bst` were supplied from CTAN in an external temporary TeX search path. No template package changes or downloaded build dependencies were committed.
