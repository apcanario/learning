---
audit: fresh check
unit: PB6 · How YouTube growth works
course: personal-brand · PB · Building a Personal Brand on Instagram and YouTube
model: Opus 5.5 (claude-opus-5-5, as the agent states; this session keeps no agent transcript on disk, so the model could not be confirmed from a transcript's "model" field; live search). A Fable 5.1 fresh check of PB6 is owed to the Fable stage (P49)
date: 2026-11-12
chat: own Opus 5.5 agent context, not shown the writing (P31), launched by the W-PB5/W-PB6 chat (which ran on Opus 5.5 and only staged, applied, filed and published) in session https://claude.ai/code/session_01KMmgQyyVNoMqGMdFywhNmh
verdict: fix · 2 errors, 12 should-fix, 14 minor
---

The checker's final report, verbatim, from its hand-back in the chat (the checker was told to return its report rather than write a file; the harness's indentation of the hand-back is removed). Saved before any finding was applied.

Model: claude-opus-5-5

# PB6 fresh check: How YouTube growth works

I read only the files in /tmp/pb6/check/. Every source was opened live on 12 Nov 2026, each through a URL that a WebSearch in this run had returned. I edited no file and published nothing. All four viz blocks parse, and tools/viz.py renders each one.

**Verdict: PB6 is "fix".** There are 2 errors, 12 should-fix and 14 minor findings, and every one can be fixed with an edit.

The two errors:
- **§3 and rule R6 cut YouTube's sentence on changing packaging.** YouTube recommends a change when CTR is lower *and* the video is getting fewer impressions than usual. The unit keeps only the CTR half, and R6's selection rule is built on that half.
- **The §4 figure has two numbers the text never gives.** The 34.6% and 10.8% bands appear only in the figure.

## Findings

1. [error] [accuracy] §3 "Testing packaging on a phone" and D1 R6
   - Current: `that such changes "are recommended when a video has a lower click-through rate (CTR)", and that`
   - Problem: the source's sentence goes on with "and is receiving fewer impressions than usual". Cutting it changes the condition. R6 then picks the lowest-CTR upload whatever its impressions, which YouTube's FAQ (7628154) says can be natural at high impressions.
   - Fix: `that such changes "are recommended when a video has a lower click-through rate (CTR) and is receiving fewer impressions than usual", and that`
   - Before applying: my fetch returned this as two quoted pieces that run on from each other. Check that they are contiguous on the page.
   - Basis: https://support.google.com/youtube/answer/16559651?hl=en

2. [error] [accuracy] D1 R6 (follows from item 1)
   - Current, rule: `at most one upload at least 28 days old whose CTR is the lowest of the quarter and whose Intro is at or above her median gets one new thumbnail or one new title`
   - Fix: `at most one upload at least 28 days old whose CTR is the lowest of the quarter, whose impressions are below her median upload's and whose Intro is at or above her median gets one new thumbnail or one new title`
   - Current, evidence: `Changes "recommended when a video has a lower click-through rate"`
   - Fix: `Changes "recommended when a video has a lower click-through rate (CTR) and is receiving fewer impressions than usual"`
   - Also: the notes.md register entry for Mara's packaging check needs the same change.
   - Basis: same page as item 1.

3. [error] [figure] §4, second compare figure
   - Current: `the top 1% of videos took 54.1% of all first-week views`
   - Problem: the figure's rows "Next 9%" (34.6) and "Next 40%" (10.8) are not in the unit's text. Both figures are on the source page.
   - Fix: `the top 1% of videos took 54.1% of all first-week views, the next 9% took 34.6%, the next 40% took 10.8% and the bottom 50% took 0.5%`
   - Basis: https://vidiq.com/research/youtube-first-week-views/

4. [should-fix] [accuracy] §3 "Testing packaging on a phone"
   - Current: `"The first title and thumbnail you uploaded becomes the default"`
   - Problem: the words in quotation marks are not the page's.
   - Fix: `"the first title and thumbnail you upload will be the default title and thumbnail for your video"`
   - Basis: https://support.google.com/youtube/answer/16391400?hl=en

5. [should-fix] [accuracy] §8, paragraph after the table
   - Current: `"Videos made with AI can be recommended as broadly as those made without AI"`
   - Problem: not verbatim.
   - Fix: `"Videos that are made with AI can be recommended as broadly as videos made without AI"`
   - Basis: https://support.google.com/youtube/answer/16089387?hl=en

6. [should-fix] [accuracy] §5 "Against, or no difference", OverseerOS bullet
   - Current: `it cannot see impressions, click-through, retention or traffic sources, and its channels chose when to start`
   - Problem: this leaves out the study's own weaker result, which matters in a section that weighs the evidence both ways. A stricter catalogue-coverage subset of 16 channels showed 0.754x.
   - Fix: `a stricter subset of 16 channels showed a ratio of 0.754, so it does not claim Shorts have no effect; it cannot see impressions, click-through, retention or traffic sources, and its channels chose when to start`
   - Basis: https://www.overseeros.com/blog/do-youtube-shorts-hurt-long-form-views

7. [should-fix] [figure] §3 decision figure, caption
   - Current: `Every branch quotes or paraphrases YouTube Help, Impressions and click-through rate FAQ, answer 7628154, checked 12 Nov 2026;`
   - Problem: the remedy "make the package true to the first 30 seconds" is not in answer 7628154. It is rule R2 and PB5's promise test.
   - Fix: `Every branch quotes or paraphrases YouTube Help, Impressions and click-through rate FAQ, answer 7628154, checked 12 Nov 2026, except the remedy on the clickbait branch, which is rule R2 (PB5's promise test);`
   - Also, Current: `At least 7 days old and over 100 views?` Fix: `At least 7 days old and 100 views or more?` (the FAQ's line is "fewer than 100 views").

8. [should-fix] [figure] §5 matrix
   - Current: `"Shorts reach more; flat across ten"`
   - Problem: vidIQ says the two formats "are shown on separate scales and are not directly compared to each other". The text already says this; the figure cell contradicts it.
   - Fix: `"Shorts about 1,362 to 1,344 views; flat across ten; not compared with long-form"`
   - Basis: https://vidiq.com/research/youtube-first-10-videos-study/

9. [should-fix] [figure] D2 YT9
   - Current: `+0.5 a month at 1–99 subscribers, +1.4 at 100–499, +3.7 at 500–999, channels that added videos in the 90 days to 20 Jul 2026`
   - Problem: a vendor dataset cited without its sample size.
   - Fix: `+0.5 a month at 1–99 subscribers, +1.4 at 100–499, +3.7 at 500–999, 3,332,098 channels that added videos in the 90 days to 20 Jul 2026`
   - Basis: https://vidiq.com/research/youtube-subscriber-benchmarks-2026/ (bands of 1,047,481, 1,430,714 and 853,903 channels)

10. [should-fix] [style] D2, "What the rows do not tell her"
    - Current: `(see the notes on PB1, D3)`
    - Problem: the writer's notes are not something a reader can open.
    - Fix: `(PB10 decides whether such an upload counts towards verdict 3)`

11. [should-fix] [style] §5 "For Mara"
    - Current: `PB3 gave Shorts no hours at 6 hours a week, and PB4 and PB5 kept that pending this unit (flag F24).`
    - Problem: "flag F24" is internal process language a public reader cannot interpret.
    - Fix: `PB3 gave Shorts no hours at 6 hours a week, and PB4 and PB5 left that for this unit to revisit.`

12. [should-fix] [style] §6
    - Current: `**Weighing them (flag F31).**`
    - Problem: same as item 11.
    - Fix: `**Weighing them.**`

13. [should-fix] [attribution] §6 and §8, where the cadence FAQ was published
    - Current (§6): `PPC Land dates the FAQ's publication in YouTube's German help centre to 2 September 2026,`
    - Problem: PPC Land says a German-language recommendations FAQ was posted in the YouTube Help community forum, "alongside Help Center pages covering the Audience tab and content performance troubleshooting". It does not say "German help centre".
    - Fix (§6): `PPC Land reports a German-language FAQ posted in the YouTube Help community on 2 September 2026, alongside Help Center pages on the Audience tab and on performance troubleshooting,`
    - Current (§8 row): `Performance FAQ with the break and cadence answers published in YouTube's German help centre`
    - Fix (§8 row): `German-language recommendations FAQ posted in the YouTube Help community, with Help Center pages on the Audience tab and performance troubleshooting`
    - Basis: https://ppc.land/youtube-finds-no-link-between-upload-breaks-and-view-counts/

14. [should-fix] [attribution] §3 and Sources, Focus Digital
    - Problem: the page has a byline date, 11 Sep 2026, which the unit does not give (the unsure list says no exact date was found).
    - Current: `Focus Digital, Average YouTube CTR, 2026` Fix: `Focus Digital, Average YouTube CTR, 11 Sep 2026`
    - Current: `Focus Digital, "Average YouTube CTR: organic and paid benchmarks 2026", checked 12 Nov 2026.` Fix: `Focus Digital, "Average YouTube CTR: organic and paid benchmarks 2026", 11 Sep 2026, checked 12 Nov 2026.`
    - Basis: https://focus-digital.co/average-youtube-ctr-organic-paid-benchmarks-2026/

15. [should-fix] [coverage] after Sources: add the unsure list
    - Current: `- YouTube Official Blog (Julia Lee Harter), related videos traffic guide, 14 Jul 2026. https://blog.youtube/creator-and-artist-stories/youtube-related-videos-traffic-guide/`
    - Fix: that line unchanged (or as amended in item 18), followed by:
```
## Unsure list

- The YouTube Studio app paths in D2 (Content, the video, Analytics, Reach) come from YouTube's Android help page (answer 9314355); the iPhone version was not read, and the app's name for the Engagement tab and the retention report's path in the app were not confirmed (§2, D2 YT4, YT5).
- When the sentence on videos made with AI first appeared on the recommendations page (answer 16089387) is not shown (§8).
- The English performance FAQ (answer 141805) shows no date; the 2 Sep 2026 date rests on PPC Land's report of a German-language FAQ in the YouTube Help community, published alongside Help Center pages (§6, §8).
- Metricool states its period as comparing 2025 with 2026 and gives no exact date range; its traffic-source categories are not formally defined (§2, §5, §6).
- Beaupré's 2026 statements on topic matching for channels with no history, impressions stopping, notifications as the only push and videos peaking a month or more later are PPC Land's paraphrases of an interview (§1, §2, §4).
- vidIQ's first-week study does not state its channel count, and livestreams were not filtered out of its long-form cohort (§4).
- AIR's title study states no period for its title data, and no Home and DIY figure could be read (§7).
- The 4 Dec 2025 date for global title testing is Search Engine Journal's; YouTube's Creator Insider announcement was not opened (§8).
```
    - Changes from unsure.md:
      - The Test & Compare duration item is dropped. The page says a test "can take a few days or up to 2 weeks", and the unit uses no duration.
      - The Focus Digital item is dropped, because its date is now resolved (item 14).

16. [minor] [attribution] Sources: `YouTube Help, "Changes to YouTube Partner Program terms" (answer 12843009)` → `YouTube Help, "Changes to the YouTube Partner Program" (answer 12843009)` (the page's title in search results; PB1 uses the same old title and needs the same fix). https://support.google.com/youtube/answer/12843009

17. [minor] [attribution] Sources: `YouTube Official Blog (Julia Lee Harter), related videos traffic guide, 14 Jul 2026.` → `YouTube Official Blog (Julia Lee Harter), "How to convert YouTube Shorts views into long-form channel growth", 14 Jul 2026.` https://blog.youtube/creator-and-artist-stories/youtube-related-videos-traffic-guide/

18. [minor] [attribution] Sources, authors missing:
    - `Search Engine Journal, "YouTube title A/B testing rolls out globally to creators", 4 Dec 2025.` → `Search Engine Journal (Matt G. Southern), "YouTube title A/B testing rolls out globally to creators", 4 Dec 2025.`
    - Also add "(Olha Kapinos)" after the AIR Shorts entry's "AIR Media-Tech" and "(Gretchen Oestreicher)" after "Metricool", as PB3 does.

19. [minor] [accuracy] §7: `titles of 90 or more characters underperforming on views` → `titles of over 90 characters underperforming on views, with search-optimised content a partial exception`. https://air.io/en/audience-growth/how-to-write-a-youtube-title-that-gets-clicked-research-across-11-niches

20. [minor] [style] §7, quotation not exact: `how well the title, tags, description and video content match your search query` → `how well the title, tags, description, and video content match your search query`. https://support.google.com/youtube/answer/16090438?hl=en

21. [minor] [deliverable] D2 YT11: `no viewer can qualify as regular before month six` → `no viewer can qualify as regular before month seven` (regular means watched in "more than 6 months in the past year"). https://support.google.com/youtube/answer/10246996?hl=en

22. [minor] [deliverable] T2 YT11: `[from the first review at least six months after your first upload]` → `[from the first review more than six months after your first upload]`. Same source.

23. [minor] [attribution] §6 and R7, pointer to PB4
    - The "never two videos in one week" rule is in PB4's D1 checklist (line 267), not in PB4 §7.
    - `When a week is lost, PB4 §7's rules apply: no catch-up video, never two videos in one week.` → `When a week is lost, PB4's rules apply (§7, D1): no catch-up video, never two videos in one week.`
    - `(PB4 §7). |` → `(PB4 §7, D1). |`

24. [minor] [label] §8 row 2: `creator reports, unconfirmed` → `creator anecdote and an analyst's reading; unconfirmed by YouTube` (SEJ names a retention strategist and one creator's data). https://www.searchenginejournal.com/youtube-shorts-algorithm-may-now-favor-fresh-over-evergreen/562661/

25. [minor] [attribution] §9 item 6: `An analyst's working theory reported by PPC Land, 2 Dec 2025` → `An analyst's reading (Mario Joos, on X, 30 Nov 2025) reported by PPC Land, 2 Dec 2025`. https://ppc.land/youtube-creators-report-drops-in-shorts-viewership-after-september-algorithm-change/

26. [minor] [style] §3: `needs advanced features enabled, cannot test Shorts` → `needs YouTube's advanced features enabled (a channel setting the creator turns on in Studio), cannot test Shorts`. "Creator Insider" in §1 could also be glossed as "YouTube's channel for creator briefings" (PPC Land's description).

27. [minor] [coverage] §5. A non-peer-reviewed arXiv preprint (Rajendran, Creusy and Garnes, 2024; 250 creators) reports "a significant decrease in both view counts and engagement in long-form videos" since Shorts arrived. It is not in the brief's source classes. No change required. The filing chat may add one sentence to §5 naming it as an unreviewed preprint left out. https://arxiv.org/abs/2402.18208

28. [minor] [coverage] D2. The brief asks for the rows "worked for Mara's first quarter". The unit sets which uploads qualify, the dates, the bands and what she writes, and leaves the values to PB10. No change required, since PB10's brief runs her Q1 and Q2 with invented numbers; the filing chat should confirm that split.

## Confirmed (PASS)

YouTube's own pages:
- **answer 16089387:** where recommendations appear; the signals; "over 80 billion pieces of information"; "satisfaction, not just watch time"; Up Next uses the current video as main signal; Home "relies primarily on watch history"; no mention of clicks, upload time or new channels. https://support.google.com/youtube/answer/16089387?hl=en
- **Goodrow, 15 Sep 2021:** all five quotations are verbatim, including "Clicking on a video provides a strong indication...". https://blog.youtube/inside-youtube/on-youtubes-recommendation-system/
- **answer 16559651:** "What matters is how viewers respond..."; "does not penalize a channel overall"; "Long-term channel performance can be affected..."; monetised videos not prioritised; unlisted-first; Unique Viewers; the formats quotes; "a viewer that often engages..."; "Changing a video's title or thumbnail can lead to a shift..."; "not to change what is already working well"; "expertise or a clear niche"; "critical mass of content". The truncation in item 1 is the exception.
- **answer 1714921:** all traffic-source definitions verbatim; H1 is "Understand your YouTube video reach", Computer version. https://support.google.com/youtube/answer/1714921?hl=en-GB
- **answer 9314355:** Android; path Content, video, Analytics card, Reach; "Thumbnail impressions" and "Thumbnail impressions click-through-rate"; the search terms sentence.
- **answer 7628154:** all seven bullet quotes and the definition; external sites and end screens not counted.
- **answer 9314415:** Intro, Spikes and Dips (verbatim), 60 s / 100 views, "all YouTube videos of similar length".
- **answer 12942217:** typical retention, "A typical intro is about 30 seconds long", the 50% "above typical intros" list.
- **answer 16391400:** up to 3 titles and thumbnails, computers only, advanced features, no Shorts, watch time over CTR, "Not enough impressions" and "Inconclusive". The default-title quote is the exception (item 4).
- **answer 141805:** reasons old videos gain views; "dozens of channels"; break and cadence findings; publish time; no date on the page.
- **answer 72851:** public long-form qualified hours; private, unlisted and removed videos and Shorts excluded; "any qualified watch hours from Shorts views in the Shorts feed won't count".
- **answer 12843009:** 8,000 hours / 20M Shorts views with 1,000 subscribers from 1 Feb 2027; 10M for Shorts revenue; accept terms by 31 Jan 2027; fan funding 500 subscribers + 3,000 hours / 3M Shorts views.
- **answer 16090438:** the three elements; "may vary by search type"; engagement and quality quotes; search history; no paid placement; no date or size factor.
- **answer 146402:** "a minimal role"; misspellings; title, thumbnail and description matter more.
- **answer 13615784:** all four quotations.
- **answer 10246996:** regular viewers "more than 6 months"; "Audience segments do not affect reach or monetization".
- **answer 14075157:** the related-video quotes; advanced feature access; steps start in Studio.
- **YouTube Blog, 14 Jul 2026:** "billions of daily views"; no conversion figure.
- **YouTube Blog, 10 Aug 2026:** the thresholds and the 1 Feb 2027 date.

Press and executives:
- **SEJ, 4 Mar 2024:** all four Beaupré quotations; he "leads YouTube's growth and discovery team". https://www.searchenginejournal.com/youtube-algorithm-myths-debunked-insights-from-the-growth-team/510091/
- **PPC Land, 2 Sep 2026 (interview):** Creator Insider interview of 1 Sep 2026; the 10% and 90% quotes; "Each viewer gets a different ranking"; first hour; topic matching and impressions stopping (paraphrases); notifications; day-one versus month-plus peaks; television. https://ppc.land/subscribers-skip-90-of-uploads-in-their-feed-youtube-director-says/
- **SEJ, 4 Dec 2025:** global title testing; Creator Insider; up to three; long-form only; desktop only; watch time.
- **SEJ, 5 Dec 2025:** mid-September shift; "YouTube hasn't confirmed any algorithm change".
- **TechCrunch, 23 Sep 2026:** Ask Studio expanding to mobile; Dynamic Thumbnails with no date or eligibility; "three different cuts for Shorts" from 2027. https://techcrunch.com/2026/09/23/youtube-adds-new-creator-tools-like-video-a-b-testing-dynamic-thumbnails-and-live-dubbing/
- **PPC Land, 2 Dec 2025:** "satisfied watch time per click" is an analyst's formula; YouTube "provided no official explanation".

Vendor data:
- **Metricool, 29 Jul 2026 (modified 4 Aug 2026):** 799,718 videos and 71,177 accounts; the period is "comparing 2025 with 2026"; Shorts feed "More than 61%", subscribers 11%, search 9%, related 5.77%, playlists 5.05%, channel page about 3%; browse not reported; 8,789 / 5,985 / 4,364; 35+ Shorts fall back; "Correlation isn't causation here..."; long-form best at 2 to 4 a week (10,552); less than weekly weakest; peak in three days; 83% of interactions in ten days; "keeps earning views for months". https://metricool.com/youtube-trends/
- **Focus Digital:** "4–6%"; January to June 2026; sources named; no sample.
- **vidIQ average view duration page (updated 21 Jul 2026):** the 40–55% band; "vidIQ guidance for target bands"; "best baseline is your own comparable library"; 30.3% across 16.5M views, 26 Jun 2025 to 25 Jun 2026.
- **vidIQ first-week views, 16 Sep 2026:** 38,229,639 videos; 15 Aug to 5 Sep 2026; median 234; 37.7% and 70.1%; 54.1%; all three caveats; no channel count; livestreams not filtered.
- **vidIQ first ten videos, 28 Jul 2026 (updated 30 Jul 2026):** 180 and 272; 1,948; 1,362 and 1,344; "no incremental growth..."; separate scales; "Views are not subscriber counts"; "excluded entirely".
- **vidIQ uploads study, 11 Sep 2026:** 32,926,088 channels; 0.20 / 1.86 / 8.65 / 30.77%; the observational caveat; formats not separated.
- **vidIQ subscriber benchmarks, 20 Jul 2026:** +0.5 / +1.4 / +3.7.
- **AIR Shorts study, 28 May 2026:** 18,000 channels with at least 40 videos, 10 long-form, March 2025 to March 2026; the Home and DIY quote; 95,100 v 94,600 and 251,500 v 256,000 (long-only first); "subscriber counts, not cross-format viewing rates"; the 0.04–0.5% figure has no method.
- **AIR posting study, 8 Jun 2026:** US, UK, Canada, Australia; primary analysis 100K–1M; 83,050/116, 114,000/178, 105,000/130, 90,700/87; went dark for 14+ days; predictable schedule; "This is correlational data, not causal".
- **AIR title study, 12 Jun 2026:** 18,080 channels; 100K–100M; 11 niches; engagement-rate and p75 outcomes; 30–50 "the universal sweet spot"; first 40%; Home and DIY finished project; both caveats; no period.
- **OverseerOS, 1 Sep 2026:** 370 videos on 37 channels; 1.021; 19 of 37; the quotation; no private metrics; creators choose timing.
- **OverseerOS, 8 Nov 2026:** 9,982 Shorts; about eight days; "Among 1,546 Shorts..."; "The research corpus is selected, not random."

Arithmetic:
- Mara's title is 82 characters; "teak" starts at character 13; 40% of 82 is 32.8.
- On 5 Apr 2027, uploads 1–5 are at least 30 days old and upload 7 is 6 days old.

## (7) Figures

1. **compare, §2 (Metricool split): PASS.** Every label and value is in §2's text. The caption names the section and the source. Compare fits. Optional minor: "the shares do not sum to 100" is derived and not stated in the text.
2. **decision, §3 (reading one upload's CTR): FIX.** Branches trace to the bullets quoted in §3. The caption over-attributes and the first question's threshold is off; replacements in item 7. Decision fits a rule with branches.
3. **compare, §4 (first-week view shares): FIX.** 54.1, 0.5, 234 and the cohort are in the text; 34.6 and 10.8 are not (item 3, fixed in the text). The caption is good. Compare fits.
4. **matrix, §5 (Shorts sources): FIX.** All rows trace to §5 except the vidIQ cell's "Shorts reach more", which contradicts the source (item 8). The caption is good. Matrix fits.

## (8) The writer's notes

**Source errors:**
- **A6 §1.1, page title for answer 1714921: confirmed.** The H1 is "Understand your YouTube video reach" (Computer). Nuance: the section heading is "Understand types of traffic sources", not "Traffic sources".
- **PB3 §4, AIR sample omission: confirmed.** The page says each channel posted "at least 40 videos, including 10 long-form videos" (fetch wording).
- **A6 §1.2, "narrower, more loyal audience": the writer's premise is not confirmed.** The page still says "These higher numbers are because they've been viewed by a narrower, more loyal audience." A6 is right, no replacement is needed, and PB6's quotation of the preceding sentence is fine.

**Contradictions:**
- **PB1 D3 verdict 3: a real methodological conflict.** PB1 reads "click-through under 2% ... on 3 or more of the quarter's uploads". Answer 7628154 says "If a video gets a lot of impressions (such as if it appears on the homepage), it's natural for the CTR to be lower." The proposed impressions condition is consistent with answer 16559651's "fewer impressions than usual" (item 1).
- **PB3 §3 shelf life ("Months, by platform statement and vendor data"): partly real.** Metricool does assert "keeps earning views for months", but measures only interactions; the platform statement concerns eligibility. The proposed wording is more exact.
- **DD-PB1: not a contradiction**, as the writer says.
- **PB9 / PB1 §4: real gap, not a contradiction.** PB1 §4 has no row for the 10M-in-90-days Shorts revenue rule. Answer 12843009 says creators must "maintain 10M qualified Shorts views over the last 90 days".

## (9) Sourcing standard Part 5, line by line

1. Sourced where made: **FAIL** at §3 / R6 (truncated condition, item 1). Otherwise PASS.
2. Source classes: PASS. Focus Digital and the AIR 0.04–0.5% figure are named and then excluded.
3. Anecdote, vendor and correlational labels: PASS. Minor: the §8 SEJ row (item 24).
4. Platform named for each growth, format or metrics claim: PASS. The whole unit is YouTube and each claim says so.
5. Carried claims re-verified: PASS. Every claim I opened held, apart from the items above.
6. No private-course reader or private units: PASS. A scan found no private names or terms; private_terms.py was not available to run.
7. Mara facts: PASS. "(Mara, fictional)" at line 16; consistent with case-facts.md; never used as evidence.
8. Tax and law: PASS. Nothing applicable; the YPP thresholds are platform terms.
9. No uncited figures or invented names: PASS. Figure 3's two bands fail under Part 1's figure line (item 3).
10. Dates on changeable facts: PASS (blanket date at line 14, plus dated vendor sources). Focus Digital's date is missing (item 14).
11. Deliverable for Mara, then template: PASS.
12. Not advice without evidence: PASS. Every rule carries evidence, grade and label, with convention marked.
13. Links given as links: PASS.

## (10) Read as the public persona

- "flag F24" and "flag F31" (§5, §6) are internal process labels (items 11, 12).
- "see the notes on PB1, D3" points to writer's notes the reader cannot open (item 10).
- "advanced features" and "Creator Insider" are unexplained (item 26).
- Everything else is defined in earlier units the reader has read: PB1's labels, verdict 3, Q1/Q2 reviews, the cut window's packaging hour, Season 1 and the promise test. No private course, unit or name appears.
- Answer numbers serve as locators and are linked.

## (6) Errata

- No PB6 audit report exists yet. From A6's fresh check, erratum 2 (AIR posting: "primary analysis" on 100K–1M) is applied in §6. Erratum 9 (the month-six model) is not carried, which is correct.
- Pointers to filed units match what those units say, except the PB4 §7 pointer (item 23): PB1 rows Y1–Y11 and D3; PB1 §2 and §4; PB3 §4, §6 and D2 (24.0 of 24 h, no Shorts hours); PB4 §2; PB5 §3 and §7.

**PB6 — fix · 2 errors, 12 should-fix, 14 minor.**
