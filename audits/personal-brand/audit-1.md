---
audit: stratified-sample audit (Audit 1)
units: PB1, PB2, PB3, PB4
course: personal-brand · PB · Building a Personal Brand on Instagram and YouTube
model: Fable 5.2 (claude-fable-5-2; accepted by Pedro for row F-PB, 14 Nov 2026), search on
date: 2026-11-14
chat: one fresh Fable agent per unit, isolated on its packet, in session https://claude.ai/code/session_01KMmgQyKuvCKpHpSB9xzQYA (row F-PB part 1)
verdicts: PB1 PASS · PB2 PASS · PB3 PASS · PB4 PASS
---

# Audit 1 · PB · PB1, PB2, PB3, PB4

Built by script (`f-pb/tools/build_audits.py`) from each agent's `out/audit.md`, saved verbatim under `audits/personal-brand/f-pb/<code>/` before any erratum was applied. Errata applied by `f-pb/tools/apply.py`; what was applied, held and flagged is in `f-pb/applied.json`.

---

<!-- PB1: f-pb/PB1/audit.md, verbatim -->

Model: claude-fable-5-2

# PB1 · stratified-sample audit (course PB, Audit 1) · 14 November 2026 · search on

## Provenance
Fresh isolated auditor, model claude-fable-5-2. Read only /home/claude/fpb/PB1. No prior working files in out/ (new run). Web rule followed: WebSearch first, WebFetch only a URL a search in this agent returned verbatim.

## Sample (recorded before any check)
One claim per `##` section (13 sections: §1–§10, Deliverable, Sources, Unsure list); the Deliverable gives one each for D1, D2, D3; the Template carries no cited claim of its own (consistency only).

| # | Section | Claim | Source to open |
|---|---|---|---|
| S1 | §1 | Mara: 38, accountant, 0 YouTube subscribers, 140 Instagram followers, 6 h/week; day one Monday 4 January 2027; 26 videos a year, 3 feed posts a week | case-facts.md; calendar |
| S2 | §2 | vidIQ: 32,926,088 sub-1,000 channels, 500,409 crossed 1,000 in 360 days; 12–51 band 1,259,198 channels, 8.65% | vidiq.com/research/youtube-uploads-1000-subscribers/ |
| S3 | §3 | Buffer: 2.1M feed posts, 102,000 accounts, fixed effects; +0.12/0.26/0.44/0.66% | buffer.com/library/how-often-to-post-on-instagram/ |
| S4 | §4 | YouTube from 1 Feb 2027: 1,000 subscribers + 8,000 qualified watch hours in 365 days or 20M qualified Shorts views in 90 days, new creators | support.google.com/youtube/answer/12843009 |
| S5 | §5 | vidIQ frequency study: 10,210,278 channels 1,000+; 1–3 a month 0.89% views, 0.10% subscribers; "correlation, not causation" | vidiq.com/research/youtube-upload-frequency-study/ |
| S6 | §6 | Billion Dollar Boy: 1,000 US/UK creators; 52% burnout; 37% considering leaving; 40/31/27%; 55% | billiondollarboy.com/news/over-half-of-creators-face-burnout |
| S7 | §7 | Wu and Huberman: success = top 1% of views for upload week; about 21% with first video, 34.1% within first week | arxiv.org/pdf/0904.0489 |
| S8 | §8 | RØDE Wireless Micro $99.00 USD in every variant | brandstore.rode.com/products/wireless-micro |
| S9 | §9 | Pascual: first video 9 Apr 2023; 36 videos (311 minutes); 29,385 subscribers at one year | verynormal.substack.com/p/issue-14-the-statistics-of-being |
| S10 | §10 | Instagram's creator page publishes no follower thresholds for its earning tools | creators.instagram.com/earn-cash-making-what-you-love |
| S11 | Deliverable D1 (Y2) | YouTube: half of all channels and videos have an impressions CTR between 2% and 10% | support.google.com/youtube/answer/7628154 |
| S12 | Deliverable D2 | Postal address 58.00 € + VAT a year, CTT tariff, Nov 2020 | no link given in the unit |
| S13 | Deliverable D3 | YouTube Help 16559651 quotes: "has a lower click-through rate (CTR)" and "is receiving fewer impressions than usual" | support.google.com/youtube/answer/16559651 |
| S14 | Sources | Buffer entry: title "How often should you post on Instagram in 2026? What data from 2 million posts tells us" (Kirsti Lang; analysis by Julian Winternheimer), 13 Aug 2025 | buffer.com/library/how-often-to-post-on-instagram/ |
| S15 | Unsure list | Edits launched 22 Apr 2025, free, "without added watermarks" (PetaPixel) | petapixel.com/2025/04/22/... |

## Table (sampled claims)

| # | Section | Claim | Source | Verdict | Note |
|---|---|---|---|---|---|
| S1 | §1 | Mara: 38, accountant, 0 subscribers, 140 followers, 6 h/week; day one Monday 4 Jan 2027; 26 videos a year, 3 posts a week | case-facts.md; calendar | PASS | Agrees with case-facts.md (lines 7, 9, 14, 15); 4 Jan 2027 is a Monday; label "(Mara, fictional)" on first use. |
| S2 | §2 | 32,926,088 channels; 500,409 crossed; 12–51 band 1,259,198, 8.65%; 360 days; 11 Sep 2026 | https://vidiq.com/research/youtube-uploads-1000-subscribers/ | PASS | Every figure, the band table, the 360 days and the date confirmed; band counts sum to the total; 1.52% derived correctly. |
| S3 | §3 | Buffer: 2.1M feed posts, 102,000 accounts, fixed effects, +0.12/0.26/0.44/0.66%, 5,000-follower example, reach +12% | https://buffer.com/library/how-often-to-post-on-instagram/ | PASS | All four increments, the 5,000-follower example (6/13/22/33), Stories excluded, reach about 12% higher confirmed; no CI, period or band counts on the page, as the unit says. |
| S4 | §4 | From 1 Feb 2027: 1,000 subscribers + 8,000 qualified watch hours in 365 days or 20M qualified Shorts views in 90 days, new creators | https://support.google.com/youtube/answer/12843009 | PASS | Confirmed on the page titled "Changes to the YouTube Partner Program". |
| S5 | §5 | 10,210,278 channels 1,000+; Apr 2025–Mar 2026; four bands of view and subscriber growth; "correlation, not causation" | https://vidiq.com/research/youtube-upload-frequency-study/ | PASS | All four bands and the window confirmed. Page wording: "This study shows correlation, not causation."; the resources point is the page's ("may have more resources to publish frequently"). |
| S6 | §6 | Billion Dollar Boy: 1,000 US/UK creators; 52%; 37%; 40/31/27%; 55% most severe among burned out; 7 Jul 2025 | https://billiondollarboy.com/news/over-half-of-creators-face-burnout | PASS | Confirmed; the survey also covered 1,000 marketers, which the unit does not need. 55% is a severity ranking among those who burned out, as the unit says. |
| S7 | §7 | Wu and Huberman: success = top 1% of views for upload week; about 21% first video; 34.1% first week; chance declines | https://ar5iv.arxiv.org/html/0904.0489 (arXiv 0904.0489) | PASS | Opened as the ar5iv HTML of the same arXiv paper. 21.0% and 34.1% confirmed. The preprint counts 9,896,784 videos and 579,470 producers, the 2008 paper 9,896,816 and 579,471; "the same 2008 data" holds. |
| S8 | §8 | RØDE Wireless Micro $99.00 USD in every variant; receiver USB-C or Lightning | https://rode.com/products/wireless-micro (cited brandstore link not opened) | PASS | USD 99.00 for all six variants confirmed at RØDE's own site, rode.com/products/wireless-micro. The cited brandstore.rode.com link was returned by no search and was not opened (flag PB1-5). |
| S9 | §9 | Pascual: first video 9 Apr 2023; 36 videos, 311 minutes; 29,385 subscribers; alongside research; post 9 Apr 2024 | https://verynormal.substack.com/p/issue-14-the-statistics-of-being | PASS | All confirmed. |
| S10 | §10 | Instagram creator page names six tools and publishes no follower threshold | https://creators.instagram.com/earn-cash-making-what-you-love | PASS | Six tools named (Subscriptions, Partnership Ads, Creator Marketplace, Gifts, Badges, Bonuses); no follower, age or country requirement stated. |
| S11 | Deliverable D1 (Y2) | Half of all channels and videos: impressions CTR between 2% and 10%; wider under a week old or under 100 views; no target | https://support.google.com/youtube/answer/7628154?hl=en-GB | PASS | Exact sentence: "Half of all channels and videos on YouTube have an impressions CTR that can range between 2% and 10%." |
| S12 | Deliverable D2 | CTT PO box for an individual 58.00 € + VAT a year, tariff Nov 2020 | https://www.ctt.pt/application/themes/pdfs/1_tarifario_servicos_postais_1nov.pdf | PASS | Figure confirmed (58.00 €, "Preços sujeitos a aplicação de IVA", Preços 2020, November 2020). The unit gives no link and Sources has no entry: errata PB1-2, PB1-3. Current price not found by search; the unit already says it is to check. |
| S13 | Deliverable D3 | YouTube Help 16559651: title or thumbnail change when "lower click-through rate (CTR)" and "fewer impressions than usual" | https://support.google.com/youtube/answer/16559651?hl=en | PASS | Both phrases and the title-or-thumbnail advice confirmed; page title as in Sources. |
| S14 | Sources | Buffer article title, Kirsti Lang, analysis by Julian Winternheimer, 13 Aug 2025 | https://buffer.com/library/how-often-to-post-on-instagram/ | PASS | Title, author, analyst and date confirmed. |
| S15 | Unsure list | Edits: free, iOS and Android, "without added watermarks"; 22 Apr 2025 from the URL, text says "today" | https://petapixel.com/2025/04/22/instagrams-capcut-competitor-edits-is-now-available/ | PASS | Free, iOS and Android, "without added watermarks" confirmed; the text gives no calendar date, as the Unsure list says. |

## Also checked (beyond the sample, counted in the totals)

| # | Section | Claim | Source | Verdict |
|---|---|---|---|---|
| A1 | §2 | First-ten study: cohort, 137,355, 180/211/272, 1,948, 57.8%, 30.8%, Shorts 367,243 at 1,362/1,344, exclusion quote, dates | https://vidiq.com/research/youtube-first-10-videos-study/ | PASS |
| A2 | §2 | 5,330,249 vidIQ users' channels created in prior three years; seven bucket shares; 9 Jun 2025 | https://vidiq.com/blog/post/how-many-videos-to-get-1000-subscribers | PASS |
| A3 | §2 | Median gain +0.5/+1.4/+3.7 with band counts; 61,186,246 channels, 40.6% and 7.90%; 20 Jul 2026 | https://vidiq.com/research/youtube-subscriber-benchmarks-2026/ | PASS |
| A4 | §2 | Beaupré title, interview 1 Sep 2026, both quotes, no sample; article 2 Sep 2026 | https://ppc.land/subscribers-skip-90-of-uploads-in-their-feed-youtube-director-says/ | PASS |
| A5 | §3 | Socialinsider: 67,541,436 posts, about 579,000 accounts, definition quote, 2025 and 2024 rates, 131,955, both inconsistencies | https://www.socialinsider.io/blog/instagram-benchmark-study/ | PASS |
| A6 | §3 | Metricool: 24,364,803 posts, 375,118 accounts, Jan–Feb 2025 vs 2026, 21% quote, growing undefined, 16 Jun 2026 | https://metricool.com/press-release-instagram-study-2026/ | PASS |
| A7 | §4 | 500 subscribers + 3,000 hours or 3M Shorts views; unchanged; Creator Partnerships and Shopping grouped | https://support.google.com/youtube/answer/12843009 | PASS |
| A8 | §4 | Existing members: status not impacted; terms accepted by 31 Jan 2027 to keep earning from the features | https://support.google.com/youtube/answer/12843009 | PASS |
| A9 | §4 | Activity rule: 1,000 hours / 1M Shorts views / 2 long-form or 5 Shorts per 90 days; 90 days to recover | https://support.google.com/youtube/answer/12843009 | PASS |
| A10 | §4 | Shorts Creator Pool: 10M qualified Shorts views in 90 days; not removed; other earnings unaffected | https://support.google.com/youtube/answer/12843009 | PASS |
| A11 | §4 | Page does not say whether qualifying or applying decides which rule applies | https://support.google.com/youtube/answer/12843009 | PASS |
| A12 | §4 | Current rule: 1,000 + 4,000 hours in 12 months or 10M Shorts views in 90 days; review, not automatic | https://support.google.com/youtube/answer/72851?hl=en-gb | PASS |
| A13 | §6 | 27,360,211 with no net change, 0.20% crossed; uploads can be offset by removals | https://vidiq.com/research/youtube-uploads-1000-subscribers/ | PASS |
| A14 | §6 | 11,752,034 channels; median monthly growth 1.26/0.59/0.53/0.51/0.48/0.30/0.24% by band | https://vidiq.com/research/youtube-subscriber-benchmarks-2026/ | PASS |
| A15 | §6 | YouTube: "no correlation between break length and changes in views", "thousands of channels that took a break"; no sample or method | https://support.google.com/youtube/answer/141805?hl=en | PASS |
| A16 | §7 | Wu and Huberman: data cannot observe when producers stop | https://ar5iv.arxiv.org/html/0904.0489 | PASS |
| A17 | §9 | Candogan: assistant professor; 28 Jul 2023; 88 videos; 20K+, 600K+, $300+; "was viewed only 164 times"; undated | https://sidikatunccandogan.substack.com/p/first-year-as-a-youtuber | PASS |
| A18 | Deliverable D3 | YouTube: with a lot of impressions "it's natural for the CTR to be lower" | https://support.google.com/youtube/answer/7628154?hl=en-GB | PASS |
| A19 | Deliverable D3 | Stop rule base rate: 1–11 band, 1.86% crossed within 360 days | https://vidiq.com/research/youtube-uploads-1000-subscribers/ | PASS |

Arithmetic and internal checks, all correct: 1.52% (500,409 / 32,926,088); 83.1%; 91.35%; 68% and 53.5% (bucket sums; the seven buckets sum to 100.00%); about 200, 290 and 135 months at the band medians; 1,948 / 272 ≈ 7; 480,000 minutes → 87,300–120,000 views, 3,360–4,620 per video, 12–17 times 272; 32,700–45,000 views for 3,000 hours; §5 months (18.5, 32.3, 69.2; 9.2, 16.2, 34.6); 140 × 0.0026 ≈ 0.36; Y6 sample 3,332,098 = sum of three bands; upload 10 in week 19; uploads per quarter 7/6/7/6; hours sum 12.0; money sums to 150 USD; 4 Jan 2027 to 1 Feb 2027 is four weeks; review dates are Mondays at +13, +26, +39, +52 weeks.

Pointers to other units, checked in `others/`: PB10 §5 (review hour from two Reels; 39 posts in Q1, 37 in Q2–Q4, 29 in Q2 with the guide) agrees; PB9 D2 V17 (58.00 € + VAT, CTT) and D3 exist and agree; PB8 register E4 (postal address) agrees; PB5 §2 (audio check) and §10 (what not to buy) exist; PB3 §5 (email list) and PB4 (0.25 email, reply slots) agree; PB7 row IG8 reads I1, I4, I7 as PB1 states them; DD-PB1 cites PB1 §9 consistently. Mara's facts agree with case-facts.md (PB1 block, PB9 postal-address line, PB10 review hour).

## Not checked
- https://brandstore.rode.com/products/wireless-micro: returned by no search in this agent, so not fetched; the price was confirmed at https://rode.com/products/wireless-micro instead.
- WebFetch of https://vidiq.com/research/youtube-subscriber-benchmarks-2026/: one tool-permission refusal, retried once, then opened (checked).
- Not in the sample and not opened: Buffer benchmarks page, Metricool Instagram Trends and YouTube Trends, 9to5Mac, TechCrunch, Inro, Meta fan-subs, vidIQ average view duration, arXiv 0809.3030 and its library record, Cornell Chronicle, AIR Media-Tech, MarketingProfs, Your Europe, GOV.UK, IRS, YouTube Help 9228390. No verdict is given on these.
- CTT's current PO-box price: one search, nothing found; the unit already marks it "current price to check".

## Failure rate
Sampled: 15 claims, 0 FAIL, 0 STALE, 0 unverifiable: 0%. All checked: 34 claims, 0 FAIL, 0 STALE, 0 unverifiable. The one-in-ten threshold is not reached; no full audit run.

## Figures
1. §2 compare (crossing 1,000 by videos added): PASS. Four values, 32,926,088, 360 days, the source and date and the three labels are in §2's text and table.
2. §3 compare (Buffer increments): PASS. Baseline and four values, 2.1 million, 102,000, feed posts only, no confidence intervals, source and date are in §3.
3. §6 compare (median monthly growth by size): PASS. Seven values, 11,752,034, the 90 days to 20 July 2026, source and date are in §6.
4. D3 decision: PASS. Three questions and four outcomes match verdicts 1–4 word for word in substance; the caption's 1.86%, 360 days, rows Y2 and Y3, and both YouTube Help answers are in D1 and D3.

## Deliverable
Present in full: D1 (21 rows, each with platform, metric, value, source, sample, date, label and the worked column), D2 (hours 12.0 a fortnight; money cap 150 USD), D3 (stop rule, four verdicts in order, seven reads, four dated reviews), then T1–T3 with every blank saying what goes in it. It follows from the evidence: the stop rule rests on output and the 12–51 band's floor, no subscriber or follower count decides anything in year one, and unsourced rows (Y9, I7) are kept out of every rule. It can be used without the unit, with two gaps in D2's postal-address line (no link; errata PB1-2, PB1-3) and one unlabelled inference in D3's Q3 line (PB1-4). The postal-address cell is long and leans on four other units; it is correct against PB9 and case-facts but is the one cell a reader of D2 alone cannot follow.

## Course goal and sourcing standard
The unit serves the third outcome (reading numbers against sourced benchmarks to decide continue, change format or stop) and fixes the hours budget the second outcome needs. Nothing reads as advice without evidence: every rule in D3 is labelled as Mara's and tied to a sourced row; vendor, correlational, survivor, agency-survey, preprint and creator-case labels are present at each use; changeable facts are dated; tax is put as a question with EU, UK and US starting pages and the not-advice line. Breaches of Part 1 found: one cited source missing from Sources (YouTube Help 141805; PB1-1); one figure with no openable locator (CTT tariff; PB1-2, PB1-3); one inference stated as fact in the closing material (PB1-4). Sources lists nothing the unit does not cite.

## Counts
Words: 10,979 (`wc -w unit.md`). `##` sections: 13. Cited claims in the unit: 148, counted by script with this rule: outside `viz` blocks, Sources, the Unsure list and the template, one for each data table row that carries a number and a source, and one for each sentence carrying a number or a quotation inside a paragraph or bullet that cites a link, "same source", a § reference or a sheet row. Per section: §1 0 · §2 25 · §3 13 · §4 17 · §5 11 · §6 10 · §7 4 · §8 8 · §9 4 · §10 1 · Deliverable 55. Web: 21 searches, 23 fetch calls (22 opened, 1 permission refusal that opened on retry).

## Verdict
**PB1 · PASS.** 0 of 15 sampled claims failed (0 of 34 checked in all); no full audit run. Three should-fix citation errata, one minor erratum and one flag.

## Most consequential errors
No factual error was found. The defects, in order of weight:
1. §6 quotes YouTube's own statement on breaks (Help answer 141805) but the page is missing from Sources, so the course bibliography would not collect it.
2. D2's postal-address price (58.00 € + VAT, CTT, November 2020) is right but has no link and no Sources entry; it is also a six-year-old tariff, which the unit says itself.
3. D3's Q3 line presents as fact ("the upper tail that channels crossing 1,000 come from") what §2 correctly labels an untested inference.

## Bibliography line
Add: YouTube Help, "YouTube performance FAQ & Troubleshooting" (answer 141805); CTT, "Preços 2020" tariff (November 2020). Note: RØDE's price is confirmed at rode.com/products/wireless-micro, the brandstore link unopened. Seen in search, not read, possible later source: vidIQ Research, youtube-first-week-views (September 2026). Sources to mark failed: none.

## Changelog line
2026-11-14 · PB1 · Audit 1 stratified sample (claude-fable-5-2, search on): PASS, 0/15 sampled and 0/34 checked failed; errata PB1-1 to PB1-4 (3 should-fix, 1 minor: Sources entry for YouTube Help 141805, link and Sources entry for the CTT tariff, Q3 inference labelled) and flag PB1-5 (RØDE brandstore link not opened; price confirmed at rode.com); figures 1–4 pass.

## Errata

**PB1-1** · erratum · should-fix · other · Sources
- Current: `- YouTube Help, "The YouTube Partner Programme overview and eligibility" (answer 72851), checked 12 Nov 2026. https://support.google.com/youtube/answer/72851?hl=en-gb`
- Fix: `- YouTube Help, "The YouTube Partner Programme overview and eligibility" (answer 72851), checked 12 Nov 2026. https://support.google.com/youtube/answer/72851?hl=en-gb` then, on a new line, `- YouTube Help, "YouTube performance FAQ & Troubleshooting" (answer 141805), checked 12 Nov 2026. https://support.google.com/youtube/answer/141805?hl=en`
- Basis: §6 cites YouTube Help answer 141805 with a link, but Sources does not list it (sourcing standard Part 1: every source the unit cites is listed). Page title and the quoted sentence confirmed 14 Nov 2026 at https://support.google.com/youtube/answer/141805?hl=en

**PB1-2** · erratum · should-fix · other · Deliverable · D2
- Current: `58.00 € + VAT a year (CTT tariff, Nov 2020; current price to check)`
- Fix: `58.00 € + VAT a year ([CTT, Preços 2020, tariff of November 2020](https://www.ctt.pt/application/themes/pdfs/1_tarifario_servicos_postais_1nov.pdf), Apartados, Singulares, concessão anual; current price to check)`
- Basis: The amount is right (58.00 €, prices subject to VAT, tariff dated November 2020) but D2 gives no locator a reader can open and Sources has no entry (Part 1: sourced where made, source can be opened). Confirmed 14 Nov 2026 at https://www.ctt.pt/application/themes/pdfs/1_tarifario_servicos_postais_1nov.pdf

**PB1-3** · erratum · should-fix · other · Sources
- Current: `- Cornell Chronicle, "What social media creators can't say about their job" (Nguyen and Duffy, *New Media & Society*, 7 Jul 2026), 8 Jul 2026. https://news.cornell.edu/node/333256`
- Fix: `- Cornell Chronicle, "What social media creators can't say about their job" (Nguyen and Duffy, *New Media & Society*, 7 Jul 2026), 8 Jul 2026. https://news.cornell.edu/node/333256` then, on a new line, `- CTT, "Preços 2020" (tariff of postal services, November 2020; Apartados, Singulares, concessão anual). https://www.ctt.pt/application/themes/pdfs/1_tarifario_servicos_postais_1nov.pdf`
- Basis: Sources entry for the tariff D2 cites (goes with PB1-2). https://www.ctt.pt/application/themes/pdfs/1_tarifario_servicos_postais_1nov.pdf

**PB1-4** · erratum · minor · other · Deliverable · D3 (Q3 review)
- Current: `Above the median is the upper tail that channels crossing 1,000 come from.`
- Fix: `Above the median is the upper half of her band; that channels crossing 1,000 come from its upper tail is an inference no dataset found tests (§2).`
- Basis: The sentence states as fact what §2 labels "An inference, which no dataset found tests", and "above the median" is the upper half, not the upper tail; closing material may add no unsourced claim (Part 1). vidIQ Subscriber Benchmarks gives band medians only: https://vidiq.com/research/youtube-subscriber-benchmarks-2026/

**PB1-5** · flag · minor · other · §8; Deliverable · D2; Sources
- Current: `[RØDE brand store](https://brandstore.rode.com/products/wireless-micro)`
- Fix: `No text change proposed here. The cited link brandstore.rode.com/products/wireless-micro was returned by no search in this audit (nor in the fresh check), so it was not opened; the same price, USD 99.00 for every variant, was confirmed on 14 Nov 2026 at https://rode.com/products/wireless-micro. Replacing the link in §8, D2 and Sources would also touch the 12 Nov 2026 check date held in case-facts.md, so it is left to the maintainer.`
- Basis: https://rode.com/products/wireless-micro (USD 99.00, six variants, receiver USB-C or Lightning), 14 Nov 2026

Each Current was counted with `grep -c -F` in unit.md: 1 for PB1-1, PB1-2, PB1-3, PB1-4 and for the flag PB1-5.

---

<!-- PB2: f-pb/PB2/audit.md, verbatim -->

Model: claude-fable-5-2

# Stratified-sample audit · PB2 · Positioning: the sentence a stranger can repeat · 14 November 2026 · search on

## Provenance

- Auditor: one fresh, isolated agent, model claude-fable-5-2. Read only `/home/claude/fpb/PB2`; wrote only `out/`. No memory, past-chat, Projects, connector, Artifact, Agent or `mcp__` tool used.
- Unit: `unit.md` (PB2, written 2026-11-12 by Opus 5.5, front matter `search: off`). Not edited.
- Web rule followed: WebSearch first; WebFetch only on a URL a search in this agent returned verbatim.
- `out/` was empty at the start: no earlier run to resume.

## Sample (recorded before any check)

One claim per `##` section (9 sections).

| # | Section | Sampled claim | Source the unit cites |
|---|---|---|---|
| S1 | §1 | Camerer, Loewenstein and Weber named the "curse of knowledge"; markets reduced it by "approximately 50 percent" without removing it; JPE 97(5), 1989, 1232–1254 | IDEAS/RePEc record |
| S2 | §2 | OverseerOS: 1,620 long-form videos with 1M+ views from 163 channels with five or more such videos; 97.5% of channels had a different topic query for every video; median most-repeated entity in 20.0% of winners; quote "Successful channels repeated a recognizable world…"; 21 Aug 2026 | OverseerOS article |
| S3 | §3 | With five people, one answer moves the result by 20 percentage points (derived: 1 of 5); the reason for strangers is sourced, the five / ten minutes / four of five are conventions | derived; Camerer et al. |
| S4 | §4 | YouTube handle: changeable twice within a 14-day period; previous handle held 14 days, both URLs work, then "Afterward, the handle will become available for other users to select" | YouTube Help 15920820 (and 11585688) |
| S5 | §5 | YouTube channel description: 1,000 characters in the Data API; "accessible in the channel header" | YouTube Data API Channels; YouTube Help 2657964 |
| S6 | Deliverable | D3 bio is 111 characters including line breaks, against a third-party limit of 150 (Bitly) | script count; Bitly |
| S7 | Template | T4 "Handle: … 3–30" characters | YouTube Help 11585688 |
| S8 | Sources | Thomson, "Human brands: investigating antecedents to consumers' strong attachments to celebrities", *Journal of Marketing* 70(3), 2006, 104–119 | library record |
| S9 | Unsure list | Instagram name-change rule "twice every 14 days" and old username "may become available for others to claim" rest on SocialBee, 27 Apr 2026, modified 5 Nov 2026 | SocialBee |

## Table (sample)

| # | Section | Claim | Source | Verdict | Note |
|---|---|---|---|---|---|
| S1 | §1 | "Curse of knowledge"; markets reduced it by "approximately 50 percent" without removing it; JPE 97(5), 1989, 1232–1254 | https://ideas.repec.org/a/ucp/jpolec/v97y1989i5p1232-54.html ; wording confirmed in the paper itself, https://www.cmu.edu/dietrich/sds/docs/loewenstein/CurseknowledgeEconSet.pdf | PASS | Authors, journal, volume, issue, year, pages hold. The abstract reads "reduce the curse by approximately 50 percent but do not eliminate it". The unit's limit ("economic judgments, not profiles") is right. |
| S2 | §2 | OverseerOS: 1,620 videos, 163 channels, 1M+ views, five or more per channel, English, long-form; 97.5%; 20.0%; the "recognizable world" quote; limits; 21 Aug 2026 | https://www.overseeros.com/blog/stick-to-one-niche-youtube | PASS | Every figure, the date, the author and both quotations hold. The limits are the article's own (no failed channels, machine-extracted labels, "Correlation Is Not Causation"). "Vendor of YouTube analytics tools" fits how the site describes itself. |
| S3 | §3 | Five people: one answer moves the result by 20 percentage points (derived: 1 of 5); the number, delay and pass mark are conventions | derived; Camerer et al. (S1) | PASS | 1/5 = 20 points. The unit says in the text and in the figure caption that the five, the ten minutes and four of five are unsourced conventions. |
| S4 | §4 | YouTube handle: twice within a 14-day period; previous handle held 14 days; both URLs work; "Afterward, the handle will become available for other users to select" | https://support.google.com/youtube/answer/15920820 | PASS | All four points verbatim on the page (the sentence continues "as their handle"). |
| S5 | §5 | Channel description: 1,000 characters in the Data API; "Your description is accessible in the channel header" | https://developers.google.cn/youtube/v3/docs/channels?hl=en ; https://support.google.com/youtube/answer/2657964 | PASS | "The property's value has a maximum length of 1000 characters" (snippet.description and brandingSettings.channel.description). Help sentence verbatim; the Help page states no limit, as the unit says. Opened as the search returned it, without `?hl=en`. |
| S6 | Deliverable | D3 bio is 111 characters including line breaks; third-party limit 150 | script count; https://bitly.com/blog/instagram-character-limit/ | PASS | Recounted: 111. Bitly: "The Instagram bio character limit is 150 characters." It cites no Instagram page, as the unit says. |
| S7 | Template | T4 handle "3–30" characters | https://support.google.com/youtube/answer/11585688?hl=en | PASS | "between 3-30 characters"; the Han/Hangul 1–10 and Ethiopic/Hiragana/Katakana 2–20 exceptions in §4 hold too. |
| S8 | Sources | Thomson, "Human brands…", *Journal of Marketing* 70(3), 2006, 104–119 | https://bvbvf1.bib-bvb.de/vufind/PrimoRecord/cdi_proquest_journals_227781169 | PASS | Author, title, journal, volume, issue, year (July 2006), pages hold. |
| S9 | Unsure list | Instagram display-name rule "twice every 14 days" and old username "may become available for others to claim" rest on SocialBee, 27 Apr 2026, modified 5 Nov 2026 | https://socialbee.com/blog/how-to-change-your-name-on-instagram/ | PASS | Both wordings, the author (Roxana) and both dates hold; they are SocialBee's statements, labelled third-party in the unit. |

## Also checked (beyond the sample; counted in the totals)

| # | Section | Claim | Source | Verdict | Note |
|---|---|---|---|---|---|
| A1 | §1 | Both Ries and Trout wordings, as quoted from Graham Mann's notes | https://grahammann.net/book-notes/positioning-al-ries-jack-trout | PASS | Verbatim. The page gives 1981 and no publisher; "McGraw-Hill" was not checked here. The unit says the book was not opened. |
| A2 | §2 | YouTube tips: both quotations; no effect sizes, no ranking | https://support.google.com/youtube/answer/13615784?hl=en | PASS | Verbatim, under the returning-viewer tips. |
| A3 | §2, §5 | Mosseri, 25 Aug 2021: search matches "usernames, bios, captions, hashtags and places"; handle, profile name and bio advice | https://about.instagram.com/blog/announcements/break-down-how-instagram-search-works/ | PASS | Quote verbatim; the advice is paraphrased fairly (the bio tip also mentions locations). |
| A4 | §2 | Beaupré's two quotations, via Search Engine Journal, 4 Mar 2024 | https://www.searchenginejournal.com/youtube-algorithm-myths-debunked-insights-from-the-growth-team/510091/ | PASS | Both verbatim; author and date hold. The unit marks its own inference from them as untested. |
| A5 | §2 | Aaker and Keller: "a perception of 'fit' between the two product classes", high quality of the original brand; CiteDrive year 2018 in error | https://www.citedrive.com/en/discovery/consumer-evaluations-of-brand-extensions/ | PASS | Abstract wording and the 2018 error hold. Volume and pages (54(1), 27–41) are not on this record and were not re-checked. |
| A6 | §2 | Bottomley and Holden, JMR 38(4), 2001, 494–500; original plus seven replications; both quotations | https://researchers.mq.edu.au/en/publications/do-we-really-know-how-consumers-evaluate-brand-extensions-empiric/ | PASS | All hold. |
| A7 | §2 | Net Influencer, 4 Mar 2026: "himself learning a new skill as quickly as possible"; the second channel Mike Boyd Climbs, no numbers | https://www.netinfluencer.com/learning-in-public-how-mike-boyd-built-a-sustainable-youtube-business-on-curiosity/ | PASS | Quote verbatim; author Dragomir Stojkov; the reason for the second channel and the absence of numbers hold. |
| A8 | §2 | Laughing Squid, 30 Dec 2016 (Lori Dorn): the six skills of the 2016 round-up | https://laughingsquid.com/a-recap-of-everything-mike-boyd-taught-himself-to-quickly-learn-in-2016/ | PASS | Violin, lock, Rubik's Cube under two minutes, reverse-steering bicycle, juggling, unicycle ("among other things"). |
| A9 | §2 | The round-up is "titled" "A round up of 2016's 'Learn Quick'" | same page | FAIL (minor) | The page quotes "A round up of 2016's "Learn Quick". What will you learn in 2017?" as a line under the embedded video. It does not say this is the video's title, and its own headline is different. "Titled" is not supported. Erratum PB2-1. |
| A10 | §2 | vidIQ, Mike Boyd: created 23 Oct 2008; 2.93 million subscribers; 197 videos; 477,008,214 views on 11 Nov 2026 | https://vidiq.com/youtube-stats/channel/@mikeboyd/ | PASS | Join date, subscribers and video count hold. The page now reads 477,016,889 views, updated 13 Nov 2026; the unit's figure is dated 11 Nov and is a snapshot, so no change. |
| A11 | §2 | Rosetta: nine 2019 titles with "30 days"; sugar 12 Feb 2019; breathwork 10 Dec 2019; zone 2 on 30 Mar 2026 | https://rosetta.to/u/mattdavella/2019 ; https://rosetta.to/u/mattdavella/i-quit-sugar-for-30-days ; https://rosetta.to/u/mattdavella/i-tried-zone-2-training-for-30-days-what-i-learned | PASS | Nine counted; titles and all three dates hold. |
| A12 | §2 | vidIQ, Matt D'Avella: created 25 Jul 2011; 4.06 million subscribers; 472 videos on 5 Nov 2026 | https://vidiq.com/youtube-stats/channel/@mattdavella/ | PASS | All hold; the page is still dated 5 Nov 2026. |
| A13 | §2 | Michelle Khare: "award-winning docuseries Challenge Accepted"; "tackled the world's toughest professions and stunts"; 5.43 million, undated | https://michellekhare.com/about | PASS | Both phrases and 5.43M on the page; no date beyond a © 2026 footer. |
| A14 | §2 | Thomson: three studies; both quotations | library record (S8) | PASS | Verbatim in the abstract; three studies. |
| A15 | §4 | YouTube handle rules: allowed characters, none at start or end, not case-sensitive, one per channel, "already being used", "are distinct from channel names" | https://support.google.com/youtube/answer/11585688?hl=en | PASS | All hold. |
| A16 | §4 | Channel name: "You can change your channel name twice within a 14-day period"; "Changing your name will remove your verification badge" | https://support.google.com/youtube/answer/2657964 | PASS | Both verbatim. |
| A17 | §4, §5 | Data API: channel title 30 characters (brandingSettings.channel.title); keywords 500 in total | https://developers.google.cn/youtube/v3/docs/channels?hl=en | PASS | Both hold; snippet.title states no maximum. The page calls keywords "a space-separated list of strings"; D4 writes them with commas, which the unit does not source. Observation, no erratum. |
| A18 | §4 | Instagram Help: "periods, numbers, underscores or abbreviations"; no limit or release rule stated | https://help.instagram.com/513717858639392 | PASS | Sentence verbatim; the page gives no limit and no rule on old usernames. |
| A19 | §4 | SocialBee: up to 30 characters for username and display name | https://socialbee.com/blog/how-to-change-your-name-on-instagram/ | PASS | "Instagram allows up to 30 characters for both your username and your display name." |
| A20 | §4, Sources | Bitly: username 30; Daniel Wiersema; 19 Dec 2023, updated 29 Sep 2026; no Instagram source | https://bitly.com/blog/instagram-character-limit/ | PASS | All hold. |
| A21 | Deliverable | Counts: sentence 29 words; expansion 60 words; name field 26; description 841; handles 17, 21, 9; names 19, 23, 9; keywords 152 of 500 | script in this audit | PASS | All recounted and equal. 4 Jan 2027, 5 Apr 2027 and 7 Dec 2026 are Mondays. |
| A22 | §1, Deliverable | Mara's facts against `case-facts.md` | register | PASS | Base facts, PB1's cadence and dates, and every "Set by PB2" line agree; the handle is provisional in both. |
| A23 | whole unit | Pointers to PB1 §1 (labels), PB3 (audience), PB4 (series), PB6, PB7 (formats; sending a viewer to YouTube, §9), PB8 (trademark §6.7 for EU, UK, US; disclosure; other people's image §6.2), PB10 (run 2 at the review) | `others/` | PASS | Each pointed-to unit does what PB2 says it does. |

## Not checked

- No URL was refused, redirected or timed out, and no tool call was refused for permission.
- Not attempted: Aaker and Keller's pages 27–41 at the DOI (the unit reads the abstract on CiteDrive; the fresh check confirmed the pages elsewhere); "McGraw-Hill" as the 1981 publisher; whether any of the five handles is in use (no tool here can open the two apps; the unit and the register both say so).
- https://help.instagram.com/182492381886913 (returned by a search, opened to look for an Instagram-stated username limit): the page served no article text. The unit's statement that no Instagram page found states the limit stands unchanged.

## Failure rate

- Sample: 9 claims, 0 FAIL, 0 STALE, 0 unverifiable. Failure rate 0 in 9 (0%). The one-in-ten rule is not triggered; no full audit run.
- All claims checked: 32 (9 sampled, 23 also checked): 31 PASS, 1 FAIL (minor), 0 STALE, 0 unverifiable.

## Counts

- Words: 8,183 (`wc -w unit.md`). `##` sections: 9.
- Cited claims in the unit: 65, tallied by section (a sentence or table row resting a number, date, quotation, attribution or mechanism on a cited source counts once; a sentence citing two sources for two facts counts twice; summary restatements in the grades and in "What no source shows" are not counted again):
  - §1: 3 (Ries and Trout attribution; Mann's two quotations; Camerer et al.)
  - §2: 23 (topic 8; method 10; person 5)
  - §3: 1 (the reason for strangers, by back-reference)
  - §4: 13 (handles "distinct"; 7 table rows; 3 in "Three things follow"; 2 in the availability steps)
  - §5: 5
  - Deliverable: 4 (the limits cited in D3 and D4)
  - Template: 7 (the limits in T2, T3, T4)
  - Sources: 0 (24 reference entries; each matches a link in the body and none is uncited)
  - Unsure list: 9

## Figures

1. Matrix, §2: PASS. Every cell traces to §2's text; the caption names its sources; the legend's three marks cover every tone used.
2. Flow, §3: PASS. Seven steps equal §3's steps 1 to 7; the caption marks the conventions as unsourced.
3. Decision, D2: PASS. The override question, both outcomes, the handles in the caption and the order of fallbacks equal D2's text.

## Deliverable

Present in full: D1 (sentence and 60-word expansion), D2 (three options, the checks, the pick, the override, the conditions), D3 (username, name field, bio), D4 (name, handle, description, keywords), D5 (the script, scoring, pass mark, what to do on a fail), then the template T1 to T5 with every blank saying what goes in it. It follows from §1 to §5, adds no unsourced claim about the world, states what was not checked (the handles, the trademark), and can be used without the body. Every count in it is right.

## Course goal and standard

- Goal: the unit delivers the first outcome (one sentence saying who the account is for and what it gives) and puts it into both profiles.
- Standard: claims are sourced where made; vendor, third-party, anecdote and survivor labels are applied; platforms are named; conventions are marked as unsourced; the trademark question is left to PB8 with "information, not legal advice".
- Advice without evidence: none that decides anything. Two small unsourced lines remain, neither in the deliverable as a claim: §4 step 3, "viewers will confuse the two" (a reason given without a source), and D4's comma-separated keywords (the Data API describes a space-separated list). Reported as observations, no errata.
- Front matter says `search: off` while the unit states search was used on 12 Nov 2026 to check its sources; the unit explains this in its first paragraph. No change proposed.

## Verdict

**PB2: PASS.** Sample 0 FAIL in 9; no full audit run. One minor erratum from the wider check.

## Most consequential errors

1. §2 calls a line that Laughing Squid quotes under Mike Boyd's video the video's title. The page does not say it is the title. Nothing in the unit's argument depends on it.

No other error found.

## Bibliography line

No source to mark failed. Optional addition: the paper itself for Camerer, Loewenstein and Weber (https://www.cmu.edu/dietrich/sds/docs/loewenstein/CurseknowledgeEconSet.pdf), which carries the exact "approximately 50 percent" wording.

## Changelog line

2026-11-14 · PB2 stratified-sample audit (Audit 1, PB) · claude-fable-5-2 · PASS: 9 sampled, 0 FAIL; 32 checked in all, 1 minor FAIL (Laughing Squid "titled"), 0 STALE, 0 unverifiable; 3 figures PASS; 1 erratum (PB2-1), no flags.

## Errata

**PB2-1** · minor · FAIL · §2, The method or repeatable format (creator cases)

- Current: `and his 2016 round-up, titled "A round up of 2016's 'Learn Quick'", covered`
- Fix: `and his 2016 round-up video, which the page quotes as "A round up of 2016's 'Learn Quick'", covered`
- Basis: the Laughing Squid page prints "A round up of 2016's "Learn Quick". What will you learn in 2017?" as a quoted line under the embedded video and does not call it the title; its own headline is "A Recap of Everything Mike Boyd Taught Himself to Quickly Learn in 2016". https://laughingsquid.com/a-recap-of-everything-mike-boyd-taught-himself-to-quickly-learn-in-2016/
- `grep -c -F` on Current: 1.

---

<!-- PB3: f-pb/PB3/audit.md, verbatim -->

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

---

<!-- PB4: f-pb/PB4/audit.md, verbatim -->

Model: claude-fable-5-2

# Stratified-sample audit · PB4 The content system · 14 November 2026 · search on

## Provenance
Fresh, isolated auditor (claude-fable-5-2). Read only `/home/claude/fpb/PB4`; wrote only `out/`. No earlier working files were in `out/`; this is a first run. Web rule followed: WebSearch first, WebFetch only on URLs a search in this agent returned verbatim.

## Sample (recorded before any check)
One claim per `##` section (11 sections).

| # | Section | Sampled claim | Source cited |
|---|---|---|---|
| S1 | §1 | Ruan et al.: speech 2.93× keyboard for English (153 v 52 wpm); pooled English+Mandarin 5.30% v 11.22% corrected, 1.30% v 0.79% left; IMWUT 1(4), Dec 2017 | arXiv 1608.07323 |
| S2 | §2 | AIR Media-Tech, 8 Jun 2026: 18,000 English-language channels (US, UK, CA, AU), primary analysis 100k–1M monthly views; "Channels that went dark for 14+ days three or more times a year got fewer views per video"; "This is correlational data, not causal" | air.io (posting study) |
| S3 | §3 | Buffer, 13 Aug 2025: 2.1M feed posts, 102,000 accounts, fixed effects; +0.12% (1–2 posts), +0.26% (3–5) weekly follower growth v none; reach per post about 12% higher at 3–5 than 1–2 | buffer.com/library/how-often-to-post-on-instagram/ |
| S4 | §4 | Dai, Milkman and Riis, Management Science 60(10), 2014, 2563–2582: "diet" searches, gym visits, commitments rise after temporal landmarks ("the outset of a new week, month, year, or semester; a birthday; a holiday"); "relegate past imperfections to a previous period" | EconPapers record |
| S5 | §5 | Gollwitzer and Sheeran 2006: meta-analysis of 94 independent tests; "the when, where, and how of goal striving in advance"; medium-to-large effect, d = .65; AESP 38, 69–119 | KOPS record |
| S6 | §6 | Masicampo and Baumeister, JPSP 101(4), 2011, 667–683: unfinished goals caused intrusive thoughts in a reading task and hurt an anagram task; "formulate specific plans for their unfulfilled goals" eliminated the effects; "Once a plan is made, the drive to attain a goal is suspended" | BVB library record |
| S7 | §7 | PB3 set the cut order: Instagram three to one (frees 1.0 h); replies to next week; video to about 8 minutes (frees an estimated 1.0 h); upload moved up to 7 days, once; log never cut (PB3, D2) | others/PB3 D2 |
| S8 | Deliverable | D2: every week 1–12 sums to 6.0 (72.0 total); upload 7 public Tuesday 30 March 2027, so Q1 holds seven uploads "as PB1's Q1 review expects (uploads 1–7)"; review Monday 5 April 2027 | arithmetic; others/PB1 D3; case-facts |
| S9 | Template | T2: PB3's 3-hour plan is one anchor every four weeks, one Instagram post a week, one email per anchor, 11.75 h per four weeks; the unit's four weeks sum 3.0, 3.0, 3.0, 2.75 | others/PB3 D2; arithmetic |
| S10 | Sources | Monsell, Sumner and Waters, "Task-set reconfiguration with predictable and unpredictable task switches", Memory & Cognition 31(3), 2003, 327–342, at orca.cardiff.ac.uk/33842 (and the §5 quotation it carries) | ORCA record |
| S11 | Unsure list | "PPC Land dates the FAQ's publication to 2 Sep 2026 in the German Help Centre" (YouTube performance FAQ, answer 141805) | PPC Land |

## Table (sample)

| Section | Claim | Source | Verdict | Note |
|---|---|---|---|---|
| §1 | S1 Ruan et al. speech v keyboard | https://www.arxiv.org/abs/1608.07323?context=cs and the arXiv PDF | PASS | Abstract: "2.93 times faster (153 vs. 52 WPM)" for English; 5.30% v 11.22% corrected, 1.30% v 0.79% uncorrected. The paper's per-language rates (English 3.93 v 4.72 and 0.55 v 0.35; Mandarin 6.67 v 17.73 and 2.06 v 1.22) average to the abstract's figures, so "across English and Mandarin together" holds. IMWUT 1(4), Dec 2017; v1 25 Aug 2016, v2 17 Jan 2018. The recogniser was Baidu Deep Speech 2, a 2015 publication; "2016 recognisers" is loose, not wrong enough to fix. |
| §2 | S2 AIR Media-Tech, posting study | https://air.io/en/audience-growth/does-posting-more-on-youtube-help-we-studied-18000-channels-to-find-out | PASS | Dated 8 Jun 2026; 18,000 English-language channels, US, UK, Canada, Australia (India excluded); primary analysis at 100K–1M monthly views; both quotations exact; the schedule finding is views per subscriber at the same number of videos. The page gives no effect size or method for that finding, which the unit's "vendor, correlational" label covers. |
| §3 | S3 Buffer posting frequency | https://buffer.com/library/how-often-to-post-on-instagram/ | PASS | Kirsti Lang, 13 Aug 2025; 2.1 million posts, 102K accounts; photos, Reels, carousels, Stories excluded; fixed-effects model; +0.12% and +0.26% against no-post weeks; about 12% more reach per post at 3–5 than at 1–2. The 0.14-point step and 140 × 0.0014 ≈ 0.2 are correct. |
| §4 | S4 Dai, Milkman and Riis | https://econpapers.repec.org/RePEc:inm:ormnsc:v:60:y:2014:i:10:p:2563-2582 | PASS | Management Science 60(10), 2014, 2563–2582; both quotations exact; searches for "diet" (Study 1), gym visits (Study 2), commitments (Study 3); three archival field studies. |
| §5 | S5 Gollwitzer and Sheeran | https://kops.uni-konstanz.de/entities/publication/2e749bfb-8533-437c-8203-7e788c910c5f | PASS | AESP 38, 2006, 69–119; "94 independent tests"; "the when, where, and how of goal striving in advance"; "medium-to-large magnitude (d= .65)". |
| §6 | S6 Masicampo and Baumeister | https://bvbvf1.bib-bvb.de/vufind/PrimoRecord/cdi_proquest_miscellaneous_918752704 | PASS | JPSP 101(4), 2011, 667–683, doi 10.1037/a0024192; intrusive thoughts in a reading task (Studies 1, 5B), anagram task (Study 4); both quotations exact. |
| §7 | S7 PB3's cut order | others/PB3 D2 | PASS | PB3 D2 steps 1–4 and "Never cut: the log" match, with the hours freed (1.0; estimated 1.0). PB3's step 2 frees "up to 0.6 hours", which the unit omits without changing the order. |
| Deliverable | S8 D2 sums, upload 7, Q1 review | script; others/PB1 D3; case-facts.md | PASS | Run-in 4.25, 1.5, 5.25, 5.75; weeks 1–12 each 6.0; total 72.0. Every date and weekday checked by script. PB1 D3: "Q1 review, Monday 5 April 2027 · YouTube uploads 1–7". Upload dates match the register. |
| Template | S9 T2 rules for 3 hours | others/PB3 D2; arithmetic | PASS | PB3's 3-hour column: 2.0, 4.0, 1.0, 2.0, 1.5, 0.25, 1.0 = 11.75. The unit's four weeks sum 3.0, 3.0, 3.0, 2.75 and rebuild every PB3 line exactly. |
| Sources | S10 Monsell, Sumner and Waters | https://orca.cardiff.ac.uk/33842 | PASS | Memory & Cognition 31(3), 2003, 327–342; quotation exact; digit high/low and odd/even tasks. |
| Unsure list | S11 PPC Land and the FAQ's date | https://ppc.land/youtube-finds-no-link-between-upload-breaks-and-view-counts/ | FAIL | PPC Land (2 Sep 2026) dates a German-language recommendations FAQ posted that day in the German YouTube Help community forum, not the Help Centre. The performance FAQ is one of two accompanying Help Centre pages, for which it gives only a 2026 footer year. The unit's line moves the date onto the wrong document and the wrong place. Erratum PB4-1. |

## Also checked

| Section | Claim | Source | Verdict | Note |
|---|---|---|---|---|
| §1 | Instagram original content guidelines | https://creators.instagram.com/original-content-guidelines/ | PASS | All three quotations exact; "low-effort edits (e.g. borders, watermarks, speed changes, just crediting the original creator)"; no date but a 2026 footer. |
| §1 | Instagram, 30 Apr 2026, Reels to photos and carousels | https://techcrunch.com/2026/04/30/instagram-restricts-reach-of-content-aggregators-in-new-crackdown/ | PASS | "these protections were already in place for reels, and are now being applied to photos and carousels". |
| §1 | Shiffman, Stone and Hufford, abstract | https://citedrive.com/en/discovery/ecological-momentary-assessment | PASS | "Assessment in clinical psychology typically relies on global retrospective self-reports"; "recall bias"; "maximize ecological validity". Year 2008, volume and pages stay unconfirmed (see Not checked). |
| §2 | YouTube Help 13615784, two quotations | https://support.google.com/youtube/answer/13615784?hl=en | PASS | Both exact. |
| §2 | YouTube Help 141805, breaks | https://support.google.com/youtube/answer/141805?hl=en | PASS | Three quotations exact; no sample size, period, method or page date. |
| §2 | vidIQ, 12–51 band | https://vidiq.com/research/youtube-uploads-1000-subscribers/ | PASS | Bands 0, 1–11, 12–51, 52+; 8.65% in the 12–51 band; published 11 Sep 2026. The title the unit gives is not the page's (errata PB4-3, PB4-4). |
| §2 | Tasty Edits rule of thumb | https://www.tastyedits.com/how-long-does-it-take-to-edit-a-video/ | PASS | Quotation exact; 19 May 2021, updated 17 Sep 2026; no method or sample; 5 to 10 hours for 10 minutes is correct. |
| §3 | AIR Media-Tech, Shorts study | https://air.io/en/audience-growth/do-youtube-shorts-help-your-long-form-videos-grow-data-from-18000-channels | PASS | 28 May 2026; 18,000 English-language channels; March 2025 to March 2026; quotation exact; "this is correlational data". |
| §3 | Fanpage Karma format reach | https://www.fanpagekarma.com/insights/instagram-format-reach/ | PASS | 7 Aug 2026, modified 28 Aug 2026; more than 3 million posts, January to April 2026; 4.9%, 3.5%, 2.6%; quotation exact; no account count. |
| §3 | Socialinsider: figures "do not match its own 45% headline" | https://www.socialinsider.io/blog/how-long-does-it-take-for-reels-to-get-views/ | FAIL | Two samples: confirmed (40M Reels from 450K accounts; 25,503,389 Reels). The mismatch is not there: the page gives about 14,578 views by day 10 and "just above 8,000" at day 20, a fall of about 45%, which is what "After 10 days ... decreasing by 45%" says. The 17,100 to 14,578 fall (about 15%) is the period before day 10. What the page lacks is a stated end point. Erratum PB4-2. |
| §3 | TechCrunch, 8 Nov 2022 | https://techcrunch.com/2022/11/08/instagram-scheduling-tool-all-professional-accounts | PASS | Title as listed; all professional accounts; "posts, reels and carousels"; "up to 75 days in advance". |
| §3 | Social Media Today, 1 Mar 2026 | https://www.socialmediatoday.com/news/instagram-opens-up-content-scheduling-to-all-users/813448/ | PASS | First sentence: creator tools "available to all public accounts"; scheduling, the insights dashboard and trending audio are listed among them; no quoted Instagram statement; no horizon. |
| §4 | Kivetz, Urminsky and Zheng | https://business.columbia.edu/faculty/research/goal-gradient-hypothesis-resurrected-purchase-acceleration-illusionary-goal | PASS | JMR 43, Feb 2006, 39–58; three quotations exact; the head-start card is the 12-stamp card with two bonus stamps. |
| §4 | YouTube Help series quotations | answers 13615784 and 141805 (URLs above) | PASS | All three exact; the second continues ", or work with the same host". |
| §5 | Rubinstein, Meyer and Evans via APA release | https://www.newswise.com/articles/is-multitasking-more-efficient | PASS | 5 Aug 2001; JEP:HPP 27(4); young adults, four experiments; quotation exact; less familiar tasks cost more; maths problems and classifying geometric objects. |
| §5 | Leroy 2009 | https://econpapers.repec.org/RePEc:eee:jobhdp:v:109:y:2009:i:2:p:168-181 | PASS | OBHDP 109(2), 168–181; two experiments; unfinished task; finishing not sufficient; time pressure. The source has "people" in lower case (erratum PB4-5). |
| §5 | APA, "40 percent" | https://www.apa.org/topics/research/multitasking | PASS | 20 Mar 2006; quotation exact; attributed to Meyer; no study cited. |
| §3 | 0.2 followers a week and PB1 I4's 0.36 | others/PB3 §6; others/PB1 §3, D1 I4 | PASS | Both as the units give them. |
| §1 | PB1 D2 capture quotation; PB3 D2 "24.0 of 24" | others/PB1 D2; others/PB3 D2 | PASS | Exact. |
| §1 | PB2 D4 promise quotation | others/PB2 D4 | PASS | Exact. |
| Template | T2 rules for 10 hours | others/PB3 D2; arithmetic | PASS | 9.75 a week, 39.0 per four weeks, each PB3 line rebuilt; override weeks 10.0 and 8.0; PB3's override and cut order as stated. |
| §7 | PB1 verdict 2 and the 7-hour line | others/PB1 D2, D3 | PASS | "over 7 hours in 3 or more weeks of the quarter"; "A week over 7 hours is logged as over budget". |
| Unsure list | CiteDrive dates Shiffman et al. 2007, no volume | https://citedrive.com/en/discovery/ecological-momentary-assessment | PASS | Year 2007; journal, volume and pages not shown. |
| Deliverable | D2 run-in: PB5 D A 0.75 h; PB2 D5 run 1 | others/PB5 D A; others/PB2 D5 | PASS | PB5: 0.5 to R1 (4.25), 0.25 to R2 (1.5). PB2: run 1 in the week of 7 December 2026. |
| §1 | Cadence rule from PB10 §5 | others/PB10 §5 | PASS | "two or more pieces in a quarter took more than two weekends, in two consecutive quarters". |
| §2 | YouTube Help 1270709 (scheduling; strike penalty period) | https://support.google.com/youtube/answer/1270709?hl=en | unverifiable | Not opened: see Not checked. |
| §3 | Instagram Help scheduling page summary | https://help.instagram.com/iphone-app/439971288310029 | unverifiable | Not opened: see Not checked. |

Other pointers read and found to hold, not counted as claims: PB1 §1 (labels), §7, §8; PB1 D3 (stop rule; verdict 3 from Q2; Q2 review uploads 8–13); PB3 §3, §4, §5, §6; PB5 §1 (one clip per step); PB10 §5 and §8 (two Reels fewer; recovery weeks at 6.5).

## Not checked

- `https://support.google.com/youtube/answer/1270709?hl=en`: WebSearch was refused (the session's search budget, shared by every agent, was used up); retried once, refused again. No search returned the URL, so the web rule barred fetching it.
- `https://help.instagram.com/iphone-app/439971288310029`: same refusal; not fetched.
- `https://pubmed.ncbi.nlm.nih.gov/18509902/` (Shiffman et al.: year, volume, pages): fetched once, the page returned no article content; not retried. The unit's Unsure list already carries this.
- WebSearch: 22 searches ran; three more were refused for the budget reason above. 33 fetches ran.
- Quotations were confirmed through the fetch tool's short verbatim extracts, not by reading whole pages.

## Failure rate

Sample: 1 FAIL in 11 (9.1%). That is not more than one in ten, so the full audit was not triggered. All checks: 38 claims, 34 PASS, 2 FAIL, 0 STALE, 2 unverifiable. 24 of the unit's 26 listed sources were opened.

## Counts

Words (`wc -w`): 10,438. `##` sections: 11. Cited claims in the unit: 111 (48 resting on an outside source, 63 on a named unit of the course). Counted by reading, one per sentence or table row; the 26 entries of the Sources list are references and are not counted.

| Section | Outside source | Other unit | Total |
|---|---|---|---|
| §1 | 4 | 10 | 14 |
| §2 | 8 | 3 | 11 |
| §3 | 8 | 2 | 10 |
| §4 | 4 | 4 | 8 |
| §5 | 6 | 0 | 6 |
| §6 | 1 | 3 | 4 |
| §7 | 1 | 10 | 11 |
| Deliverable | 4 | 19 | 23 |
| Template | 3 | 9 | 12 |
| Sources | 0 | 0 | 0 |
| Unsure list | 9 | 3 | 12 |
| **Total** | **48** | **63** | **111** |

## Figures

1. §2 matrix, "Three pieces in the system at once": PASS. Piece 3 is captured in weeks 1–2 (9 and 16 Jan), edited and cut in weeks 3–4 (24 and 31 Jan) and published in week 5 (2 Feb); pieces 4 and 5 follow a fortnight apart, as D2 has them. "6 posts" is §3's. The caption names §2 and D2.
2. §7 decision, "A lost week: what moves": PASS. Each outcome is in §7's two bullets; the caption's summary of PB3 D2 and PB1 D2's 7-hour line is correct. The 6.5 h in two outcomes is the unit's own figure (see flag PB4-6).
3. §7 stacked bars: PASS. Week A 6.0 and week B 6.0 match D1 E line by line; both recovery rows sum to 6.5 and match §7 (edit 3.0, packaging 1.0, two posts 1.0, scheduling 0.25, capture 1.0, log 0.25). The 0.25 under "Publish, replies" in the recovery rows is scheduling alone (flag PB4-6).

## Deliverable

D1, D2, T1 and T2 are present in full. D1 and D2 follow from the body: every line names its section or unit, the hours table matches PB1 and PB3, and every sum and date is right. T1 and T2 can be filled without the body; each blank says what goes in it, and the 3- and 10-hour rules rebuild PB3's totals exactly. Mara's facts agree with `case-facts.md` (week pattern, run-in, upload dates, seasons, backlog, piece rules, lost-week rules).

One gap, reported as a flag: the 6.5-hour recovery weeks leave out the recovery week's own reply slots. With them the week after a lost week A is 6.75 hours, and the week after a lost week B is 7.0, which is at PB1's line and not under it. The unit never says the slots are dropped.

## Course goal and standard

The unit serves the second outcome directly: it gives a publishing system and a twelve-week calendar inside a 6-hour budget, and hands PB10 the log and the rules its reviews read. Evidence and inference are kept apart: transfers from other settings are marked as the unit's inference, conventions as "her rule", and §4 and §5 say what the evidence does not support. Nothing reads as advice without evidence.

Three observations that need no erratum:
- The header says `search: off`, but the unit dates live platform facts to 12 Nov 2026 and adds sources no earlier unit carries. The six-month staleness check should treat it as a search-on unit.
- Tasty Edits is not one of Part 5's source types. The unit labels it weak and keeps it out of the deliverable as evidence.
- The unit is 10,438 words against the brief's 2,000–6,000 range. About 5,980 words are body (§1–§7, figures included); the rest is deliverable, template, sources and notes.

## Verdict

PB4: **PASS**. Sample failure rate 1 in 11; full audit not run. Two errata on claims (one should-fix, one minor), three minor citation errata, one flag.

## Most consequential errors

1. §7 and D1 F: the recovery weeks after a lost week are given as 6.5 hours, but only if that week's reply slots are skipped, which the unit does not say. Counted, the week after a lost cut window is 7.0 hours, at the over-budget line. This is the one finding that touches the reader's own calendar (flag PB4-6).
2. §3: the unit says Socialinsider's figures contradict its own 45% headline. They do not: day 10 to day 20 on the page is a fall of about 45%. The source is still weak, for other reasons the unit also gives (PB4-2).
3. Unsure list: PPC Land's 2 Sep 2026 date belongs to a German forum FAQ on recommendations, not to the Help Centre performance FAQ the unit quotes (PB4-1).

## Bibliography

No source to mark failed. Retitle vidIQ's 11 Sep 2026 study to "Reaching 1,000 YouTube Subscribers: What 32.9 Million Channels Reveal" (PB1 uses the same wrong label). To add only if the Unsure list is to link what it names: PPC Land, "YouTube finds no link between upload breaks and view counts", 2 Sep 2026, https://ppc.land/youtube-finds-no-link-between-upload-breaks-and-view-counts/. Two sources not opened in this audit: YouTube Help 1270709 and the Instagram Help scheduling page.

## Changelog

Audit 1 · PB4 · 14 Nov 2026 · claude-fable-5-2 · PASS: sample 1 FAIL in 11, 38 claims checked (34 PASS, 2 FAIL, 2 unverifiable), three figures pass; 5 errata (1 should-fix, 4 minor) and 1 flag (recovery-week reply slots).

## Errata

**PB4-1** · minor · FAIL · Unsure list
- Current: `PPC Land dates the FAQ's publication to 2 Sep 2026 in the German Help Centre, and the English page's own date was not seen`
- Fix: `PPC Land (2 Sep 2026) reports a German-language recommendations FAQ posted that day in the German YouTube Help community forum, with the performance FAQ as an accompanying Help Centre page that it does not date, and the English page's own date was not seen`
- Basis: PPC Land places the dated FAQ ("FAQ: Wie funktionieren die Empfehlungen?") in the German YouTube Help community forum; the performance FAQ is one of two accompanying Help Centre pages with only a 2026 footer year. https://ppc.land/youtube-finds-no-link-between-upload-breaks-and-view-counts/

**PB4-2** · should-fix · FAIL · §3
- Current: `whose page gives two different samples and day-by-day figures that do not match its own 45% headline`
- Fix: `whose page gives two different samples and does not say what period its 45% fall after day 10 covers`
- Basis: the page gives about 14,578 views by day 10 and "just above 8,000" at the 20-day mark, a fall of about 45% (derived), so its figures do not contradict the headline; it states no end point for the 45%. PB3 §3 calls the same page unclear without claiming a mismatch. https://www.socialinsider.io/blog/how-long-does-it-take-for-reels-to-get-views/

**PB4-3** · minor · other · Sources
- Current: `- vidIQ Research, "Uploads and reaching 1,000 subscribers", 11 Sep 2026. https://vidiq.com/research/youtube-uploads-1000-subscribers/`
- Fix: `- vidIQ Research, "Reaching 1,000 YouTube Subscribers: What 32.9 Million Channels Reveal", 11 Sep 2026. https://vidiq.com/research/youtube-uploads-1000-subscribers/`
- Basis: the page's headline, published September 11, 2026; the quoted phrase appears nowhere on it. PB1 carries the same label; change both together. https://vidiq.com/research/youtube-uploads-1000-subscribers/

**PB4-4** · minor · other · §2
- Current: `[vidIQ, Uploads and reaching 1,000 subscribers, 11 Sep 2026]`
- Fix: `[vidIQ, Reaching 1,000 YouTube Subscribers, 11 Sep 2026]`
- Basis: as PB4-3. https://vidiq.com/research/youtube-uploads-1000-subscribers/

**PB4-5** · minor · other · §5
- Current: `found that "People need to stop thinking about one task`
- Fix: `found that "people need to stop thinking about one task`
- Basis: the abstract has the words mid-sentence in lower case; quotation marks hold the source's exact words. The fresh check noted it and proposed no fix. https://econpapers.repec.org/RePEc:eee:jobhdp:v:109:y:2009:i:2:p:168-181

**PB4-6** · flag · should-fix · other · §7 (also D1 F, both §7 figures, `case-facts.md`, PB10 §8)
- Current: `With capture 1.0 and the log 0.25 that week is 6.5 hours.`
- Fix (a suggestion; needs a decision): `With capture 1.0 and the log 0.25 that week is 6.5 hours, its own reply slot skipped (PB3's step 2); with the slot kept it is 6.75, and the recovery week after a lost week B, which has two reply slots, is 7.0.`
- Basis: D1 E gives week B one reply slot (0.25) and week A two (0.5). §7's 6.5 hours counts neither, and the unit says only that replies "wait for the next slots". With the slots, the weeks are 6.75 and 7.0; 7.0 is at PB1's line, not under it (PB10 §8). The 6.5 figure is also in the register, PB10 §8 and both §7 figures, so it is not applied as an erratum. Internal arithmetic; no URL.
