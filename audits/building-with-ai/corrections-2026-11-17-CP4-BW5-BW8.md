Checker: claude-opus-5-5. Corrections check of corrections.md (CP-4, BW5 to BW8), 17 Nov 2026. Packet only; no web. All 38 Currents occur exactly once in their files and the changes apply in sequence (checked by script); each New block's Current also occurs once at its point in the sequence. No replacement holds an em dash; British spelling throughout ('Customize > Skills' is a product label). Result: 34 PASS, 4 FAIL, 4 New. No change alters a brief. Change 2 passes only together with Change 15's replacement New 15. Private-terms note: kit/private_terms.py is not in this packet; Changes 1, 2, 5, 14, 15, 16, 17 (and New 15) carry private-course unit codes, course names or "the private courses" from the case file, so the filer runs the script before filing.

## Change 1
File: BW5-specifying-a-project.md, 6 · The decision log (F35)
Current:
````
The case file holds no dates for these decisions.
````
Replacement:
````
The case file dates two of them: the per-unit fresh check made a rule for the marketing and AI courses after Audit 1 on 28 Oct 2026, and figures fixed until they pass, never dropped, on 3 Nov 2026 (Academy case file §2); it gives no date for the early figure rule or for the model-version decision.
````
Result: PASS. Case file §2 (Decision dates) dates the per-unit fresh check (28 Oct 2026) and figures fixed until they pass (3 Nov 2026), and dates neither the three-failure rule nor anything on the named model version. Reads in place after the list of three decisions.

Syllabus: no conflict: F35 (decision dates). No brief contradicted; agrees with Changes 10 and 11 in the same unit.

## Change 2
File: BW5-specifying-a-project.md, 10 · The Academy case's method, as the worked example (F47 (companion, so that BW5 and BW6 agree; BW6 points here))
Current:
````
The second audit's four units all passed (§4); the case file does not say whether those four had a fresh check, so nothing here says the check caused the pass.
````
Replacement:
````
The second audit's four units, B2, B3, B4 and A1, all passed (§4), and all four are among the 36 that had a fresh check before filing (§5); with no unit written without the method to compare (§9), nothing here says the check caused the pass.
````
Result: PASS. Judged with Change 15. Case file §4 (Audit 2) names B2, B3, B4 and A1; all four are rows of the §5 table of the 36 units fresh-checked before filing; §9 records no control. The conclusion (nothing says the check caused the pass) is unchanged. Needed so that BW5 §10 and BW6 §7 (which points here) do not contradict each other once Change 15 or New 15 is applied; apply only with one of them.

Syllabus: no conflict: Companion to F47/F105 via Change 15 / New 15. No brief contradicted. Unit codes and 'the private courses' are taken from the case file, which is compiled with private details removed; kit/private_terms.py is not in this packet, so the filer runs it after applying.

## Change 3
File: BW5-specifying-a-project.md, Deliverable · A one-page spec, a build order, a unit brief, done-when lines and a decision log > 1a · The one-page spec (`SPEC.md`) (F35)
Current:
````
[NOT IN CASE FILE: the reader of any course.]
````
Replacement:
````
This course's reader: an experienced professional who reasons and writes well, uses a chat assistant with no method, may not write code, and brings one real project (§2). [NOT IN CASE FILE: the reader of the other courses.]
````
Result: FAIL. Facts correct (case file §2, this course's reader). But inside the reconstructed SPEC.md, whose subject is Academy, 'This course's reader' has no antecedent: it can be read as the reader of every Academy course. Naming the course fixes it; see New 3.

Syllabus: no conflict: F35 (the reader). No brief contradicted; the wording matches the case file's paraphrase of the preamble, not the brief's longer text, and says it is the case file's.

## Change 4
File: BW5-specifying-a-project.md, Deliverable · A one-page spec, a build order, a unit brief, done-when lines and a decision log > 1a · The one-page spec (`SPEC.md`) (F35, F63)
Current:
````
(BW4, Part 3; the case file does not record Academy's own layout)
````
Replacement:
````
(BW4, Part 3; in Academy's own layout no file named INDEX.md, INSTRUCTIONS.md or BUILD-ORDER.md appears in the records, and their equivalents are `docs/courses-index.md`, `docs/project-instructions.md` and each course's build order as a list in its data file, §1)
````
Result: PASS. Case file §1 (Layout names) states exactly this. The old clause 'does not record Academy's own layout' is no longer true (§1, Layout and Layout names). Reads in place as a parenthesis to the rules-folder pointer, and agrees with Change 38 in BW8.

Syllabus: no conflict: F35, F63. No brief contradicted; consistent with BW8 Deliverable F after Change 38.

## Change 5
File: BW5-specifying-a-project.md, Deliverable · A one-page spec, a build order, a unit brief, done-when lines and a decision log > 1b · The build order (`BUILD-ORDER.md`) (F35)
Current:
````
and no course's unit list.
````
Replacement:
````
and one unit list: the two private courses' 22 units in build order, with the date each was written (Academy case file §1); it gives no Takes or Gives for them.
````
Result: PASS. Case file §1 (One course's build order): 22 units in build order with their dates; counted 22 codes. The line gives codes and dates only, so 'no Takes or Gives' is correct, and the next sentence (worked on this course instead) still follows.

Syllabus: no conflict: F35 (a course's unit list in build order with Takes and Gives). No brief contradicted. Unit codes and 'the private courses' are taken from the case file, which is compiled with private details removed; kit/private_terms.py is not in this packet, so the filer runs it after applying.

## Change 6
File: BW5-specifying-a-project.md, Deliverable · A one-page spec, a build order, a unit brief, done-when lines and a decision log > 1c · A unit brief, on the case (F35)
Current:
````
The case file describes both and holds the text of neither, so the preamble's contents are marked.
````
Replacement:
````
The case file describes both and holds the text of neither; for this course it gives the reader and the goal (§2), and the rest of the preamble's contents are marked.
````
Result: PASS. Case file §2 gives this course's reader and goal; §9 says the case file holds no private brief text and this course's preamble is held in its data file, not quoted. Reads in place before the preamble block that Changes 7 and 8 fill.

Syllabus: no conflict: F35 (preamble text). No brief contradicted.

## Change 7
File: BW5-specifying-a-project.md, Deliverable · A one-page spec, a build order, a unit brief, done-when lines and a decision log > 1c · A unit brief, on the case (F35)
Current:
````
    READER: [NOT IN CASE FILE: the course's reader, as the preamble states it]
````
Replacement:
````
    READER: an experienced professional who reasons and writes well, uses a chat assistant with no method, may not write code, and brings one real project (as the case file gives it, §2)
````
Result: PASS. Verbatim from case file §2 (line 115). Indentation kept for the code block.

Syllabus: no conflict: F35. Matches the BW5 brief's reader in substance (the brief's wording is longer; the line says it is the case file's).

## Change 8
File: BW5-specifying-a-project.md, Deliverable · A one-page spec, a build order, a unit brief, done-when lines and a decision log > 1c · A unit brief, on the case (F35)
Current:
````
    GOAL: [NOT IN CASE FILE: the course goal in one sentence]
````
Replacement:
````
    GOAL: by the end of the course the reader can say what the model saw when an output fails; brief a task so that the first output is usable and keep a project structure that does not rot; verify AI-written work by sample before trusting it; and decide what to hand to an agent, with one real project of their own specified and running (as the case file gives it, §2)
````
Result: PASS. Verbatim from case file §2 (line 115).

Syllabus: no conflict: F35. No brief contradicted.

## Change 9
File: BW5-specifying-a-project.md, Deliverable · A one-page spec, a build order, a unit brief, done-when lines and a decision log > 1e · The decision log (`records/decisions.md`), on the case (F35)
Current:
````
lost writers can be resumed from working files (§7) | [NOT IN CASE FILE] |
````
Replacement:
````
lost writers can be resumed from working files (§7) | [NOT IN CASE FILE: the one-chat rule's date]; an isolated agent context counted as a new chat from 29 Oct 2026 (§2) · [NOT IN CASE FILE] |
````
Result: PASS. Case file §2 (Decision dates): an isolated agent context counts as a new chat, 29 Oct 2026; no date for the one-context rule itself. The cell keeps the 'date · re-check by' form.

Syllabus: no conflict: F35 (decision dates).

## Change 10
File: BW5-specifying-a-project.md, Deliverable · A one-page spec, a build order, a unit brief, done-when lines and a decision log > 1e · The decision log (`records/decisions.md`), on the case (F35)
Current:
````
28 drafts had at least one error (§5) | [NOT IN CASE FILE] |
````
Replacement:
````
28 drafts had at least one error (§5) | 28 Oct 2026 (§2) · [NOT IN CASE FILE] |
````
Result: PASS. Case file §2 (Decision dates): 28 Oct 2026 for the per-unit fresh check. Attached to D2, the right row.

Syllabus: no conflict: F35. Agrees with Change 1.

## Change 11
File: BW5-specifying-a-project.md, Deliverable · A one-page spec, a build order, a unit brief, done-when lines and a decision log > 1e · The decision log (`records/decisions.md`), on the case (F35)
Current:
````
| One sitemap figure passed on its eighth check (§6) | [NOT IN CASE FILE] |
````
Replacement:
````
| One sitemap figure passed on its eighth check (§6) | 3 Nov 2026 (§2) · [NOT IN CASE FILE] |
````
Result: PASS. Case file §2 (Decision dates): 3 Nov 2026 for figures fixed until they pass. The Current matches D4's Consequences and date cells only (D4 is the never-dropped row).

Syllabus: no conflict: F35. Agrees with Change 1.

## Change 12
File: BW6-research-and-verification.md, 1 · Ask, search or deep research > Deep research (F18)
Current:
````
The case file does not record the research agents' model (§9 of the file; BW2, row 7).
````
Replacement:
````
The research agents were Fable 5.1, and the report was written on 27 Oct 2026 (Academy case file §3).
````
Result: FAIL. Model correct (case file §3, research report's agents: Fable 5.1). The report's date (27 Oct 2026) is a fact F18 does not name; the change adds it beyond the flag. See New 12.

Syllabus: no conflict: F18 (model of the research agents). No brief contradicted.

## Change 13
File: BW6-research-and-verification.md, 7 · The Academy case's numbers, read as an anecdote (F18)
Current:
````
(case file §2, which says the model that wrote each unit is recorded; the case file does not list it per draft)
````
Replacement:
````
(case file §2; every one of the 36 was written by Opus 5.5, case file §5)
````
Result: PASS. Case file §5 (Writing model of the 36): every one written by Opus 5.5. Reads in place inside the parenthesis.

Syllabus: no conflict: F18 (writing model of the 36).

## Change 14
File: BW6-research-and-verification.md, 7 · The Academy case's numbers, read as an anecdote (F47, F105)
Current:
````
The case file does not say how many of the ten stale claims were in the sample.
````
Replacement:
````
3 of the ten stale claims were in the sample, all in B2's nine, and 7 were found while checking beyond it; the decision rule was applied to the sample only (case file §4).
````
Result: PASS. Case file §4 (Audit 2, its report): B2's sample 0 of 9 failing with 3 stale; 3 of 10 stale among the 28 sampled; 7 beyond; decision rule on the sample only. Reads in place after the clean-sample arithmetic.

Syllabus: no conflict: F47, F105. No brief contradicted. Unit codes and 'the private courses' are taken from the case file, which is compiled with private details removed; kit/private_terms.py is not in this packet, so the filer runs it after applying.

## Change 15
File: BW6-research-and-verification.md, 7 · The Academy case's numbers, read as an anecdote (F47, F105, F18)
Current:
````
the case file does not record whether Audit 2's units had a fresh check (BW5 §10 makes the same point). Which model ran each audit after Fable 5.2's release, and what any check cost in time or money, are not recorded (case file §9; BW2, routing table, "Sources for Part 1").
````
Replacement:
````
Audit 2's units, B2, B3, B4 and A1 (case file §4), all had a fresh check before filing (case file §5), but with no control (case file §9) the check's part in the pass cannot be measured (BW5 §10 makes the same point). The audits after Fable 5.2's release, the public marketing course's four, ran on Fable 5.2, and no audit of the private courses or the UX course ran after Audit 2 (case file §4); what any check cost in time or money is not recorded (case file §9; BW2, routing table, "Sources for Part 1").
````
Result: FAIL. The first sentence is correct (case file §4, §5, §9). The second asserts that 'the audits after Fable 5.2's release' are the public marketing course's four; the case file (§4, Auditing model) says those four ran on Fable 5.2 and no private or UX audit ran after Audit 2, but gives no release date for Fable 5.2, so the identification is an inference the source does not state. See New 15, which states the same facts without it. Change 2 stands with New 15.

Syllabus: no conflict: F47, F105, F18. No brief contradicted; with Change 2 applied, BW5 §10 and BW6 §7 agree. Unit codes and 'the private courses' are taken from the case file, which is compiled with private details removed; kit/private_terms.py is not in this packet, so the filer runs it after applying.

## Change 16
File: BW6-research-and-verification.md, Deliverable · A verification protocol > Part 1 · On the Academy case (F47, F105)
Current:
````
`[UNKNOWN: date] · four units [UNKNOWN: codes] ·
````
Replacement:
````
`29 Oct 2026 · four units, B2, B3, B4, A1 ·
````
Result: PASS. Case file §4 (Audit 2): 29 Oct 2026, over B2, B3, B4 and A1. Fills the log's date and text fields; the blank asked for codes.

Syllabus: no conflict: F47, F105 (date and units). Unit codes and 'the private courses' are taken from the case file, which is compiled with private details removed; kit/private_terms.py is not in this packet, so the filer runs it after applying.

## Change 17
File: BW6-research-and-verification.md, Deliverable · A verification protocol > Part 1 · On the Academy case (F47, F105)
Current:
````
10 STALE in one unit (how many sampled not recorded);
````
Replacement:
````
10 STALE in one unit, 3 of them in the sample (B2's);
````
Result: PASS. Case file §4: 3 of the 10 stale among the 28 sampled, all in B2's sample.

Syllabus: no conflict: F47, F105.

## Change 18
File: BW6-research-and-verification.md, Deliverable · A verification protocol > Part 1 · On the Academy case (F47, F105, F18)
Current:
````
[UNKNOWN: the model that ran Audit 2; the method names Fable 5.1, case file §2]
````
Replacement:
````
Fable 5.1, with live search, in its own agent context that had not seen the writing
````
Result: FAIL. The log field is 'checker model and version'. Fable 5.1 is correct (case file §4, Audit 2 and Auditing model); 'with live search, in its own agent context that had not seen the writing' are true but are not the field's content and go beyond what F47 names (which model ran it). See New 18.

Syllabus: no conflict: F47, F105, F18.

## Change 19
File: BW7-pipelines-raw-material-to-finished-output.md, 6 · Steps that can be re-run without harm (F53)
Current:
````
The case file does not say how the re-runs were recorded, which is the next section's subject.
````
Replacement:
````
The case recorded them in place: each figure's check count in its unit's course-index row and in the fresh-check report's maintainer note, and a row run again as its own changelog row (Academy case file §6); how to log a re-run is the next section's subject.
````
Result: PASS. Case file §6 (How re-runs were recorded). The pointer to §7 is kept.

Syllabus: no conflict: F53 (how re-runs were recorded).

## Change 20
File: BW7-pipelines-raw-material-to-finished-output.md, 8 · The Academy case's pipeline, and where it failed (F53)
Current:
````
| Not recorded: the file names "a maintainer" (§2) |
````
Replacement:
````
| Until 14 Nov 2026 the chat that orchestrated and filed the row, recorded as "the maintainer", on Opus 5.5 except in three UX rows; from 15 Nov 2026 a separate Opus 5.5 agent, the applier (§2) |
````
Result: PASS. Case file §2 (Who applied findings): the filing chat recorded as the maintainer until 14 Nov 2026, Opus 5.5 except two UX rows on Fable 5.1 and one on Fable 5.2; from 15 Nov 2026 a separate Opus 5.5 applier. Follows the S-BW line (195), which supersedes line 119's 'does not say who applied the findings for the earlier units'; no filed unit in this packet says 'from BW7 on'.

Syllabus: no conflict: F53 (who applies findings).

## Change 21
File: BW7-pipelines-raw-material-to-finished-output.md, 8 · The Academy case's pipeline, and where it failed (F53)
Current:
````
| None: a script (§1, §6) | Not recorded | Not recorded |
````
Replacement:
````
| None: a script (§1, §6) | Code: the build's verify script (§1) | Not recorded |
````
Result: PASS. Case file §1 (Publishing: rebuilt by script, verified; Gates before publishing: the build's verify script). 'Code:' is BW7's own gate label (§2 table, Part 2).

Syllabus: no conflict: F53 (the build's own checks).

## Change 22
File: BW7-pipelines-raw-material-to-finished-output.md, 8 · The Academy case's pipeline, and where it failed (F53)
Current:
````
| A separate agent (§6); model not recorded |
````
Replacement:
````
| A separate Opus 5.5 agent (§6) |
````
Result: PASS. Case file §6 (Figure checkers' model).

Syllabus: no conflict: F53, F107 (figure checkers' model).

## Change 23
File: BW7-pipelines-raw-material-to-finished-output.md, 8 · The Academy case's pipeline, and where it failed (F53)
Current:
````
| The built site → one website with one design (§1) | Not recorded | Not recorded |
````
Replacement:
````
| The built site → one website with one design, published first as an artifact on claude.ai and then on GitHub Pages (§1) | Not recorded | Code: the verify script, the course-index check and the private-terms check must pass, then the publish is read back by sha256 (§1) |
````
Result: PASS. Case file §1 (Publishing; Gates before publishing). The model stays 'Not recorded', correctly: §7 (Who publishes) names the session, not a model.

Syllabus: no conflict: F53 (publishing steps, places, gates).

## Change 24
File: BW7-pipelines-raw-material-to-finished-output.md, 8 · The Academy case's pipeline, and where it failed (F53 (CP-4: "it records none before publishing"))
Current:
````
- **The gates the case file records sit before filing; it records none before publishing.**
````
Replacement:
````
- **The gates the case file records sit before filing; before publishing it records only scripts.**
````
Result: PASS. Case file §1 (Gates before publishing): scripts must pass, then a sha256 read-back. The same line records the owner approving the repository attach after a refused permission check; that is a permission event, not a check of the output, so 'only scripts' holds as a description of the gates.

Syllabus: no conflict: F53 (gates before publishing; CP-4's 'records none before publishing').

## Change 25
File: BW7-pipelines-raw-material-to-finished-output.md, 8 · The Academy case's pipeline, and where it failed (F53)
Current:
````
the case file does not say whether one was added.
````
Replacement:
````
one was added on 11–12 Nov 2026, after the structure audit: a script that fails the build on a private term in a public course, now among the scripts that must pass before a publish (§1, §7).
````
Result: PASS. Case file §7 (Private-terms check, start): added 11 to 12 Nov 2026 with the two public courses, after the structure audit of 29 Oct 2026; §1 (Gates before publishing) lists it among the scripts. En dash in a date range, no em dash.

Syllabus: no conflict: F53 (when the private-terms check began).

## Change 26
File: BW7-pipelines-raw-material-to-finished-output.md, Deliverable · A pipeline written as a runnable procedure > Step 4 · Apply findings (F53)
Current:
````
- **Model:** `[NOT IN CASE FILE: whether the maintainer who applies findings is a person or a model, and which]`.
````
Replacement:
````
- **Model:** in the case, until 14 Nov 2026, the chat that orchestrated and filed the row, recorded as "the maintainer", on Opus 5.5 except in three UX rows (two on Fable 5.1, one on Fable 5.2); from 15 Nov 2026 a separate Opus 5.5 agent, the applier (case file §2).
````
Result: PASS. Case file §2 (Who applied findings), counts of UX rows and models as stated there.

Syllabus: no conflict: F53.

## Change 27
File: BW7-pipelines-raw-material-to-finished-output.md, Deliverable · A pipeline written as a runnable procedure > Step 4 · Apply findings (F53)
Current:
````
- **Gate (maintainer; whether a person or a model is `[NOT IN CASE FILE]`):**
````
Replacement:
````
- **Gate (maintainer; in the case the filing chat, then the applier, case file §2):**
````
Result: PASS. Case file §2 (Who applied findings).

Syllabus: no conflict: F53.

## Change 28
File: BW7-pipelines-raw-material-to-finished-output.md, Deliverable · A pipeline written as a runnable procedure > Step 6 · Build (F53)
Current:
````
`[NOT IN CASE FILE: the build's own checks]`.
````
Replacement:
````
In the case the build is checked by its verify script (case file §1).
````
Result: PASS. Case file §1 (Publishing; Gates before publishing).

Syllabus: no conflict: F53.

## Change 29
File: BW7-pipelines-raw-material-to-finished-output.md, Deliverable · A pipeline written as a runnable procedure > Step 7 · Checks (F53)
Current:
````
`[NOT IN CASE FILE: its model]`
````
Replacement:
````
Opus 5.5 for every check and re-check
````
Result: PASS. Case file §6 (Figure checkers' model). Reads in place in the Model line.

Syllabus: no conflict: F53, F107.

## Change 30
File: BW7-pipelines-raw-material-to-finished-output.md, Deliverable · A pipeline written as a runnable procedure > Step 8 · Publish (F53)
Current:
````
`[NOT IN CASE FILE: the publishing steps and where the site is published]`.
````
Replacement:
````
In the case, after each filing the site is rebuilt, verified and published in two places, first as an artifact on claude.ai and then on GitHub Pages (case file §1).
````
Result: PASS. Case file §1 (Publishing), verbatim in substance.

Syllabus: no conflict: F53.

## Change 31
File: BW7-pipelines-raw-material-to-finished-output.md, Deliverable · A pipeline written as a runnable procedure > Step 8 · Publish (F53)
Current:
````
(proposal; the case file records no gate here)
````
Replacement:
````
(proposal; the case's own gates here are scripts: the verify script, the course-index check and the private-terms check must pass, then the publish is read back by sha256, case file §1)
````
Result: PASS. Case file §1 (Gates before publishing). The step's human gate stays a proposal, as before; see note on Change 24.

Syllabus: no conflict: F53.

## Change 32
File: BW7-pipelines-raw-material-to-finished-output.md, Deliverable · A pipeline written as a runnable procedure > The run log, on the case (F53)
Current:
````
| `[NOT IN CASE FILE]` | 2 Write · run 3, one deep dive | The packet and the second writer's working files | `[NOT IN CASE FILE]` |
````
Replacement:
````
| 2–3 Nov 2026 (case file §8) | 2 Write · run 3, one deep dive | The packet and the second writer's working files | Opus 5.5 (case file §5, §8) |
````
Result: PASS. The deep dive that lost two writers is the usage review (case file §8, Working files); it read the history on 2 and 3 Nov 2026 across three agent runs (§8, Date), so the third run falls in 2 to 3 Nov; the review is DD-B2, one of the 36 all written by Opus 5.5 (§5). The unit's text names no code. En dash in a date range.

Syllabus: no conflict: F53 (run log on the case).

## Change 33
File: BW7-pipelines-raw-material-to-finished-output.md, Deliverable · A pipeline written as a runnable procedure > The run log, on the case (F53)
Current:
````
| The checker's packet only | `[NOT IN CASE FILE]` |
````
Replacement:
````
| The checker's packet only | Opus 5.5 (case file §5) |
````
Result: PASS. Case file §5 (BW1 to BW9, checker Opus 5.5 on each).

Syllabus: no conflict: F53.

## Change 34
File: BW7-pipelines-raw-material-to-finished-output.md, Deliverable · A pipeline written as a runnable procedure > The run log, on the case (F53)
Current:
````
| A new agent each time; `[NOT IN CASE FILE: model]` |
````
Replacement:
````
| A new Opus 5.5 agent each time (case file §6) |
````
Result: PASS. Case file §6 (Figure checkers' model).

Syllabus: no conflict: F53, F107.

## Change 35
File: BW8-skills-and-automation.md, 5 · Scripts inside a skill for the steps that must be exact (F53, F62)
Current:
````
The case file does not record when the terms check was added relative to the structure audit that found private terms in a public build (Academy case file §7), nor whether either script lives inside a skill `[NOT IN CASE FILE]`.
````
Replacement:
````
The terms check was added on 11–12 Nov 2026, when the two public courses were created, after the structure audit of 29 Oct 2026 that found private terms in a public build (Academy case file §7). The case kept four skills in its repository, for writing a unit, running a fresh check or audit, filing a unit and starting a course (§7); whether either script lives inside one `[NOT IN CASE FILE]`.
````
Result: PASS. Case file §7 (Private-terms check, start; Skills). The remaining NOT IN CASE FILE (whether either script lives inside a skill) is still true: §7 names the skills by purpose only.

Syllabus: no conflict: F53, F62.

## Change 36
File: BW8-skills-and-automation.md, 7 · Counting the repeats before automating (F62)
Current:
````
On the count, it passes; the case file does not record the minutes per check, or whether the case wrote the check as a skill `[NOT IN CASE FILE]`.
````
Replacement:
````
On the count, it passes, and the case did write it as a skill: one of four in its repository, installed by hand on the owner's account under Customize > Skills, with the method telling a chat to run fresh checks with it (Academy case file §7); the case file does not record the minutes per check `[NOT IN CASE FILE]`.
````
Result: PASS. Case file §7 (Skills): four skills in the repository, one for running a fresh check or audit, installed by hand under Customize > Skills (the product's own label), the method telling a chat to run fresh checks with it; §9: no hours. 'Customize' is the UI label, not a spelling choice.

Syllabus: no conflict: F62.

## Change 37
File: BW8-skills-and-automation.md, Deliverable · A skill that checks a draft against its sources, tested, with one scheduled task (F53)
Current:
````
applying findings stays with the maintainer, whether a person or a model `[NOT IN CASE FILE]`.
````
Replacement:
````
applying findings stays with the maintainer, in the case the filing chat until 14 Nov 2026 and from 15 Nov 2026 a separate Opus 5.5 agent, the applier (Academy case file §2).
````
Result: PASS. Case file §2 (Who applied findings).

Syllabus: no conflict: F53.

## Change 38
File: BW8-skills-and-automation.md, Deliverable · A skill that checks a draft against its sources, tested, with one scheduled task > F · The scheduled task: the monthly rot check (F63)
Current:
````
On the case `[NOT IN CASE FILE: whether the repository holds INDEX.md, INSTRUCTIONS.md and BUILD-ORDER.md in BW4's and BW5's form; the case file records the method, a backlog and a changelog, §1, §2]`. Until it does, the script reports those files as missing, which is itself the first finding.
````
Replacement:
````
On the case, no file named INDEX.md, INSTRUCTIONS.md or BUILD-ORDER.md appears in the records; their equivalents are `docs/courses-index.md` (the index), `docs/project-instructions.md` (a copy of the Project's instructions field) and each course's build order as a list in its data file (Academy case file §1). Run on the case as written, the script reports those three files as missing, which is itself the first finding; read each of those FAIL lines against its equivalent above.
````
Result: PASS. Case file §1 (Layout names), with the mapping F63 asks for; the FAIL lines refer to the script's own output (Deliverable F, 'Each FAIL becomes a backlog row'). Agrees with Change 4 in BW5.

Syllabus: no conflict: F63.

## New 3
File: BW5-specifying-a-project.md, Deliverable · A one-page spec, a build order, a unit brief, done-when lines and a decision log > 1a · The one-page spec (`SPEC.md`) (F35)
Current:
````
> **Reader.** Each course names its own reader in its shared preamble (§2). [NOT IN CASE FILE: the reader of any course.]
````
Replacement:
````
> **Reader.** Each course names its own reader in its shared preamble (§2). Building with AI's reader: an experienced professional who reasons and writes well, uses a chat assistant with no method, may not write code, and brings one real project (§2). [NOT IN CASE FILE: the reader of the other courses.]
````
Result: PASS. Replaces Change 3. Names the course instead of 'This course'. Facts from case file §2 (line 115).

Syllabus: no conflict: as Change 3.

## New 12
File: BW6-research-and-verification.md, 1 · Ask, search or deep research > Deep research (F18)
Current:
````
The case file does not record the research agents' model (§9 of the file; BW2, row 7).
````
Replacement:
````
The research agents were Fable 5.1 (Academy case file §3).
````
Result: PASS. Replaces Change 12. The model only, as F18 names. Case file §3.

Syllabus: no conflict: as Change 12.

## New 15
File: BW6-research-and-verification.md, 7 · The Academy case's numbers, read as an anecdote (F47, F105, F18)
Current:
````
the case file does not record whether Audit 2's units had a fresh check (BW5 §10 makes the same point). Which model ran each audit after Fable 5.2's release, and what any check cost in time or money, are not recorded (case file §9; BW2, routing table, "Sources for Part 1").
````
Replacement:
````
Audit 2's units, B2, B3, B4 and A1 (case file §4), all had a fresh check before filing (case file §5), but with no control (case file §9) the check's part in the pass cannot be measured (BW5 §10 makes the same point). The public marketing course's four audits ran on Fable 5.2, and no audit of the private courses or the UX course ran after Audit 2 (case file §4); what any check cost in time or money is not recorded (case file §9; BW2, routing table, "Sources for Part 1").
````
Result: PASS. Replaces Change 15. States the case file's §4 line without identifying the post-release audits. Companion: Change 2.

Syllabus: no conflict: as Change 15.

## New 18
File: BW6-research-and-verification.md, Deliverable · A verification protocol > Part 1 · On the Academy case (F47, F105, F18)
Current:
````
[UNKNOWN: the model that ran Audit 2; the method names Fable 5.1, case file §2]
````
Replacement:
````
Fable 5.1
````
Result: PASS. Replaces Change 18. The field's content only. Case file §4 (Audit 2; Auditing model).

Syllabus: no conflict: as Change 18.
