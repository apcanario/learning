Model: claude-fable-5-2

# PB10 · Stratified-sample audit (course PB, Audit 3, part 2) · 15 November 2026 · search on

## Provenance

- Auditor: one fresh, isolated agent, model claude-fable-5-2. Read only `/home/claude/fpb/PB10`; wrote only `out/`. No memory, past-chat, Projects, connector, Artifact, Agent or `mcp__` tool used.
- Unit: `unit.md` (PB10; written 2026-11-13 by Opus 5.5; search flag off; Audit 4's seven replacements of 14 Nov 2026 applied). Not edited.
- `out/` was empty at the start: a first run of part 2, not a resumed one. The sample was written to `out/audit.md` and `out/sample.md` before any check.
- Part 2 of the audit of 14 Nov 2026 (`run1-audit.md`), which opened no outside source. The sample is run 1's, copied unchanged and not redrawn.
- Web: 31 searches (limit 40), 31 fetches, each of a URL a search in this agent returned verbatim. No call was refused.

## Sample (copied from run 1, recorded before any check)

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

## Table: the sample

| n | Section | Claim | Source | Verdict | Note |
|---|---|---|---|---|---|
| 1 | §1 | Qualifying ages: 30 days (YT2), 7 days (YT3, YT4), 7 days for an Instagram post | others/PB6 D2 YT2-YT4; others/PB7 D2 IG2-IG7 and D1 IR4 | PASS | PB6 D2: "uploads at least 30 days old", "at least 7 days old"; PB7 D2 rows: "posts at least 7 days old"; PB7 D1 IR4: "read once it is 7 days old". Internal pointer; no outside source |
| 2 | §2 | Watch hours only from "long-form videos that you've set to public"; not private, unlisted, deleted or Shorts | https://support.google.com/youtube/answer/72851?hl=en-GB | PASS | Page (title "The YouTube Partner Programme overview and eligibility"): "Qualified watch hours gained from long-form videos that you've set to public"; private, unlisted and deleted videos and Shorts listed as not counting |
| 3 | §3 | About 2,045 impressions (hypothesis 3%, true 2%), about 1,747 the other way; continuity correction adds 100 | https://itl.nist.gov/div898/handbook/prc/section2/prc242.htm | PASS | §7.2.4.2 "Sample sizes required" gives the two-sided formula with z(1-α/2) and z(1-β) over δ, and the correction N = N' + 1/δ (1/0.01 = 100). Recomputed: 2,044.6 and 1,746.9 |
| 4 | §4 | Buffer's I4 is an increment over weeks with no posts: "points added to the weekly growth rate" | others/PB1 §3; https://buffer.com/library/how-often-to-post-on-instagram/ | PASS | Quotation exact in PB1 §3. Buffer (13 Aug 2025, 2.1M posts, 102K accounts, fixed-effects): +0.12/+0.26/+0.44/+0.66%, "compared to weeks when users don't post at all", "an increase in follower growth rate" |
| 5 | §5 | "Not returned if the IG User has less than 100 followers"; follows and unfollows likewise | https://developers.facebook.com/docs/instagram-platform/api-reference/instagram-user/insights | PASS | Exact words on the page under follower_demographics and under follows_and_unfollows |
| 6 | §6 | Floor of the 12-51 band; below it 1.86% | others/PB1 D1 Y4; https://vidiq.com/research/youtube-uploads-1000-subscribers/ | PASS | vidIQ, 11 Sep 2026, 32,926,088 channels, 360 days: 0.20%, 1.86% (1-11), 8.65% (12-51), 30.77% (52+) |
| 7 | §7 | Regression to the mean "happens when unusually large or small measurements tend to be followed by measurements that are closer to the mean" | https://pubmed.ncbi.nlm.nih.gov/15333621/ | PASS | PubMed abstract: "It happens when unusually large or small measurements tend to be followed by measurements that are closer to the mean." Int J Epidemiol 2005, 34(1), 215-20 |
| 8 | §8 | 1,000 US and UK creators: 52% burnout, 37% considering leaving | others/PB1 D1 B2; https://billiondollarboy.com/news/over-half-of-creators-face-burnout | PASS | Billion Dollar Boy, 7 Jul 2025: survey of 1,000 creators (and 1,000 senior marketers) across the US and UK; 52% burnout; 37% "actively consider leaving" |
| 9 | §9 | Google 2023: two years' inactivity; "We do not have plans to delete accounts with YouTube videos at this time" | https://techcrunch.com/2023/05/18/youtube-will-no-longer-be-deleting-videos-from-inactive-accounts | PASS | TechCrunch, 18 May 2023, headline as in Sources; the sentence is quoted from Google's updated blog post; two-year inactivity policy stated |
| 10 | Deliverable D4 | Low CTR with fewer impressions than usual is the case YouTube names for a title or thumbnail change | others/PB1 D3; https://support.google.com/youtube/answer/16559651?hl=en | PASS | Page: changes are advised when "a video has a lower click-through rate (CTR) and is receiving fewer impressions than usual" |
| 11 | Deliverable D5 | 91.35% under 1,000 in her band; 68% of crossers had 40+, 53.5% had 70+ | others/PB1 D1 Y4, Y5; https://vidiq.com/research/youtube-uploads-1000-subscribers/ ; https://vidiq.com/blog/post/how-many-videos-to-get-1000-subscribers | PASS | 100 - 8.65 = 91.35 (derived). vidIQ, 9 Jun 2025, 5,330,249 channels: 14.54 + 22.58 + 30.89 = 68.01%; 22.58 + 30.89 = 53.47% |
| 12 | Sources | Newman, letter, JAMA 274(13), 4 Oct 1995, 1013; credits Hanley and Lippman-Hand (JAMA, 1983); 3/n | https://jamanetwork.com/journals/jama/article-abstract/389714 ; https://scilit.com/publications/ddfc523d905fccaecb8488227831d6ec | PASS | JAMA page: title, Thomas B. Newman, letter, 274(13), 4 Oct 1995, p. 1013; credits Hanley and Lippman-Hand's rule, upper limit "approximately 3/N". Scilit record of the earlier paper: JAMA 249(13), 1 Apr 1983, 1743-1745 |

All twelve were opened at the outside source where one stands behind the claim (eleven of twelve; claim 1 is a pointer to PB6 and PB7 only).

## Also checked (beyond the sample)

| n | Section | Claim | Source | Verdict | Note |
|---|---|---|---|---|---|
| 13 | §2 | Todd Beaupré, senior director of growth and discovery: "maybe a 10% or less"; PPC Land, 2 Sep 2026 | https://ppc.land/subscribers-skip-90-of-uploads-in-their-feed-youtube-director-says/ | PASS | PPC Land, 2 Sep 2026: "probably all your videos have about maybe a 10% or less click-through rate"; title as given |
| 14 | §2 | PB1's band medians: +0.5 (1-99) and +1.4 (100-499) subscribers a month | https://vidiq.com/research/youtube-subscriber-benchmarks-2026/ | PASS | vidIQ, 20 Jul 2026: +0.5 (1,047,481 channels), +1.4 (1,430,714), +3.7 (853,903) |
| 15 | §3 | NIST §7.2.4.1: Wilson interval's worth "does not strongly depend upon the value of n and/or p"; the page also gives p ± z·√(p(1−p)/n) | https://itl.nist.gov/div898/handbook/prc/section2/prc241.htm | PASS | Exact words; the page names the method Wilson and gives the normal-approximation expression as the one "most frequently used" |
| 16 | §3 | NIST §7.2.4.1: limits may not be accurate enough "if the number of failures is very small or if the sample size N is very small" | https://itl.nist.gov/div898/handbook/prc/section2/prc241.htm | PASS | Exact words (the page's sentence begins "If the number of failures...") |
| 17 | §3 | NIST §1.3.6.6.19: Poisson "is used to model" events in a time interval; standard deviation is the square root of the mean | https://itl.nist.gov/div898/handbook/eda/section3/eda366j.htm | PASS | "The Poisson distribution is used to model the number of events occurring within a given time interval."; mean λ, standard deviation √λ |
| 18 | §3 | NIST Dataplot: "the test statistic for the sign test follows a binomial distribution with p=0.5" | https://itl.nist.gov/div898/software/dataplot/refman1/auxillar/signtest.htm | PASS | Exact words |
| 19 | §3 | Binomial formula in NIST §1.3.6.6.18 | https://itl.nist.gov/div898/handbook/eda/section3/eda366i.htm | PASS | Section 1.3.6.6.18 "Binomial Distribution" gives the probability mass function |
| 20 | §3 | Wilson intervals for 3.0% at 250-5,000 impressions; skip rate 62% on 100 and 400 views; verdict-3 table | derived; recomputed in this run | PASS | All ten bounds, 52.2-70.9, 57.2-66.6, and 87.7/99.7, 46.9/59.7, 13.0/3.3, 2.0/0.02 reproduced |
| 21 | §4 | Y1: median about 180 (upload 1) to 272 (upload 10); median best of ten 1,948 | https://vidiq.com/research/youtube-first-10-videos-study/ | PASS | vidIQ, 28 Jul 2026 (updated 30 Jul): 137,355 long-form channels; 180, 211, 272; best of first ten 1,948; 57.8% had one past 1,000 |
| 22 | §4 | Y2: half of channels and videos between 2% and 10% click-through | https://support.google.com/youtube/answer/7628154?hl=en-GB | PASS | "Half of all channels and videos on YouTube have an impressions CTR that can range between 2% and 10%." |
| 23 | §4 | Y3: 40-55% viewed for 5-15 minute videos, vendor heuristic, no sample | https://vidiq.com/blog/post/average-view-duration/ | PASS | vidIQ, updated 21 Jul 2026: "aim for 40 to 55% viewed", "vidIQ guidance for target bands"; no sample |
| 24 | §4 | Y4: 8.65% of channels adding 12-51 videos crossed 1,000 within 360 days | https://vidiq.com/research/youtube-uploads-1000-subscribers/ | PASS | as sampled claim 6 |
| 25 | §4 | Y5: 68% of channels that crossed 1,000 had 40 or more videos | https://vidiq.com/blog/post/how-many-videos-to-get-1000-subscribers | PASS | as sampled claim 11 |
| 26 | §4 | Y6: +0.5, +1.4, +3.7 subscribers a month by band | https://vidiq.com/research/youtube-subscriber-benchmarks-2026/ | PASS | as above |
| 27 | §4 | Y10, Y11: 8,000 and 3,000 watch hours with 1,000 and 500 subscribers | https://support.google.com/youtube/answer/12843009 (PB1's source; not returned by search) | unverifiable | The Help page was not returned by any search, so it could not be fetched. A secondary page agrees: vidIQ (https://vidiq.com/blog/post/youtube-partner-program-changes-2027/) gives 1,000 + 8,000 hours for new creators from 1 Feb 2027 and 500 + 3,000 for the fan-funding tier. Answer 72851 (en-GB) still shows 4,000 hours, the rule until that date |
| 28 | §4 | Y12, I5: Live at 50 subscribers; Instagram Live at 1,000 followers | https://support.google.com/youtube/answer/9228390 ; https://9to5mac.com/2025/08/01/new-instagram-rule-cuts-off-live-broadcasts-for-small-accounts/ | PASS | YouTube Help: "At least 50 subscribers" and a verified channel; 9to5Mac, 1 Aug 2025: public accounts with 1,000 followers or more, confirmed by Meta to TechCrunch |
| 29 | §4 | I3: median reach 261 accounts a post, all sizes pooled | https://buffer.com/social-media-benchmarks/instagram | PASS | Buffer benchmarks, updated 8 Nov 2026: 261 under "All"; 7.5% monthly growth |
| 30 | §4 | PB1's earlier Q3 wording: "with the 0.36-a-week illustration (I4)" | others/PB1 (current text and correction note of 2026-11-13) | unverifiable | The unit now says these are PB1's earlier words (Audit 4). PB1 no longer holds them; its correction note confirms the comparison was removed but does not reproduce the sentence, so the exact earlier wording cannot be checked from the folder |
| 31 | §4 | PB1 D3's Q3 line and PB7's IG8 column were corrected on 13 Nov 2026 and now read this way | others/PB1 correction note; others/PB7 D2 IG8 | PASS | Run-1 erratum 1 no longer applies |
| 32 | §5 | PB1's earlier wording: "that fortnight's publishing-and-replies line" (PB1 D2); PB4 D1 G repeated it; both corrected 13 Nov 2026 | others/PB1 D2 and correction note; others/PB4 | unverifiable | As above: the correction is confirmed (PB1 D2 now takes the hour from the Instagram derivatives); the earlier sentence is not in the folder. Run-1 erratum 2 no longer applies |
| 33 | §5 | Buffer's within-account estimates: +0.12% at 1-2 posts against +0.26% at 3-5 | https://buffer.com/library/how-often-to-post-on-instagram/ | PASS | as sampled claim 4; 0.14% × 212 = 0.30 |
| 34 | §5 | YouTube 9101241: thresholds "are not published"; "Not enough demographic data" | https://SUPPORT.GOOGLE.COM/youtube/answer/9101241 | PASS | "The actual thresholds at which data is limited are not published and subject to change at YouTube's discretion."; "Not enough demographic data." |
| 35 | §5 | YouTube 141805: "We studied thousands of channels that took a break and found no correlation between break length and changes in views"; "growth in views across uploads is not correlated with time between uploads"; no sample size, period or method | https://support.google.com/youtube/answer/141805?hl=en | PASS | Both exact. The page gives "thousands of channels" and "over the years" and no method, as the unit says |
| 36 | §5 | AIR Media-Tech: dark 14+ days three or more times a year goes with fewer views per video; main analysis 100,000-1,000,000 monthly views | https://air.io/en/audience-growth/does-posting-more-on-youtube-help-we-studied-18000-channels-to-find-out | PASS | AIR, 8 Jun 2026: "Channels that went dark for 14+ days three or more times a year got fewer views per video"; 100K-1M segment; "This is correlational data, not causal." |
| 37 | §5 | PB4 §1's earlier wording: "If her log shows pieces averaging more than two weekends" | others/PB4 §1 (current text) | unverifiable | The unit marks it as earlier wording (P108). PB4 now states the two-pieces-in-two-quarters rule; the earlier sentence is not in the folder |
| 38 | §5 | PB2: five strangers, ten minutes, four of five; conventions (PB2 §3, D5) | others/PB2 | PASS | carried from run 1, row 45; text unchanged |
| 39 | §5 | PB8 clause 10 and its five pre-mortem questions (PB8 D1, D2) | others/PB8 | PASS | carried from run 1, row 54; text unchanged |
| 40 | §7 | Kohavi et al. 2009: controlled experiments are "the best scientific design for establishing a causal relationship between changes" and their effect | https://exp-platform.com/journal-survey | PASS | Page: "Controlled experiments embody the best scientific design for establishing a causal relationship between changes and their influence on user-observable behavior"; DMKD 18(1), 2009, 140-181; four authors as listed |
| 41 | §7 | Test & Compare is computer-only and may return "Not enough impressions" or "Inconclusive" (PB6 §3) | others/PB6 §3; https://support.google.com/youtube/answer/13861714 | PASS | PB6 §3 has both strings. YouTube Help, "A/B test titles & thumbnails": "currently only available on computers through YouTube Studio"; "Inconclusive" is a result label; "Not enough impressions" appears as a reason no winner is named, not as a label (loose, not wrong) |
| 42 | §6 | Verdict 3 reads the anchor platform, "whose two numbers YouTube itself documents" | https://support.google.com/youtube/answer/7628154?hl=en-GB | PASS | YouTube documents both metrics and the 2-10% range; the 40-55% band is vidIQ's, which §4 says |
| 43 | Deliverable D1 | AU2: Studio, Audience, "Channels your audience watches" | https://support.google.com/youtube/answer/9314416 | FAIL | YouTube Help 9314416 names the report "Channels that your audience watches"; PB3 D1 trait 9 quotes it that way. The quoted label drops "that" (errata PB10-6, PB10-7). Minor |
| 44 | Deliverable D1 | YT5: 50% "above typical" list (PB6 YT5) | others/PB6 | PASS | string present in PB6 |
| 45 | Deliverable D3 | PB3's "on Instagram, mainly under 50" | others/PB3 | PASS | string present in PB3 |
| 46 | Deliverable D4 | None past 1,000 views, as for 42.2% of PB1's cohort | https://vidiq.com/research/youtube-first-10-videos-study/ | PASS | 100 - 57.8 = 42.2 |
| 47 | Deliverable D4 | New thumbnail "at most four words, in her colours (PB5 §7)" | others/PB5 §7, §8 | FAIL | §7 rule 2 sets the four words; the colour rule is §8 ("text is white or cream on a near-black or teak band"). Section pointer; erratum PB10-1. Minor |
| 48 | Deliverable D4 | Thumbnail change "in place of the two whole-piece views from the taped mark, as found and finished, that PB5 §7 rule 1 set" | others/PB5 §7 rule 1; case-facts.md PB10 entry | PASS | PB5 §7 rule 1: "usually the as-found and finished views from the taped mark side by side". Run-1 flag 8 no longer applies |
| 49 | Deliverable D5 | "YouTube answer 141805 finds no correlation between break length and change in views"; "three or more times" (PB1 §6) | https://support.google.com/youtube/answer/141805?hl=en ; https://air.io/en/audience-growth/does-posting-more-on-youtube-help-we-studied-18000-channels-to-find-out | PASS | as above |
| 50 | §1 | PB6 D2, PB7 D2, "What the rows do not tell her" | others/PB6, PB7 | PASS | heading present in both |

Run 1's rows 13–75 that rest only on other units, the register or the unit's own arithmetic (its 60 internal PASS rows) were not re-run one by one and are not recounted in this run's totals. Re-read here: every passage Audit 4 changed (§4's last sentence, §5's first paragraph, D4's verdict), the internal quotations listed above, and the statistics of §3 and D3–D4 (recomputed).

## Attribution pass

Every quotation, every "X says / reports / according to X" and every Sources title, each against its page. Rows marked A are in the tables above under the number given; the Sources titles follow.

| Item | Section | Verdict | Row |
|---|---|---|---|
| A | §2 | PASS | sample 2: Watch hours only from "long-form videos that you've set to public"; not private, unlisted, |
| A | §4 | PASS | sample 4: Buffer's I4 is an increment over weeks with no posts: "points added to the weekly growth r |
| A | §5 | PASS | sample 5: "Not returned if the IG User has less than 100 followers"; follows and unfollows likewise |
| A | §7 | PASS | sample 7: Regression to the mean "happens when unusually large or small measurements tend to be foll |
| A | §8 | PASS | sample 8: 1,000 US and UK creators: 52% burnout, 37% considering leaving |
| A | §9 | PASS | sample 9: Google 2023: two years' inactivity; "We do not have plans to delete accounts with YouTube  |
| A | Deliverable D4 | PASS | sample 10: Low CTR with fewer impressions than usual is the case YouTube names for a title or thumbna |
| A | Sources | PASS | sample 12: Newman, letter, JAMA 274(13), 4 Oct 1995, 1013; credits Hanley and Lippman-Hand (JAMA, 198 |
| A | §2 | PASS | 13: Todd Beaupré, senior director of growth and discovery: "maybe a 10% or less"; PPC Land, 2  |
| A | §2 | PASS | 14: PB1's band medians: +0.5 (1-99) and +1.4 (100-499) subscribers a month |
| A | §3 | PASS | 15: NIST §7.2.4.1: Wilson interval's worth "does not strongly depend upon the value of n and/o |
| A | §3 | PASS | 16: NIST §7.2.4.1: limits may not be accurate enough "if the number of failures is very small  |
| A | §3 | PASS | 17: NIST §1.3.6.6.19: Poisson "is used to model" events in a time interval; standard deviation |
| A | §3 | PASS | 18: NIST Dataplot: "the test statistic for the sign test follows a binomial distribution with  |
| A | §3 | PASS | 19: Binomial formula in NIST §1.3.6.6.18 |
| A | §4 | PASS | 22: Y2: half of channels and videos between 2% and 10% click-through |
| A | §4 | unverifiable | 30: PB1's earlier Q3 wording: "with the 0.36-a-week illustration (I4)" |
| A | §4 | PASS | 31: PB1 D3's Q3 line and PB7's IG8 column were corrected on 13 Nov 2026 and now read this way |
| A | §5 | unverifiable | 32: PB1's earlier wording: "that fortnight's publishing-and-replies line" (PB1 D2); PB4 D1 G r |
| A | §5 | PASS | 33: Buffer's within-account estimates: +0.12% at 1-2 posts against +0.26% at 3-5 |
| A | §5 | PASS | 34: YouTube 9101241: thresholds "are not published"; "Not enough demographic data" |
| A | §5 | PASS | 35: YouTube 141805: "We studied thousands of channels that took a break and found no correlati |
| A | §5 | PASS | 36: AIR Media-Tech: dark 14+ days three or more times a year goes with fewer views per video;  |
| A | §5 | unverifiable | 37: PB4 §1's earlier wording: "If her log shows pieces averaging more than two weekends" |
| A | §5 | PASS | 38: PB2: five strangers, ten minutes, four of five; conventions (PB2 §3, D5) |
| A | §5 | PASS | 39: PB8 clause 10 and its five pre-mortem questions (PB8 D1, D2) |
| A | §7 | PASS | 40: Kohavi et al. 2009: controlled experiments are "the best scientific design for establishin |
| A | §7 | PASS | 41: Test & Compare is computer-only and may return "Not enough impressions" or "Inconclusive"  |
| A | §6 | PASS | 42: Verdict 3 reads the anchor platform, "whose two numbers YouTube itself documents" |
| A | Deliverable D1 | FAIL | 43: AU2: Studio, Audience, "Channels your audience watches" |
| A | Deliverable D1 | PASS | 44: YT5: 50% "above typical" list (PB6 YT5) |
| A | Deliverable D3 | PASS | 45: PB3's "on Instagram, mainly under 50" |
| A | Deliverable D4 | FAIL | 47: New thumbnail "at most four words, in her colours (PB5 §7)" |
| A | Deliverable D4 | PASS | 48: Thumbnail change "in place of the two whole-piece views from the taped mark, as found and  |
| A | Deliverable D5 | PASS | 49: "YouTube answer 141805 finds no correlation between break length and change in views"; "th |
| A | §1 | PASS | 50: PB6 D2, PB7 D2, "What the rows do not tell her" |

| Sources title | URL opened | Verdict | Note |
|---|---|---|---|
| Barnett, van der Pols and Dobson, "Regression to the mean: what it is and how to deal with it", IJE 34(1), 2005, 215-220, PubMed 15333621 | https://pubmed.ncbi.nlm.nih.gov/15333621/ | PASS | title, journal, year, volume, issue, pages confirmed; the fetched text did not show the authors' names |
| Kohavi, Longbotham, Sommerfield and Henne, "Controlled experiments on the web: survey and practical guide", DMKD 18(1), 2009, 140-181 | https://exp-platform.com/journal-survey | PASS |  |
| Meta for Developers, "Instagram account insights" | https://developers.facebook.com/docs/instagram-platform/api-reference/instagram-user/insights | PASS | page title "Instagram Account Insights" |
| Newman, "If almost nothing goes wrong... Interpreting small numerators", letter, JAMA 274(13), 4 Oct 1995, 1013 | https://jamanetwork.com/journals/jama/article-abstract/389714 | PASS | counted as sampled claim 12 |
| NIST, Dataplot Reference Manual, "Sign test" | https://itl.nist.gov/div898/software/dataplot/refman1/auxillar/signtest.htm | PASS |  |
| NIST/SEMATECH §1.3.6.6.18, "Binomial distribution" | https://itl.nist.gov/div898/handbook/eda/section3/eda366i.htm | PASS |  |
| NIST/SEMATECH §1.3.6.6.19, "Poisson distribution" | https://itl.nist.gov/div898/handbook/eda/section3/eda366j.htm | PASS |  |
| NIST/SEMATECH §7.2.4.1, "Confidence intervals" | https://itl.nist.gov/div898/handbook/prc/section2/prc241.htm | PASS |  |
| NIST/SEMATECH §7.2.4.2, "Sample sizes required" | https://itl.nist.gov/div898/handbook/prc/section2/prc242.htm | PASS |  |
| TechCrunch, "YouTube will no longer be deleting videos from inactive accounts", 18 May 2023 | https://techcrunch.com/2023/05/18/youtube-will-no-longer-be-deleting-videos-from-inactive-accounts | PASS |  |
| YouTube Help, "The YouTube Partner Programme overview and eligibility" (answer 72851) | https://support.google.com/youtube/answer/72851?hl=en-GB | PASS |  |
| YouTube Help, "Understand limited data in YouTube Analytics" (answer 9101241) | https://SUPPORT.GOOGLE.COM/youtube/answer/9101241 | PASS | title right; host in capitals (errata PB10-2, PB10-3) |
| YouTube Help, "YouTube performance FAQ & troubleshooting" (answer 141805) | https://support.google.com/youtube/answer/141805?hl=en | PASS | page: "YouTube performance FAQ & Troubleshooting" |

Attribution stratum: 45 items; FAIL 2 (both minor: a section pointer and a quoted report name), unverifiable 3 (three quotations of other units' wording as it stood before 13 Nov 2026, which the folder no longer holds). Every quotation from an outside page is exact.

## Not checked

- https://support.google.com/youtube/answer/12843009: not returned by any search in this agent, so not fetched (PB1's source for rows Y10, Y11; a secondary page agrees)
- https://creators.instagram.com/earn-cash-making-what-you-love: not searched (PB1's source for row I6; outside the sample and the run-1 list)
- Hanley and Lippman-Hand, JAMA 1983, full text: not opened (bibliographic record only)
- Newman's JAMA letter: abstract excerpt only; the rest of the letter is behind the publisher's wall
- No search or fetch was refused for budget or permission. One note on a fetch: `https://support.google.com/youtube/answer/13861714` (returned by search as "Test & compare thumbnails") served the page "A/B test titles & thumbnails", the page PB6 cites as answer 16391400; it was read as served.

## Failure rate

- Sample: 12 claims. PASS 12, FAIL 0, STALE 0, unverifiable 0. Failure rate 0 of 12 (0%); the full audit is not triggered.
- All claims checked in this run: 62. PASS 56, FAIL 2 (both minor, both outside the sample), STALE 0, unverifiable 4.

## Counts

- Words (`wc -w unit.md`): 12,916. `##` sections: 12.
- Cited claims in the whole unit: **171**. Counted by `out/count_claims.py` (every sentence or table row outside the `viz` blocks that carries a link, a unit pointer, a Help answer number, the handbook or a PB1 row code: 222 candidates, in `out/claim_candidates.json`), then read one by one: 51 removed that state no claim (front matter, templates, Sources and Unsure lists: 17; method statements, lead-ins, cross-references, procedure steps, her-rule lines and sentence fragments split from a counted sentence: 34). Run 1 counted 173 before Audit 4's edits, by a slightly different rule.

| Section | Candidates | Cited claims |
|---|---|---|
| Opening | 4 | 1 |
| §1 | 8 | 7 |
| §2 | 6 | 6 |
| §3 | 12 | 9 |
| §4 | 19 | 16 |
| §5 | 38 | 30 |
| §6 | 12 | 11 |
| §7 | 5 | 4 |
| §8 | 10 | 8 |
| §9 | 7 | 7 |
| D1 | 37 | 35 |
| D2 | 7 | 2 |
| D3 | 16 | 13 |
| D4 | 13 | 13 |
| D5 | 11 | 9 |
| Front matter, Templates, Sources, Unsure list | 17 | 0 |
| **Total** | **222** | **171** |

## Figures

1. `range`, §3: five labels and ten bounds match the table and were recomputed (1.50–5.93, 1.83–4.89, 2.11–4.25, 2.34–3.84, 2.56–3.51); the caption's handbook section is right. **PASS.**
2. `compare`, §3: 99.7, 59.7, 3.3 match the table and the recomputation; 0.0 stands for 0.02%, and the caption says so. **PASS.**
3. `matrix`, §5: every cell traces to §5, D2 or D5 (0.75 h, 5 min, 3 min, annual page, packaging hour, three reply slots, two Reels fewer). **PASS.**
4. `flow`, D2: seven steps, minutes and row codes match D2 steps 1–7. **PASS.**

No figure needs a fix.

## Deliverable

- Exists in full: D1 (the sheet, five blocks), D2 (the sixty-minute procedure), D3 and D4 (Mara's Q1 and Q2), D5 (the annual page), T1–T4.
- Follows from the unit's evidence: verdict 3's count rests on §3's binomial table (recomputed); the packaging choice in D4 rests on YouTube Help 16559651, which says what the unit says it says.
- Mara's facts agree with `case-facts.md` (PB10 entry: review hours, admin hours, T1, sales, list, clamp, verdicts, year-two dates). Run 1's contradiction with PB5 (flag 8) is gone: D4 now replaces the two whole-piece views PB5 §7 rule 1 set.
- Usable without the unit: yes for D2–D5 and the templates; D1 leans on the body in four cells, each a pointer to a reason.
- Open: the R6 line that calls 1.7% the lowest CTR beside a 1.6% row (PB10-4); the colour pointer (PB10-1); the report name in AU2 (PB10-6).

## Course goal and sourcing standard

- Course goal: the unit delivers the third outcome (reading the two platforms' numbers against sourced benchmarks each quarter to decide whether to continue, change format or stop).
- Advice without evidence: none found. Each rule no source sets is marked "her rule".
- "Words in quotation marks are the source's exact words": met for every outside quotation (each checked at its page); not met in one UI label (PB10-6, PB10-7). Three quotations of earlier wording in PB1 and PB4 are labelled as such and cannot be checked from the folder.
- "The unit leaves its sources": the closing line of Sources is incomplete and YouTube Help 16559651 is listed nowhere (PB10-5); one URL's host is in capitals (PB10-2, PB10-3).
- Dates: all thirteen sources carry "checked 13 Nov 2026" or a publication date; all thirteen opened on 15 Nov 2026 and say what the unit says.

## Verdict

**PB10: PASS.** 0 FAIL in 12 sampled claims, each opened at its source; no full audit run. Seven minor errata, no flag. The qualification on run 1's PASS (no outside source opened) is lifted: all thirteen listed sources and eighteen further pages behind the carried figures were opened.

Run-1 errata re-verified against `unit.md` as it stands:

- Run-1 PB10-1 (§4, PB1's Q3 wording): dropped. Audit 4 added the sentence saying PB1 and PB7 were corrected and the quoted words are earlier wording; the run-1 Current no longer occurs.
- Run-1 PB10-2 (§5, the review's hour): dropped. Audit 4 rewrote the sentence ("PB1 first took...; both were corrected on 13 Nov 2026"); the Current no longer occurs.
- Run-1 PB10-3 → PB10-1 here: holds.
- Run-1 PB10-4 → PB10-2: holds.
- Run-1 PB10-5 → PB10-3: holds.
- Run-1 PB10-6 → PB10-4: holds.
- Run-1 PB10-7 → PB10-5: holds.
- Run-1 PB10-8 (flag, D4 thumbnail against PB5 §7): dropped. Audit 4 rewrote D4's change as a close frame of the fault beside the finished piece, in place of the two whole-piece views PB5 §7 rule 1 set; the Current no longer occurs and the contradiction is gone.
- New in part 2: PB10-6 and PB10-7.

## The most consequential errors

None of consequence. The three largest, all minor:

1. D4's R6 line calls upload 11's 1.7% the quarter's lowest click-through while the table beside it shows upload 13 at 1.6%; the line is right only because upload 13 is under 28 days old, which it does not say (PB10-4).
2. The Sources closing line names four units as the origin of carried figures where the unit carries from nine, and YouTube Help 16559651, on which D4's packaging choice rests, is listed nowhere (PB10-5).
3. The quoted Studio report name in AU2 is not the name on YouTube's Help page or in PB3 (PB10-6, PB10-7).

## Bibliography line

No new source to add and none to mark failed; PB10's thirteen sources all re-opened on 15 Nov 2026 and confirmed; normalise `https://SUPPORT.GOOGLE.COM/youtube/answer/9101241` to lower case so it merges with PB3's entry; note that PB10 D4 also cites YouTube Help 16559651 (already listed through PB1 and PB6).

## Changelog line

2026-11-15 · Audit 3 part 2, PB10 · claude-fable-5-2 (fresh isolated agent, search on: 31 searches, 31 fetches) · run 1's sample of 12 re-checked at source: 12 PASS, 0 FAIL; 62 claims checked in all: 56 PASS, 2 FAIL (minor), 0 STALE, 4 unverifiable; attribution pass run; verdict PASS; 7 minor errata (5 carried from run 1, 2 new), 0 flags; run-1 errata 1, 2 and flag 8 dropped as fixed by Audit 4; figures 4 of 4 PASS.

## Errata

**PB10-1** · minor · FAIL · Deliverable D4, Verdict
- Current: `in her colours (PB5 §7)`
- Fix: `in her colours (PB5 §7, §8)`
- Basis: others/PB5: §7 rule 2 sets the four-word limit; the colour rule is §8 ("text is white or cream on a near-black or teak band"); case-facts.md, PB5 entry. No URL: a unit of this course. Run-1 erratum 3, carried over.

**PB10-2** · minor · other · §5, PB3
- Current: `[YouTube Help, Understand limited data in YouTube Analytics, answer 9101241](https://SUPPORT.GOOGLE.COM/youtube/answer/9101241)`
- Fix: `[YouTube Help, Understand limited data in YouTube Analytics, answer 9101241](https://support.google.com/youtube/answer/9101241)`
- Basis: The host is in capitals; others/PB3 D1 cites the same page as https://support.google.com/youtube/answer/9101241, so a bibliography collected by URL lists it twice. The page opened on 15 Nov 2026 and its title and both quotations are right. Run-1 erratum 4, carried over.

**PB10-3** · minor · other · Sources
- Current: `checked 13 Nov 2026. https://SUPPORT.GOOGLE.COM/youtube/answer/9101241`
- Fix: `checked 13 Nov 2026. https://support.google.com/youtube/answer/9101241`
- Basis: As PB10-2, the same URL in the Sources list; others/PB3 D1 gives https://support.google.com/youtube/answer/9101241. Run-1 erratum 5, carried over.

**PB10-4** · minor · other · Deliverable D4, YouTube, R6
- Current: `Lowest CTR, upload 11 (1.7%);`
- Fix: `Lowest CTR among them, upload 11 (1.7%; upload 13's 1.6% is lower but the upload is under 28 days old);`
- Basis: Unit D4 table: upload 13 reads 1.6% and is 13 days old on 5 Jul 2027; others/PB6 D1 R6 (at least 28 days old, lowest CTR of the quarter). No URL: internal. Run-1 erratum 6, carried over.

**PB10-5** · minor · other · Sources, closing line
- Current: `PB1 D1 (Y1–Y12, I1–I7, B1–B2), PB1 §2, §4 and §6, PB6 D1–D2, PB7 D1–D2, PB9 D2–D5;`
- Fix: `PB1 D1 (Y1–Y12, I1–I7, B1–B2), PB1 §2, §3, §4, §6 and §8, PB1 D2–D3 (which carries YouTube Help 16559651), PB2 §3 and D5, PB3 §4 and D1–D2, PB4 §1 and §4–§7, PB5 §7–§9, PB6 §3 and D1–D2, PB7 §9 and D1–D2, PB8 D1–D3, PB9 §8 and D1–D5;`
- Basis: The unit also rests figures and rules on those sections; sourcing standard Part 1, 'The unit leaves its sources'. YouTube Help 16559651 (https://support.google.com/youtube/answer/16559651?hl=en, opened 15 Nov 2026) is cited in D4 by number only and listed nowhere in Sources. Run-1 erratum 7, carried over.

**PB10-6** · minor · FAIL · Deliverable D1, Block D, AU2
- Current: `Studio, Audience, "Channels your audience watches"`
- Fix: `Studio, Audience, "Channels that your audience watches"`
- Basis: YouTube Help, Understand your YouTube audience, https://support.google.com/youtube/answer/9314416 (opened 15 Nov 2026) names the report "Channels that your audience watches"; others/PB3 D1 trait 9 quotes it so. New in part 2 (attribution pass).

**PB10-7** · minor · FAIL · Unsure list
- Current: `The YouTube Studio app path to "Channels your audience watches" was not confirmed in the app (D1 AU2).`
- Fix: `The YouTube Studio app path to "Channels that your audience watches" was not confirmed in the app (D1 AU2).`
- Basis: As PB10-6, the second occurrence: https://support.google.com/youtube/answer/9314416.

Working files left in `out/`: `sample.md`, `count_claims.py`, `claim_candidates.json`, `build.py`.
