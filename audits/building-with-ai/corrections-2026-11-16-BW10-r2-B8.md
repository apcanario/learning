# Corrections check, round 2 (W-BW10, 16 Nov 2026)

Checker: claude-opus-5-5, fresh context, packet only.

## Change 1
File: B8-cost-limits-hygiene.md
Result: PASS. The After text occurs exactly once (line 54, the "Usage credits are prepaid and billed at standard API rates" row). Source read 16 Nov 2026, Claude Help Center, *Manage usage credits for paid Claude plans*, https://support.claude.com/en/articles/12429409-manage-usage-credits-for-paid-claude-plans (URL returned by WebSearch in this agent; fetch succeeded):
- "Generally, usage credits purchased on or after December 7, 2026 expire 12 months after the purchase date."
- "Credits purchased before December 7, 2026 don't expire."
- "Expiration dates may vary in certain countries."
- Plans: "individuals subscribed to paid Claude plans (Pro, Max, and Ultra)"; spend limit: "Your usage continues until you reach your monthly spend limit, or your balance runs out with auto-reload off."; billing: "Usage credits are billed at standard API rates."
The After text matches these sentences ("generally" carries the page's hedge) and adds nothing beyond the page. It omits the country-variation sentence; "generally" covers it, so not a FAIL.
Note outside the change (no edit required by this check): the row's source cell says the page was labelled "Updated yesterday"; on this agent's read the page shows "Updated this week". Both are consistent with an update on or about 15 Nov 2026; the label is relative and will drift.
Syllabus: no conflict. The fact is dated to the day read, as the BW10 brief and F2/F15 require; it touches no flag's content (F7, F33 are memory; F15 plan facts are re-read and dated here); it uses no case fact and no private reference beyond the file's own register.
