# P-DEC14: every course's drawer in a full run

Model: Opus 5.5 (claude-opus-5-5). Base: HEAD d9fccb0. Nothing committed, nothing pushed.

## Files changed
- `kit/verify.py`
  - Phone pass, drawer loop: a full run's `DRAWERS` was `['home'] + [LEAD, SECOND home ids] + MDSUBS` (the root drawer, the two history courses the navigation visits and the live sub-courses of the first markdown course with a unit filed: home, greece, rome, brand-a, brand-b). It is now `['home'] + [q for c in COURSES for q in sub_pages(c)]`: the root drawer and every drawer context of every course in the edition (a history course's home; each markdown sub-course's page, the same ids `verify_scope.py` maps from `data-ctx`). The scoped branch is unchanged (root drawer plus the drawer of each course with a changed page). The existing `continue` still skips an id not in the edition's shell (P70).
  - The S-DEC4 comment on `verify_sample` (about line 191): "drawer" taken out of the passes it samples; it now says a full run checks every course's drawer (P-DEC14).
- `docs/decoupling.md` §6 "Verify by scope" note: "The full run checks the sample courses' drawers ..." now reads that the full run checks every course's drawer (P-DEC14, 21 Nov 2026; before, only the courses the navigation visits).
- `kit/verify-hashes.json`: rewritten by the full run (ALL CHECKS PASSED); left in the working tree, not judged, not committed.
- `out/DEC-A/p-dec14-full.txt`: full-run output.

Reading recorded: the row says the full run checked the `verify_sample` courses' drawers; in the code it was the courses the navigation visits (LEAD, SECOND, MDSUBS), which in the academy edition were greece, rome, brand-a, brand-b. Either way, ux-ia, personal-brand-pb, building-with-ai-bw, sport-psychology-sp and supply-chain-execution-sce were never checked; now they are.

Drawer contexts in the academy shell (all present, so all checked): home, greece, rome, brand-a, brand-b, ux-ia, personal-brand-pb, building-with-ai-bw, sport-psychology-sp, supply-chain-execution-sce (10, was 5).

## Full run (`cd kit && python3 verify.py --full`, 24 m 34 s)
- First line: `full: --full`
- Last line: `ALL CHECKS PASSED`
- No `drawer@...` finding on any course. No fix to `design/theme.css` or `kit/build.py` needed.

## Output
Unchanged (only `verify.py` and a doc changed; the build is untouched).

`python3 kit/baseline.py --check`:
```
academy: built in 101 s, 457 files
academy: 457 files, 0 differ
greece: 82 files, 0 differ
baseline: clean
```
