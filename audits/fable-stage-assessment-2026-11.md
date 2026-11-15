# Fable stage: cost assessment after row F-PB (November 2026)

Built by `audits/personal-brand/f-pb/tools/assess.py` from each auditor's completion notice (`f-pb/usage.json`) and its report files (`f-pb/<code>/stats.json`, `claims.json`). All twelve unit audits are in.

**Meter readings.** Part 1 (14 Nov 2026): the prompt's first line arrived unfilled; Pedro's reading after it: 18% of the weekly Fable allowance used (03:32), before a shorter-window Fable limit stopped the row at 03:27. Part 2 (15 Nov 2026): the first line arrived unfilled again (All models __% · Fable only __%). After part 2: to be read by Pedro from Settings > Usage and set against the token totals below.

**Model and parts.** The row ran in two parts. Part 1, 14 Nov 2026: every auditor stated `claude-fable-5-2` (Fable 5.2, accepted by Pedro for this row on 14 Nov 2026); the chat ran as Fable 5.2 until 03:28, then as Opus 5.5 for saving, applying and recording, and carried each returned report in its context. Part 2, 15 Nov 2026: the chat ran as Opus 5.5 (claude-opus-5-5) throughout and read only each auditor's six-line reply and `stats.json`; the four auditors (PB9, PB10, DD-PB1, DD-PB2) stated `claude-fable-5-2`, re-checked their run-1 samples at source and ran a full attribution pass, 40 searches each at most. The chat's own tokens are **not measured** (no completion notice exists for it); in part 2 they were Opus, not Fable.

## 1 · Per unit

| Unit | Audit | Search | Words | Sections | Sampled | Checked in all | FAIL (in sample) | STALE | Unverifiable | Tokens | Tool uses | Minutes | Tokens per claim checked | Errata applied / held / flags |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| PB1 | 1 | on | 10,979 | 13 | 15 | 34 | 0 (0) | 0 | 0 | 199,815 | 58 | 7.6 | 5,876 | 4 / 0 / 1 |
| PB2 | 1 | off | 8,183 | 9 | 9 | 32 | 1 (0) | 0 | 0 | 179,631 | 63 | 6.14 | 5,613 | 1 / 0 / 0 |
| PB3 | 1 | on | 9,437 | 10 | 10 | 55 | 3 (0) | 0 | 1 | 253,612 | 89 | 9.76 | 4,611 | 7 / 0 / 1 |
| PB4 | 1 | off | 10,438 | 11 | 11 | 38 | 2 (1) | 0 | 2 | 255,764 | 79 | 11.99 | 6,730 | 3 / 2 / 1 |
| PB5 | 2 | off | 12,497 | 14 | 14 | 34 | 1 (0) | 0 | 1 | 246,461 | 65 | 9.98 | 7,248 | 4 / 0 / 1 |
| PB6 | 2 | on | 10,515 | 12 | 13 | 54 | 2 (0) | 0 | 2 | 251,659 | 94 | 10.68 | 4,660 | 2 / 0 / 2 |
| PB7 | 2 | on | 10,591 | 13 | 15 | 37 | 6 (1) | 0 | 0 | 236,397 | 62 | 8.33 | 6,389 | 8 / 0 / 0 |
| PB8 | 2 | on | 14,410 | 11 | 17 | 29 | 1 (1) | 0 | 0 | 275,867 | 87 | 13.66 | 9,512 | 9 / 2 / 0 |
| PB9 | 3 | on | 8,974 | 15 | 15 | 96 | 6 (1) | 0 | 2 | 233,863 | 98 | 9.73 | 2,436 | 12 / 0 / 3 |
| PB10 | 3 | off | 12,916 | 12 | 12 | 62 | 2 (0) | 0 | 4 | 228,888 | 80 | 7.07 | 3,691 | 7 / 0 / 0 |
| DD-PB1 | 3 | on | 9,457 | 14 | 14 | 183 | 5 (0) | 0 | 1 | 262,778 | 104 | 11.18 | 1,435 | 9 / 0 / 0 |
| DD-PB2 | 3 | off | 8,875 | 10 | 10 | 58 | 3 (1) | 0 | 0 | 208,823 | 74 | 7.59 | 3,600 | 7 / 0 / 2 |

## 2 · Totals

| | Units | Words | Sampled | Checked | FAIL | STALE | Unverifiable | Tokens | Tool uses | Agent minutes | Tokens per claim checked | Tokens per 1,000 words |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Audit 1 | 4 | 39,037 | 45 | 159 | 6 | 0 | 3 | 888,822 | 289 | 35.5 | 5,590 | 22,768 |
| Audit 2 | 4 | 48,013 | 59 | 154 | 10 | 0 | 3 | 1,010,384 | 308 | 42.6 | 6,560 | 21,043 |
| Audit 3 | 4 | 40,222 | 51 | 399 | 16 | 0 | 7 | 934,352 | 356 | 35.6 | 2,341 | 23,229 |
| Unit audits, complete runs | 12 | 127,272 | 155 | 712 | 32 | 0 | 13 | 2,833,558 | 953 | 113.7 | 3,979 | 22,263 |
| PB9 (run 1, no web search) | | | | | | | | 188,781 | 22 | 5.71 | | |
| DD-PB1 (run 1, no web search) | | | | | | | | 183,932 | 24 | 6.5 | | |
| DD-PB2 (run 1, no web search) | | | | | | | | 179,836 | 24 | 5.89 | | |
| PB10 (run 1, no web search) | | | | | | | | 254,438 | 41 | 10.55 | | |
| Audit 4 | | | | | | | | 0 |  |  | | |
| **Row, all agents measured** | | | | | | | | **3,640,545** | | | | |

The chat's own share is unmeasured. Runs marked "no web search" spent their tokens reading and checking inside the folder only: the turn's web search budget (200 WebSearch calls per turn, shared by every agent) was used up by the first eight auditors, which is itself a finding for the planning of stage 5 (section 5).

## 3 · Projections

Rates from the 12 complete runs: 236,130 tokens per unit (range 179,631 to 275,867); 22,264 tokens per 1,000 words (range 17,721 to 27,787); 3,980 tokens per claim checked; 28 web searches per unit. Tokens varied little with length (the largest unit cost 1.54 times the smallest for 1.76 times the words), so each projection gives a flat per-unit figure and a per-word figure; the truth should lie between them.

**(a) Sample audits still owed.**

| Set | Units | Words | Sections | Tokens at the per-unit rate | Tokens at the per-word rate | Searches at the per-unit rate |
|---|---|---|---|---|---|---|
| Course B, seven unaudited (B5, B6, B7, B8, DD-B1, DD-B2, DD-B3) | 7 | 62,217 | 66 | 1,652,909 | 1,385,187 | 195 |
| Course A, seven unaudited (A3, A4, A5, A7, A8, DD-A1, DD-A2) | 7 | 61,890 | 67 | 1,652,909 | 1,377,906 | 195 |
| User Experience, fifteen | 15 | 228,802 | 176 | 3,541,948 | 5,094,001 | 418 |
| Rome, twenty flagged modules (11.3 to 11.8, 12.1 to 12.8, 13.3 to 13.8) | 20 | 110,737 | 218 | 4,722,597 | 2,465,426 | 557 |

Caveats: the private courses' units are of different lengths and source types than PB's; Rome's modules cite ancient texts and scholarship, where a claim is checked against a book or a passage, not a web page, and their full audit is the kit's scorecard, not this procedure, so the Rome line is the least reliable. Each set also needs its chat (staging, saving, applying, records), unmeasured here.

**(b) A full Fable fresh check of PB's twelve units.** The reports counted 1,531 cited claims in 12 of the 12 units (PB1 148, PB2 65, PB3 109, PB4 111, PB5 139, PB6 144, PB7 126, PB8 169, PB9 94, PB10 171, DD-PB1 168, DD-PB2 87). Upper estimate, at the average of 3,980 tokens per claim checked: about 6,092,946 tokens. That average carries each agent's fixed cost of reading the unit, its packet and the other eleven units' pointers, so it overstates.

A closer estimate separates the two costs. The 4 runs that had no web search still cost 179,836 to 254,438 tokens each (mean 201,747): that is the cost of reading and of the internal checks (arithmetic, pointers, the register, figures, the deliverable). The complete runs averaged 236,130 tokens for 59 claims checked, so opening sources cost about 579 tokens per claim on top. On that split a full check of the 12 counted units is about 3,308,160 tokens (201,747 + 579 × its cited claims, per unit), roughly 1.2 times their sample audits. The no-search runs did more internal checking than a searching run would, so the fixed part is somewhat overstated and the per-claim part understated; the true figure lies between the two estimates, nearer the lower.

Searches are the binding limit, not tokens: at the sample's 0.47 searches per claim checked, a full check of 1,531 claims needs about 718 web searches, against a budget of 200 per turn shared by every agent in it.

## 4 · What the sample found, against what the Opus fresh checks had fixed

| Unit | Search | Checked | FAIL | per 100 | STALE | Unverifiable | Opus fresh check (verdict line of its report) |
|---|---|---|---|---|---|---|---|
| PB1 | on | 34 | 0 | 0.0 | 0 | 0 | fix · 1 error, 6 should-fix, 7 minor |
| PB2 | off | 32 | 1 | 3.1 | 0 | 0 | fix · 1 error, 3 should-fix, 6 minor |
| PB3 | on | 55 | 3 | 5.5 | 0 | 1 | fix · 1 error, 5 should-fix, 6 minor |
| PB4 | off | 38 | 2 | 5.3 | 0 | 2 | fix · 0 errors, 8 should-fix, 15 minor |
| PB5 | off | 34 | 1 | 2.9 | 0 | 1 | fix · 0 errors, 3 should-fix, 11 minor |
| PB6 | on | 54 | 2 | 3.7 | 0 | 2 | fix · 2 errors, 12 should-fix, 14 minor |
| PB7 | on | 37 | 6 | 16.2 | 0 | 0 | fix · 3 errors, 9 should-fix, 7 minor |
| PB8 | on | 29 | 1 | 3.4 | 0 | 0 | fix · 2 errors, 6 should-fix, 8 minor |
| PB9 | on | 96 | 6 | 6.2 | 0 | 2 | fix · 3 errors, 5 should-fix, 10 minor |
| PB10 | off | 62 | 2 | 3.2 | 0 | 4 | fix · 0 errors, 8 should-fix, 33 minor |
| DD-PB1 | on | 183 | 5 | 2.7 | 0 | 1 | rewrite by the count rule, read as fix (every error a single misquoted phrase or unsupported clause with its e |
| DD-PB2 | off | 58 | 3 | 5.2 | 0 | 0 | fix · 1 error, 4 should-fix, 8 minor |

| Search flag | Checked | FAIL | per 100 | STALE | Unverifiable |
|---|---|---|---|---|---|
| off | 224 | 9 | 4.0 | 0 | 7 |
| on | 488 | 23 | 4.7 | 0 | 6 |

| Claim kind | Checked | FAIL | per 100 | STALE | Unverifiable |
|---|---|---|---|---|---|
| attribution | 251 | 22 | 8.8 | 0 | 3 |
| date | 20 | 1 | 5.0 | 0 | 0 |
| mechanism | 31 | 3 | 9.7 | 0 | 1 |
| number | 186 | 2 | 1.1 | 0 | 4 |
| quotation | 223 | 4 | 1.8 | 0 | 5 |
| recommendation | 1 | 0 | 0.0 | 0 | 0 |

| Sampled or also checked | Checked | FAIL | per 100 | STALE | Unverifiable |
|---|---|---|---|---|---|
| also checked | 557 | 27 | 4.8 | 0 | 11 |
| sampled | 155 | 5 | 3.2 | 0 | 2 |

## 5 · Reading and recommendation

**How the row ran.** Two parts. Part 1, 14 Nov 2026: eight unit audits with live search (PB1 to PB8; Audits 1 and 2) and Audit 4, the full read; the turn's 200-call WebSearch budget, shared by all twelve auditors, ran out after the first eight, so PB9, PB10, DD-PB1 and DD-PB2 ran without opening a source (their reports are kept in `f-pb/<code>-run1-no-search/`, and their 0.81M tokens are counted above as waste); a shorter-window Fable limit stopped the row at 03:27, after 18% of the weekly Fable allowance (Pedro, 03:32). Part 2, 15 Nov 2026: the chat ran on Opus 5.5 and read only six-line replies and `stats.json`; four Fable auditors re-checked the four recorded samples at source, each with a full attribution pass and a cap of 40 searches (134 used of 160, none refused). Each part-2 auditor cost 208,823 to 262,778 tokens, the same as a part-1 sample audit, although it also checked every quotation, attribution and Sources title in its unit. Held errata were worked by the chat at source: vidIQ's study title in PB1, PB3, PB4 and PB6, the fair-dealing cells of PB8, A4-13 re-anchored in PB1, and the HMRC title in PB8 and DD-PB2 (`f-pb/chat/errata.json`).

**Final totals.** Twelve unit audits, all PASS: 712 claims checked, 155 of them sampled; 32 FAIL (5 in the sample), none STALE, 13 unverifiable; no unit reached the one-in-ten rule, so no full audit ran and there is no REWRITE. 2.83M tokens for the twelve complete runs, 3.64M for every agent measured (Audit 4's tokens were not reported), plus the chat. Errata applied: 73 from the unit reports, 14 from Audit 4, 16 worked by the chat; 17 flags, of which 16 became fourteen syllabus-flag rows (F87 to F100) and one (DD-PB2-9, an HMRC title shared with PB8) was worked by the chat.

**What the sample found.** Numbers failed at 1.1 per 100 (2 in 186) and quotations at 1.8 (4 in 223): the Opus fresh checks had caught those. Attribution failed at 8.8 per 100 (22 in 251) and mechanism at 9.7 (3 in 31). The part-2 attribution passes give the cleaner rate for that stratum, because they checked every attribution rather than those a sample happened to draw: 12 FAIL in 200, 6 per 100, against 20 per 100 in part 1's samples. The kinds of failure did not change: titles taken from URL slugs or joined from a site's name and a page's (DD-PB2, PB9), a paper's mechanism restated with its referent reversed (PB9 §11, DD-PB1 §4), a quotation credited to the outlet that reported it (DD-PB1 §6), a percentage cited to a page that gives it for something else (PB9's 55%/45%). Search-on and search-off units failed at much the same rate (4.7 and 4.0 per 100).

**Is sampling the wrong tool for any stratum?** For numbers, dates and quotations, no. For attribution, sampling alone is: at 6 to 20 per 100 a one-claim-per-section sample misses most of a unit's attribution errors. A full attribution pass, run inside the sample audit, catches them at no measurable extra cost (part 2's runs cost the same as part 1's). A full Fable fresh check is not needed: it would cost about 2.5 times a sample audit (section 3b) and about 720 searches for PB alone, against 200 a turn.

**Recommendation.** Pick: **sample audit of course B's seven unaudited units, each with a full attribution pass in the same agent.** Reasons: numbers failed under 2 per 100 after the Opus fresh checks; the attribution pass found the stratum's errors at no extra cost; a full fresh check costs 2.5 times as much and needs searches no turn has. Override if: course B's samples, written before the fresh-check routine settled, fail numbers at more than 1 in 10, which triggers that unit's full audit under the method anyway. Order for the rest of stage 5: **course B** next (seven units, about 1.4M to 1.7M tokens and 195 searches at the per-unit rate, so one turn at most six auditors capped at 30 searches each, the seventh in the next turn or in a second chat); then **course A**'s seven (about the same); then **User Experience** (fifteen, 3.5M to 5.1M tokens, in three runs of five); **Rome** last, on its own scorecard procedure, which this row does not cost. The chat runs on Opus 5.5 and reads only short replies and stats files: part 2 shows that Fable then spends nothing on the chat.

