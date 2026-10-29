# QuantTM: Business-Centric Threat Quantification for Risk Management and Cyber Resilience

## Identity and reading basis

- **Authors:** Jan von der Assen, Muriel F. Franco, Muyao Dong, Burkhard Stiller (University of Zurich).
- **Version:** arXiv:2402.14140v1, 21 February 2024, marked "Preprint submitted to arXiv". DOI https://doi.org/10.48550/arXiv.2402.14140 (arXiv identifier). BibTeX key `vonderassen2024quanttm`.
- **Text examined:** the complete 16-page preprint including all tables, equations (1)–(5), and references; figures were read through captions. No peer-reviewed version was checked. Locators are section, table, and equation numbers.

## Problem and contribution

Threat prioritization in threat modeling usually relies on qualitative or ordinal scores (for example DREAD) that business decision-makers find hard to interpret. QuantTM converts threat events into expected financial loss by combining technical, business-process, and organizational views (Sections I–III). It has three parts: a three-layer methodology (information systems, business process, organizational), a business impact analysis (BIA) process with a loss model, and a browser-based prototype. The paper's domain is cyber threat modeling and security economics, and BIA is used there as a means of estimating loss.

## Method

**Methodology (Section III-A, Fig. 2, Eqs. 1–3).** Seven steps move from a technical threat model (threat events, assets, probability of initiation Pi and of success Ps, optional duration d) through translation into business-process effects (with an optional degree of impact) to an organizational impact assessment that yields cost factors.

**Quantitative model (Section III-B, Eq. 4).** Q(t) is the sum over threat effects of Pi × Ps × single-loss estimate for the stated duration and degree.

**BIA process (Section IV-A, Fig. 3, Eq. 5).** Six steps: scenario definition, classification against confidentiality, integrity, availability, and accountability (CIAA), mapping to 16 business impact factors drawn from industry reports, loss estimation per factor, recovery modeling (maximum tolerable period of disruption, currency, mitigation duration), and loss calculation. Impacts are either one-time or persistent. Total loss is the sum over persistent impacts and recovery stages of the per-day loss × (1 − recovery level at stage t) × days at that stage, plus the sum of one-time losses.

**Prototype (Section IV-B).** A client-side HTML and JavaScript tool with browser storage. For a persistent impact the user enters tuples of recovery level and time frame with a financial estimate, for example (recovery = 0, timeframe = 4) for a total four-day outage. The tool plots losses per threat, tangible versus intangible shares, and recovery trajectories over time.

## Evaluation and reported findings

- **Case study (Section V-A, Tables III–VII):** one Swiss B2B machinery SME with 10–20 employees, moving from phone ordering to a web shop. Six threat events were modeled with probabilities and durations (Table IV), business-process effects (Table V), and organization-level impacts in USD (Table VI). Reported expected-loss values (Table VII) were 324 USD for DDoS, 194 USD for deserialization, 13,543 USD for ransomware, and zero for three input-manipulation threats. Ransomware was characterized as existential because of potential exposure of customer-specific purchasing conditions.
- **Focus group (Section V-B, Tables VIII–IX):** five participants selected from 14 screened (three master's students, one software engineer, one finance expert, only one with prior BIA knowledge), a 57-minute online session on a hypothetical manufacturer with three threat scenarios, and normalized System Usability Scale scores of 75, 85, 55, 72.5, and 72.5. Participants gave congruent answers on the first six functional questions, and one participant misread a graph for the question on the most urgent threat. Usability feedback requested clearer inputs, textual hints, and information on data storage.
- **Expert contrast (Section V-C, Table X, Fig. 5):** one expert prioritized the same threats with a 3×3 risk matrix (all rated medium) and with DREAD (almost all medium-to-high, DDoS critical). The authors argue that QuantTM is more granular and explainable, while stating that correctness cannot be judged without ground truth.

## Critical reading and limits

1. **Preprint and self-evaluation.** The version reviewed is not peer reviewed, and the authors evaluate their own method and prototype.
2. **Small, informal evaluation.** The case is one very small SME; the focus group has five people, mostly students without BIA experience; the comparison with other methods uses one expert. The authors acknowledge the absence of ground truth (Section V-D).
3. **Numerical inconsistency found on recomputation.** Table VI lists 1,080,000 USD for the ransomware data-exposure impact. Using Eq. 4 with Pi = 0.6 and Ps = 0.2, the reported Q = 13,543 is reproduced only if that impact is 108,000 USD (0.12 × (3,240 + 1,620 + 108,000) ≈ 13,543); with 1,080,000 the product would be about 130,183. One of the two figures contains a typographical error, so the numbers should be checked against the authors' prototype before being quoted.
4. **Reporting slips.** The seven focus-group questions list the same question twice (Q2 and Q5). The mean of the five SUS scores is 72.0 by the reviewer's calculation; the paper does not report a mean.
5. **MTPD is an input, not a result.** The tolerable period is collected during recovery modeling; the paper does not derive MTPD or RTO from impact-over-time thresholds, and the output is monetary loss.
6. **Transfer.** The domain is cyber threats; the SME is not a public-sector service provider; impacts are monetized, whereas national continuity guidance uses ordinal impact scales.

## Use in the approved chapter

**Primary:** Section 2.2.3 Time-Dependent Impact Assessment, as an example that models persistent impact as a function of recovery level over time frames and totals it, which can be contrasted with threshold-based reading of impact scales. **Secondary:** Section 2.5.2 Decision Support in Continuity and Disaster Management (a documented BIA prototype with a client-side architecture), Section 2.6 Research Methods and Evaluation (a layered evaluation that combines a case study, a focus group with a usability scale, and expert comparison, with explicit acknowledgement of missing ground truth), and Section 2.3.2 (its discussion of nominal, ordinal, interval, and ratio scales as context for ordinal impact levels).

Cite it as a preprint, and state that its contribution is financial quantification of cyber-threat scenarios. Do not use it as evidence on MTPD or RTO derivation or on service criticality ranking, and do not quote the ransomware figures without resolving the inconsistency noted above.
