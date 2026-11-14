# Fable stage: cost assessment after row F-PB (November 2026)

Built by `audits/personal-brand/f-pb/tools/assess.py` from each auditor's completion notice (`f-pb/usage.json`) and its report files (`f-pb/<code>/stats.json`, `claims.json`). **PARTIAL: 8 of 12 unit audits are in; pending: PB9, PB10, DD-PB1, DD-PB2.**

**Meter readings.** At start: All models __% · Fable only __% (the prompt's first line arrived unfilled; Pedro had not entered the readings). After: to be read by Pedro from Settings > Usage and set against the token totals below.

**Model.** Every auditor stated `claude-fable-5-2` (Fable 5.2, accepted by Pedro for this row on 14 Nov 2026). The chat that staged, saved, applied and recorded also ran as claude-fable-5-2; its own tokens are **not measured** here (no completion notice exists for the chat itself), and it carried each returned report in its context, so its share is not small.

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

## 2 · Totals

| | Units | Words | Sampled | Checked | FAIL | STALE | Unverifiable | Tokens | Tool uses | Agent minutes | Tokens per claim checked | Tokens per 1,000 words |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Audit 1 | 4 | 39,037 | 45 | 159 | 6 | 0 | 3 | 888,822 | 289 | 35.5 | 5,590 | 22,768 |
| Audit 2 | 4 | 48,013 | 59 | 154 | 10 | 0 | 3 | 1,010,384 | 308 | 42.6 | 6,560 | 21,043 |
| Audit 3 | 0 | | | | | | | | | | | |
| Unit audits, complete runs | 8 | 87,050 | 104 | 313 | 16 | 0 | 6 | 1,899,206 | 597 | 78.1 | 6,067 | 21,817 |
| PB9 (run 1, no web search) | | | | | | | | 188,781 | 22 | 5.71 | | |
| DD-PB1 (run 1, no web search) | | | | | | | | 183,932 | 24 | 6.5 | | |
| DD-PB2 (run 1, no web search) | | | | | | | | 179,836 | 24 | 5.89 | | |
| **Row, all agents measured** | | | | | | | | **2,451,755** | | | | |

The chat's own share is unmeasured. Runs marked "no web search" spent their tokens reading and checking inside the folder only: the turn's web search budget (200 WebSearch calls per turn, shared by every agent) was used up by the first eight auditors, which is itself a finding for the planning of stage 5 (section 5).

## 3 · Projections

Rates from the 8 complete runs: 237,401 tokens per unit (range 179,631 to 275,867); 21,817 tokens per 1,000 words (range 18,200 to 26,874); 6,068 tokens per claim checked; 25 web searches per unit. Tokens varied little with length (the largest unit cost 1.54 times the smallest for 1.76 times the words), so each projection gives a flat per-unit figure and a per-word figure; the truth should lie between them.

**(a) Sample audits still owed.**

| Set | Units | Words | Sections | Tokens at the per-unit rate | Tokens at the per-word rate | Searches at the per-unit rate |
|---|---|---|---|---|---|---|
| Course B, seven unaudited (B5, B6, B7, B8, DD-B1, DD-B2, DD-B3) | 7 | 62,217 | 66 | 1,661,805 | 1,357,414 | 175 |
| Course A, seven unaudited (A3, A4, A5, A7, A8, DD-A1, DD-A2) | 7 | 61,890 | 67 | 1,661,805 | 1,350,280 | 175 |
| User Experience, fifteen | 15 | 228,802 | 176 | 3,561,011 | 4,991,868 | 375 |
| Rome, twenty flagged modules (11.3 to 11.8, 12.1 to 12.8, 13.3 to 13.8) | 20 | 110,737 | 218 | 4,748,015 | 2,415,995 | 500 |

Caveats: the private courses' units are of different lengths and source types than PB's; Rome's modules cite ancient texts and scholarship, where a claim is checked against a book or a passage, not a web page, and their full audit is the kit's scorecard, not this procedure, so the Rome line is the least reliable. Each set also needs its chat (staging, saving, applying, records), unmeasured here.

**(b) A full Fable fresh check of PB's twelve units.** The reports counted 1,359 cited claims in 11 of the 12 units (PB1 148, PB2 65, PB3 109, PB4 111, PB5 139, PB6 144, PB7 126, PB8 169, PB9 94, DD-PB1 167, DD-PB2 87). Upper estimate, at the average of 6,068 tokens per claim checked: about 8,246,073 tokens for those units. That average carries each agent's fixed cost of reading the unit, its packet and the other eleven units' pointers, so it overstates.

A closer estimate separates the two costs. The 3 runs that had no web search still cost 179,836 to 188,781 tokens each (mean 184,183): that is the cost of reading and of the internal checks (arithmetic, pointers, the register, figures, the deliverable). The complete runs averaged 237,401 tokens for 39 claims checked, so opening sources cost about 1,360 tokens per claim on top. On that split a full check of the 11 counted units is about 3,874,522 tokens (184,183 + 1,360 × its cited claims, per unit), roughly 1.5 times their sample audits. The no-search runs did more internal checking than a searching run would, so the fixed part is somewhat overstated and the per-claim part understated; the true figure lies between the two estimates, nearer the lower.

Searches are the binding limit, not tokens: at the sample's 0.64 searches per claim checked, a full check of 1,359 claims needs about 868 web searches, against a budget of 200 per turn shared by every agent in it.

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

| Search flag | Checked | FAIL | per 100 | STALE | Unverifiable |
|---|---|---|---|---|---|
| off | 104 | 4 | 3.8 | 0 | 3 |
| on | 209 | 12 | 5.7 | 0 | 3 |

| Claim kind | Checked | FAIL | per 100 | STALE | Unverifiable |
|---|---|---|---|---|---|
| attribution | 51 | 10 | 19.6 | 0 | 1 |
| date | 15 | 1 | 6.7 | 0 | 0 |
| mechanism | 18 | 1 | 5.6 | 0 | 1 |
| number | 122 | 1 | 0.8 | 0 | 2 |
| quotation | 107 | 3 | 2.8 | 0 | 2 |

| Sampled or also checked | Checked | FAIL | per 100 | STALE | Unverifiable |
|---|---|---|---|---|---|
| also checked | 209 | 13 | 6.2 | 0 | 5 |
| sampled | 104 | 3 | 2.9 | 0 | 1 |

## 5 · Reading and recommendation

To be written when the reports are in.

