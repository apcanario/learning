---
kind: corrections-check
row: W-BW5
course: building-with-ai
date: 2026-11-15
model: claude-opus-5-5
units: [BW1, B4]
round: 1
chat: https://claude.ai/code/session_01KMmgQxb5xyzkrLHQ6hh6WQ
---

The checker's report, verbatim, saved before any change was applied.

Model: claude-opus-5-5
Verdict: 3 pass, 0 fail, 0 syllabus conflicts

# W-BW5 step 1b · corrections check of the three W-BW4 leftovers

Checked 15 Nov 2026. Every Current below was counted by script (`out/check.py`) in its file and occurs exactly once; no Replacement text already occurs in its file. Pages were fetched only from URLs returned verbatim by this run's own searches.

Sources fetched this run:
- **S1** Claude Help Center, *How do usage and length limits work?*, https://support.claude.com/en/articles/11647753-understanding-usage-and-length-limits. Title as fetched: "How do usage and length limits work? | Claude Help Center"; label "Updated over a week ago". Text: "On paid plans, the newest models support up to a 1M token context window, while others support 500K or 200K tokens."
- **S2** Anthropic, *Models overview*, fetched at https://platform.claude.com/docs/en/about-claude/models/overview.md (the page's own front matter gives url https://platform.claude.com/docs/en/models/overview, the URL BW1 lists; search also returned https://platform.claude.com/docs/en/about-claude/models/overview verbatim). Text: "1M tokens is roughly 555k words or 2.5M Unicode characters on the current tokenizer (introduced with Claude Opus 4.7); models before it fit about 750k words in 1M tokens. 200k tokens is roughly 150k words."
- **S3** Claude Help Center, *Manage Claude's tool access*, https://support.claude.com/en/articles/13730515-manage-claude-s-tool-access. Title as fetched: "Manage Claude’s tool access | Claude Help Center"; date shown on its own line under the heading: "March 16, 2026".

Syllabus check covered briefs/ (BW1, BW4–BW10, DD-BW1–DD-BW3), case-academy.md and syllabus-flags.md. Relevant: BW4's brief, "Takes: B4 as source material; its audit is summarised in the Academy case file; BW1, BW3."; F9, "Later units cite BW1 for the mechanism and re-read the figure on the day."; F25, which records the connector page as "dated 16 Mar 2026, read 15 Nov 2026".

---

## Change 1
File: files/B4-context-engineering.md, line 12 (opening evidence paragraph). Count: 1.
Current:
```
What a context window is, the 200K window on claude.ai, the 2.7-characters-per-token arithmetic, why every turn re-sends the whole chat, and the layer map of his setup are in B1 (§1, §2, §6, §7).
```
Replacement:
```
What a context window is, why every turn re-sends the whole chat, and the layer map of his setup are in B1 (§1, §2, §6, §7). B1's 200K window on claude.ai and its 2.7-characters-per-token arithmetic are out of date: on paid plans the newest models have a 1M-token window and others 500K or 200K (Claude Help Center, read 15 Nov 2026), and the current tokenizer runs at about 2.5 characters per token (Anthropic, *Models overview*, read 15 Nov 2026; BW1 §2).
```
Result: PASS. The windows match S1 and the 2.5 figure matches S2 (2.5M Unicode characters per 1M tokens). The replacement uses the same wording and citations the corrected body already uses (lines 166, 193, 364), so it adds no new claim or source.
Source: S1, "On paid plans, the newest models support up to a 1M token context window, while others support 500K or 200K tokens." S2, "1M tokens is roughly 555k words or 2.5M Unicode characters on the current tokenizer (introduced with Claude Opus 4.7)".
Syllabus: no conflict. This matches F9 (1M / 500K / 200K, dated). BW4 takes B4 as source material and already rests on the corrected figures. No brief relies on the 200K or 2.7 figures.

## Change 2
File: files/B4-context-engineering.md, Sources (header note and the Anthropic entries, lines 544–547). Count: 1.
Current:
```
All web sources opened 29 October 2026.

- Anthropic. *Agent Skills*. Claude Platform docs. https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview
- Anthropic. *Effective context engineering for AI agents*. Anthropic Engineering, 29 September 2025. https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
```
Replacement:
```
All web sources opened 29 October 2026, except *Models overview*, opened 15 November 2026; *How do usage and length limits work?* was opened again on 15 November 2026 for the erratum below.

- Anthropic. *Agent Skills*. Claude Platform docs. https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview
- Anthropic. *Effective context engineering for AI agents*. Anthropic Engineering, 29 September 2025. https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
- Anthropic. *Models overview*. Claude Platform docs. https://platform.claude.com/docs/en/about-claude/models/overview
```
Result: PASS. The page exists under that title at that path (S2), and the body cites it at line 364 only since the 15 Nov erratum. The usage page is cited in the body as "read 15 Nov 2026" (lines 166, 201, 385). It already had a Sources entry, under its corrected title. The new entry follows the list's existing format and alphabetical order among the Anthropic entries.
- Alternative URL: the page's canonical URL is https://platform.claude.com/docs/en/models/overview, which BW1 uses. Either URL loads the same page.
Source: S2 page title "Models overview"; "1M tokens is roughly 555k words or 2.5M Unicode characters on the current tokenizer (introduced with Claude Opus 4.7)". S1 title "How do usage and length limits work? | Claude Help Center".
Syllabus: no conflict. Sourcing standard Part 1 asks each source to carry its locator and date, and this change satisfies it. No brief cites B4's Sources list.

## Change 3
File: files/BW1-mental-model.md, Sources note, line 383. Count: 1.
Current:
```
All web pages read on 15 November 2026. Anthropic's help-centre pages show no exact date.
```
Replacement:
```
All web pages read on 15 November 2026. Most of Anthropic's help-centre pages show no exact date; *Manage Claude's tool access* shows 16 March 2026.
```
Result: PASS. S3 shows a full date, which contradicts the Current. S1 shows the relative label the note describes ("Updated over a week ago"), so "most" holds. BW1's own entry at line 406 already gives "16 March 2026".
Source: S3, "March 16, 2026", shown under the page heading. S1, "Updated over a week ago".
Syllabus: no conflict. This is consistent with F25 ("dated 16 Mar 2026, read 15 Nov 2026"). F25's still-open proposal to add the article to BW1's Sources is already done: line 406 lists it, so that proposal can be closed.

---

## New items

## New 1
File: files/BW1-mental-model.md, line 12 (opening paragraph). Count: 1. This is the same error as Change 3.
Current:
```
Anthropic's help-centre pages carry no exact date, only a note of how recently they were updated, so the reading date is the only date they can be given.
```
Replacement:
```
Most of Anthropic's help-centre pages carry no exact date, only a note of how recently they were updated, so for those the reading date is the only date they can be given.
```
Result: PASS.
Source: S3, "March 16, 2026", shown under the heading. S1, "Updated over a week ago".
Syllabus: no conflict.

## New 2
File: files/BW1-mental-model.md, line 439 (Unsure list, item 6). Count: 1. This is the same error as Change 3.
Current:
```
6. Anthropic help-centre pages carry no exact date (
```
Replacement:
```
6. Most Anthropic help-centre pages carry no exact date (
```
Result: PASS.
Source: S3, "March 16, 2026". S1, "Updated over a week ago".
Syllabus: no conflict.

## New 3
File: files/B4-context-engineering.md, line 12, in the same paragraph as Change 1. Count: 1. The paragraph says every product-documentation page "was opened on 29 October 2026 and is cited for that day". That is now untrue for the two pages Change 2 dates to 15 Nov.
Current:
```
each page was opened on 29 October 2026 and is cited for that day,
```
Replacement:
```
each page was opened on 29 October 2026 and is cited for that day (two were opened on 15 November 2026 for the erratum; see Sources),
```
Result: PASS. It matches the body's own "read 15 Nov 2026" citations and Change 2.
Source: S1 and S2, as in Changes 1 and 2.
Syllabus: no conflict.

## New 4
File: files/B4-context-engineering.md, erratum paragraph under Sources, line 564. Count: 1. The parenthetical attributes *Models overview* to the Claude Help Center. The windows come from the Help Center page (S1), but *Models overview* is Anthropic's platform documentation (S2), and it is the source of the 2.5 figure.
Current:
```
the 1M, 500K and 200K windows of paid plans (Claude Help Center, Models overview)
```
Replacement:
```
the 1M, 500K and 200K windows of paid plans (Claude Help Center, *How do usage and length limits work?*; Anthropic, *Models overview*)
```
Result: PASS.
Source: S1, "On paid plans, the newest models support up to a 1M token context window, while others support 500K or 200K tokens." S2 is served from platform.claude.com, page title "Models overview".
Syllabus: no conflict.

Verdict: 3 pass, 0 fail, 0 syllabus conflicts; 4 new items (all pass, no conflicts).
