---
kind: corrections-check
row: W-BW8
course: building-with-ai
date: 2026-11-16
model: claude-opus-5-5
units: [BW8]
chat: https://claude.ai/code/session_01KMmgQy4zywM5ERbdfFcK6a
---

Fourth report (second round on figure 4 and §6). The checker's report, verbatim from its report file, saved before any change was applied.

claude-opus-5-5

# Corrections check, row W-BW8 step 7b, second round on figure 4

Reads of 16 Nov 2026 (this check), WebSearch then WebFetch of URLs that search returned verbatim:

- *Schedule recurring tasks in Claude Code Desktop*, https://code.claude.com/docs/en/desktop-scheduled-tasks and https://code.claude.com/docs/en/desktop-scheduled-tasks.md: both forms carry the same table. Cloud permission prompts "Auto mode by default"; cloud customizable schedule "Yes"; Desktop minimum interval "1 minute when Claude sets it, 1 hour in the forms".
- *Run prompts on a schedule*, https://code.claude.com/docs/en/scheduled-tasks (the page): the table matches the Desktop page's table in every cell, all nine rows and three columns. This is the URL the earlier check cited.
- *Run prompts on a schedule*, https://code.claude.com/docs/en/scheduled-tasks.md (the .md copy): this is an older revision. It still has the earlier section text, for example "Routines" links and the older Jitter section. Its table differs from the Desktop table in **three** cells, not two: cloud "Permission prompts" is "No (runs autonomously)", not "Auto mode by default"; cloud "Customizable schedule" is "Via `/schedule` in the CLI", not "Yes"; Desktop "Minimum interval" is "1 minute", not "1 minute when Claude sets it, 1 hour in the forms".

The vendor page changed during the day. The writer's read and the .md copy have the old table, while the earlier corrections check and the page URL today have the new one. The .md copy lags the page, which is the same pattern as F41 (Best practices, page and .md copy differ). On the page itself the two tables match. The unit's "differs on two cells" is wrong under either read: zero cells on the page, three on the .md copy. Both changes below delete the "differ" statements and nothing else. What is left cites only the Desktop page's table and is true under both reads.

## Change 1

File: BW8-skills-and-automation.md

Current:
```
. The copy of that table on *Run prompts on a schedule* gives the Desktop task's minimum interval as 1 minute and the cloud task's permission prompts as "No (runs autonomously)", so two of the vendor's own pages differ: a cloud task
```

Replacement:
```
: a cloud task
```

Result: PASS. Desktop page table (https://code.claude.com/docs/en/desktop-scheduled-tasks, also its .md copy): Permission prompts, cloud "Auto mode by default"; Minimum interval, Desktop "1 minute when Claude sets it, 1 hour in the forms". Run prompts page table (https://code.claude.com/docs/en/scheduled-tasks): the same, "Auto mode by default" and "1 minute when Claude sets it, 1 hour in the forms", with every other cell also the same. The .md copy (https://code.claude.com/docs/en/scheduled-tasks.md) still has "No (runs autonomously)" and "1 minute", and also "Via `/schedule` in the CLI" for the cloud customizable schedule. After the change, §6 reads "...read 16 Nov 2026; vendor): a cloud task runs on Anthropic's cloud, ...". Every value after the colon is from the Desktop page's table, which both reads confirm.

Syllabus: no conflict. F41 is the precedent for page and .md copies that differ. Each unit names the URL it read, and §6 names the Desktop page's URL.

## Change 2

File: BW8-skills-and-automation.md

Current:
```
read 16 Nov 2026 (vendor); the copy of the table on Run prompts on a schedule differs on two cells (§6). A /loop
```

Replacement:
```
read 16 Nov 2026 (vendor). A /loop
```

Result: PASS. The tables and URLs are the same as in Change 1. This text is inside figure 4's ```viz block. Checked by script: every viz block in the unit still parses as JSON after both changes, and each Current string occurs exactly once. No figure cell changes. The figure's Minimum interval cells ("1 hour", "1 hour in forms, 1 minute by Claude", "1 minute") match the Desktop page's table and the Run prompts page's table.

Syllabus: no conflict

## Not a text change 1

§6's "(all by the Desktop page's table)", the seven-day `/loop` expiry, and §9 "Also look for: ... a product fact that differs between two of the vendor's own pages" are not named by this correction. The expiry is confirmed on both forms of Run prompts: "Recurring tasks automatically expire 7 days after creation". They are unchanged.

## Not a text change 2

Proposal, flagged ⚠: a syllabus flag in the form of F41 for *Run prompts on a schedule*. On 16 Nov 2026 its page and its .md copy carry different comparison tables, which differ in three cells. Any unit or staleness check that cites it should name the exact URL it read. The disruption is limited to the staleness check of BW8, which should read https://code.claude.com/docs/en/scheduled-tasks, the page.
