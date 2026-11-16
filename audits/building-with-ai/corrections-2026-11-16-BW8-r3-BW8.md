---
kind: corrections-check
row: W-BW8
course: building-with-ai
date: 2026-11-16
model: claude-opus-5-5
units: [BW8]
chat: https://claude.ai/code/session_01KMmgQy4zywM5ERbdfFcK6a
---

Third report (figure 4 and §6, from the figure re-check). The checker's report, verbatim from its report file, saved before any change was applied.

claude-opus-5-5

# Corrections check, BW8 (row W-BW8, step 7b, third report)

Sources read 16 Nov 2026, each from a URL a WebSearch in this agent returned:
- Anthropic, *Schedule recurring tasks in Claude Code Desktop*, https://code.claude.com/docs/en/desktop-scheduled-tasks — table "Compare scheduling options".
- Anthropic, *Run prompts on a schedule*, https://code.claude.com/docs/en/scheduled-tasks — table "Compare scheduling options" and "Seven-day expiry".

Remedy chosen for the /loop cells: the clause. The Desktop page's table states the three cells the figure shows for /loop: "Runs on | ... | Your machine", "Requires machine on | ... | Yes", "Access to local files | ... | Yes". The figure is right; the text lacked the clause. The figure's JSON is unchanged.

## Change 1

File: BW8-skills-and-automation.md
Current:
```
`/loop` runs inside an open session, takes that session's permissions, can repeat every minute, and a recurring one expires seven days after it is created (*Run prompts on a schedule*, read 16 Nov 2026; vendor).
```
Replacement:
```
`/loop` runs on your machine, which must be on, inside an open session, reaches local files, takes that session's permissions and can repeat every minute (all by the Desktop page's table); a recurring `/loop` task expires seven days after it is created (*Run prompts on a schedule*, read 16 Nov 2026; vendor).
```
Result: PASS. Merges the checker's two points on this sentence (the missing /loop clause; the closing citation). Desktop page's table, /loop column: "Runs on | Cloud, Anthropic-managed by default | Your machine | Your machine"; "Requires machine on | No | Yes | Yes"; "Requires open session | No | No | Yes"; "Access to local files | No (fresh clone) | Yes | Yes"; "Permission prompts | ... | Inherits from session"; "Minimum interval | 1 hour | ... | 1 minute" (https://code.claude.com/docs/en/desktop-scheduled-tasks). Expiry: "Recurring tasks automatically expire 7 days after creation." (https://code.claude.com/docs/en/scheduled-tasks). The citation was wrong: the sentence opens by saying its values are the Desktop page's table, and says the Run prompts copy differs, yet closed by citing Run prompts for every value. The replacement credits the cell values to the Desktop page and keeps Run prompts only for the expiry, which only that page states. No new source.
Syllabus: no conflict. BW8's brief asks for "scheduled tasks, what they can and cannot touch, dated"; the clause adds what /loop touches, dated by the sentence's existing read date. F31, F32, F65, F66 and F68 are unaffected.

## Change 2

File: BW8-skills-and-automation.md
Current:
```
From Anthropic, Schedule recurring tasks in Claude Code Desktop, the table 'Compare scheduling options', read 16 Nov 2026 (vendor)
```
Replacement:
```
From Anthropic, Schedule recurring tasks in Claude Code Desktop, its comparison table, read 16 Nov 2026 (vendor)
```
Result: PASS. The page's heading is "## Compare scheduling options" (https://code.claude.com/docs/en/desktop-scheduled-tasks). The title is right, but the text never names it: §6 says "the comparison table as *Schedule recurring tasks in Claude Code Desktop* prints it". The caption now uses the text's own words. After the replacement, every ```viz block's JSON parses (checked by script); figure 4 is still a 3-column matrix with 6 rows, each with 3 cells.
Syllabus: no conflict

## Not a text change 1

Figure 4's cells. The checker's alternative cells ("an open session", "not stated" ×2) are not applied. The cited table states all three /loop values the figure shows, so the figure stays as filed (Change 1 brings the text level with it).

## Not a text change 2

Out of scope; flagged for a later corrections pass ⚠. On today's read, the two pages' tables are identical. *Run prompts on a schedule* now gives the Desktop task's minimum interval as "1 minute when Claude sets it, 1 hour in the forms" and the cloud task's permission prompts as "Auto mode by default", the same as the Desktop page (https://code.claude.com/docs/en/scheduled-tasks). The unit's statement that the copy on Run prompts "gives the Desktop task's minimum interval as 1 minute and the cloud task's permission prompts as "No (runs autonomously)", so two of the vendor's own pages differ" (§6), and the caption's "differs on two cells (§6)", are not supported by this read. The page may have changed since the writer read it. No correction names that text, so it is unchanged here. Proposal: a corrections pass re-reads both tables and, if they still match, removes the "differ" clause from §6 and the caption. That changes no figure cell.

## Not a text change 3

§6 bullet "**Your computer.**" (cites *Run prompts on a schedule*, comparison table). Its cloud and Desktop values ("No (fresh clone)"; Desktop runs on "Your machine") are present in that page's table as read today. It is correct and no correction names it.
