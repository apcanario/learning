---
kind: corrections-check
row: W-BW10
course: building-with-ai
date: 2026-11-16
model: claude-opus-5-5
units: [BW9]
chat: https://claude.ai/code/session_01KMmgQy4zywM5ERbdfFcK6a
---

Corrections C-BW9-1 and C-BW9-2. The checker's report, verbatim from its reply (the harness refused it a report file), saved before any change was applied.

claude-opus-5-5

# Corrections check, W-BW10 step 1b: C-BW9-1 and C-BW9-2 on BW9-agents.md

I could not write the report file (out/report.md was refused), so the full report is here.

Page read: Anthropic, *Extend Claude with skills*, at its bare address https://code.claude.com/docs/en/skills. WebSearch returned this address verbatim; I fetched it with WebFetch on 16 Nov 2026. The fetch covered characters 0 to 100,000 of 118,106, and every passage below falls in that range. It found no version string ("As of v2.1…") near the scheduled-task clause.

C-BW9-2: the lead-in supports four facts. All four hold on the bare page, so both citations move.
1. Subagent `skills` field: "In a regular session, skill descriptions are loaded into context so Claude knows what's available, but full skill content only loads when invoked. Subagents with preloaded skills work differently: the full skill content is injected at startup." Holds.
2. `disable-model-invocation`: "Set to `true` to prevent Claude from automatically loading this skill. … Also prevents the skill from being preloaded into subagents and from running when a session-scoped scheduled task fires with the skill as its prompt." Holds once "session-scoped" is inserted (C-BW9-1, Change 2).
3. Re-reading: "Claude Code does not re-read the skill file on later turns, so write guidance that should apply throughout a task as standing instructions rather than one-time steps." Holds.
4. Compaction: "Claude Code re-attaches the most recent invocation of each skill after the summary, keeping the first 5,000 tokens of each. Re-attached skills share a combined budget of 25,000 tokens. Claude Code fills this budget starting from the most recently invoked skill, so older skills can be dropped entirely after compaction if you have invoked many in one session." Holds.

## Change 1
File: BW9-agents.md
Current:
```
re-read on 16 Nov 2026 on Anthropic's *Extend Claude with skills* ([Claude Code documentation](https://code.claude.com/docs/en/skills?m=1); vendor):
```
Replacement:
```
re-read on 16 Nov 2026 on Anthropic's *Extend Claude with skills* ([Claude Code documentation](https://code.claude.com/docs/en/skills); vendor):
```
Result: PASS. All four facts this lead-in supports hold on the bare page (quotes 1 to 4 above). https://code.claude.com/docs/en/skills
Syllabus: no conflict. F70 says to cite the bare address.

## Change 2
File: BW9-agents.md
Current:
```
and from running when a scheduled task fires with the skill as its prompt.
```
Replacement:
```
and from running when a session-scoped scheduled task fires with the skill as its prompt.
```
Result: PASS. "Also prevents the skill from being preloaded into subagents and from running when a session-scoped scheduled task fires with the skill as its prompt." https://code.claude.com/docs/en/skills
Syllabus: no conflict

## Change 3
File: BW9-agents.md
Current:
```
- Anthropic. *Extend Claude with skills*. Claude Code documentation (read at this address). https://code.claude.com/docs/en/skills?m=1
```
Replacement:
```
- Anthropic. *Extend Claude with skills*. Claude Code documentation. https://code.claude.com/docs/en/skills
```
Result: PASS. This is the same page at its bare address, and the facts it supports hold there (quotes 1 to 4 above). https://code.claude.com/docs/en/skills. "(read at this address)" is dropped because the entry now gives the plain address, in the same form as the other bare-address entries.
Syllabus: no conflict

## Not a text change 1
The corrections ask for no other changes. Two nearby passages still hold on the bare page: the bullet's last sentence ("A skill you mark this way cannot be handed to an agent.") and the inference after the list ("inside the first 5,000 tokens"). A script confirmed that each "Current:" text occurs exactly once in BW9-agents.md.

## Outside scope (not changed, for the next chat)
1. Unsure list item 4 still says Extend Claude with skills was read at a ?m=1 address. After Changes 1 and 3 that is no longer true, so Extend Claude with skills and "?m=1" need to come out of the item. No correction names this item.
2. Three citations still carry query strings, which F70's rule does not allow: Best practices for Claude Code (?ref=t01.li), Manage costs effectively (?ref=t01.li) and Security (?web=1). Each appears in the text and in Sources. Moving them needs its own correction, with each fact re-read on the bare page.

---
Summary: claude-opus-5-5 — 3 PASS, 0 FAIL, no syllabus conflicts. Outside scope: Unsure item 4 is now stale, and three other citations (best-practices, costs, security) still carry query strings against F70.
