---
code: DD-BW1
title: Deep dive: how the best practitioners work
course: building-with-ai · BW · Building with AI
model: Opus 5.5
written: 2026-11-16
search: on
---

# DD-BW1 · Deep dive: how the best practitioners work

Every source in this unit was found by a web search and opened, or tried, on 16 November 2026, at the address the search returned. A page that refused the fetch, redirected elsewhere or did not come up in a search is marked "not checked" and was not retried from a copy. Each method carries one of the three grades this course uses (BW9 opening): **measured** (a study or test that reports numbers), **documented practice** (a named person or vendor describing what they do, with something you can inspect) and **stated opinion** (a named person's view, with nothing inspectable behind it). A study's finding names its models and task; carrying it to a current model or to your work is this unit's inference, and is said to be.

**Two limits, stated once.** Andrej Karpathy publishes much of his practice as posts on X, and no X page was opened for this unit; where a post matters, it is read through a reproduction that prints his words (Simon Willison's blog, Thread Reader App) and the reproduction is named. His keynote at Y Combinator's AI Startup School was not watched; its quotations rest on a third-party automatic transcription, labelled where used.

**Interests.** This unit was written by an Anthropic model. Three of its methods are Anthropic's own documents, one new item reviews an Anthropic model, and Karpathy started at Anthropic, on its pre-training team, in the week of 19 May 2026, and is to start a team using Claude to accelerate pre-training research ([Bellan and Franceschi-Bicchierai, TechCrunch, 19 May 2026](https://techcrunch.com/2026/05/19/openai-co-founder-andrej-karpathy-joins-anthropics-pre-training-team/), read 16 Nov 2026). Every Karpathy source below predates the move, except possibly the nanochat README, read in its current form (its policy carries no date). Nothing was weighted to favour Anthropic; you should still know.

The ten core units are assumed. What a window holds is BW1; routing by model and effort, BW2; the brief, BW3; project layout, BW4; the spec, BW5; sampling and the fresh checker, BW6; pipelines, BW7; skills, BW8; agents and their decision rule, BW9; usage and privacy, BW10. This unit points to them by code and does not restate them.

## 1 · Andrej Karpathy, from his own words

The rule for this section: a practice is attributed to him only where his own post, talk, repository or interview states it, read on the day.

### 1.1 · Vibe coding (February 2025)

His post, as Willison reproduces it in full: "There's a new kind of coding I call 'vibe coding'", where you "forget that the code even exists"; "I 'Accept All' always, I don't read the diffs anymore"; and the scope, "It's not too bad for throwaway weekend projects" ([Willison, *Not all AI-assisted programming is vibe coding (but vibe coding rocks)*, 19 Mar 2025](https://simonwillison.net/2025/Mar/19/vibe-coding/), read 16 Nov 2026). Willison dates the coinage 6 February; the post's X status number decodes to 2 February 2025 (this unit's arithmetic on X's public ID format, not a published source).

Karpathy then tested it on a small web app. "100% of the code was written by Cursor+Claude"; Claude "kept hallucinating deprecated APIs, model names, and input/output conventions"; his verdict: vibe coding full web apps "is kind of messy and not a good idea for anything of actual importance" ([Karpathy, *Vibe coding MenuGen*, 27 Apr 2025](https://karpathy.bearblog.dev/vibe-coding-menugen/), read 16 Nov 2026).

- **Claim:** for throwaway work you can accept every change unread and steer by results.
- **Evidence:** his own weekend practice, and one project written up. Grade: stated opinion, with one documented project.
- **Written for:** programmers building prototypes.
- **Transfer:** to a script you will delete, whose output you can see is right (BW9 §3). It does not transfer to anything you file, publish or send, on his own verdict.

### 1.2 · The autonomy slider, the leash, the verification loop (June 2025)

From his keynote at Y Combinator's AI Startup School, San Francisco, 16–17 June 2025 ([Y Combinator, *Join us at AI Startup School — June 16-17*](https://www.ycombinator.com/blog/ai-startupschool), read 16 Nov 2026; the day of his talk was not found), as a third-party automatic transcription prints it ([*Andrej Karpathy: Software Is Changing (Again) - transcription by yt-transcribe*](https://cdn.billmill.org/static/yt-transcribe/karpathy/httpswwwyoutubecomwatchvLCEmiRjPEtQ.html), read 16 Nov 2026; the recording was not watched):

- In a coding tool that ranges from completing a line to changing a repository, "you are in charge of the autonomy slider".
- "usually they are doing the generation and we as humans are doing the verification", and "It is in our interest to make this loop go as fast as possible"; a visual interface helps people verify faster.
- "we have to keep the AI on the leash"; his own habit: "I always go in small incremental chunks".
- Context windows are "kind of like working memory".

Grade: stated opinion, from long engineering practice. Written for: people building AI products. Transfer: whole. The slider is how much of a task you hand over, decided per task; the loop says your checking speed limits the whole system; the leash is BW3's one output per brief. BW9 §2 already teaches the slider and the leash from the same talk.

### 1.3 · Context engineering (June 2025)

His post, quoted by Willison: "+1 for 'context engineering' over 'prompt engineering'", because in a real application the skill is "the delicate art and science of filling the context window", which involves task descriptions, few-shot examples, retrieved and related data, tools, state, history and compacting. He was agreeing with Tobi Lütke, who wrote that the term "describes the core skill better" ([Willison, *Context engineering*, 27 Jun 2025](https://simonwillison.net/2025/Jun/27/context-engineering/), read 16 Nov 2026). Grade: stated opinion. Written for: people building LLM applications (his "industrial-strength LLM app"). Transfer: complete. BW1 and BW4 are built on the idea, from Anthropic's version of it (§2.2).

### 1.4 · Agents on his own code (October 2025, then January 2026)

**October 2025.** On the Dwarkesh Podcast he called autocomplete "my sweet spot" and said agents failed on his nanochat repository: it is "a fairly unique repository", and the models had "too much memory from all the typical ways of doing things"; they were "way too over-defensive". His verdict: "It's just not net useful." Agents did well on boilerplate and on a Rust port of code he already had in Python, with tests. He called the period "the decade of agents" ([Dwarkesh Patel, *Andrej Karpathy — AGI is still a decade away*, 17 Oct 2025](https://dwarkesh.com/p/andrej-karpathy), read 16 Nov 2026). Grade: documented practice, one codebase, his own account.

**January 2026.** Three months later his thread of 26 January reported that he went from about 80% manual coding (with autocomplete) and 20% agents in November 2025 to about 80% agent coding and 20% edits and touch-ups in December 2025, the "biggest change to my basic coding workflow" in about two decades (reproduced on [Thread Reader App](https://threadreaderapp.com/thread/2015883857489522876.html), read 16 Nov 2026; the X post itself was not opened). The same thread gives the method and its failure list, in his words:

- For any code you care about, he would "watch them like a hawk."
- Models "make wrong assumptions on your behalf and just run along with them without checking"; "they don't seek clarifications, they don't surface inconsistencies"; they are "still a little too sycophantic"; "they bloat abstractions"; "they don't clean up dead code after themselves"; one construction of 1,000 lines came down to "100 lines" when questioned.
- "Don't tell it what to do, give it success criteria and watch it go." "Change your approach from imperative to declarative".
- "Generation (writing code) and discrimination (reading code) are different capabilities in the brain", and "I am slowly starting to atrophy my ability to write code manually".

```viz
{"kind": "bars", "mode": "grouped", "unit": "%", "max": 100, "series": [{"name": "Manual", "tone": 4}, {"name": "Agents", "tone": 3}], "rows": [{"label": "November 2025", "values": [80, 20]}, {"label": "December 2025", "values": [20, 80]}], "caption": "Karpathy's own rough split of his coding between manual work and agents, before and after the shift he reported (§1.4). His figures, from his X thread of 26 January 2026 as reproduced on Thread Reader App, read 16 Nov 2026; the X post itself was not opened. A self-report about one person's work, not a measurement."}
```

Grade: stated opinion with a self-reported figure. Written for: professional programmers. Transfer, case by case:

- **The failure list transfers** with a change of vocabulary. An unchecked assumption built on is a figure taken from memory in a report; bloat is padding; dead code is a superseded paragraph left in place; not surfacing inconsistencies is two sections that disagree in silence. It becomes a checklist for whoever checks a draft (rule 3 of the Deliverable).
- **Success criteria transfer whole.** They are BW5's done-when lines and BW3's output contract.
- **Generation against discrimination** transfers as the reason a checker needs your own judgement and the sources (BW6 §4), and as a warning: if you only review, the skill of writing can fade. Karpathy reports it of himself; nothing here measures it.
- **The 80/20 shift is about code.** It says nothing about how much of a report a model should write.

### 1.5 · Verifiability (November 2025)

In a post of 16 November 2025, quoted by Willison, he argued that "the new most predictive feature to look at is verifiability": a task can be learned well by AI when its environment is "resettable (you can start a new attempt)", "efficient (a lot attempts can be made)" and "rewardable (there is some automated process to reward any specific attempt that was made)" ([Willison, *A quote from Andrej Karpathy*, 16 Nov 2025](https://feeds.simonwillison.net/2025/Nov/16/andrej-karpathy/), read 16 Nov 2026; his blog version of the essay did not come up in a search and was not checked). His subject is what models can be trained to do. Written for: anyone weighing which kinds of task AI will learn to do well (his "task/job"). Grade: stated opinion, built on an argument about training. Transfer: as a test of what to delegate, which is this course's inference and the one BW6 (Deliverable, step I) and BW9 §2 already draw. A citation can be checked against its source by a context that did not write it; a sentence of positioning cannot be checked by anything but your judgement.

### 1.6 · nanochat and autoresearch (October 2025 to March 2026)

**Disclosure.** nanochat's README sets its "Current AI policy: disclosure": a pull request must "declare any parts that had substantial LLM contribution" that the contributor did not write or does not fully understand ([karpathy/nanochat](https://github.com/karpathy/nanochat), README read 16 Nov 2026). Grade: documented practice (a policy in force on a public repository). Written for: contributors to the repository. Transfer: whole, to anything you hand to another person (§3.4).

**The autoresearch loop.** The README of [karpathy/autoresearch](https://github.com/karpathy/autoresearch) (read 16 Nov 2026; 36 commits shown, no commit date on the page) describes an agent that edits a small training setup, "trains for 5 minutes, checks if the result improved, keeps or discards, and repeats". Its guards:

- One editable file: `train.py` is "the single file the agent edits"; the file holding the data preparation and evaluation is not modified. The stated reason: "This keeps the scope manageable and diffs reviewable."
- A fixed budget per run: five minutes, so results are comparable whatever the agent changes, at about 12 experiments an hour and "approx 100 experiments while you sleep"; the cost, that results are not comparable with other people's hardware.
- An instruction file, `program.md`, which the README calls "essentially a super lightweight "skill"".

The result is on his own leaderboard. nanochat's README lists the wall-clock time a run takes to beat GPT-2's score on one 8-GPU node: entry 4 (4 March 2026, a change of dataset) at 2.02 hours, entry 5 (9 March) at 1.80 hours labelled "autoresearch round 1", entry 6 (14 March) at 1.65 hours, "autoresearch round 2" (README, read 16 Nov 2026). That is about 11% faster after round one and about 18% after round two (this unit's arithmetic on his figures).

```viz
{"kind": "compare", "unit": " h", "max": 3.5, "decimals": 2, "rows": [{"label": "#4 dataset change, 4 Mar", "value": 2.02, "tone": 4}, {"label": "#5 autoresearch round 1, 9 Mar", "value": 1.8, "tone": 2}, {"label": "#6 autoresearch round 2, 14 Mar", "value": 1.65, "tone": 2}], "caption": "Hours for a nanochat run to beat GPT-2's score, leaderboard entries 4 to 6, 4 to 14 March 2026 (§1.6). From the leaderboard in the README of karpathy/nanochat, read 16 Nov 2026: one project, one metric, his own record."}
```

Grade: documented practice with a self-reported, inspectable result; one task, one metric. Written for: machine-learning research with a number to optimise. Transfer: the loop needs three things most knowledge work lacks: a score a script computes, a run cheap enough to repeat a hundred times, and one file whose changes can be thrown away. A report has none of the three. A check script has all three: it passes or fails, runs in seconds, and lives in a file version control can revert. The loop transfers to the tooling around your writing; it does not transfer to the writing. The instruction file's stop rule was not re-read for this unit (`program.md` did not come up in a search), so nothing here says how the agent is told to stop.

### 1.7 · The LLM wiki (April 2026)

A gist he published on 4 April 2026 sets out a knowledge base a model writes and maintains ([Karpathy, *llm-wiki*, GitHub gist, created 4 Apr 2026](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f), read 16 Nov 2026):

- **Three layers.** Raw sources, which "are immutable — the LLM reads from them but never modifies them"; the wiki, model-written Markdown, where "The LLM owns this layer entirely"; and a schema, an instruction file "(e.g. CLAUDE.md for Claude Code or AGENTS.md for Codex)" that sets structure and conventions.
- **Three operations.** Ingest a source, which "might touch 10-15 wiki pages"; query, answering from the wiki; lint, which looks for "contradictions between pages, stale claims that newer sources have superseded", orphan pages and missing cross-references.
- **Navigation.** An `index.md`, "a catalog of everything in the wiki", read first, and a `log.md`, "an append-only record of what happened and when". At about a hundred sources this "avoids the need for embedding-based RAG infrastructure"; with retrieval, "the LLM is rediscovering knowledge from scratch on every question".
- **The human's part.** "You never (or rarely) write the wiki yourself."

Grade: documented practice (a method file anyone can copy); its scale is his own report. Written for: personal research. Transfer: the layers, the index, the log and the lint transfer to any project of documents, and BW4 already teaches their equivalents (one source of truth, §5; the rot check, §6). One part needs a change for work that others rely on: where claims must be checked, a model that rewrites filed pages at will erases the record of what was checked. Lint that reports, with changes applied as exact replacements you approve, keeps the gist's structure and the check (stated opinion). This course's running example, Academy (Academy case), runs it this way: its checker never edits, and each finding is applied as an exact replacement (Academy case file §2); one project, an anecdote.

### 1.8 · Two items not rebuilt

- **"How I use LLMs" (February 2025).** A two-hour video on his channel. Its page did not come up in a search; only third-party summaries and transcripts did. Nothing from it is used.
- **The Sequoia AI Ascent 2026 summary (April 2026).** The blog page on which he posted a model-written summary of his talk, separating vibe coding from "agentic engineering", did not come up in a search. The distinction is taken here from Willison's own definitions (§3.1), which say the same in his words.

## 2 · Vendors: Anthropic and OpenAI

### 2.1 · Building effective agents (Anthropic, December 2024)

Erik S. and Barry Zhang (the page's byline) separate workflows, where models and tools are "orchestrated through predefined code paths", from agents, which "dynamically direct their own processes and tool usage". The advice: "finding the simplest solution possible, and only increasing complexity when needed"; agents suit "open-ended problems where it's difficult or impossible to predict the required number of steps". Five workflow patterns: prompt chaining, routing, parallelization, orchestrator-workers, evaluator-optimizer ([*Building effective agents*, Anthropic Engineering, 19 Dec 2024](https://anthropic.com/engineering/building-effective-agents), read 16 Nov 2026). Grade: documented practice, vendor; no measurement published. Written for: developers building on the API. Transfer: the simplicity rule whole; the pattern names as a vocabulary for your own pipeline. BW7 §1 and BW9 §1 already use it.

### 2.2 · Effective context engineering for AI agents (Anthropic, September 2025)

Prithvi Rajasekaran, Ethan Dixon, Carly Ryan and Jeremy Hadfield of Anthropic's Applied AI team define context engineering as the "set of strategies for curating and maintaining the optimal set of tokens", aim for the "smallest possible set of high-signal tokens", and recommend loading by "lightweight identifiers" such as file paths, compaction, structured notes kept outside the window, and sub-agents "with clean context windows" that return a summary "often 1,000-2,000 tokens" long ([*Effective context engineering for AI agents*, Anthropic Engineering, 29 Sep 2025](https://anthropic.com/engineering/effective-context-engineering-for-ai-agents), read 16 Nov 2026). The page reports no benchmark. Written for: developers building agents. Grade: documented practice, vendor. Transfer: whole; BW1, BW3 and BW4 cite and apply it.

### 2.3 · Claude Code: best practices for agentic coding (Anthropic, April 2025)

Boris Cherny's post of 18 April 2025, now marked as no longer maintained, gives patterns that worked "both for Anthropic's internal teams and for external engineers" ([Cherny, *Claude Code: Best practices for agentic coding*, Anthropic, 18 Apr 2025](https://www.anthropic.com/research/claude-code-best-practices), read 16 Nov 2026):

- **Explore, plan, code, commit**, with the note that the first two steps, reading and planning, "are crucial".
- **Tests first** as "an Anthropic-favorite workflow for changes that are easily verifiable".
- **One Claude writes, another reviews**: "sometimes having separate context is beneficial", and "This separation often yields better results than having a single Claude handle everything."
- **Clear between tasks**: "Use the `/clear` command frequently between tasks to reset the context window."
- **Keywords for thinking**: "think" < "think hard" < "think harder" < "ultrathink", each mapped to a larger thinking budget in the product of the time.

Grade: documented practice, vendor; "often yields better results" has no figure behind it. Written for: Claude Code users. Transfer: the separate reviewer, the check that comes back pass or fail, and a fresh context per task all transfer. BW6 §4 and BW9 §2, §5 and §7 teach the first two from Anthropic's current documentation page, which those units read on 16 Nov 2026 and which did not come up at its plain address in a search for this unit; BW4 §4 and BW10 (rule 1) teach the third. The keyword ladder was a mechanism of one product in 2025; on current Claude models effort is the lever, set in the model menu (BW2 §3, read 15 Nov 2026).

### 2.4 · A practical guide to building agents (OpenAI, undated)

The guide reserves agents for workflows with "Complex decision-making", "Difficult-to-maintain rules" or "Heavy reliance on unstructured data"; recommends to "maximize a single agent's capabilities first", to "build your agent prototype with the most capable model for every task" and to "Set up evals to establish a performance baseline"; calls guardrails "a layered defense mechanism" because "a single one is unlikely to provide sufficient protection"; and says "Actions that are sensitive, irreversible, or have high stakes should trigger human oversight" ([OpenAI, *A practical guide to building agents*](https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf), read 16 Nov 2026; the PDF shows no date). Grade: documented practice, vendor. Written for: product teams. Transfer: one agent before several, layered guards and a person on irreversible steps transfer; BW9 §7 teaches them. "Most capable model first" is the opposite order to BW2's routing for small recurring tasks; for a new kind of task whose quality you do not yet know, it is a way to set the bar before stepping down (stated opinion).

### 2.5 · GPT-4.1 prompting guide (OpenAI, April 2025)

Noah MacCallum and Julian Lee: the model "is trained to follow instructions more closely and more literally than its predecessors"; three reminders in agent prompts (persistence, tool use, planning) "increased our internal SWE-bench Verified score by close to 20%"; explicit planning "increased the pass rate by 4%"; with long inputs, "place your instructions at both the beginning and end" ([MacCallum and Lee, *GPT-4.1 Prompting Guide*, OpenAI Cookbook, 14 Apr 2025](https://developers.openai.com/cookbook/examples/gpt4-1_prompting_guide), read 16 Nov 2026; marked archived). Grade: vendor data, internal benchmark, method not published. Written for: developers prompting GPT-4.1. Transfer: literal reading of instructions, which BW3 already handles; the figures belong to one vendor's 2025 model and are not used.

## 3 · Practitioners and researchers

### 3.1 · Simon Willison: review what you ship

**The commit rule (March 2025).** Vibe coding is "building software with an LLM without reviewing the code it writes", and it is "not the same thing as writing code with the help of LLMs". His rule for production work: he will not commit code "if I couldn't explain exactly what it does to somebody else". And the test of stakes: "Think about how much harm the code you are writing could cause" (*Not all AI-assisted programming is vibe coding*, 19 Mar 2025, above).

**Agentic engineering (2026).** His guide defines it as "the practice of developing software with the assistance of coding agents", and keeps "vibe coding" for "unreviewed, prototype-quality LLM-generated code" ([Willison, *What is agentic engineering?*](https://simonwillison.net/guides/agentic-engineering-patterns/what-is-agentic-engineering), read 16 Nov 2026; the page shows an update of about March 2026). Its one named anti-pattern: "Don't file pull requests with code you haven't reviewed yourself", because the reviewer is handed your work, and it is "rude to expect someone else to read text that you haven't read" ([Willison, *Anti-patterns: things to avoid*](https://simonwillison.net/guides/agentic-engineering-patterns/anti-patterns), read 16 Nov 2026). In May he wrote that the two had come closer than he liked in his own work, as agents grew reliable enough that he no longer read every line, vibe coding being "the thing where you're not looking at the code at all" ([Willison, *Vibe coding and agentic engineering are getting closer than I'd like*, 6 May 2026](https://simonwillison.net/2026/May/6/vibe-coding-and-agentic-engineering), read 16 Nov 2026).

Grade: stated opinion of a named practitioner, with his public projects as the inspectable record. Written for: programmers. Transfer: whole, with "code" read as "text". Nothing goes to another person that you could not explain, and the stakes decide how much reading that takes.

### 3.2 · Simon Willison: how he uses LLMs for code (March 2025)

The craft "comes down to managing its context"; account for training cut-off dates; ask for options; for production code treat the model as a "digital intern" given exact instructions; and the one thing you "cannot outsource to the machine is testing that the code actually works" ([Willison, *Here's how I use LLMs to help me write code*, 11 Mar 2025](https://simonwillison.net/2025/Mar/11/using-llms-for-code/), read 16 Nov 2026). Grade: documented practice. Written for: programmers. Transfer: context (BW4), cut-offs (BW1 §4) and options (BW7 §4's options stage) are taught; "testing" is BW6's sampling.

### 3.3 · Simon Willison: the lethal trifecta (June 2025)

An agent that combines "Access to your private data", "Exposure to untrusted content" and "The ability to externally communicate" can be made to leak your data; the safe course is to "avoid that lethal trifecta combination entirely", and a filter that catches 95% of attacks is no answer, since "in web application security 95% is very much a failing grade" ([Willison, *The lethal trifecta for AI agents: private data, untrusted content, and external communication*, 16 Jun 2025](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/), read 16 Nov 2026). Grade: stated opinion, on a documented attack class (BW9 §8 gives the studies). Written for: users and builders of agents that mix tools. Transfer: whole, to any chat with connectors. BW9 box 1 is this test.

### 3.4 · New in November 2026: label what the model wrote (Willison, 9 November)

Willison now opens each agent-written pull request with a short paragraph he selects himself (sometimes words the agent gave him), which carries "my human judgement as to what is definitely worth their time", and puts the agent's full description below it in a collapsed `<details>` block whose summary line names the model and often the effort level, so a reader sees at once which part a person vouches for ([Willison, *Hide your slop PR descriptions behind <details><summary>*, 9 Nov 2026](https://simonwillison.net/2026/nov/9/details-summary), read 16 Nov 2026). Grade: documented practice, one practitioner, days old. Written for: programmers who open pull requests. Transfer: whole. A memo, a report or an email can carry your own opening paragraph and mark the model-written remainder as such; with nanochat's disclosure policy (§1.6) it makes a rule (rule 4).

### 3.5 · Ethan Mollick and the jagged frontier

**The field experiment (2023; now in a journal).** Fabrizio Dell'Acqua, Ethan Mollick and seven co-authors ran a pre-registered experiment with 758 consultants. On tasks inside the model's frontier, those using GPT-4 completed "12.2% more tasks on average", "25.1% more quickly", with "more than 40% higher quality"; on a task chosen to sit outside it, AI users were "19 percentage points less likely to produce correct solutions" ([Dell'Acqua et al., *Navigating the Jagged Technological Frontier*, HBS Working Paper 24-013, 22 Sep 2023](https://mitsloan.mit.edu/sites/default/files/2023-10/SSRN-id4573321.pdf), read 16 Nov 2026). The paper is now published in *Organization Science*, whose abstract gives the outside-frontier result as "19% less likely" ([*Organization Science*, DOI 10.1287/orsc.2025.21838](https://pubsonline.informs.org/doi/full/10.1287/orsc.2025.21838?af=R), read 16 Nov 2026; volume and date not shown on the page read). Grade: measured; GPT-4 in 2023, consulting tasks; BW7 §4 already cites it. Written for: researchers and managers of knowledge work. Transfer: the mechanism, as this unit's inference; the sizes do not transfer. On a task outside what the model does well, its answer is persuasive and wrong, and using it made skilled people less accurate.

A later field experiment points the same way for expert writing. In a pre-registered trial run by Google, David Autor and six co-authors randomised 133 patent lawyers between access to a custom drafting assistant and a control group, for three months; drafts with the assistant scored 0.34 standard deviations higher at 10 days and 0.38 at 90, and on a later task done without it, the lawyers who had used it scored 0.32 higher overall, 0.45 among seniors and no higher on average among juniors ([Autor et al., *Does AI Assistance Enhance or Erode Expertise?*, NBER Working Paper 35720, Sep 2026, revised Oct 2026](https://nber.org/papers/w35720), read 16 Nov 2026; not peer-reviewed; one custom tool, one profession). Measured. What it adds for this unit (inference): the people who gained lasting skill were those who already had the judgement to check the output.

**Four principles (Co-Intelligence, 2024): not rebuilt.** The four principles widely attributed to Mollick's book ("always invite AI to the table" among them) were found only in readers' notes and summaries; neither the book nor a post of his stating them came up in a search. They are left out of the rules.

**New in November 2026: the model does not judge its own work (Mollick, 9 November).** Mollick describes directing Anthropic's Fable 5.2 on several projects. He started and steered each, and "my feedback along the way turned out to matter a lot"; he had a model from another vendor act as peer reviewer, which "twice found issues that needed to be resolved"; and the model's own critics and fact-checkers fixed errors but "the AI did not notice these problems itself": none asked whether the work was too long or repetitive. Judging "when your own work is not good enough", he writes, "is the part Fable does least reliably" ([Mollick, *Fable 5.2 and Jagged AGI*, One Useful Thing, 9 Nov 2026](https://www.oneusefulthing.org/p/fable-52-and-jagged-agi), read 16 Nov 2026). Grade: stated opinion, on his own projects; anecdote, one person. Written for: his newsletter's general readers. Transfer: whole. The checker that matters sees the work from outside; a different model where the stakes justify it (BW2 §5); and the questions of length, repetition and worth stay yours.

### 3.6 · Spec-driven development

Harper Reed's three steps (an interview to `spec.md`, a plan of "small, iterative chunks that build on each other", execution; "The success really depends on how well step 2 went"), GitHub's Spec Kit ("the specification becomes the source of truth"; tasks as "small, reviewable chunks") and AWS's Kiro (requirements with acceptance criteria, a design, then tasks ordered by their dependencies and linked to the requirements) were each re-read on 16 Nov 2026 ([Reed, 16 Feb 2025](https://harper.blog/2025/02/16/my-llm-codegen-workflow-atm/); [Delimarsky, GitHub Blog, 2 Sep 2025](https://github.blog/ai-and-ml/generative-ai/spec-driven-development-with-ai-get-started-with-a-new-open-source-toolkit); [Swaminathan and Singh, 14 Jul 2025](https://kiro.dev/blog/introducing-kiro/)). BW5 §1 presents them with Böckeler's critique, Claude Code's spec interview and the one measured spec-first result (Tufano et al., a preprint); BW5 §11 gives OpenAI's and Google's equivalents. They are not presented again here. Grades: documented practice (Reed an anecdote; Spec Kit and Kiro vendor tools). Written for: programmers. Transfer: the pattern whole (BW5 is built on it); the tooling and EARS notation stay with software.

### 3.7 · The prompting literature

- **Chain-of-thought.** Jason Wei and colleagues found that a few worked reasoning examples in the prompt improve large models on "a range of arithmetic, commonsense, and symbolic reasoning tasks" ([Wei et al., NeurIPS 2022, arXiv 2201.11903](https://arxiv.org/pdf/2201.11903), read 16 Nov 2026). Measured, 2022 models.
- **Where it helps.** Zayne Sprague and colleagues, in a meta-analysis of "over 100 papers" and their own tests of "20 datasets across 14 models", found it helps "primarily on tasks involving math or logic"; on MMLU, answering directly does about as well "unless the question or model's response contains an equals sign" ([Sprague et al., *To CoT or not to CoT?*, ICLR 2025](https://proceedings.iclr.cc/paper_files/paper/2025/hash/ead542f13a38179d1b55b88610f959a1-Abstract-Conference.html), read 16 Nov 2026). Measured.
- **ReAct.** Shunyu Yao and colleagues interleaved reasoning with actions such as lookups; it "overcomes issues of hallucination and error propagation" seen with reasoning alone on question answering and fact checking, and beat other methods "by an absolute success rate of 34% and 10% respectively" on two interactive benchmarks ([Yao et al., ICLR 2023, arXiv 2210.03629](https://arxiv.org/abs/2210.03629), read 16 Nov 2026). Measured, 2022 models.
- **Self-consistency.** Xuezhi Wang and colleagues sampled several reasoning paths and kept the most common answer: +17.9 points over chain-of-thought on GSM8K, +11.0 on SVAMP, +12.2 on AQuA ([Wang et al., ICLR 2023, arXiv 2203.11171](https://arxiv.org/abs/2203.11171), read 16 Nov 2026). Measured, 2022 models.

Written for: machine-learning researchers. What survives for knowledge work (this unit's inference). On current Claude models thinking cannot be turned off in the app and effort sets how much of it there is (BW2 §3, read 15 Nov 2026), so "think step by step" asks for what the setting already governs; Sprague's result puts long-form writing and judgement outside the tasks where explicit reasoning measurably helps. ReAct is how a chat with search already works (BW6 §1). Self-consistency survives as a check: a figure or a verdict that two independent runs give alike is less likely to be invented than one draw, which BW6 §4 takes from SelfCheckGPT; agreement is a screen and proves nothing. The papers tested short tasks with answer keys; none tested prose.

## 4 · Who each method was written for, and what the core units already teach

Most of these methods were written by programmers for programmers. What decides transfer is whether the method's working part depends on code: a test suite, a diff, a metric a script computes. Where it does, the method stays with software, or with the scripts around your project. Where it depends on a check, a file, a context or a person, it transfers.

The figure sets each method's grade, its transfer to knowledge work and the core unit that teaches it beside each other.

```viz
{"kind": "matrix", "cols": ["Grade", "Transfers", "Core unit"], "rows": [
 {"label": "Vibe coding (Karpathy)", "cells": ["opinion", "throwaway only", "BW9 §3"]},
 {"label": "Slider and leash (Karpathy)", "cells": ["opinion", "yes", "BW9 §2"]},
 {"label": "Context engineering (Karpathy)", "cells": ["opinion", "yes", "BW4"]},
 {"label": "Agents on his code; failure list", "cells": ["opinion", "list: yes", "BW9 §6, part"]},
 {"label": "Verifiability (Karpathy)", "cells": ["opinion", "yes", "BW6, BW9 §2"]},
 {"label": "nanochat disclosure", "cells": ["practice", "yes", "none"]},
 {"label": "autoresearch loop", "cells": ["practice", "scripts only", "none"]},
 {"label": "LLM wiki", "cells": ["practice", "with a change", "BW4, part"]},
 {"label": "Building effective agents", "cells": ["practice", "yes", "BW7 §1, BW9"]},
 {"label": "Effective context engineering", "cells": ["practice", "yes", "BW1, BW3, BW4"]},
 {"label": "Claude Code practices, 2025", "cells": ["practice", "most", "BW6, BW9"]},
 {"label": "OpenAI agents guide", "cells": ["practice", "yes", "BW9 §7"]},
 {"label": "GPT-4.1 guide", "cells": ["vendor data", "literalness", "BW3"]},
 {"label": "Willison: review what you ship", "cells": ["opinion", "yes", "none"]},
 {"label": "Willison: how he codes", "cells": ["practice", "yes", "BW4, BW6"]},
 {"label": "Lethal trifecta", "cells": ["opinion", "yes", "BW9 §8"]},
 {"label": "Label model text (Willison)", "cells": ["practice", "yes", "none"]},
 {"label": "Jagged frontier experiment", "cells": ["measured", "mechanism", "BW7 §4"]},
 {"label": "Outside reviewer (Mollick)", "cells": ["opinion", "yes", "BW2 §5, BW6"]},
 {"label": "Spec-driven development", "cells": ["practice", "pattern", "BW5"]},
 {"label": "CoT, ReAct, self-consistency", "cells": ["measured", "self-consistency", "BW6 §4, part"]}
], "caption": "Each method of §1 to §3 with its grade, whether it transfers to knowledge work, and the core unit that already teaches it ('none': taught here first; 'part': the unit teaches the idea without this source). Grades, transfers and core units from §1 to §4 of this unit; units by code. Opinion: stated opinion; practice: documented practice."}
```

Four methods are taught here for the first time: Willison's rule that you ship nothing you have not read, his labelling of model-written text, nanochat's disclosure policy, and the guards of the autoresearch loop for unattended scripts. Three are taught in part: Karpathy's failure list (BW9 §6 has the silent assumption, from Anthropic, and not the rest), the LLM wiki (BW4 has the single source of truth and the rot check, and not the index-first layout or the log), and self-consistency (BW6 §4 has the cheap screen of two fresh chats, from SelfCheckGPT). Everything else is already in a core unit, often from the same source.

## 5 · The methods against BW9's decision rule

BW9's Deliverable, Part 1, is an agent-use decision rule in eight boxes: the trifecta (1), irreversible steps (2), a pass/fail check a context can run (3), tools over dependent steps (4), shape (5), unattended runs (6), the five questions (7), and what must pass before anything is kept (8). Each method here was set against it (stated opinion; the boxes are BW9's).

| Method | Box | Agrees or conflicts |
|---|---|---|
| Lethal trifecta (§3.3) | 1 | The same test, from the same post |
| OpenAI's human oversight for irreversible actions (§2.4) | 2 | Agrees: BW9 cites it there |
| Verifiability (§1.5); tests first (§2.3) | 3 | Agrees: box 3 is verifiability stated as a question |
| Simplest solution first (§2.1); one agent first (§2.4) | 4, 5 | Agrees: a chat where a chat will do, one session before subagents |
| Slider and leash (§1.2) | 6 | Agrees: small chunks you verify are box 6's "session you watch" |
| autoresearch loop (§1.6) | 7 | Agrees on three of its guards (scope, budget, a check); passes box 7 only if something stops it and a person signs off, which the README does not state |
| Vibe coding (§1.1) | 3, 8 | Conflicts with box 8 unless the output is a throwaway whose result you can see; there it passes box 3 by looking |
| LLM wiki (§1.7) | 8 | Conflicts where the model rewrites filed pages unchecked; agrees once lint reports and you apply |
| Failure list (§1.4); outside reviewer (§3.5) | 8 | Agree: they say what box 8's reviewer looks for and who it should be |
| Review what you ship; label model text (§3.1, §3.4) | 2, 8 | Agree, and add a step: whatever leaves your hands carries a part you wrote and read |

No method found here argues against BW9's rule. Two press on it: the autoresearch loop shows that an unattended run can be safe with narrow guards, and Willison's May post records a careful practitioner reading less as agents improve. The second is the risk the rule exists for.

## 6 · On other tools

The methods in this unit are stated by their authors for language models in general or for coding agents of several vendors; the rules in the Deliverable hold for any current assistant. Three claims are specific to Claude, and one example names a Claude model. Read on 16 Nov 2026; a page that redirected or failed is "not checked".

| Claim in this unit | Claude | ChatGPT and OpenAI | Gemini and Google |
|---|---|---|---|
| A check in a context that has not seen the work (§2.3; rule 3) | A custom subagent "starts with a fresh, isolated context window"; a fork "inherits the parent conversation", and fork mode is "on by default" in local sessions, off with `CLAUDE_CODE_FORK_SUBAGENT` set to `0` ([*Create custom subagents*](https://code.claude.com/docs/en/sub-agents)) | Not checked: Codex's pages redirected to another site (as BW9 §10 records) | "Each subagent operates within its own separate context window" ([Wotherspoon and Patel, *Subagents have arrived in Gemini CLI*, 15 Apr 2026](https://developers.googleblog.com/subagents-have-arrived-in-gemini-cli/)) |
| Reasoning set by a setting, not by words in the prompt (§2.3, §3.7; rule 10) | Effort, set in the model menu (BW2 §3, read 15 Nov 2026) | `reasoning.effort` "guides the model on how much to think", values model-dependent ([*Reasoning models*](https://developers.openai.com/docs/guides/reasoning)) | "Gemini models engage in dynamic thinking by default", set by `thinkingLevel` ([*Gemini thinking*](https://ai.google.dev/gemini-api/docs/generate-content/thinking)) |
| An instruction file that sets a wiki's conventions (§1.7) | `CLAUDE.md`, as Karpathy's gist names it | `AGENTS.md`, as the gist names it; OpenAI's own page redirected to another site, not checked | `GEMINI.md`, and the file name can be set to `AGENTS.md`: "define them once in a context file" ([*Provide context with GEMINI.md files*](https://geminicli.com/docs/cli/gemini-md/)) |
| A model-written description labelled with its model (§3.4) | Willison's example names a Claude model; nothing in it depends on the vendor | Same practice applies | Same practice applies |

The studies name their own models: GPT-4 (Dell'Acqua et al.), a custom drafting assistant (Autor et al.), PaLM and other 2022 models (Wei, Wang, Yao), 14 models (Sprague).

## Deliverable · Method cards and ten operating rules

Three parts. Part 1 is the method cards, one per method of §1 to §3, each traced to its section. Part 2 is the ten operating rules, each traced to its cards, built on the Academy case, a library of self-study courses built by one person with Claude in October and November 2026, with a method of one brief per unit, and a fresh check and sample audits that the case file records as run on part of the library (Academy case file §1, §2, §5, §9). It is one project by one person: an anecdote, never evidence for a rule, and its record holds no control (case file §9). Each rule has a column saying what your own record of chats would show, so DD-BW3 can test it. Part 3 is the templates. Grades are this unit's; the rules as a set are this unit's synthesis (stated opinion), each resting on the cards named.

### Part 1 · Method cards

**K1 · Vibe coding**
- Author: Andrej Karpathy.
- Primary source: X post, Feb 2025, via Willison, 19 Mar 2025; *Vibe coding MenuGen*, 27 Apr 2025 (§1.1).
- Claim: for throwaway projects you can accept every change unread and steer by results.
- Grade: stated opinion; one documented project.
- Transfers: a script you delete, whose output you can see is right. Does not: anything filed, published or sent.

**K2 · Autonomy slider, leash, verification loop**
- Author: Andrej Karpathy.
- Primary source: YC AI Startup School keynote, 16–17 Jun 2025, via a third-party transcription (§1.2).
- Claim: decide per task how much autonomy to grant, work in small verified chunks, and make your checking fast.
- Grade: stated opinion.
- Transfers: all of it. Does not: the interface-design advice, which is for product builders.

**K3 · Context engineering**
- Author: Andrej Karpathy, agreeing with Tobi Lütke.
- Primary source: X post, June 2025, via Willison, 27 Jun 2025 (§1.3).
- Claim: the skill is filling the window with the right information for the next step.
- Grade: stated opinion.
- Transfers: whole (BW4). Does not: nothing withheld.

**K4 · Agents on an unusual codebase**
- Author: Andrej Karpathy.
- Primary source: Dwarkesh Podcast, 17 Oct 2025 (§1.4).
- Claim: agents fail on work unlike their training data and help on boilerplate and on ports with tests.
- Grade: documented practice, one codebase.
- Transfers: expect a model to pull unusual work toward the usual. Does not: the comparison with autocomplete, which is about code editors.

**K5 · Verifiability**
- Author: Andrej Karpathy.
- Primary source: X post, 16 Nov 2025, via Willison the same day (§1.5).
- Claim: AI gets good fastest at tasks that are resettable, efficient and rewardable by an automatic check.
- Grade: stated opinion.
- Transfers: as the test of what to delegate (BW6 step I, BW9 box 3). Does not: the claim about training, which is about labs.

**K6 · Agent-first coding and its failure list**
- Author: Andrej Karpathy.
- Primary source: X thread, 26 Jan 2026, via Thread Reader App (§1.4).
- Claim: agents now write most of his code, must be watched for unchecked assumptions, unasked questions, bloat and dead code, and work best given success criteria.
- Grade: stated opinion, self-reported figure.
- Transfers: the failure list as a checker's checklist; success criteria in every brief. Does not: the 80/20 share.

**K7 · Disclosure of model contribution**
- Author: Andrej Karpathy.
- Primary source: nanochat README, read 16 Nov 2026 (§1.6).
- Claim: whoever submits work declares the parts a model substantially wrote that they did not write or do not fully understand.
- Grade: documented practice.
- Transfers: whole, to anything handed to another person. Does not: nothing withheld.

**K8 · The autoresearch loop**
- Author: Andrej Karpathy.
- Primary source: autoresearch README; nanochat leaderboard, entries 5 and 6, 9 and 14 Mar 2026 (§1.6).
- Claim: an agent changing one file against one metric, on a fixed budget per run, keeping only improvements, found real gains (2.02 to 1.80 to 1.65 hours, his record).
- Grade: documented practice, self-reported result.
- Transfers: its guards, to an unattended script with a pass/fail check. Does not: to prose, which has no metric a script computes.

**K9 · The LLM wiki**
- Author: Andrej Karpathy.
- Primary source: gist *llm-wiki*, 4 Apr 2026 (§1.7).
- Claim: a model can compile raw sources into a Markdown wiki, navigate it by an index without retrieval at about a hundred sources, and keep it healthy by lint.
- Grade: documented practice; scale self-reported.
- Transfers: immutable sources, index read first, append-only log, lint. Does not: a model rewriting checked pages at will.

**K10 · How I use LLMs**
- Author: Andrej Karpathy.
- Primary source: YouTube video, Feb 2025; not checked (§1.8).
- Claim: none taken; the primary source was not reached.
- Grade: not re-verified.
- Transfers: nothing used.

**K11 · Agentic engineering (Sequoia summary)**
- Author: Andrej Karpathy.
- Primary source: blog summary, Apr 2026; not checked (§1.8).
- Claim: carried by W1 in Willison's words.
- Grade: not re-verified.
- Transfers: see W1.

**A1 · Building effective agents**
- Author: Erik S. and Barry Zhang, Anthropic.
- Primary source: Anthropic Engineering, 19 Dec 2024 (§2.1).
- Claim: use the simplest workflow that works, and agents only for open-ended problems.
- Grade: documented practice, vendor.
- Transfers: the simplicity rule; the pattern names. Does not: the framework advice, which is for API developers.

**A2 · Effective context engineering**
- Author: Prithvi Rajasekaran, Ethan Dixon, Carly Ryan and Jeremy Hadfield, Anthropic.
- Primary source: Anthropic Engineering, 29 Sep 2025 (§2.2).
- Claim: aim for the smallest set of high-signal tokens; load by identifier, compact, keep notes outside the window, use clean sub-agent windows.
- Grade: documented practice, vendor; no figures.
- Transfers: whole (BW1, BW3, BW4). Does not: nothing withheld.

**A3 · Claude Code: best practices for agentic coding**
- Author: Boris Cherny, Anthropic.
- Primary source: Anthropic, 18 Apr 2025, no longer maintained (§2.3).
- Claim: read and plan before writing, test first where results are verifiable, review in a separate context, clear between tasks.
- Grade: documented practice, vendor; no figures.
- Transfers: the separate reviewer, the pass/fail check, a fresh context per task. Does not: the thinking keywords, a 2025 product mechanism.

**O1 · A practical guide to building agents**
- Author: OpenAI.
- Primary source: PDF, undated (§2.4).
- Claim: one agent first, layered guardrails, evals for a baseline, and human oversight of sensitive or irreversible actions.
- Grade: documented practice, vendor.
- Transfers: one agent first; layered guards; a person on irreversible steps. Does not: "most capable model for every task" as a standing rule, against BW2's routing.

**O2 · GPT-4.1 prompting guide**
- Author: Noah MacCallum and Julian Lee, OpenAI.
- Primary source: OpenAI Cookbook, 14 Apr 2025, archived (§2.5).
- Claim: newer models read instructions literally; agent reminders raised an internal benchmark by close to 20%.
- Grade: vendor data, internal benchmark.
- Transfers: literal reading (BW3). Does not: the figures.

**W1 · Review what you ship**
- Author: Simon Willison.
- Primary source: blog, 19 Mar 2025; *What is agentic engineering?* and *Anti-patterns*, guide, 2026; blog, 6 May 2026 (§3.1).
- Claim: ship nothing you could not explain to someone else, and never hand someone a text you have not read.
- Grade: stated opinion.
- Transfers: whole, with "code" read as "text". Does not: nothing withheld.

**W2 · How he uses LLMs for code**
- Author: Simon Willison.
- Primary source: blog, 11 Mar 2025 (§3.2).
- Claim: manage context, mind the cut-off, ask for options, give exact instructions, and test what it writes yourself.
- Grade: documented practice.
- Transfers: all, "testing" read as BW6's sampling. Does not: library choices.

**W3 · The lethal trifecta**
- Author: Simon Willison.
- Primary source: blog, 16 Jun 2025 (§3.3).
- Claim: private data, untrusted content and a way to communicate out in one agent make data theft possible, and filters do not fix it.
- Grade: stated opinion on a documented attack class.
- Transfers: whole. Does not: nothing withheld.

**W4 · Label the model-written part (new)**
- Author: Simon Willison.
- Primary source: blog, 9 Nov 2026 (§3.4).
- Claim: open with a short part you chose yourself, and put the model's text below it, marked with the model that wrote it.
- Grade: documented practice, one practitioner.
- Transfers: whole, to any document you send. Does not: the HTML element, which is for code hosts.

**M1 · Four principles of Co-Intelligence**
- Author: Ethan Mollick.
- Primary source: book, 2024; not reached in his own words (§3.5).
- Claim: none taken.
- Grade: not re-verified.
- Transfers: nothing used.

**M2 · The jagged frontier**
- Author: Fabrizio Dell'Acqua, Ethan Mollick and seven others.
- Primary source: HBS Working Paper 24-013, 22 Sep 2023; *Organization Science* (§3.5).
- Claim: with 758 consultants, GPT-4 raised output, speed and quality inside its frontier and lowered correct answers outside it.
- Grade: measured; GPT-4, 2023.
- Transfers: the expectation that a confident wrong answer is likeliest where the task lies outside the model's strength. Does not: the sizes.

**M3 · The model does not judge its own work (new)**
- Author: Ethan Mollick.
- Primary source: One Useful Thing, 9 Nov 2026 (§3.5).
- Claim: steer each project yourself and use an outside reviewer, because the model fixes errors its own critics find but does not notice when its work is too long, repetitive or not worth it.
- Grade: stated opinion; anecdote.
- Transfers: whole. Does not: the projects' figures, which are one person's.

**S1 · Harper Reed's workflow**
- Author: Harper Reed.
- Primary source: blog, 16 Feb 2025 (§3.6; BW5 §1).
- Claim: interview to a spec, plan in small chunks with a checklist, then execute.
- Grade: documented practice, anecdote.
- Transfers: the pattern (BW5). Does not: the code tooling.

**S2 · GitHub Spec Kit**
- Author: Den Delimarsky, GitHub.
- Primary source: GitHub Blog, 2 Sep 2025 (§3.6; BW5 §1).
- Claim: the specification is the source of truth; specify, plan, split into reviewable tasks.
- Grade: documented practice, vendor tool.
- Transfers: the pattern (BW5). Does not: the toolkit.

**S3 · AWS Kiro**
- Author: Nikhil Swaminathan and Deepak Singh, AWS.
- Primary source: Kiro blog, 14 Jul 2025 (§3.6; BW5 §1).
- Claim: requirements with acceptance criteria, then a design, then tasks ordered by dependency and linked to requirements.
- Grade: documented practice, vendor tool.
- Transfers: each task traced to a requirement. Does not: EARS notation and the IDE.

**P1 · Chain-of-thought, and where it helps**
- Author: Jason Wei and others; Zayne Sprague and others.
- Primary source: NeurIPS 2022; ICLR 2025 (§3.7).
- Claim: worked reasoning helps large models mainly on maths and logic.
- Grade: measured; 2022 to 2024 models.
- Transfers: effort as the control (BW2 §3). Does not: "think step by step" lines in a brief.

**P2 · ReAct**
- Author: Shunyu Yao and others.
- Primary source: ICLR 2023 (§3.7).
- Claim: interleaving reasoning with tool use reduces hallucination against reasoning alone.
- Grade: measured; 2022 models.
- Transfers: nothing to write; search-enabled chats work this way. Does not: the prompt format.

**P3 · Self-consistency**
- Author: Xuezhi Wang and others.
- Primary source: ICLR 2023 (§3.7).
- Claim: several sampled reasoning paths, majority answer, beat a single path (17.9 points on GSM8K).
- Grade: measured; 2022 models.
- Transfers: two independent runs for a figure or verdict that matters. Does not: voting on prose.

### Part 2 · Ten operating rules, on the Academy case

Each rule is stated for any project, traced to its cards, graded by the strongest evidence behind it, given the record that would show whether you keep it (DD-BW3 reads your chats against this column), and set against what the Academy case file records. Where the case file is silent, the cell says so.

| # | Rule | Cards | Grade | What your record shows | Academy case (anecdote) |
|---|---|---|---|---|---|
| 1 | **Delegate what something other than your reading can check.** Before handing a task to a model, name its check: a source, a script, a context that did not do the work. With none, the model drafts and you decide. | K5, M2, A3 | Stated opinion; M2's mechanism measured on GPT-4 in 2023 | Delegated tasks with no named check; judgement calls (what to cut, what to claim) accepted from a model unchanged | Every cited claim is checked against its source by a fresh context (case file §2); a proposed task is not worked until the owner confirms it (§2) |
| 2 | **Brief the result, not the steps.** Every brief ends with success criteria a stranger could check. | K6, S2, S3, A3 | Documented practice | Briefs without done-when lines; outputs that met the brief and were still rejected | One brief per unit, never reworded; the fresh check tests the deliverable against the brief (§2) |
| 3 | **The writer never checks its own work.** The check runs in a context that did not see the writing (a new chat, or a custom subagent; never a fork of the writing conversation), opens the sources, and looks for unchecked assumptions, unflagged contradictions, padding and superseded text left in place. Where the stakes justify it, the checker is another model. | A3, M3, K6, W2 | Documented practice, vendor; no figures | Checks asked for in the same chat that wrote the draft; checks that re-read without opening sources | A separate context that has not seen the unit checks it and never edits (§2); 28 of 36 drafts had at least one error at that check (§5); checkers of three models (§5) |
| 4 | **Read what you send, and label what you did not write.** Nothing goes to another person or a published page that you have not read; the part you chose and vouch for comes first, and model-written text is marked with the model. | W1, W4, K7 | Stated opinion; documented practice (K7, W4) | Model output forwarded or published unedited; documents with no mark of which part a model wrote | The model that wrote each unit is recorded (§2); whether the owner reads each unit before publishing is not in the case file |
| 5 | **Small pieces, one at a time.** One output per brief, sized so you can read it in one sitting, each checked before the next is built on it. | K2, S1, S2 | Stated opinion; documented practice (S1, S2) | Chats asking for several unrelated outputs; outputs too long to have been read | One unit per context, 2,000 to 6,000 words by guide (§1, §2) |
| 6 | **The simplest setup that does the job.** A chat before a pipeline, a pipeline before an agent, one agent before several. | A1, O1 | Documented practice, vendor | Agent or research runs for tasks a single chat answered | From BW7 on, writer, fresh checker, applier and filer are each a fresh agent (§2); with no control, its record cannot show a lighter setup would have done worse (§2, §9) |
| 7 | **An unattended loop has four guards.** One thing it may change, a fixed budget per run, a check that decides keep or revert, and a person who stops it and signs off. | K8, O1 | Documented practice | Background or scheduled runs missing any of the four | Failed figures are fixed and re-checked by a new agent until they pass (§6); an index check restores every file if it fails (§1); budgets per run are not in the case file |
| 8 | **Files are the memory.** The project's knowledge lives in Markdown files you can read: sources kept unchanged, an index read first, an append-only log; a periodic lint reports problems, and changes to checked pages are replacements you approve. | K9, A2 | Documented practice | Facts that live only in chat history or a memory feature; pages changed with no log entry | Units are Markdown files in one repository (§1); a course index lists each unit (§1); every finished row moves to a changelog (§2); the checker never edits and each finding is applied as an exact replacement (§2) |
| 9 | **Never the trifecta.** No chat or agent holds your private material, untrusted content and a way to send or publish at once; remove the way out first. | W3 | Stated opinion on a documented attack class | Chats with connectors that read the web, hold private files and can send | Which tools each agent held is not in the case file |
| 10 | **Effort is a setting; a number that matters gets two runs.** Set effort in the model menu, never by "think harder" in the prompt; a figure or verdict that matters is asked in two fresh chats, and a disagreement means it is checked at a source. | P1, P3, A3 | Measured (P1, P3, on 2022 to 2024 models); the transfer is inference | Prompts carrying "think step by step"; key figures taken from one draw unchecked | The model of each unit is recorded (§2); effort settings are not in the case file |

What the ten have in common: each puts a check, a file or a person where a model's own confidence would otherwise decide. No rule rests on the case; where the case runs a rule, it shows only that one person kept it.

### Part 3 · Templates

**A blank method card.** Fill one for any method you meet that is not in Part 1.

**[Code] · [Name of the method]**
- Author: [the person or organisation whose own words state it; if only a third party states it, stop: the method is not attributed]
- Primary source: [their post, talk, repository or paper, with its date; and the date you read it]
- Claim: [one sentence, in your words, that the source supports without stretching]
- Grade: [measured: a study with numbers, naming the models and task / documented practice: a named person's or vendor's account with something you can inspect / stated opinion: a view with nothing to inspect]
- Transfers: [the part that depends on a check, a file, a context or a person, applied to your project]
- Does not: [the part that depends on code, a metric or a product feature your project lacks]

**Your operating rules.** Keep the rules of Part 2 that hold for your project, change the wording where your tools differ, and fill the two right-hand columns.

| # | Rule | Cards | Grade | What my record shows | How my project keeps it |
|---|---|---|---|---|---|
| 1 | [Delegate what something other than your reading can check] | [K5, M2, A3] | [as Part 2] | [count of delegated tasks with no named check, from your chats] | [the check you name for each recurring task, from your BW6 protocol] |
| 2 | [Brief the result, not the steps] | [K6, S2, S3, A3] | [as Part 2] | [briefs without done-when lines] | [where your briefs' done-when lines live: your BW5 brief form] |
| 3 | [The writer never checks its own work] | [A3, M3, K6, W2] | [as Part 2] | [checks run in the writing chat] | [how you get a fresh context: a new chat, a custom subagent; which model checks] |
| 4 | [Read what you send, and label what you did not write] | [W1, W4, K7] | [as Part 2] | [model text sent or published unedited] | [the mark you put on model-written text] |
| 5 | [Small pieces, one at a time] | [K2, S1, S2] | [as Part 2] | [chats with several unrelated outputs] | [the largest output you can read in one sitting] |
| 6 | [The simplest setup that does the job] | [A1, O1] | [as Part 2] | [agent runs for one-chat tasks] | [the tasks your BW9 rule sends to an agent] |
| 7 | [An unattended loop has four guards] | [K8, O1] | [as Part 2] | [unattended runs missing a guard] | [for each run: what it may change, its budget, its check, who stops it] |
| 8 | [Files are the memory] | [K9, A2] | [as Part 2] | [facts living only in chats or memory] | [your index file, your log file, your monthly rot check from BW4] |
| 9 | [Never the trifecta] | [W3] | [as Part 2] | [chats holding all three legs] | [which leg you remove first, per tool] |
| 10 | [Effort is a setting; a number that matters gets two runs] | [P1, P3, A3] | [as Part 2] | [prompts asking the model to think harder; figures from one draw] | [your effort per task type, from your BW2 routing table] |

## Sources

All read, or tried, on 16 November 2026 at the address a search returned.

- Bellan, R. and Franceschi-Bicchierai, L. *OpenAI co-founder Andrej Karpathy joins Anthropic's pre-training team*. TechCrunch, 19 May 2026. https://techcrunch.com/2026/05/19/openai-co-founder-andrej-karpathy-joins-anthropics-pre-training-team/
- Willison, S. *Not all AI-assisted programming is vibe coding (but vibe coding rocks)*. 19 March 2025. https://simonwillison.net/2025/Mar/19/vibe-coding/
- Karpathy, A. *Vibe coding MenuGen*. 27 April 2025. https://karpathy.bearblog.dev/vibe-coding-menugen/
- yt-transcribe. *Andrej Karpathy: Software Is Changing (Again) - transcription by yt-transcribe* (third-party automatic transcription of the keynote at AI Startup School, San Francisco, 16–17 June 2025; dates from Y Combinator, *Join us at AI Startup School — June 16-17*, https://www.ycombinator.com/blog/ai-startupschool). https://cdn.billmill.org/static/yt-transcribe/karpathy/httpswwwyoutubecomwatchvLCEmiRjPEtQ.html
- Willison, S. *Context engineering*. 27 June 2025. https://simonwillison.net/2025/Jun/27/context-engineering/
- Patel, D. *Andrej Karpathy — AGI is still a decade away*. Dwarkesh Podcast, 17 October 2025. https://dwarkesh.com/p/andrej-karpathy
- Thread Reader App. *Thread by @karpathy on Thread Reader App* (reproduction of Andrej Karpathy's X thread of 26 January 2026). https://threadreaderapp.com/thread/2015883857489522876.html
- Willison, S. *A quote from Andrej Karpathy*. 16 November 2025. https://feeds.simonwillison.net/2025/Nov/16/andrej-karpathy/
- Karpathy, A. *nanochat* (README). GitHub. https://github.com/karpathy/nanochat
- Karpathy, A. *autoresearch* (README). GitHub. https://github.com/karpathy/autoresearch
- Karpathy, A. *llm-wiki*. GitHub gist, created 4 April 2026. https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
- Erik S. and Zhang, B. *Building effective agents*. Anthropic Engineering, 19 December 2024. https://anthropic.com/engineering/building-effective-agents
- Rajasekaran, P., Dixon, E., Ryan, C. and Hadfield, J. *Effective context engineering for AI agents*. Anthropic Engineering, 29 September 2025. https://anthropic.com/engineering/effective-context-engineering-for-ai-agents
- Cherny, B. *Claude Code: Best practices for agentic coding*. Anthropic, 18 April 2025. https://www.anthropic.com/research/claude-code-best-practices
- OpenAI. *A practical guide to building agents* (PDF, undated). https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf
- MacCallum, N. and Lee, J. *GPT-4.1 Prompting Guide*. OpenAI Cookbook, 14 April 2025. https://developers.openai.com/cookbook/examples/gpt4-1_prompting_guide
- Willison, S. *What is agentic engineering?* Agentic Engineering Patterns. https://simonwillison.net/guides/agentic-engineering-patterns/what-is-agentic-engineering
- Willison, S. *Anti-patterns: things to avoid*. Agentic Engineering Patterns. https://simonwillison.net/guides/agentic-engineering-patterns/anti-patterns
- Willison, S. *Vibe coding and agentic engineering are getting closer than I'd like*. 6 May 2026. https://simonwillison.net/2026/May/6/vibe-coding-and-agentic-engineering
- Willison, S. *Here's how I use LLMs to help me write code*. 11 March 2025. https://simonwillison.net/2025/Mar/11/using-llms-for-code/
- Willison, S. *The lethal trifecta for AI agents: private data, untrusted content, and external communication*. 16 June 2025. https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/
- Willison, S. *Hide your slop PR descriptions behind <details><summary>*. 9 November 2026. https://simonwillison.net/2026/nov/9/details-summary
- Dell'Acqua, F., McFowland III, E., Mollick, E., Lifshitz-Assaf, H., Kellogg, K. C., Rajendran, S., Krayer, L., Candelon, F. and Lakhani, K. R. *Navigating the Jagged Technological Frontier: Field Experimental Evidence of the Effects of AI on Knowledge Worker Productivity and Quality*. HBS Working Paper 24-013, 22 September 2023. https://mitsloan.mit.edu/sites/default/files/2023-10/SSRN-id4573321.pdf
- *Navigating the Jagged Technological Frontier: Field Experimental Evidence of the Effects of Artificial Intelligence on Knowledge Worker Productivity and Quality*. Organization Science, DOI 10.1287/orsc.2025.21838. https://pubsonline.informs.org/doi/full/10.1287/orsc.2025.21838?af=R
- Autor, D., Rodchenko, T., Martin, J., Iscenko, Z., Strand, S., Pearl, D. and Ferere, M. *Does AI Assistance Enhance or Erode Expertise? Evidence from a Three-Month Field Experiment in Patent Drafting*. NBER Working Paper 35720, September 2026, revised October 2026. https://nber.org/papers/w35720
- Mollick, E. *Fable 5.2 and Jagged AGI*. One Useful Thing, 9 November 2026. https://www.oneusefulthing.org/p/fable-52-and-jagged-agi
- Reed, H. *My LLM codegen workflow atm*. 16 February 2025. https://harper.blog/2025/02/16/my-llm-codegen-workflow-atm/
- Delimarsky, D. *Spec-driven development with AI: Get started with a new open source toolkit*. GitHub Blog, 2 September 2025. https://github.blog/ai-and-ml/generative-ai/spec-driven-development-with-ai-get-started-with-a-new-open-source-toolkit
- Swaminathan, N. and Singh, D. *Introducing Kiro*. Kiro blog, 14 July 2025. https://kiro.dev/blog/introducing-kiro/
- Wei, J. et al. *Chain-of-Thought Prompting Elicits Reasoning in Large Language Models*. NeurIPS 2022; arXiv 2201.11903v6. https://arxiv.org/pdf/2201.11903
- Sprague, Z. et al. *To CoT or not to CoT? Chain-of-thought helps mainly on math and symbolic reasoning*. ICLR 2025. https://proceedings.iclr.cc/paper_files/paper/2025/hash/ead542f13a38179d1b55b88610f959a1-Abstract-Conference.html
- Yao, S. et al. *ReAct: Synergizing Reasoning and Acting in Language Models*. ICLR 2023; arXiv 2210.03629. https://arxiv.org/abs/2210.03629
- Wang, X. et al. *Self-Consistency Improves Chain of Thought Reasoning in Language Models*. ICLR 2023; arXiv 2203.11171. https://arxiv.org/abs/2203.11171
- Anthropic. *Create custom subagents*. Claude Code documentation. https://code.claude.com/docs/en/sub-agents
- OpenAI. *Reasoning models*. OpenAI API documentation. https://developers.openai.com/docs/guides/reasoning
- Google. *Gemini thinking*. Gemini API documentation. https://ai.google.dev/gemini-api/docs/generate-content/thinking
- Google. *Provide context with GEMINI.md files*. Gemini CLI documentation. https://geminicli.com/docs/cli/gemini-md/
- Wotherspoon, J. and Patel, A. *Subagents have arrived in Gemini CLI*. Google Developers Blog, 15 April 2026. https://developers.googleblog.com/subagents-have-arrived-in-gemini-cli/
- Academy case file, §1, §2, §5, §6, §9 (the course's data folder).

## Unsure list

# DD-BW1 · Unsure list

1. The YC AI Startup School quotations (§1.2, card K2) rest on a third-party automatic transcription (yt-transcribe on billmill.org); the recording was not watched, and no transcript from YC or Karpathy was found.
2. Karpathy's thread of 26 January 2026 (§1.4, card K6, figure 1) was read only as reproduced on Thread Reader App; X was not opened. Its Sources title is left as organisation, document type and date because the page's own headline was not read.
3. Karpathy's verifiability post (§1.5, K5) and context-engineering post (§1.3, K3) are read through Willison's quotations; the blog version of the verifiability essay did not come up in a search.
4. The vibe-coding post's date: Willison gives 6 February; the X status number decodes to 2 February 2025 by this unit's own arithmetic (§1.1).
5. autoresearch: `program.md` was not re-read (no search returned it), so the keep-or-revert detail beyond the README's "keeps or discards" and the agent's stop instruction are not stated (§1.6, K8, rule 7, §5 row).
6. Anthropic's current *Best practices for Claude Code* page did not come up at its plain address in any search (only the .md copy and query-string addresses did), so it was not read for this unit; §2.3 points to BW6 and BW9, which read it on 16 Nov 2026, for the current versions of the reviewer and pass/fail practices.
7. Mollick's four Co-Intelligence principles (M1) were found only in readers' notes; his own wording was not reached, and they are left out of the rules.
8. Dell'Acqua et al. in *Organization Science*: volume, issue and date were not shown on the page read; the published abstract says "19% less likely" where the working paper says "19 percentage points less likely" (§3.5, M2).
9. "How I use LLMs" (K10) and the Sequoia AI Ascent 2026 summary (K11) were not reached at their primary pages; nothing from them is used.
10. The Gemini thinking page's headline was not read on the page itself; the Sources title "Gemini thinking" is the page title a search returned (§6).

Object: none

Fresh check 2026-11-16 (claude-opus-5-5): fix · 3 errors, 20 should-fix, 12 minor; report `audits/building-with-ai/fresh-check-DD-BW1.md`

Correction 2026-11-16, found by DD-BW1's filer (flag F98, as F52) and checked by a fresh agent (`audits/building-with-ai/corrections-2026-11-16-DD-BW1-r3-DD-BW1.md`): the Deliverable intro describes the case in the case file's wording.
