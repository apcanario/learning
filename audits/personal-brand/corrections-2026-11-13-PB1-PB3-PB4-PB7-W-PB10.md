---
audit: correction check (docs/public-courses.md §3 rule 12; steps 6 and 7b of row W-PB10)
units: PB1, PB3, PB4, PB7, register (C1 to C4 applied); PB4 §1 and the register (C5, held for round 2)
course: personal-brand · PB · Building a Personal Brand on Instagram and YouTube
model: Opus 5.5 (claude-opus-5-5, as the agent states; this session keeps no agent transcript on disk; live search)
date: 2026-11-13
chat: own Opus 5.5 agent context, not shown the chat's reasoning (P31), launched by the W-PB9/W-PB10 chat in session https://claude.ai/code/session_01KMmgR1xZNfEBXV8FGL7SYn
verdict: C1 to C4 PASS, no syllabus conflict; C5 PASS on the units but conflicts with the register unless the register line changes with it (round 2)
---

The checker's final report, verbatim, as the file it wrote in its own folder (`out/correction-check.md`), copied unchanged by script before any change was applied. The exact strings applied are its `out/edits.json`.

Model: claude-opus-5-5

# Correction check, row W-PB10 (C1 to C5), 13 Nov 2026

Verdict: C1, C2, C3 and C4 PASS with no syllabus conflict and are in `out/edits.json` (13 entries over five files, four of them notes). C5 PASSES on the units and the register, but it conflicts with the register's PB4 line, which C5 does not name, so it is held out of `edits.json` and listed under New. Every Current was checked with Python `str.count` == 1, in order, on a copy (`out/build.py`, result "ALL OK"). No source file was edited.

Web: two WebSearches. Two fetches, both of URLs returned verbatim by those searches, and both were opened: buffer.com/library/how-often-to-post-on-instagram/ and developers.facebook.com/docs/instagram-platform/api-reference/instagram-user/insights.

## C1 · the review's hour (Source error 1)

**C1a** · `PB1-what-to-expect-odds-timeline-cost.md` (D2)
- Current: `The quarterly review (60 minutes, PB10) is taken from that fortnight's publishing-and-replies line.`
- Replacement: `The quarterly review (60 minutes, PB10) is taken from the Instagram derivatives of the fortnight that holds it: that fortnight's cut window makes four posts in place of six, two Reels fewer (PB10 §5).`

**C1b** · `PB4-the-content-system.md` (D1 G)
- Current: `(PB1, D3; PB10 runs it), its hour taken from that fortnight's publishing-and-replies line (PB1, D2);`
- Replacement: `(PB1, D3; PB10 runs it), its hour taken from that fortnight's cut window, two Reels fewer (PB1 D2; PB10 §5);`

**C1c** · `PB4-the-content-system.md` (D2, "After week 12")
- Current: `(week 14), its hour taken from that fortnight's publishing-and-replies line (PB1, D2), with`
- Replacement: `(week 14), its hour taken from that fortnight's cut window, two Reels fewer (PB1 D2; PB10 §5), with`
- The bare phrase occurs twice in PB4, so each Current carries its own context.

**PASS** (rests on the units and register). Register, PB3 entry: "publishing and replies 1.25". Register, PB4 entry: "replies Wednesday and Friday of week A and Wednesday of week B, 0.25 each" and "cut window ... (packaging 1.0, six Instagram posts 3.0, scheduling 0.5)". That gives 0.75 + 0.5 = 1.25, so 60 minutes would take all the replies and half the scheduling. PB10 §5: "The hour is therefore taken ... from the Instagram derivatives of the fortnight that holds the review. That fortnight's cut window makes four posts in place of six, two Reels fewer".

**Syllabus:** no conflict.
- brief-PB1 "Gives: ... the hours budget PB3 and PB4 allocate": the 12 hours are unchanged.
- brief-PB4 "Gives: ... the cadence PB6, PB7 and PB10 measure": the video cadence is unchanged. The Instagram cadence loses two posts a quarter, the same trade the register already records for PB9 ("two Reels fewer in each of those fortnights (six posts become four)").
- PB1 D3 verdict 2 ("Instagram derivatives drop from six a fortnight to four") is the same order.
- Flag F5 is answered by PB10's writer: "posting rates kept ... PB1's rows Y1, Y4, Y5, I4 and its stop rule re-read and stand".
- The resulting count changes are C4.

## C2 · Buffer's increment used as a total (Source error 2)

**C2a** · `PB1-what-to-expect-odds-timeline-cost.md` (D3, Q3 line)
- Current: `Compare net subscribers per month with the band median (+0.5, +1.4 or +3.7; Y6) and Instagram net followers with the 0.36-a-week illustration (I4). Above the median is the upper tail that channels crossing 1,000 come from.`
- Replacement: `Compare net subscribers per month with the band median (+0.5, +1.4 or +3.7; Y6). Above the median is the upper tail that channels crossing 1,000 come from. Instagram net followers are recorded with no benchmark: no dataset found follows accounts from under 1,000 followers (§3; I7), and I4 is an increment over weeks without posts, not a total.`
- Changed from the writer's text in two ways:
  - The Instagram sentence moves after "Above the median ...", so that sentence still follows the subscriber comparison it refers to.
  - "no dataset gives a total for her size (I7)" becomes PB1 §3's own wording ("No dataset found follows new personal accounts from under 1,000 followers").

**C2b** · `PB7-how-instagram-growth-works.md` (D2, IG8 reference column)
- Current: `3 posts a week at 140 followers ≈ 0.36 a week (PB1 I4, derived)`
- Replacement: `Buffer's +0.26% (PB1 I4) is an increment over weeks without posts, not a total, and places her posting rate only (IG1)`
- Only the 0.36 item is replaced. The writer's whole-column text would also have dropped the Socialinsider item and the I7 item, which C2 does not name.

**PASS.** Buffer, 13 Aug 2025 (fetched; the page shows "Aug 13, 2025"):
- The analysis measured growth "compared to weeks when users don't post at all".
- Its 5,000-follower example assumes "when I don't post at all, my account remains stagnant (my baseline growth rate is 0%)". The no-post baseline is an assumption of the example, so +0.26% is an increment, not an expected total.
- This matches PB1 §3: "so they are points added to the weekly growth rate".

**Syllabus:** no conflict. PB10 §4 already reads it this way: "I4 places her posting rate in Buffer's band (IG1); net followers (IG8) are recorded with no benchmark." brief-PB7 asks for "which PB1 row it is set against". IG8's PB1-row column still lists I1, I4 and I7, and the reference cell now says what I4 does.

## C3 · PB3 trait 8, the API qualifier (Source error 3)

**C3** · `PB3-audience-and-the-two-platforms.md` (D1 trait 8)
- Current: `Unknown. Instagram returns follower demographics from 100 followers (she has 140);`
- Replacement: `Unknown. Meta's developer reference does not return follower demographics through the API under 100 followers (she has 140); whether the app uses the same threshold was not checked;`
- The cell's YouTube clause that follows is kept.

**PASS.** Meta for Developers, Instagram Account Insights (fetched; an API reference page for the insights endpoint). The follower_demographics row reads: "Not returned if the IG User has less than 100 followers." PB3 §1 and its unsure list already say the app was not checked.

**Syllabus:** no conflict. It matches flag F55 ("PB10 keeps the 'API' qualifier") and PB10 §5. It does not touch the register's PB3 entry ("trait 8 ... unknown until her own data shows them").

## C4 · Instagram counts after each review takes two Reels (Contradiction 1)

These were built against the files as they are now.

**C4a** · `PB1-what-to-expect-odds-timeline-cost.md` (D3 read 1)
- Current: `(7 or 6 videos; 39 posts, 31 in Q2 if PB9's guide build is decided at the Q1 review)`
- Replacement: `(7 or 6 videos; 39 posts in Q1, 37 in Q2, Q3 and Q4, 29 in Q2 if PB9's guide build is decided at the Q1 review)`

**C4b** · `PB7-how-instagram-growth-works.md` (end of D2)
- Current: `when 39 more posts (25 Reels, 14 carousels; derived from the same post order; 31, with 17 Reels, if PB9's guide build is decided at the Q1 review)`
- Replacement: `when 37 more posts (23 Reels, 14 carousels; derived from the same post order, less two Reels for the Q1 review's hour, PB10 §5; 29, with 15 Reels, if PB9's guide build is decided at the Q1 review)`

**C4c** · `case-facts.md` (PB7 entry)
- Current: `25 and 14 in Q2 (17 and 14 if PB9's guide build`
- Replacement: `23 and 14 in Q2, two Reels fewer in the fortnight cut on Sun 11 Apr 2027 for the Q1 review's hour (PB10 §5, D3) (15 and 14 if PB9's guide build`
- As the checker required, this replaces "25 and 14 in Q2 (17 and 14" as a whole. PB9's four guide dates that follow are kept.

**PASS** (rests on the units and register).
- Register, PB7 entry: "27 Reels and 12 carousels in Q1, 25 and 14 in Q2 (17 and 14 if PB9's guide build ...: two Reels fewer in each of the four fortnights cut on 25 Apr, 9 May, 23 May and 6 Jun 2027)".
- PB10 §5: "each review takes two Reels from the quarter after it, so Q2, Q3 and Q4 each plan 37 posts in place of 39, and Q2 plans 29 if the guide is built". PB10 D3: "Hours for this review: two Reels fewer in the cut window of Sun 11 April". PB10 D4 IG1: "Plan 29: 39, less two Reels for the Q1 review's hour, less eight for the guide (15 Reels, 14 carousels)".
- Arithmetic: 39−2=37; 25−2=23; 37−8=29; 23−8=15. 11 Apr 2027 is the Sunday of week 14 (week B), which is not one of PB9's four dates, so the two cuts do not overlap.
- Q1 is unchanged: its review's cut window falls in Q2, and the twelve-month review's falls in year two.
- The condition wording matches PB9 D1 ("Decided at the Q1 review, Monday 5 April 2027").
- PB7 D1 IR1 and IG1 give Q1 figures only (27 Reels, 12 carousels; 39 planned) and need no change.
- The register's PB9 entry states no counts ("two Reels fewer in each of those fortnights (six posts become four)") and needs no change.

**Syllabus:** no conflict. brief-PB7 "Gives: the Instagram rows of PB10's metrics sheet" is unaffected. IR11's test ("across Q1 and Q2") still has both quarters, and PB10 D4 runs it on these counts.

## C5 · PB4 §1, the weekends-per-piece rule (Contradiction 2)

**C5** · `PB4-the-content-system.md` (§1). Proposed only; **not in edits.json.**
- Current (count 1): `If her log shows pieces averaging more than two weekends, the promise holds and the cadence changes: at a checkpoint she moves to one video every four weeks, the cadence PB3 set for 3 hours a week, and re-reads PB1's posting-rate rows the same day.`
- Replacement (no "..."): `If her log shows two or more pieces in a quarter taking more than two weekends, in two consecutive quarters, the promise holds and the cadence changes: at the checkpoint that closes the second of those quarters she moves to one video every four weeks, the cadence PB3 set for 3 hours a week, and re-reads PB1's posting-rate rows the same day (PB10 §5).`
- No numbers are added, so nothing has to be reconciled with 7 and 7 against 7 and 6.
- I checked PB10 §5's own figures. Seven-piece quarters: 26.4% and 73.7% for one quarter; squared, 6.9% and 54.3%. A six-piece quarter followed by a seven-piece quarter: 0.207 × 0.264 ≈ 5.5% and 0.649 × 0.737 ≈ 47.8%. Both pairs match §5 as written ("about 7%"/"54%"; "about 5% and 48%").

**PASS against the units and register.** PB10 §5: "the move is made when two or more pieces in a quarter took more than two weekends, in two consecutive quarters (her rule, built on PB1's two-quarter stop rule)". PB10 D3: "PB4's cadence move: no (one piece of seven over two weekends; the rule needs two in each of two quarters)". The Q1 and Q2 piece counts are 7 and 6 (uploads 1–7, 8–13).

**Syllabus: CONFLICT.** The register's PB4 entry reads "if pieces average more than two weekends she moves to one video every four weeks at a checkpoint (§1)". Changing §1 alone would leave PB4 contradicting the register, and C5 does not name the register. The change is held until the register line is corrected in the same edit (see New 1). No brief relies on the averaging wording: brief-PB4 says only "the cadence PB6, PB7 and PB10 measure".

## Note lines (in edits.json, each anchored on its file's last line)

- PB1: `- Correction 2026-11-13, found by PB10's writer: D2 now takes the quarterly review's hour from the Instagram derivatives of the fortnight that holds it, two Reels fewer, since PB3 D2 and PB4 D1 E left the publishing-and-replies line no hour to give (PB10 §5); D3's Q3 line no longer compares Instagram net followers with the 0.36-a-week illustration, because I4 is an increment over weeks without posts, not a total (Buffer, 13 Aug 2025; §3); D3 read 1 now gives 39 posts in Q1 and 37 in Q2, Q3 and Q4, 29 in Q2 if PB9's guide build is decided at the Q1 review (row W-PB10).`
- PB3: `- Correction 2026-11-13, found by PB10's writer: D1 trait 8 restores the qualifier dropped from §1: the 100-follower threshold is Meta's developer reference for the API ("Not returned if the IG User has less than 100 followers"), and the app's threshold was not checked (flag F55; row W-PB10).`
- PB4: `- Correction 2026-11-13, found by PB10's writer: D1 G and D2 ("After week 12") now take the quarterly review's hour from that fortnight's cut window, two Reels fewer, in place of the publishing-and-replies line, which D1 E fills with three reply slots and the cut window's scheduling (PB1 D2; PB10 §5; row W-PB10).`
- PB7: `- Correction 2026-11-13, found by PB10's writer: IG8's reference column no longer sets Buffer's increment (0.36 a week at 140 followers) as a reference for net followers, since I4 is an increment over weeks without posts, not a total (PB1 §3, I4); the Q2 count at the end of D2 now gives 37 posts (23 Reels), 29 (15 Reels) if PB9's guide build is decided at the Q1 review, each review's hour taking two Reels from the quarter after it (PB10 §5); Q1's figures are unchanged (row W-PB10).`
- case-facts.md is not a unit and gets no note.

## New

1. **C5 with its register companion, as one change (proposed).**
   - In `case-facts.md`, replace `if pieces average more than two weekends she moves to one video every four weeks at a checkpoint (§1)` (count 1) with `if two or more pieces in a quarter take more than two weekends, in two consecutive quarters, she moves to one video every four weeks at the checkpoint that closes the second (§1; PB10 §5)`.
   - Apply it together with C5 and a PB4 note, appended after the C1 note: `- Correction 2026-11-13, found by PB10's writer: §1's cadence rule now moves her to one video every four weeks when two or more pieces in a quarter take more than two weekends, in two consecutive quarters, in place of a mean above two weekends, which one three-weekend piece in seven would trigger (PB10 §5; row W-PB10).`
2. The register has no PB10 section yet. Among the facts PB10's writer lists, "review hours from two Reels in the review fortnight" is the one that C1 and C4 rely on, and it belongs with the filing.
3. Flags F5, F22, F48, F55 and F65 are still marked open in `flags.md`. F65's text ("39 posts a quarter") predates C4. Carrying or closing them is the filing chat's job; flags.md was not edited.
4. Checked; no change needed:
   - PB1 D1 row I4's last column ("3 a week at 140 followers: about 0.36 followers a week") and PB7 §8 already describe 0.36 as an increment. C2 names only D3 and IG8.
   - PB7's earlier W-PB9 note ("31 posts (17 Reels)") is a dated record and stays.
