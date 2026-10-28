# learning

The one home of the Learning Project (Pedro's self-study courses): the Personal Mythology kit, the design theme, the method docs, the Brand + AI generator and the course vault. Decided 28 October 2026 (`docs/pm-status-2026-10-28.md`, D4): the kit no longer travels as a zip; a chat clones this repo and ends with a commit.

## Layout

| Path | What |
|---|---|
| `kit/` | The Personal Mythology kit: the site builder (`build.py`), checks, both courses' reports, syllabi, audits, bibliographies, changelog. `kit/README.md` is its own guide. |
| `design/theme.css` | The one stylesheet for every page in the Project. `design/README.md` says how to change it and propagate the change. |
| `docs/` | The method layer: `method.md`, `courses-index.md`, `BACKLOG.md` (the queue of chats: start here), `CHANGELOG.md` (chats done), `sourcing-standard.md`, `reader.md`, `project-instructions.md`, the status notes. The claude.ai Project "Learning" holds mirrors of these; this repo is canonical. |
| `generator/data/brand-ai/` | The Brand + AI hub content (`units_data.py`, `hub.py`, the unit and research files). |
| `courses/` | The vault: finished units filed at `courses/<course>/<code>-<slug>.md` (`docs/method.md` §7). |

## Working in a chat

1. Clone (or be given) this repo. Work in it; never from a zip.
2. Kit work: `cd kit`, then `python3 build.py` and confirm it reproduces `personal-mythology.html` byte for byte before changing anything (the rule in `kit/NEXT-SESSION.md`).
3. End the session with a commit that names the session (`CHANGELOG.md` entry, `review_notes`, the next `NEXT-SESSION.md`), and push.

## After a theme change

1. Edit `design/theme.css` (a token in section 1 before a component).
2. Copy it over `kit/shell.css`: `cp design/theme.css kit/shell.css`.
3. `cd kit && python3 build.py && python3 verify.py` (ALL CHECKS PASSED), and the Brand + AI hub build in `generator/`.
4. Republish each page to its existing artifact (links in `docs/courses-index.md`). Never a new artifact.

## Still missing (28 October 2026)

`generator/build_hub.py` and `generator/check_page.py` were never written or never transferred: `hub.py`'s docstring names a builder that exists nowhere (checked the Project, the "Knowledge transfer" artifact and GitHub). S2 of `docs/pm-status-2026-10-28.md` writes `build_hub.py` from `hub.py` and the published hub (version 6.1) and confirms it reproduces that page. The kit's `shell.css` is still the pre-theme copy until S1 runs.
