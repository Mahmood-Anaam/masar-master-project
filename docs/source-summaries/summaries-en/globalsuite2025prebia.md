# GlobalSuite Solutions: Pre-BIA (user manual page)

## Identity and reading basis

Vendor help page for the GlobalSuite platform, key `globalsuite2025prebia`, URL https://help.globalsuitesolutions.com/en/globalsuite/v1/pre-bia. The page metadata shows a last modification date of 23 December 2025, and it was read in full on 29 October 2026. Only the text was reviewed (screenshots and linked pages were not), and no software was tested. Everything below is the vendor's documented behaviour.

## What the page documents

**Service-level impact table over time.** A Pre-BIA is created for one service from a service catalogue. The analyst fills a table of impacts against a time scale, choosing for each cell a rating from Very Low to Very High. The impact categories and the time scale are configured beforehand in the application's configuration section. A graph can show each impact, the maximum impact per time point, and the MTPD.

**Automatic or manual MTPD.** The responsible user can either enter the maximum interruption time manually or let the platform calculate it. Three automatic criteria are described: *first impact* (the MTPD is set when the first impact level found matches the scale level the user defined), *first impact average* (when the average of the impacts matches the chosen level), and *first impact of type* (when the first level of one specific impact type matches). The page also records a minimum operating level (the minimum processes and resources needed to provide the service), a confidence level in the measure, a resumption deadline for returning to normal operating levels, and a justification note.

**Consolidation across departments.** Several individual Pre-BIAs for the same service can be consolidated, manually or automatically. Automatic consolidation uses average, weighted average (with importance weights per Pre-BIA), maximum, or minimum, either the same rule for all impact types or a different rule per impact type. Graphs by department and by impact type support manual consolidation. The consolidated Pre-BIA is then used to obtain the MTPD and minimum operating levels in the same way as an individual one.

## Reading for the project

- The documented logic is close in spirit to a threshold rule over a service-level impact table indexed by time, with configurable scales, so it is evidence that **temporal threshold-based MTPD derivation and configurable impact scales already exist in commercial products**. It must not be described as new to the field.
- The manual describes how the first matching level is found, not tie handling, missing time periods, non-monotonic ratings, or the behaviour when no level is reached. Those are **unknown**, not absent.
- The page does not describe RTO derivation, dependency inheritance, or service ranking in the reviewed text, and it says nothing about validation or measured outcomes.
- "First impact" wording is ambiguous about whether it is the earliest time or the first listed category; the reviewer's reading is the earliest time at which a rating reaches the chosen level, but this is an interpretation.
- The page is documentation, and the reviewer did not check that the product behaves as written.

## Use in the approved chapter

**Primary:** Section 2.5.3 Continuity Management Software (a documented configurable MTPD calculation with consolidation rules and confidence). **Secondary:** Section 2.3.2 Rule-Based Approaches (commercial examples of rule options such as maximum or weighted aggregation), Section 2.2.3 (time-indexed impact rating tables), and Section 2.7 (prior art that bounds any novelty claim). Cite it as vendor documentation, together with `servicenow2025rto`, and distinguish documented capability from validated effectiveness.
