---
audit: fresh check
unit: BW1 · Mental model
course: building-with-ai · Building with AI
model: claude-opus-5-5
date: 2026-11-15
chat: https://claude.ai/code/session_01KMmgQyvcEehfr4eG93G5iB
verdict: fix · 1 errors, 7 should-fix, 7 minor
---

The checker's final report, verbatim, from its hand-back. Saved before any finding was applied.

Checker reply: claude-opus-5-5. Verdict: BW1 · fix · error 1, should-fix 7, minor 7. (Its Write of out/report.md was refused, so the report below was returned as text and saved here by the chat.)

# BW1 · Fresh check

Checker: claude-opus-5-5. Run 15 Nov 2026 with live search, packet files only. There is no audit report or errata for this course. Two fetches were refused and count as "not checked": arxiv.org/html/2509.04664v1 and openai.com/blog/why-language-models-hallucinate/.

## (1) Coverage
All brief items are covered:
- context window as the one thing you control (§1)
- tokens as cost and as attention (§2)
- what persists inside a chat, across chats, and with memory, dated (§3)
- trained, retrieved and in-conversation knowledge, and the training cutoff (§4)
- why the same prompt gives different answers (§5)
- system prompt, project instruction and user message (§6)
- fabrication (§7)
- layer map (§8)
- "On other tools" before the deliverable (§10)
- deliverable: the five-minute model on the case and as a template (Parts 1–2), and the diagnosis table on the case and as a template (Parts 3–4)
- "(Academy case)" label on first use (l.50)

The "Treated in" assignments (BW3, BW4, BW6) cannot be checked because no other BW brief is in the packet (unsure #1). The body is about 6,400 words and the deliverable about 2,700, above the brief's 2,000–6,000 guide. The brief allows what the topic needs, so this is not a finding.

## Findings

[error] [accuracy] §3 Across chats; Current: "**Memory** is on by default on the Free, Pro, Max and Ultra plans; on Team and Enterprise the organisation's owners decide."; Problem: the cited page names Free, Pro and Max only, with no Ultra. It also says memory is off for each Team/Enterprise member until they turn it on; Fix: "**Memory** is on by default on the Free, Pro and Max plans; on Team and Enterprise the organisation's owners decide whether it is available, and it is off for each member until they turn it on."; Basis: https://support.claude.com/en/articles/11817273-use-claude-s-chat-search-and-memory-to-build-on-previous-context ("Memory is on by default for Free, Pro, and Max plans…"; "owners control whether memory is available, and it's off for each member until they turn it on").

[should-fix] [attribution] §7; Current: "The authors work at OpenAI; the paper is a preprint,"; Problem: the cited arXiv page lists no affiliations. The pages that might state them refused the fetch, so this was not checked. My unsourced recollection is that Vempala is an academic; Fix: "The paper is a preprint,"; Basis: https://arxiv.org/abs/2509.04664.

[should-fix] [accuracy] §2 What a token is; Current: "On those two figures, an English token on a current Claude model is roughly 3.5 ÷ 1.3 ≈ 2.7 characters. That division is this unit's arithmetic; nobody measured it, the glossary gives no figure for other languages, and it points to Anthropic's token-counting endpoint for exact counts (same page)."; Problem: the vendor states a conversion for the current tokenizer, about 2.5 characters per token. The unit derives 2.7 instead and says no figure exists; Fix: "Anthropic's model page gives the current tokenizer's own conversion: 1M tokens is roughly 555k words or 2.5M Unicode characters, about 2.5 characters a token ([*Models overview*](https://platform.claude.com/docs/en/models/overview), read 15 Nov 2026; the per-token division is this unit's arithmetic). The glossary gives no figure for other languages, and points to Anthropic's token-counting endpoint for exact counts (same page)."; Basis: https://platform.claude.com/docs/en/models/overview ("1M tokens is roughly 555k words or 2.5M Unicode characters on the current tokenizer (introduced with Claude Opus 4.7)").

[should-fix] [label] §2 Liu et al.; Current: "The models tested date from 2023."; Problem: Part 6 requires the finding to name the models and the task tested, and the unit names neither. The abstract gives the tasks; the models are listed in the paper body, which I did not open; Fix: "The tasks were multi-document question answering and key-value retrieval; the models tested were released in 2023 (the paper lists them), and none is current." Then name the models from the paper's experimental section before filing; Basis: https://aclanthology.org/2024.tacl-1.9/.

[should-fix] [accuracy] §1; Current: "These numbers change; a unit written four weeks earlier on the same pages would have read different ones."; Problem: unsourced and not checkable by the reader. It rests on the private source unit (notes, Source error 1), which the brief bars; Fix: "These numbers change; check them on the vendor's page on the day you rely on them."; Basis: brief.txt ("never refer to the private course or its units"); sourcing-standard Part 1.

[should-fix] [attribution] Deliverable Part 1 ¶4; Current: "That is why Academy writes each unit in a fresh context that sees only its brief and the units already filed."; Problem: the case file's stated reason is repetition from leaked context, not attention or cost; Fix: "Academy writes each unit in a fresh context that sees only its brief and the units already filed; the reason it gives is that leaked context is how a course starts repeating itself."; Basis: Academy case file §2.

[should-fix] [label] Part 3, row "A cited page exists but does not say…"; Current: "| Documented practice in one project; no control (case file §9) |"; Problem: the anecdote is the sole support for a general recommendation; Fix: "| Documented practice (vendor): have the model find a supporting quote for each claim and retract any it cannot support, [*Reduce hallucinations*](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations.md); a separate reader is practice in one project, no control (case file §9) |"; Basis: https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations ("If it can't find a quote, it must retract the claim").

[should-fix] [accuracy] §10 instructions row, Gemini cell; Current: "Gems hold a name, instructions and files: [*Use Gems in Gemini Apps*](https://support.google.com/gemini/answer/15146780?hl=en) |"; Problem: Gems become read-only on personal accounts on 17 Nov 2026, two days after the read, and move to skills. The cited page carries a banner saying so; Fix: "Gems hold a name, instructions and files: [*Use Gems in Gemini Apps*](https://support.google.com/gemini/answer/15146780?hl=en); on personal accounts they move to skills from November 2026 (see the skills row) |"; Basis: https://support.google.com/gemini/answer/15146780?hl=en ("Starting in November 2026, Gems will go away on personal Google accounts and automatically transition to skills"); https://support.google.com/gemini/answer/18560919?hl=en.

[minor] [attribution] Sources; Current: "- Anthropic. *Models overview*. Claude Platform Docs. https://platform.claude.com/docs/en/about-claude/models/overview"; Problem: the page's canonical URL is /docs/en/models/overview; Fix: "- Anthropic. *Models overview*. Claude Platform Docs. https://platform.claude.com/docs/en/models/overview". Apply the same change to the in-text links; Basis: page metadata.

[minor] [accuracy] §8 Agents row; Current: "| Throughout a task; a subagent in its own fresh window |"; Problem: the page says a subagent starts fresh unless it is a fork, which copies the conversation; Fix: "| Throughout a task; a subagent in its own window, fresh unless forked from the conversation |"; Basis: https://code.claude.com/docs/en/how-claude-code-works.

[minor] [attribution] §5; Current: "and Opus 5.5 thinks adaptively, always on, so the amount of reasoning placed in the window varies with the request ([*Models overview*](https://platform.claude.com/docs/en/about-claude/models/overview), all read 15 Nov 2026)"; Problem: the variation is stated on Context windows, not Models overview. This resolves unsure #10; Fix: "and Opus 5.5 thinks adaptively, always on, so the amount of reasoning placed in the window varies with the request ([*Models overview*](https://platform.claude.com/docs/en/models/overview); [*Context windows*](https://platform.claude.com/docs/en/build-with-claude/context-windows), all read 15 Nov 2026)"; Basis: Context windows ("thinking token usage varies from request to request").

[minor] [figure] §1 tree caption; Current: "on Anthropic, <em>Context windows</em> and <em>System prompts</em> (platform.claude.com, read 15 Nov 2026)."; Problem: §1 does not cite System prompts, and the grouping is the unit's own; Fix: "on Anthropic, <em>Context windows</em> (platform.claude.com, read 15 Nov 2026); the grouping by who writes each part is this unit's."; Basis: unit §1 ll.16–18.

[minor] [figure] §9 decision; Current: "\"q\": \"Did a source support it?\","; Problem: the label rewords text item 3; Fix: "\"q\": \"Did it come from a source?\","; Basis: unit §9 item 3.

[minor] [label] Part 3 usage row; Current: "| Vendor documentation: [*How do usage and length limits work?*](https://support.claude.com/en/articles/11647753-understanding-usage-and-length-limits) | No instance in the case file (it holds no measure of usage spent, §9) |"; Problem: the page directly supports the new-chat change, but the cell does not say so; Fix: "| Vendor documentation: longer conversations that trigger automatic context management consume more of the limit, and the page suggests a new conversation; tools and connectors are token-intensive: [*How do usage and length limits work?*](https://support.claude.com/en/articles/11647753-understanding-usage-and-length-limits) | No instance in the case file (it holds no measure of usage spent, §9) |"; Basis: same page ("Longer conversations that trigger automatic context management consume more of your usage limit"; "Try starting a new conversation…").

[minor] [label] §9; Current: "Each answer points to a different change:"; Problem: the unit's own ordering method carries no evidence grade; Fix: "Grade: stated opinion (this unit's ordering, built on §1 to §7). Each answer points to a different change:"; Basis: sourcing-standard Part 6.

## Confirmed (PASS unless noted)

**Anthropic platform docs**
- *Context windows* (platform.claude.com/docs/en/build-with-claude/context-windows):
  - the definition, including the response
  - what counts: system prompt, messages, tool definitions, output and thinking
  - the "context rot" quotation, exact
  - full history every turn
  - each response becomes the next input
  - thinking blocks kept on Opus 4.5 and later
  - 1M window and 128K output for the four current models
- *Models overview* (/docs/en/models/overview):
  - prices $4/$20, $2/$10, from $0.10/$0.50 and $8/$40; output is five times input on every row
  - June 2026 reliable knowledge cutoff
  - Transparency Hub
  - "Adaptive (always on)"
- *Glossary*:
  - the window is distinct from the training corpus and is "working memory"
  - tokens: about 30% more on the 4.7+ tokenizer, 3.5 characters on earlier models, token counting
  - temperature; temperature 0 is not deterministic on first-party or cloud services
  - RAG: retrieval via tools; quality and relevance matter
  - pretraining, fine-tuning, RLHF
- *Using the Messages API*:
  - stateless; message threads in beta with a 5-minute expiry
  - temperature/top_p/top_k unsupported on 4.7+ (400 error), use prompting
  - a mid-conversation system message has the same authority
- *Agent Skills*: about 100 tokens per skill in the system prompt; body under 5k on trigger; files when read; the description is what requests are matched against.
- *System prompts*: claude.ai and mobile apps; current date; periodically updated; not the API.
- *Reduce hallucinations*:
  - the opening statement, "can drastically reduce"
  - quotes first, cite and retract, restrict to documents
  - best-of-N
  - reduces but does not eliminate

**Claude Code docs**
- *How Claude remembers your project*: fresh context per session; CLAUDE.md plus auto memory; under 200 lines, adherence; "context, not enforced configuration"; PreToolUse hook; specific and concise.
- *How Claude Code works*: older tool outputs cleared first, then summary; early instructions may be lost; put persistent rules in CLAUDE.md; MCP definitions deferred; gather/act/verify loop; the harness manages context; a subagent gets its own window and returns a summary.

**Claude Help Center**
- Window sizes: 1M / 500K / 200K, as the unit states.
- Usage: usage factors; one limit across surfaces; tools and connectors token-intensive; part of the window reserved for the reply; summarisation with history kept.
- Personalization: profile instructions apply to all chats, project instructions only to that project; usable independently or in combination; no precedence stated.
- RAG for projects: automatic near the limit; most relevant parts; 10x.
- Memory article:
  - topics; carried to the next chat
  - per-project scoping
  - sensitive topics not stored by default
  - deleting a chat leaves its memories
  - edit and delete
  - chat search on paid plans, as a tool call, with its scopes
  - how much is inserted is not stated
  - "Incognito chats are not used for memory" is only partly verified: the page as fetched speaks of chat search not pulling from incognito chats.
- Connectors: apps, data and actions; remote MCP.

**Other Anthropic pages**
- Rajasekaran, Dixon, Ryan, Hadfield (Applied AI team), 29 Sep 2025: n²; attention budget; "a finite resource with diminishing marginal returns", exact; smallest set of high-signal tokens.
- Consumer terms: headline; 28 Aug 2025; Free/Pro/Max; new or resumed chats; 5 years vs 30 days.
- Tracing thoughts, 27 Mar 2025: the circuits as described. Claude 3.5 Haiku is named in the introduction only (unsure #3 confirmed).

**Research**
- Liu et al.: authors, TACL 12, 157–173, doi, beginning/end vs middle finding.
- Chroma: Hong, Troynikov, Huber, 14 Jul 2025; 18 models; the five Claude models named; seven OpenAI models (unsure #5 resolved); unreliable with length, non-uniform, distractors.
- Holtzman et al.: authors; arXiv v2 14 Feb 2020; bland, repetitive; nucleus sampling.
- He / Thinking Machines, 10 Sep 2025: Qwen3-235B-A22B-Instruct-2507; 1,000 completions at temperature 0; 80 unique; 78 most common; diverged at token 103; identical with batch-invariant kernels; load and batch size.
- Kalai et al.: authors; 4 Sep 2025; binary classification; "reward guessing over acknowledging uncertainty", exact.

**OpenAI and Google**
- OpenAI *Conversation state*: stateless; chained input billed again.
- OpenAI *Prompt engineering*: developer messages ahead of user messages; snapshots differ; pinning; non-deterministic.
- OpenAI *Memory and new controls*: 13 Feb 2024, updated to 3 Jun 2025; deleting a chat keeps its memories; temporary chats use no memory.
- OpenAI *Using projects*: 10 Apr 2026; project-only memory.
- OpenAI *Custom instructions*: 20 Jul 2023; every conversation.
- Google *Long context*: several facts are found less accurately; query at the end. The "last updated 15 Oct 2026" date is unverifiable because the .md.txt copy has no date.
- Google *Save info*: settings or by asking; past chats.
- Google transition page: skills are "reusable custom instructions", applied when relevant; read-only 17 Nov 2026, removed 17 Dec 2026, personal accounts 18+ (unsure #8 confirmed).

**Arithmetic and case facts**
- Arithmetic: 110,000; 420,000; 930,000; 20 × 100 = 2,000. All correct.
- Academy facts all trace to the case file: §2, §3 (23/91, nothing invented, qualifiers), §4, §5 (36 units, 28 with errors, 58 errors, kinds named), §7 (restarts, "fable", 17 findings, BW4), §9.

## Figures (section 7)

1. **tree, §1.** Every label is in l.18. The kind fits a hierarchy. **FIX (minor)**: caption. Replacement: "What reaches the context window, grouped by who writes it, from §1 of this unit, on Anthropic, <em>Context windows</em> (platform.claude.com, read 15 Nov 2026); the grouping by who writes each part is this unit's."
2. **line, §2.** x [1,10,20,30] and values [2,110,420,930] trace to l.62. The caption says illustrative and unmeasured, and names the section and source. The kind fits a trend. **PASS**.
3. **decision, §9.** Questions and outcomes trace to ll.227–233. The caption names §9 as the unit's own reasoning. The kind fits a rule with branches. **FIX (minor)**: replace `"q": "Did a source support it?",` with `"q": "Did it come from a source?",`.

## (8) The writer's Source errors list (notes.md)

1. **Confirmed.**
2. **Confirmed.** Also: any model from API version 2026-10-21 rejects the sampling parameters.
3. **Confirmed.**
4. **Confirmed** for "Using the Messages API", "Agent Skills" and "Updates to Consumer Terms and Privacy Policy". "How do usage and length limits work?" is confirmed by URL slug only.
5. **Confirmed.** Also: a thread is deleted within 1 hour.
6. The arXiv page names no venue: confirmed. ICLR is **not confirmed**: the iclr.cc page showed no conference name. The arXiv v2 citation stands.
7. **Not confirmed.** Both statements are on the pages:
   - The memory article lists "government ID numbers, criminal history, financial account numbers, and immigration status".
   - The usage article says "Longer conversations that trigger automatic context management consume more of your usage limit" and "Try starting a new conversation if you're approaching your usage limit in a longer chat."
   - Deleting them from B1 would be wrong.

**Needs list.** Sound. Need 1 (course map) and Need 2 (case facts) are real. Need 3 items are confirmed. Add one item: BW1 should apply the Gems caution in its own §10 (should-fix above).

## (9) Part 6, line by line

- Sourced where made: yes, except the "four weeks earlier" line.
- Source types labelled: yes.
- Evidence grades: yes, except the §9 ordering (minor).
- Models and task named:
  - He and the Anthropic interpretability work: yes.
  - Chroma: models named, tasks not.
  - Liu: neither (should-fix).
  - Transfers to current models are marked as inference.
- Product facts dated: yes.
- "On other tools": present, with one stale Gems cell.
- Carried-over claims re-verified: yes. The conclusion of Source error 7 is wrong, but BW1 does not depend on it.
- No private-reader detail: none found. The only implicit private-course reference is the "four weeks earlier" line.
- Academy facts: all trace to the case file and are labelled. Part 3 row 5 rests on the anecdote alone (should-fix).
- No invented figures or quotations: none found. Every quotation checked is exact.
- Deliverable on the case, then as a template with described blanks: yes.
- Not advice without evidence: passes.
- Links given as links: yes.

## (10) Read as the brief's persona

- Nothing assumes the private course's reader. No private term reaches the unit apart from the "four weeks earlier" line.
- Some case terms are not explained: "deep dive", "writer agents … container restarts", "the method names". A non-coder would need a gloss on "container".
- The API material (message threads, `temperature`) is developer-facing, but the unit says what it means for a chat user.
- The §10 table (4 columns) and the Part 3 table (6 columns) are hard to read on a phone. This is a style point, not a finding.

## (11) Attribution pass

- Every source title matches its page's headline. Help-centre titles were matched by headline or slug. The Models overview URL is not canonical (minor).
- All quotations are exact and credited to the right speaker.
- Every figure matches the page that states it, except the token-character ratio (should-fix).
- Two credits go beyond their sources: "The authors work at OpenAI" is unsupported (should-fix), and "That is why Academy…" gives the case a reason the case file does not state (should-fix).

## Verdict

BW1 · fix · error 1, should-fix 7, minor 7
