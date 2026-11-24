---
audit: corrections check
course: supply-chain-execution · Supply Chain Execution for Product Teams
row: W-SCE4
flags: F35, F36 (quality reviews of SCE1 and SCE2)
model: Opus 5.5
date: 2026-11-24
chat: https://claude.ai/code/session_01KMmgQyoX6Hnru9aiNiXdBA
result: 45 changes: 37 passed, 2 failed, 6 held
---

The corrections checker's report, verbatim, as it saved it. Saved before anything was applied.

## Change 1
File: SCE1-the-map-the-words-and-the-evidence.md
Current:
```
a 30-term working glossary
```
Replacement:
```
a 39-row working glossary
```
Result: PASS. R1.10 merged with the count effect of D1.8: deliverable B has 31 rows now (counted); Change 22 adds 8, so 39.
Syllabus: no conflict

## Change 2
File: SCE1-the-map-the-words-and-the-evidence.md
Current:
```
its index listed three *Supply Chain Planning Solutions* evaluations
```
Replacement:
```
its index listed *Supply Chain Planning Solutions* evaluations (discrete industries and process industries; a third, for retail and distribution-intensive industries, was not confirmed on a re-read)
```
Result: HOLD. R1.5 rests on a Gartner index re-read that the reviewer says an extraction may have missed; the §6 row "(three industry variants)" has the same matter and no exact fix. A fresh read of the index is needed, which is more than a wording correction.
Syllabus: no conflict (touches held fresh-check f4's matter; see Held)

## Change 3
File: SCE1-the-map-the-words-and-the-evidence.md
Current:
```
the deliverable gives the inbound pair a row of its own, so its table has twelve rows.
```
Replacement:
```
the deliverable gives the inbound pair a row of its own (row 5), so its table has twelve rows and, from Pick on, its numbers run one higher than this list's; later units and the case register cite the deliverable's numbers.
```
Result: PASS. D1.3 verified: §2 numbers Pick 5 to Return 11; deliverables A and D number Pick 6 to Return 12; the register's SCE1 rows cite step 9 for carry and track (Jonas) and step 11 for settle (Helene), which is the deliverable's numbering. SCE3's "SCE1 §2, step 4" (Release) is the same in both.
Syllabus: no conflict

## Change 4
File: SCE1-the-map-the-words-and-the-evidence.md
Current:
```
6. **Pack and ship.** The order is checked, packed and loaded;
```
Replacement:
```
6. **Pack and ship.** The order is checked, packed and loaded (SCE3 takes steps 4 to 6);
```
Result: PASS. D1.11, second part. SCE3 covers release, picking and packing up to departure. The evidence: its register rows (picking released by route after cut-off; roll cages staged and loaded by route), flags F26 (picking methods) and F34 (cut-off and departure, SCE3 §8), and SCE2 §2 ("later units treat their picking differently (SCE3)").
Syllabus: no conflict

## Change 5
File: SCE1-the-map-the-words-and-the-evidence.md
Current:
```
Two inbound steps feed every promise:
```
Replacement:
```
Two inbound steps, which SCE2 takes, feed every promise:
```
Result: PASS. D1.11, first part. SCE2 is "Inbound and storage", and its brief covers receiving through put-away.
Syllabus: no conflict

## Change 6
File: SCE1-the-map-the-words-and-the-evidence.md
Current:
```
Halvern Warehouse (fictional) lists Labour, Yard, Slotting and Automation Connect modules
```
Replacement:
```
Halvern Warehouse (fictional) lists Labour, Voice, Yard, Slotting, Automation Connect and Client Billing modules
```
Result: PASS. R1.11 verified against case-facts.md, Halvern Systems, Warehouse line (six modules).
Syllabus: no conflict

## Change 7
File: SCE1-the-map-the-words-and-the-evidence.md
Current:
```
and each client brings its own rules and reports, as Tandric's (fictional) do (case register).
```
Replacement:
```
and at Tandric (fictional) each client brings its own rules and reports (case register); this unit opened no source on whether that holds for logistics providers generally.
```
Result: PASS. D1.6 verified: the register's Tandric "Known trouble" row is the only support, and the brief says the case is never evidence for a claim about the world.
Syllabus: no conflict

## Change 8
File: SCE1-the-map-the-words-and-the-evidence.md
Current:
```
| Distributed Order Management | none shown | 23 Nov 2026 |
```
Replacement:
```
| Distributed Order Management | no row confirmed on the index (abstract dated 12 Nov 2026) | not confirmed |
```
Result: HOLD. R1.1 is fresh-check f4's matter, still held. It turns on what Gartner's index shows, so it needs a browser re-read of https://www.gartner.com/magic-quadrant. The writer and the applier saw the row; the checker, the main chat and this reviewer did not.
Syllabus: no conflict

## Change 9
File: SCE1-the-map-the-words-and-the-evidence.md
Current:
```
| Supply Chain Management Suites | 11 Aug 2026 | 11 Aug 2027 |
```
Replacement:
```
| Supply Chain Management Suites | not confirmed on the index | not confirmed |
```
Result: HOLD. R1.3: the reviewer's own fix is conditional ("apply only if a browser read also lacks the row"), and no browser read has been made.
Syllabus: no conflict

## Change 10
File: SCE1-the-map-the-words-and-the-evidence.md
Current:
```
| Global Trade Compliance Solutions | none shown | 30 Nov 2026 |
```
Replacement:
```
| Global Trade Compliance Solutions | not confirmed on the index | not confirmed |
```
Result: HOLD. R1.4: conditional on a browser read of the index, as in Change 9.
Syllabus: no conflict

## Change 11
File: SCE1-the-map-the-words-and-the-evidence.md
Current:
```
The index and the report disagree on one date: Gartner's own abstract page for the Distributed Order Management Magic Quadrant is dated 12 November 2026 ([Gartner, abstract](https://www.gartner.com/en/documents/8617033)) [analyst], while the index read nine days later still showed no last-updated date for it.
```
Replacement:
```
Gartner's own abstract page for the Distributed Order Management Magic Quadrant is dated 12 November 2026 ([Gartner, abstract](https://www.gartner.com/en/documents/8617033)) [analyst]; no row for it could be confirmed on the index.
```
Result: HOLD. R1.2 depends on Change 8 (f4). The same index re-read decides both, so they go in together or not at all.
Syllabus: no conflict

## Change 12
File: SCE1-the-map-the-words-and-the-evidence.md
Current:
```
so this unit does not describe Gartner's evaluation criteria in detail.
```
Replacement:
```
so the quadrant itself is covered only in part: this unit does not describe Gartner's evaluation criteria beyond the two measures and four quadrants named below, or its reprint terms, and uses Forrester's Wave, a different evaluation whose method could be read in full, for the steps.
```
Result: PASS. D1.2, with the fix corrected. The reviewer's text said the unit "does not describe Gartner's evaluation criteria", but §8 does give the FAQ's two measures and four quadrants (the front matter says "not described beyond the FAQ's two axes and four quadrants"). The reviewer's "shows the steps below" also repeated the next paragraph's lead-in.
Syllabus: no conflict (F3 and F4 stay open for the Gartner method and reprint pages)

## Change 13
File: SCE1-the-map-the-words-and-the-evidence.md
Current:
```
1. The analyst sets inclusion criteria, meant to be differentiating rather than exhaustive.
2. The analyst drafts evaluation criteria at kickoff, puts them in the vendor questionnaire, and weights them at scoring.
```
Replacement:
```
1. The analyst sets the inclusion criteria that decide which vendors are evaluated.
2. The analyst drafts evaluation criteria at kickoff, puts them in the vendor questionnaire, and weights them at scoring; Forrester intends these criteria to be differentiating, rather than exhaustive.
```
Result: PASS. R1.8, with the fix corrected. The method page (opened 24 Nov 2026) says "the analyst creates the inclusion criteria that determine which vendors to include in the evaluation". It says "We intend the criteria to be differentiating, rather than exhaustive" of the evaluation criteria. The reviewer's fix kept the phrase in step 1, where "its criteria" still reads as the inclusion criteria, so it moves to step 2.
Syllabus: no conflict

## Change 14
File: SCE1-the-map-the-words-and-the-evidence.md
Current:
```
and published from the fourth quarter of 2024
```
Replacement:
```
and publishing in the fourth quarter of 2024
```
Result: PASS. R1.9 verified: the page says "Wave evaluations that kick off on or after July 1, 2024, and publish in Q4 2024" and "Customer feedback will replace market presence on the graphic".
Syllabus: no conflict

## Change 15
File: SCE1-the-map-the-words-and-the-evidence.md
Current:
```
"Not searched here" means this unit did not look and makes no finding.
```
Replacement:
```
Where no independent source was found, the row says so and names the unit that goes further.
```
Result: HOLD. D1.1 (error): setting C3 to C9 and C11 to C14 against evidence needs searches. It is flag F2's matter, and corrections.md says not to change §11.
Syllabus: F2 (carried): the brief replacement for §11 awaits a syllabus review. If it is vetoed, SCE1 searches C3 to C14 and is refiled (fresh-check f20).

## Change 16
File: SCE1-the-map-the-words-and-the-evidence.md
Current:
```
Both trace to textbooks; no measurement study was opened.
```
Replacement:
```
Both trace to textbooks; no measurement study was opened, and no independent source found.
```
Result: PASS. R1.6 verified: the brief's Common claims rule requires "no independent source found" where none was, and the C1 cell names only practice-graded sources. Only the C1 cell changes; the F2 matter is left alone.
Syllabus: no conflict (F31's proposed append to the C1 cell still applies after it)

## Change 17
File: SCE1-the-map-the-words-and-the-evidence.md
Current:
```
"As much as" is an upper bound, which the circulating version drops.
```
Replacement:
```
"As much as" is an upper bound, which the circulating version drops. No independent source found.
```
Result: PASS. R1.7 verified as in Change 16: both of the C2 cell's sources are graded practice.
Syllabus: no conflict (F31's append to the C2 cell still applies)

## Change 18
File: SCE1-the-map-the-words-and-the-evidence.md
Current:
```
A logistics provider runs other companies' goods and bills per activity, which changes what it needs from the record (section 5).
```
Replacement:
```
A logistics provider runs other companies' goods; Tandric (fictional) bills its clients per activity, which changes what it needs from the record (section 5).
```
Result: PASS. D1.7 verified: billing per activity comes from the register's Tandric "How it is paid" row, and §5 gives it as Tandric's.
Syllabus: no conflict

## Change 19
File: SCE1-the-map-the-words-and-the-evidence.md
Current:
```
tracking order status (section 2)
```
Replacement:
```
tracking order status (sections 2 and 3)
```
Result: PASS. R1.13 verified: status tracking is in the §3 table ("tracks status through the chain") and the §3 figure legend, not in §2.
Syllabus: no conflict

## Change 20
File: SCE1-the-map-the-words-and-the-evidence.md
Current:
```
5. **What document confirms an international road shipment under the CMR Convention, and how many original copies does it have?**
   A consignment note, in three original copies signed by sender and carrier (section 2, region note).
```
Replacement:
```
5. **Name the map's steps in order and say which system holds the record at each.**
   Take the order, promise and source (order system); release, receive and put away, pick, and pack and ship (warehouse system); plan and tender, and carry and track (transport system, a working placement); deliver (section 3 places it in no system); settle (ERP, a working placement); return (a typical warehouse module in Gartner's glossary) (sections 2 and 3; deliverable A).
```
Result: PASS. D1.4 and D1.5 merged, with the answer corrected: the reviewer's answer put receive and put away before release and gave deliver no placement. This answer follows deliverable A's rows 1 to 12, and every placement comes from the §3 table. The list stays at eight questions, and the CMR fact stays in §2's region note.
Syllabus: no conflict

## Change 21
File: SCE1-the-map-the-words-and-the-evidence.md
Current:
```
| Each carrier's own portal | Jonas
```
Replacement:
```
| Not in the register (carriers are booked through each carrier's own portal) | Jonas
```
Result: PASS. R1.12 verified: the register's Corvane Systems row says carriers are booked through each carrier's own portal. It says nothing about tracking there, and the fact is not in "Added by units".
Syllabus: no conflict

## Change 22
File: SCE1-the-map-the-words-and-the-evidence.md
Current:
```
| Evidence grade | One of independent, analyst, vendor-reported, practice (part C) | This unit |
```
Replacement:
```
| Evidence grade | One of independent, analyst, vendor-reported, practice (part C) | This unit |
| Lane (freight) | A recurring route from one origin to one destination that a shipper buys carriage for | Course term; SCE7 sources it |
| Radio-frequency identification (RFID) | Tags read by radio, used beside bar codes to identify goods | Named in Gartner WMS definition [analyst]; definition is the course's |
| Critical Capabilities | Gartner's companion report to a Magic Quadrant, meant to be read with it | Named as the companion report in Gartner 2024 note, abstract [analyst]; definition is the course's |
| Item master | The record of every item the company stocks or sells | Working definition; not sourced in this unit |
| General ledger | The company's main book of accounts | Working definition; not sourced in this unit |
| Replenishment | Resupplying a store, or a pick location, with stock | Course term; SCE2 sources the pick-location sense |
| Slotting | Assigning each item to a storage location | Course term; SCE2 adds the forward-area sense |
| Go-live | The day a new system starts running the operation | Course term |
```
Result: PASS. D1.8, with three rows corrected. "Lane" is qualified "(freight)" because SCE2 uses "lane" for storage and staging lanes. Critical Capabilities is marked the course's definition, because the 2024 abstract only names it as the companion report. Slotting drops "SCE4 sources it", which the packet cannot confirm (SCE4's brief is not in it), and points to SCE2's row instead. Every row is in plain words, marked the course's own where not sourced, in the glossary's three-column form. The count is in Change 1.
Syllabus: no conflict. SCE2 deliverable D already has a Slotting row ("Assigning SKUs to locations, including which go forward | Course term"). The two definitions agree, and the duplicate is merged when the course glossary is built.

## Change 23
File: SCE1-the-map-the-words-and-the-evidence.md
Current:
```
Grade: analyst, abstract only; the unit states nothing about the report beyond the abstract.
```
Replacement:
```
(B2B: sales to businesses; B2C: sales to consumers.) Grade: analyst, abstract only; the unit states nothing about the report beyond the abstract. Vendors license Gartner's reprints (the course's working assumption, section 8), so a copy on a vendor's site is one that vendor chose to post.
```
Result: PASS. R1.14 and D1.9 merged, as both touch this sentence. R1.14: B2B and B2C are first used in the body here, undefined. D1.9: the key's Test column and the brief's analyst grade both require the reprint note. The note is worded as §8 words it, the course's working assumption.
Syllabus: no conflict (F4 stays open: SCE17 checks Gartner's reprint terms)

## Change 24
File: SCE1-the-map-the-words-and-the-evidence.md
Current:
```
add a row where the operation has a step the map lacks, and say why.
```
Replacement:
```
add a row where the operation has a step the map lacks, and say why. In rows 2 to 12, the System, Owner, Known trouble and Grade blanks take what row 1 describes for each column.
```
Result: PASS. D1.10, second part: the brief requires each blank to say what goes in it, and rows 2 to 12 leave four columns bare.
Syllabus: no conflict

## Change 25
File: SCE1-the-map-the-words-and-the-evidence.md
Current:
```
| ______ (a failure you saw or a source reports) | ______ |
```
Replacement:
```
| ______ (a failure you saw or a source reports) | ______ (independent, analyst, vendor-reported or practice, by part C) |
```
Result: PASS. D1.10, first part: row 1's grade blank is bare.
Syllabus: no conflict

## Change 26
File: SCE1-the-map-the-words-and-the-evidence.md
Current:
```
fix · 1 errors, 2 should-fix, 24 minor; report
```
Replacement:
```
fix · 1 error, 2 should-fix, 24 minor; 25 applied, f4 held, f20 no change; report
```
Result: PASS. R1.15 verified against the front matter: there were 27 findings. The applier applied 24 and held f1, f4 and f20, then the main chat applied f1. That leaves 25 applied, f4 held and f20 with no text change (F2).
Syllabus: no conflict

## Change 27
File: SCE2-inbound-and-storage.md
Current:
```
A cross-dock is a warehouse that consolidates without storing.
```
Replacement:
```
A cross-dock, in this unit's summary, is a warehouse that consolidates without storing.
```
Result: PASS. R2.9 verified: the line is the unit's own summary. F15's corrections check found that Bartholdi & Hackman §1.1 does not say "without storing".
Syllabus: no conflict

## Change 28
File: SCE2-inbound-and-storage.md
Current:
```
This is this unit's reading of the register, and it is why later units treat their picking differently (SCE3).
```
Replacement:
```
That suppliers deliver both operations by the pallet is a fact this unit adds, listed for the case register; the rest is this unit's reading of the register, and it is why later units treat their picking differently (SCE3).
```
Result: PASS. D2.7 verified: the register gives Corvane's outbound flows and Ostrel's case picking, and says nothing about pallets arriving at either. The list of added facts is Change 43.
Syllabus: no conflict

## Change 29
File: SCE2-inbound-and-storage.md
Current:
```
as cited in section 3."}
```
Replacement:
```
as cited in section 3; the quality-hold note is this unit's working description (section 3.5)."}
```
Result: PASS. D2.11 and R2.8 merged, as both fix the same mismatch: the caption credits all notes to Bartholdi and Hackman and GS1, but "where inspection applies" rests on §3.5's working description. Only the caption fix is taken, so the figure's label still matches the text.
Syllabus: no conflict

## Change 30
File: SCE2-inbound-and-storage.md
Current:
```
**Common failure.** Goods left in staging are in the building but not in a location the record knows (this unit's inference from §4.2).
```
Replacement:
```
**Common failure.** Goods left in staging are in the building but not in a location the record knows (this unit's inference from §4.2).

**Measure.** Dock-to-stock cycle time starts when the delivery is received from the supplier (APQC, section 8) [practice].
```
Result: PASS. R2.3 (first part) and D2.4 merged. The operations pattern needs a measure for each step, and deliverable rows A3 and B3 give "Dock-to-stock time starts here (8)". The wording follows §8's APQC sentence ("the cycle begins when the business receives the delivery from the supplier").
Syllabus: no conflict

## Change 31
File: SCE2-inbound-and-storage.md
Current:
```
best-before, expiry and sell-by dates are optional, and where used must relate to the trade item on the label
```
Replacement:
```
where applicable, one of the guideline's date types (among them best-before, expiry and sell-by) should be given, and it always relates to the trade item identified on the label
```
Result: PASS. R2.1 verified at ref.gs1.org (24 Nov 2026). Rule [4-18]: "If applicable one of the following dates should be given, depending on the type of product". §4.6: "It is recommended to include date information whenever it is relevant". Rule [4-19], normative: "Dates always relate to the GTIN specified on the label". The reviewer's wording is kept, except that the date types are named as the unit already names them.
Syllabus: no conflict

## Change 32
File: SCE2-inbound-and-storage.md
Current:
```
mixed-batch pallets are therefore split or labelled by the site's own scheme (this unit's inference).
```
Replacement:
```
mixed-batch pallets are therefore split or labelled by the site's own scheme (this unit's inference).

**Measure.** No inbound benchmark for labels was found in the sources opened; the flow map uses WERC's correct-documents measure (section 8) as the nearest, because the labels must match the notice (this unit's inference).
```
Result: PASS. R2.3 (second part) and D2.5 merged into one line. Deliverable rows A6 and B6 give "Percent with correct documents (8)", which §8 does not tie to labels; the line says so and labels the mapping.
Syllabus: no conflict

## Change 33
File: SCE2-inbound-and-storage.md
Current:
```
**System.** Bartholdi and Hackman list flow-through processing among a WMS's high-end features (§4.3) [practice].
```
Replacement:
```
**People.** Whoever decides at the dock whether goods go to shipping or to storage; neither register names one.

**System.** Bartholdi and Hackman list flow-through processing among a WMS's high-end features (§4.3) [practice].
```
Result: PASS. R2.3 (third part) and D2.6 merged. The line goes before System, the order every other step uses (event, people, system, failure, measure). Deliverable rows A7 and B7 and template row 7 ("who decides at the dock") already assume it.
Syllabus: no conflict

## Change 34
File: SCE2-inbound-and-storage.md
Current:
```
**Common failure.** Goods arrive for which no outbound load is ready, and so are stored after all, or wait on the dock. Named, not measured.
```
Replacement:
```
**Common failure.** Goods arrive for which no outbound load is ready, and so are stored after all, or wait on the dock. Named, not measured.

**Measure.** No inbound benchmark for cross-docking was found in the sources opened.
```
Result: PASS. R2.3 and D2.6, the measure line: deliverable rows A7 and B7 say "No benchmark found" with no body section behind them.
Syllabus: no conflict

## Change 35
File: SCE2-inbound-and-storage.md
Current:
```
**Two cost shares you will hear.** Bartholdi and Hackman say receiving accounts for only about 10% of operating costs in a typical distribution centre, and put-away about 15%, crediting both to Frazelle's *World-Class Warehousing* (1996) and, for receiving, also his *World-Class Warehousing and Material Handling* (2002) (§3.1, §3.2; bibliography [21], [22]) [practice]. This unit did not open Frazelle, so the origin is not traced and both figures are graded practice under SCE1's key.
```
Replacement:
```
```
Result: FAIL. D2.2's basis is wrong: its 6,192 words include the figure JSON. Counted here, title to end of Self-check without figure JSON is 5,796 words, which is how R2's review, SCE1 and SCE3 (F27) count it. That is inside 2,000 to 6,000, and still is (5,970) after this check's PASS changes. The paragraph is sourced, and the review verified it (B&H §3.1, §3.2, bibliography [21], [22]). Not applied.
Syllabus: F17 (open) asks what the length range covers; this check does not decide it.

## Change 36
File: SCE2-inbound-and-storage.md
Current:
```
On how much, the textbook tests two rules commonly used: give every SKU the same space (Equal Space), or the same number of days of supply (Equal Time). It shows that Equal Time requires the same total restocks as Equal Space, contrary to the belief that it reduces them, and that neither is optimal (§8.3.2, Theorem 8.3) [practice]; for two warehouses it reports that Equal Time needed about 1.45 times the restocks of the optimal allocation for 6,000 fast-moving SKUs of a major drug-store chain, and about 2.44 times for 4,000 SKUs of a telecommunications company (§8.3.3) [practice]. This unit did not read the data behind the two ratios, so they are graded practice; they show the size of the difference the rule can make, not a figure to expect.
```
Replacement:
```
```
Result: FAIL. D2.3 rests on the same count as Change 35, so no length cut is needed. Its second ground, unconfirmed extraction (Unsure item 3), no longer holds: R2's pass 2 confirmed Theorem 8.3 and the 1.45 and 2.44 ratios of EQT to OPT restocks in the 0.98 PDF. Not applied, and Unsure item 3 stays.
Syllabus: F17 (open), as in Change 35.

## Change 37
File: SCE2-inbound-and-storage.md
Current:
```
picking starts in the evening (case register)
```
Replacement:
```
work starts in the evening for delivery the next morning (case register)
```
Result: PASS. R2.6 and D2.8 merged, verified: the register's Ostrel Distribution row reads "work starts in the evening for delivery next morning".
Syllabus: no conflict

## Change 38
File: SCE2-inbound-and-storage.md
Current:
```
the page shows no formula and no values
```
Replacement:
```
the page shows no formula, and its benchmark values are shown only to users with access
```
Result: PASS. R2.10 verified at the APQC page (24 Nov 2026). There is no formula ("Units for this measure are hours"), the percentile fields are blank with "Not all users have access to all of our resources", and a sample size of 3,561 is shown. The fix is worded closer to the page than the reviewer's "for members only".
Syllabus: no conflict

## Change 39
File: SCE2-inbound-and-storage.md
Current:
```
they are not WERC's wording.
```
Replacement:
```
they are not WERC's wording, and WERC's own definitions (in its online tool) were not opened, so of the five only dock-to-stock is set against a published description (APQC's, above).
```
Result: PASS. D2.12, with the fix reworded: the reviewer's "this cover item is met only for dock-to-stock" talks to the reader about the brief. The gap itself is verified (§8 and the front matter say WERC's definitions were not opened).
Syllabus: no conflict (F20 and F28 stay open)

## Change 40
File: SCE2-inbound-and-storage.md
Current:
```
and that recording batch codes and quantities at goods inwards and dispatch is best practice
```
Replacement:
```
and that best practice is to be able to say which batches, and what quantity, went to which customer, with the goods inwards area and the point of dispatch the best places to record it
```
Result: PASS. R2.11 verified at the FSAI page (24 Nov 2026): "best practice is to be able to say which batches and the quantity of which product went to which customer"; separately, "The best place to record information is at the goods inwards area and at the point of dispatch."
Syllabus: no conflict

## Change 41
File: SCE2-inbound-and-storage.md
Current:
```
Forward empty when picking starts in the evening
```
Replacement:
```
Forward empty when the evening's work starts
```
Result: PASS. D2.9 verified, as in Change 37.
Syllabus: no conflict

## Change 42
File: SCE2-inbound-and-storage.md
Current:
```
web pickers such as Mina, operator (register), depend on it
```
Replacement:
```
Mina, operator, picks web orders (register); her picks depend on it (this unit's reading)
```
Result: PASS. R2.7 and D2.10 merged. D2.10's wording is taken because it gives Mina's register role ("Operator, picks web orders") and labels the reading as row A9 does.
Syllabus: no conflict

## Change 43
File: SCE2-inbound-and-storage.md
Current:
```
## Sources
```
Replacement:
```
## Notes: facts for the case register

- Corvane: suppliers deliver by the pallet, so the centre breaks units pallet to carton and carton to each (section 2; this unit's assumption).
- Ostrel Foods: producers deliver by the pallet, so the warehouse breaks units pallet to case (section 2; this unit's assumption).
- Ostrel Foods: Ilse's chilled pickers depend on Bram's replenishment (section 6, deliverable A row 9; this unit's reading).
- Corvane: Mina's web picks depend on replenishment of forward locations (deliverable B row 9; this unit's reading).

## Sources
```
Result: PASS. R2.4 verified: the brief says a fact the unit invents about the case is listed in the notes. SCE2 lists none, and case-facts.md has no SCE2 rows. The first two notes are worded to match Change 28.
Syllabus: no conflict

## Change 44
File: SCE2-inbound-and-storage.md
Current:
```
8. GOV.UK page: "updated 22 October 2026" is the page's timestamp as extracted.
```
Replacement:
```
8. GOV.UK page: the page's public date is 25 June 2026 (metadata public-updated-at 2026-06-25); the metadata also carries an internal updated-at of 22 October 2026, which is not the public date.
```
Result: PASS. R2.2 and D2.1 merged, verified at the GOV.UK page (24 Nov 2026): first-published-at and public-updated-at are 2026-06-25, updated-at is 2026-10-22, and the page shows no "Last updated" label. §9 and Sources ("last updated 25 Jun 2026") stand, so D2.1's alternative (changing §9 and Sources) is not needed.
Syllabus: no conflict. This settles flag F25's matter (body and Sources stand, item 8 corrected), so F25 can be closed at filing.

## Change 45
File: SCE2-inbound-and-storage.md
Current:
```
fix · 1 errors, 10 should-fix, 16 minor; report
```
Replacement:
```
fix · 1 error, 10 should-fix, 16 minor; all applied; report
```
Result: PASS. R2.5 verified: the front matter says "every finding applied". "1 errors" is corrected as in Change 26.
Syllabus: no conflict

## Held

- R1.1 (Change 8) and R1.2 (Change 11), SCE1 §6: the Distributed Order Management row and the sentence that sets it against the abstract. This is fresh-check f4, still held. Route: flag. Someone re-reads https://www.gartner.com/magic-quadrant in a browser and records what the DOM row shows; then both changes go in together or neither does.
- R1.3 (Change 9) and R1.4 (Change 10), SCE1 §6: the Supply Chain Management Suites and Global Trade Compliance rows. The reviewer's fixes apply only if a browser read also lacks the rows. Route: the same flag and the same read.
- R1.5 (Change 2), SCE1 §1 and the §6 "(three industry variants)" row: the third Supply Chain Planning variant. The same index read decides it. Route: the same flag; if the read confirms only two variants, the §6 row is fixed at the same time.
- D1.1 (Change 15), SCE1 §11: eleven claims (C3 to C9, C11 to C14) are not set against evidence, which needs searches. Route: F2, carried. It is a proposal for the syllabus review the owner confirms (the brief replacement); if vetoed, SCE1 searches C3 to C14 and is refiled (f20).
- Not a finding, recorded so it is not lost: R2's note on F28 (the Hyster-Yale sentence "would verify") is that flag's own optional proposal for the owner. It has no Current or Fix and is not counted.

## Counts

Findings read: 49 (R1 15, D1 11, R2 11, D2 12). PASS: 41. FAIL: 2 (D2.2, D2.3). HOLD: 6 (R1.1, R1.2, R1.3, R1.4, R1.5, D1.1). Blocks: 45 (37 PASS, 2 FAIL, 6 HOLD). Merged findings share a block, and D1.10 and D1.11 each take two. Key: R1 = quality-review-SCE1, D1 = its delta, R2 = quality-review-SCE2, D2 = its delta, each numbered in report order. Only PASS blocks are applied, in order. Every Current, including those in FAIL and HOLD blocks, occurs exactly once in its file after the PASS changes before it. Sources opened 24 Nov 2026, each URL returned by a search in this agent: the Forrester Wave methodology page, the GS1 Logistic Label Guideline (ref.gs1.org), GOV.UK "Chilling and freezing", the APQC dock-to-stock page and FSAI "Traceability - FAQ". Gartner's index was not re-read. Body after PASS changes, title to end of Self-check without figure JSON: SCE1 5,807 words, SCE2 5,970.
