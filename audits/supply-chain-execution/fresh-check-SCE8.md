---
audit: fresh check
unit: SCE8 · The transport system as a product
course: supply-chain-execution · Supply Chain Execution for Product Teams
model: claude-opus-5-5
date: 2026-11-27
chat: https://claude.ai/code/session_01KMmgR1VZACTLVqHg81yMhf
verdict: fix · 1 errors, 4 should-fix, 11 minor
---

The checker's final report, verbatim, from its hand-back. Saved before any finding was applied.

claude-opus-5-5

Verdict: SCE8 · fix · 1 error, 4 should-fix, 11 minor

(The harness refused the write to out/report.md, so the full report is below. out/report.md still holds only the interim notes I wrote earlier in the run, before the refusal. 30 claims confirmed, 7 could not be verified. 19 references opened, 4 not opened (Rodrigue's ISBN record, Bartholdi & Hackman, the FreightLab procurement page, the vendors' landing pages). No reference fails to exist.)

## Findings
[error] [accuracy] §5 Portals; Current: "**Direct integration to carrier networks**, connecting a large number of external carriers, is a common feature of the 2026 evaluation (section 1) [analyst]; the report's wording does not say by which technology."; Problem: the report's common-feature bullet does say: "a large number of external carriers connected via API or electronic data interchange [EDI]", exchanging "rates, booking requests and confirmations and tracking events", in the core product or through partnerships with external carrier networks; Fix: "**Direct integration to carrier networks**, a large number of external carriers \"connected via API or electronic data interchange [EDI]\" and exchanging data such as rates, booking requests and confirmations and tracking events, either in the core product or through partnerships with external carrier networks, is a common feature of the 2026 evaluation (section 1) [analyst]."; Basis: Gartner, Magic Quadrant for Transportation Management Systems, 30 Mar 2026, G00832918, reprint, Common Features, read 27 Nov 2026, https://lp.shipsy.ai/hubfs/Shipsy%20Content%20Library/Gartner/Gartner%20MQ%20TMS%202026.pdf
[should-fix] [accuracy] §1 Rating; Current: "- **Rating.** The glossary names freight rating; the 2026 report names neither rating nor tendering in its definition, overview or criteria (same keyword search) [analyst]. Tendering is folded, at most, into \"communications with carriers\"."; Problem: the word "rating" is indeed absent, but the Market Definition names "bid and rate management and optimization" under sourcing, and the carrier-network common feature exchanges "booking requests and confirmations". A word search has been stretched into a claim about content; Fix: "- **Rating.** The glossary names freight rating; the 2026 report's Market Definition names \"bid and rate management and optimization\" under sourcing, and neither the word \"rating\" nor \"tender\" appears in its definition, overview or criteria (same keyword search) [analyst]. Tendering is folded, at most, into \"communications with carriers\" and into the common feature of direct carrier integration, which exchanges \"booking requests and confirmations\" (section 5) [analyst]."; Basis: Gartner MQ TMS 2026 reprint, Market Definition/Description and Common Features, https://lp.shipsy.ai/hubfs/Shipsy%20Content%20Library/Gartner/Gartner%20MQ%20TMS%202026.pdf
[should-fix] [accuracy] §10 One study looked inside; Current: "They define a control tower as a technology-enabled platform that integrates real-time data with analytics and organisational knowledge; they found"; Problem: the authors' definition goes on "to provide end-to-end visibility, automate decision-making, ...". Cutting it off hides that the study builds the C11 claim into its own definition as an aim, which its findings then show is not met; Fix: "They define a control tower as a technology-enabled platform that integrates real-time data, advanced analytics and organisational knowledge \"to provide end-to-end visibility\", among other aims; they found"; Basis: Staudt et al. 2026, Production 36, e20250126, full text, https://scielo.br/j/prod/a/99Lvbdfx9npmc998DYb57yc/?lang=en (https://doi.org/10.14488/1980-5411.20250126)
[should-fix] [accuracy] §5 EDI; Current: "In GS1's EANCOM subset of UN/EDIFACT messages, IFTSTA carries transport status (SCE7 §6, step 7) [independent]."; Problem: the pointer states as fact something SCE7 §6 step 7 marks unverified ("that it is a UN/EDIFACT message is unverified here"); Fix: "In GS1's EANCOM subset, IFTSTA carries transport status (SCE7 §6, step 7, which leaves its UN/EDIFACT status unverified) [independent]."; Basis: filed SCE7 §6 step 7 and §7 (IFTSTA row)
[should-fix] [deliverable] D. Templates, D2; Current: "**D2. Shipper versus provider.** One row per need; keep rows 1 to 15 and add rows the operation has."; Problem: rows 4, 7, 9, 11 and 15, and most cells of the other rows, are bare "______" with no rule for what goes in them. D3 has such a rule; the brief requires each blank to say what goes in it; Fix: "**D2. Shipper versus provider.** One row per need; keep rows 1 to 15 and add rows the operation has. A bare blank takes, for that row's need: in Shipper and Provider, what that company does or holds, with \"no public figure\" for a private company's number; in the fourth column, the difference that matters to the product; in Basis, the source with its grade, or \"register\" or \"observed\"."; Basis: course brief ("each blank saying what goes in it"); sourcing-standard Part 8
[minor] [accuracy] Self-check 1; Current: "The glossary adds freight rating and the management of freight bills and payments; neither text names tendering (section 1)."; Problem: once the Rating fix is made, this answer must agree with it; Fix: "The glossary adds freight rating (the report names only \"bid and rate management\" under sourcing) and the management of freight bills and payments; neither text uses the word tender (section 1)."; Basis: Gartner MQ TMS 2026 reprint, https://lp.shipsy.ai/hubfs/Shipsy%20Content%20Library/Gartner/Gartner%20MQ%20TMS%202026.pdf
[minor] [accuracy] §1 Payment; Current: "found no \"payment\" outside one vendor's profile"; Problem: in the reprint "payment" appears in two vendor profiles ("freight audit and payment"; "Freight Payment Agent"), not one; Fix: "found \"payment\" only in two vendors' profiles"; Basis: Gartner MQ TMS 2026 reprint, Vendor Strengths and Cautions, URL as above
[minor] [accuracy] §1 common features; Current: "analytics beyond the embedded kind"; Problem: the common analytics bullet is embedded too ("utilizing embedded analysis and reporting capabilities to measure key performance indicators, such as on-time performance; emissions calculations; and costs by mode, customer, product line and location"); Fix: "analytics measuring key performance indicators such as on-time performance, emissions and costs by mode, customer, product line and location"; Basis: Gartner MQ TMS 2026 reprint, Common Features, URL as above
[minor] [accuracy] §8; Current: "was dropped as it did not meet the inclusion criteria [analyst]"; Problem: the report gives the reason: "did not meet the TMS technology customer criteria"; Fix: "was dropped as it did not meet the TMS technology customer criteria [analyst]"; Basis: Gartner MQ TMS 2026 reprint, Vendors Added and Dropped, URL as above
[minor] [accuracy] §4 What small providers can spend; Current: "only 38% of the sample offered track and trace, partly because customers did not demand it"; Problem: the reason comes from the case companies that did not offer it ("customers did not demand it and their existing ICT systems would not support it"), not from the survey; Fix: "only 38% of the sample offered track and trace, and case companies that did not offer it said mainly that customers did not demand it and their systems would not support it"; Basis: Evangelista, McKinnon & Sweeney 2013, author's manuscript, https://publications.aston.ac.uk/id/eprint/22288/1/Technology_adoption_in_small_and_medium_sized_logistics_providers.pdf (https://doi.org/10.1108/IMDS-10-2012-0374)
[minor] [accuracy] Deliverable E; Current: "| Control tower | A platform integrating real-time data with analytics and organisational knowledge (one study's definition); a selling term with no agreed reach |"; Problem: the same cut-off definition as in §10; Fix: "| Control tower | A platform integrating real-time data, analytics and organisational knowledge to provide end-to-end visibility (one study's definition, which states the aim; the same study found it unmet in its cases); a selling term with no agreed reach |"; Basis: Staudt et al. 2026, https://scielo.br/j/prod/a/99Lvbdfx9npmc998DYb57yc/?lang=en
[minor] [label] §3.1 In the case; Current: "Sofia (fictional) builds Ostrel Foods' next day's routes"; Problem: the first body use of Ostrel Foods has no label (the label sits on Sofia); Fix: "Sofia builds Ostrel Foods' (fictional) next day's routes"; Basis: course brief; case-facts.md rules
[minor] [label] front matter intro; Current: "five transport role cards on Ostrel's and Tandric's staff"; Problem: both case operations appear without the label, while Halvern has it; Fix: "five transport role cards on the staff of Ostrel and Tandric (both fictional)"; Basis: case-facts.md rules
[minor] [accuracy] Deliverable A card 2 field 3; Current: "calls from 40 drivers and from customers [register]"; Problem: the register gives 40 vehicles, not 40 drivers; Fix: "calls from the drivers of 40 vehicles and from customers [register]"; Basis: case-facts.md, Ostrel Foods, Delivery
[minor] [style] §2 Visibility; Current: "independent of the ETA other parties give"; Problem: ETA is never defined; Fix: "independent of the estimated time of arrival (ETA) other parties give"; Basis: course brief (Frame); https://www.gartner.com/reviews/market/real-time-transportation-visibility-platforms
[minor] [deliverable] D3; Current: "by the steps of SCE6 deliverable C"; Problem: SCE6 deliverable C is the template; the steps are SCE6 §9's method, as SCE8 §9 itself says; Fix: "by the steps of SCE6 §9"; Basis: filed SCE6 §9 and deliverable C
(A script confirmed that every Current string occurs exactly once in unit.md.)

## Confirmed
- Gartner MQ TMS, 30 Mar 2026, G00832918, analysts B. Johns, O. Sanchez Duran, M. Jain: definition; all mandatory and common features; the customer definition and the reseller/service-provider exclusion; thresholds of 50 customers, $10 million, 20%, seven industries (3PLs given as an example), 10 customers outside the home region, TL/LTL/parcel/ocean, GA by 31 Oct 2025; "evolving needs of shippers"; "control-tower-like capabilities"; "end-to-end visibility" absent; no count of vendors considered; the 16 vendors in order; none added; Aptean dropped (reprint URL above).
- Peer Insights TMS page: same definition and list, April 2026, 92 products, no total review count, product descriptions claiming tendering, freight audit and payment (https://www.gartner.com/reviews/market/transportation-management-systems).
- Gartner glossary TMS entry, all four quoted parts, undated (https://gcom.pdo.aws.gartner.com/en/information-technology/glossary/tms-transportation-management-system).
- Visibility platforms: definition, five mandatory features, March 2025, 46 products. Freight audit and payment: definition, 42 products, no date. Vehicle routing: definition including fleet costs and mileage, six mandatory features, July 2026, 79 products (gartner.com/reviews market pages; external.pi.gpi.aws.gartner.com for freight audit).
- X12 204, 210 and 214 purpose statements and quotations (https://x12.org/node/4207, /4210, /4214).
- O*NET 43-5032.00, 13-1081.02, 43-5011.00, 43-5011.01, 43-3021.00: titles, tasks, which tasks are core and which supplemental, software categories, updated 2026 (onetonline.org pages as cited).
- 2025 3PL Study: 68%, 54%, 53%, 55%, 87%; respondent shares 44%, 9%, 27%; survey closed July 2024; no total respondent count; sponsors NTT DATA and Penske; graded vendor-reported, which follows the SCE1 key (NTT DATA pdf).
- Evangelista et al. 2013: Crossref record (113(7), 967-989); 1,992 firms, 153 responses, focus groups, seven cases, Italy; findings as quoted.
- Staudt et al. 2026: bibliographic record, design (32 papers; four employees; three Brazilian companies; sectors) and findings.
- FMCSA Pocket Guide RRC-24-002, July 2025: all counts, snapshot 29 Dec 2023; the 53.2% and 90.2% shares recomputed and correct.
- FMCSA-2023-0257 notice: right of review; electronic records, itemised charges, 48 hours, the parties.
- Rodrigue, 6th ed.: 3PL and 4PL wording. Cengage page: 9th ed. authors, ISBN, ch. 3 on TMS, 10th ed. ISBN. APQC: measure name, no definition. MIT CTL FreightLab: shippers, carriers and brokers.
- Pointers to filed units, all right except the two in Findings: SCE1 §§4, 7, 8, 10, C10, C11; SCE5 deliverable A and card 4; SCE6 §2, §7, §9, W2, W22, W26, deliverable A ("case" grade); SCE7 §§1 to 11, deliverable A row 10, deliverable B rows 2, 4, 7 to 12, register notes.
- Case facts against case-facts.md for Ostrel, Tandric, Corvane and Halvern: all right apart from the "40 drivers" minor. Deliverable C counts (7 + 1 + 16 = 24) are right.

## The seven passes
1. References exist and match: PASS. All 23 Sources entries exist and match their records (Rodrigue's ISBN not checked).
2. Claims against sources: one FAIL (the §5 error), two stretches (§1 rating, §10 definition) and four minor misreadings; every other claim PASS.
3. Grades: PASS. The FMCSA registration counts graded independent are a borderline case for F18 (see Flags).
4. Vendors: PASS. The list is dated and every vendor is given alike, with no placements; no vendor is named elsewhere in the text.
5. The case: PASS, apart from two label minors and the "40 drivers" minor. No case fact is used as evidence.
6. Scope and tone: PASS. AI is raised in one sentence; there are no em dashes and no "not X but Y" constructions; one term (ETA) is undefined.
7. Deliverable and figures: PASS with fixes. Parts A to E are all built. "On a site visit" and "Self-check" agree with the body (Self-check 1 needs the minor fix). D2's blanks need a rule; D3's pointer is wrong.
- Part 8, line by line: met except as listed in Findings. kit/private_terms.py is outside the packet and was not run; I saw no private term on reading.
- Read as the preamble's reader: the unit builds in order and is honest about its limits; the long tables are heavy on a phone but usable.

## Figures
- Fig 1 (matrix, §2): PASS. Every cell traces to §§1 and 2, and the caption is complete.
- Fig 2 (swimlanes, §5): PASS.
- Fig 3 (matrix, §6): PASS. The caption's "Steps 5, 6, 8 and 9 have no module" matches §6.

## Writer's contradictions
1. SCE1 FreightLab citation: right in substance. The replacement agrees with SCE7 §3 (Acocella et al., practice) and §2 (Sheffi). I could not check the 302 redirect, because no search returned that address. Three gaps:
   - SCE1 §2's flow-figure caption also cites "MIT FreightLab's procurement page" and must change with the text. Proposed caption tail: "... and Acocella, Caplice and Sheffi (2020) as read in SCE7 §3."
   - The new Shipper source cell "SCE7 §1 [course term]" is circular, because SCE7 §1 cites the SCE1 glossary. Use "Course term (also SCE7 §1)".
   - SCE1's source log should mark the FreightLab entry superseded rather than delete it.
2. SCE1's 3PL row: right. Rodrigue says a 3PL "is an asset-based company" and that 4PLs "are non-asset based, meaning that they mainly provide organizational expertise". The proposed cell is accurate. The notes' line that Tandric's desk "is a 4PL in freight" stretches Rodrigue; the unit's own wording is the safe form. Bartholdi & Hackman §1.2 was not opened.

## Flags
- F64 and F6 (SCE1 §3, SCE7 §5, SCE10): the 2026 MQ names "bid and rate management" in its definition and "booking requests and confirmations" in a common feature. "Payment" appears in two vendor profiles, not one.
- F18 (SCE7, SCE8, later transport units): FMCSA registration counts are graded independent, but a registration snapshot is not one of the SCE1 key's named kinds, and SCE7's preamble covers only surveys whose design is stated.
- Staleness (SCE8, DD-SCE1): trade press, which is not a course source (Transport Topics, 2 Sep 2026), reports that the 2024 broker proposal was never finalised and that a supplemental proposal went to OIRA on 27 Aug 2026. DD-SCE1 should open the Federal Register before relying on the proposal.
- SCE13 and SCE5: Sofia has two cards. I agree with writer's Needs 10.
- Bibliography: Cengage's page slug for the 10th edition gives Novack, Gibson and Suzuki.

## Could not verify
- The FreightLab 302 redirect: the address was not returned by any search, so it was not fetched.
- Bartholdi & Hackman §1.2.
- Rodrigue's ISBN 9781032380407 (the page shows only DOI 10.4324/9781003343196).
- The tail of the MQ planning quotation after "including order and" (the same wording appears on Peer Insights and in SCE7 §5).
- §9 "Two vendors' landing pages ... held no report text, only the offer of a copy on request" (not opened; carries no claim).
- §3.3 "X12, the US-based standards body" (no source).
- private_terms.py (not run; outside the packet).
