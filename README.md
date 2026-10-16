# Masar Master's Project

Masar is a proposed web-based business continuity decision support system incorporating **Time-Dependent Recovery Prioritization (TDRP)**, a rule-based method connecting impact assessments, recovery requirements, and dependency-aware service priorities.

This is a **non-thesis master's project in Information Systems at King Saud University**. The current **IS595** work establishes the academic foundation and proposal; **IS597** will cover implementation, testing, and evaluation.

## Current delivery

The `develop` branch was created from `overleaf` at `61010c368885d5835212072dad07dc034aed68d0`. Chapter 1 has been revised against `docs/assets/Guidlines.md` and the supervisor's feedback. The final academic review is recorded in [`docs/IS595-introduction-final-review.md`](docs/IS595-introduction-final-review.md). Work on the literature review is paused pending the user's approval.

Build the chapter-only submission from the repository root:

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error introduction-review.tex
```

The result is `introduction-review.pdf`: the revised introduction and its cited references, without incomplete front matter or chapter placeholders. The chapter uses the same source and shared layout as the main report.

Build the complete report template:

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

**The full report template is not ready for submission.** Its front matter and literature review still contain placeholders. The inherited title-page PDF identifies another university and a thesis; it is inactive and must be replaced before final report submission.

## Repository map

| Path | Role and current state |
| --- | --- |
| `main.tex` | Full-report entry point. Includes front matter, introduction, and the literature-review placeholder. Later chapters are commented out. |
| `introduction-review.tex` | Chapter-specific entry point for this delivery; includes only the revised introduction and cited references. |
| `packages.tex` | Shared layout, fonts, tables, graphics, citations, and utility packages. Algorithm packages load only if installed; no current chapter uses them. |
| `references.bib` | Shared BibTeX database. The introduction cites seven verified records; unused inherited records require review before use. |
| `chapters/introduction.tex` | Revised Chapter 1. |
| `chapters/literaturereview.tex` | Untouched placeholder, reserved for the approved next stage. |
| `chapters/methodology.tex`, `results.tex`, `conclusion.tex`, `AppendixA.tex` | Inactive template content; final IS595 structure must follow the university guidelines rather than adopt these headings automatically. |
| `titlepage.tex`, `abstract.tex`, `acknowledgements.tex`, `acronyms.tex`, `symbols.tex` | Full-report front matter. Several files retain template text and need later alignment. |
| `arabicabstract.tex`, `arabicabstract.pdf` | Standalone Arabic abstract template and its precompiled PDF. Compile with XeLaTeX and Amiri when authoring the final Arabic abstract; current content is a placeholder. |
| `titlepage.doc`, `titlepage.pdf`, `thesisapproval.pdf` | Inherited Word/PDF templates; not valid final submission pages for this project. Title/approval inclusions are currently commented out. |
| `figures/`, `tables/` | Reserved asset folders, currently empty apart from tracking files. |
| `docs/assets/Guidlines.md` | University guidelines for IS595 and IS597. |
| `docs/IS595-introduction-revision.md` | Detailed revision, requirements mapping, validation, and remaining work. |
| `docs/IS595-introduction-source-audit.md` | Introduction source-to-claim audit and access limitations. |
| `.github/workflows/build-latex.yml` | Manually triggered GitHub Actions workflow compiling `main.tex`; it does not currently build the chapter-only entry point. |
| `.gitignore` | Excludes TeX build products and intermediate/output directories. |

## Toolchain

Use a TeX Live installation with `latexmk`, pdfLaTeX, BibTeX, Times-compatible fonts, and the packages declared in `packages.tex`. The Arabic abstract additionally needs XeLaTeX, `polyglossia`, and Amiri. No application code, backend, or database is implemented in the current stage.

The chapter delivery was compiled with TeX Live 2023 and visually checked after PDF rendering. See the revision record for page limits, citation checks, and the distinction between proposed benefits and future evaluation.
