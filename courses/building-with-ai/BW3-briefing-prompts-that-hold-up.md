---
code: BW3
title: "Briefing: prompts that hold up"
course: building-with-ai
model: Opus 5.5
written: 2026-11-15
search: off
---

# BW3 · Briefing: prompts that hold up

This unit was written with search off. Searches were used only to re-verify each source it cites, on 15 November 2026, and every product fact (a model name, a default, a feature) carries that reading date. Most vendor documentation pages show no date of their own, so the reading date is the only one they can be given. Each practice carries an evidence grade, as in BW1 and BW2: **measured** (a study or test with numbers), **documented practice** (a vendor or a named practitioner says to do it; nobody measured it here) or **stated opinion**. Every study names the models it tested; carrying its finding to a current model is this unit's inference, and is said to be. What a context window is, why the whole conversation is re-sent on every turn and why every instruction raises a probability without guaranteeing anything are in BW1 (§1, §2, §6); which model and effort a task gets is BW2's routing table. This unit assumes both and uses them by section number.

## 1 · The four parts of a brief that survives

A brief survives when a reader with no context can act on it without coming back with a question. Anthropic's general prompting guide states the test in those terms: think of Claude as "a brilliant but new employee who lacks context on your norms and workflows", and before sending, show the prompt to a colleague who knows little about the task; "If they'd be confused, Claude will be too." ([Anthropic, *Prompting best practices*](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices), read 15 Nov 2026; documented practice, vendor). A model given a gap in a brief usually fills it with the most probable reading of the window (BW1 §7). A brief is the text that removes the gaps that matter.

Four parts do most of that work. The vendors' guides read for this unit cover all four, each in its own words; none of them presents them as a set, so the grouping is this unit's.

### Who the reader is

Two different things travel under the word "role". One is a persona for the model ("You are an expert editor"). Anthropic says a role set in the system prompt focuses Claude's behaviour and tone, and that "Even a single sentence makes a difference" ([*Prompting best practices*](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices), read 15 Nov 2026). Measured on factual accuracy, personas did not help. Mingqian Zheng and colleagues compiled 162 roles, tested four families of models on 2,410 factual questions, and found that "adding personas in system prompts does not improve model performance"; picking the best persona for each question helped, but choosing it automatically did about as well as choosing at random ([Zheng, Pei, Logeswaran, Lee and Jurgens, *Findings of EMNLP 2024*](https://aclanthology.org/2024.findings-emnlp.888/); measured). The two sources measure different things, tone and correctness, so they do not contradict each other. Together they place a persona's documented effect in register.

The other meaning is the reader of the output: who will read it, what they already know, and what they will do with it. Anthropic's article on prompting lists "Explaining the purpose or audience for the output" among the cases where context improves results ([Claude, *Best practices for prompt engineering for 2026*, 10 Nov 2025](https://claude.com/resources/articles/best-practices-for-prompt-engineering), read 15 Nov 2026; vendor). OpenAI's help centre asks for prompts that are specific about "the desired context, outcome, length, format, style" ([OpenAI Help Center, *Best practices for prompt engineering with the OpenAI API*](https://help.openai.com/en/articles/6654000), read 15 Nov 2026; vendor). Anthropic gives the mechanism: an instruction that carries its reason lets the model apply the reason to cases the instruction did not name. Its example replaces "NEVER use ellipses" with the reason (the response will be read aloud by a text-to-speech engine that cannot pronounce them) and adds that "Claude can generalize from the explanation" ([*Prompting best practices*](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)). A reader line is that kind of reason, given once for the whole output: "a lawyer who will read this on a phone between meetings" settles length, register and layout for every sentence without a rule for each.

**The case.** Academy (Academy case), a library of self-study courses built by one person with Claude in October and November 2026, is this course's running example; it is one project, an anecdote, never evidence about AI tools in general. Its method joins a shared preamble (the reader, the goal, the sourcing standard, the tone) to each unit's own brief, so every context is self-contained (Academy case file §2). The reader travels with every brief because no writer sees any other.

### What the output is

The second part names the artefact, its form and where it will live. Anthropic: "Be specific about the output format and constraints you want." ([*Prompting best practices*](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)). OpenAI: "Articulate the desired output format through examples" ([OpenAI Help Center](https://help.openai.com/en/articles/6654000)). §3 turns this part into a contract.

### Constraints

Constraints are the rules the output must satisfy: what it must contain, what it must leave out, its tone and its limits. Three pieces of guidance shape how they are written.

**State the positive.** Anthropic: "Tell Claude what to do instead of what not to do", replacing "Do not use markdown in your response" with "Your response should be composed of smoothly flowing prose paragraphs." ([*Prompting best practices*](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)). OpenAI's help centre gives the same rule: "Instead of just saying what not to do, say what to do instead" ([OpenAI Help Center](https://help.openai.com/en/articles/6654000)). Both vendor guidance.

**When a prohibition is needed, name the pattern.** Anthropic's guide to Opus 5.5 says a general instruction such as "avoid a generic AI look" "mostly swaps one default for another", and that the model "responds well to instructions that name specific patterns to avoid" ([Anthropic, *Prompting Claude Opus 5.5*](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5-5), read 15 Nov 2026; vendor, written about frontend design). Carrying it to prose ("no opening sentence that restates the question" in place of "avoid filler") is this unit's extension.

**Give an absolute its scope.** Anthropic's guide to Fable 5.2 says the model treats an instruction that contains "never" as absolute, and advises writing "ask for approval before deleting files" in place of "never delete files" where an exception is meant; it also says Fable 5.2 follows style rules closely, so a hard limit on sentence length can make its prose choppy ([Anthropic, *Prompting Claude Fable 5.2*](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-2), read 15 Nov 2026; vendor). A constraint is followed as written; write it as you mean it.

Older research gives a reason to be wary of bare negatives. Joel Jang, Seonghyeon Ye and Minjoon Seo tested nine tasks phrased with negation and found that, across pretrained, instruction-tuned, few-shot and negation-fine-tuned setups, "all LM types perform worse on negated prompts as they scale" ([Jang, Ye and Seo, *Proceedings of the 1st Transfer Learning for NLP Workshop*, PMLR 203, 2023, 52–62](https://proceedings.mlr.press/v203/jang23a.html); measured). The models were OPT and GPT-3 from 125M to 175B parameters, and InstructGPT. None is current, and the finding says nothing measured about today's models. It supports one habit only: pair each "do not" with the "do" that replaces it.

### Examples, including negative ones

The fourth part shows the output instead of describing it. What the evidence and the vendors say about examples, and how far they disagree, is §4. The short version: an example teaches its shape (length, structure, register) more than its content, and a bad example belongs in a brief only beside a good one, labelled as wrong, with the reason it fails.

## 2 · Specificity against length

Length is a cost, and specificity is what the cost buys. Anthropic's prompting article lists among common mistakes that "Longer, more complex prompts are NOT always better." ([*Best practices for prompt engineering for 2026*](https://claude.com/resources/articles/best-practices-for-prompt-engineering)). Anthropic's Applied AI team frames the goal as the "smallest possible set of high-signal tokens" that makes the outcome you want likely, adds that "minimal does not necessarily mean short", and describes two ways to miss: "hardcoding complex, brittle logic" at one end and "vague, high-level guidance" at the other ([Rajasekaran, Dixon, Ryan and Hadfield, *Effective context engineering for AI agents*, Anthropic, 29 Sep 2025](https://anthropic.com/engineering/effective-context-engineering-for-ai-agents); vendor). All documented practice.

**Why extra text costs.** BW1 §2 sets out the attention budget and the evidence that a model uses any one piece of a long window less reliably. Three studies bear on prompts in particular; §7 gives their models and dates.

- Mosh Levy, Alon Jacoby and Yoav Goldberg padded the same reasoning questions with extra text of different lengths, types and positions, and found "a notable degradation" in reasoning "at much shorter input lengths than their technical maximum", in every version of their dataset ([Levy, Jacoby and Goldberg, ACL 2024](https://aclanthology.org/2024.acl-long.818); measured).
- Shi and colleagues added irrelevant sentences to school arithmetic problems (GSM-IC) and found performance "dramatically decreased when irrelevant information is included"; one mitigation that helped was an instruction telling the model it could ignore irrelevant information ([Shi et al., ICML 2023](https://arxiv.org/pdf/2302.00093); measured).
- Daniel Jaroslawicz and colleagues gave 20 models from seven providers up to 500 keyword-inclusion instructions in one report-writing task; the best frontier models reached 68% accuracy at 500, and models showed a bias towards earlier instructions ([Jaroslawicz, Whiting, Shah and Maamari, arXiv 2507.11538, 2025](https://arxiv.org/abs/2507.11538); preprint, presented as a [NeurIPS 2025 workshop poster](https://neurips.cc/virtual/2025/122417); measured).

The direction is the same in all three: material that does not serve the task competes with material that does.

**What specificity means.** Claude Code's documentation gives a working definition: write instructions "concrete enough to verify", such as "Use 2-space indentation" in place of "Format code properly", and it states that "The more specific and concise your instructions, the more consistently Claude follows them" ([Anthropic, *How Claude remembers your project*](https://code.claude.com/docs/en/memory), read 15 Nov 2026; vendor, written for instruction files). OpenAI's help centre gives the same rule from the other side: "Reduce “fluffy” and imprecise descriptions" ([OpenAI Help Center](https://help.openai.com/en/articles/6654000)). A specific instruction is one the output can be checked against, and it can be short. "Keep it concise" cannot be checked; "at most three reasons, twelve words each" can.

**Where sources disagree.** OpenAI's API guide says "reasoning models will provide better results on tasks with only high-level guidance", and adds that this differs from its GPT models, "which benefit from precise instructions" ([OpenAI, *Prompt engineering*](https://developers.openai.com/api/docs/guides/prompt-engineering), read 15 Nov 2026). Anthropic's general guide points the other way: "The more precisely you explain what you want, the better the result." ([*Prompting best practices*](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)). On one point Anthropic's Opus 5.5 guide agrees with OpenAI: in chat applications, instructions telling the model to think carefully before answering can be removed, because the model decides how much to think and "the effort level is the main control" ([*Prompting Claude Opus 5.5*](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5-5)). The reconciliation this unit uses (stated opinion): be exact about the output (what it is, who reads it, when it is done), which every source supports, and leave the route to the model, which is where the reasoning-model guidance points. The templates at the end follow that split: they specify artefacts and checks, and none of them scripts the model's reasoning.

## 3 · Output contracts

An output contract is the part of a brief that says what will be handed back. It has three clauses.

**Format.** Anthropic's guide gives three levers: say what to do; use XML tags to mark the parts; and match the prompt's own style to the output wanted, since "removing markdown from your prompt can reduce the volume of markdown in the output" ([*Prompting best practices*](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices); vendor). A format clause names the container as well as the layout: a Markdown file, a table in the chat, an email ready to paste, a file at a given path. A chat assistant that can make documents will choose a container if you do not, and the one it chooses may not be the one your next step can read.

**Length rule.** Length targets hold for short outputs and fail for long ones. Wei Zhang and colleagues built LIFEBench, 10,800 instances in English and Chinese with length targets from 16 to 8,192 words, tested 26 models, and found that most follow short-length instructions reasonably but "deteriorate sharply beyond a certain threshold"; almost all fell short of the maximum output lengths their vendors claim ([Zhang et al., *LIFEBench*, NeurIPS 2025 Datasets and Benchmarks Track](https://proceedings.nips.cc/paper_files/paper/2025/hash/c84f00ccee3d35cee1901acb0e258dc7-Abstract-Datasets_and_Benchmarks_Track.html); measured). Anthropic's guidance adds two product facts (read 15 Nov 2026): its latest models are less verbose and "Might skip detailed summaries for efficiency unless prompted otherwise" ([*Prompting best practices*](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)), and on Fable 5.2 "Effort has little effect on the length of assistant turn responses"; length is set by prompting ([*Prompting Claude Fable 5.2*](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-2)). So a word limit is a usable contract for a caption, a message or an abstract. For a long piece the contract that holds is structural: one section per item of the brief, each answered, none padded, and a range stated as a guide. That form is this unit's synthesis of the LIFEBench result and the vendor notes (stated opinion).

**The case.** Academy sets a unit's length at 2,000 to 6,000 words "by guide"; its longest UX unit is about 16,900 words (Academy case file §1). The case file does not say whether that length was wanted. It shows one unit that ran past a stated range. That is an anecdote, not a test of the evidence above, and not the failure LIFEBench measured, where long outputs often came out far too short.

**What done looks like.** Anthropic's prompt-engineering overview assumes three things before any prompting starts: "A clear definition of the success criteria for your use case", "Some ways to empirically test against those criteria", and "A first draft prompt you want to improve" ([Anthropic, *Prompt engineering overview*](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview), read 15 Nov 2026; vendor). Claude Code's guide puts the reason plainly: Claude stops when the work looks done, and without a check it can run, "looks done" is the only signal available; give it something that produces a pass or fail ([Anthropic, *Best practices for Claude Code*](https://code.claude.com/docs/en/best-practices.md), read 15 Nov 2026; vendor; documented practice). The same guide asks for evidence in place of an assertion of success (the test output, the command that was run), and warns that a reviewer prompted to find gaps "will usually report some, even when the work is sound", so a review brief should say to flag only gaps that affect correctness or the stated requirements (same page). In a chat, the check is a list you can run on the output line by line: every item of the brief has its section; every figure names its source; the table has these columns. The templates end with that list, under **DONE WHEN**.

One more clause belongs in any contract that touches facts: a sanctioned place for what the model could not verify. Anthropic's hallucination guide recommends giving explicit permission to admit uncertainty, which it says "can drastically reduce false information" (no figure given), asking for quotes or sources for each claim, and having the model retract any claim it cannot support with a quote ([Anthropic, *Reduce hallucinations*](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations), read 15 Nov 2026; documented practice, vendor). Academy's method builds this in: before handing in, the writer runs the sourcing checklist and lists up to ten claims it could not verify (Academy case file §2). When Academy's first audit sent three units back for rewriting, one of its two reasons was that the three deliverables did not exist (Academy case file §3). A contract that names the deliverable and says it is built in full gives a check something to find missing.

## 4 · Examples and the position of the question: what the evidence says, and what the vendors say

Both topics are full of confident advice. This section keeps the two kinds of support apart: vendor guidance (a model maker's documentation, which says what it recommends and rarely shows the measurement behind it) and research (peer-reviewed work, or a preprint labelled as one).

### Examples

**Vendor guidance** (all read 15 Nov 2026):

- Anthropic's documentation: "Include 3–5 examples for best results", each wrapped in `<example>` tags so the model can tell them from instructions ([*Prompting best practices*](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)).
- Anthropic's prompting article: "Start with one example (one-shot)", and add more only if the output still does not match ([*Best practices for prompt engineering for 2026*](https://claude.com/resources/articles/best-practices-for-prompt-engineering)).
- Anthropic's Applied AI team warns against stuffing "a laundry list of edge cases" into a prompt and recommends teams "curate a set of diverse, canonical examples" ([*Effective context engineering for AI agents*](https://anthropic.com/engineering/effective-context-engineering-for-ai-agents)).
- OpenAI's help centre: start with zero-shot, then few-shot ([OpenAI Help Center](https://help.openai.com/en/articles/6654000)); its API guide asks for examples that show "a diverse range of possible inputs with the desired outputs" ([*Prompt engineering*](https://developers.openai.com/api/docs/guides/prompt-engineering)).

The range runs from none to five, and in every source the deciding variable is whether the output matches. Google's prompt-design page for Gemini was not checked: the fetch was refused, so its advice on examples is left out of this unit.

**Research.** Sewon Min and colleagues found that randomly replacing the labels in demonstrations "barely hurts performance" on classification and multiple-choice tasks, across 12 models including GPT-3; what drove the effect was the label space, the distribution of the input text and the format of the sequence ([Min et al., EMNLP 2022, 11048–11064](https://aclanthology.org/2022.emnlp-main.759); measured). On those tasks a demonstration worked mainly by showing the shape of an answer. The reading for a brief (this unit's inference): choose an example for its shape, and expect the shape to be copied. If the example is 200 words, expect 200 words; if it opens with a definition, expect a definition.

**Negative examples.** None of the vendor pages read for this unit advises putting a labelled bad example into a prompt, and none forbids it. One preprint tested the form directly. Yew Ken Chia and colleagues gave GPT-3.5-Turbo (the 0301 version) a valid and an invalid reasoning demonstration side by side, the invalid one made by shuffling the numbers and names of the valid one, and reported higher accuracy than standard chain-of-thought on every benchmark they ran: GSM8K 69.2 to 79.0, SVAMP 67.2 to 81.6, Bamboogle 40.8 to 56.8 among them ([Chia, Chen, Tuan, Poria and Bing, *Contrastive Chain-of-Thought Prompting*, arXiv 2311.09277, 2023](https://arxiv.org/pdf/2311.09277); preprint; measured, on one 2023 model, on reasoning tasks). That is thin support for a general rule, and it is the only measurement found. The rule the templates follow is this unit's synthesis (stated opinion): a bad example appears only beside a good one, labelled as wrong, with the pattern named and the reason it fails, so the model sees the contrast and is never shown a bad shape alone to copy.

### Where the question sits in a long prompt

The ask is buried when it sits in the middle of a message, after background and before pasted material. The sources disagree on where it belongs, and they are written for different situations.

**Vendor guidance** (all read 15 Nov 2026):

- OpenAI's help centre: "Put instructions at the beginning of the prompt", and mark them off from the context with ### or triple quotes ([OpenAI Help Center](https://help.openai.com/en/articles/6654000)).
- OpenAI's API guide: context is "usually best positioned near the end of your prompt", with stable content such as instructions and examples at the start, which also helps prompt caching ([*Prompt engineering*](https://developers.openai.com/api/docs/guides/prompt-engineering)).
- Anthropic, for inputs of 20k tokens or more: put long documents near the top, above the query, instructions and examples; queries at the end can improve response quality by "up to 30 percent in tests", especially with complex, multi-document inputs ([*Prompting best practices*](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)). That figure is vendor data: the page gives no method, task set or model list behind it.
- Google's long-context page: performance "will be better if you put your query / question at the end of the prompt" ([Google, *Long context*, Gemini API docs, last updated 15 Oct 2026](https://ai.google.dev/gemini-api/docs/long-context)). A Google Cloud page on prompting Gemini 3 says to place specific instructions or questions at the end, after the data, and that "negative constraints should be placed at the end of the instruction" ([Google Cloud, Vertex AI documentation page on prompting Gemini 3](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/start/gemini-3-prompting-guide), read 15 Nov 2026; its headline was not shown in the copy read).

**Research.** Nelson Liu and colleagues found performance often highest when the relevant information sat at the beginning or end of a long input, and significantly worse when it sat in the middle, even for models built for long contexts ([Liu et al., *TACL* 12, 2024, 157–173](https://aclanthology.org/2024.tacl-1.9/); measured; BW1 §2 gives its models). IFScale found a bias towards earlier instructions (§2). The research agrees on one point only: the middle is the weak position.

The layout the templates use is this unit's synthesis (stated opinion): a one-line TASK first, so the ask is never buried; the long material in tags after the brief; and, when the material is long, the TASK repeated as the last line. That puts the ask where OpenAI's help centre puts instructions and, again, where Anthropic and Google put the question; it departs from Anthropic's advice to place long documents above the instructions as well, which is a trade-off this unit makes so the brief is read before the material.

```viz
{
  "kind": "matrix",
  "caption": "Where each source places the parts of a long prompt, as §4 of this unit reports it: OpenAI Help Center, Best practices for prompt engineering with the OpenAI API; OpenAI, Prompt engineering (API docs); Anthropic, Prompting best practices (inputs of 20k tokens or more); Google, Long context (Gemini API docs); Liu et al., TACL 2024. All vendor pages read 15 Nov 2026. The last row is this unit's own synthesis (§4); the closing TASK is added only when the material is long.",
  "cols": ["Beginning", "Middle", "End"],
  "rows": [
    {"label": "OpenAI Help Center", "tone": 3, "cells": ["instructions", null, null]},
    {"label": "OpenAI API guide", "tone": 3, "cells": ["instructions, examples", null, "context"]},
    {"label": "Anthropic, 20k+ tokens", "tone": 3, "cells": ["long documents", null, "query"]},
    {"label": "Google, long context", "tone": 3, "cells": [null, null, "question"]},
    {"label": "Liu et al. (measured)", "tone": 5, "cells": [null, {"mark": "significantly worse", "tone": 1}, null]},
    {"label": "The templates", "tone": 2, "cells": ["TASK", "material in tags", "TASK again"]}
  ]
}
```

## 5 · How a long conversation drifts, and when to restart

A chat that starts well can end badly with no single bad message in it. Four mechanisms are documented, and they compound.

1. **The window fills.** Every turn re-sends the whole history (BW1 §2), so a rule stated at turn 3 competes at turn 30 with everything said since. Claude Code's guide states the constraint most of its advice rests on: the context window "fills up fast, and performance degrades as it fills"; when it is getting full, Claude "may start 'forgetting' earlier instructions or making more mistakes" ([*Best practices for Claude Code*](https://code.claude.com/docs/en/best-practices.md), read 15 Nov 2026; vendor).
2. **Early instructions are summarised away.** When a chat grows long, Claude Code, and claude.ai for users with code execution enabled, summarise earlier turns so the conversation can continue, and Claude Code's documentation warns that detailed instructions from early in the conversation may be lost (BW1 §3, with its sources, read 15 Nov 2026).
3. **Failed attempts stay in the window.** Each wrong answer and each correction is part of the input from then on (BW1 §4). Claude Code's guide: if you have corrected Claude more than twice on the same issue in one session, "the context is cluttered with failed approaches"; clear it and start again with a more specific prompt that includes what you learned, since a clean session with a better prompt "almost always outperforms a long session with accumulated corrections" (same page; documented practice).
4. **A brief given in pieces does worse than the same brief given whole.** Philippe Laban and colleagues took tasks that models do well when fully specified in one turn and gave the same instruction in pieces, at most one per turn, through a simulated user. Across more than 200,000 simulated conversations, all the top open- and closed-weight models they tested did significantly worse in the multi-turn setting, "an average drop of 39% across six generation tasks". The models "make assumptions in early turns and prematurely attempt to generate final solutions", rely on those attempts, and once they take a wrong turn "they get lost and do not recover" ([Laban, Hayashi, Zhou and Neville, *LLMs Get Lost In Multi-Turn Conversation*, arXiv 2505.06120](https://arxiv.org/pdf/2505.06120); [ICLR 2026](https://iclr.cc/virtual/2026/oral/10009147); measured). The paper splits the drop in two: aptitude, the best a model does, fell by 15 to 16% on average (the paper's figure and text differ by a point), while unreliability, the spread between its good and bad runs, rose by 112% (§6.2 of the paper). The 15 models tested include Claude 3.7 Sonnet, GPT-4.1, o3 and Gemini 2.5 Pro; none is current.

The third and fourth points describe the same shape from two sides: an early guess, built on and never retracted. The paper's own advice to users is the practical rule (§7.4): consolidating the requirements into a single instruction is "an effective strategy", and starting a new conversation that repeats the same information "might yield significantly better outcomes". It also found that setting temperature to 0 left an unreliability of around 30% (§7.2). That result was measured on GPT-4o and GPT-4o-mini through their APIs in 2025 (Table 3 of the paper). On current Claude models you cannot set temperature at all: Anthropic's API rejects it on Claude 4.7 and later (BW1 §5, read 15 Nov 2026 there), so for those models the question is closed and only the brief remains as a lever.

**The case.** Academy writes each unit in a new chat or a fresh agent context that sees only its brief and the units already filed, and gives as its reason that leaked context is how a course starts repeating itself (Academy case file §2). When writer agents were lost to container restarts, the third writer of one deep dive resumed from the second's working files (Academy case file §7): the restart worked because the brief and the work were in files, outside the chat. One project; it shows the practice run, and nothing about whether it beats the alternative (Academy case file §9).

**When to restart** (stated opinion, assembled from the documented practice and the measurement above). Start a new chat, with a brief that consolidates what the old one learned, when any of these holds:

- the next request is a different task (Claude Code's "kitchen sink session": one task, then something unrelated, then back; [*Best practices for Claude Code*](https://code.claude.com/docs/en/best-practices.md));
- you have corrected the same issue twice and it is still wrong (same page);
- the requirements changed partway through, so the chat holds an old version of the brief beside the new one (Laban et al. §7.4);
- the chat has been summarised, or is long enough that it may be (BW1 §3).

Restarting has a cost: you rewrite the brief. Laban's suggested sentence for the old chat, "Please consolidate everything I've told you so far", gives you a draft of it, which you then check against what you meant before pasting it into the new chat. Claude Code's guide gives the counter-case too: sometimes the history is the valuable part, because you are deep in one complex problem ([*Best practices for Claude Code*](https://code.claude.com/docs/en/best-practices.md)). The rule is for when the history has stopped helping.

The decision below draws the rule in the order it is cheapest to check.

```viz
{
  "kind": "decision",
  "root": {
    "q": "Is the next request a different task?",
    "tone": 4,
    "branches": [
      {"label": "yes", "to": {"outcome": "New chat, with its own brief", "tone": 1}},
      {"label": "no", "to": {
        "q": "Corrected the same issue twice, still wrong?",
        "tone": 4,
        "branches": [
          {"label": "yes", "to": {"outcome": "Rewrite the brief with what you learned; new chat", "tone": 1}},
          {"label": "no", "to": {
            "q": "Did the requirements change, or has the chat been summarised, or is it long enough that it may be?",
            "tone": 4,
            "branches": [
              {"label": "yes", "to": {"outcome": "Consolidate the brief; new chat", "tone": 1}},
              {"label": "no", "to": {"outcome": "Continue in this chat", "tone": 3}}
            ]
          }}
        ]
      }}
    ]
  },
  "caption": "When to restart a conversation, the rule in §5 of this unit (stated opinion), built on Anthropic, Best practices for Claude Code (read 15 Nov 2026; the kitchen-sink session and the two-corrections rule), Laban et al., LLMs Get Lost In Multi-Turn Conversation, §7.4 (consolidate and restart), and BW1 §3 (summarised chats)."
}
```

## 6 · The common failures

Three failures recur in the vendor guidance and the studies below; no source read for this unit counts how often each causes a miss. Each has a fix that the templates build in.

### Asking for a plan when you want the thing

The verb of the request sets the artefact. Anthropic's guide: if you ask whether Claude can suggest some changes, it "will sometimes provide suggestions rather than implementing them", even when changes were what you wanted; and if you want more than the task strictly requires, "explicitly request it rather than relying on the model to infer" it ([*Prompting best practices*](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices), read 15 Nov 2026). The failure runs both ways. Anthropic's Sonnet 5.5 guide says an open-ended request "can start building a presentation, report, or video when you only wanted ideas", and that if you want ideas or a plan first you should say so ([Anthropic, *Prompting Claude Sonnet 5.5*](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-sonnet-5-5), read 15 Nov 2026). OpenAI's guide to its GPT-6 models suggests prompting the model not to stop at proposing a plan or offering to continue, so that you approve "a concrete, reviewable result" ([OpenAI, *Using GPT-6*](https://developers.openai.com/api/docs/guides/prompt-guidance), read 15 Nov 2026). All vendor guidance. Scope can also overrun on its own: the Sonnet 5.5 guide says that, when coding, the model tends to add tests, documentation and small supporting files nobody asked for, and suggests a system-prompt paragraph that limits changes to what was requested and has the model mention any extra it thinks would help at the end (same Sonnet 5.5 page).

Fix: the first line of every brief is a TASK line that opens with the verb of the artefact and names it ("Write the memo", "Extract a table", "Change the script and add its test"). When you do want a plan first, say so and make it a separate stage: Claude Code's guide separates exploring and planning from implementing, so as not to solve the wrong problem, and skips the plan when you could describe the change in one sentence ([*Best practices for Claude Code*](https://code.claude.com/docs/en/best-practices.md); documented practice). Template 7 is that two-stage brief.

### Burying the ask

The ask sits in the middle: a paragraph of background, the request, then pasted material. §4 gives the evidence that the middle is the weak position and the vendor guidance on where the ask belongs. Fix: TASK first, material in tags, TASK again at the end when the material is long.

### Stacking unrelated tasks

"Summarise these notes, fix the spreadsheet formula and draft the client email" is three tasks in one window. Each task's material is irrelevant context for the other two, which is the condition Shi and colleagues and Levy and colleagues measured (§2); every added instruction competes for adherence (IFScale, §2); and the three tasks may want different models and efforts (BW2's routing table), while one chat runs them all on one. Claude Code's guide names the pattern as a failure and gives the fix, clearing the context between unrelated tasks ([*Best practices for Claude Code*](https://code.claude.com/docs/en/best-practices.md)). Anthropic's general guide says explicit chaining stays useful "when you need to inspect intermediate outputs or enforce a specific pipeline structure" ([*Prompting best practices*](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)). Fix (documented practice): one artefact per brief. Where tasks form a pipeline, each stage is its own brief and its output is read before it feeds the next; BW7 builds that chain.

**The case.** Every Academy chat works one row of its backlog, and each chat ends by writing the prompt for the next (Academy case file §2): one task per context, with the hand-off written down. One project; it shows the discipline is workable for one person, and nothing about its effect.

## 7 · What the prompting literature measured, and on which models

Every study cited in this unit, with what it tested. None tested a model current on 15 November 2026; where a page did not name the models, the table says so.

| Study | Status | Task | Models tested | Finding used here |
|---|---|---|---|---|
| [Min et al., 2022](https://aclanthology.org/2022.emnlp-main.759) | Peer-reviewed (EMNLP) | Classification, multiple choice | 12 models, GPT-3 among them | Demonstrations teach label space, input distribution and format; correct labels matter little (§4) |
| [Jang, Ye and Seo, 2023](https://proceedings.mlr.press/v203/jang23a.html) | Peer-reviewed (workshop, PMLR) | Nine tasks with negated prompts | OPT and GPT-3, 125M to 175B; InstructGPT | Worse on negated prompts as models scale (§1) |
| [Shi et al., 2023](https://arxiv.org/pdf/2302.00093) | Peer-reviewed (ICML) | School arithmetic with irrelevant sentences | code-davinci-002, text-davinci-003 | Irrelevant information sharply lowers accuracy; an ignore instruction helps (§2) |
| [Chia et al., 2023](https://arxiv.org/pdf/2311.09277) | Preprint | Arithmetic and factual reasoning | GPT-3.5-Turbo (0301) | Valid beside invalid demonstrations beat valid alone (§4) |
| [Zheng et al., 2024](https://aclanthology.org/2024.findings-emnlp.888/) | Peer-reviewed (Findings of EMNLP) | 2,410 factual questions, 162 personas | Four model families | Personas in the system prompt do not improve accuracy (§1) |
| [Levy, Jacoby and Goldberg, 2024](https://aclanthology.org/2024.acl-long.818) | Peer-reviewed (ACL) | Reasoning questions with padding | Not named in the abstract read | Reasoning degrades far below the maximum input length (§2) |
| [Liu et al., 2024](https://aclanthology.org/2024.tacl-1.9/) | Peer-reviewed (TACL) | Multi-document QA, key-value retrieval | Listed in BW1 §2 | Middle of a long input recalled worst (§4) |
| [Jaroslawicz et al., 2025](https://arxiv.org/abs/2507.11538) | Preprint; workshop poster | 500 keyword instructions in one report | 20 models, seven providers (not named in the abstract read) | 68% at best at 500; earlier instructions favoured (§2) |
| [Zhang et al., 2025](https://proceedings.nips.cc/paper_files/paper/2025/hash/c84f00ccee3d35cee1901acb0e258dc7-Abstract-Datasets_and_Benchmarks_Track.html) | Peer-reviewed (NeurIPS Datasets and Benchmarks) | Length targets, 16 to 8,192 words | 26 models (not named in the abstract read) | Short targets followed; long ones fail sharply (§3) |
| [Laban et al., 2025](https://arxiv.org/pdf/2505.06120) | Peer-reviewed (ICLR 2026) | Six generation tasks, instruction in pieces | 15 models, Claude 3.7 Sonnet, GPT-4.1, o3 and Gemini 2.5 Pro among them | 39% average drop when the brief arrives in pieces (§5) |

What transfers, and what does not (this unit's inference):

- **Direction transfers better than size.** Where several studies on different models point the same way (extra material hurts; the middle is weak; long length targets fail; pieces do worse than a whole), the direction is a reasonable working assumption for a current model. The sizes (39%, 68%, the Chia gains) belong to the models and tasks measured, and none should be quoted as a property of the model you use.
- **Vendor figures are not measurements you can inspect.** Anthropic's "up to 30 percent" (§4) has no published method. It is a vendor statement, graded as such.
- **Several findings rest on settings you no longer control.** Studies of 2022 and 2023 ran models with sampling settings their authors chose. On current Claude models temperature cannot be set (BW1 §5), so a technique that depended on a setting does not carry over as stated.
- **The research tested short, checkable tasks.** Arithmetic, classification, keyword inclusion, retrieval. Most project work (a report, a memo, a critique) has no answer key, which is why the templates below put the check in the brief instead of trusting a technique.

## 8 · On other tools

The principles in §1 to §7 (a brief with four parts, specificity that can be checked, an output contract with a done list, examples chosen for their shape, the ask out of the middle, a new chat when the old one has drifted, one task per brief) are stated for any current assistant. The detail is Claude's. Below, each Claude-specific claim with the equivalent where the other vendor's own documentation was found, all read 15 Nov 2026. Google's main prompt-design page for the Gemini API refused the fetch and was not checked; Google rows rest on its long-context page and on a Google Cloud page on Gemini 3.

| Claim in this unit | Claude | ChatGPT / OpenAI | Gemini / Google |
|---|---|---|---|
| Give the reader and purpose of the output (§1) | [*Prompting best practices*](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices); [*Best practices for prompt engineering for 2026*](https://claude.com/resources/articles/best-practices-for-prompt-engineering) | Be specific about context, outcome, length, format, style: [Help Center](https://help.openai.com/en/articles/6654000) | Not checked: the prompt-design page refused the fetch |
| Say what to do, not only what not to do (§1) | [*Prompting best practices*](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices) | Same rule: [Help Center](https://help.openai.com/en/articles/6654000) | On using provided information: "Rather than a large blanket negative constraint, tell the model explicitly" to use it; negative constraints go at the end of the instruction: [Google Cloud page on Gemini 3](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/start/gemini-3-prompting-guide) |
| Name the patterns to avoid (§1) | [*Prompting Claude Opus 5.5*](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5-5) | The GPT-6 guide's suggested prompt bans named words and phrases: [*Using GPT-6*](https://developers.openai.com/api/docs/guides/prompt-guidance) | No equivalent found in the pages read |
| Instructions concrete enough to verify (§2) | [*How Claude remembers your project*](https://code.claude.com/docs/en/memory) | Reduce imprecise descriptions: [Help Center](https://help.openai.com/en/articles/6654000) | No equivalent found in the pages read |
| High-level guidance for reasoning models; effort, not prompts, sets thinking (§2) | [*Prompting Claude Opus 5.5*](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5-5) | Reasoning models better with high-level guidance: [*Prompt engineering*](https://developers.openai.com/api/docs/guides/prompt-engineering) | Not checked for this unit (BW2 §3 covers Gemini's thinking levels) |
| Length is set by prompting; long targets unreliable (§3) | [*Prompting Claude Fable 5.2*](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-2) | No equivalent found in the pages read | Gemini 3 is less verbose by default: [Google Cloud page on Gemini 3](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/start/gemini-3-prompting-guide) |
| State what done looks like; give a check (§3) | [*Prompt engineering overview*](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview); [*Best practices for Claude Code*](https://code.claude.com/docs/en/best-practices.md) | Approve a concrete, reviewable result: [*Using GPT-6*](https://developers.openai.com/api/docs/guides/prompt-guidance) | No equivalent found in the pages read |
| How many examples (§4) | 3–5, or start with one: [*Prompting best practices*](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices); [*Best practices for prompt engineering for 2026*](https://claude.com/resources/articles/best-practices-for-prompt-engineering) | Zero-shot, then few-shot: [Help Center](https://help.openai.com/en/articles/6654000); diverse inputs: [*Prompt engineering*](https://developers.openai.com/api/docs/guides/prompt-engineering) | Not checked: the prompt-design page refused the fetch |
| Where the question goes in a long prompt (§4) | Query after long documents, 20k+ tokens: [*Prompting best practices*](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices) | Instructions first: [Help Center](https://help.openai.com/en/articles/6654000); context near the end: [*Prompt engineering*](https://developers.openai.com/api/docs/guides/prompt-engineering) | Question at the end: [*Long context*](https://ai.google.dev/gemini-api/docs/long-context); [Google Cloud page on Gemini 3](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/start/gemini-3-prompting-guide) |
| Restart after repeated corrections; one task per session (§5, §6) | [*Best practices for Claude Code*](https://code.claude.com/docs/en/best-practices.md) | No equivalent found in the pages read | No equivalent found in the pages read |
| Ask for the artefact, or say you want a plan (§6) | [*Prompting best practices*](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices); [*Prompting Claude Sonnet 5.5*](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-sonnet-5-5) | Do not stop at proposing a plan: [*Using GPT-6*](https://developers.openai.com/api/docs/guides/prompt-guidance) | No equivalent found in the pages read |

The multi-turn finding in §5 is not Claude-specific: Laban and colleagues tested OpenAI, Anthropic, Google, Meta and other models, and all of them did worse when the brief arrived in pieces.

## Deliverable · Ten briefs that hold up

Ten templates for general project work, each ready to paste, each followed by a worked example. Nine examples are worked on the Academy case, using only facts from its case file, cited by section; where the case file lacks a value the brief needs, the example marks it `[UNKNOWN: …]` and it must be replaced before sending. The voice rewrite (template 8) is worked on a neutral example whose content is invented and labelled so, because the case file holds no voice samples. Product facts are as read on 15 November 2026. BW5 uses the brief form below for every unit of your project; BW6 builds its checker brief from templates 3 and 9; BW7 writes its stage briefs from template 7.

### The brief form

Every template has the same parts in the same order, each traced to this unit:

- **TASK**: one line, opening with the verb of the artefact (§6).
- **READER**: who reads the output, what they know, what they will do with it (§1).
- **OUTPUT**: the contract: container, layout, length rule (§3).
- **CONSTRAINTS**: positive rules first; prohibitions as named patterns; an absolute only with its scope (§1).
- **EXAMPLES**: chosen for shape; a bad example only beside a good one, with why it is wrong (§4).
- **DONE WHEN**: checks you can run on the output line by line, including where unverifiable claims go (§3).
- **MATERIAL**: pasted inside tags, after the brief (§4).
- **TASK (again)**: the last line, when the material is long (§4).

```viz
{
  "kind": "flow",
  "caption": "The parts of every brief in this unit's deliverable, in order, each with the section of the unit it is traced to. From \"The brief form\" in the Deliverable; the form is this unit's synthesis (stated opinion).",
  "steps": [
    {"label": "TASK", "note": "the artefact's verb · §6"},
    {"label": "READER", "note": "§1"},
    {"label": "OUTPUT", "note": "the contract · §3"},
    {"label": "CONSTRAINTS", "note": "positive first · §1"},
    {"label": "EXAMPLES", "note": "bad only beside good · §4"},
    {"label": "DONE WHEN", "note": "checks on the output · §3"},
    {"label": "MATERIAL", "note": "inside tags · §4"},
    {"label": "TASK again", "note": "when the material is long · §4"}
  ]
}
```

**Conventions.**

- `[FILL: …]` is a slot you fill every time; the words after FILL say what goes in it.
- `[UNKNOWN: …]` in a worked example marks a real value the case file does not hold. Replace it before sending; never let the model guess it.
- Tags such as `<material>` and `</material>` wrap pasted text, so instructions and material cannot be confused ([*Prompting best practices*](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)).
- The **Model** line comes from BW2's routing table, read 15 Nov 2026; where BW2 has no row for the task, the line says so and the pick is an analogy.
- One brief per chat. If the first output misses, change the brief and open a new chat (§5). In a specified project, where briefs are not reworded once work starts, the miss is raised as a flag and the brief changes at a boundary (BW5 §5, §9).
- Each avoid-list is a starting choice. Extend it from the first outputs, as Anthropic's Opus 5.5 guide advises for named patterns: check what the first result did instead "and extend the list if needed" ([*Prompting Claude Opus 5.5*](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5-5)).

### 1 · Research brief

**Use when:** you need sources found and read before you write or decide. **Model:** large · Opus 5.5, medium; deep multi-source research, large · Opus 5.5, xhigh (BW2, rows 6 and 7).

    TASK: Find and report the sources that answer this question: [FILL: the question, in one sentence].

    READER: [FILL: who will use the findings, what they already know, and what they will write or decide from them].

    OUTPUT: a Markdown table in this chat, one row per claim, columns: Claim | Source (author or organisation, the page's own headline, link) | Date of the page or data | Date you read it | Kind (peer-reviewed, preprint, vendor, practice, benchmark) | Supporting words from the page (under 15 words, exact). At most [FILL: number] rows. Then a list headed "Not found": each part of the question no source answered.

    CONSTRAINTS:
    - Search first. Open every page you cite; cite nothing you did not open.
    - A claim carries the qualifiers its source carries (the sample, the models, the year, "up to") and no others.
    - A figure is cited to the page that states it for that thing, not to a page that repeats it.
    - Scope: [FILL: date range, places, kinds of source to include or exclude].
    - A part of the question no source answers goes under "Not found". Never fill it from memory.

    EXAMPLE (shape of one row):
    <example>
    | Gemini answers better with the question at the end of a long prompt | Google, "Long context" (Gemini API docs), link | updated 15 Oct 2026 | [read date] | vendor | "put your query / question at the end of the prompt" |
    </example>

    BAD EXAMPLE (shown beside the good one; never write this):
    <bad_example>
    | Putting the question last improves answers by 30% | Anthropic | | | vendor | |
    Why it is wrong: the page says "up to 30 percent", for inputs of 20k tokens or more, with no published method; the row drops both qualifiers, the headline, the dates and the supporting words.
    </bad_example>

    DONE WHEN:
    - every row has a link, a read date and supporting words that appear on the page;
    - no row carries a qualifier, number or scope its source does not state;
    - every part of the question is answered by a row or listed under "Not found".

**Worked example · the reading behind a unit whose facts change.** Academy's method marks a unit written with live search, and gives such a unit a staleness check six months later (Academy case file §2); its first audit named the pattern of its failures as qualifiers the source does not carry (case file §3), and its second found ten claims stale because a benchmark had changed version the day before they were read (case file §4). The brief carries all three lessons. The question is this unit's example; the case file records no research brief.

    TASK: Find and report the sources that answer this question: what is the context window of each current model in the Claude, ChatGPT and Gemini chat apps on a paid plan, as each vendor states it today?

    READER: the writer of one unit of a self-study course, who will cite each figure with the date it was read, and a checker who will open every link six months from now.

    OUTPUT: a Markdown table in this chat, one row per model and app, columns: Claim | Source (author or organisation, the page's own headline, link) | Date of the page or data | Date you read it | Kind | Supporting words from the page (under 15 words, exact). At most 30 rows. Then a list headed "Not found".

    CONSTRAINTS:
    - Search first. Open every page you cite; cite nothing you did not open.
    - Use each vendor's own pages only: help centre, documentation, pricing page. No news articles, no third-party comparisons.
    - A claim carries the qualifiers its source carries (the plan, the app or the API, "up to", "some models") and no others.
    - Where a figure names a version (a model version, an index version), the row names it.
    - Where two pages of the same vendor disagree, give both rows and say so.
    - A model whose window no vendor page states goes under "Not found". Never fill it from memory.

    EXAMPLE (shape of one row):
    <example>
    | [model] in [app], [plan]: [window] tokens | [vendor], "[page headline]", link | [page date or "no date shown"] | [read date] | vendor | "[the sentence fragment that gives the figure]" |
    </example>

    DONE WHEN:
    - every row has a link, a read date and supporting words that appear on the page;
    - no row carries a qualifier the page does not state;
    - every model in each app's model menu is a row or is under "Not found".

### 2 · Long-form draft

**Use when:** a report, chapter, proposal or course unit has to be written in full from a brief. **Model:** large · Opus 5.5, high (BW2, row 4).

    TASK: Write [FILL: the document: its kind and title] in full, in this chat.

    READER: [FILL: who reads it, what they already know, how they read it (on paper, on a phone, in one sitting), and what they will do after reading].

    SCOPE (in this order): [FILL: the items the document must cover, one line each].

    READ FIRST: [FILL: the files or pasted material the draft must use, and any earlier documents it must agree with].

    OUTPUT: one Markdown document. "# [title]", then one section per SCOPE item in the order given, then [FILL: the closing part: a recommendation, a table, a plan], built in full and never described, then "## Unsure" (up to ten claims you could not verify), then "## Sources" (every link cited in the text, and nothing else). Length: [FILL: a range, as a guide]. The items decide the length: do not pad an item, do not cut one short.

    CONSTRAINTS:
    - Cite every number, mechanism and recommendation where it is made, with a link, and say what kind of source it is.
    - Quotation marks hold the source's exact words.
    - A claim you cannot source is called unsourced or left out, and never enters the closing part.
    - Tone: [FILL: register, person, spelling].
    - Avoid: [FILL: named patterns, for example an opening paragraph that previews the document; a closing paragraph that restates it].

    DONE WHEN:
    - every SCOPE item has its own section, in order;
    - the closing part is complete and usable without reading the rest;
    - every link in the text is in Sources and every Sources entry is cited;
    - "Unsure" exists and has at most ten items.

    MATERIAL:
    <material>
    [FILL: anything pasted: notes, data, earlier sections]
    </material>

    TASK (again): write [FILL: the document] in full now.

**Worked example · a unit of a self-study course.** Academy's unit is a long-form report in Markdown, 2,000 to 6,000 words by guide, sources cited in place, with a closing deliverable built in full (case file §1). Its brief is a shared preamble joined to the unit's own brief, never reworded; the writer sees only that brief and the units already filed; before handing in it lists up to ten claims it could not verify (case file §2). The brief's text is not in the case file, so it is marked unknown.

    TASK: Write unit [UNKNOWN: the unit's code and title] of the course in full, with its deliverable, in this chat.

    READER: as the brief's preamble describes them; the preamble is part of the brief below.

    BRIEF (verbatim; never reword it):
    <brief>
    [UNKNOWN: the shared preamble, then the unit's own brief, pasted unchanged]
    </brief>

    READ FIRST: the units of this course already filed: [UNKNOWN: their file names]. Read nothing else from the project.

    OUTPUT: one Markdown file. "# [code] · [title]", then one section per item of the brief in the brief's order, then the deliverable the brief names, built in full and never described, then "## Sources" (every link cited, nothing else). Length: 2,000 to 6,000 words, as a guide; the items decide. Separately, a list of up to ten claims you could not verify.

    CONSTRAINTS:
    - Run the brief's sourcing standard over every claim before handing in.
    - A claim you cannot source is called unsourced or left out, and never enters the deliverable.
    - Quotation marks hold the source's exact words; a figure is cited to the page that states it.
    - A pointer to another unit says what that unit says; open it first.
    - Avoid: a preamble before the first section; a closing summary; motivational lines.

    DONE WHEN:
    - every item of the brief has its own section, in order;
    - the deliverable is complete and usable without reading the unit;
    - every link in the text is in Sources and every Sources entry is cited;
    - the list of unverified claims exists and has at most ten items.

    TASK (again): write the unit in full now.

### 3 · Critique of a draft

**Use when:** a draft must be checked before you rely on it or send it. Run it in a fresh chat that has not seen the draft written, on a model other than the writer's where you can afford it (BW2 §5). **Model:** large, fresh context · Fable 5.2, high (BW2, row 5).

    TASK: Check the draft below against its sources and its brief, and report findings. Do not edit the draft.

    READER: [FILL: the person who will apply the findings]. They apply each finding as an exact text replacement; a finding they would have to re-check before applying has failed.

    OUTPUT: Markdown in this chat.
    1. Findings, most serious first, each in this form:
       [error | should-fix | minor] [section] · Current: "[exact text, occurring once in the draft]" · Problem: [what is wrong] · Fix: "[replacement text]" · Basis: [source link and where on the page]
       An error is a claim the source does not support, a miscitation, or a missing part of the brief. A should-fix makes the draft less accurate or less usable. A minor is wording.
    2. Confirmed: each claim you checked that holds, one line, with its source.
    3. Last line: verdict (keep | fix | rewrite) and the counts.

    CONSTRAINTS:
    - Open every cited source before giving a verdict on its claim. A source you cannot open is "unverifiable", never an error.
    - Check the draft's closing part against the brief: is it there, in full, as the brief names it?
    - Flag only what affects correctness or the brief's requirements; style preferences are minors at most.
    - No praise, no summary of the draft.
    - Scope: [FILL: every cited claim, or a sample; see template 9 for sampling].

    MATERIAL:
    <brief>
    [FILL: the brief the draft was written from]
    </brief>
    <draft>
    [FILL: the draft]
    </draft>

    DONE WHEN:
    - every finding quotes text that occurs exactly once in the draft and gives its replacement and its basis;
    - every cited claim in scope is either a finding or confirmed;
    - the last line gives one verdict and the counts.

    TASK (again): check the draft above and report.

**Worked example · the fresh check before filing.** Academy's fresh check is a separate context that has not seen the unit written; it checks every cited claim against its source and the deliverable against the brief, writes findings as error, should-fix or minor, and never edits; a maintainer verifies each finding and applies it as an exact replacement (case file §2). The kinds of error its reports name include a figure the cited page does not carry, an author named wrongly, a law that had changed, a quotation the page does not hold, a count that did not add up, and a product fact that differed between two of the vendor's own pages (case file §5).

    TASK: Check unit [UNKNOWN: code] against its sources and its brief, and report findings. Do not edit the unit.

    READER: the maintainer, who verifies each finding and applies it as an exact text replacement; a finding they would have to re-check before applying has failed.

    OUTPUT: Markdown in this chat.
    1. Findings, most serious first: [error | should-fix | minor] [section] · Current: "[exact text, occurring once]" · Problem · Fix: "[replacement]" · Basis: [link and where].
    2. Confirmed: each claim checked that holds, one line, with its source.
    3. Last line: verdict (keep | fix | rewrite) and the counts of errors, should-fix and minor.

    CONSTRAINTS:
    - Open every cited source before giving a verdict. A source you cannot open is "unverifiable", never an error.
    - Look in particular for: a figure the cited page does not carry; an author named wrongly; a law or product fact that has changed; a quotation the page does not hold; a count that does not add up; a product fact that differs between two of the vendor's own pages.
    - Check the deliverable against the brief: present, in full, as named.
    - Flag only what affects correctness or the brief's requirements.
    - No praise, no summary of the unit.
    - Scope: every cited claim in the unit.

    MATERIAL:
    <brief>
    [UNKNOWN: the unit's brief, verbatim]
    </brief>
    <unit>
    [UNKNOWN: the unit as handed in]
    </unit>

    DONE WHEN:
    - every finding quotes text that occurs exactly once in the unit and gives its replacement and its basis;
    - every cited claim is either a finding or confirmed;
    - the last line gives one verdict and the counts.

    TASK (again): check the unit above and report.

### 4 · Decision memo

**Use when:** someone must choose between options and the choice should rest on stated evidence. **Model:** BW2 has no row for this task; large · Opus 5.5, high, by analogy with its row 10 (a plan or spec: open-ended judgement).

    TASK: Write a decision memo on this question: [FILL: the decision, as one question with a yes, a no, or named options].

    READER: [FILL: who decides, what they already know, and by when they decide].

    OUTPUT: Markdown in this chat, at most [FILL: words, e.g. 400]:
    1. The decision asked, in one sentence.
    2. Options (two to four): for each, what it costs, what it risks, and the evidence from the material, with where it is.
    3. Recommendation: one option; at most three reasons, each twelve words or fewer, each pointing to evidence in 2.
    4. What would change the recommendation.
    5. Unknowns: facts the decision needs that the material does not hold.

    CONSTRAINTS:
    - Use only the material. A fact not in it goes under Unknowns.
    - Every option is one a reasonable person would choose; add none to make the list longer.
    - Keep each fact at the weight the material gives it.

    EXAMPLE (shape of the recommendation):
    <example>
    [FILL: one recommendation from a past memo that worked]
    </example>

    BAD EXAMPLE (shown beside the good one; never write this):
    <bad_example>
    Recommendation: it depends on your priorities; both options have merit.
    Why it is wrong: it picks no option, gives no reason, and points to no evidence.
    </bad_example>

    MATERIAL:
    <material>
    [FILL: the facts, records, figures the decision rests on, each with its source]
    </material>

    DONE WHEN:
    - exactly one option is recommended;
    - every reason points to evidence in the options section;
    - every fact appears in the material or is listed under Unknowns.

**Worked example · whether a figure that keeps failing its check is dropped.** In Academy, a separate agent checks each figure against the unit's text; a figure that failed was fixed and checked again by a new agent. The early rule dropped a figure after three failures, and two were dropped; the later rule, set by the owner, is that figures are never dropped and are fixed until they pass; one sitemap figure passed on its eighth check (case file §6). The case file records the decision, not a memo; this brief is how the question could have been put. The record holds no measure of hours or money per unit (case file §9), so the cost of each re-check is unknown.

    TASK: Write a decision memo on this question: should a figure that fails its check three times be dropped from its unit, or fixed until it passes?

    READER: the owner of the project, who sets the rule (case file §6).

    OUTPUT: Markdown in this chat, at most 400 words: the decision asked; the two options, each with its cost, its risk and the evidence from the material; one recommendation with at most three reasons of twelve words or fewer; what would change it; unknowns.

    CONSTRAINTS:
    - Use only the material. A fact not in it goes under Unknowns.
    - Keep each fact at the weight the material gives it.

    EXAMPLE (invented, on another decision; shape of the recommendation):
    <example>
    Recommendation: B, move the review to Mondays. Reason: two of three missed reviews fell on Fridays (Options, B).
    </example>

    BAD EXAMPLE (shown beside the good one; never write this):
    <bad_example>
    Recommendation: it depends on your priorities; both options have merit.
    Why it is wrong: it picks no option, gives no reason, and points to no evidence.
    </bad_example>

    MATERIAL:
    <material>
    - Each figure is checked by a separate agent against the unit's text: every label and number must already be in the text. (Case file §6)
    - A figure that fails is fixed and checked again by a new agent. (Case file §6)
    - Under the rule "dropped after three failures", two figures were dropped. (Case file §6)
    - One sitemap figure passed on its eighth check. (Case file §6)
    - Time or cost per re-check: [UNKNOWN: not recorded; case file §9]
    </material>

    DONE WHEN:
    - exactly one option is recommended;
    - every reason points to evidence in the options section;
    - the cost of re-checks is listed under Unknowns.

### 5 · Extraction to a table

**Use when:** the same fields must be pulled from many documents into one table. **Model:** small · Haiku 5.5, high; totals by script, never by the model (BW2, row 2).

    TASK: Extract [FILL: the fields] from each document below into one table.

    READER: [FILL: who uses the table and for what: a count, a comparison, a check].

    OUTPUT: one Markdown table (or CSV, if [FILL: the tool that will read it] needs it), one row per [FILL: the unit of a row: a document, a person, an item], columns: [FILL: the columns, in order, with the unit of each number]. No totals or averages: these are computed afterwards by a script or a spreadsheet. Then a list of any document that produced no row, with the reason.

    CONSTRAINTS:
    - Copy values as the document gives them. A field the document does not state is "not stated"; never infer it.
    - Numbers exactly as written, with their units.
    - One row per [FILL: unit]; no merged rows.

    EXAMPLE (one row):
    <example>
    [FILL: one correct row, from a document you have checked yourself]
    </example>

    DONE WHEN:
    - the number of rows equals the number of [FILL: units] in the material;
    - every cell is either in its document or "not stated";
    - three rows picked at random match their documents when you check them by hand.

    MATERIAL:
    <documents>
    [FILL: the documents, each in its own <document name="..."> tag]
    </documents>

    TASK (again): extract the table from the documents above.

**Worked example · fresh-check findings per unit.** Academy's case file holds a table of the 36 units that got a fresh check before filing, with each unit's course, checker, verdict and counts of errors, should-fix and minor findings; the totals are 58 errors, 237 should-fix and 303 minor (case file §5). This brief rebuilds such a table from the fresh-check reports; the reports themselves are not in the case file.

    TASK: Extract the course, unit, checker model, verdict and finding counts from each fresh-check report below into one table.

    READER: the owner, who will total the counts and compare them by course and by checker.

    OUTPUT: one Markdown table, one row per report, columns: Course | Unit | Checker | Verdict (keep, fix or rewrite) | Errors | Should-fix | Minor. No totals: they are computed afterwards by a script. Then a list of any report that produced no row, with the reason.

    CONSTRAINTS:
    - Copy values as the report gives them. A field the report does not state is "not stated"; never infer it.
    - Counts are the report's own counts on the draft as handed in, not after fixes.
    - One row per report.

    EXAMPLE (one row, from the case file's table):
    <example>
    | UX | IA1 | Opus 5.5 | keep | 0 | 4 | 7 |
    </example>

    DONE WHEN:
    - the table has 36 rows;
    - every cell is in its report or "not stated";
    - the script's totals are 58 errors, 237 should-fix and 303 minor; if not, find the row that differs before using the table.

    MATERIAL:
    <documents>
    [UNKNOWN: the 36 fresh-check reports, each in its own <document name="..."> tag]
    </documents>

    TASK (again): extract the table from the reports above.

### 6 · Summary for a named reader

**Use when:** one person must act on material too long for them to read. **Model:** mid · Sonnet 5.5, medium (BW2, row 3).

    TASK: Summarise the material below for [FILL: the named reader], so they can [FILL: the decision or action].

    READER: [FILL: their role, what they already know, how long they will spend reading, where they read].

    OUTPUT: at most [FILL: words]. First sentence: what they must decide or do, and the main reason. Then up to [FILL: number] points, each one sentence, each saying where in the material it comes from. Then one line: what the material does not say that they might assume.

    CONSTRAINTS:
    - Use only the material. Numbers exactly as the material gives them.
    - Keep the material's qualifiers (the sample, the scope, "none", "only").
    - Leave out what does not bear on [FILL: the decision or action].

    EXAMPLE (shape of the first sentence):
    <example>
    [FILL: one sentence you would want to read first, from a past summary that worked]
    </example>

    DONE WHEN:
    - the first sentence states the action and its reason;
    - every number appears in the material in the same form;
    - every point says where it comes from.

    MATERIAL:
    <material>
    [FILL: the material]
    </material>

    TASK (again): write the summary for [FILL: the named reader].

**Worked example · the first audit, for the owner.** Academy's first audit sampled the first three units of its marketing course: one of eight sampled claims failed, which triggered a full audit; of 91 claims, 23 failed and none was stale; nothing was invented and no conclusion flipped. The verdict was rewrite, for two reasons: the three deliverables did not exist, and two table rows rested on figures the cited vendor pages did not contain. The pattern it named was qualifiers the source does not carry (case file §3). The audit report's text is not in the case file.

    TASK: Summarise the audit report below for the owner of the project, so they can decide today whether to rewrite the three units it covers.

    READER: the owner, who decides whether the three units are rewritten.

    OUTPUT: at most 150 words. First sentence: the decision and the main reason. Then up to four points, each one sentence, each saying which part of the report it comes from. Then one line: what the report does not say that the owner might assume.

    CONSTRAINTS:
    - Use only the report. Numbers exactly as the report gives them.
    - Keep the report's qualifiers: the sample size, "none was stale", "nothing was invented".
    - Leave out claim-by-claim detail; the owner opens the report for that.

    EXAMPLE (shape of the first sentence):
    <example>
    Rewrite all three units: their deliverables do not exist, and two table rows cite figures their vendor pages do not contain.
    </example>

    DONE WHEN:
    - the first sentence states the decision and its reason;
    - 23 of 91, and one of eight, appear exactly as in the report;
    - every point says where in the report it comes from.

    MATERIAL:
    <report>
    [UNKNOWN: the text of the first audit's report]
    </report>

    TASK (again): write the summary for the owner.

### 7 · Plan, then build

**Use when:** the work is large or the approach is unclear, so you want to approve a plan before anything is built. Two briefs, two chats: the plan, then each part built from the approved plan in its own chat (§5, §6). **Model:** the plan, large · Opus 5.5, high (BW2, row 10); each build, the row for what is built (BW2, row 4 for a long draft, row 8 for a code change).

Stage 1, the plan:

    TASK: Write a plan for [FILL: the project or piece of work]. Do not build any part of it yet; stop when the plan is written.

    READER: [FILL: who approves the plan, and what they will check it against].

    OUTPUT: Markdown in this chat:
    1. Goal: one sentence.
    2. Outcomes: [FILL: how many] things that will be true when it is done, each one you can check.
    3. Parts, in build order: each with a one-line scope, the artefact it produces, and the check that says it is done.
    4. Open questions: what you need decided before building, each with the options.

    CONSTRAINTS:
    - Every part produces a named artefact; a part that only "explores" or "considers" is not a part.
    - Each part can be built in one chat from the plan and the parts before it.
    - [FILL: limits on size, time, tools].

    MATERIAL:
    <material>
    [FILL: what the plan must use: the request, constraints, earlier work]
    </material>

    DONE WHEN:
    - the goal is one sentence;
    - every part names its artefact and its done-check;
    - nothing has been built.

Stage 2, each part, in a new chat:

    TASK: Build [FILL: the part's artefact] for part [FILL: number] of the approved plan below.

    READER: [FILL: as in the plan].

    OUTPUT: [FILL: the artefact as the plan names it], in full.

    CONSTRAINTS:
    - Build this part only. If the plan is wrong or incomplete for this part, say so at the top and build what the plan allows.
    - Agree with the parts already built: [FILL: their files or text].

    MATERIAL:
    <approved_plan>
    [FILL: the plan as approved, unchanged]
    </approved_plan>

    DONE WHEN: [FILL: the part's done-check, copied from the plan].

    TASK (again): build part [FILL: number] now.

**Worked example · a course syllabus, then its briefs.** Academy starts a course as a goal in one sentence, three measurable outcomes, eight to twelve core units and two or three deep dives, each unit with a one-line scope, a named deliverable and a brief; each unit is then written in its own context from its brief (case file §2). The course's subject is not a case fact, so it is marked unknown.

Stage 1:

    TASK: Write a syllabus for a self-study course on [UNKNOWN: the subject]. Do not write any unit or brief yet; stop when the syllabus is written.

    READER: the owner, who approves the syllabus and will check that every unit can be written in one context from its brief alone.

    OUTPUT: Markdown in this chat:
    1. Goal: one sentence.
    2. Three measurable outcomes.
    3. Eight to twelve core units and two or three deep dives, in build order: each with a one-line scope and a named deliverable.
    4. Open questions, each with the options.

    CONSTRAINTS:
    - Every unit names a deliverable that can be built in full inside the unit.
    - Each unit can be written from its brief and the units before it, with no other context.

    MATERIAL:
    <material>
    [UNKNOWN: the course request: the subject, the reader, what they should be able to do]
    </material>

    DONE WHEN:
    - the goal is one sentence and there are three outcomes;
    - every unit has a scope and a deliverable;
    - no unit or brief has been written.

Stage 2, one new chat per brief:

    TASK: Write the brief for unit [UNKNOWN: code] of the approved syllabus below.

    READER: the writer of that unit, who will see only this brief, joined to the course's shared preamble, and the units already filed.

    OUTPUT: the unit's brief: what it covers, in order, and its deliverable, named.

    CONSTRAINTS:
    - Cover this unit only, within its scope line.
    - Say nothing the shared preamble already says.

    MATERIAL:
    <approved_plan>
    [UNKNOWN: the syllabus as approved, unchanged]
    </approved_plan>

    DONE WHEN: the brief can be followed by a writer who has seen nothing else.

    TASK (again): write the brief for unit [UNKNOWN: code] now.

### 8 · Rewrite in a voice from samples

**Use when:** a draft has the right content and the wrong voice, and you have samples of the voice you want. **Model:** BW2 has no row for this task; mid · Sonnet 5.5, medium, by analogy with its row 3 (well-scoped writing from given material).

    TASK: Rewrite the draft below in the voice of the samples.

    READER: [FILL: who reads the rewritten text, and where].

    OUTPUT: the rewritten text only, then a list of every sentence whose meaning you changed, with the reason. Length within [FILL: a range, e.g. ten per cent either side] of the draft.

    CONSTRAINTS:
    - Match these features of the samples: [FILL: what you see in them: sentence length, person, vocabulary, how a paragraph opens, what the voice never does].
    - Keep every fact, number, name and date in the draft. Add none.
    - Keep the draft's order unless [FILL: when reordering is allowed].
    - Avoid: [FILL: named patterns the samples never use].

    EXAMPLES (the voice; match their shape, not their topics):
    <voice_sample>
    [FILL: sample 1, 100 to 300 words]
    </voice_sample>
    <voice_sample>
    [FILL: sample 2, on a different topic]
    </voice_sample>

    BAD EXAMPLE (beside the samples; never write this):
    <bad_example>
    [FILL: one sentence of the draft rewritten wrongly]
    Why it is wrong: [FILL: the pattern it shows, named].
    </bad_example>

    MATERIAL:
    <draft>
    [FILL: the draft]
    </draft>

    DONE WHEN:
    - every fact, number, name and date in the draft is in the rewrite, and nothing new is;
    - none of the avoided patterns appears;
    - the length is within the range.

**Worked example · a neutral one.** The case file holds no voice samples, so this example is invented: the practice, the samples and the draft are made up for illustration, and nothing in them is a fact. The shape is what to copy.

    TASK: Rewrite the draft below in the voice of the samples.

    READER: clients of a small design studio (invented), reading the studio's monthly email on their phones.

    OUTPUT: the rewritten text only, then a list of every sentence whose meaning you changed, with the reason. Length within ten per cent of the draft.

    CONSTRAINTS:
    - Match these features of the samples: sentences under twenty words; first person plural; the news in the first sentence; one concrete detail per paragraph; no exclamation marks.
    - Keep every fact, number, name and date in the draft. Add none.
    - Keep the draft's order.
    - Avoid: "we are thrilled", "exciting news", "journey"; a closing line inviting replies.

    EXAMPLES (invented; the voice):
    <voice_sample>
    We moved the print room to the ground floor in March. The big press needed a floor that does not flex. It also means deliveries no longer climb two flights of stairs.
    </voice_sample>
    <voice_sample>
    Our proofing day is now Thursday. Proofs sent by Wednesday at noon come back the next morning. Anything later waits a week.
    </voice_sample>

    BAD EXAMPLE (invented; never write this):
    <bad_example>
    We're thrilled to share some exciting news about our studio's journey!
    Why it is wrong: it uses three avoided words and an exclamation mark, and delays the news.
    </bad_example>

    MATERIAL:
    <draft>
    (invented) We are very pleased to announce that, after a great deal of consideration, the studio will be closed for two weeks from 22 December to 5 January, during which time we will not be able to respond to enquiries, although any urgent matters can be sent to the usual address and will be dealt with on our return.
    </draft>

    DONE WHEN:
    - 22 December, 5 January, two weeks and the usual address are all in the rewrite, and nothing new is;
    - none of the avoided words appears;
    - the length is within ten per cent of the draft.

### 9 · Audit of claims against sources

**Use when:** a finished document's claims must be checked against their sources by sample, with a rule that sends it to a full check. **Model:** large, top rung, a model other than the writer's · Fable 5.2, high (BW2, row 9). BW6 sets the sampling rule and what a clean sample proves; this template is the brief that carries it.

    TASK: Audit the claims in [FILL: the document] against their cited sources, by sample. Report; do not edit the document.

    READER: [FILL: who decides what happens to the document on your verdict].

    METHOD, in this order:
    1. List the document's sections. From each, draw one checkable claim: a sentence with a number, a date, a named source, an attribution, a mechanism or a recommendation. Record the sample before checking anything.
    2. Open each sampled claim's source. Verdict: PASS (the source holds it), FAIL (wrong, unsupported, miscited or invented), STALE (true when written, superseded now: give the newer value and its source), or UNVERIFIABLE (the source cannot be opened).
    3. If more than [FILL: the threshold, e.g. one in ten] sampled claims FAIL, check every cited claim in the document by the same method.
    4. Check the document's closing part against its body: it adds no claim the body does not source.

    OUTPUT: a table (section | claim, exact | source | verdict | note); the failure rate; one verdict: [FILL: the verdicts you use, e.g. pass | full audit run, with its result | rewrite, with the sections named].

    CONSTRAINTS:
    - Open every source before its verdict.
    - A FAIL quotes what the source says instead.
    - No praise, no summary of the document.

    MATERIAL:
    <document>
    [FILL: the document]
    </document>

    DONE WHEN:
    - every section has one sampled claim with a verdict and a source;
    - the threshold rule has been applied and its result stated;
    - the last line gives one verdict.

    TASK (again): audit the document above.

**Worked example · the sample audit.** Academy runs a sample audit every four units: one claim is drawn from every section of each unit and checked against its source; a unit with more than one sampled claim in ten failing is audited in full; the verdicts are pass, full audit and rewrite (case file §2). Its first audit found that the failing claims carried qualifiers their sources did not (case file §3). The unit codes are not case facts here, so they are marked unknown.

    TASK: Audit the claims in units [UNKNOWN: the four unit codes] against their cited sources, by sample. Report; do not edit any unit.

    READER: the owner, who files, corrects or sends back each unit on your verdict.

    METHOD, in this order:
    1. For each unit, list its sections. From each section, draw one checkable claim. Record the sample before checking anything.
    2. Open each sampled claim's source. Verdict: PASS, FAIL, STALE (give the newer value and its source) or UNVERIFIABLE.
    3. If more than one sampled claim in ten FAILs for a unit, check every cited claim in that unit.
    4. Check each unit's deliverable: it exists in full, follows from the unit's evidence, and adds no unsourced claim.

    OUTPUT: per unit, a table (section | claim, exact | source | verdict | note); its failure rate; its verdict: pass | full audit run, with its result | rewrite, with the sections named.

    CONSTRAINTS:
    - Open every source before its verdict.
    - A FAIL quotes what the source says instead.
    - Look in particular for qualifiers the claim carries that its source does not.
    - No praise, no summary of the units.

    MATERIAL:
    <units>
    [UNKNOWN: the four units, each in its own <unit code="..."> tag]
    </units>

    DONE WHEN:
    - every section of every unit has one sampled claim with a verdict and a source;
    - the one-in-ten rule has been applied to each unit;
    - the last lines give one verdict per unit.

    TASK (again): audit the four units above.

### 10 · Code change with its test

**Use when:** a script, formula or small tool must change, and you want proof that the change works and broke nothing. You do not need to write code to use this brief; you need to be able to run the command it asks for. **Model:** mid · Sonnet 5.5, medium (BW2, row 8). In Claude Code, the model can run the test itself (§3).

    TASK: Change [FILL: the script or file] so that [FILL: the behaviour you want, in one sentence], and add a test that fails before the change and passes after it.

    READER: [FILL: who will run and maintain the code, and how much code they read].

    OUTPUT:
    1. The change, as a diff.
    2. The test.
    3. The command that runs the tests, and its output after the change.
    4. Three lines: what changed, what did not, how to undo it.

    CONSTRAINTS:
    - Change only [FILL: the files that may change].
    - No new dependencies unless [FILL: when one is allowed].
    - Do not add features, files, documentation or refactors that were not asked for; mention any you think would help at the end.
    - Show the test output; do not state that the tests pass without it.

    EXAMPLE (the behaviour, as cases):
    <example>
    [FILL: two or three inputs with the output you expect for each]
    </example>

    DONE WHEN:
    - the new test fails on the old code and passes on the new;
    - every existing test still passes, shown by the output;
    - no file outside the allowed list changed.

    MATERIAL:
    <code>
    [FILL: the file, or its path if the tool can read it]
    </code>

    TASK (again): make the change and its test.

**Worked example · a script check on figures.** In Academy, figures are declared as data and drawn by a script, and a separate agent checks each figure against the unit's text: every label and number must already be in the text (case file §6). The change below is hypothetical: it would move one part of that agent's check into a script. The case file records the rule and the agent check, not this change, and it names no files.

    TASK: Change [UNKNOWN: the checking script's path] so that it lists every number in a unit's figure blocks that does not appear in the unit's own text, and add a test that fails before the change and passes after it.

    READER: the project's owner, who decides whether the change goes in.

    OUTPUT:
    1. The change, as a diff.
    2. The test.
    3. The command that runs the tests, and its output after the change.
    4. Three lines: what changed, what did not, how to undo it.

    CONSTRAINTS:
    - Change only the checking script and its test file: [UNKNOWN: their paths].
    - No new dependencies.
    - Report the missing numbers; do not change any unit or figure.
    - Do not add features, files, documentation or refactors that were not asked for; mention any you think would help at the end.
    - Show the test output; do not state that the tests pass without it.

    EXAMPLE (the behaviour, as cases):
    <example>
    - A figure whose numbers all appear in the unit's text: no output.
    - A figure with one number the text does not contain: one line naming the unit, the figure and the number.
    </example>

    DONE WHEN:
    - the new test fails on the old code and passes on the new;
    - every existing test still passes, shown by the output;
    - no file outside the two allowed changed.

    MATERIAL:
    <code>
    [UNKNOWN: the checking script]
    </code>

    TASK (again): make the change and its test.

### Template: your own brief

The form, blank, for any task the ten do not cover. Each blank says what goes in it.

    TASK: [FILL: the verb of the artefact, then the artefact: "Write the…", "Extract…", "Change…"].

    READER: [FILL: who reads the output, what they already know, what they will do with it].

    OUTPUT: [FILL: the container (a file, a table in the chat, an email), the layout (sections, columns), and the length: a hard limit for a short output, a range as a guide for a long one].

    CONSTRAINTS:
    - [FILL: what the output must contain, stated positively].
    - [FILL: the scope: what is in and what is out].
    - Avoid: [FILL: named patterns, each specific enough to spot].

    EXAMPLES:
    <example>
    [FILL: one output of the right shape; add more only if the first output misses]
    </example>
    <bad_example>
    [FILL: optional; one wrong output, only beside a good one]
    Why it is wrong: [FILL: the pattern, named].
    </bad_example>

    DONE WHEN:
    - [FILL: a check you can run on the output];
    - [FILL: a second check];
    - claims you could not verify are listed under "Unsure", not left in the text.

    MATERIAL:
    <material>
    [FILL: the pasted material, or "none"]
    </material>

    TASK (again): [FILL: the TASK line, repeated, when the material is long].

## Sources

All web pages read on 15 November 2026. Most vendor documentation pages show no date; where a page gives one, it is listed.

**Vendor documentation and statements: Anthropic**

- Anthropic. *Prompting best practices*. Claude Platform Docs. https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices
- Anthropic. *Prompting Claude Opus 5.5*. Claude Platform Docs. https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5-5
- Anthropic. *Prompting Claude Sonnet 5.5*. Claude Platform Docs. https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-sonnet-5-5
- Anthropic. *Prompting Claude Fable 5.2*. Claude Platform Docs. https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-2
- Anthropic. *Prompt engineering overview*. Claude Platform Docs. https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview
- Anthropic. *Reduce hallucinations*. Claude Platform Docs. https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations
- Anthropic. *Best practices for Claude Code*. Claude Code Docs. https://code.claude.com/docs/en/best-practices.md
- Anthropic. *How Claude remembers your project*. Claude Code Docs. https://code.claude.com/docs/en/memory
- Rajasekaran, P., Dixon, E., Ryan, C. and Hadfield, J. (Anthropic Applied AI team). *Effective context engineering for AI agents*. Anthropic Engineering, 29 September 2025. https://anthropic.com/engineering/effective-context-engineering-for-ai-agents
- Claude. *Best practices for prompt engineering for 2026*. 10 November 2025. https://claude.com/resources/articles/best-practices-for-prompt-engineering

**Vendor documentation: OpenAI and Google**

- OpenAI Help Center. *Best practices for prompt engineering with the OpenAI API*. The page shows only a relative update date. https://help.openai.com/en/articles/6654000
- OpenAI. *Prompt engineering*. OpenAI API docs. https://developers.openai.com/api/docs/guides/prompt-engineering
- OpenAI. *Using GPT-6*. OpenAI API docs. https://developers.openai.com/api/docs/guides/prompt-guidance
- Google. *Long context*. Gemini API docs, last updated 15 October 2026. https://ai.google.dev/gemini-api/docs/long-context
- Google Cloud. Vertex AI documentation page on prompting Gemini 3, read 15 November 2026 (no headline shown in the copy read). https://docs.cloud.google.com/vertex-ai/generative-ai/docs/start/gemini-3-prompting-guide

**Research**

- Min, S., Lyu, X., Holtzman, A., Artetxe, M., Lewis, M., Hajishirzi, H. and Zettlemoyer, L. "Rethinking the Role of Demonstrations: What Makes In-Context Learning Work?". *Proceedings of EMNLP 2022*, 11048–11064 (peer-reviewed). https://aclanthology.org/2022.emnlp-main.759
- Jang, J., Ye, S. and Seo, M. "Can Large Language Models Truly Understand Prompts? A Case Study with Negated Prompts". *Proceedings of the 1st Transfer Learning for Natural Language Processing Workshop*, PMLR 203 (2023), 52–62 (peer-reviewed, workshop). https://proceedings.mlr.press/v203/jang23a.html
- Shi, F., Chen, X., Misra, K., Scales, N., Dohan, D., Chi, E. H., Schärli, N. and Zhou, D. "Large Language Models Can Be Easily Distracted by Irrelevant Context". *Proceedings of the 40th International Conference on Machine Learning* (ICML 2023), PMLR 202 (peer-reviewed). https://arxiv.org/pdf/2302.00093
- Chia, Y. K., Chen, G., Tuan, L. A., Poria, S. and Bing, L. "Contrastive Chain-of-Thought Prompting". arXiv 2311.09277, 2023 (preprint). https://arxiv.org/pdf/2311.09277
- Zheng, M., Pei, J., Logeswaran, L., Lee, M. and Jurgens, D. "When "A Helpful Assistant" Is Not Really Helpful: Personas in System Prompts Do Not Improve Performances of Large Language Models". *Findings of the Association for Computational Linguistics: EMNLP 2024*, 15126–15154 (peer-reviewed). https://aclanthology.org/2024.findings-emnlp.888/
- Levy, M., Jacoby, A. and Goldberg, Y. "Same Task, More Tokens: the Impact of Input Length on the Reasoning Performance of Large Language Models". *Proceedings of the 62nd Annual Meeting of the ACL (Volume 1: Long Papers)*, 2024, 15339–15353 (peer-reviewed). https://aclanthology.org/2024.acl-long.818
- Liu, N. F., Lin, K., Hewitt, J., Paranjape, A., Bevilacqua, M., Petroni, F. and Liang, P. "Lost in the Middle: How Language Models Use Long Contexts". *Transactions of the Association for Computational Linguistics* 12 (2024), 157–173 (peer-reviewed). https://aclanthology.org/2024.tacl-1.9/
- Jaroslawicz, D., Whiting, B., Shah, P. and Maamari, K. "How Many Instructions Can LLMs Follow at Once?". arXiv 2507.11538, 2025 (preprint); poster at a NeurIPS 2025 workshop. https://arxiv.org/abs/2507.11538 · https://neurips.cc/virtual/2025/122417
- Zhang, W., Zhou, Z., Wang, K., Fang, J., Xu, R., Zhang, Y., Wang, R., Zhang, G., Li, X., Sun, L., Lyu, L., Liu, Y. and Su, S. "LIFEBENCH: Evaluating Length Instruction Following in Large Language Models". NeurIPS 2025, Datasets and Benchmarks Track (peer-reviewed). https://proceedings.nips.cc/paper_files/paper/2025/hash/c84f00ccee3d35cee1901acb0e258dc7-Abstract-Datasets_and_Benchmarks_Track.html
- Laban, P., Hayashi, H., Zhou, Y. and Neville, J. "LLMs Get Lost In Multi-Turn Conversation". arXiv 2505.06120, 2025; ICLR 2026 (peer-reviewed). https://arxiv.org/pdf/2505.06120 · https://iclr.cc/virtual/2026/oral/10009147

**The case**

- Academy case file (`generator/data/building-with-ai/case-academy.md`), compiled 11 November 2026; cited by section, §1 to §7 and §9.

**This course**

- BW1 · Mental model, §1 to §7.
- BW2 · Choosing the model and the effort, §3, §5 and the routing table.

## Unsure list

1. Anthropic's "up to 30 percent" gain for queries placed after long documents (§4) is vendor data: the page publishes no method, task set or model list. It is reported as such, and nothing in the deliverable depends on the number.
2. Google's prompt-design page for the Gemini API was not checked: its fetch was refused (15 Nov 2026), so Google's advice on examples and on one prompt per instruction is left out. Google rows in §4 and §8 rest on *Long context* and on a Google Cloud page on prompting Gemini 3 whose headline was not shown in the copy read; that page's Sources title is given as organisation, document type and date.
3. OpenAI's API guide read on 15 Nov 2026 says GPT models "benefit from precise instructions"; an earlier check of the same page (29 Oct 2026, recorded in the source material) had "very precise instructions". The page now names GPT-6 models, so it has probably been revised; the unit quotes the wording read on 15 Nov.
4. OpenAI's help-centre article shows only a relative update date ("Updated: 6 days ago"), so how current its advice is for OpenAI's present models could not be established.
5. Laban et al.: the aptitude drop is 15% in the paper's Figure 1 and 16% in its text; the unit gives both. The ICLR 2026 venue rests on the iclr.cc page title returned by search (an oral-session URL); that page was not fetched.
6. Levy et al., Jaroslawicz et al. (IFScale) and Zhang et al. (LIFEBench): the models tested are not named in the abstracts read, and §7's table says so; their full model lists were not read.
7. Anthropic's model-specific prompting guides (Opus 5.5, Sonnet 5.5, Fable 5.2) and Claude Code's best-practices page are written for API, agent and coding use; carrying their advice into a claude.ai chat is this unit's inference throughout.
8. Academy case file §1 gives a 2,000 to 6,000-word guide and a longest UX unit of about 16,900 words; the file does not say whether that length was wanted, and the unit reads it only as a range that did not bound a long output.
9. The Model lines of templates 4 (decision memo) and 8 (voice rewrite) have no BW2 row; they are analogies from BW2's rows 10 and 3, marked as such.
Object: the written brief (§1, and the Deliverable's brief form)

Fresh check 2026-11-15 (Opus 5.5): fix · 0 errors, 8 should-fix, 11 minor; report `audits/building-with-ai/fresh-check-BW3.md`

*Correction, 17 November 2026: changed by this course's syllabus review (BW-1, row S-BW) after a corrections check by a fresh Opus 5.5 agent (audits/building-with-ai/corrections-2026-11-17-S-BW.md); see the course's changelog for what changed.*
