Model: claude-fable-5-2

# PB10 · Stratified-sample audit (course PB, Audit 3) · 14 November 2026 · search on

## Provenance

- Auditor: one fresh, isolated agent, model claude-fable-5-2. Read only `/home/claude/fpb/PB10`; wrote only `out/`. No memory, past-chat, Projects, connector, Artifact, Agent or `mcp__` tool used.
- Unit: `unit.md` (PB10 · Read your numbers: the quarterly review; written 2026-11-13 by Opus 5.5; search flag off). Not edited.
- `out/` was empty at the start: this is a first run, not a resumed one.
- The earlier fresh check (`fresh-check-PB10.md`) was read only to avoid re-reporting fixed findings; none of its verdicts is reused.

## Sample (recorded before any check)

Twelve `##` sections. One claim drawn from each section that carries a checkable claim; the Deliverable gives two (one from Mara's run, one from the annual page). The Unsure list carries no cited claim and gives none.

| n | Section | Sampled claim | Source the unit cites |
|---|---|---|---|
| 1 | §1 | A 30-day view count needs an upload at least 30 days old (PB6 D2 YT2); click-through and percentage viewed need 7 days (YT3, YT4); an Instagram post is read once it is 7 days old (PB7 D2) | PB6 D2, PB7 D2 (`others/`) |
| 2 | §2 | YouTube counts qualified watch hours only from "long-form videos that you've set to public", not from private, unlisted or deleted videos or Shorts | YouTube Help 72851 |
| 3 | §3 | NIST's sample-size formula gives about 2,045 impressions to tell a true 2% from a hypothesised 3% (5% two-sided, 80% power), about 1,747 with 2% as the hypothesis; the continuity correction adds 100 | NIST/SEMATECH §7.2.4.2 |
| 4 | §4 | Buffer's I4 estimate (+0.26% weekly follower growth at 3–5 posts) is the difference from weeks with no posts: "points added to the weekly growth rate" | PB1 D1 I4, PB1 §3 (`others/`); Buffer behind it |
| 5 | §5 | Meta's developer reference: follower demographics are "Not returned if the IG User has less than 100 followers", and follows and unfollows likewise | Meta for Developers, Instagram account insights |
| 6 | §6 | Three a quarter is 12 a year, the floor of the 12–51 band; below it the base rate is 1.86% | PB1 D1 Y4 (`others/`) |
| 7 | §7 | Regression to the mean "happens when unusually large or small measurements tend to be followed by measurements that are closer to the mean" | Barnett, van der Pols, Dobson, IJE 34(1), 2005 |
| 8 | §8 | Of 1,000 US and UK creators surveyed, 52% reported burnout and 37% were considering leaving | PB1 §6, row B2 (`others/`) |
| 9 | §9 | In 2023 Google said it would delete accounts inactive for two years, and "We do not have plans to delete accounts with YouTube videos at this time" | TechCrunch, 18 May 2023 |
| 10 | Deliverable (D4) | Click-through under 2% with impressions below her median "is the case YouTube names for a title or thumbnail change" | PB1 D3; YouTube Help 16559651 |
| 11 | Deliverable (D5) | 68% of channels that crossed 1,000 had 40 or more videos; 53.5% had 70 or more; 91.35% of her band stay under 1,000 | PB1 D1 Y4, Y5 (`others/`) |
| 12 | Sources | Newman, "If almost nothing goes wrong, is almost everything all right? Interpreting small numerators", letter, JAMA 274(13), 4 Oct 1995, 1013, crediting Hanley and Lippman-Hand (JAMA, 1983); the 3/n rule | JAMA Network |
| – | Unsure list | No cited claim; nothing sampled | – |

## Limit of this run: no outside source was opened

WebSearch was refused on the first batch and again on the one retry the rules allow ("this turn's web search budget is used up", a limit shared by every agent). The web rule lets WebFetch open only a URL that a search in this agent returned, so nothing could be fetched. Every claim that rests on one of the unit's thirteen outside sources is therefore **unverifiable** in this audit, not PASS. What was checked in full: every pointer to another unit (against `others/`), every Mara fact (against `case-facts.md`), every derived statistic and every piece of Mara's arithmetic and dates (recomputed, `out/recompute.py`), and the four figures.

## Table: the sample

| n | Section | Claim | Source | Verdict | Note |
|---|---|---|---|---|---|
| 1 | §1 | Qualifying ages: 30 days (YT2), 7 days (YT3, YT4), 7 days for an Instagram post | PB6 D2; PB7 D2 | PASS | PB6 D2 rows YT2–YT4 say "uploads at least 30 days old" and "at least 7 days old"; PB7 D2: "A post is read once it is 7 days old" |
| 2 | §2 | Watch hours only from "long-form videos that you've set to public" | YouTube Help 72851 | unverifiable | Page not opened (search refused). PB6 D2 YT10 cites the same answer, which is no check of the page |
| 3 | §3 | About 2,045 impressions (hypothesis 3%, true 2%); about 1,747 the other way; correction adds 100 | NIST §7.2.4.2 | unverifiable | Arithmetic recomputed: 2,044.6 and 1,746.9 with z 1.960 and 0.842. That the handbook gives this formula and a continuity correction of 1/δ was not confirmed: page not opened |
| 4 | §4 | Buffer's I4 is an increment over weeks with no posts: "points added to the weekly growth rate" | PB1 §3, D1 I4 | PASS | Quotation exact in PB1 §3; I4's row heading is "against no posts". Buffer's page not opened |
| 5 | §5 | "Not returned if the IG User has less than 100 followers" | Meta for Developers | unverifiable | Page not opened. PB3 D1 trait 8 and PB7 IG12 say the same, which is no check of the page |
| 6 | §6 | Floor of the 12–51 band; below it 1.86% | PB1 D1 Y4, D3 | PASS | PB1 D1 Y4: 1.86% (1–11), 8.65% (12–51); PB1 D3 stop rule uses the same words |
| 7 | §7 | Regression to the mean "happens when unusually large or small measurements tend to be followed by measurements that are closer to the mean" | Barnett et al., IJE 2005 | unverifiable | PubMed page not opened |
| 8 | §8 | 1,000 US and UK creators: 52% burnout, 37% considering leaving | PB1 §6, D1 B2 | PASS | PB1 D1 B2: "52% experienced burnout; 37% considering leaving", 1,000 US and UK creators, agency survey, self-report. Billion Dollar Boy's page not opened |
| 9 | §9 | Google 2023: two years' inactivity; "We do not have plans to delete accounts with YouTube videos at this time" | TechCrunch, 18 May 2023 | unverifiable | Page not opened |
| 10 | D4 | Low CTR with below-median impressions is the case YouTube names for a title or thumbnail change | PB1 D3; YouTube Help 16559651 | PASS | PB1 D3's figure caption: "a title or thumbnail change is advised when low CTR comes with fewer impressions than usual (answer 16559651)"; PB6 D1 R6 quotes the page to the same effect. The Help page itself not opened; it is cited by number only and is not in Sources (erratum PB10-7) |
| 11 | D5 | 91.35% under 1,000 in her band; 68% of crossers had 40+, 53.5% had 70+ | PB1 D1 Y4, Y5 | PASS | PB1 §2 and D1 Y4, Y5 give all three, each marked derived |
| 12 | Sources | Newman, letter, JAMA 274(13), 4 Oct 1995, 1013; credits Hanley and Lippman-Hand (1983); 3/n | JAMA Network | unverifiable | Page not opened. 3 ÷ 118 = 2.54% recomputed |

## Also checked (beyond the sample)

| n | Section | Claim | Source | Verdict |
|---|---|---|---|---|
| 13 | §1 | PB6 set twelve YouTube rows, PB7 thirteen Instagram rows, PB1 seven reads and four verdicts, PB9 eight revenue rows | others/PB6 D2; PB7 D2; PB1 D3; PB9 D5 | PASS |
| 14 | §1 | Only YT1, YT3, YT4 enter a verdict; IG2 and IG4-IG5 enter IR11 and IR12; the rest has no sourced benchmark at her size | others/PB1 D3; PB7 D1; PB6 D2 and PB7 D2 notes | PASS |
| 15 | §2 | Todd Beaupre, senior director of growth and discovery: "maybe a 10% or less"; PPC Land, 2 Sep 2026 | others/PB1 §2 | PASS |
| 16 | §2 | Band medians +0.5 (1-99) and +1.4 (100-499) subscribers a month; no Instagram timeline from under 1,000 | others/PB1 D1 Y6, I7 | PASS |
| 17 | §3 | NIST §7.2.4.1: Wilson interval's worth "does not strongly depend upon the value of n and/or p"; normal limits unreliable "if the number of failures is very small or if the sample size N is very small" | https://itl.nist.gov/div898/handbook/prc/section2/prc241.htm | unverifiable |
| 18 | §3 | Wilson 95% intervals for 3.0% at 250, 500, 1,000, 2,000 and 5,000 impressions | derived; recomputed (out/recompute.py) | PASS |
| 19 | §3 | Skip rate 62%: 52.2-70.9% on 100 views, 57.2-66.6% on 400; IR12 line 65.5% | derived; recomputed; others/PB7 D1 IR12 | PASS |
| 20 | §3 | Zero sends in 118 reached bounds the rate at about 2.5% (3/118) | derived; recomputed | PASS |
| 21 | §3 | NIST §1.3.6.6.19: Poisson "is used to model" counts in a time interval; standard deviation is the square root of the mean | https://itl.nist.gov/div898/handbook/eda/section3/eda366j.htm | unverifiable |
| 22 | §3 | PB9 §8 used the same Poisson model for sales | others/PB9 §8 | PASS |
| 23 | §3 | NIST Dataplot: "the test statistic for the sign test follows a binomial distribution with p=0.5" | https://itl.nist.gov/div898/software/dataplot/refman1/auxillar/signtest.htm | unverifiable |
| 24 | §3 | 0.5^n: 12.5%, 6.25%, 3.1%; range coverage 93.75% (5) and 96.9% (6); order-statistic intervals 3rd-10th of 12 (96.1%) and 12th-25th of 36 (97.1%) | derived; recomputed | PASS |
| 25 | §3 | Verdict-3 table: 87.7/99.7, 46.9/59.7, 13.0/3.3, 2.0/under 0.1 | derived; recomputed (exact binomial) | PASS |
| 26 | §3 | Only two of thirteen uploads passed 2,000 impressions in Q1 and Q2 | unit D3, D4 (uploads 3 and 10) | PASS |
| 27 | §4 | Y1: median about 180 to 272; median best of ten 1,948 | others/PB1 D1 Y1 | PASS |
| 28 | §4 | Y2: half of channels and videos between 2% and 10% click-through | others/PB1 D1 Y2 | PASS |
| 29 | §4 | Y3: 40-55% viewed for 5-15 minute videos, vendor heuristic, no sample | others/PB1 D1 Y3 | PASS |
| 30 | §4 | Y4: 8.65% of channels adding 12-51 videos crossed 1,000 within 360 days | others/PB1 D1 Y4 | PASS |
| 31 | §4 | Y5: 68% of crossers had 40 or more videos | others/PB1 D1 Y5 | PASS |
| 32 | §4 | Y6: +0.5, +1.4, +3.7 subscribers a month by band | others/PB1 D1 Y6 | PASS |
| 33 | §4 | Y10, Y11: 8,000 and 3,000 watch hours with 1,000 and 500 subscribers | others/PB1 D1 Y10, Y11 | PASS |
| 34 | §4 | Y12, I5: Live at 50 subscribers; Instagram Live at 1,000 followers | others/PB1 D1 Y12, I5 | PASS |
| 35 | §4 | I3: median reach 261 accounts a post, all sizes pooled | others/PB1 D1 I3 | PASS |
| 36 | §4 | I4: +0.26% weekly growth at 3-5 posts against weeks with none | others/PB1 D1 I4 | PASS |
| 37 | §4 | I6: no published follower threshold for Instagram earning tools | others/PB1 D1 I6 | PASS |
| 38 | §4 | B1, B2: hours creators report; burnout | others/PB1 D1 B1, B2 | PASS |
| 39 | §4 | Y7, Y8, Y9, I1, I2, I7 excluded, with the reason given for each | others/PB1 D1 | PASS |
| 40 | §4 | PB1's Q3 instruction compares net followers "with the 0.36-a-week illustration (I4)"; PB7 IG8 sets the same figure as a reference | others/PB1 D3 Q3 line and correction note; others/PB7 D2 IG8 and correction note | STALE |
| 41 | §5 | PB1 took the review's hour from "that fortnight's publishing-and-replies line" (PB1 D2); PB4 repeated it (PB4 D1 G) | others/PB1 D2 and correction note; others/PB4 D1 G and correction note | STALE |
| 42 | §5 | The line was 1.5 h, cut to 1.25 with 0.25 to email (PB3), split into 0.75 replies and 0.5 scheduling (PB4 D1 E) | register (PB1 hours); others/PB3 D2; others/PB4 D1 E | PASS |
| 43 | §5 | Buffer: +0.12% at 1-2 posts against +0.26% at 3-5; about 0.3 followers a week at 212 | others/PB1 §3, D1 I4; recomputed | PASS |
| 44 | §5 | Q2, Q3, Q4 plan 37 posts; Q2 plans 29 if the guide is built | register (PB7 entry); others/PB1 correction note; others/PB7 D2 | PASS |
| 45 | §5 | Repeat-back test: five strangers, ten minutes, four of five; conventions; one answer moves the result 20 points | others/PB2 §3, D5 | PASS |
| 46 | §5 | YouTube 9101241: demographic thresholds "are not published"; "Not enough demographic data" | https://SUPPORT.GOOGLE.COM/youtube/answer/9101241 | unverifiable |
| 47 | §5 | Next season's first two pieces picked by week 10; the rest by the two-weekend rule unless a bank exists | others/PB4 §6, §1 | PASS |
| 48 | §5 | YouTube 141805: "found no correlation between break length and changes in views"; "growth in views across uploads is not correlated with time between uploads" | https://support.google.com/youtube/answer/141805?hl=en | unverifiable |
| 49 | §5 | AIR Media-Tech: dark 14+ days three or more times a year goes with fewer views per video; main analysis 100,000-1,000,000 monthly views | others/PB1 §6 (AIR page not opened) | PASS |
| 50 | §5 | 13, 27 and 20 days with no upload; two breaks leave 24 uploads, passing the cadence test of 24 and staying in the 12-51 band | derived; others/PB1 D3, D1 Y4 | PASS |
| 51 | §5 | PB4 §1 earlier wording "If her log shows pieces averaging more than two weekends", with the P108 note | others/PB4 §1 and its correction note of 13 Nov 2026 | PASS |
| 52 | §5 | Mean 2.14; 26.4% and 73.7% a quarter; about 7% and 54% for two quarters; about 5% and 48% with a six-piece quarter | derived; recomputed | PASS |
| 53 | §5 | PB6 R6: one upload 28+ days old, lowest CTR, impressions below median, Intro at or above median; change in the packaging hour; Intro needs 100 views | others/PB6 D1 R6, D2 YT5 | PASS |
| 54 | §5 | PB8 clause 10 re-read at each checkpoint, with five one-line questions from the pre-mortem | others/PB8 D1 clause 10, D2 | PASS |
| 55 | §5 | PB9 rows R1-R8 have first-read dates; the guide decision at Q1 depends on T1 | others/PB9 D5, D1 | PASS |
| 56 | §6 | Four verdicts in PB1's order; load verdict over 7 hours in 3 or more weeks; cut order; verdict 3 as corrected | others/PB1 D3; others/PB3 D2 | PASS |
| 57 | §6 | A format change takes effect at the season's second video | others/PB4 §4 | PASS |
| 58 | §6 | IR12's 65.5% is an average for brand accounts of 1,000-5,000 followers | others/PB7 D1 IR12, D2 IG4 | PASS |
| 59 | §7 | Kohavi et al. 2009: controlled experiments are "the best scientific design for establishing a causal relationship between changes" | https://exp-platform.com/journal-survey | unverifiable |
| 60 | §7 | Test & Compare is computer-only and may return "Not enough impressions" or "Inconclusive"; likely inconclusive at small views (inference) | others/PB6 §3 | PASS |
| 61 | §7 | No source measures how one platform affects the other | others/PB3 §4; others/PB7 §9 | PASS |
| 62 | §8 | Recovery weeks plan 6.5 hours; the 4-hour edit stop; three consecutive overruns move the video to about 8 minutes | others/PB4 §7, §5; others/PB5 §9 | PASS |
| 63 | §8 | Register tasks: contract by Sun 29 Nov 2026, trademark search by Sun 6 Dec 2026, sign-up notice by Sun 31 Jan 2027 | others/PB8 D3 (J1, M1, E3) | PASS |
| 64 | §8 | No dataset gives hours per video or post for one-person accounts | others/PB1 §8 | PASS |
| 65 | §9 | PB8 clause 9 (announce within the week) and clause 8 (delete only for privacy, safety, legal demand) | others/PB8 D1 | PASS |
| 66 | §9 | Watch hours count over the last 365 days; a separate Partner Programme activity rule from 1 February 2027 | others/PB1 §4 | PASS |
| 67 | Deliverable D1 | Rows YT5 (100 views; 50% list), YT8 (from Q2), YT11 (from Q3), IG13 (1,000 followers, IR8), R5 (0.62%, V14), R8 (150 USD cap) | others/PB6 D2; PB7 D1, D2; PB9 D2, D5; PB1 D2 | PASS |
| 68 | Deliverable D2 | Studio and Insights not opened between reviews | others/PB1 D3; others/PB7 D2 | PASS |
| 69 | Deliverable D3 | Q1 hours 77.25, median 6.0, one week over 7; posts 35 of 39, 32 qualifying; medians 61, 1,015, 56.5%; Wilson 1.1-2.9% | unit's own values; recomputed; register | PASS |
| 70 | Deliverable D3 | Review and upload dates, weekdays and week numbers of Q1; guide blocks and launch (PB9 D1) | recomputed; others/PB9 D1; register | PASS |
| 71 | Deliverable D4 | Q2 hours 80.75, median 6.0, week 21 over 7; plan 29, published 25, 24 qualifying; medians 72, 1,275, 55.5%; Wilson intervals; IR11 counts 36 and 23 | unit's own values; recomputed; register | PASS |
| 72 | Deliverable D4 | None past 1,000 views, as for 42.2% of PB1's cohort | others/PB1 D3 (Q2 line) | PASS |
| 73 | Deliverable D4 | Guide net 13.00 a sale; V6 is 2, 8, 24 sales over 209 days; 26-day expectations 0.25, 1.0, 3.0 | others/PB9 D2 V6, D3; recomputed | PASS |
| 74 | Deliverable D4 | New thumbnail "at most four words, in her colours (PB5 §7)" | others/PB5 §7 (four words) and §8 (colours) | FAIL |
| 75 | Deliverable D5 | Year-two review dates, upload ranges, 1 January 2029; cadence test of 24; first count of subscribers at 24 months | recomputed; others/PB1 D3; register | PASS |

Notes on three rows. Row 40 (§4) and row 41 (§5): PB1 D2, PB1 D3's Q3 line, PB4 D1 G and PB7 IG8 were all corrected on 13 November 2026 at this unit's prompting, so the words PB10 quotes from PB1 are no longer in PB1 and its present-tense account of PB1 and PB7 is out of date; the unit already carries such a note for PB4 §1 (P108) and needs the same two here (errata PB10-1, PB10-2). Row 74 (D4): the colour rule is PB5 §8, not §7 (erratum PB10-3).

## Not checked

- WebSearch: refused twice ("this turn's web search budget is used up"; limit of 200 searches shared by every agent). Seven queries were sent in two attempts; none ran. Not checked: permission.
- WebFetch: not used. No search returned a URL, so the web rule allowed no fetch.
- Each of the unit's thirteen outside sources, not checked: permission:
  - https://support.google.com/youtube/answer/72851?hl=en-GB
  - https://itl.nist.gov/div898/handbook/prc/section2/prc241.htm
  - https://itl.nist.gov/div898/handbook/prc/section2/prc242.htm
  - https://itl.nist.gov/div898/handbook/eda/section3/eda366i.htm
  - https://itl.nist.gov/div898/handbook/eda/section3/eda366j.htm
  - https://itl.nist.gov/div898/software/dataplot/refman1/auxillar/signtest.htm
  - https://jamanetwork.com/journals/jama/article-abstract/389714
  - https://developers.facebook.com/docs/instagram-platform/api-reference/instagram-user/insights
  - https://SUPPORT.GOOGLE.COM/youtube/answer/9101241
  - https://support.google.com/youtube/answer/141805?hl=en
  - https://exp-platform.com/journal-survey
  - https://pubmed.ncbi.nlm.nih.gov/15333621/
  - https://techcrunch.com/2023/05/18/youtube-will-no-longer-be-deleting-videos-from-inactive-accounts
- The sources behind the carried figures (vidIQ, Buffer, Billion Dollar Boy, AIR Media-Tech, PPC Land, YouTube Help 16559651): not opened; those claims were checked against the PB units the unit cites for them.

## Failure rate

- Sample: 12 claims. PASS 6, FAIL 0, STALE 0, unverifiable 6. Failure rate 0 of 12 (0%); the full audit is not triggered.
- All claims checked: 75. PASS 60, FAIL 1 (a section pointer, minor), STALE 2, unverifiable 12.
- Of the 6 sampled claims that passed, all rest on other units of the course. No sampled claim resting on an outside source could be confirmed.

## Counts

- Words (`wc -w unit.md`): 12,786. `##` sections: 12.
- Cited claims in the whole unit: **173**. Counted by `out/count_claims.py` (every sentence or table row outside the `viz` blocks that names a linked source, a unit pointer or the handbook; 191 candidates, saved in `out/claim_candidates.json`), then adjusted by reading: 12 rows of §4's table added (they carry PB1's row code without the letters "PB"), and 30 candidates removed that state no claim (method statements, cross-references, procedure steps, the templates, and the Sources and Unsure lists, which are references and not claims).

| Section | Cited claims |
|---|---|
| Opening paragraphs | 1 |
| §1 | 6 |
| §2 | 6 |
| §3 | 10 |
| §4 | 15 |
| §5 | 32 |
| §6 | 11 |
| §7 | 4 |
| §8 | 9 |
| §9 | 7 |
| Deliverable D1 | 35 |
| Deliverable D2 | 2 |
| Deliverable D3 | 13 |
| Deliverable D4 | 13 |
| Deliverable D5 | 9 |
| Templates | 0 |
| Sources | 0 |
| Unsure list | 0 |
| **Total** | **173** |

Sixteen of the 173 name an outside source directly (§2 one, §3 six, §5 three, §7 two, §9 two, D4 one, D5 one); the rest rest on other units of the course or on the unit's own derivations.

## Figures

1. `range`, §3, "A 3.0% click-through reading": five labels and ten bounds match the table above it (1.50–5.93, 1.83–4.89, 2.11–4.25, 2.34–3.84, 2.56–3.51), and all ten were recomputed. Caption names §3, the handbook section and "derived in this unit". **PASS.**
2. `compare`, §3, "Chance that 3 or more of 6 uploads read under 2%": 99.7, 59.7, 3.3 match the table and the recomputation; 0.0 stands for "under 0.1%" (0.02% recomputed) and the caption says so. **PASS.**
3. `matrix`, §5, "What each unit hands the review": every cell traces to §5, D2 or D5 (0.75 h; 5 min; 3 min; annual page; packaging hour; three reply slots; two Reels fewer). The row "PB7 IR11 and IR12" gives "from Q2" for both, where §5's heading has IR11 at Q2 only; the row is a merged one and adds no fact. **PASS.**
4. `flow`, D2, "The quarterly review in sixty minutes": the seven steps, their minutes and their row codes match D2 steps 1–7 and the block headings of D1. **PASS.**

No figure needs a fix.

## Deliverable

- It exists in full: D1 the metrics sheet (47 rows in five blocks), D2 the sixty-minute procedure with its beside-the-hour list, D3 and D4 the procedure run on Mara's Q1 and Q2, D5 the one-page annual review, T1–T4 the templates, each blank saying what goes in it. That is what the brief asks for.
- It follows from the unit's evidence: verdict 3's count rests on §3's binomial table; IR12 is kept out of verdict 3 with its reason; the hours come first because verdicts 1 and 2 read them.
- Mara's arithmetic holds throughout: hours (77.25 and 80.75, medians 6.0, one week over 7 in each quarter), post counts (39, 35, 32; 29, 25, 24; IR11's 36 and 23), medians (61, 72, 100; 1,015 and 1,275; 56.5% and 55.5%), Wilson intervals, the verdict-3 count of three, subscribers (23, 61; 50 passed in June), followers (212, 318), age bands (100%; 89% under 55), traffic splits (100%), the guide (3 × 13.00 = 39.00; 0.25, 1.0, 3.0 expected in 26 days), and every date, weekday and week number through 1 January 2029.
- Mara's facts agree with `case-facts.md` (the PB10 entry and the earlier entries it depends on). She is labelled "(Mara, fictional)" on first use in the body and in the deliverable, and is never used as evidence.
- One contradiction with another unit (flag PB10-8): D4's Q2 format change moves her thumbnail to "the fault and the finished piece side by side ... in place of the finished piece alone", but PB5 §7 and PB5's own deliverable already set her thumbnail as "the as-found and finished views ... side by side". As filed, the Q2 verdict's one change is the layout she already uses.
- One line reads wrongly against its own table (erratum PB10-6): R6 calls upload 11's 1.7% the lowest CTR while upload 13 reads 1.6%; upload 13 is under 28 days old, which the line should say.
- Usable without the unit: yes for D2–D5 and the templates. D1 leans on the body in four cells ("§3's √n", "§3's 3/n", "None (§4)", "(§5)"); each is a pointer to a reason, and the row can be read without it.

## Course goal and sourcing standard

- Course goal: the unit delivers the third outcome directly (reading Instagram and YouTube numbers against sourced benchmarks each quarter to decide whether to continue, change format or stop), and D5 extends it to the 24-month rule.
- Advice without evidence: none found. Each rule no source sets is marked "her rule"; each of those rests on §3's statistics or on a named row of an earlier unit. Estimates of time are marked as hers and listed in the Unsure list.
- Sourced where made, figures say whose they are, labels (vendor, correlational, survivor, platform-official, derived, statistical reference): met.
- "Words in quotation marks are the source's exact words": not met in two places, where PB1 is quoted in wording PB1 no longer has (errata PB10-1, PB10-2).
- "The unit leaves its sources": the closing line of Sources names only PB1, PB6, PB7 and PB9 as the units figures are carried from, while the unit also carries from PB2, PB3, PB4, PB5 and PB8; YouTube Help 16559651 is cited in D4 by number only and listed nowhere (erratum PB10-7). One URL's host is in capitals in the body and in Sources (errata PB10-4, PB10-5).
- Neutral ground on tax and law, platform named for each metric claim, changeable facts dated (13 Nov 2026), no private-course reference: met.
- Source types: the NIST handbook, a JAMA letter and TechCrunch fall outside the four types Part 5 names; each is labelled for what it is.

## Verdict

**PB10: PASS** on the decision rule (0 FAIL in 12 sampled claims; no full audit run), with two should-fix errata, five minor errata and one flag.

The PASS is qualified. Six of the twelve sampled claims, and twelve of the 75 checked, rest on outside sources that could not be opened in this run, and they are reported as unverifiable. The stratified sample has not tested this unit's outside citations. Those six sampled claims (rows 2, 3, 5, 7, 9, 12) should be opened when search is available before Audit 3 is closed for PB10.

## The most consequential errors

1. D4's Q2 verdict changes Mara's thumbnail to a layout PB5 had already given her, so the one worked example of "change the format" changes nothing (flag PB10-8; needs a decision between PB10 and PB5).
2. §4 and §5 describe PB1, PB4 and PB7 as they read before 13 November 2026 and quote words PB1 no longer contains; a reader who checks the citation finds a different sentence (errata PB10-1, PB10-2).
3. None further. The remaining findings are a section pointer, a URL's capitals, one unclear line in D4 and an incomplete closing line in Sources.

## Bibliography line

No new source to add and none to mark failed; the thirteen sources PB10 lists stay "not re-checked on 14 Nov 2026" (search refused); normalise `https://SUPPORT.GOOGLE.COM/youtube/answer/9101241` to lower case so it merges with PB3's entry, and note that PB10 D4 also cites YouTube Help 16559651 (already in the bibliography through PB1 and PB6).

## Changelog line

2026-11-14 · Audit 3, PB10 · claude-fable-5-2 (fresh isolated agent) · stratified sample 12 claims: 6 PASS, 0 FAIL, 6 unverifiable (web search refused, no outside source opened); 75 claims checked in all: 60 PASS, 1 FAIL, 2 STALE, 12 unverifiable; verdict PASS, qualified; 7 errata (2 should-fix, 5 minor), 1 flag (D4's thumbnail change against PB5 §7); figures 4 of 4 PASS.

## Errata

**PB10-1** · should-fix · STALE · §4
- Current: `Read PB1 D3's Q3 line and PB7's IG8 reference column this way.`
- Fix: `PB1 D3's Q3 line and PB7's IG8 reference column were corrected on 13 November 2026 and now read this way; the words quoted above are PB1's earlier wording.`
- Basis: `others/` PB1 D3, Q3 review line, which no longer holds the quoted words, and PB1's correction note of 2026-11-13; PB7 D2 IG8 and PB7's correction note of 2026-11-13. No URL: units of this course.

**PB10-2** · should-fix · STALE · §5
- Current: `PB1 took the review's hour from "that fortnight's publishing-and-replies line" (PB1 D2), and PB4 repeated it (PB4 D1 G).`
- Fix: `PB1 first took the review's hour from "that fortnight's publishing-and-replies line" (PB1 D2, as worded before 13 November 2026), and PB4 repeated it (PB4 D1 G); both were corrected that day and now take the hour as this section sets it.`
- Basis: `others/` PB1 D2, now "taken from the Instagram derivatives of the fortnight that holds it", and its correction note of 2026-11-13; PB4 D1 G, D2 and its correction note of 2026-11-13. No URL: units of this course.

**PB10-3** · minor · FAIL (section pointer) · Deliverable D4, Verdict
- Current: `in her colours (PB5 §7)`
- Fix: `in her colours (PB5 §7, §8)`
- Basis: `others/` PB5: §7 sets the four-word limit; the colour rule is §8 ("text is white or cream on a near-black or teak band"); the register's PB5 entry says the same. No URL: a unit of this course.

**PB10-4** · minor · other · §5, PB3
- Current: `[YouTube Help, Understand limited data in YouTube Analytics, answer 9101241](https://SUPPORT.GOOGLE.COM/youtube/answer/9101241)`
- Fix: `[YouTube Help, Understand limited data in YouTube Analytics, answer 9101241](https://support.google.com/youtube/answer/9101241)`
- Basis: the host is in capitals; PB3 D1 cites the same page as https://support.google.com/youtube/answer/9101241, and a bibliography collected by URL would list it twice. The page was not opened in this run.

**PB10-5** · minor · other · Sources
- Current: `checked 13 Nov 2026. https://SUPPORT.GOOGLE.COM/youtube/answer/9101241`
- Fix: `checked 13 Nov 2026. https://support.google.com/youtube/answer/9101241`
- Basis: as PB10-4, the same URL in the Sources list; PB3 D1 gives https://support.google.com/youtube/answer/9101241.

**PB10-6** · minor · other · Deliverable D4, YouTube, R6
- Current: `Lowest CTR, upload 11 (1.7%);`
- Fix: `Lowest CTR among them, upload 11 (1.7%; upload 13's 1.6% is lower but the upload is under 28 days old);`
- Basis: the unit's D4 table (upload 13: 1.6%, 13 days old on 5 Jul 2027); `others/` PB6 D1 R6 ("at least 28 days old whose CTR is the lowest of the quarter"). No URL: internal.

**PB10-7** · minor · other · Sources, closing line
- Current: `PB1 D1 (Y1–Y12, I1–I7, B1–B2), PB1 §2, §4 and §6, PB6 D1–D2, PB7 D1–D2, PB9 D2–D5;`
- Fix: `PB1 D1 (Y1–Y12, I1–I7, B1–B2), PB1 §2, §3, §4, §6 and §8, PB1 D2–D3 (which carries YouTube Help 16559651), PB2 §3 and D5, PB3 §4 and D1–D2, PB4 §1 and §4–§7, PB5 §7–§9, PB6 §3 and D1–D2, PB7 §9 and D1–D2, PB8 D1–D3, PB9 §8 and D1–D5;`
- Basis: the unit also rests figures and rules on those sections (each pointer checked in `others/`); sourcing standard Part 1, "The unit leaves its sources". No URL: internal.

**PB10-8** · flag · should-fix · other · Deliverable D4, Verdict (also D5 item 2 and the register's PB10 entry)
- Current: `in place of the finished piece alone.`
- Fix: not an exact replacement; a decision is needed. Either PB5 §7 and its deliverable are changed so that Seasons 1–2 thumbnails show the finished piece alone, or D4's Q2 change is rewritten as a change PB5 has not already made (for example the title, or the thumbnail's words), with the register's PB10 line and D5 item 2 following.
- Basis: `others/` PB5 §7 item 1 ("usually the as-found and finished views from the taped mark side by side") and PB5's deliverable, piece 1 ("thumbnail the as-found and finished views from the taped mark side by side"). No URL: internal.

Working files left in `out/`: `recompute.py`, `count_claims.py`, `claim_candidates.json`, `build.py`.
