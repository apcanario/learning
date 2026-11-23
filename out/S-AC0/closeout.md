# S-AC0 · close-out

Close-out agent: claude-opus-5-5, a fresh agent, 23 Nov 2026, on the working tree over HEAD 8285ef2 (the row not yet landed). Nothing committed, pushed or landed; no `.py` file edited; `kit/land.py`, `build.py` and `verify.py` not run; `courses/athlete-career/briefs.md` not touched (sha256 33308c81d6b43c334d72b4cd482196d533855f2b11335c05831bb50fcdfe1cc3). No memory, past-chat, Projects, connector or Artifact tool used.

## Files changed

- `docs/CHANGELOG.md`: two rows added at the top, in S-AIE0's form: the S-AC0 row (date, session, models, result, "see git log"), and a proposal row "P-AC1 to P-AC12 ... accepted by the owner on 21 Nov 2026; registered at S-AC0" in the form of the P-SP2 and P-SP3 rows (dated 23 Nov 2026, the day it was recorded, so the file stays newest first; the 21 Nov acceptance, the 22:18 and 22:26 times, P-AC2 superseded, P-AC6 withdrawn and P-AC12 replaced are in its cells, as `docs/public-courses.md` §1 has them).
- `docs/BACKLOG.md`: the S-AC0 row and its one-row table (header, the launcher with overrides 1 to 13 and the general rules) removed from section 4i; the heading, intro paragraph and the W-AC bundles kept; "Next up" now names S-EG0 (with S-AC0's and S-AIE0's closes), or W-SCE3, or W-AIE1's bundle, or W-AC1's bundle; G-R-AC kept under Proposed, unchanged. S-EG0's launcher: overrides 1 to 13 present, adapted to the History track (items 1, 2, 3, 5, 7, 10, 12, 13); override 1's conditional "Parts 1-10 exist ...; if S-AC0 closed first it took Part 11, so it is **Part 12**; otherwise take the next free number." made definite: "Parts 1-11 exist (Part 10 = AI in Supply Chain Execution; Part 11 = Managing an Athlete's Career, taken by S-AC0, which closed first), so it is **Part 12**." (as S-AIE0 made S-AC0's definite). Nothing else in S-EG0's row changed.
- `docs/site-log.md`: Done entry "2026-11-23 · S-AC0 · Sports · Managing an Athlete's Career, a new course, added: designed; 18 units to write; Running a Squad is still to come in the Sports track."; Next entries 51 to 68 added, one per unit in writing order (AC1 to AC15, DD-AC2, DD-AC1, DD-AC3), in S-AIE0's form; entries 1 to 50 unchanged, no gap; the header's Area rule now "Sports (courses SP and AC; ...)", as S-AIE0 added AIE to Supply Chain's.
- `docs/sports-track-coming-soon.md`: beyond the registrar's status cell ("syllabus written 21 Nov 2026") and reader line, only the lines that contradicted the course being set up: the opening "Neither course below is a backlog row yet"; "Neither syllabus is written before Sport Psychology is complete ..." (now said of Running a Squad, with AC's syllabus date and path); a "Now" line at the head of section 3 (set up 23 Nov 2026, 0 of 18; the syllabus wins over the 19 Nov scope below); the last step "then of Managing an Athlete's Career" (now: designed first, P-AC7). The Sport Psychology status cell ("11 of 13") is stale but does not concern this course: left.
- `inbox/athlete-career/` deleted (8 files, `git rm -r`) after confirming `docs/athlete-career-syllabus.md`, `docs/athlete-career-prompts.md` and `courses/athlete-career/` (briefs, course.toml, notes, pages) are filed; its 8 lines removed from `inbox/SHA256SUMS` (6 egypt lines left; `sha256sum -c` passes). The design's `athlete-career-units.toml` and setup prompt are not filed in `docs/`, as with S-AIE0 (course.toml holds the data).
- `out/S-AC0/closeout.md`: this file.

## Placeholder for the main chat

- `docs/CHANGELOG.md`, S-AC0 row: "Verify: [TO BE RECORDED BY THE MAIN CHAT AFTER VERIFY]." Replace with the verify result (and, as S-AIE0's row has them, the landing commit, the artifact republish with sha256 read back, and the deploy run) once known.

## Checks

- `python3 kit/private_terms.py`: 170 files, 0 private terms, 313 warnings: OK (the new site-log line 84 warns on "Portugal", the unit title DD-AC3).
- `python3 kit/index_check.py`: courses-index.md matches the sources.
- `python3 kit/next_prompt.py --row W-AC1`: first line exactly `Clone apcanario/learning (shallow, push access).`
- `python3 kit/next_prompt.py --row W-SCE3 | sha256sum`: 8b4cce450497cadbe87131d974484fed93e4517c6b6228c87e1e9162e229f8e0, unchanged.
- `docs/CHANGELOG.md` new rows: 7 `|` fields each, no `|` inside a cell.
