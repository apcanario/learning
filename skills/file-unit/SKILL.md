---
name: file-unit
description: File a finished Learning Project unit, then update its hub (reading page, counters, changelog, bibliography), rebuild and republish. Use after a unit is written or when asked to file one.
---

# File a unit

Turns a written unit into a filed one: vault, hub, index. The procedure is `method.md` §7. The design rule holds throughout: pages are rebuilt by the generator from `design/theme.css`; nothing is styled by hand.

## 1. Check the unit
- It is complete: every brief item covered, the deliverable (Brand + AI) or Self-test and Carry forward (history) built in full, a Sources list or bibliography file present.
- It starts with the front matter (code, title, course, model, written, search). Add it if missing; the model is the one that actually wrote the unit.
- If anything is missing, stop and say what; do not file a partial unit.

## 2. Vault
Save to `courses/<course>/<code>-<slug>.md` (`brand-ai`, `greece` or `rome`; slug = the title lower-cased, hyphenated, accents and punctuation dropped). If the vault is connected (GitHub), commit it there with the message `<course> <code>: <title>`; otherwise send the file and say where it goes.

## 3. Personal Mythology: the kit (needs the kit zip attached)
1. Save the fragment without front matter as `<course>/r-<id>.html`; the bibliography as `bibliography/<course>/r-<id>.md`; the writer's unsure list as `reviews/<session folder>/<course>-<id>-writer.md`.
2. `python3 check.py <course>/r-<id>.html` until OK.
3. Fresh check: a new agent or chat that has not seen the unit written, briefed with `reviews/units-9-13/BRIEF.md`; it writes findings and never edits. Verify every finding before applying it, as exact replacements; log a paragraph in the session's `log.md`.
4. `python3 register.py <course> "<model>" <id>`; read the `review_due.py` line it prints.
5. When the syllabus unit is complete: `python3 crosscheck.py <course> <ids>` and check every pointer between its modules.
6. Make sure the kit's `shell.css` is a copy of `design/theme.css`; if not, copy it.
7. `python3 build.py`, then `python3 verify.py` (must print ALL CHECKS PASSED).
8. Publish `personal-mythology.html` to https://claude.ai/artifact/WwmQpUSqAUJvrcmLczppEH: read it with the Artifact tool first, publish once with that `url`, never as a new artifact, never forced.
9. Add the session to `CHANGELOG.md`, update `README.md` "Where things stand", and send the new kit zip.

## 4. Brand + AI: the hub data
In `generator/data/brand-ai/`:
1. Copy the unit to `units/<code>-<slug>.md`.
2. `hub.py`: add a `READINGS` entry (`id='read-<code lower>'`, `md='units/<file>'`, `course`, `title`, `covers=[code]`, `name` for the top bar, an `intro` of one paragraph saying what the unit is, when it was written, with or without search, and its known gaps from the unsure list); map `WRITTEN[code]` to that id; set `STATUS[code] = 'written <d Mon>'`; move `NEXT_UNIT` to the next row of `ORDER` and update `NEXT_AUDIT`; bump `VERSION`; add a `CHANGELOG` row at the top (`'<yyyy-mm-dd hh:mm>', '<version>. <code> <title> written (<model>) and filed; <what changed on the hub>.'`).
3. Do not edit `units_data.py`: briefs are never reworded. The unit's links join the Bibliography page automatically.

## 5. Rebuild, check, republish
1. From `generator/`: `python3 build_hub.py data/brand-ai` (Brand + AI) or `python3 build_history.py <kit>` (history, if not published from the kit).
2. `python3 check_page.py hubs/<page>.html`: no overflow, no target under 44 px, no console error, in dark and light. Fix in `design/theme.css` only, then rebuild every hub.
3. Republish to the hub's existing artifact (links in `courses-index.md`): read it with the Artifact tool first, then publish the built file once with its `url`. Never create a new artifact for an existing hub.

## 6. Index and count
- `courses-index.md`: the unit's row (status "written <date>", model, path to the vault file); for a search-on unit, a row in "Staleness checks due" (written + six months); the hub's audit counter plus one.
- If the counter reaches four, the reply's first line says: "Audit due before the next unit (audit-units)."
- Brand + AI: after Audit 1 (28 Oct 2026) every unit gets a fresh check before filing (`audit-units`, "Fresh check of one Brand + AI unit"); a unit without the fresh-check line at the end of its unsure list is not filed.
- Commit and push the repository (`learning-project` on GitHub; `kit/` for history) with the message `<course> <code>: filed`; before the repository exists, send the new `learning-project.zip` (and kit zip).
- Re-upload the changed Project knowledge files (`courses-index.md`, `hub.py`, the unit).
- Reply with what was filed where, the hub version, and the counter. Nothing else.
