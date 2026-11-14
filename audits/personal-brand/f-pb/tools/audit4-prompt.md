# Audit 4, the final audit: course PB · Building a Personal Brand on Instagram and YouTube

Date: 14 November 2026. You are one fresh, isolated auditor. Your folder is `{FOLDER}`. Read only inside it; write only inside `{FOLDER}/out/`.

**First line of everything you write and of your final reply:** `Model: <your exact model ID>`. If your model is neither claude-fable-5-2 nor claude-fable-5-1, write that line to `out/audit.md`, change nothing else, and stop.

## What is in the folder
- `units/`: all twelve units as filed (PB1 to PB10, DD-PB1, DD-PB2). You never edit them.
- `briefs/`: each unit's brief (the shared preamble, which holds the reader persona and the course goal; the Aim, Takes and Gives lines; the unit brief).
- `course-goal-and-outcomes.md`: the course goal, its three outcomes, the intro and the preamble.
- `case-facts.md`: the register of invented facts about Mara Venn, the fictional running example.
- `sourcing-parts-1-and-5.md`: the sourcing standard, for reference.

## Rules
- Nothing in your context outside this folder is a source. No web: you check no source again (twelve separate auditors are checking sources tonight). Do not use WebSearch, WebFetch, any memory, past-chat, Projects, connector, Artifact or Agent tool, and no tool whose name starts with `mcp__`. Tools you use: Read, Write, Edit, Bash (for `grep`, `wc`, `python3` inside the folder).
- The owner is asleep. Never ask a question, never wait for an approval, never call a tool that waits for an answer. Where a choice is open, take the most reasonable reading, record it and go on.
- Write `out/audit.md` as you go (notes per unit first), so a restart loses little. If `out/` already holds working files from a lost run, resume from them and say so in the report.
- Do not fix the units; report.

## The task
Read all twelve units in full, in reading order (PB1 to PB10, then DD-PB1, DD-PB2). Then:
1. **The course against its goal.** For the goal and each of the three outcomes: which units deliver it, with what deliverable, and what is missing or thin. Each brief against its unit only where a gap bears on the goal.
2. **A read-through as the persona of the preamble.** Reading in order: where a unit assumes what an earlier one did not give (a term, a number, a tool, a decision); where two units disagree; where Mara's facts differ from the register or between units. Quote each.
3. **Contradictions between units**, each quoted from both sides with unit and section: numbers, thresholds, dates, rules, definitions, Mara's facts, pointers ("PB6 §3 shows...") that say something the target does not say.
4. **What a reader still cannot do at the end**, set against the goal and outcomes.

## Report (`out/audit.md`)
First line `Model: ...`. Then: findings by severity (error, should-fix, minor), each with an id `A4-n`, the units and sections, the quoted text from each side, the problem, and, where a text change settles it, an exact replacement: `Current` copied verbatim from the unit, occurring exactly once in that unit (check with `grep -c -F -- '<current>' units/<file>`; it must print 1 and sit on one line), and `Fix`. Where you cannot tell which side is right without a source, say so and give no replacement: it becomes a flag for a syllabus review. A finding that needs a brief changed is a flag too. Then the four sections above in prose and tables. Then **Verdict on the course**: does it deliver its goal as written; a verdict per unit only where it is REWRITE (with the sections named); what a reader still cannot do; one line for the changelog.

Also write:
- `out/errata.json`: a JSON list, one object per finding: `{"id": "A4-1", "unit": "PB6", "kind": "erratum" | "flag", "severity": "error" | "should-fix" | "minor", "section": "...", "current": "...", "fix": "...", "basis": "the other unit and section, or the register line, quoted", "figure": false}`; `current` and `fix` exact, empty strings for a flag. A finding that needs changes in two units is two objects.
- `out/stats.json`: `{"model": "...", "units_read": 12, "words_read": 0, "findings": {"error": 0, "should-fix": 0, "minor": 0}, "errata": 0, "flags": 0, "contradictions": 0, "verdict": "one line"}`.
- `out/DONE`: written last, one line with the verdict, only when both JSON files parse and every erratum's Current has been counted once.

Your final reply is `out/audit.md` verbatim, nothing before its `Model:` line and nothing after the report.
