---
audit: fresh check
unit: SP6 · Training under pressure
course: sport-psychology · Sport Psychology for Coaches
model: claude-opus-5-5
date: 2026-11-18
chat: https://claude.ai/code/session_01KMmgR2e7dZXhbRyUQ6qdop
verdict: fix · 2 errors, 11 should-fix, 7 minor
---

The checker's final report, verbatim, from its hand-back. Saved before any finding was applied.

Verdict: SP6 · fix · 2 error, 11 should-fix, 7 minor

Model: claude-opus-5-5. This is the fresh check of SP6 "Training under pressure" (row W-SP6), run as audit-units SKILL section 3 with its figures paragraph. The harness refused the report file at /tmp/w/checker/out/report.md, so the whole report is here.

**What I read:** unit.md, brief.txt, sourcing-standard.md Parts 1 and 7, notes.md, unsure.md, sources.md, case-facts.md, SP1 section 9, SP3, SP4 sections 5 and 8 and its Deliverable, and SP5 sections 4 to 6 and its Deliverable. There are no audit errata for this course, so that step was skipped. I checked every Current below with grep -cF; each occurs once in unit.md.

**Fetch record.** WebSearch came first, and I fetched only URLs a search returned.
- **Refused by the permission check, not retried:**
  - repository.essex.ac.uk/26305/3/PressureTrainingForPerformanceDomains.pdf (the Low 2021 manuscript)
  - researchonline.ljmu.ac.uk/id/eprint/13094/
  - lida.sport-iat.de/svd/Record/4088526/Cite
  - informahealthcare.com/doi/ref/10.1080/1750984X.2021.1944271
- **Failed at the site:** pubmed.ncbi.nlm.nih.gov/23516804/ and journals.sagepub.com/doi/10.1177/0018720812448394.
- **Blocked by a verification or login wall:** scinapse.io, x-mol.com, vuir.vu.edu.au (Anubis), peeref.com.
- **Redirected, not followed:** medienportal.univie.ac.at.
- **Low et al. (2021) results:** checked instead in chapter 4 of William Low's PhD thesis, which is the same meta-analysis but not the version of record: https://repository.essex.ac.uk/33331/1/WilliamLow_PhD-Thesis-AUG2022-final%20submission.pdf

## Findings

[error] [accuracy] 2, Two studies with younger athletes; Current: "(a one-against-one task with crowd noise"; Problem: FAIL. The pressure task was two against two ("two attacking players and two defending players"), not one against one; Fix: "(a two-against-two task with crowd noise"; Basis: Kent et al., accepted manuscript, https://eprints.glos.ac.uk/9339/1/9339-Kent-(2021)-Implementing-a-pressure-training-program.pdf

[error] [accuracy] 11, "Harsh coaching builds toughness"; Current: "A pressure drill made harsh by shouting, humiliation or punishment adds nothing the opened pressure studies used to make pressure work: the forfeit that raised pressure in the shooters was a staged media interview, and the consequences in this unit's ladder are sporting ones."; Problem: FAIL. The opened studies did use punishment. In the basketball package a missed free throw made the team sprint, and players said having to run made their frustration worse; section 2 of the unit reports this. The staged media interview was a five-minute press conference about failing the required score, which section 4's rule 1 would itself rule out. No opened study compared a harsh consequence with a sporting one; Fix: "No opened study tested whether harshness adds anything. The opened pressure studies did use punishment: the basketball package made the team sprint after missed free throws, and players reported frustration at having to run ([Kegelaers et al., 2021](https://doi.org/10.1080/10413200.2019.1630864)); the forfeit that raised pressure most in the shooters was a staged media interview about missing the score, which section 4's rule 1 would itself rule out. They show that a consequence and being judged create pressure; none compared a harsh consequence with a sporting one, and the consequences in this unit's ladder are sporting ones."; Basis: Kegelaers et al., full text, https://core.ac.uk/download/387931251.pdf; Stoker et al. 2019 manuscript, https://researchonline.ljmu.ac.uk/id/eprint/13095/1/Effect%20of%20pressure%20training%20manipulations%20pressure.pdf

[should-fix] [accuracy] 2, Two studies with younger athletes; Current: "one group also had three 30-minute coping-skills workshops and reflective diaries"; Problem: the paper calls them cognitive-behavioural (CB) workshops, and the 17- and 18-year-olds' sessions were cut to 15 minutes; Fix: "one group also had three 30-minute cognitive-behavioural workshops (15 minutes for the 17- and 18-year-olds) and reflective diaries"; Basis: Kent et al. manuscript (as above); abstract at https://informahealthcare.com/doi/full/10.1080/10413200.2020.1868618

[should-fix] [deliverable] 9, Caps by age band; Current: "SP5's light pressure stage (a scored game, a timed rep, a teammate watching) sits at levels 1 to 3, under every cap except the new athlete's."; Problem: F65 check. SP5's week-4 rondo for Milan's squad ("If you lose it, you lose a point") is a sporting consequence, which is level 5 on this unit's ladder (level 5 lists "a point lost"). It was run for Milan, whose referral was under way, so it was above the referral cap this unit sets; Fix: "SP5's light pressure stage (a scored game, a timed rep, a teammate watching) sits mostly at levels 1 to 3; its week-4 rondo, in which a lost ball costs a point, is a sporting consequence, level 5 on this ladder. From this unit on, every pressure drill, SP5's included, stays under the athlete's cap."; Basis: SP5 Deliverable A, Milan week 4; unit section 9, ladder table, level 5

[should-fix] [deliverable] 12; Current: "(3 for the squad, under each athlete's cap)"; Problem: level 3 means being watched and rated "against the standard", and level 2's standard comes "from the athlete's own record". SP5's block set no per-player standard and no rating against one, so the squad did not complete level 3 as this ladder defines it. The template's own rule ("the highest level completed in an earlier block, or 1") gives 1, not 3. Milan's week-9 row depends on this; Fix: "(SP5's even weeks used scores, a lost point and the coach watching, which this unit counts as level 3 for the squad, although no standard from each player's own record was set; the coach sets those standards before week 9; under each athlete's cap)"; Basis: SP5 Deliverable A, Milan weeks 2, 4, 6 and 8; unit section 9 and the template's "Starting level" line

[should-fix] [deliverable] Deliverable A, Dani's squad; Current: "Athletes aged 16 and 17 who reach level 4 in week 4 may climb to 5 or 6 in the next block, never in a competition week."; Problem: sections 8 and 9 have no "competition week" rule; the rule is no new level in the last session before a competition. Both built plans climb in competition weeks: Dani's squad adds level 4 on the Monday of the week of the competition, and Milan's squad plays every weekend and climbs every week. "5 or 6" also reads as a two-level jump; Fix: "Athletes aged 16 and 17 who reach level 4 in week 4 may climb to 5, then 6, in the next block, one level a week at most, never in the last session before a competition."; Basis: unit section 8 (The days before a competition) and section 9 (Readiness to climb)

[should-fix] [deliverable] Deliverable A, Dani's squad, week 4; Current: "(level 4 for athletes aged 13 to 17 who are ready; level 3 for the rest)"; Problem: "the rest" includes athletes who are not ready, or are still at level 1 or 2. They would be raised to 3 without meeting the readiness rule; Fix: "(level 4 for athletes aged 13 to 17 who are ready; everyone else stays at their current level, and the 11- and 12-year-olds at 3 at most)"; Basis: unit section 9, Readiness to climb

[should-fix] [deliverable] Deliverable A, Milan within the block; Current: "at level 3 he does what the squad does, with the coach watching and rating, and without one-chance or consequence drills."; Problem: the week-12 Tuesday slot is a level-6 rehearsal of the squad's first fifteen minutes, with a wrong call, waiting and noise. The unit does not say what Milan, capped at 3, does in it, and a coach reading the table would put him in it; Fix: "at level 3 he does what the squad does, with the coach watching and rating, and without one-chance or consequence drills. In the week-12 rehearsal he plays at level 3: the coach watches and rates his first passes, and no wrong call or consequence is aimed at him; if he asks, he sits it out."; Basis: unit section 8 (referral cap), section 9 caps table, Milan's week-12 row

[should-fix] [deliverable] Deliverable B, Sara; Current: "Cap 3 while her referral is under way. |"; Problem: section 8 counts Sara's "six weeks of about five hours' sleep a night" as load and says that in such a week "the athlete trains one level lower, or at level 1". Step-down trigger 4 names short sleep. Sara's plan runs levels 1 to 3 without applying it; Fix: "Cap 3 while her referral is under way; while her short sleep continues, section 8's heavy-week step applies, so she practises one level lower, at level 2 at most. |"; Basis: unit section 8 (Add up what the athlete already carries); section 9, step-down rule 4; case-facts.md (Sara)

[should-fix] [figure] 9, step-down decision figure; Current: "{"outcome": "Stop pressure; first conversation; SP4 table and scope card", "tone": 1}"; Problem: this branch is taken for "Red flag or a sign on SP4's normal-or-refer table", but its outcome gives only the first conversation. For a red flag, step-down rule 5, section 8 and SP4 rows 9 and 10 all say the urgent route the same day; Fix: "{"outcome": "Stop pressure; first conversation, SP4 table and scope card; a red flag goes by the urgent route the same day", "tone": 1}"; Basis: unit section 9, step-down rule 5; SP4 Deliverable rows 9 and 10

[should-fix] [attribution] Sources, Low et al. (2023); Current: "*Journal of Sport Psychology in Action* 2023 (published online 18 Jan 2023)"; Problem: the version of record is 2024, volume 15, issue 1, pages 3–18 (Heriot-Watt research portal: published 2 Jan 2024, early online 18 Jan 2023). The entry's later words "volume, issue and pages not shown on the copy read" should then be removed; Fix: "*Journal of Sport Psychology in Action* 2024;15(1):3–18 (published online 18 Jan 2023; cited in the text by its online year)"; Basis: https://researchportal.hw.ac.uk/en/publications/pressure-training-from-research-to-applied-practice/

[should-fix] [attribution] Sources, Kent et al.; Current: "*Journal of Applied Sport Psychology* 34(4):691–712 (published online 25 Feb 2021)"; Problem: the year of the issue is missing; volume 34, issue 4 is 2022; Fix: "*Journal of Applied Sport Psychology* 2022;34(4):691–712 (published online 25 Feb 2021; cited in the text by its online year)"; Basis: issue listing at https://idrottsforum.org/journal-of-applied-sport-psychology-volume-34-2022-issue-4/ (Sofie Kent, Tracey J. Devonport, Andrew M. Lane, Wendy Nicholls; pp. 691–712; 2022)

[should-fix] [attribution] Sources, Rupprecht et al.; Current: "- Rupprecht, Tran, Gröpel. The effectiveness"; Problem: the authors have no initials, and Part 7 requires authors to match the record. The University of Vienna's news release names them as Anton Rupprecht, Ulrich Tran and Peter Gröpel; it is used for bibliographic fields only, not for any claim; Fix: "- Rupprecht A, Tran U, Gröpel P. The effectiveness"; Basis: https://www.eurekalert.org/news-releases/934597

[minor] [attribution] Sources, Rupprecht et al.; Current: "authors' family names from the course's seed list, initials not seen: not verified)"; Problem: follows from the finding above; Fix: "authors' names from the University of Vienna's news release on EurekAlert, not the publisher's record)"; Basis: https://www.eurekalert.org/news-releases/934597

[minor] [attribution] Sources, Gröpel & Mesagno; Current: "authors as SP4 recorded them from the journal's issue listing: not verified in this session"; Problem: the authors can now be confirmed. A University of Vienna sport psychology news item announces the review by Peter Gröpel and Christopher Mesagno; Fix: "authors confirmed on the University of Vienna's sport psychology news page announcing the review, not the publisher's record"; Basis: https://soko-psy.univie.ac.at/news/details/news/neuer-artikel-in-international-review-of-sport-and-exercise-psychology-impact-factor-2917/

[minor] [label] 3, table, Consequences; Current: "Rewards: [weak, no pressure effect shown; same study]."; Problem: six adults applied to under-18s, without the label *inference* that SP1's key requires; Fix: "Rewards: [weak, no pressure effect shown; same study; inference for under-18s]."; Basis: SP1 section 9, third further rule

[minor] [label] 3, table, Fatigue; Current: "[weak, no pressure effect shown for cognitive pre-fatigue, one study of six adults;"; Problem: the *inference* label is missing, as above; Fix: "[weak, no pressure effect shown for cognitive pre-fatigue, one study of six adults, inference for under-18s;"; Basis: SP1 section 9

[minor] [accuracy] 11; Current: "SP3 regraded it."; Problem: SP3 section 10 re-examined the claim and kept SP1's grade [weak, against]; "regraded" suggests a change; Fix: "SP3 re-examined it and kept [weak, against]."; Basis: SP3 section 10

[minor] [deliverable] Deliverable A, Milan week 9; Current: "the coach watches and rates "forward first passes" against each player's standard from SP5's block."; Problem: SP5's block set no per-player standard for forward first passes; Fix: "the coach watches and rates "forward first passes" against a standard set from each player's own count in SP5's week-8 game."; Basis: SP5 Deliverable A, Milan week 8

[minor] [figure] 2, range figure; Current: "{"label": "Debriefs, outside sport (Tannenbaum & Cerasoli)", "low": 0.67, "high": 0.67, "tone": 5}"; Problem: a row with low equal to high and no point draws a zero-width bar or nothing. The caption already says no interval was given; the row needs a point so the estimate shows; Fix: "{"label": "Debriefs, outside sport (Tannenbaum & Cerasoli)", "low": 0.67, "high": 0.67, "point": 0.67, "tone": 5}"; Basis: unit section 10 (d = 0.67)

## Confirmed

- **Section 1, Oudejans & Pijpers (2009):** 17 expert basketball players practised free throws for five weeks; 17 expert dart players threw on a climbing wall. Performance held on the anxious post-test only after training with anxiety; the habituation explanation is the authors'. PASS (abstract). https://research.vu.nl/en/publications/training-with-anxiety-has-a-positive-effect-on-expert-perceptual--2/
- **Section 2, Low et al. (2021), abstract:** 14 studies (10 sport, 4 law enforcement), 394 participants; g = 0.67 after the outlier, I² = 17.1%, abstract CI [0.43, 1.12]. PASS. https://repository.essex.ac.uk/26305/ ; https://researchportal.hw.ac.uk/en/publications/pressure-training-for-performance-domains-a-meta-analysis/
- **Section 2, Low et al. (2021), results.** PASS, but checked in the author's thesis chapter 4, not the version of record (the manuscript fetch was refused):
  - all studies g = 0.85 [0.37, 1.34], I² 78.4%; without the outlier 0.67 [0.41, 0.94];
  - sport 0.72 [0.45, 1.00], k = 10; law enforcement 0.63 [−0.14, 1.39], k = 3;
  - novices 0.77 (5 studies), experienced 0.61 (8);
  - one session 0.73 (6), two to five sessions 0.72 (4), more than five 0.42 with the interval crossing zero (3);
  - no clear moderator; Egger p = 0.12; funnel fairly symmetrical; sports as listed;
  - manipulations: judgement 8, rewards 6, forfeits 4 in the table, environmental 3;
  - only Bell et al. (2013) measured competition, as overall performance; one retention test, not pooled.

  The thesis notes that the per-study Ns sum to 399, as the unit's unsure list says.
- **Section 2, Low et al. (2021), unverifiable** (the manuscript was refused): the quotation "physically practiced as much as", the inclusion criteria, "no mean ages", and risk of bias "unclear in most domains". The thesis says most randomised studies were unclear on selection, with several high on attrition or "other" items, which fits the unit.
- **Section 2, Kent et al.:** 82 male academy players aged 11 to 18, mean 14.12, randomly allocated; three pressure sessions over 18 weeks; crowd noise, a public leaderboard, rewards for the top three, dice-roll consequences for the bottom three, sprints for the 15- to 18-year-olds; coach-rated; decision-making χ² = 7.15, p = .028; skill execution not significant; 68 retested at six weeks and 26 at twelve; "partial support"; the ethics recommendations (protection from harm; results not to inform contractual decisions). PASS apart from the two findings above.
- **Section 2, Kegelaers et al.:** PASS. https://core.ac.uk/download/387931251.pdf
  - 19 players, group means 18.37 and 17.76; switching replications, groups matched, not random.
  - A 1.5-hour workshop and eight sessions of about 30 minutes over three weeks.
  - Manipulations: referee, deficit, last two minutes, cap on attempts, team sprints after misses, the team watching, limited time-outs.
  - A coach-led reflection after every session.
  - CD-RISC interaction not significant; CREST interaction p = .013.
  - Reports of stress, frustration, unfairness and panic; younger players more sensitive to consequences that fell on teammates.
  - "a careful balance between sufficient challenge and support"; players said training cannot fully re-create competition.
- **Section 3, Stoker et al. (2016):** 11 elite coaches; task, forfeit and judgement stressors; demands and consequences; the definition of pressure is quoted exactly. PASS (abstract). https://ijsp-online.com/abstract/view/47/262
- **Section 3, Stoker et al. (2019):** PASS. "Random order" of the conditions was not confirmed in the extraction: unverifiable.
  - Six GB disability shooters (five rifle, one pistol), aged 20 to 41; seven conditions.
  - The required score was each athlete's mean from their last three competitions.
  - Perceived pressure and cognitive anxiety rose under the forfeit and under judgement; scores fell under judgement and under the time limit; judgement was more debilitative; the reward was not significant.
  - Means 1.83, 2.8, 4.5 and 4.9, the others not given; sample size named as a limitation.
- **Sections 3, 4, 8 and 10, Low et al. (2023):** PASS. https://researchonline.ljmu.ac.uk/id/eprint/18698/3/Pressure%20Training%20From%20Research%20to%20Applied%20Practice.pdf
  - Demands do not reliably create pressure (from the netball study); rewards are not recommended.
  - The graded-exposure analogy ("so that athletes are not overwhelmed").
  - The forfeit list (singing, deselection, teammates' sprints or push-ups); "Few ethical consequences are likely to be strong enough"; a consequence is tied to performance only, not to self-worth.
  - Limiting repetitions; pressure one day a month is not enough, and not every session is pressurised.
  - Stopping before competition may protect confidence.
  - The debrief and routine questions.
- **Section 5, Rupprecht et al. (2024):** PASS. https://informahealthcare.com/doi/abs/10.1080/1750984X.2021.1944271
  - The definition (Moran, 1996) quoted.
  - 33 articles, 61 samples, 112 effect sizes; 15 sports (golf 15, basketball 13, tennis 6); ages 11 to 40.
  - g = 0.64 [0.45, 0.83] under low pressure and 0.70 [0.24, 1.16] under pressure; pre-post SMC 0.31 [0.18, 0.44].
  - No moderator; "can already be applied by young individuals".
  - 16 samples under 10 participants and 32 with 10 to 19; a small-study effect in the pre-post data; p-uniform found no bias; no senior athletes.
  - Extensive routines in 33 samples, stand-alone in 27 (handgrip 7, quiet eye 3).
- **Section 6, Gröpel & Mesagno (2019):** 47 studies to April 2017; the designs; 13 interventions grouped as distraction, self-focus and acclimatisation; routines, quiet eye, left-hand contractions and acclimatisation most often effective; dual-task helps under pressure but harms in training; analogy mixed; goal setting, neurofeedback and reappraisal null. PASS (abstract). https://lida.sport-iat.de/ta/Record/4055257. The sample details credited to SP4 (62%, 68%, golf, four in competition, medium quality) agree with SP4 section 5.
- **Section 8, Soligard et al. (2016):** "psychological load and travel"; guidelines for monitoring training, competition and psychological load. PASS (abstract); the full author list matches. https://dspace.lboro.ac.uk/2134/22957
- **Section 8, Tranaeus et al. (2024):** seven experts; "Stress responses are the strongest psychological risk factor for acute injuries" is exact, cited to Ivarsson et al. PASS. https://research.stmarys.ac.uk/id/eprint/6344/1/s40279-024-02045-w.pdf ; citation at https://experts.umn.edu/en/publications/50-years-of-research-on-the-psychology-of-sport-injury-a-consensu/
- **Section 10, Tannenbaum & Cerasoli (2013):** 46 samples, N = 2,136; about 25%, d = .67; similar for teams and individuals, simulated and real, both designs, medical and non-medical; alignment strengthens the effect; facilitation and structure show potential. PASS (abstract). https://www.epistemonikos.org/en/documents/62327b87190b146b78b9cda25182d69d9e3f255d
- **Cross-references to earlier units:** all PASS.
  - SP4: the two accounts of choking; rows 9 and 10 as red flags with the urgent route; exposure as a clinician's treatment (row 5).
  - SP3: never using selection as a threat; exercise as punishment [practice] from adults' accounts; the ego-involving climate and fear of failure (an association); Dani's coach's changes (normal volume; ask first, then one point).
  - SP5: the four stages; the light pressure in weeks 2, 4, 6 and 8; the night-before rule; the grades for breathing [weak], imagery [moderate, positive], self-talk [weak, mixed] and attentional focus [contested].
  - SP1: its moderate worked example uses Rupprecht et al.

## (7) Figures

1. **range, section 2: FIX.** Every row traces to the text:
   - 0.67 [0.41, 0.94] (section 2, "without it, g = 0.67 ... 0.41 to 0.94 in the results");
   - 0.72 [0.45, 1.00] and 0.63 [−0.14, 1.39] (section 2, sport and law-enforcement subgroups);
   - 0.70 [0.24, 1.16], 0.64 [0.45, 0.83] and SMC 0.31 [0.18, 0.44] (section 5, "What it found");
   - d = 0.67 (section 10).

   The caption names sections 2, 5 and 10, the metrics and the sources, and range fits competing estimates. The fix: the debriefs row needs "point": 0.67 (finding above).
2. **compare, section 3: PASS.** 1.83, 2.8, 4.5 and 4.9 and the four labels trace to section 3 ("Mean perceived pressure on a 1-to-7 scale was 1.83 at baseline, 2.8 under the performer demand, 4.5 under judgement and 4.9 under the forfeit"). The caption names the section, the source and what is left out, and "significantly above baseline" matches the text. Compare fits numbers compared.
3. **flow, section 9: PASS.** The six labels and notes trace to the ladder table. The caption says the order is the unit's reading of section 3 and that the ladder is untested [practice], which matches section 9 ("in the order section 3's evidence suggests ... The ladder is untested"). Flow fits a sequence.
4. **decision, section 9: FIX.** The questions and outcomes trace to step-down rules 1 to 5 and to section 8; the caption gives the order and the source; decision fits a rule with branches. The fix: the first outcome leaves out the urgent route for a red flag (finding above).

## Passes

**Claims.** I opened all 12 cited sources, at least in abstract; for Low 2021 the results came from the author's thesis chapter, not the manuscript.
- Two FAILs: Kent's task described as one against one (it was two against two), and section 11's sentence that the opened studies used no punishment.
- Not opened, because the fetch was refused: the Low 2021 accepted manuscript. Its inclusion criteria and the "physically practiced as much as" quotation are unverifiable, not PASS.
- Not checked: whether the Stoker 2019 conditions ran in random order.
- Everything else PASS, as listed under Confirmed.

**Bibliography.** I checked each entry field by field against publisher pages, institutional records or an issue listing. Crossref itself was not reachable, because no search returned a Crossref URL.
- Gröpel & Mesagno 2019, IRSEP 12(1):176–201, with DOI: matches LIDA; authors confirmed on the Vienna news page.
- Kegelaers et al. 2021, JASP 33(2):151–172: matches the VU record exactly.
- Kent et al.: authors and pages match; the 2022 issue year is missing (should-fix).
- Low et al. 2021, SEPP 10(1):149–163: matches Heriot-Watt ("Published Feb 2021").
  - Author order Low, Sandercock, Freeman, per Heriot-Watt; the Essex record lists Freeman second, as the unit says.
  - "Online 16 Jan 2020" not verified.
- Low et al. 2023: the version of record is 2024;15(1):3–18 (should-fix).
- Oudejans & Pijpers 2009, QJEP 62(8):1631–1647: matches.
- Rupprecht et al. 2024, IRSEP 17(1):39–64: matches LIDA; initials missing (should-fix).
- Soligard et al. 2016, BJSM 50(17):1030–1041: all 18 authors in order match Loughborough.
- Stoker et al. 2016, IJSP 47(3):262–281: matches the journal page.
- Stoker et al. 2019, TSP 33(3):221–227, DOI 10.1123/tsp.2017-0045: matches Essex. Low et al. (2023)'s own reference list attaches the netball paper's DOI to this paper; that is their typo, and the unit does not copy it.
- Tannenbaum & Cerasoli 2013, Human Factors: volume, issue and pages could not be checked (PubMed and SAGE failed at the site), as the unit itself says. The paper exists (Epistemonikos; PubMed ID 23516804).
- Tranaeus et al. 2024, Sports Medicine 54(7):1733–1748: matches the University of Minnesota record.

Every reference exists.

**Source log.** All 12 Sources entries have a row in sources.md. Every abstract-only claim is marked in the unit: Oudejans, Stoker 2016, Gröpel, Soligard and Tannenbaum, and Rupprecht as "abstract and parts of the text".

There is one error in the log, not in the unit. The "Not opened" row for the netball study (Stoker et al., 2017) gives "TSP" and DOI 10.1123/tsp.2017-0045, which belong to the shooters' paper. Low et al. (2023)'s reference list gives the netball paper as JASP 29(4):434–448, DOI 10.1080/10413200.2017.1298166. Correct the log, and give notes "Needs" item 5 the right reference.

**Grades.** All checked against SP1 section 9:
- **Pressure training [moderate, positive]:** correct. Rule 3 fails (risk of bias unclear; the law-enforcement and long-dose subgroups cross zero), so rule 4 applies.
- **Pre-performance routines [moderate]:** correct under rule 4 (small samples, small-study effect), and it agrees with SP1's worked example.
- **Coping skills alongside pressure training [weak]:** correct; one randomised study, rule 5.
- **Section 3 stressors [weak]:** correct; they rest on one within-subject study.
- **One attempt, bad calls, waiting [practice]:** correct; no study isolates them.
- **Quiet eye and the other single techniques [weak]:** a defensible floor, since the review was read in abstract and per-technique counts were not seen.
- **Debriefs [weak]:** correct. The unit calls the evidence outside sport while also saying the abstract does not state whether any sample was athletes; rule 5 gives weak either way.
- **Rules, ladder and caps [practice]:** correct.

Other checks:
- The unit states the F1 answer: "Does any technique in this unit reach strong (flag F1)? No."
- The F47 and F48 conventions are applied as SP5 applied them and are logged in the notes (contradictions 2 and 5).
- Two grades lack the *inference* label (the minor findings above).

**Population.** Every finding names its sample and design:
- Oudejans: expert players; no ages given, and the unit says so.
- Low 2021: novices to experts and police, with one elite youth sample.
- Kent: male academy players aged 11 to 18, randomised.
- Kegelaers: a women's academy, players about 18, not randomised.
- Stoker 2016: 11 elite coaches.
- Stoker 2019: six adult shooters, within-subject.
- Rupprecht: ages 11 to 40.
- Gröpel: athletes, with SP4's details.
- Tannenbaum: 46 samples and their settings.

Every transfer to under-18s is labelled *inference* except in the two minor findings. The age caps say they rest on no study of harm in under-18s.

**Scope and safety.** PASS.
- Nothing teaches assessment, diagnosis or treatment. Section 8 says treatment belongs to a clinician and that exposure is borrowed only as an analogy, and the debrief rating is said not to be clinical.
- Where the coach's part ends is stated for distress (SP4's table, the scope card, the urgent route) and for eating and weight (Dani: the scope card, the club's medical contact, DD-SP2; rule 8).
- No weight-loss method, calorie figure or target weight; no method of self-harm.
- No law is stated as the reader's, and the preamble says the unit is information, not advice.
- No real athlete, coach or club is named.

**Any sport.** PASS. Counting illustrative examples by sport (each case plan counted once; studies left out), there are 23 in all and the largest share is 5 of 23, or 22%:

| Sport | Examples | Count |
|---|---|---|
| Football | academy lost ball, section 7 footballer, penalty kick, Milan's block, its rehearsal | 5 |
| Athletics | high jumper, 400 m runner's hour, one jump at the height, 300 m rep, Sara's routine | 5 |
| Judo | Dani's block, section 7 judoka, level-6 judo round, Dani in the block | 4 |
| Swimming | | 3 |
| Tennis | | 2 |
| Volleyball | | 2 |
| Basketball | free throw | 1 |
| Gymnastics | | 1 |

Individual, team, weight-class, judged and endurance sports are all present. With the studies added (basketball 2, football 1, shooting 1, darts and climbing 1), no sport goes above a third. `python3 kit/private_terms.py` on the unit prints "0 private terms, 0 warnings: OK", and nothing points to the Project's owner.

**Part 7, line by line.**
- Every claim sourced where it is made: PASS.
- Source types: PASS. Low 2023 is labelled a practitioner article and supports [practice] grades only.
- No video, podcast, blog or press report cited: PASS.
- Source log, with abstract-only claims labelled: PASS. The log error is noted above.
- Sources match their records: FAIL on three entries (Low 2023, Kent, Rupprecht's initials).
- Every technique carries one of the five grades, following SP1's key: PASS, apart from two missing *inference* labels.
- Sample and design stated, correlations called correlations: PASS.
- *Inference* labelled: PASS, apart from the two minor findings.
- Effect sizes in the source's own terms: PASS (g, SMC, d, χ²).
- Popular claims: PASS. "Harsh coaching" and "Mental toughness" are both on the seed list; the section 11 error stands apart.
- Coach's part: PASS. Weight and self-harm: PASS. Law: PASS. Real persons: PASS.
- At least three kinds of sport, none above a third: PASS.
- Case facts: PASS. Each athlete is labelled "(fictional)", the facts agree with case-facts.md, the new ones are marked *added* and listed in notes 1 to 5, and the case is never evidence. Sara's kept breathing and imagery scene are covered by note 5 but marked *added* only once, at the end of the sentence; acceptable.
- Private terms: PASS.
- Search flag off and no current facts: not applicable.
- Deliverable built in full and given as templates: PASS.
- Does not read as advice without evidence: PASS; every rule says it is the unit's practice and untested.
- Links as DOI links: PASS.

**F65.** PASS, with two corrections. SP6 builds SP5 section 4's stage 3 (the ladder and the step-down rule, section 9) and points back to SP5's eight-week block in sections 1, 9 and 12.
- SP5's stage does not sit wholly within levels 1 to 3: its week-4 lost point is level 5 on this ladder.
- The squad's starting level of 3 was not completed as this ladder defines level 3.

Both are should-fix findings above.

**Deliverable plans against the unit's own rules.**
- **Dani:** PASS.
  - Caps: age 14 gives 4; her referral under way gives 3.
  - Her weeks run 1, 2, 3, then 3 and 2, one level down in the last session before the competition.
  - She never goes above 3 and climbs at most once a week.
  - No pressure drill falls the day before: the competition is at the weekend and the last slot is Wednesday.
- **Dani's squad in week 4:** "level 3 for the rest" breaks the readiness rule (finding).
- **Both squads:** the "never in a competition week" clause contradicts both plans (finding).
- **Milan:** PASS, apart from his place in the week-12 rehearsal (finding). His referral cap of 3 holds every week, with Thursdays at 2, and the conditions for climbing follow section 8 exactly.
- **Sara:** her referral cap of 3 holds, she practises at levels 1 to 3, and first use comes after two weeks at level 2 or above. The heavy-week step for her ongoing short sleep is not applied (finding).
- **Milan's squad:** PASS, given the starting level. It climbs 3, 4, 5, 6 over weeks 9 to 12, one level a week; Thursdays run one level below, and the rehearsal is not the last session before a match.

**Captions against the text.** Done in section (7): two FIX, two PASS.

**Read as the coach in the preamble.** The unit works on a phone and read in order, and every rule comes with its reason. Three things would stop a coach, and the findings above settle each:
- what Milan does in the squad's week-12 rehearsal;
- whether a week with a match counts as a "competition week" in which no one climbs;
- whether Sara's ongoing short sleep lowers her level.

Verdict: SP6 · fix · 2 error, 11 should-fix, 7 minor

Summary:
- Two FAILs: Kent's pressure task was two against two, not one against one, and section 11 says the opened studies used no punishment when Kegelaers used team sprints after misses.
- The deliverable breaks the unit's own rules in four places: the "never in a competition week" clause, Dani's squad in week 4, Milan in the week-12 rehearsal, and the heavy-week step for Sara's sleep.
- F65 is met. SP5's week-4 lost point is level 5 on this ladder, and the squad's starting level of 3 needs qualifying.
- Bibliography: Low 2023 is 2024;15(1):3–18, Kent is 2022;34(4), and Rupprecht's entry lacks initials. No reference is invented. The source log gives the wrong journal and DOI for the netball study.
- Grades follow SP1's key and nothing reaches strong. Scope, safety, any-sport and private-terms all pass.
- The Low 2021 manuscript fetch was refused, so its quotation and inclusion criteria are unverifiable; its results were confirmed in the author's thesis.
