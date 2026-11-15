---
code: BW1
title: Mental model
course: building-with-ai
model: Opus 5.5
written: 2026-11-15
search: on
---

# BW1 · Mental model

Every product fact in this unit (a window size, a price, a cutoff, how memory, projects or skills behave) was read on the vendor's own page on 15 November 2026, and is dated where it appears. Anthropic's help-centre pages carry no exact date, only a note of how recently they were updated, so the reading date is the only date they can be given. Research findings name the models they tested; carrying a finding to a current model is this unit's inference, and is said to be. Each practice carries an evidence grade: **measured** (a study or a test with numbers), **documented practice** (a vendor or a named practitioner says to do it; nobody measured it here), or **stated opinion**.

## 1 · The context window is the one thing you control

Anthropic defines the context window as all the text a language model can reference when generating a response, the response itself included ([Anthropic, *Context windows*](https://platform.claude.com/docs/en/build-with-claude/context-windows), read 15 Nov 2026). Its glossary separates that window from the corpus the model was trained on and calls the window the model's working memory ([Anthropic, *Glossary*](https://platform.claude.com/docs/en/about-claude/glossary.md), read 15 Nov 2026). Everything in a request counts against it: the system prompt, every message (tool results, images and documents included), the tool definitions, and the output the model writes for the turn, its thinking included ([*Context windows*](https://platform.claude.com/docs/en/build-with-claude/context-windows)).

That is the whole interface. The model's trained weights are fixed by the time you use it. What changes from one answer to the next is the text in the window, and most of that text is chosen by you: what you type, paste and attach, the standing instructions you save, the files you put in a project, the tools and connectors you switch on, the skills you install, whether memory is on, and when you start a new chat. The rest is written by the vendor (the product's system prompt) or by the model itself: its earlier replies, and the search and file results it fetches. When an output fails, the first question is what was in the window when it was written.

The tree below sorts what reaches the window by who writes it.

```viz
{
  "kind": "tree",
  "caption": "What reaches the context window, grouped by who writes it, from §1 of this unit, on Anthropic, <em>Context windows</em> (platform.claude.com, read 15 Nov 2026); the grouping by who writes each part is this unit's.",
  "root": {
    "label": "Context window",
    "tone": 1,
    "children": [
      {"label": "The vendor", "tone": 2, "children": [{"label": "System prompt"}]},
      {"label": "You", "tone": 3, "children": [
        {"label": "Standing instructions"},
        {"label": "Project files"},
        {"label": "What you type, paste, attach"},
        {"label": "Tools, skills, memory switched on"}
      ]},
      {"label": "The model, as it works", "tone": 4, "children": [
        {"label": "Its earlier replies"},
        {"label": "Search and file results"}
      ]}
    ]
  }
}
```

**How big the window is (read 15 Nov 2026).** On Anthropic's API, Opus 5.5, Sonnet 5.5, Haiku 5.5 and Fable 5.2 each have a 1M-token window and can write up to 128K output tokens in one request ([Anthropic, *Models overview*](https://platform.claude.com/docs/en/models/overview); [*Context windows*](https://platform.claude.com/docs/en/build-with-claude/context-windows)). In the claude.ai chat on a paid plan, the help centre lists 1M tokens for Opus 5.5, Sonnet 5.5, Haiku 5.5 and Fable 5.2, 500K for some older models such as Opus 4.8 and Sonnet 4.6, and 200K for any model not in its table ([Claude Help Center, *How large is the context window on paid Claude plans?*](https://support.claude.com/en/articles/8606394-how-large-is-the-context-window-on-paid-claude-plans)). Part of the window is held back for the reply, so the longest conversation is slightly shorter than the full window ([Claude Help Center, *How do usage and length limits work?*](https://support.claude.com/en/articles/11647753-understanding-usage-and-length-limits)). These numbers change; check them on the vendor's page on the day you rely on them.

A big window is a ceiling. It says how much text can be placed in front of the model, and nothing about how well the model will use it (§2).

**The case.** Academy (Academy case), a library of self-study courses built by one person with Claude in October and November 2026, is the running example of this course. It is one project by one person: an anecdote, never evidence about AI tools in general. Its method writes each unit in a new chat or a fresh agent context that sees only its brief and the units already filed, and the stated reason is that leaked context is how a course starts repeating itself (Academy case file §2). That rule is a decision about the window: it fixes what the writer can see. Whether it works better than the alternative is untested, because the record holds no unit written without the method (Academy case file §9). Grade: documented practice, in one project.

## 2 · Tokens: what you pay with and what the model attends with

### What a token is

A token is the smallest unit a language model works in; it can be a word, part of a word, a character or a byte. For Claude, how many characters make a token depends on the model and the language. Claude 4.7 and later models use a tokenizer that produces about 30 percent more tokens for the same text than earlier models, on which a token is about 3.5 English characters ([*Glossary*](https://platform.claude.com/docs/en/about-claude/glossary.md), read 15 Nov 2026). Anthropic's model page gives the current tokenizer's own conversion: 1M tokens is roughly 555k words or 2.5M Unicode characters, about 2.5 characters a token ([*Models overview*](https://platform.claude.com/docs/en/models/overview), read 15 Nov 2026; the per-token division is this unit's arithmetic). The glossary gives no figure for other languages, and points to Anthropic's token-counting endpoint for exact counts (same page).

### Tokens as cost

The model keeps nothing between turns. Anthropic's API documentation says the Messages API is stateless, so the full conversational history is sent with every request ([Anthropic, *Using the Messages API*](https://platform.claude.com/docs/en/build-with-claude/working-with-messages.md), read 15 Nov 2026). The context-window page says the same turn by turn: each turn's input holds all previous history plus the new message, and previous turns are preserved completely ([*Context windows*](https://platform.claude.com/docs/en/build-with-claude/context-windows)). The same API page now describes a beta feature, message threads, in which the API keeps the conversation so that a later request sends only the new messages; a thread expires five minutes after its last request ([*Using the Messages API*](https://platform.claude.com/docs/en/build-with-claude/working-with-messages.md)). That changes what a developer sends over the wire. It does not say the model reads less: on the context-window page, each turn's input still contains the whole history.

The consequence is that cost grows faster than the conversation. Illustrative arithmetic, unmeasured: if every exchange adds about 2,000 tokens, the first turn sends about 2,000, turn 10 sends about 20,000 tokens of history, turn 20 about 40,000 and turn 30 about 60,000. Added up, the first 10 turns send about 110,000 tokens of input, the first 20 about 420,000, and the first 30 about 2,000 × (1 + 2 + … + 30) = 930,000, before any standing layer (system prompt, instructions, memory, skill descriptions) is counted again on every turn.

```viz
{
  "kind": "line",
  "caption": "Illustrative only: total input tokens sent over a chat in which each exchange adds about 2,000 tokens, from the arithmetic in §2 of this unit (unmeasured), on the turn-by-turn mechanism in Anthropic, <em>Context windows</em> (read 15 Nov 2026).",
  "x": [1, 10, 20, 30],
  "unit": "k",
  "xlabel": "Turn",
  "ylabel": "Total input sent (tokens)",
  "series": [{"name": "Total input sent", "values": [2, 110, 420, 930], "tone": 3}]
}
```

On claude.ai you see a usage limit in place of a price. Anthropic says usage depends on the length and complexity of your conversations and on the model, features and effort level you choose; that claude.ai, Claude Code and Claude Desktop count toward the same limit; and that tools and connectors are token-intensive ([*How do usage and length limits work?*](https://support.claude.com/en/articles/11647753-understanding-usage-and-length-limits), read 15 Nov 2026). On the API, the price per million tokens (read 15 Nov 2026) is $4 input and $20 output for Opus 5.5, $2 and $10 for Sonnet 5.5, from $0.10 and $0.50 for Haiku 5.5, and $8 and $40 for Fable 5.2 ([*Models overview*](https://platform.claude.com/docs/en/models/overview)). Output costs five times input on every row.

OpenAI documents the same mechanism for its own API: each request is independent and stateless, and when responses are chained, all previous input tokens are billed again as input ([OpenAI, *Conversation state*](https://developers.openai.com/api/docs/guides/conversation-state), read 15 Nov 2026). The principle holds across vendors; the prices do not.

### Tokens as attention

Anthropic's Applied AI team (Prithvi Rajasekaran, Ethan Dixon, Carly Ryan and Jeremy Hadfield) explain why more text is not free even when it fits: a transformer relates every token to every other, which gives n² pairwise relationships for n tokens, so a model has an attention budget that each new token draws down, and context is "a finite resource with diminishing marginal returns" ([Rajasekaran et al., *Effective context engineering for AI agents*, Anthropic, 29 Sep 2025](https://anthropic.com/engineering/effective-context-engineering-for-ai-agents)). Anthropic's documentation names the effect: "As token count grows, accuracy and recall degrade, a phenomenon known as *context rot*" ([*Context windows*](https://platform.claude.com/docs/en/build-with-claude/context-windows), read 15 Nov 2026).

Three kinds of evidence stand behind this, and they measure different things.

- **Peer-reviewed (measured).** Liu and colleagues found that performance was often highest when the relevant information sat at the beginning or end of a long input, and degraded significantly when it sat in the middle, even for models built for long contexts ([Liu et al., "Lost in the Middle: How Language Models Use Long Contexts", *TACL* 12, 2024, 157–173](https://aclanthology.org/2024.tacl-1.9/)). The tasks were multi-document question answering and key-value retrieval. The models were MPT-30B-Instruct, LongChat-13B (16K), GPT-3.5-Turbo, GPT-3.5-Turbo (16K), Claude-1.3 and Claude-1.3 (100K), with Flan-T5-XXL, Flan-UL2, Llama-2 and GPT-4 (8K) in further experiments.
- **Vendor research (measured, by an interested party).** Chroma tested 18 models, among them Claude Opus 4, Sonnet 4, Sonnet 3.7, Sonnet 3.5 and Haiku 3.5, and found performance growing less reliable as input length grew; models did not use their context uniformly, and distractors (passages similar to the answer) lowered accuracy further ([Hong, Troynikov and Huber, *Context Rot: How Increasing Input Tokens Impacts LLM Performance*, Chroma, 14 Jul 2025](https://trychroma.com/research/context-rot)). Chroma sells a retrieval database, a product whose case this finding supports; label it vendor data.
- **Vendor statements (documented, no figure).** Anthropic states context rot as a property of its models without a number ([*Context windows*](https://platform.claude.com/docs/en/build-with-claude/context-windows)). Google's Gemini documentation says retrieval of a single fact in a long context scores well, that with several facts to find the model does not perform with the same accuracy, and that putting the question at the end of a long prompt gives better results ([Google, *Long context*, Gemini API docs, last updated 15 Oct 2026](https://ai.google.dev/gemini-api/docs/long-context)).

None of these measured Opus 5.5 or any model current on 15 Nov 2026. The direction agrees across all of them: the more text in the window, the less reliably the model uses any one piece of it. How large the effect is on the model you use is unmeasured. Practical consequence (documented practice): Anthropic's team frames the job as finding the smallest set of high-signal tokens that makes the outcome you want likely ([Rajasekaran et al.](https://anthropic.com/engineering/effective-context-engineering-for-ai-agents)), and Claude Code's documentation asks for instruction files under 200 lines because longer files consume more context and reduce adherence ([Anthropic, *How Claude remembers your project*](https://code.claude.com/docs/en/memory), read 15 Nov 2026).

## 3 · What persists: inside a chat, across chats, and what memory changes

### Inside a chat

Inside one chat everything persists, because everything is re-sent (§2). On Opus 4.5 and later Opus models, the API also keeps the model's earlier thinking blocks by default, and they count against the window like any other input ([*Context windows*](https://platform.claude.com/docs/en/build-with-claude/context-windows), read 15 Nov 2026).

A fact can still be lost inside a chat in two ways.

1. **It is in the window and goes unused.** That is the attention problem in §2. A rule stated in turn 3 of a 40-turn chat is present and competing with everything written after it.
2. **It is summarised away.** On claude.ai, for users with code execution enabled, Claude summarises earlier messages when a chat grows long so the conversation can continue; the help centre says the full history is still kept so earlier content can be referred to ([*How do usage and length limits work?*](https://support.claude.com/en/articles/11647753-understanding-usage-and-length-limits), read 15 Nov 2026). In Claude Code, as the window fills, older tool outputs are cleared first and then the conversation is summarised; the documentation warns that detailed instructions from early in the conversation may be lost, and tells you to put persistent rules in the `CLAUDE.md` file instead ([Anthropic, *How Claude Code works*](https://code.claude.com/docs/en/how-claude-code-works), read 15 Nov 2026). Grade of that advice: documented practice.

### Across chats

Across chats nothing persists in the model. A new chat is a new request with a new window, built from whatever the product puts into it. Claude Code's documentation says it directly: each session begins with a fresh context window, and knowledge crosses sessions through two mechanisms, the `CLAUDE.md` files you write and the auto-memory notes Claude writes itself ([*How Claude remembers your project*](https://code.claude.com/docs/en/memory), read 15 Nov 2026). claude.ai runs on the same principle with more layers (all read 15 Nov 2026):

- **Profile instructions** are account-wide and applied to all your conversations; **project instructions** apply only to chats inside that project ([Claude Help Center, *Understanding Claude's personalization features*](https://support.claude.com/en/articles/10185728-understanding-claude-s-personalization-features)).
- **Project files** sit in project knowledge. When a project nears or passes the window limit, retrieval mode switches on automatically: Claude searches the uploaded documents and loads only the most relevant parts, which lets a project hold up to ten times more ([Claude Help Center, *Retrieval augmented generation (RAG) for projects*](https://support.claude.com/en/articles/11473015-retrieval-augmented-generation-rag-for-projects)).
- **Memory**, in Anthropic's post of 25 Aug 2026 (read 15 Nov 2026), is on by default on the Free, Pro, Max and Ultra plans; on Team and Enterprise, "admins control availability for their organization" and memory is off for each member until they turn it on. An undated update note on the same post changes that for members of most Team and Enterprise organisations created on or after 31 Oct 2026: memory is on by default for them, and owners can still turn it off for the organisation; nothing changes for organisations created before that date ([Anthropic, *Claude's memory works everywhere, and you decide what's in it*](https://claude.com/resources/articles/claudes-memory-works-everywhere-and-you-decide-whats-in-it)). The help-centre article cited below refused the fetch, so its plan list was not checked. Claude saves memory as individual topics during chats, and an update made in one chat is known in the next. Each project has its own memory: inside a project Claude uses that project's memory and your non-project memory, never another project's. Sensitive topics are not stored by default; incognito chats are not used for memory; deleting a conversation does not delete the memories written from it; and you can open, edit or delete any topic ([Claude Help Center, *Use Claude's chat search and memory to build on previous context*](https://support.claude.com/en/articles/11817273-use-claude-s-chat-search-and-memory-to-build-on-previous-context)).
- **Chat search**, on paid plans, retrieves past chats by search and shows the search as a tool call in the conversation; outside projects it searches all non-project chats, and inside a project only that project's chats (same article).

### What a memory feature changes

Memory changes what gets put into the next window. It does not change the model. Every layer above is text that something re-inserts; take the re-insertion away and the fact is gone. Memory is also text written by a model about your chats, so it is open to every failure in this unit: it can be incomplete, out of date or slightly wrong, and once inserted it competes for attention like anything else. How much memory is inserted into a given chat is not stated on the help-centre pages read for this unit.

One path does run from your chats into a model, and it is slow. Since Anthropic's consumer-terms update of 28 August 2025, users of the Free, Pro and Max plans choose whether their chats may be used to improve Claude; the setting applies to new or resumed chats, and data from users who allow it is kept for five years, against 30 days otherwise ([Anthropic, *Updates to Consumer Terms and Privacy Policy*, 28 Aug 2025](https://www.anthropic.com/news/updates-to-our-consumer-terms)). That feeds a future training run. None of the documentation read for this unit describes a path by which a chat changes the model you talk to the next day.

**The case.** In Academy (anecdote), writer agents were lost to container restarts; in one deep dive two writers were lost, and the third resumed from the second's working files (Academy case file §7). The conversation did not survive; the files did. That is the across-chats rule in one event: what you need to outlive a session has to be written somewhere a later window will read.

**Diagnostic.** When a new chat ignores something you said last week, ask which layer was supposed to carry it into this window, and whether it did. The usual answers: it was said inside another project; memory did not write it, or wrote another version; chat search was not triggered; the project was in retrieval mode and fetched other passages.

## 4 · Three kinds of knowledge, and the training cutoff

### Trained

Claude's underlying model was pretrained on a large body of text to predict the next word given the text before it, then fine-tuned and trained with reinforcement learning from human feedback to behave as a helpful assistant ([*Glossary*](https://platform.claude.com/docs/en/about-claude/glossary.md), read 15 Nov 2026). What it learned that way stops at a cutoff. On 15 Nov 2026, Anthropic lists the reliable knowledge cutoff of Opus 5.5, Sonnet 5.5, Haiku 5.5 and Fable 5.2 as June 2026, and points to its Transparency Hub for training-data cutoffs ([*Models overview*](https://platform.claude.com/docs/en/models/overview)). This unit was written five months after that cutoff. Any model lineup, price, plan limit or event after June 2026 is something the model can know only if it reaches the window: you supply it, a search fetches it, or memory re-inserts it.

The claude.ai system prompt supplies the current date at the start of every conversation ([Anthropic, *System prompts*](https://platform.claude.com/docs/en/release-notes/system-prompts.md), read 15 Nov 2026). So the model knows what day it is without knowing what has happened since June. That gap produces a characteristic failure: an answer that is correctly dated and out of date.

### Retrieved

Retrieval-augmented generation fetches material when the question is asked and passes it into the context window with the question, so that the answer can be grounded in evidence; the model can do the fetching itself through a tool ([*Glossary*](https://platform.claude.com/docs/en/about-claude/glossary.md)). The glossary adds that how well this works depends on the quality and relevance of what is retrieved (same page). Web search, chat search, a project in retrieval mode, a connector pulling a document, Claude Code reading a file: each is retrieval. Retrieval is selection. The model sees the passages that were fetched and nothing else, and the answer is only as current as the page it came from.

**The case.** In Academy's second audit (anecdote), ten claims in one unit were stale, all from one cause: an independent benchmark published a new index version the day before the unit read its leaderboard (Academy case file §4). The case file does not record how the older figures reached the unit. What it shows is that a fetched figure belongs to a version and a date, which is why this course dates every product fact to the day it was read.

### In the conversation

Whatever you typed, pasted or attached, plus everything the model wrote earlier in the same chat. The second half is easy to miss. Each response becomes part of the input for the next turn ([*Context windows*](https://platform.claude.com/docs/en/build-with-claude/context-windows)), so a wrong figure the model produced at turn 5 is in the window at turn 25, read on every turn like anything you supplied.

### Why the distinction matters

The three kinds look the same in the output. A sentence about last month's price reads the same whether it came from a page fetched ten seconds ago, from a memory note written last week, or from no source at all. The only way to tell is to know what was in the window. A claim that points to a fetched source can be checked against it; a claim that points to nothing came from training, or was produced without a basis (§7).

## 5 · Why the same prompt gives different answers

### Sampling is the design

At each step the model computes a probability distribution over possible next tokens, and one is drawn from it. Temperature is the parameter that controls how random that draw is: higher gives more varied output, lower gives more conservative, more probable phrasing ([*Glossary*](https://platform.claude.com/docs/en/about-claude/glossary.md), read 15 Nov 2026). Sampling is deliberate. Holtzman and colleagues showed that decoding by likelihood alone produces text that is bland and repetitive, and proposed sampling from the most probable part of the distribution ("nucleus sampling") to get diverse text without losing fluency (measured; [Holtzman, Buys, Du, Forbes and Choi, "The Curious Case of Neural Text Degeneration", arXiv:1904.09751, revised 14 Feb 2020](https://arxiv.org/abs/1904.09751); cited here as the arXiv version, since the conference version could not be checked).

On current Claude models you no longer set this yourself. On 15 Nov 2026, Anthropic's API documentation says the `temperature`, `top_p` and `top_k` parameters are not supported on Claude 4.7 and later models, that a non-default value returns an error, and that you should use prompting to guide behaviour instead ([*Using the Messages API*](https://platform.claude.com/docs/en/build-with-claude/working-with-messages.md)). None of the claude.ai help pages read for this unit offers a sampling setting either. The randomness is still there; you just do not hold the dial.

### Even fixed settings vary

Anthropic's glossary states that even with temperature set to 0, results will not be fully deterministic, and identical inputs may give different outputs across calls, on Anthropic's own service and through cloud providers ([*Glossary*](https://platform.claude.com/docs/en/about-claude/glossary.md)). The glossary does not give the cause. One lab gives a candidate. Horace He, with colleagues at Thinking Machines Lab, sampled 1,000 completions at temperature 0 from an open-weights model (Qwen3-235B-A22B-Instruct-2507) for one prompt, and got 80 distinct completions; the most common appeared 78 times, and the completions first diverged at token 103. He traced the variation to computations whose results depend on batch size, which varies with server load; with batch-invariant kernels, all 1,000 completions were identical ([He, *Defeating Nondeterminism in LLM Inference*, Thinking Machines Lab, 10 Sep 2025](https://www.thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/)). Grade: measured, in a lab blog post that is not peer-reviewed, on a non-Anthropic model and serving stack. Whether the same cause dominates on Anthropic's service is not stated by either source.

The divergence point is the useful detail. Once one token differs, every later token is conditioned on a different history, so a small early difference becomes a different answer.

### Usually the prompt was not the same

The more common reason two runs differ is that the window differed. Between two chats with the same typed prompt, the system prompt carries a new date and is periodically updated ([*System prompts*](https://platform.claude.com/docs/en/release-notes/system-prompts.md)); memory may have been updated in between, and chat search may return other chats ([*Use Claude's chat search and memory*](https://support.claude.com/en/articles/11817273-use-claude-s-chat-search-and-memory-to-build-on-previous-context)); a project in retrieval mode may fetch other passages ([*RAG for projects*](https://support.claude.com/en/articles/11473015-retrieval-augmented-generation-rag-for-projects)); and Opus 5.5 thinks adaptively, always on, so the amount of reasoning placed in the window varies with the request ([*Models overview*](https://platform.claude.com/docs/en/models/overview); [*Context windows*](https://platform.claude.com/docs/en/build-with-claude/context-windows), all read 15 Nov 2026). The model behind a name can also change. OpenAI's prompting guide warns that different snapshots of models in the same family can produce different results, and advises pinning production applications to a specific snapshot ([OpenAI, *Prompt engineering*](https://developers.openai.com/api/docs/guides/prompt-engineering), read 15 Nov 2026).

**The case.** In Academy (anecdote), a session's model named "fable" resolved to a newer version than the method names, so the checks it ran were recorded as owed again on the named version (Academy case file §7). Same instruction, different model.

**What this means for checking.** One good answer is one draw. It shows the window can produce a good answer; how often it does stays unknown until there are more draws. Anthropic's own guidance lists running the same prompt several times and comparing the outputs as a way to spot hallucinations, since inconsistency between runs can signal them ([Anthropic, *Reduce hallucinations*](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations.md), read 15 Nov 2026). Grade: documented practice (vendor), unmeasured on its page.

## 6 · System prompt, project instruction, user message

All three are text in the same window. They differ in who writes them, where they sit and how far they reach.

| Layer | Written by | Reaches | Source (read 15 Nov 2026) |
|---|---|---|---|
| claude.ai system prompt | Anthropic | Every claude.ai and mobile-app chat; not the API | [*System prompts*](https://platform.claude.com/docs/en/release-notes/system-prompts.md) |
| Profile instructions | You | All your conversations | [*Personalization features*](https://support.claude.com/en/articles/10185728-understanding-claude-s-personalization-features) |
| Project instructions | You | Chats inside that project only | [*Personalization features*](https://support.claude.com/en/articles/10185728-understanding-claude-s-personalization-features) |
| Skill name and description | The skill's author | Every chat where it is installed; the body loads only when triggered | [*Agent Skills*](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview.md) |
| User message | You | This turn, then every later turn of the chat | [*Context windows*](https://platform.claude.com/docs/en/build-with-claude/context-windows) |

**The system prompt** sets the frame. Anthropic publishes the claude.ai version and says it gives Claude up-to-date information such as the current date at the start of every conversation, encourages certain behaviours, is periodically updated, and that those updates do not apply to the API ([*System prompts*](https://platform.claude.com/docs/en/release-notes/system-prompts.md)). On the API the developer writes the system prompt, and a system message added partway through a conversation has the same authority as the top-level one ([*Using the Messages API*](https://platform.claude.com/docs/en/build-with-claude/working-with-messages.md)). Authority comes from the role a piece of text is given. When it arrives does not change it.

**Project instructions and profile instructions** are your standing orders at two scopes. The help centre says the personalisation features can be used independently or in combination, and states no order of precedence between them ([*Personalization features*](https://support.claude.com/en/articles/10185728-understanding-claude-s-personalization-features)). Two consequences follow. A rule repeated in two layers is paid for twice on every turn. Two layers that disagree leave the model to settle the conflict with no documented rule. OpenAI, by contrast, documents an order for its API: developer messages are prioritised ahead of user messages ([OpenAI, *Prompt engineering*](https://developers.openai.com/api/docs/guides/prompt-engineering)). Neither vendor's documentation read here says how its consumer chat app ranks a project's instructions against your account-wide ones.

**Skills** sit across the layers. On 15 Nov 2026, Anthropic's documentation says only each skill's name and description load at startup, about 100 tokens a skill, placed in the system prompt; the body of its `SKILL.md`, under 5K tokens, enters the window only when a request matches the description; and bundled files load only when read ([Anthropic, *Agent Skills*](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview.md)). The description is what your request is matched against (same page). Twenty installed skills therefore cost about 2,000 tokens in every chat, on Anthropic's per-skill figure, and each one fires on its description alone.

**The user message** is the request itself. Once sent, it is part of the history re-read on every later turn (§2).

**None of these is enforced.** Claude Code's documentation says Claude treats its instruction files as context and that they are not enforced configuration; to block an action whatever Claude decides, it points to a hook, a script that runs outside the model; and it says the more specific and concise the instructions, the more consistently Claude follows them ([*How Claude remembers your project*](https://code.claude.com/docs/en/memory), read 15 Nov 2026). The page is about Claude Code's files. Applying it to every instruction layer is this unit's inference, on the ground that every layer reaches the model the same way, as text in the window (§1). Every instruction raises the probability of a behaviour. None guarantees it.

**The case.** A structure audit of Academy itself (anecdote) made seventeen findings, among them project instructions that carried procedures and paraphrased the method file (Academy case file §7). A paraphrase in one layer and the original in another is the two-layer problem above: the same rule in two wordings, with nothing to say which wins. BW4 works through that audit.

## 7 · Fabrication follows from how the text is produced

A language model writes by predicting the next token from the text before it (§4, §5). Nothing in that step consults a store of facts. When the window holds a source, the most probable continuation tends to follow the source; when it does not, the most probable continuation is whatever reads like an answer. A fluent, specific, wrong sentence is therefore an ordinary output of the mechanism, produced the same way as a right one. Three lines of evidence support treating it that way.

- **A statistical argument (preprint).** Adam Tauman Kalai, Ofir Nachum, Santosh Vempala and Edwin Zhang argue that hallucinations originate as errors in binary classification: if incorrect statements cannot be told apart from facts, hallucinations in pretrained models arise through natural statistical pressures. They argue that they persist because training and evaluation procedures "reward guessing over acknowledging uncertainty" ([Kalai, Nachum, Vempala and Zhang, "Why Language Models Hallucinate", arXiv:2509.04664, 4 Sep 2025](https://arxiv.org/abs/2509.04664)). The paper is a preprint, and its argument is theoretical, with no new measurement on a current Claude model.
- **A mechanism observed inside a model (vendor research).** Anthropic's interpretability team reports that in the model it studied, a circuit that declines to answer is on by default, and a feature for known entities inhibits it; hallucinations occur when that known-entity feature fires on something the model recognises without actually knowing, suppressing the default ([Anthropic, *Tracing the thoughts of a large language model*, 27 Mar 2025](https://anthropic.com/research/tracing-thoughts-language-model)). The article's introduction says its companion research studied Claude 3.5 Haiku; the hallucination section does not name its model. Transfer to the model you use is this unit's inference.
- **The vendor's own statement (documented).** Anthropic's guide says even the most advanced models, Claude included, can generate text that is factually incorrect or inconsistent with the given context, and that its techniques reduce hallucinations without eliminating them ([*Reduce hallucinations*](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations.md), read 15 Nov 2026).

The practical consequence is a change of posture. A fabrication is a property of every unchecked output, present at some rate, and the rate is what you manage. Anthropic's guide lists ways to lower it (documented practice, vendor): give the model explicit permission to say it does not know; for long documents, have it extract word-for-word quotes before doing the task; have it cite a quote for each claim and retract any claim it cannot support; and tell it to use only the documents provided ([*Reduce hallucinations*](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations.md)). The page says the first "can drastically reduce" false information and gives no figure; treat the size of the effect as unmeasured.

Fabrication also covers more than invented sources. A real page cited for something it does not say, a figure carried to the wrong thing, a qualifier the source never wrote: each is text completed past what the window supported.

**The case** (anecdote). Of 36 Academy units given a fresh check before filing, 28 had at least one error in the writer's handed-in draft, with 58 errors across the 36. The kinds the reports name include a figure the cited page does not carry, an author named wrongly, a quotation the page does not hold, and a product fact that differed between two of the vendor's own pages (Academy case file §5). The first audit of three marketing units found 23 of 91 claims failing and nothing invented; the pattern it named was qualifiers the source does not carry (Academy case file §3). These counts come from one project, written by one model family, checked by others; they say nothing about rates elsewhere. They do show a shape. None of the kinds of error the reports name is an invented source, and in the one audit that counted, nothing was invented: a check for made-up sources alone would have caught none of those 23 failures. How to check by sample is BW6.

## 8 · The layers of a current assistant: a map

Every feature of a current assistant is a way of deciding what enters the window, when, and who chose it. The map below names the layers this course uses; later units fill them in (erratum 15 Nov 2026: the chat in BW3 and BW4; projects, memory, and tools and connectors in BW4, memory also in BW10; skills in BW8; agents in BW9). Product behaviour is as read on 15 Nov 2026.

| Layer | What it puts in the window | When | Source |
|---|---|---|---|
| **Chat** | Your messages, attachments and the model's replies so far | Every turn, all of it | [*Context windows*](https://platform.claude.com/docs/en/build-with-claude/context-windows) |
| **Project** | Project instructions; project files, loaded whole or, in retrieval mode, the passages a search returns | Every chat in the project | [*Personalization features*](https://support.claude.com/en/articles/10185728-understanding-claude-s-personalization-features); [*RAG for projects*](https://support.claude.com/en/articles/11473015-retrieval-augmented-generation-rag-for-projects) |
| **Memory** | Notes a model wrote about earlier chats; past chats, when chat search runs | Next chat, as the app inserts them; search results when searched | [*Chat search and memory*](https://support.claude.com/en/articles/11817273-use-claude-s-chat-search-and-memory-to-build-on-previous-context) |
| **Tools and connectors** | Results of a web search, a file read, or an action in a connected service | The connector: at the start in Always available mode, by Claude's choice in Auto, when searched for in On demand ([*Manage Claude's tool access*](https://support.claude.com/en/articles/13730515-manage-claude-s-tool-access)); its results: only when called, then for the rest of the chat (erratum 15 Nov 2026: was "Only when called, then for the rest of the chat") | [*Use connectors*](https://support.claude.com/en/articles/11176164-use-connectors-to-extend-claude-s-capabilities); [*How Claude Code works*](https://code.claude.com/docs/en/how-claude-code-works) |
| **Skills** | A name and description per skill; the body and files on trigger | Description always; body when a request matches | [*Agent Skills*](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview.md) |
| **Agents** | Whatever the agent's own tool calls bring in, in a loop | Throughout a task; a subagent in its own window, fresh unless forked from the conversation | [*How Claude Code works*](https://code.claude.com/docs/en/how-claude-code-works) |

Notes on the rows:

- **Tools and connectors.** Anthropic's help centre says connectors let Claude access your apps and services, retrieve your data and take actions in them; custom connectors use the remote Model Context Protocol (MCP) ([Claude Help Center, *Use connectors to extend Claude's capabilities*](https://support.claude.com/en/articles/11176164-use-connectors-to-extend-claude-s-capabilities), read 15 Nov 2026). In Claude Code, MCP tool definitions are deferred by default, so only tool names and server instructions take up context until a tool is used ([*How Claude Code works*](https://code.claude.com/docs/en/how-claude-code-works)). Every result a tool returns is new text in the window.
- **Agents.** Claude Code describes its working cycle as an agentic loop: gather context, take action, verify results, repeated, with tools that read and edit files, run commands and search the web; the model reasons and the surrounding harness supplies the tools and manages what the model sees. A subagent works in its own context window and hands back a summary ([*How Claude Code works*](https://code.claude.com/docs/en/how-claude-code-works), read 15 Nov 2026). An agent is the same model reading the same kind of window; what differs is that it fills much of that window itself, with the results of its own actions.
- **What none of the layers does.** None of them changes the model's weights (§3). Each puts text in front of it.

## 9 · Reading a failed output

When an output fails, the model in §1 to §7 gives five questions, asked in this order because each is cheaper to answer than the next.

1. **Was the needed fact in the window?** If it lives only in a past chat, another project, a file nobody attached or your head, the model never had it (§3, §4).
2. **Was it buried?** If it was there, how much else was there with it, and where did it sit? Long windows degrade recall, and a long chat may have been summarised (§2, §3).
3. **Did it come from a source, or from training?** If no source in the window supports the claim, it came from trained knowledge, which stops at the cutoff, or from nowhere (§4, §7).
4. **Do two layers disagree?** If the system prompt, your standing instructions, a skill and your message pull different ways, nothing documented says which wins (§6).
5. **Was it one draw?** Run it again in a fresh chat. If the answers differ materially, neither is reliable on its own (§5).

Grade: stated opinion (this unit's ordering, built on §1 to §7). Each answer points to a different change: put the fact in a layer that re-inserts it; trim the window or start a new chat; supply the source and ask for quotes; keep each rule in one layer; run it again and check a sample. The decision below draws the same order.

```viz
{
  "kind": "decision",
  "root": {
    "q": "Was the needed fact in the window?",
    "tone": 4,
    "branches": [
      {"label": "no", "to": {"outcome": "Put it in a layer that re-inserts it", "tone": 1}},
      {"label": "yes", "to": {
        "q": "Was it buried?",
        "tone": 4,
        "branches": [
          {"label": "yes", "to": {"outcome": "Trim the window or start a new chat", "tone": 1}},
          {"label": "no", "to": {
            "q": "Did it come from a source, or from training?",
            "tone": 4,
            "branches": [
              {"label": "no source", "to": {"outcome": "Supply the source; ask for quotes", "tone": 1}},
              {"label": "a source", "to": {
                "q": "Do two layers disagree?",
                "tone": 4,
                "branches": [
                  {"label": "yes", "to": {"outcome": "Keep each rule in one layer", "tone": 1}},
                  {"label": "no", "to": {
                    "q": "Was it one draw?",
                    "tone": 4,
                    "branches": [
                      {"label": "yes", "to": {"outcome": "Run it again; check a sample", "tone": 1}}
                    ]
                  }}
                ]
              }}
            ]
          }}
        ]
      }}
    ]
  },
  "caption": "The five questions for reading a failed output, in the order §9 of this unit asks them, each with the change its answer points to; a path ends at the first answer that points to a change, and every other path reaches the fifth question, whether the output was one draw (the unit's own reasoning in §9, drawing on the sources cited in §2 to §7)."
}
```

The diagnosis table at the end of this unit turns these five questions into symptoms you can recognise, with the change each one points to and the unit of this course that treats it.

## 10 · On other tools

The principles in §1 to §9 (a window rebuilt on every turn, cost and attention both spent in tokens, nothing persisting except what something re-inserts, a cutoff, sampling, instruction layers that raise probabilities, fabrication as a rate) are stated for any current assistant. The detail is Claude's. Below, each Claude-specific claim, with the equivalent where the other vendor's own documentation was found (all read 15 Nov 2026). Two OpenAI help-centre pages (memory, and apps in ChatGPT) refused the fetch and were not checked.

| Claim in this unit | Claude | ChatGPT (OpenAI) | Gemini (Google) |
|---|---|---|---|
| The API keeps no state; history is re-sent and re-billed (§2) | [*Using the Messages API*](https://platform.claude.com/docs/en/build-with-claude/working-with-messages.md) | Each request stateless; chained input re-billed: [*Conversation state*](https://developers.openai.com/api/docs/guides/conversation-state) | Not checked for this unit |
| Long context degrades use of any one piece (§2) | [*Context windows*](https://platform.claude.com/docs/en/build-with-claude/context-windows) | No vendor statement found in the pages read | Several facts found less accurately than one; question at the end: [*Long context*](https://ai.google.dev/gemini-api/docs/long-context) |
| Window sizes and prices (§1, §2) | [*Models overview*](https://platform.claude.com/docs/en/models/overview); [*Context window on paid plans*](https://support.claude.com/en/articles/8606394-how-large-is-the-context-window-on-paid-claude-plans) | Not checked for this unit | Not checked for this unit |
| Memory written between chats; deleting a chat leaves its memories (§3) | [*Chat search and memory*](https://support.claude.com/en/articles/11817273-use-claude-s-chat-search-and-memory-to-build-on-previous-context) | Saved memories and chat history; deleting a chat does not delete its memories; temporary chats use no memory: [*Memory and new controls for ChatGPT*](https://openai.com/index/memory-and-new-controls-for-chatgpt/) | Personal context saved in settings or by asking; can look at past chats: [*Save info and reference past chats in Gemini Apps*](https://support.google.com/gemini/answer/16413516) |
| Per-project memory kept apart (§3) | [*Chat search and memory*](https://support.claude.com/en/articles/11817273-use-claude-s-chat-search-and-memory-to-build-on-previous-context) | Project-only memory limits chat context to the project: [*Using projects in ChatGPT*](https://openai.com/academy/projects) (10 Apr 2026) | No equivalent found in the pages read |
| Account-wide and project instructions; no documented precedence (§6) | [*Personalization features*](https://support.claude.com/en/articles/10185728-understanding-claude-s-personalization-features) | Custom instructions apply to every conversation: [*Custom instructions for ChatGPT*](https://openai.com/index/custom-instructions-for-chatgpt/) (20 Jul 2023); project instructions: [*Using projects in ChatGPT*](https://openai.com/academy/projects); precedence between them not stated | Gems hold a name, instructions and files: [*Use Gems in Gemini Apps*](https://support.google.com/gemini/answer/15146780?hl=en); on personal accounts they move to skills from November 2026 (see the skills row) |
| Instruction roles: a later system message keeps full authority (§6) | [*Using the Messages API*](https://platform.claude.com/docs/en/build-with-claude/working-with-messages.md) | Developer messages prioritised ahead of user messages: [*Prompt engineering*](https://developers.openai.com/api/docs/guides/prompt-engineering) | Not checked for this unit |
| Skills: description always loaded, body on trigger (§6, §8) | [*Agent Skills*](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview.md) | No equivalent found in the pages read | Skills are reusable custom instructions that Gemini can apply when relevant; on personal accounts (users 18 and over), Gems become read-only on 17 Nov 2026 and move to skills: [*About the transition from Gems to skills*](https://support.google.com/gemini/answer/18560919?hl=en) |
| Sampling settings not exposed on current models (§5) | [*Using the Messages API*](https://platform.claude.com/docs/en/build-with-claude/working-with-messages.md) | Output non-deterministic; snapshots differ: [*Prompt engineering*](https://developers.openai.com/api/docs/guides/prompt-engineering) | Not checked for this unit |
| Connectors and agents (§8) | [*Use connectors*](https://support.claude.com/en/articles/11176164-use-connectors-to-extend-claude-s-capabilities); [*How Claude Code works*](https://code.claude.com/docs/en/how-claude-code-works) | Not checked: the help page refused the fetch | Not checked for this unit |

The research in §2, §5 and §7 spans vendors where it tested many models (Chroma: 18 models, Claude and GPT models among them) and is specific where it did not (He: one Qwen model; Anthropic's interpretability work: a Claude model).

## Deliverable · A five-minute model and a diagnosis table

Four parts. Parts 1 and 2 are the model of how an assistant works, as prose you could say to a colleague in five minutes: first as it reads for the Academy case, then as a template for your own project. Parts 3 and 4 are the diagnosis table that BW3, BW4 and BW6 point back to: first in full with the Academy case's instances, then as a template. Every claim in both parts is sourced in §1 to §10 above; product facts are as read on 15 Nov 2026.

### Part 1 · The five-minute model, on the Academy case

The assistant does not remember anything. Each time a message is sent, the app sends the model one long piece of text, and the model writes its reply by reading that text. That text is the context window. It holds the vendor's own instructions, any standing instructions, the files of whatever project the chat sits in, any notes the app keeps, the whole conversation so far, and the new message. The model reads all of it, writes a reply, and keeps nothing. On the next message the whole lot is sent again with the new message on the end.

So the only way to change what the model does is to change what is in that text. The model itself is fixed. It was trained on a huge amount of writing to predict the next word, then trained further to act as an assistant, and what it learned that way stops at a cutoff: for the current Claude models, June 2026. Anything after that it knows only if something puts it in the window: someone pastes it, a search fetches it, or a memory note carries it. In Academy, ten claims in one unit went stale at once: an independent benchmark had published a new index version the day before the unit read its leaderboard. A fetched fact belongs to a version and a date, which is why every product fact carries the date it was read.

What looks like memory is re-insertion. The app writes notes about earlier chats and puts some of them into the next window; a project puts its instructions and files into every chat inside it; Claude Code reads its instruction file at the start of each session. If a fact was never written to one of those places, a new chat has never heard of it. Academy lost two writer agents to container restarts; the third picked up from the second's working files. The conversation was gone. The files were still there.

The text is measured in tokens, a few characters each. Tokens are what it costs: the whole conversation is re-sent every turn, so a long chat costs more with every message. Tokens are also attention: the more text there is, the less reliably the model uses any one piece of it, especially what sits in the middle. A bigger window raises the ceiling on how much fits. It does nothing for how well the model uses what is there. Academy writes each unit in a fresh context that sees only its brief and the units already filed; the reason it gives is that leaked context is how a course starts repeating itself.

The same request can get different answers. The model draws each next word from a spread of likely options, and even with the settings fixed, the servers do not return exactly the same result every time. More often, the two windows differed: a new date, an updated note, a different search result, a different model behind the same name. In Academy, a session's model, called by the name the method uses, resolved to a newer version than the one the method names. One good answer is one draw. It shows the setup can get it right and says nothing about how often.

Instructions sit at different levels: the vendor's in every chat, the account-wide ones in every chat of that account, a project's only in that project, and then the message itself. All of them are text in the same window. None is a hard rule; each makes a behaviour more likely, and shorter, more specific instructions are followed more consistently. When two levels say the same thing in different words, nothing documented says which one wins. Academy's own structure audit found project instructions that paraphrased the method file.

The model will sometimes write things that are not true, because it writes what is probable given the text in front of it, and when no source is there, a plausible answer is what comes out. In Academy, 28 of 36 drafts had at least one error when a separate checker read them against their sources, and none of the kinds of error named was an invented source: they include a figure the page does not carry, a quotation it does not hold, an author named wrongly. That is one project, and it proves nothing in general; it is why 36 of Academy's units got a fresh check of every cited claim before they were filed.

When something goes wrong, ask five things in order. Was the fact in the window? Was it buried? Did it come from a source or from training? Do two instructions disagree? Was it one draw? Each has a different fix.

*Sources for Part 1:* the mechanism, §1 to §7; Academy facts, Academy case file §2 (fresh context per unit; checking), §4 (benchmark), §5 (28 of 36 drafts), §7 (restarts, model name, structure audit).

### Part 2 · Template: your five-minute model

Copy this, fill each blank, and say it aloud once to check it fits in five minutes. Keep the mechanism sentences as they are; change only the blanks. Each blank says what goes in it.

> The assistant does not remember anything. Each time I send a message, [*name of the app or tool you use*] sends the model one long piece of text, the context window, and the model writes its reply by reading it. In my setup that text holds [*list what enters your window: the vendor's system prompt, your account-wide instructions, your project's instructions and files, memory if it is on, the connectors and skills you have switched on*], the conversation so far, and my new message. The model keeps nothing; next turn, the whole lot is sent again.
>
> The model is fixed, and what it learned in training stops at [*the reliable knowledge cutoff of the model you use, from the vendor's model page, with the date you read it*]. Anything after that reaches it only through [*the ways current facts reach your window: you paste them, web search, a connector, a project file*]. In my project, the facts that change are [*the facts in your project that go out of date: prices, rules, product features, figures*], so I date each one to the day I read it.
>
> What looks like memory is re-insertion. The things I need every chat to know live in [*the layer you keep them in: project instructions, a project file, an instruction file such as CLAUDE.md*]; anything said only in a chat is gone when the chat ends.
>
> Tokens are cost and attention. My window on [*model and plan*] is [*the window size from the vendor's page, with the date read*], and my usage is limited by [*your plan's limit, or the API price per million tokens, with the date read*]. I keep the window short by [*your rule for when to start a new chat and what to leave out*].
>
> The same request can give different answers, so one good answer is one draw. For [*the outputs in your project that matter most*], I check [*how you check: a second run, a sample of claims against their sources, a second reader*] before I trust them.
>
> My instructions live at these levels: [*each layer you use, and what it holds*]. Each rule lives in one layer only, and none of them is enforced.
>
> The model will sometimes write things that are not true. The kind of error that would hurt my project most is [*the error that costs you most: a wrong figure, a misquoted source, a wrong date, an invented name*], and I catch it by [*your check*].
>
> When something goes wrong, I ask: was it in the window, was it buried, did it come from a source, do two instructions disagree, was it one draw?

### Part 3 · The diagnosis table, on the Academy case

Each row: a symptom you can see in an output, its likely cause in the model of this unit, what to change, and the unit of this course that treats it. The Academy column gives the case's instance where the case file holds one, with the case file's section number (anecdote; reading each instance as that cause is this unit's interpretation, which the case file does not make). "Likely" means the cause to check first, in the order of §9; it is a diagnosis to test, never a verdict.

| Symptom | Likely cause in the model | What to change | Evidence for the change | Academy case instance | Treated in |
|---|---|---|---|---|---|
| A new chat does not know something said in an earlier chat | The fact was never re-inserted: said in another project, not written to memory, chat search not run (§3) | Put the fact in a layer that re-inserts it (project instructions or file, instruction file), or paste it | Documented practice: [*How Claude remembers your project*](https://code.claude.com/docs/en/memory); [*Chat search and memory*](https://support.claude.com/en/articles/11817273-use-claude-s-chat-search-and-memory-to-build-on-previous-context) | Writers lost to container restarts; the third resumed from the second's working files (§7) | BW4 |
| An instruction given early in a long chat stops being followed | Buried among later text, or summarised away when the chat was compacted (§2, §3) | Move the rule to a standing layer; start a new chat that carries only what the task needs | Documented practice: [*How Claude Code works*](https://code.claude.com/docs/en/how-claude-code-works); context rot measured on older models: [Liu et al.](https://aclanthology.org/2024.tacl-1.9/), [Chroma](https://trychroma.com/research/context-rot) (vendor) | No instance in the case file; its one-context-per-unit rule (§2) applies this change in advance | BW3, BW4 |
| A long attached document is used unevenly; facts from its middle are missed | Position and length effects in a long window (§2) | Shorten what you attach; ask for word-for-word quotes first; put the question after the material | Measured on 2023 models: [Liu et al.](https://aclanthology.org/2024.tacl-1.9/); documented practice: [*Reduce hallucinations*](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations.md), [*Long context*](https://ai.google.dev/gemini-api/docs/long-context) | No instance in the case file | BW3 |
| A confident, specific claim with no source behind it is wrong | Generated from training patterns with no source in the window; fabrication as a rate (§4, §7) | Supply the source; allow it to say it does not know; require a quote per claim and drop claims without one | Documented practice (vendor), effect unmeasured: [*Reduce hallucinations*](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations.md); mechanism: [Kalai et al.](https://arxiv.org/abs/2509.04664) (preprint) | A quotation the page does not hold; an author named wrongly (§5) | BW6 |
| A cited page exists but does not say what the output says | Text completed past what the source supports: a stretched qualifier, a figure moved to another thing (§7) | Check each cited claim against its page, by a reader who did not write it | Documented practice (vendor): have the model find a supporting quote for each claim and retract any it cannot support, [*Reduce hallucinations*](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations.md); a separate reader is practice in one project, no control (case file §9) | Audit 1: 23 of 91 claims failed, nothing invented; pattern: qualifiers the source does not carry (§3); a figure the cited page does not carry (§5) | BW6 |
| An answer about a recent price, product or rule is out of date | After the training cutoff, and nothing current was retrieved; or the retrieved page has since changed (§4) | Turn on search or paste the current page; date every fact to the day it was read | Vendor statement of cutoff: [*Models overview*](https://platform.claude.com/docs/en/models/overview) | Ten claims stale after a benchmark published a new index version the day before (§4) | BW6 |
| Two vendor pages, or two of your own files, give different values | Two sources in or near the window disagree; the model picks one (§4) | Name which source is authoritative; cite the more specific page and record the conflict | Stated opinion (this unit) | A product fact that differed between two of the vendor's own pages (§5) | BW4, BW6 (erratum 15 Nov 2026: was BW6) |
| The same request gives materially different answers | Sampling, server-side variation, or a different window: date, memory, retrieval, model version (§5) | Run it more than once and compare; fix the inputs in the brief; pin the model where you can | Measured on one non-Anthropic model: [He](https://www.thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/); documented practice: [*Reduce hallucinations*](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations.md), [*Prompt engineering*](https://developers.openai.com/api/docs/guides/prompt-engineering) | A model name resolved to a newer version than the method names (§7) | BW6 |
| The output follows one rule and breaks another | Two instruction layers disagree, with no documented precedence (§6) | Keep each rule in one layer, in one wording; remove paraphrases | Documented practice: [*How Claude remembers your project*](https://code.claude.com/docs/en/memory); no precedence stated: [*Personalization features*](https://support.claude.com/en/articles/10185728-understanding-claude-s-personalization-features) | Project instructions that carried procedures and paraphrased the method file (§7) | BW4 |
| A skill fires when it should not, or fails to fire | Skills trigger on their description alone (§6) | Rewrite the description to say what the skill does and when to use it | Vendor documentation: [*Agent Skills*](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview.md) | No instance in the case file | BW8 (erratum 15 Nov 2026: was BW4) |
| A large project answers from the wrong file | Retrieval mode fetched other passages (§3, §4) | Name the file in the request; trim project knowledge below the point where retrieval switches on | Vendor documentation: [*RAG for projects*](https://support.claude.com/en/articles/11473015-retrieval-augmented-generation-rag-for-projects) | No instance in the case file | BW4 |
| The usage limit is reached early | Long chats re-send their history every turn; tools and connectors are token-intensive (§2) | Start a new chat per task; switch off connectors the task does not need | Vendor documentation: longer conversations that trigger automatic context management consume more of the limit, and the page suggests a new conversation; tools and connectors are token-intensive: [*How do usage and length limits work?*](https://support.claude.com/en/articles/11647753-understanding-usage-and-length-limits) | No instance in the case file (it holds no measure of usage spent, §9) | BW4, BW10 (erratum 15 Nov 2026: was BW4) |

### Part 4 · Template: your diagnosis table

Keep the first four columns: they are the course's shared vocabulary, and later units point back to them. Fill the last column from your own project, and add rows for symptoms your project shows that the table lacks.

| Symptom | Likely cause in the model | What to change | Treated in | Your instance |
|---|---|---|---|---|
| A new chat does not know something said in an earlier chat | Never re-inserted (§3) | Put it in a layer that re-inserts it | BW4 | [*the fact that went missing, and the layer that should have carried it*] |
| An instruction given early in a long chat stops being followed | Buried or summarised away (§2, §3) | Move it to a standing layer; start a new chat | BW3, BW4 | [*the instruction, and the turn at which it stopped holding*] |
| A long document is used unevenly | Position and length effects (§2) | Shorten; quotes first; question last | BW3 | [*the document, its length, and what was missed*] |
| A confident claim with no source is wrong | No source in the window; fabrication as a rate (§4, §7) | Supply the source; quote per claim | BW6 | [*the claim, and where the right answer was*] |
| A cited page does not say what the output says | Text completed past the source (§7) | Check each cited claim against its page | BW6 | [*the claim, the page, and what the page actually says*] |
| A recent fact is out of date | Past the cutoff, or the page changed (§4) | Search or paste; date the fact | BW6 | [*the fact, the date you read it, and the date it changed*] |
| Two sources give different values | Conflict in or near the window (§4) | Name the authoritative source; record the conflict | BW4, BW6 (erratum 15 Nov 2026: was BW6) | [*the two sources and the two values*] |
| Same request, different answers | Sampling or a different window (§5) | Run twice, compare; fix the inputs | BW6 | [*the request, and how the answers differed*] |
| One rule followed, another broken | Layers disagree (§6) | One rule, one layer, one wording | BW4 | [*the two layers and the two wordings*] |
| A skill fires wrongly | Description-only trigger (§6) | Rewrite the description | BW8 (erratum 15 Nov 2026: was BW4) | [*the skill, the request, and what happened*] |
| A large project answers from the wrong file | Retrieval fetched other passages (§3) | Name the file; trim the project | BW4 | [*the file it should have used*] |
| The usage limit arrives early | History re-sent; tools token-heavy (§2) | New chat per task; fewer connectors | BW4, BW10 (erratum 15 Nov 2026: was BW4) | [*the chat length, and the tools that were on*] |
| [*a symptom your project shows*] | [*which of §2 to §7 explains it*] | [*the change you will test*] | [*the unit that treats it, once you reach it*] | [*the instance*] |

## Sources

All web pages read on 15 November 2026. Anthropic's help-centre pages show no exact date.

**Vendor documentation and statements: Anthropic**

- Anthropic. *Context windows*. Claude Platform Docs. https://platform.claude.com/docs/en/build-with-claude/context-windows
- Anthropic. *Glossary*. Claude Platform Docs. https://platform.claude.com/docs/en/about-claude/glossary.md
- Anthropic. *Models overview*. Claude Platform Docs. https://platform.claude.com/docs/en/models/overview
- Anthropic. *Using the Messages API*. Claude Platform Docs. https://platform.claude.com/docs/en/build-with-claude/working-with-messages.md
- Anthropic. *Agent Skills*. Claude Platform Docs. https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview.md
- Anthropic. *System prompts* (release notes). Claude Platform Docs. https://platform.claude.com/docs/en/release-notes/system-prompts.md
- Anthropic. *Reduce hallucinations*. Claude Platform Docs. https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations.md
- Anthropic. *How Claude remembers your project*. Claude Code Docs. https://code.claude.com/docs/en/memory
- Anthropic. *How Claude Code works*. Claude Code Docs. https://code.claude.com/docs/en/how-claude-code-works
- Rajasekaran, P., Dixon, E., Ryan, C. and Hadfield, J. (Anthropic Applied AI team). *Effective context engineering for AI agents*. Anthropic Engineering, 29 September 2025. https://anthropic.com/engineering/effective-context-engineering-for-ai-agents
- Anthropic. *Tracing the thoughts of a large language model*. 27 March 2025 (vendor research). https://anthropic.com/research/tracing-thoughts-language-model
- Anthropic. *Updates to Consumer Terms and Privacy Policy*. 28 August 2025. https://www.anthropic.com/news/updates-to-our-consumer-terms
- Claude Help Center. *How large is the context window on paid Claude plans?* https://support.claude.com/en/articles/8606394-how-large-is-the-context-window-on-paid-claude-plans
- Claude Help Center. *How do usage and length limits work?* https://support.claude.com/en/articles/11647753-understanding-usage-and-length-limits
- Claude Help Center. *Use Claude's chat search and memory to build on previous context*. https://support.claude.com/en/articles/11817273-use-claude-s-chat-search-and-memory-to-build-on-previous-context
- Anthropic. *Claude's memory works everywhere, and you decide what's in it*. 25 August 2026, with an undated update note. https://claude.com/resources/articles/claudes-memory-works-everywhere-and-you-decide-whats-in-it
- Claude Help Center. *Understanding Claude's personalization features*. https://support.claude.com/en/articles/10185728-understanding-claude-s-personalization-features
- Claude Help Center. *Retrieval augmented generation (RAG) for projects*. https://support.claude.com/en/articles/11473015-retrieval-augmented-generation-rag-for-projects
- Claude Help Center. *Use connectors to extend Claude's capabilities*. https://support.claude.com/en/articles/11176164-use-connectors-to-extend-claude-s-capabilities
- Claude Help Center. *Manage Claude's tool access*. 16 March 2026. https://support.claude.com/en/articles/13730515-manage-claude-s-tool-access

**Vendor documentation and statements: OpenAI and Google**

- OpenAI. *Conversation state*. OpenAI API docs. https://developers.openai.com/api/docs/guides/conversation-state
- OpenAI. *Prompt engineering*. OpenAI API docs. https://developers.openai.com/api/docs/guides/prompt-engineering
- OpenAI. *Memory and new controls for ChatGPT*. 13 February 2024, with updates to 3 June 2025. https://openai.com/index/memory-and-new-controls-for-chatgpt/
- OpenAI. *Using projects in ChatGPT*. OpenAI Academy, 10 April 2026. https://openai.com/academy/projects
- OpenAI. *Custom instructions for ChatGPT*. 20 July 2023. https://openai.com/index/custom-instructions-for-chatgpt/
- Google. *Long context*. Gemini API docs, last updated 15 October 2026. https://ai.google.dev/gemini-api/docs/long-context
- Google. *Save info and reference past chats in Gemini Apps*. Gemini Apps Help. https://support.google.com/gemini/answer/16413516
- Google. *Use Gems in Gemini Apps*. Gemini Apps Help. https://support.google.com/gemini/answer/15146780?hl=en
- Google. *About the transition from Gems to skills*. Gemini Apps Help. https://support.google.com/gemini/answer/18560919?hl=en

**Research**

- Liu, N. F., Lin, K., Hewitt, J., Paranjape, A., Bevilacqua, M., Petroni, F. and Liang, P. "Lost in the Middle: How Language Models Use Long Contexts". *Transactions of the Association for Computational Linguistics* 12 (2024): 157–173. doi:10.1162/tacl_a_00638. https://aclanthology.org/2024.tacl-1.9/ (peer-reviewed)
- Hong, K., Troynikov, A. and Huber, J. *Context Rot: How Increasing Input Tokens Impacts LLM Performance*. Chroma technical report, 14 July 2025. https://trychroma.com/research/context-rot (vendor research)
- Holtzman, A., Buys, J., Du, L., Forbes, M. and Choi, Y. "The Curious Case of Neural Text Degeneration". arXiv:1904.09751, v2, 14 February 2020. https://arxiv.org/abs/1904.09751
- He, H., with Thinking Machines Lab. *Defeating Nondeterminism in LLM Inference*. Thinking Machines Lab, 10 September 2025 (lab blog, not peer-reviewed). https://www.thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/
- Kalai, A. T., Nachum, O., Vempala, S. S. and Zhang, E. "Why Language Models Hallucinate". arXiv:2509.04664, 4 September 2025 (preprint). https://arxiv.org/abs/2509.04664

**The case**

- Academy case file (`generator/data/building-with-ai/case-academy.md`), compiled 11 November 2026; cited by section, §2 to §9.

## Unsure list

1. The "Treated in" column of the diagnosis table (Parts 3 and 4) assigns rows to BW3 (briefing), BW4 (project structure) and BW6 (verification). Only BW4's subject is supported by the packet (Academy case file §7: the structure audit is the source of BW4); BW3 and BW6 are inferred from the brief's Gives line and the order of the course goal. Their briefs were not in the packet.
2. Holtzman et al. is cited as the arXiv version (v2, 14 Feb 2020); the ICLR 2020 conference version was not checked, so it is not claimed.
3. Anthropic, "Tracing the thoughts of a large language model": the hallucination section does not name its model; the unit says the introduction names Claude 3.5 Haiku for the companion research, and that transfer is inference.
4. Liu et al.: "the models tested date from 2023" rests on the paper's 2023 arXiv posting (2307.03172) and its 2024 journal date; the list of models was not re-read on the page fetched (abstract only).
5. Chroma, Context Rot: "Claude and GPT models among them" is from the page's distractor-test discussion as summarised by the fetch; the full model list beyond the five Claude models was not read.
6. Anthropic help-centre pages carry no exact date ("updated this week", "over 3 weeks ago"); the window sizes, memory behaviour and plan lists were read on 15 Nov 2026 and may change within days.
7. OpenAI help-centre pages (Memory FAQ, Projects in ChatGPT, Apps in ChatGPT) refused the fetch and were not checked; ChatGPT rows in "On other tools" rest on openai.com pages (Memory and new controls for ChatGPT; Using projects in ChatGPT; Custom instructions for ChatGPT) and the OpenAI API docs.
8. Gemini skills: "Gemini can apply a skill when relevant" and the Gems read-only date (17 Nov 2026, personal accounts, users 18 and over) come from one Gemini Apps Help page with no publication date.
9. Message threads (Anthropic API, beta): the unit reports the page's statement that the API keeps the conversation; how billing treats the kept history was not read.
10. Opus 5.5 "adaptive thinking, always on" is from the Models overview table as fetched; the effect on how much reasoning enters the window per request is the unit's reading.
Object: the context window (§1 and §2)

Fresh check 2026-11-15 (claude-opus-5-5): fix · 1 errors, 7 should-fix, 7 minor; report `audits/building-with-ai/fresh-check-BW1.md`

Correction 15 Nov 2026, found by BW3's corrections check (Opus 5.5, row W-BW3, flag F3): 7 exact replacements applied to §8 (the layer map names the unit that treats each layer) and to the "Treated in" column of the diagnosis table (Parts 3 and 4), each checked against the course's briefs; `audits/building-with-ai/corrections-2026-11-15-BW1-B3.md`.
