# S-DEC4 packet 7: unit prompts re-printed, pick your adventure gathered

Agent: Opus 5.5 (claude-opus-5-5), fresh, 20 Nov 2026. Repo `/home/claude/learning`, branch main, not committed (the main chat commits).

## Verdict

Done. 21 unit rows re-printed and saved, their ⚠ waits lines removed; 27 options written to `out/s-dec4/adventure/` (20 files plus `options.json`); one new proposed row, P-DEC16 (styling). Checks: `index_check` matches, `private_terms` OK, `baseline.py --check` clean before and after.

## Files changed

- `docs/BACKLOG.md`: the 21 unit rows (spec cell: ⚠ waits line removed; W-SCE1's hero note reworded; prompt cell: re-printed) and one new row, P-DEC16, under Proposed after P-DEC15. Nothing else changed: a script compared the file before and after with the 21 rows masked, and the rest was identical before P-DEC16 was added.
- `out/s-dec4/adventure/`: new, 20 `.md` files and `options.json`.
- `out/s-dec4/07-adventure.md`: this report.

The generator script is `/tmp/s-dec4-adv/gen.py`, outside the repo. The printed prompts are in `/tmp/s-dec4-adv/printed/` and the backlog before the edits is `/tmp/BACKLOG.before.md`.

## A. Unit rows

- **Count: 21, not 22.** The packet said 22. `grep "Waits for S-DEC4"` found 21 rows: W-DD-SP3, W-SCE1 to W-SCE18 and W-DD-SCE2's pair W-DD-SCE1 and W-DD-SCE2. That is 1 + 18 + 2 = 21. No other row carried the line.
- **Method.**
  1. The waits sentence "⚠ Waits for S-DEC4 (Pedro, 20 Nov 2026: no unit row runs until S-DEC4 has closed). " was removed from each spec cell by exact replacement.
  2. Then `python3 kit/next_prompt.py --row <row> --save` was run for each row. It saves the printed prompt in the prompt cell and keeps cells 1 to 3.
  3. A check script then confirmed three things for every row: the cell equals `head | <printed> |`, a fresh `--row` print equals the saved one, and the file outside the 21 rows is unchanged. All 21 passed.
  - Each print took about 0.1 s.
- **W-SCE1's other flag (the hero contour budget).**
  - `git diff 5e8c5d8 HEAD -- kit/build.py kit/verify.py` shows no S-DEC4 change to `HERO_INTERVAL` (still 23000) or to `verify.py`'s `20 * 1024` limit.
  - So the fix stays with W-SCE1. The row now says: "S-DEC4 did not change the budget (...), so this chat fixes it in `kit/build.py` before it files SCE1, as W-DD-SP2 did, and lists the changed hero layers as expected differences. The prompt below does not repeat this: work it at step 7b."
  - ⚠ **Finding:** the printed W-SCE1 prompt never mentions the hero budget (grep: 0 hits), and the spec cell is not pasted. In `adventure/supply-chain-execution.md`, above the line, I suggest pasting one extra first line with the prompt. Alternatives: a Corrections row (which every next prompt prints at step 1b), or a `NOTES`-style entry in `kit/next_prompt.py`. That choice is the main chat's or Pedro's. I did not change the prompt, since it is printed by script.
- **What changed in the re-printed prompts** (old saved prompts compared with new, word by word):
  - All of them: "`units_data.py`" became "`briefs.md`" and "the units in `course.toml`". The mirrors `claude/<course>-hub.py` and `-units_data.py` became `-course.toml` and `-briefs.md` (the S-DEC2 pack).
  - W-DD-SP3: its step 11 "`--save` saves the prompt of …" now names **W-SCE1 (unit SCE1)**, no longer "the next row in the Queue … (no unit of this course is left; its reliefs, row G-R-SP, wait for Pedro's confirmation)". That is correct: SCE joined `QUEUE` after DD-SP3's prompt was first saved. One side effect: the DD-SP3 prompt no longer names G-R-SP, and unlike SCE's last row the SP template has no closing-corrections prompt. G-R-SP is still listed under Proposed.
  - W-SCE7 still opens with "Do not run until Pedro has closed P-SCE6." (GATES).
- The "Next up" line was left alone.

## B. Options (`out/s-dec4/adventure/`, `options.json`: 27 entries)

The fields are as the packet set them. Three decisions:

1. A finished course with nothing queued has `prompt_file: null`, and its `.md` file says "Nothing queued" with its staleness dates.
2. The by-hand rows have `prompt_file: null` and a short `.md` file.
3. The rows of a grouped chat all point at the group's file (`DEC-A.md`, `DEC-B.md`, `DEC-C.md`). Their `state` and `next` fields name the group.

### Courses

The course list was checked with the loader: `kit/courses.py` COURSES holds 8 courses, and editions are academy, greece and marketing-ai. The counts come from the vault against the pack ORDER, cross-checked with `next_prompt.py --list` and the two index files.

| Course | State | Next | Blocking |
|---|---|---|---|
| greece | finished, 78 of 78 reports (83 modules with the audit unit) | nothing queued | none; search off, no staleness date |
| rome | finished, 79 of 79 reports (85 modules) | nothing queued | none |
| brand-ai | finished, 22 of 22 (A 11, B 11; ORDER lists 19 because A2, A6 and A9 are the rewrites); private | nothing queued | staleness checks on 28 Apr, 29 Apr and 2 May 2027 |
| ux | finished, 15 of 15; private | nothing queued | staleness checks on 10 May 2027 |
| personal-brand | finished, 12 of 12; reliefs done (G-R) | nothing queued | staleness checks on 12 and 13 May 2027 |
| building-with-ai | finished, 13 of 13; reliefs done; CP-4 done in W-SP1 | nothing queued | staleness checks on 15 and 16 May 2027 (with BW6 and DD-BW3 re-read) |
| sport-psychology | 12 of 13 | DD-SP3, W-DD-SP3 | none now; 23 open flags in its prompt, among them F218 (quality review, worked inside the row); S-SP1 is not a gate; G-R-SP comes after |
| supply-chain-execution | 0 of 20 | SCE1, W-SCE1 | the hero budget inside the row (above); P-SCE11 before W-SCE6; the P-SCE6 gate holds W-SCE7 to W-DD-SCE2; P-SCE1 before sharing; G-R-SCE comes after |

There is no open REWRITE verdict in `docs/courses-index.md`. The Corrections and Carried proposals sections are empty. No staleness check is due before 28 Apr 2027. `kit/verify-hashes.json` exists (commit fd10c5c), so the first unit chat's verify is scoped.

### Non-unit work

- **CSS and styling rows (§7).** None existed in `docs/BACKLOG.md`; the only CSS mentions were inside other rows. I added **P-DEC16** under Proposed, the id after P-DEC15, with its prompt in `adventure/P-DEC16.md`.
  - The prompt's design: Pedro is present, and a slot holds his styling list. If he leaves it empty, an Opus agent surveys `verify.py --shots` and ranks faults, and Pedro keeps or drops items.
  - Edits go to `theme.css` (then `cp` to `kit/shell.css`) and `brands/academy.toml` only.
  - The expected differences are the inlined theme in every shell-carrying file, academy and greece. Then the manifest is re-recorded, a full verify runs, and Academy is published along with the greece artifact.
  - Corroboration from memory (Project memory `areas/learning.md`, 19 Nov 2026): Pedro asked for "fine-tuning of Academy's CSS and styling" to follow the refactor. The row itself cites only `docs/decoupling.md` §7.
- **By hand, no prompt:** P-SCE1, P-SCE6, P-SCE11. No other row is marked for Pedro by hand.
  - S-SP1 is "For Pedro (a brief or preamble change)" but it is a chat, so it got a prompt: Fable 5.2, Pedro present, with an Opus 5.5 checker.
- **Prompts written:**
  - Grouped chats: DEC-A, DEC-B, DEC-C.
  - Single rows: P-DEC5, P-DEC16, G-R-SP (blocked by W-DD-SP3), G-R-SCE (blocked by the 20 SCE units and P-SCE6), S-SP1, P-SCE10.
  - P-SCE10 is written for the first course, Supply Chain Planning for Product Teams, on Fable 5.2 with Pedro present. The same prompt with the next title serves the other three, in catalog order.
  - Each prompt follows S-DEC4's standard: the clone with its ten-minute timeout; the thin Sonnet 5.5 main chat with Opus 5.5 agents and a separate Opus 5.5 checker; the agent rules; the §5 test; the checks; the publish where output changes (artifact read first, patch, sha256 read-back, then `kit/deploy.sh academy`, and the greece artifact only if its bytes changed); the close per method §8 steps 1 to 5; the reply.
  - No row has a prompt column under Proposed, so every non-unit prompt lives only in the options folder.
- **Grouping** (each row keeps its id and closes on its own line):
  - **DEC-A = P-DEC12, P-DEC10, P-DEC13, P-DEC14.** All four touch `kit/verify.py` and none changes Academy's bytes, so one clone, one checker and one 25-minute full verify serve them. If P-DEC14 surfaces drawer findings, the prompt switches to the output-changed test and one publish.
  - **DEC-B = P-DEC4, P-DEC9, P-DEC6.** None changes the site. Each touches a different `kit/*.py`, and every `kit/*.py` change forces a full verify, so one verify serves all three. P-DEC6 rewrites about 30 bibliography files that are build outputs in `kit/baseline.json` but outside `kit/academy/`: they are listed as expected differences, and the manifest is re-recorded after proof that they differ only by the path.
  - **DEC-C = P-DEC8, P-DEC11, P-DEC15.** All three change output on purpose (`build.py`, `howbuilt.py`), so they share one expected-differences proof, one manifest re-record, one full verify and one publish.
  - **P-DEC5 is kept alone** because it puts figure geometry at risk. It is suggested before P-DEC16 if the styling pass wants new `--sans` or `--mono` faces.

## Findings for the main chat (not fixed: outside the packet)

1. **Orphan prompt bodies in `docs/BACKLOG.md`.** Lines 68 to 198 of the backlog before the edits (§4c) hold two full prompt bodies with no row line: W-SP1's, from "Read first" to its "**Reply:**", and W-SP6's. They sit between the §4c table header and W-DD-SP3's row and belong to rows already closed. It looks like a row was moved to the changelog without its continuation lines. They are untouched, because the packet allows no other row change. Proposed: remove them in the close.
2. **Two P-DEC rows have their cells shifted.** P-DEC5 and P-DEC6 carry "Opus 5.5" in the Why column and leave Suggested place empty. The text is unchanged.
3. **Planned Sports courses have no row.** The Sports track's planned courses in `catalog.toml` (Running a Squad, Managing an Athlete's Career; "each designed once [Sport Psychology for Coaches] is complete") have no row like P-SCE10. They will need a design-chat proposal once DD-SP3 closes. Personal Mythology's eight courses to come likewise have no row. Neither is a course in `kit/courses.py`, so neither is an option.
4. **The option files use "Pedro" on purpose.** `kit/private_terms.py` run over `out/s-dec4/adventure/*` reports "Pedro" (113 hits). Like `docs/BACKLOG.md`, these are internal prompt files, not built or published. The repo's own `private_terms.py` run (site and public courses) prints OK.

## Check results (last lines)

- Before any change, `python3 kit/baseline.py --check`: `baseline: clean` (academy 457 files, 0 differ; greece 82 files, 0 differ).
- After the edits:
  - `python3 kit/index_check.py`: `courses-index.md matches the sources`.
  - `python3 kit/private_terms.py`: `125 files, 0 private terms, 114 warnings: OK`.
  - `python3 kit/baseline.py --check`: `academy: 457 files, 0 differ` / `greece: 82 files, 0 differ` / `baseline: clean` (2 m 34 s). The docs-only edits did not change the build.

No unit was written or filed. Nothing was published or deployed, and nothing was committed.
