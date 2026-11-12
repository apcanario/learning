---
audit: correction check, second round (docs/public-courses.md §3 rule 12 (f))
units: PB1, PB5, PB6, case-facts.md (knock-ons 10 to 14 of `corrections-2026-11-12-P99-P100.md`)
corrections: P99 (flags F36, F37), P100 (flag F42)
course: personal-brand · PB · Building a Personal Brand on Instagram and YouTube
model: Opus 5.5 (claude-opus-5-5, as the agent states; no agent transcript on disk; live search)
date: 2026-11-12
chat: own Opus 5.5 agent context, not shown the chat's reasoning nor the first round's checker (P31), launched by the W-PB7/W-PB8 chat in session https://claude.ai/code/session_01KMmgQyAmFapUaWMYDKogYn
verdict: all five PASS, three notes' wording corrected; nothing left open
---

The checker's final report, verbatim, from its hand-back in the chat (the harness's indentation of the hand-back is removed). Saved before any change was applied.

Model: claude-opus-5-5

Round-2 correction check of changes 10 to 14. All five pass, with three wording fixes, all in the dated notes and the register entries. Every Current below was counted with Python str.count on the files as they now stand, and each occurs once. I checked two sources on the web on 12 Nov 2026:
- **Answer 7628154** (en-GB page; the URL came from my own search): "If a video gets a lot of impressions (such as if it appears on the homepage), it's natural for the CTR to be lower."
- **Answer 16559651** (the URL my search returned was the hl=ja page, so I fetched that one): its title is "Good to know about recommendations for YouTube's recommendation system". It says "such changes are recommended when a video has a lower click-through rate (CTR) and is receiving fewer impressions than usual."

I wrote no out/ file because the brief said not to write files. rules.txt asks for one, so the two instructions conflicted.

---

## 10. PB1 Sources: add answer 16559651
1. **Current** (count 1), in units/PB1-what-to-expect-odds-timeline-cost.md:
`- YouTube Help, "Create a live stream on mobile" (answer 9228390), checked 12 Nov 2026. https://support.google.com/youtube/answer/9228390?hl=en`
2. **Replacement:** that line, a newline, then:
`- YouTube Help, "Good to know about recommendations for YouTube's recommendation system" (answer 16559651), checked 12 Nov 2026. https://support.google.com/youtube/answer/16559651?hl=en`
   - Alphabetical order is right: "Create" < "Good" < "Impressions" < "The YouTube Partner".
   - The entry does not exist yet (the count of "Good to know about recommendations" in PB1 is 0).
   - It is identical to PB6 Sources line 323.
3. **PASS.** The page title as fetched is "Good to know about recommendations for YouTube's recommendation system". PB1 verdict 3 already cites the page: "([YouTube Help 16559651](https://support.google.com/youtube/answer/16559651?hl=en))".
4. **Syllabus:** no conflict.
5. **Dated note:** needed, not optional.
   - PB1's notes record changes to its Sources (the 12843009 note: "(§4 table, twice, and Sources)"). Without a note this line would change with no record.
   - Adding it to the existing F42 note is right: the line completes the F42 correction itself, which already cites 16559651, so the note keeps "found by PB6's writer".
   - **Current** (count 1): `(YouTube Help, answers 7628154 and 16559651) (flag F42).`
   - **Replacement:** `(YouTube Help, answers 7628154 and 16559651, the latter added to Sources) (flag F42).`

## 11. PB1 D3 read 4
1. **Current** (count 1): `4. YouTube: click-through rate and percentage viewed for each upload at least 7 days old (Y2, Y3).`
2. **Replacement** (as proposed): `4. YouTube: click-through rate, impressions and percentage viewed for each upload at least 7 days old, and her median upload's impressions (Y2, Y3).`
3. **PASS** (a knock-on). Corrected verdict 3: "click-through under 2% with impressions at or below her median upload's … An upload under 2% with impressions above her median is recorded and not counted". Read 4 must collect both inputs. No new claim.
4. **Syllabus:** no conflict, but it touches what a later brief relies on.
   - PB10's brief: "the items earlier units hand the review besides PB1's seven reads". The count stays at seven.
   - It agrees with PB6 D2 YT3: "Impressions and impressions click-through rate per upload, with the largest traffic source beside them".
   - It agrees with the register's "each with the seven reads of D3".
5. **Dated note**, with the finder corrected:
   - **Current** (count 1), the F45 note, which is the last line of the file: `Correction 12 Nov 2026, found by PB6's writer: §4 gains a row for the rule from 1 February 2027 that earning from the Shorts Creator Pool needs 10 million qualified Shorts views in the last 90 days (YouTube Help, answer 12843009) (flag F45).`
   - **Replacement:** that line, a blank line, then:
   `Correction 12 Nov 2026, found by the P100 correction check: D3 read 4 now records each upload's impressions and her median upload's impressions, which verdict 3 as corrected uses (flag F42).`

## 12. PB6 D2, "What the rows do not tell her"
1. **Current** (count 1), in units/PB6-how-youtube-growth-works.md: `(PB10 decides whether such an upload counts towards verdict 3).`
2. **Replacement** (as proposed): `(PB1 D3 verdict 3, as corrected on 12 Nov 2026, records an upload under 2% with impressions above her median upload's and does not count it).`
   - It reads correctly after "so that PB10 can see it before verdict 3 counts the upload".
3. **PASS.**
   - Corrected PB1: "An upload under 2% with impressions above her median is recorded and not counted".
   - Answer 7628154: "it's natural for the CTR to be lower".
4. **Syllabus:** no conflict. PB10 still runs the verdict ("the verdicts a review can reach … and what counts as evidence for each"), and F42 says "PB10 applies whichever wording stands".
5. **Dated note**, with the finder corrected:
   - PB6 has no notes block. Putting the note before `## Sources` follows PB4, where this same check's F36 and F37 notes sit before `## Sources`.
   - **Current** (count 1):
```
Your device for reading Studio: [phone app or computer]. Rows you cannot open on that device: [list them and when you will read them elsewhere, or drop them].

## Sources
```
   - **Replacement:**
```
Your device for reading Studio: [phone app or computer]. Rows you cannot open on that device: [list them and when you will read them elsewhere, or drop them].

Correction 12 Nov 2026, found by the P100 correction check: D2's note on the rows ("What the rows do not tell her") now says that PB1 D3 verdict 3, as corrected, records an upload under 2% with impressions above her median and does not count it, where it said PB10 decides (flag F42).

## Sources
```

## 13. PB5 §1
1. **Current** (count 1), in units/PB5-production-craft-with-a-phone.md: `PB4 has the phone recording before the first tool comes out of the box.`
2. **Replacement** (as proposed): `PB4 first had the phone recording before the first tool comes out of the box.`
   - The next sentence, "This unit refines that into one clip per step", still reads correctly.
3. **PASS.** PB4 now reads "recording before each step's tool comes out, one clip per step (PB5 §1)". Its note says "in place of before the first tool comes out of the box (flag F36)".
4. **Syllabus:** no conflict.
   - PB5 shot 1 ("The box opened on the table, before the first tool comes out") is a shot, not when recording starts, so it stays.
   - The D A checklist line 308 stays for the same reason.
   - The register has "one clip per step, started before each step's tool is picked up".
5. **Dated note**, with the finder corrected:
   - **Current** (count 1; the Boxes line alone occurs twice, so the anchor includes `## Sources`):
```
**Boxes** ([minutes] in all): pick stills [ ]; crop [ ]; text bands [ ]; contrast and spelling [ ]; first-slide test [ ]; export [ ].

## Sources
```
   - **Replacement:**
```
**Boxes** ([minutes] in all): pick stills [ ]; crop [ ]; text bands [ ]; contrast and spelling [ ]; first-slide test [ ]; export [ ].

Correction 12 Nov 2026, found by the P99 correction check: §1 now says PB4 first had the phone recording before the first tool comes out of the box, since PB4 now carries this unit's one clip per step (flag F36).

## Sources
```

## 14. case-facts.md
The register is not a unit, so the finder goes inside the entry itself, as its own "(S-PB1, 12 Nov 2026)" style does.

**(a) PB4 entry**
1. **Current** (count 1): `piece 1 session 1; 3.75 h), R2 14–20 Dec (1.25 h)`
2. **Replacement** (corrected):
`piece 1 session 1, PB5's production tests; 4.25 h), R2 14–20 Dec (PB5's audio re-test; 1.5 h; R1 and R2 corrected 12 Nov 2026, found by the P99 correction check, flag F37)`
   - The proposal's "(audio re-test; 1.5 h)" says nothing to show that R2 was also corrected. "PB5's" keeps it parallel with R1.
   - Moving the dated phrase to the end covers both weeks.
   - The register lists one highlight per week, not every item (R3 has "piece 1 edited Sun 27 Dec"), so naming only the re-test fits its style.
3. **PASS.**
   - PB4 D2 R1 row, total **4.25**: "Production tests: editor, storage, light, audio check (PB5, D A) 0.5".
   - PB4 D2 R2 row: "Audio re-test (PB5, D A) 0.25 · Log 0.25 | **1.5**".
   - PB5 D A: "0.5 to R1, which then totals 4.25 hours, and 0.25 to R2 for the audio re-test, 1.5 hours".
4. **Syllabus:** no conflict. It agrees with the register's PB5 entry: "R1 4.25 h, R2 1.5 h (D A; flag F37 for PB4's D2)".

**(b) PB1 entry**
1. **Current** (count 1): `change the format (from Q2, click-through under 2% or percentage viewed under its band on 3 or more uploads)`
2. **Replacement** (finder added):
`change the format (from Q2, on 3 or more uploads, click-through under 2% with impressions at or below her median upload's, or percentage viewed under its band; an upload under 2% with impressions above her median is recorded and not counted; corrected 12 Nov 2026, found by the P100 correction check, flag F42)`
3. **PASS.** PB1 D3 verdict 3: "on 3 or more of the quarter's uploads, click-through under 2% with impressions at or below her median upload's, or percentage viewed under its band".
4. **Syllabus:** no conflict. It agrees with the register's PB6 packaging check ("impressions below her median upload's").

---

## Found in this check

1. **flags.md still marks F36, F37, F42 and F45 as "open"**, though Changes 1 to 9 are applied. Row P99 says "flags set to resolved". The filing chat should set all four to resolved. This is not unit text, so I give no Current/Replacement.
2. **PB1 template T3 needs no change.** Its line "per-piece click-through and retention or their Instagram equivalents (PB6, PB7)" is generic reader guidance. "Change the format if: [the per-piece reads, with the sourced band for each…]" leaves the rule to the reader. Neither contradicts the corrected verdict 3.
3. **PB6 R6 needs no change.** It uses "impressions below her median upload's" (strictly below), while PB1 verdict 3 counts "at or below". These are different rules: R6 picks one upload to repackage, verdict 3 counts uploads. They do not conflict.
4. **Nothing else in PB1, PB4, PB5 or PB6 is still stale.** I searched for "first tool", "3.75", "PB10 decides", "verdict 3" and "under 2". PB6 YT3 ("Verdict 3 is not applied in Q1") and PB1 row Y2 ("Read per upload from Q2") agree with the corrected text.

Nothing in this report came from memory.
