# Exploring a Multidisciplinary Assessment of Organisational Maturity in Business Continuity: A Perspective and Future Research Outlook

## Identity and reading basis

- **Authors:** Nelson Russo, Henrique São Mamede, Leonilde Reis, José Martins, Frederico Branco.
- **Published:** *Applied Sciences*, 13(21), article 11846, 30 October 2023 (review article, 19 pages, special issue "Application of Information Systems").
- **DOI / BibTeX:** https://doi.org/10.3390/app132111846, key `russo2023maturity`.
- **Text examined:** the complete open-access HTML full text (introduction through conclusions, Tables 1–4, reference list). The eight figures were read through their captions only. The page metadata states CC BY 3.0 while the footer states CC BY 4.0; the access record keeps both. No PDF is archived. Locators below are section and table numbers.

## Problem and contribution

The authors report a systematic literature review (SLR) that serves as the problem-identification step of a design-science project (Peffers et al. process, Section 3). The project aims to build a framework for the multidisciplinary assessment of organisational maturity in business continuity, with emphasis on ICT-supported processes (Section 3.1). The review asks what strategic guidelines the literature offers for implementing a business continuity plan (BCP), and it looks for gaps that the framework should fill. This is a field-mapping review. It does not evaluate impact-analysis methods, recovery parameters, or prioritization techniques, and it contains no artefact evaluation.

## Method

The protocol follows evidence-based software engineering guidance (Kitchenham) and the Parsifal tool, using a PICOC structure (Section 3.3, Table 1). Intervention terms are "business continuity plan" or "disaster recovery plan" plus guideline, guidance, or strategy. Comparison terms are framework, approach, methodology, procedure, and program. Outcome terms are streamlining synonyms. Scopus, ScienceDirect, and EBSCOhost were searched with Boolean strings (Table 2). Because of ScienceDirect operator limits, thirteen string combinations were used there against seven for the other two databases (Section 4.1).

Inclusion required peer-reviewed publications in English or Portuguese from 2000 onward, with 2015 onward used for the focused set. Studies limited to one industry, one disaster type, one system, or one software product were excluded as not transposable. Quality scoring used six questions and omitted studies scoring below 2.5 points, and data extraction was applied to 393 quality-assessed publications (Sections 3.4, 4.2, 4.3).

## Results actually reported

- **Corpus:** 1297 non-duplicated publications for 2000–2021 (1284 after dropping 2021 for comparison). Annual output averaged 42 publications in 2000–2010 and roughly doubled afterwards. The focused set since 2015 contains 143 publications (Sections 5, 5.1, 5.4).
- **Keywords:** BCP/BC plan/DRP terms account for 34% of publications, risk management or assessment 14%, emergency management 10%, crisis management 6% (Section 5.3).
- **Standards comparison:** ISO 22301:2019, CMMI v2.0, COBIT 2019, ITIL 4, and NFPA 1600 were mapped against common BCM components (Section 2.1, Figure 1). The authors conclude that the standards say how, when, and by whom measurement occurs but leave organisations to decide what to measure, so BC metrics are the main identified gap. BC teams are treated as given in most standards.
- **Component counts (Table 4):** risk assessment 167, BCP design and implementation 163, ICT strategy 129, BCM strategy 121, testing and maintenance 68, business impact analysis 58, understanding the organisation 31, administration support 29, alternatives to critical functions 26, training 20, BC teams 19. Counts overlap because a publication can address several components.
- **BIA (Section 6.3):** of the 58 BIA publications, 15 present BIA frameworks or methodologies (sometimes integrated with risk assessment and BCP), eight relate BIA to information systems or ICT, five concern information and data, six concern recovery objectives, and eleven analyse natural-disaster impact.
- **Definition of business continuity (Section 6.1, Table 3):** the definition is not unique across research objects. The discipline is described as derived from disaster recovery practice of the 1980s, citing Herbane.
- **Measurement and ICT:** about 15% of the focused set establishes a process for measuring BCP implementation, and about two thirds assume ICT-supported processes (Section 5.5).

## Critical reading and limits

1. **Narrow retrieval scope.** The search string requires BCP or DRP together with guideline or strategy terms. The counts therefore describe that filtered corpus. They are not the size of the BIA literature, and the figure of six recovery-objective papers must not be read as a count of all such studies.
2. **Exclusion of context-specific work.** Industry-, disaster-, system-, and software-specific publications were excluded by design. Many BIA case studies would fall under this rule, so the review under-represents them.
3. **Reporting inconsistencies.** Section 5.4 states 143 final publications since 2015 but later refers to "the 63 publications resulting from the SLR". The 2015 cut-off is applied for the focused set while search coverage starts in 2000. Table 3 assigns BIA to a single reference. Descriptive counts are not accompanied by a per-study synthesis.
4. **Project-driven framing.** The review is steered by the authors' own framework goal (maturity assessment), so its identified gap, metrics, reflects that goal and not the field as a whole.
5. **Evidence strength.** Synthesis is quantitative and thematic. The paper does not appraise effect sizes or compare methods.

## Use in the approved chapter

**Primary:** Section 2.1 Business Continuity Management (field overview, non-unique definition of business continuity, the position of standards). **Secondary:** Section 2.2.1 (BIA's share of the literature and the existence of BIA framework papers), Section 2.6 (an SLR embedded in a design-science process), and Section 2.7 (context for gap statements).

Use it for field-level statements such as growth of the literature, the thematic distribution, and the observation that standards leave measurement choices to the organisation. Do not use it to describe how BIA methods derive MTPD or RTO, to claim that recovery objectives are under-studied overall, or to support any TDRP-specific point. Treat the count tables as indicative of the authors' corpus only.
