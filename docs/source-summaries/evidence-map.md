# Evidence map for the approved Chapter 2 roadmap

This is a research working map, not drafted chapter prose or a final comparison table. Citation keys resolve in references.bib; source versions, coverage and original locators are in the paired summaries and manifest.

| Approved section | Main evidence | Analytical role | Inference boundary |
|---|---|---|---|
| 2.1 Business Continuity Management; standards; Saudi guidance | russo2023maturity (field-level SLR counts and standards comparison); bcms2026reference; nist2010contingency; dga2025bcm; dga2025guidelineen; nrcnationalframework; iso22301catalogue; iso22313catalogue; iso22317catalogue | Explain BCM lifecycle, BIA's place, governance, international scope and local context. | Russo's counts describe its filtered BCP/DRP-plus-guideline corpus, not the whole BCM or BIA literature. Catalogue scope is not full-standard clause review; a tool implements a subset of BCMS work and does not thereby achieve certification/compliance. |
| 2.2 Business Impact Analysis; impact categories; temporal impact; recovery parameters; approaches | vonderassen2024quanttm (persistent impact by recovery level and time frame); globalsuite2025prebia (time-indexed impact table); nist2010contingency; quinn2025bia; DGA/NRC; amm2023bia; container2021bia; assetcriticality2023 | Compare contextual impact scales, time horizons, data collection, service/process/resource links and definitions before analytical variants. | Case scales and illustrative targets are not universal. Distinguish MTPD/MTD, RTO, RPO and MBCO; retain case-table inconsistencies. |
| 2.3 Criticality and Recovery Prioritization; MCDM; rules; sequencing | nist2018criticality (rankings with ranges and thresholds); elshekeil2017precesion (sequencing under dependencies and worker capacity); globalsuite2025prebia (vendor MTPD criteria and consolidation rules); vonderassen2024quanttm (quantitative versus ordinal scales); assetcriticality2023; sahebjamnia2015integrated; DGA/NRC; servicenow2025rto | Contrast weighted/fuzzy ranking, multi-objective resource-constrained planning and configured rules. | Criteria-dependency Bayesian networks differ from service-resource maps. Sahebjamnia's RPO terminology differs. A priority list does not imply a feasible schedule. |
| 2.4 Dependency Modeling; services; interdependency; criticality | nist2018criticality (dependency mapping and shared components, E.3-E.5 unread); rinaldi2001interdependencies; quinn2025bia; raptaki2025propagation; assetcriticality2023; DGA/NRC | Distinguish link direction/types, shared exposure, mission-derived inheritance and process-log propagation. | Rinaldi is conceptual; NIST inheritance is prior art; process-mining scores are relative, scenario-dependent, not failure probabilities or MTPD. Maximum-over-services remains a project policy to evaluate. |
| 2.5 Decision Support for BCM; foundations; continuity DSS; tools | arnott2005descriptive (DSS typology and field critique); vonderassen2024quanttm (BIA prototype); globalsuite2025prebia (vendor Pre-BIA module); grasp2025bia and verinice2025bcm (further commercial and open-source tools; see docs/similar-systems/README.md); power2007history; sahebjamnia2015integrated; selfassessment2025; raptaki2025propagation; servicenow2025bia; servicenow2025rto; servicenow2025datasheet; fusion2026bcm; riskonnect2026bcm | Separate data/model/rule support, implementation examples, readiness assessment and provider functions. | An advertised feature is not an independently measured benefit. Readiness scores are not service criticality. Undocumented behavior is unknown. No commercial tenant was tested. |
| 2.6 Research Methods and Evaluation | arnott2005descriptive (DSS research methods and relevance); russo2023maturity (SLR inside a design-science process); hevner2004design; peffers2007dsrm; venable2016feds; empirical cases above; bcms2026reference; selfassessment2025 | Distinguish DSR guidelines, research process, evaluation strategy, cases, experts, sensitivity and artifacts. | Demonstration, correctness, usability and organizational effectiveness require different evidence. Do not convert local feedback into universal validation. |
| 2.7 Comparative Synthesis and Research Gap | All reviewed relevant evidence, weighted by type and coverage | Build a defensible gap around the specified TDRP method and Masar implementation/evaluation. | Do not claim that temporal rules, service support, inheritance or BCM software have never existed. No universal superiority is established. |
| 2.8 Chapter Summary | Synthesis of preceding sections | Restate established themes and the bounded need addressed by the project. | Introduce no new results, design decisions or unsupported novelty claims. |

## Comparison dimensions to carry into Task 3

- Unit of analysis: product, service, process, activity, system, asset, or overall preparedness.
- Inputs and provenance: expert judgement, questionnaires, operational records, logs, approved scales and configurations.
- Temporal representation: fixed tier, multiple impact horizons, loss duration, restoration time or dynamic propagation.
- Decision logic: weighted/fuzzy/MCDM score, mathematical optimization, deterministic configured rule or descriptive classification.
- Parameters: how MTPD/MTD, RTO, RPO and minimum operating level are defined, derived and checked.
- Dependencies: what is linked, direction, shared resources, indirect/cyclic paths, inheritance/aggregation and assumptions.
- Outputs and authority: explanation, priority, plan, schedule, report and human review.
- Implementation and evaluation: conceptual artifact, prototype, case, solver, logs, experts, sensitivity and deployment evidence.
- Transferability: context, sample, data access, validation limits, version and disclosed versus unknown behavior.

A single source need not report all dimensions. Mark unreported details explicitly. Original-source results and the reviewer's implications must stay distinguishable. Any final LaTeX tables belong in separate files under tables/ with input inclusion, as required by the project.

## Known evidence gaps after the corpus extension

These roadmap functions still rest on thin or non-scholarly evidence and should be strengthened or stated cautiously in Task 3:

- **2.3.3 Recovery Sequencing:** two scholarly sources (sahebjamnia2015integrated and elshekeil2017precesion). Both are optimization studies. Vendor recovery-order tools exist but are not yet recorded.
- **2.5.2 Decision support in continuity and disaster management:** one BIA prototype (vonderassen2024quanttm, a preprint in the cyber-threat domain) and the readiness tool in selfassessment2025. No continuity DSS journal prototype has been read in full; Schätter et al. (2019) and Merz et al. (2009) were not accessible.
- **2.3.1 Multi-criteria approaches:** one BIA-based quantitative study (assetcriticality2023) and the AHP use inside sahebjamnia2015integrated. No dedicated fuzzy or TOPSIS criticality study has been read.
- **2.4.1 Service dependencies:** guidance, vendor documentation and the three-layer model in elshekeil2017precesion, with no ITSM or configuration-management research article.
- **2.2.4 BIA methods:** torabi2014framework remains metadata-only.
- **2.1 and 2.5.1:** the BCM literature reviews of Gibb and Buchanan, Herbane, and Charoenthammachoke et al. (2020) were not read; Hosack et al. (2012) was not reached.
