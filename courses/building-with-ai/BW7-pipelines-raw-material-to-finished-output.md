---
code: BW7
title: "Pipelines: raw material to finished output"
course: building-with-ai · BW · Building with AI
model: Opus 5.5
written: 2026-11-16
search: off
---

# BW7 · Pipelines: raw material to finished output

This unit was written with search off. Searches were used only to re-verify each source it cites, on 16 November 2026, and every product fact (a feature, a page's advice, a model name) carries the date it was read on the vendor's own page; most documentation pages show no date of their own. Each practice carries an evidence grade, as in BW1 to BW6: **measured** (a study or a test with numbers), **documented practice** (a vendor or a named practitioner says to do it; nobody measured it here) or **stated opinion**. Every study names the models and the task it tested; carrying its finding to a current model or to your work is this unit's inference, and is said to be. Three earlier units are used by name throughout: BW2's routing table (a stage takes its model from a row of it), BW3's brief form (each stage's brief is written in it, from its template 7) and BW5's flag-and-review rule (BW5 §9 and Deliverable 2e; a human gate is placed at its boundaries). None of them is restated here.

## 1 · What a pipeline is

A pipeline is your project's repeated work written down as a fixed sequence of **stages**. Each stage has four things and only four: a defined **input** (named files), a defined **output** (one named file, in a stated form), **one model** (or none, where a script or you do the work), and a **gate** that the output must pass before the next stage may read it. The pipeline is the list of stages in order, plus a log of every run.

The idea is not new, and the vendors document it under another name. Anthropic's engineering post *Building effective agents* calls it prompt chaining: it "decomposes a task into a sequence of steps", each call working on the output of the one before, and "You can add programmatic checks" on any intermediate step, which its diagram labels a "gate". It is ideal, the post says, when a task "can be easily and cleanly decomposed into fixed subtasks", and the aim is to trade latency for accuracy by making each call an easier task; its two examples are marketing copy then its translation, and an outline that is checked against criteria before the document is written from it ([Anthropic, *Building effective agents*, 19 Dec 2024](https://anthropic.com/engineering/building-effective-agents), read 16 Nov 2026; vendor, documented practice). The same post separates such **workflows**, "orchestrated through predefined code paths", from **agents**, which "dynamically direct their own processes and tool usage" (same page). A pipeline in this unit is a workflow: you fix the stages in advance. Which stages, if any, you then hand to an agent is BW9's question; this unit gives it the procedure to decide on.

Anthropic's current prompting reference keeps the pattern for a narrower case. On 16 Nov 2026 it says that with adaptive thinking and subagents, Claude "handles most multistep reasoning internally", and that explicit chaining "is still useful when you need to inspect intermediate outputs or enforce a specific pipeline structure"; each step is a separate call "so you can log, evaluate, or branch at any point" ([Anthropic, *Prompting best practices*, section "Chain complex prompts"](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/chain-prompts), read 16 Nov 2026; vendor). That is the test for when a pipeline is worth its overhead (stated opinion, built on the two pages above): the work repeats, its parts can be fixed in advance, and you need to see and check what each part produced before the next one builds on it. Work done once, or whose steps change each time, is a brief (BW3), not a pipeline.

**Why one model per stage.** Each stage is one task in one window. BW3 §6 gives the evidence against stacking unrelated tasks in one prompt: each task's material is irrelevant context for the others, and every added instruction competes for adherence. A stage that does one thing can also be routed on its own: BW2's routing table sets a tier and an effort per task, so a stage takes the row for its task (BW2, Deliverable Part 1), written by tier and effort with the model and the date it was read, so that the stage survives a change of lineup (BW2 §7, rule 1). This unit uses BW2's tier words throughout: small, mid, large, and large top rung. A stage that no BW2 row covers says so and names the row it borrows by analogy, as BW3's templates do.

**What a stage is not.** A stage is not a chat that wanders across several tasks, and it is not "the model" in general. If two parts of the work need different material, different models or different checks, they are two stages.

## 2 · Hand-offs as files, not as conversation

Between stages, the output of one becomes the input of the next. The rule this unit uses (stated opinion, on the sources below): **every hand-off is a file**, written by the stage that produced it, read by name by the stage that uses it; no stage takes its input from the conversation of another.

Four reasons; the first three are sourced, and the fourth is an anecdote that illustrates the first.

1. **A new context sees only what it is given.** Across chats nothing persists except what a layer re-inserts (BW1 §3), and BW4 §4's test for leaving a chat is whether a fresh chat could do the next step from the files alone. A stage that must run in a fresh context, such as a check (BW2 §5; BW6 §4), can only be fed by files.
2. **A brief given in pieces does worse than the same brief given whole.** That is Laban and colleagues' measurement across 15 models and six generation tasks, summarised in BW3 §5 ([Laban, Hayashi, Zhou and Neville, *LLMs Get Lost In Multi-Turn Conversation*, arXiv 2505.06120](https://arxiv.org/pdf/2505.06120); preprint). A hand-off made by continuing a conversation feeds the next stage its instructions in pieces, mixed with the last stage's reasoning.
3. **A file can be inspected, logged and re-run from.** Anthropic gives exactly this reason for separate calls: you can "log, evaluate, or branch at any point" (*Prompting best practices*, read 16 Nov 2026). A gate needs something fixed to check; a log needs something to point to (§7).
4. **Files survive the loss of a session.** In Academy (Academy case), a library of self-study courses built by one person with Claude in October and November 2026, whose method writes each unit in its own context from a brief, gives it a fresh check before filing (36 units in the case file's count) and audits by sample, writer agents were lost to container restarts: one deep dive lost two writers, and the third resumed from the second's working files (Academy case file §1, §2, §5, §7). One project, an anecdote; it shows a file hand-off carrying a stage across a lost session.

**What a hand-off file holds.** The output in the form the stage's brief names (BW3 §3, output contracts), and a header that the next stage and the log can read: the stage, the date, the input files it read, the model and version that ran it. The input files are never edited by the stage that reads them; it writes a new file (§6 says why).

**Where the case fell back on conversation.** When this course's first unit, BW1, was given its fresh check, the checker was a separate context that read only its packet; its write of its report was refused, and the chat saved the report from the checker's reply (Academy case file §7). The hand-off still reached a file, but through the conversation of the stage that was meant only to receive it. Nothing in the case file says the report was altered; the point is that the path the file took was not the one the method sets, and only the case file's note records it.

## 3 · The human gate: where it sits and what it checks

A gate is a check an output must pass before the next stage may read it. There are three kinds, and a pipeline uses all three.

| Gate | Who runs it | What it can check | Example |
|---|---|---|---|
| **Code gate** | A script | Anything countable or matchable: length, word count, required headings, every quotation found verbatim in its source, every number present in the source | Anthropic's "programmatic checks" between chained calls (*Building effective agents*) |
| **Model check** | A fresh context, ideally a different model from the writer | Claims against their sources, the output against its brief | BW6's verification protocol, steps B to F |
| **Human gate** | You | Judgement no source can settle: whether the structure serves the reader, which option to take, whether a line is true of you, whether to publish | The final pass (§5) |

Code gates are the cheapest and run on every output. Model checks run where claims must be checked against sources, on BW6's sampling rule. This section is about the third kind, because it is the one with a fixed budget: your attention.

**Where a human gate sits.** Four places, each with its basis.

1. **After a stage whose output fixes everything downstream.** Anthropic's chaining example checks the outline before the document is written from it (*Building effective agents*). BW3's template 7 makes the same cut: a plan is approved before anything is built from it. A structure you approve early costs one reading; a structure you reject after the draft costs the draft.
2. **Before anything irreversible.** Publishing, sending, filing where others will build on it. Once out, a correction is made in the open, with a date and a reason (BW6, Deliverable Part 1, step G).
3. **At BW5's boundaries.** BW5's flag-and-review rule holds every flag raised during the work until a boundary fixed in advance, where you decide each one (BW5 §9 and Deliverable 2e). In a pipeline, the end of each run and the end of each group of runs are those boundaries: a human gate is placed there, and the flags the stages raised are decided there and nowhere else. This unit does not restate the rule; it places the gates on it.
4. **Where the task may be outside what the model does well.** Fabrizio Dell'Acqua and colleagues gave 758 consultants GPT-4 access, with or without a prompt-engineering overview, against a control without AI. On tasks inside what they called the frontier of the model's capability, consultants with AI "completed 12.2% more tasks on average, and completed tasks 25.1% more quickly", with quality more than 40% higher than the control; on a task chosen to fall outside it, "consultants using AI were 19 percentage points less likely to produce correct solutions compared to those without AI" ([Dell'Acqua et al., *Navigating the Jagged Technological Frontier*, Harvard Business School Working Paper 24-013, 22 Sep 2023](https://mitsloan.mit.edu/sites/default/files/2023-10/SSRN-id4573321.pdf); measured; a working paper, GPT-4 in 2023, consulting tasks). The transfer is this unit's inference: you cannot tell in advance which side of the line a given output fell on, so a stage whose output you cannot check by source or by code needs your gate.

**What a human gate checks.** Lines you can answer yes or no, written into the stage before it runs: the stage's own done-when lines (BW3's DONE WHEN; BW5, Deliverable 1d) and the questions only you can answer. A gate that says "review the draft" checks nothing in particular. Each failed line names the stage the output goes back to.

**What a human gate does not do.** It does not re-check what a code gate or a model check already checked; your reading is the scarcest resource in the pipeline, and BW6 §6 already sets how much of a checker's work you re-open. It does not edit the output silently: a change at a gate is a new version of the stage's output file, logged (§7).

## 4 · What the studies on writing with language models found

The stages of a pipeline that produces prose divide into those where a model's contribution is safe to take and those where it changes the writing in ways you may not see. Nine studies bear on where that line falls. None tested a current model, and none tested your material; every transfer below is this unit's inference.

| Study | Models | Task | Finding | Grade |
|---|---|---|---|---|
| Noy and Zhang, *Science* 2023; working paper 10 Mar 2023 | ChatGPT (version not named in the working paper) | 453 college-educated professionals; occupation-specific writing tasks: press releases, short reports, analysis plans, delicate emails | Time down 40%, quality up 18%; time shifted away from rough-drafting toward ideas and editing | Measured |
| Dell'Acqua et al., HBS working paper, 2023 | GPT-4 | 758 consultants; consulting tasks inside and outside the model's frontier | Faster and better inside; 19 points less likely to be correct outside; less variable ideas | Measured (working paper; since published in *Organization Science*, DOI 10.1287/orsc.2025.21838) |
| Doshi and Hauser, *Science Advances* 2024 | GPT-4 | Eight-sentence stories; 293 writers analysed, 600 evaluators | Ideas from the model raised novelty and usefulness, most for the least creative writers; stories became more similar to each other | Measured |
| Padmakumar and He, ICLR 2024 | GPT-3 (davinci), InstructGPT (text-davinci-003) | 38 writers; argumentative essays of about 300 words | InstructGPT, not GPT-3, reduced diversity; the reduction came from the model's text, not the writers' | Measured |
| Chakrabarty, Laban and Wu, arXiv preprint, v5 2025 | GPT-4o, Claude-3.5-Sonnet, Llama-3.1-70b | 18 MFA-trained writers edited 1,057 model paragraphs | 8,035 edits; writer-edited text preferred most | Measured (preprint) |
| Agarwal, Naaman and Vashistha, CHI 2025 | GPT-4o | 118 participants in India and the US; four short culturally grounded essays in English | Suggestions moved Indian participants toward Western styles | Measured |
| Jentzsch and Kersting, WASSA 2023 | ChatGPT | 1,008 jokes requested | Over 90% were the same 25 jokes | Measured |
| Gorenz and Schwarz, *PLOS ONE* 2024 (via a report) | ChatGPT 3.5 | Acronyms, fill-in-the-blank and roast jokes against lay writers; satirical headlines against *The Onion* | Outperformed most lay writers on all three tasks; headlines not significantly different from *The Onion*'s | Measured |
| Jakesch et al., CHI 2023 | GPT-3 (text-davinci-002), steered for or against | 1,506 participants wrote on whether social media is good for society | Writers adopted the model's side about twice as often, and were often unaware of its influence | Measured |

Sources are cited at each finding below.

### Where a model helps: structure, cuts and options

**Structure.** In Shakked Noy and Whitney Zhang's experiment, 453 college-educated professionals did occupation-specific writing tasks, and with ChatGPT "The average time taken decreased by 40% and output quality rose by 18%" ([Noy and Zhang, *Experimental evidence on the productivity effects of generative artificial intelligence*, *Science*, Jul 2023, abstract on Stanford SCALE](https://scale.stanford.edu/publications/experimental-evidence-productivity-effects-generative-artificial-intelligence), read 16 Nov 2026). Their working paper describes how: before treatment participants spent about a quarter of their time brainstorming, half on a rough draft and a quarter editing, and ChatGPT "restructures tasks towards idea-generation and editing and away from rough-drafting"; the share of time on the rough draft fell by more than half ([Noy and Zhang, *Experimental Evidence on the Productivity Effects of Generative Artificial Intelligence*, MIT working paper, 10 Mar 2023](https://economics.mit.edu/sites/default/files/inline-files/Noy_Zhang_1_0.pdf), read 16 Nov 2026; the working paper is not peer-reviewed, and the published abstract read does not carry the restructuring sentence). The tasks were 20 to 30 minutes long and written with the ChatGPT of early 2023. What it supports for a pipeline (inference): the model takes the rough-draft work, and your time moves to choosing and editing, which is where the gates are. The study measured time and graded quality, not the model's arranging of a text; grade for structure: stated opinion, built on this finding and Anthropic's outline example (§1).

**Cuts.** No study found measures a model cutting a writer's own text. Two findings bear on it indirectly. Vishakh Padmakumar and He He found that the loss of diversity in co-written essays "is mainly attributable to InstructGPT contributing less diverse text", while "user-contributed text remains unaffected by model collaboration" ([Padmakumar and He, *Does Writing with Language Models Reduce Content Diversity?*, ICLR 2024, pp. 642–669](https://proceedings.iclr.cc/paper_files/paper/2024/hash/02dec8877fb7c6aa9a79f81661baca7c-Abstract-Conference.html), read 16 Nov 2026). A stage that selects and reorders your sentences, and writes none of its own, adds no model text for that effect to work on (inference). And the professional writers in Chakrabarty and colleagues' study (below) spent 18% of their edits removing unnecessary or redundant exposition from model paragraphs: a model writing its own prose tends to need cutting, which argues for giving it your text to cut rather than asking it to write and cutting after. Grade for cuts: stated opinion, built on those two findings.

**Options.** Anil Doshi and Oliver Hauser had writers produce eight-sentence stories with no AI, with one idea from GPT-4, or with up to five; 600 evaluators rated them, and 293 writers were analysed. Writers with up to five ideas wrote stories rated 8.1% more novel and 9.0% more useful than those with none, and less creative writers gained more: 10.7% in novelty and 11.5% in usefulness ([Doshi and Hauser, *Generative AI enhances individual creativity but reduces the collective diversity of novel content*, *Science Advances* 10, eadn5290, 12 Jul 2024](https://ore.exeter.ac.uk/rest/bitstreams/199326/retrieve), repository copy read 16 Nov 2026; measured). Fiction, rated by strangers, with GPT-4 as it was before the paper's submission on 14 December 2023. The transfer (inference): ask a stage for several options where you have least practice, and choose at a gate. The same study gives the cost, below.

### Where a model flattens: first-person prose, humour and endings

**First-person prose.** Five studies point the same way: text the model writes pulls writing toward the model's average.

- *The reduction comes from the model's sentences.* Padmakumar and He's 38 writers wrote argumentative essays of about 300 words alone, with GPT-3 (davinci) or with InstructGPT (text-davinci-003); writing with InstructGPT "(but not the GPT3) results in a statistically significant reduction in diversity" ([arXiv v3](https://arxiv.org/html/2309.05196v3), read 16 Nov 2026), and the effect sits in the model's contributed text (above).
- *Ideas converge too.* In Doshi and Hauser's study the stories written with the model's ideas were more similar to each other; the paper expresses the increase for one and five ideas as "10.7% and 8.9% of the total range" of its similarity score, and describes the result as resembling a social dilemma: each writer gains, and the collection loses variety (repository copy, read 16 Nov 2026). Dell'Acqua and colleagues report the same in their consultants' ideas: "a marked reduction in the variability of these ideas compared to those not using AI" (working paper, §3.1, read 16 Nov 2026).
- *Professional writers rewrite model prose heavily.* Tuhin Chakrabarty, Philippe Laban and Chien-Sheng Wu had 18 writers with MFA backgrounds edit 1,057 paragraphs written by GPT-4o, Claude-3.5-Sonnet and Llama-3.1-70b, gathering 8,035 edits, "about 8 edits per paragraph"; the four largest of seven categories were awkward word choice and phrasing (28% of edits), poor sentence structure (20%), unnecessary or redundant exposition (18%) and clichés (17%) (§5.1). They warn of "a reduction in linguistic diversity and individual voice" (§7.4) ([Chakrabarty, Laban and Wu, *Can AI writing be salvaged? Mitigating Idiosyncrasies and Improving Human-AI Alignment in the Writing Process through Edits*, arXiv 2409.14509 v5, 4 Mar 2025](https://arxiv.org/html/2409.14509v5), read 16 Nov 2026; preprint, no venue on the copy read).
- *The model's style displaces the writer's own.* Dhruv Agarwal, Mor Naaman and Aditya Vashistha had 118 participants from India and the United States write four short essays in English, with or without GPT-4o's inline suggestions: "AI suggestions led Indian participants to adopt Western writing styles", "altering not just what is written but also how it is written" ([Agarwal, Naaman and Vashistha, *AI Suggestions Homogenize Writing Toward Western Styles and Diminish Cultural Nuances*, arXiv 2409.11360 v3](https://arxiv.org/html/2409.11360v3), read 16 Nov 2026; the paper's ACM reference line names CHI '25, Yokohama).

The four largest kinds of edit the professional writers made, by share of all edits:

```viz
{"kind": "compare", "unit": "%", "max": 30,
 "rows": [
  {"label": "Awkward word choice and phrasing", "value": 28, "tone": 5},
  {"label": "Poor sentence structure", "value": 20, "tone": 5},
  {"label": "Unnecessary or redundant exposition", "value": 18, "tone": 5},
  {"label": "Clichés", "value": 17, "tone": 5}
 ],
 "caption": "§4: the four largest of seven categories among 8,035 edits that 18 professional writers with MFA backgrounds made to 1,057 paragraphs from GPT-4o, Claude-3.5-Sonnet and Llama-3.1-70b. Chakrabarty, Laban and Wu, Can AI writing be salvaged?, arXiv 2409.14509 v5 (preprint), §5.1, read 16 Nov 2026."}
```

What the five have in common (inference): the flattening is carried by the sentences the model writes, and a writer's sentences used as they are do not carry it. A stage that drafts first-person prose for you is the stage most likely to change how you sound without your noticing.

**Humour.** Two studies, measuring different things. Sophie Jentzsch and Kristian Kersting asked ChatGPT for jokes 1,008 times: "Over 90% of 1008 generated jokes were the same 25 Jokes" ([Jentzsch and Kersting, *ChatGPT is fun, but it is not funny! Humor is still challenging Large Language Models*, WASSA 2023, pp. 325–340](https://aclanthology.org/2023.wassa-1.29), read 16 Nov 2026; the paper describes the model as GPT-3-based). Drew Gorenz and Norbert Schwarz compared ChatGPT 3.5's jokes with those of lay writers on three tasks and found that it outperformed 73% of the human participants on acronyms, 63% on fill-in-the-blank prompts and 87% on roast jokes, and that its satirical headlines did not differ significantly in rated funniness from *The Onion*'s (*PLOS ONE*, 2024, as reported by Eric W. Dolan in [PsyPost, *AI outshines humans in humor: Study finds ChatGPT is as funny as The Onion*, 4 Jul 2024](https://www.psypost.org/ai-outshines-humans-in-humor-study-finds-chatgpt-is-as-funny-as-the-onion/), read 16 Nov 2026; the paper itself was not opened). Read together: one measures whether strangers laugh at a joke on a set prompt; the other whether the model's jokes vary. Neither measures whether a joke sounds like a particular person. For a pipeline (stated opinion): a joke in your voice is a claim about how you talk, and a stage that writes it is inventing that claim. The model may mark a line in your material that you meant as a joke; it writes none.

**Endings.** No study found measures endings directly. The nearest evidence concerns conclusions. Maurice Jakesch and colleagues had 1,506 participants write on whether social media is good for society, with GPT-3 (text-davinci-002) prompted to argue one side; those with the supportive model were "2.04 times more likely than control group participants" to argue that it is good, and those with the critical model "2.0 times more likely" to argue that it is bad; their opinions in a later survey moved too, and "participants were often unaware of the model's opinion and influence" ([Jakesch, Bhat, Buschek, Zalmanson and Naaman, *Co-Writing with Opinionated Language Models Affects Users' Views*, CHI 2023, arXiv 2302.00560](https://arxiv.org/pdf/2302.00560), read 16 Nov 2026). An ending is where a text states what it means. The transfer (inference): a stage that drafts your ending supplies your conclusion, and the evidence suggests you may not notice it was supplied.

The division of the work that follows (stated opinion, on the findings above), used by every pipeline in the Deliverable. For structure, cuts of your own text and options, the model's stage drafts and its output is taken, then gated: you approve the structure, check the cuts and choose among the options. For first-person prose, humour and the ending, the model writes none of the final words: in first-person text it may write a marked bridge only (defined below), it never writes humour, and for the ending it points to candidates in your material; you write the prose and the humour and decide the ending.

```viz
{"kind": "matrix",
 "cols": ["The model's stage", "Your gate"],
 "rows": [
  {"label": "Structure: order, outline, sections", "cells": [{"mark": "drafts", "tone": 2}, {"mark": "approves", "tone": 4}]},
  {"label": "Cuts of your own text", "cells": [{"mark": "drafts", "tone": 2}, {"mark": "checks", "tone": 4}]},
  {"label": "Options", "cells": [{"mark": "drafts", "tone": 2}, {"mark": "chooses", "tone": 4}]},
  {"label": "First-person prose", "cells": [{"mark": "marked bridge only", "tone": 1}, {"mark": "writes", "tone": 4}]},
  {"label": "Humour", "cells": [{"mark": "never", "tone": 1}, {"mark": "writes", "tone": 4}]},
  {"label": "The ending", "cells": [{"mark": "points to candidates", "tone": 1}, {"mark": "decides", "tone": 4}]}
 ],
 "legend": [
  {"mark": "drafts", "means": "the model's output is taken, then gated", "tone": 2},
  {"mark": "bridge, never, points", "means": "the model writes none of the final words", "tone": 1},
  {"mark": "your marks", "means": "you approve, check, choose, write or decide", "tone": 4}
 ],
 "caption": "§4's division of the work. Structure from Noy and Zhang (2023) and Anthropic's chaining example; cuts from Padmakumar and He (ICLR 2024) and Chakrabarty, Laban and Wu (arXiv 2409.14509); options from Doshi and Hauser (Science Advances, 2024); first-person prose from those three and Agarwal, Naaman and Vashistha (CHI 2025); humour from Jentzsch and Kersting (WASSA 2023) and Gorenz and Schwarz (PLOS ONE, 2024, via PsyPost); the ending from Jakesch et al. (CHI 2023). The division itself is this unit's (stated opinion)."}
```

A **marked bridge** is one sentence the model may write to join two of yours, tagged so that a code gate finds it and you rewrite or cut it at the final pass. It is the only model-written sentence the division allows into first-person text.

## 5 · The rule that the final pass is yours

The rule (stated opinion, on the evidence below): **nothing leaves the pipeline until you have made the last pass over it**, and that pass is a short list of lines you answer yes or no. It is the last human gate, and it is never handed to a model or an agent.

Four things support it.

1. **Edited text was preferred, and unedited model text was least preferred.** In Chakrabarty and colleagues' preference study, writer-edited paragraphs were marked the most preferred variant "65% of the time", and unedited model paragraphs were "least preferred 60% of the time" (§6.3, arXiv v5, read 16 Nov 2026; preprint). Their writers edited model prose; your final pass may be mostly over your own arranged text, so the transfer is partial (inference).
2. **Influence passes unnoticed.** Jakesch and colleagues' writers were often unaware of the model's opinion and influence (§4). A gate that relies on noticing will miss what was not noticed; a gate that asks a fixed question ("is the ending a line I wrote?") does not rely on noticing.
3. **A model grades its own work too kindly, and does not reliably correct itself without outside input.** BW2 §5 gives the studies; BW6 §4 what a fresh context removes and what it does not. A model check is a check on sources; it is not a check on whether the text is yours.
4. **Outside the frontier, the output looks as good and is wrong more often.** Dell'Acqua and colleagues' 19-point drop (§3) was on a task designed so that GPT-4 would make an error, and the AI users' recommendations were still rated higher in quality whether or not they were correct. The final pass is where you ask whether this run's output is one you could defend.

**What the final pass contains.** Only lines no earlier gate covers (this unit's list; each line traces to §4 or to BW6):

- every marked bridge is rewritten in your words or cut;
- every line of humour is one you made;
- the ending is yours, chosen by you;
- every first-person statement is one you would make;
- every open item the model check left (BW6, Deliverable Part 1, steps F and G) is closed;
- the output meets the brief's purpose for its reader, read as that reader would;
- the run's log line is written (§7).

**What it costs.** No source measures the time a final pass takes on any task in this unit; the case file holds no measure of hours per unit (Academy case file §9). Keep the list short enough to answer in one sitting, and move any line a script can answer into a code gate.

## 6 · Steps that can be re-run without harm

A stage will be run again: its model check fails, a session is lost, a source changes, a better model arrives. A pipeline is safe to re-run only if each stage can be repeated without damaging anything that came before or after it.

The practice comes from data engineering, where the scheduler retries failed tasks. Apache Airflow's best-practice page says: "You should treat tasks in Airflow equivalent to transactions in a database", which means "you should never produce incomplete results from your tasks", and "the tasks should produce the same outcome on every re-run"; it warns against a step that appends ("Do not use INSERT during a task re-run", which may duplicate rows) and against reading "the latest available data", recommending a fixed partition instead ([Apache Airflow, *Best Practices*, documentation version 2.3.3](https://airflow.apache.org/docs/apache-airflow/2.3.3/best-practices.html), read 16 Nov 2026; documented practice in data engineering, not written for language models; an older documentation version).

**What changes with a model in the stage.** A model stage cannot "produce the same outcome on every re-run": the same window can produce a different text on each run (BW1 §5). Re-runnable, for a model stage, means three things (this unit's adaptation, stated opinion):

1. **Same inputs, named.** The stage reads named, dated files, never "the latest draft" or whatever is in the chat. Airflow's fixed partition becomes a file name with a version.
2. **A new output, never an edit in place.** The stage writes a new versioned file (`draft-v2`), and never appends to or edits its input; a re-run replaces only its own output. That is Airflow's warning against INSERT: an appended re-run leaves two outputs mixed in one file.
3. **Everything downstream is re-gated.** Because the new output is a new draw, every gate after it runs again on it, and nothing downstream built on the old version stands until it does. "Same outcome" becomes "same contract, passed again".

A stage that cannot meet these (one that sends an email, publishes a page, posts) is not re-runnable, and is marked so in the procedure: it runs only after the final pass, once.

**The case.** Two of Academy's loops show re-running in practice (anecdote). A figure that failed its check was fixed and checked again by a new agent; under the early rule a figure failing three times was dropped (two were), and under the later rule set by the owner figures are fixed until they pass, and one sitemap figure passed on its eighth check (Academy case file §6). And a lost writer was resumed from working files (§7). The case recorded them in place: each figure's check count in its unit's course-index row and in the fresh-check report's maintainer note, and a row run again as its own changelog row (Academy case file §6); how to log a re-run is the next section's subject.

## 7 · Logging what ran

A pipeline's log is one line per stage run. BW5 §7's changelog records each finished row of work; the run log records each stage inside it, so that when an output is wrong you can say which stage made it, from which inputs, on which model.

**What a line holds** (this unit's form, stated opinion; each field traces to the source named):

| Field | Why | Source |
|---|---|---|
| Date and time | Order of runs; the six-month re-check | BW2 §7 |
| Stage and run number | Which stage, which attempt | §6 above |
| Input files, with versions | What the stage could see | BW1 §1; §2 above |
| Model, version and effort | What actually ran, not what was intended | BW2 §7, rule 5; BW6 §6, rule 5 |
| Output file | What the next stage read | §2 above |
| Gate and result | Pass, fail, and back to which stage | §3 above |
| Who ran the gate | You, a script, or which checker | BW6 §6 |

Anthropic's reason for chaining is the same: each step separate "so you can log, evaluate, or branch at any point" (*Prompting best practices*, read 16 Nov 2026; vendor).

**Why the model field records what ran.** In the case, a session's model named "fable" resolved to a newer version than the method names, so the checks it ran were recorded as owed again on the named version (Academy case file §7). A log that had recorded only the requested name would have shown those checks as done. **Why the log keeps evidence of what was read.** Some sessions kept no agent transcript on disk, so scripted checks of what each agent had read could not run, and the agents' own reports stood in their place (Academy case file §7; BW6 §6, rule 6). Both are anecdotes from one project; they show two ways a log without the right field stops being evidence.

## 8 · The Academy case's pipeline, and where it failed

Academy's method, read as a pipeline (anecdote: one project, one person, no control; Academy case file §9). Each stage below is as the case file records it; where it records nothing, the cell says so. The case's flow of a unit through the method is in BW5 §10; this section reads the same method stage by stage for its inputs, outputs, models, gates and failures.

| Stage | Input → output | Model | Gate | Where it failed (case file) |
|---|---|---|---|---|
| 1 · Brief | Shared preamble + unit brief, never reworded (§2) → one self-contained brief | None recorded | Not recorded | No failure recorded at this stage |
| 2 · Writer | The brief and the units already filed (§2) → the unit, a long-form report with sources cited in place and a deliverable built in full (§1), and up to ten unverified claims (§2) | Opus 5.5 (§2) | The writer's own pass: the sourcing checklist (§2) | Writers lost to container restarts; one deep dive lost two, and the third resumed from the second's working files (§7). Before the fresh check existed, Audit 1 found three units whose deliverables did not exist and two table rows resting on figures the cited vendor pages did not contain (§3) |
| 3 · Fresh check | The unit, in a context that has not seen it written (§2) → findings graded error, should-fix and minor; it never edits (§2) | Fable 5.1 on 19 drafts, Opus 5.5 on 12, Fable 5.2 on 5 (§5) | Model check | 28 of 36 drafts had at least one error; 58 errors in all (§5). A "fable" session resolved to a newer version, and its checks were recorded as owed again (§7). BW1's checker could not write its report; the chat saved it from the reply (§7) |
| 4 · Applying findings | The unit and the findings → the corrected unit | Until 14 Nov 2026 the chat that orchestrated and filed the row, recorded as "the maintainer", on Opus 5.5 except in three UX rows; from 15 Nov 2026 a separate Opus 5.5 agent, the applier (§2) | Human or maintainer gate: each finding verified, then applied as an exact replacement (§2) | No failure recorded at this stage |
| 5 · Filing | The corrected unit → the unit filed; the backlog row moved to the changelog; the writing model recorded (§2) | None recorded | Not recorded | No failure recorded at this stage |
| 6 · Build | The repository → the website, built by script; no page styled by hand (§1); figures declared as data and drawn by script (§6) | None: a script (§1, §6) | Code: the build's verify script (§1) | Not recorded |
| 7 · Checks | Each figure against the unit's text (§6) | A separate Opus 5.5 agent (§6) | Model check: every label and number must already be in the text (§6) | Figures failed and were re-checked by new agents; two were dropped under the early rule; one sitemap passed on its eighth check (§6). Some sessions kept no transcript, so scripted checks of what agents had read could not run (§7) |
| 8 · Publishing | The built site → one website with one design, published first as an artifact on claude.ai and then on GitHub Pages (§1) | Not recorded | Code: the verify script, the course-index check and the private-terms check must pass, then the publish is read back by sha256 (§1) | A structure audit of the project found private terms (words meant to stay out of the public site) reaching a public build (§7) |

```viz
{"kind": "flow",
 "steps": [
  {"label": "Brief", "note": "never reworded", "tone": 3},
  {"label": "Writer", "note": "writers lost to restarts", "tone": 1},
  {"label": "Fresh check", "note": "28 of 36 drafts with an error", "tone": 2},
  {"label": "Applying findings", "note": "each verified, exact replacement", "tone": 3},
  {"label": "Filing", "note": "row to changelog, model recorded", "tone": 3},
  {"label": "Build", "note": "by script", "tone": 3},
  {"label": "Checks", "note": "a sitemap passed on its eighth check", "tone": 1},
  {"label": "Publishing", "note": "private terms reached a public build", "tone": 1}
 ],
 "caption": "§8: the Academy case's method read as eight stages, with the failure the case file records at each where it records one. From the table in §8 of this unit; Academy case file §1, §2, §5, §6, §7 (one project, an anecdote)."}
```

**What the failures share.** Read against §2 to §7 (this unit's reading, stated opinion):

- **Hand-offs as files held where they were used.** The lost writers were recovered because the second writer's working files existed (§2 above). The one hand-off that went through conversation, BW1's check report, is the one the record had to annotate.
- **The gates the case file records sit before filing; before publishing it records only scripts.** The fresh check found an error in 28 of 36 drafts before filing (Academy case file §5); Audit 1's missing deliverables are the failure a writer stage produces when no gate checks the output against its brief (§3). The private terms in a public build (§7) are what a publishing stage produces without a gate of its own; one was added on 11–12 Nov 2026, after the structure audit: a script that fails the build on a private term in a public course, now among the scripts that must pass before a publish (§1, §7).
- **The log was missing two fields.** The model that actually ran, and the evidence of what each agent read (§7 above).
- **Re-running worked where the stage wrote a new version and was re-checked from scratch.** The figure loop (§6).

**What the case cannot show.** No unit was written without the method, so nothing here shows the pipeline beats a lighter one; there is no measure of hours or money per unit (Academy case file §9). The case shows one person running these stages, with a fresh check before filing on 36 units (§5), and where they broke.

## 9 · On other tools

The principles of §1 to §7 (fixed stages, one model per stage, file hand-offs, three kinds of gate, a final pass that stays yours, re-runnable stages, a run log) need no particular product. Their evidence is from studies of several vendors' models and from data-engineering practice. What is specific to a vendor, as read on 16 November 2026:

| Claim in this unit | Claude | ChatGPT and OpenAI | Gemini and Google |
|---|---|---|---|
| Chaining fixed steps, each working on the last one's output, with checks between (§1) | Prompt chaining with programmatic "gate" checks: [*Building effective agents*](https://anthropic.com/engineering/building-effective-agents) (Dec 2024; the page notes its tooling has changed since) | OpenAI Agents SDK: "Chaining multiple agents by transforming the output of one into the input of the next", e.g. research, outline, write, critique, improve: [*Agent orchestration*](https://openai.github.io/openai-agents-python/multi_agent/) | Vertex AI documentation: "make each step a prompt and chain the prompts together in a sequence", where "the output of one prompt in the sequence becomes the input of the next prompt": [*Break down complex tasks into simpler prompts*](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/break-down-prompts) (last updated 12 Nov 2026) |
| Explicit chaining for inspecting intermediate outputs, logging each step (§1, §7) | "so you can log, evaluate, or branch at any point": [*Prompting best practices*](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/chain-prompts) | No equivalent sentence found on the page read | Smaller prompts "can help you improve controllability, debugging, and accuracy": same Vertex AI page |
| A check run in a loop until the output passes (§3, §6) | Self-correction chain: draft, review against criteria, refine, each a separate call (*Prompting best practices*) | An evaluator agent in a loop that stops "when the evaluator says the output passes the required criteria" (*Agent orchestration*) | Not found on the page read |
| A fresh context for the check (§3) | BW6 §4 | As BW6 §8 records: not checked | As BW6 §8 records: Gemini CLI subagents |

Two limits. The OpenAI and Google pages are developer documentation for code that calls a model; neither describes the consumer chat products (ChatGPT, the Gemini app), whose pages were not read for this unit. Google's Gemini API page on prompt design strategies could not be fetched on 16 Nov 2026 and was not checked. In any chat product the pipeline in this unit can be run by hand: one chat per stage, files saved and attached by you, gates run by you or by a script; BW8 turns one stage of the procedure, the fresh check, into a skill.

## Deliverable · A pipeline written as a runnable procedure

Three parts. Part 1 is the Academy case's pipeline, written as a procedure you could run: numbered steps, each with its input, output, model, gate, done-when lines, a re-run rule and a log line. Part 2 is a short second pipeline on neutral material, interview notes to a report, a summary and an email, whose content is invented and labelled so. Part 3 is the template for your project. BW8 turns one stage in this form into a skill and schedules a different, date-driven check; BW9 decides which of its steps an agent may take.

Conventions, as in BW3 to BW6. Every fact about Academy comes from the Academy case file and is cited by section; where the case file holds no value, the cell says `[NOT IN CASE FILE: …]`, a blank for the project's owner and never a claim. Anything marked **(proposal)** is this unit's addition to what the case records (stated opinion, traced to the section named). File paths are this unit's naming, after BW4's Part 3 folders and BW5's `records/`; the paths of the case's own that the case file names (`docs/courses-index.md`, `docs/method.md`, `docs/CHANGELOG.md`, `docs/project-instructions.md`, `courses/building-with-ai/` and files under `audits/building-with-ai/`; Academy case file header, §1, §2, §5) are not used here. The **Model** line gives a BW2 routing-table row by tier and effort, with the model in that tier as BW2 read it on 15 Nov 2026; where BW2 has no row, it says so and names the row borrowed. Gate kinds are §3's: **code**, **model check**, **human**.

### Part 1 · The Academy case's pipeline

**Pipeline card**

- **What it produces:** one unit of a course: a long-form report in Markdown, 2,000 to 6,000 words by guide, sources cited in place, a closing deliverable built in full (Academy case file §1).
- **Trigger:** one backlog row; every chat works one row (§2).
- **Stages:** 1 Packet, 2 Write, 3 Fresh check, 4 Apply findings, 5 File, 6 Build, 7 Checks, 8 Publish (§8 of this unit).
- **Boundaries** (BW5 §9): the end of each unit's run, at step 8's gate; and every four units, at the sample audit (case file §2; audits 3 onward had not run at 11 Nov 2026, and on 15 Nov 2026 the owner retired the four-unit audit, case file §9). Flags raised by any step wait for one of these.
- **Run log:** `records/run-log.md`, one line per step run (§7). **(proposal;** the case file records a changelog per row, §2, and no per-step log**)**

#### Step 0 · Before the run

- [ ] The unit's brief exists, with the course's shared preamble (case file §2).
- [ ] Every unit the brief's Takes line names is filed (case file §2: the writer sees "the units already filed").
- [ ] No open flag touches this unit (BW5 §9, step 5).
- [ ] `records/run-log.md` exists.

#### Step 1 · Packet

- **Input:** `briefs/<course>/preamble.md`, `briefs/<course>/<code>.md`, the filed units the Takes line names, the sourcing standard.
- **Output:** `packets/<code>/` holding `brief.txt` (preamble, then unit brief) and the files above, nothing else.
- **Model:** none; a script copies (proposal, so that no model can reword the brief).
- **Gate (code):** `brief.txt` matches the approved brief character for character (case file §2: one brief per unit, never reworded).
- **Done when:** the packet holds only the brief and the units already filed, as the method sets (case file §2).
- **Re-run:** safe; rebuilt from the same files.
- **Log:** date · 1 Packet · run n · inputs and their versions · script · gate pass/fail.

#### Step 2 · Write

- **Input:** `packets/<code>/`, in a new chat or a fresh agent context (case file §2).
- **Output:** `packets/<code>/out/unit-v1.md` and `unsure.md` (up to ten claims the writer could not verify, case file §2).
- **Model:** BW2 row 4, a long first draft · large · Opus 5.5, high. The case records Opus 5.5 as the writing model (§2) and not the effort (`[NOT IN CASE FILE: effort per unit]`).
- **Gate (code):** the file has a Sources list and a Deliverable heading; `unsure.md` has at most ten items. **(proposal;** from the case's Audit 1, where three deliverables did not exist, case file §3**)**
- **Done when:** the writer's own pass is done: the sourcing checklist run and the unsure list written (case file §2); BW5 Deliverable 1d, its first four lines.
- **Re-run:** safe in a new context from the packet. A writer lost mid-run is resumed from its working files, as the case's third writer was (case file §7); the resumed run writes `unit-v1.md` afresh and the log records both runs.
- **Log:** date · 2 Write · run n · packet version · model and version as run, effort · `unit-v1.md` · code gate result.

#### Step 3 · Fresh check

- **Input:** `unit-v1.md`, `brief.txt`, the sourcing standard; never the writer's conversation (case file §2: a context that has not seen the unit written).
- **Output:** `checks/<code>-fresh-check.md`: findings graded error, should-fix and minor; the checker edits nothing (case file §2). Each finding gives the current text and its replacement, so step 4 can apply it as an exact replacement (proposal; the case file records only that findings are applied that way, §2).
- **Model:** BW2 row 5, critique of a draft · large top rung · Fable 5.2, high, in a fresh context; override: Opus 5.5, high, in a fresh context; the log records that the checker ran on the writer's model. The case ran Fable 5.1 on 19 drafts, Opus 5.5 on 12, Fable 5.2 on 5 (case file §5).
- **Gate (code):** the report file exists, written by the checker itself, and names the model and version that ran. **(proposal;** from BW1's check, whose report was saved from the checker's reply, and the "fable" session that resolved to a newer version, case file §7**)**
- **Done when:** every cited claim has been checked against its source and the deliverable against the brief (case file §2); BW6, Deliverable Part 1, steps D and E.
- **Re-run:** safe; a new context writes `-fresh-check-v2.md`. A check whose model resolved to another version than the one named is recorded as owed again on the named version (case file §7).
- **Log:** date · 3 Fresh check · run n · `unit-v1.md` · model requested, model and version as run · report path · verdict and counts.

#### Step 4 · Apply findings

- **Input:** `unit-v1.md` and the check report.
- **Output:** `unit-v2.md` and `checks/<code>-decisions.md`: for each finding, applied, changed or rejected, with the reason.
- **Model:** in the case, until 14 Nov 2026, the chat that orchestrated and filed the row, recorded as "the maintainer", on Opus 5.5 except in three UX rows (two on Fable 5.1, one on Fable 5.2); from 15 Nov 2026 a separate Opus 5.5 agent, the applier (case file §2). BW2 has no row for applying verified replacements; the reading is row 5's kind of work and the edit is mechanical.
- **Gate (maintainer; in the case the filing chat, then the applier, case file §2):** each finding is verified at its source before it is applied, and applied as an exact replacement (case file §2; BW6 §6, rule 1).
- **Done when:** every finding has a decision line; every applied replacement is found once in `unit-v2.md`.
- **Re-run:** safe; it starts again from the unchanged `unit-v1.md` and the report.
- **Log:** date · 4 Apply · run n · report path · applied / changed / rejected counts · who verified.

#### Step 5 · File

- **Input:** `unit-v2.md`.
- **Output:** the unit in the course's folder; the backlog row moved to the changelog with the date, the model that wrote the unit and a one-line result; the prompt for the next chat (case file §2; BW5 §7).
- **Model:** none recorded in the case file.
- **Gate (code):** the changelog row names a model; the row is no longer in the backlog (BW5 §7: a row in both files is a row nobody knows the state of).
- **Done when:** BW5 Deliverable 1d, its last two lines.
- **Re-run:** safe if filing replaces the unit's file rather than adding a second copy (§6).
- **Log:** date · 5 File · unit path · changelog row.

#### Step 6 · Build

- **Input:** the repository (case file §1).
- **Output:** the site's files, built by script, with no page styled by hand; figures declared as data in the units and drawn by script (case file §1, §6).
- **Model:** none; a script.
- **Gate (code):** the build completes. In the case the build is checked by its verify script (case file §1).
- **Done when (proposal):** every filed unit has its page.
- **Re-run:** safe by construction: the output is rebuilt from source and never edited in place (§6; BW4 §5).
- **Log:** date · 6 Build · commit or folder version · pass/fail.

#### Step 7 · Checks

- **Input:** the built pages and each unit's text.
- **Output:** `checks/<code>-figures.md` (one verdict per figure) and `checks/<code>-terms.md`.
- **Model:** for the figure check, a separate agent (case file §6), Opus 5.5 for every check and re-check; BW2 has no row, and row 5 (critique against a text) is the nearest. The terms check: none, a script.
- **Gate (model check):** every label and number in a figure is already in the unit's text (case file §6). A figure that fails is fixed and checked again by a new agent, until it passes; figures are never dropped (case file §6).
- **Gate (code) (proposal):** search the built output for every term on a private list kept outside the repository; pass if nothing is found. From the structure audit that found private terms reaching a public build (case file §7); the check is BW4's rot-check step 6.
- **Done when:** every figure has passed; the terms search has found nothing.
- **Re-run:** safe; each re-check is a new agent and a new verdict file (case file §6).
- **Log:** date · 7 Checks · figure id · check n · verdict; terms search · count found.

#### Step 8 · Publish

- **Input:** the built site that passed step 7.
- **Output:** the published site (case file §1). In the case, after each filing the site is rebuilt, verified and published in two places, first as an artifact on claude.ai and then on GitHub Pages (case file §1).
- **Model:** none.
- **Gate (human) (proposal; the case's own gates here are scripts: the verify script, the course-index check and the private-terms check must pass, then the publish is read back by sha256, case file §1):** the final pass of §5, answered yes on each line for the new unit:
  - [ ] Every finding in `checks/<code>-decisions.md` has a decision, and every rejection a reason.
  - [ ] Every line on `unsure.md` is either sourced now, said in the unit to be unsourced, or cut.
  - [ ] Every figure has passed, and the terms search found nothing.
  - [ ] The unit's deliverable is built in full and answers its brief, read as the course's reader would.
  - [ ] The flags this run raised are written down for the next boundary (BW5 §9).
  - [ ] The log has a line for every step of this run.
- **Done when:** the gate's lines are all yes and the site is live.
- **Re-run:** **not re-runnable.** Once published, a correction is made in the open, with the date and the reason (BW6, Deliverable Part 1, step G).
- **Log:** date · 8 Publish · what went live · gate answered by.

#### Every four units · Boundary

The sample audit: one claim drawn from every section of each unit and checked against its source; a unit with more than one sampled claim in ten failing is audited in full; verdicts pass, full audit, rewrite (case file §2; BW6 §5). This is the pipeline's second boundary: open flags are decided here (BW5 §9). Model: BW2 row 9, an audit against sources · large top rung · Fable 5.2, high, a model other than the writer's; the method names Fable 5.1 (case file §2). In the case the owner retired this audit on 15 Nov 2026, leaving the fresh check and the staleness check as the guards (case file §9).

#### The run log, on the case

Lines the case file supports, in §7's form. Every blank is a field the case did not record, which is the point of keeping it.

| Date | Step · run | Inputs | Model as run | Output | Gate · result |
|---|---|---|---|---|---|
| 2–3 Nov 2026 (case file §8) | 2 Write · run 3, one deep dive | The packet and the second writer's working files | Opus 5.5 (case file §5, §8) | The unit | Resumed after two writers were lost to container restarts (case file §7) |
| `[NOT IN CASE FILE]` | 3 Fresh check · `[NOT IN CASE FILE: unit]` | `[NOT IN CASE FILE]` | Requested "fable"; resolved to a newer version than the method names | Findings | Recorded as owed again on the named version (case file §7) |
| 15 Nov 2026 | 3 Fresh check · BW1 | The checker's packet only | Opus 5.5 (case file §5) | Report saved by the chat from the checker's reply; the checker's write was refused | Run from a Claude Code session on claude.ai (case file §7) |
| `[NOT IN CASE FILE]` | 7 Checks · a sitemap figure, check 8 | The unit's text | A new Opus 5.5 agent each time (case file §6) | Verdict | Pass on the eighth check (case file §6) |

### Part 2 · A second pipeline, on neutral material

**Everything in this part's content is invented** for the example: the project, the interviews, the quotes, the names of themes and the numbers. Only the procedure is the unit's.

**Pipeline card (invented example).** A researcher runs eight 40-minute interviews with operations managers at regional food wholesalers about late deliveries. From the notes, the pipeline produces a findings report of about 3,000 words for the client, a one-page summary for the client's director, and a thank-you email to the eight interviewees. It runs once per study, about four times a year. Boundaries: after step 3 (the structure) and at step 8 (the final pass). Log: `records/run-log.md`.

| Step | Input → output | Model (BW2 row) | Gate | Done when | Re-run |
|---|---|---|---|---|---|
| **1 · Tidy notes** | `notes/raw/int-01.md` … `int-08.md` → `notes/clean/int-0n.md`, headings added, every word kept | Row 1 · small · Haiku 5.5, low | **Code:** the clean file holds every word of the raw file, in order | Eight clean files, each passing | Safe |
| **2 · Extract** | The clean notes → `records/quotes.md`: one row per quote, with interview, quote and theme | Row 2 · small · Haiku 5.5, high; counts by script | **Code:** every quote is found verbatim in its interview's clean file; theme counts computed by script | Every row passes; no quote paraphrased | Safe; writes `quotes-v2.md` |
| **3 · Structure options** | `quotes.md` → `outline-v1.md`: three outlines for the report, each with its sections and the quotes each section uses | Row 10 · large · Opus 5.5, high (a plan) | **Human:** you choose one outline, or merge two, and approve its section list (§4, structure and options; §3, place 1) | One approved outline, saved as `outline-approved.md` | Safe; boundary: flags decided here |
| **4 · Draft findings** | `outline-approved.md`, `quotes.md` → `report-v1.md`: the findings sections only; any joining sentence tagged `[BRIDGE]`; the recommendations and the closing section left as `[YOURS]` | Row 4 · large · Opus 5.5, high | **Code:** quotes verbatim; `[YOURS]` present for recommendations and close; `[BRIDGE]` lines counted | Every finding section drafted; the two `[YOURS]` slots untouched | Safe; writes a new draft version (`report-v1b.md`); steps 5 to 8 re-run on it |
| **5 · Fresh check** | `report-v1.md`, the clean notes → `checks/report-check.md`, then the verified findings applied → `report-v2.md` | Row 5 · large top rung · Fable 5.2, high, fresh context | **Model check**, then **human:** each finding verified before it is applied (BW6 §6, rule 1) | BW6, Deliverable Part 1, steps D to F | Safe; new report file |
| **6 · Your sections** | `report-v2.md` → `report-final.md` | None: you | **Human:** you write the recommendations and the close; every `[BRIDGE]` rewritten or cut (§4, first-person prose and the ending) | No tag left; the code gate finds none | Safe |
| **7 · Summary and email draft** | `report-final.md` → `summary-v1.md` (one page) and `email-v1.md` (three subject lines and a skeleton with slots) | Summary: row 3 · mid · Sonnet 5.5, medium. Email: no BW2 row; row 3 by analogy | **Code:** every number in the summary is in the report; the summary is at most 400 words | Summary drafted; the email's body slots empty | Safe |
| **8 · Final pass, then send** | Everything above → the report and summary sent to the client; the email sent to the eight interviewees | None: you | **Human:** §5's list, plus: the email's sentences are yours, its subject line one you chose | All yes | **Not re-runnable:** sending is irreversible |

**Three outputs from the run (invented content):**

*Step 2, two rows of `records/quotes.md`:*

| Interview | Quote | Theme |
|---|---|---|
| int-03 | "We find out the truck is late when the shelf is empty." | No advance warning |
| int-06 | "Our drivers call me, not the system." | Informal tracking |

*Step 3, the three outline options, as the stage returned them (headings only):* A · by theme (warning, tracking, cost); B · by the delivery's timeline (order, dispatch, arrival, shelf); C · by who acts (supplier, driver, store). You choose B, because the client's director thinks in that order, and move C's last section into it as the recommendations' frame.

*Step 7, the email skeleton the stage returns:* three subject lines ("Thank you, and what we found", "Your interview on late deliveries: the summary", "Eight conversations about late trucks"), then a body of slots: `[YOURS: thanks, in one sentence]`, `[YOURS: the one finding they will recognise]`, a link line to the summary, `[YOURS: sign-off]`. You write the four sentences.

**Run log, the first three lines (invented):**

| Date | Step · run | Inputs | Model as run | Output | Gate · result |
|---|---|---|---|---|---|
| 3 Mar | 1 Tidy · run 1 | `notes/raw/int-01…08.md` | Haiku 5.5, low | `notes/clean/` | Code: pass, 8 of 8 |
| 3 Mar | 2 Extract · run 1 | `notes/clean/` | Haiku 5.5, high | `quotes-v1.md` | Code: fail, 2 quotes not verbatim |
| 3 Mar | 2 Extract · run 2 | `notes/clean/` | Haiku 5.5, high | `quotes-v2.md` | Code: pass, 41 of 41 |

### Part 3 · Template: your pipeline

Copy into `records/pipeline-[name].md`. Fill every blank; delete what does not apply. Each blank says what goes in it. Write one pipeline per kind of repeated work.

**Pipeline card**

- **What it produces:** [*the finished output, its form and its reader*]
- **Trigger:** [*what starts a run: a backlog row, a date, new raw material arriving*]
- **How often:** [*runs a week or a month*]
- **Raw material:** [*what goes in at the first step, and where it lives*]
- **Boundaries:** [*the points where open flags are decided: at least the end of each run, and every [number] runs; from BW5's BUILD-ORDER.md*]
- **Run log:** [*the file, e.g. records/run-log.md*]

**Step 0 · Before the run**

- [ ] [*every input the first step needs exists, with its version*]
- [ ] [*the briefs for every model step exist, in BW3's form, from template 7*]
- [ ] No open flag touches this run (BW5 §9, step 5).
- [ ] The run log exists.

**Step [n] · [name]** (copy this block once per step)

- **Input:** [*the named files, with versions; never "the latest"; never a chat*]
- **Output:** [*one new file, its path and version, and the form the brief sets for it*]
- **Model:** [*the BW2 row by number and name · tier · model, effort, with the date you read it; or "no BW2 row: row [n] by analogy, because [reason]"; or "none: a script" or "none: you"*]
- **Model's part:** [*from §4's division: drafts structure / cuts your text / gives options; or writes no final words here: marked bridges only / never / points to candidates*]
- **Gate ([*code / model check / human*]):** [*the yes-or-no lines; for code, what the script compares with what; for a model check, the BW6 step it runs; for a human gate, only what no script or source can settle*]
- **Done when:** [*the lines from the brief's DONE WHEN that this step must meet*]
- **Re-run:** [*"safe: reads the same named inputs and writes a new version; every later gate runs again", or "not re-runnable: [why], runs once after the final pass"*]
- **Log:** date · [step] · run n · [inputs and versions] · [model and version as run, effort] · [output file] · [gate result, and back to which step on failure]

**Final step · The final pass, then release** (yours; never handed to a model or an agent)

- [ ] Every marked bridge is rewritten in my words or cut.
- [ ] Every line of humour is one I made.
- [ ] The ending is mine.
- [ ] Every first-person statement is one I would make.
- [ ] Every open item from the model check is closed (BW6, Deliverable Part 1, steps F and G).
- [ ] The output does its job for [*its reader*], read as that reader would.
- [ ] [*a line only you can answer for this kind of output*]
- [ ] The log has a line for every step of this run.
- **Re-run:** [*not re-runnable if release is publishing or sending; where a correction goes: [the page or file where corrections are listed with date and reason]*]

**Checks on the pipeline itself, before the first run**

- [ ] Every step has exactly one output file, and no step edits another's.
- [ ] Every model step names a BW2 row, not only a model name.
- [ ] Every step whose output is first-person prose, humour or an ending gives the model no final words.
- [ ] A human gate sits after the step that fixes the structure, before every irreversible step, and at every boundary.
- [ ] Every step that is not re-runnable comes after the final pass.
- [ ] Re-decide the model rows on BW2 §7's events, and by [*the date six months after you read the vendor pages*].

## Sources

All web sources read 16 November 2026 unless marked. Product facts carried from BW2 are as BW2 read them on 15 November 2026.

- Agarwal, Dhruv, Mor Naaman and Aditya Vashistha. *AI Suggestions Homogenize Writing Toward Western Styles and Diminish Cultural Nuances*. arXiv 2409.11360 v3; the paper's ACM reference line names CHI '25, Yokohama, 2025. https://arxiv.org/html/2409.11360v3
- Anthropic (Erik S. and Barry Zhang, as the page names them). *Building effective agents*. Anthropic Engineering, 19 December 2024 (vendor). https://anthropic.com/engineering/building-effective-agents
- Anthropic. *Prompting best practices*, section "Chain complex prompts". Claude API documentation (vendor). https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/chain-prompts
- Apache Airflow. *Best Practices*. Airflow documentation, version 2.3.3. https://airflow.apache.org/docs/apache-airflow/2.3.3/best-practices.html
- Chakrabarty, Tuhin, Philippe Laban and Chien-Sheng Wu. *Can AI writing be salvaged? Mitigating Idiosyncrasies and Improving Human-AI Alignment in the Writing Process through Edits*. arXiv 2409.14509 v5, 4 March 2025 (preprint). https://arxiv.org/html/2409.14509v5
- Dell'Acqua, Fabrizio, Edward McFowland III, Ethan Mollick and others. *Navigating the Jagged Technological Frontier: Field Experimental Evidence of the Effects of AI on Knowledge Worker Productivity and Quality*. Harvard Business School Working Paper 24-013, 22 September 2023. https://mitsloan.mit.edu/sites/default/files/2023-10/SSRN-id4573321.pdf
- Dolan, Eric W. *AI outshines humans in humor: Study finds ChatGPT is as funny as The Onion*. PsyPost, 4 July 2024 (reporting Gorenz and Schwarz, *How funny is ChatGPT? A comparison of human- and A.I.-produced jokes*, *PLOS ONE*, 2024, not opened). https://www.psypost.org/ai-outshines-humans-in-humor-study-finds-chatgpt-is-as-funny-as-the-onion/
- Doshi, Anil R. and Oliver P. Hauser. *Generative AI enhances individual creativity but reduces the collective diversity of novel content*. *Science Advances* 10, eadn5290, 12 July 2024 (University of Exeter repository copy). https://ore.exeter.ac.uk/rest/bitstreams/199326/retrieve
- Google Cloud. *Break down complex tasks into simpler prompts*. Vertex AI documentation, last updated 12 November 2026 (vendor). https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/break-down-prompts
- Jakesch, Maurice, Advait Bhat, Daniel Buschek, Lior Zalmanson and Mor Naaman. *Co-Writing with Opinionated Language Models Affects Users' Views*. CHI 2023; arXiv 2302.00560. https://arxiv.org/pdf/2302.00560
- Jentzsch, Sophie and Kristian Kersting. *ChatGPT is fun, but it is not funny! Humor is still challenging Large Language Models*. WASSA 2023, pp. 325–340, doi:10.18653/v1/2023.wassa-1.29. https://aclanthology.org/2023.wassa-1.29
- Laban, Hayashi, Zhou and Neville. *LLMs Get Lost In Multi-Turn Conversation*. arXiv 2505.06120 (preprint). https://arxiv.org/pdf/2505.06120
- Noy, Shakked and Whitney Zhang. *Experimental evidence on the productivity effects of generative artificial intelligence*. *Science*, July 2023, doi:10.1126/science.adh2586 (Stanford SCALE abstract page). https://scale.stanford.edu/publications/experimental-evidence-productivity-effects-generative-artificial-intelligence
- Noy, Shakked and Whitney Zhang. *Experimental Evidence on the Productivity Effects of Generative Artificial Intelligence*. MIT working paper, 10 March 2023 (not peer-reviewed). https://economics.mit.edu/sites/default/files/inline-files/Noy_Zhang_1_0.pdf
- OpenAI. *Agent orchestration*. OpenAI Agents SDK documentation (vendor). https://openai.github.io/openai-agents-python/multi_agent/
- Padmakumar, Vishakh and He He. *Does Writing with Language Models Reduce Content Diversity?* ICLR 2024, pp. 642–669. https://proceedings.iclr.cc/paper_files/paper/2024/hash/02dec8877fb7c6aa9a79f81661baca7c-Abstract-Conference.html; arXiv v3: https://arxiv.org/html/2309.05196v3
- Academy case file (`generator/data/building-with-ai/case-academy.md`), §1, §2, §3, §5, §6, §7, §9.
- Units of this course cited by section: BW1 (§1, §3, §5); BW2 (§5, §7, Deliverable Part 1, rows 1 to 5, 9 and 10); BW3 (§3, §5, §6, Deliverable template 7); BW4 (§4, §5, Deliverable Part 3, Deliverable Part 4, step 6); BW5 (§7, §9, §10, Deliverable 1d and 2e); BW6 (§4, §5, §6, §8, Deliverable Part 1, steps B to G).

## Unsure list

1. Gorenz and Schwarz (PLOS ONE, 2024) was read only through Eric W. Dolan's PsyPost report (4 Jul 2024); the paper's PubMed Central copy is reached by a redirect and was not opened. The 73%, 63% and 87% figures and "no significant difference" from The Onion are the report's account.
2. Doshi and Hauser was read through the University of Exeter repository copy; the PubMed Central copy refused the fetch. Volume 10 and article eadn5290 are from that copy; the issue number was not confirmed. The 293 analysed writers (of 500 recruited) and GPT-4 are from the same copy, as the fetch tool reported them.
3. Chakrabarty, Laban and Wu is a preprint (arXiv v5, 4 Mar 2025) with no venue on the copy read; the 28/20/18/17% shares (§5.1), the 65% and 60% preference figures (§6.3) and the §7.4 quotation are as the fetch tool reported them from v5. "18 writers with MFA backgrounds" rests on §4.2 and Table 4 as reported; whether every one of the 18 held an MFA was not confirmed.
4. Noy and Zhang's restructuring finding ("towards idea-generation and editing and away from rough-drafting", the 25/50/25 split, the rough-draft share falling by more than half) is from the MIT working paper of 10 Mar 2023; the Science abstract page read does not carry it, and the published version's text was not opened. The ChatGPT version is not named in the working paper.
5. Dell'Acqua et al. is a working paper; the "marked reduction in the variability of these ideas" quotation is from its §3.1 as the fetch tool reported it.
6. Jentzsch and Kersting describe the model only as OpenAI's ChatGPT, "The GPT3-based model"; the exact version is not given on the page read.
7. No study found measures a model cutting a writer's own text, or measures endings; §4's "cuts" and "endings" claims are this unit's inference from Padmakumar and He, Chakrabarty et al. and Jakesch et al., and are graded as such.
8. Anthropic's Building effective agents names its authors on the page as "Erik S. and Barry Zhang", and notes that much of its tooling landscape "has changed since December 2024"; the chaining pattern was read as still current from Anthropic's Prompting best practices (16 Nov 2026).
9. The Apache Airflow page cited is the documentation for version 2.3.3, an older version; the current version's wording was not checked. Its use for model stages is this unit's adaptation.
10. Google's Gemini API page on prompt design strategies was refused and not checked; the ChatGPT and Gemini consumer products' equivalents of a chained pipeline were not read, so the On other tools table covers developer documentation only.
Object: none

Fresh check 2026-11-16 (Opus 5.5): fix · 2 errors, 7 should-fix, 11 minor; all 20 applied, with 2 companion edits (22 replacements); report `audits/building-with-ai/fresh-check-BW7.md`

Correction 2026-11-16, found by DD-BW1's writer (corrections check `audits/building-with-ai/corrections-2026-11-16-DD-BW1-DD-B3-BW7.md`, Change 6).

*Correction, 17 November 2026: changed by this course's syllabus review (BW-1, row S-BW) after a corrections check by a fresh Opus 5.5 agent (audits/building-with-ai/corrections-2026-11-17-S-BW.md); see the course's changelog for what changed.*

Correction 17 Nov 2026 (CP-4), found by W-SP1, each change checked by a fresh Opus 5.5 agent against case-academy.md

Correction 17 Nov 2026 (CP-5), found by the flag F124 pass and checked by a fresh Opus 5.5 agent against the Academy case file; report audits/building-with-ai/corrections-2026-11-17-CP5-BW5-BW7-BW8-DD-BW2-DD-BW3.md.

Correction 17 Nov 2026 (CP-5, second pass), found by the flag F124 pass and checked by a fresh Opus 5.5 agent against the Academy case file; report audits/building-with-ai/corrections-2026-11-17-CP5b-BW5-BW7.md.
