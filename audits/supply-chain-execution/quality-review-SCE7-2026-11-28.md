---
audit: quality review
unit: SCE7 · Transportation in practice
course: supply-chain-execution · Supply Chain Execution for Product Teams
model: Opus 5.5 (claude-opus-5-5)
date: 2026-11-28
chat: https://claude.ai/code/session_01KMmgQzMe8qwXyeLryD2JaE
verdict: fix · 1 errors, 2 should-fix, 13 minor
---

The checker's final report, from its hand-back, with the findings' "fN ·" ids and cross-references to them reworded to plain descriptions so that `thin.py fixes` can parse it (the chat had to write the file: the agent's Write was refused). Saved before any finding was applied.

claude-opus-5-5

The Write tool refused /home/claude/work/qr7/out/report.md ("Subagents should return findings as text"), so the full report follows here.

# Quality review: SCE7 · Transportation in practice (unit.md as it now stands)

Checker: a fresh claude-opus-5-5 agent that had not seen the unit written and was not shown any earlier check. Live search on 28 November 2026. Procedure: audit-units-SKILL.md §3 fresh-check prompt and its figures paragraph, run as the seven passes of the quality review. Every URL fetched was one that a WebSearch in this agent returned. Quotations come from a fetch tool's extraction and were not read against a second copy.

## Findings

[should-fix] [accuracy] §13, European Union bullet; Current: "No later Eurostat figure for the empty share was found (the later Eurostat news items on road freight that were opened give none), so 2020 is the latest year given here."; Problem: Eurostat publishes a later empty share. Its Statistics Explained article "Road freight transport by journey characteristics" (data extracted August 2024) gives 2023: "one fifth of total road freight vehicle-kilometres were carried out by empty vehicles (21.8%)", national about one quarter (25.9%), international 13.1%. The unit presents 2020 as the latest year and builds C12's verdict on it. Fix: "A later figure is on Eurostat's Statistics Explained page: in 2023, one fifth of EU road freight vehicle-kilometres (21.8%) were run by empty vehicles, 25.9% in national and 13.1% in international transport (data extracted August 2024) ([Eurostat, \"Road freight transport by journey characteristics\"](https://ec.europa.eu/eurostat/statistics-explained/index.php/Road_freight_transport_by_journey_characteristics)) [independent]; the 2020 country figures above come from the 2021 news item, and the figure below shows 2020."; Basis: https://ec.europa.eu/eurostat/statistics-explained/index.php/Road_freight_transport_by_journey_characteristics

[minor] [attribution] Sources, Eurostat road_go entry; Current: "- Eurostat. \"Road freight statistics (road_go)\", reference metadata, last updated 22 July 2026. https://ec.europa.eu/eurostat/cache/metadata/en/road_go_esms.htm"; Problem: the new reference of the finding above needs a Sources entry. It also needs a source-log line, and the applier needs to update the opened-on lead-ins (the preamble and Sources) with its date. Fix: "- Eurostat. \"Road freight statistics (road_go)\", reference metadata, last updated 22 July 2026. https://ec.europa.eu/eurostat/cache/metadata/en/road_go_esms.htm\n- Eurostat. \"Road freight transport by journey characteristics\", Statistics Explained, data extracted August 2024. https://ec.europa.eu/eurostat/statistics-explained/index.php/Road_freight_transport_by_journey_characteristics"; Basis: https://ec.europa.eu/eurostat/statistics-explained/index.php/Road_freight_transport_by_journey_characteristics

[should-fix] [coverage] §5, second paragraph; Current: "Paying the carrier is not in the definition; where the payment is held"; Problem: flag F88 proposes this exact addition by the correction route, and it has not been applied. SCE1 §3 (TMS row) and SCE10 §7 (Carrier payment row) both cite Gartner's TMS glossary entry, "manage freight bills and payments" (SCE8 §1), but SCE7 still reads as if no source places payment in the TMS. Fix: "Paying the carrier is not in the definition; Gartner's glossary entry for the TMS (undated) places freight bills and payments in the TMS (SCE8 §1) [analyst]; where the payment is held"; Basis: filed SCE8 §1 (Gartner glossary, TMS entry, as cited there), syllabus-flags F88; the glossary page itself was not opened by this checker.

[error] [figure] §6, swimlanes figure, step "6 Pick up"; Current: "\"note\": \"CMR note or BOL\""; Problem: the procedure requires every label in a figure to appear in the unit's text. "BOL" is not in the text, which always writes "bill of lading". This is mechanical, but the rule grades it as an error. Fix: "\"note\": \"CMR note or bill of lading\""; Basis: unit §6 step 6 and §7 ("bill of lading").

[minor] [accuracy] Self-check 4, answer; Current: "not with past behaviour (section 4)"; Problem: the paper says soft-market shipper behaviour did not, in general, predict tight-market PAR. It names one exception (soft-period destination dwell, for non-asset carriers), and it finds that soft-market PAR, "an indicator of previous carrier behavior", does predict tight-period PAR. "Not with past behaviour" overstates this, and section 4 itself says "in general". Fix: "not, in general, with the shipper's own soft-market behaviour (section 4)"; Basis: https://sheffi.mit.edu/sites/sheffi.mit.edu/files/2021-01/Acocella_Sheffi_Publication%202020.pdf

[minor] [accuracy] §7 table, Air waybill row; Current: "three original parts, for the carrier, the consignee and the consignor (Art. 7(1))"; Problem: Art. 7(1) gives the three parts. Art. 7(2) gives who gets each: the first is marked for the carrier, the second for the consignee, and the third is signed by the carrier and handed to the consignor. Fix: "three original parts: the first for the carrier, the second for the consignee, the third signed by the carrier and handed to the consignor (Art. 7(1)–(2))"; Basis: https://eur-lex.europa.eu/eli/convention/2001/539/oj/eng

[minor] [accuracy] §7 table, Air waybill row; Current: "for delay within 21 days (Art. 31(2))"; Problem: Art. 31(2) runs the 21 days from the date the cargo was placed at the person's disposal, a different start point from the 14 days "of receipt" for damage. Fix: "for delay within 21 days from the date the cargo was placed at the consignee's disposal (Art. 31(2))"; Basis: https://eur-lex.europa.eu/eli/convention/2001/539/oj/eng

[minor] [style] §4, first paragraph; Current: "1,933,299 US dry-van, long-haul (over 250 miles) truckload loads"; Problem: "dry-van" is used without a definition, here, in the figure caption and in Self-check 4, and no earlier unit defines it. The brief requires a definition on first use. Fix: "1,933,299 US dry-van (an enclosed, unrefrigerated trailer; course's working definition), long-haul (over 250 miles) truckload loads"; Basis: brief, Frame ("define each term on first use"); no source opened for the term.

[minor] [attribution] §5, first paragraph; Current: "([Gartner Peer Insights, TMS market, features updated April 2026](https://www.gartner.com/reviews/market/transportation-management-systems)) [analyst]"; Problem: SCE1 §10 question 2 says an analyst source gives how it was read and "the note that vendors license reprints". The unit gives neither here. Fix: "([Gartner Peer Insights, TMS market, features updated April 2026](https://www.gartner.com/reviews/market/transportation-management-systems), the public market page read in full; vendors license Gartner's reprints, SCE1 §8) [analyst]"; Basis: filed SCE1 §10; https://www.gartner.com/reviews/market/transportation-management-systems

[minor] [label] Deliverable A, row 2, Document; Current: "Carrier's rate in its portal; whether rates are contracted is not in the register"; Problem: the map's own assumption (intro to A, and case-facts "Added by units", SCE7 row) is "a contracted road carrier". Without saying so, the row reads as if it contradicts the assumption. Fix: "Carrier's rate in its portal; a contracted rate is this map's assumption (notes), not a register fact"; Basis: case-facts.md, Added by units, SCE7 Corvane row 2.

[minor] [style] Deliverable A, row 12, Document; Current: "Reservation on the CMR note; written claim (7)"; Problem: the pointer is wrong. Section 7's table says nothing about reservations or claims; they are in §6 steps 8 and 12 and in the glossary row "Reservation (CMR)". Fix: "Reservation on the CMR note; written claim (6, steps 8 and 12)"; Basis: unit §6 steps 8 and 12; §7 table.

[minor] [style] Deliverable B, row 12, Document; Current: "Reservation and written claim (7)"; Problem: the same wrong pointer as the finding above. Fix: "Reservation and written claim (6, steps 8 and 12)"; Basis: unit §6 steps 8 and 12.

[minor] [accuracy] §6 step 11; Current: "so a later amendment is not ruled out (SCE10 §5)"; Problem: SCE10 §5 says more than the pointer reports: "No act amending Article 3 was found by search on 28 November 2026", and the 2023 replacement proposal (COM(2023) 533) had not been adopted. Fix: "and SCE10 §5 found by search on 28 November 2026 no act amending Article 3, the Commission's 2023 proposal to replace the directive (COM(2023) 533) not yet adopted"; Basis: filed SCE10 §5.

[minor] [accuracy] §1, Private fleet; Current: "hauling property it owns, leases or holds, to further its business (§13102(15))"; Problem: the statute says the person is "the owner, lessee, or bailee" and the property moves "for sale, lease, rent, or bailment or to further a commercial enterprise". The unit's "holds … to further its business" narrows it. Fix: "transporting property of which it is the owner, lessee or bailee, for sale, lease, rent or bailment or to further a commercial enterprise (§13102(15))"; Basis: https://www.govinfo.gov/content/pkg/USCODE-2019-title49/html/USCODE-2019-title49-subtitleIV-partB-chap131-sec13102.htm

[minor] [accuracy] §2, LTL bullet; Current: "the class sets what an LTL shipment costs"; Problem: this stretches the source. NMFTA says that the denser and easier freight is to move, "the lower the class—and the lower the cost". The class is one input to price, not the price itself. Fix: "the class is an input to what an LTL shipment costs"; Basis: https://nmfta.org/standards/classification/

[minor] [accuracy] Deliverable D, glossary row Freight class; NMFC; Current: "The class (50 to 500) that sets an LTL shipment's price"; Problem: the same stretch as the finding above. Fix: "The class (50 to 500) that is an input to an LTL shipment's price"; Basis: https://nmfta.org/standards/classification/

Every Current string above was counted by script in unit.md: each occurs exactly once.

## Confirmed

- Acocella, Caplice & Sheffi (2020), TR Part E 142, 102073, title as listed. Confirmed figures: 1,933,299 loads; 71 shippers; Table 1 has 1,640 primary carriers (1,446 asset-based, 194 non-asset) and §4.1 says 1,650; 1 Sept 2015 to 30 May 2019; dry van, long haul over 250 miles; data from a managed services provider that is not a brokerage. Market phases: soft 15 Apr 2016 to 14 Apr 2017, tight 1 Oct 2017 to 30 Sep 2018. Average weekly PAR 81.9% and 68.5%; accepted cost per load $1,155.9 and $1,420.7; backup premium 1.009 and 1.182. Tight-market predictors: price against market, volume CV (negative), frequency (positive), destination dwell (negative), shipper size (negative). Tender lead time is not significant. Also confirmed: "goldfish"; low predictive power; no bid timing or contracted volume in the data; only the price binds; PAR and dwell definitions. Read at the author's copy: https://sheffi.mit.edu/sites/sheffi.mit.edu/files/2021-01/Acocella_Sheffi_Publication%202020.pdf
- Scott, Parker & Craighead (2017), Transportation Science 51(4), 1086–1101, doi 10.1287/trsc.2016.0677. The abstract confirms: no legally binding obligation to offer or accept a load; spot about 62% above contract; operational and economic factors drive rejection; the relationship deters it; primary and secondary carriers differ. No sample size in the abstract. https://ideas.repec.org/a/inm/ortrsc/v51y2017i4p1086-1101.html
- Sheffi (2004), Interfaces 34(4), 245–252, doi 10.1287/inte.1040.0075. Confirmed: TL truck dedicated to a single shipment; LTL and parcel consolidate; freight estimated "usually by compiling the prior year's movements"; lane as "a one-way movement from an origin to a destination"; single-round sealed bids, lane by lane; contracts of one to two years; empty repositioning; closed loop raises utilisation; "save three to 15 percent of transportation costs while maintaining or increasing their service levels" (in the introduction); savings hard to attribute; fewer than 10% of lanes in packages. "Routing guide" and "backhaul" are not in the paper, so the unit is right to credit them elsewhere. https://sheffi.mit.edu/sites/sheffi.mit.edu/files/2018-07/10_CombinatorialAuctionsInTheProcurementOfTransportationServices.pdf
- Laporte (2009), Transportation Science 43(4), 408–416, doi 10.1287/trsc.1090.0301. The abstract confirms the VRP was introduced 50 years earlier by Dantzig and Ramser "under the title 'The Truck Dispatching Problem'", with exact algorithms and heuristics. https://ideas.repec.org/a/inm/ortrsc/v43y2009i4p408-416.html ; https://www.gerad.ca/en/papers/G-2009-43
- Flodén, Bärthel & Sorkina (2010), in that author order, 12th WCTR Proceedings, from p. 29. The abstract confirms: 1990 to 2009; English and Scandinavian languages; interviews and surveys; modelling excluded; core factors cost, time, reliability and quality; price decides once basic requirements are met; low willingness to pay for the environment. No peer-review label. https://research.chalmers.se/en/publication/122890
- Gartner Peer Insights TMS market definition, "Updated April 2026". Definition quote and mandatory features confirmed (sourcing with bid management and optimisation; planning with consolidation, mode, route and carrier; execution as carrier communications; visibility from pickup to final delivery; settlement quote; analytics including on-time and cost by mode). Freight audit, tendering and rating are not named. https://www.gartner.com/reviews/market/transportation-management-systems
- 49 U.S.C. §13102 (2019 ed.): (2) broker, including the quoted words "arranging for, transportation by motor carrier for compensation"; (8) freight forwarder A–C; (14) motor carrier; (15) motor private carrier (with the narrowing finding above). https://www.govinfo.gov/content/pkg/USCODE-2019-title49/html/USCODE-2019-title49-subtitleIV-partB-chap131-sec13102.htm
- 49 U.S.C. §14706(a)(1) and (e)(1): receipt or bill of lading; actual loss or injury; failure to issue does not affect liability; minimum 9 months for a claim and 2 years to sue; current through Pub. L. 119-136. https://uscode.house.gov/us/usc/119-136/t49/s14706/
- 49 CFR Part 377, 10-1-09 edition. §377.203: credit period begins the day after presentation, 15 days by default, a tariff period not longer than 30 calendar days. §377.205: 7 days for prepaid (from receipt) and collect (from delivery), excluding Saturdays, Sundays and legal holidays; when credit is extended, the bill states late-payment penalties and the time by which payment must be made. https://www.govinfo.gov/content/pkg/CFR-2009-title49-vol5/pdf/CFR-2009-title49-vol5-part377.pdf
- CMR (1956): Arts. 1(1), 4, 5(1) (three originals; first to sender, second with goods, third to carrier), 6(1)(e), 9(1), 17(1), 23(3) (25 francs, gold franc), 30(1) (seven days excluding Sundays and public holidays; prima facie evidence), 32(1) (one year; three for wilful misconduct). https://treaties.un.org/doc/Treaties/1961/07/19610702%2001-56%20AM/Ch_XI_B_11.pdf
- 1978 CMR Protocol, Art. 2: 8.33 units of account per kilogram of gross weight short; the unit is the IMF's SDR; in force 28 Dec 1980; UNTS vol. 1208, No. 19487. https://treaties.un.org/doc/Publication/UNTS/Volume%201208/volume-1208-I-19487-English.pdf ; https://treaties.un.org/doc/Publication/MTDSG/Volume%20I/Chapter%20XI/XI-B-11-a.en.pdf
- Montreal Convention, OJ L 194, 18.7.2001, pp. 39–49: Art. 4 (air waybill or other record; cargo receipt on request), Art. 7 (three parts; see the air waybill findings), Art. 22(3) 17 SDR per kg, Art. 24 five-yearly review, Art. 31(2) 14 and 21 days (see the 21-day finding). https://eur-lex.europa.eu/eli/convention/2001/539/oj/eng
- ICAO 2024 revised limits: Art. 22(3) 26 SDR from 28 Dec 2024 (22 SDR from 2019). https://www.icao.int/sites/default/files/secretariat/legal/LEB%20Treaty%20Collection%20Documents/2024_Revised_Limits_of_Liability_Under_the_Montreal_Convention_of_1999_en.pdf
- GS1 EANCOM 2002 S3 IFTSTA: title; reference directory D.01B; reports transport status or a change in it between agreed parties, with exceptions and their reasons; the page does not say UN/EDIFACT. https://www.gs1.org/sites/gs1/files/docs/eancom/ean02s3/part2/iftsta/intro.htm
- TRADE/CEFACT/2001/33, 14 Feb 2001, "UN/EDIFACT Standard Directory D.01A and related documentation": lists IFTSTA with status UNSM. This closes F68's open point. https://digitallibrary.un.org/record/433163/files/%5EE_ECE_%5ETRADE_CEFACT_2001_33-EN.pdf
- X12 990, Response to a Load Tender, replying to the 204 Motor Carrier Load Tender. https://x12.org/node/4450
- FMCSA detention page, last updated 3 Oct 2025: detention defined; 1 in 10 stops; 1.4 h beyond the 2-hour standard; dwell 3.4 h; medium carriers 19% against large 9%; sample not stated; a 2018 OIG study is mentioned. https://www.fmcsa.dot.gov/research-and-analysis/impact-driver-detention-time-safety-and-operations
- Eurostat news, 10 Dec 2021: 2020 EU about 20%, national 24%, international 13%; Cyprus 44%, Belgium 6%; Malta exempt; no data for Italy and Romania; the comments on shorter domestic distances and Cyprus's port and construction traffic. https://ec.europa.eu/eurostat/web/products-eurostat-news/-/ddn-20211210-1
- Eurostat road_go metadata, last updated 22 July 2026: hire or reward; own account (manufacturing, construction, trade); "a sample of hauliers"; Reg. (EU) No 70/2012; vehicles below 3.5 t loading capacity excluded; tonne-km as weight × distance per goods operation. https://ec.europa.eu/eurostat/cache/metadata/en/road_go_esms.htm
- Eurostat Glossary for transport statistics, 5th ed., 2019: product page dated 25 July 2019, 744 definitions, Eurostat, UNECE and ITF. https://ec.europa.eu/eurostat/web/products-manuals-and-guidelines/-/ks-gq-19-004
- ATRI, 1 July 2025: "empty miles rose to an average of 16.7 percent", year not stated for that figure (the release's cost figure is for 2024); no sample. https://truckingresearch.org/2025/07/new-atri-report-shows-trucking-profitability-severly-squeezed-by-high-costs-low-rates/
- ATRI, 15 July 2026: industry-average cost to operate a truck in 2025 was $2.336 per mile; "deadhead mileage remained elevated", no share; no sample. https://truckingresearch.org/2026/07/new-atri-report-details-accelerating-costs-and-low-profitability-despite-cuts/
- CSCMP State of Logistics page: produced by Kearney, presented by Penske Logistics; released 16 June; $2.4 trillion and 7.8% of GDP, against $2.6 trillion and 8.7% "in 2025"; no year measured stated; no split. https://cscmp.org/CSCMP/Educate/State_of_Logistics_Report.aspx
- Kearney 2026 key takeaways: no logistics cost figure; it treats AI. https://www.kearney.com/documents/d/asset-library-291362522/2026-state-of-logistics-key-takeaways
- NMFTA classification: classes 50 to 500; density, handling, stowability, liability; reclassification charges. https://nmfta.org/standards/classification/
- FIATA: the forwarder "ensures that internationally traded goods move from point of origin to point of destination"; the 2004 services list. https://fiata.org/about-freight-forwarding/
- European Commission eFTI page: authorities must accept information via certified eFTI platforms; road, rail, inland waterway, air; applies in full 9 July 2027; undated. https://transport.ec.europa.eu/transport-themes/logistics-and-multimodal-transport/efti-regulation_en
- ECE/TRANS/2008/14, 13 Dec 2007: Secretariat note circulating the e-CMR additional protocol. https://digitallibrary.un.org/record/619052
- Directive 2011/7/EU Art. 3(3)(b)(i) and 3(5), as adopted: "Member States shall ensure"; 30 calendar days after receipt of the invoice; 60 calendar days unless expressly agreed and not grossly unfair. https://www.legislation.gov.uk/eudr/2011/7/article/3/adopted
- Pointers to filed units checked against their text:
  - SCE1 §2 (plan and tender; carry and track; settle), §3 TMS row and flag F6, §4 yard management, §5 logistics providers, the glossary rows (Shipper, Lane, Routing guide, Tender, Truckload, TMS, 3PL) and FAR 47.001 all hold.
  - SCE2 §3.2 (30-minute windows; appointment scheduling among basic WMS features; the second step of the flow map) holds.
  - SCE3 §7 (staging, loading, departure scan), §8 (Kim [practice]; missed cut-off as SCE3's working description), §12 (APQC perfect order uses on-time delivery), deliverable C row 6 (label re-keyed) and row 8 (ship, departure scan) hold.
  - SCE10 §7 (approved charge in the TMS, payment in the ERP; appointments at own doors in the WMS, requests at another party's dock in the TMS) and deliverable A row 15 hold.
  - SCE10 §5 is misreported (see the §6 step 11 finding).
- Internal pointers (sections 3, 4, 6 to 11, 13; steps by number) hold, except the two Deliverable row 12 pointers.
- Case facts: every Corvane, Ostrel, Tandric, Halvern and Varnby fact in the unit matches case-facts.md or the register's "Added by units" SCE1 and SCE7 rows. The placements marked "reading", "assumption" or "inference" are labelled as such.

## Could not verify

- The unit's source log (sources.md) was not in the packet. Part 8's check that every Sources entry is in the log, with its address, what was read and the date, could not be run.
- The writer's statements about its own searches, which cannot be checked from outside:
  - the "later Eurostat news items … opened give none" (superseded by the first finding);
  - "the excerpt of ATRI's 2026 report that this unit could read had no empty-mile figure" (the excerpt is not cited);
  - APQC's transport cost page returning an error;
  - Meixell & Norbis (2008) not opening;
  - Kearney's summary "covers AI" (confirmed), but whether the full report gives a split was not checked (it is sold).
- Which calendar year ATRI's 16.7% measures. The release does not say; the cost figures in the same release are for 2024.
- Whether 49 CFR §§377.203 and 377.205 read the same today. eCFR was not opened, and the unit says it did not check.
- Whether 49 U.S.C. §13102's definitions changed after the 2019 edition. Only the 2019 edition was read.
- Whether Directive 2011/7/EU Art. 3 has been amended. This checker relied on SCE10 §5, not on a consolidated text.
- Which states are party to the CMR, to the 1978 Protocol and to the e-CMR protocol. The unit says it did not check.
- What ECE/TRANS/2008/14 contains beyond its catalogue record. Only the record was opened, as in the unit.
- Gartner's TMS glossary entry (the §5 finding). Only SCE8 §1's citation of it was read.
- Bartholdi & Hackman (30-minute windows; appointment scheduling among basic WMS features) and Kim (2020), reached only through SCE2 and SCE3. The textbooks and paper were not opened.
- FAR 47.001, reached only through SCE1.
- Whether the Flodén et al. proceedings were peer-reviewed. The Chalmers record has no refereed label.
- The exact full wording of the Scott et al. and Laporte abstracts. The fetch tool returned segments and summaries.
- "Groupage", parcel pricing, ocean carriage and the ocean bill of lading, national European consignment notes, and intermodal definitions. The unit opened no source for these and says so; this checker opened none either. The ITF document returned by search was a meeting presentation, not the glossary.

## Passes

1. **References exist and match: PASS.** 29 Sources entries; 28 were opened, at the publisher's page, the issuing body's page or an index record (IDEAS, Chalmers, GERAD). Authors, title, journal, year, volume, pages and DOI match where given. The two ATRI titles match the releases; the 2025 URL's "severly" is ATRI's own. The NMFTA page title was not confirmed: the search listed the page as "What is Freight Class?", while the unit has "Classification - NMFTA". Not opened as a separate record: none. The Eurostat finding needs one new entry.
2. **Claims against sources: PASS with findings.** Every cited claim with a number, date, quotation or attribution was read against its source. Findings: one stale claim (the Eurostat empty share); stretches (Self-check 4, §1 private fleet, the two freight class lines); incomplete paraphrases (the air waybill rows); a misreported pointer (§6 step 11). Nothing invented. Nothing that could not be opened carries a claim, except the SCE2, SCE3 and SCE1 relays listed above.
3. **Grades against SCE1's key: PASS with one minor finding (the §5 Gartner reading note).**
   - Correctly graded: the treaty, statute and regulation texts and the X12, GS1 and UN/CEFACT standards text [independent]; the Acocella findings [independent] and its market descriptions [practice: description]; Scott [independent, abstract]; Sheffi, Flodén and Laporte [practice]; FMCSA, eFTI, ECE and ATRI [practice, F18]; CSCMP [practice]; Gartner [analyst]; Eurostat official statistics [independent], as the preamble states (F94 open).
   - Abstract-only readings are said to be so: Flodén, Scott, Laporte.
   - No vendor statement is used.
4. **Vendors: PASS.**
   - No software vendor is named, assessed, ranked, compared, recommended or mapped. The Gartner Peer Insights page lists vendors, and the unit names none of them.
   - Kearney and Penske Logistics, a real logistics provider, are named only as producer and presenter of CSCMP's report, as CSCMP's page states. Whether the vendor rule covers service providers is flag F72, still open.
   - No private company's unpublished figure appears.
   - Halvern and Varnby are labelled fictional, placed only by register facts, and "say nothing about any real product".
5. **The case: PASS.** Every case fact matches case-facts.md, including the SCE7 rows of "Added by units". Each operation is labelled "(fictional)" on first use: Tandric §1, Ostrel §1, Corvane §6 step 3, Halvern and Varnby §5. The case is never used as evidence. One minor wording point (Deliverable A, row 2).
6. **Scope and tone: PASS with one minor finding (dry-van).**
   - AI appears once, as the one-sentence note on Kearney's summary.
   - No interview framing, no craft method, nothing about the Project's owner or his employer (term scan clean).
   - Terms are defined on first use, except "dry-van". EDI is defined in SCE6, which the reader has read before this unit.
   - No "not X but Y" constructions found.
   - Legal points are put as questions for counsel or the regulator.
7. **Deliverable and figures: FIX on one figure.**
   - The deliverable meets the brief's wording. Six columns (step, party, document, system touchpoint, common failure, measure); built in full for a Corvane store delivery (A) and a Tandric client load (B); then a template (C) whose blanks each say what goes in them; glossary lines (D).
   - "On a site visit" and "Self-check" (8 questions) are present. The Self-check answers agree with the body, except the overstatement in Self-check 4.
   - Figure 1, decision, §3: PASS. Labels traced to §3, and to the glossary's "backups in order, with their prices". The caption names the section and sources. The kind fits a rule with branches.
   - Figure 2, compare, §4: PASS. 81.9 and 68.5 and the phase dates appear in §4. The caption gives the source and sample.
   - Figure 3, swimlanes, §6: FIX ("BOL" is not in the text). Every other note is traced to §§3, 6 and 7. The caption names the sections and sources. The kind fits a journey across actors.
   - Figure 4, compare, §13: PASS. 24, 20 and 13 appear in §13. The caption names the source, its exclusions and the metadata date. It stays correct as a 2020 figure after the Eurostat finding.
   - Brief coverage: every item the brief names is covered.
     - Thin by the unit's own statement: ocean carriage, parcel and intermodal pricing, "groupage", European payment practice beyond the directive, and transport measures from an association (F73, F77, F78, F90, F92 open).
     - The step-by-step lifecycle rests largely on the course's working description, because no transport textbook was read (F124).
     - National logistics cost figures are taken from CSCMP's own page, dated by release, with the year measured said to be unstated (F70).
   - Part 8, line by line:
     - Every line passes except these: the source-log line (not checkable here); the grade-key line, with one minor (the §5 Gartner reading note); the search-flag line, which does not apply because search is off (F65 proposes on); and the "every analyst list, market figure and filing figure carries the date it was read" line, which also does not apply. The unit still dates its CSCMP, ATRI and Gartner figures.
     - private_terms.py could not be run here; a manual scan was clean.
   - As the brief's reader would read it: dense but navigable on a phone. The §6 step 7 parenthesis on IFTSTA's directories is hard to parse, but it is accurate.

Verdict: SCE7 · fix · 1 error, 2 should-fix, 13 minor

References opened: 28 of the 29 in Sources, plus 1 new one (Eurostat Statistics Explained, journey characteristics). References not opened: none of the Sources entries was refused. Gartner's TMS glossary entry was not opened; it is cited in the unit only through the §5 finding's proposed text.
