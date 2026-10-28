# Backlog

The ordered queue of chats for the Learning Project. One row is one chat. Take the top row that is not done; paste its prompt into a new chat in the Project on the model named; when the chat ends, move the row to Done with the date and commit. Specs are in `pm-status-2026-10-28.md`; the rule for keeping this file and `CHANGELOG.md` current is `method.md` §8: a finished row moves to the changelog, tasks uncovered are added as *proposed* rows, and the backlog is handed to Pedro at the end of every chat for confirmation of what is next. (`kit/BACKLOG.md` is a different file: the Rome writing prompt with the lane notes, used by S6 and its successors.)

## Queue

| # | Spec | Model | Prompt to paste |
|---|---|---|---|
| 1 | S1 · Theme migration and housekeeping | any | Clone `apcanario/learning` and run S1 of `docs/pm-status-2026-10-28.md`: copy `design/theme.css` over `kit/shell.css`; in `kit/` run `build.py` and `verify.py` (ALL CHECKS PASSED) and `verify.py --shots`; fix the kit docs (remove the retired syllabus artifact links, replace zip references with the repo, fix the README file table); `CHANGELOG.md` session 11; publish the site to its existing artifact once, never force; commit and push. If the chat has room, also run S3. |
| 2 | S2 · The generator | any | Clone `apcanario/learning`. `generator/data/brand-ai/hub.py` describes a builder, `build_hub.py`, that does not exist. Write `generator/build_hub.py` (inlines `design/theme.css`, renders `hub.py`'s content to `generator/hubs/brand-and-ai-courses.html`) and `generator/check_page.py` (400 px, dark and light, no horizontal scroll, no control under 44 px, no console error; Playwright). Confirm the build reproduces the published hub v6.1 (https://claude.ai/artifact/XVMtDGuqTLkfuZapXstoMT; read it with the Artifact tool first). Update the row for Brand + AI Audit 1 in `docs/courses-index.md` (an audit artifact exists from 28 October; the index still says none ran). Commit and push. |
| 3 | S4 · Greek 13.2 and 13.5, the six flagged reports | Fable 5.1 | Clone `apcanario/learning`, `cd kit`, and follow `NEXT-SESSION.md` exactly, except: no zip; end with a commit and push. The six reports are 11.1, 11.2, 11.4, 11.5, 11.6, 11.8. |
| 4 | S5 · Bibliography spot-check | Fable 5.1, search on | Clone `apcanario/learning`, `cd kit`. Run S5 of `../docs/pm-status-2026-10-28.md`: one Rome and two Greek units; open every "(not verified)" reference in their `bibliography/<course>/r-<id>.md` by web search; correct or confirm; write `audits/bibliography-spot-check.md` with the hit rate; set the `artefacts` entry in `provenance.json` to "Sonnet 5.5, spot-checked with Fable 5.1 (sampled)" if under about one in ten is wrong, otherwise leave it flagged and say what is wrong. Build, commit, push. |
| 5 | S3 · Review counter | any | Clone `apcanario/learning`, `cd kit`. Run S3 of `../docs/pm-status-2026-10-28.md`: rewrite `review_due.py` to count content reports registered since the last `review_notes` entry whose provenance does not mention Fable 5.1 (FABLE REVIEW DUE at 4, exit 2; keep the call sites); replace the "three deep dives count as three units" paragraph of `BACKLOG.md` with the five-batch plan; confirm `python3 review_due.py` prints "0 of 4 modules written since the last review". Commit and push. Skip if S1 already did it. |
| 6 | S6 · Rome batch 1 | Opus 5.5 | Clone `apcanario/learning`, `cd kit`, and run `BACKLOG.md` for 11.3, 11.4, 11.5 and 11.6 only (writer, `check.py`, fresh checker, maintainer, `register.py`, bibliography file per report). Build, `verify.py`, publish the site once. Stop when `review_due.py` reads FABLE REVIEW DUE and say so in the first line. Commit and push. |
| 7 | Fable review of batch 1 | Fable 5.1 | The `method.md` §6 stratified-sample audit on Rome 11.3, 11.4, 11.5, 11.6; a module failing more than one claim in ten gets the kit scorecard audit (`kit/audits/AUDIT-BRIEF.md`). Then batches 2 to 5 as in `docs/courses-index.md`, a review after each. |

Brand + AI runs its own queue (the hub's Build order page): Audit 1 ran on 28 October; B2 is next, then B3, B4, A1, Audit 2.

## Proposed (awaiting Pedro's confirmation)

| # | Task | Why | Suggested place |
|---|---|---|---|
| P1 | Delete the "Knowledge transfer" artifact (https://claude.ai/artifact/Tgy4URAP8HTf4tPK7GZwfJ) | Its files are in the repo; its own text says delete after use | Pedro, by hand, any time |
| P2 | Update the Brand + AI Audit 1 row in `courses-index.md` | An audit artifact exists from 28 October; the index says none ran | Folded into S2 |

Done rows are in `CHANGELOG.md`.
