# Literature Review Chapter: Revision and Change Log

## Scope and alignment

The literature review was rebuilt to align with the thesis title, *A Decision Support System for Business Continuity and Critical Service Recovery Prioritization*, and with the project’s stated contribution: Time-Dependent Recovery Prioritization (TDRP), implemented in the Masar web-based decision-support system. The chapter proceeds from BCM standards and Saudi guidance to BIA, criticality and recovery prioritization, dependency modelling, continuity decision support, research evaluation, and a bounded synthesis of the gap.

The prior LaTeX chapter contained developed material on BCM and BIA but left the central prioritization, dependency, decision-support, methods, and gap sections empty. It also contained drafting language that was not suitable for submission. The rewritten chapter replaces that scaffold with connected academic prose and explicit evidence limitations.

## Chapter structure and substantive changes

The revised chapter:

1. distinguishes BCM, BCMS, resilience, information-system contingency planning, and disaster recovery, and limits claims about standards to the public descriptions actually reviewed;
2. compares ISO catalogue scope, NIST SP 800-34, the National Risk Council framework, and DGA guidance without presenting illustrative thresholds as universal requirements;
3. analyzes BIA units, impact categories, elicitation and operational evidence, time-indexed impact assessment, and the distinct meanings of MTPD/MTD, RTO, RPO, MBCO, and achieved recovery time;
4. compares matrix, data-assisted, financial, optimization, fuzzy multi-criteria, and process-mining approaches, with a separate table of representative studies;
5. distinguishes criticality, priority, recovery targets, and executable recovery sequences, including multi-criteria, rule-based, and constrained optimization approaches;
6. examines dependency types and shared-resource aggregation, while treating the proposed maximum-criticality inheritance rule as a project policy to evaluate rather than a rule mandated by the reviewed guidance;
7. compares selected commercial, open-source, and research systems using public documentation and states that products were not independently installed or tested;
8. relates the artifact to design-science research and separates correctness, implementation verification, traceability, practitioner interpretation, and real-incident effectiveness as different evaluation claims;
9. states a bounded research gap around the documented combination and evaluation of configurable service-level rules, time-dependent impact assessments, recovery requirements, shared dependencies, and traceability. It does not claim that related functions or systems have never existed.

The chapter includes four comparison tables in `tables/` and retains the existing schematic figure on time-dependent impact and recovery parameters. Table and figure content is included from separate files as required by the project structure.

## Introduction change

A chapter-opening paragraph was added to `chapters/introduction.tex`. It previews the four sections using `Section~\\ref{...}` references to the existing labels. Unnecessary emphasis markup around the names TDRP and Masar was removed so that the terms appear as ordinary proper names.

## Sources and citation practice

The chapter uses the existing citation keys in `references.bib` and cites sources with `\\cite{...}`. The bibliography remains configured for IEEEtran. The evidence base includes academic studies, NIST reports, public ISO catalogue records, Saudi guidance, and product documentation. Claims from standards catalogues and vendor pages are identified by their evidence type; product descriptions are not represented as independent product evaluations. The chapter does not rely on the metadata-only Torabi 2014 entry for substantive claims.

The ZoteroCiteLinker repository README describes an MS Word add-in that links Zotero-generated citation fields to bibliography entries through bookmarks and hyperlinks, can change citation color, and includes a separate function for activating bibliography URLs: [sBaydin/ZoteroCiteLinker](https://github.com/sBaydin/ZoteroCiteLinker). This source was consulted when matching the visible linked-citation treatment in the Word document.

## Word document and citation-field limitation

The repository contains `masar-master-project.docx`; the attachment instructions referred to a different name (`Egypt-master-project.docx`), which was not present in the repository. The existing project Word file was therefore used as the template.

The Word version is updated using the university template’s existing heading, body, caption, and bibliography styles. The six existing Zotero citations and the existing Zotero bibliography field are preserved. New citation numbers are blue internal hyperlinks to their bibliography entries, and URLs/DOIs in the appended IEEE-formatted references are clickable. This reproduces the visible citation-to-reference navigation associated with ZoteroCiteLinker.

The cloud environment does not have the user’s Zotero library or desktop Word/Zotero application, so it cannot create or validate new live Zotero-library item IDs or execute the add-in’s VBA macro. Consequently, new chapter citations and added bibliography entries are static linked references rather than newly managed Zotero citation fields. If live Zotero editability is required, the new sources should be imported into the user’s Zotero library and the citations/bibliography refreshed or reinserted in Word, after which ZoteroCiteLinker can be run in Word. The thesis text and its IEEE numbering are preserved in the delivered Word version; this limitation is disclosed rather than represented as completed live-field integration.

## Validation and remaining boundaries

LaTeX source, cross-reference labels, and citation keys were checked during the build. The chapter’s length was checked in the compiled thesis, and the Word document was checked for content, reference order, and rendered layout. Public software documentation remains a purposive, non-exhaustive survey and was not independently tested. No claim is made that the thesis draft constitutes a certification audit, live incident simulation, or evidence of improved recovery performance in actual disruptions.
