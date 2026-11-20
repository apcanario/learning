# Common rules for every S-DEC4 agent (row S-DEC4, docs/decoupling.md §6)

You are a fresh Opus 5.5 agent. Repo: /home/claude/learning (branch main, already cloned; do not clone, push or commit: the main chat commits).
Read first: docs/decoupling.md (§1 to §8, the notes on the rows in §6), kit/baseline.py docstring. Your packet below names the rest.

Rules
- Before any change: `python3 kit/baseline.py --check` must print `baseline: clean`. If not, stop and say so.
- After every step that moves data or touches kit/*.py that builds output: `python3 kit/baseline.py --check` prints `baseline: clean` again (academy and greece byte-identical to kit/baseline.json), unless your packet lists an expected difference; then list it first, and fail on any other.
- Do not run the unit workflow, file or publish any unit. Do not publish Academy, deploy Pages or republish the greece artifact. Do not run kit/deploy.sh without --dry-run.
- If the session's permission check refuses to run a repo script, stop at once and say so in one line. Never work around it.
- Where a choice is open, take the most reasonable reading, record it in your report and carry on. Ask only if genuinely blocked.
- Briefs, units and the vault's unit files are never changed.
- Write your full output (what you changed and why, every decision, every check result with its last line, timings) to the report file named in your packet. Your reply to the main chat is SIX LINES AT MOST: verdict, files changed, check results, the report path.
- Probe copies of the repo for destructive or slow experiments go under a literal /tmp path (cp -r the repo), never in the main tree.
