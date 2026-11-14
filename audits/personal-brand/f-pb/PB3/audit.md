Model: claude-fable-5-2

# PB3 · Audience and the two platforms · stratified-sample audit (course PB, Audit 1)

Date: 14 November 2026. Search: on. Auditor: one fresh, isolated agent; this unit only.

## Provenance

- Unit audited: `unit.md` (PB3, written 2026-11-12 by Opus 5.5, search on). Not edited.
- Read: `PROMPT.md`, `brief.txt`, `sourcing-parts-1-and-5.md`, `case-facts.md`, `fresh-check-PB3.md` (read so as not to re-report what was fixed; none of its verdicts reused), `others/` for pointers.
- No working files from an earlier run were in `out/`; this is a first run.
- Web rule followed: WebSearch first; WebFetch only on a URL a search in this agent returned verbatim.

## Sample (recorded before any check)

One claim per `##` section (10 sections).

| # | Section | Sampled claim | Source cited |
|---|---|---|---|
| S1 | §1 | Instagram account insights break down by "age, city, country, gender"; follower demographics "Not returned if the IG User has less than 100 followers" | Meta for Developers, Instagram account insights reference |
| S2 | §2 | Pew fact sheet of 19 Oct 2026: NPORS, 5,511 US adults, fieldwork 30 Jan to 18 Jun 2026, ±1.8 points; YouTube 84%, Instagram 51% of all adults (with the age rows) | Pew Research Center, Americans' Use of Social Media in 2026 |
| S3 | §3 | Fanpage Karma: "more than 3 million" posts, Jan–Apr 2026; under 10,000 followers median reach 4.9% Reels, 3.5% image posts, 2.6% carousels; interaction 0.51% against 0.34%; "nearly three times as many non-followers as carousels" | Fanpage Karma, 7 Aug 2026 |
| S4 | §4 | vidIQ First 10 Videos: median 30-day views about 180 → 272 for long-form (137,355 channels), about 1,362 → 1,344 for Shorts (367,243 channels); "no incremental growth, in fact a slight decline over time" | vidIQ, 28 Jul 2026 |
| S5 | §5 | beehiiv: average open rate 41.24% in 2025 across 28 billion emails; 37.98% for 2024 in text, 37.67% in graphic; dated 6 Jan 2026 | beehiiv, The State of Newsletters 2026 |
| S6 | §6 | Buffer: 2.1 million feed posts, 102,000 accounts, fixed effects; growth rate higher by 0.12% / 0.26% / 0.44% / 0.66% by band; reach per post about 12% higher at 3–5 than at 1–2 | Buffer, 13 Aug 2025 |
| S7 | Deliverable (D1 trait 2) | 48% of the EU population lived in a flat in 2024; two thirds of US housing units had a garage or carport in 2021 | Eurostat, Housing in Europe 2025; US DOE FOTW 1268 |
| S8 | Template (T2, T1) | The totals row caps (12, 24, 40 hours per four weeks) and the "first quarterly review date, from PB1" pointer agree with the body and with PB1 | unit §6/D2; others/PB1 |
| S9 | Sources | Metricool (Gretchen Oestreicher), "YouTube Trends 2026: what 799,718 videos tell us about views, Shorts, and watch time", 29 Jul 2026, modified 4 Aug 2026 | metricool.com/youtube-trends/ |
| S10 | Unsure list | OverseerOS, 8 Nov 2026: about eight days of observation per Short; "90.5% gained views" | OverseerOS, Do YouTube Shorts get views after 30 days? |

## Table: the sample

| # | Section | Claim | Source | Verdict | Note |
|---|---|---|---|---|---|
| S1 | §1 | Instagram insights break down by "age, city, country, gender"; demographics "Not returned if the IG User has less than 100 followers" | https://developers.facebook.com/docs/instagram-platform/api-reference/instagram-user/insights | PASS | Both strings are on the page as quoted. |
| S2 | §2 | Pew fact sheet 19 Oct 2026: NPORS, 5,511 US adults, 30 Jan–18 Jun 2026, ±1.8 points; YouTube 84%, Instagram 51%; four age rows | https://www.pewresearch.org/internet/fact-sheet/social-media/markdown | PASS | Date, survey, sample, fieldwork, margin and all ten age and total cells match. |
| S3 | §3 | Fanpage Karma: more than 3 million posts, Jan–Apr 2026; under 10,000 followers median reach 4.9% Reels, 3.5% image posts, 2.6% carousels; interaction 0.51% against 0.34%; "nearly three times as many non-followers as carousels" | https://www.fanpagekarma.com/insights/instagram-format-reach/ | PASS | All figures and the quotation match; published 7 Aug 2026, modified 28 Aug 2026; account count not stated, as the unit says. |
| S4 | §4 | vidIQ First 10 Videos: about 180 → 272 (137,355 long-form channels), about 1,362 → 1,344 (367,243 Shorts channels); "no incremental growth, in fact a slight decline over time" | https://vidiq.com/research/youtube-first-10-videos-study/ | PASS | Figures, cohort sizes, the 90-day ten-upload criterion, dates and the quoted words match; the page reports no Shorts-to-subscriber or Shorts-to-long-form finding. |
| S5 | §5 | beehiiv: 41.24% average open rate in 2025 across 28 billion emails; 37.98% for 2024 in text, 37.67% in graphic; 6 Jan 2026; "auto-loads images"; bot filtering | https://www.beehiiv.com/blog/the-state-of-newsletters-2026.md | PASS | All match, including the text/graphic discrepancy the unit reports. |
| S6 | §6 | Buffer: 2.1 million feed posts, 102,000 accounts, fixed effects, Stories excluded; +0.12% / +0.26% / +0.44% / +0.66%; about 12% more reach per post at 3–5 than at 1–2 | https://buffer.com/library/how-often-to-post-on-instagram/ | PASS | All match; 13 Aug 2025, Kirsti Lang. The page writes the growth differences with a % sign and never says "points"; the unit reads them as points of weekly growth rate, the reading PB1 uses. 3–5 is the band Buffer recommends. |
| S7 | Deliverable | D1 trait 2: 48% of the EU population lived in a flat in 2024 (Eurostat, 2025 edition); two thirds of US housing units had a garage or carport in 2021 (DOE FOTW 1268, Census data) | https://ec.europa.eu/eurostat/web/interactive-publications/housing ; https://www.energy.gov/cmei/vehicles/articles/fotw-1268-december-12-2022-2021-two-thirds-us-housing-units-had-garage-or | PASS | Eurostat: 2025 edition, 48% in a flat in 2024. DOE: 12 Dec 2022, "two-thirds of all housing units", Census Bureau housing survey data; "about one third without" is the unit's derivation and is labelled. |
| S8 | Template | T2 total caps (12, 24, 40 hours per four weeks) and T1 "first quarterly review date, from PB1" agree with the body and with PB1 | unit.md §6 and D2; others/PB1 D3 | PASS | 3, 6 and 10 hours × 4 weeks; PB1 D3 sets the checkpoints and PB2 D5 uses the same pointer. The template states no outside fact. |
| S9 | Sources | Metricool (Gretchen Oestreicher), "YouTube Trends 2026: what 799,718 videos tell us about views, Shorts, and watch time", 29 Jul 2026, modified 4 Aug 2026 | https://metricool.com/youtube-trends/ | PASS | Title, author and both dates match the page. |
| S10 | Unsure list | OverseerOS, 8 Nov 2026: about eight days of observation per Short; "90.5% gained views" | https://www.overseeros.com/blog/do-youtube-shorts-get-views-after-30-days | PASS | Median interval 7.9 days; 90.5% (9,036 of 9,982) gained views; dated 8 Nov 2026. |

## Also checked (beyond the sample; counted in the totals, not in the decision rule)

| # | Section | Claim | Source | Verdict | Note |
|---|---|---|---|---|---|
| 11 | §1 | Instagram lists Reels signals "roughly in order of importance", starting "Your activity", then "Your history of interacting with the person who posted"; four headings, none is age or gender | https://about.instagram.com/blog/announcements/instagram-ranking-explained | PASS | 31 May 2023, Adam Mosseri; wording and the four headings match. |
| 12 | §1 | YouTube Help: "The algorithm aims to understand a viewer's interest across Shorts, long videos, live streams, and posts"; "individual preferences vary, not just by topic but also by format" | https://support.google.com/youtube/answer/16559651?hl=en | PASS |  |
| 13 | §1 | YouTube Audience reports "Channels that your audience watches", "What your audience watches", "Formats your viewers watch on YouTube" | https://support.google.com/youtube/answer/9314416 | PASS | Report names match exactly. |
| 14 | §1 | YouTube: data limited "when metrics do not meet a certain threshold"; thresholds not published; "Not enough demographic data" | https://support.google.com/youtube/answer/9101241?authuser=1 | PASS | Opened at the ?authuser=1 address a search returned; the plain address the unit cites was not returned by search. |
| 15 | §2 | Pew rows for men, women, education and income; derived gaps of 13 and 17 points | https://www.pewresearch.org/internet/fact-sheet/social-media/markdown | PASS | 85/45, 83/56, 77/42, 90/59, 77/42, 90/59; 90−77 = 13, 59−42 = 17. |
| 16 | §2 | Ofcom, 10 Dec 2025: YouTube "used by 94% of adults"; "reaching an average of 51 minutes a day, not including the TV set"; no Instagram figure, no panel or fieldwork dates | https://www.ofcom.org.uk/media-use-and-attitudes/online-habits/from-apps-to-ai-search-how-the-uk-goes-online-in-2025 | PASS |  |
| 17 | §3 | Beaupré (senior director of growth and discovery), Creator Insider interview of 1 Sep 2026: four quotations; PPC Land 2 Sep 2026; transcript misspells the names | https://ppc.land/subscribers-skip-90-of-uploads-in-their-feed-youtube-director-says/ | PASS | All four quotations, the title and both dates match PPC Land. The video itself was not opened, as the unit also says. |
| 18 | §3 | YouTube Help: "Viewers, on average, are subscribed to dozens of channels and may not return for every new upload" | https://support.google.com/youtube/answer/141805?hl=en | PASS |  |
| 19 | §3 | Instagram on Feed, Stories, Explore and Reels (four quotations) | https://about.instagram.com/blog/announcements/instagram-ranking-explained | PASS |  |
| 20 | §3 | Mosseri, Jan 2025: "The top three signals that matter most for ranking are watch time, likes and sends"; likes for connected, sends for unconnected content | https://www.socialmediatoday.com/news/instagram-shares-algorithm-insights-2025/738034/ | PASS | 22 Jan 2025, Andrew Hutchinson. |
| 21 | §3 | Trial reels "will be shown to non-followers first"; metrics about 24 hours later; "globally available to all eligible creators" forecast in Dec 2024; eligibility left to the Help Centre; 10 Dec 2024, updated 26 Jun 2025 | https://about.fb.com/news/2024/12/trial-reels-try-content-non-followers/ | PASS |  |
| 22 | §3 | Instagram, 30 Apr 2024: eligible content "is shown to a small audience that we think will enjoy it"; "the top performing set of reels are shown to a slightly wider audience" | https://creators.instagram.com/recommendations-and-originality | PASS |  |
| 23 | §3 | Fanpage Karma "reach within the existing community": 2.1% image posts, 2.0% Reels, under 10,000 followers | https://www.fanpagekarma.com/insights/instagram-format-reach/ | PASS |  |
| 24 | §3 | YouTube Help on new channels: four quotations ("naturally drawn", "takes time", "critical mass of content", "delve deeper into your channel") | https://support.google.com/youtube/answer/16559651?hl=en | PASS |  |
| 25 | §3 | YouTube Help: "binging" old videos; a new video in a series | https://support.google.com/youtube/answer/141805?hl=en | PASS |  |
| 26 | §3 | YouTube Help: viewers do not watch in chronological order; right videos "regardless of when that video was uploaded" | https://support.google.com/youtube/answer/141805?hl=en | PASS |  |
| 27 | §3 | Metricool: 799,718 videos, 71,177 accounts; peak in first three days; roughly 83% of interactions within ten days; "keeps earning views for months" | https://metricool.com/youtube-trends/ | PASS |  |
| 28 | §3 | OverseerOS: 9,982 Shorts, 676 channels, 30+ days old; median gain 57; the 1,546-Shorts sentence; "selected, not random" | https://www.overseeros.com/blog/do-youtube-shorts-get-views-after-30-days | PASS |  |
| 29 | §3 | Socialinsider: 25,503,389 Reels of brand accounts with 1,000 to 1 million followers, 2025; "golden window"; the 45% sentence; second sample of 40 million Reels from 450,000 accounts; 21 Jan 2026, updated 6 Nov 2026 | https://www.socialinsider.io/blog/how-long-does-it-take-for-reels-to-get-views/ | PASS | All match. The page's own follower range is unclear as the reader returned it (a "1K–1M" statement, an exclusion line naming 100,000, and a breakdown with an under-5,000 bucket); the unit already labels the page "internally unclear". No erratum. |
| 30 | §4 | YouTube Help on Shorts and long-form: three quotations | https://support.google.com/youtube/answer/16559651?hl=en | PASS |  |
| 31 | §4 | Net Influencer, 23 May 2025: Todd Sherman, Shorts product lead, on Creator Insider; paraphrase, no quote, no data | https://www.netinfluencer.com/youtube-debunks-common-myths-about-shorts-as-format-gains-traction/ | PASS |  |
| 32 | §4 | YouTube Help: "a clickable link below your channel handle"; "is only available with advanced feature access" | https://support.google.com/youtube/answer/14075157?hl=en | PASS |  |
| 33 | §4 | YouTube Blog guide of 14 Jul 2026 gives no figure for viewers following the link | https://blog.youtube/creator-and-artist-stories/youtube-related-videos-traffic-guide/ | PASS | Date and the absence of a rate confirmed. The page's title differs from the one in Sources (see erratum PB3-4). |
| 34 | §4 | AIR Media-Tech Shorts study: 18,000 English-language channels, 40+ videos and 10+ long-form, Mar 2025–Mar 2026; 41%, 39%, 37%; Home and DIY 95,100/94,600 and 251,500/256,000; "0.04% to 0.5%"; "measured subscriber counts, not cross-format viewing rates directly"; correlational | https://air.io/en/audience-growth/do-youtube-shorts-help-your-long-form-videos-grow-data-from-18000-channels | PASS | 28 May 2026, Olha Kapinos. |
| 35 | §4 | Metricool: about five Shorts a month, 8,789 views per long-form video against 5,985; correlation by its own account | https://metricool.com/youtube-trends/ | PASS |  |
| 36 | §4 | OverseerOS, 1 Sep 2026: 370 long-form videos, 37 channels; "no consistent evidence…"; "cannot observe competitor impression allocation"; no cross-format rate | https://www.overseeros.com/blog/do-youtube-shorts-hurt-long-form-views | PASS |  |
| 37 | §5 | GetResponse: more than 4.4 billion messages in 2023, senders with at least 500 contacts; 39.64% open rate; Mail Privacy Protection sentence | https://www.getresponse.com/resources/reports/email-marketing-benchmarks?frame=0 | PASS | The report page opened this time (the fresh check could not open it). The page's country and industry "All" rows show other averages (38.33%, 42.53%); 39.64% is the figure its FAQ gives. |
| 38 | §5 | GetResponse landing pages: 10.76% average (subscription rate); 0.7% retail; 39.93% restaurants and food | https://www.getresponse.com/resources/reports/email-marketing-benchmarks?frame=0 | PASS |  |
| 39 | §5 | Substack, 22 Feb 2024: network "drives 50% of all new subscriptions and 25% of new paid subscriptions on Substack" | https://on.substack.com/p/substacks-recommendations-network | PASS |  |
| 40 | §5 | beehiiv: newsletters using Recommendations grew "2.75x faster on average" | https://www.beehiiv.com/blog/the-state-of-newsletters-2026.md | PASS |  |
| 41 | §5 | beehiiv Free plan: $0, "Up to 2,500" subscribers, landing pages, "Unlimited email sends" | https://www.beehiiv.com/pricing?via=start | PASS | Confirmed at pricing?via=start (search-returned). beehiiv's pricing.md, also opened, gives $0, "Up to 2,500" and unlimited sends but lists "Custom pages: 1" and a website builder, with no "landing pages" line. The plain pricing address the unit cites was not returned by search. The unsure list already discloses this. |
| 42 | §5 | EUR-Lex address is Regulation (EU) 2016/679, the General Data Protection Regulation | https://eur-lex.europa.eu/eli/reg/2016/679/oj | PASS | The fresh check could not open this page; it opens and is the regulation. |
| 43 | §5 | FTC, "CAN-SPAM Act: A Compliance Guide for Business", Aug 2023, updated 22 Jul 2025 | https://www.ftc.gov/business-guidance/resources/can-spam-act-compliance-guide-business?frame=0 | PASS | Opened at the ?frame=0 address a search returned: published August 2023, last modified 22 Jul 2025. |
| 44 | §6 | vidIQ uploads study: 32,926,088 channels under 1,000 subscribers, 360 days; 1.86%, 8.65%, 30.77%; both caveats quoted; 11 Sep 2026 | https://vidiq.com/research/youtube-uploads-1000-subscribers/ | PASS |  |
| 45 | §6 | AIR Media-Tech posting study: 18,000 channels in four countries, 100,000–1 million monthly views; Home and DIY 114,000 (178 channels) against 90,700 (87); schedule finding; "went dark for 14+ days three or more times a year"; "This is correlational data, not causal"; 8 Jun 2026 | https://air.io/en/audience-growth/does-posting-more-on-youtube-help-we-studied-18000-channels-to-find-out | PASS |  |
| 46 | §6 | YouTube Help: "We studied thousands of channels that took a break and found no correlation between break length and changes in views"; no sample size, period or method | https://support.google.com/youtube/answer/141805?hl=en | PASS |  |
| 47 | Deliverable | D1 trait 1: Censuswide for uShip, 2,003 US consumers, 23–28 May 2024; 48% have bought used furniture; 78% of those likely to again; mid-century not sized | https://businesswire.com/news/home/20240719968636/en/The-Secondhand-Furniture-Phenomenon-What-48-of-Americans-Know-That-You-Dont | PASS | The page text carries no dateline; 19 Jul 2024 is in its address. |
| 48 | Deliverable | D1 trait 3: "36% of US home-improvement projects in 2023 were done by do-it-yourselfers (50 million of 140 million)" | https://www.census.gov/content/dam/Census/library/visualizations/2024/demo/2023%20Home%20Improvements%20Infographic.pdf | FAIL | The figures are right (36%; about 50 million of about 140 million). The date and population are not: the infographic reports homeowners' projects from the 2023 American Housing Survey, heads its spending "2021–2023", and nowhere says the projects were done in 2023. Minor. Erratum PB3-5. |
| 49 | Deliverable | D1 trait 4: Pew, 7 Nov 2018: 51% of US YouTube users (35% of all adults); 4,594 adults, 29 May–11 Jun 2018 | https://www.pewresearch.org/data-labs/2018/11/07/many-turn-to-youtube-for-childrens-content-news-how-to-lessons/ | unverifiable | The search-returned Pew address failed at the site (client error); not retried, no copy fetched. The /markdown address the unit cites was not returned by search. |
| 50 | Deliverable | D1 trait 7: FeedSpot list of 20 channels, 441K to 1.5K subscribers; mid-century channel 4K; hand-tool channel 3.2K; updated 2 Jul 2026 | https://videos.feedspot.com/furniture_restoration_youtube_channels | PASS |  |
| 51 | Sources | YouTube Blog, "YouTube related videos traffic guide", 14 Jul 2026 | https://blog.youtube/creator-and-artist-stories/youtube-related-videos-traffic-guide/ | FAIL | The page is titled "How to convert YouTube Shorts views into long-form channel growth"; the title in Sources is the address slug put in quotation marks. Date right. Minor. Erratum PB3-4. |
| 52 | §6 | "a fixed schedule is what PB1's stop rule counts" | others/PB1 D3 | FAIL | PB1's stop rule counts uploads per quarter ("fewer than 3 YouTube videos in each of two consecutive quarters"); it does not count a schedule. PB4 §2 states it correctly. Minor. Erratum PB3-6. |
| 53 | Deliverable | D2 arithmetic: column totals 11.75, 24.0, 39.0; 13/26/52 a year and 1.1/2.2/4.3 a month; 7.0 hours a video; 0.14 points and 0.2 followers; hours freed; five-week gap | unit.md D2 tables; https://buffer.com/library/how-often-to-post-on-instagram/ | PASS | Every line recomputed. |
| 54 | Deliverable | Mara's facts and the pointers to PB1 (§1, §8, D2, D3, 150 USD cap, rows Y1/Y4/Y5/I4, 5 Apr 2027) and PB2 (D1 wording, §3 conventions) | case-facts.md; others/PB1, others/PB2 | PASS | All agree with the register and with the units. One loose pointer on PB2's run 2 is flagged (PB3-8). |
| 55 | Sources | Buffer (Kirsti Lang), "How often should you post on Instagram in 2026? What data from 2 million posts tells us", 13 Aug 2025 | https://buffer.com/library/how-often-to-post-on-instagram/ | PASS |  |

## Not checked

- https://www.pewresearch.org/data-labs/2018/11/07/many-turn-to-youtube-for-childrens-content-news-how-to-lessons/: failed at its site (client error); not retried; the unit's /markdown address was not returned by search
- https://support.google.com/youtube/answer/13615375: not opened (no search run for it)
- https://www.legislation.gov.uk/eur/2016/679/introduction: not opened (no search run for it)
- https://www.measure.studio/blog/tiktok-vs-instagram: not opened (the unit cites it only to say it is not used)
- https://www.beehiiv.com/pricing: plain address not returned by search; pricing?via=start and pricing.md opened instead
- https://support.google.com/youtube/answer/9101241: plain address not returned by search; the ?authuser=1 address opened instead
- https://www.ftc.gov/business-guidance/resources/can-spam-act-compliance-guide-business: plain address not returned by search; the ?frame=0 address opened instead
- Creator Insider video of 1 Sep 2026: not opened; quotations checked against PPC Land only
- No tool-permission refusal occurred.

Every page was read through a summarising fetch tool, so "matches" means matches as that reader returned the page's words.

## Failure rate

- Sample: 0 FAIL of 10 sampled claims (0%). The rule (more than one in ten) is not met; no full audit was run.
- All claims checked: 55; PASS 51, FAIL 3 (all three minor, none in the sample), STALE 0, unverifiable 1.
- Counts of the unit: 9437 words (`wc -w`); 10 `##` sections; 109 cited claims, tallied by section by reading: §1 6, §2 19, §3 26, §4 10, §5 8, §6 8, Deliverable 18, Template 0, Sources 0, Unsure list 14. A sentence or table row resting on a cited source counts once; `viz` blocks, the Sources list and pointers to other units are not counted; the Unsure list's count includes its three correction notes.
- Searches 36, fetches 39 (one failed).

## Figures (`viz` blocks)

1. §2, grouped bars, platform use by age: PASS. All ten values and the labels match the §2 table; the caption's date, survey, sample and fieldwork match the text.
2. §3, compare, Instagram reach by format: PASS. 4.9, 3.5 and 2.6 match the text; the caption's date, sample, period and labels match.
3. D2, stacked bars, hours per four weeks: PASS. All 21 values match the hours table; the totals 11.75, 24.0 and 39.0 add up.
4. D2, flow, cut order: PASS. The four steps and their notes match the numbered cut order; the caption's sources and dates match §3 and §6.

## Deliverable

- Exists in full: D1 (one sentence, ten traits with evidence, source and label, and what the profile does not claim) and D2 (roles, posting rates, hours at 3, 6 and 10 a week, the reasons, the cut order at each budget), then T1 and T2 with every blank saying what goes in it.
- Follows from the evidence: every band and figure in D1 and D2 is one the body sources; the arithmetic was recomputed and holds. One gap: the 3-hour paragraph of D2 gives AIR's finding on gaps without YouTube's contrary statement, which §6 has carried since its correction (PB3-7).
- Usable without the unit: yes. D1 carries its own links and labels; D2 names its datasets with dates. Its "(§3)", "(§4)" and "(§6)" pointers are to reasons, and the plan can be followed without them.
- Mara: every fact agrees with `case-facts.md` (age, job, counts, 6 hours, the hours per line doubled to four weeks, One Box Restoration, the Q1 review on Monday 5 April 2027, the email on beehiiv Free, the cut order, the two alternative budgets). She is labelled "(Mara, fictional)" on first use and is never used as evidence.
- Pointers to other units: PB1 §1 (labels; re-reading rows), PB1 §8 (no hours dataset), PB1 D2 and the 150 USD cap, PB1 D3 (stop rule, floor of 3, checkpoints), PB2 D1 (audience wording, verbatim), PB2 §3 (conventions), PB4 (lost-week rule, its §7), PB6 (Shorts revisited), PB7 (format mix, Instagram's statements, the move to YouTube), PB8 (the sign-up question, its §6.6), PB9 (list pricing and the tool comparison) all hold. Two do not hold exactly: §6's "a fixed schedule is what PB1's stop rule counts" (PB3-6) and D1's description of PB2's run 2 (flag PB3-8).

## Course goal and sourcing standard

- Goal: the unit moves the reader toward two of the three outcomes: the audience half of the one-sentence statement, and an hours budget split between the platforms with a cut order, which the twelve-week system needs. It hands PB4 the posting rates, PB6 and PB7 the roles, and PB9 the finding that no follower-to-list rate exists, as its Gives line asks.
- Advice without evidence: none found that is not labelled. Hours per piece are called planning estimates each time; the repeat-back conventions and the 8-minute edit are called unsourced; unmeasured rates are kept out of the deliverable. The roles table's "Minutes per piece" and "Seconds per piece" carry no source; they describe the formats and decide nothing, so no erratum is given.
- Part 1, per unit, "every source it cites is listed": not met. §5 cites EUR-Lex, legislation.gov.uk and the FTC, added after the fresh check, and Sources lists none of them (PB3-1 to PB3-3). One Sources title is not the page's title (PB3-4).
- Part 5: platform named for each growth, format and metric claim; vendor, correlational and survivor labels present; dates given; no country's tax rate or threshold stated; the legal point is a question with a primary source for the EU, the UK and the US, and the unit says it is information, not legal advice. No reference to a private course found.
- Staleness: nothing found superseded. Pew's fact sheet of 19 Oct 2026 is current; Ofcom's page is of 10 Dec 2025 and its next annual report was not looked for.

## Verdict

**PB3: PASS.** 0 of 10 sampled claims failed; no full audit was run. Beyond the sample, three minor failures and four other corrections are listed as errata, and one flag.

## The most consequential errors

1. The Sources list leaves out the three legal sources §5 cites (the GDPR on EUR-Lex, the UK GDPR on legislation.gov.uk, the FTC's CAN-SPAM guide), so the course bibliography would miss them.
2. D1 trait 3 dates the 50 million do-it-yourself projects to 2023 and to the US as a whole; the source gives homeowners' projects from the 2023 survey without dating them. The 36% stands.
3. §6 says PB1's stop rule counts a fixed schedule; it counts uploads per quarter. The cut order does not change.

None of the three changes a number Mara plans with or a decision the unit reaches.

## Bibliography line

Add: European Union, Regulation (EU) 2016/679 (EUR-Lex); legislation.gov.uk, UK GDPR; FTC, "CAN-SPAM Act: A Compliance Guide for Business". Retitle: the YouTube Blog entry of 14 Jul 2026. Mark failed: none. Still unverifiable: Pew, 7 Nov 2018 (the site refused the one address search returned).

## Changelog line

2026-11-14 · PB3 stratified-sample audit (Audit 1, claude-fable-5-2, search on) · PASS · 10 sampled, 0 FAIL; 55 claims checked in all, 3 minor FAIL outside the sample, 0 STALE, 1 unverifiable (Pew 2018) · 7 errata (3 should-fix: Sources omits three §5 sources; 4 minor) and 1 flag (PB2 run 2) · figures 1 to 4 pass · GetResponse report and EUR-Lex, unopened by the fresh check, now opened and confirmed.

## Errata

### PB3-1 · erratum · should-fix · other · Sources

- Current: `- Eurostat, Housing in Europe, 2025 edition (interactive publication), read 12 Nov 2026. https://ec.europa.eu/eurostat/web/interactive-publications/housing`
- Fix (two lines):

```
- European Union, Regulation (EU) 2016/679 of the European Parliament and of the Council of 27 April 2016 (General Data Protection Regulation), EUR-Lex. https://eur-lex.europa.eu/eli/reg/2016/679/oj
- Eurostat, Housing in Europe, 2025 edition (interactive publication), read 12 Nov 2026. https://ec.europa.eu/eurostat/web/interactive-publications/housing
```
- Basis: §5 cites this source and Sources does not list it (standard Part 1, per unit: every source cited is listed). Opened 14 Nov 2026: https://eur-lex.europa.eu/eli/reg/2016/679/oj
- `grep -c -F` on `unit.md`: 1

### PB3-2 · erratum · should-fix · other · Sources

- Current: `- FeedSpot, "20 Furniture Restoration YouTubers in 2026", updated 2 Jul 2026. https://videos.feedspot.com/furniture_restoration_youtube_channels`
- Fix (two lines):

```
- Federal Trade Commission, "CAN-SPAM Act: A Compliance Guide for Business", Aug 2023, updated 22 Jul 2025. https://www.ftc.gov/business-guidance/resources/can-spam-act-compliance-guide-business
- FeedSpot, "20 Furniture Restoration YouTubers in 2026", updated 2 Jul 2026. https://videos.feedspot.com/furniture_restoration_youtube_channels
```
- Basis: §5 cites this source and Sources does not list it. Title and dates confirmed 14 Nov 2026 at the search-returned address https://www.ftc.gov/business-guidance/resources/can-spam-act-compliance-guide-business?frame=0
- `grep -c -F` on `unit.md`: 1

### PB3-3 · erratum · should-fix · other · Sources

- Current: `- Measure Studio (Sweta Panigrahi), "What engagement data reveals about content lifespan in TikTok vs Instagram", 3 Jul 2025, updated 18 Aug 2025. https://www.measure.studio/blog/tiktok-vs-instagram`
- Fix (two lines):

```
- legislation.gov.uk, Regulation (EU) 2016/679 as it applies in the United Kingdom (UK GDPR). https://www.legislation.gov.uk/eur/2016/679/introduction
- Measure Studio (Sweta Panigrahi), "What engagement data reveals about content lifespan in TikTok vs Instagram", 3 Jul 2025, updated 18 Aug 2025. https://www.measure.studio/blog/tiktok-vs-instagram
```
- Basis: §5 cites this source and Sources does not list it. This audit did not open the page (not checked); the reference is built from the unit's own §5 and PB8's citation of the same instrument, and whoever applies it should confirm the page title. https://www.legislation.gov.uk/eur/2016/679/introduction
- `grep -c -F` on `unit.md`: 1

### PB3-4 · erratum · minor · FAIL · Sources

- Current: `- YouTube Blog, "YouTube related videos traffic guide", 14 Jul 2026. https://blog.youtube/creator-and-artist-stories/youtube-related-videos-traffic-guide/`
- Fix: `- YouTube Blog, "How to convert YouTube Shorts views into long-form channel growth", 14 Jul 2026. https://blog.youtube/creator-and-artist-stories/youtube-related-videos-traffic-guide/`
- Basis: The page's title, read 14 Nov 2026; the date is right. https://blog.youtube/creator-and-artist-stories/youtube-related-videos-traffic-guide/
- `grep -c -F` on `unit.md`: 1

### PB3-5 · erratum · minor · FAIL · Deliverable · D1 trait 3

- Current: `36% of US home-improvement projects in 2023 were done by do-it-yourselfers (50 million of 140 million)`
- Fix: `36% of the home-improvement projects US homeowners reported in the 2023 American Housing Survey were done by do-it-yourselfers (about 50 million of about 140 million; the infographic does not date the projects)`
- Basis: The infographic gives homeowners' projects from the 2023 survey, heads its spending figure "2021–2023" and does not say the projects were done in 2023. https://www.census.gov/content/dam/Census/library/visualizations/2024/demo/2023%20Home%20Improvements%20Infographic.pdf
- `grep -c -F` on `unit.md`: 1

### PB3-6 · erratum · minor · FAIL · §6 · What is cut first in a bad week

- Current: `and because a fixed schedule is what PB1's stop rule counts`
- Fix: `and because uploads per quarter are what PB1's stop rule counts`
- Basis: PB1 D3: "fewer than 3 YouTube videos in each of two consecutive quarters"; PB4 §2 says the rule "counts uploads per quarter". others/PB1-what-to-expect-odds-timeline-cost.md (no URL: a pointer inside the course)
- `grep -c -F` on `unit.md`: 1

### PB3-7 · erratum · minor · other · Deliverable · D2, at 3 hours

- Current: `longer than the 14 days AIR associates with fewer views when it recurs.`
- Fix: `longer than the 14 days AIR associates with fewer views when it recurs; YouTube's own FAQ reports no correlation between break length and changes in views (YouTube Help, answer 141805; no sample size, period or method given).`
- Basis: §6 gives both findings since the correction of 12 Nov 2026; the deliverable, which must stand without the body, gives only AIR's. "We studied thousands of channels that took a break and found no correlation between break length and changes in views." https://support.google.com/youtube/answer/141805?hl=en
- `grep -c -F` on `unit.md`: 1

### PB3-8 · flag · minor · other · Deliverable · D1, What the profile does not claim

- Current: `the sentence goes into the second run of PB2's repeat-back test the same day`
- Fix: `the answers from the second run of PB2's repeat-back test, held the same day on one complete video, are read against the sentence`
- Basis: PB2 D5: run 2 shows "one complete video, the most recent" and marks each answer for who and what; no sentence is shown to the five people. A reading of another unit's procedure, so reported as a flag. others/PB2-positioning-the-sentence-a-stranger-can-repeat.md (no URL)
- `grep -c -F` on `unit.md`: 1

