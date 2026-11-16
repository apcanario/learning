---
kind: corrections-check
row: W-BW8
course: building-with-ai
date: 2026-11-16
model: claude-opus-5-5
units: [B5]
chat: https://claude.ai/code/session_01KMmgQy4zywM5ERbdfFcK6a
---

Second round. The checker's report, verbatim from its report file, saved before any change was applied.

claude-opus-5-5 (Opus 5.5), corrections checker, round 2, row W-BW8

Sources fetched 16 Nov 2026, each URL returned verbatim by a WebSearch in this agent:
- https://support.claude.com/en/articles/12512180-use-skills-in-claude (page title "Use skills in Claude | Claude Help Center")
- https://code.claude.com/docs/en/skills (two parts: characters 0 to 100000 and 100000 to end)

## Change 1

File: B5-skills-and-automation.md
Current:
```
the claude.ai help page suggests the same: "Try being more explicit in your request", for example "Use my brand guidelines skill to create a presentation" ([*Using skills in Claude*](https://support.claude.com/en/articles/12512180-using-skills-in-claude))
```
Replacement:
```
the claude.ai help page suggests the same: "Try being more explicit in your request", for example "Use my brand guidelines skill to create a presentation" ([*Use skills in Claude*](https://support.claude.com/en/articles/12512180-use-skills-in-claude))
```
Result: PASS. Page title "Use skills in Claude | Claude Help Center"; the page has "Try being more explicit in your request" and, under "Claude isn't using a skill", "Use my brand guidelines skill to create a presentation". https://support.claude.com/en/articles/12512180-use-skills-in-claude
Syllabus: no conflict

## Change 2

File: B5-skills-and-automation.md
Current:
```
(the folder name must match the skill name: [*Using skills in Claude*](https://support.claude.com/en/articles/12512180-using-skills-in-claude))
```
Replacement:
```
(the folder name must match the skill name: [*Use skills in Claude*](https://support.claude.com/en/articles/12512180-use-skills-in-claude))
```
Result: PASS. Page title "Use skills in Claude | Claude Help Center"; its troubleshooting lists "Skill folder name doesn't match the skill name". https://support.claude.com/en/articles/12512180-use-skills-in-claude
Syllabus: no conflict

## Change 3

File: B5-skills-and-automation.md
Current:
```
As documented on 29 October 2026 ([*Using skills in Claude*](https://support.claude.com/en/articles/12512180-using-skills-in-claude);
```
Replacement:
```
As documented on 29 October 2026 ([*Use skills in Claude*](https://support.claude.com/en/articles/12512180-use-skills-in-claude);
```
Result: PASS. Page title "Use skills in Claude | Claude Help Center", the title and slug B5's §1 and Sources list already use. https://support.claude.com/en/articles/12512180-use-skills-in-claude
Syllabus: no conflict

## Change 4

File: B5-skills-and-automation.md
Current:
```
(1,536, description and when_to_use combined); all opened 29 Oct 2026.
```
Replacement:
```
(1,536 by default, description and when_to_use combined); all opened 29 Oct 2026.
```
Result: PASS. "each entry's combined text is capped at 1,536 characters regardless of budget. The cap is configurable with skillListingMaxDescChars." https://code.claude.com/docs/en/skills
Syllabus: no conflict

## Change 5

File: B5-skills-and-automation.md
Current:
```
Claude Code keeps the first 1,536 characters and drops whole descriptions
```
Replacement:
```
Claude Code keeps the first 1,536 characters by default and drops whole descriptions
```
Result: PASS. "each entry's combined text is capped at 1,536 characters regardless of budget. The cap is configurable with skillListingMaxDescChars." https://code.claude.com/docs/en/skills
Syllabus: no conflict

## Change 6

File: B5-skills-and-automation.md
Current:
```
and that "Custom skills you upload aren't visible to colleagues until you share them" ([Claude Help Center, *Use skills in Claude*]
```
Replacement:
```
and that "Custom skills you upload aren't visible to colleagues until you share them"; sharing is available "On Team and Enterprise plans" ([Claude Help Center, *Use skills in Claude*]
```
Result: PASS. "On Team and Enterprise plans, you can share skills (see Share a skill below), or provision skills for your organization." and "Custom skills you upload aren't visible to colleagues until you share them." https://support.claude.com/en/articles/12512180-use-skills-in-claude
Syllabus: no conflict

## Not a text change 1

"None of his is near 1,536" (§3 item 1) and the chart's "Claude Code listing" value 1536 are comparisons with the cap, not statements of it; the "by default" qualifier is carried by the caption (Change 4) and the sentence before it (Change 5). Left unchanged.
