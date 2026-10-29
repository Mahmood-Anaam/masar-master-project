# Guideline of Risk and Business Continuity Management for Digital Government: English issue 1.0

## Identity and coverage
Digital Government Authority, document DGA-1-2-5-210, issue 1.0, 2025. Key: dga2025guidelineen. The 155-page supplied English PDF shows 28 January 2025 on the cover and 29/01/2025 in running footers. Both date presentations are recorded rather than silently resolved. It is distinct from Arabic DGA-1-2-5-231, version 3.0, 13 January 2025.

Examined: cover/contents, pp. 3–9 for purpose, scope and risk-system context; complete BCM division pp. 97–130; documentation p. 131; definitions/abbreviations pp. 132–138; and BCM annexes pp. 152–154. The broader risk-method details in pp. 10–96 were not fully reviewed; this summary does not claim their comprehensive extraction. The pre-existing PDF is unchanged.

## Purpose, governance and lifecycle
The guide supports reliable digital-government services and implementation of DGA's controls, while explicitly describing itself as general guidance that does not replace standards' requirements (p. 3). Application depends on entity operations, size, geography and circumstances (p. 5). BCM includes leadership, context, dependencies, policy, resources, awareness and reporting; a Plan–Do–Check–Act structure links planning, activation, verification and correction (pp. 98–114). Example governance structures differ depending on whether the entity has a board, and responsibilities are indicative.

## BIA and prioritization content
Section 5.2.5.2.1 (pp. 115–119) calls for inventorying internal/external procedures and operations, their dependencies, and disruption impacts over time using an approved matrix. It produces critical-process classification, RTO, RPO, MTPD, MBCO and resource requirements. Assessment timing is contextual: a half-hour or day-scale starting interval is an example, not a fixed universal grid.

Figure 59 applies stakeholder, financial, legal/regulatory and reputation impact to five platform/application tiers. It selects the highest factor level and associates very critical/critical/important/moderate/low with 4/8/12/24/48-hour RTOs subject to review. Table 24 illustrates two eight-hour critical platforms. Consequently, maximum-impact selection and tier-to-RTO mapping precede this thesis. They are not sufficient to infer the entire TDRP temporal calculation or dependency aggregation.

Translation/editing requires care: Table 24 labels its time column “Recovery Point Objective RTO,” although values and the surrounding discussion concern recovery time. The low-tier financial percentage is poorly formatted. Do not reproduce these as precise definitions or calculations. Definitions on p. 136 separately distinguish recovery time, recovery point, disruption tolerance and minimum service level.

## Strategies, plans and verification
Risk assessment considers disruption threats; strategies should respond to BIA requirements and available capacity. BCPs cover critical procedures, recovery times, alternatives, resources, communications and internal/external dependencies; ICT recovery gaps feed strategy (pp. 120–124). Separate roles cover crisis/incident/emergency management, recovery, communications, logistics and analysis.

Verification covers exercises and tests, including tabletop, procedural and full-scope activities, with review and improvement (pp. 125–130). The English text's placement differs from Arabic: it moves directly to correction at p. 127; Arabic p. 127 contains additional exercise-report discussion. Do not mix locators or assume literal equivalence.

Documentation management emphasizes standard forms, controlled archiving, workflows and reports (p. 131). Annex 11.3 identifies missing priorities, unmapped dependencies, unclear coordination, untested emergency plans and inadequate restart procedures as common mistakes (p. 152); annexes 11.4–11.5 illustrate ICT incident phases and team/plan structures (pp. 153–154).

## Evidence status and thesis use
This is primary institutional guidance, not a case-study evaluation or a measured performance comparison. No numerical effectiveness estimate or Masar validation is established. Public classification does not itself establish a new open redistribution licence.

Map principally to §2.1 Saudi guidance and §§2.2–2.5, with limits in §2.7. Use this separate citation when relying on English wording, especially version-specific details. It supports explicit, reviewable impact criteria and service-resource information; it does not establish full compliance, authorize replacing human approvals, or prove that a ranking is an executable recovery schedule.

## Detailed supplement from a second reading of the original (pp. 115–119)

**Figure 58 (p. 116).** A timeline relating backups, the incident, expected recovery time versus required recovery time, the recovery point objective, the recovery time objective, and the maximum tolerable period of disruption. The RTO sits inside the MTPD.

**Figure 59, the BIA matrix (pp. 117–118).** Five impact levels are crossed with four factors (stakeholder, financial, legal and regulatory, reputational), and each level carries a targeted recovery time. Entities classify each platform and, where the factors differ, adopt the highest level. The targeted times are subject to continuous review.

| Level | Stakeholder scope | Financial threshold | Legal/regulatory | Targeted RTO |
|---|---|---|---|---|
| Very critical | Complete impact across Saudi Arabia on all three beneficiary groups (government entities, businesses and supply chains, citizens and residents) | Up to SAR 1,000,000 per hour or 0.0115% of the service's annual revenue, whichever is greater | Loss of compliance certification or exposure to lawsuits and penalties | 4 hours |
| Critical | Complete impact across Saudi Arabia on one or more groups | SAR 500,000 per hour or 0.00575% | Suspension of compliance certification or legal exposure | 8 hours |
| Important | One or more regions, affecting one group | SAR 100,000 per hour or 0.00115% | Warning of suspension, clarification requests, potential accountability | 12 hours |
| Moderate | One or more governorates within a region | SAR 50,000 per hour or 0.000575% | Warning notice or clarification request | 24 hours |
| Low | A single centre or body, such as a university | SAR 10,000 per hour (the printed percentage is garbled) | Clarification request without legal violation | 48 hours |

The reputational column runs from damage to the overall reputation of digital government, including the Kingdom's ranking on the United Nations E-Government Development Index, down to no noticeable media attention.

**Table 24 (p. 119).** An illustrative row classifies a unified national platform with stakeholder impact critical, financial low, legal low, reputational moderate. The highest level, critical, gives an 8-hour RTO.

**Observations by the reviewer (not statements of the guideline).**
- Financial thresholds are expressed per hour, so a time rate is embedded in the tier definition, but the matrix assigns one level and one RTO per platform. It does not present an impact trajectory across successive time points. The text separately lets each entity choose the start of the impact timeline, for example after half an hour or after one or two days (p. 116).
- The stakeholder column mixes scope (national, regional, governorate, centre) with severity, so the five levels are not defined on a single scale.
- The stated hourly amounts fall by factors of 2, 5, 2, and 5 from level to level (by the reviewer's calculation), and the percentages follow the same ratios for the first four tiers. The printed percentage for the low tier is unreadable and should not be reconstructed.
- No computed example shows how the percentage-of-revenue and the hourly amount interact when they disagree beyond the phrase "whichever is greater", and no example covers a platform whose impacts are assessed at several time points.
