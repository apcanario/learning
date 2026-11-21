# P-DEC12 · the History track's id and copy out of the engine

Agent: Opus 5.5 (claude-opus-5-5), fresh agent, 21 Nov 2026. Nothing committed, nothing pushed, nothing published.

Verdict: **done**. Academy and greece byte-identical (`kit/baseline.py --check`: `baseline: clean`, run twice, after the
code change and again after the doc edits). Manifest not re-recorded.

## Files changed

- `pages/track-history.md` (new; a new root folder `pages/`, as the row's `extra = "pages/…md"` names): the
  "Why history and myth together" block (mythos/logos, Herodotus, Thucydides, Plato, Nestle), raw HTML, extracted
  programmatically from the old f-string in `kit/build.py` (no `{}` in it, so the text is exactly what was emitted).
- `catalog.toml`: the top-level `next` array is gone; its eight rows are now the History track's `planned`. The History
  `[[tracks]]` table gained `extra = "pages/track-history.md"`, `planned_anchor = "planned-courses"`,
  `planned_drawer = true`, `planned_note = "The two civilisations that border the Greek story, …"` (the note that was
  typed in build.py). Header comment documents the optional track keys and their defaults.
- `kit/build.py`: no track id. Removed the `NEXT` import, `if 'planned' in OMIT: NEXT = []`, `soon_cards`, the History
  count line, the `if t['id'] == 'history'` block (copy and its own Planned block), and the drawer's History-only
  `dplan` block. Now generic: `extra` = `'\n' + page text less final newline` when the track names a page; the
  existing per-track planned block (S-SPORTS) serves History too, with `id` from `planned_anchor` (default
  `planned-<id>`); the drawer's folded planned row is shown for any track with `planned_drawer` and planned courses,
  numbered `k + n + 1` (n = the track's courses; was `len(HISTORY)`, equal for academy: Greece and Rome are both in
  History, no markdown course there). `HOME_PH` phase count drops `len(NEXT)` (the rows are now in `PLANNED`; same
  total, same order of `next()` calls).
- `kit/courses.py`: `NEXT` and the `next` read removed (also from `_TAKEN` and the tuple note); the loader stops with
  catalog.toml named if a track's `extra` file does not exist. Docstring updated.
- `kit/verify.py`: `NEXT` import gone; the ghost-tile `plans` list is `t.get('planned', [])` for every track (no id).
  The HOME_JS test `t.id === 'track-history' … #planned-courses` is now data-driven: `opt.tracks` (from THEMES) gives
  each track's `extra` and planned anchor; a track with `extra` must keep a non-planned `details.howto.rules`, a track
  with planned courses (when planned is not omitted) its `details.planned#<anchor>`. This extends the second test to
  Sports and Supply Chain (their blocks exist). JS syntax checked with `node --check`; the new test run with
  Playwright against the built `kit/academy/index.html`: 6 tracks, no fault.
- `docs/courses-index.md` (line 112) and `skills/new-course/SKILL.md` (step for a new history culture, two places):
  `catalog.toml` `next` → the History track's `planned`. `index_check.py`: matches the sources.

## Design choices

- **`next` merged into History's `planned`** (the row: "the `next` test to the History track's `planned`"), rather than
  keeping a top-level `next` keyed to History some other way. Everything History did differently from the S-SPORTS
  tracks became an optional track key with today's generic value as its default, so no other track's output moves:
  `planned_anchor` (History's list keeps `id="planned-courses"`, used by verify.py's P93 pass) and `planned_drawer`
  (only History's planned courses appear in the root drawer; turning it on for Sports/Supply Chain would change output).
- **Track page format:** raw HTML in a `.md` file, the file's text less its final newline, as the markdown courses'
  `pages/*.md` blocks are (pack.py convention). Path from the repo root, as course.toml paths are. Shown in every
  edition holding the track, `omit = planned` or not (as before: greece shows the copy without the Planned list).
- **verify_scope.py not changed:** the track page is not in GLOBAL. It reaches only the home, which every scoped run
  checks (ALWAYS), so a change to it is checked. Adding it to GLOBAL would force a full run on a copy edit.

## Grep results

`grep -n "'history'\|\"history\"" kit/*.py`: no track id left. Every remaining hit is the course **family**
`'history'` (courses.py `_FAMILY_KEYS`, `HISTORY`; verify.py 178, 196, 202, 358, 376, 982, 1814, 1887; verify_scope.py
81; howbuilt.py 355-356, the brand's `[howbuilt]` family section key). `track-history` no longer appears in kit/.

## Baseline

```
academy: built in 129 s, 457 files
greece: built in 36 s, 82 files
academy: 457 files, 0 differ
greece: 82 files, 0 differ
baseline: clean
```

## Open points for the main chat

1. **`#planned-courses` literal left in `kit/verify.py`** (about lines 2813 and 2815, the P93 reduced-motion pass opens
   that list before `check_topo`/`check_tiles` on the home). It is an anchor, not a track id, now set by catalog.toml
   `planned_anchor`. Kept literal so the pass measures exactly what it did; deriving it from data (e.g. opening every
   track's planned list) would change what the pass measures (Sports' and Supply Chain's lists, closed today, would be
   open). Proposed follow-up, not done.
2. **`kit/README.md` is stale** (line 73: "`NEXT` (`catalog.toml` `next`) holds the eight history courses still to
   come"; line 150: "its row removed from `catalog.toml` `next`"). Not edited: it is a hashed build output in
   `kit/baseline.json`, and the brief said not to re-record the manifest. Fix both lines and rehash that one entry
   (as S-DEC1 did), or leave for a later row.
3. **Mirrors and account copies:** `docs/courses-index.md` is mirrored in the Project (`courses-index.md`), and
   `skills/new-course/SKILL.md` has an account copy to re-save.
4. **Full verify not run** (per brief). `kit/*.py` and `catalog.toml` changed, so the main chat's run is a full one.
5. Not touched: `docs/BACKLOG.md` (row close), `docs/CHANGELOG.md`, `docs/decoupling.md` §6 (the S-DEC4 note "Left: the
   History track's id and copy … P-DEC12" is now done).
