---
code: BW10
title: Cost, limits, privacy
course: building-with-ai · BW · Building with AI
model: Opus 5.5
written: 2026-11-16
search: on
intro: The tenth unit of Building with AI: what running a project costs in usage and what it gives away: what a subscription meters (a five-hour session window, a weekly limit, one pool across surfaces, credits past the limit) and what the vendor does not publish (the tokens a window or a week allows, the rate at which each model draws the limit, how much less a cached token counts, how long a claude.ai cache lasts, how much memory enters a chat); what burns usage for no gain; when a new chat is cheaper, with its arithmetic and a decision rule; a token budget per task type, for every row of BW2's routing table and three kinds of run; caching as far as it is documented, on the API, in Claude Code and on claude.ai; what the vendor keeps, for how long, and the settings that govern training, each from the vendor's page and dated; which material belongs in memory, in a project, in a private store or nowhere; work material and an employer's policy, put as questions for the reader; a section on other tools; and a deliverable in three parts: twelve numbered usage rules, each with its source, its evidence grade, what a record of your own chats shows and the Academy case's instance, a table of where material belongs on the case, and templates for your own project. It was written by an AI model (Opus 5.5) from its brief, with live search on 16 Nov 2026; every page it cites was read that day at the address a search returned, and every product fact is dated where it appears. A separate model (Opus 5.5), in a context that had not seen the writing, checked every cited claim, the deliverable against the brief and every figure against the text; its verdict was fix, with no error, 7 should-fix and 11 minor points, and all 18 were applied before filing, 4 of them after the fix the check proposed had itself been corrected; none was held. Known gaps: Anthropic publishes no token count for a window or a week, no rate per model and no weight for a cached token, so the budgets per task give what enters the window and a line at which to stop, not token figures; for Claude Code's Manage costs effectively, Claude's Pricing page and Automate work with scheduled tasks no search returned the plain address, so they were read at addresses carrying query strings and are cited at the plain address, and the check could not verify their quotations; Anthropic's help article on the Ultra plan refused the fetch, so Ultra's lack of a five-hour limit rests on the pricing page and the usage-limits article; two of Anthropic's help pages disagree on whether some plans have a separate weekly limit for Fable, and the unit takes the more recently updated Fable article and states the disagreement; how long a claude.ai cache lasts is unpublished, so the one-hour break of rule 2 is Claude Code's subscription figure applied by analogy and graded stated opinion, as are rules 8, 11 and 12; one Privacy Center article was fetched at an address whose slug names another article, the unit cites it at its own address and relies on it only for two facts, and no general retention period for chats on commercial plans was found; the on-screen label of the model-improvement setting is not quoted; the update note on Anthropic's memory post carries no date of its own; Anthropic's 4× and 15× token multiples describe its 2025 research system, and no dedicated search for a 2026 figure was run; ChatGPT's plan page, its Memory FAQ and OpenAI's page on business data failed to load, so those cells of the section on other tools say not checked, and Google's limits page shows no date; the twelve rules are untested against a reader's record, which DD-BW3 does; and the Academy case file does not record the plan the project runs on, its memory and training settings, any token, window or usage measure, how often each routed task recurs, any spend cap on agent runs, where private material other than the private-terms list is kept, or any employer material or policy, so those cells of the deliverable are marked not recorded or [NOT IN CASE FILE] as blanks for the project's owner.
---

# BW10 · Cost, limits, privacy

This unit was written with search on. Every page it cites was found by a web search and read on 16 November 2026 at the address the search returned; every product fact (a limit, a price, a retention period, a setting, a default) carries that date. Most help-centre pages show only a relative label ("Updated this week"), which is given where it appears. A page that refused the fetch or failed to load is marked "not checked" and was not retried. Each practice carries an evidence grade, as in BW1 to BW9: **measured** (a study or test with numbers), **documented practice** (a vendor or a named practitioner says to do it; nobody measured it here) or **stated opinion**. Calculations are labelled **arithmetic**: they are done on published figures, shown so you can redo them, and measure nothing. Four earlier units are taken as read: what a token is and why every turn re-sends the history (BW1 §2), the plan comparison and the routing table (BW2 §6 and Deliverable), the layers of a project and when each loads (BW4 §1 to §4), and what an agent is and what it costs in tokens (BW9 §1 and §4). This unit points to them and does not restate them. Re-check every product fact on 16 May 2027, six months after this reading.

## 1 · What a subscription measures, and what it does not publish

BW2 §6 compared Anthropic's plans and the API on 15 November 2026. Read again on 16 November 2026, Anthropic's pages describe what a subscription meters in four parts.

**A session window.** "The period starts when you send your first message, and your limit resets in full five hours later" ([Claude Help Center, *How do usage and length limits work?*](https://support.claude.com/en/articles/11647753-how-do-usage-and-length-limits-work), labelled "Updated over a week ago", read 16 Nov 2026; vendor). The pricing page calls it "a rolling five-hour session window", on which "paid plans add weekly limits on top" ([Claude, *Pricing*](https://claude.com/pricing), read 16 Nov 2026; vendor). The same page lists Ultra with "No 5-hour limit"; the help article says verified Ultra accounts do not have the session limit. Anthropic's own article on Ultra refused the fetch for this unit and was not checked.

**A weekly limit.** "Weekly limits apply across all models" (*How do usage and length limits work?*). On Max and Ultra, Fable models "draw from your plan's regular weekly usage limits and use them faster than other Claude models", and "You can use up to 50% of your weekly usage limits on Fable models at no extra cost"; on Pro, "Fable models run on pay-as-you-go usage credits from the start" ([Claude Help Center, *Claude Fable models on your plan*](https://support.claude.com/en/articles/15424964-claude-fable-models-on-your-plan), labelled "Updated this week", read 16 Nov 2026; vendor). The usage-limits article says some plans also have a separate weekly limit for Fable; the Fable article, updated more recently, describes a share of the regular limit and no separate one. Two of the vendor's pages differ here; the Fable article is the more specific.

**One pool across surfaces.** "Your activity across Claude on web, desktop, mobile, and Claude Code all draws from the same pool" (*Pricing*). Scheduled tasks in Claude Code "draw down subscription usage the same way interactive sessions do" ([Anthropic, *Automate work with scheduled tasks*](https://code.claude.com/docs/en/web-scheduled-tasks), read 16 Nov 2026; vendor).

**Credits past the limit.** On paid plans you can "turn on usage credits to keep working at standard API rates" (*Pricing*). The credits page adds that "Usage credits are billed at standard API rates", that you can "Set a maximum amount you're willing to spend on usage credits each month" under Settings > Usage with "Adjust limit", that credits cover Claude Code in the terminal as well as chat, and that credits bought on or after 7 December 2026 generally expire twelve months after purchase ([Claude Help Center, *Manage usage credits for paid Claude plans*](https://support.claude.com/en/articles/12429409-manage-usage-credits-for-paid-claude-plans), labelled "Updated this week", read 16 Nov 2026; vendor). Settings > Usage shows "progress bars showing how much of your five-hour session and weekly usage limits you've consumed" ([Claude Help Center, *Usage limit best practices*](https://support.claude.com/en/articles/9797557-usage-limit-best-practices), labelled "Updated over 2 weeks ago", read 16 Nov 2026; vendor).

**What draws the limit down.** Anthropic lists eight factors: "Message length", "File attachment size", "Current conversation length", "Tool usage (e.g., Research, web search)", "Model choice", "Effort level", "Artifact creation and usage", and "Multi-step tasks, like running code, creating files, or browsing websites" (*Usage limit best practices*). The pricing page sums it up: "How much you can do depends on the length and complexity of your conversations, the model you choose, and the features you use, so there's no fixed message count."

**What is not published.** None of the pages read gives:

- the number of tokens a five-hour window or a week allows on any plan. The one worked example is still the Pro article's: around 45 messages every five hours for short conversations, often more depending on capacity ([Claude Help Center, *About Claude's Pro Plan Usage*](https://support.claude.com/en/articles/8324991-about-claude-s-pro-plan-usage), labelled "Updated over a week ago", read 16 Nov 2026; vendor). The same article keeps the right to "limit your usage in other ways, such as weekly and monthly caps or model and feature usage, at our discretion";
- the rate at which each model draws the limit (BW2 §6 found the same on 15 Nov 2026), beyond Fable using it "faster";
- the size of the weekly limit;
- how much less a cached token counts against a plan (§5);
- how long a claude.ai cache lasts (§5);
- how much memory is loaded into a given chat (§6).

The window itself is published: in the claude.ai chat on paid plans, Fable 5.2, Fable 5.1, Opus 5.5, Opus 5, Sonnet 5.5, Sonnet 5 and Haiku 5.5 have 1M tokens; Fable 5, Opus 4.6 to 4.8 and Sonnet 4.6 have 500K; and "Outside of these models, Claude’s context window size is 200K" ([Claude Help Center, *How large is the context window on paid Claude plans?*](https://support.claude.com/en/articles/8606394-how-large-is-the-context-window-on-paid-claude-ai-plans), labelled "Updated this week", read 16 Nov 2026; vendor). The usage-limits article now agrees ("the newest models support up to a 1M token context window, while others support 500K or 200K tokens"), and states the split this unit relies on: "Length limits relate to Claude's context window", while usage limits govern how much you use over time.

The matrix sorts what a subscriber can read from the vendor against what has to be inferred.

```viz
{
 "kind": "matrix",
 "cols": ["Published", "Not published"],
 "rows": [
  {"label": "Session window: five hours from the first message", "cells": [{"mark": "yes", "tone": 3}, null]},
  {"label": "Weekly limit across all models", "cells": [{"mark": "exists", "tone": 3}, {"mark": "its size", "tone": 1}]},
  {"label": "Fable on Max and Ultra", "cells": [{"mark": "up to 50%", "tone": 3}, {"mark": "how much faster", "tone": 1}]},
  {"label": "Tokens or messages per window", "cells": [{"mark": "Pro example: about 45", "tone": 4}, {"mark": "token count", "tone": 1}]},
  {"label": "Rate per model", "cells": [null, {"mark": "not stated", "tone": 1}]},
  {"label": "Cached project content", "cells": [{"mark": "counts less", "tone": 3}, {"mark": "how much less", "tone": 1}]},
  {"label": "Cache lifetime, claude.ai", "cells": [null, {"mark": "not stated", "tone": 1}]},
  {"label": "Cache lifetime, Claude Code on a subscription", "cells": [{"mark": "one hour", "tone": 3}, null]},
  {"label": "Context window, current models in chat", "cells": [{"mark": "1M", "tone": 3}, null]},
  {"label": "Usage credits", "cells": [{"mark": "API rates", "tone": 3}, null]}
 ],
 "caption": "What Anthropic publishes about a subscription's metering, as read 16 Nov 2026, from §1 and §5 of this unit: Claude, Pricing; Claude Help Center, How do usage and length limits work?, Claude Fable models on your plan, About Claude's Pro Plan Usage, Usage limit best practices, Manage usage credits for paid Claude plans and How large is the context window on paid Claude plans?; Anthropic, How Claude Code uses prompt caching."
}
```

**What follows** (stated opinion, on the pages above). You cannot budget a subscription in tokens, because the exchange rate is unpublished. You can budget it in what enters each window, which you control (BW1 §1), and read the result on the usage bars. Every rule in this unit is of that kind.

**The case.** Academy (Academy case), a library of self-study courses built by one person with Claude in October and November 2026, is this course's running example: one project, an anecdote, never evidence about AI tools in general. Its record does not say which plan the project runs on, or any token or window measure for the writing of a single unit (Academy case file §9); on the Project's setup of 28 Oct 2026 account memory flowed into the Project beside its own memory store (§7); and it holds no measure of hours or money spent per unit (§9). So the case cannot show a usage figure per unit; the token figures it holds are totals for two batches of agent work (§7). What it can show is the shape of its work, which decides what enters each window: each unit is written in a new chat or a fresh agent context that sees only its brief and the units already filed (§2).

## 2 · What burns usage for no gain

Each of the four habits below spends one of Anthropic's eight factors (§1) and buys nothing the task needed.

**Re-reading large files.** A file read into a chat sits in the history from then on and is re-sent on every later turn (BW1 §2). Reading it again adds a second copy. Anthropic's Pro article names the plain case: "Don't re-upload files within the same conversation" (*About Claude's Pro Plan Usage*). In Claude Code, the documented remedies are to read less in the first place: specific requests let Claude "work efficiently with minimal file reads", and a hook that filters a 10,000-line log to its error lines cuts the context "from tens of thousands of tokens to hundreds" ([Anthropic, *Manage costs effectively*](https://code.claude.com/docs/en/costs), read 16 Nov 2026; vendor; documented practice). BW4 §2 gave the general form: a file a chat is pointed to by name loads once, when needed, and nothing else arrives.

**Giant pastes.** Message length is the first factor on the list, and a paste is re-sent like a file. Anthropic's advice runs the other way for material the task does need: "Provide all relevant data in a single, well-structured message" (*Usage limit best practices*), and BW3 §5 gave the evidence that a brief given in pieces does worse than the same brief given whole. The waste is the paste the task did not need: a full export when one column is used, a whole transcript when one section is used, the same document pasted again three turns later. The test before pasting (stated opinion): does the model need this text to produce this output?

**Chats that never end.** BW1 §2's illustrative arithmetic: at about 2,000 tokens an exchange, the first 30 turns send about 930,000 tokens of input in all. Claude Code's page says the same in plan terms: "a one-line question in a session that has been open all day still draws usage for the whole conversation" (*Manage costs effectively*). On claude.ai a chat long enough to be summarised costs more again: "Longer conversations that trigger automatic context management consume more of your usage limit", and the article's advice is to "Try starting a new conversation if you're approaching your usage limit in a longer chat" (*How do usage and length limits work?*). The tokens buy worse answers as well, by context rot (BW1 §2).

**Research run twice.** "Research is subject to the same limits as standard Claude conversations", and research sessions "can use up your limits faster due to Claude retrieving multiple sources" ([Claude Help Center, *Use research on Claude*](https://support.claude.com/en/articles/11088861-use-research-on-claude), labelled "Updated over 2 weeks ago", read 16 Nov 2026; vendor). The only research multiple Anthropic has published is for its 2025 system: agents use "about 4× more tokens than chat interactions" and "multi-agent systems use about 15× more tokens than chats" ([Hadfield, Zhang, Lien, Scholz, Fox and Ford, *How we built our multi-agent research system*, Anthropic, 13 Jun 2025](https://www.anthropic.com/engineering/multi-agent-research-system), read 16 Nov 2026; vendor, measured internally, 2025 system). No newer figure was found for this unit; 15× is a 2025 system's figure, and no current rate is published. Running the same question again pays it again, and every run brings fresh claims to check (BW6 §1, §5). The remedy is BW4 §4's: a finding worth keeping is written to a file with its source and date, and the next chat reads the file.

Three more items on the list spend usage when left at a setting the task does not need.

- **Effort above the task's need.** Effort level is one of the eight factors; BW2 §3 sets effort per task. In Claude Code, thinking tokens "are billed as output tokens", and lowering effort is the documented way to cut them on models whose thinking cannot be switched off (*Manage costs effectively*).
- **Tools and connectors left on.** "Tools and connectors are token-intensive", and the article's advice is to "Turn off apps you've connected when a conversation doesn't need them" (*How do usage and length limits work?*). BW4 §1 gives the On demand setting.
- **Work that runs while you are away.** In Claude Code, a session-scoped scheduled task "fires on its interval even while the session is idle, sending your full context each time"; goal check-ins, subagents and agent teammates send requests of their own, and each teammate "keeps consuming tokens until it exits" (*Manage costs effectively*). BW9 §4 costs agents; this unit adds that background work keeps spending.

**The case** (anecdote). The case's method avoids the first and third habits by construction: one unit, one context, which sees its brief and the filed units (Academy case file §2). It records one failure traced to a chat's length: a chat that had filed two units could not refresh the remaining Project copies, its context unable to hold them (§7); and a rewrite that opened 43 distinct sources, 34 of them already opened that morning by the audit before it (§8). A usage review of the owner's chats, 53 chats over six days, produced ten ranked changes, each tied to a count (§8), which the case file lists (lines added 17 Nov 2026).

## 3 · When a new chat is cheaper

BW4 §4 set out when to start a new chat for quality and independence, and when not to. This section adds the cost side.

**The mechanism.** Continuing a chat re-sends its history on every turn (BW1 §2). A new chat sends the standing layers (instructions, skill descriptions, memory, project files while small: BW4 §2) plus what you hand it. The standing layers are paid on every turn of every chat either way, so they drop out of the comparison; what differs is the history.

**The arithmetic** (illustrative, unmeasured, uncached). On BW1 §2's assumption of about 2,000 tokens an exchange, 30 turns in one chat send 2,000 × (1 + 2 + … + 30) = 930,000 tokens of history. The same 30 turns as three chats of 10, each later chat opening with a 2,000-token handoff note, send 110,000 + 130,000 + 130,000 = 370,000 (turn k of a later chat sends the note plus 2,000 × k). That is about 60% less, provided the later turns needed only what the note carries.

```viz
{
 "kind": "compare",
 "unit": "k tokens",
 "max": 1000,
 "rows": [
  {"label": "30 turns in one chat", "value": 930, "tone": 1},
  {"label": "Three chats of 10 turns, with a handoff note", "value": 370, "tone": 3}
 ],
 "caption": "History sent over 30 turns, in thousands of tokens, on BW1 §2's illustrative 2,000 tokens an exchange and a 2,000-token handoff note: arithmetic in §3 of this unit, unmeasured and uncached, on the mechanism in BW1 §2 and Anthropic, Manage costs effectively (read 16 Nov 2026: a question in a session open all day still draws usage for the whole conversation, §2)."
}
```

**What caching changes.** While a cache is warm, re-sent history costs less (§5), so inside one working session a long chat costs less than the uncached arithmetic says. After a break the comparison flips back. For project content on claude.ai, "If you come back to a project after a long break, your first message counts that content in full again" (*Usage limit best practices*). In Claude Code, "your first message after a break longer than the cache lifetime misses the cache and reprocesses your full context" (*Manage costs effectively*). The cache lifetime there is one hour for the main conversation on a subscription within the plan's included usage, and five minutes on usage credits ([Anthropic, *How Claude Code uses prompt caching*](https://code.claude.com/docs/en/prompt-caching), read 16 Nov 2026; vendor). claude.ai publishes no lifetime: "Caches expire after a period of inactivity" (*Usage limit best practices*).

**Trimming, in Claude Code** (documented practice; *How Claude Code uses prompt caching*, *Manage costs effectively*):

- `/rewind` truncates to an earlier turn: "Rewinding truncates back to a prefix that is already cached, rather than building a new one as compaction does." It is the cheap way off a wrong path.
- `/compact` replaces the history with a summary. The summarising request reads the whole conversation, cheaply while the cache is warm and at full price after a break. The page's tip: "Pick your model and effort level at the top of a session, then save `/compact` for natural breaks between tasks."
- `/clear` starts fresh: "When you want a fresh start instead of continuity, `/clear` costs nothing", and "Stale context wastes tokens on every subsequent message" (*Manage costs effectively*).
- If you leave a long conversation idle in a terminal on the one-hour cache, "Claude Code can compact it shortly before the cache expires" (*How Claude Code uses prompt caching*): the tool writes its own handoff note while the history is still cheap to read.

On claude.ai no help article read for this unit describes a way to trim a chat by hand; the one trimming mechanism is automatic context management, which costs more of the limit (§2).

**Switching model or effort mid-chat.** In Claude Code, "each model has its own cache", and switching models "recomputes the entire request even when the content is identical". Changing effort does the same on most models; on Opus 5.5, Sonnet 5.5, Haiku 5.5 and Fable 5.1, with an API key or a Claude subscription, "the cache stays intact by default" (*How Claude Code uses prompt caching*). The page does not list Fable 5.2 among those models. On claude.ai the effect is undocumented; BW2's rule 1 already sets both dials before the first message, and that rule costs nothing.

**The rule** (stated opinion; each branch traces to a source above). First ask: does the next step need this chat's history? If it does not, start a new chat (Claude Code: /clear). If it does, ask: has the chat been idle longer than the cache lifetime? If it has, start a new chat with a handoff note, since the next message pays for the whole history anyway and the note is smaller. If it has not, ask: is the chat on a wrong path? If it is: Claude Code: /rewind. claude.ai: new chat, since claude.ai documents no hand trim. If it is not: stay; /compact only between tasks. On claude.ai the lifetime is unpublished, so this unit treats a break of over an hour as expired, by analogy with Claude Code's one-hour figure (stated opinion). This refines BW4 §4's third reason to stay ("The pause is short"): short means inside the cache lifetime.

```viz
{
 "kind": "decision",
 "root": {
  "q": "Does the next step need this chat's history?",
  "tone": 4,
  "branches": [
   {"label": "no", "to": {"outcome": "New chat (Claude Code: /clear)", "tone": 3}},
   {"label": "yes", "to": {
    "q": "Has the chat been idle longer than the cache lifetime?",
    "tone": 4,
    "branches": [
     {"label": "yes", "to": {"outcome": "New chat with a handoff note", "tone": 3}},
     {"label": "no", "to": {
      "q": "Is the chat on a wrong path?",
      "tone": 4,
      "branches": [
       {"label": "yes", "to": {"outcome": "Claude Code: /rewind. claude.ai: new chat", "tone": 2}},
       {"label": "no", "to": {"outcome": "Stay; /compact only between tasks", "tone": 2}}
      ]
     }}
    ]
   }}
  ]
 },
 "caption": "When a new chat is cheaper: the rule in §3 of this unit (stated opinion), built on Anthropic, How Claude Code uses prompt caching and Manage costs effectively, and Claude Help Center, Usage limit best practices, all read 16 Nov 2026."
}
```

**The case** (anecdote). The case's chats end by writing the prompt for the next chat (Academy case file §2), and a lost writer's work was resumed by a third writer from the second's working files (§7): the handoff lived in files, so a new context could pick it up. Whether any of its chats were continued across a break is not recorded, beyond its largest history writing session, which stopped twice on usage limits and resumed both times (§7, added 17 Nov 2026).

## 4 · A token budget per task type

Since no allowance per window is published (§1), a budget here is a ceiling on what may enter the window for one task, and the point at which its chat stops. It is written in what enters, not in tokens, because no page read gives the exchange rate between tokens and a plan's limit (§1). BW2's routing table gave each recurring task a tier and an effort, and left a "How often" column for this unit (BW2, Deliverable Part 2). The table below takes BW2's ten rows and adds the three runs BW8 and BW9 introduced. Its cost column holds only what a vendor states; where nothing is stated, it says so.

| Task (BW2 row) | What may enter the window | What drives its usage (documented) | Stop line |
|---|---|---|---|
| 1. Triage and reformatting | The items to sort and the rule that sorts them | Message length; model (*Usage limit best practices*) | One pass; outside the project, so its standing files stay out (BW4 §1) |
| 2. Extraction to a table | The documents and the column list; totals by script | Attachment size; a re-upload in the same chat (*About Claude's Pro Plan Usage*) | One table; a second batch in a new chat |
| 3. Summary for a named reader | The material and who reads the summary | Message length | One summary |
| 4. A long first draft | The brief and the files it names, read by name (BW4 §2) | Conversation length; effort (*Usage limit best practices*) | The draft and its deliverable; checking in another context |
| 5. Critique of a draft | The draft, the brief and the sources it opens | Tool use; a stronger model draws faster: Fable on Max and Ultra (*Claude Fable models on your plan*) | The report; findings applied in another context |
| 6. Research with search | The question and the pages returned | "Tool usage (e.g., Research, web search)" (*Usage limit best practices*) | The facts filed with source and date; searched again only at the six-month check |
| 7. Deep research | The research brief (BW3) | Research uses limits faster; about 15× a chat's tokens on Anthropic's 2025 system (§2) | One run per question; the report filed and sampled (BW6) |
| 8. A code change | Instruction file under 200 lines; files read as needed | "Aim to keep CLAUDE.md under 200 lines" (*Manage costs effectively*) | `/clear` between unrelated tasks |
| 9. An audit against sources | The sampled claims and their sources | Tool use; model choice | The audit report |
| 10. A plan or spec | The idea, the constraints, BW5's form | Effort | One spec; the build order in a file |
| Agent run (BW9) | The brief and the scope BW9's checklist sets | "The subagent's own requests still draw on your usage"; subagents get a five-minute cache even on a subscription; agent teams "approximately 7x more tokens than standard sessions when teammates run in plan mode" (*Manage costs effectively*; *How Claude Code uses prompt caching*) | The run's done-when line; a spend cap where the tool has one |
| Scheduled task (BW8) | A self-contained prompt and the repositories and connectors it names | Draws subscription usage like an interactive session; at most 100 scheduled runs an hour per account; all your connectors included unless removed (*Automate work with scheduled tasks*) | One run's outcome; the task paused when its outcome stops being used |
| Skill trigger test (BW8) | One request, in a new chat, 48 runs in all (BW8 §7) | Each installed skill's metadata loads at startup, about 100 tokens a skill ([Anthropic, *Agent Skills*](https://platform.claude.com/docs/agents-and-tools/agent-skills/overview), read 16 Nov 2026; vendor) | The 48 runs recorded; rerun only after the description changes |

Three readings (arithmetic and stated opinion, on the table).

1. **Standing layers are a per-turn tax.** Twenty installed skills at about 100 tokens each add about 2,000 tokens to every turn of every chat where they are installed (arithmetic on *Agent Skills*; BW4 §2 made the same count). A light task run inside a heavy project pays the project's standing files on every turn, which is why rows 1 to 3 run outside it.
2. **The dearest rows are the ones that multiply.** Research, agent runs and agent teams all multiply a chat's tokens by a published factor (about 15× and 4× on Anthropic's 2025 research system, §2; about 7× for agent teams in plan mode, the table above), each against its own baseline (BW9 §4), and each is the row most worth running once and filing.
3. **On a subscription, watch two numbers.** Settings > Usage shows the session and weekly bars (§1); in Claude Code on Pro, Max, Team or Enterprise, `/usage` also attributes recent usage to "skills, subagents, plugins, and individual MCP servers", and recommends changes for any behaviour behind 10% or more of it (*Manage costs effectively*). The spend cap for a Claude Code run on the API is `--max-budget-usd`, which the costs page names; BW9 gives the rest of an agent's guardrails.

**The case** (anecdote). The case file does not record how often any of the ten tasks recurs, or any cost per task (Academy case file §9; BW2, Deliverable Part 1); over the six reviewed days it records the model by task type, with unit writing on Opus 5.5 in 14 of 15 chats, audits and fresh checks on Fable 5.1 in 5 of 6, and none of the 53 chats on Sonnet 5.5 or Haiku 5.5 (§8, added 17 Nov 2026). It records the volume of the one task it was built for: 194 units by 11 Nov 2026, each 2,000 to 6,000 words by guide (§1), and 36 fresh checks (§5). Its usage review counted 31 chats on Opus, 18 on Fable and 4 on both over six days (§8). Every frequency for the case is therefore "not recorded" except row 4 and row 5 (Deliverable, the paragraph after Part 1).

## 5 · Caching, as far as it is documented

Caching is the one mechanism that makes a re-sent history cheaper. How much is documented depends on where you work.

**On the API.** "By default, the cache has a 5-minute lifetime"; a one-hour lifetime costs more. Cache writes cost 1.25 times the base input price for five minutes and 2 times for one hour; cache reads cost 0.1 times, with exceptions: 0.05 times on Opus 5.5 and Sonnet 5.5, 0.025 times on Fable 5.2 and Fable 5.1. The shortest cacheable prompt on the newest models is 512 tokens ([Anthropic, *Prompt caching*](https://platform.claude.com/docs/build-with-claude/prompt-caching), read 16 Nov 2026; vendor). The page does not mention claude.ai or subscriptions.

**In Claude Code.** The cache is a prefix: "The match is exact, so a change anywhere in the prefix recomputes everything after it" (*How Claude Code uses prompt caching*). On a Claude subscription within the plan's included usage, the main conversation gets one hour and almost everything else five minutes: "Subagents fall outside the main-conversation TTL bucket, so they get five minutes even on a subscription". Once a session draws on usage credits, the main conversation drops to five minutes (same page). Actions that break the cache include switching models, changing effort on most models, turning on fast mode, connecting or removing an MCP server when tool search is off, and compacting; actions that keep it include editing files, invoking skills and rewinding (same page). A fork "inherits the parent's system prompt, tools, and conversation history exactly, so its first request reads the parent's cache"; a fresh subagent does not (same page).

That last fact has a cost side BW9 §4 did not need. A fork is the cheaper way to hand off a side task, because it reads a warm cache; it is also a reviewer that has seen the writing (BW9 §4). When a check must be independent (BW6 §4), pay for a fresh subagent, a new session or a custom subagent: the independence is what you are buying (stated opinion).

**On claude.ai.** Three sentences are all that is published. "Content in projects is cached and counts less against your limits when reused" (*Usage limit best practices*); "cached tokens count less than uncached portions toward your usage limits" (*About Claude's Pro Plan Usage*); and "Caches expire after a period of inactivity" (*Usage limit best practices*). The best-practices page also lists "Claude remembers context from earlier in the conversation" under caching, without a rate or a lifetime. How much less a cached token counts, how long a claude.ai cache lives, and whether a new chat in the same project reads the project's cache are not stated (BW4 §4 found the last unstated on 15 Nov 2026).

**What follows** (stated opinion). Caching rewards three habits you already have reasons for: fixed standing layers at the top of the window (BW4 §1), model and effort chosen before the first message (BW2, rule 1), and work done in one sitting. It punishes a long chat resumed after a break, which is §3's case for a new chat with a handoff note.

## 6 · What the vendor keeps, for how long, and the settings that govern training

All facts below are Anthropic's, for its consumer plans unless marked, as read 16 Nov 2026.

**Chats.** The retention page covers Free, Pro and Max and Claude Code used through those accounts, and is dated 1 July 2026. "Anthropic retains your personal data for as long as reasonably necessary"; a deleted chat leaves your history at once and is "Deleted from our back-end storage systems within 30 days". With the model-improvement setting on, new or resumed chats and coding sessions may be kept de-identified "for up to 5 years in our model training pipelines". A chat flagged by the trust and safety systems keeps its inputs and outputs "for up to 2 years" and its classification scores for up to seven. Data tied to a thumbs up or down, or a bug report, is kept five years. "Your Incognito chats are not used to improve Claude" ([Anthropic Privacy Center, *How long do you store my data?*](https://privacy.claude.com/en/articles/10023548-how-long-do-you-store-my-data), 1 Jul 2026, read 16 Nov 2026; vendor).

**The training setting.** It is a toggle under Settings > Privacy. Off, "we will not use any new chats and coding sessions you have with Claude for future model training"; and "Your data will still be included in model training that has already started"; chats flagged by safety classifiers may still be used to improve internal trust and safety models ([Anthropic Privacy Center, *How do I change my model improvement privacy settings?*](https://privacy.claude.com/en/articles/12109829-how-do-i-change-my-model-improvement-privacy-settings), 3 Aug 2026, read 16 Nov 2026; vendor). The terms change that created it: "These updates apply to users on our Claude Free, Pro, and Max plans"; they "do not apply to services under our Commercial Terms"; retention is five years if you allow training and "our existing 30-day data retention period" if you do not, for new or resumed chats; and "If you delete a conversation with Claude it will not be used for future model training" ([Anthropic, *Updates to Consumer Terms and Privacy Policy*, 28 Aug 2025](https://www.anthropic.com/news/updates-to-our-consumer-terms), read 16 Nov 2026; vendor). The 2026 retention page does not restate the 30 days for chats you keep; it gives 30 days only for deleted chats.

**Who can read them.** "Access is limited to a small number of personnel involved in model training", and "We automatically de-link your data from your user ID (like your email address) before any review". The same article asks for care with financial details such as card and bank numbers, health records, passwords and login credentials, and confidential business or personal documents; it covers Free, Pro, Max and Ultra and Claude Code on those accounts ([Claude Help Center, *I would like to input sensitive data into my chats with Claude. Who can view my conversations?*](https://support.claude.com/en/articles/8325621-i-would-like-to-input-sensitive-data-into-my-chats-with-claude-who-can-view-my-conversations), labelled "Updated over 2 weeks ago", read 16 Nov 2026; vendor).

**Memory.** "Claude saves memory as a set of individual topics as you chat, rather than summarizing conversations after they end." "Each project has its own memory"; a project's chats use that memory and your memory from chats outside projects, never another project's, and "Use account memory" on the project's page separates them fully. By default memory does not store personal or sensitive subjects such as health, politics or religion, unless you turn on "Include sensitive topics in memory". "Some information is never saved to memory, even if you ask": government ID numbers, criminal history, financial account numbers and immigration status. When a chat is deleted, including under a retention period, the memory entries generated from it are not removed; you delete them yourself under Settings > Your Claude, "Manage" next to "Your memory". An organisation's custom retention period for chats also applies to memory, project memory excepted. The article does not say how much memory is loaded into a chat ([Claude Help Center, *Use Claude's chat search and memory to build on previous context*](https://support.claude.com/en/articles/11817273), labelled "Updated this week", read 16 Nov 2026; vendor). On plans: "Memory is on by default on Free, Pro, Max, and Ultra plans across web, desktop, and mobile"; an undated update note on the same post says memory is now on by default for members of most Team and Enterprise organisations created on or after 31 October 2026, and older organisations are unchanged ([Anthropic, *Claude's memory works everywhere, and you decide what's in it*](https://claude.com/resources/articles/claudes-memory-works-everywhere-and-you-decide-whats-in-it), 25 Aug 2026, read 16 Nov 2026; vendor). The help article says owners control whether memory is available on Team and Enterprise, and "Owners can't turn memory on for individual users".

**Projects.** "Context is not shared across chats within a project unless the information is added into the project knowledge base." The article describes sharing a project on Team and Enterprise and deleting one, and says nothing about retention, training or what happens to the files after deletion ([Claude Help Center, *How can I create and manage projects?*](https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects), labelled "Updated over a week ago", read 16 Nov 2026; vendor). The retention page does not mention projects, memory or uploaded files either. So no retention period for project files is published on the pages read.

**Incognito.** Incognito chats are not saved to your history or to memory, are kept 30 days by default, "are not used for training", are "currently only available for chats outside of projects", and "Once closed, incognito chats cannot be reopened"; they are available on every plan ([Claude Help Center, *Use incognito chats*](https://support.claude.com/en/articles/12260368-use-incognito-chats), labelled "Updated over 2 weeks ago", read 16 Nov 2026; vendor).

**Commercial plans.** Anthropic's privacy centre states that by default it does not use inputs or outputs from its commercial products, such as Claude for Work and the API, to train models, unless you send feedback or otherwise opt in; feedback stores the conversation for up to five years ([Anthropic Privacy Center, *Is my data used for model training?*](https://privacy.claude.com/en/articles/7996868-is-my-data-used-for-model-training), 18 Aug 2026, read 16 Nov 2026; vendor). The page gives no general retention period for commercial chats.

| What | Kept | Source (all read 16 Nov 2026) |
|---|---|---|
| A chat you keep | "as long as reasonably necessary" | Retention page, 1 Jul 2026 |
| A chat you delete | Gone from history at once; back-end within 30 days | Retention page |
| Training off (a chat you keep) | "our existing 30-day data retention period" in the 2025 post; the 2026 retention page gives no period beyond "as long as reasonably necessary", and 30 days only for a deleted chat | Consumer terms post, 28 Aug 2025; retention page, 1 Jul 2026 |
| Training on (new or resumed chats) | Up to 5 years, de-identified | Retention page; consumer terms post |
| A chat with feedback | 5 years | Retention page; commercial page for Claude for Work |
| A flagged chat | Inputs and outputs up to 2 years; scores up to 7 years | Retention page |
| An incognito chat | 30 days by default; never trained on | Incognito article |
| A memory entry | Until you delete it; survives the chat's deletion | Memory article |
| A project file | Not stated | Projects article; retention page silent |

**The deletion sequence** (stated opinion, on the table). Deleting a chat that held private material is three steps: delete the chat; delete the memory entries it wrote, since the chat's deletion leaves them; and know that if training was on when the chat ran, a de-identified copy may already be in a training run that has started. Rating a chat with a thumb keeps its data five years, so do not rate chats that hold private material.

## 7 · Which material belongs in memory, in a project, in a private store, or nowhere

Four places can hold what you work with. Each has properties from §6 and from earlier units that decide what belongs there.

- **Memory** is written by a model about your chats, loaded in amounts nobody publishes, reaches every chat outside projects and, unless a project's "Use account memory" is off, every project's chats, and survives the deletion of the chat it came from (§6; BW1 §3). With memory on, a project's own memory can also be referenced in chats outside projects ([Claude Help Center, *Use Claude's chat search and memory to build on previous context*](https://support.claude.com/en/articles/11817273), read 16 Nov 2026; vendor). BW4 §1 put it as the wrong home for a rule you need held exactly.
- **A project's knowledge** loads into every chat in that project while the project is small, and is searched once it is large (BW4 §1, §3); its retention is not stated (§6). Its output goes wherever the project's work goes.
- **A private store** is a folder or repository you control, read by a chat only when you name a file (BW4 §2). What it holds enters a vendor's systems only when a chat reads it, and then under the chat's retention rules (§6). A repository adds one hazard: BW9 §7 uses version control as the undo, and a commit is designed to be kept.
- **Nowhere in this account** is the place for what no vendor setting can make safe for you to send: credentials, and material you have no right to put on a third party's servers.

| Material | Memory | Project | Private store | Nowhere | Basis |
|---|---|---|---|---|---|
| Facts about you that you would say to anyone | Yes | Yes | Yes | | Memory is meant for facts that come up unprompted (BW4 §1) |
| Rules and method | No | Yes, if small | Yes, canonical | | BW4 §1: rules held exactly belong in a file; memory is model-written |
| Drafts, raw notes, working files | No | No | Yes | | Read by name when needed (BW4 §2); no retention stated for project files (§6) |
| Health, beliefs and other sensitive facts | No | No | Yes, if you need them | | Memory excludes them by default; "Include sensitive topics in memory" stays off (§6) |
| Other people's personal data | No | No | Only with their consent and a reason | | Stated opinion; the sensitive-data article asks for care (§6) |
| Work material your employer has not cleared | No | No | No | Yes | §8: the consumer terms are not your employer's terms |
| Passwords, keys, card, bank and ID numbers | No | No | No | Yes | Sensitive-data article and memory article (§6); a commit is designed to be kept (BW9 §7) |

```viz
{
 "kind": "matrix",
 "cols": ["Memory", "Project", "Private store", "Nowhere"],
 "rows": [
  {"label": "Facts you would say to anyone", "cells": [{"mark": "yes", "tone": 3}, {"mark": "yes", "tone": 3}, {"mark": "yes", "tone": 3}, null]},
  {"label": "Rules and method", "cells": [{"mark": "no", "tone": 1}, {"mark": "if small", "tone": 4}, {"mark": "canonical", "tone": 3}, null]},
  {"label": "Drafts, raw notes, working files", "cells": [{"mark": "no", "tone": 1}, {"mark": "no", "tone": 1}, {"mark": "yes", "tone": 3}, null]},
  {"label": "Health, beliefs, sensitive facts", "cells": [{"mark": "no", "tone": 1}, {"mark": "no", "tone": 1}, {"mark": "if needed", "tone": 4}, null]},
  {"label": "Other people's personal data", "cells": [{"mark": "no", "tone": 1}, {"mark": "no", "tone": 1}, {"mark": "with consent", "tone": 4}, null]},
  {"label": "Work material not cleared", "cells": [{"mark": "no", "tone": 1}, {"mark": "no", "tone": 1}, {"mark": "no", "tone": 1}, {"mark": "yes", "tone": 2}]},
  {"label": "Passwords, keys, card, bank and ID numbers", "cells": [{"mark": "no", "tone": 1}, {"mark": "no", "tone": 1}, {"mark": "no", "tone": 1}, {"mark": "yes", "tone": 2}]}
 ],
 "caption": "Where each kind of material belongs, the table in §7 of this unit: stated opinion built on the vendor facts in §6 (Claude Help Center, Use Claude's chat search and memory to build on previous context, and the sensitive-data article, both read 16 Nov 2026) and on BW4 §1 to §2 and BW9 §7."
}
```

**The case** (anecdote). Academy keeps everything in one private repository: course texts, briefs, build scripts, method, backlog and changelog (Academy case file §1). A structure audit of the project found, among seventeen findings, private terms reaching a public build (§7). A check now exists: no private term may appear in the public course's data folder, checked by a script against a list, and the fresh checker also checks each unit against it (§7 note). The case file itself was compiled with private details removed (header). On the Project's setup of 28 Oct 2026 account memory flowed into the Project beside its own memory store, the model called the memory tool in 6 of 53 reviewed chats, in the parts read, and on 16 Nov 2026 the setting was not visible in the records (§7, §8, added 17 Nov 2026); what memory held is not recorded, so the case's memory column is blank in the deliverable. One project's leak and fix shows the failure is possible; it does not show how often it happens.

## 8 · Work material and your employer's policy: a question for you

This section gives the facts the vendors publish and the questions they leave to you. It is information, not legal advice.

**The facts** (vendor, read 16 Nov 2026). Anthropic's consumer terms change of 2025 applies to Free, Pro and Max and does not apply to services under its Commercial Terms (§6). Its commercial products do not train on inputs or outputs by default (§6). Its sensitive-data article asks for care with confidential business documents (§6). Google's Gemini Apps Privacy Hub says that with a work or school account, use of Gemini Apps "may be subject to different data handling terms", and asks: "Please don’t enter confidential information that you wouldn’t want a reviewer to see" ([Google, *Gemini Apps Privacy Hub*](https://support.google.com/bard/answer/13594961), last updated 26 Oct 2026, read 16 Nov 2026; vendor). OpenAI's Data Controls FAQ points professionals who need more control of their data to its business plans and their privacy policies ([OpenAI, *Data Controls FAQ*](https://help.openai.com/en/articles/7730893-data-controls-faq), labelled "Updated over 4 months ago", read 16 Nov 2026; vendor).

**What they leave to you.** Which terms govern the account you are using is a fact about your account; whether your employer allows its material on that account is a fact about your employer. No vendor page can answer the second. Before any work material enters a chat, answer five questions in writing:

1. Does my employer have a written policy on AI tools, and which tools and plans does it approve?
2. Is the account I am using a personal consumer account or one my employer provides under its own terms?
3. On a personal account, is the training setting off, and does the policy allow any work material there at all?
4. Does the material include other people's personal data, client material or anything under a confidentiality agreement?
5. Who do I ask when the policy is silent, and have I asked?

If any answer is "I don't know", the material goes nowhere in your account (§7) until it is answered (stated opinion). The case file holds no fact about an employer, so the case cannot illustrate this section.

## 9 · On other tools

The principles in §1 to §8 (meter what enters the window when the allowance is unpublished; a long chat re-sends its history; a new chat is cheaper after a cache expires; know what the vendor keeps and the setting that governs training; sort material by where it can safely live) hold for any current assistant. The detail is Claude's. Below, each Claude-specific claim, with the equivalent where the other vendor's own documentation was found (all read 16 Nov 2026). OpenAI's ChatGPT Pro help page, its Memory FAQ and its business-data page each failed to load and were not checked; OpenAI's pages failed in the same way for BW1, BW4, BW5, BW6 and BW9.

| Claim in this unit | Claude | ChatGPT (OpenAI) | Gemini (Google) |
|---|---|---|---|
| Usage resets on a five-hour window under a weekly limit; no fixed count (§1) | [*How do usage and length limits work?*](https://support.claude.com/en/articles/11647753-how-do-usage-and-length-limits-work); [*Pricing*](https://claude.com/pricing) | Not checked: the plan page failed to load | Limits refresh every five hours until a weekly limit, as multiples of a standard limit, and "may change": [*Gemini Apps limits & feature availability*](https://support.google.com/gemini/answer/16275805) |
| Context window per plan (§1) | 1M for current models: [*Context window on paid plans*](https://support.claude.com/en/articles/8606394-how-large-is-the-context-window-on-paid-claude-ai-plans) | Not checked | 32k without a plan, 128k on AI Plus, 1 million on AI Pro and Ultra: [*Gemini Apps limits & feature availability*](https://support.google.com/gemini/answer/16275805) |
| Deep research costs more of the limit (§2) | [*Use research on Claude*](https://support.claude.com/en/articles/11088861-use-research-on-claude) | Not checked: OpenAI's deep-research pages failed to load for BW6 | Deep Research rated "High" in relative usage cost: [*Gemini Apps limits & feature availability*](https://support.google.com/gemini/answer/16275805) |
| Cache lifetimes and prices (§5) | [*Prompt caching*](https://platform.claude.com/docs/build-with-claude/prompt-caching); [*How Claude Code uses prompt caching*](https://code.claude.com/docs/en/prompt-caching) | API only: caching is on by default for supported models; on GPT-5.6 and later a default minimum lifetime of 30 minutes, and cache reads at 0.1× the input rate on most of those models and 0.05× on GPT-6.1 Sol and GPT-6.1 Terra: [*Prompt caching*](https://developers.openai.com/api/docs/guides/prompt-caching), read 16 Nov 2026; ChatGPT plans not checked | API only: implicit caching on by default for Gemini 2.5 and newer; an explicit cache defaults to one hour: [*Context caching*](https://ai.google.dev/gemini-api/docs/generate-content/caching), a page labelled Legacy, read 16 Nov 2026; Gemini Apps plans not checked |
| A training setting; off stops future use (§6) | [*Model improvement settings*](https://privacy.claude.com/en/articles/12109829-how-do-i-change-my-model-improvement-privacy-settings) | "Improve the model for everyone"; off, new conversations are not used to train: [*Data Controls FAQ*](https://help.openai.com/en/articles/7730893-data-controls-faq) | Keep Activity off: chats not used for training unless you send feedback, kept 72 hours: [*Gemini Apps Privacy Hub*](https://support.google.com/bard/answer/13594961) |
| Retention periods (§6) | [*How long do you store my data?*](https://privacy.claude.com/en/articles/10023548-how-long-do-you-store-my-data) | Not checked beyond temporary chats | Activity auto-deleted after 18 months by default (3 or 36 selectable); reviewed chats kept up to three years: [*Gemini Apps Privacy Hub*](https://support.google.com/bard/answer/13594961) |
| A chat outside history and training (§6) | Incognito, 30 days: [*Use incognito chats*](https://support.claude.com/en/articles/12260368-use-incognito-chats) | Temporary Chats not used for training, deleted within 30 days: [*Data Controls FAQ*](https://help.openai.com/en/articles/7730893-data-controls-faq) | Temporary chats not used to improve Google AI with human reviewers: [*Gemini Apps Privacy Hub*](https://support.google.com/bard/answer/13594961) |
| Memory survives chat deletion; sensitive topics off by default (§6) | [*Chat search and memory*](https://support.claude.com/en/articles/11817273) | Not checked: the Memory FAQ failed to load (BW1 §10 cites an older OpenAI post) | No equivalent found in the pages read |
| Work accounts under other terms (§8) | [*Is my data used for model training?*](https://privacy.claude.com/en/articles/7996868-is-my-data-used-for-model-training) | Not checked: the business-data page failed to load | Work or school accounts "may be subject to different data handling terms": [*Gemini Apps Privacy Hub*](https://support.google.com/bard/answer/13594961) |

## Deliverable · Usage rules, a table of where material belongs, and the templates

Three parts. Part 1 is twelve numbered usage rules, each with its source and evidence grade, a line saying what in a record of your own chats shows the rule kept or broken (DD-BW3 audits a reader's record against these), and the Academy case's instance where the case file holds one. Part 2 is the table of where material belongs, on the case. Part 3 holds the templates. Product facts as read 16 Nov 2026; re-check on 16 May 2027.

### Part 1 · Usage rules, on the Academy case

| # | Rule | Source and grade | What your record shows | Academy case (anecdote) |
|---|---|---|---|---|
| 1 | **One task, one chat.** A new task gets a new chat (Claude Code: `/clear`). | "Stale context wastes tokens on every subsequent message" ([*Manage costs effectively*](https://code.claude.com/docs/en/costs)); BW4 §4. Documented practice | Chats that cover more than one task, by count | One unit per context (case file §2) |
| 2 | **Back after a break, a new chat with a handoff note.** A break longer than the cache lifetime (an hour, by analogy, on claude.ai) ends the chat; the note carries decisions, open items and file paths. | First message after a break pays the full history ([*Usage limit best practices*](https://support.claude.com/en/articles/9797557-usage-limit-best-practices); [*Manage costs effectively*](https://code.claude.com/docs/en/costs)); one hour in Claude Code on a subscription ([*How Claude Code uses prompt caching*](https://code.claude.com/docs/en/prompt-caching)). Documented practice; the claude.ai hour is stated opinion | Chats resumed after a gap of over an hour | Each chat ends by writing the next prompt (§2); one history writing session stopped twice on usage limits and resumed both times (§7); resumption across other breaks not recorded |
| 3 | **Model and effort set before the first message.** To change either, a new chat. | A model switch recomputes the whole request; an effort change does too on most models ([*How Claude Code uses prompt caching*](https://code.claude.com/docs/en/prompt-caching)); BW2 rule 1. Documented practice | Mid-chat switches of model or effort | 4 of 53 reviewed chats switched model (§8); effort recorded in none of them (§2) |
| 4 | **A file is read once per chat, by name, and never pasted or re-uploaded.** | "Don't re-upload files within the same conversation" ([*About Claude's Pro Plan Usage*](https://support.claude.com/en/articles/8324991-about-claude-s-pro-plan-usage)); minimal file reads ([*Manage costs effectively*](https://code.claude.com/docs/en/costs)); BW4 §2. Documented practice | Repeated uploads or pastes of one file in one chat | Each writer's context sees only its brief and the filed units (§2); how they reached it is not recorded |
| 5 | **A paste carries only what this output needs, in one message.** | "Provide all relevant data in a single, well-structured message" ([*Usage limit best practices*](https://support.claude.com/en/articles/9797557-usage-limit-best-practices)); BW3 §5. Documented practice | Pastes larger than the part the output used | 7 chats on the first reviewed day carried a whole unit pasted (§8); how much of each the output used is not recorded |
| 6 | **A question is researched once and filed with its source and date;** searched again only at its six-month check. Deep research runs once per question. | Research "can use up your limits faster" ([*Use research on Claude*](https://support.claude.com/en/articles/11088861-use-research-on-claude)); about 15× a chat's tokens on the 2025 system ([Hadfield et al.](https://www.anthropic.com/engineering/multi-agent-research-system)). Documented practice; 15× measured by the vendor in 2025 | The same question researched twice | A staleness check six months after live search (§2) |
| 7 | **Tools and connectors are off unless the chat uses them.** | "Tools and connectors are token-intensive" ([*How do usage and length limits work?*](https://support.claude.com/en/articles/11647753-how-do-usage-and-length-limits-work)); BW4 §1. Documented practice | Chats with connectors on that called none | BW9's fresh checker and corrections checkers ran with web search, page fetch and scripts (§7 note); where transcripts were kept, writers used search and fetch and no connector, and eight connectors were connected that no Project procedure used (§7, added 17 Nov 2026) |
| 8 | **Light tasks run outside the project.** | Standing layers load every turn (BW4 §2); about 100 tokens per installed skill ([*Agent Skills*](https://platform.claude.com/docs/agents-and-tools/agent-skills/overview)). Documented mechanism; the rule is stated opinion | Short tasks run inside a heavy project | All 53 reviewed chats ran in the project (§8), whose knowledge held 33 files, 907,260 characters, on 29 Oct 2026; whether it ran in retrieval mode is not known (§7) |
| 9 | **Every background run has an end.** Scheduled tasks, loops, agent teammates and subagents get a done-when line, a spend cap where the tool has one, and are stopped when their output stops being used. | Scheduled tasks draw usage like interactive sessions ([*Automate work with scheduled tasks*](https://code.claude.com/docs/en/web-scheduled-tasks)); idle tasks send full context; teammates keep consuming tokens ([*Manage costs effectively*](https://code.claude.com/docs/en/costs)); BW9 §7. Documented practice | Runs without an end condition; usage attributed to loops and subagents in `/usage` | Agents' spend caps not recorded (§9); figure passes ran at most eight agents at a time, re-run auditors were held to 40 searches each, and four figure-pass asks gave an attempt cap; no scheduled task appears in the records (§7) |
| 10 | **The usage bars are read before a heavy task, and credits carry a monthly cap.** | Settings > Usage bars ([*Usage limit best practices*](https://support.claude.com/en/articles/9797557-usage-limit-best-practices)); "Adjust limit" ([*Manage usage credits for paid Claude plans*](https://support.claude.com/en/articles/12429409-manage-usage-credits-for-paid-claude-plans)). Documented practice | Heavy tasks stopped by a limit; credit spend without a cap | Plan not recorded (§9); a history writing session stopped twice on usage limits, and an audit chat was stopped by a shorter-window limit after 18% of the auditing model's weekly allowance (§7) |
| 11 | **Material goes where Part 2 puts it;** "Include sensitive topics in memory" stays off; "Use account memory" is off in any project whose output is published. | Memory article ([*Chat search and memory*](https://support.claude.com/en/articles/11817273)); sensitive-data article; §7. Stated opinion on documented settings | Private or work material found in chats, memory topics or project files | Private-terms check by script on the public course's data (§7 note); account memory flowed into the Project on the setup of 28 Oct 2026, the setting not visible in the records of 16 Nov 2026 (§7); whether "Include sensitive topics in memory" was on is not recorded (§9) |
| 12 | **Training and deletion are decisions, written down once.** The training setting is chosen and recorded; deleting a private chat means deleting its memory entries too; private chats get no feedback rating; a one-off private question outside a project goes in an incognito chat. | Retention page ([*How long do you store my data?*](https://privacy.claude.com/en/articles/10023548-how-long-do-you-store-my-data), 1 Jul 2026); training setting (3 Aug 2026); memory article; [*Use incognito chats*](https://support.claude.com/en/articles/12260368-use-incognito-chats). Documented facts; the rule is stated opinion | The setting's value and the date it was chosen; deleted chats whose memory entries remain | Not recorded |

**The budget each rule protects.** Rules 1 to 8 keep each task inside §4's ceiling; on the case, row 4 (a long first draft) is the one with a recorded volume: 194 units by 11 Nov 2026, 2,000 to 6,000 words each by guide (case file §1), and row 5 (critique) 36 fresh checks (§5). Every other "How often" for the case is not recorded.

### Part 2 · Where material belongs, on the Academy case

| Material | Memory | Project | Private store | Nowhere | What the case file records |
|---|---|---|---|---|---|
| Method, briefs, backlog, changelog | [NOT IN CASE FILE] | Backlog and changelog: copies, which each chat that works a row rewrites in full (§7); method and briefs not recorded | Yes: one private repository (§1) | | §1, §2, §7 |
| Course texts, drafts and working files | [NOT IN CASE FILE] | Filed units were removed from the Project's knowledge on 15 Nov 2026; units are not mirrored (§7) | Course texts: the same repository (§1); a third writer resumed from the second's working files (§7); the usage review's working files were kept in its writer's packet folder in the session and are not published (§8); where other drafts and working files were kept is not recorded | | §1, §7, §8 |
| Private terms (the list the case file's §7 note names) | [NOT IN CASE FILE] | [NOT IN CASE FILE] | The private repository, not the public one the site is deployed from (§7) | Out of the public course: a script checks its data folder against a list, and the fresh checker checks each unit (§7 note); the case file itself was compiled with private details removed (header) | §7, §7 note, header |
| Other people's personal data | [NOT IN CASE FILE] | [NOT IN CASE FILE] | [NOT IN CASE FILE] | [NOT IN CASE FILE] | Not recorded |
| Work material for an employer | [NOT IN CASE FILE] | [NOT IN CASE FILE] | [NOT IN CASE FILE] | [NOT IN CASE FILE] | Not recorded |
| Passwords, keys, card, bank and ID numbers | [NOT IN CASE FILE] | [NOT IN CASE FILE] | [NOT IN CASE FILE] | [NOT IN CASE FILE] | Not recorded |

Where a cell is [NOT IN CASE FILE], this unit's rule from §7 applies to the case as to any project; the table records only what the case did.

*Sources for Parts 1 and 2:* the evidence is §1 to §8 of this unit, each cell pointing to its source; Academy facts are from Academy case file §1, §2, §5, §7, §7 notes, §8 and §9, and the file's header. The case file does not record the plan, a token or window measure for a single unit, the tools of agents beyond those §7 names, or any employer material (§9), or what memory held.

### Part 3 · Templates for your project

**Template A · Usage rules.** Copy the twelve rules. For each, fill the blanks; delete a rule only with a written reason.

| # | Rule | Source and grade | What your record shows | Your instance |
|---|---|---|---|---|
| 1 to 12 | [*the rule from Part 1, reworded only where your tool differs; name your tool*] | [*the vendor page for your tool, read on [date], with its grade; "not found" where your vendor publishes nothing*] | [*the count you will take from your chat history to see the rule kept or broken: chats, switches, uploads, gaps over an hour*] | [*one example from your project, or "none yet"*] |
| 13 | [*a rule of your own, from a waste you have seen twice*] | [*its source, or "stated opinion"*] | [*the count that tests it*] | [*the two instances*] |

**Template B · Budget per routing row.** One row per row of your BW2 routing table.

| Task (BW2 row) | How often | What may enter the window | What drives its usage on your tool | Stop line |
|---|---|---|---|---|
| [*task name, as in your routing table*] | [*times a week or month, from your records; "unknown" until counted*] | [*the files and text the task needs, named; nothing else*] | [*the vendor's documented factor: length, attachments, tools, model, effort, research, agents*] | [*the output that ends the chat, and where the next step runs*] |

**Template C · Where material belongs.** One row per kind of material your project handles.

| Material | Memory | Project | Private store | Nowhere | Basis |
|---|---|---|---|---|---|
| [*a kind of material in your project, named as you would name it to a colleague*] | [*yes or no, and why, from §6 and §7*] | [*yes or no; for yes, the project whose output it can reach*] | [*yes or no; for yes, the folder or repository, and who else can read it*] | [*yes if no place in your account is safe for it*] | [*the vendor fact, your employer's policy, or "stated opinion"*] |

**Template D · Settings and answers, written once.**

- Training setting: [*on or off*], chosen on [*date*], because [*reason*].
- Memory: [*on or off*]; sensitive topics in memory: [*on or off*]; "Use account memory" in [*each project whose output is published*]: [*on or off*].
- Usage credits: [*on or off*]; monthly cap: [*amount, currency*].
- Employer questions (§8): 1 [*answer*] · 2 [*answer*] · 3 [*answer*] · 4 [*answer*] · 5 [*answer, with the name of the person asked and the date*].
- Re-check by: [*six months after the date you read the vendor pages*], re-reading [*the plan, usage, caching, retention, memory and training pages for your tool*].

## Sources

All web sources read on 16 November 2026, unless a date of their own is given.

- Claude. *Pricing*. https://claude.com/pricing
- Claude Help Center. *How do usage and length limits work?* Labelled "Updated over a week ago". https://support.claude.com/en/articles/11647753-how-do-usage-and-length-limits-work
- Claude Help Center. *Claude Fable models on your plan*. Labelled "Updated this week". https://support.claude.com/en/articles/15424964-claude-fable-models-on-your-plan
- Claude Help Center. *Manage usage credits for paid Claude plans*. Labelled "Updated this week". https://support.claude.com/en/articles/12429409-manage-usage-credits-for-paid-claude-plans
- Claude Help Center. *Usage limit best practices*. Labelled "Updated over 2 weeks ago". https://support.claude.com/en/articles/9797557-usage-limit-best-practices
- Claude Help Center. *About Claude's Pro Plan Usage*. Labelled "Updated over a week ago". https://support.claude.com/en/articles/8324991-about-claude-s-pro-plan-usage
- Claude Help Center. *How large is the context window on paid Claude plans?* Labelled "Updated this week". https://support.claude.com/en/articles/8606394-how-large-is-the-context-window-on-paid-claude-ai-plans
- Claude Help Center. *Use research on Claude*. Labelled "Updated over 2 weeks ago". https://support.claude.com/en/articles/11088861-use-research-on-claude
- Claude Help Center. *I would like to input sensitive data into my chats with Claude. Who can view my conversations?* Labelled "Updated over 2 weeks ago". https://support.claude.com/en/articles/8325621-i-would-like-to-input-sensitive-data-into-my-chats-with-claude-who-can-view-my-conversations
- Claude Help Center. *Use Claude's chat search and memory to build on previous context*. Labelled "Updated this week". https://support.claude.com/en/articles/11817273
- Claude Help Center. *How can I create and manage projects?* Labelled "Updated over a week ago". https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects
- Claude Help Center. *Use incognito chats*. Labelled "Updated over 2 weeks ago". https://support.claude.com/en/articles/12260368-use-incognito-chats
- Anthropic Privacy Center. *How long do you store my data?* 1 July 2026. https://privacy.claude.com/en/articles/10023548-how-long-do-you-store-my-data
- Anthropic Privacy Center. *How do I change my model improvement privacy settings?* 3 August 2026. https://privacy.claude.com/en/articles/12109829-how-do-i-change-my-model-improvement-privacy-settings
- Anthropic Privacy Center. *Is my data used for model training?* 18 August 2026. https://privacy.claude.com/en/articles/7996868-is-my-data-used-for-model-training
- Anthropic. *Updates to Consumer Terms and Privacy Policy*. 28 August 2025. https://www.anthropic.com/news/updates-to-our-consumer-terms
- Anthropic. *Claude's memory works everywhere, and you decide what's in it*. 25 August 2026, with an undated update note. https://claude.com/resources/articles/claudes-memory-works-everywhere-and-you-decide-whats-in-it
- Anthropic. *Manage costs effectively*. Claude Code documentation. https://code.claude.com/docs/en/costs
- Anthropic. *How Claude Code uses prompt caching*. Claude Code documentation. https://code.claude.com/docs/en/prompt-caching
- Anthropic. *Automate work with scheduled tasks*. Claude Code documentation. https://code.claude.com/docs/en/web-scheduled-tasks
- Anthropic. *Prompt caching*. Claude Platform documentation. https://platform.claude.com/docs/build-with-claude/prompt-caching
- Anthropic. *Agent Skills*. Claude Platform documentation. https://platform.claude.com/docs/agents-and-tools/agent-skills/overview
- Hadfield, J., Zhang, B., Lien, K., Scholz, F., Fox, J. and Ford, D. *How we built our multi-agent research system*. Anthropic, 13 June 2025 (vendor). https://www.anthropic.com/engineering/multi-agent-research-system
- OpenAI. *Data Controls FAQ*. Labelled "Updated over 4 months ago". https://help.openai.com/en/articles/7730893-data-controls-faq
- Google. *Gemini Apps Privacy Hub*. Gemini Apps Help, last updated 26 October 2026. https://support.google.com/bard/answer/13594961
- Google. *Gemini Apps limits & feature availability*. Gemini Apps Help, no date shown. https://support.google.com/gemini/answer/16275805
- OpenAI. *Prompt caching*. OpenAI API documentation. https://developers.openai.com/api/docs/guides/prompt-caching
- Google. *Context caching*. Gemini API documentation, labelled Legacy. https://ai.google.dev/gemini-api/docs/generate-content/caching
- Academy case file, §1, §2, §5, §7, §7 notes, §8, §9 and header.
- Units of this course cited by section: BW1 (§1, §2, §3), BW2 (§3, §6; Deliverable, rule 1 and Part 2), BW3 (§5), BW4 (§1 to §4), BW5 (the spec form), BW6 (§1, §4, §5), BW8 (§7), BW9 (§4, §7).

## Unsure list

# BW10 · Unsure list

1. *Manage costs effectively* (Claude Code docs): no search returned the bare address; it was read at the only address search returned, https://code.claude.com/docs/en/costs?ref=t01.li, and is cited at the bare address https://code.claude.com/docs/en/costs. A check should read the bare address (F70) and confirm the quoted sentences (7x agent teams, "/clear costs nothing", the subagent and scheduled-task lines, the /usage attribution list).
2. Anthropic Privacy Center page at https://privacy.claude.com/en/articles/7996868-how-long-do-you-store-my-organization-s-data shows the headline "Is my data used for model training?" (18 Aug 2026), not the title its URL slug suggests; the fetch may have been served another article on the same host. §6 and §9 rely on it only for "commercial products not trained on by default; feedback kept up to five years". No general retention period for commercial chats was found.
3. Anthropic's help article *What is the Ultra plan?* refused the fetch (not checked, not retried). Ultra's lack of a five-hour limit rests on the pricing page ("No 5-hour limit") and *How do usage and length limits work?* (verified Ultra accounts).
4. Separate weekly Fable limit: *How do usage and length limits work?* says some plans have one; *Claude Fable models on your plan* (more recently updated) describes only a share of up to 50% of the regular weekly limit. The unit takes the Fable article and states the disagreement.
5. How long a claude.ai cache lasts, and how much less a cached token counts against a plan, are unpublished. Rule 2's one-hour break on claude.ai is Claude Code's subscription figure applied by analogy (stated opinion).
6. The model-improvement toggle's exact on-screen label was not quoted (the fetched text gave it as "Help Improve our AI models" in a summary); the unit names it only as the toggle under Settings > Privacy.
7. The update note on Anthropic's memory post (Team and Enterprise organisations created on or after 31 Oct 2026) carries no date of its own.
8. Hadfield et al.'s 4× and 15× are 2025 figures for Anthropic's 2025 research system; one search for the post was made and no newer vendor figure turned up, but no dedicated search for a 2026 figure was run.
9. BW1 §2's statement that Anthropic's model page gives 1M tokens as roughly 555k words or 2.5M Unicode characters could not be found on *Models overview* (https://platform.claude.com/docs/en/models/overview) on 16 Nov 2026 (two reads); this unit gives no characters-per-token figure.
10. ChatGPT's plan page (*What is ChatGPT Pro plans*), Memory FAQ and OpenAI's business-data page each failed to load; the "On other tools" cells for them say "not checked". The Gemini limits page shows no date.

Object: none

Fresh check 2026-11-16 (claude-opus-5-5): fix · 0 errors, 7 should-fix, 11 minor; report `audits/building-with-ai/fresh-check-BW10.md`

Correction 17 Nov 2026 (CP-4), found by W-SP1, each change checked by a fresh Opus 5.5 agent against case-academy.md
