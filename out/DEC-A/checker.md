# DEC-A fresh check: P-DEC12, P-DEC10, P-DEC13, P-DEC14

Checker: Opus 5.5 (claude-opus-5-5), fresh agent, 21 Nov 2026. Diff: `git diff e855c10d4 HEAD` (4 commits, 2618dbe..72abb12), out/ excluded. Writers' reports in out/DEC-A/ were not read before this view was formed. They were grepped once afterwards: two of the stale-doc findings below (S2, S4) are ones the writers had noted and left open.

## Evidence

- `python3 kit/baseline.py --check` (main tree, HEAD): academy 457 files, 0 differ; greece 82 files, 0 differ; "baseline: clean", exit 0. `kit/baseline.json` is not in the diff, so the comparison is against the manifest from before the change. Academy and greece are byte-identical.
- `kit/verify-hashes.json`: academy `pages` 0 of 292 changed. Its `global` changed only for files that changed (catalog.toml, build.py, courses.py, private_terms.py, verify.py, plus land.py and next_prompt.py from commits before the base). The greece and marketing-ai entries are new. Nothing else changed.
- `grep -n "'history'\|\"history\"" kit/*.py` finds only family keys: `courses.py:81` `_FAMILY_KEYS` and `howbuilt.py:355-356` `method_section('history')`. Neither is a track id. No `NEXT` import is left anywhere in the repo.
- Probe copy `/tmp/decA-probe` with a mixed edition `mixtest` (ux and greece private; supply-chain-execution with dated_lists; personal-brand) built in the copy. `edition_files('mixtest', skip=['ux','greece'])` returned personal-brand-pb 16, supply-chain-execution-sce 4 and 3 root files. The greece/ and ux-ia/ folders were skipped. DATED held the 4 sce files. `scan` gave 4 hits (see S1).
- `private_terms.folders()` over every course equals the folder list of `kit/academy/` exactly (9 folders).

## Verdict per row

- **P-DEC12: satisfied.** The copy in `pages/track-history.md` is word for word what build.py produced, and baseline clean proves it for academy and for greece (greece shows the copy). The history `next` rows are now the History track's `planned`, with `planned_anchor = "planned-courses"`, `planned_drawer = true` and the note carried over. The ghost-tile phases, the count (`· 8 planned`) and the drawer numbering (`k + n + 1`, equal to the old `k + len(HISTORY) + 1` for History) are unchanged. verify.py's `next` test is now `t.get('planned')` for every track, and HOME_JS checks each track's `extra` and anchor from data. One leftover anchor literal remains (N1). Some docs are stale (S2, S3).
- **P-DEC10: satisfied.** `edition_files` puts a `dated_lists` course's folder files into DATED (probe: 4 sce files). Output is unchanged.
- **P-DEC13: satisfied as the row is worded.** The edition is scanned outside the private courses' folders (history: `<id>/`; markdown: `<prefix or id>-<key>/`). The run prints which folders are skipped. An edition of only private courses takes the old branch (`len(PRIVATE) == len(COURSES)`, both filtered by edition), so greece is unchanged. The folder computation is correct for every current course. Nothing private can leak: the change only narrows what is checked, never what is published. Every public course's folder and every root file is scanned. However, the row's folder rule does not make a mixed edition pass (S1).
- **P-DEC14: satisfied.** On a full run, `DRAWERS` is the root plus `sub_pages(c)` of every course in the edition, and pages absent from the edition are skipped. The scoped line is unchanged.

## Findings

### Blockers
None.

### Should-fix

**S1. A mixed edition fails private terms on a private course's panels that live in the shell** (`kit/private_terms.py:133-138`, `kit/verify.py:2989-2997`).
- What is wrong: only split pages go to a course's folder. A private course's unsplit panels stay in `index.html`. Probe evidence: `mixtest` gives 4 hits of the owner's name at `editions/mixtest/index.html:1063`, inside `ux-ia`'s panels (data-ctx="ux-ia"), the changelog rows of the ux course. So the first real mixed edition will fail verify on the private course's own text. That is not a leak, since it over-checks, but the check as built cannot pass that edition. The home tiles and What's new rows that name a private course are also scanned.
- Fix: before scanning, also drop the shell's `<section … data-ctx="<private folder>">…</section>` panels (cut them with `verify_scope.panels()` or the same balanced-section walk, then scan the remainder as text), and say so in the run output. Alternatively, record this limit in the row's close and in `docs/decoupling.md` as known, for the chat that creates the first mixed edition.

**S2. `kit/README.md` is stale after P-DEC12 and P-DEC14.**
- Line 73: "`NEXT` (`catalog.toml` `next`) holds the eight history courses still to come". Both are gone.
- Line 150: "its row removed from `catalog.toml` `next`". Following this sends a new history course's author to a key that is ignored.
- Line 101: "drawer per context (root, each history course, Brand + AI)". A full run now checks every course's drawer.
- Fix: edit the three passages to name the History track's `planned` and every course's drawer. Then rehash that one entry of `kit/baseline.json`, as S-DEC1 and S-DEC5 did for this file, after checking it is the only change.

**S3. `docs/decoupling.md:124` (§6, S-DEC4 notes) is now false in two places.**
- `private` is described as "an edition holding one is not checked for private terms over its own files".
- "Left: the History track's id and copy (`build.py`, `verify.py`; P-DEC12)".
- Line 125 was updated for P-DEC14; this line was not.
- Fix: annotate in the same style as line 125, for example: "its pages are left out of a mixed edition's check (P-DEC13, 21 Nov 2026; an edition of private courses only is still not checked)" and "Left: … P-DEC12 done 21 Nov 2026: the copy is `pages/track-history.md`, the rows the History track's `planned`".

**S4. Course comments and the loader docstring are made false.**
- `courses/{brand-ai,greece,rome,ux}/course.toml:7`: "an edition holding it is not checked for private terms over its own files". After P-DEC13 that is true only for an edition of private courses only.
- `courses/{brand-ai,greece,rome,ux}/course.toml:9` and `kit/courses.py:41`: `verify_sample` "(drawer, topography, motion, shots)". After P-DEC14 the drawer is not sampled.
- Fix:
  - Line 7: "its pages are left out of an edition's private-terms check (P-DEC13; an edition of private courses only is not checked)".
  - Line 9 and courses.py:41: drop "drawer".
  - Comments are not built output (`course.toml` hashes only into its own course's pages through verify_scope, not the build), so baseline is unaffected. Confirm with a rebuild.
  - `courses/_template/course.toml:21` already omits "drawer" and is fine.

### Nits

**N1. `kit/verify.py:2815, 2817` still type History's anchor `#planned-courses`.** It is not a track id, so the grep test passes, but it is the History track's own value left in code. Fix: build the selector from data, for example `', '.join('#' + t['planned_anchor'] for t in THEMES if t.get('planned_anchor'))`. That keeps today's behaviour (only History's list is opened). Using `details.planned` would also open the sports and supply-chain lists and change what check_topo and check_tiles see.

**N2. `private_terms.folders()` restates the build's folder rule in a third place.** The other two are build.py `md_courses` pid and `split()` `data-ctx`, and verify.py `sub_pages`. `folders()` keys on the course's `tracks` keys, while the build keys on the pack's sub-course keys. They are equal today, but they can drift. Fix: `folders()` could read the `data-ctx` values of the edition's built `index.html` for that course's panels, or reuse `verify.sub_pages` logic from one shared helper.

**N3. `kit/courses.py` silently ignores a leftover top-level `next` in `catalog.toml`.** With S2's stale README text, a top-level `next` that someone adds or edits does nothing and nothing warns. Fix: `_fail` when `'next' in _CATALOG` ("moved to the History track's `planned`, P-DEC12").

**N4. Behaviour change in another check, benign: HOME_JS now checks every track with `planned` for its folded list (`#planned-sports`, `#planned-supply-chain`, …).** Before, only History's was checked. It is stricter, and the full run passed. It should be recorded in the row's close as a widened check.

**N5. `kit/courses.py:38` reads "its pages are left out of an edition's private-terms check, P-DEC13".** It omits that an edition holding only private courses is not checked at all. Add the clause, as verify.py's docstring has it.

## Not in scope of the diff
The four rows are still in `docs/BACKLOG.md` Proposed. Closing them by §8 is the main chat's job. The S-DEC4 reference in `docs/decoupling.md` §6's "Proposed rows" bullet could note which are done.
