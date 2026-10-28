# Academy

Decided 28 October 2026. One artifact holds every course Pedro runs: the ancient-history courses, Brand + AI, and every course to come. Each course is written to the same rules (`method.md`, `sourcing-standard.md`), and each shows its content, how it was built (model, dates, checks, audits, flags) and its sources. Academy is the Personal Mythology site grown to hold other kinds of course; it is not a third system.

## Decisions

| # | Decision | Reason |
|---|---|---|
| AD1 | Academy takes over the Personal Mythology artifact, https://claude.ai/artifact/WwmQpUSqAUJvrcmLczppEH; the title becomes Academy | The link and the reader's stored progress survive; 137 reports, their audits and provenance stay as built |
| AD2 | The builder is the kit's `build.py`, extended; the separate Brand + AI hub (`generator/build_hub.py`, which exists and works) is absorbed at A3 and retired then | `build.py` is already course-generic (courses as data, one drawer per course, eight queued courses); Brand + AI is content on the same theme; `build_hub.py`'s Markdown renderer and hub pages are the starting material for A3 |
| AD3 | Academy is a shell page plus the reports as separate published files, fetched on demand | A published artifact page is capped at 16 MB; the site is 4.3 MB with two courses and eight more are planned. An artifact may carry up to 511 files and 256 MB, and a page may `fetch` its own files |
| AD4 | Order of chats: P4 (kit session 11 in) → A1 → A3 → A2 → A4 → A5, then S4 → S5 → S3 → S6. Brand + AI units keep being written in their own lane meanwhile (B3, B4, A1, Audit 2), filed on the standalone hub until A3 lands and in Academy after | Brand + AI is moving fast (five units on 28 Oct), so its migration comes before the split; the history content work (S4, S5) does not depend on Academy and waits |
| AD5 | `generator/data/brand-ai/hub.py` stays the Brand + AI data file (`COURSES`, `WRITTEN`, `READINGS`, `AUDIT_LOG`, `NEXT_UNIT`, `ORDER`, `STATUS`, the prose blocks); `kit/courses.py` only points at it (`data=`) and nothing moves into `courses.py`. `build_hub.py` is retired at A3; `hub.py` is not | Decided 28 Oct 2026 (P9). One source already read by both sides: `build.py:load_markdown` imports `hub.py`, and the hub builders A3 imports read the same module as `D[...]` (18 fields, about 200 lines, half of it prose). Moving the fields would rewrite every `D[...]` access, fold a 200-line data file into the course list, and change `file-unit` §4 and SETUP §2, which edit and upload `hub.py`; keeping it changes neither. A5 later decides whether a new Markdown course's data file keeps this shape |
| AD6 | The Academy home is a catalogue grouped by track (`courses.py:THEMES`: History, Marketing, Technology; a course names its track), each track a banner over its course cards; the Brand + AI data file yields one Academy course per course (A under Marketing, B under Technology), each with its own panel and drawer context; course and home titles are the course names, never a slogan | Pedro, 28 Oct 2026: a Coursera-style academy that grows with the collection; courses separated by subject, self-evident titles. A3 keeps the per-course split: the migrated hub pages become the Learn pages of `brand-a` and `brand-b` |
| AD7 | Academy is navigable by anyone it is shared with, using only what the site shows: a breadcrumb trail on every course, syllabus, report and changelog page (Academy › track or course › unit › here, every step a link), Start the course where there is no progress and Continue where there is, prev/next within a course, the drawer or sidebar for the contents. The content and its copy stay written for Pedro (`reader.md`): the course cards, goals and intros are not neutralised. Course B is renamed Using AI to Build a Brand | Pedro, 28 Oct 2026 |

## What exists to build from (28 October 2026)

- `kit/build.py` + `kit/shell.js`: the history site. Courses as data (`courses.py`), one drawer context per course, prev/next and continue buttons, syllabus panels with prompts, changelog panel, provenance flags, `verify.py` on an emulated phone. Session 11 put it on `design/theme.css` (version 41).
- `generator/build_hub.py` + `generator/hub.js`: the Brand + AI hub. Learn (course pages, reading pages from Markdown via the `markdown` package) and Build (method, build order, briefs, audits log, bibliography collected from links, hub template, changelog), back navigation. `check_page.py` measures 400 px, both themes, 44 px targets, overflow, console.
- Both inline the same `theme.css`; `hub.js` is modelled on `shell.js`. Academy keeps `build.py` and `shell.js` as the shell and takes `build_hub.py`'s Markdown renderer and Build pages as a second course family.

## Course families

- **History** (Greece, Rome, the eight to come): HTML fragments per module in `kit/<course>/r-<id>.html`, syllabus with prompts, audit unit, bibliography files, `provenance.json`. Unchanged.
- **Brand + AI** (courses A and B; the pattern for any Markdown course): units as Markdown in `courses/brand-ai/`, briefs and build order from `generator/data/brand-ai/units_data.py`, audits as log rows, bibliography collected from the units' links. Rendered by `build.py` through a Markdown renderer onto the same theme classes.

Every course page shows the same things: the course home (goal, outcomes, progress, unit cards), the reading pages, the syllabus or build order with the briefs, the audits run, the bibliography, and the course's own "How it was built" page (A4).

## Specs (one chat each)

In every spec, "publish Academy" means two steps: publish the built page to the Academy artifact (read it first, publish once with its `url`, never force), then run `kit/deploy.sh`, which pushes the same build to GitHub Pages at https://apcanario.github.io/academy/ through the public repo `apcanario/academy`. A publish that skips `deploy.sh` leaves Pages behind the artifact.

### A1 · Academy shell
1. `kit/courses.py`: a course family field (`history`, `markdown`); the root home becomes Academy (title, hero, course cards for every course including Brand + AI as "live, in progress"); `NEXT` keeps the eight coming courses.
2. `build.py`: the root panel and drawer read as Academy; course panels unchanged for history; a placeholder course panel for Brand + AI that links to its current artifact until A3 lands.
3. `verify.py` passes; publish to the existing URL with the new title; `kit/README.md` and `docs/courses-index.md` updated (the hub table becomes one row).
Done when: the live page is titled Academy, lists both hubs' courses on its home, and every history report is where it was. (Reworked the same day under AD6: the home is a catalogue by track and Brand + AI is two Academy courses.)

### A2 · Split the monolith
1. `build.py` writes `academy/index.html` (shell: theme, drawer, home, syllabi, changelog) and one file per report under `academy/<course>/r-<id>.html`; the shell loads a report by `fetch` on navigation and caches it in memory; the hash routing, prev/next, continue buttons and stored progress keep working.
2. The publish step passes the report files through the Artifact tool's `files`; a first publish may need several calls (255 files per publish). Then `deploy.sh` copies the whole built site, shell plus report files, into `apcanario/academy` (P10: the shell fetches the reports by relative path, so Pages needs the same tree the artifact has; the script already copies `kit/academy/` when it exists).
3. `verify.py` extended: loads a report through the shell, measures the shell's size and the largest report; a size table per course in `kit/README.md`.
Done when: the shell is under 1 MB, every report loads by `fetch`, `verify.py` prints ALL CHECKS PASSED on the published artifact's structure.

### A3 · Brand + AI migration (done 28 Oct 2026; the builders are `kit/mdcourse.py`, written from `build_hub.py` rather than imported; the Hub template page was dropped from the site, its requirement blocks stay in `hub.py` for `new-course`; the two artifacts were deleted the same day)
1. `kit/build.py` imports the page builders of `generator/build_hub.py` as the `markdown` family: course page (goal, outcomes, progress, unit cards), reading pages (Markdown via the `markdown` package, theme classes), briefs, build order, audits log, bibliography from links, changelog. Data source (AD5): `generator/data/brand-ai/hub.py` stays the course's data file and is the one source for both `load_markdown` (already imports it as `c['hub']`) and the migrated builders (they receive that same module as their `D`); `courses.py` keeps only its pointer (`data=`), and `file-unit` §4 keeps editing `hub.py` unchanged. `courses/brand-ai/` is the vault copy (A5 makes it the source).
2. The hub's Learn/Build split becomes one course context per course (`brand-a`, `brand-b`, AD6) in the Academy drawer: that course's Learn pages first, the shared Build pages under a "How it is built" group; `hub.js`'s back navigation is folded into `shell.js` or dropped.
3. `verify.py` absorbs `check_page.py`'s checks (44 px targets, both themes, console) so one check covers every page.
4. Publish Academy (artifact, then `deploy.sh`); then delete the Brand + AI artifact (https://claude.ai/artifact/XVMtDGuqTLkfuZapXstoMT) and the Audience Growth page (https://claude.ai/artifact/7bK7Pz5BVsEFfGjm8vtpQw); `build_hub.py`, `hub.js`, `check_page.py` and `build_history.py` are retired.
5. `skills/file-unit` and `skills/new-course` point at Academy's build and publish steps; `SETUP.md` §7 and §9 likewise.
Done when: every written Brand + AI unit reads in Academy with its brief, audit log and bibliography; filing a Brand + AI unit is one procedure (`file-unit`) ending in an Academy publish; the old artifacts are gone.

### A4 · "How it was built" per course
One generated page per course: the method in force, the model that wrote each unit, dates, the checks and audits run with verdicts, flags still open, the sources policy, and links to the audit files. History courses generate it from `provenance.json`, `review_notes` and `audits/`; Markdown courses from front matter and the audit log. The site's Changelog page stays the cross-course record.
Done when: every course has the page and no fact on it is typed by hand.

### A5 · Vault as source and the method
1. `build.py` reads Markdown courses from `courses/` directly; history keeps the kit layout. `courses-index.md` is generated or checked by a script, not maintained by hand.
2. `method.md` §7 (filing) and the `new-course` skill updated: a new course of either family is a folder plus a `courses.py` entry; the Project instructions name Academy.
Done when: `new-course` can start a Markdown course and a history course and both appear on the Academy home after one build.

## Not decided yet
- Whether `kit/` is renamed `academy/` in the repo (cosmetic; decide at A2 when paths change anyway).
- The eight coming courses' order and syllabi (out of scope; `courses.py:NEXT`).
