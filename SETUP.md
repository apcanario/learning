# Setup

**28 October 2026:** the repository is https://github.com/apcanario/learning. Every session clones it and ends with a commit and push; nothing travels as a zip. `kit/` is Academy's builder with the history courses, `courses/` the vault (since A5 the source of the markdown courses' units; since S-DEC2 also their data, each course's pack), `docs/` the method layer, `skills/` the four account skills.

Exact steps to stand up the Learning Project and run it.

## 1. Create the Project
1. Go to claude.ai/projects and click **+ New Project**. Name it **Learning**.
2. Open it, click **Set project instructions**, paste everything in `project-instructions.md` below its title line, and click **Save instructions**.

## 2. Project knowledge
The Project copies are mirrors; the repo is canonical. The Project holds a named set and nothing else (`docs/method.md` §8 step 4; P30-F1, 17 Nov 2026): `reader.md`, `method.md`, `sourcing-standard.md`, `courses-index.md`, `claude/BACKLOG-chats.md`, `claude/CHANGELOG-chats.md`, and, only while a course is being written, that course's three data mirrors (`claude/<course>-hub.py`, `claude/<course>-units_data.py`, `claude/<course>-syllabus-flags.md`). Everything else (the kit's briefs and rubrics, the theme, the skills, the research files, the finished courses' data) is read from the clone.

Replace a knowledge file whenever its source changes: `claude/BACKLOG-chats.md` and `claude/CHANGELOG-chats.md` at the end of every chat; `courses-index.md`, `method.md` and the course's data mirrors when they change. From a chat, the Projects tool's `project_write` with the repo path does it.

## 3. Install the four skills
Skills belong to your account, not the Project. For each folder in `skills/` (`write-unit`, `audit-units`, `file-unit`, `new-course`):
1. Zip the folder itself, so the zip's root is the folder (`write-unit.zip` → `write-unit/SKILL.md`).
2. In claude.ai: **Customize → Skills → + → Create skill → Upload a skill**, and upload the zip.
3. Check it appears in the list and is on.

## 4. The vault
In the vault repository, create `courses/brand-ai/`, `courses/rome/` and `courses/greece/`. Units are filed there as `<code>-<slug>.md` (`method.md` §7). For Brand + AI the vault is the source: Academy reads the units from `courses/brand-ai/` (A5), and there is no other copy. The 137 history reports already written stay in the kit; nothing is moved.

## 5. One site (done 28 October 2026)
Every course is read in Academy, https://claude.ai/artifact/WwmQpUSqAUJvrcmLczppEH and https://apcanario.github.io/academy/, built by `kit/build.py` on `design/theme.css`. The Brand + AI hub and the Audience Growth artifacts were absorbed at A3 (`docs/academy.md`) and deleted.

## 6. Writing a unit
One new chat per unit, model **Opus 5.5** (the build order names any exception).
- **Brand + AI:** paste the unit's brief from the course's Briefs page in Academy (course home → How it is built → Briefs; the Copy brief button). Turn web search on if the unit's search flag is on (the Search column of `courses-index.md`). Attach nothing else. The `write-unit` skill runs.
- **Personal Mythology:** clone `apcanario/learning` and work in `kit/` (the reports named in the module's lane note and the quality-bar reports `greece/r-4.2.html`, `r-6.3.html`, `r-8.1.html` are there). Paste the module's prompt from the syllabus and its lane note from `kit/archive/LANES.md`. Search stays off except to verify a doubtful point.

The chat ends by sending the unit file(s). It does not file them.

## 7. Filing a unit
A new chat, any writing model. Attach the unit file(s); the chat clones `apcanario/learning`. The `file-unit` skill saves to the vault (for Brand + AI that file is what Academy renders), updates the course's data file and `courses-index.md`, rebuilds Academy, checks it (`verify.py`, which also checks `courses-index.md` with `kit/index_check.py`) and publishes it (the artifact, then `kit/deploy.sh` to GitHub Pages), and commits and pushes. Re-upload the changed knowledge files (step 2).

## 8. Staleness checks
No audit runs: the Fable stage closed on 15 Nov 2026 (`docs/method.md` §6). Every unit gets its fresh check before filing (§5). When a staleness date in `courses-index.md` has come (six months after a search-on unit was written): a new chat on **Opus 5.5** with web search on. The chat clones `apcanario/learning`; the `audit-units` skill uses the staleness prompt in `method.md` §6 verbatim and records the result.

## 9. After a theme change
A change to `design/theme.css` reaches a page only when the page is rebuilt and republished.
1. In a new chat, clone `apcanario/learning` and describe the change. Edit `design/theme.css` only (a token first, a component in section 5 if one is new).
2. `cp design/theme.css kit/shell.css`, then `cd kit && python3 build.py && python3 verify.py`. Nothing may fail at any width, in dark or light.
3. Publish Academy: read https://claude.ai/artifact/WwmQpUSqAUJvrcmLczppEH with the Artifact tool, publish `kit/academy/index.html` once with that `url`, `root` `kit/academy` and the fetched files `python3 publish_files.py` prints as `files`, then `./deploy.sh` so https://apcanario.github.io/academy/ carries the same build.
4. Add the session to `kit/CHANGELOG.md` and the version note to `design/README.md`; re-upload `design/theme.css` and `design/README.md` to the Project knowledge; commit and push.

## 10. A new course
A new chat, clone the repo, and say what the course is. The `new-course` skill drafts the frame and asks you to confirm the pick, then builds the syllabus, the briefs and the course's folder (`kit/<id>/` for a history course, `courses/<slug>/`, a copy of `courses/_template/`, for a markdown one), writes its entry, `courses/<id>/course.toml`, and its section in `courses-index.md`, builds, verifies and publishes Academy. The folders are the whole course; no existing file under `kit/` is edited (a history course adds its folder `kit/<id>/`) (A5; S-DEC1).
