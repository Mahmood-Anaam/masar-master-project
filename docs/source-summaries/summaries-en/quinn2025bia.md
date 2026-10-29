# Using Business Impact Analysis to Inform Risk Prioritization and Response

## Identity, version and coverage
Stephen D. Quinn, Nahla Ivy, Julie Chua, Matthew Barrett, Larry Feldman, Daniel Topper, Gregory A. Witte, R. K. Gardner. NIST IR 8286D-upd1, February 2025, updated 26 February 2025. DOI: https://doi.org/10.6028/NIST.IR.8286D-upd1. Citation key: quinn2025bia. Complete 27-page report examined: executive summary, §§1–3, references and Appendices A–B. This version supersedes November 2022; they are not independent studies. Original public U.S. government PDF retained with attribution.

## Purpose and constructs
The report extends BIA beyond availability/recovery planning to consequences of confidentiality, integrity and availability loss. It links enterprise risk management (ERM) and cybersecurity risk management (CSRM). Mission, financial and reputational consequences explain asset value; replacement cost alone is insufficient. Assets include technology, intangible information/reputation, transactions, control signals and sensor readings (Table 1; §§2.1–2.4). Impact domains are illustrative and should fit context.

A BIA register records impacts, criticality/sensitivity and rationale; it is related to, but distinct from, a cybersecurity risk register. Leadership supplies mission priorities, risk appetite and tolerance; system owners interpret these directions in system-level BIA. Consistent forms, approved criteria, periodic review and worst-case timing support comparability (§1.2). Consistency does not eliminate uncertainty.

## Process, dependency logic and outputs
Figure 1 and §2.2 describe a feedback cycle: identify essential products/processes and enabling assets; communicate risk direction; analyze mission support and losses at system level; inform CSRM; aggregate residual risk in organizational registers; evaluate composite consequences and adjust enterprise responses/direction. This is iterative, not a rigid waterfall.

Importantly, §2.2 Step A (printed pp. 7–8) states that supporting assets inherit criticality/priority from the functions they support. This is prior conceptual support for inheritance; Masar cannot claim to invent that concept. The report does not specify the project's exact maximum-over-services calculation, tie policy or executable configuration. Interdependencies, ownership and contacts belong in a maintained registry (§§2.6–2.8).

Criticality concerns availability loss; sensitivity concerns confidentiality/integrity loss (§2.5). Loss may be partial, including degraded operation. Event timing, latency and duration affect consequences. High-level BIA loss scenarios differ from detailed risk scenarios; BIA does not itself estimate event probability (§2.4). Mentioned fault/event trees, FMEA and simulation are broader risk-analysis options, not a mandated BIA algorithm or experiments implemented here.

Outputs include categorized assets, documented impact values/rationale, protection requirements, registry records and inputs to risk prioritization and communication. Feedback from aggregated registers can refine asset valuations and leadership criteria.

## Evidence, limitations and thesis use
This is technical guidance, not controlled empirical evaluation: no participant sample, predictive accuracy, optimized recovery schedule or measured downtime reduction is reported. Claimed alignment benefits are guidance/rationale, not causal effect estimates. Appendix B labels 2025 changes editorial, including CSF 2.0 inventory wording and companion references. Historical references to drafts do not establish those drafts' currency in 2026.

Primary mapping: §§2.2 BIA and 2.4 inheritance; secondary §§2.1, 2.3, 2.5, 2.7. It supports a mission/service-to-resource chain, explicit criteria, a central registry and human governance. Narrow the gap to a defined, implemented and evaluated service-first temporal method with traceable decisions, rather than absence of inheritance or impact-driven prioritization. It supplies neither universal MTPD/RTO cut-offs nor evidence that TDRP includes probability, confidentiality or integrity analysis.
