---
code: SP3
kind: quality-review (rule 13)
model: claude-opus-5-5
date: 2026-11-19
chat: https://claude.ai/code/session_01KMmgQzDra5WhwrnjTVBqy8
note: report returned as the agent reply (harness blocked its file write) and saved verbatim by the chat
---
Verdict: SP3 · fix · 0 error, 5 should-fix, 9 minor
Model: claude-opus-5-5

(The harness refused the write to out/report.md, so this reply is the whole report.)

Quality review (rule 13) of SP3, "Motivation and the climate you create", as it stands in the packet. Fresh agent, live search, 19 Nov 2026. Only packet files and the web were used. The unit was not edited.

## 1. Claims: FIX
I opened and checked every cited claim except Brenner & Watson (2024): the PubMed page returned an empty page and no publisher page came back from a search. Discrepancies:
- Section 4: the reward rule is graded [practice, rule 2], but a meta-analysis of experiments the unit cites tests it outside sport (Deci et al., 1999). SP1's rule 2 then does not apply; rule 5 gives weak. See the findings.
- Section 8: one quoted phrase from the IOC statement is "over-training" in the unit and "overtraining" on the copy read (minor; the earlier check read the BJSM page).
- Section 2: the coach programme's avoid list has three items, not two (Smoll et al., 2007, publisher's page).
Every other number, sample and quotation checked holds; see Confirmed.

## 2. Bibliography: FIX
- Brenner & Watson: no DOI link (Part 7 asks for one). The seed list's Crossref DOI is available.
- Meeusen et al.: volume 45 and issue 1 are shown on the copy (the sportgeneeskunde.com PDF); the entry says not verified.
- Bergeron et al.: the full author list and pages 843–851 are shown on a hosted copy; the entry says not verified.
- Tzioumakis et al.: the five middle authors are still not shown on the publisher page (as the entry says). Not fixable from what is reachable.
- Burke et al.: Ulster's record confirms the authors (Burke, Sharp, Woods, Paradis) and DOI. The volume and issue are still not shown anywhere opened.
- Mossman et al.: volume and pages not confirmed (the Melbourne record served a bot-check page). The entry already says so.
- The other entries match what was shown: authors, title, journal, year, volume, article or pages, DOI.
- No reference is non-existent.

## 3. Source log: FIX
- Tzioumakis et al.: the entry has no date for the "correction session" read.
- The section heading says 17 Nov, but several entries record reads on 18 Nov.
- In the section 2 table, the Mossman row does not say "abstract", though section 1 does.
- Several entries say "at the publisher's page" with no address (Adams, Gu & Cheng, Haberstock, Hu, Lewis, Morales-Sánchez, Zhang ×2; Monteiro "at PubMed Central"). The DOI link stands in for the address. Not raised as a finding.
- Every Sources entry is cited in the text.
- The Bartholomew 2010 CCBS paper is named as "not opened" and is correctly not listed.

## 4. Grades: FIX
- One grade is off SP1's key: the reward rule in section 4 (see section 1 of this report).
- The other grades follow the key:
  - Mossman: [moderate] by rule 4. The authors' in-press manuscript shows no quality rating of the primary studies and I² = 86%, so rule 3 cannot be met; moderate is right.
  - Zhang, Wang & Shao: [moderate] by rule 4.
  - Two controlled studies (section 3): [weak] by rule 5.
  - Gao: [weak], a systematic review with no pooled estimate.
  - Burke: [weak].
  - Harsh coaching: [weak, against].
- The preamble's [practice] convention for consensus statements whose studies were not opened is SP2's convention under F14. Its conflict with SP1's section 9 is open as F47, so it is not counted as an error here.

## 5. Population: PASS
- Each finding names its sample and design. Correlations are called correlations.
- Transfers to younger athletes are labelled inference: Mossman (ages not given), Deci (lab, children and students), Adams (adults), Lewis (adults 18 to 40).
- Transfers from younger samples to older bands are also labelled inference (sections 3, 7, 11). That use of the label is open as F48 and is not counted.
- Haberstock "40% para-athletes": the source gives 39.6%. Acceptable rounding.

## 6. Scope and safety: PASS
- Nothing teaches assessment, diagnosis or treatment. Section 8 hands burnout or overtraining decisions to a doctor or licensed professional by the SP1 route.
- Weight and eating are kept out of the session plans and the parents' page, with a named contact.
- No weight-loss method, calorie figure, target weight or self-harm method appears.
- No law is stated. Filming consent is put as a question to the welfare or safeguarding officer.
- The information-not-advice line is present (preamble and the parents' pages).
- No real athlete, coach or club is named.

## 7. Any sport: PASS
Example count, case athletes and studies used as illustrations:
- football 3 (Milan; Morales-Sánchez; PAPA trial)
- swimming 2 (section 2 illustration; Monteiro)
- 1 each: judo (Dani), athletics 400 m (Sara), handball, basketball, ice hockey, gymnastics, volleyball, rowing, tennis

That is 14 in all, the largest share 3/14 (21%), under a third. The required kinds are present: individual, team, weight-class (judo), timed (400 m) and judged (gymnastics). `kit/private_terms.py` is not in the packet, so it was not run. Nothing in the text points to a particular club or squad outside the case register.

## Part 7, line by line
- Sourced where made: yes.
- Source types: yes. Fletcher & Sarkar is a practitioner article and only a [practice] grade rests on it.
- No banned source types: yes.
- Source log complete: FIX (Tzioumakis date).
- Entries match publisher or Crossref records: FIX (Brenner DOI, Meeusen volume; minor Bergeron).
- Grades follow the key: FIX (section 4 reward rule).
- Sample and design stated: yes.
- Inference labelled: yes.
- Effect sizes in the source's terms: yes.
- Popular claim named and set against evidence: yes (harsh coaching, exercise as punishment, "praise in public, correct in private", challenge-support model).
- Coach's part: yes.
- Weight and self-harm: yes.
- Law: yes.
- Real names: yes.
- Three kinds of sport, at most a third each: yes.
- Case labelled "(fictional)" and consistent with `case-facts.md`: yes. Dani, Milan and Sara are labelled on first use. Facts agree with the register, including the SP3 additions. The case is never used as evidence.
- Private terms: not run (script not in packet).
- Search-flag dating: not applicable (search off; no current rules or services stated).
- Deliverable built on the case, then as a template: yes.
- Reads as advice without evidence: no.
- DOI links: yes, except Brenner (finding).

## Read as the preamble's coach
A coach without psychology training can use it:
- The design warning comes first.
- Each recommendation has its grade beside it.
- The self-audit is countable from one filmed session.
- The three-change rule is mechanical and is applied visibly. Milan's deviation from it is explained.

The weakest part for that reader is section 6. The challenge-and-support model rests only on a practitioner article's abstract and notes, and the unit says so plainly.

## Brief coverage
- Self-determination theory and achievement goal theory, each with its youth-sport evidence and design: covered.
- Behaviours one by one, with enjoyment, anxiety, effort, dropout and burnout: covered. Effort is stated as unmeasured in the studies opened.
- Coach-training interventions with their samples: covered. Smith, Smoll & Cumming (2007) is stated as not opened.
- Rewards, punishment, and exercise as punishment: covered.
- Selection, playing time and attention: covered.
- High challenge with high support: covered, thin by necessity.
- Enjoyment and dropout: covered. Crane & Temple is stated as not opened.
- Burnout and overtraining from the consensus statements: covered.
- Parents: covered.
- Deliverable:
  - Twenty observable behaviours (S1–S10, C1–C10), scored for three case sessions, with three changes each, and a template: full.
  - Three session plans (judo as the individual sport, football as the team sport, 400 m as the timed sport), each written twice, and a template: full.
  - Parents' page for Dani's squad, Milan's squad, and an athlete version for Sara (adult), and a template: full.
- Gives: the autonomy-supportive and controlling behaviour list (for SP7 and DD-SP1) and the parents' page (for SP8 and SP10) are present.

## Flags naming SP3
- F5, F184 (Bartholomew reviews): partly met by this review. The 2009 review is reachable as the authors' manuscript in the University of Birmingham repository and was read in full (finding below). The 2011 paper was not found. Grade unchanged.
- F7, F24: process only; no action in the unit.
- F8: SP1's key is used unchanged.
- F14, F47: the preamble follows SP2's convention, pending syllabus review S-SP1. Not dealt with in the unit; not this unit's to decide.
- F48: the unit uses "inference" for older bands, pending S-SP1. Carried.
- F78: SP3's rules on exercise as punishment and selection as a threat stand (sections 4 and 5, C6, C10). Nothing to change.
- F104: Smith, Smoll & Cumming (2007) still not opened. Section 3 says so and reports nothing from it. Dealt with.
- F108, F158 (Neely et al., 2016): not cited by SP3. Nothing to do.
- F109 (MMCOS list): dealt with by disclosure in Deliverable A (abstract only; the twenty behaviours are not checked against it). Smith et al. (2016) is not added. Open.
- F128: SP3 section 8 no longer contains "your part ends at the referral"; it points to "the line ... in SP1". Nothing to change until S-SP1.
- F183: the study count in section 10 is not updated to DD-SP1's two additional studies. Optional ("may"). DD-SP1 is not in the packet, so it was not applied here.
- F189: section 5 states that no study opened tests public against private feedback. Consistent.
- F203: this review.

## Figures
1. Section 1, kind "range": PASS. The four ρ values (.39, .16, −.01, −.19) and "131 samples, 38,844 participants" are in section 1. The caption names the section and the source. A range with low equal to high is used as a dot plot so that negative values can be shown. Acceptable for comparing numbers.
2. Section 1, kind "compare": PASS. 313, 12, 9 and 334/177 are in section 1 ("of the effect sizes, 313 came from cross-sectional designs, 12 from longitudinal and 9 from experimental"). The caption names the section and the source.
3. Section 3, kind "line": PASS. 25.44 → 23.98 and 24.12 → 27.01, the range 15 to 60 and "about 12 weeks" are in section 3. The caption names the section, the source and the design. A line fits a pre/post change in two groups.

## FINDINGS
should-fix · accuracy · section 4
- Current: "practice, for the reward rule alone, which no study opened tests, rule 2]"
- Problem: Deci et al. (1999), cited in the same paragraph, is a meta-analysis of 128 experiments testing whether rewards lower free-choice intrinsic motivation. A study of some design tests the claim, so SP1's rule 2 (practice) does not apply. Rule 5 (evidence only from outside sport) gives weak, with the inference label for athletes.
- Fix: "weak, for the reward rule alone: tested only in laboratory experiments with children and college students outside sport (Deci et al., 1999), rule 5; for athletes, inference]"
- Basis: Deci, Koestner & Ryan 1999, full text on a copy, https://depts.washington.edu/techdocs/papers/deciExtrinsicRewardsAndIntrinsicMotivation99.pdf; SP1 section 9, rules 2 and 5.

should-fix · coverage · section 10 (F5, F184)
- Current: "the two reviews by Bartholomew and colleagues (2009, 2011) could not be opened at a publisher's page, PubMed or a DOI address, and nothing is reported from them."
- Problem: the 2009 review is reachable in full as the authors' manuscript. F5 asked SP3 to open it.
- Fix: "the 2011 paper by Bartholomew and colleagues could not be opened, and nothing is reported from it. The 2009 review was read in full on the authors' manuscript in the University of Birmingham's repository, not the publisher's version (quality review, 19 Nov 2026). It is a narrative review that proposes a preliminary taxonomy of six controlling strategies: tangible rewards, controlling feedback, excessive personal control, intimidation, promoting ego-involvement (including public evaluation and comparison with others) and conditional regard. It draws mainly on parenting and education research; the sport studies it cites are mostly correlational, and it states that no sport study had yet examined conditional regard ([Bartholomew et al., 2009, author manuscript read](https://doi.org/10.1080/17509840903235330)). It adds no controlled test, so the grade below stands."
- Basis: https://research.birmingham.ac.uk/files/2920310/Ntoumanis_2009_International_Review_of_Sport_and_Exercise_Psychology.pdf

should-fix · attribution · Sources
- Current: "- Bergeron MF, Mountjoy M, Armstrong N, et al. International Olympic Committee consensus statement on youth athletic development."
- Problem: the Bartholomew 2009 review, cited by the fix above, needs its Sources entry. Initials were not shown on the manuscript.
- Fix: "- Bartholomew, Ntoumanis, Thøgersen-Ntoumani (initials not verified). A review of controlling motivational strategies from a self-determination theory perspective: implications for sports coaches. *International Review of Sport and Exercise Psychology* 2009;2(2):215–233. https://doi.org/10.1080/17509840903235330 (full text read on the authors' manuscript, https://research.birmingham.ac.uk/files/2920310/Ntoumanis_2009_International_Review_of_Sport_and_Exercise_Psychology.pdf, not the publisher's version, by the quality review, 19 Nov 2026; journal, volume, issue and pages as in the course's seed list (Crossref) and the manuscript's citation)\n- Bergeron MF, Mountjoy M, Armstrong N, et al. International Olympic Committee consensus statement on youth athletic development."
- Basis: same URL; bibliography.md R2.

should-fix · attribution · Sources (Brenner & Watson)
- Current: "(volume, issue and article number from the publisher's address, not shown on the page opened; DOI not verified)."
- Problem: Part 7 requires the DOI address as a link. The seed list carries the Crossref-checked DOI. The entry gives none.
- Fix: "(volume, issue and article number from the publisher's address, not shown on the page opened). https://doi.org/10.1542/peds.2023-065129 (DOI from the course's seed list, checked at Crossref on 16 Nov 2026; not opened by the checks)."
- Basis: bibliography.md C8. PubMed https://pubmed.ncbi.nlm.nih.gov/38247370/ could not be read (empty page).

should-fix · attribution · Sources (Tzioumakis et al.)
- Current: "(full text of the final version read at the publisher's page in the correction session;"
- Problem: the source log has no date for this read (Part 7: address, what was read, date).
- Fix: "(full text of the final version read at the publisher's page, https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2026.1563931/full, in the correction session (date not recorded) and by the quality review, 19 Nov 2026, which confirmed 68 coaches (36 intervention, 32 control), players aged 10 to 15, a workshop of about six hours, the MMCOS described as validated, no standardised effect sizes, no athlete outcomes and \"short-term, but not sustained\";"
- Basis: the URL in the fix.

minor · attribution · Sources (Meeusen et al.)
- Current: "*Medicine & Science in Sports & Exercise* 2013 (first page 186)."
- Problem: volume and issue are shown on the copy already cited.
- Fix: "*Medicine & Science in Sports & Exercise* 2013;45(1):186– (last page not verified)."
- Basis: https://sportgeneeskunde.com/wp-content/uploads/Meeusen-et-al-2013-Overtraining-Consensus-ECSS-ACSM.pdf

minor · attribution · Sources (Meeusen et al.)
- Current: "volume, issue and last page not verified;"
- Problem: as above.
- Fix: "volume 45 and issue 1 confirmed on the same copy by the quality review, 19 Nov 2026; last page not verified;"
- Basis: same URL.

minor · attribution · Sources (Bergeron et al.)
- Current: "authors and end page not verified: taken from the course's seed list, as the page showed initials only and no journal details)"
- Problem: the full author list and pages are shown on a hosted copy of the published article.
- Fix: "authors (Bergeron MF, Mountjoy M, Armstrong N, Chia M, Côté J, Emery CA, Faigenbaum A, Hall G Jr, Kriemler S, Léglise M, Malina RM, Pensgaard AM, Sanchez A, Soligard T, Sundgot-Borgen J, van Mechelen W, Weissensteiner JR, Engebretsen L) and pages 843–851 confirmed on a copy of the published article hosted by World Rowing, not the publisher's page, by the quality review, 19 Nov 2026)"
- Basis: https://d2cx26qpfwuhvu.cloudfront.net/worldrowing/wp-content/uploads/2020/12/04181717/IOCOlympicCommitteeStatement_Neutral.pdf

minor · accuracy · section 8
- Current: "systems that promote over-training"
- Problem: the copy read gives "systems that promote overtraining" with no hyphen. Quotation marks require the exact words. The earlier check reports a word-for-word match at BJSM, so check the publisher's page before applying.
- Fix: "systems that promote overtraining"
- Basis: World Rowing copy, URL above.

minor · coverage · section 2
- Current: "adds two behaviours to avoid: withholding reinforcement for effort, and punishing mistakes"
- Problem: the programme's guidelines list a third behaviour to avoid, which also supports C3.
- Fix: "adds three behaviours to avoid: withholding reinforcement for effort, punishing mistakes, and giving instruction in a harsh, sarcastic or demeaning manner"
- Basis: Smoll et al. 2007, https://jyd.pitt.edu/ojs/jyd/article/view/358/344

minor · label · section 2 table
- Current: "Meta-analysis of 131 samples in sport and exercise; correlational; ages not in abstract ("
- Problem: the claim rests on the abstract alone, and this row does not say so.
- Fix: "Meta-analysis of 131 samples in sport and exercise; correlational; abstract read; ages not in abstract ("
- Basis: https://informahealthcare.com/doi/abs/10.1080/1750984X.2022.2031252

minor · accuracy · section 1
- Current: "if they are mainly exercisers, rule 5 makes it weak; no causal claim.]"
- Problem: the authors' in-press manuscript settles two of the unknowns behind this grade. It reports no quality rating of primary studies, so rule 3 cannot be met. It reports I² = 86% for autonomous motivation. It finds no moderation by sport or exercise setting.
- Fix: "if they are mainly exercisers, rule 5 makes it weak; no causal claim. The authors' in-press manuscript (https://selfdeterminationtheory.org/wp-content/uploads/2022/02/InPress_MossmanSlempEtAl_Autonomy.pdf, read by the quality review, 19 Nov 2026, not the published version) reports no rating of the primary studies' quality, heterogeneity of I² = 86% for autonomous motivation, and no moderation by sport or exercise setting; rule 3 cannot be met, so the grade is moderate.]"
- Basis: the URL in the fix.

minor · style · Sources heading
- Current: "## Sources (addresses opened 17 Nov 2026 by the writer or by the checks, as each entry says)"
- Problem: the entries record reads on 18 Nov, and the fixes above add 19 Nov.
- Fix: "## Sources (addresses opened 17 to 19 Nov 2026 by the writer or by the checks, as each entry says)"
- Basis: the unit's own entries.

## UNVERIFIED
- Section 8: Brenner & Watson (2024), both quotations (the overtraining syndrome definition, the burnout definition, "one of the primary reasons for attrition in youth sports"). PubMed served an empty page and no publisher page was returned by a search. Not opened.
- Section 3: Smoll et al. (2007), "with the second author, wrote the manuals". Not stated in what the fetch returned.
- Section 2 table: Zhang, Du & Tao (2025), the exact words "causation cannot be established". The fetch paraphrased that the authors state it; the wording was not seen verbatim.
- Section 1: Gu & Cheng (2026), the remark that "their abstract uses causal wording". The text read shows causal language in the Discussion and Conclusion; the abstract was not seen separately.
- Sources: Mossman et al., volume 17(1) and pages 540–563. The Melbourne record served a bot-check page; the publisher's page shows none.
- Sources: Tzioumakis et al., the five middle authors (not shown).
- Sources: Burke et al., volume and issue (not shown on the publisher's page or Ulster's record).
- Sources: Gustafsson et al. Verified on the University of Canberra record, not at the publisher (the publisher's page shows no details).
- Section 6 and Sources: Fletcher & Sarkar's volume, issue and pages. Not re-checked; the Nottingham Trent record was not fetched.

## Confirmed
- Mossman 2024: 1,320 correlations, 131 samples, N = 38,844; ρ = .39 / .16 / −.01 / −.19; no moderation by culture or sport type; competence support, relatedness support, structure and involvement named. https://informahealthcare.com/doi/abs/10.1080/1750984X.2022.2031252
- Gómez-López 2020: 479 players (250 boys, 229 girls), aged 16 and 17, regional teams, measured during the championship; PMCSQ-2 items as quoted; r = 0.43 and −0.31; task path to fear of failure not significant; ego to anxiety through fear of failure; authors, 17(2):592. https://core.ac.uk/download/322669511.pdf
- Gu & Cheng 2026: 177 studies, 334 effect sizes; 313/12/9; r = 0.27, CI [0.22, 0.32] in the table and [0.20, 0.32] in the text; I² = 98.45%; no I² for the subgroup; "pattern of association rather than a confirmed causal mechanism"; coding of negative outcomes not stated; vol 16, published 8 Jan 2026. https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2025.1716745/full
- Morales-Sánchez 2020: 103 male players aged 12–17, one club, convenience sample, before a training session; the four CCBS subscales; negative conditional support defined as withholding attention and affection; β = 0.53; indirect effect 0.35; thwarting "stronger" than the absence of satisfaction; autonomy-support recommendations; ABQ dimensions. https://mdpi-res.com/d_attachment/ijerph/ijerph-17-04909/article_deploy/ijerph-17-04909.pdf
- Hu 2023: 252 athletes, ages 10–14 to 25+, six provinces, team and individual sports, professional teams, cross-sectional; γ = −0.46; no direct effect on fear of failure; chain through constrained commitment; 14:1106916. https://frontiersin.org/articles/10.3389/fpsyg.2023.1106916/full
- Zhang, Du & Tao 2025: 325 athletes aged 12–18, China, two waves two weeks apart; resilience, optimism, coach-rated development; vol 15, 8 Jan 2025. https://www.frontiersin.org/articles/10.3389/fpsyg.2024.1433171/full
- Zhang, Wang & Shao 2022: 21 studies, 1,199 participants aged 5–19, 9 cross-sectional and 12 longitudinal; enjoyment r = 0.45 [0.42, 0.49], k = 4; coach support r = 0.43 [0.08, 0.69], k = 4; SMD 0.68 [0.27, 1.10], k = 5; intention SMD 1.13; enjoyment not pooled for persistence; sports as listed. https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2022.871936/full
- Smoll 2007: 17 + 17 teams, 34 coaches, 151 athletes aged 9–15 (mean 11.6), 82 and 69 analysed; 75- and 60-minute workshops; about 12 weeks; SAS-2 range 15–60; means 25.44 → 23.98 and 24.12 → 27.01; interactions for total, somatic, worry and concentration disruption; quasi-experimental; only athletes whose parents attended counted; no behavioural data; first author delivered the workshops; no effect sizes; guideline list; 2(1) 0701FA002. https://jyd.pitt.edu/ojs/jyd/article/view/358/344
- Tzioumakis 2026: 68 coaches, 36 and 32, four countries, randomised, MMCOS "validated", three points; about six hours; ages 10–15; disempowering and ego-involving behaviour reduced; autonomy and relatedness support "short-term, but not sustained"; no standardised effect sizes; no athlete outcomes; vol 17, 5 Aug 2026; listed authors. https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2026.1563931/full
- Smith 2015 (MMCOS): "preliminary support"; abstract does not list the coded dimensions; authors, 37(1):4–22, DOI. https://research.birmingham.ac.uk/en/publications/development-and-validation-of-the-multidimensional-motivational-c
- Deci 1999: 128 studies; tangible d = −0.34 [−0.39, −0.28], worse for children; verbal d = 0.43 [0.27, 0.58] in college students and d = 0.11 [−0.11, 0.34] in children; no sport tasks; 125(6):627–668; author order Deci, Koestner, Ryan. https://depts.washington.edu/techdocs/papers/deciExtrinsicRewardsAndIntrinsicMotivation99.pdf
- Adams 2024: 20 former college athletes, 9 sports, mean 26.0, range 19–44, United States, qualitative; most accepted some physical punishment; performance-tied conditioning distinguished from punitive; arbitrary, unsafe or cruel; injury and fear; title, 6:1428682. https://www.frontiersin.org/articles/10.3389/fspor.2024.1428682/full
- Lewis 2023: 48 analysed; non-disabled adults aged 18–40; RT+POS not different in retention; perceived competence rose in RT+POS and not in RT ONLY; author list. https://frontiersin.org/articles/10.3389/fpsyg.2022.1005705/pdf
- Haberstock 2024: 101 team-sport athletes, mean 28.68, age range not reported, 39.6% para-athletes, cross-sectional; peer disempowering climate predicts autonomy and relatedness frustration; 54(4):609–614. https://link.springer.com/article/10.1007/s12662-024-00980-4
- Stein 2012: 70 youth ice hockey players, cross-sectional; perceived–preferred feedback gaps with higher task and ego climate; no public or private feedback in the abstract; 13(4):484–490. https://lida.sport-iat.de/svd/Record/4024663?lng=en
- Fletcher & Sarkar 2016: notes 3 and 7 contain "the world's best athletes and teams", London 2012 and Rio, "extreme challenge-no support environments" and "the unethical and inappropriate imposition of adversity"; no model named; main text not visible. https://informahealthcare.com/doi/full/10.1080/21520704.2016.1255496
- Monteiro 2017: six studies, ages 5–30, four from Canada, studies from 1982 and 1985, mixed designs, the reasons listed, "controllable by the athletes", 727 in the text against 955 summed from the table; 5(3):50. https://pmc.ncbi.nlm.nih.gov/articles/PMC5968952
- Bergeron 2015: the quotations in sections 5, 7, 8 and 9 (except the hyphen noted above); authors; 49:843–851. World Rowing copy (URL above).
- Gustafsson 2011: multifaceted; process and state; model of antecedents, early signs, consequences, personality, coping and environment; "not to present the definitive model"; 4(1):3–24. https://informahealthcare.com/doi/full/10.1080/1750984X.2010.541927 and https://researchprofiles.canberra.edu.au/en/publications/athlete-burnout-an-integrated-model-and-future-research-direction/
- Meeusen 2013: functional overreaching recoverable within about two weeks; non-functional overreaching weeks to months; OTS "may take months or possibly years to completely recover"; diagnosis by exclusion; author list. Sportgeneeskunde copy (URL above).
- Gao 2024: 29 studies, 9,185 athletes, 2,191 parents, 26 quantitative and 3 qualitative, 82.8% cross-sectional; autonomy support, pressure (one opposite study: Amado et al.) and enjoyment findings; mixed results on parents against coaches; "the manner and extent of their involvement are key"; no pooled estimate; byline order; 14:1291711, 8 Jan 2024. https://frontiersin.org/articles/10.3389/fpsyg.2023.1291711/full
- Burke 2021: 12 studies, ages 5–18, quality 20–100%, all five quantitative studies significant, designs and measures prevent firm conclusions, no sport-specific measure of parent behaviour, pp. 208–235, online 7 Nov 2021. https://informahealthcare.com/doi/full/10.1080/1750984X.2021.1992793. Authors confirmed on https://pure.ulster.ac.uk/en/publications/enhancing-parental-support-through-parent-education-programs-in-y/

## References opened and not opened
- Opened (22): Mossman, Gómez-López, Gu & Cheng, Morales-Sánchez, Hu, Zhang–Du–Tao, Zhang–Wang–Shao, Smoll, Tzioumakis, Smith 2015 (record), Deci (copy), Adams, Lewis, Haberstock, Stein (index record), Fletcher & Sarkar (abstract and notes), Monteiro, Bergeron (copy), Gustafsson (abstract and record), Meeusen (copy), Gao, Burke. Also opened: Bartholomew 2009 (author manuscript) and Mossman (in-press manuscript).
- Not opened (1): Brenner & Watson (2024). PubMed served an empty page; no publisher URL came back from a search.
- Fetches refused or redirected, not retried: the MDPI XML page (bot check), two PMC and PubMed addresses (redirect or reCAPTCHA), the Sport Australia PDF (redirect), the McGill PDF (URL too long) and the Melbourne record (bot check).
