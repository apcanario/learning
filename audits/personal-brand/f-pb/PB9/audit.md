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
