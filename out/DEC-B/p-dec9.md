# P-DEC9 · relief tools derive their course lists (21 Nov 2026, Opus 5.5 implementer)

Verdict: done. Derived TEXTS / NAMES / TONE / NAME (and p96 `pages()`) equal the old hand-typed values exactly, same key order; the three tools, re-run old code vs new code in probe worktrees, write byte-identical output; main tree `git status --short design/` empty; `baseline: clean`.

## Diff summary (not committed)

- `kit/p95_library.py`: `_reliefs()` builds `RELIEFS` (page id -> course, name, tone, prefix, files, readings) from every course with `reliefs = true` (kit/courses.py, course order), page ids as verify.py `sub_pages()`. `TEXTS`, `NAMES`, `TONE` derived from it.
  - files: history = vault `*.md` (minus briefs.md); markdown sub-course = vault files `<code>-*.md` for the pack sub-course's unit codes, sorted, then the notes/ file of each `[[pack.readings]]` with that `course` key (brand-a's audience-growth file).
  - name: history `short`; markdown `tracks` short name with a trailing " · x" written " (x)" ("Personal brand · public" -> "Personal brand (public)").
  - tone: derivable, so no course.toml key: the course's (history) or `[[pack.courses]]` sub-course's (markdown) `color` mapped by build.py's `_TONE` (read from build.py's source with ast, not duplicated; default 4 as mdcourse.py). Old values matched: red 1, purple 5, teal 3, blue 4.
  - a `tracks` key with no `[[pack.courses]]` stops with the file named.
- `kit/p96_uses.py`: `NAMES = L.NAMES`; `pages()` uses each relief page's history `prefix` (was 'm'/'rm' by course name) and `readings` (was the typed 'read-audience-growth'); `unit_key` tests the prefix, not `c in ('greece','rome')`.
- `kit/p95_sheet.py`: `TONE = p95_library.TONE`, `NAME = p95_library.NAMES`.
- `courses/_template/course.toml`: the `reliefs` comment says the outline tools read the course from it (name, tone, texts).
- `skills/new-course/SKILL.md` step 5b: only `reliefs = true`; no kit list to edit.
- `docs/BACKLOG.md`: G-R-SP and G-R-SCE rows: the §5b parenthesis now says the tools derive the lists (no kit edit).

## Derived vs old (assert, script against a JSON snapshot of the old module values taken before the edit, /tmp/pdec9/old.json)

TEXTS equal, same order 7 · NAMES equal, same order 7 · TONE equal, same order 7 · NAME equal, same order 7 · p96 pages() equal, same order 220.

New-course probe (worktree copy, sport-psychology given `reliefs = true`, no kit edit): page `sport-psychology-sp`, name "Sport psychology (public)", tone 2 (orange), 12 unit files.

## Outlines byte-identity

The icon-set clones worked (game-icons, phosphor at the recorded commits; tabler fetched at the recorded commit 58f60538). Two git worktrees of HEAD 6ffb7aa under /tmp/pdec9: `oldtree` (HEAD code) and `newtree` (HEAD + the three edited tools). Ran in each: `p95_library.py /tmp/pdec9/clones`, `p96_uses.py`, `p95_sheet.py <dir>`.

- `diff -r newtree/design/outlines oldtree/design/outlines`: empty (every SVG, JSON, licence, outlines.json, uses.json, uses-why.md).
- p95_sheet: page() HTML sha256 equal (dark da628e72…, light 1e8fc842…); sheet-dark.png and sheet-light.png byte-identical.
- Main tree: the tools were not left writing; `git status --short design/` empty.

Pre-existing, the same under the old code (not P-DEC9's, not fixed):
1. `p96_uses.py` stops at HEAD: `read-dd-bw2: "…as far as the record goes; a rate per day cannot be computed…" is not in its prose`: DD-BW2's text no longer holds MAP's deciding sentence (the unit was corrected after the last p96 run). The probes ran with that stop bypassed (env PROBE, probe copies only) to get output; uses.json then equals the committed file; uses-why.md differs from the committed file by 5 BW rows' "names" counts (BW10 150->158, BW3 95->97, BW4 28->29, DD-BW2 38->34, DD-BW3 212->227), identically under old and new code.
2. `p95_library.py` re-run vs committed `outlines.json`: 124 lines differ, all from drift: the brand-ai research file's path is still `generator/data/brand-ai/…` in the committed file (S-DEC2 moved it to `courses/brand-ai/notes/`) and building-with-ai counts changed with the corrected BW units. Every SVG and licence equals the committed one.
So `design/outlines/` was never committed from a run after S-DEC2; a later row (with a MAP fix for read-dd-bw2) should re-run the tools and commit the refreshed outlines.json / uses-why.md.

## Baseline

`python3 kit/baseline.py --check`: academy 457 files, 0 differ; greece 82 files, 0 differ; `baseline: clean`.

## Left / open

- `kit/p96_extract.py` `GROUPS = {'H': ['greece','rome'], 'M': ['brand-a','brand-b','ux-ia']}` still types page ids (a P96 one-off extraction tool, not in this row's file list; not needed by new-course 5b).
- `docs/decoupling.md` §6 S-DEC4 note ("the three p9x lists stay typed (P-DEC9)") and `docs/method.md`/`file-unit` were not in the allowed files; the main chat updates decoupling §6 if wanted.
- Choice taken: NAME's " (public)" comes from a formatting rule on the tracks short name (" · x" -> " (x)") rather than a new course.toml key; TONE needs no key.
