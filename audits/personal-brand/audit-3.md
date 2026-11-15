---
audit: stratified-sample audit (Audit 3)
units: PB9, PB10, DD-PB1, DD-PB2
course: personal-brand · PB · Building a Personal Brand on Instagram and YouTube
model: Fable 5.2 (claude-fable-5-2; accepted by Pedro for row F-PB, 14 Nov 2026), search on
date: 2026-11-15
chat: one fresh Fable agent per unit, isolated on its packet, in session https://claude.ai/code/session_01KMmgQyNZfTSHF35S2ivXpn (row F-PB part 2; the four units' first runs, without web search, in session https://claude.ai/code/session_01KMmgQyKuvCKpHpSB9xzQYA, kept in `f-pb/<code>-run1-no-search/`)
verdicts: PB9 PASS · PB10 PASS · DD-PB1 PASS · DD-PB2 PASS
---

# Audit 3 · PB · PB9, PB10, DD-PB1, DD-PB2

Built by script (`f-pb/tools/build_audits.py`) from each agent's `out/audit.md`, saved verbatim under `audits/personal-brand/f-pb/<code>/` before any erratum was applied. Errata applied by `f-pb/tools/apply.py`; what was applied, held and flagged is in `f-pb/applied.json`.

---

<!-- PB9: f-pb/PB9/audit.md, verbatim -->

Model: claude-fable-5-2

# Stratified-sample audit · PB9 · Monetisation: what pays at each audience size (part 2)

Course PB, Audit 3. Date: 15 November 2026. Search: on. One unit, one fresh auditor; the unit was not edited.

## Provenance

- Auditor model: claude-fable-5-2. Folder `/home/claude/fpb/PB9`; `out/` was empty at the start (no resumed run).
- Read: `PROMPT.md`, `unit.md`, `brief.txt`, `sourcing-parts-1-and-5.md`, `case-facts.md`, `fresh-check-PB9.md` (to avoid re-reporting; none of its verdicts reused), `run1-audit.md`, `run1-errata.json`, `others/` for pointers only.
- Tools: Read, Write, Edit, Bash, WebSearch, WebFetch. No memory, past-chat, Projects, connector, Artifact, Agent or `mcp__` tool.
- Web rule: search first; fetch only a URL a search of this agent returned verbatim. At most 40 searches.

## Sample (copied unchanged from run 1 of 14 Nov 2026; recorded here before any check)

One claim per `##` section, 15 sections.

| # | Section | Sampled claim | Source cited |
|---|---|---|---|
| S1 | §1 The lines | YouTube fan funding at 500 subscribers and 3,000 watch hours; ad revenue share at 1,000 subscribers and, for new applicants from 1 Feb 2027, 8,000 watch hours | YouTube Help 12843009 |
| S2 | §2 Platform revenue share | vidIQ cohort of 137,355 new long-form channels, median about 272 views in 30 days on the tenth upload; exclusion sentence quoted | vidIQ, First 10 Videos Study |
| S3 | §3 Affiliate links | Amazon US fixed rates: 3.00% Toys, Furniture, Home, Home Improvement, Lawn & Garden (and Tools); 4.50% Physical Books, Kitchen, Automotive; 4.00% All Other | Amazon Associates statement |
| S4 | §4 Brand deals | Collabstr: "more than 21,000 collaborations" in 2025; average paid $255 YouTube, $193 Instagram; asking $311 and $214; "down 63% year over year from $418" | Collabstr 2026 report |
| S5 | §5 Own product | Gumroad "10% + $0.50" direct, 30% via marketplace, no monthly fee, "Gumroad is your merchant of record", taxes since 1 Jan 2025 | Gumroad, Pricing |
| S6 | §6 Paid membership | beehiiv: "The median paid conversion rate across beehiiv is 0.62%"; about 6 per 1,000; medians $10/month and $100/year; churn 5.06%–16.67% | beehiiv, State of Paid Newsletters 2026 |
| S7 | §7 Services and teaching | PB1's stop rule protects the long-form cadence (PB1, D3); PB3 D2 gives the 10-hour plan | others/PB1, others/PB3 |
| S8 | §8 Small-number events | NIST: Poisson models "the number of events occurring within a given time interval", mean λ, SD √λ; 5th–95th percentiles 0–5, 4–13, 16–32, 84–117 | NIST e-Handbook §1.3.6.6.19; arithmetic |
| S9 | §9 Fees | Stripe (Portugal): 1.5% + €0.25 standard EEA cards; 2.5% + €0.25 UK; 3.15% + €0.25 international; + 2% conversion | Stripe, Preços (Portugal) |
| S10 | §10 When to start | Step 1's pointers: PB8 D1 clause 7; register T1 before any income, A3 before a deal, E3–E4 before commercial email | others/PB8 |
| S11 | §11 Advert | Li, Gao, Gu and Leung: U-shape quote; 4,908 Australian influencers, 6,869 sponsored posts; low point 0.475 comments, 0.393 likes; Douyin 1,000, near 0.52 | JM record; accepted manuscript |
| S12 | Deliverable | D2 V17: CTT, Preços 2020, novembro/2020, Apartados, Singulares, concessão anual 58.00 € before VAT | CTT tariff PDF |
| S13 | Template | T1 points the Shopping row to answer 13376398 ("whether your country is listed"): the affiliate programme's 18 listed countries, Portugal absent, YPP required | YouTube Help 13376398 |
| S14 | Sources | Eisend, van Reijmersdal, Boerman and Tarrahi, Journal of Advertising 49(3), 344–366, 2020; "61 papers that use 57 distinct data sets" | WUR record |
| S15 | Unsure list | YouTube's 55%/45% shares are from its blog of 10 Aug 2026 | YouTube Official Blog |

**What this part did.** Run 1 (14 Nov 2026) opened no outside source. This part opened 34 of the unit's 35 sources (Gumroad's pricing page was never returned by search) plus two pages the unit does not cite (YouTube Help 72902; the PolyU repository record of the Li et al. file). 38 searches of the 40 allowed, 47 fetches, no call refused.

## Table (the sample)

| # | Section | Claim | Source | Verdict | Note |
|---|---|---|---|---|---|
| S1 | §1 | Fan funding at 500 subscribers + 3,000 hours; ad share at 1,000 + 8,000 hours for new applicants from 1 Feb 2027 | https://support.google.com/youtube/answer/12843009 | PASS | All six strings the unit quotes from this page are on it |
| S2 | §2 | vidIQ cohort 137,355 long-form channels; median about 272 views at 30 days on the tenth upload; exclusion sentence | https://vidiq.com/research/youtube-first-10-videos-study/ | PASS | 137,355; "272 on the tenth"; sentence exact; published 28 Jul 2026, updated 30 Jul 2026 |
| S3 | §3 | Amazon US 3.00% / 4.50% / 4.00% by category | https://affiliate-program.amazon.com/help/node/topic/GRXPHT8U84RAYDXZ?lang=en | PASS | Row strings exact; Tools is in the 3.00% band ("Outdoors, Tools, Sports"); no effective date |
| S4 | §4 | Collabstr: more than 21,000 collaborations; paid $255 / $193; asking $311 / $214; "down 63% ... from $418" | https://collabstr.com/2026-influencer-marketing-report | PASS | All figures and the 63% sentence as quoted; no page date; no follower breakdown |
| S5 | §5 | Gumroad 10% + $0.50, 30% via marketplace, no monthly fee, merchant of record, taxes since 1 Jan 2025 | https://gumroad.com/pricing | unverifiable | Four searches did not return the URL, so the web rule allowed no fetch |
| S6 | §6 | beehiiv median paid conversion 0.62%; about 6 per 1,000; $10 / $100; churn 5.06%–16.67% | https://www.beehiiv.com/blog/the-state-of-paid-newsletters-2026.md | PASS | Three quotations exact; 22 Jun 2026; churn 5.06% (Food & Drink) to 16.67% (Money) |
| S7 | §7 | PB1 stop rule protects the long-form cadence (PB1 D3); PB3 D2 gives the 10-hour plan | others/PB1, others/PB3 | PASS | PB1 D3 stop rule (fewer than 3 videos in each of two consecutive quarters); PB3 D2 allocation at 3, 6 and 10 hours |
| S8 | §8 | NIST: Poisson models "the number of events occurring within a given time interval"; mean λ, SD √λ; percentiles 0–5, 4–13, 16–32, 84–117 | https://itl.nist.gov/div898/handbook/eda/section3/eda366j.htm | PASS | Quotation exact, §1.3.6.6.19; percentiles recomputed |
| S9 | §9 | Stripe (Portugal) 1.5% + €0.25; 2.5% + €0.25 UK; 3.15% + €0.25 international; + 2% conversion | https://stripe.com/pt-PT/pricing | PASS | All four as shown (premium EEA cards 2.8% + €0.25 are not in the unit, which says "standard") |
| S10 | §10 | Step 1 pointers: PB8 D1 clause 7; register T1, A3, E3–E4 | others/PB8 | PASS | Clause 7, T1, A3 and E5 (needs E3 and E4) as described |
| S11 | §11 | Li, Gao, Gu and Leung: U-shape quotation; 4,908 Australian influencers, 6,869 posts; 0.475 comments, 0.393 likes; Douyin 1,000, near 0.52 | https://research.polyu.edu.hk/en/publications/endorsement-rate-in-influencer-marketing/ ; https://ira.lib.polyu.edu.hk/bitstream/10397/119670/1/Li_Endorsement_Rate_Influencer.pdf | PASS | Every figure and the quotation confirmed (Douyin 0.519). The label on the file and the mechanism sentence fail separately (attribution pass) |
| S12 | Deliverable | V17: CTT, Preços 2020, novembro/2020, Apartados, Singulares, concessão anual 58.00 € before VAT | https://www.ctt.pt/application/themes/pdfs/1_tarifario_servicos_postais_1nov.pdf | PASS | "Preços 2020", "novembro/2020", 58,00 €; footnote: prices subject to VAT. The unit itself grades it a stale 2020 tariff |
| S13 | Template | T1 sends the Shopping row to answer 13376398 for "whether your country is listed": 18 countries, Portugal absent, YPP required | https://support.google.com/youtube/answer/13376398?hl=en | PASS | 18 countries exactly as §2 lists them; Portugal absent |
| S14 | Sources | Eisend, van Reijmersdal, Boerman and Tarrahi, Journal of Advertising 49(3), 344–366, 2020; "61 papers that use 57 distinct data sets" | https://research.wur.nl/en/publications/a-meta-analysis-of-the-effects-of-disclosing-sponsored-content/ | PASS | Reference and quotation exact |
| S15 | Unsure list | YouTube 55%/45% revenue shares are from its blog of 10 Aug 2026 | https://blog.youtube/news-and-events/new-opportunities-to-earn-and-changes-to-the-youtube-partner-program/ | FAIL | The quotation is in the blog, but under "1. Premium Lite", as the split of the subscription pools; the blog states no ad share. Ad shares are on YouTube Help 72902. PB9-4 to PB9-7 |

## Attribution pass

Every quotation and every "X says / reports" in the unit, then every Sources title, each against its page. Items identical to a sampled claim (the vidIQ exclusion sentence, the Amazon rows, Collabstr's 63% sentence, the Gumroad quotations, the NIST quotation, the Eisend reference) are in the sample table and not repeated.

| # | Section | Quotation or attribution | Source | Verdict | Note |
|---|---|---|---|---|---|
| A1 | §2 | 12843009: "8,000 qualified watch hours in the last 365 days, or 20M qualified Shorts views in the last 90 days" | https://support.google.com/youtube/answer/12843009 | PASS |  |
| A2 | §2 | 12843009: "If you are already in YPP, your status is not impacted by this update" | https://support.google.com/youtube/answer/12843009 | PASS |  |
| A3 | §2 | 12843009: "review and accept the updated terms in YouTube Studio by January 31, 2027" | https://support.google.com/youtube/answer/12843009 | PASS |  |
| A4 | §2 | 12843009: "stop earning from the associated monetization features beginning February 1, 2027" | https://support.google.com/youtube/answer/12843009 | PASS |  |
| A5 | §2 | 12843009: "does not impact your channel’s status in the YouTube Partner Program" | https://support.google.com/youtube/answer/12843009 | PASS |  |
| A6 | §2 | 13429240: "with 4,000 qualified watch hours in the last 12 months" | https://support.google.com/youtube/answer/13429240 | PASS |  |
| A7 | §2 | 12843009: "500 subscribers and either 3,000 qualified watch hours in the last year or 3M qualified Shorts views in the last 90 days"; thresholds do not change | https://support.google.com/youtube/answer/12843009 | PASS | "There are no changes to the eligibility requirements for fan funding, YouTube Creator Partnerships, or YouTube Shopping" |
| A8 | §2 | 13429240: "3 valid public uploads in the last 90 days"; the five features named; Portugal listed | https://support.google.com/youtube/answer/13429240 | PASS |  |
| A9 | §2 | 12843009: "10M qualified Shorts views over the last 90 days"; missing it does not remove a channel or affect other earnings | https://support.google.com/youtube/answer/12843009 | PASS |  |
| A10 | §2 | YouTube's announcement "states the creator revenue share as" "55% for long-form videos and 45% for Shorts" | https://blog.youtube/news-and-events/new-opportunities-to-earn-and-changes-to-the-youtube-partner-program/ | FAIL | Words exact, attribution stretched: the sentence is about the Premium and Premium Lite pools. PB9-4 |
| A11 | §9 | Fee table: ad revenue creator share 55% long-form, 45% Shorts, sourced to the YouTube Official Blog | https://blog.youtube/news-and-events/new-opportunities-to-earn-and-changes-to-the-youtube-partner-program/ | FAIL | Figure right for ads (YouTube Help 72902), source wrong. PB9-5 |
| A12 | §2 | 7491256: "Creators get 70% of membership revenue after applicable taxes and fees are deducted"; "All transaction costs (including credit card fees) are currently covered by YouTube" | https://support.google.com/youtube/answer/7491256?hl=en | PASS |  |
| A13 | §2 | vidIQ: "aim for 40 to 55% viewed" for 5–15 minutes, published without a sample; updated 21 Jul 2026 | https://vidiq.com/blog/post/average-view-duration/ | PASS | "The ranges below are vidIQ guidance for target bands" |
| A14 | §2 | AIR Media-Tech "reports" median RPM $2.39 Crafting & Handmade, $2.98 Lifestyle; 300 channels, May 2025–May 2026; no home or DIY category; dated 1 Jul 2026 yet refers to September 2026 | https://air.io/en/air-data-findings/which-youtube-niche-makes-the-most-money-in-2026-ranked-by-real-rpm-and-cpm | PASS | Page says channels it "works with", not clients: PB9-15 (minor wording) |
| A15 | §2 | 13376398: "Every participating brand and retailer will set their commission rates and attribution window for each product" | https://support.google.com/youtube/answer/13376398?hl=en | PASS |  |
| A16 | §2 | Instagram's page names six earning tools and states no follower, age, country or account-type requirement | https://creators.instagram.com/earn-cash-making-what-you-love | PASS |  |
| A17 | §2 | Inro: "Meta's own documentation is not consistent on this and access appears to be invite-based and genuinely uneven"; "Meta takes 0% of subscription revenue"; "roughly 30% for a subscriber's first year"; cites no Meta page; updated 23 Jul 2026 | https://www.inro.social/blog/instagram-subscriptions | PASS |  |
| A18 | §2 | Meta for Creators: "10,000 followers or 250+ Return Viewers"; "50,000 Post Engagements" or "180,000 Watch Minutes" in the last 60 days; says nothing about Instagram | https://creators.facebook.com/tools/fan-subs | PASS | Instagram appears only in navigation links |
| A19 | §3 | EMARKETER reporting Agentio: more than 10,000 mostly US integrations, Oct 2023–Dec 2025; "affiliate link CTR reaches 1.8x the rate of the first integration" by the eighth; no base or purchase rate | https://www.emarketer.com/content/sticking-with-same-youtube-creator-nearly-doubles-affiliate-link-ctr | PASS |  |
| A20 | §3 | CMA: "Any form of incentive or reward – including money, commissions, discounts"; "It is not enough just to tag a brand in your post, use discount codes or affiliate links"; updated 3 Sep 2025 | https://www.gov.uk/government/publications/social-media-endorsements-guide-for-influencers/social-media-endorsements-being-transparent-with-your-followers | PASS |  |
| A21 | §3 | FTC: a disclosure "should be in the video and not just in the description"; Nov 2019, modified 3 Dec 2024 | https://ftc.gov/business-guidance/resources/disclosures-101-social-media-influencers/ | PASS | Body shows "November 2019"; metadata published 24 Oct 2019, modified 3 Dec 2024 |
| A22 | §4 | Collabstr blog: "Micro-influencers (10K–100K followers) average $198 per collaboration"; no figure for smaller accounts | https://collabstr.com/blog/influencer-costs-2025 | PASS |  |
| A23 | §4 | Influencer Marketing Hub "reports" 51.43% expansion intent for nano creators (42.86% + 8.57%); "600+"; nano not defined; 4 May 2026 | https://influencermarketinghub.com/influencer-marketing-benchmark-report/?facet1=pdf | PASS | Read at the ?facet1=pdf address search returned; the unit's ?bbpage=1 address was not returned |
| A24 | §4 | YouTube blog: "incentives for brand deals" for channels below its Shorts threshold; "We'll share more details soon" | https://blog.youtube/news-and-events/new-opportunities-to-earn-and-changes-to-the-youtube-partner-program/ | PASS | "For channels below the 10 million view threshold, these initiatives introduce new ways to earn" |
| A25 | §4 | Eisend et al.: the disclosure lowered brand attitudes and credibility | https://research.wur.nl/en/publications/a-meta-analysis-of-the-effects-of-disclosing-sponsored-content/ | PASS | "reduced brand attitudes, credibility, and source evaluation" |
| A26 | §5 | beehiiv Pricing: "Digital Products" on every plan; "beehiiv takes 0%"; "Stripe's standard processing fee of 2.9% + $0.30 per transaction"; Free $0 to 2,500; paid subscriptions from Lite, $49 a month yearly; merchant of record not stated | https://www.beehiiv.com/pricing | PASS | "at 1,000 subscribers" sits in a selector and could not be read as text |
| A27 | §5 | Etsy: "$0.20 Listing fee"; "6.5 % Transaction fee" on the sale price including the shipping you set; "3% + $0.25 payment processing fee"; varies by bank country | https://etsy.com/sell | PASS | Read at etsy.com/sell, the address search returned (unit: www.etsy.com/sell) |
| A28 | §5 | European Commission: since 1 July 2021, One Stop Shop; EU-wide threshold of EUR 10,000 | https://vat-one-stop-shop.ec.europa.eu/index_en? | PASS | "From 1 July 2021, the VAT rules on cross-border business-to-consumer (B2C) e-commerce activities changed"; "a new EU-wide threshold of EUR 10 000" |
| A29 | §5 | GOV.UK: "The place of supply of cross-border digital services is the consumer's location"; updated 28 Mar 2022 | https://www.gov.uk/guidance/the-vat-rules-if-you-supply-digital-services-to-private-consumers | PASS | HMRC page; exact apart from the apostrophe glyph |
| A30 | §6 | beehiiv: "first-party data from thousands of publications on beehiiv, analyzed across the 2021-2026 period"; publications that chose to charge; conversion not formally defined | https://www.beehiiv.com/blog/the-state-of-paid-newsletters-2026.md | PASS | "no breakdown by list size" holds for conversion only: PB9-14 (minor wording) |
| A31 | §6 | Artificial Ignorance: 13,413 free and 121 paid subscribers on 1 January 2025; post of 11 Feb 2025 | https://www.ignorance.ai/p/two-years-of-artificial-ignorance | PASS |  |
| A32 | §6 | beehiiv describes Generalist World as "a living community of 43,000 newsletter subscribers and 700+ paying members"; 6 Jan 2026 | https://www.beehiiv.com/blog/the-state-of-newsletters-2026.md | PASS |  |
| A33 | §6 | Patreon's own article gives none of the State of Create figures other summaries quote; 19 Feb 2025 | https://news.patreon.com/articles/state-of-create | PASS | Only "almost 90%" would recommend being a creator; it links to the full report, which this audit did not open either |
| A34 | §6 | Kit: "completely free for up to 10,000 subscribers"; "Unlimited digital products and subscriptions"; fee not stated; 23 Sep 2026 | https://intercom.help/convertkit/en/articles/9053602-the-kit-newsletter-plan | PASS |  |
| A35 | §6, §9 | Patreon Help: 10% for pages published after 4 Aug 2025; 3.4% + €0.35 for EUR payouts; 2.9% + $0.30 USD card; 2.5% currency conversion; Apple 30% on iOS | https://support.patreon.com/hc/en-us/articles/11111747095181-Creator-fees | PASS | The article names no monthly fee |
| A36 | §11 | Li et al. define endorsement rate as the share of sponsored posts among all posts before a given sponsored post | https://ira.lib.polyu.edu.hk/bitstream/10397/119670/1/Li_Endorsement_Rate_Influencer.pdf | PASS | "the proportion of sponsored posts to total posts by the influencer prior to the focal sponsored post" |
| A37 | §11 | The turning points are cited from "the authors' accepted manuscript" (body, link text, Sources, Unsure list) | https://ira.lib.polyu.edu.hk/handle/10397/119670 | FAIL | The repository record lists the file as "Version of Record". PB9-9 to PB9-12 |
| A38 | §11 | "The authors attribute the U to two forces: a higher rate raises recognition of the brand and also suspicion of manipulative intent" | https://ira.lib.polyu.edu.hk/bitstream/10397/119670/1/Li_Endorsement_Rate_Influencer.pdf | FAIL | The first force is the influencer's perceived recognition by brands, not recognition of the brand. PB9-8 |
| A39 | §11 | Li et al.: two experiments with 168 and 208 participants; Instagram sample mean 83,782.6 followers, smallest 630; Douyin smallest 939; follower count a control | https://ira.lib.polyu.edu.hk/bitstream/10397/119670/1/Li_Endorsement_Rate_Influencer.pdf | PASS |  |
| A40 | §11 | An own product introduced as yours is an ad under the UK guide's rule for brands you own | https://www.gov.uk/government/publications/social-media-endorsements-guide-for-influencers/social-media-endorsements-being-transparent-with-your-followers | PASS | "you must make this known and clearly label these posts as ads" |

| # | Sources title as the unit gives it | Page | Verdict | Note |
|---|---|---|---|---|
| T1 | AIR Media-Tech, "Which YouTube niche makes the most money in 2026, ranked by real RPM and CPM", last updated 1 Jul 2026 | https://air.io/en/air-data-findings/which-youtube-niche-makes-the-most-money-in-2026-ranked-by-real-rpm-and-cpm | PASS |  |
| T2 | Amazon Associates, "Associates Program Standard Commission Income Statement" | https://affiliate-program.amazon.com/help/node/topic/GRXPHT8U84RAYDXZ?lang=en | PASS |  |
| T3 | Artificial Ignorance, "Two years of Artificial Ignorance", 11 Feb 2025 | https://www.ignorance.ai/p/two-years-of-artificial-ignorance | PASS |  |
| T4 | beehiiv, Pricing | https://www.beehiiv.com/pricing | PASS | Descriptive, not quoted |
| T5 | beehiiv, "The State of Newsletters 2026", 6 Jan 2026 | https://www.beehiiv.com/blog/the-state-of-newsletters-2026.md | PASS |  |
| T6 | beehiiv, "The State of Paid Newsletters 2026", 22 Jun 2026 | https://www.beehiiv.com/blog/the-state-of-paid-newsletters-2026.md | PASS |  |
| T7 | CMA, "Social media endorsements: guidance for content creators", updated 3 Sep 2025 | https://www.gov.uk/government/publications/social-media-endorsements-guide-for-influencers/social-media-endorsements-being-transparent-with-your-followers | PASS |  |
| T8 | Collabstr, "2026 Influencer Marketing Report" (2025 data) | https://collabstr.com/2026-influencer-marketing-report | FAIL | Page title: "Collabstr Annual Influencer Marketing Report 2026". PB9-13 |
| T9 | Collabstr, "What influencers really cost in 2026" | https://collabstr.com/blog/influencer-costs-2025 | PASS | First part of the full title |
| T10 | CTT, "Preços 2020", novembro/2020 | https://www.ctt.pt/application/themes/pdfs/1_tarifario_servicos_postais_1nov.pdf | PASS |  |
| T11 | EMARKETER, "Sticking with the same YouTube creator nearly doubles affiliate link CTR" (Agentio data) | https://www.emarketer.com/content/sticking-with-same-youtube-creator-nearly-doubles-affiliate-link-ctr | PASS |  |
| T12 | Etsy, "Sell on Etsy" | https://etsy.com/sell | PASS | Page title "How to sell on Etsy"; "Sell on Etsy" is on the page only as a link label. No erratum |
| T13 | European Commission, VAT One Stop Shop | https://vat-one-stop-shop.ec.europa.eu/index_en? | PASS |  |
| T14 | FTC, "Disclosures 101 for Social Media Influencers", Nov 2019, modified 3 Dec 2024 | https://ftc.gov/business-guidance/resources/disclosures-101-social-media-influencers/ | PASS |  |
| T15 | GOV.UK (HMRC), "VAT rules for supplies of digital services to consumers", updated 28 Mar 2022 | https://www.gov.uk/guidance/the-vat-rules-if-you-supply-digital-services-to-private-consumers | PASS |  |
| T16 | Gumroad, Pricing | https://gumroad.com/pricing | unverifiable | URL not returned by search |
| T17 | Influencer Marketing Hub, "Influencer Marketing Benchmark Report 2026", 4 May 2026 | https://influencermarketinghub.com/influencer-marketing-benchmark-report/?facet1=pdf | PASS |  |
| T18 | Inro, "Instagram Subscriptions: setup, cost and what you keep", updated 23 Jul 2026 | https://www.inro.social/blog/instagram-subscriptions | PASS |  |
| T19 | Instagram, "Monetize with Instagram" | https://creators.instagram.com/earn-cash-making-what-you-love | PASS | The label above the heading "Earn money by doing what you love" |
| T20 | Kit, "The Kit Newsletter plan", 23 Sep 2026 | https://intercom.help/convertkit/en/articles/9053602-the-kit-newsletter-plan | PASS |  |
| T21 | Li, Y., A. Gao, F. Gu and F. Leung, "Endorsement Rate in Influencer Marketing", Journal of Marketing, 2026, doi:10.1177/00222429261422744 | https://research.polyu.edu.hk/en/publications/endorsement-rate-in-influencer-marketing/ | PASS | Published 27 January 2026 |
| T22 | Meta for Creators, "Subscriptions" (Facebook) | https://creators.facebook.com/tools/fan-subs | PASS |  |
| T23 | NIST/SEMATECH, e-Handbook of Statistical Methods, §1.3.6.6.19, Poisson distribution | https://itl.nist.gov/div898/handbook/eda/section3/eda366j.htm | PASS |  |
| T24 | Patreon, "State of Create in 2025", 19 Feb 2025 | https://news.patreon.com/articles/state-of-create | PASS |  |
| T25 | Patreon Help, "Creator fees overview" | https://support.patreon.com/hc/en-us/articles/11111747095181-Creator-fees | PASS |  |
| T26 | Stripe, "Preços" (Portugal) | https://stripe.com/pt-PT/pricing | PASS | Page title "Preços e tarifas"; the cited word is its first |
| T27 | vidIQ, "YouTube average view duration: what is a good AVD?", updated 21 Jul 2026 | https://vidiq.com/blog/post/average-view-duration/ | PASS |  |
| T28 | vidIQ Research, "YouTube First 10 Videos Study", 28 Jul 2026, updated 30 Jul 2026 | https://vidiq.com/research/youtube-first-10-videos-study/ | PASS | Heading: "YouTube First 10 Videos Study: Shorts vs Long-Form" |
| T29 | YouTube Help, "Analyze and manage your YouTube channel memberships program" (answer 7491256) | https://support.google.com/youtube/answer/7491256?hl=en | PASS |  |
| T30 | YouTube Help, "Changes to the YouTube Partner Program" (answer 12843009) | https://support.google.com/youtube/answer/12843009 | PASS |  |
| T31 | YouTube Help, "Overview of the expanded YouTube Partner Program" (answer 13429240) | https://support.google.com/youtube/answer/13429240 | PASS |  |
| T32 | YouTube Help, "YouTube Shopping affiliate program overview & eligibility" (answer 13376398) | https://support.google.com/youtube/answer/13376398?hl=en | PASS |  |
| T33 | YouTube Official Blog (The YouTube Team), "New opportunities to earn and changes to the YouTube Partner Program", 10 Aug 2026 | https://blog.youtube/news-and-events/new-opportunities-to-earn-and-changes-to-the-youtube-partner-program/ | PASS | Title, byline and date as cited |

The two remaining Sources lines are covered above: Eisend et al. (S14) and the Li et al. repository file (A37).

## Also checked (inside the folder, re-run in this part)

| # | Section | What | Verdict | Note |
|---|---|---|---|---|
| 1 | §2 | Views the thresholds mean: 87,273–120,000; 3,357–4,615 a video; 32,727–45,000; 1,259–1,731; 12 to 17 times 272; $208.58 | PASS | Recomputed |
| 2 | §3, §4, §6, §9 | USD 11.70; 418 to 255 is 39%; 0.90%; 1.63%; 1,613; €3.98; fees on USD 15 (2.00, 0.74, 1.88) | PASS | Recomputed |
| 3 | §8 | Poisson: empty months 31.2% and 74.7%; percentiles; 45.3%; 10.0% | PASS | Exact Poisson, λ of 8 and 2 sales over 209 days per month |
| 4 | §11 | One sponsored video in a season of six or seven is 14%–17% | PASS |  |
| 5 | Deliverable | D3: USD 13.00 a sale; totals 26.00 / 104.00 / 567.00; members 0.37, 1.35, 6.52, 2.48; per-hour figures; $588 | PASS | Recomputed |
| 6 | Deliverable | Weekdays of all dates; upload 12 on 8 Jun 2027, upload 14 on 6 Jul 2027; 209 days | PASS |  |
| 7 | Intro, Deliverable | Mara's facts against case-facts.md (PB9 block) | PASS | Guide, hours, dates, deals, address, scenario inputs agree |
| 8 | §2–§11, Deliverable | Pointers to PB1, PB3, PB4, PB5, PB6, PB7, PB8, PB10 used by the unit | PASS | Spot re-checked: PB1 D3, PB3 D2, PB8 clause 7 and register, PB10 §5 and D1; three frictions stay as flags PB9-1 to PB9-3 |

## Not checked

- https://gumroad.com/pricing: not returned by any of four searches, so the web rule allowed no fetch; its claims are unverifiable
- https://influencermarketinghub.com/influencer-marketing-benchmark-report/?bbpage=1: this exact address was not returned; the same report was read at the ?facet1=pdf address search returned
- https://www.etsy.com/sell: this exact address was not returned; the page was read at https://etsy.com/sell, which search returned
- https://ira.lib.polyu.edu.hk/bitstream/10397/119670/1/Li_Endorsement_Rate_Influencer.pdf: characters 100,000 to 112,144 of the PDF text were beyond the fetch window and not read
- https://www.beehiiv.com/pricing: the '1,000 subscribers' tier sits in a selector and could not be read as text
- kit/private_terms.py: not in the folder, not run
- No WebSearch or WebFetch call was refused for budget or permission. Two of the 40 searches were left unused.

## Failure rate

- Sample: 15 claims. PASS 13, FAIL 1, STALE 0, unverifiable 1. Failure rate 1 in 15 (6.7%; 1 in 14 of those that could be opened). Not more than one in ten, so the full-audit rule was not triggered.
- All claims checked: 96 (15 sampled, 40 attribution items, 33 Sources titles, 8 internal). PASS 88, FAIL 6, STALE 0, unverifiable 2.
- The six FAILs are four errors, one of them met in three places: the 55%/45% citation (S15, A10, A11), the Li et al. file label (A37), the Li et al. mechanism (A38), and one Sources title (T8). Attribution stratum alone: 5 FAIL in 73 items.
- Nothing is STALE: every dated platform figure opened on 15 Nov 2026 still reads as the unit gives it.

## Counts

- Words (`wc -w unit.md`): 8,974. `##` sections: 15.
- Cited claims in the whole unit: **94**, tallied again section by section in this part with run 1's rule (each sentence or table row resting a number, date, quotation, attribution or mechanism on an outside cited source, figures derived from one included; pointers to other units, `viz` blocks, Sources and the Unsure list not counted): §1 3 · §2 20 · §3 6 · §4 7 · §5 5 · §6 12 · §7 0 · §8 5 · §9 9 · §10 0 · §11 8 · Deliverable 19 (D2 9, D3 7, D4 1, D5 2) · Template 0 · Sources 0 · Unsure list 0.
- 35 sources listed; 34 opened.

## Figures

1. **flow, §1: PASS.** Labels and notes equal §1–§2; the thresholds in it were confirmed at answers 12843009 and 13429240.
2. **range, §8: PASS.** Lows, highs and points equal §8 item 3, recomputed.
3. **bars, D3: PASS.** 26.00, 104.00, 312.00, 255.00 and the caption totals equal D3.
4. **decision, D4: PASS.** Questions and outcomes equal §10 and D4's rule; the caption's "Li, Gao, Gu and Leung, Journal of Marketing, 2026" is right. It carries the one-labelled-piece limit that flag PB9-2 questions.

No figure erratum.

## Deliverable

- Exists in full (D1–D5, then template T1–T4 with every blank described), follows from the unit's evidence, and is usable by a reader who has the PB8 codes.
- None of the errata changes a number in it: D2 does not use the 55%/45% share, and V9, V13 and V17 were confirmed at Collabstr, beehiiv and CTT. V5 (Gumroad) could not be opened in this part.
- The three internal frictions of run 1 still hold and stay flags: PB9-1 (a deal's 2.0 hours come from a line PB10 §5 shows cannot give them), PB9-2 (the one-labelled-piece limit against counting her own product's mentions), PB9-3 (V6, R1 and R2 disagree on when her sales count replaces the illustration).

## Course goal and standard

- Goal: served. The unit gives PB10 its revenue rows and DD-PB2 its income lines, and sets every benchmark with its grade.
- Standard: claims are sourced where made, labels are present, dates are given, amounts stay in source currency, the tax point is a question with EU, UK and US sources. Three departures: a quotation cited for more than its passage says (PB9-4 to PB9-6), a mechanism the source does not state (PB9-8), a file described as an accepted manuscript when its record says Version of Record (PB9-9 to PB9-12).
- Advice without evidence: none found unlabelled.

## Verdict

**PASS**, with 12 errata and 3 flags. One sampled claim in 15 failed, so no full audit was run under the rule; in practice this part opened every source but one and checked every quotation. No section is named for rewrite. This report replaces run 1's "incomplete".

## Most consequential errors

1. §11 says a higher endorsement rate "raises recognition of the brand". The paper says it raises the audience's belief that the influencer is recognised by brands. The unit states the first of the study's two forces wrongly (PB9-8).
2. The 55%/45% creator share is cited to a blog sentence that is about Premium subscription pools. The figures are right for ads, but the page that states them is YouTube Help 72902, and the Unsure list wrongly says the Help Center does not give them (PB9-4 to PB9-7).
3. The Li et al. file is called the authors' accepted manuscript four times; the repository lists it as the Version of Record, so the unit's caution about it is unfounded (PB9-9 to PB9-12).

## Bibliography line

Add: YouTube Help, "YouTube partner earnings overview" (answer 72902), https://support.google.com/youtube/answer/72902?hl=en-EN . Correct: Collabstr's title ("Collabstr Annual Influencer Marketing Report 2026") and the Li et al. repository file (Version of Record, not accepted manuscript). Mark failed: none. Not opened: Gumroad, Pricing.

## Changelog line

2026-11-15 · PB9 · Audit 3 stratified sample, part 2 with search (claude-fable-5-2): PASS; 15 sampled, 13 PASS, 1 FAIL, 1 unverifiable (Gumroad); 96 claims checked in all, 6 FAIL, 0 STALE, 2 unverifiable; full attribution pass run; figures 4 of 4 pass; 12 errata (PB9-4 to PB9-15), 3 flags carried (PB9-1 to PB9-3).

## Errata

Run-1 errata re-verified: run 1 had no erratum and three flags. All three still hold against `unit.md` and `others/` as they now stand and are carried over with the same Current; none was dropped. Every Current below occurs exactly once in `unit.md` (`grep -c -F` prints 1) and sits on one line.

- **PB9-1** · flag · should-fix · other · Deliverable D2, row V10 (and D4, Brand deal row)
  - Current: `| V10 | Hours for one deal | — | — | 2.0 | Her estimate, from the publishing-and-replies line | None: her estimate |`
  - Fix: No replacement given: the cut that supplies a deal's 2.0 hours has to be decided (PB10 §5 took its own hour from the Instagram derivatives for the same reason). Not an erratum.
  - Basis: others/PB10 §5 ('Where the sixty minutes themselves come from'): the publishing-and-replies line is 1.25 hours a fortnight (three 15-minute reply slots plus 0.5 hours of scheduling, PB3, PB4 D1 E), and 'Taking 60 minutes from it would remove all three reply slots and half the scheduling, and scheduling cannot be skipped'. PB9 takes 2.0 hours from that line, which contradicts PB10 and fails PB9's own step 3 (hours from a named cut). No URL: internal. Re-verified 15 Nov 2026 against unit.md and others/ as they now stand: still holds.
- **PB9-2** · flag · minor · other · Deliverable D4, the rule
  - Current: `adds no more than one labelled piece per season to the account`
  - Fix: No replacement given: decide whether later mentions of the guide count against the one-piece limit, or state the limit as one sponsored piece plus her own product's mentions. Not an erratum.
  - Basis: unit §11 ('An own product introduced as yours is also an ad under the UK guide's rule ... so it is counted too') and others/PB8 D1 clause 7 ('Anything she sells herself is introduced as hers every time'): from Season 3 a season with one sponsored video and any video that names the guide holds two or more labelled pieces, above the limit D4 sets; D4's table counts only 'One "mine" mention per launch video'. No URL: internal. Re-verified 15 Nov 2026 against unit.md and others/ as they now stand: still holds.
- **PB9-3** · flag · minor · other · Deliverable D2, row V6 (against D5 R1)
  - Current: `replaced by her Gumroad count at the Q3 review`
  - Fix: No replacement given: D5 R1 (first read Q2, 5 Jul 2027) says it replaces V6, D5 R2 (first read Q3) also says it replaces V6, and V6 says Q3. One of the three has to change; PB10 D1 copies both first-read dates, so the choice touches PB10. Not an erratum.
  - Basis: unit D5 rows R1 and R2; others/PB10 D1 rows R1 ('From Q2') and R2 ('From Q3'), PB10 D4 (three guide sales read at Q2 under R1, 'R2 from Q3'). No URL: internal. Re-verified 15 Nov 2026 against unit.md and others/ as they now stand: still holds.
- **PB9-4** · erratum · should-fix · FAIL · §2 · YouTube, What the platform pays when you are in
  - Current: `YouTube's announcement of these changes states the creator revenue share as "55% for long-form videos and 45% for Shorts" ([YouTube Official Blog, The YouTube Team, 10 Aug 2026](https://blog.youtube/news-and-events/new-opportunities-to-earn-and-changes-to-the-youtube-partner-program/)).`
  - Fix: `For ads, YouTube says it will pay a partner "55% of net revenues from ads displayed or streamed on their public videos" on the watch page and, for Shorts, "45% of the revenue allocated to them" from the Creator Pool ([YouTube Help, YouTube partner earnings overview, answer 72902](https://support.google.com/youtube/answer/72902?hl=en-EN), checked 15 November 2026). YouTube's announcement of the 2027 changes gives the same split, "55% for long-form videos and 45% for Shorts", for what creators receive from the Premium and Premium Lite subscription pools; it states no ad revenue share ([YouTube Official Blog, The YouTube Team, 10 Aug 2026](https://blog.youtube/news-and-events/new-opportunities-to-earn-and-changes-to-the-youtube-partner-program/)).`
  - Basis: The blog sentence sits under the heading "1. Premium Lite": "This pool is distributed to creators based on member watch time and views, and from that distribution creators receive revenue share: 55% for long-form videos and 45% for Shorts"; the article states no watch-page ad share. https://blog.youtube/news-and-events/new-opportunities-to-earn-and-changes-to-the-youtube-partner-program/ . The ad shares are on YouTube Help 72902 (Watch Page Monetization Module, Shorts Monetization Module): https://support.google.com/youtube/answer/72902?hl=en-EN
- **PB9-5** · erratum · should-fix · FAIL · §9 · fee table, Ad revenue row
  - Current: `| Ad revenue | YouTube | Creator share 55% long-form, 45% Shorts | YouTube Official Blog, 10 Aug 2026 |`
  - Fix: `| Ad revenue | YouTube | Creator share 55% of net ad revenue on long-form watch pages; 45% of the Shorts revenue allocated to the creator | YouTube Help 72902 |`
  - Basis: As PB9-4: the blog gives 55%/45% for the subscription pools, not for ads; the ad shares are stated at https://support.google.com/youtube/answer/72902?hl=en-EN
- **PB9-6** · erratum · minor · FAIL · Unsure list
  - Current: `- YouTube's 55%/45% revenue shares are from its blog of 10 Aug 2026; the Help Center pages read did not state them (§2).`
  - Fix: `- YouTube's 55%/45% ad revenue shares are from YouTube Help answer 72902, opened 15 Nov 2026; its blog of 10 Aug 2026 gives the same split only for the Premium and Premium Lite subscription pools (§2, §9).`
  - Basis: As PB9-4. https://support.google.com/youtube/answer/72902?hl=en-EN ; https://blog.youtube/news-and-events/new-opportunities-to-earn-and-changes-to-the-youtube-partner-program/
- **PB9-7** · erratum · minor · other · Sources (entry to add for PB9-4 and PB9-5)
  - Current: `- YouTube Help, "Overview of the expanded YouTube Partner Program" (answer 13429240), checked 13 Nov 2026. https://support.google.com/youtube/answer/13429240`
  - Fix: `- YouTube Help, "Overview of the expanded YouTube Partner Program" (answer 13429240), checked 13 Nov 2026. https://support.google.com/youtube/answer/13429240` then on a new line `- YouTube Help, "YouTube partner earnings overview" (answer 72902), checked 15 Nov 2026. https://support.google.com/youtube/answer/72902?hl=en-EN`
  - Basis: Sourcing standard Part 1: every source cited is listed. Page title "YouTube partner earnings overview - YouTube Help": https://support.google.com/youtube/answer/72902?hl=en-EN . Apply only together with PB9-4 and PB9-5.
- **PB9-8** · erratum · error · FAIL · §11 · What the evidence on sponsorship load says
  - Current: `a higher rate raises recognition of the brand and also suspicion of manipulative intent`
  - Fix: `a higher rate raises the audience's belief that the influencer is recognised by brands (the paper's "perceived brand recognition") and also suspicion of manipulative intent`
  - Basis: The construct is about the influencer, not the sponsoring brand: the paper defines perceived brand recognition as "the extent to which consumers believe the influencer is acknowledged and validated in the brand marketplace" (Study 2 item: "The influencer has been recognized by brands within his/her domain"); the abstract says a higher endorsement rate enhances the influencer's "perceived brand recognition". https://ira.lib.polyu.edu.hk/bitstream/10397/119670/1/Li_Endorsement_Rate_Influencer.pdf ; https://research.polyu.edu.hk/en/publications/endorsement-rate-in-influencer-marketing/
- **PB9-9** · erratum · should-fix · FAIL · §11 · What the evidence on sponsorship load says
  - Current: `In the authors' accepted manuscript, the Instagram field study`
  - Fix: `In the full text held by the PolyU repository, which its record lists as the Version of Record, the Instagram field study`
  - Basis: The repository record gives the File Version as "Version of Record", open access, "© The Author(s) 2026", CC BY-NC 4.0; the PDF carries no accepted-manuscript statement. https://ira.lib.polyu.edu.hk/handle/10397/119670
- **PB9-10** · erratum · minor · FAIL · §11 · link text of the same citation
  - Current: `[Li et al., accepted manuscript, PolyU repository]`
  - Fix: `[Li et al., full text, PolyU repository]`
  - Basis: As PB9-9. https://ira.lib.polyu.edu.hk/handle/10397/119670
- **PB9-11** · erratum · minor · FAIL · Sources
  - Current: `- Li et al., accepted manuscript, PolyU Institutional Research Archive. https://ira.lib.polyu.edu.hk/bitstream/10397/119670/1/Li_Endorsement_Rate_Influencer.pdf`
  - Fix: `- Li et al., full text (Version of Record, open access), PolyU Institutional Research Archive. https://ira.lib.polyu.edu.hk/bitstream/10397/119670/1/Li_Endorsement_Rate_Influencer.pdf`
  - Basis: As PB9-9. https://ira.lib.polyu.edu.hk/handle/10397/119670
- **PB9-12** · erratum · minor · FAIL · Unsure list
  - Current: `- The endorsement-rate turning points (0.393–0.475 on Instagram) come from the authors' accepted manuscript in the PolyU repository, not the publisher's version (§11).`
  - Fix: `- The endorsement-rate turning points (0.393–0.475 on Instagram) were read in the copy in the PolyU repository, which its record lists as the Version of Record; the publisher's own page was not opened (§11).`
  - Basis: As PB9-9. https://ira.lib.polyu.edu.hk/handle/10397/119670
- **PB9-13** · erratum · minor · FAIL · Sources
  - Current: `- Collabstr, "2026 Influencer Marketing Report" (2025 data). https://collabstr.com/2026-influencer-marketing-report`
  - Fix: `- Collabstr, "Collabstr Annual Influencer Marketing Report 2026" (2025 data). https://collabstr.com/2026-influencer-marketing-report`
  - Basis: The page's title and first heading read "Collabstr Annual Influencer Marketing Report 2026"; the quoted title "2026 Influencer Marketing Report" does not appear on it. https://collabstr.com/2026-influencer-marketing-report
- **PB9-14** · erratum · minor · other · §6 · The share of a list that pays
  - Current: `no breakdown by list size, and "conversion" is not formally defined`
  - Fix: `no breakdown of conversion by list size (the report breaks prices and revenue projections down by list size, and conversion by industry only), and "conversion" is not formally defined`
  - Basis: The report has "Conversion Rate by Industry" and a table "Annual Revenue Projections by List Size", and says "Subscriber count doesn't meaningfully affect pricing for monthly and yearly tiers"; the unit's phrase is true of conversion only. https://www.beehiiv.com/blog/the-state-of-paid-newsletters-2026.md
- **PB9-15** · erratum · minor · other · §2 · What the ad line would pay once open
  - Current: `the channels are its clients, not a random sample`
  - Fix: `the channels are ones it works with, not a random sample`
  - Basis: The page describes the sample as "the real YouTube Analytics of 300 channels AIR Media-Tech works with"; it does not call them clients. https://air.io/en/air-data-findings/which-youtube-niche-makes-the-most-money-in-2026-ranked-by-real-rpm-and-cpm

---

<!-- PB10: f-pb/PB10/audit.md, verbatim -->

Model: claude-fable-5-2

# PB10 · Stratified-sample audit (course PB, Audit 3, part 2) · 15 November 2026 · search on

## Provenance

- Auditor: one fresh, isolated agent, model claude-fable-5-2. Read only `/home/claude/fpb/PB10`; wrote only `out/`. No memory, past-chat, Projects, connector, Artifact, Agent or `mcp__` tool used.
- Unit: `unit.md` (PB10; written 2026-11-13 by Opus 5.5; search flag off; Audit 4's seven replacements of 14 Nov 2026 applied). Not edited.
- `out/` was empty at the start: a first run of part 2, not a resumed one. The sample was written to `out/audit.md` and `out/sample.md` before any check.
- Part 2 of the audit of 14 Nov 2026 (`run1-audit.md`), which opened no outside source. The sample is run 1's, copied unchanged and not redrawn.
- Web: 31 searches (limit 40), 31 fetches, each of a URL a search in this agent returned verbatim. No call was refused.

## Sample (copied from run 1, recorded before any check)

| n | Section | Sampled claim | Source the unit cites |
|---|---|---|---|
| 1 | §1 | A 30-day view count needs an upload at least 30 days old (PB6 D2 YT2); click-through and percentage viewed need 7 days (YT3, YT4); an Instagram post is read once it is 7 days old (PB7 D2) | PB6 D2, PB7 D2 (`others/`) |
| 2 | §2 | YouTube counts qualified watch hours only from "long-form videos that you've set to public", not from private, unlisted or deleted videos or Shorts | YouTube Help 72851 |
| 3 | §3 | NIST's sample-size formula gives about 2,045 impressions to tell a true 2% from a hypothesised 3% (5% two-sided, 80% power), about 1,747 with 2% as the hypothesis; the continuity correction adds 100 | NIST/SEMATECH §7.2.4.2 |
| 4 | §4 | Buffer's I4 estimate (+0.26% weekly follower growth at 3–5 posts) is the difference from weeks with no posts: "points added to the weekly growth rate" | PB1 D1 I4, PB1 §3 (`others/`); Buffer behind it |
| 5 | §5 | Meta's developer reference: follower demographics are "Not returned if the IG User has less than 100 followers", and follows and unfollows likewise | Meta for Developers, Instagram account insights |
| 6 | §6 | Three a quarter is 12 a year, the floor of the 12–51 band; below it the base rate is 1.86% | PB1 D1 Y4 (`others/`) |
| 7 | §7 | Regression to the mean "happens when unusually large or small measurements tend to be followed by measurements that are closer to the mean" | Barnett, van der Pols, Dobson, IJE 34(1), 2005 |
| 8 | §8 | Of 1,000 US and UK creators surveyed, 52% reported burnout and 37% were considering leaving | PB1 §6, row B2 (`others/`) |
| 9 | §9 | In 2023 Google said it would delete accounts inactive for two years, and "We do not have plans to delete accounts with YouTube videos at this time" | TechCrunch, 18 May 2023 |
| 10 | Deliverable (D4) | Click-through under 2% with impressions below her median "is the case YouTube names for a title or thumbnail change" | PB1 D3; YouTube Help 16559651 |
| 11 | Deliverable (D5) | 68% of channels that crossed 1,000 had 40 or more videos; 53.5% had 70 or more; 91.35% of her band stay under 1,000 | PB1 D1 Y4, Y5 (`others/`) |
| 12 | Sources | Newman, "If almost nothing goes wrong, is almost everything all right? Interpreting small numerators", letter, JAMA 274(13), 4 Oct 1995, 1013, crediting Hanley and Lippman-Hand (JAMA, 1983); the 3/n rule | JAMA Network |
| – | Unsure list | No cited claim; nothing sampled | – |

## Table: the sample

| n | Section | Claim | Source | Verdict | Note |
|---|---|---|---|---|---|
| 1 | §1 | Qualifying ages: 30 days (YT2), 7 days (YT3, YT4), 7 days for an Instagram post | others/PB6 D2 YT2-YT4; others/PB7 D2 IG2-IG7 and D1 IR4 | PASS | PB6 D2: "uploads at least 30 days old", "at least 7 days old"; PB7 D2 rows: "posts at least 7 days old"; PB7 D1 IR4: "read once it is 7 days old". Internal pointer; no outside source |
| 2 | §2 | Watch hours only from "long-form videos that you've set to public"; not private, unlisted, deleted or Shorts | https://support.google.com/youtube/answer/72851?hl=en-GB | PASS | Page (title "The YouTube Partner Programme overview and eligibility"): "Qualified watch hours gained from long-form videos that you've set to public"; private, unlisted and deleted videos and Shorts listed as not counting |
| 3 | §3 | About 2,045 impressions (hypothesis 3%, true 2%), about 1,747 the other way; continuity correction adds 100 | https://itl.nist.gov/div898/handbook/prc/section2/prc242.htm | PASS | §7.2.4.2 "Sample sizes required" gives the two-sided formula with z(1-α/2) and z(1-β) over δ, and the correction N = N' + 1/δ (1/0.01 = 100). Recomputed: 2,044.6 and 1,746.9 |
| 4 | §4 | Buffer's I4 is an increment over weeks with no posts: "points added to the weekly growth rate" | others/PB1 §3; https://buffer.com/library/how-often-to-post-on-instagram/ | PASS | Quotation exact in PB1 §3. Buffer (13 Aug 2025, 2.1M posts, 102K accounts, fixed-effects): +0.12/+0.26/+0.44/+0.66%, "compared to weeks when users don't post at all", "an increase in follower growth rate" |
| 5 | §5 | "Not returned if the IG User has less than 100 followers"; follows and unfollows likewise | https://developers.facebook.com/docs/instagram-platform/api-reference/instagram-user/insights | PASS | Exact words on the page under follower_demographics and under follows_and_unfollows |
| 6 | §6 | Floor of the 12-51 band; below it 1.86% | others/PB1 D1 Y4; https://vidiq.com/research/youtube-uploads-1000-subscribers/ | PASS | vidIQ, 11 Sep 2026, 32,926,088 channels, 360 days: 0.20%, 1.86% (1-11), 8.65% (12-51), 30.77% (52+) |
| 7 | §7 | Regression to the mean "happens when unusually large or small measurements tend to be followed by measurements that are closer to the mean" | https://pubmed.ncbi.nlm.nih.gov/15333621/ | PASS | PubMed abstract: "It happens when unusually large or small measurements tend to be followed by measurements that are closer to the mean." Int J Epidemiol 2005, 34(1), 215-20 |
| 8 | §8 | 1,000 US and UK creators: 52% burnout, 37% considering leaving | others/PB1 D1 B2; https://billiondollarboy.com/news/over-half-of-creators-face-burnout | PASS | Billion Dollar Boy, 7 Jul 2025: survey of 1,000 creators (and 1,000 senior marketers) across the US and UK; 52% burnout; 37% "actively consider leaving" |
| 9 | §9 | Google 2023: two years' inactivity; "We do not have plans to delete accounts with YouTube videos at this time" | https://techcrunch.com/2023/05/18/youtube-will-no-longer-be-deleting-videos-from-inactive-accounts | PASS | TechCrunch, 18 May 2023, headline as in Sources; the sentence is quoted from Google's updated blog post; two-year inactivity policy stated |
| 10 | Deliverable D4 | Low CTR with fewer impressions than usual is the case YouTube names for a title or thumbnail change | others/PB1 D3; https://support.google.com/youtube/answer/16559651?hl=en | PASS | Page: changes are advised when "a video has a lower click-through rate (CTR) and is receiving fewer impressions than usual" |
| 11 | Deliverable D5 | 91.35% under 1,000 in her band; 68% of crossers had 40+, 53.5% had 70+ | others/PB1 D1 Y4, Y5; https://vidiq.com/research/youtube-uploads-1000-subscribers/ ; https://vidiq.com/blog/post/how-many-videos-to-get-1000-subscribers | PASS | 100 - 8.65 = 91.35 (derived). vidIQ, 9 Jun 2025, 5,330,249 channels: 14.54 + 22.58 + 30.89 = 68.01%; 22.58 + 30.89 = 53.47% |
| 12 | Sources | Newman, letter, JAMA 274(13), 4 Oct 1995, 1013; credits Hanley and Lippman-Hand (JAMA, 1983); 3/n | https://jamanetwork.com/journals/jama/article-abstract/389714 ; https://scilit.com/publications/ddfc523d905fccaecb8488227831d6ec | PASS | JAMA page: title, Thomas B. Newman, letter, 274(13), 4 Oct 1995, p. 1013; credits Hanley and Lippman-Hand's rule, upper limit "approximately 3/N". Scilit record of the earlier paper: JAMA 249(13), 1 Apr 1983, 1743-1745 |

All twelve were opened at the outside source where one stands behind the claim (eleven of twelve; claim 1 is a pointer to PB6 and PB7 only).

## Also checked (beyond the sample)

| n | Section | Claim | Source | Verdict | Note |
|---|---|---|---|---|---|
| 13 | §2 | Todd Beaupré, senior director of growth and discovery: "maybe a 10% or less"; PPC Land, 2 Sep 2026 | https://ppc.land/subscribers-skip-90-of-uploads-in-their-feed-youtube-director-says/ | PASS | PPC Land, 2 Sep 2026: "probably all your videos have about maybe a 10% or less click-through rate"; title as given |
| 14 | §2 | PB1's band medians: +0.5 (1-99) and +1.4 (100-499) subscribers a month | https://vidiq.com/research/youtube-subscriber-benchmarks-2026/ | PASS | vidIQ, 20 Jul 2026: +0.5 (1,047,481 channels), +1.4 (1,430,714), +3.7 (853,903) |
| 15 | §3 | NIST §7.2.4.1: Wilson interval's worth "does not strongly depend upon the value of n and/or p"; the page also gives p ± z·√(p(1−p)/n) | https://itl.nist.gov/div898/handbook/prc/section2/prc241.htm | PASS | Exact words; the page names the method Wilson and gives the normal-approximation expression as the one "most frequently used" |
| 16 | §3 | NIST §7.2.4.1: limits may not be accurate enough "if the number of failures is very small or if the sample size N is very small" | https://itl.nist.gov/div898/handbook/prc/section2/prc241.htm | PASS | Exact words (the page's sentence begins "If the number of failures...") |
| 17 | §3 | NIST §1.3.6.6.19: Poisson "is used to model" events in a time interval; standard deviation is the square root of the mean | https://itl.nist.gov/div898/handbook/eda/section3/eda366j.htm | PASS | "The Poisson distribution is used to model the number of events occurring within a given time interval."; mean λ, standard deviation √λ |
| 18 | §3 | NIST Dataplot: "the test statistic for the sign test follows a binomial distribution with p=0.5" | https://itl.nist.gov/div898/software/dataplot/refman1/auxillar/signtest.htm | PASS | Exact words |
| 19 | §3 | Binomial formula in NIST §1.3.6.6.18 | https://itl.nist.gov/div898/handbook/eda/section3/eda366i.htm | PASS | Section 1.3.6.6.18 "Binomial Distribution" gives the probability mass function |
| 20 | §3 | Wilson intervals for 3.0% at 250-5,000 impressions; skip rate 62% on 100 and 400 views; verdict-3 table | derived; recomputed in this run | PASS | All ten bounds, 52.2-70.9, 57.2-66.6, and 87.7/99.7, 46.9/59.7, 13.0/3.3, 2.0/0.02 reproduced |
| 21 | §4 | Y1: median about 180 (upload 1) to 272 (upload 10); median best of ten 1,948 | https://vidiq.com/research/youtube-first-10-videos-study/ | PASS | vidIQ, 28 Jul 2026 (updated 30 Jul): 137,355 long-form channels; 180, 211, 272; best of first ten 1,948; 57.8% had one past 1,000 |
| 22 | §4 | Y2: half of channels and videos between 2% and 10% click-through | https://support.google.com/youtube/answer/7628154?hl=en-GB | PASS | "Half of all channels and videos on YouTube have an impressions CTR that can range between 2% and 10%." |
| 23 | §4 | Y3: 40-55% viewed for 5-15 minute videos, vendor heuristic, no sample | https://vidiq.com/blog/post/average-view-duration/ | PASS | vidIQ, updated 21 Jul 2026: "aim for 40 to 55% viewed", "vidIQ guidance for target bands"; no sample |
| 24 | §4 | Y4: 8.65% of channels adding 12-51 videos crossed 1,000 within 360 days | https://vidiq.com/research/youtube-uploads-1000-subscribers/ | PASS | as sampled claim 6 |
| 25 | §4 | Y5: 68% of channels that crossed 1,000 had 40 or more videos | https://vidiq.com/blog/post/how-many-videos-to-get-1000-subscribers | PASS | as sampled claim 11 |
| 26 | §4 | Y6: +0.5, +1.4, +3.7 subscribers a month by band | https://vidiq.com/research/youtube-subscriber-benchmarks-2026/ | PASS | as above |
| 27 | §4 | Y10, Y11: 8,000 and 3,000 watch hours with 1,000 and 500 subscribers | https://support.google.com/youtube/answer/12843009 (PB1's source; not returned by search) | unverifiable | The Help page was not returned by any search, so it could not be fetched. A secondary page agrees: vidIQ (https://vidiq.com/blog/post/youtube-partner-program-changes-2027/) gives 1,000 + 8,000 hours for new creators from 1 Feb 2027 and 500 + 3,000 for the fan-funding tier. Answer 72851 (en-GB) still shows 4,000 hours, the rule until that date |
| 28 | §4 | Y12, I5: Live at 50 subscribers; Instagram Live at 1,000 followers | https://support.google.com/youtube/answer/9228390 ; https://9to5mac.com/2025/08/01/new-instagram-rule-cuts-off-live-broadcasts-for-small-accounts/ | PASS | YouTube Help: "At least 50 subscribers" and a verified channel; 9to5Mac, 1 Aug 2025: public accounts with 1,000 followers or more, confirmed by Meta to TechCrunch |
| 29 | §4 | I3: median reach 261 accounts a post, all sizes pooled | https://buffer.com/social-media-benchmarks/instagram | PASS | Buffer benchmarks, updated 8 Nov 2026: 261 under "All"; 7.5% monthly growth |
| 30 | §4 | PB1's earlier Q3 wording: "with the 0.36-a-week illustration (I4)" | others/PB1 (current text and correction note of 2026-11-13) | unverifiable | The unit now says these are PB1's earlier words (Audit 4). PB1 no longer holds them; its correction note confirms the comparison was removed but does not reproduce the sentence, so the exact earlier wording cannot be checked from the folder |
| 31 | §4 | PB1 D3's Q3 line and PB7's IG8 column were corrected on 13 Nov 2026 and now read this way | others/PB1 correction note; others/PB7 D2 IG8 | PASS | Run-1 erratum 1 no longer applies |
| 32 | §5 | PB1's earlier wording: "that fortnight's publishing-and-replies line" (PB1 D2); PB4 D1 G repeated it; both corrected 13 Nov 2026 | others/PB1 D2 and correction note; others/PB4 | unverifiable | As above: the correction is confirmed (PB1 D2 now takes the hour from the Instagram derivatives); the earlier sentence is not in the folder. Run-1 erratum 2 no longer applies |
| 33 | §5 | Buffer's within-account estimates: +0.12% at 1-2 posts against +0.26% at 3-5 | https://buffer.com/library/how-often-to-post-on-instagram/ | PASS | as sampled claim 4; 0.14% × 212 = 0.30 |
| 34 | §5 | YouTube 9101241: thresholds "are not published"; "Not enough demographic data" | https://SUPPORT.GOOGLE.COM/youtube/answer/9101241 | PASS | "The actual thresholds at which data is limited are not published and subject to change at YouTube's discretion."; "Not enough demographic data." |
| 35 | §5 | YouTube 141805: "We studied thousands of channels that took a break and found no correlation between break length and changes in views"; "growth in views across uploads is not correlated with time between uploads"; no sample size, period or method | https://support.google.com/youtube/answer/141805?hl=en | PASS | Both exact. The page gives "thousands of channels" and "over the years" and no method, as the unit says |
| 36 | §5 | AIR Media-Tech: dark 14+ days three or more times a year goes with fewer views per video; main analysis 100,000-1,000,000 monthly views | https://air.io/en/audience-growth/does-posting-more-on-youtube-help-we-studied-18000-channels-to-find-out | PASS | AIR, 8 Jun 2026: "Channels that went dark for 14+ days three or more times a year got fewer views per video"; 100K-1M segment; "This is correlational data, not causal." |
| 37 | §5 | PB4 §1's earlier wording: "If her log shows pieces averaging more than two weekends" | others/PB4 §1 (current text) | unverifiable | The unit marks it as earlier wording (P108). PB4 now states the two-pieces-in-two-quarters rule; the earlier sentence is not in the folder |
| 38 | §5 | PB2: five strangers, ten minutes, four of five; conventions (PB2 §3, D5) | others/PB2 | PASS | carried from run 1, row 45; text unchanged |
| 39 | §5 | PB8 clause 10 and its five pre-mortem questions (PB8 D1, D2) | others/PB8 | PASS | carried from run 1, row 54; text unchanged |
| 40 | §7 | Kohavi et al. 2009: controlled experiments are "the best scientific design for establishing a causal relationship between changes" and their effect | https://exp-platform.com/journal-survey | PASS | Page: "Controlled experiments embody the best scientific design for establishing a causal relationship between changes and their influence on user-observable behavior"; DMKD 18(1), 2009, 140-181; four authors as listed |
| 41 | §7 | Test & Compare is computer-only and may return "Not enough impressions" or "Inconclusive" (PB6 §3) | others/PB6 §3; https://support.google.com/youtube/answer/13861714 | PASS | PB6 §3 has both strings. YouTube Help, "A/B test titles & thumbnails": "currently only available on computers through YouTube Studio"; "Inconclusive" is a result label; "Not enough impressions" appears as a reason no winner is named, not as a label (loose, not wrong) |
| 42 | §6 | Verdict 3 reads the anchor platform, "whose two numbers YouTube itself documents" | https://support.google.com/youtube/answer/7628154?hl=en-GB | PASS | YouTube documents both metrics and the 2-10% range; the 40-55% band is vidIQ's, which §4 says |
| 43 | Deliverable D1 | AU2: Studio, Audience, "Channels your audience watches" | https://support.google.com/youtube/answer/9314416 | FAIL | YouTube Help 9314416 names the report "Channels that your audience watches"; PB3 D1 trait 9 quotes it that way. The quoted label drops "that" (errata PB10-6, PB10-7). Minor |
| 44 | Deliverable D1 | YT5: 50% "above typical" list (PB6 YT5) | others/PB6 | PASS | string present in PB6 |
| 45 | Deliverable D3 | PB3's "on Instagram, mainly under 50" | others/PB3 | PASS | string present in PB3 |
| 46 | Deliverable D4 | None past 1,000 views, as for 42.2% of PB1's cohort | https://vidiq.com/research/youtube-first-10-videos-study/ | PASS | 100 - 57.8 = 42.2 |
| 47 | Deliverable D4 | New thumbnail "at most four words, in her colours (PB5 §7)" | others/PB5 §7, §8 | FAIL | §7 rule 2 sets the four words; the colour rule is §8 ("text is white or cream on a near-black or teak band"). Section pointer; erratum PB10-1. Minor |
| 48 | Deliverable D4 | Thumbnail change "in place of the two whole-piece views from the taped mark, as found and finished, that PB5 §7 rule 1 set" | others/PB5 §7 rule 1; case-facts.md PB10 entry | PASS | PB5 §7 rule 1: "usually the as-found and finished views from the taped mark side by side". Run-1 flag 8 no longer applies |
| 49 | Deliverable D5 | "YouTube answer 141805 finds no correlation between break length and change in views"; "three or more times" (PB1 §6) | https://support.google.com/youtube/answer/141805?hl=en ; https://air.io/en/audience-growth/does-posting-more-on-youtube-help-we-studied-18000-channels-to-find-out | PASS | as above |
| 50 | §1 | PB6 D2, PB7 D2, "What the rows do not tell her" | others/PB6, PB7 | PASS | heading present in both |

Run 1's rows 13–75 that rest only on other units, the register or the unit's own arithmetic (its 60 internal PASS rows) were not re-run one by one and are not recounted in this run's totals. Re-read here: every passage Audit 4 changed (§4's last sentence, §5's first paragraph, D4's verdict), the internal quotations listed above, and the statistics of §3 and D3–D4 (recomputed).

## Attribution pass

Every quotation, every "X says / reports / according to X" and every Sources title, each against its page. Rows marked A are in the tables above under the number given; the Sources titles follow.

| Item | Section | Verdict | Row |
|---|---|---|---|
| A | §2 | PASS | sample 2: Watch hours only from "long-form videos that you've set to public"; not private, unlisted, |
| A | §4 | PASS | sample 4: Buffer's I4 is an increment over weeks with no posts: "points added to the weekly growth r |
| A | §5 | PASS | sample 5: "Not returned if the IG User has less than 100 followers"; follows and unfollows likewise |
| A | §7 | PASS | sample 7: Regression to the mean "happens when unusually large or small measurements tend to be foll |
| A | §8 | PASS | sample 8: 1,000 US and UK creators: 52% burnout, 37% considering leaving |
| A | §9 | PASS | sample 9: Google 2023: two years' inactivity; "We do not have plans to delete accounts with YouTube  |
| A | Deliverable D4 | PASS | sample 10: Low CTR with fewer impressions than usual is the case YouTube names for a title or thumbna |
| A | Sources | PASS | sample 12: Newman, letter, JAMA 274(13), 4 Oct 1995, 1013; credits Hanley and Lippman-Hand (JAMA, 198 |
| A | §2 | PASS | 13: Todd Beaupré, senior director of growth and discovery: "maybe a 10% or less"; PPC Land, 2  |
| A | §2 | PASS | 14: PB1's band medians: +0.5 (1-99) and +1.4 (100-499) subscribers a month |
| A | §3 | PASS | 15: NIST §7.2.4.1: Wilson interval's worth "does not strongly depend upon the value of n and/o |
| A | §3 | PASS | 16: NIST §7.2.4.1: limits may not be accurate enough "if the number of failures is very small  |
| A | §3 | PASS | 17: NIST §1.3.6.6.19: Poisson "is used to model" events in a time interval; standard deviation |
| A | §3 | PASS | 18: NIST Dataplot: "the test statistic for the sign test follows a binomial distribution with  |
| A | §3 | PASS | 19: Binomial formula in NIST §1.3.6.6.18 |
| A | §4 | PASS | 22: Y2: half of channels and videos between 2% and 10% click-through |
| A | §4 | unverifiable | 30: PB1's earlier Q3 wording: "with the 0.36-a-week illustration (I4)" |
| A | §4 | PASS | 31: PB1 D3's Q3 line and PB7's IG8 column were corrected on 13 Nov 2026 and now read this way |
| A | §5 | unverifiable | 32: PB1's earlier wording: "that fortnight's publishing-and-replies line" (PB1 D2); PB4 D1 G r |
| A | §5 | PASS | 33: Buffer's within-account estimates: +0.12% at 1-2 posts against +0.26% at 3-5 |
| A | §5 | PASS | 34: YouTube 9101241: thresholds "are not published"; "Not enough demographic data" |
| A | §5 | PASS | 35: YouTube 141805: "We studied thousands of channels that took a break and found no correlati |
| A | §5 | PASS | 36: AIR Media-Tech: dark 14+ days three or more times a year goes with fewer views per video;  |
| A | §5 | unverifiable | 37: PB4 §1's earlier wording: "If her log shows pieces averaging more than two weekends" |
| A | §5 | PASS | 38: PB2: five strangers, ten minutes, four of five; conventions (PB2 §3, D5) |
| A | §5 | PASS | 39: PB8 clause 10 and its five pre-mortem questions (PB8 D1, D2) |
| A | §7 | PASS | 40: Kohavi et al. 2009: controlled experiments are "the best scientific design for establishin |
| A | §7 | PASS | 41: Test & Compare is computer-only and may return "Not enough impressions" or "Inconclusive"  |
| A | §6 | PASS | 42: Verdict 3 reads the anchor platform, "whose two numbers YouTube itself documents" |
| A | Deliverable D1 | FAIL | 43: AU2: Studio, Audience, "Channels your audience watches" |
| A | Deliverable D1 | PASS | 44: YT5: 50% "above typical" list (PB6 YT5) |
| A | Deliverable D3 | PASS | 45: PB3's "on Instagram, mainly under 50" |
| A | Deliverable D4 | FAIL | 47: New thumbnail "at most four words, in her colours (PB5 §7)" |
| A | Deliverable D4 | PASS | 48: Thumbnail change "in place of the two whole-piece views from the taped mark, as found and  |
| A | Deliverable D5 | PASS | 49: "YouTube answer 141805 finds no correlation between break length and change in views"; "th |
| A | §1 | PASS | 50: PB6 D2, PB7 D2, "What the rows do not tell her" |

| Sources title | URL opened | Verdict | Note |
|---|---|---|---|
| Barnett, van der Pols and Dobson, "Regression to the mean: what it is and how to deal with it", IJE 34(1), 2005, 215-220, PubMed 15333621 | https://pubmed.ncbi.nlm.nih.gov/15333621/ | PASS | title, journal, year, volume, issue, pages confirmed; the fetched text did not show the authors' names |
| Kohavi, Longbotham, Sommerfield and Henne, "Controlled experiments on the web: survey and practical guide", DMKD 18(1), 2009, 140-181 | https://exp-platform.com/journal-survey | PASS |  |
| Meta for Developers, "Instagram account insights" | https://developers.facebook.com/docs/instagram-platform/api-reference/instagram-user/insights | PASS | page title "Instagram Account Insights" |
| Newman, "If almost nothing goes wrong... Interpreting small numerators", letter, JAMA 274(13), 4 Oct 1995, 1013 | https://jamanetwork.com/journals/jama/article-abstract/389714 | PASS | counted as sampled claim 12 |
| NIST, Dataplot Reference Manual, "Sign test" | https://itl.nist.gov/div898/software/dataplot/refman1/auxillar/signtest.htm | PASS |  |
| NIST/SEMATECH §1.3.6.6.18, "Binomial distribution" | https://itl.nist.gov/div898/handbook/eda/section3/eda366i.htm | PASS |  |
| NIST/SEMATECH §1.3.6.6.19, "Poisson distribution" | https://itl.nist.gov/div898/handbook/eda/section3/eda366j.htm | PASS |  |
| NIST/SEMATECH §7.2.4.1, "Confidence intervals" | https://itl.nist.gov/div898/handbook/prc/section2/prc241.htm | PASS |  |
| NIST/SEMATECH §7.2.4.2, "Sample sizes required" | https://itl.nist.gov/div898/handbook/prc/section2/prc242.htm | PASS |  |
| TechCrunch, "YouTube will no longer be deleting videos from inactive accounts", 18 May 2023 | https://techcrunch.com/2023/05/18/youtube-will-no-longer-be-deleting-videos-from-inactive-accounts | PASS |  |
| YouTube Help, "The YouTube Partner Programme overview and eligibility" (answer 72851) | https://support.google.com/youtube/answer/72851?hl=en-GB | PASS |  |
| YouTube Help, "Understand limited data in YouTube Analytics" (answer 9101241) | https://SUPPORT.GOOGLE.COM/youtube/answer/9101241 | PASS | title right; host in capitals (errata PB10-2, PB10-3) |
| YouTube Help, "YouTube performance FAQ & troubleshooting" (answer 141805) | https://support.google.com/youtube/answer/141805?hl=en | PASS | page: "YouTube performance FAQ & Troubleshooting" |

Attribution stratum: 45 items; FAIL 2 (both minor: a section pointer and a quoted report name), unverifiable 3 (three quotations of other units' wording as it stood before 13 Nov 2026, which the folder no longer holds). Every quotation from an outside page is exact.

## Not checked

- https://support.google.com/youtube/answer/12843009: not returned by any search in this agent, so not fetched (PB1's source for rows Y10, Y11; a secondary page agrees)
- https://creators.instagram.com/earn-cash-making-what-you-love: not searched (PB1's source for row I6; outside the sample and the run-1 list)
- Hanley and Lippman-Hand, JAMA 1983, full text: not opened (bibliographic record only)
- Newman's JAMA letter: abstract excerpt only; the rest of the letter is behind the publisher's wall
- No search or fetch was refused for budget or permission. One note on a fetch: `https://support.google.com/youtube/answer/13861714` (returned by search as "Test & compare thumbnails") served the page "A/B test titles & thumbnails", the page PB6 cites as answer 16391400; it was read as served.

## Failure rate

- Sample: 12 claims. PASS 12, FAIL 0, STALE 0, unverifiable 0. Failure rate 0 of 12 (0%); the full audit is not triggered.
- All claims checked in this run: 62. PASS 56, FAIL 2 (both minor, both outside the sample), STALE 0, unverifiable 4.

## Counts

- Words (`wc -w unit.md`): 12,916. `##` sections: 12.
- Cited claims in the whole unit: **171**. Counted by `out/count_claims.py` (every sentence or table row outside the `viz` blocks that carries a link, a unit pointer, a Help answer number, the handbook or a PB1 row code: 222 candidates, in `out/claim_candidates.json`), then read one by one: 51 removed that state no claim (front matter, templates, Sources and Unsure lists: 17; method statements, lead-ins, cross-references, procedure steps, her-rule lines and sentence fragments split from a counted sentence: 34). Run 1 counted 173 before Audit 4's edits, by a slightly different rule.

| Section | Candidates | Cited claims |
|---|---|---|
| Opening | 4 | 1 |
| §1 | 8 | 7 |
| §2 | 6 | 6 |
| §3 | 12 | 9 |
| §4 | 19 | 16 |
| §5 | 38 | 30 |
| §6 | 12 | 11 |
| §7 | 5 | 4 |
| §8 | 10 | 8 |
| §9 | 7 | 7 |
| D1 | 37 | 35 |
| D2 | 7 | 2 |
| D3 | 16 | 13 |
| D4 | 13 | 13 |
| D5 | 11 | 9 |
| Front matter, Templates, Sources, Unsure list | 17 | 0 |
| **Total** | **222** | **171** |

## Figures

1. `range`, §3: five labels and ten bounds match the table and were recomputed (1.50–5.93, 1.83–4.89, 2.11–4.25, 2.34–3.84, 2.56–3.51); the caption's handbook section is right. **PASS.**
2. `compare`, §3: 99.7, 59.7, 3.3 match the table and the recomputation; 0.0 stands for 0.02%, and the caption says so. **PASS.**
3. `matrix`, §5: every cell traces to §5, D2 or D5 (0.75 h, 5 min, 3 min, annual page, packaging hour, three reply slots, two Reels fewer). **PASS.**
4. `flow`, D2: seven steps, minutes and row codes match D2 steps 1–7. **PASS.**

No figure needs a fix.

## Deliverable

- Exists in full: D1 (the sheet, five blocks), D2 (the sixty-minute procedure), D3 and D4 (Mara's Q1 and Q2), D5 (the annual page), T1–T4.
- Follows from the unit's evidence: verdict 3's count rests on §3's binomial table (recomputed); the packaging choice in D4 rests on YouTube Help 16559651, which says what the unit says it says.
- Mara's facts agree with `case-facts.md` (PB10 entry: review hours, admin hours, T1, sales, list, clamp, verdicts, year-two dates). Run 1's contradiction with PB5 (flag 8) is gone: D4 now replaces the two whole-piece views PB5 §7 rule 1 set.
- Usable without the unit: yes for D2–D5 and the templates; D1 leans on the body in four cells, each a pointer to a reason.
- Open: the R6 line that calls 1.7% the lowest CTR beside a 1.6% row (PB10-4); the colour pointer (PB10-1); the report name in AU2 (PB10-6).

## Course goal and sourcing standard

- Course goal: the unit delivers the third outcome (reading the two platforms' numbers against sourced benchmarks each quarter to decide whether to continue, change format or stop).
- Advice without evidence: none found. Each rule no source sets is marked "her rule".
- "Words in quotation marks are the source's exact words": met for every outside quotation (each checked at its page); not met in one UI label (PB10-6, PB10-7). Three quotations of earlier wording in PB1 and PB4 are labelled as such and cannot be checked from the folder.
- "The unit leaves its sources": the closing line of Sources is incomplete and YouTube Help 16559651 is listed nowhere (PB10-5); one URL's host is in capitals (PB10-2, PB10-3).
- Dates: all thirteen sources carry "checked 13 Nov 2026" or a publication date; all thirteen opened on 15 Nov 2026 and say what the unit says.

## Verdict

**PB10: PASS.** 0 FAIL in 12 sampled claims, each opened at its source; no full audit run. Seven minor errata, no flag. The qualification on run 1's PASS (no outside source opened) is lifted: all thirteen listed sources and eighteen further pages behind the carried figures were opened.

Run-1 errata re-verified against `unit.md` as it stands:

- Run-1 PB10-1 (§4, PB1's Q3 wording): dropped. Audit 4 added the sentence saying PB1 and PB7 were corrected and the quoted words are earlier wording; the run-1 Current no longer occurs.
- Run-1 PB10-2 (§5, the review's hour): dropped. Audit 4 rewrote the sentence ("PB1 first took...; both were corrected on 13 Nov 2026"); the Current no longer occurs.
- Run-1 PB10-3 → PB10-1 here: holds.
- Run-1 PB10-4 → PB10-2: holds.
- Run-1 PB10-5 → PB10-3: holds.
- Run-1 PB10-6 → PB10-4: holds.
- Run-1 PB10-7 → PB10-5: holds.
- Run-1 PB10-8 (flag, D4 thumbnail against PB5 §7): dropped. Audit 4 rewrote D4's change as a close frame of the fault beside the finished piece, in place of the two whole-piece views PB5 §7 rule 1 set; the Current no longer occurs and the contradiction is gone.
- New in part 2: PB10-6 and PB10-7.

## The most consequential errors

None of consequence. The three largest, all minor:

1. D4's R6 line calls upload 11's 1.7% the quarter's lowest click-through while the table beside it shows upload 13 at 1.6%; the line is right only because upload 13 is under 28 days old, which it does not say (PB10-4).
2. The Sources closing line names four units as the origin of carried figures where the unit carries from nine, and YouTube Help 16559651, on which D4's packaging choice rests, is listed nowhere (PB10-5).
3. The quoted Studio report name in AU2 is not the name on YouTube's Help page or in PB3 (PB10-6, PB10-7).

## Bibliography line

No new source to add and none to mark failed; PB10's thirteen sources all re-opened on 15 Nov 2026 and confirmed; normalise `https://SUPPORT.GOOGLE.COM/youtube/answer/9101241` to lower case so it merges with PB3's entry; note that PB10 D4 also cites YouTube Help 16559651 (already listed through PB1 and PB6).

## Changelog line

2026-11-15 · Audit 3 part 2, PB10 · claude-fable-5-2 (fresh isolated agent, search on: 31 searches, 31 fetches) · run 1's sample of 12 re-checked at source: 12 PASS, 0 FAIL; 62 claims checked in all: 56 PASS, 2 FAIL (minor), 0 STALE, 4 unverifiable; attribution pass run; verdict PASS; 7 minor errata (5 carried from run 1, 2 new), 0 flags; run-1 errata 1, 2 and flag 8 dropped as fixed by Audit 4; figures 4 of 4 PASS.

## Errata

**PB10-1** · minor · FAIL · Deliverable D4, Verdict
- Current: `in her colours (PB5 §7)`
- Fix: `in her colours (PB5 §7, §8)`
- Basis: others/PB5: §7 rule 2 sets the four-word limit; the colour rule is §8 ("text is white or cream on a near-black or teak band"); case-facts.md, PB5 entry. No URL: a unit of this course. Run-1 erratum 3, carried over.

**PB10-2** · minor · other · §5, PB3
- Current: `[YouTube Help, Understand limited data in YouTube Analytics, answer 9101241](https://SUPPORT.GOOGLE.COM/youtube/answer/9101241)`
- Fix: `[YouTube Help, Understand limited data in YouTube Analytics, answer 9101241](https://support.google.com/youtube/answer/9101241)`
- Basis: The host is in capitals; others/PB3 D1 cites the same page as https://support.google.com/youtube/answer/9101241, so a bibliography collected by URL lists it twice. The page opened on 15 Nov 2026 and its title and both quotations are right. Run-1 erratum 4, carried over.

**PB10-3** · minor · other · Sources
- Current: `checked 13 Nov 2026. https://SUPPORT.GOOGLE.COM/youtube/answer/9101241`
- Fix: `checked 13 Nov 2026. https://support.google.com/youtube/answer/9101241`
- Basis: As PB10-2, the same URL in the Sources list; others/PB3 D1 gives https://support.google.com/youtube/answer/9101241. Run-1 erratum 5, carried over.

**PB10-4** · minor · other · Deliverable D4, YouTube, R6
- Current: `Lowest CTR, upload 11 (1.7%);`
- Fix: `Lowest CTR among them, upload 11 (1.7%; upload 13's 1.6% is lower but the upload is under 28 days old);`
- Basis: Unit D4 table: upload 13 reads 1.6% and is 13 days old on 5 Jul 2027; others/PB6 D1 R6 (at least 28 days old, lowest CTR of the quarter). No URL: internal. Run-1 erratum 6, carried over.

**PB10-5** · minor · other · Sources, closing line
- Current: `PB1 D1 (Y1–Y12, I1–I7, B1–B2), PB1 §2, §4 and §6, PB6 D1–D2, PB7 D1–D2, PB9 D2–D5;`
- Fix: `PB1 D1 (Y1–Y12, I1–I7, B1–B2), PB1 §2, §3, §4, §6 and §8, PB1 D2–D3 (which carries YouTube Help 16559651), PB2 §3 and D5, PB3 §4 and D1–D2, PB4 §1 and §4–§7, PB5 §7–§9, PB6 §3 and D1–D2, PB7 §9 and D1–D2, PB8 D1–D3, PB9 §8 and D1–D5;`
- Basis: The unit also rests figures and rules on those sections; sourcing standard Part 1, 'The unit leaves its sources'. YouTube Help 16559651 (https://support.google.com/youtube/answer/16559651?hl=en, opened 15 Nov 2026) is cited in D4 by number only and listed nowhere in Sources. Run-1 erratum 7, carried over.

**PB10-6** · minor · FAIL · Deliverable D1, Block D, AU2
- Current: `Studio, Audience, "Channels your audience watches"`
- Fix: `Studio, Audience, "Channels that your audience watches"`
- Basis: YouTube Help, Understand your YouTube audience, https://support.google.com/youtube/answer/9314416 (opened 15 Nov 2026) names the report "Channels that your audience watches"; others/PB3 D1 trait 9 quotes it so. New in part 2 (attribution pass).

**PB10-7** · minor · FAIL · Unsure list
- Current: `The YouTube Studio app path to "Channels your audience watches" was not confirmed in the app (D1 AU2).`
- Fix: `The YouTube Studio app path to "Channels that your audience watches" was not confirmed in the app (D1 AU2).`
- Basis: As PB10-6, the second occurrence: https://support.google.com/youtube/answer/9314416.

Working files left in `out/`: `sample.md`, `count_claims.py`, `claim_candidates.json`, `build.py`.

---

<!-- DD-PB1: f-pb/DD-PB1/audit.md, verbatim -->

Model: claude-fable-5-2

# DD-PB1 · Stratified-sample audit (course PB, Audit 3, part 2) · 15 November 2026 · search on

## Provenance

Auditor: claude-fable-5-2, one fresh isolated agent, 15 Nov 2026. Read only `/home/claude/fpb/DD-PB1`; no memory, past-chat, Projects, connector, Artifact, Agent or `mcp__` tool used. `out/` was empty at the start: no earlier run of part 2 to resume. Web: 37 WebSearch calls (limit 40) and 51 WebFetch calls; every page fetched at an address a search in this agent returned; none refused, none retried. Run 1's report and errata and the earlier fresh check were read; no verdict of either is reused: each claim below was read at its page today. The sample below is the one run 1 recorded on 14 Nov 2026, copied unchanged (addition A), and written here before any check.

## Sample (run 1's, copied unchanged and recorded before any check; one claim per `##` section, 14 sections)

| n | Section | Claim sampled | Source the unit cites |
|---|---|---|---|
| 1 | §1 How the six were chosen | Candogan reports 88 long-form videos, 20,000+ subscribers, 600,000+ views and $300+ revenue at one year | her newsletter, about 28 Jul 2024 |
| 2 | §2 How each history is read | PB6's rules as described: R3 titles carry the words a viewer would type, R4 one topic and format per season, R7 hold the date, R8 no Shorts in year one, R10 no chasing an hour, R11 keep every video public | others/PB6 (pointer) |
| 3 | §3 Ali Abdaal | "In my last three months of working full-time as a doctor, I was cranking out three YouTube videos a week"; since leaving "down to only one or two videos a week" | Every, Superorganizers, 24 Sep 2020 |
| 4 | §4 Christian Pascual | 29,385 subscribers at 12 months (9 Apr 2024); Partner Programme 212 days in, on 7 Nov 2023 | Very Normal, Issue 14, 9 Apr 2024 |
| 5 | §5 Mike Boyd | "There wasn't a grind to 10,000 subs. The first one just hit the nail on the head" | Net Influencer, 4 Mar 2026 |
| 6 | §6 Cam Anderson | 93,400 Instagram followers on 27 Feb 2019 ("the account now at 93.4k followers") | Woodpreneur Podcast ep. 83 show notes |
| 7 | §7 Kayla Itsines | 3.1 million Instagram followers on 26 Jun 2015 | Yahoo (Molly Shea), 26 Jun 2015 |
| 8 | §8 Joe Wicks | "over a million Instagram followers" on 21 Jun 2016 | AP via Global News, 21 Jun 2016 |
| 9 | §9 Against PB6's and PB7's rules | Itsines "a post every three or four hours" (USA Today, 2015), read as departing from IR6 | USA Today via PressReader, 21 Dec 2015 |
| 10 | §10 What a sample of survivors cannot show | 8.65% of channels adding 12 to 51 videos crossed 1,000 subscribers within 360 days (vidIQ, 11 Sep 2026, as PB1 cites it) | others/PB1 §2; vidIQ |
| 11 | §11 Your plan against the six | Abdaal took a break from medicine in August 2020 and decided to leave it in 2021 (his site) | aliabdaal.com/about |
| 12 | Deliverable | Itsines, Latest: 13.1M IG (Startup Daily, 15 Jul 2021) | Startup Daily, 15 Jul 2021 |
| 13 | Sources | Tubefilter (Geoff Weiss), "YouTube launches Shorts beta in U.S.", 18 Mar 2021 (and the body's use: India Sept 2020, US beta 18 Mar 2021) | Tubefilter |
| 14 | Unsure list | The Guardian piece on Wicks is dated 18 June 2016 only in Wikipedia's citation; the inkl copy shows no date | inkl; Wikipedia |

## Table (the sample)

| n | Section | Claim | Source | Verdict | Note |
|---|---|---|---|---|---|
| 1 | §1 | Candogan: 88 long-form videos, 20,000+ subscribers, 600,000+ views, $300+ revenue at one year | https://sidikatunccandogan.substack.com/p/first-year-as-a-youtuber | PASS | Page: "I have published 88 long-form videos, gained 20K+ subscribers, and earned $300+ revenue from 600K+ views"; "my first year of teaching as an assistant professor". The page shows no post date; the first video was recorded on 28 Jul 2023 and the post marks its anniversary, so "about 28 July 2024" holds. |
| 2 | §2 | PB6 rules R3, R4, R7, R8, R10, R11 as the unit describes them | others/PB6 Deliverable rule table | PASS | PB6 rule table rows R3, R4, R7, R8, R10, R11 read as the unit summarises them. |
| 3 | §3 | Abdaal: "cranking out three YouTube videos a week"; "down to only one or two videos a week" | https://every.to/superorganizers/the-double-life-of-productivitys-3842641 | PASS | Both sentences are on the page word for word, first person (Abdaal); article dated 24 Sep 2020 (metadata 23 Sep), byline Dan Shipper. |
| 4 | §4 | Pascual: 29,385 subscribers at 12 months; Partner Programme 212 days in, 7 Nov 2023 | https://verynormal.substack.com/p/issue-14-the-statistics-of-being | PASS | "The channel has attracted 29,385 subscribers."; "The channel took 212 days to reach YouTube Partner status on November 7." Post dated 9 Apr 2024; the page gives no year for 7 November, and 9 Apr 2023 plus 212 days is 7 Nov 2023. |
| 5 | §5 | Boyd: "There wasn't a grind to 10,000 subs. The first one just hit the nail on the head" | https://www.netinfluencer.com/learning-in-public-how-mike-boyd-built-a-sustainable-youtube-business-on-curiosity/ | PASS | Both sentences on the page, Mike speaking; Dragomir Stojkov, 4 Mar 2026. |
| 6 | §6 | Anderson: 93,400 Instagram followers on 27 Feb 2019 ("the account now at 93.4k followers") | https://pod.co/the-woodpreneur-podcast-1/083-woodworking-building-a-following-on-instagram-with-cam-anderson-of-blacktail-studio | PASS | Show notes, S1E83, 27 Feb 2019: "With the account now at 93.4k followers and his services on a waiting list". |
| 7 | §7 | Itsines: 3.1 million Instagram followers on 26 Jun 2015 | https://www.yahoo.com/health/how-trainer-kayla-itsines-built-a-global-fitness-122451982837.html | PASS | "Kayla, for the unaware, has 3.1 million followers on Instagram."; Molly Shea; page date line 26 Jun 2015 (shown as "Updated"). |
| 8 | §8 | Wicks: "over a million Instagram followers" on 21 Jun 2016 | https://globalnews.ca/news/2776599/personal-trainer-joe-wicks-trying-to-get-the-whole-world-lean/ | PASS | "With over a million Instagram followers and a bestselling book"; Louise Dixon, The Associated Press; 21 Jun 2016. |
| 9 | §9 | Itsines "a post every three or four hours" (USA Today, 2015), read as departing from IR6 | https://www.pressreader.com/usa/usa-today-us-edition/20151221/282265254388654 | PASS | "She tries to post something every three or four hours for that particular reason." The date is in the address (20151221); the fetched text shows no date line. The reading against IR6 (three a week, others/PB7) follows. |
| 10 | §10 | 8.65% of channels adding 12 to 51 videos crossed 1,000 subscribers within 360 days (vidIQ, 11 Sep 2026, as PB1 cites it) | others/PB1 §2; https://vidiq.com/research/youtube-uploads-1000-subscribers/ | PASS | PB1 §2 row "12 to 51 \| 1,259,198 \| 8.65%". vidIQ itself, opened: published 11 Sep 2026; 12 to 51: 1,259,198 channels, 108,952 reached 1,000, 8.65%; the study calls itself observational. |
| 11 | §11 | Abdaal took a break from medicine in August 2020 and decided to leave it in 2021 (his site) | https://aliabdaal.com/about | PASS | "In August 2020, I took a break from Medicine, intending to go to Australia to do a year's placement in Emergency Medicine."; "made the decision to officially leave Medicine" sits in the paragraph that opens "In 2021". |
| 12 | Deliverable | Itsines, latest: 13.1M IG (Startup Daily, 15 Jul 2021) | https://www.startupdaily.net/2021/07/fitness-app-founder-kayla-itsines-sells-sweat-for-400-million/ | PASS | "She now has 13.1 million Instagram fans, more than 20 million on Facebook."; Simon Thomsen, 15 Jul 2021. Read at the outlet's /2021/07/ address, the one two searches returned; the unit's /topic/asx/ address was not returned and is not checked. |
| 13 | Sources | Tubefilter (Geoff Weiss), "YouTube launches Shorts beta in U.S.", 18 Mar 2021; India Sept 2020, US beta 18 Mar 2021 | https://tubefilter.com/2021/03/18/youtube-launches-shorts-beta-us-working-on-monetization/ | PASS | Geoff Weiss, 18 Mar 2021; "first launched last September in India"; "is rolling out today in the U.S. via a beta test". The page's full headline is longer: YouTube Launches Shorts Beta In U.S., Says It's "Actively Working On" Monetization; the unit gives its first six words. |
| 14 | Unsure list | The Guardian piece on Wicks is dated 18 June 2016 only in Wikipedia's citation; the inkl copy shows no date | https://www.inkl.com/news/meet-the-body-coach-the-man-with-the-million-dollar-muscles ; https://en.wikipedia.org/wiki/Joe_Wicks_(coach) | PASS | inkl: no date on the page. Wikipedia reference: Stuart Heritage, 18 June 2016, The Guardian. |

## Also checked (beyond the sample; counted in the totals)

Internal checks: the unit against the other units, the register and its own text, re-run on 15 Nov against the unit as it now stands.

| n | Section | Claim | Source | Verdict |
|---|---|---|---|---|
| 15 | §1 | Candogan is one of PB1 §9's two first-year cases, with the same figures | others/PB1 §9 | PASS |
| 16 | §1 | PB1 §9 point 3: an existing audience changes the base rate | others/PB1 §9 point 3 | PASS |
| 17 | §1 | Entry rule: a creator entered only with a dated audience number from the first three years or near a 12-, 24- or 36-month point; Boyd has none | unit §1 against §5; https://www.netinfluencer.com/learning-in-public-how-mike-boyd-built-a-sustainable-youtube-business-on-curiosity/ ; https://yespress.io/mike-boyd | FAIL |
| 18 | §2 | PB1 §9's six-point checklist as listed | others/PB1 §9 points 1 to 6 | PASS |
| 19 | §2 | PB7 rules IR1, IR2, IR5, IR6, IR7, IR9 as described | others/PB7 Deliverable rule table | PASS |
| 20 | §3 | Month counts from June 2017: 14, 18, 38, 39 | arithmetic on the unit's dates | PASS |
| 21 | §3 | One to three videos a week is the 52-plus band and twice Mara's 26 a year or more | others/PB1 §2; case-facts.md (PB1) | PASS |
| 22 | §4 | 787 days from 9 Apr 2023 to 4 Jun 2025; 212 days to 7 Nov 2023 | arithmetic | PASS |
| 23 | §4 | 36 videos a year sits in the 12-51 band, where 8.65% crossed 1,000 within 360 days (figure right; label missing, erratum 2) | others/PB1 §2; https://vidiq.com/research/youtube-uploads-1000-subscribers/ | PASS |
| 24 | §4 | Partner Programme thresholds change on 1 February 2027, as PB1 §4 sets out | others/PB1 §4 | PASS |
| 25 | §5 | 197 videos since Nov 2015 is about 18 a year | arithmetic (17.9) | PASS |
| 26 | §6 | Mar 2020 about 42 months, 27 Feb 2019 about 29 months after 19 Sep 2016; 147 videos about 14 a year | arithmetic (14.5) | PASS |
| 27 | §7 | 21 at the start; 26 Jun 2015 about 34 months in; eight years before Reels | arithmetic | PASS |
| 28 | §8 | 21 Jun 2016 about 29 months, Jun 2017 about 41 months from Jan 2014 | arithmetic | PASS |
| 29 | §9 | PB7's evidence for IR6 is a within-account vendor association (Buffer, 13 Aug 2025) | others/PB7 rule table, IR6 | PASS |
| 30 | §10 | Of 18 points one is a dated count at its point; near numbers 2 to 5 months away; five of six started before Reels and Shorts | unit §3 to §8 | PASS |
| 31 | §10 | PB1 §6's plateau | others/PB1 §6 | PASS |
| 32 | §11 | Mara's plan: one 10-minute video every two weeks, 26 a year, three feed posts a week, 6 hours, no Shorts in year one, day one Mon 4 Jan 2027 | case-facts.md | PASS |
| 33 | §11 | Her pieces: chairs, side tables and small cabinets (PB2) | case-facts.md (PB2) | PASS |
| 34 | Deliverable | Twelve-month review 3 Jan 2028; 24-month review in the week of 1 January 2029 | case-facts.md; others/PB10; others/DD-PB2 | PASS |
| 35 | Deliverable | Pattern 2: "Four of six document" a floor, with Pascual "weekly in year one" | unit §4, §9 R7; https://verynormal.substack.com/p/issue-14-the-statistics-of-being | FAIL |
| 36 | Deliverable | Read for Mara: the four rules as the register records them | case-facts.md "Set by DD-PB1" | PASS |
| 37 | Deliverable | DD-PB2 takes "Keep the job through year two" from this unit | others/DD-PB2 | PASS |
| 38 | Sources | Every address cited in the body is in Sources and the reverse (43 and 43) | script over unit.md | PASS |

## Attribution pass (addition D; counted in the totals)

Every quotation and every "X says / reports / according to X" in the unit, each read against its page on 15 Nov 2026. A row groups the quotations one sentence or bullet takes from one page.

| n | Section | Quotation or attribution | Source | Verdict |
|---|---|---|---|---|
| 39 | §1 | Abdaal: "2 years working full-time as a Junior Doctor" | https://aliabdaal.com/about | PASS |
| 40 | §1 | Pascual: "a Ph.D candidate in Biostatistics at a California university" | https://verynormal.substack.com/about | PASS |
| 41 | §1 | yespress: "Boyd grew up in Dundee, Scotland" (undated, unsigned) | https://yespress.io/mike-boyd | PASS |
| 42 | §1 | Anderson a LifeFlight pilot until March 2020 (Tubefilter; the page writes "Life Flight") | https://tubefilter.com/2022/06/03/youtube-millionaires-blacktail-studio/ | PASS |
| 43 | §1 | Itsines born 21 May 1991 (Wikipedia) | https://en.wikipedia.org/wiki/Kayla_Itsines | PASS |
| 44 | §1 | Wicks a personal trainer running bootcamps (Campaign) | https://www.pressreader.com/uae/campaign-middle-east/20170611/281509341172242 | PASS |
| 45 | §1 | Candogan's archive lists twelve posts, March to August 2025, none about the channel | https://sidikatunccandogan.substack.com/archive | PASS |
| 46 | §1 | Abel "built on social media while" "working a full-time sales job at a boat dealership" | https://socialstudies.beehiiv.com/p/90k-ig-followers-for-a-furniture-restorer ; https://heatherparady.com/blog/38 | FAIL |
| 47 | §1 | Abel: the only audience number is the headline's "90K+ IG Followers", undated; the rest is paywalled; the Parady profile gives no count or start year | https://socialstudies.beehiiv.com/p/90k-ig-followers-for-a-furniture-restorer ; https://heatherparady.com/blog/38 | PASS |
| 48 | §1 | Partridge founded UNILAD (2010) and LADbible (2011) (BusinessCloud, 19 Jan 2025) | https://businesscloud.co.uk/news/adhd-felt-like-10-caffeinated-squirrels-in-my-head-ladbible-founder/ | PASS |
| 49 | §1 | Lewis: "from financial services to full-time YouTube"; 325,000 subscribers, undated | https://youtubecreatorshub.libsyn.com/from-financial-services-to-full-time-youtube-mark-lewiss-story | PASS |
| 50 | §3 | Kagan: first upload a guitar cover on 4 Jan 2017; medical content from 20 Jun 2017, filmed on his phone in Cambodia | https://noahkagan.com/ali-abdaal-interview/ | PASS |
| 51 | §3 | Abdaal: "I started my YouTube channel in 2017 while I was at university" | https://aliabdaal.com/about | PASS |
| 52 | §3 | Kagan: email list "over 130,000", a backup if the platform changes | https://noahkagan.com/ali-abdaal-interview/ | PASS |
| 53 | §3 | First cohort of the course in November 2020; book in 2023 | https://aliabdaal.com/?p=222 ; https://aliabdaal.com/about | PASS |
| 54 | §3 | Kagan: one to three videos a week since 2017; "He's never skipped a week" | https://noahkagan.com/ali-abdaal-interview/ | PASS |
| 55 | §3 | vidIQ: 1,513 videos, 5 long-form and 26 Shorts in 28 days (data 11 Nov 2026) | https://vidiq.com/youtube-stats/channel/@aliabdaal/index.md | unverifiable |
| 56 | §3 | Abdaal: "either me or someone on my team" | https://every.to/superorganizers/the-double-life-of-productivitys-3842641 | PASS |
| 57 | §3 | 50,000-subscriber video of 24 Aug 2018: "a year ago"; "a junior doctor working in Cambridge" | https://rosetta.to/u/aliabdaal/answering-personal-questions-50k-subs-q-a | PASS |
| 58 | §3 | 100,000-subscriber Q&A dated 8 Dec 2018 | https://rosetta.to/u/aliabdaal/ask-doctor-ali-100k-subscribers-q-a | PASS |
| 59 | §3 | "I hit 100,000 subscribers on YouTube in 2018"; "1 million subscribers in September 2020"; 2M Jul 2021, 3M Jun 2022, 4M Apr 2023 | https://aliabdaal.com/?p=222 | PASS |
| 60 | §3 | vidIQ: 6.71 million; gains of 10,000 to 30,000 a month Nov 2025 to Sep 2026, none in Oct 2026 | https://vidiq.com/youtube-stats/channel/@aliabdaal/index.md | PASS |
| 61 | §3 | Abdaal: "made the decision to officially leave Medicine" (2021); pandemic closed Australia's borders | https://aliabdaal.com/about | PASS |
| 62 | §3 | Kagan: he quit his day job at 1 million subscribers | https://noahkagan.com/ali-abdaal-interview/ | PASS |
| 63 | §3 | Abdaal: sponsorships "a vitally important part of our revenue" | https://every.to/superorganizers/the-double-life-of-productivitys-3842641 | PASS |
| 64 | §3 | His site: the business has "grown to over 20 employees" | https://aliabdaal.com/about | PASS |
| 65 | §3 | Abdaal: "I thought I'd be way more productive than I've been so far" | https://every.to/superorganizers/the-double-life-of-productivitys-3842641 | PASS |
| 66 | §3 | Kagan's first tactic: start very niche (an admissions exam), then broaden | https://noahkagan.com/ali-abdaal-interview/ | PASS |
| 67 | §4 | Pascual: "I uploaded my first video on April 9th, 2023"; the page carries no post date | https://verynormal.substack.com/p/issue-41-a-lifelong-goal-achieved | PASS |
| 68 | §4 | "a newsletter for the Very Normal YouTube Channel" | https://verynormal.substack.com | PASS |
| 69 | §4 | 36 videos totalling 311 minutes in the first year | https://verynormal.substack.com/p/issue-14-the-statistics-of-being | PASS |
| 70 | §4 | Weekly schedule "an awful experience"; "about two weeks" | https://verynormal.substack.com/p/issue-14-the-statistics-of-being | PASS |
| 71 | §4 | About page: "I post roughly every two weeks" | https://verynormal.substack.com/about | PASS |
| 72 | §4 | "Balancing it with my research is an ongoing struggle" | https://verynormal.substack.com/p/issue-14-the-statistics-of-being | PASS |
| 73 | §4 | "not going to give up my Ph.D just to get explosive growth on the channel" (Issue 25, 11 Sep 2024) | https://verynormal.substack.com/p/issue-25-should-you-be-afraid-of | PASS |
| 74 | §4 | 100,000 on 4 Jun 2025, "it took 787 days"; "to reach 100K before I graduate" | https://verynormal.substack.com/p/issue-41-a-lifelong-goal-achieved | PASS |
| 75 | §4 | Most viewed "The most important skill in statistics"; best earner "The better way to do statistics" (Issue 18, 17 May 2024) | https://verynormal.substack.com/p/issue-18-a-realistic-look-at-creating | PASS |
| 76 | §4 | "to a new life in industry" | https://verynormal.substack.com/p/issue-41-a-lifelong-goal-achieved | PASS |
| 77 | §4 | Affiliate links: "I may get a small amount of money" | https://verynormal.substack.com/p/issue-14-the-statistics-of-being | PASS |
| 78 | §4 | Explainer videos "hover at around 1-2 cents a day", maximum "$1.20 in a single day"; first two weeks left out | https://verynormal.substack.com/p/issue-18-a-realistic-look-at-creating | PASS |
| 79 | §4 | "Maybe this has hurt my potential channel growth", said "of holding to strict consistency" | https://verynormal.substack.com/p/issue-14-the-statistics-of-being | FAIL |
| 80 | §4 | "I don't think the weekly pace helped, but rather a more mindful approach to the thumbnail and title" | https://verynormal.substack.com/p/issue-41-a-lifelong-goal-achieved | PASS |
| 81 | §4 | His content "has ended up confusing a lot of people" | https://verynormal.substack.com/p/issue-14-the-statistics-of-being | PASS |
| 82 | §5 | vidIQ dates the channel to 23 Oct 2008; yespress says it lay dormant until 2015 | https://vidiq.com/youtube-stats/channel/@mikeboyd/ ; https://yespress.io/mike-boyd | PASS |
| 83 | §5 | MetaFilter, 11 Nov 2015: "It took him five hours and forty-seven minutes" | https://www.metafilter.com/154630/Gladwell-eat-my-shorts | PASS |
| 84 | §5 | Second channel launched "three years ago"; "I struggle to put stuff on TikTok. I don't think it's a good thing to be on" | https://www.netinfluencer.com/learning-in-public-how-mike-boyd-built-a-sustainable-youtube-business-on-curiosity/ | PASS |
| 85 | §5 | Kim: "When we realized we could pay both of us, we both quit our jobs and went all in"; "We have an editor and occasionally hire other cameramen" | https://www.netinfluencer.com/learning-in-public-how-mike-boyd-built-a-sustainable-youtube-business-on-curiosity/ | PASS |
| 86 | §5 | vidIQ: 2.93 million, 197 videos; losses of 10,000 in Dec 2025, Apr 2026, Sep 2026, no change otherwise (views were 477,016,889 on 13 Nov; 477,027,345 on the page's 15 Nov data) | https://vidiq.com/youtube-stats/channel/@mikeboyd/ | PASS |
| 87 | §5 | "people resonated with the first video I put up" | https://www.netinfluencer.com/learning-in-public-how-mike-boyd-built-a-sustainable-youtube-business-on-curiosity/ | PASS |
| 88 | §5 | Most-viewed long-form videos date Dec 2021 to Nov 2022, led by "Can I make money counting cards?" (23 Feb 2022, 3.89 million) | https://vidiq.com/youtube-stats/channel/@mikeboyd/ | PASS |
| 89 | §5 | Kim: "Deciding not to become a huge production company is what has made it sustainable"; "I always say mood over work" | https://www.netinfluencer.com/learning-in-public-how-mike-boyd-built-a-sustainable-youtube-business-on-curiosity/ | PASS |
| 90 | §5 | "Get a good agent who brings you third parties that are worth trusting"; "Stay away from gambling, alcohol"; "I'm really bad at that stuff" | https://www.netinfluencer.com/learning-in-public-how-mike-boyd-built-a-sustainable-youtube-business-on-curiosity/ | PASS |
| 91 | §5 | Two engineering degrees and a master's thesis in progress at the start (yespress) | https://yespress.io/mike-boyd | PASS |
| 92 | §6 | "my wife showed me what a hashtag was"; YouTube in 2016 (his words) | https://tubefilter.com/2022/06/03/youtube-millionaires-blacktail-studio/ | PASS |
| 93 | §6 | vidIQ dates the channel to 19 Sep 2016 | https://vidiq.com/youtube-stats/channel/UC6I0KzAD7uFTL1qzxyunkvA | PASS |
| 94 | §6 | Woodworking Talk Show, 6 Aug 2021: posting "since 2018" | https://thewoodworkingtalkshow.libsyn.com/cam-anderson-of-blacktail-studio-ep-5 | PASS |
| 95 | §6 | Seven days on, seven off; in Tubefilter's words "so much downtime"; quit in March 2020 | https://tubefilter.com/2022/06/03/youtube-millionaires-blacktail-studio/ | PASS |
| 96 | §6 | Feb 2019: emergency services flight pilot; "a one-man woodworking company based out of Portland, Oregon" | https://pod.co/the-woodpreneur-podcast-1/083-woodworking-building-a-following-on-instagram-with-cam-anderson-of-blacktail-studio | PASS |
| 97 | §6 | "the thousands of views" given as "Tubefilter's account" (the words are Anderson's, quoted) | https://tubefilter.com/2022/06/03/youtube-millionaires-blacktail-studio/ | FAIL |
| 98 | §6 | About one video a month in 2022, a wish for every two to three weeks, Shorts under test | https://tubefilter.com/2022/06/03/youtube-millionaires-blacktail-studio/ | PASS |
| 99 | §6 | Show notes: first year slow; Instagram, at his wife's suggestion, is what took the business off | https://pod.co/the-woodpreneur-podcast-1/083-woodworking-building-a-following-on-instagram-with-cam-anderson-of-blacktail-studio | PASS |
| 100 | §6 | Sponsorship offers at about 30,000 to 40,000 subscribers, 2018 to 2019: "They weren't very good offers" | https://tubefilter.com/2022/06/03/youtube-millionaires-blacktail-studio/ | PASS |
| 101 | §6 | About one million subscribers by June 2022 | https://tubefilter.com/2022/06/03/youtube-millionaires-blacktail-studio/ | PASS |
| 102 | §6 | vidIQ: 3.46 million, 147 videos, no net change in 28 days, none in four of the last twelve months | https://vidiq.com/youtube-stats/channel/UC6I0KzAD7uFTL1qzxyunkvA | PASS |
| 103 | §6 | Fifth or sixth video, an epoxy table: "that one got a couple million views pretty quick"; about 20,000 subscribers | https://tubefilter.com/2022/06/03/youtube-millionaires-blacktail-studio/ | PASS |
| 104 | §6 | Barnwood, "a big part of the whole 'ugly end products' thing" | https://tubefilter.com/2022/06/03/youtube-millionaires-blacktail-studio/ | PASS |
| 105 | §6 | The Tilt: "regularly turning down $20K commissioned projects that don't fit his business model"; most sponsorship offers declined | https://www.thetilt.com/content-entrepreneur/blacktail-studio-cam-anderson | PASS |
| 106 | §6 | "I never wanted to be a big furniture company with a bunch of employees"; hired a videographer | https://tubefilter.com/2022/06/03/youtube-millionaires-blacktail-studio/ | PASS |
| 107 | §6 | "thousands, or even tens of thousands"; Home Depot; "I never spent any money I didn't make from furniture" | https://tubefilter.com/2022/06/03/youtube-millionaires-blacktail-studio/ | PASS |
| 108 | §6 | Blog post, 9 Nov 2023: advertising revenue of five videos, $5,486 to $70,533 | https://cameron-anderson-f9sx.squarespace.com/blog/5-terrible-builds-that-paid-me-131708 | PASS |
| 109 | §6 | "I was an idiot so I sold it on Etsy for like $350 and didn't charge shipping"; shipping $150; "was apparently pricing myself way too low" | https://tubefilter.com/2022/06/03/youtube-millionaires-blacktail-studio/ | PASS |
| 110 | §6 | His view that giving away his methods brought more sales and followers | https://tubefilter.com/2022/06/03/youtube-millionaires-blacktail-studio/ | PASS |
| 111 | §6 | Instagram announced Reels on 5 Aug 2020 | https://about.instagram.com/blog/announcements/introducing-instagram-reels-announcement | PASS |
| 112 | §7 | She "joined as @kayla_itsines in August 2012" (Bloomberg, 7 Jul 2016) | https://www.bloomberg.com/features/2016-cult-of-kayla/ | PASS |
| 113 | §7 | Yahoo: women-only gym, mobile trainer, "about 220 clients"; began posting to store her photos; posts followers' progress photos | https://www.yahoo.com/health/how-trainer-kayla-itsines-built-a-global-fitness-122451982837.html | PASS |
| 114 | §7 | Company founded March 2013; two PDF guides January 2014 (Bloomberg) | https://www.bloomberg.com/features/2016-cult-of-kayla/ | PASS |
| 115 | §7 | Facebook: more than 20 million followers in July 2021 (Startup Daily) | https://www.startupdaily.net/2021/07/fitness-app-founder-kayla-itsines-sells-sweat-for-400-million/ | PASS |
| 116 | §7 | "In a few months, Itsines attracted hundreds of thousands of followers" | https://www.bloomberg.com/features/2016-cult-of-kayla/ | PASS |
| 117 | §7 | 4 million in December 2015 (USA Today) | https://www.pressreader.com/usa/usa-today-us-edition/20151221/282265254388654 | PASS |
| 118 | §7 | 4.6 million on 18 March 2016 (Christian Post): the headline's figure; the body says "close to five million" | https://www.christianpost.com/trends/bbg-creator-kayla-itsines-instafamous-trainer-with-4-6-million-followers-on-instagram.html | PASS |
| 119 | §7 | More than 5.3 million in July 2016 (Bloomberg) | https://www.bloomberg.com/features/2016-cult-of-kayla/ | PASS |
| 120 | §7 | "Do I regret calling my guides Bikini Body? My answer is yes"; she "doesn't even like the term 'BBG' anymore"; calorie levels raised in 2014 | https://www.bloomberg.com/features/2016-cult-of-kayla/ | PASS |
| 121 | §7 | Sale to iFIT, July 2021: A$400 million widely reported; note: "the M&A was worth just under $200m" | https://www.startupdaily.net/2021/07/fitness-app-founder-kayla-itsines-sells-sweat-for-400-million/ | PASS |
| 122 | §7 | Bloomberg: a spokesperson narrowed "25 million people" to everyone who had interacted with the products online | https://www.bloomberg.com/features/2016-cult-of-kayla/ | PASS |
| 123 | §8 | Guardian via inkl: "I was a personal trainer for five years"; Instagram for self-promotion in 2014 | https://www.inkl.com/news/meet-the-body-coach-the-man-with-the-million-dollar-muscles | PASS |
| 124 | §8 | Campaign: a friend urged him to try it later in 2013, when Instagram launched video | https://www.pressreader.com/uae/campaign-middle-east/20170611/281509341172242 | PASS |
| 125 | §8 | First YouTube video "HIIT Home Workout for beginners", 29 Aug 2014 (Wikipedia, citing YouTube) | https://en.wikipedia.org/wiki/Joe_Wicks_(coach) | PASS |
| 126 | §8 | Mission page: bootcamps in Richmond, "Often no one came" (undated) | https://thebodycoach.com/mission | PASS |
| 127 | §8 | #leanin15 for 15-second recipe videos; 90-day plan; books (Campaign; mission page) | https://www.pressreader.com/uae/campaign-middle-east/20170611/281509341172242 ; https://thebodycoach.com/mission | PASS |
| 128 | §8 | "Every single day posting breakfast, lunch and dinner" (Campaign; the page has it mid-sentence, lower-case "every") | https://www.pressreader.com/uae/campaign-middle-east/20170611/281509341172242 | PASS |
| 129 | §8 | Guardian: "I've got a million followers" | https://www.inkl.com/news/meet-the-body-coach-the-man-with-the-million-dollar-muscles | PASS |
| 130 | §8 | Campaign: Instagram "rocketed from 600,000 to 1.8 million"; YouTube "has grown from 30,000 subscribers to 300,000" | https://www.pressreader.com/uae/campaign-middle-east/20170611/281509341172242 | PASS |
| 131 | §8 | He quit his job to launch The Body Coach (Business Insider India, undated) | https://businessinsider.in/a-day-in-the-life-of-the-body-coach-the-british-instagram-star-inspiring-thousands-of-people-to-get-lean/amp_articleshow/49486010.cms | PASS |
| 132 | §8 | About 400 sign-ups a day at £147 (the Guardian) | https://www.inkl.com/news/meet-the-body-coach-the-man-with-the-million-dollar-muscles | PASS |
| 133 | §8 | Lean in 15: The Shift Plan (2015) sold 77,000 copies in its opening week (Wikipedia, citing Metro, 26 Mar 2020) | https://en.wikipedia.org/wiki/Joe_Wicks_(coach) | PASS |
| 134 | §8 | "In order to be good on social media, I was antisocial in real life" | https://www.pressreader.com/uae/campaign-middle-east/20170611/281509341172242 | PASS |
| 135 | §9 | Top titles such as "$4000 Block of Wood" (vidIQ); Boyd's and Anderson's most-viewed videos date from 2021 to 2024 | https://vidiq.com/youtube-stats/channel/UC6I0KzAD7uFTL1qzxyunkvA ; https://vidiq.com/youtube-stats/channel/@mikeboyd/ | PASS |
| 136 | §9 | Pascual: two video types inside one subject (Issue 18) | https://verynormal.substack.com/p/issue-18-a-realistic-look-at-creating | PASS |
| 137 | §10 | Kagan credits Abdaal's niche and email list; Pascual says titles and thumbnails mattered more than pace | https://noahkagan.com/ali-abdaal-interview/ ; https://verynormal.substack.com/p/issue-41-a-lifelong-goal-achieved | PASS |
| 138 | Deliverable | Quotations repeated in the brief: "never skipped a week", "we both quit our jobs", "not to become a huge production company", "I never wanted to be a big furniture company" | https://noahkagan.com/ali-abdaal-interview/ ; https://www.netinfluencer.com/learning-in-public-how-mike-boyd-built-a-sustainable-youtube-business-on-curiosity/ ; https://tubefilter.com/2022/06/03/youtube-millionaires-blacktail-studio/ | PASS |
| 139 | Deliverable | Table quotations: "hundreds of thousands" (Bloomberg), "2018 or 2019" (Tubefilter), "antisocial in real life" (Campaign), "way more productive" (Every) | https://www.bloomberg.com/features/2016-cult-of-kayla/ ; https://tubefilter.com/2022/06/03/youtube-millionaires-blacktail-studio/ ; https://www.pressreader.com/uae/campaign-middle-east/20170611/281509341172242 ; https://every.to/superorganizers/the-double-life-of-productivitys-3842641 | PASS |
| 140 | Deliverable | Pattern 1: "Itsines: client transformations since August 2012 (Bloomberg, 7 Jul 2016)" | https://www.bloomberg.com/features/2016-cult-of-kayla/ | PASS |
| 141 | Deliverable | Pattern 1: Wicks joined later in 2013 by Campaign's account or in 2014 by the Guardian's | https://www.pressreader.com/uae/campaign-middle-east/20170611/281509341172242 ; https://www.inkl.com/news/meet-the-body-coach-the-man-with-the-million-dollar-muscles | PASS |

Every Sources entry against its page (author, outlet, title, date). The Tubefilter Shorts entry is sampled claim 13.

| n | Sources entry | Verdict | Note |
|---|---|---|---|
| 142 | aliabdaal.com, about page | PASS |  |
| 143 | aliabdaal.com, ?p=222 (earlier about page) | PASS | The page opens and holds the lines cited; that it is the earlier version is the unit's description. |
| 144 | AP (Louise Dixon) via Global News, "Personal trainer Joe Wicks trying to get the whole world lean", 21 Jun 2016 | PASS | Author, agency and date hold. The headline carries quotation marks the entry drops (erratum 9). |
| 145 | Bloomberg (Claire Suddath), "The Bikini Body Cult of Kayla Itsines", 7 Jul 2016 | PASS |  |
| 146 | The Body Coach, mission page, undated | PASS | No date on the page. |
| 147 | Business Insider India, "A day in the life of The Body Coach", undated | PASS | Undated, unsigned. The headline goes on: "- the British Instagram star inspiring thousands of people to 'get lean'"; the entry gives its opening words. |
| 148 | BusinessCloud (Chris Maguire), "'ADHD felt like 10 caffeinated squirrels in my head' – LADbible founder", 19 Jan 2025 | PASS |  |
| 149 | Campaign Middle East, Joe Wicks profile, 11 Jun 2017, via PressReader | PASS | A description, not a title: the page's headline is "Cooking up a storm of success", by Gurjit Degun. Date from the address. |
| 150 | Cameron Anderson, "5 Terrible Builds That Paid Me $131,708", 9 Nov 2023 | PASS |  |
| 151 | Candogan, "First year as a YouTuber", about 28 Jul 2024 | PASS | The page shows no date. |
| 152 | Candogan, newsletter archive | PASS |  |
| 153 | Christian Post (Abigail Briones), "#BBG Creator Kayla Itsines, 'Instafamous' Trainer With 4.6 Million Followers on Instagram", 18 Mar 2016 | PASS |  |
| 154 | Every, Superorganizers, "The double life of productivity's most famous doctor", 24 Sep 2020 | PASS | Byline Dan Shipper; the text is Abdaal in the first person. |
| 155 | The Guardian (Stuart Heritage), "Meet The Body Coach: the man with the million-dollar muscles", via inkl | PASS | Author and outlet hold. The headline on inkl and in Wikipedia's reference reads "Meet the Body Coach, the man with the million-dollar muscles" (erratum 8). |
| 156 | Heather Parady, Leif Abel profile, 25 Jun 2024 | PASS | A description: the page's title is "How this Man Uses Storytelling on IG to Build His Furniture Business". |
| 157 | Instagram, "Introducing Instagram Reels", 5 Aug 2020 | PASS |  |
| 158 | MetaFilter, "Gladwell, eat my shorts", 11 Nov 2015 | PASS |  |
| 159 | Net Influencer (Dragomir Stojkov), "Learning in public: how Mike Boyd built a sustainable YouTube business on curiosity", 4 Mar 2026 | PASS |  |
| 160 | Noah Kagan, Ali Abdaal interview write-up, 25 Jan 2022 | PASS | A description: the page's title is "How Ali Abdaal Gained 1,300,000 Subscribers While in Med School". |
| 161 | Rosetta, "Answering personal questions - 50k subs Q&A", 24 Aug 2018 | PASS |  |
| 162 | Rosetta, "Ask Doctor Ali - 100k subscribers Q&A", 8 Dec 2018 | PASS |  |
| 163 | Social Studies, "90K+ IG Followers.. For a furniture restorer???", 23 Sep 2024 | PASS |  |
| 164 | Startup Daily (Simon Thomsen), Sweat sale to iFIT, 15 Jul 2021, with editor's note | PASS | Read at the /2021/07/ address; the headline now reads "Fitness app founder Kayla Itsines sells Sweat for $200 million". The unit's /topic/asx/ address: not checked. |
| 165 | The Tilt (Leo Bonacci), "Entrepreneur: Cam Anderson", 3 Jul 2023 | PASS | The search listing gives this title; the fetched page's heading reads "Blacktail Studio: Content Entrepreneur Cam Anderson". |
| 166 | Tubefilter (James Hale), "YouTube Millionaires: Cam Anderson makes a living building $20,000 tables", 3 Jun 2022 | PASS | The headline goes on: "–and a million people watch him do it"; the entry gives its opening words. |
| 167 | USA Today, Kayla Itsines profile, 21 Dec 2015, via PressReader | PASS | A description: the page's headline is "Building body, following and brand on Instagram". Date from the address. |
| 168 | Very Normal, newsletter home | PASS |  |
| 169 | Very Normal, about page | PASS |  |
| 170 | Very Normal, Issue 14, "The statistics of being on YouTube for one year", 9 Apr 2024 | PASS |  |
| 171 | Very Normal, Issue 18, "A realistic look at creating evergreen content", 17 May 2024 | PASS |  |
| 172 | Very Normal, Issue 25, "Should you be afraid of 'falling off'?", 11 Sep 2024 | PASS |  |
| 173 | Very Normal, Issue 41, "A lifelong goal achieved", after 4 Jun 2025 (undated) | PASS | The title is in the address only; the page opens with "NEW VIDEO DROP" and shows no date. |
| 174 | vidIQ, Ali Abdaal channel stats, data 11 Nov 2026 | PASS | The page now carries data of 13 Nov 2026. |
| 175 | vidIQ, Blacktail Studio channel stats, data 13 Nov 2026 | PASS | The page now carries data of 14 Nov 2026. |
| 176 | vidIQ, Mike Boyd channel stats, data 13 Nov 2026 | PASS | The page now carries data of 15 Nov 2026. |
| 177 | Wikipedia, "Joe Wicks (coach)" | PASS |  |
| 178 | Wikipedia, "Kayla Itsines" | PASS |  |
| 179 | The Woodpreneur Podcast, ep. 83, Cam Anderson, 27 Feb 2019 | PASS |  |
| 180 | The Woodworking Talk Show, ep. 5, Cam Anderson, 6 Aug 2021 | PASS |  |
| 181 | Yahoo (Molly Shea), "Kayla Itsines on the 28-Min 'Bikini Body' Secret that Earned Her Instagram Fame", 26 Jun 2015 | PASS |  |
| 182 | yespress.io, "The engineer who learned to fail on camera", undated | PASS |  |
| 183 | YouTube Creators Hub, "From Financial Services to Full-Time YouTube: Mark Lewis's story", undated | PASS |  |

## Not checked

- No WebSearch or WebFetch call was refused; no permission prompt was met; the search limit was not reached (37 of 40).
- Startup Daily, the unit's address `https://www.startupdaily.net/topic/asx/fitness-app-founder-kayla-itsines-sells-sweat-for-400-million/`: two searches returned the article only at `https://www.startupdaily.net/2021/07/fitness-app-founder-kayla-itsines-sells-sweat-for-400-million/` (the outlet's own site, not a copy). The piece was read there; the unit's address itself is not checked. The earlier fresh check met the same thing.
- vidIQ, Ali Abdaal, the snapshot of 11 Nov 2026: the page now carries data of 13 Nov 2026 (1,514 videos; 6 long-form videos and 25 Shorts in 28 days; 6.71 million). The unit's 1,513, 5 and 26 are dated 11 Nov and cannot be read any more: unverifiable, consistent with the page two days on, no erratum. The subscriber count and the monthly series hold.
- Hellah Sidibe (§1): the unit cites no address (it says the article refused its fetch); nothing to open.
- All 43 addresses in the unit's Sources list that run 1 reported as not checked were opened today, the Startup Daily one at its other address.

## Run 1's errata, re-verified against the unit as it now stands (addition C)

| Run 1 id | Now | Why |
|---|---|---|
| DD-PB1-1 (Boyd and criterion 1) | carried as DD-PB1-1 | Current still occurs once; Net Influencer and yespress, opened today, give no early count. |
| DD-PB1-2 (§4's 8.65% unlabelled) | carried as DD-PB1-2 | Current still occurs once; vidIQ's study opened and confirms the figure and that it is observational. |
| DD-PB1-3 (pattern 2, "Four of six") | carried as DD-PB1-3 | Current still occurs once; Issue 14 opened: the weekly schedule was given up inside year one. |
| DD-PB1-4 (pattern 2, "weekly in year one") | carried as DD-PB1-4 | Current still occurs once; Issue 14: 36 videos in the year. |
| DD-PB1-5 (§10 vidIQ data dates) | dropped | Applied since run 1 (Audit 4): the unit now reads "vidIQ, data 11 Nov 2026 for Abdaal and 13 Nov 2026 for Boyd and Anderson"; run 1's Current no longer occurs. |
| DD-PB1-6 (pattern 1, Itsines and Bloomberg) | dropped | The source holds the claim. Bloomberg, opened today: she "joined as @kayla_itsines in August 2012 and used her account to post pictures of clients in sports bras and underwear, along with how much weight they'd lost". Run 1 had inferred from the body that Bloomberg was cited only for the date. |
| DD-PB1-7 (flag, 24-month review date) | dropped | Applied since run 1 (Audit 4): the unit now reads "the 24-month review in the week of 1 January 2029"; run 1's Current no longer occurs. The register line still reads "the 24-month review (1 Jan 2029)"; the two agree in substance, and the register is not this audit's to change. |

## Failure rate

Sample: 14 claims; 14 PASS, 0 FAIL, 0 STALE, 0 unverifiable. Failure rate in the sample: 0 of 14. The decision rule (more than one sampled claim in ten) is not met: no full audit is triggered.

Totals with "Also checked" and the attribution pass: 183 claims; 177 PASS, 5 FAIL, 0 STALE, 1 unverifiable. Of the 5 FAIL, 2 are internal (run 1's: the entry rule that Boyd does not meet; the deliverable's pattern 2) and 3 come from the attribution pass. Attribution pass alone: 145 rows (103 quotation and attribution rows, 42 Sources entries); 3 FAIL, 1 unverifiable: 2.1 per 100, against the 20 per 100 of part 1's stratum. The earlier fresh check's quotation fixes hold at their pages: every quotation it corrected is now the page's wording.

## Figures

1. **Matrix, §9: PASS.** All 42 cells follow §9's text and definitions (R4: Boyd, Anderson, Pascual consistent, Abdaal departs; R7: Abdaal consistent, Pascual departs; R8 n/a for the four whose first years predate Shorts, not documented for Pascual; R11: Boyd and Anderson consistent; IR1 n/a; IR6: both trainers depart, Anderson not documented; IR7: Anderson consistent, Wicks not documented). The caption's sources and dates are the text's.
2. **Timeline, §10: PASS.** The eleven events, their dates and positions and the one span (Sep 2016 to Mar 2020) agree with §3 to §8; each date was also read at its page today (Bloomberg; MetaFilter; vidIQ; Kagan; Tubefilter, both pieces; Instagram; aliabdaal.com; Issue 41).
3. **Matrix, Deliverable A: PASS.** All 60 cells agree with "The six at a glance" and §3 to §8: one "own" count at its point (Pascual, 12 months), seven "near", Itsines's 12 months "unpub.".

No figure erratum.

## Deliverable

It exists in full: A (five patterns, what the six cannot show, four rules for Mara, the twelve-row table, the matrix) and B (a template whose blanks say what goes in them). It can be used without the unit: each number names its owner and date, "unpub." is defined, each rule names the course rule it agrees with. It follows from the body except in pattern 2, which counts Pascual among those with "a floor of output they did not let slide" and calls his year one "weekly"; his own Issue 14 says otherwise (errata 3 and 4). Pattern 1's Itsines line, which run 1 queried, holds at Bloomberg. Observation, no erratum: pattern 4's "six of six" fits Boyd loosely ("a skill learned on camera" is not work that already existed).

## Course goal and standard

The unit serves the third outcome: it sets no benchmark of its own, sends the reader to PB1's sheet and PB10's review, and labels all six histories anecdote and survivors. The four rules for Mara are marked untested and each names its pattern; it does not read as advice without evidence. Against the standard: §4's 8.65% carries no source or vendor label where it is made (erratum 2); §1 states an entry rule one of the six does not meet (erratum 1); two attributions say something the page does not (errata 5 and 6) and one names the wrong speaker (erratum 7). Mara's facts agree with `case-facts.md`; she is labelled on first use and never used as evidence. Pointers to PB1 §2, §4, §6 and §9, PB6's and PB7's rule tables, PB10 and DD-PB2 hold. Observations, no erratum: five Sources entries give a description in place of the page's title (Kagan, Campaign Middle East, USA Today, Heather Parady, Startup Daily; the titles are in the Sources table above), three give a headline's opening words (both Tubefilter pieces, Business Insider India), and the Christian Post's 4.6 million is its headline's figure, where its text says "close to five million".

## Verdict

**PASS.** 0 FAIL in 14 sampled claims, each read at its source; no full audit triggered, no section to rewrite. Outside the sample, 5 FAIL in 169 further claims, all corrected by exact replacements: 9 errata (1 error, 5 should-fix, 3 minor), no flag.

## The most consequential errors

1. **Pascual's doubt is turned round (§4).** He wrote "Maybe this has hurt my potential channel growth" about giving up his strict weekly schedule. The unit says he wrote it about holding to strict consistency: the opposite. A reader weighing whether to hold a fixed date is told his regret points the other way.
2. **The summary counts Pascual as holding a floor of output (Deliverable A, pattern 2).** His own post says the weekly schedule "quickly became an awful experience" and was dropped inside the first year, in which he posted 36 videos. "Four of six" should be three, and "weekly in year one" is wrong. This is the page a reader keeps.
3. **Leif Abel is said to have built beside a full-time job (§1).** In the interview cited he left the sales job first, "with no plan B, cold turkey", and took up furniture afterwards. The quoted words are exact; the sentence around them is not what he says. He is the creator closest to the running example, so the slip matters although he was left out.

Also of weight: Boyd does not meet the unit's own entry rule, and the unit does not say so (erratum 1).

## Bibliography line

New sources to add: none (vidIQ Research, "Reaching 1,000 YouTube Subscribers", 11 Sep 2026, is already PB1's). Sources to mark failed: none; all 43 opened on 15 Nov 2026 (Startup Daily at its /2021/07/ address); two titles corrected (the Guardian via inkl; AP via Global News).

## Changelog line

15 Nov 2026 · Audit 3 part 2, DD-PB1 · claude-fable-5-2 · search on (37 searches, 51 fetches) · run 1's sample of 14 read at source: 14 PASS, 0 FAIL; attribution pass of 145 rows: 3 FAIL, 1 unverifiable; 183 claims in all, 5 FAIL, 0 STALE; PASS, no full audit; 9 errata (1 error, 5 should-fix, 3 minor), no flag; run 1's errata 1 to 4 carried, 5 and 7 dropped as applied by Audit 4, 6 dropped as the source holds; figures 1 to 3 PASS.

## Counts

Words (`wc -w unit.md`): 9,457. `##` sections: 14. Cited claims in the unit: 168, tallied by section (each sentence or table row that rests a number, date, quotation, attribution or mechanism on a cited source, once): §1 13 · §2 3 · §3 18 · §4 19 · §5 13 · §6 21 · §7 14 · §8 10 · §9 13 · §10 5 · §11 7 · Deliverable 32 · Sources 0 · Unsure list 0 (reference list and notes, not counted). §3 to §9 and Deliverable A were counted by `out/count_claims.py` (a sentence or table row holding a link or a parenthetical source reference; `viz` blocks and template B left out); §1, §2, §10 and §11 were tallied by hand, since their citations sit in one sentence serving a whole table or outside parentheses (§1: six table rows, seven sentences on those left out). Run 1 counted 167 with its own script; the difference is the sentence splitter.

## Errata

Ids are new for this run; DD-PB1-1 to DD-PB1-4 carry run 1's errata of the same numbers, with the basis now read at the source.

**DD-PB1-1** · erratum · should-fix · §1 How the six were chosen (the spread sentence)
- Current: `four outside the United States (Abdaal, Boyd, Itsines, Wicks).`
- Fix: `four outside the United States (Abdaal, Boyd, Itsines, Wicks). One of the six does not meet criterion 1 as written: no source opened gives a dated audience number from Boyd's first three years or near a 12-, 24- or 36-month point (§5: all three unpublished); he is kept with that gap stated, and his history documents practice, not early numbers.`
- Basis: Carried from run 1 (its DD-PB1-1), now with the sources open. Unit §1 criterion 1 against §5 ('All three unpublished'). Net Influencer, 4 Mar 2026, gives no subscriber count and no start year, https://www.netinfluencer.com/learning-in-public-how-mike-boyd-built-a-sustainable-youtube-business-on-curiosity/ ; yespress.io gives one count, '2.7M subscribers', for 2026, https://yespress.io/mike-boyd ; vidIQ's monthly series starts in October 2025, https://vidiq.com/youtube-stats/channel/@mikeboyd/ . Abel and Lewis were left out in §1 for the same gap.

**DD-PB1-2** · erratum · should-fix · §4 Christian Pascual, Read against PB1 §9, point 2
- Current: `where 8.65% of channels crossed 1,000 within 360 days; his rate`
- Fix: `where 8.65% of channels crossed 1,000 subscribers within 360 days (vidIQ, 11 Sep 2026, as PB1 cites it; vendor data, correlational); his rate`
- Basis: Carried from run 1 (its DD-PB1-2), now with the source open. Sourcing standard Part 5: vendor and correlational data are labelled, and a number is sourced where it is made. vidIQ Research, 'Reaching 1,000 YouTube Subscribers: What 32.9 Million Channels Reveal', 11 Sep 2026: 12 to 51 videos, 1,259,198 channels, 108,952 reached 1,000 (8.65%); the study calls itself observational. https://vidiq.com/research/youtube-uploads-1000-subscribers/ ; PB1 §2 carries the same row.

**DD-PB1-3** · erratum · should-fix · Deliverable A, One-page summary, pattern 2 (the count)
- Current: `Four of six document one; Boyd and Anderson show only an average`
- Fix: `Three of six document one; Pascual dropped his weekly date within year one and uploads when a video is ready (Issue 14), and Boyd and Anderson show only an average`
- Basis: Carried from run 1 (its DD-PB1-3), now with the source open. Very Normal, Issue 14, 9 Apr 2024: 'I started with a weekly upload schedule, and it quickly became an awful experience.'; 'At some point, I decided that strict consistency in uploads was not tenable.' https://verynormal.substack.com/p/issue-14-the-statistics-of-being ; the unit's own §4 (What he stopped: the weekly schedule), §9 R7 (Pascual departs) and figure 1 say the same.

**DD-PB1-4** · erratum · should-fix · Deliverable A, One-page summary, pattern 2 (Pascual)
- Current: `Pascual: weekly in year one, then every two weeks (Issue 14, about page)`
- Fix: `Pascual: 36 videos in year one, the weekly date dropped during it, then roughly every two weeks (Issue 14, about page)`
- Basis: Carried from run 1 (its DD-PB1-4), now with the sources open. Very Normal, Issue 14, 9 Apr 2024: 'I posted 36 videos, adding a total of 311 minutes of statistics content to Youtube'; the weekly schedule 'quickly became an awful experience' and was given up inside the year the post covers. https://verynormal.substack.com/p/issue-14-the-statistics-of-being ; about page: 'I post roughly every two weeks', https://verynormal.substack.com/about

**DD-PB1-5** · erratum · should-fix · §1 Considered and left out (Leif Abel)
- Current: `a furniture restorer who built on social media while "working a full-time sales job at a boat dealership"`
- Fix: `a furniture restorer who began restoring furniture after leaving "a full-time sales job at a boat dealership"`
- Basis: Social Studies, 23 Sep 2024, his words: 'I was working a full-time sales job at a boat dealership ...'; 'I felt I was supposed to leave. So I did, with no plan B, cold turkey.'; 'After leaving my sales job, I was chatting with my mom, and she suggested doing furniture flipping.' https://socialstudies.beehiiv.com/p/90k-ig-followers-for-a-furniture-restorer ; Heather Parady, 25 Jun 2024, has him begin restoring after leaving the sales job, https://heatherparady.com/blog/38 . The quoted words are exact; the claim that he built beside the job is not what the source says. His exclusion (no dated number) stands.

**DD-PB1-6** · erratum · error · §4 Christian Pascual, What he says he got wrong
- Current: `"Maybe this has hurt my potential channel growth", of holding to strict consistency (Issue 14)`
- Fix: `"Maybe this has hurt my potential channel growth", of giving up strict consistency in uploads (Issue 14)`
- Basis: Very Normal, Issue 14, 9 Apr 2024, in order: 'At some point, I decided that strict consistency in uploads was not tenable.' 'What I opted for instead was consistency in effort.' ... 'It turns out that it takes me about two weeks to do this, so that's the rate that it happens.' 'Maybe this has hurt my potential channel growth.' The 'this' is dropping the strict schedule; the unit has the referent reversed. https://verynormal.substack.com/p/issue-14-the-statistics-of-being

**DD-PB1-7** · erratum · minor · §6 Cam Anderson, Platform mix
- Current: `because of his Instagram following (Tubefilter's account).`
- Fix: `because of his Instagram following (Tubefilter; his words).`
- Basis: Tubefilter (James Hale), 3 Jun 2022: the words are Anderson's, in quotation: 'You know, they got in the thousands of views, because I had my Instagram following to kinda push it to.' §9 IR7 of the unit already gives them as 'his account'. https://tubefilter.com/2022/06/03/youtube-millionaires-blacktail-studio/

**DD-PB1-8** · erratum · minor · Sources (the Guardian via inkl)
- Current: `"Meet The Body Coach: the man with the million-dollar muscles", via inkl`
- Fix: `"Meet the Body Coach, the man with the million-dollar muscles", via inkl`
- Basis: The headline on the inkl page reads 'Meet the Body Coach, the man with the million-dollar muscles', https://www.inkl.com/news/meet-the-body-coach-the-man-with-the-million-dollar-muscles ; Wikipedia's reference gives the same title, https://en.wikipedia.org/wiki/Joe_Wicks_(coach)

**DD-PB1-9** · erratum · minor · Sources (AP via Global News)
- Current: `"Personal trainer Joe Wicks trying to get the whole world lean", 21 Jun 2016.`
- Fix: `"Personal trainer Joe Wicks 'trying to get the whole world lean'", 21 Jun 2016.`
- Basis: The page's headline is: Personal trainer Joe Wicks 'trying to get the whole world lean' (the phrase is his, in quotation marks). https://globalnews.ca/news/2776599/personal-trainer-joe-wicks-trying-to-get-the-whole-world-lean/

Each Current was counted with `grep -c -F -- '<current>' unit.md`: 1 each, each on one line. No flag.

---

<!-- DD-PB2: f-pb/DD-PB2/audit.md, verbatim -->

Model: claude-fable-5-2

# Stratified-sample audit, part 2 · DD-PB2 · Deep dive: the quit-your-job math (course PB, Audit 3)

Date: 15 November 2026. Search on: 28 WebSearch calls (limit 40), 29 WebFetch calls, none refused. One unit, one fresh agent. `out/` was empty at the start; this is not a resume. The sample was written to this file before any check.

## Provenance

- Auditor model: claude-fable-5-2. Unit written by Opus 5.5, `search: off`, with six live verifications dated 14 Nov 2026.
- Read: `unit.md`, `brief.txt`, `sourcing-parts-1-and-5.md`, `case-facts.md`, `fresh-check-DD-PB2.md` (to avoid re-reporting; no verdict reused), `run1-audit.md`, `run1-errata.json`, and `others/` for pointers.
- Web rule kept: every page fetched was a URL a search in this agent returned verbatim. No memory, past-chat, Projects, connector, Artifact, Agent or `mcp__` tool was called.
- Part 2 opens all fourteen outside sources run 1 listed as not checked, and seven of the vendor and platform pages behind the unit's PB1 and PB9 pointers.

## Sample (copied from run1-audit.md, recorded before any check)

One claim per `##` section, ten sections.

| # | Section | Sampled claim | Source the unit cites |
|---|---|---|---|
| S1 | §1 The household floor | DOL's COBRA guide lists termination "for any reason other than gross misconduct" and a reduction in hours as qualifying events, 18 months as a rule, premium "cannot exceed 102 percent of the plan's total cost" | US DOL, A Worker's Guide to Health Benefits Under COBRA |
| S2 | §2 Runway | MoneyHelper: "have three to six months' essential outgoings available in an instant access savings account" | MoneyHelper, Emergency savings: how much is enough? |
| S3 | §3 PB9's income lines | In vidIQ's dataset 8.65% of sub-1,000 channels adding 12 to 51 videos crossed 1,000 subscribers within 360 days; no dataset follows new channels for 24 or 36 months | PB1 §2 (vidIQ; vendor, correlational) |
| S4 | §4 Tax | The sources to open are the ones PB8 §6.5 gives: Your Europe FAQ (which sends you to your national authority), HMRC Tax help for hustles: content creators, IRS Topic 554 | PB8 §6.5 and the three pages |
| S5 | §5 Reduced hours, sabbatical, contract | Raffiee and Feng: NLSY79, 1994 to 2008, 2,198 spells of full-time self-employment by 1,093 people, "a 33.3% decrease in the hazard of exit" | Raffiee and Feng 2014, AMJ 57(4), 936–963 |
| S6 | §6 Sensitivity | Base row: earliest pass Mon 7 Jul 2042, 15.0 years after 5 Jul 2027 (derived, by script), with the other ten rows recomputed alongside | The unit's own arithmetic on D1's inputs |
| S7 | Deliverable | Conversion at $1.1052 per euro, the ECB reference rate of 13 November 2026 | ECB, euro foreign exchange reference rates, US dollar |
| S8 | Template | T2 line 2 and T3: T = F_s ÷ (1 − i8); audience needed = T ÷ i12; months = (audience needed − i10) ÷ i11; earliest honest date = the later of the income date and the runway date (agrees with §4, D2, D3) | The unit's body (§2, §4, D2, D3) |
| S9 | Sources | Instituto da Segurança Social, Guia prático: subsídio de desemprego (6001 v4.72), 20 Feb 2025, with the p. 6 condition and p. 14 resignation reading used in §1 | seg-social.pt guide 6001 |
| S10 | Unsure list | "the 33.3% figure is a hazard ratio from a Cox model" | Raffiee and Feng 2014 |

## Table (sampled claims)

| # | Section | Claim | Source | Verdict | Note |
|---|---|---|---|---|---|
| 1 | §1 | S1 · DOL COBRA guide: termination 'for any reason other than gross misconduct', reduction in hours, 18 months as a rule, premium 'cannot exceed 102 percent of the plan's total cost' | https://www.dol.gov/agencies/ebsa/about-ebsa/our-activities/resource-center/publications/workers-guide-health-benefits-cobra?lang=en | PASS | Page opened. 'Termination of employment for any reason other than gross misconduct.'; 'Reduction in hours.'; the chart's maximum period for these events is 18 months (29 or 36 with an extension); 'Your premium cannot exceed 102 percent of the plan's total cost of providing you with coverage.' No date on the page. |
| 2 | §2 | S2 · MoneyHelper: 'have three to six months' essential outgoings available in an instant access savings account' | https://www.moneyhelper.org.uk/en/savings/types-of-savings/emergency-savings-how-much-is-enough?source=mas | PASS | Page opened. Sentence: 'A good rule of thumb to give yourself a solid financial cushion is to have three to six months' essential outgoings available in an instant access savings account.' Undated; (c) 2026 Money and Pensions Service. |
| 3 | §3 | S3 · vidIQ: 8.65% of sub-1,000 channels adding 12 to 51 videos crossed 1,000 within 360 days; no dataset follows new channels 24 or 36 months | https://vidiq.com/research/youtube-uploads-1000-subscribers/ (and others/PB1 §2) | PASS | vidIQ page opened: 12 to 51 band, 108,952 of 1,259,198 = 8.65%; 32,926,088 channels; published 11 Sep 2026; two snapshots 360 days apart, no longer follow-up. PB1 §2 says the same. |
| 4 | §4 | S4 · Sources to open are PB8 §6.5's: Your Europe FAQ (sends you to your national authority), HMRC content creators, IRS Topic 554 | https://europa.eu/youreurope/citizens/work/taxes/income-taxes-abroad/faq/index_en.htm ; https://taxhelpforhustles.campaign.gov.uk/tax-rules-content-creators/ ; https://www.irs.gov/taxtopics/tc554 | PASS | All three opened. Your Europe: 'FAQs - Income taxes abroad', last checked 18/06/2026, tells the reader to 'contact the national tax authorities'. HMRC page live, modified 22 Sep 2026. IRS 'Topic no. 554, Self-employment tax', last reviewed or updated 09-Nov-2026. PB8 §6.5 gives the same three links. |
| 5 | §5 | S5 · Raffiee and Feng: NLSY79, 1994 to 2008, 2,198 spells by 1,093 people, 'a 33.3% decrease in the hazard of exit' | https://msbfile03.usc.edu/digitalmeasures/joe.raffiee/intellcont/Raffiee_Feng_2014_AMJ-1.pdF | PASS | Author's copy opened. '1,093 unique participants, representing 2,198 full-time self-employed job spells'; 1994 to 2008; discussion: 'a significant survival benefit (i.e., a 33.3% decrease in the hazard of exit) associated with staged entry'. AMJ 57(4), 936-963. |
| 6 | §6 | S6 · Base row: earliest pass Mon 7 Jul 2042, 15.0 years after 5 Jul 2027, and the other ten rows | recomputed, out/check.py and out/check2.py | PASS | Recomputed in this run. All ten dated rows reproduce when month k carries the subscribers at its end (61 + 12.67 x (k+1), July 2027 = k 0); the trailing-twelve-month row has no date before 2100. Note: counting each month at its opening subscribers moves four rows (exchange rate, t = 10%, income halved, vidIQ median) one quarter later and leaves the base row unchanged; the unit's own text says the first decimal is noise. |
| 7 | Deliverable | S7 · $1.1052 per euro, the ECB reference rate of 13 November 2026 | https://www.ecb.europa.eu/stats/policy%5Fand%5Fexchange%5Frates/euro%5Freference%5Fexchange%5Frates/html/eurofxref-graph-usd.en.html | PASS | Page opened: 13 November 2026, 1.1052, the latest entry and the low of the August to November 2026 window; high 1.1699 on 21 August 2026. |
| 8 | Template | S8 · T2/T3 formulas agree with §4, D2 and D3 | unit §2, §4, D2, D3 | PASS | Same arithmetic in template and build (re-read in this run). |
| 9 | Sources | S9 · ISS, Guia prático: subsídio de desemprego (6001 v4.72), 20 Feb 2025; p. 6 condition; p. 14 resignation | https://seg-social.pt/documents/10152/15007/6001_subsidio_desemprego/1867b682-64f2-4b1a-8f39-ca008602a16b | PASS | PDF opened: 'Guia Prático – Subsídio de Desemprego', 6001 – v4.72, 20 de fevereiro de 2025. P. 6: 'Ter ficado desempregado por razões alheias à sua vontade (desemprego involuntário).' P. 14: an employer's declaration giving a reason 'que caracterize o desemprego como voluntário, nomeadamente o motivo de denúncia do contrato de trabalho/demissão por iniciativa do trabalhador'. |
| 10 | Unsure list | S10 · 'the 33.3% figure is a hazard ratio from a Cox model' | https://msbfile03.usc.edu/digitalmeasures/joe.raffiee/intellcont/Raffiee_Feng_2014_AMJ-1.pdF | FAIL | Half right. The paper uses 'Cox semiparametric proportional hazards models'. But 33.3% is the percentage fall in the hazard, computed from the coefficient -.405 as 100 x (e^b - 1); the hazard ratio is about 0.667. §5's own wording ('a 33.3% decrease in the hazard of exit') is correct. Erratum DD-PB2-6 (minor). |

## Attribution pass (every quotation, every attributed statement, every Sources title; counted in the totals)

| # | Section | Claim | Source | Verdict | Note |
|---|---|---|---|---|---|
| 11 | §1 | DOL COBRA guide 'does not say whether a resignation qualifies' (also Unsure list) | https://www.dol.gov/agencies/ebsa/about-ebsa/our-activities/resource-center/publications/workers-guide-health-benefits-cobra?lang=en | PASS | No sentence on quitting or resignation; the nearest is the FMLA line. |
| 12 | §1 | DOL: 'unemployed through no fault of your own (determined under State law)'; a separation for a reason other than 'lack of work' is decided by the state; last updated 11 Sep 2026 | https://oui.doleta.gov/unemploy/uifactsheet.asp | PASS | Exact words; 'last updated September 11, 2026'. |
| 13 | §1 | GOV.UK: 'leave a job or lose pay by choice while claiming Universal Credit or just before you claim, without a good reason'; 91 days for a first one in a year; updated 6 Apr 2026 | https://www.gov.uk/guidance/universal-credit-sanctions | PASS | Exact words; 'You'll be sanctioned for 91 days (about 3 months)' for a first high level sanction in any 365 days; last updated 6 April 2026. The page adds that special rules apply to the length where the job was left before the claim. |
| 14 | §2 | PB1 §10 lists 'who continues among part-time creators with full-time jobs' | others/PB1 §10, line 211 | PASS | Exact words, capital W as a list item. |
| 15 | §2 | WA DFI: 'Many experts suggest saving 3 to 6 months of basic living costs'; a state regulator reporting unnamed experts; undated | https://dfi.wa.gov/financial-education/information/importance-having-emergency-savings-account | PASS | Exact words; no date on the page. |
| 16 | §2 and Sources | WA DFI page title 'The importance of having an emergency savings account' | https://dfi.wa.gov/financial-education/information/importance-having-emergency-savings-account | FAIL | The page's title and heading are 'Building an Emergency Savings Fund'. The unit's title is the URL's slug. The URL, the publisher and the quotation hold. Errata DD-PB2-7 and DD-PB2-8 (minor). |
| 17 | §2 | CGD: 'pelo menos, seis meses de despesas'; 'pelo menos, um ano de despesas'; 9 Apr 2026 | https://www.cgd.pt/Site/Saldo-Positivo/protecao/Pages/fundo-emergencia.aspx | PASS | Both phrases on the page; dated 09-04-2026. |
| 18 | §2 | Caixa Geral de Depósitos is 'a state-owned bank' | https://www.cgd.pt/Institucional/Governo-Sociedade-CGD/Praticas-de-Bom-Governo/Documents/Relatorio-Governo-Sociedade-CGD-2020.pdf | PASS | CGD's 2020 corporate governance report: the shares 'pertencem na sua totalidade ao Estado Português e são detidas pela Direção-Geral do Tesouro'. The fresh check had left this unverifiable; the unit cites no source for it. |
| 19 | §2 | Grades: MoneyHelper has no mention of self-employment or variable income; CGD none of independent work or variable income | https://www.moneyhelper.org.uk/en/savings/types-of-savings/emergency-savings-how-much-is-enough?source=mas ; https://www.cgd.pt/Site/Saldo-Positivo/protecao/Pages/fundo-emergencia.aspx | PASS | Neither article body mentions them (MoneyHelper only in the site menu). 'Government-backed' for MoneyHelper is not stated on the page opened; not checked further. |
| 20 | §2 | 'No unemployment benefit follows a resignation in the three places checked (§1)' | https://oui.doleta.gov/unemploy/uifactsheet.asp ; https://www.gov.uk/guidance/universal-credit-sanctions ; https://seg-social.pt/documents/10152/15007/6001_subsidio_desemprego/1867b682-64f2-4b1a-8f39-ca008602a16b | FAIL | Confirmed at the pages: the US page leaves a separation for a reason other than lack of work to the state's decision; GOV.UK describes a sanction of 91 days where there was no good reason; only the ISS guide classes a worker's own resignation as voluntary. Run-1 erratum DD-PB2-1 stands. |
| 21 | §3 | vidIQ: of channels that crossed 1,000, 68% had 40+ videos and 53.5% had 70+ (survivor sample) | https://vidiq.com/blog/post/how-many-videos-to-get-1000-subscribers | PASS | 9 Jun 2025; 5,330,249 channels; 14.54 + 22.58 + 30.89 = 68.01; 22.58 + 30.89 = 53.47. |
| 22 | §3 | AIR Media-Tech: median $2.39 per 1,000 views, Crafting & Handmade, its own client channels | https://air.io/en/air-data-findings/which-youtube-niche-makes-the-most-money-in-2026-ranked-by-real-rpm-and-cpm | PASS | Median RPM $2.39; 'the real YouTube Analytics of 300 channels AIR Media-Tech works with'; May 2025 to May 2026. The unit omits the period (DD-PB2-3). |
| 23 | §3 | YouTube: ad share at 1,000 subscribers with 8,000 qualified watch hours in 365 days for applicants from 1 Feb 2027 (platform-official) | https://blog.google/intl/en-mena/product-updates/connect-communicate/new-opportunities-to-earn-and-changes-to-the-youtube-partner-program/ | PASS | Checked on YouTube's announcement on blog.google: '8,000 qualified watch hours in the last 365 days' for new applicants, terms in effect February 1, 2027, with 1,000 subscribers. YouTube Help answer 12843009 itself was not returned by a search and was not opened. |
| 24 | §3 | YouTube: fan funding, Creator Partnerships, Shopping open at 500 subscribers with 3,000 watch hours | https://support.google.com/youtube/answer/13429240 | PASS | Answer 13429240: '500 subscribers with 3 valid public uploads in the last 90 days, and 3,000 qualified watch hours in the last 12 months'; fan funding and Shopping named. Creator Partnerships at this tier rests on answer 12843009 (via PB9 §2), not opened. |
| 25 | §3 | YouTube Shopping affiliate programme lists 18 countries and not Portugal | https://support.google.com/youtube/answer/13376398?hl=en | PASS | 18 listed; Portugal absent. |
| 26 | §3 | Collabstr: average paid $255 for YouTube in 2025, its own marketplace, no tier breakdown | https://collabstr.com/2026-influencer-marketing-report | PASS | $255 paid, $311 asked; about 21,000 collaborations; no breakdown by follower tier. |
| 27 | §3 | beehiiv's median 0.62% (platform data) | https://www.beehiiv.com/blog/the-state-of-paid-newsletters-2026.md | PASS | 'The median paid conversion rate across beehiiv is 0.62%.' 22 Jun 2026. |
| 28 | §3 | 'PB10 notes that launch-week sales are not independent of the launch email' | others/PB10 D4 R1, line 466 | PASS | PB10: 'Launch-week sales are not independent of the launch email'. |
| 29 | §3 | Sales at these numbers behave like a Poisson count (PB9 §8) | others/PB9 §8, line 120 | PASS |  |
| 30 | §5 | Raffiee and Feng attribute the difference to learning, not measured directly; 'systematically select better ideas ex ante'; shared frailty model; 'unlikely' | https://msbfile03.usc.edu/digitalmeasures/joe.raffiee/intellcont/Raffiee_Feng_2014_AMJ-1.pdF | PASS | Limitations: 'individuals who choose to enter hybrid entrepreneurship systematically select better ideas ex ante'; 'the results from our shared frailty model indicate that this is unlikely'; learning is postulated and inferred from moderators. |
| 31 | §5 | EUR-Lex summary: 'fully consider'; 'to transfer from full-time work to any part-time work that becomes available'; 'is not sufficient reason'; last updated 4 Dec 2016 | https://eur-lex.europa.eu/EN/legal-content/summary/part-time-work.html | PASS | All three phrases present; last update 04.12.2016; page title 'Part-time work'. |
| 32 | §5 | UK: since 6 April 2024 a statutory flexible-working request from the first day of employment (S.I. 2023/1328) | https://www.legislation.gov.uk/uksi/2023/1328/made/data.pdf | PASS | In force 6 April 2024; regulation 2 omits the 26-week qualifying rule; explanatory note: 'a day 1 right'. |
| 33 | §5 | 'COBRA lists a reduction in hours as a qualifying event' | https://www.dol.gov/agencies/ebsa/about-ebsa/our-activities/resource-center/publications/workers-guide-health-benefits-cobra?lang=en | PASS |  |
| 34 | §6 | vidIQ median for 500 to 999 subscribers, +3.7 a month; caption title 'YouTube Subscriber Benchmarks 2026' | https://vidiq.com/research/youtube-subscriber-benchmarks-2026/ | PASS | +3.7 (0.53%); study title 'YouTube Subscriber Benchmarks 2026: What 61 Million Channels Reveal', 20 Jul 2026. |
| 35 | §6 and D1 i9 | ECB: August to November 2026 range $1.1052 to $1.1699; 'the August 2026 high' | https://www.ecb.europa.eu/stats/policy%5Fand%5Fexchange%5Frates/euro%5Freference%5Fexchange%5Frates/html/eurofxref-graph-usd.en.html | PASS | High 1.1699 on 21 August 2026; low 1.1052 on 13 November 2026. |
| 36 | Deliverable D3 | vidIQ band medians +0.5 and +1.4 a month 'for channels of her size' | https://vidiq.com/research/youtube-subscriber-benchmarks-2026/ | PASS | Figures hold: +0.5 at 1 to 99, +1.4 at 100 to 499. Only the first is her band at 61 subscribers; run-1 erratum DD-PB2-2 (minor wording) stands. |
| 37 | Deliverable D3 | Percentage growth falls with size (PB1 §2, §6) | https://vidiq.com/research/youtube-subscriber-benchmarks-2026/ | PASS | 1.26%, 0.59%, 0.53%, 0.51%, 0.48%, 0.30%, 0.24% by band. |
| 38 | Deliverable D6 | DD-PB1's prior: 'Keep the job through year two' | others/DD-PB1 Deliverable A, line 278 | PASS | Exact words. |
| 39 | Sources | Title: CGD, Saldo Positivo, 'Fundo de emergência', 9 Apr 2026 | https://www.cgd.pt/Site/Saldo-Positivo/protecao/Pages/fundo-emergencia.aspx | PASS | The page is indexed as 'Fundo de Emergência'; its on-page heading is longer, 'Constituir um fundo de emergência: poupe para uma urgência'. Date holds. Note only. |
| 40 | Sources | Title: ECB, euro foreign exchange reference rates, US dollar | https://www.ecb.europa.eu/stats/policy%5Fand%5Fexchange%5Frates/euro%5Freference%5Fexchange%5Frates/html/eurofxref-graph-usd.en.html | PASS | Page 'US dollar (USD)' under the euro reference rates. |
| 41 | Sources | Title: EUR-Lex, summary of Directive 97/81/EC, 'Part-time work', last updated 4 Dec 2016 | https://eur-lex.europa.eu/EN/legal-content/summary/part-time-work.html | PASS |  |
| 42 | Sources | Title: GOV.UK (DWP), 'Universal Credit sanctions', updated 6 Apr 2026 | https://www.gov.uk/guidance/universal-credit-sanctions | PASS | Publisher Department for Work and Pensions. |
| 43 | Sources | Title: HMRC, 'Tax help for hustles: content creators', modified 22 Sep 2026 | https://taxhelpforhustles.campaign.gov.uk/tax-rules-content-creators/ | PASS | Site 'Tax Help for Hustles', page title 'Tax rules for content creators'; the unit's title joins the two, as PB8 does. Date holds. Flag DD-PB2-9. |
| 44 | Sources | Title: IRS, Topic no. 554, Self-employment tax, last reviewed or updated 9 Nov 2026 | https://www.irs.gov/taxtopics/tc554 | PASS |  |
| 45 | Sources | Title: MoneyHelper (Money and Pensions Service), 'Emergency savings: how much is enough?', undated | https://www.moneyhelper.org.uk/en/savings/types-of-savings/emergency-savings-how-much-is-enough?source=mas | PASS | Page title 'Emergency savings – how much is enough?' (a dash where the unit has a colon). |
| 46 | Sources | Reference: Raffiee and Feng, AMJ 57(4), 2014, 936–963, doi:10.5465/amj.2012.0522, author's copy | https://msbfile03.usc.edu/digitalmeasures/joe.raffiee/intellcont/Raffiee_Feng_2014_AMJ-1.pdF | PASS | Title, journal, volume, issue, year and pages hold. The DOI was not read off the copy. |
| 47 | Sources | Title: The Flexible Working (Amendment) Regulations 2023, S.I. 2023/1328 | https://www.legislation.gov.uk/uksi/2023/1328/made/data.pdf | PASS |  |
| 48 | Sources | Title: US DOL, EBSA, 'A Worker's Guide to Health Benefits Under COBRA', undated | https://www.dol.gov/agencies/ebsa/about-ebsa/our-activities/resource-center/publications/workers-guide-health-benefits-cobra?lang=en | PASS |  |
| 49 | Sources | Title: US DOL, ETA, 'State Unemployment Insurance Benefits', last updated 11 Sep 2026 | https://oui.doleta.gov/unemploy/uifactsheet.asp | PASS |  |
| 50 | Sources | Title: Your Europe, 'FAQs: Income taxes abroad', last checked 18 Jun 2026 | https://europa.eu/youreurope/citizens/work/taxes/income-taxes-abroad/faq/index_en.htm | PASS | Heading 'FAQs - Income taxes abroad'. |

The ISS Sources title and the §1 ISS quotation are sampled claim S9; the Raffiee quotation of §5 is S5; the WA DFI Sources title is row 16.

## Also checked (beyond the sample; counted in the totals)

| # | Section | Claim | Source | Verdict | Note |
|---|---|---|---|---|---|
| 51 | §2 | Runway arithmetic: 12 x 1,500 = 18,000; 9,000 / 450 = 20 months to end Feb 2029; 9,000 / 550 = 16.4 | arithmetic on D1 | PASS |  |
| 52 | §3 | Paid tier: 10 / 0.62% = 1,613; (1,613 - 31) / 22 = 72 quarters, 18 years | arithmetic; others/PB9 D2 V14 | PASS | 1,612.9; 71.9. |
| 53 | §6 | Fourteenfold (income per subscriber) and 1.65 times (pace) | arithmetic on PB10 D3, D4 counts | PASS | 14.05; 1.65. |
| 54 | Deliverable D2 | T = USD 1,657.80 a month, 19,893.60 a year; 1,842.00 at t = 10% | arithmetic on D1 | PASS |  |
| 55 | Deliverable D3 | 2,215 subscribers; 170 months; 127.5 sales; 3.5 a month; 36 times; 693,640 views; about 437; about 1,590 times | arithmetic on D1; others/PB9 D3, PB10 D4 | PASS | 2,214.9; 170.0; 127.52; 3.51; 36.3; 693,640; 437.0; 1,587. |
| 56 | Deliverable D4 | USD 45.66 = EUR 41.31; K about EUR 1,459 | arithmetic on D1 | PASS |  |
| 57 | Deliverable D5 | EUR 1,720; margin 20; 69.8%; 450 months; EUR 430 less saving | arithmetic on D1 | PASS |  |
| 58 | whole unit | Mara's facts agree with the register | case-facts.md, Set by DD-PB2 | PASS | Household, 2,150 / 1,700 / 120 / 200 / 1,500 / 450 / 9,000, R, t, checkpoints, pass rule, 0.7485, 12.7, the three path dates, K and D7 all match. |

## Not checked

- https://support.google.com/youtube/answer/12843009: not returned by any search in this agent, so not fetched (web rule); its 8,000-hour rule was checked on YouTube's blog.google announcement instead, and 'Creator Partnerships at 500 subscribers' stands on PB9 §2 alone
- Instagram's creator page (PB9 §2's source for 'no threshold or rate published'): not searched; the claim was checked in others/PB9 in run 1 only
- doi:10.5465/amj.2012.0522: not read off the author's copy; no publisher page opened
- MoneyHelper 'government-backed' (§2 grade): not stated on the page opened; no further page opened
- https://www.cgd.pt/Investor-Relations/Informacao-Financeira/CGD/Relatorios-Contas/2025/Documents/Press-Release-PT-4T-2025.pdf: opened, does not name the shareholder; ownership taken from CGD's 2020 governance report instead
- run-1 'Also checked' rows 12, 16, 17, 22, 24 to 29, 38 to 41 (pointers into others/): not re-run one by one in part 2; they stand as run 1 left them (all PASS) and are not counted in part 2's totals
- Refused calls: none (no search, fetch or permission refusal in this run).

## Failure rate

- Sample: 10 claims. PASS 9, FAIL 1 (S10, minor), STALE 0, unverifiable 0. Rate 1 in 10: not more than one in ten, so no full audit was run.
- Attribution pass: 40 claims, FAIL 2 (the §2 benefit sentence; the WA DFI title), a rate of 5 per 100 against 20 per 100 in part 1's stratum.
- All claims checked in part 2: 58. PASS 55, FAIL 3, STALE 0, unverifiable 0.

## Counts

- Words: 8,875 (`wc -w unit.md`). `##` sections: 10.
- Cited claims in the whole unit: 87. Method: `out/check.py` split the text outside `viz` blocks into sentences, list items and table rows and kept each that names a cited source (110 candidates, lists in `out/claims_NN.txt`); each was then read. Removed: the 16 Sources entries (references, not claims), 2 template blanks, split halves of one sentence (1 in §3, 2 in §5, 1 in the Unsure list), pointers that rest no claim (1 intro, 3 in §3, 1 in D7, the fresh-check line). Added: §1 'The page does not say whether a resignation qualifies', §2's benefit sentence, two Raffiee sentences in §5, §6's exchange-rate row.
- Per section: intro 3 · §1 5 · §2 6 · §3 26 · §4 4 · §5 11 · §6 2 · Deliverable 24 · Template 0 · Sources 0 · Unsure list 6. The total equals run 1's count, reached independently.

## Figures (`viz` blocks)

1. Matrix, §3: PASS. Nine rows as §3's nine lines; every cell is in the text. The caption's answer numbers 12843009 and 13429240 are PB9 §2's locators and do not appear in this unit's text; no fix.
2. Compare, §6: PASS. Ten bars equal the table (7.7, 8.0, 15.0, 15.8, 16.5, 17.0, 21.3, 24.2, 29.5, 49.3); the caption explains the undrawn row; vidIQ's title and the ECB dates hold at their pages.
3. Decision, D2: PASS. Questions and outcomes are D2 line 6, i17 and i18; USD 1,657.80 and EUR 18,000 are D2 lines 3 and 4.
4. Timeline, D6: PASS. Six dates agree with D3 to D5 and §6; decimal positions agree with the dates.

## Deliverable

- Exists in full: D1 to D7 for Mara, then template T1 to T4 with each blank saying what goes in it.
- Follows from the evidence: every number recomputed (rows 51 to 57, S6); each date names the unsourced assumption it rests on; lines without a sourced timeline enter at zero.
- Usable without the unit: yes for Mara's build; the template points to §1, §2 and §3 in three blanks (i7, i13, i18).
- Build against template: flag DD-PB2-5 (her preconditions omit the health-cover and benefit questions the template asks for).
- Mara's facts agree with `case-facts.md` (row 58).

## Course goal and sourcing standard

- Goal: serves the third outcome (deciding with evidence whether to continue, change or stop); advises neither quitting nor staying.
- Advice without evidence: none found. Rules are labelled as the course's or Mara's; recommendations are questions or pointers.
- Part 1: quotations are the sources' exact words in every case opened. One sentence says more than its sources (DD-PB2-1); one Unsure-list line misnames a statistic (DD-PB2-6); one title is the URL slug, not the page's title (DD-PB2-7, -8); the Sources pointer line misses DD-PB1 §3 to §8 (DD-PB2-4). 'A state-owned bank' is true but uncited in the unit.
- Part 5: no tax rate stated; illustrative values marked; EU, UK and US given with gaps said; one amount without its date (DD-PB2-3).

## Verdict

**DD-PB2: PASS.** 1 FAIL in 10 sampled claims (minor, Unsure list); the more-than-one-in-ten rule is not met and no full audit was run. All fourteen outside sources were opened and hold for every quotation, figure and date the unit takes from them. Across 58 claims: 3 FAIL (1 should-fix, 2 minor), 0 STALE, 0 unverifiable. Run 1's limit (six sampled claims unverifiable) is lifted.

## Most consequential errors

1. §2 says no unemployment benefit follows a resignation in the three places checked. The pages say less: in the US the state decides, in the UK a 91-day sanction applies where there was no good reason, and only Portugal's guide classes a resignation as voluntary. A UK or US reader would read §2 as ruling a benefit out (DD-PB2-1, should-fix).
2. The Unsure list calls the 33.3% a hazard ratio; it is the percentage fall in the hazard, and the ratio is about 0.667. §5 itself words it correctly (DD-PB2-6, minor).
3. The Washington State DFI page is cited under its URL slug; its title is 'Building an Emergency Savings Fund' (DD-PB2-7, -8, minor). Nothing else changes a number or a date.

## Bibliography line

No source to mark failed; all fourteen outside sources of DD-PB2 re-opened 15 Nov 2026 and holding; retitle the WA DFI entry 'Building an Emergency Savings Fund'; optional new source for 'state-owned': CGD, Relatório de Governo Societário 2020, https://www.cgd.pt/Institucional/Governo-Sociedade-CGD/Praticas-de-Bom-Governo/Documents/Relatorio-Governo-Sociedade-CGD-2020.pdf .

## Changelog line

2026-11-15 · Audit 3 part 2, DD-PB2 · claude-fable-5-2 · PASS (1 FAIL in 10 sampled, minor; no full audit) · search on, 28 searches, 14 of 14 outside sources opened · 58 claims checked, 3 FAIL (1 should-fix §2, 2 minor), 0 STALE, 0 unverifiable · 7 errata, 2 flags · run-1 errata 1 to 5 all carried over, none dropped.

## Run-1 errata re-verified

All five run-1 entries still occur exactly once in `unit.md` as it now stands and still hold; none was dropped. DD-PB2-1, -2 and -3 are now confirmed at the outside pages (bases updated); DD-PB2-4 and the flag DD-PB2-5 are internal and unchanged. New in part 2: DD-PB2-6 to -8 (errata) and DD-PB2-9 (flag).

## Errata

**DD-PB2-1** · erratum · should-fix · FAIL

- Section: §2 · Runway, 'What the guidance says', after the table
- Current: `No unemployment benefit follows a resignation in the three places checked (§1).`
- Fix: `None of the three places checked pays unemployment benefit after a resignation as a matter of course (§1): the US leaves the decision to the state, the UK applies a sanction, 91 days for a first one, where there was no good reason, and Portugal treats a worker's own resignation as voluntary.`
- Basis: Pages opened 15 Nov 2026. US: a separation for a reason other than 'lack of work' is decided by the state, https://oui.doleta.gov/unemploy/uifactsheet.asp . UK: a high level sanction of 91 days for a first one in 365 days for leaving 'without a good reason', https://www.gov.uk/guidance/universal-credit-sanctions . Portugal: the guide requires involuntary unemployment and classes a worker's own resignation as voluntary, https://seg-social.pt/documents/10152/15007/6001_subsidio_desemprego/1867b682-64f2-4b1a-8f39-ca008602a16b (pp. 6, 14). §2 says more than these pages and than the unit's own §1.
- `grep -c -F`: 1

**DD-PB2-2** · erratum · minor · other

- Section: Deliverable D3, What has to be true, item 2
- Current: `above the band medians of +0.5 and +1.4 a month for channels of her size (PB1 D1 Y6; vendor)`
- Fix: `above the band median of +0.5 a month for channels of her size, 1 to 99 subscribers, and the +1.4 of the next band, 100 to 499 (PB1 D1 Y6; vendor)`
- Basis: vidIQ, YouTube Subscriber Benchmarks 2026, 20 Jul 2026, opened 15 Nov 2026: +0.5 a month is the 1 to 99 band, +1.4 the 100 to 499 band, https://vidiq.com/research/youtube-subscriber-benchmarks-2026/ ; Mara has 61 subscribers (PB10 D4); PB1 D1 Y6.
- `grep -c -F`: 1

**DD-PB2-3** · erratum · minor · other

- Section: §3 · item 1, YouTube ad revenue share
- Current: `$2.39 per 1,000 views on its own client channels (PB9 §2)`
- Fix: `$2.39 per 1,000 views on its own client channels, May 2025 to May 2026 (PB9 §2)`
- Basis: Part 5: an amount is in its source's currency with its date. AIR Media-Tech, opened 15 Nov 2026: 300 channels it works with, every monetised month from May 2025 to May 2026, https://air.io/en/air-data-findings/which-youtube-niche-makes-the-most-money-in-2026-ranked-by-real-rpm-and-cpm ; PB9 §2.
- `grep -c -F`: 1

**DD-PB2-4** · erratum · minor · other

- Section: Sources, last line
- Current: `DD-PB1 (§11; Deliverable A)`
- Fix: `DD-PB1 (§3 to §8, §11; Deliverable A)`
- Basis: §2 of the unit cites 'DD-PB1 §3 to §8, §11' (a fresh-check fix that the Sources line did not follow); Part 1: the unit leaves its sources. No URL: internal.
- `grep -c -F`: 1

**DD-PB2-5** · flag · minor · other

- Section: Deliverable D1 row i18 against Template T1 row i18
- Current: `| i18 | Preconditions | Employment contract read and any notice given (PB8 J1, J2); income registration answered (T1, done 18 Mar 2027); t filled (i8) | PB8 register; PB10 D3 |`
- Fix: `No replacement given. The template's i18 adds 'health cover and benefits after leaving answered (§1)', and §1 says each of its six items 'has to be answered before a date means anything'; Mara's own i18 leaves it out. Adding it to her row sets a new fact about Mara (what her employer pays that she would have to buy) and changes the preconditions the register records as (J1, J2, T1, t), so it is for the owner to decide.`
- Basis: unit §1 'What a survivable floor leaves out', items 2 and 3; Template T1 i18; case-facts.md, 'Set by DD-PB2', pass-rule line. No URL: internal.
- `grep -c -F`: 1

**DD-PB2-6** · erratum · minor · FAIL

- Section: Unsure list, Raffiee and Feng line
- Current: `the 33.3% figure is a hazard ratio from a Cox model (§5)`
- Fix: `the 33.3% figure is the fall in the hazard of exit computed from a Cox model's coefficient, a hazard ratio of about 0.667 (§5)`
- Basis: Raffiee and Feng 2014, author's copy, opened 15 Nov 2026: Cox proportional hazards models; 33.3% is 100 x (e^b - 1) for the coefficient -.405, so the hazard ratio is about 0.667 (derived: e^-0.405). https://msbfile03.usc.edu/digitalmeasures/joe.raffiee/intellcont/Raffiee_Feng_2014_AMJ-1.pdF
- `grep -c -F`: 1

**DD-PB2-7** · erratum · minor · FAIL

- Section: §2 · Runway, table, US row
- Current: `[WA DFI, The importance of having an emergency savings account]`
- Fix: `[WA DFI, Building an Emergency Savings Fund]`
- Basis: The page at this URL is titled 'Building an Emergency Savings Fund' (opened 15 Nov 2026); the unit's title is the URL slug. Quotation and publisher hold. https://dfi.wa.gov/financial-education/information/importance-having-emergency-savings-account
- `grep -c -F`: 1

**DD-PB2-8** · erratum · minor · FAIL

- Section: Sources, Washington State DFI entry
- Current: `"The importance of having an emergency savings account", undated`
- Fix: `"Building an Emergency Savings Fund", undated`
- Basis: As DD-PB2-7: the page's title is 'Building an Emergency Savings Fund'. https://dfi.wa.gov/financial-education/information/importance-having-emergency-savings-account
- `grep -c -F`: 1

**DD-PB2-9** · flag · minor · other

- Section: Sources, HMRC entry (and the §4 link text)
- Current: `HMRC, "Tax help for hustles: content creators", modified 22 Sep 2026, as PB8 §6.5 cites it.`
- Fix: `No replacement given. The site is 'Tax Help for Hustles' and the page is titled 'Tax rules for content creators'; the title used here joins the two, exactly as PB8 §6.5 and PB8's Sources do. A change here alone would part from PB8; if wanted, change both to: HMRC, Tax Help for Hustles, "Tax rules for content creators".`
- Basis: Page opened 15 Nov 2026, last modified 22 Sep 2026: https://taxhelpforhustles.campaign.gov.uk/tax-rules-content-creators/ ; others/PB8 lines 171 and 397.
- `grep -c -F`: 1
