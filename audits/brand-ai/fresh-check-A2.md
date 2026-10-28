---
audit: fresh check
unit: A2 · Audience and platform economics
course: brand-ai · A · Building a Marketable Personal Brand
model: Fable 5.1 (search on)
date: 2026-10-28
chat: https://claude.ai/chat/a0bcb6f1-bea8-4c17-8c10-a0079c9395c5
verdict: fix · 3 errors, 13 should-fix, 11 minor (all applied the same day)
---

# Fresh check · A2 · Audience and platform economics

Filed 28 October 2026 under backlog row P3 from the chat above, verbatim. The prompt was the `method.md` §5 fresh check ("Fresh check of one Brand + AI unit"); the checker had not seen the unit written and did not edit it. The unit as rewritten by Opus 5.5 on 28 October 2026 was the input; every finding was applied before the unit was filed (`courses/brand-ai/A2-audience-and-platform-economics.md`). The sources were opened in five parallel batches; the interim batch notes are left out and the report is the chat's final turn.

**A2 · fix.** 3 errors, 13 should-fix, 11 minor. Every finding below is a text replacement; nothing needs a rewrite.

Two notes on scope:
- **No unsure list.** The pasted unit ends at Sources, with no writer's unsure list. I started from the unit's own caveats ("could not match", "not confirmed", "not checked").
- **How the sources were checked.** Every cited page was opened today. Pew, Edison, beehiiv and Substack were read through a text-extraction step, not as raw HTML.

## Findings

1. **[error] [accuracy] §2 Instagram, Click Analytic base.**
   - Current: "its TikTok base is 15.8 million accounts with at least 10,000 followers, full-year 2025, and the page does not describe its Instagram base"
   - Problem: the page does describe its Instagram base: "compared with 5.9 million Instagram accounts and 1.9 million YouTube accounts". Only the Instagram follower threshold and period are missing. Click Analytic is also not labelled as vendor data.
   - Fix: "its TikTok base is 15.8 million accounts with at least 10,000 followers, full-year 2025, against 5.9 million Instagram accounts, for which the page gives no follower threshold or period (vendor data)"
   - Basis: https://www.clickanalytic.com/creator-economy-report/tiktok/

2. **[error] [attribution] §3, Kajabi bullet.**
   - Current: "([Kajabi, via Silicon UK, 17 Apr 2025](https://www.silicon.co.uk/press-release/kajabis-2025-state-of-creator-commerce-report-unveils-major-shift-in-the-creator-economy-as-creators-embrace-an-entrepreneurial-mindset); sample from [Net Influencer](https://www.netinfluencer.com/creator-commerce-rises-as-platform-dependency-declines-kajabi-report-shows/))"
   - Problem: Silicon UK carries only the three declines (−33%, −36%, −52%). The +20% digital downloads, the +14% educational content, the 1,717 sample and the fieldwork dates are all on Net Influencer.
   - Fix: "([Net Influencer, 17 Apr 2025, reporting Kajabi's 2025 State of Creator Commerce](https://www.netinfluencer.com/creator-commerce-rises-as-platform-dependency-declines-kajabi-report-shows/); the three declines also in [Silicon UK, 17 Apr 2025](https://www.silicon.co.uk/press-release/kajabis-2025-state-of-creator-commerce-report-unveils-major-shift-in-the-creator-economy-as-creators-embrace-an-entrepreneurial-mindset))"
   - Also in Sources: "Net Influencer, Kajabi creator commerce report summary." → "Net Influencer, Kajabi creator commerce report summary, 17 Apr 2025."
   - Basis: both URLs above.

3. **[error] [accuracy] §4, vidIQ sample.**
   - Current: "The sample excludes channels that quit before ten uploads and is observational."
   - Problem: the source excludes channels that "gave up before publishing ten same-format videos in their first 90 days". That cohort posted about weekly or faster. At his cadence, ten uploads take about 18 weeks, so the cohort is not comparable to his channel.
   - Fix: "The sample excludes channels that did not publish ten same-format videos within their first 90 days, so it is a cohort posting about weekly or faster (he reaches ten uploads in about 18 weeks; my arithmetic), and it is observational."
   - Basis: https://vidiq.com/research/youtube-first-10-videos-study/

4. **[should-fix] [figure] §1, Enkamp subscriber gain.**
   - Current: "had 1.67 million YouTube subscribers and added 30,000 in the 28 days to 18 October 2026 ([vidIQ, updated 18 Oct 2026]"
   - Problem: the live page, updated 28 Oct 2026, gives 1,670,000 subscribers "as of 2026-10-27" and a gain of 20,000 between 29 Sep and 26 Oct. The 30,000 and 18 Oct figures cannot be confirmed (unverifiable), and they conflict with the unit's "checked 28 October" line.
   - Fix: "had 1.67 million YouTube subscribers on 27 October 2026 and gained 20,000 between 29 September and 26 October ([vidIQ, updated 28 Oct 2026]"
   - Also replace "vidIQ, 18 Oct 2026" in the Deliverable 1 table with "vidIQ, 28 Oct 2026".
   - Also replace "updated 18 Oct 2026. https://vidiq.com/youtube-stats/channel/@karatebyjesse/" in Sources with "updated 28 Oct 2026. https://vidiq.com/youtube-stats/channel/@karatebyjesse/".
   - Basis: https://vidiq.com/youtube-stats/channel/@karatebyjesse/

5. **[should-fix] [attribution] §1, "largest karate creator".**
   - Current: "The largest karate creator, Jesse Enkamp,"
   - Problem: vidIQ makes no "largest" claim. FeedSpot ranks him first, but by a popularity score, not by subscribers alone.
   - Fix: "The top-ranked channel on FeedSpot's karate list, Jesse Enkamp,"
   - Also in Deliverable 1, replace "Largest creator 1.67M subscribers" with "Top of FeedSpot's list, 1.67M subscribers".
   - Basis: https://videos.feedspot.com/karate_youtube_channels/

6. **[should-fix] [figure] §2, Pew table.**
   - Current: "| Facebook | 78% | 70% | — |"
   - Problem: the fact sheet gives 70% for college graduates.
   - Fix: "| Facebook | 78% | 70% | 70% |"
   - Basis: https://www.pewresearch.org/internet/fact-sheet/social-media/

7. **[should-fix] [accuracy] §2 YouTube, Edison podcast figure.**
   - Current: "up from 51% in 2023 ([Edison Research, The Podcast Consumer 2026, slide 14]"
   - Problem: the 51% for 2023 is on slide 13, not slide 14. Slide 13 also notes that from 2025 the measure counts watching as well as listening, so the series is not like-for-like.
   - Fix: "up from 51% in 2023, though from 2025 the measure counts watching as well as listening ([Edison Research, The Podcast Consumer 2026, slides 13–14]"
   - Basis: https://www.edisonresearch.com/wp-content/uploads/2026/06/Podcast-Consumer-2026_Final_6.2.26.pdf

8. **[should-fix] [label] §3, Hidayat study.**
   - Current: "Why this audience trusts one creator enough to buy is a separate question with peer-reviewed evidence: perceived expertise and trustworthiness predicted the parasocial bond that predicted purchase intention in a 2026 study of 407 followers"
   - Problem: the sample is 407 Indonesian women following beauty influencers, in a cross-sectional survey. It is not "this audience". Attractiveness also had a significant direct effect on purchase intention, which the sentence leaves out.
   - Fix: "Why an audience trusts one creator enough to buy has peer-reviewed evidence from a different population: in a 2026 cross-sectional survey of 407 Indonesian women who follow beauty influencers, perceived expertise and trustworthiness predicted the parasocial bond that predicted purchase intention, while attractiveness did not predict the bond but was directly related to purchase intention"
   - Basis: https://public-pages-files-2025.frontiersin.org/journals/communication/articles/10.3389/fcomm.2026.1723759/text

9. **[should-fix] [label] §2 LinkedIn, Metricool study.**
   - Current: "In Metricool's study of 673,658 posts from 63,108 accounts,"
   - Problem: vendor data, not labelled as such.
   - Fix: "In Metricool's study (vendor data) of 673,658 posts from 63,108 accounts,"
   - Basis: https://metricool.com/linkedin-trends/

10. **[should-fix] [deliverable] Deliverable 2, Substack pick.**
    - Current: "- List starts at zero; platform network supplies half of subscriptions."
    - Problem: the 50% is Substack's own platform-wide figure for recommendations plus the app (Feb 2024). It does not say what share a new list gets.
    - Fix: "- List starts at zero; Substack says its network drove half of new subscriptions platform-wide (Feb 2024)."
    - Basis: https://on.substack.com/p/substacks-recommendations-network

11. **[should-fix] [deliverable] Deliverable 1, profile sentence.**
    - Current: "who pay for the gear that pursuit consumes and, on weaker evidence, for long-form guidance in it."
    - Problem: the gear evidence is one sponsored, mostly US runner survey. The body says no equivalent exists for karate.
    - Fix: "who spend on their pursuit's gear (sourced for runners only) and, on weaker evidence, would pay for long-form guidance in it."
    - Basis: https://sgbonline.com/global-survey-running-participation-surpasses-pre-pandemic-levels/

12. **[should-fix] [accuracy] §3, closing summary.**
    - Current: "Put together, the sourced picture is this audience pays for the equipment its pursuit consumes and, on weaker evidence, for long-form or structured guidance from someone it trusts."
    - Problem: the same stretch as finding 11, from runners to every pursuit.
    - Fix: "Put together, the sourced picture is that runners spend on the equipment running consumes (one sponsored, mostly US survey) and that this audience, on weaker evidence, would pay for long-form or structured guidance from someone it trusts."
    - Basis: as finding 11.

13. **[should-fix] [deliverable] §5 and Deliverable 2, Ghost break-even.**
    - Current: "Override if: paid revenue passes about $3,480 a year (Ghost Publisher becomes cheaper), or Substack's terms change on fees or export."
    - Problem: $29 is Ghost's price at the 1,000-member tier. Ghost's price rises with members, and a list earning $3,480 a year will likely exceed 1,000 members, so the break-even rises with the list.
    - Fix: "Override if: paid revenue passes about $3,480 a year while the list is within Ghost's 1,000-member tier (above it Ghost costs more, so recompute), or Substack's terms change on fees or export."
    - In §5, also replace "(my arithmetic; processor fees apply to both and are left out)" with "(my arithmetic, at Ghost's 1,000-member tier; processor fees apply to both and are left out)".
    - Basis: https://ghost.org/pricing/

14. **[should-fix] [coverage] §6, editing pointer to A5.**
    - Current: "The allocation therefore sets the episode at about 10 minutes and plans on the low end, 5 hours, which is A5's target to hit."
    - Problem: A5's brief targets "an editing workflow that lands a 12-minute episode in under 4 hours". The pointer misstates A5's target.
    - Fix: "The allocation therefore sets the episode at about 10 minutes and plans on the low end, 5 hours. A5's brief aims lower (a 12-minute episode in under 4 hours); the plan keeps 5 until that workflow is in use."
    - Basis: `units_data.py`, A5 brief.

15. **[should-fix] [deliverable] Deliverable 2, cut-the-load trigger.**
    - Current: "If even that cannot be met twice in a quarter, A9's \"cut the load\" verdict applies at the next checkpoint."
    - Problem: A9's trigger is "hours over 7 in three or more weeks of the quarter". A2 sets a different trigger under A9's name.
    - Fix: "Weeks over 7 hours are logged; three or more in a quarter trigger A9's \"cut the load\" verdict at the next checkpoint."
    - Basis: A9 rewrite, Deliverable 2, "The four verdicts".

16. **[should-fix] [coverage] §1, "employed" trait.**
    - Current: "**The serious pursuit.**"
    - Problem: "employed" is one of the brief's four traits but has no paragraph in §1. It appears only in the deliverable table.
    - Fix: insert before the current text: "**Employed.** No source used here describes the audience by employment; the trait is the brief's definition and is carried unsourced.\n\n"
    - Basis: `units_data.py`, A2 brief.

17. **[minor] [accuracy] §2 LinkedIn, Buffer ranking.**
    - Current: "the highest of the ten networks it measured"
    - Problem: Buffer measured ten platforms but ranks only seven by engagement rate; Bluesky, Mastodon and YouTube use other metrics.
    - Fix: "the highest of the seven networks it ranks by engagement rate (Buffer measured ten; three use other metrics)"
    - Basis: https://buffer.com/resources/state-of-social-media-engagement-2026/

18. **[minor] [attribution] §2 YouTube, Edison 37% figure.**
    - Current: "which I could not match to Edison's own slide"
    - Problem: slide 30 ("Service Used Most Often to Consume Podcasts", Q1 2026) carries a 31 → 36 → 37% series that matches Radio Ink. The text extraction did not confirm that the label is YouTube.
    - Fix: "which appears to match slide 30 of Edison's 2026 deck (service used most often, Q1 2026), though the slide's labels could not be confirmed"
    - Basis: the Edison PDF above; https://radioink.com/?p=103936

19. **[minor] [attribution] §2 Instagram, Mosseri.**
    - Current: "and sends slightly more important for reaching people who do not follow the account"
    - Problem: Mosseri says "unconnected content"; the follower gloss is Social Media Today's. Audit 1's PASS note on this was not applied.
    - Fix: "and sends slightly more important for \"unconnected content\", which Social Media Today glosses as reaching people who do not follow the account"
    - Basis: https://www.socialmediatoday.com/news/instagram-shares-algorithm-insights-2025/738034/

20. **[minor] [accuracy] §3, Amazon.es categories.**
    - Current: "6.0% on clothing and shoes"
    - Problem: these are two separate 6.0% categories.
    - Fix: "6.0% on clothing (Ropa y Accesorios) and on shoes (Zapatos, Bolsos y Carteras)"
    - Basis: https://afiliados.amazon.es/help/node/topic/GRXPHT8U84RAYDXZ

21. **[minor] [figure] §3, PYMNTS sample.**
    - Current: "PYMNTS surveyed 3,196 US adults"
    - Problem: the page says "U.S. consumers", weighted to the adult population.
    - Fix: "PYMNTS surveyed 3,196 US consumers, weighted to the US adult population"
    - Basis: https://www.pymnts.com/study_posts/influencers-may-not-be-so-influential-in-driving-purchases/

22. **[minor] [attribution] §1, ADHD Chatter host.**
    - Current: "ADHD Chatter, a long-form interview podcast with a male host,"
    - Problem: OutlierKit names no host. FeedSpot names Alex Partridge.
    - Fix: "ADHD Chatter, Alex Partridge's interview podcast (host named on FeedSpot),"
    - Basis: https://videos.feedspot.com/adhd_youtube_channels/

23. **[minor] [accuracy] §1, FeedSpot ranking.**
    - Current: "ranked by a popularity score that weighs subscribers, views, uploads and consistency"
    - Problem: FeedSpot's wording is "quality & consistency", not consistency alone.
    - Fix: "ranked by popularity, which FeedSpot says weighs subscribers, video views, uploads, and quality and consistency"
    - Basis: https://videos.feedspot.com/karate_youtube_channels/

24. **[minor] [accuracy] §4, Metricool threshold.**
    - Current: "and that above 35 Shorts a month performance fell back to the level of channels posting none"
    - Problem: the source says "35 or more" and "roughly the same level".
    - Fix: "and that at 35 or more Shorts a month performance fell back to roughly the level of channels posting none"
    - Basis: https://metricool.com/youtube-trends/

25. **[minor] [accuracy] §6, Welsh.**
    - Current: "can be written in 45 minutes from a fixed template"
    - Problem: Welsh calls it a "4-step formula".
    - Fix: "can be written in 45 minutes with a four-step formula"
    - Basis: https://justinwelsh.me/newsletter/my-secret-to-writing-a-great-newsletter-in-45-minutes

26. **[minor] [figure] §4, Shorts share arithmetic.**
    - Current: "AIR's 25–40% share means 0.7 to 1.5 Shorts a month"
    - Problem: 40% of uploads at 2.17 episodes a month is 1.44 Shorts.
    - Fix: "AIR's 25–40% share means 0.7 to 1.4 Shorts a month"
    - Basis: arithmetic.

27. **[minor] [accuracy] §1, birth years.**
    - Current: "which is exactly the millennial cohort as PYMNTS defines it (1981–1996), with the youngest Gen X years (PYMNTS: 1965–1980) just outside"
    - Problem: ages 30 to 45 during 2026 include people born in late 1980, so the band is not exactly the millennial cohort.
    - Fix: "which is the millennial cohort as PYMNTS defines it (1981–1996) plus part of 1980, the youngest Gen X year (PYMNTS: 1965–1980)"
    - Basis: arithmetic; PYMNTS page.

## Confirmed

**Audience (§1)**
- PYMNTS: millennials 1981–1996, Gen X 1965–1980; 72% and 58%; 12% more than six times; 10–15 Jan, no year given.
- RunRepeat: 107.9M results, 70,000+ events, 1986–2018; half-marathon age 37.5 → 39; average runner 39.3; dated 16 Jul 2019, updated 25 Mar 2024.
- Strava: 180M+ users, 185+ countries (Endurance Sportswire).
- CreatorDB: the quotation is exact; demographics behind a paywall; dated 25 Jul 2026.
- FrancsJeux: 818,000 subscribers; "from now on" exact; 8 Jan 2026.
- FeedSpot karate (2 Jul 2026): WKF 834K, TEAM KI 117K, Shotokan Karate 52.3K; positions 5–10 run 38.9K–16.1K.
- Song et al.: 40 articles, 30 countries, 2.58% and 6.76%, 2020 adjustment, J Glob Health 11:04009, 11 Feb 2021.
- FeedSpot ADHD: How to ADHD 1.9M; exactly 12 of 75 above 100K; ADHD Chatter 318K.
- OutlierKit: 408K subscribers, 83.3K average views, about 1.2 uploads a week; 21 Sep 2026.
- DataReportal Portugal: 7.59M, 6.35M, 6.10M members, 4.11M aged 18+; the ad-reach caveat; 8 Nov 2025.
- DataReportal Brazil: YouTube 150M in late 2025.
- Modash: top 20 of 172; four largest have English bios; largest Portuguese bio is 14.6K (@hugorbarreto); 21 Oct 2026.

**Platforms (§2)**
- Pew fact sheet: every other cell exact; NPORS, 5,511 adults, 30 Jan–18 Jun 2026; "ever use" wording; 19 Oct 2026.
- Edison Top 10 of 2025, slide 9: YouTube 32%, Spotify 25%, weekly consumers, Q1 2025.
- Radio Ink: 37%.
- Patreon State of Create: fan sample n=2,002, US, Aug 2024; feed shares 32/25/38; long-form 49% vs short-form 29%.
- Instagram blog, 10 Dec 2024: "shown to non-followers first"; no follower minimum.
- Haberman: Trial Reels available to professional accounts.
- Socialinsider Instagram: 7,032,675 posts from 131,955 under-5K accounts; 580 and 993; 38% → 22%.
- Metricool and HypeAuditor: about 700M posts, 28M influencer accounts, Jan–Jun 2025; about 3× likes and comments.
- Click Analytic: 39% vs 4.6%; 2.7% list a YouTube account.
- Instagram Subscriptions: Portugal added in the 20 Sep 2023 update.
- Meta Gifts: 33 countries, no Portugal; 6 Nov 2023.
- Socialinsider TikTok vs Reels: 350, 625 and 15,160 views; 145,444 under-5K accounts; Jan 2025–Jun 2026; under 1,000 followers excluded.
- Quasa (27 Jul 2026) and TT Calculator (9 Jul 2026): conflicting lists, neither includes Portugal. TikTok's own page is still unreadable.
- Metricool LinkedIn: 2.60% vs 1.60%; 1,451 vs 606 impressions; −27% for link posts on personal profiles.
- Buffer engagement: ~6.2% in key findings, ~6.1% in body text; Buffer-only posts; definitions differ.
- Globe and Mail: Kang's quotation exact, with "Etsy" in her own words.
- beehiiv: 37.98% → 41.24%; 65,000+ newsletters; 28B emails; 2.75× and 32× quotation exact.

**Conversion (§3)**
- Substack, Feb 2024: 50% of new subscriptions and 25% of new paid.
- Substack, Oct 2024: 3M from the app and 2M from recommendations; quotation exact.
- Pew 2022: 6,034 adults, 5–17 Jul 2022; 33% of social media users aged 30–49.
- Running USA via SGB: 7,400+ runners, 94% US, Jun–Jul 2024, sponsored by Active; 24.9%, 24.7%, 29%, 21%.
- Amazon.es: 4.0% Deportes y Fitness, 5.0% books.
- Kajabi via Net Influencer: 1,717 creators; Dec 2024–Jan 2025.

**YouTube (§4)**
- YouTube Help 141805: all three quotations exact.
- YouTube Help 16533387: the publish-time quotation exact.
- PPC Land, 2 Sep 2026: "accumulate the bulk…" is PPC Land's own prose; the interview was 1 Sep 2026.
- vidIQ first 10: 180 → 272 views on 137,355 channels; 1,362 → 1,344 on 367,243; quotation exact.
- Humble&Brag: month six, 24–26 videos; one upload a week at about 450 first-week views.
- YouTube Help 72902: 55% and 45%.
- Alphabet's Q3 2025 call (29 Oct 2025): the Shorts quotation is exact.
- AIR frequency: 172,000 (82 channels) vs 77,700 (63 channels); Education 116,000; predictable-schedule finding; "correlational".
- AIR Shorts: 41%, 39% and 37%; "optimal Shorts ratio" 25–40%; "crowding out" above 55%; March 2025–March 2026; at least 40 videos.
- Metricool YouTube: 799,718 videos from 71,177 accounts; 8,789 vs 5,985, which Metricool itself calls 46%.

**Archive (§5)**
- Substack Support (29 Sep 2026): 10%, Stripe 2.9% + $0.30, Billing 0.7%.
- Substack dashboard guide: CSV export.
- beehiiv: free to 2,500; Lite $49 and Pro $95 a month billed yearly.
- Kit: free to 10,000; 3.5% + $0.30.
- Ghost: $29 Publisher and $18 Starter, both billed yearly; Starter has no paid subscriptions; 0% from Ghost.
- Pew AI summaries: 900 adults, March 2025; 8% vs 15%; 1%.
- Ahrefs: 300,000 keywords, Dec 2023 vs Dec 2025, −58%.
- Seer: 3,119 terms across 42 organisations; 1.76% → 0.61%.

**Hours (§6)**
- Tasty Edits: 30–60 minutes per finished minute, no method stated.
- Buffer Instagram: 2.1M posts, 102K accounts, 0.12% and 0.26%, feed posts only.
- YouTube Help 13615784: "more consistent and similar in topic or format" exact; responding to comments listed.
- Amy Suto: quotation exact.

**Arithmetic**
- Hours: 12.0 per fortnight, 6.0 a week, 9.0 in the bad fortnight.
- Ghost break-even: $3,480.
- Amazon example: €7.20.
- Shoe spend: 49.6% above $300.
- Cadence: 2.17 episodes a month; video 24 at about month 11 and video 26 at about month 12; Shorts shares 50% at one per episode, 67–75% at two to three.

**Pointers**
- The rewritten A9 holds the other pointers: row 13 is the email list; Deliverable 2 read 2 is hours; the stop rule; the quarter-4 review on 2 Nov 2027; no platform change at review.
- A3's brief does say "2–3 Shorts per episode".

**Coverage**
- Covered: age, serious pursuit, restless brain, platforms with 2025–26 data, conversion, allocation for 5–7 h, why long-form compounds, where the archive lives.
- Thin: employed (finding 16).

**Labels**
- Labelled: anecdotes (Welsh, Suto), vendor (Socialinsider, Metricool YouTube, Ahrefs, Seer, Tasty Edits), company and platform data (Patreon, beehiiv, Substack, Strava), sponsored (Running USA), correlational (AIR, vidIQ, Metricool), model (Humble&Brag).
- Not labelled: Metricool LinkedIn (finding 9), Click Analytic (finding 1), Hidayat (finding 8).

**Deliverables**
- Both are present in full and usable without the unit. Every hour figure is either cited or marked as the allocation's estimate. The two stretches are findings 10 and 11.

**Audit 1 errata touching A2: all applied except one.**
- Applied:
  - Trial Reels re-sourced, 1,000-follower rule dropped.
  - 3× re-cited, as likes and comments.
  - TikTok +40% and −23% dropped.
  - Welsh reworded.
  - Buffer 6.2% re-linked.
  - Globe and Mail: Kang quoted from the canonical URL.
  - Regular-viewer timing consistent with the months definition.
  - Enkamp count re-cited.
  - Modash "six of eleven" dropped.
  - HypeAuditor Brazil dropped; 150M re-cited to DataReportal.
  - WKF figure dated.
  - Humble&Brag: "exceed views", not earnings.
  - Metricool: "above the global average".
  - DataReportal: ad-reach labelled.
  - The minor's name is absent.
- Not applied: the Mosseri gloss note (finding 19).

---

A2 · **fix** · error 3 · should-fix 13 · minor 11
