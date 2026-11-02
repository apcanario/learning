---
audit: fresh check
unit: B8 · Cost, limits, hygiene
course: brand-ai · B · Using AI to Build a Brand
model: Opus 5.5 (search on; a Fable 5.1 fresh check is owed, deferred by Pedro 31 Oct 2026 to the Fable stage)
date: 2026-11-02
chat: own Opus 5.5 agent context, not shown the writing (P31), in session https://claude.ai/code/session_01KMmgR1vGhZ8nCLyF55jNsY
verdict: rewrite by the count rule (4 errors), 4 should-fix, 4 minor; every error is a one-sentence replacement listed below, and two of the four share one cause
---

# Fresh check · B8 · Cost, limits, hygiene

**A Fable 5.1 fresh check of B8 is still owed.** Pedro deferred Fable 5.1 checks to a later stage on 31 Oct 2026, so Opus 5.5 ran this check in an isolated context (P31) on 2 November 2026. The checker did not see the writing and edited no file.

**What was read first:**
- `docs/sourcing-standard.md`, Parts 1 and 2.
- B8's brief as Academy shows it: `PRE`, with `{GOAL}` replaced by `GOAL_B`, then B8's own brief from `units_data.py`.
- `audits/brand-ai/audit-1.html` and `audit-2.md`.
- The unit in full. The check copy is identical to `courses/brand-ai/B8-cost-limits-hygiene.md` (checked with `diff`).
- For the pointers: the filed units B1, B2, B3, B4, B5, B6, B7, A4, A8 and DD-B3.

**Method:**
- Web: WebSearch first. WebFetch was used only on URLs a search in this agent returned.
- Every Current below was checked with `grep -F -c` and occurs exactly once in its file.
- Every calculation was re-run by script.

## (1) Coverage

- **Current plan limits and how usage windows work, searched and dated:** covered (§1). Searched on 2 Nov 2026 rather than in October. Dated throughout.
- **What burns usage for no gain:**
  - Re-reading large files: covered (§2).
  - Giant pastes: covered (§2).
  - Chats that never end: covered (§2).
  - Re-running research: covered (§2).
- **When a new chat is cheaper:** covered (§3).
- **Token budgets per task type:** covered (§4).
- **Privacy and retention of memory and projects:** covered (§5). Thin on project files. Anthropic's pages give no retention period for them, and the unit says so (unsure 7). Two privacy-centre pages failed to load (unsure 6).
- **What should live only in the vault:** covered (§5, table and matrix).
- **Deliverable, usage rules as additions to his way-of-working file:** present (rules 11 to 24).

## (2)–(7) Findings

[error | accuracy] §3, Model and effort; Current: `In Claude Code, "each model has its own cache" and "each effort level has its own cache for the same model", so switching either mid-session "recomputes the entire request"; the page's tip is to "Pick your model and effort level at the top of a session" (*How Claude Code uses prompt caching*).`; Problem: The second quotation is not on the page. The page says "on most models, each effort level has its own cache", and then makes an exception that covers every model the course uses: "On Opus 5.5, Sonnet 5.5, Haiku 5.5, and Fable 5.1 with an API key or a Claude subscription, the cache stays intact by default". It adds that changing effort on these models "keeps the cache". So an effort switch does not recompute the request for him. Only a model switch does.; Fix: `In Claude Code, "each model has its own cache", so a model switch mid-session "recomputes the entire request even when the content is identical"; an effort change does the same "on most models", but on Opus 5.5, Sonnet 5.5, Haiku 5.5 and Fable 5.1 with a Claude subscription "the cache stays intact by default". The page's tip is still to "Pick your model and effort level at the top of a session" (*How Claude Code uses prompt caching*).`; Basis: Claude Code docs, *How Claude Code uses prompt caching*, https://code.claude.com/docs/en/prompt-caching, read 2 Nov 2026 (section "How the cache is organized" and section "Changing effort level").

[error | deliverable] Deliverable, rule 11; Current: `In Claude Code each model and each effort level has its own cache, and a switch recomputes the whole request; on claude.ai the effect is undocumented, and the rule costs nothing.`; Problem: The rule's stated ground repeats the §3 error. On a subscription, an effort switch on the 5.5 models and Fable 5.1 keeps the cache. The rule itself (set both before the first message) can stand on the model-switch cost, on the claude.ai unknown and on B2's rule.; Fix: `In Claude Code a model switch recomputes the whole request, and an effort switch does too on most models, though not on the 5.5 models or Fable 5.1 on a subscription; on claude.ai the effect is undocumented, and the rule costs nothing.`; Basis: as above, https://code.claude.com/docs/en/prompt-caching.

[error | accuracy] §3, What caching changes; Current: `Anthropic's own product draws the conclusion: on Pro or Max, when a large Claude Code session is resumed after a long break, Claude Code "offers to resume from a summary" so that later requests do not carry the full history (*How Claude Code uses prompt caching*). That is a new chat with a handoff note, built into the tool.`; Problem: The cited page was fetched in full twice. It does not contain "offers to resume from a summary" and does not mention Pro or Max. A search for the phrase on Anthropic's documentation returned no Anthropic page. What the page does document is idle compaction before the cache expires.; Fix: `Anthropic's own product points the same way: if a long conversation sits idle in a terminal session on the one-hour cache, Claude Code "can compact it shortly before the cache expires", so the summary is written while the history is still cheap to read (*How Claude Code uses prompt caching*). That is a handoff note, written by the tool.`; Basis: https://code.claude.com/docs/en/prompt-caching, read 2 Nov 2026 (section "Compacting the conversation": "If you leave a long conversation idle in a terminal session while it is on the one-hour TTL, Claude Code can compact it shortly before the cache expires.").

[error | figure] §3, decision figure; Current: `When it does and the cache is warm, stay; in Claude Code, `/rewind` off a wrong path and `/compact` only between tasks.`; Problem: The figure's outcome "Claude Code: /rewind. claude.ai: new chat" has a claude.ai branch that the unit's text never states. The prose rule gives `/rewind` for Claude Code only. A figure may add no fact. The fix puts the claude.ai branch into the prose, where it follows from §3's own finding that claude.ai documents no hand trim. If the maintainer prefers to change the figure instead, see (7).; Fix: `When it does and the cache is warm, stay; in Claude Code, `/rewind` off a wrong path and `/compact` only between tasks; on claude.ai, where no help article read describes a way to trim a chat by hand, a wrong path means a new chat.`; Basis: the unit's §3 ("On claude.ai no help article read describes a way to trim a chat by hand"); sourcing-standard Part 1, "A figure adds no fact".

[should-fix | accuracy] §1, Where sources disagree; Current: `Two pages against one, and the more specific page is the recently updated one: this unit takes 1M as the window for the four current models in claude.ai chat, and flags it (unsure list, 1).`; Problem: The Max article is cited in the same §1 and labelled "Updated this week". It still says "the context window size remains at 200K across all plans". So the count is two pages against two, and both 200K pages are not the stale undated one. The decision can stand. The count and the description cannot.; Fix: `The Max plan article, also labelled "Updated this week", still says "the context window size remains at 200K across all plans" (article 11014257). Two pages against two; the most specific page is recently updated and the pricing page agrees with it, so this unit takes 1M as the window for the four current models in claude.ai chat, and flags it (unsure list, 1).`; Basis: Claude Help Center, *About Claude's Max plan usage*, https://support.claude.com/en/articles/11014257-about-claude-s-max-plan-usage, read 2 Nov 2026.

[should-fix | accuracy] Writer's unsure list, item 1; Current: `article 11647753 (undated) still says 200K across all models and paid plans. The unit takes 1M; which page Anthropic will correct is unknown.`; Problem: This leaves out the Max article's 200K, as in the finding above.; Fix: `article 11647753 (undated) and the Max article 11014257 (updated this week) still say 200K across all plans. The unit takes 1M; which pages Anthropic will correct is unknown.`; Basis: as above.

[should-fix | deliverable] §4, budget table, "One current fact" row; Current: `| The fact filed with source and date; never searched twice |`; Problem: "Never" contradicts two things: the method's six-month staleness check (`method.md` §6, which re-searches every fact that can change), and the unit's own deliverable preamble ("re-read the sources at the staleness check").; Fix: `| The fact filed with source and date; searched again only at its staleness check |`; Basis: `docs/method.md` §6 (staleness check); the unit's Deliverable preamble.

[should-fix | deliverable] Deliverable, rule 18; Current: `> 18. **A fact is searched once.** Found, it is filed with its source and date, and the next chat reads the file.`; Problem: This is the same contradiction with the staleness check.; Fix: `> 18. **A fact is searched once, until its staleness check.** Found, it is filed with its source and date, and the next chat reads the file; it is searched again only at the six-month staleness check (method §6).`; Basis: as above.

[minor | accuracy] §1, Where sources disagree; Current: `gives a table for Claude chat in which Fable 5.1, Opus 5.5, Sonnet 5.5 and Haiku 5.5 have 1M tokens, Fable 5 and Opus 4.6 to 4.8 have 500K`; Problem: The page's table also gives 1M to Opus 5 and Sonnet 5, and 500K to Sonnet 4.6. The list as written reads as complete.; Fix: `gives a table for Claude chat in which Fable 5.1, Opus 5.5, Opus 5, Sonnet 5.5, Sonnet 5 and Haiku 5.5 have 1M tokens, Fable 5, Opus 4.6 to 4.8 and Sonnet 4.6 have 500K`; Basis: Claude Help Center, *How large is the context window on paid Claude plans?*, https://support.claude.com/en/articles/8606394-how-large-is-the-context-window-on-paid-claude-ai-plans, read 2 Nov 2026.

[minor | coverage] §1, plans table, Max row; Current: `| Max | $100 a month | "5x Pro usage every 5 hours and every week" | Included, "up to half your weekly limit" |`; Problem: The pricing page now lists a monthly API credit on Max ($100) and Ultra ($200). This bears on cost. The unit does not mention it.; Fix: `| Max | $100 a month, with "$100 a month in API credits to build on the Claude Platform" | "5x Pro usage every 5 hours and every week" | Included, "up to half your weekly limit" |`. In the Ultra row, replace `| Ultra | $200 a month |` with `| Ultra | $200 a month, with $200 a month in API credits |`. That shorter Current also occurs once.; Basis: Claude, *Plans & pricing*, https://claude.com/pricing, read 2 Nov 2026 (Max card; Ultra card: "$200 a month in API credits, up from $100 on Max").

[minor | label] §4, budget table header; Current: `| Task type | Route (B6 A) |`; Problem: Three rows give "routes" that B6 Deliverable A does not have: "Writing chat", "Fresh chat" and "Claude Code". The header implies all seven are B6's.; Fix: `| Task type | Route (B6 A where it applies) |`; Basis: B6 Deliverable A (`courses/brand-ai/B6-research-and-verification.md`, lines 298–309).

[minor | figure] §5, matrix caption; Current: `A8 R15 and R19 to R22, B4 F13 and F15, and B5 §5."`; Problem: The caption leaves out the source of the employer row, which is the consumer-terms post together with "my rule".; Fix: `A8 R15 and R19 to R22, B4 F13 and F15, B5 §5, and Anthropic's consumer-terms post (28 Aug 2025) with the writer's own rule for employer material."`; Basis: the unit's §5 table, "Employer material" row.

**Public-site rules:** no breach.
- No personal fact beyond the brief and the filed units: weight and ADHD are in the brief, and "biometrics" is in A3, B2 and B5.
- Privacy is treated as categories and rules. §5 says "No inventory of what he has stored is made here."
- No private person is named. B4 F15's private terms are not repeated.
- Nothing from his memory, Projects or chats is quoted or described.
- The employer is referred to only as "his employer" or "employer material".

**Style:** no "not X but Y" constructions found. The body is about 6,500 words without figures, inside the brief's range.

**Arithmetic:** every calculation was re-run by script and all come out.
- The 17 filed units excluding B8 hold 973,729 characters (Unicode).
  - About 360,600 tokens at 2.7 characters per token.
  - About 278,200 tokens at 3.5.
  - About 36% of 1M.
- Mean unit: 57,278 characters, about 21,214 tokens.
- Largest unit: B3, 83,280 characters, about 30,844 tokens.
- Four average units: 84,857 tokens, about $0.849 at $10 per million.
- Five average units: about 106,071 tokens.
- History sums:
  - 2,000 × (1 + … + 30) = 930,000.
  - 110,000 + 130,000 + 130,000 = 370,000, which is 60.2% less.
- API costs on 4,000 in and 1,500 out:
  - Opus 5.5 at $4/$20: $0.046.
  - Sonnet 5.5 at $2/$10: $0.023.
- 336,000 tokens against 1M is about a third.

## (6) Errata and pointers

**Audit errata:** Audit 1 and Audit 2 contain no erratum that touches B8. Audit 1's course-wide consequence (a fresh checker for every later Brand + AI unit) is met by this check.

**(a) B1 line 144, "Treat it as unknown. Usage rules are B8."**
- B8 §1, "B1 §2's caching question", answers it by name. The answer is partial: caching cuts the draw for project content and Claude Code history, by an amount Anthropic does not publish.
- B1's text is reported correctly. The line sits in B1 §2.
- B1's pointer still reads true, since B8 gives usage rules (11–24).
- Optional sharpening, not required: in B1, replace `Treat it as unknown. Usage rules are B8.` (occurs once) with `Treat it as unknown here; B8 §1 gives what Anthropic states, and B8's deliverable the usage rules.`

**(b) B1 §4 line 197, "B2 and B8 are flagged to search before writing".**
- B8 §1 names it. Every plan fact is searched and dated 2 Nov 2026.
- B8's phrasing "left B8 the rule" slightly overstates B1, which explains why B8 is flagged.
- The pointer reads true.

**(c) B1 line 290, "trim the window or start a new chat".**
- B8 §3 quotes it exactly and places it correctly in B1 §7 ("Reading a bad output").
- §3 answers both halves: trimming (none by hand on claude.ai; `/rewind`, `/compact` and `/clear` in Claude Code) and when a new chat is cheaper.
- The pointer reads true.

**(d) B4 F15, "B8 sets the general privacy rules".**
- B8 §5 and rules 22–24 answer it by name. B8 reports F15 correctly: private terms in the public build, and GitHub's warning that commits may persist.
- The pointer reads true.

**(e) DD-B3's ten operating rules.**
- B8 numbers on from them (11–24) and says which DD-B3 rule each refines.
- No B8 rule contradicts a DD-B3 rule. Checked against rules 6, 8, 9 and 10.
- Rule 18 as written contradicts the method's staleness check (should-fix above), not a DD-B3 rule.

**(f) B6 Deliverable A.** B8 §4 re-checks it by name. Every cost B6 quotes still holds on 2 Nov 2026:
- $0.046 on Opus 5.5.
- $10 per 1,000 searches.
- 4× and 15× (Hadfield et al.).
- "Can use up your limits faster" (*Use research on Claude*).

B8's budgets agree with B6 and add no cost figure. B6 has no pointer to B8, so nothing in B6 needs changing.

**(g) B2 §2.**
- B8 re-reads it claim by claim. It dates B2's sources to 28 Oct 2026 and the usage-limit article to 22 Sep 2026, both correctly.
- It marks as changed: the $200 tier (now Ultra) and the 200K window (disputed).
- B2 has no pointer to B8.

**Stale lines elsewhere.** These are observations for Pedro, not B8 findings. Each Current occurs once in its own file; propose them as a staleness row if wanted:
- B2 §2, `The window stays at 200K tokens on every plan`, is disputed as of 2 Nov 2026 (B8 §1).
- B2 §2, `and $200 for twenty times`: the $200 tier is now Ultra, "10x Pro usage every week".
- B1 §1, `His Project runs on claude.ai, so his working budget is 200K tokens, a fifth of the figure on the model page.`, is disputed in the same way.
- B4 F1's "against a 200K window" premise: B8 §1, consequence 3, already records it as undetermined.

## (7) Figures

1. **Matrix, §1 (B2 §2's claims re-read): PASS.**
   - Every row label and status traces to the §1 table, including "Ultra, 10x weekly" and "up to 1M, disputed".
   - The caption names the section and the sources.
   - Matrix fits items by status.
2. **Compare, §3 (930 against 370): PASS.**
   - Both values and labels trace to "The arithmetic" paragraph.
   - The caption names §3, B1 §2 and *Context windows*, and labels the data unmeasured and uncached.
   - Compare fits numbers compared.
3. **Decision, §3: FIX.**
   - The outcome "Claude Code: /rewind. claude.ai: new chat" has a claude.ai half that the text does not state.
   - The error finding above fixes it in the prose. If that prose fix is not applied, replace the figure line `{"label": "yes", "to": {"outcome": "Claude Code: /rewind. claude.ai: new chat", "tone": 2}},` with `{"label": "yes", "to": {"outcome": "Claude Code: /rewind", "tone": 2}},`.
   - Every other label traces to "The rule, put together". The caption names §3 and its three sources. Decision fits a rule with branches.
4. **Matrix, §5 (where material may live): PASS on labels and kind. Caption minor (above).**
   - Every cell traces to the §5 table. "Passwords, keys, card and ID numbers" drops the table's "bank", which shortens the label without adding a fact.

## Confirmed

**Pricing page and plan articles**
- Claude, *Plans & pricing* (https://claude.com/pricing):
  - Pro $20, or $17 billed as $200 a year.
  - Max $100, "5x Pro usage every 5 hours and every week", Fable "up to half your weekly limit".
  - Ultra $200, "No 5-hour limit", "10x Pro usage every week".
  - FAQ: "rolling five-hour session window", "no fixed message count", "How fast you reach a limit depends on…", "at least 5x more usage per 5-hour session than Free", Claude Code "shares the same usage limits".
  - Context window "Up to 1M", "varies by model".
- *What is the Ultra plan?* (https://support.claude.com/en/articles/17728952):
  - "Updated this week".
  - Max 20x is now Ultra at the same price.
  - Verified accounts have no five-hour limit; unverified accounts have a temporary one.
  - Weekly limit across all models plus a separate weekly Fable limit.
- FourWeekMBA (https://fourweekmba.com/ai-claude-ultra-drops-5-hour-limit-for-verified-users-at-200/): dated 30 Oct 2026, attributes the change to an @claudeai X post that day. Digg's summary (https://digg.com/ai/e1dnwnjk) agrees on the date and adds Max 5x → Max.
- *About Claude's Pro plan usage* (https://support.claude.com/en/articles/8324991-about-claude-s-pro-plan-usage):
  - "Updated over a week ago"; resets every five hours.
  - "may limit your usage in other ways…".
  - 45 messages, 200 sentences, "often more depending on Claude's current capacity".
  - "When you add documents to a project, they're cached"; "cached tokens count less…".
  - "Don't re-upload files within the same conversation".
- *About Claude's Max plan usage* (https://support.claude.com/en/articles/11014257-about-claude-s-max-plan-usage): "Updated this week"; still 5x and 20x; "at least 900 messages".

**Usage, context-window and effort articles**
- *Understanding usage and length limits* (https://support.claude.com/en/articles/11647753-understanding-usage-and-length-limits):
  - No date shown.
  - 200K across all models and paid plans; 500K on some Enterprise models.
  - One shared limit across claude.ai, Claude Code and Desktop.
  - "Tools and connectors are token-intensive"; disable web search, Research and connectors when not needed.
  - "Longer conversations that trigger automatic context management consume more of your usage limit"; with code execution on, it summarises earlier messages.
- *How large is the context window on paid Claude plans?* (https://support.claude.com/en/articles/8606394-how-large-is-the-context-window-on-paid-claude-ai-plans): "Updated this week"; 1M and 500K table; "Outside of these models, Claude's context window size is 200K".
- *Usage limit best practices* (https://support.claude.com/en/articles/9797557-usage-limit-best-practices):
  - "Updated this week".
  - The eight listed factors are verbatim.
  - The caching heading; "Claude remembers context from earlier in the conversation".
  - "Caches expire after a period of inactivity"; "counts that content in full again".
  - Usage bars, with Fable where the plan includes it.
  - "Provide all relevant data in a single, well-structured message".
- *Change the model, effort and extended thinking settings* (https://support.claude.com/en/articles/8664678-change-the-model-effort-and-extended-thinking-settings): "Updated over 3 weeks ago"; both effort quotes; "can change the model, effort level, or thinking setting at any point"; no mention of cache.
- *Claude Fable models on your plan* (https://support.claude.com/en/articles/15424964-claude-fable-models-on-your-plan): "Updated today"; Pro on credits; Max up to 50% of the weekly limit. It groups Ultra with Max in the regular pool, so the disagreement in unsure item 4 is confirmed.
- *Manage usage credits for paid Claude plans* (https://support.claude.com/en/articles/12429409-manage-usage-credits-for-paid-claude-plans): "Updated yesterday"; Pro, Max and Ultra; prepaid; standard API rates; monthly spend limit; "Adjust limit".
- *RAG for projects* (https://support.claude.com/en/articles/11473015-retrieval-augmented-generation-rag-for-projects): "Updated this week"; quote exact; no threshold given.
- *Use research on Claude* (https://support.claude.com/en/articles/11088861-use-research-on-claude): "Updated yesterday"; "can use up your limits faster due to Claude retrieving multiple sources".

**API and Claude Code documentation**
- Anthropic, *Context windows* (https://platform.claude.com/docs/build-with-claude/context-windows): "Contains all previous conversation history plus the current user message"; both context-rot sentences; "Cached prompt prefixes still occupy the context window…".
- Anthropic, *Prompt caching* (https://platform.claude.com/en/docs/build-with-claude/prompt-caching): 0.05× for Opus 5.5 and Sonnet 5.5; 0.025× for Fable 5.1; five-minute default and one-hour option; no mention of claude.ai.
- Anthropic, *Pricing* (https://platform.claude.com/docs/en/about-claude/pricing): Opus 5.5 $4/$20; Sonnet 5.5 $2/$10; Fable 5.1 $10/$50; "$10 USD per 1,000 searches" plus token costs.
- Claude Code docs, *Manage costs effectively* (https://code.claude.com/docs/en/costs):
  - "re-reads that history at the cached token rate, so a one-line question…".
  - "minimal file reads"; the 10,000-line log, "tens of thousands of tokens to hundreds".
  - "/clear costs nothing"; "Stale context wastes tokens on every subsequent message".
  - "Aim to keep CLAUDE.md under 200 lines".
  - "your first message after a break longer than the cache lifetime misses the cache and reprocesses your full context".
- Claude Code docs, *How Claude Code uses prompt caching* (https://code.claude.com/docs/en/prompt-caching):
  - A one-hour TTL for the main conversation "only on a Claude subscription within your plan's included usage", dropping to five minutes on usage credits.
  - `/rewind` truncates to a cached prefix.
  - The `/compact` summary request reads the whole history, cheaply while warm and at full price after a break.
  - "at a natural break in your work, such as between tasks".
  - "Pick your model and effort level at the top of a session".

**Vendor research post**
- Hadfield et al., Anthropic Engineering, 13 Jun 2025 (https://www.anthropic.com/engineering/multi-agent-research-system): six authors as listed; "about 4× more tokens than chat interactions"; "about 15× more tokens than chats".

**Privacy, memory, projects and incognito**
- Anthropic Privacy Center, *How long do you store my data?* (https://privacy.claude.com/en/articles/10023548-how-long-do-you-store-my-data):
  - Dated 1 July 2026; covers Free, Pro, Max and Claude Code on those accounts.
  - "as long as reasonably necessary".
  - Deleted chats leave history at once and back-end storage within 30 days.
  - Training on: up to 5 years de-identified. Training off: not used for future training; data already in runs stays.
  - Policy violations: inputs and outputs 2 years, classifier scores 7 years. Feedback: 5 years.
  - Says nothing on memory, projects or files.
- *How do I change my model improvement privacy settings?* (https://privacy.claude.com/en/articles/12109829-how-do-i-change-my-model-improvement-privacy-settings): dated 3 Aug 2026; toggle under Settings > Privacy; off means new chats are not used for future training.
- Anthropic, *Updates to our consumer terms* (https://www.anthropic.com/news/updates-to-our-consumer-terms): 28 Aug 2025; five years if training is allowed, else the existing 30 days; new or resumed chats only; excludes Claude for Work, Government, Education and the API.
- *I would like to input sensitive data…* (https://support.claude.com/en/articles/8325621-i-would-like-to-input-sensitive-data-into-my-chats-with-claude-who-can-view-my-conversations): "Updated this week"; "Access is limited to a small number of personnel involved in model training"; de-linked from user ID; trust-and-safety quote; the caution list.
- *Use Claude's chat search and memory…* (https://support.claude.com/en/articles/11817273-use-claude-s-chat-search-and-memory-to-build-on-previous-context):
  - "Updated this week"; topics quote.
  - Project memory "alongside" account memory, "but not memory from other projects"; "Use account memory".
  - Sensitive topics excluded by default; "Include sensitive topics in memory".
  - The never-saved list.
  - Deleting a chat leaves its memory entries; Settings > Your Claude, "Manage" next to "Your memory".
  - The amount loaded into a chat is not stated.
- *How can I create and manage projects?* (https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects): "Updated this week"; context-sharing quote; nothing on retention or training.
- *Use incognito chats* (https://support.claude.com/en/articles/12260368-use-incognito-chats): "Updated this week"; not in history or memory; 30 days; not trained on; outside projects only; cannot be reopened.

**Filed units, as B8 reports them**
- B1 §1 (200K, a fifth of 1M), §2 (2.7 characters per token; 930,000), §4 and §7.
- B2 §2 (the closing phrase, 22 Sep 2026), §5 ($0.046 and $0.023), §7 (claude.ai effort undocumented), and the light-chat rule.
- B3 §4 (Laban et al.).
- B4 §1 memory row; §3 cold fetch, 1,600 tokens; §4 "Work has paused briefly"; F1 (336,000); F13; F14 "On demand"; F15.
- B5 §3 (19 descriptions, about 2,300 tokens) and §5.
- B6 §1 and Deliverable A.
- B7 step 9; A4 publish list; A8 R15 and R19–R22.
- DD-B3 rule 8 wording.

**Unverifiable (not checked)**
- "Five-hour limits raised at the Opus 5.5 launch": no search returned Anthropic's launch page (the unit says the same). Only secondary reports came back.
- GitHub Docs: the unit cites it as not re-checked, and it was not opened here.
- Windows Report: the fetch failed.

B8 · verdict rewrite (more than three errors: 4; two share one cause, and every error is a one-sentence replacement above, so the list of edits fixes the unit; Pedro decides whether the count or the edit list governs) · error 4 · should-fix 4 · minor 4
