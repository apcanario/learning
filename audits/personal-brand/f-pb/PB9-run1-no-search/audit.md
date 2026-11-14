Model: claude-fable-5-2

# Stratified-sample audit · PB9 · Monetisation: what pays at each audience size

Course PB, Audit 3. Date: 14 November 2026. Search: on. One unit, one fresh auditor; the unit was not edited.

## Provenance

- Auditor model: claude-fable-5-2. Folder `/home/claude/fpb/PB9`; `out/` was empty at the start (no resumed run).
- Read: `PROMPT.md`, `unit.md`, `brief.txt`, `sourcing-parts-1-and-5.md`, `case-facts.md`, `fresh-check-PB9.md` (to avoid re-reporting; none of its verdicts reused), `others/` for pointers only.
- Tools: Read, Write, Edit, Bash, WebSearch, WebFetch. No memory, past-chat, Projects, connector, Artifact, Agent or `mcp__` tool.
- Web rule followed: search first; fetch only a URL a search of this agent returned verbatim.

## Sample (recorded before any check)

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

**What happened to the web checks.** WebSearch was called twice, as the first two checks (S1, S2). Both calls were refused before any search ran: "this turn's web search budget is used up (limit: 200 WebSearch calls per turn, shared by every agent in it)". The refusal says not to work around it. Under the web rule a WebFetch needs a URL that a search of this agent returned, and no search returned one, so nothing was fetched. **No external source of this unit was opened in this audit.** Every claim that rests on an external source is therefore "unverifiable" here, which says nothing about whether it is right. What follows is everything that could be checked inside the folder: the unit's arithmetic and dates, its pointers to the other eleven units, Mara's facts against the register, the four figures against the text, the Sources list against the body, the deliverable and the standard.

## Table

| # | Section | Claim | Source | Verdict | Note |
|---|---|---|---|---|---|
| S1 | §1 | Fan funding at 500 subscribers + 3,000 hours; ads at 1,000 + 8,000 hours for new applicants from 1 Feb 2027 | YouTube Help 12843009 | unverifiable | Source not opened. Agrees with §2, figure 1, D2 V1–V2, D5 R3, PB1 D1 rows Y10–Y11 and PB6 YT10 |
| S2 | §2 | vidIQ cohort 137,355; median about 272 at upload 10; exclusion sentence | vidIQ, First 10 Videos Study | unverifiable | Source not opened. Agrees with PB1 §2 and D1 row Y1 |
| S3 | §3 | Amazon US 3.00% / 4.50% / 4.00% by category | Amazon Associates statement | unverifiable | Source not opened. §9 row and D2 V11 agree with §3 |
| S4 | §4 | Collabstr: 21,000+ collaborations; paid $255 / $193; asking $311 / $214; "down 63% ... from $418" | Collabstr 2026 report | unverifiable | Source not opened. The unit's own arithmetic on it holds: 418 to 255 is a fall of 39.0% |
| S5 | §5 | Gumroad 10% + $0.50, 30% via marketplace, merchant of record, taxes since 1 Jan 2025 | Gumroad, Pricing | unverifiable | Source not opened. §9 row, D2 V5 and D3's USD 13.00 follow from it |
| S6 | §6 | beehiiv median paid conversion 0.62%; about 6 per 1,000; $10 / $100; churn 5.06%–16.67% | beehiiv, State of Paid Newsletters 2026 | unverifiable | Source not opened. 0.62% is used consistently in §6, V13, V14, D3, D5 R5 |
| S7 | §7 | PB1's stop rule protects the long-form cadence (PB1 D3); PB3 D2 gives the 10-hour plan | others/PB1, others/PB3 | PASS | PB1 D3: stop or rebuild at fewer than 3 YouTube videos in each of two consecutive quarters. PB3 D2: allocation at 3, 6 and 10 hours a week |
| S8 | §8 | NIST: Poisson models "the number of events occurring within a given time interval"; mean λ, SD √λ | NIST e-Handbook §1.3.6.6.19 | unverifiable | Quotation not opened. Everything derived from the model was recomputed and holds (Also checked 6) |
| S9 | §9 | Stripe (Portugal) 1.5% + €0.25; 2.5% + €0.25; 3.15% + €0.25; + 2% conversion | Stripe, Preços (Portugal) | unverifiable | Source not opened |
| S10 | §10 | Step 1: PB8 D1 clause 7; register T1 before any income, A3 before a deal, E3–E4 before commercial email | others/PB8 | PASS | Clause 7 (no deal, gift, affiliate link or code in Seasons 1–2); T1 "before the first income, of any kind"; A3 to do by 5 Jul 2027; E5 opens the form only if E3 and E4 are done |
| S11 | §11 | Li, Gao, Gu and Leung: U-shape; 4,908 influencers, 6,869 posts; 0.475 / 0.393; Douyin 1,000, near 0.52 | JM record; accepted manuscript | unverifiable | Sources not opened. 39%–48% in the same section matches 0.393–0.475 |
| S12 | Deliverable | V17: CTT, Preços 2020, novembro/2020, Singulares, 58.00 € a year before VAT | CTT tariff PDF | unverifiable | Source not opened. Agrees with the register (PB9 block) and PB1 D2's address line. The unit itself grades the price stale (2020 tariff, no current price found) |
| S13 | Template | T1 sends the Shopping row to answer 13376398 for "whether your country is listed" | YouTube Help 13376398 | unverifiable | Source not opened. T1 matches §2's use of the three answers |
| S14 | Sources | Eisend et al., Journal of Advertising 49(3), 344–366, 2020; "61 papers that use 57 distinct data sets" | WUR record | unverifiable | Source not opened. Reference identical to PB8's Sources entry |
| S15 | Unsure list | 55% / 45% shares are from YouTube's blog of 10 Aug 2026 | YouTube Official Blog | unverifiable | Source not opened. Agrees with §2 and the §9 table |

## Also checked (beyond the sample; all inside the folder)

| # | Section | What | Verdict | Note |
|---|---|---|---|---|
| 1 | §2 | Views the thresholds mean: 480,000 minutes; 87,273–120,000; 3,357–4,615 a video; 32,727–45,000; 1,259–1,731; 12 to 17 times 272 | PASS | Recomputed (12.3 and 17.0) |
| 2 | §2 | 87,273 views at $2.39 = $208.58 | PASS | Recomputed |
| 3 | §3 | 13 × 30 × 0.03 = USD 11.70; 13 videos | PASS | Uploads 14–26 are 13 videos |
| 4 | §4 | 418 to 255 is a fall of 39% | PASS | 38.995% |
| 5 | §6 | 0.90%, 1.63%, 1,613, €3.98 | PASS | Recomputed |
| 6 | §8 | Relative spread ±50% / ±35% / ±10%; empty months 31.2% and 74.7%; percentiles 0–5, 4–13, 16–32, 84–117; 45.3%; 10.0% | PASS | Exact Poisson; 1.165 and 0.291 a month are 8 and 2 sales over 209 days |
| 7 | §9 | On USD 15: Gumroad 2.00 (13.3%), Stripe 0.74 (4.9%), Etsy 1.88 (12.5%) | PASS | Recomputed |
| 8 | §11 | One sponsored video in a season of six or seven is 14%–17% | PASS | 16.7% and 14.3% |
| 9 | D3 | USD 13.00 a sale; totals 26.00 / 104.00 / 567.00; 0.37, 1.35, 6.52, 2.48 members; per-hour figures; $588 | PASS | Recomputed |
| 10 | D1, D5 | Weekdays, upload numbers and the 209 days | PASS | 8 Jun 2027 is upload 12, 6 Jul 2027 upload 14; four Sundays; four checkpoint Mondays |
| 11 | §2, D3 | Pointers to PB1 (§1, §4, D1 Y1/Y10/Y11, D2, D3 read 6) | PASS | PB1 D2 holds the address line PB9 describes |
| 12 | §6, §7 | Pointers to PB3 (§5, D2) | PASS | |
| 13 | §2, D1, D3 | Pointers to PB4 §1, PB5 §2 and §10, PB6 D1 and YT10, PB7, PB8 | PASS | |
| 14 | §3–§5, §10, §11, D | Pointers to PB8 (§2, §6.1, §6.5, §7, clauses 3 and 7, register lines) | PASS | |
| 15 | Deliverable | PB10 and DD-PB2 use PB9's rows and numbers as PB9 gives them | PASS | Three points of friction are flags PB9-1 to PB9-3 |
| 16 | Intro, D | Mara's facts against `case-facts.md` | PASS | "(Mara, fictional)" on first use; dates, hours, prices and scenario inputs agree with the PB9 block; Portugal per P102 |
| 17 | Sources | Sources list against the body | PASS | 35 linked URLs in the body, the same 35 in Sources |

## Not checked

- **WebSearch**: refused twice (search budget for the turn used up; a limit, not a site refusal). 2 attempts, 0 searches performed.
- **WebFetch**: 0 calls. No search returned a URL, so the web rule allowed none.
- **All 35 source URLs of the unit**: not checked, for the reason above. They are the 35 lines of the unit's Sources section; none was opened.
- `kit/private_terms.py` is not in the folder and was not run.

## Failure rate

- Sample: 15 claims. PASS 2, FAIL 0, STALE 0, unverifiable 13. Failure rate 0 of 15 (0 of the 2 that could be verified).
- All claims checked: 32 (15 sampled, 17 also checked). PASS 19, FAIL 0, STALE 0, unverifiable 13.
- The more-than-one-in-ten rule was not triggered, so no full audit was run. The rule was applied to a sample in which 13 of 15 claims could not be tested; it carries little weight here.

## Counts

- Words (`wc -w unit.md`): 8,974. `##` sections: 15.
- Cited claims in the whole unit: **94**. Counting rule: each sentence or table row that rests a number, date, quotation, attribution or mechanism on an external cited source, including a figure derived from one; pointers to other units, the four `viz` blocks, the Sources list and the Unsure list (which restate) are not counted. Tally by section: §1 3 · §2 20 · §3 6 · §4 7 · §5 5 · §6 12 · §7 0 · §8 5 · §9 9 · §10 0 · §11 8 · Deliverable 19 (D2 9, D3 7, D4 1, D5 2) · Template 0 · Sources 0 · Unsure list 0.
- Separately: 35 sources listed; about 29 pointers to other units.

## Figures

1. **flow, §1: PASS.** All five labels and notes trace to §1–§2 ("day one"; programme's or brand's terms; no threshold published and the professional dashboard; 500 + 3,000 in the last year or 3M Shorts views in the last 90 days; 1,000 + 8,000 in 365 days from 1 Feb 2027). The caption names the two YouTube answers and Instagram's page with the date.
2. **range, §8: PASS.** Lows, highs and points equal §8 item 3 and were recomputed; 2, 8 and 24 are D2 V6.
3. **bars, D3: PASS.** 26.00, 104.00, 312.00 and 255.00 equal D3's table; the caption's totals equal D3's.
4. **decision, D4: PASS.** Questions and outcomes equal §10 steps 1–4 and D4's rule; the caption agrees with D1 and D4. It carries the "one labelled piece a season" limit that flag PB9-2 questions.

No figure erratum.

## Deliverable

- Exists in full: D1 decisions, D2 eighteen assumptions each with source and grade, D3 arithmetic for three scenarios with the table and figure, D4 the start rule applied to seven lines, D5 eight revenue rows; then template T1–T4 with every blank described.
- Follows from the unit's evidence: platform lines are zero on the cited thresholds; the guide's net follows Gumroad's stated fee; counts with no source are labelled illustrations; the deal fee is graded vendor and "likely above" her size.
- Usable without reading the unit: mostly. It leans on codes from PB8 (T1, T2, A3, E4, clause 7) and on §8, §10, §11; a reader in order has them.
- Three internal points, reported as flags because each needs a decision or touches another unit:
  - **PB9-1.** V10 takes a deal's 2.0 hours "from the publishing-and-replies line". PB10 §5 shows that line is 1.25 hours a fortnight and cannot give up even one hour. The deal's hours have no workable source, so the deal does not pass the unit's own step 3.
  - **PB9-2.** D4 limits each line to one labelled piece a season. §11 counts her own product's mentions as labelled, and PB8 clause 7 has her introduce it as hers every time. From Season 3 a sponsored video plus any guide mention exceeds the limit.
  - **PB9-3.** V6 says her Gumroad count replaces it at the Q3 review; D5 R1 (Q2) and R2 (Q3) both say they replace V6.

## Course goal and standard

- Goal: the unit serves the third outcome (reading numbers against sourced benchmarks each quarter) by giving PB10 its revenue rows and DD-PB2 its income lines; both units use them as written.
- Part 1 and Part 5, as far as they can be judged without opening sources: claims are sourced where made; vendor, correlational, survivor and documented-case labels are present; Inro and EMARKETER are labelled and kept out of the model; changeable facts carry 13 Nov 2026; amounts stay in source currency; the legal point is given as a question with EU, UK and US sources and the not-advice line; Sources and body match.
- Advice without evidence: none found that is unlabelled. §10's test and §7's rule on service hours are the course's own, said to be so, with the basis named; no study is claimed for them.
- Not judged: whether each source says what the unit says. That is the part of the standard this run could not test.

## Verdict

**INCOMPLETE: not a PASS.** Nothing checked failed: 0 FAIL in the sample, no figure fix, no erratum, three flags. But step 2 of the method (open the source, confirm the figure) was carried out for no external source, because search was unavailable to this agent. PB9 should not be recorded as audited on this report. The sample above is fixed and can be rerun as it stands when search is available. No section is named for rewrite.

## Most consequential errors

No error was established. The three open points, in order of weight:

1. A brand deal's hours come from a line that another unit shows cannot supply them (PB9-1).
2. The one-labelled-piece limit conflicts with counting her own guide's mentions (PB9-2).
3. Two revenue rows and V6 disagree on when the guide's sales count replaces the illustration (PB9-3).

## Bibliography line

No new source to add and none to mark failed; no source was opened in this run.

## Changelog line

2026-11-14 · PB9 · Audit 3 stratified sample (claude-fable-5-2): incomplete, web search budget exhausted before any source was opened; 15 sampled, 2 PASS, 0 FAIL, 13 unverifiable; internal checks (arithmetic, dates, pointers, register, four figures) pass; 0 errata, 3 flags (PB9-1 to PB9-3); rerun owed with search.

## Errata

No erratum. Three flags (not applied as errata); each Current occurs exactly once in `unit.md` (`grep -c -F` prints 1).

- **PB9-1** · flag · should-fix · Deliverable D2, row V10 (also D4, Brand deal row)
  - Current: `| V10 | Hours for one deal | — | — | 2.0 | Her estimate, from the publishing-and-replies line | None: her estimate |`
  - Fix: none given; the cut that supplies the 2.0 hours has to be decided (PB10 §5 took its own hour from the Instagram derivatives for the same reason).
  - Basis: others/PB10 §5, "Taking 60 minutes from it would remove all three reply slots and half the scheduling, and scheduling cannot be skipped"; the line is 1.25 hours a fortnight (PB3; PB4 D1 E). Internal, no URL.
- **PB9-2** · flag · minor · Deliverable D4, the rule
  - Current: `adds no more than one labelled piece per season to the account`
  - Fix: none given; decide whether later mentions of the guide count against the limit, or restate the limit.
  - Basis: unit §11 ("so it is counted too"); others/PB8 D1 clause 7 ("Anything she sells herself is introduced as hers every time"). Internal, no URL.
- **PB9-3** · flag · minor · Deliverable D2, row V6 (against D5 R1 and R2)
  - Current: `replaced by her Gumroad count at the Q3 review`
  - Fix: none given; V6, R1 (Q2) and R2 (Q3) must be made to agree, and PB10 D1 copies both first-read dates.
  - Basis: unit D5 rows R1, R2; others/PB10 D1 rows R1, R2 and D4. Internal, no URL.
