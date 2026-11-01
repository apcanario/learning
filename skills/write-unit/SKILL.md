---
name: write-unit
description: Write one course unit in the Learning Project from its brief, in full, with its deliverable. Use when asked to write a unit or module (B1, A3, Rome 11.3) or when a unit brief is pasted.
---

# Write a unit

One chat writes one unit. The method is `method.md` (§2 anatomy, §3 order, §4 writing); the checklist is `sourcing-standard.md`; the reader is `reader.md`.

**The course's entry.** Every course is one entry in `kit/courses.py`. For a markdown course (Brand + AI, User Experience, any new one) its entry gives the paths this skill uses: `data` (the course's `hub.py`; its `units_data.py` sits in the same folder), `vault` (the folder of filed units) and `sourcing_part` (its own part of `sourcing-standard.md`; without the key, Part 2 for a markdown course and Part 3 for a history course, as `kit/howbuilt.py` has it). Below, `<data>`, `<data folder>`, `<vault>` and `<sourcing part>` mean those values for the unit's course; no step names one course's folders.

## 1. Check you may start
- This chat must be new, or an isolated agent context started for this unit alone (method §4, P31). If it already holds another unit's work, stop and say: "One chat per unit: start a new chat for <code>."
- Check the model you are running as. Units are written with Opus 5.5 unless `courses-index.md` names another model for this unit (Brand + AI DD-B2: Fable 5.1). If they differ, say so in your first line and stop.
- Open `courses-index.md`. If the unit's hub shows four units since the last audit, or an open REWRITE, stop and say in your first line that the audit comes first (`audit-units`).
- Every unit this one points back to must be filed (history: every report its lane note names is registered). If one is not, stop and name it.

## 2. Assemble the brief (never reword it)
- **Markdown course (Brand + AI, User Experience):** use the brief pasted from the course's Briefs page in Academy. If none was pasted, build it exactly as the hub does: `PRE` from `<data folder>/units_data.py` with `{GOAL}` replaced by the course goal in `<data>`, a blank line, then the unit's brief (fifth field of its entry).
- **Personal Mythology:** the module's `<pre>` prompt in its syllabus (`roman-syllabus.html` or `greek-syllabus.html`, `data-id="<id>"`) is the contract. Read `AGENT-SPEC.md` and `WRITER-BRIEF.md` in full, the module's lane note in `BACKLOG.md`, the quality-bar reports `WRITER-BRIEF.md` names, and every extra file the lane note lists. If a needed file is not attached, ask for it before writing.

## 3. Set the search mode
Read the unit's search flag in `courses-index.md`.
- **on:** search before writing. Every fact that can change (rules, thresholds, prices, plan limits, model lineups, benchmarks, regulatory status) is dated in the text.
- **off:** write from knowledge; search only to verify a specific date, figure or contested point you are unsure of. Every history module is off.

## 4. Plan, then write in one pass
- List the brief's items in order; give each a section and a rough word budget. The topic decides the length: never pad, never cut substance to a number.
- Write the whole unit, in the course's format (`method.md` §2):
  - **Markdown course:** Markdown long-form report; headed sections answering the brief in order; claims sourced in place with links; anecdote, vendor and correlational data labelled; then the deliverable named in the unit's "Ships" line, **built in full** (the actual statement, table, calendar, skill, model; never a description of it); then a `## Sources` list of every link cited.
  - **Personal Mythology:** an HTML fragment exactly as `AGENT-SPEC.md` specifies (6–10 `h2`, dispute boxes with a named side each, `Self-test` with 10 questions and answers in `details`, `Carry forward` with exactly 3 items); British spelling; no em dashes; no preamble. Never use the Artifact tool or any publishing tool.
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
- **Hidden answers.** No figure draws what a Self-test or exam hides in `<details>` (a model answer, a key): a figure sits at the top level and would show the answer under its question. An exam's figures draw only what its visible questions give.
- **How many.** One to four figures a unit is a guide, and none where nothing has a shape; a figure is never added for decoration. A brief that names its own number stands (the User Experience briefs ask for three to eight).
- **Caption.** Say what the figure shows and where its data comes from: the section of this unit and the source it cites there (author, work, line or page; organisation, report, date). A figure redrawn or adapted from a source credits it.
- **Syntax.** Markdown units (Brand + AI, User Experience): a fenced ` ```viz ` block holding the JSON, `kind` and `caption` inside it. History fragments: `<figure class="viz" data-viz="<kind>"><script type="application/json">{…}</script><figcaption>…</figcaption></figure>` (`kit/WRITER-BRIEF.md`).
- **Draw it.** Before handing in, render every figure with `viz.render` (from `kit/`: `python3 -c "import json, viz; viz.render(json.load(open('fig.json')))"`, or `python3 check.py <course>/r-<id>.html` for a history fragment). A figure that raises is fixed or dropped, never left to break the build.

## 5. Check before handing in
- Run `sourcing-standard.md` Part 1 and `<sourcing part>` over every checkable claim. Fix what fails; a claim you cannot source is said to be unsourced or removed (and never enters the deliverable).
- Confirm the closing artefact agrees with the body and the deliverable (or Self-test) is complete.
- Check every figure against the text: each label and number is in the unit, the caption names the section and the source, the kind fits the shape (§4b).
- Write the unsure list: up to ten claims you could not verify, one per line.

## 6. Hand in
- **Markdown course:** one file `<code>-<slug>.md`, filed later in `<vault>` (code, then the title lower-cased, hyphenated, accents and punctuation dropped), starting with the front matter from `method.md` §7 (code, title, course, model, written date, search flag).
- **Personal Mythology:** three files: `<id>-<slug>.md` (front matter, then the fragment unchanged), `r-<id>.html` (the fragment alone), and `bibliography-r-<id>.md` (the curated bibliography: ancient sources with passages and edition where known; modern works with author, full title, place or journal, year of the edition named).
- Send the files. Reply with one line (unit, word count, search used or not), one line per figure (kind, section, what it draws) and the unsure list. Filing is a separate step (`file-unit`).
