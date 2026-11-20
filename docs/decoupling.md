# Decoupling Academy: content, engine, brand

Plan written 20 Nov 2026 (Fable 5.2) against `apcanario/learning` at commit `4243182`. Written read-only: the plan's chat changed nothing in the repo. Filed as `docs/decoupling.md` by row S-DEC0 on 20 Nov 2026, with Pedro's decisions of that day in §6 and S-DEC0's result in §6 and §8.

## 1 · Goal and done-when

Three things that can each be swapped without touching the other two:

- **Content**: a course is one folder of Markdown plus one plain data file. No Python.
- **Engine**: `kit/` knows no course and no brand by name.
- **Brand**: site name, copy, colours, fonts and deploy target are one file per brand, chosen by an edition.

**Done when (the template test):** in a copy of the repo, a course nobody has seen before (a folder with two `.md` units and a `course.toml`) appears on a site with a different name and palette, built by one command, with no `.py` file edited and no "Academy", "apcanario" or private term anywhere in the output.

Constraints kept: GitHub and GitHub Pages only, Python only, no framework, no database, no accounts, no progress sync. Unit codes are permanent ids.

## 2 · What the repo already does (corrections to the chat)

The chat of 19 Nov said the site had no edition concept. That was wrong. Found in the code:

- **Editions exist (P70, 1 Nov).** `kit/courses.py` `EDITIONS`, `build.py --edition <name>`, `verify.py --edition <name>`, `build.py --epub <edition>`. One edition is live: `greece`, with its own artifact.
- **A marketing + AI edition builds today.** Tested in a scratch copy: one `EDITIONS` entry holding `personal-brand` and `building-with-ai` built in 19 s: 25 units, 27 fetched files, 3.53 MB. Not yet run through `verify.py --edition`; no markdown-course edition ever has been (S-DEC0 has since: §8).
- **Units are already engine-free.** Markdown plus front matter in `courses/<slug>/`; `WRITTEN` is derived from the vault; a filed unit without a `READINGS` entry still gets its page.
- **Figures are already declarative.** ` ```viz ` blocks drawn by `viz.py` at build.

So the folders stay as they are: `courses/` is content, `kit/` is the engine, `design/` is the theme. No `content/` or `engine/` rename (the 28 Oct decision that `kit/` keeps its name stands; a rename would touch every doc and skill for no gain).

## 3 · What still couples them (measured)

| Coupling | Where | Size |
|---|---|---|
| Course registry and tracks are Python inside the engine | `kit/courses.py` (`THEMES`, one dict per course, `EDITIONS`, `NEXT`) | 293 lines |
| Course data is Python outside the course folder | `generator/data/<slug>/hub.py` and `units_data.py`, 7 folders | 2,077 lines |
| Site copy and HTML typed into course data | `hub.py`: `BUILD_BODY`, `BUILD_PICK`, `FRAME`, `BRIEFS_LEDE` differ per course (7 of 7); `BUILD_LEDE`, `LEARN_LEDE` are identical in all 7 | part of the above |
| Hand-kept state | `STATUS`, `NEXT_UNIT`, `VERSION` in each `hub.py`; the filer agent (`kit/thin.py`) writes them | every filing |
| Brand typed into the engine | "Academy" literal: 21× `build.py`, 8× `mdcourse.py`, 9× `verify.py`, 3× `howbuilt.py`, 3× `epub.py`; 9× in a built edition's shell | about 45 places |
| One deploy target | `kit/deploy.sh`: remote `apcanario/academy`, URL, and a `<title>Academy</title>` guard hard-coded | 1 file |
| History courses keep inputs in the engine | `kit/greek-syllabus.html`, `roman-syllabus.html`, `prompts-*.json`, `provenance.json`, `kit/bibliography/` | 2 courses |
| Checks know courses by name | `verify.py`: 67 lines naming a course, 41 check functions, 2,762 lines | highest risk |
| Tooling reads the Python data | `thin.py`, `next_prompt.py`, `index_check.py`, `howbuilt.py`, `private_terms.py` | 5 files |

## 4 · Target structure

```
courses/<slug>/
  course.toml        title, goal, sub-courses, unit order, per-unit title/scope/deliverable, changelog
  briefs.md          the shared preamble and one brief per unit, word for word
  pages/*.md         the course's own long copy (frame, how it is made), Markdown not HTML
  <code>-<slug>.md   the units (unchanged)
catalog.toml         tracks (today's THEMES) and the planned courses (today's NEXT)
editions/<name>.toml courses held, pages omitted, brand, deploy remote, artifact URL
brands/<name>.toml   site name, home copy, rules text, repo link base, storage-key prefix, token overrides, fonts
kit/                 engine only; courses.py becomes a loader that discovers courses/*/course.toml
design/theme.css     unchanged; a brand's tokens are appended as CSS custom properties
```

Decisions inside it:

- **TOML, read with `tomllib`** (standard library; the repo runs Python 3.13). No new dependency. Comments survive, long text is readable.
- **`kit/courses.py` stays as a module name** and returns the same dicts it does now, built from the TOML. `build.py`, `verify.py` and the tooling keep their imports; the change is where the data comes from.
- **`hub.py` is replaced by a loader object with the same attribute names** (`COURSES`, `READINGS`, `ORDER`, `STATUS`, …), so `mdcourse.py` (628 lines) is not rewritten.
- **Derived, no longer typed:** `STATUS` from each unit's `written` front matter, `NEXT_UNIT` from the order minus the vault, `READINGS` for unit pages from front matter (an `intro` key added to front matter where a course has a hand-written one). `VERSION` is dropped in favour of the changelog's top row.
- **Generic copy moves to engine defaults** with a per-course override; course-specific HTML blocks become Markdown in `pages/`.
- **`generator/` disappears** once its data has moved; `_template/` becomes `courses/_template/`.
- **State stays out.** Nothing here stores reader progress; an app would add its own save layer keyed by unit code.

## 5 · The safety test

Every row that only moves data proves itself the way A5 did: **the built site is byte-for-byte identical before and after.** S-DEC0 records a hash manifest of `kit/academy/` and of the `greece` edition; each later row rebuilds and diffs. A row whose diff is empty needs one full `verify.py` pass at its end, not one per step. Rows that change output on purpose (S-DEC3) list the expected differences first and fail on any other.

## 6 · Rows

The six rows run in four chats (Pedro, 20 Nov 2026): chat 1 = S-DEC0 + S-DEC1, chat 2 = S-DEC2, chat 3 = S-DEC3 + S-DEC5, chat 4 = S-DEC4. Each chat: Sonnet 5.5 thin main chat, the work by fresh Opus 5.5 agents, a separate Opus 5.5 agent checking the diff. Each row updates the docs and skills it makes false in the same chat, ends by delivering the next chat's prompt (the chain rule below), and carries corrections forward.

| Row | Work | Done when |
|---|---|---|
| **S-DEC0** · File and baseline | File this plan as `docs/decoupling.md`. Queue S-DEC1 to S-DEC5 in `docs/BACKLOG.md` ahead of every unit row (W-DD-SP3, W-SCE1 onward), each with its prompt. Record the output hash manifest (`kit/baseline.py`). Run `verify.py --edition` on a throwaway markdown edition and log what fails. | Plan and rows pushed; manifest committed; the markdown-edition verify result written into the plan's §8 |
| **S-DEC1** · Registry out of the engine | `THEMES` and `NEXT` to `catalog.toml`; `EDITIONS` to `editions/*.toml`; each course's dict to `courses/<slug>/course.toml`; `kit/courses.py` becomes the loader. | Output byte-identical for `academy` and `greece`; `verify.py` ALL CHECKS PASSED; adding a course is a folder, no edit under `kit/` |
| **S-DEC2** · Course data into the pack | `hub.py` and `units_data.py` of all 7 markdown courses into `course.toml`, `briefs.md`, `pages/`; derive `STATUS`, `NEXT_UNIT`, unit `READINGS`; loader shim for `mdcourse.py`; `thin.py`, `next_prompt.py`, `index_check.py`, `howbuilt.py`, `private_terms.py` read the new files; `generator/` removed; `file-unit`, `new-course`, `method.md` §7 rewritten. Briefs are compared word for word. | Output byte-identical; filing a unit touches no `.py`; a dry-run filing of a dummy unit in a repo copy passes |
| **S-DEC3** · Brand and deploy | `brands/academy.toml` holds every "Academy" string, the home copy, the rules lines (replacing `EDITIONS[...]['rules']`), the repo link base and storage-key prefix; token and font overrides; `deploy.sh <edition>` takes remote, URL and title from the edition. Build a second brand and a `marketing-ai` edition as the proof. | `academy` output byte-identical; the second-brand edition passes `verify.py --edition` and contains no "Academy", no "apcanario", no private term |
| **S-DEC4** · Verify by scope | `verify.py` keeps a hash of each page's sources and checks only pages whose sources changed; a change to `kit/*.py`, `shell.js` or `theme.css` forces the full run; `--full` always available. Course names leave the checks (67 lines) for data read from the packs. | A one-unit filing verifies only that unit's pages plus the home; a theme change still runs everything; both runs timed and recorded |
| **S-DEC5** · History packs and the template test | Greece and Rome inputs (`*-syllabus.html`, `prompts-*.json`, their `provenance.json` entries, `kit/bibliography/<course>/`) into their course folders. Then the done-when test of §1, and a `README` section "Bring your own course". | Output byte-identical for history; the template test passes in a repo copy |

**When units may resume:** after S-DEC4 has closed (Pedro, 20 Nov 2026). No unit row runs until then.

**The chain rule (Pedro, 20 Nov 2026).** Every chat of the refactor ends with the paste-ready prompt for the next chat, carrying any correction found. The last chat (S-DEC4) ends instead with a "pick your adventure": one entry per course in Academy, each with its state (units written of total, the next unit and its backlog row, anything blocking it such as a gate or a task waiting on Pedro), plus the non-unit work waiting (the CSS and styling rows, proposed rows), and the paste-ready prompt for each option's first chat. Built from `courses-index.md` and `docs/BACKLOG.md` as they stand at that moment, not from memory.

**Notes on the rows from S-DEC0 (20 Nov 2026; nothing fixed, §8 last bullet):**

- **S-DEC3.** The `How every course works` line "One unit per chat, built in full." (`kit/build.py`, `RULE_LINES`) names Brand + AI; a markdown edition without Brand + AI shows it unchanged, and `verify.py` does not catch it. Today such an edition needs its own `rules` override, as `greece` has; S-DEC3's rules lines in the brand file must cover it. ⚠ S-DEC3's done-when has the second-brand edition pass `verify.py --edition`, which crashes on any edition without Greece until S-DEC4 (next bullet), and chat 3 runs before chat 4. Proposed: chat 3 records that edition's verify result up to the known crash and the checks it does pass, and chat 4 runs `verify.py --edition` on it in full as part of S-DEC4's done-when. The `marketing-ai` edition will also hit the motion pass's What's new failure (largest day 7 levels, not 10 to 25; S-DEC4's note).
- **S-DEC4.** `verify.py` assumes Greece is in every edition: `check_split` reads `#m23` and `greece/r-2.3.html` by fixed id and crashes; the phone navigation block of `main()` clicks `#home a.course[href="#greece"]` and times out; the tablet pass takes `TAB = 'rome' if ROME else 'greece'`; the desktop pass reads `#m23` by fixed id (about lines 2518 to 2541); `rp` falls back to `'m55'` (line 2472); the phone pass checks the Greece drawer accordion (about lines 2450 to 2456); the motion pass's performance loop measures `'greece'` (line 2626) and passes silently on an edition without it; What's new's "10 to 25 levels" rule (line 834) fails on an edition with fewer filings, and S-DEC4 decides whether the range or the build's level scale is wrong. The tablet and desktop passes crash on a markdown edition (§8). These leave with the course names (the 67 lines).
- **S-DEC5.** `kit/baseline.py` hashes `kit/bibliography/` as an academy output. Moving `kit/bibliography/<course>/` into the course folders changes those paths: the row updates the output roots in `kit/baseline.py` and compares the moved files by content, or lists the moved paths as its expected differences.

**Notes on the rows from S-DEC1 (20 Nov 2026):**

- **Where the registry now lives.** Each course's dict is `courses/<id>/course.toml` (found by folder; `courses/supply-chain-execution/` now exists, holding only its `course.toml`); `THEMES` is `catalog.toml` `[[tracks]]`, `NEXT` is `catalog.toml` `next`, and `catalog.toml` `course_order` and `edition_order` fix the order (a course or edition not named follows, sorted by id); `EDITIONS` is `editions/<name>.toml` at the repo root (not `kit/editions/`, which is the greece build's output). `kit/courses.py` is the loader; it turns, by key name, a course's `parts`, `eras` and `ticks` rows, its `tracks` values, a track's `planned` rows, the `next` rows and an edition's `courses` and `omit` into tuples, and an edition's `courses = "all"` into None. A new tuple-valued key needs its line in `_course` or `_edition` there.
- **S-DEC2.** The pack data goes into the same `course.toml` that already holds the registry keys, and everything in that file reaches the course dict build.py reads. The only top-level `hub.py` name that collides with a registry key is `STATUS`/`status`; `name`, `color` and `tile` are keys of the hub's sub-course dicts and collide only if hoisted to the top level; a pack table named, for example, `courses` or `units` at the top level would also change the registry dict. Put the pack's data under its own table, have the loader shim read it from there and strip it from the registry dict, so `COURSES` stays equal. The loader skips `courses/_*`, so `_template` can move to `courses/_template/`. The data folders hold more than `hub.py` and `units_data.py` (brand-ai `briefs/`, `research/`, `audience-growth-across-platforms.md`; the public courses' `case-facts.md` or `case-academy.md` and `syllabus-flags.md`; `bibliography.md` of sport-psychology and supply-chain-execution; ux `perqo-facts.md`), read by `thin.py` (`case-*.md`), `build.py` (`data_dir`), `p95_library.py` (a hard-coded path) and `rot_check.py` (which lists `generator/data/*/hub.py` and would drop them silently once `generator/` goes); loose `.md` moved into `courses/<slug>/` would meet the vault globs (`private_terms.py`, `build.py`, `index_check.py`, `next_prompt.py`): a subfolder or an explicit exclusion. `kit/README.md` is a build output in `kit/baseline.json` (the size table) and also hand-written prose: a row that edits its prose rehashes that one entry (S-DEC1 did, after a check showing it the only change). Left for S-DEC2: `generator/data/_template/hub.py` still says "add the course to kit/courses.py"; the docstrings of `kit/thin.py`, `kit/next_prompt.py` (and the unit prompt it prints: "`kit/courses.py` entry"), `kit/private_terms.py`, `kit/private-terms.txt` and the prompts templates in `docs/*-prompts.md` still name `kit/courses.py` for a course's fields.
- **S-DEC3.** A new track still needs a kit edit: its place on the home hero, `_HERO_AT` in `kit/build.py` (build.py stops without one). The place belongs with the track in `catalog.toml` or with the brand.
- **S-DEC4.** A new course's outlines (`new-course` step 5b) are still lists in `kit/`: `REL_COURSES` in `kit/verify.py`, `TEXTS` in `kit/p95_library.py`, `NAMES` in `kit/p96_uses.py`, `TONE`/`NAME` in `kit/p95_sheet.py`. The build does not need them (the throwaway course of S-DEC1 built without), but filing reliefs does.
- **S-DEC5.** `kit/howbuilt.py` matches a history course's `provenance.json` artefact key `courses.py:<ID>` (for example `courses.py:ROME`); the key names the old file. Moving the provenance entries can rename it, or keep it as a plain label.

## 7 · Not in this plan

- **A GitHub Action for build and deploy.** It can push Pages but cannot publish the claude.ai artifact, and the Project rule is to publish both every time. Revisit after S-DEC4, when the build is fast and scoped; until then it would create two publishing paths.
- **A neutral JSON export of the course model.** The loader's dicts are that model in memory; writing it to disk waits for a second consumer (an app).
- **Splitting into two repos.** Only if someone else maintains the engine or the content is licensed out.
- **CSS and styling changes.** They follow this plan as their own rows; after S-DEC3 they are edits to `theme.css` and a brand file only.

## 8 · Risks and open points

- **`verify.py`** is the largest file and names courses in 67 lines. S-DEC1 and S-DEC2 leave it reading the same dicts, so it should not move until S-DEC4. If it fails earlier, the loader is wrong, not the check.
- **Briefs must not be reworded** (Project rule). S-DEC2 converts them mechanically and the byte-identical Briefs pages are the proof.
- **The filer and next-prompt tooling** (`thin.py`, `next_prompt.py`) is what every unit chat runs. S-DEC2's dry-run filing is the guard; no unit row runs between S-DEC2's start and its close.
- **Account skills** (`file-unit`, `new-course`) are copies of `skills/` in the repo; after S-DEC2 they must be re-saved to the account or the next unit chat follows the old procedure.
- **The `greece` edition's artifact** must be republished only if its bytes change; under this plan they should not until S-DEC3.
- **Markdown-edition verify result (S-DEC0, 20 Nov 2026, in a repo copy; nothing fixed):** throwaway edition `mdtest` holding `personal-brand` and `building-with-ai` (one `EDITIONS` entry, greece's `omit`, no `rules`): builds in 22 s, 25 units, 29 files, 3.70 MB on disk (3.53 MB by the build's count). `verify.py --edition mdtest` crashes: `check_split` reads `#m23` (Greece) by fixed id, and the phone navigation block clicks `#greece` (the tablet pass likewise). Run past the crashes (a probe copy of `verify.py` with each check and each pass wrapped), the tablet pass crashes (`#greece` missing) and the desktop pass crashes (`#m23` missing); these checks pass with 0 faults: files, figure keys (125 blocks), opening notes, figure rules (91), figures on a phone, matrix at 320 px (21), lines (4), scatters (2), reading (25 units, 249 sections), separators, reliefs, panels at phone width dark and light (29), home, What's new, contrast (lowest 4.29:1), the home at every width (P91), topographies (P93), `index_check`, private terms, rot check. The motion pass (P92) fails 168 times: What's new's largest day stands 7 levels, not 10 to 25 (`verify.py` line 834); its performance loop measures `greece` on an edition without it and passes silently. The `How every course works` line "One unit per chat" names Brand + AI in an edition without it; `verify.py` does not catch it. Notes on S-DEC3, S-DEC4 and S-DEC5: §6.
