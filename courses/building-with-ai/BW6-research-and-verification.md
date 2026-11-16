---
code: BW6
title: Research and verification
course: building-with-ai · BW · Building with AI
model: Opus 5.5
written: 2026-11-16
search: off
---

# BW6 · Research and verification

This unit was written with search off. Searches were used only to re-verify the sources it cites, on 16 November 2026, and every product fact (a feature, a limit, a running time) carries the date it was read on the vendor's own page; most help-centre pages show no exact date of their own. Each practice carries an evidence grade, as in BW1 to BW5: **measured** (a study or test with numbers), **documented practice** (a vendor or a named practitioner says to do it; nobody measured it here) or **stated opinion**. Every study names the models it tested; carrying its finding to a current model or to your work is this unit's inference, and is said to be. The sampling arithmetic is shown in the text so you can redo it by hand.

What this unit assumes: why fabrication follows from how text is produced (BW1 §7); why one good answer is one draw (BW1 §5); the self-preference and self-correction studies and the rule that the check runs outside the writer's conversation (BW2 §5); the brief form and the two checking templates, critique and audit (BW3, Deliverable, templates 3 and 9); and the every-unit done-when lines of a spec (BW5, Deliverable 2b). It uses them by section and does not restate them. What it adds is the part those units leave here: how to get an answer, how to read it, how big a sample to check, and what a clean sample proves.

## 1 · Ask, search or deep research

BW1 §4 separated three kinds of knowledge: trained, retrieved and in the conversation. The three ways of asking map onto them. Asking directly draws on trained knowledge and whatever is already in the window. Search adds retrieved pages. Deep research adds many retrieved pages, gathered by several agents at once. Each step up spends more tokens and returns more claims, and each claim returned is one you may have to check. The price of research has two parts: the tokens to produce it and your time to verify it.

### Ask directly

**When.** The answer is a concept, a mechanism or a method settled before the model's training cutoff (June 2026 for Opus 5.5, Sonnet 5.5, Haiku 5.5 and Fable 5.2, as BW1 §4 read Anthropic's page on 15 Nov 2026), or the job transforms material already in the window: summarising a pasted document, reformatting, drafting from your notes. In those jobs the window holds the facts and the model supplies the structure.

**When not.** Anything after the cutoff, and any specific number, name, date, quotation or citation you will publish, file or act on. A sentence from training and a sentence produced with no basis read the same (BW1 §4, §7); only a source in the window tells them apart.

**Cost and time.** Tokens only; what a task costs on each model is BW2 §1. No source read for this unit gives a time figure for a direct answer.

### Search

**When.** One current fact, one rule, one price, or one citation that has to exist: a lookup with one answer.

**Cost.** On Anthropic's API, web search costs $10 per 1,000 searches plus the tokens the results add, and on a plan it draws on your usage limit (BW2 §6, read 15 Nov 2026). Anthropic's engineering team reports that agents, which call tools such as search in a loop, "typically use about 4× more tokens than chat interactions" ([Hadfield, Zhang, Lien, Scholz, Fox and Ford, *How we built our multi-agent research system*, Anthropic Engineering, 13 Jun 2025](https://www.anthropic.com/engineering/multi-agent-research-system); vendor, measured on Anthropic's 2025 systems). No source read gives a time figure for one search.

**What it changes.** Search puts a page in the window, so a claim can point to something. The claim can still be false, and search adds a failure that asking directly lacks: the page itself may be stale, secondary or poor. The same post reports that Anthropic's early research agents "consistently chose SEO-optimized content farms over authoritative" sources until source-quality rules were added to their prompts (Hadfield et al., 2025; vendor). §3 is the reading rule for what search brings back.

### Deep research

**What it is.** On claude.ai, Research "runs multiple searches that build on each other"; it is available on the Pro, Max, Ultra, Team and Enterprise plans, and "You must have web search turned on for research to function" ([Claude Help Center, *Use research on Claude*](https://support.claude.com/en/articles/11088861-use-research-on-claude), read 16 Nov 2026; the page shows only "Updated over 2 weeks ago"). Anthropic built the feature as a multi-agent system: a lead agent plans and starts subagents that search in parallel, and a separate citation agent places the citations at the end (Hadfield et al., 2025; vendor).

**When.** Anthropic's own account of where the design fits: it excels at "breadth-first queries" that involve "pursuing multiple independent directions simultaneously"; tasks where all agents must share the same context, or with many dependencies between agents, "are not a good fit for multi-agent systems today" (Hadfield et al., 2025; vendor). A landscape question (what three literatures each say about one practice) fits. A chain of questions where each depends on the last answer does not; that is search, one step at a time, in one chat.

**Cost.** Multi-agent systems, the post reports, "use about 15× more tokens than chats", and on Anthropic's BrowseComp evaluation "token usage by itself explains 80% of the variance" in performance, with the number of tool calls and the choice of model as the two other factors (Hadfield et al., 2025; vendor, an association across its runs on Claude Opus 4 as lead and Claude Sonnet 4 as subagents). No source read says whether the 15× ratio holds for Research on current models. On a plan, the help page says "research sessions can use up your limits faster due to Claude retrieving multiple sources" and gives no rate (*Use research on Claude*, read 16 Nov 2026).

**Time.** When Anthropic extended Research in 2025 it said reports arrive "in anywhere from five to 45 minutes" and that "most reports complete in five to 15 minutes" ([Anthropic, *Claude can now connect to your world*, 1 May 2025](https://claude.com/blog/integrations); vendor, the 2025 feature). The current help page gives no running time (read 16 Nov 2026).

**What it changes.** Deep research returns the most claims and the most citations, and §2 shows that the share of invented links rises with it.

The three routes on one axis:

```viz
{
  "kind": "compare",
  "unit": "×",
  "max": 15,
  "rows": [
    {"label": "Chat", "value": 1, "tone": 3},
    {"label": "Agent with tools", "value": 4, "display": "about 4×", "tone": 2},
    {"label": "Multi-agent research", "value": 15, "display": "about 15×", "tone": 1}
  ],
  "caption": "Tokens used by an agent and by a multi-agent research system, relative to a chat (§1 of this unit). From Hadfield et al., <em>How we built our multi-agent research system</em>, Anthropic Engineering, 13 Jun 2025; vendor figures, measured on Anthropic's 2025 systems."
}
```

**The routing rule** (stated opinion, each branch traced to a source above). Ask directly when nothing in the answer needs a source; a specific that turns up anyway is checked before use. Search when one answer needs one source. When several directions need covering and each depends on the others' findings, search one step at a time in one chat. When they are independent, use deep research if the result is worth roughly fifteen chats of tokens plus the checking of every claim it returns; otherwise search each direction in its own chat.

```viz
{
  "kind": "decision",
  "root": {
    "q": "Does the answer need, from outside the chat, a fact after the cutoff or a specific you will publish, file or act on?",
    "tone": 4,
    "branches": [
      {"label": "no", "to": {"outcome": "Ask directly", "tone": 3}},
      {"label": "yes", "to": {
        "q": "Several directions to cover?",
        "tone": 4,
        "branches": [
          {"label": "no", "to": {"outcome": "Search", "tone": 2}},
          {"label": "yes", "to": {
            "q": "Are the directions independent of each other?",
            "tone": 4,
            "branches": [
              {"label": "no", "to": {"outcome": "Search, one step at a time, in one chat", "tone": 2}},
              {"label": "yes", "to": {
                "q": "Worth about fifteen chats of tokens plus checking its claims?",
                "tone": 4,
                "branches": [
                  {"label": "no", "to": {"outcome": "Search each direction in its own chat", "tone": 2}},
                  {"label": "yes", "to": {"outcome": "Deep research", "tone": 1}}
                ]
              }}
            ]
          }}
        ]
      }}
    ]
  },
  "caption": "The routing rule of §1 (this unit's synthesis, stated opinion): the cutoff from BW1 §4; the fit conditions and the roughly fifteen-fold token cost from Hadfield et al., Anthropic Engineering, 13 Jun 2025 (vendor). Every route that ends in something published, filed or acted on then goes through the sampling rule of §5."
}
```

**The case** (Academy case; one project, an anecdote). The first three units of one of Academy's courses were written from one research report produced by research agents across five tracks; a later full audit of those units failed 23 of 91 claims, with nothing invented (Academy case file §3). The case file does not record the research agents' model (§9 of the file; BW2, row 7). What the case shows is a report that read as finished and still carried a failure rate of about one claim in four (23/91 = 25.3%, by arithmetic) into the work built on it.

## 2 · How models fail, and the studies that measured it

BW1 §7 gave the mechanism: a fluent, specific, wrong sentence is an ordinary output of next-token prediction. This section gives the rates. Three failures recur, and each looks like a good answer.

### Confident, specific, wrong

The confidence in the wording carries no information about the truth of the content. OpenAI's SimpleQA benchmark asked models short factual questions with one indisputable answer each and also asked them to state their confidence; the authors found that "models consistently overstate their confidence". On that benchmark GPT-4o answered 38.2% of questions correctly and Claude 3.5 Sonnet 28.9%, and the Claude models declined to answer more often than the GPT-4o models ([Wei et al., *Measuring short-form factuality in large language models*, arXiv 2411.04368, 7 Nov 2024](https://arxiv.org/pdf/2411.04368); preprint, a vendor's benchmark; tested GPT-4o, GPT-4o-mini, o1-preview, o1-mini and four Claude 3 and 3.5 models). The accuracy figures belong to that question set; the calibration finding is the one this unit carries over, and carrying it to current models is this unit's inference.

Retrieval lowers the rate without removing it. Varun Magesh and colleagues ran a preregistered test of the AI research tools of two legal publishers, whose vendors had described retrieval as eliminating or avoiding hallucinations, one promising "hallucination-free" citations; the tools of LexisNexis (Lexis+ AI) and Thomson Reuters (Westlaw AI-Assisted Research and Ask Practical Law AI) produced hallucinated content "between 17% and 33% of the time", fewer than general-purpose GPT-4 ([Magesh, Surani, Dahl, Suzgun, Manning and Ho, *Hallucination-Free? Assessing the Reliability of Leading AI Legal Research Tools*, arXiv 2405.20362v1, 30 May 2024](https://arxiv.org/abs/2405.20362v1); preprint version; measured on 2024 tools).

### Stale facts presented as current

A model's trained knowledge stops at its cutoff, and nothing in the output marks which sentences depend on it (BW1 §4). Tu Vu and colleagues built FreshQA, a set of questions whose answers change over time or rest on false premises, and found that "all models (regardless of model size) struggle on questions that involve fast-changing knowledge and false premises"; adding current search results to the prompt raised accuracy substantially ([Vu et al., *FreshLLMs: Refreshing Large Language Models with Search Engine Augmentation*, arXiv 2310.03214v2, 22 Nov 2023](https://arxiv.org/abs/2310.03214); preprint; tested 2023 models).

Search can bring staleness in with the page. Delip Rao, Eric Wong and Chris Callison-Burch checked the URLs cited by ten systems on a research benchmark; for OpenAI's deep-research agent, about 65% of the links that no longer resolved were real pages that had gone offline, against links that never existed ([Rao, Wong and Callison-Burch, *Detecting and Correcting Reference Hallucinations in Commercial LLMs and Deep Research Agents*, arXiv 2604.03173v1, 3 Apr 2026](https://arxiv.org/abs/2604.03173); preprint).

In the Academy case (anecdote), ten claims in one unit went stale from one cause: an independent benchmark published a new index version the day before the unit read its leaderboard (Academy case file §4). BW1 §4 drew the lesson for writing (date every fact); the lesson for checking is that staleness arrives in batches, because every fact read on one day ages together.

### Invented citations

William Walters and Esther Isabelle Wilder asked GPT-3.5 and GPT-4 for 84 short literature reviews on 42 topics and checked all 636 citations: 55% of GPT-3.5's and 18% of GPT-4's citations were fabricated, and among the real works cited, 43% (GPT-3.5) and 24% (GPT-4) carried substantive errors in the reference itself (authors, title, date, journal, volume, pages). They note that fabricated citations "tend to look legitimate at first glance" ([Walters and Wilder, *Fabrication and errors in the bibliographic citations generated by ChatGPT*, *Scientific Reports* 13, 14045, 2023](https://www.nature.com/articles/s41598-023-41032-5.pdf); peer-reviewed, 2023 models, no search). The study did not test whether the real works supported the text.

Search and deep research do not remove the problem. In Rao and colleagues' study, the two deep-research agents (Gemini 2.5 Pro Deep Research and OpenAI's) cited far more links per query, 113.1 and 41.2 against 3.0 to 24.3 for eight search-augmented models, and a larger share of them were hallucinated, meaning the URL did not resolve and had no archived copy: 10.7% pooled, against 4.8% (Rao et al., 2026; preprint). The authors call their rates "conservative lower bounds". The systems tested were 2024 and 2025 releases, Claude 3.5 and 3.7 Sonnet with search among them; no Claude deep-research agent was evaluated. No study read compares the same model with and without search on the same questions, so how much search lowers the rate is not measured here.

### What the case adds: the failures it names were in real sources, none invented

The case points the checking effort somewhere specific (anecdote, one project). Of the 36 Academy units given a fresh check before filing, 28 had at least one error in the writer's draft, 58 errors in all; the kinds the reports name are a figure the cited page does not carry, an author named wrongly, a law that had changed, a quotation the page does not hold, a count that did not add up, and a product fact that differed between two of the vendor's own pages (Academy case file §5). None of those kinds is an invented source. The one audit that counted (23 failures in 91 claims) found nothing invented, and named its pattern: qualifiers the source does not carry (case file §3). A check that only confirms each cited source exists would have passed every one of those failures. The rule this unit draws (stated opinion, built on the case and on Walters and Wilder's finding that real citations also carry errors): a check opens the source and compares the claim with what it says, figure, sample, date, population and qualifiers. Existence is the first test, never the last.

## 3 · How to read a research report

A research report is a list of claims, each attached to a source. Reading it well means grading each attachment before believing the claim. Four questions, in order.

**1. What class of source is it, and is it the source or a report of one?** This course accepts five classes: peer-reviewed work; a preprint, labelled as one; vendor documentation or statements, labelled and dated; a named practitioner's own post, talk or repository, labelled as practice; and an independent benchmark with its version and date (the course's sourcing standard, in its shared preamble). They differ in what they can carry. Peer review checks method; a preprint has not had that check; a vendor describes its own product; a practitioner reports one practice; a benchmark measures one version on one day. Anything else (a content-farm summary, a tool vendor's post with no sample, a forum thread) is a lead to a source and never the source. The class also tells you whether you hold the claim or a report of it: a figure is cited to the page that measured it, and a page that repeats the figure is a reporter, kept separate.

**2. Who paid for it, and what do they sell?** A vendor's numbers may be right; what the funding predicts is the direction of any error. The best measurement comes from medicine. A Cochrane review of 75 papers found industry-sponsored studies more likely than non-industry studies to report favourable efficacy results (risk ratio 1.27, 95% CI 1.17 to 1.37) and favourable conclusions (1.34, 1.19 to 1.51), and concluded that the bias could not be explained by standard risk-of-bias assessments ([Lundh, Lexchin, Mintzes, Schroll and Bero, *Industry sponsorship and research outcome*, Cochrane Database of Systematic Reviews, 16 Feb 2017](https://www.cochrane.org/MR000033/METHOD_industry-sponsorship-and-research-outcome); peer-reviewed). Carrying that to software vendors is this unit's analogy; no study read measures sponsorship bias in AI benchmarks. Two signs that it applies: the legal-tool vendors' claims of hallucination-free citation against the measured 17% to 33% (§2), and a model maker's launch table, which reports its own model against rivals it chose (BW2 §4). The reading: name the vendor, give the sample and the date, read the method note for what the sample leaves out, and treat the vendor's figure as the best case.

**3. Does the design support the verb?** A correlational finding supports "is associated with". It does not support "causes", "drives" or "leads to". Austin Bradford Hill's 1965 paper is still the standard list of what moves an association towards causation: strength, consistency, specificity, temporality, biological gradient, plausibility, coherence, experiment and analogy; Hill held that a causal relationship can exist when some of them do not apply, and warned against using them as exact rules ([Hill, *The Environment and Disease: Association or Causation?*, *Proceedings of the Royal Society of Medicine* 58(5), 1965, 295–300](https://pmc.ncbi.nlm.nih.gov/articles/PMC1898525/); as summarised by [Abboud, *"The Environment and Disease: Association or Causation?" (1965), by Austin Bradford Hill*, Embryo Project Encyclopedia, 23 Mar 2017](https://embryo.asu.edu/pages/environment-and-disease-association-or-causation-1965-austin-bradford-hill)). For reading an AI-written report, three of the nine do most of the work (stated opinion): temporality (did the cause come first?), gradient (does more of it go with more of the effect?) and experiment (has anyone changed it on purpose and measured the result?). The verbs to watch are the ones the model supplies: "drives", "boosts", "the key to", "proven". Each needs a design behind it; where the source is correlational, the sentence is rewritten with "is associated with".

**4. Is the claim what the source says, today?** The claim must match the source without a stretch: the figure, the sample, the date, the population and the qualifiers. And a fact that can change carries the date it was read, because a report is a snapshot (§2, the case's benchmark version). The pattern the case's first audit named, a qualifier the source does not carry (§2), fails here.

A report that passes all four questions on a sample of its claims can be used. §5 sets the sample.

## 4 · Why the writer should not be its checker, and what a fresh context changes

BW2 §5 gives the evidence that a model grades its own work too kindly and does not reliably correct itself without outside input, and sets the course's rule: the check runs in a fresh context at the least, by a different model where the stakes justify the cost. This section adds what the separation buys and what it does not.

**What a fresh context removes.** The writer's reasoning. Anthropic's Claude Code guide says that `/code-review` reviews the diff "in a fresh subagent that never saw your conversation. It isn't swayed by the reasoning that produced the code", and that, while handing the same task to a subagent does not make the answer better, "A fresh reviewer does help, because it hasn't seen your reasoning" ([Anthropic, *Best practices for Claude Code*](https://code.claude.com/docs/en/best-practices?ref=t01.li), read 16 Nov 2026; vendor, documented practice). In BW1's terms (§1), the window holds the text and its sources, and not the conversation that made the text seem right. BW2 §5's table adds the limit: a fresh context of the same model removes the conversation and not self-recognition; only a different model removes both, as far as the studies tested.

**What it does not remove.** A checker who re-reads the text without opening the sources is the same kind of draw as the writer (BW1 §5), and the self-correction evidence in BW2 §5 is about exactly that case. The fresh context helps only if the check carries outside feedback: the source, a test, a file. Where no source exists to open, the only outside signal is other draws. Potsawee Manakul, Adian Liusie and Mark Gales showed that when a model hallucinates a fact, "stochastically sampled responses are likely to diverge and contradict one another" ([Manakul, Liusie and Gales, *SelfCheckGPT*, EMNLP 2023, 9004–9017](https://aclanthology.org/2023.emnlp-main.557); peer-reviewed, tested on GPT-3 passages about people in the WikiBio dataset). Asking the same factual question in two or three fresh chats is therefore a cheap screen: different specific answers mean the fact is treated as invented until a source is found. Agreement proves nothing; it only fails to raise the alarm.

**What a fresh checker adds of its own.** The same guide warns that "A reviewer that's asked to find problems will always find *something*", and that fixing every finding ends in "extra abstraction layers and tests for cases that can't happen" (*Best practices for Claude Code*, read 16 Nov 2026; vendor). A checker produces false alarms as well as misses. §6 deals with both.

**The case** (anecdote). Academy's fresh check is a separate context that has not seen the unit written; it checks every cited claim against its source and the deliverable against the brief, writes graded findings and never edits, and a maintainer verifies each finding before applying it (Academy case file §2). Two different checks run in the case and must be kept apart: the fresh check before filing, which three models ran (Fable 5.1 on 19 drafts, Opus 5.5 on 12, Fable 5.2 on 5; case file §5), and the sample audit every four units, for which the method names Fable 5.1 (case file §2). BW2 §5 reads the fresh-check counts by checker model; they compare nothing, since units, courses and dates differ and there is no control (case file §9).

## 5 · The stratified-sample audit, and what a clean sample proves

### The rule

A sample audit, as this course uses the term (stated opinion, generalised from the case's method in BW5 §10, which this unit does not restate):

1. **List and count** the checkable claims: every sentence that carries a number, a date, a named source, an attribution, a mechanism or a recommendation. Call the count N.
2. **Stratify.** Split the claims into groups that could fail together: the sections of a long text, the source classes of a research report, the claim types of a short piece (numbers, quotations, names, dates, links). Draw at least one claim from every stratum, then more from the largest until the sample reaches its size.
3. **Draw by number, never by eye.** Number the claims in each stratum and pick with a random number.
4. **Record the sample before opening any source**, so that a claim that turns out hard to check cannot be swapped for an easy one.
5. **Check each sampled claim** against its source and give it one verdict: PASS, FAIL, STALE (true when written, superseded now) or UNVERIFIABLE (the source cannot be opened; drawn again from the same stratum, and the claim itself marked unsourced).
6. **Let the sample decide.** It is a trigger: a FAIL sends the whole text to a full check; a clean sample lets the rest stand, at a known risk.

Stratification matters because errors cluster: one bad source feeds every claim drawn from it, and one benchmark version change made ten claims stale in one unit of the case (Academy case file §4). A simple random sample of the same size can miss a whole section; a stratified one cannot.

This is acceptance sampling, an established part of statistical quality control: a sample is drawn from a lot, and the lot is accepted or rejected on it. The NIST/SEMATECH handbook lists when it is used (testing is destructive, full inspection costs too much or takes too long) and states its limit: its purpose is to decide whether the lot is likely to be acceptable, "not to estimate the quality of the lot" ([NIST/SEMATECH, *6.2.1. What is Acceptance Sampling?*, e-Handbook of Statistical Methods](https://itl.nist.gov/div898/handbook/pmc/section2/pmc21.htm), read 16 Nov 2026). Checking an AI-written text against its sources is not destructive, but it is slow, which is the case for sampling; and the limit carries over exactly.

### What a sample can catch

Suppose a fraction *p* of a text's checkable claims would FAIL, and the sampled claims behave like independent draws. The chance that a sample of *n* claims contains no FAIL is (1 − *p*)ⁿ. Worked out (arithmetic, no source needed):

| Claims sampled (*n*) | No FAIL seen, if 10% would fail | No FAIL seen, if 25% would fail |
|---|---|---|
| 7 | 47.8% | 13.3% |
| 9 | 38.7% | 7.5% |
| 14 | 22.9% | 1.8% |
| 20 | 12.2% | 0.3% |
| 29 | 4.7% | 0.0% (0.02%) |

```viz
{
  "kind": "line",
  "x": ["7", "9", "14", "20", "29"],
  "unit": "%",
  "min": 0,
  "max": 50,
  "decimals": 1,
  "xlabel": "Claims sampled",
  "height": 520,
  "series": [
    {"name": "If 10% would fail", "values": [47.8, 38.7, 22.9, 12.2, 4.7], "tone": 4},
    {"name": "If 25% would fail", "values": [13.3, 7.5, 1.8, 0.3, 0.0], "tone": 1}
  ],
  "caption": "The chance that a sample shows no FAIL, by sample size, when 10% or 25% of a text's claims would fail: the table in §5 of this unit, computed as (1 − p)ⁿ. Arithmetic in this unit; 25% is close to the failure rate of the case's research-based units at their full audit (23 of 91, Academy case file §3)."
}
```

Read the two lines. A text failing at one claim in four is caught by almost any sample of nine or more. A text failing at one in ten slips past a sample of seven about half the time, and past a sample of fourteen about one time in four. A small sample is a tripwire for bad texts and lets moderately flawed ones through.

When sampling without replacement from a short text, the true chance of missing is a little lower than (1 − *p*)ⁿ, so the table errs on the side of caution (this unit's arithmetic). The independence assumption errs the other way when failures cluster inside one stratum; stratification is the answer to that.

### What a clean sample proves

Run the arithmetic backwards. If all *n* sampled claims pass, the largest failure rate still consistent with that at 95% confidence is the *p* for which (1 − *p*)ⁿ = 0.05, so *p* = 1 − 0.05^(1/*n*). For a clean 7 that is 34.8%; for 9, 28.3%; for 14, 19.3%; for 20, 13.9%; for 29, 9.8%. Thomas Newman, writing in *JAMA*, credits James Hanley and Marilyn Lippman-Hand with the shortcut: when nothing goes wrong in N trials, the upper 95% limit for the rate is about 3/N ([Newman, *If Almost Nothing Goes Wrong, Is Almost Everything All Right? Interpreting Small Numerators*, *JAMA* 274(13), 1995, 1013](https://jamanetwork.com/journals/jama/article-abstract/389714); a letter). For 29 claims, 3/29 = 10.3%, close to the exact 9.8%.

So a clean sample is permission to proceed with a stated residual risk, and it certifies nothing. A clean sample of seven says only that the text is probably not failing at more than about one claim in three.

### Choosing the sample size from the stakes

The same formula, solved for *n*, turns a decision about stakes into a sample size. Decide the failure rate you must be able to rule out (*p\**) and solve (1 − *p\**)ⁿ ≤ 0.05: *n* = ln(0.05) / ln(1 − *p\**), rounded up, roughly 3/*p\**. Three tiers (the tiers and their rates are this unit's design, stated opinion; the sizes follow from them by arithmetic):

| Tier | What the text is | Rate to rule out (*p\**) | Sample (*n*) | A clean sample shows, at 95% |
|---|---|---|---|---|
| **1 · Low** | For you alone; easily corrected; nothing is decided on it | 30% | 9 | failure rate below 28.3% |
| **2 · Medium** | Shared with others, or a decision rests on it | 20% | 14 | below 19.3% |
| **3 · High** | Published under your name, sent to a client, or carrying legal, financial or health consequences | 10% | 29 | below 9.8% |

Three rules sit on top (stated opinion):

- **Census when small.** If N is no larger than the tier's *n*, check every claim; a sample would cost as much and leave risk behind.
- **The claims the conclusion rests on are always checked**, in every tier, outside the sample: the figure in the headline, the quotation the argument turns on, the citation a decision depends on. A sample bounds the rate across the rest; it says nothing about the one claim that matters most.
- **Any FAIL in the sample sends the text to a full check.** This is an acceptance number of zero, stricter than the case's "more than one in ten" (Academy case file §2). The reason is the arithmetic: with *n* at 14 or 29, one-in-ten would let one or two failures through, and a single FAIL already shows the rate is above zero; the sample sizes above were chosen so that a clean sample means something, and that only holds if clean is required. Below ten sampled claims the two rules coincide, since one FAIL is already more than one in ten.

Two outcomes widen the check whatever the tier (stated opinion). An **invented** source, quotation or number in the sample sends the text to a full check at once, because invention at the rates of §2 is unlikely to be alone. A **STALE** claim is not a FAIL, but it triggers a sweep of every fact in the text that can change, re-read and dated, because facts read on one day age together (§2).

## 6 · Checking a checker

A checker's report is AI-written. Its verdicts are claims ("this figure matches the source"), and they fail in two directions: a false FAIL, which the Claude Code guide predicts when it says a reviewer asked for gaps will usually find some (§4), and a false PASS, which lets an error through silently. The rules (stated opinion, built on §4 and §5):

1. **Re-open the source behind every FAIL and STALE before applying its fix.** A wrong FAIL applied as a correction puts an error into a text that was right. The case already does this: a maintainer verifies each finding and applies it as an exact replacement (Academy case file §2).
2. **Re-open a sample of PASS verdicts:** five, drawn by number. Be clear about what that buys. Five clean re-checks bound the checker's false-PASS rate only below 45% at 95% (1 − 0.05^(1/5) = 45.1%): the re-check catches a careless checker and no more. One wrong PASS in it sends the check to be run again by a context, and if possible a model, that saw neither the writing nor the first check.
3. **Re-check against the source, never against the checker's wording.** Reading the report and agreeing with it is a draw on the checker's reasoning (BW2 §5).
4. **Seed known errors when the checker is new or the stakes are high.** Change three checkable claims in a copy of the text so they no longer match their sources, record which, and see whether the checker reports them. The arithmetic is modest: a checker that misses half of all errors still catches three of three one time in eight (0.5³ = 12.5%), so one seeded check shows little; across checks, ten seeded errors all caught bound the checker's miss rate below 25.9%. Seeding detects a blind checker cheaply; it takes many checks to show a good one.
5. **Record which model checked, and its version.** In the case, a session's model named "fable" resolved to a newer version than the method names, and the checks it ran were recorded as owed again on the named version (Academy case file §7).
6. **Keep the checker's reading record.** In the case, some sessions kept no agent transcript, so scripted checks of what each agent had read could not run, and the agents' own reports stood in their place (case file §7). A report that says a source was opened is a claim; where you can, keep the evidence that it was.

The case's figure checks show the loop working and its cost (anecdote): a separate agent checked each figure against the unit's text, a figure that failed was fixed and checked again by a new agent, and one sitemap figure passed on its eighth check (Academy case file §6). The case file does not count how many fresh-check findings the maintainer rejected as wrong, so the case gives no measure of its checkers' false-alarm rate (a need, listed in this unit's notes).

## 7 · The Academy case's numbers, read as an anecdote

What the case's two kinds of check found, and what the arithmetic of §5 says each result proves. One project by one person, one model family writing, no control and no second project (Academy case file §9): these numbers describe the case and say nothing about rates elsewhere.

**The fresh check, a census.** 36 drafts got one before filing; 28 had at least one error and 8 had none; the findings totalled 58 errors, 237 should-fix and 303 minor (case file §5). That is 77.8% of drafts with an error, by arithmetic. A count kept at the time in one unit gives the same picture earlier: fifteen of the first twenty drafts had an error at first check (case file §5). A first draft written to a sourcing standard, under a method that names Opus 5.5 as its writer (case file §2, which says the model that wrote each unit is recorded; the case file does not list it per draft), was usually close and rarely clean.

**Audit 1, a sample that triggered.** One of eight sampled claims failed, which triggered a full audit of the three research-based units: 23 of 91 claims failed, none was stale, nothing was invented and no conclusion flipped (case file §3). On §5's arithmetic, a sample of eight from a text failing at that rate (25.3%) shows no FAIL about one time in ten (0.747⁸ = 9.7%): the tripwire worked as designed, and could have missed. The verdict was rewrite, because the three deliverables did not exist and two table rows rested on figures the cited vendor pages did not contain; from then on every unit of that family got a fresh check before filing (case file §3). The same audit passed one unit on seven of seven sampled claims (case file §3), which on §5's arithmetic is consistent with a failure rate up to 34.8% in that unit.

**Audit 2, a clean sample and what it missed.** 28 claims were sampled across four units and none failed; 96 were checked in all; one incidental claim outside the sample failed (a miscited caption); ten claims were stale, all in one unit, from one benchmark version change; all four units passed and 26 errata were applied the same day (case file §4). A clean 28 is consistent with a failure rate of up to about 10% across the four units (1 − 0.05^(1/28) = 10.1%; 3/28 = 10.7%), and the incidental FAIL is the kind of error that rate allows. The case file does not say how many of the ten stale claims were in the sample.

**What the numbers support.** They support three of this unit's rules as observations in one project: that a full check of the first drafts found errors in most of them (§4), that the failures the reports name were in real sources, with none invented (§2), and that a clean sample left errors standing (§5). They do not show that the fresh check caused the later audits to pass; the case file does not record whether Audit 2's units had a fresh check (BW5 §10 makes the same point). Which model ran each audit after Fable 5.2's release, and what any check cost in time or money, are not recorded (case file §9; BW2, routing table, "Sources for Part 1").

## 8 · On other tools

The principles of §2 to §7 (failure as a rate, reading by source class and design, a fresh context for the check, stratified sampling, the arithmetic of a clean sample, checking the checker) need no particular product; their sources are peer-reviewed work, preprints across vendors, and a statistics handbook. What is specific to Claude, with the equivalent where the other vendor's own documentation was found (all read 16 Nov 2026):

| Claim in this unit | Claude | ChatGPT and OpenAI | Gemini and Google |
|---|---|---|---|
| A deep-research mode that runs many searches, with a stated running time (§1) | Research: [*Use research on Claude*](https://support.claude.com/en/articles/11088861-use-research-on-claude) (no running time); five to 45 minutes in 2025 ([*Claude can now connect to your world*](https://claude.com/blog/integrations)) | Not checked: OpenAI's deep-research help page refused the fetch. On the API, a docs page headed [*Web search*](https://developers.openai.com/api/docs/guides/deep-research.md) advises background mode "for reports that can take several minutes" | Deep Research makes a research plan you can edit, and "It usually takes about 5-10 minutes to generate the report"; daily limits apply: [*Use Deep Research in Gemini Apps*](https://support.google.com/gemini/answer/15719111) |
| Deep research uses about 15× a chat's tokens (§1) | Anthropic's own 2025 system: [Hadfield et al.](https://www.anthropic.com/engineering/multi-agent-research-system) | No equivalent figure found in the pages read | No equivalent figure found in the pages read |
| A fresh subagent for review, one that never saw the conversation (§4) | [*Best practices for Claude Code*](https://code.claude.com/docs/en/best-practices?ref=t01.li) | Not checked for this unit (BW5 §11 records OpenAI's Codex review page as unreadable on 15 Nov 2026) | Gemini CLI subagents each have an "Independent context window": [*Subagents*, Gemini CLI documentation](https://geminicli.com/docs/core/subagents/) (vendor, read 16 Nov 2026) |
| Help-centre warning that the deep-research mode can use limits faster (§1) | *Use research on Claude* | Not checked (fetch refused) | The Deep Research page states daily request limits and gives no statement about accuracy or checking |

The research of §2 tested OpenAI, Google, Anthropic and legal-publisher systems; none of it tested a model current on 16 Nov 2026.

## Deliverable · A verification protocol

Two parts. Part 1 is the protocol as a checklist, built in full on the Academy case: route, tier, sampling rule with its arithmetic, how to check one claim, the brief for a fresh checker, the check of the checker, what to do on failure, the log, and the verifiability test. Part 2 is the template for your project, each blank saying what goes in it. Every rule traces to the section named beside it. BW8 turns the checker brief (step E) into a skill; BW9 uses the verifiability test (step I) to decide what to hand to an agent. Product facts are as read on 16 Nov 2026; model names are from BW2's routing table, read 15 Nov 2026.

### Part 1 · On the Academy case

The text is one unit of a course, written by one model from its brief and published to anyone (Academy case file §1, §2). Values the case file does not hold are marked `[UNKNOWN: …]`; they must be filled from the project's records before use, never guessed.

**A · Route the job before asking** (§1)

| Job | Route | Cost, dated | Time | Then |
|---|---|---|---|---|
| A concept settled before the cutoff; summarising or reformatting material in the chat | Ask directly | Tokens only (BW2 §1) | No source gives a figure | Any number, name, date or quotation it gives is checked before use |
| One current fact, price, rule or citation | Search | $10 per 1,000 searches plus result tokens on the API; draws on a plan's limit (BW2 §6, read 15 Nov 2026); an agent with tools about 4× a chat's tokens (Anthropic, 13 Jun 2025; vendor) | No source gives a figure | Open the cited page yourself; date the fact |
| Several independent directions, worth a report (the case: the research report behind three units, case file §3) | Deep research | About 15× a chat's tokens (Anthropic, 13 Jun 2025; vendor, 2025 system); "can use up your limits faster" (help page, read 16 Nov 2026) | 5 to 45 minutes, most 5 to 15 (Anthropic, 1 May 2025; vendor, 2025 feature) | Tier 3 sample on the whole report before anything is written from it |
| Several independent directions, not worth a report | Search each direction in its own chat | As search, per direction | As search | As search |
| Several directions that each need the others' findings | Search, one step at a time, in one chat | As search | As search | As search |

- [x] The brief asks for a source behind each claim and allows "I do not know" (BW1 §7; BW3 §3).

**B · Before checking** (§5)

- [x] **List and count** the checkable claims. The case: N = `[UNKNOWN: the number of checkable claims in the unit; the case file does not record claim counts per unit]`.
- [x] **Set the tier.** The case: **tier 3**, published to anyone (case file §1).
- [x] **Set the strata.** The case: the unit's sections, as the case's audit does (case file §2), plus the deliverable as its own stratum.
- [x] **Name the claims the conclusion rests on**, checked in full outside the sample. The case: every figure and citation in the deliverable.

**C · The sampling rule, with its arithmetic** (§5)

| Tier | *n* | A clean sample shows (95%) | If 25% would fail, chance the sample misses it |
|---|---|---|---|
| 1 · Low | 9 | rate below 28.3% | 7.5% |
| 2 · Medium | 14 | rate below 19.3% | 1.8% |
| 3 · High | 29 | rate below 9.8% | 0.02% |

*n* = ln(0.05) / ln(1 − *p\**), rounded up, for *p\** = 30%, 20%, 10%; upper bound = 1 − 0.05^(1/*n*); miss chance = 0.75ⁿ.

- [x] **C1 · Census if small.** If N ≤ *n*, check every claim.
- [x] **C2 · Draw.** One claim per stratum, then extra draws from the largest strata until the sample reaches *n*; within a stratum, by random number.
- [x] **C3 · Record** the sample (claim, stratum, cited source) before opening any source.
- [x] **C4 · Verdicts.** PASS · FAIL (wrong, unsupported, miscited, stretched or invented) · STALE (give the newer value and its source) · UNVERIFIABLE (draw again from the same stratum; mark the claim unsourced).
- [x] **C5 · Decide.**
  - an invented source, quotation or number → **full check**, at once;
  - any FAIL → **full check** (acceptance number zero);
  - any STALE → **sweep**: re-read and date every fact in the text that can change;
  - all PASS → **use it**, with the residual risk the table states, and log it.
- [x] **C6 · State what the clean sample means** in the log, in words: "consistent with up to [bound]% failing".

**How the case runs it, and what the arithmetic says.** The case checks every cited claim of a unit at the fresh check before filing (case file §2): a census, which leaves no sampling risk and is what this protocol asks of a tier 3 text whose N is unknown. Its audit every four units draws one claim per section (case file §2); Audit 2 drew 28 across four units, about seven a unit (case file §4). Under C, seven per unit is smaller than even a tier 1 sample (9): a clean seven is consistent with up to 34.8% failing in that unit, and the four units' clean 28 with up to 10.1% across them. The protocol therefore reads the case's audit as a tripwire behind the census, and its fresh check as the step that carries the assurance (this unit's reading; the case file draws no such conclusion).

```viz
{
  "kind": "decision",
  "root": {
    "q": "Anything invented, or any FAIL, in the sample?",
    "tone": 4,
    "branches": [
      {"label": "yes", "to": {"outcome": "Full check", "tone": 1}},
      {"label": "no", "to": {
        "q": "Any STALE?",
        "tone": 4,
        "branches": [
          {"label": "yes", "to": {"outcome": "Sweep every fact that can change, then use it and log it", "tone": 2}},
          {"label": "no", "to": {"outcome": "Use it; log what the clean sample means", "tone": 3}}
        ]
      }}
    ]
  },
  "caption": "Rule C5 of the Deliverable: what each sample result triggers. The acceptance number of zero, the early stop on invention and the sweep on STALE are this unit's design (stated opinion), argued in §5."
}
```

**D · Checking one claim** (§2, §3)

- [x] Open the cited source. A claim with no source is FAIL in tier 3 and is marked unsourced in tiers 1 and 2.
- [x] The source exists, and says this: the same figure, sample, date, population and qualifiers. The pattern the case's first audit named was a qualifier the source does not carry (case file §3).
- [x] The source is the original, cited for its own words; a page that repeats it is a reporter.
- [x] The class is acceptable and labelled: peer-reviewed; preprint; vendor, dated; practice; benchmark with version and date.
- [x] Vendor figures are read as the best case; a correlational source carries "is associated with", never "causes", "drives" or "boosts".
- [x] A fact that can change carries the date it was read.
- [x] Words in quotation marks are the source's exact words.

**E · The checker brief, on the case** (§4; BW3's form, built from its templates 3 and 9)

Run in a context that has not seen the unit written, on a model other than the writer's where affordable: large, top rung, Fable 5.2, high (BW2, rows 5 and 9, read 15 Nov 2026). The case's own fresh-check prompt is not in the case file; the brief below is this protocol's, applied to the case.

    TASK: Check unit [UNKNOWN: the unit's code] against its cited sources and its brief, and report findings. Do not edit the unit.

    READER: the maintainer, who verifies each finding at its source and applies it as an exact text replacement; a finding they cannot verify from what you give them has failed.

    SCOPE AND SAMPLE:
    - Tier 3 (published). Count the checkable claims: every sentence with a number, a date, a named source, an attribution, a mechanism or a recommendation. Give the count, N.
    - Check every cited claim (census). If the maintainer has set a sample instead, it is 29 claims: one per section, the deliverable as its own section, then extra draws from the largest sections, by random number.
    - Before opening any source, list the claims you will check, with their section and cited source.
    - Check in full, outside any sample, every figure and citation in the deliverable.

    METHOD, for each claim:
    1. Open the cited source. A source you cannot open is UNVERIFIABLE, never FAIL.
    2. Compare the claim with what the source says: the figure, the sample, the date, the population, the qualifiers. Look in particular for a qualifier the claim carries that the source does not; a figure the cited page does not carry; an author named wrongly; a law or product fact that has changed; a quotation the page does not hold; a count that does not add up; a product fact that differs between two of the vendor's own pages.
    3. Check that the source is the original (a page that repeats it is a reporter) and that its class is labelled.
    4. Verdict: PASS, FAIL, STALE (give the newer value and its source) or UNVERIFIABLE.

    OUTPUT, Markdown in this chat:
    1. N, and the list of claims checked, recorded before checking.
    2. Findings, most serious first: [error | should-fix | minor] [section] · Current: "[exact text, occurring once in the unit]" · Problem · Fix: "[replacement]" · Basis: [source link and where on the page]. An error is a claim the source does not support, a miscitation, an invented item or a missing part of the brief.
    3. Confirmed: each claim that holds, one line, with its source and the words on the page that support it (under 15 words, exact).
    4. Invented items found: list them, or "none".
    5. Last line: verdict (keep | fix | rewrite), counts of errors, should-fix and minor, and the model and version you ran as.

    CONSTRAINTS:
    - Open every source before its verdict; cite nothing you did not open.
    - Check the deliverable against the brief: present, in full, as named.
    - Flag only what affects correctness or the brief's requirements. Style is minor at most.
    - No praise, no summary of the unit.

    MATERIAL:
    <brief>
    [UNKNOWN: the unit's brief, verbatim]
    </brief>
    <unit>
    [UNKNOWN: the unit as handed in]
    </unit>

    DONE WHEN:
    - the claims checked were listed before any source was opened;
    - every finding quotes text that occurs once in the unit and gives its fix and its basis;
    - every claim checked is a finding or confirmed;
    - the last line gives one verdict, the counts and the checker's model and version.

    TASK (again): check the unit above against its sources and its brief, and report.

**F · Checking the checker** (§6)

- [x] Every FAIL and STALE: re-open its source before applying the fix. (The case: the maintainer verifies each finding, case file §2.)
- [x] Five PASS verdicts, drawn by number: re-open their sources. Five clean bound the checker's false-PASS rate below 45%; one wrong PASS → the check runs again in a context that saw neither the writing nor the first check.
- [x] Re-check against the source, never against the checker's wording.
- [x] For a new checker brief or model: seed three known errors in a copy; all three must be reported. Keep a running count across checks: ten seeded and all caught bound the miss rate below 25.9%.
- [x] Record the checker's model and version from the session itself. (The case: a model name that resolved to a newer version, case file §7.)
- [x] A long text in which the checker found nothing: run a second check with another model (BW2, row 5 override).

**G · On failure**

- [x] **Full check:** every checkable claim, by D; each FAIL fixed as an exact replacement, checked before it is applied (case file §2).
- [x] **Rewrite** from the brief in a new context when the full check shows the deliverable missing or the conclusion resting on failed claims. (The case: Audit 1's rewrite verdict, for missing deliverables and rows resting on figures the cited pages did not contain, case file §3.)
- [x] **Already published:** correct it in the open, with the date and the reason.
- [x] **The same kind of failure twice:** change the brief or the route as well as the text (BW2, rule 4).

**H · The log**

One line per check: date · text · tier · N · sampled · PASS / FAIL / STALE / UNVERIFIABLE · decision (C5) · "consistent with up to …% failing" · checker model and version · what changed.

The case, Audit 2 (case file §4): `[UNKNOWN: date] · four units [UNKNOWN: codes] · tier 3 · N [UNKNOWN] · 28 sampled · 28 not FAIL, 0 FAIL; 10 STALE in one unit (how many sampled not recorded); 1 incidental FAIL outside the sample · all four passed · consistent with up to 10.1% failing across the four · [UNKNOWN: the model that ran Audit 2; the method names Fable 5.1, case file §2] · 26 errata applied the same day`.

**I · The verifiability test, for deciding what to delegate** (§4, §5; used by BW9)

A task's output can be handed to a model, or to an agent, only as far as it can be checked. Anthropic's Claude Code guide states the condition for leaving an agent to work unwatched: "Give Claude something it can run that comes back pass or fail. Once it has that, it can keep going on its own and you don't have to watch" (*Best practices for Claude Code*, read 16 Nov 2026; vendor). Four questions, in order (stated opinion):

1. **Can the output be broken into checkable claims, or does it come with a check that returns pass or fail** (a source per claim, a test, a total that can be recomputed)?
2. **Can a context that did not do the work run that check** from the output and its sources alone, without the worker's reasoning?
3. **Does checking the tier's sample cost clearly less than doing the task yourself?**
4. **Is the residual risk of a clean sample acceptable for this text** (C's bound for its tier), and is an error that slips through visible and correctable later?

Verdict: four yes → delegate, and check by C. Questions 1 or 2 no → do not delegate as it stands; restructure the task so that its output carries sources or a test, or keep it. Question 3 no → delegate only if a census is still cheaper than doing it, or keep it. Question 4 no → delegate the draft, and check in full.

The case, writing a unit: (1) yes, every claim is cited in place (case file §1); (2) yes, the fresh check is a separate context that has not seen the unit written and checks it against its sources and its brief (case file §2); (3) `[UNKNOWN: the case file records no hours or money per unit or per check, case file §9]`; (4) the census at fresh check leaves no sampling risk, and a published error can be corrected by erratum (case file §4: 26 errata applied). Verdict on the record: delegate and check, with question 3 unanswered.

**J · The done-when line this protocol fills in BW5's spec** (BW5, Deliverable 2b)

- [x] A context that did not do the work has checked the unit by step E (census, or the tier's sample), its checker re-checked by step F, and the result logged by step H.

### Part 2 · Template: your verification protocol

Copy it, fill each blank, and keep the rules as they are unless your log gives you a reason to change one.

**A · Route.** Keep the five routes of Part 1, and fill the two dated columns:

| Job | Route | Cost on your tool, dated | Time on your tool, dated | Then |
|---|---|---|---|---|
| [*a direct-answer job in your project*] | Ask directly | [*the model and plan you use; the date you read its pricing or limits page*] | [*a stated time, or "no source gives a figure"*] | Check every specific before use |
| [*a single lookup in your project*] | Search | [*your tool's search price or limit, and the date read*] | [*as above*] | Open the page; date the fact |
| [*a landscape question in your project*] | Deep research | [*your tool's statement of how deep research draws on limits, and the date read*] | [*the vendor's stated running time, and the date read*] | Tier [*1, 2 or 3*] sample on the whole report |
| [*independent directions not worth a report*] | Search each in its own chat | [*as search*] | [*as search*] | As search |
| [*a chain of dependent questions*] | Search, one step at a time | [*as search*] | [*as search*] | As search |

**B · Before checking.**

- [ ] N = [*the count of sentences with a number, a date, a named source, an attribution, a mechanism or a recommendation*]
- [ ] Tier = [*1: for you alone, easily corrected; 2: shared, or a decision rests on it; 3: published under your name, sent to a client, or with legal, financial or health consequences*]
- [ ] Strata = [*sections for a long text; source classes for a research report; claim types (numbers, quotations, names, dates, links) for a short piece*]
- [ ] Claims the conclusion rests on, checked in full = [*the headline figure, the quotation the argument turns on, the citation a decision depends on*]

**C · Sampling rule.** Keep the table of Part 1 unchanged. If you change a tier's rate *p\**, recompute *n* = ln(0.05) / ln(1 − *p\**) and the bound 1 − 0.05^(1/*n*), and write both here: [*your tier, your p\*, your n, your bound*]. Keep C1 to C6.

**D · Checking one claim.** Keep the seven checks of Part 1. Add the source classes your field accepts beyond the five: [*e.g. statutes and case law with their citation, a regulator's guidance with its date; or "none"*].

**E · Checker brief.** Copy Part 1's brief and fill:

    TASK: Check [FILL: the text, and its name or code] against its cited sources and its brief, and report findings. Do not edit it.
    READER: [FILL: who applies the findings, and how: exact replacements, or a decision to send it back].
    SCOPE AND SAMPLE:
    - Tier [FILL: 1, 2 or 3] ([FILL: why this tier]). Count the checkable claims and give N.
    - [FILL: "Check every cited claim (census)", or "Sample n = 9 / 14 / 29: one per stratum, then extra draws from the largest strata, by random number"]. Strata: [FILL: the strata from B].
    - Before opening any source, list the claims you will check.
    - Check in full, outside the sample: [FILL: the claims the conclusion rests on].
    METHOD: keep steps 1 to 4 of Part 1; add to step 2 the failure kinds your own log has recorded: [FILL: from your log, or "none yet"].
    OUTPUT: keep items 1 to 5 of Part 1.
    CONSTRAINTS: keep Part 1's four; add [FILL: any field rule, e.g. "cite the paragraph of the statute"; or nothing].
    MATERIAL:
    <brief>
    [FILL: the brief the text was written from, verbatim]
    </brief>
    <text>
    [FILL: the text as handed in]
    </text>
    DONE WHEN: keep Part 1's four lines.
    TASK (again): check the text above against its sources and its brief, and report.

Model line: [*from your BW2 routing table, rows 5 and 9: tier, model, effort, and the date you read the vendor's model page; a model other than the writer's where affordable*].

**F · Checking the checker.** Keep the six checks of Part 1. Seeded-error count to date: [*seeded so far / caught so far, and the bound 1 − 0.05^(1/seeded) if all were caught*].

**G · On failure.** Keep Part 1's four lines. Where a published correction goes in your project: [*the page, the description field or the changelog where corrections are listed with date and reason*].

**H · Log.** Where it lives: [*the file, e.g. records/verification-log.md*]. One line per check, in Part 1's form.

**I · Verifiability test.** For each task you are thinking of delegating:

| Task | 1 · Checkable claims or a pass/fail check? | 2 · Checkable by a context that did not do it? | 3 · Checking cheaper than doing? | 4 · Residual risk acceptable and errors visible? | Verdict |
|---|---|---|---|---|---|
| [*the task, from your BW2 routing table*] | [*yes/no, and what the check is*] | [*yes/no, and what the checker needs*] | [*yes/no, with your estimate of each, in minutes*] | [*yes/no, with the tier and its bound*] | [*delegate and sample · delegate and check in full · restructure · keep*] |

**J · Done-when line for your spec** (BW5, 2b): replace the blank "a review by a context that did not do the work: BW6 sets how" with: A context that did not do the work has checked [*the unit*] by step E ([*census, or tier and n*]), the checker re-checked by step F, and the result logged by step H.

## Sources

All web sources read 16 November 2026 unless marked; product facts carried from BW2 are as BW2 read them on 15 November 2026.

- Abboud, C. J. *"The Environment and Disease: Association or Causation?" (1965), by Austin Bradford Hill*. Embryo Project Encyclopedia, 23 March 2017. https://embryo.asu.edu/pages/environment-and-disease-association-or-causation-1965-austin-bradford-hill
- Anthropic. *Best practices for Claude Code*. Claude Code documentation (vendor). https://code.claude.com/docs/en/best-practices?ref=t01.li
- Anthropic. *Claude can now connect to your world*. 1 May 2025 (vendor). https://claude.com/blog/integrations
- Claude Help Center. *Use research on Claude*. Undated ("Updated over 2 weeks ago" on 16 November 2026) (vendor). https://support.claude.com/en/articles/11088861-use-research-on-claude
- Google. *Subagents*. Gemini CLI documentation (vendor). https://geminicli.com/docs/core/subagents/
- Google. *Use Deep Research in Gemini Apps*. Gemini Apps Help, undated (vendor). https://support.google.com/gemini/answer/15719111
- Hadfield, J., Zhang, B., Lien, K., Scholz, F., Fox, J. and Ford, D. *How we built our multi-agent research system*. Anthropic Engineering, 13 June 2025 (vendor). https://www.anthropic.com/engineering/multi-agent-research-system
- Hill, A. B. *The Environment and Disease: Association or Causation?*. *Proceedings of the Royal Society of Medicine* 58(5), 1965, 295–300. https://pmc.ncbi.nlm.nih.gov/articles/PMC1898525/
- Lundh, A., Lexchin, J., Mintzes, B., Schroll, J. B. and Bero, L. *Industry sponsorship and research outcome*. Cochrane Database of Systematic Reviews (MR000033.pub3), 16 February 2017; read in Cochrane's summary page. https://www.cochrane.org/MR000033/METHOD_industry-sponsorship-and-research-outcome
- Magesh, V., Surani, F., Dahl, M., Suzgun, M., Manning, C. D. and Ho, D. E. *Hallucination-Free? Assessing the Reliability of Leading AI Legal Research Tools*. arXiv 2405.20362v1, 30 May 2024 (preprint version). https://arxiv.org/abs/2405.20362v1
- Manakul, P., Liusie, A. and Gales, M. *SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models*. Proceedings of EMNLP 2023, 9004–9017. https://aclanthology.org/2023.emnlp-main.557
- Newman, T. B. *If Almost Nothing Goes Wrong, Is Almost Everything All Right? Interpreting Small Numerators*. *JAMA* 274(13), 1995, 1013 (letter). https://jamanetwork.com/journals/jama/article-abstract/389714
- NIST/SEMATECH. *6.2.1. What is Acceptance Sampling?*. e-Handbook of Statistical Methods. https://itl.nist.gov/div898/handbook/pmc/section2/pmc21.htm
- OpenAI. *Web search*. OpenAI API documentation, reached at the deep-research guide's address (vendor). https://developers.openai.com/api/docs/guides/deep-research.md
- Rao, D., Wong, E. and Callison-Burch, C. *Detecting and Correcting Reference Hallucinations in Commercial LLMs and Deep Research Agents*. arXiv 2604.03173v1, 3 April 2026 (preprint). https://arxiv.org/abs/2604.03173
- Vu, T., Iyyer, M., Wang, X., Constant, N., Wei, J., Wei, J., Tar, C., Sung, Y.-H., Zhou, D., Le, Q. and Luong, T. *FreshLLMs: Refreshing Large Language Models with Search Engine Augmentation*. arXiv 2310.03214v2, 22 November 2023 (preprint). https://arxiv.org/abs/2310.03214
- Walters, W. H. and Wilder, E. I. *Fabrication and errors in the bibliographic citations generated by ChatGPT*. *Scientific Reports* 13, 14045, 2023. https://www.nature.com/articles/s41598-023-41032-5.pdf
- Wei, J., Karina, N., Chung, H. W., Jiao, Y. J. et al. *Measuring short-form factuality in large language models*. arXiv 2411.04368v1, 7 November 2024 (preprint; OpenAI). https://arxiv.org/pdf/2411.04368
- Academy case file, §1 to §9 (compiled 11 November 2026, with its later notes).
- Units of this course cited by section: BW1 (§1, §4, §5, §7); BW2 (§1, §4, §5, §6; routing table rows 5, 7 and 9; rule 4); BW3 (§3; Deliverable, the brief form and templates 3 and 9); BW5 (§10, §11; Deliverable 2b).

## Unsure list

1. OpenAI, *Web search* (§8 table, Sources): fetched at the address of OpenAI's deep-research guide (developers.openai.com/api/docs/guides/deep-research.md, returned by search), but the page's headline read "Web search"; the address may redirect within the site. The phrase "for reports that can take several minutes" was read through the fetch summary. OpenAI's deep-research help page and its deep-research announcement both refused the fetch (not checked, not retried).
2. Walters and Wilder (§2): the PDF read gives "(2023) 13:14045", received 11 July and accepted 21 August 2023, and no publication date; the unit cites the year only.
3. Lundh et al. (§3): read on the Chinese edition of Cochrane's summary page (headline 行业赞助和研究结局); the 75 papers, both risk ratios and the date match, but the English wording of the authors' conclusion was not read, so it is paraphrased, not quoted.
4. Hill 1965 (§3): the PMC page gives the citation and a scan only; the nine viewpoints and Hill's caveats (a causal relationship can exist when some do not apply; no exact rules) are taken from Abboud's Embryo Project summary, cited as such.
5. Magesh et al. (§2, §3): cited as the arXiv v1 preprint of 30 May 2024; whether and where it was later peer-reviewed was not checked. "between 17% and 33% of the time" and the vendors' claims (eliminating, avoiding, "hallucination-free") were read through the fetch summary of the abstract page.
6. Wei et al., SimpleQA (§2): the calibration quotation and the 38.2% and 28.9% figures were read through the fetch summary of the PDF; the description of how confidence was elicited (models asked to state it) is this unit's reading of the calibration section, not checked line by line.
7. Vu et al., FreshQA (§2): cited as arXiv v2 (22 Nov 2023); the venue of later publication was not checked; no accuracy figure is used, only the abstract's "struggle" finding and "substantially".
8. Hadfield et al. (§1): the 4× and 15× ratios and the 80% variance figure describe Anthropic's 2025 system (Opus 4 lead, Sonnet 4 subagents); whether they hold for Research on current models is stated nowhere read. The page's metadata shows a modification in October 2026; the figures were read as they stand on 16 Nov 2026.
9. Rao, Wong and Callison-Burch (§2): labelled a preprint; the HTML v1 read did not show the words "Preprint. Under review."; the 65% stale share is the paper's own (10.1% non-resolving, 3.5% hallucinated, for OpenAI's deep-research agent).
10. The tiers and their rates (30%, 20%, 10%), the acceptance number of zero, the five-PASS re-check, the three seeded errors, the early stop on invention and the STALE sweep are this unit's design (stated opinion); the sample sizes and bounds follow from them by arithmetic, but no source sets the rates. The Gemini CLI and OpenAI Codex entries in §8 are carried from BW5 §11 (read 15 Nov 2026) and were not re-read.
Object: none

Fresh check 2026-11-16 (Opus 5.5): fix · 1 errors, 7 should-fix, 3 minor; 12 applied, 1 held (f11, the search flag: the build order sets it off; raised as a flag); report `audits/building-with-ai/fresh-check-BW6.md`

Correction 2026-11-16, found by BW9's writer (corrections check `audits/building-with-ai/corrections-2026-11-16-BW9-BW6-BW8.md`, Changes 1 to 5: the page of Best practices for Claude Code, not its older .md copy).
