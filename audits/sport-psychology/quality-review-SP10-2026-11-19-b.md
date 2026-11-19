---
code: SP10
kind: quality-review (rule 13)
model: claude-opus-5-5
date: 2026-11-19
chat: https://claude.ai/code/session_01KMmgR35wf5wmG58AbjrCFw
note: report returned as the agent reply (harness blocked its file write) and saved verbatim by the chat
---

# Quality review: SP10 · The season plan

Model: claude-opus-5-5. Date: 19 Nov 2026. Fresh agent with live search, working only from the packet. SP1 to SP9 are not in the packet, so no claim the unit sources to them could be opened (see Could not verify).

References opened (19 Nov 2026; every URL was returned by a search in this agent):
- Pluhar et al. (2019): full text and abstract at jssm.org (https://www.jssm.org/jssm-18-490.xml-Fulltext; https://jssm.org/jssm-18-490.xml-abst).
- Rodrigues et al. (2023): full text at SciELO (https://www.scielo.br/j/rbme/a/GVN6pKgvZdLb9h5FhQBYVZc/?lang=en).
- Hertting et al. (2020): full text at MDPI (https://www.mdpi.com/2075-4663/8/11/146/htm).
- Ferreira et al. (2024): full text at Frontiers (https://public-pages-files-2025.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2024.1301978/text; https://frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2024.1301978/pdf, Table 2).
- Mitchell et al. (2021): abstract and record at the publisher (https://scholarworks.bgsu.edu/jade/vol3/iss3/4).
- Silva et al. (2016): full text at SciELO (https://scielo.br/j/motriz/a/D6z9stkYzRMqgDd7jpGPqwF/?lang=en); abstract at BVS (https://search.bvsalud.org/portal/resource/en/lil-776621); authors and DOI from a DOAJ-derived record (https://oalib-perpustakaan.upi.edu/Record/doaj_b0cdfc7fd15b4d719fb943c5e91e9fb1/Description).

Not opened:
- Park et al. (2013) and Neely et al. (2016): searches returned only repository or index pages.
- PubMed record for Pluhar: the page came back empty.
- Frontiers /text address for Ferreira: it redirected, so it was not retried. The target and the PDF, both returned by the search, were fetched instead.
- SP1 to SP9.

## 1. Claims
PASS. Every claim resting on the six new references holds at the publisher's page. Claims sourced to SP1 to SP9 are listed under Could not verify.

## 2. Bibliography
PASS. All six entries match the publisher's record field by field. Pluhar shows no DOI on the publisher's page, as the entry says.

## 3. Source log
FIX. The Silva entry and its in-text hedge say the full text was not confirmed. The publisher's page holds the full text and confirms every detail the unit gives.

## 4. Grades
FIX. One label breaks the unit's own convention for evidence from younger athletes applied to older ones (section 7). Three recommendations carry no grade (sections 2 and 9).

## 5. Population
PASS. The new studies carry their sample and design, and transfers to under-18s are labelled. Two findings relayed from SP2 (relative age; the junior-to-senior meta-analysis) give no sample here; both are under Could not verify.

## 6. Scope and safety
PASS.
- Nothing teaches assessment, diagnosis or treatment.
- No weight method, calorie figure, target weight or self-harm method appears.
- Data protection and the regulators are put as questions, each with a body to ask.
- No real person is named.
- The information-not-advice line is present.

## 7. Any sport
PASS, borderline. Each sport was counted once per section and once per deliverable part:

| Sport | Examples |
|---|---|
| Football | 6 of 21 (29%) |
| Judo | 4 |
| Athletics | 3 |
| Swimming | 2 |
| Volleyball | 2 |
| Gymnastics | 2 |
| Rowing | 1 |
| Cycling | 1 |

It is borderline because the deliverable is built on one football squad; F156 records this for the syllabus review. Nothing identifying the owner was seen, but private_terms.py was not run because it is not in the packet.

## Brief, deliverable, flags, Part 7, the coach's reading
- **Cover items:** all ten met.
- **Deliverable:** met in full. A1 and A2 are the formulations. B is the season plan for Milan's squad, by week, skill, slot, competition, parents and review point. C is the weekly review, built on the case. D gives the templates in start order: formulation, season plan, transition sheet (built on Milan) and weekly review.
- **Length:** sections 1 to 10 run to about 7,200 words before the deliverable, over the brief's 2,000 to 6,000. The brief says not to cut to a target, so this is noted, not a finding.
- **Arithmetic:** correct.
  - Own minutes: 110 pre-season (10+40+5+15+20+15+5), 80 in a block and 80 between blocks.
  - The compare figure sums to 80.
  - Session time: 20 of 360 is 5.6% and 40 of 360 is 11.1%.
- **Plan against section 4's rules:** consistent.
  - Thursday runs one level down before a Saturday match, and there is no Friday session.
  - Wednesday, the hardest session, carries no slot.
  - Players climb one level a week at most.
  - The level-6 rehearsal is on Tuesday of week 24, which is not the last session before a match.
  - Weeks 35 to 38 are treated as heavy weeks.
- **Flags naming SP10:**
  - Dealt with in the unit: F8, F14, F26, F37, F67, F70, F85, F118, F124, F137, F139, F153, F154, F155, F168, F171, F175.
  - Not met, and the unit says so: F20, F21/F117, F108, F130, F131.
  - Partly met, and the unit says so: F132, F142.
  - F47 and F48 are carried, with one lapse (finding 1).
  - F163: Ferreira's Table 2 gives no coach level for any study, so the unit's sentence holds.
- **Part 7:** met line by line except the grade line (findings 1, 6, 7, 8) and the source-log line (findings 2, 3).
- **As the coach would read it:** usable, but dense on a phone. The Silva hedge is the hardest passage, and findings 2 and 3 remove it.

## Findings
[should-fix] [label] Section 7; Current: "coaches of players aged 10 to 15, so for 16 to 25 an inference"; Problem: the preamble keeps *inference* for adults, students or non-athletes applied to under-18s, and marks evidence from younger athletes applied to an older band as "outside the sampled ages" (F48 open); Fix: "coaches of players aged 10 to 15, so for 16 to 25 outside the sampled ages"; Basis: the unit's preamble (line 12); syllabus-flags.md F48
[minor] [attribution] Section 9; Current: "Further details rest only on the writer's reading of the publisher's page through the fetch tool's extraction, and the abstract records seen by later checks give none of them:"; Problem: the SciELO page holds the full text, and its Methods and Results confirm every listed detail: 127 PE students with a mean age of 21.6; 90 athletes (soccer 43, swimming 34, indoor soccer 13) whose ages are not reported; a 14-day retest; athletes scoring higher (41.95 against 28.78). The link label "read through the fetch tool's extraction of the publisher's page" in the same bullet should become "full text read at the publisher's page"; Fix: "The full text at the publisher's page adds:"; Basis: Silva et al. (2016), https://scielo.br/j/motriz/a/D6z9stkYzRMqgDd7jpGPqwF/?lang=en
[minor] [attribution] Sources; Current: "(read through the fetch tool's extraction of the publisher's page, https://scielo.br/j/motriz/a/D6z9stkYzRMqgDd7jpGPqwF/?lang=en; the abstract records seen by later checks do not confirm that the page held the full text)"; Problem: the page holds the full text; Fix: "(full text read at the publisher's page, https://scielo.br/j/motriz/a/D6z9stkYzRMqgDd7jpGPqwF/?lang=en; confirmed by the quality review, 19 Nov 2026)"; Basis: as above
[minor] [accuracy] Section 4; Current: "**Club academy players aged 18 to 20.**"; Problem: the paper describes U-20 male soccer athletes at three clubs; "academy" is not its term; Fix: "**Club under-20 players aged 18 to 20.**"; Basis: Rodrigues et al. (2023), https://www.scielo.br/j/rbme/a/GVN6pKgvZdLb9h5FhQBYVZc/?lang=en
[minor] [figure] Section 4 matrix; Current: "{"label": "Development note (SP2)", "cells": [{"mark": "write", "tone": 2}, null, null, {"mark": "rewrite", "tone": 3}]}"; Problem: the caption says a blank cell means nothing is placed in that phase, but the unit rewrites the note before a known transition in the competitive season (section 1 table; B, week 34); Fix: "{"label": "Development note (SP2)", "cells": [{"mark": "write", "tone": 2}, {"mark": "rewrite", "tone": 3}, null, {"mark": "rewrite", "tone": 3}]}"; Basis: the unit, section 1 and Deliverable B
[minor] [label] Section 2; Current: "**When.** Write it once the baseline is built"; Problem: a recommendation with no grade; Fix: "**When** [practice; the earlier units' review dates]. Write it once the baseline is built"; Basis: brief; sourcing-standard.md Part 7
[minor] [label] Section 9; Current: "Do not run it on your squad."; Problem: a recommendation with no grade; Fix: "Do not run it on your squad [practice; the unit's own reading of the two studies]."; Basis: brief; Part 7
[minor] [label] Section 9; Current: "The plan puts each selection date in the calendar"; Problem: a recommendation with no grade (SP3's grade covers SP3's steps, not this placing); Fix: "The plan [practice; the unit's own] puts each selection date in the calendar"; Basis: brief; Part 7
[minor] [coverage] Notes, Added facts; Current: "the squad's weekly match (at the weekend, SP5) is on Saturday."; Problem: the register lists two SP10 facts about Dani (her enjoyment not yet asked; the look after each exchange not yet asked) that the unit's added-facts line omits. A1 also says, with no register entry, that what she wants from her coach after a loss has not been asked; the same applies to "Not yet asked (SP7's script 1)" unless SP7 records it; Fix: "the squad's weekly match (at the weekend, SP5) is on Saturday; nobody has yet asked Dani what she enjoys in training and what she would change, what her look to her coach after each exchange is about, or what she wants from her coach after a loss."; Basis: case-facts.md SP10 rows; Deliverable A1

Could not verify (all sourced to units not in the packet):
- "teaching psychological skills inside training is [moderate, positive; samples mostly adult where ages are reported, so for athletes under 18 an inference] (SP5, section 2)"
- "training under pressure is [moderate, positive; inference for under-18s] (SP6, section 2)"
- "a pre-performance routine is [moderate, positive; ages 11 to 40] (SP6, section 5)"
- "there was some evidence that effects were greatest when coaches delivered the intervention [weak, positive] (SP5, section 2)"
- "the band cap (3 at 10 to 12, 4 at 13 to 15, 6 from 16), 3 while a referral is under way, 1 for four weeks when new to the squad (SP6, section 9)"
- "imagery effects larger after 100 days than after 20, and an eight-week self-talk programme that changed coach-rated performance where a one-week programme did not (SP5, section 4)"
- "its practitioner source warns that pressure once a month is too rare to develop coping"
- "SP9 found figures only for elite adults and for elite youth athletes of mean age 12 to 17 who compete internationally"
- "[moderate, positive, for the association between early multi-sport practice and later world-class performance] (SP2, section 9)"
- "SP2's table holds back more than 8 months a year in one sport, the NSCA statement's limit"
- "SP3's review of parent-education programmes found 12 studies of mixed design and quality"
- "one qualitative study of 12- to 15-year-old girls in team sports"
- "a sport-science route whose graduates teach mental skills and usually do not become licensed psychologists"
- "treating athletes for mental illness is ethically beyond many sport psychology practitioners' professional competencies (SP5, section 1)"
- "in a meta-analysis of young athletes aged 5 to 19, it was the strongest correlate of intending to continue in sport"
- "the gain in observed autonomy support faded within the season"
- "[moderate, positive, for the maturity–performance association in boys"
- "SP2 reported a meta-analysis in which the relative age effect grew with the gap in relative age" (no sample given)
- "In the meta-analysis SP2 opened, higher-performing juniors had entered talent programmes younger, and higher-performing seniors had entered them older [strong, for the association; correlational]" (no sample given)
- "The ISSP stand describes this transition as lasting months to years (SP2, section 7)."
- "physical and psychological readiness to return do not necessarily coincide (SP9, sections 2 and 9)"
- "The ISSP stand, as SP2 read it, reports a review of 126 studies finding that adjustment to the end of a career depends on athletic identity, education and finances"
- "as SP3's review of dropout from swimming reported from six studies of mixed design, in swimmers aged 5 to 30 (SP3, section 7)"
- "counted shouting or belittling 7 times, most attention to the strongest judoka 6 times, and asking an athlete's view 0 times"
- "His coach's training audit scored well; the three changes are no public comparisons, no selection threats, expectations set at the start" (the register gives Milan's column one selection threat and two public comparisons)
- "Duration and cost are outside the ordinary range: referral offered."
- "(SP8, Deliverables A, B and D)"

Confirmed:
- **Pluhar et al. (2019):** 756 athletes aged 18 or under (6 to 18 in the abstract), mean 13.5, at one injury prevention centre. 8% reported clinician-diagnosed anxiety or depression, self-reported in one question. The rate was 13% in athletes who played only individual sports and 7% in team-sport athletes, and the difference was not significant after adjustment. The sample was not random, answers were not checked against records, and no DOI is shown. https://www.jssm.org/jssm-18-490.xml-Fulltext
- **Rodrigues et al. (2023):** 62 male U-20 players aged 18 to 20 at three clubs in Recife, cross-sectional, measured on HADS. 9 (14.5%) scored above the cut-off for anxiety and 4 (6.5%) for depression. The Discussion's 14.3% does not match these figures, as the unit's unsure list says. https://www.scielo.br/j/rbme/a/GVN6pKgvZdLb9h5FhQBYVZc/?lang=en
- **Hertting et al. (2020):** 688 unpaid coaches, 70% of them coaching ages 10 to 15. Stress was measured on a two-item index the authors say is not validated, with a mean of 2.20 of 5. The predictors match the unit. One survey. https://www.mdpi.com/2075-4663/8/11/146/htm
- **Ferreira et al. (2024):** 11 studies (5 questionnaire, 6 interview) from 8 countries, with no pooling. The findings on support, burnout, stress and satisfaction match the unit, and no coach level is reported. https://frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2024.1301978/pdf
- **Mitchell et al. (2021):** 259 male academy players aged 12 to 18. Both models were supported, "not within the same analysis". https://scholarworks.bgsu.edu/jade/vol3/iss3/4
- **Silva et al. (2016):** every detail in the unit holds (see finding 2). https://scielo.br/j/motriz/a/D6z9stkYzRMqgDd7jpGPqwF/?lang=en
- **Bibliography:** all six entries match field by field.
- **Park and Neely:** this review's searches also returned no publisher's page or DOI address, and no claim rests on either.
- **Section 10 arithmetic:** correct.
- **Case facts:** those in A1, A2 and B agree with case-facts.md, including every SP10 row.

Verdict: QR-SP10 · fix · 0 error, 1 should-fix, 8 minor
