# PRECESION: Progressive Recovery and Restoration Planning of Interdependent Services in Enterprise Data Centers

## Identity and reading basis

- **Authors:** Ibrahim El-Shekeil, Amitangshu Pal, Krishna Kant (Temple University).
- **Published:** *Digital Communications and Networks*, 2017 (received 26 February 2017, accepted 4 August 2017). DOI https://doi.org/10.1016/j.dcan.2017.08.001. BibTeX key `elshekeil2017precesion`.
- **Text examined:** the complete in-press PDF (pp. 1–9) including all equations, tables, and the reference list. Figures were read through captions and the surrounding text. The in-press copy carries no final volume or page numbers, so locators below are the article's own section and equation numbers. The article states a CC BY-NC-ND 4.0 licence; no PDF is archived.

## Problem and contribution

After a partial or full disruption of an enterprise data center, services cannot all be restored at once because they depend on each other and on a limited number of skilled workers. The paper formulates progressive recovery planning (PRECESION): the order in which servers are restored so that the weighted availability of user-request types over the whole recovery horizon is maximized (Section 1, Eq. 1). It is a sequencing and scheduling study. It takes disrupted components and their dependencies as given, and it does not decide which services are important. Importance enters only through given weights on user-request types.

## Model

**Three-layer dependency structure (Section 2.1, Figs. 2–3, Table 1).** Layer 1 holds user-request types, layer 2 services, and layer 3 servers. Inter-layer dependencies (a user request needs services, a service needs servers) and intra-layer dependencies (for example, email and HR services depend on DNS and Active Directory, and a web server depends on an application server that depends on a database server) are binary matrices (H, Q, S, P, O). A service is available only when all required servers are fully restored.

**Timing and workers (Section 2.1).** Time is discretized in slots. Restoring a server has an exclusive phase, in which a named expert must work on it, and a shared phase, which ordinary operators can finish. A small set of workers, with skill-based eligibility (R), rotates across servers.

**Objective and constraints (Section 2.2, Eqs. 1–18).** The objective maximizes the sum, over user-request types and time slots, of weights multiplied by an availability indicator. The weights are proportional to the number of users in each type. Constraints enforce dependency order (Eqs. 2–6, linearized from products), timing of exclusive and total restoration (Eqs. 7–10), worker eligibility and non-overlap (Eqs. 11–13), and monotone availability (Eqs. 14–18). The problem is shown NP-hard by reduction from minimum latency set cover (Theorem 1). A worked example with four user-request types, five services, and three servers shows that shared prerequisite services (A1 and A3) force servers 1 and 2 to be restored first (Section 2.3).

**Heuristic (Section 3).** A genetic algorithm encodes a chromosome as a server restoration sequence and generates only sequences that respect precedence via a candidate-server-set rule. Workers are assigned by a Hungarian-method bipartite matching, followed by greedy assignment as workers become free. The algorithm uses elitism, roulette-wheel selection, two-point crossover, and mutation, and stops when fitness no longer improves.

## Evaluation and reported findings

- **Synthetic validation (Section 4.1):** five user-request types, 17 services, 24 servers, exclusive times of 10–180 minutes, and total restoration times of 50–700 minutes. The heuristic reached 99% of the optimal user satisfaction obtained with the PuLP solver, and ran over 2800 times faster, with the exact solver exceeding 150 hours. Increasing workers from three to five raised satisfaction by only about 0.5%, because long shared phases and prerequisites left workers idle more than 80% of the time.
- **Anonymized real data center (Section 4.2):** a medium-size company with 15 user-request types, 60 services, and 107 servers (mean 4.5 services per request type, 1.8 servers per service). Three worker/skill cases were tested. With all workers fully skilled, uptime gains were 6–9% when moving from three to four and from four to six workers, 2–3% around ten workers, and below 1% beyond that. Skill-limited cases showed non-monotone gains and rising idle time.
- The abstract reports a speed-up range of 600–2800 times against the exact solver.

## Critical reading and limits

1. **Accuracy was validated only on synthetic scenarios.** The comparison with the optimal solution is reported for the synthetic instance. The real-data section reports heuristic behaviour across worker cases and does not report an optimality gap, so the abstract's phrase about real-world examples should not be read as an optimality check on real data.
2. **Simplifying assumptions stated by the authors (Section 6).** A service is treated as fully on once all its servers are up. Partial service, security patching before restoration, and multi-step restores (backup then logs) are not modeled. The worker count and skills are given.
3. **Importance is exogenous.** User-request weights are proportional to user counts and are inputs. There is no impact-over-time function, no tolerable-disruption threshold, and no MTPD or RTO in the model, and no mechanism for deriving service criticality.
4. **Single anonymized dataset.** The company is not identified, the dependency data cannot be inspected, and the synthetic dependencies are artificially generated (Section 4.1).
5. **Unclear extraction detail.** The text extraction gives the recovery duration in Fig. 1 as "approximately 3020 hours", which looks like a formatting artifact; the figure should be checked in the original before any number is quoted.
6. **Weight scale.** Objective weights are non-comparable across organizations because they are user-count shares. Nothing is reported about sensitivity to the weights.

## Use in the approved chapter

**Primary:** Section 2.3.3 Recovery Sequencing. It is a clear published example of recovery order being driven by dependency prerequisites, restoration durations, and worker capacity, so it shows concretely why an importance ranking is not an executable recovery sequence. **Secondary:** Section 2.4.1 Service Dependencies (a three-layer user–service–server dependency formulation with intra-layer prerequisites), Section 2.4.2 (a data-center-specific, restoration-oriented view of interdependency), and Section 2.7 (boundary with TDRP).

Pair it with `sahebjamnia2015integrated`, and keep the contrast explicit: that paper optimizes operating levels and resource allocation over time from BIA inputs, while this one optimizes server restoration order under given weights. Use it to support statements about recovery sequencing needing prerequisites, durations, and capacity. Do not use it to argue that service-first rule-based prioritization is invalid or inferior, since it addresses a different decision and offers no comparison with rule-based ranking.
