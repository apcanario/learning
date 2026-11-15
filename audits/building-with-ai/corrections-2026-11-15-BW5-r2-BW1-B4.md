---
kind: corrections-check
row: W-BW5
course: building-with-ai
date: 2026-11-15
model: claude-opus-5-5
units: [BW1, B4]
round: 2
chat: https://claude.ai/code/session_01KMmgQxb5xyzkrLHQ6hh6WQ
---

The checker's report, verbatim from its reply (the harness refused it a report file), saved before any change was applied.

Model: claude-opus-5-5
Verdict: 4 pass, 0 fail, 0 syllabus conflicts

(The harness would not let me write /tmp/bw5/corr2/out/report.md, so the full report is below. The only file I wrote is the count script /tmp/bw5/corr2/out/check.py.)

# W-BW5 step 1b, round two · corrections check of round one's New 1 to New 4

Checked 15 Nov 2026 against files/BW1-mental-model.md and files/B4-context-engineering.md as they now stand. I counted every Current with `out/check.py`. Each occurs exactly once, and no Replacement already occurs in its file. The two changes in each file don't overlap. After all four are applied, neither file has a "carry no exact date" line without "Most". I fetched sources only from URLs that my own searches in this run returned verbatim, and took no source text from the round-one report.

Sources fetched this run:
- **S1** Claude Help Center, *How do usage and length limits work?*, https://support.claude.com/en/articles/11647753-understanding-usage-and-length-limits.
  - Title as fetched: "How do usage and length limits work? | Claude Help Center".
  - Label: "Updated over a week ago" (no exact date).
  - Text: "On paid plans, the newest models support up to a 1M token context window, while others support 500K or 200K tokens."
- **S2** Anthropic, *Models overview*, https://platform.claude.com/docs/en/about-claude/models/overview.md.
  - Front matter: "title: Models overview", "url: https://platform.claude.com/docs/en/models/overview".
  - I also fetched the HTML page at https://platform.claude.com/docs/en/models/overview. Its title is "Models overview - Claude Platform Docs": it is Anthropic's developer documentation, not the Help Center.
  - Text (from the .md): "Context window: 1M tokens is roughly 555k words or 2.5M Unicode characters on the current tokenizer (introduced with Claude Opus 4.7); models before it fit about 750k words in 1M tokens."
- **S3** Claude Help Center, *Manage Claude's tool access*, https://support.claude.com/en/articles/13730515-manage-claude-s-tool-access.
  - Title as fetched: "Manage Claude’s tool access | Claude Help Center".
  - Date shown: "March 16, 2026". The page has no "updated" label.

The syllabus check covered briefs/ (BW1, BW4 to BW10, DD-BW1 to DD-BW3), case-academy.md, syllabus-flags.md and sourcing-standard.md. Two flags are relevant:
- F25: "*Manage Claude's tool access*, dated 16 Mar 2026, read 15 Nov 2026".
- F9: "BW1 states it dated. ... Later units cite BW1 for the mechanism and re-read the figure on the day."

No brief or flag relies on help-centre pages being undated, on B4's opened dates, or on which source the erratum names.

---

## Change 1
File: BW1-mental-model.md, line 12 (opening paragraph). Count: 1.
Current:
```
Anthropic's help-centre pages carry no exact date, only a note of how recently they were updated, so the reading date is the only date they can be given.
```
Replacement:
```
Most of Anthropic's help-centre pages carry no exact date, only a note of how recently they were updated, so for those the reading date is the only date they can be given.
```
Result: PASS. S3 shows a full date, so "pages carry no exact date" is false for every page. S1 shows only a relative label, so "most" holds. The wording matches the corrected Sources note on line 383 ("Most of Anthropic's help-centre pages show no exact date") and BW1's own Sources entry on line 406 ("16 March 2026"). It adds no new claim or source.
Source: S3, "March 16, 2026" shown under the heading of "Manage Claude’s tool access | Claude Help Center". S1, "Updated over a week ago".
Syllabus: no conflict. Consistent with F25 ("dated 16 Mar 2026"). F9 asks BW1 to state figures with dates, which the paragraph still does.

## Change 2
File: BW1-mental-model.md, line 439 (Unsure list, item 6). Count: 1.
Current:
```
6. Anthropic help-centre pages carry no exact date (
```
Replacement:
```
6. Most Anthropic help-centre pages carry no exact date (
```
Result: PASS. This is the same error as Change 1. The item's examples ("updated this week", "over 3 weeks ago") still illustrate the undated majority. The rest of the item (window sizes, memory behaviour, plan lists read 15 Nov 2026) is unchanged.
Source: S3, "March 16, 2026". S1, "Updated over a week ago".
Syllabus: no conflict. Consistent with F25.

## Change 3
File: B4-context-engineering.md, line 12 (opening evidence paragraph, the Product documentation sentence). Count: 1. It does not overlap the text that round one's Change 1 replaced later in the same line.
Current:
```
each page was opened on 29 October 2026 and is cited for that day,
```
Replacement:
```
each page was opened on 29 October 2026 and is cited for that day, except two pages read on 15 November 2026 for the erratum and cited for that day (see Sources),
```
Result: PASS. The Sources header on line 544 now says *Models overview* was opened 15 November 2026 and *How do usage and length limits work?* was opened again that day for the erratum. The body cites both as "read 15 Nov 2026" (lines 12, 166, 201, 364). So "each page ... is cited for that day [29 Oct]" is untrue for two pages.

I reworded round one's version ("two were opened on 15 November 2026"), because the usage page was also opened on 29 October. "Read on 15 November ... and cited for that day" is true of both pages. It adds no new claim or source.
Source: S1 (usage page, read 15 Nov 2026) and S2 (Models overview, read 15 Nov 2026), as quoted above.
Syllabus: no conflict. BW4's brief takes B4 as source material, but no brief relies on B4's opened dates. The change also does better on Sourcing standard Part 1, which asks for a date on each source.

## Change 4
File: B4-context-engineering.md, line 565 (erratum paragraph under Sources). Count: 1.
Current:
```
the 1M, 500K and 200K windows of paid plans (Claude Help Center, Models overview)
```
Replacement:
```
the 1M, 500K and 200K windows of paid plans (Claude Help Center, *How do usage and length limits work?*; Anthropic, *Models overview*)
```
Result: PASS. The current parenthetical reads as one Help Center page called "Models overview". In fact S2 is Anthropic's Claude Platform Docs (title "Models overview - Claude Platform Docs") and is the source of the 2.5-characters-per-token figure. The window sizes come from the Help Center page, S1. Both titles are already in B4's Sources list (line 548 and the usage-limits entry), so the change adds no new source.
Source: S1, "On paid plans, the newest models support up to a 1M token context window, while others support 500K or 200K tokens." S2, "1M tokens is roughly 555k words or 2.5M Unicode characters on the current tokenizer (introduced with Claude Opus 4.7)".
Syllabus: no conflict. No brief cites B4's erratum.

---

New: none.

Summary: claude-opus-5-5; report returned here because the report file was refused (script at /tmp/bw5/corr2/out/check.py); 4 pass, 0 fail, 0 syllabus conflicts, 0 new items.
