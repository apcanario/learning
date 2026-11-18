---
audit: fresh check
unit: SP6 · Training under pressure
course: sport-psychology · Sport Psychology for Coaches
model: claude-opus-5-5
date: 2026-11-18
chat: https://claude.ai/code/session_01KMmgR2e7dZXhbRyUQ6qdop
verdict: rewrite · 4 errors, 8 should-fix, 10 minor
---

The checker's final report, verbatim, from its hand-back. Saved before any finding was applied.

Verdict: SP6 · rewrite · 4 error, 8 should-fix, 10 minor

The harness refused the write to /tmp/w/checker/out/report.md ("Subagents should return findings as text"), so the whole report follows.

# Fresh check, SP6 "Training under pressure" (row W-SP6)

Model: claude-opus-5-5, in an isolated agent context that did not see the unit written.

- **Packet read:** everything in /tmp/w/checker, plus sourcing-standard Part 1 and Part 7. brief.txt stood in for units_data.py. There is no audit errata for this course, so that step was skipped.
- **Earlier units read for pointers only:** SP1 §9 (the grade key), SP3 §§4, 5 and 10, SP4's headings and Deliverable B, and SP5 §3.4, §4 and Deliverable A.
- **Web rule:** every URL fetched was returned verbatim by a WebSearch in this agent. Fetches that were refused, redirected or bot-blocked are marked "not opened" and were not retried.

**Why the verdict is rewrite.** The skill defines rewrite as more than three errors, and four findings are errors. Each of the four is one exact replacement:
- Two are safety contradictions in the deliverable. Section 11 caps a referred athlete at level 2 and names Milan and Sara, yet their plans take them to level 6.
- One misstates the inclusion criterion of a review.
- One is a figure caption that uses a term ("Hedges'") that is not in the text. The figures rule makes that an error.

Under the method, rewrite sends the unit to a new writing chat and blocks new units. The maintainer may judge whether four one-line errors warrant that.

## (1) Coverage
All brief items are covered:
- §1, why a skill learned calm fails in competition.
- §2, the pressure-training meta-analysis with its domains and samples. Ages and study quality are thin, because only the abstract could be read; the unit says so.
- §3, the seven ways of making pressure.
- §4, rules for minors with reasons: no humiliation, no physical punishment, no threat to the athlete's place, and a way to step down.
- §6, routines and their meta-analysis.
- §7, the review of choking interventions.
- §8, competition-day rehearsal.
- §9, the debrief.
- §10, psychological load as load.
- §11, when not to train under pressure: distress, the days before a competition, an athlete new to the squad.
- Deliverable A for Dani's and Milan's squads, plus its template. Deliverable B for Sara, plus its template.

The body (§§1–11, without the viz JSON) is about 5,750 words, inside the 2,000–6,000 range. The deliverable adds about 2,800.

## (2) Findings

[error] [accuracy] §7; Current: "They included only peer-reviewed studies with significant results, so publication bias is possible"; Problem: the review's rule was to include only studies whose pressure manipulation significantly raised anxiety, not studies with significant performance results. The authors write that they "included only peer-reviewed published studies with significant anxiety effects", and they say separately that publication bias may have affected the results; Fix: "They included only peer-reviewed studies whose pressure manipulation significantly raised anxiety, and say publication bias may have affected the results"; Basis: Gröpel & Mesagno 2019, full text, https://informahealthcare.com/doi/abs/10.1080/1750984X.2017.1408134

[error] [deliverable] Deliverable A, Milan's squad; Current: "if the person he sees advises against pressure work, he stays at level 1 or stops [practice]."; Problem: §11 says "no pressure above level 2" for any athlete "whose referral is under way (Milan's and Sara's are offered)". Milan's block still takes him to level 6, and caps him only if the clinician objects; Fix: "while that referral is under way he works at level 2 at most, whatever the squad's ceiling (section 11), and if the person he sees advises against pressure work, he stays at level 1 or stops [practice]."; Basis: unit §11; SP4 Deliverable (Milan's referral offered)

[error] [deliverable] Deliverable B, Sara; Current: "| **Practised in training** | Weeks 1 and 2: the routine at levels 1 and 2 before timed 150 m reps from blocks, a group member watching. Week 3: level 3, one block start with the group watching. Week 4: level 6, a time trial with a starter, a call-room wait and the full routine. |"; Problem: Sara is referred on her SP1 card, and §11 names her and caps her at level 2. This plan goes to level 3 and then level 6; Fix: "| **Practised in training** | While her referral is under way (section 11), levels 1 and 2 only: weeks 1 to 4, the routine before timed 150 m reps from blocks, a group member watching. Levels 3 to 6 (one block start with the group watching; then a time trial with a starter, a call-room wait and the full routine) only once the person she is referred to has no objection. |"; Basis: unit §11; SP5 Deliverable A (Sara's SP1 referral)

[error] [figure] §2 range caption; Current: "Pooled effects on sport performance: point estimate and 95% confidence interval, as each source gives them (Hedges' g, except the pre-to-post row, a standardised mean change)."; Problem: "Hedges'" does not appear anywhere in the unit's text. Also, "sport performance" is wrong for the Low row, which pools law enforcement studies; Fix: "Pooled effects on performance: point estimate and 95% confidence interval, as each source gives them (g, except the pre-to-post row, a standardised mean change)."; Basis: unit §2 and §6; https://researchportal.hw.ac.uk/en/publications/pressure-training-for-performance-domains-a-meta-analysis/

[should-fix] [attribution] Sources; Current: "[Authors not shown on the pages opened.] The effect of manipulating training demands and consequences on experiences of pressure in elite netball. *Journal of Applied Sport Psychology* 2017;29(4):434–. https://doi.org/10.1080/10413200.2017.1298166 (abstract read at the publisher's page; journal, year, volume, issue, first page and DOI from the UK Research Excellence Framework 2021 record; authors and end page not verified)"; Problem: the Essex and British Library records both give the authors as Mike Stoker, Ian Maynard, Joanne Butt, Kate Hays, Pete Lindsay and Danielle Adams Norenberg, and the pages as 29(4):434–448; Fix: "Stoker M, Maynard I, Butt J, Hays K, Lindsay P, Adams Norenberg D. The effect of manipulating training demands and consequences on experiences of pressure in elite netball. *Journal of Applied Sport Psychology* 2017;29(4):434–448. https://doi.org/10.1080/10413200.2017.1298166 (abstract read at the publisher's page; authors and pages from the University of Essex repository record and the British Library catalogue record)"; Basis: https://repository.essex.ac.uk/26359/ ; https://eld.bl.uk/catalog/100049540513_0x000001 (source log row 5 needs the same change)

[should-fix] [attribution] §3 Consequences; Current: "[netball study, 2017, abstract read]"; Problem: the authors are now known; Fix: "[Stoker et al., 2017, abstract read]"; Basis: as above

[should-fix] [attribution] Sources; Current: "*Journal of Applied Sport Psychology* 2022. https://doi.org/10.1080/10413200.2022.2061637 (abstract read on Liverpool John Moores University's repository; volume and issue not shown)"; Problem: the version of record is 2023;35(4):710–730, published online in April 2022; Fix: "*Journal of Applied Sport Psychology* 2023;35(4):710–730 (online 2022). https://doi.org/10.1080/10413200.2022.2061637 (abstract read on Liverpool John Moores University's repository; volume, issue and pages from the University of Essex repository record)"; Basis: https://repository.essex.ac.uk/32658/ (source log row 2 needs the same change)

[should-fix] [accuracy] §7 table, quiet eye; Current: "[moderate, positive; rule 4 on the review's count; samples include trained novices]"; Problem: the review lists 4 of the 7 quiet-eye studies as trained novices and 2 as experts, and calls 1 inconclusive. That leaves fewer than three agreeing controlled studies in athletes, so rule 4 does not apply and rule 5 does; Fix: "[weak, positive; by the review's account four of the seven studies trained novices and two sampled experts, so fewer than three controlled studies in athletes agree, rule 5]"; Basis: Gröpel & Mesagno 2019 (above); SP1 §9 (notes Need 3 and §7's sentence on what has "the most support" should follow this change)

[should-fix] [accuracy] §6; Current: "mainly so that they accept it"; Problem: the authors' main reason is a stronger subjective benefit from a tailored routine; they raise acceptance and motivation only as a possible reason they did not test; Fix: "because the athlete's subjective benefit, and their acceptance of the routine, may be greater when it is tailored"; Basis: Rupprecht et al. 2024, https://informahealthcare.com/doi/abs/10.1080/1750984X.2021.1944271

[should-fix] [deliverable] Deliverable A, common to both squads; Current: "Each athlete starts the block at the level they reached in SP5's block (level 2 at most)."; Problem: §5 says Milan's squad's SP5 week-4 rondo was level 4, which conflicts with "level 2 at most"; Fix: "Each athlete starts the block at level 1 or 2, the highest of those they reached in SP5's block; a level-4 drill in SP5's block, such as Milan's squad's week-4 rondo, does not count, because SP5's block had no step-down rule."; Basis: unit §5; SP5 Deliverable A, week 4

[should-fix] [deliverable] Deliverable A, Milan's week 3, Tuesday; Current: "Second game: the same, with the bench making match noise and the coach-referee giving one wrong call."; Problem: the whole squad goes from level 4 to level 5 in one session. That breaks §5's readiness rule: meet the standard at the level below across a session, and want to go up; Fix: "Second game, only for players who met the standard in the first and want to go up (section 5, readiness; the others record from the bench): the same, with the bench making match noise and the coach-referee giving one wrong call."; Basis: unit §5, "Readiness to climb"

[should-fix] [figure] §5 flow caption; Current: "The pressure ladder: six levels, each adding one source of pressure to the one before."; Problem: not stated in the text. Level 6 adds several sources of pressure at once; Fix: "The pressure ladder: six levels, each adding to the pressure of the one before."; Basis: unit §5 table

[minor] [attribution] §3, first paragraph; Current: "[Low et al., 2022, abstract read]"; Problem: the in-text year should match the version of record, as the unit already does for Rupprecht; Fix: "[Low et al., 2023, abstract read]"; Basis: https://repository.essex.ac.uk/32658/

[minor] [attribution] §3 matrix caption; Current: "the netball study (2017);"; Problem: the authors are now known; Fix: "Stoker et al. (2017);"; Basis: https://repository.essex.ac.uk/26359/

[minor] [attribution] Sources, Alder; Current: "2016;38:93–104. https://doi.org/10.1123/jsep.2015-0145 (accepted manuscript read in full at Leeds Beckett University's repository, not the publisher's page; issue number not shown)"; Problem: the issue is 1; Fix: "2016;38(1):93–104. https://doi.org/10.1123/jsep.2015-0145 (accepted manuscript read in full at Leeds Beckett University's repository, not the publisher's page; issue from the Sport-IAT index record)"; Basis: https://lida.sport-iat.de/ta/Record/4045474?lng=en

[minor] [attribution] Sources, Gröpel & Mesagno; Current: "second author from the course's seed list"; Problem: the publisher's permissions page shows both authors; Fix: "second author shown on the publisher's permissions page"; Basis: https://informahealthcare.com/doi/permissions/10.1080/1750984X.2017.1408134?scroll=top

[minor] [accuracy] §10; Current: "describes the evidence as limited and mostly indirect"; Problem: I did not find this wording in the full text. The paper says "in only a few studies were these risk factors included in multiple risk factor modelling"; Fix: "notes that only a few studies have modelled these risk factors together"; Basis: Schwellnus et al. 2016, https://bjsm.bmj.com/content/50/17/1043.full

[minor] [figure] §7 table; Current: "| Reappraisal cue | 1 | Null."; Problem: the text read gives no count for reappraisal studies, and they sit inside the acclimatisation category; Fix: "| Reappraisal cue | not stated in the text read (within acclimatisation) | Null."; Basis: Gröpel & Mesagno 2019

[minor] [label] §7 table, left-hand contractions; Current: "[moderate, positive; rule 4 on the review's count; ages not given in the text read]"; Problem: whether the samples were athletes is not given either, and the grade has no under-18 label; Fix: "[moderate, positive; rule 4 on the review's count; ages and athlete status of the samples not given in the text read; for under-18s inference]"; Basis: Gröpel & Mesagno 2019 (mean age 20 to 40 in 68% of studies); SP1 §9

[minor] [label] §7 table, dual task; Current: "[moderate, positive, during performance only]"; Problem: no population label on evidence from mostly adult samples; Fix: "[moderate, positive, during performance only; for under-18s inference]"; Basis: as above

[minor] [label] §5 readiness; Current: "[weak, for the harm of distraction during learning; practice, for the readiness rule]"; Problem: no inference label on a finding from adult samples; Fix: "[weak, for the harm of distraction during learning, for under-18s inference; practice, for the readiness rule]"; Basis: as above

[minor] [figure] §3 matrix, "A wrong call" row; Current: "{"mark": "level 5, announced", "tone": 4}"; Problem: level 5 is 13 and up, and every other level-5 cell says so; Fix: "{"mark": "level 5, 13 and up, announced", "tone": 4}"; Basis: unit §5, "Caps by age"

Every Current string occurs exactly once in unit.md (checked with grep -cF).

## Confirmed (PASS)
- **Low 2021 (abstract):** 14 studies, 10 in sport and 4 in law enforcement, 394 participants; g = 0.67 (0.43 to 1.12), I² = 17.1%; no clear moderators; the conclusions as stated. https://researchportal.hw.ac.uk/en/publications/pressure-training-for-performance-domains-a-meta-analysis/
- **Oudejans & Pijpers 2009 (abstract):** 17 basketball players and 17 darts players. https://research.vu.nl/en/publications/training-with-anxiety-has-a-positive-effect-on-expert-perceptual--2/
- **Alder 2016:** 30 players, mean age 21.2, three groups of 10, three sessions of about 30 minutes; p = .04 and p = .02; field test; the "bottom 20%" and filming manipulations. https://eprints.leedsbeckett.ac.uk/id/eprint/2528/6/Alder%20et%20al.%2C%202015.pdf
- **Gröpel & Mesagno 2019:** 36 articles and 47 studies; 62% experienced athletes, "mostly from collegiate sports and nonprofessional clubs and leagues"; 32% novices; mean age 20 to 40 in 68%; 15 sports (golf 15, soccer 6, basketball 5); pressure artificial in 91%; ego relevance 23, video 19, simulated competition 18, audience 9; 4 real competitions; MMAT 34 of 38 at 50%, with the risk of exaggeration; filming alone may not raise anxiety; PPR 7, never worse; quiet eye 7, 1 inconclusive; left hand 5, 30 seconds, right-hand controls choked; acclimatisation 10, 1 null; dual task helped for automated skills but harmed in training; analogy 3/3/1; process goals 2; neurofeedback 1; "Band-Aid fix". https://informahealthcare.com/doi/abs/10.1080/1750984X.2017.1408134 ; https://lida.sport-iat.de/ta/Record/4055257
- **Oudejans 2025 (abstract):** 16 youth gymnasts; the results as stated. https://research.hva.nl/en/publications/high-pressure-protocol-during-practice-evokes-competition-like-ps/
- **Stoker 2016:** 11 coaches; task, forfeit and judgement demands; the quoted definition. https://ijsp-online.com/abstract/view/47/262
- **Kegelaers 2020:** 9 coaches and the 9 kinds of disruption. https://research.vu.nl/en/publications/a-coach-perspective-on-the-use-of-planned-disruptions-in-high-per/
- **Low 2022/23:** 8 and 8 participants; "approximating, but not replicating". https://researchonline.ljmu.ac.uk/id/eprint/16742/
- **Netball 2017:** mean age 26.14, randomised within-subject design; consequences raised pressure, demands did not. https://repository.essex.ac.uk/26359/
- **Kegelaers 2021:** groups of 10 (mean age 18.37) and 8 (17.76); non-random; 8 sessions of about 30 minutes over about 3 weeks; Table 1 contents; reflection; p = .208 and p = .013 (group B); performance not measured; frustration; younger players more sensitive to team consequences; "ethical and healthy manner"; "unrelenting environment". https://core.ac.uk/download/387931251.pdf
- **Rupprecht 2024:** 33, 61 and 112; all three effects with their CIs; PI −0.54 to 1.95; 5 of 19 effects from competition; small-study effect; ages 11 to 40, no senior athletes, mostly male; 16 samples under 10 and 32 of 10–19; 15 sports (golf 15, basketball 13); self-paced skills; no moderators; 10–15 minutes; the quote; the single elements. https://informahealthcare.com/doi/abs/10.1080/1750984X.2021.1944271
- **Mountjoy 2016:** both quotations and the normalisation sentence. https://bjsm.bmj.com/content/50/17/1019
- **Soligard 2016 (abstract):** psychological load and travel; monitoring. https://repository.up.ac.za/handle/2263/57024?show=full
- **Schwellnus 2016:** life events and daily hassles; young elite soccer players; reduce load under stress; "Variation in an athlete's psychological stressors should guide the prescription"; periodic stress assessments. https://bjsm.bmj.com/content/50/17/1043.full

## (3) Figures in text
PASS. Every number names its source. Case numbers are marked *added* or as examples.

## (4) Labels
PASS, apart from the three missing inference labels above. Abstract-only reads are labelled at first citation, and interview studies are labelled as testing nothing.

## (5) Deliverable
Built in full for Dani, Milan and Sara, each with a template whose blanks say what goes in them. Grades are honest, and the plans can be used alone. The problems are the two errors and two should-fixes above: referred athletes taken past the level-2 cap, the starting level, and Milan's jump from level 4 to 5 in one session.

## (6) Errata and pointers
No errata. These pointers check out:
- SP5 §4 stage 3, quoted exactly ("a scored game, a timed rep, a teammate watching").
- The SP5 week-4 rondo is level 4.
- SP5 §3.4: no slow breathing before a reaction start.
- SP5's stop rule.
- SP3: no exercise as punishment [practice] and no selection as a threat [practice].
- SP3's harsh-coaching grade [weak, against] and its parents' page.
- SP4's normal-or-refer table, §5 choking accounts, §9 check-ins and §10 first fifteen minutes.
- SP1's list entry on the mental-toughness trait.
- Case facts from SP2 and SP4.

"SP7's baseline sheet" points to a unit not yet written, so it could not be checked; it is not a finding.

## (7) Figures
1. **Range, §2: FIX (error).** All numbers trace to §2 and §6. "Hedges'" is not in the text, and the Low row is not sport-only. The kind fits. Full replacement caption: "Pooled effects on performance: point estimate and 95% confidence interval, as each source gives them (g, except the pre-to-post row, a standardised mean change). From sections 2 and 6 of this unit: Low et al. (2021), abstract, 14 studies in sport and law enforcement, 394 participants; Rupprecht et al. (2024), 61 samples aged 11 to 40."
2. **Matrix, §3: FIX (minor).** The "wrong call" cell and the netball label in the caption. All other cells trace to §3 and §4. The kind fits.
3. **Flow, §5: FIX (should-fix).** "One source each" is not in the text. Labels match the table. The kind fits. Full replacement caption: "The pressure ladder: six levels, each adding to the pressure of the one before. This unit's own construction, untested as a sequence in any study opened [practice]; the sources of pressure come from section 3 of this unit (Gröpel & Mesagno, 2019; Kegelaers et al., 2020 and 2021; Low et al., 2024). Athletes about 10 to 12 stop at level 3 and rehearse level 6 as a game without a consequence."
4. **Decision, §5: PASS.** The questions and outcomes match the step-down bullets, the caption names its section and source, and the kind fits.

## The seven passes

**Claims.** Checked as above. Not opened:
- **Low et al. 2024, accepted manuscript.** The LJMU PDF fetch was refused by the permission check. I read the HW, LJMU and Essex records for citation and abstract only. These claims are therefore unverified, not PASS: little youth guidance; the forfeit examples; limiting repetitions; "not overwhelmed"; graded exposure; "might initially impede skill acquisition"; once a month "not enough"; transparency; the debrief questions; arguments both ways before competition; self-worth.
- **Low 2021 full text.** The SHU PDF was refused and the SHU record was bot-blocked.

**Bibliography.** 12 of 15 entries match their records:
- Low 2021 and Low 2024 (Essex gives 2023 as the online year).
- Stoker 2016, Kegelaers 2020 and 2021, Oudejans 2009 and 2025.
- Mountjoy, Schwellnus (PubMed), Soligard.
- Gröpel & Mesagno.
- Rupprecht: surnames confirmed by an idw press record; initials not confirmed.

Wrong or incomplete: Low 2022, the netball study, Alder. No reference is non-existent.

**Source log.** All 15 entries have a row, and abstract-only claims are labelled in the text. Rows 2 and 5 need the corrected citations.

**Grades.** Pressure training [moderate] passes rule 4, and routines [moderate] passes rule 4. [weak] and [practice] grades are correct. Analogy under rule 5 is correctly argued. Quiet eye fails (should-fix); left-hand contractions is unverified (minor). The unit states that no technique reaches strong under rule 3, which is correct.

**Population.** Each finding names its sample. Transfers to under-18s are labelled inference, apart from three gaps (minor).

**Scope and safety.** PASS:
- Nothing teaches assessment, diagnosis or treatment. The unit says it is "not exposure therapy", and step-out goes to the scope card.
- Return from injury is handed to the person who manages it.
- Weight is excluded (rule 7), and Dani's snack goes to her scope card.
- No weight-loss, calorie or self-harm content.
- The law is put as a question for the welfare officer, with the disclaimer present.
- No real person is named.

**Any sport.** PASS. Counting examples:
- Athletics 3, swimming 2, basketball 2.
- One each: volleyball, tennis, gymnastics, rowing, golf, judo, football, and a generic team sport.

That is 15 in all, with no sport above 3. With study samples added, basketball is 4 of 21. The private-terms script on unit.md printed "1 files, 0 private terms, 0 warnings: OK".

**Part 7, line by line.** Every line passes except:
- Record match (Low 2022, the netball study, Alder).
- Grades (quiet eye).
- Inference labels (three gaps).
- Deliverable (the two §11 errors).

Search is off, so the dating line does not apply.

**F65.** PASS, with one should-fix. §5 builds SP5 §4 stage 3 and quotes it exactly. It maps SP5 weeks 2, 4, 6 and 8 to levels 1 and 2, with the rondo at level 4. It applies the step-down rule back to those weeks and places the block in weeks 9 to 12. The one problem is the deliverable's "(level 2 at most)" against the level-4 rondo. Dani's squad had no SP5 block, so this unit adds one as a fact, listed in the notes.

**Read as the coach.** Usable: the ladder, the seven rules and the step-down rule could be run on Monday. The most consequential defect is that a coach of a referred athlete would follow the Milan and Sara tables past §11's cap. The §7 table is dense on a phone; this is not a finding.

Not opened: Low et al. 2024 manuscript (refused), Low et al. 2021 full text (refused and bot-blocked), the netball LJMU and ref pages (refused), Rupprecht initials.
