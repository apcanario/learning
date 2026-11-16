---
code: DD-BW2
title: "Deep dive: one project, with its numbers"
course: building-with-ai · BW · Building with AI
model: Opus 5.5
written: 2026-11-16
search: off
---

# DD-BW2 · Deep dive: one project, with its numbers

This unit reads one project's record from end to end: Academy (Academy case), a library of self-study courses built by one person with Claude in October and November 2026, with a method of one brief per unit, and a fresh check and sample audits that the case file records as run on part of the library (Academy case file §1, §2, §5, §9). Every fact about it comes from the Academy case file, cited by section; where the file holds nothing, the text says "not recorded" and the gap is listed in this unit's notes as a need. The whole unit is an anecdote: one project, one person, one vendor's models (case file §1, §2), no control and no second project (case file §9). What it can do is show you what a real record holds, what its numbers support, and how much of what you would want to know a careful record still leaves out. DD-BW3 sets your own record beside this one.

What it assumes, by section and without restating: the vocabulary of what the model saw (BW1 §1, §9); routing by tier and effort, and why the check runs outside the writer's context (BW2 §5, §7); the brief and its done-when lines (BW3; BW5, Deliverable 1d); the structure audit of the case (BW4 §7); the case's method read as a spec (BW5 §10); the sampling arithmetic, applied to the case's two audits (BW6 §5, §7), which this unit points to and does not re-derive; the case's pipeline, stage by stage, and its run log (BW7 §8 and Deliverable, "The run log, on the case"); the case's agent failures (BW9 §9); usage, which the case did not measure (BW10 §1, §4); and the ten operating rules (DD-BW1, Deliverable Part 2). Those units read the case for one question each. This one reads the whole record at once, and asks of each rule in the course whether the numbers support it, are merely consistent with it, or say nothing.

Grades follow the course: **measured**, **documented practice**, **stated opinion**. Every count from the case is an anecdote whatever its size; the grade of a rule comes from the unit that teaches it, never from the case.

## 1 · What was built, by count

At 11 November 2026 Academy held five written courses in four subjects: two history courses of 78 and 79 long-form reports, a marketing course of 11 units, an AI course of 11 units and a UX course of 15 units, 194 units in all (case file §1). A unit is a long-form report in Markdown, 2,000 to 6,000 words by guide, with sources cited in place and a closing deliverable built in full; the longest UX unit is about 16,900 words (§1). Everything lives in one private repository (texts, briefs, build scripts, method, backlog and changelog), and the site is built from it by script, with no page styled by hand (§1).

```viz
{
  "kind": "compare",
  "unit": "units",
  "max": 80,
  "rows": [
    {"label": "History course (78)", "value": 78, "tone": 1},
    {"label": "History course (79)", "value": 79, "tone": 1},
    {"label": "UX course", "value": 15, "tone": 3},
    {"label": "Marketing course", "value": 11, "tone": 4},
    {"label": "AI course", "value": 11, "tone": 4}
  ],
  "caption": "Units written per course at 11 Nov 2026, 194 in all: §1 of this unit, from Academy case file §1 (one project, an anecdote). The case file does not say which history course holds which count."
}
```

This course is a sixth, written after that count. By 16 November 2026 its folder held BW1 to BW10 and DD-BW1, one Markdown file per unit (case file §1, notes of 16 Nov 2026). Each unit's reading page on the site opens by saying that an AI model wrote it, naming the model, and that a separate model in a context that had not seen the writing checked it, with the check's counts (§1, note).

Three things the count does not tell you. The case file gives no total of words written, so 194 units at 2,000 to 6,000 words each is a range by guide, not a measure. It does not say whether the history courses' 157 units had a fresh check: its table of fresh checks covers the marketing, AI and UX courses only (§5). And it does not say how long any unit took (§9). "October and November 2026" and 194 units is as far as the record goes; a rate per day cannot be computed from it, because the file gives no start date.

## 2 · The method, as it was run

The method is laid out as a spec in BW5 §10 and as a pipeline in BW7 §8; this section adds only what those units do not: how the method changed while it ran, which is where the record is most informative.

**As written** (case file §2). A syllabus first; one brief per unit, joined to a shared preamble and never reworded; one context per unit, for the stated reason that leaked context is how a course starts repeating itself; the writer's own pass against the sourcing checklist, with up to ten unverified claims listed; a fresh check by a context that has not seen the unit written, which writes graded findings (error, should-fix, minor) and never edits, each finding verified by a maintainer and applied as an exact replacement; a sample audit every four units; a staleness check six months after any unit written with live search; Opus 5.5 to write and Fable 5.1 to audit, with the writing model recorded; a backlog and a changelog, with proposed rows held until the owner confirms them.

**What changed, in the order the record allows** (the case file dates only some of these):

1. **The fresh check became a rule after a failure.** The first three marketing units were written from one research report produced by research agents across five tracks, without a fresh check; Audit 1 sent them to rewrite, and "from then on every unit of that family got a fresh check before filing" (§3). The first AI unit predates the rule (§5).
2. **Three checker models ran the fresh check:** Fable 5.1 on 19 drafts, Opus 5.5 on 12, Fable 5.2 on 5 (§5, by count of its table). The method names Fable 5.1 as the auditing model (§2); it names no model for the fresh check.
3. **The figure rule changed.** At first a figure that failed its check three times was dropped, and two were; the owner later ruled that figures are never dropped and are fixed until they pass (§6).
4. **The applying step became an agent.** From BW7 of this course (16 Nov 2026), a separate agent, the applier, running Opus 5.5, applied the fresh check's findings and could add companion edits a finding implies; writer, checker, applier, filer and corrections checker were each a fresh agent (§2, note). The record does not say who applied findings for the 36 earlier units (§2, note).
5. **A thinner main chat was asked for and not run.** For BW10 and for DD-BW1, the row's prompt asked for a main chat on a smaller model (Sonnet 5.5) that only staged packets, filed and recorded; both sessions ran Opus 5.5 and were recorded as such (§2, notes). DD-BW1's row was the second of three rows run in one main chat (§2, note).
6. **Checks were added; the record does not date them.** A script now checks this course's data folder against a list of private terms, and its fresh checker checks each unit against the same list; the record does not say when this was added relative to the structure audit that found private terms in a public build (§7, note). A script also checks the course index after each filing chat and restores every file if the check fails (§1, note).

The proposal rule shows in the flag counts: the case file's method says a proposed row is not worked until the owner confirms it (§2), and the case file's syllabus-flags note says a flag that would change a brief waits for a syllabus review the owner confirms, with no fixed date for one; at 16 Nov 2026, before BW5's flags were added, of 34 flags raised at the course's creation and by BW1 to BW4, 26 were open, 7 carried, 1 resolved by a correction and none resolved by a syllabus review (§2, note). Read plainly (this unit's reading): proposals were raised faster than any review settled them.

## 3 · Errors per unit at the fresh check

The fresh check is the one stage the record counts for every unit it covers. The table below is the case file's §5 table, with two changes: the private courses' unit codes are replaced by the row's number in the case file's order (the case file does not say that order is the order of writing), and this course's two units whose checks the case file records are added at the foot. Counts are the checker's findings on the writer's handed-in draft (§5).

| Row | Course | Checker | Verdict | Errors | Should-fix | Minor |
|---|---|---|---|---|---|---|
| 1 | Marketing | Fable 5.1 | fix | 2 | 15 | 8 |
| 2 | Marketing | Fable 5.1 | fix | 3 | 13 | 11 |
| 3 | Marketing | Fable 5.1 | fix | 1 | 9 | 7 |
| 4 | AI | Fable 5.1 | fix | 3 | 10 | 14 |
| 5 | AI | Fable 5.1 | fix | 1 | 4 | 9 |
| 6 | AI | Fable 5.1 | fix | 0 | 7 | 9 |
| 7 | Marketing | Fable 5.1 | fix | 1 | 4 | 6 |
| 8 | AI | Fable 5.1 | fix | 1 | 3 | 9 |
| 9 | Marketing | Fable 5.1 | keep | 0 | 1 | 9 |
| 10 | AI | Fable 5.1 | fix | 1 | 4 | 5 |
| 11 | Marketing | Fable 5.1 | fix | 2 | 3 | 8 |
| 12 | Marketing | Opus 5.5 | fix | 1 | 4 | 8 |
| 13 | AI | Opus 5.5 | fix | 1 | 4 | 8 |
| 14 | Marketing | Opus 5.5 | keep | 0 | 3 | 6 |
| 15 | Marketing | Opus 5.5 | fix | 2 | 8 | 7 |
| 16 | AI | Opus 5.5 | fix | 3 | 8 | 12 |
| 17 | AI | Opus 5.5 | rewrite | 4 | 4 | 4 |
| 18 | Marketing | Opus 5.5 | fix | 3 | 6 | 6 |
| 19 | AI | Opus 5.5 | fix | 0 | 10 | 14 |
| 20 | Marketing | Opus 5.5 | fix | 0 | 5 | 5 |
| 21 | AI | Opus 5.5 | fix | 3 | 4 | 5 |
| 22 | UX | Opus 5.5 | keep | 0 | 4 | 7 |
| 23 | UX | Opus 5.5 | fix | 3 | 10 | 17 |
| 24 | UX | Fable 5.1 | keep | 0 | 2 | 6 |
| 25 | UX | Fable 5.1 | fix | 2 | 18 | 9 |
| 26 | UX | Fable 5.1 | fix | 2 | 3 | 5 |
| 27 | UX | Fable 5.1 | fix | 2 | 4 | 11 |
| 28 | UX | Fable 5.1 | fix | 0 | 6 | 3 |
| 29 | UX | Fable 5.1 | fix | 1 | 3 | 9 |
| 30 | UX | Fable 5.1 | fix | 1 | 3 | 8 |
| 31 | UX | Fable 5.1 | fix | 3 | 3 | 3 |
| 32 | UX | Fable 5.2 | fix | 2 | 13 | 10 |
| 33 | UX | Fable 5.2 | fix | 3 | 8 | 13 |
| 34 | UX | Fable 5.2 | fix | 2 | 12 | 20 |
| 35 | UX | Fable 5.2 | fix | 2 | 11 | 7 |
| 36 | UX | Fable 5.2 | fix | 3 | 8 | 5 |
| **1–36** | **Three courses** | | **31 fix, 4 keep, 1 rewrite** | **58** | **237** | **303** |
| BW10 | This course | Opus 5.5 | fix | 0 | 7 | 11 |
| DD-BW1 | This course | Opus 5.5 | fix | 3 | 20 | 12 |

Sources: rows 1 to 36 and their totals, Academy case file §5; BW10 and DD-BW1, case file §5, notes of 16 Nov 2026. The checks of BW1 to BW9 of this course are not in the case file's counts.

What the table says, by arithmetic on it:

- **Most drafts had an error.** 28 of the 36 had at least one; 8 had none (§5). That is 77.8%. A count kept in one AI unit at the time it was written gives the same picture from earlier: fifteen of the first twenty drafts had an error at first check (§5), 75%.
- **Errors were few per draft; findings were many.** 58 errors across 36 drafts is 1.6 a draft: 8 drafts had none, 9 had one, 9 had two, 9 had three and 1 had four. All findings together number 598, from 8 to 34 a draft, 16.6 on average. Errors are 9.7% of the findings, should-fix 39.6%, minor 50.7%.
- **A clean draft still got work.** Of the 8 drafts with no error, 4 were kept as they were and 4 were sent back to fix on their should-fix findings. Every "keep" had no error. The one "rewrite" (row 17) had the most errors, 4.
- **The courses look alike.** Marketing: 8 of 11 drafts with an error; 15 errors, 71 should-fix, 81 minor. AI: 8 of 10; 17, 58, 89. UX: 12 of 15; 26, 108, 133.

```viz
{
  "kind": "compare",
  "unit": "drafts",
  "max": 10,
  "rows": [
    {"label": "No error", "value": 8, "tone": 3},
    {"label": "1 error", "value": 9, "tone": 4},
    {"label": "2 errors", "value": 9, "tone": 4},
    {"label": "3 errors", "value": 9, "tone": 1},
    {"label": "4 errors", "value": 1, "tone": 1}
  ],
  "caption": "The 36 fresh-checked drafts of three courses by the number of errors the checker found in each: §3 of this unit, counted from the table in Academy case file §5 (one project, an anecdote)."
}
```

```viz
{
  "kind": "bars",
  "mode": "stacked",
  "series": [
    {"name": "Errors", "tone": 1},
    {"name": "Should-fix", "tone": 4},
    {"name": "Minor", "tone": 3}
  ],
  "rows": [
    {"label": "Marketing (11 drafts)", "values": [15, 71, 81]},
    {"label": "AI (10 drafts)", "values": [17, 58, 89]},
    {"label": "UX (15 drafts)", "values": [26, 108, 133]}
  ],
  "caption": "Fresh-check findings by grade and course, 598 in all: §3 of this unit, summed from the table in Academy case file §5. The courses differ in subject, units, dates and checkers, and there is no control (§3), so the bars compare nothing causal."
}
```

**What the table cannot be read for.** It cannot rank the checker models. BW6 §4 and BW2 §5 already say so: units, courses and dates differ, and there is no control (case file §9). It cannot say which model wrote each draft: the method names Opus 5.5 as the writer and says the writing model is recorded (§2), but the table does not list it per draft. It cannot say whether the fresh check made later drafts better: the file does not say the rows are in order of writing. And an error count is a count of what one checker found, not of what was there: the case file does not count findings the maintainer rejected after verifying them, so the checkers' false-alarm rate is unknown, and nothing measures what they missed. The nearest evidence on both is in §5 below.

## 4 · The two sample audits, and what each led to

The sampling arithmetic for both audits is in BW6 §5 and §7; this section gives what happened and what followed.

**Audit 1** sampled the first three marketing units, which had been written from one research report produced by research agents across five tracks. One of eight sampled claims failed, which triggered a full audit: of 91 claims, 23 failed and none was stale; nothing was invented and no conclusion flipped (case file §3). The verdict was rewrite, for two reasons: the three deliverables did not exist, and two table rows rested on figures the cited vendor pages did not contain. The pattern the audit named was "qualifiers the source does not carry" (§3). The same audit passed the first AI unit on seven of seven sampled claims (§3).

*What it led to.* The three units were rewritten from their briefs the same day, and from then on every unit of that family got a fresh check before filing (§3). On this unit's reading, that is the largest single change in the record, and it was made on one audit's findings on three units (the same audit passed a fourth).

**Audit 2** covered four units: 28 claims sampled, 96 checked in all. No sampled claim failed; one incidental claim outside the sample failed, a miscited caption. Ten claims were stale, all in one unit and from one cause: an independent benchmark published a new index version the day before the unit read its leaderboard. All four units passed, and 26 errata were applied the same day (§4).

*What it led to.* Errata, the same day (§4). The case file records no change of method after Audit 2. It does not give Audit 2's date, which units it covered, which model ran it, or whether any of the ten stale claims were among the 28 sampled (BW6, Deliverable H, marks these unknown).

**What did not happen.** Audits 3 onward of the marketing, AI and UX courses had not run at 11 November 2026 (§9). The method calls for an audit every four units (§2); the three courses together had 37 units at that date (§1), so, on this unit's reading of the method's schedule (the case file does not say whether it counts units per course or across courses), more audits were due than had run. The record does not say why. Two audits on eight units (four each) is the whole of the case's sample-audit evidence.

## 5 · The kinds of error that recur

The case file names kinds of error without counting them. Gathered from every section, with the count where one exists:

| Kind | Where recorded | Count in the record |
|---|---|---|
| A figure the cited page does not carry | Fresh-check reports (§5); Audit 1, two table rows on vendor figures (§3) | Audit 1: 2 table rows. Fresh checks: not counted by kind |
| A qualifier the source does not carry | Audit 1's named pattern (§3) | Within the 23 failures of 91; not split out |
| An author named wrongly | Fresh-check reports (§5) | Not counted |
| A law that had changed | Fresh-check reports (§5) | Not counted |
| A quotation the page does not hold | Fresh-check reports (§5) | Not counted |
| A count that did not add up | Fresh-check reports (§5) | Not counted |
| A product fact that differed between two of the vendor's own pages | Fresh-check reports (§5) | Not counted |
| A fact stale on the day it was read | Audit 2 (§4) | 10 claims, one unit, one cause |
| A miscited caption | Audit 2 (§4) | 1 |
| A figure carrying facts the text did not | DD-BW1's fresh check (§5, note) | 3 of DD-BW1's 3 errors |
| A deliverable that did not exist | Audit 1 (§3) | 3 of 3 units |
| A proposed fix that was itself wrong or incomplete | BW10 and DD-BW1 appliers (§5, notes) | 4 of 18; 2 of 35 |
| A proposed correction to another unit that could not stand | BW10 and DD-BW1 corrections checks (§2, notes) | 1 of 5 failed; 1 of 8 failed as uncheckable |

Three patterns stand out (this unit's reading, stated opinion).

**The failures are in real sources.** Nothing in the record is an invented source: Audit 1 found nothing invented among 91 claims (§3), and none of the kinds the fresh-check reports name is invention (§5). The errors sit between a real page and the sentence that cites it: a figure, a qualifier, an author, a quotation, a date. BW6 §2 draws the checking rule from this: a check opens the source and compares; confirming that a source exists would have passed every one of these.

**Errors arrive in batches from one cause.** Ten stale claims from one benchmark's version change (§4); three missing deliverables in the three units written from one research report (§3; the case file does not name the cause); three figure errors in one unit, all of one kind (§5, note). A check that samples one claim at a time will find one member of a batch, which is why BW6 §5 stratifies and sends any STALE to a sweep.

**The checking chain makes errors too.** Of the fixes DD-BW1's checker proposed, the applier held 2 of 35 as incomplete or wrong; of BW10's, it held 4 of 18; in both rows it wrote corrected fixes and applied them in a second pass (§5, notes). On BW10's row a corrections checker passed 4 of 5 replacements the writer proposed and failed 1, proposed to an earlier unit of another course, because the text it would have changed quoted another unit's claim and the word it called wrong was not wrong; on DD-BW1's row, a corrections checker failed 1 of 8 because no search returned the address the replacement cited, so it could not be checked (§2, notes). These are the only counts in the record of a proposed fix, the checker's or the writer's, being held or failed, and they cover two rows. They are not a false-alarm rate: a held fix may still answer a real finding.

## 6 · Figures that failed their checks, and what fixing them took

Units declare figures as data and a script draws them; a separate agent checks each figure against the unit's text, and every label and number must already be in the text (case file §6). A figure that failed was fixed and checked again by a new agent (§6).

What fixing took, as far as the record goes:

- **Under the early rule**, a figure that failed three times was dropped: two were (§6).
- **Under the later rule**, set by the owner, figures are never dropped and are fixed until they pass. One sitemap figure passed on its eighth check (§6): seven failures, each followed by a fix and a check by a new agent.
- **At the fresh check**, all three errors in DD-BW1's draft were figures that carried facts the text did not (§5, note).

What the record does not hold: how many figures the units declare, how many failed their first check, what each failure was, how long a fix took, or which model checked figures (BW7 §8 marks the last as not recorded). One figure at eight checks is the extreme; the record gives no typical case.

The rule the figures obey is the course's own: a figure adds no fact (the course's shared preamble; Academy case file §6: every label and number must already be in the text). DD-BW1's count shows how it is broken: a fact placed in a figure with no sentence in the text that states and sources it.

## 7 · What failed in operation

The machinery around the text (case file §7, with the notes of 15 and 16 Nov 2026):

| Failure | What it cost | What followed |
|---|---|---|
| **Lost agents.** Writer agents were lost to container restarts; one deep dive lost two writers, and the third resumed from the second's working files (§7) | Two writer runs | The third writer resumed from files; no rule recorded (BW9 §9) |
| **No transcript.** Some sessions kept no agent transcript on disk, so scripted checks of what each agent had read could not run; the agents' own reports stood in their place (§7) | A check that could not run | No rule recorded |
| **The wrong model ran.** A session's model named "fable" resolved to a newer version than the method names (§7) | Every check it ran, recorded as owed again on the named version | Checks re-owed |
| **Refused report writes.** BW1's checker could not write its report; on BW9's row, the fresh checker and both corrections checkers were refused a write of their reports; on BW10's and DD-BW1's rows, every agent was (§7, notes) | Each report the record follows reached its file only through the main chat, which saved it from the agent's reply (verbatim on the records of BW9 and DD-BW1, and of BW10's fresh checker) | Saved before any change was applied (§7, note on BW9) |
| **A thinner main chat not run.** Two rows asked for Sonnet 5.5 and ran on Opus 5.5 (§2, notes) | Not recorded | Recorded as run |
| **Private terms in a public build.** One of seventeen findings of a structure audit of the project itself; another was project instructions that carried procedures and paraphrased the method file (§7) | Not recorded | A script check against a list of private terms, date not recorded (§7, note); BW4 §7 reads the two findings |

**A publish that had to be repeated.** The case file records none. It says the site is published in two places after each filing, first as an artifact on claude.ai and then on GitHub Pages (§1, note), and that a script restores every file if the course index check fails (§1, note); it records no failed or repeated publish. If one happened, it is not in the record.

**What the failures have in common** (stated opinion). Four of the six are failures of the record: a run whose work survived only in files, a check with no evidence of what was read, a model name that did not say what ran, a report that reached its file by an unplanned path. The other two are not: a main chat that ran on another model than the one asked for, which the record logged as run (§2, notes), and private terms reaching a public build, a leak in the output; the case file records a private-terms check but does not date it against the leak (§7, note). In the four, what was at risk was the project's ability to say what had happened, which is the thing this unit, and DD-BW3 for your project, depends on.

## 8 · What was recorded about cost, in chats and time, and what was not

**Recorded: chats and models.** The owner's chats in the project were reviewed for one deep dive: 53 chats over six days, the project's whole history at the time (case file §8). By model, read from commit trailers: 31 on Opus, 18 on Fable, 4 on both (§8). Each ask was classified by task type, model, outcome and number of turns; the labels were applied by hand, "accepted" was a proxy, and 14 endings were not seen (§8). The review produced ten changes, ranked, each tied to a count (§8); the case file does not list them.

**Recorded: agents per row.** On BW10's and DD-BW1's rows, writer, fresh checker, applier, two corrections checkers and filer were each a fresh Opus 5.5 agent, six to a row, under a main chat (§2, notes). One sitemap figure took eight checks by new agents (§6). One deep dive took three writers (§7).

**Recorded: time, only as "the same day".** Audit 1's three units were rewritten the same day; Audit 2's 26 errata were applied the same day (§3, §4). The whole build ran in October and November 2026 (§1).

**Not recorded.** No measure of hours or money spent per unit (§9). No plan, token, window or usage-bar measure for any unit or check (§7, note of 15 Nov 2026; BW10 §1 and Deliverable Part 1 mark the same gaps). No record of the effort setting for any unit (§9), or of any budget or stop set on agent runs (§9). BW2's routing table and BW10's budgets were built for the case with "not recorded" in every cost cell for this reason, and this unit takes no usage figure from either.

The consequence is the largest single limit on what the record can support. Every change in this unit's deliverable adds work: a check, a log field, a re-run. The record can say what each change would have caught; it cannot say what any of them cost, so it cannot say whether one is worth its price. A reader who keeps one more column than Academy did (hours, or the usage bar before and after) can answer that for their own project.

## 9 · What one person's record cannot show

- **No control.** No unit was written without the method (§9). Nothing in the record shows the method beats a lighter one; BW5 §10, BW7 §8 and BW9 §9 each say the same.
- **No second project and no second person** (§9). Every rate above is one person's, on one kind of output (long-form sourced reports), with one family of models.
- **No before and after.** The fresh check was introduced after Audit 1; Audit 2's units passed; the case file does not say whether those units had a fresh check (BW5 §10, BW6 §7), so the record cannot say the check caused the pass.
- **No measure of what the checks missed.** The 58 errors are what checkers found. Audit 2's incidental miscited caption outside the sample (§4) shows that errors survive a clean sample; how many survive a fresh check is not measured anywhere in the record.
- **No model comparison.** Three checker models ran on different units, courses and dates (§5). Any difference between their counts is confounded with all three.
- **A record compiled by the project itself.** The case file was compiled from the project's own records, with private details removed (case file header). Its counts are the project's counts of its own work, and the case file records no outside check of them.

What it can show: that the stages described in BW5 to BW9 can be run by one person on a real project of 194 units and more, what that person's record caught, and where it went blind.

## 10 · Which of the course's rules the numbers support

Three verdicts (this unit's reading, stated opinion): **supported by a count**, when the record holds a count of the failure the rule is meant to catch; **consistent**, when the record is in line with the rule but holds nothing that tests it; **silent**, when the record holds nothing on it. "Supported" means supported as an observation in one project; the rule's grade is the grade its own unit gives it.

| Rule (unit) | Verdict | The count, or what is missing |
|---|---|---|
| The check runs in a context that did not write the work (BW2 §5; BW6 §4; DD-BW1 rule 3) | Supported by a count | 28 of 36 drafts with an error at the fresh check (§5). Not tested: the writer's own pass ran before every fresh check (§2), and the record holds no count of what it caught |
| A check opens the source and compares; existence is not enough (BW6 §2, §3) | Supported by a count | 23 of 91 claims failed with nothing invented; pattern, qualifiers the source does not carry (§3) |
| Sample, and send any FAIL to a full check; a clean sample certifies nothing (BW6 §5) | Supported by a count | Audit 1: 1 of 8 sampled, then 23 of 91 (§3). Audit 2: clean sample of 28, one failure outside it (§4) |
| Date every fact; a STALE triggers a sweep (BW1 §4; BW6 §5) | Supported by a count | 10 stale claims, one unit, one cause (§4) |
| Verify each finding before applying it; check the checker (BW6 §6) | Supported by a count | 6 of 53 proposed fixes held as wrong or incomplete; 2 of 13 replacements failed a corrections check (§2, §5 notes) |
| A deliverable built in full, with done-when lines a stranger can check (BW5, Deliverable 1d; DD-BW1 rule 2) | Supported by a count | 3 of 3 deliverables missing at Audit 1 (§3) |
| A figure adds no fact; a failed stage is re-run and re-checked from scratch (the course's shared preamble; BW7 §6) | Supported by a count | 3 of DD-BW1's 3 errors in figures (§5, note); one figure passed on its eighth check (§6) |
| Hand-offs as files (BW7 §2) | Supported by a count | 2 writers lost, the third resumed from files (§7); reports on 4 rows reached files only through the main chat (§7, notes) |
| Log what ran, not what was asked for (BW7 §7; BW2 §7) | Supported by a count | One "fable" session's checks re-owed (§7); 2 rows asked for Sonnet 5.5 and ran Opus 5.5 (§2, notes) |
| A deterministic check on the output before publishing (BW4 §7; BW9 §7) | Supported by a count | 1 finding: private terms in a public build (§7) |
| One context per unit (BW4 §4; BW5 §3) | Consistent | Every unit run so (§2). Not tested: no unit written otherwise (§9) |
| A spec and a build order before building (BW5) | Consistent | Every course started from a syllabus (§2). Not tested |
| Route by tier and effort (BW2) | Silent (effort); models partly recorded | Writer and checker models recorded (§2, §5); effort not recorded (§9) |
| The simplest setup that does the job (DD-BW1 rule 6; BW9 §2) | Silent | No lighter setup was run (§9) |
| Guardrails on agent runs: scopes, budgets, commits (BW9 §7; DD-BW1 rule 7) | Silent | Tools, permission modes, commits and caps not recorded (§7 notes, §9) |
| Usage rules and budgets (BW10) | Silent | No usage, token or cost measure (§7 note, §9) |
| Never the trifecta (DD-BW1 rule 9; BW9 §8) | Silent | Which tools each agent held is not recorded (§9) |

```viz
{
  "kind": "compare",
  "unit": "rules",
  "max": 10,
  "rows": [
    {"label": "Supported by a count", "value": 10, "tone": 3},
    {"label": "Consistent", "value": 2, "tone": 4},
    {"label": "Silent", "value": 5, "tone": 1}
  ],
  "caption": "The seventeen rules of the table in §10 of this unit by what the Academy record says about each: this unit's reading of Academy case file §2 to §9 (one project, an anecdote)."
}
```

Of the seventeen rules, ten are supported by a count, two are consistent with the record and five meet silence. The split is the unit's main finding, and it has a shape: the record supports the rules about checking, and is silent on the rules about cost and control. That follows from what the project chose to count. It counted errors at every check, because the method made checking a stage with a written output; it never counted hours, tokens, effort or tools, because no stage wrote them down. A record supports the rules its stages produce numbers for, and no others.

## 11 · On other tools

This unit states no product fact of its own: every fact in it is a fact about one project's record. Two of the case's facts depend on Claude's products, and the units that read them hold the comparison.

- **A model name that resolved to a newer version** (case file §7) is a fact about how Claude model names were resolved in that session. BW2 §7 gives it as the case's instance of one of the four kinds of change that trigger its re-decision rule. BW2 §8 cites, for ChatGPT and Gemini, the vendors' pages on their model tiers (read 15 Nov 2026); none of the pages it lists is about how a model name resolves to a version, so no equivalent is documented in this course, and this unit, written with search off, did not look further.
- **Fresh agent contexts** for the writer, checker, applier and filer (case file §2, notes) ran in Claude; one check is recorded as run from a Claude Code session on claude.ai (§7, note). BW6 §8 records Gemini CLI's subagents, each with an "Independent context window" ([*Subagents*, Gemini CLI documentation](https://geminicli.com/docs/core/subagents/); vendor, read 16 Nov 2026 for BW6), and OpenAI's equivalent as not checked; BW9 §10 gives the same comparison for permission modes, subagents and checkpoints.

Everything else in this unit, the counts and what they support, needs no product: any assistant that lets you open a new chat lets you keep the same record.

## Deliverable · The case report, and ten changes the record supports

Four parts. Part 1 is the case report: the record of §1 to §9 as one form, each line with its count and its source, and "not recorded" where the case file holds nothing. Part 2 is the ten changes the record supports, ranked, each tied to its count and to the unit of this course that teaches it. Parts 3 and 4 are the same two forms as templates for your project, each blank saying what goes in it. DD-BW3 has you fill Parts 3 and 4 from your own chats and set them beside Parts 1 and 2.

### Part 1 · The case report, on the Academy case

**Academy · case report · as of 16 November 2026.** One project, one person; an anecdote. Every line from Academy case file, section given.

**A. What was built**

| Line | Value | Source |
|---|---|---|
| Courses written | 5 at 11 Nov 2026 (two history, marketing, AI, UX), plus this course, BW1 to BW10 and DD-BW1, by 16 Nov 2026 | §1; §1 notes |
| Units written | 194 at 11 Nov 2026: 78, 79, 11, 11, 15; plus 11 of this course by 16 Nov 2026 | §1; §1 notes |
| Unit form | Long-form Markdown report, 2,000 to 6,000 words by guide (longest about 16,900), sources in place, deliverable built in full | §1 |
| Total words | Not recorded | — |
| Period | October and November 2026; start date not recorded | §1 |

**B. The method as run**

| Line | Value | Source |
|---|---|---|
| Stages | Syllabus; brief per unit, never reworded; one context per unit; writer's own pass; fresh check; sample audit every four units; staleness check at six months | §2 |
| Writer model | Opus 5.5 named; per-draft model not in the table | §2, §5 |
| Checker models (fresh check) | Fable 5.1: 19; Opus 5.5: 12 plus BW10 and DD-BW1; Fable 5.2: 5 | §5; §5 notes |
| Audit model | Fable 5.1 named; per-audit model not recorded | §2 |
| Effort settings | Not recorded | §9 |
| Changes while running | Fresh check made a rule after Audit 1; figure rule from drop-after-three to fix-until-pass; applier agent from BW7; thin main chat asked for on two rows and not run | §3, §6, §2 notes |

**C. The fresh check**

| Line | Value | Source |
|---|---|---|
| Drafts checked (three courses) | 36 | §5 |
| Drafts with at least one error | 28 of 36 (77.8%); earlier count, 15 of the first 20 | §5 |
| Findings | 58 errors, 237 should-fix, 303 minor: 598 | §5 |
| Verdicts | 31 fix, 4 keep, 1 rewrite | §5 |
| This course | BW10: 0 errors, 7 should-fix, 11 minor. DD-BW1: 3 errors (all in figures), 20 should-fix, 12 minor. BW1 to BW9: not in the case file | §5 notes |
| Fixes held as wrong or incomplete | BW10: 4 of 18. DD-BW1: 2 of 35. Earlier units: not recorded | §5 notes |
| Findings rejected after verification | Not recorded | — |
| History courses' 157 units checked? | Not recorded | — |

**D. Sample audits**

| Line | Value | Source |
|---|---|---|
| Audit 1 | 3 marketing units: 1 of 8 sampled failed; full audit 23 of 91 failed, 0 stale, 0 invented; verdict rewrite (no deliverables; 2 table rows on figures the vendor pages lacked). First AI unit: 7 of 7, pass | §3 |
| What Audit 1 led to | Three units rewritten the same day; fresh check on every later unit of that family | §3 |
| Audit 2 | 4 units: 0 of 28 sampled failed; 96 checked; 1 incidental fail (miscited caption); 10 stale in one unit, one cause; all passed; 26 errata the same day | §4 |
| Audit 2's date, units, model | Not recorded | — |
| Audits due and not run | Audits 3 onward not run at 11 Nov 2026 | §9 |

**E. Recurring errors.** A figure the cited page does not carry; a qualifier the source does not carry; an author named wrongly; a law that had changed; a quotation the page does not hold; a count that did not add up; a product fact differing between two of the vendor's pages (§3, §5). Batches from one cause: 10 stale claims (§4), 3 missing deliverables (§3), 3 figure errors in one unit (§5 note). Invented sources: none recorded (§3). Counts by kind: not recorded.

**F. Figures.** Figures declared as data and drawn by script, each checked against the text by a separate agent (§6). 2 dropped under the early rule; one sitemap passed on its eighth check (§6). Figures declared, first-check failure rate, checker model: not recorded.

**G. Operation.** 2 writers lost to restarts, third resumed from files (§7). Transcripts missing in some sessions; scripted reading checks could not run (§7). One "fable" session resolved to a newer version; its checks re-owed (§7). Report writes refused on 4 rows, reports saved from replies (§7 notes). Private terms in a public build, 1 of 17 structure-audit findings (§7). Repeated publish: not recorded.

**H. Cost.** 53 chats in six days at the review: 31 Opus, 18 Fable, 4 both (§8). Six fresh agents a row on BW10 and DD-BW1 (§2 notes). Hours, money, tokens, usage, plan, effort, agent budgets: not recorded (§9; §7 note).

**I. Limits.** No control, no second project, no second person (§9). No before-and-after: Audit 2's units' fresh check not recorded. No measure of misses. Counts compiled by the project itself (header).

### Part 2 · Ten changes the record supports, ranked

Each change is for the case's own method. **Ranking rule** (stated opinion): by the number of recorded items behind the change, largest first, because a change resting on more instances is less likely to be answering a one-off; ties go to the change whose failure reached a filed text. The count column says what each rests on. The grade is the grade of the rule in the unit named; the case adds an anecdote to it and changes no grade.

| # | Change | Count behind it (Academy case file) | Unit that teaches it | Grade of the rule |
|---|---|---|---|---|
| 1 | **Keep the fresh check on every unit, and record for every unit whether it had one.** The check stays a stage with a written report; the course index gains a column saying whether each unit, history courses included, was checked, by which model, with what counts. | 28 of 36 drafts with an error; 58 errors, 598 findings (§5); 15 of the first 20 (§5); check counts in the case file for 38 of 205 units (§1, §5 and notes) | BW6 §4; BW2 §5 | Stated opinion on measured self-preference evidence (BW2 §5); documented practice, vendor (BW6 §4; DD-BW1 rule 3) |
| 2 | **Put "qualifiers and figures the source does not carry" first in the checker's brief,** above existence and format, and have the checker quote the source's sentence beside each claim it passes. | 23 of 91 claims failed at Audit 1, none invented; the pattern named (§3); 2 table rows on figures the vendor pages lacked (§3) | BW6 §2, §3 | Stated opinion, built on measured citation-error studies (BW6 §2) |
| 3 | **On any STALE, sweep every claim read from the same page or version, across all units,** and date each again (the sweep across units is this unit's extension of BW6 §5's sweep within one text). | 10 stale claims in one unit, one cause (§4) | BW6 §5; BW1 §4 | Stated opinion (BW6 §5) |
| 4 | **Record every finding's fate: applied, applied as corrected, rejected, with the reason.** The applier's practice of holding wrong fixes stays; the count it produces becomes the checkers' false-alarm measure. | 6 of 53 fixes held on two rows (§5 notes); 2 of 13 replacements failed a corrections check (§2 notes); rejected findings not counted (§5) | BW6 §6 | Stated opinion, built on vendor guidance (BW6 §4, §6) |
| 5 | **Give the writer the figure check as part of its own pass:** before hand-in, every label and number of every figure is found in the text. Keep fix-until-pass, and log each figure's checks. | 3 of DD-BW1's 3 errors in figures (§5 note); 2 figures dropped; one passed on its 8th check (§6) | BW7 §6; the course's shared preamble | Stated opinion, adapted from documented practice (BW7 §6) |
| 6 | **Give every agent a file to write its report to, and every writer working files that outlive it.** A report that can reach its file only through the main chat is a hand-off through conversation. | Report writes refused on 4 rows (§7 notes); 2 writers lost, the third resumed from files (§7) | BW7 §2; BW9 §9 | Stated opinion, on measured and vendor sources (BW7 §2) |
| 7 | **Check each deliverable against its brief's done-when lines before any unit is built on its material,** and at Audit time check that the deliverable exists before sampling its claims. | 3 of 3 deliverables missing at Audit 1; verdict rewrite (§3) | BW5, Deliverable 1d; BW3 | Documented practice (DD-BW1 rule 2) |
| 8 | **Log the model and version that ran, and keep each agent's transcript or reading list,** for every check and every main chat. | One "fable" session's checks re-owed (§7); 2 rows asked for Sonnet 5.5 and ran Opus 5.5 (§2 notes); transcripts missing in some sessions (§7) | BW7 §7; BW2 §7 | Stated opinion (BW7 §7) |
| 9 | **Run the private-terms check on the built site before each publish, and record the date it was added.** A check on the source folder does not check what the build renders. | 1 of 17 structure-audit findings: private terms in a public build (§7); date of the check not recorded (§7 note) | BW4 §7; BW10 §7 | Stated opinion (BW4 §7) |
| 10 | **Record hours and usage per unit,** at least the usage bar before and after each row and the clock time of each stage, so that changes 1 to 9 can be weighed against what they cost. | 0 measures of hours, money, tokens or effort across 205 units (§9; §7 note) | BW10 §1, §4; BW7 §7 | Stated opinion (this unit), on BW10 §1: no usage allowance is published, so the record must keep its own |

*Sources for Parts 1 and 2:* Academy case file §1 to §9, its notes of 15 and 16 Nov 2026 and its header; the units of this course named in each row. "205 units" is 194 at 11 Nov 2026 plus this course's 11 by 16 Nov 2026 (§1 and notes); "38" is the 36 of §5's table plus BW10 and DD-BW1.

### Part 3 · Template: your project's report

Fill it from your own records only. Where you have no record, write "not recorded": the gaps are findings. Keep the source column; DD-BW3 checks it.

**[Project name] · case report · as of [date you compiled it].** One project, one person: an anecdote.

**A. What was built**

| Line | Value | Source |
|---|---|---|
| Outputs | [count, by kind: reports, units, chapters, tools, posts] | [the file or log you counted from] |
| Output form | [what one output is: length, format, what it must contain] | [your spec, BW5] |
| Total size | [words, pages or files, if you have a count; else "not recorded"] | |
| Period | [first and last date of work] | [your changelog] |

**B. The method as run**

| Line | Value | Source |
|---|---|---|
| Stages | [your pipeline's stages, as run, not as planned: BW7] | [your procedure] |
| Writer model and effort | [model, version, effort; per output if you have it] | [your run log, BW7 §7] |
| Checker model, and whether its context was fresh | [model; new chat, subagent, or the writing chat] | [run log] |
| Changes while running | [each change to the method, with its date and the failure that prompted it] | [your changelog or decision log, BW5] |

**C. The check**

| Line | Value | Source |
|---|---|---|
| Outputs checked | [count, and the count not checked] | |
| Outputs with at least one error | [count of total, and the percentage] | |
| Findings by grade | [errors / should-fix / minor, or your own grades] | |
| Findings rejected or fixes held | [count, or "not recorded"] | |

**D. Sample audits**

| Line | Value | Source |
|---|---|---|
| Each audit | [date; outputs covered; claims sampled; FAILs; claims checked in full; STALE; verdict] | [the audit report, BW6 protocol] |
| What it led to | [the change made, with its date; or "errata only"] | |
| Audits due and not run | [count, by your own schedule] | |

**E. Recurring errors.** [each kind of error, with its count; batches traced to one cause; invented sources found, or "none"]

**F. Figures or other drawn or computed parts.** [declared; failed first check; checks to pass, typical and worst; dropped]

**G. Operation.** [lost sessions or agents; missing logs or transcripts; wrong model or version run; hand-offs that went through conversation; leaks; repeated publishes]

**H. Cost.** [chats, by model; agents per task; hours; usage bar before and after; money; or "not recorded" for each]

**I. Limits.** [what your record cannot show: no control, no second project, no measure of misses, who compiled the counts]

### Part 4 · Template: your ten changes

Rank by the count behind each change, largest first; a change you cannot tie to a count from Part 3 is not on the list. Each change names the unit of this course that teaches it, and that unit's grade.

| # | Change | Count behind it (your Part 3 line) | Unit that teaches it | Grade of the rule |
|---|---|---|---|---|
| 1 | [the change, written so you could tell next month whether you made it] | [the count, and the Part 3 line it comes from] | [BW unit and section] | [measured / documented practice / stated opinion, as that unit grades it] |
| 2 | [ ] | [ ] | [ ] | [ ] |
| 3 | [ ] | [ ] | [ ] | [ ] |
| 4 | [ ] | [ ] | [ ] | [ ] |
| 5 | [ ] | [ ] | [ ] | [ ] |
| 6 | [ ] | [ ] | [ ] | [ ] |
| 7 | [ ] | [ ] | [ ] | [ ] |
| 8 | [ ] | [ ] | [ ] | [ ] |
| 9 | [ ] | [ ] | [ ] | [ ] |
| 10 | [the change that records what your Part 3 most often marks "not recorded"] | [the number of "not recorded" lines it would fill] | [BW7 §7, BW10, or the unit for that field] | [ ] |

**Ranking rule:** [your rule, if it is not the count; say why]

## Sources

- Academy case file (`generator/data/building-with-ai/case-academy.md`), compiled 11 Nov 2026 from the project's own records, with notes of 15 and 16 Nov 2026: header, §1 to §9.
- Units of this course, pointed to by section: BW1 (Mental model), BW2 (Choosing the model and the effort), BW3 (Briefing: prompts that hold up), BW4 (Context engineering), BW5 (Specifying a project), BW6 (Research and verification), BW7 (Pipelines: raw material to finished output), BW9 (Agents), BW10 (Cost, limits, privacy), DD-BW1 (Deep dive: how the best practitioners work).
- The course's shared preamble, its rule for figures ("a figure adds no fact"), and Academy case file §6.
- Google. *Subagents*. Gemini CLI documentation (vendor). https://geminicli.com/docs/core/subagents/ (read 16 Nov 2026 for BW6 §8; not re-read for this unit).

This unit cites one outside page, the Gemini CLI page in §11, as BW6 §8 read it and not re-read: its brief limits it to the case file and the units of this course, and every other outside source behind a rule it names is cited in the unit that teaches the rule.

## Unsure list

# DD-BW2 · Unsure list

1. §4: "more audits were due than had run" is this unit's inference, labelled as such in the text, from 37 units of three courses at 11 Nov 2026 (case file §1) and "a sample audit every four units" (§2); the case file does not say whether the schedule counts units per course or across courses, nor whether the history courses' units are audited on it.
2. §2 item 2 and Part 1 B: "the method names no model for the fresh check" rests on case file §2 naming only a writing and an auditing model; a later record could name one.
3. §3: replacing the private courses' unit codes with row numbers keeps the case file's row order; the case file does not say the order is the order of writing, and the unit says so.
4. §5 and Part 2 change 4: "6 of 53 fixes held" adds BW10's 4 of 18 and DD-BW1's 2 of 35 (case file §5 notes); the notes describe the held fixes as "itself wrong" (BW10) and "itself incomplete or wrong" (DD-BW1), and the unit treats both as one count.
5. §8 and Part 2: "205 units" is 194 at 11 Nov 2026 plus this course's 11 by 16 Nov 2026; the case file does not say whether the other courses' counts changed between those dates.
6. §11: no vendor documentation was read for this unit (search off); the On other tools section points to BW2 §8, BW6 §8 and BW9 §10, which read the vendors' pages on 15 and 16 Nov 2026, and says no equivalent page on model-name resolution is cited in the course.
7. §10: the three verdicts (supported, consistent, silent) and the assignment of each of the seventeen rules are this unit's reading; a different reader could count "route by tier and effort" as partly supported, which would change the split to 10, 3, 4.
8. Part 2: the grades given for changes 5, 6, 8, 9 and 10 summarise the grade the named unit gives its rule; BW7 §6's grade ("this unit's adaptation, stated opinion" of Airflow's documented practice) and BW10 §4's (no explicit grade found for the budget rule) were read in passing, not re-checked line by line.
9. §1: "Each filed unit's reading page" rests on case file §1 (note of 16 Nov 2026, "the course's data file"); the note may cover only this course's reading pages.

Object: none

Fresh check 2026-11-16 (claude-opus-5-5): fix · 2 errors, 12 should-fix, 10 minor; report `audits/building-with-ai/fresh-check-DD-BW2.md`

Correction 2026-11-16, found by DD-BW2's filer (flag F112, as F52 and F98) and checked by a fresh agent (`audits/building-with-ai/corrections-2026-11-16-DD-BW2-r2-DD-BW2.md`): the opening describes the case in the case file's wording.
