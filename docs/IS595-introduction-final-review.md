# IS595 Introduction: Final Academic Review

**Date:** 16 October 2026  
**Branch:** `develop`  
**Reviewed baseline:** `cd0669b2016cf4e79eb07a9aeaf6b7fe92fb486d`  
**Status:** Final chapter revision for the current IS595 submission stage. This status concerns Chapter 1; it does not imply supervisor approval or completion of the full IS595 report.

## Review outcome

The introduction has been reviewed and revised for conceptual accuracy, argument structure, consistency of terminology, alignment between the problem and objectives, evidence attribution, scope feasibility, and typeset presentation. The final version preserves Masar and its TDRP method while making the progression from continuity needs to the proposed system more direct.

## Changes from the reviewed baseline

1. Reworked the opening to connect organizational services, supporting resources, BCM, and the project's information-management focus.
2. Defined MTPD as a duration beyond which interruption causes unacceptable consequences. Distinguished it from the RTO planning target and the data-oriented RPO.
3. Introduced the time-dependent impact profile before presenting TDRP. Explicitly clarified that the method concerns changes in assessed consequences with outage duration, rather than live incident monitoring or prediction.
4. Consolidated the problem around three linked issues: derivation of recovery requirements, dependencies, and integrity of supporting information. Retained one guiding design question.
5. Strengthened the explanation of the IS contribution through the relationship between the repository, decision logic, user responsibilities, and dashboard.
6. Removed repeated declarations about unimplemented features and unproven benefits. Preserved the necessary qualifications where they affect interpretation or evaluation.
7. Refined the objectives into a five-sentence paragraph: overall aim and four objectives, mapped to information requirements, the method, information presentation, and evaluation.
8. Kept TDRP conceptual: candidate MTPD, reviewed RTO, relative priorities, explicit exceptions, and dependency visibility. No numerical thresholds, validation outcomes, or unsupported novelty claims were invented.
9. Separated the domain method (TDRP) from the research approach (design science). Retained implementation and evaluation in IS597.
10. Made the evaluation account more precise by distinguishing rule-output checks, traceability checks, practitioner/user review, and a possible equivalent-case comparison with manual work.
11. Added shared LaTeX widow/orphan penalties to prevent a single opening or closing paragraph line from appearing alone at a page boundary. Resolved two overfull lines by editing the prose rather than shrinking text or widening margins.

## Requirements and page verification

| University/supervisor requirement | Final location | Result |
| --- | --- | --- |
| Motivation and scope: 1–2 pages | Section 1.1, pages 1–2 | Met. |
| Problem statement and IS significance: fewer than 3 pages | Section 1.2, starts page 3 and ends in the upper part of page 5 | Met; less than 3 pages of occupied content. |
| Importance and broader perspective | Section 1.3, pages 5–6 | Met. |
| Objectives: 3–5 sentences | Section 1.4.1, page 6 | Five sentences. |
| Objectives and proposed solution | Section 1.4, pages 6–8 | Includes the proposed system, conceptual method, study approach, and intended evaluation. |
| Supporting in-text citations | Throughout Chapter 1 | Seven unique `\cite` keys, all resolved. |
| DOI for used references | `references.bib`; reference page 9 | All seven cited entries have DOI fields; the reference output exposes the identifiers. |
| Implementation deferred to IS597 | Sections 1.1 and 1.4.3 | No implementation, testing, participant findings, or measured benefits are presented as completed work. |

## Evidence review

The final chapter retains the same seven sources and uses them within the bounds documented in `docs/IS595-introduction-source-audit.md`. Relevant NIST BIA/recovery material and the journal's DSRM description were revisited during this review. Broad source-based statements remain separate from proposed Masar design choices. This revision does not claim full-text reading of all cited papers and does not constitute the literature-review reading archive.

The inherited bibliography has not been globally validated. Uncited entries are not evidence of reading or endorsement. No new references were added simply to increase the reference count; the university's 20–30-reference expectation applies to the completed IS595 report.

## Final technical and visual checks

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error introduction-review.tex
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

- Both entry points compile successfully.
- Final chapter PDF: **9 A4 pages**, comprising **8 introduction pages and 1 reference page**.
- No unresolved citations/references, BibTeX warnings, overfull boxes, or underfull boxes in the chapter build.
- All seven citation keys exist and have nonempty DOI fields; the objectives paragraph contains exactly five sentences.
- All extracted text blocks lie within page bounds.
- Every final PDF page was rendered and visually inspected, with enlarged inspection of the opening and reference pages. No clipped text, overlapping elements, broken references, or placeholder content appears in the chapter deliverable.
- The full-report template still contains inherited placeholders and its existing non-blocking `lipsum` language warning. It remains separate from this chapter-only submission.

## Files in this revision

- `chapters/introduction.tex`: final academic and editorial revision.
- `packages.tex`: paragraph widow/orphan controls.
- `docs/IS595-introduction-final-review.md`: this final review record.
- `docs/IS595-introduction-revision.md`: pointer to the final review, preserving the earlier revision history.
- `README.md`: pointer to the final review.

The reproducible submission entry point remains `introduction-review.tex`. The separately delivered PDF is named `masar-master-project_develop_chapter-01-introduction-final.pdf`. Chapter 2 remains untouched pending explicit approval to begin the literature review.
