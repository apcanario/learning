---
kind: corrections-check
row: W-BW9
course: building-with-ai
date: 2026-11-16
model: claude-opus-5-5
units: [BW8, BW9]
chat: https://claude.ai/code/session_01KMmgQy4zywM5ERbdfFcK6a
---

Second round. The checker's report, verbatim from its reply (the harness refused it a report file), saved before any change was applied.

Model: claude-opus-5-5 (Opus 5.5)

I could not write `/home/claude/w-bw9/corr2/out/report.md`: the write was refused ("Subagents should return findings as text"). The full report is below, in the parse format.

# Corrections check, second round, row W-BW9 (items 3 and 4)

Pages read on 16 Nov 2026, each URL returned verbatim by a WebSearch in this agent:
- https://code.claude.com/docs/en/skills (the page; 118,106 characters, read in two parts, offset 0 and 100000).
- https://code.claude.com/docs/en/skills?m=1 (the address BW9 cites; 115,286 characters, first 100,000 read). This address serves a different, shorter version of the page from the bare address; see Change 2.

No .md copy was read.

## Change 1

File: BW8-skills-and-automation.md

Current:
```
It then loads in sessions in that repository and in scheduled runs that clone it, but not in cloud threads inside a project.
```

Replacement:
```
It then loads in sessions in that repository and in cloud sessions on it, including cloud scheduled tasks, but not in cloud threads inside a project.
```

Result: PASS. The step sits under "read 16 Nov 2026: *Extend Claude with skills*"; that page does not use "clone" (the word does not occur on it). It does state the fact in these words, so the attribution holds once the wording follows the page: "Cowork sessions and cloud sessions, including cloud scheduled tasks, don't read `~/.claude/skills/` on your machine." ... "If a skill exists only in `~/.claude/skills/` on your machine, Claude Code reports that the skill was not found when a cloud scheduled task invokes it. This happens because each run starts as a fresh cloud session. To make a personal skill available in these sessions: ... For cloud sessions other than project threads, you can instead commit the skill to the repository's `.claude/skills/`." And, locations table, Project row: "Sessions in this repository, but not cloud threads in a project." URL: https://code.claude.com/docs/en/skills. The fresh-clone fact stays in §6, cited there to the scheduled-tasks pages; no citation moves and no source is added.

Syllabus: no conflict. F59 and F65 record the same page and its "not cloud threads in a project"; nothing in the BW8 brief or the flags fixes the old wording.

## Change 2

File: BW9-agents.md

Current:
```
also prevents the skill from being preloaded into subagents, and, as of v2.1.196, from running when a scheduled task fires with the skill as its prompt.
```

Replacement:
```
also prevents the skill from being preloaded into subagents, and from running when a scheduled task fires with the skill as its prompt.
```

Result: PASS. The page at the bare address gives the scheduled-task clause no version. Frontmatter reference table, `disable-model-invocation` row, verbatim: "Set to `true` to prevent Claude from automatically loading this skill. Use for workflows you want to trigger manually with `/name`. Also prevents the skill from being preloaded into subagents and from running when a session-scoped scheduled task fires with the skill as its prompt. Default: `false`." The string "As of v2.1.196" does not occur on it. The only v2.1.196 on the page is in the Troubleshooting note on `/context`: "Before v2.1.196, the row counted the full text of every description and could show a value several times larger than the configured budget." URL: https://code.claude.com/docs/en/skills.

The fresh check's reading came from the cited address. https://code.claude.com/docs/en/skills?m=1 serves a different version (115,286 characters against 118,106), whose row reads: "Also prevents the skill from being preloaded into subagents. As of v2.1.196, also prevents the skill from running when a scheduled task fires with the skill as its prompt." The same version ties v2.1.196 to `${CLAUDE_PROJECT_DIR}` ("requires Claude Code v2.1.196 or later"), and the bare page states no such requirement. On the current page the version belongs to the `/context` note, so the version is removed. The bare address is the page BW8 cites, and F65 (16 Nov 2026) recorded its "session-scoped" wording.

Syllabus: no conflict. F65 states the fact without a version ("running it from session-scoped scheduled tasks"); the BW9 brief names no version.

## Not a text change 1

Item 3's alternative, moving the step's attribution to the scheduled-tasks page, is not needed. Change 1 rewords the step to what the cited skills page states, which keeps the citation where it is.

## Not a text change 2

BW8 needs no change for item 4. BW8 does not state v2.1.196 (checked by search of files/BW8-skills-and-automation.md), as item 4 says.

## Outside scope (reported, not changed)

1. BW9 §4, same bullet: the page's current row says "session-scoped scheduled task". BW9 says "a scheduled task", which on BW8 §6's reading would also cover cloud and Desktop tasks. No correction names this word, so it was left unchanged. A later corrections pass could insert "session-scoped" before "scheduled task", as F65 already has it.
2. BW9 cites https://code.claude.com/docs/en/skills?m=1 twice (line 131, the "Four facts" lead-in, and line 499, Sources, "read at this address"). Today that address serves an older version of the page than the bare address. This is the two-versions problem of F41 and F69, now on a query-string variant rather than a .md copy. The other three facts in that BW9 list were not re-checked against the bare page here. Proposal: move both citations to https://code.claude.com/docs/en/skills after a check reads the three facts there, and add a syllabus flag saying a unit cites the bare page URL with no query string.

---
Summary:
- Model: claude-opus-5-5. 2 PASS, 0 FAIL. 0 syllabus conflicts.
- I checked by script that each Current block occurs exactly once in its file. Neither change touches a viz block.
- Report file write was refused; the full report is above.
- New outside scope: the ?m=1 address BW9 cites serves an older version of the skills page (it has "As of v2.1.196"; the bare page does not), the same two-versions problem as F41 and F69. BW9 also says "a scheduled task" where the page says "session-scoped scheduled task".
