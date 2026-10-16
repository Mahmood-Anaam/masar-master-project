# Masar Master's Project

Masar is a proposed web-based business continuity decision support system incorporating **Time-Dependent Recovery Prioritization (TDRP)**, a rule-based method connecting impact assessments, recovery requirements, and dependency-aware service priorities.

This is a **non-thesis master's project in Information Systems at King Saud University**. The current **IS595** work establishes the academic foundation and proposal; **IS597** will cover implementation, testing, and evaluation.

## Current delivery

The `develop` branch was created from `overleaf` at `61010c368885d5835212072dad07dc034aed68d0`. Chapter 1 has been revised against `docs/assets/Guidlines.md` and the supervisor's feedback. The final academic review is recorded in [`docs/IS595-introduction-final-review.md`](docs/IS595-introduction-final-review.md). Chapter 2 is now complete: 25 body pages and two reference pages, with fourteen fully read academic studies and two NIST guidance sources. Its final academic review is documented in [the final review record](docs/IS595-literature-review-final-review.md). Work on the next chapter awaits approval.

Build the chapter-only submissions from the repository root:

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error introduction-review.tex
latexmk -pdf -interaction=nonstopmode -halt-on-error literature-review.tex
```

The outputs are `introduction-review.pdf` and `literature-review.pdf`, each containing the respective chapter and cited references without incomplete front matter. Both entry points use the same chapter sources and shared layout as the main report.

Build the complete report template:

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

**The full report template is not ready for submission.** Its front matter still contains placeholders, and later IS595 sections remain unwritten. The inherited title-page PDF identifies another university and a thesis; it is inactive and must be replaced before final report submission.

## Repository map

| Path | Role and current state |
| --- | --- |
| `main.tex` | Full-report entry point. Includes front matter, introduction, and the completed literature review. Later chapters are commented out. |
| `introduction-review.tex` | Chapter-specific entry point for this delivery; includes only the revised introduction and cited references. |
| `literature-review.tex` | Standalone Chapter 2 entry point, including its cited references. |
| `packages.tex` | Shared layout, fonts, tables, graphics, citations, and utility packages. Algorithm packages load only if installed; no current chapter uses them. |
| `references.bib` | Shared BibTeX database. The two chapters cite 21 distinct sources. Each cited record has a DOI; unused inherited records require review before use. |
| `chapters/introduction.tex` | Revised Chapter 1. |
| `chapters/literaturereview.tex` | Completed Chapter 2 with critical synthesis, three comparison/traceability tables, and a bounded research gap. |
| `chapters/methodology.tex`, `results.tex`, `conclusion.tex`, `AppendixA.tex` | Inactive template content; final IS595 structure must follow the university guidelines rather than adopt these headings automatically. |
| `titlepage.tex`, `abstract.tex`, `acknowledgements.tex`, `acronyms.tex`, `symbols.tex` | Full-report front matter. Several files retain template text and need later alignment. |
| `arabicabstract.tex`, `arabicabstract.pdf` | Standalone Arabic abstract template and its precompiled PDF. Compile with XeLaTeX and Amiri when authoring the final Arabic abstract; current content is a placeholder. |
| `titlepage.doc`, `titlepage.pdf`, `thesisapproval.pdf` | Inherited Word/PDF templates; not valid final submission pages for this project. Title/approval inclusions are currently commented out. |
| `figures/`, `tables/` | Reserved asset folders, currently empty apart from tracking files. |
| `docs/assets/Guidlines.md` | University guidelines for IS595 and IS597. |
| `docs/IS595-introduction-revision.md` | Detailed revision, requirements mapping, validation, and remaining work. |
| `docs/IS595-introduction-source-audit.md` | Introduction source-to-claim audit and access limitations. |
| `docs/studies/`, `docs/study-notes/` | Sixteen original source PDFs with provenance/licence manifests and sixteen individual critical reading notes. |
| `docs/IS595-literature-review-search-protocol.md` | Review approach, selection record, exclusions and limitations. |
| `docs/IS595-literature-review-completion.md` | Chapter 2 requirements mapping, content changes, verification and delivery boundary. |
| `.github/workflows/build-latex.yml` | Manually triggered GitHub Actions workflow compiling `main.tex`; it does not currently build the chapter-only entry point. |
| `.gitignore` | Excludes TeX build products and intermediate/output directories. |

## Toolchain

Use a TeX Live installation with `latexmk`, pdfLaTeX, BibTeX, Times-compatible fonts, and the packages declared in `packages.tex`. The Arabic abstract additionally needs XeLaTeX, `polyglossia`, and Amiri. No application code, backend, or database is implemented in the current stage.

The chapter delivery was compiled with TeX Live 2023 and visually checked after PDF rendering. See the revision record for page limits, citation checks, and the distinction between proposed benefits and future evaluation.
