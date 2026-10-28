# Academy

Decided 28 October 2026. One artifact holds every course Pedro runs: the ancient-history courses, Brand + AI, and every course to come. Each course is written to the same rules (`method.md`, `sourcing-standard.md`), and each shows its content, how it was built (model, dates, checks, audits, flags) and its sources. Academy is the Personal Mythology site grown to hold other kinds of course; it is not a third system.

## Decisions

| # | Decision | Reason |
|---|---|---|
| AD1 | Academy takes over the Personal Mythology artifact, https://claude.ai/artifact/WwmQpUSqAUJvrcmLczppEH; the title becomes Academy | The link and the reader's stored progress survive; 137 reports, their audits and provenance stay as built |
| AD2 | The builder is the kit's `build.py`, extended; the separate Brand + AI hub and its planned `build_hub.py` (S2) are dropped | `build.py` is already course-generic (courses as data, one drawer per course, eight queued courses); Brand + AI is content on the same theme |
| AD3 | Academy is a shell page plus the reports as separate published files, fetched on demand | A published artifact page is capped at 16 MB; the site is 4.3 MB with two courses and eight more are planned. An artifact may carry up to 511 files and 256 MB, and a page may `fetch` its own files |
| AD4 | Order of chats after S1: A1 → A2 → S4 → S5 → A3 → A4 → A5 → S6 | Shell early so that every new unit lands in one place; Rome writing resumes once Academy holds everything |

## Course families

- **History** (Greece, Rome, the eight to come): HTML fragments per module in `kit/<course>/r-<id>.html`, syllabus with prompts, audit unit, bibliography files, `provenance.json`. Unchanged.
- **Brand + AI** (courses A and B; the pattern for any Markdown course): units as Markdown in `courses/brand-ai/`, briefs and build order from `generator/data/brand-ai/units_data.py`, audits as log rows, bibliography collected from the units' links. Rendered by `build.py` through a Markdown renderer onto the same theme classes.

Every course page shows the same things: the course home (goal, outcomes, progress, unit cards), the reading pages, the syllabus or build order with the briefs, the audits run, the bibliography, and the course's own "How it was built" page (A4).

## Specs (one chat each)

### A1 · Academy shell (replaces S2)
1. `kit/courses.py`: a course family field (`history`, `markdown`); the root home becomes Academy (title, hero, course cards for every course including Brand + AI as "live, in progress"); `NEXT` keeps the eight coming courses.
2. `build.py`: the root panel and drawer read as Academy; course panels unchanged for history; a placeholder course panel for Brand + AI that links to its current artifact until A3 lands.
3. `verify.py` passes; publish to the existing URL with the new title; `kit/README.md` and `docs/courses-index.md` updated (the hub table becomes one row).
Done when: the live page is titled Academy, lists both hubs' courses on its home, and every history report is where it was.

### A2 · Split the monolith
1. `build.py` writes `academy/index.html` (shell: theme, drawer, home, syllabi, changelog) and one file per report under `academy/<course>/r-<id>.html`; the shell loads a report by `fetch` on navigation and caches it in memory; the hash routing, prev/next, continue buttons and stored progress keep working.
2. The publish step passes the report files through the Artifact tool's `files`; a first publish may need several calls (255 files per publish).
3. `verify.py` extended: loads a report through the shell, measures the shell's size and the largest report; a size table per course in `kit/README.md`.
Done when: the shell is under 1 MB, every report loads by `fetch`, `verify.py` prints ALL CHECKS PASSED on the published artifact's structure.

### A3 · Brand + AI migration
1. Data model for a Markdown course in `build.py`: units from `courses/<course>/*.md` (front matter header = provenance), briefs and build order from `units_data.py`, audits from a log file, bibliography from the units' links.
2. Markdown renderer to theme classes (headings, tables in `div.tbl`, blockquotes, code, links with `small.url`); the hub's Learn/Build pages become course pages in the drawer.
3. Port the text of `generator/data/brand-ai/hub.py` (method, briefs, audits, template) into the data files; `hub.py` is retired.
4. Publish; the Brand + AI artifact (https://claude.ai/artifact/XVMtDGuqTLkfuZapXstoMT) and the Audience Growth page are deleted once their content is live in Academy.
Done when: A2, A6, A9 and B1 read in Academy with their briefs, audit log and bibliography, and the old artifacts are gone.

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
