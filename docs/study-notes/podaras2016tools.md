# Podaras, Antlová and Motejlek (2016): Business Continuity Testing Points

- **DOI:** https://doi.org/10.15240/tul/001/2016-1-012
- **Full text:** `../studies/podaras2016tools.pdf`, 18 pages; read completely, 16 October 2026.
- **Design:** Analytical method construction using Use Case Points, ranked factor weights, and illustrative scenarios.
- **Evidence:** Method rationale, pp. 165–170; actor/process classification and weights, pp. 171–177; effort mapping and future validation, pp. 178–180.

## Findings and critique

BCTP adapts Use Case Points to human/application actors, process complexity, and technical, environmental, and unexpected recovery factors. Rank Order Centroid weights support calculations of recovery points and an illustrative recovery-time-effort mapping. The method links criticality and exercise categories and compares estimated effort with recovery requirements. Actual organizational validation is explicitly future work.

This is a close conceptual comparator, not evidence that explicit recovery rules are absent from prior research. Its inverse mapping between recovery points and permitted effort reflects the urgency assigned to critical functions; agreement with selected time bands is not independent evidence of achievable recovery duration. Complexity, business tolerance, and capacity should not be collapsed into one construct. The paper also uses terminology such as “Rational Time Objective” inconsistently with standard RTO usage; Masar should retain its own clearly sourced definitions.

## Implication for Masar

Separate business tolerance, approved targets, and tested technical capability. Treat weights and time bands as reviewable configuration, not universal constants. Include exception cases and validate outputs independently. Do not copy the illustrative hours or factor weights as TDRP requirements.
