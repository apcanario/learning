# Registration check · S-SCE0 · Supply Chain Execution for Product Teams

Checker: one isolated, fresh Opus 5.5 agent (claude-opus-5-5), 19 Nov 2026. It did not see the registrar's work. Packet: the seven files in `/home/claude/scratch/sce`, `out/registration.md`, the clone at `82caee5` (baseline `382fee3`). Nothing in the repo was edited or committed apart from this file. Scratch work, outside the repo: `/home/claude/scratch/chk/`. That covers a worktree of `382fee3` (removed afterwards), a copy of the repo for planted-term tests, and a clean copy rebuilt with `build.py`.

**Verdict: no errors. 4 should-fix, 8 minor.** Every item on the check list passes, with the exceptions below.

## What was checked and passed

- **units_data.py.** `diff` of the zip's file against the repo's file shows one changed line, line 128 (SCE17's brief), where "Brindle Software" became "Varnby Software". Nothing else differs. The counts are right: the zip held 1 "Brindle" in units_data.py, 4 in case-facts.md, 2 in syllabus.md, 1 in prompts.md and 1 in setup-prompt.md, 9 in all, and "Brindle" now appears nowhere in the repo except `out/registration.md`. case-facts.md differs from the zip only by those 4 replacements. bibliography.md is identical to the zip's.
- **hub.py against syllabus.md.**
  - The title matches.
  - The goal is §3 word for word, apart from a lower-case first letter, which is the convention in sport-psychology's hub.
  - The three outcomes are word for word, with the units that deliver them.
  - `ORDER` runs SCE1 to SCE18, then DD-SCE1 and DD-SCE2.
  - Search is on for exactly SCE1, SCE6, SCE8, SCE9, SCE11, SCE12, SCE16, SCE17 and DD-SCE1.
  - `FRAME` is §1 word for word.
- **Coming soon.**
  - `THEMES['supply-chain']['planned']` holds the four courses in the file's order.
  - Checked by script against track-coming-soon.md, each title, scope line and teaser (the `planned_label` plus the tuple's last field) is word for word.
  - The built `kit/academy/index.html` (`#planned-supply-chain`) contains all three texts for each course.
  - None of the four has a data folder, a vault folder, a `QUEUE` entry or a writing row. Their names appear only in P-SCE10.
- **Part 8.** All 22 checklist lines of `docs/sourcing-standard.md` Part 8 equal syllabus §6's (Brindle→Varnby applied). The opening line of the file was extended.
- **method.md §9.**
  - It holds the carry-forward rule, all seven points of prompts.md §4 with the names made general.
  - It holds every clause of the source-credibility floor: opened before cited and logged with address, what was read and date; a short seed bibliography checked against Crossref or the publisher before the first unit, never an authority; a grade on every claim, from the first unit's key; the six kinds of non-source; interested parties labelled; fewer sources read in full; unsourced said or left out; the fresh checker verifying every record and every cited claim.
  - `skills/new-course/SKILL.md` §4b points to it.
- **Briefs.** All 20 open with their code and title. The 18 core units use "Unit SCEn, <title>." and the two deep dives "Deep dive SCEn, <title>.", which is the repo's deep-dive form (as in "Deep dive SP1, …"). All 20 end with the Deliverable clause.
- **Queue and backlog.**
  - `next_prompt.py --list` gives W-SCE1 … W-SCE18, W-DD-SCE1, W-DD-SCE2 after W-DD-SP3.
  - `docs/BACKLOG.md` §4d has the 20 rows in order, each with 4 cells. W-SCE6 and W-SCE7 carry the gate.
  - Under Proposed: P-SCE1, P-SCE6, P-SCE7 (marked for Pedro by hand), G-R-SCE and P-SCE10.
- **W-SCE1's prompt** (`--row W-SCE1`, not saved):
  - Writer rules 1–10, the seven passes, the row's paragraph and the carry-forward rule are all word for word from prompts.md, with Varnby.
  - Rules 11 and 12 are the disclosed adaptations.
  - There is no unfilled slot and no leftover SP, sport, coach, athlete, safety, 5b or Part 7 (also scanned on W-SCE6, W-SCE9 and W-DD-SCE2).
  - The 20 paragraphs and search flags in the template's table equal §3's.
  - W-SCE7's prompt opens with "Do not run until Pedro has closed P-SCE6."; W-SCE6's does not.
  - Planted test in a scratch copy: a correction and a flag naming SCE2 are both printed in W-SCE2's prompt (with the limits (a) to (f)), and the flag is not printed in W-SCE3's.
- **No owner, employer or product.** The course's data folder, its two docs and its built pages under `kit/academy/supply-chain-execution-sce/`, plus its panels and track section in `index.html`, were grepped for Pedro, Canário/Canario, Infios, Körber, HighJump, MercuryGate, K.Motion, ToolsGroup, Porto and Braga.
  - The only hits are "Pedro" in `docs/supply-chain-execution-syllabus.md` and `-prompts.md`. These are private repo docs, as with sport-psychology's.
  - `built.html` links the repo by handle, which is excluded by P24, as on every course.
  - No employer list exists in the course yet, so there is nothing for the dated-list exception to apply to.
- **private_terms.py on other courses.**
  - Full scan with the old script (worktree of `382fee3`) and the new one: the hits and the 114 warnings are identical once the SCE files are set aside (97 against 105 files).
  - Planted test: "Infios", "ToolsGroup" and "Pedro" were added, in a dated list, a sentence and a table, to an SP vault unit, PB's hub.py, the site log and SCE's case-facts.md. Old and new scripts give identical hits on the three non-SCE files.
  - On the SCE file, Infios inside the dated list passes; Infios in a sentence, and in a table after an undated lead-in, fails; ToolsGroup and Pedro fail even inside the list.
  - The same planted Markdown run through `mdcourse.render_md` gives HTML whose `dated_lines` behave the same way.
- **thin.py.**
  - `stage writer|checker|applier|filer` was run for W-DD-SP3 and W-SP2 with the old script on the old tree and the new script on the new tree, on the same dummy inputs. The packets are identical, apart from the opening line of `sourcing-standard.md`, which comes from the docs change, not from thin.py.
  - All four stages work for W-SCE1:
    - `sourcing-standard.md` holds the opening, Part 1 and Part 8 only.
    - `brief.txt` holds the preamble, then Aim, Takes and Gives, then the brief.
    - Filer rule 5 reads "| <code> | <operation> | <fact> |".
    - `index-rows.txt` holds the SCE section.
- **Other kit changes.**
  - Old and new `next_prompt.py` give byte-identical prompts for every PB, BW and SP row except W-DD-SP3, whose step 11 now names W-SCE1.
  - `build.py` changes nothing for History or Sports (`planned_heading` is unset there).
  - A clean copy of `82caee5` rebuilt with `build.py` reproduces `kit/academy/` byte for byte.
  - `index_check.py` prints "courses-index.md matches the sources".
  - `verify.py` was not re-run (about 22 minutes), and no screenshots were taken.
- **Prompts doc.** Rule 13 is kept: `quality_text` is generic and points to "step 4's seven passes". Step 5b and every mention of the safety reader are gone from the template. `doc_parts` accepts a prompts document with no safety block.
- **courses-index.md.** "## Supply Chain Execution (public)" is in SP's form, with 20 rows, "0 of 20 written", the search flags and the vault paths. "## Courses to come (Supply Chain)" is present.

## Findings

### Should-fix

1. **kit/private-terms.txt / docs/BACKLOG.md: the employer's product names are missing, and no row carries the gap.**
   - Quote (private-terms.txt): "The repo held no product name of the employer on 19 Nov 2026: add each as its own "employer:" line."
   - Quote (registration.md, Left undone): "Product names of the employer in the private-terms list (none in the repo; see (e))."
   - What is wrong: P-SCE2 and step (e) require the check to fail on the employer's product names. Only "Infios" is guarded. The gap is recorded only in the report and in a comment, with no backlog row, Corrections line or proposal for Pedro to supply the names. Setup-prompt step 7 says "Nothing found is left only in a report", and the Project rule says nothing is done that is not a backlog row.
   - Fix: add a proposed row, for Pedro by hand, to supply the product names as `employer:` lines before W-SCE6, the first unit that gives a vendor list.
2. **docs/supply-chain-execution-prompts.md, template step 11 and Reply, as printed for W-DD-SCE2: the last row does not deliver the closing prompt that §4 point 7 requires.**
   - Quote: "`python3 kit/next_prompt.py --save` saves the prompt of the next row in the Queue of `docs/BACKLOG.md` (no unit of this course is left; its reliefs, row G-R-SCE, wait for Pedro's confirmation)." and "…then the next prompt in a code block."
   - What is wrong: §4 point 7, which is printed in the same prompt, says "The last row (W-DD-SCE2) delivers a closing corrections prompt in place of a next unit's, listing every correction and flag still open." Neither the template nor `next_prompt.py` produces a closing corrections prompt, so the last row is told two different things.
   - Fix: give W-DD-SCE2's step 11 and Reply the closing-corrections wording, or add a mode to `next_prompt.py` that prints such a prompt.
3. **docs/supply-chain-execution-prompts.md §1, rules 11 and 12: the old wording still stands in §1, while the printed prompt corrects it and cites §1 as the source.**
   - Quote (§1, unchanged): "is written to `out/flags.md` in the form of `syllabus-flags.md`" and "`out/flags.md`; … `out/stats.json`".
   - Quote (printed prompt): "The writer rules of this course (`docs/supply-chain-execution-prompts.md` §1)", followed by rules that send flags to `out/notes.md` and take `stats.json` from the writer.
   - What is wrong: the correction lives only in the template copy and its note. Anyone who opens §1, such as a later syllabus review or a corrections checker given "the syllabus", reads the superseded rules. Carry-forward point 5 asks for the rule to be corrected in the prompts document itself.
   - Fix: apply the two corrected rules in §1 as well, with a dated note, or point the template line at the template's own rule list rather than at §1.
4. **docs/supply-chain-execution-prompts.md, template step 11 ("the course's `hub.py` and `syllabus-flags.md` mirrors refreshed"): the step assumes Project mirrors that do not exist yet.**
   - What is wrong: setup-prompt step 6 tells S-SCE0 not to add this course's data mirrors while another course's mirrors are in the Project (sport-psychology's are). W-SCE1's prompt says to refresh mirrors that do not exist, and no row is told to create them or to retire SP's.
   - Fix: give W-SCE1's step 11 one line: create the SCE mirrors (hub.py, units_data.py, syllabus-flags.md) if they are absent, and remove SP's if W-DD-SP3 has filed SP's last unit.

### Minor

5. **docs/supply-chain-execution-syllabus.md §9 and case-facts.md line 11: the Brindle→Varnby replacement rewrote what the record says was searched.**
   - Quote: "P-SCE4. The setup row searches the six coined names (Corvane, Ostrel, Tandric, Halvern, Varnby, Kestrow)…"
   - What is wrong: the name actually searched was Brindle. The blanket replacement turned the design chat's record into a statement that is not true.
   - Fix: none required, since the instruction asked for replacement "in every file", but a note beside P-SCE4 would keep the record straight.
6. **generator/data/supply-chain-execution/hub.py (CHANGELOG v1) and docs/courses-index.md: the public changelog overstates the bibliography check.**
   - Quote: "a seed bibliography of 41 references checked for existence".
   - What is wrong: the bibliography marks 3 entries "Secondhand" (A6, A7 and one more). B5's handbook title and volume are "from memory". Syllabus §10 says one entry was "not opened".
   - Fix: "41 references, 38 checked for existence (3 seen secondhand)", or similar.
7. **kit/next_prompt.py `GATES`: W-SCE7's saved prompt keeps the gate line after the gate closes.**
   - What is wrong: W-SCE6 saves W-SCE7's prompt while P-SCE6 is open, so the saved prompt opens with "Do not run until Pedro has closed P-SCE6." When Pedro closes P-SCE6, nothing re-saves W-SCE7's prompt, and the line stays in the saved copy.
   - Fix: one line in P-SCE6's row, such as "on closing, re-run `next_prompt.py --row W-SCE7 --save`".
8. **W-DD-SP3's printed prompt, step 11: the reminder that SP's reliefs wait has gone.**
   - Quote (before): "…(no unit of this course is left; its reliefs, row G-R-SP, wait for Pedro's confirmation)."
   - Quote (now): "saves the prompt of W-SCE1 (unit SCE1)."
   - What is wrong: the change follows from the queue and is correct. Its side effect is that the SP course's last row no longer mentions G-R-SP. Row G-R-SP itself is still under Proposed, so nothing is lost from the backlog.
9. **kit/private_terms.py `dated_lines`: the dated-list test is purely mechanical.**
   - What is wrong: any lead-in line holding "analyst" (or "filing", "annual report" and the like) and a year opens an exempt list. Example: "Infios, the analyst favourite of 2026:" followed by bullets about it passes.
   - Fix: none needed now; the registrar disclosed it, and the fresh checker's pass 4 is the real guard. Worth a line in F1 telling the fresh checker to confirm that every list in which the script exempts the employer is a real analyst or filing list, copied whole.
10. **Template step 3 (writer): the replacement of SP's writer bullets dropped three rules that §1 does not restate.**
    - What is wrong: "covers each" overstates it. These three are lost:
      - "A title is the article's own title, never a slug."
      - "A figure is cited to the paper that reports it, not to one that repeats it."
      - "Each Sources entry is checked against the publisher's record before hand-in."
    - The rule on quotation marks survives in Part 1, which is in the writer's packet.
    - Fix: optional, add the three as one line under rule 2.
11. **out/registration.md (preamble): the report says the file is untracked, but commit 82caee5 includes it.**
    - Quote: "The repo does not track `out/` …"
    - What is wrong: the checkpoint commit added `out/registration.md`, so the statement is stale.
12. **Home page, Supply Chain track: the course itself does not show among the track's tiles.**
    - Quote (built count line): "1 course coming soon · 0 of 20 units · 4 more coming soon".
    - What is wrong: under G-0's existing rule, a course with nothing filed gets no tile. SCE is therefore not on the home page; it is reached only from the drawer. The four courses that come "after this course" show alone, under the same "coming soon" words. This is an existing rule, not a regression, but worth a look in the screenshots step.

## Not checked

- `verify.py` and `--shots`, so the hero ring at top centre (.50/.17 tall, .50/.13 wide), between Marketing and Technology, was not seen.
- The six name searches were not repeated.
- `next_prompt.py --save` was not run, as instructed.
