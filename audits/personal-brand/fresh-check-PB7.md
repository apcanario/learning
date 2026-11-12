---
audit: fresh check
unit: PB7 · How Instagram growth works
course: personal-brand · PB · Building a Personal Brand on Instagram and YouTube
model: Opus 5.5 (claude-opus-5-5, as the agent states; this session keeps no agent transcript on disk, so the model could not be confirmed from a transcript's "model" field; live search). A Fable 5.1 fresh check of PB7 is owed to the Fable stage (P49)
date: 2026-11-12
chat: own Opus 5.5 agent context, not shown the writing (P31), launched by the W-PB7/W-PB8 chat (which ran on Opus 5.5 and only staged, applied, filed and published) in session https://claude.ai/code/session_01KMmgQyAmFapUaWMYDKogYn
verdict: fix · 3 errors, 9 should-fix, 7 minor
---

The checker's final report, verbatim, as the file it wrote in its own folder (`out/report.md`), copied unchanged. Saved before any finding was applied.

Model: claude-opus-5-5

# PB7 · How Instagram growth works · fresh check

Checked 12 Nov 2026 by a fresh checker that did not see the unit written. Packet read: unit.md, unsure.md, brief.txt, sourcing.md (Parts 1 and 5), case-facts.md, notes.md, units/PB1–PB6, figure-kinds.txt. No audit report was read. Every source was opened by WebFetch on a URL returned by WebSearch in this run. One source was read at a variant URL: Search Engine Journal's collabs article at https://www.searchenginejournal.com/instagram-collabs/424231/; the unit links https://www.searchenginejournal.com/instagram-collabs.

## (1) Coverage

- How each surface ranks content (Feed, Stories, Explore, Reels, Search), from Instagram's pages, dated: covered (§1; Search from the 2021 post, the 2023 page names it only).
- The head's public statements, each cited to the statement itself and dated: thin. Every Mosseri statement is cited through a press report (Social Media Today, Metricool, TechJuice) and labelled that way; no original video or post is cited (finding 11).
- What reaches non-followers and what reaches followers: covered (§2).
- Formats in the largest vendor datasets, labelled, with the places they disagree: covered (§3; six rows, five datasets).
- The signals the platform names, as it names them: covered (§4).
- Stated rules on originality and reposted content: covered (§5).
- Features for reaching non-followers and for collaborating, named and dated: covered (§6). Collabs is thin: there is no current Instagram page, and the collaborator limit was not found. The unit says so.
- Hashtags and search as currently documented: covered (§7).
- Cadence: covered (§8).
- Instagram viewer to YouTube, mechanics and limits: covered (§9).
- Common claims with no source found: covered (§10).
- Deliverable (playbook with evidence, grade and label; metrics rows with metric, Insights location, frequency and PB1 row, worked for Mara's Q1; template): covered (D1, D2, T1, T2).

## (2)–(4) Findings

[error | accuracy] §6, table, Search engine indexing row; Current: "Public posts of professional accounts of users over 18 can appear in Google and Bing results from 10 July 2025"; Problem: PPC Land names "Google and other search engines". Bing does not appear in the article (it appears only in an unrelated "Read Next" headline). The claim adds a fact the source does not give; Fix: "Public posts of professional accounts of users over 18 can appear in the results of Google and other search engines from 10 July 2025"; Basis: PPC Land, 9 Jul 2025, "will automatically become searchable through Google and other search engines", https://ppc.land/instagram-content-becomes-searchable-on-google-starting-july-10/

[error | accuracy] §7, Search outside Instagram; Current: "can be indexed by Google and Bing unless the owner turns the setting off"; Problem: same as above. The source does not name Bing; Fix: "can be indexed by Google and other search engines unless the owner turns the setting off"; Basis: PPC Land, 9 Jul 2025, https://ppc.land/instagram-content-becomes-searchable-on-google-starting-july-10/

[error | accuracy] §8, Metricool 2026 bullet; Current: "and larger accounts did better per post when they posted less (Metricool, Instagram Trends 2026)"; Problem: this stretches the source. Metricool says that big accounts (100K–1M) do better per post when they post less and that huge accounts (1M+) posting less than weekly get about 6x the interactions per post, while medium accounts (10K–100K) peak at 14–30 posts a week, more than small accounts. "Larger accounts" as a class is not what it says; Fix: "and accounts of 100,000 to 1 million did better per post when they posted less, while accounts of 10,000 to 100,000 did best at 14 to 30 posts a week (Metricool, Instagram Trends 2026)"; Basis: Metricool, 10 Instagram Trends Backed By Real Data in 2026, 16 Jun 2026, https://metricool.com/instagram-trends/

[should-fix | attribution] §8, Metricool and HypeAuditor bullet; Current: "and 10 or more with about 79% "likely growth", the baseline and window undefined"; Problem: "likely growth" is not in the source. Its words are "Posting 2-3 times weekly will drive on average 19% growth, while 10+ posts per week will most likely boost it by 79%."; Fix: "and 10 or more with 79% ("10+ posts per week will most likely boost it by 79%"), the baseline and window undefined"; Basis: Metricool press release, 14 Oct 2025, https://metricool.com/press-release-instagram-content-playbook/

[should-fix | attribution] §3, Stories; Current: "left them out "because Stories are typically not shown to non-followers""; Problem: the quotation is not the source's wording, which is "Since stories are not typically shown to non-followers"; Fix: "left them out: "Since stories are not typically shown to non-followers""; Basis: Buffer, How often should you post on Instagram, 13 Aug 2025, https://buffer.com/library/how-often-to-post-on-instagram/

[should-fix | attribution] §4, Shares, saves… bullet; Current: "are "Not returned under 100 followers" in the API"; Problem: the string does not appear on the page. The rows for follows_and_unfollows and follower_demographics both read "Not returned if the IG User has less than 100 followers."; Fix: "are "Not returned if the IG User has less than 100 followers" in the API"; Basis: Meta for Developers, Instagram account insights, https://developers.facebook.com/docs/instagram-platform/api-reference/instagram-user/insights

[should-fix | accuracy] §1, paragraph after the table; Current: "and that Account Status, in the app's settings, shows whether"; Problem: the cited 2023 page places Account Status in the profile ("Check Account Status menu in your Instagram Profile"), not in settings. The source is cited as "same source"; Fix: "and that Account Status, a menu in the Instagram profile, shows whether"; Basis: Instagram, Instagram Ranking Explained, 31 May 2023, https://about.instagram.com/blog/announcements/instagram-ranking-explained

[should-fix | accuracy] §10, item 3; Current: "3. **A link in a Story or in the profile cuts reach.** No Instagram statement found either way; the only press reading is that Story links are "in theory, not reach restricted" (§9)."; Problem: an executive statement on the closely related claim exists and was not found. Mosseri said that writing "link in bio" does not reduce reach, which bears directly on IR7's "Full video: link in profile". The quoted press phrase is also clipped from "at least in theory, not reach restricted"; Fix: "3. **A link in a Story or in the profile cuts reach.** No Instagram statement on the links themselves was found; the only press reading is that Story links are "at least in theory, not reach restricted" (§9). On the related claim that writing "link in bio" in a post cuts reach, Mosseri said "You're more than welcome to say 'link in bio,' it will not affect your reach one way or another" ([Social Media Today, 23 Jul 2025](https://www.socialmediatoday.com/news/instagram-doesnt-penalize-posts-that-include-link-in-bio/753899/); executive statement via the press)."; Basis: Social Media Today, 23 Jul 2025, https://www.socialmediatoday.com/news/instagram-doesnt-penalize-posts-that-include-link-in-bio/753899/ ; Social Media Today, 25 Nov 2024, https://socialmediatoday.com/news/heres-each-big-social-platform-stand-external-links/733946/

[should-fix | attribution] Sources (goes with the previous finding); Current: "- Social Media Today, Instagram expands access to trial reels, 13 Jul 2025. https://socialmediatoday.com/news/instagram-expands-access-trial-reels/752895/"; Problem: the new citation must be listed; Fix: "- Social Media Today, Instagram expands access to trial reels, 13 Jul 2025. https://socialmediatoday.com/news/instagram-expands-access-trial-reels/752895/
- Social Media Today, Instagram says it doesn't restrict the reach of posts that include the term link in bio, 23 Jul 2025. https://www.socialmediatoday.com/news/instagram-doesnt-penalize-posts-that-include-link-in-bio/753899/"; Basis: as above.

[should-fix | label] D1, IR7, Evidence and Grade cells; Current: "Stories reach followers only (Instagram, 2023) | Strong for the mechanics; the effect is unmeasured |"; Problem: under the unit's own grades, Strong needs Instagram's or Meta's own pages. Two of the four mechanics come from the press: five profile links (TechCrunch) and no caption links (SMT). The rule's "link in profile" line also has a related executive statement it does not use; Fix: "Stories reach followers only (Instagram, 2023); saying "link in bio" does not affect reach (Mosseri via SMT, 23 Jul 2025) | Strong for the Story link sticker; weak for the profile-link and caption mechanics, reported by the press; the effect is unmeasured |"; Basis: the unit's grade definitions (D1 preamble); https://techcrunch.com/2023/04/18/instagram-takes-on-linktree-and-others-with-support-for-up-to-5-links-in-bio/ ; https://www.socialmediatoday.com/news/instagram-doesnt-penalize-posts-that-include-link-in-bio/753899/

[should-fix | style] §4 (item 10, reader persona); Current: "**The Instagram equivalents of YouTube's two numbers (flag F6).**"; Problem: "flag F6" is an internal syllabus flag. A reader of this public course cannot open it or know what it means; Fix: "**The Instagram equivalents of YouTube's two numbers.**"; Basis: brief preamble (reader; course shared with anyone).

[should-fix | coverage] Opening paragraph; Current: "where a Help Centre page would have settled a point, the unit says so and uses the next-best source, labelled."; Problem: the brief asks for the head's statements "each cited to the statement itself and dated". Every Mosseri statement is cited through a press or vendor report. Each is labelled "via the press" where it is used, but the unit never says once that the originals were not opened; Fix: "where a Help Centre page would have settled a point, the unit says so and uses the next-best source, labelled. Statements by Instagram's head, Adam Mosseri, are cited through the press reports that quote them, with the date of the report; the original videos and posts were not opened."; Basis: brief.txt (Cover); sourcing.md Part 1, "cited for what it says itself, not for what a later source reports about it (keep the reporter separate from the claim)".

[minor | accuracy] §10, item 7; Current: "paraphrases a November 2026 Mosseri interview"; Problem: Uppbeat's article is dated 3 Nov 2026 but gives no date for the interview. It calls it Mosseri's latest conversation with Colin and Samir; Fix: "paraphrases a recent Mosseri interview with Colin and Samir (the article does not date it)"; Basis: Uppbeat, 3 Nov 2026, https://uppbeat.io/blog/creator-news/whats-working-on-instagram-right-now-carousels-and-sends-says-adam-mosseri

[minor | accuracy] §3, Where they agree; Current: "Carousels lead or tie on engagement in every dataset but Fanpage Karma's small band, where images lead."; Problem: Fanpage Karma gives no carousel interaction rate for the under-10,000 band (images 0.51%, Reels 0.34% only), and Metricool 2026 does not compare formats on engagement (the unit's own figure marks it "not compared"); Fix: "Carousels lead or tie on engagement in every dataset that compares them; in Fanpage Karma's small band, which gives no carousel figure, images lead Reels, and Metricool 2026 does not compare formats on engagement."; Basis: Fanpage Karma, 7 Aug 2026, https://www.fanpagekarma.com/insights/instagram-format-reach/ ; Metricool, Instagram Trends 2026, https://metricool.com/instagram-trends/

[minor | label] §3 table, Fanpage Karma row, Label cell; Current: "| Vendor; medians |"; Problem: the page says its analysis "focuses on median reach per follower and post". It does not say the interaction rates in the same row are medians; Fix: "| Vendor; reach figures are medians; interaction rates not stated as medians |"; Basis: Fanpage Karma, 7 Aug 2026, https://www.fanpagekarma.com/insights/instagram-format-reach/

[minor | label] D1, IR1, Grade cell; Current: "| Moderate for the surface roles;"; Problem: what each surface shows is Instagram's own description on its own page. By the unit's grades that is Strong ("a rule or definition on Instagram's or Meta's own pages, about what the platform does"); Fix: "| Strong for the surface roles (Instagram's own description);"; Basis: D1 grade definitions; Instagram Ranking Explained, 31 May 2023, https://about.instagram.com/blog/announcements/instagram-ranking-explained

[minor | figure] §1 figure, Reels row; Current: "{"label": "Reels", "tone": 5, "cells": ["not followed","; Problem: the text and the source say Reels shows "mostly" accounts the viewer does not follow, and the cell drops "mostly"; Fix: "{"label": "Reels", "tone": 5, "cells": ["mostly not followed","; Basis: unit §1 table ("mostly accounts you do not follow"); Instagram Ranking Explained, 31 May 2023.

[minor | accuracy] D2, IG13, PB1 row cell; Current: "| I5 (the 1,000 line) |"; Problem: PB1's I5 is Live eligibility ("1,000 followers and a public account"), not trial reels. Calling it "the 1,000 line" hides what the row is; Fix: "| I5 (PB1's 1,000-follower milestone, set for Live) |"; Basis: units/PB1, metrics row I5.

[minor | accuracy] D2, IG3, Mara column; Current: "recorded against 261 as context only, since the benchmark pools every size"; Problem: 261 is the page's "All" figure, and the page recommends filtering by follower tier, so a per-tier figure may exist. It was not readable in this check (unverifiable). The sentence should not imply that no size split exists; Fix: "recorded against 261 as context only, since that figure pools every size (the page recommends filtering by follower tier; no tier figure was read)"; Basis: Buffer, Instagram benchmarks, updated 8 Nov 2026, https://buffer.com/social-media-benchmarks/instagram

## (2) Unsure list, item by item

1. Trial reels eligibility. SMT (13 Jul 2025) paraphrases Mosseri: "all creators with at least 1,000 followers and an account set to 'Public'". PASS as reported. SMT's link goes to a Threads post by another account (@oncescuradu), not Mosseri's own, so "a Mosseri Threads post" in the unsure note is not confirmed. The unit's text says "Mosseri, as reported", which is correct. The Help Centre was not read (unverifiable).
2. Insights menu names: unverifiable; the Help Centre was not read. The unit flags them.
3. In-app threshold below 100 followers and per-post insight retention: unverifiable. The API threshold is confirmed (wording finding above).
4. Under-1,000 medians 134/56/23: PASS against Net Influencer, 14 Oct 2025. The likes figures (7 and 6) are averages, as the unit says. The gated study was not read.
5. Collabs: SEJ, 20 Oct 2021: both names, both grids, both sets of followers, shared insights; the invitee must accept. PASS. The collaborator limit was not found on Instagram's 30 Apr 2026 page either.
6. Indexing: PASS on date, eligibility (public professional accounts, 18+), setting name and default. FAIL on "Bing" (finding above).
7. Five-hashtag limit: PASS. SMT, 18 Dec 2025, quotes Instagram's @creators Threads post verbatim; Mosseri's "don't improve visibility" is dated May 2025 by SMT.
8. Creator tools opened to all public accounts: PASS. SMT, 1 Mar 2026, paraphrases Instagram and does not quote it; no scheduling horizon is given.
9. Edits Reel links: PASS. Blog du Modérateur, 20 Jan 2026, names only an Instagram account or another public Reel as destinations and cites the @Creators post.
10. Carousel second chance: PASS on Haberman's wording ("the algorithm gives your Carousel a second chance after it's posted, resurfacing it to followers who previously swiped by"). The attribution is "Last year", which the unit dates to 2024 from the article's 2025 date, a fair reading. Uppbeat paraphrases and does not quote, PASS, but the interview date is not given (finding above).

## Confirmed

- Instagram Ranking Explained, 31 May 2023: the Feed, Stories and Explore quotations are verbatim; Reels "mostly" from accounts not followed, with an emphasis on entertainment; the signal groups in the listed order; Search "uses its own algorithm"; low-resolution or watermarked, muted, bordered, majority-text and already-posted reels made less visible; Recommendation Guidelines covering Explore, Reels, Search, suggested posts and suggested accounts; "none of their posts will be eligible for recommendation for a period of time"; appeal via Account Status; the shadowban sentences, "that's not our intention" and "we don't suppress content to encourage people to buy ads". https://about.instagram.com/blog/announcements/instagram-ranking-explained
- Instagram, 25 Aug 2021: "by far the most important signal for Search"; activity, then popularity signals (clicks, likes, shares, follows); the three tips; keywords "in the caption, not the comments"; "may appear lower in search results". https://about.instagram.com/blog/announcements/break-down-how-instagram-search-works/
- Instagram Creators, 30 Apr 2024: all four quotations; originals replace copies when "relatively new"; label linking to the original; aggregators excluded from recommendations; reach regardless of follow; no audience size, window or effect size. https://creators.instagram.com/recommendations-and-originality
- SMT, 22 Jan 2025: "top three signals…", "Likes are slightly more important for connected content…", "average watch time, likes per reach, and sends per reach"; connected is not defined. https://www.socialmediatoday.com/news/instagram-shares-algorithm-insights-2025/738034/
- SMT, 10 Jun 2024: "I would look at sends per reach" and "There's way more unconnected content…", from an interview (Colin and Samir). https://www.socialmediatoday.com/news/instagram-chief-shares-insights-into-its-algorithms-creator-monetization/718540/
- TechCrunch, 10 Dec 2025: Your Algorithm in the US, AI-summarised topics, more or less of a topic or add one, "globally in English soon", Explore later. https://techcrunch.com/2025/12/10/instagrams-new-your-algorithm-tool-gives-you-more-control-over-the-reels-you-see
- Fanpage Karma, 7 Aug 2026 (modified 28 Aug 2026): more than 3 million posts, Jan–Apr 2026, accounts not counted; under 10,000: 4.9% / 3.5% / 2.6% medians; "Reels reach nearly three times as many non-followers as carousels"; community reach 2.1% images and 2.0% Reels; interaction rates 0.51% and 0.34%. https://www.fanpagekarma.com/insights/instagram-format-reach/
- Metricool press release, 14 Oct 2025: 700 million posts, 28 million influencer accounts, Jan–Jun 2025, medians; "Reels lead in reach across follower tiers"; carousels "increasingly win on likes and comments" at 500K+; 8 p.m. local time, Wednesday and Friday. https://metricool.com/press-release-instagram-content-playbook/
- Net Influencer, 14 Oct 2025: under 1,000, Reels 134, carousels 56, images 23; likes 7 for carousels and 6 for Reels. https://www.netinfluencer.com/instagram-carousels-outperform-reels-for-larger-accounts-content-performance-benchmarks-show/
- Buffer, 23 Oct 2024: more than 4 million posts, Jan 2022–Oct 2024; ratios 1.36, 2.25, 1.12 and 2.14; charts give medians while the text says "on average"; no size split. https://buffer.com/resources/instagram-reach-engagement-analysis/
- Buffer, 19 Mar 2026: carousels 6.9%, images 4.4%, Reels 3.3%, median engagement as a share of reach; repeats the 2024 reach ratios; no Instagram post count. https://buffer.com/resources/data-best-content-format-social-media/
- Socialinsider benchmarks, 20 Feb 2026, modified 4 Nov 2026: 67,541,436 posts from brands of 1K–1M followers; "Carousels got the most views on Instagram at every account size in 2025"; 1K–5K views 993 / 580 / 417; engagement 0.55% / 0.52% / 0.37%; follower growth 22% a year in 2025 (38% in 2024); averages. https://www.socialinsider.io/instagram-benchmarks
- Metricool, Instagram Trends 2026: 24,364,803 posts and 375,118 accounts; carousels about 1.69% ahead on views; "carousels beat them on every measure", where "them" is single images; Reels engagement rate up 24.76% and shares up 67.19%; Stories reach down 1.77% and replies up 88%; 65% and 76% of views in days 1–3 and 44% on day 1 for static posts; 2K–10K accounts best at 7–14 posts a week. https://metricool.com/instagram-trends/
- Buffer, 13 Aug 2025: 2.1M feed posts from 102K accounts, fixed effects; +0.12/+0.26/+0.44/+0.66%; reach per post about +12/18/24%; "likely the sweet spot" (3–5 a week); "treat with caution" (6–9+); no size or format split. 0.26% of 140 is about 0.36, correct. https://buffer.com/library/how-often-to-post-on-instagram/
- SMT, 7 Aug 2024: both quotations verbatim; no follower/non-follower split and no mention of impressions. https://socialmediatoday.com/news/instagram-updates-metrics-to-focus-creators-on-views/723645/
- Metricool, 14 Aug 2024: the Mosseri quotation; the Followers/Non-followers split and the removal of impressions both reported in the future tense. https://metricool.com/instagram-insights/
- Meta account insights: the views and reach definitions (reach estimated; the full definition adds ", including in ads"); FOLLOWER and NON_FOLLOWER breakdowns; profile_links_taps counts contact buttons. https://developers.facebook.com/docs/instagram-platform/api-reference/instagram-user/insights
- Meta media insights: reels_skip_rate; ig_reels_avg_watch_time "The average amount of time spent playing the reel"; "Insights data is not available for any media within an Instagram Media album". https://developers.facebook.com/docs/instagram-platform/reference/instagram-media/insights/
- SMT, 24 Aug 2025: the skip-rate definition, the replacement of view rate, "the flatter the line…". https://www.socialmediatoday.com/news/instagram-adds-retention-insights-reels/758464/
- SMT, 1 Mar 2026: insights dashboard, scheduling and trending audio "available to all public accounts", previously Professional Mode only; thresholds not listed. https://www.socialmediatoday.com/news/instagram-opens-up-content-scheduling-to-all-users/813448/
- Socialinsider Reels statistics, 24 Jun 2026, updated 6 Nov 2026: 9,771,822 Reels, Jan–Jun 2026; skip rate 65.50% (1–5K) and 60.50% (100K–1M); brands; no watch-time figure. https://socialinsider.io/blog/instagram-reels-statistics/
- Original content guidelines: every quotation verbatim; 30-day period; Account Status; undated (© 2026 Meta). https://creators.instagram.com/original-content-guidelines/
- Instagram Creators, 30 Apr 2026: protections extended to photos and carousels; "will no longer be shown in places where we recommend content"; "does not impact how we show people content from accounts they follow"; "new information, context, or a point of view"; 75% of US recommendations from original posts; collabs, remix, the paid partnership label, Stories sharing and reposts. https://creators.instagram.com/blog/rewarding-original-creators-on-instagram
- Instagram Creators, 10 Dec 2024: "all eligible creators"; non-followers first; hidden from followers' Feed, the Reels tab and the grid; metrics after about a day; automatic sharing on 72-hour views. https://creators.instagram.com/blog/instagram-trial-reels
- Meta, 6 Aug 2025: reposts recommended to friends' and followers' feeds, in a profile tab, "credited to the original poster", and may reach the reposter's followers. https://about.fb.com/news/2025/08/new-instagram-features-help-you-connect/
- TechCrunch, 31 Mar 2021: Remix side by side; remixes on the remixer's Reels tab; the original creator sees them in Activity; on by default for new Reels from public accounts. https://techcrunch.com/2021/03/31/instagram-officially-launches-remix-on-reels-a-tiktok-duets-like-feature
- SMT, 23 Aug 2026: the captions quotation from an Instagram post. https://socialmediatoday.com/news/instagram-stresses-the-importance-of-captions/828554/
- TechJuice, 25 Aug 2025: "It is not going to affect your reach much one way or the other", Stories Q&A, undated. https://www.techjuice.pk/instagram-chief-finally-puts-rest-to-a-big-caption-myth/
- TechCrunch, 18 Apr 2023: up to five links, announced on Zuckerberg's broadcast channel, opened in the app with "open in system browser". https://techcrunch.com/2023/04/18/instagram-takes-on-linktree-and-others-with-support-for-up-to-5-links-in-bio/
- Instagram, 27 Oct 2021: "we're expanding the ability to add links in Stories to all accounts"; new accounts and repeat violators "will not have access to the Link sticker". https://about.instagram.com/blog/announcements/expanding-sharing-links-in-stories-to-everyone
- SMT, 25 Nov 2024: "Instagram doesn't let you post links in captions"; Story links "at least in theory, not reach restricted", shown to followers. https://socialmediatoday.com/news/heres-each-big-social-platform-stand-external-links/733946/
- Engadget, 12 Mar 2026: Meta confirmed the caption-link test for Meta Verified subscribers; no word on wider availability. https://www.engadget.com/social-media/meta-is-testing-clickable-links-in-instagram-captions-for-verified-subscribers-184555406.html
- YouTube Help 1714921: the External and Direct or unknown definitions verbatim, and the External sites or apps card. https://support.google.com/youtube/answer/1714921?hl=en-GB
- Buffer benchmarks, updated 8 Nov 2026: 261 median reach (All); 27M posts from 273,000 accounts and 30M from 250,000 both on the page. https://buffer.com/social-media-benchmarks/instagram
- Arithmetic and calendar (Mara): 39 Q1 posts = 27 Reels + 12 carousels from PB4's posts 1–4 Reels and 5–6 carousels, with week 13 a week A; 36 posts at least 7 days old on 5 Apr 2027 (24 + 12); Reels of 30 Mar, 1 Apr and 3 Apr; Q2 25 + 14 (week 14 a week B). 4.9% × 140 ≈ 7 and 2.6% × 140 ≈ 4. All checked.

## (5) Deliverable

Present in full. D1 has twelve rules, each with evidence, grade and label. D2 has thirteen rows with metric, Insights location, frequency, PB1 row, reference and label, and Mara's Q1 entry. T1 and T2 are templates whose blanks say what goes in them. The deliverable follows from the body, and the rules with no source are marked convention. It is usable alone. Corrections it needs: IR7's grade and evidence (finding above); IG3, IG13 and IR1 (minor findings). The Q1 values are left to PB10, which agrees with the unit's statement and with case-facts.

## (6) Errata and pointers

No audit report was in the packet and none was read, so no erratum applies. Pointers to filed units, checked against units/:
- PB1 I1, I3, I4, I5, I7: rows exist as described (I5 is Live; see the minor finding). D3 read 1 (output against plan, 39 posts) and verdict 3 (YouTube CTR and percentage viewed) match.
- PB2 D3 name field: matches.
- PB3 §3 (the 7-accounts calculation), §4 (no conversion source), D1 trait 8: all match.
- PB4: posting days, mix, 30 minutes, cut-window hours (3.0 + 0.5), 1.25 publishing and replies, lost-week rules, Season 3 second video: all match case-facts.
- PB5 §3 rule 4, §5 export from her own edit, Reels 30–60 s: match.
- PB6 YT6 and the grade definitions: match.

## (7) Figures

1. §1, matrix: "Instagram's surfaces: whom each serves". Every label traces to §1's table and text ("a mix of content from the accounts you've chosen to follow" → "followed, plus recommended"; "The stories you see are from people you've chosen to follow" → "followed only"; the first signal groups; "The text you enter in the search bar is by far the most important signal for Search"). The caption names the section and both sources and says the last column is the unit's reading. The kind fits (items by sections). FIX (minor): the Reels cell "not followed" becomes "mostly not followed", to match "mostly accounts you do not follow". Replacement row: {"label": "Reels", "tone": 5, "cells": ["mostly not followed", "your activity", {"mark": "yes", "tone": 3}]}
2. §3, matrix: "Which Instagram format each dataset puts first". Every mark traces to §3's table and "Where they disagree" (Reels in three datasets; carousels in Socialinsider; "carousels, by 1.69%"; HypeAuditor likes under 1,000; Fanpage Karma images 0.51% against Reels 0.34%; "not compared" for Metricool 2026; populations as labelled). The caption names the section, the sources and the labels. The kind fits: the cells are rankings, not comparable numbers, so compare or bars would not fit. PASS.
3. §9, flow: "From a Reel to the YouTube video". Every step traces to §9 ("tap the name, tap a link, and the video opens in the in-app browser or the phone's browser"; "up to five links"; "no clickable link" in captions; External and Direct or unknown). The caption names the section and sources and says the path is the unit's reading. The kind fits (a sequence). PASS.

## (8) Writer's Source errors (notes.md)

1. A6, the followers/non-followers split reported as done in Aug 2024: confirmed. Metricool, 14 Aug 2024: Instagram "will use the same calculations to display 'Followers' and 'Non-followers' views by format"; impressions "will no longer be available in Insights" (both future). SMT, 7 Aug 2024 does not mention the split or impressions.
2. Socialinsider's modified date: confirmed. The page shows modified 4 Nov 2026, with 580 / 993 / 417 views (1K–5K) and follower growth of 22.00% (2025) and 38.00% (2024).

## (9) Sourcing standard Part 5, line by line

- Every claim with a number, mechanism or recommendation sourced where made: PASS, except the Bing and Metricool-frequency stretches (findings).
- Source types (peer-reviewed, platform-official, named large-sample vendor with size and date, documented creator case): PASS. Every vendor row gives its sample and date; Fanpage Karma's account count is absent and the unit says so. TechJuice, PPC Land, Blog du Modérateur and Uppbeat are press reports of platform or executive statements and are labelled as such.
- Anecdote, vendor and correlational data labelled: PASS (one minor label finding: Fanpage Karma "medians").
- Each growth, format or metric claim says which platform: PASS. The unit is Instagram throughout, and the YouTube side in §9 and IG10 is named.
- Carried-over claims re-verified at source: PASS on the claims sampled (PB3's Fanpage Karma figures, PB1's Buffer and Socialinsider rows, PB5's skip rate).
- No private-course reader or units referred to: PASS. No A-unit code or private detail appears. "flag F6" is an internal syllabus reference (finding).
- Mara labelled on first use, consistent with case-facts, never used as evidence: PASS. "(Mara, fictional)" appears at the first mention in §2; her new facts agree with the register; her numbers are illustrations.
- No tax rate as the reader's; amounts in source currency with date; legal points with EU, UK and US sources and a not-advice line: PASS, not applicable. The unit states no amount and makes no legal point; originality is treated as platform policy, and the paid-partnership label is left to PB8.
- No uncited figures and no invented handles, names, studies or numbers: PASS. The hashtags in D1 are labelled her choice. The misquotations are listed as findings.
- Facts that can change carry a check date: PASS. There is a global "checked on 12 November 2026" line, and the sources are dated.
- Deliverable in full for Mara, then a template: PASS.
- Does not read as advice without evidence: PASS.
- Links given as links: PASS. Every body URL is in Sources and every Sources entry is cited in the body (checked by script).

## (10) Reader persona

The reader is an adult under 1,000 followers who reads in order and cannot open the private course. The only term only an insider would know is "flag F6" in §4 (finding). Cross-references to PB1–PB6 and to PB10, a later unit of this course, are by code, as the brief requires. "PB4's cut window" and "the Wednesday reply slot" assume PB4, which the reader has read in order. No other private assumption was found.

PB7 · verdict: fix · error 3, should-fix 9, minor 7
