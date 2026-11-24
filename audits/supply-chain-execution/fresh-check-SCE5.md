---
audit: fresh check
unit: SCE5 · The floor: people, devices and machines
course: supply-chain-execution · Supply Chain Execution for Product Teams
model: claude-opus-5-5
date: 2026-11-24
chat: https://claude.ai/code/session_01KMmgQyoX6Hnru9aiNiXdBA
verdict: fix · 2 errors, 8 should-fix, 5 minor
---

The checker's final report, verbatim, from its hand-back. Saved before any finding was applied.

Verdict: SCE5 · fix · 2 error, 7 should-fix, 5 minor

Model: claude-opus-5-5. Fresh check in an isolated agent context, with live search; this agent did not see the unit written. No cited reference was found not to exist, so the row is not stopped. (The agent's write of this report was refused; the main chat saved the returned text verbatim.)

## Findings

[error] [accuracy] §1.1 Pace and conditions; Current: "warehousing and storage recorded 4.4 nonfatal injury and illness cases per 100 full-time equivalent workers in 2025, down from 4.6 in 2024, against 2.3 for private industry as a whole"; Problem: the release's 4.4 (and 4.6 for 2024) is warehousing and storage's injury-only rate ("The rate of injuries fell to 4.4 cases per 100 FTE workers, down from 4.6 in 2024"). Private industry's 2.3 is total recordable cases (injuries and illnesses). The unit calls the injury-only rate an injury-and-illness rate and compares it with a different measure. BLS Industries at a Glance gives warehousing's 2025 total recordable rate (injuries and illnesses) as 4.5 (unsure item 4); Fix: "warehousing and storage recorded 4.5 injury and illness cases (total recordable cases) per 100 full-time workers in 2025 ([BLS, Industries at a Glance, NAICS 493](https://www.bls.gov/iag/tgs/iag493.htm), data extracted 20 Nov 2026), against 2.3 total recordable cases per 100 full-time equivalent workers for private industry as a whole; the release gives warehousing's injury-only rate as 4.4, down from 4.6 in 2024"; Basis: https://www.bls.gov/news.release/archives/osh_11182026.htm ; https://www.bls.gov/news.release/osh.htm ; https://www.bls.gov/iag/tgs/iag493.htm

[error] [accuracy] §4 findings paragraph; Current: "In the working paper's means, parallel pickers picked 53.9 order lines under competition against 46.84 under cooperation, a 15.2% gain; zone pickers picked 47.58 under cooperation against 35.37 under competition, a 34.3% gain; dynamic zone showed "hardly any differences""; Problem: the six values are the model's least-squares means of error-free order lines. They are not order lines picked: the raw means in Table 6 differ (54.56/45.94; 45.21/33.91). 15.2% and 34.3% are the paper's index scores (Tables 10 and 11), not the ratios of these means, which give 15.1% and 34.5%. The figure's dynamic-zone values 41.03 and 43.91 appear nowhere in the text (figure rule: error); Fix: "In the working paper's model estimates (least-squares means of error-free order lines per participant), parallel pickers reached 53.9 under competition against 46.84 under cooperation, which the paper indexes as a 15.2% gain; zone pickers reached 47.58 under cooperation against 35.37 under competition, indexed as a 34.3% gain; dynamic zone reached 41.03 under competition against 43.91 under cooperation, "hardly any differences""; Basis: https://repub.eur.nl/pub/78365/ERS-2015-009-LIS.pdf (Table 6 and its least-squares means; Tables 10 and 11)

[should-fix] [figure] §2 figure 1; Current: "{"kind": "compare", "title": "Nonfatal injury and illness cases per 100 FTE workers, US, 2025", "unit": "", "max": 5, "rows": [{"label": "Warehousing and storage", "value": 4.4}, {"label": "Private industry, all", "value": 2.3}], "caption": "Section 1.1 of this unit. Data: US Bureau of Labor Statistics, Employer-Reported Workplace Injuries and Illnesses – 2025, news release of 18 November 2026 (Survey of Occupational Injuries and Illnesses). US only."}"; Problem: follows from the first error. The figure sets an injury-only rate against a total recordable rate under an injury-and-illness title; Fix: "{"kind": "compare", "title": "Total recordable injury and illness cases per 100 full-time workers, US, 2025", "unit": "", "max": 5, "rows": [{"label": "Warehousing and storage", "value": 4.5}, {"label": "Private industry, all", "value": 2.3}], "caption": "Section 1.1 of this unit. Data: US Bureau of Labor Statistics, Survey of Occupational Injuries and Illnesses: warehousing and storage from Industries at a Glance, NAICS 493 (data extracted 20 November 2026); private industry from the news release of 18 November 2026. US only."}"; Basis: https://www.bls.gov/iag/tgs/iag493.htm ; https://www.bls.gov/news.release/osh.htm

[should-fix] [figure] §4 figure 2 title; Current: "{"kind": "bars", "title": "Order lines picked in the recorded run, by method and incentive""; Problem: the values are least-squares means of error-free order lines (second error); Fix: "{"kind": "bars", "title": "Error-free order lines in the recorded run, by method and incentive (model means)""; Basis: https://repub.eur.nl/pub/78365/ERS-2015-009-LIS.pdf

[should-fix] [figure] §4 figure 2 caption; Current: ""decimals": 2, "caption": "Section 4 of this unit. Mean order lines per participant in a 10-minute recorded run,"; Problem: same as the title; Fix: ""decimals": 2, "caption": "Section 4 of this unit. Least-squares means of error-free order lines per participant in a 10-minute recorded run,"; Basis: same

[should-fix] [label] §4 findings paragraph; Current: "and "No effects on order picking quality were identified" (2016, abstract) [independent]."; Problem: the unit takes its numbers from the 2015 working paper but follows the published abstract on quality, and does not say the two versions differ. The working paper reports error rates that differ by condition and calls its quality findings exploratory (notes, contradiction 3; unsure item 2). A reader who checks the cited working paper meets the conflict without warning; Fix: "and "No effects on order picking quality were identified" (2016, abstract) [independent]. The 2015 working paper, from which the numbers below come, reported error rates that differed by condition (zone picking: 19.1% of orders with an error under competition, 31.6% under cooperation) and called its quality findings exploratory; whether the published full text keeps them was not checked."; Basis: https://repub.eur.nl/pub/78365/ERS-2015-009-LIS.pdf ; https://repub.eur.nl/pub/96216

[should-fix] [accuracy] §1.3; Current: "(GAO-24-106889, June 2024 exposure draft, para. 10.04) [independent, for what the text says]."; Problem: the draft has been superseded and the unit does not say so. GAO issued the final 2025 Green Book (GAO-25-107721) on 15 May 2025, effective from fiscal year 2026, replacing the 2014 edition. The draft's text was confirmed: segregation of authorising, processing and recording, reviewing, and handling related assets; physical control over "cash, securities, inventories, and equipment"; Fix: "(GAO-24-106889, June 2024 exposure draft, para. 10.04) [independent, for what the text says]. GAO issued the final revision (GAO-25-107721) on 15 May 2025, effective from fiscal year 2026, superseding the 2014 edition ([GAO-25-107721](https://www.gao.gov/products/gao-25-107721), read 24 Nov 2026); whether para. 10.04 keeps this wording in the final text was not checked." (add GAO-25-107721 to Sources and the source log); Basis: https://www.gao.gov/products/gao-25-107721 ; https://www.gao.gov/assets/880/872514.pdf

[should-fix] [accuracy] §7 Where the line is drawn; Current: "the WMS holds the stock record and the orders (SCE1 §3)"; Problem: the pointer misstates SCE1 §3. SCE1 places the customer order in the order management system and gives the WMS "every customer order's pick lists and their progress"; Fix: "the WMS holds the stock record and each order's pick lists and progress, while the customer order itself sits in the order system (SCE1 §3)"; Basis: filed SCE1 §3 table

[should-fix] [deliverable] Card 3 row 9; Current: "answers to Marek and to finance for the record (SCE1 register)"; Problem: the register (SCE1 row) says only that Carla answers for the stock record at receiving and put-away. It names no reporting line to Marek or to finance. The card invents that line, attributes it to the register, and the notes do not list it as a case fact; Fix: "answers for the stock record (SCE1 register); reports to Marek [working]" (and add to the notes: "SCE5 · Corvane · Carla reports to Marek (card 3; working placement)"); Basis: case-facts.md, Added by units, SCE1 row on Carla

[should-fix] [deliverable] Card 5 row 9; Current: "| 9 | Hands to and depends on | Answers to Edda, vice-president, supply chain [register] |"; Problem: the line is tagged register, but the register does not say who the site manager reports to. The writer's own notes (case fact 9) call it a working placement; Fix: "| 9 | Hands to and depends on | Answers to Edda, vice-president, supply chain [working; the register does not say who the site manager reports to] |"; Basis: case-facts.md; notes.md case fact 9

[minor] [accuracy] §4 design; Current: "Each team had a 10-minute practice run and a 10-minute recorded run"; Problem: the working paper gives the runs per participant, on the same orders; Fix: "Each participant had a 10-minute practice run and a 10-minute recorded run on the same orders"; Basis: https://repub.eur.nl/pub/78365/ERS-2015-009-LIS.pdf

[minor] [style] Self-check 1; Current: "there was a clear lack of attention to human factors (section 3; abstract)"; Problem: the "management-oriented efficiency criteria" finding is stated in the unit's introduction. Section 3 restates only the gap; Fix: "there was a clear lack of attention to human factors (introduction and section 3; abstract)"; Basis: unit lines 14 and 96

[minor] [deliverable] Card 2 row 9; Current: "hands staged cages to loading and to Nuno, dispatcher [register]"; Problem: the register says Nuno handles the day's calls from drivers and customers. It records no handoff of cages to him; Fix: "hands staged cages to loading [register, SCE3 register note]; tells Nuno, dispatcher, of shorts and substitutes [working]"; Basis: case-facts.md, Ostrel Foods people; SCE3 register rows

[minor] [deliverable] Card 5 row 5; Current: "prepare the replacement of a warehouse system near end of vendor support [register]"; Problem: one [register] tag covers working placements. The register gives the system's state and Edda as sponsor. Marek's tasks (staffing peak, setting standards, approving workarounds, preparing the replacement) are working placements; Fix: "prepare the replacement of a warehouse system near end of vendor support [register for the system and the decision; Marek's tasks working]"; Basis: case-facts.md, Corvane

[minor] [attribution] §5 What vendors say; Current: "quotes Peter Schnorbach saying"; Problem: the page names him as senior director of product management at Manhattan Associates. Without that, the reader cannot see that the quote comes from the vendor's own staff; Fix: "quotes Peter Schnorbach, senior director of product management at Manhattan Associates, saying"; Basis: https://www.manh.com/our-insights/resources/articles/key-attributes-robust-gamification-program-in-labor-management

All 14 Current strings were verified to occur exactly once in unit.md.

## Confirmed

- BLS Industries at a Glance, NAICS 493: 1,839.2 thousand, Oct 2026 (p), seasonally adjusted; 2025 occupations 457,740 / 433,060 / 286,750; data extracted 20 Nov 2026. PASS. https://www.bls.gov/iag/tgs/iag493.htm
- BLS release of 18 Nov 2026: private-industry TRC rate 2.3; the release states no sample size. PASS. https://www.bls.gov/news.release/osh.htm
- de Vries et al. 2015: 142 participants in 48 teams; 28/39/75; bonus to the top four individuals; bonus to the best team. PASS. https://repub.eur.nl/pub/78365/ERS-2015-009-LIS.pdf
- de Vries et al. 2016, POMS 25(8) 1363–1376: warehouse erected for picking research; results by method; strongest for promotion-focused pickers; prevention focus in zone picking; "No effects on order picking quality were identified". PASS. https://repub.eur.nl/pub/96216
- de Vries et al. 2016, IJPR 54(8) 2260–2274: 101 participants; voice "performs better than RF-terminal picking"; Neuroticism, Extraversion, Conscientiousness and age; "without sacrificing quality". PASS. https://econpapers.repec.org/RePEc:taf:tprsxx:v:54:y:2016:i:8:p:2260-2274
- Grosse, Glock & Neumann 2017, IJPR 55(5) 1260–1276: "one of the most labour- and time-intensive processes"; "management-oriented efficiency criteria". PASS, but "a clear lack of attention" was not seen verbatim in the record. https://econpapers.repec.org/RePEc:taf:tprsxx:v:55:y:2017:i:5:p:1260-1276
- Grosse & Glock 2013, JMTM 24(6) 850–872: household-products manufacturer; "learning occurs in order picking"; two models gave unrealistic results. PASS. https://d2pnhgckm19p0r.cloudfront.net/insight/content/doi/10.1108/JMTM-03-2012-0036/full/html
- Bartholdi & Eisenstein, 1 Aug 1996, no venue: pick rates over 30% above previous averages, sustained; 50% to 200% of work standard; "persuade workers"; fifteen minutes and half an hour; temporary workers; "no changes to a typical warehouse management system"; over 50% within a day. PASS. https://www2.isye.gatech.edu/~jjb/bucket-brigades/papers/bbwh.pdf
- Bartholdi & Hackman, release 0.98, ch. 11: the rule; "sputter"; §11.2 over 30% with no change to layout, equipment or control system; music distributor about 20%, variance down about 90%; Fig. 11.6 expressed as a fraction of the work standard. PASS. https://www2.isye.gatech.edu/~jjb/wh/book/editions/wh-sci-0.98.pdf
- Fragapane et al. 2021, EJOR 294(2) 405–426: AGV central unit; AMRs "communicate and negotiate independently". PASS. https://econpapers.repec.org/RePEc:eee:ejores:v:294:y:2021:i:2:p:405-426
- Azadeh et al. 2019, Transportation Science 53(4) 917–945: the systems reviewed; "hardly been studied"; decisions to reconsider. PASS. https://econpapers.repec.org/RePEc:inm:ortrsc:v:53:y:2019:i:4:p:917-945
- Bahr et al. 2021: DOI and online date 25 Feb 2021; no volume shown. PASS on the citation. https://research.aston.ac.uk/en/publications/gamification-of-warehousing-exploring-perspectives-of-warehouse-m/
- Putz et al. 2019: 17 full-time pickers; an Austrian shipping company; March–May 2018; vignettes; individual and group feedback rated about alike. PASS. https://ceur-ws.org/Vol-2359/paper14.pdf
- Scriven (Interact Analysis), 22 Feb 2023: WCS and WES definitions; "sit above the WCS"; "most eWES solutions are truly 'embedded' into the WMS"; standalone versions. PASS on content, read in the same article (ID 22724398) on Food Logistics: https://www.foodlogistics.com/warehousing/automation/article/22724398/interact-analysis-warehouse-execution-systems-vs-warehouse-control-systems
- Gartner WMS definition: lists task interleaving, wave planning, labor management, yard management and automated materials handling equipment interfaces. PASS on the text. https://gcom.pdo.aws.gartner.com/en/information-technology/glossary/warehouse-management-system-wms
- Infios: "uses game mechanics and rewards/recognition tools to digitally engage employees"; leaderboards, badges, points, rewards or challenges; "up to 7%" with no basis; undated, © 2026. PASS. https://www.infios.com/en/supply-chain-solutions/gamification/what-is-gamification
- Banker, 3 June 2021: the engineered-standards quote; Schnorbach's "has no gamification" and "tend to fall short". PASS. https://www.manh.com/our-insights/resources/articles/key-attributes-robust-gamification-program-in-labor-management
- ISO 6780:2003: edition 2, published 2003-12, last reviewed and confirmed 2026. PASS. https://www.iso.org/standard/30524.html
- GAO-24-106889: June 2024 exposure draft; OV2.01 and OV4.17; para. 10.04 on segregation of duties and physical control. PASS, but superseded (see finding). https://www.gao.gov/assets/880/872514.pdf
- Census arithmetic: 7,975 / 23,883 = 0.334; 23,883 − 7,975 − 4,388 = 11,520. PASS. The figures themselves were not checked.

## The seven passes

1. **References exist and match.** Every reference opened matches its record: de Vries ×3, Grosse ×2, Fragapane, Azadeh, Bahr, Putz, Bartholdi & Eisenstein, Bartholdi & Hackman, ISO, BLS ×2, GAO, Infios, Banker, Scriven. None is non-existent. The GAO draft is superseded (should-fix). Not checked: Scriven's sdcexec.com address, which no search returned (content confirmed at Food Logistics); FRED; the Census methodology page.
2. **Claims against sources.** Two FAILs: the BLS rate's measure, and the de Vries means described as order lines picked. Every other claim opened PASSes.
3. **Grades.** These follow SCE1 §10. Abstract-only readings are said to be abstract-only, and the vendor pages are graded vendor-reported. Scriven is graded analyst as a signed article, and the unit says it is not a report. Grading government statistics and a draft standard as independent falls outside SCE1's key as written (writer's Need 1, F8). That is a gap in SCE1, not an error in this unit.
4. **Vendors.** PASS. Two real vendors are named, each only to attribute its public statements, graded vendor-reported, one sentence each. There is no assessment, ranking or mapping. The 1996 paper names a real customer; the unit does not repeat the name. There is no private figure. Halvern and Kestrow are labelled (fictional), and neither is tied to a real company.
5. **The case.** Each operation is labelled (fictional) on first use, and the case is never used as evidence. Facts agree with case-facts.md except card 3 row 9 (an invented reporting line) and card 5 row 9 (a working placement tagged register). Cards 2 and 5 have minor tagging problems.
6. **Scope and tone.** PASS. There is no AI treatment, no interview framing, no method teaching, and nothing about the Project's owner. Legal points are put as questions to a named body. Terms are defined on first use. No "not X but Y" construction was found.
7. **Deliverable and figures.** The deliverable is complete: the form; five cards in full for named Corvane and Ostrel staff; the template, each blank saying what goes in it; glossary lines. "On a site visit" and "Self-check" are present and agree with the body (Self-check 1's pointer is a minor finding). Figures, per audit-units §3(7):
   - **Fig 1** (compare, §2): FIX. Measure mismatch; replacement given.
   - **Fig 2** (grouped bars, §4): FIX. Title and caption; 41.03 and 43.91 were missing from the text, which the second error's fix supplies.
   - **Fig 3** (flow, §7): PASS. Labels trace to §7, the kind fits a sequence, and the caption names the sources.
   - **Fig 4** (compare, §8): PASS. 7,975, 4,388, 11,520 and 23,883 are all in §8, and the caption says the third bar is a subtraction.

## Part 8, line by line

- **Sourced where made:** yes.
- **Acceptable source types:** yes; the Scriven article is accepted with its label.
- **No banned source types:** yes.
- **Grades per SCE1:** yes, with the F8 gap noted under pass 3.
- **Analyst read mode stated:** yes.
- **No vendor assessed or mapped:** yes.
- **Real-vendor naming rule:** yes.
- **Fictional vendors only in worked examples:** yes.
- **Peer-review sites:** none used.
- **Number says whose figure, sample and year:** mostly yes. The BLS release gives no sample size and the unit says so; the measure problem is the first error.
- **Study sample, setting and design; inferences labelled:** yes.
- **Common claims C3, C5, C6 set against evidence:** yes.
- **Every reference in the source log:** yes, all 21.
- **Sources match their records:** yes, for those opened.
- **Case labelled and consistent:** yes, except the card findings.
- **Nothing about the owner:** yes. private_terms.py was not run by this checker.
- **No AI, interview framing or method:** yes.
- **Current facts dated:** yes.
- **Deliverable in full, then as template:** yes.
- **Site visit and Self-check present and agreeing:** yes.
- **Not advice without evidence:** yes; the requests in card field 8 are marked working.
- **Links as links, DOI for papers:** yes.

**As the brief's reader.** The reader is a product person with no operations background who checks citations. The unit is clear and states its limits plainly. A reader checking citations would stumble in two places: the BLS measure and the de Vries numbers. Both are fixed above.

## Also checked

- **F5.** WCS and WES are sourced to Scriven [analyst], and no standards-body or peer-reviewed definition was found. The writer's proposed SCE1 §3 and glossary corrections match SCE1's text.
- **F24.** The ISO sizes are right. The unit makes no claim about regional dominance because Annex A was not read; acceptable.
- **F39.** W2 was not checked; the writer's proposal to close it as "not checked" stands.
- **F44, SCE5 parts.**
  - Bucket brigades: done; figures confirmed.
  - de Vries incentives: done, but the means need fixing (second error).
  - Cost of goods-to-person equipment: no figure, correctly stated as none.
  - Adjustment approval: rests on the GAO draft by inference; cite the final revision as well.
- **F2 and F8.**
  - F2: SCE1 §11 rows C3, C5 and C6 read "Not searched here". The writer's proposed replacements agree with SCE5 §§3, 5 and 8.
  - F8: the grade-key gap for government statistics and draft standards is real.
- **Contradictions with filed units.**
  - SCE1 §3: the WMS/orders pointer is wrong (should-fix finding).
  - SCE1 §11, C6: it takes the de Vries quality result from the abstract. SCE5 does the same, and the working-paper conflict should be disclosed (should-fix finding).
  - SCE3 §3.4 cites Bartholdi & Hackman on the music distributor; SCE5 states both sources consistently.
  - Pointers checked and correct: SCE4 §§4, 5, 9 and 10; SCE3 §§2, 3.5, 3.7, 8, 9 and 12 and deliverable C; the SCE2 register rows on Bram and Mina.
- **Internal section pointers.** All match their sections except Self-check 1 (minor finding).

## Body length

About 4,810 words, from the title to the end of Self-check. This excludes figure JSON and the deliverable but counts headings and the claims table. The Sources list (about 570 words) is excluded; the deliverable is about 2,000 words. Within 2,000 to 6,000.

## Could not verify

- **Census Service Annual Survey via FRED:** the 2012 figures and the discontinuation of the total-expense series. The fetches were refused or interrupted; not checked and not retried. The Census methodology page was not checked either. A FRED series for employers' cost of fringe benefits (EXPECFEF493ALLEST) exists by its search-result title. That supports "payroll excludes benefits", but the series was not opened.
- **Scriven at sdcexec.com:** no search returned the address. The content was confirmed at the Food Logistics copy of the same article.
- **Gartner glossary:** the gcom.pdo.aws.gartner.com page does not identify itself as Gartner's IT Glossary, so unsure item 6 stands.
- **"hardly any differences":** the 2015 working paper's phrase for dynamic zone picking was not seen verbatim.
- **Bahr et al. details:** §2.4 and the counts (47 articles, five on the theme, eight managers) were not re-read; the record page shows no counts. Bräuer and Mazarakis are known only as Bahr et al. report them.
- **Azadeh et al.:** "little space" and "around the clock" are not in the record read.
- **GAO-25-107721:** the final text of para. 10.04 was not opened.

Verdict: fix, with 2 errors, 7 should-fix and 5 minor. No reference fails to exist and no rewrite is needed. The errors are the BLS injury rate (an injury-only 4.4 compared with a total recordable 2.3; IAG gives 4.5) and the de Vries numbers (they are model means of error-free order lines). The figure and GAO findings follow from those or are stale. The rest are case-register tags and pointers.
