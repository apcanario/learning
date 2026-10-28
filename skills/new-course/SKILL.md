---
name: new-course
description: Start a new course in the Learning Project, its syllabus, briefs and hub, from the template on design/theme.css. Use when asked to add a course, plan a new syllabus or start a new hub.
---

# Start a new course

A course is not started by writing units. It is started by a syllabus, a brief per unit and a hub, in that order. The rules are `method.md`; the requirement sets are on the Brand + AI hub's Build · Hub template page; the look is `design/theme.css` and nothing else.

## 1. Decide where it lives
- **A new culture in Personal Mythology** (Egypt, Persia, Norse and the others in the kit's `courses.py` `NEXT`): it joins the existing site, which is its hub. Follow the kit's `README.md`, "Adding a course": a syllabus in the same structure as `roman-syllabus.html` (units, modules, one `<pre>` prompt each, an audit unit last), a dict in `COURSES` in `courses.py` (removed from `NEXT`), a fragments folder, an empty prompts index, an empty `provenance.json` entry with the syllabus under `artefacts`; then `build.py` and `verify.py`. Briefs are the syllabus prompts plus `AGENT-SPEC.md` (add a section for the new course's conventions) and `WRITER-BRIEF.md`.
- **A new course in an existing hub** (a course C beside Brand + AI's A and B): add it to that hub's data folder.
- **A new family of courses:** a new hub. Steps 2 to 6 below.
Say which in the first line.

## 2. The frame (his decision, recorded)
Draft the frame before the syllabus: the pick, up to three reasons, the override condition, and where the evidence pushes back. Ask him to confirm or change the pick. One question, then build.

## 3. The syllabus
- 8–10 core units plus 2 deep dives, written last (the comparables, and the hard-number one), unless the subject's own logic needs another shape; say so if it does.
- A course goal in one sentence and three measurable outcomes, each mapped to the units that deliver it.
- Per unit: code, title, one-line scope, the deliverable it ships (built in full inside the unit), and the unit brief (`method.md` §4, Brief template: "Unit <code>, <Title>. [Search before writing.] Cover: … Deliverable: …").
- A search flag per unit: on only where facts are current.
- An explicit writing order, with interleaving where two units build the same asset, and an audit row after every fourth unit.

## 4. The shared preamble
Fill the template in `method.md` §4 once for the course. Reader: copied from `reader.md`, nothing added. Sourcing standard: Part 1 of `sourcing-standard.md` plus a new part for this course (its acceptable sources and labels), which you add to `sourcing-standard.md`. Tone: the Project's. End with "End with the unit's deliverable, built out in full, not described."

## 5. The hub
1. Copy `generator/data/_template/` to `generator/data/<slug>/`.
2. `units_data.py`: `PRE` (step 4) and the units (step 3). `hub.py`: replace every `⟨…⟩` (identity, courses with goal and outcomes, `ORDER`, frame, ledes, changelog v1). Prose blocks use theme classes only (`design/README.md` lists them); no `style` attribute except `--c`, `--cc`, `--hc`.
3. If the page needs a component the theme lacks, add it to `design/theme.css` section 5 with a one-line comment, then rebuild every hub, not just this one.
4. `python3 build_hub.py data/<slug>`, then `python3 check_page.py hubs/<page>.html` (dark and light, 400 px: no overflow, no target under 44 px).
5. Publish the page once as a new artifact (it is a new hub), then use that link for every later republish.

## 6. Register it in the Project
- `courses-index.md`: the hub row with its link; a section for the course with every unit in build order (status "not written", model, search flag, vault path `courses/<slug>/<code>-<slug>.md`); an audit counter at 0.
- `project-instructions.md`: add the course to the Purpose line only if it stays under 400 words.
- Reply with the hub link, the unit count, the first unit to write and its model. Do not write a unit in this chat.
