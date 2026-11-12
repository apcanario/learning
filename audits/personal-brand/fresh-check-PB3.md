---
audit: fresh check
unit: PB3 · Audience and the two platforms
course: personal-brand · PB · Building a Personal Brand on Instagram and YouTube
model: Opus 5.5 (claude-opus-5-5, as the agent states; this session keeps no agent transcript on disk, so the model could not be confirmed from a transcript's "model" field; live search). A Fable 5.1 fresh check of PB3 is owed to the Fable stage (P49)
date: 2026-11-12
chat: own Opus 5.5 agent context, not shown the writing (P31), launched by the W-PB3 chat (which ran on Opus 5.5 and only staged, applied, filed and published; the same chat runs W-PB4) in session https://claude.ai/code/session_01KMmgR1EH9ai7ZGKeeFZHjN. The checker was first launched with its prompt's placeholder unfilled; the chat sent it the filled audit-units §3b prompt (saved in its folder) at its next tool round, before it reported
verdict: fix · 1 error, 5 should-fix, 6 minor
---

The checker's final report, verbatim, from its hand-back in the chat (its file write was refused by the harness, so it returned the report as text; the harness's indentation of the hand-back is removed). Saved before any finding was applied.

Model: claude-opus-5-5

# PB3 · Fresh check: Audience and the two platforms

The PB3 verdict is fix: 1 error, 5 should-fix and 6 minor. Each finding has exact replacement text below.

The report was not written to /tmp/pb3-check/out/report.md: the harness refused the file write ("Subagents should return findings as text"). This message is the whole report.

I checked the unit in an isolated context on 12 Nov 2026 with live search on, using only files in /tmp/pb3-check. I fetched only URLs that a WebSearch here returned word for word. The fetches went through a summarising reader, so "verbatim" below means verbatim as that reader reported it. I did not edit the unit.

## (1) Coverage

| Brief item | Status |
|---|---|
| Audience described by what it does and needs, not by demographics alone; how each trait is evidenced, with a label for each | Covered (§1, evidence table, four labels added) |
| Who uses Instagram and who uses YouTube, from the largest current surveys, dated | Covered for the US (Pew 2026) and the UK (Ofcom 2025, YouTube only). Thin for the EU: no survey was found, and the unit says so |
| What each platform does for a small account: discovery against depth, reach to followers and to non-followers, shelf life | Covered (§3 and the roles table) |
| What is and is not measured about short-form viewers becoming long-form viewers | Covered (§4) |
| The email list as the channel you own, with the conversion data that exists | Covered (§5). The legal question names no primary sources (see findings) |
| Hours split at 3, 6 and 10 hours a week, and what is cut first in a bad week | Covered (§6, D2) |
| Deliverable for Mara, then the template | Covered (D1, D2, T1, T2) |
| What it gives later units (PB4, PB6, PB7, PB9) | Covered |

## (2) Accuracy: sources opened

| Claim | Source | Verdict |
|---|---|---|
| Pew 2026: survey NPORS, 5,511 adults, fieldwork 30 Jan–18 Jun 2026, margin ±1.8; all 22 cells of the §2 table | Pew fact sheet, 19 Oct 2026 | PASS |
| Derived figures: 13 and 17 points; 41 against 85 read as "about half" | Pew | PASS |
| Ofcom: "used by 94% of adults"; 51 minutes; 10 Dec 2025; no Instagram figure; no panel named | Ofcom | PASS |
| Instagram's own account of its surfaces (Feed, Stories, Explore, Reels); the four Reels headings; no age or gender signal | Instagram, 31 May 2023 | PASS. One quotation is inexact: the source says "roughly in order of importance" (minor) |
| Mosseri's two quotations | Social Media Today, 22 Jan 2025 | PASS |
| Trial reels: shown to non-followers first; metrics about 24 hours later; dates; eligibility left to the Help Centre | Meta newsroom | PASS. "Globally available to all eligible creators" was a forecast ("in the coming weeks") and the unit states it as fact (minor) |
| TechCrunch paraphrase | TechCrunch, 30 Apr 2024 | PASS, and no spokesperson is quoted. Instagram's own post exists (Instagram for Creators, "Helping Creators Find New Audiences", 30 Apr 2024) and should be cited instead (should-fix) |
| Beaupré's title, quotations, the 1 Sep 2026 interview, the first-hour context | PPC Land, 2 Sep 2026 | PASS on the quotations. The page notes that the machine transcript misspells the participants' names. It does not say outright that the quotations come from auto-generated transcripts (minor) |
| Nine quotations | YouTube Help 16559651 | PASS |
| Five quotations | YouTube Help 141805 | PASS |
| Quotations | YouTube Help 14075157, 9101241, 9314416, 13615375 | PASS |
| Related-videos guide: dated 14 Jul 2026, gives no rate | YouTube Blog | PASS |
| Breakdowns "age, city, country, gender"; demographics "Not returned if the IG User has less than 100 followers" | Meta for Developers | PASS |
| All figures: more than 3M posts; 4.9, 3.5 and 2.6% reach; 0.51 and 0.34% interaction; 2.1 and 2.0% community reach; "nearly three times"; account count not stated; dates | Fanpage Karma | PASS |
| Socialinsider Reels study | Socialinsider | FAIL on the follower range. The source says "between 1K - 1M followers"; the unit says 1,000 to 100,000. All else PASS: 25,503,389 Reels, brand accounts, 2025, "golden window", the 45% sentence, the 40M/450K callout, dates |
| Sample of 799,718 videos and 71,177 accounts; peak in the first three days; about 83% of interactions in ten days; "keeps earning views for months"; 8,789 against 5,985; called correlation | Metricool | PASS |
| OverseerOS Shorts after 30 days | OverseerOS, 8 Nov 2026 | PASS on figures: 9,982 Shorts, 676 channels, about 8 days (median gap 7.9), 90.5%, median gain 57, "selected, not random". FAIL on one quotation: the source's sentence is "Among 1,546 Shorts starting below 1,000 views, none gained another 1,000 views during that interval." |
| OverseerOS: do Shorts hurt long-form views | OverseerOS, 1 Sep 2026 | PASS on 370 videos, 37 channels and the "no consistent evidence…" quotation. "cannot observe" is stretched: the source "cannot observe competitor impression allocation", which is not cross-format viewing |
| First 10 videos: 137,355 channels, 180 → 272 views; 367,243 channels, 1,362 → 1,344; quotation; no subscriber finding | vidIQ | PASS |
| Uploads study: 32,926,088 channels; 1.86, 8.65 and 30.77%; 360 days; both caveats | vidIQ | PASS |
| Posting-frequency study: 18,000 channels in four countries, 100K–1M monthly views; Home and DIY 114,000 subscribers (178 channels) against 90,700 (87); predictable-schedule finding; "went dark for 14+ days…"; "This is correlational data, not causal" | AIR Media-Tech, 8 Jun 2026 | PASS |
| Shorts study: 41, 39 and 37% ("at smaller sizes"); the Home and DIY sentence; 95,100/94,600 and 251,500/256,000; 0.04–0.5%; "measured subscriber counts, not cross-format viewing rates directly" | AIR Media-Tech, 28 May 2026 | PASS |
| Sherman paraphrased, with no direct quotation | Net Influencer, 23 May 2025 | PASS |
| 2.1M posts and 102K accounts; Stories excluded; fixed effects; the four growth bands; 12% reach; 3–5 posts a week recommended | Buffer, 13 Aug 2025 | PASS. The page itself is ambiguous on whether its percentages are points; the unit follows PB1's reading |
| 6 Jan 2026; 41.24%; 37.98 against 37.67%; 28B emails; 65,000+ newsletters; "auto-loads images"; bot filtering; "2.75x faster" | beehiiv State of Newsletters | PASS |
| Free plan: $0, up to 2,500 subscribers, landing pages, unlimited sends | beehiiv pricing | PASS at the search-returned URL pricing?via=start. pricing.md lists "Custom pages" and a website builder instead of landing pages. The plain URL the unit cites was not returned by search (unverifiable) |
| 39.64% open rate, 2023 data | GetResponse blog (search-returned) | PASS |
| 4.4 billion messages, 500-contact threshold, 10.76%, 0.7% and 39.93%, Mail Privacy Protection in 2021 | GetResponse report | Unverifiable: the cited URL (?frame=0) was not returned by search. The blog says "more than 4 billion" and gives no landing-page figure |
| 22 Feb 2024; 50% of new subscriptions and 25% of new paid ones | Substack | PASS |
| 2,003 consumers, 23–28 May 2024, 48%, 78% of buyers; no mid-century mention | Censuswide for uShip | PASS |
| 48% of the EU population in flats in 2024 | Eurostat | PASS |
| Two-thirds of US housing units had a garage or carport (Census 2021 data); about one third without is derived | US Department of Energy, Fact of the Week 1268 | PASS |
| 140M home-improvement projects, 50M DIY, 36% | Census/HUD infographic | PASS |
| 51% of YouTube users, 35% of adults, 4,594 adults, fieldwork dates | Pew 2018 | PASS |
| 20 channels, 441K to 1.5K; mid-century channel 4K (described as "MCM"); hand-tool channel 3.2K | FeedSpot | PASS |
| Lifespan figures | Measure Studio | Not checked (the unit does not use them) |

## (3) Figures: whose number

Every number has an owner (a source, "derived", or "Mara, fictional"). One gap: "frees up to 0.6 hours" is derived from the whole publishing-and-replies line (2.5 ÷ 4), which also covers scheduling and captions, and the unit does not show this (minor).

## (4) Labels

All present where needed. No finding.

## (5) Deliverable

D1, D2, T1 and T2 are present in full and can each be used on their own. They follow from §1–§6. The arithmetic checks out:
- Totals 11.75, 24.0 and 39.0, with every line consistent.
- 13, 26 and 52 videos a year, which is 1.1, 2.2 and 4.3 a month.
- 7.0 hours against 6 a fortnight.
- 0.14 points, about 0.2 followers.
- 1.0 hour freed.

One wording slip: "above the floor of 3" (minor, below).

## (6) Errata and pointers

- A2 fresh-check finding 19 (Mosseri, "unconnected content") is applied.
- A2 finding 10 (Substack's figure is platform-wide) is applied.
- The other A2 errata touch claims PB3 does not carry.
- Every pointer to PB1 and PB2 says what those units say:
  - PB1: §1 labels, §8 on hours, the D2 lines and the 150 USD cap, rows Y1/Y4/Y5/I4 and the stop rule, §1 on re-reading rows, D3 verdict 2, the Q1 review on 5 Apr 2027.
  - PB2: the D1 audience wording (verbatim), the §3 conventions, the profile link.

## (7) Figures (viz blocks)

1. **Grouped bars, §2.** Every value traces to the §2 table ("Ages 18–29 | 95% | 79%" … "All adults | 84% | 51%"). The caption names the section, source and sample. The kind fits. **PASS.**
2. **Compare, §3.** 4.9, 3.5 and 2.6 trace to "median reach was 4.9% of followers for Reels, 3.5% for image posts and 2.6% for carousels". Caption is complete; the kind fits. **PASS.**
3. **Stacked bars, D2.** Every value traces to the hours table. The caption names D2, PB1's D2 and the totals. The kind fits. **PASS.** Style note, not counted as a finding: Capture and Log share tone 1, so they cannot be told apart in the stack. Give Log an unused tone if viz.py has one; I did not check which tones it offers.
4. **Flow, D2.** Labels and notes trace to the numbered cut order. A flow fits a sequence. **FIX (minor):** the caption says "rests on §6", but YouTube Help 141805 and the shelf-life argument are in §3. Replacement caption: "D2's cut order (Mara, fictional). The order rests on §3 and §6: Buffer, 13 Aug 2025 (Instagram bands, within-account, vendor), AIR Media-Tech, 8 Jun 2026 (gaps of 14+ days, correlational, vendor), and YouTube Help answer 141805 (old videos keep being recommended). The hours freed are her planning estimates. The log is never cut."

## (8) The writer's source-errors list

- **beehiiv date, 5 Jan → 6 Jan 2026:** confirmed. The page says January 6, 2026; the metadata authors are Denk, Kanishka and Cromwell.
- **beehiiv 2024 open rate, 37.98% against 37.67%:** confirmed. The Key Takeaways give 37.98% and the comparison graphic 37.67%.
- **Patreon per-platform shares:** not checked here. PB3 does not use them; no action.
- **"No error found in the PB1/PB2 claims carried":** confirmed for every carried claim I re-opened (both vidIQ studies, Buffer, AIR Home and DIY, PB2's audience wording).

## (9) Sourcing standard, line by line

**Part 1, per claim**
- Sourced where made: met.
- Openable reference: met.
- The source says what the claim says: **not met**. Socialinsider's follower range (§3); OverseerOS "cannot observe" (§4).
- Reporter kept separate from the source: **not met**. §3 cites TechCrunch where Instagram's own post exists. PPC Land and Social Media Today are correctly framed as reporters.
- Each number says whose it is: met, with the small 0.6 h gap.
- A view is attached only to the person who holds it: met.
- Quotation marks hold exact words: **not met**. The OverseerOS 1,546 sentence (§3); Instagram's "in rough order of importance" (§1).
- Nothing invented: met.
- Figure captions: met, except figure 4 names the wrong section (minor).
- Object-relief rule: not applicable.

**Part 1, per unit**
- Unsourced claims are said to be unsourced or left out: met.
- Changeable facts dated: met.
- Sources list matches what is cited: met.
- Closing material agrees with the body: met.

**Part 5**
- Numbers, mechanisms and recommendations sourced: met.
- Acceptable source types: met.
- Anecdote, vendor and correlational labels: met.
- Platform named for growth, format and metric claims: met.
- Carried claims re-verified: met.
- No private-course reader or reference: met. I found no "A2" and no private-course terms in unit.md. I did not run kit/private_terms.py; it is not in this folder.
- Mara rules: met.
- Legal point given as a question with the primary source for the EU, the UK and the US, plus the "information, not legal advice" line: **partly met**. The question and the line are there; no primary source is named (should-fix).
- No uncited figures: met.
- Search dates: met.
- Deliverable built twice: met.
- Not advice without evidence: met.
- Links given as links: met.

## (10) Read as the persona; Mara against case-facts.md

**Persona.** No sentence assumes knowledge of the private course or its reader, and every pointer is to a PB unit. The audience evidence is mostly American, and the unit says so: US labels, no EU row, and T1 tells the reader to use their own country's largest survey. "Creator Insider" is named without being explained; this is not a finding.

**Mara.** All consistent with case-facts.md:
- The first use is labelled.
- Her age, job, niche, starting counts, phone and 6 hours match.
- PB1's D2 hours and cap, and the Q1 review date, match.
- PB2's restoration format, audience wording, account name and second repeat-back run match.

The one change to a registered fact is publishing and replies, from 1.5 to 1.25 hours a fortnight plus 0.25 for email. The writer's notes give the matching replacements for PB1 D2 and for case-facts.md. Both must be applied when PB3 is filed.

## Findings

- [error] [accuracy] §3 How long a post keeps working, Instagram
  - Current: "brand accounts with 1,000 to 100,000 followers"
  - Problem: the source's methodology says "between 1K - 1M followers".
  - Fix: "brand accounts with 1,000 to 1 million followers"
  - Basis: https://www.socialinsider.io/blog/how-long-does-it-take-for-reels-to-get-views/

- [should-fix] [attribution] §3 How long a post keeps working, YouTube Shorts
  - Current: "\"None of the 1,546 Shorts starting below 1,000 views gained another 1,000\""
  - Problem: these are not the source's words.
  - Fix: "\"Among 1,546 Shorts starting below 1,000 views, none gained another 1,000 views during that interval\""
  - Basis: https://www.overseeros.com/blog/do-youtube-shorts-get-views-after-30-days

- [should-fix] [accuracy] §4 What vendors measured
  - Current: "and says it \"cannot observe\" cross-format viewing"
  - Problem: the source "cannot observe competitor impression allocation", not cross-format viewing.
  - Fix: "and says it \"cannot observe competitor impression allocation\", because impressions are private Analytics data; it reports no cross-format viewing rate"
  - Basis: https://www.overseeros.com/blog/do-youtube-shorts-hurt-long-form-views

- [should-fix] [attribution] §3 Discovery, Instagram
  - Current: "TechCrunch reported in April 2024 that Instagram would show eligible content first to a small audience likely to enjoy it and widen distribution for what performs ([TechCrunch, 30 Apr 2024](https://techcrunch.com/2024/04/30/instagram-is-updating-its-ranking-systems-to-surface-more-content-from-smaller-original-creators)); the press's paraphrase, with no Instagram spokesperson quoted."
  - Problem: Instagram's own statement exists, so the unit should cite it rather than the reporter.
  - Fix: "Instagram said on 30 April 2024 that each eligible piece of content \"is shown to a small audience that we think will enjoy it\", and that \"the top performing set of reels are shown to a slightly wider audience\", then to a wider one again ([Instagram for Creators, Helping Creators Find New Audiences, 30 Apr 2024](https://creators.instagram.com/recommendations-and-originality)). Platform-official."
  - Basis: https://creators.instagram.com/recommendations-and-originality

- [should-fix] [attribution] Sources
  - Current: "- TechCrunch, \"Instagram is updating its ranking systems to surface more content from smaller, original creators\", 30 Apr 2024. https://techcrunch.com/2024/04/30/instagram-is-updating-its-ranking-systems-to-surface-more-content-from-smaller-original-creators"
  - Problem: follows from the finding above.
  - Fix: delete the line. After the line "- Instagram (Adam Mosseri), \"Instagram Ranking Explained\", 31 May 2023. https://about.instagram.com/blog/announcements/instagram-ranking-explained" insert "- Instagram for Creators, \"Helping Creators Find New Audiences\", 30 Apr 2024. https://creators.instagram.com/recommendations-and-originality"
  - Basis: as above.

- [should-fix] [coverage] §5 The rule that comes first
  - Current: "is a question PB8 answers with the primary sources."
  - Problem: Part 5 and the brief require the primary source to open for the EU, the UK and the US; none is named.
  - Fix: "is a question PB8 answers with the primary sources: for the EU, the General Data Protection Regulation (Regulation (EU) 2016/679, [EUR-Lex](https://eur-lex.europa.eu/eli/reg/2016/679/oj)); for the UK, the UK GDPR ([legislation.gov.uk](https://www.legislation.gov.uk/eur/2016/679/introduction)); for the US, the CAN-SPAM Act ([FTC, CAN-SPAM Act: A Compliance Guide for Business, Aug 2023, updated 22 Jul 2025](https://www.ftc.gov/business-guidance/resources/can-spam-act-compliance-guide-business))."
  - Basis: I opened the FTC and legislation.gov.uk pages on 12 Nov 2026. EUR-Lex refused the fetch, so the writer must open it before filing. The UK's e-marketing rules (PECR) are left to PB8.

- [minor] [attribution] §3 Discovery, YouTube
  - Current: "PPC Land notes the quotes come from auto-generated transcripts"
  - Problem: the page notes that the machine transcript misspells the participants' names; it does not say outright that the quotations come from it.
  - Fix: "PPC Land's text rests on the interview's machine transcript, which it notes misspells the participants' names"
  - Basis: https://ppc.land/subscribers-skip-90-of-uploads-in-their-feed-youtube-director-says/

- [minor] [attribution] §1 Why behaviour comes before demographics
  - Current: "\"in rough order of importance\""
  - Problem: the source says "roughly in order of importance".
  - Fix: "\"roughly in order of importance\""
  - Basis: https://about.instagram.com/blog/announcements/instagram-ranking-explained

- [minor] [accuracy] §3 Discovery, Instagram
  - Current: "Meta says they are \"globally available to all eligible creators\""
  - Problem: this was a December 2024 forecast ("in the coming weeks"), not a current statement.
  - Fix: "Meta said in December 2024 that they would be \"globally available to all eligible creators\" within weeks"
  - Basis: https://about.fb.com/news/2024/12/trial-reels-try-content-non-followers/

- [minor] [deliverable] D2, at 3 hours
  - Current: "above the floor of 3 in PB1's stop rule"
  - Problem: a quarter with 3 uploads is at the floor, not above it.
  - Fix: "at or above the floor of 3 in PB1's stop rule"
  - Basis: PB1 D3.

- [minor] [figure] D2 cut order, step 2
  - Current: "(frees up to 0.6 hours; nothing is lost)"
  - Problem: the derivation is not shown, and 0.6 is the whole line, which includes scheduling and captions.
  - Fix: "(frees up to 0.6 hours, derived: the week's whole publishing-and-replies line, 2.5 ÷ 4, so replies alone free less; nothing is lost)"
  - Basis: the D2 hours table.

- [minor] [figure] D2 cut-order figure caption
  - Current: "The order rests on §6:"
  - Problem: YouTube Help 141805 and the shelf-life argument are in §3.
  - Fix: "The order rests on §3 and §6:"
  - Basis: the unit's §3 and §6.

## Confirmed

Each was checked against its source and found right (details in section 2):
- Pew 2026 fact sheet: https://www.pewresearch.org/internet/fact-sheet/social-media/markdown
- Ofcom 2025: https://www.ofcom.org.uk/media-use-and-attitudes/online-habits/from-apps-to-ai-search-how-the-uk-goes-online-in-2025
- Instagram Ranking Explained: https://about.instagram.com/blog/announcements/instagram-ranking-explained
- Social Media Today on Mosseri: https://www.socialmediatoday.com/news/instagram-shares-algorithm-insights-2025/738034/
- Meta trial reels: https://about.fb.com/news/2024/12/trial-reels-try-content-non-followers/
- PPC Land quotations: https://ppc.land/subscribers-skip-90-of-uploads-in-their-feed-youtube-director-says/
- YouTube Help 16559651, 141805, 14075157, 9101241, 9314416, 13615375
- YouTube Blog related-videos guide: https://blog.youtube/creator-and-artist-stories/youtube-related-videos-traffic-guide/
- Meta for Developers insights reference: https://developers.facebook.com/docs/instagram-platform/api-reference/instagram-user/insights
- Fanpage Karma: https://www.fanpagekarma.com/insights/instagram-format-reach/
- Socialinsider, all except the follower range
- Metricool: https://metricool.com/youtube-trends/
- Both OverseerOS pages, figures only
- vidIQ First 10 and uploads studies
- Both AIR Media-Tech studies
- Net Influencer
- Buffer: https://buffer.com/library/how-often-to-post-on-instagram/
- beehiiv State of Newsletters 2026
- beehiiv Free plan, at pricing?via=start
- GetResponse 39.64%, from the blog
- Substack, 22 Feb 2024
- Censuswide for uShip
- Eurostat Housing in Europe 2025
- DOE Fact of the Week 1268
- AHS 2023 infographic
- Pew 2018
- FeedSpot
- The writer's unsure list, items 1–10: each matches its source as the writer describes it.

Unverifiable: the GetResponse report page (4.4 billion messages, 500 contacts, 10.76%, 0.7% and 39.93%). Not checked: the plain beehiiv pricing URL; Measure Studio.

PB3, verdict fix · 1 error, 5 should-fix, 6 minor
