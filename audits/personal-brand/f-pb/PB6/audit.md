Model: claude-fable-5-2

# Stratified-sample audit · PB6 · How YouTube growth works · 14 November 2026 · search on

**Verdict: PASS.** 13 claims sampled, one per `##` section plus the two parts of the deliverable; 0 FAIL, so no full audit was run. 54 claims checked in all: 50 PASS, 2 FAIL (both minor, both outside the sample), 0 STALE, 2 unverifiable (one YouTube Help page could not be opened). Two minor errata and two flags follow.

## Provenance

- Auditor: one fresh, isolated agent, model claude-fable-5-2, 14 Nov 2026. Read only `/home/claude/fpb/PB6`; wrote only `out/`. `out/` was empty at the start, so nothing was resumed.
- Unit: `unit.md` (PB6, written 2026-11-12 by Opus 5.5, search on). Not edited.
- The sample below was written to this file before any source was opened.
- Web rule followed: WebSearch first; WebFetch only on a URL a search in this agent returned verbatim. 34 searches, 43 fetches. Pages were read through the fetch tool, which returns extracts; where it cut a long sentence short, the note says so.
- The earlier fresh check (`fresh-check-PB6.md`) was read to avoid re-reporting; none of its verdicts was reused. Erratum PB6-1 reverses its item 19, on the page's own bucket labels.

## Sample (recorded before checking; one claim per `##` section)

| # | Section | Sampled claim | Source cited |
|---|---|---|---|
| S1 | §1 | Recommendations page: "over 80 billion pieces of information"; surveys help understand "satisfaction, not just watch time" | https://support.google.com/youtube/answer/16089387?hl=en |
| S2 | §2 | Metricool: 799,718 videos, 71,177 accounts, 2025 against 2026; Shorts feed more than 61%, subscribers 11%, search 9%, related 5.77%, playlists 5.05%, channel pages about 3%; browse not reported | https://metricool.com/youtube-trends/ |
| S3 | §3 | "Half of all channels and videos on YouTube have an impressions CTR that can range between 2% and 10%." | https://support.google.com/youtube/answer/7628154?hl=en-GB |
| S4 | §4 | vidIQ first-week views: 38,229,639 long-form videos, 15 Aug to 5 Sep 2026; median 234; 37.7% under 100; 70.1% under 1,000; top 1% took 54.1%, next 9% 34.6%, next 40% 10.8%, bottom 50% 0.5%; published 16 Sep 2026 | https://vidiq.com/research/youtube-first-week-views/ |
| S5 | §5 | AIR: 18,000 English-language channels, 40+ videos and 10+ long-form, Mar 2025 to Mar 2026; Home and DIY "near-identical", 95,100 v 94,600 and 251,500 v 256,000 | https://air.io/en/audience-growth/do-youtube-shorts-help-your-long-form-videos-grow-data-from-18000-channels |
| S6 | §6 | vidIQ: 32,926,088 channels under 1,000 subscribers, 360 days; 0.20% / 1.86% / 8.65% / 30.77% crossed 1,000 by videos added; "observational association"; formats not separated | https://vidiq.com/research/youtube-uploads-1000-subscribers/ |
| S7 | §7 | Search: relevance ("how well the title, tags, description, and video content match your search query"), engagement (watch time per query), quality (expertise, authoritativeness, trustworthiness); importance "may vary by search type"; no payment for placement; no channel size or upload date on the page | https://support.google.com/youtube/answer/16090438?hl=en |
| S8 | §8 | 10 Aug 2026 blog post: from 1 Feb 2027 new applicants need 8,000 qualified watch hours in 365 days or 20M qualified Shorts views in 90 days; Shorts revenue sharing only at 10M qualified Shorts views in 90 days; (with 1,000 subscribers; terms accepted by 31 Jan 2027) | https://blog.youtube/news-and-events/new-opportunities-to-earn-and-changes-to-the-youtube-partner-program/ |
| S9 | §9 | "Publish time is not known to impact a video's long-term performance"; publishing when the audience is active "can be beneficial for early viewership" | https://support.google.com/youtube/answer/141805?hl=en |
| S10 | Deliverable D1 R4 | "consistent and similar in topic or format"; "a series of videos from topics that have already proven popular" | https://support.google.com/youtube/answer/13615784?hl=en |
| S11 | Deliverable D2 YT9 | +0.5 a month at 1–99 subscribers, +1.4 at 100–499, +3.7 at 500–999; 3,332,098 channels; 90 days to 20 Jul 2026 | https://vidiq.com/research/youtube-subscriber-benchmarks-2026/ |
| S12 | Sources | TechCrunch (Amanda Silberling), "YouTube adds new creator tools like video A/B testing, dynamic thumbnails, and live dubbing", 23 Sep 2026; and the §8 row it supports | https://techcrunch.com/2026/09/23/youtube-adds-new-creator-tools-like-video-a-b-testing-dynamic-thumbnails-and-live-dubbing/ |
| S13 | Unsure list | vidIQ first-week study states no channel count; livestreams not filtered out | https://vidiq.com/research/youtube-first-week-views/ |

The twelve `##` sections are §1 to §9, Deliverable, Sources and Unsure list. The deliverable gave two sampled claims (D1 and D2). The templates carry no checkable claim of their own beyond the D1 and D2 rows; they are covered under "Deliverable".

## Table: sampled claims

| # | Section | Claim | Source | Verdict | Note |
|---|---|---|---|---|---|
| S1 | §1 | Recommendations page: "over 80 billion pieces of information"; surveys help understand "satisfaction, not just watch time" | https://support.google.com/youtube/answer/16089387?hl=en | PASS | Both strings are on the page as quoted. The page names no clicks, upload time or new-channel treatment, as the unit says. |
| S2 | §2 | Metricool: 799,718 videos, 71,177 accounts, 2025 against 2026; Shorts feed more than 61%, subscribers 11%, search 9%, related 5.77%, playlists 5.05%, channel pages about 3%; browse not reported | https://metricool.com/youtube-trends/ | PASS | Every figure, the sample, the author (Gretchen Oestreicher) and both dates (29 Jul, modified 4 Aug 2026) confirmed. |
| S3 | §3 | "Half of all channels and videos on YouTube have an impressions CTR that can range between 2% and 10%." | https://support.google.com/youtube/answer/7628154?hl=en-GB | PASS | Verbatim. |
| S4 | §4 | vidIQ first-week views: 38,229,639 long-form videos, 15 Aug to 5 Sep 2026; median 234; 37.7% under 100; 70.1% under 1,000; top 1% took 54.1%, next 9% 34.6%, next 40% 10.8%, bottom 50% 0.5%; published 16 Sep 2026 | https://vidiq.com/research/youtube-first-week-views/ | PASS | All figures and the three caveat phrases confirmed. |
| S5 | §5 | AIR: 18,000 English-language channels, 40+ videos and 10+ long-form, Mar 2025 to Mar 2026; Home and DIY "near-identical", 95,100 v 94,600 and 251,500 v 256,000 | https://air.io/en/audience-growth/do-youtube-shorts-help-your-long-form-videos-grow-data-from-18000-channels | PASS | Confirmed, with both caveat sentences. The page meta description says "the full 2025 calendar year"; the body says March 2025 through March 2026, which the unit follows. |
| S6 | §6 | vidIQ: 32,926,088 channels under 1,000 subscribers, 360 days; 0.20% / 1.86% / 8.65% / 30.77% crossed 1,000 by videos added; "observational association"; formats not separated | https://vidiq.com/research/youtube-uploads-1000-subscribers/ | PASS | All confirmed; published 11 Sep 2026. |
| S7 | §7 | Search: relevance ("how well the title, tags, description, and video content match your search query"), engagement (watch time per query), quality (expertise, authoritativeness, trustworthiness); importance "may vary by search type"; no payment for placement; no channel size or upload date on the page | https://support.google.com/youtube/answer/16090438?hl=en | PASS | Confirmed; two of the quoted sentences were returned truncated but matched as far as shown. |
| S8 | §8 | 10 Aug 2026 blog post: from 1 Feb 2027 new applicants need 8,000 qualified watch hours in 365 days or 20M qualified Shorts views in 90 days; Shorts revenue sharing only at 10M qualified Shorts views in 90 days; (with 1,000 subscribers; terms accepted by 31 Jan 2027) | https://blog.youtube/news-and-events/new-opportunities-to-earn-and-changes-to-the-youtube-partner-program/ | PASS | Blog confirms title, byline (The YouTube Team), date, 8,000/365, 20M/90, 10M/90 and 1 Feb 2027. The 1,000-subscriber condition and the 31 Jan 2027 deadline were not found in the blog as read; they rest on answer 12843009, which was not opened (see Not checked). Answer 72851 (en-GB) carries both "1,000 subscribers" and "review and accept the updated terms in YouTube Studio by 31 January 2027", so the row holds. |
| S9 | §9 | "Publish time is not known to impact a video's long-term performance"; publishing when the audience is active "can be beneficial for early viewership" | https://support.google.com/youtube/answer/141805?hl=en | PASS | Both verbatim. |
| S10 | Deliverable D1 R4 | "consistent and similar in topic or format"; "a series of videos from topics that have already proven popular" | https://support.google.com/youtube/answer/13615784?hl=en | PASS | Both strings are on the page. |
| S11 | Deliverable D2 YT9 | +0.5 a month at 1–99 subscribers, +1.4 at 100–499, +3.7 at 500–999; 3,332,098 channels; 90 days to 20 Jul 2026 | https://vidiq.com/research/youtube-subscriber-benchmarks-2026/ | PASS | Medians confirmed. 3,332,098 is the sum of the three bands (1,047,481 + 1,430,714 + 853,903), not a figure the page prints; PB1 row Y6 uses the same sum. |
| S12 | Sources | TechCrunch (Amanda Silberling), "YouTube adds new creator tools like video A/B testing, dynamic thumbnails, and live dubbing", 23 Sep 2026; and the §8 row it supports | https://techcrunch.com/2026/09/23/youtube-adds-new-creator-tools-like-video-a-b-testing-dynamic-thumbnails-and-live-dubbing/ | PASS | Author, title, date, Ask Studio, Dynamic Thumbnails, "three different cuts for Shorts" from 2027 and the absence of dates or eligibility all confirmed. |
| S13 | Unsure list | vidIQ first-week study states no channel count; livestreams not filtered out | https://vidiq.com/research/youtube-first-week-views/ | PASS | Page: "Livestreams were not separately filtered out"; no channel count. |

## Also checked (beyond the sample, counted in the totals)

| # | Section | Claim | Source | Verdict | Note |
|---|---|---|---|---|---|
| 14 | §1 | Help page: where recommendations appear, the signal list, Up Next main signal, Home relies primarily on watch history | https://support.google.com/youtube/answer/16089387?hl=en | PASS |  |
| 15 | §1 | Goodrow, VP of engineering, 15 Sep 2021: six quoted strings | https://blog.youtube/inside-youtube/on-youtubes-recommendation-system/ | PASS | All six verbatim. |
| 16 | §1 | Creator page: "What matters is how viewers respond…", "does not penalize a channel overall", "consistently stops watching", monetised videos not prioritised, unlisted-first quote | https://support.google.com/youtube/answer/16559651?hl=en | PASS |  |
| 17 | §1 | Beaupré, SEJ 4 Mar 2024: four quotations | https://www.searchenginejournal.com/youtube-algorithm-myths-debunked-insights-from-the-growth-team/510091/ | PASS | First fetch refused by permission; retried once and read. All four verbatim. |
| 18 | §1 | Beaupré via PPC Land, 2 Sep 2026: interview published 1 Sep 2026; "Each viewer gets a different ranking"; "videos are reaching people who've never watched the channel before"; topic-match and impressions-stop are paraphrases | https://ppc.land/subscribers-skip-90-of-uploads-in-their-feed-youtube-director-says/ | PASS | Quotes are inside quotation marks attributed to him; the paraphrases are labelled as PPC Land's in the unit. |
| 19 | §2 | Traffic source definitions (six table rows) | https://support.google.com/youtube/answer/1714921?hl=en-GB | PASS | All quoted definitions verbatim; the page labels the last two "External sources" and "Direct or unknown sources". |
| 20 | §2 | FAQ: "You released a new video in a series…"; "Viewers, on average, are subscribed to dozens of channels…" | https://support.google.com/youtube/answer/141805?hl=en | PASS |  |
| 21 | §2 | Beaupré on subscribers: "10% or less click-through rate", "even your best videos, 90% of the time…", "The number one place…"; subscriptions feed small in paraphrase | https://ppc.land/subscribers-skip-90-of-uploads-in-their-feed-youtube-director-says/ | PASS | The "even your best videos" sentence stands in quotation marks in the article without its own speaker tag, directly after the attributed 10% quote. |
| 22 | §2 | Android Studio app path (Content, video, Analytics card, Reach); "Thumbnail impressions" naming; search terms report | https://support.google.com/youtube/answer/9314355?hl=en | PASS |  |
| 23 | §3 | CTR definition; external sites and end screens not counted; the other six FAQ bullets | https://support.google.com/youtube/answer/7628154?hl=en-GB | PASS | Two sentences were returned truncated and matched as far as shown. |
| 24 | §3 | Focus Digital: "4–6%", January to June 2026, sources named, no sample size; 11 Sep 2026 | https://focus-digital.co/average-youtube-ctr-organic-paid-benchmarks-2026/ | PASS | Page metadata shows it was modified on 5 Nov 2026; the byline date is 11 Sep 2026. |
| 25 | §3 | Retention report: Intro, spikes, dips, 60 seconds and 100 views, "all YouTube videos of similar length" | https://support.google.com/youtube/answer/9314415?hl=en | PASS |  |
| 26 | §3 | Typical retention ("the last 10 of your videos of a similar length"); "A typical intro is about 30 seconds long"; 50% and the "above typical intros" list | https://support.google.com/youtube/answer/12942217?hl=en | PASS |  |
| 27 | §3 | vidIQ: "5 to 15 minutes: aim for 40 to 55% viewed"; "vidIQ guidance for target bands"; own channel 30.3% across 16.5M views, 26 Jun 2025 to 25 Jun 2026; updated 21 Jul 2026 | https://vidiq.com/blog/post/average-view-duration/ | PASS |  |
| 28 | §3 | Test & Compare: up to 3, computers only, advanced features, no Shorts, "Not enough impressions", "Inconclusive", default-title sentence, watch time over CTR | https://support.google.com/youtube/answer/16391400?hl=en | PASS |  |
| 29 | §3 | Packaging changes: "can lead to a shift in its performance…", "recommended when a video has a lower click-through rate (CTR)…", "not to change what is already working well" | https://support.google.com/youtube/answer/16559651?hl=en | PASS | The second sentence was returned truncated after "(CTR)"; the "fewer impressions than usual" half was not re-read in this run. |
| 30 | §4 | Four FAQ quotes on old videos and "regardless of when that video was uploaded" | https://support.google.com/youtube/answer/141805?hl=en | PASS |  |
| 31 | §4 | "Qualified watch hours gained from long-form videos that you've set to public"; private, unlisted, deleted and Shorts do not count | https://support.google.com/youtube/answer/72851?hl=en-GB | PASS | The page also excludes ad campaigns. |
| 32 | §4 | Answer 12843009: "8,000 qualified watch hours in the last 365 days, or 20M qualified Shorts views in the last 90 days", with 1,000 subscribers | https://support.google.com/youtube/answer/12843009 | unverifiable | Page not opened: no search in this run returned its URL. The figures themselves are confirmed by the 10 Aug 2026 blog post. |
| 33 | §4 | Metricool: peak in first three days; about 83% of interactions within ten days; "keeps earning views for months" | https://metricool.com/youtube-trends/ | PASS |  |
| 34 | §5 | Formats "will not inherently confuse the algorithm"; long-form viewers may see Shorts; "Any perceived effect…" | https://support.google.com/youtube/answer/16559651?hl=en | PASS |  |
| 35 | §5 | Related video on a Short; "only available with advanced feature access"; blog guide 14 Jul 2026, "billions of daily views", no conversion figure | https://support.google.com/youtube/answer/14075157?hl=en; https://blog.youtube/creator-and-artist-stories/youtube-related-videos-traffic-guide/ | PASS |  |
| 36 | §5 | Metricool: 8,789 at about five Shorts a month, 5,985 global, 4,364 with none; 35+ falls back; "Correlation isn't causation here…" | https://metricool.com/youtube-trends/ | PASS |  |
| 37 | §5 | vidIQ first ten: Shorts 1,362 and 1,344; long-form 180 and 272; three caveat quotes; "no incremental growth, in fact a slight decline over time" | https://vidiq.com/research/youtube-first-10-videos-study/ | PASS | Best-of-ten 1,948 (D2 YT2) also confirmed. |
| 38 | §5 | OverseerOS: 370 videos, 37 channels, 1.021, 19 of 37, subset of 16 at 0.754, "found no consistent evidence…", 1 Sep 2026, no subscriber finding | https://www.overseeros.com/blog/do-youtube-shorts-hurt-long-form-views | PASS |  |
| 39 | §5 | OverseerOS: 9,982 Shorts at least 30 days old, about eight days; "Among 1,546 Shorts starting below 1,000 views, none gained another 1,000 views during that interval"; "selected, not random"; 8 Nov 2026 | https://www.overseeros.com/blog/do-youtube-shorts-get-views-after-30-days | PASS | The quoted sentence is in the page's opening summary; median interval 7.9 days. |
| 40 | §5 | AIR states "0.04% to 0.5% Shorts-to-long-form conversion" with no definition, method, source or sample | https://air.io/en/audience-growth/do-youtube-shorts-help-your-long-form-videos-grow-data-from-18000-channels | PASS |  |
| 41 | §6 | Break and cadence quotes; PPC Land reports a German-language FAQ in the YouTube Help community on 2 Sep 2026 with two Help Center pages | https://support.google.com/youtube/answer/141805?hl=en; https://ppc.land/youtube-finds-no-link-between-upload-breaks-and-view-counts/ | PASS | The English page shows no date, as the unit says. |
| 42 | §6 | "To grow regular viewers, publish content regularly and maintain a strong connection with your audience" | https://support.google.com/youtube/answer/13615784?hl=en | PASS |  |
| 43 | §6 | AIR cadence: 18,000 channels, US/UK/Canada/Australia, 100K–1M tier; Home and DIY 83,050 (116), 114,000 (178), 105,000 (130), 90,700 (87); 14+ day gaps; predictable schedule; "correlational data, not causal"; no effect size for the gap finding | https://air.io/en/audience-growth/does-posting-more-on-youtube-help-we-studied-18000-channels-to-find-out | PASS | Author Mariia Loboda, 8 Jun 2026. |
| 44 | §6 | Metricool: 2 to 4 long-form posts a week best per post, about 10,552 views; under once a week weakest monthly result | https://metricool.com/youtube-trends/ | PASS |  |
| 45 | §7 | Tags "play a minimal role in your video's discovery"; useful where "commonly misspelled"; title, thumbnail, description matter more | https://support.google.com/youtube/answer/146402?hl=en | PASS |  |
| 46 | §7 | AIR titles: 18,080 channels, 100K–100M monthly views, 11 niches; engagement definition; "the universal sweet spot" at 30 to 50; keyword in first 40%; Home and DIY finished-project finding; caveats; period not stated; titles not separated from thumbnails | https://air.io/en/audience-growth/how-to-write-a-youtube-title-that-gets-clicked-research-across-11-niches | PASS | Page H1 matches the Sources entry; author Nataliia Prokopchuk, 12 Jun 2026. |
| 47 | §8 | 4 Dec 2025: title testing in Test & Compare, global, up to three titles, thumbnails or pairs, long-form, desktop, watch time | https://www.searchenginejournal.com/youtube-title-a-b-testing-rolls-out-globally-to-creators/562571/ | PASS |  |
| 48 | §8 | Shift in Shorts ranking from mid-Sep 2025; YouTube "hasn't confirmed any algorithm change"; SEJ 5 Dec 2025 | https://www.searchenginejournal.com/youtube-shorts-algorithm-may-now-favor-fresh-over-evergreen/562661/ | PASS |  |
| 49 | §8 | "Videos that are made with AI can be recommended as broadly as videos made without AI" | https://support.google.com/youtube/answer/16089387?hl=en | PASS |  |
| 50 | §9 | Item 6: Mario Joos, on X, 30 Nov 2025, "satisfied watch time per click", reported by PPC Land 2 Dec 2025; YouTube gave no explanation | https://ppc.land/youtube-creators-report-drops-in-shorts-viewership-after-september-algorithm-change/ | PASS | PPC Land dates his disclosure 30 Nov 2025; the X post it embeds is stamped 29 Nov 2025. The unit follows PPC Land's date. His full phrase is "expected satisfied watch time per click from impressions". |
| 51 | §9 / D2 YT11 | "Audience segments do not affect reach or monetization"; regular = at least once a month for more than 6 months in the past year | https://support.google.com/youtube/answer/10246996?hl=en | PASS | Answer 13615784 words the same definition as "at least six months"; the unit cites 10246996, which says "more than 6 months". |
| 52 | D2 YT10 | "3,000 for fan funding (answers 12843009, 72851)" | https://support.google.com/youtube/answer/12843009; https://support.google.com/youtube/answer/72851?hl=en-GB | unverifiable | 12843009 was not opened. The en-GB page 72851, as read, gave no fan-funding threshold (it links to a video on earlier access). The 10 Aug 2026 blog says fan-funding thresholds are unchanged but prints no number. The 3,000 could not be confirmed at either cited page. |
| 53 | D2 YT11 / T2 YT11 | Metric named "Returning, casual and regular viewers" | https://support.google.com/youtube/answer/10246996?hl=en | FAIL | The cited page names three segments: "New viewers", "Casual viewers", "Regular viewers". "Returning" is not one of them (casual and regular viewers together are the returning ones). PB10 repeats the label, so it is reported as a flag. |
| 54 | §7 | AIR: "titles of over 90 characters underperforming on views" | https://air.io/en/audience-growth/how-to-write-a-youtube-title-that-gets-clicked-research-across-11-niches | FAIL | The page's bucket is "90+" ("90+ character titles consistently underperform on views"); it does not say "over 90". A one-character boundary; minor. |

## Not checked

- https://support.google.com/youtube/answer/12843009: not checked, no WebSearch in this run returned this URL, so it could not be fetched under the web rule
- WebSearch: the turn's search budget ran out after 34 searches; one further search (fan-funding threshold) was refused and not retried by other means
- https://www.searchenginejournal.com/youtube-algorithm-myths-debunked-insights-from-the-growth-team/510091/: first fetch refused by permission; retried once and read (checked)
- Not opened, and nothing rests on them here: the iPhone version of the reach page (the unit says it was not read); YouTube's Creator Insider videos behind the press reports; the German-language community FAQ.
- A second YouTube blog URL for the Partner Programme post appeared in search results (`blog.youtube/news-and-events/youtube-partner-program-updates-2027-new-opportunities-earn/`); it was not opened. The URL the unit cites opened and carries the post.

## Failure rate

- Sample: 0 FAIL of 13 (0%). The rule (more than one in ten) is not met; no full audit.
- All claims checked: 2 FAIL of 54 (3.7%), both minor; 0 STALE; 2 unverifiable.
- Nothing checked had been superseded between 12 and 14 Nov 2026. Answer 72851 still shows the 4,000-hour line as current, with the 1 Feb 2027 change announced, which agrees with the unit.

## Counts

- Words: 10,515 (`wc -w unit.md`). `##` sections: 12.
- Cited claims in the whole unit: 144, counted by `out/count.py`. Rule: outside `viz` blocks, Sources and the Unsure list, each prose sentence, bullet or table row counts once if it names an outside source (a link, a Help answer number, or a named vendor, publication or speaker) or carries a number or quotation inside a paragraph or list that does; rows and sentences resting only on other units of the course or on Mara's invented facts are not counted; blank template rows are not counted.
- Per section: §1 9 · §2 13 · §3 26 · §4 10 · §5 17 · §6 10 · §7 12 · §8 9 · §9 12 · Deliverable 26 · Sources 0 · Unsure list 0.

## Figures

| Figure | Checked against | Result |
|---|---|---|
| §2 compare, share of organic views by source | §2 text: 61, 11, 9, 5.77, 5.05, 3; 799,718 videos; 71,177 accounts; 29 Jul and 4 Aug 2026 | PASS |
| §3 decision, reading one upload's click-through rate | §3 FAQ bullets (a week old, 100 views, clickbait signature, lower CTR at high impressions, compare over the long term); caption's exception for rule R2 | PASS |
| §4 compare, share of first-week views by band | §4 text: 54.1, 34.6, 10.8, 0.5; 38,229,639 videos; 15 Aug to 5 Sep 2026; median 234; 16 Sep 2026 | PASS |
| §5 matrix, Shorts and a long-form channel | §5 text for all seven rows; caption dates 29 Jul, 28 Jul, 28 May and 1 Sep 2026 | PASS |

No figure adds a fact, and each caption says what it shows and where its data comes from. No FIX.

## Deliverable

- **Exists in full.** D1 has eleven rules, each with evidence, a grade and a label, and the grades are defined. D2 has twelve rows with all six asked-for columns, worked for the Q1 review on Monday 5 April 2027. T1 and T2 follow, and every blank says what goes in it.
- **Follows from the evidence.** Each rule's evidence cell repeats a claim checked above. Conventions are marked as conventions (R6's selection rule, R7's date, R8's hours decision). R4 quotes answer 13615784 for two strings the body does not use; both are on the page (S10).
- **Dates and arithmetic hold.** 5 Jan 2027 is a Tuesday; 5 Apr and 5 Jul 2027 are Mondays. On 5 Apr, uploads 1 to 5 are 34 days old or more, upload 6 is 20 days old and upload 7 is 6 days old, as YT2 and YT3 say. Mara's first title is 82 characters and "teak" starts at character 13.
- **Usable without the unit, with two limits.** Evidence cells cite Help pages by answer number and vendors by short name, so a reader needs the Sources list to open them. R10 gives only the half of YouTube's sentence that supports it (erratum PB6-2).
- **Two cells could not be confirmed.** YT10's "3,000 for fan funding" was not found at 72851 as read, and 12843009 was not opened. YT11's metric name does not match the cited page (flags PB6-3 and PB6-4).

## Mara's facts and pointers to other units

- **Register:** every Mara fact in the unit agrees with `case-facts.md` (channel name, cadence, upload dates 5 Jan to 30 Mar 2027, review dates, phone only, no Shorts in year one, title and search rule, packaging check, rows YT1 to YT12, 24.0 hours per four weeks). "(Mara, fictional)" is on her first use. None of her numbers is used as evidence.
- **Pointers, all found:** PB1 rows Y1, Y2, Y3, Y4, Y6, Y10, Y11, §2, §4 and D3 (stop rule, verdict 3 as corrected, the Q1 note); PB3 §4 and D2; PB4 §2, §7 and D1 ("Never publish two videos in one week to catch up"); PB5 §3 and §7 (the title, the promise test, Test & Compare on computers only); PB10 (60-minute review, rows YT1 to YT12, R6, the Shorts test at the twelve-month review); DD-PB1 reads rules R3, R4, R7, R8, R10 and R11.
- **One cross-unit point:** PB10 carries the same "Returning, casual and regular viewers" label for YT11 (see flags).

## Course goal and sourcing standard

- **Goal.** The unit serves the third outcome directly: it gives the YouTube rows the quarterly review reads, each set against a sourced benchmark or marked as own-baseline only. The brief's ten topics are all covered.
- **Sourced where made.** Every number, mechanism and recommendation sampled had its source beside it. Vendor data is labelled vendor and correlational, survivor samples are named, executive statements via the press are labelled, and paraphrases are attributed to PPC Land. Sources lists exactly the 38 URLs linked in the body, no more and no fewer.
- **Advice without evidence.** None found. Rules with no source are marked "convention" and inferences are marked as inferences.
- **Platform and dates.** Every claim is about YouTube; facts that can change carry 12 Nov 2026 or their own date.
- **Private course.** No reference to it or to its reader was seen.
- **Process language (observation, no erratum).** The correction line after the templates and the last Unsure-list item carry internal codes ("P100", "flag F42", "P49"). PB1's correction lines do the same, so this looks like the course's convention for those lines.

## Verdict

**PB6: PASS.** No full audit was run (0 of 13 sampled claims failed). No section needs rewriting.

## Most consequential errors

None is consequential. In order of weight:

1. D2 row YT10 cites two pages for "3,000 for fan funding" and neither could be confirmed: one was not opened, and the other, as read, does not print the figure. This is unverifiable, not shown wrong; the next check should open answer 12843009.
2. The YT11 metric is called "Returning, casual and regular viewers"; YouTube's page calls the segments new, casual and regular. PB10 repeats the label.
3. §7 says AIR found titles of "over 90" characters underperform; AIR's bucket is "90+".

## Bibliography line

No new source to add and none to mark failed; note against YouTube Help answer 12843009 that it was not opened in this audit, and that vidIQ's 3,332,098 is a sum of three band counts.

## Changelog line

2026-11-14 · Audit 2, PB6 · claude-fable-5-2 · stratified sample 13 claims, 0 FAIL; 54 checked, 2 minor FAIL, 0 STALE, 2 unverifiable (answer 12843009 not opened); four figures PASS; verdict PASS; 2 minor errata, 2 flags (YT11 label, shared with PB10).

## Errata

**PB6-1** · erratum · severity minor · verdict FAIL · §7 · Titles and search for a small channel (What the title data says)
- Current: `titles of over 90 characters underperforming on views`
- Fix: `titles of 90 or more characters underperforming on views`
- Basis: AIR Media-Tech's length buckets are "under 30, 30–50, 50–70, 70–90, 90+ characters", and the finding reads "90+ character titles consistently underperform on views"; the page does not say "over 90". https://air.io/en/audience-growth/how-to-write-a-youtube-title-that-gets-clicked-research-across-11-niches

**PB6-2** · erratum · severity minor · verdict other · Deliverable · D1, rule R10
- Current: `| "Publish time is not known to impact a video's long-term performance" (answer 141805) | Strong |`
- Fix: `| "Publish time is not known to impact a video's long-term performance", although publishing when the audience is most active "can be beneficial for early viewership" (answer 141805) | Strong |`
- Basis: The same FAQ answer carries both halves, and §9 item 8 of the unit gives both; the deliverable row, which must stand without the unit, gives only the half that supports the rule. https://support.google.com/youtube/answer/141805?hl=en

**PB6-3** · flag · severity minor · verdict FAIL · Deliverable · D2, row YT11
- Current: `| YT11 | Returning, casual and regular viewers |`
- Fix: `| YT11 | New, casual and regular viewers |`
- Basis: The cited page names the three segments "New viewers", "Casual viewers" and "Regular viewers"; "returning" is not a segment name. Flag, not erratum: PB10 (D1, row YT11) uses the same label "Returning, casual and regular viewers", so the two units would have to change together. https://support.google.com/youtube/answer/10246996?hl=en

**PB6-4** · flag · severity minor · verdict FAIL · Deliverable · Templates, T2, row YT11
- Current: `| YT11 | Returning, casual, regular viewers |`
- Fix: `| YT11 | New, casual, regular viewers |`
- Basis: Same finding as PB6-3, second occurrence (the template row). https://support.google.com/youtube/answer/10246996?hl=en

Each Current was counted once in `unit.md` with `grep -c -F`.
