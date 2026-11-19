# Registration recheck · S-SCE0 · the applier's fixes

Checker: one isolated, fresh Opus 5.5 agent (claude-opus-5-5), 19 Nov 2026. It did not see the earlier work. Scope: the changed items only (`git diff 82caee5..HEAD`, HEAD 4d12203), against `out/registration-check.md` and `out/registration-fixes.md`. Nothing in the repo was edited or committed apart from this file. Scratch work, outside the repo: `/home/claude/scratch/rechk/` (worktrees of 82caee5, 382fee3 and HEAD, all removed afterwards).

**Verdict: no errors. 1 should-fix, 4 minor.**

## What was checked and passed

- **Every fix against its finding.**
  - Finding 1: P-SCE11 is added under Proposed, for Pedro by hand. It names no product, says no chat may guess one, and gives the gap and its ⚠. `private-terms.txt` gains a comment only and no term. The Reply lists P-SCE11 among Pedro's tasks.
  - Finding 3: §1 rules 11 and 12 now equal the template's, with a dated note (rule 11's "section 4" stands where the template has "the carry-forward rule above", which is correct for §1).
  - Finding 4: step 11 names the three mirrors and limits them to when they exist.
  - Finding 5: dated notes are added. The syllabus note names Brindle; it is a private doc and is not built (no "Brindle" anywhere under `kit/academy/`). The case-facts note does not name it.
  - Finding 6: the bibliography's Checked column gives 26 Crossref, 6 Search, 5 Abstract, 3 Secondhand (R4, A6, A7) and 1 not opened (A8), which is 41. "37 checked … (3 seen only secondhand, 1 not opened)" is right. The built `index.html` differs from 82caee5 only by that text.
  - Finding 7: a line in P-SCE6's row and in the template note.
  - Finding 9: one sentence in F1's proposed change.
  - Finding 10: one sentence in rule 2, in §1 and in the template. Note (3) is corrected.
  - Finding 11: the preamble and the Created list are corrected.
  - No change goes beyond its finding, apart from the minor items below.
- **Held findings.**
  - Finding 8 is held for a sound reason. It concerns sport-psychology's printed prompt, not this course's. Row G-R-SP is still under Proposed. W-DD-SP3's Reply still lists every proposal with its ⚠. Restoring the clause would change another course's prompt. It bears on no SCE prompt or guideline, so it need not go into `docs/supply-chain-execution-prompts.md`.
  - Finding 12 is held for a sound reason: G-0's existing rule, a screenshot matter for the main chat.
- **Other courses' prompts.** Every row's prompt was printed with `--row` (never `--save`) at 82caee5 (worktree) and at HEAD. All 38 PB, BW and SP rows are byte-identical. All 20 SCE rows differ only by these changes:
  - rule 2's new sentence;
  - the mirror clause;
  - P-SCE11 in the Reply;
  - on W-DD-SCE2, the closing corrections clause and "the closing corrections prompt (or the line saying nothing is open)".
  - No SCE prompt has an unfilled slot.
- **W-DD-SCE2.** Step 11 and the Reply now agree with §4 point 7 (every correction and flag still open, in place of a next unit's prompt, G-R-SCE left waiting).
- **Gate.** In a scratch worktree of HEAD:
  - W-SCE7's prompt opens with "Do not run until Pedro has closed P-SCE6." while P-SCE6's row is in `docs/BACKLOG.md`.
  - With the row deleted, the prompt opens with "Clone …".
  - W-SCE1, W-SCE6, W-SCE8 and W-DD-SCE2 never open with it. W-SCE6 has it only inside its paragraph, as intended.
- **P-SCE11.** It reads correctly and names no product of the employer. No employer term was added to any file. Every added line holding an employer or owner term is in `out/` reports.
- **Scripts at HEAD.**
  - `python3 kit/private_terms.py`: "105 files, 0 private terms, 114 warnings: OK".
  - `python3 kit/index_check.py`: "courses-index.md matches the sources".
  - `cd kit && python3 verify.py`: "ALL CHECKS PASSED", exit 0, no FAIL line.
  - The working tree was clean afterwards, apart from this file.

## Findings

### Should-fix

1. **kit/next_prompt.py, the `SAVE` and `NEXTPROMPT` slots: the closing corrections prompt depends on the queue's end, not the course's.**
   - Quote: `'SAVE': f"… saves the prompt of {nx}" if nxt else (… closing corrections prompt …)`. `nxt` is `next((r for r in rs[k + 1:] if r['code'] not in r['filed']), None)` over every public row of every course (W-DD-SP3's `nxt` is W-SCE1).
   - What is wrong: W-DD-SCE2 gets the closing corrections prompt only because no course is queued after SCE today. Once any later course is registered (P-SCE10 names four), W-DD-SCE2 would silently print "`--save` saves the prompt of <other course's first row>" and "the next prompt". That again contradicts §4 point 7, which is printed in the same prompt.
   - Fix: key the branch on the course, for example `nxt and nxt['c'] is c` (or `r['row'] == the course's last ORDER row`). On the last row, the closing-corrections clause can then be followed by the `--save` line for the next course's row, if there is one.

### Minor

2. **docs/supply-chain-execution-prompts.md, template step 10, as printed for W-DD-SCE2.**
   - Quote: "…and save the next prompt in its row (step 11)".
   - What is wrong: on the last row, step 11 now says to add row C-SCE with the closing prompt and not to run `--save`. Step 10 still says to save the next prompt in "its row".
   - Fix: make step 10 read "…save the next prompt (or, on the last row, the closing corrections row C-SCE) as step 11 says", or leave it. Step 11 is specific enough to govern.
3. **docs/supply-chain-execution-prompts.md, template step 11 (mirror clause): "they are added by the row that files sport-psychology's last unit (W-DD-SP3), which deletes that course's".**
   - What is wrong: W-DD-SP3's printed prompt deletes SP's mirrors (through method §8 step 4) but says nothing of adding SCE's. The fallback in the same sentence, "a row of this course that finds them absent after that adds all three", means W-SCE1 adds them, so nothing is lost, but the first half states something no prompt instructs.
   - Fix: "SP's are deleted by the row that files sport-psychology's last unit (W-DD-SP3); the first row of this course that finds this course's absent after that adds all three…".
4. **docs/supply-chain-execution-prompts.md, the Slots line: `{NEXT}` is still listed, but the template no longer uses it.** Step 11's clause is now `{SAVE}`. `NEXT`'s no-next text in `next_prompt.py` is dead for this course. Fix: drop `{NEXT}` from the slots list, or note "(used only inside `{SAVE}`)".
5. **out/registration.md, preamble (finding 11's fix).**
   - Quote: "The repo does not track `out/` and `.gitignore` does not ignore it; the checkpoint commit 82caee5 added this file, so it is now tracked".
   - What is wrong: the sentence says `out/` is untracked and that the file is tracked.
   - Fix: "`out/` is not ignored by `.gitignore`; the checkpoint commit 82caee5 added this file, so it is tracked."

## Not checked

- `verify.py --shots` and screenshots.
- `--save` and `--bundle`.
