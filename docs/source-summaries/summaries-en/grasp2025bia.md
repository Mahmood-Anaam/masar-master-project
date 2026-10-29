# GRASP GRC: Business Impact Analysis Assessment in the BCM module

## Identity and reading basis

Documentation page of the GRASP governance, risk and compliance platform published by DextraData GRC Technologies GmbH, key `grasp2025bia`, URL https://docs.grasp-grc.com/en/apps/bcm/bia/assessment.html. The page shows no release number or date. It was read in full on 29 October 2026. The configuration page and the pages on protection-needs inheritance were visible only as menu titles and were not opened. No software was tested.

## What the page documents

**Impact over time, per damage scenario.** In the detail view of a process the analyst selects a damage scenario (for example financial, legal, or reputation) and records how the damage develops across configured time horizons, including the point from which impact becomes medium, high, or very high. The page's example is illustrative: low damage up to two hours, medium from four hours, high from eight hours, and very high from twenty-four hours. The view is typically a table or a curve. Scenarios, time horizons, and damage potentials are set in a separate configuration step.

**Recovery objectives derived from the assessment.** The analyst sets a recovery time objective (the time within which the process must be operational again), a maximum tolerable period of disruption (the downtime before existentially threatening or unacceptable damage occurs), and optionally an emergency operating level, for example 50% of normal throughput. The page uses the verb "derive", but it describes no automatic rule that computes these values from the ratings, so the derivation appears to be a human judgement supported by the table.

**Dependencies and single points of failure.** The assessment shows linked assets, service providers, and upstream and downstream process chains. The analyst checks whether an asset or provider is a single point of failure, flags critical dependencies, and derives requirements for redundancy or alternative processes. The results feed risk management, strategies, and plans.

**Traceability and scoping.** Each assessment should carry a recorded rationale (why the criticality level, which assumptions, which limitations are acceptable in emergency operation) for audits and handovers. A pre-filter can classify processes as critical or non-critical to limit the detailed assessments.

## Reading for the project

- It is a documented example of a **time-horizon impact assessment per scenario, configurable scales, and recovery objectives that include MTPD** in a commercial platform. As in the other vendor sources, this bounds any novelty claim.
- The page shows **no executable threshold rule** for MTPD or RTO, no handling of missing periods or unreached thresholds, and no dependency-criticality rule in the portion read. These are unknown, not absent.
- The navigation lists "protection needs assessment and inheritance" pages under the ISO 27001 and IT baseline protection applications of the same platform. Their content was not read, so inheritance in this product is neither confirmed nor ruled out for BCM.
- The page is process-oriented. The platform's inventory has processes, assets, and dependencies as shared areas.

## Use in the approved chapter

**Primary:** Section 2.5.3 Continuity Management Software. **Secondary:** Section 2.2.3 (time-horizon impact tables), Section 2.4.1 (dependency and single-point-of-failure views), and Section 2.7 (comparison matrix). Cite as vendor documentation and distinguish documented capability from validated effectiveness.
