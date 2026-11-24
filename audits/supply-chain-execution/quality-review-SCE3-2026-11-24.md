Verdict: SCE3 · keep · 0 error, 8 should-fix, 11 minor

Checker: claude-opus-5-5, isolated agent context, 24 Nov 2026. It had not seen the unit written or any earlier check. Edited nothing. Live search was on. Every fetch below used a URL returned by a search in this agent.

## Findings

[should-fix] [length] whole unit; Current: "# SCE3 · Outbound: release, pick, pack, ship"; Problem: the body (heading to "Self-check", figures excluded) is about 6,940 words, and the deliverable adds about 3,425 more, about 12,200 in the file. The brief sets 2,000–6,000 words. SCE2's body is about 5,810 words. Fix: no single replacement. Cut about 950 words from sections 1–12 without dropping any brief item. Candidates: the Georgia Tech 63% paragraph in section 9 (it "carries no evidence"; delete it and its Sources line); section 11, whose first paragraph only points to sections 2–7 and deliverables C and E; repeated case restatements in sections 8 and 10 that deliverable B repeats; Basis: brief.txt, "Length is whatever the topic needs (2,000–6,000 words)".
[should-fix] [coverage/flag] front matter, known gaps; Current: "no source was opened on carrier cut-off practice beyond one European field study"; Problem: flag F22 asks SCE3 or SCE4 to retry seed W2 (Gu, Goetschalckx & McGinnis 2007) and W3 (Rouwenhorst et al. 2000) from fresh searches. The unit never names either source, and does not say it is leaving them to SCE4; Fix: "seed W2 (Gu, Goetschalckx and McGinnis, 2007) and W3 (Rouwenhorst et al., 2000) were not retried here (flag F22) and are left to SCE4; no source was opened on carrier cut-off practice beyond one European field study"; Basis: flags.txt F22.
[should-fix] [attribution] 3.2 What it costs; Current: "**What it costs.** The batch must be split back into orders, either while picking or downstream (B&H §3.3) [practice]."; Problem: B&H §3.3 does not say this. The nearest text there is about assembling pieces picked "by different people in different areas", which is zoning. The two ways of splitting a batch are de Koster §2.2's sort-while-pick and pick-and-sort; Fix: "**What it costs.** The batch must be split back into orders, either on the cart while picking (sort-while-pick) or after picking has finished (pick-and-sort) (de Koster §2.2) [practice]."; Basis: B&H 0.98 §3.3, https://www2.isye.gatech.edu/~jjb/wh/book/editions/wh-sci-0.98.pdf; de Koster et al. 2007 §2.2, https://pure.eur.nl/ws/portalfiles/portal/46713708/DesignandControl_2007.pdf
[should-fix] [case] 8, Corvane; Current: "so whatever the departures are, the web work before them is about four times a normal week's (this unit's reading)."; Problem: the register says peak web volume is about four times a normal week. Carrying that to the work before each departure assumes the same departures in peak, and the register gives none; Fix: "so the week's web work is about four times a normal week's; how it falls across departures is not in the register (this unit's reading)."; Basis: case-facts.md, Corvane, Peak.
[should-fix] [case] Deliverable B, Corvane web orders; Current: "| What peak changes | About four times a normal week's web orders before each departure:"; Problem: the same stretch of the register as the section 8 finding above; Fix: "| What peak changes | About four times a normal week's web orders across the week (how they fall across departures is not in the register):"; Basis: case-facts.md, Corvane, Peak.
[should-fix] [figure] 2, flow figure caption; Current: "chapter 4 introduction and sections 3.4 and 3.5, as cited in those sections.\"}"; Problem: the caption says the notes come from de Koster and B&H. The "SSCC on a logistic unit" note comes from GS1 by way of SCE2 §3.6 (unit section 6), and the caption does not name that source; Fix: "chapter 4 introduction and sections 3.4 and 3.5, as cited in those sections; the SSCC note is from GS1's Logistic Label Guideline as SCE2 section 3.6 sets it out (section 6 of this unit).\"}"; Basis: unit section 6; audit-units-SKILL §3 Figures, rule 7.
[should-fix] [figure] 3.8, decision figure; Current: "\"q\": \"One item going to many orders in a short window?\""; Problem: the caption says every branch is a "suits" line of sections 3.1–3.6. De Koster's line is "a large number of customer order lines" in a short window. "One item going to many orders" is the unit's own inference (section 3.6 says so), so this node puts the unit's inference forward as the source's line; Fix: "\"q\": \"Many order lines to pick in a short window?\""; Basis: de Koster et al. 2007 §2.2 (put systems); unit 3.6.
[should-fix] [region] 7, Common failure; Current: "(B&H §17.2.3 on reverse loading \"to avoid double-handling\") [practice]."; Problem: B&H §17.2.3 is the textbook's account of warehousing in Singapore, Hong Kong and Japan ("must be loaded in reverse sequence of delivery to avoid double-handling"). The unit cites it as a general rule without its region, which the brief forbids; Fix: "(B&H §17.2.3, on practice in Singapore, Hong Kong and Japan: trailers \"must be loaded in reverse sequence of delivery to avoid double-handling\"; the general staging rule is B&H §3.5) [practice]."; Basis: B&H 0.98 §17.2.3 and §3.5; brief.txt, Regions.
[minor] [attribution] 3.2 What it is; Current: "Batching raises **pick density** (picks per unit of distance travelled), which cuts travel per pick (B&H §3.3) [practice]."; Problem: in release 0.98 the sentence about pick density and travel per pick is in the chapter 5 introduction. The term does not appear in §3.3; Fix: "Batching raises **pick density** (picks per unit of distance travelled), which cuts travel per pick (B&H ch. 5 introduction) [practice]."; Basis: B&H 0.98, ch. 5 introduction: "which increases pick density and so reduces travel per pick".
[minor] [attribution] Deliverable F, glossary; Current: "| Pick density | Picks per unit of travel | B&H §3.3 [practice]; wording the course's |"; Problem: wrong location, as in the 3.2 finding above; Fix: "| Pick density | Picks per unit of travel | B&H ch. 5 introduction [practice]; wording the course's |"; Basis: as above.
[minor] [accuracy] 3.2 What it costs; Current: "proximity batching is hard to solve exactly in some settings (de Koster §6) [practice]"; Problem: de Koster §6 says "order batching is an NP-hard problem, many studies focus on developing heuristic methods". It does not single out proximity batching; Fix: "order batching is NP-hard, so most studies develop heuristics (de Koster §6) [practice]"; Basis: de Koster et al. 2007 §6.
[minor] [grade] Deliverable F, glossary; Current: "| Continuous (waveless) release | Orders released one by one or in small groups as capacity frees | Gallien and Weber 2010 [independent] |"; Problem: this is a definition, not the study's finding. Section 2 grades the abstract's framing practice, and SCE1's key grades independent only a source's own finding; Fix: "| Continuous (waveless) release | Orders released one by one or in small groups as capacity frees | Gallien and Weber 2010 [practice]; wording the course's |"; Basis: SCE1 §10, question 3.
[minor] [grade] 2, Continuous release; Current: "[practice: the abstract's framing, not a finding of the study]"; Problem: the grade tag is not in the key's bracket form, which every other claim uses; Fix: "[practice] (the abstract's framing, not a finding of the study)"; Basis: unit's own grade rule, opening paragraph; SCE1 §10.
[minor] [attribution] Deliverable A, row 9; Current: "B&H §14.2.1, ch. 8; SCE2 §5 [practice]"; Problem: the fast-pick argument from Figure 14.1 (the 5,000 busiest SKUs, over 75% of picks) is in §14.2.2, as section 1 of the unit itself cites; Fix: "B&H §14.2.2, ch. 8; SCE2 §5 [practice]"; Basis: B&H 0.98 §14.2.2.
[minor] [accuracy] Deliverable A, row 7; Current: "| 7 | One item going to many orders in a short window | Put system |"; Problem: the profile is the unit's inference, and the row does not say so. De Koster's line is many order lines in a short window; Fix: "| 7 | Many order lines in a short window (for example one item going to many stores: this unit's inference) | Put system |"; Basis: de Koster et al. 2007 §2.2; unit 3.6.
[minor] [accuracy] 10, Missed cut-offs; Current: "Waves planned without regard to deadlines produce missed orders (Çeven, abstract) [practice]."; Problem: the abstract says that when the number and timing of waves are not planned systematically, "missed orders and upset customers are the result". "Without regard to deadlines" stretches that; Fix: "When the number and timing of waves are not planned systematically, missed orders result (Çeven, abstract) [practice]."; Basis: https://etd.auburn.edu/handle/10415/3716?show=full
[minor] [scope] 3.7; Current: "SCE5 treats the machines; where a vendor describes them as artificial intelligence, this course does not treat that."; Problem: the brief allows the one-sentence AI note only where a source raises AI. No source cited here does: Boysen et al.'s abstract does not mention it; Fix: "SCE5 treats the machines."; Basis: brief.txt, Out of scope.
[minor] [coverage] front matter, known gaps; Current: "on packing-station checks beyond the textbook"; Problem: the brief names cluster picking. Section 3.3 says no opened source defines it, but the known gaps do not list this; Fix: "on packing-station checks beyond the textbook, on a definition of cluster picking"; Basis: brief.txt, Cover list.
[minor] [case] notes; Current: "## Sources"; Problem: the unit cites "listed in notes" three times: Corvane store orders covering many items, Corvane stores on one route sharing a departure, and Ostrel releasing by route after the cut-off. The unit has no notes section, and the packet has no notes file, so the invented facts cannot be appended to the register. If a separate notes file exists, close this finding; Fix: "## Notes: facts for the case register\n\n| Unit | Operation | Fact |\n|---|---|---|\n| SCE3 | Corvane | Assumed: a store order covers many items across the range. |\n| SCE3 | Corvane | Assumed: stores on one route or carrier share a departure. |\n| SCE3 | Ostrel Foods | Assumed: the warehouse module releases by route after the late-afternoon cut-off. |\n\n## Sources"; Basis: brief.txt, Running case; case-facts.md rule 2.

## The seven passes

**(1) References against their publisher or Crossref record.**
- de Koster, Le-Duc & Roodbergen, EJOR 182(2) 481–501 (2007): PASS (RePEc; pure.eur.nl PDF).
- Boysen, de Koster & Weidinger, EJOR 277(2) 396–411 (2019), DOI 10.1016/j.ejor.2018.08.023: PASS (RePEc).
- Gallien & Weber, MSOM 12(4) 642–662 (2010): PASS (LBS Research Online gives 12(4) 642–662; the INFORMS page gives the DOI; MIT DSpace gives the authors).
- Batt & Gallino, Management Science 65(6) 2624–2645 (2019), DOI 10.1287/mnsc.2018.3059: PASS (RePEc).
- Kim, C&IE 139 (2020), DOI 10.1016/j.cie.2018.12.011: PASS on author, volume, year and DOI (Middlesex repository). Article number not confirmed.
- Kim, EI2018-02, author Thai Young Kim: PASS.
- Çeven 2013, Auburn dissertation, ISE: PASS. The record spells the name "Erdem Ceven" (no cedilla) and gives the date as 11 Jul 2013.
- Choe & Sharp 1991: PASS. Authors "Kyung Il-Choe and Gunter Sharp"; "Copyright: 1991 Georgia Tech Research Corporation".
- Dekker, de Koster, Van Kalleveen & Roodbergen, ERS-2002-19-LIS, February 2002: PASS.
- ERIM "Order picking" page, undated, no author: PASS.
- Georgia Tech CALI page, no author or date: PASS.
- WERC 2025 survey PDF: PASS.
- APQC measure pages (three), undated: PASS.
- Hyster-Yale white paper, 2026, code ...082026: PASS.
- B&H release 0.98: PASS on the PDF address. The 28 Aug 2017 revision date was not seen in the extraction.

**(2) Claims against sources.** PASS:
- de Koster: 80% "based on the authors' experience" (§2.2); wave picking and its usual combination with batch picking (§2.2); sort-while-pick and pick-and-sort (§2.2); put systems (§2.2); zoning benefits and its main disadvantage (§5); pick-and-pass and synchronised zoning (§5); bucket brigades self-balancing (§5); zone imbalance (§5).
- de Koster: batching criteria after Choe and Sharp (§6); "when orders are small" (§6); simple batching beating first-come first-served (§6, cited as De Koster et al. 1999b); routing heuristics (§7); 5% (Petersen 1997, §7.1); 7–33% (De Koster & Van der Poort 1998 and De Koster et al. 1998; single-block, random storage, simulation, §7.3); three reasons for heuristics (§7.1); Ratliff and Rosenthal linear time (§7).
- de Koster: sorter description, lanes and capacity (§8); late lane assignment (§8); late orders squeezing picking time (§1); "travel is often the dominant component" and Fig. 4 from Tompkins 2003 (§2.3); "as much as 55%" (abstract).
- B&H: §14 opening ("necessary first step"), §14.2.1 (20/80), §14.2.2 (strong indicator of work; 5,000 SKUs over 75%; complete distribution; Fig. 14.4), Q14.3; ch. 4 introduction (pick lists; "to meet shipping schedules"; tracks assembly); §4.1; §4.3 wave management.
- B&H: §3.3 (55% table credited to [21] Frazelle 1996; 55% of operating costs; assembly line; orders emerge in release sequence; shipment integrity); §3.4 (check, scan, parts to packing); §3.5 (larger units; staging; trailer scan); §5.2 and §5.2.1; §7.1.2 (defer restocks); §7.4.2 (congestion model); §8.2; §8.5.2.
- B&H: ch. 9 (concentrating popular items); §10.1 (sequence, not path); §10.2 (sort pick lines by location); §10.2.1 (serpentine); §10.3.2 (catalog centre; batching); ch. 10 ("largest component of labor"); ch. 11 (local search); §11.2 bucket brigades (over 30%, no change to layout or equipment; music distributor 20% and 90%); §15.1; §16.3 (both quotations).
- Gallien & Weber abstract; Batt & Gallino abstract (16%, experience, about 5%); Boysen abstract; Kim journal abstract (critical ratio, fastest flow time).
- Kim EI2018-02: postponing the cut-off; "Such cut-off rules induce order peaks just before the cut-off time"; pick-up times spread across the day; OEM packing "often the most demanding one"; a consumer-electronics manufacturer's DC.
- Çeven abstract; Choe & Sharp (major portion of total process time; 30–40% after Gross 1981; progressive and synchronised zoning; accumulation step; idle pickers; time-window batching needs minimal analysis); Dekker et al. (50% and 55%, both credited to Tompkins et al. 1996).
- ERIM (60%, cf. Drury 1988); Georgia Tech (63%, no source); WERC (all 16 names verbatim, no definitions, sample or values, 2024 performance); APQC (three definitions); Hyster-Yale (two definitions; no sample; no AI mention).
- FAIL or stretched: see the findings on B&H §3.3 batch splitting, B&H §3.3 pick density, de Koster §6 proximity batching and the Çeven stretch.

**(3) Grades against SCE1's key.** Consistent apart from the two minor findings: the glossary row for continuous release graded independent, and the non-standard grade tag. The review statements in de Koster and Boysen are graded practice, as SCE1 grades de Koster. The Kim report and the Çeven dissertation, neither peer-reviewed, are practice. WERC, with no sample stated, is practice. APQC definitions are practice. Hyster-Yale is vendor-reported. Batt & Gallino's, Gallien & Weber's and Kim's own findings are independent. Repeated numbers (Frazelle, Tompkins, Gross, Drury, bucket brigade [6]) are practice by origin.

**(4) Vendors.** PASS:
- No real software vendor is assessed, ranked, compared, recommended or mapped.
- Hyster-Yale is named once, for a dated public document, graded vendor-reported, with no private figure.
- Halvern Warehouse and Kestrow WMS modules appear only as case-register facts, labelled fictional and "say nothing about real products". No fictional vendor is tied to a real one.
- No case operation uses a real vendor's product.

**(5) Case against case-facts.md.** PASS, apart from the two findings on peak "before each departure" and the missing notes section. Every operation is labelled fictional on first use. Every person and role matches the register or SCE1's added rows (Tobias, Mina, Jonas). Ostrel's facts all match: Bram, Ilse, Sofia, Nuno, 40 vehicles, 600 points, late-afternoon cut-off, three zones, roll cages, paper notes, substitutions, refused goods, short-dated stock. Assumptions are marked "assumed". The case is never used as evidence.

**(6) Scope and tone.** PASS, apart from the minor finding on the AI sentence in 3.7. There is no interview framing and no craft method. Nothing touches the Project's owner or employer. No "not X but Y" construction was found. There is no flattery or filler.

**(7) Deliverable and figures against the brief.** Deliverable: PASS.
- A, the decision table: profile, method, reason and source.
- B, worked for Corvane web orders, Corvane store orders and Ostrel case picking.
- C, outbound flow maps in SCE2's numbered six-column form, for both operations.
- D and E, templates whose blanks say what goes in them.
- F, glossary lines.
- "On a site visit" (8 questions) and "Self-check" (8 questions) are present. All eight Self-check answers agree with the body and its sources.

Figures:
- Figure 1, flow, section 2: FIX (caption source; see findings). Labels trace to sections 2–7, and the kind fits.
- Figure 2, decision, 3.8: FIX (root node; see findings). Other branches trace to 3.1–3.5, and the kind fits.
- Figure 3, compare, section 9: PASS. 55/15/10/20 match B&H §3.3 and the text, and the caption names the source and Frazelle.
- Figure 4, timeline, section 9: PASS. Every date and figure is in the C1 and C2 tables. "Travel 50-55%" combines the 50% credited to Tompkins and the 55% credited to Frazelle, both in the text.

**Brief coverage.** Everything the brief names is covered: order profile; release, waves and continuous; one-order, batch, cart, zone, pass-along, conveyor and sorter, and goods-to-picker picking; routing; sorting; packing, labelling and checking; staging and loading; cut-offs; where a picker's time goes, with ages; failures; and measures by definition. Thin spots:
- Cluster picking: named, with no source.
- "What it costs" for the cart, put systems, sorters and goods-to-picker: inference, or no source.
- Cut-off practice: one field study.

**Flags naming SCE3.**
- F2: dealt with in section 9. C1 and C2 are traced in tables, with ages, against "no independent source found".
- F20: dealt with in section 12. The WERC definitions tool was not found. APQC (three measures) and Hyster-Yale (two) replace working definitions where they exist, and the rest are marked the course's. Nothing found would correct SCE2's inbound definitions.
- F22: not dealt with (should-fix above).
- F11 and F16 do not name SCE3. The unit cites the release it opened (0.98), as they propose.

## Could not verify
- B&H release 0.98 title-page date "Revised August 28, 2017" (not in the extraction).
- B&H §10.1/§10.3: that most WMS do not keep shortest distances between locations (only "must know the geometric layout" was found).
- Kim EI2018-02: that retailer orders leave "on the next working day" (only the pick-up times spread across the day were confirmed).
- Kim (2020): article number, and whether the journal text keeps the report's cut-off and packing sentences.
- Batt & Gallino: that the abstract names "online and multichannel retail fulfilment" as the setting.
- Gallien & Weber: Crossref record itself (citation confirmed at LBS Research Online, not Crossref).
- Choe & Sharp: whether the work was published in another venue.
- Dekker et al. (2002): which edition of Tompkins et al. the 1996 reference is (the reference list gives 1996 and no edition).
- de Koster Fig. 4 percentages (Tompkins 2003), and the origins Frazelle 1996, Tompkins 1996, Gross 1981 and Drury 1988 (not opened by the unit or this check).
- B&H bucket-brigade reference [6] (bucketbrigades.com), not opened.
- Çeven: the spelling of the surname (the Auburn record shows "Ceven").
- The unit's source log (sources.md) and notes file: not in the packet.
- python3 kit/private_terms.py: not run (not in the packet); read by eye.
