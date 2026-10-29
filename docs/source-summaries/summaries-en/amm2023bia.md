# Business Impact Analysis of AMM Data: A Case Study

## Identification and scope

**Author:** Josef Horalek. **Publication:** *Applied System Innovation*, 6(5), article 82, 2023. **DOI:** https://doi.org/10.3390/asi6050082. **BibTeX:** `amm2023bia`. The 30-page publisher PDF is CC BY 4.0. Reading covers its technical/data-flow description, assessment criteria, temporal matrices, asset findings, discussion, and conclusions. Page references below use PDF pagination.

## Purpose and setting

This case combines a technical account of Automated Meter Management (AMM) with business-impact and information-security assessments at Czech electricity distributor ČEZ Distribuce. It seeks to justify protections for the datasets and systems supporting smart metering. The organization serves more than three million customers, but this is **not** the number of research respondents. The methodology combines public scientific/technical material, knowledge of the distribution environment, and repeated guided interviews with dataset sponsors and owners. A respondent count and inter-rater agreement statistic are not reported in the main methodological account (pp. 3–5).

## Assessment structure and data model

The paper identifies seven principal dataset groups: LP15, LP60, billing values (BW), disconnect instructions (ODP), reconnect instructions (PRIPO), tariff/control messages (TAR), and power limitation (BLOCK). It traces their movement between meters, telecommunications/base stations, the data centre, reading/validation, accounting, customer systems, the market-operator interface, and field staff. Tables of OBIS registers and electrical-market aggregation equations explain the technical context; they are not the recovery-priority algorithm (pp. 5–10).

CIA classification uses A–D categories. Business-impact criteria address legal/contractual obligations, organizational operation, essential service provision, confidence/reputation, and financial loss. Availability is assessed over 30 minutes, 2 hours, 12 hours, 24 hours, 2 days, 1 week, and more than 1 week. Other columns concern backup gaps, total data loss, disclosure, and accidental/deliberate errors. Eleven system/asset entries are assessed in the main matrix (Table 12, p. 17).

MTPD represents the time band at which high impacts arise; the paper also defines a medium-impact disruption period (MIPD) and maximum tolerable data loss (MTDL). It discusses RTO and RPO subject to the stated relationships RTO ≤ MIPD, RTO ≤ MTPD, and RPO ≤ MTDL (Tables 7–10, pp. 14–15). These are definitions and choices within this case; MIPD is not a project deliverable to add automatically to Masar. Ratings and legal thresholds are organization/sector-specific.

## Findings and practical recommendations

Tables 13–23 give asset-level judgements and temporal requirements. The discussion identifies the data centre, reading/validation system, and accounting system as particularly vulnerable. Dataset findings distinguish meter-control messages from information-only customer data, and note that integrity or disclosure consequences can differ from downtime consequences. The timing of an outage relative to billing or reporting deadlines matters (pp. 16–27).

Examples of reported MTPD values include two days for BTS and reading/validation, one week for the data centre, more than one week for the customer system, and 12 hours for accounting. These illustrate differing tolerability assumptions; they are not proposed defaults for other organizations. The paper recommends role-restricted access, network separation, encryption, backups, alternative systems, controlled credentials, supplier obligations, and periodic audits. Its closing cryptographic recommendations are historical, domain-specific recommendations, not independently verified current security advice (pp. 25–28).

## Quality and interpretation cautions

The paper documents contextual reasoning and a worked assessment, rather than a comparative trial of recovery outcomes or an evaluated configurable DSS. Several internal inconsistencies matter for reuse:

- Table 6 uses four impact grades, while the text introducing Table 12 describes a five-point scale including “none.” Do not merge the numerical scales silently.
- The accounting row in Table 18 reports MTPD 12 hours and MIPD 2 days, which needs clarification against the stated threshold meanings. Do not copy this pair as a validated rule.
- Some labels vary (MIPD/MIDP; system acronyms); distinguish editorial variation from a new concept.
- Qualitative discussion and tabulated temporal bands are not always perfectly aligned. Preserve locators and describe reported judgements without asserting a fully reproducible universal derivation.

The case does not quantify whether the proposed controls achieved the stated recovery times in actual incidents. Extensive interview reasoning provides context, but no automated implementation, open replication dataset, or independent inter-rater validation is established by the paper. Its claims about national laws are historical case context and should not be used as current legal guidance.

## Application to the review

**Primary:** §2.2.2 Time-Dependent Impact Assessment and §2.2.3 Recovery Parameters. **Secondary:** §§2.2.4, 2.4.1, 2.6, 2.7. This is strong evidence that temporal impact matrices, explicit impact criteria, recovery parameters, and technical dependencies have already been connected in a practical BIA case. It helps motivate TDRP's need for explicit scale definitions, boundary handling, validated mappings, and traceability. It does not establish highest-criticality inheritance or show that Masar's proposed methodology is absent from every other system.
