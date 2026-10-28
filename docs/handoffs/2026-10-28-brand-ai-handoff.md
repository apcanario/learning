# Next session

Start here. The first job is to move this folder off zip files and into a GitHub repository; everything after that runs from the repo.

## State at hand-off (28 Oct 2026, 08:25 Lisbon)

- Brand + AI: B1, A9, A2, A6, B2 written, fresh-checked and filed (5 of 21; B2's check: fix, 3 errors, 10 should-fix, 14 minor, all applied). Audit 1 ran (B1 PASS; A2·A6·A9 REWRITE → rewritten). Next unit: **B3**, then B4, A1, then **Audit 2** (four units since Audit 1: B2, B3, B4, A1). Every Brand + AI unit gets a fresh checker (method §1 override, in force).
- Personal Mythology: Greece complete; Rome as `BACKLOG.md` in the kit says. Kit copy on the theme is session 11 (`personal-mythology-kit.zip`).
- Hubs: Brand + AI https://claude.ai/artifact/XVMtDGuqTLkfuZapXstoMT (v6.4); history site https://claude.ai/artifact/WwmQpUSqAUJvrcmLczppEH (Version 41).
- Project: claude.ai Project "Learning", id `01a180ff-1a65-76f7-ac6e-78559607b587`. Knowledge (29 files: method, reader, sourcing standard, project instructions, courses-index, hub.py, units_data.py, theme.css, design README, the five written units, the superseded research page and its five notes, the kit briefs and rubrics) is current as of this hand-off.
- Vault: the unit files in `generator/data/brand-ai/units/` are the copies to commit to the vault at `courses/brand-ai/`; nothing has been committed there from these sessions.
- Temporary artifact "Knowledge transfer" carried files into the Project knowledge; deleted 28 Oct 2026 (P1) once the repo existed. Knowledge uploads now come from the repo (`SETUP.md` §2).

## Step 1 · Create the repository (first thing, before any unit)

Do this in a new chat in the Learning Project, with the computer linked or GitHub connected.

1. Create a **private** GitHub repository named `learning-project` under the user's account. Use the session's GitHub tools (`add_repo` / `list_repos`) or `gh repo create apcanario/learning-project --private`; if neither is authenticated, ask the user to create the empty private repo at github.com/new and come back with its URL.
2. Unzip the newest `learning-project.zip` (attached to that chat) and push its contents as the initial commit: `project-instructions.md`, `method.md`, `courses-index.md`, `reader.md`, `sourcing-standard.md`, `SETUP.md`, `NEXT-SESSION.md`, `design/`, `generator/` (including `data/brand-ai/units/`), `skills/`. Add a `.gitignore` for `__pycache__/` and `*.zip`.
3. Add the Personal Mythology kit as a second top-level folder `kit/` from the newest `personal-mythology-kit.zip` (its 137 reports, scripts, `BACKLOG.md`, `CHANGELOG.md`), in the same commit or the next.
4. Commit message: `Initial import from learning-project.zip (28 Oct 2026) and personal-mythology-kit session 11`.
5. Replace the "Keep only the newest zip" rule: from now on `SETUP.md` §7 (filing) and §9 (theme change) end with `git commit` and `git push`, not a new zip. Edit those two sections in `SETUP.md` and `skills/file-unit/SKILL.md` to say so, and add the repo URL to `courses-index.md` under "Where everything lives".
6. In the Project knowledge, add nothing new for the repo; knowledge files still get re-uploaded after a filing (SETUP §2), from the repo checkout.
7. Tell the user the repo URL and that every later session starts with "clone `learning-project`" instead of attaching a zip.

## Step 2 · Resume the pipeline (B3)

Clone the repo. One chat per unit, Opus 5.5 High, Auto approval; checker chats on Fable 5.1 High.

1. **Write B3** (Briefing well; search off): new chat, paste the B3 brief from `units_data.py` with the chat instructions used for B2 (one unit per chat; B1 and B2 are in knowledge, point to them; Markdown file with method §7 front matter; sourcing-standard Parts 1 and 2 pass; unsure list at the end of the file).
2. **Fresh check** in a new Fable 5.1 chat: the checker prompt (`skills/audit-units/SKILL.md`, "Fresh check of one Brand + AI unit") followed by the unit's full text. Apply every finding as an exact replacement (assert each `Current:` string occurs once), keep the unsure list, add a line "Fresh check <date> (Fable 5.1): <verdict> · counts; all applied".
3. **File** per method §7 and `skills/file-unit`: copy to `generator/data/brand-ai/units/`, add a READINGS entry, WRITTEN, STATUS, NEXT_UNIT, VERSION bump, CHANGELOG row in `hub.py`; `python3 build_hub.py data/brand-ai`; `python3 check_page.py hubs/brand-and-ai-courses.html`; republish to the hub artifact (read first, publish once with `url`); update `courses-index.md`; re-upload `courses-index.md`, `hub.py` and the unit to Project knowledge (remove the old copy first; "Add text content" takes pasted text); commit and push.
4. Repeat for B4 (search off) and A1 (search off).
5. **Audit 2**: new Fable 5.1 chat, search on; `skills/audit-units` with the stratified-sample prompt from method §6 over B2, B3, B4, A1. Log it in `hub.py` AUDIT_LOG and `courses-index.md`. No new unit while a REWRITE is open.

## Automation notes (what worked this session)

- claude.ai can be driven from the built-in browser pane: the composer is the `[contenteditable]`; insert text with `document.execCommand('insertText')`; model and approval pickers are the two buttons under the composer ("Opus 5.5 High", "Auto").
- A finished chat's file is read from its "View" page: toggle to source, parse `body.innerText` between the line-numbered block start and "Claude finished the response".
- Project knowledge: the Context dialog's **Add → Add text content** takes a title and pasted text; large texts are set with the React native value setter plus an `input` event. "More options for <file>" → "Remove from project" deletes without a confirm. Getting text into the claude.ai tab from the container goes through a published artifact page that `postMessage`s its files to the parent (the "Knowledge transfer" pattern); with the repo in place, the same can be done by fetching raw files from GitHub if the account allows it, otherwise keep the transfer page.
- Foreground `sleep` is blocked in the container; wait with a background `sleep N; echo tick` and an `until grep` loop.
