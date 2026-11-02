---
audit: fresh check
unit: DD-A2 · Deep dive: the exit math
course: brand-ai · A · Building a Marketable Personal Brand
model: Opus 5.5 (search off; a Fable 5.1 fresh check is owed, deferred by Pedro 31 Oct 2026 to the Fable stage)
date: 2026-11-02
chat: own Opus 5.5 agent context, not shown the writing or the writer's report (P31), in session https://claude.ai/code/session_01KMmgR37RxR23LNtnYJijb7 (row A-5)
verdict: fix · 0 errors, 5 should-fix, 5 minor
---

# Fresh check · DD-A2 · Deep dive: the exit math

The checker's final report follows verbatim, extracted by script from its hand-back (its `SubagentHandback` message).

**Opus 5.5 ran this fresh check. A Fable 5.1 fresh check is still owed: the course owner moved Fable 5.1 checks to a later stage on 31 Oct 2026, and this report does not replace it.**

**What I checked against**
- **Unit copy.** `diff` shows that /tmp/claude-0/a5/check-DD-A2/DD-A2-check-copy.md and /home/claude/learning/courses/brand-ai/DD-A2-deep-dive-the-exit-math.md are identical. I read the copy in full (341 lines).
- **Brief.** I built it by script the way kit/mdcourse.py does: PRE with {GOAL} replaced by hub.GOAL_A, a blank line, then the fifth field of DD-A2's entry in hub.COURSES.
- **What I read.** sourcing-standard.md Parts 1–2, audit-1.html, audit-2.md, kit/viz.py's docstring, and the cited sections of A2, A3, A7, A8, A9 and DD-A1.
- **What I did not touch.** I edited no repository file and ran no git command. Scratch scripts are in /tmp/claude-0/a5/check-DD-A2/scratch/ (calc.py, dates.py, pathA.py, pathB.py).
- **Web rule.** Every fetch was a URL that a WebSearch in this agent returned, character for character. One fetch failed and is marked not checked. Three sources never came back from a search, so I did not fetch them (listed under Accuracy).

## Findings

[should-fix | accuracy] §2; Current: `The same guide caps the benefit at two and a half times the IAS, which it states as €1,306.25 a month, which would be 27.2% of €4,800 in any case (my arithmetic).`; Problem: €1,306.25 is 2.5 × €522.50, the 2025 IAS. The guide (v4.72, 20 Feb 2025) predates the 2026 IAS of €537.13 that A8 §3 gives, so the cap is out of date for 2026. The conclusion (no benefit after a resignation) is unaffected; Fix: `The same guide caps the benefit at two and a half times the IAS, which it states as €1,306.25 a month, the 2025 figure; at the 2026 IAS of €537.13 (A8 §3) the cap is €1,342.83, which would be 28.0% of €4,800 in any case (my arithmetic).`; Basis: ISS guide 6001 v4.72, https://seg-social.pt/documents/10152/15007/6001_subsidio_desemprego/1867b682-64f2-4b1a-8f39-ca008602a16b (cap text "duas vezes e meia o valor do IAS (1.306,25€)"); A8 §3, Portaria 480-A/2025/1.

[should-fix | attribution] §4.4; Current: `The rate under them, 0.40–1.20% of followers per drop and a $48.50 order, is VoxBooster's`; Problem: VoxBooster gives a share of the follower base and does not say "per drop". A7 §1 says so explicitly, adopts per drop as the brief's reading, and tests the per-year reading (B3, T1). The unit attributes "per drop" to VoxBooster; Fix: `The rate under them, 0.40–1.20% of followers (read per drop, as A7 reads it; VoxBooster does not say per drop or per year, A7 §1) and a $48.50 order, is VoxBooster's`; Basis: https://voxbooster.com/blog/merch-sales-creator-statistics-2026 ("0.40% to 1.20% of a creator's total social media follower base converts into physical merchandise buyers"); A7 §1 and B3.

[should-fix | deliverable] D4 table; Current: `| m = 100%, 0.40% per drop | Tue 29 Jul 2042 |`; Problem: Path B is built on A7's weakest joint but drops the per-year reading that A7 itself tests (T1). Under that reading each drop gets 0.60%, and the unit's own model moves the date three and a half years later; Fix: `| m = 100%, 0.40% per drop | Tue 29 Jul 2042 |`, then on a new line `| m = 100%, rate read per year (0.60% per drop; A7 B3, T1), 105,167 followers on drop day | Tue 31 Jul 2040 |`; Basis: my script. It reproduces D4 line 6 exactly (€55,927.04 of sales, €53,533.36 after social security), and the same model at 0.60% first passes on 31 Jul 2040. 631 ÷ 0.006 = 105,167.

[should-fix | attribution] §5, A9 paragraph; Current: `on YouTube, median monthly subscriber growth falls with size at every band (vidIQ, vendor data), and A9 says the median rates describe no actual path to a large audience.`; Problem: the vidIQ source has no link and no date, and it is missing from the Sources list. A9 makes the "no actual path" point in §4 and §5, not §8; Fix: `on YouTube, median monthly subscriber growth falls with size at every band, from 1.26% a month at 1–99 subscribers to 0.24% above a million ([vidIQ, Subscriber Benchmarks 2026, 20 Jul 2026](https://vidiq.com/research/youtube-subscriber-benchmarks-2026/), as A9 §8 cites it; vendor data), and A9 says the median rates describe no actual path to a large audience (A9 §4, §5).`; Basis: https://vidiq.com/research/youtube-subscriber-benchmarks-2026/ (1.26%, 0.59%, 0.53%, 0.51%, 0.48%, 0.30%, 0.24%, strictly falling, 20 Jul 2026); A9 §4 ("not a route anyone takes"), §5 ("the median describes no actual path").

[should-fix | attribution] Sources; Current: `- vidIQ, "How many videos to get 1,000 subscribers", 9 Jun 2025, as cited in A9 §3. https://vidiq.com/blog/post/how-many-videos-to-get-1000-subscribers/`; Problem: the unit cites vidIQ Subscriber Benchmarks 2026 (§5) but does not list it (Part 1: every source cited is listed); Fix: `- vidIQ, "How many videos to get 1,000 subscribers", 9 Jun 2025, as cited in A9 §3. https://vidiq.com/blog/post/how-many-videos-to-get-1000-subscribers/`, then on a new line `- vidIQ Research, "YouTube Subscriber Benchmarks 2026", 20 Jul 2026, as cited in A9 §8. https://vidiq.com/research/youtube-subscriber-benchmarks-2026/`; Basis: as above.

[minor | accuracy] §5, A7 paragraph; Current: `it is €11,682.13 to €12,279.35, under €15,000 throughout (my arithmetic).`; Problem: A7's High total carries the paid tier net of Substack and card fees. IVA turnover counts it gross. The conclusion holds, but the figure tested is understated; Fix: `it is €11,682.13 to €12,279.35, under €15,000 throughout (my arithmetic). Those totals carry the paid tier net of fees; turnover counts it gross, $11,640.00 + $2,438.33 = $14,078.33, which is €12,601.44 at $1.1172 and €12,033.79 to €12,648.99 across the range, still under €15,000 (my arithmetic on A7 B2).`; Basis: A7 B2, High lines 3 and 8; ECB page (below).

[minor | deliverable] D1 i30; Current: `| i30 | Pass rule | Side income over the trailing twelve full months ≥ 12 × T, at two checkpoints running | **His rule**; basis: A9's fixed-date reads; A7 Deliverable A, part 7 (a trigger must hold twice) |`; Problem: D3's 5% row (Tue 13 Feb 2029) holds only with a condition that D6 states ("twelve months of side income stand behind two checkpoints running") but i30 and D2 line 8 do not. Under i30 as written, the trailing sums are €69,240.76 on 15 Aug 2028 and €87,501.92 on 14 Nov 2028, both ≥ €61,679.60, so the test passes on 14 Nov 2028. The 15 Aug window holds only eleven months of tier income; Fix: `| i30 | Pass rule | Side income over the trailing twelve full months ≥ 12 × T, at two checkpoints running, each with twelve full months of side income behind it | **His rule**; basis: A9's fixed-date reads; A7 Deliverable A, part 7 (a trigger must hold twice) |`; Basis: my script (pathA.py).

[minor | style] §3; Current: `Three facts from the sources push to the top of the bank's range.`; Problem: CGD gives two minimums ("pelo menos, seis meses"; "pelo menos, um ano"), not a range with a top. Twelve months is the floor of its longer advice; Fix: `Three facts from the sources push to the bank's longer figure, at least a year.`; Basis: https://www.cgd.pt/Site/Saldo-Positivo/protecao/Pages/fundo-emergencia.aspx

[minor | figure] D6 timeline; Current: `{"at": 2027, "date": "Aug 2027", "label": "Car credit ends; saving can start", "tone": 4},`; Problem: §1 says saving starts in September 2027 and that nothing is saved before it. The label puts it in August; Fix: `{"at": 2027, "date": "Aug 2027", "label": "Last car-credit month; saving from Sep 2027", "tone": 4},`; Basis: unit §1, "nothing is saved before September 2027".

[minor | coverage] Writer's unsure list, item 5; Current: `whether a first-year exemption or another regime applies to a newly independent worker was not checked here (A8 R12 is open on enrolment timing).`; Problem: a filed unit already gives the one first-year rule. A8 §3 cites CRC art. 145.º: first enrolment takes effect on the first day of the 12th month after the start of activity. Under A8 R1 the activity is opened while he is employed, so that period has run before any exit date in this model; Fix: `A8 §3 gives the one first-year rule found: first enrolment takes effect on the first day of the 12th month after the activity starts (CRC art. 145.º); with the activity opened while employed (A8 R1), that period has run before any exit date in this model, so the 14.98% applies from the exit; whether any other regime applies was not checked (A8 R12 is open on enrolment timing).`; Basis: A8 §3, register R1 and R12.

## Confirmed
- **ECB rate.** $1.1172 per euro on 30 Oct 2026. July–October 2026 minimum $1.1130 (29 Oct) and maximum $1.1699 (21 Aug). PASS. https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/eurofxref-graph-usd.it.html
- **ISS guide 6001 v4.72, 20 Feb 2025.** "por razões alheias à sua vontade" is condition 5. "denúncia do contrato de trabalho/demissão por iniciativa do trabalhador" is given as a voluntary reason. Mutual agreement counts only for "reestruturação, viabilização ou recuperação" or "situação económica difícil". The cap is €1,306.25. PASS (the cap is stale, see findings). URL above.
- **CGD.** "pelo menos, seis meses de despesas" and "pelo menos, um ano de despesas"; page dated 09-04-2026 (the page does not label it as the publication date). PASS.
- **gov.pt exemption.** The 4 × IAS threshold and three conditions, one of them mandatory cover from the job; updated 03.09.2026. PASS. https://www.gov.pt/servicos/requerer-a-isencao-do-pagamento-de-contribuicoes-para-a-seguranca-social
- **beehiiv, 6 Jan 2026.** Generalist World has 43,000 subscribers and 700+ paying members; median 8,314 at year one; median time to first dollar 66 days. PASS. https://www.beehiiv.com/blog/the-state-of-newsletters-2026.md
- **Artificial Ignorance.** 13,413 free and 121 paid on 1 Jan 2025; post dated 11 Feb 2025. PASS. https://www.ignorance.ai/p/two-years-of-artificial-ignorance
- **Patreon via Net Influencer.** $52 per fan, $110 per paying member; 1,000 creators and 2,000 fans; 21 Feb 2025. PASS. https://www.netinfluencer.com/patreon-2025-state-of-create-report-how-creators-are-breaking-free-from-platform-control/
- **Amy Suto.** 42,000 in three years; 4 Jul 2026; nothing on the page about full-time (audit-1 erratum applied). PASS. https://www.amysuto.com/desk-of-amy-suto/how-to-grow-a-substack
- **Kajabi via Net Influencer.** 1,717 creators; brand deals down 52%, downloads up 20%, educational content up 14%; 17 Apr 2025. PASS. https://www.netinfluencer.com/creator-commerce-rises-as-platform-dependency-declines-kajabi-report-shows/
- **Kolsquare.** 783 creators, 5,000+ followers, at least one brand collaboration; 28% full-time; 23% of men under €500 a month; 7 Jul 2025. PASS. https://www.kolsquare.com/en-gb/free-resources/voices-of-the-creator-economy-by-kolsquare-newtonx
- **Influencer Marketing Hub.** Over 3,000 creators; "more than half still earn under $15,000 a year"; Aug 2025. PASS. https://influencermarketinghub.com/creator-earnings-report-2025/
- **AIR Media-Tech.** Health & Sport median RPM $1.23; 300 channels, 3,595 channel-months; 1 Jul 2026. PASS. The page says "channels AIR works with"; the label "managed" is inherited from A9. https://air.io/en/air-data-findings/which-youtube-niche-makes-the-most-money-in-2026-ranked-by-real-rpm-and-cpm
- **YPP from 1 Feb 2027.** 1,000 subscribers plus 8,000 qualified watch hours in 365 days. PASS on PPC Land, 12 Aug 2026 (https://ppc.land/new-youtube-creators-face-8-000-hour-bar-for-ad-revenue-from-february-2027/). Audit-1 verified the YouTube Help primary.
- **vidIQ uploads study.** 8.65% of 1,259,198 in the 12–51 band; 11 Sep 2026. PASS. https://vidiq.com/research/youtube-uploads-1000-subscribers/
- **vidIQ blog.** 68% of 5,330,249 channels; 9 Jun 2025. PASS; the page says "more than 40" where the unit says "40 or more", inherited from A9 row 6 and passed by audit-1. https://vidiq.com/blog/post/how-many-videos-to-get-1000-subscribers/
- **VoxBooster.** 0.40–1.20% and $48.50; 22 Aug 2026. PASS on the figures (attribution of "per drop" is a finding). URL above.
- **Summify.** Part-Time YouTuber Academy cohort 1 "brought in £220,000"; video of 28 Dec 2020. PASS. https://summify.io/discover/how-much-money-i-earn-as-a-doctor-youtuber-VTTp5A/
- **Teachery.** "about 2-3% of your email audience to purchase your mini-course"; undated page. PASS. https://make500.teachery.co/lessons/part-2-managing-expectations
- **On Substack.** 50% of new subscriptions and 25% of new paid; 22 Feb 2024. PASS. https://on.substack.com/p/substacks-recommendations-network
- **vidIQ Subscriber Benchmarks 2026.** Growth falls at every band. PASS (citation form is a finding).

**Not checked by URL (searches did not return them; the claims rest on the filed units, which carry them as stated):**
- Substack Support fees page (A7 a12)
- Socialinsider 22.0% (A7 §1)
- DL 2/2018 PDF (A8 §3)
- The Introverted Networker and The Creator's Playbook (A9 §6)

**Fetch failed:** economiafinancas.com/?p=31120 (a possible newer ISS guide). Whether a version after v4.72 exists is not checked.

## (1) Coverage
- **Household floor** (€4,800, ≈ €0, €430 to Aug 2027): covered.
- **Survivable floor with the variable second income:** covered. It is a formula with V_min and C; no amount is invented, and the brief gives none.
- **Months of runway for a sole earner:** covered. The unit says no dataset exists, bases twelve months on CGD's advice and labels it his rule.
- **Income mix:**
  - Brand deals: covered; rate and timeline marked unsourced.
  - Shōmen margin: covered; revenue from A7, margin unfilled.
  - Consulting or fractional work: covered; marked unsourced.
  - Courses: covered; Teachery reported and kept out.
- **Realistic timeline for each:** covered as far as sources allow. Only the paid tier and merch are dated.
- **Deliverable, three paths with the earliest honest date on each:** present and in full.
- **"Do not treat the current employer as failing or the exit as decided":** held (the opening paragraph, D2 line 8, the decision figure).

## (2) Accuracy
See Findings and Confirmed. From the writer's unsure list:
- Items 2 and 3: confirmed (ECB rate and range; ISS v4.72 text), apart from the stale cap.
- Item 5: partly answered by A8 §3 (minor finding).
- Items 1, 4 and 6–10 are correctly stated as open or assumed.

## (3) Figures say whose
Every number names its owner or "my arithmetic". The one exception is the vidIQ banding in §5, which has no link or date (should-fix above).

## (4) Labels
- Vendor, platform-published, company-sponsored, anecdote, bank guidance and official guidance are all labelled.
- vidIQ in §5 is labelled vendor but unlinked (finding).

## (5) Deliverable
Present in full; it follows from the evidence and can be used on its own. Issues are the pass-rule wording (i30) and the missing per-year test on Path B.

## (6) Errata applied
- **Audit 1.** "full-time" is not attached to Suto. The VoxBooster attribution is not misstated as Spring or Fourthwall. The YPP rule, the RPM, IMH, Kolsquare, the 68% figure, Patreon and Substack's 50% match the audited wording.
- **Audit 2.** Its errata touch B2 and A1 only; none apply to this unit.
- **Pointers:** see the pointers section below.

## (7) Figures
- **Figure 1, compare, §4.7.** PASS.
  - Labels and values trace to the text. 5,139.97: "**€5,139.97 a month**" (§1). 4,370: "€4,370 from September 2027" (§1). 1,019.43, 186.49 and 28.94: "€28.94, €186.49 and €1,019.43 a month" (§4.7).
  - The caption names §1 and §4.7, A7 Deliverable B, B2, and the ECB rate.
  - Kind fits (numbers compared).
- **Figure 2, decision, Deliverable D2.** PASS.
  - The questions and outcomes trace to D2 line 8 ("Until all three hold, the state is the present one: employed, building, read next quarter") and to D2 lines 4–5 (T, runway).
  - The caption names D2 line 8 and the sources.
  - Kind fits (a rule with branches).
- **Figure 3, timeline, D6.** FIX, minor. Replacement event JSON is in the findings.
  - The other dates trace: 14 Nov 2028 (§5), 11 Feb 2031 (D3), 9 Nov 2032 (§3, D2 line 6), 3 Feb 2037 (D4), 3 Nov 2037 (D2 line 6, D5).
  - The caption names D3–D5 and the sources.
  - Kind fits (dated events).

## Each Current occurs exactly once
I checked every Current with `grep -F -c` on /tmp/claude-0/a5/check-DD-A2/DD-A2-check-copy.md, and cross-checked with Python str.count for those containing quotes or $. Each returned 1. None contains a backtick or a newline.

## Calculations (re-run by script; agrees unless marked)

**§1**
- €4,800 − €430 = €4,370
- 8 × 4,800 + 4 × 4,370 = €55,880
- 0.214 × 0.70 = 0.1498; 0.214 × 0.20 = 0.0428
- T = €5,139.97 a month, €61,679.60 a year; on €4,800, €5,645.73
- €100 ÷ 0.8502 = €117.62
- The cap is 27.2% of €4,800: agrees with the €1,306.25 given, but differs for 2026: €1,342.83, 28.0%.

**§3 and D2 lines 5–7**
- €52,440 and €26,220
- 121.95 → 122 months, Oct 2037, Tue 3 Nov 2037
- 60.98 → 61 months, Sep 2032, Tue 9 Nov 2032
- 2.33 and 10.16 months

**§4.1 and D3 lines 1–4**
- Net per member $110 − $14.96 − $3.60 = $91.44 = €81.85 = €6.82 a month
- $68,908.45 → 753.6 → 754 members
- Lists: 47,125, 83,778, 15,080
- Years to the list: 56.6 / 23.6 / 5.67 / 3.37

**§4.2**
- 56.0M views a year; 2,154,736 an episode; 7,922 times the median

**§4.3**
- €500 is 11.4% of €4,370
- $15,000 = €13,426.42 a year, €1,118.87 a month

**§4.4**
- €347.30, €2,083.78, €10,418.90 a year; €28.94, €173.65, €868.24 a month

**§4.6**
- 166 to 249 buyers; 41 months

**§4.7**
- €347.30, €2,237.92, €12,233.19 a year; €28.94, €186.49, €1,019.43 a month
- 0.6%, 4.0%, 21.9% of €55,880
- Fees $1,989.68 + $478.80; net $12,161.52; €907.14 a month; 17.6%
- €868.24 is 19.9% of €4,370

**§5**
- Base and High paid-tier lines and the three totals agree with A7
- Merch is 93.1% and 85.2% of the totals
- €12,233.19; €11,682.13 to €12,279.35 (gross turnover is a minor finding)
- Checkpoints: 16 Feb, 18 May, 17 Aug, 16 Nov 2027; 15 Feb 2028; 14 Nov 2028 (31 Oct 2028 + 14 days). All Tuesdays, every 91 days.

**D2**
- Goods threshold €4,565.40 a month, €54,784.79 a year

**D3 lines 5–7**
- List 10,924 on 17 Aug 2027 (285 days × 14,000 ÷ 365.25)
- 3.37 years, March 2030 (18 Mar 2030)
- Trailing €60,075.41 / €64,655.73 / €69,236.06 (end-of-month list, unrounded members)
- 41 months × €430 = €17,630
- Cumulative receipts €160,909.41; 21.6% banked

**D3 table**
- 11 Feb 2031: agrees
- 10 May 2033: agrees
- 9 Aug 2033: agrees
- 3 Nov 2037 (0.9% at 8,314): agrees; at that point salary saving alone is €52,460
- 6 Feb 2035: agrees
- 13 Feb 2029: agrees only under D6's twelve-months-behind condition. Under i30 as written it would be 14 Nov 2028 (minor finding).
- Part-time paces: no date, agrees

**D3, per €100 of B, K or Q**
- 14.66 members and 916 on the list: agrees

**D4**
- Order €43.41
- €54,784.79 of sales; 1,262 orders, 631 per drop
- 52,584 followers (157,750 at 0.40%)
- 8.35 years
- €55,927.04 of sales; €53,533.36 after social security
- 5 Aug 2036 window €48,439.87; 4 Nov 2036 and 3 Feb 2037
- 113 × €430 = €48,590; 7.2% banked
- Table: 3 Feb 2037; 110,167 followers and 29 Jan 2041; 29 Jul 2042. All agree.

**D5**
- €3,069: agrees with A8 §3

**Every date derived from a count of months:** checked. All checkpoint dates fall on the 91-day grid from 16 Feb 2027.

## Inputs traced
- **i1–i3:** the brief (take-home €4,800; margin ≈ €0; €430 to Aug 2027). The second earner's income is handled through V_min (i5), unfilled.
- **i4:** derived. **i5–i7:** unfilled, no number invented.
- **i8:** his rule, on CGD (opened) and ISS (opened).
- **i9–i10:** A8 §3. Confirmed that A8 §3 gives 21.4%, 70% and 20%.
- **i11:** none. **i12:** ECB (opened, confirmed).
- **i13:** A9 §7 and A7 a9 (confirmed 0.9%, 1.6%, 5–10%).
- **i14:** A7 a11. **i15:** A7 a12.
- **i16:** A9 §6 for Suto, beehiiv and both anecdotes; row 13 carries three of the four.
- **i17:** A7 a7. **i18:** A7 a8. **i19:** A7 a4. **i20:** A7 a2. **i21:** A7 a1.
- **i22:** A7 §1. **i23:** A7 Deliverable A part 4. **i24:** A7 a16.
- **i28:** A9 rows 11–12. **i29:** A3 §5 (16 Feb 2027, 91 days). **i30:** his rule.
- **Other numbers:** €2,148.52 is A8 §3 and R11. $1.1130–$1.1699 is the ECB page. €1,306.25 is the ISS guide.

No untraced number.

## Public-site rules
- **No personal fact beyond the brief and filed units:** held. The half marathon, karate, coaching, SC Braga, Shōmen and the history course all come from A8 §11 and the brief. There is no location, health or family detail.
- **No private person named:** held. The brief's Cover names one; the unit says "the second earner" throughout. "Boyd's partner" is DD-A1's public case.
- **Nothing about the employer, no exit as decided, no employer as failing:** held.
  - The opening paragraph says nothing assumes the job should end.
  - "Leaving to build an independent income is a resignation" is hypothetical.
  - §4.5 says the employer's business "no filed unit states and this unit does not".
  - No company is named in connection with his job.
- **No household number beyond the brief's:** held. Only €4,800, ≈ €0 and €430, plus derivations from them. S0, C and V_min are left unfilled.

## Pointers
- **A7 Deliverable B** ($388.00 / $2,500.20 / $13,666.92): reported right and recomputed.
- **A7's treatment of the margin** (a16, B4): reported right and carried forward (m unfilled).
- **A7's "per drop" reading:** misattributed to VoxBooster, and T1 is not carried into Path B (findings).
- **A9 §8 plateau:** reported right. The "no actual path" line belongs to A9 §4–§5 (finding).
- **A9 expectation sheet rows 1, 5, 6, 11, 12, 13:** right.
- **A9 quarterly checkpoints on A3 §5's dates:** right, and the two-year review shift to 14 Nov 2028 is right.
- **A2 §3:** right (list-join rate unsourced; Substack 50%; Kajabi figures).
- **DD-A1:** right (§2 Abdaal figures and dates; §3 Boyd agent partnerships; §4 Sidibe Gymshark title; pattern 3; the quoted "Keep the job" line is exact; the "none grew on 5–7 hours" line).
- **A8:** right (§1, §2 open question, §3, §4 items 1, 2 and 6, §11 hours, R1/R3/R5/R6/R9/R10/R11/R13/R18).
- **Filed units contradicted:** none. A8 §2's open question on €15,000 is partly answered for 2027 (under €15,000 at every rate July–October 2026, gross or net). That narrows A8 §2's open question and contradicts nothing.

## Search mode
- The unit is search off and dates its three verifications to 2 Nov 2026.
- Facts that should carry a date: the vidIQ banding in §5 (finding).
- The ISS guide is dated, but its cap is the 2025 figure (finding).
- The YouTube Help YPP rule is undated in this unit and rests on A9's check of 28 Oct 2026, which is acceptable under search off.

## Proposed for memory or backlog
None.

DD-A2, verdict fix, 0 errors, 5 should-fix, 5 minor

**Maintainer's note (2 Nov 2026, the orchestrating chat of row A-5).** The checker's transcript was checked by script: no memory, Projects, past-chat, connector, Artifact or `mcp__*` tool; all 21 WebFetch calls on URLs a WebSearch in its own context had returned, copied exactly; no redirect met; nothing opened under the writer's packet, the prompts folder, its hand-back or any agent transcript. Every finding was verified before it was applied, each as an exact replacement whose Current occurred once in the unit (Python `str.count`), all ten by one script reading the pairs from this report (a Fix given as two backticked parts "then on a new line" was applied as the two lines). How each was verified:

- **1 (the benefit cap):** a search and a fetch of the ISS guide 6001 v4.72 the search returned: the cap is "duas vezes e meia o valor do IAS (1.306,25€)", the 2025 IAS; A8 §3 gives the 2026 IAS as €537.13 (Portaria 480-A/2025/1); 2.5 × 537.13 = €1,342.83, 28.0% of €4,800, by script. The same search returned an ECO report of 29 Nov 2025 putting the 2026 maximum at about €1,343. Holds.
- **2 (per drop):** a search and a fetch of VoxBooster's page: the 0.40–1.20% sentence gives no window; A7 §1 says the page does not say per drop or longer and follows its brief's per-drop reading. Holds.
- **3 (Path B per year):** Path B rebuilt by script from D1 (10,000 followers in 2027, 22.0% a year from 1 Jan 2028, drops on 4 Mar and 16 Sep, $48.50 at $1.1172, the 91-day checkpoints, two running): the existing rows come out at 3 Feb 2037, 29 Jan 2041 and 29 Jul 2042, and a per-drop rate of 0.60% (A7 B3's T1, the rate read per year) first passes at 1 May 2040, so two running at 31 Jul 2040; 631 ÷ 0.006 = 105,167. Holds; the row went in after the 0.40% row, as the Fix places it.
- **4 and 5 (vidIQ banding):** a search and a fetch of vidIQ's Subscriber Benchmarks 2026: 1.26%, 0.59%, 0.53%, 0.51%, 0.48%, 0.30%, 0.24%, published 20 Jul 2026; A9 §8 cites it with these figures and lists it in its Sources; A9 §4 and §5 carry the "not a route anyone takes" and "describes no actual path" lines. Hold.
- **6 (IVA turnover gross):** A7 B2 High line 8 is $2,438.33 gross; 11,640.00 + 2,438.33 = 14,078.33, ÷ 1.1172 = €12,601.44, ÷ 1.1699 = €12,033.79, ÷ 1.1130 = €12,648.99, by script. Holds.
- **7 (the pass rule):** D6 already states that no path passes before twelve months of side income stand behind two checkpoints running, and D3's 5% row (13 Feb 2029) holds only under it; i30 now says so. Holds.
- **8 (CGD):** a search and a fetch of CGD's page: "pelo menos, seis meses de despesas" and "pelo menos, um ano de despesas", dated 09-04-2026; two minimums, not a range. Holds.
- **9 (timeline label):** §1 says nothing is saved before September 2027. Holds.
- **10 (first enrolment):** A8 §3 quotes art. 145.º ("no primeiro dia do 12.º mês posterior ao do início de atividade"), and R12 carries it. Holds.

**Found by the chat, before the fix:** `verify.py`'s figure rules failed figure 3 (a stem ran through the text "3 Feb 2037" and "Path B, at 100% margin"), because every event sat at a whole year and the two 2037 events shared one. Each event's `at` is now its date as a fraction of the year (2027.62, 2028.87, 2031.11, 2032.86, 2037.09, 2037.84), no label or date changed; verify's figure rules then passed.

## Figure re-check 1 (2 Nov 2026, a separate Opus 5.5 agent given the unit without its figures, the captions and figure 3's frames sheets at phone, tablet and desktop, dark and light; report verbatim)

**Figure 3 re-check, DD-A2 "Deep dive: the exit math": PASS**

I opened only the files in /tmp/claude-0/a5/recheck-DD-A2-f3/. That was unit-without-figures.md, captions.md and all six sheets: desktop, tablet and phone, each in dark and light. The phone sheets have 4 frames each and were read frame by frame. To measure the dot and stem positions I wrote zoomed crops to the scratchpad. I edited nothing in the folder.

**Kind and place.** It is a timeline of six dated events. It sits in §D6 "The three dates together" (`[Figure 3 (timeline) stands here; its caption is in captions.md]`). Dated events suit a timeline.

**The fix.**
- The label now reads `Aug 2027` / `Last car-credit month; saving from Sep 2027`. This now agrees with the unit:
  - §1: `a car credit of €430 a month until August 2027` and `nothing is saved before September 2027 unless spending is cut`
  - i3: `€430 a month to August 2027`
  - §3: `From September 2027 the household can save the €430 the car credit frees`
  - D3 line 7: `salary saving from September 2027`
- The August 2027 / September 2027 contradiction is gone.
- Events now sit at their dates. On every sheet, the 3 Nov 2037 stem runs clear of the `3 Feb 2037` / `Path B, at 100% margin` label. It is to the right of the label's last character and only reaches the axis above its own label.

**Every label traced to the unit's text**
- `Aug 2027` · `Last car-credit month; saving from Sep 2027`: §1 and i3, quoted above.
- `14 Nov 2028` · `A9 two-year review`: §5, `A9's two-year review of 31 October 2028 falls on Tuesday 14 November 2028`.
- `11 Feb 2031` · `Path A: tier carries the floor`: D3, `Earliest honest date: Tuesday 11 February 2031`, and §4.1, `The earliest date the tier could carry the floor ... Tuesday 11 February 2031, at Suto's pace`.
- `9 Nov 2032` · `Six-month runway, zero savings`: §3, `The six-month runway takes €26,220 ÷ €430 = 60.98, so 61 months, to September 2032, first read at the checkpoint of Tuesday 9 November 2032`. D5 says `or Tuesday 9 November 2032 on a six-month runway`, and S0 = 0 is the default (i7).
- `3 Feb 2037` · `Path B, at 100% margin`: D4, `Earliest honest date: Tuesday 3 February 2037, and only at a margin of 100%`.
- `3 Nov 2037` · `Path C bound: twelve-month runway`: D5, `The only dated bound is the runway at k = 0: Tuesday 3 November 2037`. D2 line 6 says `first read **Tue 3 Nov 2037**`.
- The axis years run 2027 to 2037, every two years, with ticks only. No label or number in the figure is missing from the text.

I rebuilt the 91-day checkpoint chain from Tue 16 Feb 2027. Each dated event lands on a Tuesday in that chain: 14 Nov 2028, 11 Feb 2031, 9 Nov 2032, 3 Feb 2037 and 3 Nov 2037.

**Caption.** It says what the figure shows: the earliest honest date on each path, the end of the car credit, A9's review and the runway dates at zero savings. It names the sections ("Deliverable, D3 to D5") and the sources: the brief, A9 on A3's dates, Suto (anecdote), the 1.6% documented case, and VoxBooster (weakly sourced). Each basis it describes matches i13, i16, i19, i20, D4 and D5. "the end of the car credit (brief)" fits the new label. No should-fix.

**Drawing, from the sheets**
- **Placement.** On the tablet sheet the axis runs about 154.4 px a year from the 2027 tick at x≈150. The predicted dot positions match the drawn ones within 1–2 px:
  - Aug 2027 ≈ 246
  - 14 Nov 2028 ≈ 439
  - 11 Feb 2031 ≈ 785
  - 9 Nov 2032 ≈ 1055
  - 3 Feb 2037 ≈ 1708
  - 3 Nov 2037 ≈ 1824

  The phone frame 1 sheet matches at about 168.75 px a year: Aug 2027 at 269 and Nov 2028 at 481. Desktop matches in proportion.
- **No overlaps, no stem through text.**
  - The 14 Nov 2028 stem is the closest call. It passes to the right of "Last car-credit month;". On the phone sheet the label ends at x=447 and the stem is at x=480–481, about 11 CSS px of clear space. Desktop and tablet are also clear.
  - The A9 label (second row) does not touch "Path A: tier carries / the floor" (first row).
  - "Six-month runway, zero savings" and "Path B, at 100% margin" are well apart.
  - "twelve-" / "month runway" breaks at the word's own hyphen.
- **Legibility and wholeness.** Every label is whole and readable at desktop and tablet, in both themes, where one frame holds the whole figure.
  - On the phone, each label is whole in at least one frame:
    - Aug 2027 and 14 Nov 2028: frame 1
    - 11 Feb 2031: frames 1 and 2
    - 9 Nov 2032: frame 2
    - 3 Feb 2037: frames 3 and 4
    - 3 Nov 2037: frame 4
  - The faded "Six-", "Pa" and "3 Nov 2037" at the frame edges are the scroll fade, and each is whole in the next frame.
  - The axis is continuous across frames 1–4. The "scroll sideways for the whole figure" hint is present.
  - In dark and light, the dots, stems, labels and mono dates all keep adequate contrast.

No replacement JSON or caption is needed.

**Notes on the unit's text**

I found no errors. The month counts and dates I recomputed hold:
- 122 months from Sep 2027 ends Oct 2037; 61 months ends Sep 2032.
- 41 months from Sep 2027 to Jan 2031; 113 months to Jan 2037.
- Path A's list reaches 47,125 in March 2030.

Optional, no fix needed: in the figure only the six-month label says "zero savings", while the twelve-month Path C label does not. The caption's "runway dates at zero savings" covers both.

Nothing in this report came from memory.

**Maintainer's note on the figure re-check (2 Nov 2026).** The re-checker's transcript was checked by script: no web, memory, Projects, connector or Artifact tool. It read every file of its folder and nothing else of the row's; to measure positions it wrote zoomed crops of its own frames sheets to the session scratchpad and to a sibling folder, and read back only those crops, outside the folder it was told to keep to; nothing it read there was other than its own sheets. Figure 3 passed (no finding). Its one optional note (only the six-month label says "zero savings") needs no change, as it says: the caption covers both runway dates. Figures 1 (compare) and 2 (decision) passed the fresh check; figure 3 (timeline) was fixed and passed its re-check. None dropped. At phone width the compare figure's values scroll away from their row labels: that is the renderer change already queued as P83, recorded on that row.
