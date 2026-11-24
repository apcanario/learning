claude-opus-5-5

Verdict: SCE5 · fix · 0 error, 4 should-fix, 14 minor

## Findings

[should-fix] [coverage] after Deliverable D, before Sources; Current: "## Sources"; Problem: The brief says "a fact the unit invents about them is listed in the notes so that it can be added to the register". SCE2 to SCE4 each have "## Notes: facts for the case register". SCE5 has no notes section, but its cards add facts that are not in case-facts.md: Carla reports to Marek; Marek answers to Edda; Ilse tells Nuno of shorts and substitutes; the devices used by Ilse, Carla, Sofia and Marek; Sofia's route list serves as the warehouse's release plan and her routes go to Nuno; Sofia's measures and desk hours; routes are changed after picking has begun; Marek's tasks. Fix: "## Notes: facts for the case register\n\nWorking descriptions in deliverable B, not in case-facts.md; each is this unit's assumption.\n\n- Corvane: Mina confirms picks with a handheld scanner showing a sequence of locations (card 1; from SCE3 deliverable C).\n- Corvane: Carla uses a desktop for reports and adjustments and a handheld for counts, and reports to Marek (card 3).\n- Corvane: Marek, site manager, answers to Edda; he staffs the peak, sets standards and any bonus scheme, approves workarounds and prepares the warehouse-system replacement (card 5).\n- Ostrel Foods: Ilse's pickers use handhelds or voice; Ilse watches the route backlog on a desktop or handheld and tells Nuno of shorts and substitutes (card 2).\n- Ostrel Foods: Sofia's route list is the warehouse's release plan; she works at a desk between the cut-off and the evening start, on the routing tool and the ERP, is measured on routes built by the time picking starts and vehicles used, and hands routes to Ilse's team and to Nuno; routes are sometimes changed after picking has begun (card 4).\n\n## Sources"; Basis: brief, "a fact the unit invents about them is listed in the notes so that it can be added to the register"; case-facts.md (these rows are absent).

[should-fix] [coverage] end of unit; Current: "para. 10.04 read in a copy at https://www.thompsongrants.com/sites/grants/files/advisory_files/gao-25-107721.pdf)"; Problem: The unit has no unsure list. SCE1 to SCE4 each end with one, audit-units §3 starts from it, and the applier adds the fresh-check line under it. Flag F39 is also not dealt with anywhere: the unit never mentions W2 (Gu, Goetschalckx & McGinnis 2007). This checker ran a fresh search on 24 Nov 2026. It returned only index records (RePEc, IDEAS) and the DOI address, which redirects to Elsevier's linking hub. No open copy was found. Fix: "para. 10.04 read in a copy at https://www.thompsongrants.com/sites/grants/files/advisory_files/gao-25-107721.pdf)\n\n## Unsure list\n\n- Seed W2 (Gu, Goetschalckx & McGinnis 2007, EJOR 177(1) 1–21, https://doi.org/10.1016/j.ejor.2006.02.025): a fresh search on 24 Nov 2026 returned only index records and the DOI address, which redirects to Elsevier's linking hub; not checked; no open copy found by SCE2, SCE3, SCE4 or SCE5 (flag F39 closes for W2).\n- Regional use of the ISO 6780 pallet sizes (Annex A) was not read; flag F24 stays open for regional pallet sizes.\n- Abstract-only: Grosse et al. (2017), Grosse & Glock (2013), de Vries et al. (2016, IJPR and POMS), Azadeh et al. (2019), Fragapane et al. (2021).\n- Not opened: the GAO exposure draft's paragraphs OV2.01 and OV4.17 in the final text; the Census Service Annual Survey's other expense lines; Bräuer and Mazarakis (reported through Bahr et al.); W6's full text."; Basis: audit-units-SKILL.md §3; flags.txt F39; https://www.doi.org/10.1016/J.EJOR.2006.02.025 (redirected, not opened).

[should-fix] [accuracy] section 8, What was opened; Current: "Payroll excludes employers' benefit costs, and the other detail lines (rent, depreciation, benefits, and the rest, $11,520 million together by subtraction) were not opened, so whether payroll is the largest single line is not shown."; Problem: The benefits line is published in the same FRED family and opens: Employer's Cost for Fringe Benefits, NAICS 493, employer firms, 2012 = $1,895 million. C3 is a claim about labour, so leaving benefits unopened understates the labour share the evidence shows. Fix: "Payroll excludes employers' benefit costs, which the same survey put at $1,895 million in 2012 ([FRED, EXPECFEF493ALLEST](https://fred.stlouisfed.org/data/EXPECFEF493ALLEST)) [independent]; payroll and benefits together were about 41% of total expense (this unit's arithmetic: 9,870 / 23,883). The other detail lines (rent, depreciation and the rest, $9,625 million together by subtraction) were not opened, so whether labour is the largest single line is not shown."; Basis: https://fred.stlouisfed.org/data/EXPECFEF493ALLEST (2012: 1,895, millions of dollars; series 2005–2022).

[should-fix] [accuracy] section 1.1, Measured on; Current: "Bartholdi and Eisenstein report that under zone picking at one chain retailer's distribution centre individual pick rates ranged from 50% to 200% of work standard"; Problem: The paper says workers' pick rates "typically range from 50% to 200% of work standard". That is a general statement in its discussion of zone picking, not a range measured at the site. Fix: "Bartholdi and Eisenstein, describing zone picking at one chain retailer's distribution centre, write that individual workers' pick rates \"typically range from 50% to 200% of work standard\""; Basis: https://www2.isye.gatech.edu/~jjb/bucket-brigades/papers/bbwh.pdf

[minor] [figure] section 8 viz; Current: "{\"label\": \"Other lines, not opened (by subtraction)\", \"value\": 11520}"; Problem: Goes with the section 8 should-fix. Fix: "{\"label\": \"Employer's cost for fringe benefits\", \"value\": 1895}, {\"label\": \"Other lines, not opened (by subtraction)\", \"value\": 9625}"; Basis: FRED EXPECFEF493ALLEST.

[minor] [figure] section 8 viz caption; Current: "(series EXPEF493ALLEST, EXPGAPEF493ALLEST, EXPAOOEF493ALLEST)"; Problem: Goes with the section 8 should-fix. Fix: "(series EXPEF493ALLEST, EXPGAPEF493ALLEST, EXPECFEF493ALLEST, EXPAOOEF493ALLEST)"; Basis: FRED.

[minor] [accuracy] section 9 table, C3 row; Current: "US Census data, 2012: payroll about a third of warehousing firms' total expense; other lines not opened; no source ranks all lines (section 8)."; Problem: Goes with the section 8 should-fix. Fix: "US Census data, 2012: payroll about a third of warehousing firms' total expense, payroll with benefits about 41%; other lines not opened; no source ranks all lines (section 8)."; Basis: FRED.

[minor] [accuracy] Self-check 8; Current: "the other lines were not opened and benefits are excluded, so \"largest\" is not shown (section 8)"; Problem: Goes with the section 8 should-fix. Fix: "payroll with benefits was about 41%; the other lines were not opened, so \"largest\" is not shown (section 8)"; Basis: FRED.

[minor] [attribution] Sources, Census entry; Current: "EXPGAPEF493ALLEST.txt ; https://fred.stlouisfed.org/data/EXPAOOEF493ALLEST"; Problem: Goes with the section 8 should-fix: the new series must be listed. Fix: "EXPGAPEF493ALLEST.txt ; https://fred.stlouisfed.org/data/EXPECFEF493ALLEST ; https://fred.stlouisfed.org/data/EXPAOOEF493ALLEST"; Basis: FRED.

[minor] [accuracy] section 2, third bullet; Current: "the bucket-brigade rule was explained in about fifteen minutes"; Problem: The paper says "We described the idea to the workers in fifteen minutes". Fix: "the authors described the bucket-brigade rule to the workers in fifteen minutes"; Basis: bbwh.pdf.

[minor] [accuracy] section 2, third bullet; Current: "the authors also say temporary workers become productive more quickly under the method"; Problem: The source says temporary workers "can become productive more quickly". Fix: "the authors also say temporary workers \"can become productive more quickly\" under the method"; Basis: bbwh.pdf.

[minor] [attribution] section 4, Bucket brigades; Current: "Sequenced from slowest to fastest, the line rebalances itself; otherwise, in B&H's Theorem 11.1, it may \"sputter\" (§11.1) [practice]"; Problem: Theorem 11.1 is the convergence result for slowest-to-fastest sequencing. "Sputter" comes from §11.1's text on the other case. Fix: "Sequenced from slowest to fastest, the line rebalances itself (B&H Theorem 11.1); otherwise it may \"sputter\" (§11.1) [practice]"; Basis: https://www2.isye.gatech.edu/~jjb/wh/book/editions/wh-sci-0.98.pdf ch. 11.

[minor] [figure] section 7 viz; Current: "\"note\": \"timing and location of workflows; most embedded in the WMS\""; Problem: Scriven says WES that sit above the WCS are "embedded WES" and that most eWES are embedded in the WMS. The note says most WES are. Fix: "\"note\": \"timing and location of workflows; embedded WES sit above the WCS, most inside the WMS\""; Basis: https://www.foodlogistics.com/warehousing/automation/article/22724398/interact-analysis-warehouse-execution-systems-vs-warehouse-control-systems (same article, same ID as the SDCExec URL cited).

[minor] [attribution] Deliverable B, card 3 row 8; Current: "(section 1.3, GAO draft [independent], applied by inference)"; Problem: Para. 10.04 of the final GAO-25-107721 contains both passages (confirmed). Cite the standard in force, not the draft. Fix: "(section 1.3, GAO-25-107721 para. 10.04 [independent], applied by inference)"; Basis: https://www.thompsongrants.com/sites/grants/files/advisory_files/gao-25-107721.pdf para. 10.04.

[minor] [accuracy] section 5; Current: "they interviewed eight UK warehouse managers, each with at least four years' experience"; Problem: The paper says eight "warehousing managers", and its Table 3 includes a Head of Logistics. Fix: "they interviewed eight UK warehousing managers (one a head of logistics), each with at least four years' experience"; Basis: https://publications.aston.ac.uk/id/eprint/42403/1/gamification_2020_authors_revision_2_openaccess.pdf §3.2, Table 3.

[minor] [label] section 7, The terms; Current: "[analyst: a signed article by the firm's analyst, read in full; not a report]"; Problem: Part 8 lists "an analyst report by firm, title and date". A signed trade-magazine article does not match any listed kind exactly. The label is honest, but it should say why the source is used. Fix: "[analyst: a signed article by the firm's analyst in a trade magazine, read in full; not an analyst report, used because no listed kind of source defining either term was found]"; Basis: sourcing-standard.md Part 8, source kinds.

[minor] [attribution] Sources, Grosse & Glock; Current: "https://doi.org/10.1108/JMTM-03-2012-0036 (abstract)"; Problem: Every other abstract-only entry says where it was read. Fix: "https://doi.org/10.1108/JMTM-03-2012-0036 (abstract, read at the publisher's page)"; Basis: Part 8, source-log rule.

[minor] [style] section 3; Current: "Seed W6's full text"; Problem: "W6" is an internal seed code that no unit defines for the reader. Fix: "Grosse et al.'s full text"; Basis: brief (reader has no operations background, reads in order).

Every Current above was checked to occur exactly once in unit.md.

## Passes (audit-units §3)
(1) Coverage: PASS. Every item in the brief is covered:
- the five roles, each with measures, pace, conditions and what the person does when the system is wrong
- shifts, temporary staff and training, given only where a figure is sourced
- devices as working conditions, with what the research studied and what it did not
- standards, tracking and incentives, with samples
- gamification, graded vendor-reported
- conveyors and sorters, goods-to-person and mobile robots, from the reviews
- the WCS/WES line and where it is disputed

Thin but disclosed: the planner (the register has no warehouse planner, so a transport planner is used and the unit explains why), cold-store conditions, shift patterns. Missing: the notes section (finding 1).

(2) Accuracy: FIX. Findings 3, 4, 10, 11, 12, 15.

(3) Figures (whose number): PASS.

(4) Labels: PASS, with one minor finding (the Scriven grade wording). Labels for single-site, abstract-only, vendor and inference claims are all present. Bräuer & Mazarakis is graded by its origin, per F8(c). GAO is graded independent for what the text says, per F8(d).

(5) Deliverable: PASS.
- Form A fixes nine fields in order: Who, Measured on, Conditions, Device, Top tasks, What goes wrong, What they do about it, What they would ask of the software, Hands to/depends on. That covers the brief's seven fields plus two; these are the fields SCE8, SCE9, SCE11 and SCE13 will reuse.
- Five cards are built in full: Mina, Ilse, Carla, Sofia, Marek.
- Template C has the same nine fields, each blank saying what goes in it.
- Glossary lines are present.
- Every register-tagged line agrees with case-facts.md.

(6) Errata and pointers: PASS. No audit report applies. Pointers were checked against filed SCE1 to SCE4. SCE1's WCS/WES glossary line says "SCE5 sources both", and SCE5 does.

(7) Figures (viz):
- viz 1 (compare, injury rates): PASS.
- viz 2 (bars, incentives): PASS. All six values, 142 participants, 48 teams and the 10-minute runs are in §4.
- viz 3 (compare, C3): PASS as written; FIX only to go with finding 3.
- viz 4 (flow, WCS/WES): FIX (finding 13).

Body length: 5,020 words, counted from line 10 to line 199 (intro to Self-check) without the viz JSON; 5,389 words with it. The brief allows 2,000 to 6,000, so the body is within range.

## Flags
- **F5: dealt with.** WCS and WES are defined from Scriven (Interact Analysis, 22 Feb 2023), and the definitions were verified. The glossary lines replace SCE1's "not sourced". The unit says no peer-reviewed or standards-body definition was found.
- **F24: partly dealt with.** The six ISO 6780:2003 sizes were verified (clause 4.1, Tables 1 and 2; ISO's page says the standard was "last reviewed and confirmed in 2026"). Regional use is in Annex A, which was not read, so the unit makes no regional claim and says so. F24 stays open for regional use (finding 2).
- **F39: not dealt with in the unit.** This checker's search found no open copy of W2. Finding 2 records this and closes F39 for W2.
- **F44, SCE5 parts:**
  - Bucket brigades (B&H §11.2): verified.
  - de Vries 2016 on incentives by picking method: the working-paper numbers were verified.
  - Cost of goods-to-person equipment: the unit says no public figure was found.
  - Who counts and who approves an adjustment: handled through GAO para. 10.04 (both passages confirmed in the final text) as the unit's inference, with the question put to auditors.
- **F2:** C3, C5 and C6 are each stated as they circulate and set against what was opened, with "No independent source found" where none was.
- **F8:** the key's rules are followed.

## Confirmed (opened 24 Nov 2026)
- **Grosse, Glock & Neumann 2017:** the abstract quotes.
- **BLS NAICS 493:** 1,839.2 thousand in Oct 2026 (preliminary, seasonally adjusted); occupations 457,740, 433,060 and 286,750 (2025); total recordable case rate 4.5; data extracted 20 Nov 2026.
- **BLS release, 18 Nov 2026:** private-industry total recordable case rate 2.3 per 100 FTE; warehousing injury rate 4.4, down from 4.6; no sample stated.
- **Bartholdi & Eisenstein 1996:** "over 30%", "no changes to a typical warehouse management system", "persuade workers", "within a half-hour", "over 50% within a day".
- **B&H 0.98:** §3.3; Fig. 11.6 (rates as a fraction of the work standard, over 30%); §11.1 rule and "sputter"; §11.2 layout, equipment and control system unchanged; 20% and 90%; no one computes a balance.
- **de Vries 2016 IJPR abstract:** 101 participants; voice better than RF terminals; the quality quote.
- **de Vries 2016 POMS abstract:** all quoted phrases; 25(8) 1363–1376.
- **de Vries 2015 working paper:** 3×2 design; 142 participants in 48 teams; 28/39/75; top four; 10-minute practice and recorded runs; all six least-squares means; 15.2% and 34.3%; "Hardly any differences"; 19.1% and 31.6%; "more exploratory perspective".
- **Grosse & Glock 2013 abstract:** as summarised.
- **Bahr et al. 2021:** 47 articles screened (SCOPUS), "only five", eight managers with four years' experience, exploratory, generalisation impossible, §2.4.
- **Putz et al. 2019:** 17 full-time pickers, Austria, 2018.
- **Infios page:** "up to 7%", no basis given, © 2026.
- **Manhattan-site article:** Banker, 3 June 2021, and the Schnorbach quotes. The page says it originally appeared on Forbes.
- **ISO 6780:** the six sizes; confirmed 2026.
- **Azadeh 2019 and Fragapane 2021:** abstracts as summarised.
- **Scriven 2023:** all quotes.
- **Gartner glossary, WMS:** the capabilities as quoted.
- **FRED:** total expense 23,883 (2012, series discontinued); payroll 7,975.
- **GAO-25-107721:** May 2025, effective FY2026, supersedes GAO-14-704G; para. 10.04 holds both passages.

## Could not verify
- FRED "All other operating expenses" 2012 = $4,388 million: the fetch was refused. The $11,520 and $9,625 subtraction figures depend on it.
- The Census SAS methodology page ("probability sample") was not opened.
- That the three BLS occupations are the "largest" in NAICS 493: the values are confirmed, the ranking is not.
- de Vries 2016 IJPR: personality traits and age as predictors.
- de Vries 2015: "every team on the same set of orders, with order lines counted per participant".
- GAO-24-106889 exposure draft, OV2.01 and OV4.17: not opened. In the final text, nonfederal use is in OV4.20, and OV4.17 covers cost-benefit.
- The unit's source log (sources.md) is not in the packet, so the Part 8 source-log check could not be run.
- SCE3/SCE4 section contents used as cross-references: headings were checked, content only spot-checked.
