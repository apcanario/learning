# Packet 6: the fresh check's findings applied (row S-DEC4)

Agent: fresh Opus 5.5 (claude-opus-5-5), 20 Nov 2026. Nothing committed or pushed. Inputs: `out/s-dec4/checker/fresh-check-s-dec4.md`, `out/s-dec4/packets/00-common.md`, `06-apply.md`, `docs/decoupling.md`, the earlier agents' reports (for the proposed rows and results).

**Verdict: done.** Both errors, all five should-fixes and minors M2, M4 and M6 applied. M1, M3 and M5 are not one-line fixes: recorded and proposed as rows. Academy and greece are byte-identical (`baseline: clean`). The only manifest change is the `README.md` entry (kit/README.md prose, rehashed). marketing-ai and greece pass `verify.py --edition` with the fixes in. A corrupt record falls back to a full run and says why.

## Check results

| Step | Command | Last line(s) | Wall |
|---|---|---|---|
| Before any change | `python3 kit/baseline.py --check` | `academy: 457 files, 0 differ` / `greece: 82 files, 0 differ` / `baseline: clean` | about 2 m 45 s |
| After the code and doc edits | `python3 kit/baseline.py --check` | `academy: changed README.md` / `academy: 457 files, 1 differ (0 added, 0 removed, 1 changed)` / `greece: 82 files, 0 differ` / `baseline: 1 files differ` (expected: kit/README.md prose, see S2) | 190 s |
| Proof that README is the only change | `git diff kit/README.md` after the build | 4 additions, 2 deletions: the `verify.py` row, the two new rows and the line on adding a course. The size table is unchanged. The `README.md` entry of `kit/baseline.json` rehashed (`0a47a026…` → `46635ae0…`, 1 line) | n/a |
| End | `python3 kit/baseline.py --check` | `academy: 457 files, 0 differ` / `greece: 82 files, 0 differ` / `baseline: clean` | 153 s |
| Probe `/tmp/s-dec4-apply` (copy of the main tree after every code edit; `cmp` of verify.py, verify_scope.py, private_terms.py and courses.py equal to the main tree) | `python3 kit/build.py --edition marketing-ai` then `cd kit && python3 verify.py --edition marketing-ai` | first line `full: no passed run recorded for edition marketing-ai (verify-hashes.json)`; `What's new: edition marketing-ai's largest day (2026-11-16, 79,671 words) is under 110,000 words, so the build's scale (11,000 words a level) cannot raise it to 10 levels; it is checked against that scale, 7 levels, at most 25; the 10 to 25 range is left out here`; `verify-hashes.json: edition marketing-ai recorded, 42 pages` / `ALL CHECKS PASSED` | 22 s + 384 s |
| Same probe, E1 on greece | `python3 kit/build.py --edition greece` then `verify.py --edition greece` | first line `full: no passed run recorded for edition greece (verify-hashes.json)`. There is no "What's new:" scale line, so the 10 to 25 range applied (221,673 words, 20 levels) and passed. New S5 line: `nav: no second history course in this edition; ...`. Then `verify-hashes.json: edition greece recorded, 82 pages` / `ALL CHECKS PASSED` | 34 s + 418 s |
| Probe `/tmp/s-dec4-scope`, corrupt record, `verify.py --edition marketing-ai` first line (run cut at 25 s) | records `garbage{`, empty, `[1,2]`, `{"marketing-ai": "x"}`, `{"marketing-ai": {"pages": {}}}`, `{"marketing-ai": {"global": [], "pages": {}}}` | each: `full: verify-hashes.json unreadable or malformed for edition marketing-ai` | about 25 s each |
| Same, run to the end over `{"marketing-ai": {"pages": {}}}` | `verify.py --edition marketing-ai` | first line as above; `verify-hashes.json: edition marketing-ai recorded, 42 pages` / `ALL CHECKS PASSED`; the record now has `global` and `pages` | 391 s |
| `Scope` directly (`/tmp/s-dec4-scopetest.py`, academy site of the copy, state in /tmp) | 11 shapes: garbage, empty, list, string, null, edition a string, edition `{}`, pages only, global a list, binary bytes, another edition only; then missing; then save and re-scope; then save over `[1,2]` | the malformed shapes: `full: … unreadable or malformed for edition academy`; another edition only and missing: `full: no passed run recorded …`; after save: `scoped: no page changed + home; 4 of 292 pages checked …`; save over a malformed file writes a valid record. No crash | instant |
| `python3 kit/private_terms.py` (after M2) | `PUBLIC` derived = `('personal-brand', 'building-with-ai', 'sport-psychology', 'supply-chain-execution')`, the same as before; `125 files, 0 private terms, 114 warnings: OK` | 1 s |

The full academy verify was not run (packet: the main chat runs it once).

## Findings: id, verified, applied, how

| Id | Verified | Applied | How |
|---|---|---|---|
| E1 What's new range on greece, no lower bound | yes (verify.py: `if FULL:` only; greece's largest day 221,673 words, `NEW_INTERVAL = 11000`, 20 levels) | yes | Replaced the block with the checker's code: `if FULL or (top[1] or 0) >= 10 * NEW_INTERVAL:` gives the range, otherwise the scale. I added `or 0` so a day with no word count cannot crash the check. The printed line now gives the edition's largest day, the 110,000-word threshold, and "(it stands 0 levels: no rise is drawn)" when that is the case. Docstring sentence updated. Decision recorded in decoupling §6 (S-DEC4 notes): an edition below 110,000 words is held to the scale and a 0-level What's new is accepted by design; a per-edition scale is proposed as P-DEC15. Greece passes in range. |
| E2.1 new-course step 5b | yes (`REL_COURSES` gone from verify.py; line 1703 derives it from `reliefs`) | yes | The checker's text, plus "(these three lists stay typed until P-DEC9)". ⚠ The account copy of the skill must be re-saved (§8 risk): for Pedro, or the main chat's save card. |
| E2.2 BACKLOG G-R-SP, G-R-SCE | yes | yes | "`REL_COURSES` in `kit/verify.py`" → "`reliefs = true` in `courses/<id>/course.toml` (S-DEC4)" in both rows. |
| E2.3 root README "Known limits" | yes (root `README.md` line 43; the packet's "kit/README.md" is the root file, as the checker noted) | yes | The checker's text, with "(S-DEC4)", and P-DEC11 and P-DEC8 named. |
| S1 malformed record crashes | yes (`AttributeError`/`KeyError` path on `rec['global']`) | yes | The checker's code, widened: `_load` also catches `UnicodeDecodeError` and treats a non-dict top level as unreadable. The new mode is `full: <file> unreadable or malformed for edition <e>`. `self.unreadable` is set before the first `_load()`. `save()` now always gets a dict, so it repairs a corrupt file. Docstring: a missing, unreadable or malformed record gives a full run. |
| S2 kit/README.md | yes | yes | The `verify.py` row: the checker's sentence after the first, plus "a missing or malformed record" and the M4 sentence. New rows for `verify_scope.py` and `verify-hashes.json`. The line on adding a course: the checker's text. Prose only; manifest entry rehashed after the check showed it was the only change. |
| S3 filing docs | yes | yes | `docs/method.md` §7 step 6: the checker's text (not rendered into any page: the baseline shows no other change). `skills/file-unit` history step 7 and markdown step 1: the checker's parenthesis added after `python3 verify.py` (⚠ re-save to the account). decoupling §6: a new S-DEC4 notes block (keys `private`, `reliefs`, `verify_sample`; scope and M3 reading; timings; the What's new decision; edition results; proposed rows). §8 first bullet: the checker's text. Root README line 40: the `--edition` form of `private_terms.py` and `verify.py --edition`. |
| S4 record not in the tree | yes (`kit/verify-hashes.json` absent) | no (not this packet's) | The record is written by the main chat's single `cd kit && python3 verify.py --full` at the final HEAD. It must then be committed. Flagged with ⚠ in decoupling §6. |
| S5 silent skip and crash path | yes (`if SECOND:` has no else; `MDSUBS[0][0]` IndexError; `rp`/`DESK` None) | yes | `else: print('nav: no second history course in this edition; ...')` (seen in both edition runs). `TAB` falls back to `'home'` when there is no MDSUBS. After `DESK` is set: `if rp is None or DESK is None: fails.append('tablet and desktop: the edition holds no history course with reports 2.3, ... and no markdown course with a unit filed; their report checks have no page to open')`. I tested `rp`/`DESK` rather than the checker's `not (SECOND or LEAD or MDSUBS)`, because it also covers MDSUBS without a reading page. The tablet report block is under `if rp:` and the desktop DESK block under `if DESK:`, so the run fails with a reason instead of crashing. This edition shape was not exercised (none exists); the parse is checked and both edition runs pass. |
| M1 track id and copy in the engine | yes | no (not one line; changes build.py) | Proposed as P-DEC12. |
| M2 `PUBLIC` duplicates `private` | yes | yes | `private_terms.PUBLIC = tuple(c['id'] for c in COURSES if not c.get('private'))`, same four ids as before. verify.py's "both private and public" check is now always empty, so it was removed (2 lines). Docstrings of private_terms.py and courses.py updated. |
| M3 scope wider than the done-when's words; drawers | yes | recorded | Reading recorded in decoupling §6. The full run covering every course's drawer is proposed as P-DEC14. |
| M4 tool versions not hashed | yes | yes | One sentence in the `verify_scope.py` docstring and in the kit/README `verify.py` row. |
| M5 private terms on a mixed edition | yes | no (no mixed edition exists; more than one line) | Proposed as P-DEC13. |
| M6 P-DEC7 | yes (P-DEC7 is the closed skills re-save in CHANGELOG; agent 1's P-DEC7, the provenance footer link, was done by packet 4) | yes | Dropped; said so in decoupling §6. |

## Proposed rows: ids

Taken ids: P-DEC1 to P-DEC7, of which P-DEC7 is closed. The earlier reports' ids P-DEC8 (01-engine), P-DEC9, P-DEC10 and P-DEC11 (02-verify-names) are the next free ids already, so no renumbering was needed; only agent 1's P-DEC7 is dropped (done). New from this check: P-DEC12 (M1), P-DEC13 (M5), P-DEC14 (M3) and P-DEC15 (E1's per-edition scale). All eight rows are written under Proposed in `docs/BACKLOG.md` after P-DEC6, in the 4-column form of P-DEC4. P-DEC8 to P-DEC11 are copied word for word from the reports. The main chat should not add them again.

## Decisions taken

- I wrote the proposed rows into `docs/BACKLOG.md` because README and decoupling §6 now cite P-DEC8, P-DEC9, P-DEC11 and P-DEC12 to P-DEC15. I did not touch the S-DEC4 row itself, the CHANGELOG, site-log, the Project copies or the pick your adventure.
- decoupling §6: I appended "Done by S-DEC4 (20 Nov 2026)" to S-DEC0's S-DEC4 note and the `reliefs` outcome to S-DEC1's S-DEC4 note. That is how I read "the notes on S-DEC4 in §6 are now done". §8: an "S-DEC4 result" was added to both edition-verify bullets, giving today's passing runs.
- The marketing-ai and greece timings (6 m 24 s and 6 m 58 s) come from my probe runs, which ran alongside the main tree's baseline check and the other probe. They are slower than agent 2's 5 m 33 s and 5 m 48 s.

## Files changed

`kit/verify.py`, `kit/verify_scope.py`, `kit/private_terms.py`, `kit/courses.py` (docstring), `kit/README.md`, `kit/baseline.json` (README.md entry), `README.md`, `docs/method.md`, `docs/decoupling.md`, `docs/BACKLOG.md`, `skills/file-unit/SKILL.md`, `skills/new-course/SKILL.md`, and this report.

## For the main chat

- Run `cd kit && python3 verify.py --full` once at the final HEAD and commit the `kit/verify-hashes.json` it writes (S4).
- Re-save the account skills `file-unit` and `new-course` (both changed).
- Probe copies left: `/tmp/s-dec4-apply`, `/tmp/s-dec4-scope`; logs `/tmp/s-dec4-apply-*.log`, `/tmp/s-dec4-scope-ma.log`.
