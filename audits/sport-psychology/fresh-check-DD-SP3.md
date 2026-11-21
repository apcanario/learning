---
audit: fresh check
unit: DD-SP3 · Deep dive: tuning out the noise
course: sport-psychology · Sport Psychology for Coaches
model: claude-opus-5-5
date: 2026-11-21
chat: https://claude.ai/code/session_01KMmgQxLz98LrpygbnweyMU
verdict: fix · 0 errors, 3 should-fix, 10 minor
---

The checker's final report, verbatim, from its hand-back. Saved before any finding was applied.

Verdict: DD-SP3 · fix · error 0, should-fix 3, minor 10

# Fresh check · DD-SP3 (claude-opus-5-5, 2026-11-21; Part 7 + Part 1; brief.txt; no audit report: skip it)

Isolated context; only /tmp/pk-checker was read. Every page fetched came from a URL that a WebSearch in this context returned. Refused or redirected fetches are marked "not checked".

## (1) Coverage
Every item in the brief is covered.
- §1: noise inside and outside.
- §2: suppression, with the F6 regrade.
- §3: written against assigned cues (one study, abstract only, and the unit says so).
- §4: what makes a phrase usable, graded, with no proven list.
- §5: "you" or own name.
- §6: arousal read as readiness.
- §7: if-then plans.
- §8: routines and resets.
- §9: breathing, with no performance claim.
- §10: outward attention, regraded.
- §11: acceptance.
- §12: music, phones and social media.
- §13: the opponent and officials.
- §14: waiting.
- §15: every technique with its sample and grade.
- §16: training by age band.
- §17: how to tell a technique is making things worse.

The deliverable is complete:
- Twelve cards, each with every required field plus Milan's version.
- Cue-word builder, four-week plan and one-page pocket card, each built for Milan and then given as a template.
- An extra E (season-plan row).

## Findings
1. [should-fix] [attribution] Sources; Current: "- [Authors and title not shown on the publisher's page opened; abstract read.] A self-talk intervention study in 81 collegiate cross-country runners, assigned against freely chosen self-talk. *International Journal of Sport and Exercise Psychology* (DOI registered 2012). https://doi.org/10.1080/1612197X.2012.645135"; Problem: Part 7 requires each entry to match its Crossref or publisher record. This one has no authors, title, volume or pages. The reference does exist: the DOI resolves to its abstract. My searches found no record showing the authors. Fix: the applying chat opens the Crossref record for the DOI. Only if it confirms every field, it replaces the entry with "- [Authors as on Crossref]. [Title as on Crossref]. *International Journal of Sport and Exercise Psychology* [year];[vol]([issue]):[pages]. https://doi.org/10.1080/1612197X.2012.645135" and updates §3, Card 2 and source-log row 6. Otherwise the entry stays as it is. Basis: https://informahealthcare.com/doi/abs/10.1080/1612197X.2012.645135
2. [should-fix] [accuracy] §4; Current: "| It is instructional for a fine, precise task | The self-talk meta-analysis | [weak, positive; abstract read, participants not described; inference under 18] |"; Problem: a meta-analysis of 32 sport-task studies (ES = .48) fits rule 4 on its face. The unit grades it by rule 5 without saying why. Fix: "| It is instructional for a fine, precise task | The self-talk meta-analysis | [weak, positive; rule 5: the meta-analysis was read in abstract only and does not say whether its participants were athletes, so rule 4 cannot be shown to apply; inference under 18] |"; Basis: https://ir.lib.uth.gr/xmlui/handle/11615/28461
3. [should-fix] [label] Card 1; Current: "| **Milan's version** | His coach's touchline words, rewritten: "Show for it" in place of "Stop hiding!"; "Scan, open, forward" in place of "Don't play it back". |"; Problem: this states as fact that his coach shouted these words. They are not in case-facts.md and not listed in notes.md. Fix: "| **Milan's version** | Illustration, not an event: touchline words of the kind a loud coach uses, rewritten: "Show for it" in place of "Stop hiding!"; "Scan, open, forward" in place of "Don't play it back". |"; Basis: case-facts.md (Milan, DD-SP1 rows).
4. [minor] [attribution] Sources; Current: "Hatzigeorgiadis, Zourbanos, Galanis, Theodorakis (authors, year, volume and pages not shown on the page opened; from Crossref via the course list)."; Fix: "Hatzigeorgiadis A, Zourbanos N, Galanis E, Theodorakis Y (initials, year, volume and pages confirmed on a library catalogue record, 21 Nov 2026; the publisher's page opened showed the abstract only)." Also add this to source-log row 5. Basis: https://bvbvf1.bib-bvb.de/vufind/PrimoRecord/cdi_proquest_miscellaneous_1696683610 (6(4):348–356).
5. [minor] [label] Deliverable B template; Current: "| 7 Voice | "I", "you" or own name; the athlete picks (not below 14). |"; Problem: Card 3 and §16 exclude under-13s, not under-14s. Fix: "| 7 Voice | "I", "you" or own name; the athlete picks (not below 13). |"; Basis: Card 3, §16.
6. [minor] [label] §7; Current: "the athlete sample was mostly adult, so for 13 to 18 an inference, and for 10 to 12 outside the sampled ages]"; Problem: the sample was aged 14 to 68. Card 5 and the matrix already say "from 14". Fix: "the athlete sample was mostly adult, so for 14 to 18 an inference, and below 14 outside the sampled ages]"; Basis: Achtziger 2008, https://www.socmot.uni-konstanz.de/sites/default/files/08_Achtziger_Gollwitzer_Sheeran_Implem.intentions_and_sh%282%29.pdf
7. [minor] [accuracy] §7; Current: "The groups differed before the match (the if-then group reported more competition anxiety)"; Problem: the anxiety difference was only against the goal-intention group, not the no-goal group. Fix: "The groups differed before the match (the if-then group reported more competition anxiety than the goal-only group)"; Basis: same PDF.
8. [minor] [figure] §15 matrix; Current: ""from 15""; Problem: the text says "athletes over 15" (§11, Card 10). Fix: ""over 15""; Basis: §11, Card 10.
9. [minor] [figure] §17 decision; Current: ""Keep; review at the next block""; Problem: "next block" is not in the text. Fix: ""Keep; review on the date on its card""; Basis: Deliverable A template, line "Review".
10. [minor] [label] §6; Current: "The choking-interventions review in athletes classed reappraisal cues"; Problem: the page read does not give the reappraisal study's sample. Fix: "The review of choking interventions in sport classed reappraisal cues"; Basis: https://informahealthcare.com/doi/abs/10.1080/1750984X.2017.1408134
11. [minor] [accuracy] §12; Current: "relative mean power (0.38) and peak power (0.53)"; Fix: "relative mean power (0.38) and relative peak power (0.53)"; Basis: https://www.frontiersin.org/articles/10.3389/fpsyg.2023.1293783
12. [minor] [deliverable] Card 6; Current: "this card's plans read once in the dressing room"; Problem: the plans are on Card 5. Fix: "Card 5's plans read once in the dressing room"; Basis: Cards 5 and 6.
13. [minor] [label] Deliverable B; Current: "Calm in SP5's weeks 3 and 4; under pressure in SP6's block at levels 1 to 3."; Problem: an unregistered case fact that is not marked *added*. Fix: "Calm in SP5's weeks 3 and 4; under pressure in SP6's block at levels 1 to 3 (*added*)." Also add it to notes.md. Basis: case-facts.md.

All 13 Current strings were checked with grep and each occurs once in unit.md.

## Confirmed (claim, source)
- **Woodman 2015**: 40 male university hockey players, mean 20.25, 30 penalties per condition, £100, counterbalanced; target 11.70→9.85, ironic 6.95→8.77, non-ironic unchanged. Study 2: 73 adults, fixed order. Neither study compares avoid with positive instructions. Citation TSP 29(3):213–223. Sources: https://core.ac.uk/download/186464386.pdf ; Bangor record.
- **Bartura review**: 24 studies in 17 articles; 1,152 participants, mean 21.78; skill 12/3/8/1; one under-18 study; 22 of 24 consistent; finding on positive instructions that name the target. Citation 2024;17(2):1378–1417, author order as in the unit. Sources: publisher full page; Brage and Uludağ avesis records.
- **Gorgulu & Gokcek 2021**: 43 female players aged 13–16, mean 14.51; fixed order, no control group; no overall change; Wegner not supported. Citation JHK 78:239–249. Source: jhk.termedia.pl page.
- **Wegner 1998**: abstract as described; no sample given.
- **Hatzigeorgiadis 2011**: 32 studies, 62 effect sizes, ES = .48, moderators as stated; participants not described.
- **Runner study abstract**: as stated in §3.
- **Hardy 2019**: 16 recreationally active men; 10 km; 1045 against 1068 s, 2.2%, d = .24; 13 of 16 faster; RPE no difference; no control condition. Source: Bangor PDF.
- **Moser 2017**: Study 1, n = 29, LPP; Study 2, n = 50, d = 1.01; no cognitive-control engagement; no performance measure. Source: nature.com.
- **Moore 2015**: n = 50 novices, mean 20.24; randomised; one putt; 8.64 against 24.92 cm, d = 0.93; arousal rated more helpful; cardiovascular difference not significant. Citation JSEP 37(3):339–343. Source: Gloucestershire post-print.
- **Sammy 2017**: n = 54, mean 21.72; group × time p = .72; challenge-like index; higher resources and confidence; the authors' "did not improve performance" statement. Citation 30(6):619–629. Source: Gloucestershire post-print.
- **Gröpel & Mesagno 2019**: reappraisal cues null. Citation 12(1):176–201. Sources: publisher abstract page; lida record.
- **Gollwitzer & Sheeran 2006**: 94 tests, d = .65, shielding. Citation 38:69–119. Source: Konstanz record.
- **Achtziger 2008, Study 2**: 107 players aged 14–68, mean about 34; three arms; plans chosen from lists; blind ratings; if-then group above both other groups; mechanisms not measured. Citation 34(3):381–393. Source: Konstanz PDF.
- **Rupprecht 2024**: SMC 0.31 [0.18, 0.44]; g 0.64 [0.45, 0.83]; g 0.70 [0.24, 1.16]; no moderators. Citation 17(1):39–64. Source: lida record. The publisher fetch was refused, so the article, sample and sport counts were not checked.
- **Chua 2021**: every number in §10 and the figure. Citation 147(6):618–645. Source: Penn State record.
- **McKay 2024**: bias-corrected g 0.01, 0.15, 0.09, −0.01; Bayes factors favour the null; "small to nil". Citation 150(11):1347–1362, eight authors. Source: McMaster record. The full text was reached only by a redirect: not checked.
- **Delleli 2023**: 30 studies, 474 participants, ages 16.4–26.04; completion time −0.24 [−0.46, −0.01]; RMP 0.38; RPP 0.53; RPE n.s.; self-selected music better on 2 outcomes; possible publication bias. Authors as in the unit. Source: frontiersin.org.
- **Fortes 2021a**: 24 national male volleyball players, 15.7 ± 0.6; pair-matched, randomised; Olympic documentaries as control; 20 sessions over 4 weeks; results as stated. Citation 128(6):2745–2766. Sources: Bologna record and accepted manuscript.
- **Fortes 2021b**: 25 international swimmers, mean 20.4; randomised crossover; 100 and 200 m slower, 50 m not; about 2%; internal statistical inconsistencies confirmed. Title and 128(1):390–408 as in the unit; the repository prints "Nasicmento". Sources: Bologna record and proof.
- **Ring 2019**: 60 undergraduates, mean 19.45, basketball novices; random assignment; insults raised anger; both comment groups more distracted; baskets p = .84; indirect path through distraction. Citation 37(8):871–877. Source: Leeds Beckett accepted manuscript.

Not checked:
- Delleli: "many trained or active athletes" and "one study of nine".
- The Fortes "jump result the Discussion contradicts".
- All pointers to SP1–SP10, DD-SP1 and DD-SP2 (outside the folder).

## (6) Errata applied
There is no audit report, so this is skipped.

## (7) Figures
1. **Range, §10.** Every value traces to §10. The caption names the section and both sources, abstract only. The kind fits competing estimates. PASS.
2. **Matrix, §15.** The cells trace to the §15 table and §§2–14, except "from 15" (the text says "over 15"). The caption is fine and the kind fits. FIX: "over 15" (finding 8).
3. **Flow, §16.** The steps trace to sessions 1–4 and first use. The caption is fine and the kind fits a sequence. PASS.
4. **Decision, §17.** The questions and outcomes trace to §17, except "Keep; review at the next block". The caption is fine and the kind fits a rule with branches. FIX (finding 9).

## Seven passes
1. **Claims: PASS, with exceptions.** Every claim opened held, apart from the three minor accuracy items. The items listed under "Not checked" were not opened.
2. **Bibliography: PASS, with one should-fix.** 19 entries match their records field by field. None is nonexistent. The runner entry is incomplete (finding 1). Rupprecht's initials were not seen by this checker either.
3. **Source log: PASS.** All 20 Sources entries have a row in sources.md. Every abstract-only claim says "abstract read", and repository copies are labelled.
4. **Grades: PASS, with one should-fix.** The grades fit the key: routines moderate (rule 4); mindfulness programmes moderate (SP5's grade); outward attention contested (rule 1); the rest weak or practice. §15 says plainly that nothing reaches strong under rule 3. The self-talk grade's reason is missing (finding 2).
5. **Population: PASS, with minor inconsistencies.** Every finding names its sample, and transfers to younger athletes are labelled inference or "outside the sampled ages". All 12 cards state their sample. Cards resting on novice adults or studies outside sport (3, 4, 8) are graded weak and say why. The age-boundary inconsistencies are findings 5, 6 and 8.
6. **Scope and safety: PASS.**
   - No assessment, diagnosis or treatment is taught. Notice-name-return is labelled "not therapy", and distress leads to stop, first conversation and referral.
   - There is no weight-loss method, calorie figure or target weight. Body talk points to DD-SP2's card.
   - No self-harm method appears.
   - Device rules are put as a question for the organiser, and the disclaimer is present.
   - No real person is named.
   - Every phrase is labelled as an example, and the athlete writes their own.
7. **Any sport: PASS.**
   - Approximate counts in the body: football ~6; tennis 4; fencing, gymnastics, diving, swimming, volleyball, judo and athletics 3 each; handball and cycling 2 each; archery 1; basketball, hockey and darts 1 each (studies). No sport is above a third.
   - The deliverable is football because the brief requires it to be built for Milan.
   - On reading, nothing names or points to the Project's owner. `kit/private_terms.py` is outside the folder and was not run.

## Part 7, brief, length, case
- **Part 7:** every line passes apart from the findings above. The search flag is off and no rule or date is stated as fact.
- **Brief and deliverable:** met in full.
- **Length:** about 7,060 words before the deliverable (excluding the figure JSON), about 5,720 in the deliverable and about 670 in Sources, so the report runs over the brief's 6,000. The overrun is substance, not padding. It is driven by the brief's ~20 topics, the per-technique sample reporting and the reasoning for the F6, F68 and F83 regrades. Optional trims: the §15 table and matrix carry the same grades twice; §20 recaps the course's tools; one line in §1 lists the sports drawn on.
- **Case facts:** the 11 listed facts agree with the register. Two facts are invented but unlisted (findings 3 and 13). Milan's "cap level 3" is attributed to SP6 and SP10 and is not in the register; I could not verify it here.
- **Read as the coach:** usable on a phone, the citations open, and the grades are honest. §2's rule-number reasoning assumes SP1 is at hand, which is acceptable for a course read in order.

Verdict: DD-SP3 · fix · error 0, should-fix 3, minor 10
