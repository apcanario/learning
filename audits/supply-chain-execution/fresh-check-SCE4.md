---
audit: fresh check
unit: SCE4 · Inventory and control
course: supply-chain-execution · Supply Chain Execution for Product Teams
model: claude-opus-5-5
date: 2026-11-24
chat: https://claude.ai/code/session_01KMmgQyoX6Hnru9aiNiXdBA
verdict: fix · 3 errors, 18 should-fix, 12 minor
---

The checker's final report, verbatim, from its hand-back. Saved before any finding was applied.

Verdict: SCE4 · fix · 3 error, 17 should-fix, 12 minor

Fresh check of SCE4 (Inventory and control), Supply Chain Execution for Product Teams. Checker: claude-opus-5-5, isolated agent context that did not see the unit written, live search, 24 Nov 2026. Prompt: audit-units-SKILL.md §3 with the figures paragraph. Audit errata: none were supplied in the packet. Body length, excluding the deliverable and the viz blocks: about 4,870 words, inside the brief's 2,000–6,000. All references exist. No reference stops the row.

## Pass 1 · References exist and match

All 13 Sources entries exist. Every DOI resolves to the stated work.
- DeHoratius & Raman 2008, Management Science 54(4) 627–641, DOI 10.1287/mnsc.1070.0789: matches RePEc/IDEAS. PASS.
- DeHoratius, Holzapfel, Kuhn, Mersereau & Sternbeck 2023, MSOM 25(1) 288–306, DOI 10.1287/msom.2022.1119: matches EconPapers. PASS.
- Kök & Shang 2007, MSOM 9(2) 185–205, DOI 10.1287/msom.1060.0136: matches Duke Scholars. PASS.
- Fleisch & Tellkamp 2005, IJPE 95(3) 373–385, DOI 10.1016/j.ijpe.2004.02.003: matches the St. Gallen record. PASS.
- Kull, Barratt, Sodero & Rabinovich 2013, JBL 34(3) 189–208, DOI 10.1111/jbl.12019: matches Marquette. PASS.
- de Koster, Le-Duc & Roodbergen 2007, EJOR 182(2) 481–501, DOI 10.1016/j.ejor.2006.07.009: matches the version of record. PASS.
- Rekik, Syntetos & Glock, ECR, October 2019: authors and date match. The date comes from the copyright line. PASS.
- Bartholdi & Hackman, release 0.98, revised 28 August 2017: PASS.
- 21 CFR Part 211: the title and "up to date as of 6/16/2026" are confirmed on eCFR. PASS.
- FDA traceability page: modified 4 Nov 2026. PASS.
- APQC "Inventory accuracy": PASS.
- Blackburn et al. working paper (2005): wrong author order. FAIL, see the findings.
- WERC DC Measures Survey 2025: not checked, because no search returned its address.

[should-fix] [attribution] Sources; Current: "Blackburn, J., Guide, V. D. R., Jr., Souza, G. & Van Wassenhove, L."; Problem: the repository record gives the authors as Souza, Guide, Van Wassenhove, Blackburn, and the published version (Management Science 52(8), 2006) as Guide, Souza, Van Wassenhove, Blackburn. Alphabetising them misstates the record. Fix: "Souza, G., Guide, V. D. R., Jr., Van Wassenhove, L. & Blackburn, J."; Basis: https://drum.lib.umd.edu/items/76d3af97-f39a-4e91-9e7e-19fceb1806f1/full (issued 13 January 2005).
[should-fix] [attribution] §7; Current: "Blackburn, Guide, Souza & Van Wassenhove, working paper, 2005"; Problem: same author order as above. Fix: "Souza, Guide, Van Wassenhove & Blackburn, working paper, 2005"; Basis: same record.

## Pass 2 · Claims against sources

[error] [accuracy] §9; Current: "Kull, Barratt, Sodero and Rabinovich found, in one multichannel retailer's daily data and a simulation,"; Problem: the abstract places the study in distribution centres. Its subject is retailers "fulfilling both brick-and-mortar and direct channel demands from their distribution centers". The full text studies one DC of a midsize US apparel retailer: 27 SKUs over 10 business days, 540 observations. The unit's premise that every inaccuracy study it opened is of stores is false, and so is unsure item 9 ("not established"). Fix: "Kull, Barratt, Sodero and Rabinovich, writing about multichannel retailers that fill store and direct orders \"from their distribution centers\", found, in one multichannel retailer's daily data and a simulation,"; Basis: https://epublications.marquette.edu/mgmt_fac/252 (abstract); https://core.ac.uk/download/213060804.pdf (full text).
[should-fix] [accuracy] §4 opening paragraph (body line 13); Current: "every study of record inaccuracy this unit could open was carried out in **retail stores**."; Problem: this follows from the Kull error and is false for Kull. Fix: "every study this unit could open that reports how many records were wrong was carried out in **retail stores**; the one distribution-centre study, Kull et al. (2013, section 9), was read in abstract and gives no rate."; Basis: as above.
[should-fix] [accuracy] front matter intro; Current: "Known gaps: the empirical studies of record inaccuracy that could be opened are all of retail stores, not warehouses."; Problem: same. Fix: "Known gaps: the empirical studies of record inaccuracy that could be opened and that report a rate are all of retail stores; the one distribution-centre study (Kull et al. 2013) was read in abstract only and gives no rate."; Basis: as above.
[should-fix] [accuracy] §9 "What it costs"; Current: "The evidence is indirect, and all of it from stores or textbooks:"; Problem: same. Fix: "The evidence is indirect: from stores, from a textbook, and from one study of a retailer's distribution-centre records whose abstract gives no cost per error:"; Basis: as above.
[should-fix] [accuracy] §10 C4; Current: "No independent source found measures warehouse record accuracy, at 99.9% or any other level."; Problem: Kull et al. measured DC record inaccuracy, according to its full text. Fix: "No independent source opened here reports a warehouse record-accuracy rate, at 99.9% or any other level; Kull et al. (2013), on a retailer's distribution-centre records, was read in abstract, which gives none."; Basis: as above.
[should-fix] [accuracy] Self-check 8; Current: "No independent source found measures it."; Problem: the answer must agree with the corrected §10. Fix: "No independent source opened here reports a warehouse rate."; Basis: as above.
[error] [accuracy] §5 "What to count"; Current: "The rules ranked items by sales, recorded decreases or increases, past error, forecast sales and days since the last count, and two ranked them by a model [independent]."; Problem: INVENTORY DEC and INVENTORY INC rank items by recorded stock, highest first and lowest first. They do not rank by recorded decreases or increases. RELATIVE DAYS is left out. Unsure item 3 flagged this paraphrase. Fix: "Seven rules ranked items by one index each: sales since the last count; recorded stock, highest first or lowest first; past error; forecast sales; days since the last sale relative to the forecast; and days since the last count. Two more ranked them by a model of the true stock [independent]."; Basis: DeHoratius et al. 2023, Table 1, https://edoc.ku.de/id/eprint/27376/1/msom.2022.1119.pdf.
[should-fix] [accuracy] §5; Current: "The best policy for empty shelves found over eight times the unknown out-of-stocks that random selection found [independent]."; Problem: the abstract names the policy: high-activity rules detect discrepancies best, and a low-activity rule ranking by low recorded stock finds over eight times the unknown out-of-stocks. Fix: "High-activity rules detected discrepancies best. A low-activity rule, ranking items by low recorded stock, found over eight times the unknown out-of-stocks that random selection found [independent]."; Basis: https://econpapers.repec.org/RePEc:inm:ormsom:v:25:y:2023:i:1:p:288-306.
[should-fix] [accuracy] Self-check 5; Current: "The best policies found over twice the discrepancies random selection found. The best one found over eight times the unknown out-of-stocks (section 5)."; Problem: the question asks "which" rules, and the answer gives only magnitudes. Fix: "High-activity rules, such as ranking by sales, found the most discrepancies, the best over twice what random selection found. A rule ranking by low recorded stock found over eight times the unknown out-of-stocks (section 5)."; Basis: as above.
[should-fix] [accuracy] §7; Current: "The ECR report links fashion's positive discrepancies (physical above record, in its sign) to product returns [independent: stores]."; Problem: this stretches the source. The report offers returns as a possible explanation, for two fashion retailers only: "This may be attributed to product returns that are very frequent in the fashion sector." Fix: "For two fashion retailers whose positive discrepancies (physical above record, in its sign) exceeded the negative, the ECR report suggests this \"may be attributed to product returns\" [independent: stores; an explanation offered, not tested]."; Basis: https://orca.cardiff.ac.uk/142664/1/84486%20ECR%20Inventory%20Inaccuracy%20Report.pdf.
[should-fix] [accuracy] §4; Current: "It found that manual adjustments were linked to discrepancies [independent]."; Problem: the finding comes from one retailer's data and has a direction: "Manually removing stock from the inventory records seems to lead to positive inventory discrepancies over time", and adding stock the opposite. Fix: "In one retailer's data it found that manually removing stock from the record \"seems to lead to positive inventory discrepancies over time\", and adding stock the opposite [independent: one retailer]."; Basis: ECR report.
[should-fix] [accuracy] §5; Current: "The ECR report's finding that manual adjustments are both a named cause and linked to discrepancies [independent] is the reason the question matters."; Problem: same. Fix: "The ECR report names manual adjustments as a cause and, in one retailer's data, found discrepancies following them [independent]; that is why the question matters."; Basis: ECR report.
[should-fix] [accuracy] §6; Current: "- **Random storage**: high space use, more travel."; Problem: the source's term is space *utilisation* (high utilisation, low space requirement). "Space use" can be read the opposite way. Fix: "- **Random storage**: high space utilisation (a low space requirement), at the cost of more travel; it works only under computer control."; Basis: de Koster et al. 2007 §4, https://pure.eur.nl/ws/portalfiles/portal/46713708/DesignandControl_2007.pdf.
[should-fix] [accuracy] §6; Current: "- **Dedicated storage**: the lowest space use of all."; Problem: the source says "space utilisation is lowest among all storage policies", meaning dedicated storage needs the most space. The unit's wording reads as if it needs the least. Fix: "- **Dedicated storage**: the lowest space utilisation of all policies, because a location stays reserved for its product even when that product is out of stock."; Basis: same.
[should-fix] [accuracy] §6; Current: "SCE2's glossary used the word more broadly, for assigning SKUs to locations, including which go forward (SCE2 §5)."; Problem: Bartholdi and Hackman also use the broad sense: "we slotted over 6,000 SKUs for a major chain retailer" (§8.6, sizing a forward area). The writer's contradiction 2, the proposed SCE2 §5 replacement, is not warranted. Fix: "SCE2's glossary used the word more broadly, for assigning SKUs to locations, including which go forward (SCE2 §5); Bartholdi and Hackman also use it that way, reporting that they \"slotted over 6,000 SKUs\" when sizing a forward area (§8.6) [practice]."; Basis: https://www2.isye.gatech.edu/~jjb/wh/book/editions/wh-sci-0.98.pdf §8.6.
[should-fix] [label] §3 (F23); Current: "They are a regulated setting, so applying them to food or fashion is this unit's inference."; Problem: Part 211 is CGMP for finished pharmaceuticals and binds manufacturers. 211.82–211.89 cover incoming components, containers and closures, not finished stock in a distribution warehouse. Fix: "21 CFR Part 211 governs the manufacture of finished drugs; its quarantine sections (211.82 to 211.89) cover incoming components, containers and closures, and holding and distribution are in 211.142 and 211.150. They are a regulated setting, so applying them to food or fashion, or to a distribution warehouse, is this unit's inference."; Basis: https://www.ecfr.gov/current/title-21/chapter-I/subchapter-C/part-211.
[minor] [accuracy] §6; Current: "They report that one retailer's slotting of over 6,000 SKUs cut the flow rack needed from 325 to 285 bays"; Problem: the authors did the slotting themselves, for a major chain retailer's national DC. Fix: "They report that their own slotting of over 6,000 SKUs for a major chain retailer cut the flow rack its national distribution centre needed from 325 to 285 bays"; Basis: B&H §8.6.
[minor] [accuracy] §8; Current: "Records go to FDA within 24 hours of a request."; Problem: the page says "within 24 hours or within some reasonable time to which the FDA has agreed". Fix: "Records go to FDA within 24 hours of a request, or within a reasonable time FDA agrees to."; Basis: https://fda.gov/food/food-safety-modernization-act-fsma/fsma-final-rule-requirements-additional-traceability-records-certain-foods.
[minor] [label] §7; Current: "The system matches it to the original order where it can, records the item and quantity, and puts it into a held status until graded."; Problem: a mechanism with no source and no inference label. Fix: "The system matches it to the original order where it can, records the item and quantity, and puts it into a held status until graded (working description, unsourced)."; Basis: Part 1, "unsourced is said".

Confirmed (PASS), read live on 24 Nov 2026:
- DeHoratius & Raman abstract: nearly 370,000 records; 37 stores of one retailer; 65%; 26.4% and 2.7%; HLM; 67.6% across stores and 69.0% across categories. This resolves unsure item 4.
- DeHoratius et al. 2023 full text: 10 dm stores, about 500 items, 9 categories, spring 2017, students; week-3 count 31%, stores 19–45%; the sign definition; phantom and hidden; counting depth; "over twice"; Mosconi.
- ECR: seven retailers, four countries, 91 stores, 233,318 SKUs; 59.54%, 63.39%, 54.08%, 6.20–73.33%; "single unit"; the sign; causes; negatives accumulate and positives stay stable; 3.83–8.38%, average 5.98%, test against control stores (resolves unsure item 2); "high discrepancy fast movers".
- Kök & Shang: the threshold inspection; near optimal.
- Fleisch & Tellkamp: the causes quotation; three echelons.
- Kull: "increases inventory levels while also decreasing service levels".
- Blackburn et al.: more than US$100 billion; 90 days.
- Every B&H quotation, including §4.2, §2.4, ch. 9, §8.1, §8.6, §9.3, §3.7, §3.4, §4.3 and ch. 18 "What to count and when…" (resolves unsure item 5).
- de Koster §4: definitions; reshuffling; Petersen and Roll & Rosenblatt as cited.
- 21 CFR 211.82(a)(b), .84(a), .87, .89, .130(c), .137, .142, .150(a)(b), .196, .204, .208: all verbatim; the Part title is confirmed (resolves unsure item 6).
- FDA page: TLC; CTEs; the 24-hour spreadsheet; both compliance dates and the congressional direction.
- APQC: the definition, percent, "4,283", no values.

Inventory record research: sample, setting and design are stated before the numbers (PASS), and store-to-warehouse extensions are labelled as inference, apart from the false "all stores" premise corrected above.

## Pass 3 · Grades against SCE1's key (SCE1 §10)

PASS. The CFR is graded independent, the FDA summary practice, WERC and APQC practice, ECR independent (unsure item 1 notes the caveat), Fleisch & Tellkamp practice, Kök & Shang independent, and B&H practice. Abstract-only readings are said to be so in the text. No vendor statement is graded.
[minor] [label] Deliverable E; Current: "Staff walk the aisles noting empty locations | DeHoratius et al. 2023 [independent]"; Problem: §5 grades the same content as practice (origin not opened). Fix: "Staff walk the aisles noting empty locations | DeHoratius et al. 2023 [practice]"; Basis: SCE1 §10 Q3.

## Pass 4 · Vendors

PASS. No real software vendor is named. Associations and regulators only. Halvern Warehouse's (fictional) Slotting module is a register fact graded nothing. There are no private figures.

## Pass 5 · The case

PASS. Every fact matches case-facts.md, including the Added-by-units rows. Each operation is labelled "(fictional)" on first use, and the case is never used as evidence.
[minor] [label] Deliverable A row 1.1; Current: "Mina at a short pick; Carla at a count |"; Problem: Carla counting is not in the register or the notes. Fix: "Mina at a short pick; Carla at a count (assumption) |"; Basis: case-facts rule. Also add a notes row: SCE4 · Corvane · Carla runs or reviews counts.
[minor] [accuracy] §9 step 5; Current: "answers customers about shipments (case register)"; Problem: the register reads "shipments in transit". Fix: "answers customers about shipments in transit (case register)"; Basis: case-facts.md, SCE1 row.
[minor] [deliverable] Deliverable A row 4.1; Current: "A count; the ECR report links fashion overs to returns (section 7)"; Problem: must agree with the corrected §7. Fix: "A count; the ECR report suggests fashion overs may come from returns (section 7)"; Basis: ECR report.

## Pass 6 · Scope and tone

PASS on scope:
- No AI features, no interview framing and no method teaching.
- Nothing about the owner or his employer.
- Legal and regulatory points are put as questions.
[minor] [style] §8; Current: "US drug distribution records must hold the product, the consignee's name and address"; Problem: "consignee" is not defined. Fix: "US drug distribution records must hold the product, the consignee's (receiver's) name and address"; Basis: brief, define terms on first use.
[minor] [style] §4; Current: "simulation of a three-echelon retail chain"; Problem: "echelon" is not defined. Fix: "simulation of a three-echelon (three-tier: for example supplier, warehouse, store) retail chain"; Basis: brief.
[minor] [style] Deliverable E; Current: "| A pick that takes the wrong item or quantity |"; Problem: overlaps "short pick", and §4 says "wrong item or size". Fix: "| A pick that takes the wrong item or size |"; Basis: unit §4.

## Pass 7 · Deliverable and figures

Deliverable: PASS on structure.
- The cause tree has the brief's four columns plus a branch column and is built for Corvane (13 rows).
- The Ostrel count plan has 16 elements.
- Both templates are present, and every blank says what goes in it.
- Glossary lines are present.
- "On a site visit" and "Self-check" are present. Self-check answers agree with the body except 5 and 8 (fixed above).
[minor] [deliverable] Deliverable B; Current: "Section 5 (rule DAYS)"; Problem: the body never uses the name "DAYS". Fix: "Section 5 (DeHoratius et al. 2023: days since the last count)"; Basis: DeHoratius et al. Table 1.
[minor] [label] Deliverable B; Current: "never adjusted out unrecorded | Section 3 |"; Problem: drug rules are applied to food without the inference label. Fix: "never adjusted out unrecorded | Section 3 (US drug rules applied to food: this unit's inference) |"; Basis: brief.

Figures:
- Figure 1 (states, §3): FIX. The kind fits. The rejected → destroyed "dispose" transition is not in the text, and the caption's "back to stock only if proven" has no transition.
[error] [figure] §3 viz; Current: "{"from": "rejected", "to": "destroyed", "label": "dispose"}"; Problem: a transition that is not in the unit's text. Fix: "{"from": "returned", "to": "available", "label": "proven fit"}"; Basis: §3 step 3 (211.89), §7 (211.204), the caption.
- Figure 2 (compare, §4): PASS. 65, 59.54 and 31, with their samples, are traced to §4. The caption and kind are fine.
- Figure 3 (flow, §9): FIX. Count and adjust sits last, but §9 step 2 puts it right after the short pick.
[should-fix] [figure] §9 viz; Current: ", {"label": "Count and adjust", "note": "location checked, record corrected", "tone": 2}]"; Problem: the order of steps does not match the text. Fix: "]"; Basis: §9 step 2.
[should-fix] [figure] §9 viz; Current: "{"label": "Short pick", "note": "Mina reports the line", "tone": 4}, "; Problem: same, the second half of the move. Fix: "{"label": "Short pick", "note": "Mina reports the line", "tone": 4}, {"label": "Count and adjust", "note": "location checked, record corrected", "tone": 2}, "; Basis: §9 step 2.

## Also checked

- **F12:** the abstract was opened, and every number the unit uses is in it. Closing F12 is supported.
- **F23:** sourced, with quotations verified. The extension to other goods is labelled in §1, §3 and the figure caption, but the manufacturer and components scope is not stated (should-fix), and Deliverable B's Holds row lacks the label (minor). Not otherwise stretched.
- **F34:** the SCE3 §10 pointer holds (short pick defined; "wrong item or quantity … SCE4 traces"). Closing F34 is supported.
- **Contradiction 1 (SCE2 §3.5 and glossary):** the quotations match SCE2 lines 106 and 378. The proposal is accurate; add "incoming components".
- **Contradiction 2 (SCE2 §5 and glossary "Slotting"):** not supported, because B&H §8.6 uses the broad sense. Withdraw the replacement and add only a cross-reference to storage assignment.
- **Contradiction 3 (SCE1 §11 C4):** the quotation matches SCE1 line 187. The new cell should add "one distribution-centre study (Kull et al. 2013) read in abstract gives no rate" and say "reports" rather than "measures".
- **Filed-unit pointers:** all hold: SCE1 §10; SCE2 §2, §3.3–3.6, §3.8, §4, §5, §6, §8, §9; SCE3 §3, §6, §10, §12. Internal section pointers all match.
- **notes.md Need 5 and unsure item 9** are wrong, per the Kull error.

## Could not verify

- WERC DC Measures Survey 2025 PDF: no search returned the address, so it was not fetched. The measure names in §10 and Deliverable B are not checked.
- ECR Experiment I comparison basis: read through an extraction only, not the report's tables.
- Petersen et al. 2004, Roll & Rosenblatt 1983 and Mosconi et al. 2004 were not opened; they are known only as cited.
- SCE2's GS1 and FSAI sources behind the §1, §2 and §8 pointers were checked against SCE2's text only.
