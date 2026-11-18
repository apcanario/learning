---
audit: fresh check
unit: SP5 · The cognitive-behavioural toolkit
course: sport-psychology · Sport Psychology for Coaches
model: claude-opus-5-5
date: 2026-11-18
chat: https://claude.ai/code/session_01KMmgQyRRZh9LyWjTQYMJfx
verdict: fix · 2 errors, 13 should-fix, 17 minor
---

The checker's final report, verbatim, from its hand-back. Saved before any finding was applied.

Verdict: SP5 · fix · 2 error, 13 should-fix, 17 minor

Model: claude-opus-5-5

The harness refused the write to out/report.md, so the full report is below.

# Fresh check · SP5 · The cognitive-behavioural toolkit

Checker: claude-opus-5-5, an isolated agent context that has not seen the unit written. Date: 18 Nov 2026.

- **Prompt:** audit-units-SKILL.md §3, with the figures paragraph (section 7). Errata: no audit report: skip it. Brief: brief.txt.
- **Web:** live search on. Every URL fetched was returned verbatim by a WebSearch in this session. A refused fetch was recorded as "not opened" and not fetched from a copy.
- **Not opened** (fetch refused by the session's permission check):
  - Reinebo et al. 2024: refused at the Springer PDF, then at PMC and PubMed.
  - Walter et al. 2019: refused at PMC and at the MDPI XML.
  - Every claim resting on these two is "unverifiable", not PASS.
- **Not checked:** pointers to SP1–SP4. Those units are not in the folder.

## Findings

[error] [attribution] 3.1 Goal setting; Current: "Its authors call the time goal an outcome goal; under this unit's definitions, a target time from one's own record is a performance goal."; Problem: the paper never calls the goal an outcome goal. It calls it a "time-based performance goal" throughout (abstract, methods, discussion, conclusion), and "outcome" appears only in a table caption. notes.md contradiction 5 rests on the same misreading; Fix: "Its authors call it a time-based performance goal, which matches this unit's definition of a performance goal."; Basis: Ferchichi et al. 2026, full text, https://public-pages-files-2025.frontiersin.org/journals/sports-and-active-living/articles/10.3389/fspor.2026.1759066/pdf
[error] [accuracy] 3.5 Grade; Current: "[moderate, positive, for learning and performing sport skills in mostly adult samples; meta-analyses that fail rule 3 on bias and heterogeneity, rule 4; in athlete samples one small meta-analysis found no significant difference; inference for under-18s]"; Problem: the brief's key gives moderate only for evidence in athletes, and the unit's own wording of rule 4 is "meta-analyses in athletes". Favre-Bulle (566 healthy adults, novices in all but one study) and Zang (physically fit participants) are not athlete samples, and the one meta-analysis in athletes found no difference. Under the key this is weak (studies outside sport); contested is the alternative if SP1's rule 1 counts disagreeing reviews; Fix: "[weak, positive, for learning sport skills in mostly novice non-athlete adults (outside the athlete samples the key's moderate grade asks for), rule 5; in athlete samples one small meta-analysis found no significant difference; inference for under-18s]"; Basis: Favre-Bulle et al. 2024, https://peerj.com/articles/17799.pdf; Zang et al. 2025, https://peerj.com/articles/20012; brief.txt grade key
[should-fix] [accuracy] Deliverable A, Milan week 5; Current: "[moderate, positive; mostly adult samples, so inference]"; Problem: carries the 3.5 misgrade; Fix: "[weak, positive; mostly novice adult samples, so inference]"; Basis: as above
[should-fix] [accuracy] Deliverable A, Milan week 6; Current: "[moderate, positive; inference] |"; Problem: carries the 3.5 misgrade; Fix: "[weak, positive; inference] |"; Basis: as above
[should-fix] [accuracy] Card 5 Grade; Current: "[moderate, positive; mostly adults; inference under 18]. In athlete samples, one small meta-analysis found no significant difference."; Problem: carries the 3.5 misgrade; Fix: "[weak, positive; mostly novice adults; inference under 18]. In athlete samples, one small meta-analysis found no significant difference."; Basis: as above
[should-fix] [label] 3.2 Grade; Current: "so it covers 13 to 25; for 10 to 12 outside the sampled ages]"; Problem: the sample stopped at 23. The preamble keeps "outside the sampled ages" for evidence from younger athletes applied to older bands. Here an older sample (13 to 23, including adults) is applied to younger children, which the brief labels inference; Fix: "so it covers 13 to 23; for 10 to 12 an inference from older athletes]"; Basis: unit preamble; brief.txt (Ages); sources.md row 13
[should-fix] [label] 3.4 Breathing; Current: "In 35 students who were not athletes (mean age 21.7)"; Problem: the paper does not say the participants were not athletes. It describes 35 healthy right-handed adults from kinesiology courses and reports no athletic status; Fix: "In 35 healthy kinesiology students whose athletic status was not reported (mean age 21.7)"; Basis: Buchanan & Janelle 2022, Participants, https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2022.963711/pdf
[minor] [label] 3.4 Grade; Current: "laboratory studies in sport students and non-athletes, one with fewer errors"; Problem: same as above; Fix: "laboratory studies in sport students and kinesiology students, one with fewer errors"; Basis: as above
[minor] [label] 3.4 Grade; Current: "[weak; one laboratory study in non-athletes, rule 5; inference]"; Problem: same as above; Fix: "[weak; one laboratory study in students not described as athletes, rule 5; inference]"; Basis: as above
[minor] [label] Card 4 Tested on; Current: "35 non-athletes ("; Problem: same as above; Fix: "35 kinesiology students, athletic status not reported ("; Basis: as above
[minor] [label] Card 4 When not to use it; Current: "[weak; one laboratory study in non-athletes; inference]"; Problem: same as above; Fix: "[weak; one laboratory study in students not described as athletes; inference]"; Basis: as above
[minor] [label] Deliverable A, Sara week 4; Current: "not just before a reaction start [weak; inference from non-athletes]"; Problem: same as above; Fix: "not just before a reaction start [weak; inference from a laboratory study in students]"; Basis: as above
[should-fix] [accuracy] 3.4 Relaxation; Current: "14 trained, 10 controls; assignment by gender, with two replacements"; Problem: groups were randomised within gender and some participants were replaced after randomisation. "Assignment by gender" reads as allocation by sex; Fix: "14 trained, 10 controls; randomised within gender, with participants replaced after randomisation"; Basis: Liang et al. 2021, https://www.frontiersin.org/articles/10.3389/fpsyg.2020.617541/full
[should-fix] [accuracy] 3.2 Self-talk; Current: "neither kind changed three-point shooting, in quiet or under noise, and the two kinds did not differ"; Problem: the main and interaction effects were null, as the unit says. But the authors read, from simple effects, that self-talk buffered the effect of noise on static shots (only the control group dropped under noise), and their abstract says so; Fix: "neither kind changed three-point shooting against no self-talk, in quiet or under noise (no significant intervention effect or interaction; the authors read a buffering of noise on static shots from simple effects), and the two kinds did not differ"; Basis: Yang et al. 2024, https://www.frontiersin.org/journals/sports-and-active-living/articles/10.3389/fspor.2023.1304911/pdf
[should-fix] [label] 5 Offer the alternative to control; Current: "offer the acceptance approach in section 3.6 [moderate, positive; inference under 16]"; Problem: the moderate grade is for mindfulness and acceptance effects on performance. No source opened tests offering the approach to athletes whose control strategies have failed, so that targeting is practice; Fix: "offer the acceptance approach in section 3.6 [practice, for offering it to this athlete; the approach itself moderate, positive; inference under 16]"; Basis: Bühlmayer et al. 2017 abstract; Noetel et al. 2019 abstract (neither tests the targeting)
[should-fix] [attribution] 1 The model; Current: "a narrative review, outside the source types the course lists, so no grade rests on it)"; Problem: Part 7 allows only these source types: consensus statements, systematic reviews or meta-analyses, primary studies, textbooks by edition and chapter, and issuing-body pages. A mechanism claim rests here on a narrative review alone. Either label it as held to a lower standard, or replace it with a standard textbook chapter, opened; Fix: "a narrative review, outside the source types the course lists: the model is reported as this review states it, and no grade or recommendation rests on it)"; Basis: sourcing-standard.md Part 7, line 2; Turner 2016 ("REVIEW article"), https://frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2016.01423/full
[should-fix] [deliverable] Deliverable A, Milan week 2; Current: "Tue: same goal in a scored 5-a-side, goals by count of process actions, not only by goals scored. Thu: each player writes one process goal for the first fifteen minutes of Saturday's match."; Problem: section 4 says a skill is used "first in a competition that matters less", and the template asks which competitions are "lower-stakes enough for a first use". Milan's block sends every skill straight into the next weekly match with no such check, in the season that ends in his retention decision (case-facts); Fix: "Tue: same goal in a scored 5-a-side, goals by count of process actions, not only by goals scored. Thu: each player writes one process goal for the first fifteen minutes of Saturday's match if you judge it lower-stakes; if not, the first use waits for the next match that is."; Basis: unit section 4, stage 4; case-facts.md (Milan)
[should-fix] [attribution] Sources, Favre-Bulle; Current: "- Favre-Bulle et al. The effectiveness"; Problem: the author list is incomplete. The publisher's PDF gives all six authors, so the source log's note that the page shows only the first author no longer holds; Fix: "- Favre-Bulle E, Nyfeler S, Schorderet C, Risso G, Bassolino M, Sattelmayer KM. The effectiveness"; Basis: https://peerj.com/articles/17799.pdf
[should-fix] [figure] 1, flow viz caption; Current: "The notes give where each skill in section 3 enters; the example thought is Milan's (fictional) from SP4."; Problem: the figure shows no example thought (its Thought note is "goals, self-talk"); Fix: "The notes give where each skill in section 3 enters; the situation note is Milan's (fictional) first fifteen minutes."; Basis: unit section 1; the figure's JSON
[should-fix] [figure] 4, flow viz caption; Current: "The four stages of teaching a skill, as section 4 of this unit sets them out [practice]."; Problem: the figure has five steps; the fifth ("Keep it going") comes from section 4's "How long" paragraph; Fix: "The four stages of teaching a skill, as section 4 of this unit sets them out [practice], and the keeping-going step that section 4 adds after them."; Basis: unit section 4
[minor] [figure] 3.6, matrix viz caption; Current: "Buchanan & Janelle (2022), about 22"; Problem: the text gives mean 21.7, and "about 22" is not in the unit's text; Fix: "Buchanan & Janelle (2022), mean 21.7"; Basis: unit section 3.4
[minor] [accuracy] 3.3 Imagery; Current: "and speed not significantly, with certainty low to very low."; Problem: GRADE rates both serve accuracy and serve speed low. Only serve technique is rated very low; Fix: "and speed not significantly, with certainty low for both (very low for serve technique)."; Basis: Deng et al. 2024, Table 1 and abstract, https://mdpi.com/2076-328X/14/3/207
[minor] [accuracy] Card 3 Grade; Current: "For ages 9 to 18: tennis serve accuracy, low to very low certainty."; Problem: as above; Fix: "For ages 9 to 18: tennis serve accuracy, low certainty."; Basis: as above
[minor] [accuracy] Card 2 Tested on; Current: "117 athletes aged 13 to 23 in eight sports"; Problem: section 3.2 lists seven sports, so the card and the body disagree (Walter not opened by me); Fix: "117 athletes aged 13 to 23 in individual and team sports"; Basis: unit section 3.2; sources.md row 13
[minor] [accuracy] 5 opening; Current: "the meta-analyses report heterogeneity for every skill above"; Problem: no meta-analysis was opened for goal setting or self-talk; Fix: "the meta-analyses opened report heterogeneity or wide intervals for the skills they pooled"; Basis: unit sections 3.1, 3.2
[minor] [label] 4 How long; Current: "mindfulness programmes from 4 weeks to over 2 years ([Bühlmayer et al., 2017](https://doi.org/10.1007/s40279-017-0752-9))"; Problem: the claim rests on an abstract alone and does not say so (Part 7, line 4); Fix: "mindfulness programmes from 4 weeks to over 2 years ([Bühlmayer et al., 2017, abstract read](https://doi.org/10.1007/s40279-017-0752-9))"; Basis: sources.md row 3
[minor] [label] Card 6 Tested on; Current: "Nine controlled trials, 290 athletes over 15 in 13 sports ([Bühlmayer et al., 2017](https://doi.org/10.1007/s40279-017-0752-9)); 66 studies, 3,908 athletes, none at low risk of bias ([Noetel et al., 2019](https://doi.org/10.1080/1750984X.2017.1387803))."; Problem: both rest on abstracts alone and are not marked; Fix: "Nine controlled trials, 290 athletes over 15 in 13 sports ([Bühlmayer et al., 2017, abstract read](https://doi.org/10.1007/s40279-017-0752-9)); 66 studies, 3,908 athletes, none at low risk of bias ([Noetel et al., 2019, abstract read](https://doi.org/10.1080/1750984X.2017.1387803))."; Basis: sources.md rows 3, 4
[minor] [label] Card 4 Tested on; Current: "measuring heart-rate variability ([Laborde et al., 2022](https://doi.org/10.1016/j.neubiorev.2022.104711))"; Problem: read in abstract and parts of the text only, not marked; Fix: "measuring heart-rate variability ([Laborde et al., 2022, abstract and parts of the text read](https://doi.org/10.1016/j.neubiorev.2022.104711))"; Basis: sources.md row 8
[minor] [figure] 3.4 What it is; Current: "Slow breathing usually means about six breaths a minute with a longer out-breath."; Problem: the number has no citation; Fix: "Slow breathing in the studies opened means about six breaths a minute; one paced a longer out-breath (4.5 seconds in, 5.5 out) ([Laborde et al., 2019](https://doi.org/10.3389/fpsyg.2019.01923))."; Basis: Laborde et al. 2019, https://frontiersin.org/articles/10.3389/fpsyg.2019.01923/pdf
[minor] [accuracy] 3.5 Adults learning sport skills; Current: "566 healthy adults aged 18 to 65, mostly novices"; Problem: 18 to 65 was the eligibility range; the reported mean ages ran from about 19 to 27; Fix: "566 healthy adults (eligible from 18 to 65; reported mean ages about 19 to 27), mostly novices"; Basis: Favre-Bulle et al. 2024, https://peerj.com/articles/17799.pdf
[minor] [attribution] Sources, Brown & Fletcher; Current: "*Sports Medicine* 2017;47:77–99."; Problem: the issue number is missing. The publisher's partner page shows issue 1/2017; it does not show volume or pages, and I did not verify those; Fix: "*Sports Medicine* 2017;47(1):77–99."; Basis: https://www.springermedizin.de/effects-of-psychological-and-psychosocial-interventions-on-sport/12118340
[minor] [style] Deliverable A, Milan within the block; Current: "the coach's example for him (*added*: Milan chose the phrase "Scan, open, forward") is listed in the notes"; Problem: the sentence calls the phrase both the coach's example and Milan's own choice; Fix: "the phrase he chose (*added*: "Scan, open, forward") is listed in the notes"; Basis: notes.md case fact 3

## Confirmed

- **Brown & Fletcher 2017:** PASS (abstract). https://www.springermedizin.de/effects-of-psychological-and-psychosocial-interventions-on-sport/12118340
  - g = 0.57 (0.22–0.92; k = 35, n = 997).
  - Follow-up g = 1.16 (0.25–2.08; k = 8, n = 189), 1 to 4 weeks after the intervention.
  - "Some evidence" that coach-delivered interventions had the greatest effects.
  - No ages in the abstract.
- **Lochbaum & Lane 2025:** PASS. https://www.mdpi.com/2075-4663/13/12/420
  - 73 meta-analyses, published 1988–2025.
  - Confidence effects 0.25–0.30.
  - Three anxiety meta-analyses "negligible or unreliable".
  - Process-goal setting, mindfulness and PST "often produced effects in the medium-to-large range"; short-term breathing manipulations negligible or inconsistent.
  - The "vastly different effect size values across process, performance, and outcome goals" quote is exact.
  - No quality appraisal and no pooling; athletes "from youth to elite levels"; the tables are images.
  - Lochbaum and Lane are both authors of the 2022 review.
- **Ferchichi 2026:** PASS, apart from the outcome-goal finding.
  - 24 male swimmers, 15.2 ± 0.8, top 30 nationally, randomised 12/12, eight weeks.
  - 4.3% against 2.5% improvement (interaction p = 0.004).
  - Total mood disturbance +47.1% against +19.1%.
  - Process goals were not tested.
  - The paper is internally inconsistent (2.6% in its Discussion; the TMD percentages do not match its table means). The unit uses the Results figures.
- **Liu 2025:** PASS. https://www.mdpi.com/2076-328X/15/5/685/html
  - 86 randomised studies, 3,593 athletes, 10 studies without ages.
  - SMD 0.5 (0.34–0.67); GRADE low; over half of studies at unclear risk.
  - Funnel plot asymmetric; S-value: no plausible bias nullifies the effect.
  - Moderators: duration 0.62 / 0.47 / 0.38; frequency 0.59 / 0.09 / −0.13; session length 10 min 0.51, 20 min 0.22, 45 min 0.93 (−0.10 to 2.11); imagery combined with other skills larger.
  - No age result found.
- **Deng 2024:** PASS, apart from the certainty finding. https://mdpi.com/2076-328X/14/3/207
  - 9 trials, 548 participants aged 9–18, beginners to national level.
  - Serve accuracy g = 0.99 (0.68–1.30); speed not significant.
  - Programmes 4–24 weeks (mean 10.9), 1–3 sessions a week, 3–25 min a session (mean 13.3).
- **Behrendt 2021:** PASS. https://www.mdpi.com/1660-4601/18/18/9467
  - 22 RCTs, 934 participants aged 9–18, populations as the unit states.
  - Two studies pooled, SMD 0.83–1.87; risk of bias from some concerns to high; GRADE low.
  - The "high potential" conclusion is as stated.
- **Yang 2024:** PASS, apart from the finding. https://www.frontiersin.org/journals/sports-and-active-living/articles/10.3389/fspor.2023.1304911/pdf
  - 42 male university players, mean age 20.93, randomised to instructional, motivational or no self-talk.
  - No intervention effect; the two kinds did not differ.
- **Laborde 2022:** PASS (abstract, on the repository record returned by search). https://pure.solent.ac.uk/en/publications/effects-of-voluntary-slow-breathing-on-heart-rate-and-heart-rate-/
  - 223 studies.
  - vmHRV rose during breathing, immediately after one session, and after multi-session programmes.
- **Laborde 2019:** PASS. https://frontiersin.org/articles/10.3389/fpsyg.2019.01923/pdf
  - Sport-university students, 107 analysed, ages 18–41; sport background not assessed.
  - One 17-minute session at about 6 breaths a minute, against a documentary, after burpees.
  - Stroop errors 0.36 against 0.69; no effect on reaction time or perceived stress; RMSSD not a mediator.
  - The authors' "quick fix" wording is as the unit reports it.
- **Buchanan & Janelle 2022:** PASS on the values (the label is a finding).
  - n = 35, mean age 21.68.
  - Slow breathing raised SDNN and slowed reaction time; fast breathing raised errors and breathlessness.
- **Liang 2021:** PASS, apart from the assignment wording.
  - 24 athletes, about 21 years, before the provincial college games.
  - Self-confidence g = 0.8 and 1.0 at weeks 1–2 only; no anxiety differences.
  - Personal bests 7/14 against 2/10, one-sided p = 0.074.
- **Battaglini 2022:** PASS (abstract page).
  - 59 players aged 14–19 at one club; 12 sessions.
  - Heart rate fell against control (p < 0.01); baseline difference in cognitive anxiety; assignment not stated.
- **Favre-Bulle 2024:** PASS.
  - 12 trials, 566 participants, mostly novices; sports as listed.
  - Retention 0.56 (0.20–0.92); transfer 0.35 (0.02–0.68).
  - Blinding at high risk in all studies or all but one, depending on the item; post-acquisition I² 71.3%.
- **Zang 2025:** PASS. https://peerj.com/articles/20012
  - 20 RCTs, 497 participants, one study of children (mean age 7.35).
  - Distal external against internal 0.59 (0.14–1.05); proximal external against internal 0.32 (0.13–0.51).
  - The benefit of distance appears in experienced performers.
  - The "no evidence that novices can benefit..." quote is exact.
- **Bühlmayer 2017:** PASS (abstract). https://link.springer.com/doi/10.1007/s40279-017-0752-9
  - 9 trials, 290 participants over 15; PEDro 5.4 ("fair").
  - Mindfulness 1.03 (90% CI 0.67–1.40); psychological measures 0.72 (0.46–0.98); shooting and darts 1.35 (0.61–2.09), I² 82%.
  - Programmes 4 weeks to over 2 years.
- **Noetel 2019:** PASS (abstract). https://informahealthcare.com/doi/abs/10.1080/1750984X.2017.1387803
  - 66 studies, n = 3,908; large effects in randomised trials against no treatment; evidence graded low quality.
  - The "None of the included studies were rated as having a low risk of bias" quote is exact.
- **Turner 2016:** PASS. https://frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2016.01423/full
  - "original cognitive-behavior therapy (CBT) by many scholars".
  - The ABC framework is as the unit states it.
  - The "ethically beyond many practitioners' professional competencies" quote is exact; the practitioners meant are sport psychologists.
- **Unverifiable (not opened):**
  - Every Reinebo 2024 value in sections 2, 3.3, 3.5, 3.6 and 4, including figure 2's three Reinebo rows.
  - Every Walter 2019 value in sections 3.2, 4, 5 and 6.
- **Not checked:** the SP1, SP3 and SP4 pointers (the grade-key rule texts, the SP1 section 6 values d = 0.51 and −0.21, the ironic-effects grade, the self-focus account, the scope card, the normal-or-refer table). Those units are not in the folder.

## Section 7 · Figures

1. **Flow, section 1: FIX (caption).** The labels and notes trace to section 1. The kind fits. The caption claims an example thought the figure does not show.
2. **Range, section 2: PASS.** All eight rows match the text, and the 90% interval is noted. The caption names the sections and sources. The kind fits competing estimates. The Reinebo rows are unverifiable at source.
3. **Matrix, section 3.6: FIX (caption, minor).** The cells agree with the samples named in the caption. "About 22" is not in the text.
4. **Flow, section 4: FIX (caption).** The steps trace to section 4 and Deliverable A. The caption says four stages; the figure has five steps.

## The seven passes

1. **Claims: FAILED.** I opened 17 of the 19 sources.
   - One FAIL: the Ferchichi outcome-goal attribution.
   - Three stretches: Yang, Liang, Buchanan.
   - Reinebo and Walter unverifiable. The rest PASS.
2. **Bibliography: PASSED, with should-fix.** No reference found that does not exist.
   - Full PASS: Battaglini, Behrendt, Buchanan, Deng, Ferchichi, Laborde 2019, Liang, Liu, Lochbaum & Lane, Noetel (2019;12(1):139–175 on the LIDA record returned by search), Turner, Yang.
   - Bühlmayer: 47(11):2309–2321 confirmed; the order of the last two authors is not confirmed.
   - Laborde 2022: volume 138 not shown on the page I opened.
   - Brown & Fletcher: issue missing (finding).
   - Favre-Bulle: authors incomplete (finding).
   - Zang: authors not verified (PDF fetch refused).
   - Reinebo and Walter: not opened.
3. **Source log: FAILED (minor).**
   - All 19 Sources entries have a row in sources.md.
   - Abstract-only labels are missing in section 4 and Cards 4 and 6.
   - The log's Favre-Bulle note is contradicted by the publisher's PDF.
4. **Grades: FAILED.** Checked against the key as quoted in the brief and the preamble; the text of rules 1–5 is not in the folder.
   - Attentional focus graded moderate on non-athlete samples: error, carried into Milan weeks 5–6 and Card 5.
   - Section 5 gives the acceptance offer a grade that does not cover it.
   - Self-talk weak (two studies, "several" meaning three or more), imagery, mindfulness and packages moderate, breathing and relaxation weak, and F1 (nothing strong) are all consistent with the key.
5. **Population: FAILED (should-fix).**
   - Self-talk for ages 10 to 12 is mislabelled "outside the sampled ages".
   - Buchanan's sample is called "non-athletes" in six places.
   - Every other finding names its sample, and transfers to younger athletes are labelled inference.
6. **Scope and safety: PASSED.**
   - Nothing teaches assessment, diagnosis or treatment.
   - Stop-and-refer appears in sections 1 and 5 and on every card.
   - No weight-loss method, calorie figure or target weight; no method of self-harm; no law stated.
   - The disclaimer is the first line; no real person is named as an example.
   - Breathing is never turned into a performance claim (section 3.4, Sara week 3, Card 4).
   - Scripts are labelled as examples throughout.
7. **Any sport: PASSED.**
   - About 34 examples outside the case blocks: football about 7, athletics about 7, swimming 5, tennis 5, judo 3, rowing 2, and one each for gymnastics, cycling, volleyball, basketball and golf.
   - No sport exceeds a third, with or without the case deliverables.
   - No owner-identifying detail found. kit/private_terms.py is not in the folder, so I did not run it.

## Coverage

All brief items are covered, with these exceptions:

- **Thin, and the unit says so:** what the goal-setting meta-analysis found for each kind of goal (Williamson not opened).
- **Practice only, and the unit says so:** matching instructional and motivational self-talk to the task (reviews not opened).
- **Deliverable:** the eight-week block for Milan's squad and for Sara, six skill cards and two templates are all complete. The one gap is the lower-stakes first use in Milan's block (finding).

## Part 7, line by line

- **Yes:** source types other than Turner; no banned sources; sample and design stated; effect sizes in the source's terms; coach's part; weight and self-harm; no law, disclaimer present; no real person named; three or more kinds of sport, none over a third; case facts agree with case-facts.md, are labelled "(fictional)" and are never used as evidence; deliverable built in full and as a template; links as DOI links; the unit does not read as advice without evidence.
- **Exceptions:**
  - Turner is outside the allowed source types (should-fix).
  - Abstract-only labels are partly missing.
  - Two bibliography entries are incomplete.
  - The attentional-focus grade does not follow the key.
  - One inference label is wrong.
  - The breathing-rate definition is uncited.
  - The popular-claims list (seed bibliography) is not in the folder, so that line was not checked further.

## Read as the coach in the preamble

The block is usable on a phone and reads in order. The scripts are short and say what to do, and the breathing script is honest about what breathing does. A coach of Milan's squad would ask which Saturday counts as "matters less". A coach could also take the attentional-focus cards as better evidenced than they are.

## For the maintainer (outside the unit)

- notes.md contradiction 5 rests on the Ferchichi misreading.
- notes.md Needs 2 (F1): after the regrade, the moderate list no longer includes attentional focus.
- sources.md row 17: Favre-Bulle's full author list is on the publisher's PDF.
- Reinebo and Walter need opening in a session that can reach them.

Verdict: SP5 · fix · 2 error, 13 should-fix, 17 minor
