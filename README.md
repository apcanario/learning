# learning

The one home of the Learning Project (Pedro's self-study courses): the Personal Mythology kit, the design theme, the method docs and the course vault (with each markdown course's data, its pack). Decided 28 October 2026 (`docs/pm-status-2026-10-28.md`, D4): the kit no longer travels as a zip; a chat clones this repo and ends with a commit.

## Layout

| Path | What |
|---|---|
| `kit/` | Academy: the site builder (`build.py`, with `mdcourse.py` for markdown courses), `verify.py`, `deploy.sh`, the history courses' audits and reviews, the kit's part of `provenance.json`, the site changelog. `kit/README.md` is its own guide. |
| `catalog.toml`, `editions/`, `brands/` | The site's registry outside the engine (`docs/decoupling.md`): `catalog.toml` the tracks (each with its place on the home hero), the planned courses and the orders; `editions/<name>.toml` one build each (courses held, pages left out, its brand, artifact, Pages URL and deploy remote; `academy` is the default); `brands/<name>.toml` one brand each (S-DEC3: site name, home copy, "How every course works" lines, repo link base, storage keys, colour and font tokens appended to the theme). |
| `design/theme.css` | The one stylesheet for every page in the Project. `design/README.md` says how to change it and propagate the change. |
| `docs/` | The method layer: `method.md`, `courses-index.md`, `BACKLOG.md` (the queue of chats: start here), `CHANGELOG.md` (chats done), `academy.md` (the one-artifact plan), `sourcing-standard.md`, `reader.md`, `project-instructions.md`, the status notes. The claude.ai Project "Learning" holds mirrors of these; this repo is canonical. |
| `skills/` | The four account skills (`write-unit`, `audit-units`, `file-unit`, `new-course`); install per `SETUP.md` §3. |
| `SETUP.md` | How the Project, knowledge, skills and vault are set up and kept current. |
| `audits/` | Audit reports that are not kit files (Brand + AI Audit 1). |
| `courses/` | The vault: finished units filed at `courses/<course>/<code>-<slug>.md` (`docs/method.md` §7). The source of the markdown courses' units since A5, and of their data since S-DEC2 (20 Nov 2026; no generator since A3, and `generator/` is gone): each course's pack, `course.toml` `[pack]`, `briefs.md`, `pages/`, `notes/`, read by `kit/pack.py` and rendered by `kit/build.py` through `kit/mdcourse.py`; `courses/_template/` is the pack of a new markdown course. A history course (Greece, Rome) keeps its inputs in its folder too since S-DEC5 (20 Nov 2026), named by its `course.toml`: `inputs/` (the syllabus, `prompts-<course>.json`, its part of the provenance) and `bibliography/` (the curated `r-<id>.md` and `biblio.py`'s `unit-<n>.md`). |

## Working in a chat

1. Clone (or be given) this repo. Work in it; never from a zip.
2. Kit work: `cd kit`, then `python3 build.py` and confirm it reproduces `academy/` byte for byte (`git status` clean) before changing anything (the kit's standing rule).
3. End the session with a commit that names the session (`CHANGELOG.md` entry, `review_notes`), and push.

## After a theme change

1. Edit `design/theme.css` (a token in section 1 before a component).
2. Copy it over `kit/shell.css`: `cp design/theme.css kit/shell.css`.
3. `cd kit && python3 build.py && python3 verify.py` (ALL CHECKS PASSED).
4. Publish Academy: the built site to its existing artifact (link in `docs/courses-index.md`), never a new one: the shell `kit/academy/index.html` with the fetched files `python3 publish_files.py` lists as `files` (`kit/README.md`, Site layout and sizes); then `./deploy.sh` for GitHub Pages.

## Bring your own course

The engine (`kit/`) knows no course and no brand by name (`docs/decoupling.md` §1). A course, a site name and a build are data files; nothing under `kit/` is edited. The template test of S-DEC5 (20 Nov 2026) did exactly this in a copy of the repo: a new course, brand and edition, built by one command with no `.py` file changed.

1. **The course folder.** Copy `courses/_template/` to `courses/<slug>/` and replace every `⟨…⟩`. `course.toml` holds the course's entry (`id` = the folder name, `family = "markdown"`, `short`, `label`, `name`, `color`, `home_id`, `data` and `vault` pointing at the folder, `tracks.<KEY>` and `tiles.<KEY>` per course key) and, under `[pack]`, its data: the courses with their goal, outcomes and units (code, title, scope, deliverable), the writing `order`, the changelog rows. `kit/pack.py`'s docstring is the schema. `briefs.md` holds `## Preamble` and one `## <code>` brief per unit; `pages/*.md` the long copy (frame, build body, order notes, briefs lede) as theme-class HTML; `notes/` anything else (a subfolder, so the unit globs never meet it). `kit/courses.py` finds the folder; `catalog.toml` `course_order` places it (unnamed, it comes after the named courses, by id).
2. **The units.** One Markdown file per unit, `courses/<slug>/<code>-<slug>.md`, with the front matter of `docs/method.md` §7 (`code`, `title`, `course: <slug> · <KEY> · <name>`, `model`, `written: YYYY-MM-DD`, `search: on|off`, and `intro` for its reading page), then `# <code> · <title>`, the text, its deliverable and its Sources. Status, the next unit and the version are derived from these files; nothing is typed.
3. **A track, if none fits.** A `[[tracks]]` table in `catalog.toml`: `id`, `name`, `color`, `lede` and `hero` (its place on the home hero, `[[x, y] tall, [x, y] wide]`). No kit edit.
4. **A brand.** `brands/<name>.toml`: `name`, `mark`, `lede`, `repo` (the link base of "How it was built"), `id_base`, `fonts_href`, `log_area`, `[storage]` (its own localStorage keys), optional `[tokens]` and `[tokens_light]` (the palette, appended to `design/theme.css` as custom properties; leave `--sans` and `--mono` alone, `kit/viz.py` sizes figures from their metrics), `[[rules]]` ("How every course works"), `strip_comments = true` (leave the theme's and `shell.js`'s comments, the maintainer's notes, out of the shell) and optional `[howbuilt]` (the method and sourcing docs the "How it was built" pages quote; without it they quote neither). `brands/academy.toml`'s header describes every key.
5. **An edition.** `editions/<name>.toml`: `title`, `courses` (the ids it holds, or `"all"`), `omit` (`changelog` and `backlog` unless the brand's `log_area` has a section in `docs/site-log.md`; also `build`, `figures`, `planned`), `site` (its folder under `kit/`, e.g. `editions/<name>`), `brand`, and for deploying `url` and `deploy_remote`. `editions/academy.toml`'s header describes every key.
6. **Build.** From the repo root: `python3 kit/build.py --edition <name>`, which writes `kit/<site>/`. `python3 kit/private_terms.py <files>` checks the output against `kit/private-terms.txt`.
7. **Deploy.** `kit/deploy.sh <name> --dry-run` prints the plan; `kit/deploy.sh <name>` pushes the build to the edition's `deploy_remote` (a GitHub Pages repo) and checks the built page carries the edition's `title`.

Known limits (S-DEC5): `verify.py --edition <name>` stops on any edition without Greece until S-DEC4 (`check_split` reads Greece's `#m23`); the Figure kinds page and the "How it was built" page still carry a few sentences about this repo's own history (Rome examples, the closed Fable stage), engine text that names no brand and no private term.

## Where this is going (28 October 2026)

One site, Academy, holds every course (`docs/academy.md`). A3 is done: `kit/build.py` renders the Brand + AI courses from their data file and the standalone hub is gone. A2 split the page into a shell plus fetched files (reports; syllabi, briefs and bibliographies since P20). A4 added a generated "How it was built" page per course. A5 made `courses/` the source of the markdown courses, made a new course of either family a folder plus a `kit/courses.py` entry, and put `docs/courses-index.md` under a script check (`kit/index_check.py`, run by `verify.py`).
