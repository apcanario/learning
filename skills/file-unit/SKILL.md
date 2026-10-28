---
name: file-unit
description: File a finished Learning Project unit, then update its course data (reading page, counters, changelog), rebuild Academy, verify and publish it. Use after a unit is written or when asked to file one.
---

# File a unit

Turns a written unit into a filed one: vault, course data, Academy, index. The procedure is `method.md` §7. The design rule holds throughout: Academy is rebuilt by `kit/build.py` from `design/theme.css`; nothing is styled by hand.

## 1. Check the unit
- It is complete: every brief item covered, the deliverable (Brand + AI) or Self-test and Carry forward (history) built in full, a Sources list or bibliography file present.
- It starts with the front matter (code, title, course, model, written, search). Add it if missing; the model is the one that actually wrote the unit.
- If anything is missing, stop and say what; do not file a partial unit.

## 2. Vault
Save to `courses/<course>/<code>-<slug>.md` (`brand-ai`, `greece` or `rome`; slug = the title lower-cased, hyphenated, accents and punctuation dropped). If the vault is connected (GitHub), commit it there with the message `<course> <code>: <title>`; otherwise send the file and say where it goes.

## 3. Personal Mythology: the kit (`kit/` in the repo)
1. Save the fragment without front matter as `<course>/r-<id>.html`; the bibliography as `bibliography/<course>/r-<id>.md`; the writer's unsure list as `reviews/<session folder>/<course>-<id>-writer.md`.
2. `python3 check.py <course>/r-<id>.html` until OK.
3. Fresh check: a new agent or chat that has not seen the unit written, briefed with `reviews/units-9-13/BRIEF.md`; it writes findings and never edits. Verify every finding before applying it, as exact replacements; log a paragraph in the session's `log.md`.
4. `python3 register.py <course> "<model>" <id>`; read the `review_due.py` line it prints.
5. When the syllabus unit is complete: `python3 crosscheck.py <course> <ids>` and check every pointer between its modules.
6. Make sure the kit's `shell.css` is a copy of `design/theme.css`; if not, copy it.
7. `python3 build.py`, then `python3 verify.py` (must print ALL CHECKS PASSED).
8. Look at the new page once at the three widths: `python3 verify.py --shots <dir> --page <panel id>` (the report's panel id, e.g. `rm11-3`), then open its six screenshots (phone, tablet, desktop; dark and light) with the Read tool and check by eye what the checks cannot: the hero and the first screen read as one page, nothing is cut at the column edge, tables and code scroll inside their box, the sidebar carries the right current item. A fault is fixed in `design/theme.css` (then `cp design/theme.css kit/shell.css`), never in the page; rebuild and verify again.
9. Publish `personal-mythology.html` to https://claude.ai/artifact/WwmQpUSqAUJvrcmLczppEH: read it with the Artifact tool first, publish once with that `url`, never as a new artifact, never forced. Then `./deploy.sh`, which pushes the same build to GitHub Pages (https://apcanario.github.io/academy/). "Publish Academy" always means both: the artifact, then `deploy.sh`.
10. Add the session to `CHANGELOG.md` and update `README.md` "Where things stand".

## 4. Brand + AI: the course data
In `generator/data/brand-ai/` (AD5: `hub.py` stays the course's data file; `kit/build.py` reads it through `kit/mdcourse.py`):
1. Copy the unit to `units/<code>-<slug>.md`.
2. `hub.py`: add a `READINGS` entry (`id='read-<code lower>'`, `md='units/<file>'`, `course`, `title`, `covers=[code]`, `name` for the top bar, an `intro` of one paragraph saying what the unit is, when it was written, with or without search, and its known gaps from the unsure list); map `WRITTEN[code]` to that id; set `STATUS[code] = 'written <d Mon>'`; move `NEXT_UNIT` to the next row of `ORDER` and update `NEXT_AUDIT`; bump `VERSION`; add a `CHANGELOG` row at the top (`'<yyyy-mm-dd hh:mm>', '<version>. <code> <title> written (<model>) and filed; <what changed on the hub>.'`).
3. Do not edit `units_data.py`: briefs are never reworded. The unit's links join the course's Bibliography page automatically.

## 5. Rebuild, check, publish Academy (both families)
1. `cd kit && python3 build.py`, then `python3 verify.py` (ALL CHECKS PASSED: three widths, dark and light, 6 px gaps, 44 px targets, no overflow, no console error, the navigation walk). Fix a layout failure in `design/theme.css` only (then `cp design/theme.css kit/shell.css`), never in a page.
2. Look at the new page once at the three widths: `python3 verify.py --shots <dir> --page <panel id>` (`read-<code lower>` for a Brand + AI unit, the report id for history), then open its six screenshots (phone, tablet, desktop; dark and light) with the Read tool and check by eye what the checks cannot: hero and first screen read as one page, nothing cut at the column edge, tables and code scrolling inside their box, the right current item in the sidebar. A fault goes to `design/theme.css`, never the page; rebuild and verify again.
3. Publish `kit/personal-mythology.html` to https://claude.ai/artifact/WwmQpUSqAUJvrcmLczppEH: read it with the Artifact tool first, publish once with that `url`, never as a new artifact, never forced. Then `./deploy.sh` so https://apcanario.github.io/academy/ carries the same build. "Publish Academy" always means both.

## 6. Index and count
- `courses-index.md`: the unit's row (status "written <date>", model, path to the vault file); for a search-on unit, a row in "Staleness checks due" (written + six months); the hub's audit counter plus one.
- If the counter reaches four, the reply's first line says: "Audit due before the next unit (audit-units)."
- Brand + AI: after Audit 1 (28 Oct 2026) every unit gets a fresh check before filing (`audit-units`, "Fresh check of one Brand + AI unit"). A unit is not filed unless the fresh-check line ends its unsure list, `audits/brand-ai/fresh-check-<code>.md` exists as `audits/README.md` sets out, and that file's `verdict` matches the line (verdict and counts). The path goes on the unit's `courses-index.md` row.
- Commit and push `apcanario/learning` with the message `<course> <code>: filed`.
- Re-upload the changed Project knowledge files (`courses-index.md`, `hub.py`, the unit).
- Reply with what was filed where, the Academy version, and the counter. Nothing else.
