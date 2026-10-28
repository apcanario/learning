# Backlog

The ordered queue of chats for the Learning Project. One row is one chat. Take the top row that is not done; paste its prompt into a new chat in the Project on the model named; when the chat ends, move the row to Done with the date and commit. Specs are in `pm-status-2026-10-28.md`; the rule for keeping this file and `CHANGELOG.md` current is `method.md` §8: a finished row moves to the changelog, tasks uncovered are added as *proposed* rows, and the backlog is handed to Pedro at the end of every chat for confirmation of what is next. (`kit/BACKLOG.md` is a different file: the Rome writing prompt with the lane notes, used by S6 and its successors.)

## Queue

Order decided 28 October 2026 (`academy.md` AD4, reworked after the Brand + AI hand-off landed in the repo; P4, S1 and A1 with P5 to P7, then P8 to P11 and A0, done the same day). Two lanes: the **Academy lane** (one chat at a time, in order) and the **Brand + AI writing lane** (runs in parallel, one unit per chat, per `docs/handoffs/2026-10-28-brand-ai-handoff.md` step 2 and `skills/`). History content work (S4, S5, S3, S6) follows the Academy lane.

### Academy lane

| # | Spec | Model | Prompt to paste |
|---|---|---|---|
| 1 | A3 · Brand + AI migration | any | Clone `apcanario/learning` and run A3 of `docs/academy.md`: `kit/build.py` imports `generator/build_hub.py`'s page builders as the Markdown course family; one course context per Brand + AI course in the drawer with Learn pages and a "How it is built" group; `verify.py` absorbs `check_page.py`; publish Academy; delete the Brand + AI and Audience Growth artifacts; retire `build_hub.py`, `hub.js`, `check_page.py`, `build_history.py`; point `skills/file-unit`, `skills/new-course` and `SETUP.md` §7/§9 at Academy. Commit and push. |
| 2 | A2 · Split the monolith | any | Clone `apcanario/learning` and run A2 of `docs/academy.md`: shell page plus one published file per report or unit loaded by `fetch`; hash routing, prev/next and stored progress intact; publish through the Artifact tool's `files`; `verify.py` extended with the size table. Commit and push. |
| 3 | A4 · "How it was built" per course | any | Clone `apcanario/learning` and run A4 of `docs/academy.md`: one generated page per course from `provenance.json`, `review_notes`, `kit/audits/`, the Markdown front matter and the audit log; nothing typed by hand. Publish, commit, push. |
| 4 | A5 · Vault as source and the method | any | Clone `apcanario/learning` and run A5 of `docs/academy.md`: `build.py` reads Markdown courses from `courses/` (the `generator/data/<slug>/units/` copies go away); `courses-index.md` generated or checked by script; `method.md` §7, `SETUP.md` and the four skills updated; the Project instructions name Academy. Commit and push. |
| 5 | S4 · Greek 13.2 and 13.5, the six flagged reports | Fable 5.1 | Clone `apcanario/learning`, `cd kit`, and follow `NEXT-SESSION.md` exactly, except: no zip; end with a commit and push. The six reports are 11.1, 11.2, 11.4, 11.5, 11.6, 11.8. |
| 6 | S5 · Bibliography spot-check | Fable 5.1, search on | Clone `apcanario/learning`, `cd kit`. Run S5 of `../docs/pm-status-2026-10-28.md`: one Rome and two Greek units; open every "(not verified)" reference in their `bibliography/<course>/r-<id>.md` by web search; correct or confirm; write `audits/bibliography-spot-check.md` with the hit rate; set the `artefacts` entry in `provenance.json` to "Sonnet 5.5, spot-checked with Fable 5.1 (sampled)" if under about one in ten is wrong, otherwise leave it flagged and say what is wrong. Build, commit, push. |
| 7 | S3 · Review counter | any | Clone `apcanario/learning`, `cd kit`. Run S3 of `../docs/pm-status-2026-10-28.md`: rewrite `review_due.py` to count content reports registered since the last `review_notes` entry whose provenance does not mention Fable 5.1 (FABLE REVIEW DUE at 4, exit 2; keep the call sites); replace the "three deep dives count as three units" paragraph of `BACKLOG.md` with the five-batch plan; confirm `python3 review_due.py` prints "0 of 4 modules written since the last review". Commit and push. |
| 8 | S6 · Rome batch 1 | Opus 5.5 | Clone `apcanario/learning`, `cd kit`, and run `BACKLOG.md` for 11.3, 11.4, 11.5 and 11.6 only (writer, `check.py`, fresh checker, maintainer, `register.py`, bibliography file per report). Build, `verify.py`, publish Academy once. Stop when `review_due.py` reads FABLE REVIEW DUE and say so in the first line. Commit and push. |
| 9 | Fable review of Rome batch 1 | Fable 5.1 | The `method.md` §6 stratified-sample audit on Rome 11.3, 11.4, 11.5, 11.6; a module failing more than one claim in ten gets the kit scorecard audit (`kit/audits/AUDIT-BRIEF.md`). Then batches 2 to 5 as in `docs/courses-index.md`, a review after each. |

### Brand + AI writing lane (parallel; one unit per chat)

| # | Unit | Model | Prompt |
|---|---|---|---|
| B-1 | B3 · Prompting that holds up (search off) | Opus 5.5 write · Fable 5.1 fresh check | `docs/handoffs/2026-10-28-brand-ai-handoff.md` step 2: paste the B3 brief from `generator/data/brand-ai/units_data.py` with the chat instructions used for B2; fresh check with `skills/audit-units` ("Fresh check of one Brand + AI unit"); apply findings; file with `skills/file-unit` (until A3 lands: `build_hub.py`, `check_page.py`, republish the hub; after A3: Academy). Commit and push. |
| B-2 | B4 · Context engineering (search off) | same | Same procedure. |
| B-3 | A1 · Positioning (search off) | same | Same procedure. |
| B-4 | Audit 2 over B2, B3, B4, A1 | Fable 5.1, search on | `skills/audit-units`, `method.md` §6 prompt verbatim; log in `hub.py` AUDIT_LOG (or Academy's audit log after A3) and `docs/courses-index.md`; no new unit while a REWRITE is open. |

Dropped 28 October 2026: S2 (`generator/build_hub.py` exists; A3 absorbs it).

## Proposed (awaiting Pedro's confirmation)

| # | Task | Why | Suggested place |
|---|---|---|---|
| P1 | Delete the "Knowledge transfer" artifact (https://claude.ai/artifact/Tgy4URAP8HTf4tPK7GZwfJ) | Its files are in the repo; its own text says delete after use. Pedro held it on 28 Oct: the Brand + AI pipeline still uses it to move files into Project knowledge (handoff, Automation notes) | After A3, or when knowledge uploads come from the repo |
| P3 | File the three fresh-check reports of A2, A6, A9 (28 Oct 2026, Fable 5.1) into `audits/brand-ai/` | They exist only in their chats; the hub summarises them (A9 2/15/8, A2 3/13/11, A6 1/9/7) | Any chat that can read those chats, or paste them in |
| P12 | Desktop and tablet screenshots of each new page in `file-unit` and `new-course` (`verify.py --shots`, `check_page.py --shots`) as a filing step, so a new unit or hub is looked at once at the three widths | P11 made the checks automatic; the look is still only checked by eye when someone runs `--shots`, and the two skills do not say to | After A3 (the skills are rewritten there) |
| P13 | A2 note: `check_page.py` and `verify.py` measure the desktop sidebar on a single-file page; once the shell `fetch`es reports, the desktop and tablet passes must load a report through the shell as the phone pass will | The three-width passes were written against the monolith | A2 |

Done rows are in `CHANGELOG.md`.
