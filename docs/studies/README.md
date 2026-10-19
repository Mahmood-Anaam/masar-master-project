# Studies reviewed for Chapter 2 (Literature Review)

This folder documents every source cited in `chapters/literaturereview.tex`: bibliographic data, DOI where one exists, what was actually read, a detailed summary, and how the source is used in the chapter. Citation keys match `references.bib`.

## How the sources were gathered and read

- The two Saudi documents (`docs/assets`) were treated as the principal sources. The National Framework PDF could not be extracted as text (the Arabic text was garbled), so the relevant pages were read through OCR (Tesseract, Arabic) and one page was checked visually. The DGA guideline was read through text extraction.
- Academic studies were located through web searches of publisher, repository and indexing records. Where the open full text could be fetched it was read; otherwise the abstract and bibliographic record were used. The access level of each source is stated in its own file. Statements in the chapter about abstract-only sources are limited to what the abstracts report.
- Commercial platforms were examined through public vendor documentation. Their internal algorithms are not visible, and the chapter says so.
- Metadata (authors, venue, volume, pages, DOI) was verified against at least one repository, index or publisher record. Items whose metadata is incomplete are flagged in their files (Aghabegloo et al. 2024: volume and pages; Cedergren and Hassel 2025: article number).

## Index

| Source | Key | Type | DOI | Access |
|---|---|---|---|---|
| [National Framework (NRC)](nrcnationalframework.md) | `nrcnationalframework` | Official national framework (primary source) | See file | Selected sections (OCR) |
| [DGA guideline](dga2025bcm.md) | `dga2025bcm` | Official guideline (primary source) | See file | Selected sections (text) |
| [ISO 22301:2019](iso22301.md) | `iso22301` | International standard | None found/used | Standard/guidance, not fully read |
| [NIST SP 800-34 Rev. 1](nist80034.md) | `nist80034` | Government guidance (IT contingency planning) | 10.6028/NIST.SP.800-34r1 | Standard/guidance, not fully read |
| [Gibb and Buchanan (2006)](gibb2006framework.md) | `gibb2006framework` | Journal article | 10.1016/j.ijinfomgt.2005.11.008 | Abstract / record |
| [Niemimaa (2015)](niemimaa2015review.md) | `niemimaa2015review` | Journal article (literature review) | 10.17705/1CAIS.03704 | Abstract / record |
| [Jarvelainen (2013)](jarvelainen2013incidents.md) | `jarvelainen2013incidents` | Journal article (survey-based validation) | 10.1016/j.ijinfomgt.2013.03.001 | Abstract / record |
| [Fani and Subriadi (2019)](fani2019multiusable.md) | `fani2019multiusable` | Conference paper (open access) | 10.1016/j.procs.2019.11.124 | Full text |
| [Labus et al. (2020)](labus2020adaptive.md) | `labus2020adaptive` | Journal article (open access) | 10.2298/CSIS190202037L | Abstract / record |
| [Torabi et al. (2014)](torabi2014framework.md) | `torabi2014framework` | Journal article | 10.1016/j.ssci.2014.04.017 | Abstract / record |
| [Sahebjamnia et al. (2015)](sahebjamnia2015integrated.md) | `sahebjamnia2015integrated` | Journal article | 10.1016/j.ejor.2014.09.055 | Abstract / record |
| [Rezaei Soufi et al. (2019)](rezaeisoufi2019quantitative.md) | `rezaeisoufi2019quantitative` | Journal article | 10.1080/00207543.2018.1483586 | Abstract / record |
| [Aghabegloo et al. (2023)](aghabegloo2023bia.md) | `aghabegloo2023bia` | Journal article (open access) | 10.3390/buildings13010264 | Abstract / record |
| [Aghabegloo et al. (2024)](aghabegloo2024integrating.md) | `aghabegloo2024integrating` | Journal article | 10.1016/j.eswa.2023.122737 | Abstract / record |
| [Rinaldi et al. (2001)](rinaldi2001identifying.md) | `rinaldi2001identifying` | Magazine article (conceptual framework) | 10.1109/37.969131 | Abstract / record |
| [Redlich et al. (2014)](redlich2014mdbia.md) | `redlich2014mdbia` | Conference paper | 10.1145/2568088.2576797 | Full text |
| [Zambon et al. (2011)](zambon2011qualtd.md) | `zambon2011qualtd` | Journal article | 10.1007/s10270-010-0166-8 | Abstract / record |
| [Schatter et al. (2019)](schatter2019decision.md) | `schatter2019decision` | Journal article | 10.1016/j.dss.2018.12.006 | Abstract / record |
| [Cedergren and Hassel (2025)](cedergren2025public.md) | `cedergren2025public` | Journal article (scoping review) | 10.1111/1468-5973.70055 | Abstract / record |
| [ServiceNow BCM](servicenowbcm.md) | `servicenowbcm` | Commercial platform (vendor documentation) | None (vendor documentation) | Vendor pages |
| [Fusion Risk Management](fusionrm.md) | `fusionrm` | Commercial platform (vendor web pages) | None (vendor web pages) | Vendor pages |
| [GlobalSUITE](globalsuite.md) | `globalsuite` | Commercial platform (vendor help documentation) | None (vendor help center) | Full text |
| [Hevner et al. (2004)](hevner2004design.md) | `hevner2004design` | Journal article (methodology) | 10.2307/25148625 | Not re-read |
| [Peffers et al. (2007)](peffers2007dsrm.md) | `peffers2007dsrm` | Journal article (methodology) | 10.2753/MIS0742-1222240302 | Not re-read |

## Recommended follow-up before submission

1. Obtain the full texts of the abstract-only items from the King Saud University digital library and check each statement made about them in the chapter (priority: Torabi et al. 2014, Sahebjamnia et al. 2015, Rezaei Soufi et al. 2019, Labus et al. 2020, Zambon et al. 2011).
2. Read ISO 22301:2019 and NIST SP 800-34 Rev. 1 directly if more than the general statements made in Section 2.2.1 are required.
3. Complete the missing metadata flagged above.
4. The reference list contains 24 entries. The programme guidelines expect 20 to 30 references for the final report, so the list is within range, and further studies can be added in the same format.

## Chapter structure (for reference)

Chapter 2 runs from the general to the specific: 2.1 overview and review approach; 2.2 BCM concepts and the IS perspective; 2.3 the Saudi regulatory context (National Framework, DGA guideline, synthesis); 2.4 business impact analysis and recovery parameters; 2.5 dependencies and criticality; 2.6 information systems for continuity decisions (academic proposals and commercial platforms); 2.7 comparative analysis and research gap; 2.8 summary. Tables: 2.1 recovery-time guidance in the Saudi sources; 2.2 National Framework versus DGA guideline (sideways); 2.3 commercial platforms (sideways); 2.4 academic studies (sideways); 2.5 capability comparison (sideways).
