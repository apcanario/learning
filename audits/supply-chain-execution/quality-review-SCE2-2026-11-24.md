Verdict: SCE2 · fix · 0 error, 4 should-fix, 7 minor

Quality review of SCE2 · Inbound and storage (unit.md; identical to filed/SCE2-inbound-and-storage.md). Reviewer: claude-opus-5-5, isolated context, had not seen the unit written or any earlier check. Searches and fetches were run on 24 Nov 2026. The audit-units §3 prompt and the seven passes were run on the whole unit, including its Unsure list and fresh-check line.

(Saved by the main chat verbatim from the reviewer's reply: the harness refused the reviewer's own write. The reviewer's packet held SCE4's brief, not SCE2's; the brief check was re-run as `quality-review-SCE2-delta-2026-11-24.md`.)

PACKET NOTE: brief.txt holds the brief for SCE4 · Inventory and control, not SCE2. Its shared preamble applies to every unit and was used for the general rules (length, operations pattern, vendors, grades, case, site visit, self-check, templates). SCE2's own "Cover:" and "Deliverable:" lines are not in the packet. Coverage, the deliverable and the figures were therefore checked against the unit's own statement of its brief (front matter intro; §3 "The brief's sequence"; flow caption "Step names follow the course brief").

## Findings

[should-fix] [accuracy] §3.6 What the sources say; Current: "best-before, expiry and sell-by dates are optional, and where used must relate to the trade item on the label"; Problem: the guideline does not call the dates optional. Rule [4-18] says "If applicable one of the following dates should be given, depending on the type of product", §4.6 recommends including date information whenever it is relevant, and [4-19] (normative) says dates always relate to the GTIN on the label; Fix: "where applicable, one date (best-before, expiry, sell-by or another of the guideline's types) should be given, and it always relates to the trade item identified on the label"; Basis: GS1 Logistic Label Guideline r1.3, rules [4-18], [4-19], https://ref.gs1.org/guidelines/logistic-label

[should-fix] [style] Unsure list item 8; Current: "8. GOV.UK page: "updated 22 October 2026" is the page's timestamp as extracted."; Problem: this contradicts the body and Sources, which give "last updated 25 Jun 2026". The page carries public-updated-at 2026-06-25 (the public date) and an internal updated-at of 2026-10-22. SCE3's intro already flags that SCE2 gives the date two ways; Fix: "8. GOV.UK page: its public "last updated" date is 25 June 2026 (metadata public-updated-at 2026-06-25); the metadata also carries an internal updated-at of 22 October 2026, which is not the public date."; Basis: https://www.gov.uk/food-hygiene-businesses/chilling-and-freezing (page metadata)

[should-fix] [coverage] §3.3, §3.6, §3.7 (operations pattern); Current: "**Common failure.** Goods left in staging are in the building but not in a location the record knows (this unit's inference from §4.2)."; Problem: §3.3, §3.6 and §3.7 have no Measure line, and §3.7 has no People line. The deliverable rows still assign measures to these steps ("Dock-to-stock time starts here", "Percent with correct documents", "No benchmark found"), so the closing material adds mappings the body does not make; Fix: "**Common failure.** Goods left in staging are in the building but not in a location the record knows (this unit's inference from §4.2).\n\n**Measure.** Dock-to-stock cycle time starts at arrival (section 8) [practice]."; plus Current: "mixed-batch pallets are therefore split or labelled by the site's own scheme (this unit's inference)."; Fix: "mixed-batch pallets are therefore split or labelled by the site's own scheme (this unit's inference).\n\n**Measure.** None of WERC's five inbound measures is a labelling measure; the flow map uses the correct-documents measure as the nearest (section 8; this unit's reading)."; plus Current: "Whether either cross-docks is not in the register."; Fix: "Whether either cross-docks is not in the register.\n\n**People.** Whoever decides at the dock whether goods go to shipping or to storage; neither register names one.\n\n**Measure.** No inbound benchmark for cross-docking was found in the sources opened."; Basis: brief preamble ("Operations pattern ... the measure that shows it improved"); deliverable A and B rows 3, 6, 7.

[should-fix] [coverage] Notes for the case register (missing); Current: "## Sources"; Problem: the brief says "a fact the unit invents about them is listed in the notes". SCE2 relies on assumptions the register lacks and lists none of them. Neither register says Corvane or Ostrel receives pallets (§2's unit breaks). That Ilse's pickers and Mina depend on replenishment is the unit's reading. SCE3 has such a section; Fix: "## Notes: facts for the case register\n\n- Corvane: inbound goods arrive as pallets and cartons, so units are broken pallet to carton and carton to each (section 2; this unit's assumption).\n- Ostrel Foods: inbound goods arrive as pallets and are picked by the case (section 2; this unit's assumption).\n- Ostrel Foods: Ilse's chilled pickers depend on Bram's replenishment (section 6, deliverable A row 9; this unit's reading).\n- Corvane: web pickers such as Mina depend on replenishment of forward locations (deliverable B row 9; this unit's reading).\n\n## Sources"; Basis: brief preamble (Running case); case-facts.md; filed/SCE3 "Notes: facts for the case register".

[minor] [style] Fresh-check line; Current: "fix · 1 errors, 10 should-fix, 16 minor; report"; Problem: the line omits "all applied", which the audit-units §3 line format includes; Fix: "fix · 1 errors, 10 should-fix, 16 minor; all applied; report"; Basis: audit-units-SKILL.md §3.

[minor] [accuracy] §6 At the case operation; Current: "and picking starts in the evening (case register)"; Problem: the register says "work starts in the evening for delivery next morning", not that picking does; Fix: "and work starts in the evening for delivery the next morning (case register)"; Basis: case-facts.md, Ostrel Foods, Distribution.

[minor] [label] Deliverable B row 9; Current: "web pickers such as Mina, operator (register), depend on it"; Problem: the dependence on replenishment is the unit's reading, and the row does not label it, unlike Ostrel's row 9; Fix: "web pickers such as Mina, operator (register), depend on it (this unit's reading)"; Basis: case-facts.md, Corvane people.

[minor] [figure] §3 flow figure; Current: ""note": "where inspection applies""; Problem: the caption credits the notes to Bartholdi and Hackman and GS1, but the quality-hold note is the unit's unsourced working description (§3.5); Fix: ""note": "where inspection applies (working description)""; Basis: unit §3.5.

[minor] [label] §1; Current: "A cross-dock is a warehouse that consolidates without storing."; Problem: this is the unit's own summary and carries neither a grade nor an inference label; Fix: "A cross-dock, in this unit's summary, is a warehouse that consolidates without storing."; Basis: SCE1 §10 key.

[minor] [accuracy] §8 Definitions; Current: "the page shows no formula and no values"; Problem: the page shows a sample count (3,561, all companies) and hides its percentile values for members only; Fix: "the page shows no formula, and its benchmark values are for members only"; Basis: https://www.apqc.org/what-we-do/benchmarking/open-standards-benchmarking/measures/dock-stock-cycle-time-hours-supplier

[minor] [accuracy] §9 Traceability; Current: "and that recording batch codes and quantities at goods inwards and dispatch is best practice"; Problem: the page makes two separate statements and the unit joins them into one. Best practice is to "be able to say which batches and the quantity of which product went to which customer". Separately, the best places to record are "the goods inwards area and at the point of dispatch"; Fix: "and that best practice is to be able to say which batches, and what quantity, went to which customer, with the goods inwards area and the point of dispatch the best places to record it"; Basis: https://www.fsai.ie/business-advice/starting-a-food-business/traceability/traceability

## The seven passes

(1) References exist and match their records:
- Bartholdi & Hackman 0.98: PASS. Revised 28 Aug 2017; bibliography [21] is Frazelle 1996 and [22] is Frazelle 2002, as the unit says.
- GS1 Logistic Label Guideline: PASS, r1.3, Jul 2019.
- GS1 SSCC page: PASS; undated, no headline.
- APQC: PASS.
- FSAI labelling and traceability pages: PASS; undated, © 2026.
- USDA FSIS: PASS; undated.
- GOV.UK: PASS; public date 25 Jun 2026.
- WERC 2025 survey PDF: PASS.
- Staudt et al. 2015: PASS. RePEc/IDEAS gives IJPR 53(18) 5524–5544, DOI 10.1080/00207543.2015.1030466. The Crossref API itself was not queried.

(2) Claims against sources: every Bartholdi & Hackman quotation and section placement was found in the 0.98 PDF, which covers Unsure items 1 to 5:
- §2.2 SKU; ch. 3 opening (handling cost; scan at key decision points); §3.1, §3.2; the 10% and 15% shares citing [21, 22] and [21]; §4.1 to §4.3.
- §5.1.1 to §5.1.3; ch. 6 aisles and §6.2.1 deadheading; ch. 7 intro; §7.1.1 and §7.1.2.
- §8.1, §8.2; Theorem 8.3, with the "folk wisdom" that Equal Time reduces restocks and neither allocation optimal.
- §8.3.3: the ratio is the number of restocks under EQT over OPT, 1.45 for 6,000 drug-store SKUs and 2.44 for 4,000 telecom SKUs. This resolves Unsure item 3.
- §8.3.6, exercise 8.9, §8.4, §8.5.2, exercise 7.20, §1.1, §1.2, §2.4.
- GS1: [3-1], [4-20] and [4-24] are normative, [4-21] is best practice, and [9-19] (Despatch Advice / ASN) is not marked normative; all PASS. The "same type" sentence also PASS. This resolves Unsure item 10.
- FSAI labelling: PASS. USDA: PASS. GOV.UK: PASS.
- WERC: five names, no definitions, sample or values; regions include North America, EEA, Europe (not EEA) and Asia. PASS.
- Staudt abstract: PASS.
- Exceptions are in the findings above.

(3) Grades against SCE1's key: PASS.
- Textbook claims are practice. The Frazelle shares are practice with the origin said to be untraced.
- GS1 is a standard's text, so independent. Staudt is independent, with the abstract stated.
- WERC has no sample stated, so practice. APQC and the agency guidance are practice.
- The one ungraded summary line is in the findings.

(4) Vendors: PASS. No real vendor is named, assessed or mapped, and no private figure appears. Halvern Warehouse and Kestrow WMS (both fictional) carry only register facts, and the unit says they "say nothing about real products".

(5) Case against case-facts.md: PASS apart from the findings above. Every operation is labelled fictional on first use, all figures match the register, and every named person's role matches. No case operation uses a real product.

(6) Scope and tone: PASS. There is no AI, interview framing or craft method, and nothing about the owner or employer. The only "not X but Y" construction is a quoted source sentence in §3.2.

(7) Deliverable and figures:
- Present in full: Ostrel map (9 rows), Corvane map (9 rows), template with every blank saying what goes in it, and 26 glossary lines.
- 'On a site visit' (9 prompts) and 'Self-check' (8 questions) are present and agree with the body.
- Flow figure: PASS apart from the caption minor. Matrix figure: PASS; cells trace to §4, blanks are explained and the kind fits.
- Exact brief wording could not be checked (see the packet note).

Length: body to the end of Self-check is about 5,800 words without figure JSON, within 2,000–6,000. With the deliverable it is about 8,400; SCE3 has the same shape.

Pointers:
- SCE1 §3 (ERP holds POs as a working placement; a receipt pays the supplier): PASS.
- SCE1 §4 (yard management covers dock doors; module or separate system; no mention of appointments, confirmed): PASS.
- Carla added by SCE1: PASS. SCE1's key: PASS.
- SCE3 reuses the six columns and treats Corvane's two unit breaks: PASS.
- Pointers to SCE4, SCE5, SCE7 and SCE9 cannot be checked, because those units are not filed.

F28 (Hyster-Yale sentence for §8; not added): it would verify.
- Source: Hyster-Yale Materials Handling, Inc., "Benchmarking and Improving Distribution Center Metrics", © 2026, code 0000YBC0WP008_E_EN-US_54R0_082026, presenting WERC's 2026 report, at the yale.com yal-1558_werc2026updates PDF.
- It defines Dock-to-Stock Cycle Time as "Time elapsed between the arrival of goods and when they are put away and recorded into inventory management systems".
- It states no sample and defines no other inbound measure.
- The sentence must be graded vendor-reported, dated 2026, with "no sample stated".

## Could not verify
- SCE2's own brief: not in the packet, because brief.txt is SCE4's.
- GS1 SSCC page "such as a case, pallet or parcel": the fetch showed no examples.
- Whether pallet flow rack is stated to support FIFO: a fetch paraphrase said yes, but no verbatim text was obtained.
- Whether §1.1 has exactly two headings: the heading structure was not visible. This bears on self-check Q1.
- §3.2 "where it is stored largely decides how quickly it can be retrieved": not located in the extraction.
- The Crossref record for Staudt was not queried; RePEc matches.
- The texts of EU 1169/2011 Art. 24(1) and EC 178/2002, and US state rules: not opened.
- WERC's online definitions and its paid 2026 report: not opened.
