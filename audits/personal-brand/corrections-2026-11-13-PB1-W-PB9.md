---
audit: correction check (docs/public-courses.md §3 rule 12; steps 6 and 7b of row W-PB9)
units: PB1 (C1, source error found by PB9's fresh checker; C2 and C3, contradictions found by PB9's writer, flag F58); register (C2)
course: personal-brand · PB · Building a Personal Brand on Instagram and YouTube
model: Opus 5.5 (claude-opus-5-5, as the agent states; this session keeps no agent transcript on disk; live search)
date: 2026-11-13
chat: own Opus 5.5 agent context, not shown the chat's reasoning (P31), launched by the W-PB9/W-PB10 chat in session https://claude.ai/code/session_01KMmgR1xZNfEBXV8FGL7SYn
verdict: C1, C2, C3 PASS (C2 and C3 reworded by the checker), no syllabus conflict; 4 new items (worked in round 2)
---

The checker's final report, verbatim, as the file it wrote in its own folder (`out/correction-check.md`), copied unchanged by script before any change was applied. The exact strings applied are its `out/edits.json`.

Model: claude-opus-5-5

# Correction check, row W-PB9: C1 to C3 (2026-11-13)

Sources: the files in /home/claude/stage/corr3/. Two web pages, each fetched from a URL that a WebSearch in this run returned word for word: YouTube Help 12843009 and the CTT tariff PDF. Each `current` was checked with `str.count` == 1, and checked again after the earlier edits to the same file had been applied in order (script run on copies). Every change below passes. `out/edits.json` holds all of them, the notes included.

## C1 · PB1 §4 table, line 101

- **id**: C1. **File**: PB1-what-to-expect-odds-timeline-cost.md
- **Current** (1 occurrence): `channels already in the programme keep their status, provided they accept the updated terms in YouTube Studio by 31 January 2027, without which they stop earning from the affected features from 1 February 2027`
- **Replacement**: `for channels already in the programme, status is not affected by the update or by whether they accept the updated terms; earning from the associated features from 1 February 2027 needs those terms accepted in YouTube Studio by 31 January 2027`
- **PASS.** YouTube Help 12843009, fetched 13 Nov 2026, says: "If you are already in YPP, your status is not impacted by this update." It also says: "To continue fully monetizing your content, review and accept the updated terms in YouTube Studio by January 31, 2027." On missing the deadline it says: "Starting February 1, 2027, if you haven't accepted the terms, you'll stop earning from the associated monetization features". It adds: "Your decision to accept these terms does not impact your channel's status in the YouTube Partner Program." The old cell made status depend on acceptance, and the page says it does not.
- **Syllabus**: no conflict. PB9 §2 (line 42) already states the page this way, so the change brings PB1 into line with PB9. No brief relies on the old wording. DD-PB2's brief asks for "each income line of PB9 with the timeline the evidence supports", which this change does not touch. The register has no entry on it.
- **Note** (N-C1, anchored on PB1's current last unsure-list line, the 12 Nov paragraph on PB4's correction):
  `- Correction 2026-11-13, found by PB9's fresh checker: §4's row for the 1 February 2027 entry said channels already in the Partner Programme keep their status provided they accept the updated terms by 31 January 2027; YouTube Help 12843009 says their status "is not impacted by this update" and that the decision to accept the terms does not affect it either, acceptance governing only earning from the associated features from 1 February 2027; the cell now says so (row W-PB9).`

## C2 · PB1 D3 read 1, and the register's PB7 entry

- **id**: C2-PB1. **File**: PB1-what-to-expect-odds-timeline-cost.md
  - **Current** (1): `(7 or 6 videos; 39 posts)`
  - **Replacement**: `(7 or 6 videos; 39 posts, 31 in Q2 if PB9's guide build is decided at the Q1 review)`
- **id**: C2-register. **File**: case-facts.md
  - **Current** (1): `27 Reels and 12 carousels in Q1, 25 and 14 in Q2`
  - **Replacement**: `27 Reels and 12 carousels in Q1, 25 and 14 in Q2 (17 and 14 if PB9's guide build is decided at the Q1 review: two Reels fewer in each of the four fortnights cut on 25 Apr, 9 May, 23 May and 6 Jun 2027)`
- **PASS, with the condition reworded.**
  - PB9 D1 says the four 1.0-hour blocks come from "the cut windows of Sundays 25 April, 9 May, 23 May and 6 June 2027: in each of those fortnights two Reels are not made (six posts become four)".
  - Dates checked by script against day one, Mon 4 Jan 2027 (week 1 is a week A). All four are Sundays of week B: weeks 16, 18, 20 and 22. Each cut window feeds uploads 9 to 12 (27 Apr, 11 May, 25 May, 8 Jun), and upload 12 on 8 Jun is the launch PB9 names. The posts they feed run from 27 Apr to 19 Jun, all inside Q2 (Mon 5 Apr to Sun 4 Jul; review on 5 Jul).
  - Q2 baseline: PB7 §D2 gives "39 more posts (25 Reels, 14 carousels)". With the guide build that becomes 8 Reels fewer: 39 − 8 = 31 posts, and 25 − 8 = 17 Reels with 14 carousels.
  - Why the condition changed: PB9 D1 says the guide is "Decided at the Q1 review, Monday 5 April 2027, if register line T1 has been answered by a tax professional; otherwise the launch moves to the first upload after it is." Under that rule the build can happen and still miss Q2, so "if PB9's guide build runs" would be wrong in that case. The condition that actually decides the Q2 count is "decided at the Q1 review". In the register line I also named the four cut dates as the fortnights' cut windows. The fortnights themselves run 26 Apr to 20 Jun, so "fortnights, 25 Apr to 6 Jun" would have been loose.
- **Syllabus**: no conflict.
  - PB10's brief relies on "PB1's seven reads" and on "setting the quarter against PB1's expectation sheet". Read 1 stays a read against plan, and only the Q2 plan figure gains a condition.
  - PB7's IR11 format test at the Q2 review ("carousels' median non-follower views across Q1 and Q2 equal or beat Reels'") still has Reels in both quarters.
  - The change does not contradict PB4's cut-window pattern in the register ("cut window Sunday of week B, 10:00, 4.5 hours (packaging 1.0, six Instagram posts 3.0 …)"). Two Reels at 30 minutes each make the 1.0 hour.
- **Note** (N-C2, anchored on N-C1):
  `- Correction 2026-11-13, found by PB9's writer: D3 read 1 now gives 31 posts for Q2 if PB9's guide build is decided at the Q1 review (PB9 D1: two Reels fewer in each of the fortnights cut on 25 Apr, 9 May, 23 May and 6 Jun 2027); 39 stands otherwise (row W-PB9).`

## C3 · PB1 D2 money table (flag F58)

- **id**: C3. **File**: PB1-what-to-expect-odds-timeline-cost.md
- **Current** (1): `| Contingency | 11 USD | The remainder of the cap |`
- **Replacement** (new row inserted before Contingency):
  `| Postal address for commercial email (PB8 E4) | 58.00 € + VAT a year (CTT tariff, Nov 2020; current price to check) | Paid from the unspent microphone line (PB5 §2) at the day's rate, not added to the cap; the cap stands unless the converted price exceeds what remains under it (PB9 D2 V17) |`
  `| Contingency | 11 USD | The remainder of the cap |`
- **PASS, with the text changed from the proposal.**
  - CTT PDF (fetched 13 Nov 2026). Header: "Preços 2020" / "novembro/2020". Section "SERVIÇOS ESPECIAIS". Apartados, "Concessão Anual": Singulares "58,00 €" (Coletivos 80,00 €). Note (a): "Preços sujeitos a aplicação de IVA à taxa legal em vigor".
  - The price, the box type, the individual rate and the "+ VAT" all hold. The document shows no day: the "1 Nov" in the proposal comes from the file name only, so the row says "Nov 2020".
  - Columns: the row has three cells (Item | Amount | Basis) and fits the table.
  - Arithmetic: the table sums to its cap (0 + 0 + 0 + 99 + 40 + 11 = 150 USD). Adding an unconverted euro amount as a further line would break that sum. The proposed row only gave its funding source in the Basis column, so its Amount read as an addition. The replacement says plainly that the amount is paid from the 99 USD microphone line and is not added. The microphone line is unspent per PB5 §2 ("She buys no microphone; PB1's microphone line stays unspent") and §10.
  - Whether 58 € + VAT fits under 99 USD once converted cannot be confirmed here: no exchange rate or VAT rate is sourced in these files. The row therefore carries PB9's own fallback: "if it exceeds what remains under the cap, PB1's D2 is corrected" (PB9 D3).
  - Brief PB1 requires that "an amount appears in its source's currency with its date". The row meets this, and so does P102 in the register ("Amounts keep their source's currency and date"). No country's tax rate is stated.
- **Syllabus**: no conflict.
  - F58 says: "if it breaks PB1's cap, PB1 D2 is corrected then". The row records the cost without breaking the cap, which that line allows.
  - The register's PB5 entry has "no microphone bought, PB1's microphone line unspent", which agrees. Its PB1 money entry stays true, since the cap and the 11 USD contingency are unchanged.
  - PB10's brief needs read 7 ("Money spent against the 150 USD cap"), which still works.
- **Note** (N-C3, anchored on N-C2):
  `- Correction 2026-11-13, found by PB9's writer: D2 gains a line for the postal address PB8 register E4 requires, 58.00 € + VAT a year on CTT's tariff dated November 2020 (Apartado, Singulares, concessão anual; prices subject to VAT), paid from the unspent microphone line (PB5 §2) at the day's rate; the current price was not checked, and the cap stands unless the converted price exceeds what remains under it (PB9 D2 V17; flag F58; row W-PB9).`

**Where the notes go.** PB1's unsure list ends in two prose correction paragraphs, after its last bullet ("- Fresh check 2026-11-12 …"). The first note is anchored on the final paragraph (PB4's correction of 12 Nov) and preceded by a blank line, so it renders as a list. Each later note is anchored on the note before it.

## edits.json

`out/edits.json` has two keys:
- `PB1-what-to-expect-odds-timeline-cost.md`: C1, C2-PB1, C3, N-C1, N-C2, N-C3
- `case-facts.md`: C2-register

A script reloaded the JSON and applied each file's list in order to a copy. Every `current` was found exactly once at the point it is applied.

## New

1. **PB7 now disagrees with C2.** PB7 §D2 line 258 ("39 more posts (25 Reels, 14 carousels)") and row IG1 ("39 planned (27 Reels, 12 carousels)") do not carry PB9's condition. After C2 they disagree with the register and with PB1 read 1 whenever the guide is decided at the Q1 review. Proposed: give PB7 the same condition. No correction in this set covers it.
2. **The tariff date in PB9 is wrong.** PB9 cites CTT as "1 Nov 2020" in D2 V17, in Sources and in the unsure list. The document shows only "novembro/2020", and "1nov" is the file name. Proposed: change it to "Nov 2020". PB9 also labels the tariff "Platform-official". CTT is the postal operator, not a platform, so "operator's own tariff" would be more exact.
3. **The register has not caught up with PB9.** case-facts.md has no "Set by PB9" section: nothing on the guide, its cut windows, its launch on 8 Jun 2027, V17, or the brand-deal rules from Season 3. PB8's "Left free" list still includes "the price of the postal address", which PB9 V17 has now set (as a stale 2020 tariff). The C2 register change points to a PB9 decision that the register does not yet record.
4. **The C3 row depends on PB5.** If a later piece fails the audio check and the microphone is bought (PB5 §2: "the check is re-run if a piece needs a noisier tool"), the address has no funding line and the 150 USD cap would break. The row's own fallback, "the cap stands unless …", covers this only partly.
