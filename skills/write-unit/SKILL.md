---
name: write-unit
description: Write one course unit in the Learning Project from its brief, in full, with its deliverable. Use when asked to write a unit or module (B1, A3, Rome 11.3) or when a unit brief is pasted.
---

# Write a unit

One chat writes one unit. The method is `method.md` (§2 anatomy, §3 order, §4 writing); the checklist is `sourcing-standard.md`; the reader is `reader.md`.

## 1. Check you may start
- This chat must be new. If it already holds another unit's work, stop and say: "One chat per unit: start a new chat for <code>."
- Check the model you are running as. Units are written with Opus 5.5 unless `courses-index.md` names another model for this unit (Brand + AI DD-B2: Fable 5.1). If they differ, say so in your first line and stop.
- Open `courses-index.md`. If the unit's hub shows four units since the last audit, or an open REWRITE, stop and say in your first line that the audit comes first (`audit-units`).
- Every unit this one points back to must be filed (history: every report its lane note names is registered). If one is not, stop and name it.

## 2. Assemble the brief (never reword it)
- **Brand + AI:** use the brief pasted from the hub's Build · Briefs page. If none was pasted, build it exactly as the hub does: `PRE` from `generator/data/brand-ai/units_data.py` with `{GOAL}` replaced by the course goal in `generator/data/brand-ai/hub.py`, a blank line, then the unit's brief (fifth field of its entry).
- **Personal Mythology:** the module's `<pre>` prompt in its syllabus (`roman-syllabus.html` or `greek-syllabus.html`, `data-id="<id>"`) is the contract. Read `AGENT-SPEC.md` and `WRITER-BRIEF.md` in full, the module's lane note in `BACKLOG.md`, the quality-bar reports `WRITER-BRIEF.md` names, and every extra file the lane note lists. If a needed file is not attached, ask for it before writing.

## 3. Set the search mode
Read the unit's search flag in `courses-index.md`.
- **on:** search before writing. Every fact that can change (rules, thresholds, prices, plan limits, model lineups, benchmarks, regulatory status) is dated in the text.
- **off:** write from knowledge; search only to verify a specific date, figure or contested point you are unsure of. Every history module is off.

## 4. Plan, then write in one pass
- List the brief's items in order; give each a section and a rough word budget. The topic decides the length: never pad, never cut substance to a number.
- Write the whole unit, in the course's format (`method.md` §2):
  - **Brand + AI:** Markdown long-form report; headed sections answering the brief in order; claims sourced in place with links; anecdote, vendor and correlational data labelled; then the deliverable named in the unit's "Ships" line, **built in full** (the actual statement, table, calendar, skill, model; never a description of it); then a `## Sources` list of every link cited.
  - **Personal Mythology:** an HTML fragment exactly as `AGENT-SPEC.md` specifies (6–10 `h2`, dispute boxes with a named side each, `Self-test` with 10 questions and answers in `details`, `Carry forward` with exactly 3 items); British spelling; no em dashes; no preamble. Never use the Artifact tool or any publishing tool.
- Begin with the first section. No preamble, no summary of what follows, no closing filler, no motivational language.

## 5. Check before handing in
- Run `sourcing-standard.md` Part 1 and the course's part over every checkable claim. Fix what fails; a claim you cannot source is said to be unsourced or removed (and never enters the deliverable).
- Confirm the closing artefact agrees with the body and the deliverable (or Self-test) is complete.
- Write the unsure list: up to ten claims you could not verify, one per line.

## 6. Hand in
- **Brand + AI:** one file `<code>-<slug>.md` (code, then the title lower-cased, hyphenated, accents and punctuation dropped), starting with the front matter from `method.md` §7 (code, title, course, model, written date, search flag).
- **Personal Mythology:** three files: `<id>-<slug>.md` (front matter, then the fragment unchanged), `r-<id>.html` (the fragment alone), and `bibliography-r-<id>.md` (the curated bibliography: ancient sources with passages and edition where known; modern works with author, full title, place or journal, year of the edition named).
- Send the files. Reply with one line (unit, word count, search used or not) and the unsure list. Filing is a separate step (`file-unit`).
