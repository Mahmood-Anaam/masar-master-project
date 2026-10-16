# IS595 Introduction Revision Record

> This file records the initial revision. The subsequent final academic review is documented in [IS595-introduction-final-review.md](IS595-introduction-final-review.md); the current chapter source reflects that final review.

## Delivery scope

- Repository: `Mahmood-Anaam/masar-master-project`.
- Source branch: `overleaf`, starting at `61010c368885d5835212072dad07dc034aed68d0`.
- Working branch: `develop`, created from that source commit.
- Revision date: 16 October 2026.
- Deliverable: Chapter 1 only, written in English to preserve the report's existing language.
- Governing local source: `docs/assets/Guidlines.md`, read in full. The supervisor's feedback supplied in the task reiterates its introduction structure.
- The literature review has not been written or expanded. Work on it requires the user's approval after this delivery.

## Academic positioning

This is the non-thesis master's project in Information Systems at King Saud University. IS595 establishes the problem, scope and impact, literature foundation, discussion of anticipated applications, and conclusions. IS597 continues with implementation, testing, and evaluation. The revised introduction consistently describes Masar and TDRP as proposed work and reports no fabricated interviews, datasets, implementation results, or measured benefits.

The existing concept is preserved: Masar is an integrated web-based business continuity decision support system; TDRP is its proposed rule-based method. The chapter does not replace that concept with an AI system or an optimization model. Its proposed contribution is the method's integration with continuity records, traceable outputs, and a dashboard. Novelty relative to existing research remains to be assessed in the literature review.

## Response to the supervisor and university guidance

| Requirement | Revision | Verification in chapter-only PDF |
| --- | --- | --- |
| Motivation/scope, 1–2 pages | Section 1.1 connects service continuity to impact information, defines the principal concepts, identifies users and system boundaries, and separates the two courses. | Pages 1–2. |
| Problem statement, fewer than 3 pages, with IS significance | Section 1.2 identifies derivation, dependency, and information-governance difficulties; states the design question; and explains the IS contribution. | Starts on page 3 and ends on page 5 before Section 1.3; occupies less than 3 pages. |
| Importance and broader picture | Section 1.3 explains planning, coordination, and accountability implications without promising measured operational gains. | Pages 5–6. |
| Objectives: 3–5 sentence summary | Section 1.4.1 contains exactly five sentences: an overall goal and four objectives. | Page 6. |
| Objectives and proposed solution | Section 1.4 adds the conceptual TDRP workflow, repository/dashboard role, study approach, and future evaluation. | Pages 6–8. |
| In-text references | Unsupported numeric fragments in the original are replaced by actual `\cite{...}` commands. Seven distinct references are cited. | All seven citation keys resolve. |
| DOI for each used reference | All seven cited entries have a `doi` field in `references.bib`; the chapter entry point uses `plainnat` so journal DOIs and the NIST DOI URLs appear in the PDF. | Seven entries on reference page 9. |

The 20–30 literature-review pages, 5–10 discussion pages, 2–3 conclusion pages, and 20–30 references specified in the university file apply to the completed IS595 report. This chapter delivery does not claim to fulfill the entire report. Seven relevant references are used here; the later review must establish and verify the full corpus rather than pad this introduction.

## Substantive corrections

1. **MTPD and RTO are not interchangeable.** The revised text distinguishes a service's tolerable interruption from a recovery target for a specified service/resource and required service level.
2. **A high-impact label is not automatically an unacceptable-impact threshold.** TDRP requires an explicit, approved interpretation of the impact matrix.
3. **Threshold observations can imply an interval.** The method must not fabricate an exact crossing time from coarse time bands.
4. **RTO is not automatically feasible.** Candidate targets require review of recovery capability, prerequisites, service resumption activities, and approval.
5. **Candidate and approved requirements are distinct.** The proposal requires explicit status and traceability.
6. **Criticality and recovery precedence differ.** Dependency visibility is required; the output is not claimed to be a resource-feasible recovery schedule.
7. **Missing data must remain visible.** Unreached thresholds, missing assessments, contradictory inputs, cycles, and target conflicts are identified as cases requiring explicit design treatment.
8. **RPO and MBCO remain contextual.** The proposal does not derive acceptable data loss or minimum service capacity from interruption severity alone.
9. **Benefits are prospective.** Reduced retrieval effort and improved consistency are intended evaluation topics, not established findings.
10. **Scope is bounded.** No autonomous incident command, recovery execution, predictive detection, machine learning, simulation, or recovery-schedule optimization is proposed in this delivery.
11. **Method versus research approach.** TDRP is the proposed domain method; design science organizes the project's investigation, construction, and evaluation across the two terms.
12. **No unverified local claims.** The illustrative fragmented-record situation is explicitly an assumed problem setting; no Saudi organizational prevalence, financial loss estimate, or regulatory-compliance claim is invented.

## Files changed

| Path | Purpose |
| --- | --- |
| `chapters/introduction.tex` | Replaces the initial chapter with the revised four-part academic introduction. |
| `references.bib` | Adds the DOI-bearing NIST SP 800-34 Rev. 1 and updated 2025 NIST IR 8286D entries; retains inherited entries. |
| `introduction-review.tex` | Adds a reproducible chapter-only submission entry point, excluding incomplete front matter and the untouched literature-review placeholder. Uses the same chapter and shared layout as the full report. |
| `packages.tex` | Makes the two unused algorithm packages optional with `\IfFileExists`; they were absent in the local TeX installation and blocked compilation. No current chapter uses algorithm environments. |
| `.gitignore` | Excludes the generated chapter PDF; source remains tracked and the compiled PDF is delivered separately. |
| `README.md` | Documents the repository map, build commands, current delivery boundary, and remaining template work. |
| `docs/IS595-introduction-revision.md` | Records requirements mapping, academic decisions, and verification. |
| `docs/IS595-introduction-source-audit.md` | Records the source-to-claim mapping, DOI checks, access limits, and remaining literature-review work. |

The original introduction remains recoverable from the source commit and Git history. No other chapter or front-matter content was rewritten.

## Build and quality verification

Commands, from the repository root:

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error introduction-review.tex
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

- Chapter output: 9 A4 pages, comprising 8 introduction pages and 1 reference page; 12-point Times-style font, double-spaced body, single-spaced references, inherited margins.
- Chapter build: no unresolved citations, unresolved references, overfull boxes, underfull boxes, or BibTeX warnings in the final build.
- Rendered every chapter-output page and visually reviewed the page contact sheet and enlarged pages. Checked section transitions, numbering, reference wrapping, and absence of clipped text.
- Extracted PDF text to check content and section boundaries; no placeholder text is present in the chapter output.
- Full report entry point also compiles. It retains a non-blocking `lipsum` Latin-language warning from inherited placeholder front matter. That full report is not the submission deliverable for this stage.
- No tables or figures are needed for this introduction. The existing `rotating` support remains available for later literature-review tables; no claim is made that future tables have been validated.

## Template findings and remaining work

The inherited `titlepage.pdf` and equivalent Word title template identify Imam Mohammad bin Saud Islamic University and describe a thesis. They must not be submitted for this King Saud University non-thesis project. They are currently commented out in `titlepage.tex` and were preserved, not silently relabeled. The approval page is a generic thesis form and is also inactive.

The active full-report front matter contains placeholder English and Arabic abstracts, acknowledgements, and generic symbols. `chapters/literaturereview.tex` is a placeholder. These materials are excluded by `introduction-review.tex`; they must be replaced or removed in the final complete report. Student ID and supervisor identity have not been supplied, so no cover page with invented information was created.

After approval to continue, the literature review must establish a documented search and screening strategy, obtain lawful full texts, store studies under `docs/studies`, and create one Markdown reading summary per study in a new folder such as `docs/study-notes`. Abstract access or a bibliographic record is insufficient for claiming a full-text reading. The chapter should progress from BCM foundations to BIA, recovery requirements, dependencies, decision support, and methods/systems closest to TDRP; comparative tables must be rendered and checked. These are next-stage requirements, not completed work.
