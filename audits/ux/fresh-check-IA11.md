---
audit: fresh check
unit: IA11 · Validating an IA: evidence, methods, numbers
course: ux · IA · Information Architecture
model: Fable 5.2 (claude-fable-5-2, confirmed from the agent's transcript; live search). The session's "fable" model is now Fable 5.2, not the Fable 5.1 method §4 names, so by the rule as written a Fable 5.1 fresh check of IA11 is owed to the Fable stage (P49)
date: 2026-11-10
chat: own Fable 5.2 agent context, not shown the writing (P31), launched by the U-11 chat (Opus 5.5 as the orchestrating chat; the writer ran on Opus 5.5) in session https://claude.ai/code/session_01KMmgR2ZJvL25WNeciiyWda
verdict: fix · 2 error, 13 should-fix, 10 minor
---

The checker's final report, verbatim: its hand-back message, extracted by script from its transcript (the `SubagentHandback` call). Its own `out/report.md` holds only early progress notes (the harness refused its full report file, as the report says), so the hand-back is the record. Transcript checks (U-11 chat): no tool named `mcp__*`, Projects, Artifact, connector or Agent; every one of its 23 WebFetch URLs was returned verbatim by an earlier WebSearch in its transcript; no redirect followed; the one rate-limited URL (nngroup.com, card sort vs tree test) was not fetched again; three URLs (nngroup.com interpreting tree tests, twice more; the Lewis and Sauro PDF and the Katsanos preprint, once more each) were fetched again after successful fetches, recorded, not a breach (U-10's reading); every path inside its folder.

Model: I am running as Fable 5.2 (claude-fable-5-2), not Fable 5.1. A Fable 5.1 fresh check is therefore STILL OWED for IA11.

# IA11 fresh check · "Validating an IA: evidence, methods, numbers"

Integrity: `sha256sum` of unit/IA11.md and unit/IA11-readonly-copy.md both give 413e83c696090beecdc675f7213bdcbd2ce9e125c4c63b356f1c3f2e6fb009cb, the value in unit/sha256.txt for both; `cmp` reports the two files identical. The unit was not edited.

Report file: /home/claude/agents/ia11-checker/out/report.md holds only my early progress notes (written by shell before the final pass). The final write of the full report with the Write tool was refused by the harness ("Subagents should return findings as text, not write report files"), and I did not work around the refusal. This reply is the full report and the record; the caller should save it to out/report.md if the file is needed. My scripts are in /home/claude/agents/ia11-checker/out/work/calc.py and /home/claude/agents/ia11-checker/out/work/struct.py.

Scope notes. No audit report exists for this unit, so step 6's errata list is empty; step 6 was run as pointer checks only. Every count and calculation was re-run by script. Every Current below was checked with `grep -F -c` on unit/IA11.md and occurs exactly once. Web rule kept: one fetch was rate-limited (Tankala, "Card Sorting vs. Tree Testing") and was not retried. No memory, Project, connector or Artifact tool was used.

## 1 · Coverage (brief item: covered / thin / missing)

- Open, closed, hybrid card sorting, what each proves and does not: covered (2.1). Spencer's Card Sorting: thin, and said so (contents page plus Gaffney's review; text not read). NN/g guidance: covered (Nielsen 2004; Tankala through IA3 and IA9).
- Tree testing: covered (2.2, 3.2, 4.2).
- First-click testing: covered (2.3, 3.3, FC-A).
- Search-log analysis: covered (2.4); Rosenfeld's book thin, and said so (contents and publisher's line only; substance through IA3's Farrell).
- Analytics path and funnel review: covered (2.5), on one source carried through IA9 (Cardello); no new source.
- Task-based usability testing of a built navigation: covered (2.6, UT-A).
- Sample sizes and reliability: card sorts covered (three studies; Tullis and Wood only as reported, said so); tree tests covered as "no study found", with guidance labelled; vendor guidance labelled (dscout, definition only).
- Metrics (success, directness, time, agreement): covered (1.2, 4.2, 4.3).
- Running cheaply and remotely, no tool required: covered (5).
- Results into IA changes; when a result is too weak: covered (6.1 to 6.4).
- No access to users, bridge to IA12: covered, short (7).
- Figures asked for: method-selection table (Fig. 1), card-sort result as similarity matrix (Fig. 4, plus placement Fig. 3), tree-test result (Fig. 2), confidence ladder (Fig. 6): all present; Fig. 5 (intervals) extra. Six figures, within three to eight.
- Deliverable: validation plan with question, method, participants, what decides, cost (A, V-01 to V-17): present in full. Tree-test script with tasks, correct nodes, instructions (B): present in full. Closed card-sort protocol with cards, categories, instructions (C): present in full. Analysis template for each (TT-A, CS-A, FC-A, UT-A, SG-A): present. Usable alone, given the IA6 identifiers it cites.
- Takes (IA6's app IA; IA3's findability evidence) and Gives (plan, scripts, templates; IA12's tests per assumption; DD-IA2's measurement model): met.

## 2 · Findings

1. [error] [figure] section 4.3, Figure 4; Current: `which is why bike helmet's cells against gym membership and train pass do not add to 100.`; Problem: Figure 4 draws four off-diagonal values the text never states: yoga class with coding course 25, yoga class with cookery course 17, gym membership with bike helmet 17, yoga class with bike helmet 17. Two of them (yoga with cookery, yoga with helmet) are joint facts that cannot be derived from the placement counts in the text (the overlap could be 0 to 3, and 0 to 2), so the figure adds facts. Fix: `which is why bike helmet's cells against gym membership and train pass do not add to 100. The other cells follow from who placed what (Perqo, fictional): the 3 who placed yoga class in Learning put it with coding course (25%), and 2 of them had also placed cookery course in Learning (17%); the 2 who placed bike helmet in Health put it with gym membership (17%), and both had yoga class in Health too (17%).`; Basis: sourcing-standard.md Part 1 ("A figure adds no fact"); script check of Figure 4 against section 4.3's counts.
2. [error] [figure] section 3.1 / Figure 1; Current: `that a second study of similar people would largely reproduce.`; Problem: Figure 1's Participants cell for the hybrid sort, "as an open sort", has no sentence in section 3 (the caption says the participant numbers are section 3's); none of the three studies is about hybrid sorts. Fix: `that a second study of similar people would largely reproduce. None of the three studied a hybrid sort; its added groups are read as an open sort's are, so this unit gives it the open sort's numbers (this unit's reasoning, unsourced).`; Basis: sourcing-standard.md Part 1; unit section 3.1.
3. [should-fix] [accuracy] Deliverable D, TT-A; Current: `every other task is undecided at 12, as section 3.4 says it must be`; Problem: the table above it gives T3 "pass (pilot: held)": 12 of 12 has a lower end of 71.8%, above T3's 70% mark; and section 3.4 does not say every task must be undecided. Fix: `T3's 12 of 12 clears its 70% mark and is held as a pilot result; every other task is undecided at 12`; Basis: script: 12/12 gives 71.8 to 100; unit TT-A row T3.
4. [should-fix] [accuracy] section 4.4, T7 bullet; Current: `it cannot show a pass, because a pass needs a narrow one.`; Problem: contradicted by the unit's own verdicts (T3 passes at 12 of 12; C-03 and eight cards "confirmed"; C-05 "keep"). Fix: `it can show a pass only at the extreme: at 12 participants nothing short of 12 of 12 clears a 70% mark (T3 does), and nothing clears 80%.`; Basis: script: 11/12 lower end 62.5%, 12/12 lower end 71.8%.
5. [should-fix] [attribution] section 2.2; Current: `Boxes and Arrows, undated and with no byline on the page as read,`; Problem: the page carries a byline and a date: Iain Barker, 24 April 2007. Fix: `Iain Barker, Boxes and Arrows, 24 April 2007,`; Basis: https://boxesandarrows.com/measuring-the-success-of-a-classification-system/ (fetched 10 Nov 2026; byline and date as the fetch read them, one reading).
6. [should-fix] [attribution] Sources; Current: `- Boxes and Arrows. "Measuring the Success of a Classification System". Undated, no byline on the page as read (practice).`; Problem: as finding 5. Fix: `- Barker, Iain. "Measuring the Success of a Classification System". Boxes and Arrows, 24 April 2007 (practice).` (and move the entry to its place under B, after Bailey); Basis: as finding 5.
7. [should-fix] [attribution] Unsure list; Current: `- The Boxes and Arrows article: no byline or date was shown on the page as read; it is cited by its publication.`; Problem: as finding 5; the line is now wrong. Fix: delete the line (replace with the empty string); Basis: as finding 5.
8. [should-fix] [accuracy] section 3.4; Current: `Every interval in this unit and its templates is computed this way.`; Problem: the unit attributes its interval method to Lewis and Sauro 2006 (Figure 5's caption), but that paper puts 1.645 in place of 1.96 when x = 0 or x = n, because one side of the interval is fixed. The unit uses 1.96 for 12 of 12 (71.8%); with 1.645 the lower end is 78.4%, and a perfect score clears 80% at 14 participants, not 19. The unit's choice is defensible and conservative but must be declared, since "no perfect score can until 19 participants" depends on it. Fix: `Every interval in this unit and its templates is computed this way. Lewis and Sauro put 1.645 in place of 1.96 for their adjusted estimate when x = 0 or x = n, where one side of the interval is fixed; this unit keeps 1.96 throughout, the more cautious choice, so its lower end for a perfect score (71.8% at 12 of 12) is lower than 1.645 would give (78.4%).`; Basis: Lewis and Sauro 2006, https://uxpajournal.org/wp-content/uploads/sites/7/pdf/JUS_Lewis_May2006.pdf ("When x=0 or x=n (so one side of the confidence interval is fixed), it is necessary to use 1.645"); script.
9. [should-fix] [attribution] section 6.2; Current: `Laubheimer's diagnostics narrow the options: concentrated wrong first clicks point to the top level`; Problem: "wrong first clicks point to the top level" is the Boxes and Arrows article's reading (as section 4.2 itself says); Laubheimer 2024 reads the first clicks of a low-success task as places where the item could be moved or cross-listed. Fix: `Two diagnostics narrow the options: concentrated wrong first clicks point to the top level (the Boxes and Arrows article, practice), Laubheimer reads the first clicks of a low-success task as the places where the item could be moved or at least cross-listed`; Basis: https://nngroup.com/articles/interpreting-tree-test-results/ ; https://boxesandarrows.com/measuring-the-success-of-a-classification-system/
10. [should-fix] [deliverable] Deliverable B, B.4, T10; Current: `You want to understand how the money shown in the app works and what it can be spent on.`; Problem: the second clause makes What you can claim in each category (TN-12) and the category screens defensible answers, yet the script marks them wrong (2 of the pilot's 3 failures are TN-12); by the unit's own section 6.3, reason 4, the task measures two questions. Fix: `You want to understand how the money shown in the app works.` (TT-0's T10 and FC-1's F3 then use the same words); Basis: unit B.3 (TN-12 stands for H-2.1.3), TT-A row T10, section 6.3.
11. [should-fix] [accuracy] Deliverable A, V-13; Current: `M-07 per query for "allowance", "gym" and "refund"`; Problem: IA3's log gives zero results for "allowance" and "gym" only; "refund" returned H-2.1.2, and IA9, section 6.1, names only "allowance" and "gym" as the queries the next log must clear. Fix: `M-07 per query for "allowance" and "gym", the two that returned zero results (IA3, section 5.2), and the rank of "refund"`; Basis: vault IA3, section 5.2 table; vault IA9, section 6.1.
12. [should-fix] [accuracy] Deliverable D, SG-A, LG-1 row; Current: `zero-result searches for "allowance", "gym", "refund"`; Problem: as finding 11. Fix: `zero-result searches for "allowance", "gym"`; Basis: as finding 11.
13. [should-fix] [deliverable] Deliverable D, SG-A; Current: `rung (C1 for a single read; C5 for a before-and-after read of a released change)`; Problem: the plan gives V-02 (AN-2) and V-16 (AN-4) rung C5, but both are single reads of one quarter, which this rule and the ladder's C1 ("read once") make C1; V-09 is a randomised comparison, not a before-and-after read. Fix: `rung (C1 for a single read that raises a hypothesis about the structure; C5 for a read that measures in use the behaviour the assumption is about, as AN-2 to AN-4 do, or a before-and-after read of a released change)`; Basis: unit section 6.4 table; Deliverable A rows V-02, V-09, V-16.
14. [should-fix] [deliverable] section 6.4, table; Current: `| C5 Confirmed in use | production records before and after a release |`; Problem: as finding 13. Fix: `| C5 Confirmed in use | production records of the behaviour itself, or before and after a release |`; Basis: as finding 13.
15. [should-fix] [figure] section 6.4, Figure 6; Current: `"cells": ["production records before and after a release",`; Problem: as finding 13; the figure must match the table. Fix: `"cells": ["production records of the behaviour itself, or before and after a release",`; Basis: as finding 13.
16. [minor] [figure] section 2.7, Figure 1; Current: `"about 50 for a share"`; Problem: reads as a general requirement; the text gives 50 as the Perqo plan's number and Sauro's 193 for a 7% margin. Fix: `"50 in the Perqo plan; about 193 for a 7% margin"`; Basis: unit section 3.1; https://measuringu.com/card-sorting/
17. [minor] [deliverable] Deliverable B, B.4, T1; Current: `You want to know how much you have left to spend on a train pass this month.`; Problem: "this month" implies a monthly period; the register leaves the period's length free (IA8, section 3.3). Fix: `You want to know how much you have left to spend on a train pass.`; Basis: perqo-facts.md, "Set by IA8" and "Not yet set".
18. [minor] [accuracy] Deliverable A, V-17; Current: `on the tasks whose answers moved?`; Problem: T7 is among the five tasks and its correct node is "as TT-1" (Account › Notifications in both trees). Fix: `on the tasks whose answers, or the tab around them, changed?`; Basis: unit B.6 table.
19. [minor] [attribution] Sources, "Cited through the filed units"; Current: `NN/g, 2018 (IA4);`; Problem: section 2.2 cites Zaphiris 2000 and Larson and Czerwinski 1998 through IA4 and IA3, and neither is in the list (Part 1: every source cited is listed). Fix: `NN/g, 2018 (IA4); Larson and Czerwinski, "Web Page Design: Implications of Memory, Structure and Scent for Information Retrieval", CHI 98, 1998 (IA3, IA4); Zaphiris, "Depth Vs Breadth in the Arrangement of Web Links", HFES 44th Annual Meeting, 2000 (IA4);`; Basis: vault IA3, section 6.2; vault IA4, section 2.1.
20. [minor] [style] section 3.4; Current: `Their book with the same authors carries`; Problem: redundant wording. Fix: `Their book carries`; Basis: none needed.
21. [minor] [accuracy] opening table, last row; Current: `IA7, IA8, IA9 and IA10, "What later units take"`; Problem: IA7's heading is "What IA8 and later units take". Fix: `IA7, "What IA8 and later units take"; IA8, IA9 and IA10, "What later units take"`; Basis: vault IA7, line 613.
22. [minor] [deliverable] Deliverable B, B.3; Current: `Elements on Home are nodes under Home.`; Problem: the tree is called the app "as designed (IA6, Deliverable B, B.3)" but silently leaves out six of that map's boxes, while TT-0 keeps Check and submit. Fix: `Elements on Home are nodes under Home. Left out, because no task can end on them: Join and sign in (A-0), which a signed-in employee does not see; the screens reached only inside a flow or from a list item (Check and submit, Claim submitted, Claim, Purchase); and How approval rules work, a link on New claim. The four Claims groups are nodes, since the Claims screen shows them.`; Basis: vault IA6, Deliverable B, B.3.
23. [minor] [accuracy] Deliverable A.2, row 17; Current: `RV-02 counts, read at RV-10`; Problem: IA9's test is RV-02's share of built screens that differ from their F3 artefact, compared from quarter to quarter; IA9 does not send it to RV-10. Fix: `RV-02's share of built screens that differ from their F3 artefact, compared from quarter to quarter`; Basis: vault IA9, "What later units take", row 1.
24. [minor] [figure] section 6.4, Figure 6 caption; Current: `Rungs this unit's construct: C1 from IA9, section 6.4,`; Problem: the caption sources every rung but C0. Fix: `Rungs this unit's construct: C0 from IA2, section 5.2 ("assumed"); C1 from IA9, section 6.4,`; Basis: unit section 6.4 table, C0 row.
25. [minor] [style] Deliverable D, FC-A; Current: `read against F2's purpose`; Problem: "F2" has three meanings in this unit (fidelity F2, task F2, IA3's checklist item F2); the sentence does not say which. Fix: `read against IA3's item F2 (is everything the task needs reachable from here?)` if the checklist item is meant; Basis: vault IA3, checklist row F2.

Not findings, noted: FC-1's F6 does not count the Account tab although TT-1's T8 counts Help (TN-30); the file runs to about 19,000 words against the brief's 2,000 to 6,000, in line with IA6 and IA7; "the word card ... (IA3, D1)" in section 6.3 leans on D1 for more than D1 says.

## 3 · Checks by heading

(3) Whose figure: every number names its owner (Nielsen, Sauro, Laubheimer, O'Brien, Bailey, Katsanos, Lantz, or "this unit's rule" for the marks 80/70/15/50 and the two-of-five threshold). PASS.
(4) Labels: Sauro (practice, a consultancy), dscout (vendor documentation), O'Brien (practice), Krug (practice), Boxes and Arrows (practice), Gaffney (review, practice) labelled; tree-test numbers labelled guidance; Bailey's .87 labelled a likelihood across scenarios and its missing sample noted; Katsanos limited to similar profiles. PASS.
(5) Deliverable: present in full, follows from the body, usable alone. PASS with findings 10 to 15, 17, 18, 22, 23, 25.
(6) Errata: none exist for this unit. Pointers to filed units checked against the vault: see Confirmed; exceptions are findings 11, 12, 21, 23.
Public-site rules: no personal fact about the reader; no private person named (only published authors); "(Perqo, fictional)" on first use (line 12) and at each new fact; every pilot result is labelled fictional in text and captions; no real study's data is presented as a card-sort or tree-test result. New Perqo facts (pilot, marks, TN- identifiers, "offers are in Meals only", recruitment through customer success, DL-016) contradict nothing in perqo-facts.md; DL-016 is the next free number after IA10's DL-015. PASS but for finding 17.

## 4 · Figures (step 7)

- Figure 1, matrix, section 2.7 (method selection). Eight rows, five columns; every row tone 5, named in the text. Row labels 9 to 19 characters, each a method of sections 2.1 to 2.6. Cells trace to sections 2.1 to 2.6, 3 and 5, except the hybrid sort's "as an open sort" (finding 2) and "about 50 for a share" (finding 16). Caption says what it shows, the section and the sources. Kind fits (items by sections). FIX: apply finding 2 to the text and replace the cell `"about 50 for a share"` with `"50 in the Perqo plan; about 193 for a 7% margin"`.
- Figure 2, bars (stacked), section 4.2 (tree-test result). Ten rows; values 12/0, 11/1, 12/0, 11/1, 10/2, 9/3, 4/8, 10/2, 11/1, 9/3 match TT-A's Success column and each sums to 12; labels are B.4's short names; tones 3 and 6 named in the text. Caption gives section, definition source and the T2 note. Kind fits (numbers compared). PASS.
- Figure 3, numeric matrix, section 4.3 (placement shares). Twelve rows, each summing to 100; values are the text's counts of 12 as rounded percentages (9, 3, 11, 1, 7, 5, 9, 2, 1 of 12 give 75, 25, 92, 8, 58, 42, 75, 17, 8); row labels are C.2's card texts, longest "Dinner at a restaurant" (22 characters); tone 3 named. Caption gives section and sources. Kind fits. PASS.
- Figure 4, numeric matrix, section 4.3 (similarity). Symmetric; consistent with the placements; four values not in the text (finding 1). Tone 3 named; row labels short (14 characters at most). Caption gives section and sources. Kind fits (the brief asks for a similarity matrix). FIX: no change to the JSON; add finding 1's sentence to the text.
- Figure 5, range, section 4.4 (intervals). All seven rows recomputed: 71.8 to 100; 62.5 to 100 (91.7); 13.6 to 61.2 (33.3); 19.3 to 68.1 (41.7); 13.6 to 61.2 (33.3); 8.3 to 53.9 (25.0); 66.8 to 88.9 (80.0). Each is in TT-A, CS-A or section 3.4; ticks are the plan's marks; tones 3 and 6 named. Caption gives method, section and source. Kind fits (a low-to-high bar with a point). PASS (finding 8 adds a sentence to the text, no change to the figure).
- Figure 6, matrix, section 6.4 (confidence ladder). Six rows; cells are short forms of the table above it; rows tone 5 and the Perqo column tone 3, both named in the text; row labels 10 to 19 characters. Kind fits. FIX: replace `"cells": ["production records before and after a release",` with `"cells": ["production records of the behaviour itself, or before and after a release",` (finding 15) and in the caption replace `Rungs this unit's construct: C1 from IA9, section 6.4,` with `Rungs this unit's construct: C0 from IA2, section 5.2 ("assumed"); C1 from IA9, section 6.4,` (finding 24).
- All six blocks parse as JSON; every key is in VIZ_KEYS for its kind; every matrix row has as many cells as columns. No flow figure, so no step notes to check. Tones drawn: 3, 5, 6, all three named in the unit's second paragraph and matching IA2, section 5.2. Every identifier a figure draws (T1 to T10, C0 to C5, TT-1, CS-1, FC-1, AN-1) is stated in the text.

## 5 · Confirmed (claims checked and found right)

Calculations (script):
- Section 3.4 table: 4/5 36.0 to 98.0; 8/10 47.9 to 95.4; 16/20 57.8 to 92.5; 40/50 66.8 to 88.9; 80/100 71.0 to 86.7. Widths are the differences of the printed ends (40/50 is 22.2 unrounded, 22.1 from the printed ends; consistent with the other rows' method).
- Thresholds at 50: 70% passes at 42 and fails at 28; 80% passes at 46 and fails at 34; cross-listing kept at 13, removed at 2; home confirmed at 32. 42 of 50 is 84%.
- Every interval in TT-A, CS-A and the cross-listing line (1, 2, 3, 4, 5, 7, 9, 10, 11, 12 of 12); every verdict follows from its interval and mark.
- "No perfect score can until 19 participants" by the unit's formula (18 of 18 gives 79.3%, 19 of 19 gives 80.2%).
- Binomial: a problem met by one in three shows in two or more of five 53.9% of the time. 1 − 0.69^5 = 84.4%, Nielsen's "85%".
- TT-A: correct-node counts sum to successes and wrong-node counts to failures on all ten tasks; first-click counts agree with the tree's parents; T6 9 successes and 7 direct; T7 8 wrong first clicks = Purchases 6 + Card details 2; times run 7 to 21 seconds.
- Counts: M-01 to M-11 (11); V-01 to V-17 (17); A.2 rows 1 to 25 (25 = IA7's 9 + IA8's 7 + IA9's 5 + IA10's 6, less two merged); TN-00 to TN-30 (31); C-01 to C-12; T1 to T10; F1 to F6; U1 to U3; C0 to C5; eight cards at 100%.
- O'Brien's 20 tasks at 10 each needing 100 participants for 50 answers; .87/.46 = 1.9; Sauro's 193 gives a 7.05% margin at 95%.

Sources opened (10 Nov 2026):
- Nielsen 2004: 18 July 2004; 168 users at Fidelity; 0.75, 0.90, 0.95, 0.98 at 5, 15, 30, 60; "Tullis and Wood recommend testing 20–30 users for card sorting."; the 0.90/0.93 sentence; "Card sorting is a generative method"; 15 users, 30 for big projects; the UPA 2004 paper title. PASS. https://www.nngroup.com/articles/card-sorting-how-many-users-to-test/
- Sauro 2012: 3 April 2012; both definitions verbatim; "above .93" at 20 to 30; the 193 sentence verbatim; dendrograms "notoriously subjective, especially when there isn't high agreement between users"; "the percent of users who place cards in each category". PASS. https://measuringu.com/card-sorting/
- Laubheimer 2024: 19 January 2024; success, directness and time definitions (time is an average); "Even though 74% of users eventually found the right answer, only 50% took a direct path."; the first-click sentence; sub-category labels, multiple categories, polyhierarchy for "a substantial portion"; two-proportion test and t-tests. The "50+ participants" quotation is exact as far as it runs; the source sentence goes on "and find a statistically significant difference between them". PASS. https://nngroup.com/articles/interpreting-tree-test-results/
- Laubheimer 2023: 6 August 2023; definition; "completely devoid of visual styling and content"; "focuses exclusively on evaluating the findability"; "requires only a few participants"; "often executed as a remote, unmoderated study"; "should avoid using terms that give away the answers". PASS. https://nngroup.com/articles/tree-testing/
- Boxes and Arrows article: top 3 or 4 levels on index cards; around 15 tasks; ten to fifteen 30-minute one-on-one sessions; no word on correctness; last selection recorded; "indicative"; correct location the evaluator's decision; first-click reading. PASS on content; byline and date FAIL (findings 5 to 7). https://boxesandarrows.com/measuring-the-success-of-a-classification-system/
- Nielsen 2000: 18 March 2000; "31%, averaged across a large number of projects we studied"; 85%; "a single monster study with 15 users"; distinct groups; the pointer to 20 users for quantitative studies; Nielsen and Landauer, INTERCHI '93. PASS. https://nngroup.com/articles/why-you-only-need-to-test-with-5-users/
- Lewis and Sauro 2006: vol. 1, issue 3, May 2006, pp. 136 to 150; "Always compute a confidence interval, as it is more informative than a point estimate."; 95% adjusted-Wald for most usability work; adjustment when n < 20; centre (x + z²/2)/(n + z²). PASS, with finding 8. https://uxpajournal.org/wp-content/uploads/sites/7/pdf/JUS_Lewis_May2006.pdf
- Bailey and others 2009: LNCS 5619, pp. 3 to 12; .87 and .46 verbatim; ratio 1.9, range 1.4 to 2.7; no sample stated; "over 100 FirstClick scenarios" against 10 to 15; .82 between page views and time. PASS. https://link.springer.com/content/pdf/10.1007/978-3-642-02806-9_1.pdf
- Lantz and others 2019: six authors in the unit's order; Journal of Classification 36(3), 649 to 658; "approximately 10–15 participants provided optimal estimation of the similarity matrix"; pairwise judgements as gold standard. PASS. https://ideas.repec.org/a/spr/jclass/v36y2019i3d10.1007_s00357-018-9292-8.html
- Katsanos and others 2019: six open sorts, 140 participants, three travel and three eshop, 16 to 34 each; Mantel r 0.609 to 0.930, p < 0.001; 63.2% to 92.7%; the "justifies" sentence; tech-savvy students and practitioners. PASS. Author order as the unit gives it matches the published record's key (KatsanosTADSA19, from a search result); the preprint's first page extracts in another order. https://arxiv.org/pdf/1903.08644
- Sauro 2011: 21 March 2011; 78%; 1,189 tasks, 115 tests, 3,472 users; above 92% top quartile, below 49% bottom. PASS. https://measuringu.com/task-completion/
- O'Brien: ch. 9, "Recruiting participants"; updated 27 August 2024; "Aim for about 50 participants per user group"; 30, 50 to 100, diminishing returns; the 100-participant example. PASS. https://treetesting.atlassian.net/wiki/spaces/TTFW/pages/1310747/How+many+participants
- Gaffney 2009: User Experience 8(3), 2009, printed "Gaffney, G."; open and closed; physical cards; teams; spreadsheet first; cluster analysis and MDS; the "nice outputs" words are Spencer's, quoted by the reviewer. PASS. https://oldmagazine.uxpa.org/?p=5384
- Krug 2014: both quotations verbatim in the publisher's excerpt of the 3rd edition; no chapter given there. PASS. https://www.peachpit.com/articles/article.aspx?p=2209313
- dscout: hybrid and closed lines verbatim; undated. PASS. https://help.dscout.com/study-basics/question-types/card-sort-questions
- Spencer 2009 contents: chs 4, 6, 7, 8, 9, 10 as named. PASS. https://rosenfeldmedia.com/?p=187469
- Rosenfeld 2011 contents: chs 3 to 10 as named; "Search queries are gold: ..." verbatim. PASS. https://rosenfeldmedia.com/books/search-analytics
- Sauro and Lewis 2016 contents: 2nd ed., Morgan Kaufmann, 2016; chs 3, 4, 6, 7 as described. PASS. https://www.schweitzer-online.de/en/buch/Sauro/Quantifying-User-Experience/9780128023082/A35053706/

Unverifiable (not checked):
- Tankala, "Card Sorting vs. Tree Testing", NN/g, 23 February 2024: fetch rate-limited, not retried; the two quotations match IA9, section 6.4, word for word.
- Tullis and Wood 2004 and Nielsen and Landauer 1993: not opened; the unit cites both only as reported, and the reports hold.
- The text of Spencer 2009, Rosenfeld 2011 and Sauro and Lewis 2016: not opened; the unit claims only their contents.
- Sources carried through filed units (Farrell 2017, Cardello 2013, Budiu 2020, Mausser 2011, Tankala June 2024, Laubheimer 2018, Zaphiris 2000, Larson and Czerwinski 1998): not reopened; each checked against what IA3, IA4 and IA9 say.

Pointers to filed units, found as stated:
- IA2, section 5.2: six tones; tone 3 the app and the employee, tone 5 shared, tone 6 a stop; "assumed" in a note.
- IA3: section 1.1 threshold; 1.2 Budiu and H-2.2.1; 3.2 Tankala's sentence verbatim; 3.3 the three far members and six items; 5.1 the Help centre is where the app's failures show; 5.2 Farrell's list, several months, identifiers removed, "proxy evidence, useful when no one can be interviewed, and labelled as proxy" verbatim, "gym" zero results; 6.1 the tree test as the measure; 6.2 a few times a month; checklist A1 to A3, B1, B2, C2, C3, E1, E2; "What this hands on"; the as-is navigation, which TT-0 reproduces node for node.
- IA4: section 4.3 sentence verbatim; 2.1 and R7 (depth slowed people in every study); 2.2; R6; B.3, BI-001 to BI-012, each matching C.2's card, home and second place.
- IA5: H-1.2.5 also listed under H-2.1; Help opens H-2; S-6.
- IA6: twelve assumptions, V-01 to V-12 in its order; A.1 priorities and T- numbers for every task mark in B.4; section 3.2; section 4.3; B.2 E1 (no search); B.3 map against TN-01 to TN-30 (identifiers, parents, H- pages); Recent activity items open their Claim; B.4 E-2, E-4, E-7, E-8; B.5 route only when a category has offers; B.6 leaves the banner comparison to IA11.
- IA7, IA8, IA9, IA10 assumption tables (each with a "Test (IA11)" column, as IA6's): each of the 27 rows is in A.2 or the plan; IA8, section 4.5 (a declined attempt is not in Purchases); G-5; CL-4.
- IA9: section 6 and 6.1 to 6.4; "as declined, with the test as its reason" verbatim; Tankala's two phrases; Cardello's three uses; screen views by identifier; RV-04, RV-05, RV-06, RV-10, RV-11 (trigger: a change to a top level or a tab); W-09 and W-17 wording verbatim; decision log to DL-010.
- IA10: section 2.5 customer success; 2.7 clients' words as variants; FO-01, FO-03, FO-06, FO-07 (admin users from at least two clients); TP-05; DL-011 to DL-015.

## 6 · Verdict

IA11: fix. 2 errors, 13 should-fix, 10 minor. A Fable 5.1 fresh check is still owed (this check ran on Fable 5.2).

Sources:
- [Card Sorting: How Many Users to Test](https://www.nngroup.com/articles/card-sorting-how-many-users-to-test/)
- [10 Things to Know about Card Sorting](https://measuringu.com/card-sorting/)
- [Tree Testing Part 2: Interpreting the Results](https://nngroup.com/articles/interpreting-tree-test-results/)
- [Tree Testing: Evaluate Menu Labels and Categories](https://nngroup.com/articles/tree-testing/)
- [Measuring the Success of a Classification System](https://boxesandarrows.com/measuring-the-success-of-a-classification-system/)
- [Why You Only Need to Test with 5 Users](https://nngroup.com/articles/why-you-only-need-to-test-with-5-users/)
- [Lewis and Sauro 2006, JUS](https://uxpajournal.org/wp-content/uploads/sites/7/pdf/JUS_Lewis_May2006.pdf)
- [Bailey and others 2009](https://link.springer.com/content/pdf/10.1007/978-3-642-02806-9_1.pdf)
- [Lantz and others 2019, record](https://ideas.repec.org/a/spr/jclass/v36y2019i3d10.1007_s00357-018-9292-8.html)
- [Katsanos and others 2019, preprint](https://arxiv.org/pdf/1903.08644)
- [What Is A Good Task-Completion Rate?](https://measuringu.com/task-completion/)
- [O'Brien, How many participants?](https://treetesting.atlassian.net/wiki/spaces/TTFW/pages/1310747/How+many+participants)
- [Gaffney, Deal Them Again](https://oldmagazine.uxpa.org/?p=5384)
- [Krug excerpt, Peachpit](https://www.peachpit.com/articles/article.aspx?p=2209313)
- [dscout, Card sort questions](https://help.dscout.com/study-basics/question-types/card-sort-questions)
- [Spencer, Card Sorting, Rosenfeld Media](https://rosenfeldmedia.com/?p=187469)
- [Rosenfeld, Search Analytics for Your Site](https://rosenfeldmedia.com/books/search-analytics)
- [Sauro and Lewis, Quantifying the User Experience, contents](https://www.schweitzer-online.de/en/buch/Sauro/Quantifying-User-Experience/9780128023082/A35053706/)

## Maintainer's notes (U-11 chat, 10 November 2026)

Each finding was verified against the unit, the filed units (IA3, section 5.2's log; IA6, Deliverable B, B.3; IA7's "What IA8 and later units take"; IA9's "What later units take", row 1; IA3's checklist item F2; IA4's and IA3's Sources; the register's "Not yet set": the period's length) and, for the outside sources, the maintainer's own searches and fetches under the web rule: boxesandarrows.com (byline Iain Barker, 24 April 2007; "Lots of red in the 'getting first click right' cells" read as a top-level problem), nngroup.com, "Tree Testing Part 2: Interpreting the Results" (first clicks "suggest locations where the item should be moved (or at least cross-listed)"; nothing there reads concentrated wrong first clicks as a top-level problem), and uxpajournal.org, Lewis and Sauro 2006 (the PDF). Applied as exact replacements by script, each Current occurring once:

- Findings 1 to 7, 9, 11 to 25 applied as the report gives them, with three adjustments. Finding 19: Larson and Czerwinski placed after Farrell and Zaphiris after the last Tankala, so the list keeps its alphabetical order. Finding 24: the caption's quotation marks around assumed are single, since the caption is a JSON string (the report's double quotes broke the block). Finding 25: the report's conditional Fix taken with IA3's own wording of item F2, quoted.
- Finding 8 holds in part. The paper's 1.645 for x = 0 or x = n is for its Wilson point estimate (the interval's centre); the paper does not say to move the interval's ends, so the 78.4% the report computes is not the paper's figure. Applied as: the paper's substitution stated for the point estimate, and this unit's 1.96 for every interval's ends kept and called the cautious choice for a perfect score. The writer's adjusted-Wald unsure line was extended with what the check read.
- Finding 10 applied, and T10's row in B.4 gained a note that the pilot ran with the cut wording, so its pilot result understates success (the pilot's numbers stand as recorded).
- Not findings (the report's "noted" line): FC-1's F6 and the length note recorded, not acted on; the D1 point is the checker's reading, not a finding.
- Figures. Figures 2, 3 and 5 passed the check. Figure 1 (finding 16's cell; finding 2's sentence for its hybrid cell), figure 4 (finding 1's sentence for its four cells) and figure 6 (findings 15 and 24) are re-checked by new agents below.
- The model. The checker ran on Fable 5.2 (claude-fable-5-2), which the session now gives for the model "fable"; method §4 names Fable 5.1, so by the rule as written the Fable 5.1 fresh check of IA11 is recorded as owed to the Fable stage (P49).

## Figure 1, second check (new agent, Opus 5.5, 10 November 2026), verbatim

Given only the unit's text with its figures taken out, the six captions, the figure's declaration, IA2, the figure kinds and the frames sheets `verify.py --shots` saved for it at every width, dark and light. Its hand-back, extracted by script from its transcript, is below; transcript checks: Read, Glob, Grep and Bash only, every path inside its folder, no web, memory, Projects, Artifact or `mcp__*` tool; model claude-opus-5-5 from its transcript.

**Maintainer:** Applied as given, verified against sections 2.1, 2.5, 2.7 and 5: the hybrid sort's cheapest form (section 5 gives it the form with a free-text group; the cell's quotation marks single inside the JSON); the six row labels shortened to the text's words; the caption and section 2.7's paragraph name section 5 for the cheapest forms. Re-checked by a new agent (third check).

Running as Opus 5.5. Fresh figure check of IA11, figure 1 (matrix, section 2.7, method selection). I checked it only against the files in /home/claude/agents/ia11-fig1-check2. My crops are in /home/claude/agents/ia11-fig1-check2/out/.

**1. Every item traces to the text: FIX (one cell)**

Columns. "Answers" traces to 1.1 ("A test answers one question about one part of the structure"). "Proves" and "Does not prove" trace to 2.1 ("What each form proves, and what it does not"). "Participants" traces to section 3. "Cheapest form" traces to section 5 ("Running each method cheaply… What each needs, at the least").

Rows:
- **Open card sort.** 2.1: "An open sort shows how a group of people clusters the content and what they call the clusters. It does not show that a structure built from those clusters can be navigated". 3.1: "15 to 30 participants give a similarity matrix". 5: "Open card sort. The same, with blank headers…", where "the same" is paper cards and "Record one row per participant… in a spreadsheet". PASS.
- **Closed card sort.** 2.1: "A closed sort shows whether people put each item where an existing scheme puts it… It measures agreement with a scheme the team chose, so it cannot show a better scheme the team did not offer". 3.1: "the Perqo plan gives CS-1 50 participants" and "to have a margin of error of around 7% you should plan on having around 193 participants". 5: "a form with one question per card and the categories as its choices (closed)". PASS.
- **Hybrid card sort.** Most cells trace. 2.1: "the groups people add when the given ones do not fit. Those added groups are the gaps in the scheme; they are not yet a tested part of it". 3.1: "this unit gives it the open sort's numbers".
  - **Error:** "Cheapest form" says "paper cards and blank headers". Section 5 gives blank headers to the open sort ("Open card sort. The same, with blank headers the participant names"). It gives the hybrid sort a form "plus a free-text 'another group' choice (hybrid)".
- **Tree test.** 1.1: "Can people find things in this structure?" 2.2: "whether the labels and the grouping of a hierarchy lead people to an item" and "No visual design, no content on the page, no search". 3.2: "50+ participants per tree" and "Fifty participants per tree". 5: "On index cards, moderated". PASS.
- **First-click test.** 2.3: "where people start on a real layout… What it does not: that the task is completed". 3.3: "the Perqo plan gives it the tree test's 50". 5: "A screen image shown on a video call". PASS.
- **Search-log analysis.** 2.4: "what people who searched asked for, in their words, and which searches failed. What it does not: why they searched, what the people who did not search did". A.1, V-13: "none: the log". 5: "An export of the queries… sort by frequency". "Demand" is a fair gloss of "asked for". PASS.
- **Analytics paths.** 1.1: "What do people do with the built product? Asked after release". 2.5: "frequencies, paths and drop-offs, measured on everyone, with no recruiting. What it does not: intent". 5: "The screen views by identifier". PASS.
- **Usability test.** 2.6: "whether real tasks succeed on the whole system… and why they fail" and "What it does not prove at five participants is a rate. Five people find problems". 2.6 also has "three rounds of five", and 5 has "five participants a round". 5: "A video call… a prototype or the built app". PASS.

Legend. "tone 5, shared: a method serves any surface" traces to 106: "Every row is tone 5, since a method serves any surface". PASS.

**2. Caption: FIX**

What passes:
- It says what the figure shows and the decision it supports, and names section 2.7 and Deliverable A.
- Every source it names is cited in the text, with the line:
  - Nielsen 2004: line 35 and Sources.
  - Sauro 2012: 2.1.
  - dscout: 2.1.
  - Tankala 2024 through IA3: 2.1.
  - Laubheimer 2023 and 2024: 2.2 and 2.3.
  - Boxes and Arrows: 2.2.
  - Bailey 2009: 2.3.
  - Rosenfeld 2011: 2.4.
  - Farrell 2017 through IA3: 2.4.
  - Cardello 2013 through IA9: 2.5.
  - Nielsen 2000 and Krug 2014: 2.6.
- It says Perqo is fictional.

**Fault:** the whole "Cheapest form" column comes from section 5, and neither the caption nor the text says so. The caption names only section 2.7 and section 3. Line 106 says the cells are "short forms of what those sections say" (2.1 to 2.6) and the participant numbers are section 3's.

**3. Kind: PASS**

The data is items by sections: eight methods against five dimensions. That is a matrix.

**4. Notation: FIX (row labels)**

What passes:
- **Tone 5 means what IA2 says.** IA2 5.2 defines it as "shared… any object or term that lives on more than one surface". The unit's "a method serves any surface" applies that meaning. The unit names it at line 14 ("Tone 5, shared, carries the methods… because a method serves any surface") and again at 106.
- **Colour is not the only carrier.** Every row has the same tone, so colour tells no row from another. The caption and legend say it in words.

**Fault:** the row labels take more than half a 320 px phone. "Search-log analysis" is about 120 css px, and the cells start at about 176 of 320 css px, which leaves about 144 px. Only one column fits in view at a time, under the fade (see item 5). If the labels are shortened to the text's own words, the longest becomes "Usability test" (about 81 css px), and the cells gain about 40 px. Each short label traces to a line:
- "Open sort": 2.1, "An open sort shows…"
- "Closed sort": 2.1, "A closed sort shows…"
- "Hybrid sort": 2.1, "A hybrid sort shows…"
- "First click": 2.7, "first click for a screen"
- "Search logs": 1.1, "The methods read records of use: search logs, analytics paths and funnels"
- "Analytics": 2.5, "Product analytics record what people did"

The caption already uses these short forms ("first click", "search logs", "analytics").

**5. How the reader sees it: FIX at 320, 360 and 390; PASS at 430, tablet and desktop**

- **Desktop and tablet:** one frame each, dark and light (light on cream). The whole figure fits. All text is inside its boxes; the tightest cell, "can people do real tasks on the built thing, and why not", fits with small padding. Nothing overlaps, the legend is whole, and the caption sits under the figure. PASS.
- **430:** three frames. Every column is shown whole in some frame; in frame 1 the right edge of "Proves" sits under the fade and stays legible. PASS.
- **390:** "Proves" is never whole. Frame 1 cuts it at the right; frame 2 (scrolled 164) has the left part under the label column ("e groups", "ulation"). FIX.
- **360:** neither "Proves" nor "Does not prove" is whole in any of the four frames. FIX.
- **320:** none of "Answers", "Does not prove" or "Participants" is whole in any of the five frames. "Answers" loses its line ends at the edge ("put each item i[n]", "can people do re[al]"); the other two are cut on the left in frames 3 and 4. FIX.
- At 320 the "e" of "surface" at the end of the legend falls under the fade in frame 1 but is present and readable. I do not count that as a fault.
- At every width, light and dark: text is inside its boxes, nothing overlaps, and the caption is under the figure.

The sticky label column, the fade, the column widths (each as wide as its widest wrapped cell, from the 700-unit width) and the screenshot run's frame steps are the renderer's. My notes on cut columns rest on that layout. The fix the figure itself can make is the shorter row labels. The screenshot run needs repeating after the change. If a column still never shows whole at 320 or 360, the next fix is shorter cells, starting with the Usability "Answers" cell, which sets that column's width.

**Figure 1: FIX.** Each Current, in backticks, occurs once in the file named.

- **declaration.json, hybrid card sort cell (item 1).** Current: `"paper cards and blank headers"`. Replacement: `"a form with a free-text \"another group\" choice"`
- **declaration.json, row labels (items 4 and 5).**
  - `"Open card sort"` → `"Open sort"`
  - `"Closed card sort"` → `"Closed sort"`
  - `"Hybrid card sort"` → `"Hybrid sort"`
  - `"First-click test"` → `"First click"`
  - `"Search-log analysis"` → `"Search logs"`
  - `"Analytics paths"` → `"Analytics"`
- **Caption, in declaration.json and captions.md (item 2).** Current: `participant numbers from section 3.` Replacement: `participant numbers from section 3; cheapest forms from section 5.`
- **Unit text, line 106 (item 2).** Current: `say, and the participant numbers are section 3's.` Replacement: `say, the participant numbers section 3's and the cheapest forms section 5's.`

## Figure 4, second check (new agent, Opus 5.5, 10 November 2026), verbatim

Given only the unit's text with its figures taken out, the six captions, the figure's declaration, IA2, the figure kinds and the frames sheets `verify.py --shots` saved for it at every width, dark and light. Its hand-back, extracted by script from its transcript, is below; transcript checks: Read, Glob, Grep and Bash only, every path inside its folder, no web, memory, Projects, Artifact or `mcp__*` tool; model claude-opus-5-5 from its transcript.

**Maintainer:** Applied in part, verified against IA3, section 3.3: IA3 does not test its six items; it reasons about them and leaves where people look to IA11. So the caption's phrase became "for the six items of IA3, section 3.3" and section 4.3's sentence the same words, rather than the checker's longer list. The venue made the text's "CHI '19 Extended Abstracts". The renderer notes (the pinned label column and fade at 320 and 360 px) recorded, not applied. Re-checked by a new agent (third check).

Running as Opus 5.5 (claude-opus-5-5).

# IA11, figure 4 (section 4.3, card-sort similarity matrix): fresh figure check

The figure needs two fixes, both in the caption. The data and rendering are sound.

**1. Every label, cell, note, identifier and number traces to the text: FIX**

Cells. I recomputed every cell from the placements in section 4.3, line 183: "eight cards were placed in their home category by everyone; therapy session by 11, with one in Not sure; yoga class by 9 in Health and 3 in Learning; cookery course by 7 in Learning and 5 in Meals; bike helmet by 9 in Mobility, 2 in Health and 1 in Not sure."
- Gym membership and yoga class: 9/12 = 75. Train pass and bike helmet: 9/12 = 75. Coding course and cookery course: 7/12 = 58. All match line 189: "gym membership with yoga class at 75%, train pass with bike helmet at 75% … coding course with cookery course at 58%".
- Yoga class and coding course 25, yoga class and cookery course 17, bike helmet and gym membership 17, bike helmet and yoga class 17. These match line 185: "the 3 who placed yoga class in Learning put it with coding course (25%), and 2 of them had also placed cookery course in Learning (17%); the 2 who placed bike helmet in Health put it with gym membership (17%), and both had yoga class in Health too (17%)."
- The 0 cells follow from the home-only placements: "The other cells follow from who placed what".
- The matrix is symmetric. The diagonal is null, per line 185: "a card with itself is left blank". "decimals": 0 gives 17 and 58, as the text writes them.
- Bike helmet's cells against gym membership and train pass add to 92, which is consistent with "do not add to 100".

Labels.
- Rows and columns are the card texts in Deliverable C, C.2: "| C-01 | Gym membership |", "| C-02 | Yoga class |", "| C-04 | Coding course |", "| C-05 | Cookery course |", "| C-07 | Train pass |", "| C-08 | Bike helmet |".
- All six also appear in line 185.

Scale and units.
- "unit": "%", "min": 0, "max": 100: the text gives every cell as a percentage.
- "scale_label": "share of the 12 participants": line 179 has "each cell the share of the 12 participants".

Caption identifiers that trace:
- "the Perqo CS-1 pilot, 12 employees": section 4.1, "Perqo piloted … (CS-1) with 12 employees of the example client".
- "(M-06)": section 1.2, "M-06 | Pair similarity | … participants who placed two cards in the same group"; CS-A, "each cell the participants who placed both cards in one category divided by n".
- "a card in Not sure is in no group": line 185, the same words.
- "Supports reading a sort's clusters apart from the category labels": line 185, "reads the same sort without the category names", and line 189, "Read as clusters".
- "(section 4.3; Deliverable D, CS-A)": CS-A, "Then the similarity matrix M-06 for the cards in question".
- "Similarity matrix as used by Katsanos … Lantz": M-06, "the similarity matrix as in Katsanos and others 2019 and Lantz and others 2019".
- "Lantz and others, Journal of Classification, 2019": section 3.1, "*Journal of Classification* 36, no. 3, 2019".
- "Shaded in tone 3, the employee": line 185, "shaded in tone 3"; line 14, "Tone 3, the Perqo app and the employee".
- "no cell decides an IA change (section 6.3)": 6.3, item 2, "the Perqo pilot decides nothing in the IA".
- "Perqo and its pilot are fictional": "(Perqo, fictional)" throughout.

Faults:
- **"for the six items IA3 tested by reasoning (IA3, section 3.3)" is not in the text.** The text says only "Figure 4 draws it for IA3's six items" (line 185). It cites IA3, section 3.3 for the three far members (line 183: "The three far members IA3 named, and only those, were placed in a second category (IA3, section 3.3)"). "tested by reasoning" appears nowhere, and the text never ties "six items" to IA3, section 3.3. IA3 is not in my folder, so I could not check the claim against IA3 itself.
- **"CHI EA 2019" is not the text's form.** The text and Sources give "*CHI '19 Extended Abstracts*". The other captions in this unit use the text's own venue form, for example "HCII 2009".

**2. Caption: PASS once the item 1 fixes are made**
- It says what the figure shows: card-sort result, similarity matrix, what each cell is, the blank diagonal and the Not sure rule.
- It names the section it draws (4.3; Deliverable D, CS-A) and where the data comes from (the CS-1 pilot, M-06).
- Both sources it names, Katsanos and others 2019 and Lantz and others 2019, are cited in section 3.1 and in Sources.
- A note, not a fault: IA2, section 5.2 says a caption names "the decision it supports". This caption names a reading ("reading a sort's clusters"), not a decision. The text gives the matrix no decision, and M-06 is "never one cell at a time", so I am not asking for one. Writing one in would mean inventing it.

**3. Kind: PASS**
The data is pairs of cards with a numeric share where each pair meets. That is a square numeric matrix ("matrix" with "numeric": true). Compare, bars or another kind would lose the pairing.

**4. Notation: PASS**
- The one tone, 3, means what IA2, section 5.2 says: "Tone 3: the Perqo app and the employee". The unit's text names it (lines 14 and 185).
- Colour is not the only carrier: every cell prints its value, and the blank diagonal is marked by having no number. The caption names the tone's meaning.
- The row labels are 10 to 14 characters, the cards' own words, each in line 185 and in C.2.
- At 320 px the label column takes about 140 of the frame's CSS pixels and leaves one whole value column in view at a time. That is enough, and shortening the labels would break the card wording the rows and columns share.

**5. How the reader sees it: PASS**
I looked at desktop, tablet and phones at 320, 360, 390 and 430 px, in dark and light; the light theme is on cream.
- Desktop and tablet: the whole figure fits in one frame. All text sits inside its cells, nothing overlaps, the legend is whole, and the caption is under the figure.
- Phones: every column's cells appear whole in at least one frame, and each figure ends on a frame with the bike helmet column whole. The caption and the "scroll sideways for the whole figure" line are under the figure at every width.
- Light theme: the shading steps are distinct on cream.
- Dark theme: the blank diagonal cells (dark grey) are close in colour to the 0–20% cells. They are told apart by having no number, so this is not a fault.

These notes rest on how the renderer lays the figure out (the sticky label column with its fade, the frame scroll steps and the sticky section bar), not on the declaration:
- The "YOGA CLASS" header is cut in every sampled frame at 320 and 360 px: at the right edge in frame 1, under the label-column fade in frame 2. "TRAIN PASS" has its "T" under the fade at 320.
- The yoga class column's values at 320 are readable only through the fade (frame 2).
- The legend chip "60–80%" at 320 is partly faded in frame 3 and cut in frame 4.
- At 390 px the "80–100%" chip is partly under the fade in frame 3, but whole in frame 2.
- The opening frame at 320 is clipped by the sticky section bar, so the header row and the Gym membership row are hidden.

None of these can be fixed in the declaration without shortening the card wording.

**Figure 4: FIX.** Both replacements are in the caption string. Each Current occurs once in declaration.json and once in the unit's viz block; captions.md carries the same caption and changes with it.
- Current: `for the six items IA3 tested by reasoning (IA3, section 3.3)`. Replacement: `for IA3's six items, the three far members it named (IA3, section 3.3) and gym membership, coding course and train pass`. If IA3, section 3.3 really does test six items by reasoning, the alternative is to keep the caption and change line 185 instead: replace `Figure 4 draws it for IA3's six items, shaded in tone 3` with `Figure 4 draws it for the six items IA3 tested by reasoning (IA3, section 3.3), shaded in tone 3`.
- Current: `Katsanos and others, CHI EA 2019` (in the caption). Replacement: `Katsanos and others, CHI '19 Extended Abstracts`.

The phone-sheet crops I made for viewing are in /home/claude/agents/ia11-fig4-check2/out/.

## Figure 6, second check (new agent, Opus 5.5, 10 November 2026), verbatim

Given only the unit's text with its figures taken out, the six captions, the figure's declaration, IA2, the figure kinds and the frames sheets `verify.py --shots` saved for it at every width, dark and light. Its hand-back, extracted by script from its transcript, is below; transcript checks: Read, Glob, Grep and Bash only, every path inside its folder, no web, memory, Projects, Artifact or `mcp__*` tool; model claude-opus-5-5 from its transcript.

**Maintainer:** Applied as given, verified against section 6.4's table and section 2.4 (the search log is the Help centre's, on perqo.com): the C3 and C5 cells restored to the table's words; tone 3 named as the employee in the legend, the caption and section 6.4's sentence (shortened from the checker's wording); the rung names moved into a Rung column so the row labels are the identifiers. Re-checked by a new agent (third check).

I ran this check as Opus 5.5 (claude-opus-5-5). It is a fresh check of IA11, figure 6 (the confidence-ladder matrix, section 6.4). I worked only inside /home/claude/agents/ia11-fig6-check2. My only writes were the phone frame-sheet slices in out/ and a full replacement declaration, /home/claude/agents/ia11-fig6-check2/out/fig6-replacement.json, which parses and has every row's cells matching the columns.

**1. Every label, cell and number traces to the text: FIX**
The source is the table under section 6.4, lines 259–266 of unit-without-figures.md.
- **Columns.** "Evidence", "Can decide", "Cannot decide" and "At Perqo" match the header row `| Rung | Evidence | Can decide | Cannot decide | At Perqo (Perqo, fictional) |`.
- **C0 row.** Matches `| C0 Assumed | reasoning at a desk, from the literature and the domain | a labelled default, marked "assumed" (IA2, section 5.2) | anything a person would do | IA6's task frequencies (IA6, Deliverable A) |`. The shortenings are faithful.
- **C1 row.** Matches `| C1 Signal | a log, ticket tags or paths, read once | what to test next (IA9, section 6.4) | why, or the fix | the zero results for "gym" (IA3, section 5.2) |` exactly.
- **C2 row.** Matches `| C2 Observed | a small test with people: a usability round, a pilot, a moderated tree test | that a problem exists, and its cause (section 2.6) | a rate, or a pass (section 3.4) | the TT-1 pilot, 12 employees |`. Only the examples are dropped.
- **C3 row: fault.** The text has `| C3 Measured | a planned test from the right people, its interval clear of a mark set beforehand | ...`. The figure drops "from the right people", which is the condition section 6.3 reason 2 rests on ("twelve employees of one client are a convenience sample of one profile ... the Perqo pilot decides nothing in the IA even where its intervals are clear"). Without it, the cell would let the pilot's clear sort result count as C3. The other three C3 cells match.
- **C4 row.** Matches `| C4 Converging | two methods of different kinds that agree | a change to a tab or a top level (IA9, RV-11) | how it performs in use | TT-1 with CS-1 on a cross-listing; FC-1 with ticket tags |`.
- **C5 row: fault.** The text has `| C5 Confirmed in use | ... | closing the DL entry as applied and confirmed | why it worked | AN-1 one quarter after release |`. The figure's "closing the DL entry" drops "as applied and confirmed". That makes the cell wrong: section 6.1 already closes a DL entry "as declined, with the test as its reason" on a pass, which is C3.
- **Legend, tone 5.** "shared: the rungs serve any surface" traces to line 14: "Tone 5, shared, carries the methods and the confidence ladder, because a method serves any surface."
- **Legend, tone 3.** "the Perqo app" traces to line 268: "the Perqo column in tone 3, the app". That line has the tone fault described under item 4.
- **Identifiers.** C0 to C5 trace to line 257: "IA12 and DD-IA2 cite rungs by identifier, C0 to C5." TT-1, CS-1, FC-1, AN-1 and DL also appear in the text.

**2. Caption: PASS**
- It names the artefact, what the figure shows, the decision it supports and section 6.4, and says Perqo is fictional.
- Every source it names is cited in the text and listed in Sources: Nielsen 2000, Lewis and Sauro 2006, Laubheimer 2024, and Rosenfeld 2011 (line 37, "after Rosenfeld ... IA3, section 5.2").
- The internal references are cited too: IA2 5.2, IA9 6.4, IA9 6.3 (in M-08), IA9 RV-11, and sections 3.4 and 6.3.
- Its last sentence repeats the tone 3 wording, "the app", which is fixed under item 4.

**3. Kind: PASS**
The figure shows items (rungs) against dimensions (evidence, can decide, cannot decide, Perqo example), which is the shape a matrix is for. The order C0 to C5 carries the ladder.

**4. Notation: FIX**
- **Tone 5.** Correct for shared, and named at lines 14 and 268.
- **Tone 3: fault.** The figure draws tone 3 and labels it "the Perqo app". But the C1 example, "the zero results for 'gym'", is not app evidence. Line 90 says "At Perqo the log is the Help centre's, on perqo.com; the app has no search", and V-13 and LG-1 name it the For employees log. IA2's tone 3 is "the Perqo app and the employee". Every Perqo example in the column is evidence about employees, so the meaning to cite is the employee, not the app.
- **Colour.** It is not the only carrier: the column is headed "At Perqo" and the legend states each tone's meaning in words.
- **Row labels: fault.** "C0 Assumed" to "C5 Confirmed in use" trace to the text, but they are too long for a phone. The fixed label column takes about 180 of the frame's 290 px at 320, which leaves the cells a window of about 120 px (see item 5).

**5. How the reader sees it: FIX**
- **Desktop and tablet, dark and light: PASS.** One frame shows the whole figure. Text sits inside its boxes, nothing overlaps, and the caption is under the figure. The light theme reads on cream.
- **Phone 430: PASS.** Every column is whole in one of the three frames, and so is each legend item.
- **Phone 390.** Cannot decide is cut in both frames that show it: frame 2 at the right edge, frame 3 at the left ("thing a", "n would do"). No frame shows it whole.
- **Phone 360.** Evidence is cut at the right in frame 1 ("reasoning at a desk" ends in "des", and "a small test with peo") and is gone by frame 2. No frame shows it whole.
- **Phone 320.** No cell of any column is shown whole in any of the five frames. Each frame shows a sliver about 120 px wide between fades. The legend item "the Perqo app" is never whole either ("the Perq", "the Perqo ap", "› app").
- **Dark versions** have the same layout and read fine. The captions are under the figure at every width.
- **Renderer-dependent notes.** The fixed label column and its fade are the renderer's known behaviour, not a fault. What the figure controls is the label width: the column is as wide as the longest label, "C5 Confirmed in use". My estimate is that with labels of two characters the column falls to about 75 px, and the window at 320 grows to about 225 px. The widest cell, Evidence, is about 195 px at 430, so every column should then fit whole in some frame. That estimate rests on how the renderer sizes the label column, which figure-kinds.md does not document for matrix.

**Replacements**
Each Current occurs once in declaration.json, or in unit-without-figures.md for the last one.
- Columns: `"cols": ["Evidence"` becomes `"cols": ["Rung", "Evidence"`
- Row C0: `"label": "C0 Assumed", "tone": 5, "cells": [` becomes `"label": "C0", "tone": 5, "cells": ["Assumed", `
- Row C1: `"label": "C1 Signal", "tone": 5, "cells": [` becomes `"label": "C1", "tone": 5, "cells": ["Signal", `
- Row C2: `"label": "C2 Observed", "tone": 5, "cells": [` becomes `"label": "C2", "tone": 5, "cells": ["Observed", `
- Row C3: `"label": "C3 Measured", "tone": 5, "cells": [` becomes `"label": "C3", "tone": 5, "cells": ["Measured", `
- Row C4: `"label": "C4 Converging", "tone": 5, "cells": [` becomes `"label": "C4", "tone": 5, "cells": ["Converging", `
- Row C5: `"label": "C5 Confirmed in use", "tone": 5, "cells": [` becomes `"label": "C5", "tone": 5, "cells": ["Confirmed in use", `
  - "Rung" traces to the text table's header. Each name traces to its row in that table.
- C3 Evidence cell: `"a planned test, its interval clear of a mark set beforehand"` becomes `"a planned test from the right people, its interval clear of a mark set beforehand"`
- C5 Can decide cell: `"closing the DL entry"` becomes `"closing the DL entry as applied and confirmed"`
- Tone 3 legend: `"means": "the Perqo app"` becomes `"means": "the employee: every Perqo example"`
- Caption: `the Perqo column tone 3, the app.` becomes `the Perqo column tone 3, the employee, since every example is evidence about employees, the perqo.com Help centre's search log included (section 2.4).`
- Unit text, line 268: `the Perqo column in tone 3, the app.` becomes `the Perqo column in tone 3, the employee: every example is evidence about employees, the Help centre's search log on perqo.com included (section 2.4).`

The full corrected declaration with all the declaration changes applied is /home/claude/agents/ia11-fig6-check2/out/fig6-replacement.json.

Nothing new for memory.

Figure 6: FIX. Restore the dropped qualifiers in the C3 Evidence and C5 Can decide cells, recast tone 3 as the employee, and move the rung names into a Rung column so the row labels are only the identifiers.

## Figure 1, third check (new agent, Opus 5.5, 10 November 2026), verbatim

Given only the unit's text with its figures taken out, the six captions, the figure's declaration, IA2, the figure kinds and the frames sheets of the filed build (page read-ia11). Its hand-back, extracted by script from its transcript, is below; transcript checks: Read, Glob, Grep and Bash only, every path inside its folder, no web, memory, Projects, Artifact or `mcp__*` tool; model claude-opus-5-5 from its transcript.

**Maintainer:** Applied as given, verified against section 3.1 (the closed sort's 50 is the Perqo plan's, which the second check's cell put there): the caption's last sentence. Its renderer note (the screenshot run steps sideways by a fixed distance, so at 320 to 390 px some columns are cut in every sampled frame while a reader scrolling freely can stop on each whole) rests on the renderer and the screenshot run, and is recorded, not applied. The drawing is unchanged, so the fourth check reads the same frames sheets with the new caption.

Running as Opus 5.5 (claude-opus-5-5). This was a fresh check of IA11, figure 1 (the section 2.7 method-selection matrix). I worked only inside /home/claude/agents/ia11-fig1-check3 and wrote crops and montages only to out/. I used no memory, Projects, connector, web or Artifact tool.

**Result: FIX.** One fault, in the caption: it says "no Perqo fact is drawn", but one cell draws a Perqo fact. Everything else passes. The phone frames sheets also show a problem that comes from the renderer, not from this figure (item 5).

## 1. Every label, cell and number traces to the text: PASS

**Columns:**
- "Answers": l.31 "A test answers one question about one part of the structure".
- "Proves" and "Does not prove": l.57 "The methods, and what each does and does not prove".
- "Participants" and "Cheapest form": l.106 "the participant numbers section 3's and the cheapest forms section 5's".

**Row labels:**
- Open sort, Closed sort, Hybrid sort: l.67–69 "An open sort… A closed sort… A hybrid sort".
- Tree test: l.72 "Tree testing".
- First click: l.80 "First-click testing".
- Search logs: l.37 "search logs, analytics paths and funnels".
- Analytics: l.92 "Analytics paths and funnels".
- Usability test: l.100 "A usability test gives a participant realistic tasks".

**Open sort:**
- "how people group and name the content": l.35 "How do people group and name these things?… open and hybrid card sorts".
- "the groups and names a population makes": l.67 "shows how a group of people clusters the content and what they call the clusters".
- "that a structure built on them is findable": l.67 "It does not show that a structure built from those clusters can be navigated".
- "15 to 30": l.122 "15 to 30 participants give a similarity matrix".
- "paper cards and a spreadsheet": l.214–215 "Paper cards and category headers… in a spreadsheet" and "Open card sort. The same, with blank headers".

**Closed sort:**
- "which given category people put each item in": l.68 "whether people put each item where an existing scheme puts it"; l.61 "sort items into previously defined category names".
- "agreement with an existing scheme": l.68 "It measures agreement with a scheme the team chose".
- "a better scheme nobody offered": l.68 "it cannot show a better scheme the team did not offer".
- "50 in the Perqo plan; about 193 for a 7% margin": l.122 "to have a margin of error of around 7% you should plan on having around 193 participants" and "the Perqo plan gives CS-1 50 participants".
- "a form with one choice per card": l.214 "a form with one question per card and the categories as its choices". This is a fair short form.

**Hybrid sort:**
- "whether a given scheme has gaps": l.69 "Those added groups are the gaps in the scheme".
- "the groups people add to it": l.69 "plus the groups people add when the given ones do not fit".
- "that the added groups are findable": l.69 "they are not yet a tested part of it".
- "as an open sort": l.122 "this unit gives it the open sort's numbers".
- "a form with a free-text 'another group' choice": l.214 "plus a free-text "another group" choice (hybrid)".

**Tree test:**
- "can people find items in this hierarchy": l.36 "Can people find things in this structure?"; l.74 "find the locations in the tree".
- "findability of labels and grouping": l.78 "whether the labels and the grouping of a hierarchy lead people to an item".
- "visual design, content, search": l.78 "No visual design, no content on the page, no search".
- "50 or more per tree": l.128 "50+ participants per tree"; l.132 "Fifty participants per tree".
- "index cards, moderated": l.216 "On index cards, moderated".

**First click:**
- "is the first move on this screen right": l.82 "records where they tap or click first… if the user's first click was correct".
- "where people start on a real layout": l.84, the same words.
- "that the task is completed": l.84, the same words.
- "as a tree test": l.136 "the Perqo plan gives it the tree test's 50".
- "a screen image on a video call": l.217 "A screen image shown on a video call".

**Search logs:**
- "what people ask for, in their words": l.90 "what people who searched asked for, in their words".
- "demand and failed searches": l.90 "and which searches failed".
- "why, or what non-searchers did": l.90 "why they searched, what the people who did not search did".
- "none: the log": l.37 "The methods read records of use: search logs".
- "an exported log and a spreadsheet": l.218 "An export of the queries for one period"; l.212 "a form and a spreadsheet".

**Analytics:**
- "what people did in production": l.94 "Product analytics record what people did"; l.37 "Asked after release".
- "frequencies, paths and drop-offs at scale": l.96 "frequencies, paths and drop-offs, measured on everyone".
- "intent": l.96 "What it does not: intent."
- "none: the records": l.96 "with no recruiting".
- "screen views by identifier": l.219 "The screen views by identifier, per session".

**Usability test:**
- "can people do real tasks on the built thing, and why not": l.102 "whether real tasks succeed on the whole system… and why they fail".
- "problems and their causes": l.136 "which problems exist and why".
- "a stable rate at five": l.102 "What it does not prove at five participants is a rate".
- "5 per round, several rounds": l.100 "three rounds of five"; l.220 "five participants a round".
- "a video call and a prototype": l.220 "A video call… a prototype or the built app".

**Legend, "tone 5: shared: a method serves any surface"**: l.106 "Every row is tone 5, since a method serves any surface"; l.14 "Tone 5, shared, carries the methods".

## 2. The caption: FIX

The caption says what the figure shows, the decision it supports and the section (2.7; Deliverable A). Every source it names is cited in the text:
- Nielsen 2004: l.35
- Sauro 2012: l.61
- dscout: l.61
- Tankala 2024 through IA3: l.70
- Laubheimer 2023: l.74; Laubheimer 2024: l.128
- Boxes and Arrows: l.76
- Bailey 2009: l.82
- Rosenfeld 2011: l.88
- Farrell 2017 through IA3: l.88
- Cardello 2013 through IA9: l.94
- Nielsen 2000 and Krug 2014: l.100

Tankala (terminology) and Krug feed no cell. They are cited in sections 2.1 and 2.6, and IA2's caption rule asks for "the sources cited there", so naming them is in order.

**The fault:** the caption ends "Perqo is fictional; no Perqo fact is drawn." The closed-sort cell draws one: "50 in the Perqo plan" (l.122, "the Perqo plan gives CS-1 50 participants").

## 3. The kind fits the data: PASS

Eight items (the methods) against five dimensions is "items by sections", so a matrix is the right kind.

## 4. The notation is IA2's: PASS

- IA2 defines tone 5 as "shared: … any object or term that lives on more than one surface" (IA2 §5.2). Reading a method as shared because it serves any surface is the unit's own use of that meaning. It is stated in the text (l.14, l.106), the legend and the caption.
- All rows carry the one tone, so colour distinguishes nothing. The meaning is carried in words.
- Row labels are at most 14 characters ("Usability test"). At 320 px the label column leaves the cell window about 170 css px, and each label traces to its section heading, quoted above.

## 5. How the reader sees it: PASS for the figure, with a renderer note

**Desktop and tablet, dark and light:**
- Each is one frame with the whole figure.
- Text sits inside its cells, nothing overlaps, and the legend and caption sit under the figure.
- Light theme on cream: the lavender cells and dark text read cleanly.

**Phones, 320, 360, 390 and 430 px, dark and light:**
- No text overflows a cell and nothing overlaps.
- The caption is under the figure and "scroll sideways for the whole figure" shows.
- The 430 opening frame is clipped by the sticky section bar. That is known behaviour.

**Renderer note, resting on how the renderer lays the figure out:** the frames step sideways by a fixed distance (129, 149, 164 and 184 px), not column by column. Combined with the sticky label column and its fade, some columns are cut in every frame of a sheet:
- **320:** Participants is cut at the right in frame 3. In frame 4 its first words ("50", "5", "as") sit under the label column and cannot be read.
- **360:** Proves and Does not prove are each cut at one edge or the other in every frame.
- **390:** Proves is cut at the right in frame 1 and its first characters are under the fade in frame 2.
- **The legend line:** "surface" fades at the right edge at 320 but stays legible.

Every column fits inside the visible cell window, so a reader scrolling freely can stop on each column whole. The fault is in how the screenshot run samples the scroll, not in the declaration, and no change to the figure's JSON fixes it. To clear the check, the screenshot run should add a frame at each column's left edge, or the renderer should snap scrolling to columns. 430, desktop and tablet show every column whole.

**Figure 1: FIX.** One replacement, in the caption (declaration.json "caption"; the same text in captions.md, Figure 1):

Current: `Perqo is fictional; no Perqo fact is drawn.`
Replacement: `The closed sort's 50 is the Perqo plan's (section 3.1); Perqo is fictional.`

## Figure 4, third check (new agent, Opus 5.5, 10 November 2026), verbatim

Given only the unit's text with its figures taken out, the six captions, the figure's declaration, IA2, the figure kinds and the frames sheets of the filed build (page read-ia11). Its hand-back, extracted by script from its transcript, is below; transcript checks: Read, Glob, Grep and Bash only, every path inside its folder, no web, memory, Projects, Artifact or `mcp__*` tool; model claude-opus-5-5 from its transcript.

**Maintainer:** PASS. Its notes on the YOGA CLASS and TRAIN PASS headers at 320 and 360 px rest on the pinned label column, its fade and the run's fixed scroll steps; recorded, not applied.

Running as Opus 5.5 (claude-opus-5-5). This is a fresh check: I had not seen the unit's writing, the writer's report or any earlier check. I used only my folder, and wrote crops and montages only to out/. I used no memory, project, connector, web or Artifact tool.

**Verdict: figure 4 passes on all five items.** The figure needs no replacement JSON, caption or text.

## 1. Every element traces to the text: PASS
I recomputed all 30 off-diagonal cells from the placements in the text, with n = 12. All of them match and the matrix is symmetric.

**Placements the cells come from**
- Line 183: "eight cards were placed in their home category by everyone; therapy session by 11, with one in Not sure; yoga class by 9 in Health and 3 in Learning; cookery course by 7 in Learning and 5 in Meals; bike helmet by 9 in Mobility, 2 in Health and 1 in Not sure."
- Deliverable C, C.2 gives the home categories: gym membership in Health, coding course in Learning, train pass in Mobility. So those three cards were placed 12 of 12 in their homes.

**Row and column labels (the six cards, in the card text of C.2)**
- `Gym membership`: "| C-01 | Gym membership | BI-001 | Health | none |"
- `Yoga class`: "| C-02 | Yoga class | BI-002 | Health | Learning |"
- `Coding course`: "| C-04 | Coding course | BI-004 | Learning | none |"
- `Cookery course`: "| C-05 | Cookery course | BI-005 | Learning | Meals |"
- `Train pass`: "| C-07 | Train pass | BI-007 | Mobility | none |"
- `Bike helmet`: "| C-08 | Bike helmet | BI-008 | Mobility | Health |"

**Cells**
- Gym membership with yoga class, 75 (9 of 12), and train pass with bike helmet, 75 (9 of 12): "two firm pairs (gym membership with yoga class at 75%, train pass with bike helmet at 75%)" (line 189).
- Coding course with cookery course, 58 (7 of 12 is 58.3): "one loose one (coding course with cookery course at 58%)" (line 189).
- Yoga class with coding course, 25: "the 3 who placed yoga class in Learning put it with coding course (25%)" (line 185).
- Yoga class with cookery course, 17: "and 2 of them had also placed cookery course in Learning (17%)" (line 185).
- Bike helmet with gym membership, 17: "the 2 who placed bike helmet in Health put it with gym membership (17%)" (line 185).
- Bike helmet with yoga class, 17: "and both had yoga class in Health too (17%)" (line 185).
- The 0 cells: "The other cells follow from who placed what (Perqo, fictional)" (line 185). Every zero pairs cards that never shared a category in the placements above.
- The blank diagonal (`null`): "a card with itself is left blank" (line 185).
- Bike helmet's row: 17 plus 75 is 92, matching "a card in Not sure is in no group, which is why bike helmet's cells against gym membership and train pass do not add to 100" (line 185).

**Other keys**
- `numeric`, `min` 0, `max` 100, `unit` %, `decimals` 0: the M-06 definition reads "in any sort, participants who placed two cards in the same group, divided by participants who sorted both" (line 50). The whole numbers match the rounding used in the text (58%, 17%).
- `scale_label` "share of the 12 participants": "for each pair of cards, the share of participants who put both in one group" (line 185), and "Perqo piloted ... (CS-1) with 12 employees" (section 4.1).
- `tone` 3: "Figure 4 draws it for the six items of IA3, section 3.3, shaded in tone 3" (line 185).
- Identifiers. M-06 is in line 50 and line 185. CS-1 is in section 4.1 and Deliverable C. CS-A is "### CS-A · Closed card sort" (Deliverable D). Sections 4.3 and 6.3 exist ("### 4.3 · Agreement: placement and similarity", "### 6.3 · Six reasons a result is too weak to act on").
- "the six items of IA3, section 3.3" matches line 185 word for word. IA3 is not in my folder, so I could not check that reference against IA3 itself.
- Every key is a documented matrix key in VIZ_KEYS.

## 2. Caption: PASS
- **What it shows:** "Card-sort result, similarity matrix ... each cell the share who placed both cards in one category (M-06)", plus the diagonal and Not-sure conventions.
- **Section:** "section 4.3; Deliverable D, CS-A".
- **Where the data comes from:** the Perqo CS-1 pilot, 12 employees, flagged "Perqo and its pilot are fictional", as the text does in "(Perqo, fictional)".
- **Method sources:** Katsanos and others (CHI '19 Extended Abstracts) and Lantz and others (Journal of Classification, 2019). Both are cited in section 3.1, in the M-06 row (line 50) and in the references (lines 606 and 608).
- **"no cell decides an IA change (section 6.3)":** this matches section 6.3, "This is why the Perqo pilot decides nothing in the IA" (line 249), and section 4.1, "the rule of section 6.3 that a pilot's numbers do not change the IA".
- **"Shaded in tone 3, the employee":** this matches IA2 and the text's wording for figure 3 (line 179).

## 3. Kind fits the data: PASS
The data is items crossed with items, one number in each cell. That is the matrix kind with `numeric: true`, which is the standard form of a card-sort similarity matrix.

## 4. Notation: PASS
- **Tone:** the one tone used, tone 3, means "the Perqo app and the employee" in IA2, section 5.2. The unit names it in the text ("shaded in tone 3", line 185) and in the caption.
- **Colour is not the only carrier:** every cell prints its value, the legend gives each step's range, and the caption explains the blank diagonal. The 0 cells and 17 cells share the 0–20% shade, so the printed number tells them apart.
- **Row labels:** each is the card text of C.2, two words and at most 14 characters, each traced in item 1. At 320 px they leave about 137 CSS px for cells, more than one whole column of about 99 px. Shortening them would break the card wording that section 4.3 sets for the sort's figures ("one row per card in the card's own words", line 179).

## 5. How the reader sees it: PASS
I checked desktop, tablet and phone at 320, 360, 390 and 430 px, in dark and in light. I judged the light theme on its cream ground.

**Whole at every width and theme:**
- Every cell's text sits inside its box.
- Nothing overlaps.
- The caption sits under the figure and the legend.
- The "scroll sideways for the whole figure" hint shows on phones.
- The blank diagonal reads as a distinct neutral cell in both themes.
- Contrast holds on dark and on cream.

**Desktop and tablet:** each shows the figure whole in one frame.

**Phone 390 and 430:** each header, column of cells and legend chip appears whole in at least one frame.

**Phone 320 and 360** (these notes rest on how the renderer lays the figure out, not on the figure):
- At 320, no frame shows the "YOGA CLASS" header whole. Frame 1 cuts it at the right edge, and in frame 2 it sits under the fade of the sticky label column. The same happens to "TRAIN PASS" (frame 4) and the "60–80%" legend chip (frame 3).
- At 360, the "YOGA CLASS" header is likewise never wholly clear.
- Every cell value in those columns is still legible in some frame, dimmed in places by the fade.
- These gaps come from where the screenshot run stops the sideways scroll, plus the sticky-column fade. A reader scrolling freely can bring each of these columns fully into view, because the window (about 137 CSS px at 320) is wider than one column (about 99 px).

**Opening frame:** at 320 and 360 the top of the figure is clipped by the sticky section bar. This is the known renderer behaviour for a figure taller than the screen, also a layout note.

**Memory:** I used nothing from memory, and I have nothing new to propose saving.

Figure 4: PASS.

## Figure 6, third check (new agent, Opus 5.5, 10 November 2026), verbatim

Given only the unit's text with its figures taken out, the six captions, the figure's declaration, IA2, the figure kinds and the frames sheets of the filed build (page read-ia11). Its hand-back, extracted by script from its transcript, is below; transcript checks: Read, Glob, Grep and Bash only, every path inside its folder, no web, memory, Projects, Artifact or `mcp__*` tool; model claude-opus-5-5 from its transcript.

**Maintainer:** Applied in part, verified against section 6.4, A.2 and IA2, section 5.2: the legend note's reason added to section 6.4's sentence ("since the rungs serve any surface"), without the checker's parenthesis on A.2, which the sentence does not need. A correction to the text a figure draws reopens it: fourth check by a new agent on the same frames sheets (the declaration is unchanged).

Running as Opus 5.5 (claude-opus-5-5). I worked only inside /home/claude/agents/ia11-fig6-check3; the only files I wrote are image crops in out/crops/.

**Figure 6 (IA11, section 6.4, the confidence ladder, a matrix): FIX.** There is one fault: one legend note does not trace to the unit's text. Everything else passes.

**1. Trace to text: FIX (one item)**
- **Columns.** "Rung", "Evidence", "Can decide", "Cannot decide", "At Perqo" come from the table header at line 259: `| Rung | Evidence | Can decide | Cannot decide | At Perqo (Perqo, fictional) |`.
- **Row labels C0 to C5.** Line 257: "IA12 and DD-IA2 cite rungs by identifier, C0 to C5."
- **Row C0 (line 261):** "| C0 Assumed | reasoning at a desk, from the literature and the domain | a labelled default, marked "assumed" (IA2, section 5.2) | anything a person would do | IA6's task frequencies (IA6, Deliverable A) |". The cells "Assumed", "reasoning at a desk", "a labelled default", "anything a person would do" and "IA6's task frequencies" are all there, two of them as leading short forms.
- **Row C1 (line 262):** "| C1 Signal | a log, ticket tags or paths, read once | what to test next (IA9, section 6.4) | why, or the fix | the zero results for "gym" (IA3, section 5.2) |". Every cell matches. The figure writes 'gym' in single quotes where the text uses double; the captions do the same with ('assumed'), so this is a quoting convention, not a fault.
- **Row C2 (line 263):** "| C2 Observed | a small test with people: a usability round, a pilot, a moderated tree test | that a problem exists, and its cause (section 2.6) | a rate, or a pass (section 3.4) | the TT-1 pilot, 12 employees |". Every cell matches, "a small test with people" as a leading short form.
- **Row C3 (line 264):** "| C3 Measured | a planned test from the right people, its interval clear of a mark set beforehand | a label, a placement, a cross-listing | a top level on one method alone | TT-1 and CS-1 at 50 (planned) |". Exact.
- **Row C4 (line 265):** "| C4 Converging | two methods of different kinds that agree | a change to a tab or a top level (IA9, RV-11) | how it performs in use | TT-1 with CS-1 on a cross-listing; FC-1 with ticket tags |". Exact.
- **Row C5 (line 266):** "| C5 Confirmed in use | production records of the behaviour itself, or before and after a release | closing the DL entry as applied and confirmed | why it worked | AN-1 one quarter after release |". Exact.
- **Numbers.** "12" (line 263) and "50" (line 264) both trace.
- **Legend, tone 3, "the employee: every Perqo example".** Line 268: "the Perqo column in tone 3, the employee, since every example is evidence about employees".
- **Legend, tone 5, "shared: the rungs serve any surface": FIX.** No sentence says this. Line 14 gives a different reason: "Tone 5, shared, carries the methods and the confidence ladder, because a method serves any surface." Line 268 says only "rows in tone 5, shared". The claim itself holds, since table A.2 holds Admin assumptions at C1 (rows 6 and 9), but the text never says it. The fix below adds it to the text.

**2. Caption: PASS**
- The caption says what the figure shows (six rungs, what each can and cannot decide, a Perqo example), names the decision it supports and the section (6.4), and says "Perqo is fictional".
- Every source it names is cited in the text:
  - IA2, section 5.2: line 261.
  - IA9, section 6.4: line 262.
  - Rosenfeld through IA3, section 5.2: line 37, "after Rosenfeld: each record says what happened and never why … (IA9, section 6; IA3, section 5.2, after Mausser…)".
  - Nielsen, NN/g, 2000: section 2.6.
  - Section 3.4: line 263.
  - Lewis and Sauro, Journal of Usability Studies, 2006: section 3.4.
  - Laubheimer, NN/g, 2024: section 3.2.
  - Section 6.3: lines 246 to 253.
  - IA9, RV-11: line 265.
  - IA9, section 6.3: line 94.
- The tone statement matches line 268.
- The caption in captions.md and the one in the declaration are identical.
- Minor, not a fault: the text's C3 and C5 rows cite nothing, so their sources rest on the caption alone. Those sources are all cited elsewhere in the text.

**3. Kind: PASS**
The figure is six items (rungs) against five dimensions, which is a matrix. Its keys are all valid matrix keys in VIZ_KEYS (cols, rows with label, tone and cells, cell mark and tone, legend).

**4. Notation: PASS**
- Tone 5 means "shared … any object or term on more than one surface" (IA2, line 206, and the notation sheet). The rungs are terms used on the app, Admin and the register, and the unit names the tone at lines 14 and 268.
- Tone 3 means "the Perqo app and the employee". The unit names it at line 268 and justifies applying it to C1's perqo.com Help-centre search log: the example is evidence about employees.
- Colour is not the only carrier of meaning. The legend states both meanings in words, the caption repeats them, and the column header "At Perqo" marks the tone 3 column.
- Row labels are two characters each and trace to line 257.

**5. How the reader sees it: PASS**
- **Desktop and tablet, dark and light.** One frame holds the whole figure. Every text sits inside its box, nothing overlaps, and the caption sits under the figure. On light, the cells sit correctly on the cream paper.
- **Phone 320 (4 frames), 360, 390 and 430 (3 frames each), dark and light.** Every cell, header and caption is shown whole in at least one frame, and the drawing is whole across the frames:
  - The tone 5 legend swatch and note are whole in frame 1.
  - The tone 3 swatch is whole in an earlier frame, and its note "the employee: every Perqo example" is whole in the last frame.
- Nothing overlaps at any width, and the caption is under the figure every time.

**What rests on the renderer:**
- The label column stays in view with a fade while the cells scroll.
- The fade lies across parts of the legend text as the legend scrolls past the label column (for example "e|very" in the last frame at 320). The text stays legible.
- The label column takes about 40% of the 320 px frame although the labels are two characters wide. The renderer sets that width, not the figure.
- The opening frames at every phone width are clipped by the sticky section bar.
- The matrix draws at its own width on desktop and tablet.

**Replacement (one fault):**
- Current: `Figure 6 draws the ladder, rows in tone 5, shared, and the Perqo column in tone 3, the employee,`
- Replacement: `Figure 6 draws the ladder, rows in tone 5, shared, since the rungs serve any surface (table A.2 holds Admin's assumptions at C1), and the Perqo column in tone 3, the employee,`

figure 6, FIX: replace `Figure 6 draws the ladder, rows in tone 5, shared, and the Perqo column in tone 3, the employee,` (unit text, line 268) with `Figure 6 draws the ladder, rows in tone 5, shared, since the rungs serve any surface (table A.2 holds Admin's assumptions at C1), and the Perqo column in tone 3, the employee,`

## Figure 6, fourth check (new agent, Opus 5.5, 10 November 2026), verbatim

Given only the unit's text with its figures taken out, the six captions, the figure's declaration, IA2, the figure kinds and the frames sheets of the filed build (the drawing unchanged since). Its hand-back, extracted by script from its transcript, is below; transcript checks: Read, Glob, Grep and Bash only, every path inside its folder, no web, memory, Projects, Artifact or `mcp__*` tool; model claude-opus-5-5 from its transcript.

**Maintainer:** Applied as given, verified against IA6, Deliverable A, IA3, section 5.2, section 4.1 and plan rows V-01, V-05 and V-15: the caption's verb and the sources of the Perqo column. Its renderer notes (the label column's width, the narrow Evidence column, the fade over the legend at 320 and 360 px) recorded, not applied. Fifth check by a new agent.

Running as Opus 5.5 (claude-opus-5-5).

Fresh check of IA11, figure 6 (matrix, section 6.4, the confidence ladder). I used only the files in /home/claude/agents/ia11-fig6-check4. The only things I wrote are crops in out/.

**1. Declaration traces to the text: PASS**
Every row, cell and Perqo mark comes from the table in section 6.4 (unit lines 259 to 266). Some cells are shortened from the text but say nothing it does not.
- Columns: "| Rung | Evidence | Can decide | Cannot decide | At Perqo (Perqo, fictional) |" (l.259).
- Row labels: "IA12 and DD-IA2 cite rungs by identifier, C0 to C5" (l.257).
- C0: "| C0 Assumed | reasoning at a desk, from the literature and the domain | a labelled default, marked "assumed" (IA2, section 5.2) | anything a person would do | IA6's task frequencies (IA6, Deliverable A) |" (l.261).
- C1: "| C1 Signal | a log, ticket tags or paths, read once | what to test next (IA9, section 6.4) | why, or the fix | the zero results for "gym" (IA3, section 5.2) |" (l.262).
- C2: "| C2 Observed | a small test with people: a usability round, a pilot, a moderated tree test | that a problem exists, and its cause (section 2.6) | a rate, or a pass (section 3.4) | the TT-1 pilot, 12 employees |" (l.263).
- C3: "| C3 Measured | a planned test from the right people, its interval clear of a mark set beforehand | a label, a placement, a cross-listing | a top level on one method alone | TT-1 and CS-1 at 50 (planned) |" (l.264).
- C4: "| C4 Converging | two methods of different kinds that agree | a change to a tab or a top level (IA9, RV-11) | how it performs in use | TT-1 with CS-1 on a cross-listing; FC-1 with ticket tags |" (l.265).
- C5: "| C5 Confirmed in use | production records of the behaviour itself, or before and after a release | closing the DL entry as applied and confirmed | why it worked | AN-1 one quarter after release |" (l.266).
- Both legend items: "Figure 6 draws the ladder, rows in tone 5, shared, since the rungs serve any surface, and the Perqo column in tone 3, the employee, since every example is evidence about employees" (l.268).
- The examples also trace further into the unit: "TT-1 and CS-1 … 50 employees" (Deliverable A, l.312); V-05 "TT-1, tasks T3 to T5; CS-1 | the same 50 … C4 when both agree" (l.296); V-15 "TK-1's most-tagged A- screens … set beside FC-1's results" (l.306); V-01 "AN-1 … one quarter after release" (l.292).
- One note, not an error: under the declaration's form, "Rung" heads the name column (Assumed…), and C0 to C5 sit in the unheaded label column.

**2. Caption: FIX**
- What is right: the caption says what the figure shows and names section 6.4. Every source it names is cited in the text:
  - IA2, section 5.2 (l.261).
  - IA9, section 6.4 (l.262).
  - Rosenfeld through IA3, section 5.2 (l.37: "after Rosenfeld … IA3, section 5.2"; Sources l.616).
  - Nielsen, NN/g, 2000 (section 2.6; Sources).
  - Section 3.4.
  - Lewis and Sauro 2006 (section 3.4; Sources).
  - Laubheimer, NN/g, 2024 (l.128, "50+ participants per tree"; Sources).
  - Section 6.3.
  - IA9, RV-11 (l.265).
  - IA9, section 6.3 (l.52, l.94, l.219).
  - "Rungs … this unit's construct" matches l.257.
- Fault (a): the caption gives sources for the rungs but not for the Perqo column. That column comes from IA6, Deliverable A (C0); IA3, section 5.2 (C1); section 4.1 (C2, the pilot of 12); and Deliverable A, V-05, V-15 and V-01 (C3 to C5).
- Fault (b), minor: "Rungs this unit's construct:" is missing its verb.

**3. Kind: PASS**
Six ordered rungs, each against the same five attributes, are items by sections, so a matrix fits. A flow would lose the four attribute columns.

**4. Notation: PASS**
- Tone 5 is IA2's "shared: … any object or term on more than one surface" (IA2 l.206, l.342). The unit names this use: "Tone 5, shared, carries the methods and the confidence ladder, because a method serves any surface" (l.14), and again at l.268.
- Tone 3 is IA2's "the Perqo app and the employee". Line 268 names it and explains the one perqo.com case: "the search log is the Help centre's, on perqo.com: section 2.4".
- No other tones are drawn.
- Colour is not the only carrier: the "At Perqo" header and the legend's words carry both meanings.
- The row labels C0 to C5 are two characters each and trace to l.257 and the table.

**5. Frames, all widths, dark and light: PASS**
I checked 320, 360, 390 and 430 px, tablet and desktop, plus the opening frames. Light was judged on cream: the lavender (tone 5) and sage (tone 3) fills read well on it.
- Text sits inside its boxes everywhere, and nothing overlaps.
- The caption is under the figure at every width.
- Every column is shown whole in at least one frame: at 320, Evidence in frame 1, Can decide in frame 2, Cannot decide in frame 3, At Perqo in frame 4. 360, 390 and 430 follow the same pattern.
- Tablet and desktop each fit in one frame.

These notes rest on how the renderer lays the figure out, not on the figure:
- The sticky label column with its fade on phones.
- The sticky section bar clipping the opening frames.
- The label column is about 115 px wide even though its labels are two characters.
- The Evidence column is narrow, so C3 and C5 wrap to eight or nine lines (the column-width rule).
- At 320 and 360 the legend item "tone 3 the employee: every Perqo example" never appears clean in a single frame: the fade dims part of it, or its last letters are at the edge. The chip and its text are each readable whole across frames 3 and 4 (at 360, frames 2 and 3).

**Figure 6: FIX.** Two caption replacements, each to be applied identically to the "caption" field of declaration.json (the figure's viz block) and to captions.md. Each Current occurs once in each.
1. Current `Rungs this unit's construct:` → Replacement `Rungs are this unit's construct:`
2. Current `the Perqo column tone 3, the employee. Perqo is fictional.` → Replacement `the Perqo column tone 3, the employee. Perqo examples from IA6, Deliverable A (C0); IA3, section 5.2 (C1); section 4.1 (C2); and Deliverable A, V-05 (C3, C4), V-15 (C4) and V-01 (C5). Perqo is fictional.`
