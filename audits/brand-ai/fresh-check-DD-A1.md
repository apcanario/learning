---
audit: fresh check
unit: DD-A1 · Deep dive: five creators who did this
course: brand-ai · A · Building a Marketable Personal Brand
model: Opus 5.5 (search on; a Fable 5.1 fresh check is owed, deferred by Pedro 31 Oct 2026 to the Fable stage)
date: 2026-11-02
chat: own Opus 5.5 agent context, not shown the writing or the writer's report (P31), in session https://claude.ai/code/session_01KMmgR2JHHbRJ1y4AhNmTNi
verdict: fix · 3 errors (four entries, two of them one fact in two places), 6 should-fix, 6 minor; against filed units: A9 1 should-fix and 1 minor, A1 1 minor
---

# Fresh check · DD-A1 · Deep dive: five creators who did this

The checker's final report follows verbatim, extracted by script from its hand-back (its `SubagentHandback` message). A first checker agent was launched with the §3b prompt missing (the orchestrating chat sent two unfilled placeholders); it was stopped within its first step, before it reported, and this second, fresh agent was given the prompt in full.

**Fresh check of DD-A1 by Opus 5.5. A Fable 5.1 fresh check is still owed: the course owner deferred Fable 5.1 checks to the Fable stage on 31 Oct 2026, and this report does not replace that check.**

## Read first
- I confirmed with `diff` that the check copy `/tmp/claude-0/-home-claude/39706f3e-940f-5a6f-82bf-d3661dae8679/scratchpad/check/DD-A1-check-copy.md` matches `/home/claude/learning/courses/brand-ai/DD-A1-deep-dive-five-creators-who-did-this.md` exactly. I read all 403 lines.
- `docs/sourcing-standard.md`, Parts 1 and 2.
- The brief, built by script: `PRE` with `{GOAL}` replaced by `GOAL_A`, a blank line, then the fifth field of DD-A1's entry in `hub.COURSES[0]['units']`.
- `audits/brand-ai/audit-1.html` and `audit-2.md`, read for errata that touch these creators. These were applied: Enkamp's "fifteen years" is not repeated, Boyd's count uses vidIQ beside Social Blade, and ADHD Chatter's National Diversity Awards text is labelled.
- The filed units A1 (§2, §3, §5, unsure list), A9 (§1 to §5, §8, Deliverable 1, checkpoints), A6 (§1.3, §2.2, §3, Deliverable 1), A7 §3, and A2 §1's ADHD Chatter line.
- I opened nothing under `reports/`, `writer-packet/` or `tasks/`.

## Method
- **Web rule:** I ran WebSearch before every fetch. I fetched only URLs a search in this context returned, exactly as returned. I used no memory, Projects, connector or browser tool.
- **Redirects:** Two fetches redirected: `podcast.creatorscience.com/guests/ali-abdaal/` and `podcast.creatorscience.com/ali-abdaal/`, both to `creatorscience.com/podcast/ali-abdaal/`. I did not follow either. Every claim cited to Creator Science is therefore "unverifiable (not checked)".
- **Failed fetch:** The vidIQ HellahGood page returned no figures, so its claims are unverifiable.
- **Uniqueness check:** I checked every Current below on the check copy with `grep -F -c`. For Currents with characters that break the shell (asterisks, a leading hyphen, quote marks inside JSON) I used Python `str.count`. Every Current returns 1. The three Currents against filed units were checked the same way in A1 and A9.
- **Calculations:** I re-ran every calculation in the unit by Python script (results below).

## (1) Coverage
- **Choice of five from the brief's nine:** covered. The test is stated and the four left out are named, each with a reason.
- **Start date:** covered for all five.
- **Platform mix:** covered.
- **Cadence:** covered.
- **Hours a week:** thin. Only Abdaal has a figure, and the unit says the others are unpublished, as the evidence requires.
- **Numbers at 12, 24 and 36 months:** thin. Most points are unpublished; the unit says so and approximates nothing.
- **Breakout piece:** covered for four; Partridge is said to be unpublished.
- **What they stopped doing:** covered for four; none found for Partridge.
- **How they monetised:** covered for Abdaal and Boyd; thin for Sidibe, Lewis and Partridge.
- **What they got wrong:** covered for Abdaal and Partridge; "none found" for three.
- **Deliverable** (comparables brief with a one-page pattern summary): covered.

## (2) to (6) Findings
- [error | accuracy] §3 What he says he got wrong; Current: `and that he is bad at business administration, which an outside company now runs.`; Problem: Net Influencer says Kim handles the business side. Mike: "Paying people, getting paid, working with management at Ziggurat XYZ. Everything you don't see is what Kim's doing." No outside company runs it. This is also a public-site breach: a living creator's statement misreported. Fix: `and that he is "really bad at" the business side (paying people, getting paid, working with management at Ziggurat XYZ), which Kim handles.`; Basis: https://www.netinfluencer.com/learning-in-public-how-mike-boyd-built-a-sustainable-youtube-business-on-curiosity/ (4 Mar 2026)
- [error | accuracy] §2 Hours a week; Current: `By October 2020 he had editors and a small team, so the 5–10 hours is his share of a team's output, at three videos a week.`; Problem: Every (Sept 2020) says three a week was his last three months as a full-time doctor and that he was "down to only one or two videos a week" after leaving. In October 2020 he was on sabbatical, so "three a week" contradicts the unit's own source. Fix: `By October 2020 he had editors and a small team, so the 5–10 hours is his share of a team's output; by his account to Every in September 2020 he was then making one or two videos a week, down from three in his last three months as a doctor.`; Basis: https://every.to/superorganizers/the-double-life-of-productivitys-3842641
- [error | accuracy] §7.3 Hours (same cause as above); Current: `and it is the show's summary of a man with editors producing three videos a week (§2).`; Problem: same contradiction. Fix: `and it is the show's summary of a man with editors producing one or two videos a week (§2).`; Basis: as above.
- [error | figure] §7.3 At 24 and 36 months; Current: `This unit does not change that: of fifteen 24- and 36-month points across the five, only one is even approximately dated (Sidibe's 125,000-plus between May 2019 and January 2020), and it is a self-reported awards figure. The others are unpublished.`; Problem: five creators at two points each is ten points, not fifteen. "The others are unpublished" is also wrong: Partridge has claims in other measures at 22 and 36 months, and Abdaal has 1M at 39 months. Fix: `This unit does not change that: of the ten 24- and 36-month points across the five, no YouTube subscriber count is dated at either point; the nearest is Sidibe's 125,000-plus, taken between May 2019 and January 2020 by inference, a self-reported awards figure. Partridge's points are listener and follower claims in other measures, Abdaal's one million came at 39 months, and the rest are unpublished.`; Basis: the unit's own §2 to §6 and its table.
- [should-fix | attribution] §2 Platform mix; Current: `YouTube first; then a blog and newsletter, Skillshare classes, a cohort course (Part-Time YouTuber Academy, first run November 2020), a podcast (Deep Dive) and, by 2023, a larger team and London studio (his about page, above).`; Problem: the about page names the Part-Time YouTuber Academy (PTYA) cohort of Nov 2020, the Deep Dive podcast and a bigger team. It does not contain "studio", "Skillshare", "blog" or "newsletter". Fix: `YouTube first; then a cohort course (Part-Time YouTuber Academy, first cohort November 2020), a podcast (Deep Dive) and a larger team (his about page, above); Skillshare classes by 2020 (Summify summary, below); an email list (Kagan, below); and, by 2023, an expensive London studio, since given up (Mark Ellis, below).`; Basis: https://aliabdaal.com/?p=222 ; https://markellis.substack.com/p/two-massive-lessons-from-ali-abdaal
- [should-fix | attribution] §4 Breakout piece; Current: `His most-watched videos, in his own words, come from the 2021 Run Across America (NAZ Elite)`; Problem: the words are the NAZ Elite interviewer's question ("Some of your most-watched videos are from your Run Across America in 2021"), not Sidibe's. Public-site rule on a creator's statements. Fix: `Some of his most-watched videos, in the NAZ Elite interviewer's words, come from the 2021 Run Across America (NAZ Elite)`; Basis: https://nazelite.com/meet-hellah-sidibe/
- [should-fix | attribution] Deliverable, Sidibe (same cause); Current: `most-watched: Run Across America, 2021 (own words, NAZ Elite)`; Fix: `some of the most-watched: Run Across America, 2021 (NAZ Elite interviewer)`; Basis: as above.
- [should-fix | attribution] §6 Platform mix; Current: `A book: Sheldon Press bought *Now It All Makes Sense* in July 2024 ([The Bookseller, 2 Jul 2024](https://thebookseller.com/rights/sheldon-press-to-publish-life-changing-deep-dive-into-adhd-by-ladbible-founder-alex-partridge)), and Entrepreneur UK reported it as published on 27 February 2025`; Problem: The Bookseller does not name the title. Entrepreneur UK says "out now", which gives no publication date. Fix: `A book: Sheldon Press bought the rights to his book on ADHD in July 2024 ([The Bookseller, 2 Jul 2024](https://thebookseller.com/rights/sheldon-press-to-publish-life-changing-deep-dive-into-adhd-by-ladbible-founder-alex-partridge)), and Entrepreneur UK called *Now It All Makes Sense* "out now, published by Sheldon Press" on 27 February 2025`; Basis: The Bookseller and https://uk.entrepreneur.com/?p=1293
- [should-fix | accuracy] §4 Hours a week; Current: `so the channel's first years ran alongside other paid work; how many hours it took is not stated.`; Problem: InsideHook documents the coaching work in August 2021, about 46 months after the day-163 video. That evidence does not cover the "first years". Fix: `so in 2021, about 46 months after the day-163 video (my arithmetic), the channel ran alongside other paid work; whether it did earlier, and how many hours it took, is not stated.`; Basis: https://www.insidehook.com/article/sports/hellah-sidibe-transcontinental-run-across-america (10 Aug 2021)
- [should-fix | deliverable] Pattern 3 (same cause); Current: `**3. Other income carried the early years.** Three of five documented; one more documented without dates.`; Fix: `**3. Other income carried the early years.** Two of five documented; one more documented in the fourth year only, and one without dates.`; Basis: as above.
- [should-fix | deliverable] Pattern 3, Sidibe line (same cause); Current: `- Sidibe: soccer personal training and youth coaching in 2021 (InsideHook, 10 Aug 2021).`; Fix: `- Sidibe: soccer personal training and youth coaching in 2021, about 46 months in; earlier years undocumented (InsideHook, 10 Aug 2021).`; Basis: as above.
- [should-fix | attribution] §7.4 Instagram; Current: `Partridge *complicates* the reading of Instagram as a minor shop window`; Problem: A6 calls Instagram "the rented shop window" and never "minor". Fix: `Partridge *complicates* A6's reading of Instagram as the rented shop window beside a YouTube home channel`; Basis: A6 Deliverable 1 heading, line 251.
- [minor | figure] §2 Start date; Current: `vidIQ dates the channel itself to 20 November 2007, ten years before the first upload Kagan gives`; Problem: 20 Nov 2007 to 4 Jan 2017 is 9.1 years. Fix: `vidIQ dates the channel itself to 20 November 2007, about nine years before the first upload Kagan gives (4 January 2017)`; Basis: https://vidiq.com/youtube-stats/channel/@aliabdaal/ ; https://noahkagan.com/ali-abdaal-interview/
- [minor | attribution] §3 Hours a week; Current: `(Mike and his wife Kim, who calls them creative partners;`; Problem: "creative partner" is the article's own description, in the singular, not Kim's words. Fix: `(Mike and his wife Kim, his "creative partner" in the profile's words;`; Basis: Net Influencer.
- [minor | accuracy] §1 Ben Felton; Current: `gives "over 165,000 followers across YouTube and Instagram" combined`; Problem: the words inside the quotation marks are not the source's. Fix: `gives "more than 165,000 followers on YouTube and Instagram" combined`; Basis: https://www.gazette-news.co.uk/news/24124243.ben-running-colchester-runner-ben-felton/
- [minor | accuracy] §1 Jesse Enkamp; Current: `Black Belt's interview page gives "over 800,000" with no date`; Problem: the quotation is not the source's words. Fix: `Black Belt's interview page gives "more than 800,000 subscribers on YouTube" with no date`; Basis: https://blackbeltmag.com/full-interview-video-jesse-enkamp-and-his-massive-legacy-of-karate-nerds
- [minor | figure] §6 At 12 to 18 months; Current: `The text says one year; the page is dated 18 months after the first episode (my arithmetic).`; Problem: 20 Mar 2023 to 4 Sep 2024 is 17.5 months. Fix: `The text says one year; the page is dated about 17½ months after the first episode (my arithmetic).`; Basis: Pod Engine; National Diversity Awards page.
- [minor | accuracy] §7.4 Long-form compounds; Current: `Lewis also *supports* it: three of his five most-viewed videos date from 2022 and 2023`; Problem: all five of his top five date from 2022 and 2023 (15 Feb 2022, 8 Oct 2022, 27 Aug 2023, 29 Oct 2023, 13 Dec 2023). Fix: `Lewis also *supports* it: all five of his most-viewed videos date from 2022 and 2023`; Basis: https://vidiq.com/youtube-stats/channel/UC6dr32gbapkzgw_Eyr6VsJw (data 1 Nov 2026)

**Findings against filed units:**
- [should-fix | accuracy] A9 §5 (`courses/brand-ai/A9-what-to-expect-benchmarks.md`); Current: `went up on day 163 and was an instant hit, and his HellahGood channel`; Problem: CNN says it "gained traction immediately", but Skydio quotes him: "months later it started catching on". The two accounts disagree, as DD-A1 §7.3 says. Fix: `went up on day 163 and, in CNN's account, gained traction at once (a Skydio post of 24 February 2021 has him say it caught on months later; DD-A1 §4), and his HellahGood channel`; Basis: https://skydio.com/blog/skydio-featured-flyer-get-to-know-hellah-sidibe
- [minor | accuracy] A9 §5; Current: `began posting training videos during lockdown (the article gives no year)`; Problem: true of the Gazette, but a dated source now gives the year. Fix: `began posting training videos during lockdown (the article gives no year; Zwift Insider, 21 Sep 2026, dates it to the 2020 lockdown: DD-A1 §1)`; Basis: https://zwiftinsider.com/ben-felton/
- [minor | coverage] A1 §5 (`courses/brand-ai/A1-positioning-the-journey-as-a-format.md`); Current: `How the five, or any of the similar channels listed in DD-A1's brief, grew month by month and what they stopped doing is DD-A1's job; Mike Boyd and Goal Guys are on that brief's list.`; Problem: the pointer still reads true, but DD-A1 found no month-by-month series for Boyd and left Goal Guys out. Fix: `How the five, or any of the similar channels listed in DD-A1's brief, grew month by month and what they stopped doing is DD-A1's job; Mike Boyd and Goal Guys are on that brief's list. DD-A1 (2 Nov 2026) covers Mike Boyd (no month-by-month series found; counts agree with the table above, vidIQ 28 Oct 2026) and leaves Goal Guys out (two people; no dated growth source found).`; Basis: DD-A1 §1, §3.

**(3) Figures:** every number in the unit says whose figure it is (vidIQ, OutlierKit, the creator's own account, press, or a third-party summary), with its date.

**(4) Labels:** creator cases are labelled anecdote and survivors (intro, §7.3, Deliverable). vidIQ and OutlierKit are labelled as vendors. Summify and Recall are labelled as third-party summaries. Mark Ellis is labelled secondary. Nomination and speaker texts are labelled self-reported. The A9 data is carried with A9's correlational labels. No label is missing beyond the attribution findings above.

**(5) Deliverable:** present in full. It has the pattern summary (five patterns, each with a count), a five-at-a-glance table, a matrix and a profile per creator. It follows from the evidence, except pattern 3's Sidibe line and the two "three videos a week" lines (findings above). It can be used on its own and is explicitly not a benchmark.

**(6) Errata:** applied, as listed under Read first.

## (7) Figures
1. **line**, §5: PASS. The values 262/343/392/400 and their months are on line 120 ("Subscribers rose from 262,000 (October 2023) to 343,000 (October 2024), 392,000 (October 2025) and 400,000 (September 2026)"). The caption names §5, vidIQ and the data date. A line suits a trend.
2. **timeline**, §7.1: PASS. Every event traces to the text:
   - "by 11 Nov 2015" kickflip: line 63.
   - 15 May 2017 and 24 Oct 2017: line 85.
   - June 2017: line 37.
   - June 2018 iPad video: line 53.
   - 11 Sep 2018: line 110.
   - 15 Feb 2022: line 126.
   - 20 Mar 2023: line 136.
   - Junior doctor span 2018–2020: line 55.

   The caption names the sections and sources. A timeline suits dated events. The June 2018 date rests on Creator Science, which I could not verify.
3. **compare**, §7.1: PASS. The values come from lines 51 (6.7M), 71 (2.93M), 150 (408,000), 202/277 (399,000) and 98 (294,000). The caption names the tracker and date for each. A compare suits numbers set side by side.
4. **matrix**, Deliverable: FIX. The Partridge "Got wrong" cell is marked "partial", but the text documents a statement about his earlier businesses, which fits none of the legend's meanings. The caption also says "the brief's items" while the matrix shows five of them. A matrix suits items by sections.
   - Caption Current: `"caption": "Which of the brief's items a source opened in this unit documents for each creator. §2 to §6; 'partial' means an approximate date, a figure in another measure or a secondary or summary source."`
   - Caption Fix: `"caption": "Which of five of the brief's items (hours a week, the 12-, 24- and 36-month numbers, and what they say they got wrong) a source opened in this unit documents for each creator. §2 to §6 and the deliverable's table; 'partial' means an approximate date, a figure in another measure, a secondary or summary source, or a statement about earlier work."`
   - Legend Current: `{"mark": "partial", "means": "approximate date, another measure, or a secondary source", "tone": 4}`
   - Legend Fix: `{"mark": "partial", "means": "approximate date, another measure, a secondary source, or a statement about earlier work", "tone": 4}`

## Calculations (re-run by script)
- Day 163 of a streak from 15 May 2017 (day 1): 24 Oct 2017. PASS.
- Day 730: 14 May 2019, consistent with "730 consecutive days in May". PASS.
- Day 3,350: 16 Jul 2026, consistent with "past 3,350 days in September 2026". Tenth anniversary in May 2027. PASS.
- Boyd views: 476,918,067 − 476,842,692 = 75,375, over 11 days. PASS.
- Boyd upload rate: 197 / 11 = 17.9 a year (17.97 from 11 Nov 2015), "about 18". PASS.
- Sidibe upload rate: 479 over 5 Dec 2016 to 1 Nov 2026 = 48.4 a year, "about 48". PASS.
- Lewis upload rate: 514 over 11 Sep 2018 to 31 Oct 2026 = 63.2 a year, "about 63". PASS.
- Abdaal channel created 20 Nov 2007, first upload 4 Jan 2017: 9.1 years. The unit says "ten years". FAIL (minor finding).
- Abdaal 1M (Sep 2020) counted from June 2017: 39 months. PASS.
- Abdaal ~4,000 at March 2018: 9 months. PASS.
- Abdaal ad share: £106,950 / £1,013,000 = 10.6%, "about a tenth". PASS.
- Abdaal 2022: $4,600,593 − $2,527,356 = $2,073,237. PASS.
- Abdaal 2026 growth: 20,000 / 6.6M = 0.30% (range 0.15–0.45%), "about 0.3%". PASS.
- Sidibe 276K (22 Sep 2022) from 24 Oct 2017: 58.9 months, "59". PASS.
- Sidibe 264K (10 Aug 2021): 45.5 months, "~46". PASS.
- Sidibe Shorty window (May 2019 to 21 Jan 2020): 18.2–26.9 months, "about 19 to 27". PASS (approximately).
- Lewis 262K (end Oct 2023) from 11 Sep 2018: 61.7 months, "61". PASS.
- Lewis yearly gains: 262→343 (+81K), 343→392 (+49K), 392→400 (+8K). Monthly gain Dec 2023→Jan 2024: +11K. From Feb 2026: 0–1K a month, 0 in Jul–Sep. PASS.
- Lewis Kipchoge videos, 15 Feb 2022 to 13 Dec 2023: 21.9 months, "22". PASS.
- Partridge, months from 20 Mar 2023:
  - National Diversity Awards (4 Sep 2024): 17.5 months. The unit says "18". Minor finding.
  - BusinessCloud (19 Jan 2025): 22.0. PASS.
  - Pod Engine snapshot (15 Sep 2025): 29.8, "~30". PASS.
  - Thinking Digital (23 Mar 2026): 36.1, "36". PASS.
- OutlierKit channel age 4.6 years back from 21 Sep 2026: about 14 Feb 2022, "early 2022". PASS.
- Partridge Instagram against YouTube: 1M / 408K = 2.45, "more than twice". PASS.
- Boyd Courier figure (3 Nov 2021) from Nov 2015: 6.0 years, "six years in". PASS.
- "Fifteen" 24- and 36-month points: actually 5 × 2 = 10. FAIL (error finding).
- OutlierKit Boyd data (11 Jul 2026) to the read date: about 3.7 months, "about four months". PASS.

## Public-site rules
- Names, handles, dates and numbers: all come from opened sources and are dated. Exceptions: the Creator Science items and the HellahGood vidIQ figures, which I could not verify.
- Figures stated by a creator or third party: labelled whose they are.
- Numbers not found: said to be unpublished. None is estimated as if found.
- What living creators say they got wrong:
  - Abdaal's Every quote: verified. His Creator Science quote: unverifiable.
  - Partridge's "short-term dopamine": verified.
  - The 2023 cuts: correctly kept out of Abdaal's own words.
  - Breaches found: Sidibe's "own words" (should-fix) and Boyd's "outside company" (error), both above.
- Reader: no personal fact beyond the brief (5–7 hours a week, a running journey, ADHD in public, a job held). The employer is not named.
- Private persons: none named. Kim Boyd is named and quoted in the Net Influencer profile as his creative partner. Sidibe's fiancée is not named.

## Pointers
1. **A1 §5:**
   - Boyd: answered. DD-A1's vidIQ 2.93M · 197 · 476,918,067 (28 Oct 2026) agrees with A1's Social Blade 2.93M · 197 · 476,842,692 (17 Oct 2026) and with A1's own unsure item 8. DD-A1 adds OutlierKit's downward trend in recent views.
   - Goal Guys: not answered. The unit says so by name and gives its reasons. Goal Guys' vidIQ page was not returned by my search either.
   - A1's text still reads true; a minor addition is proposed above.
2. **A9:**
   - 12 months: DD-A1 agrees with Deliverable 1 and rows 1, 5 and 7, and names its creators as the survivor cases A9 §1 warns about (§7.3, Deliverable).
   - 24 and 36 months: it agrees that A9 rows 8 and 10 and §4/§5 have no sourced duration. Its "fifteen points" arithmetic is wrong (error above).
   - Corrections to A9 §5 by name: Sidibe's "instant hit" holds as a dispute (should-fix against A9 proposed). Felton's year holds (minor against A9 proposed).
   - Lewis's figures (399K, 514, −1,000) still agree. vidIQ's window has rolled to 5 Oct–1 Nov 2026, still −1,000.
   - Sidibe's 294K: unverifiable this pass, because the vidIQ page returned nothing.
3. **A6:**
   - §1.3 long-form compounds; YouTube rule 6; rule 7 (correctly "not tested"); §1.3 point 3 (Shorts watch hours); §2.2 rented reach; Substack rule 1 (the owned list): each is named and applied fairly.
   - One exception: the word "minor" is not A6's (should-fix above).
4. **Other pointers:**
   - A7 §3 does use Enkamp for a gi brand beside a channel. PASS.
   - A1 §2's working claim is quoted accurately. PASS.
   - A1 §3's "karate was season one" season label. PASS.
   - A9 "cut the load" verdict (episode shorter before cadence slips, line 287). PASS.
   - A2 §1's ADHD Chatter figures (408,000, 83,300, 1.2 a week, OutlierKit 21 Sep 2026) agree with DD-A1.

## Confirmed
**Ali Abdaal**
- vidIQ Abdaal: 6.7M, 1,503 videos, created 20 Nov 2007, 2026 monthly gains 10–30K, no change 5 Oct–1 Nov 2026 (https://vidiq.com/youtube-stats/channel/@aliabdaal/).
- About page: started 2017 as a Cambridge student; 100K "in 2018"; 1M Sep 2020; 2M Jul 2021; 3M Jun 2022; 4M Apr 2023; junior doctor 2018–2020; left medicine for good; PTYA cohort 1 Nov 2020; Deep Dive podcast (https://aliabdaal.com/?p=222).
- Kagan: guitar cover 4 Jan 2017; medical content from June 2017 on a phone; 130,000+ email subscribers; started narrow then widened; email list as backup. Dated 25 Jan 2022 (https://noahkagan.com/ali-abdaal-interview/).
- Every: three videos a week in his last three months as a doctor, one or two after; "I thought I'd be way more productive than I've been so far". The page shows 24 Sep 2020; its metadata says 23 Sep (https://every.to/superorganizers/the-double-life-of-productivitys-3842641).
- Mark Ellis, 18 Aug 2023: London studio, staff reduced, PTYA version ended, heard on The Colin and Samir Show (https://markellis.substack.com/p/two-massive-lessons-from-ali-abdaal).
- Podwise: episode title, 14 Aug 2023, no notes (https://podwise.ai/episodes/1469618).
- Recall: "after nearly 5 years", undated (https://www.recall.it/summary/ali-abdaal/my-take-on-quitting-youtube).
- Summify, 2020 video (28 Dec 2020): AdSense £1 / £12,329 / £33,186 / £106,950; total about £1,013,000; Skillshare £350,000; PTYA £220,000; the internal disagreements are as the unit says (https://summify.io/discover/how-much-money-i-earn-as-a-doctor-youtuber-VTTp5A/).
- Summify, 2022 video (5 Jan 2023): revenue $4,600,593, costs $2,527,356, profit $2,073,237, 2021 profit $2,525,714, Skillshare down "due to pricing changes" (https://summify.io/discover/how-much-money-i-made-as-a-youtuber-entrepreneur-2022-KvDHMe/).
- Build, 24 Feb 2023: 50,000 in a year; 1,000 after six months and 52 videos; vlogging from 1 Aug 2018; 5,000 by March 2018; the internal conflict holds (https://thehustlers.substack.com/p/special-edition-turning-a-side-hustle).

**Mike Boyd**
- vidIQ Boyd: 2.93M, 197 videos, 476,918,067 views, created 23 Oct 2008, no change 30 Sep–27 Oct 2026 (https://vidiq.com/youtube-stats/channel/@mikeboyd/).
- OutlierKit Boyd, 11 Jul 2026: 2.9M, 196 videos, 475.7M views, 2.4M average, 0.3 a week, last upload 31 days before, 86/14 long-form/Shorts, 90% evergreen, downward trend tied to climbing content, Dotted Lines 15.0M (https://outlierkit.com/channel/mikeboyd).
- Net Influencer, 4 Mar 2026: kickflip filmed to learn editing during his master's thesis; "people resonated with the first video I put up"; Mike Boyd Climbs launched "three years ago"; no TikTok; both quit their jobs; an editor; "There wasn't a grind to 10,000 subs"; the production-company quote; "mood over work"; agent; gambling and alcohol refused; photographer (https://www.netinfluencer.com/learning-in-public-how-mike-boyd-built-a-sustainable-youtube-business-on-curiosity/).
- MetaFilter, 11 Nov 2015: "five hours and forty-seven minutes" (https://www.metafilter.com/154630/Gladwell-eat-my-shorts).
- The Courier: "a following of 2.7 million people". The date is not shown on the fetched page (unverifiable) (https://thecourier.co.uk/fp/news/dundee/2700738/mike-boyd-dundee-youtube-campaign).

**Hellah Sidibe**
- CNN via ABC17, 22 Sep 2022, George Ramsay: 15 May 2017 start; 10 minutes a day for two weeks; day-163 video "why I run every day" at his fiancée's urging; gained traction immediately; about 276,000 subscribers; outdoors and at least two miles; 14 miles a week because of shin damage; "I give myself permission to quit every day" (https://abc17news.com/sports/cnn-sports/2022/09/22/when-his-hopes-of-a-soccer-career-faded-hellah-sidibe-started-running-every-day-hes-still-going-five-and-a-half-years-later/).
- Skydio, 24 Feb 2021: "months later it started catching on"; "That video launched the amazing running community I'm surrounded by today" (https://skydio.com/blog/skydio-featured-flyer-get-to-know-hellah-sidibe).
- Shorty entry: "125K+ YouTube subscribers", "20K+ followers on Instagram", "In May, he topped 730 consecutive days"; edition labels 12th/14th/19th (https://shortyawards.com/12th/hellahgood9).
- Wikipedia: 12th Shorty nominations announced 21 Jan 2020 (https://en.wikipedia.org/wiki/12th_Shorty_Awards).
- InsideHook, 10 Aug 2021, Rafael Canton: 264,000 subscribers; soccer personal training and youth coaching; 3,061 miles in 84 days from March 2021.
- NAZ Elite, undated (about early 2023): "286,000+"; "For almost 6 years I've just run in a way that felt comfortable"; coach Ben Rosario.
- BoxLife, 21 Sep 2026: "over 3,350 consecutive days"; 10th anniversary in May.
- Gymshark Central: published 1 Mar 2021, updated 16 Aug 2021; "Gymshark Athlete, Hellah Sidibe".

**Mark Lewis**
- vidIQ Lewis: created 11 Sep 2018; 399K; 514 videos; the monthly series Oct 2023–Sep 2026 as the unit gives it; top five videos with their dates and views; three of the five on the Kipchoge premise (data now 1 Nov 2026) (https://vidiq.com/youtube-stats/channel/UC6dr32gbapkzgw_Eyr6VsJw).
- YouTube Creators Hub, undated: 325,000; financial services to full-time YouTube; Casey Neistat; the bio quote; monetisation and sponsorship topics.
- Men's Fitness, 4 Jun 2026, Todd Cole: "mid-50s"; "More than one million YouTube subscribers".
- BoxLife, 26 Apr 2024: four months away from the gym, reason not given.
- Tenacity Podcast, 19 Aug 2024, Fergus Crawley: the "frustrations with social media and content creation" topic.
- Mature Muscle, S.3 Ep.9, 4 Nov 2022: @marklewispics and his own site.

**Alex Partridge (ADHD Chatter)**
- Pod Engine: first episode 20 Mar 2023; 239 episodes; hosted on Acast; 33,906,469 YouTube views at 15 Sep 2025.
- BusinessCloud, 19 Jan 2025, Chris Maguire: UNILAD 2010; LADbible 2011; diagnosed at 34; "over 500,000 listeners every month".
- OutlierKit ADHD Chatter, 21 Sep 2026: 408.0K; 815 videos; 67.9M views; 83.3K average; 1.2 a week; 4.6 years; 57% Shorts; recent uploads long-form; female-ADHD episode 758.0K.
- National Diversity Awards, 4 Sep 2024: "over 1 million neurodivergent listeners with 100,000 monthly downloads".
- Thinking Digital, 23 Mar 2026: "over 1m followers on Instagram" (the page attributes this to the podcast); "hundreds of thousands of listeners each month".
- Entrepreneur UK, 27 Feb 2025, Patricia Cullen: "I was starting them on short-term dopamine".
- The Bookseller: dated 2 Jul 2024.
- Apple Podcasts: "Updated weekly". The al storefront showed 235 episodes on 2 Nov; the unit's 233 on the nz page is unverifiable and has likely moved.

**Left-out creators**
- ThoughtLeaders, 11 May 2020: Cam and Brenden; no date, number or quote.
- Zwift Insider, 21 Sep 2026: "During the 2020 lockdown".
- Gazette: undated.
- vidIQ Enkamp: 11 Sep 2008, 1.67M, 789 videos, 1 Nov 2026.
- Black Belt: updated 31 Jan 2024.
- G.I. Jobs, 25 Apr 2019: Fort Hood; "took about 4-5 years to really start making money".

**Unverifiable (not checked)**
- Every claim cited to Creator Science (redirect). This covers: ~4,000 at nine months, the 10,000 goal, the first hundred videos, the cadence and two-a-week figures, 5–10 hours, £100,000 a month, 40–44 clinical hours, monetisation from 17 Apr 2018 at £5–15 a day, the iPad video in June 2018, and "I kind of wish I'd done that from day one".
- The vidIQ HellahGood figures: 294K, 479 videos, 5 Dec 2016, latest upload 25 Oct 2026, −1,000 in Sep 2026.
- The Courier's date.
- Apple nz's 233 episodes.

## Verdict
DD-A1 · fix · 3 errors (four entries above; the two "three videos a week" lines are one fact in two places), 6 should-fix (including the matrix figure), 6 minor. Against filed units: A9, 1 should-fix and 1 minor; A1, 1 minor.
---

**Maintainer's note (2 Nov 2026, the orchestrating chat of row A-4).** The checker's transcript was checked by script: no memory, Projects, past-chat or connector tool; every WebFetch on a URL a WebSearch in its own context had returned; the two Creator Science redirects not followed; nothing opened under the writer's packet, its report or any agent transcript. Every finding was verified before it was applied, each as an exact replacement whose Current occurred once in its file (Python `str.count`), all 23 by one script reading the pairs from this report. How each was verified:

- **Errors 1 (Boyd's business side) and minor 2 ("creative partner"):** search, then a fetch of the Net Influencer profile the search returned (4 Mar 2026): Mike says he is "really bad at that stuff" and that the unseen work, including management at Ziggurat XYZ, is Kim's; no outside company runs it; "his wife and creative partner Kim" is the article's narration. Held; applied as given.
- **Errors 2 and 3 (three videos a week in October 2020):** one fact in two places. Search, then a fetch of Every's article (24 Sep 2020): three a week in his last three months as a doctor; "down to only one or two videos a week" since. The unit's own §2 cadence paragraph already said so. Held; applied as given.
- **Error 4 (fifteen points):** the unit's own arithmetic (five creators, two points each) and its §6 (Partridge's claims at about 22 and 36 months in other measures) and §2 (Abdaal's million at 39 months). Held; applied as given.
- **Should-fix 1 (Abdaal's platform mix):** search, then a fetch of his about page: it names a website, PTYA's first cohort (November 2020), the Deep Dive podcast and a hired team; no studio, Skillshare, blog or newsletter. The replacement's other sources (Summify, Kagan, Mark Ellis) are already cited elsewhere in §2 and in the deliverable; Mark Ellis's article itself was not returned to the maintainer's search and was not re-read. Held; applied as given.
- **Should-fix 2 and 3 (Sidibe's most-watched videos):** search, then a fetch of NAZ Elite's interview: the sentence is the interviewer's question 2. Held; applied as given.
- **Should-fix 4 (the book):** searches, then fetches of The Bookseller (2 Jul 2024: no title, no publication date) and Entrepreneur UK (27 Feb 2025: "out now, published by Sheldon Press"). Held; applied as given.
- **Should-fix 5, 6 and 7 (Sidibe's other income):** search, then a fetch of InsideHook (10 Aug 2021): it describes his routine at the time (running, soccer personal training, coaching youth athletes) in the present tense and dates no earlier work. Held; applied as given (the pattern count becomes two of five).
- **Should-fix 8 (A6's "minor"):** A6's Deliverable 1 heading reads "Instagram · the rented shop window"; "minor" is not A6's. Held; applied as given.
- **Minor 1 (ten years):** 20 Nov 2007 to January 2017 is about nine years. Held in part: the replacement's "(4 January 2017)" gives a day the unit does not state and the maintainer did not re-read on Kagan's page, so it was applied as "(January 2017)".
- **Minor 3 and 4 (Gazette and Black Belt wording):** searches, then fetches: "more than 165,000 followers on YouTube and Instagram" (Gazette, undated) and "more than 800,000 subscribers on YouTube" (Black Belt, updated 31 Jan 2024). Held; applied as given.
- **Minor 5 (18 months):** 20 Mar 2023 to 4 Sep 2024 is 17.5 months (script). Held; applied as given.
- **Minor 6 (Lewis's top five):** search, then a fetch of vidIQ's Lewis page (data 1 Nov 2026): all five top videos date from 15 Feb 2022 to 13 Dec 2023. Held; applied as given.
- **Against A9 (should-fix: "instant hit"; minor: Felton's year):** searches, then fetches of Skydio (24 Feb 2021: "months later it started catching on") and Zwift Insider (21 Sep 2026: "During the 2020 lockdown"). Held; both applied to A9 §5 as given, each pointing to DD-A1.
- **Against A1 (minor: the pointer):** the pointer still read true; the replacement adds what DD-A1 did with Boyd and Goal Guys, dated. Applied as given.
- **Figure 4 (matrix, FIX):** the caption and the legend's "partial" meaning, applied as given; the figure was rebuilt and re-checked by a new agent (below).

**Verdict as recorded.** Four error entries by count, two of them one fact in two places (Abdaal's October 2020 cadence), so three distinct errors and a list of edits fixes the unit: fix, as the checker itself read it.

## Figure re-check 1 (2 Nov 2026, a separate Opus 5.5 agent given the unit without its figures, the captions and figure 4's frames sheets at phone, tablet and desktop, dark and light; report verbatim)

Figure 4 now passes, with three minor findings and no errors or should-fix items. I checked all 25 cells against the unit's text, and each one matches it.

Findings:

[minor] [drawing] The legend's definition of 'partial' is shorter than the caption's. Current: `approximate date, another measure, a secondary source, or a statement about earlier work`. Problem: the caption reads "a secondary or summary source", and the Abdaal hours cell is a summary source: "Creator Science's show notes say … 5 to 10 hours of his effort a week as of October 2020 (the show's summary)". The legend leaves out "summary", so that cell is covered only if a show's summary is read as a secondary source. Fix: `approximate date, another measure, a secondary or summary source, or a statement about earlier work`

[minor] [drawing] At phone width (390 px), the creator names scroll out of view. In frames 2 and 3 (scrolled to 164 and 184 px) the row labels are gone, so a reader looking at the 24 MONTHS, 36 MONTHS and GOT WRONG columns can't see which creator a row belongs to. Nothing is lost: the names are in frame 1 and the "scroll sideways for the whole figure" note is there. Current: row-label column scrolls with the grid. Problem: across five rows the reader has to remember the row order. Fix: `make the row-label column sticky (position: sticky; left: 0) inside the scroll frame`

[minor] [text] The per-creator list for Abdaal disagrees with the figure and with the other summaries. Current: `- *12 / 24 / 36 months:* unpub. / unpub. / unpub.; ~4,000 at ~9 months; 100K in 2018; 1M Sep 2020 (own words and own site).` Problem: the figure marks his 12- and 36-month points as partial. In the same list, Sidibe's count with an approximate date goes into its slot ("unpub. / 125K+ between May 2019 and Jan 2020 (own Shorty entry) / unpub."). Abdaal's counts of the same kind are pushed after three "unpub."s instead, so the list is applying two rules. Fix: `- *12 / 24 / 36 months:* ~4,000 at ~9 months and 100K "in 2018" (own words, own site) / unpub. / 1M at 39 months, Sep 2020 (own site).`

Checks:

1. **Labels and cells.** All 25 cells match the text.
   - **Abdaal:**
     - Hours, partial: "5 to 10 hours of his effort a week as of October 2020 (the show's summary)".
     - 12 months, partial: "~4,000 at ~9 months … 100K 'in 2018'".
     - 24 months, unpub.: "*At 24 months (June 2019):* unpublished."
     - 36 months, partial: "1M at 39 months, Sep 2020".
     - Got wrong, own words: "I kind of wish I'd done that from day one" (Creator Science, 15 Dec 2020).
   - **Boyd:**
     - Hours, unpub.: "Unpublished."
     - 12, 24 and 36 months, all unpub.: "All three unpublished."
     - Got wrong, none found: "No statement found."
   - **Sidibe:**
     - Hours, 12 months and 36 months, all unpub.: "Unpublished." and "unpublished".
     - 24 months, partial: "So the count was taken between May 2019 and January 2020".
     - Got wrong, none found: "No statement found about the channel."
     - 264K at about 46 months is left as unpub. §7.3 supports this: "Abdaal's one million came at 39 months, and the rest are unpublished".
   - **Lewis:** every cell is unpub. or none found: "Unpublished.", "All three unpublished.", "No statement found."
   - **Partridge:**
     - Hours, unpub.: "Unpublished."
     - 12, 24 and 36 months, partial (another measure): "the figures that exist are listening and following claims, each in a different measure".
     - Got wrong, partial (earlier work): "About the businesses before UNILAD, not the podcast … 'I was starting them on short-term dopamine'".
   - The column headers match the five items named in the caption.
2. **Caption.** It says what the figure shows, names the sections ("§2 to §6 and the deliverable's table"), states the source ("a source opened in this unit") and defines 'partial'. It sits under the figure. No issue.
3. **Kind.** Creators by items, each cell a category: a matrix fits.
4. **Legend.** The four marks are used as the legend defines them. own words appears once, a dated quote. none found appears only in GOT WRONG where the text says "No statement found". unpub. appears only where the text says unpublished. partial covers approximate dates, other measures, the show's summary and a statement about earlier work. The one gap is "summary" missing from the legend (minor 1).
5. **Drawing.**
   - At desktop and tablet the whole figure fits in one frame, in both themes.
   - At phone width it scrolls 184 px across 3 frames. Taken together the frames show every column, every cell and the full legend. The "no statement found" text cut off in frame 1 is whole in frame 2.
   - All text sits inside its box and nothing overlaps.
   - The caption is under the figure.
   - Both themes are readable. Every cell carries a text label, so colour is not the only way to tell the marks apart, which matters most for the dark theme's brown own words against the maroon unpub.
   - The only problem is that the row names scroll off (minor 2).
6. **Unit text.** §7.3 ("only Abdaal has an hours figure"; "of the ten 24- and 36-month points … the rest are unpublished") agrees with the figure. One inconsistency in the per-creator list for Abdaal (minor 3).

Figure 4: PASS (errors 0, should-fix 0, minor 3)
**Maintainer's note on the figure re-check (2 Nov 2026).** The re-checker's transcript was checked by script: no web, memory, Projects or connector tool; every file it opened inside its packet. Figure 4 passed (0 errors, 0 should-fix, 3 minor). Minor 1 (the legend's "partial" lacked "summary", which the caption has and the Abdaal hours cell needs) verified against the caption and §2 and applied as given. Minor 3 (the deliverable's Abdaal line put three "unpub." where §2 gives approximate counts at about 9 and 39 months, while Sidibe's line puts his in their slot) verified against §2 and applied as given; the figure was rendered again. Minor 2 (the row labels scroll out of view at phone width) is the renderer change already queued as P83 (a sticky label column for a matrix at phone width), a proposed row awaiting Pedro's confirmation, which a chat does not work; it is recorded there. Figures 1 (line), 2 (timeline) and 3 (compare) passed the fresh check; figure 4 (matrix) passed after one fix. None dropped.
