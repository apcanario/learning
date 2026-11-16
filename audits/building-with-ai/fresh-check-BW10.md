---
audit: fresh check
unit: BW10 · Cost, limits, privacy
course: building-with-ai · Building with AI
model: claude-opus-5-5
date: 2026-11-16
chat: https://claude.ai/code/session_01KMmgR36FFxqBvGbNsHzyhJ
verdict: fix · 0 errors, 0 should-fix, 0 minor
---

The checker's final report, verbatim, from its hand-back. Saved before any finding was applied.

Verdict: BW10 · fix · 0 error, 7 should-fix, 11 minor

claude-opus-5-5

# BW10 · Fresh check (Opus 5.5, 16 Nov 2026)

The harness refused the write to out/report.md, so the full report follows.

Packet read: unit.md, brief.txt, sourcing-standard.md (Part 1, Part 6), case-academy.md, notes.md, unsure.md and §3 of audit-units-SKILL.md. There was no audit report, so that step was skipped as instructed. I followed the web rule: every page I fetched was at an address that a WebSearch in this agent returned verbatim. For three pages the unit cites, search never returned the bare address, so they are "unverifiable" (not checked), not FAIL:
- Claude *Pricing*: search returned only https://claude.com/pricing?m=1.
- Claude Code *Manage costs effectively*: search returned only `?ref=t01.li` and `.md` copies.
- Claude Code *Automate work with scheduled tasks*: search returned only `?mode=reply`.

## Findings

should-fix [accuracy] §6 retention table; Current: "| Training off | 30 days | Consumer terms post, 28 Aug 2025 |"; Problem: the row presents a 30-day retention for kept chats with training off as a current fact. The current retention page (1 Jul 2026) gives no period for kept chats with training off beyond "as long as reasonably necessary", and gives 30 days only for deleted chats. The 30 days is the 2025 post's wording, and the row conflicts with the row above it ("A chat you keep"); Fix: "| Training off (a chat you keep) | \"Our existing 30-day data retention period\" in the 2025 post; the 2026 retention page gives no period beyond \"as long as reasonably necessary\", and 30 days only for a deleted chat | Consumer terms post, 28 Aug 2025; retention page, 1 Jul 2026 |"; Basis: Anthropic Privacy Center, How long do you store my data?, https://privacy.claude.com/en/articles/10023548-how-long-do-you-store-my-data (read 16 Nov 2026); Anthropic, Updates to Consumer Terms and Privacy Policy, https://www.anthropic.com/news/updates-to-our-consumer-terms
should-fix [attribution] §6 Commercial plans; Current: "([Anthropic Privacy Center, *Is my data used for model training?*](https://privacy.claude.com/en/articles/7996868-how-long-do-you-store-my-organization-s-data), 18 Aug 2026"; Problem: the URL slug names a different article, "How long do you store my organization's data?", which the page itself lists as a related article. The article's own address carries its headline; Fix: "([Anthropic Privacy Center, *Is my data used for model training?*](https://privacy.claude.com/en/articles/7996868-is-my-data-used-for-model-training), 18 Aug 2026"; Basis: https://privacy.claude.com/en/articles/7996868-is-my-data-used-for-model-training (headline "Is my data used for model training?", 18 Aug 2026)
should-fix [attribution] §9 On other tools; Current: "| Work accounts under other terms (§8) | [*Is my data used for model training?*](https://privacy.claude.com/en/articles/7996868-how-long-do-you-store-my-organization-s-data)"; Problem: the same slug mismatch as above; Fix: "| Work accounts under other terms (§8) | [*Is my data used for model training?*](https://privacy.claude.com/en/articles/7996868-is-my-data-used-for-model-training)"; Basis: https://privacy.claude.com/en/articles/7996868-is-my-data-used-for-model-training
should-fix [attribution] Sources; Current: "Anthropic Privacy Center. *Is my data used for model training?* 18 August 2026. https://privacy.claude.com/en/articles/7996868-how-long-do-you-store-my-organization-s-data"; Problem: the same slug mismatch as above; Fix: "Anthropic Privacy Center. *Is my data used for model training?* 18 August 2026. https://privacy.claude.com/en/articles/7996868-is-my-data-used-for-model-training"; Basis: https://privacy.claude.com/en/articles/7996868-is-my-data-used-for-model-training
should-fix [accuracy] §2 Research run twice; Current: "The only multiple Anthropic has published is for its 2025 system:"; Problem: the unit itself cites a second published multiple: agent teams at about 7× a standard session (*Manage costs effectively*, §4 table). As written, the sentence is false within the unit; it holds only for research; Fix: "The only research multiple Anthropic has published is for its 2025 system:"; Basis: unit §4 table, Agent run row; Hadfield et al., https://www.anthropic.com/engineering/multi-agent-research-system
should-fix [label] Deliverable Part 2; Current: "| Private terms (the owner's details, the private courses' names) |"; Problem: the case file does not say what the private-terms list contains (its §7 note says only "checked by a script against a list"). The gloss is an inference about the case, and it names private courses, which the brief says a unit never refers to; Fix: "| Private terms (the list the case file's §7 note names) |"; Basis: Academy case file §7 note and header; brief ("never infer a fact about the case that the file does not hold"; "never refer to the private course")
should-fix [coverage] §9 On other tools; Current: "| Cache lifetimes and prices (§5) | [*Prompt caching*](https://platform.claude.com/docs/build-with-claude/prompt-caching); [*How Claude Code uses prompt caching*](https://code.claude.com/docs/en/prompt-caching) | Not checked for this unit | Not checked for this unit |"; Problem: the brief requires each Claude-specific claim to be matched to the other vendor's documentation, or to "no equivalent found". Both vendors document API caching on pages that load; Fix: "| Cache lifetimes and prices (§5) | [*Prompt caching*](https://platform.claude.com/docs/build-with-claude/prompt-caching); [*How Claude Code uses prompt caching*](https://code.claude.com/docs/en/prompt-caching) | API only: caching is on by default for supported models; on GPT-5.6 and later a default minimum lifetime of 30 minutes and cache reads at 0.1× the input rate: [*Prompt caching*](https://developers.openai.com/api/docs/guides/prompt-caching); ChatGPT plans not checked | API only: implicit caching on by default for Gemini 2.5 and newer; an explicit cache defaults to one hour: [*Context caching*](https://ai.google.dev/gemini-api/docs/generate-content/caching), a page labelled Legacy; Gemini Apps plans not checked |"; Basis: OpenAI, Prompt caching, https://developers.openai.com/api/docs/guides/prompt-caching ("Prompt caching is enabled by default for supported OpenAI models"; GPT-5.6 and later: 30-minute default minimum lifetime, cache reads at 0.1×); Google, Context caching, https://ai.google.dev/gemini-api/docs/generate-content/caching ("Implicit caching is enabled by default for all Gemini 2.5 and newer models"; "If not set, the TTL defaults to 1 hour"); both read 16 Nov 2026
minor [coverage] Sources (companion to the §9 cache row); Current: "- Google. *Gemini Apps limits & feature availability*. Gemini Apps Help, no date shown. https://support.google.com/gemini/answer/16275805"; Problem: if the §9 cache-row fix is applied, its two pages must be listed; Fix: "- Google. *Gemini Apps limits & feature availability*. Gemini Apps Help, no date shown. https://support.google.com/gemini/answer/16275805\n- OpenAI. *Prompt caching*. OpenAI API documentation. https://developers.openai.com/api/docs/guides/prompt-caching\n- Google. *Context caching*. Gemini API documentation, labelled Legacy. https://ai.google.dev/gemini-api/docs/generate-content/caching"; Basis: as above
minor [accuracy] §6 The training setting; Current: "and \"If you delete a conversation with Claude it will not be used for future model training\" ([Anthropic, *Updates to Consumer Terms and Privacy Policy*, 28 Aug 2025](https://www.anthropic.com/news/updates-to-our-consumer-terms), read 16 Nov 2026; vendor)."; Problem: the 2026 retention page does not restate the 2025 post's "30-day data retention period" for training-off chats; it gives 30 days only for deleted chats. The reader should know the two pages differ; Fix: "and \"If you delete a conversation with Claude it will not be used for future model training\" ([Anthropic, *Updates to Consumer Terms and Privacy Policy*, 28 Aug 2025](https://www.anthropic.com/news/updates-to-our-consumer-terms), read 16 Nov 2026; vendor). The 2026 retention page does not restate the 30 days for chats you keep; it gives 30 days only for deleted chats."; Basis: https://privacy.claude.com/en/articles/10023548-how-long-do-you-store-my-data
minor [figure] §4 Three readings; Current: "Research, agent runs and agent teams all multiply a chat's tokens by a published factor (15×, 7×), each against its own baseline (BW9 §4)"; Problem: 15× is a 2025 system's figure. It is dated in §2 and in row 7, but not here, and the agent-run factor (4×) is missing from the list; Fix: "Research, agent runs and agent teams all multiply a chat's tokens by a published factor (about 15× and 4× on Anthropic's 2025 research system, §2; about 7× for agent teams in plan mode, the table above), each against its own baseline (BW9 §4)"; Basis: Hadfield et al., 13 Jun 2025, https://www.anthropic.com/engineering/multi-agent-research-system ("agents typically use about 4× more tokens than chat interactions"; "multi-agent systems use about 15× more tokens than chats")
minor [figure] §3 compare figure caption; Current: "(read 16 Nov 2026: Claude Code sends the full conversation with every request)"; Problem: a caption adds no fact, but this one carries a paraphrased claim that is not in the unit's text (§2 quotes the costs page in other words), and the costs page could not be opened at its bare address; Fix: "(read 16 Nov 2026: a question in a session open all day still draws usage for the whole conversation, §2)"; Basis: unit §2 ("a one-line question in a session that has been open all day still draws usage for the whole conversation"); sourcing-standard Part 1 (a figure adds no fact)
minor [label] Deliverable Part 1, rule 7; Current: "| Checkers ran with web search, fetch and scripts, the tools their task used (§7 note); other agents' tools not recorded |"; Problem: the §7 note records the tools of BW9's fresh checker and two corrections checkers only. It does not say these were "the tools their task used"; Fix: "| BW9's fresh checker and corrections checkers ran with web search, page fetch and scripts (§7 note); other agents' tools not recorded |"; Basis: Academy case file §7 note (BW9)
minor [label] Deliverable Part 1, rule 4; Current: "| Writers read the filed units, not pastes (§2) |"; Problem: §2 says each context sees its brief and the filed units. It does not say how the writer reached them, so "not pastes" is inferred; Fix: "| Each writer's context sees only its brief and the filed units (§2); how they reached it is not recorded |"; Basis: Academy case file §2
minor [label] Deliverable Part 2; Current: "| Yes, canonical: one private repository (§1) |"; Problem: "canonical" implies other copies, which the case file does not record; Fix: "| Yes: one private repository (§1) |"; Basis: Academy case file §1 ("Everything lives in one private repository")
minor [label] Deliverable Part 2; Current: "| Yes: the same repository; a lost writer was resumed from working files (§7) |"; Problem: the case file puts course texts in the repository (§1). It does not say where drafts or the lost writer's working files were kept; Fix: "| Course texts: the same repository (§1); a third writer resumed from the second's working files (§7); where drafts and working files were kept is not recorded |"; Basis: Academy case file §1, §7
minor [style] §4 The case; Current: "Every \"How often\" cell in the deliverable's case column is therefore \"not recorded\" except row 4 and row 5."; Problem: the deliverable has no case "How often" column: Part 1's table has none and Template B is blank. The frequencies are given in the paragraph after Part 1; Fix: "Every frequency for the case is therefore \"not recorded\" except row 4 and row 5 (Deliverable, the paragraph after Part 1)."; Basis: unit, Deliverable Part 1
minor [coverage] §4 opening; Current: "a budget here is a ceiling on what may enter the window for one task, and the point at which its chat stops."; Problem: the brief asks for "a token budget per task type". The unit gives none in tokens, for a sound reason (§1), but §4 does not say that it departs from the brief's unit of measure; Fix: "a budget here is a ceiling on what may enter the window for one task, and the point at which its chat stops. It is written in what enters, not in tokens, because no page read gives the exchange rate between tokens and a plan's limit (§1)."; Basis: brief.txt; unit §1
minor [accuracy] §7 Memory bullet; Current: "reaches every chat outside projects and the project it belongs to,"; Problem: account memory also reaches every project's chats unless that project's "Use account memory" is off, as the unit's own §6 says. The bullet understates its reach; Fix: "reaches every chat outside projects and, unless a project's \"Use account memory\" is off, every project's chats (a project's own memory stays in that project),"; Basis: Claude Help Center, Use Claude's chat search and memory to build on previous context, https://support.claude.com/en/articles/11817273 (read 16 Nov 2026)

## Confirmed

- *How do usage and length limits work?* PASS: headline as given, labelled "Updated over a week ago", with these quotations:
  - "The period starts when you send your first message, and your limit resets in full five hours later"
  - "Weekly limits apply across all models" and "some plans also have a separate weekly limit for Fable"
  - "Verified Ultra accounts don't have a five-hour limit"
  - "Longer conversations that trigger automatic context management consume more of your usage limit"
  - "Try starting a new conversation if you're approaching your usage limit in a longer chat"
  - "Tools and connectors are token-intensive"
  - "Turn off apps you've connected when a conversation doesn't need them"
  - "the newest models support up to a 1M token context window, while others support 500K or 200K tokens"
  - "Length limits relate to Claude's context window"
  - Source: https://support.claude.com/en/articles/11647753-how-do-usage-and-length-limits-work
- *Claude Fable models on your plan*, labelled "Updated this week": PASS. https://support.claude.com/en/articles/15424964-claude-fable-models-on-your-plan
  - The two quoted Max/Ultra sentences.
  - "Fable models run on pay-as-you-go usage credits from the start" (exact, confirmed).
  - Up to 50% on Max, Ultra and premium seats; no separate Fable limit beyond that share.
- *Manage usage credits for paid Claude plans*, labelled "Updated this week": PASS. https://support.claude.com/en/articles/12429409-manage-usage-credits-for-paid-claude-plans
  - "billed at standard API rates"; "Set a maximum amount you're willing to spend on usage credits each month"; "Adjust limit".
  - Covers Claude Code in the terminal.
  - Credits bought on or after 7 Dec 2026 expire 12 months after purchase.
  - The word "prepaid" does not appear.
- *Usage limit best practices*, labelled "Updated over 2 weeks ago": PASS. https://support.claude.com/en/articles/9797557-usage-limit-best-practices
  - The eight factors, verbatim.
  - "progress bars showing how much of your five-hour session and weekly usage limits you've consumed"
  - "Provide all relevant data in a single, well-structured message"
  - "Content in projects is cached and counts less against your limits when reused"
  - "Caches expire after a period of inactivity"
  - "If you come back to a project after a long break, your first message counts that content in full again"
  - "Claude remembers context from earlier in the conversation", in the caching list.
- *About Claude's Pro Plan Usage*, labelled "Updated over a week ago": PASS. https://support.claude.com/en/articles/8324991-about-claude-s-pro-plan-usage
  - Around 45 messages every five hours for relatively short chats, often more.
  - "limit your usage in other ways, such as weekly and monthly caps or model and feature usage, at our discretion" (exact).
  - "Don't re-upload files within the same conversation"
  - "cached tokens count less than uncached portions toward your usage limits"
- *How large is the context window on paid Claude plans?* (headline as the page shows it), labelled "Updated this week": PASS. https://support.claude.com/en/articles/8606394-how-large-is-the-context-window-on-paid-claude-ai-plans
  - 1M: Fable 5.2, Fable 5.1, Opus 5.5, Opus 5, Sonnet 5.5, Sonnet 5, Haiku 5.5.
  - 500K: Fable 5, Opus 4.6–4.8, Sonnet 4.6.
  - "Outside of these models, Claude's context window size is 200K"
- *How Claude Code uses prompt caching*: PASS. https://code.claude.com/docs/en/prompt-caching
  - "The match is exact, so a change anywhere in the prefix recomputes everything after it"
  - Each model has its own cache, and a switch "recomputes the entire request even when the content is identical".
  - Changing effort keeps the cache on Opus 5.5, Sonnet 5.5, Haiku 5.5 and Fable 5.1 with an API key or a Claude subscription: "the cache stays intact by default". Fable 5.2 is not listed.
  - One hour for the main conversation on a subscription within plan usage; five minutes on usage credits.
  - "Subagents fall outside the main-conversation TTL bucket, so they get five minutes even on a subscription"
  - A fork "inherits the parent's system prompt, tools, and conversation history exactly, so its first request reads the parent's cache"
  - Fast mode, an MCP change with tool search off, and compaction break the cache; editing files, skills and rewind keep it.
  - "Rewinding truncates back to a prefix that is already cached, rather than building a new one as compaction does"
  - The "Pick your model and effort level…" tip.
  - Compaction is cheap while the cache is warm and full price after a break.
  - "Claude Code can compact it shortly before the cache expires"
- Platform *Prompt caching*: PASS, read at https://platform.claude.com/docs/en/build-with-claude/prompt-caching, the address search returned.
  - "By default, the cache has a 5-minute lifetime"
  - Writes at 1.25× (5 min) and 2× (1 h).
  - Reads at 0.1×; 0.05× on Opus 5.5 and Sonnet 5.5; 0.025× on Fable 5.2 and 5.1.
  - 512-token minimum on the newest models.
  - No mention of claude.ai or subscriptions.
- *Agent Skills*: "~100 tokens per Skill" at startup: PASS. https://platform.claude.com/docs/agents-and-tools/agent-skills/overview
- *Use research on Claude*, labelled "Updated over 2 weeks ago": PASS. https://support.claude.com/en/articles/11088861-use-research-on-claude
  - "Research is subject to the same limits as standard Claude conversations"
  - "can use up your limits faster due to Claude retrieving multiple sources" (exact).
- Hadfield, Zhang, Lien, Scholz, Fox, Ford, *How we built our multi-agent research system*, 13 Jun 2025: PASS. https://www.anthropic.com/engineering/multi-agent-research-system
  - "about 4× more tokens than chat interactions"
  - "multi-agent systems use about 15× more tokens than chats"
- *How long do you store my data?*, 1 Jul 2026, covering Free, Pro, Max and Claude Code on those accounts: PASS. https://privacy.claude.com/en/articles/10023548-how-long-do-you-store-my-data
  - "as long as reasonably necessary"
  - Deleted chats leave back-end storage within 30 days.
  - "for up to 5 years in our model training pipelines"
  - Flagged inputs and outputs up to 2 years; classification scores up to 7.
  - Feedback kept 5 years.
  - "Your Incognito chats are not used to improve Claude"
  - No mention of projects, memory or files.
- *How do I change my model improvement privacy settings?*, 3 Aug 2026: PASS. https://privacy.claude.com/en/articles/12109829-how-do-i-change-my-model-improvement-privacy-settings
  - The toggle is under Settings > Privacy.
  - "we will not use any new chats and coding sessions you have with Claude for future model training"
  - "Your data will still be included in model training that has already started"
  - Flagged chats may still be used to improve trust and safety models.
- *Updates to Consumer Terms and Privacy Policy*, 28 Aug 2025: all four quoted strings: PASS. https://www.anthropic.com/news/updates-to-our-consumer-terms
- Sensitive-data article, labelled "Updated over 2 weeks ago", covering Free, Pro, Max, Ultra and Claude Code: both quotes and the care list: PASS. https://support.claude.com/en/articles/8325621-i-would-like-to-input-sensitive-data-into-my-chats-with-claude-who-can-view-my-conversations
- Memory article, labelled "Updated this week": every statement in §6: PASS. https://support.claude.com/en/articles/11817273
  - Memory saved as topics; each project has its own memory; "Use account memory".
  - Sensitive topics excluded by default, and the toggle that includes them.
  - The never-saved list.
  - Memory entries survive chat deletion; delete under Settings > Your Claude > Manage.
  - An organisation's retention period applies to memory except project memory.
  - Owners control availability; "Owners can't turn memory on for individual users".
  - The article does not say how much memory loads into a chat.
- Memory post, 25 Aug 2026: PASS. https://claude.com/resources/articles/claudes-memory-works-everywhere-and-you-decide-whats-in-it
  - "Memory is on by default on Free, Pro, Max, and Ultra plans across web, desktop, and mobile"
  - The undated update note on Team and Enterprise organisations created on or after 31 Oct 2026.
- *How can I create and manage projects?*, labelled "Updated over a week ago": the context quote; sharing and deletion described; nothing on retention, training or files after deletion: PASS. https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects
- *Use incognito chats*, labelled "Updated over 2 weeks ago": every statement in §6; available on all plans: PASS. https://support.claude.com/en/articles/12260368-use-incognito-chats
- *Is my data used for model training?*, 18 Aug 2026: PASS; the URL slug is covered by the findings. https://privacy.claude.com/en/articles/7996868-is-my-data-used-for-model-training
  - Commercial products are not trained on by default, unless you send feedback or opt in.
  - Feedback is kept up to 5 years.
  - No general retention period for commercial chats.
- *Gemini Apps Privacy Hub*, last updated 26 Oct 2026: PASS. https://support.google.com/bard/answer/13594961
  - Both quotes.
  - With Keep Activity off, chats are kept 72 hours.
  - 18 months by default, 3 or 36 selectable.
  - Reviewed chats kept up to three years.
  - Temporary chats.
- *Gemini Apps limits & feature availability* (headline as the page shows it; no date): PASS. https://support.google.com/gemini/answer/16275805
  - Limits refresh every five hours until a weekly limit, as multiples, and "may change".
  - Context windows of 32k, 128k and 1 million.
  - Deep Research rated "High".
- OpenAI *Data Controls FAQ*, labelled "Updated over 4 months ago": PASS. https://help.openai.com/en/articles/7730893-data-controls-faq
  - "Improve the model for everyone".
  - Temporary Chats are not trained on and are deleted within 30 days.
  - Business plans are pointed to for more control.
- Arithmetic: PASS.
  - §3: 2,000 × 465 = 930,000; 110,000 + 130,000 + 130,000 = 370,000; about 60% less.
  - §4: 20 × 100 = 2,000.
- Case facts from the Academy case file: PASS, except the five case-label findings above.
  - §1: 194 units; 2,000–6,000 words by guide; one private repository.
  - §2: one context per unit; each chat writes the next prompt; staleness check.
  - §5: 36 fresh checks.
  - §7: lost writers; the structure audit's seventeen findings; private terms.
  - §7 notes: plan, memory and token measures not recorded; the private-terms check.
  - §8: 53 chats over six days; 31 Opus, 18 Fable, 4 both; ten ranked changes.
  - §9: no measure of hours or money.
  - Header.
- Unverifiable: search did not return the bare address, so these were not checked.
  - Claude *Pricing*: the four §1 quotes; "No 5-hour limit"; one pool across surfaces; credits at API rates; no fixed message count.
  - *Manage costs effectively*: minimal file reads; the 10,000-line log hook; the one-line question; thinking billed as output; the idle scheduled task; teammates; "Stale context…"; "/clear costs nothing"; CLAUDE.md under 200 lines; subagent requests draw usage; agent teams about 7×; `/usage` attribution and 10%; `--max-budget-usd`; the first message after a break misses the cache.
  - *Automate work with scheduled tasks*: draws subscription usage; 100 runs an hour; connectors included.

## (1) Coverage

- What a subscription measures and how its windows work, as stated today: covered (§1).
- Plain statement of what the vendor does not publish: covered (the §1 list and matrix).
- What burns usage for no gain (re-reading large files, giant pastes, chats that never end, research run twice): covered (§2), with three extra items.
- When a new chat is cheaper: covered (§3: arithmetic and a decision rule).
- A token budget per task type: thin. Budgets are given as what enters the window plus a stop line, with no token figures, for a reason the unit states (§1); see the minor finding on §4.
- Caching as far as documented: covered (§5: API, Claude Code, claude.ai).
- What the vendor keeps, for how long, and the training settings, each from the vendor's page and dated: covered (§6); one row overstated (finding).
- Which material belongs in memory, a project, a private store or nowhere: covered (§7).
- Work material and an employer's policy, as a question: covered (§8, five questions).
- Deliverable:
  - numbered rules, each with a source: covered (twelve rules);
  - table of where material belongs: covered (§7 table, and Part 2 on the case);
  - template: covered (Templates A–D).
- "On other tools" section before the deliverable: present; the caching row is thin (finding).
- Academy case labelled on first use and as an anecdote: covered.
- Re-check date: given (16 May 2027).

## (5) Deliverable

- **Present in full:** twelve rules, each with a source, a grade, the count a reader's record shows and the case instance; Part 2 on the case; Templates A–D, with every blank saying what goes in it.
- **Follows from the evidence:** yes. Rule 2's claude.ai hour and rules 8, 11 and 12 are labelled stated opinion.
- **Usable alone:** largely. Part 2 on the case is mostly [NOT IN CASE FILE] and relies on §7's general table, which sits in the body, not the deliverable. That is acceptable under the brief, since the case table records only what the case did, but a reader using the deliverable alone needs §7.

## (6) Errata and pointers

There were no audit errata to apply. I could not check pointers to BW1–BW9 against those units, which are not in the packet. As far as the unit and the brief show, they are consistent:
- Each unit in the brief's Takes line (BW1, BW2, BW4, BW9) is pointed to for what the brief says it holds.
- The deliverable honours the brief's "Gives" line (DD-BW3).

## (7) Figures

1. **matrix, §1: PASS.** Every label traces to the text:
   - "Session window: five hours from the first message": "your limit resets in full five hours later"
   - "Weekly limit across all models": "Weekly limits apply across all models"
   - "its size": "the size of the weekly limit"
   - "up to 50%" and "how much faster": "up to 50% of your weekly usage limits"; "use them faster"
   - "Pro example: about 45": "around 45 messages every five hours"
   - "no fixed count": "there's no fixed message count"
   - "Rate per model / not stated": "the rate at which each model draws the limit"
   - "counts less" and "how much less": the §1 list; §5
   - "Cache lifetime, claude.ai / not stated": "how long a claude.ai cache lasts"
   - "one hour": §3 and §5, "one hour for the main conversation on a subscription"
   - "1M": the §1 window list
   - "API rates": "billed at standard API rates"
   - The caption names what the figure shows, its sections and its sources. The kind fits: items by sections.
2. **compare, §3: FIX.** 930 and 370 trace to "= 930,000 tokens of history" and "= 370,000"; the labels trace; the kind fits (numbers compared). The caption carries a paraphrased claim that is not in the text. Replacement caption: "History sent over 30 turns, in thousands of tokens, on BW1 §2's illustrative 2,000 tokens an exchange and a 2,000-token handoff note: arithmetic in §3 of this unit, unmeasured and uncached, on the mechanism in BW1 §2 and Anthropic, Manage costs effectively (read 16 Nov 2026: a question in a session open all day still draws usage for the whole conversation, §2)."
3. **decision, §3: PASS.** Every question and outcome traces to "The rule" paragraph: "Does the next step need this chat's history?"; "has the chat been idle longer than the cache lifetime?"; "is the chat on a wrong path?"; "Claude Code: /rewind. claude.ai: new chat"; "stay; /compact only between tasks". The caption names the rule, its section and its sources. The kind fits: a rule with branches.
4. **matrix, §7: PASS.** Every row and mark traces to the §7 table: "Yes, if small" → "if small"; "Yes, canonical" → "canonical"; "Yes, if you need them" → "if needed"; "Only with their consent and a reason" → "with consent". The caption names §7 and its sources. The kind fits.

## (8) Writer's "Source errors" (notes.md)

1. B8's statement that the context window is "200K tokens across all models" is no longer on article 11647753: confirmed. The page is now headed "How do usage and length limits work?", labelled "Updated over a week ago", and says "On paid plans, the newest models support up to a 1M token context window, while others support 500K or 200K tokens" (read 16 Nov 2026).
2. Fable: confirmed. *Claude Fable models on your plan* ("Updated this week") describes only a share of up to 50% of the weekly limit on Max, Ultra and premium seats. *How do usage and length limits work?* still says "some plans also have a separate weekly limit for Fable".
3. Credits described as "prepaid": confirmed. The word does not appear; the article says credits are "billed at standard API rates" and that credits bought on or after 7 Dec 2026 expire 12 months after purchase.

Confirmed 3, not confirmed 0.

## (9) Sourcing standard, Part 1 and Part 6

Part 1
- **Sourced where made:** yes, throughout.
- **Source openable (organisation, title, locator, date):** yes; one locator is misleading (the 7996868 slug; finding).
- **Source says what the claim says:** yes, except the training-off retention row (finding) and the reach of memory in §7 (finding).
- **Cited for what it says itself:** yes; 15× is kept as Anthropic's own 2025 figure.
- **Number says whose figure it is:** yes, except §4 reading 2's undated 15× (finding).
- **View attached to a named person only if they argued it:** yes; Hadfield et al. are named for their figures only.
- **Quotation marks exact:** every quotation on pages that opened matched. Quotations from *Pricing*, *Manage costs effectively* and *Automate work with scheduled tasks* are unverifiable.
- **Nothing invented:** no invented citation, name or number found.
- **Figure adds no fact:** three figures pass; the compare caption carries a paraphrase (finding).
- **Illustration rule:** no illustration in the unit.
- **Unsourceable claims said to be unsourced:** yes (§1 "What is not published"; §6 project files "Not stated").
- **Search-on facts dated:** yes; every vendor fact is dated 16 Nov 2026, with page labels.
- **Sources list complete, nothing extra:** yes, the 7996868 address aside.
- **Closing material agrees with the body:** yes; but Part 2's private-terms gloss and three case cells infer beyond the case file (findings).

Part 6
- **Number, mechanism or recommendation sourced:** yes.
- **Source types labelled (vendor and dated; practice; preprint):** yes; every vendor source is labelled "vendor"; there are no preprints.
- **Evidence grade per practice:** yes, in §2–§5 and on every rule.
- **Study names its models and task; transfer labelled:** Hadfield's figures are labelled as Anthropic's 2025 system, and the unit disclaims any transfer to current rates.
- **Product facts dated on the vendor's page:** yes.
- **"On other tools" cites vendor docs or says none was found:** present. The caching row says "Not checked" for both vendors where documentation exists (finding). Several ChatGPT cells say "Not checked" because the pages failed, and the unit says so.
- **Carried-over claims re-verified:** the unit states every fact was re-read on 16 Nov 2026, and notes.md lists what was not carried over.
- **Nothing about the private course's reader; no reference to the private course:** one reference to "the private courses' names" in Part 2 (finding); no name, city, health detail or handle found.
- **Academy facts from the case file, cited, labelled, never sole support:** yes, with five cells that go beyond the file (findings).
- **No uncited figures; no invented names:** yes.
- **Deliverable built on the case, then as a template:** yes.
- **Not advice without evidence:** passes.
- **Links as links:** yes.

## (10) Read as the brief's reader

The public course's reader, an experienced professional, can follow the unit. These places assume knowledge only an insider has:
- **Fable model names** (Fable 5, 5.1, 5.2) appear without a gloss, so a reader who skipped BW2 meets them cold. They are Anthropic's own product names on the pages cited, so this is a dependency on an earlier unit, not private knowledge.
- **"[NOT IN CASE FILE]"** in Part 2 is a writing-process marker. The sentence under the table explains it, so it stands.
- **"the private courses' names"** in Part 2 points at courses the reader cannot see (finding).
- **"the fresh checker" and "corrections checkers"** (rule 7's case cell) are terms from the case's method. Academy case file §2 explains them, and BW6 presumably does too, so nothing needs changing beyond the finding.
- **"A page that refused the fetch" and "the address the search returned"** in the intro describe the writer's tooling, but are plain enough for this reader.

Verdict: BW10 · fix · 0 error, 7 should-fix, 11 minor
