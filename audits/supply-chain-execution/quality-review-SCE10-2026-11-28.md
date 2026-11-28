---
audit: quality review
unit: SCE10
model: claude-opus-5-5
date: 2026-11-28
chat: https://claude.ai/code/session_01KMmgR1zm5V3ijatCgRUBSN
row: W-SCE10 (step 5a, flag F116)
---

claude-opus-5-5
Verdict: SCE10 · fix · 0 error, 8 should-fix, 14 minor

(Writing to /tmp/w10/qr10/out/report.md was refused, so here is the full report.)

# Quality review: SCE10 · The seams (as corrected)

Reviewer: fresh Opus 5.5 agent with live search. It had not seen the unit written or any earlier check. Date: 28 Nov 2026. No edits made. Addresses fetched were only those returned by a search in this agent.

## Findings

[should-fix] [coverage] §3 "The physical event"; Current: "**The physical event.** Packed units are staged, scanned onto a vehicle and leave; the driver signs (SCE3 §7; SCE7 §6, step 6)."; Problem: flags F34 and F44 give SCE10 "the cut-off and departure as the warehouse-to-transport handoff (SCE3 §8)". The unit never mentions the cut-off, and the notes do not record the flag; Fix: "**The physical event.** Packed units are staged, scanned onto a vehicle and leave; the driver signs (SCE3 §7; SCE7 §6, step 6). The handoff runs to a clock. The order cut-off is the latest time an order is accepted for a given dispatch, and the carrier departure is the time the vehicle leaves (SCE3 §8, working definitions). An order that misses the cut-off waits for the next departure (SCE3 §8; SCE7 §10, step 6)."; Basis: flags-all F34, F44; filed SCE3 §8 ("An **order cut-off** is the latest time an order is accepted for a given dispatch"; "A **missed cut-off**: the vehicle leaves without an order").

[should-fix] [deliverable] Deliverable A, row 16; Current: "| 16 | Return authorisation and refund trigger | Order system for the authorisation (SCE9 §9); the refund trigger is not in the register | Warehouse system (receipt, grade), ERP (refund) | Return received and not refunded, or refunded and not received (SCE9 A, rows 11, 12) | Order line Returns module authorises; which line grades is open (SCE6 B, row 14) |"; Problem: flags F64 and F89 ask SCE10 to "place the tender on its system-of-record table" using their sources. The table has no tender or booking row, and the notes do not mention either flag; Fix: "| 16 | Return authorisation and refund trigger | Order system for the authorisation (SCE9 §9); the refund trigger is not in the register | Warehouse system (receipt, grade), ERP (refund) | Return received and not refunded, or refunded and not received (SCE9 A, rows 11, 12) | Order line Returns module authorises; which line grades is open (SCE6 B, row 14) |\n| 17 | Carrier booking: the tender and the carrier's answer | Each carrier's portal (register; SCE7 A, rows 3, 4); no analyst definition names tendering (SCE1 §3; flags F64, F89) | Warehouse system (pickup time, if keyed) | Booked for a time the centre's dock cannot serve (10) | Transport line (Rating and Tendering; register) |"; Basis: flags-all F64, F89; filed SCE7 deliverable A rows 3–4; case register (Halvern Transport modules).

[should-fix] [deliverable] Deliverable A, line below the table (follows the previous finding); Current: "Below the table: sixteen facts; four rest on sourced placements (5, 7, 9, 10) and eleven on working placements or the register (1 to 4, 6, 11 to 16); row 8, and the refund trigger and the grading of returns in row 16, are open. The decision moves four owners (4, 11, 12, 13) and one approved charge (15); it leaves the ERP's facts (1, 2, 14) where they are."; Problem: the counts must change once row 17 is added; Fix: "Below the table: seventeen facts; four rest on sourced placements (5, 7, 9, 10) and twelve on working placements or the register (1 to 4, 6, 11 to 17); row 8, and the refund trigger and the grading of returns in row 16, are open. The decision moves five owners (4, 11, 12, 13, 17) and one approved charge (15); it leaves the ERP's facts (1, 2, 14) where they are."; Basis: the unit's own table once the previous finding is applied.

[should-fix] [accuracy] §7 table, Returns row, last cell; Current: "| Order system owns the authorisation and the refund trigger; the warehouse system owns receipt, grade and stock (course's) |"; Problem: this places the refund trigger in the order system. §5 says "this unit leaves it open too, as no source opened places it", deliverable A row 16 says it is not in the register and is open, and notes contradiction 8 says "the refund trigger stays open". The body contradicts itself; Fix: "| Order system owns the authorisation; the warehouse system owns receipt, grade and stock; which system triggers the refund is open (section 5) (course's) |"; Basis: unit §5, deliverable A row 16, notes contradiction 8.

[should-fix] [attribution] §12 table, row 2, "Who makes it" cell; Current: "Single-vendor ERP vendors ("vendors claim", as the authors report it)"; Problem: the words in quotation marks are not in the paper. The full text says "vendors of ERP software state that companies will have current technologies through upgrades"; Fix: "Single-vendor ERP vendors ("vendors of ERP software state", as the authors report it)"; Basis: Light, Holland, Kelly & Willis (2000), full text at https://salford-repository.worktribe.com/OutputFile/1499857 (read 28 Nov 2026).

[should-fix] [accuracy] §5, carrier invoice bullet; Current: "EUR-Lex lists the procedure as ongoing ([EUR-Lex, procedure 2023/0323/COD](https://eur-lex.europa.eu/procedure/EN/2023_323), read 28 November 2026) [independent]."; Problem: the search flag is on and the unit leaves out a dated current fact. The Commission's 2027 work programme, adopted 4 November 2026, announces 18 pending proposals that its Annex III says it intends to withdraw within six months. Press reports name the late-payment regulation among them, but the annex was not opened here. The grade is also wrong: a procedure record is not the text of a law, so SCE1's key gives practice; Fix: "EUR-Lex lists the procedure as ongoing ([EUR-Lex, procedure 2023/0323/COD](https://eur-lex.europa.eu/procedure/EN/2023_323), read 28 November 2026) [practice: the EU's procedure record, not a legal text]. The Commission's 2027 work programme, adopted 4 November 2026, has an Annex III of pending proposals it intends to withdraw within six months ([European Commission, 2027 Commission work programme](https://commission.europa.eu/strategy-and-policy/strategy-documents/commission-work-programme/commission-work-programme-2027_en?prefLang=bg), read 28 November 2026) [practice]. The annex was not opened, so whether this proposal is on it is not stated." (also add the page to Sources and to the source log); Basis: the Commission's 2027 work programme page (fetched; it says 18 proposals are to be withdrawn and gives the Annex III wording); EUR-Lex procedure page (fetched: "Ongoing", last event 11/07/2024); SCE1 §10, question 3.

[should-fix] [label] Source log (sources.md), row 13 and the missing entry; Current: "Later amendments not checked; EUR-Lex not tried"; Problem: the body says the EUR-Lex procedure page was read on 28 November 2026 and that a search found no amending act. The log says EUR-Lex was not tried and has no row for the procedure page, which Sources cites. Part 8 requires every Sources entry to be in the log; Fix: "No act amending Art. 3 found by search on 28 Nov 2026; no consolidated EU text opened; EUR-Lex procedure page read (row 26)", and add row "| 26 | European Commission, Proposal COM(2023) 533, procedure 2023/0323/COD | https://eur-lex.europa.eu/procedure/EN/2023_323 | Procedure page: status and events | 28 Nov 2026 | Proposal not adopted; procedure ongoing (§5) |"; Basis: unit §5; sourcing-standard Part 8 ("Every reference in Sources is in the unit's source log").

[should-fix] [label] Deliverable D, GDSN row; Current: "| GDSN | GS1's network for keeping trading partners' product data the same | GS1 [independent] |"; Problem: §6 grades the same page "[practice: a standards body's description of its own service, as section 9 grades X12's]". One claim carries one grade (SCE1 §10), and the page is a service description, not the text of a standard; Fix: "| GDSN | GS1's network for keeping trading partners' product data the same | GS1, How GDSN works [practice] |"; Basis: SCE1 §10, questions 3–4; unit §6.

[minor] [accuracy] §1 table, row "7 Pack and label", transport cell; Current: "(1 Plan, 2 Rate, 3 Tender, 4 Answer, 5 Book a dock, done ahead)"; Problem: SCE7 §6 names step 4 "Accept or refuse"; Fix: "(1 Plan, 2 Rate, 3 Tender, 4 Accept or refuse, 5 Book a dock, done ahead)"; Basis: filed SCE7 §6, step 4.

[minor] [style] §6, opening paragraph; Current: "When two copies differ, the error does not appear at the seam; it appears later, where someone acts on the wrong copy (this unit's inference)."; Problem: this is a "not X but Y" construction, which the brief's tone rule bans; Fix: "When two copies differ, the error shows later, where someone acts on the wrong copy (this unit's inference)."; Basis: brief, Tone.

[minor] [accuracy] §10, yard description; Current: "through the planning, direction and control of scheduling, movement, parking and inspection"; Problem: the page reads "supports the planning, direction, monitoring and control of activities. These include scheduling, moving, parking, inspecting and reassigning trucks, trailers and containers". The unit drops monitoring and reassigning; Fix: "through the planning, direction, monitoring and control of activities such as scheduling, moving, parking, inspecting and reassigning trucks, trailers and containers"; Basis: Gartner Peer Insights, Yard Management, https://www.gartner.com/reviews/market/yard-management (read 28 Nov 2026).

[minor] [accuracy] Deliverable D, YMS row; Current: "| Yard management system (YMS) | Software for scheduling, moving, parking and inspecting trailers in the yard |"; Problem: the source names trucks, trailers and containers; Fix: "| Yard management system (YMS) | Software for scheduling, moving, parking and inspecting trucks, trailers and containers in the yard |"; Basis: same Gartner page.

[minor] [figure] §10; Current: "the page lists 40 products and carries this description"; Problem: the gartner.com host of the same market page showed "Products 1 - 20 of 48" on 28 Nov 2026. The host the unit cites was not returned by a search here, so its count could not be checked. The count carries nothing; Fix: "the page carries this description"; Basis: https://www.gartner.com/reviews/market/yard-management (read 28 Nov 2026).

[minor] [accuracy] §2, Ishfaq et al.; Current: "in 50 interviews with supply chain executives at large store-based retailers, Ishfaq, Defee, Gibson and Raja found"; Problem: the design is understated. The abstract describes mixed methods: a qualitative evaluation of 50 interviews with supply chain executives of large retailers, plus secondary data on firm size, store and distribution networks and online sales. Part 8 asks for the design; Fix: "in a study combining 50 interviews with supply chain executives at large retailers with secondary data on firm size, store and distribution networks and online sales, Ishfaq, Defee, Gibson and Raja found"; Basis: Emerald abstract, https://www.emerald.com/insight/content/doi/10.1108/ijpdlm-02-2015-0032/full/html (read 28 Nov 2026).

[minor] [label] Deliverable B, row 2, "Who sees it first"; Current: "| Tobias's packer, if anyone (register) |"; Problem: the register names Tobias and no packers. "His packer sees it first" is this unit's reading; Fix: "| A packer on Tobias's shift, if anyone (reading of register; working) |"; Basis: case-facts.md, Corvane people.

[minor] [label] Deliverable B, row 9, "Who sees it first"; Current: "| Ilse's picker (register) |"; Problem: the register has the known trouble (short-dated stock found too late) but not who finds it; Fix: "| Ilse's picker (reading of register; working) |"; Basis: case-facts.md, Ostrel Foods.

[minor] [deliverable] Self-check 1 answer; Current: "A point where one system hands a fact to another. SCE9's rows"; Problem: the body defines a seam as a point where one system hands a fact to another "and stops being the place that changes it". The answer drops the second half, which is the part that ties a seam to the system of record; Fix: "A point where one system hands a fact to another and stops being the place that changes it. SCE9's rows"; Basis: unit, opening paragraph 2.

[minor] [deliverable] Deliverable D, Seam row; Current: "| Seam | A point where one system hands a fact to another | Course term (this unit) |"; Problem: same truncation as Self-check 1; Fix: "| Seam | A point where one system hands a fact to another and stops being the place that changes it | Course term (this unit) |"; Basis: unit, opening paragraph 2.

[minor] [style] Sources, the Hohpe & Woolf entry; Current: "- Hohpe, G. & Woolf, B. (2003)."; Problem: it sits after van de Weerd and X12 is still to come, so the list is out of alphabetical order; Fix: none (move the entry, unchanged, to follow GS1's GSIN entry); Basis: Sources list order.

[minor] [figure] Rendered figure files /tmp/w10/writer/out/figures/fig1-swimlanes.html and fig2-matrix.html; Current: fig2 shows row 7 "shipped?" and one legend line, "shipped? only if the warehouse's or carrier's message reached the order system". Fig1's caption lacks "(the 940 and 945 between companies, such as a logistics provider and its clients, section 2)"; Problem: the files predate the corrected viz blocks. The unit's blocks have "delivered?" in row 7, a separate "delivered?" legend entry and the longer caption; Fix: none (rebuild both from the unit's viz blocks with kit/build.py before filing); Basis: comparison of the files with the unit's viz blocks.

[minor] [label] notes.md, Needs 1, F17 sentence; Current: "F17: the body through the Self-check is about 6,100 words including tables, at the top of the brief's range"; Problem: a word count of the body to "## Deliverable" (viz lines excluded) gives about 6,300, above the brief's 6,000, not at the top of the range; Fix: "F17: the body through the Self-check is about 6,300 words including tables, above the brief's 2,000–6,000"; Basis: wc on unit.md.

[minor] [label] notes.md, Needs 1, flags not recorded; Current: "1. **Flags dealt with or not (SCE10).**"; Problem: Needs 1 does not account for F2 (C9 is now tested, so SCE1 §11's C9 row "Not searched here" needs SCE10's result by the correction route), F88 (carrier payment decided: §7 and deliverable A row 15), F44's FDA-date part (not used by SCE10), or F34, F44, F64 and F89 (see the findings above); Fix: none (add a line for each of F2, F34/F44, F64/F89 and F88 saying how it was dealt with, and propose SCE1 §11's C9 cell: "Tested in SCE10 §12: one ERP case study (Light et al. 2000), no independent source found on total cost; SCE16 prices it"); Basis: flags-all F2, F34, F44, F64, F88, F89.

## Pass 1 · References exist and match

- Alter (2014), CAIS 34, art. 55, doi 10.17705/1CAIS.03455: matches the AIS record. PASS.
- Bartholdi & Hackman, release 0.98: the title page reads "Revised August 28, 2017"; ch. 4 pp. 33–36 and section numbers match. PASS.
- Directive 2011/7/EU Art. 3, legislation.gov.uk copy as adopted: PASS.
- EUR-Lex procedure 2023/0323/COD: PASS (status "Ongoing"). The source log has no row for it (should-fix above).
- Gartner Peer Insights, DOM (features updated July 2025), WMS (May 2026) and SCM Suites (undated; 40 products): PASS. Yard Management: definition PASS at gartner.com; the external host and its 40-product count were not checked.
- GS1 EANCOM 2002 Part I §5: the content matches. The section title in Sources ("United Nation's Directories ...") was not confirmed, because the fetch tool reported different headings. See Could not verify.
- GS1 reference card (undated), GSIN page, How GDSN works page, Logistic Label Guideline release 1.3 (July 2019): PASS.
- Ishfaq, Defee, Gibson & Raja (2016), IJPDLM 46(6/7), 543–561, doi 10.1108/IJPDLM-02-2015-0032: PASS (Emerald).
- Klaus, Rosemann & Gable (2000), ISF 2(2), 141–162, doi 10.1023/A:1026543906354: PASS (IDEAS record).
- Light, Holland, Kelly & Willis (2000), ECIS 2000, paper 180: PASS. The AIS record lists Ben Light, Christopher P. Holland, Sue Kelly and Karl Willis.
- Light, Holland & Willis (2001), BPMJ 7(3), 216–224, doi 10.1108/14637150110392683: PASS (Salford record). The Emerald page was not opened.
- UN Treaty Series vol. 1208, No. 19487 (CMR Protocol 1978): PASS.
- UN/CEFACT Rec. 20, TRADE/CEFACT/2001/20, 15 Jan 2001: PASS. TRADE/CEFACT/2001/33, D.01A, 14 Feb 2001: PASS.
- van de Weerd, Vollers, Beerepoot & Fantinato, ECIS 2019 (Stockholm-Uppsala), paper 183: PASS. Every page header of the Utrecht copy reads ECIS2019, whatever its file name says.
- Woolf, Enterprise Integration Patterns site, "Integration Styles" introduction: PASS. The page footer credits Bobby Woolf.
- X12 856, 940, 945 and About X12: PASS.

## Pass 2 · Claims against sources

- 940 lets "the depositor or other business party" tell a warehouse to make, confirm, modify or cancel a shipment: PASS.
- 945 "It is used to reconcile order quantities with shipment quantities": PASS.
- 856 "describe the contents and configuration of a shipment" at various levels, with order, product, packaging, marking, carrier and equipment: PASS.
- About X12: ANSI-chartered more than 40 years; ANSI-accredited, consensus-based, non-profit; more than 320 transaction standards; "Millions of entities around the world": PASS.
- GS1 label: SSCC "the single mandatory element for all logistic labels"; the despatch advice gives each unit's SSCC and contents; a scanned SSCC should match it: PASS (clauses 3-1, 9-19, 9-36).
- GS1 card: definitions of GTIN, GLN, SSCC, GSIN and GINC; undated: PASS. GSIN "assigned by a seller and shipper of goods": PASS. GDSN "Everyone has access to the same continuously refreshed data", data pools and Global Registry: PASS.
- EANCOM: "All EANCOM® 2002 messages are based on the UN/EDIFACT directory D.01B"; GS1 is the agency controlling the subset; the description of UN/EDIFACT: PASS.
- D.01A: "IFTSTA International multimodal status report message UNSM D4 Transport (SWG)": PASS.
- Rec. 20: "the greatest possible clarity in the use of units of measure"; one list of codes: PASS.
- CMR Protocol Art. 2: 8.33 units of account per kg of gross weight short; the unit of account is the SDR; in force 28 Dec 1980: PASS.
- Directive Art. 3(3)(b)(i) (30 days from receipt of invoice) and 3(5) (60 days): PASS.
- EUR-Lex: proposal not adopted, procedure ongoing: PASS. The 2027 work programme's withdrawal annex is not reported (should-fix above).
- B&H: receipt drives supplier bills and shipping drives invoices (§4.1, p. 34); a WMS may talk to a YMS, and summary data go to a larger SCMS (p. 33); "extending their functionality out along the supply chain", "increasingly competing", "already connected to financial systems", "The enterprise systems have advantages where they can grow out of a manufacturing enterprise" (§4.5, p. 36): PASS. The text's "most fundamental capability" is paraphrased as "most basic": acceptable.
- Gartner DOM mandatory items (inventory for ATP/ATS, orchestration of routing and allocation, order visibility), July 2025: PASS. WMS core capabilities, May 2026: PASS. SCM suite "portfolio of (pre)packaged applications": PASS. YMS: PASS, but the wording is incomplete (minor above).
- Klaus et al.: methods, and "unlikely that at this stage a broadly agreed definition of ERP can be achieved": PASS.
- Light et al. 2000: record company, over 10,000 SKUs, about eighty countries, two interviewees over two years, plans and accounts, 80% rule and 80%-plus fit, about 36 months and comparable to single-vendor ERP, "no one strategy is the 'best' for all contexts", "the complexity of implementation", "the likely costs of future ownership", "may be left waiting for the next upgrade", simpler model and synergies, risk spread if a vendor "falls out of the market": PASS. "vendors claim" is not the paper's wording: FAIL (should-fix above).
- Light et al. 2001 abstract: complexity, functionality, process alignment, maintenance: PASS.
- Ishfaq et al.: 50 interviews; "integrating their store and DC inventories": PASS (design understated, minor).
- van de Weerd et al.: 12 team managers, four stores, March–June 2018, 29 workarounds, survey of 292; counts 159, 236, 247 and 6 on pp. 5–6: PASS.
- Alter: the uses for compliance and noncompliance and for systems analysis and design: PASS.
- Woolf: the four styles; "Each style has its advantages and disadvantages"; messaging "often the best style": PASS.

## Pass 3 · Grades against SCE1's key

- Standards' and treaties' texts are graded independent for what they say: correct (SCE1 §10, question 3).
- About X12 and GDSN (in §6) are practice: correct. The GDSN glossary row says independent: inconsistent (should-fix).
- The EUR-Lex procedure page is graded independent: it should be practice (folded into the §5 should-fix).
- Gartner definitions are analyst: correct. The yard description's attribution is flagged in the writer's unsure list: accepted.
- Light et al.: the arguments are practice and the case finding is independent, single case: acceptable split.
- Abstract-only readings say so (Ishfaq, Klaus, Light 2001, Alter): correct.
- Inference, reading and working lines carry no grade: correct.

## Pass 4 · Vendors

- No real vendor is named, assessed, ranked, compared, recommended or mapped. A grep for common vendor names found none.
- C9 sides are attributed to kinds of party: authors, single-vendor ERP vendors (as reported), best-of-breed advocates (as summarised), textbook authors, analyst, and fictional vendors.
- §7 declines to read real vendors' documentation and explains why (notes, contradiction 6). Accepted. The owner decides under contradiction 6.

PASS.

## Pass 5 · The case against case-facts.md

- Corvane, Tandric, Ostrel, Halvern, Varnby and Kestrow are each labelled "(fictional)" on first use. Corvane's first label is at §1 (line 32, after the front matter).
- Every register fact checked agrees with case-facts.md: 60 stores in four countries; ERP, warehouse system about twelve years old, order system and portals; known trouble; the people; the vendor slogans; the rows added by SCE1, SCE5, SCE7, SCE8 and SCE9.
- The case is never used as evidence.
- Register against working labels: two cells are labelled "register" for a reading (B rows 2 and 9; minor above). The assumptions of §8 are in notes 1–2.

## Pass 6 · Scope and tone

- No AI features, no interview framing, no craft method, no owner or employer content.
- Legal points are put as questions: the late-payment directive and the CMR claim.
- One "not X but Y" construction in §6 (minor).
- The body is about 6,300 words, over the brief's 6,000 (F17 open; notes miscount, minor).

## Pass 7 · Deliverable and figures

- **A. System-of-record table.** It has the brief's four columns (fact, owner, who else holds a copy, what breaks when they differ), plus one for the decision. It is built in full for Corvane. It has no tender row (should-fix).
- **B. Handoff failure catalogue.** It has the brief's columns (handoff, failure, who sees it first, who can fix it), plus Operation, and covers all three operations.
- **C. Templates.** C1 and C2 are present, and each blank says what goes in it.
- **D. Glossary lines.** Present.
- **On a site visit.** Agrees with §§2–5, 8, 10 and 11.
- **Self-check.** Seven questions, all agreeing with the body. Q1 truncates the definition (minor). Q5 agrees with the §7 stock row. The Returns row of §7 disagrees with §5 and with A row 16 (should-fix).
- **Fig 1** (swimlanes, §1): every label traced. The 940 is in §2; 945 and 856 are in §3; 214 is SCE8 §5 and IFTSTA is §4; the shipment-to-invoice link is B&H §4.1 in §5; carrier payment in the ERP is §5 and SCE1. Caption PASS. Kind fits a journey across actors. PASS.
- **Fig 2** (matrix, §8): the seven rows and three columns match the §8 table; the legend matches the text. Caption PASS. Kind acceptable (items by sections). PASS.
- The rendered files on disk are stale (minor).

## Part 8, line by line

- Sourced where made: yes.
- Acceptable source types: yes. The EUR-Lex procedure record is an official body's page.
- No video, blog or press rewrite cited: yes. The press items this review found are not proposed as sources.
- One grade per claim, following the key: no (GDSN row; EUR-Lex grade).
- Analyst reports say how they were read: yes. Only market pages are used; the 2026 SCM Suites report "refused", so nothing is stated from it.
- No vendor assessed or mapped: yes.
- Real vendors named only as allowed: yes (none named).
- Worked examples use only the fictional vendors, labelled: yes.
- Peer-review sites: only Gartner's definitions are used, no reviews: yes.
- Numbers say whose figure, the sample and the year: yes. The yard page's product count is unverifiable (minor).
- A study states its sample, setting and design: mostly. Ishfaq understated (minor). Inference from one setting is labelled (§§11, 12): yes.
- Common claim C9 set against evidence, with "No independent source found": yes. C14 is deferred to SCE13 with a statement: yes.
- Every Sources entry is in the source log: no (EUR-Lex procedure page missing).
- Sources match publisher and Crossref records: yes, except the EANCOM section title, which was not confirmed.
- Case facts labelled, agree with the register, never evidence: yes (two label slips, minor).
- No owner content: yes (no private term found by grep; kit/private_terms.py not run here).
- No AI, no interview framing, no craft method: yes.
- Search flag on, dated facts: mostly. The 2027 work programme's withdrawal annex was missed (should-fix).
- Deliverable built in full and as templates: yes.
- On a site visit and Self-check present and agreeing: mostly (refund-trigger contradiction).
- Not advice without evidence: yes. §12's gains and losses are labelled as the unit's reading.
- Links given as links, DOI for papers: yes. ECIS papers have no DOI and are given by their AIS address.

## Flags naming SCE10

- **F2:** C9 tested in §12. The notes do not propose the update to SCE1 §11's C9 row (minor).
- **F7:** dealt with as far as a source allows (§5, glossary, notes contradiction 4).
- **F8:** applied in the preamble.
- **F9, F18, F19, F80, F94:** owner decisions. SCE10 follows SCE1's key; noted in Needs 1.
- **F13, F21, F102, F110:** bibliography rows; Needs 2.
- **F34, F44:** the cut-off and departure handoff is not dealt with (should-fix). The FDA date in F44 is not used (minor, notes).
- **F64, F89:** the tender is not placed on the table (should-fix).
- **F66:** cap found; parties not checked (§5).
- **F68:** resolved (§4).
- **F71:** not applicable; no routing guide is used.
- **F76:** EU rule found; no error-rate study found (§5).
- **F79:** not resolved; stated in §9.
- **F88:** decided in §7 and A row 15, but not recorded in Needs 1 (minor).
- **F90 (with F73):** not resolved; Needs 1.
- **F96:** not reused; Needs 1.
- **F98:** decided (§7; notes contradiction 5).
- **F108:** A row 8 is left open; Needs 1.
- **F109:** not dealt with; Needs 1.
- **F113:** done.
- **F116:** this review.

## Could not verify

- The Salford copy of Light et al. (2000): which version it is, and whether its wording matches the ECIS printed text. The quotations were checked only against that copy, through the fetch tool's extraction.
- GS1 EANCOM 2002 Part I §5: the section title given in Sources. The fetch tool listed different headings.
- The Gartner Peer Insights yard page at the external.pi.gpi.aws.gartner.com host, and its "40 products". Not returned by a search here; the gartner.com host shows 48.
- Whether Annex III of the Commission's 2027 work programme (COM(2026) 710) lists COM(2023) 533. The annex PDF was not returned by a search, and a EUR-Lex document (C/2025/5423) refused the fetch. Press reports say it is listed; they are not sources.
- Directive 2011/7/EU Art. 3(5)'s "grossly unfair to the creditor" wording. Only the 60-day excerpt was returned.
- Ishfaq et al.'s "store-based" wording. The abstract returned said "large retailers".
- The Light, Holland & Willis (2001) record at Emerald. Not opened; the Salford record was used.
- The §7 dock and parcel rows' Gartner 2022 WMS and 2026 TMS readings. Taken from filed SCE6 and SCE8 and not re-opened (writer's unsure item 9).
- B&H §4.3 feature menu (basic, high-end and advanced features). Read only through SCE6 §6.
- GS1 GINC page. Not opened; the unit says it refused the fetch.
- kit/private_terms.py. Not run in this packet.
