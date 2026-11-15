---
audit: final audit (Audit 4), a full read of the course against its goal
units: PB1, PB2, PB3, PB4, PB5, PB6, PB7, PB8, PB9, PB10, DD-PB1, DD-PB2
course: personal-brand · PB · Building a Personal Brand on Instagram and YouTube
model: Fable 5.2 (claude-fable-5-2; accepted by Pedro for row F-PB, 14 Nov 2026); no source re-checked
date: 2026-11-14
chat: one fresh Fable agent with the twelve units, the briefs, the goal and outcomes and the register, in session https://claude.ai/code/session_01KMmgQyKuvCKpHpSB9xzQYA (row F-PB part 1)
verdicts: see the report's verdict on the course
---

Model: claude-fable-5-2

# Audit 4, the final audit: course PB · Building a Personal Brand on Instagram and YouTube

Date: 14 November 2026. One auditor, isolated, no web. Read: all twelve units in full, in reading order (PB1 to PB10, DD-PB1, DD-PB2; 127,096 words), the twelve briefs, the goal and outcomes, the register of Mara's facts, the sourcing standard. No source was opened: every finding below rests on one unit set against another unit, a brief or the register, or on arithmetic redone here. `out/` was empty at the start; this is not a resumed run. Source lists at the end of each unit were read for form only.

Counts: 19 findings (0 error, 7 should-fix, 12 minor). 24 objects in `errata.json`: 15 errata with exact replacements (each `Current` counted once in its unit, on one line), 9 flags (6 findings that a text change does not settle). 10 contradictions between units. No unit is REWRITE.

## Findings

### Should-fix

**A4-1 · PB10 D4 against PB5 §7 and PB5 D A · the Q2 format change is the layout she already uses.**
- PB5 §7, rule 1: "The thumbnail image is a frame from the footage, usually the as-found and finished views from the taped mark side by side."
- PB5 D A, piece 1: "thumbnail the as-found and finished views from the taped mark side by side, text "Water rings, one box""
- PB10 D4, Verdict: "the thumbnail shows the fault and the finished piece side by side, at most four words, in her colours (PB5 §7), in place of the finished piece alone."
- Problem: PB10's one worked "change the format" verdict replaces a layout ("the finished piece alone") that no earlier unit gave her, with one PB5 already set. The reader is shown a change that is no change. The register's line ("the thumbnail shows the fault and the finished piece side by side") stays true under the fix; the close frame is a small new fact to append.
- Current: `the thumbnail shows the fault and the finished piece side by side, at most four words, in her colours (PB5 §7), in place of the finished piece alone`
- Fix: `the thumbnail shows the fault in a close frame beside the finished piece, at most four words, in her colours (PB5 §7), in place of the two whole-piece views from the taped mark, as found and finished, that PB5 §7 rule 1 set`

**A4-2 · PB1 D3 and PB6 D1 R6 against PB10 D2 and D4 · "her median upload's" impressions has no stated scope, and the scope decides the worked verdict.**
- PB1 D3, verdict 3: "click-through under 2% with impressions at or below her median upload's"; read 4: "and her median upload's impressions (Y2, Y3)."
- PB6 D1 R6: "whose impressions are below her median upload's".
- PB10 D2 step 3: "Then the quarter: median impressions, the uploads that count for verdict 3"; D4: "median impressions of uploads 8–13, 1,275 ... upload 11 (1.7%, 1,210 ...)".
- Problem: PB1 and PB6 read as the median of all her uploads; PB10 uses the quarter's. On the readings PB10 prints for all thirteen uploads (Q1 readings for uploads 1–7, which would have risen by July), the median is 1,150, under upload 11's 1,210: on that reading upload 11 is "recorded and not counted", two uploads count, and Q2's verdict is continue. A reader applying PB1's words can reach the opposite verdict from PB10's on the same sheet.
- PB1, Current: `and her median upload's impressions (Y2, Y3).` Fix: `and her median upload's impressions, the median across the quarter's uploads at least 7 days old, which is the median verdict 3 uses (PB10 D2 step 3) (Y2, Y3).`
- PB6, Current: `whose impressions are below her median upload's` Fix: `whose impressions are below her median upload's (the median of that quarter's uploads at least 7 days old, as in PB1 D3 read 4)`

**A4-3 · PB8 §6.1 and PB9 §11 against PB8 D3 A1, PB8 D1 clause 7 and PB9 D1 · her own product is promoted in Season 2 with no ad label, while the register says no label is needed until the first deal. FLAG, no replacement.**
- PB8 §6.1, decision figure: "is it your own product or your employer's ...?" leads to "Label it: 'ad' up front in the post, and in the video itself for a video, plus YouTube's paid promotion setting or Instagram's paid partnership label".
- PB9 §11: "An own product introduced as yours is also an ad under the UK guide's rule for brands you own (PB8 §6.1), so it is counted too."
- PB8 D3 A1: "Settled: none needed in Seasons 1–2, no deals or gifts (clause 7); recheck at first deal". PB8 D1 clause 7: "Anything she sells herself is introduced as hers every time."
- PB9 D1: "Launch Tuesday 8 June 2027 with upload 12, named in that video as hers and in that day's email." PB9 D4: "One "mine" mention per launch video".
- Problem: upload 12 is in Season 2. By PB8's own figure it needs the word "ad"; by A1 nothing needs a label before the first deal; by clause 7 "introduced as hers" is enough. PB10's two reviews re-read the register and do not reopen A1 when the guide is decided. Which reading is right is a question of what the CMA and FTC guidance require for an own product, which I cannot settle without the sources. For a syllabus review: decide whether "introduced as hers" satisfies the guidance PB8 quotes, then align the figure, clause 7, A1 and PB9 D1.

**A4-4 · PB10 §4 against PB1 D3 and PB7 D2 IG8 as filed · PB10 quotes a wording the two units no longer carry.**
- PB10 §4: "**One row is misread downstream.** PB1's Q3 instruction compares Instagram net followers "with the 0.36-a-week illustration (I4)", and PB7's IG8 sets the same figure as a reference."
- PB1 D3, Q3 review, as filed: "Instagram net followers are recorded with no benchmark: no dataset found follows accounts from under 1,000 followers (§3; I7), and I4 is an increment over weeks without posts, not a total."
- PB7 D2 IG8, as filed: "Buffer's +0.26% (PB1 I4) is an increment over weeks without posts, not a total".
- Problem: both units were corrected on 13 Nov 2026 to say what PB10 argues. A reader who checks the pointer finds neither quotation. PB10 §5 already handles the same case for PB4 with a dated note; §4 and §5's first paragraph (A4-5) do not.
- Current: `Read PB1 D3's Q3 line and PB7's IG8 reference column this way.`
- Fix: `PB1 D3's Q3 line and PB7's IG8 reference column were corrected on 13 Nov 2026 and now read this way; the words quoted above are PB1's earlier wording.`

**A4-5 · PB10 §5 against PB1 D2 and PB4 D1 G as filed · the same, for where the review's hour comes from.**
- PB10 §5: "PB1 took the review's hour from "that fortnight's publishing-and-replies line" (PB1 D2), and PB4 repeated it (PB4 D1 G)."
- PB1 D2, as filed: "The quarterly review (60 minutes, PB10) is taken from the Instagram derivatives of the fortnight that holds it: that fortnight's cut window makes four posts in place of six, two Reels fewer (PB10 §5)."
- PB4 D1 G, as filed: "its hour taken from that fortnight's cut window, two Reels fewer (PB1 D2; PB10 §5)".
- Current: `PB1 took the review's hour from "that fortnight's publishing-and-replies line" (PB1 D2), and PB4 repeated it (PB4 D1 G).`
- Fix: `PB1 first took the review's hour from "that fortnight's publishing-and-replies line" (PB1 D2), and PB4 repeated it (PB4 D1 G); both were corrected on 13 Nov 2026 and now state the rule this paragraph reaches.`

**A4-6 · PB4 and PB10 against outcome 2 · the hours log is never built. FLAG (a brief changes), no replacement.**
- PB1 D2: "Log | 0.5 | Hours logged each week against this table". PB4 D2 R1: "Folders, log sheet, Season 1 playlist 0.5". PB4 D1 C: "log the week's hours and the backlog, 0.25". PB10 D1: H1 to H5 read "Hours log (PB1 D2)", "Hours log (PB4 §7)", "Hours log, admin line".
- Problem: the goal's second clause is a system run "for twelve weeks inside an hours budget you set yourself". The only proof a reader has of that is the log, and three verdicts read it (stop through uploads, cut the load, PB4's cadence move). No unit builds the log for Mara or gives a template: not its columns (hours by PB1 line per week, the week's total, over 7 or not, recovery week, edit overrun, weekends per piece, admin with its week, hours on income lines), not one filled week. PB10 D3 shows what the review extracts from it, which lets a careful reader reconstruct it. Needs a deliverable line in PB4's or PB10's brief; a text change does not settle it.

**A4-7 · PB7 D1 IR7 and PB8 D3 E3, E5 · the email sign-up has a date and no place, and its notice is never written. FLAG, no replacement.**
- PB8 D3 E5: "the form goes live with upload 3, Tue 2 Feb 2027, if E3 and E4 are done". E3: "To do: notice with the art. 13 items, written by Sun 31 Jan 2027".
- PB7 D1 IR7: "Profile link 1 is the YouTube channel; the newest video is link 2 from each upload Tuesday. Every post ends with "Full video: link in profile"."
- PB2 D4's channel description and PB5's description rule (season line, chapter list) carry no link to a form.
- Problem: no unit says where a viewer meets the form (a third profile link, the video description, a spoken line, a pinned comment). PB3 §5 names this as the missing number ("how many of a small account's viewers ever reach one"), and then the course never routes anyone to it. PB10's list grows to 9 and 31 by a path the reader cannot copy. The notice E3 requires is listed by GDPR item in PB8 §6.6 and not written out, for Mara or as a template. The list is not in the goal, but PB9's first income line is launched through it. For a syllabus review: one rule in PB7 or PB8 on placement, and the notice built once.

### Minor

**A4-8 · PB10 D4 HO3 against PB4 D2 · Season 3's first two pieces are dated a week late.**
- PB10 D4: "On the table: 14, a teak sewing cabinet (from 19 Jun), and 15, a beech stool (from 3 Jul)."
- PB4 D2: every piece's first session is the Saturday 24 days before its upload ("its first two, on the table from 20 March and 3 April", for uploads 8 and 9 on 13 and 27 April). Uploads 14 and 15 are Tue 6 Jul and Tue 20 Jul 2027 (PB9 D1; PB10 D4), which gives Sat 12 Jun and Sat 26 Jun; 19 Jun is piece 14's second session and 3 Jul piece 15's (derived here from PB4's pattern; PB4 does not print weeks 13 to 26).
- Current: `14, a teak sewing cabinet (from 19 Jun), and 15, a beech stool (from 3 Jul)`
- Fix: `14, a teak sewing cabinet (from 12 Jun), and 15, a beech stool (from 26 Jun)`

**A4-9 · PB10 D3 H4 against PB4 D2 · piece 5's third Saturday is piece 6's first session, and the unit does not say how pieces 6 and 7 kept their dates.**
- PB4 D2, week 7: "Sat 20: piece 5 reveal, piece 6 session 1, capture 1.0".
- PB10 D3: "Piece 5 took a third Saturday (20 Feb) ...", pieces 6 and 7 "2" weekends each, "7 of 7 published on their dates".
- Problem: if 20 Feb went to piece 5 alone, piece 6's reveal falls after its edit window of 7 March and the loss repeats. The story holds only if piece 6 also started on 20 Feb, which the unit should say. The fix sets one small fact (piece 5's reveal on 27 Feb) for the register.
- Current: `Piece 5 took a third Saturday (20 Feb), so its reveal was not filmed before the Sunday edit window: the cause of week 7's lost window`
- Fix: `Piece 5 took a third Saturday (20 Feb), so its reveal was not filmed before the Sunday edit window: the cause of week 7's lost window. Piece 6's first session was filmed the same Saturday, as PB4 D2 plans, and piece 5's reveal on Sat 27 Feb, so pieces 6 and 7 kept their dates`

**A4-10 · PB3 D2 against PB1 D2 as filed.** PB3: "at 6 h this is PB1's 1.5 a fortnight less the email's 0.25". PB1 D2: "Publishing and replies | 1.25" with an Email line of 0.25 citing PB3. A reader in order has just seen 1.25.
- Current: `at 6 h this is PB1's 1.5 a fortnight less the email's 0.25`
- Fix: `at 6 h this is PB1's 1.25 a fortnight: the 1.5 PB1 first gave the line, less the email's 0.25`

**A4-11 · PB5 §1 against PB4 §1 as filed.** PB5: "PB4 first had the phone recording before the first tool comes out of the box. This unit refines that into one clip per step (her rule)". PB4 §1, capture table: "recording before each step's tool comes out, one clip per step (PB5 §1)". The reader never saw the wording PB5 says it refines.
- Current: `PB4 first had the phone recording before the first tool comes out of the box. This unit refines that into one clip per step (her rule)`
- Fix: `PB4's capture table has the phone recording before each step's tool comes out, one clip per step, and takes that rule from this unit (PB4 §1). The rule is hers (her rule)`

**A4-12 · DD-PB1 Deliverable A against PB10 D5 and DD-PB2 D1.** DD-PB1: "the 24-month review on 1 January 2029". PB10 D5 item 7: "Monday 1 January 2029 (47–52), a public holiday, so PB4's holiday rule moves it within its own week". DD-PB2 i14: "week of Mon 1 Jan 2029". The register's DD-PB1 line carries the same "1 January 2029".
- Current: `the 24-month review on 1 January 2029 (Mara, fictional`
- Fix: `the 24-month review in the week of 1 January 2029 (Mara, fictional`

**A4-13 · PB1 D2 · a Portuguese post-office tariff appears four units before her country is set.** PB1 D2: "58.00 € + VAT a year (CTT tariff, Nov 2020; current price to check)". Portugal is set in PB8 ("she lives in Portugal (Mara, fictional; set 13 Nov 2026)"); PB1 never says what CTT is, and its other amounts are in USD.
- Current: `58.00 € + VAT a year (CTT tariff, Nov 2020; current price to check)`
- Fix: `58.00 € + VAT a year (a PO box at CTT, the post office of Portugal, where PB8 sets her home; tariff of Nov 2020; current price to check)`

**A4-14 · PB10 §5 and D2 against PB10 D3 (inside one unit; PB4 D2 for the weeks).** §5: "taken from the three reply slots of the review fortnight"; D2: "from the review fortnight's three reply slots". D3: "0.75 hours from the reply slots of 7, 14 and 16 April". The fortnight that holds Monday 5 April is weeks 13 to 14 (PB4 D2), whose slots are 31 March, 2 April and 7 April; two have passed. The register has it right ("the three reply slots of weeks 14–15").
- Current: `taken from the three reply slots of the review fortnight; replies wait for the next slots` Fix: `taken from the next three reply slots after the review (at Q1: Wed 7, Wed 14 and Fri 16 April 2027, weeks 14–15); replies wait for the slots after those`
- Current: `Q1: the repeat-back test, run 2, 0.75 hours, from the review fortnight's three reply slots.` Fix: `Q1: the repeat-back test, run 2, 0.75 hours, from the next three reply slots after the review.`
- The matrix cell "three reply slots" and its caption ("from that fortnight's reply slots") are a figure; left as they are, noted for the figure check.

**A4-15 · PB4 D2 R1 against PB2 D2, PB5 §7, PB7 IR10 · the profiles go live with no line in the run-in. FLAG.** Outcome 1 ends "live on both profiles". PB2 D2: "she claims @oneboxrestoration on YouTube and on Instagram on the same day". PB5 §7: a creator can "upload your own if your account is verified". PB7 IR10: "Her account is public and professional (creator)". PB4 D2 R1 has "Folders, log sheet, Season 1 playlist 0.5" and the repeat-back test on the profile, and no line or hours for claiming the handle, pasting PB2's copy, verifying the channel for custom thumbnails or switching the Instagram account type. Each is said somewhere; none is a step with a date. Whether her claim succeeded is left free in the register, by design.

**A4-16 · course-wide · internal process codes in text a public reader sees. FLAG.** PB4, PB5 and PB6 carry correction notes after their Templates and before Sources: "found by the P99 correction check ... (flag F36)". PB10 §5: "(Correction 2026-11-13, P108: ...)". Every Unsure list: "report `audits/personal-brand/fresh-check-PB1.md`", "a Fable 5.1 fresh check is owed, P49", "(row W-PB3)". The preamble says the course "is written to be shared with anyone" and points "only to units of this course". None of these names the private course, and none can be opened by a reader. For the build or a syllabus decision: whether the Unsure lists and correction notes are shown, and in what form.

**A4-17 · PB4 §7 · the recovery week after a lost week A leaves out week B's own reply slot. FLAG.** PB4 §7: "the edit at about 8 minutes (3.0), then a shortened cut: packaging 1.0, two Instagram posts in place of six (1.0 ...), scheduling 0.25. With capture 1.0 and the log 0.25 that week is 6.5 hours." PB4 D1 E gives week B "Publishing and replies 0.75" (scheduling 0.5, a Wednesday reply slot 0.25). With the slot the week is 6.75, still under 7; "Replies wait for the next slots" may mean it is dropped. One clause would say which.

**A4-18 · DD-PB1 §10 · one citation date for three trackers.** "on 13 November 2026 Boyd and Anderson had no net subscriber change ... and Abdaal ... added none in October 2026 (vidIQ, data 11 Nov 2026)". §5 and §6 date Boyd's and Anderson's data 13 Nov 2026.
- Current: `added none in October 2026 (vidIQ, data 11 Nov 2026)`
- Fix: `added none in October 2026 (vidIQ, data 11 Nov 2026 for Abdaal and 13 Nov 2026 for Boyd and Anderson)`

**A4-19 · PB4 §2 against PB1 §6 and PB3 §6 as filed.** PB4: "PB1 and PB3 cited only the first." PB1 §6: "YouTube's performance FAQ says it found "no correlation between break length and changes in views"". PB3 §6: "YouTube's own performance FAQ reports no such link for breaks". Both were corrected to carry it.
- Current: `PB1 and PB3 cited only the first. Read together, neither shows`
- Fix: `PB1 §6 and PB3 §6 give both. Read together, neither shows`

Not raised as findings: the correction logs in PB1 and PB7 each hold a line superseded by a later line ("31 posts" for Q2 with the guide, then 29; "39 stands otherwise", then 37). The body text is right (29 and 37, re-derived here from PB4 D2); the logs are history.

## 1 · The course against its goal

| | Units and deliverable | Delivered | Missing or thin |
|---|---|---|---|
| **Goal, clause 1**: state in one sentence who the account is for and what it gives them | PB2 D1 and T1 (the sentence, 29 words, and a 60-word expansion); PB2 D5 and T5 (the repeat-back test as a script); PB3 D1 (the audience tested against outside evidence, ten traits with basis and label) | Yes | The test's five people, delay and pass mark are conventions, said so. Run 1's result for Mara is never given; run 2's is one line in PB10 D3 (4 of 5), with no filled sheet |
| **Goal, clause 2**: a publishing system run for twelve weeks inside an hours budget you set yourself | PB1 D2 and T2 (budget); PB3 D2 and T2 (allocation at 3, 6 and 10 hours, cut order); PB4 D1, D2, T1, T2 (checklist; run-in and twelve weeks, every week summed at 6.0; rules for 3 and 10 hours); PB5 A to D and T-A to T-D (production checklist, 240-minute edit, Reel, carousel); PB8 D1 to D3 (policy, pre-mortem, register) | Yes, as a plan and its rules | The hours log, the instrument that shows the budget was held, has no template and no filled week (A4-6). A reader at 4 or 8 hours builds a column the templates do not have. No time for PB8's register tasks in the run-in (PB10 logs them after the fact as admin) |
| **Goal, clause 3**: read your Instagram and YouTube numbers against sourced benchmarks each quarter to decide, with evidence, whether to continue, change format or stop | PB1 D1, D3, T1, T3 (expectation sheet of 21 rows, stop rule, four verdicts, four dated reviews); PB6 D1, D2 (eleven rules, rows YT1 to YT12); PB7 D1, D2 (twelve rules, rows IG1 to IG13); PB9 D5 (rows R1 to R8); PB10 D1 to D5, T1 to T4 (one sheet, sixty-minute procedure, two quarters run, annual page) | Yes for YouTube; for Instagram as record, not as decision | See below |
| **Outcome 1**: a positioning a stranger can repeat, live on both profiles (PB2, PB3; DD-PB1) | PB2 D2 to D4 (name, handle with fallbacks and override, bio at 111 characters, description at 841); DD-PB1 A (six histories, five constants, what survivors cannot show) | Yes for the copy | "Live" is a condition, not a step: the same-day handle claim, the profile copy going up, channel verification and the Instagram account type have no line in the run-in (A4-15). No handle was or can be checked by a unit; the reader claims it in the apps |
| **Outcome 2**: a publishing system held for twelve weeks inside your own hours budget (PB4, PB5, PB8) | As clause 2 | Yes | As clause 2. PB5's 220-minute edit is set against a vendor rule of thumb of 300 to 600 minutes and the unit says the plan's first break will be there; PB4 and PB5 give the fallback |
| **Outcome 3**: a quarterly decision to continue, change format or stop, on your numbers against sourced benchmarks (PB1, PB6, PB7, PB9, PB10; DD-PB2) | As clause 3; DD-PB2 D1 to D7 (threshold model, three paths, dates) | Yes, with the limit below | |

**Where outcome 3 is thinner than its words.** The course is exact about this and the goal sentence is not. (a) The stop verdict reads uploads per quarter, an input, and in year one no audience number can stop her (PB1 D3; PB10 §6); "your numbers against sourced benchmarks" decides a stop only from month 24, under her rule in PB10 D5. (b) The format verdict reads two YouTube numbers against a platform range with no target (2% to 10%, "half of all channels and videos") and a vendor band with no sample (40% to 55%); PB10 §3 shows what the three-of-a-quarter count can and cannot tell, which is the strongest section of the course. (c) On Instagram no sourced benchmark decides anything at under 1,000 followers: I7 is unsourced, I3 is context, IR11 is her own two medians, IR12's line is an average for brand accounts she is not among. PB10 §6 keeps IR12 out of verdict 3 for that reason. The reader does read Instagram numbers each quarter; they decide "change one thing" at most. (d) The worked run shows two verdicts, continue and change the format; cut the load and stop are stated and not run. (e) The scope of "her median upload" is not fixed where the rule is set (A4-2).

**Briefs against units, where a gap bears on the goal.** PB4's brief asks for "Mara's 12-week calendar with hours per item, every week summed and inside 6 hours": delivered; it does not ask for the log, which is why none exists (A4-6). PB10's brief asks that items beside the hour have their hours "found inside the reader's budget": delivered (two Reels fewer; reply slots), with the slot wording loose (A4-14). PB8's brief asks for the register "filled where her facts allow": delivered; the sign-up notice is a to-do, not a text (A4-7). DD-PB1's brief asks for numbers at 12, 24 and 36 months: 17 of 18 points are unpublished, and the unit says so instead of interpolating. DD-PB2's brief asks for "the earliest honest date on each" path: delivered, with Path B's answer "none from the evidence".

## 2 · Read-through as the reader of the preamble

Reading in order, on a phone, checking pointers.

**Where a unit assumes what an earlier one did not give.**

| Where | What is assumed | Quoted |
|---|---|---|
| PB1 D2 | Her country, and what CTT is; set in PB8 | "58.00 € + VAT a year (CTT tariff, Nov 2020; current price to check)" (A4-13) |
| PB1 D2, D3 | PB5's audio check, PB8's line E4, PB9's guide and PB10's hour, all four to nine units ahead | "29 in Q2 if PB9's guide build is decided at the Q1 review"; "Paid from the unspent microphone line (PB5 §2)". These are forward pointers left by later corrections; each resolves when its unit is reached. A first-time reader of PB1's D2 money table cannot follow the postal-address row |
| PB1 D3 | The scope of a median | "impressions at or below her median upload's" (A4-2) |
| PB4 D2 R1 | That the profiles exist and are live in the week of 7 December | "Repeat-back test run 1 on the profile" (A4-15) |
| PB5 §2 | A YouTube channel able to take unlisted uploads on 12 December, and automatic captions on them; the Unsure list says the second is assumed | "Upload both to YouTube as unlisted" |
| PB5 §7 | A verified channel, for custom thumbnails | "upload your own if your account is verified"; no checklist line |
| PB6 D2, PB7 D2 | Menu paths on the reader's device | "the iPhone help was not read"; "No Instagram Help Centre page could be read to confirm the menu names". Both units say the app is the authority |
| PB8 E5, PB9 D1 | A place where the sign-up form is shown | "the form goes live with upload 3" (A4-7) |
| PB8 §2 | A statistical method | "analysed the answers with PLS-SEM", not glossed; nothing rests on it |
| PB10 D1 | The hours log | "Hours log (PB1 D2)" (A4-6) |

Terms are otherwise given before use: the evidence labels in PB1 §1 and reused by name; fixed-effects (PB1 §3), lower third (PB5 §4), RPM (PB9 §2), Poisson and Wilson (PB9 §8, PB10 §3) each glossed where met.

**Where two units disagree.** Section 3.

**Where Mara's facts differ from the register or between units.**
- Thumbnail layout before the Q2 change: PB5 §7 and D A (side by side from piece 1) against PB10 D4 ("the finished piece alone") (A4-1). The register sides with neither on the earlier layout.
- First sessions of pieces 14 and 15: PB10 D4 ("from 19 Jun", "from 3 Jul") against PB4 D2's calendar (12 and 26 June) (A4-8).
- The 24-month review's day: DD-PB1 and the register's DD-PB1 line ("1 January 2029") against PB10 D5 (moved within its week) (A4-12).
- Piece 5's third Saturday: PB10 D3 against PB4 D2, week 7; reconcilable, not said (A4-9).
- The repeat-back test's reply slots: PB10 §5 and D2 against PB10 D3 and the register (A4-14).
- Everything else checked agrees with the register: day one and the four review dates; upload dates 1 to 15; post counts 39, 37, 37, 37 and 29 (re-derived from PB4 D2); the run-in totals 4.25, 1.5, 5.25, 5.75; the fortnight's 12.0 hours by line; the cap and its lines; audio check dates and counts; colours; the register's dates (29 Nov, 6 Dec, 31 Jan, 2 Feb, 5 Jul); the guide's four build blocks and launch; Q1 and Q2 values (every sum, median and interval in PB10 D3 and D4 recomputed); admin hours; year two's dates (all Mondays, checked); DD-PB2's floor, runway, threshold and the three dates (Path A re-run: Monday 7 July 2042).
- Labelling: "(Mara, fictional)" is present on first use in every unit. No Mara number is used as evidence about the world in any unit read.

## 3 · Contradictions between units

| # | Kind | Side A | Side B | Finding |
|---|---|---|---|---|
| 1 | Mara's facts | PB5 §7 rule 1: "usually the as-found and finished views from the taped mark side by side" | PB10 D4: "in place of the finished piece alone" | A4-1 |
| 2 | Rule, definition | PB1 D3: "impressions at or below her median upload's"; PB6 R6: "below her median upload's" | PB10 D2 step 3: "Then the quarter: median impressions"; D4: "uploads 8–13, 1,275" | A4-2 |
| 3 | Rule | PB8 §6.1 figure: own product, "Label it: 'ad' up front"; PB9 §11: "also an ad" | PB8 D3 A1: "none needed in Seasons 1–2 ... recheck at first deal"; PB9 D1: upload 12 "named in that video as hers" | A4-3 |
| 4 | Pointer | PB10 §4: PB1's Q3 instruction compares net followers "with the 0.36-a-week illustration (I4)" | PB1 D3 Q3: "recorded with no benchmark ... I4 is an increment over weeks without posts, not a total" | A4-4 |
| 5 | Pointer | PB10 §5: PB1 took the hour from "that fortnight's publishing-and-replies line" (PB1 D2), "and PB4 repeated it (PB4 D1 G)" | PB1 D2: "taken from the Instagram derivatives of the fortnight that holds it"; PB4 D1 G: "from that fortnight's cut window, two Reels fewer" | A4-5 |
| 6 | Dates | PB10 D4 HO3: "(from 19 Jun)", "(from 3 Jul)" | PB4 D2: first session 24 days before upload; uploads 14 and 15 on 6 and 20 July | A4-8 |
| 7 | Number | PB3 D2: "PB1's 1.5 a fortnight less the email's 0.25" | PB1 D2: "Publishing and replies | 1.25" | A4-10 |
| 8 | Pointer | PB5 §1: "PB4 first had the phone recording before the first tool comes out of the box" | PB4 §1: "recording before each step's tool comes out, one clip per step (PB5 §1)" | A4-11 |
| 9 | Date | DD-PB1 A: "the 24-month review on 1 January 2029" | PB10 D5: "a public holiday, so PB4's holiday rule moves it within its own week" | A4-12 |
| 10 | Pointer | PB4 §2: "PB1 and PB3 cited only the first" | PB1 §6 and PB3 §6 both give YouTube's statement on breaks | A4-19 |

Five of the ten (4, 5, 7, 8 and 10) have one cause: a later unit's writer found a fault, the earlier unit was corrected, and the later unit's sentence describing the fault stayed. A sixth (3) is the same seam the other way round: PB9 set a fact after PB8's register line was written, and the line was not reopened. The correction notes record each case; the bodies were not reconciled.

Checked and found consistent, where a contradiction was most likely: thresholds (500 and 3,000; 1,000 and 8,000 from 1 February 2027; 10M Shorts views) in PB1 §4, PB6 §4 and §8, PB9 §2 and DD-PB2 §3; the views those hours mean (PB1 rounds, PB9 gives 87,273 to 120,000, and says so); vidIQ's bands and medians wherever repeated; Buffer's four increments; the 65.5% skip rate (PB5, PB7, PB10); PB3's cut order against PB4 §7 (PB4 names its one departure, the skip on a second lost cut window); verdict 3 "from Q2" (PB1, PB4, PB6, PB10); "no Shorts in year one" (PB3, PB4, PB5, PB6, PB10); brand deals "from Season 3, upload 14, Tue 6 Jul 2027" (PB8, PB9, PB10, DD-PB2); the 7-hour line ("a week at 7.0 is at the line, not over it").

## 4 · What a reader still cannot do at the end

Set against the goal and outcomes.

1. **Decide anything on Instagram against a sourced benchmark at under 1,000 followers.** No dataset follows such accounts (PB1 §3, I7; PB7 confirms). The reader records, compares with their own earlier quarters, and runs two tests whose thresholds are conventions. The course says this in every unit it touches; the goal sentence promises more than exists.
2. **Show from a template that the hours budget was held** (A4-6).
3. **Route a viewer to the email list, or write the form's notice** (A4-7).
4. **Know whether their own product needs the word "ad"** (A4-3).
5. **Check a handle, a menu path, or what the app shows**, from the course: handles cannot be checked by a unit (by design, the reader claims them); Studio paths rest on the Android help; Instagram's Help Centre could not be read by any unit, so menu names, the in-app demographics threshold, trial-reel eligibility and the hashtag limit rest on press reports. Each is on an Unsure list.
6. **Put a month on any milestone**, on either platform: no dataset gives one (PB1 §5, §10). The course gives upload counts converted to months and says that is all they are.
7. **Answer a tax or legal line.** By design: each is a question with the EU, UK and US source, and a line that says who answers it. Professional fees are unpriced in every unit.
8. **Budget at an hours figure other than 3, 6 or 10** from a filled column.
9. **See a cut-the-load or a stop verdict run** on numbers; both are rules without a worked case.
10. **Date a full exit from a job.** DD-PB2 computes that no path has an income date the evidence supports; that is the unit's finding, not its gap.

## Verdict on the course

**Does it deliver its goal as written?** Yes for the first two clauses and for the YouTube half of the third. The Instagram half is delivered as a quarterly reading that informs and rarely decides, because no benchmark exists at this size; every unit says so, and I would change the goal's wording before the units. Sourcing discipline, as far as it can be judged without opening a source, is consistent across all twelve: claims are labelled where made, conventions are marked as conventions, unsourced claims are named and left out of rules, Mara is never evidence. The arithmetic I redid (calendar, post counts, hours, thresholds in views, Wilson and binomial tables, Poisson figures, PB10's two quarters, DD-PB2's three paths) holds without exception.

**What is wrong is seam work, not content.** Five of ten contradictions are sentences in a later unit that still describe an earlier unit as it was before its correction (A4-4, A4-5, A4-10, A4-11, A4-19). Two findings change what a reader would decide: the undefined median in the format verdict (A4-2), and the own-product label (A4-3). One makes the only worked format change empty (A4-1). Two are missing pieces of the system the goal names (A4-6, A4-7).

**REWRITE:** none. No unit, and no section of a unit, needs rewriting. PB10 carries the most errata (seven, in §4, §5, D2, D3 and D4), each one sentence or one clause.

**What a reader still cannot do:** decide on Instagram numbers against a sourced benchmark at under 1,000 followers; keep the hours log from a template; place the email sign-up and write its notice; know whether an own product needs an ad label; everything else in the goal they can do.

**Changelog line:** Audit 4, final, course PB, 14 Nov 2026, Fable 5.2: twelve units read in full, no web; 19 findings (0 error, 7 should-fix, 12 minor), 15 errata and 9 flags, 10 contradictions between units, no REWRITE; the course delivers its goal, with Instagram benchmarks thin by evidence, and three flags for a syllabus review (own-product ad label, hours log, email sign-up).

---

## Appendix · Working notes, written unit by unit during the read


#### PB1 (read in full)
- Sets: day one Mon 4 Jan 2027; 26 videos/yr; 3 IG posts/wk; 12 h/fortnight; cap 150 USD; stop rule <3 uploads in each of two consecutive quarters; verdict order stop / cut load (>7 h in 3+ weeks) / format (from Q2, 3+ uploads, CTR<2% with impressions <= median, or APV under band) / continue; reviews 5 Apr, 5 Jul, 4 Oct 2027, 3 Jan 2028; seven reads.
- Arithmetic re-done: 8,000 h -> 87,300-120,000 views; 3,360-4,620 per video; upload 10 in week 19; all hold.
- T2 template has no Email line though D2 has one (minor).

#### PB2 (read in full)
- Sets sentence (29 words), name One Box Restoration, @oneboxrestoration, fallbacks, bio, description, repeat-back test (5 strangers, pass 4 of 5 on who+what; run 1 week of 7 Dec 2026; run 2 at Q1 review on one video).
- Agrees with register. Bio/description are the live-profile deliverable for outcome 1. Handle availability unchecked by design (reader claims in-app).

#### PB3 (read in full)
- Keeps PB2's audience; roles (YouTube home, Instagram shop window, email owned list); no Shorts at 6 h; 3/6/10-hour allocations (11.75/24/39 per four weeks); cut order.
- Pointers to check: "PB9 compares them" (email tool prices); "PB7 completes them" (PB1 I7).

#### PB4 (read in full)
- Week A/B pattern, run-in R1-R4 (4.25, 1.5, 5.25, 5.75), 12-week calendar at 6.0 each (72.0), seasons = quarters, lost-week rules, 3 h and 10 h rules. Calendar dates and sums re-computed: hold. Post counts 39/37/37/37 and 29 with guide re-derived from the calendar: hold.
- Recovery week after lost week A sums to 6.5 only if week B's Wednesday reply slot (0.25) is dropped; text says replies "wait for the next slots" (minor ambiguity).

#### PB5 (read in full)
- Frame 3840x2160/30, audio check (fail 12 Dec, pass 19 Dec), runtime map 8 chapters = 10:00, edit boxes = 220 min, Reel 45 s, carousel 8 slides (post 5, Thu 14 Jan 2027), packaging rules (thumbnail "usually the as-found and finished views ... side by side"; at most four words), contrast table, what not to buy.
- To check against PB10: Q2 format change "thumbnail shows the fault and the finished piece side by side" vs PB5 §7 rule 1 / D A piece 1 thumbnail, which is already side by side.

#### PB6 (read in full)
- Playbook R1-R11, rows YT1-YT12; Q1 worked as "what qualifies and what she writes"; values left to PB10. Q1 qualification dates re-computed: hold. Title length 82 and position 13: hold.

#### PB7 (read in full)
- Playbook IR1-IR12, rows IG1-IG13; Q1: 39 posts (27 Reels, 12 carousels), 36 qualify on 5 Apr; Q2 37 (23/14), 29 (15/14) with guide. Re-derived from PB4 D2: hold.
- PB1's I7 stays unsourced (PB7 found no dataset); PB1 said PB7 "completes them if its research finds a dataset": consistent.
- Unsure-list line "31 posts (17 Reels)" superseded by the later correction (37/29); log only.

#### PB8 (read in full)
- Policy (10 clauses), pre-mortem (9 causes, January 2029), register (A1-A3, P1-P3, C1-C3, J1-J3, T1-T3, E1-E5, M1-M2, H1, R1). Dates: J1/J2 by 29 Nov 2026, M1 by 6 Dec 2026, E3/E4 by 31 Jan 2027, E5 form live with upload 3 (2 Feb 2027), A3 by 5 Jul 2027. Agrees with register.
- No time budget for the register lines in PB4's run-in; left to PB10 (PB10 gives admin hours).

#### PB9 (read in full)
- Lines and thresholds; guide (USD 15, Gumroad, net 13.00), build blocks 25 Apr/9 May/23 May/6 Jun, launch Tue 8 Jun 2027 with upload 12; scenarios USD 26/104/567; start rule; rows R1-R8. Arithmetic re-done (209 days, fees, 1.165/month): holds.
- PB3's pointer "PB9 compares them" (email tool prices): delivered in PB9 §6 table.

#### PB10 (read in full)
- Metrics sheet (blocks A-E), 60-minute procedure, Q1 and Q2 run with invented values, annual page, templates. All sums, medians, Wilson intervals, binomial and Poisson figures re-computed: hold.
- Candidates: (a) §4 "One row is misread downstream" and §5 "Where the sixty minutes themselves come from" quote PB1/PB4/PB7 wording those units no longer carry (corrected 13 Nov 2026); (b) D4 Q2 format change "in place of the finished piece alone" against PB5 §7 rule 1 and D A (already side by side); (c) D4 HO3 "from 19 Jun" / "from 3 Jul" against PB4 D2's calendar (12 Jun / 26 Jun); (d) D3: piece 5's third Saturday (20 Feb) is piece 6's first session in PB4 D2, yet pieces 6-7 take two weekends and publish on date: cascade not explained.

#### DD-PB1 (read in full)
- Six creators (Abdaal, Pascual, Boyd, Anderson, Itsines, Wicks), left-out list, PB1 §9 checklist per creator, PB6/PB7 rules read where outside evidence reaches, survivors' limits, Mara's brief (five constants, four rules), template. Month arithmetic re-done (38, 42, 787 days): holds. 17 of 18 points unpublished, said plainly.
- §10 plateau bullet dates Boyd's and Anderson's vidIQ data 13 Nov and then cites "vidIQ, data 11 Nov 2026" for all three (minor, within the unit).

#### DD-PB2 (read in full)
- Floor EUR 1,500, runway EUR 18,000 (20 months, first read Mon 2 Apr 2029), T = USD 1,657.80, Path A Mon 7 Jul 2042 (re-run by script: holds), Path B no date (runway bound), Path C Mon 3 Jan 2028 conditional. All weekdays and first-Monday checkpoints verified. Neither quitting nor staying is advised.
- All twelve units read. Cross-unit candidates being verified with grep before the report is written.
