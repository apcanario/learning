# Setup

**28 October 2026:** the repository is https://github.com/apcanario/learning. Every session clones it and ends with a commit and push; nothing travels as a zip. `kit/` is Academy's builder with the history courses, `generator/data/` the markdown courses' data, `courses/` the vault, `docs/` the method layer, `skills/` the four account skills.

Exact steps to stand up the Learning Project and run it.

## 1. Create the Project
1. Go to claude.ai/projects and click **+ New Project**. Name it **Learning**.
2. Open it, click **Set project instructions**, paste everything in `project-instructions.md` below its title line, and click **Save instructions**.

## 2. Project knowledge
In the Project, click **+** in the knowledge panel and upload these files from the repo. The Project copies are mirrors; the repo is canonical.

Method layer (`docs/`): `method.md`, `reader.md`, `sourcing-standard.md`, `courses-index.md`, `project-instructions.md`, `pm-status-2026-10-28.md`, `academy.md`, and the backlog and chats changelog as `claude/BACKLOG-chats.md` and `claude/CHANGELOG-chats.md` (`method.md` §8 step 4).

Design: `design/README.md` (uploaded as `design-README.md`), `design/theme.css`.

Brand + AI (`generator/data/brand-ai/`): `units_data.py` (every brief and the shared preamble), `hub.py` (goals, build order, audit log and prompts), `audience-growth-across-platforms.md`, `research/research-*.md` (five files), and each filed unit (`units/<code>-<slug>.md`).

Personal Mythology (`kit/`): `AGENT-SPEC.md`, `WRITER-BRIEF.md`, `BACKLOG.md` (the Rome writing prompt with the lane notes), `roman-syllabus.html` (every Rome prompt; Greece is complete), `reviews/units-9-13/BRIEF.md` (uploaded as `CHECKER-BRIEF.md`), `audits/AUDIT-BRIEF.md`, `audits/AUDIT-BRIEF-GREECE.md`, `audits/greece-13.1-rubric.md`, `audits/rome-14.1-rubric.md`.

Replace a knowledge file whenever its source changes: `courses-index.md`, `hub.py` and the unit after every filing; `claude/BACKLOG-chats.md` and `claude/CHANGELOG-chats.md` at the end of every chat; `method.md`, `theme.css` and `design-README.md` when they change; `kit/BACKLOG.md` after a kit session. From a chat, the Projects tool's `project_write` with the repo path does it.

## 3. Install the four skills
Skills belong to your account, not the Project. For each folder in `skills/` (`write-unit`, `audit-units`, `file-unit`, `new-course`):
1. Zip the folder itself, so the zip's root is the folder (`write-unit.zip` → `write-unit/SKILL.md`).
2. In claude.ai: **Customize → Skills → + → Create skill → Upload a skill**, and upload the zip.
3. Check it appears in the list and is on.

## 4. The vault
In the vault repository, create `courses/brand-ai/`, `courses/rome/` and `courses/greece/`. Units are filed there as `<code>-<slug>.md` (`method.md` §7). The 137 history reports already written stay in the kit; nothing is moved.

## 5. One site (done 28 October 2026)
Every course is read in Academy, https://claude.ai/artifact/WwmQpUSqAUJvrcmLczppEH and https://apcanario.github.io/academy/, built by `kit/build.py` on `design/theme.css`. The Brand + AI hub and the Audience Growth artifacts were absorbed at A3 (`docs/academy.md`) and deleted.

## 6. Writing a unit
One new chat per unit, model **Opus 5.5** (the build order names any exception).
- **Brand + AI:** paste the unit's brief from the course's Briefs page in Academy (course home → How it is built → Briefs; the Copy brief button). Turn web search on if the unit's search flag is on (`courses-index.md`; currently B2, A8, B8, DD-A1, DD-B3). Attach nothing else. The `write-unit` skill runs.
- **Personal Mythology:** attach `personal-mythology-kit.zip` (or, at least, the reports named in the module's lane note and the quality-bar reports `greece/r-4.2.html`, `r-6.3.html`, `r-8.1.html`). Paste the module's prompt from the syllabus and its lane note from `BACKLOG.md`. Search stays off except to verify a doubtful point.

The chat ends by sending the unit file(s). It does not file them.

## 7. Filing a unit
A new chat, any writing model. Attach the unit file(s) and `learning-project.zip` (newest); for a history module also the kit zip. The `file-unit` skill saves to the vault, updates the course's data file, rebuilds Academy, checks and publishes it (the artifact, then `kit/deploy.sh` to GitHub Pages), updates `courses-index.md`, and commits and pushes to the repository (before the repository exists: sends the new `learning-project.zip` and kit zip). Re-upload the changed knowledge files (step 2).

## 8. Audits
When `courses-index.md` shows four units since the last audit in a hub (Brand + AI: the first is due after B1), or a staleness date has come (A2, A6, A9: 27 April 2027): a new chat on **Fable 5.1** with web search on. Attach the units (vault files) and, for history, the kit zip. Say "Run the audit." The `audit-units` skill uses the prompts in `method.md` §6 verbatim and records the result.

## 9. After a theme change
A change to `design/theme.css` reaches a page only when the page is rebuilt and republished.
1. In a new chat, attach `learning-project.zip` and describe the change. Edit `design/theme.css` only (a token first, a component in section 5 if one is new).
2. `cp design/theme.css kit/shell.css`, then `cd kit && python3 build.py && python3 verify.py`. Nothing may fail at any width, in dark or light.
3. Publish Academy: read https://claude.ai/artifact/WwmQpUSqAUJvrcmLczppEH with the Artifact tool, publish `kit/academy/index.html` once with that `url`, `root` `kit/academy` and the report files `python3 publish_files.py` prints as `files`, then `./deploy.sh` so https://apcanario.github.io/academy/ carries the same build.
4. Add the session to `kit/CHANGELOG.md` and the version note to `design/README.md`; re-upload `design/theme.css` and `design/README.md` to the Project knowledge; commit and push.

## 10. A new course
A new chat, clone the repo, and say what the course is. The `new-course` skill drafts the frame and asks you to confirm the pick, then builds the syllabus, the briefs and the course's data folder, adds the course to `kit/courses.py`, builds and publishes Academy, and adds the course to `courses-index.md`.
