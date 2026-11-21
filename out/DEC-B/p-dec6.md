# P-DEC6 · bibliography path in biblio.py's generated text and BIBLIO-BRIEF.md (21 Nov 2026, Opus 5.5 implementer)

Verdict: DONE. Nothing committed or pushed (the main chat commits). Only P-DEC6 touched.

## Steps
1. `python3 kit/baseline.py --check` before the change: academy 457 files 0 differ, greece 82 files 0 differ, `baseline: clean`. The non-site outputs of the manifest (every academy-edition path outside `academy/`) were copied to `/tmp/pdec6-old/` as the "old bytes".
2. Changes:
   - `kit/biblio.py`: docstring line 4 names `kit/bibliography/README.md`; the docstring's last sentence (formerly "still says `bibliography/<course>/...` ... so the files stay byte-identical") now says the text names `courses/<course>/bibliography/...` since P-DEC6, and what it said before; unit-file intro (line 83) and "Curated bibliography:" line (89) now `courses/<id>/bibliography/r-...md`; the README text's "(`<course>/unit-<n>.md`)" now "(`courses/<course>/bibliography/unit-<n>.md`)"; the console print of `python3 biblio.py` no longer claims the unit files went to `bibliography/`.
   - `kit/bibliography/BIBLIO-BRIEF.md`: line 5 (KIT definition) adds that `courses/<course>/bibliography/` is from the repo root; line 12 input and line 15 output now `courses/<course>/bibliography/unit-<n>.md` and `.../r-<id>.md`. Line 11 (`KIT/<course>/r-<id>.html`, the reports, now Markdown in `courses/<course>/`) is also stale but is not the bibliography path; left, reported below.
3. `--check` after the change: academy 29 changed, 0 added, 0 removed; greece 0 differ. The expected differences (29):
- `kit/../courses/greece/bibliography/unit-0.md`
- `kit/../courses/greece/bibliography/unit-1.md`
- `kit/../courses/greece/bibliography/unit-10.md`
- `kit/../courses/greece/bibliography/unit-11.md`
- `kit/../courses/greece/bibliography/unit-12.md`
- `kit/../courses/greece/bibliography/unit-2.md`
- `kit/../courses/greece/bibliography/unit-3.md`
- `kit/../courses/greece/bibliography/unit-4.md`
- `kit/../courses/greece/bibliography/unit-5.md`
- `kit/../courses/greece/bibliography/unit-6.md`
- `kit/../courses/greece/bibliography/unit-7.md`
- `kit/../courses/greece/bibliography/unit-8.md`
- `kit/../courses/greece/bibliography/unit-9.md`
- `kit/../courses/rome/bibliography/unit-0.md`
- `kit/../courses/rome/bibliography/unit-1.md`
- `kit/../courses/rome/bibliography/unit-10.md`
- `kit/../courses/rome/bibliography/unit-11.md`
- `kit/../courses/rome/bibliography/unit-12.md`
- `kit/../courses/rome/bibliography/unit-13.md`
- `kit/../courses/rome/bibliography/unit-2.md`
- `kit/../courses/rome/bibliography/unit-3.md`
- `kit/../courses/rome/bibliography/unit-4.md`
- `kit/../courses/rome/bibliography/unit-5.md`
- `kit/../courses/rome/bibliography/unit-6.md`
- `kit/../courses/rome/bibliography/unit-7.md`
- `kit/../courses/rome/bibliography/unit-8.md`
- `kit/../courses/rome/bibliography/unit-9.md`
- `kit/bibliography/BIBLIO-BRIEF.md`
- `kit/bibliography/README.md`

   That is 13 Greece unit files (unit-0 to unit-12), 14 Rome unit files (unit-0 to unit-13), `kit/bibliography/README.md` (generated) and `kit/bibliography/BIBLIO-BRIEF.md` (hand-edited; it is in the manifest because it sits under `kit/bibliography/`). None under `kit/academy/`; no Academy bytes change.
4. Proof by script, `out/DEC-B/p-dec6-proof.py` (`python3 out/DEC-B/p-dec6-proof.py <check output> /tmp/pdec6-old`): for each changed file, the new text with `` `courses/<c>/bibliography/`` mapped back to `` `bibliography/<c>/`` (README: its one sentence; brief: its three edits) must equal the old bytes, and at least one mention must have been rewritten; it also fails if any changed path is under `academy/` or any other edition differs. Result:

    ok   ../courses/greece/bibliography/unit-0.md  (4 path mentions rewritten)
    ok   ../courses/greece/bibliography/unit-1.md  (4 path mentions rewritten)
    ok   ../courses/greece/bibliography/unit-10.md  (13 path mentions rewritten)
    ok   ../courses/greece/bibliography/unit-11.md  (9 path mentions rewritten)
    ok   ../courses/greece/bibliography/unit-12.md  (9 path mentions rewritten)
    ok   ../courses/greece/bibliography/unit-2.md  (7 path mentions rewritten)
    ok   ../courses/greece/bibliography/unit-3.md  (8 path mentions rewritten)
    ok   ../courses/greece/bibliography/unit-4.md  (6 path mentions rewritten)
    ok   ../courses/greece/bibliography/unit-5.md  (7 path mentions rewritten)
    ok   ../courses/greece/bibliography/unit-6.md  (8 path mentions rewritten)
    ok   ../courses/greece/bibliography/unit-7.md  (5 path mentions rewritten)
    ok   ../courses/greece/bibliography/unit-8.md  (6 path mentions rewritten)
    ok   ../courses/greece/bibliography/unit-9.md  (5 path mentions rewritten)
    ok   ../courses/rome/bibliography/unit-0.md  (4 path mentions rewritten)
    ok   ../courses/rome/bibliography/unit-1.md  (7 path mentions rewritten)
    ok   ../courses/rome/bibliography/unit-10.md  (6 path mentions rewritten)
    ok   ../courses/rome/bibliography/unit-11.md  (9 path mentions rewritten)
    ok   ../courses/rome/bibliography/unit-12.md  (9 path mentions rewritten)
    ok   ../courses/rome/bibliography/unit-13.md  (9 path mentions rewritten)
    ok   ../courses/rome/bibliography/unit-2.md  (6 path mentions rewritten)
    ok   ../courses/rome/bibliography/unit-3.md  (6 path mentions rewritten)
    ok   ../courses/rome/bibliography/unit-4.md  (6 path mentions rewritten)
    ok   ../courses/rome/bibliography/unit-5.md  (7 path mentions rewritten)
    ok   ../courses/rome/bibliography/unit-6.md  (5 path mentions rewritten)
    ok   ../courses/rome/bibliography/unit-7.md  (6 path mentions rewritten)
    ok   ../courses/rome/bibliography/unit-8.md  (7 path mentions rewritten)
    ok   ../courses/rome/bibliography/unit-9.md  (6 path mentions rewritten)
    ok   bibliography/BIBLIO-BRIEF.md  (3 path mentions rewritten)
    ok   bibliography/README.md  (1 path mention rewritten)
    29 changed files; academy/ site files among them: 0; other editions differing: 0
    PROOF PASSED

5. Manifest re-recorded with `python3 kit/baseline.py` (no argument; the docstring's re-record mode): `wrote kit/baseline.json: academy 457 files, greece 82 files`; `git diff --stat kit/baseline.json`: 29 insertions, 29 deletions (the 29 hashes above).
6. `python3 kit/baseline.py --check`: academy 457 files 0 differ, greece 82 files 0 differ, `baseline: clean`.

Working tree after: M kit/baseline.json, kit/biblio.py, kit/bibliography/BIBLIO-BRIEF.md, kit/bibliography/README.md, the 27 `courses/{greece,rome}/bibliography/unit-*.md`; new `out/DEC-B/p-dec6-proof.py` (and this file).

## Docs that still name the old place (not edited; outside this row's files)
Present-tense statements, now stale:
- `kit/README.md:87` (the `courses/<course>/bibliography/` row): says `BIBLIO-BRIEF.md` is the brief "whose `KIT/bibliography/<course>/` paths are the old place"; no longer true after this row.
- `kit/README.md:88` (`biblio.py` row): "a rebuild of unchanged reports leaves `bibliography/` untouched"; the unit files are in `courses/<course>/bibliography/` now (vague rather than wrong).
- `kit/bibliography/BIBLIO-BRIEF.md:11` (own file, not the bibliography path): input 1 is `KIT/<course>/r-<id>.html`; the reports are Markdown in `courses/<course>/` since P71-3. Left for a row of its own.
Historical records (dated, describe the past; no change suggested): `kit/README.md:38` (session 3, 27 Oct), `kit/CHANGELOG.md:994, 1267, 1304`, `docs/p71-3.md:31`, `docs/pm-status-2026-10-28.md:58`, `docs/decoupling.md:82, 92` (the S-DEC5 plan). `skills/`: no mention of the old place.
