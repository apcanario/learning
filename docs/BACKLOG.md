# Backlog

The ordered queue of chats for the Learning Project. One row is one chat. Take the top row that is not done; paste its prompt into a new chat in the Project on the model named; when the chat ends, move the row to Done with the date and commit. Specs are in `pm-status-2026-10-28.md`; the rule for keeping this file and `CHANGELOG.md` current is `method.md` §8: a finished row moves to the changelog, tasks uncovered are added as *proposed* rows, and the backlog is handed to Pedro at the end of every chat for confirmation of what is next. (`kit/BACKLOG.md` is a different file: the Rome writing prompt with the lane notes, used by S6 and its successors.)

## Queue

Order decided 28 October 2026 (`academy.md` AD4, reworked after the Brand + AI hand-off landed in the repo; P4, S1 and A1 with P5 to P7, then P8 to P11 and A0, done the same day). Two lanes: the **Academy lane** (one chat at a time, in order) and the **Brand + AI writing lane** (one unit per chat, per `docs/handoffs/2026-10-28-brand-ai-handoff.md` step 2 and `skills/`). Order decided 28 October 2026 (Pedro, 14:57): the Academy lane runs first, rows 1 to 3 (A2, A4, A5; all three done the same day), then the Brand + AI lane (B-1 onward); the history content work (S4, S5, S3, S6) follows after. The lanes no longer run in parallel.

### Academy lane

| # | Spec | Model | Prompt to paste |
|---|---|---|---|
| 4 | S4 · Greek 13.2 and 13.5, the six flagged reports | Fable 5.1 | Clone `apcanario/learning`, `cd kit`, and follow `NEXT-SESSION.md` exactly, except: no zip; end with a commit and push. The six reports are 11.1, 11.2, 11.4, 11.5, 11.6, 11.8. |
| 5 | S5 · Bibliography spot-check | Fable 5.1, search on | Clone `apcanario/learning`, `cd kit`. Run S5 of `../docs/pm-status-2026-10-28.md`: one Rome and two Greek units; open every "(not verified)" reference in their `bibliography/<course>/r-<id>.md` by web search; correct or confirm; write `audits/bibliography-spot-check.md` with the hit rate; set the `artefacts` entry in `provenance.json` to "Sonnet 5.5, spot-checked with Fable 5.1 (sampled)" if under about one in ten is wrong, otherwise leave it flagged and say what is wrong. Build, commit, push. |
| 6 | S3 · Review counter | any | Clone `apcanario/learning`, `cd kit`. Run S3 of `../docs/pm-status-2026-10-28.md`: rewrite `review_due.py` to count content reports registered since the last `review_notes` entry whose provenance does not mention Fable 5.1 (FABLE REVIEW DUE at 4, exit 2; keep the call sites); replace the "three deep dives count as three units" paragraph of `BACKLOG.md` with the five-batch plan; confirm `python3 review_due.py` prints "0 of 4 modules written since the last review". Commit and push. |
| 7 | S6 · Rome batch 1 | Opus 5.5 | Clone `apcanario/learning`, `cd kit`, and run `BACKLOG.md` for 11.3, 11.4, 11.5 and 11.6 only (writer, `check.py`, fresh checker, maintainer, `register.py`, bibliography file per report). Build, `verify.py`, publish Academy once. Stop when `review_due.py` reads FABLE REVIEW DUE and say so in the first line. Commit and push. |
| 8 | Fable review of Rome batch 1 | Fable 5.1 | The `method.md` §6 stratified-sample audit on Rome 11.3, 11.4, 11.5, 11.6; a module failing more than one claim in ten gets the kit scorecard audit (`kit/audits/AUDIT-BRIEF.md`). Then batches 2 to 5 as in `docs/courses-index.md`, a review after each. |

### Brand + AI writing lane (parallel; one unit per chat)

| # | Unit | Model | Prompt |
|---|---|---|---|
| B-1 | B3 · Prompting that holds up (search off) | Opus 5.5 write · Fable 5.1 fresh check | `docs/handoffs/2026-10-28-brand-ai-handoff.md` step 2: paste the B3 brief from `generator/data/brand-ai/units_data.py` with the chat instructions used for B2; fresh check with `skills/audit-units` ("Fresh check of one Brand + AI unit"); apply findings; file with `skills/file-unit` (Academy: build, verify, publish the artifact, `deploy.sh`). Commit and push. |
| B-2 | B4 · Context engineering (search off) | same | Same procedure. |
| B-3 | A1 · Positioning (search off) | same | Same procedure. |
| B-4 | Audit 2 over B2, B3, B4, A1 | Fable 5.1, search on | `skills/audit-units`, `method.md` §6 prompt verbatim; log in `hub.py` AUDIT_LOG and `docs/courses-index.md`; no new unit while a REWRITE is open. |
| B-5 | DD-B3 · Deep dive: how the best practitioners use the tool (search on) | Opus 5.5 write · Fable 5.1 fresh check | Added 28 Oct 2026 (Pedro's request: Karpathy's documented practice and the other verifiable methods of using AI as a tool). Same procedure as B-1: paste the DD-B3 brief from the hub's Build · Briefs page, web search on; fresh check; file. Then A3, B5 and the rest in the hub's build order. |

Dropped 28 October 2026: S2 (`generator/build_hub.py` exists; A3 absorbs it).

## Proposed (awaiting Pedro's confirmation)

| # | Task | Why | Suggested place |
|---|---|---|---|
| P23 | Record a written date per history report: `register.py` stores the date beside the model in `provenance.json` (or a `written` map per course); backfill the 137 from `review_notes` and `kit/CHANGELOG.md` where a session dates them, "not recorded" otherwise; `howbuilt.py` shows it; the home's New since list (A6) reads the same map, so history reports appear there once dated | A4 found `provenance.json` holds no date per report, so the history "How it was built" pages say so instead of giving one; the Brand + AI pages have it from front matter. A5 makes the vault the source for new units, so only the backfill is extra | Academy lane, after A5 (A5 did not settle it: it changed the markdown courses only; history dates still come from `provenance.json`) |
| P24 | Decide where the audit and review files open for someone Academy is shared with: today every file link on the "How it was built" pages points at the private repo `apcanario/learning` on GitHub, which opens only for Pedro. Options: publish them as fetched pages in Academy (about 120 Markdown files rendered once per build; also on the public Pages repo) or keep them private and say so | AD7 makes Academy navigable by anyone it is shared with; the provenance pages are, but their evidence is not. Publishing audits publicly is Pedro's call | Academy lane, after A5; Pedro decides first |
| P27 | Figures in the written Brand + AI units where the text already carries the numbers: A2 (platform economics, a `compare` of reach or payout per platform), A9 (benchmarks, `compare`), B2 (model lineups, `compare`); one ` ```viz ` fence each, from the unit's own sourced figures, captioned to the source | A8 built the contract and the history example; the Brand + AI units have the most numeric content and no figure yet. Each is a small edit to a filed unit, so it is a filing chat, not a rewrite; the fresh check is not rerun | Brand + AI lane, after B-4 (audit 2), so the audit sees the units as written |
| P26 | Tablet rail: between 768 and 1100 px the drawer becomes a narrow icon rail (track squares, course numbers) that expands on tap, instead of the phone drawer | The A6 plan listed it; not built because the drawer works at tablet width and Pedro reads on a phone. Optional | Academy lane, last; drop if the tablet is never used |
| P25 | `kit/index_check.py` also checks the audit counters in `docs/courses-index.md`: the history counter against the rewritten `review_due.py`, the Brand + AI counter against `hub.py` `AUDIT_LOG` and the vault's written dates | A5 left the counters hand-kept because `review_due.py` still counts syllabus units (S3 rewrites it); the counter is the one fact in the index that decides whether the next chat is a unit or an audit | Academy lane, after S3 |

Done rows are in `CHANGELOG.md`.
