# learning

The one home of the Learning Project (Pedro's self-study courses): the Personal Mythology kit, the design theme, the method docs and the course vault (with each markdown course's data, its pack). Decided 28 October 2026 (`docs/pm-status-2026-10-28.md`, D4): the kit no longer travels as a zip; a chat clones this repo and ends with a commit.

## Layout

| Path | What |
|---|---|
| `kit/` | Academy: the site builder (`build.py`, with `mdcourse.py` for markdown courses), `verify.py`, `deploy.sh`, both history courses' reports, syllabi, audits, bibliographies, the site changelog. `kit/README.md` is its own guide. |
| `catalog.toml`, `editions/`, `brands/` | The site's registry outside the engine (`docs/decoupling.md`): `catalog.toml` the tracks (each with its place on the home hero), the planned courses and the orders; `editions/<name>.toml` one build each (courses held, pages left out, its brand, artifact, Pages URL and deploy remote; `academy` is the default); `brands/<name>.toml` one brand each (S-DEC3: site name, home copy, "How every course works" lines, repo link base, storage keys, colour and font tokens appended to the theme). |
| `design/theme.css` | The one stylesheet for every page in the Project. `design/README.md` says how to change it and propagate the change. |
| `docs/` | The method layer: `method.md`, `courses-index.md`, `BACKLOG.md` (the queue of chats: start here), `CHANGELOG.md` (chats done), `academy.md` (the one-artifact plan), `sourcing-standard.md`, `reader.md`, `project-instructions.md`, the status notes. The claude.ai Project "Learning" holds mirrors of these; this repo is canonical. |
| `skills/` | The four account skills (`write-unit`, `audit-units`, `file-unit`, `new-course`); install per `SETUP.md` §3. |
| `SETUP.md` | How the Project, knowledge, skills and vault are set up and kept current. |
| `audits/` | Audit reports that are not kit files (Brand + AI Audit 1). |
| `courses/` | The vault: finished units filed at `courses/<course>/<code>-<slug>.md` (`docs/method.md` §7). The source of the markdown courses' units since A5, and of their data since S-DEC2 (20 Nov 2026; no generator since A3, and `generator/` is gone): each course's pack, `course.toml` `[pack]`, `briefs.md`, `pages/`, `notes/`, read by `kit/pack.py` and rendered by `kit/build.py` through `kit/mdcourse.py`; `courses/_template/` is the pack of a new markdown course. |

## Working in a chat

1. Clone (or be given) this repo. Work in it; never from a zip.
2. Kit work: `cd kit`, then `python3 build.py` and confirm it reproduces `academy/` byte for byte (`git status` clean) before changing anything (the kit's standing rule).
3. End the session with a commit that names the session (`CHANGELOG.md` entry, `review_notes`), and push.

## After a theme change

1. Edit `design/theme.css` (a token in section 1 before a component).
2. Copy it over `kit/shell.css`: `cp design/theme.css kit/shell.css`.
3. `cd kit && python3 build.py && python3 verify.py` (ALL CHECKS PASSED).
4. Publish Academy: the built site to its existing artifact (link in `docs/courses-index.md`), never a new one: the shell `kit/academy/index.html` with the fetched files `python3 publish_files.py` lists as `files` (`kit/README.md`, Site layout and sizes); then `./deploy.sh` for GitHub Pages.

## Where this is going (28 October 2026)

One site, Academy, holds every course (`docs/academy.md`). A3 is done: `kit/build.py` renders the Brand + AI courses from their data file and the standalone hub is gone. A2 split the page into a shell plus fetched files (reports; syllabi, briefs and bibliographies since P20). A4 added a generated "How it was built" page per course. A5 made `courses/` the source of the markdown courses, made a new course of either family a folder plus a `kit/courses.py` entry, and put `docs/courses-index.md` under a script check (`kit/index_check.py`, run by `verify.py`).
