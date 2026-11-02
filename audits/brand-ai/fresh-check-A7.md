---
audit: fresh check
unit: A7 · Monetisation through Shōmen
course: brand-ai · A · Building a Marketable Personal Brand
model: Opus 5.5 (search on; a Fable 5.1 fresh check is owed, deferred by Pedro 31 Oct 2026 to the Fable stage)
date: 2026-11-02
chat: own Opus 5.5 agent context, not shown the writing (P31), in session https://claude.ai/code/session_01KMmgQzMxzB9yQae4ooCocp (backlog row A-2)
verdict: keep · 0 errors, 3 should-fix, 6 minor
---

**Fresh check of A7 · Monetisation through Shōmen (Brand + AI): verdict keep, no errors, 3 should-fix and 6 minor**

This was an Opus 5.5 fresh check, run on 2 November 2026. A Fable 5.1 fresh check of this unit is still owed. Pedro deferred it on 31 October 2026 to the Fable stage at the end of the queue.

## (1) Coverage
- The conversion numbers applied to 2027 audience sizes: **covered** (§1, both tables). The brief's 1–3% is split by how good its sources are, and the 0.4–1.2% merch rate is called weakly sourced each time it is used.
- Why under 10K followers a drop is a few orders, and what that means for inventory: **covered** (§2, four inventory rules).
- Seishin and Enkamp as proof that it exists, and why that is no template: **covered** (§3, four reasons).
- Sponsorship stories about the three SC Braga athletes through December 2027, told as episodes rather than adverts: **covered** (§4, Deliverable A part 2). They run on Shōmen's own Instagram rather than the channel, and the unit argues that from A3 §4.
- The override where Shōmen comes first and Instagram becomes home: **covered** (§5, Deliverable A part 7).
- From the brief's lead, "product placement that is just him wearing the gi": **covered** (Deliverable A part 1, first row).
- Deliverable (integration plan, plus a 2027 revenue model in three scenarios with the assumptions shown): **present in full**.

## (2)–(6) Findings

[should-fix] [attribution] Deliverable B, B1 row a4; Current: `VoxBooster, attributed there to Shopify / Fourthwall store analytics; weakly sourced.`; Problem: the page credits the $48.50 order value three different ways. Its table says "Shopify / Fourthwall Store Analytics", its text carries a "(Fanjoy)" citation next to the figure, and its methodology says "Fourthwall & Grand View Research". It links no study. Audit 1's erratum asked for the attribution to be given "variously"; this row gives one credit only; Fix: `VoxBooster, attributed there variously to Shopify / Fourthwall store analytics (table), Fanjoy (text) and Fourthwall & Grand View Research (methodology), with no study linked; weakly sourced.`; Basis: https://voxbooster.com/blog/merch-sales-creator-statistics-2026 (read 2 Nov 2026); audits/brand-ai/audit-1.html §5.

[should-fix] [accuracy] §4, "The platform mechanism…"; Current: `Instagram ranks Reels on watch time, likes and sends, with sends weighing slightly more for people who do not follow the account (Mosseri, as`; Problem: Social Media Today reports these as Instagram's top three ranking signals in general, not for Reels only. The source says sends are "slightly more important for unconnected content". Reading "unconnected" as "people who do not follow the account" is A6's interpretation (A6 §2.1 says so), and the unit states it as fact; Fix: `Instagram ranks content on watch time, likes and sends, with sends "slightly more important for unconnected content", which A6 reads as content shown to people who do not follow the account (Mosseri, as`; Basis: https://www.socialmediatoday.com/news/instagram-shares-algorithm-insights-2025/738034/ ; courses/brand-ai/A6-how-growth-works-per-platform.md §2.1.

[should-fix] [coverage] Deliverable A part 3 (pointer); Current: `- Thumbnails lead with the journey, never with Shōmen: A4 clause 5; A5 §4 rule 5.`; Problem: A4 clause 5 and A5 §4 rule 5 say a thumbnail leads with the journey and "never with a diagnosis, a crisis, a loss or a verdict". Neither says anything about Shōmen. "Never with Shōmen" is this unit's own rule credited to two other units; Fix: `- Thumbnails lead with the journey: A4 clause 5; A5 §4 rule 5. A Shōmen product appears on one only when it is in the frame used, and never leads it **(his rule)**.`; Basis: courses/brand-ai/A4-voice-disclosure-and-the-record.md (Deliverable A, clause 5); courses/brand-ai/A5-production-craft.md §4, rule 5.

[minor] [figure] §1, *Instagram followers*; Current: `at 22.0% a year they would start 2027 at about 820, 2,459 and 8,197 (my arithmetic)`; Problem: dividing by 1.22 treats 1,000 / 3,000 / 10,000 as end-of-2027 counts, but the table calls them "followers on drop day" (March and September). Also, Socialinsider's 22.0% is for the 1,000–5,000 tier, and the 10,000 case sits above it (A6 §2.3 gives 20.3% for 5,000–10,000); Fix: `at 22.0% a year, accounts that reached them by the end of 2027 would have started the year at about 820, 2,459 and 8,197 (my arithmetic; Socialinsider's 22.0% is the 1,000–5,000 tier, and the 10,000 case sits above it)`; Basis: courses/brand-ai/A6-how-growth-works-per-platform.md §2.3; recomputed in Python.

[minor] [coverage] Deliverable A part 2 (pointer); Current: `Each one is a carousel plus a Reel cut from the same material, made with B3 template 6 in both locked styles.`; Problem: B3 template 6 asks for on-image text for a 1:1 feed post and a 9:16 story, plus a caption and alt text. It does not produce a carousel or a Reel; Fix: `Each one is a carousel plus a Reel cut from the same material, with the on-image text, caption and alt text drafted from B3 template 6 (which asks for a 1:1 feed post and a 9:16 story) in both locked styles.`; Basis: courses/brand-ai/B3-prompting-that-holds-up.md, template 6.

[minor] [accuracy] §2, "The channel's 2027 audience…"; Current: `Shōmen sells karate gi and kumite apparel.`; Problem: the brief and the filed units say "a small karate-apparel brand" (the brief's lead also mentions him "wearing the gi"). "Kumite apparel" is a product-line detail no filed unit states. It is a fact about the business, not a personal one, so I graded it minor rather than error. It still goes beyond what the published units say; Fix: `Shōmen sells karate apparel.`; Basis: generator/data/brand-ai/units_data.py (preamble and A7 entry).

[minor] [coverage] Deliverable B, B1 row a14 (pointer); Current: `A9 row 11: 8,000 watch hours ≈ 72,700–100,000 views a year against first-ten medians of 180–272 per upload`; Problem: the first-ten medians are in A9 row 1, not row 11; Fix: `A9 row 11: 8,000 watch hours ≈ 72,700–100,000 views a year; A9 row 1: first-ten medians of 180–272 per upload`; Basis: courses/brand-ai/A9-what-to-expect-benchmarks.md, Deliverable 1.

[minor] [style] §5, "What decides it"; Current: `Shōmen's own conversion beats the top of the weakly sourced range twice running`; Problem: the trigger in Deliverable A part 7 and in the decision figure is "at least 1.20%", which reaches the top of the range rather than beating it; Fix: `Shōmen's own conversion reaches the top of the weakly sourced range twice running`; Basis: the unit's own Deliverable A part 7, trigger 1.

[minor] [deliverable] Deliverable A part 5; Current: `| S4 | Weeks over 7 publishing hours in the quarter, and how many of them were caused by Shōmen work | A9 read 2, with the cause noted |`; Problem: part 1 puts Shōmen's own work "outside the 5–7 hours", so S4 and trigger 2 need to say which Shōmen work can count against publishing hours. Otherwise the read is ambiguous when the deliverable is used on its own; Fix: `| S4 | Weeks over 7 publishing hours in the quarter, and how many of them went over because Shōmen work (a drop, its Story or email line, a Shōmen post) was done in publishing time | A9 read 2, with the cause noted |`; Basis: the unit's own Deliverable A part 1 (Shōmen's own Instagram row) and part 7, trigger 2.

**Errata applied (6).**
- Audit 1, VoxBooster attribution: applied for the conversion rate. §1 is more precise than the erratum (table "Spring Benchmark Studies / Linktree", text Linktree, methodology "Shopify & Linktree"; all confirmed on the page). It is only partly applied for the order value (finding a4 above).
- Audit 1, Teachery "per launch" → "per offer": applied ("per-offer course guidance").
- Audit 1, Enkamp "1.6M over ~fifteen years" cited to WKF: not repeated. The count is now cited to vidIQ (dated 27 Oct 2026) and no time span is claimed.
- Audit 1, Sacra 0.7% and the OpenSponsorship athlete: neither is used.
- Audit 2, A1-1 (@apcanario): consistent.

**Pointers to filed units.** All checked against the units and correct except the three findings above:
- A2 §3 quote "A7 applies them to Shōmen"; A2 Deliverable 2 (12.0 h of 10–14, up to 2.0 slack, no Shōmen line, Instagram 1.0 h, episode 8.0 h, 6.0 h a week, "Shōmen and brand contact", the $3,480 Ghost override); A2 §4; A2 §5 fees; A2 §1 Enkamp.
- A3 §3, §4 and §5: shifted review dates 16 Feb, 18 May, 17 Aug and 16 Nov 2027; Email 1 on Thu 5 Nov 2026; Week 2 Tue 10 Nov description change; Athens finale Tue 17 Nov 2026.
- A4 clauses 1, 2, 4 (question 4), 6, 7 and 10; record rules 4 and 5; the quotes "Every mention of Shōmen says it is my brand", "is spent or kept at the moment he recommends something he owns", "when recommending" and "The miss is always in".
- A5 §4 rule 6.
- A6 §2.1, §2.2 and §4; playbook rules Instagram 2, 4 and 5, YouTube 5, Substack 1 and 3; row E7; rows I1–I9; the closing note of Deliverable 2.
- A9 §1, §6 and §7 (including "the weakest sourced in the unit"); row 13; read 7 "orders per offer, if any offer ran"; the quarter-4 quote "no source found measures what moving platform does to a channel of this size"; the stop rule; the "cut the load" verdict.
- A1 description (794 characters) and bio (121): recounted by script. With the added lines they come to 865 and 134, as the unit says.
- B2 "Shōmen posts" row; B3 template 10's avoid line, quoted exactly; B5 step 7.

**Labels (4).** Vendor, correlational, anecdote, platform-claim and company-sponsored labels are present wherever needed.

**Deliverable (5).** Both deliverables are present in full and follow from the evidence. They are usable on their own once the S4 wording is fixed.

**Public-site check.** The unit names nothing about the three SC Braga athletes beyond their number and the sponsorship running through December 2027. It states no personal fact about Pedro beyond the brief and the filed units. The one product-line detail is the minor finding above.

## Confirmed
- Artificial Ignorance: 13,413 free and 121 paid on 1 January 2025; post dated 11 Feb 2025. https://www.ignorance.ai/p/two-years-of-artificial-ignorance
- beehiiv, 6 Jan 2026: Generalist World "43,000 newsletter subscribers and 700+ paying members"; median of 8,314 at the end of year one. https://www.beehiiv.com/blog/the-state-of-newsletters-2026.md
- Really Good Business Ideas, 4 Sep 2026: Substack's own "We tend to see 5-10%…", quoted exactly; the 3% median rests on a paywalled dataset. https://www.reallygoodbusinessideas.com/p/substack-average-paid-subscriber-conversion-rate
- Teachery: "about 2-3% of your email audience to purchase your mini-course", per offer, with no dataset. https://make500.teachery.co/lessons/part-2-managing-expectations
- VoxBooster, 22 Aug 2026: the quote about 0.40% to 1.20%; $48.50; no sample and no period stated; links go to homepages only; the rate attributions are exactly as §1 gives them. https://voxbooster.com/blog/merch-sales-creator-statistics-2026
- Net Influencer, 21 Feb 2025: $52 per fan and $110 per paying member; 1,000 creators and 2,000 fans via NewtonX, August 2024; "fan" is not defined; 24% of Instagram time. https://www.netinfluencer.com/patreon-2025-state-of-create-report-how-creators-are-breaking-free-from-platform-control/
- vidIQ, 11 Sep 2026: 12–51 band, 1,259,198 channels, 8.65%. https://vidiq.com/research/youtube-uploads-1000-subscribers/
- vidIQ, 20 Jul 2026: median of +0.5 subscribers a month in the 1–99 band. https://vidiq.com/research/youtube-subscriber-benchmarks-2026/
- The Introverted Networker: 2,500 over three years; charts as of 28 May 2025. https://theintrovertednetworker.substack.com/p/how-i-grew-my-newsletter-to-2500
- YouTube Partner Program from 1 February 2027: 1,000 subscribers plus 8,000 qualified watch hours in 365 days. Confirmed through PPC Land, which quotes the Help Center. https://ppc.land/new-youtube-creators-face-8-000-hour-bar-for-ad-revenue-from-february-2027/
- AIR Media-Tech: Health & Sport median RPM $1.23; 300 channels, May 2025 to May 2026; dated 1 Jul 2026. $89 for 72,700 views recomputed. https://air.io/en/air-data-findings/which-youtube-niche-makes-the-most-money-in-2026-ranked-by-real-rpm-and-cpm
- AIR Media-Tech, 28 May 2026: Shorts-share shift of more than 30 points, lower median subscribers, cause unresolved. https://air.io/en/audience-growth/do-youtube-shorts-help-your-long-form-videos-grow-data-from-18000-channels
- FeedSpot: Enkamp listed first; updated 2 Jul 2026; ranked by popularity. https://videos.feedspot.com/karate_youtube_channels/
- vidIQ: "1,670,000 subscribers as of 2026-10-27"; +20,000 between 2026-09-29 and 2026-10-26; page updated 28 Oct 2026. https://vidiq.com/youtube-stats/channel/@karatebyjesse/
- WKF, 17 Feb 2018: "the founder of the karate-gi brand Seishin International"; "gathered a massive online community of enthusiasts". https://www.wkf.net/news-center-new/meet-internet-sensation-and-karate-nerd-jesse-enkamp/670
- karatebyjesse.com: "I’m “The Karate Nerd” and founder of Seishin International"; the "Karate Gi" menu item links to the Seishin site; a 7-day email guide; training programmes on Gumroad (three of four). https://www.karatebyjesse.com/?page_id=2
- CreatorDB, 25 Jul 2026: "predominantly adult males across the US, UK, and beyond"; the demographic breakdown is behind a paywall. https://creatordb.app/creatorstats/karatebyjesse/
- YouTube Help 154235: the setting covers "branded content, sponsorships, endorsements, or other commercial relationships"; the label appears at the beginning of the video; nothing on a creator's own brand. Note: on 2 Nov 2026 the live page's title read "Add branded content restrictions & disclosure labels", while search results still show the title the unit lists. https://support.google.com/youtube/answer/154235?hl=en
- CAP/ASA guide: "promoting your own products/services … a clear and upfront disclosure is always necessary"; the CMA is named as a joint party. https://www.asa.org.uk/static/9cc1fb3f-1288-405d-af3468ff18277299/INFLUENCERGuidanceupdatev6HR.pdf
- Muhmin, Syah and Anggraeni, *Frontiers in Communication* 11, 5 Feb 2026: 407 responses; cross-sectional; expertise and trustworthiness predict the parasocial bond, which predicts purchase intention; the honesty item reads "when recommending". https://www.frontiersin.org/journals/communication/articles/10.3389/fcomm.2026.1723759/full
- Buffer, 13 Aug 2025: +0.12% and +0.26%; within-account fixed effects; feed posts only. https://buffer.com/library/how-often-to-post-on-instagram/
- Instagram Subscriptions: Portugal is listed in the 20 Sep 2023 update. https://creators.instagram.com/blog/bringing-subscriptions-to-more-creators-on-instagram
- YouTube Help 141805: "regardless of when that video was uploaded". https://support.google.com/youtube/answer/141805?hl=en
- Substack IAP FAQ, 18 Aug 2025: 30% in the first year. https://on.substack.com/p/in-app-payments-iap-faq
- Amy Suto, 4 Jul 2026: "the first 1,000 subscribers are the slowest". https://www.amysuto.com/desk-of-amy-suto/how-to-grow-a-substack
- All arithmetic, recomputed in Python: both §1 tables; 6,680–20,040; 285 and 421 days; list sizes 564, 1,354 and 5,628 at the 17 Aug review; every line of B2; T1–T3; 93% and 85%; $0.55 and $6.50 an hour; $1,300 and $14,630.
- All dates: every drop and instalment date is a Thursday in week B counted from A3's week A of 17 Nov 2026; 15 Feb 2028 is 16 Nov 2027 plus 91 days, a Tuesday.
- The unit's Sources list matches the URLs it cites exactly, both ways.
- Not checked, because no search of mine returned the page: Substack Support's fee page (a12; the unit cites it as A2 §5 gives it), Socialinsider benchmarks, The Creator's Playbook, AIR Media-Tech 8 Jun 2026, and Instagram Ranking Explained. Every figure the unit draws from these matches the filed unit that reports it.

## (7) Figures

1. **range, §1. PASS.** Labels "1,000 / 3,000 / 10,000 followers" and values 4–12, 12–36 and 40–120 trace to the rows `| 1,000 | 4 | 12 | $194–582 |`, `| 3,000 | 12 | 36 | $582–1,746 |` and `| 10,000 | 40 | 120 | $1,940–5,820 |`. The labels "0.40%" and "1.20%" trace to the column headers `Orders per drop at 0.40% | Orders per drop at 1.20%`. The caption names the section, the source (VoxBooster, 22 Aug 2026) and its weak sourcing. A low–high span per row fits the range kind.
2. **decision, Deliverable A part 7. PASS.** "at or above 1.20%" ← `orders were at least 1.20% of followers on drop day`. "3+ weeks over 7 h in each of two quarters" ← `three or more weeks went over 7 publishing hours`. "Median 30-day views rising" ← `The median 30-day views of the quarter's uploads did not rise`. Each outcome traces to the Outcomes list ("stock held to the last drop's sales"; "Stock for the next drop is set from the last drop's sales"; "Shōmen's appearances on @apcanario drop to the drop-day Story"; "The home becomes Shōmen's Instagram account"). The caption names the section, the sources of the thresholds, and 15 Feb 2028. A rule with branches fits the decision kind.
3. **bars (stacked), Deliverable B. PASS.** Values trace to `| Shōmen merch, gross sales | $388.00 | $2,328.00 | $11,640.00 |` and `| Paid tier, net of fees | $0.00 | $172.20 | $2,026.92 |`. The caption totals trace to `| **Total, 2027** | **$388.00** | **$2,500.20** | **$13,666.92** |`. The caption names the section and its sources. Numbers compared by scenario, split into parts, fit stacked bars.

**A7: verdict keep** (no errors). Severity counts: 0 error, 3 should-fix, 6 minor. The nine edits above are exact replacements and are still worth applying.
