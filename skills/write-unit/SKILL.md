---
name: write-unit
description: Write one course unit in the Learning Project from its brief, in full, with its deliverable. Use when asked to write a unit or module (B1, A3, Rome 11.3) or when a unit brief is pasted.
---

# Write a unit

One chat writes one unit. The method is `method.md` (§2 anatomy, §3 order, §4 writing); the checklist is `sourcing-standard.md`; the reader is `reader.md`.

**The course's entry.** Every course is one entry, `courses/<id>/course.toml`, read by `kit/courses.py` (S-DEC1). For a markdown course (Brand + AI, User Experience, any new one) its entry gives the paths this skill uses: `data` (the course's `hub.py`; its `units_data.py` sits in the same folder), `vault` (the folder of filed units) and `sourcing_part` (its own part of `sourcing-standard.md`; without the key, Part 2 for a markdown course and Part 3 for a history course, as `kit/howbuilt.py` has it). Below, `<data>`, `<data folder>`, `<vault>` and `<sourcing part>` mean those values for the unit's course; no step names one course's folders.

## 0. In a thin main chat (S-BW1)
A writing row's chat runs on Sonnet 5.5 and never opens the unit: the writer is a fresh Opus 5.5 agent on a packet that `python3 kit/thin.py stage writer --row <row> <folder>` builds, it writes `out/unit.md`, `out/unsure.md` and `out/notes.md`, and it replies to the chat in at most six lines. Everything below is the agent's.

## 1. Check you may start
- This chat must be new, or an isolated agent context started for this unit alone (method §4, P31). If it already holds another unit's work, stop and say: "One chat per unit: start a new chat for <code>."
- Check the model you are running as. Units are written with Opus 5.5 unless `courses-index.md` names another model for this unit. If they differ, say so in your first line and stop.
- Open `courses-index.md`. If an earlier unit has an open REWRITE verdict, stop and say in your first line that the rewrite comes first.
- Every unit this one points back to must be filed (history: every report its lane note names is registered). If one is not, stop and name it.

## 2. Assemble the brief (never reword it)
- **Markdown course (Brand + AI, User Experience):** use the brief pasted from the course's Briefs page in Academy. If none was pasted, build it exactly as the hub does, with `kit/mdcourse.py`'s `open_brief(d, sc, u)`: `PRE` from `<data folder>/units_data.py` with `{GOAL}` replaced by the course goal in `<data>`, a blank line, then, where the course data has `AIMS` (User Experience since S-1, 3 Nov 2026), the unit's Aim, Takes and Gives lines and a blank line, then the unit's brief (fifth field of its entry). The Aim says what the reader can do after the unit; Takes names the filed units the writer must read; Gives names what later units will take from this one, so the deliverable is built for them. A course with a Perqo-style register of invented facts (`<data folder>/perqo-facts.md`) adds it to the packet: every invented fact is checked against it and new ones are appended at filing.
- **Personal Mythology:** the module's `<pre>` prompt in its syllabus (`roman-syllabus.html` or `greek-syllabus.html`, `data-id="<id>"`) is the contract. Read `AGENT-SPEC.md` and `WRITER-BRIEF.md` in full, the module's lane note in `kit/archive/LANES.md`, the quality-bar reports `WRITER-BRIEF.md` names, and every extra file the lane note lists. If a needed file is not attached, ask for it before writing.

## 3. Set the search mode
Read the unit's search flag in `courses-index.md`.
- **on:** search before writing. Every fact that can change (rules, thresholds, prices, plan limits, model lineups, benchmarks, regulatory status) is dated in the text.
- **off:** write from knowledge; search only to verify a specific date, figure or contested point you are unsure of. Every history module is off.

## 4. Plan, then write in one pass
- List the brief's items in order; give each a section and a rough word budget. The topic decides the length: never pad, never cut substance to a number.
- Write the whole unit, in the course's format (`method.md` §2):
  - **Markdown course:** Markdown long-form report; headed sections answering the brief in order; claims sourced in place with links; anecdote, vendor and correlational data labelled; then the deliverable named in the unit's "Ships" line, **built in full** (the actual statement, table, calendar, skill, model; never a description of it); then a `## Sources` list of every link cited.
  - **Personal Mythology:** a Markdown report exactly as `AGENT-SPEC.md` specifies (since P71-3, 1 Nov 2026: front matter and title, then 6–10 `## ` sections, dispute boxes opening `**Where sources disagree.**` with a named side each, `## Self-test` with 10 numbered questions each followed by its indented `Answer:` paragraph, `## Carry forward` with exactly 3 numbered items; no HTML); British spelling; no em dashes; no preamble. Never use the Artifact tool or any publishing tool.
- Begin with the first section. No preamble, no summary of what follows, no closing filler, no motivational language.

## 4b. Figure pass (after the draft)
With the whole draft written, go through it section by section and ask of each: does this content have a shape? Where it does, declare the matching figure kind from `kit/viz.py`'s docstring; where it does not, declare nothing. A figure is drawn from the unit's own sourced text, never the other way round.

| The content is | Kind |
|---|---|
| dated events | `timeline` |
| a sequence of steps or stages | `flow` |
| a hierarchy or a line of descent | `tree`, or `sitemap` for a site's pages |
| numbers compared across items | `compare` (one value each) or `bars` (several series, grouped or stacked) |
| a trend over time | `line` |
| two measures of the same items | `scatter` |
| competing estimates of one quantity | `range` |
| a rule with branches | `decision` |
| roles or items by sections (who may do what, what sits where) | `matrix` |
| a grid of numbers (rows by columns) | `matrix` with `"numeric": true` |
| a lifecycle | `states` |
| a journey across actors | `swimlanes` |
| screens and the moves between them | `wireflow` |
| things and their relationships | `objects` |

- **Source.** Every label, date and number in a figure already appears in the unit's text, sourced there. A figure adds no fact.
- **Place.** Put the figure directly after the paragraph or table it draws, with at most one plain sentence introducing it.
- **Hidden answers.** No figure draws what a Self-test or exam hides behind its answer box (a model answer, a key): a figure sits at the top level and would show the answer under its question. An exam's figures draw only what its visible questions give.
- **How many.** One to four figures a unit is a guide, and none where nothing has a shape; a figure is never added for decoration. A brief that names its own number stands (the User Experience briefs ask for three to eight).
- **Caption.** Say what the figure shows and where its data comes from: the section of this unit and the source it cites there (author, work, line or page; organisation, report, date). A figure redrawn or adapted from a source credits it.
- **Syntax.** Every course (history too, since P71-3): a fenced ` ```viz ` block holding the JSON, `kind` and `caption` inside it (`kit/WRITER-BRIEF.md`).
- **Draw it.** Before handing in, render every figure with `viz.render` (from `kit/`: `python3 -c "import json, viz; viz.render(json.load(open('fig.json')))"`, or `python3 check.py ../courses/<course>/<id>-<slug>.md` for a history report). A figure that raises is fixed until it draws, never dropped and never left to break the build (Pedro, 3 Nov 2026: figures are not dropped). Filing then draws each figure as the reader meets it, every frame of a figure wider than its column stacked in one sheet (`verify.py --shots`, P89).

## 4c. Sources and attribution (S-BW1, 15 Nov 2026; from row F-PB, where attribution failed at 8.8 claims per 100 and numbers at 1.1)
- **A Sources title is the page's own headline**, as the page shows it: never its URL slug, never a site name joined to a page name ("Reaching 1,000 YouTube Subscribers: What 32.9 Million Channels Reveal", not "uploads-1000-subscribers" and not "vidIQ Research: Uploads"). Check each title against its page before handing in; a page whose headline you could not read is listed on the unsure list with the title left as the organisation, the document type and the date.
- **A quotation is credited to the speaker**, with the outlet named as where it was said ("Kim Boyd, in Net Influencer"), never to the outlet alone.
- **A paraphrase is never in quotation marks.** Words inside quotation marks are exactly the source's words, under fifteen words; anything else is written without them.
- **A figure is cited to the page that states it for that thing**: the study that measured it, not a page that mentions the topic and not a page that repeats the number. When two pages give it, cite the original and say the other repeats it.

## 5. Check before handing in
- Run `sourcing-standard.md` Part 1 and `<sourcing part>` over every checkable claim. Fix what fails; a claim you cannot source is said to be unsourced or removed (and never enters the deliverable).
- Confirm the closing artefact agrees with the body and the deliverable (or Self-test) is complete.
- Check every figure against the text: each label and number is in the unit, the caption names the section and the source, the kind fits the shape (§4b).
- Check §4c over every Sources entry, quotation and figure citation.
- Write the unsure list: up to ten claims you could not verify, one per line. Then one last line (P96, 8 Nov 2026): `Object: <the object the unit discusses most, with the section that discusses it at length>`, or `Object: none` when the unit discusses no object at length, only in passing. Filing maps the page's relief from it (`file-unit`); name the thing the text discusses (the lekythos, the Twelve Tables, the phone on a tripod), not a theme.

## 6. Hand in
- **Markdown course:** one file `<code>-<slug>.md`, filed later in `<vault>` (code, then the title lower-cased, hyphenated, accents and punctuation dropped), starting with the front matter from `method.md` §7 (code, title, course, model, written date, search flag).
- **Personal Mythology:** two files: `<id>-<slug>.md` (front matter, title, then the report in Markdown; the only copy, since P71-3), and `bibliography-r-<id>.md` (the curated bibliography: ancient sources with passages and edition where known; modern works with author, full title, place or journal, year of the edition named).
- Send the files. Reply with one line (unit, word count, search used or not), one line per figure (kind, section, what it draws) and the unsure list with its Object line. Filing is a separate step (`file-unit`).
