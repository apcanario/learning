# Registration fixes · S-SCE0 · Supply Chain Execution for Product Teams

Applier: one isolated, fresh Opus 5.5 agent (claude-opus-5-5), 19 Nov 2026. Packet: `out/registration-check.md` (4 should-fix, 8 minor), `out/registration.md`, the clone at 82caee5, the seven originals in `/home/claude/scratch/sce` (read, not changed). Every change was an exact replacement whose count was checked before anything was written (dry run of all 21; the script stops on any count it does not expect): `/home/claude/scratch/apply/apply.py`. No brief, no line of the preamble, no `AIMS` line and nothing of another course changed. Nothing committed or pushed.

## Findings

### 1. Employer's product names missing, no row carries the gap (Should-fix): applied

Added row P-SCE11 (*proposed*, for Pedro, by hand) under Proposed in `docs/BACKLOG.md`, after P-SCE10, asking for the product names as `employer:` lines in `kit/private-terms.txt` before W-SCE6; says the course is gated only on the employer's own name until then. No term added or guessed. The registration record (`out/registration.md` (e) and Left undone) and the comment in `kit/private-terms.txt` now say so; the Reply of the template names P-SCE11 among Pedro's tasks.

- `docs/supply-chain-execution-prompts.md`, count 1 (findings 2,1)

  Old:

  ````
  P-SCE1, P-SCE6 and P-SCE7), repeated in every reply until he marks it done; then the next prompt in a code block.
  ````

  New:

  ````
  P-SCE1, P-SCE6, P-SCE7 and P-SCE11), repeated in every reply until he marks it done; then {NEXTPROMPT} in a code block.
  ````

- `docs/BACKLOG.md`, count 1 (finding 1)

  Old:

  ````
  | P-SCE10 | *Proposed (syllabus decision D12).* Each coming-soon course needs its own design chat on Fable before any row is queued for it; the listing promises a course, not a date. ⚠ A public page will name four courses that do not exist yet. The four are Supply Chain Planning for Product Teams, Warehouse Automation and Robotics, AI in Supply Chain Execution, and Last Mile and Omni-channel Fulfilment, listed in Academy as coming soon by S-SCE0; none has a data folder, a brief or a writing row. | A course is designed before it is queued (`new-course` skill) | One design chat per course, on Fable, each before any row of that course |
  ````

  New:

  ````
  | P-SCE10 | *Proposed (syllabus decision D12).* Each coming-soon course needs its own design chat on Fable before any row is queued for it; the listing promises a course, not a date. ⚠ A public page will name four courses that do not exist yet. The four are Supply Chain Planning for Product Teams, Warehouse Automation and Robotics, AI in Supply Chain Execution, and Last Mile and Omni-channel Fulfilment, listed in Academy as coming soon by S-SCE0; none has a data folder, a brief or a writing row. | A course is designed before it is queued (`new-course` skill) | One design chat per course, on Fable, each before any row of that course |
  | P-SCE11 | *Proposed, for Pedro, by hand.* Supply the employer's product names, each as its own `employer: <name>` line in `kit/private-terms.txt`. Until then this course is gated only on the employer's own name: `kit/private_terms.py` fails it outside a dated list, but no product name of the employer is checked. The names are not in the repo and no chat may guess them. ⚠ None on the build; until this row is closed, a unit could name one of the employer's products without the check failing. | S-SCE0's registration check (19 Nov 2026, finding 1): P-SCE2 and setup step (e) ask the check to fail on the employer's product names too | `kit/private-terms.txt`, before W-SCE6, the first unit that gives a vendor list |
  ````

- `kit/private-terms.txt`, count 1 (finding 1)

  Old:

  ````
  # held no product name of the employer on 19 Nov 2026: add each as its own "employer:" line.
  ````

  New:

  ````
  # held no product name of the employer on 19 Nov 2026: add each as its own "employer:" line.
  # Row P-SCE11 of docs/BACKLOG.md asks Pedro for them; until then the course is gated only on the employer's own name.
  ````

- `out/registration.md`, count 1 (finding 1)

  Old:

  ````
  - Product names of the employer in the private-terms list (none in the repo; see (e)).
  ````

  New:

  ````
  - Product names of the employer in the private-terms list (none in the repo; see (e)). Carried by row P-SCE11 of `docs/BACKLOG.md` (*proposed*, for Pedro, by hand; added by the registration check, finding 1): until Pedro supplies them, the course is gated only on the employer's own name.
  ````

- `out/registration.md`, count 1 (finding 1)

  Old:

  ````
  Each product name goes in as its own `employer:` line; until then the check guards only the employer's name.
  ````

  New:

  ````
  Each product name goes in as its own `employer:` line; until then the check guards only the employer's name. Row P-SCE11 of `docs/BACKLOG.md` asks Pedro for them (added by the registration check, finding 1).
  ````

### 2. W-DD-SCE2 step 11 and Reply contradict carry-forward point 7 (Should-fix): applied

Template step 11 ends with a new slot `{SAVE}` and the Reply with `{NEXTPROMPT}`; `kit/next_prompt.py` fills them: for every row with a next unit, exactly the old text ("`python3 kit/next_prompt.py --save` saves the prompt of <next>" / "the next prompt"); for the last row (W-DD-SCE2), the closing corrections prompt (every open Corrections row and open flag, worked under limits (a) to (f), added as row C-SCE in the Queue, `--save` not run, G-R-SCE left waiting) and "the closing corrections prompt (or the line saying nothing is open)". Only the SCE template uses the new slots: every PB, BW and SP prompt is byte-identical to 82caee5's (all rows compared).

- `docs/supply-chain-execution-prompts.md`, count 1 (finding 2)

  Old:

  ````
  `{PAGE}` (read-sce4), `{NEXT}`, `{FILED}`
  ````

  New:

  ````
  `{PAGE}` (read-sce4), `{NEXT}`, `{SAVE}` (step 11's last clause: the `--save` line, or on the last row the closing corrections prompt), `{NEXTPROMPT}` (the Reply's last item), `{FILED}`
  ````

- `docs/supply-chain-execution-prompts.md`, count 1 (findings 2,1)

  Old:

  ````
  P-SCE1, P-SCE6 and P-SCE7), repeated in every reply until he marks it done; then the next prompt in a code block.
  ````

  New:

  ````
  P-SCE1, P-SCE6, P-SCE7 and P-SCE11), repeated in every reply until he marks it done; then {NEXTPROMPT} in a code block.
  ````

- `docs/supply-chain-execution-prompts.md`, count 1 (findings 7,3,4,2,10)

  Old:

  ````
  so W-SCE6's paragraph is met by the script.
  ````

  New:

  ````
  so W-SCE6's paragraph is met by the script. The chat that closes P-SCE6 runs `python3 kit/next_prompt.py --row W-SCE7 --save`, so the prompt saved in W-SCE7's row loses that line. Corrected by S-SCE0's registration check (19 Nov 2026): (7) section 1's rules 11 and 12 now read as the template's; (8) the three sourcing rules of the sport-psychology bullets that section 1 did not restate (a title is the article's own; a figure cited to the paper that reports it; each Sources entry checked against the publisher's record) are rule 2's last sentence; (9) step 11: the course's data mirrors are refreshed only once they exist in the Project; (10) step 11 and the Reply: the last row, W-DD-SCE2, writes the closing corrections prompt of section 4, point 7, in place of a next prompt (slots `{SAVE}` and `{NEXTPROMPT}`, filled by `kit/next_prompt.py`); (11) the Reply names P-SCE11 among Pedro's tasks.
  ````

- `kit/next_prompt.py`, count 1 (finding 2)

  Old:

  ````
          'PARTICULAR': part[r['row']],
      }
  ````

  New:

  ````
          'PARTICULAR': part[r['row']],
          # registration check of S-SCE0 (19 Nov 2026): the last row writes a closing corrections prompt (prompts doc §4, point 7)
          'SAVE': f"`python3 kit/next_prompt.py --save` saves the prompt of {nx}" if nxt else
                  ("there is no next unit (the carry-forward rule, point 7): in place of a next unit's prompt, write a closing corrections prompt to the "
                   "standard of this one, listing every row still open in the Corrections section of `docs/BACKLOG.md` and every flag still open in "
                   f"`{pathlib.Path(c['data']).parent.as_posix()}/syllabus-flags.md`, each with its unit, the passage or flag, what is wrong and its "
                   "source, to be worked under the limits (a) to (f) of step 1b; add it as row C-" + r['sc']['key'] + " at the end of this course's "
                   "section of the Queue of `docs/BACKLOG.md`, the prompt in its prompt cell, and set the backlog's \"Next up\" line to it; do not run "
                   "`--save`; if nothing is open, say so and add no row. The course's reliefs, row G-R-" + r['sc']['key'] + ", wait for Pedro's confirmation"),
          'NEXTPROMPT': 'the next prompt' if nxt else 'the closing corrections prompt (or the line saying nothing is open)',
      }
  ````

### 3. §1 rules 11 and 12 still held the superseded wording (Should-fix): applied

§1 rules 11 and 12 replaced by the template's (rule 11's "the carry-forward rule above" read as "section 4" in §1), with a dated note after the list. The template's rules were already right and are unchanged; the line citing §1 now agrees with §1.

- `docs/supply-chain-execution-prompts.md`, count 1 (finding 3)

  Old:

  ````
  11. **Flags and corrections.** A contradiction with a filed unit or a brief, a mistake noticed in a filed unit, or a need the syllabus does not meet, is written to `out/flags.md` in the form of `syllabus-flags.md`, naming every unit it affects. It is carried by section 4. The writer never rewords a brief.
  ````

  New:

  ````
  11. **Flags and corrections.** A contradiction with a filed unit or a brief, a mistake noticed in a filed unit, or a need the syllabus does not meet, is written to `out/notes.md` (a contradiction or a mistake under **Contradictions**, a mistake with the quoted passage, what is wrong, the source and the exact replacement; a need under **Needs**), naming every unit it affects and with a proposed change, so that the filer writes it into `syllabus-flags.md` in that file's form. It is carried by section 4. The writer never rewords a brief.
  ````

- `docs/supply-chain-execution-prompts.md`, count 1 (finding 3)

  Old:

  ````
  12. **Hand-in.** The unit; `out/sources.md`; `out/flags.md`; the figures rendered; up to ten claims it is unsure of, closing with the `Object:` line; `out/stats.json`; a reply of six lines at most.
  ````

  New:

  ````
  12. **Hand-in.** The unit, `out/unit.md` (front matter, the unit, the deliverable, Sources); `out/sources.md`; `out/notes.md` with three lists, each item naming the unit codes it touches, an empty list written as "none": **Case facts** (rule 8), **Contradictions** and **Needs** (rule 11); the figures rendered; `out/unsure.md`, up to ten claims it is unsure of, closing with the `Object:` line; a reply of six lines at most (its model, the files it wrote, the counts of its lists, the number of references opened and not opened). `out/stats.json` is not the writer's: the chat writes it from these files with `python3 kit/thin.py stats`.
  
  Rule 2's last sentence, and rules 11 and 12 as they now read, were set by S-SCE0's registration check (19 Nov 2026, findings 3 and 10) to match the template below and the repo's thin chat: flags go to `out/notes.md`, which the filer reads, and `out/stats.json` is the chat's, written with `thin.py stats`. The template's rules are these.
  ````

- `docs/supply-chain-execution-prompts.md`, count 1 (findings 7,3,4,2,10)

  Old:

  ````
  so W-SCE6's paragraph is met by the script.
  ````

  New:

  ````
  so W-SCE6's paragraph is met by the script. The chat that closes P-SCE6 runs `python3 kit/next_prompt.py --row W-SCE7 --save`, so the prompt saved in W-SCE7's row loses that line. Corrected by S-SCE0's registration check (19 Nov 2026): (7) section 1's rules 11 and 12 now read as the template's; (8) the three sourcing rules of the sport-psychology bullets that section 1 did not restate (a title is the article's own; a figure cited to the paper that reports it; each Sources entry checked against the publisher's record) are rule 2's last sentence; (9) step 11: the course's data mirrors are refreshed only once they exist in the Project; (10) step 11 and the Reply: the last row, W-DD-SCE2, writes the closing corrections prompt of section 4, point 7, in place of a next prompt (slots `{SAVE}` and `{NEXTPROMPT}`, filled by `kit/next_prompt.py`); (11) the Reply names P-SCE11 among Pedro's tasks.
  ````

### 4. Step 11 refreshed Project mirrors that do not exist (Should-fix): applied

Step 11 now names the three data mirrors and refreshes them only once they exist: added by the row that files sport-psychology's last unit (W-DD-SP3), which deletes SP's, or by the first SCE row that finds them absent after that; none written while SP's are in the Project (method §8 step 4).

- `docs/supply-chain-execution-prompts.md`, count 1 (finding 4)

  Old:

  ````
  and the course's `hub.py` and `syllabus-flags.md` mirrors refreshed; `python3 kit/next_prompt.py --save` saves the prompt of {NEXT}.
  ````

  New:

  ````
  and the course's three data mirrors (`claude/supply-chain-execution-hub.py`, `claude/supply-chain-execution-units_data.py`, `claude/supply-chain-execution-syllabus-flags.md`) refreshed when this row changed them, but only once they exist: S-SCE0 did not add them while sport-psychology's were in the Project (`docs/method.md` §8 step 4); they are added by the row that files sport-psychology's last unit (W-DD-SP3), which deletes that course's, and a row of this course that finds them absent after that adds all three from their repo files (`project_write` with `local_path`); while sport-psychology's are still in the Project, none is written; {SAVE}.
  ````

- `docs/supply-chain-execution-prompts.md`, count 1 (findings 7,3,4,2,10)

  Old:

  ````
  so W-SCE6's paragraph is met by the script.
  ````

  New:

  ````
  so W-SCE6's paragraph is met by the script. The chat that closes P-SCE6 runs `python3 kit/next_prompt.py --row W-SCE7 --save`, so the prompt saved in W-SCE7's row loses that line. Corrected by S-SCE0's registration check (19 Nov 2026): (7) section 1's rules 11 and 12 now read as the template's; (8) the three sourcing rules of the sport-psychology bullets that section 1 did not restate (a title is the article's own; a figure cited to the paper that reports it; each Sources entry checked against the publisher's record) are rule 2's last sentence; (9) step 11: the course's data mirrors are refreshed only once they exist in the Project; (10) step 11 and the Reply: the last row, W-DD-SCE2, writes the closing corrections prompt of section 4, point 7, in place of a next prompt (slots `{SAVE}` and `{NEXTPROMPT}`, filled by `kit/next_prompt.py`); (11) the Reply names P-SCE11 among Pedro's tasks.
  ````

### 5. P-SCE4 record rewritten by Brindle→Varnby (Minor): applied

Dated note beside P-SCE4 in syllabus §9 (names Brindle; the syllabus is a private repo doc, not built into Academy) and a note in case-facts.md that does not name the real company (writers read that file; writer rule 5).

- `docs/supply-chain-execution-syllabus.md`, count 1 (finding 5)

  Old:

  ````
  replaces any that matches a real company in the field, in every file. ⚠ None.
  ````

  New:

  ````
  replaces any that matches a real company in the field, in every file. ⚠ None. (Note, S-SCE0, 19 Nov 2026: the fifth name as coined and searched was "Brindle Software"; it matched a real software maker and was replaced by "Varnby Software" in every file, this line included.)
  ````

- `generator/data/supply-chain-execution/case-facts.md`, count 1 (finding 5)

  Old:

  ````
  a name that matches a real company in logistics, retail, food or software is replaced before any unit is written.
  ````

  New:

  ````
  a name that matches a real company in logistics, retail, food or software is replaced before any unit is written. (S-SCE0, 19 Nov 2026: one coined name matched a real software maker and was replaced; the six above are the names after that search.)
  ````

### 6. "41 references checked for existence" overstated (Minor): applied

Counted from `bibliography.md`'s How-checked column: 26 Crossref, 6 Search, 5 Abstract (37 checked), 3 Secondhand (R4, A6, A7), 1 not opened (A8). Hub CHANGELOG v1 and `docs/courses-index.md` now say "41 references, 37 checked for existence (3 seen only secondhand, 1 not opened)". Rebuilt.

- `generator/data/supply-chain-execution/hub.py`, count 1 (finding 6)

  Old:

  ````
  a seed bibliography of 41 references checked for existence,
  ````

  New:

  ````
  a seed bibliography of 41 references, 37 checked for existence (3 seen only secondhand, 1 not opened),
  ````

- `docs/courses-index.md`, count 1 (finding 6)

  Old:

  ````
  a seed bibliography of 41 references checked for existence only
  ````

  New:

  ````
  a seed bibliography of 41 references, 37 checked for existence only (3 seen only secondhand, 1 not opened)
  ````

### 7. W-SCE7's saved prompt keeps the gate line (Minor): applied

The script already prints the line only while row P-SCE6 is in `docs/BACKLOG.md`; closed rows leave the file (to the changelog), so no code change. What persisted was the saved copy: P-SCE6's row (and the template's note) now say the chat that closes P-SCE6 moves it and runs `python3 kit/next_prompt.py --row W-SCE7 --save`. Proved both ways: with the row present the first line is "Do not run until Pedro has closed P-SCE6."; with the row removed (dummy edit) the prompt opens with "Clone `apcanario/learning`…"; BACKLOG restored from a copy (`cmp` equal) and the line is back; W-SCE6 never has it.

- `docs/supply-chain-execution-prompts.md`, count 1 (findings 7,3,4,2,10)

  Old:

  ````
  so W-SCE6's paragraph is met by the script.
  ````

  New:

  ````
  so W-SCE6's paragraph is met by the script. The chat that closes P-SCE6 runs `python3 kit/next_prompt.py --row W-SCE7 --save`, so the prompt saved in W-SCE7's row loses that line. Corrected by S-SCE0's registration check (19 Nov 2026): (7) section 1's rules 11 and 12 now read as the template's; (8) the three sourcing rules of the sport-psychology bullets that section 1 did not restate (a title is the article's own; a figure cited to the paper that reports it; each Sources entry checked against the publisher's record) are rule 2's last sentence; (9) step 11: the course's data mirrors are refreshed only once they exist in the Project; (10) step 11 and the Reply: the last row, W-DD-SCE2, writes the closing corrections prompt of section 4, point 7, in place of a next prompt (slots `{SAVE}` and `{NEXTPROMPT}`, filled by `kit/next_prompt.py`); (11) the Reply names P-SCE11 among Pedro's tasks.
  ````

- `docs/BACKLOG.md`, count 1 (finding 7)

  Old:

  ````
  W-SCE7 is not run until Pedro closes this row. |
  ````

  New:

  ````
  W-SCE7 is not run until Pedro closes this row. The chat that closes it moves it to `docs/CHANGELOG.md` and then runs `python3 kit/next_prompt.py --row W-SCE7 --save`, so the prompt saved in W-SCE7's row loses that first line. |
  ````

### 8. W-DD-SP3's step 11 no longer mentions G-R-SP (Minor): held

Held: the checker gives no fix and says nothing is lost (G-R-SP is still under Proposed); restoring it would change another course's printed prompt, which this applier must not do.

### 9. dated-list test is mechanical (Minor): applied

F1's proposed change in `syllabus-flags.md` gains a sentence telling the fresh checker, at pass 4, to confirm that every list the script exempts is a real analyst or filing list, copied whole. Printed in SCE6, 8, 9, 16 and 17's prompts.

- `generator/data/supply-chain-execution/syllabus-flags.md`, count 1 (finding 9)

  Old:

  ````
  raises a flag for the Project's owner. No brief changes.
  ````

  New:

  ````
  raises a flag for the Project's owner. The test is mechanical (any lead-in naming an analyst or a filing and a year opens a list): the fresh checker confirms, at pass 4, that every list in which the script lets the employer pass is a real analyst or filing list, copied whole. No brief changes.
  ````

### 10. three writer rules dropped (Minor): applied

Rule 2 (in §1 and in the template) gains one sentence: a title is the article's own; a figure cited to the paper that reports it; each Sources entry checked against the publisher's record before hand-in. Note (3)'s "which covers each" corrected.

- `docs/supply-chain-execution-prompts.md`, count 2 (finding 10)

  Old:

  ````
  A reference that could not be opened is listed as not opened and carries nothing.
  ````

  New:

  ````
  A reference that could not be opened is listed as not opened and carries nothing. A title is the article's own title, never a slug; a figure is cited to the paper that reports it, not to one that repeats it; each Sources entry is checked against the publisher's record before hand-in.
  ````

- `docs/supply-chain-execution-prompts.md`, count 1 (finding 10)

  Old:

  ````
  are replaced by section 1, which covers each;
  ````

  New:

  ````
  are replaced by section 1, which covers all but three of them (restored as rule 2's last sentence, item 8 below);
  ````

- `docs/supply-chain-execution-prompts.md`, count 1 (findings 7,3,4,2,10)

  Old:

  ````
  so W-SCE6's paragraph is met by the script.
  ````

  New:

  ````
  so W-SCE6's paragraph is met by the script. The chat that closes P-SCE6 runs `python3 kit/next_prompt.py --row W-SCE7 --save`, so the prompt saved in W-SCE7's row loses that line. Corrected by S-SCE0's registration check (19 Nov 2026): (7) section 1's rules 11 and 12 now read as the template's; (8) the three sourcing rules of the sport-psychology bullets that section 1 did not restate (a title is the article's own; a figure cited to the paper that reports it; each Sources entry checked against the publisher's record) are rule 2's last sentence; (9) step 11: the course's data mirrors are refreshed only once they exist in the Project; (10) step 11 and the Reply: the last row, W-DD-SCE2, writes the closing corrections prompt of section 4, point 7, in place of a next prompt (slots `{SAVE}` and `{NEXTPROMPT}`, filled by `kit/next_prompt.py`); (11) the Reply names P-SCE11 among Pedro's tasks.
  ````

### 11. registration.md says the file is untracked (Minor): applied

Preamble and the Created list corrected: tracked since checkpoint commit 82caee5.

- `out/registration.md`, count 1 (finding 11)

  Old:

  ````
  This file is at `out/registration.md` in the clone. The repo does not track `out/` and `.gitignore` does not ignore it: a `git add -A` would pick it up.
  ````

  New:

  ````
  This file is at `out/registration.md` in the clone. The repo does not track `out/` and `.gitignore` does not ignore it; the checkpoint commit 82caee5 added this file, so it is now tracked (corrected by the registration check, finding 11).
  ````

- `out/registration.md`, count 1 (finding 11)

  Old:

  ````
  `out/registration.md` (this file; untracked)
  ````

  New:

  ````
  `out/registration.md` (this file; tracked since the checkpoint commit 82caee5)
  ````

### 12. SCE not shown as a tile on the home page (Minor): held

Held: the existing G-0 rule, not a regression; the checker asks only for a look at the screenshots step, which is the main chat's.

## Checks after the changes

- `cd kit && python3 build.py`: "… Supply Chain Execution (public): 0/20 units · shell 547 KB, 266 fetched files, site 23.60 MB".
- `python3 verify.py`: last line "ALL CHECKS PASSED", exit 0, no FAIL line (about 28 minutes).
- `python3 index_check.py`: "courses-index.md matches the sources".
- `python3 private_terms.py`: "105 files, 0 private terms, 114 warnings: OK".
- `python3 kit/next_prompt.py --row W-SCE1` (3,137 words) and `--row W-SCE2` (3,117 words) print with no unfilled slot; W-SCE1's holds rule 2's new sentence, rules 11 and 12 identical to §1's, the mirror clause, the `--save` line naming W-SCE2 and P-SCE11. `--row W-DD-SCE2` prints the closing-corrections clause and Reply. No `--save` was run.
- Every PB, BW and SP row's prompt from the changed `next_prompt.py` is byte-identical to 82caee5's (worktree of HEAD, removed afterwards).

## Round 2

Applier: one isolated, fresh Opus 5.5 agent (claude-opus-5-5), 19 Nov 2026. Packet: `out/registration-recheck.md` (1 should-fix, 4 minor), this file, the clone at 4d12203, the seven originals in `/home/claude/scratch/sce` (not changed). Seven exact replacements, every count checked in a dry run before any write (script stops on a mismatch): `/home/claude/scratch/apply2/apply.py`. No brief, no preamble line, nothing of another course changed. Nothing committed or pushed. All five findings applied; none held.

- `kit/next_prompt.py`, count 1 (should-fix 1)

  Old:

  ````
      slots = {
          'ROW':
  ````

  New:

  ````
      last = r['code'] == r['order'][-1]   # S-SCE0 registration recheck (19 Nov 2026): the last row of this course, not of the queue
      slots = {
          'ROW':
  ````

- `kit/next_prompt.py`, count 1 (should-fix 1)

  Old:

  ````
  'SAVE': f"`python3 kit/next_prompt.py --save` saves the prompt of {nx}" if nxt else
  ````

  New:

  ````
  'SAVE': f"`python3 kit/next_prompt.py --save` saves the prompt of {nx}" if not last else
  ````

- `kit/next_prompt.py`, count 1 (minor 2)

  Old:

  ````
  'NEXTPROMPT': 'the next prompt' if nxt else 'the closing corrections prompt (or the line saying nothing is open)',
  ````

  New:

  ````
  'NEXTPROMPT': 'the next prompt' if not last else 'the closing corrections prompt (or the line saying nothing is open)',
          'SAVEROW': 'save the next prompt in its row (step 11)' if not last else 'add the closing corrections row, if any, as step 11 says',
  ````

- `docs/supply-chain-execution-prompts.md`, count 1 (minor 2)

  Old:

  ````
  from Next to Done and save the next prompt in its row (step 11), so the published
  ````

  New:

  ````
  from Next to Done and {SAVEROW}, so the published
  ````

- `docs/supply-chain-execution-prompts.md`, count 1 (minor 3)

  Old:

  ````
  they are added by the row that files sport-psychology's last unit (W-DD-SP3), which deletes that course's, and a row of this course
  ````

  New:

  ````
  the Project holds the data mirrors only of the course being written, and the row that files that course's last unit deletes them, so this course's are added by the row that files the last unit of whichever course is being written when they are due; a row of this course
  ````

- `docs/supply-chain-execution-prompts.md`, count 1 (minor 4, minor 2)

  Old:

  ````
  `{PAGE}` (read-sce4), `{NEXT}`, `{SAVE}` (step 11's last clause: the `--save` line, or on the last row the closing corrections prompt), `{NEXTPROMPT}` (the Reply's last item),
  ````

  New:

  ````
  `{PAGE}` (read-sce4), `{SAVE}` (step 11's last clause: the `--save` line, or on the last row the closing corrections prompt), `{SAVEROW}` (step 10's clause on the next prompt), `{NEXTPROMPT}` (the Reply's last item),
  ````

- `out/registration.md`, count 1 (minor 5)

  Old:

  ````
  The repo does not track `out/` and `.gitignore` does not ignore it; the checkpoint commit 82caee5 added this file, so it is now tracked
  ````

  New:

  ````
  `out/` is not ignored by `.gitignore`; the checkpoint commit 82caee5 added this file, so it is tracked
  ````

Notes:
- Should-fix 1: `SAVE` and `NEXTPROMPT` now key on `last = r['code'] == r['order'][-1]` (the course's own last ORDER row), not on `nxt`. `NEXT` is unchanged (sport-psychology's template reads it; W-DD-SP3's prompt must stay as it is). Proof, in memory only (no file changed, nothing to revert, no `--save`): a dummy row W-ZZ1 of personal-brand appended after W-DD-SCE2 becomes its `nxt`; W-DD-SCE2's prompt still carries the closing corrections clause, no "saves the prompt of", no W-ZZ1, and is identical to its prompt without the dummy.
- Minor 2: step 10 now reads `{SAVEROW}`: "save the next prompt in its row (step 11)" on every row but the last (text unchanged there); on W-DD-SCE2, "add the closing corrections row, if any, as step 11 says".
- Minor 3: the mirror clause no longer says W-DD-SP3 adds this course's mirrors; it states the §8 step 4 rule (the Project holds only the data mirrors of the course being written; the row filing that course's last unit deletes them) and that this course's are added by the row that files the last unit of whichever course is being written when they are due. W-DD-SP3's prompt is unchanged.
- Minor 4: `{NEXT}` was read by nothing in this course's template (only the Slots line named it), so it is dropped from the SCE Slots line; the `NEXT` key in `next_prompt.py` stays, read by sport-psychology's template.
- Minor 5: the opening sentence of `out/registration.md` corrected as the recheck proposed.

Checks after Round 2:
- `python3 build.py`: last line ends "site 23.60 MB" (Supply Chain Execution (public): 0/20 units).
- `python3 verify.py`: last line "ALL CHECKS PASSED", exit 0, no FAIL line.
- `python3 index_check.py`: "courses-index.md matches the sources".
- `python3 private_terms.py`: "105 files, 0 private terms, 114 warnings: OK".
- `python3 kit/next_prompt.py --row` W-SCE1 (3,166 words), W-SCE2 (3,146), W-DD-SCE2 (3,260): no unfilled slot; W-SCE1 and W-SCE2 save the next prompt in their row and name W-SCE2 / W-SCE3 in `--save`; W-DD-SCE2 never says to save the next prompt. No `--save` run.
- All 38 PB, BW and SP rows' prompts byte-identical to HEAD 4d12203's (sha256, worktree of HEAD, removed afterwards).
