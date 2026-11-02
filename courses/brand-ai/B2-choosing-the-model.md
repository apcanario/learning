---
code: B2
title: Choosing the model
course: brand-ai · B · Using AI to Build a Brand
model: Opus 5.5
written: 2026-10-28
search: on
---

# B2 · Choosing the model

Every current fact in this unit (model lineups, prices, plan limits, effort settings, benchmark scores) was checked against its source on 28 October 2026 and carries that date unless another is given. Benchmark figures come from two kinds of source, labelled where they appear. **Vendor** figures are a model maker reporting its own model against rivals it chose. **Third-party** figures come from Artificial Analysis, a benchmarking company that runs the same tests across vendors; its data is treated here as a vendor dataset in the sourcing standard's sense and labelled as such. None of these benchmarks measured any of his tasks. What a token is, why claude.ai gives him a 200K window, and why each turn of a long chat costs more than the last are in B1 (§1, §2); this unit builds on them and does not restate them.

## 1 · The lineup, and what each model is for

Four current Claude models, as Anthropic's model page lists them on 28 October 2026 ([Anthropic, *Models overview*](https://platform.claude.com/docs/en/models/overview)); release dates from each launch page.

| Model | Released | API price, input / output per million tokens | Anthropic's one-line positioning | Relative speed | Default effort on the API |
|---|---|---|---|---|---|
| Fable 5.1 | Sep 2026 | $10 / $50 | "For demanding reasoning and long-horizon agentic work" | Slower | high |
| Opus 5.5 | 22 Sep 2026 | $4 / $20 | "For long-running agentic coding and knowledge work" | Moderate | medium |
| Sonnet 5.5 | 28 Sep 2026 | $2 / $10 | "The best combination of speed and intelligence" | Fast | high |
| Haiku 5.5 | 7 Oct 2026 | $0.10 / $0.50 (prompts up to 100K tokens; qualifier from the Pricing page) | "For high-volume, latency-sensitive tasks such as classification, extraction, and routing" | Fastest | medium |

All four share a 1M-token window on the API, 128K output tokens and a June 2026 knowledge cutoff (same page; B1 §1 covers the 200K window he gets on claude.ai, B1 §4 the cutoff).

What each is for, in Anthropic's own launch material (vendor statements):

- **Opus 5.5** is the first model of the 5.5 family. Anthropic says it performs at about the level of Fable 5.1 on most work, and that lower per-token prices plus fewer tokens per task cut costs by 40% against Opus 5 ([Anthropic, *Introducing Claude Opus 5.5*, 22 Sep 2026](https://www.anthropic.com/claude-opus-5-5)). The model page's own advice is to start with Opus 5.5 when unsure, and to move to Fable 5.1 for demanding reasoning and long-horizon agentic work, or when Opus 5.5 at higher effort still falls short ([Anthropic, *Models overview*](https://platform.claude.com/docs/en/models/overview)).
- **Fable 5.1** is the same underlying model as Mythos 5.1 with stricter safeguards; Mythos 5.1 is limited to vetted organisations in cybersecurity and life sciences. Fable 5.1 still routes exploit generation and life-sciences R&D queries to Opus models, and Anthropic estimates its cost for typical workloads at about 25% below Fable 5 ([Anthropic, *Introducing Claude Fable 5.1 and Claude Mythos 5.1*, Sep 2026](https://www.anthropic.com/claude-fable-and-mythos-5-1)).
- **Sonnet 5.5** is described as a faster, cheaper complement to Opus 5.5 for well-scoped everyday tasks, bug fixing, and polished documents, slides and spreadsheets. Anthropic adds that Opus 5.5 stays clearly stronger on complex, open-ended work, and gives no figure for that claim ([Anthropic, *Introducing Claude Sonnet 5.5*, 28 Sep 2026](https://www.anthropic.com/claude-sonnet-5-5)).
- **Haiku 5.5** is pitched at high-volume, cost-sensitive work: summaries, compactions, database queries, classification, live customer support, browser use, and acting as a subagent beside a larger model ([Anthropic, *Introducing Claude Haiku 5.5*, 7 Oct 2026](https://www.anthropic.com/claude-haiku-5-5)).

The brief's working map (Haiku for triage, Sonnet for drafting, Opus for long-form, Fable for audit) matches Anthropic's positioning for three of the four. The fourth needs a flag now. On the benchmark table Anthropic published with Opus 5.5, Opus 5.5 scores above Fable 5.1 on all nine tests listed, from agentic coding (Terminal-Bench 4.0: 66.4%, Opus at xhigh, against 55.8%) to knowledge work (GDPval-AA v2.1: 1846 against 1735) and reasoning with tools (Humanity's Last Exam: 67.7% against 65.6%) ([Anthropic, *Introducing Claude Opus 5.5*](https://www.anthropic.com/claude-opus-5-5); vendor). The case for Fable as his auditor cannot rest on Fable being the stronger model on those tests. §8 sets out what it can rest on.

## 2 · What his plan measures

claude.ai shows him no prices. It meters him against limits, and Anthropic publishes the rules but almost no rates.

**Plans and prices (USD; the pricing page shows no euro prices).** Pro is $20 a month billed monthly, or $17 a month billed annually ($200 up front). Max is $100 a month for five times Pro's usage per session and $200 for twenty times ([Claude, *Plans & pricing*](https://claude.com/pricing); [Claude Help Center, *About Claude's Max plan usage*](https://support.claude.com/en/articles/11014257-about-claude-s-max-plan-usage)). (On 2 Nov 2026 the $200 tier is Ultra, "10x Pro usage every week", with no five-hour limit for verified accounts: B8 §1.)

**How usage is counted.** The session limit resets every five hours; paid plans also carry weekly limits, and Anthropic reserves the right to add other caps ([Claude Help Center, *About Claude's Pro plan usage*](https://support.claude.com/en/articles/8324991-about-claude-s-pro-plan-usage); [Claude, *Plans & pricing*](https://claude.com/pricing)). Claude Code draws on the same limit as chat (both pages). The only numbers Anthropic gives: about 45 messages per five hours on Pro, defined as about 200 English sentences of 15 to 20 words on a less compute-intensive model; at least 225 on Max 5x and at least 900 on Max 20x for "relatively short" conversations on such a model. The window stays at 200K tokens on every plan ([Max usage](https://support.claude.com/en/articles/11014257-about-claude-s-max-plan-usage); Claude Help Center, usage and length limits). (On 2 Nov 2026 those two articles still say 200K, while the context-window article gives 1M for the current models in chat: B8 §1.)

**What draws it down.** Anthropic's list, dated 22 September 2026: message length, attachment size, current conversation length, tool use (Research, web search), model choice, effort level, artifacts, and multi-step tasks such as running code or browsing. Project content is cached and counts less when reused ([Claude Help Center, *Usage limit best practices*](https://support.claude.com/en/articles/9797557-usage-limit-best-practices)). Higher effort spends more tokens and reaches the limit sooner ([Claude Help Center, *Change the model, effort and extended thinking settings*](https://support.claude.com/en/articles/8664678-change-the-model-effort-and-extended-thinking-settings)).

**How much each model costs him inside the plan is undocumented.** None of these articles gives a per-model rate. The Pro article says only that a less compute-intensive model allows more messages. Fable is the one model with rules of its own (article dated 2 September 2026):

- On Pro, Fable 5.1 sits outside the plan's limits and runs on usage credits.
- On Max, up to half of the weekly limit may go to Fable at no extra cost; this is a cap inside the same pool, and Fable uses the pool faster than other Claude models.
- On Team and seat-based Enterprise, premium seats include Fable; standard seats pay with credits ([Claude Help Center, *Claude Fable models on your plan*](https://support.claude.com/en/articles/15424964-claude-fable-models-on-your-plan)).

Usage credits are prepaid and billed at standard API rates once an included limit is used up ([Claude Help Center, *Manage usage credits for paid Claude plans*](https://support.claude.com/en/articles/12429409-manage-usage-credits-for-paid-claude-plans)). Anthropic also raised five-hour limits on Pro, Max, Team and seat-based Enterprise when Opus 5.5 launched, without saying by how much ([Anthropic, *Introducing Claude Opus 5.5*](https://www.anthropic.com/claude-opus-5-5)).

The consequence for routing: he pays in two currencies. Inside his limits the currency is a share of a five-hour and a weekly allowance, at an exchange rate per model that Anthropic does not publish. Past his limits, and for every Fable run on Pro, the currency is credits at API prices. That second rule is why this unit uses the API price list as the common measure: it is the only published price that applies to him, and, with credits enabled, it is his literal marginal price whenever he runs over.

## 3 · API pricing, per model

From Anthropic's pricing page, 28 October 2026, in USD per million tokens ([Anthropic, *Pricing*](https://platform.claude.com/docs/en/about-claude/pricing)):

| Model | Input | Output | Cache read | Batch input / output |
|---|---|---|---|---|
| Fable 5.1 | $10 | $50 | $0.25 | $5 / $25 |
| Opus 5.5 | $4 | $20 | $0.20 | $2 / $10 |
| Sonnet 5.5 | $2 | $10 | $0.10 | $1 / $5 |
| Haiku 5.5, prompt up to 100K | $0.10 | $0.50 | $0.01 | $0.05 / $0.25 |
| Haiku 5.5, prompt over 100K | $0.50 | $2.50 | $0.05 | $0.25 / $1.25 |

Four rules on the same page change what a task costs:

- **Haiku 5.5 has a cliff at 100K.** A request whose prompt exceeds 100,000 tokens pays five times the per-token rate (arithmetic on the table), and the prompt count includes cache reads and writes. Every other current model bills its full 1M window at one rate.
- **Batch is half price** for every model, for work that can wait.
- **Web search** costs $10 per 1,000 searches plus the tokens the results add.
- **Newer tokenizer.** Claude 4.7 and later models produce about 30% more tokens for the same text; all four current models are in that group (B1 §2).

**Thinking is billed as output.** The tokens Claude spends thinking are charged at the output rate, and in full, even when the app shows only a summary or nothing; thinking blocks kept from earlier turns are billed again as input ([Anthropic, *Steering thinking*](https://platform.claude.com/docs/en/build-with-claude/thinking-steering-and-cost)). The pricing page itself does not mention thinking.

On the price list alone, an output token on Haiku, Sonnet, Opus and Fable costs in the ratio 1 : 20 : 40 : 100 (arithmetic on the table). §5 shows why that ratio misleads.

```viz
{"kind": "compare", "title": "API output price, USD per million tokens", "max": 50,
 "rows": [
  {"label": "Fable 5.1", "value": 50, "display": "$50", "tone": 1},
  {"label": "Opus 5.5", "value": 20, "display": "$20", "tone": 2},
  {"label": "Sonnet 5.5", "value": 10, "display": "$10", "tone": 3},
  {"label": "Haiku 5.5", "value": 0.5, "display": "$0.50 (prompt up to 100K)", "tone": 4}
 ],
 "caption": "The Output column of the table above: list price per million output tokens, the rate thinking tokens are also billed at. <a href=\"https://platform.claude.com/docs/en/about-claude/pricing\">Anthropic, Pricing</a>, read 28 Oct 2026. The 1 : 20 : 40 : 100 ratio; §5 gives the cost per task, which is what matters."}
```

## 4 · The other vendors on the same axes

His Project runs on claude.ai, which runs only Claude models. The other vendors matter to him where he calls a model from his own code, and as a check on whether Anthropic's prices are high or low. This unit compares the other vendors on API price, effort controls and window only; their positioning statements and consumer plan limits were not researched. Per-token prices, 28 October 2026, USD per million tokens unless stated:

| Vendor · model | Input | Output | Notes |
|---|---|---|---|
| OpenAI · GPT-6 Astra | $10.00 | $50.00 | cached input $1.00 |
| OpenAI · GPT-6.1 Sol | $2.00 | $10.00 | |
| OpenAI · GPT-6.1 Terra | $1.00 | $5.00 | |
| OpenAI · GPT-6 Luna | $0.10 | $0.50 | |
| Google · Gemini 4 Argon | $2.00 | $10.00 | to 30 Nov 2026; $4 / $20 from 1 Dec 2026 |
| Google · Gemini 3.8 Flash | $0.75 | $3.75 | to 31 Dec 2026; $1.50 / $7.50 from 1 Jan 2027 |
| Google · Gemini 3.5 Flash-Lite | $0.30 | $2.50 | |
| DeepSeek · deepseek-flash (V4.1-Flash-1017) | ¥1 off-peak, ¥2 peak (cache miss) | ¥4 off-peak, ¥8 peak | yuan; peak = Beijing weekdays 9:00–12:00 and 14:00–18:00, excluding Chinese public holidays |
| DeepSeek · deepseek-v4-pro | ¥4.5 off-peak, ¥9 peak (cache miss) | ¥13.5 off-peak, ¥27 peak | yuan |

Sources: [OpenAI, *API pricing*](https://developers.openai.com/api/docs/pricing); [Google, *Gemini API pricing*](https://ai.google.dev/gemini-api/docs/pricing) (output prices include thinking tokens); [DeepSeek, *模型 & 价格*](https://api-docs.deepseek.com/zh-cn/quick_start/pricing).

Three things line up across vendors.

**The tiers mirror each other price for price.** Astra is priced like Fable ($10 / $50), Sol like Sonnet ($2 / $10), Luna like Haiku ($0.10 / $0.50), and Argon like Sonnet until December and like Opus after it (arithmetic on the two tables). The tier names differ; the price ladder is the same.

**Every vendor exposes an effort control.** Gemini 4 Argon takes low, medium and high thinking levels ([Google, *Gemini 4 Argon* model page, updated 14 Oct 2026](https://ai.google.dev/gemini-api/docs/models/gemini-4-argon)); DeepSeek's documented request enables thinking with a `reasoning_effort` setting ([DeepSeek pricing page, English](https://api-docs.deepseek.com/quick_start/pricing)). OpenAI documents five effort levels for GPT-6.1 Sol, low, medium (the default), high, xhigh and max ([OpenAI, *Latest model guide*](https://developers.openai.com/api/docs/guides/latest-model)); The Next Web reports that developers can change effort without losing cached context ([The Next Web, 22 Sep 2026](https://thenextweb.com/news/openai-gpt-6-sol-luna-api-price-cut)). Note that the 22 September models are GPT-6 Sol and Luna; the pricing page and Artificial Analysis now list GPT-6.1 Sol, which OpenAI's guide treats as a separate, later model; this unit's prices and scores are for GPT-6.1 Sol.

**Windows have converged at about a million tokens.** Argon's is 1,048,576 tokens, with 65,536 output tokens by default ([Google model page](https://ai.google.dev/gemini-api/docs/models/gemini-4-argon)); DeepSeek's is 1M with 384K output ([DeepSeek](https://api-docs.deepseek.com/zh-cn/quick_start/pricing)); Artificial Analysis lists 1M for each OpenAI model it tests ([Artificial Analysis, *Leaderboard*](https://artificialanalysis.ai/leaderboards/models)).

Consumer access differs. Google is rolling Argon out first to vetted cyber defenders, then to paid API customers and Google AI Ultra subscribers ([Google, *Gemini 4 Argon*, 30 Sep 2026](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-argon/)). The Next Web reports GPT-6 Sol and GPT-6 Luna in ChatGPT Work and Codex for paid accounts, with Luna available to Free and Go users in the desktop app ([The Next Web](https://thenextweb.com/news/openai-gpt-6-sol-luna-api-price-cut)). How the vendors compare per task, which is the measure that matters, is in §5.

## 5 · Cost per task

The cost of a task is input tokens times the input price plus output tokens, thinking included, times the output price, summed over every turn, with the whole history re-sent on each turn (B1 §2; §3 above). The price list fixes one factor. The other, how many tokens a model spends to finish the task, varies by model and by effort, and it can swamp the first.

**A small task, by arithmetic.** Assume a Shōmen post takes 4,000 input tokens (instructions, brand notes, the brief) and 1,500 output tokens including thinking. Those token counts are my assumption; nobody measured them. At API prices:

| Model | One post | A hundred posts |
|---|---|---|
| Haiku 5.5 | $0.0012 | $0.12 |
| Sonnet 5.5 | $0.023 | $2.30 |
| Opus 5.5 | $0.046 | $4.60 |
| Fable 5.1 | $0.115 | $11.50 |

On equal token counts the ratios follow the price list. In practice the counts are unequal.

**A measured comparison.** Artificial Analysis runs its Intelligence Index, a weighted set of agentic, coding, scientific and general tasks (categories from its methodology page), across models and effort levels, and reports a weighted cost per task computed from the model's token counts and prices (third-party vendor dataset; definition from [Artificial Analysis, *Claude Opus 5.5*](https://artificialanalysis.ai/models/claude-opus-5-5); figures from [Artificial Analysis, *Leaderboard*](https://artificialanalysis.ai/leaderboards/models), accessed 28 Oct 2026, figures updated to Intelligence Index v5.0 on 29 Oct 2026 after Audit 2):

| Model (effort) | Index | Cost per task |
|---|---|---|
| Opus 5.5 (low / medium / high / xhigh / max) | 35 / 48 / 52 / 57 / 58 | $0.98 / $2.45 / $3.46 / $6.05 / $10.04 |
| Sonnet 5.5 (low / medium / high / xhigh / max) | 25 / 30 / 41 / 50 / 54 | $0.51 / $0.78 / $1.64 / $4.09 / $10.02 |
| Haiku 5.5 (low / medium / high / xhigh / max) | 19 / 25 / 30 / 34 / 36 | $0.04 / $0.09 / $0.16 / $0.25 / $0.41 |
| Fable 5.1 (low / medium / high / xhigh / max) | 38 / 43 / 47 / 50 / 49 | $4.49 / $5.58 / $7.56 / $10.89 / $13.04 |
| GPT-6.1 Sol (high / max) | 50 / 55 | $0.59 / $1.27 |
| GPT-6 Luna (max) | 28 | $0.15 |
| Gemini 4 Argon (high) | 50 | $3.84 |
| Gemini 3.8 Flash (high) | 31 | $7.77 |
| DeepSeek V4.1 Flash (max) | 32 | $0.60 |

```viz
{"kind": "scatter", "title": "Index against cost per task, Claude models by effort",
 "x": {"label": "Cost per task (USD)", "min": 0, "max": 14, "ticks": [0, 2, 4, 6, 8, 10, 12, 14]},
 "y": {"label": "Index", "min": 15, "max": 60, "ticks": [20, 30, 40, 50, 60]},
 "points": [
  {"label": "Opus low", "x": 0.98, "y": 35, "tone": 2},
  {"label": "Opus medium", "x": 2.45, "y": 48, "tone": 2},
  {"label": "Opus high", "x": 3.46, "y": 52, "tone": 2},
  {"label": "Opus xhigh", "x": 6.05, "y": 57, "tone": 2},
  {"label": "Opus max", "x": 10.04, "y": 58, "tone": 2},
  {"label": "Sonnet low", "x": 0.51, "y": 25, "tone": 3},
  {"label": "Sonnet medium", "x": 0.78, "y": 30, "tone": 3},
  {"label": "Sonnet high", "x": 1.64, "y": 41, "tone": 3},
  {"label": "Sonnet xhigh", "x": 4.09, "y": 50, "tone": 3},
  {"label": "Sonnet max", "x": 10.02, "y": 54, "tone": 3},
  {"label": "Haiku low", "x": 0.04, "y": 19, "tone": 4},
  {"label": "Haiku max", "x": 0.41, "y": 36, "tone": 4},
  {"label": "Fable low", "x": 4.49, "y": 38, "tone": 1},
  {"label": "Fable medium", "x": 5.58, "y": 43, "tone": 1},
  {"label": "Fable high", "x": 7.56, "y": 47, "tone": 1},
  {"label": "Fable xhigh", "x": 10.89, "y": 50, "tone": 1},
  {"label": "Fable max", "x": 13.04, "y": 49, "tone": 1}
 ],
 "caption": "The four Claude rows of the table above: Intelligence Index score against weighted cost per task at each effort level (Haiku 5.5 at low and max only). §5, from <a href=\"https://artificialanalysis.ai/leaderboards/models\">Artificial Analysis, Leaderboard</a>, Intelligence Index v5.0, read 29 Oct 2026; third-party vendor dataset."}
```

Four readings, all arithmetic on that table:

1. **Price per token predicts little at the top of the effort range.** Opus 5.5 costs twice Sonnet 5.5 per token. At medium effort it costs 3.1 times as much per task; at max, Sonnet costs the same as Opus (99.8%) and scores four points lower. Pushing the cheaper model to maximum effort spends its price advantage.
2. **A small model at full effort can match a large one at low effort.** Haiku 5.5 at max scores 36 against Opus 5.5 at low's 35, for 42% of the cost.
3. **A cheaper token can make a dearer task.** At current prices, Gemini 3.8 Flash is 2.7 times cheaper per token than Argon and costs 2.0 times more per task, scoring 19 points lower.
4. **Across vendors, the same score has very different prices.** Around an index of 47 to 50: GPT-6.1 Sol at high costs $0.59, Opus 5.5 at medium $2.45 (4.2 times Sol), Gemini 4 Argon at high $3.84 (6.5 times Sol), Fable 5.1 at high $7.56 (12.8 times Sol).

```viz
{"kind": "compare", "title": "Cost per task, USD, at an index of 47 to 50", "max": 8,
 "rows": [
  {"label": "GPT-6.1 Sol (high)", "value": 0.59, "tone": 5},
  {"label": "Opus 5.5 (medium)", "value": 2.45, "tone": 2},
  {"label": "Gemini 4 Argon (high)", "value": 3.84, "tone": 6},
  {"label": "Fable 5.1 (high)", "value": 7.56, "tone": 1}
 ],
 "caption": "Reading 4 in §5: four models scoring around 47 to 50 on the Intelligence Index, by weighted cost per task. From <a href=\"https://artificialanalysis.ai/leaderboards/models\">Artificial Analysis, Leaderboard</a>, Intelligence Index v5.0, read 29 Oct 2026; third-party vendor dataset."}
```

**Where sources disagreed.** On 28 October 2026 Artificial Analysis's model page for Opus 5.5 gave $10.04 per task at max effort under index v5.0 with nine evaluations ([model page](https://artificialanalysis.ai/models/claude-opus-5-5)), while its leaderboard still gave $5.98 under the previous index ([leaderboard](https://artificialanalysis.ai/leaderboards/models)) and its methodology page named v4.3.2 with ten evaluations ([methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)). The disagreement was the changeover to Intelligence Index v5.0, announced on 27 October 2026 ([Artificial Analysis, *Announcing Intelligence Index v5*](https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v5)); by 29 October all three pages carried v5.0, and the table above was updated to it in Audit 2. The v5.0 index drops GDPval-AA and adds private coding and science tests, so its scores are not comparable with the figures the unit cited on 28 October. The absolute dollar figures should still be read as approximate; the index will move again.

Anthropic's own cost-per-task claims point the same way and are vendor data: at its default (medium) effort, Opus 5.5 beat Opus 5 at max effort on Terminal-Bench 4.0 for about a fifth of the cost, and beat GPT-6 Astra at max effort on GDPval-AA for about a fifth of the cost per task ([Anthropic, *Introducing Claude Opus 5.5*](https://www.anthropic.com/claude-opus-5-5)).

None of these tasks is a course unit, a caption or a calendar entry. What transfers is the mechanism: the bill is set by tokens spent per finished job, and effort moves that number as much as the model does.

One cost no table captures is his own time. A cheap first output that needs a second run, or a correction he has to spot and make, is paid out of 5 to 7 hours a week. No study measures that for him. The deliverable handles it with escalation triggers, so that a model that keeps costing him rework is replaced.

## 6 · When the cheap model is the right one

Three bodies of evidence say the cheap model is often enough, and they agree on when.

**Routing research.** FrugalGPT (Chen, Zaharia and Zou, TMLR 2024; first posted on arXiv 2023) found API prices varying by up to two orders of magnitude and reported that a cascade, which learns which models to query for each request, matched GPT-4's performance with up to 98% lower cost ([arXiv 2305.05176](https://arxiv.org/abs/2305.05176)). RouteLLM (Ong et al., ICLR 2025) trained routers that send each query to a strong or a weak model and cut costs by more than half in some cases without loss of response quality on the benchmarks they tested ([ICLR 2025 proceedings](https://proceedings.iclr.cc/paper_files/paper/2025/hash/5503a7c69d48a2f86fc00b3dc09de686-Abstract-Conference.html)). The mechanism in both: for a large share of queries the weak model's answer is already as good as the strong model's, and the saving comes from identifying those queries. Both tested 2023–24 models.

**Compute against size.** Snell and colleagues compared spending more inference compute on a smaller model against using a larger one at equal total compute. On problems where the smaller model already had a non-trivial success rate, the smaller model with more compute beat a model 14 times its size ([Snell et al., arXiv 2408.03314](https://arxiv.org/abs/2408.03314); published at [ICLR 2025](https://proceedings.iclr.cc/paper_files/paper/2025/hash/1b623663fd9b874366f3ce019fdfdd44-Abstract-Conference.html) under a slightly changed title). Effort can stand in for model size on tasks within the small model's reach.

**Vendor guidance.** Anthropic positions Haiku 5.5 for classification, extraction and routing ([Models overview](https://platform.claude.com/docs/en/models/overview)) and for summaries, compactions and classification ([Haiku 5.5 launch](https://www.anthropic.com/claude-haiku-5-5)). Its effort documentation says to run Haiku 5.5 at low for chat, short tool tasks and simple high-volume requests, and at high for knowledge work, longer agent tasks and strict instruction following ([Anthropic, *Effort*](https://platform.claude.com/docs/en/build-with-claude/effort)). A Claude Code team post (Lydia Hallie, 7 Jul 2026, before the 5.5 family) gives the general rule: smaller models for more routine tasks; larger models for more complex or ambiguous ones ([Claude blog, *Choosing a Claude model and effort level in Claude Code*](https://www.claude.com/blog/claude-model-and-effort-level-in-claude-code)).

**Where the cheap model falls off.** Anthropic's own table shows the gap widening with task length. On GDPval-AA v2.1, a knowledge-work test, Haiku 5.5 scores 1620 against Sonnet 5.5's 1840; on Terminal-Bench 4.0, long agentic terminal tasks, 39.2% against 70.6% ([Haiku 5.5 launch](https://www.anthropic.com/claude-haiku-5-5); vendor).

Put together, Haiku is the right model when the task is fully specified by its input, its correct output can be recognised at a glance, volume or speed matters, and an error is cheap to catch: classification, extraction to a fixed schema, reformatting, short tool calls. It is the wrong model when the task is open-ended, long or multi-step, or when a mistake hides well (a plausible wrong figure inside a long text). The combination of conditions is my synthesis of the sources above; each condition traces to one of them.

Two cautions specific to his setup. On the API, Haiku's price quintuples once a prompt passes 100K tokens (§3), so a cheap task loaded with a heavy context loses most of its advantage. On claude.ai, the same applies to his limits in kind: conversation length and attachments draw usage whatever the model (§2), so a small task belongs in a light chat, outside a Project stuffed with course documents.

## 7 · What thinking and effort settings do

**Thinking is adaptive.** On each request the model judges whether reasoning would improve the answer and how much; a simple factual question may get no thinking at all, a multistep problem gets more ([Anthropic, *Steering thinking*](https://platform.claude.com/docs/en/build-with-claude/thinking-steering-and-cost)). On Opus 5.5 and Fable 5.1 thinking is always on and cannot be switched off; on Haiku 5.5 and Sonnet 5.5 it cannot be switched off in the apps either ([Help Center, *Change the model, effort and extended thinking settings*](https://support.claude.com/en/articles/8664678-change-the-model-effort-and-extended-thinking-settings)).

**Effort sets how many tokens the whole response may spend.** Anthropic describes it as a behavioural signal, not a strict token budget, covering how often and how deeply Claude thinks, how many tool calls it makes, and how much it explains. The levels are low, medium, high, xhigh and max, with availability varying by model; xhigh is aimed at long-horizon work of more than 30 minutes. At lower effort Claude can skip thinking on easy problems and still thinks, less, on hard ones. On Opus 5.5, effort is the main lever on reasoning because thinking cannot be disabled ([Anthropic, *Effort*](https://platform.claude.com/docs/en/build-with-claude/effort)).

**Defaults.** On the API, Opus 5.5 and Haiku 5.5 default to medium; Sonnet 5.5 and Fable 5.1 to high ([Effort](https://platform.claude.com/docs/en/build-with-claude/effort); [Models overview](https://platform.claude.com/docs/en/models/overview)). Opus 5 defaulted to high, so the same request on Opus 5.5 with no effort set runs one level lower than it used to ([Effort](https://platform.claude.com/docs/en/build-with-claude/effort)). In the apps, Sonnet 5.5 defaults to medium ([Sonnet 5.5 launch](https://www.anthropic.com/claude-sonnet-5-5)) and Fable 5.1 to medium on claude.ai and in Cowork, high in Claude Code ([Fable 5.1 launch](https://www.anthropic.com/claude-fable-and-mythos-5-1)). The claude.ai help article marks each model's default in the menu without listing them ([Help Center](https://support.claude.com/en/articles/8664678-change-the-model-effort-and-extended-thinking-settings)).

**On claude.ai** the effort setting sits inside the model menu next to the send button. Anthropic's labels: low and medium suit routine tasks and stretch his limits; high is the best overall balance; extra high is for long-running coding and agentic work (Opus 4.7 and newer); max is the most thorough. Higher effort means more thorough responses that take longer, use more tokens and reach limits sooner ([Help Center](https://support.claude.com/en/articles/8664678-change-the-model-effort-and-extended-thinking-settings)).

**What a step of effort costs, measured.** On Artificial Analysis's index (third-party vendor data, §5), Opus 5.5 from low to max costs 10.2 times as much per task for 23 more points; medium to high costs 41% more for 4 points; high to xhigh costs 1.7 times more for 5 points; xhigh to max 1.7 times more for 1 point. Sonnet 5.5 from low to max costs 19.6 times more ([leaderboard](https://artificialanalysis.ai/leaderboards/models); arithmetic on its figures). The Claude Code post's diagram caption says the high-effort path "generates roughly 7x more tokens" for one prompt; the post gives no measurement behind it, and the only visuals it labels illustrative are its two cost-curve charts ([Claude blog](https://www.claude.com/blog/claude-model-and-effort-level-in-claude-code)), so that figure is one unmeasured example, not evidence.

**Extra thinking on easy problems is waste.** Chen and colleagues documented reasoning models spending large amounts of compute on trivially easy problems (the title's example is 2 + 3) and showed the excess could be cut while keeping accuracy ([Chen et al., ICML 2025; arXiv 2412.21187](https://arxiv.org/abs/2412.21187)). Anthropic's own guidance says the same in product terms: lower effort before trying to talk the model out of thinking ([Steering thinking](https://platform.claude.com/docs/en/build-with-claude/thinking-steering-and-cost)).

**Model or effort: the diagnostic.** The Claude Code post separates the two: "the model setting is roughly how capable; the effort setting is roughly how thorough." If Claude had full context, clearly tried, and still got it wrong, pick a more capable model; if it skipped files, skipped tests or did not double-check, raise effort ([Claude blog](https://www.claude.com/blog/claude-model-and-effort-level-in-claude-code)). The same post recommends the default effort for most tasks and treating effort as a standing preference more than a per-task dial (same post).

```viz
{"kind": "decision", "root": {"q": "Model or effort?", "tone": 4, "branches": [
  {"label": "full context, clearly tried, still wrong", "to": {"outcome": "More capable model", "tone": 2}},
  {"label": "skipped files, tests or double-check", "to": {"outcome": "Raise effort", "tone": 3}}]},
 "caption": "The model-or-effort diagnostic in §7, from Lydia Hallie, <a href=\"https://www.claude.com/blog/claude-model-and-effort-level-in-claude-code\">Choosing a Claude model and effort level in Claude Code</a>, Claude blog, 7 Jul 2026."}
```

**Keep effort fixed within a chat.** On the API, changing thinking or effort between requests invalidates the prompt cache, with two exceptions the page lists ([Steering thinking](https://platform.claude.com/docs/en/build-with-claude/thinking-steering-and-cost)). Whether the same happens on claude.ai is undocumented, as is the effect of caching on his limits (B1 §2). Setting effort once, before the first message, costs nothing and avoids the question.

## 8 · Where the quality differences show, and where they do not

### Long-form synthesis

On Anthropic's knowledge-work tests the gap between Opus and Sonnet nearly vanishes. GDPval-AA v2.1: Opus 5.5 1846, Sonnet 5.5 1844; AA-Briefcase v1.1: 1822 against 1811 ([Sonnet 5.5 launch](https://www.anthropic.com/claude-sonnet-5-5); vendor). The Haiku launch reports Sonnet at 1840 and 1824 on the same two tests and Haiku 5.5 at 1620 and 1578 ([Haiku 5.5 launch](https://www.anthropic.com/claude-haiku-5-5)), so Anthropic's own figures for Sonnet move by a few points between pages; the Sonnet page notes those two runs used a pre-release deployment with a since-fixed bug and may understate Sonnet slightly (Sonnet 5.5 launch). Anthropic ran Opus 5.5 at max effort for its table unless noted ([Opus 5.5 launch](https://www.anthropic.com/claude-opus-5-5)).

On reasoning with tools (Humanity's Last Exam), Anthropic reports Opus 5.5 at 67.7%, Sonnet 5.5 at 64.5% and Haiku 5.5 at 57.4% ([Sonnet 5.5 launch](https://www.anthropic.com/claude-sonnet-5-5); [Haiku 5.5 launch](https://www.anthropic.com/claude-haiku-5-5); vendor).

At the efforts he actually gets by default, the third-party index separates Opus and Sonnet: Opus 5.5 at medium scores 48, Sonnet 5.5 at medium 30, and Sonnet needs max effort (54, at $10.02 a task) to come within four points of Opus at max ([leaderboard](https://artificialanalysis.ai/leaderboards/models)).

A course unit is long, open-ended, searched and cited synthesis. The case for Opus there rests on that default-effort gap and on Anthropic's unquantified statement that Opus is stronger on open-ended work (§1). No source here measured anything like a course unit. His own record adds one data point about process: in the Greek review, reports written without a fresh checker scored 4.28 on his rubric, and syllabus unit 12, written with one, scored 4.8 (`method.md` §1, citing `audits/greece-13.4-cohorts.md`). That is a small internal sample, and it measures a checking step, which is the subject of B6.

### Code

On agentic coding the top two are level and Haiku falls behind on long tasks. Terminal-Bench 4.0: Sonnet 5.5 70.6%, Opus 5.5 66.4% (at xhigh), Haiku 5.5 39.2%. FrontierCode 1.1: Opus 54.4%, Sonnet 52.1% (at xhigh), Haiku 46.4% ([Sonnet 5.5 launch](https://www.anthropic.com/claude-sonnet-5-5); [Haiku 5.5 launch](https://www.anthropic.com/claude-haiku-5-5); vendor). Anthropic still recommends Sonnet or Opus over Haiku for complex agentic coding (Haiku launch). For his generator scripts and parsers, Sonnet is enough on this evidence; the Claude Code diagnostic (§7) says when to move up.

```viz
{
 "kind": "bars",
 "mode": "grouped",
 "unit": "%",
 "max": 100,
 "series": [
  {
   "name": "Opus 5.5",
   "tone": 2
  },
  {
   "name": "Sonnet 5.5",
   "tone": 3
  },
  {
   "name": "Haiku 5.5",
   "tone": 4
  }
 ],
 "rows": [
  {
   "label": "Terminal-Bench 4.0",
   "values": [
    66.4,
    70.6,
    39.2
   ]
  },
  {
   "label": "FrontierCode 1.1",
   "values": [
    54.4,
    52.1,
    46.4
   ]
  }
 ],
 "caption": "Anthropic's scores for the three 5.5 models on agentic coding (Terminal-Bench 4.0, Opus at xhigh; FrontierCode 1.1, Sonnet at xhigh). §8, from <a href=\"https://www.anthropic.com/claude-sonnet-5-5\">Anthropic, Introducing Claude Sonnet 5.5</a>, 28 Sep 2026, and <a href=\"https://www.anthropic.com/claude-haiku-5-5\">Introducing Claude Haiku 5.5</a>, 7 Oct 2026; vendor figures."
}
```

### Audit

No benchmark measures auditing a course unit against its sources. Three pieces of evidence bear on it.

- **Knowledge reliability.** On AA-Omniscience v1.1 (3,000 questions across six domains; it rewards correct answers, penalises wrong ones and leaves abstentions unpenalised), Fable 5.1 has the highest accuracy, 68%; Gemini 4 Carbon at high, listed by 29 October 2026, has the highest overall index, 54; Opus 5.5 has 48, against 46 for Fable 5.1 and Gemini 4 Argon; Gemini 4 Argon has the lowest hallucination rate, 4% ([Artificial Analysis, *AA-Omniscience*](https://artificialanalysis.ai/evaluations/omniscience); third-party vendor data).
- **Model judges.** Strong model judges agreed with human preferences more than 80% of the time, the same rate at which humans agree with each other, and showed position, verbosity and self-enhancement biases ([Zheng et al., NeurIPS 2023, arXiv 2306.05685](https://arxiv.org/abs/2306.05685)). The judges tested were 2023 models.
- **Self-preference.** Model evaluators score their own outputs above others', and the bias grows with the model's ability to recognise its own text ([Panickssery, Bowman and Feng, NeurIPS 2024](https://papers.nips.cc/paper_files/paper/2024/hash/7f1f0218e45f5414c79c0679633e47bc-Abstract-Conference.html); [arXiv 2404.13076](https://arxiv.org/abs/2404.13076)).

So the best-evidenced part of his method is that a different model audits from the one that wrote. Choosing Fable specifically rests on that independence and on a narrow lead in factual accuracy; general capability benchmarks favour Opus 5.5 (§1). Fable and Opus are both Anthropic models, and none of the studies above tested whether self-preference carries across sibling models from one maker. That question stays open.

His own record is consistent with this. Audit 1 failed 23 of 91 cited claims in the A2/A6/A9 research document and none of the 7 sampled in B1 ([Audit 1, 28 Oct 2026](https://claude.ai/artifact/2uA7uLCuUAGRZuUoywpaRj)); the research document was written by Fable 5.1 research agents and B1 by Opus 5.5 (`courses-index.md`; the audit notes that its own prompt named Opus 5.5 for all four and that the index record should stand). Two documents on different tasks prove nothing about the models. They do show that the dearer model's output was the one that failed, and that the audit, whatever wrote the text, is what caught it.

### Reformatting and triage

No benchmark isolates reformatting or triage, so the evidence that model size stops mattering here is indirect: the routing results and the compute-against-size result in §6, and Anthropic's positioning of Haiku for exactly these jobs. The reasoning that ties them together is mine: reformatting and triage are tasks whose correct output is fully determined by the input, so a model has nothing to add beyond following the instruction, and capability differences show up where a task needs something the input does not contain (judgement, synthesis, search). The check is cheap, because the output can be compared with the input at a glance; sample it before trusting it (B6).

One exception. Where the task is arithmetic over numbers, such as totals or averages from an export, the model should write and run code, and the code should produce the numbers. The same input can give a model different outputs even at fixed settings (B1 §5); a script gives the same output every time.

## Deliverable · Model routing table

For his recurring tasks, as of 28 October 2026. Set model and effort before the first message of a chat and leave them. "Escalate" means one step up, once, when the trigger fires. Section numbers point to the evidence in this unit.

| Task | Pick | Effort | Why | Override if |
|---|---|---|---|---|
| **Journal entries** (his notes or a voice transcript into a dated entry in his words) | Sonnet 5.5 | medium | Polished writing from given material; Sonnet's knowledge-work score is within a few points of Opus (vendor, §8); about a third of Opus's per-task cost at medium (32%, §5). | The entry has to synthesise several weeks or several journeys: Opus 5.5, medium. Pure tidy-up of a transcript: Haiku 5.5, low. |
| **Biometrics parsing** (exports into tables or totals) | Haiku 5.5 writes and maintains the parsing script; the script does the parsing | high | Extraction is Haiku's documented use (§6); high effort is Anthropic's setting for strict instruction following (§6); numbers come from code because model outputs vary run to run (§8, B1 §5). | The script breaks twice on a new export format: Sonnet 5.5, medium, to rewrite it. |
| **Course units** (Brand + AI units, history modules) | Opus 5.5 | high | The method's writing model; at default effort Opus leads Sonnet by 18 index points (third-party, §8); medium to high adds 4 points for 41% more cost per task (§7); the units still to write number in the dozens (`courses-index.md`), so the premium is paid rarely. | Limits run short mid-unit: stay on Opus 5.5 at medium and keep the chat; never switch model inside a unit. |
| **Audits** (four-unit sample, staleness check, fresh checks) | Fable 5.1 | high | A different model from the writer counters self-preference (§8); highest factual accuracy on AA-Omniscience (third-party, §8); the method's audit model. On Pro every Fable run is billed in usage credits at API rates; on Max it competes for half the weekly limit (§2). | Fable is unavailable or out of budget: Opus 5.5 at high in a fresh chat that has not seen the unit, and record in the audit that the auditor was the writer's model. |
| **Message drafts, routine** (logistics, replies, short notes) | Sonnet 5.5 | low | Short, well-scoped writing; low effort is Anthropic's setting for routine work and stretches limits (§7). | The draft misreads the situation twice: treat it as high-stakes. |
| **Message drafts, high-stakes** (manager, board, HR, conflict, performance) | Opus 5.5 | medium | Anthropic describes Opus 5.5 as built for complex work requiring careful judgment (Sonnet 5.5 launch; vendor); the cost of one message at any tier is cents (§5); the judgement that this is small next to a bad message is mine. | Nothing; this row is the escalation. |
| **Calendar** (creating and editing events with his rules) | Haiku 5.5 | high | A short tool task with strict, fixed rules; Anthropic's guidance for Haiku is high effort for strict instruction following (§6); errors are visible at a glance in the event. | An event breaks one of his calendar rules twice in a month: Sonnet 5.5, medium. |
| **Research** (questions that need web search and synthesis) | Opus 5.5 | high | Multi-step, searched work; on Humanity's Last Exam with tools, Opus 5.5 67.7%, Sonnet 64.5%, Haiku 57.4% (vendor, §8); search draws usage on any model (§2), so a model that needs a second round of searching costs more than one that does it once. | A single factual lookup: Sonnet 5.5, low. |
| **Video scripts** | From a finished unit: Sonnet 5.5. Original, with no unit behind it: Opus 5.5 | medium | A script cut from a sourced unit is derivative work, which the method gives to Sonnet; an original script is synthesis (§8). | Sonnet's script drops or bends a sourced claim from the unit: redo on Opus 5.5, medium. |
| **Shōmen posts** (captions, product copy) | Sonnet 5.5 | low | Short derivative copy in a public voice; at a hundred posts the cost on Sonnet is about $2.30 by the §5 arithmetic, so the saving from Haiku buys little. | Twenty or more variants at once: Haiku 5.5, medium, and he picks by hand. |
| **Reformatting and triage** (brain dumps into lists, tables between formats, tagging, sorting an inbox) | Haiku 5.5 | low | Fully specified by its input; Haiku's documented use (§6); routing research shows weak models match strong ones on such queries (§6). | The triage needs a judgement about priorities: Sonnet 5.5, medium. |

**Rules for using the table**

- **Escalate by cause.** Wrong with full context and a real attempt: move the model up one step. Skipped steps, missed files, no double-check: raise effort one step (§7).
- **Run small tasks in a light chat.** Captions, calendar and reformatting go outside the Learning Project, where the window carries less (§2, §6; B1 §2).
- **Never trust a single run on anything that will be published or filed.** Sample its claims against the sources first (§8; B6).
- **Keep a one-line log of every escalation** (task, from, to, trigger). Two escalations on the same row in a month change the row.
- **Re-read the prices before relying on them.** Two change on dates already announced: Gemini 4 Argon on 1 December 2026, Gemini 3.8 Flash on 1 January 2027 (§4). Re-read the Artificial Analysis index version too: the scores and per-task costs under the routing table are Intelligence Index v5.0 (§5); if its methodology page names a later version, the numbers have changed method and are not comparable with these. The whole table is due for the staleness check on 28 April 2027.

## Writer's unsure list

Fresh check 28 Oct 2026 (Fable 5.1): fix · 3 errors, 10 should-fix, 14 minor; all applied; report `audits/brand-ai/fresh-check-B2.md`.

Audit 2 29 Oct 2026 (Fable 5.1, stratified sample): PASS · 0 of 9 sampled FAIL, 3 STALE; 1 incidental FAIL (§7 seven-times miscite); Artificial Analysis figures moved to Intelligence Index v5.0; errata B2-1 to B2-25 applied; report `audits/brand-ai/audit-2.md`.

Erratum P34 29 Oct 2026: the deliverable's "re-read the prices" rule now also names the Artificial Analysis index version (v5.0).

1. **Artificial Analysis figures changed the day after writing.** On 28 October the leaderboard gave Opus 5.5 at max $5.98 per task and the model page $10.04; the gap was the changeover to Intelligence Index v5.0, and Audit 2 (29 October) replaced every §5, §7, §8 and deliverable figure with the v5.0 values. The meaning of "with fallback" in the model labels is not explained on the pages read. Every §5 and §7 ratio rests on the leaderboard as read on 29 October 2026.
2. **Gemini 3.8 Flash at $7.77 per task, above Argon's $3.84,** is the most surprising figure in the unit and may be a data artefact. It is reported as the leaderboard shows it.
3. **OpenAI's announcement page failed to load.** GPT-6 Sol and Luna positioning and ChatGPT availability come from The Next Web (secondary); GPT-6.1 Sol's effort levels come from OpenAI's model guide. Prices come from OpenAI's own pricing page, which lists gpt-6.1-sol where the news coverage says GPT-6 Sol.
4. **claude.ai defaults for Opus 5.5 and Haiku 5.5** are not stated anywhere I found; the unit gives the API defaults and the app defaults only for Sonnet 5.5 and Fable 5.1.
5. **The per-model rate at which claude.ai usage is drawn** is undocumented. The claim that API prices are his marginal price holds only for usage credits and for Fable on Pro.
6. **Anthropic's benchmark figures move between its own pages:** Sonnet 5.5 GDPval-AA 1844 (Sonnet launch) against 1840 (Haiku launch); AA-Briefcase 1811 against 1824; Fable 5.1 GDPval-AA 1853 on v2 (Fable launch) against 1735 on v2.1 (Opus launch).
7. **FrugalGPT and the overthinking paper were cited from arXiv as preprints;** the fresh check found their venues (TMLR 2024; ICML 2025) and the text now cites them.
8. **The token counts in the Shōmen example (4,000 in, 1,500 out)** are my assumptions, and the per-post costs are arithmetic on them.
9. **The self-preference evidence is about a model judging its own output.** Whether it extends to a sibling model from the same maker (Fable auditing Opus) is untested in the sources cited.
10. **The Claude Code post on model and effort choice** predates the 5.5 family (7 Jul 2026); its advice is general, and its seven-times token figure is a single diagram caption with no measurement behind it.

## Sources

All web sources checked 28 October 2026.

- Anthropic. *Models overview*. Claude Platform docs. https://platform.claude.com/docs/en/models/overview
- Anthropic. *Pricing*. Claude Platform docs. https://platform.claude.com/docs/en/about-claude/pricing
- Anthropic. *Effort*. Claude Platform docs. https://platform.claude.com/docs/en/build-with-claude/effort
- Anthropic. *Steering thinking*. Claude Platform docs. https://platform.claude.com/docs/en/build-with-claude/thinking-steering-and-cost
- Anthropic. *Introducing Claude Fable 5.1 and Claude Mythos 5.1*. September 2026. https://www.anthropic.com/claude-fable-and-mythos-5-1
- Anthropic. *Introducing Claude Opus 5.5*. 22 September 2026. https://www.anthropic.com/claude-opus-5-5
- Anthropic. *Introducing Claude Sonnet 5.5*. 28 September 2026. https://www.anthropic.com/claude-sonnet-5-5
- Anthropic. *Introducing Claude Haiku 5.5*. 7 October 2026. https://www.anthropic.com/claude-haiku-5-5
- Claude. *Plans & pricing*. https://claude.com/pricing
- Claude Help Center. *About Claude's Pro plan usage*. https://support.claude.com/en/articles/8324991-about-claude-s-pro-plan-usage
- Claude Help Center. *About Claude's Max plan usage*. https://support.claude.com/en/articles/11014257-about-claude-s-max-plan-usage
- Claude Help Center. *Claude Fable models on your plan*. 2 September 2026. https://support.claude.com/en/articles/15424964-claude-fable-models-on-your-plan
- Claude Help Center. *Manage usage credits for paid Claude plans*. https://support.claude.com/en/articles/12429409-manage-usage-credits-for-paid-claude-plans
- Claude Help Center. *Usage limit best practices*. 22 September 2026. https://support.claude.com/en/articles/9797557-usage-limit-best-practices
- Claude Help Center. *Change the model, effort and extended thinking settings*. https://support.claude.com/en/articles/8664678-change-the-model-effort-and-extended-thinking-settings
- Hallie, L. *Choosing a Claude model and effort level in Claude Code*. Claude blog, 7 July 2026. https://www.claude.com/blog/claude-model-and-effort-level-in-claude-code
- OpenAI. *API pricing*. https://developers.openai.com/api/docs/pricing
- OpenAI. *Latest model guide*. https://developers.openai.com/api/docs/guides/latest-model
- The Next Web. *OpenAI cuts GPT-6 prices in half with Sol and Luna*. 22 September 2026 (secondary report). https://thenextweb.com/news/openai-gpt-6-sol-luna-api-price-cut
- Google. *Gemini API pricing*. https://ai.google.dev/gemini-api/docs/pricing
- Google. *Gemini 4 Argon*. Gemini API model page, last updated 14 October 2026. https://ai.google.dev/gemini-api/docs/models/gemini-4-argon
- Google. *Gemini 4 Argon: our next era of frontier intelligence*. 30 September 2026. https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-argon/
- DeepSeek. *模型 & 价格* (Models and pricing). API docs. https://api-docs.deepseek.com/zh-cn/quick_start/pricing · English page with the `reasoning_effort` example: https://api-docs.deepseek.com/quick_start/pricing
- Artificial Analysis. *LLM Leaderboard*. Accessed 28 October 2026; figures re-read 29 October 2026 under Intelligence Index v5.0 (vendor dataset). https://artificialanalysis.ai/leaderboards/models
- Artificial Analysis. *Announcing Artificial Analysis Intelligence Index v5*. 27 October 2026. https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v5
- Artificial Analysis. *Claude Opus 5.5*. Model page (vendor dataset). https://artificialanalysis.ai/models/claude-opus-5-5
- Artificial Analysis. *Intelligence benchmarking methodology*. https://artificialanalysis.ai/methodology/intelligence-benchmarking
- Artificial Analysis. *AA-Omniscience*. v1.1, October 2026 (vendor dataset). https://artificialanalysis.ai/evaluations/omniscience
- Chen, L., Zaharia, M. and Zou, J. "FrugalGPT: How to Use Large Language Models While Reducing Cost and Improving Performance". arXiv 2305.05176, 2023; published in Transactions on Machine Learning Research, 2024. https://arxiv.org/abs/2305.05176 · https://openreview.net/forum?id=cSimKw5p6R
- Ong, I., Almahairi, A., Wu, V., Chiang, W.-L., Wu, T., Gonzalez, J. E., Kadous, M. W. and Stoica, I. "RouteLLM: Learning to Route LLMs from Preference Data". ICLR 2025. https://proceedings.iclr.cc/paper_files/paper/2025/hash/5503a7c69d48a2f86fc00b3dc09de686-Abstract-Conference.html
- Snell, C., Lee, J., Xu, K. and Kumar, A. "Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters". arXiv 2408.03314, 2024; published at ICLR 2025 as "Scaling LLM Test-Time Compute Optimally Can be More Effective than Scaling Parameters for Reasoning". https://arxiv.org/abs/2408.03314 · https://proceedings.iclr.cc/paper_files/paper/2025/hash/1b623663fd9b874366f3ce019fdfdd44-Abstract-Conference.html
- Chen, X. et al. "Do NOT Think That Much for 2+3=? On the Overthinking of o1-Like LLMs". arXiv 2412.21187, 2024; published at ICML 2025 as "Do NOT Think That Much for 2+3=? On the Overthinking of Long Reasoning Models". https://arxiv.org/abs/2412.21187 · https://icml.cc/virtual/2025/poster/45540
- Zheng, L. et al. "Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena". NeurIPS 2023 Datasets and Benchmarks Track. arXiv 2306.05685. https://arxiv.org/abs/2306.05685
- Panickssery, A., Bowman, S. R. and Feng, S. "LLM Evaluators Recognize and Favor Their Own Generations". NeurIPS 2024. https://papers.nips.cc/paper_files/paper/2024/hash/7f1f0218e45f5414c79c0679633e47bc-Abstract-Conference.html · arXiv 2404.13076: https://arxiv.org/abs/2404.13076
- Learning Project. *Audit 1: A2 · A6 · A9 and B1*. Fable 5.1, 28 October 2026. https://claude.ai/artifact/2uA7uLCuUAGRZuUoywpaRj
- Learning Project files cited by name: `method.md` §1; `courses-index.md`; B1 · Mental model (`B1-mental-model.md`).
