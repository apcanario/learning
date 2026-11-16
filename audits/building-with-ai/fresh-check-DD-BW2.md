---
audit: fresh check
unit: DD-BW2 · Deep dive: one project, with its numbers
course: building-with-ai · Building with AI
model: claude-opus-5-5
date: 2026-11-16
chat: https://claude.ai/code/session_01KMmgR36FFxqBvGbNsHzyhJ
verdict: fix · 2 errors, 12 should-fix, 10 minor
---

The checker's final report, verbatim, from its hand-back. Saved before any finding was applied.

Verdict: DD-BW2 · fix · 2 error, 12 should-fix, 10 minor
claude-opus-5-5. The write to out/findings.md was refused, so the full report is below, verbatim.

# DD-BW2 · Fresh check

Checker: claude-opus-5-5 (Opus 5.5), isolated agent context, packet only. No search was used: the unit is search off and cites no outside page. Audit errata: there is no audit report, so this step was skipped. All arithmetic was re-run by script (python3), and the 36-row table matches case file §5 cell for cell.

## Findings

[error] [accuracy] §2; Current: "Checks were added after leaks."; Problem: the heading states an order that the case file says it does not hold. The body of the same item says the record does not date the check against the structure audit, and the index check the item also lists is not tied to any leak; Fix: "Checks were added; the record does not date them."; Basis: Academy case file §7 note: "The record does not say when the check was added relative to the structure audit."
[error] [accuracy] §10; Current: "Not tested: no self-check by the writer to compare"; Problem: the case file records a writer's self-check before every hand-in: the writer's own pass against the sourcing checklist. What is missing is a count of what that pass caught, so the cell misstates the method; Fix: "Not tested: the writer's own pass ran before every fresh check (§2), and the record holds no count of what it caught"; Basis: Academy case file §2: "The writer's own pass. Before handing in, the writer runs the sourcing checklist and lists up to ten claims it could not verify."; §5: "Counts are the checker's findings on the writer's handed-in draft."
[should-fix] [accuracy] §2; Current: "at 16 Nov 2026, of 34 flags raised by then"; Problem: 34 is the count before BW5's flags were added, covering flags from the course's creation and BW1 to BW4. "Raised by then" makes it the count at 16 Nov, when BW5 to DD-BW1 had also run; Fix: "at 16 Nov 2026, before BW5's flags were added, of 34 flags raised at the course's creation and by BW1 to BW4"; Basis: Academy case file §2 note: "At 16 Nov 2026, before BW5's flags were added, 34 flags had been raised (at the course's creation and by BW1 to BW4): 26 open, 7 carried, 1 resolved by a correction"
[should-fix] [accuracy] §5; Current: "three missing deliverables from three units written off one research report (§3)"; Problem: this is given as a batch "from one cause", but the case file names no cause for the missing deliverables. It records the research report as the units' source and the missing deliverables as a reason for the verdict, separately; Fix: "three missing deliverables in the three units written from one research report (§3; the case file does not name the cause)"; Basis: Academy case file §3: "The first three marketing units were written from one research report produced by research agents across five tracks." and "the three deliverables did not exist"
[should-fix] [accuracy] §5; Current: "These are the only counts in the record of a checker's output being wrong, and they cover two rows."; Problem: only the applier's held fixes are a checker's output. The corrections-check failures were replacements the writer proposed, and DD-BW1's one failure was a replacement that could not be checked, not one shown to be wrong; Fix: "These are the only counts in the record of a proposed fix, the checker's or the writer's, being held or failed, and they cover two rows."; Basis: Academy case file §2 notes: "failed 1 that the writer had proposed to an earlier unit"; "failed 1, an author line, because no search returned the address the replacement cited, so it could not be checked"
[should-fix] [accuracy] §7; Current: "Every one is a failure of the record, not of the text: a run whose work survived only in files, a check with no evidence of what was read, a model name that did not say what ran, a report that reached its file by an unplanned path. In each case the text itself was recovered or re-checked."; Problem: the table above lists six failures. Private terms reaching a public build is a leak in the published output, not a failure of the record, and the case file does not say it was recovered or how. The sentence also uses a "not X" construction, which the brief bars; Fix: "Four of the six are failures of the record: a run whose work survived only in files, a check with no evidence of what was read, a model name that did not say what ran, a report that reached its file by an unplanned path. The other two are not: a main chat that ran on another model than the one asked for, which the record caught (§2, notes), and private terms reaching a public build, a leak in the output whose fix the case file does not describe (§7)."; Basis: Academy case file §7: "private terms reaching a public build"; §7 note: "The record does not say when the check was added relative to the structure audit."
[should-fix] [accuracy] §9; Current: "Its counts are the project's counts of its own work, and nobody outside checked them."; Problem: the case file does not say that nobody outside checked its counts. It says only that it was compiled from the project's own records; Fix: "Its counts are the project's counts of its own work, and the case file records no outside check of them."; Basis: Academy case file header: "Compiled on 11 Nov 2026 from the Learning Project's own records"
[should-fix] [label] §4; Current: "so on the method's own schedule more audits were due than had run."; Problem: this is an inference (37 units against "a sample audit every four units") presented as the method's own verdict. The case file does not say whether the schedule counts units per course or across courses; Fix: "so, on this unit's reading of the method's schedule (the case file does not say whether it counts units per course or across courses), more audits were due than had run."; Basis: Academy case file §2: "A sample audit every four units."; §9: "Audits 3 onward of the marketing, AI and UX courses had not run at 11 Nov 2026."
[should-fix] [label] Deliverable Part 2, change 1; Current: "| Documented practice (vendor), on measured self-preference evidence (BW2 §5) |"; Problem: the column is "the grade of the rule in the unit named", and BW2 §5 grades the rule as stated opinion. The grade "documented practice, vendor" belongs to DD-BW1 rule 3, and BW6 §4 labels its source that way; Fix: "| Stated opinion on measured self-preference evidence (BW2 §5); documented practice, vendor (BW6 §4; DD-BW1 rule 3) |"; Basis: BW2 §5: "The rule this course uses (stated opinion, on the findings above)"; DD-BW1 Part 2 rule 3: "Documented practice, vendor; no figures"
[should-fix] [deliverable] Deliverable Part 2; Current: "| 3 | **Record every finding's fate"; Problem: the ranking rule is "by the number of recorded items behind the change, largest first". Change 3 rests on 8 items (6 held fixes and 2 failed replacements) and change 4 on 10 stale claims, so under the unit's own rule change 4 ranks above change 3. Companion edit: "| 4 | **On any STALE" becomes "| 3 | **On any STALE", and the two rows swap places; Fix: "| 4 | **Record every finding's fate"; Basis: unit, Part 2 ranking rule; Academy case file §4 ("Ten claims were stale"), §5 notes (4 of 18; 2 of 35) and §2 notes (1 of 5; 1 of 8)
[should-fix] [figure] §3, stacked bars caption; Current: "The courses differ in subject, length and checker model, so the bars compare nothing causal."; Problem: "length" is a fact in the caption that the text does not state, since the text gives no length per course. The checker models also overlap across courses. A figure adds no fact; Fix: "The courses differ in subject, units, dates and checkers, and there is no control (§3), so the bars compare nothing causal."; Basis: unit §3: "units, courses and dates differ, and there is no control (case file §9)"
[should-fix] [attribution] §6; Current: "a figure adds no fact (the sourcing standard, Part 1)"; Problem: "Part 1" is a section of the project's internal checklist, which this course's reader cannot open. Filed units cite the rule as the course's sourcing standard in its shared preamble, and the case file records the same rule; Fix: "a figure adds no fact (the course's shared preamble; Academy case file §6: every label and number must already be in the text)"; Basis: BW6 §3: "(the course's sourcing standard, in its shared preamble)"; Academy case file §6: "every label and number must already be in the text"
[should-fix] [attribution] Sources; Current: "- The course's sourcing standard, Part 1 ("a figure adds no fact")."; Problem: the same locator the reader cannot open; Fix: "- The course's shared preamble, its rule for figures ("a figure adds no fact"), and Academy case file §6."; Basis: BW6 §3; Academy case file §6
[should-fix] [attribution] §11; Current: "BW6 §8 records Gemini CLI's documented subagents with their own context window and OpenAI's equivalent as not checked (16 Nov 2026)"; Problem: the On other tools section must cite the other vendor's own documentation for each equivalent, as a link, and the Gemini page is named only through BW6. Companion edits: add to Sources "- Google, *Subagents*, Gemini CLI documentation, https://geminicli.com/docs/core/subagents/ (vendor; read 16 Nov 2026 for BW6 §8, not re-read for this unit)." and change the closing line "This unit cites no outside page:" to "This unit cites one outside page, as BW6 §8 read it:"; Fix: "BW6 §8 records Gemini CLI's subagents, each with an "Independent context window" ([*Subagents*, Gemini CLI documentation](https://geminicli.com/docs/core/subagents/); vendor, read 16 Nov 2026 for BW6), and OpenAI's equivalent as not checked"; Basis: BW6 §8 table row "A fresh subagent for review"; sourcing standard Part 6: "cites the other vendors' own documentation for each equivalent, or says none was found"; "Links are given as links"
[minor] [accuracy] §8; Current: "No effort setting for any unit (§9). No budget or stop on any agent run (§9)."; Problem: the case file says only that the record does not show these, but the sentences read as if none existed; Fix: "No record of the effort setting for any unit (§9), or of any budget or stop set on agent runs (§9)."; Basis: Academy case file §9 note: "The record does not say whether the owner reads each unit before publishing, any budget or stop set on agent runs, which tools and connectors each agent held, or the effort setting used for each unit"
[minor] [attribution] §10; Current: "(sourcing standard Part 1; BW7 §6)"; Problem: an internal locator the reader cannot open (see the §6 finding); Fix: "(the course's shared preamble; BW7 §6)"; Basis: BW6 §3
[minor] [attribution] Deliverable Part 2, change 5; Current: "| BW7 §6; sourcing standard Part 1 |"; Problem: the same internal locator; Fix: "| BW7 §6; the course's shared preamble |"; Basis: BW6 §3
[minor] [style] §7; Current: "Not the text but the machinery around it"; Problem: a "not X but Y" construction, which the brief's tone rule bars; Fix: "The machinery around the text"; Basis: brief preamble: "no 'not X but Y' constructions"
[minor] [label] §4; Current: "That is the largest single change in the record, and it was made on one audit of three units."; Problem: "largest" is the unit's own judgement and is not labelled as one. Audit 1 also covered four units, not three: it passed the first AI unit as well; Fix: "On this unit's reading, that is the largest single change in the record, and it was made on one audit's findings on three units (the same audit passed a fourth)."; Basis: Academy case file §3: "The same audit passed the first AI unit: seven of seven sampled claims held."
[minor] [accuracy] §7 table; Current: "Each report reached its file only through the main chat, which saved it verbatim from the agent's reply"; Problem: BW1's note says the chat saved the report from the reply and does not say "verbatim". BW10's note says only the fresh checker's report was saved verbatim; Fix: "Each report reached its file only through the main chat, which saved it from the agent's reply (verbatim, on the records of BW9, BW10 and DD-BW1)"; Basis: Academy case file §7 notes: "the chat saved the report from the checker's reply" (BW1); "the chat saved the fresh checker's report verbatim from its reply" (BW10); "the chat saved the reports verbatim from their replies" (DD-BW1)
[minor] [accuracy] opening; Current: "one person, one family of models, no control and no second project (case file §9)"; Problem: §9 holds no control, no second project and no second person. "One family of models" comes from §1 ("with Claude") and §2, not from §9; Fix: "one person, one vendor's models (case file §1, §2), no control and no second project (case file §9)"; Basis: Academy case file §1: "built by one person with Claude"; §9: "No control" / "No second project and no second person."
[minor] [accuracy] §11; Current: "BW2 §7 builds its re-decision rule on it."; Problem: BW2 §7 lists the "fable" resolution as one dated instance among four kinds of change; the rule does not rest on it alone; Fix: "BW2 §7 lists it among the four triggers of its re-decision rule."; Basis: BW2 §7 table, row "A name that resolves to a newer model, or a benchmark that changes version"
[minor] [label] Deliverable Part 2, change 4; Current: "**On any STALE, sweep every claim read from the same page or version, across all units,** and date each again."; Problem: BW6 §5's sweep covers one text. "Across all units" is this unit's extension and is not marked as such; Fix: "**On any STALE, sweep every claim read from the same page or version, across all units,** and date each again (the sweep across units is this unit's extension of BW6 §5's sweep within one text)."; Basis: BW6 §5: "it triggers a sweep of every fact in the text that can change"
[minor] [accuracy] §8; Current: ""accepted" was a proxy for a good outcome"; Problem: the case file says only that "accepted" was a proxy; "for a good outcome" is the writer's addition; Fix: ""accepted" was a proxy"; Basis: Academy case file §8: "The labels were applied by hand; "accepted" was a proxy; 14 endings were not seen."

## Confirmed

- §1: five courses, history courses of 78 and 79 reports, marketing 11, AI 11, UX 15, 194 units (case file §1: "two history courses (78 and 79 long-form reports), a marketing course (11 units), an AI course (11 units) and a UX course (15 units): 194 units"). PASS; 78+79+11+11+15 = 194 by script.
- §1: 2,000 to 6,000 words by guide; the longest UX unit about 16,900 words; one private repository; site built by script with no page styled by hand (case file §1). PASS.
- §1: 157 history units (78+79, by script). PASS. "No total of words written" and "no start date" are both absent from the case file. PASS.
- §1: BW1 to BW10 and DD-BW1 in the folder by 16 Nov 2026 (case file §1 note: "holds BW1 to BW10 and DD-BW1"). PASS. Reading-page introduction (case file §1 note: "opens with an introduction that says the unit was written by an AI model and names the model..."). PASS.
- §2 "As written": every stage matches the case file §2 lines on syllabus, brief, one context ("leaked context is how a course starts repeating itself"), the writer's pass ("up to ten claims"), fresh check, an audit every four units, staleness at six months, Opus 5.5 writing and Fable 5.1 auditing, and backlog and changelog. PASS.
- §2 item 1: the quotation "from then on every unit of that family got a fresh check before filing" is verbatim (case file §3). PASS. The first AI unit predates the rule (§5 header). PASS.
- §2 item 2: Fable 5.1 on 19, Opus 5.5 on 12, Fable 5.2 on 5 (counted by script from the §5 table). PASS. The method names no fresh-check model: the §2 "Models" line names only the writer and the auditor. PASS (unsure item 2).
- §2 item 3: the early figure rule, two figures dropped, the owner's later rule (case file §6). PASS.
- §2 item 4: the applier from BW7 on, Opus 5.5, companion edits; the record is silent on who applied findings earlier (case file §2 note: "The record does not say who applied the findings for the earlier units of §5"). PASS.
- §2 item 5: BW10 and DD-BW1 asked for Sonnet 5.5 and ran Opus 5.5; DD-BW1 was the second of three rows in one main chat (case file §2 notes). PASS.
- §2 item 6, body: the private-terms script and checker; the index check restores every file (case file §7 note; §1 note). PASS. The heading is wrong (see the first error).
- §2 flags: 26 open, 7 carried, 1 resolved by a correction, none by a syllabus review; 26+7+1 = 34 (by script). PASS, apart from the date finding.
- §3 table: all 36 rows equal case file §5 (course, checker, verdict and the three counts), compared by script, with the private unit codes replaced by row numbers. PASS. BW10 0/7/11 and DD-BW1 3/20/12 (case file §5 notes). PASS.
- §3 totals: 58, 237, 303 and 598; 31 fix, 4 keep, 1 rewrite (by script). PASS.
- §3 arithmetic, all by script: 28/36 = 77.8%; 15/20 = 75%; 58/36 = 1.6; 598/36 = 16.6; range 8 to 34; 9.7%, 39.6% and 50.7%; drafts by error count 8, 9, 9, 9, 1; of the 8 error-free drafts, 4 keep and 4 fix; every keep had 0 errors; the rewrite (row 17) had 4. PASS.
- §3 by course: Marketing 8 of 11, 15/71/81; AI 8 of 10, 17/58/89; UX 12 of 15, 26/108/133 (by script). PASS.
- §3 "cannot be read for": BW6 §4 says so ("they compare nothing, since units, courses and dates differ and there is no control"), and so does BW2 §5 ("the counts compare nothing"). PASS.
- §4 Audit 1: 1 of 8 sampled failed; full audit, 23 of 91 failed, none stale, nothing invented, no conclusion flipped; rewrite for two reasons; the quoted pattern "qualifiers the source does not carry"; the first AI unit held 7 of 7; the units were rewritten the same day (case file §3). PASS.
- §4 Audit 2: 4 units, 28 sampled, 96 checked; one incidental failure (a miscited caption); ten stale claims in one unit from one benchmark version change; all passed; 26 errata the same day (case file §4). PASS. BW6 Deliverable H marks the date, units, model and stale-in-sample as UNKNOWN. PASS.
- §4: 37 units = 11+11+15 (by script); Audits 3 onward had not run (case file §9). PASS. The inference needs a label (see finding).
- §5 table: every kind matches the case file §5 list and §3, §4. "3 of DD-BW1's 3 errors" matches the §5 note ("all three in figures that carried facts the text did not"). 4 of 18 and 2 of 35 match the §5 notes (18 = 0+7+11 and 35 = 3+20+12, by script). 1 of 5 and 1 of 8 match the §2 notes. PASS.
- §5: BW6 §2 draws the rule that a check opens the source ("Existence is the first test, never the last"); BW6 §5 stratifies and sends a STALE to a sweep. PASS.
- §6: figures declared as data; a separate agent checks each; every label and number must be in the text; a failed figure is fixed and re-checked by a new agent; two dropped; the sitemap passed on its eighth check (case file §6). BW7 §8, table stage 7, says "model not recorded". PASS.
- §7 table: lost writers; missing transcripts; the "fable" resolution and re-owed checks; refused writes on 4 rows (BW1; BW9's fresh checker and two corrections checkers; BW10; DD-BW1); private terms as one of seventeen findings; instructions that paraphrased the method (case file §7 and notes). PASS. BW9 §9 says "No rule is recorded" for the lost writers. PASS. BW4 §7 reads the two findings. PASS.
- §7 publish: the site is published in two places, artifact then GitHub Pages; no repeated publish is recorded (case file §1 note). PASS.
- §8: 53 chats over six days, 31/18/4 (sum 53, by script); labels applied by hand; 14 endings not seen; the ten changes not listed (case file §8). PASS. Six agents a row on BW10 and DD-BW1 (case file §2 notes). PASS. "The same day" for Audit 1's rewrites and Audit 2's errata (§3, §4). PASS. No hours or money (§9); no plan, token or window measure (§7 note). PASS.
- §9: no control, no second project, no second person (§9). BW5 §10, BW7 §8 and BW9 §9 each say the method is not shown to beat a lighter one. PASS. BW5 §10 and BW6 §7 both say the case file does not record whether Audit 2's units had a fresh check. PASS.
- §10: verdict counts of 10 supported, 2 consistent and 5 silent, out of 17 (counted from the table). PASS. Pointers checked: BW2 §5; BW6 §2 to §6; BW1 §4 (date every fact, as BW6 §2 reports it); BW5 Deliverable 1d (it exists: "1d · Done-when lines, on the case"); BW7 §2, §6 and §7; BW4 §7; BW9 §7 (deterministic controls); DD-BW1 rules 2, 3, 6, 7 and 9. PASS.
- §11: BW2 §8 cites vendor pages read 15 Nov 2026, none of them on model-name resolution; BW9 §10 covers permission modes, subagents and checkpoints; one check was run from a Claude Code session on claude.ai (case file §7 note). PASS.
- Deliverable Part 2 grades checked against the units named:
  - change 2: BW6 §2, "stated opinion, built on the case and on Walters and Wilder's finding". PASS.
  - change 3: BW6 §6, "stated opinion, built on §4 and §5". PASS.
  - change 4: BW6 §5, stated opinion. PASS.
  - change 5: BW7 §6, "this unit's adaptation, stated opinion" of Airflow practice. PASS.
  - change 6: BW7 §2, "stated opinion, on the sources below". PASS.
  - change 7: DD-BW1 rule 2, "Documented practice". PASS.
  - change 8: BW7 §7, "this unit's form, stated opinion". PASS.
  - change 9: BW4 §7, "only a check on the output does (stated opinion)". PASS.
  - change 10: BW10 §1, no allowance published. PASS.
- "205" = 194 + 11 and "38" = 36 + 2 (by script); the unit states how both were derived. PASS.
- Unsure list: items 1, 2, 4, 5 and 7 to 9 are checked above. Item 3 (row order) is stated in the unit. For item 6, see the §11 finding.

## (1) Coverage

- What was built, by count: covered (§1, figure 1).
- The method as run: covered (§2), with its changes in order.
- Errors per unit at the fresh check, as a table: covered (§3: 36 rows plus BW10 and DD-BW1; BW1 to BW9 marked as absent from the case file).
- What each sample audit found and what it led to: covered (§4).
- Kinds of error that recur: covered (§5). The record holds no counts by kind, and the unit says so.
- Figures that failed their checks and what fixing them took: covered but thin, because the record is thin (§6); the gaps are stated.
- What failed in operation: lost agents and restarts are covered. The repeated publish is covered as "none recorded" (§7).
- Cost in chats and time, recorded and not: covered (§8).
- What one person's record cannot show: covered (§9).
- Labelled as an anecdote: covered (opening, figure captions, Part 1 header).
- Deliverable: the case report and ten ranked changes, each with its count and unit, are covered. The ranking order breaks its own rule once (see finding).
- Preamble requirements:
  - "(Academy case)" on first use: covered.
  - Evidence grades: covered.
  - On other tools: thin. It points through other units, and one vendor link is missing (see finding).
  - Template blanks say what goes in them: covered.
  - Links as links: the unit cites no outside source, so none are required apart from the §11 finding.
- Takes line: B6's count is used through the case file without naming the private unit. The staged records (fresh-check reports, audit reports, changelog) were not in the writer's packet (the writer's Contradiction 2), so no finding quotes them.

## (5) Deliverable

Present in full:
- Part 1 is the case report, sections A to I, with every line carrying a count or "not recorded" and a case-file section.
- Part 2 gives ten ranked changes, each with its count, unit and grade.
- Parts 3 and 4 are templates whose blanks say what goes in them.

It follows from the evidence: every Part 1 value traces to the case file, and every Part 2 change rests on a count in §3 to §8. Two fixes are needed: the order of changes 3 and 4 contradicts the stated ranking rule, and change 1's grade misreads BW2 §5. Usable alone: yes. Part 4 restates the ranking rule and that a change with no count stays off the list.

## (7) Figures

1. §1, compare, "Units written per course". Its labels and values (78, 79, 15, 11, 11; 194; 11 Nov 2026) are all in §1: "two history courses of 78 and 79 long-form reports, a marketing course of 11 units, an AI course of 11 units and a UX course of 15 units, 194 units in all". The caption names §1, case file §1 and the anecdote label. The kind fits (numbers compared). PASS.
2. §3, compare, "drafts by number of errors". Values in §3: "8 drafts had none, 9 had one, 9 had two, 9 had three and 1 had four". The caption names §3 and case file §5. The kind fits. PASS.
3. §3, bars (stacked), "findings by grade and course". The values and labels are in §3: "Marketing: 8 of 11 drafts with an error; 15 errors, 71 should-fix, 81 minor. AI: 8 of 10; 17, 58, 89. UX: 12 of 15; 26, 108, 133."; "All findings together number 598". The kind fits. FIX: the caption adds "length", which is not in the text. Replacement caption: "Fresh-check findings by grade and course, 598 in all: §3 of this unit, summed from the table in Academy case file §5. The courses differ in subject, units, dates and checkers, and there is no control (§3), so the bars compare nothing causal."
4. §10, compare, "rules by verdict". Values in §10: "Of the seventeen rules, ten are supported by a count, two are consistent with the record and five meet silence." The caption names §10 and the case-file sections, with the anecdote label. The kind fits. PASS.

## (9) Sourcing standard, Part 1 and Part 6

Part 1
- Sourced where made: yes; every case fact carries its section.
- Source can be opened: the case file and the filed units are cited by code and section. "Sourcing standard, Part 1" cannot be opened by this reader (see findings).
- Source says what the claim says: no in two places (the errors on the §2 heading and the §10 writer's self-check). Claims go beyond the source in §5, §7 and §9 (should-fix findings).
- Cited for what it says itself: yes.
- Every number says whose figure it is: yes. Every count is the case file's or this unit's arithmetic on it.
- View attached to a named person: none.
- Quotation marks hold exact words: "from then on every unit of that family got a fresh check before filing" and "qualifiers the source does not carry" are exact. "accepted" is exact, but the unit adds a gloss to it (minor).
- Nothing invented: yes.
- A figure adds no fact: figure 3's caption adds "length" (see finding); the others pass.
- Illustrations: none.
- Unsourced claims said to be unsourced: yes, at length ("not recorded").
- Search flag: off; the unit states no changeable fact of its own.
- Sources listed: the case file and the units are listed. The sourcing-standard entry needs re-pointing, and the Gemini page must be added if the §11 fix is applied.
- Closing material agrees with the body: yes, apart from the ranking order.

Part 6
- Every number, mechanism and recommendation sourced: yes.
- Source classes: the case file (an anecdote) and the course's units; no outside class is used.
- Evidence grade per practice: yes (the Part 2 column; the readings in §5, §7 and §10 are labelled stated opinion). Change 1's grade misreads its unit (see finding).
- Study findings name their models and task: no study is cited directly.
- Product facts dated: the unit states none of its own; the model names are case facts.
- On other tools: present, but it cites vendor documentation only through other units (see finding).
- Carried-over claims re-verified: B6's count is taken from the case file, not from the private unit. Yes.
- Nothing about the private course's reader, and no reference to the private course or its units: none found (a scan for private unit codes, names and places came back clean). The case file's generic "marketing course", "AI course" and "history courses" are used as the case file allows.
- Academy facts are in the case file, cited, labelled "(Academy case)" on first use and as an anecdote, and never the only support for a general claim: yes, apart from the two errors and the flagged inferences.
- No uncited figures, invented names or invented quotations: yes.
- Deliverable built on the case, then as a template: yes.
- Reads as advice without evidence: no; every change is tied to a count.
- Links as links: not applicable, apart from §11.

## (10) Read as the brief's reader

- Locators the reader cannot open: "the sourcing standard, Part 1", in four places (see findings). "This unit's notes" in the opening points to a file the reader cannot see. Filed units use the same wording (BW6 §6), so it is course style and not a finding.
- Project jargon not defined for this reader: "staged packets" (§2 item 5) and "corrections checker" (§2 item 4, explained only in §5). "Row" is defined through BW5. Minor; no finding raised.
- Private material: nothing is revealed beyond what the case file holds. The private units appear as rows 1 to 36 with their codes removed. The flags note, the filing chats and the model names are all in the case file. Nothing found that the case file treats as private.

## Writer's Source errors list

The writer's list is "none". This check found no error in the case file or in a filed unit that the unit should have reported.

Verdict: DD-BW2 · fix · 2 error, 12 should-fix, 10 minor
