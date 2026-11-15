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
