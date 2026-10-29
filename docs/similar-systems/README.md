# Similar Systems and Tools: Commercial, Open-Source, and Research Prototypes

This document maps the systems and tools that resemble the proposed system, Masar, which implements the TDRP methodology. It supports Sections 2.5.2, 2.5.3, and 2.7 of the Literature Review chapter. It is a working reference for the writing stage and is not text for the thesis.

## 1. What "similar" means here

Masar is a decision support system that (a) holds service-level BIA results across successive assessment periods and impact dimensions, (b) applies configurable rules to derive criticality, MTPD, and RTO, (c) sets relative recovery priorities, (d) links services to supporting dependencies and assigns those dependencies a criticality by a documented rule (default: highest among the services supported), and (e) shows results with traceability to the rules and assessments behind them. It does not simulate incidents or generate executable recovery schedules. A tool is therefore treated as similar if it covers any of (a) to (e), and the comparison below states which parts.

## 2. Method and evidence levels

Tools were identified through general web search for BCM and BIA software, open-source GRC and ISMS projects, CMDB tools with impact analysis, and research prototypes. Only public documentation was used and no software was installed or tested. The survey is purposive and is **not exhaustive**: other commercial suites exist and were not examined.

Each entry carries an evidence level: **A** = the public page was read in full and has a record in `docs/sources/`; **B** = only a search-result excerpt of a public page was seen, so statements are limited to the excerpt and the entry is a candidate for a full record before it is cited. "Not documented in the reviewed text" means unknown, not absent.

## 3. Commercial platforms

| Tool (vendor) | What the reviewed material documents | Level | Source key |
|---|---|---|---|
| ServiceNow Business Continuity Management | BIA workflow with questionnaires, calculated RTO and RPO, recovery tiers, dependency assessment tied to the CMDB, approval and archive. RTO is the minimum of category downtimes determined by configured tolerability and durations; a configured maximum applies when nothing is intolerable. | A | servicenow2025bia, servicenow2025rto, servicenow2025datasheet |
| Fusion Risk Management | BIA, recovery requirements, plans, exercises, and relationship mapping across people, processes, places, systems, and third parties with upstream and downstream dependencies. A vendor blog describes a Recovery Optimization feature that proposes a recovery order from dependency data, priorities, recovery objectives, and constraints. | A (product page); B (blog) | fusion2026bcm |
| Riskonnect BCM | BIA and risk assessment, dependency mapping, planning, workflows, exercises, dashboards, ERM integration. Calculation details are not disclosed on the page. | A | riskonnect2026bcm |
| GlobalSuite Business Continuity | Impact table by service across a configurable time scale with Very Low to Very High ratings; manual or automatic MTPD by three criteria; consolidation of departmental BIAs by average, weighted average, maximum, or minimum; minimum operating level; resumption deadline; confidence level. | A | globalsuite2025prebia |
| GRASP GRC (DextraData), BCM module | Impact over configurable time horizons per damage scenario, recovery time objective, MTPD, optional emergency operating level, dependencies with single-point-of-failure checks, rationale recording, pre-filter of processes. MTPD and RTO appear to be set by the analyst. | A | grasp2025bia |
| IBM OpenPages Business Continuity Management | BIA and plan workflows with testing and issue tracking. A GRC calculation is said to define the maximum acceptable outage for a business function by scoring BIA selections. | B | not yet recorded (https://ibm.com/services/business-continuity/plan) |
| [alive-IT] | A BIA module based on ISO 22317 whose parameterizable procedure calculates RTO and MTPD to identify critical processes. | B | not yet recorded (https://www.softguide.com/program/alive-it) |
| MEGA HOPEX BCM | BIA defined per process category within a BCM system. | B | not yet recorded (https://doc.mega.com/hopex-v6-en/BCM/BIA.Defining_a_Business_Impact_Analysis.html) |

## 4. Open-source and research tools

| Tool | What the reviewed material documents | Level | Source key |
|---|---|---|---|
| verinice (SerNet) | Open-source ISMS tool with a BCM domain for ISO 22301 and BSI 200-4: process capture, dependency evaluation, a BIA view of process and resource dependencies, and, in the classic product, automatic inheritance of business-impact values in the asset tree. Licence stated as GPLv3 for the classic application; the newer web generation's licence was not verified. | A (BCM page); B (licence, inheritance, BIA view) | verinice2025bcm |
| iTop (Combodo) | Open-source IT service management platform with a configurable CMDB, service and contract management, SLA management, and a graphical impact analysis. It is not a BCM tool and has no BIA or recovery-objective model in the reviewed excerpt. | B | not yet recorded (https://github.com/Combodo/iTop) |
| Open Resilience | A community, MIT-licensed project (TypeScript and React) described as a business continuity and operational resilience platform covering BIA, risk management, and incident response. Registered on SourceForge in April 2026, so it is very recent; its features and maturity were not reviewed. | B | not yet recorded (https://sourceforge.net/projects/open-resilience/) |
| QuantTM (University of Zurich) | Research prototype, client-side web tool: threat-scenario BIA with one-time and persistent impacts, recovery level over time frames, financial loss totals. A repository is cited in the paper but was not checked. | A (preprint) | vonderassen2024quanttm |
| PRECESION and the model of Sahebjamnia et al. | Optimization models for recovery order or recovery planning, not deployed tools. | A | elshekeil2017precesion, sahebjamnia2015integrated |

## 5. Capability comparison against Masar's intended functions

Cells state what the reviewed text documents. "n.d." means not documented in the reviewed text.

| Tool | Service/process BIA | Time-indexed impact | MTPD or RTO derived by a documented rule | Configurable scales and thresholds | Dependency mapping | Dependency criticality inherited by a documented rule | Recovery-order support |
|---|---|---|---|---|---|---|---|
| ServiceNow BCM | Yes | Yes (durations per category) | RTO yes; MTPD n.d. | Yes | Yes (CMDB) | Partial: related-item RTOs are shown; aggregation rule n.d. | n.d. |
| Fusion | Yes | n.d. | n.d. | n.d. | Yes | n.d. | Yes (vendor blog) |
| Riskonnect | Yes | n.d. | n.d. | n.d. | Yes | n.d. | n.d. |
| GlobalSuite | Yes | Yes | MTPD yes (three criteria); RTO managed | Yes | Resource mapping | n.d. | n.d. |
| GRASP GRC | Yes | Yes | Set by analyst; no rule shown | Yes | Yes, with SPOF checks | n.d. for BCM | n.d. |
| IBM OpenPages | Yes | n.d. | Maximum acceptable outage by scoring (excerpt) | n.d. | n.d. | n.d. | n.d. |
| [alive-IT] | Yes | n.d. | RTO and MTPD by parameterizable procedure (excerpt) | Parameterizable | n.d. | n.d. | n.d. |
| verinice | Yes | n.d. | n.d. | Customizable (page) | Yes (BIA view) | Impact values inherited in asset tree (excerpt) | n.d. |
| iTop | No | No | No | n.d. | Yes (CMDB) | n.d. | No |
| Open Resilience | Stated | n.d. | n.d. | n.d. | n.d. | n.d. | n.d. |
| QuantTM | Threat-scenario BIA | Yes (recovery tuples) | MTPD is an input | Partly | No | No | No |
| **Masar (planned)** | Service level | Successive periods and dimensions | MTPD and RTO from configurable rules | Yes | Yes | Yes, default highest among supported services | No (priority is not a schedule) |

## 6. What the comparison supports

1. **Commercial tools already automate parts of the pipeline.** ServiceNow and GlobalSuite document configurable temporal rules that yield RTO or MTPD, so a claim that such derivation is new would not be supportable.
2. **No reviewed tool documents the full combination** of time-indexed service-level impact, a published rule for criticality, MTPD, and RTO with handling of incomplete data and unreached thresholds, and a documented inheritance rule for shared dependencies. This is a statement about the reviewed documentation only, since products may implement undocumented behaviour.
3. **Inheritance exists in some form.** verinice documents impact-value inheritance through an asset tree, NIST IR 8286D states that supporting assets inherit the priority of the functions they support, and GRASP lists protection-needs inheritance pages in its ISMS applications. The distinctive element for Masar is the documented rule for shared dependencies and its evaluation, not inheritance itself.
4. **Open-source coverage is thin for temporal BIA logic.** The reviewed open-source tools cover BIA recording, dependency views, and asset inheritance. None showed time-indexed threshold derivation in the reviewed text.
5. **Scope differs.** Commercial suites span plans, exercises, crisis communication, and workflow, which Masar deliberately omits. Comparisons should therefore be made by analytical inputs, rule disclosure, configuration, traceability, and evaluation, and not by feature count.

## 7. Limits and follow-up

- The survey relies on public documentation and excerpts, with no software tested. Vendor claims are attributed claims.
- Entries at level B should be fully read and recorded in `docs/sources/` before they are cited in the thesis: IBM OpenPages, [alive-IT], MEGA HOPEX, iTop, Open Resilience, and the Fusion Recovery Optimization pages.
- Further commercial and open-source tools should be searched for before the final chapter is submitted, including open-source GRC platforms with a BCM module and, if available, recorded trial or demonstration evidence for the leading products.
