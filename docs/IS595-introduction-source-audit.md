# Introduction Source Audit

Checked on 16 October 2026. This audit supports Chapter 1 only. It is not the full-text reading archive or systematic search log required for the later literature review.

## Cited sources and permitted use

| BibTeX key | Verified DOI | Primary evidence consulted | Use in the introduction and access limits |
| --- | --- | --- | --- |
| `gibb2006framework` | `10.1016/j.ijinfomgt.2005.11.008` | [Authors' university record](https://pureportal.strath.ac.uk/en/publications/a-framework-for-business-continuity-management/) | The abstract connects BCM design, implementation, and monitoring with information strategy. Used for this broad framing only; no detailed framework components or empirical results are attributed to it. Full article not read at this stage. |
| `torabi2014framework` | `10.1016/j.ssci.2014.04.017` | [Publisher record and abstract](https://www.sciencedirect.com/science/article/pii/S0925753514001027) | The abstract explicitly identifies critical functions, MTPD, and MBCO as BIA concerns. Used only for that high-level statement. No claim about comparative performance or detailed calculations. Full article not read at this stage. |
| `swanson2010contingency` | `10.6028/NIST.SP.800-34r1` | [NIST publication record](https://www.nist.gov/publications/contingency-planning-guide-federal-information-systems-including-updates-through) and [official PDF](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-34r1.pdf) | Consulted the publication metadata and relevant BIA/recovery sections, especially Section 3.2 and the BIA template. Supports distinction among business-process downtime, resource RTO, data RPO, dependencies, and recovery priorities. NIST uses MTD; Masar's service-level MTPD terminology is explicitly distinguished in the text. This is U.S. federal guidance, not a Saudi regulatory requirement. No full-document reading is claimed. |
| `quinn2025bia` | `10.6028/NIST.IR.8286D-upd1` | [NIST record](https://www.nist.gov/publications/using-business-impact-analysis-inform-risk-prioritization-and-response-0) and [official updated PDF](https://nvlpubs.nist.gov/nistpubs/ir/2025/NIST.IR.8286D-upd1.pdf) | Executive summary and relevant BIA-register discussion support centralized, reliable asset information and criticality linked to enterprise objectives. The 2025 update supersedes the inherited 2022 source. The old entry is retained for history but is not cited. No full-document reading is claimed. |
| `jarvelainen2013incidents` | `10.1016/j.ijinfomgt.2013.03.001` | [Publisher abstract](https://www.sciencedirect.com/science/article/abs/pii/S026840121300039X) and [author university repository record](https://www.utupub.fi/items/64fe9315-3eff-41a2-b71f-02594fa3be25) | Supports only that prior IS research examines continuity management and IT incident/business impact relationships. The chapter does not reproduce survey findings or make causal claims. Full-text retrieval was not reliable in the browsing interface; full paper not read. |
| `hevner2004design` | `10.2307/25148625` | [MIS Quarterly/AIS record](https://aisel.aisnet.org/misq/vol28/iss1/6/) | Its abstract supports positioning artifact construction/evaluation in relation to an organizational IS problem. No detailed evaluation framework is claimed to have been applied. Full article not read at this stage. |
| `peffers2007dsrm` | `10.2753/MIS0742-1222240302` | [Journal record](https://www.jmis-web.org/articles/765) and [author-hosted PDF](https://scholar.cgu.edu/samir-chatterjee/wp-content/uploads/sites/6/2013/07/jmis-article.pdf) | The journal abstract explicitly lists the six DSRM activities. Used to organize the proposed study across IS595/IS597. The journal identifies Volume 24 Number 3 as 2007; the PDF bears Winter 2007–8 and a 2008 copyright. The existing publisher-year convention of 2007 is retained. Full-document reading is not claimed. |

## Citation controls

- Every cited key exists in `references.bib` and includes a nonempty `doi` field.
- Seven unique keys are cited; no `\nocite{*}` is used to inflate the bibliography.
- DOI display is enabled for this deliverable by `plainnat`; for the two NIST reports, the DOI is also recorded as a resolver URL so the identifiers are visible in the generated bibliography.
- The existing bibliography contains additional inherited entries that have **not** all been verified or used. Their presence is not evidence of reading. The literature-review phase must audit each selected record and obtain its full text before synthesis.
- No DOI has been invented for an ISO standard. ISO metadata was checked as background, but the revised chapter does not cite an unverified standard entry or claim ISO compliance/certification.
- Source-based background is distinguished from original project proposals. Threshold rules, review states, exception handling, and dashboard requirements are proposed design decisions; cited literature is not represented as having validated TDRP.

## Claims deliberately avoided

No global claim that existing systems cannot support these functions; no statement that TDRP is the first such method; no claim of completed practitioner approval; no assertion of a particular organization's document fragmentation; no demonstrated reduction in downtime, monetary losses, or decision time. Such claims require evidence beyond the sources and work completed here.
