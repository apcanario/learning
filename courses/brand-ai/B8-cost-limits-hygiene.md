---
code: B8
title: Cost, limits, hygiene
course: brand-ai · B · Using AI to Build a Brand
model: Opus 5.5
written: 2026-11-02
search: on
---

# B8 · Cost, limits, hygiene

Every product fact in this unit was read on Anthropic's own pages on 2 November 2026 and carries that date. Most help-centre pages show only a relative label ("Updated this week"); the unit gives the label as read. Three kinds of evidence are used, labelled where they appear. **Product documentation** is Anthropic's help centre, privacy centre, pricing page and developer documentation. **Arithmetic** is calculation on figures from those pages or from the filed units, shown so it can be checked by hand; nobody measured its results. **His setup** means sizes counted by script from the course's own filed units on 2 November 2026. One secondary source is used, for a date Anthropic's pages do not give, and it is labelled. Where Anthropic publishes no figure, the unit says so and gives none.

## 1 · What his plan measures, re-read on 2 November 2026

B2 §2 set out what claude.ai meters and closed on "an exchange rate per model that Anthropic does not publish". B1 §4 left B8 the rule that any model lineup, price or plan limit dated after June 2026, the models' knowledge cutoff, must be searched and dated: every such fact in this unit was searched on 2 November 2026 and carries that date. This section re-reads B2 §2's sources and says, claim by claim, what still holds.

### The plans, as of 2 November 2026

From the pricing page ([Claude, *Plans & pricing*](https://claude.com/pricing), read 2 Nov 2026; USD, tax excluded):

| Plan | Price | Usage, in the page's words | Fable |
|---|---|---|---|
| Pro | $20 a month, or $17 a month billed as $200 a year | "More usage than Free" every 5 hours and every week; the FAQ gives "at least 5x more usage per 5-hour session than Free" | Paid with usage credits |
| Max | $100 a month | "5x Pro usage every 5 hours and every week" | Included, "up to half your weekly limit" |
| Ultra | $200 a month | "No 5-hour limit" for verified accounts; "10x Pro usage every week" | Included, up to half the weekly limit |

**Ultra is new since B2.** The help article *What is the Ultra plan?* says "The Max 20x plan is now called the Ultra plan", that existing Max 20x subscribers moved to it at the same price, that "Verified Ultra accounts don't have a five-hour limit", that an unverified account has a temporary limit, and that Ultra has a weekly limit across all models plus a separate weekly limit for Fable ([Claude Help Center, article 17728952](https://support.claude.com/en/articles/17728952), read 2 Nov 2026, labelled "Updated this week"). The article gives no date for the change. FourWeekMBA dates it 30 October 2026 and attributes it to an Anthropic post on X that day ([FourWeekMBA, 30 Oct 2026](https://fourweekmba.com/ai-claude-ultra-drops-5-hour-limit-for-verified-users-at-200/); secondary report, the X post not opened).

**How the windows work.** "Most accounts have a limit that resets on a rolling five-hour session window, and paid plans add weekly limits on top" (pricing page FAQ). The Pro article says the session limit "will reset every five hours" and that Anthropic "may limit your usage in other ways, such as weekly and monthly caps or model and feature usage, at our discretion" ([Claude Help Center, *About Claude's Pro plan usage*](https://support.claude.com/en/articles/8324991-about-claude-s-pro-plan-usage), read 2 Nov 2026, labelled "Updated over a week ago"). Usage on claude.ai, Claude Code and Claude Desktop draws on one shared limit ([Claude Help Center, *Understanding usage and length limits*](https://support.claude.com/en/articles/11647753-understanding-usage-and-length-limits), read 2 Nov 2026). Settings > Usage shows progress bars for the five-hour session and the weekly limits, and for Fable where the plan includes it ([Claude Help Center, *Usage limit best practices*](https://support.claude.com/en/articles/9797557-usage-limit-best-practices), read 2 Nov 2026, labelled "Updated this week").

**What Anthropic does not publish.** No page read gives the number of tokens or messages a plan allows per five-hour window or per week. The pricing page says it outright: "there's no fixed message count." The one worked example is still the Pro article's: about 45 messages every five hours for short conversations (about 200 English sentences of 15 to 20 words) on a less compute-intensive model, "often more depending on Claude's current capacity". No page gives the rate at which each model draws the limit; the pricing page says only that "How fast you reach a limit depends on the model you use, how long your chats are, and how large your files are." No page gives the size of a weekly cap.

### B2 §2, claim by claim

B2 §2 cited its sources on 28 October 2026, and dated the usage-limit article 22 September 2026. Re-read on 2 November 2026:

| B2 §2 said | Status on 2 Nov 2026 | Source read today |
|---|---|---|
| Pro $20 monthly, $17 annual ($200 up front) | Holds | Pricing page |
| Max $100 for five times Pro per session | Holds; the page now says "every 5 hours and every week" | Pricing page |
| $200 for twenty times Pro | **Changed.** The $200 tier is Ultra, "10x Pro usage every week", no five-hour limit when verified. The Max article still describes 5x and 20x tiers and "at least 900" messages on 20x ([*About Claude's Max plan usage*](https://support.claude.com/en/articles/11014257-about-claude-s-max-plan-usage), labelled "Updated this week"), so Anthropic's pages disagree | Pricing page; Ultra article; Max article |
| Session resets every five hours; weekly limits; other caps at Anthropic's discretion | Holds | Pro article; pricing FAQ |
| Claude Code draws on the same limit | Holds | Pro article; pricing page ("shares the same usage limits") |
| About 45 messages per five hours on Pro, as defined | Holds | Pro article |
| The window is 200K tokens on every plan | **Changed, and disputed.** See below | Two help articles; pricing page |
| What draws usage (the list dated 22 Sep 2026) | Holds; the article is updated and the eight items are unchanged | Usage limit best practices |
| Project content is cached and counts less when reused | Holds | Usage limit best practices; Pro article |
| Higher effort reaches the limit sooner | Holds | [*Change the model, effort and extended thinking settings*](https://support.claude.com/en/articles/8664678-change-the-model-effort-and-extended-thinking-settings), labelled "Updated over 3 weeks ago" |
| No per-model rate is published | Holds | All of the above |
| Fable: credits on Pro; up to half the weekly limit on Max, used faster than other models | Holds, and Ultra is added with Max | [*Claude Fable models on your plan*](https://support.claude.com/en/articles/15424964-claude-fable-models-on-your-plan), labelled "Updated today" |
| Usage credits are prepaid and billed at standard API rates | Holds; available on Pro, Max and Ultra; a monthly spend limit can be set | [*Manage usage credits for paid Claude plans*](https://support.claude.com/en/articles/12429409-manage-usage-credits-for-paid-claude-plans), labelled "Updated yesterday" |
| Five-hour limits were raised at the Opus 5.5 launch | **Not checked.** No search returned Anthropic's launch page | none |

```viz
{
 "kind": "matrix",
 "cols": ["Holds", "Changed", "Not checked"],
 "rows": [
  {"label": "Pro price", "cells": ["●", null, null]},
  {"label": "Max $100, five times Pro", "cells": ["●", null, null]},
  {"label": "$200 tier, twenty times Pro", "tone": 4, "cells": [null, {"mark": "Ultra, 10x weekly", "tone": 4}, null]},
  {"label": "Five-hour and weekly limits", "cells": ["●", null, null]},
  {"label": "Claude Code shares the limit", "cells": ["●", null, null]},
  {"label": "About 45 messages on Pro", "cells": ["●", null, null]},
  {"label": "200K window", "tone": 4, "cells": [null, {"mark": "up to 1M, disputed", "tone": 4}, null]},
  {"label": "What draws usage", "cells": ["●", null, null]},
  {"label": "Project content cached", "cells": ["●", null, null]},
  {"label": "Higher effort, limit sooner", "cells": ["●", null, null]},
  {"label": "No per-model rate published", "cells": ["●", null, null]},
  {"label": "Fable rules", "cells": ["●", null, null]},
  {"label": "Credits at API rates", "cells": ["●", null, null]},
  {"label": "Limits raised at Opus 5.5 launch", "cells": [null, null, "●"]}
 ],
 "legend": [{"mark": "●", "means": "the status of B2 §2's statement when re-read"}],
 "caption": "B2 §2's plan claims re-read on 2 November 2026, from the table in §1 of this unit; sources: <a href=\"https://claude.com/pricing\">Claude, <em>Plans &amp; pricing</em></a> and the Claude Help Center articles on Pro, Max, Ultra, Fable, usage credits, usage limit best practices, effort settings and context windows, all read 2 Nov 2026."
}
```

### The window: two Anthropic pages disagree

B1 §1 built the course on a 200K-token window on claude.ai, a fifth of the API's 1M. On 2 November 2026 Anthropic's pages say two things.

> **Where sources disagree.** *Understanding usage and length limits* still says "Claude's context window size is 200K tokens across all models and paid plans", with 500K on some models for Enterprise; the page shows no date ([article 11647753](https://support.claude.com/en/articles/11647753-understanding-usage-and-length-limits), read 2 Nov 2026). *How large is the context window on paid Claude plans?*, labelled "Updated this week", gives a table for Claude chat in which Fable 5.1, Opus 5.5, Sonnet 5.5 and Haiku 5.5 have 1M tokens, Fable 5 and Opus 4.6 to 4.8 have 500K, and "Outside of these models, Claude's context window size is 200K" ([article 8606394](https://support.claude.com/en/articles/8606394-how-large-is-the-context-window-on-paid-claude-ai-plans), read 2 Nov 2026). The pricing page lists "Up to 1M" and "varies by model" for every plan. Two pages against one, and the more specific page is the recently updated one: this unit takes 1M as the window for the four current models in claude.ai chat, and flags it (unsure list, 1).

Three consequences for the course.

1. **The window no longer forces a new chat.** On 1M, a chat can run five times longer than B1 §1 assumed before it hits the wall. Every turn still re-sends the whole history (B1 §2; Anthropic's context-window page says the input of each turn "Contains all previous conversation history plus the current user message", [Anthropic, *Context windows*](https://platform.claude.com/docs/en/build-with-claude/context-windows), read 2 Nov 2026). A larger window lets that cost grow further before anything stops it.
2. **The binding limit is attention.** The same page, read today: "As token count grows, accuracy and recall degrade, a phenomenon known as *context rot*. This makes curating what's in context just as important as how much space is available." It adds that "Cached prompt prefixes still occupy the context window: prompt caching changes what you pay for those tokens, not whether they count."
3. **B4 F1's inference no longer follows from its arithmetic.** B4 F1 measured the Project knowledge at about 336,000 tokens and concluded, from the retrieval article's rule, that a Project above the 200K window runs in retrieval mode. The retrieval article still ties the switch to the window ("When your project knowledge approaches the context window limit, Claude will automatically enable RAG mode", [Claude Help Center, *RAG for projects*](https://support.claude.com/en/articles/11473015-retrieval-augmented-generation-rag-for-projects), read 2 Nov 2026, labelled "Updated this week") and gives no threshold. Against a 1M window, 336,000 tokens is about a third of it (arithmetic), so whether that Project ran in retrieval mode is undetermined. F1's fix still stands on the other two grounds B4 gave: what every chat must obey should arrive whole, and every loaded token competes for attention.

### B1 §2's caching question

B1 §2 left this to B8: whether, and how, caching reduces what a claude.ai conversation draws from his usage limit. What Anthropic states on 2 November 2026:

- **Project content: yes, by an unpublished amount.** "When you add documents to a project, they're cached", and "Every time you reference that content, cached tokens count less than uncached portions toward your usage limits" (Pro article). "Caches expire after a period of inactivity", and "If you come back to a project after a long break, your first message counts that content in full again" (usage limit best practices). Neither page says how much less a cached token counts, or how long the period of inactivity is.
- **Conversation history in a claude.ai chat: not stated.** The best-practices article lists "Claude remembers context from earlier in the conversation" under the heading "Our system also includes caching that helps you optimize your limits" and gives no rate and no lifetime.
- **Claude Code on a subscription, which draws on the same limit: yes, and documented.** "With prompt caching, Claude Code re-reads that history at the cached token rate, so a one-line question in a session that has been open all day still draws usage for the whole conversation" ([Claude Code docs, *Manage costs effectively*](https://code.claude.com/docs/en/costs), read 2 Nov 2026). Claude Code requests a one-hour cache for the main conversation "only on a Claude subscription within your plan's included usage", and drops it to five minutes once the session draws on usage credits ([Claude Code docs, *How Claude Code uses prompt caching*](https://code.claude.com/docs/en/prompt-caching), read 2 Nov 2026).
- **On the API, for comparison:** cache hits on Opus 5.5 and Sonnet 5.5 cost 0.05 times the base input price, on Fable 5.1 0.025 times, with a five-minute default lifetime and a one-hour option ([Anthropic, *Prompt caching*](https://platform.claude.com/docs/en/build-with-claude/prompt-caching), read 2 Nov 2026). The page does not mention claude.ai or subscription usage.

So the answer is partial: caching reduces the draw for project content and for Claude Code history; the size of the reduction on his plan, and the lifetime of a claude.ai chat's cache, are unpublished.

## 2 · What burns usage for no gain

Anthropic's list of what draws the limit, as read on 2 November 2026: "Message length", "File attachment size", "Current conversation length", "Tool usage (e.g., Research, web search)", "Model choice", "Effort level", "Artifact creation and usage", and "Multi-step tasks, like running code, creating files, or browsing websites" (usage limit best practices). Each of the four habits the brief names spends one of these without buying anything.

**Re-reading large files.** A file read into a chat is part of the history from then on and is re-sent on every later turn (B1 §2; B4 §3 called this the cost of a cold fetch). Reading it a second time adds a second copy. Anthropic's Pro article names the simplest case: "Don't re-upload files within the same conversation." In Claude Code the documented remedy is to read less in the first place: specific requests let Claude "work efficiently with minimal file reads", and a hook that greps a 10,000-line log for errors cuts the context "from tens of thousands of tokens to hundreds" (*Manage costs effectively*). In his setup the vault is the large file. The 17 filed units of this course come to 973,729 characters (his setup, counted by script, 2 Nov 2026), about 360,600 tokens at B1 §2's 2.7 characters per token and about 278,200 at the older 3.5: more than the 200K window B1 assumed, about a third of the 1M window (arithmetic). The mean unit is about 57,300 characters, about 21,200 tokens; the largest, B3, about 30,800. A chat that reads whole units to find one section pays for every other section on every turn after.

**Giant pastes.** Message length is the first item on Anthropic's list, and a paste is re-sent on every turn like a file. Anthropic's own advice cuts the other way for material the task needs: "Provide all relevant data in a single, well-structured message" (best practices, research tasks), and B3 §4 gave the evidence that a brief arriving in pieces does worse than one complete brief. The waste is the paste the task does not need: a whole transcript where the takes for one week would do, a full export where the script needs one column, the same document pasted again in a later turn. The test before pasting is whether the model needs this text to produce this artefact.

**Chats that never end.** B1 §2's illustrative arithmetic: at about 2,000 tokens an exchange, the 30th turn re-sends about 60,000 tokens of history, and 30 turns send about 930,000 tokens of input in all. Claude Code's documentation names the effect in plan terms: "a one-line question in a session that has been open all day still draws usage for the whole conversation" (*Manage costs effectively*). On claude.ai, a chat long enough to trigger automatic context management costs more again: "Longer conversations that trigger automatic context management consume more of your usage limit" (article 11647753). And the cost buys worse answers, by context rot (§1).

**Re-running research.** Research "can use up your limits faster due to Claude retrieving multiple sources" ([Claude Help Center, *Use research on Claude*](https://support.claude.com/en/articles/11088861-use-research-on-claude), read 2 Nov 2026, labelled "Updated yesterday"); Anthropic's engineering team measured its 2025 multi-agent research system at "about 15× more tokens than chats" ([Hadfield et al., *How we built our multi-agent research system*, Anthropic Engineering, 13 Jun 2025](https://www.anthropic.com/engineering/multi-agent-research-system), re-read 2 Nov 2026; vendor, 2025 system). Running the same question again pays that again, and B6 §1 adds the second cost: every run produces fresh claims to check, so a re-run doubles the checking as well as the tokens. The fix is DD-B3's rule 8, "an answer worth keeping becomes a file": a fact found once is filed with its source and date, and the next chat reads the file.

Two more items on Anthropic's list belong here. **Effort above the task's need:** low and medium "work well for routine tasks and stretch your usage further"; higher effort means you "reach your usage limits faster" (effort-settings article). **Tools and connectors left on:** "Tools and connectors are token-intensive", and the help centre's advice is to turn off web search, Research and connectors a chat does not need (article 11647753). B4 F14 already recommended "On demand" for connectors.

## 3 · When a new chat is cheaper

B1 §7 closed with the fix for a buried fact, "trim the window or start a new chat", and handed it to B3, B4, B6 and B8. B4 §4 set out when to start a new chat on grounds of quality and independence. This section adds the cost side.

**The mechanism.** Continuing a chat re-sends its whole history on every turn. A new chat sends its fixed layers (preferences, project instructions, skill descriptions, memory, connectors) plus whatever he hands it. The fixed layers are paid on every turn of every chat either way, so they cancel out of the comparison; what differs is the history. B4 §3 measured the project instructions at about 1,600 tokens and B5 §3 the 19 skill descriptions at about 2,300; the system prompt, memory and preferences were not measured.

**The arithmetic.** On B1 §2's assumption of about 2,000 tokens an exchange, 30 turns in one chat re-send about 930,000 tokens of history. The same 30 turns as three chats of 10, each later chat opening with a handoff note of about 2,000 tokens, send 110,000 + 130,000 + 130,000 = 370,000 (arithmetic; turn k of a chat sends the handoff plus 2,000k). That is 60% less history for the same work, provided the later turns needed only what the handoff note carries.

```viz
{
 "kind": "compare",
 "unit": "k tokens",
 "max": 1000,
 "rows": [
  {"label": "30 turns in one chat", "value": 930, "tone": 1},
  {"label": "Three chats of 10 turns, with a handoff note", "value": 370, "tone": 3}
 ],
 "caption": "History re-sent over 30 turns, in thousands of tokens, on B1 §2's illustrative 2,000 tokens an exchange and a 2,000-token handoff note. §3 of this unit, arithmetic on B1 §2 and <a href=\"https://platform.claude.com/docs/en/build-with-claude/context-windows\">Anthropic, <em>Context windows</em></a> (each turn's input contains all previous history); unmeasured, uncached."
}
```

**What caching changes.** While a cache is warm, re-sent history costs less: on the API, an Opus 5.5 cache hit is 0.05 times the input price (*Prompt caching*); on his plan the discount exists for project content and Claude Code history and its size is unpublished (§1). So inside one working session, a long chat costs less than the uncached arithmetic says. The comparison flips back after a break. The first message after the cache expires "counts that content in full again" (usage limit best practices, for project content), and in Claude Code "your first message after a break longer than the cache lifetime misses the cache and reprocesses your full context" (*Manage costs effectively*). Anthropic's own product draws the conclusion: on Pro or Max, when a large Claude Code session is resumed after a long break, Claude Code "offers to resume from a summary" so that later requests do not carry the full history (*How Claude Code uses prompt caching*). That is a new chat with a handoff note, built into the tool.

**Trimming.** On claude.ai no help article read describes a way to trim a chat by hand; the one trimming mechanism is automatic context management, which summarises earlier messages when code execution is on and "consume[s] more of your usage limit" (article 11647753). In Claude Code there are three documented moves, with different costs (*How Claude Code uses prompt caching*):

- `/rewind` truncates to an earlier turn, a prefix that is already cached, so it is the cheap way to abandon a wrong path.
- `/compact` replaces the history with a summary; the summarising request reads the whole conversation, cheaply while the cache is warm, at full price after a break. Anthropic's advice is to run it "at a natural break in your work, such as between tasks".
- `/clear` starts fresh: "When you want a fresh start instead of continuity, `/clear` costs nothing" (*Manage costs effectively*), and "Stale context wastes tokens on every subsequent message" (same page).

**Model and effort.** In Claude Code, "each model has its own cache" and "each effort level has its own cache for the same model", so switching either mid-session "recomputes the entire request"; the page's tip is to "Pick your model and effort level at the top of a session" (*How Claude Code uses prompt caching*). On claude.ai, Anthropic says he "can change the model, effort level, or thinking setting at any point in a conversation" (effort-settings article) and says nothing about the cache. B2 §7 called the claude.ai effect undocumented; it still is. The Claude Code rule costs nothing to apply on claude.ai too.

**The rule, put together** (my synthesis; each branch traces to a source above): when the next step does not need this chat's history, a new chat (in Claude Code, `/clear`). When it does, and he is coming back after the cache has expired, a new chat with a handoff note, since the next message pays the full history anyway and the note is smaller. When it does and the cache is warm, stay; in Claude Code, `/rewind` off a wrong path and `/compact` only between tasks. The cache lifetime on claude.ai is unpublished; Claude Code's documented one hour on a subscription is the only figure for his plan, and using it for claude.ai is an analogy.

```viz
{
 "kind": "decision",
 "root": {
  "q": "Does the next step need this chat's history?",
  "tone": 4,
  "branches": [
   {"label": "no", "to": {"outcome": "New chat (Claude Code: /clear)", "tone": 2}},
   {"label": "yes", "to": {
    "q": "Back after the cache expired?",
    "tone": 4,
    "branches": [
     {"label": "yes", "to": {"outcome": "New chat with a handoff note", "tone": 2}},
     {"label": "no", "to": {
      "q": "Abandoning a wrong path?",
      "tone": 4,
      "branches": [
       {"label": "yes", "to": {"outcome": "Claude Code: /rewind. claude.ai: new chat", "tone": 2}},
       {"label": "no", "to": {"outcome": "Stay; /compact only between tasks", "tone": 3}}
      ]
     }}
    ]
   }}
  ]
 },
 "caption": "Continue, trim or start again, the rule in §3 of this unit, synthesised from <a href=\"https://code.claude.com/docs/en/prompt-caching\">Claude Code docs, <em>How Claude Code uses prompt caching</em></a>, <a href=\"https://code.claude.com/docs/en/costs\"><em>Manage costs effectively</em></a> and <a href=\"https://support.claude.com/en/articles/9797557-usage-limit-best-practices\">Claude Help Center, <em>Usage limit best practices</em></a>, read 2 Nov 2026; B4 §4 gives the quality reasons for a new chat."
}
```

This rule refines B4 §4's third "stay" condition ("Work has paused briefly"): a brief pause is one inside the cache lifetime.

## 4 · Token budgets per task type

A budget here is the most text a task may put into its window, and where its chat stops. Anthropic publishes no token allowance per window (§1), so each budget is set as a ceiling on what enters the chat, from sizes that are documented or measured.

**B6 Deliverable A, re-checked.** B6's routing table priced its three routes from B2's figures of 28 October. On 2 November 2026: Opus 5.5 is still $4 input and $20 output per million tokens ([Anthropic, *Pricing*](https://platform.claude.com/docs/about-claude/pricing), read 2 Nov 2026), so B2 §5's $0.046 for an assumed 4,000 tokens in and 1,500 out still holds; web search is still "$10 USD per 1,000 searches" plus the result tokens (same page); the 4× and 15× ratios are as B6 quoted them (Hadfield et al., re-read today); and Research still "can use up your limits faster" (*Use research on Claude*). The budgets below agree with B6 Deliverable A and add nothing to its cost column.

| Task type | Route (B6 A) | Where it runs | What may enter the window | Size basis | Stop line |
|---|---|---|---|---|---|
| Short output from material in hand: caption, Shōmen post, routine message, calendar event, reformatting | Ask directly | Light chat outside the Project (B2, rules for using the table) | The brief and the material for this one piece | B2 §5 assumes about 4,000 tokens in and 1,500 out: $0.046 on Opus 5.5, $0.023 on Sonnet 5.5 at API prices (arithmetic, 2 Nov 2026 prices) | One artefact; after two failed corrections, a rewritten brief in a new chat (DD-B3 rule 6) |
| Journal entry | Ask directly | A session on the journey repository (B5 §5) | That week's takes and the template | Unmeasured | One entry |
| One current fact | Search | Any chat | One search and the page it returns | $10 per 1,000 searches plus result tokens on the API; an agent with tools about 4× a chat's tokens (vendor, 2025) | The fact filed with source and date; never searched twice |
| Landscape question | Deep research | Its own chat | The research brief (B3 template 7) | About 15× a chat's tokens (vendor, 2025 system) | One run per question; the report filed and sampled (B6 C) |
| Course unit | Writing chat | Fresh chat or agent, repository cloned | The brief, the method files, and the sections of earlier units the brief points to, found by search | A filed unit averages about 21,200 tokens, so reading one whole costs about that; all 17 together about 360,600 (his setup, 2.7 characters per token) | The unit and its deliverable; filing in another chat |
| Audit of four units | Fresh chat | Fable 5.1, a chat that saw no writing | The four units and the sources it opens | About 84,900 tokens for four average units (arithmetic); on Pro, Fable runs on credits at $10 per million input tokens, about $0.85 per uncached pass over them (arithmetic; whether credit billing on claude.ai applies cache rates is unpublished) | The audit report |
| Code and scripts | Claude Code | A session on the repository | `CLAUDE.md` under 200 lines; files read as needed | Anthropic: "Aim to keep CLAUDE.md under 200 lines" (*Manage costs effectively*) | `/clear` between unrelated tasks |

Two readings. First, the heaviest single item in his routine is reading whole units: a writing chat that reads five earlier units in full has taken in about 106,000 tokens before writing (arithmetic on the mean), more than the four-unit audit. Second, the cheapest saving is in the light chats, which carry the fixed layers of whatever context they are opened in; B2's rule to run small tasks outside the Learning Project removes the project instructions and knowledge from every one of them.

## 5 · Privacy and retention: memory, projects, and what lives only in the vault

B4 F15 found private terms in the public build and left the general rules to B8. This section sets them as categories and rules, from what Anthropic says it does with each kind of stored material. No inventory of what he has stored is made here.

### What Anthropic keeps, and for how long (as of 2 November 2026)

**Chats.** The privacy centre's retention page covers Free, Pro, Max and Claude Code on those accounts and is dated 1 July 2026 ([Anthropic Privacy Center, *How long do you store my data?*](https://privacy.claude.com/en/articles/10023548-how-long-do-you-store-my-data), read 2 Nov 2026). It gives no fixed period for chats he keeps; personal data is retained "for as long as reasonably necessary". A deleted chat leaves his history at once and back-end storage within 30 days. With the model-improvement setting on, new or resumed chats may be kept de-identified for up to five years in training pipelines; with it off, they are not used for future training, though data already in a training run in progress stays there. A chat flagged for a usage-policy violation keeps its inputs and outputs for up to two years and its classification scores for up to seven. Feedback (a thumbs-up or thumbs-down, or a bug report) keeps the associated data for five years. The August 2025 terms change set the same two branches: five years with training allowed, the existing 30-day retention without it, for new or resumed chats only; it does not apply to Claude for Work, Government, Education or the API ([Anthropic, *Updates to our consumer terms*, 28 Aug 2025](https://www.anthropic.com/news/updates-to-our-consumer-terms), re-read 2 Nov 2026). The setting is a toggle under Settings > Privacy ([Anthropic Privacy Center, *How do I change my model improvement privacy settings?*](https://privacy.claude.com/en/articles/12109829-how-do-i-change-my-model-improvement-privacy-settings), dated 3 Aug 2026).

**Who can read them.** Review happens only when he allows chats to improve Claude; "Access is limited to a small number of personnel involved in model training", and data is de-linked from his user ID before review; chats flagged by safety classifiers "may still be used to improve our internal trust and safety models". The same article advises caution with bank and card numbers, medical records, passwords or login credentials, and confidential business or personal documents ([Claude Help Center, *I would like to input sensitive data into my chats with Claude*](https://support.claude.com/en/articles/8325621-i-would-like-to-input-sensitive-data-into-my-chats-with-claude-who-can-view-my-conversations), read 2 Nov 2026, labelled "Updated this week").

**Memory.** "Claude saves memory as a set of individual topics as you chat." Each project has its own memory; in a project, Claude uses that project's memory and his memory from chats outside projects, never another project's; turning off "Use account memory" on the project's page separates them fully. By default memory does not store sensitive topics such as health, politics or religion, unless he opts in; "Some information is never saved to memory, even if you ask": government ID numbers, criminal history, financial account numbers and immigration status. Deleting a chat does not remove the memory entries written from it; they are deleted one by one under Settings > Your Claude, "Manage" next to "Your memory". The article does not say how much memory enters a chat ([Claude Help Center, *Use Claude's chat search and memory to build on previous context*](https://support.claude.com/en/articles/11817273-use-claude-s-chat-search-and-memory-to-build-on-previous-context), read 2 Nov 2026, labelled "Updated this week"). The retention page says nothing about memory, projects or uploaded files.

**Projects.** "Context is not shared across chats within a project unless the information is added into the project knowledge base"; the article describes sharing for Team and Enterprise and says nothing about retention or training for project files ([Claude Help Center, *How can I create and manage projects?*](https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects), read 2 Nov 2026).

**Incognito.** Incognito chats "aren't saved to your chat history or to Claude's memory", are kept 30 days by default, are not used for training, are available only outside projects, and cannot be reopened once closed ([Claude Help Center, *Use incognito chats*](https://support.claude.com/en/articles/12260368), read 2 Nov 2026, labelled "Updated this week").

### What follows for each kind of material

Four places can hold what he works with: memory, a Project, the private vault (a private repository, B5 §5), and the public build (B4 F15). Five properties decide which: memory is written by a model and re-inserted in amounts nobody publishes (B1 §7; the memory article above); a Project's output, in the Learning Project's case, is published (B4 F13); a chat's text sits on Anthropic's servers under the retention rules above; a commit to a repository is hard to take back, since GitHub's documentation says removed data may survive in clones, forks and cached views (B4 F15 cites [GitHub Docs](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository), not re-checked here); and the public build renders whatever the data files hold (B4 F15).

| Material | Memory | Project | Private vault | Public build | Basis |
|---|---|---|---|---|---|
| Facts the brief already makes public (his role in the brief's words, ADHD, the journeys, the brand) | Yes | Yes | Yes | Yes | Already public by his choice (brief; A4) |
| Rules and method | No | Yes | Yes, canonical | Only what the method publishes | B4 §1: rules do not belong in memory; DD-B3 rule 8 |
| Raw takes, drafts not yet cleared | No | No | Yes | No | B5 §5 (journey text in a private repository); B7 step 9 (the final pass is his) |
| Health numbers (weight, biometrics) | No | No | Yes | Change only, from the publish list | Memory excludes health by default; A8 R15 (publish change only); A4 publish list |
| Other people's personal data, consent records | No | No | Yes | Only with written consent | A8 R19 to R22 |
| Employer material | No | No | No | No | The sensitive-data article's caution on confidential business documents; the consumer terms cover Free, Pro and Max (my rule) |
| Passwords, keys, card, bank and ID numbers | No | No | No | No | Sensitive-data article; memory never stores ID or account numbers; git history persists (B4 F15) |

```viz
{
 "kind": "matrix",
 "cols": ["Memory", "Project", "Private vault", "Public build"],
 "rows": [
  {"label": "Facts the brief makes public", "cells": [{"mark": "yes", "tone": 3}, {"mark": "yes", "tone": 3}, {"mark": "yes", "tone": 3}, {"mark": "yes", "tone": 3}]},
  {"label": "Rules and method", "cells": [{"mark": "no", "tone": 1}, {"mark": "yes", "tone": 3}, {"mark": "canonical", "tone": 3}, "as published"]},
  {"label": "Raw takes, uncleared drafts", "cells": [{"mark": "no", "tone": 1}, {"mark": "no", "tone": 1}, {"mark": "yes", "tone": 3}, {"mark": "no", "tone": 1}]},
  {"label": "Health numbers", "cells": [{"mark": "no", "tone": 1}, {"mark": "no", "tone": 1}, {"mark": "yes", "tone": 3}, "change only"]},
  {"label": "Other people's data, consents", "cells": [{"mark": "no", "tone": 1}, {"mark": "no", "tone": 1}, {"mark": "yes", "tone": 3}, "with consent"]},
  {"label": "Employer material", "cells": [{"mark": "no", "tone": 1}, {"mark": "no", "tone": 1}, {"mark": "no", "tone": 1}, {"mark": "no", "tone": 1}]},
  {"label": "Passwords, keys, card and ID numbers", "cells": [{"mark": "no", "tone": 1}, {"mark": "no", "tone": 1}, {"mark": "no", "tone": 1}, {"mark": "no", "tone": 1}]}
 ],
 "caption": "Where each kind of material may live, the table in §5 of this unit, from <a href=\"https://support.claude.com/en/articles/11817273-use-claude-s-chat-search-and-memory-to-build-on-previous-context\">Claude Help Center, memory</a>, <a href=\"https://support.claude.com/en/articles/8325621-i-would-like-to-input-sensitive-data-into-my-chats-with-claude-who-can-view-my-conversations\">the sensitive-data article</a> (both read 2 Nov 2026), A4's publish list, A8 R15 and R19 to R22, B4 F13 and F15, and B5 §5."
}
```

Three notes on the table. **Memory gets only what is already public** because nobody can see in advance which chat it will reach, and inside the Learning Project the chats it reaches write published units (B4 F13, whose fix, turning off "Use account memory" for that Project, the memory article confirms still exists). **Health stays out of memory** by Anthropic's default; opting in under "Include sensitive topics in memory" would send health facts into every chat memory reaches. **Employer material goes nowhere in this account**: the consumer terms govern Free, Pro and Max, and Anthropic's commercial products are under separate terms (consumer-terms post); work for his employer belongs under whatever terms that employer has set, outside this course. That line is my rule; the sources give the two sets of terms and the caution, and he decides.

**Deleting is three steps, and the second is easy to miss.** Delete the chat (gone from history at once, from back-end storage within 30 days); delete any memory entries it wrote, since the chat's deletion leaves them; and, where model improvement was on when the chat ran, accept that a de-identified copy may already be in a training run (retention page; model-improvement article). For a one-off question involving private material outside any Project, an incognito chat avoids the first two steps.

## Deliverable · Usage rules 11 to 24, for the way-of-working file

Paste after DD-B3's ten operating rules. Each rule names its source; where it refines a DD-B3 rule, it says which. Product facts as of 2 November 2026; re-read the sources at the staleness check.

> **Usage, limits and privacy (from B8, 2 Nov 2026)**
>
> 11. **Model and effort are set before the first message and never changed inside a chat.** To change either, I start a new chat. In Claude Code each model and each effort level has its own cache, and a switch recomputes the whole request; on claude.ai the effect is undocumented, and the rule costs nothing. *(Refines DD-B3 rule 10 and B2's rules for the routing table. [Claude Code docs, How Claude Code uses prompt caching](https://code.claude.com/docs/en/prompt-caching).)*
> 12. **One task per chat; a new task gets a new chat** (in Claude Code, `/clear`). Stale context is paid on every later message. *(Refines DD-B3 rule 6. [Claude Code docs, Manage costs effectively](https://code.claude.com/docs/en/costs); B4 §4.)*
> 13. **Back to a long chat after a break, I start a new chat with a handoff note.** The first message after the cache expires pays for the whole history again; a note costs only itself. Claude Code's cache lasts one hour on a subscription; claude.ai publishes no lifetime, so I treat a break over an hour the same way (analogy). A short pause inside the hour: I stay. *([Claude Help Center, Usage limit best practices](https://support.claude.com/en/articles/9797557-usage-limit-best-practices); Claude Code docs, Manage costs effectively and How Claude Code uses prompt caching; B8 §3.)*
> 14. **A handoff note carries decisions, open items and file paths, never the transcript, and lives in the vault.** *(DD-B3 rule 8; B4 §4, Anthropic's structured note-taking.)*
> 15. **In Claude Code: `/rewind` to abandon a wrong path, `/compact` only between tasks, `/clear` for a fresh start.** Rewind returns to a cached prefix; compacting reads the whole conversation; clearing costs nothing. *(Claude Code docs, How Claude Code uses prompt caching and Manage costs effectively.)*
> 16. **I never paste what a chat can read by path, and never re-upload a file in the same chat.** A paste or a file is re-sent on every later turn. What the task needs, I give once, whole, in the first message. *([Claude Help Center, About Claude's Pro plan usage](https://support.claude.com/en/articles/8324991-about-claude-s-pro-plan-usage); Usage limit best practices; B3 §4.)*
> 17. **I read sections, never the whole vault.** A chat finds the section a brief points to by search and reads that. The 17 filed units are about 360,000 tokens; one averages about 21,000. *(B8 §2 and §4, counted 2 Nov 2026; Claude Code docs, Manage costs effectively, on minimal file reads.)*
> 18. **A fact is searched once.** Found, it is filed with its source and date, and the next chat reads the file. Deep research runs once per question, by B6's routing; it costs about fifteen chats of tokens (Anthropic's 2025 figure) and every run brings new claims to check. *(Refines DD-B3 rule 8. B6 Deliverable A; [Claude Help Center, Use research on Claude](https://support.claude.com/en/articles/11088861-use-research-on-claude); [Hadfield et al., Anthropic Engineering, 13 Jun 2025](https://www.anthropic.com/engineering/multi-agent-research-system).)*
> 19. **Tools and connectors stay off unless the chat uses them**; connectors load on demand. *(Supports DD-B3 rule 9. [Claude Help Center, Understanding usage and length limits](https://support.claude.com/en/articles/11647753-understanding-usage-and-length-limits); B4 F14.)*
> 20. **Token budgets by task type.** What may enter the window, and where the chat stops. *(B8 §4; agrees with B6 Deliverable A, re-checked 2 Nov 2026 against [Anthropic, Pricing](https://platform.claude.com/docs/about-claude/pricing).)*
>
> | Task | Window holds | Size | Stops at |
> |---|---|---|---|
> | Caption, post, routine message, calendar, reformatting | Brief and material for one piece, in a light chat outside the Project | About 4,000 in, 1,500 out (B2 §5 assumption): $0.046 Opus 5.5, $0.023 Sonnet 5.5 at API prices | One artefact |
> | Journal entry | One week's takes and the template | Unmeasured | One entry |
> | One current fact | One search and its page | $10 per 1,000 searches plus result tokens (API) | The fact filed |
> | Landscape question | The research brief | About 15× a chat's tokens (vendor, 2025) | One report, sampled |
> | Course unit | Brief, method files, the sections the brief points to | A whole unit about 21,000 tokens; all 17 about 360,000 | Unit and deliverable |
> | Audit of four units | The four units and the sources opened | About 85,000 tokens; on Pro, Fable credits about $0.85 per uncached pass | The report |
> | Code | `CLAUDE.md` under 200 lines, files as needed | Anthropic's 200-line guidance | `/clear` between tasks |
>
> 21. **Before a unit or an audit I check Settings > Usage, and usage credits carry a monthly spend limit.** No page publishes how many tokens a window holds, so the bars are the only gauge; credits are billed at API rates and the limit is set under "Adjust limit". *(Usage limit best practices; [Claude Help Center, Manage usage credits for paid Claude plans](https://support.claude.com/en/articles/12429409-manage-usage-credits-for-paid-claude-plans).)*
> 22. **Memory holds only what is already public; health, other people's data and drafts live in the private vault; employer material, passwords, keys and card, bank and ID numbers go nowhere in this account.** "Include sensitive topics in memory" stays off; "Use account memory" stays off in the Learning Project, whose output is published. *(Refines DD-B3 rule 8. [Claude Help Center, chat search and memory](https://support.claude.com/en/articles/11817273-use-claude-s-chat-search-and-memory-to-build-on-previous-context); [the sensitive-data article](https://support.claude.com/en/articles/8325621-i-would-like-to-input-sensitive-data-into-my-chats-with-claude-who-can-view-my-conversations); A8 R15, R19 to R22; B4 F13, F15; the employer line is my rule.)*
> 23. **Deleting a chat is three steps:** delete the chat (back-end within 30 days), delete the memory entries it wrote (the chat's deletion leaves them), and know that with model improvement on, a de-identified copy may already be in training for up to five years. Feedback buttons keep a chat's data five years, so I do not rate chats that hold private material. A one-off private question outside a Project goes in an incognito chat (not in history or memory, kept 30 days, never trained on). *([Anthropic Privacy Center, How long do you store my data?](https://privacy.claude.com/en/articles/10023548-how-long-do-you-store-my-data), 1 Jul 2026; chat search and memory; [Use incognito chats](https://support.claude.com/en/articles/12260368).)*
> 24. **The model-improvement setting is a decision, made once and written down:** on means new and resumed chats may be kept de-identified up to five years for training; off means they are not used for future training. *([Anthropic Privacy Center, model improvement settings](https://privacy.claude.com/en/articles/12109829-how-do-i-change-my-model-improvement-privacy-settings), 3 Aug 2026; [Anthropic, Updates to our consumer terms, 28 Aug 2025](https://www.anthropic.com/news/updates-to-our-consumer-terms).)*

## Sources

All web sources read on 2 November 2026 unless a date of their own is given.

- Claude. *Plans & pricing*. https://claude.com/pricing
- Claude Help Center. *About Claude's Pro plan usage* (article 8324991), labelled "Updated over a week ago". https://support.claude.com/en/articles/8324991-about-claude-s-pro-plan-usage
- Claude Help Center. *About Claude's Max plan usage* (article 11014257), labelled "Updated this week". https://support.claude.com/en/articles/11014257-about-claude-s-max-plan-usage
- Claude Help Center. *What is the Ultra plan?* (article 17728952), labelled "Updated this week". https://support.claude.com/en/articles/17728952
- Claude Help Center. *Claude Fable models on your plan* (article 15424964), labelled "Updated today". https://support.claude.com/en/articles/15424964-claude-fable-models-on-your-plan
- Claude Help Center. *Manage usage credits for paid Claude plans* (article 12429409), labelled "Updated yesterday". https://support.claude.com/en/articles/12429409-manage-usage-credits-for-paid-claude-plans
- Claude Help Center. *Usage limit best practices* (article 9797557), labelled "Updated this week". https://support.claude.com/en/articles/9797557-usage-limit-best-practices
- Claude Help Center. *Understanding usage and length limits* (article 11647753), no date shown. https://support.claude.com/en/articles/11647753-understanding-usage-and-length-limits
- Claude Help Center. *How large is the context window on paid Claude plans?* (article 8606394), labelled "Updated this week". https://support.claude.com/en/articles/8606394-how-large-is-the-context-window-on-paid-claude-ai-plans
- Claude Help Center. *Retrieval augmented generation (RAG) for projects* (article 11473015), labelled "Updated this week". https://support.claude.com/en/articles/11473015-retrieval-augmented-generation-rag-for-projects
- Claude Help Center. *Change the model, effort and extended thinking settings* (article 8664678), labelled "Updated over 3 weeks ago". https://support.claude.com/en/articles/8664678-change-the-model-effort-and-extended-thinking-settings
- Claude Help Center. *Use research on Claude* (article 11088861), labelled "Updated yesterday". https://support.claude.com/en/articles/11088861-use-research-on-claude
- Claude Help Center. *Use Claude's chat search and memory to build on previous context* (article 11817273), labelled "Updated this week". https://support.claude.com/en/articles/11817273-use-claude-s-chat-search-and-memory-to-build-on-previous-context
- Claude Help Center. *Use incognito chats* (article 12260368), labelled "Updated this week". https://support.claude.com/en/articles/12260368
- Claude Help Center. *How can I create and manage projects?* (article 9519177), labelled "Updated this week". https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects
- Claude Help Center. *I would like to input sensitive data into my chats with Claude. Who can view my conversations?* (article 8325621), labelled "Updated this week". https://support.claude.com/en/articles/8325621-i-would-like-to-input-sensitive-data-into-my-chats-with-claude-who-can-view-my-conversations
- Anthropic Privacy Center. *How long do you store my data?* 1 July 2026. https://privacy.claude.com/en/articles/10023548-how-long-do-you-store-my-data
- Anthropic Privacy Center. *How do I change my model improvement privacy settings?* 3 August 2026. https://privacy.claude.com/en/articles/12109829-how-do-i-change-my-model-improvement-privacy-settings
- Anthropic. *Updates to our consumer terms*. 28 August 2025. https://www.anthropic.com/news/updates-to-our-consumer-terms
- Anthropic. *Pricing*. Claude Platform docs. https://platform.claude.com/docs/about-claude/pricing
- Anthropic. *Prompt caching*. Claude Platform docs. https://platform.claude.com/docs/en/build-with-claude/prompt-caching
- Anthropic. *Context windows*. Claude Platform docs. https://platform.claude.com/docs/en/build-with-claude/context-windows
- Claude Code docs. *Manage costs effectively*. https://code.claude.com/docs/en/costs
- Claude Code docs. *How Claude Code uses prompt caching*. https://code.claude.com/docs/en/prompt-caching
- Hadfield, J., Zhang, B., Lien, K., Scholz, F., Fox, J. and Ford, D. *How we built our multi-agent research system*. Anthropic Engineering, 13 June 2025 (vendor). https://www.anthropic.com/engineering/multi-agent-research-system
- FourWeekMBA. *Claude Ultra Drops 5-Hour Limit for Verified Users at $200*. 30 October 2026 (secondary report, used only for the date of the change). https://fourweekmba.com/ai-claude-ultra-drops-5-hour-limit-for-verified-users-at-200/
- GitHub Docs. *Removing sensitive data from a repository*, as cited by B4 F15; not re-checked here. https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository
- Filed units cited by section: A4 · Voice, disclosure and the record (Deliverable, publish list); A8 · Legal, tax, time (R15, R19 to R22); B1 · Mental model (§1, §2, §4, §7); B2 · Choosing the model (§2, §5, §7; rules for using the table); B3 · Prompting that holds up (§4; template 7); B4 · Context engineering (§1, §3, §4; F1, F13, F14, F15); B5 · Skills and automation (§3, §5); B6 · Research and verification (§1; Deliverable A and C); B7 · Content pipeline (step 9); DD-B3 · Deep dive (Deliverable B, operating rules 6, 8, 9, 10). Unit sizes counted by script from `courses/brand-ai/*.md` on 2 November 2026.

## Writer's unsure list

1. **The claude.ai window.** Article 8606394 (updated this week) and the pricing page give up to 1M for the current models; article 11647753 (undated) still says 200K across all models and paid plans. The unit takes 1M; which page Anthropic will correct is unknown.
2. **The date of the Ultra change (30 October 2026)** comes from FourWeekMBA, a secondary source citing an X post that was not opened. Two other reports returned by search (Windows Report, Crypto Briefing) failed to load: not checked.
3. **"Five-hour limits raised at the Opus 5.5 launch"** (B2 §2) was not checked: no search returned Anthropic's launch page.
4. **The Max article and the pricing page disagree** on the $200 tier (20x per session and at least 900 messages, against Ultra at 10x weekly). The Ultra article and the Fable article also differ on whether Fable has a separate weekly limit on Ultra or shares the regular pool.
5. **How much a cached token counts against a plan limit, and how long a claude.ai chat's cache lasts,** are unpublished. Rule 13's one hour is Claude Code's documented subscription figure, applied to claude.ai by analogy.
6. **Two privacy-centre pages failed to load:** *Can you delete data sent via Claude.ai?* and the page on inputting third parties' personal data. Not checked. Deletion facts come from the retention page only.
7. **Retention of memory, project files and uploads** is not stated on the retention page or the projects article; the unit says so and draws no period for them.
8. **Token sizes rest on B1 §2's 2.7 characters per token,** which is arithmetic on Anthropic's glossary and unmeasured; the per-post figures rest on B2 §5's assumed 4,000 in and 1,500 out.
9. **The 930,000 against 370,000 comparison** is uncached illustrative arithmetic; with a warm cache the gap in cost is smaller by an unpublished amount on his plan.
10. **Whether usage-credit billing on claude.ai applies cache rates** is unpublished; the $0.85 per uncached pass for a four-unit Fable audit is list-price arithmetic.
