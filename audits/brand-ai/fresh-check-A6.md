---
audit: fresh check
unit: A6 · How growth works, per platform
course: brand-ai · A · Building a Marketable Personal Brand
model: Fable 5.1 (search on)
date: 2026-10-28
chat: https://claude.ai/chat/5352e040-7ef4-4c6f-a318-9b033851d376
verdict: fix · 1 error, 9 should-fix, 7 minor (all applied the same day)
---

# Fresh check · A6 · How growth works, per platform

Filed 28 October 2026 under backlog row P3 from the chat above, verbatim. The prompt was the `method.md` §5 fresh check ("Fresh check of one Brand + AI unit"); the checker had not seen the unit written and did not edit it. The unit as rewritten by Opus 5.5 on 28 October 2026 was the input; every finding was applied before the unit was filed (`courses/brand-ai/A6-how-growth-works-per-platform.md`).

## Findings

1. [error] [attribution] §2.1
   - Current: "Mosseri said in 2024 that the system gives a carousel "a second chance after it's posted, resurfacing it to followers who previously swiped by" (quoted in"
   - Problem: the quoted words are Haberman's bullet summary of a linked Instagram post. She does not quote Mosseri.
   - Fix: "In Lia Haberman's summary of what Mosseri said in 2024, the algorithm gives a carousel "a second chance after it's posted, resurfacing it to followers who previously swiped by"; the words are Haberman's, not a transcript of Mosseri ("
   - Also replace "Two follower-side and stranger-side mechanics have official or executive sources:" with "Two follower-side and stranger-side mechanics are sourced to Instagram or to reports of what its head said:"
   - Basis: https://liahaberman.substack.com/p/the-best-instagram-content-formats

2. [should-fix] [accuracy] §1.3 Breaks
   - Current: "AIR Media-Tech's study of 18,000 English-language channels in the 100,000–1,000,000 monthly-views segment (published 8 June 2026)"
   - Problem: the 18,000 channels span 11 niches and four size segments. Only the primary analysis is on 100K–1M.
   - Fix: "AIR Media-Tech's study of 18,000 English-language channels across 11 niches and four size segments, with its primary analysis on the 100,000–1,000,000 monthly-views segment (published 8 June 2026)"
   - Basis: https://air.io/en/audience-growth/does-posting-more-on-youtube-help-we-studied-18000-channels-to-find-out

3. [should-fix] [accuracy] §3.2
   - Current: "Amy Suto spent six months posting daily on Substack Notes"
   - Problem: the page says "posting constantly" for the experiment. "I post daily" describes her current routine. The 42,000+ figure is her three-year total, not a count dated to the experiment.
   - Fix: "Amy Suto spent six months going all-in on Substack Notes"
   - Also replace "Anecdote, one writer with 42,000-plus subscribers at the time." with "Anecdote, one writer, who reports 42,000-plus subscribers over three years."
   - Basis: https://www.amysuto.com/desk-of-amy-suto/substack-notes

4. [should-fix] [accuracy] §2.2
   - Current: "For him: a clip carrying another app's watermark, or a repost of a training partner's video, sits outside the recommendation surfaces that bring strangers."
   - Problem: the originality rule covers other people's work, including watermarks added to it. His own watermarked clip is original; the 2023 page says watermarked Reels get less distribution, not exclusion.
   - Fix: "For him: posting mostly reposts of training partners' videos can take the account out of recommendations to new audiences; a clip of his own that carries another app's watermark stays eligible but, on Instagram's 2023 account, gets less distribution."
   - Basis: https://creators.instagram.com/original-content-guidelines/ ; https://about.instagram.com/blog/announcements/instagram-ranking-explained

5. [should-fix] [accuracy] §2.2 "The exits are narrow"
   - Current: "Instagram does not allow links in captions;" and "A stranger who finds a Reel can leave Instagram only through the bio link."
   - Problem: Meta has been testing clickable caption links for Meta Verified subscribers since 12 Mar 2026. The bio-link "only" appears in neither cited source.
   - Fix (first sentence): "Instagram does not allow links in ordinary captions (Social Media Today, Nov 2024), though since March 2026 Meta has been testing clickable caption links for Meta Verified subscribers ([Engadget, 12 Mar 2026](https://engadget.com/social-media/meta-is-testing-clickable-links-in-instagram-captions-for-verified-subscribers-184555406.html));"
   - Fix (second sentence): "For a stranger who finds a Reel on an account without Meta Verified, the bio link is the remaining exit (his reading of the two sources; no source states it)."
   - Add Engadget to Sources.
   - Basis: Engadget, above; https://socialmediatoday.com/news/heres-each-big-social-platform-stand-external-links/733946/

6. [should-fix] [deliverable] Metrics sheet Y2
   - Current: "| Each completed test | Packaging record for the next episode |"
   - Problem: this contradicts "Between checkpoints nothing is opened". YouTube applies the winner itself, so nothing needs reading between checkpoints.
   - Fix: "| Every checkpoint (tests completed that quarter; YouTube applies the winner automatically) | Packaging record for the next episode |"
   - Basis: https://support.google.com/youtube/answer/16391400?hl=en ("the option with the highest watch time will be shown to all viewers")

7. [should-fix] [deliverable] Playbook, Substack 3 (unsure item 7)
   - Current: "3. **Point paying readers to web checkout where he can.** Basis: app-store purchases keep the billing relationship with Apple and cost 30% in the first year (Substack IAP FAQ, Aug 2025)."
   - Problem: the FAQ settles "where he can". In-app web checkout is shown to US readers only. Desktop, mobile-web and email-link subscriptions are unaffected.
   - Fix: "3. **Send paid-tier offers as web and email links.** Basis: app-store purchases keep the billing relationship with Apple and cost 30% in the first year; web checkout inside the iOS app is shown only to US readers, so a reader in Portugal subscribing in the iOS app sees only in-app purchase, while desktop, mobile-web and email-link subscriptions are unaffected (Substack IAP FAQ, Aug 2025)."
   - Basis: https://on.substack.com/p/in-app-payments-iap-faq

8. [should-fix] [accuracy] §2.1 Trial Reels and Playbook, Instagram 4 (unsure item 2)
   - Current: "The 1,000-follower requirement in the earlier research has no source on either page and is dropped (Audit 1 erratum); eligibility was not checked."
   - Problem: the figure has a source elsewhere. Mosseri, reported by SMT on 13 Jul 2025, said trial reels are available "to all creators with at least 1,000 followers and an account set to 'Public.'" The playbook rule may be unusable at his current following.
   - Fix: "The 1,000-follower requirement in the earlier research has no source on either page (Audit 1 erratum); it does have one elsewhere: Mosseri said in July 2025 that trial reels are available to creators with at least 1,000 followers and a public account ([Social Media Today, 13 Jul 2025](https://www.socialmediatoday.com/news/instagram-expands-access-trial-reels/752895/), executive statement reported second-hand; no later change found)."
   - In Instagram 4, replace "Eligibility is set in the Help Center and was not checked." with "Available from 1,000 followers on a public account (Mosseri via SMT, Jul 2025); below that, post the opener as an ordinary Reel."
   - Add SMT 13 Jul 2025 to Sources.
   - Basis: SMT, above

9. [should-fix] [attribution] §1.3
   - Current: "A practitioner model that puts the crossover at month six circulates; it rests on assumed per-video views with no data behind them and is left out."
   - Problem: a numbered claim with no citation. Naming an uncited model in order to discard it still puts its figure in the text.
   - Fix: delete.
   - Basis: sourcing-standard.md Part 1; Audit 1 §4, §2 row (Humble&Brag)

10. [should-fix] [figure] Metrics sheet E4
    - Current: "| E4 | Unsubscribes per send | Readers leaving | Vendor average 0.15% (GetResponse, 2023 data) |"
    - Problem: GetResponse does not say how the rate is calculated. Audit 1 flagged "per send" as an inference, and the inference is still here.
    - Fix: "| E4 | Unsubscribe rate per issue | Readers leaving | Vendor average unsubscribe rate 0.15% (GetResponse, 2023 data; the page does not say how the rate is calculated) |"
    - Basis: https://www.getresponse.com/resources/reports/email-marketing-benchmarks?web=1

11. [minor] [attribution] Playbook, YouTube 7
    - Current: "YouTube says there is no penalty box for breaks (SEJ 2024)"
    - Problem: "penalty box" is SEJ's term, and the breaks point is SEJ's paraphrase of Beaupré.
    - Fix: "Beaupré disputed that channels are penalised for breaks (SEJ 2024, the article's paraphrase; "penalty box" is SEJ's term)"
    - Basis: https://www.searchenginejournal.com/youtube-algorithm-myths-debunked-insights-from-the-growth-team/510091/

12. [minor] [attribution] §2.1
    - Current: ""Unconnected" is Instagram's term for content shown to people who do not follow the account."
    - Problem: neither the article nor Mosseri defines the word.
    - Fix: ""Unconnected" is not defined in the article; it is read here as content shown to people who do not follow the account."
    - Basis: https://www.socialmediatoday.com/news/instagram-shares-algorithm-insights-2025/738034/

13. [minor] [accuracy] Playbook, YouTube 8
    - Current: "Basis: subscribers mostly watch through the suggested list, and Beaupré put the subscribers-row CTR at around a tenth or less (PPC Land 2026, hedged, no sample)."
    - Problem: Beaupré said the suggested list is the top place, not most viewing. "No subscribe appeals" is an unmarked convention.
    - Fix: "Basis: the suggested list is the top place subscribers watch, and Beaupré put the subscribers-row CTR at around a tenth or less (PPC Land 2026, hedged, no sample). **(his rule** for subscribe appeals**)**"
    - Basis: https://ppc.land/subscribers-skip-90-of-uploads-in-their-feed-youtube-director-says/

14. [minor] [accuracy] §1.2
    - Current: "The only external bands for average percentage viewed are vidIQ's"
    - Problem: this is a search-negative stated as a fact.
    - Fix: "The only external bands for average percentage viewed found for this unit are vidIQ's"
    - Basis: n/a

15. [minor] [deliverable] Metrics sheet E6 (unsure item 1)
    - Current: "Substack dashboard, subscriber sources"
    - Problem: Substack's name for the view is the Growth Sources tab.
    - Fix: "Substack dashboard, Growth Sources tab (Substack sources incl. Notes and Recommendations; trackbacks; external)"
    - Basis: https://on.substack.com/p/a-new-growth-chart-and-tools-to-help (12 Sep 2025)

16. [minor] [style] §1.3
    - Current: "(bi-weekly against weekly: about 1.5 times the view growth and 3.9 times the subscriber growth, on channels already past 1,000)"
    - Problem: as written, the multiple reads as bi-weekly's advantage.
    - Fix: "(weekly against bi-weekly: about 1.5 times the view growth and 3.9 times the subscriber growth, on channels already past 1,000)"
    - Basis: A9 row 9 (+0.89% → +1.32% views, +0.10% → +0.39% subscribers)

17. [minor] [accuracy] §3.1
    - Current: "Since 18 August 2025 readers can pay through Apple's in-app purchase;"
    - Problem: the FAQ is dated 18 Aug 2025 but gives no launch date.
    - Fix: "As of Substack's FAQ of 18 August 2025, readers in the iOS app can pay through Apple's in-app purchase;"
    - Basis: https://on.substack.com/p/in-app-payments-iap-faq

## Errata applied (Audit 1, those touching A6)
- 2–10% re-cited to YouTube Help 7628154, and the 4–6% target dropped: applied
- Trial Reels 1,000-follower figure and the Stories claim: applied. The 1,000 figure was dropped and Stories was re-sourced to Ranking Explained; see finding 8.
- 3× re-cited to the Metricool and HypeAuditor press release, as likes and comments: applied
- YouTube's statement on history re-sourced from Cornell to SEJ: applied
- Regular viewers defined in months: applied
- Vidpros Regular-tier benchmarks dropped: applied
- "Doubles" replaced by 1.5× and 3.9×, on channels past 1K: applied, by pointer to A9 row 9
- "A month or more" pointed to PPC Land: applied
- Socialinsider labelled as brand accounts: applied
- GetResponse cited directly: applied. The "per send" inference remains; see finding 10.
- Humble&Brag: dropped rather than reworded, but an uncited residue remains; see finding 9.
- OpenSponsorship minor: absent

## Confirmed
- Traffic source definitions; embeds count as External (YouTube Help 1714921)
- Search: relevance, engagement, quality, "may vary by search type", history, no paid placement, nothing on size or recency (16090438)
- Impressions page (7628154):
  - CTR definition; external sites and end screens excluded
  - Half of channels at 2–10%; wider in week one and under 100 views
  - "Narrower, more loyal audience"; homepage CTR lower
  - Compare over the long term; small variations are not cause for action
  - "high CTR but low average view duration and lower than expected Impressions" (verbatim)
- Test & Compare (16391400): up to 3 variants; "optimize tests for overall watch time over other metrics, like click-through-rate"; a few days to 2 weeks; computer only; advanced features required; inconclusive tests keep the first variant
- Key moments (9314415): 10 latest videos of similar length, or all YouTube videos; Intro at 30 s; minimum 60 s and 100 views
- Viewer segments (10246996): definitions; no effect on reach or monetisation. Tips page (13615784): consistency, series, regular publishing, comments; no effect sizes
- YPP: long-form public watch hours only (72851); 8,000 hours in 365 days from 1 Feb 2027 (12843009)
- YouTube blog, 20 Feb 2024: more than 1 billion hours a day on TVs
- SEJ, 4 Mar 2024: Beaupré on pull vs push; "focused more on individual videos"; not over-weighting history; a weak video followed by a strong one; older videos regaining traction
- PPC Land, 2 Sep 2026, on the Creator Insider interview of 1 Sep:
  - Title; per-viewer ranking; suggested list vs subscriptions feed
  - "maybe a 10% or less"
  - "Month or more later" is a paraphrase
  - TV quotes are Beaupré's
- Metricool YouTube, 29 Jul 2026: 799,718 videos and 71,177 accounts; Shorts 61%+, subscribers 11%, search 9%, related 5.77%, playlists 5.05%, channel ~3%; AVD 2.51 min vs ~16 s; peak in 3 days; 83% of interactions within 10 days
- AIR, 8 Jun 2026: 14+-day gaps; predictable schedules; no effect sizes for these; "correlational data, not causal"
- vidIQ AVD, 21 Jul 2026: "vidIQ guidance", no sample
- Instagram Ranking Explained, 31 May 2023:
  - All four surfaces and their predictions
  - Reels quote verbatim
  - Watermarked, low-resolution and already-posted Reels get less distribution
  - Account Status shows recommendation eligibility
- Mosseri via SMT, 22 Jan 2025: top three signals; connected/unconnected sentence verbatim; the three Insights metrics
- Trial reels (Meta, 10 Dec 2024, updated 26 Jun 2025; Instagram Creators): non-followers first; Feed and Reels tab hidden from followers; DM share; metrics at ~24 h; auto-share on views within 72 h; eligibility referred to the Help Center
- Metricool and HypeAuditor, 14 Oct 2025: 700M posts, 28M influencer accounts, Jan–Jun 2025, medians; Reels lead reach across tiers; ~3× likes and comments
- Socialinsider (pub. 20 Feb 2026, upd. 22 Oct 2026):
  - 131,955 business accounts, 7,032,675 posts
  - Reels 580, carousels 993, images 417 (averages)
  - Growth 38.00→22.00% and 35.00→20.29%
  - "2025 values, presented as 2026"
- Original content guidelines: recommendations to new audiences; 30-day rolling window; followers unaffected; the list of edits that are not enough
- Instagram, 30 Apr 2026: photos and carousels added; Reels since 2024; aggregators; Account Status check and appeal; 75% of US recommendations from original posts
- Instagram metrics changes:
  - SMT, 7 Aug 2024 and Metricool, 14 Aug 2024: Views primary, repeats counted, impressions out, Followers/Non-followers split
  - TechCrunch, 29 Jan 2025: view rate and views over time
  - SMT, 24 Aug 2025: skip-rate quote verbatim; retention chart
- Patreon via Net Influencer, 21 Feb 2025: 1,000 creators and 2,000 fans, NewtonX, Aug 2024; 24/32/38%; 53%; company-sponsored
- Buffer, 13 Aug 2025: 2.1M posts, 102K accounts; fixed effects; +0.12/0.26/0.44/0.66%; ~12% more reach per post; Stories excluded; no size split
- Substack Support: "always own your readers' email addresses", export at any time
- Substack IAP FAQ: billing relationship quote verbatim; 30% then 15%; 10% on the web price
- On Substack, 22 Feb 2024: 50% of new subscriptions and 25% of paid. The 2022 posts are older (30%+, 40%+), and no newer split was found.
- beehiiv, State of Newsletters 2026 (verified on the .md copy; the canonical page truncates in fetch): 41.24%; 3.23% (image text); 65,000+; 28B emails; the MPP sentence verbatim; 2.75×; 32×; 482 / 8,314
- Amy Suto, 14 Jul 2026: 1,459 vs 8,366; 15,800 likes, 28,055 clicks, 378 free, zero paid
- Apple MPP: "downloads remote content in the background by default"; senders could otherwise learn "when and how many times you opened"
- GetResponse 2024: 4.4B messages in 2023, senders with 500+ contacts; 39.64 / 3.25 / 0.15 / <0.01%; Apple auto-opens attribution
- Ahrefs, 4 Feb 2026: 300K keywords; GSC desktop; Dec 2023 vs Dec 2025; 58% against forecast, 7.3→1.6%; 7.6→3.9%; Seer 49.4–65.2%, Authoritas 47.5%, Indig >50%
- A9 pointers: rows 1, 2, 3, 4, 5–8, 9, 11, 13 and 14, A9 §6, the checkpoint dates (13-week steps through 31 Oct 2028), the four verdicts, read 7, and "not before quarter 8" all match the A9 rewrite
- Labels: every vendor, platform-published, executive, self-report and anecdote source carries its label where it is used
- Figures: every number names its owner, apart from the items in findings 5 and 9

**Unverifiable:** the Studio and Instagram menu locations (unsure item 1, except E6) cannot be checked without the live apps. Whether Studio offers the "all YouTube videos" retention comparison on a small channel (unsure item 9) cannot be checked either.

**A6 · fix · 1 error, 9 should-fix, 7 minor**
