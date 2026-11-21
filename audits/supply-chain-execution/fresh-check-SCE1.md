---
audit: fresh check
unit: SCE1 · The map, the words and the evidence
course: supply-chain-execution · Supply Chain Execution for Product Teams
model: claude-opus-5-5
date: 2026-11-21
chat: https://claude.ai/code/session_01KMmgR2t23jqnYGkyyiMfd9
verdict: fix · 1 errors, 2 should-fix, 24 minor
---

The checker's final report, verbatim, from its hand-back. Saved before any finding was applied.

Verdict: SCE1 · fix · 1 error, 2 should-fix, 24 minor

# Fresh check: SCE1, The map, the words and the evidence

Checker: claude-opus-5-5, isolated agent context, 21 Nov 2026. Live search on.

Read from the packet: unit.md, brief.txt, notes.md, unsure.md, sources.md, sourcing-standard.md (Part 1 and Part 8), case-facts.md, and audit-units-SKILL.md (the §3 prompt and its figures paragraph). There were no audit errata, because the packet holds no audit report for this course.

Web rule kept: every URL fetched was returned verbatim by a WebSearch in this agent, and no refused fetch was retried. Every reference in Sources exists.

## Findings

[error] [figure] §6 table, Cloud ERP row; Current: "| Cloud ERP for Product-Centric Enterprises | 13 Oct 2025 | 9 Nov 2026 |"; Problem: on 21 Nov 2026 the index gives the Product-Centric Magic Quadrant a refresh date of 11/2/26. The date 11/9/26 belongs to Cloud ERP for Service-Centric Enterprises, so the row mixes two markets. Fix: "| Cloud ERP for Product-Centric Enterprises | 13 Oct 2025 | 2 Nov 2026 |"; Basis: Gartner Magic Quadrant index, https://gartner.com/magic-quadrant (read 21 Nov 2026).

[should-fix] [coverage] §8 Gartner; Current: "so this unit does not describe Gartner's axes, criteria or quadrant names from Gartner's own words, and does not describe them from anyone else's."; Problem: the brief asks how an analyst quadrant is made "from the analyst firm's own published method". Gartner's Magic Quadrant FAQ opens at a gartner.com subdomain, which a search in this agent returned, and it gives the axes and the quadrant names. The applier must open the page, log it in sources.md (address, what was read, date) and add it to Sources. Fix: "so this unit does not describe Gartner's evaluation criteria in detail. Gartner's FAQ on the Magic Quadrant, served at a gartner.com subdomain, names the two measures a vendor is placed on, Ability to Execute and Completeness of Vision, and four quadrants, Leaders, Challengers, Visionaries and Niche Players; the page gives no date and does not mention reprints ([Gartner, \"FAQ: How Markets and Vendors Are Evaluated in Gartner Magic Quadrants\", read 21 Nov 2026](https://gcom.pdo.aws.gartner.com/en/about/magic-quadrant-faq)) [analyst]."; Basis: https://gcom.pdo.aws.gartner.com/en/about/magic-quadrant-faq. The page names "Ability to Execute" and "Completeness of Vision" and the Leaders, Challengers, Visionaries and Niche Players quadrants. It shows no date and says nothing about reprints.

[should-fix] [label] §2 region note; Current: "In the United States, the Federal Acquisition Regulation defines the **bill of lading**"; Problem: the FAR governs the federal government's own purchasing. Placed beside the CMR, it reads as the general US commercial definition, and the unit opened no source for that. Fix: "In the United States, the Federal Acquisition Regulation, which governs the federal government's own purchasing (this unit opened no source for the commercial definition), defines the **bill of lading**"; Basis: https://www.acquisition.gov/index%2Ephp/far/47.001 (FAC 2026-01, effective 03/13/2026).

[minor] [accuracy] §6 table, DOM row; Current: "| Distributed Order Management | none shown | 23 Nov 2026 |"; Problem: unverifiable. Neither the www.gartner.com nor the gcom.pdo.aws.gartner.com version of the index, as served to the checker on 21 Nov 2026, had a Distributed Order Management row. The paragraph after the table, which sets the index against the abstract, rests on this row. Re-open the index before filing. If the row is absent, apply the Fix and also delete "while the index read nine days later still showed no last-updated date for it". Fix: "| Distributed Order Management | 12 Nov 2026 (report abstract; no index row confirmed) | not confirmed |"; Basis: https://gartner.com/magic-quadrant; https://gcom.pdo.aws.gartner.com/en/research/magic-quadrant; https://www.gartner.com/en/documents/8617033.

[minor] [label] §2 step 5; Current: "2007, §2.1](https://doi.org/10.1016/j.ejor.2006.07.009)) [independent]."; Problem: the source is a review's list of warehouse activities. That is an account of how the work is done (key Q4), not the source's own finding (Q3). C1 grades §2.3 of the same paper practice, so two readers would split. Fix: "2007, §2.1](https://doi.org/10.1016/j.ejor.2006.07.009)) [practice]."; Basis: unit §10; de Koster et al. 2007 §2.1, https://pure.eur.nl/ws/portalfiles/portal/46713708/DesignandControl_2007.pdf.

[minor] [label] Deliverable B; Current: "| Order picking | Taking ordered goods from storage | de Koster et al. §2.1 [independent] |"; Problem: same as above. Fix: "| Order picking | Taking ordered goods from storage | de Koster et al. §2.1 [practice] |"; Basis: unit §10.

[minor] [label] Deliverable B; Current: "| Cross-docking | Moving goods from receiving to shipping without storing them | Named in de Koster et al. §2.1 [independent]; definition is the course's |"; Problem: same. Fix: "| Cross-docking | Moving goods from receiving to shipping without storing them | Named in de Koster et al. §2.1 [practice]; definition is the course's |"; Basis: unit §10.

[minor] [label] Deliverable B; Current: "| Sortation | Grouping picked goods by order or destination | Named in de Koster et al. §2.1 [independent]; definition is the course's |"; Problem: same. Fix: "| Sortation | Grouping picked goods by order or destination | Named in de Koster et al. §2.1 [practice]; definition is the course's |"; Basis: unit §10.

[minor] [accuracy] §8, Gartner 2024 note; Current: "recommends reading one together with its companion Critical Capabilities report"; Problem: the abstract recommends reading the note itself "in conjunction with a Magic Quadrant and companion Critical Capabilities". Fix: "recommends reading the note together with a Magic Quadrant and its companion Critical Capabilities report"; Basis: https://www.gartner.com/en/documents/5292963.

[minor] [accuracy] §8, Forrester citation rules; Current: "and any slide showing the graphic must carry the disclaimer"; Problem: the guidelines require the disclaimer to be legible on the slide when the graphic is shown in presentations to live audiences, not on any slide. Fix: "and a slide showing the graphic to a live audience must carry, legibly, the disclaimer"; Basis: https://www.forrester.com/staticassets/marketing/about/Forrester_Wave_Citation_Guidelines.pdf.

[minor] [accuracy] §8, Forrester step 6; Current: "for Waves begun on or after 1 July 2024, customer feedback replaced market presence on the graphic."; Problem: the page says Waves that "kick off on or after July 1, 2024, and publish in Q4 2024". Fix: "for Waves begun on or after 1 July 2024 and published from the fourth quarter of 2024, customer feedback replaced market presence on the graphic."; Basis: https://www.forrester.com/marketing/policies/forrester-wave-methodology.html.

[minor] [accuracy] §5, Tandric; Current: "is paid per activity, so a pick it did not record is a pick it cannot bill (case register)"; Problem: the register says warehousing is paid by activity and freight at a margin, with "invoices disputed because activity was not recorded". "Cannot bill" is the unit's inference, credited to the register. Fix: "is paid per activity for warehousing, and its invoices are disputed when activity was not recorded (case register)"; Basis: case-facts.md (Tandric).

[minor] [accuracy] Deliverable A, step 5; Current: "| Stock the record shows and the shelf does not (feeds step 2) |"; Problem: the column is headed "(case register)", but the register records this trouble only at the promise. Placing it at step 5 is the unit's reading, and notes.md does not list it. Fix: "| Stock the record shows and the shelf does not (this unit's reading of the step 2 trouble) |"; Basis: case-facts.md (Corvane, Known trouble).

[minor] [accuracy] Deliverable A, step 6; Current: "| Same as step 2 at the shelf |"; Problem: same as step 5. Fix: "| Same as step 2 at the shelf (this unit's reading) |"; Basis: case-facts.md.

[minor] [style] §2 step 5; Current: "and before accumulation or sortation, cross-docking and shipping"; Problem: these terms are not defined on first use. Fix: "and before accumulation or sortation (grouping picked goods by order or destination), cross-docking (moving goods from receiving to shipping without storing them) and shipping"; Basis: brief, "define each term on first use".

[minor] [style] §2 step 7; Current: "For truckload freight, MIT's FreightLab"; Problem: "truckload" is not defined and is not in the glossary. Fix: "For truckload freight (one vehicle hired for one shipper's load; the course's working definition, sourced in SCE7), MIT's FreightLab"; also add the glossary row "| Truckload (TL) | One vehicle hired for one shipper's load | Course term; SCE7 sources it |"; Basis: brief.

[minor] [style] §3; Current: "and potentially RFID as its transactional foundation"; Problem: RFID is not defined. Fix: "and potentially RFID (radio-frequency identification tags) as its transactional foundation"; Basis: brief.

[minor] [style] §1; Current: "Gartner evaluates planning software in its own Magic Quadrants,"; Problem: Magic Quadrant is used before it is defined. Fix: "Gartner evaluates planning software in its own Magic Quadrants (its dated evaluations of the vendors in one software market; section 8),"; Basis: brief.

[minor] [label] Opening paragraph; Current: "Where this unit could not open a source for something, it says so, and the claim carries no grade because it is not made as a claim."; Problem: lines marked as "this unit's inference" (§1 bullets, §8, §9) and the course's own line (§1) carry mechanisms or recommendations without a grade, and the key does not say how such lines are treated. Part 8 item 4 requires every claim to carry one grade. Fix: "Where this unit could not open a source for something, it says so, and the claim carries no grade because it is not made as a claim. A line marked as this unit's inference, or as the course's own line, carries no grade; it rests on the graded sources it names."; Basis: sourcing-standard.md Part 8.

[minor] [coverage] §11; Current: "\"Not searched here\" means this unit did not look and makes no finding."; Problem: the brief says each common claim is "set against its evidence", but only C1, C2 and C10 (and part of C6) are. The other ten are marked "not searched here". notes.md (Contradictions) proposes a replacement for that line of the brief. Fix: no text change. If Pedro vetoes the brief replacement in notes.md, the unit searches C3–C14 before filing; Basis: brief.txt; notes.md.

[minor] [figure] Figure 3 (decision, §10); Current: "\"q\": \"Did a vendor write, sponsor it or choose who answered?\""; Problem: the label does not match the question in §10. Fix: "\"q\": \"Did a vendor write it, sponsor it or choose who answered?\""; Basis: unit §10, question 1.

[minor] [attribution] Deliverable B, DC/FC row; Current: "| Gartner WMS definition names both [analyst] |"; Problem: Gartner names DC and FC but does not separate them. The split by who receives the goods is the course's. Fix: "| Gartner WMS definition names both [analyst]; the distinction is the course's |"; Basis: https://www.gartner.com/reviews/market/warehouse-management-systems?months=12.

[minor] [attribution] Deliverable B; Current: "| Available-to-promise (ATP) | The quantity that can still be committed to new orders | Gartner DOM definition [analyst] |"; Problem: Gartner names ATP without defining it. Fix: "| Available-to-promise (ATP) | The quantity that can still be committed to new orders | Named in Gartner DOM definition [analyst]; definition is the course's |"; Basis: https://www.gartner.com/reviews/market/distributed-order-management-systems.

[minor] [attribution] Deliverable B; Current: "| Available-to-ship | The quantity that can leave now | Gartner DOM definition [analyst] |"; Problem: same as ATP. Fix: "| Available-to-ship | The quantity that can leave now | Named in Gartner DOM definition [analyst]; definition is the course's |"; Basis: same page.

[minor] [accuracy] §8 inference; Current: "an analyst report read on a vendor's website is a licensed copy chosen by that vendor"; Problem: this is sourced for Forrester, which requires purchased reprint rights. For Gartner it rests only on the brief. Fix: "a Forrester Wave read on a vendor's website is a copy the vendor bought reprint rights for and chose to post (for Gartner, the course's working assumption until SCE17 checks it)"; Basis: Forrester Wave Citation Guidelines; notes.md (Needs).

[minor] [attribution] Sources, Meyr et al.; Current: "*Supply Chain Management and Advanced Planning*. Springer, Berlin, Heidelberg, 2015, pp. 99–106 (abstract)."; Problem: Part 8 requires a textbook's edition. Springer's book page gives the 5th edition (©2015; DOI 10.1007/978-3-642-55309-7). Update S19 in sources.md to match. Fix: "*Supply Chain Management and Advanced Planning*, 5th ed. Springer, Berlin, Heidelberg, 2015, pp. 99–106 (abstract)."; Basis: https://link.springer.com/book/10.1007/978-3-642-55309-7?page=1.

[minor] [attribution] §1, Meyr et al.; Current: "in Stadtler, Kilger & Meyr (eds.), *Supply Chain Management and Advanced Planning*, Springer, 2015, pp. 99–106, abstract read"; Problem: the edition is missing here too. Fix: "in Stadtler, Kilger & Meyr (eds.), *Supply Chain Management and Advanced Planning*, 5th ed., Springer, 2015, pp. 99–106, abstract read"; Basis: same.

Every Current string above was checked by script and occurs exactly once in unit.md.

## The seven passes

**1. References exist and match: PASS.**
- de Koster et al. 2007: EJOR 182(2), 481–501, DOI 10.1016/j.ejor.2006.07.009. Checked against the version of record.
- de Vries et al. 2016: POMS 25(8), 1363–1376, DOI 10.1111/poms.12547. Checked against the SAGE page.
- Meyr, Wagner & Rohde: pp. 99–106, DOI 10.1007/978-3-642-55309-7_5. The 5th edition is not stated in the unit.
- Bartholdi & Hackman: release 0.98, revised 28 Aug 2017.
- Gartner: S1 (19 Mar 2024, three authors), S2 (30 Jun 2025) and S4 (12 Nov 2026, no analysts named) match. S3, S8 and S9 are undated, as the unit says.
- Forrester: S10 (28 Apr 2026) matches; S11 is undated, as the unit says.
- CMR (Geneva, 19 May 1956) and FAR 47.001 (FAC 2026-01) match.
- MHI magazine: 26 Jun 2026, byline Robin Lamerson. It reports MHI and Deloitte's Business Wire release of 15 Apr 2026.

**2. Claims against sources: PASS with findings.**
- One FAIL (Cloud ERP date), one unverifiable (DOM row), four stretches (Gartner 2024 recommendation, Forrester disclaimer scope, Forrester start condition, Tandric billing).
- The unsure list resolves as follows:
  - Quotations confirmed: the Ombuds sentence; the glossary opening; "don’t base your decision on this evaluation only"; the Forrester disclaimer; the Bartholdi & Hackman phrases; the MHI phrase.
  - Bartholdi & Hackman reference [21] is Frazelle, *World-Class Warehousing*, Logistics Resources International, 1996.
  - The Fig. 4 values cannot be read from the extracted text.
  - The de Vries abstract states no country and no sample.
  - The WMS page shows 140 products and no total review count.
  - CMR Art. 1(1) applies where the two countries differ and at least one is a contracting country. The unit's wording does not contradict this.
  - Not resolved: whether MHI owns MHI Solutions magazine.

**3. Grades: PASS with findings.**
- Abstract-only readings are declared for S1, S4, S14 and S19.
- No vendor statement is graded above vendor-reported.
- Gartner's Peer Insights FAQ and market pages are graded analyst, which is correct for Gartner's own pages.
- C1 and C2 are graded practice by origin.
- de Koster §2.1 is graded independent, inconsistently with C1 (four findings above). The key has no rule for inference lines (one finding).

**4. Vendors: PASS.**
- No software vendor is named, assessed, ranked or mapped. §6 gives categories only, and the Peer Insights pages are used without vendor ratings.
- Gartner and Forrester are named for their own published statements. Deloitte and MHI are named as authors of the report under examination.
- No private company's figures appear.
- Halvern, Varnby and Kestrow are labelled "(fictional)" and none is tied to a real company.

**5. The case: PASS with findings.**
- Every first use is labelled "(fictional)": lines 30, 65, 73, 87 and 88.
- Corvane, Ostrel and Tandric facts match case-facts.md, and the owner assignments the unit invented are listed in notes.md.
- Three cells or lines go beyond the register: Tandric "cannot bill", and the step 5 and step 6 trouble cells.
- The case is never used as evidence. C9 names the fictional vendors only as stating the claim, and the vendor-reported worked example is Kestrow's own line.

**6. Scope and tone: PASS with findings.**
- AI appears in one sentence and is set aside. There is no interview framing, no craft method, and nothing about the owner or his employer.
- Tone is direct. "Differentiating rather than exhaustive" paraphrases Forrester's own words.
- Regions are marked, but the FAR's federal scope is not stated (should-fix).
- Terms used before definition: accumulation, sortation, cross-docking, truckload, RFID, Magic Quadrant.

**7. Deliverable and figures: PASS with findings.**
- The deliverable follows the brief's wording in full: A, Corvane's 12-row map; B, a 30-term glossary; C, the grade key with one worked example per grade; D, the template, each blank saying what goes in it.
- "On a site visit" asks questions of colleagues, as the brief asks for a non-operations unit.
- All eight Self-check answers agree with the body.
- Figure 1 (flow, §2) PASS: every label and note traces to lines 32–42.
- Figure 2 (matrix, §3) PASS: every cell traces to lines 58–65, and the caption names the section and sources.
- Figure 3 (decision, §10) PASS on facts: it traces to lines 166–169, with one minor label fix.

## Confirmed (the source of each check)
- Gartner SCE glossary: the opening "Supply chain execution (SCE) is focused on execution-oriented applications"; "generally, Gartner does not include order management in its definition of SCE"; typical modules are labour, yard/dock, returns and inventory control. https://gcom.pdo.aws.gartner.com/en/information-technology/glossary/supply-chain-execution-sce
- Index, https://gartner.com/magic-quadrant:
  - WMS 4/29/26 (refresh 4/30/27)
  - TMS 3/30/26 (refresh 4/22/27)
  - Supply Chain Planning, Discrete and Process, 3/18/26 (refresh 4/7/27)
  - 3PL 3/5/26 (refresh 1/20/27)
  - Cloud ERP for Product-Centric Enterprises 10/13/25
- Seen only on https://gcom.pdo.aws.gartner.com/en/research/magic-quadrant: SCM Suites 8/11/26 (refresh 8/11/27), Global Trade Compliance (11/30/26) and Supply Chain Planning for Retail.
- DOM Magic Quadrant abstract, 12 Nov 2026: the B2B/B2C sentence is exact. https://www.gartner.com/en/documents/8617033
- Peer Insights DOM page (July 2025, 71 products) and WMS page (May 2026, 140 products, no total review count): the definitions match the unit. https://www.gartner.com/reviews/market/distributed-order-management-systems ; https://www.gartner.com/reviews/market/warehouse-management-systems?months=12
- Review Sourcing:
  - vendors invite reviewers through a custom URL
  - incentives must be under $25 and offered to every invited customer, "not just the happy ones"
  - the first 50 approved reviews get a $25 gift card
  - reviewers are validated

  https://blogs.gartner.com/reviews-pages/tpt-faq/review-sourcing/
- Ombuds, 30 Jun 2025: inclusion is "determined solely" by the criteria, and the client-status sentence is exact. https://www.gartner.com/en/about/ombuds/news/how-gartner-experts-work-with-vendors
- Independence and Objectivity: technology providers buy services and exhibit space; the revenue sentence is exact. https://www.gartner.com/en/research/methodologies/independence-and-objectivity
- Gartner 2024 note: "visual snapshots"; "direction, maturity and participants"; narrowing the list; "don’t base your decision on this evaluation only". https://www.gartner.com/en/documents/5292963
- Forrester method, steps 1–5, and its three bands. https://www.forrester.com/marketing/policies/forrester-wave-methodology.html
- Forrester citation guidelines: subscriber or reprint rights to cite; no citing of placement; the disclaimer sentence is exact. https://www.forrester.com/staticassets/marketing/about/Forrester_Wave_Citation_Guidelines.pdf
- de Koster et al. 2007: abstract "as much as 55%"; the §2.1 activity list; §2.3 "travel is often the dominant component"; Fig. 4 credited to Tompkins et al. (2003). https://pure.eur.nl/ws/portalfiles/portal/46713708/DesignandControl_2007.pdf
- Bartholdi & Hackman 0.98:
  - §1.2, pp. 8–9: the quotes match.
  - Ch. 3: "scanned at all key decision points".
  - §3.3, p. 25: the two 55% figures, both citing [21].
  - Ch. 4 introduction: the WMS knows every item, makes pick lists, tracks assembly, talks to a YMS, sends summary data to an SCMS, and tracks worker productivity.
  - §4.1: "drives the paying of bills to suppliers upstream".
  - §4.3: labour management is a high-end feature.

  https://www2.isye.gatech.edu/~jjb/wh/book/editions/wh-sci-0.98.pdf
- de Vries et al. 2016 abstract: the setting, the results, and "No effects on order picking quality were identified". https://journals.sagepub.com/doi/10.1111/poms.12547
- Meyr et al.: APS are built from several modules. https://rd.springer.com/chapter/10.1007/978-3-642-55309-7_5
- MIT FreightLab: "routing guides" holding "pricing, assignments, and priority logic"; exchanges complement the catalogue. https://freightlab.mit.edu/optimization-based-transportation-procurement
- CMR Arts. 4 and 5(1). https://treaties.un.org/doc/Treaties/1961/07/19610702%2001-56%20AM/Ch_XI_B_11.pdf
- FAR 47.001 bill of lading definition. https://www.acquisition.gov/index%2Ephp/far/47.001
- MHI magazine: "based on a survey of supply chain leaders", with no sample stated. https://www.mhisolutionsmag.com/index.php/2026/06/26/new-mhi-and-deloitte-report-finds-ai-is-biggest-disruptor-of-supply-chains-over-the-next-decade/

## Part 8, line by line
1. Claims sourced where made: yes.
2. Acceptable source types: yes. The treaty and the regulation are raised in notes.md.
3. No banned sources: yes. The MHI magazine article is named only as the claim under examination.
4. Grades follow the key: partly, because of de Koster §2.1 and the inference lines.
5. Reading mode stated for analyst reports: yes.
6. No vendor assessed: yes.
7. Vendor naming rule: yes.
8. Fictional vendors labelled: yes.
9. Peer-review counts: the unit says none is available.
10. Whose figure, sample and year: yes.
11. Study sample, setting and design: yes.
12. Common claims: named, but ten are not searched (minor).
13. Source log: yes. It must add the Gartner FAQ if that finding is applied.
14. Records match: yes, except the 5th edition.
15. Case: yes, with three minor over-attributions.
16. Private terms: nothing found by reading. `kit/private_terms.py` is not in the packet and was not run.
17. No AI, interview framing or method: yes.
18. Dates on analyst lists: yes.
19. Deliverable in full, then template: yes.
20. Site visit and Self-check: yes.
21. Not advice without evidence: yes.
22. Links as links: yes.

## As the reader
- §§1–5 can be followed in order by a reader with no operations background.
- The map, the systems table and the grade key are usable alone.
- The "working placement" and "not searched here" cells are honest but leave TMS, ERP and WCS/WES thin; these are pointers to later units.
- On a phone, the 7-column template and the §11 table will need horizontal scrolling. This is not a finding.
