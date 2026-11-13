---
audit: fresh check
unit: PB10 · Read your numbers: the quarterly review
course: personal-brand · PB · Building a Personal Brand on Instagram and YouTube
model: Opus 5.5 (claude-opus-5-5, as the agent states; this session keeps no agent transcript on disk, so the model could not be confirmed from a transcript's "model" field; live search). A Fable 5.1 fresh check of PB10 is owed to the Fable stage (P49)
date: 2026-11-13
chat: own Opus 5.5 agent context, not shown the writing (P31), launched by the W-PB9/W-PB10 chat (which ran on Opus 5.5 and only staged, applied, filed and published) in session https://claude.ai/code/session_01KMmgR1xZNfEBXV8FGL7SYn
verdict: fix · 0 errors, 8 should-fix, 33 minor
---

The checker's final report, verbatim, as the file it wrote in its own folder (`out/fresh-check.md`), copied unchanged by script. Saved before any finding was applied. The exact strings applied are its `out/findings.json`.

Model: claude-opus-5-5

# PB10 · Fresh check · Read your numbers: the quarterly review

Checked 13 Nov 2026 with live search. I read only the unit, its brief, sourcing standard Parts 1 and 5, case-facts.md, notes.md, the filed units PB1–PB9, and the A6/A9 source units for pointers. No audit report was used. The unit was not edited. Every statistic and every piece of Mara arithmetic was recomputed in Python (scipy).

## (1) Coverage

- Full metrics sheet from PB6's and PB7's rows (D1, all of YT1–YT12 and IG1–IG13, plus H, AU, R and HO rows): covered.
- Numbers that lead and lag (§2): covered.
- Small-number noise, and how many posts a rate needs, argued from sourced statistics (§3: Wilson, sample size, rule of three, Poisson, sign test/binomial, median coverage): covered. Two stretches of what NIST says (findings 3, 5).
- Setting the quarter against PB1's expectation sheet (§4): covered. Y9 is omitted (finding 7).
- PB2 repeat-back test run 2 at Q1, beside, 0.75 h from reply slots: covered.
- PB3 traits 8 and 9, with the Meta API 100-follower threshold and YouTube's unpublished thresholds, inside: covered, with the API qualifier kept.
- PB4's three items (picking the next pieces, inside; a break between seasons at the twelve-month review, beside; the log of weekends, overruns and 6.5-hour weeks against the 7-hour line, inside), each placed and its hours found: covered. The break argument is flawed (finding 1).
- The four verdicts and the evidence for each (§6): covered.
- One change at a time (§7): covered.
- Hours against budget (§8): covered.
- Pausing or stopping without deleting the record (§9): covered.
- Deliverable: metrics sheet (D1), sixty-minute procedure (D2), Mara's Q1 and Q2 run (D3, D4), one-page annual review (D5, with Q3 and Q4 lines left to fill, which is correct since they have not happened), templates T1–T4: all covered.

## (2) Accuracy: findings

1. [should-fix] [accuracy] §5 PB4 item 2; Current: "The rule in D5 allows at most two breaks a year, each one fortnight with no upload, so that gaps of 14 days or more happen at most twice."; Problem: The rule's claim is false at her cadence: uploads are 14 days apart, so AIR's 14-day line sits one day past her normal rhythm, and every upload moved 7 days under PB4 §7 (a planned recovery rule) also leaves a 14+ day gap. The unit also drops PB1 §6's caveat that AIR's main analysis covers channels with 100,000–1,000,000 monthly views.; Fix: "The rule in D5 allows at most two breaks a year, each one fortnight with no upload. At her cadence uploads are 14 days apart, with 13 days between them carrying no upload, so AIR's line sits one day past her normal rhythm: a break leaves 27 days with no upload, and an upload moved 7 days under PB4 §7 leaves 20, so moved uploads count towards the same three. AIR's main analysis covers channels with 100,000 to 1,000,000 monthly views, far larger than hers (PB1 §6)."; Basis: PB1 §6 (AIR, 8 Jun 2026, as PB1 reports it; AIR page not returned by search: unverifiable); PB4 §7 lost-week-B rule; https://air.io/en/audience-growth/does-posting-more-on-youtube-help-we-studied-18000-channels-to-find-out (not checked)
2. [minor] [accuracy] D5 item 6; Current: "(gaps of 14+ days at most twice a year, against the "three or more times" of PB1 §6;"; Problem: Same claim repeated in the annual page; moved uploads also produce 14+ day gaps.; Fix: "(two breaks, plus any upload moved 7 days under PB4 §7, kept under the "three or more times" of PB1 §6;"; Basis: PB4 §7
3. [should-fix] [accuracy] §3 One rate, one post; Current: "and the Wilson interval corrects it when n or the count is small"; Problem: Stretch: NIST §7.2.4.1 gives the Wilson interval and says its worth "does not strongly depend upon the value of n and/or p"; it does not say Wilson corrects the normal interval at small n (its small-sample remedy is the exact binomial method).; Fix: "and the handbook also gives the Wilson interval, whose worth "does not strongly depend upon the value of n and/or p""; Basis: https://itl.nist.gov/div898/handbook/prc/section2/prc241.htm
4. [minor] [figure] §3 One rate, one post; Current: "gives about 2,045 impressions to tell a true 2% from a true 3% at the usual 5% significance and 80% power (derived: z values 1.96 and 0.84)"; Problem: NIST's formula puts p0 (the hypothesis) with z(1−α/2). 2,045 holds with p0 = 3% and unrounded z; with the z values the unit names (1.96, 0.84) it is 2,043; with p0 = 2% it is about 1,747; the handbook adds a continuity correction of 1/δ = 100. The unit names none of this.; Fix: "gives about 2,045 impressions to tell a true 2% from a hypothesised 3% at the usual 5% significance (two-sided) and 80% power, or about 1,747 with 2% as the hypothesis (derived: z values 1.960 and 0.842; the handbook's continuity correction adds 100 to each)"; Basis: https://itl.nist.gov/div898/handbook/prc/section2/prc242.htm; recomputed in Python
5. [minor] [accuracy] §3 Counts per month; Current: "Net subscribers or followers gained in a month are counts of independent decisions, which the NIST handbook models as Poisson, with a standard deviation equal to the square root of the mean"; Problem: NIST says the Poisson "is used to model the number of events occurring within a given time interval"; it does not model net subscribers or call them independent decisions. A net count (gains less losses) is not Poisson.; Fix: "Subscribers or followers gained in a month are a count of events in a time interval, which the NIST handbook says the Poisson distribution "is used to model", with a standard deviation equal to the square root of the mean; reading a net count (gains less losses) the same way is an assumption"; Basis: https://itl.nist.gov/div898/handbook/eda/section3/eda366j.htm
6. [minor] [attribution] §2 Lagging; Current: "YouTube's director of growth and discovery put"; Problem: PPC Land and PB1 §2 give Todd Beaupré as YouTube's "senior director of growth and discovery".; Fix: "YouTube's senior director of growth and discovery, Todd Beaupré, put"; Basis: https://ppc.land/subscribers-skip-90-of-uploads-in-their-feed-youtube-director-says/; PB1 §2
7. [minor] [coverage] §4; Current: "Rows Y7, Y8, I1, I2 and I7 do not enter the review: Y7 applies only above 1,000 subscribers, Y8 and I2 are context with undefined windows, I1's sample starts at 1,000 followers and I7 has no source (PB1 D1)."; Problem: Y9 (months to 1,000; no sourced figure) is in neither the table nor the excluded list; I2's gap is an undefined growth measure, not a window.; Fix: "Rows Y7, Y8, Y9, I1, I2 and I7 do not enter the review: Y7 applies only above 1,000 subscribers, Y8 is context with an undefined window and I2 context with an undefined growth measure, I1's sample starts at 1,000 followers, and Y9 and I7 have no source (PB1 D1)."; Basis: PB1 D1 rows Y8, Y9, I2
8. [minor] [style] §6 verdict 2; Current: "a season of deferred replies is a season without replies, and a moved cadence is verdict 1's business."; Problem: Same paragraph says a moved cadence is verdict 1's business, then lists PB4's cadence move as a verdict-2 change.; Fix: "a season of deferred replies is a season without replies, and a season of moved dates is a lower cadence, which only verdict 1 or PB4's cadence move (§5) may set."; Basis: Unit §6
9. [minor] [accuracy] §7; Current: "YouTube's own Test & Compare is computer-only and returns "Not enough impressions" or "Inconclusive" for small channels, and Mara works on a phone (PB6 §3)"; Problem: PB6 §3 says Test & Compare "may return" those messages and that a small channel is likely to get inconclusive results (inference); the unit states it as fact.; Fix: "YouTube's own Test & Compare is computer-only and may return "Not enough impressions" or "Inconclusive", the likely result at a small channel's views (PB6 §3, inference), and Mara works on a phone (PB6 §3)"; Basis: PB6 §3 (YouTube Help 16391400 as PB6 quotes it)
10. [minor] [label] §8; Current: "because burnout is what the evidence links to quitting (PB1 §6, row B2: 52% of 1,000 US and UK creators surveyed reported burnout; agency survey, self-report)"; Problem: B2 is a prevalence survey: 52% burnout, 37% considering leaving; it does not link the two.; Fix: "because burnout is the strain creators report most (PB1 §6, row B2: of 1,000 US and UK creators surveyed, 52% reported burnout and 37% were considering leaving; agency survey, self-report)"; Basis: PB1 §6 and D1 B2 (Billion Dollar Boy, 7 Jul 2025)
11. [minor] [accuracy] §9; Current: "In 2023 Google said it would delete personal Google accounts inactive for two years"; Problem: TechCrunch says Google's policy covers "any account that has not been active in two years"; it does not say "personal".; Fix: "In 2023 Google said it would delete Google accounts inactive for two years"; Basis: https://techcrunch.com/2023/05/18/youtube-will-no-longer-be-deleting-videos-from-inactive-accounts
12. [minor] [figure] §5 PB4 item 3; Current: "(derived, binomial: 26.4% and 73.7% for one quarter, squared)"; Problem: The 7% and 54% assume seven pieces in both quarters; consecutive quarters run 7 and 6 (Q1 7, Q2 6), giving 5.5% and 47.8%.; Fix: "(derived, binomial, seven pieces a quarter: 26.4% and 73.7% for one quarter, squared; with a six-piece and a seven-piece quarter, about 5% and 48%)"; Basis: Recomputed in Python (binomial)
13. [should-fix] [figure] D4 YouTube YT9; Current: "50 passed in May"; Problem: Mara's own figures: 23 + 11 = 34 by the end of month 1, + 13 = 47 by the end of month 2, + 14 = 61. She passes 50 in the third month (June), not May.; Fix: "50 passed in June"; Basis: D3 and D4 YT9; arithmetic
14. [should-fix] [figure] D4 YouTube YT5; Current: "Intro shown for uploads 2, 3, 5, 6, 8, 9, 10 and 11; her median 55.5%."; Problem: D3 shows Intro "not shown" for uploads 5 and 6, and no Intro values for them are given anywhere, so the median of eight cannot be checked. The six stated values (52, 61, 59, 54, 51, 57) have a median of exactly 55.5%, and R6 still qualifies (57% ≥ 55.5%).; Fix: "Intro shown for uploads 2, 3, 8, 9, 10 and 11 (52%, 61%, 59%, 54%, 51%, 57%); her median of the six, 55.5%."; Basis: D3 and D4 tables; recomputed
15. [minor] [attribution] D3 Money R8; Current: "within PB5's 40 USD line"; Problem: The 40 USD tripod-or-clamp line is PB1 D2's; PB5 §10 only says the clamp is already in PB1's line.; Fix: "within PB1 D2's tripod-or-clamp line of up to 40 USD"; Basis: PB1 D2; PB5 §10
16. [minor] [attribution] D2; Current: "Studio and Insights not opened since the last review (PB1 D3)"; Problem: PB1 D3 says only that Studio and Insights "are opened for the review on its date"; "and not between them" is PB7 D2's.; Fix: "Studio and Insights not opened since the last review (PB1 D3; PB7 D2)"; Basis: PB1 D3; PB7 D2
17. [minor] [deliverable] D1 Block E; Current: "**Block E · Handed-over items (minutes 45–50)**"; Problem: Block E's heading puts HO5 and HO6 at minutes 45–50; D2 step 4 runs IR11 and IR12 at minutes 28–40, and HO2 and HO4 are beside the hour.; Fix: "**Block E · Handed-over items (HO1 and HO3 at minutes 45–50; HO5 and HO6 in the Instagram block, minutes 28–40; HO2 and HO4 beside the hour)**"; Basis: Unit D1, D2
18. [minor] [style] D3 Handed-over items HO3; Current: "piece 10, a teak magazine rack; 11, a telephone side table; 12, a small teak wall shelf; 13, a teak plant stand."; Problem: Register consistency: PB2 D1 sets her pieces as mid-century chairs, side tables and small cabinets. A magazine rack, a wall shelf and a plant stand fall outside that, the positioning the repeat-back test checks.; Fix: "piece 10, a teak coffee table; 11, a telephone side table; 12, a small teak wall cabinet; 13, a teak plant table."; Basis: case-facts.md, PB2 entry
19. [minor] [style] D4 YouTube table; Current: "| 10 · 11 May | Teak magazine rack |"; Problem: As 18.; Fix: "| 10 · 11 May | Teak coffee table |"; Basis: case-facts.md
20. [minor] [style] D4 YouTube table; Current: "| 12 · 8 Jun | Small teak wall shelf |"; Problem: As 18.; Fix: "| 12 · 8 Jun | Small teak wall cabinet |"; Basis: case-facts.md
21. [minor] [style] D4 YouTube table; Current: "| 13 · 22 Jun | Teak plant stand |"; Problem: As 18.; Fix: "| 13 · 22 Jun | Teak plant table |"; Basis: case-facts.md
22. [should-fix] [style] §4; Current: "The correction is in the notes to PB1 and PB7."; Problem: Points the reader to writer's notes they cannot open.; Fix: "Read PB1 D3's Q3 line and PB7's IG8 reference column this way."; Basis: Brief preamble (reader persona)
23. [should-fix] [style] §5; Current: "the counts it changes in PB1, PB7 and the register are listed in the notes."; Problem: Points to the internal register and notes; the reader needs the counts themselves. 39 − 2 = 37; 37 − 8 = 29.; Fix: "each review takes two Reels from the quarter after it, so Q2, Q3 and Q4 each plan 37 posts in place of 39, and Q2 plans 29 if the guide is built (derived)."; Basis: Brief preamble; arithmetic
24. [should-fix] [style] §5 PB4 item 3; Current: "The correction is proposed to PB4 in the notes."; Problem: Points the reader to notes they cannot open.; Fix: "This unit reads PB4's rule this way from here on."; Basis: Brief preamble
25. [minor] [style] §1; Current: "copied into IG10 (flag F49)."; Problem: Internal writer flag; the reader cannot open or interpret it.; Fix: "copied into IG10."; Basis: Brief preamble (reader persona)
26. [minor] [style] §5 PB2; Current: "(PB2 §3; flag F20)"; Problem: Internal writer flag; the reader cannot open or interpret it.; Fix: "(PB2 §3)"; Basis: Brief preamble (reader persona)
27. [minor] [style] §5 PB3; Current: "was not checked (flag F55)."; Problem: Internal writer flag; the reader cannot open or interpret it.; Fix: "was not checked."; Basis: Brief preamble (reader persona)
28. [minor] [style] §5 PB6; Current: "(PB6 D1 R6; flag F46)"; Problem: Internal writer flag; the reader cannot open or interpret it.; Fix: "(PB6 D1 R6)"; Basis: Brief preamble (reader persona)
29. [minor] [style] §5 PB8; Current: "(PB8 D1 clause 10, D2; flag F62)"; Problem: Internal writer flag; the reader cannot open or interpret it.; Fix: "(PB8 D1 clause 10, D2)"; Basis: Brief preamble (reader persona)
30. [minor] [style] §5 PB8; Current: "under an admin line (§8; flag F57)"; Problem: Internal writer flag; the reader cannot open or interpret it.; Fix: "under an admin line (§8)"; Basis: Brief preamble (reader persona)
31. [minor] [style] §5 PB9; Current: "at every review (flag F67)."; Problem: Internal writer flag; the reader cannot open or interpret it.; Fix: "at every review."; Basis: Brief preamble (reader persona)
32. [minor] [style] §6; Current: "(PB1 D3; flag F8)"; Problem: Internal writer flag; the reader cannot open or interpret it.; Fix: "(PB1 D3)"; Basis: Brief preamble (reader persona)
33. [minor] [style] §6 verdict 2; Current: "(PB1 D3; PB3 D2; flag F22)"; Problem: Internal writer flag; the reader cannot open or interpret it.; Fix: "(PB1 D3; PB3 D2)"; Basis: Brief preamble (reader persona)
34. [minor] [style] §6 IR12; Current: "was left for this unit to place (flag F48)."; Problem: Internal writer flag; the reader cannot open or interpret it.; Fix: "was left for this unit to place (PB7 D1 IR12)."; Basis: Brief preamble (reader persona)
35. [minor] [style] §8; Current: "held no hours for (flag F57)."; Problem: Internal writer flag; the reader cannot open or interpret it.; Fix: "held no hours for."; Basis: Brief preamble (reader persona)
36. [minor] [style] §9; Current: "(they did not load for earlier units either; flag F54)"; Problem: Internal writer flag; the reader cannot open or interpret it.; Fix: "(they did not load for earlier units either)"; Basis: Brief preamble (reader persona)
37. [minor] [style] D1 H5; Current: "| Whether taken from a publishing line | Record (flag F57) |"; Problem: Internal writer flag; the reader cannot open or interpret it.; Fix: "| Whether taken from a publishing line | Record |"; Basis: Brief preamble (reader persona)
38. [minor] [style] D1 YT6; Current: "| Own baseline | Record (flag F49) |"; Problem: Internal writer flag; the reader cannot open or interpret it.; Fix: "| Own baseline | Record; Instagram's share copied to IG10 |"; Basis: Brief preamble (reader persona)
39. [minor] [style] D1 IG10; Current: "| A floor | Record (flag F49) |"; Problem: Internal writer flag; the reader cannot open or interpret it.; Fix: "| A floor | Record |"; Basis: Brief preamble (reader persona)
40. [minor] [style] D5 item 7; Current: "**7. Year two's dates (flag F8).**"; Problem: Internal writer flag; the reader cannot open or interpret it.; Fix: "**7. Year two's dates.**"; Basis: Brief preamble (reader persona)
41. [should-fix] [figure] D2 figure (flow); Current: "{"kind": "flow", "title": "The quarterly review in sixty minutes",\n "steps": [\n  {"label": "0–5 Set up", "note": "date; list what qualifies"},\n  {"label": "5–13 Output and hours", "note": "YT1, IG1, H1–H5"},\n  {"label": "13–28 YouTube", "note": "YT2–YT11; R6 choice"},\n  {"label": "28–40 Instagram", "note": "IG2–IG13; IR11, IR12"},\n  {"label": "40–45 Audience and money", "note": "AU1, AU2, R1–R8"},\n  {"label": "45–50 Handed-over items", "note": "HO1, HO3, HO5"},\n  {"label": "50–60 Verdict", "note": "PB1 order; one change per platform"}\n ],\n "caption": "D2: the order and minutes of the review (Mara, fictional; her rule, no source sets the minutes). The blocks follow PB1 D3's verdict order: the inputs the stop and load verdicts read, then the YouTube rows verdict 3 reads, then Instagram's tests (PB7 D1 IR11, IR12), audience (PB3 D1), money (PB9 D5) and the items of §5."}\n"; Problem: The flow puts HO5 at minutes 45–50, but D2 step 6 runs only HO1 and HO3 there, and step 4 already runs IR11 (HO5) at minutes 28–40.; Fix: "{"kind": "flow", "title": "The quarterly review in sixty minutes",\n "steps": [\n  {"label": "0–5 Set up", "note": "date; list what qualifies"},\n  {"label": "5–13 Output and hours", "note": "YT1, IG1, H1–H5"},\n  {"label": "13–28 YouTube", "note": "YT2–YT11; R6 choice"},\n  {"label": "28–40 Instagram", "note": "IG2–IG13; IR11, IR12"},\n  {"label": "40–45 Audience and money", "note": "AU1, AU2, R1–R8"},\n  {"label": "45–50 Handed-over items", "note": "HO1, HO3"},\n  {"label": "50–60 Verdict", "note": "PB1 order; one change per platform"}\n ],\n "caption": "D2: the order and minutes of the review (Mara, fictional; her rule, no source sets the minutes). The blocks follow PB1 D3's verdict order: the inputs the stop and load verdicts read, then the YouTube rows verdict 3 reads, then Instagram's tests (PB7 D1 IR11, IR12), audience (PB3 D1), money (PB9 D5) and the items of §5."}\n"; Basis: Unit D2 steps 4 and 6

## Confirmed

Sources opened live (13 Nov 2026):
- Meta for Developers, Instagram account insights: follower_demographics and follows_and_unfollows are "Not returned if the IG User has less than 100 followers". PASS. https://developers.facebook.com/docs/instagram-platform/api-reference/instagram-user/insights
- YouTube Help 72851: "Qualified watch hours gained from long-form videos that you've set to public"; private, unlisted and deleted videos and Shorts are excluded. PASS. https://support.google.com/youtube/answer/72851?hl=en-GB
- YouTube Help 9101241: thresholds "are not published"; "Not enough demographic data". PASS. https://SUPPORT.GOOGLE.COM/youtube/answer/9101241
- YouTube Help 141805: both quotes exact. PASS. https://support.google.com/youtube/answer/141805?hl=en
- YouTube Help 16559651: changes are "recommended when a video has a lower click-through rate (CTR)" and fewer impressions than usual (D4's packaging reason). PASS. https://support.google.com/youtube/answer/16559651?hl=en
- NIST §7.2.4.1: the normal-approximation formula, and the quote "if the number of failures is very small or if the sample size N is very small". PASS. https://itl.nist.gov/div898/handbook/prc/section2/prc241.htm
- NIST §7.2.4.2: the sample-size formula exists as described (see finding 4 for the choice of null). PASS with a minor finding. https://itl.nist.gov/div898/handbook/prc/section2/prc242.htm
- NIST §1.3.6.6.19: Poisson standard deviation √λ. PASS. https://itl.nist.gov/div898/handbook/eda/section3/eda366j.htm
- NIST §1.3.6.6.18: binomial pmf. PASS. https://itl.nist.gov/div898/handbook/eda/section3/eda366i.htm
- NIST Dataplot sign test: "the test statistic for the sign test follows a binomial distribution with p=0.5". PASS. https://itl.nist.gov/div898/software/dataplot/refman1/auxillar/signtest.htm
- Newman, JAMA 274(13), 4 Oct 1995, 1013. It is a letter, credits Hanley and Lippman-Hand "twelve years ago" (1983), and gives 3/N. PASS. https://jamanetwork.com/journals/jama/article-abstract/389714
- Barnett, van der Pols and Dobson, IJE 34(1), 2005, 215–220: the definition quote is exact. PASS. https://pubmed.ncbi.nlm.nih.gov/15333621/
- Kohavi et al., DMKD 18(1), 2009, 140–181: "the best scientific design for establishing a causal relationship between changes" is exact. PASS. https://exp-platform.com/journal-survey
- TechCrunch, 18 May 2023: "We do not have plans to delete accounts with YouTube videos at this time"; two years of inactivity. PASS ("personal" is not in the source, finding 11).
- PPC Land, 2 Sep 2026: "maybe a 10% or less" is exact. PASS (title, finding 6).

Statistics recomputed (Python):
- Wilson intervals for 3.0% at 250, 500, 1,000, 2,000 and 5,000 impressions: 1.50–5.93, 1.83–4.89, 2.11–4.25, 2.34–3.84, 2.56–3.51. All PASS.
- Skip rate 62% on 100 views: 52.2–70.9. On 400 views: 57.2–66.6. PASS.
- 3/118 = 2.54%, "about 2.5%". PASS. √9 = 3. PASS.
- 0.5^3, 0.5^4, 0.5^5 = 12.5%, 6.25%, 3.1%. Range coverage at n = 5 and 6: 93.75% and 96.9%. Order-statistic intervals: n = 12, 3rd–10th, 96.1%; n = 36, 12th–25th, 97.1%. All PASS.
- Verdict-3 table (1,000 impressions, under 2% meaning 19 clicks or fewer): 87.7/99.7, 46.9/59.7, 13.0/3.3, 2.0/0.02. All PASS.
- PB4 mean (2·6 + 3)/7 = 2.14. PASS. 26.4% and 73.7% one quarter, 6.9% and 54.3% squared. PASS on its 7+7 assumption (finding 12).
- 0.14% × 212 = 0.297. PASS. 100 − 8.65 = 91.35. PASS.
- Mara: Q1 hours sum 77.25, median 6.0, one week over 7 (week 8). Q2 hours sum 80.75, median 6.0, one week over 7 (week 21). Week-by-week hours match the funding rules (week 14 +0.75 −0.25 = 6.5; week 15 5.5; week 18 6.75 from the 1.75-hour guide block). YT2 medians 61 (Q1) and 72 (Q2, uploads 1–10). YT3 median impressions 1,015 and 1,275. Wilson for upload 4 (1.1–2.9), 11 (1.1–2.6) and 13 (0.9–2.8). Verdict-3 count of three. R6 selection (upload 11). IG counts: 39 planned, 35 published, 32 qualifying; Q2 plan 29, published 25, qualifying 24; IR11's 36 and 23. Followers 140 + 72 = 212 and 212 + 106 = 318. Subscribers 23 and 61. Age bands sum to 100 and under-55 is 89%. Traffic-source splits sum to 100. YT8 118/402 = 29%. R5 at 0.06 and 0.19. R1 at 3 × 13.00 = 39.00. V6 pro-rated to 26 days gives 0.25, 1.0 and 3.0. D5 Q2 median 100. Admin 1.75 + 1.0 + 0.5. All PASS except YT9 "May" (finding 13) and the YT5 median (finding 14).
- Dates: every review is a Monday 13 weeks apart (5 Apr, 5 Jul, 4 Oct 2027; 3 Jan, 3 Apr, 3 Jul, 2 Oct 2028; 1 Jan 2029). Every upload is on a Tuesday. Cut windows 11 Apr, 18 Jul and 10 Oct 2027 and 16 Jan 2028 are Sundays of week B. Reply slots of 7, 14 and 16 Apr fall on week B Wednesday and week A Wednesday and Friday. Upload 27 falls on 4 Jan 2028. Year-two upload counts 7/6/7/6. All PASS.

Carried figures checked against filed units (PASS): PB1 Y1 (180, 272, 1,948), Y2, Y3, Y4 (8.65%, 1.86%), Y5 (68%/40, 53.5%/70), Y6 (+0.5/+1.4/+3.7), Y10–Y12, I3 (261), I4 (+0.12%, +0.26%; "points added to the weekly growth rate" exact), I6, I7, B2 (52%, 1,000 US and UK), 42.2%, PB1 D2 7-hour line, the "as corrected" verdict 3; PB4 §1, §4, §5, §6 (week 10), §7 (6.5 h; lost-week rules) and the holiday rule; PB5 §9; PB6 R6, YT5 (100 views, 50% "above typical"), YT8, YT11, YT12, R3, R8; PB7 IG4 65.5% (brand accounts 1,000–5,000), IR11, IR12, IG13/IR8; PB8 clauses 8, 9 and 10 and the five questions (verbatim); PB9 R1–R8 first-read dates, V6 (209 days; 2/8/24), V14 0.62%, net 13.00 a sale, guide windows and launch, brand deals from upload 14; PB2 D5 conventions and the 20-point step; PB3 trait 8/9 sources.

Unverifiable: AIR Media-Tech's "14+ days three or more times a year" finding. Search did not return the AIR page; it rests on PB1 §6's reading, as the unit's unsure list says.

## (3) Figures say whose figure: met

Each carried number names its unit and row. Each derived number is labelled derived. Mara's numbers are labelled. One exception is the PPC Land speaker's title (finding 6).

## (4) Labels: met

Vendor, correlational, survivor, executive-statement-via-press, agency-survey, platform-official and derived labels are present. The new labels "statistical reference" and "her rule" are defined in the opening paragraph. The AIR line lacks PB1's size caveat (finding 1).

## (5) Deliverable

It is present in full. D1 has 41 rows plus 6 HO items; D2 is a timed procedure with a beside-the-hour list; D3 and D4 are full runs with verdicts; D5 is the annual page; T1–T4 are templates whose blanks say what goes in them. It follows from the evidence: verdict 3's count rule is justified by §3's binomial table, and IR12 is kept out of verdict 3 with a reason. It is usable alone, apart from internal flag and notes references (findings 22–40) and the Block E/D2 placement mismatch (findings 17, 41).

## (6) Errata and pointers

No audit report was read, as instructed, so no errata were checked against one. Pointers to filed units say what those units say, with these exceptions: PB5's 40 USD line (finding 15), PB1 D3 on not opening Studio between reviews (finding 16), PB6 §3 on Test & Compare (finding 9), and the PB2 piece scope (findings 18–21). The unit's three corrections to PB1/PB4, PB1/PB7 and PB3 are argued in the body. It never refers to A6 or A9.

## (7) Figures

1. range, §3, "A 3.0% click-through reading": all five labels and ten bounds appear in the §3 table ("| 250 | 1.50% to 5.93% |" and the rest). The caption names §3, NIST §7.2.4.1 and "derived in this unit". Kind fits: competing interval estimates call for a range. PASS.
2. compare, §3, "Chance that 3 or more of 6 uploads read under 2%": 99.7, 59.7 and 3.3 appear in the table ("| 1.5% | 87.7% | 99.7% |" and the rest). 0.0 is explained in the caption ("the last bar is under 0.1% and shows as 0.0"), matching "| 3.0% | 2.0% | under 0.1% |". The caption names §3, PB1 D3 and NIST §1.3.6.6.18. Kind fits: numbers compared call for compare. PASS.
3. matrix, §5, "What each unit hands the review": every cell traces to §5's text ("0.75 hours", "five-minute task", "three minutes", "in the money block", "two Reels fewer", "packaging hour"). The caption names §5 and the source rows. Kind fits: items by sections call for a matrix. PASS.
4. flow, D2, "The quarterly review in sixty minutes": the minutes and notes trace to D2 steps 1–7. The exception is the note "HO1, HO3, HO5" at 45–50: step 6 reads "HO1 ... HO3" only, and IR11 (HO5) is run in step 4. The caption names D2, says no source sets the minutes, and gives the sources of the order. Kind fits: a sequence calls for a flow. FIX (finding 41). Replacement JSON is the old block with "note": "HO1, HO3" at step 6, given in findings.json n 41. It renders with kit-viz.

## (8) Writer's notes

Source errors:
1. PB1 D2 and PB4 D1 G/D2, the review's hour: confirmed. PB1 D2 reads "The quarterly review (60 minutes, PB10) is taken from that fortnight's publishing-and-replies line." (occurs once). PB4's "its hour taken from that fortnight's publishing-and-replies line (PB1, D2)" occurs twice (D1 G and D2 "After week 12"), and the note covers both. Arithmetic: 1.25 = 0.75 replies + 0.5 scheduling (register, PB3 D2 and PB4 D1 E). 60 minutes would take all replies and half the scheduling. Confirmed.
2. Buffer's increment used as a total: confirmed. PB1 D3 reads "and Instagram net followers with the 0.36-a-week illustration (I4)" (once). PB7 IG8 reads "3 posts a week at 140 followers ≈ 0.36 a week (PB1 I4, derived)" (once). PB1 §3 reads "so they are points added to the weekly growth rate", and I4 is measured "against no posts". Confirmed.
3. PB3 D1 trait 8, the dropped API qualifier: confirmed. "Unknown. Instagram returns follower demographics from 100 followers (she has 140)" occurs once. Meta's page confirms the threshold is the API's (live).

Contradictions:
1. Counts after the review's hour moves: arithmetic confirmed (39 − 2 = 37; 37 − 8 = 29; 25 − 2 = 23; 17 − 2 = 15; 31 − 2 = 29). The four cut-window dates are Sundays of week B, confirmed. PB1 read 1's Current occurs once, confirmed. PB7's "39 more posts (25 Reels, 14 carousels" and "31, with 17 Reels," occur once each, confirmed. Not confirmed: the stated "25 and 14 in Q2" does not occur in PB7 (0 occurrences in IR1 or D2). It occurs once in case-facts.md, and there it is followed by "(17 and 14 if PB9's guide build ...)". The proposed replacement "23 and 14 in Q2 (15 and 14 if ...)" would then sit beside the old "(17 and 14 ...)" parenthetical. The register edit must replace "25 and 14 in Q2 (17 and 14" as a whole.
2. PB4 §1 rule: the Current occurs once, confirmed. 2.14, 7% and 54% are confirmed on the 7+7 assumption. The proposed replacement contains "..." and so is not an exact replacement text: not confirmed as applicable verbatim.
3. PB6 R6 and the 100-view Intro: confirmed (PB6 YT5: key moments need "at least 100 views"). No replacement proposed.
4. PB2 run 2 had no hours: confirmed. PB4's calendar has no line for it, and PB2 places it at the Q1 review. No replacement.
5. IR12: no contradiction. PB7 IR12 says the flag "is reported to PB10's review beside PB1's verdict 3", which matches the unit. Confirmed.

## (9) Part 5, line by line

1. Claims with a number, mechanism or recommendation sourced where made: met, except findings 3, 5 and 9 (stretches) and finding 1 (the break rule's reasoning).
2. Source types: met in substance. The NIST handbook, a JAMA letter and TechCrunch fall outside the four named types; each is labelled ("statistical reference", "published letter", "platform statement via the press").
3. Anecdote, vendor and correlational data labelled: met (§4 table, §5 AIR, §8 B2).
4. Platform named for growth, format and metric claims: met (§2, §3 split by YouTube and Instagram; D1 by block).
5. Carry-over re-verified: met. Nothing rests on A6 or A9; the carried numbers are cited through PB1, PB6 and PB7 rows. AIR was not re-opened (unsure list).
6. No private-course reader or units: met (no A-unit or private-reader reference found). kit/private_terms.py is not in this folder and was not run.
7. Mara labelled on first use ("Mara Venn (Mara, fictional)", §intro and Deliverable) and consistent with case-facts: mostly met. Exceptions are the pieces outside PB2's scope (findings 18–21) and internal inconsistencies (13, 14). She is never used as evidence, and her benchmarks are sourced.
8. Neutral ground on tax and law: met. No rates are given; T1 is hers; CTT is not priced; §9 states no rule it did not open.
9. No uncited figures or invented names: met (channel names in AU2 deliberately not given).
10. Changeable facts dated: met (each platform page "checked 13 Nov 2026").
11. Deliverable for Mara, then template with described blanks: met.
12. Reads as advice without evidence: no. Rules marked "her rule" are conventions rested on §3's statistics.
13. Links as links: met. YouTube Help 16559651 in D4 is cited by number only, via PB1.

## (10) Read as the brief's reader

- Sixteen "flag Fnn" references (§1, §5, §6, §8, §9, D1, D5) are internal writer flags with no meaning to a reader (findings 25–40).
- "The correction is in the notes to PB1 and PB7", "listed in the notes", "proposed to PB4 in the notes" and "the register" (§4, §5) point to the writer's notes and the internal case-facts register, which the reader cannot open (findings 22–24).
- The front matter says "search: off" while the first paragraph says search was used. That is a minor oddity, explained in the text.
- Otherwise the private references are this course's own (PB rows, PB8 register lines J1, M1, A3 and T3, PB9 V-rows), which a reader who has done PB1–PB9 knows.

PB10 · verdict fix · error 0, should-fix 8, minor 33
