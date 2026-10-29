# Criticality Analysis Process Model: Prioritizing Systems and Components (NIST IR 8179)

## Identity and reading basis

- **Authors:** Celia Paulsen, Jon Boyens (NIST); Nadya Bartol, Kris Winkler (Boston Consulting Group).
- **Publication:** NIST Internal Report 8179, April 2018, 94 pages. DOI https://doi.org/10.6028/NIST.IR.8179. BibTeX key `nist2018criticality`.
- **Text examined:** the PDF text from the cover through the start of sub-process E.2, which covers the Executive Summary, Chapters 1–3, and all of Processes A–D. Sub-processes E.3–E.5, Appendix B–C (references and methods), Appendix D (two illustrative examples, an ERP system design and a smart-city concept), and Appendix E (full diagram) were **not** read. Statements below are limited to what was read. Locators are the report's printed page numbers.

## Purpose and positioning

The report defines a process model for prioritizing programs, systems, and components by their importance to organizational goals and the impact their inadequate operation or loss would have on those goals (pp. iv, 1). Its stated motivation is that existing standards give high-level, fragmented guidance on prioritization, often prioritizing either projects by goals or components by system function, which can leave an incomplete picture (p. 1). The model is aimed at information-security and privacy risk management, supply-chain risk management, acquisition, and systems engineering. It is not a business continuity method, and it does not mention MTPD or RTO in the portions read. It is presented as a component to be integrated into existing processes and tailored by each organization (p. iii, Section 1.1).

## Structure of the model

The model has five processes (pp. iv–v, 5–8). **A** defines the criticality analysis procedure and triggers for review. **B** is program-level analysis (business objectives and workflow paths). **C** is system or subsystem analysis within a critical workflow path. **D** is component or subcomponent analysis within a system. **E** is a bottom-up detailed review that harmonizes the three levels and assigns final criticality. B–D are top-down: they identify critical activities, then the systems supporting them, then the components that make those systems function. Process E traces impact bottom-up from subcomponents to components, systems, programs, and higher-level programs, "to ensure criticality determination is consistent across all layers" (p. 9). The model was built from an environmental scan of methods from several disciplines, a comparative matrix, and translation into security and privacy practice (Section 2.1, pp. 5–6).

## Elements relevant to this project

1. **Dependencies are mapped at every level.** Sub-processes B.2–B.3, C.3, D.3, and E.1 identify interactions, intersections, connections, and dependencies. The report asks the analyst to highlight any activity or output that several workflows depend on (p. 22) and, in E.1, to find a component used in multiple subsystems, a system supporting multiple programs, and components from a single supplier (pp. 47–48).
2. **Operating states with severity and duration.** Sub-processes B.4, C.4, and D.4 describe non-operational, impaired, normal, increased, and unintended states, and ask for severity as a ranking (low, moderate, high) or a measure (such as time lost). The text notes that long-term adverse states often have greater impact than short-term ones and asks how long a state must last before it becomes severe (p. 24). This is a qualitative prompt about duration; no impact-over-time function is specified.
3. **Baseline criticality by ranking, measure, ranges, or thresholds.** B.5, C.5, and D.5 allow a low/moderate/high ranking, a measure such as time lost or cost, or ranges and thresholds (pp. 25, 35, 44). One example scheme ranks as "High Criticality" the items affected by the highest number of scenarios (p. 44).
4. **Criticality traceable to goals.** Process B ensures that system and component determinations "can be directly traced back" to program objectives and organizational goals (pp. 17–18).
5. **Tailoring and documentation.** Process A requires documented procedures, roles (responsible/accountable/consulted/informed), and triggers for full or partial re-analysis, such as a changed environment or a modified system (pp. 12–14).

## Critical reading and limits

- **Different object and purpose.** The model prioritizes assets for protection and acquisition decisions. It does not derive recovery time objectives, maximum tolerable disruption, or recovery sequences, and the portions read give no formula.
- **Method-level guidance, not an algorithm.** Rankings and thresholds are left to the user, and the model is described as idealized and adaptable (p. iii). There is no specified aggregation rule for how a component's final criticality follows from the several systems it supports in the pages read. Final assignment (E.5) was not read, so the report must not be cited for or against any particular aggregation rule such as maximum-over-dependents.
- **No evaluation in the portions read.** The report describes a process; the reading did not include demonstrated validation. Its two examples (Appendix D) were not reviewed.
- **Context.** Written for federal information systems and supply-chain risk; application to service-level business continuity decisions is an inference by the reviewer.

## Use in the approved chapter

**Primary:** Section 2.4.3 Criticality of Dependencies, as documented guidance that criticality is analysed at program, system, and component level and traced across shared components. **Secondary:** Section 2.3.2 Rule-Based Approaches (rankings with ranges and thresholds defined by the organization), Section 2.2.3 Time-Dependent Impact Assessment (operating states and duration as a qualitative prompt), and Section 2.7 (evidence for prior art on dependency-based criticality).

Pair it with `quinn2025bia`, which the evidence map already records for criticality inheritance, and keep the two distinct: this report supplies a general criticality-analysis process, not a business-continuity recovery method. Do not claim that it specifies how criticality is inherited by shared dependencies unless E.3–E.5 are read first.
