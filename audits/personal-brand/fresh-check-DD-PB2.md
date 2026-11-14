---
audit: fresh check
unit: DD-PB2 · Deep dive: the quit-your-job math
course: personal-brand · PB · Building a Personal Brand on Instagram and YouTube
model: Opus 5.5 (claude-opus-5-5, as the agent states; this session keeps no agent transcript on disk, so the model could not be confirmed from a transcript's "model" field; live search). A Fable 5.1 fresh check of DD-PB2 is owed to the Fable stage (P49)
date: 2026-11-14
chat: own Opus 5.5 agent context, not shown the writing (P31), launched by the W-DD-PB1/W-DD-PB2 chat (which ran on Opus 5.5 and only staged, applied, filed and published) in session https://claude.ai/code/session_01KMmgR36yR2m9MAPwT6wfRt
verdict: fix · 1 error, 4 should-fix, 8 minor
---

The checker's final report, verbatim, as the file it wrote in its own folder (`out/fresh-check.md`), copied unchanged by script. Saved before any finding was applied. The exact strings applied are its `out/findings.json`.

claude-opus-5-5

# DD-PB2 fresh check (claude-opus-5-5, 14 Nov 2026)

## Findings

[error] [accuracy] Deliverable D3, line 2; Current: "her monthly account income first reaches T in about August 2041"; Problem: 170 months counted from July 2027 end in September 2041. Under the writer's own model (writer-calc/model.py: income in month k = 0.7485 × (61 + 12.67 × (k + 1)), k = 0 is July 2027), the first month at or above USD 1,657.80 is k = 170, September 2041.; Fix: "her monthly account income first reaches T in about September 2041"; Basis: writer-calc/model.py, rerun 14 Nov 2026.
[should-fix] [attribution] §2, What the guidance says; Current: "and DD-PB1 found no channel income at the date any of its six creators left a job (DD-PB1 §11)"; Problem: DD-PB1 does not say there was no income. It found no income figure: Boyd's household 'both quit our jobs' when 'we could pay both of us' (DD-PB1 §5, Net Influencer), so there was channel income at that exit, of unknown size and date. §11 itself does not discuss income.; Fix: "and DD-PB1 found no figure for channel income at the date any of its six creators left a job (DD-PB1 §3 to §8, §11)"; Basis: units/DD-PB1 §3, §5, §6, §11.
[should-fix] [accuracy] Deliverable D3, Earliest honest date; Current: "pace slowing as vidIQ's medians do by size, PB1 §6"; Problem: vidIQ's absolute monthly medians rise with size (+0.5, +1.4, +3.7 a month, PB1 §2); its percentage medians fall (1.26% to 0.24%, PB1 §6). 'Pace slowing as the medians do by size' misreads both. What supports a later date is that her 12.7 a month is far above the band medians of PB1 §2.; Fix: "her pace falling towards vidIQ's band medians, which sit far below it, as percentage growth falls with size, PB1 §2, §6"; Basis: units/PB1 §2 and §6 (vidIQ, YouTube Subscriber Benchmarks 2026, https://vidiq.com/research/youtube-subscriber-benchmarks-2026/).
[should-fix] [accuracy] §5, Reduced hours, first bullet; Current: "a refusal to transfer "is not sufficient reason" for dismissal"; Problem: The summary says: "A worker's refusal to transfer from full-time to part-time work or vice versa is not sufficient reason for their dismissal." The refusal is the worker's, not the employer's; as written the sentence can be read as an employer's refusal of the reader's request.; Fix: "a worker's refusal to transfer from full-time to part-time work or back "is not sufficient reason" for dismissal"; Basis: EUR-Lex summary of Directive 97/81/EC, last update 4 Dec 2016, https://eur-lex.europa.eu/EN/legal-content/summary/part-time-work.html.
[should-fix] [accuracy] §6, after the table; Current: "each €100 a month of extra saving brings her 12-month runway forward by 3.6 months"; Problem: The effect is not linear: €9,000 ÷ €550 = 16.4 months (3.6 earlier), but €9,000 ÷ €650 = 13.8 months (a further 2.5). 'Each' says every €100 gives 3.6.; Fix: "€100 a month of extra saving brings her 12-month runway forward by 3.6 months"; Basis: arithmetic on D1 i5, i6.
[minor] [accuracy] §6, The two that move the date most; Current: "The floor and the exchange rate move the date by a year or two."; Problem: §6's own table: 17.0 − 15.0 = 2.0 and 15.8 − 15.0 = 0.8; the exchange rate moves it by under a year.; Fix: "The floor and the exchange rate move the date by two years or less (no agreed cuts, 2.0 years; the August 2026 high, 0.8 years)."; Basis: §6 table; writer-calc/model.py.
[minor] [accuracy] Deliverable D2, line 3; Current: "Each 10 points of t multiplies T by 1 ÷ (1 − t)"; Problem: T = F_s ÷ (1 − t) for any t; the factor does not apply per 10 points (at t = 20% it is 1.25, not 1.11²).; Fix: "Any value of t multiplies T by 1 ÷ (1 − t)"; Basis: §4 formula.
[minor] [accuracy] §5, The one study found on leaving in stages; Current: "and acknowledge the rival explanation that people who choose the staged route "systematically select better ideas ex ante"."; Problem: The authors raise the selection explanation and then report a test that leads them to call it unlikely; the unit gives the first half only.; Fix: "and acknowledge the rival explanation that people who choose the staged route "systematically select better ideas ex ante", which they test with a shared frailty model and judge "unlikely"."; Basis: Raffiee and Feng 2014, author's copy, Limitations, https://msbfile03.usc.edu/digitalmeasures/joe.raffiee/intellcont/Raffiee_Feng_2014_AMJ-1.pdF.
[minor] [attribution] Deliverable D1, row i13; Current: "§3; PB9 D2 V1–V3, V8, V11, V15, V16"; Problem: Row i13 lists the paid tier among the lines at zero; its PB9 row is V14, which the citation leaves out.; Fix: "§3; PB9 D2 V1–V3, V8, V11, V14, V15, V16"; Basis: units/PB9 D2.
[minor] [attribution] Sources; Current: "- HMRC, "Tax help for hustles: content creators", as PB8 §6.5 cites it."; Problem: Part 1 asks for the date of each source; the page's modified date is 22 Sep 2026 (also PB8 §6.5's).; Fix: "- HMRC, "Tax help for hustles: content creators", modified 22 Sep 2026, as PB8 §6.5 cites it."; Basis: https://taxhelpforhustles.campaign.gov.uk/tax-rules-content-creators/ (meta modified 2026-09-22).
[minor] [attribution] Sources; Current: "- IRS, Topic no. 554, Self-employment tax, as PB8 §6.5 cites it."; Problem: Part 1 asks for the date of each source.; Fix: "- IRS, Topic no. 554, Self-employment tax, last reviewed or updated 9 Nov 2026, as PB8 §6.5 cites it."; Basis: https://www.irs.gov/taxtopics/tc554 (Page Last Reviewed or Updated 09-Nov-2026).
[minor] [attribution] Sources; Current: "- Your Europe, "FAQs: Income taxes abroad", as PB8 §6.5 cites it."; Problem: Part 1 asks for the date of each source.; Fix: "- Your Europe, "FAQs: Income taxes abroad", last checked 18 Jun 2026, as PB8 §6.5 cites it."; Basis: https://europa.eu/youreurope/citizens/work/taxes/income-taxes-abroad/faq/index_en.htm (Last checked 18/06/2026).
[minor] [coverage] §5, A sabbatical, first bullet; Current: "- Does your contract, a policy it points to, or your national law offer unpaid leave, for how long, and is the job held in writing?"; Problem: Part 5 asks that a legal point name the primary source to open for the EU, the UK and the US, or say none was opened; the sabbatical questions do neither (reduced hours says so for the US).; Fix: "- Does your contract, a policy it points to, or your national law offer unpaid leave, for how long, and is the job held in writing? This unit opened no EU, UK or US source on unpaid leave; the sources to open are your contract and your country's employment law."; Basis: sourcing-parts-1-and-5.md, Part 5.

## (1) Coverage (brief items)

- Household floor computed, and what a survivable floor leaves out: covered (§1; six items, with EU/UK/US questions).
- Runway, the guidance on its length and the grade of that guidance: covered (§2 table; graded consumer guidance, no dataset). The EU row is one national bank only, which the unit says.
- Each PB9 income line with its timeline, or marked an unfilled input: covered (§3, nine lines; one with a count, eight unfilled; matrix figure).
- Tax as an input the model does not compute, with the instruction: covered (§4; t, T = F_s ÷ (1 − t), four questions, EU/UK/US sources).
- Reduced hours, sabbatical, contract work as questions: covered (§5); the sabbatical names no source for any of the three jurisdictions (minor finding above).
- Sensitivity to the two assumptions that move the date most: covered (§6; table, compare figure; income per subscriber and pace named).
- Deliverable: Mara's threshold model, three paths, earliest honest date each, arithmetic shown: covered (D1 to D7). Template with its list of inputs: covered (T1 to T4).
- Advise neither quitting nor staying: met (intro; D2 line 6; D6).

## (2) Accuracy: writer's unsure list first

- MoneyHelper, "three to six months' essential outgoings available in an instant access savings account": PASS; the page is undated (only "© 2026"), no mention of self-employment or variable income. https://www.moneyhelper.org.uk/en/savings/types-of-savings/emergency-savings-how-much-is-enough?source=mas
- WA DFI, "Many experts suggest saving 3 to 6 months of basic living costs": PASS; undated. https://dfi.wa.gov/financial-education/information/importance-having-emergency-savings-account
- COBRA and resignation: PASS as written. The worker's guide lists "Termination of employment for any reason other than gross misconduct" and "Reduction in hours", 18 months, "Your premium cannot exceed 102 percent of the plan's total cost of providing you with coverage"; undated; it does not mention resignation. DOL's employer guide is also silent on voluntary or involuntary. The unit's "does not say" stands. https://www.dol.gov/agencies/ebsa/about-ebsa/our-activities/resource-center/publications/workers-guide-health-benefits-cobra?lang=en
- ISS guide 6001 v4.72, 20 Feb 2025: PASS; the URL serves v4.72 of 20 Feb 2025; "por razões alheias à sua vontade (desemprego involuntário)" p. 6; worker's resignation ("denúncia do contrato de trabalho/demissão por iniciativa do trabalhador") as a voluntary reason p. 14. No later version was returned by the search. https://seg-social.pt/documents/10152/15007/6001_subsidio_desemprego/1867b682-64f2-4b1a-8f39-ca008602a16b
- ECB: PASS; 1.1052 on 13 Nov 2026 (the period's minimum); maximum 1.1699 on 21 Aug 2026. https://www.ecb.europa.eu/stats/policy%5Fand%5Fexchange%5Frates/euro%5Freference%5Fexchange%5Frates/html/eurofxref-graph-usd.en.html
- Raffiee and Feng (2014): PASS on NLSY79, 1994 to 2008, 2,198 full-time self-employment spells by 1,093 people, "a 33.3% decrease in the hazard of exit", learning not measured directly, "systematically select better ideas ex ante", AMJ 57(4) 936–963, doi 10.5465/amj.2012.0522; the authors then judge that explanation "unlikely" (minor finding). https://msbfile03.usc.edu/digitalmeasures/joe.raffiee/intellcont/Raffiee_Feng_2014_AMJ-1.pdF
- EUR-Lex summary: PASS on "fully consider", "transfer from full-time work to any part-time work that becomes available", last update 4 Dec 2016; the "not sufficient reason" clause is about a worker's refusal (should-fix above). https://eur-lex.europa.eu/EN/legal-content/summary/part-time-work.html
- Path A assumptions, Path C 80%, US reduced-hours rules not researched, no EU-level runway guidance: stated in the unit as limits; no change.

## (2) Accuracy: other sourced claims

- US UI fact sheet: PASS; "You must be determined to be unemployed through no fault of your own (determined under State law)"; separation for "some reason other than a 'lack of work'" goes to a state determination; last updated 11 Sep 2026. https://oui.doleta.gov/unemploy/uifactsheet.asp
- GOV.UK Universal Credit sanctions: PASS; "leave a job or lose pay by choice while claiming Universal Credit or just before you claim, without a good reason"; first high-level sanction 91 days; last updated 6 Apr 2026. https://www.gov.uk/guidance/universal-credit-sanctions
- CGD, Saldo Positivo: PASS; "pelo menos, seis meses de despesas", "pelo menos, um ano de despesas", dated 9 Apr 2026; no mention of independent work or variable income. https://www.cgd.pt/Site/Saldo-Positivo/protecao/Pages/fundo-emergencia.aspx
- CGD described as "a state-owned bank": unverifiable (the search's CGD corporate page returned "page not found"; the rating-agency page redirected, not checked).
- S.I. 2023/1328: PASS; in force 6 April 2024; regulation 3 of the Flexible Working Regulations (26 weeks' service) omitted, so a request can be made from the start of employment. https://www.legislation.gov.uk/uksi/2023/1328/made/data.pdf
- PB8 §6.5's three tax pages: dates confirmed (HMRC modified 22 Sep 2026; IRS Topic 554 reviewed 9 Nov 2026; Your Europe last checked 18 Jun 2026, sends readers to national administrations).
- Claims cited to filed units (YPP 8,000 h and 1,000 subs from 1 Feb 2027; 500 subs + 3,000 h; Instagram by absence; Shopping affiliate's 18 countries without Portugal; Collabstr USD 255; AIR Media-Tech USD 2.39 RPM; beehiiv 0.62%; Gumroad net USD 13.00; vidIQ 8.65%, 68% and 53.5%, +0.5/+1.4/+3.7; PB3 §5's unmeasured list share; PB1 §10's list): all PASS against units/PB1, PB3, PB9.

## (3) Figures: whose figure

Every number names its owner: Mara's are labelled (Mara, fictional) or "her rule", "her estimate", "her planning value", "derived"; benchmarks carry vendor, platform-official, consumer guidance or regulator labels. Met, apart from the findings above.

## (4) Labels

Vendor (vidIQ, AIR Media-Tech, Collabstr), correlational (vidIQ upload study), survivor sample (vidIQ crossing counts), platform data (beehiiv), peer-reviewed observational (Raffiee and Feng), consumer guidance (new label, defined in the intro) and regulator guidance are all labelled. DD-PB1's six as survivors: labelled in D6. Met.

## (5) Deliverable

Present in full: D1 inputs (18 rows with source or label), D2 thresholds with arithmetic, D3 to D5 three paths with arithmetic, earliest honest date, tests and what has to be true, D6 together with the DD-PB1 prior, D7 reading schedule; template T1 to T4 with every blank saying what goes in it. It follows from §1 to §6 and is usable alone. Met, with the D3 month fix.

## (6) Errata and pointers

No audit report was read (as instructed); no erratum applies in this packet. Pointers to filed units checked: PB1 §1, §2, §6, §10, D1 I7/Y6, D2; PB3 §5, D2; PB4 holiday rule; PB8 §6.4 items 1, 2, 6, §6.5, J1, J2, T1, T3; PB9 §2 to §5, §7, §8, D1 to D4, V14, V18; PB10 §3, D3 (T1 on Thu 18 Mar 2027, R8, list 9), D4 (61 subs, 11/13/14, 133.0 h, 402 views, USD 39.00 in 26 days, launch-email caution), D5 (year-two dates; upload 40 on Tue 4 Jul 2028 in Q7's 40–46); DD-PB1 Deliverable A ("Keep the job through year two"). All say what the unit says, except DD-PB1 §11 (should-fix) and the PB1 §6 reading in D3 (should-fix).

## (7) Figures (viz blocks)

1. matrix, §3: every label traced ("1,000 subs + 8,000 h", "500 subs + 3,000 h", "no threshold published", "not in year one", "inbound, from 6 Jul 2027", "since 8 Jun 2027", "list of about 1,613", "open, no hours", "0 until her own RPM" ← "enters at zero until her Studio shows both thresholds met, then at her own revenue per thousand views"). Caption names section and sources. Kind fits (items by sections). Renders. PASS.
2. compare, §6: all ten values and labels match §6's table ("Mon 2 Apr 2035 | 7.7" ... "Mon 5 Oct 2076 | 49.3"); recomputed from the dates: 7.74, 7.99, 15.01, 15.75, 16.50, 17.00, 21.25, 24.24, 29.49, 49.25. Caption names section, ECB and vidIQ sources and why one row is not drawn. Kind fits (numbers compared). Renders. PASS.
3. decision, Deliverable D2: questions and outcomes trace to D2 line 6 and i18 ("the path's income test has passed at that checkpoint and the one before, (b) the runway is saved, and (c) the preconditions (i18) are done"); USD 1,657.80 and €18,000 from D2 lines 3 to 4. Caption names section, rule owner and basis. Kind fits (a rule with branches). Renders. PASS.
4. timeline, Deliverable D6: every date traced (5 Jul 2027, 3 Jan 2028 "Earliest honest date: Monday 3 January 2028", week of 1 Jan 2029, 2 Apr 2029 "first read **Monday 2 April 2029**", 2 Jul 2035 "Subscriber pace doubled ... Mon 2 Jul 2035", 7 Jul 2042); positions (2029.25, 2035.5, 2042.51) consistent. Caption names D3 to D5, PB10 D4/D5 and the ECB rate. Kind fits (dated events). Renders. PASS.

## (8) Writer's Source errors list

- "none": confirmed; nothing found wrong in DD-A2's CGD and ISS readings or in the filed units' figures the unit uses.
- CGD's two phrases, page dated 9 Apr 2026: confirmed.
- ISS 6001 v4.72, p. 6 condition and p. 14 resignation: confirmed.
- Recomputed filed-unit figures: confirmed (PB1 §2: about 198, 286 and 135 months; PB9 §2: 87,273 to 120,000 views; PB10 D4 R1: 0.25, 1.0 and 3.0 expected sales in 26 days; DD-PB1: about 38 and 42 months).
- DD-A2 carried for structure only: confirmed. None of its household figures (take-home, car credit, floor, IAS, contribution rates, its income lines) appears; the shared pieces are the F_s formula, the runway logic and the two re-verified sources.

## (9) Part 5, line by line

- Number, mechanism, recommendation sourced where made: met.
- Source types: met, with one note. Runway guidance (MoneyHelper, WA DFI, CGD) and legal pages fall outside the four listed types; the unit labels them (consumer guidance, regulator guidance, primary law), grades them and uses them only for "her rule" and questions.
- Anecdote, correlational and vendor labels: met.
- Platform named for growth, format and metric claims: met (YouTube subscribers as the model's audience, Instagram stated as entering as nothing).
- Carried-over claims re-verified: met (CGD, ISS confirmed live).
- Nothing about the private course's reader; no reference to it: met (grep for its figures and terms: none; kit/private_terms.py not in the packet).
- Mara labelled on first use, consistent with case-facts.md, not evidence: met. New facts (partner, rented flat, €2,150, €1,700, €200, €9,000, R = 12) fill what case-facts left free (household and income).
- No country's rate stated as the reader's; currency and date; EU/UK/US question and source; "information, not legal or tax advice": met, except the sabbatical bullet (minor finding).
- No uncited figures; nothing invented: met.
- Search flag: the front matter says "search: off" while the intro lists six live verifications, each dated 14 Nov 2026; every changeable fact used carries its date, so the line is met either way.
- Deliverable for Mara in full, then template: met.
- Does not read as advice without evidence: met.
- Links as links: met.

## (10) Read as the persona (any reader, any country)

Nothing assumes knowledge of the private course, and no unit is named that the reader cannot open. Register codes (J1, T1, T3, R1, V14) are PB8's, PB9's and PB10's and the reader has them. "Four days" assumes a five-day week, and the Path C arithmetic is said to be a placeholder until payroll gives a figure. The EU runway row is one Portuguese bank, said so. No barrier found.

## (11) Arithmetic and Mara facts

writer-calc/model.py rerun: every printed date and value reproduced (F_s €1,500; s €450; r0 USD 0.7485; T USD 1,657.80 and 19,893.60; 2,214.9 subscribers; 170.0 months; base pass 7 Apr and 7 Jul 2042; all eleven sensitivity rows). Hand checks: 12 × €1,500 = €18,000; €9,000 ÷ €450 = 20 months to end Feb 2029, first checkpoint Mon 2 Apr 2029; USD 1,657.80 ÷ 0.9 = 1,842.00; 127.5 guide sales vs 3.5 (36×); 693,640 views vs 437 a month (about 1,590×); K ≈ €1,459 (€1,500 − €41.31); 80% = €1,720; 69.8%; saving €20, 450 months; 1,613 list, 72 quarters; ratios 14.0 and 1.65; Sun 30 Jan 2028 is the week-B cut window of weeks 55–56; all named weekdays correct. One disagreement: "about August 2041" should be September 2041 (error above). Mara facts against case-facts.md, PB9, PB10 and DD-PB1: consistent (Portugal, One Box Restoration, 5 Jan 2027 start, T1 18 Mar 2027, guide launched 8 Jun 2027 at USD 15 net 13.00, list 9 and 31, deals inbound from 6 Jul 2027, year-two reviews, "Keep the job through year two").

## Confirmed

- ECB USD reference rate 1.1052 on 13 Nov 2026; Aug–Nov 2026 high 1.1699 (21 Aug). ECB USD page.
- MoneyHelper three to six months' essential outgoings, undated. MoneyHelper page.
- WA DFI "3 to 6 months of basic living costs", undated. WA DFI page.
- CGD six months / at least a year, 9 Apr 2026. CGD Saldo Positivo.
- COBRA termination "for any reason other than gross misconduct", reduction in hours, 18 months, 102 percent cap; resignation not mentioned. DOL worker's guide.
- US UI "no fault of your own (determined under State law)", "lack of work", updated 11 Sep 2026. DOL ETA fact sheet.
- UK UC high-level sanction wording, 91 days, updated 6 Apr 2026. GOV.UK.
- ISS 6001 v4.72, 20 Feb 2025, pp. 6 and 14. seg-social.pt.
- Raffiee and Feng 2014: NLSY79 1994–2008, 2,198 spells, 1,093 people, 33.3%, quote, citation. Author's copy.
- EUR-Lex summary "fully consider", last update 4 Dec 2016. EUR-Lex.
- S.I. 2023/1328 in force 6 Apr 2024, removes the 26-week condition. legislation.gov.uk.
- HMRC content creators page modified 22 Sep 2026; IRS Topic 554 reviewed 9 Nov 2026; Your Europe FAQ last checked 18 Jun 2026.
- Filed-unit figures used by the unit (PB1, PB3, PB8, PB9, PB10, DD-PB1) as listed in (2) and (6).
- Writer's model: all dates and amounts reproduced except the August 2041 month.

DD-PB2 · verdict: fix · error 1, should-fix 4, minor 8
