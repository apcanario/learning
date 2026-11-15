---
kind: corrections-check
row: W-BW4
course: building-with-ai
date: 2026-11-15
model: claude-opus-5-5
units: [BW1, B4]
chat: https://claude.ai/code/session_01KMmgQzjvLSGBCfKL6ycyBm
---

Model: claude-opus-5-5. The harness refused the report file, so the full report follows.

Verdict: 7 pass, 2 fail, 0 syllabus conflicts. Corrections 3 and 4 fail: the current B4 wording matches the page, so make no change to either.

# W-BW4 · corrections check

Checked 15 Nov 2026. Every Current was counted by script in its file: each occurs exactly once. Pages were fetched only from URLs this agent's own searches returned.

Sources fetched:
- **S1:** Claude Help Center, *How do usage and length limits work?* (https://support.claude.com/en/articles/11647753-understanding-usage-and-length-limits). The fetched page title is "How do usage and length limits work? | Claude Help Center". Text: "On paid plans, the newest models support up to a 1M token context window, while others support 500K or 200K tokens."
- **S2:** Anthropic, *Models overview* (https://platform.claude.com/docs/en/about-claude/models/overview.md). Text: "1M tokens is roughly 555k words or 2.5M Unicode characters on the current tokenizer (introduced with Claude Opus 4.7)".
- **S3:** Claude Code docs, *How Claude remembers your project* (https://code.claude.com/docs/en/memory.md). Text:
  - (a) "If an entry is a multi-step procedure or only matters for one part of the codebase, move it to a [skill] or a [path-scoped rule] instead."
  - (b) "Consistency: if two instructions contradict each other, Claude may pick one arbitrarily. Review your CLAUDE.md files, nested CLAUDE.md files in subdirectories, and .claude/rules/ periodically to remove outdated or conflicting instructions. To have Claude find them for you, run a prompt audit."
  - (c) Under "Audit your instruction files": "Claude looks for problems such as instructions written for older models, references to files or commands that don't exist, and files that contradict each other."
  - No sentence that contains "contradict" uses the word "rules".
- **S4:** Claude Code docs, *Automate work with scheduled tasks* (https://code.claude.com/docs/en/web-scheduled-tasks.md). Text: "A cloud scheduled task, formerly a routine, is a saved Claude Code configuration: a prompt, one or more repositories, and a set of connectors, packaged once and run automatically."
- **S5:** Claude Help Center, *Manage Claude's tool access* (https://support.claude.com/en/articles/13730515-manage-claude-s-tool-access), dated March 16, 2026. Text:
  - "Each connector takes up space in a conversation."
  - Auto: "Claude decides dynamically which connectors to load based on what you're working on."
  - Always available: "All your connectors are loaded at the start of every conversation."
  - On demand: "Connectors aren't loaded until Claude searches for the right one based on your request."

Syllabus check covered all thirteen briefs in units_data.py (BW1–BW10, DD-BW1–DD-BW3), the AIMS lines, syllabus-flags.md and case-academy.md. Only BW4's AIMS line takes B4: "B4 as source material; its audit is summarised in the Academy case file". No other brief takes it.

---

## 1 · B4 §2, the history reports against the window

**File:** B4-context-engineering.md, line 166. Count: 1.

**Current:** `the history reports alone are about 1.3 million tokens, more than six times the 200K window he has on claude.ai (B1 §1)`

**Replacement:** `the history reports alone are about 1.3 million tokens, more than the 1M-token window the newest models have on paid claude.ai plans (Claude Help Center, read 15 Nov 2026)`

**Source check:** PASS. S1: "On paid plans, the newest models support up to a 1M token context window, while others support 500K or 200K tokens." The comparison holds at either rate: 3,484,164 characters at 2.7 is about 1.29M tokens, and at 2.5 about 1.39M.

Not in this correction's scope: the same sentence opens "At B1 §2's arithmetic of about 2.7 characters per token". That stays at 2.7 while corrections 2 and 8 move B4 to 2.5. At 2.5 the figure would be "about 1.4 million".

**Syllabus:** NO. F9 already records 1M / 500K / 200K, and no brief relies on B4's 200K figure.

## 2 · B4 §3, project knowledge against the window

**File:** B4-context-engineering.md, line 193. Count: 1.

**Current:** `907,260 characters is about 336,000 tokens at B1's 2.7 characters per token, and about 259,000 at the older 3.5 figure B1 also reports. Both exceed the 200K window.`

**Replacement:** `907,260 characters is about 363,000 tokens at the current tokenizer's 2.5 characters per token (BW1 §2). That is inside the 1M-token window the newest models have on paid plans and above the 200K window of older ones, so whether the Project runs in retrieval mode depends on the model, and is not visible from the repository.`

**Source check:** PASS. S2 gives 2.5M Unicode characters per 1M tokens, and 907,260 / 2.5 = 362,904. S1 gives 1M / 500K / 200K. The replacement leaves out the 500K tier (363K also fits inside 500K), but "depends on the model" still holds.

Problems this correction leaves in place:
- The next sentence still says "On the retrieval article's rule, a Project of that size runs in retrieval mode … an inference from the documented rule and the measured size". It now contradicts the replacement.
- The notes say this correction "touches … F1 and Deliverable A" but give no replacements for them. The 2.7 / 200K figures stay in:
  - the §3 table: "about 1,600 tokens at 2.7", line 184
  - the §3 viz block: caption "2.7 and its older 3.5 … against the 200K window", and labels "200K window" and "Knowledge at 2.7"
  - Deliverable A: "above the window, so in retrieval mode by the documented rule", line 376
  - F1 evidence: "about 336,000 tokens … against a 200K window", line 385
  - check 5: "about 40,000 tokens at 2.7", line 492
  - limitations 1: "exceed the 200K window under either tokens-per-character figure", line 531

**Syllabus:** NO. The case file holds no retrieval-mode fact, and BW4 marks that cell `[NOT IN CASE FILE]`. BW4's brief does not rest on B4's inference.

## 3 · B4 §5, Instructions that contradict preferences

**File:** B4-context-engineering.md, line 349. Count: 1.

**Current:** `Claude Code's documentation: "if two instructions contradict each other, Claude may pick one arbitrarily"`

**Replacement:** `Claude Code's documentation: "if two rules contradict each other, Claude may pick one arbitrarily"`

**Source check:** FAIL. S3(b) reads "if two instructions contradict each other, Claude may pick one arbitrarily". The Current is accurate, and the replacement would put a misquotation in. Make no change.

**Syllabus:** NO.

## 4 · B4 §5, Stale files

**File:** B4-context-engineering.md, line 345. Count: 1.

**Current:** `Claude Code's documentation lists what its own instruction audit looks for, among them "instructions written for older models, references to files or commands that don't exist, and files that contradict each other"`

**Replacement:** `Claude Code's documentation asks you to review its instruction files "periodically to remove outdated or conflicting instructions"`

**Source check:** FAIL. The list is on the page, in the "Audit your instruction files" section (`/doctor prompt-audit`). S3(c): "Claude looks for problems such as instructions written for older models, references to files or commands that don't exist, and files that contradict each other." The Current is accurate. Make no change.

Applying the replacement would also cause two problems:
- The next sentence, "His repository has all three:", would point at a list that is no longer there.
- The quoted phrase already appears four lines later, on line 349.

**Syllabus:** NO.

## 5 · B4 §1, The rule that sorts them

**File:** B4-context-engineering.md, line 44. Count: 1.

**Current:** `and "If an entry is a multi-step procedure or only matters for one part of the codebase, move it to a skill"`

**Replacement:** `and "If an entry is a multi-step procedure or only matters for one part of the codebase, move it to a skill or a path-scoped rule instead"`

**Source check:** PASS. S3(a) has exactly these words; the replacement only drops the page's links.

**Syllabus:** NO. BW4 §1 (line 42) already gives the full rule.

## 6 · B4 §1, Scheduled tasks

**File:** B4-context-engineering.md, line 42. Count: 1.

**Current:** `In Claude Code, a cloud scheduled task is "a saved Claude Code configuration: a prompt, one or more repositories, and a set of connectors"`

**Replacement:** `In Claude Code, a cloud scheduled task (formerly called a routine) is "a saved Claude Code configuration: a prompt, one or more repositories, and a set of connectors"`

**Source check:** PASS. S4: "A cloud scheduled task, formerly a routine, is a saved Claude Code configuration: a prompt, one or more repositories, and a set of connectors, packaged once and run automatically." The quoted span is exact.

**Syllabus:** NO. It is consistent with BW4 §1 and with the BW8 need. BW8's brief ("scheduled tasks, what they can and cannot touch, dated") is unaffected.

## 7 · B4 Sources, usage and length limits

**File:** B4-context-engineering.md, line 557. Count: 1.

**Current:** `Claude Help Center. *Usage and length limits* (article 11647753). https://support.claude.com/en/articles/11647753`

**Replacement:** `Claude Help Center. *How do usage and length limits work?* https://support.claude.com/en/articles/11647753-understanding-usage-and-length-limits`

**Source check:** PASS. The fetched page title is "How do usage and length limits work? | Claude Help Center", which matches BW1 Sources (line 400). Search returned that URL and the fetch loaded it.

**Syllabus:** NO.

## 8 · B4 Deliverable A, tokens convention

**File:** B4-context-engineering.md, line 364. Count: 1.

**Current:** `about 2.7 characters per English token for Opus 5.5's tokenizer, unmeasured`

**Replacement:** `about 2.5 characters per token for the current tokenizer (Anthropic, *Models overview*: 1M tokens ≈ 2.5M Unicode characters; BW1 §2)`

**Source check:** PASS. S2: "1M tokens is roughly 555k words or 2.5M Unicode characters on the current tokenizer (introduced with Claude Opus 4.7)".

Scope:
- The notes say "§2 and Deliverable A", but this Current occurs only in the Deliverable. §2's wording ("At B1 §2's arithmetic of about 2.7", line 166) is different text, and no correction covers it.
- The bullet's frame stays "B1 §2's arithmetic (…), with the 3.5 figure beside it", so after the change it credits a 2.5 figure to B1 §2.

**Syllabus:** NO.

## 9 · Contradiction: BW1 §8, layer map, row "Tools and connectors", "When" cell

**File:** BW1-mental-model.md, line 213. Count: 1.

**Current:** `Only when called, then for the rest of the chat`

**Replacement:** `The connector: at the start in Always available mode, by Claude's choice in Auto, when searched for in On demand ([*Manage Claude's tool access*](https://support.claude.com/en/articles/13730515-manage-claude-s-tool-access)); its results: only when called, then for the rest of the chat`

**Source check:** PASS. Each mode matches S5:
- Always available: "All your connectors are loaded at the start of every conversation."
- Auto: "Claude decides dynamically which connectors to load based on what you're working on."
- On demand: "Connectors aren't loaded until Claude searches for the right one based on your request."
- The page also says: "Each connector takes up space in a conversation."

Scope:
- The row's "What it puts in the window" cell still reads "Results of a web search, a file read, or an action in a connected service". It does not name the connector itself, which the new "When" cell describes. Read with that cell, the old row was arguably correct; the contradiction holds only against the row label.
- BW1 Sources has no entry for article 13730515, so this adds a new source to BW1 without a Sources line.
- There is no erratum marker in BW1's convention ("(erratum 15 Nov 2026: was …)").

**Syllabus:** NO. BW1's brief asks for the layers "as a map the later units fill in". §8 already routes tools and connectors to BW4.

---

## New items found (not fixed)

1. **B4 is left inconsistent after corrections 1, 2 and 8.** The following still need their own Current and replacement:
   - §2 line 166 ("At B1 §2's arithmetic of about 2.7"; at 2.5 the figure is about 1.4M)
   - the §3 sentence asserting retrieval mode by rule
   - the §3 table (1,600 tokens)
   - the §3 viz block
   - Deliverable A table, line 376
   - F1, line 385
   - check 5, line 492 (110,000 characters is about 44,000 tokens at 2.5)
   - limitations 1, line 531
2. **BW4 §8 contradicts notes.md on the OpenAI scheduled-tasks page.**
   - BW4 cites OpenAI *Scheduled tasks in ChatGPT* (help.openai.com/en/articles/10291617) as "read 15 Nov 2026" (line 195; Sources line 385).
   - BW4 line 186 says the ChatGPT column rests on "the help-centre page on scheduled tasks".
   - notes.md Needs 8 says that article failed to load.

   One of the two is wrong. If the fetch failed, line 195's ChatGPT cell is unsourced.
3. **The notes rest on a wrong premise about the briefs.** notes.md says the "Packet held no Briefs data for the course's unwritten units", but this packet's units_data.py holds all thirteen briefs. The writer checked contradictions against BW1–BW3 only, so BW4 has not been checked against the briefs of BW5–BW10 and DD-BW1–DD-BW3. Corrections 1–9 were checked against all of them here, and none conflicts.
4. **Minor paraphrase in BW4 §6, line 170.** It has `if two rules contradict each other, "Claude may pick one arbitrarily"`. The page says "instructions"; the quoted part is exact.

Verdict: 7 pass, 2 fail, 0 syllabus conflicts
