# Contingency Planning Guide for Federal Information Systems

## Identity and coverage
Marianne Swanson, Pauline Bowen, Amy Wohl Phillips, Dean Gallup, David Lynes. NIST SP 800-34 Revision 1, May 2010, errata through 11 November 2010. DOI: https://doi.org/10.6028/NIST.SP.800-34r1. Key: nist2010contingency. Complete 149-page PDF obtained. Main chapters 1–5, BIA template B, FAQs C, personnel D, historical controls E, SDLC F, glossary G and supporting lists examined. Appendix A's repeated low/moderate/high plan templates were compared, including different site, recovery and testing instructions. The authority page explicitly states that the publication is not subject to copyright; PDF retained with attribution.

## Scope and lifecycle
The guide concerns federal information-system recovery. Its scope excludes comprehensive business-process continuity and facility-level disaster recovery except as needed to restore systems (§1.2). Chapter 2 distinguishes BCP, COOP, crisis communication, infrastructure protection, cyber incident response, DRP, ISCP and occupant emergency plans. These contextual definitions need not match every modern organization's terminology.

The seven planning steps are policy, BIA, preventive controls, contingency strategies, plan development, testing/training/exercises, and maintenance (Figure 3-1). Plans contain supporting information, activation/notification, recovery, reconstitution and appendices (Chapter 4). Roles, approval, contacts, vendor agreements and procedures complement time targets.

## BIA and recovery parameters
Three BIA tasks identify business processes/recovery criticality, resources, then system-resource recovery priorities (§3.2). Process owners, managers, system owners and interconnected/external contacts provide input. Impact categories and severity scales should express consequences meaningful to the organization. Availability categorization is an input rather than the whole analysis. Figure 3-2 contains notional times, not measured performance.

Maximum tolerable downtime (MTD) is total acceptable process outage. RTO concerns the permitted unavailability of a system resource supporting that process. RTO should normally be shorter than MTD because subsequent work, such as reprocessing, consumes remaining time (§3.2.1, printed p. 17). RPO concerns the pre-disruption point to which data can be restored and tolerated data loss; it is not added as a duration within MTD. Contextual differences between MTD here and MTPD in the thesis must be explained.

Resources include facilities, personnel, equipment, software, data, components and vital records. Priorities combine process criticality, impacts, downtime tolerance and resource relationships (§§3.2.2–3.2.3). Appendix B supports interviews, workshops, email and questionnaires; its template captures process descriptions, impact criteria, MTD/RTO/RPO rationale, workarounds, inventories and recovery priorities. Example dollar values and times are illustrative, not universal thresholds.

## Priorities, strategies and executable recovery
Section 3.4 connects shorter recovery requirements with cost/strategy trade-offs: backups, cold/warm/hot sites, redundancy, equipment replacement and personnel. Cost balancing is a conceptual illustration, not a solved universal optimization model. Chapter 5 discusses client/server, communications and mainframes, secure backups, configuration records, geographic separation and shared failure points; specific technologies reflect 2010.

Operational sequence also needs technical prerequisites: restore/verify the operating system before its application/data (§4.3.1). Activation authority, damage assessment, procurement, team coordination and escalation precede or accompany recovery. Reconstitution validates data/function, notifies users, documents events and returns to normal operations (§4.4). An importance ranking alone does not establish a feasible schedule or successful restoration.

## Evaluation and maintenance
Testing validates operability; training prepares people; exercises examine roles and plans (§3.5). Objectives, success criteria, scope, scenario and after-action findings should be explicit. Tabletop discussions differ from functional/full-scale exercises. Maintenance responds to organizational/system changes and new BIA needs, using version control and protected access (§3.6).

Appendix A supplies plan variants, approval, activation, recovery, data/function validation, contact/inventory/interconnection records and example test schedules. Moderate/high templates add alternate site/storage/telecommunications detail; high-impact treatment includes optional concurrent processing and more demanding failover exercises. Appendices C–I explain FAQs, personnel safety/welfare/communication, historical CP controls, life-cycle integration, definitions and references. They are guidance, not empirical tests of an artifact.

## Limitations and thesis mapping
No participant-based comparison, classification accuracy or causal downtime reduction is demonstrated. Older U.S. policies and SP 800-53 Rev. 3 controls are historical, not a current Saudi compliance checklist. Template schedules should be read with errata and organization-defined frequency language.

Primary §§2.1–2.3; secondary §§2.4–2.7. Useful for definitions, process-to-resource links, documented priorities and independent capability verification. It motivates checking TDRP's configured time relationships and traceability but does not prescribe its exact rules or validate maximum-criticality inheritance. Masar's planning support remains distinct from incident command and technical restoration.
