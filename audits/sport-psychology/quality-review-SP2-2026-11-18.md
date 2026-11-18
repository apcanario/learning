---
check: quality review of SP2 (rule 13), W-SP4, 18 Nov 2026
model: claude-opus-5-5 (stated by the agent: "Opus 5.5 (claude-opus-5-5)")
saved: by the main chat verbatim from the agent's reply (the harness refused the agent a report file)
---

Model: Opus 5.5 (claude-opus-5-5).

QUALITY REVIEW · SP2 · W-SP4 · 18 Nov 2026. I edited nothing and wrote no files. Unit read in full: files/SP2-the-developing-athlete-10-to-25.md. A script confirmed that every Current string below occurs exactly once.

Findings
[should-fix] [accuracy] §3; Current: "([Cobley et al., 2009, abstract read; not verified, because the DOI address later redirected](https://doi.org/10.2165/00007256-200939030-00005))"; Problem: the DOI address opened today. The abstract confirms every figure the unit gives: 38 studies from 1984 to 2007, 253 samples, 14 sports, 16 countries, effect sizes "small", largest in males aged 15 to 18 at the representative (regional and national) level, a call for research in female contexts, and "the first meta-analytical review". Fix: "([Cobley et al., 2009, abstract read](https://doi.org/10.2165/00007256-200939030-00005))"; Basis: https://www.doi.org/10.2165/00007256-200939030-00005
[should-fix] [label/grade] §3; Current: "in sport overall it rests on Cobley et al. (2009), which is not verified, so it carries no grade]"; Problem: with Cobley verified, the claim takes a grade on the same footing as Smith et al.: one meta-analysis in athletes, read in abstract, so rule 4. Fix: "in sport overall, moderate (Cobley et al., 2009: one meta-analysis in athletes, read in abstract, which calls the effects small and gives no pooled figure, rule 4)]"; Basis: as above.
[should-fix] [deliverable] Deliverable A, 10–12 "What to watch"; Current: "the same in sport overall (Cobley et al., 2009) is not verified;"; Problem: same as above. Fix: "moderate in sport overall (Cobley et al., 2009);"; Basis: as above.
[should-fix] [bibliography] Sources, Cobley; Current: "(abstract read at the DOI address, 17 Nov 2026; on a later attempt the DOI address redirected, so the abstract's content and the authors, volume, issue and pages are not verified)"; Problem: the DOI page shows S. Cobley, J. Baker, N. Wattie et al., 39(3):235–256. Fix: "(abstract read at the DOI address, 17 Nov 2026, and again by the quality review, 18 Nov 2026, which confirmed its content, the first three authors, volume, issue and pages)"; Basis: as above.
[minor] [bibliography] Sources, Boccia; Current: "its content not read; the article's authors, volume and issue are not verified)"; Problem: doi.org opened today and gives Boccia G, Moisè P, Franceschi A, Trova F, Panero D, La Torre A, et al., PLoS ONE 12(1):e0170744, 2017. Fix: "its content not read for this unit; the first six authors, volume, issue and article number confirmed at the DOI address by the quality review, 18 Nov 2026)"; Basis: https://doi.org/10.1371/journal.pone.0170744
[minor] [population] §5; Current: "40 adolescents aged 11 to 18 and 24 adults aged 20 to 38 (28 recruited, 4 excluded)"; Problem: the 20 to 38 range is for the 28 adults recruited, not the 24 analysed. Fix: "40 adolescents aged 11 to 18 and 24 adults (28 recruited, aged 20 to 38; 4 excluded)"; Basis: Haddad et al. 2014, https://www.frontiersin.org/articles/10.3389/fpsyg.2014.01476/pdf
[minor] [population] §9; Current: "\"accounted for only 1% of the variance in performance among elite-level performers\";"; Problem: the sample is not given. The full text bases the elite estimate on six effect sizes (N = 228). Fix: "\"accounted for only 1% of the variance in performance among elite-level performers\" (an estimate the full text bases on six effect sizes from 228 athletes);"; Basis: Macnamara et al. 2016, copy of the published PDF, https://hhs.purdue.edu/skill-learning-and-performance-lab/wp-content/uploads/sites/43/2024/08/macnamara-et-al-2016-the-relationship-between-deliberate-practice-and-performance-in-sports-a-meta-analysis.pdf
[minor] [source log] §9; Current: "The paper mentions 10,000 hours only in describing an earlier study of violinists, not as a finding of its own."; Problem: this claim rests on the full text, which was read on a non-publisher copy. The Sources entry says so; the text where the claim is made does not. Fix: "In its full text, read on a copy of the published PDF, not the publisher's page, the paper mentions 10,000 hours only in describing an earlier study of violinists."; Basis: same copy; I confirmed the wording.
[minor] [label] Deliverable A, 10–12; Current: "[weak; IOC consensus summary (Bergeron et al., 2015), rule 5]"; Problem: the unit's own unsure list (item 10) says the growth studies behind this claim are outside the athlete populations, and the claim is applied to under-12s, so SP1's key requires the inference label. Fix: "[weak; IOC consensus summary (Bergeron et al., 2015), rule 5; inference]"; Basis: SP1 §9.
[minor] [bibliography] Sources, Bergeron; Current: "2015;49(13):843–851 (last page not verified)."; Problem: the statement prints "Br J Sports Med 2015;49:843–851", and the British Library record gives issue 13. Fix: "2015;49(13):843–851 (pages as printed on a copy of the statement)."; Basis: https://www.sportaus.gov.au/__data/assets/pdf_file/0004/689647/IOC_consensus_statement_on_youth_athletic_development.pdf (a copy, not BJSM)
[minor] [bibliography] Sources, Lorenz; Current: "2022;51(9):1693–1707 (volume and pages not verified)."; Problem: an index record gives issue 9 and pages 1693–1707; the volume is still unconfirmed. Fix: "2022;51(9):1693–1707 (volume not verified)."; Basis: https://ouci.dntb.gov.ua/works/4NrMaE84
[minor] [source log] §10; Current: "were \"7.2% identical and 92.8% disparate\""; Problem: these figures come from the abstract only (the full text does not show the calculation). The Sources entry says so; the sentence that uses them does not. Fix: "were \"7.2% identical and 92.8% disparate\" (figures from its abstract; the full text does not show the calculation)"; Basis: https://link.springer.com/content/pdf/10.1007/s40279-023-01840-1.pdf

Confirmed:
Lloyd et al. 2016 (NSCA server PDF): all four quotations verbatim; the maturation definition; the early-specialisation definition with overuse injury, overtraining or dropout and motor "blunting"; "training age" absent; 30(6):1491–1509 and the nine authors.
Bergeron et al. 2015 (sportaus copy): November 2014 meeting; "more related to biological clocks…"; first two decades; peak VO2 up about 80% in girls and 150% in boys from 8 to 16; girls outscore boys on cycling peak power until about 12; selection between 9 and 15; both selection quotations; "older individuals generally outperform…"; 8.5–9.5 h; injury quotation; later bedtimes; "should avoid early sport specialisation"; specialising after puberty "tend to" mean fewer injuries; diversification; "highly unlikely" (for most); disconnect; tailored schedules; burnout and dropout.
Albaladejo-Saura et al. 2021 (MDPI): 13 studies; SMDs 0.37–2.31, 0.17–2.31 and 0.96–1.19; citation.
Ghadirzadeh et al. 2025 (elsevier.es PDF and USP page): 13 studies (5 cohort, 8 cross-sectional); 434,838 participants; OR 1.36 (1.20–1.53); adolescents 1.34 (1.15–1.56); late menarche not significant; I² about 80%; publication bias; confounders not consistently controlled; no males; DOI; authors.
Smith et al. 2018 (PubMed abstract): 57 studies, 308 samples, 25 sports, 1984–2016, OR 1.25 (1.21–1.30), age groups, level, sport type; 48(6):1451–1478. The correction to Table 4 (48:1989–1990) is confirmed.
Bethlehem et al. 2022 (eScholarship copy): 123,984 scans; 101,457 people; more than 100 studies; about 10% longitudinal; peaks 5.9 (5.8–6.1), 14.4 (14.0–14.7) and 28.7 (28.1–29.2); 2–10 years across 34 areas; bias quotation.
Foulkes & Blakemore 2018 (Springer abstract): the quotation and the three sources of variation; 21(3):315–323.
Tervo-Clemmens et al. 2023 (Nature PDF): 4 datasets (2 longitudinal, 2 cross-sectional); 10,766 people aged 8–35; 23 measures from 17 tasks; the 18–20 quotation; more than 95% of change before 18; fastest change 10–15; individual variation; citation.
Arain et al. 2013 (Dovepress): the abstract names no end age; citation.
Crone & Dahl 2012 (Springer page): inconsistent evidence on cognitive control; limbic responses peaking in mid-adolescence; heuristic model; adaptive value; 13:636–650.
Haddad et al. 2014: no difference when alone; d = 0.95 under observation; adults became safer; no within-group test; photographs; citation.
Lorenz & Kray 2022 (repository PDF): N 184, ages about 9–19; webcam peer; quotation; female pre-adolescents; male adolescents unaffected.
Sanchis-Sanchis et al. 2020 (Frontiers PDF): 254 pupils in 8 schools; CERQ differences after correction; partial η² 0.02 with the younger group higher; the abstract's mismatch; gender × age interaction 0.07 in both directions; "no causal relationships…".
Stambulova et al. 2021 (JYU repository copy): six layers; three transition types; ice-hockey phases; dual-career quotation and its consequences; Park review of 126 studies (1968–2010); 19(4):524–550, online 10 March 2020.
Paruthi et al. 2016 (PubMed: 12(6):785–786, DOI) and 2016b (AASM PDF): 13 voting members; modified RAND; 864 articles; hours; associations; 12(11):1549–1561.
Watson et al. 2015 (AASM PDF): 7 h or more; harms; "may be appropriate for young adults"; 15 experts; 5,314 articles; Sleep 38:843–844 and JCSM 11(6):591–592.
Güllich et al. 2022 (APS abstract): 51 reports; 477 effect sizes; 6,096 athletes, 772 world-class; adult and youth patterns; 17(1):6–29 (sponet record).
Gallant & Bélanger 2021 (Frontiers PDF): 38 studies, 33 testing the DMSP; all supported tenet 1; 6 supported tenet 2, 5 of them cross-sectional; after 16; the quotation; 71% cross-sectional; elite athletes.
Macnamara et al. 2016 (Purdue copy): 18%; 1%; no earlier start; 10,000 hours only for the violinists; 11(3):333–350.
Güllich & Barth 2024 (Springer PDF): 51 effect sizes; 6,233 athletes, 82% male; 2009–2022; nine countries; d −0.53 (−0.74 to −0.32, k 16) and 0.56 (0.40 to 0.72, k 34); studies rated high quality; I² about 75% and not discussed; "two disparate populations"; turnover 25–47% and 28–55%; correlational; 54:697–710.
Güllich et al. 2023 (Springer PDF): 110 samples (38,383 athletes) and 79 samples (22,961); quotation; a synthesis with no meta-analysis; 7.2% and 92.8% in the abstract; 53:1201–1217.
Tzioumakis et al. 2026 (Frontiers): players aged 10–15; autonomy support rose and fell (quadratic); disempowering behaviour fell; 17:1563931. The paper itself calls the design both randomly allocated and quasi-experimental; "trial" is acceptable.

Passes:
Claims: PASS on every claim I opened, with the corrections above. The Cobley claims, previously marked "not verified", now PASS.
Bibliography: PASS with minors (Cobley, Boccia, Bergeron, Lorenz). No reference is missing or invented. Unconfirmed fields are listed under Not verified.
Source log: PASS with minors. Every abstract-only claim is marked where it is made, except the 7.2% figure (finding above). Two claims rest on copies read off the publisher's page (Crone & Dahl, Macnamara); both are logged in Sources.
Grades: PASS with fixes. The grades follow SP1 §9. Güllich & Barth "strong, association" holds: every subgroup CI excludes zero, studies are rated high quality and the authors do not flag heterogeneity. The Güllich 2023 "weak" is right by rule 5. The F47 and F48 inconsistencies remain for the syllabus review.
Population: PASS with two minors (Haddad, Macnamara). Every under-18 transfer is labelled inference, except the cycling peak-power cell (finding above).
Scope and safety: PASS. Nothing teaches assessment, diagnosis or treatment. There is no weight-loss method, calorie figure or target weight, and no self-harm method. No law is stated. No real person is named. The disclaimer is present. Dani's snack and weight class are referred with no comment on weight. Sara's sleep, flatness and withdrawal go to referral.
Any sport: PASS. The 15 examples split as F25 records (football 4, athletics 4, judo 2, one each for swimming, basketball, handball, ice hockey and tennis); the largest share is 27%. No term tied to the Project owner, his sport, club or athletes was found.
Part 7, line by line: all items met except those in the findings. The search flag is off and the unit cites no rule or route. Case facts agree with the register, including every "added" fact.
Coach reading: usable. Every recommendation carries its evidence and its limits. The body runs to about 4,800 words; with the deliverable it is about 7,200, above the brief's 2,000–6,000 guide. The length is not padding, so this is no finding.
Figures (7): figure 1 (§4, range) PASS; figure 2 (§8, range) PASS; figure 3 (§10, range) PASS. Every label and number traces to the text, and each caption names its section and source.
Brief and flags: every brief item is covered. Thin, and stated as such in the unit: self-image (unsourced) and emotion regulation from 16 to 25 (unsourced). Deliverable A is complete with every cell graded; Deliverable B is built for all three athletes and as a template whose blanks say what goes in them. F12–F26, F28 and F42 are dealt with. F22 changes: Cobley is now verified in abstract, but there is still no pooled figure for male sport. F42 for Boccia: the DOI now opens. At the DOI address Boccia et al. report that the annual rate of improvement from 13 to 18 improved prediction of adult bests. No fix here adds that claim; it is for the maintainer to decide whether to cite it. F16, F23 (Somerville, Sawyer, Malina) and F21 (Walsh) remain open. The unit takes no claim from those sources.

Not verified:
- Lloyd 2016 DOI (PubMed showed a reCAPTCHA page).
- Lorenz volume 51.
- Crone & Dahl issue 9.
- Güllich 2022 author list against Crossref, and its intervals and study quality (full text not opened).
- Albaladejo-Saura and Smith full texts.
- The calculation behind the 7.2%.
- The Sleep version of Watson.
- The IOC statement and Bethlehem read only on copies, not BJSM or Nature pages.
- Ghadirzadeh at PMC: the address redirected, so it was not checked; the full text was read on elsevier.es instead.
- Haddad's frontiersin.org /text address redirected; I read the PDF instead.
- Not opened by the unit or by me: Somerville 2016, Sawyer 2018, Malina 2015, Walsh 2021, Park 2013.

Verdict: SP2 · fix · 0 error, 4 should-fix, 8 minor
