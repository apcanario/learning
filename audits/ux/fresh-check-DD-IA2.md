---
audit: fresh check
unit: DD-IA2 · Deep dive: what IA costs and returns
course: ux · IA · Information Architecture
model: Fable 5.2 (claude-fable-5-2, as the agent states; this session keeps no agent transcript on disk, so the model could not be confirmed from a transcript's "model" field; live search). The session's "fable" model is Fable 5.2, not the Fable 5.1 method §4 names, so a Fable 5.1 fresh check of DD-IA2 is owed to the Fable stage (P49)
date: 2026-11-10
chat: own Fable 5.2 agent context, not shown the writing (P31), launched by the U-14 chat (which itself ran on Fable 5.2 and only filed; the writer ran on Opus 5.5) in session https://claude.ai/code/session_01KMmgR1E3GMDHzpY7jqHeSG
verdict: fix · 2 error, 11 should-fix, 7 minor
---

The checker's final report, verbatim: the file it wrote to its own folder as it went (`out/report.md`, 42,636 bytes, copied by script), which its hand-back calls the same report; the hand-back as delivered differs from it only in its framing lines (a one-line verdict summary, a files note naming `out/findings.json`, sha256 f85f6caf…, and a closing note for the main session). This session writes no agent transcript to disk, so the hand-back could not be extracted by script; the file is the record. It checked an exact copy of the unit as committed at cf7802a (sha256 3d7b5a25537ef4bdfaf69fd271a24f9ef05792c8776c8e3cab3f1e3755015d4a, two copies, confirmed by the checker at its start, after the restart and at its end). The session restarted once about four minutes into the check; the harness resumed the same agent from its saved state, and it carried on from its own log. Saved before any finding was applied. Maintainer's notes follow the report.

Model: Fable 5.2 (exact model id claude-fable-5-2). I am not Fable 5.1: a Fable 5.1 fresh check of DD-IA2 is still owed.

# DD-IA2 fresh check, 10 November 2026

Run note: the session restarted once mid-run. The checker folder was intact; I resumed from my own log. One WebFetch (Moran 2020) was cut off by the restart, not by the site, and I ran it once more; say if that breaks the web rule as you read it and treat Moran as "not checked".

## sha256
Start, after the restart, and end: DD-IA2.md and readonly/DD-IA2.copy.md both 3d7b5a25537ef4bdfaf69fd271a24f9ef05792c8776c8e3cab3f1e3755015d4a, equal to both lines of SHA256SUMS. The unit was not edited.

## Context seen and not used
My context held a memory snapshot (a listing of three memory files), Project instructions and a Project doc list, a commit-attribution reminder, and a skills list. None was opened or used as a source. No memory, past-chat, Projects, connector, Artifact, Agent or mcp__ tool was called. Nothing under /home/claude/work/writer or /home/claude/learning was opened. The audit reports were not read (see 6).

## (1) Coverage against the brief
- Published evidence on findability failure and cost: covered (1.2 to 1.5). Task-success rates covered; search versus browse covered; support contacts and failed self-service covered (one press release, Gartner 2019: thin, and the unit says so); redesigns with before-and-after numbers covered (two averages, four single cases).
- Each with source, sample, date and label: covered, in the text and in register RD-16 to RD-31. Labels used: peer-reviewed, consultancy report, maker's report, vendor, anecdote, official statistics.
- What cannot be measured; claims without evidence named: covered (2.1, 2.2), but claim 3 is wrong about its source (finding 2).
- Measurement model, leading (tree-test success, first-click accuracy) and lagging (task success, search exits, support tickets by category, time to find): covered; each of the four lagging items maps to a metric (M-19, M-14, M-15, M-16).
- Business case: cost of change by layer, cost of not changing, the decision supported: covered (4.1 to 4.3), plus cost of evidence and benefits by rung.
- Limits of the exercise: covered (5).
- Figures named in the brief: evidence table as a compare (figure 1), cost by layer (figure 4), measurement model (figure 3): all present; three more (2, 5, 6). Six figures, inside the three-to-eight rule.
- Deliverable: model with metric, source of data, baseline method, target, cadence: covered (A). Template with sourced ranges and labels: covered (B). Filled once for Perqo Admin, every figure traced or marked assumed: covered, with the gaps in findings 7 to 10.
- Missing: nothing. Thin: support-contact cost (one source).

## (2) Accuracy: sources opened, each PASS / FAIL / unverifiable
Writer's unsure list first.
- Boehm and Basili 2001: PASS as stated (catalogue record only; Computer 34(1), 2001/01, pp. 135 to 137; ratios not used). https://umiacs.umd.edu/node/12156
- McKinsey 2012, "19% not found": FAIL. The 19% is in the report (finding 2). The 35%, 6% and 28 hours PASS.
- Gartner 2019: PASS. 9%; $8.01 and $0.10 from "Gartner's 2019 Customer Service and Support Leader poll"; "survey of 8,398 customers" for channels; phone 44%; the 9% is tied to no sample. "Mostly consumer service" not confirmed (finding 18).
- Moran 2020: PASS. 99 case studies; 247% to 75%; "statistically significant (p = 0.01)"; 95% interval "from 8% to 104%"; half between 13% and 157%; each case with at least one before-and-after pair. "Teams chose to submit": unverifiable (finding 13).
- Katz and Byrne 2003: PASS for both quoted phrases and the date (1 Sep 2003); participant numbers not on the record, as the unit says; issue and pages not shown on the record (unverifiable there, consistent with IA3).
- Pshock and Haefele: PASS. 170 participants, four tasks, 63% to 70%, 69% to 74%, borrow task 79% to 61%, no test; no year on the page, as the unit says.
- Spool 2001: PASS. 30 users, 121 tasks, "between 3 and 6 web sites", 21%, 32%, 47%; number of sites not stated.
- Anderson 2021: PASS. Quotes confirmed; no quotation from or page of the Forrester report.
- Nielsen 2009: PASS in the body (14% and 10% of task attempts; 25 and 24 websites; 66% and 81%; both quotations; scheme of 2004, book, coders not stated). FAIL in register row RD-18 (finding 1).
Other sources.
- Sauro 2011: PASS. 78%; 1,189 tasks, 115 tests, 3,472 users, "over a dozen organizations"; 92% and 49%.
- Sauro 2013 (tree testing; RD-17; figure 1's 66; the "17 of 20" that section 3.1 leans on): unverifiable. Three searches did not return the article's address, so it was not fetched. Not in the vault either.
- Bailey and others 2009: not opened (cited through IA11); the unit's wording matches IA11 section 2.3 exactly.
- Nielsen 1997: not opened (cited through IA3); matches IA3 section 5.1.
- Dub 2021: PASS, opened: "We found that while most users start from a search engine, around 15% use topic pages to navigate"; no method.
- Fraser, Sutter and Stockford 2024: PASS. 14%, 11%, 8%; ramped to "50% of users (who had consented to analytics tracking)"; no n, length or intervals.
- Dub 2022: PASS. 50%; "Overall this increased from 61.6% to 65.1%"; clickthrough to content.
- Feldman 2004: PASS for 15% to 35% and $5,000; the 21% study's year is off (finding 4).
- Nielsen, intranet, 2002: PASS. 14 companies, sixteen tasks, $3,042, $2,069, $1,563, $311,294,070,513, about $600 billion, $1.3 trillion.
- Nielsen, foreword, 2002: PASS. Exact sentence; no method.
- Nielsen 2008: 83%, 135%, six years, factor of 10, about 12%, p = 8%, "marginally significant" PASS; the "72 case studies" and the quoted phrase are misattached (finding 3).
- Porton, ONS, 2013: PASS. All seven quoted figures; "sets a satisfaction benchmark of 78%".
- SWOOP: PASS. Sharon Dawson, "27 Jul", no year; quotation; no sample.
- Wayne 2021: PASS for the three quotations; "for design-level defects" unverifiable (finding 17).
- Bossavit, Leanpub: PASS. Ch. 10 and appendix B titles; page metadata date 2025-12-20.
- Cohn: PASS. "Last updated March 3rd, 2026"; sentence; no data cited.
- BLS HR managers: PASS, $149,280, May 2025, last modified 29 October 2026. BLS financial managers: PASS, $166,570, May 2025, last modified 27 August 2026. BLS Economics Daily: PASS, 17 September 2026, $46.89, wages 70.0 percent.
No figure had changed between the writer's date and mine (same day). No figure is taken from a secondary page as if it were the source: the three second-hand ones are marked "as cited in".

## (3) Figures say whose they are
Every published number names its author or organisation where it is made. Every Perqo number in section 4 and Deliverable C is marked as the unit's assumption, IA7's, IA11's plan, or arithmetic. Exceptions: the kinds in C.8 and its missing rows (findings 9, 10).

## (4) Labels
Anecdote (SWOOP), vendor (SWOOP), maker's report (GOV.UK, ONS, UNC), consultancy report, practice and official statistics are all labelled where used. No correlational data is cited as causal; 2.1 and 5 say what before-and-after numbers cannot show. Perqo is never used as evidence about the world.

## (5) Deliverable
Present in full: A (model, 15 rows, rules), B (template, reference ranges, number rule), C (filled case with options, load, costs, break-even, sensitivity, benefits, number register, leadership page, sales line), D (DL-021, DL-022). It follows from the evidence: no published figure enters the Perqo arithmetic. Usable alone: yes; each row cites its defining unit. Defects: findings 6 to 10.

## (6) Errata, pointers, Perqo facts
- Errata of the audit reports: not checked. I was told to skip the audit reports and they are not in my folder, so I cannot say which errata touch this unit or whether they were applied.
- Pointers to filed units, opened in vault/ and found right: IA7 2.2 (1,200 employees, three admin users, 180 a month, 9 a day), 4.5 (no search, find fields), O-17, AD-1.3, AD-2.2, AD-3.1.1; IA9 2.4 (the IA-debt quotation), 4.2 (steps 2, 3, 6, 7), 4.4 (version rule), 6.2 (tags), 6.3 (Admin page views, failed sign-ins), Deliverable C (RV-04, 05, 06, 10, 11; owners; "ranked by value and effort on the backlog"), D.1, D.3; IA10 A.1 (TP-01 to TP-12 as used), A.2 (FO-01, 04, 05, 07, 08, 09), 1.4, 2.4, 2.9, BR-3 "What Perqo does not do", "What later units take"; IA11 1.2 (M-01 to M-11), 2.2, 2.3, 2.5, 3.1, 3.2, 4.4 (marks, the 12-of-12 sentence, Sauro's 78%), 6.1, 6.3, 6.4, 7, plan rows V-01, V-03, V-17, A.2 row 1, B.6, TT-A (one fail, one pass, eight undecided), facts table (Admin's marks left free); IA12 3.2, 3.3, 3.4 (49 rows, 28, all C0), 5 (criterion, ten layers, 25 backbone), Deliverable B (every AR- row the unit names, with its fix and test), D.1 template fields, D.4 DL-019; DD-IA1 1, 2 (the quotation, RD-03, RD-05), handoff; IA3 5.1, 5.2; IA2 5.2 and the notation sheet; IA8 CL-6.
- Pointers found wrong or loose: findings 5, 6, 14, 15, 20.
- Metrics: M-01 to M-04, M-07, M-11 as IA11 defines them; M-05 extended without saying so (finding 6); M-12 to M-19 said to be new.
- Perqo facts: "(Perqo, fictional)" on first use (first sentence). Consistent with the vault and the register; the client count and staff rates were free. Every new fact I found is in "Perqo facts set by this unit". DL-021 and DL-022 follow DL-020, use IA12's template field for field, are proposed, routed by IA9 D.1, and change no filed artefact.
- Public-site rules: no personal fact about the reader; no private person (named people are bylined authors); real companies only as their own or cited publications say, each dated; no long unbroken link text.

## (7) Figures
1. compare, section 1.6. Every label and value is in the paragraph before it ("Usability tasks completed (MeasuringU, 2011), 78; ... Attempts failed by IA, 2009 (NN/g), 10"). Kind fits (numbers compared). Tones 2 and 6 named in the text. Caption names what, section and sources. FIX, caption only: finding 12b. (Row 2's 66 rests on Sauro 2013, unverifiable.)
2. matrix, numeric, section 1.6. Rows and cells are in the paragraph before it ("GOV.UK topic pages, clickthrough, 61.6 and 65.1; ..."). scale_label "percent, as published" is not in the text. Kind acceptable for pairs by before and after. FIX: finding 11 (text, not JSON).
3. matrix, section 3.4. All 15 rows, four columns, cells and the three legend lines are in the bullets before it. Kind fits (items by dimensions). Tones 5, 1, 4 named. PASS.
4. compare, section 4.2. Ten layers and values are in the paragraph before it and sum correctly in C.4. Caption says every magnitude is the unit's assumption. PASS.
5. decision, Deliverable B, B.3. Three questions, yes and no (yes left), four outcomes all quoted in the paragraph before it. Kind fits (a rule with branches). PASS.
6. range, Deliverable C, C.6. Labels, lows, highs, point 28.2 and "assumed" tags are in the paragraph before it; all six ends recomputed right. Caption says the assumptions are the unit's. Kind fits (a result across ranges). PASS.
All six use kinds and keys in figure-kinds.md and IA2's tones; the unit names tones 1, 2, 4, 5 and 6 in its text and draws no tone 3.

## Script results (out/check.py, out/ia12.py)
All RIGHT: C.4's ten row totals; C.5 9 staff days, 6 + 5 + 3.75 = 14.75 hours, 86.75 hours; E1 1.5; 9.6 hours; A = 308; break-even 28.17%; sensitivity 15.27 and 86.75, 17.08 and 41.71, 11.79 and 62.41; Perqo-only 72 and 12; clients-only 296 and 4.98%; $71.77; $102.53; $1,512; $30,349; 180 and 9; 17 clients; thirteenfold; FO-07 21, FO-05 6, FO-08 4, FO-09 1 = 32 = 30 wholly + 2 partly absent (counted from IA12's Input column); 49 rows, 25 backbone. Counts right: 16 register rows RD-16 to RD-31; fifteen metrics (6 leading, 9 lagging; 8 new); six claims; five things; four single redesigns; ten rows in figure 1; seven backbone rows and three open rows in C.2; five of six tones. Nothing wrong.

## Findings
1. [error] [accuracy] 1.6, register row RD-18; Current: `IA caused 14% (2004) and 10% (2009) of failed attempts; success 66% and 81%` Fix: `14% (2004) and 10% (2009) of task attempts failed because of the IA; success 66% and 81%` Problem: The source counts shares of all task attempts (14% and 10% of attempts failed because of the IA), not shares of failed attempts; the body (1.2) and figures 1 and 2 have it right, the register row, which the final audit samples, has it wrong. Basis: Nielsen, "IA Task Failures Remain Costly", NN/g, 15 Apr 2009, https://www.nngroup.com/articles/ia-task-failures-remain-costly/ ("14% of task attempts failed due to IA problems in 2004").
2a. [error] [accuracy] 2.2, claim 3; Current: `is attributed to McKinsey Global Institute's 2012 report on social technologies. Its text, as read for this unit, gives a different pair of numbers: social tools could reduce "information searching time by as much as 35 percent", which "would return approximately 6 percent of the workweek", and knowledge workers spend 28 hours a week "writing e-mails, searching for information, and collaborating internally"` Fix: `is McKinsey Global Institute's own estimate, in its 2012 report on social technologies: interaction workers spend "19 percent of working hours trying to track down information needed to complete tasks", which its appendix gives as 8.8 hours of a 46.5-hour week in an exhibit titled "We adjust IDC data to estimate time spent on different activities by a typical interaction worker" (Exhibit A7; 8.8 hours over five days is 1.76 hours a day, this unit's arithmetic). The same report says social tools could reduce "information searching time by as much as 35 percent", which would "return approximately 6 percent of the workweek to other tasks", and that knowledge workers spend 28 hours a week "writing e-mails, searching for information, and collaborating internally"` Problem: The unit says the 19% is not in the McKinsey report and that the report gives "a different pair of numbers". The report does hold it: main text, "19 percent of working hours trying to track down information needed to complete tasks" (beside Exhibit 20), and Exhibit A7, "We adjust IDC data to estimate time spent on different activities by a typical interaction worker": search and gather information 8.8 hours, 19%, of a 46.5-hour week. The claim is a consultancy estimate with no sample, not a misattribution. Basis: Chui and others, The social economy, MGI, July 2012, full report at the mckinsey.com address the unit links; read in five parts (characters 0 to 500,000 of 505,103).
2b. [error] [accuracy] 2.2, claim 3; Current: `The 19% was not found in that text. Feldman's 15% to 35% names no sample (RD-24).` Fix: `The 19% is therefore a consultancy's estimate adjusted from IDC survey data, with no sample given in the passages read; it estimates time spent looking for information and measures nothing about time lost to a poor structure. Feldman's 15% to 35% names no sample (RD-24).` Problem: Same; the closing sentence of the claim. Basis: as 2a
2c. [error] [accuracy] Unsure list; Current: `McKinsey Global Institute 2012: the commonly quoted "19%" or "1.8 hours a day" was not found in the report's text as extracted; an exhibit not captured as text may hold it.` Fix: `McKinsey Global Institute 2012: the "19%" is in the report (the main text beside Exhibit 20, and Exhibit A7, 8.8 hours of 46.5); "1.8 hours a day" does not appear there and is 8.8 hours over five days, rounded; the sample behind the IDC data the report adjusts was not found in the passages read.` Problem: Same; the unsure item is now resolved. Basis: as 2a
2d. [error] [accuracy] Deliverable B, B.2; Current: `| Time spent searching at work | 15% to 35% | RD-24 | consultancy report, no sample | do not use |` Fix: `| Time spent searching at work | 15% to 35%; 19% (McKinsey Global Institute, 2012, adjusted from IDC data) | RD-24; section 2.2, claim 3 | consultancy report, no sample | do not use |` Problem: Same; the reference table should carry the 19% with its label so the template does not leave it as an unexamined figure. Basis: as 2a
3a. [should-fix] [accuracy] 1.5; Current: `Nielsen reported in 2008 that across 72 case studies "the average improvement in key performance indicators" was 83%, against 135% in NN/g's survey six years earlier;` Fix: `Nielsen reported in 2008 that in NN/g's new survey of design projects "the average improvement was 83%" in key performance indicators, against 135% in its survey six years earlier; the full report holds 72 case studies, and the article does not say how many projects the 83% averages;` Problem: The quoted phrase "the average improvement in key performance indicators" belongs in the article to the earlier survey's 135%; the 83% sentence reads "this time the average improvement was 83%". The article ties "72 case studies" to the full report's contents and does not say the 83% is an average across 72 (outliers were removed). Basis: Nielsen, "Usability ROI Declining, But Still Strong", NN/g, 21 Jan 2008, https://www.nngroup.com/articles/usability-roi-declining-but-still-strong/ (read twice).
3b. [should-fix] [accuracy] 1.6, RD-26 sample cell; Current: `72 case studies; outliers removed` Fix: `not given for the 83%; the report holds 72 case studies; outliers removed` Problem: Same. Basis: as 3a
3c. [should-fix] [accuracy] 2.1, last bullet; Current: `and Nielsen's 72 are design projects (RD-26)` Fix: `and Nielsen's survey is of design projects (RD-26)` Problem: Same. Basis: as 3a
4. [should-fix] [accuracy] 1.4; Current: `and that an IDC study of 2002 found that only 21%` Fix: `and that an IDC study, which the article dates 2001 and cites as "Quantifying Enterprise Search", IDC, May 2002, found that only 21%` Problem: The article says "An IDC study in 2001" and cites it as "Quantifying Enterprise Search", IDC, May 2002; the unit gives 2002 as the study's year. Basis: Feldman, KMWorld, 1 Mar 2004, https://www.kmworld.com/Articles/Editorial/Feature/The-high-cost-of-not-finding-information-9534.aspx
5. [should-fix] [attribution] 3.2, table row M-12; Current: `the interval of a difference of two proportions, period with period (IA11, section 3.4)` Fix: `the interval of a difference of two proportions, period with period (IA11, section 1.2, M-10's reading, and section 6.2; section 3.4 gives the interval of one proportion)` Problem: IA11 section 3.4 sets only the adjusted-Wald interval of one proportion. The interval of a difference is in IA11 section 1.2 (M-10's reading), section 6.2 and plan rows V-09 and V-17. A.3 rule 2 already cites 3.4 and 6.2 together. Basis: vault/IA11, sections 1.2, 3.4, 6.2.
6. [should-fix] [attribution] Deliverable A, A.1, row M-05; Current: `| M-05 | Placement share | IA11, section 1.2 | hybrid card sort with admin users (Deliverable C, E3) |` Fix: `| M-05 | Placement share | IA11, section 1.2, which defines it for a closed sort; applied here to the given categories of a hybrid sort (this unit's extension) | hybrid card sort with admin users (Deliverable C, E3) |` Problem: IA11 defines M-05 "in a closed sort"; the unit reads it from a hybrid sort while saying each leading metric is "as IA11 defines it". The extension is reasonable (a hybrid sort has given categories) but must be said. Basis: vault/IA11, section 1.2, row M-05; section 3.1.
7a. [should-fix] [deliverable] Deliverable C, C.7, row 1; Current: `| C0 | C5 for M-16 and M-18 | C2 for the list and detail |` Fix: `| C0 | C5 for M-18; C5 for M-16 once its find-field event is recorded (section 3.2) | C2 for the list and detail |` Problem: M-16 needs a find-field event that section 3.2 says Perqo does not record; E1 (O-2) reads only first actions, page views and claim records and prices no engineering to add events. O-2 cannot give C5 for M-16. Basis: the unit's own section 3.2 and C.5.
7b. [should-fix] [deliverable] Deliverable C, C.6, last paragraph; Current: `E1's read of N or of f (through M-15 and M-16) moves the break-even directly` Fix: `the client count from customer success (N) and the reads bearing on f (M-15 at RV-05; M-16 once its find-field event is recorded, section 3.2) move the break-even directly` Problem: Same; and C.3 says N is replaced by customer success's client count, not by E1. Basis: the unit's own C.3 and section 3.2.
8. [should-fix] [deliverable] Deliverable C, C.5, row E3; Current: `hybrid card sort of Admin's objects and their names, 20 minutes each, in E2's sessions` Fix: `hybrid card sort of Admin's objects and their names, 20 minutes each, in E2's twelve sessions and three more` Problem: E3 has 15 participants "in E2's sessions", but E2 has 12. Hours (5) and the five-client precondition are unaffected by the fix. Basis: the unit's own C.5.
9. [should-fix] [deliverable] Deliverable C, C.8; Current: `| 8 | hours in a staff day | assumed | this unit |` Fix: `| 8 | hours in a staff day | assumed | this unit |
| 10 to 40 | range of clients now | assumed, C0 | this unit; customer success |
| 4 minutes a week; 48 working weeks | the working behind the 10 hours | assumed, C0 | this unit; M-16 once its event is recorded |
| 30; 20 minutes | session length of E2; of E3 | assumed | this unit |
| 3; 2; 1 | staff days of E2, E3 and recruiting | assumed | this unit; E2's carried from IA11, V-03 |
| 9; 14.75; 72; 12; 296; 5% | staff days and participants' hours of E2 to E4; Perqo's hours spent and saved; clients' hours saved and their break-even | arithmetic | C.5 and C.6 |
| 15.3% to 86.8%; 17.1% to 41.7%; 11.8% to 62.4% | the break-even across each assumption's range | arithmetic | C.6, figure 6 |` Problem: C.8 is offered as "every number in the case" and as the final audit's test, but omits numbers the case uses: the 10 to 40 range, the 4 minutes and 48 weeks behind f, E2's and E3's session lengths, the staff days 3, 2 and 1, and the derived 9, 14.75, 72, 12, 296, 5% and sensitivity ends. Each is labelled where it is made, so nothing is untraced; the register is incomplete. Fix adds six rows after the row quoted. Basis: the unit's own C.5, C.6; brief: "every figure traced to its source or marked as the unit's own assumption".
10a. [should-fix] [deliverable] 4.6; Current: `Every number in a case is one of three kinds, and the case says which beside it:` Fix: `Every number in a case is sourced, measured or assumed, or a published figure kept as context, and the case says which beside it:` Problem: 4.6 says three kinds; B.3, figure 5 and "What later units take" use four (context added); C.8 adds "Perqo's plan" and "arithmetic". Basis: the unit's own B.3 and C.8.
10b. [should-fix] [deliverable] Deliverable B, B.3, last paragraph; Current: `its kind (measured, sourced, context, assumed);` Fix: `its kind (measured, sourced, context, assumed; a number computed from others is marked arithmetic, and a cost taken from a filed Perqo plan is marked as that plan's);` Problem: Same: name the two extra kinds C.8 uses. Basis: as 10a
11. [should-fix] [figure] 1.6, text before figure 2; Current: `as a grid in tone 2, each cell a percent:` Fix: `as a grid in tone 2, each cell a percent, its scale labelled "percent, as published":` Problem: Figure 2's scale_label "percent, as published" is drawn and is not in the unit's text. It adds no fact, so should-fix not error; the fix adds the words to the text and leaves the viz block alone. Basis: sourcing-standard Part 1 (a figure's labels appear in the text).
12a. [should-fix] [label] introduction, second paragraph; Current: `Every published figure in this unit was read at its source on 10 November 2026, the day the unit was written, and each carries that date, its sample and its label where it is made.` Fix: `Every published figure in this unit was read at its source on 10 November 2026, the day the unit was written, and each carries that date, its sample and its label where it is made; the exceptions are the figures cited through IA3, IA11 and DD-IA1 (Nielsen 1997, Bailey and others 2009, Dub 2021), which are marked as cited there.` Problem: Three published figures were not read at their source that day and are cited through filed units (Nielsen 1997, Bailey 2009, Dub 2021); the blanket sentence contradicts the unit's own "as cited in" labels. Basis: the unit's own 1.2, 1.3.
12b. [should-fix] [figure] figure 1, caption; Current: `All read 10 November 2026. Samples differ` Fix: `All but Bailey and others read 10 November 2026. Samples differ` Problem: Same, in the caption. Basis: as 12a
13a. [should-fix] [accuracy] 1.5; Current: `Both are averages of cases that teams chose to submit, across every kind of UX change, of which IA is one.` Fix: `Both are averages of case studies NN/g collected for its reports, by a selection neither article describes, across every kind of UX change, of which IA is one.` Problem: "cases that teams chose to submit" is not in either NN/g article as returned: unverifiable. Neither describes how its cases were selected. Basis: Moran 2020, https://www.nngroup.com/articles/ux-gains-shrinking/ ; Nielsen 2008.
13b. [should-fix] [accuracy] 5, second paragraph; Current: `and it comes from cases teams chose to submit.` Fix: `and it comes from case studies whose selection the article does not describe.` Problem: Same. Basis: as 13a
14. [minor] [accuracy] 3.1; Current: `a tree test has "no visual design, no content on the page, no search"` Fix: `a tree test has no visual design, no content on the page and no search` Problem: IA11 writes "No visual design, no content on the page, no search, and no scent ..."; the quotation lower-cases and truncates it. Paraphrase instead. Basis: vault/IA11, section 2.2.
15. [minor] [attribution] 1.6; Current: `The register below records each published figure in DD-IA1's form, continuing` Fix: `The register below records each published figure in a form adapted from DD-IA1's (the columns are this unit's), continuing` Problem: DD-IA1's register columns are Product, Claim, Source, Evidence kind, Not tested, Not visible, Rung; this register's differ. Basis: vault/DD-IA1, Deliverable A.
16. [minor] [attribution] Sources, last entry; Current: `NN/g, 2024 (IA11); Lewis and Sauro, "When 100% Really Isn't 100%", *Journal of Usability Studies*, 2006 (IA11); Nielsen, "Search and You May Find"` Fix: `NN/g, 2024 (IA11); Nielsen, "Search and You May Find"` Problem: Lewis and Sauro 2006 is listed and never cited in the unit's text (Part 1: nothing listed that is not cited). Basis: grep of the unit.
17. [minor] [accuracy] 2.2, claim 2; Current: `is that it "tentatively points in that direction" for design-level defects, with "no smoking gun"` Fix: `is that it "tentatively points in that direction", depending on how late-stage, bugs and more expensive are read, with "no smoking gun"` Problem: "for design-level defects" was not in the sentence as returned, which ends "depending on how you interpret 'late-stage', 'bugs', and 'more expensive'". Unverifiable as written. Basis: Wayne, https://buttondown.com/hillelwayne/archive/i-ing-hate-science/
18. [minor] [accuracy] 1.4; Current: `The cost figures are averages reported by service leaders, across industries and mostly consumer service, and say nothing about a business tool's support.` Fix: no change required Problem: "across industries and mostly consumer service" was not confirmed in the release as returned (I did not ask the page that question); the writer should confirm or cut. The same reading recurs in 4.3 and B.2. Basis: Gartner press release, 25 Sep 2019.
19. [minor] [style] 3.2; Current: `eight lagging metrics are new here, three from GOV.UK's search work and five that Admin's records need.` Fix: no change required Problem: M-12 to M-19 as metric identifiers share the M- prefix and numbers with IA5's template modules M-01 to M-27 (and DD-IA1's proposed M-28). The collision began with IA11's M-01 to M-11 and is not this unit's; a proposed backlog row could settle it. Basis: vault/IA5 Deliverable C; perqo-facts.md line 117.
20. [minor] [attribution] Deliverable D, D.1; Current: `inside one artefact, renaming nothing (IA9, D.1), as DL-019 is` Fix: no change required Problem: IA9 D.1 reads "inside one surface and renaming nothing"; "inside one artefact" repeats IA12's DL-019 wording. Consistent with the filed IA12. Basis: vault/IA9 D.1; vault/IA12 D.4.

## Confirmed
- 78% average completion, 1,189 tasks, 115 tests, 3,472 users, quartiles 92% and 49%: Sauro 2011, https://measuringu.com/task-completion/
- 14% and 10% of task attempts failed due to IA; 25 and 24 websites; 66% and 81%: Nielsen 2009, https://www.nngroup.com/articles/ia-task-failures-remain-costly/
- 30 users, 121 tasks, 21% / 32% / 47% of sites: Spool 2001, https://articles.centercentre.com/?p=15
- Search "did not yield faster or more accurate performance"; "should not be used to compensate for poor menu design": Katz and Byrne 2003, https://unpaywall.org/10.1145%2F937549.937551
- "around 15% use topic pages to navigate": Dub 2021, https://gds.blog.gov.uk/2021/05/17/our-plans-to-improve-navigation-on-gov-uk
- 14%, 11%, 8%; 50% of consenting users: https://insidegovuk.blog.gov.uk/2024/10/23/a-new-search-engine-for-gov-uk/
- 61.6% to 65.1%: https://insidegovuk.blog.gov.uk/2022/08/08/rolling-out-a-new-design-for-browsing-gov-uk-by-topic/
- 9%; $8.01; $0.10; 8,398 customers; phone 44%: Gartner, https://www.gartner.com/en/newsroom/press-releases/2019-09-25-gartner-says-only-9--of-customers-report-solving-thei
- 15% to 35%; $5,000 per worker (IDC, 1999): Feldman, https://www.kmworld.com/Articles/Editorial/Feature/The-high-cost-of-not-finding-information-9534.aspx
- $3,042, $2,069, $1,563; $311,294,070,513; $600 billion; $1.3 trillion: https://www.nngroup.com/articles/intranet-usability-the-trillion-dollar-question/
- "$100 billion per year in lost employee productivity": https://www.nngroup.com/articles/foreword-ia-2nd/
- 83%; 135%; factor of 10; about 12%; p = 8%: https://www.nngroup.com/articles/usability-roi-declining-but-still-strong/
- 99 cases; 247%; 75%; p = 0.01; 8% to 104%; 13% to 157%: https://www.nngroup.com/articles/ux-gains-shrinking/
- ONS: about 200, over 130, 86%, half the time, almost 30%, 11 to 4, over 1400, 5 levels: https://digitalblog.ons.gov.uk/2013/12/05/no-longer-taxing-we-hope
- UNC: 170, four tasks, 63% to 70%, 69% to 74%, 79% to 61%: https://libux.web.unc.edu/2016/05/19/assessing-nav-changes/
- SWOOP "53% faster", no sample, no year: https://www.swoopanalytics.com/case-studies/intranet-information-faster-to-find
- Anderson's "$1 ... $100" and its hedge: https://www.mindsetconsulting.com/user-experience-ux-turns-your-1-investment-into-a-100-return-really/
- Wayne on the IBM chart: https://buttondown.com/hillelwayne/archive/i-ing-hate-science/
- Bossavit ch. 10, appendix B: https://leanpub.com/leprechauns
- Boehm and Basili record: https://umiacs.umd.edu/node/12156
- Cohn's sentence, no data: https://www.mountaingoatsoftware.com/blog/the-cost-of-change-curve-is-outdated
- McKinsey 35%, 6%, 28 hours (and the 19%): the full-report address the unit links
- BLS $149,280: https://www.bls.gov/ooh/Management/human-resources-managers.htm ; $166,570: https://www.bls.gov/OOH/management/financial-managers.htm ; 70.0%: https://www.bls.gov/opub/ted/2026/compensation-costs-for-private-industry-workers-averaged-46-89-per-hour-worked-in-june-2026.htm
- Every vault pointer listed under (6) as right.

## Sources opened, and not checked
Opened (all fetched from an address a search of mine returned, none refused or redirected): the 25 pages listed under Confirmed, the McKinsey report in five parts (last 5,103 characters unread), Nielsen 2008 twice, Moran once after the interrupted call.
Not checked: Sauro 2013, "Using Tree-Testing To Test Information Architecture" (three searches, address never returned); Bailey and others 2009 and Nielsen 1997 (cited through IA11 and IA3, not opened); the Forrester report, Prioritizing Web Usability, and the Boehm and Basili article (the unit says it did not see them either); the audit reports (by instruction). The full search and fetch log, in order, is /home/claude/work/checker/out/log.md.

## New things worth remembering (for the main session to decide)
- The M- prefix is shared by IA5's modules and IA11's and DD-IA2's metrics (learned from vault/IA5 and perqo-facts.md): a candidate proposed backlog row.
- Sauro 2013 could not be opened by search today; the Fable 5.1 check should try again.

DD-IA2: verdict fix; 2 errors, 11 should-fix, 7 minor (20 findings, 29 replacements).

```json
[
 {
  "n": "1",
  "severity": "error",
  "current": "IA caused 14% (2004) and 10% (2009) of failed attempts; success 66% and 81%",
  "fix": "14% (2004) and 10% (2009) of task attempts failed because of the IA; success 66% and 81%"
 },
 {
  "n": "2a",
  "severity": "error",
  "current": "is attributed to McKinsey Global Institute's 2012 report on social technologies. Its text, as read for this unit, gives a different pair of numbers: social tools could reduce \"information searching time by as much as 35 percent\", which \"would return approximately 6 percent of the workweek\", and knowledge workers spend 28 hours a week \"writing e-mails, searching for information, and collaborating internally\"",
  "fix": "is McKinsey Global Institute's own estimate, in its 2012 report on social technologies: interaction workers spend \"19 percent of working hours trying to track down information needed to complete tasks\", which its appendix gives as 8.8 hours of a 46.5-hour week in an exhibit titled \"We adjust IDC data to estimate time spent on different activities by a typical interaction worker\" (Exhibit A7; 8.8 hours over five days is 1.76 hours a day, this unit's arithmetic). The same report says social tools could reduce \"information searching time by as much as 35 percent\", which would \"return approximately 6 percent of the workweek to other tasks\", and that knowledge workers spend 28 hours a week \"writing e-mails, searching for information, and collaborating internally\""
 },
 {
  "n": "2b",
  "severity": "error",
  "current": "The 19% was not found in that text. Feldman's 15% to 35% names no sample (RD-24).",
  "fix": "The 19% is therefore a consultancy's estimate adjusted from IDC survey data, with no sample given in the passages read; it estimates time spent looking for information and measures nothing about time lost to a poor structure. Feldman's 15% to 35% names no sample (RD-24)."
 },
 {
  "n": "2c",
  "severity": "error",
  "current": "McKinsey Global Institute 2012: the commonly quoted \"19%\" or \"1.8 hours a day\" was not found in the report's text as extracted; an exhibit not captured as text may hold it.",
  "fix": "McKinsey Global Institute 2012: the \"19%\" is in the report (the main text beside Exhibit 20, and Exhibit A7, 8.8 hours of 46.5); \"1.8 hours a day\" does not appear there and is 8.8 hours over five days, rounded; the sample behind the IDC data the report adjusts was not found in the passages read."
 },
 {
  "n": "2d",
  "severity": "error",
  "current": "| Time spent searching at work | 15% to 35% | RD-24 | consultancy report, no sample | do not use |",
  "fix": "| Time spent searching at work | 15% to 35%; 19% (McKinsey Global Institute, 2012, adjusted from IDC data) | RD-24; section 2.2, claim 3 | consultancy report, no sample | do not use |"
 },
 {
  "n": "3a",
  "severity": "should-fix",
  "current": "Nielsen reported in 2008 that across 72 case studies \"the average improvement in key performance indicators\" was 83%, against 135% in NN/g's survey six years earlier;",
  "fix": "Nielsen reported in 2008 that in NN/g's new survey of design projects \"the average improvement was 83%\" in key performance indicators, against 135% in its survey six years earlier; the full report holds 72 case studies, and the article does not say how many projects the 83% averages;"
 },
 {
  "n": "3b",
  "severity": "should-fix",
  "current": "72 case studies; outliers removed",
  "fix": "not given for the 83%; the report holds 72 case studies; outliers removed"
 },
 {
  "n": "3c",
  "severity": "should-fix",
  "current": "and Nielsen's 72 are design projects (RD-26)",
  "fix": "and Nielsen's survey is of design projects (RD-26)"
 },
 {
  "n": "4",
  "severity": "should-fix",
  "current": "and that an IDC study of 2002 found that only 21%",
  "fix": "and that an IDC study, which the article dates 2001 and cites as \"Quantifying Enterprise Search\", IDC, May 2002, found that only 21%"
 },
 {
  "n": "5",
  "severity": "should-fix",
  "current": "the interval of a difference of two proportions, period with period (IA11, section 3.4)",
  "fix": "the interval of a difference of two proportions, period with period (IA11, section 1.2, M-10's reading, and section 6.2; section 3.4 gives the interval of one proportion)"
 },
 {
  "n": "6",
  "severity": "should-fix",
  "current": "| M-05 | Placement share | IA11, section 1.2 | hybrid card sort with admin users (Deliverable C, E3) |",
  "fix": "| M-05 | Placement share | IA11, section 1.2, which defines it for a closed sort; applied here to the given categories of a hybrid sort (this unit's extension) | hybrid card sort with admin users (Deliverable C, E3) |"
 },
 {
  "n": "7a",
  "severity": "should-fix",
  "current": "| C0 | C5 for M-16 and M-18 | C2 for the list and detail |",
  "fix": "| C0 | C5 for M-18; C5 for M-16 once its find-field event is recorded (section 3.2) | C2 for the list and detail |"
 },
 {
  "n": "7b",
  "severity": "should-fix",
  "current": "E1's read of N or of f (through M-15 and M-16) moves the break-even directly",
  "fix": "the client count from customer success (N) and the reads bearing on f (M-15 at RV-05; M-16 once its find-field event is recorded, section 3.2) move the break-even directly"
 },
 {
  "n": "8",
  "severity": "should-fix",
  "current": "hybrid card sort of Admin's objects and their names, 20 minutes each, in E2's sessions",
  "fix": "hybrid card sort of Admin's objects and their names, 20 minutes each, in E2's twelve sessions and three more"
 },
 {
  "n": "9",
  "severity": "should-fix",
  "current": "| 8 | hours in a staff day | assumed | this unit |",
  "fix": "| 8 | hours in a staff day | assumed | this unit |\n| 10 to 40 | range of clients now | assumed, C0 | this unit; customer success |\n| 4 minutes a week; 48 working weeks | the working behind the 10 hours | assumed, C0 | this unit; M-16 once its event is recorded |\n| 30; 20 minutes | session length of E2; of E3 | assumed | this unit |\n| 3; 2; 1 | staff days of E2, E3 and recruiting | assumed | this unit; E2's carried from IA11, V-03 |\n| 9; 14.75; 72; 12; 296; 5% | staff days and participants' hours of E2 to E4; Perqo's hours spent and saved; clients' hours saved and their break-even | arithmetic | C.5 and C.6 |\n| 15.3% to 86.8%; 17.1% to 41.7%; 11.8% to 62.4% | the break-even across each assumption's range | arithmetic | C.6, figure 6 |"
 },
 {
  "n": "10a",
  "severity": "should-fix",
  "current": "Every number in a case is one of three kinds, and the case says which beside it:",
  "fix": "Every number in a case is sourced, measured or assumed, or a published figure kept as context, and the case says which beside it:"
 },
 {
  "n": "10b",
  "severity": "should-fix",
  "current": "its kind (measured, sourced, context, assumed);",
  "fix": "its kind (measured, sourced, context, assumed; a number computed from others is marked arithmetic, and a cost taken from a filed Perqo plan is marked as that plan's);"
 },
 {
  "n": "11",
  "severity": "should-fix",
  "current": "as a grid in tone 2, each cell a percent:",
  "fix": "as a grid in tone 2, each cell a percent, its scale labelled \"percent, as published\":"
 },
 {
  "n": "12a",
  "severity": "should-fix",
  "current": "Every published figure in this unit was read at its source on 10 November 2026, the day the unit was written, and each carries that date, its sample and its label where it is made.",
  "fix": "Every published figure in this unit was read at its source on 10 November 2026, the day the unit was written, and each carries that date, its sample and its label where it is made; the exceptions are the figures cited through IA3, IA11 and DD-IA1 (Nielsen 1997, Bailey and others 2009, Dub 2021), which are marked as cited there."
 },
 {
  "n": "12b",
  "severity": "should-fix",
  "current": "All read 10 November 2026. Samples differ",
  "fix": "All but Bailey and others read 10 November 2026. Samples differ"
 },
 {
  "n": "13a",
  "severity": "should-fix",
  "current": "Both are averages of cases that teams chose to submit, across every kind of UX change, of which IA is one.",
  "fix": "Both are averages of case studies NN/g collected for its reports, by a selection neither article describes, across every kind of UX change, of which IA is one."
 },
 {
  "n": "13b",
  "severity": "should-fix",
  "current": "and it comes from cases teams chose to submit.",
  "fix": "and it comes from case studies whose selection the article does not describe."
 },
 {
  "n": "14",
  "severity": "minor",
  "current": "a tree test has \"no visual design, no content on the page, no search\"",
  "fix": "a tree test has no visual design, no content on the page and no search"
 },
 {
  "n": "15",
  "severity": "minor",
  "current": "The register below records each published figure in DD-IA1's form, continuing",
  "fix": "The register below records each published figure in a form adapted from DD-IA1's (the columns are this unit's), continuing"
 },
 {
  "n": "16",
  "severity": "minor",
  "current": "NN/g, 2024 (IA11); Lewis and Sauro, \"When 100% Really Isn't 100%\", *Journal of Usability Studies*, 2006 (IA11); Nielsen, \"Search and You May Find\"",
  "fix": "NN/g, 2024 (IA11); Nielsen, \"Search and You May Find\""
 },
 {
  "n": "17",
  "severity": "minor",
  "current": "is that it \"tentatively points in that direction\" for design-level defects, with \"no smoking gun\"",
  "fix": "is that it \"tentatively points in that direction\", depending on how late-stage, bugs and more expensive are read, with \"no smoking gun\""
 },
 {
  "n": "18",
  "severity": "minor",
  "current": "The cost figures are averages reported by service leaders, across industries and mostly consumer service, and say nothing about a business tool's support.",
  "fix": null
 },
 {
  "n": "19",
  "severity": "minor",
  "current": "eight lagging metrics are new here, three from GOV.UK's search work and five that Admin's records need.",
  "fix": null
 },
 {
  "n": "20",
  "severity": "minor",
  "current": "inside one artefact, renaming nothing (IA9, D.1), as DL-019 is",
  "fix": null
 }
]
```

---

## Maintainer's notes (U-14 chat, 10 November 2026)

**How each finding was verified, and what was applied.** Every Current and Fix was taken by script from the checker's `out/findings.json` (sha256 f85f6caf…, equal string for string to the json block in the report above); each Current counted once in the unit as committed at cf7802a; each Fix checked by script to stand in the saved report; 26 replacements applied in one script run, three minors being "no change required" (18, 19, 20: recorded here, not applied). No line outside a figure holds an odd number of backticks after the run.

- 1 (error): holds. Nielsen's page, found by the maintainer's own search, reads "14% of task attempts failed due to IA problems in 2004" and "10% of task attempts failed due to IA problems in 2009"; the unit's body already said so and row RD-18 did not. Applied.
- 2 (error): holds. The maintainer's search returned the McKinsey full report at mckinsey.com; fetched in four parts from that address: characters 100,000 to 200,000 hold "19 percent of working hours trying to track down information needed to complete tasks"; characters 400,000 to 500,000 hold the exhibit titled "We adjust IDC data to estimate time spent on different activities by a typical interaction worker", with searching and gathering information at 8.8 hours of a total of 46.5; the first part holds the 35 percent and "return approximately 6 percent of the workweek to other tasks". A McKinsey Quarterly page the same search returned draws the same exhibit ("Searching and gathering information 19", source IDC and MGI analysis). 2a to 2d applied; the unsure line changed with it (2c).
- 3: holds. The search returned the NN/g article: "this time the average improvement was 83%"; "the average improvement in key performance indicators (KPI) was 135%" belongs to the earlier survey; "before-after analysis of all 72 case studies" describes the full report. 3a to 3c applied.
- 4: holds. The search returned a quotation of the article: "An IDC study in 2001 ("Quantifying Enterprise Search," IDC, May 2002)". Applied.
- 5: holds. IA11's section 3.4 has no interval of a difference; row M-10 of section 1.2 reads "the interval of a difference when two timings are compared". Applied.
- 6: holds. IA11's row M-05 opens "in a closed sort". Applied.
- 7, 8, 9, 10: hold against the unit's own sections (3.2, C.3, C.5, C.6, B.3, C.8; E2 has 12 admin users and E3 has 15). Applied; finding 9's six rows keep C.8's four columns.
- 11: holds (the scale label is drawn and was not in the text). Applied to the text; the declaration of figure 2 is unchanged.
- 12: holds (the unit's own "as cited in" labels). 12a and 12b applied; 12b changes figure 1's caption.
- 13: holds as unverifiable; neither NN/g article as returned describes how its cases were chosen. Applied. (A Boxes and Arrows review of the first edition of the report, returned by the same search, says most of its cases came from calls for case studies; it is about the 2003 edition, is not the source, and was not added to the unit.)
- 14, 15, 16: hold (IA11 section 2.2's sentence; DD-IA1's register columns; Lewis and Sauro named once, in Sources only). Applied.
- 17: holds. A search returned The Register's report of Wayne's piece quoting the sentence as ending "depending on how you interpret 'late-stage', 'bugs', and 'more expensive'"; "for design-level defects" is not in it. Applied.
- 18, 19, 20: no change required; recorded. The shared M- prefix (19) is IA11's choice and stands in the register; it is noted in the register's DD-IA2 section, with no row proposed.

**Sauro 2013, which the checker could not reach.** The maintainer's search returned the article at measuringu.com and it was fetched from the returned address: published 26 March 2013; "a much smaller sample of just 77 tree test tasks from 200 users" across three studies, "the average completion rate was 66%", "Consider this result tentative"; "Of the 20 tasks, 17 had higher task completion rates on the tree test!" (preliminary results from two retailers' sites). The unit's section 1.2, row RD-17, figure 1's second row and section 3.1 say what the page says. PASS.

**The checker's repeated fetch.** One fetch (Moran 2020) was cut off by the session's restart and run once more; it was not refused or rate-limited by the site, so it is read as within the web rule and recorded. The writer's unsure line on Moran ("read through a summary") stands as the writer's; the checker confirmed the figures.

**Transcript checks.** This session wrote no agent transcript to disk (no `.jsonl` anywhere under `/root/.claude/` or `/tmp/`), so the scripted transcript checks of the row (tool names, each fetched URL returned by an earlier search, paths, the "model" field) could not be run for any agent. What stands in their place: each agent's own statement of its model and of the tools it used; the checker's `out/log.md` (62 numbered searches and fetches, each fetch after the search that returned its address); the writer's `out/notes.md`. The gap is recorded in the session's record.
