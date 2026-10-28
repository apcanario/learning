# Backlog

The ordered queue of chats for the Learning Project. One row is one chat. Take the top row that is not done; paste its prompt into a new chat in the Project on the model named; when the chat ends, move the row to Done with the date and commit. Specs are in `pm-status-2026-10-28.md`; the rule for keeping this file and `CHANGELOG.md` current is `method.md` §8: a finished row moves to the changelog, tasks uncovered are added as *proposed* rows, and the backlog is handed to Pedro at the end of every chat for confirmation of what is next. (`kit/BACKLOG.md` is a different file: the Rome writing prompt with the lane notes, used by S6 and its successors.)

## Queue

Order decided 28 October 2026 (`academy.md` AD4). A-rows are the Academy specs in `academy.md`; S-rows are in `pm-status-2026-10-28.md`.

| # | Spec | Model | Prompt to paste |
|---|---|---|---|
| 1 | S1 · Theme migration and housekeeping | any | **Probably done in a parallel chat on 28 Oct (site version 41, "kit session 11 on the theme"); confirm by attaching the session-11 kit zip and merging it into `kit/`, then do only what remains of:** Clone `apcanario/learning` and run S1 of `docs/pm-status-2026-10-28.md`: copy `design/theme.css` over `kit/shell.css`; in `kit/` run `build.py` and `verify.py` (ALL CHECKS PASSED) and `verify.py --shots`; fix the kit docs (remove the retired syllabus artifact links, replace zip references with the repo, fix the README file table); `CHANGELOG.md` session 11; publish the site to its existing artifact once, never force; commit and push. If the chat has room, also run S3. |
| 2 | A1 · Academy shell | any | Clone `apcanario/learning` and run A1 of `docs/academy.md`: course families in `kit/courses.py`, the root home becomes Academy with every course of both hubs (Brand + AI as a placeholder panel linking to its current artifact), `verify.py`, publish to the existing site URL with the title Academy, update `kit/README.md` and `docs/courses-index.md`. Commit and push. |
| 3 | A2 · Split the monolith | any | Clone `apcanario/learning` and run A2 of `docs/academy.md`: shell page plus one published file per report loaded by `fetch`, hash routing and stored progress intact, publish through the Artifact tool's `files`, `verify.py` extended with the size table. Commit and push. |
| 4 | S4 · Greek 13.2 and 13.5, the six flagged reports | Fable 5.1 | Clone `apcanario/learning`, `cd kit`, and follow `NEXT-SESSION.md` exactly, except: no zip; end with a commit and push. The six reports are 11.1, 11.2, 11.4, 11.5, 11.6, 11.8. |
| 5 | S5 · Bibliography spot-check | Fable 5.1, search on | Clone `apcanario/learning`, `cd kit`. Run S5 of `../docs/pm-status-2026-10-28.md`: one Rome and two Greek units; open every "(not verified)" reference in their `bibliography/<course>/r-<id>.md` by web search; correct or confirm; write `audits/bibliography-spot-check.md` with the hit rate; set the `artefacts` entry in `provenance.json` to "Sonnet 5.5, spot-checked with Fable 5.1 (sampled)" if under about one in ten is wrong, otherwise leave it flagged and say what is wrong. Build, commit, push. |
| 6 | A3 · Brand + AI migration | any | Clone `apcanario/learning` and run A3 of `docs/academy.md`: Markdown course data model and renderer in `build.py`, port `hub.py`'s text into data files, A2/A6/A9/B1 with briefs, audit log and bibliography live in Academy; then delete the Brand + AI and Audience Growth artifacts. Update the Audit 1 row in `docs/courses-index.md`. Commit and push. |
| 7 | A4 · "How it was built" per course | any | Clone `apcanario/learning` and run A4 of `docs/academy.md`: one generated page per course from `provenance.json`, `review_notes`, `audits/` and the Markdown front matter; nothing typed by hand. Publish, commit, push. |
| 8 | A5 · Vault as source and the method | any | Clone `apcanario/learning` and run A5 of `docs/academy.md`: `build.py` reads Markdown courses from `courses/`; `courses-index.md` generated or checked by script; `method.md` §7 and the `new-course` skill updated; Project instructions name Academy. Commit and push. |
| 9 | S3 · Review counter | any | Clone `apcanario/learning`, `cd kit`. Run S3 of `../docs/pm-status-2026-10-28.md`: rewrite `review_due.py` to count content reports registered since the last `review_notes` entry whose provenance does not mention Fable 5.1 (FABLE REVIEW DUE at 4, exit 2; keep the call sites); replace the "three deep dives count as three units" paragraph of `BACKLOG.md` with the five-batch plan; confirm `python3 review_due.py` prints "0 of 4 modules written since the last review". Commit and push. Skip if S1 already did it. |
| 10 | S6 · Rome batch 1 | Opus 5.5 | Clone `apcanario/learning`, `cd kit`, and run `BACKLOG.md` for 11.3, 11.4, 11.5 and 11.6 only (writer, `check.py`, fresh checker, maintainer, `register.py`, bibliography file per report). Build, `verify.py`, publish Academy once. Stop when `review_due.py` reads FABLE REVIEW DUE and say so in the first line. Commit and push. |
| 11 | Fable review of batch 1 | Fable 5.1 | The `method.md` §6 stratified-sample audit on Rome 11.3, 11.4, 11.5, 11.6; a module failing more than one claim in ten gets the kit scorecard audit (`kit/audits/AUDIT-BRIEF.md`). Then batches 2 to 5 as in `docs/courses-index.md`, a review after each. |

Dropped 28 October 2026: S2. `generator/build_hub.py` turned out to exist (it arrived in `learning-project.zip`) and reproduces hub v6.4; A3 absorbs it. Brand + AI's own unit queue runs in parallel on the existing hub until A3: B3 next, then B4, A1, Audit 2 (`docs/handoffs/2026-10-28-brand-ai-handoff.md`, step 2, with `skills/`).

## Proposed (awaiting Pedro's confirmation)

| # | Task | Why | Suggested place |
|---|---|---|---|
| P1 | Delete the "Knowledge transfer" artifact (https://claude.ai/artifact/Tgy4URAP8HTf4tPK7GZwfJ) | Its files are in the repo; its own text says delete after use. Pedro held it on 28 Oct: the Brand + AI pipeline still uses it to move files into Project knowledge (handoff, Automation notes) | After A3, or when knowledge uploads come from the repo |
| P4 | Merge the session-11 Personal Mythology kit (theme applied, version 41) into `kit/` | The repo's `kit/` is session 10; the live site is ahead of it | Next chat that has the zip; then S1 closes |
| P3 | File the three fresh-check reports of A2, A6, A9 (28 Oct 2026, Fable 5.1) into `audits/brand-ai/` | They exist only in their chats; the hub summarises them (A9 2/15/8, A2 3/13/11, A6 1/9/7) | Any chat that can read those chats, or paste them in |

Done rows are in `CHANGELOG.md`.
