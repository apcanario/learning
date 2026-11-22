Clone apcanario/learning (shallow, push access).

Row S-PROMPT1 · Bring every course's prompts to one plan: a plain clone line, bundles of four, one starter line per course. Thin main chat on Sonnet 5.5; every agent a fresh Opus 5.5 agent on a packet. Unattended: never ask; take the most reasonable reading and record it. Kit and docs only: no unit is opened, written or changed, and nothing is published.

BEFORE ANYTHING
1. Run `python3 kit/land.py start S-PROMPT1`. If another row is unpushed or mid-run on the repo, stop and say which.
2. Add this row to docs/BACKLOG.md (Pedro, 21 Nov 2026: as many units a chat as is reasonable, as little by hand as possible, a plain clone line in every session).
3. Before any edit, save what `python3 kit/next_prompt.py --row <row>` prints for the first unfiled row of every course in QUEUE that has one, to a folder outside the repo.

WHAT TO CHANGE (one Opus 5.5 agent makes the changes; a second, which has not seen the first, checks them)
A. The clone line. In kit/next_prompt.py and in every docs/*-prompts.md, the sentence that begins "Clone `apcanario/learning` (attach it with add_repo" is replaced by exactly `Clone apcanario/learning (shallow, push access).` and nothing else is said about cloning, attaching the repo or approval. That line is the first line of everything the script prints, a bundle's preface included. The rest of that paragraph (kit/land.py start and what follows) is unchanged.
B. `--course <id>`: start at that course's first unit not filed, in place of the whole queue's. With no unit left, exit saying so.
C. Bundles name their course. In the `--bundle` tail, the next prompt is the course's starter line (D), never a bare `--bundle <n>` that could pick another course's row.
D. The starter line, one per course, printed by a new `--starter <id>` and used by C:
   Clone apcanario/learning (shallow, push access).
   <Course name>, next bundle. Thin main chat on Sonnet 5.5; every agent a fresh Opus 5.5 agent. Run `python3 kit/next_prompt.py --course <id> --bundle 4` and work what it prints in full, unattended.
   A bundle's one reply ends with this line in a code block, not with a long prompt, unless a stop left something only Pedro can decide.
E. Gates become boundaries. A bundle stops before a row in GATES or HOLDS. For a GATES row, Pedro pasting the starter line is his go: the chat that starts there moves the gate row (P-SCE6 for W-SCE7) to the changelog as "closed by Pedro starting the chat" and removes the "not to be run" line. HOLDS rows (a review that must run first) keep working as they do.
F. docs/BACKLOG.md: in every prompt still waiting, the clone sentence replaced as in A. For each course with unfiled units, its writing rows grouped in fours from the first unfiled unit, the first row of each group holding the starter line in its prompt cell and the others "runs in the chat of <first row>".
G. docs/method.md §4 and §8 step 5: one paragraph saying what A to F now do. Refresh the Project copy.

CHECKS (scripts and the second agent, not the chat)
- Each prompt saved at step 3, printed again, differs only in its clone line. Save the diff.
- `grep -c add_repo kit/next_prompt.py docs/*-prompts.md` prints 0 for each.
- `python3 kit/next_prompt.py --course supply-chain-execution --bundle 4` prints the next four unfiled Execution rows and its first line is the clone line; `--list` is unchanged.
- `cd kit && python3 verify.py` passes (a scoped run is enough: no page changed).

CLOSE by method.md §8: changelog (date, S-PROMPT1, models, one-line result, commit), the Project copies of the backlog and changelog, `kit/land.py land`. No publish.

THE REPLY
What changed, file by file; the saved diffs' one-line summary; anything left for Pedro by hand (expected: nothing); then, in one code block each, the starter line of every course with unfiled units.
