# Literature Review Revision and Word Transfer

## Scope

This document records the work completed on Chapters 1 and 2 of the Masar master's project on 30 October 2026. The project title is **A Decision Support System for Business Continuity and Critical Service Recovery Prioritization**. The chapter revision was aligned with the proposed Time-Dependent Recovery Prioritization (TDRP) methodology and its implementation in the Masar decision support system.

## Source and repository review

The following project material was reviewed before drafting:

- `titlepage.tex` for the project title, program, author, supervisor, and submission context;
- `chapters/introduction.tex` for the research problem, scope, objectives, proposed methodology, and intended system boundary;
- the previous `chapters/literaturereview.tex`, which contained complete BCM and BIA material but unfinished prioritization, dependency, DSS, methods, synthesis, and summary sections;
- `references.bib`, the evidence map, search-and-selection record, bilingual source summaries, and similar-systems survey;
- the existing university Word template and its Zotero field-code structure.

The literature search is described in the chapter as focused and purposive, not systematic or exhaustive. Existing verified full-text sources were preferred. A final exploratory Paperguide search used complementary queries for temporal BIA, continuity decision support, service interdependency, and rule-based analysis. It identified the ReDRiSS study by Schätter et al.; its metadata and abstract were verified, and the chapter explicitly limits its use to abstract-supported claims because full text was not available.

## Chapter 1 change

An opening overview paragraph was added immediately after the Introduction chapter heading. It describes the purpose of the chapter and points readers to the four sections using `Section~\ref{}` references:

1. Motivation and Scope;
2. Problem Statement and Significance for Information Systems;
3. Importance of the Problem and the Big Picture; and
4. Objectives and Proposed Solution.

No substantive claim in the existing Introduction was altered.

## Chapter 2 structure and content

The Literature Review was completed in a broad-to-specific order:

1. Business Continuity Management;
2. Business Impact Analysis;
3. Service Criticality and Recovery Prioritization;
4. Dependency Modeling;
5. Decision Support Systems for Business Continuity;
6. Research Methods and Evaluation;
7. Synthesis and Research Gap; and
8. Chapter Summary.

The completed chapter contains approximately 10,400 words and renders as 34 pages in the compiled thesis, including three landscape tables, one portrait table, and one figure. The length is slightly above the common 20–30-page range because the rendered count includes four full-page evidence/comparison tables and the temporal-parameter figure.

### Main analytical revisions

- Replaced the placeholder review-scope paragraph with an explicit account of the search concepts, source types, selection boundaries, abstract-only use, and limitations.
- Distinguished service criticality, relative recovery priority, and executable recovery sequencing.
- Compared multi-criteria, rule-based, optimization, probabilistic, process-mining, and temporal-matrix approaches without treating their outputs as interchangeable.
- Added explicit discussion of threshold equality, missing assessments, non-monotonic values, discrete time intervals, and cases in which an unacceptable threshold is never reached.
- Distinguished direct service dependencies, infrastructure interdependencies, criteria dependencies, and shared supporting resources.
- Positioned criticality inheritance as prior art and the maximum-over-supported-services policy as a TDRP design decision to be evaluated rather than a requirement imposed by standards.
- Separated readiness assessment, loss quantification, priority derivation, resource allocation, and recovery scheduling as different decision-support purposes.
- Compared ServiceNow, GlobalSuite, GRASP, Fusion, Riskonnect, verinice, and QuantTM using only functions documented in reviewed material.
- Framed the research gap narrowly around the integration and disclosure of service-first temporal rules, exceptional-case handling, shared-dependency aggregation, and traceability. The chapter does not claim that temporal BIA, dependency inheritance, or BCM automation is unprecedented.
- Derived an evaluation strategy covering rule correctness, boundary cases, configuration sensitivity, repeatability, traceability, and practitioner-oriented usability, while avoiding unsupported claims about real-incident effectiveness.

## Tables, figure, and bibliography

Two new LaTeX table files were added:

- `tables/lr_systems_comparison.tex` compares documented functions and evidence boundaries of related systems;
- `tables/lr_evidence_synthesis.tex` maps evidence themes to artifact implications and unresolved limitations.

The existing standards table, analytical-studies table, and temporal-parameters figure were retained and integrated into the completed argument. The new Schätter et al. record was added to `references.bib` with DOI `10.1016/j.dss.2018.12.006`, and its abstract-only evidence record was added at `docs/sources/schatter2019decision.md`.

All 35 citation keys used by Chapters 1 and 2 resolve in `references.bib`. The bibliography is generated with `IEEEtran` and includes DOI or stable source URLs where available.

## Word-template transfer and Zotero fields

The Introduction and Literature Review were transferred into `masar-master-project.docx` using the existing university styles (`Heading1`, `Heading2`, `Heading3`, `NormalCoEKSU`, and `Bibliography`). The remaining template chapters and front matter were preserved. The chapter's four tables and temporal figure were inserted into the Word document.

The transfer script at `scripts/update_word_template.py` preserves the document's Zotero preference property and creates Word `ADDIN ZOTERO_ITEM CSL_CITATION` fields for every citation. It also creates one `ADDIN ZOTERO_BIBL ... CSL_BIBLIOGRAPHY` field containing all 35 IEEE-formatted visible entries. Citation results are blue, matching the existing citation-field appearance and remaining compatible with a later Zotero refresh and ZoteroCiteLinker pass in Microsoft Word. Each bibliography entry also has a stable bookmark. The script creates a pre-transfer backup when run, but that generated backup is not tracked in the repository.

The DOCX package was validated as a ZIP/OOXML archive and rendered successfully to a 55-page PDF with LibreOffice. Because Microsoft Word, the user's Zotero library, and the ZoteroCiteLinker add-in are not available in this environment, a final Zotero **Refresh** and ZoteroCiteLinker execution should be performed in Word before university submission. This limitation does not affect the embedded field codes or visible IEEE citations, but only Word-side reconciliation with the user's local Zotero library and hyperlink add-in.

## Validation

- LaTeX compilation completed successfully with `latexmk`, `pdflatex`, BibTeX, and the `IEEEtran` bibliography style.
- The compiled thesis contains 56 pages; the Literature Review spans thesis pages 8–41.
- No citation key or section/table/figure reference is unresolved.
- The DOCX contains 156 Zotero citation fields, one Zotero bibliography field, 35 bibliography entries, five Word tables in total, and the temporal-parameter image.
- The updated DOCX passed archive-integrity checks and converted successfully to PDF.

The LaTeX build uses the repository's local TeX Live package tree for the `algorithm`, `algorithmic`, and `IEEEtran` files that are not present in the base system installation. No package files were added to the project.
