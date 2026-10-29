# Automated Cybersecurity Impact Propagation across Business Processes Using Process Mining Techniques

## Identity and evidence

**Authors:** Melina Raptaki, George Stergiopoulos, Dimitris Gritzalis. **Publication:** *International Journal of Information Security*, 24, article 129, 2025. **DOI:** https://doi.org/10.1007/s10207-025-01040-0. **BibTeX:** `raptaki2025propagation`. Complete 17-page publisher PDF examined; CC BY 4.0. This extends the authors' 2024 PRIA study; the two publications must not be counted as independent replications.

## Problem, method, and implementation

The study addresses the mismatch between high-level business-process models used in BIA and actual activities recorded in information systems. It uses process mining to reveal process dependencies and propagate a cybersecurity incident's relative impact across them. The output is a scenario-dependent ranking of activities for risk mitigation, rather than a tolerable-disruption calculation from a service's time–impact matrix.

The method has three phases (§3, pp. 4–5): extract a process graph from XES event logs; calculate and normalise transition weights using causality, diffusion, and flow-related features; propagate impact from a selected point of interest (POI). The POI starts at impact 1. Each downstream activity combines its parents' impacts weighted by incoming transitions. Iteration and normalisation address loops so they do not inflate propagated effects indefinitely. When activities are unavailable, the graph and weights are recomputed for the remaining subgraph, with a new POI selected from the most affected available activity.

A dependency-impact threshold of 0.5 flags activities as critical in the case. The threshold is a case choice and the calculated scores are relative to a POI; neither is an independently observed probability of loss nor a generic critical-service class. A Java desktop application incorporates ProM 6.12 import/discovery components, exports rankings as CSV, and exports the weighted graph as JSON (§4.1). Outputs still need association with underlying IT assets to inform organizational security planning.

## Dataset, scenarios, and evaluation

The case uses the 2023 procurement process of an international goods-transportation company. The paper reports 553,763 events, 3,565,326 records, 110,275 process instances, 30 activities, and 108 users, including two background users. Four systems cover ERP, materials/warehouse management, supplier procurement, and invoice processing (§4.2, p. 6).

Scenarios concern an August 2023 ransomware incident affecting requisitions and hypothetical attacks affecting supplier invoices/debit memos during evaluation of a proposed system change. The first case also recomputes rankings after removing unavailable warehouse-system activities. Roughly 20% of nodes exceed the critical threshold in the original first case and 28.6% in its reduced graph; hypothetical invoicing cases flag different subsets (§4.3). These percentages are scenario outputs, not classification accuracy.

Evaluation combines existing process/BIA artefacts, staged interviews with five employees in IT, cybersecurity, process management, and procurement, and comparisons with alternative weighting/propagation approaches (§5). Findings reveal tighter system coupling, skipped quotation steps, and differences between intended and enacted processes. Documented organizational responses include reconsidering mitigation measures, process safeguards, training, and system decoupling. An alternative propagation algorithm fails to terminate on the cyclic graph; interpret this as a compatibility finding in this setup, not evidence that every competing method fails.

## Limitations and reporting cautions

Logged activities define coverage: offline/unlogged activities and attacks on the integrity of the event logs are outside the stated model. One company's procurement data do not establish organization-wide or cross-sector validity. Relative scores must be combined with absolute BIA values; multi-process integration and automated asset association remain future work (§6.1).

The source reports individual execution times of 66, 63, 53, and 58 seconds, while §5.3.4 and the conclusion broadly say results are produced in under a minute. Use the specific measured times and avoid repeating that blanket claim. Its data-availability statement says no datasets were generated or analysed, despite the case analysis described in the body; an open replication dataset is not established. Interviews support contextual plausibility and usefulness, not a measured causal reduction in incident recovery time. The article's general claims that prior work is absent should not be adopted as a current exhaustive literature conclusion.

## Application to Masar's review

**Primary:** §2.4.2 Interdependency Models and §2.5.2 Decision Support in Continuity and Disaster Management. **Secondary:** §§2.2.4, 2.6, 2.7. Use this as a concrete implemented research system and a contrasting data-driven dependency method. It demonstrates that automated, inspectable rankings and dependency analysis predate Masar. TDRP differs in relying on organization-configured impact rules and service recovery requirements, without mining event logs, simulating attack propagation, or deriving a mitigation programme. No evidence here validates TDRP's MTPD/RTO mappings or maximum-criticality inheritance.
