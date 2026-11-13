---
audit: fresh check
unit: PB9 · Monetisation: what pays at each audience size
course: personal-brand · PB · Building a Personal Brand on Instagram and YouTube
model: Opus 5.5 (claude-opus-5-5, as the agent states; this session keeps no agent transcript on disk, so the model could not be confirmed from a transcript's "model" field; live search). A Fable 5.1 fresh check of PB9 is owed to the Fable stage (P49)
date: 2026-11-13
chat: own Opus 5.5 agent context, not shown the writing (P31), launched by the W-PB9/W-PB10 chat (which ran on Opus 5.5 and only staged, applied, filed and published) in session https://claude.ai/code/session_01KMmgR1xZNfEBXV8FGL7SYn
verdict: fix · 3 errors, 5 should-fix, 10 minor
---

The checker's final report, verbatim, as the file it wrote in its own folder (`out/fresh-check.md`), copied unchanged by script. Saved before any finding was applied. The exact strings applied are its `out/findings.json`.

Model: claude-opus-5-5

# Fresh check · PB9 · Monetisation: what pays at each audience size

Checked 13 November 2026 with live search. I did not see the unit being written. I read sourcing-standard Part 1 and Part 5 and the brief, then the unit, then the A7 fresh-check report for errata. The unit was not edited. Exact replacements are in `out/findings.json` (18 findings, in report order). Every Current below occurs exactly once in unit.md (checked with `str.count`).

Process note: I fetched one page (beehiiv, The State of Newsletters 2026, `.md` URL) before any search in this run had returned it. I then ran a search that returned that exact URL and fetched it again. Only the second fetch is relied on.

## (1) Coverage

- Platform revenue share, with thresholds and terms dated; Instagram's lack of a published threshold; the professional dashboard read at each checkpoint: **covered** (§2; D5 R4).
- Affiliate links, rates and conversion, graded, with a plain "no source" where none exists: **covered** (§3).
- Brand deals: **covered** (§4). Collabstr and IMH are graded vendor. The unit says plainly that no source gives offer rates for accounts under 1,000.
- Own product, digital and physical: **covered** (§5).
- Paid membership or newsletter: **covered** (§6).
- Services and teaching: **covered, thin**. No evidence exists, and §7 says so plainly. The section is mostly an hours argument, which is acceptable.
- Small-number events, and what they mean for stock and effort: **covered** (§8).
- Platform and payment fees: **covered** (§9).
- When a line is worth starting: **covered** (§10).
- Keeping the account from becoming an advert, with the sponsorship-load evidence: **covered** (§11).
- Deliverable: **covered**. Three scenarios, every assumption in one table with source and grade (D2), the arithmetic shown (D3), and a start rule (D4), then the template.
- The brief's Gives line names DD-PB2 and PB10. PB10 is named in D5. DD-PB2 is not named; it is only a downstream consumer, so this is not a finding.

## (2)–(6) Findings

1. [should-fix] [style] §1; Current: `The brief for this unit lists the lines in another order, starting with platform revenue share, and the sections below follow it; the figure gives the order in which they open.`; Problem: a public reader never sees the brief. This is a production note left in reader-facing text; Fix: `The sections below take the lines in another order, starting with platform revenue share; the figure gives the order in which they open.`; Basis: brief preamble (the reader is anyone; never refer to material the reader cannot open).
2. [error] [figure] §1, figure 1 (flow); Current: the whole viz block body (in findings.json); Problem: the note "500 subscribers + 3,000 watch hours in 12 months, or 3M Shorts views in 90 days" uses "12 months", which does not appear in the unit's text. The text says "3,000 qualified watch hours in the last year or 3M qualified Shorts views in the last 90 days"; Fix: the same JSON with that note changed to `500 subscribers + 3,000 watch hours in the last year, or 3M Shorts views in the last 90 days` (full JSON in findings.json; renders with kit-viz); Basis: unit §2; https://support.google.com/youtube/answer/12843009
3. [error] [accuracy] §2, YouTube thresholds; Current: `channels already in the programme keep their status if they "review and accept the updated terms in YouTube Studio by January 31, 2027", and without that they "stop earning from the associated monetization features beginning February 1, 2027"`; Problem: the page does not make status depend on accepting the terms. It says "If you are already in YPP, your status is not impacted by this update" and "Your decision to accept these terms does not impact your channel’s status in the YouTube Partner Program". Acceptance governs earning from the associated features, not membership; Fix: `channels already in the programme keep their status ("If you are already in YPP, your status is not impacted by this update"), but to keep earning from the associated features they must "review and accept the updated terms in YouTube Studio by January 31, 2027"; without that they "stop earning from the associated monetization features beginning February 1, 2027", a decision YouTube says "does not impact your channel’s status in the YouTube Partner Program"`; Basis: YouTube Help 12843009, https://support.google.com/youtube/answer/12843009 (opened 13 Nov 2026).
4. [minor] [accuracy] §2, What the thresholds mean in views; Current: `PB1 §4 and §5 reached the same figures on 12 November 2026.`; Problem: the view figures are in PB1 §4 ("What 8,000 hours means in views"), rounded to 87,300 and 3,360–4,620. PB1 §5 has the upload-count months, not these figures; Fix: `PB1 §4 reached the same figures, rounded, on 12 November 2026.`; Basis: units/PB1 §4, §5.
5. [should-fix] [attribution] §2, Shopping affiliate; Current: `"each brand or retailer sets its own rates"`; Problem: these are not the page's words. The page says "Every participating brand and retailer will set their commission rates and attribution window for each product"; Fix: `"Every participating brand and retailer will set their commission rates and attribution window for each product"`; Basis: https://support.google.com/youtube/answer/13376398?hl=en
6. [minor] [accuracy] §2, Instagram; Current: `"roughly 30% in a subscriber's first year"`; Problem: the quotation is inexact. The page reads "roughly 30% for a subscriber's first year"; Fix: `"roughly 30% for a subscriber's first year"`; Basis: https://www.inro.social/blog/instagram-subscriptions (last updated 23 Jul 2026).
7. [minor] [accuracy] §4, Whether brands want accounts your size; Current: `reports that 51.43% intend to expand spending on nano creators`; Problem: the page gives 51.43% as "expansion intent" for the nano tier. That figure combines 42.86% planning increases and 8.57% planning to start with the tier, and the page says it is about tier usage, not a spending amount. "Expand spending" stretches it; Fix: `reports that 51.43% of respondents indicate expansion intent for nano creators (42.86% planning an increase, 8.57% planning to start with the tier)`; Basis: https://influencermarketinghub.com/influencer-marketing-benchmark-report/?facet1=pdf (the 2026 report, 4 May 2026; the unit's `?bbpage=1` variant was not returned by search).
8. [minor] [label] §5, The tax question a sale raises; Current: `primary source to open, regulator page`; Problem: the Commission's OSS page is guidance, not primary law, so the label contradicts itself. Its figures hold (1 July 2021, EU-wide EUR 10 000 threshold, TBE services); Fix: `the Commission's own page, to open first; the law behind it, the EU VAT Directive, was not opened for this unit`; Basis: https://vat-one-stop-shop.ec.europa.eu/index_en?
9. [minor] [style] §5, Digital; Current: `"Stripe's standard processing fee of 2.9% + $0.30 per transaction" ([beehiiv, Pricing](https://www.beehiiv.com/pricing?via=start)`; Problem: `?via=` is beehiiv's referral parameter (search also returns `via=Josh-Hines`, `via=celina` and others). A course that keeps affiliate links out of Mara's year should not carry one. The plain URL was returned by search and holds every figure; Fix: `"Stripe's standard processing fee of 2.9% + $0.30 per transaction" ([beehiiv, Pricing](https://www.beehiiv.com/pricing)`; Basis: https://www.beehiiv.com/pricing
10. [minor] [style] §6, What the tools cost (table); Current: `| [beehiiv, Pricing](https://www.beehiiv.com/pricing?via=start) |`; Problem: as in 9; Fix: `| [beehiiv, Pricing](https://www.beehiiv.com/pricing) |`; Basis: as in 9.
11. [error] [accuracy] §11, What the evidence on sponsorship load says; Current: `and it did not study accounts under 1,000 followers`; Problem: false. The manuscript's descriptives give the Instagram sample a minimum of 630 followers (mean 83,782.6, SD 185,989.4) and the Douyin sample a minimum of 939. Accounts under 1,000 were in the data, but follower count was only a control and no result is reported for them; Fix: `and its accounts were mostly far larger than yours: the Instagram sample averaged 83,782.6 followers (smallest 630) and the Douyin sample's smallest had 939, with follower count a control and no result reported for accounts under 1,000`; Basis: Li et al., accepted manuscript, Tables 3 and 6, https://ira.lib.polyu.edu.hk/bitstream/10397/119670/1/Li_Endorsement_Rate_Influencer.pdf
12. [should-fix] [accuracy] D2, row V16; Current: `Restored pieces would need a handover at or near her home, which PB8 clause 3 rules out, or furniture delivery (unpriced); kits need stock (§8)`; Problem: PB8 D1 clause 3 says what is never *published* ("Her city, street or any view that places her home…"). It says nothing about a private handover to a buyer, so "rules out" credits PB8 with a rule it does not set; Fix: `Restored pieces would need a handover that tells a buyer where she lives, which PB8 clause 3 (her city, street and home are never published) does not settle, or furniture delivery (unpriced); kits need stock (§8)`; Basis: units/PB8 D1 clause 3.
13. [minor] [style] D2, row V17; Current: `CTT, Tarifário de serviços postais, 1 Nov 2020: Apartado`; Problem: this is the only source cited in the body without a link (the link appears only in Sources); Fix: `[CTT, Tarifário de serviços postais, 1 Nov 2020](https://www.ctt.pt/application/themes/pdfs/1_tarifario_servicos_postais_1nov.pdf): Apartado`; Basis: Part 5, links as links; the figure itself is confirmed below.
14. [minor] [accuracy] D4, table, Physical product row; Current: `Pieces: no (clause 3); kits: yes`; Problem: same point as 12; Fix: `Pieces: not settled (clause 3 covers what she publishes, not a handover); kits: yes`; Basis: units/PB8 D1 clause 3.
15. [should-fix] [deliverable] D4, the rule; Current: `The guide passes all five; it starts first.`; Problem: the rule says a line starts only if it "covers its own cash costs in the low scenario" and only one line starts at a time. Yet D1 and the D4 table let brand deals in from 6 Jul 2027 with step 4 marked "Unknown: lawyer unpriced", and Low has no deal at all. The deliverable breaks its own rule without saying so, and the decision caption then says only the guide starts; Fix: `The guide passes all five; it starts first. A brand deal cannot pass step 4 on the scenarios (Low has no deal, and the lawyer is unpriced), so D1 sets it apart: from Season 3 each inbound offer is tested on its own, its fee against the lawyer's fee once priced, and is taken only if it passes steps 1, 3, 4 and 5 **(her rule)**.`; Basis: the unit's own §10 steps 4 and 6, D1, D4 table.
16. [should-fix] [figure] D4, figure 4 (decision); Current: the whole viz block body (in findings.json); Problem: the caption's "Applied to her lines, only the digital guide starts in year one." contradicts D1 and D4, which admit inbound brand deals from Season 3; Fix: the same JSON with that sentence replaced by `Applied to her lines, only the digital guide starts on this rule in year one; an inbound brand deal from Season 3 is tested offer by offer (D1, D4).` (full JSON in findings.json; renders); Basis: unit D1, D4.
17. [minor] [deliverable] D5, row R1; Current: `| R1 | Income by line this quarter: gross, fees, net | Gumroad dashboard; T3 log | Q3, 4 Oct 2027 | V6, V9 |`; Problem: the guide launches on Tue 8 Jun 2027, inside Q2, so income exists at the Q2 review on 5 Jul 2027, which PB1 D3 read 7 ("any income") also reads. R1's first read misses a quarter of income; Fix: `| R1 | Income by line this quarter: gross, fees, net | Gumroad dashboard; T3 log | Q2, 5 Jul 2027 | V6, V9 |`; Basis: unit D1; units/PB1 D3 read 7.
18. [minor] [style] Sources; Current: `beehiiv, Pricing, checked 13 Nov 2026. https://www.beehiiv.com/pricing?via=start`; Problem: as in 9; Fix: `beehiiv, Pricing, checked 13 Nov 2026. https://www.beehiiv.com/pricing`; Basis: as in 9.

## Confirmed

- YouTube Help 12843009 (no date on page): from 1 Feb 2027, "8,000 qualified watch hours in the last 365 days, or 20M qualified Shorts views in the last 90 days", plus 1k subscribers; terms by January 31, 2027, quoted correctly; 500 subscribers and either 3,000 hours in the last year or 3M Shorts views in 90 days, for fan funding, Creator Partnerships and Shopping, with "no changes to the eligibility requirements"; 10M Shorts views over 90 days for the Shorts Creator Pool, without removal from YPP or effect on other earnings. https://support.google.com/youtube/answer/12843009
- YouTube Help 13429240: "1,000 subscribers with 4,000 qualified watch hours in the last 12 months"; "3 valid public uploads in the last 90 days"; memberships, Super Chat and Super Stickers, Super Thanks, Jewels and gifts, Shopping; Portugal listed. https://support.google.com/youtube/answer/13429240
- YouTube Official Blog, The YouTube Team, 10 Aug 2026: "55% for long-form videos and 45% for Shorts"; "incentives for brand deals"; "We'll share more details soon". https://blog.youtube/news-and-events/new-opportunities-to-earn-and-changes-to-the-youtube-partner-program/
- YouTube Help 7491256: both quotes exact (70% after taxes and fees; transaction costs covered). https://support.google.com/youtube/answer/7491256?hl=en
- vidIQ AVD, updated 21 Jul 2026: "5 to 15 minutes: aim for 40 to 55% viewed"; "vidIQ guidance"; no sample. https://vidiq.com/blog/post/average-view-duration/
- vidIQ First 10, 28 Jul 2026, updated 30 Jul 2026: 137,355 long-form channels; 272 at the tenth upload; 30-day views; the exclusion sentence exact. https://vidiq.com/research/youtube-first-10-videos-study/
- AIR Media-Tech, dated 1 Jul 2026: 300 channels it works with, May 2025–May 2026; Crafting & Handmade $2.39, Lifestyle $2.98; no Home/DIY niche; refers to September 2026. https://air.io/en/air-data-findings/which-youtube-niche-makes-the-most-money-in-2026-ranked-by-real-rpm-and-cpm
- YouTube Help 13376398: YPP and its subscriber threshold required; the 18 countries exactly as listed; Portugal absent. https://support.google.com/youtube/answer/13376398?hl=en
- Instagram, Monetize with Instagram: six tools as named; no follower, age, country or account-type requirement. https://creators.instagram.com/earn-cash-making-what-you-love
- Inro, last updated 23 Jul 2026: "Meta's own documentation is not consistent on this"; "invite-based and genuinely uneven"; "Meta takes 0% of subscription revenue"; no Meta page linked. https://www.inro.social/blog/instagram-subscriptions
- No Instagram Help Centre page on Subscriptions or Gifts was returned by my search either.
- Meta for Creators, Subscriptions: "10,000 followers or 250+ Return Viewers", "50,000 Post Engagements", "180,000 Watch Minutes", last 60 days; the content says nothing about Instagram. https://creators.facebook.com/tools/fan-subs
- Amazon Associates: 3.00% row includes Toys, Furniture, Home, Home Improvement, Lawn & Garden and Tools; 4.50% Physical Books, Kitchen, Automotive; 4.00% All Other Categories; no effective date. https://affiliate-program.amazon.com/help/node/topic/GRXPHT8U84RAYDXZ?lang=en
- EMARKETER (no date on page) on Agentio: more than 10,000 primarily US integrations, Oct 2023–Dec 2025; the 1.8x quote exact; no base CTR or purchase rate. https://www.emarketer.com/content/sticking-with-same-youtube-creator-nearly-doubles-affiliate-link-ctr
- CMA, updated 3 Sep 2025: both quotes exact. https://www.gov.uk/government/publications/social-media-endorsements-guide-for-influencers/social-media-endorsements-being-transparent-with-your-followers
- FTC Disclosures 101, modified 3 Dec 2024: "the disclosure should be in the video and not just in the description uploaded with the video". The page metadata gives a publication date of 24 Oct 2019; the unit's "Nov 2019" follows the guide's edition and PB8, so I made no finding. https://ftc.gov/business-guidance/resources/disclosures-101-social-media-influencers/
- Collabstr 2026 report (no page date): more than 21,000 collaborations; paid $255 YouTube and $193 Instagram; asking $311 and $214; "down 63% year over year from $418" (418 to 255 is a 39% fall, recomputed); no follower breakdown. https://collabstr.com/2026-influencer-marketing-report
- Collabstr blog: "Micro-influencers (10K–100K followers) average $198 per collaboration"; no figure under 10K. https://collabstr.com/blog/influencer-costs-2025
- IMH 2026: dated 4 May 2026; "600+ respondents"; nano not defined.
- Eisend et al. 2020, *Journal of Advertising* 49(3), 344–366: "61 papers that use 57 distinct data sets"; disclosure "reduced brand attitudes, credibility, and source evaluation". https://research.wur.nl/en/publications/a-meta-analysis-of-the-effects-of-disclosing-sponsored-content/
- Gumroad Pricing: "10% + $0.50" direct; 30% via Discover; no monthly fee; "Gumroad is your merchant of record"; taxes handled since January 1, 2025; silent on whether card processing is inside the fee (unsure item 1 holds). https://gumroad.com/pricing
- beehiiv Pricing: Free $0 up to 2,500; Digital Products on all plans; paid subscriptions only from Lite; Lite $49/mo yearly; "beehiiv takes 0%"; Stripe 2.9% + $0.30; merchant of record not stated. The "at 1,000 subscribers" tier could not be confirmed as text (slider). https://www.beehiiv.com/pricing
- Etsy Sell: $0.20 listing; 6.5% including the shipping you set; 3% + $0.25 via Etsy Payments; varies by bank location. https://etsy.com/sell
- European Commission OSS: from 1 July 2021; EU-wide EUR 10 000 threshold; TBE services. https://vat-one-stop-shop.ec.europa.eu/index_en?
- GOV.UK digital services, updated 28 Mar 2022: the quote is exact. https://www.gov.uk/guidance/the-vat-rules-if-you-supply-digital-services-to-private-consumers
- beehiiv, The State of Paid Newsletters 2026, 22 Jun 2026: the data-basis sentence, 0.62%, "about 6 are paying", $10 and $100, churn 5.06%–16.67%; conversion not formally defined; no list-size breakdown for conversion. https://www.beehiiv.com/blog/the-state-of-paid-newsletters-2026.md
- Artificial Ignorance, 11 Feb 2025: Free 13,413 and Paid 121 as of January 1, 2025. https://www.ignorance.ai/p/two-years-of-artificial-ignorance
- beehiiv, The State of Newsletters 2026, 6 Jan 2026: "43,000 newsletter subscribers and 700+ paying members". https://www.beehiiv.com/blog/the-state-of-newsletters-2026.md
- Patreon State of Create, 19 Feb 2025: no per-fan or per-member dollar figure; links to stateofcreate.co. https://news.patreon.com/articles/state-of-create
- Patreon Creator fees: 10% for pages published after Aug 4, 2025; 3.4% + €0.35 EUR; 2.9% + $0.30 USD; 2.5% conversion; Apple 30%; no monthly fee. https://support.patreon.com/hc/en-us/articles/11111747095181-Creator-fees
- Kit Newsletter plan (dated September 23, 2026 on the page): both quotes exact; no sales fee stated. https://intercom.help/convertkit/en/articles/9053602-the-kit-newsletter-plan
- NIST §1.3.6.6.19: "used to model the number of events occurring within a given time interval"; mean λ, SD √λ. https://itl.nist.gov/div898/handbook/eda/section3/eda366j.htm
- Stripe PT: 1,5% + € 0,25 standard EEE; 2,5% + € 0,25 UK; 3,15% + € 0,25 international; + 2% conversion. The page also lists premium EEE cards at 2,8% + € 0,25, which the unit omits; harmless. https://stripe.com/pt-PT/pricing
- Li, Gao, Gu and Leung, *Journal of Marketing* 2026, doi 10.1177/00222429261422744: the U-shaped quote exact; the two mechanisms; 4,908 influencers and 6,869 posts, October 2022, Australia; turning points .475 (comments) and .393 (likes), "39%–48%"; Douyin 1,000 influencers, .519; follower count a control; experiments n = 168 and 208. Operationalised as the share "prior to the focal sponsored post", as the unit says. Record: https://research.polyu.edu.hk/en/publications/endorsement-rate-in-influencer-marketing/ ; manuscript: https://ira.lib.polyu.edu.hk/bitstream/10397/119670/1/Li_Endorsement_Rate_Influencer.pdf
- CTT "Preços 2020", novembro/2020: Apartado, Singulares, Concessão Anual 58,00 €, VAT excluded. https://www.ctt.pt/application/themes/pdfs/1_tarifario_servicos_postais_1nov.pdf
- All arithmetic recomputed in Python and correct:
  - views: 87,273 / 120,000; 3,357 / 4,615; 32,727 / 45,000; 1,259 / 1,731; 12.3–17.0×; $208.58
  - Poisson: 5th–95th percentiles 0–5, 4–13, 16–32, 84–117; P(<8 | 8) 45.3%; P(≤4) 10.0%; λ/month 1.165 and 0.291 over 209 days; P(0) 31.2% and 74.7%
  - fees: USD 2.00 (13.3%), 0.74 (4.9%), 1.88 (12.5%); €3.98
  - list and paid tier: 1,613; 0.37, 1.35, 6.52, 2.48 members
  - D3 totals 26 / 104 / 567; $588
- All dates recomputed and correct: 25 Apr, 9 May, 23 May, 6 Jun 2027 are Sundays (cut windows two days before uploads 9–12); 8 Jun 2027 is upload 12 and 6 Jul 2027 is upload 14; checkpoint Mondays; 209 days from 8 Jun 2027 to 3 Jan 2028.
- Not checked (no search in my run returned them; the unit says it did not open them either): Substack fees, Kit commerce fees, *South Dakota v. Wayfair*, YouTube answer 72851.

## Unsure list, item by item

1. Gumroad processing: confirmed silent.
2. Instagram Help Centre: confirmed not returned.
3. CTT 2020 price: confirmed. No current price checked.
4. Collabstr: confirmed (no tier breakdown, no page date, the 63% contradiction).
5. Amazon effective date: confirmed absent. Joinability from Portugal was not checked.
6. Li turning points: confirmed in the manuscript.
7. beehiiv 0.62%: confirmed undefined.
8. 55/45 from the blog: confirmed. The Help page gives only the 45% for targeted Shorts ads.
9. Not opened: not checked.
10. AIR date: confirmed inconsistent.

## (3) Figures say whose they are · (4) Labels

Every number names its source or is marked derived, or labelled as Mara's. Vendor, correlational, survivor, platform-data, documented-case, regulator and peer-reviewed labels are present wherever needed. Inro is labelled "Vendor claim, unsourced" and kept out of the model. EMARKETER is labelled a secondary report and kept out of the model. No missing labels.

## (5) Deliverable

Present in full: D1 to D5, the arithmetic shown, the stacked bars, and template T1 to T4 with every blank described. It follows from the evidence: zero platform lines on cited thresholds, Gumroad's fee, illustrative counts labelled, a paid share from beehiiv and two cases. It can be used on its own. The one internal inconsistency is the brand-deal exception to the start rule (findings 15 and 16).

## (6) Errata and pointers

- **A7 fresh-check errata touching PB9.** The VoxBooster rates are not used. The Social Media Today reading is not used. Patreon's $52/$110 (sourced in A7 through Net Influencer) is correctly left out, because Patreon's own article lacks them (confirmed). No erratum is pending against PB9.
- **A gap from the A7 report.** A7's check found an Instagram-official page listing Portugal for Subscriptions (creators.instagram.com blog, 20 Sep 2023). PB9 does not use it. That is not an error, because that page gives no eligibility rule, but the writer could have cited it for availability.
- **Pointers confirmed against the filed units:**
  - PB1: §1 labels; §4 Y10/Y11 thresholds and views (§5 wrongly added; finding 4); D1 rows Y1, Y10, Y11; D2 cap of 150 USD, microphone 99.00 USD, clamp up to 40 USD, hours log; D3 stop rule, read 6 (dashboard), checkpoint dates.
  - PB3 §5 (no follower-to-list rate; beehiiv Free) and D2 (10-hour plan).
  - PB4 §1 voice notes and stills.
  - PB5 §2 (audio passed, line unspent) and §10 (clamp only).
  - PB6 D1 R8 (no Shorts) and YT10.
  - PB8: §2 (Eisend; "how many sponsored pieces… which PB9 takes up"); §6.1 (CMA own-brand rule); §6.5; §7 (lawyer for the first contract); D1 clause 7; register A1–A3, T1–T3, E3–E5.
  - PB8 clause 3: overstated (findings 12, 14).
- **Carried from PB1 (outside this unit).** PB1 §4 and D1 row Y10 carry the same status-on-acceptance wording as finding 3 ("keep their status, provided they accept…"). I propose a correction row for PB1.

## (7) Figures

1. **flow, §1: FIX** (finding 2).
   - Traced: "day one; no platform threshold" ← §1 "Lines you open yourself, on day one… need no audience threshold"; "programme's or brand's terms" ← §1; "no threshold published; the professional dashboard shows eligibility" ← §2 "the place an Instagram account reads its own eligibility is the professional dashboard"; "1,000 subscribers + 8,000 watch hours in 365 days for new applicants from 1 Feb 2027" ← §2.
   - Not traced: "in 12 months". The text says "in the last year".
   - Caption: names the section and the sources. Kind: a sequence, so flow fits.
   - Instagram's place in the order between affiliate links and YouTube's 500 tier is not set by any text. It is harmless, and I made no finding.
2. **range, §8: PASS.**
   - Lows and highs 0–5, 4–13, 16–32, 84–117 and points 2, 8, 24, 100 ← §8 item 3 ("0 to 5 sales when 2 are expected, 4 to 13 when 8 are, 16 to 32 when 24 are, and 84 to 117 when 100 are").
   - Caption: names §8, NIST and the derivation; 2, 8 and 24 ← D2 V6.
   - Kind: an interval per row, so range fits.
3. **bars (stacked), D3: PASS.**
   - Values 26.00, 104.00, 312.00, 255.00 ← D3 table rows "Own digital product (net of Gumroad's fee) | 26.00 | 104.00 | 312.00" and "Brand deals | 0.00 | 0.00 | 255.00"; caption totals ← "**Total, USD** | **26.00** | **104.00** | **567.00**".
   - Caption: names D3, Gumroad, Collabstr and Mara's labels.
   - Kind: numbers compared by scenario, so bars fits.
4. **decision, D4: FIX** (finding 16).
   - Questions ← §10 steps 1–4 and D4's rule paragraph ("needs no stock bought ahead, takes its hours from a named cut, covers its own cash costs in the low scenario, and adds no more than one labelled piece per season"); outcomes ← §8 ("Made-to-order, print-on-demand or pre-order") and D4.
   - Caption: its last sentence contradicts D1 and D4.
   - Kind: a rule with branches, so decision fits.

Both fixed figures were rendered with kit-viz/viz.py without error.

## (8) Writer's notes

**Source errors ("none")**
- Confirmed: the 1 Feb 2027 thresholds; the 500 tier; 10M Shorts; 13429240's 4,000-hour route; vidIQ 137,355 and 272 and the 40–55% band; Instagram's page stating no threshold; Facebook's 10,000; beehiiv Free $0 to 2,500; the CMA and FTC lines; Eisend; Artificial Ignorance 121 of 13,413 (1 Jan 2025); Generalist World "43,000 newsletter subscribers and 700+ paying members" (6 Jan 2026); AIR 300 channels, May 2025–May 2026; Patreon's article giving neither $52 nor $110.
- **Not confirmed:** "the terms-acceptance condition … held". The page says acceptance does not affect status ("If you are already in YPP, your status is not impacted by this update"), so the condition as the unit and PB1 word it is a source error (finding 3).
- Not checked: Substack's page and answer 72851.

**Contradiction 1: Q2 Instagram counts. Confirmed.**
- The register's PB7 entry contains "27 Reels and 12 carousels in Q1, 25 and 14 in Q2". PB1 D3 read 1 contains "(7 or 6 videos; 39 posts)". PB7 IR1 gives Q1 only.
- All four cut windows (25 Apr–6 Jun 2027) produce posts inside Q2, which ends 4 Jul. 25 − 8 = 17 Reels, and 17 + 14 = 31 posts.
- The proposed replacement strings are exact and coherent.

**Contradiction 2: PB1 D2 money. Confirmed as a proposal.**
- PB1 D2 has a Contingency row to insert before.
- The microphone line is 99.00 USD and unspent (PB5 §2, §10). The clamp is up to 40 USD.
- CTT's 58,00 € VAT-excluded annual concession for individuals (Nov 2020) is confirmed.
- The note rightly leaves the converted current price unchecked.

## (9) Part 5, line by line

1. Sourced where made: **met**. Recommendations are marked **(her rule)** with a basis.
2. Source types: **met**, with three exceptions. Inro and EMARKETER are secondary or unsourced, labelled so and kept out of the model. NIST is a reference for the arithmetic. The CTT tariff is the provider's own price list.
3. Anecdote, vendor and correlational labels: **met**.
4. Platform named for growth, format and metric claims: **met** (Collabstr per platform; Li Instagram and Douyin; Agentio YouTube; YouTube vs Instagram eligibility).
5. Claims carried over re-verified: **not met** in one place. The YPP status wording carried from PB1 does not match the page (finding 3).
6. No private-course reader or reference: **met**. A grep for the source course's names and terms finds nothing. `kit/private_terms.py` is not in this folder, so it was not run.
7. Mara labelled on first use, consistent with the register, never evidence: **met**. The intro and D1 carry the label. The upload, season and checkpoint dates agree. The Q2 Instagram count change is flagged in the notes.
8. Neutral ground: **met**, with one gap.
   - No rate is stated as the reader's; amounts are in source currency; "information, not legal or tax advice" (intro).
   - The gap: the EU "primary source" is the Commission's page (finding 8), and the US primary source (*Wayfair*) was not opened, which the unit says.
9. No uncited figures or invented items: **met**.
10. Changeable facts dated: **met** (13 Nov 2026 throughout; Sources dated).
11. Deliverable for Mara, then a template with described blanks: **met**.
12. Not advice without evidence: **met**.
13. Links as links: **met**, except CTT in V17 (finding 13).

## (10) The unit read as the persona

The reader has under 1,000 followers, reads in order, is sceptical and checks citations.
- The one reference only an insider would know is "The brief for this unit…" in §1 (finding 1).
- The shorthand codes are all defined in earlier units of this public course, so a reader going in order can follow them, though they are dense on a phone. They are PB8's register lines (T1, T2, T3, A1–A3, E3–E4), "clause 7", "the run-in", "cut windows", "the clamp" and "the publishing-and-replies line". A parenthetical gloss at first use would help: for example "register line T1 (registering income)" and "A3 (the national advertising authority)". These are optional, not findings.
- PB10 is named as the unit that runs the review. It is not yet written, which is acceptable for a forward pointer.

## For the main session

- A proposed correction outside this unit: PB1 §4 table and D1 row Y10 state that existing YPP channels keep their status "provided they accept the updated terms". YouTube Help 12843009 says status is not affected and only earnings from the associated features are. The same correction as finding 3 is owed in PB1, and possibly the register.
- No memory was used.

**PB9 · verdict: fix · 3 error, 5 should-fix, 10 minor**
