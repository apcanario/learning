---
name: new-course
description: Start a new course in the Learning Project, its syllabus, briefs and Academy course pages, from the template on design/theme.css. Use when asked to add a course or plan a new syllabus.
---

# Start a new course

A course is not started by writing units. It is started by a syllabus, a brief per unit and its pages in Academy, in that order. The rules are `method.md`; the requirement sets are `TEMPLATE_BLOCKS` in `generator/data/brand-ai/hub.py` (the syllabus and AI-rule requirements; the website ones are met by `design/theme.css`); the look is `design/theme.css` and nothing else.

## 1. Decide where it lives
- **A new culture in Personal Mythology** (Egypt, Persia, Norse and the others in the kit's `courses.py` `NEXT`): it joins the existing site, which is its hub. Follow the kit's `README.md`, "Adding a course": a syllabus in the same structure as `roman-syllabus.html` (units, modules, one `<pre>` prompt each, an audit unit last), a dict in `COURSES` in `courses.py` (removed from `NEXT`), a fragments folder, an empty prompts index, an empty `provenance.json` entry with the syllabus under `artefacts`; then `build.py` and `verify.py`. Briefs are the syllabus prompts plus `AGENT-SPEC.md` (add a section for the new course's conventions) and `WRITER-BRIEF.md`.
- **A new course beside Brand + AI's A and B** (a course C in the same data file): add it to `generator/data/brand-ai/` (`COURSES` in `hub.py`, its units in `units_data.py`, its track in `kit/courses.py` `tracks`); it appears in Academy on the next build.
- **A new markdown course family:** a new data folder. Steps 2 to 6 below.
Say which in the first line.

## 2. The frame (his decision, recorded)
Draft the frame before the syllabus: the pick, up to three reasons, the override condition, and where the evidence pushes back. Ask him to confirm or change the pick. One question, then build.

## 3. The syllabus
- 8–10 core units plus 2 or 3 deep dives, written last: the comparables and the hard-number one always; a third only when the subject has a documented practice worth verifying against its primary sources (as DD-B3 in course B). More than three, or another shape, needs the subject's own logic; say so if it does.
- A course goal in one sentence and three measurable outcomes, each mapped to the units that deliver it.
- Per unit: code, title, one-line scope, the deliverable it ships (built in full inside the unit), and the unit brief (`method.md` §4, Brief template: "Unit <code>, <Title>. [Search before writing.] Cover: … Deliverable: …").
- A search flag per unit: on only where facts are current.
- An explicit writing order, with interleaving where two units build the same asset, and an audit row after every fourth unit.

## 4. The shared preamble
Fill the template in `method.md` §4 once for the course. Reader: copied from `reader.md`, nothing added. Sourcing standard: Part 1 of `sourcing-standard.md` plus a new part for this course (its acceptable sources and labels), which you add to `sourcing-standard.md`. Tone: the Project's. End with "End with the unit's deliverable, built out in full, not described."

## 5. The course in Academy
1. Copy `generator/data/_template/` to `generator/data/<slug>/`.
2. `units_data.py`: `PRE` (step 4) and the units (step 3). `hub.py`: replace every `⟨…⟩` (identity, courses with goal and outcomes, `ORDER`, frame, ledes, changelog v1). Prose blocks use theme classes only (`design/README.md` lists them); no `style` attribute except `--c`, `--cc`, `--hc`.
3. `kit/courses.py`: a dict with `family='markdown'`, `data='generator/data/<slug>/hub.py'` and a `tracks` map (course key → track id and short name) in `COURSES`; a new track in `THEMES` if none fits.
4. If a page needs a component the theme lacks, add it to `design/theme.css` section 5 with a one-line comment and copy it to `kit/shell.css`.
5. `cd kit && python3 build.py && python3 verify.py` (ALL CHECKS PASSED), then publish Academy: the artifact (read first, publish once with its `url`), then `./deploy.sh`.

## 6. Register it in the Project
- `courses-index.md`: a section for the course with every unit in build order (status "not written", model, search flag, vault path `courses/<slug>/<code>-<slug>.md`); an audit counter at 0.
- `project-instructions.md`: add the course to the Purpose line only if it stays under 400 words.
- Reply with the course's Academy anchor, the unit count, the first unit to write and its model. Do not write a unit in this chat.
