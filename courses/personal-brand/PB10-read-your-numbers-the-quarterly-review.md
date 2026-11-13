---
code: PB10
title: Read your numbers: the quarterly review
course: personal-brand · PB · Building a Personal Brand on Instagram and YouTube
model: Opus 5.5
written: 2026-11-13
search: off
---

# Read your numbers: the quarterly review

Search was off for this unit. It was used on 13 November 2026 only to re-open at its source each platform rule and statistical method this unit states as fact; each carries that date. Benchmarks carried from earlier units are cited by unit and row (PB1 D1 Y1, PB6 D2 YT3) and rest on those units' sourced lines. The labels are PB1 §1's (platform-official, vendor, correlational, survivor sample, peer-reviewed, derived), plus two: **statistical reference**, a method as a government statistics handbook states it, and **her rule**, a convention Mara sets that no source sets.

The running example is Mara Venn (Mara, fictional): 38, a full-time accountant who restores mid-century furniture at weekends and teaches it to people with no workshop, as One Box Restoration. She started on Monday 4 January 2027 with no YouTube subscribers and 140 Instagram followers, films on a phone, and has 6 hours a week: one 10-minute video a fortnight and three Instagram posts a week (PB1, PB4). Her numbers below are invented to show the procedure working; they are evidence about nothing.

## 1 · The metrics sheet: PB6's and PB7's rows in one place

PB6 set twelve YouTube rows (YT1–YT12) and PB7 thirteen Instagram rows (IG1–IG13); PB1 set seven reads and four verdicts; PB9 set eight revenue rows (R1–R8). Read as written, that is forty-odd numbers, several of them the same number reached by two routes. The sheet in the deliverable (D1) puts them in the order the review needs them, which is the order of the verdicts: first what was produced and what it cost in hours, because the stop rule and the load verdict read those; then the per-upload YouTube rows, because the format verdict reads them; then Instagram; then audience, money and the items other units hand over.

Three rules shape the sheet.

**One reading, written in two places.** PB6's YT6 (traffic sources) and PB7's IG10 (YouTube views from Instagram) both read YouTube Studio's External card. It is opened once, in the YouTube block, and the Instagram share is copied into IG10. PB9's R3 (watch hours and subscribers against the programme thresholds) is YT10 and YT9 read again; it is not read again, the R3 line points to them.

**A row says what qualifies on the day.** A 30-day view count needs an upload at least 30 days old (PB6 D2 YT2); click-through and percentage viewed need 7 days (YT3, YT4); an Instagram post is read once it is 7 days old (PB7 D2). Each review starts by listing which uploads and posts qualify, so that a number is never compared with a number of a different age.

**Every row says what it decides, or that it decides nothing.** Of the YouTube rows, only YT1 (uploads), YT3 and YT4 (click-through, percentage viewed) enter a verdict (PB1 D3); on Instagram, IG2 and IG4–IG5 enter the two Instagram tests PB7 set (IR11, IR12). Everything else is recorded for direction against her own earlier quarters, because no sourced benchmark exists for it at her size (PB6 D2, PB7 D2, "What the rows do not tell her"). Writing "decides nothing" on a row is what stops a weak number from being acted on.

## 2 · Numbers that lead and numbers that lag

Some numbers describe each piece; others are running totals that sum every piece so far. The first kind moves first.

**Lagging: stocks.** Subscribers, followers, watch hours in the last 365 days, the email list and income are sums of past reach. YouTube counts qualified watch hours only from "long-form videos that you've set to public", and not from private, unlisted or deleted videos or from Shorts ([YouTube Help, YouTube Partner Programme overview and eligibility, answer 72851](https://support.google.com/youtube/answer/72851?hl=en-GB), checked 13 Nov 2026; platform-official), so the 365-day total is built upload by upload from views and their duration. A subscriber count moves after the videos that earned it, and subscribers do little to deliver the next one: YouTube's senior director of growth and discovery, Todd Beaupré, put subscribers' click-through on a creator's videos at "maybe a 10% or less" (PB1 §2, via PPC Land, 2 Sep 2026; executive statement via the press, no sample). PB1 therefore keeps every count out of the year-one verdicts (PB1 D3).

**Leading: per piece.** Impressions, click-through rate, percentage viewed and the Intro on YouTube; views split into followers and non-followers, skip rate, watch time and sends on Instagram. These change with the next upload. They are what PB1's verdict 3 and PB7's IR11 and IR12 read.

**Leading: inputs.** Uploads published and hours logged lead everything else, and they are the only numbers wholly in your control. PB1's stop rule reads uploads and its load verdict reads hours; neither waits for an audience.

Reading in that order has a practical point: a quarter in which the inputs held and the per-piece numbers moved is a quarter that worked, whatever the stocks did. At Mara's size the stocks barely move. PB1's band medians put a YouTube channel of 1–99 subscribers at +0.5 a month and one of 100–499 at +1.4 (PB1 D1 Y6; vendor, medians), and no Instagram dataset gives a follower timeline from under 1,000 (PB1 D1 I7). A stock that moves by a handful a month is mostly noise at quarterly scale, which §3 shows.

## 3 · Small numbers: how many posts a rate needs before it means anything

Every rate on the sheet is a count divided by a count: clicks over impressions, skips over views, sends over accounts reached. When the denominator is small, the rate moves by large steps for no reason, and a review that reacts to that movement changes things at random.

**One rate, one post.** For a proportion p observed on n trials, the usual 95% interval is p ± 1.96·√(p(1−p)/n), and the handbook also gives the Wilson interval, whose worth "does not strongly depend upon the value of n and/or p" ([NIST/SEMATECH e-Handbook of Statistical Methods, §7.2.4.1, Confidence intervals](https://itl.nist.gov/div898/handbook/prc/section2/prc241.htm); statistical reference). The handbook warns that limits based on the normal approximation may not be accurate enough "if the number of failures is very small or if the sample size N is very small". Treating impressions as independent trials is an assumption: a viewer shown the same thumbnail twice is not two independent chances. On that assumption, a click-through rate of 3% has these 95% Wilson intervals (derived):

| Impressions | 95% interval for a 3.0% reading |
|---|---|
| 250 | 1.50% to 5.93% |
| 500 | 1.83% to 4.89% |
| 1,000 | 2.11% to 4.25% |
| 2,000 | 2.34% to 3.84% |
| 5,000 | 2.56% to 3.51% |

```viz
{"kind": "range", "unit": "%", "min": 0, "max": 7, "ticks": [0, 1, 2, 3, 4, 5, 6, 7], "decimals": 2,
 "title": "A 3.0% click-through reading: 95% interval by number of impressions",
 "rows": [
  {"label": "250 impressions", "low": 1.50, "high": 5.93, "point": 3.0, "low_src": "Wilson", "high_src": "Wilson", "tone": 2},
  {"label": "500 impressions", "low": 1.83, "high": 4.89, "point": 3.0, "low_src": "Wilson", "high_src": "Wilson", "tone": 2},
  {"label": "1,000 impressions", "low": 2.11, "high": 4.25, "point": 3.0, "low_src": "Wilson", "high_src": "Wilson", "tone": 3},
  {"label": "2,000 impressions", "low": 2.34, "high": 3.84, "point": 3.0, "low_src": "Wilson", "high_src": "Wilson", "tone": 3},
  {"label": "5,000 impressions", "low": 2.56, "high": 3.51, "point": 3.0, "low_src": "Wilson", "high_src": "Wilson", "tone": 4}
 ],
 "caption": "§3: the table above drawn. Wilson 95% interval for an observed 3.0% click-through rate, impressions treated as independent trials (an assumption). Formula from the NIST/SEMATECH e-Handbook of Statistical Methods, §7.2.4.1; the intervals are derived in this unit. The tones only tell the rows apart."}
```

The same arithmetic, turned round, says how many impressions a single upload needs before its rate can be told apart from a line. The handbook's sample-size formula for a test of a proportion ([NIST/SEMATECH e-Handbook, §7.2.4.2, Sample sizes required](https://itl.nist.gov/div898/handbook/prc/section2/prc242.htm); statistical reference) gives about 2,045 impressions to tell a true 2% from a hypothesised 3% at the usual 5% significance (two-sided) and 80% power, or about 1,747 with 2% as the hypothesis (derived: z values 1.960 and 0.842; the handbook's continuity correction adds 100 to each). In Mara's first two quarters only two of thirteen uploads passed 2,000 impressions (D3, D4; her numbers). A single upload's click-through rate, at her size, does not say on which side of 2% her channel sits.

The same holds on Instagram. A skip rate of 62% read on 100 views has a 95% interval of 52.2% to 70.9%; on 400 views, 57.2% to 66.6% (derived, Wilson). PB7's IR12 line is 65.5%, so a single Reel with a few hundred views cannot be placed above or below it.

**When the count is zero.** Most of a small account's posts get no sends. If no event occurs in n trials, the upper end of the 95% interval for its rate is about 3/n, a rule a 1995 letter in JAMA credits to Hanley and Lippman-Hand ([Newman, "If almost nothing goes wrong, is almost everything all right?", *JAMA* 274(13), 1995, 1013](https://jamanetwork.com/journals/jama/article-abstract/389714); published letter). A carousel that reached 118 accounts with no sends has a true send rate somewhere between 0 and about 2.5% (derived: 3 ÷ 118). A zero on a small sample says little about whether anyone shares her posts.

**Counts per month.** Subscribers or followers gained in a month are a count of events in a time interval, which the NIST handbook says the Poisson distribution "is used to model", with a standard deviation equal to the square root of the mean; reading a net count (gains less losses) the same way is an assumption ([NIST/SEMATECH e-Handbook, §1.3.6.6.19, Poisson distribution](https://itl.nist.gov/div898/handbook/eda/section3/eda366j.htm); statistical reference; PB9 §8 used the same model for sales). At an expected 9 a month the standard deviation is 3 (derived), so a month of 6 and a month of 12 can come from the same channel doing the same thing.

**Many posts, one direction.** The rules that decide anything therefore read several pieces together, and the arithmetic for that is the binomial. If a line sits exactly at a channel's true median, each piece falls above or below it with probability one half, which is the sign test's assumption ([NIST Dataplot reference, Sign test](https://itl.nist.gov/div898/software/dataplot/refman1/auxillar/signtest.htm): "the test statistic for the sign test follows a binomial distribution with p=0.5"; binomial formula in the [NIST/SEMATECH e-Handbook, §1.3.6.6.18](https://itl.nist.gov/div898/handbook/eda/section3/eda366i.htm); statistical reference). The chance that every one of n pieces falls on the same named side is 0.5^n: 12.5% for three, 6.25% for four, 3.1% for five (derived). Five pieces is the smallest number for which "all on one side" happens by chance less than one time in twenty.

The same arithmetic bounds a median. The true median lies outside the range from the smallest to the largest of n readings only if all n fall on one side of it, so that range covers it with probability 1 − 2 × 0.5^n: 93.75% for five readings, 96.9% for six (derived). A median of six uploads is pinned down only to "somewhere between the worst and the best of them". For twelve readings the 95% interval runs from the 3rd to the 10th smallest (96.1% coverage), and for 36 from the 12th to the 25th (97.1%) (derived from the binomial). Medians of a quarter's Reels, or of two quarters' posts, start to mean something; medians of one quarter's six or seven videos are wide.

**What this does to PB1's format verdict.** Verdict 3 counts uploads under 2% click-through (with impressions at or below her median) and fires on three or more of the quarter's uploads (PB1 D3). Each upload alone is too small to judge, as above. Counting them is what gives the rule its meaning. Assume six uploads of 1,000 impressions each; the chance that three or more read under 2% is (derived, exact binomial):

| Her channel's true click-through rate | Chance one upload reads under 2% | Chance 3 or more of 6 read under 2% |
|---|---|---|
| 1.5% | 87.7% | 99.7% |
| 2.0% | 46.9% | 59.7% |
| 2.5% | 13.0% | 3.3% |
| 3.0% | 2.0% | under 0.1% |

```viz
{"kind": "compare", "title": "Chance that 3 or more of 6 uploads read under 2% click-through, by the channel's true rate", "unit": "%", "max": 100, "decimals": 1,
 "rows": [
  {"label": "True rate 1.5%", "value": 99.7, "tone": 1},
  {"label": "True rate 2.0%", "value": 59.7, "tone": 2},
  {"label": "True rate 2.5%", "value": 3.3, "tone": 3},
  {"label": "True rate 3.0%", "value": 0.0, "tone": 4}
 ],
 "caption": "§3: the table above drawn; the last bar is under 0.1% and shows as 0.0. Six uploads of 1,000 impressions each; each upload's clicks binomial at the true rate; the rule is PB1 D3 verdict 3's count of three or more. Derived in this unit from the binomial distribution (NIST/SEMATECH e-Handbook, §1.3.6.6.18); impressions treated as independent trials, an assumption. The tones only tell the rows apart."}
```

So the rule almost never fires on a channel running at 2.5% or better, fires more often than not at 2%, and almost always fires at 1.5%: it separates channels near or under 2% from those clearly above it. That is all it can do, and it is what it was built for. A verdict reached this way says "her click-through is probably at or under about 2%", and never "upload 11 failed".

**Her rule, for every rate on the sheet.**

1. A single upload's or post's rate is written down and never acted on alone.
2. A claim about a format or a quarter rests on at least five pieces read together, or on PB1's three-of-the-quarter count.
3. A median is quoted with how many pieces it rests on.
4. A count per month is read against the square root of itself before it is called a rise or a fall.
5. Where a rule compares two groups (PB7's IR11), each group has at least five pieces, and the result is read as a direction, since the medians of small groups overlap.

## 4 · Setting the quarter against PB1's expectation sheet

PB1's expectation sheet (D1) is the benchmark side of the review. Each row of it has one place on the metrics sheet and one use:

| PB1 row | What it gives | Where the review reads it | Use |
|---|---|---|---|
| Y1 | 30-day views of uploads 1–10: median about 180 (upload 1) to 272 (upload 10); median best of the ten 1,948 (vendor; survivor sample) | YT2 | Q2 review: median of uploads 1–10 against 180–272, expecting to sit at or below, since the cohort posted faster and excludes quitters |
| Y2 | Half of channels and videos between 2% and 10% click-through (platform-official) | YT3 | Verdict 3, from Q2 |
| Y3 | 40–55% viewed for 5–15 minute videos (vendor heuristic, no sample) | YT4 | Verdict 3, from Q2 |
| Y4 | 8.65% of channels adding 12–51 videos crossed 1,000 within 360 days (vendor; correlational) | YT1 | The stop rule's floor of 3 a quarter keeps her in this band |
| Y5 | 68% of channels that crossed 1,000 had 40 or more videos (vendor; survivors) | YT1, upload count | Why no count is a stop ground before 24 months |
| Y6 | Median +0.5, +1.4, +3.7 subscribers a month by band (vendor; medians) | YT9 | Context from Q3; read against §3's Poisson spread |
| Y10, Y11 | 8,000 and 3,000 watch hours with 1,000 and 500 subscribers (platform-official) | YT10, R3 | Recorded each quarter |
| Y12, I5 | Live at 50 subscribers; Instagram Live at 1,000 followers | YT9, IG8 | Milestones only |
| I3 | Median reach 261 accounts a post, all sizes pooled (vendor) | IG3 | Context only |
| I4 | +0.26% weekly follower growth at 3–5 posts against weeks with none (vendor; within-account) | IG1 | Posting rate only; see below |
| I6 | No published follower threshold for Instagram's earning tools (platform-official, by absence) | R4 | What the dashboard shows |
| B1, B2 | Hours creators report; burnout | Hours block | Why hours are read every quarter |

Rows Y7, Y8, Y9, I1, I2 and I7 do not enter the review: Y7 applies only above 1,000 subscribers, Y8 is context with an undefined window and I2 context with an undefined growth measure, I1's sample starts at 1,000 followers, and Y9 and I7 have no source (PB1 D1).

**One row is misread downstream.** PB1's Q3 instruction compares Instagram net followers "with the 0.36-a-week illustration (I4)", and PB7's IG8 sets the same figure as a reference. Buffer's estimate is the difference between an account's weekly growth rate in weeks with 3–5 posts and in weeks with no posts (PB1 §3: "points added to the weekly growth rate"). It is an increment attributable to posting, and an account's total weekly growth also includes what it gains in weeks without posts. Comparing her total net followers with it compares two different quantities. In this review I4 places her posting rate in Buffer's band (IG1); net followers (IG8) are recorded with no benchmark. Read PB1 D3's Q3 line and PB7's IG8 reference column this way.

## 5 · What the other units hand the review, and where each sits

PB1's seven reads are the core. Seven units hand the review something more. Each item below is placed **inside** the sixty minutes, because it is a reading or a short decision made from the sheet, or **beside** them, because it needs other people, a delay or a writing task. The hours of everything beside are found inside the 6-hour week.

**Where the sixty minutes themselves come from.** PB1 took the review's hour from "that fortnight's publishing-and-replies line" (PB1 D2), and PB4 repeated it (PB4 D1 G). That line was 1.5 hours a fortnight when PB1 wrote it. PB3 cut it to 1.25 and gave 0.25 to email, and PB4 then split it into three 15-minute reply slots (0.75) and 0.5 hours of scheduling inside the cut window (PB4 D1 E). Taking 60 minutes from it would remove all three reply slots and half the scheduling, and scheduling cannot be skipped. The hour is therefore taken where PB9 took the guide's hours: from the Instagram derivatives of the fortnight that holds the review. That fortnight's cut window makes four posts in place of six, two Reels fewer (her rule; PB9 D1 uses the same trade; PB3 D2 puts Instagram first in the cut order). At her rate of three posts a week, two weeks a quarter fall to two posts. Buffer's within-account estimates put a week of 1–2 posts at +0.12% weekly growth against +0.26% at 3–5 (PB1 D1 I4; vendor), a difference of about 0.3 followers a week at 212 followers (derived: 0.14% × 212). The cost is small; each review takes two Reels from the quarter after it, so Q2, Q3 and Q4 each plan 37 posts in place of 39, and Q2 plans 29 if the guide is built (derived).

**PB2: the repeat-back test, run 2 (Q1 review only; beside).** Five strangers watch one complete video, wait at least ten minutes, and say in one sentence what the account is and who it is for; the pass mark is four of five naming both who and what (PB2 D5). The five people, the delay and the pass mark are this course's conventions; no source validates them, and with five people one answer moves the result by 20 points (PB2 §3). It needs other people and a delay, so it sits beside the hour. Its time is Mara's estimate, 0.75 hours (her estimate, no source), taken from the three reply slots of the review fortnight; replies wait for the next slots, which is PB3's second cut. Its scored sheet is filed with the review.

**PB3: audience traits 8 and 9 (every review; inside).** Trait 8 is her audience's age, gender and country; trait 9 is what else it watches (PB3 D1). On Instagram, Meta's developer reference says follower demographics are "Not returned if the IG User has less than 100 followers", and follows and unfollows likewise ([Meta for Developers, Instagram account insights](https://developers.facebook.com/docs/instagram-platform/api-reference/instagram-user/insights), checked 13 Nov 2026; platform-official). That is the API's threshold; whether the app's own Insights screen uses the same one was not checked. On YouTube, the Audience tab shows demographics only above thresholds that "are not published" and can show "Not enough demographic data" ([YouTube Help, Understand limited data in YouTube Analytics, answer 9101241](https://SUPPORT.GOOGLE.COM/youtube/answer/9101241), checked 13 Nov 2026; platform-official). Both are readings, taken in the audience block in under five minutes. Each trait replaces PB3's outside evidence only where her own data shows something.

**PB4: three items.**

1. *The pick of the next season's remaining pieces (every review; inside, five minutes).* The next season's first two pieces are already on the table, picked by week 10 (PB4 §6). The rest are picked from the backlog by PB4's rule: only pieces she estimates at two weekends unless a bank exists (PB4 §1). A pick from a list with estimates already written is a five-minute task.
2. *Whether a break between seasons enters year two (the twelve-month review; inside the annual page, which sits beside).* PB4 left it to this unit because the evidence disagrees. YouTube says "We studied thousands of channels that took a break and found no correlation between break length and changes in views", and that "growth in views across uploads is not correlated with time between uploads" ([YouTube Help, YouTube performance FAQ, answer 141805](https://support.google.com/youtube/answer/141805?hl=en), checked 13 Nov 2026; platform-official; no sample size, period or method given). AIR Media-Tech's vendor data associates going dark for 14 or more days three or more times a year with fewer views per video (PB1 §6; vendor, correlational). The rule in D5 allows at most two breaks a year, each one fortnight with no upload. At her cadence uploads are 14 days apart, with 13 days between them carrying no upload, so AIR's line sits one day past her normal rhythm: a break leaves 27 days with no upload, and an upload moved 7 days under PB4 §7 leaves 20, so moved uploads count towards the same three. AIR's main analysis covers channels with 100,000 to 1,000,000 monthly views, far larger than hers (PB1 §6). Two breaks leave 24 uploads a year, which still passes PB1's twelve-month cadence test of 24 and stays in the 12–51 band of row Y4.
3. *The log of weekends per piece, edit-window overruns and 6.5-hour recovery weeks, read against PB1's 7-hour line (every review; inside, in the hours block).* PB4 built the log and said when each entry arises (PB4 §1, §7). The review counts them. One of PB4's rules reads badly at small numbers: "If her log shows pieces averaging more than two weekends", she moves to one video every four weeks at a checkpoint (PB4 §1). Weekends are whole numbers and almost every piece is estimated at two, so one three-weekend piece in seven raises the mean to 2.14 (derived) and triggers a halving of her cadence. The rule as read here: the move is made when two or more pieces in a quarter took more than two weekends, in two consecutive quarters (her rule, built on PB1's two-quarter stop rule). If her true rate of overrunning pieces were one in seven, that happens about 7% of the time by chance; at one in three, about 54% (derived, binomial, seven pieces a quarter: 26.4% and 73.7% for one quarter, squared; with a six-piece and a seven-piece quarter, about 5% and 48%). This unit reads PB4's rule this way from here on. (Correction 2026-11-13, P108: PB4 §1 was corrected the same day and now states the rule as it is read here; the words quoted above are its earlier wording.)

**PB6: the packaging check R6 (from the Q2 review; inside for the choice, beside for the change).** At most one upload at least 28 days old, with the quarter's lowest click-through, impressions below her median and Intro at or above her median, gets one new thumbnail or one new title, made in the next cut window's packaging hour (PB6 D1 R6). The choice takes two minutes in the YouTube block; the change is already inside the packaging hour PB6 gave it. An upload whose Intro Studio does not show (under 100 views) cannot qualify.

**PB7: the format test IR11 (Q2 only) and the format flag IR12 (from Q2); inside.** Both are medians read in the Instagram block. How IR12 relates to PB1's verdict 3 is set in §6.

**PB8: the policy re-read (every review; inside, three minutes).** PB8's clause 10 sets the disclosure policy to be re-read at each checkpoint, with five one-line questions from its pre-mortem: did any title or thumbnail lead with a mistake or a mood; did anything personal go out less than ten days after its session; is every correction visible where the error was; did any product appear that someone gave her; did anyone appear who has not agreed in writing (PB8 D1 clause 10, D2). The register (PB8 D3) is re-read with it, and its run-in tasks enter the hours log under an admin line (§8).

**PB9: the revenue rows R1–R8 (every review; inside).** Each row has a first-read date (PB9 D5). They sit in the money block. At the Q1 review PB9 adds one decision: whether to build the guide, which depends on her tax line T1 having been answered by a professional (PB9 D1). D4's start rule is applied again to every line at every review.

```viz
{"kind": "matrix", "title": "What each unit hands the review, and where it sits",
 "cols": ["Inside the 60 minutes", "Beside them", "When", "Hours from"],
 "rows": [
  {"label": "PB1 seven reads", "tone": 4, "cells": [{"mark": "all", "tone": 3}, null, "every review", "two Reels fewer"]},
  {"label": "PB2 repeat-back test", "tone": 4, "cells": [null, {"mark": "0.75 h", "tone": 5}, "Q1 only", "three reply slots"]},
  {"label": "PB3 traits 8 and 9", "tone": 4, "cells": [{"mark": "audience block", "tone": 3}, null, "every review", "inside"]},
  {"label": "PB4 next season's pieces", "tone": 4, "cells": [{"mark": "5 min", "tone": 3}, null, "every review", "inside"]},
  {"label": "PB4 break between seasons", "tone": 4, "cells": [null, {"mark": "annual page", "tone": 5}, "twelve months", "three reply slots"]},
  {"label": "PB4 log of pieces and overruns", "tone": 4, "cells": [{"mark": "hours block", "tone": 3}, null, "every review", "inside"]},
  {"label": "PB6 packaging check R6", "tone": 4, "cells": [{"mark": "choice", "tone": 3}, {"mark": "change", "tone": 5}, "from Q2", "packaging hour"]},
  {"label": "PB7 IR11 and IR12", "tone": 4, "cells": [{"mark": "Instagram block", "tone": 3}, null, "from Q2", "inside"]},
  {"label": "PB8 policy and register", "tone": 4, "cells": [{"mark": "3 min", "tone": 3}, null, "every review", "inside"]},
  {"label": "PB9 revenue rows", "tone": 4, "cells": [{"mark": "money block", "tone": 3}, null, "every review", "inside"]}
 ],
 "caption": "§5: where each item handed to the review sits, and where its hours come from (Mara, fictional; her rules). The review's own hour comes from two Reels fewer in the review fortnight's cut window; items beside it come from that fortnight's reply slots or, for R6, from the packaging hour PB6 gave it. Items from PB1 D3, PB2 D5, PB3 D1, PB4 §1 and §6, PB6 D1 R6, PB7 D1, PB8 D1 clause 10 and PB9 D5."}
```

## 6 · The verdicts, and what counts as evidence for each

A review ends in one of four verdicts, read in PB1's order; the first that applies is the verdict (PB1 D3). The evidence for each is fixed in advance, so that a bad week is not where the decision is made.

**1. Stop, or rebuild before the next upload.** Evidence: fewer than 3 YouTube uploads in this quarter and the one before. Three a quarter is 12 a year, the floor of the 12–51 band; below it the base rate is 1.86% (PB1 D1 Y4; vendor, correlational). No subscriber or follower count is evidence for this verdict in year one, and from the 24-month review only under the rule in D5. She may also stop at any review because she judges the hours worth more elsewhere; that decision needs no threshold and is recorded with the day's numbers (PB1 D3).

**2. Change one thing.** PB1's form of it is cutting the load: over 7 hours in 3 or more weeks of the quarter. At quarterly scale the cut follows the order PB1 and PB3 share: first the Instagram derivatives, six a fortnight down to four for the next season; if the next quarter still shows three weeks over 7, the video goes to about 8 minutes; the cadence is never the cut (PB1 D3; PB3 D2). PB3's weekly steps of deferring replies and moving a date have no seasonal form: a season of deferred replies is a season without replies, and a season of moved dates is a lower cadence, which only verdict 1 or PB4's cadence move (§5) may set. Other single changes also count as this verdict when their own evidence fires: PB7's IR11 (carousels' median non-follower views equal or beat Reels' across Q1 and Q2), PB7's IR12, PB4's cadence move under the rule in §5, and a profile line after a failed repeat-back test (PB2 D5).

**3. Change the format.** Evidence: from Q2, three or more of the quarter's uploads with click-through under 2% and impressions at or below her median, or percentage viewed under its band; an upload under 2% with impressions above her median is recorded and not counted (PB1 D3, as corrected; rows Y2, Y3). §3 shows what the count means: it separates a channel near or under 2% from one clearly above. The change is structure, length or packaging, one of them, and takes effect at the first video edited after the review, the season's second (PB4 §4).

**IR12 and verdict 3.** PB7's Instagram format flag (Reels' median skip rate above 65.5% and median watch-time share below her Q1 median) was left for this unit to place (PB7 D1 IR12). It does not join verdict 3. Its skip-rate line is an average for brand accounts of 1,000–5,000 followers (PB7 D2 IG4; vendor), a population she is not in; verdict 3 reads the anchor platform, whose two numbers YouTube itself documents. IR12 is read after the verdict, and acts as that review's Instagram change only if no other change on Instagram was made at the same review.

**4. Continue.** Evidence: none of the above, whatever the counts.

## 7 · One change at a time

Randomised controlled experiments are "the best scientific design for establishing a causal relationship between changes" and their effect ([Kohavi, Longbotham, Sommerfield and Henne, "Controlled experiments on the web: survey and practical guide", *Data Mining and Knowledge Discovery* 18(1), 2009, 140–181](https://exp-platform.com/journal-survey); peer-reviewed). A creator with one channel cannot randomise: YouTube's own Test & Compare is computer-only and may return "Not enough impressions" or "Inconclusive", the likely result at a small channel's views (PB6 §3, inference), and Mara works on a phone (PB6 §3). What remains is a before-and-after comparison on one channel. It has three weaknesses, and the review's rules answer each.

**Other things change at the same time.** The season, the pieces, the topic's popularity and the platform all move between quarters. Two changes made together cannot be separated afterwards. Her rule: at most one change per platform per review, and a cut-the-load change counts as the change on the platform it cuts. She treats the platforms separately because no source measures how one affects the other (PB3 §4; PB7 §9).

**Changes follow bad quarters, and bad quarters are followed by better ones anyway.** Regression to the mean "happens when unusually large or small measurements tend to be followed by measurements that are closer to the mean" ([Barnett, van der Pols and Dobson, "Regression to the mean: what it is and how to deal with it", *International Journal of Epidemiology* 34(1), 2005, 215–220](https://pubmed.ncbi.nlm.nih.gov/15333621/); peer-reviewed). A change made because a quarter was poor will look as if it worked even if it did nothing. Her rule: a change is judged on the full season after it (six or seven uploads), against the season before, and the record says "before and after, one channel, no control".

**The effect will be small next to the noise.** §3 shows that one quarter's six uploads pin a median down only loosely. Her rule: a change stays in place for at least one full season before it is judged, and is reversed only by the same evidence that would have triggered it.

## 8 · Hours spent against the budget

The hours log is read before any audience number, because the stop rule and the load verdict depend on it and because burnout is the strain creators report most (PB1 §6, row B2: of 1,000 US and UK creators surveyed, 52% reported burnout and 37% were considering leaving; agency survey, self-report). The block reads, from PB1 D2 and PB4's log:

- **Hours per week against 6, and weeks over 7.** A week at 7.0 is at the line, not over it (PB1 D2). Three weeks over 7 in a quarter is verdict 2.
- **Recovery weeks.** PB4's lost-week rules plan 6.5 hours, under the line (PB4 §7). Each is counted with its logged total, since a recovery week that runs over 7 is where the line is crossed.
- **Edit-window overruns.** An edit not exported at the 4-hour stop (PB4 §5). PB5 adds that after three in a row the video goes to about 8 minutes from the next checkpoint (PB5 §9).
- **Weekends per piece**, under the rule in §5.
- **Admin.** PB8's register set tasks with dates (contract read by Sun 29 Nov 2026, trademark search by Sun 6 Dec 2026, sign-up notice by Sun 31 Jan 2027) that PB4's run-in held no hours for. They are logged on a line of their own, with the week they fell in, so that the review can see whether they were taken from a publishing line, added on top, or fell in a week with no plan.
- **Hours on income lines** (PB9 R7) and the line they were taken from.
- **The quarter's total against 78.0** (13 weeks at 6.0), and the median week.

No dataset gives hours per video or per post for one-person accounts (PB1 §8); her logged hours are the only number for her. Read across quarters, they replace PB1's planning figures line by line.

## 9 · Pausing or stopping without deleting the record

A pause or a stop is a verdict like the others, and the record it leaves is part of the account.

**Say it.** PB8's clause 9 sets how: within the week it is decided, one plain paragraph in the next scheduled slot on each platform and in the email; a stop under PB1's rule is recorded with its reason and the numbers at the time (PB8 D1 clause 9).

**Keep the videos public.** Watch hours count toward YouTube's thresholds only from public long-form videos, and not from private, unlisted or deleted ones (answer 72851, above). A paused channel whose videos stay public keeps accruing qualified hours; unlisting them removes those hours. The total is a rolling 365 days (PB1 §4), so hours from before a long pause fall out of it in time whatever she does.

**Keep the account alive.** In 2023 Google said it would delete Google accounts inactive for two years, and that "We do not have plans to delete accounts with YouTube videos at this time" ([TechCrunch, 18 May 2023](https://techcrunch.com/2023/05/18/youtube-will-no-longer-be-deleting-videos-from-inactive-accounts); platform statement via the press). "At this time" is a 2023 statement. Her rule: she signs in during any pause; what Google counts as activity is set on its policy page, which was not opened for this unit. If she is ever in the Partner Programme, PB1 §4 lists its separate activity rule from 1 February 2027.

**On Instagram, change nothing.** Instagram's Help Centre pages on deactivating and deleting an account were not opened for this unit (they did not load for earlier units either), so it states no rule about them. Her rule: the account stays public, no post is archived or deleted, and the pause is announced in a post.

**Keep the working record.** The metrics sheet, the hours log, the voice notes and every review page are kept. Nothing is deleted except under PB8's clause 8 (privacy, safety, a legal demand).

**How long a pause can be.** The stop rule counts uploads per quarter. A quarter with fewer than 3 uploads, followed by another, fires verdict 1 (PB1 D3). A pause of up to one quarter therefore leaves her inside the rule; a second paused quarter is a stop or a rebuild, decided at that review in writing.

## Deliverable

Built 13 November 2026 for Mara Venn (Mara, fictional). Every number in D3 to D5 that is not cited is hers, invented to show the procedure, and labelled (Mara, fictional) on first use; she is not evidence about anyone. **(her rule)** marks a decision no source sets.

### D1 · The metrics sheet

One sheet, read on PB1's dates in the order of D2. "Qualifies" is counted from the review date. "Decides" names the verdict or test a row feeds; "record" means it is written down and read for direction only.

**Block A · Output and hours (D2 minutes 5–13)**

| # | Metric | Read from | Qualifies | Set against | Decides |
|---|---|---|---|---|---|
| YT1 | Long-form uploads published against plan, any moved date | Studio app, Content | All in the quarter | PB1 Y4; 3 a quarter | Verdict 1 |
| IG1 | Feed posts published against plan, by format; posts dropped and why | Profile grid; professional dashboard | All in the quarter | PB1 I4 (3–5 a week band) | Record; IR11 counts |
| H1 | Hours per week; weeks over 7; quarter total against 78.0; median week | Hours log (PB1 D2) | Every week | 6.0 a week; 7.0 line | Verdict 2 |
| H2 | Recovery weeks and their logged totals | Hours log (PB4 §7) | Every lost week | 6.5 planned | Verdict 2, through H1 |
| H3 | Edit-window overruns (not exported at the 4-hour stop) | Hours log (PB4 §5) | Every edit window | Three in a row (PB5 §9) | Video length from next checkpoint |
| H4 | Weekends per piece | Backlog and log (PB4 §1, §6) | Every piece finished in the quarter | 2 estimated | Cadence move: 2+ pieces over 2 in two consecutive quarters (§5) |
| H5 | Admin hours, with the week each fell in | Hours log, admin line | Every admin task | Whether taken from a publishing line | Record |

**Block B · YouTube (minutes 13–28)**

| # | Metric | Read from | Qualifies | Set against | Decides |
|---|---|---|---|---|---|
| YT2 | 30-day views per upload; median; best so far | Content, the video, Analytics, Overview | Uploads 30+ days old | PB1 Y1 (180–272; 1,948) | Record; Q2 comparison |
| YT3 | Impressions, click-through rate, largest traffic source, per upload; her median upload's impressions | The video, Analytics, Reach | Uploads 7+ days old | PB1 Y2 (2%–10%, no target) | Verdict 3, from Q2 |
| YT4 | Average percentage viewed and view duration per upload | The video, Analytics, Engagement | Uploads 7+ days old | PB1 Y3 (40–55%, 5–15 min) | Verdict 3, from Q2 |
| YT5 | Intro (share watching at 30 s); her median Intro | Retention report, key moments | Uploads with 100+ views | 50% "above typical" list (PB6 YT5) | R6 selection |
| YT6 | Traffic source split for the quarter; External card, Instagram's share copied to IG10 | Analytics, Reach, traffic source types | All | Own baseline | Record; Instagram's share copied to IG10 |
| YT7 | YouTube search terms | Analytics, Reach, YouTube search terms | All | Own data | Next titles (PB6 R3) |
| YT8 | Back-catalogue share, last 28 days (her calculation) | Analytics, Content | From Q2 | Own baseline | Record |
| YT9 | Subscribers, net per month; unique viewers | Analytics, Overview; Audience | All | PB1 Y6 band medians; §3's √n | Record in year one |
| YT10 | Qualified public watch hours, 365 days | Analytics; Earn | All | 3,000 and 8,000 (PB1 Y10, Y11) | Record; PB9 R3 |
| YT11 | Returning, casual and regular viewers | Analytics, Audience | From Q3 | YouTube's definitions | Record |
| YT12 | Shorts rows | Not applicable | Not read | No Shorts in year one (PB6 R8) | Not read |
| R6* | Packaging check: the one upload, if any, that gets a new thumbnail or title | YT3, YT5 | Uploads 28+ days old | PB6 D1 R6 | Change in next packaging hour |

*R6 here is PB6's rule R6, distinct from PB9's revenue row R6.

**Block C · Instagram (minutes 28–40)**

| # | Metric | Read from | Qualifies | Set against | Decides |
|---|---|---|---|---|---|
| IG2 | Views per post, follower and non-follower share; medians by format | The post, View insights | Posts 7+ days old | PB7 IG2 vendor medians, context | IR11 (Q2) |
| IG3 | Accounts reached per post; median | The post, View insights | As IG2 | PB1 I3 (261, pooled) | Record |
| IG4 | Skip rate per Reel; median | The Reel, View insights | Reels 7+ days old | 65.5% (PB7 IG4; brand accounts) | IR12, from Q2 |
| IG5 | Watch time as a share of length (her calculation); median | The Reel, View insights | As IG4 | Her Q1 median | IR12, from Q2 |
| IG6 | Sends per reach (her calculation); medians by format; zeros counted | The post, View insights | Posts 7+ days old | Own baseline; §3's 3/n | Record |
| IG7 | Likes per reach (her calculation); medians by format | As IG6 | As IG6 | Own baseline | Record |
| IG8 | Followers, total and net per month | Professional dashboard | All | None (§4); §3's √n | Record |
| IG9 | Profile visits; taps on profile links | Professional dashboard, profile activity | All | Own baseline | Record |
| IG10 | YouTube views from Instagram (copied from YT6) | Studio, External card | All | A floor | Record |
| IG11 | Account Status | Settings, Account Status | All | Eligible | PB7 IR10 |
| IG12 | Follower age, gender, country | Professional dashboard, followers | From 100 followers (API threshold) | PB3 D1 trait 8 | AU1 |
| IG13 | Trial reel results | The trial reel | From 1,000 followers | PB7 IR8 | Record |

**Block D · Audience and money (minutes 40–45)**

| # | Metric | Read from | Qualifies | Set against | Decides |
|---|---|---|---|---|---|
| AU1 | Trait 8: age, gender, country, both platforms | IG12; Studio Audience tab | When shown | PB3 D1 trait 8 | Replaces outside evidence |
| AU2 | Trait 9: channels and content her audience watches | Studio, Audience, "Channels your audience watches" | When shown | PB3 D1 trait 9 | Replaces outside evidence |
| R1 | Income by line: gross, fees, net | Gumroad; T3 log | From Q2 | PB9 D3 scenarios | PB9 D4 rule |
| R2 | Guide sales; months with none | Gumroad | From Q3 | PB9 §8 Poisson | PB9 D4 rule |
| R3 | Watch hours and subscribers against programme thresholds | YT9, YT10 | All | 3,000/500; 8,000/1,000 | Record |
| R4 | What the professional dashboard shows as available | Instagram app | All | PB1 I6 | PB9 D4 rule |
| R5 | List size; list × 0.62% against 10 | beehiiv | All | PB9 V14 | PB9 D4 rule |
| R6 | Sponsored and labelled pieces as a share of all pieces | Publishing log | From Q3 | PB9 §11 | PB9 D4 rule |
| R7 | Hours on income lines and the line they came from | Hours log | From Q2 | PB9 V7, V10 | PB9 D4 rule |
| R8 | Cash costs against the 150 USD cap | T3 log | All | PB1 D2 | PB1 D2 correction rule |

**Block E · Handed-over items (HO1 and HO3 at minutes 45–50; HO5 and HO6 in the Instagram block, minutes 28–40; HO2 and HO4 beside the hour)**

| # | Item | When | Inside or beside | Decides |
|---|---|---|---|---|
| HO1 | PB8 clause 10 re-read, five pre-mortem questions, register re-read | Every review | Inside | A policy change, dated |
| HO2 | PB2 repeat-back test, run 2 (one video, five strangers) | Q1 | Beside, 0.75 h from three reply slots | A profile line if it fails |
| HO3 | Next season's remaining pieces | Every review | Inside | The season list |
| HO4 | Break between seasons; Shorts test (PB6 R8); year-two dates; 24-month rule | Twelve-month review | Annual page, beside | D5 |
| HO5 | PB7 IR11 format test | Q2 | Inside | Instagram mix |
| HO6 | PB7 IR12 format flag | From Q2 | Inside | Next season's Reel openings |

### D2 · The review as a sixty-minute procedure

The hour is taken from the review fortnight's cut window, which makes four posts in place of six, two Reels fewer **(her rule)**. Before starting: phone charged, the sheet open, Studio and Insights not opened since the last review (PB1 D3; PB7 D2).

```viz
{"kind": "flow", "title": "The quarterly review in sixty minutes",
 "steps": [
  {"label": "0–5 Set up", "note": "date; list what qualifies"},
  {"label": "5–13 Output and hours", "note": "YT1, IG1, H1–H5, R7"},
  {"label": "13–28 YouTube", "note": "YT2–YT11; R6 choice"},
  {"label": "28–40 Instagram", "note": "IG2–IG9, IG11–IG13; IR11, IR12"},
  {"label": "40–45 Audience and money", "note": "AU1, AU2, R1–R8; D4 start rule"},
  {"label": "45–50 Handed-over items", "note": "HO1, HO3"},
  {"label": "50–60 Verdict", "note": "PB1 order; at most one change per platform"}
 ],
 "caption": "D2: the order and minutes of the review (Mara, fictional; her rule, no source sets the minutes). The blocks follow PB1 D3's verdict order: the inputs the stop and load verdicts read, then the YouTube rows verdict 3 reads, then Instagram's tests (PB7 D1 IR11, IR12), audience (PB3 D1), money (PB9 D5) and the items of §5."}
```

1. **Minutes 0–5 · Set up.** Write the date and the quarter. Count back from the review date: uploads 30 or more days old (YT2), 28 or more (R6), 7 or more (YT3, YT4); posts 7 or more days old (IG2–IG7). Write the counts.
2. **Minutes 5–13 · Output and hours.** YT1, IG1 against plan. From the log: H1 (total, median week, weeks over 7), H2, H3, H4, H5, and PB9 R7. Write "verdict 1: yes/no" and "verdict 2: yes/no".
3. **Minutes 13–28 · YouTube.** Each qualifying upload: YT2, YT3 (with largest source), YT4, YT5. Then the quarter: median impressions, the uploads that count for verdict 3, YT6 (copy Instagram's External share to IG10), YT7, YT8 from Q2, YT9, YT10, YT11 from Q3. From Q2, choose the R6 upload if one qualifies. Write "verdict 3: n uploads count".
4. **Minutes 28–40 · Instagram.** IG2–IG7 per qualifying post and the medians by format, each with its count; IG8, IG9, IG11, IG12, IG13. At Q2, IR11 on all posts of Q1 and Q2; from Q2, IR12.
5. **Minutes 40–45 · Audience and money.** AU1 and AU2. R1–R8 on their first-read dates. Apply PB9 D4's start rule to every line.
6. **Minutes 45–50 · Handed-over items.** HO1: the five questions, yes or no, and the register's open lines. HO3: pick the next season's remaining pieces from the backlog by PB4's rule.
7. **Minutes 50–60 · Verdict.** PB1's order; the first that applies is the verdict. Then at most one change per platform, named, with the date it takes effect and the evidence that would reverse it. Write it in one paragraph and stop.

**Beside the hour.** Q1: the repeat-back test, run 2, 0.75 hours, from the review fortnight's three reply slots. From Q2: the R6 change, 15 minutes inside the next packaging hour (PB6 R6). Twelve-month review: the annual page (D5), 0.75 hours, from that fortnight's three reply slots.

### D3 · Mara's Q1 review, Monday 5 April 2027

Quarter: Monday 4 January to Sunday 4 April 2027, weeks 1–13; Season 1, uploads 1–7 (PB4 D2). Every value below is hers (Mara, fictional).

**Set up.** Uploads 30+ days old: 1–5. Uploads 7+ days old: 1–6; upload 7 (30 Mar) recorded only. Posts 7+ days old: up to Saturday 27 March.

**Output and hours.**

| Row | Q1 |
|---|---|
| YT1 | 7 of 7 published on their dates. Upload 5 (armchair frame, 2 Mar) cut to about 8 minutes after a lost edit window (week 7) |
| IG1 | 35 of 39: 24 of 27 Reels, 11 of 12 carousels. Four dropped (three Reels, one carousel) under PB4's lost-week rule, weeks 9–10 |
| H1 | 77.25 hours against 78.0; median week 6.0. Weeks: 6.5, 6.25, 6.0, 7.0, 6.0, 6.25, 2.0, 7.25, 6.0, 6.25, 5.75, 6.0, 6.0. Weeks over 7: one (week 8, 7.25). Week 4 at 7.0, at the line |
| H2 | One recovery week (week 8): planned 6.5, logged 7.25 |
| H3 | No edit-window overruns. Week 7's edit window was lost, not overrun: piece 5 was not finished |
| H4 | Pieces 1–7: 2, 2, 2, 2, 3, 2, 2 weekends. Piece 5 took a third Saturday (20 Feb), so its reveal was not filmed before the Sunday edit window: the cause of week 7's lost window |
| H5 | Admin 2.75 hours. Run-in: contract read 1.0 (Sun 29 Nov 2026), trademark search 0.75 (Sun 6 Dec 2026), both in weeks with no plan. Q1: sign-up notice 1.0 (week 4), added on top of the plan, which put week 4 at 7.0 |

**YouTube.**

| Upload | Piece | 30-day views | Impressions | CTR | Largest source | % viewed | Intro |
|---|---|---|---|---|---|---|---|
| 1 · 5 Jan | Teak side table | 38 | 640 | 3.0% | YouTube search | 41% | not shown |
| 2 · 19 Jan | Dining chair | 61 | 1,150 | 2.4% | Browse features | 36% | 52% |
| 3 · 2 Feb | Small teak cabinet | 112 | 2,310 | 3.6% | YouTube search | 44% | 61% |
| 4 · 16 Feb | Side table | 47 | 880 | 1.8% | Browse features | 39% | not shown |
| 5 · 2 Mar | Armchair frame (8 min) | 74 | 1,420 | 2.9% | Suggested videos | 47% | not shown |
| 6 · 16 Mar | Nest of two tables | not yet 30 days | 760 | 2.2% | Browse features | 42% | not shown |
| 7 · 30 Mar | Chest of drawers | recorded only | 210 | 4.3% | recorded only | recorded only | not shown |

- YT2: median of uploads 1–5, 61; best so far, upload 3 (112). Against PB1 Y1's 180 for a first upload: below, as PB1 expected (survivor sample, faster cohort).
- YT3: median impressions of uploads 1–6, 1,015. One upload (4) is under 2% with impressions at or below the median; its 95% interval is 1.1% to 2.9% (derived, Wilson). Verdict 3 is not applied in Q1 (PB1 D3).
- YT4: two uploads (2 and 4) under the 40% edge of PB1 Y3's band. Recorded.
- YT5: Intro shown only for uploads 2 and 3, the two past 100 views; median of the two, 56.5%.
- YT6: YouTube search 31%, Browse features 24%, Suggested videos 18%, External 12%, Channel pages 6%, Direct or unknown 5%, other 4%. External, 69 views; Instagram listed with 58, copied to IG10.
- YT7: terms included "remove white water rings teak", "teak veneer lifting", "fix wobbly table leg".
- YT8: not read (first read Q2).
- YT9: 23 subscribers; net 6, 8 and 9 a month. Above PB1 Y6's +0.5 median for 1–99 channels; at a mean of about 8 a month the monthly spread is about ±3 (derived, √8), so the three months do not show a trend. Unique viewers 431.
- YT10: 40.1 qualified watch hours in 365 days, against 3,000 and 8,000.
- YT11, YT12: not read.

**Instagram.** 32 posts qualify: 21 Reels, 11 carousels.

- IG2: Reels, median 412 views, 78% from non-followers; carousels, median 186 views, 41% from non-followers.
- IG3: median reach of the 32, 236 accounts (Reels 301, carousels 118); 261 is PB1 I3's pooled figure, context only.
- IG4: Reels' median skip rate 61.8% (21 Reels, from 54% to 71%). IR12 is not applied in Q1.
- IG5: median watch-time share 38%: the Q1 baseline IR12 reads against.
- IG6: sends per reach, median 0.7% on Reels and 0.0% on carousels; 9 of 11 carousels had no sends. At 118 reached, zero sends bounds the rate at about 2.5% (§3).
- IG7: likes per reach, median 4.0% on Reels, 9.3% on carousels.
- IG8: 212 followers; net 21, 24 and 27 a month.
- IG9: 388 profile visits, 41 taps on profile links.
- IG10: 58 YouTube views from Instagram (from YT6), a floor.
- IG11: eligible.
- IG12: see AU1.
- IG13: not read (212 followers).

**Audience and money.**

- AU1, trait 8: Instagram (212 followers, above the API threshold of 100): ages 18–24 12%, 25–34 31%, 35–44 29%, 45–54 17%, 55–64 8%, 65+ 3%; women 58%, men 42%; United States 22%, United Kingdom 14%, Portugal 9%, Germany 7%, Netherlands 6%. YouTube: "Not enough demographic data" for age and gender. PB3's "on Instagram, mainly under 50" is consistent with her followers: 89% are under 55 (her data; the dashboard's bands do not split at 50, so "under 50" itself cannot be read).
- AU2, trait 9: YouTube shows no data on channels her audience watches. Unknown, as PB3 left it.
- R3: as YT9, YT10. R4: the dashboard shows nothing available to her. R5: list of 9 since the form went live with upload 3 (2 Feb); 9 × 0.62% = 0.06 members, under 10.
- R8: clamp 32 USD (run-in; within PB1 D2's tripod-or-clamp line of up to 40 USD); postal address for the email footer paid from the unspent microphone line, amount in her T3 log from the receipt (this unit states no current CTT price; PB9 D2 V17 has only the 2020 tariff); her T1 tax question answered on Thu 18 Mar 2027 by a tax professional she knows, without charge. Within the 150 USD cap on her receipts.
- R1, R2, R6, R7: not yet due.
- PB9's decision: T1 answered, so the guide is built (PB9 D1): four 1.0-hour blocks from the cut windows of 25 April, 9 May, 23 May and 6 June, launch with upload 12 on Tue 8 June.

**Handed-over items.**

- HO1: five questions, five noes. Policy version 1 stands; register lines J1 and J2 (contract read 29 Nov 2026; it required no notice) and E3–E5 (done; form live 2 Feb) closed; M1 run on 6 Dec 2026, its result written into the register line by her. Register line A3 open, due by Mon 5 Jul 2027.
- HO2, beside (Mon 5 to Wed 7 Apr, 0.75 hours from the reply slots of 7, 14 and 16 April): upload 7 sent to five people who do not know her; answers after at least ten minutes. Who and what named by four of five: pass (convention). Method by three of five. Sheet filed with this review.
- HO3: Season 2 is six pieces, uploads 8–13. On the table: piece 8, a beech dining chair (from 20 Mar), and piece 9, a teak bedside cabinet (from 3 Apr). Picked today, each estimated at two weekends, no workshop step: piece 10, a teak coffee table; 11, a telephone side table; 12, a small teak wall cabinet; 13, a teak plant table.

**Verdict.** Verdict 1: no (7 uploads; it needs two quarters). Verdict 2: no (one week over 7). Verdict 3: not applied in Q1. PB4's cadence move: no (one piece of seven over two weekends; the rule needs two in each of two quarters). **Continue.** Changes: on Instagram, the guide's build takes two Reels from each of four fortnights (PB9 D1), and it is the quarter's one Instagram change; nothing else changes. On YouTube, none. Hours for this review: two Reels fewer in the cut window of Sun 11 April (Season 2's upload 8 posts).

### D4 · Mara's Q2 review, Monday 5 July 2027

Quarter: Monday 5 April to Sunday 4 July 2027, weeks 14–26; Season 2, uploads 8–13. Every value is hers (Mara, fictional).

**Set up.** Uploads 30+ days old: 1–11. Uploads 28+ days old: 1–11. Uploads 7+ days old: 1–13. Posts 7+ days old: up to Monday 28 June; the carousel of Thu 1 July recorded only.

**Output and hours.**

| Row | Q2 |
|---|---|
| YT1 | 6 of 6 on their dates. Upload 13's edit (Sun 13 Jun) hit the 4-hour stop unexported; finished in the cut window of Sun 20 Jun |
| IG1 | Plan 29: 39, less two Reels for the Q1 review's hour, less eight for the guide (15 Reels, 14 carousels). Published 25 (12 Reels, 13 carousels): four dropped (three Reels, one carousel) after the edit overrun, weeks 25–26 |
| H1 | 80.75 hours against 78.0; median week 6.0. Weeks: 6.5, 5.5, 6.0, 6.0, 6.75, 6.0, 6.0, 7.25, 6.0, 6.0, 6.25, 6.5, 6.0. Weeks over 7: one (week 21, 7.25: replies after a Reel was shared widely) |
| H2 | No recovery weeks |
| H3 | One edit-window overrun (week 23) |
| H4 | Pieces 8–13: 2 weekends each |
| H5 | Admin 0.5: register line A3 read in week 25, on top of the plan |
| R7 | Guide: 4.75 hours (estimate 4.0), all inside the four cut windows; the block of 9 May ran 1.75 |

**YouTube.**

| Upload | Piece | 30-day views | Impressions | CTR | Largest source | % viewed | Intro |
|---|---|---|---|---|---|---|---|
| 8 · 13 Apr | Beech dining chair | 81 | 1,340 | 3.4% | YouTube search | 43% | 59% |
| 9 · 27 Apr | Teak bedside cabinet | 104 | 1,860 | 2.6% | Browse features | 41% | 54% |
| 10 · 11 May | Teak coffee table | 241 | 4,920 | 1.9% | Suggested videos | 38% | 51% |
| 11 · 25 May | Telephone side table | 96 | 1,210 | 1.7% | Browse features | 45% | 57% |
| 12 · 8 Jun | Small teak wall cabinet | not yet 30 days | 1,050 | 2.8% | YouTube search | 40% | not shown |
| 13 · 22 Jun | Teak plant table | not yet 30 days | 690 | 1.6% | Browse features | 37% | not shown |

- YT2: 30-day views of uploads 1–10: 38, 61, 112, 47, 74, 63, 70, 81, 104, 241; median 72, against PB1 Y1's 180–272. Best so far upload 10 (241). None past 1,000, as for 42.2% of PB1's cohort (PB1 D3).
- YT3: median impressions of uploads 8–13, 1,275. Under 2%: upload 10 (1.9%, 4,920 impressions, above the median: recorded, not counted), upload 11 (1.7%, 1,210; 95% interval 1.1% to 2.6%) and upload 13 (1.6%, 690; 0.9% to 2.8%) (intervals derived, Wilson).
- YT4: under 40%: uploads 10 (38%) and 13 (37%).
- Verdict 3 count: uploads 10 (% viewed), 11 (CTR) and 13 (both): **three**. Neither CTR reading alone is clear of 2%; the count is what carries the verdict (§3).
- YT5: Intro shown for uploads 2, 3, 8, 9, 10 and 11 (52%, 61%, 59%, 54%, 51%, 57%); her median of the six, 55.5%.
- R6 (PB6): uploads 28+ days old in the quarter: 8–11. Lowest CTR, upload 11 (1.7%); impressions 1,210, under 1,275; Intro 57%, above 55.5%. It qualifies: one new thumbnail, made in the packaging hour of Sun 18 Jul, CTR before (1.7% on 1,210) recorded. A one-video comparison with no control.
- YT6: YouTube search 29%, Suggested videos 26%, Browse features 22%, External 11%, Channel pages 6%, Direct or unknown 4%, other 2%. External, 141 views; Instagram 97, copied to IG10.
- YT7: new terms included "fix veneer bubble" and "restore furniture in apartment"; the second goes into upload 16's title (PB6 R3).
- YT8: first reading: views on uploads 1–7 in the 28 days to 4 Jul, 118 of 402 channel views, 29%. Own baseline.
- YT9: 61 subscribers; net 11, 13, 14 a month; 50 passed in June (PB1 Y12, a milestone only). Unique viewers 902.
- YT10: 133.0 hours in 365 days.

**Instagram.** 24 posts qualify: 12 Reels, 12 carousels.

- IG2: Reels, median 455 views, 74% non-followers; carousels, median 240, 46% non-followers.
- IG3: median reach 251. IG4: Reels' median skip rate 63.9% (12 Reels). IG5: median watch-time share 36%.
- IG6: sends per reach, 0.9% Reels, 0.4% carousels. IG7: likes per reach, 3.8% Reels, 8.7% carousels.
- IG8: 318 followers; net 31, 36, 39. IG9: 512 profile visits, 63 link taps. IG10: 97. IG11: eligible. IG13: not read.
- IR11, on every post of Q1 and Q2 now 7+ days old (36 Reels, 23 carousels): Reels' median non-follower views 330, carousels' 97. Carousels do not equal or beat Reels: the mix stands. Both medians rest on more than five posts (§3, rule 5), and the gap is read as a direction.
- IR12: skip rate 63.9%, not above 65.5%; watch share 36%, under her Q1 38%. Both conditions are needed: not raised.

**Audience and money.**

- AU1: Instagram (318): 18–24 11%, 25–34 30%, 35–44 30%, 45–54 18%, 55–64 8%, 65+ 3%; women 55%, men 45%; United States 24%, United Kingdom 13%, Portugal 7%, Germany 7%, Canada 6%. YouTube: still "Not enough demographic data".
- AU2: YouTube lists six channels her audience watches: four furniture-restoration channels and two woodworking channels (not named here). Trait 9 now has her own data.
- R1: guide, three sales from 8 June: gross 45.00 USD, fees 6.00, net 39.00 (PB9 D3's 13.00 a sale). Base scenario V6 is 8 sales over 209 days; three in 26 days is more than the low scenario predicts (an expected 0.25 sales in 26 days) and inside the spread of the base and high scenarios (expected 1.0 and 3.0) (derived from PB9 D2 V6, Poisson as PB9 §8). Launch-week sales are not independent of the launch email, and one month's count decides nothing (PB9 §8). R2 from Q3.
- R5: list of 31; 31 × 0.62% = 0.19. R4: nothing shown. R8: no new cost.
- PB9 D4's rule re-applied: no other line starts. Brand deals open from upload 14 (6 Jul) as inbound only, register line A3 having been read (PB9 D1).

**Handed-over items.**

- HO1: five noes; register line A3 closed (23 Jun). No policy change.
- HO3: Season 3 is seven pieces, uploads 14–20. On the table: 14, a teak sewing cabinet (from 19 Jun), and 15, a beech stool (from 3 Jul). Picked today, each at two weekends: 16, an oak bedside table; 17, a teak tray table; 18, a side chair with a cane seat (the cane referred out, PB2 D4); 19, a small teak bookcase; 20, a small walnut-veneer cabinet.

**Verdict.** Verdict 1: no (7 and 6 uploads). Verdict 2: no (one week over 7). Verdict 3: yes (three uploads). **Change the format.** The one YouTube change: packaging. From upload 15 (Tue 20 Jul 2027, the season's second video, PB4 §4), the thumbnail shows the fault and the finished piece side by side, at most four words, in her colours (PB5 §7), in place of the finished piece alone. Why packaging over length or structure: two of the three uploads count on click-through with impressions below her median, which is the case YouTube names for a title or thumbnail change (PB1 D3, YouTube Help 16559651); the two percentage-viewed readings sit 2 and 3 points under the edge of a vendor band published without a sample (PB1 Y3). What reverses it: at the Q3 review, the same count on uploads 15–20. If percentage viewed is still under band on three uploads at Q3, structure is the next change. On Instagram: none (IR11 and IR12 not triggered). R6 upload 11's new thumbnail uses the new layout, so its before-and-after is one early, uncontrolled reading. Hours for this review: two Reels fewer in the cut window of Sun 18 July; week 27 ran at 7.0, at the line.

### D5 · Mara's annual review: one page, Monday 3 January 2028

The twelve-month review runs D2 as at every quarter, then this page, 0.75 hours beside the hour, from the three reply slots of weeks 53–54 **(her rule)**. Lines marked "read 4 Oct 2027" or "read 3 Jan 2028" are filled on those days (Mara, fictional).

**1. Cadence test.** 26 uploads planned; the year passes at 24 or more (PB1 D3). Q1 7, Q2 6, Q3 read 4 Oct 2027, Q4 read 3 Jan 2028.

**2. The four verdicts.** Q1 continue. Q2 change the format (thumbnail layout from upload 15). Q3 read 4 Oct 2027. Q4 read 3 Jan 2028.

**3. The year against PB1.** Expect under 1,000 subscribers, the outcome for 91.35% of channels in her band (PB1 D1 Y4), and watch hours far under 8,000 (Y10). At Q2: 61 subscribers, 133.0 hours. Median 30-day views of each quarter's uploads: Q1 61 (uploads 1–5), Q2 to date 100 (uploads 8–11, as qualifying at the Q2 review), Q3 and Q4 to fill.

**4. Hours.** Year total against 312.0; weeks over 7 by quarter (Q1 1, Q2 1); recovery weeks (Q1 1, Q2 0); edit overruns (Q1 0, Q2 1); admin by quarter (run-in 1.75, Q1 1.0, Q2 0.5). Q3, Q4 to fill.

**5. Money.** Spending against 150 USD: within it at Q2. Income against PB9's scenarios: her guide count, list size and deals replace V6, V8 and V12; the model is rerun and D4's rule applied to every line (PB9 D5).

**6. Decisions for year two.**

- *Break between seasons.* Taken only if her log shows weeks over 7 in at least two quarters, or recovery weeks or overruns in three or more; then at most two breaks in year two, each one fortnight with no upload between seasons (two breaks, plus any upload moved 7 days under PB4 §7, kept under the "three or more times" of PB1 §6; YouTube answer 141805 finds no correlation between break length and change in views). Two breaks leave 24 uploads, which passes the cadence test and stays in Y4's 12–51 band **(her rule)**. Q1 and Q2 each had one week over 7; decided 3 Jan 2028.
- *Shorts for one season* (PB6 R8): only if the log shows slack, which Q2's 80.75 hours against 78.0 does not; decided 3 Jan 2028.
- *Trademark registration* (PB8 M2): not before today; decided 3 Jan 2028.
- *The year's single change for Season 5*, under §6's verdicts.

**7. Year two's dates.** Day one of year two: Monday 3 January 2028; upload 27 on Tuesday 4 January 2028; uploads 27–52 at one a fortnight. Reviews: Q5 Monday 3 April 2028 (uploads 27–33); Q6 Monday 3 July 2028 (34–39); Q7 Monday 2 October 2028 (40–46); the 24-month review, Monday 1 January 2029 (47–52), a public holiday, so PB4's holiday rule moves it within its own week.

**8. The 24-month rule.** At the 24-month review, subscriber count may count towards a stop for the first time (PB1 D3). It counts only if all three hold: under 1,000 subscribers; net subscribers per month under row Y6's band median in each of year two's four quarters; and the median 30-day views of year two's uploads not above year one's. At 52 uploads she has passed the 40 that 68% of crossers had, and not the 70 that 53.5% had (PB1 D1 Y5), so under 1,000 at that review is inside the range those channels show **(her rule)**.

**9. Decided, in writing,** with the four quarters' sheets attached: continue, change one thing, change the format, or stop.

### Templates

**T1 · Your metrics sheet.** Copy PB6's T2 and PB7's T2 rows into the five blocks of D1. For each row:

| # | Metric | Read from | Qualifies | Set against | Decides |
|---|---|---|---|---|---|
| [PB6 or PB7 row code, or H, A, R, P for your own] | [the number, in the platform's own name for it] | [the menu path on your device] | [the minimum age of a piece, or the follower or view count, before it is read] | [the sourced benchmark from your PB1 sheet with its row, or "own baseline"] | [the verdict or test it feeds, or "record"] |

Rows read once and written twice: [any number two rows both read, and the row it is read in].

**T2 · Your sixty-minute procedure.**

- Where the hour comes from: [a named cut in the fortnight that holds the review, from your cut order; never the anchor piece].
- Minutes 0–5: [your review date; the ages that qualify, counted back from it].
- Minutes 5–13: [your output rows and hours rows; your over-budget line].
- Minutes 13–28: [your anchor platform's per-piece rows, and the count your format verdict reads].
- Minutes 28–40: [your second platform's rows and any test on it].
- Minutes 40–45: [audience traits you read from your own data; your revenue rows].
- Minutes 45–50: [the items earlier units hand your review: your policy questions, your next season's pieces].
- Minutes 50–60: [your verdicts, in order; at most one change per platform, its start date and what would reverse it].
- Beside the hour: [each item that needs other people, a delay or writing; its hours, and the slot they come from].

**T3 · Your review, filled.**

- Quarter: [dates; weeks; season; uploads n to m].
- Qualifying: [uploads 30+, 28+ and 7+ days old; posts 7+ days old; pieces recorded only].
- Output and hours: [published against plan by platform and format; hours total against plan; median week; weeks over your line; recovery weeks; overruns; units of work that took longer than estimated; admin hours and the week each fell in].
- Anchor platform, per piece: [one line per qualifying piece, every row your format verdict reads, with the denominator beside each rate].
- Anchor platform, the quarter: [medians with their counts; the pieces that count towards the format verdict; any reading whose interval you checked (§3)].
- Second platform: [medians by format with counts; any test due this quarter, its threshold, its result].
- Audience: [each trait your data now shows, and the outside evidence it replaces; "not enough data" where it does not].
- Money: [spent against your cap; income by line; your start rule applied to each line].
- Handed-over items: [your policy questions, yes or no; your next pieces; any test run beside the hour].
- Verdict: [stop or rebuild, change one thing, change the format, continue: the first that applies, with its evidence; the one change per platform, if any; its start date; what would reverse it; where this review's hours came from].

**T4 · Your annual page.**

1. Cadence test: [pieces planned; your pass line; pieces published by quarter].
2. Verdicts: [the four quarters' verdicts and changes].
3. The year against your expectation sheet: [each PB1 row that applies, its value, and yours].
4. Hours: [year total against budget; weeks over your line, recovery weeks, overruns and admin by quarter].
5. Money: [spending against cap; income against your scenarios; the inputs your counts replace].
6. Decisions for year two: [a break between seasons, with your rule and the evidence for and against; any format you test, only if your hours show slack; legal lines your register dates to this review].
7. Year two's dates: [day one; each review, 13 weeks apart; holidays moved within their week].
8. Your 24-month rule: [the conditions under which audience size counts towards stopping, each read against a sourced row].
9. Decision, in writing, with the four sheets attached.

## Sources

- Barnett, Adrian G., Jolieke C. van der Pols and Annette J. Dobson, "Regression to the mean: what it is and how to deal with it", *International Journal of Epidemiology* 34(1), 2005, 215–220, PubMed 15333621. https://pubmed.ncbi.nlm.nih.gov/15333621/
- Kohavi, Ron, Roger Longbotham, Dan Sommerfield and Randal M. Henne, "Controlled experiments on the web: survey and practical guide", *Data Mining and Knowledge Discovery* 18(1), 2009, 140–181. https://exp-platform.com/journal-survey
- Meta for Developers, "Instagram account insights" (Instagram Platform API reference), checked 13 Nov 2026. https://developers.facebook.com/docs/instagram-platform/api-reference/instagram-user/insights
- Newman, Thomas B., "If almost nothing goes wrong, is almost everything all right? Interpreting small numerators", letter, *JAMA* 274(13), 4 Oct 1995, 1013 (crediting Hanley and Lippman-Hand, *JAMA*, 1983). https://jamanetwork.com/journals/jama/article-abstract/389714
- NIST, Dataplot Reference Manual, "Sign test", checked 13 Nov 2026. https://itl.nist.gov/div898/software/dataplot/refman1/auxillar/signtest.htm
- NIST/SEMATECH e-Handbook of Statistical Methods, §1.3.6.6.18, "Binomial distribution", checked 13 Nov 2026. https://itl.nist.gov/div898/handbook/eda/section3/eda366i.htm
- NIST/SEMATECH e-Handbook of Statistical Methods, §1.3.6.6.19, "Poisson distribution", checked 13 Nov 2026. https://itl.nist.gov/div898/handbook/eda/section3/eda366j.htm
- NIST/SEMATECH e-Handbook of Statistical Methods, §7.2.4.1, "Confidence intervals", checked 13 Nov 2026. https://itl.nist.gov/div898/handbook/prc/section2/prc241.htm
- NIST/SEMATECH e-Handbook of Statistical Methods, §7.2.4.2, "Sample sizes required", checked 13 Nov 2026. https://itl.nist.gov/div898/handbook/prc/section2/prc242.htm
- TechCrunch, "YouTube will no longer be deleting videos from inactive accounts", 18 May 2023. https://techcrunch.com/2023/05/18/youtube-will-no-longer-be-deleting-videos-from-inactive-accounts
- YouTube Help, "The YouTube Partner Programme overview and eligibility" (answer 72851), checked 13 Nov 2026. https://support.google.com/youtube/answer/72851?hl=en-GB
- YouTube Help, "Understand limited data in YouTube Analytics" (answer 9101241), checked 13 Nov 2026. https://SUPPORT.GOOGLE.COM/youtube/answer/9101241
- YouTube Help, "YouTube performance FAQ & troubleshooting" (answer 141805), checked 13 Nov 2026. https://support.google.com/youtube/answer/141805?hl=en

Every other figure is carried from this course's units and cited there by row: PB1 D1 (Y1–Y12, I1–I7, B1–B2), PB1 §2, §4 and §6, PB6 D1–D2, PB7 D1–D2, PB9 D2–D5; each rests on the sources those units list.

## Unsure list

- Whether Instagram's in-app Insights shows follower demographics from the same 100 followers as Meta's API reference; the app was not checked (§5, D1 IG12).
- The Wilson intervals and the 2,045-impression figure treat impressions as independent trials; repeat impressions to one viewer break that, and how much is not measured (§3).
- AIR Media-Tech's "14+ days three or more times a year" finding rests on PB1 §6's reading; the AIR page was not re-opened in this run (§5, D5).
- Google's 2023 statement on not deleting accounts with YouTube videos is a 2023 statement via TechCrunch; Google's current inactive-account policy page was not opened, nor what counts as activity (§9).
- The Rule of three is cited through a 1995 JAMA letter that credits Hanley and Lippman-Hand; the 1983 paper itself was not opened (§3).
- The review's 60 minutes, the 0.75 hours for the repeat-back test and for the annual page, and the minute blocks of D2 are her estimates; no source gives the time a review takes (§5, D2).
- The YouTube Studio app path to "Channels your audience watches" was not confirmed in the app (D1 AU2).
- Kohavi et al. is cited from the authors' own survey page; the full paper's text was not read beyond its abstract (§7).

- Object: the metrics sheet, the review's one page of rows, discussed at length in §1 and built in D1
- Fresh check 2026-11-13 (Opus 5.5; a Fable 5.1 fresh check is owed, P49): fix · 0 errors, 8 should-fix, 33 minor; all applied as the report gives them; figure 4 corrected; on re-check from the shots two of its labels were corrected again (IG10 is filled in step 3; at most one change per platform), then two more on the third check (R7; the D4 start rule), and checked a fourth time; figures 1 to 3 passed; report `audits/personal-brand/fresh-check-PB10.md`.
- Correction 2026-11-13, found by the W-PB10 round-2 correction check (P108): §5 item 3 quotes PB4 §1's earlier cadence wording; PB4 §1 was corrected on 13 Nov 2026 to two or more pieces in a quarter taking more than two weekends, in two consecutive quarters, the rule as §5 reads it; a note after the quotation says so. The Object line is now a list item, as in the other units (the same check, no content change).
