---
audit: fresh check
unit: SCE3 · Outbound: release, pick, pack, ship
course: supply-chain-execution · Supply Chain Execution for Product Teams
model: claude-opus-5-5
date: 2026-11-24
chat: https://claude.ai/code/session_01KMmgQyoX6Hnru9aiNiXdBA
verdict: keep · 0 errors, 0 should-fix, 0 minor
---

The checker's final report, verbatim, from its hand-back. Saved before any finding was applied.

Verdict: SCE3 · keep · 0 error, 8 should-fix, 14 minor

# Fresh check: SCE3, Outbound: release, pick, pack, ship

Checker: claude-opus-5-5 (Opus 5.5), isolated agent context that did not see the unit written; 24 Nov 2026; live search (WebSearch, then WebFetch only on URLs a search returned). Edits nothing. Every reference in Sources exists: **no missing reference**.

## Findings

- [should-fix] [accuracy] §3.5 "What it suits"; Current: "and in de Koster's pass-along, a finished order is put on a conveyor for onward transport (§5) [practice]"; Problem: in de Koster et al. §5 the conveyor sentence is in the bucket-brigade passage ("where it is put on a conveyor for further transport"). The pick-and-pass description has no conveyor. FAIL as worded; Fix: "and in de Koster et al.'s description of bucket brigades, the finished order is put on a conveyor for further transport (§5) [practice]"; Basis: https://pure.eur.nl/ws/portalfiles/portal/46713708/DesignandControl_2007.pdf §5.
- [should-fix] [accuracy] §9 C1 table, Dekker row; Current: "| Travel between locations takes about 50% of the total time spent picking orders |"; Problem: the report hedges the figure ("It is generally assumed that the time needed to travel between locations takes about 50%… [Tompkins et al. 1996]"). The table drops the hedge, which is the point of the C1 trace; Fix: "| "It is generally assumed that" travel between locations takes about 50% of the total time spent picking orders |"; Basis: https://repub.eur.nl/pub/168/erimrs20020222120221.pdf .
- [should-fix] [label] §2 Continuous release; Current: "at the sorter; and that in their simulations the best waveless policy gave larger or equal throughput than the best wave-based policy in every scenario considered [independent]."; Problem: one [independent] grade covers background framing (prevalence, "several advantages", "more expensive technology") and the study's finding. SCE1 §10 says a claim carries one grade and gives independent only to the source's own finding; Fix: "at the sorter [practice: the abstract's framing, not a finding of the study]. In their simulations, the best waveless policy gave larger or equal throughput than the best wave-based policy in every scenario considered [independent]."; Basis: SCE1 §10 key; publisher abstract https://pubsonline.informs.org/doi/10.1287/msom.1100.0291 .
- [should-fix] [label] §3.5 "What it costs"; Current: "Continuous release into a sorter needs more expensive technology than waves and risks gridlock (Gallien and Weber, abstract) [independent]."; Problem: "more expensive technology" is the abstract's premise, not a measured finding, so it is practice under SCE1's key. The gridlock risk is what their model is built to control; Fix: "Continuous release into a sorter needs more expensive technology than waves, in Gallien and Weber's framing (abstract) [practice], and risks gridlock, which their model sets release rules to hold below a chosen threshold (abstract) [independent]."; Basis: same abstract; SCE1 §10.
- [should-fix] [attribution] §6 "What the sources say"; Current: "the same rules apply to an outbound pallet or carton (SCE2 §3.6)."; Problem: SCE2 §3.6 covers inbound labelling only and does not say this. The extension is SCE3's own inference, from GS1's "storage and/or transport" definition that SCE2 quotes; Fix: "since GS1's logistic unit covers units packed for transport, the same rules apply to an outbound pallet or carton (this unit's inference from SCE2 §3.6)."; Basis: filed/SCE2 §3.6.
- [should-fix] [case] §8, Corvane paragraph; Current: "so whatever the departures are, the hours before them carry four times the work (this unit's reading)."; Problem: the register gives about four times a normal week's *web* volume, not four times all work, and it adds a third shift in peak; Fix: "so whatever the departures are, the web work before them is about four times a normal week's, with a third shift added in peak (case register; this unit's reading)."; Basis: case-facts.md, Corvane: Peak; Distribution.
- [should-fix] [case] Deliverable B, Corvane web orders; Current: "| What peak changes | Four times the orders into the same hours before each departure:"; Problem: same over-reach, and "the same hours" leaves out the register's third peak shift; Fix: "| What peak changes | About four times a normal week's web orders before each departure, with a third shift added in peak (register):"; Basis: case-facts.md.
- [should-fix] [coverage] length, §11; Current: "Each step's section above says what the system does there, with its source: release (section 2), picking and routing (sections 3 and 4), sorting (section 5), packing (section 6), staging, loading and the shipment record (section 7)."; Problem: the brief sets 2,000–6,000 words. The body before the deliverable is about 6,670 words of prose and about 8,190 with tables and figures (counted here; the writer's note says 6,600 and 7,600). That is over the brief's top. Nothing reads as padding. Cuts available: this cross-reference paragraph; §11's data list, which repeats deliverable E's "Data needed" column; the §2 wave/continuous table's restocking row, which repeats SCE2 §6. The owner may accept the overrun as the writer proposes; Fix: "" (delete the paragraph; optionally fold the "data it needs" list into deliverable E); Basis: brief.txt, "Length… (2,000–6,000 words)"; notes.md Contradictions 3.
- [minor] [accuracy] §6 Kim; Current: "states that in such manufacturers' warehouses the packing stage is often the most demanding one"; Problem: the report says "in OEM warehouses", which is wider than consumer-electronics manufacturers; Fix: "states that in original equipment manufacturers' (OEM) warehouses the packing stage is often the most demanding one"; Basis: https://repub.eur.nl/pub/112492/Repub_112492.pdf .
- [minor] [accuracy] §3.4; Current: "Choe and Sharp's 1991 tutorial suggests progressive zoning for orders that visit few zones and synchronised zoning for large orders"; Problem: the tutorial gives this as one way a system may work, not as a recommendation; Fix: "Choe and Sharp's 1991 tutorial describes, as one option, progressive zoning for orders that visit few zones and synchronised zoning for large ones"; Basis: https://www2.isye.gatech.edu/~mgoetsch/cali/Logistics%20Tutorial/order/article.htm .
- [minor] [attribution] §4; Current: "S-shape routes ran between 7% and 33% longer than optimal in simulations of single-block warehouses with random storage (§7.1, §7.3) [practice]"; Problem: the unit's own rule says the origin of a repeated number is named. De Koster et al. give this in §7.3 and credit it to 1998 studies by De Koster and co-authors (De Koster and Van der Poort, 1998, as extracted); Fix: "S-shape routes ran between 7% and 33% longer than optimal in simulations of single-block warehouses with random storage (§7.3, from 1998 studies by De Koster and co-authors) [practice]"; Basis: de Koster et al. 2007 PDF §7.3.
- [minor] [style] §1, term order (1 of 2); Current: "ABC analysis sorts items into a small fraction"; Problem: "skus"/"SKUs" is used before it is defined two sentences later; Fix: "ABC analysis sorts items (SKUs: a **SKU**, stock keeping unit, is SCE2's term for the smallest unit of a product an organisation tracks) into a small fraction"; Basis: brief, "define each term on first use".
- [minor] [style] §1, term order (2 of 2); Current: " A **SKU** (stock keeping unit) is SCE2's term for the smallest unit of a product an organisation tracks."; Problem: becomes a duplicate after the previous fix; Fix: ""; Basis: as above.
- [minor] [style] §2 Common failure; Current: "Releasing an order whose stock is not at the pick face:"; Problem: "pick face" is not defined here or in the glossary lines; Fix: "Releasing an order whose stock is not at the **pick face** (the forward location a picker takes the item from; course term):"; Basis: brief, glossary rule.
- [minor] [style] §8; Current: "found that a critical-ratio rule using the real-time queue of jobs gave the fastest flow time"; Problem: "critical-ratio rule" and "flow time" are not defined; Fix: "found that a critical-ratio rule (a priority rule that ranks jobs by the time left before they are due against the work they still need; the course's working definition) using the real-time queue of jobs gave the fastest flow time (the time from a job's arrival to its completion)"; Basis: brief, glossary rule.
- [minor] [figure] §2 flow figure, step "Label"; Current: "{"label": "Label", "note": "packed unit scanned as ready"}"; Problem: B&H §3.4's scan belongs to packing, which is the step before. The label step's own content in §6 is the carrier label and the SSCC; Fix: "{"label": "Label", "note": "carrier label; SSCC on a logistic unit"}"; Basis: unit §6.
- [minor] [figure] §2 flow figure, step "Load"; Current: "{"label": "Load", "note": "onto the carrier's vehicle"}"; Problem: §7 says "onto the vehicle". Ostrel (fictional) runs its own fleet, so "carrier's" does not trace to the text; Fix: "{"label": "Load", "note": "onto the vehicle, in stop order where staged"}"; Basis: unit §7.
- [minor] [attribution] Sources, B&H entry; Current: "Chapters 3, 4, 5, 7, 8, 10, 11, 14, 15, 16, 17 and bibliography."; Problem: §10 cites ch. 9 (popular items concentrated too much), which the list leaves out; Fix: "Chapters 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 16, 17 and bibliography."; Basis: unit §10.
- [minor] [figure] §9 C2 table, Dekker row; Current: "| Tompkins et al., 1996 (not opened) |"; Problem: no age is given, though the C1 table gives one; Fix: "| Tompkins et al., 1996 (not opened; 30 years) |"; Basis: brief, "with the source and its age stated".
- [minor] [figure] §9 C2 table, B&H row; Current: "| Frazelle, 1996 (not opened) |"; Problem: as above; Fix: "| Frazelle, 1996 (not opened; 30 years) |"; Basis: as above.
- [minor] [deliverable] Table A row 3; Current: "| Batch; do not spend on route optimisation |"; Problem: B&H §10.3.2 says optimisation "matters little" here. "Do not spend" turns that into advice the source does not give; Fix: "| Batch; route optimisation adds little |"; Basis: B&H §10.3.2.
- [minor] [case] Deliverable C, Ostrel row 1; Current: "| Warehouse module releases by route after the late-afternoon cut-off (2, 8) |"; Problem: release by route is SCE3's assumption (notes, fact 4) and is not marked as one in the map; Fix: "| Warehouse module releases by route after the late-afternoon cut-off (assumed; notes) (2, 8) |"; Basis: notes.md Case facts 4; case-facts.md.

## Pass 1: References exist and match
Every Sources entry was checked against the publisher's page, the issuing body's page or an index record (IDEAS/RePEc, LBS). All exist.
- de Koster, Le-Duc, Roodbergen 2007, EJOR 182(2) 481–501: PASS (IDEAS; version of record at pure.eur.nl; pii S0377-2217(06)00647-3, consistent with the DOI).
- Boysen, de Koster, Weidinger 2019, EJOR 277(2) 396–411, DOI 10.1016/j.ejor.2018.08.023: PASS (IDEAS).
- Gallien & Weber 2010, MSOM 12(4) 642–662, DOI 10.1287/msom.1100.0291: PASS. Authors and volume, issue and pages confirmed at https://lbsresearch.london.edu/id/eprint/351, which closes writer's unsure item 4 (LBS record, not Crossref).
- Batt & Gallino 2019, Management Science 65(6) 2624–2645, DOI 10.1287/mnsc.2018.3059: PASS (RePEc handle v65 i6; the IDEAS suggested citation shows "67(6)", which is inconsistent with its own handle).
- Kim 2020, CAIE 139, DOI 10.1016/j.cie.2018.12.011: PASS on authors, title, volume, year and DOI (MDX record). Article number not shown anywhere opened.
- Kim 2018, EI2018-02, author Thai Young Kim: PASS.
- Çeven 2013, Auburn dissertation, ISE (author Erdem Ceven): PASS.
- Choe & Sharp 1991, Georgia Tech: PASS (copyright 1991 Georgia Tech Research Corporation; author given as Kyung Il-Choe).
- Dekker, de Koster, Van Kalleveen, Roodbergen, ERS-2002-19-LIS, February 2002: PASS.
- ERIM "Order picking" page; Georgia Tech CALI "Importance of Order Picking": PASS (both undated, no author).
- WERC DC Measures Survey 2025: PASS. APQC: three measure pages, PASS. Hyster-Yale white paper: PASS (© 2026, code …_082026).
- B&H release 0.98: PASS (PDF at the authors' address; bibliography [21] is Frazelle 1996, confirmed). The "revised 28 Aug 2017" date was not re-read.

## Pass 2: Claims against sources
PASS (opened and read):
- de Koster: 55% "as much as" (abstract); "over 80% … Western Europe"; wave picking; sort-while-pick; pick-and-sort; put systems in a short window; travel "often the dominant component"; Fig. 4 from Tompkins et al. 2003; main disadvantage of zoning; three reasons for heuristics; Petersen 5%; S-shape 7–33%; small orders and batching; late orders and tight windows; bucket brigades self-balancing; discrete-picking aliases; order accumulation and sorting (§2.3); late lane assignment (§8).
- B&H: 55%/15%/10%/20% table credited to [21] Frazelle 1996; "about 55% of warehouse operating costs"; batching and pick density; "requires all the work of balancing an assembly line"; orders emerge in sequence; packing check and scan; shipping larger units, staging for reverse order, trailer scan at departure; WMS turns orders into pick lists and meets "daily shipping schedules"; wave management among high-end features; §4.1 records; conveyors partition into zones; sortation "purely for efficiency"; §7.4.2 congestion; §8.2 trigger and timing; §8.5.2 stockouts; ch. 9 popular items; §10.1 sequence, not path; distances not kept; "largest component of labor…"; §10.2 sort by location; §10.2.1 serpentine; §10.3.2 one-to-three items and batching; ch. 11 dense pick areas; §11.1 bucket brigade; §11.2 30%, 20% and 90%; Q14.1, Q14.3; 20/80; 5,000 SKUs over 75%; Fig 14.4 two-thirds and one-third; full distribution of lines per order; §15.1 bias quote; §16.3 congestion quote and downstream capacity; §17.2.3 "to avoid double-handling".
- Gallien & Weber: leading US online retailer; more expensive technology; gridlock; waveless larger or equal throughput in all scenarios.
- Batt & Gallino: "online and multichannel retailing"; up to 16%; about 5%; no sample in the abstract.
- Kim (MDX abstract): cut-offs ensure fulfilment time; critical ratio fastest flow time; simulation. Kim (EI2018-02): peaks quote; postponing the cut-off; next-working-day pick-ups spread across the day; packing (OEM: see minor finding).
- Çeven: wave definition; "missed orders and upset customers".
- Choe & Sharp: travel "a major portion"; 30–40% of labour cost (Gross 1981); time-window batching "minimal analysis"; idle zone pickers in synchronised zoning.
- Dekker: about 50% (hedged, see should-fix) and about 55% of operational costs, both credited to Tompkins et al. 1996 (no edition stated).
- ERIM: "as much as 60% of all labour activities… (cf. Drury, 1988)". CALI: "Some 63%…", no source given.
- WERC: names; 2024 performance; no definitions, sample or values; pop-up wording.
- APQC: the three definitions and the perfect-order formula; undated; sample sizes shown; the line-fill-rate median is shown as a dash.
- Hyster-Yale: On-Time Shipments and Order-Picking Accuracy definitions verbatim; no sample stated.
FAIL: de Koster §5 conveyor (should-fix above). Stretches: Dekker hedge; Kim OEM; Choe & Sharp "suggests".
Unverifiable: see the list at the end.

## Pass 3: Grades
Grades follow SCE1 §10/§C. The textbook and the review are graded practice; studies' own findings independent (Gallien & Weber, Batt & Gallino, Kim's simulation); Hyster-Yale vendor-reported; WERC and APQC practice (no sample or period, consistent with SCE2 §8). Abstract-only readings are stated for Boysen, Gallien & Weber, Batt & Gallino, Kim 2020 and Çeven, in text and in Sources. Not consistent with the key: two Gallien & Weber sentences give background framing an [independent] grade (should-fix ×2). No vendor statement is graded above vendor-reported.

## Pass 4: Vendors
PASS. The one real vendor is Hyster-Yale Materials Handling, Inc. It is named only to attribute a dated (2026) public document, graded vendor-reported, and is not assessed, ranked or recommended. No real product line is mapped. No private company's figure appears. The fictional vendors (Halvern Warehouse, Kestrow WMS) are labelled, match the register, are mapped "as an exercise", and are not tied to any real company. AI is handled in one sentence in §3.7.

## Pass 5: The case
PASS with two should-fix. Every case fact used was checked against case-facts.md: Corvane's 60 stores, four countries, 18,000 items, one-to-three-item web orders, carton and single-item replenishment, ×4 peak web volume, carrier portals, Mina, Tobias (added by SCE1), Jonas; Ostrel's 4,500 items, three zones, cases onto roll cages, evening start for next-morning delivery, 40 vehicles, about 600 points, fixed routes adjusted daily, late-afternoon cut-off, phone/web shop/sales staff, Ilse, Bram, Sofia, Nuno, substitutions, refused goods, paper notes. Each is labelled "(fictional)" on first use, never used as evidence, and never tied to a real product. Over-reach: "four times the work" and "same hours" (the register adds a third peak shift). Notes facts 1–5 match the assumptions in the deliverables; fact 4 is unmarked in deliverable C Ostrel row 1 (minor).

## Pass 6: Scope and tone
PASS. No AI treatment beyond the one-sentence exclusion. No interview framing. No craft method taught. Nothing about the Project's owner or his employer (read in full; kit/private_terms.py not in the packet, so not run). No flattery or filler. No "not X but Y" construction found. Regions are noted (Western Europe estimate; CMR and US bill of lading via SCE1 §2). Terms are defined on first use except SKU (order), pick face, critical-ratio rule and flow time (minor ×4). "Cluster picking" is handled honestly as undefined in the sources opened (notes, Contradictions 2).

## Pass 7: Deliverable and figures
Deliverable PASS against the brief. A (decision table: profile, method, reason, source and grade); B (worked for Corvane web, Corvane store, Ostrel case picking); C (two flow maps in SCE2's six columns, numbered as SCE2's); D and E (templates whose blanks say what goes in them); F (glossary lines). "On a site visit" and "Self-check" are present, and all eight Self-check answers agree with the body: Q1 §1, Q2 §3.4, Q3 §2, Q4 §4, Q5 §9, Q6 §4/B&H §10.3.2, Q7 §12, Q8 §8.
Figures:
1. flow (§2): kind fits. FIX: two step notes (minor findings above). The caption names its sections and sources.
2. decision (§3.8): PASS. Every question and outcome traces to §§3.1–3.6, and the caption names its sources and says the question order is the unit's own.
3. compare (§9): PASS. 55, 15, 10 and 20 trace to the §9 text, and the caption gives the source, its credit to Frazelle and the grade.
4. timeline (§9): PASS. 1981, 1988, 1991, 1996, 2002, 2007 and 2017, and every label ("30-40% of labour cost", "up to 60% of labour", "55%, travel 50-55%", "as much as 55%"), trace to the §9 tables and text; the caption is complete.
Length: should-fix above. The body is about 6,670 words of prose and about 8,190 with tables, against 2,000–6,000.
C1/C2 ages: arithmetic correct as of 24 Nov 2026 (35, 24, 19, 9, 30, 23, 45, 38). Two C2 cells have no age (minor). The C1 conclusion holds but should carry Dekker's "generally assumed" (should-fix). The notes item 4 C1 line for SCE1 §11 should add the same hedge.
F20: my searches also returned no WERC definitions page. The Hyster-Yale Dock-to-Stock wording is verbatim and correctly graded vendor-reported, so the optional SCE2 §8 line is sound.
F22: W2 correctly "not checked" (DOI redirect). W3's record exists (EJOR 122(3) 515–533, IDEAS handle v122 i3 p515-533), consistent with the writer's note. The Gu et al. 2010 DOI was not checked here.
Notes, Contradictions 1 (SCE2 GOV.UK date clash): confirmed that SCE2 §9 shows "last updated 25 Jun 2026". The page was not opened here.

## Could not verify
- Gallien & Weber: the word "prevalent" for wave release, and "congestion-induced collapse": only a publisher summary was read. The DSpace fetch was refused by the permission layer and the INFORMS /fpi page failed (client error); not checked.
- B&H section placements in ch. 14 (pick lines at §14.2 vs §14.2.2; Fig. 14.1 at §14.2.1 vs §14.2.2): two extractions disagree (writer's unsure item 2). B&H's "necessary first step… because customer orders drive the system" was read as "for nearly any serious warehouse project". The revision date of release 0.98.
- de Koster §3.4: "in a tote with its pick list"; low-level and high-level ("man-aboard") picking; time-window batching credited "after Choe and Sharp, 1991" (the extraction credits Tang and Chew 1997 and Le-Duc and De Koster for variable time windows).
- Çeven abstract: "waves are timed backwards from departures" (§8), a paraphrase of the abstract's deadlines theme.
- WERC: whether "Distribution Cost per Unit Shipped" and "Internal Order Cycle Time" sit among the outbound measures (the grouping is the writer's; unsure item 9).
- Kim 2020 article number; Crossref record not opened.
- kit/private_terms.py not available in the packet; not run.
