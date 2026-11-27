claude-opus-5-5

Verdict: SCE8 · keep · 0 error, 2 should-fix, 10 minor

out/report.md was not written. The Write tool refused it under a harness rule that subagents return findings as text. I did not use the Python fallback, because the instructions say not to work around a harness refusal. The full report is below. I deleted the working-notes stub I had left in out/, so out/ is empty.

Quality review of SCE8 (The transport system as a product), run 27 November 2026 by a fresh agent with live search, not shown the writing or any earlier check. Every Current string was checked by script against unit.md and occurs exactly once.

Summary: 31 claims or claim groups confirmed, 17 claims could not be verified. Of the unit's 23 Sources entries, 22 opened live. The Peer Insights TMS page failed to fetch and was not retried, and Gartner's abstract page also failed. No reference fails to exist.

## Findings

[should-fix] [accuracy] §7; Current: "Three lines (T6, T22, T23) are needs the analyst definitions read here do not name; two of them are the provider's."; Problem: the unit's own table shows six lines that no analyst definition names. T6, T15, T22 and T23 say "no analyst list names it", T11 rests only on a course term, and T19 is "Working; no source opened". The count is wrong and the deliverable C summary leans on it; Fix: "Six lines (T6, T11, T15, T19, T22, T23) are named by none of the analyst definitions read here; two of them (T22, T23) are the provider's."; Basis: unit §7 table; Gartner MQ TMS 2026 reprint, https://lp.shipsy.ai/hubfs/Shipsy%20Content%20Library/Gartner/Gartner%20MQ%20TMS%202026.pdf
[should-fix] [attribution] Deliverable B, row 10; Current: "its record of each load, margin included, can be reviewed by the parties"; Problem: the cited source does not say "margin included". Read live, the FMCSA notice states the parties' right to review "the broker's record of the transaction", but it does not set out what the current record must contain. It mentions comparing what the shipper paid with what the carrier was paid only as an effect of the proposal. The current text of 49 CFR §371.3 was not read; Fix: "its record of each load can be reviewed by the parties (what the current record must contain, and so whether it shows the margin, was not read here)"; Basis: https://www.fmcsa.dot.gov/regulations/docket-no-fmcsa-2023-0257-rin-2126-ac63-transparency-property-broker-transactions
[minor] [figure] §5; Current: "56,715 had 11 to 100 and 5,062 more than 100;"; Problem: the power-unit table's 2023 total is 787,189, and it includes a row "No Power Units/Unreported" of 15,026. The unit's five bands add up to 772,163, so the list reads as complete when it is not. The 53% and 90% shares are right against 787,189; Fix: "56,715 had 11 to 100, 5,062 more than 100 and 15,026 none or unreported;"; Basis: FMCSA 2024 Pocket Guide, RRC-24-002, https://www.fmcsa.dot.gov/sites/fmcsa.dot.gov/files/2025-09/FMCSA%20Pocket%20Guide%202024-v6%20508%20.pdf
[minor] [accuracy] §3.2; Current: "and names no transport management system (same page) [practice]"; Problem: no software category on the page is a transport management system, but the page's examples under ERP software include a trucking transport-management product. The vendor rule bars naming the product; Fix: "and has no software category for transport management systems (same page) [practice]"; Basis: https://www.onetonline.org/link/summary/43-5032.00
[minor] [attribution] §7, T1; Current: "| T1 | Buying capacity (SCE7 §3) | Freight sourcing: bids, lanes, the routing guide | Gartner 2026, mandatory [analyst] |"; Problem: the 2026 report's mandatory feature is "bid management and optimization". A keyword search of the reprint found no "routing guide". Under F71 the routing guide is credited to Acocella et al. (2020); Fix: "| T1 | Buying capacity (SCE7 §3) | Freight sourcing: bids, lanes, the routing guide | Gartner 2026, mandatory, bid management [analyst]; lanes and the routing guide, Acocella et al. 2020 as SCE7 §3 reads it [practice] |"; Basis: reprint URL above; filed SCE7 §3
[minor] [label] Deliverable C, row 8; Current: "Warehouse line or transport line (SCE6 row 22)?"; Problem: the pointer does not say which table. In the filed SCE6, row 22 is deliverable B's W22 row; Fix: "Warehouse line or transport line (SCE6 deliverable B, row 22)?"; Basis: filed SCE6 deliverable B row 22
[minor] [style] §10; Current: "One vendor profile in the report describes automated agents inside a control tower; AI features are outside this course."; Problem: this singles out one listed vendor's profile, giving it space the other fifteen do not get; Fix: "Where the report's vendor profiles describe automated agents in control towers, those are AI features, which this course does not treat."; Basis: reprint, keyword "control tower"; course brief, Vendors
[minor] [accuracy] §1; Current: "the chapter was not read, so it carries nothing here (flag F73)."; Problem: the publisher's page the unit cites now lists a 10th edition, so the 9th is not the current edition. Chapter 3 is "Transportation Technology and Systems"; Fix: "the chapter was not read, so it carries nothing here; the publisher's page also lists a 10th edition (flag F73)."; Basis: https://cengage.com/c/new-edition/9781337406642
[minor] [accuracy] §4; Current: "[practice: the agency's account of the current rule and of a proposal]"; Problem: the proposal is undated in the unit. The NPRM was published in the Federal Register on 20 November 2024 (Vol. 89, No. 224), with comments due by 21 January 2025; Fix: "[practice: the agency's account of the current rule and of a proposal published in the Federal Register on 20 November 2024]"; Basis: https://govinfo.gov/content/pkg/FR-2024-11-20/pdf/2024-27115.pdf
[minor] [attribution] Sources, FMCSA docket; Current: "Notice of proposed rulemaking, undated page."; Problem: this entry has the same missing date. Adding the Federal Register record also needs a source-log line; Fix: "Notice of proposed rulemaking, undated page; published in the Federal Register, Vol. 89, No. 224, 20 November 2024, FR Doc. 2024-27115, https://govinfo.gov/content/pkg/FR-2024-11-20/pdf/2024-27115.pdf"; Basis: same
[minor] [style] Deliverable E, Control tower; Current: "; a selling term with no agreed reach |"; Problem: the closing material adds a judgement with no source; Staudt et al. do not call the term a selling term; Fix: "; in this unit's reading (section 10), a term with no agreed reach |"; Basis: https://scielo.br/j/prod/a/99Lvbdfx9npmc998DYb57yc/?lang=en; sourcing standard Part 1
[minor] [attribution] §3.3; Current: "In X12, a standards body accredited by the American National Standards Institute for electronic data interchange,"; Problem: no source in the unit carries the ANSI accreditation. The X12 pages cited give only each set's purpose; Fix: "In X12, the standards body that publishes these electronic data interchange messages,"; Basis: https://x12.org/node/4214 ; https://x12.org/node/4210

## Confirmed

Gartner 2026 Magic Quadrant (reprint at the URL above, also confirmed by Shipsy's landing page https://www.shipsy.ai/gartner-magic-quadrant-2026):
- Report: dated 30 March 2026, ID G00832918, analysts Johns, Sanchez Duran and Jain.
- Definition: as the unit quotes it.
- Mandatory features: all, as the unit gives them.
- Common features: all, as the unit gives them, including the carrier-network wording "booking requests and confirmations".
- Inclusion rules:
  - one legal entity counts as one customer; customers of resellers and service providers are not counted;
  - at least 50 live customers, $10 million in TMS revenue and 20% three-year growth;
  - at least seven industries, with 3PLs given as an example;
  - at least 10 live customers outside the home region;
  - TL, LTL, parcel and ocean supported, generally available by 31 October 2025.
- Market Overview: "evaluates vendors based on the evolving needs of shippers"; no vendors added; Aptean dropped.
- Keyword checks:
  - absent: tender, "rating" (only "rated" in the criteria), routing guide, "end-to-end visibility";
  - "payment" appears only in two vendor profiles;
  - present: "bid and rate management and optimization", "control-tower-like capabilities".
- Vendor count: not stated in the report.
- Vendor list: the 16 headings match exactly.

Gartner definition pages:
- Gartner glossary TMS entry: rating and shopping, route and carrier, bills and payments; undated.
- RTTVP market: definition, mandatory features, March 2025, 46 products.
- FAP market: definition, no features list and no date, 42 products.
- VRS market: six mandatory features, July 2026, 79 products.

X12 messages:
- 204: tender wording and LTL exclusions.
- 210: "used both as a motor carrier invoice to request payment".
- 214: status wording.

O*NET pages, all marked "Updated 2026", with titles and tasks as quoted:
- 43-5011.00: Load Planner, Freight Broker; core tasks.
- 13-1081.02: Transportation Analyst; tasks, core and supplemental as stated.
- 43-5032.00: Truck Dispatcher; tasks; software categories.
- 43-5011.01: the three core tasks.
- 43-3021.00: Pre Audit Clerk; "shipment charges"; no freight or carrier task.

Other sources:
- 2025 3PL Study:
  - shippers' must-haves from 3PLs: 68% control tower visibility, 54% planning, 53% scheduling;
  - 55% of 3PLs offer control tower visibility; 87% of shippers satisfied with 3PLs' IT;
  - respondents: 44% shipper users, 9% non-users, 27% 3PL or 4PL; no total stated;
  - survey closed July 2024; sponsors NTT DATA and Penske.
- Evangelista et al. 2013: Crossref record matches (IMDS 113(7) 967–989). Manuscript: 1,992 firms, 153 usable responses, focus groups, 7 cases; low ICT spending; 38% offer track and trace; the stated reasons; skills constraint.
- Staudt et al. 2026: record matches (Production 36, e20250126). 32 articles; four interviewees at three companies in Brazil; the three sectors; the definition; two of three companies lack visibility layers; end-to-end management not found; "full integration remains a distant goal".
- FMCSA Pocket Guide: 787,189 carriers, the five bands, 735,895 interstate freight, snapshot 29 December 2023, July 2025. Shares recomputed: 53.2% and 90.2%.
- FMCSA docket page: an NPRM; the current right of review; electronic records, itemised charges, 48 hours, who may request.
- Rodrigue, 6th edition, 2024, ch. 7.4: 3PL asset-based; 4PL non-asset.
- Cengage page: ch. 3 covers TMS.
- APQC: measure name only.
- MIT CTL FreightLab: shippers, carriers and brokers.
- IDC: no IDC page found by search, only vendor releases.

Pointers and case:
- Filed-unit pointers to SCE1, SCE5, SCE6 and SCE7 hold (sections, card 4, form fields, W22, SCE7 deliverable rows A10 and B1 to B12). The exception is "SCE6 row 22" (minor finding 6).
- Every case fact matches case-facts.md and is labelled fictional on first use.

## The seven passes

1. References exist and match: PASS. All 23 exist, and the records match.
2. Claims against sources: PASS with findings 2 and 12. The Peer Insights TMS claims are unverifiable.
3. Grades: PASS. FMCSA's registration statistics are graded independent, matching SCE7's Eurostat grading but outside SCE1's listed kinds (flag F18).
4. Vendors: PASS with finding 7. The list is dated, complete and alike; nothing is assessed or mapped.
5. The case: PASS. The facts match, the labels are present and nothing is used as evidence. The notes listing could not be checked.
6. Scope and tone: PASS. AI gets one sentence; no interview framing, no method, nothing about the owner; no em dashes; British spelling; no "not X but Y" constructions.
7. Deliverable and figures: PASS with finding 1.
   - A, B, C, D and E are in full; the carrier representative's card is unnamed because the register has no carrier staff.
   - "On a site visit" and "Self-check" (eight questions) are present and agree with the body.

Part 8: every line holds except as the findings note; private_terms.py was not available to run. Read as the preamble's reader, the unit is followable on a phone and its claims are checkable from their links.

## Figures

1. §2 matrix "Which definition names which transport step": PASS. All cells trace to §§1 and 2, the caption names its sources, and the kind fits. The MQ Rate cell is empty, which is consistent with §1's reading.
2. §5 swimlanes: PASS. The labels trace to §§1, 3.3 and 5, and the caption is complete.
3. §6 Halvern matrix: PASS. It matches SCE7 §5 and §6's assumption, and the caption is complete.

## Flags given

- F6: partly. The TMS holdings are sourced from the 2026 reprint, and the glossary places payment in the TMS. How a carrier is paid in the TMS is still not sourced, and SCE1's cells are left to the correction route.
- F54: partly. The unit uses "case" as SCE6 does, but no owner decision is in the packet and SCE1's key has no "case" line.
- F62: dealt with (T1 to T24).
- F64: partly. X12's 204 wording and the reprint keyword reading were added, but no source places the tender's record in the TMS, so it stays working.
- F67: dealt with. No air limit is stated.
- F71: dealt with in the main. T1 still files the routing guide under Gartner (finding 5).
- F73: not dealt with. No textbook chapter was read, and the 10th edition exists.
- F75: partly. The live ctl.mit.edu page is cited; SCE1's redirect is noted only in the source log.
- F77: partly. APQC's measure was found by name only; WERC was not tried.
- F84: dealt with by this review.

## Flags

- F18: decide the grade of official statistics. Affects SCE7, SCE8 and every later unit citing Eurostat, FMCSA or national statistics.
- F73: carry forward. Affects SCE7 §6, SCE10, SCE13.
- F77: carry forward. Affects SCE7 §11, SCE8 cards, SCE13.
- F64: carry forward. Affects SCE1's matrix, SCE7 §5, SCE10.
- F54: decide before SCE9 and SCE17.
- New: what the current 49 CFR §371.3 record contains, and whether the 2024 NPRM became final, have not been read. Affects DD-SCE1 and any unit on brokers.

## Could not verify

- §1: Peer Insights TMS "same opening sentence and the same mandatory list". The page failed to fetch. SCE7's quotation of it lists no stand-alone or own-technology items.
- §9: "listed 92 products ... showed no total count of reviews". Same failed page.
- §9: the product descriptions' claims of tendering, audit and payment. Same failed page.
- §1: Gartner's abstract page also failed in this review, which is consistent with the unit.
- §2: the rest of the VRS definition, "under multiple constraints ... minimising fleet costs and mileage".
- §2: GTM "which Gartner lists beside ... (SCE1 §4)". Checked against SCE1 only.
- §3.2: the dispatcher description "using radio, phone or computer". Only a paraphrase was returned.
- §3.3: the ANSI accreditation of X12 (finding 12).
- §5: the 990 and IFTSTA. Checked against SCE7 only.
- §3.3 and card 3: the 81.9% and 68.5% acceptance figures. Checked against SCE7 only.
- §4: 49 U.S.C. §13102(2). Checked against SCE7 only.
- §4: whether the FMCSA proposal became final. Only press items were found.
- Sources: the 3PL study's subtitle "Navigating Change ...".
- Sources: Rodrigue's §7.4 overview page. Not opened.
- §4: Evangelista's published version against the manuscript.
- Notes: "listed in the notes". There are no notes in the packet or in unit.md.
- Part 8: private_terms.py was not run.

Facts used from memory: none.
