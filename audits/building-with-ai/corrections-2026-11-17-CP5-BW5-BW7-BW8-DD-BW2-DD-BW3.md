Checker: claude-opus-5-5. Corrections check of corrections.md (CP-5), 17 Nov 2026. Read: corrections.md, out/draft.md (20 changes, 6 holds), case-academy.md, the five units in files/ (never edited), briefs/ (BW5, BW7, BW8, DD-BW2, DD-BW3), syllabus-flags.md (F35, F53, F63, F71, F83, F92, F105, F109, F114 to F116, F121, F123, F124), sourcing-standard.md. Method: each Current was counted in the filed unit and in a scratch copy with the earlier changes applied in draft order (all 20 occur exactly once at their turn; each Replacement then occurs once); every case-file line quoted in the draft matches case-academy.md at the line number given; replacements were scanned for em dashes, en dashes and American spellings (none). After changes 1 to 3 the §10 table counts 11 Supported by a count, 4 Consistent, 2 Silent (17), matching the figure (change 4), the closing paragraph (5), unsure item 7's alternative 11/5/1 (6), the Sources line (7) and DD-BW3 §1 (8). F115/F121 effects on DD-BW3: DD-BW2 Deliverable Part 2's wording and grades are unchanged, so DD-BW3 Part D (copied from Part 2) and DD-BW3 §4 (grades from BW10 and DD-BW1) need no edit; the only DD-BW3 text that paraphrases DD-BW2 §10's split is §1, carried by change 8; §4's 'adapted from DD-BW2 §10's three' verdicts stays true. Note on item 2: the only 'Silent' verdicts in DD-BW2 are §10's rows (Part 2 has no verdict column), so the draft's reading of 'Part 2 changes 56 to 58' as the §10 rows is the only one the files allow; which text CP-4's changes 56 to 58 touched cannot be checked from these files. BW9, BW10 and DD-BW1 were not in the packet, so 'contradicts no filed unit' is checked against the five units given. Results: 17 PASS, 3 FAIL (13, 15, 16), with New 13, New 15, New 16.

## Change 1
File: DD-BW2-deep-dive-one-project-with-its-numbers.md, §10 table, row "Guardrails on agent runs"
Current:
````
| Guardrails on agent runs: scopes, budgets, commits (BW9 §7; DD-BW1 rule 7) | Silent | Tools, permission modes, commits and caps not recorded (§7 notes, §9) |
````
Replacement:
````
| Guardrails on agent runs: scopes, budgets, commits (BW9 §7; DD-BW1 rule 7) | Consistent | A checkpoint commit after every agent; caps on agents, searches and attempts on some runs; writers' and page checkers' tool use checked by script where transcripts were kept (§7, added 17 Nov 2026). Not tested: permission modes and spend caps not recorded (§9) |
````
Result: PASS - every element rests on its line: checkpoint commit after every agent (case line 205, §7), caps on agents, searches and attempts (line 206), writers' and page checkers' tool use checked by script where transcripts were kept (line 204), permission modes and spend caps not recorded (line 254, §9). The grade is the unit's own "consistent" (in line with the rule, nothing tests it). Hold 2 confirmed: the §8 counts of line 227 (a chat reverting its own merge; 1 of 39 asks naming a branch) concern concurrent chats, not an agent run whose guardrail failed, so they do not meet "a count of the failure the rule is meant to catch".
Syllabus: no conflict: F115, F121 (DD-BW3 §4 and Part D carry BW10's, DD-BW1's and DD-BW2 Part 2's grades, not §10 verdicts; no effect), F71, F92 (needs now partly met by case file §7), DD-BW2 brief; DD-BW2 §8 "Not recorded" paragraph and Part 1 H (spend caps not recorded; caps on agents, searches, attempts recorded) agree

## Change 2
File: DD-BW2-deep-dive-one-project-with-its-numbers.md, §10 table, row "Usage rules and budgets"
Current:
````
| Usage rules and budgets (BW10) | Silent | No usage, token or cost measure (§7 note, §9) |
````
Replacement:
````
| Usage rules and budgets (BW10) | Supported by a count | Usage limits stopped two sessions, three times in all, one after 18% of the auditing model's weekly allowance (§7, added 17 Nov 2026). Not tested: no usage, token or cost measure per unit (§9) |
````
Result: PASS - "two sessions, three times in all, one after 18% of the auditing model's weekly allowance" is case line 147 exactly (largest history session twice; audit chat of 14 Nov once); "no usage, token or cost measure per unit" is line 247. A limit stop is the failure BW10's rule 10 catches (DD-BW3 §4 table, rule 10: "Heavy tasks stopped by a limit"), so "Supported by a count" meets the unit's definition; the wording matches DD-BW2 §8 ("Usage limits stopped two sessions, three times in all").
Syllabus: no conflict: F115, F121 (no grade in DD-BW2 Part 2 or DD-BW3 §4/Part D changes), F83, F109 (still open on per-unit usage: DD-BW2 Part 2 change 10 "0 measures ... no token measure for a single unit's writing" stays true), DD-BW2 and DD-BW3 briefs

## Change 3
File: DD-BW2-deep-dive-one-project-with-its-numbers.md, §10 table, row "Never the trifecta"
Current:
````
| Never the trifecta (DD-BW1 rule 9; BW9 §8) | Silent | Which tools each agent held is not recorded (§9) |
````
Replacement:
````
| Never the trifecta (DD-BW1 rule 9; BW9 §8) | Consistent | Where transcripts were kept, writers used search and fetch and no connector, memory, Projects or Artifact tool, and page checkers only read, glob and grep inside their folder; the usage-review writer alone was given the past-chat tools (§7, added 17 Nov 2026). Not tested: which tools each agent held, and any injected instruction met, not recorded (§9) |
````
Result: PASS - tool use as recorded is case line 204 verbatim in substance (writers: search and fetch, no connector, memory, Projects or Artifact tool; page checkers: read, glob, grep inside their folder; usage-review writer alone given past-chat tools); "which tools each agent held ... not recorded" rests on line 133 and line 121 (tools held, as against tools used, not recorded) and "injected instruction met" on line 254. Grade "Consistent" is the unit's vocabulary and not stretched (nothing tests the rule).
Syllabus: no conflict: F115, F121, F71, F92 (rule 9 still has no record of tools held), DD-BW2 brief

## Change 4
File: DD-BW2-deep-dive-one-project-with-its-numbers.md, §10 figure (viz block)
Current:
````
  "max": 10,
  "rows": [
    {"label": "Supported by a count", "value": 10, "tone": 3},
    {"label": "Consistent", "value": 2, "tone": 4},
    {"label": "Silent", "value": 5, "tone": 1}
````
Replacement:
````
  "max": 11,
  "rows": [
    {"label": "Supported by a count", "value": 11, "tone": 3},
    {"label": "Consistent", "value": 4, "tone": 4},
    {"label": "Silent", "value": 2, "tone": 1}
````
Result: PASS - counts follow the table after changes 1 to 3, verified by script: 11 Supported by a count, 4 Consistent, 2 Silent (one "Silent", one "Silent (effort); models partly recorded"), total 17; max 11 fits the largest bar; every number is in the closing paragraph (preamble rule: a figure adds no fact). Caption unchanged and still true.
Syllabus: no conflict: course preamble figure rule; F115, F121 (figure not copied by DD-BW3)

## Change 5
File: DD-BW2-deep-dive-one-project-with-its-numbers.md, §10 closing paragraph
Current:
````
Of the seventeen rules, ten are supported by a count, two are consistent with the record and five meet silence. The split is the unit's main finding, and it has a shape: the record supports the rules about checking, and is silent on the rules about cost and control. That follows from what the project chose to count. It counted errors at every check, because the method made checking a stage with a written output; it never counted hours, tokens, effort or tools, because no stage wrote them down. A record supports the rules its stages produce numbers for, and no others.
````
Replacement:
````
Of the seventeen rules, eleven are supported by a count, four are consistent with the record and two meet silence. The split is the unit's main finding, and it has a shape: the record supports the rules about checking with counts from every check, and on the rules about cost and control holds incidents and batch totals, which support one (usage limits stopped sessions) and leave two more consistent with it. That follows from what the project chose to count. It counted errors at every check, because the method made checking a stage with a written output; it never counted hours or effort, or tokens and tools per unit or per agent, because no stage wrote them down; what it holds on them (limit stops, caps, batch token totals, tool use checked where transcripts were kept) comes from the changelogs and the usage review (§7, added 17 Nov 2026; §9). A record supports the rules its stages produce numbers for, and on the rest holds only what someone happened to note.
````
Result: PASS - split 11/4/2 matches the table and figure; "support one (usage limits stopped sessions) and leave two more consistent" matches rows 2, 1 and 3; "never counted hours or effort, or tokens and tools per unit or per agent" is consistent with lines 245 to 247 and 133/121 (tools held per agent not recorded); batch token totals (line 145), limit stops (147), caps (206), tool use checked (204) are cited to §7 added 17 Nov 2026. The closing reading ("holds only what someone happened to note") is the unit's own opinion under §10's "this unit's reading, stated opinion"; minor note: the checkpoint commit of line 205 is a method rule, not a chance note, but it is not among the items the sentence lists, so nothing is misstated.
Syllabus: no conflict: F115 (DD-BW3 §1 paraphrase carried by change 8), F121 (Part 2 untouched), DD-BW2 brief ("what was recorded about cost ... and what was not")

## Change 6
File: DD-BW2-deep-dive-one-project-with-its-numbers.md, Unsure list item 7
Current:
````
which would change the split to 10, 3, 4.
````
Replacement:
````
which would change the split to 11, 5, 1.
````
Result: PASS - arithmetic on the unit's own §10 table after changes 1 to 3: moving "route by tier and effort" from silent to consistent turns 11/4/2 into 11/5/1 (the old 10/2/5 to 10/3/4 used the same move). No case-file line is needed; none is stretched.
Syllabus: no conflict: F115, F121

## Change 7
File: DD-BW2-deep-dive-one-project-with-its-numbers.md, Sources, first bullet
Current:
````
with notes of 15 and 16 Nov 2026: header, §1 to §9.
````
Replacement:
````
with notes of 15 and 16 Nov 2026 and lines added 17 Nov 2026: header, §1 to §9.
````
Result: PASS - case line 140 (§2, "Added 17 Nov 2026 ...") supports "lines added 17 Nov 2026"; the unit already cites "(§..., added 17 Nov 2026)" throughout after CP-4 and changes 1 to 3, 11.
Syllabus: no conflict: DD-BW2 brief; sourcing standard (source named with date)

## Change 8
File: DD-BW3-deep-dive-audit-your-own-usage.md, §1, second paragraph
Current:
````
the record supported the rules its stages produced numbers for, and was silent on the rest (stated opinion, DD-BW2's reading).
````
Replacement:
````
the record supported the rules its stages produced numbers for, and on the rest held only what someone happened to note (stated opinion, DD-BW2's reading).
````
Result: PASS - carries change 5's closing reading into DD-BW3 §1's paraphrase of DD-BW2 §10, as F115 requires in the same pass; the facts behind "held only what someone happened to note" are case lines 147, 204, 205, 206; still labelled "stated opinion, DD-BW2's reading". The sentence's argument (a chat history shows tasks no rule was written for) still holds.
Syllabus: no conflict: F115 (carried), F121 (DD-BW2 Part 2 grades and wording unchanged, so DD-BW3 Part D needs no edit; Part D's column "Grade, as DD-BW2 Part 2 gives it" stays true), DD-BW3 brief; DD-BW3 §4 line "Four verdicts, adapted from DD-BW2 §10's three" stays true (still three verdicts); DD-BW3 §4 "The case" ("DD-BW2 §10 is the only reading of the case against this course's rules") unaffected

## Change 9
File: DD-BW3-deep-dive-audit-your-own-usage.md, Unsure list item 9
Current:
````
9. §2, §6: case file §8 says each ask was classified and gives "number of turns" without defining turn or ask; the unit's sheet (one row per chat, own messages and corrections counted) is its own definition and is not presented as the case's.
````
Replacement:
````
9. §2, §6: case file §8 says each ask was classified by, among other labels, number of turns; its lines added 17 Nov 2026 define a turn as one message on either side, each agent's completion notice included, and §9 says the records define no ask; the unit's sheet (one row per chat, own messages and corrections counted) is its own definition and is not presented as the case's.
````
Result: PASS - case line 105 ("classified by task type, model, outcome and number of turns"), line 237 (§8: a turn is one message on either side; in a chat that runs agents, each agent's completion notice is a turn) and line 259 (§9: no "ask" defined) support every clause; matches DD-BW3 §2 item 4 ("The case's review counted every message on either side as a turn, each agent's completion notice included (case file §8)") and §6 ("They hold no definition of an ask (§9)") as applied by CP-4.
Syllabus: no conflict: F114 (its S-BW note asks for the case's turn beside DD-BW3's own; now consistent), F116, DD-BW3 brief (each label defined and its limits said)

## Change 10
File: DD-BW3-deep-dive-audit-your-own-usage.md, Sources, first bullet
Current:
````
compiled 11 Nov 2026 with notes of 15 and 16 Nov 2026: header, §1, §2, §7, §8, §9.
````
Replacement:
````
compiled 11 Nov 2026 with notes of 15 and 16 Nov 2026 and lines added 17 Nov 2026: header, §1, §2, §5, §7, §8, §9.
````
Result: PASS - case line 140 supports "lines added 17 Nov 2026"; §5 is cited in DD-BW3 §1 ("Academy case file §1, §2, §5, §9", from F123's correction) and was missing from the list; line 43 shows §5 exists. No other case-file section is cited by DD-BW3 and missing (checked: §3, §4, §6 are not cited as case file sections).
Syllabus: no conflict: F123, sourcing standard

## Change 11
File: DD-BW2-deep-dive-one-project-with-its-numbers.md, §2 item 4
Current:
````
From BW7 of this course (16 Nov 2026), a separate agent, the applier, running Opus 5.5, applied the fresh check's findings and could add companion edits a finding implies; writer, checker, applier, filer and corrections checker were each a fresh agent (§2, note).
````
Replacement:
````
From BW1 of this course (15 Nov 2026), a separate Opus 5.5 agent, the applier, applied the fresh check's findings (§2, added 17 Nov 2026); BW7's row record (16 Nov 2026) adds that it could add companion edits a finding implies, and that writer, checker, applier, filer and corrections checker were each a fresh agent (§2, note).
````
Result: PASS - case line 195 (§2, sourced to the method §5, the reports' maintainer notes and the project changelog) gives "until 14 Nov 2026" the filing chat and "from 15 Nov 2026 (this course's BW1)" a separate Opus 5.5 applier; line 119 states what BW7's row record holds and gives no start date for the applier, and its last sentence is answered by line 195. The case file supports BW1 (15 Nov 2026). The replacement restricts line 119's companion-edit and fresh-agent facts to "BW7's row record", which narrows and does not stretch it. BW7 Part 1 (row 4 and step 4) and BW8 §6 already say "from 15 Nov 2026 ... the applier" after CP-4, so this brings DD-BW2 into line with them.
Syllabus: no conflict: F53 (its S-BW note: who applied findings added to the case file), F124 item 4; BW7, BW8 as filed

## Change 12
File: DD-BW2-deep-dive-one-project-with-its-numbers.md, Deliverable Part 1 B, line "Changes while running"
Current:
````
applier agent from BW7;
````
Replacement:
````
applier agent from BW1 (15 Nov 2026);
````
Result: PASS - case line 195, same correction as change 11; the row's source cell ("§3, §6, §2 notes") still covers §2.
Syllabus: no conflict: F124 item 4; DD-BW3 Part B (sets DD-BW2 Part 1 beside the reader's report; holds no applier date)

## Change 13
File: BW7-pipelines-raw-material-to-finished-output.md, Deliverable, conventions paragraph
Current:
````
File paths are this unit's naming, after BW4's Part 3 folders and BW5's `records/`; the case file names no paths.
````
Replacement:
````
File paths are this unit's naming, after BW4's Part 3 folders and BW5's `records/`; the few paths of the case's own that the case file names (`docs/courses-index.md`, `docs/CHANGELOG.md`, `courses/building-with-ai/`, `audits/building-with-ai/`; Academy case file header, §1, §5) are not used here.
````
Result: FAIL - the parenthesis reads as the full list of "the few paths of the case's own that the case file names", but the case file also names `docs/method.md` (case line 3, header, which the change cites) and `docs/project-instructions.md` (line 201, §1, which the change cites, and which change 14 names), and names `audits/building-with-ai/` also in §2 (line 140); line 3: "Compiled on 11 Nov 2026 from the Learning Project's own records (`docs/courses-index.md`, `docs/method.md`, `docs/CHANGELOG.md`, ...)". "Are not used here" is true of the Deliverable's paths (briefs/, packets/, checks/, records/). Corrected text in New 13.
Syllabus: no conflict: F53, F63, BW7 brief

## New 13
File: BW7-pipelines-raw-material-to-finished-output.md, Deliverable, conventions paragraph
Current:
````
File paths are this unit's naming, after BW4's Part 3 folders and BW5's `records/`; the case file names no paths.
````
Replacement:
````
File paths are this unit's naming, after BW4's Part 3 folders and BW5's `records/`; the paths of the case's own that the case file names (`docs/courses-index.md`, `docs/method.md`, `docs/CHANGELOG.md`, `docs/project-instructions.md`, `courses/building-with-ai/` and files under `audits/building-with-ai/`; Academy case file header, §1, §2, §5) are not used here.
````
Result: proposed in place of Change 13; Rests on case lines 3 (header), 122 and 201 (§1), 140 (§2), 135 (§5); a script listing every path in case-academy.md finds these six and no other. Current occurs once at its turn in the sequence.
Syllabus: no conflict: F53, F63, BW7 brief

## Change 14
File: BW8-skills-and-automation.md, Deliverable, conventions paragraph
Current:
````
File paths follow BW4's Part 1 folders and BW7's Part 1 steps, which are those units' proposals; the case file names no paths.
````
Replacement:
````
File paths follow BW4's Part 1 folders and BW7's Part 1 steps, which are those units' proposals; where the case file names the case's own (`docs/courses-index.md`, `docs/project-instructions.md`; Academy case file §1), Deliverable F maps the script's names to them.
````
Result: PASS - case line 201 (§1) names both equivalents; BW8 Deliverable F (line 1264) maps INDEX.md, INSTRUCTIONS.md and BUILD-ORDER.md to `docs/courses-index.md`, `docs/project-instructions.md` and the data file's build-order list, so "Deliverable F maps the script's names to them" is true of the filed unit.
Syllabus: no conflict: F63 (its corrections pass done in Deliverable F), BW8 brief

## Change 15
File: BW5-specifying-a-project.md, §9, "Choosing the boundary"
Current:
````
Academy runs a sample audit every four units (Academy case file §2), which gives a natural boundary. The case file records the method's backlog and proposal rules; it does not record a separate flag mechanism, how often the spec of a course changed, or at which points it was reviewed.
````
Replacement:
````
Academy ran a sample audit every four units (Academy case file §2), a natural boundary, until the owner retired it on 15 Nov 2026 (§9). Beside the method's backlog and proposal rules, the case file records a flag mechanism for this course: a chat that writes a unit raises a flag for each contradiction between units or briefs and each need the syllabus does not meet, and a flag that would change a brief waits for a syllabus review that the owner confirms, with no fixed date set; at 16 Nov 2026 none of 34 flags had been resolved by such a review (§2). It records syllabus reviews on 3 Nov 2026 (the UX course) and 17 Nov 2026 (this course) (§2), and not how often the spec of a course changed.
````
Result: FAIL - "Academy ran a sample audit every four units ... until the owner retired it on 15 Nov 2026" states as practice what the case file records only as the method: two audits ran (case lines 37, 154, 193), "Audits 3 onward of the marketing, AI and UX courses had not run at 11 Nov 2026" (line 113, §9) and, after Audit 2, Audits 3 to 6 "were recorded as owed to a later stage" until the stage was closed (line 218, §9). It also contradicts DD-BW2 §4 ("more audits were due than had run"). The flag-mechanism and syllabus-review sentences rest on lines 116, 140 and 149 and pass. Corrected text in New 15.
Syllabus: no conflict in the flag and review sentences: F35, F124 item 5, BW5 brief ("flags raised during the work, reviewed at a boundary"); conflict in the first sentence with DD-BW2 §4 as filed

## New 15
File: BW5-specifying-a-project.md, §9, "Choosing the boundary"
Current:
````
Academy runs a sample audit every four units (Academy case file §2), which gives a natural boundary. The case file records the method's backlog and proposal rules; it does not record a separate flag mechanism, how often the spec of a course changed, or at which points it was reviewed.
````
Replacement:
````
The method of Academy sets a sample audit every four units (Academy case file §2), a natural boundary; audits 3 onward had not run at 11 Nov 2026, and on 15 Nov 2026 the owner retired the four-unit audit (§9). Beside the method's backlog and proposal rules, the case file records a flag mechanism for this course: a chat that writes a unit raises a flag for each contradiction between units or briefs and each need the syllabus does not meet, and a flag that would change a brief waits for a syllabus review that the owner confirms, with no fixed date set; at 16 Nov 2026 none of 34 flags had been resolved by such a review (§2). It records syllabus reviews on 3 Nov 2026 (the UX course) and 17 Nov 2026 (this course) (§2), and not how often the spec of a course changed.
````
Result: proposed in place of Change 15; Rests on case lines 21 (§2), 113 and 218 (§9), 116, 140 and 149 (§2). Changes 16 and 17 apply after it unchanged in their Current text (New 16 included). Current occurs once at its turn in the sequence.
Syllabus: no conflict: F35, F124 item 5, BW5 brief; agrees with DD-BW2 §4 and BW7 Part 1 (change 18)

## Change 16
File: BW5-specifying-a-project.md, Deliverable Part 1f, closing sentence
Current:
````
The case file records proposals and the backlog-to-changelog move; it does not record a flag mechanism, so the Flags section is this unit's proposal.
````
Replacement:
````
The case file records proposals and the backlog-to-changelog move, and for this course flags that wait for a syllabus review the owner confirms (§2); the Flags section's place in the backlog and its row format are this unit's proposal.
````
Result: FAIL - "for this course flags that wait for a syllabus review the owner confirms (§2)" widens case line 116, which says only that "a flag that would change a brief waits for a syllabus review that the owner confirms"; the line also records how flags are raised ("for each contradiction between units or briefs and each need the syllabus does not meet"), which the replacement leaves out while change 15 states it. Corrected text in New 16.
Syllabus: no conflict: F35, F124 item 5, BW5 brief

## New 16
File: BW5-specifying-a-project.md, Deliverable Part 1f, closing sentence
Current:
````
The case file records proposals and the backlog-to-changelog move; it does not record a flag mechanism, so the Flags section is this unit's proposal.
````
Replacement:
````
The case file records proposals and the backlog-to-changelog move, and for this course flags raised for each contradiction between units or briefs and each need the syllabus does not meet, a flag that would change a brief waiting for a syllabus review the owner confirms (§2); the Flags section's place in the backlog and its row format are this unit's proposal.
````
Result: proposed in place of Change 16; Rests on case lines 24 (§2) and 116 (§2). Current occurs once at its turn in the sequence.
Syllabus: no conflict: F35, F124 item 5, BW5 brief

## Change 17
File: BW5-specifying-a-project.md, §10, method list, "A sample audit every four units"
Current:
````
a unit with more than one sampled claim in ten failing is audited in full (§2). How to set your own threshold is BW6's subject.
````
Replacement:
````
a unit with more than one sampled claim in ten failing is audited in full (§2). On 15 Nov 2026 the owner retired the four-unit audit, leaving the fresh check and the staleness check as the guards (§9). How to set your own threshold is BW6's subject.
````
Result: PASS - case line 21 (§2) is the sentence it follows; line 218 (§9): "on 15 Nov 2026 the owner closed that stage, retired the four-unit audit and left the fresh check and the staleness check as the guards". The list still names the sample audit, as the BW5 brief requires of the worked example.
Syllabus: no conflict: BW5 brief (worked example lists the sample audit), Hold 3

## Change 18
File: BW7-pipelines-raw-material-to-finished-output.md, Deliverable Part 1, "Boundaries"
Current:
````
(case file §2; audits 3 onward had not run at 11 Nov 2026, case file §9)
````
Replacement:
````
(case file §2; audits 3 onward had not run at 11 Nov 2026, and on 15 Nov 2026 the owner retired the four-unit audit, case file §9)
````
Result: PASS - case line 113 and line 218 (§9), each clause as stated; the sentence keeps the four-unit boundary as the case specified it and dates its end.
Syllabus: no conflict: BW7 brief, BW5 §9 (boundaries), Hold 4

## Change 19
File: BW7-pipelines-raw-material-to-finished-output.md, Deliverable Part 1, "Every four units · Boundary"
Current:
````
the method names Fable 5.1 (case file §2).
````
Replacement:
````
the method names Fable 5.1 (case file §2). In the case the owner retired this audit on 15 Nov 2026, leaving the fresh check and the staleness check as the guards (case file §9).
````
Result: PASS - case line 218 (§9), as quoted; the step stays as the procedure specifies it, with the case's retirement added.
Syllabus: no conflict: BW7 brief, Hold 4

## Change 20
File: DD-BW2-deep-dive-one-project-with-its-numbers.md, §4, Audit 2, "What it led to"
Current:
````
The case file records no change of method after Audit 2.
````
Replacement:
````
The case file ties no change of method to Audit 2.
````
Result: PASS - case line 186 (§2) dates method changes after Audit 2's day (29 Oct 2026): next-row prompt (31 Oct), Markdown courses (31 Oct), figures never dropped (3 Nov), corrections in the finding chat (12 Nov), the 15 Nov set including the end of the audit stage; so "records no change of method after Audit 2" is contradicted. Neither line 186 nor line 218 ties a change to Audit 2 (line 218 gives the order of events only), so the replacement is supported.
Syllabus: no conflict: F105, DD-BW2 brief

## Holds
1. DD-BW3 Part D (F121): agree, no edit. Part 2 of DD-BW2 is untouched; §1's paraphrase is carried by change 8 (F115).
2. Guardrails grade Consistent: agree (see Change 1). Case line 227's counts are of concurrent chats and branch naming, not of a guardrail failing on an agent run.
3. BW5 Deliverable 1a outcome 3, 1b's boundaries and §10's flow-figure note: agree, stay a hold. The brief asks for the case 'as it was specified'; with changes 17 and New 15 the prose dates the retirement. Not a change.
4. BW7 Part 1, 'Flags raised by any step wait for one of these': agree, stay a hold; making the syllabus review a boundary changes the procedure's design (BW5 §9, BW7 brief). Not a change.
5. Case file line 119's last sentence: agree; a case-file line, superseded by line 195, for the chat that keeps the case file. Checked: no unit says who applied findings is unrecorded.
6. DD-BW2 Part 2 change 10: agree, still true (case lines 245 to 247; the token totals of line 145 and the stops of line 147 are batch or session figures).

None of the six should become a change. One companion the draft does not propose, offered for the applier's decision: DD-BW2's Part 2 sources line, '*Sources for Parts 1 and 2:* Academy case file §1 to §9, its notes of 15 and 16 Nov 2026 and its header;', occurs once and omits the lines added 17 Nov 2026 that Part 1 now cites (Part 1 B after change 12, case line 195; Part 1 G and H from CP-4). Proposed replacement: '*Sources for Parts 1 and 2:* Academy case file §1 to §9, its notes of 15 and 16 Nov 2026, its lines added 17 Nov 2026 and its header;' (case line 140). It is the same kind of edit as change 7.
