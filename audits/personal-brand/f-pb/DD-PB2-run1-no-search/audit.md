Model: claude-fable-5-2

# Stratified-sample audit · DD-PB2 · Deep dive: the quit-your-job math (course PB, Audit 3)

Date: 14 November 2026. Search was on for this run but every WebSearch call was refused (the turn's shared search budget was used up), so no outside page was opened; see Not checked. One unit, one fresh agent. No earlier working files were in `out/`; this is a first run, not a resume.

## Provenance

- Auditor model: claude-fable-5-2. The unit was written by Opus 5.5 (front matter), search off, with six live verifications dated 14 Nov 2026.
- Read: `unit.md`, `brief.txt`, `sourcing-parts-1-and-5.md`, `case-facts.md`, `fresh-check-DD-PB2.md` (read so as not to re-report fixed findings; none of its verdicts is reused), and `others/` for pointers only.
- Nothing outside the folder was used as a source; no memory, past-chat, Projects, connector, Artifact, Agent or `mcp__` tool was called.

## Sample (recorded before any check)

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

| Section | Claim | Source | Verdict | Note |
|---|---|---|---|---|
| S1 · §1 | DOL COBRA guide: termination 'for any reason other than gross misconduct', reduction in hours, 18 months, premium 'cannot exceed 102 percent' | https://www.dol.gov/agencies/ebsa/about-ebsa/our-activities/resource-center/publications/workers-guide-health-benefits-cobra?lang=en | unverifiable | Not opened: WebSearch refused (budget), so no URL could be fetched under the web rule. |
| S2 · §2 | MoneyHelper: 'three to six months' essential outgoings' in instant access savings | https://www.moneyhelper.org.uk/en/savings/types-of-savings/emergency-savings-how-much-is-enough?source=mas | unverifiable | Not opened: WebSearch refused. |
| S3 · §3 | vidIQ: 8.65% of sub-1,000 channels adding 12 to 51 videos crossed 1,000 within 360 days; no 24/36-month dataset | others/PB1 §2 (lines 32-38, 62) | PASS | PB1 §2's table row '12 to 51 / 1,259,198 / 8.65%' and 'No dataset found follows a cohort of new YouTube channels for 24 or 36 months'; labels vendor, correlational match. Checked at the source the unit cites (PB1 §2); vidIQ's own page not opened. |
| S4 · §4 | Sources to open are PB8 §6.5's: Your Europe FAQ (sends to national authority), HMRC content creators, IRS Topic 554 | others/PB8 §6.5 (lines 165-173) | PASS | PB8 §6.5 gives exactly these three links, with the same URLs, and names the national tax authority as the EU source to open. The three pages themselves not opened. |
| S5 · §5 | Raffiee and Feng: NLSY79, 1994-2008, 2,198 spells, 1,093 people, 'a 33.3% decrease in the hazard of exit' | https://msbfile03.usc.edu/digitalmeasures/joe.raffiee/intellcont/Raffiee_Feng_2014_AMJ-1.pdF | unverifiable | Not opened: WebSearch refused. |
| S6 · §6 | Base row: earliest pass Mon 7 Jul 2042, 15.0 years after 5 Jul 2027 (and the ten other rows) | recomputed from D1 inputs by script, 14 Nov 2026 | PASS | All eleven rows reproduced: 7 Jul 2042 (15.01), 2 Apr 2035 (7.74), 2 Jul 2035 (7.99), 6 Apr 2043 (15.75), 4 Jan 2044 (16.50), 4 Jul 2044 (17.00), 5 Oct 2048 (21.25), 2 Oct 2051 (24.24), 1 Jan 2057 (29.49), 5 Oct 2076 (49.25), trailing-twelve-month row no date before 2100. Every weekday is a Monday. |
| S7 · Deliverable | Converted at $1.1052 per euro, ECB reference rate of 13 November 2026 | https://www.ecb.europa.eu/stats/policy%5Fand%5Fexchange%5Frates/euro%5Freference%5Fexchange%5Frates/html/eurofxref-graph-usd.en.html | unverifiable | Not opened: WebSearch refused. 13 Nov 2026 is a Friday, a day on which a reference rate can be set. |
| S8 · Template | T2/T3 formulas: T = F_s / (1 - i8); audience needed = T / i12; months = (needed - i10) / i11; date = later of income and runway dates | unit §2, §4, D2 lines 3-6, D3 lines 1-3 | PASS | Each template line is the same arithmetic as the body and Mara's build. Note: the template makes the trailing twelve months the main value of i12 and the best month the marked favourable case, where Mara's build uses the launch month as its base and the trailing year as a test; the template's order is the more cautious and its T3 'Tests' line covers both. |
| S9 · Sources | ISS, Guia pratico: subsidio de desemprego (6001 v4.72), 20 Feb 2025; p. 6 condition, p. 14 resignation | https://seg-social.pt/documents/10152/15007/6001_subsidio_desemprego/1867b682-64f2-4b1a-8f39-ca008602a16b | unverifiable | Not opened: WebSearch refused. |
| S10 · Unsure list | 'the 33.3% figure is a hazard ratio from a Cox model' | https://msbfile03.usc.edu/digitalmeasures/joe.raffiee/intellcont/Raffiee_Feng_2014_AMJ-1.pdF | unverifiable | Not opened: WebSearch refused. Wording note only: a 33.3% decrease in hazard corresponds to a hazard ratio of about 0.667; the percentage is not itself the ratio. Not raised as an erratum without the paper open. |

## Also checked (beyond the sample; counted in the totals)

All of these are claims the unit rests on a filed unit, on the register or on its own arithmetic, checked in `others/`, `case-facts.md` or by script. No outside page was open, so no outside claim was checked beyond the sample.

| # | Section | Claim | Source | Verdict | Note |
|---|---|---|---|---|---|
| 11 | §2 | PB1 §10 lists 'who continues among part-time creators with full-time jobs' | others/PB1 §10 (line 211) | PASS | Exact words; PB1 capitalises 'Who' as a list item. |
| 12 | §2 | DD-PB1 found no figure for channel income at the date any of its six creators left a job | others/DD-PB1 §3-§8, §11 | PASS | 'No income figure was re-verified' (§3), 'No income figure found' (§5); no exit-date income figure in §4, §6-§8 or §11. |
| 13 | §2 | 'No unemployment benefit follows a resignation in the three places checked (§1)' | unit §1 item 3 (its own quotations of DOL, GOV.UK, ISS) | FAIL | A stretch of what §1 reports: §1 says the US 'is decided by the state' and the UK applies a sanction of '91 days for a first one in a year' for leaving 'without a good reason'. Only the Portuguese source is reported as excluding a worker's resignation. Erratum DD-PB2-1. |
| 14 | §3 | YouTube ad share: 1,000 subscribers + 8,000 qualified watch hours in 365 days for applicants from 1 Feb 2027 | others/PB9 §2 (line 42) | PASS |  |
| 15 | §3 | Of channels that crossed, 68% had 40+ videos and 53.5% had 70+ (survivor sample, no denominator) | others/PB1 §2 (line 54) | PASS | 14.54 + 22.58 + 30.89 = 68.01; 22.58 + 30.89 = 53.47. |
| 16 | §3 | Mara's 40th upload on Tue 4 Jul 2028; 70th in year three | others/PB10 D5 (line 498) | PASS | Upload 27 on Tue 4 Jan 2028 + 13 fortnights = Tue 4 Jul 2028; Q7 covers uploads 40-46. |
| 17 | §3 | Mara at Q2: 61 subscribers, 133.0 watch hours | others/PB10 D4 (lines 450-451) | PASS |  |
| 18 | §3 | AIR Media-Tech median $2.39 per 1,000 views, Crafting & Handmade, own client channels | others/PB9 §2 (line 52) | PASS | Figure and label hold. The unit gives the amount without its date (PB9: May 2025 to May 2026); Part 5 asks for the date. Erratum DD-PB2-3 (minor). |
| 19 | §3 | Fan funding, Partnerships, Shopping at 500 subscribers + 3,000 watch hours | others/PB9 §2 (line 44) | PASS |  |
| 20 | §3 | YouTube Shopping affiliate lists 18 countries and not Portugal | others/PB9 §2 (line 54) | PASS | 18 names counted; Portugal absent. |
| 21 | §3 | Collabstr average paid $255 for YouTube in 2025, all sizes, no tier breakdown | others/PB9 §4 (line 76) | PASS |  |
| 22 | §3 | Guide on sale Tue 8 Jun 2027; three sales by 4 Jul, net USD 39.00; no new cost | others/PB10 D4 R1, R5/R8 (lines 466-467) | PASS |  |
| 23 | §3 | Paid tier rule list x 0.62% >= 10, about 1,613; list 9 at Q1, 31 at Q2; 72 quarters, 18 years | others/PB9 D2 V14; PB10 D3 (line 398), D4 (line 467) | PASS | 10 / 0.0062 = 1,612.9; (1,613 - 31) / 22 = 71.9. |
| 24 | §3 | No source gives the share of viewers or followers who join a list | others/PB3 §5 (line 161) | PASS |  |
| 25 | §3 | No dataset gives Instagram follower counts at 12, 24, 36 months from under 1,000 | others/PB1 D1 I7 (line 241); PB7 (line 251) | PASS |  |
| 26 | §4 | T1 answered Thu 18 Mar 2027 by a tax professional, without charge; lawyer's fee unpriced (V18); postal address from receipt | others/PB10 D3 R8 (line 399); PB9 D2 V18 | PASS |  |
| 27 | §5 | PB3 D2's 10-hour plan; PB1's posting-rate rows and stop rule re-read on the day of the change | others/PB3 D2 (lines 268-270) | PASS |  |
| 28 | §5 | PB8 §6.4's checklist items 1, 2 and 6 | others/PB8 §6.4 (lines 153-160) | PASS | Item 1 outside work, 2 conflict of interest and outside income, 6 restrictions after leaving. |
| 29 | §5 | PB9 §7's rule: hours from a named cut, never the cadence | others/PB9 §7 (line 116) | PASS |  |
| 30 | §6 | Pace 7.7 a month at Q1 and 12.7 at Q2; readings differ 1.65 times; income per subscriber fourteenfold | others/PB10 D3 (net 6, 8, 9), D4 (net 11, 13, 14); arithmetic | PASS | 23/3 = 7.67; 38/3 = 12.67; ratio 1.65; 0.7485 / (39/12/61) = 14.05. |
| 31 | §6 | vidIQ median for 500 to 999 subscribers, +3.7 a month | others/PB1 §2 (line 56) | PASS |  |
| 32 | Deliverable | D2: F_s EUR 1,500; T USD 1,657.80 a month, 19,893.60 a year; runway EUR 18,000; 20 months to end Feb 2029; first read Mon 2 Apr 2029; USD 1,842.00 at t = 10% | arithmetic on D1 | PASS |  |
| 33 | Deliverable | D3: 2,215 subscribers; 170 months; about September 2041; 127.5 guide sales; 36 times; 693,640 views; about 437; about 1,590 times | arithmetic on D1; others/PB9 D3; PB10 D4 YT8 | PASS | 2,214.9; 170.0; first month at T is September 2041; 127.52; 36.3; 693,640; 437.0; 1,587. |
| 34 | Deliverable | D3: 'the band medians of +0.5 and +1.4 a month for channels of her size' | others/PB1 D1 Y6 (line 228) | PASS | Figures hold. Only +0.5 (1-99) is the band of a 61-subscriber channel; +1.4 is the next band (100-499). Erratum DD-PB2-2 (minor). |
| 35 | Deliverable | D4: K about EUR 1,459 a month at the Q2 run rate of USD 45.66 (EUR 41.31) | arithmetic on D1 | PASS |  |
| 36 | Deliverable | D5: EUR 1,720 at 80%; margin EUR 20; 69.8%; 450 months; loss of EUR 430 saving | arithmetic on D1 | PASS |  |
| 37 | Deliverable | DD-PB1's prior 'Keep the job through year two'; drawn from six survivors | others/DD-PB1 Deliverable A (lines 263, 278) | PASS |  |
| 38 | Deliverable | D1 i13: PB9 D2 rows V1-V3, V8, V11, V14, V15, V16 | others/PB9 D2 (lines 193-208) | PASS |  |
| 39 | Deliverable | PB9 D3: USD 13.00 net a guide sale | others/PB9 D3 (line 214) | PASS |  |
| 40 | Deliverable | D7: reviews Mon 3 Jan 2028; cut window Sun 30 Jan 2028; 24-month review week of Mon 1 Jan 2029 moved by PB4's holiday rule | others/PB10 D5 (line 498); PB4 (lines 121, 287) | PASS | Weekdays correct. |
| 41 | intro | Evidence labels are PB1 §1's seven and PB8's two | others/PB1 §1 (lines 16-22); PB8 (line 12) | PASS |  |
| 42 | whole unit | Mara's facts agree with the register | case-facts.md, 'Set by DD-PB2' and earlier sections | PASS | Household, EUR 2,150 / 1,700 / 120 / 200 / 1,500 / 450 / 9,000, R = 12 (6), t by 3 Jan 2028, checkpoints, pass rule, USD 0.7485, 12.7, the three path dates, K, D7's reading all match. Labelled '(Mara, fictional)' on first use. |

## Not checked

- WebSearch: refused seven times (six first calls and one retry), 'this turn's web search budget is used up (limit: 200 WebSearch calls per turn, shared by every agent in it)'; no search ran
- WebFetch: not called; the web rule allows only a URL a search in this agent returned, and no search ran
- https://www.dol.gov/agencies/ebsa/about-ebsa/our-activities/resource-center/publications/workers-guide-health-benefits-cobra?lang=en: not checked, no search result to fetch from (WebSearch refused)
- https://oui.doleta.gov/unemploy/uifactsheet.asp: not checked, no search result to fetch from (WebSearch refused)
- https://www.gov.uk/guidance/universal-credit-sanctions: not checked, no search result to fetch from (WebSearch refused)
- https://seg-social.pt/documents/10152/15007/6001_subsidio_desemprego/1867b682-64f2-4b1a-8f39-ca008602a16b: not checked, no search result to fetch from (WebSearch refused)
- https://www.moneyhelper.org.uk/en/savings/types-of-savings/emergency-savings-how-much-is-enough?source=mas: not checked, no search result to fetch from (WebSearch refused)
- https://dfi.wa.gov/financial-education/information/importance-having-emergency-savings-account: not checked, no search result to fetch from (WebSearch refused)
- https://www.cgd.pt/Site/Saldo-Positivo/protecao/Pages/fundo-emergencia.aspx: not checked, no search result to fetch from (WebSearch refused)
- https://msbfile03.usc.edu/digitalmeasures/joe.raffiee/intellcont/Raffiee_Feng_2014_AMJ-1.pdF: not checked, no search result to fetch from (WebSearch refused)
- https://eur-lex.europa.eu/EN/legal-content/summary/part-time-work.html: not checked, no search result to fetch from (WebSearch refused)
- https://www.legislation.gov.uk/uksi/2023/1328/made/data.pdf: not checked, no search result to fetch from (WebSearch refused)
- https://www.ecb.europa.eu/stats/policy%5Fand%5Fexchange%5Frates/euro%5Freference%5Fexchange%5Frates/html/eurofxref-graph-usd.en.html: not checked, no search result to fetch from (WebSearch refused)
- https://europa.eu/youreurope/citizens/work/taxes/income-taxes-abroad/faq/index_en.htm: not checked, no search result to fetch from (WebSearch refused)
- https://taxhelpforhustles.campaign.gov.uk/tax-rules-content-creators/: not checked, no search result to fetch from (WebSearch refused)
- https://www.irs.gov/taxtopics/tc554: not checked, no search result to fetch from (WebSearch refused)
- Because of the above, every claim the unit rests on one of those fourteen pages stands as the writer and the earlier fresh check left it: not confirmed, not contradicted. This includes "CGD, a state-owned bank", which the fresh check also could not verify.

## Failure rate

- Sample: 10 claims. PASS 4, FAIL 0, STALE 0, unverifiable 6. Failure rate 0 in 10 (0 of the 4 that could be checked). The more-than-one-in-ten rule is not met; no full audit was run.
- All claims checked: 42. PASS 35, FAIL 1, STALE 0, unverifiable 6.
- The six unverifiable sampled claims are the six whose source is an outside page. The sample therefore tests the unit's pointers and arithmetic and leaves its live-verified facts untested by this audit.

## Counts

- Words: 8,875 (`wc -w unit.md`). `##` sections: 10.
- Cited claims in the whole unit: 87. Method: `out/count_claims.py` split the text outside `viz` blocks into sentences, list items and table rows and kept each one that names a cited source (a link, a PB or DD-PB unit, or a named dataset or page); the 92 candidates were then read one by one. Removed: split halves of one sentence (2 in §5), sentences that only point to a unit without resting a claim on it (1 in the intro, 1 in §3, 1 in D7, 2 template blanks, the fresh-check line of the Unsure list). Added: §2's benefit sentence, §6's exchange-rate row, the Unsure list's EUR-Lex line.
- Per section: intro 3 · §1 5 · §2 6 · §3 26 · §4 4 · §5 11 · §6 2 · Deliverable 24 · Template 0 · Sources 0 (references, not claims) · Unsure list 6.

## Figures (`viz` blocks)

1. Matrix, §3: PASS. Nine rows, as §3's nine lines; every cell traces to the text ("1,000 subs + 8,000 h", "500 subs + 3,000 h", "no threshold published", "not in year one" twice, "inbound, from 6 Jul 2027", "since 8 Jun 2027", "list of about 1,613", "open, no hours", "0 until her own RPM", "signed contracts only", "her net sales"). Note, no fix: the caption's YouTube Help answer numbers 12843009 and 13429240 appear nowhere in the unit's text; they are PB9 §2's locators and are correct there.
2. Compare, §6: PASS. Ten bars equal §6's table and the recomputation (7.7, 8.0, 15.0, 15.8, 16.5, 17.0, 21.3, 24.2, 29.5, 49.3); the caption says why the eleventh row is not drawn. "YouTube Subscriber Benchmarks 2026" is PB1 §2's title for the vidIQ page.
3. Decision, D2: PASS. Three questions and four outcomes are D2 line 6 and D1 i17, i18; USD 1,657.80 and EUR 18,000 are D2 lines 3 and 4.
4. Timeline, D6: PASS. Six dates (5 Jul 2027, 3 Jan 2028, week of 1 Jan 2029, 2 Apr 2029, 2 Jul 2035, 7 Jul 2042) are in D3 to D5 and §6; the decimal positions agree with the dates.

## Deliverable

- Exists in full: D1 (18 inputs, each with a source or a label), D2 (thresholds and the rule), D3 to D5 (three paths, each with arithmetic, an earliest honest date and what has to be true), D6 (together, against DD-PB1's prior), D7 (when it is read); then the template T1 to T4, each blank saying what goes in it.
- Follows from the evidence: every number was reproduced from D1 (see Also checked 32 to 36). Each date says which unsourced assumption it rests on; the lines no source can date enter at zero.
- Usable without the unit: yes for Mara's build. The template leans on the unit in three blanks (i7 "the guidance you read (§2)", i13 "every line in §3", i18 "(§1)"); a reader with only the template would need those sections.
- One disagreement between build and template: flag DD-PB2-5 (her preconditions leave out the health-cover and benefit questions the template requires).
- Mara's facts agree with `case-facts.md`.

## Course goal and sourcing standard

- Goal: the unit serves the third outcome (deciding with evidence whether to continue, change or stop) by turning PB10's quarterly counts into a dated test. It advises neither quitting nor staying, as the brief requires.
- Advice without evidence: none found. Each rule is labelled as the course's or Mara's ("this course's rule; no source sets it", "her rule"), and each recommendation is either a question or a pointer to a filed unit.
- Part 1: sourced where made, yes; sources list complete both ways for links (14 links in the body, the same 14 in Sources); the unit-pointer line of Sources misses DD-PB1 §3 to §8 (DD-PB2-4). One sentence says more than its source text (DD-PB2-1).
- Part 5: platform named (YouTube subscribers as the model's audience, Instagram stated as entering as nothing); no tax rate stated, t = 10% and 30% marked illustrative; "information, not legal, tax or financial advice" stated; EU, UK and US given for benefits, tax and reduced hours, with the gaps said (no US rule on reduced hours, no source on unpaid leave); one amount without its date (DD-PB2-3). Vendor figures are cited to the filed unit that holds the link (PB1 §2, PB9 §2, §4), not linked here; with search off that is the unit's stated method, and the reader can follow each pointer.
- Front matter says `search: off` while the introduction lists six live verifications of 14 Nov 2026; each changeable fact carries its date, so the line of the standard is met either way.

## Verdict

**DD-PB2: PASS on the sample rule (0 FAIL in 10; no full audit run), with a limit that matters: 6 of the 10 sampled claims are unverifiable because web search was refused, so none of the unit's fourteen outside sources was opened in this audit.** One FAIL outside the sample (should-fix), three minor errata, one flag. A rerun of the six outside-source claims with search available is needed before this audit can stand for the unit's live facts.

## Most consequential errors

1. §2 says no unemployment benefit follows a resignation in the three places checked. The unit's own §1 says something narrower: in the US the state decides, in the UK a sanction runs 91 days for a first case where there was no good reason, and only Portugal's guide is reported as treating a resignation as voluntary. A UK or US reader would take from §2 that a benefit is ruled out, which the cited pages, as the unit quotes them, do not say (DD-PB2-1).
2. D3 calls +0.5 and +1.4 a month the band medians "for channels of her size"; only +0.5 is her band (DD-PB2-2). Minor: the comparison still holds.
3. None further. The AIR Media-Tech amount lacks its date (DD-PB2-3) and the Sources line misses DD-PB1 §3 to §8 (DD-PB2-4); neither changes a number or a date.

## Bibliography line

No new source to add; no source to mark failed; all fourteen outside sources of DD-PB2 to be marked "not re-opened in Audit 3 (search refused), re-check owed".

## Changelog line

2026-11-14 · Audit 3, DD-PB2 · claude-fable-5-2 · PASS on the sample rule (0 FAIL in 10), 6 of 10 sampled unverifiable: web search refused, no outside source opened · 42 claims checked, 1 FAIL (should-fix, §2), 3 minor errata, 1 flag · outside-source recheck owed.

## Errata

**DD-PB2-1** · erratum · should-fix · FAIL

- Section: §2 · Runway, 'What the guidance says', after the table
- Current: `No unemployment benefit follows a resignation in the three places checked (§1).`
- Fix: `None of the three places checked pays unemployment benefit after a resignation as a matter of course (§1): the US leaves the decision to the state, the UK applies a sanction, 91 days for a first one, where there was no good reason, and Portugal treats a worker's own resignation as voluntary.`
- Basis: The unit's own §1 item 3, which reports the US rule as 'decided by the state' (https://oui.doleta.gov/unemploy/uifactsheet.asp), the UK rule as a sanction of '91 days for a first one in a year' for leaving 'without a good reason' (https://www.gov.uk/guidance/universal-credit-sanctions) and only Portugal's guide as treating a resignation as voluntary (https://seg-social.pt/documents/10152/15007/6001_subsidio_desemprego/1867b682-64f2-4b1a-8f39-ca008602a16b). The three pages were not re-opened in this audit (search refused); the finding is that §2 says more than §1 does.

**DD-PB2-2** · erratum · minor · other

- Section: Deliverable D3, What has to be true, item 2
- Current: `above the band medians of +0.5 and +1.4 a month for channels of her size (PB1 D1 Y6; vendor)`
- Fix: `above the band median of +0.5 a month for channels of her size, 1 to 99 subscribers, and the +1.4 of the next band, 100 to 499 (PB1 D1 Y6; vendor)`
- Basis: PB1 D1 row Y6 and PB1 §2: +0.5 is the 1-99 band, +1.4 the 100-499 band; Mara has 61 subscribers (PB10 D4). vidIQ, YouTube Subscriber Benchmarks 2026, https://vidiq.com/research/youtube-subscriber-benchmarks-2026/ as PB1 cites it (not opened here).

**DD-PB2-3** · erratum · minor · other

- Section: §3 · item 1, YouTube ad revenue share
- Current: `$2.39 per 1,000 views on its own client channels (PB9 §2)`
- Fix: `$2.39 per 1,000 views on its own client channels, May 2025 to May 2026 (PB9 §2)`
- Basis: Part 5: an amount is in its source's currency with its date. PB9 §2 gives the period: AIR Media-Tech, 300 client channels, May 2025 to May 2026, https://air.io/en/air-data-findings/which-youtube-niche-makes-the-most-money-in-2026-ranked-by-real-rpm-and-cpm as PB9 cites it (not opened here).

**DD-PB2-4** · erratum · minor · other

- Section: Sources, last line
- Current: `DD-PB1 (§11; Deliverable A)`
- Fix: `DD-PB1 (§3 to §8, §11; Deliverable A)`
- Basis: §2 of the unit cites 'DD-PB1 §3 to §8, §11' (a fresh-check fix that the Sources line did not follow); Part 1: the unit leaves its sources. No URL: internal.

**DD-PB2-5** · flag · minor · other

- Section: Deliverable D1 row i18 against Template T1 row i18
- Current: `| i18 | Preconditions | Employment contract read and any notice given (PB8 J1, J2); income registration answered (T1, done 18 Mar 2027); t filled (i8) | PB8 register; PB10 D3 |`
- Fix: `No replacement given. The template's i18 adds 'health cover and benefits after leaving answered (§1)', and §1 says each of its six items 'has to be answered before a date means anything'; Mara's own i18 leaves it out. Adding it to her row sets a new fact about Mara (what her employer pays that she would have to buy) and changes the preconditions the register records as (J1, J2, T1, t), so it is for the owner to decide.`
- Basis: unit §1 'What a survivable floor leaves out', items 2 and 3; Template T1 i18; case-facts.md, 'Set by DD-PB2', pass-rule line. No URL: internal.

