# Integrated Business Continuity and Disaster Recovery Planning: Towards Organizational Resilience

## Identity and reading basis

- **Authors:** N. Sahebjamnia, S. A. Torabi, S. A. Mansouri.
- **Published:** *European Journal of Operational Research*, 242(1), 261–273, 2015.
- **DOI / BibTeX:** https://doi.org/10.1016/j.ejor.2014.09.055 — `sahebjamnia2015integrated`.
- **Text examined:** complete 32-page accepted manuscript from [Brunel's repository](https://bura.brunel.ac.uk/bitstream/2438/11835/1/Fulltext.pdf). Its cover and running title use “resiliency”; cite the published title and 2015 journal year. Locators below are manuscript PDF pages, not final journal pagination. Separate online supplementary files were not examined.
- **Access:** downloaded for reading; public access does not establish permission to republish the manuscript. The source access record provides the retrieval link.

## Problem and contribution

The study addresses the allocation of scarce resources between short-term continuity and longer-term restoration. Treating business continuity planning and disaster recovery planning independently can conceal competition for the same resources. The contribution is an integrated framework at strategic, tactical, and operational levels, a multi-objective mixed-integer linear programming model, and an interactive augmented epsilon-constraint solution method, IAUGCON. It is an optimisation and planning study, not simply a classification or dashboard application.

## Framework, inputs, and model

At the strategic level, the organization establishes objectives, stakeholders, scope, key products/services, critical operations, disruption scenarios, and internal/external resources. BIA supplies MTPD and minimum business continuity objective (MBCO). The tactical model chooses operating levels and resource allocations across periods. The operational stage tests the resulting plans through hypothetical disruptions and sends unacceptable results back for revision (PDF pp. 8–12).

Inputs include product importance weights, product/operation relationships, resource requirements at each operating level, disruption likelihoods and resource losses, external-resource costs and availability, period budgets, MTPD, and MBCO. The case uses AHP for relative importance and production-planning information for resource consumption. These elicited and operational data are substantive prerequisites, not outputs obtained automatically from impact ratings alone.

The two objective functions minimise weighted loss of operating level over the horizon and weighted recovery time. Constraints cover one operating level per operation/period, minimum acceptable operation after the tolerability deadline, non-decreasing recovery trajectories, internal/external resource capacities, external-resource budgets, product-level operation, time limits, and variable domains. The loss-of-resilience concept connects the depth and duration of degraded operation (PDF pp. 7, 12–15). IAUGCON constructs objective bounds, generates epsilon vectors, and interactively elicits decision-maker preferences to seek efficient compromise solutions while avoiding redundant or infeasible searches (pp. 16–21).

## Evaluation and reported findings

The case is an Iranian gearbox manufacturer. Four key products, four operations for each product, four resource types, ten operating levels, and five disruption types are considered. The resource types are facilities, equipment, personnel, and power; disruption types include flood, earthquake, fire, sabotage, and epidemics. Three planning scenarios represent optimistic, realistic, and pessimistic conditions. The model is solved using CPLEX 10 (pp. 21–26).

Reported outputs include product operating-level trajectories, recovery times, and internal/external resource requirements. Evaluation uses average loss of resilience, recovery time, and total loss under an additional hypothetical disruption. The findings demonstrate trade-offs and reveal a product whose outcomes fall outside acceptable ranges. Management considers outsourcing and staged improvement, constrained by budget (pp. 26–28). The evidence is a real organizational case with modelled scenarios; it is not a controlled demonstration of improved performance during actual incidents.

## Terminology and critical interpretation

**RPO requires particular care:** the manuscript uses it for a selected *resumption operating level*, bounded below by MBCO. That differs from the data-loss/look-back meaning of recovery point objective in other sources. Do not import this usage into Masar's terminology (pp. 11–13).

The manuscript also uses recovery/resumption terminology in ways that require careful contextual reading: its formulation discusses MTPD constraints, while the case tables contain reported recovery times exceeding some MTPD values and discuss exceptions. Describe the model's declared constraints and reported case results separately; do not claim that every reported scenario satisfies every continuity requirement. Exact equation reconstruction requires checking the original typeset mathematics because text extraction disrupts subscripts and symbols.

Limitations relevant to comparison include the single manufacturing case, extensive resource and scenario inputs, decision-maker-dependent preferences, assumptions about restoration trajectories and replaceability of resources, and reliance on hypothetical evaluation. The authors identify uncertainty modelling, further resilience measures, and multiple-event settings as future directions (p. 28). These are boundaries of the study, not evidence that simpler rules are necessarily superior.

## Use in the approved chapter

**Primary:** §2.3.3 Recovery Sequencing. **Secondary:** §2.2.4 Analytical Approaches to BIA; §2.4 Dependency Modeling; §2.6 Research Methods and Evaluation; §2.7 Synthesis and Research Gap.

Use it to establish the distinction between BIA-derived tolerability inputs and optimisation-derived recovery/resource decisions. It supports the need to connect business requirements to recovery planning, while providing a comparison outside TDRP's bounded task of reproducible service classification and relative prioritization. It does **not** establish TDRP's highest-criticality inheritance rule, demonstrate that no configurable system exists, or validate Masar. The manuscript's novelty claims belong to its historical publication context.
