---
audit: quality review (docs/public-courses.md §3 rule 13)
unit: DD-SP3 · Deep dive: tuning out the noise
course: sport-psychology · Sport Psychology for Coaches
model: claude-opus-5-5
date: 2026-11-21
chat: https://claude.ai/code/session_01KMmgQxLz98LrpygbnweyMU
verdict: fix · 1 error, 12 should-fix, 8 minor
---

The reviewer's final report, verbatim, from its hand-back (its write to a file was refused by the harness). Saved before any finding was applied. The reviewer was given the unit without its notes, unsure list, source log or earlier check.

# Quality review · DD-SP3 · Deep dive: tuning out the noise

Model: claude-opus-5-5. Date: 21 Nov 2026. Live search on.

**What I checked against:** unit.md, brief.txt, flags.txt, sourcing-standard.md (Parts 1 and 7), case-facts.md, SP1 section 9, and the eleven other filed units.

**Fetches not checked** (refused or redirected; none retried, none read from a copy):
- Bartura et al. (2024) at informahealthcare.com: refused.
- Wegner et al. (1998) at psychologicalscience.org: refused.
- Moser et al. (2017) at ncbi.nlm.nih.gov/pmc: 302 redirect.
- Fortes et al. (2021a), the accepted manuscript at cris.unibo.it: refused.

## Pass 1 · Claims (each source opened by me)

1. **§2, Wegner et al. (1998):** not opened.
2. **§2 and Card 1, Woodman et al. (2015):** PASS. Every figure matches:
   - Study 1: 40 male university hockey players, mean 20.25; 30 penalties per condition; £100 prize; order counterbalanced.
   - Target hits 11.70 to 9.85; hits in the avoided zone 6.95 to 8.77; other misses 11.53 in both conditions.
   - Study 2: 73 adults with little or no darts experience.
   - Within-subject; no comparison of avoid against positive instructions.
   - Read at https://core.ac.uk/download/186464386.pdf and https://research.bangor.ac.uk/en/publications/dont-miss-dont-miss-doh-performance-when-anxious-suffers-specific/
3. **§2, Bartura et al. (2024):** not opened, all claims.
4. **§2 and Card 1, Gorgulu & Gokcek (2021):** PASS. Fixed order, no control group, ironic-zone serves 2.40 against 2.68 (not significant), overall score unchanged (p = .50), "did not provide support for the Wegner's theory". https://jhk.termedia.pl/The-Effects-of-Avoiding-Instructions-Under-Pressure-An-Examination-of-the-Volleyball,158593,0,2.html
5. **§3, §4 and Card 2, Hatzigeorgiadis et al. (2011):** PASS. 32 studies, 62 effect sizes, ES = .48, moderators as stated, participants not described. https://www.psychologicalscience.org/journals/perspectives/1745691611413136/
6. **§3 and Card 2, the 2012 IJSEP runners' study:** PASS. 81 runners, 2×3 design, no between-group difference, the three named groups improved. https://informahealthcare.com/doi/abs/10.1080/1612197X.2012.645135
7. **§5 and Card 3, Hardy et al. (2019):** PASS. 16 men, mean 21.99; 1045 s against 1068 s; d = .24; 13 of 16 faster; RPE unchanged; no no-self-talk condition. https://pure.bangor.ac.uk/ws/portalfiles/portal/22735215/2019_To_me_to_You_.pdf
8. **§5, Moser et al. (2017):** not opened.
9. **§6 and Card 4, Moore et al. (2015):** PASS. 50 participants, mean 20.24, no putting experience; one putt; radial error 8.64 against 24.92 cm; d = 0.93; arousal rated more helpful; cardiovascular difference not significant (p = .174). https://eprints.glos.ac.uk/2885/1/Reappraising%20threat%20how%20to%20optimize%20performance%20under%20pressure.pdf
10. **§6 and Card 4, Sammy et al. (2017):** PASS. 54 novice undergraduates, mean 21.72; challenge index higher; resources and confidence higher; group × time p = .72; "did not improve performance, above that achieved by the control group". https://eprints.glos.ac.uk/4661/1/The%20effects%20of%20arousal%20reappraisal%20on%20stress%20responses.pdf
11. **§6, Gröpel & Mesagno (2019):** PASS. Reappraisal cues are among the null effects, and the study is not named outright. https://informahealthcare.com/doi/abs/10.1080/1750984X.2017.1408134
12. **§7 and Card 5, Gollwitzer & Sheeran (2006):** PASS. 94 tests; d = .65; shielding from unwanted influences; samples not described. https://kops.uni-konstanz.de/entities/publication/2e749bfb-8533-437c-8203-7e788c910c5f
13. **§7 and Card 5, Achtziger et al. (2008), Study 2:** PASS. 107 players aged 14 to 68, mean about 34; four plans chosen from lists; blind ratings; if-then group higher; more anxiety than the goal-only group; mechanisms not measured. https://www.socmot.uni-konstanz.de/sites/default/files/08_Achtziger_Gollwitzer_Sheeran_Implem.intentions_and_sh%282%29.pdf
14. **§8 and Card 6, Rupprecht et al. (2024):** PASS. Every number matches. https://informahealthcare.com/doi/abs/10.1080/1750984X.2021.1944271
15. **§10, figure 1 and Card 9, Chua et al. (2021):** PASS. https://pure.psu.edu/en/publications/superiority-of-external-attentional-focus-for-motor-performance-a/
16. **§10, figure 1 and Card 9, McKay et al. (2024):** PASS. Corrected g 0.01, 0.15, 0.09, −0.01; Bayes factors favour the null; "small to nil". https://experts.mcmaster.ca/display/publication3486012
17. **§12 and Card 11, Delleli et al. (2023):** PASS on every figure. One minor wording issue: "many trained or active athletes" leaves out the untrained participants (finding m5). https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2023.1293783/full
18. **§12 and Card 11, Fortes et al. (2021a):** partly checked, from the abstract only. https://cris.unibo.it/handle/11585/945192
    - Confirmed: 24 young male players, pair-matched and randomised, four weeks, decision-making in attack and passing improved only in the control group.
    - Not shown: the control group's "Olympic documentaries" (the abstract says "watched TV"), national level, age 15.7, 20 sessions, the mental-fatigue result.
19. **§12 and Card 11, Fortes et al. (2021b):** PASS. 25 international-level swimmers, mean 20.4; randomised crossover; about 2% slower at 100 and 200 m in the second 50 m; 50 m unchanged; the degrees-of-freedom and jump inconsistencies are real. https://cris.unibo.it/bitstream/11585/945207/6/PMS-20-0172.R2_Proof_hi.pdf
20. **§13 and Card 12, Ring et al. (2019):** PASS. 60 undergraduates, mean 19.45, mostly basketball novices; anger and distraction results; baskets unchanged (p = .84); mediation through distraction. https://eprints.leedsbeckett.ac.uk/id/eprint/4922/1/EffectsofOpponentVerbalAntisocialBehaviouronAngerAttentionandPerformanceAM-STANGER.pdf

## Pass 2 · Bibliography

**Matches the publisher's or institution's record:** Achtziger; Chua; Delleli; Fortes 2021a; Fortes 2021b (including the "Nasicmento" misspelling, which the unit notes); Gollwitzer & Sheeran; Gorgulu; Hardy; McKay; Moore; Sammy; Woodman.

**Wrong:** Ring et al. The entry uses the accepted manuscript's title. The published title is "Effects of antisocial behaviour on opponent's anger, attention, and performance" (s9).

**Incomplete:** the 2012 IJSEP study has no authors or title (s10).

**Not checked:**
- Bartura and Wegner: pages refused. Wegner's fields are stated in the unit as coming "from Crossref via the course list".
- Moser: redirect.
- Gröpel, Rupprecht (initials missing) and Hatzigeorgiadis (initials, volume, pages): the pages I opened did not show the fields.

No reference was found to be non-existent.

## Pass 3 · Source log

- **Labels pass.** Every in-text citation says whether it rests on the abstract, part of the text or the full text, and names the repository for each repository copy.
- **Gap:** the unit has no source log and names no file for one (s12).

## Pass 4 · Grades

**Correct by SP1's key:**
- §2: weak by rule 5; the youth sub-grade fits Gorgulu.
- §3: weak.
- §4.
- §5: weak.
- §7: weak.
- §8: moderate by rule 4, as SP6.
- §10: contested by rule 1; F74 is left open.
- §11: moderate for programmes, practice as a single step.
- §12: weak for music and phones.
- §13.

**Defensible:** §6, weak, mixed. It differs from SP6's grade and the unit does not say so (m1).

**Wrong:**
- §9, §15 and Card 8 quote SP5's breathing grade as "weak, no benefit shown". SP5 section 3.4 gives "[weak, mixed in the laboratory, no competition outcome tested]"; the quoted wording is SP8 section 11's (s1 to s3).
- §10 says the samples are undescribed and leaves out what SP5 section 3.5 reported: 566 mostly novice adults, and 49 athletes with no significant difference (Reinebo). §15, Card 9 and figure 2 repeat the omission (s4 to s7).

**Rule 3:** §15 states plainly that no technique reaches strong. Pass.

## Pass 5 · Population

- Every finding names its sample, or says the abstract gives none.
- Every transfer to under-18s is labelled inference or outside the sampled ages.
- Every card has a "Tested on" line.
- Cards resting on adults outside sport are weak. Cards 4 and 8 say why in the grade line; Cards 1 and 5 show it in "Tested on". Acceptable.
- Exceptions: figure 2 row 9 (s6), and Card 11's music grade has no age label (m7).

## Pass 6 · Scope and safety

Pass on every item:
- No assessment, diagnosis or treatment. Distress goes to the first conversation, SP4's table, the scope card and SP9; injury goes to the medical staff.
- No weight content; DD-SP2's language card is pointed to.
- No method of self-harm.
- No law is stated as the reader's. Device rules are a question for the organiser; abuse goes to the officials and DD-SP1's route; the information-not-advice line is there.
- No real person is named.
- "No phrase is proven", and every script is marked as an example.

## Pass 7 · Any sport

- **Body examples (§1 to §18):** tennis 5, gymnastics 4, diving 3, fencing 3, volleyball, archery, handball, swimming, judo, high jump and cycling 2 each, basketball 1, football about 3. Pass.
- **Deliverable:** all football, because the brief builds it for Milan. Counted together with the body, football is over a third. I treat this as the brief's design, as in earlier units.
- **Owner check:** no owner-identifying content found. `kit/private_terms.py` is not in the workspace and was not run.

## Brief and deliverable

- Every Cover item is present (§1 to §17), and the popular claim is named (§2).
- Deliverables A to E are complete for Milan, then given as templates. The cards carry all seven fields, the pocket card fits one page, and the season-plan row is filled.
- **Missing:** the notes listing invented case facts, which the brief requires and the Deliverable claims exist; the unsure list (e1); a source log (s12).

## Flags naming DD-SP3

- **F6:** done in §2. Woodman and Wegner (1998, abstract) were opened, Wegner (1994) is stated as not opened, and the entry is regraded (still weak).
- **F52:** partly done. The JSEP and TSP papers were reached via repositories. Eysenck (2007), Beilock & Carr (2001) and Hase (2019) are neither used nor said to be unopened (m8).
- **F63:** done. The unopened and abstract-only references are stated.
- **F64:** done in §15.
- **F68:** done in §3 and §10. The regrade rests on two abstracts, which the unit says, and leaves out SP5's athlete data (s4).
- **F73:** done in §9 and Card 8.
- **F83:** done in §6. The difference from SP6's grade is not stated (m1).
- **F119:** done in §1, §12 and §13.
- **F125:** done in §18.
- **F168:** done in §19 and Deliverable E. Week 16's level-6 rehearsal breaks SP10's no-climbing rule between blocks (s7, s8).
- **F211:** not applicable.
- **F214:** done in §6, §9 and §11 and Cards 4, 8 and 10.
- **F216:** done in §17.
- **F218:** this review.

Flags that do not name DD-SP3 but were checked:
- F1, F8, F14, F47 and F124 are observed.
- F7, F24 and F86 are packet matters.

## Figures

1. **§10 range:** PASS. Every number is in the text, the caption names section and sources, and the kind fits competing estimates.
2. **§15 matrix:** FIX. The kind fits. Row 9's "not seen" under athletes contradicts SP5. Replacement row: `{"label": "9 Attention outward", "cells": [{"mark": "contested", "tone": 1}, "yes (SP5)", "not seen"]}` (s6).
3. **§16 flow:** PASS.
4. **§17 decision:** FIX, caption only. The tree draws four of the six signs and the caption does not say so (m6).

## Consistency with the filed units and the case

**Pointers confirmed:**
- SP1: the grade key and the ironic-effects entry.
- SP3: autonomy support, moderate, association.
- SP4: section 5 and its grade; Milan's quote.
- SP5: sections 1, 3.2, 3.6 and 5; week 8's optional breathing and mindfulness.
- SP6: sections 4, 5 and 9 (caps and step-down rule 3).
- SP7: Sara's headphones; Milan calling for the ball.
- SP8: sections 2, 4 and 11; 11:00 and 9:30; the Monday talk.
- SP10: the section 10 minutes, percentages and cutting order; the week-13 to 18 slot and week-24 rehearsal; weeks 35 to 38.
- DD-SP1 and DD-SP2 tools.

**Disagreements:**
- §9, §15 and Card 8: SP5's breathing grade is misquoted (s1 to s3).
- §10 and related: SP5's attentional-focus samples are left out (s4 to s7).
- §8 and Card 7: SP8 section 5 does not cover speaking to officials or a captain's query (m3, m4).
- Card 2: attributes to SP5 a keep that this unit invented (m2).
- Deliverable C week 16 and Card 11: level 6 between blocks breaks SP10 section 4. Block 1 reaches level 5 at most, so no player can be at 6 in week 16 (s7, s8).

**Case facts:** all agree with case-facts.md, and "(fictional)" is on each first use. The facts this unit invented are marked *added* but not listed (e1).

## Findings

[error] [coverage] Deliverable and end matter; Current: "## Sources"; Problem: the Deliverable says "Facts marked *added* are invented by this unit and listed in its notes", and the brief requires the notes, but the unit has no notes section and no unsure list (audit-units §3 starts from it); Fix: "## Notes\n\nFacts about the case invented by this unit (DD-SP3), for the case register: (1) At SP5's week-8 review Milan kept his self-talk phrase \"Scan, open, forward\". (2) In session 2 of Card 3 Milan chose the name version, \"Milan: scan, open, forward\". (3) Card 4 was offered to Milan in week 15 and he chose not to keep it. (4) Milan's four if-then plans (Card 5), written in session 1. (5) The order of Milan's staged pre-match routine: short-passing warm-up, Card 5's plans read once in the dressing room, his cue in the tunnel. (6) Milan's reset: clap once, breath out, \"Call, show, again\". (7) Breathing was offered to Milan at SP5's week 8 and not taken up. (8) Milan chose not to add a separate outward-attention card. (9) Milan's notice-name-return line: \"There's the nerves. Next ball.\" (10) Milan listens to his own playlist in the car, puts his phone in his bag from 9:30, and reads the squad message group after the match; he used to read it and social media in the dressing room. (11) Milan filled in the cue-word builder in session 1 of week 13, and his coach passed it in week 13; he practised the cue calm in SP5's weeks 3 and 4 and under pressure in SP6's block at levels 1 to 3. (12) The noise block sits in weeks 13 to 16 of SP10's plan for Milan's squad. (13) At week 16 Milan keeps Cards 1 to 3, 5, 6, 7, 10 and 11, and not Card 4, Card 8 or a separate Card 9. (14) Milan wrote his pocket card in week 16. Illustrations, not events: touchline words of a loud coach rewritten (Card 1); an opposing midfielder talking to Milan at a corner (Card 12).\n\n## Unsure list\n\nNot opened, so nothing rests on them: Wegner (1994); Tod et al. (2011); Wulf (2013); Brooks (2014); Jamieson et al. (2010); Kross et al. (2014); Terry et al. (music). Read in abstract only: Wegner et al. (1998); Hatzigeorgiadis et al. (2011); the 2012 IJSEP runners' study; Chua et al. (2021); McKay et al. (2024); Gollwitzer & Sheeran (2006). Read in part: Bartura et al. (2024), without its per-study table; Gröpel & Mesagno (2019); Rupprecht et al. (2024); Delleli et al. (2023). Bibliographic fields not confirmed at a publisher's page: Wegner et al. (1998); Rupprecht et al. (2024) initials; the 2012 IJSEP study's authors and title.\n\n## Sources"; Basis: brief.txt ("a fact the unit invents about them is listed in the notes"); audit-units-SKILL.md §3; case-facts.md header.

[should-fix] [attribution] §9; Current: "and [weak, no benefit shown in competition] for performance"; Problem: SP5 §3.4 grades it "[weak, mixed in the laboratory, no competition outcome tested]"; the quoted wording is SP8 §11's; Fix: "and [weak, mixed in the laboratory, no competition outcome tested] for performance"; Basis: SP5, section 3.4, Grade.

[should-fix] [attribution] §15; Current: "| 8. Slow breathing, early | [weak, positive, for heart rhythm; weak, no benefit shown for performance] |"; Problem: the same misquotation of SP5's grade; Fix: "| 8. Slow breathing, early | [weak, positive, for heart rhythm; weak, mixed in the laboratory, no competition outcome tested, for performance] |"; Basis: SP5, section 3.4.

[should-fix] [attribution] Card 8; Current: "[weak, positive, for heart-rate variability; weak, no benefit shown for performance; inference under 18]"; Problem: the same misquotation of SP5's grade; Fix: "[weak, positive, for heart-rate variability; weak, mixed in the laboratory, no competition outcome tested, for performance; inference under 18]"; Basis: SP5, section 3.4.

[should-fix] [accuracy] §10; Current: "the abstracts do not say how many participants were athletes or children."; Problem: leaves out the samples SP5 §3.5 opened, the course's only athlete evidence on this technique; Fix: "the abstracts do not say how many participants were athletes or children. SP5, section 3.5, reports the samples it opened: a network meta-analysis in 566 mostly novice healthy adults that found an external focus better at retention and transfer, and a pooled analysis of four crossover studies in 49 athletes (baseball, table tennis, golf; mean ages about 19) that found no significant difference between external and internal focus, which its authors say may reflect low power."; Basis: SP5 §3.5 (Favre-Bulle et al., 2024; Reinebo et al., 2024).

[should-fix] [accuracy] §15; Current: "| Samples not described in the abstracts read |"; Problem: the same omission; Fix: "| Samples not described in the abstracts read; in SP5, mostly novice adults, and 49 adult athletes with no significant difference |"; Basis: SP5 §3.5.

[should-fix] [figure] §15 matrix figure; Current: "\"9 Attention outward\", \"cells\": [{\"mark\": \"contested\", \"tone\": 1}, \"not seen\", \"not seen\"]"; Problem: "not seen" under athletes contradicts SP5, and the unit's own §10 once s4 is applied; Fix: "\"9 Attention outward\", \"cells\": [{\"mark\": \"contested\", \"tone\": 1}, \"yes (SP5)\", \"not seen\"]"; Basis: SP5 §3.5.

[should-fix] [accuracy] Card 9; Current: "Samples not described in the abstracts. |"; Problem: the same omission; Fix: "Samples not described in the abstracts; SP5 found mostly novice adults, and 49 adult athletes with no significant difference (section 10). |"; Basis: SP5 §3.5.

[should-fix] [deliverable] Deliverable C, week 16; Current: "(level 6 only where the cap allows; Milan's drill at 3)"; Problem: SP10 keeps one slot at each athlete's current level with no climbing between blocks, and puts the level-6 rehearsal in block 2 (week 24); block 1 reaches level 5 at most, so no player can be at 6 here; Fix: "(at each player's current level, no climbing, as SP10 sets between blocks; the level-6 rehearsal waits for week 24; Milan's drill at 3)"; Basis: SP10 §4 and Deliverable B.

[should-fix] [deliverable] Card 11; Current: "3: a level-6 rehearsal (where the cap allows) on the match timeline, phones in bags."; Problem: this session falls in weeks 15 and 16, between blocks; same rule as above; Fix: "3: a rehearsal of the match timeline at each player's current level and within their cap, phones in bags."; Basis: SP10 §4; SP6 §9.

[should-fix] [attribution] Sources, Ring et al.; Current: "Effects of Opponent Verbal Antisocial Behaviour on Anger, Attention, and Performance."; Problem: this is the accepted manuscript's title, not the published one; Fix: "Effects of antisocial behaviour on opponent's anger, attention, and performance."; Basis: https://research.birmingham.ac.uk/en/publications/effects-of-antisocial-behaviour-on-opponents-anger-attention-and-

[should-fix] [attribution] Sources, the 2012 IJSEP study; Current: "[Authors and title not shown on the publisher's page opened; abstract read.]"; Problem: the entry has no authors or title, so it cannot be matched to a record, and no search here found them; Fix: "[Authors and title not shown on the publisher's page opened and not found by the quality review's searches; abstract read; to be completed from the DOI's Crossref record before filing.]"; Basis: https://informahealthcare.com/doi/abs/10.1080/1612197X.2012.645135

[should-fix] [coverage] Sources heading; Current: "Every reference below was opened on 21 Nov 2026 at the address in the source log;"; Problem: the unit has no source log and names no file; the Wegner (1998) fields come from the course list, not from a page opened; Fix: "Every reference below was opened on 21 Nov 2026 at the address given where it is cited in the text, and what was read is stated there (the bibliographic fields of Wegner et al., 1998, are from the course list, not from a page opened);"; Basis: brief.txt; sourcing-standard Part 7, item 4.

[minor] [label] §6; Current: "Grade: reading arousal as readiness [weak, mixed;"; Problem: the grade differs from SP6's without saying so; Fix: "SP6 graded reappraisal cues [weak, no benefit shown under pressure] from the review alone; with the two randomised studies opened here, the direction is mixed. Grade: reading arousal as readiness [weak, mixed;"; Basis: SP6 §6, table.

[minor] [label] Card 2; Current: "\"Scan, open, forward\", before his first touch in the first fifteen minutes (SP5, kept at week 8)."; Problem: SP5 records no keep for Milan; Fix: "\"Scan, open, forward\", before his first touch in the first fifteen minutes (his SP5 phrase; kept at the week-8 review, *added*)."; Basis: SP5 Deliverable A, "Milan within the block".

[minor] [attribution] §8; Current: "What the rules of the sport allow an athlete or a coach to say to an official is SP8, section 5's question."; Problem: SP8 §5 covers a coach speaking to the athlete, not to officials; Fix: "What the rules of the sport allow an athlete or a coach to say to an official is a question for the competition's rules, asked and dated as SP8, section 5 asks its questions."; Basis: SP8 §5.

[minor] [attribution] Card 7; Current: "When a call needs a captain's legitimate query under the rules (SP8, section 5)."; Problem: SP8 §5 does not mention a captain's query; Fix: "When the sport's rules give the athlete or a captain a way to query a call (check and date the rule, as SP8, section 5 does for coaching)."; Basis: SP8 §5.

[minor] [accuracy] §12; Current: "many trained or active athletes)"; Problem: the source describes a mix of active or untrained people and trained athletes; Fix: "a mix of active or untrained people and trained athletes)"; Basis: https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2023.1293783/full

[minor] [figure] §17 decision figure caption; Current: "What to do when a technique may be making an athlete worse. From section 17 of this unit:"; Problem: two of §17's six signs are not drawn and the caption does not say so; Fix: "What to do when a technique may be making an athlete worse; two of section 17's signs (the routine grows; it needs you) are not drawn and lead to simplifying or dropping the technique. From section 17 of this unit:"; Basis: unit §17.

[minor] [label] Card 11; Current: "music the athlete chooses [weak, positive, small; laboratory tasks]"; Problem: the age label given in §12 is missing; Fix: "music the athlete chooses [weak, positive, small; laboratory tasks; for 10 to 15 outside the sampled ages]"; Basis: unit §12.

[minor] [coverage] Preamble; Current: "(Chua et al., 2021; McKay et al., 2024), which were read in abstract."; Problem: the references F52 names are neither used nor said to be unopened; Fix: "(Chua et al., 2021; McKay et al., 2024), which were read in abstract. The anxiety references flag F52 names (Eysenck et al., 2007; Beilock & Carr, 2001; Hase et al., 2019) were not opened; this unit uses SP4's accounts of choking in their place."; Basis: flags.txt F52; unit §1.

I checked that every Current string above occurs exactly once in unit.md.

Verdict: DD-SP3 · fix · 1 error, 12 should-fix, 8 minor

## Could not verify

1. **§2:** Wegner et al. (1998), the putting and pendulum findings and "the abstract describes no sample". The publisher page was refused.
2. **§2, §4 and Card 1:** Bartura et al. (2024), all claims:
   - 24 studies in 17 articles; 5 experimental and 19 quasi-experimental; 1,152 participants; mean age 21.78.
   - Skill levels 12/3/8/1; 22 of 24 studies consistent and 2 inconclusive.
   - Avoidance instructions part of the pressure in every study; ironic errors after positive instructions that name the target; process goals recommended.
   - One study with under-18s.
   - The 79% description of the quasi-experimental studies (the arithmetic is right).
   - The bibliographic fields 17(2):1378–1417.
3. **§5 and Card 3:** Moser et al. (2017): n = 29 and 50, d = 1.01, no control engagement, no performance measured, and the bibliographic fields. The fetch was redirected.
4. **§12 and Card 11:** Fortes et al. (2021a): national level; mean 15.7; 20 sessions; "Olympic documentaries" (the abstract says "watched TV"); the mental-fatigue result.
5. **§12:** the statistical inconsistencies, for Fortes et al. (2021a). They are confirmed for 2021b only.
6. **Sources:** Gröpel & Mesagno (2019), the volume, issue and pages.
7. **Sources:** Rupprecht et al. (2024), the initials, volume, issue and pages.
8. **Sources:** Hatzigeorgiadis et al. (2011), the initials, volume, issue and pages.
9. **Sources:** the 2012 IJSEP study's authors and title.
10. **Sources:** that every reference was opened on 21 Nov 2026. There is no source log to check against.
11. **§6:** the identity and sample of the reappraisal study in Gröpel & Mesagno (2019). The page does not name it.
12. **Pass 7:** `kit/private_terms.py` was not available to run.
13. **Sources:** Moser et al. (2017), Sci Rep article number 4519. It appears only in a search-result URL; no page was opened.
