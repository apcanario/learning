# S-DEC4 packet 2 · course names leave verify.py; the editions without Greece pass

Agent: fresh Opus 5.5 (claude-opus-5-5), 20 Nov 2026. Nothing committed, pushed or published; deploy.sh not run.

**Verdict: done.** `verify.py --edition marketing-ai` ends ALL CHECKS PASSED in full (no probe wrapper); `--edition greece` ALL CHECKS PASSED; the template-test edition `fieldnotes` runs every check to the end with no crash and 12 failures, all content or build findings, none a course-name assumption (below). Full Academy `verify.py`: ALL CHECKS PASSED, 25 m 10 s. Baseline clean before and after. Lines of `verify.py` naming a course (the packet's grep: course ids, `BRAND`, `ROME`, `#m23`, `m55`, `TAB = '…'`): 65 at HEAD, 0 now (prose in the docstring and comments still describes Academy's courses by name; no code does).

## Checks (last lines)

| When | Command | Result | Time |
|---|---|---|---|
| Before any change | `python3 kit/baseline.py --check` | `academy: 457 files, 0 differ` / `greece: 82 files, 0 differ` / `baseline: clean` | 2 m 41 s |
| After the course.toml keys | `python3 kit/baseline.py --check` | `baseline: clean` (457 / 82, 0 differ) | 2 m 55 s |
| Done-when | `cd kit && python3 verify.py --edition marketing-ai` | `ALL CHECKS PASSED` (final file; also run 3 before the last two edits) | 5 m 33 s |
| Greece edition | `cd kit && python3 verify.py --edition greece` | `ALL CHECKS PASSED` | 5 m 48 s |
| Template test | `cd /tmp/template-test/kit && python3 verify.py --edition fieldnotes` | 12 FAIL, no crash (below) | 2 m 34 s |
| Academy | `cd kit && python3 verify.py` | `ALL CHECKS PASSED` (courses-index matches, private terms in the public courses none, rot check none) | 25 m 10 s |
| End | `python3 kit/baseline.py --check` | `academy: 457 files, 0 differ` / `greece: 82 files, 0 differ` / `baseline: clean` | 2 m 53 s |

Earlier marketing-ai runs, each fixed before the next (all runs by the real `verify.py`, no wrapper): run 1 crashed in the desktop pass (`#home .ml-grid`, History's mythos/logos block, absent without a history course); run 2 failed once: `desktop: theme fonts not loaded from fonts/: ['Gentium Book Plus']` (the workbench brand sets `--serif` to Source Serif 4; the expected faces were typed). Both fixed (below); run 3 passed.

## Files changed

- `kit/verify.py` (+312, −109; most of it the rewritten `check_split` and the new `check_split_md`).
- `courses/greece/course.toml`, `courses/rome/course.toml`, `courses/brand-ai/course.toml`, `courses/ux/course.toml` (+3 each: `private`, `reliefs`, `verify_sample`); `courses/personal-brand/course.toml`, `courses/building-with-ai/course.toml` (+1 each: `reliefs`); `courses/_template/course.toml` (+3 commented lines naming the keys).
- `kit/courses.py` (docstring only, +7: "Keys for the checks").
- Not changed: `catalog.toml` (`log_areas` already held the site-log areas), `kit/private_terms.py` (packet 1 gave it `--edition`, `edition_files`, `text_only`; used as is), `kit/build.py`, every brief, unit and vault file.
- Build output: unchanged (baseline clean; the build ignores the three new keys: no `.py` reads them but `verify.py`).

## 1 · The course names (work item 1)

Data the checks now read (course.toml keys, all existing except the three new ones):

- `HIST`: the edition's history courses. **LEAD** = the first of them holding reports 2.3, 2.4, 2.5, 5.2 and 5.5 (`SPLIT_MODS`, "Greece's structure"; report id = the course's `prefix` + module code, `rid()`); Greece in Academy and the greece edition. **SECOND** = another history course with a report 1.2 (Rome in Academy); it replaces `ROME` everywhere (deep link `rm12-2`, its syllabus, `rs-u3`, `rome-u1`, the unopened home of the failed-fetch test, the Rome navigation steps, `'COURSE 2'` = `COURSE {num}`, `'Rome'` = `short`, `'ROME · UNIT '` = `label`, `rm` = `prefix`, `rome-syllabus` = `syl_id`, the drawer's "Rome: course home").
- **MDNAV / MDSUBS**: the edition's first markdown course with a unit filed (Brand + AI in Academy, Personal Brand in marketing-ai), each live sub-course as build.py's `md_courses` names it: page id `<prefix or id>-<key>`, short name from `tracks`, briefs id (`briefs-<key>` under `legacy_ids`, else `<page>-briefs`) and brief anchor prefix. Replaces the `BRAND` tuple `(('brand-a', 'Personal brand', 'A'), ('brand-b', 'Building with AI', 'B'))` and `f'briefs-{key}'`.
- **SAMPLE**: the homes of the courses with `verify_sample = true` (greece, rome, brand-ai, ux: `greece, rome, brand-a, brand-b, ux-ia`, the old literal list), or, where the edition holds none of them, every course it holds. Read by `TOPO_PAGES`, the P92 desktop tiles (first history, first and last markdown: `greece`, `brand-a`, `ux-ia` as before), the motion pass's performance loop and the `--shots` motion sheets.
- **REL_COURSES** = the pages of every course of the repo (not only the edition's: the library serves all) with `reliefs = true`, in course order: the same 7 ids in the same order. The report-to-course attribution (`'greece' if pid.startswith('m') else 'rome' if …`) reads each history course's `prefix` (`^<prefix>\d`).
- **PRIVATE** = the edition's courses with `private = true` (item 3).

Each listed assumption:

| Assumption | Now |
|---|---|
| `check_split` (`#m23`, `greece/r-2.3.html`) | LEAD's reports and files (`<home_id>/r-2.3.html`); without LEAD it prints "split: no history course with reports 2.3, 2.4, 2.5, 5.2, 5.5 in this edition; the history split checks (report pager, syllabus, course-home continue) are left out and the stub checks run on a markdown course" and runs **`check_split_md`** (new): the first markdown course with two reading pages: course home and first reading page empty stubs until opened, each fetched once and kept, the next page prefetched, the pager's next link opening it, a link into an unopened briefs page landing on its first brief, a failed fetch (third reading page, or another fetched page of the course) showing the retry state and the retry loading it, a second course home's failed fetch and retry where the edition has one. |
| brief anchors `b-a2`, `b-b3` in `check_split` | each MDSUBS sub-course's brief of its second unit: in Academy `b-a2` and **`b-b2`** (was `b-b3`): the one place the Academy run opens a different anchor of the same kind (both are in `briefs-b`'s data-anchors). |
| phone navigation clicking `#greece` | LEAD's steps run when LEAD exists, else "nav: no history course with reports … left out (the markdown course steps below run)". Step labels now carry the page id (`greece report`, was `greek report`; output text only). |
| drawer contexts `['home', 'greece', 'rome', 'brand-a', 'brand-b']` | `home` + LEAD and SECOND homes + MDSUBS pages (same list in Academy). |
| How it was built, `('greece', 'rome')` | every history course's home id. |
| Greece drawer accordion (units "1", "2") | the edition's first history course, unit keys from its `unit_key` (greece `{unit}`, default `{id}:{unit}`); without one: "nav: no history course in this edition; the course drawer accordion … is not tried" (a markdown drawer has no unit groups to fold). |
| `root drawer groups: Marketing open` (open tracks from `BRAND`) | the tracks of the courses the run visited: LEAD's and SECOND's `theme` + MDSUBS' tracks. Academy: history, marketing, technology (as before); marketing-ai: marketing (PB) open, technology closed. The fold test uses the first open track (History in Academy; message `the {name} group`). |
| `rp` fallback `'m55'`, `TAB` | SECOND's 4th report / SECOND's syllabus / LEAD's report 5.5 / the first markdown reading page visited (`md_read`); `TAB` = SECOND's home, LEAD's, or the first markdown sub-course's home, whose unit grid is `.cgrid` (a markdown home has no `.part`). |
| desktop `#m23` | `DESK` = LEAD's report 2.3, else the first markdown reading page (`read-pb1` in marketing-ai: measure 744 px = 68ch, sidebar highlights it). |
| desktop `#home .ml-grid` (crashed marketing-ai) | measured when present; checked only where the edition holds a history course; else "desktop: no history course in this edition; the home's mythos/logos block (History's) is not measured". |
| desktop fonts `['DM Sans', 'Space Mono', 'Gentium Book Plus']` (failed marketing-ai) | `THEME_FONTS`: the vendored faces of `kit/fonts/fonts.css` that the theme's `--sans`, `--mono`, `--serif` name as the brand's `[tokens]` leave or set them (Academy: the same three). A face the brand names that is not vendored is printed ("desktop: the brand names ['Source Serif 4'], not in fonts/ …; its fallback is drawn and measured, and its loading is not checked"). Brand, not course, but it blocked the done-when. |
| motion performance loop `('home', 'greece', 'new')` | `home`, the first SAMPLE home the edition holds, `new`; a page the edition lacks is a FAIL ("nothing measured on it"), and an edition with no course home fails ("holds no course home to measure"). Never silent. marketing-ai measured `personal-brand-pb`. |
| `--shots` motion sheets `('home', 'greece', 'ux-ia')` | `home`, the first sampled history home, the last sampled markdown home (same three in Academy). Not run (no `--shots`). |
| tablet and desktop crash on a markdown edition | gone (marketing-ai and fieldnotes reach the end). |

## 2 · What's new's "10 to 25 levels" (work item 2)

Evidence: `kit/build.py` line 495, `NEW_INTERVAL = 11000`, a fixed number of words a contour level, chosen (its comment) so that Academy's largest day (22 Oct 2026, 221,673 words) stands 20, "inside the 10 to 25 the row sets"; `viz.py` line 3280 gives a rise's levels as `int(words // interval)`. The scale is the build's and is right for every edition (a level means the same words everywhere); the range is a statement about Academy's filings, so it is wrong for an edition with fewer (marketing-ai's largest day, 16 Nov, 79,671 words, stands 7; fieldnotes' 1,170 words stands 0).

Decision: keep the range as written where the edition holds every course (`FULL`, `courses = "all"`: Academy); elsewhere state the rule against the build's scale: the largest day stands `int(words // NEW_INTERVAL)` levels (read from build.py's source with `ast`, never typed in verify.py) and at most 25, with one printed line: "What's new: edition marketing-ai holds 2 of 8 courses; its largest day (2026-11-16, 79,671 words) is checked against the build's scale, 7 levels at 11,000 words a level, at most 25; the 10 to 25 range is Academy's filings' and is left out here". The greece edition (1 of 8 courses) is now held to the scale too (20 levels; it met the range as well). No output changed; the hero contour budget (20 KB) untouched.

Also fixed, same cause (fewer filings): `check_home`'s New since heading read `expect['rows'][5]` and crashed on an edition with fewer than six rows (fieldnotes: 3). It now reads the oldest of the at most six rows, as build.py's `RECENT[-1]` does; identical where there are six or more.

## 3 · Private terms and the site-log areas (work item 3)

- Rule (decided from course data, as asked): the default edition (Academy) runs `private_terms.check()` as before (its public courses' vaults, packs and built pages, and the site log). Another edition is checked over **its own built files** (`private_terms.edition_files(EDITION)`, `text_only`, `scan`) unless it holds a course with `private = true` in its course.toml (greece, rome, brand-ai, ux: the owner's courses, which name him); then it prints "private terms: edition greece holds a private course (greece), which names its owner; its files are not checked (the public courses are, in the default edition)". Results: marketing-ai 36 files, none; fieldnotes 9 files, none; greece left out, said so.
- Why a course key and not `private_terms.PUBLIC`: PUBLIC is the no-argument run's list; a course in neither (a new or template course) would then count as private and its edition go unchecked. With the key, a course is public unless marked, the safe default (fieldnotes' course is checked). `verify.py` fails if a course is both `private` and in `PUBLIC`.
- Limit: `edition_files` + `scan` does not apply `dated_lists` (the SCE employer exception), because `DATED` is filled only by `private_terms.files()`. An edition holding supply-chain-execution would fail on its dated-list employer names. None does today. Proposed in P-DEC10 below.
- `SL_AREAS` reads `courses.LOG_AREAS` (catalog.toml `log_areas`) plus the brand's `log_area`: `['Mythology', 'Marketing', 'AI', 'UX', 'Sports', 'Supply Chain', 'Academy']`, equal to the typed list.

## 4 · Outline lists (work item 4)

`REL_COURSES` is data (course.toml `reliefs`), item 1. The other lists are left, as the packet says; paste-ready row:

```
| P-DEC9 | *Proposed (S-DEC4).* The relief tools still type courses: `kit/p95_library.py` `TEXTS` (each relief course's text files, by page id, with brand-ai's split by unit letter and its notes file), `kit/p96_uses.py` `NAMES` and `kit/p95_sheet.py` `TONE`/`NAME` (display names and a tone index per page id). Derive them from the courses with `reliefs = true` in course.toml (as verify.py's REL_COURSES now is: `sub_pages()`), the names from `short`/`tracks`, the files from the vault and the pack's sub-course units; keep TONE as a course.toml key if it is not derivable. A new course's outlines (`new-course` step 5b) then need no kit edit. No build output changes (the p9x tools write design/outlines, not the site): show `design/outlines/` byte-identical after a re-run. | S-DEC4 packet 2, work item 4 | Any chat after S-DEC4 |
```

## 5 · Runs (work item 5)

- **marketing-ai** (done-when): ALL CHECKS PASSED, 5 m 29 s. Highlights: split (markdown, personal-brand-pb) passed; nav left-out lines printed; root drawer groups correct; tablet `read-pb1` 74 paragraphs; desktop `read-pb1`, measure 744 px; What's new at the build's scale (7 levels); performance measured on home, personal-brand-pb, new; private terms 36 files, none; courses-index and rot check clean.
- **greece**: ALL CHECKS PASSED, 5 m 48 s (split on Greece; "no unopened course home"; "no markdown course with a unit filed … left out"; desktop `m23`; What's new 20 levels at the scale; private terms left out, said so).
- **fieldnotes** (template test, recreated in `/tmp/template-test`, a copy of the repo without `kit/academy` and `kit/editions`; S-DEC5's report gives no file contents, so recreated to its description): course `courses/home-composting/` (two units HC1, HC2, written 18 and 19 Nov, three sections each, briefs.md, the template's pages with placeholders filled), track `garden` in `catalog.toml` (with `hero`), `brands/fieldnotes.toml` (own name, mark, storage keys, `--serif` only, two rules lines), `editions/fieldnotes.toml` (`omit = ["changelog", "backlog"]`). `python3 kit/build.py --edition fieldnotes`: 9 files, 2.4 s; every `.py` in the copy equal to the repo's (`cmp`); 0 "academy" (case-insensitive), 0 "apcanario"; `private_terms.py --edition fieldnotes` 9 files, 0. `verify.py --edition fieldnotes`: runs to the end, 2 m 34 s, **12 FAIL**, none from a course name:
  - `split: #home-composting-hc-b-hc1 on a fresh load gave panel home-composting-hc-briefs, element found True, top 248`: the briefs page of a two-unit course is too short to scroll its first brief to the top (the 200 px bound assumes a long page). A check property, not a naming one.
  - 10× `home-composting-hc desktop motion dark|light pose 0…1: the rises ['HC1'|'HC2'] have rings outside the frame or in its fade`: the build's lattice for a course of two short units puts a spot ring outside the wide layout's frame at the poses. A build finding (`kit/build.py` COURSE_TOPO / ct_lattice), out of this packet's files; proposed P-DEC11.
  - `courses-index.md: no "## Home composting" section`: the copy's `docs/courses-index.md` was not given a section for the new course (content the template procedure should add: README "Bring your own course" does not list it; noted for the main chat).
  - Everything else passed, including: split (markdown) with the failed fetch on a two-page course; nav and drawer; tablet; desktop (no ml-grid, Source Serif noted); What's new 0 levels at the scale; the New since heading with 3 rows; private terms 9 files, none.
- **academy** (full, once, at the end, final file): ALL CHECKS PASSED, 25 m 10 s. The navigation log is the old one with page-id labels (`rome home` … `greece report m23 GREECE · UNIT 2 · 2.3` … `brand-b home resumes`); split on Greece with Rome's deep link and failed home fetch; tablet report `rm11`; desktop `m23`, measure 744 px; P92 tiles `greece`, `brand-a`, `ux-ia`, `a.hnew`; performance on home, greece, new; reliefs per course greece 21, rome 18, brand-a 10, brand-b 10, ux-ia 10, personal-brand-pb 12, building-with-ai-bw 11; site log areas as before; private terms in the public courses none. The only intended difference in what it opens: the brief anchor `b-b2` in place of `b-b3` (item 1). No academy verify of HEAD was run for a side-by-side log; the equality of the derived values (LEAD greece, SECOND rome, MDSUBS brand-a/brand-b, SAMPLE, REL_COURSES, SL_AREAS, THEME_FONTS, all printed from the module before the run) is the evidence that the same pages are checked.

## Decisions recorded

1. "Greece's structure" is a property, not a name: reports 2.3–2.5, 5.2, 5.5 present in the edition's shell. Any history course with it can be LEAD; Rome has it too but comes second in course order.
2. Where Greece-only checks cannot run, a markdown equivalent runs where one exists (split → `check_split_md`, tablet/desktop → a markdown home and reading page); otherwise a printed line says what was left out and why.
3. `verify_sample` keeps Academy's sampled pages exactly (five course homes), rather than sampling all eleven, so the Academy run checks what it checked before at the same cost; an edition holding no sampled course samples all its own, so no edition is left unsampled (marketing-ai's course homes were never topography-checked before: the literal list matched none).
4. `private` is a course key with public as the default (item 3).
5. What's new: range for the full edition, the build's scale elsewhere (item 2).
6. The desktop font list follows the brand (a brand change, needed for the done-when).

## Proposed rows (paste-ready, besides P-DEC9 above)

```
| P-DEC10 | *Proposed (S-DEC4).* `verify.py --edition` checks a public edition's built files with `private_terms.scan`, but `DATED` (the courses with `dated_lists`, whose employer names are allowed inside a dated list) is filled only by `private_terms.files()`. Give `edition_files(name)` the same `DATED` registration for the pages of a `dated_lists` course (its `<home>-*/` folder in the edition), so an edition holding supply-chain-execution is checked as academy checks it. No output change. | S-DEC4 packet 2, item 3 | Any chat after S-DEC4 |
| P-DEC11 | *Proposed (S-DEC4).* A course of two short units (the template test's home-composting, 1,170 words a unit) fails verify's motion pass on the desktop: at the five poses one rise's spot ring falls outside the wide layout's frame or in its fade (10 failures, 1280 px, dark and light). Fix in `kit/build.py` (`COURSE_TOPO` wide box/view, or `ct_lattice` for n ≤ 2) so a small course's rises stay inside; and decide whether the split check's 200 px landing bound applies to a page too short to scroll (a two-brief briefs page lands at 248 px). ⚠ Academy output may change (course-home layers): list the expected differences first. | S-DEC4 packet 2, template test | Any chat after S-DEC4 |
```

## Notes for the main chat (docs this makes false, outside this packet's files)

- `README.md` "Bring your own course", "Known limits (S-DEC5)": "`verify.py --edition <name>` stops on any edition without Greece until S-DEC4" is now false. Step list could add a `docs/courses-index.md` section (fieldnotes' one remaining content failure).
- `docs/decoupling.md` §6 S-DEC4 notes and §8 (the two edition-verify results) can record: marketing-ai ALL CHECKS PASSED, greece ALL CHECKS PASSED, fieldnotes runs through with the 12 findings above.
- `skills/new-course` step 5b (outlines): `REL_COURSES` is now course.toml `reliefs = true`; the p9x lists remain (P-DEC9).
- `/tmp/template-test` (the fieldnotes copy) is left in place for packet 3.
