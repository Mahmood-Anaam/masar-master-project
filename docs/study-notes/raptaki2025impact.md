# Raptaki, Stergiopoulos and Gritzalis (2025): Process-aware impact propagation

- **DOI:** https://doi.org/10.1007/s10207-025-01040-0
- **Full text:** `../studies/raptaki2025impact.pdf`, 17 pages; complete reading, 16 October 2026.
- **Design:** Implemented Java/ProM-based tool; procurement-process case, alternative graph weightings, propagation baseline, and interviews with five organizational specialists.
- **Evidence:** Method/input/threat model, Sections 3–4; case tables, pp. 7–10; evaluation and limits, Sections 5–6.1.

## Findings and critique

PRIA constructs weighted activity graphs from XES event logs and calculates relative impact propagation from a point of interest. The case reports 553,763 events, 3,565,326 records, and 30 activities. The implementation supports unavailable-activity subgraphs and exports CSV/JSON results. Expert feedback identifies differences between documented workflows and observed execution.

The study is a particularly close functional comparator: dependencies, criticality, rankings, and explanation-relevant outputs already exist in prior work. Its relative propagation score is not elapsed outage tolerance, a recovery deadline, or MTPD. The 0.5 criticality threshold is case-configured, not universal. Unlogged activities and log integrity constrain coverage. Single-process/single-organization evaluation limits generalization. Execution-time claims are internally uneven (the case includes 63/66-second runs whereas summary prose says under a minute); exact speed superiority should not be repeated. A generic data-availability statement also conflicts with the detailed case description, limiting reproducibility.

## Implication for Masar

Document dependency meaning and input completeness. Differentiate configured impact-over-time rules from process-mined propagation. Evaluate explanations and target derivation explicitly; do not claim that Masar introduces automated dependency-aware ranking for the first time.
