---
name: file-unit
description: File a finished Learning Project unit, then update its course data (reading page, counters, changelog), rebuild Academy, verify and publish it. Use after a unit is written or when asked to file one.
---

# File a unit

Turns a written unit into a filed one: vault, course data, Academy, index. The procedure is `method.md` §7. The design rule holds throughout: Academy is rebuilt by `kit/build.py` from `design/theme.css`; nothing is styled by hand.

**The course's entry.** Every course is one entry in `kit/courses.py`. For a markdown course (Brand + AI, User Experience, any new one) the entry gives the paths used below: `id` (its audit reports go in `audits/<id>/`), `data` (the course's `hub.py`), `vault` (the folder the unit is filed in) and `sourcing_part` (its own part of `sourcing-standard.md`; Part 2 for a markdown course without the key). Below, `<id>`, `<data>` and `<vault>` mean those values for the unit's course; no step names one course's folders.

## 1. Check the unit
- It is complete: every brief item covered, the deliverable (a markdown course) or Self-test and Carry forward (history) built in full, a Sources list or bibliography file present.
- Its figures (if any) were checked: by the fresh check (a markdown course: section (7) of the fresh-check report) or the fresh checker (history), each figure PASS or fixed.
- It starts with the front matter (code, title, course, model, written, search). Add it if missing; the model is the one that actually wrote the unit.
- If anything is missing, stop and say what; do not file a partial unit.

## 2. Vault
Save to `<vault>/<code>-<slug>.md` for a markdown course, `courses/<course>/<id>-<slug>.md` for a history course (`greece` or `rome`); slug = the title lower-cased, hyphenated, accents and punctuation dropped. If the vault is connected (GitHub), commit it there with the message `<id> <code>: <title>` (`<id>`: the course entry's id, `greece` or `rome` for history); otherwise send the file and say where it goes.

## 3. Personal Mythology: the kit (`kit/` in the repo)
1. The report itself is its vault file (§2; since P71-3, 1 Nov 2026, there is no copy in the kit: `build.py` reads the vault through `vault.py`). Save the bibliography as `bibliography/<course>/r-<id>.md`; the writer's unsure list as `reviews/<session folder>/<course>-<id>-writer.md`.
2. `python3 check.py ../courses/<course>/<id>-<slug>.md` until OK.
3. Fresh check: a new agent or chat that has not seen the unit written, briefed with `reviews/units-9-13/BRIEF.md`; it writes findings and never edits. Verify every finding before applying it, as exact replacements; log a paragraph in the session's `log.md`.
4. `python3 register.py <course> "<model>" <id>`; read the `review_due.py` line it prints.
5. When the syllabus unit is complete: `python3 crosscheck.py <course> <ids>` and check every pointer between its modules.
6. Make sure the kit's `shell.css` is a copy of `design/theme.css`; if not, copy it.
7. Update `docs/courses-index.md` (§6) first, then `python3 build.py` and `python3 verify.py` (must print ALL CHECKS PASSED; it runs `index_check.py` on the index).
8. Look at the new page once at the three widths: `python3 verify.py --shots <dir> --page <panel id>` (the report's panel id, e.g. `rm11-3`), then open its six screenshots (phone, tablet, desktop; dark and light) with the Read tool and check by eye what the checks cannot: the hero and the first screen read as one page, nothing is cut at the column edge, tables and code scroll inside their box, the sidebar carries the right current item. The same run saves each figure of that panel on its own (`<width>-<panel>-fig-<nn>-<kind>-<theme>.png`, P41): open every one at phone width (390 px), dark and light, and check that its text sits inside its boxes, nothing overlaps, the caption is under it and, when it is wider than the column, it scrolls in its frame with the cue line; then open its frames sheet (`<width>-<panel>-fig-<nn>-<kind>-frames-<theme>.png`, P89: every frame a reader scrolls it across, stacked and numbered) at phone and desktop width, dark and light, and check the drawing is whole across the frames. A figure fault is fixed in the unit's declaration (shorter labels, another `per_row`, a box moved) or, if it is the drawing, in `kit/viz.py` or `design/theme.css`, never by styling the page. A fault is fixed in `design/theme.css` (then `cp design/theme.css kit/shell.css`), never in the page; rebuild and verify again.
9. Publish `academy/` to https://claude.ai/artifact/WwmQpUSqAUJvrcmLczppEH: read it with the Artifact tool first, then publish once with that `url`, `file_path` = `kit/academy/index.html` (the shell), `root` = `kit/academy` and `files` = the list `python3 publish_files.py` prints (the fetched files; one publish per printed line), never as a new artifact, never forced. Then `./deploy.sh`, which pushes the same build to GitHub Pages (https://apcanario.github.io/academy/). "Publish Academy" always means both: the artifact, then `deploy.sh`.
10. Add the session to `CHANGELOG.md` and update `README.md` "Where things stand".

## 4. Markdown course: the course data
The vault file saved in §2 is the unit Academy renders (A5): there is no copy under `generator/`, and the unit counts as written because its file is in `<vault>` with front matter. In `<data>` (AD5: the course's data file; `kit/build.py` reads it through `kit/mdcourse.py`):
1. Add a `READINGS` entry (`id='read-<code lower>'`, `course`, `title`, `covers=[code]`, `name` for the top bar, an `intro` of one paragraph saying what the unit is, when it was written, with or without search, and its known gaps from the unsure list). No `md` path: the build reads the vault file, and `WRITTEN` is derived from the vault. Without an entry the unit still gets a page, with a one-line intro from its front matter; write the entry.
2. Set `STATUS[code] = 'written <d Mon>'`; move `NEXT_UNIT` to the next row of `ORDER` and update `NEXT_AUDIT`; bump `VERSION`; add a `CHANGELOG` row at the top (`'<yyyy-mm-dd hh:mm>', '<version>. <code> <title> written (<model>) and filed; <what changed on the hub>.'`).
3. Do not edit `units_data.py`: briefs are never reworded. The unit's links join the course's Bibliography page automatically.

## 5. Rebuild, check, publish Academy (both families)
1. Update `docs/courses-index.md` first (§6), then `cd kit && python3 build.py`, then `python3 verify.py` (ALL CHECKS PASSED: three widths, dark and light, 6 px gaps, 44 px targets, no overflow, no console error, the navigation walk, and `index_check.py` on the index). Fix a layout failure in `design/theme.css` only (then `cp design/theme.css kit/shell.css`), never in a page.
2. Look at the new page once at the three widths: `python3 verify.py --shots <dir> --page <panel id>` (`read-<code lower>` for a markdown-course unit, the report id for history), then open its six screenshots (phone, tablet, desktop; dark and light) with the Read tool and check by eye what the checks cannot: hero and first screen read as one page, nothing cut at the column edge, tables and code scrolling inside their box, the right current item in the sidebar. The same run saves each figure of that panel on its own (`<width>-<panel>-fig-<nn>-<kind>-<theme>.png`, P41): open every one at phone width (390 px), dark and light, and check that its text sits inside its boxes, nothing overlaps, the caption is under it and, when it is wider than the column, it scrolls in its frame with the cue line; then open its frames sheet (`<width>-<panel>-fig-<nn>-<kind>-frames-<theme>.png`, P89: every frame a reader scrolls it across, stacked and numbered) at phone and desktop width, dark and light, and check the drawing is whole across the frames. A figure fault is fixed in the unit's declaration (shorter labels, another `per_row`, a box moved) or, if it is the drawing, in `kit/viz.py` or `design/theme.css`, never by styling the page. A fault goes to `design/theme.css`, never the page; rebuild and verify again.
3. Publish `kit/academy/` to https://claude.ai/artifact/WwmQpUSqAUJvrcmLczppEH: read it with the Artifact tool first, then publish once with that `url`, `file_path` = `kit/academy/index.html` (the shell), `root` = `kit/academy` and `files` = the list `python3 publish_files.py` prints (the fetched files; one publish per printed line), never as a new artifact, never forced. Then `./deploy.sh` so https://apcanario.github.io/academy/ carries the same build. "Publish Academy" always means both.

## 6. Index and count
- `courses-index.md`: the unit's row (status "written <date>", model, path to the vault file); for a search-on unit, a row in "Staleness checks due" (written + six months); the hub's audit counter plus one; the "N of M" line above the course's table. `python3 kit/index_check.py` until it prints "courses-index.md matches the sources" (§5 runs it again through `verify.py`).
- If the counter reaches four, the reply's first line says: "Audit due before the next unit (audit-units)."
- Markdown course: every unit gets a fresh check before filing (`audit-units` §3b, "Fresh check of one markdown-course unit"; Brand + AI since Audit 1, 28 Oct 2026). A unit is not filed unless the fresh-check line ends its unsure list, `audits/<id>/fresh-check-<code>.md` exists as `audits/README.md` sets out, and that file's `verdict` matches the line (verdict and counts). The path goes on the unit's `courses-index.md` row.
- Commit and push `apcanario/learning` with the message `<id> <code>: filed`.
- Where the course keeps a register of its invented facts (`generator/data/ux/perqo-facts.md`, S-1): append every fact the unit set, with its section, and list what the unit left free; a fact the unit changed is a fix to the earlier unit, made in the same chat.
- Re-upload the changed Project knowledge files (`courses-index.md`, the course's `hub.py`, the unit from its vault folder).
- Reply with what was filed where, the Academy version, and the counter. Nothing else.
