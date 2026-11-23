# S-AIE0 · close-out

Close-out agent: claude-opus-5-5, a fresh agent, 23 Nov 2026, on HEAD 9598c18 (= origin/main; the row landed at 34b411c). Nothing committed, pushed or landed; no `.py` file edited; `build.py` and `verify.py` not run.

## Files changed

- `docs/CHANGELOG.md`: the S-AIE0 row added at the top (date, session, models, result, "see git log").
- `docs/BACKLOG.md`: the S-AIE0 row and its one-row table removed from section 4h (the intro paragraph and the W-AIE bundles kept); "Next up" now names S-AC0, then S-EG0 (the owner's order), or W-SCE3, or W-AIE1's bundle, or any other non-unit row; the launchers of S-AC0 and S-EG0 rewritten (below).
- `docs/site-log.md`: Next entry 37 (AIE, the course) removed and a Done entry added (2026-11-23, S-AIE0, "AI in Supply Chain Execution, a new course, added: designed; 14 units to write."); Next entries 37 to 50 added, one per unit AIE1 to AIE13 and DD-AIE1, in the S-SCP0 form (§8 step 1b: an entry for each item in the queue). Entries 1 to 36 unchanged, no gap.
- `inbox/ai-in-supply-chain-execution/` deleted (8 files, `git rm -r`), and its 8 lines removed from `inbox/SHA256SUMS` (14 lines left; `sha256sum -c` passes). `inbox/athlete-career/` and `inbox/egypt/` kept.
- `out/S-AIE0/closeout.md`: this file. `out/S-AIE0/landing-report.md` is untracked: commit it with the close.

## Launcher changes

Both launchers keep the first line exactly `Clone apcanario/learning (shallow, push access).`; the second line is the owner's attach line ("`apcanario/academy` is approved for attach with push access: attach it at the start with add_repo and clone it once beside the repo."); the third is the old "Row ... Work <setup prompt> in full ..." line without its part-number and delete sentences (now overrides 1 and 11). Then "OVERRIDES (from S-AIE0, 23 Nov 2026)" items 1 to 13 and the general rules for every agent, in the wording of `/home/claude/packet-aie/overrides.md` (1 to 6, 10) and of the main chat's list (7 to 9, 11 to 13), with the row's own names and paths. The lessons of this row are folded in: (a) part numbers into item 1; (b) the artifact wrapper (the live prefix written out in full), patch-mode publish of changed files on slug f27e8dc3-7579-4b08-91d2-516bfe862526 from /home/claude, sha256 read back with list_files, and (d) P-AIE8's `built.html` paths in the `--expected` file, into item 8; (c) `verify.py` detached and polled into item 9. No `|` and no line ending in `|` inside a cell (checked with `kit/land.py`'s record grouping: each launcher is one record of 19 lines).

- **S-AC0**: Part 11; outlines waived whatever setup step 2h says, G-R-AC; case facts checked against `courses/sport-psychology/notes/case-facts.md`; mirrors `claude/athlete-career-*`; flags AC1..AC15, DD-AC1..DD-AC3; delete `inbox/athlete-career/`; item 12 passes the overrides to S-EG0 (already written there: check, and correct the part if Part 11 was not S-AC0's); item 13 ends the reply with S-EG0's launcher, the starter just before it.
- **S-EG0** (differs from S-AC0 in items 1, 2, 3, 5, 7, 10, 12, 13, as its OVERRIDES line says): Part 12 if S-AC0 closed first, else the next free; no outlines and no reliefs, P-EG6 becomes G-R-EG, and no kit `.py` edit beyond the QUEUE line (a P-EG2 renderer change stays a proposal); item 3: the course is a markdown course (`skills/new-course` §1 lead, P71; setup step 1 says the same), not the `courses/<id>/inputs/` history form of §1's first bullet, which P-EG4 corrects; item 5: no case register, so names and dates are checked against `kit/AGENT-SPEC.md` and filed Greece and Rome units and flagged, nothing restored; mirrors `claude/egypt-*`; flags EG1..EG57, DD-EG1..DD-EG21; item 12: none left to pass on; item 13: the reply lists the courses still to be written and ends with the starter.

Choice recorded: the main chat's note called EG "history family, not a markdown pack course"; the repo says otherwise (`inbox/egypt/setup-prompt.md` step 1 "for a markdown course ... from `courses/_template/`"; `skills/new-course` §1 "Every new course is a markdown course (P71) ... a new culture included, does not start in it"; the design's P-EG2 and P-EG4). Override 3 follows the repo; the main chat may veto.

## Checks

- `python3 kit/private_terms.py`: 157 files, 0 private terms, 114 warnings: OK.
- `python3 kit/index_check.py`: courses-index.md matches the sources.
- `python3 kit/next_prompt.py --row W-AIE1`: exit 0, 92 lines, first line exactly `Clone apcanario/learning (shallow, push access).`
- `python3 kit/next_prompt.py --row W-SCE3`: exit 0, 93 lines, same first line; byte-identical to the print at HEAD (before this close-out's edits). It differs from the registrar's pre-row `print-before.txt` only by the two carried proposals P-AIE8 and P-AIE9, added by the findings applier.
