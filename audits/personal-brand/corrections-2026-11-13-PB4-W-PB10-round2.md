---
audit: correction check, round 2 (docs/public-courses.md §3 rule 12 (f); step 7b of row W-PB10)
units: PB4 §1 (C5) and the register's PB4 line, with a PB4 note
course: personal-brand · PB · Building a Personal Brand on Instagram and YouTube
model: Opus 5.5 (claude-opus-5-5, as the agent states; this session keeps no agent transcript on disk; no web)
date: 2026-11-13
chat: own Opus 5.5 agent context, not shown the chat's reasoning (P31), launched by the W-PB9/W-PB10 chat in session https://claude.ai/code/session_01KMmgR1xZNfEBXV8FGL7SYn
verdict: C5, C5-register, C5-note PASS; 2 notes (PB10 §5 quotes PB4's old wording, left as P108; the register's PB10 section already exists)
---

The checker's final report, verbatim, returned as text and copied here unchanged before any change was applied. The exact strings applied are its `out/edits.json`.

Model: claude-opus-5-5

**All three changes PASS.** I wrote `/home/claude/stage/corr7/out/edits.json` with two files: `PB4-the-content-system.md` [C5, C5-note] and `case-facts.md` [C5-register]. A script applied the edits in order to copies in /tmp/c7s/copy. Before each edit its Current occurred exactly once (`str.count`), and afterwards its replacement occurred exactly once.

**C5 (PB4 §1, line 48): PASS.** Current count is 1. The replacement agrees with:
- PB10 §5: "the move is made when two or more pieces in a quarter took more than two weekends, in two consecutive quarters (her rule, built on PB1's two-quarter stop rule)".
- PB10 H4 row: "Cadence move: 2+ pieces over 2 in two consecutive quarters (§5)".
- PB10 D3: "PB4's cadence move: no (one piece of seven over two weekends; the rule needs two in each of two quarters)". D3 H4 gives 2, 2, 2, 2, 3, 2, 2. D4 H4 gives "Pieces 8–13: 2 weekends each", so no move is triggered in Q1 or Q2.
- PB1 D3 uses the same two-quarter logic: "fewer than 3 YouTube videos in each of two consecutive quarters".
- §5's figures recompute correctly: 26.4% and 73.7% for one quarter, 6.9% and 54.3% squared, about 5.5% and 47.8% with a six-piece then a seven-piece quarter. The old rule's mean is 2.14.

**C5-register (case-facts.md line 58): PASS.** Current count is 1. The new line matches the new PB4 §1 and PB10 §5. It also matches register line 129 ("piece 5 took three weekends"), which is one piece in Q1 and none in Q2. After the edits, no "averag" remains in either copy.

**C5-note (PB4): PASS.** PB4's current last line, the last line of the unsure list, is line 433: the C1 note from today, "- Correction 2026-11-13, found by PB10's writer: D1 G and D2 ("After week 12") now take…". The new note is anchored on that line and appended after it, in the same format.

**Briefs and other units checked:**
- brief-PB4 only says "the cadence PB6, PB7 and PB10 measure", so nothing in it is contradicted.
- brief-DD-PB2 takes PB10 and does not depend on the averaging wording.
- PB4's 3-hour rule ("a piece may take four weekends") and the checklist (line 219, "only pieces estimated at two weekends unless the bank holds…") are unaffected.
- No other line in PB4, PB1 or the register refers to averaging.

**Flags (not FAIL):**
1. PB10 §5 still quotes PB4's old wording ("If her log shows pieces averaging more than two weekends") as the rule it reinterprets. That quote will no longer appear in PB4. It doesn't contradict anything: PB10 says it reads the rule this way "from here on", and the new PB4 note records the old rule. It is a stale quote, though; a PB10 note line could be proposed.
2. Item 2 of corrections.md ("The register has no PB10 section yet") is wrong. case-facts.md already has "## Set by PB10 …" at line 126, and line 128 already records the review hour "taken from two Reels in the cut window". Nothing needs adding.
