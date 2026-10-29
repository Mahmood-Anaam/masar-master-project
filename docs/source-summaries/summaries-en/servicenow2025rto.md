# ServiceNow: Calculating RTO and RPO

Key: servicenow2025rto. Yokohama documentation, updated 31 July 2025; read 29 October 2026: https://www.servicenow.com/docs/r/yokohama/governance-risk-compliance/rto-rpo-calculation.html.

The original calculation sections—not the page's generated overview—were examined. Configured impact tolerability and disruption durations determine category downtime; the overall RTO takes the minimum. Without an intolerable rating, a configured maximum applies. Example selection follows alphanumeric rating order, which matters for nonmonotonic inputs. RPO takes maximum response/category scores then a template timeframe mapping. Recovery-tier configuration is required; the original example classifies eight hours as Business Critical.

For §§2.2, 2.3, 2.5 and 2.7, this documents existing configurable temporal rules. It does not establish equivalence to TDRP, its MTPD treatment, dependency inheritance or comparative effectiveness. Documentation was reviewed; software was not tested. Access record only.
