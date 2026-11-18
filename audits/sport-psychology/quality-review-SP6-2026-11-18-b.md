Verdict: SP6 · fix · 1 error, 9 should-fix, 6 minor

(The harness blocked the agent's write to out/report.md; the agent returned the full report as its reply and the chat saved it verbatim.)

Model: claude-opus-5-5. Quality review (public-courses rule 13, F92) of SP6 · Training under pressure. Packet: /tmp/w/qr-SP6. Live search run 2026-11-18.
- Prompt: audit-units-SKILL.md section 3 with its figures paragraph.
- Brief: brief.txt.
- Standard: sourcing-standard Part 1 and Part 7.
- Audit errata: none in the packet, so skipped.
- The writer's notes and unsure files were withheld. I started from the unit's own unsure list (lines 330–347).

## Findings

[error] [figure] Section 2, figure 1 (range), debrief row; Current: ", {"label": "Debriefs, outside sport (Tannenbaum & Cerasoli)", "low": 0.67, "high": 0.67, "point": 0.67, "tone": 5}"; Problem: the row draws an interval from 0.67 to 0.67. The unit's text says the paper gives no 95% CI for d = 0.67, so these bounds are not in the text (the paper gives only an 80% credibility interval). A zero-width interval reads as a precise estimate, and the row puts d on an axis of g and SMC; Fix: "" (delete the row); Basis: Tannenbaum & Cerasoli 2013, full text, https://cebma.org/assets/Uploads/Tannenbaum-Cerasoli.pdf
[should-fix] [figure] Section 2, figure 1 caption; Current: "Pooled effects from sections 2, 5 and 10 of this unit: point estimate and 95% confidence interval, Hedges' g except the pre-post routine row (standardised mean change) and the debrief row (d; the paper reports no 95% confidence interval for it). Pressure training: Low et al. (2021), accepted manuscript, without the outlying study. Pre-performance routines: Rupprecht et al. (2024). Debriefs: Tannenbaum & Cerasoli (2013), outside sport, full text read on a CEBMA copy."; Problem: the caption must match the figure once the debrief row is removed; Fix: "Pooled effects from sections 2 and 5 of this unit: point estimate and 95% confidence interval, Hedges' g except the pre-post routine row (standardised mean change). Pressure training: Low et al. (2021), accepted manuscript, every row without the outlying study, intervals from the results section. Pre-performance routines: Rupprecht et al. (2024). The debrief effect (section 10, d = 0.67) is not drawn: the paper gives no 95% confidence interval for it."; Basis: unit sections 2 and 10; https://repository.essex.ac.uk/26305/3/PressureTrainingForPerformanceDomains.pdf
[should-fix] [label] Section 2, "On whom"; Current: "The paper gives no mean ages. So the samples are mostly adults, with one youth sample whose ages the paper does not give."; Problem: the meta-analysis reports no ages. "Mostly adults" is the unit's inference, stated as a finding. Only the police samples are known to be adults; Fix: "The paper gives no mean ages. The police samples are adults and one sample is elite youth cricketers of unstated ages; for the other sport samples the meta-analysis gives no ages."; Basis: Low et al. 2021 accepted manuscript, https://repository.essex.ac.uk/26305/3/PressureTrainingForPerformanceDomains.pdf
[should-fix] [label] Section 2, Grade; Current: "samples mostly adults, with one elite youth sample of unstated ages, so for athletes under 18 an inference"; Problem: the same unsupported "mostly adults"; Fix: "sample ages mostly not given (police adults; one elite youth sample of unstated ages), so for athletes under 18 an inference"; Basis: as above
[should-fix] [label] Section 3, closing recommendation; Current: "[weak, for consequences and judgement creating felt pressure; practice, for adding demands as texture]"; Problem: the recommendation rests on one study of six adults. The table rows label it an inference for under-18s; the recommendation itself does not (Part 7); Fix: "[weak, for consequences and judgement creating felt pressure; one study of six adults, so for under-18s an inference; practice, for adding demands as texture]"; Basis: Stoker et al. 2019 manuscript, https://researchonline.ljmu.ac.uk/id/eprint/13095/1/Effect%20of%20pressure%20training%20manipulations%20pressure.pdf
[should-fix] [attribution] Section 6, sample details; Current: "SP4 read more of the same review:"; Problem: the figures that follow (62%, mean ages 20 to 40 in 68%, four competition studies, medium quality) come from SP4's reading and were not re-opened for this unit (the unit's unsure item 3). The text does not say so (Part 1: keep the reporter separate from the claim); Fix: "SP4 read more of the same review (SP4's reading, not re-read for this unit):"; Basis: unit unsure list item 3; the LIDA abstract https://lida.sport-iat.de/ta/Record/4055257 shows none of these figures
[should-fix] [label] Deliverable A, Milan's squad; Current: "Milan: his referral to the academy's medical staff is under way (SP4, SP5), so his cap is 3;"; Problem: case-facts.md has no fact that Milan's referral is under way (SP1 records only that the academy has medical staff). The fact is not in the register and not marked added; Fix: "Milan: his referral to the academy's medical staff is under way (SP4, SP5; *added* to the register by this unit), so his cap is 3;"; Basis: case-facts.md (packet)
[should-fix] [label] Deliverable B, Sara; Current: "Her referral by her SP1 scope card is under way, so"; Problem: the register has no fact that Sara's referral is under way (SP1 records only that her university has a health or counselling service). Not marked added; Fix: "Her referral by her SP1 scope card is under way (*added*), so"; Basis: case-facts.md (packet)
[should-fix] [label] Deliverable A, Dani's squad; Current: "The squad did not run SP5's block."; Problem: this is a new case fact, also used in section 12. It is not in the register and not marked added; Fix: "The squad did not run SP5's block (*added*)."; Basis: case-facts.md: SP5's added facts cover Milan's and Sara's squads only
[should-fix] [coverage] Unsure list, added facts; Current: "the self-talk phrase "Arms, tall, through". Object: none"; Problem: the added-facts list leaves out the three facts above, so they would not reach the register (the brief requires invented case facts to be listed in the notes); Fix: "the self-talk phrase "Arms, tall, through"; Dani's squad did not run SP5's block; Milan's referral to the academy's medical staff is under way and they have not yet seen him; Sara's referral through her SP1 scope card is under way. Object: none"; Basis: brief.txt (running case); case-facts.md
[minor] [figure] Section 2, figure 1, first row label; Current: ""Pressure training, all domains (Low)""; Problem: the row shows the outlier-removed estimate (0.67), but section 2's all-domains estimate is 0.85, so the label alone misleads; Fix: ""Pressure training, all domains, outlier removed (Low)""; Basis: Low et al. 2021, Essex PDF above
[minor] [accuracy] Section 2, basketball study; Current: "a cap on attempts and team sprints after misses"; Problem: the cap (six attempts) applied only in some free-throw sessions; Fix: "a cap on attempts in some sessions and team sprints after misses"; Basis: Kegelaers et al. 2021 full text, https://core.ac.uk/download/387931251.pdf
[minor] [style] Section 3 table, Consequences; Current: "Forfeits and rewards each appeared in 4 and 6 of the 14 pooled studies"; Problem: "each ... 4 and 6" is garbled; Fix: "Forfeits appeared in 4 and rewards in 6 of the 14 pooled studies"; Basis: Low et al. 2021 (forfeits k = 4, rewards k = 6), Essex PDF above
[minor] [figure] Section 2, "On whom"; Current: "Fourteen studies, 394 participants:"; Problem: the abstract's 394 conflicts with Table 1's per-study total of 399, and the unit flags this only in the unsure list; Fix: "Fourteen studies, 394 participants (the abstract's figure; Table 1's per-study numbers sum to 399):"; Basis: Low et al. 2021, Essex PDF above
[minor] [label] Deliverable A, Dani week 4 script; Current: "the way it'll be on Saturday"; Problem: the register says only "at the weekend"; "Saturday" is a further invented detail; Fix: "the way it'll be at the weekend"; Basis: case-facts.md, SP6 row
[minor] [label] Section 6 table, quiet eye; Current: "pooled 3 quiet-eye samples among its stand-alone routines, and routine type did not moderate the effect; this review's count per technique not seen]"; Problem: the moderate grade rests on a non-significant type moderator, not on an estimate for quiet eye (3 samples), and a null moderator does not show an equal effect. The left-hand row refers to this one, so the same applies there; Fix: "pooled 3 quiet-eye samples among its stand-alone routines, and routine type did not moderate the effect; no separate quiet-eye estimate was read, and a null moderator does not show an equal effect; this review's count per technique not seen]"; Basis: Rupprecht et al. 2024, https://informahealthcare.com/doi/abs/10.1080/1750984X.2021.1944271

Each Current string was checked by script against unit.md and occurs exactly once.

## (7) Figures

1. Range, section 2: **FIX** (the error, caption and label findings above).
   - Rows 1–6: every number traces to the text. Low et al.: 0.67/0.41/0.94, 0.72/0.45/1.00 and 0.63/−0.14/1.39 (line 32). Rupprecht et al.: 0.70/0.24/1.16, 0.64/0.45/0.83 and 0.31/0.18/0.44 (line 94).
   - The kind fits competing estimates.
2. Compare, section 3: **PASS**. 1.83, 2.8, 4.5 and 4.9 trace to line 55 and match the source. The caption names the section and the source; the kind fits.
3. Flow, section 9: **PASS**. The labels trace to the ladder table (lines 141–148). The caption says the ladder is untested; the kind fits a sequence.
4. Decision, section 9: **PASS**. The outcomes trace to the step-down rule (lines 169–175). The caption declares the reading order; the kind fits a rule with branches.

## Pass: Claims (each source opened in this run)

**Oudejans & Pijpers 2009.** Abstract on the VU record, https://research.vu.nl/en/publications/training-with-anxiety-has-a-positive-effect-on-expert-perceptual--2/
- PASS: 17 basketball players, 17 darts players, five weeks; only the groups trained with anxiety held up; the adaptation explanation is attributed to the authors.

**Low et al. 2021.** Accepted manuscript, https://repository.essex.ac.uk/26305/3/PressureTrainingForPerformanceDomains.pdf (the Sheffield Hallam copy was blocked: not checked).
- PASS, study and samples: definition; inclusion criteria; 14 studies and 394 participants; 10 sport and 4 law-enforcement studies; the sports listed; elite youth cricketers; no mean ages.
- PASS, pooled effects: g = 0.85 [0.37, 1.34], I² 78.4%; outlier removed, 0.67, I² 17.1%; the CI conflict (0.41–0.94 in the results, 0.43–1.12 in the abstract).
- PASS, subgroups: sport 0.72 [0.45, 1.00], k 10; police 0.63 [−0.14, 1.39], k 3; novices 0.77, k 5; experienced 0.61, k 8; by sessions 0.73 (k 6), 0.72 (k 4), 0.42 (k 3, CI crossing zero).
- PASS, bias and limits: Egger p = .12; risk of bias mostly unclear; one retention test; one competition study (overall performance only); the limitations; controls "physically practiced as much as".
- FAIL as stated: "mostly adults" (finding above).
- Unverifiable: that the law-enforcement tasks were "all shooting". The source summary says shooting and decision tasks.

**Kent et al. 2021.** Accepted manuscript, https://eprints.glos.ac.uk/9339/1/9339-Kent-(2021)-Implementing-a-pressure-training-program.pdf
- PASS, sample: 82 males aged 11–18, mean 14.12, randomly allocated.
- PASS, programme: three pressure sessions over 18 weeks; 2v2; crowd noise; leaderboard; rewards; dice-roll consequences; sprints for ages 15–18; three 30-minute workshops (15 for ages 17–18); diaries.
- PASS, results: χ² = 7.15, p = .028; no difference in execution; 68 and 26 retested; "partial support"; protection from harm; results not used for contract decisions.
- Unverifiable: "coach-rated" was not in the parts returned.

**Kegelaers et al. 2021.** Full text, https://core.ac.uk/download/387931251.pdf
- PASS, design: 19 recruited, 18 completed; group means 18.37 and 17.76; switching replications without randomisation; one workshop; eight sessions of about 30 minutes over 3 weeks; last-two-minutes scenario with a referee and a deficit; team sprints after missed free throws; coach-led reflection.
- PASS, results: individual resilience not significant; team vulnerabilities p = .013.
- PASS, players' and coaches' accounts: stress; frustration when behind and made to run; unfairness; panic; younger players more affected by consequences that fell on teammates; training cannot fully match competition; the "careful balance" quotation is exact.
- PASS with a qualification: the cap on attempts (minor finding above).
- Unverifiable: "limited" time-outs. The source returned only "time-outs".

**Stoker et al. 2016.** Abstract, https://ijsp-online.com/abstract/view/47/262
- PASS: 11 elite coaches; task, forfeit and judgement stressors; demands and consequences; individual differences; the definition of pressure is quoted exactly.

**Stoker et al. 2019.** Manuscript, https://researchonline.ljmu.ac.uk/id/eprint/13095/1/Effect%20of%20pressure%20training%20manipulations%20pressure.pdf
- PASS, design: six GB disability shooters, 5 rifle and 1 pistol, aged 20–41; the seven randomised conditions as described; required score = mean of the last three competitions.
- PASS, results: pressure and cognitive anxiety rose only under forfeit and judgement; judgement more debilitative; performance fell under judgement and the time limit; the reward changed nothing; means 1.83, 2.8, 4.5 and 4.9, other means not reported; sample size named as a limitation.

**Low et al. 2023.** Full text, https://researchonline.ljmu.ac.uk/id/eprint/18698/3/Pressure%20Training%20From%20Research%20to%20Applied%20Practice.pdf
- PASS, design guidance: demands against consequences; rewards not recommended; the exposure-therapy analogy; gradual steps; limiting repetitions.
- PASS, forfeits: the list (singing, deselection, sprints and push-ups); the self-worth warning; "Few ethical consequences are likely to be strong enough" is exact.
- PASS, timing: once a month is too rare; not every session needs pressure; stopping before competition is a trade-off; a new skill is learned without pressure first.
- PASS, debrief: the question "What did you do that helped/hurt you in this drill?" is exact.

**Rupprecht et al. 2024.** Publisher page, https://informahealthcare.com/doi/abs/10.1080/1750984X.2021.1944271, and LIDA, https://lida.sport-iat.de/ta/Record/4088526?lng=en
- PASS, scope: the definition quotation; 33 extensive and 27 stand-alone samples; handgrip 7; quiet eye 3; 33 articles, 61 samples, 112 effect sizes; 15 sports; golf 15, basketball 13, tennis 6; ages 11–40.
- PASS, effects: g 0.64 [0.45, 0.83]; g 0.70 [0.24, 1.16]; SMC 0.31 [0.18, 0.44]; no moderators.
- PASS, limits: usable by young individuals; 16 samples under 10 and 32 of 10–19; small-study effect in the pre-post data; no evidence that publication bias explains the effects; no senior athletes.

**Gröpel & Mesagno 2019.** Abstract on LIDA, https://lida.sport-iat.de/ta/Record/4055257
- PASS: 47 studies to April 2017; the designs; 13 interventions in three groups; the four most often reported effective; the secondary task; analogy learning mixed; goal setting, neurofeedback and reappraisal null.
- Not opened: the sample details taken from SP4 (finding above).

**Soligard et al. 2016.** Abstract, https://dspace.lboro.ac.uk/2134/22957
- PASS: "psychological load and travel"; the monitoring guidelines.

**Tranaeus et al. 2024.** Full text, https://pmc.ncbi.nlm.nih.gov/articles/PMC11258162/
- PASS: seven experts; the quotation is exact; it cites Ivarsson et al. 2017.

**Tannenbaum & Cerasoli 2013.** Epistemonikos abstract and the CEBMA full text (the PubMed fetch failed: not checked).
- PASS: 46 samples, 2,136 participants, about 25%, d = .67; similar effects for teams and individuals, simulated and real settings, and both control designs; alignment; facilitation and structure only "potential"; 28 medical and 18 non-medical samples; under-16s excluded; no sport samples; no 95% CI.

## Pass: Bibliography

Every Sources entry checked against the record opened, field by field. Crossref itself was not queried: no search returned a Crossref URL. No non-existent reference was found.

| Reference | Record checked | Result |
|---|---|---|
| Gröpel & Mesagno | LIDA | Title, journal, 2019, 12(1), 176–201 and DOI match. Authors not confirmed against a publisher or Crossref record (the VU repository blocked the fetch): unverifiable for authors. |
| Kegelaers et al. | VU record | All fields match. |
| Kent et al. | Gloucestershire record; publisher page | Authors, title, 34(4), 691–712 and DOI match; the repository gives the year as 2021. Online date 25 Feb 2021 matches the publisher page. Print year 2022 not seen on any page opened (consistent with volume 33 being 2021): unverifiable for print year. |
| Low et al. 2021 | Heriot-Watt | Authors and order, title, 2021, 10(1), 149–163 and DOI match. "Online 16 Jan 2020" not seen: unverifiable. |
| Low et al. 2024/2023 | Heriot-Watt | Authors, title, 2024, 15(1), 3–18, DOI and early online date 18 Jan 2023 match. |
| Oudejans & Pijpers | VU record | All fields match. |
| Rupprecht et al. | LIDA; EurekAlert release, https://www.eurekalert.org/news-releases/934597 | Journal, 2024, 17(1), 39–64 and DOI match LIDA. Authors match only the University of Vienna release, not a publisher or Crossref record. "Online 2021" not seen. |
| Soligard et al. | Brage; Loughborough | All 18 authors in order, title, 50(17), 1030–1041 and DOI match. Brage misspells two names; the unit's spelling is the usual one. |
| Stoker et al. 2016 | Journal's page | All fields match. |
| Stoker et al. 2019 | Essex record | All fields match. |
| Tannenbaum & Cerasoli | CEBMA copy; Epistemonikos | Authors, title, 55(1), 231–245 and DOI match. |
| Tranaeus et al. | PMC | All fields match. |

## Pass: Source log

- Not available for this unit: the writer's notes were withheld.
- The Sources section gives the address, what was read and the date for every entry.
- Every abstract-only claim says so in the text: Oudejans (line 22), Stoker 2016 (53), Gröpel & Mesagno (102 and the section 6 table), Soligard (125), Tannenbaum (abstract plus full text, 185), Rupprecht (abstract and parts of the text, 92).
- Exception: section 6's SP4-derived sample details do not say they were not re-read (finding above).

## Pass: Grades

- Pressure training [moderate]: PASS. It fits "a meta-analysis of small or mixed studies" in athletes and police. It is not strong: unclear risk of bias, simulated outcomes.
- Kent coping skills [weak]: PASS (single study).
- Section 3 table, [weak] for one six-athlete study and [practice] for untested ways: PASS.
- Rules, ladder, caps, readiness, step-down and debrief questions [practice]: PASS.
- Routines [moderate]: PASS (meta-analysis; small samples; small-study effect).
- Quiet eye and left-hand contractions [moderate]: defensible but stretched (minor finding above).
- Secondary task, analogy learning, goal setting and reappraisal [weak]: PASS (one review read in abstract).
- Debrief [weak]: PASS (meta-analysis outside sport).
- Low et al. 2023 used only for [practice]: PASS.
- SP1's numbered rules and the SP3–SP5 grades the unit cites are not in the packet: not checked.

## Pass: Population

- Each finding names its sample:
  - Oudejans: expert players.
  - Low: novices to experts, police, youth cricketers.
  - Kent: 82 males aged 11–18.
  - Kegelaers: 19 women of about 18.
  - Stoker 2016: 11 elite coaches.
  - Stoker 2019: six adults aged 20–41.
  - Rupprecht: ages 11–40.
  - Gröpel: athletes, ages via SP4.
  - Tannenbaum: no sport samples; under-16s excluded.
- Inference labels are present for Low, the Stoker 2019 table rows, the secondary-task rows and debriefs.
- Missing: section 3's closing recommendation has no inference label, and "mostly adults" is overstated (findings above).

## Pass: Scope and safety

PASS on every point:
- Nothing teaches assessment, diagnosis or treatment. Section 8 hands treatment to a clinician and distress to SP4's table and urgent route. The 0–10 rating is declared non-clinical.
- Eating: Dani's skipped snack goes to the club's person for medical concerns. Rule 8 bans weight, food and the body as a pressure or a consequence.
- No weight-loss method, calorie figure or target weight. No method of self-harm.
- No law stated as the reader's; the disclaimer is at line 12.
- No real athlete, coach or club is named.

## Pass: Any sport

PASS. I counted 22 examples (case blocks, prose and table examples; study samples excluded).

| Sport | Count | Where |
|---|---|---|
| Football | 5 | Academy match (s1), footballer (s7), penalty kick, Milan's block, SP5 rondo (s9) |
| Athletics | 5 | High jumper, 400 m runner (s5), jump at the height, 300 m rep, Sara's builder |
| Judo | 3 | Judoka (s7), judo round (level 6), Dani's block |
| Swimming | 3 | Call room (s5), s7, relay (level 2) |
| Tennis | 2 | |
| Volleyball | 2 | |
| Basketball | 1 | |
| Gymnastics | 1 | |

The largest share is 5/22 = 23%, under a third. The examples include individual, team, weight-class (judo), judged (gymnastics) and endurance-type (400 m) sports.

## Part 7, line by line

1. Sourced where made: PASS.
2. Source types: PASS except Low et al. 2023, a guidance article outside the listed types. The unit declares this and uses it only for [practice] grades. This exception needs the maintainer's ruling.
3. No banned sources cited: PASS. The EurekAlert release is used only for author names in Sources, not for a claim.
4. Source log: the log was withheld; Sources entries carry address, what was read and date: PASS. Abstract-only reads are flagged except the SP4-derived details (finding above).
5. Sources against publisher or Crossref records: PASS, with the unverifiable fields listed under Bibliography.
6. Grades: PASS, one minor finding.
7. Sample and design stated; a correlation called a correlation: PASS.
8. Inference labels: one missing (finding above).
9. Effect sizes in the source's terms, with sample: PASS.
10. Popular claims set against evidence or "no peer-reviewed source found": PASS (section 11).
11. Coach's part: PASS.
12. Weight and self-harm: PASS.
13. Law: PASS.
14. Real persons: PASS.
15. Sports: PASS.
16. Case facts: the "(fictional)" labels and the never-as-evidence rule PASS. Three facts are not in the register and not marked added (findings above).
17. Private terms: kit/private_terms.py is not in the packet, so it was not run. Nothing about the owner was seen.
18. Search flag: off, not applicable.
19. Deliverable built on the case, then as a template: PASS.
20. Not advice without evidence: PASS.
21. Links as DOI links: PASS.

## Brief and deliverable

Coverage, every item of the brief covered:
- Why a skill learned calm fails in competition.
- The pressure-training meta-analysis, with its domains and samples.
- The seven ways of making pressure (table).
- What is acceptable with minors, as rules with reasons, including the four the brief names.
- Pre-performance routines with their meta-analysis.
- The choking-interventions review.
- Rehearsing the competition day.
- The debrief.
- Psychological load as load.
- When not to train under pressure: distress, the days before a competition, an athlete new to the squad.

Deliverable present in full:
- The four-week block with the six-level ladder, session slot, step-down rule and debrief questions, built for Dani's squad and for Milan's.
- The routine builder, built for Sara.
- Both templates, with blanks that say what goes in them.

It can be used on its own and follows from the evidence, with [practice] grades declared where nothing tests it.

## Claims not verified

- **Low 2021:** that the law-enforcement tasks were "all shooting". "One study high on several" risk-of-bias domains: the source shows one study high on two. The online date 16 Jan 2020.
- **Kent 2021:** decision-making "coach-rated"; print year 2022.
- **Kegelaers 2021:** "limited" time-outs.
- **Gröpel & Mesagno 2019:** the authors (no publisher or Crossref record opened); the full text; the SP4-derived sample details.
- **Rupprecht 2024:** authors from a news release only; online year 2021.
- **Tannenbaum & Cerasoli:** the PubMed and SAGE pages were not opened (the PubMed fetch failed).
- **Cross-references to SP1–SP5:** the earlier units are not in the packet, so none of these were checked:
  - SP1 grade-key rule numbers.
  - SP3 climate findings and grades; SP3's change to normal volume.
  - SP4 table rows 9 and 10; Milan's anxiety profile.
  - SP5 block weeks and the rondo; Sara's 3-minute imagery scene with the pass at 250 m.
- **kit/private_terms.py:** not run.

## Confirmed

Every PASS line under "Pass: Claims" above is confirmed against the named source at its URL.
