---
audit: fresh check
unit: PB1 · What to expect: odds, timeline, cost
course: personal-brand · PB · Building a Personal Brand on Instagram and YouTube
model: Opus 5.5 (claude-opus-5-5, as the agent states; this session keeps no agent transcript on disk, so the model could not be confirmed from a transcript's "model" field; live search). A Fable 5.1 fresh check of PB1 is owed to the Fable stage (P49)
date: 2026-11-12
chat: own Opus 5.5 agent context, not shown the writing (P31), launched by the W-PB1 chat (which ran on Opus 5.5 and only staged, applied, filed and published) in session https://claude.ai/code/session_01KMmgQxN77fE9zvQ2PYwtZy
verdict: fix · 1 error, 6 should-fix, 7 minor
---

The checker's final report, verbatim, from its hand-back in the chat (the harness refused its write to its own `out/report.md`, as its first note says, so the hand-back is the record; the harness's indentation of the hand-back is removed). Saved before any finding was applied.

Model: claude-opus-5-5

Note: the harness refused the write to /home/claude/packets/PB1-check/out/report.md because subagents may not write report files, so that file does not exist. The full report is below.

# PB1 · fresh check · What to expect: odds, timeline, cost

Checked 12 Nov 2026 by a fresh agent (claude-opus-5-5) that read only /home/claude/packets/PB1-check/. Search was live. I fetched only URLs that a WebSearch in this agent had returned verbatim. All 15 Current strings occur exactly once in unit.md (counted with Python `str.count`). All four viz blocks render with tools/viz.py, and so does the replacement for figure 4.

## (1) Coverage

| Brief item | Status |
|---|---|
| Expectation on YouTube and Instagram at 12, 24, 36 months, from the largest datasets, each with sample, date, label | Covered. YouTube at 12 months: §2 and D1 Y1–Y8. At 24 and 36 months the unit says plainly that no dataset exists (end of §2, §10). Instagram: §3 and rows I1–I4 and I7; no data exists for 12/24/36 months and the rows are marked unsourced. |
| Milestones and what each unlocks, with monetisation thresholds as the platforms state them, dated | Covered (§4 table, checked 12 Nov 2026). The condition for existing members under the 2027 Partner Programme change is incomplete (finding 2). |
| Months to each milestone at different posting rates, or a plain statement where no data exists | Covered (§5 table, derived; Instagram stated as unsourced). |
| The plateau and why most accounts stop there | Covered (§6). |
| Who continues | Covered. Thin by necessity, and §7 says so. |
| Cost in hours and money of a phone-only setup | Covered (§8). |
| Survivor bias in creator cases and how to read around it | Covered (§9, with a six-point checklist). |
| What no dataset measures | Covered (§10). |
| Deliverable: expectation sheet worked for Mara at 6 h/week; hours-and-money budget; stop rule, checkpoint dates and what is read at each; then templates | Covered (D1, D2, D3, T1–T3). |

## Findings

[error] [figure] §6; Current: "On YouTube, median monthly subscriber growth among channels that added videos falls from 1.26% at 1–99 subscribers to 0.51% at 1,000–9,999 and 0.24% above a million"; Problem: the §6 compare figure shows 0.59 (100–499), 0.53 (500–999), 0.48 (10,000–99,999) and 0.30 (100,000–999,999), and its caption gives 11,752,034 channels. None of these numbers appears in the unit's text, so the figure adds facts. The text also says "above a million" where the source band is "1 million or more". The values themselves are correct at the source; Fix: "On YouTube, among the 11,752,034 channels with at least one subscriber and a net increase in video count in the 90 days to 20 July 2026, median monthly subscriber growth falls with size: 1.26% at 1–99 subscribers, 0.59% at 100–499, 0.53% at 500–999, 0.51% at 1,000–9,999, 0.48% at 10,000–99,999, 0.30% at 100,000–999,999 and 0.24% at 1 million or more"; Basis: vidIQ, YouTube Subscriber Benchmarks 2026, 20 Jul 2026, https://vidiq.com/research/youtube-subscriber-benchmarks-2026/

[should-fix] [accuracy] §4 table, row for 1 Feb 2027 entry; Current: "The same entry, for new creators; channels already in the programme keep their status"; Problem: YouTube makes existing members' status conditional on accepting the updated terms in YouTube Studio by 31 January 2027 (Help page 72851: to keep fully monetising they must review and accept the updated terms by that date). This is the writer's own Source error 2. notes.md says PB1 "now carries the corrected text", but unit.md does not; Fix: "The same entry, for new creators; channels already in the programme keep their status, provided they accept the updated terms in YouTube Studio by 31 January 2027, without which they stop earning from the affected features from 1 February 2027"; Basis: https://support.google.com/youtube/answer/12843009 ; https://support.google.com/youtube/answer/72851?hl=en-gb

[should-fix] [accuracy] §8 Hours; Current: "place 6 hours inside the commonest reported range in that survey"; Problem: the source reports only one range ("37% say they spend five to ten hours per week creating content, on average"), so it cannot show that this range is the commonest; Fix: "place 6 hours inside the one range that survey reports"; Basis: https://www.marketingprofs.com/charts/2026/54489/the-creator-landscape-in-2026-content-monetization-and-ai-trends

[should-fix] [style] §9; Current: "nobody publishes "my first year: 31 subscribers" with the same reach"; Problem: the quotation marks hold words no source uses (Part 1 requires quoted words to be the source's exact words), and "nobody publishes" is an unsourced claim; Fix: "first years that end with a few dozen subscribers are rarely written up and shared as widely, and no source found counts them"; Basis: sourcing-standard Part 1

[should-fix] [label] §2 What the numbers say together; Current: "The channels that reach 1,000 are ones where a few uploads do far better than the rest, which matches the first-ten study, where the median best video had about seven times the views of the median tenth upload (derived: 1,948 against 272)."; Problem: no cited dataset shows that the channels which cross 1,000 are the ones with a few outlier uploads. The first-ten study measures how views concentrate within a survivor cohort, not which channels cross. The sentence states an inference as a finding; Fix: "An inference, which no dataset found tests: the channels that reach 1,000 are likely to be ones where a few uploads do far better than the rest. The first-ten study shows that kind of concentration, with the median best video at about seven times the views of the median tenth upload (derived: 1,948 against 272)."; Basis: https://vidiq.com/research/youtube-first-10-videos-study/ ; https://vidiq.com/research/youtube-uploads-1000-subscribers/

[should-fix] [figure] D3 decision figure, question node; Current: "{"label": "no", "to": {"q": "From Q2: CTR under 2% or APV under its band on 3 or more uploads?""; Problem: "CTR" and "APV" do not appear in the unit's text, and APV is never defined. The text of verdict 3 says "click-through under 2% or percentage viewed under its band"; Fix: "{"label": "no", "to": {"q": "From Q2: click-through under 2% or percentage viewed under its band on 3 or more uploads?""; Basis: unit.md D3 verdict 3

[should-fix] [figure] D3 decision figure, caption; Current: ""caption": "Mara's stop rule and verdicts from the deliverable, §D3 (Mara, fictional). The thresholds are her own rules; the base rates behind them are in §2 and §5 (vidIQ, 11 Sep 2026: the 1–11 videos band crossed 1,000 at 1.86% a year) and §4 (YouTube Help, impressions CTR: half of channels and videos sit between 2% and 10%; vidIQ guidance, 21 Jul 2026, for APV bands). Subscriber count is not a branch in year one.""; Problem: the YouTube Help click-through range is not in §4; it appears only in D1 row Y2, so the caption names the wrong section. It also uses the undefined "APV"; Fix: ""caption": "Mara's stop rule and verdicts from the deliverable, §D3 (Mara, fictional). The thresholds are her own rules; the base rates behind them are in §2 and §5 (vidIQ, 11 Sep 2026: the 1–11 videos band crossed 1,000 at 1.86% a year) and the expectation sheet D1, rows Y2 (YouTube Help, impressions click-through rate: half of channels and videos sit between 2% and 10%) and Y3 (vidIQ guidance, 21 Jul 2026, for percentage-viewed bands; also §4). Subscriber count is not a branch in year one.""; Basis: unit.md §4, D1 Y2, Y3; https://support.google.com/youtube/answer/7628154?hl=en-GB

[minor] [attribution] D1 row Y1; Current: "| 28 Jul 2026 | Vendor; survivor sample |"; Problem: the study page was updated on 30 Jul 2026. §2 and the Sources list give that date; the sheet does not (the writer's Source error 3); Fix: "| 28 Jul 2026, updated 30 Jul 2026 | Vendor; survivor sample |"; Basis: https://vidiq.com/research/youtube-first-10-videos-study/

[minor] [attribution] §6 second bullet; Current: "Duffy and Nguyen, in *New Media & Society*"; Problem: Rosie Nguyen is the first author; Fix: "Nguyen and Duffy, in *New Media & Society*"; Basis: https://news.cornell.edu/node/333256

[minor] [attribution] Sources; Current: "(Duffy and Nguyen, *New Media & Society*, 7 Jul 2026)"; Problem: same author order; Fix: "(Nguyen and Duffy, *New Media & Society*, 7 Jul 2026)"; Basis: same

[minor] [accuracy] §7 third bullet; Current: "a January 2026 survey of 1,000 creators by The Influencer Marketing Factory"; Problem: the sample is "1,000 creators based in the United States", which matters for a reader who may live in any country; Fix: "a January 2026 survey of 1,000 US-based creators by The Influencer Marketing Factory"; Basis: MarketingProfs URL above

[minor] [accuracy] D1 row B1; Current: "| 1,000 creators | Jan 2026 fieldwork |"; Problem: same; Fix: "| 1,000 US-based creators | Jan 2026 fieldwork |"; Basis: same

[minor] [accuracy] §4 after the table; Current: "requires 10,000 followers or 250 return viewers for a Facebook Page"; Problem: the page also requires either 50,000 post engagements or 180,000 watch minutes in the last 60 days; Fix: "requires 10,000 followers or 250 return viewers, plus 50,000 post engagements or 180,000 watch minutes in the last 60 days, for a Facebook Page"; Basis: https://creators.facebook.com/tools/fan-subs

[minor] [label] §6 second bullet; Current: "financial instability was the top factor (55%)"; Problem: the 55% ranks financial instability by severity among creators who burned out. It is not a frequency, so it cannot be compared with the three cause percentages before it; Fix: "financial instability was ranked the most severe factor (55%)"; Basis: https://billiondollarboy.com/news/over-half-of-creators-face-burnout

## Confirmed

The writer's unsure list, checked first:
- Unsure 1, Buffer's frequency figures read as points added to the weekly growth rate: PASS. Buffer's own 5,000-follower example (about 6, 13, 22 and 33 extra followers a week, at an assumed 0% baseline) fits that reading. The page gives no model specification, no confidence intervals and no study period. https://buffer.com/library/how-often-to-post-on-instagram/
- Unsure 2, Metricool's 21% with "growing" undefined and absent from the longer report: PASS. https://metricool.com/press-release-instagram-study-2026/ ; https://metricool.com/instagram-trends/
- Unsure 3, Socialinsider's period and exclusion inconsistencies: PASS. https://www.socialinsider.io/blog/instagram-benchmark-study/
- Unsure 4, Buffer benchmarks page gives two samples (273,000/27M and 250,000/30M) and no period; updated 8 Nov 2026: PASS. https://buffer.com/social-media-benchmarks/instagram
- Unsure 5, no Instagram earning-tool thresholds: PASS. Instagram's creator page names six tools and states no requirement for any of them. Inro (updated 23 Jul 2026) says "Meta's own documentation is not consistent on this". https://creators.instagram.com/earn-cash-making-what-you-love ; https://www.inro.social/blog/instagram-subscriptions
- Unsure 6, Instagram Live rule: PASS from 9to5Mac (1 Aug 2025; the change was unannounced and Instagram confirmed it to TechCrunch). The TechCrunch page confirms the rule, but its fetched text carries no date, so the Sources entry "Aug 2025" for TechCrunch is unverifiable. https://9to5mac.com/2025/08/01/new-instagram-rule-cuts-off-live-broadcasts-for-small-accounts/ ; https://techcrunch.com/?p=3033252
- Unsure 7, the YouTube page is silent on whether qualifying or applying decides which rule applies: PASS. https://support.google.com/youtube/answer/12843009
- Unsure 8, Journal of Information Science 35(6), 2009, 758–765, with no DOI: PASS. https://bvbvf1.bib-bvb.de/vufind/PrimoRecord/cdi_proquest_miscellaneous_743151960
- Unsure 9, Candogan's post is undated (about July 2024): PASS. https://sidikatunccandogan.substack.com/p/first-year-as-a-youtuber
- Unsure 10, Edits launched 22 Apr 2025 as a free iOS/Android download that exports "without added watermarks": PASS. https://petapixel.com/2025/04/22/instagrams-capcut-competitor-edits-is-now-available/

Other claims:
- vidIQ First 10 Videos Study: all PASS. Cohort definitions, 137,355 long-form channels with live streams excluded; medians 180/211/272; best of first ten 1,948; 57.8% and 30.8%; Shorts cohort 367,243 at 1,362/1,344; the exclusion quote is exact; published 28 Jul 2026, updated 30 Jul.
- vidIQ uploads study: all PASS. 32,926,088 channels; 500,409 crossed (1.52%); the band table; all three quotes; groups not matched; uploads can be offset by removals; 11 Sep 2026.
- vidIQ 2025 study of video counts at 1,000 subscribers: PASS. 5,330,249 vidIQ users' channels created in the prior three years; the bucket shares; the derived 68% and 53.5% are correct; 9 Jun 2025.
- vidIQ Subscriber Benchmarks: PASS. +0.5/+1.4/+3.7 a month with band counts summing to 3,332,098; 61,186,246 channels, 40.6% and 7.90%; 1.26%, 0.51% and 0.24%. The derived ~200, 290 and 135 months are correct.
- vidIQ Upload Frequency Study: PASS. 10,210,278 channels; April 2025 to March 2026; all four bands; the correlation and resources caveats; 8 Jul 2026.
- vidIQ average view duration guidance: PASS. 40–55% for 5–15 minutes and 30–45% for 15–30 minutes, labelled "vidIQ guidance", no sample, updated 21 Jul 2026. The derived 87,300–120,000 views a year, 3,360–4,620 per video, 12–17 times 272, and 32,700–45,000 for fan funding are all correct.
- Metricool YouTube: PASS. 799,718 videos, 71,177 accounts; 9.59, 16.01, 7.01, 2.11 and 10.08%; window "during the period", undefined; 29 Jul 2026.
- Metricool Instagram: PASS. 24,364,803 posts, 375,118 accounts, Jan–Feb 2025 against Jan–Feb 2026; 16 Jun 2026; quote exact.
- Socialinsider: PASS. 67,541,436 posts, about 579,000 accounts; growth definition; 2025 rates 22, 20.29, 17.20, 13.62 and 11.25% against 2024's 38–27%; 131,955 accounts in the smallest band.
- Buffer: 7.5% and 261 PASS. Frequency study details PASS: 2.1M feed posts, 102K accounts, Stories excluded, fixed effects, the four increments, reach about 12% higher, 13 Aug 2025. The derived 0.36 followers a week is correct.
- Beaupré: quotes, title and the 1 Sep 2026 interview date PASS; PPC Land article 2 Sep 2026.
- YouTube Help 9228390 (50 subscribers, verified channel, no restriction in 90 days) PASS. 72851 (current thresholds; meeting them leads to review, approval not automatic) PASS. 12843009 (8,000 hours or 20M Shorts views; the 500/3,000/3M tier unchanged, with Creator Partnerships and Shopping; activity rule; 90-day window) PASS apart from finding 2. 7628154 PASS.
- Huberman, Romero and Wu: PASS. 9,896,816 videos, 579,471 uploaders, data to 30 Apr 2008, quotes exact (https://arxiv.org/pdf/0809.3030).
- Wu and Huberman: PASS. 21.0% and 34.1%; success declines with each upload; stopping is not observed.
- Billion Dollar Boy: PASS. 1,000 US/UK creators; 52%, 37%; 40/31/27%; 7 Jul 2025.
- Cornell: PASS apart from author order. Data counts 58/62/78; "unspeakable"; the "If I take a break…" line is a recurrent theme in creator interviews, relayed by Duffy.
- AIR Media-Tech: PASS. 18,000 channels; quotes exact; correlational; no effect size; primary segment 100K–1M monthly views; 8 Jun 2026.
- Pascual: PASS. 9 Apr 2023; 36 videos, 311 minutes; 29,385 subscribers; research alongside.
- Candogan: PASS. Assistant professor; 28 Jul 2023; 88 videos; 20K+, 600K+, $300+; "164 times".
- Your Europe (last checked 18 Jun 2026), GOV.UK trading-allowance page and IRS FS-2022-38 (hobby income must be reported): PASS.
- RØDE Wireless Micro at USD 99.00 for every variant: confirmed at https://rode.com/products/wireless-micro. The cited brandstore.rode.com link was never returned by a search, so it is unverifiable and was not fetched.
- Dates and arithmetic: PASS. 4 Jan 2027 is a Monday. 5 Apr, 5 Jul and 4 Oct 2027 and 3 Jan 2028 are Mondays at +13/26/39/52 weeks. The quarterly upload split is 7/6/7/6, and upload 10 falls in week 19. Hours sum to 12; money sums to 150.

## (3) and (4)
Every number in the body names its source, and arithmetic is marked "derived". The vendor, correlational, survivor-sample, agency-survey, preprint, peer-reviewed and creator-case labels are present at each use. Exceptions: the §2 inference and the Billion Dollar Boy severity wording, both listed as findings.

## (5) Deliverable
Present in full and usable alone: D1 (21 rows with every field the brief names), D2, D3 (stop rule, verdict order, seven reads, four dated checkpoints with what is read at each), and T1–T3 with blanks that say what goes in them. It follows from the evidence: the stop rule rests on output (the floor of vidIQ's 12–51 band), never on subscriber counts, and the unsourced Instagram rows are kept out of every rule. Defects are listed above (figure caption, B1 sample, Y1 date).

## (6) Errata
No course unit is filed, so there are no pointers to check. The pointers to PB3–PB10 and DD-PB1 agree with all-briefs.md (PB10 is a sixty-minute review with the verdicts continue, change one thing, change the format, stop). Of the source unit's audit errata that touch carried-over material, these are applied: the Metricool window is undefined, the qualifying-or-applying question is stated as unknown, the 2027 activity rule is included, and the stop rule is not applied at Q1. The exception is the terms condition for existing members (finding 2).

## (7) Figures
1. compare, §2: PASS. Every value and the 32,926,088 are in §2; the caption is complete; the kind fits.
2. compare, §3: PASS. Every value, the baseline, 2.1 million, 102,000 and "Buffer users" are in §3; the caption is complete; the kind fits.
3. compare, §6: FIX. 0.59, 0.53, 0.48, 0.30 and 11,752,034 are not in the text. Applying the [error] text fix makes the figure trace, and its JSON can stay as it is. The caption is complete and the kind fits.
4. decision, D3: FIX. Apply the two figure findings above (question node and caption). The kind fits, and the fixed JSON renders.

## (8) Writer's Source errors (notes.md)
1. "is not random": confirmed. A9 line 18 quotes it, but the page reads "This is not a random sample or a census of all YouTube channels." PB1 applies the fix.
2. 2027 rule for existing members: confirmed. Both YouTube Help pages (12843009 and 72851) require acceptance of the updated terms by 31 Jan 2027, and A9 line 160 omits it. PB1 does not carry the replacement (finding 2).
3. First-ten study date: confirmed. The page reads "Published July 28, 2026 · Updated July 30, 2026", and A9 gives 28 Jul only. PB1 applies the fix in §2 and Sources but not in D1 Y1 (minor finding).

## (9) Part 5, line by line
- Every claim with a number, mechanism or recommendation sourced where made: met, except §2 (inference), §8 ("commonest range") and §9 ("nobody publishes").
- Acceptable source types: met, with agency surveys and press reports labelled as such.
- Labels: met.
- Platform named for growth, format and metric claims: met.
- Carried-over claims re-verified: met in substance, except that the existing-member correction was not applied.
- Nothing about the private course or its reader: met (grep clean).
- Mara labelled on first use, consistent with case-facts.md, never used as evidence: met.
- Tax and legal neutrality, amounts in source currency with date, information-not-advice line: met (§8).
- No uncited or invented figures: met, apart from the invented quoted title in §9.
- Changeable facts dated: met.
- Deliverable built for Mara, then as a template: met.
- Not advice without evidence: met.
- Links given as links: met.

## (10) Persona read
No private name, employer, city, sport, business or handle appears, and there is no reference to another course; cross-references are only to this course's units. Two terms are used without a gloss: "Studio" (implicit in §4) and "Insights" (D3, Instagram's analytics). Neither is a private reference. The undefined "APV" is covered by the figure fix.

PB1 · fix · error 1 · should-fix 6 · minor 7
