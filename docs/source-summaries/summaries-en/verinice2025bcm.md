# verinice: Business Continuity Management domain (SerNet)

## Identity and reading basis

verinice is an information-security management tool published by SerNet GmbH, with a business continuity management domain. Key `verinice2025bcm`. The BCM domain page (https://verinice.com/en/solutions/domains/business-continuity-management) was read in full on 29 October 2026. Two other public pages were available only as search excerpts, and the tutorial documentation for the BCM domain was not reached, so statements below carry an evidence label: **[page]** read in full, **[excerpt]** from a search-result excerpt.

## What the sources say

- **Standards and purpose [page].** verinice supports business continuity or emergency management systems according to ISO 22301 or BSI Standard 200-4 across the PDCA cycle. The page says users capture business processes, identify and optimize important processes and critical infrastructures, evaluate dependencies, and continuously work on the business impact analysis. It describes the tool as highly customizable and as combining BCM, information security, and data protection management.
- **Open-source status [page, excerpt].** The page states that verinice has been produced completely as open source by SerNet since 2006. The product-page excerpt describes the classic application as GPLv3 open-source software. The BCM page also mentions a newer web-based generation (cloud and on-premises offerings), for which the licence was not verified.
- **Dependencies and BIA view [excerpt].** A news item about the BSI 200-4 product describes a new business impact analysis view with a graphical representation of process and resource dependencies, a requirements catalogue, sample data, and standard reports.
- **Impact inheritance [excerpt].** The product-page excerpt says assets can be linked with processes and owners and that business impact values can be inherited automatically in the asset tree. The excerpt does not state whether the rule is maximum-based, nor whether it applies to the BCM domain.

## Reading for the project

- verinice is the clearest open-source example in the reviewed set of a **BCM domain with BIA, dependency views, and (in the classic product) inheritance of business-impact values through an asset tree**. It supports a careful statement that open-source tools cover BIA recording and dependency analysis, and that inheritance of impact values is not new.
- Nothing reviewed shows **time-indexed impact thresholds, automatic MTPD or RTO derivation, or configurable rule evaluation** in verinice. Those are unknown for this review, not absent.
- The sources are marketing and product pages and give no validation, usability, or performance evidence.

## Use in the approved chapter

**Primary:** Section 2.5.3 Continuity Management Software (open-source category) and the comparison in Section 2.7. **Secondary:** Section 2.4.3 (inheritance of impact values in an asset hierarchy). Cite it as vendor and project documentation, and state the evidence labels when relying on the excerpt statements.
