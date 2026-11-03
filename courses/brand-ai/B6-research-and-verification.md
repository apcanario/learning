---
code: B6
title: Research and verification
course: brand-ai · B · Using AI to Build a Brand
model: Opus 5.5
written: 2026-11-02
search: off
---

# B6 · Research and verification

Search was off for the writing of this unit; it was used only to check specific figures: the token and time figures for multi-agent research, the citation-fabrication rates, the industry-sponsorship meta-analysis, and the wording of the sources on causation, self-correction and zero numerators. Every web source was opened on 2 November 2026. Product facts already recorded by B1 and B2 are cited from those units with the date they were checked, and are not re-derived. Three kinds of evidence carry the unit, labelled where they appear: **peer-reviewed** work; **vendor** material (a company describing or measuring its own product, or a dataset from a company with an interest in the result); and **his record**, meaning the audit and fresh-check lines filed at the end of the course's own units, which anyone with the repository can open and nobody else can. The sampling arithmetic is shown in the text so it can be checked by hand.

## 1 · Ask, search or deep research

B1 §4 set out the three places an answer can come from: trained knowledge, retrieved material, and the conversation. The three ways of asking a question map onto them. Asking directly gets an answer from trained knowledge plus whatever is already in the window. Search adds retrieved pages. Deep research adds many retrieved pages, gathered by several agents at once. Each step up costs more tokens and produces more claims, and every claim produced is one he may have to check. The price of research therefore has two parts: the tokens to produce it, and his time to verify it.

### Ask directly

**When.** The answer is a concept, a mechanism or a method that was settled before June 2026, which is the reliable knowledge cutoff Anthropic listed on 28 October 2026 for Opus 5.5, Sonnet 5.5, Haiku 5.5 and Fable 5.1 (B1 §4). Also when the work is a transformation of material already in the window: drafting from his takes, reformatting, summarising a pasted document. In those jobs the window holds the facts and the model supplies structure (B2 §8, "Reformatting and triage").

**When not.** Anything after June 2026, and any specific number, name, date, quotation or citation he will publish, file or act on. B1 §4 showed why: a sentence from training and a sentence invented from nothing read the same, and only the presence of a source in the window tells them apart. §2 shows the rates.

**Cost.** Tokens only. As B2 recorded on 28 October 2026, a small task of an assumed 4,000 input and 1,500 output tokens costs about $0.046 on Opus 5.5 at API prices (B2 §5; the token counts are B2's assumption). On claude.ai the cost is drawn from his usage limit by message length and conversation length (B2 §2).

**Time.** No source read for this unit gives a figure.

**One guard.** Anthropic's hallucination guidance, which B3 §3 already put into his output contracts, applies here: give the model permission to say it does not know, ask for a quote or source behind each claim, and have it retract what it cannot support (B3 §3). A direct answer that names a source has named something to check, and nothing more.

### Search

**When.** One current fact, one rule, one price, or one citation that has to exist: a lookup with a single answer.

**Cost.** As B2 recorded on 28 October 2026, web search on the API costs $10 per 1,000 searches plus the tokens the results add (B2 §3), which is one cent a search by arithmetic. On claude.ai, tool use, web search and Research included, draws on his usage limit (B2 §2, citing Anthropic's usage-limit article of 22 September 2026). Anthropic's engineering team reports that agents, which call tools such as search in a loop, "typically use about 4× more tokens than chat interactions" ([Hadfield et al., *How we built our multi-agent research system*, Anthropic Engineering, 13 Jun 2025](https://www.anthropic.com/engineering/multi-agent-research-system); vendor, measured on Anthropic's 2025 systems, before the 5.5 family).

**Time.** No source read for this unit gives a figure.

**What it changes.** Search puts a page in the window, so the claim can point to something. The claim can still be false, and search adds a failure that asking directly lacks: the page may be stale, secondary or low quality. The same Anthropic post reports that human testers found early research agents "consistently chose SEO-optimized content farms over authoritative but less highly-ranked sources" until source-quality rules were added to their prompts (same post). §3 is the reading rule for what search brings back.

### Deep research

**What it is.** On claude.ai, Research runs "multiple searches that build on each other" and needs web search switched on; it is available on paid plans ([Claude Help Center, *Use research on Claude*](https://support.claude.com/en/articles/11088861-use-research-on-claude), read 2 Nov 2026, page dated only "Updated yesterday"). Anthropic built it as a multi-agent system: a lead agent plans and spawns subagents that search in parallel, and a separate citation agent attaches sources at the end (Hadfield et al., 13 Jun 2025; vendor).

**When.** Anthropic's own account of where the design fits: it excels at "breadth-first queries that involve pursuing multiple independent directions simultaneously"; tasks where all agents need to share the same context, or where the parts depend heavily on each other, "are not a good fit for multi-agent systems today"; and the design needs "tasks where the value of the task is high enough to pay for the increased performance" (same post). A landscape question (what does the evidence say about weekly volume for a sub-1:45 half, from three literatures at once) fits. A chain of questions where each depends on the last answer does not; that is search, one step at a time, in one chat.

**Cost.** Multi-agent systems "use about 15× more tokens than chats" (same post; vendor, measured on Anthropic's 2025 research system). The post also found that token usage by itself explained 80% of the variance in performance on the BrowseComp evaluation, with the number of tool calls and the choice of model as the two other factors (same post; vendor, an association across its runs). Whether the 15× ratio holds for Research as it runs today is not stated in any source read. On his plan, the help centre says research sessions "can use up your limits faster due to Claude retrieving multiple sources" (Help Center, read 2 Nov 2026), and gives no rate.

**Time.** Anthropic's launch post said Research delivers answers "in minutes" ([Anthropic, *Claude takes research to new places*, 15 Apr 2025](https://claude.com/blog/research)). At the next expansion Anthropic said Research delivers reports "in anywhere from five to 45 minutes", and that "most reports complete in five to 15 minutes" ([Anthropic, *Claude can now connect to your world*, 1 May 2025](https://claude.com/blog/integrations); vendor). TechCrunch carried the same range the same day without attributing it ([Wiggers, TechCrunch, 1 May 2025](https://techcrunch.com/2025/05/01/anthropic-lets-you-connect-apps-to-claude)). Both describe the 2025 feature; no 2026 figure was found.

**What it changes.** Deep research produces the most claims and the most citations, and §2 shows that the share of invented links rises with it. His own record has the clearest case: the research document behind A2, A6 and A9, written by Fable 5.1 research agents, failed 23 of 91 cited claims at Audit 1 on 28 October 2026 (B2 §8, citing Audit 1). That is 25% by arithmetic, from the dearer model, in a document that read as finished.

The three routes on one axis, from the Anthropic post's own figures:

```viz
{
 "kind": "compare",
 "title": "Tokens used, relative to a chat",
 "unit": "×",
 "max": 15,
 "rows": [
  {"label": "Chat", "value": 1, "tone": 3},
  {"label": "Agent with tools", "value": 4, "tone": 2},
  {"label": "Multi-agent research", "value": 15, "tone": 1}
 ],
 "caption": "Token use of an agent and of a multi-agent research system relative to a chat, §1, from Hadfield et al., <a href=\"https://www.anthropic.com/engineering/multi-agent-research-system\"><em>How we built our multi-agent research system</em></a>, Anthropic Engineering, 13 Jun 2025; vendor figures, measured on Anthropic's 2025 systems."
}
```

**The routing rule.** Put together: ask directly when nothing in the answer needs a source (a specific that turns up anyway is checked before use, Deliverable A); search when one answer needs one; deep research when several independent directions need covering and the result is worth roughly fifteen chats of tokens plus the checking of the claims it returns; when the directions depend on each other, search one step at a time, in one chat; when they are independent but the result is not worth that, search each direction in turn, one chat each (my rule). The rule is my synthesis of the sources above; each branch traces to one of them.

```viz
{
 "kind": "decision",
 "root": {
  "q": "Needs, from outside the chat, a fact after June 2026, or a specific number, name, date, quotation or citation he will publish, file or act on?",
  "tone": 4,
  "branches": [
   {
    "label": "no",
    "to": {
     "outcome": "Ask directly",
     "tone": 3
    }
   },
   {
    "label": "yes",
    "to": {
     "q": "Several directions to cover?",
     "tone": 4,
     "branches": [
      {
       "label": "no",
       "to": {
        "outcome": "Search",
        "tone": 2
       }
      },
      {
       "label": "yes",
       "to": {
        "q": "Are the directions independent of each other?",
        "tone": 4,
        "branches": [
         {
          "label": "no",
          "to": {
           "outcome": "Search, one step at a time, in one chat",
           "tone": 2
          }
         },
         {
          "label": "yes",
          "to": {
           "q": "Worth about fifteen chats of tokens plus checking its claims?",
           "tone": 4,
           "branches": [
            {
             "label": "no",
             "to": {
              "outcome": "Search each direction in turn, one chat each",
              "tone": 2
             }
            },
            {
             "label": "yes",
             "to": {
              "outcome": "Deep research",
              "tone": 1
             }
            }
           ]
          }
         }
        ]
       }
      }
     ]
    }
   }
  ]
 },
 "caption": "The routing rule in §1, this unit's synthesis of its sources: the cutoff from B1 §4; the fit conditions and the roughly fifteen-fold token cost from Hadfield et al., <a href=\"https://www.anthropic.com/engineering/multi-agent-research-system\"><em>How we built our multi-agent research system</em></a>, Anthropic Engineering, 13 Jun 2025 (vendor). Every route that ends in something published, filed or acted on then goes through the sampling rule (Deliverable C)."
}
```

The routing rule decides how to get an answer; whether to trust it is §4's question. Every route ends in the same place: anything that will be published, filed or acted on goes through the sampling rule argued in §4 (Deliverable C).

## 2 · How models fail

B1 §5 explained why one good answer is one draw. This section is about what the bad draws look like. They fall into three kinds, and each looks like a good answer.

### Confident, specific, wrong

A specific answer feels checked. Kalai and colleagues argue that hallucinations "originate simply as errors in binary classification" during pretraining, and persist because most benchmarks score answers in a way that rewards a guess over an admission of uncertainty: "guessing when uncertain improves test performance" ([Kalai, Nachum, Vempala and Zhang, *Why Language Models Hallucinate*, arXiv 2509.04664, 4 Sep 2025](https://arxiv.org/abs/2509.04664v1); preprint, not peer-reviewed). On that account, a model trained to score well is trained to produce a confident specific answer where the honest answer is "I do not know". Specificity is a property of the style, and carries no information about whether the content is true.

The rates are measurable and they vary. B2 §8 recorded Artificial Analysis's AA-Omniscience figures on 28 October 2026: the lowest hallucination rate among the models it listed was Gemini 4 Argon's, at 4% (third-party vendor data). The lowest is not zero, and B2 recorded no hallucination rate for the Claude models; the course has no measured rate for Opus 5.5 or Fable 5.1 on his kind of question.

### Stale facts presented as current

The model's knowledge stops in June 2026 (B1 §4), and nothing in the output marks which sentences depend on that. A price, a plan limit or a model lineup from before the cutoff comes out in the present tense. DD-B3 §1.1 quotes Karpathy's own build log on the same failure in code: the model "kept hallucinating deprecated APIs, model names, and input/output conventions" (DD-B3 §1.1; documented practice, one project).

Search can bring staleness in with the page. Rao, Wong and Callison-Burch checked the URLs that research systems cited on 100 benchmark queries (53,090 URLs by the abstract's count, though the ten systems' rows in its Table 1 sum to 23,269) and separated links that never existed from links that once existed and are now dead; for OpenAI's deep-research agent, about 65% of the non-resolving links had once existed and were now dead ([Rao, Wong and Callison-Burch, *Detecting and Correcting Reference Hallucinations in Commercial LLMs and Deep Research Agents*, arXiv 2604.03173, 3 Apr 2026](https://arxiv.org/pdf/2604.03173); preprint, under review, not peer-reviewed).

His record shows how fast "current" decays. B2 was written with search on 28 October 2026. Artificial Analysis had announced Intelligence Index v5.0 on 27 October; on the 28th its model page already carried the new figures while its leaderboard still showed the old ones, and by the next day the leaderboard had moved, so every Artificial Analysis figure in B2's §5, §7, §8 and deliverable had to be replaced; Audit 2 marked three of B2's nine sampled claims STALE (B2, Writer's unsure list, item 1 and the Audit 2 line). The claims were true when written; the index moved under them within a day.

### Invented citations

This is the failure the sourcing standard exists for. Walters and Wilder asked GPT-3.5 and GPT-4 for 84 literature reviews on 42 topics and checked all 636 citations: 55% of GPT-3.5's citations and 18% of GPT-4's were fabricated, and of the citations to works that do exist, 43% (GPT-3.5) and 24% (GPT-4) carried substantive errors. The authors note that fabricated citations "tend to look legitimate at first glance" ([Walters and Wilder, "Fabrication and errors in the bibliographic citations generated by ChatGPT", *Scientific Reports* 13, 14045, 7 Sep 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC10484980); peer-reviewed, 2023 models).

Search and deep research do not remove the problem. No study read for this unit compares the same models with and without search, so how much search lowers the rate is not measured here; Walters and Wilder counted invented works from 2023 models, and the Rao study below counts links that never existed, from later models. In the Rao study, pooled across the two deep-research agents tested, 10.7% of cited URLs were hallucinated (they returned an error and had no archived copy), against 4.8% for the eight search-augmented models; the deep-research agents also cited far more links per query (113.1 and 41.2, against 3.0 to 24.3) (Rao et al., 2026; preprint). The authors call their rates conservative lower bounds, and they record invented snippets and bibliographic details without counting them. The models tested were 2024 and 2025 releases (Gemini 2.5, GPT-4.1, Claude 3.5 and 3.7 Sonnet among them); no Claude deep-research agent was tested.

Two lessons for him. First, deep research produced more invented links per query than search, because it cited more links and a larger share of them were invented (10.7% against 4.8%). Second, a real citation can still be wrong. Walters and Wilder's real-but-wrong citations carried substantive errors in the citations themselves; the study did not test whether the works supported the text. That further failure, a real source reported as saying something it does not, is the one Audit 2 found in B2 §7: B2 set aside a "seven times" token figure on the ground that the Claude Code post labelled its curves illustrative, when the post labels only its two cost-curve charts that way and not the diagram that carries the figure; marked an incidental FAIL (B2, Audit 2 line and unsure item 10; `audits/brand-ai/audit-2.md`).

### The checker fails too

Each of the three failures can appear in a check as well as in a draft. Huang and colleagues found that models "struggle to self-correct their responses without external feedback", and that "their performance even degrades after self-correction" on reasoning tasks ([Huang et al., *Large Language Models Cannot Self-Correct Reasoning Yet*, ICLR 2024; arXiv 2310.01798](https://arxiv.org/abs/2310.01798v2); peer-reviewed). A check that re-reads the text without opening the sources is the same model drawing again. B2 §8 added the self-preference evidence: model evaluators favour their own outputs (Panickssery, Bowman and Feng, NeurIPS 2024, as cited in B2 §8).

His record has one checker error and one contested verdict. Audit 1 cited the authors of the *Frontiers in Communication* study by their given names, as A2 §3 had, where the journal's citation line gives their family names; A2 took an erratum on 2 November 2026 (A4 §2). The auditor repeated the citation error it was there to catch. And A9's writer recorded that Audit 1 said a 16% tier-up figure exists nowhere, while it is on Metricool's own page (A9, Writer's unsure list, item 1). Audit 1's own words are narrower: the research document gave the figure without a citation, and Audit 1 found it "on no vidIQ research page" (Audit 1, §4); A9's fresh check then confirmed Metricool's 16.01% at source (`audits/brand-ai/fresh-check-A9.md`). Each check was right about what it opened; the dispute is over what "exists nowhere" claimed, and the next audit is to settle it. A checking step's output is AI-written material, and it gets the same treatment as any other (§4, last part).

### What his record says about first drafts

Fourteen of the fifteen filed Brand + AI units carry a fresh-check line (B1 has none). Of those fourteen, eleven had at least one finding of error severity at their first fresh check: A1, A2, A4, A5, A6, A9, B2, B3, B5, B7 and DD-B3 (count from the fresh-check lines at the end of each unit; three of the fourteen checks, A5's, A7's and B7's, were run by Opus 5.5, with a Fable 5.1 check still owed). Those units were written with the sourcing standard in the brief, all by Opus 5.5, five of the eleven with live search (each unit's front matter). It is what B1 §5's mechanism leads one to expect: a careful first draw is usually close and rarely clean. *Note, 3 Nov 2026 (DD-B2 §2):* with the units filed since, twenty of the twenty-one filed units carry a fresh-check line and fifteen of the twenty had an error at their first check; nine of the twenty checks were run by Opus 5.5, all with a Fable 5.1 check owed.

## 3 · How to read a research report

A report from search or deep research is a list of claims, each attached to a source. Reading it well means grading each attachment before believing the claim. Four questions, in order.

### 1. What class of source is it?

The course's standard lists four acceptable classes, which B3 template 7 orders strongest first: peer-reviewed work; platform-official documentation or statements; large-sample vendor datasets, named, with sample size and date; and documented creator cases with verifiable numbers. Creator anecdotes are labelled as anecdote, and vendor and correlational data are labelled as such (`sourcing-standard.md` Part 2; the same list is the constraint block of B3 template 7). Anything else (a content-farm summary, a tool vendor's blog post with no sample, a forum thread) is a lead to a source, and is never the source.

The class does two jobs. It tells him how much weight the claim can carry, and it tells him whether the claim is the source's own or a report of someone else's. The sourcing standard keeps the reporter separate from the claim (`sourcing-standard.md` Part 1). This unit's own §1 has an example: the 5-to-45-minute figure for Research appears in TechCrunch's report without attribution, and is cited here to Anthropic's own announcement of the same day, which states it.

### 2. Who paid for it, and what do they sell?

Most large creator datasets in this course come from companies that sell tools or services to creators: vidIQ, Metricool and AIR Media-Tech (A9 §1). Their numbers may still be right; what the funding predicts is the direction of any error. The best measurement of this comes from medicine. A Cochrane review of 75 papers comparing industry-sponsored with non-industry studies found sponsored studies more likely to report favourable efficacy results (risk ratio 1.27, 95% CI 1.17 to 1.37) and favourable conclusions (1.34, 1.19 to 1.51), and concluded that "Our analyses suggest the existence of an industry bias that cannot be explained by standard 'Risk of bias' assessments" ([Lundh et al., *Industry sponsorship and research outcome*, Cochrane Database of Systematic Reviews, 16 Feb 2017](https://www.cochrane.org/MR000033/METHOD_industry-sponsorship-and-research-outcome); peer-reviewed). That evidence is about drug and device trials. Applying it to creator-tool vendors is my analogy; no study read for this unit measures sponsorship bias in creator analytics.

The practical reading follows A9 §1, which already does it: name the vendor, give the sample and the date, read the vendor's own methodology note for what the sample excludes (vidIQ's states its sample "is not random" and its groups were not matched), and look for survivor samples, which count only the channels that reached a milestone (A9 §1).

AI model benchmarks are vendor data in the same sense. B2 labelled Anthropic's launch tables "vendor" because a model maker reports its own model against rivals it chose (B2, opening paragraph).

### 3. Does the design support the verb?

A correlational finding supports "is associated with". It does not support "causes", "drives" or "leads to". A6 §1.3 gives the course's standard case: AIR Media-Tech found that channels going dark for 14 or more days three or more times a year got fewer views per video, and A6 reads it as association, which "may reflect the reasons they missed them" (A6 §1.3, Breaks; vendor, correlational). The same finding written as "breaks hurt your views" is a causal claim the data cannot carry.

Bradford Hill's 1965 paper remains the standard list of what moves an association towards causation: strength, consistency, specificity, temporality, biological gradient, plausibility, coherence, experiment and analogy. He was explicit about its limit: "None of my nine viewpoints can bring indisputable evidence for or against the cause-and-effect hypothesis and none can be required as a sine qua non" ([Hill, "The Environment and Disease: Association or Causation?", *Proceedings of the Royal Society of Medicine* 58(5), 1965, 295–300](https://pmc.ncbi.nlm.nih.gov/articles/PMC1898525/); quotation from the reprint at [aliquote.org](https://aliquote.org:443/pub/Hill_1965.pdf)). For his reading, three of the nine do most of the work. Temporality: did the cause come first? Gradient: does more of it go with more of the effect? Experiment: has anyone changed it on purpose and measured the result? A creator dataset usually answers the first two loosely and the third not at all. YouTube's Test & Compare, which A6 and B7 use for titles, is an experiment in that sense; a vendor's cadence table is an observation.

The verbs to watch in an AI-written report are the ones the model supplies: "drives", "boosts", "the key to", "proven". Each needs a design behind it. If the source is correlational, the sentence is rewritten with "is associated with" and labelled.

### 4. Is the claim what the source says, today?

Two checks close the reading. The claim must match the source, without a stretch: the figure, the sample, the date, the population, the qualifiers (`sourcing-standard.md` Part 1). And a fact that can change carries the date it was read, because a report produced on one day is a snapshot (§2, the B2 index change).

A report that passes all four questions on a sample of its claims can be used. §4 sets how big the sample is and what happens when it fails.

## 4 · The sampling rule, generalised

### His rule as it stands

`method.md` §6 runs a stratified-sample audit after every four units in a course family, on Fable 5.1, in a new chat. For each unit it lists the sections and draws one claim per section that carries a number, a named source, a mechanism or a recommendation; it records that sample before checking anything; it opens each cited source and marks each claim PASS, FAIL or STALE; and if more than one sampled claim in ten is FAIL, it audits that unit in full, every cited claim (`method.md` §6; `skills/audit-units/SKILL.md` §3). A source that cannot be opened is "unverifiable", never FAIL (`sourcing-standard.md` Part 1). Since Audit 1, every Brand + AI unit also gets a fresh check by a model that did not see it written, before filing (`skills/audit-units/SKILL.md` §3b).

Three design choices sit inside that rule, and each one generalises.

- **Strata.** One claim per section guarantees that every part of the unit is looked at. Errors cluster: one bad source feeds every claim drawn from it, and one stale index moved B2's figures in three sections and the deliverable at once (§2). A simple random sample of the same size can miss whole sections; a stratified sample cannot.
- **The sample is recorded before checking.** That stops the checker from swapping a claim that turned out hard for one that is easy.
- **The sample decides.** It is a trigger. A sample that fails sends the whole unit to a full check; a sample that passes lets the rest stand.

### What a sample can and cannot detect

The arithmetic is short. Suppose a fraction *p* of a piece's checkable claims would FAIL, and the sampled claims behave like independent draws. The chance that a sample of *n* claims contains no FAIL is (1 − *p*)ⁿ. Worked out:

| Claims sampled | No FAIL seen, if 10% would fail | No FAIL seen, if 25% would fail |
|---|---|---|
| 7 | 47.8% | 13.3% |
| 10 | 34.9% | 5.6% |
| 20 | 12.2% | 0.3% |
| 30 | 4.2% | 0.0% |

(0.9⁷ = 0.478; 0.75⁷ = 0.133; and so on: arithmetic, no source needed.)

```viz
{
 "kind": "bars",
 "mode": "grouped",
 "title": "Chance a sample shows no FAIL",
 "unit": "%",
 "max": 100,
 "decimals": 1,
 "series": [
  {"name": "If 10% would fail", "tone": 4},
  {"name": "If 25% would fail", "tone": 1}
 ],
 "rows": [
  {"label": "7 claims", "values": [47.8, 13.3]},
  {"label": "10 claims", "values": [34.9, 5.6]},
  {"label": "20 claims", "values": [12.2, 0.3]},
  {"label": "30 claims", "values": [4.2, 0.0]}
 ],
 "caption": "The table in §4: the chance that a sample of n claims contains no FAIL when 10% or 25% of the piece's claims would fail, computed as (1 − p)ⁿ. Arithmetic in this unit; 25% is the rate of the research document at Audit 1 (B2 §8)."
}
```

Read the two columns against his record. The research document failed at about 25% (§1). A one-per-section sample of seven, the size of B1's at Audit 1, would have missed a document that bad about one time in eight (13.3%). A piece failing at 10% gets past a sample of seven about half the time (47.8%). The rule catches bad pieces and lets moderately flawed ones through.

The same arithmetic run backwards says what a clean sample proves. If *n* claims all pass, the largest failure rate still consistent with that at 95% confidence is the *p* where (1 − *p*)ⁿ = 0.05, so *p* = 1 − 0.05^(1/*n*). For a clean 7 that is 34.8%; for a clean 10, 25.9%; for 20, 13.9%; for 30, 9.5%. The shortcut 3/*n* gives nearly the same figure once *n* is about 30 or more; this is the rule of thumb for zero numerators that Newman credits to Hanley and Lippman-Hand: when zero events occur in N trials, the upper 95% limit is roughly 3/N ([Newman, "If Almost Nothing Goes Wrong, Is Almost Everything All Right?", *JAMA* 274(13), 1995, 1013](https://jamanetwork.com/journals/jama/article-abstract/389714)). Audit 2 sampled 28 claims across B2, B3, B4 and A1 (9, 6, 6 and 7) and found no FAIL among them (each unit's Audit 2 line). On the arithmetic, that is consistent with a failure rate of up to about 10% across the four units (1 − 0.05^(1/28) = 10.1%; 3/28 = 10.7%). It was also consistent with the one FAIL Audit 2 found outside its sample, B2's miscited "seven times" (§2).

Two limits on that arithmetic. A stratified sample of one claim per section differs from a simple random sample, so the figures are a guide to its power and give no exact property of it. And the threshold "more than one in ten" behaves differently by sample size: with fewer than ten claims sampled, one FAIL is already more than one in ten (1 of 7 is 14%), so in practice any FAIL triggers a full check; at ten to nineteen it takes two.

So a sample is a tripwire for bad pieces. A clean sample is permission to proceed with a known residual risk, and it certifies nothing.

### Generalising the rule beyond course units

Everything AI-written that he publishes, files or acts on has checkable claims, in the sourcing standard's sense: any sentence carrying a number, a date, a named source, an attribution, a mechanism or a recommendation (`sourcing-standard.md`, opening). The rule generalises in four moves. The thresholds below are my design, chosen with the arithmetic above; each says what it rests on.

**1. Count first. Small pieces are checked in full.** A caption, a title set, a weekly email or a post usually carries a handful of checkable claims. At ten or fewer, a census costs little more than a sample and leaves no residual risk, so every claim is checked. That covers most of Shōmen's copy and every title set.

**2. Tier by consequence.** A piece published under his name or filed as course material is tier **P**. A research note for himself, a draft, or a decision memo is tier **I**. The difference is what an error costs. Under his brand, published work changes only in the open: a corrected figure after publication is listed in the description with its date and reason (A4, Deliverable C, rule 2). A public error therefore stays public. Tier P triggers a full check on any FAIL; tier I keeps the method's "more than one in ten".

**3. Choose strata that match the piece.** Sections for long-form text, as the method does. Chapters for a script. For a research report, its source classes (§3), plus every sentence of its answer, which is short enough to check in full (B3 template 7 caps it at three sentences). For short pieces, the claim types: numbers, quotations, names and handles, dates, links. One claim per stratum, and extra draws from the largest strata until the sample reaches the minimum: 10 for tier P, 7 for tier I. On the table above, 10 catches a piece failing at 25% about nineteen times in twenty (1 − 0.056); 7 catches it about seven times in eight (1 − 0.133). Within a stratum, number the checkable claims and pick one by a random number, never by eye; record the sample before opening any source.

**4. Two outcomes end the sample early.** An invented source, quotation or number in the sample sends the piece to a full check at once, whatever the count. Invention is the failure the sourcing standard exists to stop, and at the rates in §2 (18% to 55% of citations in Walters and Wilder) one invented item found in a small sample is unlikely to be the only one; that inference is mine. And a STALE claim does not count as FAIL, but it triggers a sweep of every fact in the piece that can change, dated at the time of the sweep, because staleness comes from one moment of writing and hits all of that moment's facts together (B2's index change, §2).

### Checking a checking step

B2's routing table says "Never trust a single run on anything that will be published or filed. Sample its claims against the sources first" (B2, Rules for using the table). A check is a run. Its verdicts are claims ("this figure matches the source"), and §2 showed checkers erring in his own audits. The method already holds half of the answer: errata are applied as exact replacements, "each checked before it is applied" (`method.md` §6, After an audit). The generalisation adds the other half.

- **Every FAIL and STALE verdict is re-opened before its fix is applied.** That is the method's rule as written. A wrong FAIL applied as an erratum would put an error into a unit that was right.
- **A sample of PASS verdicts is re-opened too:** three, or one in five, whichever is more. A wrong PASS lets an error through silently, which is the failure Audit 1 showed when it repeated A2's miscited author names.
- **The re-check opens the source.** Re-reading the checker's report proves nothing, for the reason Huang and colleagues measured: without external feedback, a model's second look at its own reasoning does not reliably improve it, and sometimes makes it worse (§2).
- **One wrong verdict in the re-check discredits the whole report** for the claims of that kind: the remaining verdicts of that kind are re-opened, or the check is run again by a model that has seen neither the piece written nor the first check (B4 §4, item 4; B2 §8).

The same logic covers B1 §5's point about draws, when there is no source to open at all. SelfCheckGPT showed that when a model hallucinates a fact, "stochastically sampled responses are likely to diverge and contradict one another" ([Manakul, Liusie and Gales, *SelfCheckGPT*, EMNLP 2023, 9004–9017](https://aclanthology.org/2023.emnlp-main.557); peer-reviewed, tested on GPT-3 biographies). DD-B3's operating rule 10 already asks for this on any figure or verdict that matters: run it twice independently and compare (DD-B3, Deliverable B). Asking the same factual question in two or three fresh chats is a cheap screen: if the specific answers differ, the fact is treated as invented until a source is found. Agreement between draws raises confidence and proves nothing; the paper reports better detection than its baselines and stops well short of perfect, and a claim that will be published still needs its source.

## Deliverable · Verification protocol

Use for anything AI-written that will be published, filed or acted on: posts, captions, titles, scripts, emails, research notes and reports, decision memos, and a checking step's own output. Course units already have their own path (the `write-unit` skill, which B5's test set expects "Write unit B6." to fire; a Fable 5.1 fresh check before filing; the four-unit audit in `method.md` §6); this protocol is that audit generalised, and its re-check rule (E) also applies to the units' fresh-check and audit reports. Section references point to the evidence in this unit.

### A · Route the job before asking

| Job | Route | Cost, dated | Time | Then |
|---|---|---|---|---|
| A concept or mechanism settled before June 2026; drafting, reformatting or summarising material already in the chat | Ask directly | Tokens only. B2 §5: about $0.046 on Opus 5.5 for an assumed 4,000 in / 1,500 out (API prices, 28 Oct 2026). On claude.ai, drawn from his limit by message and conversation length (B2 §2) | No source gives a figure | Any number, name, date or quotation it gives is checked in full (C1) before use |
| One current fact, price, rule or citation | Search | $10 per 1,000 searches plus the result tokens on the API (B2 §3, 28 Oct 2026); tool use draws his claude.ai limit (B2 §2); an agent with tools uses about 4× a chat's tokens (Anthropic, 13 Jun 2025; vendor) | No source gives a figure | Open the cited page yourself; date the fact |
| Several independent directions at once, worth a report | Deep research (Research) | About 15× a chat's tokens (Anthropic, 13 Jun 2025; vendor, 2025 system); "can use up your limits faster" (Claude Help Center, read 2 Nov 2026) | "In minutes" (Anthropic, 15 Apr 2025); 5 to 45 minutes, most in 5 to 15 (Anthropic, 1 May 2025; vendor, 2025 feature) | Sampling rule (C) on the whole report; brief it with B3 template 7 |
| Several independent directions, not worth a report | Search each direction in turn, one chat each | As search, once per direction | As search, once per direction | As search |
| Several directions that each need the others' findings | Search, one step at a time, in one chat | As search | As search | As search |

- [ ] I asked for a source behind each claim and gave permission to say "I do not know" (B3 §3).
- [ ] For deep research, I accepted that its output carries more claims to check than a search answer (§1, §2).

### B · Before checking anything

- [ ] **List the checkable claims:** every sentence with a number, a date, a named source, an attribution, a mechanism or a recommendation. Count them (N).
- [ ] **Set the tier.** **P:** published under my name, or filed as course material. **I:** internal (my notes, drafts, memos, a decision I act on privately).
- [ ] **Set the strata:**
  - long-form text: sections;
  - script: chapters;
  - research report: its source classes, plus every sentence of its answer (all checked);
  - caption, post, title set, email: claim types (numbers, quotations, names and handles, dates, links);
  - a checker's report: see E.

### C · The sampling rule

- [ ] **C1 · Census if small.** If N is 10 or fewer, check every claim by D, give each a verdict as in C5, and decide as in C6; skip C2 to C4. A census has already checked every claim, so where C6 says full check it goes straight to F.
- [ ] **C2 · Sample size.** One claim per stratum; then extra draws from the largest strata until the sample is at least **10 (tier P)** or **7 (tier I)**.
- [ ] **C3 · Draw.** Within each stratum, number its claims and pick by a random number. Never pick by eye.
- [ ] **C4 · Record the sample** (claim, stratum, cited source) before opening any source.
- [ ] **C5 · Check each sampled claim** by D, and give it one verdict:
  - **PASS**: the source holds it.
  - **FAIL**: wrong, unsupported, miscited, stretched or invented.
  - **STALE**: true when written, superseded now; note the newer value and its source.
  - **Unverifiable**: the source cannot be opened. Not a FAIL. Replace it in the sample with another claim from the same stratum; if the claim stays in the piece, it is marked unsourced or removed.
- [ ] **C6 · Decide:**
  - an **invented** source, quotation or number in the sample → **full check**, at once;
  - **tier P** and any FAIL → **full check**;
  - **tier I** and more than one FAIL in ten sampled (with fewer than 10 sampled, any FAIL) → **full check**;
  - **tier I** and FAILs at or under one in ten, with ten or more sampled → fix each FAIL by D, then use it, and log it, after the sweep below if there is any STALE (`method.md` §6: at or under one in ten, no full audit, and the errata are applied);
  - any **STALE** → **sweep**: re-check and date every fact in the piece that can change (prices, rules, limits, lineups, benchmarks), then use it, and log it, unless a line above sends it to a full check;
  - **all PASS** → use it, and log it.
- [ ] **C7 · Remember what a clean sample means.** A clean 7 is consistent with up to about 35% failing; a clean 10, up to about 26%; a clean 30, up to about 10% (§4, 1 − 0.05^(1/n)). It is permission to proceed with known risk, and certifies nothing.

```viz
{
 "kind": "decision",
 "root": {
  "q": "Anything invented, or a FAIL over the tier's line (P: any; I: more than one in ten, any under 10 sampled)?",
  "tone": 4,
  "branches": [
   {
    "label": "yes",
    "to": {
     "outcome": "Full check",
     "tone": 1
    }
   },
   {
    "label": "no",
    "to": {
     "q": "Any STALE?",
     "tone": 4,
     "branches": [
      {
       "label": "yes",
       "to": {
        "outcome": "Sweep, fix any FAIL, use it and log it",
        "tone": 2
       }
      },
      {
       "label": "no",
       "to": {
        "outcome": "Fix any FAIL, use it and log it",
        "tone": 3
       }
      }
     ]
    }
   }
  ]
 },
 "caption": "Rule C6 of the Deliverable read as two questions: what each sample result triggers. Generalised from the stratified-sample audit in <code>method.md</code> §6 (more than one in ten FAIL, full audit; at or under one in ten, the errata are applied) with the tier and early-stop rules argued in §4 of this unit."
}
```

### D · Checking one claim

- [ ] Open the cited source myself. A claim with no source is FAIL in tier P and unsourced in tier I.
- [ ] The source exists, and says this: the same figure, sample, date, population and qualifiers. No stretch (§3, question 4).
- [ ] The source is the original, cited for its own words; a report of it by someone else is kept separate (§3, question 1).
- [ ] The source class is acceptable and labelled: peer-reviewed; platform-official; named large-sample vendor dataset with size and date; documented case with verifiable numbers; anecdote labelled as anecdote (§3, question 1).
- [ ] Vendor and correlational data are labelled; a correlational source carries "is associated with", never "causes", "drives" or "boosts" (§3, questions 2 and 3).
- [ ] A fact that can change carries the date I read it.
- [ ] Words in quotation marks are the source's exact words.

### E · Checking a checking step's output

A checker's report is AI-written. Its verdicts are its claims.

- [ ] Re-open the source behind **every FAIL and STALE** before applying its fix.
- [ ] Re-open the source behind a sample of **PASS** verdicts: three, or one in five, whichever is more, drawn as in C3.
- [ ] Re-check against the source, never against the checker's wording (§2, Huang et al.).
- [ ] **One wrong verdict** in the re-check: re-open every remaining verdict of that kind, or run the check again with a model that saw neither the piece written nor the first check (B4 §4; B2 §8).
- [ ] With no source to open at all, ask the same factual question in two or three fresh chats. Different specific answers: treat the fact as invented until sourced. Same answers: still find the source before publishing (§4, SelfCheckGPT).

### F · On failure

- [ ] **Full check:** every checkable claim, by D. Fix each FAIL as an exact replacement, checked before it is applied (`method.md` §6).
- [ ] **More than three FAILs in the full check:** rewrite from the brief in a new chat, as a fresh check's "rewrite" verdict does (`skills/audit-units/SKILL.md` §3b).
- [ ] **Already published:** correct it in the open, with the date and the reason in the description (A4, Deliverable C, rule 2). The error stays in the record.
- [ ] **The same kind of task fails twice in a month:** change the brief or the route (B2, Rules for using the table; DD-B3, operating rule 6).

### G · Log

- [ ] One line per check: date · piece · tier · N · sampled · PASS / FAIL / STALE / unverifiable · decision (C6) · what changed.

## Sources

All web sources opened 2 November 2026.

- Hadfield, J., Zhang, B., Lien, K., Scholz, F., Fox, J. and Ford, D. *How we built our multi-agent research system*. Anthropic Engineering, 13 June 2025 (vendor). https://www.anthropic.com/engineering/multi-agent-research-system
- Anthropic. *Claude takes research to new places*. 15 April 2025 (vendor). https://claude.com/blog/research
- Claude Help Center. *Use research on Claude* (article 11088861). Read 2 November 2026; the page is dated only "Updated yesterday". https://support.claude.com/en/articles/11088861-use-research-on-claude
- Wiggers, K. "Anthropic lets you connect apps to Claude". TechCrunch, 1 May 2025 (secondary report). https://techcrunch.com/2025/05/01/anthropic-lets-you-connect-apps-to-claude
- Anthropic. *Claude can now connect to your world*. 1 May 2025 (vendor). https://claude.com/blog/integrations
- Kalai, A. T., Nachum, O., Vempala, S. S. and Zhang, E. *Why Language Models Hallucinate*. arXiv 2509.04664, 4 September 2025 (preprint). https://arxiv.org/abs/2509.04664v1
- Walters, W. H. and Wilder, E. I. "Fabrication and errors in the bibliographic citations generated by ChatGPT". *Scientific Reports* 13, 14045, 7 September 2023. doi:10.1038/s41598-023-41032-5. https://pmc.ncbi.nlm.nih.gov/articles/PMC10484980
- Rao, D., Wong, E. and Callison-Burch, C. *Detecting and Correcting Reference Hallucinations in Commercial LLMs and Deep Research Agents*. arXiv 2604.03173, 3 April 2026 (preprint, under review). https://arxiv.org/pdf/2604.03173
- Huang, J., Chen, X., Mishra, S., Zheng, H. S., Yu, A. W., Song, X. and Zhou, D. "Large Language Models Cannot Self-Correct Reasoning Yet". ICLR 2024. arXiv 2310.01798. https://arxiv.org/abs/2310.01798v2
- Manakul, P., Liusie, A. and Gales, M. "SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models". *Proceedings of EMNLP 2023*, 9004–9017. https://aclanthology.org/2023.emnlp-main.557
- Lundh, A., Lexchin, J., Mintzes, B., Schroll, J. B. and Bero, L. *Industry sponsorship and research outcome*. Cochrane Database of Systematic Reviews 2017, Issue 2 (MR000033.pub3), 16 February 2017. https://www.cochrane.org/MR000033/METHOD_industry-sponsorship-and-research-outcome
- Hill, A. B. "The Environment and Disease: Association or Causation?". *Proceedings of the Royal Society of Medicine* 58(5), 1965, 295–300. https://pmc.ncbi.nlm.nih.gov/articles/PMC1898525/ · quotation taken from the reprint in Greenland (ed.), *Evolution of Epidemiologic Ideas* (1987), 7–12: https://aliquote.org:443/pub/Hill_1965.pdf
- Newman, T. B. "If Almost Nothing Goes Wrong, Is Almost Everything All Right? Interpreting Small Numerators". *JAMA* 274(13), 1995, 1013 (letter, building on Hanley and Lippman-Hand, *JAMA* 249(13), 1983, 1743–1745). https://jamanetwork.com/journals/jama/article-abstract/389714
- Learning Project files cited by name: `docs/method.md` §6; `docs/sourcing-standard.md` Parts 1 and 2; `skills/audit-units/SKILL.md` §3 and §3b.
- Filed units cited by section: A4 · Voice, disclosure and the record (§2; Deliverable C, rule 2); A6 · How growth works per platform (§1.3, Breaks); A9 · What to expect: benchmarks (§1; Writer's unsure list, item 1); B1 · Mental model (§4, §5); B2 · Choosing the model (§2, §3, §5, §8; Rules for using the table; Writer's unsure list and audit lines); B3 · Prompting that holds up (§3; template 7); B4 · Context engineering (§4); B5 · Skills and automation (Deliverable C, test set); DD-B3 · Deep dive: how the best practitioners use the tool (§1.1; Deliverable B, operating rules 6 and 10); the fresh-check lines at the end of A1, A2, A3, A4, A5, A6, A7, A9, B2, B3, B4, B5, B7 and DD-B3.

## Writer's unsure list

1. **Research's running time.** The 5-to-45-minute range and "most reports complete in five to 15 minutes" are Anthropic's figures for the 2025 feature (1 May 2025, found by the fresh check of 2 November 2026); TechCrunch carried the range the same day without attribution. No current (2026) figure was found.
2. **The 4× and 15× token ratios** were reported by Anthropic for its 2025 system (the post's internal evaluation used an Opus 4 lead with Sonnet 4 subagents; which configuration the token ratios come from is not stated). Whether they hold for Research as it runs on the 5.5 family is not stated anywhere read.
3. **No time figure exists** in the sources read for asking directly or for a single search; the Deliverable says so in place of a number.
4. **The Rao, Wong and Callison-Burch rates** come from a preprint under review, on models released in 2024 and 2025; no Claude deep-research agent was in its sample (a "claude-research" entry was excluded for returning one URL). The abstract gives 53,090 URLs for the ten systems; the ten rows of its Table 1 sum to 23,269, and the paper does not explain the gap. The 65% stale share is read from the paper's own breakdown.
5. **Kalai et al.** is a preprint; its account of why hallucinations persist is an argument with supporting analysis, cited as such.
6. **The sponsorship-bias analogy** from Lundh et al. (medical trials) to creator-tool vendors is mine; no study read measures sponsorship bias in creator analytics.
7. **The Hill quotation** was read in the 1987 Greenland reprint; the PMC page of the 1965 original gave metadata only.
8. **The thresholds of the generalised rule** (census at 10 or fewer, minimum samples of 10 and 7, the PASS re-check of three or one in five, the early stop on an invented claim) are my design, argued from the arithmetic in §4 and his method; no source sets them.
9. **The count of eleven units out of fourteen** with an error-severity finding at fresh check is from the lines filed at the end of each unit; three of the fourteen checks (A5, A7, B7) were run by Opus 5.5 with a Fable 5.1 check owed, and the two models' severity scales may differ.
10. **Audit 1's Metricool finding** is contested by A9's writer and not yet settled by an audit; this unit reports it as the writer's record.

Fresh check 2026-11-02 (Opus 5.5; a Fable 5.1 fresh check is owed): fix · 3 errors, 8 should-fix, 12 minor; all applied; report `audits/brand-ai/fresh-check-B6.md`.
