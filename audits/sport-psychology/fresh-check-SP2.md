---
audit: fresh check
unit: SP2 · The developing athlete, 10 to 25
course: sport-psychology · Sport Psychology for Coaches
model: claude-opus-5-5
date: 2026-11-17
chat: https://claude.ai/code/session_01KMmgQzXiriWxM3Z8z4XaJD
verdict: fix · 0 errors, 10 should-fix, 8 minor
---

The checker's final report, verbatim, from its hand-back. Saved before any finding was applied.

Verdict: SP2 · fix · 0 error, 10 should-fix, 8 minor

# Fresh check · SP2 · The developing athlete, 10 to 25

Checker: claude-opus-5-5, an isolated agent context that has not seen the unit written. Date: 2026-11-17. Live search was on. Inputs: unit.md; brief.txt (the brief from units_data.py); sourcing-standard.md Parts 1 and 7; notes.md; unsure.md; sources.md; case-facts.md; audit-units-SKILL.md §3 with its figures paragraph. {audit errata}: no audit report: skip it. Every fetch was of a URL that a WebSearch in this agent returned verbatim. A fetch that was redirected, refused or met a reCAPTCHA page counts as "not opened". None was retried or read from a copy.

Note: the unit's text has no unsure list at its end. The writer's list is in unsure.md, and this check started from it. The fresh-check line the maintainer adds needs an unsure list in the unit to sit under.

## (1) Coverage

- Three clocks (chronological, biological, training age): covered (§1).
- Puberty timing:
  - performance: covered.
  - selection: covered.
  - self-image: thin. No source was opened, and the unit says the point is unsourced.
- Relative age: covered for female sport. Male sport is thin; Cobley 2009 was not opened, and the unit says so.
- Brain development, protracted, by region and by person, with no cutoff age: covered (§4).
- The "25" claim: covered (§4). The unit says Somerville 2016 and Sawyer 2018 were not opened.
- Reward and peer evaluation, and what does not follow from a brain image: covered (§5).
- Self-regulation and emotion regulation by band: emotion regulation for 16 to 25 is thin (stated as unsourced).
- Identity 16 to 25, junior to senior, end of career: covered, resting on the ISSP stand alone.
- Sleep by age; sleep and mood, learning and injury: covered (§8).
- Specialisation and sampling: covered (§9).
- Early success as a weak predictor; the champion of 13 and the late developer of 17: covered (§10).
- Deliverable:
  - age-and-stage table, 4 bands by 4 columns, every cell graded: covered.
  - development notes for Dani, Milan and Sara, then a template whose blanks say what goes in them: covered.

## Findings

[should-fix] [label] §2 Selection; Current: "the selection rule itself is the IOC's consensus]"; Problem: the recommendation has no grade from the five; "the IOC's consensus" names a source, not a grade. The table already grades this rule "practice". Fix: "practice, for the selection rule (IOC consensus; no study opened tests it, rule 2)]"; Basis: brief.txt; Bergeron et al. 2015, https://bjsm.bmj.com/content/49/13/843.full

[should-fix] [label] §6 By band; Current: "[weak; inference under 18; one cross-sectional study and one behavioural study outside sport, rule 5]"; Problem: the grade covers specific advice ("prompt and model a routine and keep instructions short"). Neither cited study tests that advice; both only describe change with age. Under rule 2 the advice is practice. Fix: "[weak, for the description of change by band; inference under 18; one cross-sectional study and one behavioural study outside sport, rule 5; practice, for prompting, modelling a routine and keeping instructions short, which no study opened tests, rule 2]"; Basis: https://www.nature.com/articles/s41467-023-42540-8.pdf ; https://www.frontiersin.org/articles/10.3389/fpsyg.2020.00946/text

[should-fix] [accuracy] §9 Scoping review; Current: "most successful athletes specialised after 16, but"; Problem: the source says "many successful athletes only specialized after 16 years", and that most studies show this. It is a statement about studies, not about most athletes. Fix: "most of the studies found that successful athletes had specialised only after 16, but"; Basis: Gallant & Bélanger 2021, https://www.frontiersin.org/journals/sports-and-active-living/articles/10.3389/fspor.2021.741495/pdf

[should-fix] [label] §10 A champion of 13; Current: "[strong, for the association: early entry and junior success do not forecast senior success (one meta-analysis in athletes, effects excluding zero, high-quality studies, no disagreeing review found, rule 3; correlational, so no causal claim)]"; Problem: Güllich & Barth test the age of entry to a talent programme against later performance. They do not test whether junior success forecasts senior success. Their "largely two disparate populations" comes from an earlier study they cite (their ref. 63). Fix: "[strong, for the association: entry to a talent programme at a younger age went with higher junior and lower senior performance (one meta-analysis in athletes, effects excluding zero, high-quality studies, no disagreeing review found, rule 3; correlational, so no causal claim); moderate, for junior success as a poor forecast of senior success (Güllich et al., 2022, a meta-analysis read in abstract, and Boccia et al., 2017, one study in athletics, rule 4)]"; Basis: https://link.springer.com/content/pdf/10.1007/s40279-023-01957-3.pdf ; https://www.psychologicalscience.org/journals/perspectives/1745691620974772/

[should-fix] [label] Deliverable A, 13 to 15, What to hold back; Current: "Treating a national title or programme selection as a forecast [strong, for the association (Güllich & Barth, 2024)]"; Problem: a title is junior success, which the meta-analysis did not test; "strong" holds only for programme entry. Fix: "Treating programme selection as a forecast [strong, for the association (Güllich & Barth, 2024)]; treating a national title as one [moderate, association (Güllich et al., 2022; Boccia et al., 2017)]"; Basis: as above

[should-fix] [label] Deliverable A, 16 to 18, What to hold back; Current: "Reading junior rankings as senior forecasts [strong, association]"; Problem: same over-reach as above. Fix: "Reading junior rankings as senior forecasts [moderate, association; Güllich et al., 2022; Boccia et al., 2017]"; Basis: as above

[should-fix] [label] Deliverable B, Dani, What I hold back; Current: "Reading her title at 13 as a forecast [strong, association]"; Problem: same over-reach as above. Fix: "Reading her title at 13 as a forecast [moderate, association; Güllich et al., 2022; Boccia et al., 2017]"; Basis: as above

[should-fix] [attribution] Sources, Smith et al. 2018; Current: "*Sports Medicine* 2018;48(6) (pages not shown on the page opened)."; Problem: the publisher's record gives the pages. Fix: "*Sports Medicine* 2018;48(6):1451–1478."; Basis: https://pubmed.ncbi.nlm.nih.gov/29536262/

[should-fix] [attribution] Sources, ISSP stand; Current: "Stambulova NB, et al."; Problem: the stand has three authors; "et al." hides two of them (writer's unsure item 2). Fix: "Stambulova NB, Ryba TV, Henriksen K."; Basis: https://jyx.jyu.fi/handle/123456789/68164?show=full (vol 19(4):524–550, DOI 10.1080/1612197X.2020.1737836)

[should-fix] [figure] §8, second viz caption; Current: "None of the three was built on studies of athletes alone."; Problem: the caption adds a fact the text does not state. The text says only that Paruthi reviewed studies in children and adolescents in general. The IOC figure rests on its ref. 43, which was not opened. Fix: "Paruthi et al. (2016) reviewed studies in children and adolescents in general, not athletes; the IOC figure rests on a reference not opened for this unit."; Basis: unit §8; https://bjsm.bmj.com/content/49/13/843.full

[minor] [accuracy] §2 Performance; Current: "108 girls; football, basketball and handball;"; Problem: only 10 of the 13 included studies are in these three sports (football 5, basketball 3, handball 2). Fix: "108 girls; mostly football, basketball and handball;"; Basis: https://mdpi.com/1660-4601/18/1/328

[minor] [attribution] §10 Talent programmes; Current: "The authors call successful juniors and successful seniors largely two different populations, and report annual turnover of about 25% to 55% of athletes within programmes."; Problem: both statements are taken from earlier studies; Part 1 asks that the reporting paper be kept separate from the claim. The turnover is two ranges for two settings, not one. Fix: "Citing earlier studies, the authors call successful juniors and successful seniors largely two disparate populations, and report annual athlete turnover of 25% to 47% in youth sport academies and 28% to 55% in federations' junior squads."; Basis: https://link.springer.com/content/pdf/10.1007/s40279-023-01957-3.pdf

[minor] [accuracy] §3; Current: "pre-adolescent (11 and under) and early adolescent (12 to 14) groups"; Problem: the abstract's term is "adolescent (12–14 years)". Fix: "pre-adolescent (11 and under) and adolescent (12 to 14) groups"; Basis: https://pubmed.ncbi.nlm.nih.gov/29536262/

[minor] [label] Deliverable B, Milan, Biological age; Current: "No maturity estimate on file; at 17 none is needed for coaching decisions [practice]."; Problem: a recommendation with no source given where it is made. Fix: "No maturity estimate on file; at 17 none is needed for coaching decisions: maturity-associated selection falls mostly between about 9 and 15 (IOC) [practice]."; Basis: https://bjsm.bmj.com/content/49/13/843.full ("which covers the period between 9 and 15 years of age")

[minor] [label] §8 What to do; Current: "[weak, positive; consensus built on studies outside sport, rule 5; inference for the athlete populations]"; Problem: one grade covers both the hours (consensus, weak) and the action of asking athletes and timing sessions, which no opened study tests (practice). The writer's notes already flag that SP1 grades consensus statements differently. Fix: "[weak, positive, for the hours by age (consensus built on studies outside sport, rule 5; inference for the athlete populations); practice, for asking and timing sessions, which no study opened tests, rule 2]"; Basis: https://pmc.ncbi.nlm.nih.gov/articles/PMC4877308 ; notes.md

[minor] [attribution] Sources, Boccia et al. 2017; Current: "e0170744. https://doi.org/10.1371/journal.pone.0170744"; Problem: search results show a published correction (PMC5441632). The source log does not record it, and neither the writer nor this check opened it. Fix: "e0170744. https://doi.org/10.1371/journal.pone.0170744 (a correction was published, PMC5441632; not opened for this unit)"; Basis: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5441632/ (redirected: not opened)

[minor] [label] Deliverable A, 10 to 12, What to watch; Current: "the IOC names burnout and dropout as recognised parts of youth sport [practice]"; Problem: this claim is not in the body and has no link (Part 1: closing material adds no unsourced claim). Fix: "the IOC statement names athlete burnout and the dropout that follows it as a recognised part of youth sport ([Bergeron et al., 2015](https://doi.org/10.1136/bjsports-2015-094962)) [practice]"; Basis: https://bjsm.bmj.com/content/49/13/843.full ("athlete burnout and subsequent related drop-out from sport being a recognised part")

[minor] [style] Deliverable B, Milan, Training age; Current: "the age he started football is not in the register: ask him."; Problem: "the register" is internal to the course; the coach never sees it. Fix: "the age he started football is not recorded: ask him."; Basis: brief.txt (reader)

Every Current string was checked: each occurs exactly once in unit.md.

## Confirmed

- **Arain 2013:** the abstract names no age at which maturation ends; citation fields match. https://www.dovepress.com/maturation-of-the-adolescent-brain-peer-reviewed-fulltext-article-NDT
- **Ghadirzadeh 2025:**
  - 13 studies (5 cohort, 8 cross-sectional), 434,838 females.
  - Early menarche OR 1.36 (1.20–1.53); in adolescents 1.34 (1.15–1.56); late menarche 0.91, not significant.
  - I² about 80%; Egger's test significant; confounders not consistently controlled; no boys.
  - Authors, volume, article number and DOI match.
  - https://www.elsevier.es/en-revista-clinics-22-pdf-download-S1807593225001139
- **Bergeron 2015 (IOC):**
  - Every quotation the unit uses was found verbatim.
  - VO2 +80% in girls, +150% in boys, ages 8 to 16.
  - Girls ahead on cycling peak power until about 12, because they mature earlier.
  - 8.5–9.5 h for adolescents (its ref. 43).
  - Meeting in November 2014; selection window 9 to 15; maturation over about the first two decades.
  - Specialisation, diversification and talent-system passages as the unit gives them.
  - https://bjsm.bmj.com/content/49/13/843.full
- **Güllich & Barth 2024:**
  - k = 51, N = 6,233, 82% male, 2009–2022, nine countries.
  - Juniors d = −0.53 (−0.74 to −0.32), k = 16; seniors d = 0.56 (0.40 to 0.72), k = 34.
  - Studies rated high quality (MMAT); design correlational; Sports Med 54:697–710.
  - https://link.springer.com/content/pdf/10.1007/s40279-023-01957-3.pdf
- **Güllich 2022, abstract:**
  - 51 reports, 477 effect sizes, 6,096 athletes, 772 among the world's top.
  - Adult world-class vs national-class and youth findings as the unit states them.
  - https://www.psychologicalscience.org/journals/perspectives/1745691620974772/
- **Macnamara 2016, abstract:**
  - 18% of variance overall; "only 1%" among elite performers.
  - Higher-skill athletes did not start earlier.
  - The abstract does not mention 10,000 hours; citation fields match.
  - https://hhs.purdue.edu/skill-learning-and-performance-lab/wp-content/uploads/sites/43/2024/08/macnamara-et-al-2016-the-relationship-between-deliberate-practice-and-performance-in-sports-a-meta-analysis.pdf
- **Smith 2018, abstract:**
  - 57 studies, 308 samples, 25 sports, 1984–2016.
  - OR 1.25 (1.21–1.30), which the authors call small; moderators as the unit gives them.
  - The correction changes only Table 4.
  - https://pubmed.ncbi.nlm.nih.gov/29536262/ ; https://rd.springer.com/content/pdf/10.1007/s40279-018-0915-3.pdf
- **Haddad 2014:**
  - 40 adolescents aged 11–18 and 24 adults aged 20–38; fictitious peers shown in photographs.
  - No age difference in private; under observation d = 0.95.
  - Adults became more cautious when watched; adolescents broadly did not change.
  - https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2014.01476/full
- **Lorenz & Kray 2022:**
  - 184 participants aged 8.59–18.97; virtual same-age, same-sex peer said to be watching by webcam.
  - Quotation verbatim; boys "not susceptible to peer observation"; exploration effect largest at younger ages.
  - Volume 51(9), pages 1693–1707.
  - https://link.springer.com/10.1007/s10964-022-01608-2
- **Tervo-Clemmens 2023:**
  - 4 datasets, N = 10,766, 13,817 visits, ages 8–35, 23 measures from 17 tasks.
  - Change steepest at about 10–15; "(18–20 years old)" quotation verbatim; over 95% of change before 18.
  - Individual variability expected; no imaging.
  - https://www.nature.com/articles/s41467-023-42540-8.pdf
- **Bethlehem 2022:**
  - Scans, participants and ages as stated.
  - Peaks with 95% bootstrap CIs: total grey matter 5.9, subcortical 14.4, white matter 28.7; regional peaks 2–10 years across 34 areas.
  - Bias quotation verbatim; Nature 604:525–533.
  - https://www.nature.com/articles/s41586-022-04554-y
- **Albaladejo-Saura 2021:**
  - 13 studies; 1,431 athletes (1,323 boys, 108 girls); age ranges as stated.
  - Test results for boys as stated; for girls, height and mass only.
  - https://mdpi.com/1660-4601/18/1/328
- **Paruthi 2016 (AASM):** hours by age, 13 experts, 864 articles, method and associations as stated; citation fields match. https://pmc.ncbi.nlm.nih.gov/articles/PMC4877308
- **Watson 2015 (AASM and SRS):** 7 or more hours for ages 18–60; >9 h "may be appropriate for young adults"; 15 experts, 5,314 articles; citation fields match. https://pmc.ncbi.nlm.nih.gov/articles/PMC4434546/
- **Crone & Dahl 2012, abstract and key points:** as the unit states them. https://link.springer.com/article/10.1038/nrn3313
- **Foulkes & Blakemore 2018, abstract:** quotation verbatim; socioeconomic status, culture and peers named; 21(3):315–323. https://link.springer.com/article/10.1038/s41593-018-0078-4
- **Gallant & Bélanger 2021:**
  - 38 studies, 33 on DMSP; 71% cross-sectional.
  - Tenet 1 supported by all studies; tenet 2 by 6 studies, 5 of them cross-sectional.
  - "specific age ranges" quotation verbatim.
  - https://www.frontiersin.org/journals/sports-and-active-living/articles/10.3389/fspor.2021.741495/pdf
- **Sanchis-Sanchis 2020, abstract:** 254 pupils aged 9–16 in 8 schools; results and quotation as stated. https://www.frontiersin.org/articles/10.3389/fpsyg.2020.00946/text
- **ISSP stand:**
  - Six layers; three kinds of transition.
  - Junior-to-senior transition lasts "several months to years"; four phases in the ice-hockey research.
  - Dual-career quotation verbatim; risks without support; Park review of 126 studies, 1968–2010.
  - Pages 524–550; online 10 March 2020.
  - https://informahealthcare.com/doi/full/10.1080/1612197X.2020.1737836

## (7) Figures

1. **§4 range:** PASS. Every label and number traces to §4. The caption names the section and both sources. "Bootstrap" in the caption is true of the source.
2. **§8 range:** FIX. All labels and numbers trace to §8, but the caption's last sentence adds a fact (should-fix above).
3. **§10 range:** PASS. All values trace to §10; the caption gives source, design and the sign convention.

## (6) Errata

No audit report, so this step was skipped. The pointers to SP1 (grade key, claim-check sheet, scope card) could not be checked, because SP1 is not in the folder.

## Seven passes

- **Claims: FAIL (minor).**
  - 20 of 21 sources opened. Three stretches found: Gallant "most"; Güllich & Barth applied to junior success; Albaladejo's list of sports.
  - Boccia 2017 not opened (doi.org redirected; the econpapers fetch was refused). Its claims in §10, the table and the Milan and Sara notes are unverified.
  - Lloyd 2016 (NSCA): the content matches NSCA Japan's translation (https://nsca-japan.or.jp/pdf/database/position-statement/ps_longterm.pdf). The English quotations were not opened.
- **Bibliography: FAIL.**
  - Smith 2018 is missing its pages; the ISSP stand hides two authors; Boccia's correction is not recorded.
  - No reference that does not exist was found.
  - Not fully verified: Güllich 2022 volume and pages; Crone & Dahl issue; Lloyd DOI; Boccia's whole record; Gallant & Bélanger's authors.
- **Source log: PASS.** All 21 entries have rows with address, what was read and date. Every claim from an abstract alone is marked in the text and in Sources.
- **Grades: FAIL (should-fix).**
  - §2 selection rule has no grade.
  - §6 advice should be practice.
  - "strong" is stretched from programme entry to junior success, in §10 and three table cells.
  - §8 single grade over hours and action (minor).
  - All other grades follow the key as the unit states it.
- **Population: PASS.** Samples and designs are named; correlations are called correlations; transfers to younger athletes are labelled inference. The §3 birth-month check rests on female-sport data, and the unit says so.
- **Scope and safety: PASS.**
  - No assessment, diagnosis or treatment is taught; mood, sleep and eating each end at the first conversation and referral, naming who takes over.
  - No weight figure, calorie figure, target weight or self-harm method.
  - No law stated as the reader's; the disclaimer is present.
  - No real person named.
- **Any sport: PASS.**
  - Examples: football 4, athletics 4, judo 2, and one each of swimming, basketball, handball, ice hockey and tennis; 15 in all, largest share 27%.
  - Individual, team and weight-class sports are all present.
  - Nothing that points to the Project's owner; private_terms.py is not in the folder, so it was not run.

## Part 7, line by line

Every line of Part 7 is met, with these exceptions:
- **Sources match Crossref:** no (Smith, ISSP).
- **Grades follow SP1's key:** no (four should-fix).
- **Sourced where made:** yes, apart from two minor items (Milan's biological age; the IOC burnout line in the table).
- **Private terms:** the script was not run (absent); nothing found by reading.

## Row claims

- **Imaging:** PASS. §4 and §5 draw no advice from imaging alone, and the table marks the brain peaks "no coaching use".
- **"25":** PASS. It is examined against the sources opened and asserted neither way, with Somerville and Sawyer stated as not opened.
- **Sleep:** PASS in the text and the table; every range is given for the ages its statement names. The §8 caption needs the fix above.

## Read as the coach

The unit reads as depth, not a primer, and every action carries a grade. The "strong" grade on reading a title as a forecast, and "register" in Milan's note, would cost a careful coach some trust. Self-image and emotion regulation at 16 to 25 remain thin.

Verdict: SP2 · fix · 0 error, 10 should-fix, 8 minor
