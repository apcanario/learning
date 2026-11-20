---
code: A6
title: How growth works, per platform
course: brand-ai · A · Building a Marketable Personal Brand
model: Opus 5.5
written: 2026-10-28
search: on
name: A6 · Growth per platform
intro: Unit A6, rewritten 28 Oct 2026 by Opus 5.5 in its own chat, search on; fresh check the same day (Fable 5.1): fix, 1 error, 9 should-fix, 7 minor, all applied. Deliverables: the per-platform playbook (each rule names its evidence; his own conventions marked) and the metrics sheet read once a quarter on A9's checkpoint dates. Unverified: Studio and Instagram menu locations. Staleness check due 28 Apr 2027.
---

# A6 · How growth works, per platform

Every source in this unit was opened on 28 October 2026 (YouTube Help 12843009 through A9's check the same day). Platform rules, metric definitions and product features carry that date unless another is given. Benchmarks for what a one-person channel should expect (views per upload, subscriber odds, list growth, conversion) are A9's job and are not restated here; where this unit needs one, it points to the row of A9's expectation sheet.

Three kinds of source carry the unit, and they are labelled where they appear. Platform-official pages (YouTube Help, Instagram's own blog and creator site, Substack's support pages) say how a system is meant to work, without numbers on how much each signal weighs. Executives speaking in interviews (Todd Beaupré for YouTube, Adam Mosseri for Instagram) add direction, usually reported second-hand and hedged. Vendor datasets (Metricool, Socialinsider, Buffer, AIR Media-Tech, beehiiv, GetResponse, Ahrefs) supply the numbers; they are drawn from each vendor's own users or clients, are correlational, and several cover brand accounts, not people.

## 1 · YouTube

### 1.1 Browse, suggested and search are three different machines

YouTube Analytics sorts every view by where it started. The definitions matter, because the three large sources work differently ([YouTube Help, Understand your YouTube video reach, answer 1714921](https://support.google.com/youtube/answer/1714921?hl=en-GB)):

- **Browse features**: traffic from Home, Subscriptions, Watch Later, trending/Explore and other browsing features.
- **Suggested videos**: traffic from suggestions next to or after other videos, and from links in video descriptions.
- **YouTube search**: traffic from search results.
- Smaller sources: channel pages, playlists, notifications and emails to subscribers, external sites and apps that embed or link the video, the Shorts feed, and direct or unknown.

**Browse and suggested are a pull, ranked per viewer.** Beaupré, YouTube's senior director of growth and discovery, said in 2024 that creators picture YouTube pushing videos out to people when the process runs the other way, with viewers pulling, and that discovery "is focused more on individual videos" than on channels ([Search Engine Journal, 4 Mar 2024](https://www.searchenginejournal.com/youtube-algorithm-myths-debunked-insights-from-the-growth-team/510091/)). In a Creator Insider interview published 1 September 2026 he said every viewer gets a ranking of their own, and that the main place subscribers watch a channel they follow is the suggested list on the watch page, with the subscriptions feed small by comparison ([PPC Land, 2 Sep 2026](https://ppc.land/subscribers-skip-90-of-uploads-in-their-feed-youtube-director-says/)). In the same interview he put subscriber click-through in the subscribers row at "maybe a 10% or less", a hedged figure with no sample behind it. A subscriber is therefore one input to a per-viewer prediction; the subscription does not deliver the video.

**Search is a query match.** YouTube's own page on search names three elements, whose importance "may vary by search type" ([YouTube Help, How YouTube search works](https://support.google.com/youtube/answer/16090438?hl=en)):

- relevance: how well the title, tags, description and video content match the query;
- engagement: signals such as the watch time of a particular video for a particular query;
- quality: signals of which channels show expertise, authoritativeness and trustworthiness on a topic.

The page says results may also use the viewer's search and watch history, and that YouTube does not accept payment for organic placement. It says nothing about channel size or recency.

**How big each source is for a channel like his is unmeasured.** The only large split found is Metricool's 2026 study of 799,718 videos from 71,177 accounts (published 29 July 2026): the Shorts feed carried more than 61% of organic views, subscribers 11%, YouTube search 9%, related videos 5.77%, playlists 5.05% and channel visits about 3% ([Metricool, YouTube Trends 2026](https://metricool.com/youtube-trends/)). That is vendor data from Metricool's users, dominated by Shorts volume, and it is not a long-form or small-channel split. No source found gives the traffic mix of a small long-form channel, so his own Studio split is the only figure he can use, and it is a baseline to watch, with nothing to compare it against.

```viz
{
 "kind": "compare",
 "unit": "%",
 "max": 100,
 "caption": "Share of organic YouTube views by traffic source across Metricool's sample of 799,718 videos from 71,177 accounts (Shorts feed more than 61%; channel visits about 3%). Vendor data from Metricool's users, Shorts-heavy, not a long-form or small-channel split. §1.1; <a href=\"https://metricool.com/youtube-trends/\">Metricool, YouTube Trends 2026</a>, 29 Jul 2026.",
 "rows": [
  {
   "label": "Shorts feed",
   "value": 61
  },
  {
   "label": "Subscribers",
   "value": 11
  },
  {
   "label": "YouTube search",
   "value": 9
  },
  {
   "label": "Related videos",
   "value": 5.77
  },
  {
   "label": "Playlists",
   "value": 5.05
  },
  {
   "label": "Channel visits",
   "value": 3
  }
 ]
}
```

What the mechanics imply for a journey channel (my reading, from the definitions above): an episode can be built to be found by a query (the title and description carry the words a stranger would type, and the video holds that searcher), or built to be picked by the per-viewer prediction on Home and the watch page (packaging and retention). The two are scored on different evidence, so the traffic-source report is where he learns which kind each episode turned out to be.

### 1.2 Click-through rate and retention: the two numbers YouTube says it uses

YouTube's help page on impressions states the rule both ways: it recommends a video when the video is relevant to the viewer and its average view duration shows viewers find it interesting; a video with "high CTR but low average view duration and lower than expected Impressions" carries the clickbait signature ([YouTube Help, Impressions and click-through rate](https://support.google.com/youtube/answer/7628154?hl=en-GB)). The same page sets out how to read CTR:

- Impressions CTR is how often viewers watched after seeing a registered impression on YouTube. Impressions on external websites and end screens are not counted, and some views do not start from a thumbnail impression at all.
- Half of all channels and videos sit between 2% and 10%. Videos or channels less than a week old, or with fewer than 100 views, can range more widely still.
- Videos with few impressions tend to have higher CTR because they reach a narrower, more loyal audience; a video on the homepage will naturally have lower CTR.
- Compare CTRs between videos over the long term, bear traffic sources in mind, and avoid checking CTR immediately after upload; small variations are not cause for immediate action.

YouTube publishes no "good" CTR. The "4–6% is good" target that circulates in vendor posts has no dataset behind it and is not used in this course (Audit 1 erratum). The 2–10% range is context only (A9 row 2).

**YouTube's own testing tool chooses on watch time.** Test & Compare lets a channel upload up to three titles, thumbnails or title-thumbnail pairs; the test is optimised "for overall watch time over other metrics, like click-through-rate", takes a few days to two weeks, runs from YouTube Studio on a computer only, and needs advanced features enabled; if the result is inconclusive the first variant uploaded stays ([YouTube Help, A/B test titles & thumbnails](https://support.google.com/youtube/answer/16391400?hl=en)). That is the platform stating, in a product, which of the two numbers it values when they conflict.

**Retention is read against his own videos.** Studio's typical-retention line compares a video with the channel's 10 latest videos of similar length, or with all YouTube videos of similar length; Intro is the share of the audience still watching after the first 30 seconds; spikes mark rewatched or shared moments, dips mark abandoning or skipping; these highlights need a video of at least 60 seconds with at least 100 views ([YouTube Help, Measure key moments for audience retention](https://support.google.com/youtube/answer/9314415?hl=en)). The only external bands for average percentage viewed found for this unit are vidIQ's, which it labels "vidIQ guidance" and publishes without a sample (A9 row 3; [vidIQ, updated 21 Jul 2026](https://vidiq.com/blog/post/average-view-duration/)).

**Regular viewers are a loyalty count, and YouTube says they do not drive reach.** Regular viewers watched a video on the channel at least once a month for more than six months of the past year; casual viewers did so for one to five months; and YouTube states that these segments have no effect on reach or monetisation ([YouTube Help, Understand new, casual and regular viewers](https://support.google.com/youtube/answer/10246996?hl=en)). YouTube's tips for growing the casual and regular segments are content "more consistent and similar in topic or format", a series built from topics that already worked, regular publishing and responding to comments, with no effect sizes given ([YouTube Help, New, casual and regular viewers tips](https://support.google.com/youtube/answer/13615784?hl=en)). The count is empty for the first six months by construction and has no benchmark (A9 row 4).

### 1.3 Why long-form compounds, and how far the evidence goes

"Compounds" here means a published long-form episode keeps earning views and watch hours after its launch week. Four platform-side facts support the mechanism:

1. **An old video stays eligible.** Beaupré said YouTube tries not to over-weight a channel's history where it does not predict how the next video will do, and that a weak video followed by a strong one should not hold the strong one back; the article also reports him saying older videos can gain traction when audience interest renews ([Search Engine Journal, 4 Mar 2024](https://www.searchenginejournal.com/youtube-algorithm-myths-debunked-insights-from-the-growth-team/510091/)). PPC Land's report of the 2026 interview says some videos gather most of their audience a month or more after publication; it gives that without a direct quote ([PPC Land, 2 Sep 2026](https://ppc.land/subscribers-skip-90-of-uploads-in-their-feed-youtube-director-says/)).
2. **Search matches a query, whenever it is typed.** Relevance and per-query engagement (§1.1) are properties of the video and the query; nothing on YouTube's search page ties them to upload date ([YouTube Help 16090438](https://support.google.com/youtube/answer/16090438?hl=en)). That an evergreen query keeps sending viewers is my inference from the page, not a measured figure.
3. **Only public long-form builds watch hours.** The Partner Program counts "qualified watch hours gained from long-form videos you've set public"; Shorts-feed watch time, private, unlisted and deleted videos do not count ([YouTube Help, YPP overview](https://support.google.com/youtube/answer/72851?hl=en)). From 1 February 2027 the ad-revenue threshold for new applicants is 8,000 qualified watch hours in the last 365 days ([YouTube Help, Changes to the YouTube Partner Program](https://support.google.com/youtube/answer/12843009?hl=en); A9 row 11). Every public episode adds to that rolling total for a year; unlisting or deleting one removes it.
4. **The screen favours length.** YouTube said in February 2024 that viewers watch more than 1 billion hours of YouTube on TVs every day ([YouTube Official Blog, 20 Feb 2024](https://blog.youtube/news-and-events/youtube-number-one-streamer-nielsen/)). Beaupré in 2026 attributed the rise of longer videos to people watching on television, with recommendations following that demand ([PPC Land, 2 Sep 2026](https://ppc.land/subscribers-skip-90-of-uploads-in-their-feed-youtube-director-says/)). In Metricool's 2026 sample, long-form average view duration was 2.51 minutes against about 16 seconds for Shorts ([Metricool](https://metricool.com/youtube-trends/)).

Against that, the vendor data shows the launch window still dominates: in Metricool's sample videos usually peak in the first three days and about 83% of interactions arrive within ten days ([Metricool, 29 Jul 2026](https://metricool.com/youtube-trends/)). That sample is Shorts-heavy and counts interactions; it is still the only timing figure found. No dataset measures what share of a small long-form channel's views come from its back catalogue. So the mechanism is sourced and its size is not, and the metrics sheet below measures it on his own channel (row Y7).

**Breaks.** YouTube's position is that the system does not punish a channel for a break or a weak video (SEJ, above). AIR Media-Tech's study of 18,000 English-language channels across 11 niches and four size segments, with its primary analysis on the 100,000–1,000,000 monthly-views segment (published 8 June 2026) found that channels going dark for 14 or more days three or more times a year got fewer views per video, and that channels on a predictable schedule got more views per subscriber than channels posting the same volume on random days; it gives no effect sizes and states the data is correlational ([AIR Media-Tech, 8 Jun 2026](https://air.io/en/audience-growth/does-posting-more-on-youtube-help-we-studied-18000-channels-to-find-out)). The two do not contradict each other: YouTube describes the mechanism, AIR describes what happened to channels that missed weeks, which may reflect the reasons they missed them. AIR's channels are far larger than his. The cadence figures by upload band (weekly against bi-weekly: about 1.5 times the view growth and 3.9 times the subscriber growth, on channels already past 1,000) are in A9 row 9.

## 2 · Instagram

### 2.1 Reels and Explore show strangers; Feed and Stories serve followers

Instagram's own explanation (updated 31 May 2023) says each part of the app runs its own ranking system ([Instagram, Instagram Ranking Explained](https://about.instagram.com/blog/announcements/instagram-ranking-explained)):

| Surface | What it shows (Instagram, 2023) | What it predicts |
|---|---|---|
| Feed | posts from accounts you follow, recommended accounts and ads | whether you spend a few seconds, comment, like, share, tap the profile photo |
| Stories | people the viewer has chosen to follow, plus ads | whether you tap into, reply to or skip a story |
| Explore | mostly people the viewer does not follow | likes, saves, shares |
| Reels | "the majority of what you see is from accounts you don't follow" | whether you reshare, watch to the end, like, open the audio page |

That table is the brief's claim in Instagram's own terms: Reels (and Explore) are where a non-follower meets the account; Stories reach followers only; Feed is mostly followers with recommendations mixed in.

Mosseri updated the signals in January 2025: watch time, likes and sends are the three that matter most; likes weigh slightly more for connected content and "sends are slightly more important for unconnected content"; and in Insights creators should watch average watch time, likes per reach and sends per reach ([Social Media Today, 22 Jan 2025](https://www.socialmediatoday.com/news/instagram-shares-algorithm-insights-2025/738034/)). "Unconnected" is not defined in the article; it is read here as content shown to people who do not follow the account.

Two follower-side and stranger-side mechanics are sourced to Instagram or to reports of what its head said:

- **Carousels get a second pass at followers.** In Lia Haberman's summary of what Mosseri said in 2024, the algorithm gives a carousel "a second chance after it's posted, resurfacing it to followers who previously swiped by"; the words are Haberman's, not a transcript of Mosseri ( [Lia Haberman, ICYMI, 14 Oct 2025](https://liahaberman.substack.com/p/the-best-instagram-content-formats)).
- **Trial Reels test on strangers.** A trial Reel is "shown to non-followers first"; followers do not see it in Feed or the Reels tab (it can still reach them through a DM share); engagement metrics appear after about 24 hours; the creator can share it to everyone at any time, or set it to share automatically if it performs well on views in the first 72 hours ([Meta, Trial reels, 10 Dec 2024, updated 26 Jun 2025](https://about.fb.com/news/2024/12/trial-reels-try-content-non-followers/); [Instagram Creators, 10 Dec 2024](https://creators.instagram.com/blog/instagram-trial-reels)). Both pages refer eligibility to the Help Center without stating it. The 1,000-follower requirement in the earlier research has no source on either page (Audit 1 erratum); it does have one elsewhere: Mosseri said in July 2025 that trial reels are available to creators with at least 1,000 followers and a public account ([Social Media Today, 13 Jul 2025](https://www.socialmediatoday.com/news/instagram-expands-access-trial-reels/752895/), executive statement reported second-hand; no later change found).

**Which format reaches further at small sizes is disputed.** Metricool and HypeAuditor's Instagram Content Playbook (700 million posts from 28 million influencer accounts, January–June 2025, medians) reports that Reels have the highest reach in every follower tier ([Metricool press release, 14 Oct 2025](https://metricool.com/press-release-instagram-content-playbook/)). Socialinsider's brand dataset says the opposite for views per post: at 1,000–5,000 followers in 2025, Reels averaged 580 views, carousels 993 and images 417 ([Socialinsider, Instagram benchmarks](https://www.socialinsider.io/instagram-benchmarks)). The populations differ (influencer accounts against business accounts), as do the measures (median reach against average views). For a personal account, the platform's own description (Reels mostly reach non-followers) and the influencer dataset agree; the brand dataset is the dissent. His own Insights split of views by followers and non-followers settles it for his account (row I1).

### 2.2 Reach is rented

"Rented" means the platform decides, and can change, who sees the work, how it is counted, and whether a viewer can leave. Each of those has happened on Instagram and is documented.

**Recommendation can be withdrawn without touching followers.** Instagram's original-content guidelines: an account that mostly posts unoriginal content "may not be seen in recommendations to new audiences"; it regains eligibility when most of its recent Reels, photos and carousels are original over a 30-day period; content shown to existing followers is not affected. Unoriginal includes reposts of others' work, screenshots even with credit, and minor edits such as borders, watermarks, speed changes or a credit line ([Instagram Creators, Original content guidelines](https://creators.instagram.com/original-content-guidelines/)). On 30 April 2026 Instagram extended the rule from Reels (where it had applied since 2024) to photos and carousels, said aggregators "will no longer be eligible for recommendations across Instagram", pointed creators to Account Status to check and appeal, and said 75% of recommendations in the US now come from original posts ([Instagram Creators, Rewarding original creators, 30 Apr 2026](https://creators.instagram.com/blog/rewarding-original-creators-on-instagram)). The 2023 ranking page already listed low-resolution or watermarked Reels, and Reels already posted on Instagram, among the reasons for less distribution ([Instagram Ranking Explained](https://about.instagram.com/blog/announcements/instagram-ranking-explained)). For him: posting mostly reposts of training partners' videos can take the account out of recommendations to new audiences; a clip of his own that carries another app's watermark stays eligible but, on Instagram's 2023 account, gets less distribution.

**The exits are narrow.** Instagram does not allow links in ordinary captions (Social Media Today, Nov 2024), though since March 2026 Meta has been testing clickable caption links for Meta Verified subscribers (Engadget, 12 Mar 2026); Story link stickers are, in Social Media Today's reading, not reach-restricted "though they are only distributed to your followers" ([Social Media Today, 25 Nov 2024](https://socialmediatoday.com/news/heres-each-big-social-platform-stand-external-links/733946/)). For a stranger who finds a Reel on an account without Meta Verified, the bio link is the remaining exit (his reading of the two sources; no source states it).

**The scoreboard is redefined by the landlord.** In August 2024 Instagram made Views the primary metric across Reels, posts and Stories and counted repeat views ([Social Media Today, 7 Aug 2024](https://socialmediatoday.com/news/instagram-updates-metrics-to-focus-creators-on-views/723645/)); Metricool reported that impressions would leave Insights and that Instagram would show views split by Followers and Non-followers ([Metricool, 14 Aug 2024](https://metricool.com/instagram-insights/)). In January 2025 it added a Reels view rate (share continuing past three seconds) and views over time against the creator's usual ([TechCrunch, 29 Jan 2025](https://techcrunch.com/2025/01/29/instagram-gives-creators-more-insight-into-their-reels-performance)); in August 2025 it replaced view rate with skip rate, the share of views from people who "decided to skip your reel during those first 3 seconds", and added a retention chart ([Social Media Today, 24 Aug 2025](https://www.socialmediatoday.com/news/instagram-adds-retention-insights-reels/758464/)). A metric he tracks today may not exist under the same name in a year; the metrics sheet records the definition next to each number for that reason.

**Little attention goes to followed creators.** In Patreon's company-sponsored State of Create survey (1,000 US creators and 2,000 US fans, via NewtonX, August 2024), only 24% of users' Instagram time went to creators they follow, against 32% on YouTube and 38% on TikTok, and 53% of creators said followers were harder to reach than five years earlier ([Net Influencer, 21 Feb 2025](https://www.netinfluencer.com/patreon-2025-state-of-create-report-how-creators-are-breaking-free-from-platform-control/)). That is self-report from a company selling the alternative.

### 2.3 How much reach a small account rents

The best small-account figures are brand data. Socialinsider's sample (published 20 February 2026, updated 22 October 2026; its "2026" columns are 2025 values relabelled; 131,955 business accounts and 7,032,675 posts under 5,000 followers) gives the 1,000–5,000 tier 580 views per Reel, 993 per carousel and 417 per image, and annual audience growth falling from 38.0% in 2024 to 22.0% in 2025; the 5,000–10,000 tier fell from 35.0% to 20.3% ([Socialinsider](https://www.socialinsider.io/instagram-benchmarks)). Personal accounts may do better on interaction: in the Metricool and HypeAuditor data, influencer posts get "approximately 3 times more likes and comments than brand accounts" ([Metricool, 14 Oct 2025](https://metricool.com/press-release-instagram-content-playbook/)). That multiple is for likes and comments; no source gives one for views or growth, so the brand figures are the only sourced floor.

```viz
{
 "kind": "compare",
 "caption": "Average views per post by format for business accounts with 1,000–5,000 followers in 2025. Brand data, not personal accounts; the influencer dataset in §2.1 finds Reels reach furthest. §2.3; <a href=\"https://www.socialinsider.io/instagram-benchmarks\">Socialinsider, Instagram benchmarks</a>, updated 22 Oct 2026.",
 "rows": [
  {
   "label": "Carousels",
   "value": 993
  },
  {
   "label": "Reels",
   "value": 580
  },
  {
   "label": "Images",
   "value": 417
  }
 ]
}
```

Frequency is the one lever with within-account evidence. Buffer's study of about 2.1 million feed posts from 102,000-plus accounts (published 13 August 2025) used a fixed-effects model comparing each account's weeks with itself: against weeks with no posts, weekly follower growth rose 0.12% in weeks with 1–2 posts, 0.26% with 3–5, 0.44% with 6–9 and 0.66% with 10 or more; reach per post was about 12% higher at 3–5 posts a week than at 1–2. Stories were excluded, and results were not split by account size ([Buffer, How often to post on Instagram](https://buffer.com/library/how-often-to-post-on-instagram/)). Vendor data on Buffer's users. How many of his 5–7 hours go to Instagram is A2's allocation.

```viz
{
 "kind": "compare",
 "unit": "%",
 "caption": "Rise in weekly follower growth against weeks with no posts, by feed posts a week, from a fixed-effects model comparing each account's weeks with itself (about 2.1 million feed posts, 102,000-plus accounts; Stories excluded; not split by account size). Vendor data on Buffer's users. §2.3; <a href=\"https://buffer.com/library/how-often-to-post-on-instagram/\">Buffer, How often to post on Instagram</a>, 13 Aug 2025.",
 "rows": [
  {
   "label": "1–2 posts",
   "value": 0.12
  },
  {
   "label": "3–5 posts",
   "value": 0.26
  },
  {
   "label": "6–9 posts",
   "value": 0.44
  },
  {
   "label": "10 or more",
   "value": 0.66
  }
 ]
}
```

## 3 · Substack and his own site

### 3.1 What "owned" means, exactly

On Substack the list belongs to the writer, who will "always own your readers’ email addresses" and can export them at any time, including subscribers who joined through the app ([Substack Support](https://support.substack.com/hc/en-us/articles/4571360165396-What-happens-to-my-email-list-for-readers-who-read-in-the-Substack-app)). One part is not portable. As of Substack's FAQ of 18 August 2025, readers in the iOS app can pay through Apple's in-app purchase; the writer still gets their email address, but "Apple does not transfer billing relationships between platforms", so a paid subscriber who bought in the iOS app has to re-subscribe if the publication moves; Apple takes 30% in the first year and 15% after, and Substack's 10% is charged on the web price ([Substack, In-app payments FAQ, 18 Aug 2025](https://on.substack.com/p/in-app-payments-iap-faq)). Owned, on Substack, means the addresses; the payment relationship can sit with Apple.

### 3.2 Slow, and where new readers come from

How slowly lists grow is in A9 §6 and row 13: beehiiv's self-selected 2025 cohort at a median of 482 subscribers in month one and 8,314 at twelve months, against documented part-time cases at about 2,000 after a year and 2,500 after three.

Discovery on a newsletter platform is itself run by the platform. Substack said in February 2024 that its recommendations and app together drove "50% of all new subscriptions" and a quarter of new paid subscriptions across the network ([On Substack, 22 Feb 2024](https://on.substack.com/p/substacks-recommendations-network)); no newer official split was found, and the figure is network-wide; no per-writer split is given. beehiiv reports that newsletters using its Recommendations grew 2.75 times faster on average and that newsletters recommending others were 32 times more likely to be recommended back ([beehiiv, State of Newsletters 2026, 6 Jan 2026](https://www.beehiiv.com/blog/beehiiv-the-state-of-newsletters-2026)); platform-published, on beehiiv's own users.

One documented case shows the gap between network attention and subscribers. Amy Suto spent six months going all-in on Substack Notes: Notes brought 1,459 free subscribers against 8,366 from onboarding and recommendations in the same window, and a Note with 15,800 likes and 28,055 clicks produced 378 free subscribers and no paid ones ([Amy Suto, 14 Jul 2026](https://www.amysuto.com/desk-of-amy-suto/substack-notes)). Anecdote, one writer, who reports 42,000-plus subscribers over three years.

So the owned channel has a rented front door: the list is his, and a large share of new arrivals on Substack come through Substack's own recommendation system.

### 3.3 What the inbox numbers mean

Email reaches the people on the list in a way no feed does, and the open rate overstates by how much. beehiiv's average across 65,000-plus newsletters and 28 billion emails in 2025 was a 41.24% open rate and a 3.23% click rate; the same report says Apple's Mail Privacy Protection "has made the traditional open rate less reliable, as it auto-loads images" ([beehiiv, 6 Jan 2026](https://www.beehiiv.com/blog/beehiiv-the-state-of-newsletters-2026)). Apple's own description: the feature "downloads remote content in the background by default" and stops senders learning when or how often a message was opened ([Apple, Mail Privacy Protection](https://www.apple.com/legal/privacy/data/en/mail-privacy-protection/)). GetResponse's 2024 benchmarks (4.4 billion messages from senders with at least 500 contacts, calendar 2023) give an average 39.64% open rate, 3.25% click-through, 0.15% unsubscribe rate and spam complaints below 0.01%, and also attribute part of the rise in opens to Apple's auto-opens ([GetResponse, Email Marketing Benchmarks 2024](https://www.getresponse.com/resources/reports/email-marketing-benchmarks?web=1)). Both are vendor averages across every sender on each platform; neither isolates creator newsletters. The consequence for reading: clicks and unsubscribes are counted events; opens are partly a machine loading images.

### 3.4 His own site

A personal site is the one place no platform ranks, and it is a weak discovery channel in 2026. Ahrefs compared 300,000 keywords in Google Search Console desktop data between December 2023 and December 2025: where an AI Overview appears, position-1 click-through fell 58% against its forecast, from 7.3% to 1.6% raw; informational keywords without an AI Overview fell from 7.6% to 3.9% ([Ahrefs, 4 Feb 2026](https://ahrefs.com/blog/ai-overviews-reduce-clicks-update)). Ahrefs sells SEO tools; it cites Seer Interactive, Authoritas and Kevin Indig finding declines of 47–65%. No data was found for Portuguese-language queries. The site's sourced uses are narrower: it holds the written record, and a YouTube video embedded there shows in Studio as External traffic ([YouTube Help 1714921](https://support.google.com/youtube/answer/1714921?hl=en-GB)).

## 4 · What carries across, and where the evidence stops

On all three platforms, a new viewer arrives through a system the creator does not control: YouTube's per-viewer prediction and query match, Instagram's recommendation surfaces, Substack's recommendations and app. What differs is what the creator keeps afterwards. YouTube keeps the video eligible and its watch hours counting for a year; Instagram keeps followers, whose share of attention is small and who are served mainly on Feed and Stories, the surfaces built for them; email keeps the address, exportable, with an inbox that reports clicks reliably and opens unreliably.

Gaps that the deliverable cannot fill with a sourced number, and does not try to:

- the traffic-source mix of a small long-form YouTube channel;
- the share of views a small channel's back catalogue earns;
- reach or views benchmarks for personal Instagram accounts under 10,000 followers (only brand data and a likes-and-comments multiple);
- skip-rate, sends-per-reach or bio-link click benchmarks of any kind;
- the share of a single Substack writer's subscribers that come from the network;
- anything Portugal-specific on these mechanics.

Each of those rows in the metrics sheet records his own baseline and judges direction only.

## Deliverable 1 · Per-platform playbook

Checked 28 October 2026. Each rule names the evidence it rests on. Rules marked **(his rule)** are decision conventions set from that evidence; no source sets them. Hours per platform are A2's allocation; cadence is the course goal's (one long-form episode every two weeks); verdicts (continue, change format, cut the load, stop) are A9's quarterly checkpoints.

### YouTube · the home channel

**What it rewards.** Per-video relevance plus watch time, judged per viewer; a query match in search. Basis: YouTube Help 7628154, 16090438; Beaupré (SEJ 2024; PPC Land 2026).

1. **Decide each episode's entry door before scripting.** Search-shaped: the title and description carry the words a stranger would type for the problem the episode solves. Browse-shaped: the title and thumbnail sell the story to a person who has never heard of him. Basis: search relevance is title, tags, description and content against the query (YouTube Help 16090438); browse and suggested rank per viewer (PPC Land 2026).
2. **Make the first 30 seconds deliver what the title and thumbnail promised.** Basis: Studio's Intro metric measures exactly that window (YouTube Help 9314415); high CTR with low average view duration is YouTube's clickbait signature and gets fewer impressions (YouTube Help 7628154).
3. **Run Test & Compare on every episode with two or three title or thumbnail variants, and accept its pick.** Basis: it chooses on watch time share over CTR, over a few days to two weeks; desktop Studio only, advanced features required (YouTube Help 16391400).
4. **Judge packaging only on uploads at least seven days old, by traffic source, across several uploads.** Basis: wider CTR range in the first week and under 100 views; compare over the long term; traffic source changes CTR; small variations are not grounds for action (YouTube Help 7628154).
5. **Keep every published episode public.** No deleting or unlisting weak ones. Basis: only public long-form earns qualified watch hours (YouTube Help 72851); a weak video does not lastingly harm the channel and older videos can regain traction (SEJ 2024).
6. **Hold one recognisable format per season, and build series from episodes that already worked.** Basis: YouTube's own tips for casual and regular viewers (YouTube Help 13615784).
7. **After a missed fortnight, publish the next episode on its normal date and leave the gap.** Basis: Beaupré disputed that channels are penalised for breaks (SEJ 2024, the article's paraphrase; "penalty box" is SEJ's term); repeated gaps of 14+ days are associated with fewer views per video in vendor data (AIR, 8 Jun 2026, correlational, larger channels), so gaps are counted at each checkpoint. **(his rule:** no catch-up doubles; two episodes in one week break the 5–7 hour budget that A9's "cut the load" verdict protects**)**
8. **Do not rely on subscribers to deliver an episode.** No subscribe appeals as a reach strategy. Basis: the suggested list is the top place subscribers watch, and Beaupré put the subscribers-row CTR at around a tenth or less (PPC Land 2026, hedged, no sample). **(his rule** for subscribe appeals**)**

### Instagram · the rented shop window

**What it rewards.** Watch time, likes and sends; Reels and Explore for non-followers, Feed and Stories for followers; original material only for recommendations. Basis: Instagram Ranking Explained (2023); Mosseri (SMT, Jan 2025); Original content guidelines (2026).

1. **Use Reels for strangers, carousels and feed posts for followers, Stories for followers only.** Basis: Reels and Explore mostly show accounts the viewer does not follow; Stories show people the viewer follows; carousels get a second pass at followers who swiped by (Instagram 2023; Mosseri via Haberman).
2. **Post only material he shot or made, never another app's export with its watermark, and never a repost of someone else's clip.** Basis: unoriginal content (reposts, screenshots, watermarks, speed changes, credit-only edits) can remove an account from recommendations to new audiences, regained only when most posts over 30 days are original (Original content guidelines; Instagram, 30 Apr 2026); watermarked Reels get less distribution (Instagram 2023).
3. **Build each Reel's first three seconds as its opener, and judge Reels on skip rate and sends per reach before likes.** Basis: skip rate is the share of views skipped in the first three seconds (SMT, Aug 2025); sends weigh slightly more for unconnected content (Mosseri, Jan 2025).
4. **Test risky openers as Trial Reels, with auto-share on.** Basis: shown to non-followers first, hidden from followers' Feed and Reels tab, metrics after about 24 hours, automatic sharing on 72-hour views (Meta, Dec 2024, updated Jun 2025). Available from 1,000 followers on a public account (Mosseri via SMT, Jul 2025); below that, post the opener as an ordinary Reel.
5. **Route anyone leaving Instagram through the bio link; use Story link stickers for followers only.** Basis: no caption links; Story links reach followers only (SMT, Nov 2024).
6. **If non-follower views fall to near zero across a month of original posts, open Account Status before changing anything else.** Basis: Account Status shows recommendation eligibility and allows appeal (Instagram 2023; Instagram, 30 Apr 2026). **(his rule** for the trigger**)**
7. **Feed post count is set by A2's hours.** What the data says if hours allow: within-account weekly follower growth +0.12% at 1–2 posts a week, +0.26% at 3–5 (Buffer, Aug 2025, vendor, not size-segmented).

### Substack and own site · the owned archive

**What it rewards.** Nothing algorithmic once a reader is on the list; on the way in, the platform's recommendation network. Basis: Substack Support; On Substack (Feb 2024); beehiiv (Jan 2026).

1. **Export the subscriber list on every A9 checkpoint date and keep the file outside Substack.** Basis: Substack says the writer can export at any time (Substack Support). **(his rule** for the schedule**)**
2. **Turn on Substack recommendations and recommend a small number of publications he actually reads.** Basis: recommendations plus the app drove 50% of new subscriptions network-wide (On Substack, Feb 2024); on beehiiv, publications that recommend others are 32 times more likely to be recommended back (beehiiv, Jan 2026, platform-published).
3. **Send paid-tier offers as web and email links.** Basis: app-store purchases keep the billing relationship with Apple and cost 30% in the first year; web checkout inside the iOS app is shown only to US readers, so a reader in Portugal subscribing in the iOS app sees only in-app purchase, while desktop, mobile-web and email-link subscriptions are unaffected (Substack IAP FAQ, Aug 2025).
4. **Read clicks, replies and unsubscribes; do not make a decision on open rate.** Basis: Apple's Mail Privacy Protection loads content in the background (Apple); beehiiv and GetResponse both say opens became less reliable.
5. **Do not plan on Notes for paying readers.** Basis: one documented case, a viral Note with 378 free and no paid subscribers (Amy Suto, Jul 2026, anecdote).
6. **Keep the own site as the archive and the canonical link; do not budget hours for search discovery.** Basis: position-1 click-through down 58% where AI Overviews appear (Ahrefs, Feb 2026, vendor); embeds count as External traffic in YouTube (YouTube Help 1714921).

## Deliverable 2 · Metrics sheet

**How to use it.** Menu names are given at section level because the apps rename them (§2.2). Every metric is read once per quarter, on A9's checkpoint dates (2 Feb, 4 May, 3 Aug, 2 Nov 2027; 1 Feb, 2 May, 1 Aug, 31 Oct 2028 if upload one lands in the week of 3 November 2026), in one sitting, and written into the record with the definition in force that day. Between checkpoints nothing is opened; that follows A9's distancing rule. Each row says what the number measures, the reference value if one exists, its source and label, and which decision it feeds. "Own baseline" means no sourced benchmark exists: the first reading is recorded and later readings are judged by direction only. "A9 row n" means the benchmark sits in A9's expectation sheet.

### YouTube (Studio, desktop)

| # | Metric · where | What it measures | Reference | Source · label | Read on | Feeds |
|---|---|---|---|---|---|---|
| Y1 | Impressions CTR, per upload, by traffic source · video analytics, Reach tab | Share of impressions on YouTube that became views; excludes external sites and end screens | Half of channels and videos 2–10%; wider in week one and under 100 views (A9 row 2) | YouTube Help 7628154 · platform-official, context only | Uploads ≥7 days old | A9 "change format" verdict; playbook YouTube 4 |
| Y2 | Test & Compare result per upload · video details page | Which title or thumbnail won on watch time share | Winner, or inconclusive (first variant kept) | YouTube Help 16391400 · platform-official | Every checkpoint (tests completed that quarter; YouTube applies the winner automatically) | Packaging record for the next episode |
| Y3 | Average percentage viewed and average view duration · video analytics, Engagement tab | Share of the video watched on average | vidIQ bands by length (A9 row 3) | vidIQ, 21 Jul 2026 · vendor heuristic, no sample | Uploads ≥7 days old | A9 "change format" verdict |
| Y4 | Intro (share still watching at 30 s) and typical retention · video analytics, key moments for audience retention | Whether the opening delivers the promise; this video against his 10 latest of similar length | Own baseline; Studio's own comparison line | YouTube Help 9314415 · platform-official | Uploads with ≥100 views | Playbook YouTube 2 |
| Y5 | Traffic source split, channel and per upload · channel and video analytics, traffic source report | Share of views from Browse, Suggested, Search, External, Notifications, Shorts, other | Own baseline (no small long-form split exists); Metricool sample-wide split for context only | YouTube Help 1714921; Metricool, 29 Jul 2026 · vendor, Shorts-heavy | Every checkpoint | Playbook YouTube 1 (which door each episode used) |
| Y6 | 30-day views per upload; best upload so far · channel analytics, Content | Per-video reach | A9 row 1 | vidIQ, 28 Jul 2026 · vendor, survivor sample | Uploads ≥30 days old | A9 quarterly reads |
| Y7 | Back-catalogue share: views in the last 28 days on uploads published 90+ days earlier, divided by all channel views in those 28 days · channel analytics, Content, sorted by publish date (his calculation) | Whether long-form is compounding on his channel | Own baseline; no sourced benchmark | Mechanism: SEJ 2024; PPC Land 2026 · size unmeasured | From the second checkpoint (first uploads past 90 days) | Whether to keep investing in search-shaped episodes |
| Y8 | Qualified public watch hours, last 365 days · Studio, Earn section | Progress toward the Partner Program | 8,000 hours for new applicants from 1 Feb 2027 (A9 row 11) | YouTube Help 72851, 12843009 · platform-official | Every checkpoint | A9 checkpoint reads |
| Y9 | Regular and casual viewers · channel analytics, Audience tab | Viewers returning in more than six (regular) or one to five (casual) months of the past year; does not affect reach | Own baseline; zero before month six by definition (A9 row 4) | YouTube Help 10246996 · platform-official | From the third checkpoint | Format consistency (playbook YouTube 6) |
| Y10 | Subscribers, total and net per quarter · channel analytics, Overview | Lagging stock of past reach | A9 rows 5–8 | vidIQ; Metricool · vendor, correlational | Every checkpoint | A9 verdicts (not a stop ground before quarter 8) |

### Instagram (Insights, app)

| # | Metric · where | What it measures | Reference | Source · label | Read on | Feeds |
|---|---|---|---|---|---|---|
| I1 | Views per post, split Followers / Non-followers · post insights | Reach to strangers against reach to followers; counts repeat views | Brand accounts at 1–5K followers: Reels 580, carousels 993, images 417 views per post (2025); no personal-account benchmark | Socialinsider, upd. 22 Oct 2026 · vendor, brand data | Every checkpoint | Playbook Instagram 1 and 6 |
| I2 | Skip rate, per Reel · Reel insights | Share of views skipped in the first three seconds | Own baseline; no benchmark | Instagram via SMT, 24 Aug 2025 · platform metric | Every checkpoint | Playbook Instagram 3 |
| I3 | Sends per reach, per Reel (sends ÷ accounts reached) · post insights (his calculation) | The signal Mosseri says weighs slightly more for non-followers | Own baseline; no benchmark | Mosseri via SMT, 22 Jan 2025 · executive statement | Every checkpoint | Playbook Instagram 3 |
| I4 | Average watch time and retention chart, per Reel · Reel insights | How long strangers stay | Own baseline | Mosseri via SMT, 22 Jan 2025; SMT, 24 Aug 2025 | Every checkpoint | Opener and length of the next Reels |
| I5 | Trial Reel results at 24 hours, and whether auto-share fired · Reel insights | How an opener does with non-followers only | Own baseline | Meta, Dec 2024 (upd. Jun 2025) · platform-official | Every checkpoint | Playbook Instagram 4 |
| I6 | Likes per reach, feed posts and carousels | The follower-side signal | Own baseline | Mosseri via SMT, 22 Jan 2025 | Every checkpoint | Follower-content mix |
| I7 | Follower growth, annualised · account insights, followers | Rented audience size | Brand accounts at 1–5K: 22.0% a year in 2025 (38.0% in 2024) | Socialinsider · vendor, brand data | Every checkpoint | A2 allocation review |
| I8 | Bio link taps · account insights, profile activity | Strangers and followers leaving for an owned channel | Own baseline; no benchmark found | — · unsourced, own data only | Every checkpoint | Whether Instagram feeds the list or YouTube |
| I9 | Account Status, recommendation eligibility · Account Status in settings | Whether posts can be shown to non-followers at all | Eligible | Instagram, 30 Apr 2026 · platform-official | When I1 non-follower views collapse | Playbook Instagram 6 |

### Email and own site (Substack dashboard; Search Console)

| # | Metric · where | What it measures | Reference | Source · label | Read on | Feeds |
|---|---|---|---|---|---|---|
| E1 | Subscribers, total and net per quarter · Substack dashboard, subscribers | Owned audience size | A9 row 13 | beehiiv; named cases · platform-published, anecdote | Every checkpoint | A9 checkpoint read 7 |
| E2 | Exported list on file · Substack subscriber export | Whether the owned asset is actually held | One file per quarter | Substack Support · platform-official | Every checkpoint | Playbook Substack 1 |
| E3 | Click rate per issue | Readers acting on an issue; a counted event | Vendor averages: 3.23% (beehiiv, 2025), 3.25% (GetResponse, 2023 data) | beehiiv, 6 Jan 2026; GetResponse 2024 · vendor, all senders | Every checkpoint | Issue format |
| E4 | Unsubscribe rate per issue | Readers leaving | Vendor average unsubscribe rate 0.15% (GetResponse, 2023 data; the page does not say how the rate is calculated) | GetResponse 2024 · vendor, all senders | Every checkpoint | Cadence and issue length |
| E5 | Open rate | Recorded, not used for decisions | 41.24% (beehiiv, 2025), made less reliable by Apple auto-opens | beehiiv; Apple MPP · vendor, platform-official | Recorded only | Nothing |
| E6 | New subscribers by source: Substack network (recommendations, app, Notes) against direct and external · Substack dashboard, Growth Sources tab (Substack sources incl. Notes and Recommendations; trackbacks; external) | How much of the owned list's growth is rented | Network-wide 50% from recommendations and app (Feb 2024); no per-writer benchmark | On Substack, 22 Feb 2024 · platform-official, network-wide | Every checkpoint | Playbook Substack 2 and 5 |
| E7 | Paid share of list, and share paid via Apple in-app purchase | Monetised share; portable share | A9 row 14 for paid share; in-app share own baseline | Substack IAP FAQ, 18 Aug 2025 · platform-official | Every checkpoint after a paid tier exists | Playbook Substack 3 |
| E8 | Own site: Google search clicks, and External views on embedded episodes · Search Console; YouTube traffic source report, External | Whether the archive sends anyone anywhere | Own baseline; position-1 CTR context in Ahrefs | Ahrefs, 4 Feb 2026 · vendor; YouTube Help 1714921 | Every checkpoint | Playbook own site 6 |

**What the sheet cannot tell him.** It has no row that turns an Instagram follower or a Substack recommendation into a YouTube viewer: no source found measures that conversion, and none of the platforms reports it. Whether one platform feeds another is read only from rows I8, E6 and Y5 (External), and only as direction.

## Sources

- Ahrefs, AI Overviews reduce clicks by 58%, 4 Feb 2026. https://ahrefs.com/blog/ai-overviews-reduce-clicks-update
- AIR Media-Tech, Does posting more on YouTube help? We studied 18,000 channels, 8 Jun 2026. https://air.io/en/audience-growth/does-posting-more-on-youtube-help-we-studied-18000-channels-to-find-out
- Apple, Mail Privacy Protection & Privacy, checked 28 Oct 2026. https://www.apple.com/legal/privacy/data/en/mail-privacy-protection/
- beehiiv, The State of Newsletters 2026, 6 Jan 2026. https://www.beehiiv.com/blog/beehiiv-the-state-of-newsletters-2026
- Buffer, How often to post on Instagram, 13 Aug 2025. https://buffer.com/library/how-often-to-post-on-instagram/
- Engadget, Meta is testing clickable links in Instagram captions for verified subscribers, 12 Mar 2026. https://engadget.com/social-media/meta-is-testing-clickable-links-in-instagram-captions-for-verified-subscribers-184555406.html
- GetResponse, Email Marketing Benchmarks (2024 edition, 2023 data), checked 28 Oct 2026. https://www.getresponse.com/resources/reports/email-marketing-benchmarks?web=1
- Instagram, Instagram Ranking Explained, updated 31 May 2023. https://about.instagram.com/blog/announcements/instagram-ranking-explained
- Instagram Creators, Original content guidelines, checked 28 Oct 2026. https://creators.instagram.com/original-content-guidelines/
- Instagram Creators, Rewarding original creators on Instagram, 30 Apr 2026. https://creators.instagram.com/blog/rewarding-original-creators-on-instagram
- Instagram Creators, Trial reels: try content with non-followers first, 10 Dec 2024. https://creators.instagram.com/blog/instagram-trial-reels
- Lia Haberman, ICYMI, The best Instagram content formats, 14 Oct 2025. https://liahaberman.substack.com/p/the-best-instagram-content-formats
- Meta, Test content with non-followers using trial reels, 10 Dec 2024, updated 26 Jun 2025. https://about.fb.com/news/2024/12/trial-reels-try-content-non-followers/
- Metricool, Mosseri shares updates to Instagram Insights, 14 Aug 2024. https://metricool.com/instagram-insights/
- Metricool, press release, Instagram Content Playbook (with HypeAuditor), 14 Oct 2025. https://metricool.com/press-release-instagram-content-playbook/
- Metricool, YouTube Trends 2026, 29 Jul 2026. https://metricool.com/youtube-trends/
- Net Influencer, Patreon State of Create 2025 summary, 21 Feb 2025. https://www.netinfluencer.com/patreon-2025-state-of-create-report-how-creators-are-breaking-free-from-platform-control/
- On Substack, Substack's recommendations network, 22 Feb 2024. https://on.substack.com/p/substacks-recommendations-network
- On Substack, In-app payments (IAP) FAQ, 18 Aug 2025. https://on.substack.com/p/in-app-payments-iap-faq
- PPC Land, Subscribers skip 90% of uploads in their feed, YouTube director says, 2 Sep 2026. https://ppc.land/subscribers-skip-90-of-uploads-in-their-feed-youtube-director-says/
- Search Engine Journal, YouTube algorithm myths debunked: insights from the growth team, 4 Mar 2024. https://www.searchenginejournal.com/youtube-algorithm-myths-debunked-insights-from-the-growth-team/510091/
- Social Media Today, Here's where each big social platform stands on external links, 25 Nov 2024. https://socialmediatoday.com/news/heres-each-big-social-platform-stand-external-links/733946/
- Social Media Today, Instagram updates metrics to focus creators on views, Aug 2024. https://socialmediatoday.com/news/instagram-updates-metrics-to-focus-creators-on-views/723645/
- Social Media Today, Instagram shares algorithm insights, 22 Jan 2025. https://www.socialmediatoday.com/news/instagram-shares-algorithm-insights-2025/738034/
- Social Media Today, Instagram expands access to trial reels, 13 Jul 2025. https://www.socialmediatoday.com/news/instagram-expands-access-trial-reels/752895/
- Social Media Today, Instagram adds retention insights for Reels, 24 Aug 2025. https://www.socialmediatoday.com/news/instagram-adds-retention-insights-reels/758464/
- Socialinsider, Instagram benchmarks, published 20 Feb 2026, updated 22 Oct 2026. https://www.socialinsider.io/instagram-benchmarks
- Substack Support, What happens to my email list for readers who read in the Substack app?, checked 28 Oct 2026. https://support.substack.com/hc/en-us/articles/4571360165396-What-happens-to-my-email-list-for-readers-who-read-in-the-Substack-app
- Suto, Amy, six-month Substack Notes experiment, 14 Jul 2026. https://www.amysuto.com/desk-of-amy-suto/substack-notes
- TechCrunch, Instagram gives creators more insight into their Reels performance, 29 Jan 2025. https://techcrunch.com/2025/01/29/instagram-gives-creators-more-insight-into-their-reels-performance
- vidIQ, Average view duration, updated 21 Jul 2026. https://vidiq.com/blog/post/average-view-duration/
- YouTube Help, A/B test titles & thumbnails (answer 16391400), checked 28 Oct 2026. https://support.google.com/youtube/answer/16391400?hl=en
- YouTube Help, How YouTube search works (answer 16090438), checked 28 Oct 2026. https://support.google.com/youtube/answer/16090438?hl=en
- YouTube Help, Impressions and click-through rate (answer 7628154), checked 28 Oct 2026. https://support.google.com/youtube/answer/7628154?hl=en-GB
- YouTube Help, Measure key moments for audience retention (answer 9314415), checked 28 Oct 2026. https://support.google.com/youtube/answer/9314415?hl=en
- YouTube Help, New, casual, & regular viewers tips (answer 13615784), checked 28 Oct 2026. https://support.google.com/youtube/answer/13615784?hl=en
- YouTube Help, Understand your YouTube video reach, Computer version (answer 1714921), checked 28 Oct 2026. https://support.google.com/youtube/answer/1714921?hl=en-GB
- YouTube Help, Understand new, casual, & regular viewers (answer 10246996), checked 28 Oct 2026. https://support.google.com/youtube/answer/10246996?hl=en
- YouTube Help, YouTube Partner Program overview & eligibility (answer 72851), checked 28 Oct 2026. https://support.google.com/youtube/answer/72851?hl=en
- YouTube Help, Changes to the YouTube Partner Program (answer 12843009), via A9, checked 28 Oct 2026. https://support.google.com/youtube/answer/12843009?hl=en
- YouTube Official Blog, post on Nielsen's streaming ranking and TV viewing, 20 Feb 2024. https://blog.youtube/news-and-events/youtube-number-one-streamer-nielsen/

## Writer's unsure list

Fresh check 28 Oct 2026 (Fable 5.1): fix · 1 error, 9 should-fix, 7 minor; all applied.

1. Studio and Instagram menu locations in the metrics sheet are given at section level from memory; not checked against the live apps. The Substack "subscriber sources" view in row E6 is the least certain.
2. Trial Reels eligibility: both official posts send readers to the Help Center, which was not opened; the 1,000-follower figure rests on Mosseri as reported by Social Media Today (Jul 2025). Settled by the fresh check.
3. Instagram's originality rule is dated to 2024 for Reels on the strength of the 30 Apr 2026 post only; the 2024 announcement was not opened.
4. That every view counts toward the Followers/Non-followers split comes from secondary reports (Social Media Today, Metricool, Aug 2024); no Instagram Help page found.
5. The 1 billion hours a day of TV viewing is YouTube's February 2024 figure; no newer official figure found.
6. The 50% of new Substack subscriptions from recommendations and the app dates from February 2024; no newer official split found.
7. Playbook rule on paid-tier offers: the IAP FAQ states web checkout in the iOS app is shown to US readers only. Settled by the fresh check.
8. The Ahrefs figures are vendor data from US-weighted Search Console data; nothing found for Portuguese-language queries.
9. Studio's typical-retention line also offers a comparison with "all YouTube videos of similar length"; not confirmed as available on a small channel.
10. Social Media Today, not Instagram, is the source for Story link stickers reaching only followers; Instagram's 2023 ranking page supports it only indirectly.

Erratum 12 Nov 2026, found by PB6's writer (public course PB, row W-PB6) and confirmed by its fresh checker: the YouTube Help page at answer 1714921 is titled "Understand your YouTube video reach" (Computer version); "Traffic sources" was a section of it (§1.1, Sources).

Erratum 12 Nov 2026, found by PB7's writer (public course PB, row W-PB7) and confirmed by its fresh checker: in August 2024 the followers and non-followers split of views and the removal of impressions from Insights were reported by Metricool as changes still to come, not made; Social Media Today does not mention them (§2.2).
