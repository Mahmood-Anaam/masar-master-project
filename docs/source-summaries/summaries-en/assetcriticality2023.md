# A BIA-Based Quantitative Framework for Built Physical Asset Criticality Analysis under Sustainability and Resilience

## Identity and coverage

**Authors:** Mohsen Aghabegloo, Kamran Rezaie, S. Ali Torabi, Seyed Mohammad Khalili. **Publication:** *Buildings*, 13(1), article 264, 2023. **DOI:** https://doi.org/10.3390/buildings13010264. **BibTeX:** `assetcriticality2023`. The complete 30-page publisher PDF was examined. The separate online supplement, which contains further fuzzy-method calculations, was not examined. The paper is CC BY 4.0; retain author attribution and its embedded licence notice when sharing the unmodified PDF.

## Research problem and approach

The paper connects business continuity with physical asset management: limited resources prevent equal investment in continuity plans for every asset. Asset priority should reflect the products/services it enables and economic, social, environmental, and resilience considerations. The proposed framework has three stages: identify key products, identify and rank their supporting physical assets, and analyse which factors most affect asset criticality (PDF pp. 7–15).

Product selection uses fuzzy best–worst weighting and fuzzy TOPSIS. Supporting assets are identified using process diagrams and piping/instrumentation diagrams. Fuzzy DEMATEL elicits relationships between assessment criteria. Those relationships are transformed into a directed acyclic Bayesian network; experts review correlations, causal interpretations, and thresholds to remove cycles. This network represents dependencies among **criticality criteria**, which should not be confused with a simple map of services sharing resources (pp. 9–14).

## Model and data

Sustainability is represented by economic, social, and environmental factors. Resilience includes absorptive, adaptive, and restorative capacities, operational loss, an asset recovery point, recovery time, and total restoration time. The paper calculates loss and resilience from an illustrative degradation/recovery geometry; these quantities do not constitute a general service-impact-to-MTPD algorithm.

The asset criticality index is a weighted sum of factor-criticality probabilities, conceptually `ACI_i = sum_j w_j P(factor_j is critical for asset_i)`. Defuzzified factor weights come from fuzzy BWM. Expected criticality is recalculated with a contributor set to a critical condition; normalising these expected values produces a contributor-priority measure, NEACI (Equations 6–7, pp. 14–15). This is a probabilistic multi-criteria aggregation, not highest-service-criticality inheritance.

Inputs combine expert judgements, site history, and quantitative risk-assessment scenarios. Variables include equipment and maintenance costs, production losses, leakage, fluid hazards, pressure/temperature, flaring, protective equipment, backup assets/contractors, spare parts, and skilled repair personnel. The worked network mixes probability distributions, discrete states, and deterministic conditional rules. For example, restoration capacity is connected to spare parts and repair personnel; sustainability and resilience factors can therefore interact (pp. 16–22).

## Case evidence and results

The gas-plant case considers propane, butane, sulfur, and condensate. Four managers supply product-criterion comparisons; condensate is selected, with reported TOPSIS closeness 0.987. Product criteria include revenue loss, reputation, national importance, customer defection, and stakeholder support. The model is implemented using GeNIe. A criterion-link threshold changes from 0.50 to 0.52 to remove a cycle. Reported crisp weights are economic 0.367, social 0.207, environmental 0.104, and resilience 0.322 (pp. 15–24).

The asset-index results identify PA4 and PA2 as the most critical. Contributor analysis ranks equipment costs first, production loss second, and air pollution third; backup-asset availability is last in that particular setting (pp. 24–25). These are case-dependent outputs, not recommended universal rankings. Validation combines expert face-validity questions about network structure/parameters and sensitivity analysis. Data are available from the authors on request, rather than as a fully packaged open replication dataset (pp. 24–26).

## Limitations and useful cautions

The main text contains a reporting inconsistency: §4.2 initially identifies eight equipment items, while subsequent results discuss ten assets, PA1–PA10. Preserve this discrepancy when describing sample size; do not silently choose one count. Several PDF figures/tables have duplicated extraction layers, so visual verification is necessary for exact numerical reproduction. The network structure and elicited probabilities are context-dependent. Raising the DEMATEL threshold affects the network; it is not a proof that the omitted relation is unimportant in every organization. Face validity supports plausibility, not measured forecasting accuracy or improved recovery in live incidents.

The authors propose application in other industries, including services, and further integration of alternative decision methods as future research. The paper does not derive MTPD/RTO from a service's successive impact ratings and does not validate a maximum-criticality inheritance rule.

## Relevance and writing map

**Primary:** §2.3.1 Multi-Criteria Approaches and §2.4.3 Criticality of Dependencies. **Secondary:** §§2.2.4, 2.6, 2.7. It is valuable evidence that continuity-oriented asset prioritization already has explicit quantitative methods, including configurable criteria and dependence modelling. Compare its information demands, aggregation semantics, uncertainty representation, and evaluation with TDRP. Position Masar through its bounded method and traceability requirements, not by claiming that earlier work ignores business-service relationships.
