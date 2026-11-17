---
code: BW2
title: Choosing the model and the effort
course: building-with-ai
model: Opus 5.5
written: 2026-11-15
search: on
---

# BW2 · Choosing the model and the effort

Every product fact in this unit (a model name, a price, a default, a plan limit) was read on the vendor's own page on 15 November 2026 and carries that date. Help-centre and documentation pages mostly show no exact date, so the reading date is the only one they can be given. Benchmark figures name who ran the test, which version and when. Research findings name the models they tested; carrying a finding to a current model is this unit's inference and is said to be. Each practice carries an evidence grade, as in BW1: **measured**, **documented practice** (a vendor or a named practitioner says to do it; nobody measured it here) or **stated opinion**. What a token is, why the whole conversation is re-sent on every turn and why a model's knowledge stops at a cutoff are in BW1 (§2, §4); this unit uses them without restating them.

## 1 · Cost per task

A price list gives the cost of one token. What you pay for is a finished job. The cost of a task is the input tokens times the input price, plus the output tokens times the output price, summed over every turn the task takes, with the history re-sent on each turn (BW1 §2). The price list fixes one factor. The other, how many tokens the model spends to finish, is set by the model and by the effort setting (§3), and it varies more than the price does.

Two parts of the output are easy to miss.

- **Thinking is output.** On Claude, the tokens the model spends thinking are billed as output tokens, and in full even when the app shows only a summary of the thinking; thinking blocks kept from earlier turns are billed again as input ([Anthropic, *Steering thinking*](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking?r=0), read 15 Nov 2026). OpenAI documents the same for its reasoning tokens, which are hidden, count toward the context window and are billed as output ([OpenAI, *Reasoning models*](https://developers.openai.com/api/docs/guides/reasoning.md), read 15 Nov 2026), and Google bills a Gemini response as its output plus its thinking tokens, for the full thoughts even when only a summary is returned ([Google, *Gemini thinking*](https://ai.google.dev/gemini-api/docs/generate-content/thinking?authuser=1), last updated 14 Oct 2026, read 15 Nov 2026).
- **Output costs five times input** on every current Claude model: $4 and $20 per million tokens for Opus 5.5, for example ([Anthropic, *Models overview*](https://platform.claude.com/docs/en/models/overview), read 15 Nov 2026). A model that thinks at length pays the dear rate on every token of it.

**What the measured comparison shows.** Artificial Analysis, an independent benchmarking company, runs one set of tasks across models and reports a cost per task: the weighted-average cost in US dollars to complete one task of its Intelligence Index, computed from the tokens each model consumed and its price, which is the first-party API rate or the median across providers ([Artificial Analysis, *Artificial Analysis Benchmarking Methodology*](https://artificialanalysis.ai/methodology), read 15 Nov 2026). On its leaderboard on 15 November 2026, under Intelligence Index v5.0.1 ([*Claude Opus 5.5: Intelligence, Performance & Price Analysis*](https://artificialanalysis.ai/models/claude-opus-5-5-medium), read 15 Nov 2026, for the version), each model at its highest listed effort ([Artificial Analysis, *LLM Leaderboard*](https://artificialanalysis.ai/leaderboards/models?status=all), read 15 Nov 2026):

| Model (effort) | API price, input / output per million tokens (vendor page, read 15 Nov 2026) | Index score | Cost per task |
|---|---|---|---|
| Claude Fable 5.2 (max) | $8 / $40 | 65 | $26.54 |
| Claude Opus 5.5 (max) | $4 / $20 | 59 | $10.04 |
| Claude Sonnet 5.5 (max) | $2 / $10 | 55 | $10.02 |
| GPT-6 Astra (max) | $10 / $50 | 57 | $6.24 |
| GPT-6.1 Sol (max) | $2 / $10 | 55 | $1.27 |
| GPT-6.1 Terra (max) | $1 / $5 | 51 | $0.96 |
| Claude Haiku 5.5 (max) | from $0.10 / from $0.50 | 36 | $0.41 |
| GPT-6 Luna (max) | $0.10 / $0.50 | 28 | $0.15 |

Claude prices from [*Models overview*](https://platform.claude.com/docs/en/models/overview); OpenAI prices from [OpenAI, *Pricing*](https://developers.openai.com/api/docs/pricing), standard tier; both read 15 Nov 2026. Gemini models appear on the leaderboard at high effort (Gemini 4 Carbon 60 at $5.48, Gemini 4 Argon 50 at $4.97); their current API prices could not be read on Google's pricing page that day, so they are left out of the table.

Three readings, all arithmetic on the table (grade: measured, by a third party, on its tasks):

1. **Same token price, different task price.** Sonnet 5.5 and GPT-6.1 Sol both cost $2 and $10 per million tokens and both score 55 at max. Sonnet's task costs $10.02, Sol's $1.27: 7.9 times as much for the same score. The difference is tokens spent per task.
2. **A cheaper token can make a dearer task.** GPT-6 Astra's tokens cost more than Fable 5.2's ($10 / $50 against $8 / $40), and its task costs less ($6.24 against $26.54). Fable 5.2 scores 8 points higher.
3. **Price ratios understate the gap at the top.** Fable 5.2's tokens cost twice Opus 5.5's; its task at max costs 2.6 times as much.

A Claude Code engineer says the same in practice terms: larger models cost more per token, yet on tasks that stretch a smaller model the total cost per task can come out lower, and some tasks a smaller model cannot finish at any effort (Lydia Hallie, [*Choosing a Claude model and effort level in Claude Code*](https://www.claude.com/blog/claude-model-and-effort-level-in-claude-code), Claude blog, 7 Jul 2026; grade: documented practice). Anthropic's own launch figures point the same way and are vendor data: at default (medium) effort, Opus 5.5 beat Opus 5 at max effort on Terminal-Bench 4.0 for about a fifth of the cost, and beat GPT-6 Astra at max effort on GDPval-AA for about a fifth of the cost per task ([Anthropic, *Introducing Claude Opus 5.5*](https://anthropic.com/news/claude-opus-5-5), 22 Sep 2026, read 15 Nov 2026).

The comparison below draws the cost-per-task column.

```viz
{
  "kind": "compare",
  "title": "Cost per Intelligence Index task, USD, at the highest listed effort",
  "max": 28,
  "decimals": 2,
  "rows": [
    {"label": "Claude Fable 5.2 (max)", "value": 26.54, "display": "$26.54 · index 65", "tone": 1},
    {"label": "Claude Opus 5.5 (max)", "value": 10.04, "display": "$10.04 · index 59", "tone": 2},
    {"label": "Claude Sonnet 5.5 (max)", "value": 10.02, "display": "$10.02 · index 55", "tone": 3},
    {"label": "GPT-6 Astra (max)", "value": 6.24, "display": "$6.24 · index 57", "tone": 5},
    {"label": "GPT-6.1 Sol (max)", "value": 1.27, "display": "$1.27 · index 55", "tone": 5},
    {"label": "GPT-6.1 Terra (max)", "value": 0.96, "display": "$0.96 · index 51", "tone": 5},
    {"label": "Claude Haiku 5.5 (max)", "value": 0.41, "display": "$0.41 · index 36", "tone": 4},
    {"label": "GPT-6 Luna (max)", "value": 0.15, "display": "$0.15 · index 28", "tone": 5}
  ],
  "caption": "Weighted cost per task and Intelligence Index score at each model's highest listed effort, from the table in §1 of this unit: Artificial Analysis, LLM Leaderboard, Intelligence Index v5.0.1, read 15 Nov 2026 (third-party benchmark). Sonnet 5.5 and GPT-6.1 Sol have the same token prices and the same score."
}
```

None of these tasks is your task. What transfers is the mechanism: the bill is set by tokens spent per finished job, and the model and the effort setting both move that number. One cost no table holds is your own time. A cheap output that needs a second run, or an error you have to find, is paid in hours, and nothing measured that for the reader of this unit. The routing table at the end handles it with override triggers.

**The case.** Academy (Academy case), a library of self-study courses built by one person with Claude in October and November 2026, is this course's running example; it is one project, an anecdote, never evidence about AI tools in general. Its record holds no measure of hours or money spent per unit (Academy case file §9). So the case cannot say what any of its tasks cost; this unit's routing of it rests on the evidence above, and the deliverable says where the case file records a model and where it does not.

## 2 · The tiers outlive the lineup

Each of the three vendors this course follows sells a ladder of models, and the ladders line up by price. On 15 November 2026:

| Tier (this unit's grouping) | Anthropic | OpenAI | Google |
|---|---|---|---|
| Small and fast | Haiku 5.5: from $0.10 / from $0.50 | GPT-6 Luna: $0.10 / $0.50 | Gemini 3.5 Flash-Lite: $0.30 / $2.50 |
| Mid | Sonnet 5.5: $2 / $10 | GPT-6.1 Sol: $2 / $10; GPT-6.1 Terra: $1 / $5 | Gemini 3.8 Flash: $0.75 / $3.75 to 31 Dec 2026, then $1.50 / $7.50 |
| Large | Opus 5.5: $4 / $20; Fable 5.2: $8 / $40 | GPT-6 Astra: $10 / $50 | Gemini 4 Argon (price not read) |

Prices in USD per million input and output tokens, standard API tier, from [Anthropic, *Models overview*](https://platform.claude.com/docs/en/models/overview), [OpenAI, *Pricing*](https://developers.openai.com/api/docs/pricing), and Google's [Gemini API pricing page](https://ai.google.dev/pricing), all read 15 Nov 2026. Google's page carried output prices "including thinking tokens" for both Flash models and did not list Gemini 4 Argon in the copy read; Google's [*Gemini 4 Argon*](https://ai.google.dev/gemini-api/docs/models/gemini-4-argon) model page (last updated 30 Oct 2026) calls it the flagship reasoning model and gives no price.

What each vendor says the rungs are for (vendor statements):

- **Anthropic** describes Haiku 5.5 as for high-volume, latency-sensitive tasks such as classification, extraction and routing; Sonnet 5.5 as the best combination of speed and intelligence; Opus 5.5 as for long-running agentic coding and knowledge work; and Fable 5.2 as for demanding reasoning and long-horizon agentic work. It advises starting with Opus 5.5 when unsure and moving to Fable 5.2 for demanding reasoning and long-horizon agentic work, or when evals on Opus 5.5 at higher effort still fall short ([*Models overview*](https://platform.claude.com/docs/en/models/overview), read 15 Nov 2026). Its Haiku 5.5 launch lists summaries, compactions, database queries and classification, subagent work on coding tasks alongside Opus 5.5 and Sonnet 5.5, and speed-sensitive work such as live customer support, and says Sonnet 5.5 and Opus 5.5 remain better choices for complex agentic coding ([Anthropic, *Introducing Claude Haiku 5.5*](https://anthropic.com/claude-haiku-5-5), 7 Oct 2026, read 15 Nov 2026).
- **OpenAI**'s reasoning guide says, for cost, to consider a smaller model: start with its largest and try a mid model for lower cost or its smallest for the lowest cost and latency ([OpenAI, *Reasoning models*](https://developers.openai.com/api/docs/guides/reasoning.md), read 15 Nov 2026). The guide names those models gpt-5.6-terra and gpt-5.6-luna, while the pricing page lists gpt-6.1-terra and gpt-6-luna: on the day, OpenAI's own pages did not agree on the names.
- **Google** sets Gemini 4 Argon as its flagship reasoning model for complex software engineering, deep maths and science and autonomous multi-step agents ([*Gemini 4 Argon*](https://ai.google.dev/gemini-api/docs/models/gemini-4-argon), read 15 Nov 2026).

Three things make the ladder a better unit of decision than any model name.

1. **Names change; rungs stay.** On 15 November 2026 Anthropic's lineup lists Fable 5.2 at the top at $8 / $40, with Fable 5.1, at $10 / $50, moved to the list of all models ([*Models overview*](https://platform.claude.com/docs/en/models/overview)); Anthropic's page on the new model says its input and output cost less than Fable 5.1's ([Anthropic, *What's new in Claude Fable 5.2*](https://platform.claude.com/docs/en/models/fable-5-2/whats-new-fable-5-2), read 15 Nov 2026). A routing rule written as "large tier, high effort" survives that change; one written as "Fable 5.1" does not. In Academy, a session's model named "fable" resolved to a newer version than the method names, and the checks it ran were recorded as owed again on the named version (Academy case file §7): the name moved under the rule.
2. **The rungs are priced alike across vendors.** Haiku 5.5 and GPT-6 Luna cost the same per token, as do Sonnet 5.5 and GPT-6.1 Sol (the tables above). The cost per task does not line up the same way (§1), which is why each rung needs its own evidence.
3. **Anthropic now sells two large rungs.** Opus 5.5 and Fable 5.2 are both large, and the vendor's own advice is to start on the cheaper one. The brief of this course names three tiers; on Anthropic's lineup the top tier has a step inside it.

**Where the tier pattern holds less well.** The routing evidence (§4) shows a small model is often enough, and the measured data (§1) shows a mid model at max effort costing as much per task as a large one. A tier is a starting point for a task. The override triggers in the deliverable move a task up or down.

## 3 · What effort and thinking settings do

Every vendor in this unit now sells two dials: which model, and how hard it works. This section is from the vendors' documentation (grade: documented practice) and one benchmark.

**Claude.** Anthropic's documentation says effort controls how many tokens Claude uses when responding, and states: "Effort is a behavioral signal, not a strict token budget." At lower levels Claude still thinks on hard problems, but less, and it can skip thinking entirely on simple ones. Effort applies to every output token: the text, the tool calls and the thinking. Lower effort makes fewer tool calls and terser confirmations; higher effort may make more calls and explain its plan. The levels are low, medium, high, xhigh and max; xhigh is described as for long-running agentic and coding tasks of over 30 minutes, max as capability with no constraint on token spending ([Anthropic, *Effort*](https://platform.claude.com/docs/en/build-with-claude/effort), read 15 Nov 2026).

Defaults differ by model, and the differences matter when a model is swapped (same page, read 15 Nov 2026):

- Opus 5.5 and Haiku 5.5 default to medium; Fable 5.2 and Sonnet 5.5 to high on the API.
- Opus 5 and earlier Opus models defaulted to high, so the same request with no effort set runs one level lower on Opus 5.5.
- On Opus 5.5, thinking is always on and cannot be turned off; effort is the lever.
- Per model: for Fable 5.2, start at high, where most of the capability gain already is, and keep max for measuring the ceiling; for Sonnet 5.5, start at high unless the work is agentic or latency-sensitive, at medium for well-specified agentic coding, and at medium or low for chat; for Haiku 5.5, use low for chat, short tool tasks and simple high-volume requests, high for knowledge work, longer agent tasks and strict instruction following. At low, the page warns, Haiku in a long agent prompt is more likely to skip a search, stop early or skip a check.

On claude.ai the effort setting is inside the model menu next to the send button. The help centre describes low and medium as suiting routine tasks and stretching usage further, high as the best overall balance of quality and speed, extra high as for long-running coding and agentic tasks (Opus 4.7 and newer), and max as the most thorough; higher effort uses more tokens and reaches usage limits sooner. On Fable 5.2, Haiku 5.5, Sonnet 5.5, Opus 5.5, Fable 5.1 and Opus 5, thinking cannot be turned off in the app; to reduce it, lower the effort. The menu marks each model's default without the article listing them ([Claude Help Center, *Change the model, effort, and thinking settings*](https://support.claude.com/en/articles/8664678-change-the-model-effort-and-thinking-settings), read 15 Nov 2026).

**OpenAI and Google.** OpenAI's effort values depend on the model and can run from none through max; GPT-6.1 Sol defaults to medium and supports neither none nor minimal. Lower effort favours speed and fewer tokens, higher effort reasons more completely, and the guide advises starting at medium, evaluating medium against high before using high or xhigh, and treating effort as a tuning knob, since clear prompts and explicit output contracts matter more ([OpenAI, *Reasoning models*](https://developers.openai.com/api/docs/guides/reasoning.md), read 15 Nov 2026). Google's Gemini 4 Argon takes low, medium and high thinking levels, defaults to medium and cannot have thinking turned off; Google's page assigns little or no thinking to fact retrieval and classification and a high level to complex maths and coding, and says to lower the level to cut cost or latency ([*Gemini thinking*](https://ai.google.dev/gemini-api/docs/generate-content/thinking?authuser=1), read 15 Nov 2026).

**What a step of effort buys, measured.** Artificial Analysis reports Opus 5.5 and Sonnet 5.5 at each effort level, with the index score and the time per task; on 15 November it gave a cost per task only at max (index v5.0.1; third-party benchmark):

| Effort | Opus 5.5: index · minutes per task | Sonnet 5.5: index · minutes per task |
|---|---|---|
| low | 35 · 3.1 | 26 · 2.6 |
| medium | 48 · 6.9 | 31 · 4.1 |
| high | 52 · 9.4 | 42 · 6.9 |
| xhigh | 57 · 15.8 | 50 · 14.5 |
| max | 59 · 25.4 | 55 · 33.3 |

Sources: [*Claude Opus 5.5: Intelligence, Performance & Price Analysis*](https://artificialanalysis.ai/models/claude-opus-5-5-medium) and [*Claude Sonnet 5.5: Intelligence, Performance & Price Analysis*](https://artificialanalysis.ai/models/claude-sonnet-5-5-low), both read 15 Nov 2026.

Readings, arithmetic on the table:

- On Opus 5.5, low to medium buys 13 points for 2.2 times the time; medium to high 4 points for 36% more; high to xhigh 5 points for 1.7 times; xhigh to max 2 points for 1.6 times.
- Sonnet 5.5 at high and Opus 5.5 at medium take the same 6.9 minutes a task; Opus scores 6 points higher.
- Fable 5.2 at its lowest level scores 54, above Opus 5.5 at high (52), on the same site's Fable page ([*Claude Fable 5.2: Intelligence, Performance & Price Analysis*](https://artificialanalysis.ai/models/claude-fable-5-2-xhigh), read 15 Nov 2026), which gave no cost per task below max.

Time per task is not cost. Opus 5.5's output speed on that page is 104 to 114 tokens a second at every level, so the longer times suggest more tokens spent; that reading is this unit's inference, and the page does not state it.

```viz
{
  "kind": "scatter",
  "title": "Index score against minutes per task, by effort",
  "x": {"label": "Minutes per task", "min": 0, "max": 35, "ticks": [0, 5, 10, 15, 20, 25, 30, 35]},
  "y": {"label": "Index score", "min": 20, "max": 60, "ticks": [20, 30, 40, 50, 60]},
  "points": [
    {"label": "Opus low", "x": 3.1, "y": 35, "tone": 2},
    {"label": "Opus medium", "x": 6.9, "y": 48, "tone": 2},
    {"label": "Opus high", "x": 9.4, "y": 52, "tone": 2},
    {"label": "Opus xhigh", "x": 15.8, "y": 57, "tone": 2},
    {"label": "Opus max", "x": 25.4, "y": 59, "tone": 2},
    {"label": "Sonnet low", "x": 2.6, "y": 26, "tone": 3},
    {"label": "Sonnet medium", "x": 4.1, "y": 31, "tone": 3},
    {"label": "Sonnet high", "x": 6.9, "y": 42, "tone": 3},
    {"label": "Sonnet xhigh", "x": 14.5, "y": 50, "tone": 3},
    {"label": "Sonnet max", "x": 33.3, "y": 55, "tone": 3}
  ],
  "caption": "Claude Opus 5.5 and Sonnet 5.5 at each effort level: Intelligence Index score against time per task, from the table in §3 of this unit: Artificial Analysis model pages for Claude Opus 5.5 and Claude Sonnet 5.5, Intelligence Index v5.0.1, read 15 Nov 2026 (third-party benchmark). Time is not cost."
}
```

**Extra thinking on easy problems is waste, measured.** Xingyu Chen and colleagues found long reasoning models spending compute on simple problems for little gain, and cut that overhead while keeping performance on GSM8K, MATH500, GPQA and AIME ([Chen et al., *Do NOT Think That Much for 2+3=? On the Overthinking of Long Reasoning Models*, ICML 2025, PMLR 267](https://proceedings.mlr.press/v267/chen25bx.html); the abstract does not name the models). Anthropic's thinking page says the same in product terms: to get less thinking, lower the effort before trying to prompt the model out of it ([*Steering thinking*](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking?r=0)).

**Model or effort: the diagnostic.** Lydia Hallie puts the two dials apart: "The model setting is roughly how capable; the effort setting is roughly how thorough." If Claude had the right context and clearly tried and still failed, choose a larger model; if it skipped a file, did not run tests or did not double-check, raise effort. She frames this as a starting heuristic, and recommends the model's default effort for most tasks, treating effort as a standing preference more than a per-task choice ([Hallie, Claude blog, 7 Jul 2026](https://www.claude.com/blog/claude-model-and-effort-level-in-claude-code); grade: documented practice, written before the 5.5 models).

**Keep effort fixed inside one piece of work.** On the API, changing the top-level effort between requests can invalidate all or part of the prompt cache; models that support per-message effort keep it ([*Effort*](https://platform.claude.com/docs/en/build-with-claude/effort), read 15 Nov 2026). The claude.ai help article says changes apply from the next response and says nothing about caching ([*Change the model, effort, and thinking settings*](https://support.claude.com/en/articles/8664678-change-the-model-effort-and-thinking-settings)). Setting both dials before the first message costs nothing and avoids the question.

## 4 · Where quality differences show, and where they do not

### Read a benchmark by who ran it, which version and when

Every benchmark number in this unit comes with three facts attached, and each of them changes what the number means.

- **Who ran it.** A vendor's launch table is the vendor running its model against rivals it chose, under settings it chose. Anthropic's Opus 5.5 table runs Opus 5.5 at max effort except on Terminal-Bench 4.0, where it was run at xhigh; tasks its safeguards stopped were finished by older models, which Anthropic says likely lowers the scores; one test (AutomationBench) was run by Zapier; and the same page gives Opus 5.5 57.8% on CursorBench 4.0 in the table and 52.5% at default effort in the text ([*Introducing Claude Opus 5.5*](https://anthropic.com/news/claude-opus-5-5), read 15 Nov 2026). Each of those is stated on the page; none of them is in the headline numbers.
- **Which version.** Artificial Analysis moved to Intelligence Index v5 on 27 October 2026: it dropped GDPval-AA, SciCode and AA-LCR, added a private coding test and a set of terminal-based science tasks, and now rests about 60% of the index on private test sets or held-out answers ([Artificial Analysis, *Announcing Artificial Analysis Intelligence Index v5*](https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v5), 27 Oct 2026, read 15 Nov 2026). On 15 November its pages show v5.0.1. A score under v4 and a score under v5 measure different tasks.
- **When.** The index above changed version on 27 October 2026, so a leaderboard read before that day and one read after it rank models on different tasks. In Academy's second audit (anecdote), ten claims in one unit were stale, all from one cause: an independent benchmark published a new index version the day before the unit read its leaderboard (Academy case file §4).

A benchmark that the vendor ran, on a version that has since changed, on a date you do not know, is a claim about someone else's tasks under someone else's settings. Use it to rank options, never to predict your own result.

### Where the differences show

**Small against mid, on long or open work.** Anthropic's Haiku 5.5 launch sets Haiku 5.5 beside Sonnet 5.5 as a reference: GDPval-AA v2.1, a knowledge-work test, 1620 against 1840; Terminal-Bench 4.0, long agentic terminal tasks, 39.2% against 70.6%; Humanity's Last Exam with tools 57.4% against 64.5% ([*Introducing Claude Haiku 5.5*](https://anthropic.com/claude-haiku-5-5), read 15 Nov 2026; vendor). The gap is widest on the long agentic task. On the third-party index at max effort, Haiku 5.5 scores 36 against Sonnet 5.5's 55 (§1).

**Effort, at the bottom of the range.** On Opus 5.5, low to medium is the largest step on the third-party index, 35 to 48 (§3). On Sonnet 5.5, medium to high is 31 to 42.

**The top tier, on hard reasoning.** On the third-party index, Fable 5.2 at max scores 65 against Opus 5.5's 59, at 2.6 times the cost per task (§1).

### Where they shrink

**Large against larger, on the vendor's own table.** Anthropic's Opus 5.5 table scores Opus 5.5 above Fable 5.1 on all nine tests listed, among them GDPval-AA v2.1 (1846 against 1735), Humanity's Last Exam with tools (67.7% against 65.6%), OSWorld 2.1 (81.8% against 80.7%, both marked partial) and Chartography with tools (89.0% against 88.4%). The same page says Opus 5.5 performs at the level of Fable 5.1 on most work, and that the gap is narrower in practice than the scores suggest ([*Introducing Claude Opus 5.5*](https://anthropic.com/news/claude-opus-5-5), read 15 Nov 2026; vendor). That table compares Opus 5.5 with Fable 5.1; Fable 5.2, now on sale, is not in it.

**Mid against large, on knowledge work.** GDPval-AA v2.1 gives Opus 5.5 1846 on Anthropic's Opus page and Sonnet 5.5 1840 on its Haiku page (both read 15 Nov 2026; vendor). The two figures come from two pages and their settings are not stated side by side, so read them as close and leave the order open.

**Mid against large, on agentic coding.** Terminal-Bench 4.0 gives Sonnet 5.5 70.6% in the Haiku page's reference column and Opus 5.5 66.4%, run at xhigh, on the Opus page (both read 15 Nov 2026; vendor). Again two pages, two sets of settings; on this evidence the mid model is not behind on that test.

**Routing studies: a large share of requests does not need the large model.** Lingjiao Chen, Matei Zaharia and James Zou found that API fees could differ by two orders of magnitude, and that a cascade which learns which model to call for each request matched the best single model (GPT-4) with up to 98% lower cost ([Chen, Zaharia and Zou, *FrugalGPT*, arXiv 2305.05176](https://arxiv.org/abs/2305.05176v1), 2023; published in [*Transactions on Machine Learning Research*, 2024](https://mlanthology.org/tmlr/2024/chen2024tmlr-frugalgpt); measured, on 2023 models). Isaac Ong and colleagues trained routers that send each query to a strong model (GPT-4) or a weak one (Mixtral 8x7B), and on MMLU, MT Bench and GSM8K cut costs by more than half without loss of response quality ([Ong et al., *RouteLLM: Learning to Route LLMs from Preference Data*, ICLR 2025](https://proceedings.iclr.cc/paper_files/paper/2025/hash/5503a7c69d48a2f86fc00b3dc09de686-Abstract-Conference.html); models from the [arXiv version](https://arxiv.org/html/2406.18665v3); measured). The saving in both comes from identifying the requests the cheap model already answers well.

**Compute against size.** Charlie Snell and colleagues found that on maths reasoning problems where a smaller model already had a somewhat non-trivial success rate, in a FLOPs-matched comparison, spending more inference compute on it outperformed a model 14 times larger ([Snell, Lee, Xu and Kumar, ICLR 2025](https://proceedings.iclr.cc/paper_files/paper/2025/hash/1b623663fd9b874366f3ce019fdfdd44-Abstract-Conference.html); preprint at [arXiv 2408.03314](https://arxiv.org/abs/2408.03314); measured; the abstract does not name the model). The study varied the compute a model spends at answer time, which is not the same control as a vendor's effort setting; reading it as evidence that a higher effort setting can stand in for a larger model, on tasks within the small model's reach and only there, is this unit's inference.

### What follows (stated opinion, built on the evidence above)

A small model is right when the task is fully specified by its input, a correct output can be recognised at a glance, volume or speed matters, and an error is cheap to catch: triage, reformatting, extraction to a fixed schema, short tool calls. Each condition traces to a source above: Anthropic's positioning of Haiku, the routing studies, and Haiku's gap on long agentic work. It is the wrong model when the task is long, multi-step or open, or when a mistake hides well, such as a plausible wrong figure in a long text. The large tier earns its price on long, open, searched work and on judgement, and the top rung is the vendor's own second step, after Opus at higher effort has fallen short. One exception cuts across tiers: where a task is arithmetic over numbers, have the model write code and let the code produce the numbers, because the same input can give a model different outputs (BW1 §5) and a script gives the same output every time.

## 5 · Self-preference, and why the check runs elsewhere

On the evidence below, a model asked to grade its own work grades it too kindly. Three findings bear on this.

- **Self-enhancement.** Lianmin Zheng and colleagues found strong model judges, GPT-4 among them, agreeing with human preferences over 80% of the time, about the rate at which humans agree with each other, and named three biases in model judges: position, verbosity and self-enhancement ([Zheng et al., *Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena*, NeurIPS 2023 Datasets and Benchmarks Track](https://arxiv.org/abs/2306.05685); measured, on 2023 models).
- **Self-recognition drives it.** Arjun Panickssery, Samuel Bowman and Shi Feng found that models such as GPT-4 and Llama 2 can tell their own outputs from other models' and humans' with non-trivial accuracy, and, by fine-tuning, a linear correlation between how well a model recognises its own text and how strongly it prefers it, with controlled experiments pointing to a causal link ([Panickssery, Bowman and Feng, *LLM Evaluators Recognize and Favor Their Own Generations*, NeurIPS 2024](https://papers.nips.cc/paper_files/paper/2024/hash/7f1f0218e45f5414c79c0679633e47bc-Abstract-Conference.html); measured).
- **Checking itself without outside input does not reliably help.** Jie Huang and colleagues found that on reasoning tasks (GSM8K, CommonSenseQA, HotpotQA) GPT-3.5-Turbo and GPT-4 struggled to correct their own answers without external feedback, and that performance sometimes fell after self-correction ([Huang et al., *Large Language Models Cannot Self-Correct Reasoning Yet*, ICLR 2024](https://arxiv.org/abs/2310.01798); models from the [arXiv HTML version](https://arxiv.org/html/2310.01798v1); measured).

What each kind of separation removes, by this unit's reasoning on those findings:

| Check run by | Removes the writer's conversation from the window | Removes self-recognition | Evidence |
|---|---|---|---|
| The same chat, asked to review | No | No | Huang et al.: no reliable gain without outside feedback |
| The same model in a fresh context | Yes | No | Inference from BW1 §1 (the window) and Panickssery et al. |
| A different model in a fresh context | Yes | Yes, as far as the studies tested other makers' models | Panickssery et al.; Zheng et al. |

Two limits. None of these studies tested a sibling model from the same vendor, such as one Claude model checking another; whether self-preference carries across siblings is untested in the sources cited. And all of them tested models of 2023 and 2024; carrying them to current models is this unit's inference.

**The case** (anecdote). Academy's method has one model write (Opus 5.5) and a different model audit (Fable 5.1) (Academy case file §2). Its fresh checks before filing were run by three models: Fable 5.1 checked 19 drafts, Opus 5.5 checked 12, Fable 5.2 checked 5; the checkers found at least one error in 15, 8 and 5 of them respectively, and 58 errors in all (counts from the table in Academy case file §5). So a checker of the model the method names as its writer (case file §2; case file §5 records Opus 5.5 as the writer of all 36 drafts), in a fresh context, still found errors in two thirds of the drafts it read. The units, courses and dates differ between the three groups and there is no control (case file §9), so the counts compare nothing; they show only that a fresh context of the writer's own model was not a blind spot in this project.

```viz
{
  "kind": "bars",
  "mode": "grouped",
  "series": [
    {"name": "Drafts checked", "tone": 4},
    {"name": "Drafts with at least one error", "tone": 1}
  ],
  "rows": [
    {"label": "Checked by Fable 5.1", "values": [19, 15]},
    {"label": "Checked by Opus 5.5", "values": [12, 8]},
    {"label": "Checked by Fable 5.2", "values": [5, 5]}
  ],
  "caption": "Academy (anecdote): fresh checks before filing, by checker model, and how many drafts had at least one error, counted from the table in Academy case file §5 (§5 of this unit). The method names Opus 5.5 as the writer (case file §2), and case file §5 records it as the writer of every draft. Different units and dates, no control: the groups are not comparable."
}
```

The rule this course uses (stated opinion, on the findings above): the writer never checks its own text in the same conversation; a check runs in a fresh context at the least, by a different model where the stakes justify the cost, and the report records which model checked. How to check by sample, and what a clean sample proves, is BW6.

## 6 · A subscription against the API

**What a subscription buys (Anthropic, read 15 Nov 2026).** Anthropic's pricing page lists Pro at $20 a month billed monthly or $17 a month billed annually ($200 up front); Max at $100 a month for 5 times Pro's usage every five hours and every week; and Ultra at $200 a month for 10 times Pro's weekly usage, with no five-hour limit for verified accounts. On Fable models, Pro pays with usage credits; Max and Ultra include them up to 50% of the weekly limit ([Claude, *Pricing*](https://claude.com/max), read 15 Nov 2026). A second copy of the same page, read the same day, listed Max at 5x or 20x Pro's usage and no Ultra ([Claude, *Pricing*](https://claude.com/pricing?hsLang=en), read 15 Nov 2026), and the help article on Max prices still lists Max 20x at $200 ([Claude Help Center, *How much does the Max plan cost?*](https://support.claude.com/en/articles/11049744-how-much-does-the-max-plan-cost), read 15 Nov 2026). Anthropic's help article on Ultra, read the same day, says the Max 20x plan is now called the Ultra plan ([Claude Help Center, *What is the Ultra plan?*](https://support.claude.com/en/articles/17728952), read 15 Nov 2026), so the second copy and the Max price article are out of date; check the plan page on the day you buy.

**How usage is metered.** Every plan except Ultra on a verified account has a session limit that resets five hours after your first message ([*What is the Ultra plan?*](https://support.claude.com/en/articles/17728952)), and paid plans have weekly limits across all models, with a separate weekly limit for Fable on some plans. What you use depends on conversation length and complexity, features, the model and the effort level; claude.ai, Claude Code and Claude Desktop count toward the same limit ([Claude Help Center, *How do usage and length limits work?*](https://support.claude.com/en/articles/11647753-how-do-usage-and-length-limits-work), read 15 Nov 2026). Anthropic's list of what draws usage down names message length, attachment size, conversation length, tools such as Research and web search, model choice, effort level, artifacts and multi-step tasks, and says project content is cached and counts less when reused ([Claude Help Center, *Usage limit best practices*](https://support.claude.com/en/articles/9797557-usage-limit-best-practices), read 15 Nov 2026). On plans where Fable counts toward weekly limits, it draws from them faster than other Claude models ([Claude Help Center, *Claude Fable models on your plan*](https://support.claude.com/en/articles/15424964-claude-fable-models-on-your-plan), read 15 Nov 2026).

**What Anthropic does not publish.** None of these pages gives a rate per model: how much of a five-hour or weekly allowance one Opus turn uses against one Sonnet or Haiku turn. Inside a plan you pay in a share of an allowance, at an exchange rate that is not stated.

**Where the two meet.** Past your limits, usage credits keep you working at standard API rates, billed separately and bought in advance, on Pro, Max and Ultra ([Claude Help Center, *Manage usage credits for paid Claude plans*](https://support.claude.com/en/articles/12429409-manage-usage-credits-for-paid-claude-plans), read 15 Nov 2026). On Pro, every Fable run is on credits. So the API price list is the one published price that applies to a subscriber, at the margin.

**What the API adds.** You pay per token at the prices in the appendix, with no five-hour window. The Batch API halves input and output prices for work that can wait, which none of the plan pages read offers; cached input is billed at a fraction of the base rate, as project content counts less on a plan; web search costs $10 per 1,000 searches plus the tokens it adds ([Anthropic, *Pricing*](https://platform.claude.com/docs/en/about-claude/pricing?), read 15 Nov 2026).

**A sense of scale (arithmetic, illustrative).** Pro's $20 a month buys, at API prices, one million Opus 5.5 output tokens, or about two of Artificial Analysis's index tasks on Opus 5.5 at max effort ($10.04 each, §1). Those tasks are long agentic jobs, larger than most chat turns; the point is only that a monthly fee and a per-task cost are of the same order for heavy work, and far apart for light work.

**When which (stated opinion, on the documented mechanics above).**

- **Subscription** for interactive work: drafting, critique, research you read as it runs, work whose volume varies by week. The fee caps what you spend, and the limits cap what you can do.
- **API** for work that repeats at volume or runs without you (a batch of extractions, a scheduled check), for work you need to cost per task, and for anything that can wait for the batch discount. You need to write or run a small script, or use a tool that calls the API for you.
- **Both**, with credits switched on, when a subscription carries the daily work and a few heavy runs would otherwise stop at a limit.

Which plan the Academy project runs on is not recorded (Academy case file §7), so the case cannot illustrate this choice. How to keep a project inside its plan's limits, and what to keep out of the tool, is BW10.

## 7 · A rule for re-deciding when the lineup changes

A routing table is a set of dated claims about prices, defaults and capability. Four kinds of change make it wrong without anyone touching it, and each has a dated instance in this unit's sources.

| Change | Instance | Source |
|---|---|---|
| A new model in a tier, at a new price | Fable 5.2 at $8 / $40 beside Fable 5.1 at $10 / $50 | [*Models overview*](https://platform.claude.com/docs/en/models/overview), read 15 Nov 2026 |
| A price with an announced date | Gemini 3.8 Flash from $0.75 / $3.75 to $1.50 / $7.50 on 1 Jan 2027 | [Google, Gemini API pricing page](https://ai.google.dev/pricing), read 15 Nov 2026 |
| A default effort that moved | Opus 5.5 defaults to medium; Opus 5 defaulted to high | [*Effort*](https://platform.claude.com/docs/en/build-with-claude/effort), read 15 Nov 2026 |
| A name that resolves to a newer model, or a benchmark that changes version | Academy's "fable" resolving to a newer version (case file §7); Intelligence Index v5 | Academy case file §4, §7; [*Announcing … v5*](https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v5) |

**The rule** (stated opinion; each step rests on the sources named in it):

1. **Write each row by tier and effort, with the model and the date it was read.** "Large, high; Opus 5.5, read 15 Nov 2026."
2. **Re-decide on an event, and on a date.** The events are the four in the table. The date is six months after the table was written: the interval Academy's method sets for its staleness check of any unit written with live search (Academy case file §2).
3. **On an event, re-read before re-running.** Read the vendor's models page, price page and effort page on the day; if a tier gained a model, read its default effort, since the same request can run at another level on a new model (Opus 5.5, above).
4. **Test the change on your own work.** Keep three past inputs per row whose good output you know. Run them on the new option at the row's effort, check each output the way the row's check says (BW6 for claims against sources), and compare with the old option on what you can see: errors found, reruns needed, and the cost or usage shown. A vendor benchmark ranks the options; your three runs decide. Anthropic's model page frames its own advice the same way, in terms of your evals ([*Models overview*](https://platform.claude.com/docs/en/models/overview)), and OpenAI's guide advises evaluating effort levels against your own evals ([*Reasoning models*](https://developers.openai.com/api/docs/guides/reasoning.md)); grade: documented practice. If the new option is as good on all three inputs when checked, and costs less or uses less of the plan, change the row and log it (step 6); otherwise keep the row and re-date it with the day you re-read the pages (stated opinion).
5. **Pin what can be pinned.** Where a tool lets you name an exact model version, name it in the brief; where it does not, record which version ran (BW1 §5).
6. **Change one row at a time, and log it**: the row, from, to, the trigger, the date.

```viz
{
  "kind": "decision",
  "root": {
    "q": "Did a model, price, default or benchmark version change, or is the row six months old?",
    "tone": 4,
    "branches": [
      {"label": "no", "to": {"outcome": "Keep the row", "tone": 3}},
      {"label": "yes", "to": {
        "q": "On three past inputs, at the row's effort, is the new option as good when checked?",
        "tone": 4,
        "branches": [
          {"label": "no", "to": {"outcome": "Keep the row; re-date it", "tone": 3}},
          {"label": "yes", "to": {
            "q": "Does it cost less, or use less of the plan?",
            "tone": 4,
            "branches": [
              {"label": "yes", "to": {"outcome": "Change the row; log it", "tone": 1}},
              {"label": "no", "to": {"outcome": "Keep the row; re-date it", "tone": 3}}
            ]
          }}
        ]
      }}
    ]
  },
  "caption": "The re-deciding rule in §7 of this unit (stated opinion), drawn as a decision; the triggers are the four kinds of change in its table, each with its dated source there."
}
```

## 8 · On other tools

The principles in §1 to §7 (cost per task, a price ladder of tiers, an effort dial, benchmarks read by who ran them and when, a check run outside the writer's context, a fee against a per-token price, a dated rule for re-deciding) hold for any current assistant. The detail is Claude's. Below, each Claude-specific claim, with the equivalent where the other vendor's own documentation was found (all read 15 Nov 2026). ChatGPT's plan page failed to load and was not checked; Google's consumer plan pages were not read for this unit.

| Claim in this unit | Claude | ChatGPT / OpenAI API | Gemini / Google API |
|---|---|---|---|
| Thinking or reasoning is billed as output (§1) | [*Steering thinking*](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking?r=0) | Reasoning tokens billed as output and counted in the window: [*Reasoning models*](https://developers.openai.com/api/docs/guides/reasoning.md) | Output plus thinking tokens; full thoughts billed when a summary is returned: [*Gemini thinking*](https://ai.google.dev/gemini-api/docs/generate-content/thinking?authuser=1) |
| A price ladder of small, mid and large models (§2) | [*Models overview*](https://platform.claude.com/docs/en/models/overview) | [*Pricing*](https://developers.openai.com/api/docs/pricing); smaller models for cost: [*Reasoning models*](https://developers.openai.com/api/docs/guides/reasoning.md) | Flash and Flash-Lite prices: [Gemini API pricing page](https://ai.google.dev/pricing); Argon as flagship: [*Gemini 4 Argon*](https://ai.google.dev/gemini-api/docs/models/gemini-4-argon) |
| Effort levels and per-model defaults (§3) | Five levels; Opus 5.5 and Haiku 5.5 default medium: [*Effort*](https://platform.claude.com/docs/en/build-with-claude/effort) | Model-dependent levels from none to max; GPT-6.1 Sol default medium: [*Reasoning models*](https://developers.openai.com/api/docs/guides/reasoning.md) | thinkingLevel low, medium, high; Argon default medium: [*Gemini thinking*](https://ai.google.dev/gemini-api/docs/generate-content/thinking?authuser=1) |
| Thinking cannot be switched off on the top models (§3) | Opus 5.5 always on: [*Effort*](https://platform.claude.com/docs/en/build-with-claude/effort) | GPT-6.1 Sol supports neither none nor minimal: [*Reasoning models*](https://developers.openai.com/api/docs/guides/reasoning.md) | Gemini 4 Argon cannot disable thinking: [*Gemini thinking*](https://ai.google.dev/gemini-api/docs/generate-content/thinking?authuser=1) |
| Lower the effort before prompting around thinking (§3) | [*Steering thinking*](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking?r=0) | Effort as a tuning knob; prompts and output contracts matter more: [*Reasoning models*](https://developers.openai.com/api/docs/guides/reasoning.md) | Lower the level to cut cost or latency: [*Gemini thinking*](https://ai.google.dev/gemini-api/docs/generate-content/thinking?authuser=1) |
| Batch work at half price (§6) | [*Pricing*](https://platform.claude.com/docs/en/about-claude/pricing?) | The Flex/Batch table lists half the standard prices; the page does not state the discount in words: [*Pricing*](https://developers.openai.com/api/docs/pricing) | Batch API at 50% cost reduction: [Gemini API pricing page](https://ai.google.dev/pricing) |
| Subscription limits, per-model usage rates unpublished (§6) | [*How do usage and length limits work?*](https://support.claude.com/en/articles/11647753-how-do-usage-and-length-limits-work) | Not checked: the plan page failed to load | Not checked for this unit |
| Model-or-effort diagnostic (§3) | [Hallie, Claude blog](https://www.claude.com/blog/claude-model-and-effort-level-in-claude-code) (practice) | No equivalent found in the pages read | Level by task complexity: [*Gemini thinking*](https://ai.google.dev/gemini-api/docs/generate-content/thinking?authuser=1) |

The research in §4 and §5 is not Claude-specific: the studies whose pages name their models tested OpenAI, Meta and Mistral models released in 2023 (GPT-3.5-Turbo, GPT-4, Llama 2, Mixtral 8x7B), and none tested a model current on 15 Nov 2026 from any vendor.

## Appendix · The lineup on 15 November 2026

Read on the vendors' own pages on 15 November 2026. Re-read before relying on any of it.

**Anthropic, current models** ([*Models overview*](https://platform.claude.com/docs/en/models/overview); [*Pricing*](https://platform.claude.com/docs/en/about-claude/pricing?); [*Effort*](https://platform.claude.com/docs/en/build-with-claude/effort))

| Model | API ID | Input / output, USD per million tokens | Cache read | Default effort (API) | Thinking | Window / max output | Anthropic's positioning |
|---|---|---|---|---|---|---|---|
| Fable 5.2 | claude-fable-5-2 | $8 / $40 | $0.20 | high | adaptive, always on | 1M / 128K | demanding reasoning and long-horizon agentic work |
| Opus 5.5 | claude-opus-5-5 | $4 / $20 | $0.20 | medium | adaptive, always on | 1M / 128K | long-running agentic coding and knowledge work |
| Sonnet 5.5 | claude-sonnet-5-5 | $2 / $10 | $0.10 | high | adaptive | 1M / 128K | the best combination of speed and intelligence |
| Haiku 5.5 | claude-haiku-5-5 | $0.10 / $0.50 for prompts up to 100,000 tokens; $0.50 / $2.50 over | $0.01; $0.05 over | medium | adaptive | 1M / 128K | high-volume, latency-sensitive tasks such as classification, extraction and routing |

Rules on the pricing page that change a task's cost: a Haiku 5.5 request whose prompt is over 100,000 tokens, cache reads and writes included, pays the higher prices for the whole request; every other model above bills its full 1M window at one rate; the Batch API takes 50% off input and output; web search is $10 per 1,000 searches plus tokens; Claude 4.7 and later models use a tokenizer that produces about 30% more tokens for the same text; US-only inference costs 1.1 times; fast mode, on Fable 5.2 and Opus 5.5 among others, costs $16 / $80 and $8 / $40 respectively ([*Pricing*](https://platform.claude.com/docs/en/about-claude/pricing?)). All four models have a June 2026 reliable knowledge cutoff ([*Models overview*](https://platform.claude.com/docs/en/models/overview)). Still listed with prices: Fable 5.1 at $10 / $50, Opus 5 at $5 / $25, Sonnet 5 at $2 / $10 (same page). The context window in the claude.ai chat differs from the API's and is in BW1 §1, dated; re-read it on the help centre on the day.

**Anthropic, plans** ([Claude, *Pricing*](https://claude.com/max); [*Claude Fable models on your plan*](https://support.claude.com/en/articles/15424964-claude-fable-models-on-your-plan); [*How do usage and length limits work?*](https://support.claude.com/en/articles/11647753-how-do-usage-and-length-limits-work); [*Manage usage credits for paid Claude plans*](https://support.claude.com/en/articles/12429409-manage-usage-credits-for-paid-claude-plans))

| Plan | Price (USD) | Usage | Fable |
|---|---|---|---|
| Free | $0 | limited | not available |
| Pro | $20 a month, or $17 a month billed annually ($200 up front) | more than Free, every five hours and every week | on usage credits |
| Max | $100 a month | 5x Pro, every five hours and every week | up to 50% of weekly limits |
| Ultra | $200 a month | 10x Pro every week; no five-hour limit for verified accounts | up to 50% of weekly limits |
| Team | standard seat $20 a month billed annually or $25 monthly; premium seat $100 or $125; 2 to 150 seats | not stated on this copy of the page | premium seats up to 50% of weekly limits; standard seats on credits |
| Enterprise | $20 a seat a month billed annually, 20-seat minimum, plus usage at API rates | billed at API rates | included, per the pricing page; the Fable help article sets premium seats on seat-based plans to the Max rules and standard seats to credits |

Limits reset five hours after the first message of a session, except on Ultra for verified accounts; weekly limits apply across all models; claude.ai, Claude Code and Claude Desktop share one limit; usage credits bill overage at standard API rates on Pro, Max and Ultra. Anthropic publishes no per-model usage rate. A second copy of the pricing page, read the same day, showed Max at 5x or 20x and no Ultra; Anthropic's Ultra help article says Max 20x is now called Ultra (§6).

**OpenAI, pointer row.** API standard prices per million tokens: gpt-6-astra $10 / $50, gpt-6.1-sol $2 / $10, gpt-6.1-terra $1 / $5, gpt-6-luna $0.10 / $0.50 ([OpenAI, *Pricing*](https://developers.openai.com/api/docs/pricing)); effort levels and defaults by model ([OpenAI, *Reasoning models*](https://developers.openai.com/api/docs/guides/reasoning.md)). ChatGPT plan prices and limits: not checked (the plan page failed to load).

**Google, pointer row.** Gemini 3.8 Flash $0.75 / $3.75 to 31 December 2026, $1.50 / $7.50 from 1 January 2027; Gemini 3.5 Flash-Lite $0.30 / $2.50; output prices include thinking tokens ([Gemini API pricing page](https://ai.google.dev/pricing)). Gemini 4 Argon: 1,048,576-token window, thinking at low, medium or high, no price on its model page ([*Gemini 4 Argon*](https://ai.google.dev/gemini-api/docs/models/gemini-4-argon), last updated 30 Oct 2026). Gemini consumer plans: not checked.

## Deliverable · A routing table

Two parts. Part 1 is the routing table for ten common project tasks, worked on the Academy case: each task with its tier, its effort, the reason and an override trigger, and a last column saying what the case file records about that task. Where the case file records no model for a task, the row is this unit's routing of it, built from the evidence in §1 to §7; it is not a description of what the project did. Models and defaults are as read on 15 November 2026 (appendix). Part 2 is the template with blank rows. BW7 assigns a model to each stage of a pipeline from this table, and BW10 sets a usage budget per row.

### Part 1 · The routing table, on the Academy case

Tiers: **small** (Haiku 5.5), **mid** (Sonnet 5.5), **large** (Opus 5.5), **large, top rung** (Fable 5.2). "Override" moves one step, once, when its trigger fires; a second firing on the same row in a month re-opens the row (rule 4 below).

| Task | Academy instance | Tier · model, effort | Reason (evidence) | Override trigger | What the case file records |
|---|---|---|---|---|---|
| **1. Triage and reformatting** | Sorting the proposed rows a chat adds to the backlog (case file §2); the case file records no separate triage step, so the instance is this unit's example | Small · Haiku 5.5, low | Fully specified by its input; Anthropic positions Haiku for classification and routing, and its effort page sets low for simple, high-volume requests (§2, §3); routing studies find the cheap model already answers such requests well (§4) | The sort needs a judgement of priority, or a misfiled row would pass unseen: mid, medium | No model recorded for this task |
| **2. Extraction to a table** | The table of fresh-check findings per unit: 36 units, three counts each (case file §5) | Small · Haiku 5.5, high; totals by script | Extraction is Haiku's documented use; high is Anthropic's level for strict instruction following, and at low Haiku is more likely to skip a check (§3); numbers come from code because model outputs vary between runs (§4; BW1 §5) | The extraction needs reading judgement, such as naming the kind of each error: mid, medium. A total that does not add up: recompute by script, never by the model | Totals of 58 errors, 237 should-fix and 303 minor; no model recorded for compiling them. The history courses' curated bibliographies were extracted by Sonnet 5.5 agents, one per unit group (§2) |
| **3. Summary for a named reader** | A fresh check's findings, which a maintainer verifies one by one before applying them (case file §2); a summary of them for the maintainer is this unit's example, not a task the case file records | Mid · Sonnet 5.5, medium | Well-scoped writing from given material; on Anthropic's knowledge-work figures Sonnet sits close to Opus (§4, vendor); low and medium suit routine work on claude.ai (§3) | The summary must weigh several reports or decide what matters most: large, medium | No model recorded for this task |
| **4. A long first draft** | A unit: a long-form report of 2,000 to 6,000 words by guide, sources cited in place, closing deliverable built in full (case file §1); 194 units written by 11 Nov 2026 | Large · Opus 5.5, high | The method's writing model (case file §2); Anthropic positions Opus for long-running knowledge work (§2); on the third-party index, medium to high adds 4 points for 36% more time per task (§3) | The draft skipped a search, a source or a check: xhigh. It had its sources, clearly tried, and its reasoning is still wrong: top rung, high (§3, diagnostic) | Opus 5.5 writes (§2) and wrote all 36 fresh-checked drafts (§5); unit-writing chats of 28 Oct to 2 Nov 2026: 14 of 15 on Opus 5.5, 1 switched (§8); the first history course's 78 reports: 55 by Fable 5.1, 23 by Opus 5.5 (§2); the effort used is recorded in none of 53 chats reviewed (§2, §9) |
| **5. Critique of a draft** | The fresh check: every cited claim against its source and the deliverable against the brief, by a context that has not seen the unit written; it lists findings and never edits (case file §2) | Large, in a fresh context, a model other than the writer's where affordable · Fable 5.2, high | Self-preference and failed self-correction (§5); Anthropic's guidance for Fable 5.2 is to start at high (§3) | Fable is out of budget (on Pro it runs on credits, §6): Opus 5.5, high, in a fresh context, and the report says the checker was the writer's model. A check that finds nothing in a long draft: a second check by another model | Checkers: Fable 5.1 on 19 drafts, Opus 5.5 on 12, Fable 5.2 on 5; 28 of the 36 drafts had at least one error (case file §5) |
| **6. Research with search** | The searched reading behind a unit whose facts change, which the method marks as written with live search (case file §2) | Large · Opus 5.5, medium | Multi-step searched work; Humanity's Last Exam with tools: Opus 5.5 67.7%, Sonnet 5.5 64.5%, Haiku 5.5 57.4% (§4, vendor, two pages); at low effort a model is more likely to skip a search or stop early (§3); search draws usage on any model (§6) | It skipped sources or stopped early: high. A single factual lookup: mid, low | No model recorded for searching apart from writing |
| **7. Deep research** | The research report the first three units of one of the project's courses were written from, produced by research agents across five tracks (case file §3) | Large · Opus 5.5 as lead, xhigh; top rung if Opus at xhigh falls short | Long-horizon multi-agent work, which is what xhigh is for (§3); Anthropic's advice is to start on Opus and move to Fable when Opus at higher effort falls short (§2) | Always, before anything is built on it: sample its claims against their sources (BW6). If its claims feed several units, check before writing them | The agents were Fable 5.1 research agents, on 27 Oct 2026 (§3). Audit 1 failed 23 of 91 claims in the three units written from it, with nothing invented; the pattern was qualifiers the source does not carry (case file §3) |
| **8. A code change** | A change to the scripts that build the site from the repository and draw the figures (case file §1, §6) | Mid · Sonnet 5.5, medium | Anthropic's Sonnet guidance: medium for well-specified agentic coding, high for harder or longer tasks (§3); on Terminal-Bench 4.0 Sonnet 5.5 is not behind Opus 5.5 in Anthropic's figures (§4, vendor); Sonnet or Opus over Haiku for complex agentic coding (§2) | It skipped a test or a file: high. It had full context, tried and failed: large, high | No model recorded for code changes alone; infrastructure chats (build, repository, publishing, method and skill files) of 28 Oct to 2 Nov 2026: 15, of which 5 on Opus 5.5, 8 on Fable 5.1, 2 switched; none of the 53 on Sonnet 5.5 or Haiku 5.5 (§8) |
| **9. An audit against sources** | The sample audit: one claim drawn from every section of each unit, checked against its source; more than one in ten failing sends the unit to a full audit (case file §2) | Large, top rung, a different model from the writer · Fable 5.2, high | A different model removes self-recognition as far as the studies tested (§5); the method's audit model differs from its writer (case file §2); Fable 5.2 has the highest third-party index score (§1); start at high (§3) | Pin the version and record it, since a model name can resolve to a newer model (§2). Out of budget (on Max or Ultra, Fable uses up to half the weekly limit and draws faster, §6): Opus 5.5, high, fresh context, recorded as such | Fable 5.1 audits (§2); Audits 1 and 2 ran on Fable 5.1, the public marketing course's four audits on Fable 5.2 (14–15 Nov 2026), and no audit of the private courses or the UX course after Audit 2 (§4); Audit 2: 28 claims sampled, 96 checked, ten stale from one benchmark version change (§4) |
| **10. A plan or spec** | A course syllabus: a goal in one sentence, three measurable outcomes, eight to twelve core units and two or three deep dives, each with a scope, a deliverable and a brief (case file §2) | Large · Opus 5.5, high | Open-ended judgement with no input that fixes the answer; Anthropic's advice is to start on Opus 5.5 (§2) | The plan fails review on its reasoning, with the needed inputs present: top rung, high | Syllabus design chats of 28 Oct to 2 Nov 2026: 2, both Fable 5.1 (§8); the UX syllabus review on Fable 5.1 (3 Nov 2026), the two public courses created on Fable 5.2 (11–12 Nov 2026), and syllabus chats on Fable from 15 Nov 2026 (§2) |

**Rules for using the table**

1. **Set both dials before the first message** and keep them for that piece of work; on the API an effort change mid-session can invalidate the cache (§3).
2. **Escalate by cause.** Missing context: fix the window (BW1 §9). Skipped steps: raise effort one level. Full context, real attempt, still wrong: one tier up (§3). Grade: documented practice (Hallie) with this unit's first step added.
3. **Never trust one run of anything that will be published or filed.** Its claims are sampled against their sources by a check run outside the writer's context (§5; BW6).
4. **Log every override** (row, from, to, trigger, date). Two firings on one row in a month re-open the row under the rule in §7. The threshold is this unit's stated opinion.
5. **Re-decide on an event and on a date**: a new model in a tier, a price change, a moved default, a name or benchmark version change, or six months, here 15 May 2027 (§7).

*Sources for Part 1:* the evidence is §1 to §7 of this unit, each cell pointing to its section; Academy facts are from Academy case file §1 (unit length, count), §2 (method, models), §3 (Audit 1), §4 (Audit 2), §5 (fresh checks), §6 (figures by script). The case file holds no record of cost per unit or of the plan used (§9; §7 note), or of which model ran triage, summaries or searching apart from writing; it records the models of extraction and syllabus work (§2, §8), of infrastructure chats (§8), of the research agents (§3), of the audits (§4) and of the 36 drafts' writer (§5).

### Part 2 · Template: your routing table

Copy the table, keep the ten task names, and fill each blank; add rows for recurring tasks of your own. Fill the "Read on" column with the date you read the vendor's pages, and leave a row blank until you have three past inputs for it whose good output you know (§7, rule 4). Each blank says what goes in it.

| Task | Your instance | How often | Tier · model, effort | Reason (evidence) | Override trigger | Read on |
|---|---|---|---|---|---|---|
| 1. Triage and reformatting | [*the recurring sort or reformat in your project, with an example input*] | [*times a week or month*] | [*small, mid or large · the model in that tier on your tool, and the effort level*] | [*why this tier: is the output fully set by the input, can you check it at a glance; cite §2 to §4 or your own runs*] | [*what you will see when it fails, and the one step it moves to*] | [*date you read the vendor's model and price pages*] |
| 2. Extraction to a table | [*the documents and the columns you extract*] | [*how many documents, how often*] | [*tier · model, effort; and whether totals come from a script*] | [*why; note whether a wrong cell would be visible*] | [*the error that sends it up a tier, or to a script*] | [*date*] |
| 3. Summary for a named reader | [*the material, and who reads the summary*] | [*how often*] | [*tier · model, effort*] | [*why; how much judgement the summary needs*] | [*the sign the summary misjudged what matters*] | [*date*] |
| 4. A long first draft | [*the document, its length and its sources*] | [*how many, how often*] | [*tier · model, effort*] | [*why; cite §2 to §4*] | [*skipped steps: effort up; wrong with full context: tier up*] | [*date*] |
| 5. Critique of a draft | [*what is checked, against what*] | [*how often*] | [*tier · model, effort; and whether it is a different model from the writer, in a fresh context*] | [*why; cite §5*] | [*what you do when the checker finds nothing, or when the stronger checker is out of budget*] | [*date*] |
| 6. Research with search | [*the questions that need current sources*] | [*how often*] | [*tier · model, effort*] | [*why*] | [*skipped sources: effort up; single lookup: tier down*] | [*date*] |
| 7. Deep research | [*the multi-source report you commission*] | [*how often*] | [*tier · model, effort*] | [*why; and the check every claim gets before use*] | [*the result of that check that makes you rerun or discard*] | [*date*] |
| 8. A code change | [*the script, sheet formula or small tool you change*] | [*how often*] | [*tier · model, effort*] | [*why; cite §3 and §4*] | [*skipped tests: effort up; failed with full context: tier up*] | [*date*] |
| 9. An audit against sources | [*the text audited, and the sampling rule from BW6*] | [*how often*] | [*tier · model, effort; a model other than the writer's*] | [*why; cite §5*] | [*what you do when that model is unavailable, and how you record it*] | [*date*] |
| 10. A plan or spec | [*the plan you write for your project (BW5)*] | [*how often*] | [*tier · model, effort*] | [*why*] | [*the review result that sends it up a tier*] | [*date*] |
| [*a recurring task of your own*] | [*example input*] | [*how often*] | [*tier · model, effort*] | [*why*] | [*trigger*] | [*date*] |

Under the table, keep the five rules above as they are, and one line: **Re-decide by** [*the date six months after the "Read on" dates, and the vendor pages you will re-read on that day*].

## Sources

All web pages read on 15 November 2026. Most vendor documentation and help-centre pages show no exact date; where a page gives one, it is listed.

**Vendor documentation and statements: Anthropic**

- Anthropic. *Models overview*. Claude Platform Docs. https://platform.claude.com/docs/en/models/overview
- Anthropic. *Pricing*. Claude Platform Docs. https://platform.claude.com/docs/en/about-claude/pricing?
- Anthropic. *Effort*. Claude Platform Docs. https://platform.claude.com/docs/en/build-with-claude/effort
- Anthropic. *Steering thinking*. Claude Platform Docs. https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking?r=0
- Anthropic. *What's new in Claude Fable 5.2*. Claude Platform Docs. https://platform.claude.com/docs/en/models/fable-5-2/whats-new-fable-5-2
- Anthropic. *Introducing Claude Opus 5.5*. 22 September 2026. https://anthropic.com/news/claude-opus-5-5
- Anthropic. *Introducing Claude Haiku 5.5*. 7 October 2026. https://anthropic.com/claude-haiku-5-5
- Hallie, L. (Claude Code team, Anthropic). *Choosing a Claude model and effort level in Claude Code*. Claude blog, 7 July 2026 (practice). https://www.claude.com/blog/claude-model-and-effort-level-in-claude-code
- Claude. *Pricing* (plans page). https://claude.com/max
- Claude. *Pricing* (a second copy of the plans page, served the same day with a different plan list). https://claude.com/pricing?hsLang=en
- Claude Help Center. *How much does the Max plan cost?* https://support.claude.com/en/articles/11049744-how-much-does-the-max-plan-cost
- Claude Help Center. *What is the Ultra plan?* https://support.claude.com/en/articles/17728952
- Claude Help Center. *How do usage and length limits work?* https://support.claude.com/en/articles/11647753-how-do-usage-and-length-limits-work
- Claude Help Center. *Usage limit best practices*. https://support.claude.com/en/articles/9797557-usage-limit-best-practices
- Claude Help Center. *Claude Fable models on your plan*. https://support.claude.com/en/articles/15424964-claude-fable-models-on-your-plan
- Claude Help Center. *Manage usage credits for paid Claude plans*. https://support.claude.com/en/articles/12429409-manage-usage-credits-for-paid-claude-plans
- Claude Help Center. *Change the model, effort, and thinking settings*. https://support.claude.com/en/articles/8664678-change-the-model-effort-and-thinking-settings

**Vendor documentation: OpenAI and Google**

- OpenAI. *Pricing*. OpenAI API docs. https://developers.openai.com/api/docs/pricing
- OpenAI. *Reasoning models*. OpenAI API docs. https://developers.openai.com/api/docs/guides/reasoning.md
- Google. Gemini API pricing page, Google AI for Developers, read 15 November 2026 (no headline shown in the copy read). https://ai.google.dev/pricing
- Google. *Gemini thinking*. Gemini API docs, last updated 14 October 2026. https://ai.google.dev/gemini-api/docs/generate-content/thinking?authuser=1
- Google. *Gemini 4 Argon*. Gemini API docs, last updated 30 October 2026. https://ai.google.dev/gemini-api/docs/models/gemini-4-argon

**Independent benchmark (third party)**

- Artificial Analysis. *LLM Leaderboard*. Intelligence Index v5.0.1. https://artificialanalysis.ai/leaderboards/models?status=all
- Artificial Analysis. *Claude Opus 5.5: Intelligence, Performance & Price Analysis*. Intelligence Index v5.0.1. https://artificialanalysis.ai/models/claude-opus-5-5-medium
- Artificial Analysis. *Claude Sonnet 5.5: Intelligence, Performance & Price Analysis*. Intelligence Index v5.0.1. https://artificialanalysis.ai/models/claude-sonnet-5-5-low
- Artificial Analysis. *Claude Fable 5.2: Intelligence, Performance & Price Analysis*. Intelligence Index v5.0.1. https://artificialanalysis.ai/models/claude-fable-5-2-xhigh
- Artificial Analysis. *Artificial Analysis Benchmarking Methodology*. https://artificialanalysis.ai/methodology
- Artificial Analysis. *Announcing Artificial Analysis Intelligence Index v5*. 27 October 2026. https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v5

**Research**

- Chen, L., Zaharia, M. and Zou, J. "FrugalGPT: How to Use Large Language Models While Reducing Cost and Improving Performance". arXiv 2305.05176, 2023; *Transactions on Machine Learning Research*, 2024 (peer-reviewed). https://arxiv.org/abs/2305.05176v1 · https://mlanthology.org/tmlr/2024/chen2024tmlr-frugalgpt
- Ong, I., Almahairi, A., Wu, V., Chiang, W.-L., Wu, T., Gonzalez, J. E., Kadous, M. W. and Stoica, I. "RouteLLM: Learning to Route LLMs from Preference Data". ICLR 2025 (peer-reviewed). https://proceedings.iclr.cc/paper_files/paper/2025/hash/5503a7c69d48a2f86fc00b3dc09de686-Abstract-Conference.html · arXiv version: https://arxiv.org/html/2406.18665v3
- Snell, C., Lee, J., Xu, K. and Kumar, A. "Scaling LLM Test-Time Compute Optimally Can be More Effective than Scaling Parameters for Reasoning". ICLR 2025 (peer-reviewed); preprint as "Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters", arXiv 2408.03314, 2024. https://proceedings.iclr.cc/paper_files/paper/2025/hash/1b623663fd9b874366f3ce019fdfdd44-Abstract-Conference.html · https://arxiv.org/abs/2408.03314
- Chen, X., Xu, J., Liang, T. et al. "Do NOT Think That Much for 2+3=? On the Overthinking of Long Reasoning Models". *Proceedings of the 42nd International Conference on Machine Learning*, PMLR 267, 2025, 9487–9499 (peer-reviewed). https://proceedings.mlr.press/v267/chen25bx.html
- Zheng, L., Chiang, W.-L., Sheng, Y., Zhuang, S. et al. "Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena". NeurIPS 2023 Datasets and Benchmarks Track (peer-reviewed). https://arxiv.org/abs/2306.05685
- Panickssery, A., Bowman, S. R. and Feng, S. "LLM Evaluators Recognize and Favor Their Own Generations". NeurIPS 2024 (peer-reviewed). https://papers.nips.cc/paper_files/paper/2024/hash/7f1f0218e45f5414c79c0679633e47bc-Abstract-Conference.html
- Huang, J., Chen, X., Mishra, S., Zheng, H. S., Yu, A. W., Song, X. and Zhou, D. "Large Language Models Cannot Self-Correct Reasoning Yet". ICLR 2024 (peer-reviewed). https://arxiv.org/abs/2310.01798 · https://arxiv.org/html/2310.01798v1

**The case**

- Academy case file (`generator/data/building-with-ai/case-academy.md`), compiled 11 November 2026; cited by section, §1 to §9.

**This course**

- BW1 · Mental model, §1, §2, §4, §5, §9.

## Unsure list

1. Anthropic's plan line-up: two copies of the Plans & pricing page served on 15 Nov 2026 disagreed (claude.com/max: Max $100 at 5x, Ultra $200 at 10x weekly, no five-hour limit for verified accounts; claude.com/pricing?hsLang=en: Max 5x or 20x, no Ultra), and the Max-price help article still lists Max 20x at $200. The conflict is settled by Anthropic's help article on Ultra (support.claude.com/en/articles/17728952), read 15 Nov 2026, which says the Max 20x plan is now called the Ultra plan; the unit gives the /max copy in the appendix and says so in §6.
2. Thinking page headline: the page at platform.claude.com/docs/en/build-with-claude/adaptive-thinking?r=0 returned the headline "Steering thinking" while its search-result title was "adaptive thinking"; the Sources title follows the fetched headline.
3. Artificial Analysis leaderboard: the fetch did not return the page's headline; the Sources title "LLM Leaderboard" comes from the search result title ("LLM Leaderboard - Comparison of AI models from OpenAI, Anthropic, Google, SpaceXAI & others"). The leaderboard itself showed no index version; v5.0.1 is from the model pages.
4. Artificial Analysis gave a cost per task only at max effort on 15 Nov 2026; time per task is used for the effort steps, and the reading that longer time means more tokens is the unit's inference from a near-constant output speed.
5. Google's Gemini API pricing page (ai.google.dev/pricing) showed no headline and did not list Gemini 4 Argon or Carbon in the copy read; a second pricing URL was refused at fetch. Argon's price is left out. Sources title given as organisation, document type and date.
6. Anthropic's Sonnet 5.5 launch page was refused at fetch; every Sonnet 5.5 benchmark figure in the unit comes from the reference column of the Haiku 5.5 launch page, whose effort settings for Sonnet are stated only for FrontierCode (xhigh).
7. Snell et al.: the ICLR 2025 and arXiv abstracts read do not name the model or the benchmark; the unit says "maths reasoning problems" from the ICLR abstract and does not name the model.
8. FrugalGPT's TMLR 2024 venue rests on the mlanthology.org search result (title and URL), whose page was not fetched; the arXiv abstract was read.
9. Lydia Hallie's post: the fetch summarised her smaller-model advice as "routine work, such as precisely described edits or mechanical changes"; a fresh check of the source unit had removed "precisely described" as not in the post. The unit avoids the phrase; which reading is right was not settled.
10. Academy fresh-check counts by checker model (Fable 5.1: 19 drafts, 15 with an error; Opus 5.5: 12, 8; Fable 5.2: 5, 5) are the unit's count of the case file §5 table; that the writer of every one of those drafts was Opus 5.5 rests on case file §5, which records it from the course index's unit tables (line added 17 Nov 2026).
Object: none

Fresh check 2026-11-15 (claude-opus-5-5): fix · 1 errors, 5 should-fix, 10 minor; all applied; report `audits/building-with-ai/fresh-check-BW2.md`

Correction 17 Nov 2026 (CP-4), found by W-SP1, each change checked by a fresh Opus 5.5 agent against case-academy.md
