# learning

The one home of the Learning Project (Pedro's self-study courses): the Personal Mythology kit, the design theme, the method docs, the Brand + AI generator and the course vault. Decided 28 October 2026 (`docs/pm-status-2026-10-28.md`, D4): the kit no longer travels as a zip; a chat clones this repo and ends with a commit.

## Layout

| Path | What |
|---|---|
| `kit/` | Academy: the site builder (`build.py`, with `mdcourse.py` for markdown courses), `verify.py`, `deploy.sh`, both history courses' reports, syllabi, audits, bibliographies, the site changelog. `kit/README.md` is its own guide. |
| `design/theme.css` | The one stylesheet for every page in the Project. `design/README.md` says how to change it and propagate the change. |
| `docs/` | The method layer: `method.md`, `courses-index.md`, `BACKLOG.md` (the queue of chats: start here), `CHANGELOG.md` (chats done), `academy.md` (the one-artifact plan), `sourcing-standard.md`, `reader.md`, `project-instructions.md`, the status notes. The claude.ai Project "Learning" holds mirrors of these; this repo is canonical. |
| `generator/` | The data of the markdown courses (no generator since A3): `data/brand-ai/` (the Brand + AI data: `hub.py`, `units_data.py`, `research/`, `briefs/`; the units themselves are in `courses/brand-ai/`, read from there since A5) and `data/_template/` for a new markdown course. `kit/build.py` renders them through `kit/mdcourse.py`. |
| `skills/` | The four account skills (`write-unit`, `audit-units`, `file-unit`, `new-course`); install per `SETUP.md` §3. |
| `SETUP.md` | How the Project, knowledge, skills and vault are set up and kept current. |
| `audits/` | Audit reports that are not kit files (Brand + AI Audit 1). |
| `courses/` | The vault: finished units filed at `courses/<course>/<code>-<slug>.md` (`docs/method.md` §7). The source of the markdown courses' units since A5. |

## Working in a chat

1. Clone (or be given) this repo. Work in it; never from a zip.
2. Kit work: `cd kit`, then `python3 build.py` and confirm it reproduces `academy/` byte for byte (`git status` clean) before changing anything (the rule in `kit/NEXT-SESSION.md`).
3. End the session with a commit that names the session (`CHANGELOG.md` entry, `review_notes`, the next `NEXT-SESSION.md`), and push.

## After a theme change

1. Edit `design/theme.css` (a token in section 1 before a component).
2. Copy it over `kit/shell.css`: `cp design/theme.css kit/shell.css`.
3. `cd kit && python3 build.py && python3 verify.py` (ALL CHECKS PASSED).
4. Publish Academy: the built site to its existing artifact (link in `docs/courses-index.md`), never a new one: the shell `kit/academy/index.html` with the fetched files `python3 publish_files.py` lists as `files` (`kit/README.md`, Site layout and sizes); then `./deploy.sh` for GitHub Pages.

## Where this is going (28 October 2026)

One site, Academy, holds every course (`docs/academy.md`). A3 is done: `kit/build.py` renders the Brand + AI courses from their data file and the standalone hub is gone. A2 split the page into a shell plus fetched files (reports; syllabi, briefs and bibliographies since P20). A4 added a generated "How it was built" page per course. A5 made `courses/` the source of the markdown courses, made a new course of either family a folder plus a `kit/courses.py` entry, and put `docs/courses-index.md` under a script check (`kit/index_check.py`, run by `verify.py`).
