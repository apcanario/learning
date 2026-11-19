---
audit: fresh check
unit: SP10 · The season plan
course: sport-psychology · Sport Psychology for Coaches
model: claude-opus-5-5
date: 2026-11-19
chat: https://claude.ai/code/session_01KMmgR2iBxJPhjunwizCmdb
verdict: fix · 0 errors, 4 should-fix, 17 minor
---

The checker's final report, verbatim, from its hand-back. Saved before any finding was applied.

Verdict: SP10 · fix · 0 error, 4 should-fix, 17 minor

Model: claude-opus-5-5. The write to /tmp/sp10/checker/out/report.md was refused, so the full report follows below.
Opened at the publisher: Pluhar 2019 (jssm.org), Rodrigues 2023 (scielo.br), Hertting 2020 (mdpi.com), Ferreira 2024 (frontiersin.org), Mitchell 2021 (abstract, via the Leeds Beckett record). Silva 2016: abstract only, via BVS/DOAJ. All pointers to SP1 to SP9 were opened in filed/.
Not opened: Silva's full text (90 athletes, mean age 21.6, 14-day retest). Not checked: Silva's authors and DOI. Ferreira's Crossref record was refused, and a redirected Frontiers URL was not retried.

---

Verdict: SP10 · fix · 0 error, 4 should-fix, 17 minor

Fresh check per audit-units-SKILL.md section 3, with the prompt used verbatim and the figures paragraph (item 7). Packet equivalents: brief.txt in place of units_data.py; no audit report for this course in the packet, so there were no errata to apply; filed/ for the course's filed units. A script confirmed that every Current string below occurs exactly once in unit.md.

## Findings

[should-fix] [accuracy] Section 10, "Why count"; Current: "Two sources were opened for this unit on coaches outside elite sport, because SP9 found nothing on them (SP9, section 11):"; Problem: only Hertting et al. is known to be about non-elite coaches. Ferreira et al. give no level for their coaches, and several of their included studies are of senior Australian football league, professional or high-performance coaches; Fix: "Two sources were opened for this unit because SP9 found nothing on coaches outside elite sport (SP9, section 11); only the first is known to be about such coaches:"; Basis: Ferreira et al. 2024, full text at https://frontiersin.org/articles/10.3389/fpsyg.2024.1301978/full (coach level not stated; the included studies' titles name professional, senior-league and high-performance coaches).

[should-fix] [accuracy] Deliverable A1, Competition line; Current: "No anxiety profile built. Looks to her coach after every exchange"; Problem: this contradicts SP4, which says Dani's look "is recorded on a profile". It is also missing from the notes' list of invented facts; Fix: "No check-ins yet (SP7's baseline sheet: not yet asked). Looks to her coach after every exchange"; Basis: filed SP4, Deliverable B, "Applied to the case": "Looking to her coach after every exchange is recorded on a profile (row 2's question: what is the worry?)"; filed SP7, Deliverable A, Dani: "\"How nervous, 0 to 10?\" Not yet asked."

[should-fix] [deliverable] Deliverable D, transition sheet; Current: "**Template: transition sheet.** One per athlete per transition."; Problem: the transition sheet is the only template with no version built on the case, which breaks the preamble's "built twice" rule; Fix: "**Built on the case: Milan (fictional), the academy decision.**\n\n| Line | Entry |\n|---|---|\n| Athlete and transition | Milan, 17: the academy's decision whether to keep him (selection or deselection); weeks 35 to 38 (*added*, Deliverable B). |\n| Predictable or not | Non-normative as SP2 sorts deselection; its date is known a season ahead. |\n| Before | Week 34: his development note rewritten (SP2) and parents reminded how the academy's decisions are explained, by whom and when (section 5); both outcomes talked through with him [practice; SP2, section 7]. |\n| The conversation | The week his decision is given, in private, by the person the parents' page names; the reason given privately, with what he can work on or do next (SP3, section 5). |\n| Study, work and life outside sport | Not yet on file: what he wants from sport and from life outside it if the decision goes against him (A2). |\n| What changes in the plan | Weeks 35 to 38 are heavy weeks: level 1, or he sits the slot out if he asks (Deliverable B). |\n| Where it leaves your part | Distress that lasts or spreads: SP4's table and the academy's medical staff; his referral continues whatever the decision (SP9, section 9). |\n| Follow-up | His development note rewritten after the decision (A2, Next rewrite). |\n\n**Template: transition sheet.** One per athlete per transition."; Basis: brief.txt preamble; sourcing-standard Part 7, deliverable line; filed SP3 Deliverable C, Milan's "Selection" paragraph.

[should-fix] [coverage] Deliverable B, weeks 7 to 8; Current: "| 7 to 8 | League begins | Imagery: calm (week 7); under pressure and review (week 8): \"Which of these is yours?\" | None |"; Problem: pre-season is six weeks, so imagery's first use falls in a league week. SP5's rule that a skill is first used in a lower-stakes competition is not applied, although section 4 says the first uses land in pre-season; Fix: "| 7 to 8 | League begins | Imagery: calm (week 7); under pressure and review (week 8): \"Which of these is yours?\"; first use in a league match you judge lower-stakes, otherwise it waits for one (SP5, Deliverable A, week 2) | None |"; Basis: filed SP5 Deliverable A, week 2: "if you judge it lower-stakes; if not, the first use waits for the next match that is".

[minor] [accuracy] Section 10, Ferreira bullet; Current: "the review does not say which levels its coaches worked at"; Problem: this misses that the included studies are named, and several are of professional or high-performance coaches; Fix: "the review does not state its coaches' level, and several of its included studies are of professional or high-performance coaches"; Basis: Ferreira et al. 2024, publisher's full text.

[minor] [population] Section 3; Current: "in one meta-analysis read in abstract, effects were greatest when coaches delivered the intervention [weak, positive] (SP5, section 2)"; Problem: the sample is not named; Fix: "in one meta-analysis of randomised trials in athletes, read in abstract, which gives no ages, effects were greatest when coaches delivered the intervention [weak, positive] (SP5, section 2)"; Basis: filed SP5 s2: "randomised controlled trials of psychological and psychosocial interventions in athletes ... The abstract gives no ages."

[minor] [population] Section 7; Current: "the gain in observed autonomy support faded within the season [weak, positive, for training your own behaviour deliberately] (SP3, section 3)"; Problem: the sample is not named, and SP3's inference label is dropped; Fix: "the gain in observed autonomy support faded within the season [weak, positive, for training your own behaviour deliberately; coaches of players aged 10 to 15, so for 16 to 25 an inference] (SP3, section 3)"; Basis: filed SP3 s3: "10 to 15 in the football trial, so for 16 to 25 it is inference".

[minor] [accuracy] Section 9, junior to senior; Current: "athletes who entered talent programmes younger performed better as juniors and worse as seniors"; Problem: the study compares groups of higher and lower performers, but the sentence reads as a forecast for one athlete; Fix: "higher-performing juniors had entered talent programmes younger, and higher-performing seniors had entered them older"; Basis: filed SP2 s10, same wording.

[minor] [accuracy] Section 9; Current: "Plan it as a transition that lasts months:"; Problem: the source says months to years; Fix: "Plan it as a transition that lasts months or years:"; Basis: filed SP2 s7: "lasting months to years".

[minor] [accuracy] Section 4; Current: "(a rowing crew's winter base phase, for example)"; Problem: this is an unsourced claim about a real sport's calendar; Fix: "(a crew whose winter base phase has no racing, for example)"; Basis: Part 1, nothing invented.

[minor] [attribution] Section 6; Current: "Most coaches reading this course work without one. The course is built for that case:"; Problem: the proportion is unsourced; Fix: "The course is built for that case:"; Basis: Part 7, claims sourced where made.

[minor] [attribution] Section 2; Current: "In clinical work a formulation is a clinician's explanation of a person's difficulties."; Problem: the definition has no source; Fix: "In clinical work a formulation is, as this unit uses the word, a clinician's explanation of a person's difficulties (the unit's description; no defining source was opened)."; Basis: Part 1; SP1 s1 handles its own working definition the same way.

[minor] [figure] Section 10 table; Current: "| 1 per check-in, 3 a week: 3 per athlete |"; Problem: Milan's check-ins run before each of four sessions and on match mornings, which makes five a week; Fix: "| 1 per check-in, 5 a week (four sessions and a match morning): 5 per athlete |"; Basis: unit A2 and B; filed SP4 Deliverable A, Check-ins.

[minor] [figure] Section 10 totals (applied with the check-in fix); Current: "in pre-season, 20 session minutes and 108 of your own (10 + 40 + 3 + 15 + 20 + 15 + 5); in a pressure block, 40 session minutes and 78 of your own; between blocks, 20 session minutes and 78 of your own."; Problem: the totals change; Fix: "in pre-season, 20 session minutes and 110 of your own (10 + 40 + 5 + 15 + 20 + 15 + 5); in a pressure block, 40 session minutes and 80 of your own; between blocks, 20 session minutes and 80 of your own."; Basis: arithmetic.

[minor] [figure] Section 10 compare caption (applied with the check-in fix); Current: "one athlete on a profile: 78 in all."; Problem: the total changes; Fix: "one athlete on a profile: 80 in all."; Basis: arithmetic.

[minor] [figure] Section 10 compare data (applied with the check-in fix); Current: "{\"label\": \"Check-ins for one athlete (SP4)\", \"value\": 3}"; Problem: the value changes; Fix: "{\"label\": \"Check-ins for one athlete (SP4)\", \"value\": 5}"; Basis: as above.

[minor] [figure] Section 4 matrix; Current: "{\"label\": \"Referral plan (SP9)\", \"cells\": [{\"mark\": \"check\", \"tone\": 2}, {\"mark\": \"each term\", \"tone\": 3}, null, {\"mark\": \"review\", \"tone\": 3}]}"; Problem: no off-season review of the referral plan appears in the text. The checks are before the season, each term (the last in week 38) and after any incident; Fix: "{\"label\": \"Referral plan (SP9)\", \"cells\": [{\"mark\": \"check\", \"tone\": 2}, {\"mark\": \"each term\", \"tone\": 3}, null, null]}"; Basis: unit s4 and B, weeks 35 to 44.

[minor] [figure] Section 4 matrix legend (applied with the matrix fix); Current: "\"kept skill, every competition, friendlies, weekly, each term, review, rewrite\""; Problem: no cell says "review" any more; Fix: "\"kept skill, every competition, friendlies, weekly, each term, rewrite\""; Basis: as above.

[minor] [accuracy] Section 10, last paragraph; Current: "name in your referral plan who you talk to after a hard week (SP9, Deliverable B)"; Problem: SP9's line is about who you talk to after an urgent event, not a hard week; Fix: "name in your referral plan who you talk to after an urgent event (SP9, Deliverable B)"; Basis: filed SP9 Deliverable B template: "My own support | Who you talk to after an urgent event."

[minor] [population] Section 9; Current: "as SP3's review of dropout from swimming reported from six studies of mixed design (SP3, section 7)"; Problem: the ages are missing; Fix: "as SP3's review of dropout from swimming reported from six studies of mixed design, in swimmers aged 5 to 30 (SP3, section 7)"; Basis: filed SP3 s7: "six studies, aged 5 to 30".

[minor] [coverage] Deliverable B, week 29; Current: "| 29 | League; week before the tournament | Kept skill | Tue at current level; Thu one level below |"; Problem: a Thursday slot is added between blocks, against section 4's rule of one slot a week and section 10's budget; Fix: "| 29 | League; week before the tournament | Kept skill | One slot, Tue, current level; no Thursday slot |"; Basis: unit s4: "Between blocks, the plan keeps one 15-minute slot a week".

## (7) Figures
1. Matrix, s4: FIX on the two findings above. The kind fits, and the caption names the section and sources. Every other cell traces to s4, s5 and B.
2. Decision, s8: PASS. Its nodes match "What is never dropped", "Is it used?" and "keep, change, drop". The kind fits.
3. Compare, s10: PASS as drawn. Its values match the table and sum to 78. Change it only if the check-in fix is applied.
4. Flow, Deliverable C: PASS. The steps and minutes match the table.

## Seven passes
- **Claims: FIX.**
  - Pluhar: PASS on 756 athletes aged 6 to 18 (mean 13.5); the clinic sample; one self-report item; 8%, and 13% against 7%; not significant after adjustment (OR 1.72, 0.9 to 3.2); the stated limitations.
  - Rodrigues: PASS on 62 players aged 18 to 20 at three Recife clubs; HADS; 9 (14.5%) and 4 (6.5%). The Discussion's 14.3% discrepancy is confirmed.
  - Hertting: PASS on 688 unpaid coaches, about 70% of whom coached 10- to 15-year-olds; a non-validated two-item index; M 2.20 of 5; the three predictors.
  - Mitchell (abstract): PASS on 259 males aged 12 to 18; both models supported, not within the same analysis.
  - Ferreira: PASS on 11 studies, questionnaire and interview designs, eight countries, no pooling, and the findings. FIX on the "outside elite sport" framing.
  - Silva: PASS on 127 students, two domains and ICC 0.91. The athlete–student difference is only "good discriminant validity" in the abstract. Not opened: 90 athletes, mean age 21.6, 14 days, "athletes higher".
- **Bibliography: PASS, with some fields not checked.**
  - Ferreira, Hertting, Pluhar and Rodrigues match the publisher field by field. Pluhar has no DOI, as the unit says.
  - Mitchell: 3(3), Article 4 and 2021 match. The DOI appears only in a search listing.
  - Silva: title, journal and 2016;22(1):42–47 match BVS. Authors and DOI not checked.
  - Crossref was refused, so not checked. No non-existent reference found.
- **Source log: PASS.** All six entries have a row with address, what was read and date. Mitchell is said to be abstract-only in the unit. Park and Neely carry no claim.
- **Grades: PASS.** Every grade matches the cited unit and SP1's key. The new associations are weak (rule 5). Consensus-only claims are [practice] with the note.
- **Population: FIX.** Three samples are unnamed. All new sources name their samples, and the gap at 10 to 12 is stated.
- **Scope and safety: PASS.**
  - The formulation is described as a coach's working note, never a diagnosis, in s2, A and the template.
  - Nothing teaches assessment. The unit says "Do not run" the AIMS on your squad.
  - No weight method, calorie figure or target weight; nothing on self-harm.
  - Law is put as questions, and the disclaimer is present.
  - No real person is named.
- **Any sport: PASS.** Football 5, judo 4, athletics 3, swimming 2, volleyball 2, gymnastics 2, rowing 1, cycling 1, for 20 in all. Football's share is 25%. kit/private_terms.py is not in the packet, and no real person, club or handle appears.

## Part 7, the coach's reading, coverage
- Part 7: every line holds except the attribution and population minors and the transition-sheet should-fix. The owner check could not be run.
- Read as the coach in the preamble: D's order works from week 1. Two things would confuse that reader: the block "in pre-season" running into league weeks 7 and 8, and "no anxiety profile" set against SP4.
- Brief: every Cover item is met (s2 to s10). Deliverables: two formulations, the season plan, the weekly review and the ordered templates are in full; the transition template has no case build.

## Confirmed (filed-unit lines, opened in filed/)
- **SP1:** s1, two routes via the AASP document; s2: "It gives the coach no part in assessment, diagnosis or treatment."; s4: "shows that people changed; it does not show that the technique changed them".
- **SP2**
  - s2 grade: "[moderate, positive, for the maturity–performance association in boys...; practice, for the selection rule".
  - s3: "the effect grew with the gap in relative age".
  - s7: normative and non-normative transitions; the 126-study review not opened; the athletic identity definition; the once-a-season question [practice; ISSP].
  - s9 and Deliverable A: the NSCA limit of 8 months, in the 10-to-12 row.
  - Deliverable B: the case facts and the "What I hold back" template line.
- **SP3**
  - The warning before s1: "an anxious athlete may also perceive the coach as harsher".
  - s3: "faded within the season".
  - s5: the selection steps.
  - s7: Zhang et al., ages 5 to 19, [moderate].
  - s9: [weak, positive...; practice, for the page's format]; Burke: "prevent firm conclusions".
  - Deliverable A: counts 7, 6 and 0; repeat after six weeks; "do not use them to compare coaches".
  - Deliverable C: "What we aim for" and "Selection".
- **SP4:** s7, no prediction; s9: "A high score is not a disorder."; Deliverable A, all of Milan's lines and the six-week review.
- **SP5:** s1: "ethically beyond many practitioners' professional competencies"; s2, the grades; s4, the stages and dose findings, [weak, positive, for longer practice]; s5: "An athlete for whom a skill does nothing is common"; s6; Deliverable A.
- **SP6:** s2, s4 (rule 3), s5 (ages 11 to 40), s7, s8 (two slots of about 15 minutes, heavy weeks, cap 3, the days before a competition, new athletes, Low's "once a month"), s9 (caps, one climb a week), s10 (questions 2 and 4), s12 and Deliverable A (weeks 9 to 12, Milan's own-level drill, the warm-up opening the rehearsal).
- **SP7:** s2; Deliverable A, all of Dani's and Milan's lines; the withdrawn row; scripts 1 and 2.
- **SP8:** s1, s6, s7 ("usually the next session"), s9 (the grade; the seat in the stands; the adult page goes to the athlete), s10 (each day from the top; medical staff decide return), s11 ("One cue per player at stoppages, then silence"); Deliverables A to C.
- **SP9**
  - s1: elite adults and elite youth only, and "never a diagnosis".
  - s2: injury as a risk factor.
  - s8: the handover with "no label, no cause, no score"; selection independent; the one question.
  - s9: 24 hours; "do not necessarily coincide".
  - s11: "nothing was opened" for club, school or volunteer coaches.
  - Deliverable B: each term and after any incident.
  - Deliverable C: Sara's parents.
- **s10 arithmetic:** 108 and 78 check; 20 of 360 is about 6%; 40 of 360 is about 11%.

## Flags
- **F8, F14, F47, F48:** handled in the preamble. F47 and F48 stay open for S-SP1.
- **F124, F137:** handled in the preamble; these stay [practice].
- **F37, F118:** handled in s5 and B.
- **F67, F70:** handled in s4; SP5's inference is labelled as SP5's.
- **F85:** handled in s4 and B, under SP6 s8.
- **F139:** handled in s4 and B.
- **F20:** partly met. Park was not opened, and the unit says so. AIMS studies were opened for 12 to 18 (abstract) and for students; there is no sample of athletes aged 19 to 25.
- **F108:** not met; the unit says so in s9.
- **F132, F142:** partly met. F142 has the should-fix above.
- **F21, F117:** not needed, because the unit makes no sleep claim of its own.
- **F130, F131:** not used; carried in the notes.
- **F134, F63:** for the deep dives.
- **F7, F24:** notes only.
- **F150:** a process step after this check.

## Case facts
- Checked against case-facts.md: every athlete fact in A1, A2 and B is in the register or in an earlier unit's added rows.
- Invented facts: these match the notes' items 1 to 7.
- Not listed in the notes: "No anxiety profile built" (should-fix above).
- Saturday as match day is called "SP5's added fact", but SP5 added only "at the weekend". Saturday narrows it and should go into the register.

## Could not verify
- Ferreira against Crossref: refused, so not checked.
- Silva: authors, DOI and full-text details not opened.
- Mitchell: DOI seen only in a search listing.
- kit/private_terms.py: not in the packet.
