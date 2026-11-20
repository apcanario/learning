# S-DEC4 packet 3 · verify by scope (work part 2, done-when 4)

Agent: fresh Opus 5.5 (claude-opus-5-5), 20 Nov 2026. Nothing committed, pushed or published; deploy.sh not run. One session stop at about 2 h 22 m (during the marketing-ai proof); every proof before it survived in its log under /tmp and is recorded below.

**Verdict: done** (marketing-ai proof: section 6). A one-unit filing verifies that unit's page, its course's pages and the home in 4 m 53 s against 24 m 54 s for the full run; a theme change runs everything; a broken unit is caught by the scoped run and nothing is recorded.

## Files changed

- `kit/verify_scope.py` (new, about 170 lines): the page-source hashes, the mode, the record.
- `kit/verify.py`: docstring (usage `--full`, a paragraph on scope); `SCOPE = verify_scope.Scope(...)` after `HIST_HOMES`, its mode printed as the run's first line; the per-page passes take their pages through `SCOPE.only()` / `SCOPE.has()`; the record written at the end only when `fails` is empty; the mode repeated above the last line.
- `kit/verify-hashes.json`: **not created in the main tree** (the main chat's `cd kit && python3 verify.py --full` writes it on ALL CHECKS PASSED). Decision: **committed, no `.gitignore` line**. Every chat clones the repo; a record left out of git would make each chat's first run a full one (25 min), which defeats the row. A record that is stale (an edit made without a run) only puts more pages in scope, never fewer, because it compares content hashes, not times.

## 1 · What a page's sources are (work item 1)

`verify_scope.Scope` hashes, per page (panel id of the edition's shell):

- **What the build made of it**: its section in `index.html` (balanced `<section>` scan, everything inside) plus the file it fetches (`data-src`). Any source the build reads for the page (course.toml, briefs.md, pages/*.md, the vault, a history syllabus or prompts file, docs it renders, kit/provenance.json) that reaches the page changes this; one that does not reach the page does not.
- **The source files the checks hold it against**: a unit or report page: its own unit file in `courses/<id>/` (front matter and body; a history report by `prefix` + module code from front matter `code`) and, for a markdown unit, its `## <code>` entry in `briefs.md`. Every other page of a course (home, briefs, build order, changelog, bibliography, syllabus, How it was built): a digest of every file under `courses/<id>/` (course.toml, briefs.md, pages/, notes/, inputs/, bibliography/, the units), because its tiles and tables count the units. A unit page with no unit file of its own (`read-audience-growth`, from brand-ai's notes) counts as a course page.
- A page of no course (home, What's new, Changelog, Backlog, Figure kinds) has only the first.

Decision: hashing the built page as well as the listed sources makes the scope exact where the packet's list alone is too wide or too narrow: a filing's `[[pack.changelog]]` row in course.toml would otherwise put every unit of the course in scope, and a source missing from the list (a docs file rendered into built.html) would otherwise go unseen.

**Always checked** (every run): the pages `home`, `new`, `changelog`, `backlog`, and the edition-wide checks: `check_files` (stubs, orphans, shell size, README size table), figure keys, opening notes and figure rules (static, under 1 s together, read whole), the split (`check_split`/`check_split_md`, 4 s), the site log pages, the phone navigation block (history and markdown sample courses), the root drawer and the drawer of each course a changed page is in, the tablet and desktop layout probes, the home and What's new at every width dark and light, with and without motion (P91, P92, P93 on the home), LCP on the sampled pages, contrast of the always pages and the drawer, private terms, index_check, rot check.

**Scoped** (only the run's pages): `check_panels` at phone, phone light, tablet, desktop; `check_reading` (and its per-course deep-link sample, taken from the scoped pages); `check_seps`; the browser part of `check_reliefs` (the library and the mapping are checked whole); `check_phone_figures`, `check_matrix_320`, `check_phone_lines`, `check_phone_scatters`; `check_contrast`'s course homes and first reading pages; `check_figures` (the examples page, whose sources are kit files: left out of a scoped run, said so); the P93 topography/tile pages and the motion pages (sampled homes, Changelog, Backlog, Figure kinds, first reading page per course). Rule: a scoped run checks the full run's checks on the intersection with its pages, never a page the full run would not check (exception: the drawer of a changed page's course, which the full run checks only for the navigation's sample courses). `--shots` and the LCP pages take the unscoped lists.

## 2 · Full run triggers and the record (work item 2)

GLOBAL (any change, addition or removal forces the full run): `kit/*.py` (verify_scope.py included), `kit/shell.js`, `kit/shell.css`, `design/theme.css`, `kit/fonts/**`, `catalog.toml`, `editions/<edition>.toml`, `brands/<its brand>.toml`. Also full: `--full`; no record for the edition; `index.html` missing.

First line of every run, as printed:
- `full: --full`
- `full: no passed run recorded for edition academy (verify-hashes.json)`
- `full: design/theme.css, kit/shell.css changed` (up to four names, then "and N more")
- `scoped: 1 unit (read-pb3), 7 course pages (...) + home; 12 of 292 pages checked (home, new, changelog, backlog always), and the edition-wide checks`
- `scoped: no page changed + home; ...` when nothing changed.

The record is written (atomic replace) only when the run ends with no failure: `verify-hashes.json: edition academy recorded, 292 pages`, then `ALL CHECKS PASSED` stays the last line. A failed run prints `verify-hashes.json: not written (a failed run marks no page as checked)`; the next run scopes the same pages again.

## 3 · Per edition (work item 3)

The record is `{edition: {global: {path: sha256}, pages: {pid: sha256}}}`; each `--edition` reads and writes only its own key. Proof copy after the runs below: keys `['academy', 'greece']` side by side. Dry scope computed for the editions in the main tree (no record): greece 82 pages (78 unit, 2 course: `greece`, `syllabus`; 2 site), marketing-ai 42 pages (25 unit, 14 course, 3 site).

## 4 · The proofs (work item 4), copy `/tmp/s-dec4-scope` (cp -r of the main tree, .git removed), nothing from it committed

Profile of the old verify.py first (`/tmp/s-dec4-prof`, a wrapper timing each check): total 1,493 s; separators 525 s, check_panels 188 s (4 widths), check_home 159 s, texts_contrast 110 s, check_reading 101 s, phone figures 88 s, reliefs 88 s, poses 65 s, matrix 40 s. The page-heavy passes are the ones scoped.

| Run | Command | First line | Last lines | Wall |
|---|---|---|---|---|
| (a) first run | `python3 verify.py` | `full: no passed run recorded for edition academy (verify-hashes.json)` | `verify-hashes.json: edition academy recorded, 292 pages` / `ALL CHECKS PASSED` | **1,494 s (24 m 54 s)** |
| (b) dry-run filing, 1st | `python3 verify.py` | `scoped: 1 unit (read-pb3), 7 course pages (...) + home; 12 of 292 pages` | `FAIL courses-index.md: staleness PB3: ... expected written 13 Nov 2026, due 13 May 2027`; record not written | 287 s |
| (b) dry-run filing | `python3 verify.py` | same | `verify-hashes.json: edition academy recorded, 292 pages` / `ALL CHECKS PASSED` | **293 s (4 m 53 s)** |
| (d) `--full` | `python3 verify.py --full` | `full: --full` | recorded / `ALL CHECKS PASSED` | **1,475 s (24 m 35 s)** |
| (c) theme change | `python3 verify.py` | `full: design/theme.css, kit/shell.css changed` | recorded / `ALL CHECKS PASSED` | **1,476 s (24 m 36 s)** |
| (5) broken unit | `python3 verify.py` | `scoped: 1 unit (read-pb5), 7 course pages (...) + home; 12 of 292 pages` | 45 FAIL; `verify-hashes.json: not written`; record byte-identical to before (`cmp`) | 293 s |
| greece first run | `python3 verify.py --edition greece` | `full: no passed run recorded for edition greece` | `edition greece recorded, 82 pages` / `ALL CHECKS PASSED` | 342 s |
| greece syllabus edit | `python3 verify.py --edition greece` | `scoped: 2 course pages (greece, syllabus) + home; 4 of 82 pages checked (home, new always)` | recorded / `ALL CHECKS PASSED` | **143 s** |

Order run: a, b, d, c, 5, greece. (d) ran before (c) because one printed line of verify.py was fixed after (b) (the reliefs line listed every mapped page with 0 B; it now lists the run's pages); the fix forced the next run full anyway, so it became (d), and (c) then shows only the theme as its reason.

**(b) The dry-run filing.** In the copy: `courses/personal-brand/PB3-*.md` front matter `written: 2026-11-12` to `2026-11-13`, rebuilt (`python3 kit/build.py`, 120 s). Output diff: `index.html` (only the `personal-brand-pb-order` panel: "written 12 Nov" to "13 Nov"), `new.html`, `personal-brand-pb/built.html`. The first scoped run failed on `docs/courses-index.md` (index_check, an edition-wide check, caught the staleness row the filer updates): itself evidence the scope hides no edition-wide failure. With PB3's row of courses-index.md updated as a filing's `index_edits` would (13 Nov 2026, due 13 May 2027), the scoped run passed.
Pages it checked: **read-pb3; personal-brand-pb, -build, -order, -briefs, -bibliography, -changelog, -built; home, new, changelog, backlog** (12 of 292). By pass: panels 12 at phone, phone light, tablet, desktop; reading 1 page (8 sections; deep link sample read-pb3); separators 1 page; reliefs 1 of 123 mapped; compare/bars 1 page; matrix, lines, scatters 0 pages; contrast 5 panels and the drawer; drawers home and personal-brand-pb; examples page left out (said so). read-pb3's built file did not change; it is in scope because its unit file did.
Reading of the done-when: "that unit's pages" is the unit's reading page plus its course's pages (the course folder changed, and a real filing changes course.toml's changelog), never another unit's page.

**(c)** `design/theme.css` gained one comment line, copied to `kit/shell.css` (the Design rule), rebuilt: full, ALL CHECKS PASSED.

## 5 · Scope does not hide a failure (work item 5)

In the copy (after (c) passed and was recorded), PB5 edited two ways: its first figure block gained `"colour": "red"` (an undocumented key), and a line `Probe <span style="display:inline-block;width:900px">wide</span> line.` before its second heading (raw inline HTML passes through `render_md`). Rebuilt; scoped run (read-pb5 + its course pages + home): **45 FAIL**, among them `figure keys: courses/personal-brand/PB5-production-craft-with-a-phone.md block 1: figure.colour: not a documented key of compare`; `phone read-pb5: horizontal scroll [916, 390]` (and phone light, tablet, desktop); `separators read-pb5 phone320 dark: the page is 916 px wide on a 320 px screen` (16 such); `reliefs read-pb5 ...` (24). Record not written and byte-identical to its state before (`cmp`), so the next run checks read-pb5 again. No separate self-check mode was added: the test run is the proof, and a mode would be a second path to maintain.

## 6 · History pages and markdown editions (work item 6)

History: the greece edition run above. The edit was to `courses/greece/inputs/greek-syllabus.html` (one word in a paragraph), the history course's HTML input: the build changed only `greece/syllabus.html`; the scoped run checked `greece` (course home: the course folder changed) and `syllabus` (output and course folder) plus home and new, 4 of 82 pages, in 143 s against 342 s. A change to kit HTML or any kit/*.py forces the full run (GLOBAL).

Markdown edition: academy's scoped runs are on markdown courses (personal-brand). marketing-ai: see the addendum below.

## Notes for the main chat

- Run `cd kit && python3 verify.py --full` in the main tree (yours); on ALL CHECKS PASSED it writes `kit/verify-hashes.json` for academy: commit it. From then on the filer's plain `python3 verify.py` is scoped.
- Docs made incomplete (outside this packet's files): `skills/file-unit` and `docs/method.md` §7 should say the filing chat runs `python3 kit/verify.py` (scoped; its first line says the mode) and commits `kit/verify-hashes.json` with the filing; `--full` after any kit, theme, brand, edition or catalog change is automatic. `README.md` could name `--full`.
- The probe copies `/tmp/s-dec4-scope`, `/tmp/s-dec4-prof` and logs `/tmp/s-dec4-*.log` are left in place.

## Addendum after the stop: marketing-ai (work item 6) and the end check

The first marketing-ai run was cut by the session stop (its log ends in a Node EPIPE, no result); rerun from the start. PB5 restored from the main tree first (the broken-unit probe, section 5, sits in a course marketing-ai holds); edition rebuilt.

| Run | Command | First line | Last lines | Wall |
|---|---|---|---|---|
| marketing-ai first run | `python3 verify.py --edition marketing-ai` | `full: no passed run recorded for edition marketing-ai (verify-hashes.json)` | `edition marketing-ai recorded, 42 pages` / `ALL CHECKS PASSED` | 361 s |
| BW3 body edit | `python3 verify.py --edition marketing-ai` | `scoped: 1 unit (read-bw3), 7 course pages (building-with-ai-bw, -build, -order, -briefs, -bibliography, -changelog, -built) + home; 10 of 42 pages checked (home, new always)` | recorded / `ALL CHECKS PASSED` | **182 s** |

The edit: "(Probe.) " before the first paragraph of `courses/building-with-ai/BW3-*.md` (copy only), rebuilt. The record now holds three editions side by side: academy, greece, marketing-ai.

End, main tree: `python3 kit/baseline.py --check` → `academy: 457 files, 0 differ` / `greece: 82 files, 0 differ` / `baseline: clean`. No output change (verify_scope.py and verify.py are not read by the build). `git status`: `M kit/verify.py`, `?? kit/verify_scope.py`, `?? out/s-dec4/03-scope.md` (this report); no `kit/verify-hashes.json` in the main tree yet (the main chat's `--full` run writes it).
