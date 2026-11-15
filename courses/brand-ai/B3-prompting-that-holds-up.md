---
code: B3
title: Prompting that holds up
course: brand-ai · B · Using AI to Build a Brand
model: Opus 5.5
written: 2026-10-28
search: off
---

# B3 · Prompting that holds up

The evidence in this unit is of three kinds, labelled where it appears. **Vendor guidance** is a model maker's own documentation on how to prompt its models (Anthropic, OpenAI, Google): it says what the vendor recommends and almost never shows the measurement behind it. **Research** is peer-reviewed work, or a preprint labelled as one; most of it tested models from 2022 to 2025, and none of it tested Opus 5.5. **His setup** is the Learning Project as it stood on 28 October 2026: his saved preferences, the Project's method files and his voice-drafting skill. The unit was written with search off; searches were used only to confirm sources and their URLs, checked 28–29 October 2026. What a context window is, which layers put text into it, and why every instruction raises a probability without guaranteeing anything are in B1 (§1, §6). Which model and effort each task gets is B2's routing table. This unit assumes both.

## 1 · The four parts of a brief that survives

A brief survives when someone with no context can act on it without coming back with a question. Anthropic's prompting guide states the test in those terms. It asks the user to think of Claude as "a brilliant but new employee who lacks context on your norms and workflows", and gives a check to run before sending: "Show your prompt to a colleague with minimal context on the task and ask them to follow it. If they'd be confused, Claude will be too." ([Anthropic, *Prompting best practices*](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices); vendor guidance). Between them, the three vendors' guides read for this unit cover all four parts below, each in its own words and with its own emphasis; none of them presents the four as a set.

### Who the reader is

Two different things travel under the word "role". One is a persona given to the model ("You are an expert editor"). Anthropic says a role set in the system prompt "focuses Claude's behavior and tone for your use case" and that a single sentence makes a difference (same page; vendor guidance). Measured on accuracy, personas did nothing: Zheng and colleagues gave four families of models 162 roles across 2,410 factual questions and found that a persona in the system prompt did not improve performance against a control with none; choosing the best persona per question helped, but picking it automatically did little better than chance ([Zheng et al., Findings of EMNLP 2024](https://aclanthology.org/2024.findings-emnlp.888/)). The two sources measured different things, tone and factual accuracy, so they do not contradict each other. Together they place a persona's documented effect in register. Neither shows it making answers more correct.

The other meaning is the reader of the output: who will read it, what they already know, and what they will do with it. Anthropic's blog lists "Explaining the purpose or audience for the output" among the cases where context improves results ([Claude blog, *Best practices for prompt engineering for 2026*, 10 Nov 2025](https://claude.com/blog/best-practices-for-prompt-engineering); vendor guidance). OpenAI's help-centre article asks the user to "Be specific, descriptive and as detailed as possible about the desired context, outcome, length, format, style, etc" ([OpenAI Help Center, *Best practices for prompt engineering with the OpenAI API*](https://help.openai.com/en/articles/6654000); vendor guidance). Anthropic gives the mechanism: an instruction that carries its reason lets the model apply the reason to cases the instruction did not name. Its example replaces "NEVER use ellipses" with the reason (the output will be read by a text-to-speech engine that cannot pronounce them) and adds that "Claude can generalize from the explanation" ([Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)). A reader line is that kind of reason, given once for the whole output. His course briefs already carry one: every Brand + AI brief has a Reader line drawn from `reader.md` (`method.md` §4, Brief template).

### What the output is

The second part names the artefact, its form and where it will live. Anthropic: "Be specific about the output format and constraints you want" ([Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)). OpenAI: "Articulate the desired output format through examples" ([OpenAI Help Center](https://help.openai.com/en/articles/6654000)). §3 turns this part into a contract.

### Constraints

Constraints are the rules the output must satisfy: what it must contain, what it must leave out, its tone and its limits. Two pieces of vendor guidance shape how they are written.

**State the positive.** Anthropic: "Tell Claude what to do instead of what not to do", replacing "Do not use markdown in your response" with "Your response should be composed of smoothly flowing prose paragraphs." ([Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)). OpenAI says the same: "Instead of just saying what not to do, say what to do instead" ([OpenAI Help Center](https://help.openai.com/en/articles/6654000)).

**When a prohibition is needed, name the pattern.** Anthropic's guide to Opus 5.5 says that a general instruction such as "avoid a generic AI look" "mostly swaps one default for another", and that the model "responds well to instructions that name specific patterns to avoid" ([Anthropic, *Prompting Claude Opus 5.5*](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5-5); vendor guidance, written about frontend design). Applying it to prose ("no 'I hope this finds you well'" in place of "avoid corporate tone") is my extension.

Older research gives a reason to be wary of bare negatives. Jang, Ye and Seo found that on tasks phrased with negation, language models performed worse as they grew larger, the reverse of the usual scaling trend ([Jang et al., Transfer Learning for NLP Workshop, PMLR 203, 2023](https://proceedings.mlr.press/v203/jang23a.html)). The paper was first posted in September 2022 and tested models of that period; it says nothing measured about current Claude models. It supports one habit only: pair every "do not" with the "do" that replaces it.

### Examples, including negative ones

The vendors agree that examples help and disagree on how many.

- Anthropic's documentation: "Include 3–5 examples for best results", each relevant, diverse and wrapped in `<example>` tags so the model can tell them from instructions ([Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)).
- Anthropic's blog: "Start with one example (one-shot)", adding more only if the output still misses ([Claude blog, 10 Nov 2025](https://claude.com/blog/best-practices-for-prompt-engineering)).
- Google: "We recommend to always include few-shot examples in your prompts", with two warnings: "if you include too many examples, the model may start to overfit the response to the examples", and the examples should share one structure and format ([Google, *Prompt design strategies*, updated 13 Oct 2026](https://ai.google.dev/gemini-api/docs/prompting-strategies)).
- Anthropic's engineering team warns against stuffing "a laundry list of edge cases" into a prompt and recommends instead to "curate a set of diverse, canonical examples" ([Anthropic, *Effective context engineering for AI agents*, 29 Sep 2025](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)).

All four are vendor guidance. The range runs from one example to five, and the deciding variable in all of them is whether the output matches.

Research says what examples teach. Min and colleagues found that randomly replacing the labels in demonstrations "barely hurts performance" on classification and multiple-choice tasks, consistently over 12 models including GPT-3; what drove the effect was the label space, the distribution of the input text and the format of the sequence ([Min et al., EMNLP 2022](https://aclanthology.org/2022.emnlp-main.759/)). On those tasks a demonstration worked mainly by showing the shape of an answer. My reading for his use: choose an example for its shape (length, structure, register), and expect the shape to be copied, which is Google's overfitting warning seen from the other side.

Negative examples have thin evidence. None of the vendor pages read for this unit advises putting a labelled bad example into a prompt. Anthropic's Fable 5.1 guide recommends the positive form with a reason attached: add "one complete example of a correct response" with "a sentence explaining why the response is correct" ([Anthropic, *Prompting Claude Fable 5.1*](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-1); vendor guidance, written about quoting retrieved sources). One preprint tested the negative form directly: contrastive chain-of-thought gave models valid and invalid reasoning demonstrations side by side and reported gains on reasoning benchmarks; the abstract gives no figure and no venue was found ([Chia et al., arXiv 2311.09277, 2023](https://arxiv.org/abs/2311.09277); preprint). The rule the library follows is my synthesis of these: a bad example appears only beside a good one, labelled as wrong, with the specific pattern named and the reason it fails.

## 2 · Why specificity beats length

Length is a cost, and specificity is what the cost buys. Anthropic's blog lists among common mistakes: "Longer, more complex prompts are NOT always better." ([Claude blog, 10 Nov 2025](https://claude.com/blog/best-practices-for-prompt-engineering)). Its engineering team frames the goal as "finding the smallest possible set of high-signal tokens" and adds that "minimal does not necessarily mean short" ([Effective context engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)). The same post describes two ways to miss: engineers "hardcoding complex, brittle logic" at one extreme, "vague, high-level guidance" at the other (same post). All vendor guidance.

**Why extra text costs.** B1 §2 sets out the attention budget and the evidence that recall falls as the window fills. Three studies bear on prompts specifically:

- Levy, Jacoby and Goldberg padded the same reasoning questions with extra text of different lengths, types and positions; reasoning performance degraded "at much shorter input lengths than their technical maximum", in every version of their dataset ([Levy et al., ACL 2024](https://aclanthology.org/2024.acl-long.818/)).
- Shi and colleagues built GSM-IC, school arithmetic problems with irrelevant sentences added, and found that performance "is dramatically decreased when irrelevant information is included"; telling the model to ignore irrelevant information was one of the mitigations that helped ([Shi et al., ICML 2023](https://icml.cc/virtual/2023/poster/24255); [arXiv 2302.00093](https://arxiv.org/abs/2302.00093)).
- Jaroslawicz and colleagues gave 20 models from seven providers up to 500 keyword-inclusion instructions in one report-writing task; the best frontier models reached 68% accuracy at 500, and models showed a bias towards earlier instructions ([Jaroslawicz et al., arXiv 2507.11538, 2025](https://arxiv.org/abs/2507.11538); a workshop poster at [NeurIPS 2025](https://neurips.cc/virtual/2025/122417), not the main track).

These tested models of 2022 to 2025 on tasks unlike his. The direction is the same in all three: material that does not serve the task competes with material that does.

**What specificity means.** Claude Code's documentation gives the working definition: write instructions "concrete enough to verify", such as "Use 2-space indentation" instead of "Format code properly", and it states that the more specific and concise the instructions, the more consistently Claude follows them ([Claude Code docs, *Memory*](https://code.claude.com/docs/en/memory); vendor guidance, written for `CLAUDE.md` files). Anthropic's evaluation guide applies the same test to success criteria: "Instead of 'good performance,' specify 'accurate sentiment classification.'" ([Anthropic, *Define success criteria and build evaluations*](https://platform.claude.com/docs/en/test-and-evaluate/develop-tests)). A specific instruction is one the output can be checked against. It can be short. "Keep it concise" cannot be checked; "up to three reasons of twelve words or fewer", the decision format in his saved preferences, can.

**Where sources disagree.** OpenAI's API guide says that "reasoning models will provide better results on tasks with only high-level guidance", and that this "differs from GPT models, which benefit from precise instructions" ([OpenAI, *Prompt engineering*](https://developers.openai.com/api/docs/guides/prompt-engineering)). Anthropic's general guide points the other way: "The more precisely you explain what you want, the better the result." ([Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)). Anthropic's Opus 5.5 guide, though, agrees with OpenAI on one point: in chat applications, instructions telling the model to think carefully before answering can be removed, because the model sets its own amount of thinking and effort is the main control ([Prompting Claude Opus 5.5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5-5)). Opus 5.5 and Fable 5.1 think adaptively, always on (B2 §7), which makes them reasoning models in OpenAI's sense; that mapping is mine. My reconciliation: be exact about the output (what it is, who reads it, when it is done), which every source endorses, and leave the route to the model, which is where the reasoning-model guidance points. The templates follow that split: they specify artefacts and checks, and none of them scripts the model's reasoning.

## 3 · Output contracts

An output contract is the part of a brief that says what will be handed back. It has three clauses.

**Format.** Anthropic's guide gives three levers: say what to do; use XML tags as format indicators; and match the prompt's own style to the output wanted, since "removing markdown from your prompt can reduce the volume of markdown in the output" ([Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices); vendor guidance). A format clause names the container as well as the layout: a Markdown file in the vault, a message ready to paste, a table in the chat. §4 shows why the container matters in his setup.

**Length rule.** Length targets hold for short outputs and fail for long ones. LIFEBench tested 26 widely used models on length instructions from 16 to 8,192 words in English and Chinese and found that "most models reasonably follow short-length instructions but deteriorate sharply beyond a certain threshold"; the preprint adds that almost all fell short of the maximum output lengths their vendors claim ([Zhang et al., NeurIPS 2025 Datasets and Benchmarks Track](https://proceedings.neurips.cc/paper_files/paper/2025/hash/c84f00ccee3d35cee1901acb0e258dc7-Abstract-Datasets_and_Benchmarks_Track.html); [arXiv 2505.16234](https://arxiv.org/abs/2505.16234)). Anthropic adds that its latest models are less verbose and "Might skip detailed summaries for efficiency unless prompted otherwise" ([Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)). So a word limit is a usable contract for a caption, a message or an email. For a long piece the contract that holds is structural: one section per item of the brief, each answered, none padded. His method already says this, in its own words: the topic decides, never pad, never cut substance (`method.md` §4, Length rule). The structural form is my synthesis of the method and the LIFEBench result.

**What done looks like.** Anthropic's prompt-engineering overview assumes three things before any prompting starts: "A clear definition of the success criteria for your use case", "Some ways to empirically test against those criteria", and a first draft ([Anthropic, *Prompt engineering overview*](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview)). For unattended agents, the Opus 5.5 guide offers the option of stating "the completion condition up front" ([Prompting Claude Opus 5.5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5-5)); the Fable 5.1 guide's suggested system prompt says the request sets the scope and "the scope is the deliverable: don't quietly narrow, widen, or swap it" ([Prompting Claude Fable 5.1](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-1)). All vendor guidance, written for API and agent use; carrying it into chat is my inference. In the library, each template ends with a DONE WHEN list: checks he, or Fable, can run on the output line by line.

One more clause belongs in any contract that touches facts. Anthropic's hallucination guide recommends giving the model explicit permission to say it does not know, asking it to cite a quote or source for each claim, and having it retract any claim it cannot support with a quote ([Anthropic, *Reduce hallucinations*](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations); vendor guidance, no figure given). His method already works this way: every unit hands in an unsure list and a Sources list (B1, filed before the rule was enforced, has none), so unverified claims have a sanctioned place to go, and the checker starts from that list (`method.md` §4, Before handing in).

## 4 · Why his preferences file works, and why one-line asks sometimes do not

### The preferences file

His saved preferences are account-wide; Anthropic's help centre says instructions saved there are "applied to all of your conversations with Claude" ([Claude Help Center, *Understanding Claude's personalization features*](https://support.claude.com/en/articles/10185728)). B1 §6 places them in the window: text present in every chat, with no documented order of precedence against project instructions. Four features of his file match the guidance in §1 to §3 (the Learning Project's setup as of 28 October 2026):

1. **It is always there.** It does not depend on memory writing it down or on retrieval finding it (B1 §3).
2. **Its strongest rules can be checked.** Decisions come as a single pick, up to three reasons of twelve words or fewer, and one override line; one question per response, and only when blocked. Each can be verified against the output, which is the Claude Code standard of "concrete enough to verify" ([Claude Code docs, *Memory*](https://code.claude.com/docs/en/memory)), and each sets a short length, the range LIFEBench found models follow ([Zhang et al., NeurIPS 2025](https://proceedings.neurips.cc/paper_files/paper/2025/hash/c84f00ccee3d35cee1901acb0e258dc7-Abstract-Datasets_and_Benchmarks_Track.html)).
3. **Its prohibitions name patterns.** It bans specific openers and praise for ordinary work, by example, which is the form the Opus 5.5 guide says works ([Prompting Claude Opus 5.5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5-5)).
4. **Some rules carry their reason.** The format rule says outputs are mobile-first because he reads on a phone, so the model can apply the reason to cases the rule does not list ([Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices), the ellipsis example).

Its weak lines are the ones that cannot be checked: "concise", or sarcasm "when earned", leave the judgement to the model. And it cannot carry the task. No standing file knows who will read today's output, what it is or when it is done.

It also contains one live conflict. The preferences send anything with three or more sections to a dark-theme HTML artifact. A course unit has many sections and must be a Markdown file in the vault (`method.md` §7), and the Project instructions name its `.md` path. Claude Code's documentation states that when two instructions contradict each other, "Claude may pick one arbitrarily" ([Claude Code docs, *Memory*](https://code.claude.com/docs/en/memory)); it is written about `CLAUDE.md` files, and applying it to claude.ai is my analogy, since the help centre states no precedence at all (B1 §6). Until the layers are reconciled, which is B4's job, every template whose output collides with a preference says so in its OUTPUT line.

### One-line asks

A one-line ask still arrives in a window holding his preferences and Project instructions. What it lacks is the task's own three parts: the reader, the output and the definition of done. Three documented mechanisms explain what happens next.

- **The model takes the verb literally.** Anthropic: "If you say 'can you suggest some changes,' Claude will sometimes provide suggestions rather than implementing them, even if making changes might be what you intended." ([Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices); vendor guidance). The Sonnet 5.5 guide gives the reverse case: an open-ended request "can start building a presentation, report, or video when you only wanted ideas" ([Anthropic, *Prompting Claude Sonnet 5.5*](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-sonnet-5-5)).
- **Gaps get filled with defaults.** The Opus 5.5 guide says the model "tends to get to work quickly", and that on loosely specified tasks it helps to tell it to look through the relevant sources before acting ([Prompting Claude Opus 5.5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5-5); written about multi-app workflows).
- **A brief that arrives in pieces does worse than one complete brief.** Laban and colleagues compared the same tasks given fully specified in a single turn against a simulated conversation in which the same instruction arrives in pieces, one per turn, with no corrections from the user. Across more than 200,000 simulated conversations, every top open- and closed-weight model they tested did worse in the multi-turn setting, "an average drop of 39% across six generation tasks"; the models "make assumptions in early turns and prematurely attempt to generate final solutions, on which they overly rely", and when they take a wrong turn "they get lost and do not recover" ([Laban et al., ICLR 2026](https://iclr.cc/virtual/2026/oral/10009147); [arXiv 2505.06120](https://arxiv.org/abs/2505.06120)). The paper (posted May 2025) tested 15 models, Claude 3.7 Sonnet, GPT-4.1, o3 and Gemini 2.5 Pro among them; none is a current model.

The practical rule from the third finding, which the paper itself gives its users (§7.4: consolidate the requirements into one instruction and start a new conversation): when a first answer misses, rewrite the brief with what the miss revealed and start a new chat, instead of correcting in place. His method's one-chat-per-unit rule (`method.md` §4) applies the same logic at the scale of a course.

A one-liner is enough when the input fully determines the output and the standing layers already carry tone and format: reformatting, triage, a single lookup. B2 §6 and §8 give the evidence that these are the tasks where model differences stop mattering; that the same tasks tolerate a short prompt is my reading.

```viz
{
  "kind": "decision",
  "caption": "When a one-line ask is enough, as §4 states it: both conditions must hold; otherwise the ask needs the task's own three parts. The rule is this unit's own reading (§4), resting on B2 §6 and §8 for the tasks where model differences stop mattering.",
  "root": {
    "q": "Input fully determines the output?",
    "tone": 4,
    "branches": [
      {
        "label": "no",
        "to": {
          "outcome": "Give the reader, the output and done",
          "tone": 1
        }
      },
      {
        "label": "yes",
        "to": {
          "q": "Standing layers carry tone and format?",
          "tone": 4,
          "branches": [
            {
              "label": "no",
              "to": {
                "outcome": "Give the reader, the output and done",
                "tone": 1
              }
            },
            {
              "label": "yes",
              "to": {
                "outcome": "A one-liner is enough",
                "tone": 2
              }
            }
          ]
        }
      }
    ]
  }
}
```

## 5 · Common failure patterns

### Asking for a plan when he wants the thing

The verb of the request sets the artefact (§4, first mechanism). "How should I structure the episode?" asks for advice; "Write the script" asks for the script. His preferences push the model towards acting (no menus, deliver first), but they cannot overturn a request that literally asks for options. Anthropic's guide adds the other half: "If you want Claude to do more than the task strictly requires, explicitly request it rather than relying on the model to infer this from vague prompts." ([Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)). Fix: the first line of every template is a TASK line that opens with the verb of the artefact and names it.

### Burying the ask

The ask is buried when it sits in the middle of a message, after background and before pasted material. Sources disagree on where it belongs.

- OpenAI's help article: "Put instructions at the beginning of the prompt and use ### or """ to separate the instruction and context" ([OpenAI Help Center](https://help.openai.com/en/articles/6654000)).
- Anthropic, for inputs of 20,000 tokens or more: place long documents at the top and the query at the end; "Queries at the end can improve response quality by up to 30 percent in tests, especially with complex, multidocument inputs." ([Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)). That figure is vendor data; the page publishes no method, task set or model list behind it.
- OpenAI's API guide: context is "usually best positioned near the end of your prompt" ([OpenAI, *Prompt engineering*](https://developers.openai.com/api/docs/guides/prompt-engineering)).

The research agrees on one point only: the middle is the weak position. Liu and colleagues found recall worst in the middle of long inputs (B1 §2), and IFScale found a bias towards earlier instructions ([Jaroslawicz et al., 2025](https://arxiv.org/abs/2507.11538)). The library's layout is my synthesis: a one-line TASK first, material inside tags, and, when the material is long, the TASK repeated as the last line.

```viz
{
  "kind": "matrix",
  "caption": "What each source places at the beginning, middle or end of a prompt, as §5 reports it: <a href=\"https://help.openai.com/en/articles/6654000\">OpenAI Help Center, <em>Best practices for prompt engineering with the OpenAI API</em></a>; <a href=\"https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices\">Anthropic, <em>Prompting best practices</em></a> (inputs of 20,000 tokens or more); <a href=\"https://developers.openai.com/api/docs/guides/prompt-engineering\">OpenAI, <em>Prompt engineering</em></a>; Liu and colleagues via B1 §2. The library row is this unit's own synthesis (§5); its closing TASK is added only when the material is long.",
  "cols": [
    "Beginning",
    "Middle",
    "End"
  ],
  "rows": [
    {
      "label": "OpenAI Help Center",
      "tone": 3,
      "cells": [
        "instructions",
        null,
        null
      ]
    },
    {
      "label": "Anthropic, 20,000+ tokens",
      "tone": 3,
      "cells": [
        "long documents",
        null,
        "query"
      ]
    },
    {
      "label": "OpenAI API guide",
      "tone": 3,
      "cells": [
        null,
        null,
        "context"
      ]
    },
    {
      "label": "Liu et al. (B1 §2)",
      "tone": 5,
      "cells": [
        null,
        {
          "mark": "recall worst",
          "tone": 1
        },
        null
      ]
    },
    {
      "label": "The library",
      "tone": 2,
      "cells": [
        "TASK",
        "material in tags",
        "TASK again"
      ]
    }
  ]
}
```

### Stacking unrelated tasks

"Write the email, fix the calendar, and draft three captions" is three tasks in one window. Google: "Instead of having many instructions in one prompt, create one prompt per instruction", and for multi-step work, "make each step a prompt" ([Google, *Prompt design strategies*](https://ai.google.dev/gemini-api/docs/prompting-strategies); vendor guidance). Anthropic says explicit chaining stays useful "when you need to inspect intermediate outputs or enforce a specific pipeline structure" ([Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)). Three findings above explain the cost: each task's material is irrelevant context for the others (Shi et al.), instruction count degrades adherence (IFScale), and a long mixed window degrades reasoning (Levy et al.). B2 adds a fourth from his own routing table: the three tasks want different models and efforts, and one chat runs them all on one. Fix: one artefact per prompt. Where tasks form a pipeline (journal synthesis, then script, then titles, then email), each step is its own prompt and its output is read before it feeds the next; B5 and B7 build that chain.

## Deliverable · Prompt library

Ten templates for his recurring tasks, as of 28 October 2026. Each is usable on its own.

**How the templates are built.** Every template has the same parts in the same order, each traced to the unit: **TASK** (one line, the artefact's verb: §5), **READER** (§1), **OUTPUT** (the contract: §3), **CONSTRAINTS** (positive first, prohibitions as named patterns: §1), **EXAMPLES** (good, and bad only beside good, labelled with why: §1), **MATERIAL** (pasted inside tags: §5), **DONE WHEN** (checks on the output: §3), and **TASK again** as the last line when the material is long (§5).

```viz
{
  "kind": "flow",
  "caption": "The parts of every template in the prompt library, in order, each with the section of this unit it is traced to. From the Deliverable's \"How the templates are built\"; the unit's own synthesis.",
  "steps": [
    {
      "label": "TASK",
      "note": "the artefact's verb · §5"
    },
    {
      "label": "READER",
      "note": "§1"
    },
    {
      "label": "OUTPUT",
      "note": "the contract · §3"
    },
    {
      "label": "CONSTRAINTS",
      "note": "positive first · §1"
    },
    {
      "label": "EXAMPLES",
      "note": "bad only beside good · §1"
    },
    {
      "label": "MATERIAL",
      "note": "inside tags · §5"
    },
    {
      "label": "DONE WHEN",
      "note": "checks on the output · §3"
    },
    {
      "label": "TASK again",
      "note": "when the material is long · §5"
    }
  ]
}
```

**Conventions.**

- `<FILL: …>` is a slot filled every time the template is used.
- `<UNKNOWN: …>` in a worked example marks a real value this unit does not have. Replace it before sending; never let the model guess it.
- Tags such as `<takes>` and `</takes>` wrap pasted material, so instructions and material cannot be confused ([Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)).
- The **Model** line comes from B2's routing table; where B2 has no row, the line says so and the pick is my analogy.
- One template per chat. If the first output misses, change the brief and open a new chat (§4).
- The patterns in each avoid-list are starting choices of mine. Extend them from the first outputs, as Anthropic's Opus 5.5 guide advises for named patterns: "check which styles the first result used instead, and extend the list if needed" ([Prompting Claude Opus 5.5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5-5)).
- Private details stay generic in the templates; they go in only at the moment of use.

### 1 · Course unit

**Use when:** starting a Brand + AI unit chat. The `write-unit` skill holds the procedure; this is the opening message that hands it the job. **Model:** Opus 5.5, high (B2, Course units).

    TASK: Write unit <FILL: code> · <FILL: title> of the Learning Project in full, with its deliverable, in this chat.

    READER: Pedro, as docs/reader.md describes him. He reads on his phone, in order, and checks every citation.

    BRIEF (verbatim; never reword it):
    <brief>
    <FILL: the full text of generator/data/brand-ai/briefs/<code>-brief.txt, pasted unchanged>
    </brief>

    READ FIRST, IN FULL: skills/write-unit/SKILL.md; docs/method.md; docs/sourcing-standard.md (Part 1 and Part 2); docs/reader.md; the Brand + AI section of docs/courses-index.md; <FILL: the filed units this one points back to>.

    OUTPUT: one Markdown file, <FILL: code>-<FILL: slug>.md, starting with the front matter in method.md §7 (model: the model you actually are; search: <FILL: on | off>). Then "# <code> · <title>", then numbered sections answering the brief's items in the brief's order, then "## Deliverable · <name>" built in full, then "## Writer's unsure list" (up to ten numbered claims you could not verify), then "## Sources" (every link cited in the text, and nothing else). This is a file. Do not make an HTML artifact; this overrides the artifact rule in my preferences.

    CONSTRAINTS:
    - Search <FILL: on: search first and date every fact that can change | off: search only to verify a specific date, figure or contested point, and to find the real URL of every source you cite>.
    - Cite every number, mechanism and recommendation where it is made, with a link. Label vendor guidance, vendor data, correlational data and anecdote as such. Every number says whose it is.
    - A claim you cannot source is called unsourced or left out, and never enters the deliverable.
    - Quotation marks hold the source's exact words.
    - A pointer to another unit says what that unit actually says; open it first.
    - British spelling. Where an em dash would go, use a colon, comma or semicolon. State things directly; no "not X but Y" sentences. Start with the first section; end with Sources.
    - Nothing private: a private detail is described generically.

    DONE WHEN:
    - every item in the brief has its own section, in order;
    - the deliverable is complete and usable without reading the unit;
    - every link in the text is in Sources and every Sources entry is cited;
    - the unsure list exists and has at most ten items.

    TASK (again): write unit <FILL: code> in full now.

**Worked example · B4, the next unit in the build order** (`courses-index.md`):

    TASK: Write unit B4 · Context engineering of the Learning Project in full, with its deliverable, in this chat.

    READER: Pedro, as docs/reader.md describes him. He reads on his phone, in order, and checks every citation.

    BRIEF (verbatim; never reword it):
    <brief>
    <the full text of generator/data/brand-ai/briefs/B4-brief.txt, pasted unchanged: the course preamble, then "Unit B4, Context engineering. Cover: …">
    </brief>

    READ FIRST, IN FULL: skills/write-unit/SKILL.md; docs/method.md; docs/sourcing-standard.md (Part 1 and Part 2); docs/reader.md; the Brand + AI section of docs/courses-index.md; courses/brand-ai/B1-mental-model.md; courses/brand-ai/B2-choosing-the-model.md; courses/brand-ai/B3-prompting-that-holds-up.md; docs/project-instructions.md and the Project's file list as it stands today (the deliverable audits them).

    OUTPUT: one Markdown file, B4-context-engineering.md, starting with the front matter in method.md §7 (model: the model you actually are; search: off). Then "# B4 · Context engineering", then numbered sections answering the brief's items in the brief's order, then "## Deliverable · Project-structure audit" built in full, then "## Writer's unsure list" (up to ten numbered claims you could not verify), then "## Sources" (every link cited in the text, and nothing else). This is a file. Do not make an HTML artifact; this overrides the artifact rule in my preferences.

    CONSTRAINTS:
    - Search off: search only to verify a specific date, figure or contested point, and to find the real URL of every source you cite.
    - Cite every number, mechanism and recommendation where it is made, with a link. Label vendor guidance, vendor data, correlational data and anecdote as such. Every number says whose it is.
    - A claim you cannot source is called unsourced or left out, and never enters the deliverable.
    - Quotation marks hold the source's exact words.
    - A pointer to another unit says what that unit actually says; open it first. B1 §6 names the tone rules duplicated between my preferences and the Project instructions; B3 §4 names a conflict between them (the HTML-artifact rule); B4 owns the fix for both.
    - British spelling. Where an em dash would go, use a colon, comma or semicolon. State things directly; no "not X but Y" sentences. Start with the first section; end with Sources.
    - Nothing private: a private detail is described generically.

    DONE WHEN:
    - every item in the brief has its own section, in order;
    - the audit lists each layer of the Project with what it holds now and what it should hold;
    - the fix list is ranked by effort, each fix with the file it changes;
    - every link in the text is in Sources and every Sources entry is cited;
    - the unsure list exists and has at most ten items.

    TASK (again): write unit B4 in full now.

### 2 · Fable audit

**Use when:** a fresh check, a four-unit stratified-sample audit or a staleness check is due. The audit prompts in `method.md` §6 and in the `audit-units` skill §3b are used verbatim; this template is the frame around them. **Model:** Fable 5.1, high (B2, Audits).

    TASK: Run <FILL: the stratified-sample audit of units … | the fresh check of unit … | the staleness check of unit …>. Report; do not edit any unit.

    READER: Pedro, who applies each finding as an exact text replacement. A finding he cannot apply without checking it again himself is a failed finding.

    MODEL CHECK: you must be Fable 5.1. If you are not, say so in your first line and stop.

    READ FIRST: skills/audit-units/SKILL.md; docs/method.md §5 and §6; docs/sourcing-standard.md Part 1 and Part 2; <FILL: the units, from their vault paths>; each unit's writer's unsure list; <FILL: earlier audit or fresh-check reports the prompt names>.

    THE AUDIT PROMPT (verbatim; only its {placeholders} filled):
    <audit_prompt>
    <FILL: the prompt from method.md §6 or audit-units §3b>
    </audit_prompt>

    OUTPUT: exactly the output the audit prompt specifies, as Markdown in this chat. Do not make an HTML artifact.

    CONSTRAINTS:
    - Open every source before you give it a verdict. A source you cannot open is "unverifiable", never FAIL.
    - Every correction quotes the current text exactly (it must occur once in the unit), gives the replacement text, and gives the source URL.
    - Start each unit from its unsure list.
    - No praise and no summary of the units.

    DONE WHEN:
    - every sampled claim has a verdict and a source;
    - the decision rule (more than one FAIL in ten sampled claims means a full audit) has been applied to each unit;
    - the last lines give one verdict per unit.

**Worked example · Audit 2** (due after B3 and B4; B2 and A1 are already counted: `courses-index.md`, Audit counters):

    TASK: Run the stratified-sample audit of units B2, B3, B4 and A1. Report; do not edit any unit.

    READER: Pedro, who applies each finding as an exact text replacement. A finding he cannot apply without checking it again himself is a failed finding.

    MODEL CHECK: you must be Fable 5.1. If you are not, say so in your first line and stop.

    READ FIRST: skills/audit-units/SKILL.md; docs/method.md §5 and §6; docs/sourcing-standard.md Part 1 and Part 2; courses/brand-ai/B2-choosing-the-model.md; courses/brand-ai/B3-prompting-that-holds-up.md; courses/brand-ai/B4-context-engineering.md; courses/brand-ai/A1-positioning-the-journey-as-a-format.md; each unit's writer's unsure list; audits/brand-ai/fresh-check-B2.md, fresh-check-B3.md, fresh-check-B4.md and fresh-check-A1.md (B2's and A1's exist; B3's and B4's once those units are filed).

    THE AUDIT PROMPT (verbatim; only its {placeholders} filled):
    <audit_prompt>
    You are auditing four units of a self-study course written by Opus 5.5 for one reader. Units: B2 (courses/brand-ai/B2-choosing-the-model.md), B3 (courses/brand-ai/B3-prompting-that-holds-up.md), B4 (courses/brand-ai/B4-context-engineering.md), A1 (courses/brand-ai/A1-positioning-the-journey-as-a-format.md).

    Method, in this order:
    1. For each unit, list its sections. From every section draw one claim that carries a number, a named source, a mechanism or a recommendation. That is the sample; record it before checking anything.
    2. Check each sampled claim against the source the unit cites: open the source; confirm the figure, the date, the sample size and that the claim is what the source says, not a stretch of it. Mark each claim PASS, FAIL (wrong, unsupported, miscited, or invented) or STALE (true when written, superseded now, with the newer figure).
    3. For each unit compute the failure rate. If more than one claim in ten is FAIL, audit that unit in full: every cited claim, same procedure.
    4. Check the deliverable: it exists in full inside the unit, it follows from the unit's evidence, and it is usable without reading the unit.
    5. Check against the course goal and sourcing standard (in the unit's preamble): does the unit move the reader toward the stated outcomes, and is anything in it advice without evidence?

    Output: a table per unit (section, claim, source, verdict, note); the failure rate; a verdict per unit (PASS / FULL AUDIT RUN, result / REWRITE with the sections named); the three most consequential errors across the four units in plain language; and one line each for the bibliography (new sources to add, sources to mark failed) and the changelog. Do not fix the units; report.
    </audit_prompt>

    OUTPUT: exactly the output the audit prompt specifies, as Markdown in this chat. Do not make an HTML artifact.

    CONSTRAINTS:
    - Open every source before you give it a verdict. A source you cannot open is "unverifiable", never FAIL.
    - Every correction quotes the current text exactly (it must occur once in the unit), gives the replacement text, and gives the source URL.
    - Start each unit from its unsure list.
    - No praise and no summary of the units.

    DONE WHEN:
    - every sampled claim has a verdict and a source;
    - the decision rule (more than one FAIL in ten sampled claims means a full audit) has been applied to each unit;
    - the last lines give one verdict per unit.

### 3 · Journal synthesis

**Use when:** turning several weeks of journal entries or voice-note transcripts into one dated record, before scripting or writing the weekly email. **Model:** Opus 5.5, medium (B2, Journal entries, override for synthesis across several weeks).

    TASK: Write one dated record that synthesises my journal entries from <FILL: start date> to <FILL: end date>.

    READER: me, later, deciding what to keep doing; and the record a script or an email will be cut from. I need to find what happened, in my own words, with dates.

    OUTPUT: Markdown in this chat, in five sections:
    1. What happened: dated bullets, oldest first, one line each.
    2. What I said at the time: exact quotations from the entries, each with its date.
    3. What went wrong: every failure or setback the entries record.
    4. What changed between the first entry and the last.
    5. Open questions: what the entries raise and do not settle.

    CONSTRAINTS:
    - Use only the entries below. If it is not in them, it is not in the record.
    - Quote my sentences word for word. Mark any sentence you wrote with [C].
    - Keep every failure at the weight the entries give it. Add no lesson to it.
    - Where two entries disagree, give both, with their dates.
    - Leave out: <FILL: topics that stay out of this record>.

    EXAMPLE (shape of one bullet in section 1):
    <example>
    - <date> · <what happened, one line> · "<my sentence from that day's entry>"
    </example>

    BAD EXAMPLE (never write this):
    <bad_example>
    This was a period of real growth, and the setbacks taught valuable lessons.
    Why it is wrong: it summarises a feeling, adds a lesson no entry states, and quotes nothing.
    </bad_example>

    MATERIAL:
    <entries>
    <FILL: the entries, each with its date>
    </entries>

    DONE WHEN:
    - every bullet has a date;
    - every quotation appears word for word in the entries;
    - every failure the entries record is in section 3;
    - nothing appears that the entries do not contain, except lines marked [C].

    TASK (again): write the dated record from the entries above.

**Worked example · the competition season that ended at the WIKF Global Cup (October 2026):**

    TASK: Write one dated record that synthesises my journal entries from <UNKNOWN: date of the first entry of the 2026 competition season> to the WIKF Global Cup in October 2026.

    READER: me, later, deciding what to carry from competitive karate into the half-marathon season; and the record the retrospective episode and its weekly email will be cut from. I need to find what happened, in my own words, with dates.

    OUTPUT: Markdown in this chat, in five sections:
    1. What happened: dated bullets, oldest first, one line each.
    2. What I said at the time: exact quotations from the entries, each with its date.
    3. What went wrong: every failure or setback the entries record.
    4. What changed between the first entry and the last.
    5. Open questions: what the entries raise and do not settle.

    CONSTRAINTS:
    - Use only the entries below. If it is not in them, it is not in the record.
    - Quote my sentences word for word. Mark any sentence you wrote with [C].
    - Keep every failure at the weight the entries give it. Add no lesson to it.
    - Where two entries disagree, give both, with their dates.
    - Leave out: anything about other people beyond their role in a session or a bout.

    EXAMPLE (shape of one bullet in section 1):
    <example>
    - <date> · <what happened, one line> · "<my sentence from that day's entry>"
    </example>

    BAD EXAMPLE (never write this):
    <bad_example>
    This was a period of real growth, and the setbacks taught valuable lessons.
    Why it is wrong: it summarises a feeling, adds a lesson no entry states, and quotes nothing.
    </bad_example>

    MATERIAL:
    <entries>
    <UNKNOWN: the season's journal entries and voice-note transcripts, each with its date>
    </entries>

    DONE WHEN:
    - every bullet has a date;
    - every quotation appears word for word in the entries;
    - every failure the entries record is in section 3;
    - nothing appears that the entries do not contain, except lines marked [C].

    TASK (again): write the dated record from the entries above.

### 4 · YouTube script from dictated takes

**Use when:** two or more dictated takes exist for an episode and the script has to be cut from them. **Model:** Opus 5.5, medium (B2, Video scripts, "original, with no unit behind it").

    TASK: Cut a script for one long-form episode, <FILL: working title>, from the dictated takes below.

    READER: a viewer who has never heard of me and arrives through <FILL: search: they typed a problem | browse or suggested: they saw the thumbnail>. They decide in the first 30 seconds whether the title was true.

    OUTPUT: Markdown in this chat:
    1. Hook (first 30 seconds): the lines that make the title true.
    2. Chapters: for each, a one-line purpose, then its lines in order.
    3. Ending: the last line, taken from the takes.
    4. Gaps: anything the episode needs that the takes do not contain (a line I must record, a shot I must film, a claim that needs a source before it goes on camera).
    Mark every line with its origin: [T1], [T2] (take number, with the timestamp if the transcript has one) or [NEW] for any line you wrote.
    Target runtime: <FILL: minutes>.

    CONSTRAINTS:
    - Use my sentences from the takes. Reorder and cut freely; rewrite none.
    - A [NEW] line is one sentence at most and bridges two take lines; I rewrite every one.
    - Keep the doubts and failures the takes contain.
    - Avoid: jokes you invented; a closing line about believing in yourself; asking viewers to subscribe; any claim of fact not in the takes.

    EXAMPLE (shape of one chapter):
    <example>
    Chapter 2 · <purpose in one line>
    [T1 03:12] "<my sentence>"
    [T2 00:45] "<my sentence>"
    [NEW] <one bridging sentence>
    </example>

    MATERIAL:
    <take_1>
    <FILL: transcript of take 1>
    </take_1>
    <take_2>
    <FILL: transcript of take 2>
    </take_2>

    DONE WHEN:
    - every line carries an origin mark;
    - the hook makes the working title true within 30 seconds of speech;
    - no [NEW] line is longer than one sentence;
    - every gap is listed.

    TASK (again): cut the script from the takes above.

The 30-second hook and the search-or-browse reader come from A6 (§1.2; Playbook, YouTube rules 1 and 2): YouTube's Intro metric measures the first 30 seconds, and high click-through with low view duration is the pattern YouTube's help page describes for clickbait.

**Worked example · the half-marathon season opener** (the episode A3's brief schedules after the karate season):

    TASK: Cut a script for one long-form episode, <UNKNOWN: working title of the season opener>, from the dictated takes below.

    READER: a viewer who has never heard of me and arrives through browse or suggested: they saw the thumbnail. They decide in the first 30 seconds whether the title was true.

    OUTPUT: Markdown in this chat:
    1. Hook (first 30 seconds): the lines that make the title true.
    2. Chapters: for each, a one-line purpose, then its lines in order.
    3. Ending: the last line, taken from the takes.
    4. Gaps: anything the episode needs that the takes do not contain (a line I must record, a shot I must film, a claim that needs a source before it goes on camera).
    Mark every line with its origin: [T1], [T2] (take number, with the timestamp if the transcript has one) or [NEW] for any line you wrote.
    Target runtime: <UNKNOWN: target minutes; A3's brief gives 10–20 minutes per long-form episode>.

    CONSTRAINTS:
    - Use my sentences from the takes. Reorder and cut freely; rewrite none.
    - A [NEW] line is one sentence at most and bridges two take lines; I rewrite every one.
    - Keep the doubts and failures the takes contain. The opener starts from the end of competitive karate; that ending stays in.
    - The goal is a sub-1:45 half marathon in spring or summer 2027. State it once, in my words if the takes have them.
    - Avoid: jokes you invented; a closing line about believing in yourself; asking viewers to subscribe; any claim of fact not in the takes; any training advice.

    EXAMPLE (shape of one chapter):
    <example>
    Chapter 2 · <purpose in one line>
    [T1 03:12] "<my sentence>"
    [T2 00:45] "<my sentence>"
    [NEW] <one bridging sentence>
    </example>

    MATERIAL:
    <take_1>
    <UNKNOWN: transcript of the first dictated take>
    </take_1>
    <take_2>
    <UNKNOWN: transcript of the second dictated take>
    </take_2>

    DONE WHEN:
    - every line carries an origin mark;
    - the hook makes the working title true within 30 seconds of speech;
    - no [NEW] line is longer than one sentence;
    - every gap is listed.

    TASK (again): cut the script from the takes above.

### 5 · Title and thumbnail options

**Use when:** a script is final and the episode needs packaging for YouTube's Test & Compare, which takes up to three titles or thumbnails and picks the winner on watch time ([YouTube Help, *A/B test titles & thumbnails*](https://support.google.com/youtube/answer/16391400?hl=en); A6 §1.2). **Model:** B2 has no row for this task; Sonnet 5.5, low, by analogy with B2's Shōmen-posts row (short public copy).

    TASK: Write three title-and-thumbnail pairs for the episode below, for one Test & Compare run.

    READER: <FILL: search viewer: they typed a problem | browse viewer: they have never heard of me>.

    OUTPUT: a table in this chat with three rows and four columns: Title | Thumbnail text | Thumbnail style (Swiss-grid recap or sci-fi HUD/glitch) | What the first 30 seconds of the script show that makes this title true (quote the line).

    CONSTRAINTS:
    - Each title must be true of the script's first 30 seconds. Quote the line that makes it true.
    - The three pairs take three different angles on the same episode.
    - Thumbnail text: <FILL: word limit>, set in Tomorrow; red #FF2A50 and light blue #54C8FF on near-black; one of the two locked Shōmen styles.
    - English. <FILL: whether one Portuguese variant is wanted>.
    - Avoid: a promise the script does not keep; a question the episode does not answer; "you won't believe", "the truth about", "nobody tells you"; whole titles in capitals; emoji.

    EXAMPLES (my register: the titles of my two existing episodes):
    <example>Sometimes You Win, Sometimes You Learn. Mostly It Sucks</example>
    <example>Being a Better Athlete Made Me a Worse Person</example>

    BAD EXAMPLE (never write this):
    <bad_example>
    The ONE Training Secret Nobody Tells You
    Why it is wrong: it promises a secret the episode does not reveal, uses a banned phrase, and capitalises for volume.
    </bad_example>

    MATERIAL:
    <script>
    <FILL: the final script, hook first>
    </script>

    DONE WHEN:
    - three rows, three different angles;
    - each row quotes the hook line that makes its title true;
    - no avoided pattern appears.

**Worked example · the half-marathon season opener:**

    TASK: Write three title-and-thumbnail pairs for the episode below, for one Test & Compare run.

    READER: browse viewer: they have never heard of me.

    OUTPUT: a table in this chat with three rows and four columns: Title | Thumbnail text | Thumbnail style (Swiss-grid recap or sci-fi HUD/glitch) | What the first 30 seconds of the script show that makes this title true (quote the line).

    CONSTRAINTS:
    - Each title must be true of the script's first 30 seconds. Quote the line that makes it true.
    - The three pairs take three different angles on the same episode: leaving competition, the new goal, the starting point.
    - Thumbnail text: <UNKNOWN: word limit; A5 covers thumbnails>, set in Tomorrow; red #FF2A50 and light blue #54C8FF on near-black; one of the two locked Shōmen styles.
    - English only.
    - Avoid: a promise the script does not keep; a question the episode does not answer; "you won't believe", "the truth about", "nobody tells you"; whole titles in capitals; emoji; any finishing time the script does not state.

    EXAMPLES (my register: the titles of my two existing episodes):
    <example>Sometimes You Win, Sometimes You Learn. Mostly It Sucks</example>
    <example>Being a Better Athlete Made Me a Worse Person</example>

    BAD EXAMPLE (never write this):
    <bad_example>
    The ONE Training Secret Nobody Tells You
    Why it is wrong: it promises a secret the episode does not reveal, uses a banned phrase, and capitalises for volume.
    </bad_example>

    MATERIAL:
    <script>
    <UNKNOWN: the final script of the season opener, from template 4>
    </script>

    DONE WHEN:
    - three rows, three different angles;
    - each row quotes the hook line that makes its title true;
    - no avoided pattern appears.

### 6 · Shōmen post in the two locked styles

**Use when:** Shōmen has something to post. **Model:** Sonnet 5.5, low (B2, Shōmen posts).

    TASK: Write one Shōmen post about <FILL: subject>, in both locked styles.

    READER: people who follow a karate apparel brand on Instagram. They know the sport's vocabulary; they scroll past anything that reads like an advert.

    OUTPUT: Markdown in this chat, two versions:
    A · Swiss-grid recap. B · Sci-fi HUD/glitch.
    For each version: (1) on-image text for the 1:1 feed post: a headline, then up to <FILL: number> data lines; (2) on-image text for the 9:16 story; (3) caption; (4) alt text describing the image for a screen reader.

    CONSTRAINTS:
    - Brand system: Tomorrow typeface; red #FF2A50 and light blue #54C8FF highlights on near-black. Swiss-grid: facts in aligned rows, no decoration. HUD/glitch: the same facts as readouts.
    - Every fact comes from the material below. An athlete is named only as the material names them.
    - English. <FILL: Portuguese line yes or no>.
    - Avoid: "elevate", "unleash", "level up", "game-changer"; strings of exclamation marks; more than <FILL: number> hashtags.

    EXAMPLE (shape of a Swiss-grid data line):
    <example>
    <EVENT> · <CATEGORY> · <RESULT>
    </example>

    MATERIAL:
    <facts>
    <FILL: the facts: event, date, results, people and how they are credited>
    </facts>

    DONE WHEN:
    - both styles, each with feed text, story text, caption and alt text;
    - every fact on the image and in the caption is in the material;
    - no avoided word appears.

**Worked example · recap of the WIKF Global Cup (October 2026):**

    TASK: Write one Shōmen post recapping the WIKF Global Cup, October 2026, in both locked styles.

    READER: people who follow a karate apparel brand on Instagram. They know the sport's vocabulary; they scroll past anything that reads like an advert.

    OUTPUT: Markdown in this chat, two versions:
    A · Swiss-grid recap. B · Sci-fi HUD/glitch.
    For each version: (1) on-image text for the 1:1 feed post: a headline, then up to <UNKNOWN: number of data lines the grid holds> data lines; (2) on-image text for the 9:16 story; (3) caption; (4) alt text describing the image for a screen reader.

    CONSTRAINTS:
    - Brand system: Tomorrow typeface; red #FF2A50 and light blue #54C8FF highlights on near-black. Swiss-grid: facts in aligned rows, no decoration. HUD/glitch: the same facts as readouts.
    - Every fact comes from the material below. An athlete is named only as the material names them.
    - English only.
    - Avoid: "elevate", "unleash", "level up", "game-changer"; strings of exclamation marks; more than <UNKNOWN: hashtag limit> hashtags.

    EXAMPLE (shape of a Swiss-grid data line):
    <example>
    <EVENT> · <CATEGORY> · <RESULT>
    </example>

    MATERIAL:
    <facts>
    Event: WIKF Global Cup, October 2026.
    Venue and dates: <UNKNOWN: venue and exact dates>.
    Results: <UNKNOWN: each result, by category>.
    Shōmen-sponsored athletes: <UNKNOWN: each athlete's name exactly as they agreed to be credited, with their category and result>.
    Post angle: the last competition of my own competitive karate; the athletes carry on.
    </facts>

    DONE WHEN:
    - both styles, each with feed text, story text, caption and alt text;
    - every fact on the image and in the caption is in the material;
    - no avoided word appears.

### 7 · Research brief

**Use when:** a question needs search and synthesis before a decision. **Model:** Opus 5.5, high (B2, Research).

    TASK: Research this question and report what the evidence says: <FILL: question>.

    WHY: the answer decides <FILL: the decision it feeds>.

    READER: me. I check every citation, and I act on the answer within <FILL: timeframe>.

    OUTPUT: Markdown in this chat:
    1. Answer: three sentences at most, with the strength of the evidence stated.
    2. Findings table: Claim | Source (author or organisation, title, date, URL) | Source class | Sample or scope | Date you checked it.
    3. Where sources disagree: each side named, with its source.
    4. Not found: what you searched for and could not source.
    5. Unsure list: up to ten claims you could not verify.

    CONSTRAINTS:
    - Source classes, strongest first: peer-reviewed work; official documentation or statements from the body concerned; large-sample datasets (named, with sample size and date); documented cases with verifiable numbers. Label vendor data, correlational data and anecdote as such.
    - Every number says whose figure it is.
    - Quotation marks hold the source's exact words.
    - Date every fact that can change.
    - If a claim cannot be sourced, say so and keep it out of the Answer.
    - Out of scope: <FILL: what not to research>.

    DONE WHEN:
    - every row of the table has a working URL you opened;
    - the Answer uses only rows of the table;
    - sections 3, 4 and 5 exist, even if one says "none".

    TASK (again): research the question above and report.

The source classes and labels are the course's own sourcing standard (`sourcing-standard.md` Part 2); the unsure list follows Anthropic's advice to give the model a sanctioned place for what it cannot verify (§3).

**Worked example · structuring the half-marathon block:**

    TASK: Research this question and report what the evidence says: for a recreational runner aiming at a sub-1:45 half marathon in spring or summer 2027, what does the evidence say about weekly running volume and the share of it run at higher intensity?

    WHY: the answer decides how I structure the weekly training block from now to race day.

    READER: me. I check every citation, and I act on the answer within <UNKNOWN: start date of the block>.

    OUTPUT: Markdown in this chat:
    1. Answer: three sentences at most, with the strength of the evidence stated.
    2. Findings table: Claim | Source (author or organisation, title, date, URL) | Source class | Sample or scope | Date you checked it.
    3. Where sources disagree: each side named, with its source.
    4. Not found: what you searched for and could not source.
    5. Unsure list: up to ten claims you could not verify.

    CONSTRAINTS:
    - Source classes, strongest first: peer-reviewed work; official documentation or statements from the body concerned; large-sample datasets (named, with sample size and date); documented cases with verifiable numbers. Label vendor data, correlational data and anecdote as such.
    - Every number says whose figure it is.
    - Quotation marks hold the source's exact words.
    - Date every fact that can change.
    - If a claim cannot be sourced, say so and keep it out of the Answer.
    - Context: I also train karate and coach each week; my current half-marathon time is <UNKNOWN: most recent half-marathon or 10 km time>.
    - Out of scope: nutrition, body weight, injury treatment, supplements, and any brand's training plan sold as a product.

    DONE WHEN:
    - every row of the table has a working URL you opened;
    - the Answer uses only rows of the table;
    - sections 3, 4 and 5 exist, even if one says "none".

    TASK (again): research the question above and report.

### 8 · Message in his texting voice

**Use when:** a short message to a named person. The voice rules below are his voice-drafting skill's (the Learning Project's setup as of 28 October 2026), except the cap of one emoji, which is mine; when the skill fires, it also triages stakes. **Model:** Sonnet 5.5, low for routine messages; Opus 5.5, medium for high-stakes ones (B2, Message drafts).

    TASK: Draft one message to <FILL: first name> that <FILL: what it must do: ask, confirm, decline, thank>.

    READER: <FILL: who they are to me, in a few words>. Register: <FILL: casual | professional>. Stakes: <FILL: low | medium | high>.

    OUTPUT: the message, ready to paste, and nothing else. If stakes are medium, add three lines after it on what could be misread. If stakes are high, stop and tell me to use the voice-drafting skill.

    CONSTRAINTS (casual register):
    - lowercase throughout, "i" included; contractions always
    - one flowing block, never split into several texts
    - British-casual phrasing ("fancy grabbing", "sort something out")
    - generous exclamation marks; warm closer ("all the best!", "hope you're good!")
    - no full stop at the end of the message
    - very sparing emoji (at most one)
    - energetic, never try-hard

    CONSTRAINTS (professional register):
    - standard capitalisation and punctuation; the point in the first sentence
    - light dry wit only if the relationship is established
    - Portuguese only if they are a Portuguese speaker
    - no emoji, except 👀 or 🙏 with a peer in a casual context

    FACTS: use only these. If something the message needs is missing, write [?] in its place.
    <facts>
    <FILL: the facts>
    </facts>

    EXAMPLE (casual register; built from the rules above, not a real message):
    <example>
    hey <name>! fancy grabbing a coffee after training thursday? want to pick your brain about something, nothing serious. hope you're good!
    </example>

    BAD EXAMPLE (never write this):
    <bad_example>
    Hi <name>, I hope this message finds you well. I wanted to reach out regarding a quick question.
    Why it is wrong: capitalised, a stock opener, corporate phrasing, and a full stop at the end.
    </bad_example>

    DONE WHEN: the message follows every rule of its register, contains only the facts given, and is one block.

**Worked example · asking a training partner about filming** (filming inside a session is A5's capture method; the image rights of training partners are on A8's brief):

    TASK: Draft one message to <UNKNOWN: training partner's first name> that asks whether they're happy to appear in footage I shoot during <UNKNOWN: day> training.

    READER: a training partner at the club. Register: casual. Stakes: low.

    OUTPUT: the message, ready to paste, and nothing else.

    CONSTRAINTS (casual register):
    - lowercase throughout, "i" included; contractions always
    - one flowing block, never split into several texts
    - British-casual phrasing ("fancy grabbing", "sort something out")
    - generous exclamation marks; warm closer ("all the best!", "hope you're good!")
    - no full stop at the end of the message
    - very sparing emoji (at most one)
    - energetic, never try-hard

    FACTS: use only these. If something the message needs is missing, write [?] in its place.
    <facts>
    - the footage is for a YouTube episode about the start of my half-marathon season, with some karate in it
    - saying no is completely fine and i'll keep them out of shot
    - it goes on youtube, instagram and the weekly email, and stays up once it's out
    - they can change their mind any time with one message and i'll blur or cut them out, with a dated note
    - <UNKNOWN: anything else I am offering, e.g. seeing the cut before it goes up>
    </facts>

    EXAMPLE (casual register; built from the rules above, not a real message):
    <example>
    hey <name>! fancy grabbing a coffee after training thursday? want to pick your brain about something, nothing serious. hope you're good!
    </example>

    BAD EXAMPLE (never write this):
    <bad_example>
    Hi <name>, I hope this message finds you well. I wanted to reach out regarding a quick question.
    Why it is wrong: capitalised, a stock opener, corporate phrasing, and a full stop at the end.
    </bad_example>

    DONE WHEN: the message follows every rule of its register, contains only the facts given, and is one block.

### 9 · Decision memo

**Use when:** a choice between options needs a recorded answer. The format is his preferences' decision format. **Model:** B2 has no row for this task; Opus 5.5, medium, by analogy with B2's high-stakes message row (judgement work, cents per run).

    TASK: Decide <FILL: the decision> and write the decision memo.

    READER: me now, and me in <FILL: months> checking whether the override has fired.

    OUTPUT: Markdown in this chat, in this order:
    1. Door: two-way (reversible, low stakes) or one-way (hard to reverse). If one-way, first a pre-mortem: assume the decision failed by <FILL: date>; give the three likeliest causes.
    2. Pick: <one option>.
    3. Reasons: up to three, twelve words or fewer each, each tied to a numbered fact below.
    4. Override if: one line, a condition I can observe.
    5. Missing facts: any fact that would change the pick, and where to find it.

    CONSTRAINTS:
    - One recommendation. No neutral pro and con table; no "it depends".
    - Use only the facts below, cited by number.
    - A two-way door gets a fast, good-enough pick.

    MATERIAL:
    <options>
    <FILL: the options>
    </options>
    <facts>
    <FILL: numbered facts, each with its source>
    </facts>

    DONE WHEN: one pick; every reason cites a fact; the override can be observed without asking anyone.

**Worked example · claude.ai plan, given the audit load:**

    TASK: Decide which claude.ai plan to be on for the rest of the Brand + AI build, and write the decision memo.

    READER: me now, and me in three months checking whether the override has fired.

    OUTPUT: Markdown in this chat, in this order:
    1. Door: two-way (reversible, low stakes) or one-way (hard to reverse). If one-way, first a pre-mortem: assume the decision failed by 31 January 2027; give the three likeliest causes.
    2. Pick: <one option>.
    3. Reasons: up to three, twelve words or fewer each, each tied to a numbered fact below.
    4. Override if: one line, a condition I can observe.
    5. Missing facts: any fact that would change the pick, and where to find it.

    CONSTRAINTS:
    - One recommendation. No neutral pro and con table; no "it depends".
    - Use only the facts below, cited by number.
    - A two-way door gets a fast, good-enough pick.

    MATERIAL:
    <options>
    Pro; Max 5x; Max 20x.
    </options>
    <facts>
    1. Current plan: <UNKNOWN: my current plan>.
    2. Pro is $20 a month billed monthly, $17 a month billed annually; Max is $100 a month for five times Pro's usage per session and $200 for twenty times (B2 §2, from claude.com/pricing and the Max plan help article, 28 Oct 2026).
    3. On Pro, Fable 5.1 sits outside the plan's limits and runs on usage credits, billed at API rates: $10 input and $50 output per million tokens (B2 §2 and §3).
    4. On Max, up to half of the weekly limit may go to Fable at no extra cost; Fable uses the pool faster than other models (B2 §2).
    5. Every Brand + AI unit now gets a Fable fresh check, and every four units a Fable sample audit (method.md §1 and §6).
    6. Units still to write: <UNKNOWN: count from courses-index.md on the day>.
    7. My Fable spend on usage credits last month: <UNKNOWN: from claude.ai billing>.
    </facts>

    DONE WHEN: one pick; every reason cites a fact; the override can be observed without asking anyone.

### 10 · Weekly email

**Use when:** the week's material exists (a journal record from template 3, an episode or post) and the weekly email is due. **Model:** Sonnet 5.5, low. `method.md` §4 lists "emails from a finished unit" among the derivative work it gives to Sonnet and Haiku; treating an email cut from a finished journal record as the same kind of job is my reading, and low effort is by analogy with B2's Shōmen-posts row.

    TASK: Write this week's email, for <FILL: send date>, from the material below.

    READER: subscribers to the list. Some follow one journey only; all of them chose to get this in their inbox.

    OUTPUT: in this chat: one subject line and one alternative; then the body, <FILL: word limit> words or fewer; links as plain web links, one per item.
    Body order: (1) the lead journey, <FILL: which>, what happened this week, in my words; (2) one line on each other live journey, only if something moved; (3) this week's episode or post, with its link. Nothing else.

    CONSTRAINTS:
    - Everything comes from the material. Quote me where the material has my words.
    - Failures and missed weeks stay in, stated plainly.
    - Avoid: "I hope you're well"; "exciting news"; any line asking for shares; motivational sign-offs; Shōmen promotion beyond <FILL: what, if anything>.
    - British English.

    MATERIAL:
    <journal_record>
    <FILL: the week's dated record, from template 3>
    </journal_record>
    <links>
    <FILL: episode or post URLs>
    </links>

    DONE WHEN: one lead journey; the word limit is met; every link works; every fact is in the material.

    TASK (again): write this week's email from the material above.

**Worked example · the first email of the half-marathon season:**

    TASK: Write this week's email, for <UNKNOWN: send date; A3's brief starts its calendar on 3 November 2026>, from the material below.

    READER: subscribers to the list. Some follow one journey only; all of them chose to get this in their inbox.

    OUTPUT: in this chat: one subject line and one alternative; then the body, <UNKNOWN: word limit; A3's brief calls it "one short weekly email"> words or fewer; links as plain web links, one per item.
    Body order: (1) the lead journey, the half marathon, what happened this week, in my words; (2) one line on each other live journey (karate coaching, the history course), only if something moved; (3) this week's episode, with its link. Nothing else.

    CONSTRAINTS:
    - Everything comes from the material. Quote me where the material has my words.
    - Failures and missed weeks stay in, stated plainly. Competitive karate has ended; say so once if the material does.
    - Avoid: "I hope you're well"; "exciting news"; any line asking for shares; motivational sign-offs; any Shōmen promotion.
    - British English.

    MATERIAL:
    <journal_record>
    <UNKNOWN: this week's dated record, from template 3>
    </journal_record>
    <links>
    <UNKNOWN: URL of the season-opener episode>
    </links>

    DONE WHEN: one lead journey; the word limit is met; every link works; every fact is in the material.

    TASK (again): write this week's email from the material above.

## Writer's unsure list

Fresh check 29 Oct 2026 (Fable 5.1): fix · 1 error, 4 should-fix, 9 minor; all applied (the rendering finding by a `theme.css` rule; the optional cut of repeated template lines not taken, so each worked example stays paste-ready); report `audits/brand-ai/fresh-check-B3.md`.

Audit 2 29 Oct 2026 (Fable 5.1, stratified sample): PASS · 0 of 6 sampled FAIL, 0 of 28 checked; no errata; report `audits/brand-ai/audit-2.md`.

1. **Anthropic's "up to 30 percent" figure** for queries placed after long documents is vendor data with no published method, task set or model list on the page; it is reported as such and nothing in the library depends on the number.
2. **Laban et al.:** the paper names 15 models (Claude 3.7 Sonnet, GPT-4.1, o3, Gemini 2.5 Pro among them) and its multi-turn setting reveals a fixed instruction one piece per turn with no user corrections (fresh check, 29 Oct 2026). Whether the 39% average drop holds for Opus 5.5 or Fable 5.1 is untested.
3. **Jang et al. (negated prompts)** is a 2023 workshop paper on models of 2022; the inverse-scaling result may not hold for current models. It is used only to support pairing each prohibition with a positive instruction.
4. **Contrastive chain-of-thought (Chia et al.)** is cited as an arXiv preprint; I found no venue, and the abstract reports no figures. It is the only direct evidence for negative examples in the unit.
5. **IFScale (Jaroslawicz et al.)** is a NeurIPS 2025 workshop poster, not a main-track paper; its 500 keyword-inclusion instructions are far denser than any of his prompts, so the size of the effect at his scale is unknown.
6. **The conflict between his preferences' HTML-artifact rule and the Markdown unit format** is observed from the two texts; how the model resolves it in practice is undocumented, and the Claude Code statement that Claude "may pick one arbitrarily" is applied to claude.ai by analogy.
7. **Anthropic's model-specific prompting pages** (Opus 5.5, Fable 5.1, Sonnet 5.5) are written for API and agent use; carrying their advice into claude.ai chat is my inference throughout.
8. **OpenAI's help-centre article** shows no publication or update date (only a relative "updated" label), so how current its advice is for OpenAI's present models could not be established.
9. **Model lines for title options, decision memos and the weekly email's effort level** have no B2 row; they are my analogies from neighbouring rows and are marked as such.
10. **Rendering:** the templates are indented code blocks so their angle-bracket placeholders survive the Markdown build. `design/theme.css` has no rule for `pre` inside `.report`, so long template lines may scroll sideways on a phone; any fix belongs in `theme.css` (design rule). Resolved at filing, 29 Oct 2026: `theme.css` §4a now wraps a unit's code blocks inside the column.

## Sources

All web sources checked 28–29 October 2026.

- Anthropic. *Prompting best practices*. Claude Platform docs. https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices
- Anthropic. *Prompt engineering overview*. Claude Platform docs. https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview
- Anthropic. *Prompting Claude Opus 5.5*. Claude Platform docs. https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5-5
- Anthropic. *Prompting Claude Fable 5.1*. Claude Platform docs. https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-1
- Anthropic. *Prompting Claude Sonnet 5.5*. Claude Platform docs. https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-sonnet-5-5
- Anthropic. *Define success criteria and build evaluations*. Claude Platform docs. https://platform.claude.com/docs/en/test-and-evaluate/develop-tests
- Anthropic. *Reduce hallucinations*. Claude Platform docs. https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations
- Anthropic. *Effective context engineering for AI agents*. Anthropic Engineering, 29 September 2025. https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
- Claude blog. *Best practices for prompt engineering for 2026*. 10 November 2025. https://claude.com/blog/best-practices-for-prompt-engineering
- Claude Code docs. *How Claude remembers your project* (Memory). https://code.claude.com/docs/en/memory
- Claude Help Center. *Understanding Claude's personalization features*. https://support.claude.com/en/articles/10185728
- OpenAI Help Center. *Best practices for prompt engineering with the OpenAI API* (article 6654000). https://help.openai.com/en/articles/6654000
- OpenAI. *Prompt engineering*. OpenAI API docs. https://developers.openai.com/api/docs/guides/prompt-engineering
- Google. *Prompt design strategies*. Gemini API docs, last updated 13 October 2026. https://ai.google.dev/gemini-api/docs/prompting-strategies
- YouTube Help. *A/B test titles & thumbnails* (answer 16391400). https://support.google.com/youtube/answer/16391400?hl=en
- Zheng, M., Pei, J., Logeswaran, L., Lee, M. and Jurgens, D. "When 'A Helpful Assistant' Is Not Really Helpful: Personas in System Prompts Do Not Improve Performances of Large Language Models". *Findings of the Association for Computational Linguistics: EMNLP 2024*, 15126–15154. https://aclanthology.org/2024.findings-emnlp.888/
- Min, S., Lyu, X., Holtzman, A., Artetxe, M., Lewis, M., Hajishirzi, H. and Zettlemoyer, L. "Rethinking the Role of Demonstrations: What Makes In-Context Learning Work?". *Proceedings of EMNLP 2022*, 11048–11064. https://aclanthology.org/2022.emnlp-main.759/
- Jang, J., Ye, S. and Seo, M. "Can Large Language Models Truly Understand Prompts? A Case Study with Negated Prompts". *Proceedings of the 1st Transfer Learning for Natural Language Processing Workshop*, PMLR 203 (2023), 52–62. https://proceedings.mlr.press/v203/jang23a.html
- Chia, Y. K., Chen, G., Tuan, L. A., Poria, S. and Bing, L. "Contrastive Chain-of-Thought Prompting". arXiv 2311.09277, 2023 (preprint). https://arxiv.org/abs/2311.09277
- Levy, M., Jacoby, A. and Goldberg, Y. "Same Task, More Tokens: the Impact of Input Length on the Reasoning Performance of Large Language Models". *Proceedings of the 62nd Annual Meeting of the ACL (Volume 1: Long Papers)*, 2024, 15339–15353. https://aclanthology.org/2024.acl-long.818/
- Shi, F., Chen, X., Misra, K., Scales, N., Dohan, D., Chi, E., Schärli, N. and Zhou, D. "Large Language Models Can Be Easily Distracted by Irrelevant Context". ICML 2023. https://icml.cc/virtual/2023/poster/24255 · arXiv 2302.00093: https://arxiv.org/abs/2302.00093
- Jaroslawicz, D., Whiting, B., Shah, P. and Maamari, K. "How Many Instructions Can LLMs Follow at Once?". arXiv 2507.11538, 2025; poster at the NeurIPS 2025 workshop *Evaluating the Evolving LLM Lifecycle*. https://arxiv.org/abs/2507.11538 · https://neurips.cc/virtual/2025/122417
- Laban, P., Hayashi, H., Zhou, Y. and Neville, J. "LLMs Get Lost In Multi-Turn Conversation". ICLR 2026 (oral). https://iclr.cc/virtual/2026/oral/10009147 · arXiv 2505.06120: https://arxiv.org/abs/2505.06120
- Zhang, W. et al. "LIFEBench: Evaluating Length Instruction Following in Large Language Models". NeurIPS 2025, Datasets and Benchmarks Track. https://proceedings.neurips.cc/paper_files/paper/2025/hash/c84f00ccee3d35cee1901acb0e258dc7-Abstract-Datasets_and_Benchmarks_Track.html · arXiv 2505.16234: https://arxiv.org/abs/2505.16234
- Learning Project files cited by name: `method.md` §1, §4, §6, §7; `sourcing-standard.md` Part 2; `reader.md`; `courses-index.md`; `skills/write-unit/SKILL.md`; `skills/audit-units/SKILL.md`; B1 · Mental model (`B1-mental-model.md`) §1, §2, §3, §6; B2 · Choosing the model (`B2-choosing-the-model.md`) §2, §3, §6, §7, §8 and Deliverable; A6 · How growth works, per platform (`A6-how-growth-works-per-platform.md`) §1.2 and Deliverable 1. The Learning Project's setup as of 28 October 2026 (saved preferences, voice-drafting skill, Shōmen brand system) is cited as observed, not as a published source.

Erratum 15 Nov 2026, found by BW3's writer and confirmed by a corrections check (Opus 5.5, row W-BW3; `audits/building-with-ai/corrections-2026-11-15-BW1-B3.md`): §2 now quotes OpenAI's API guide as it reads on 15 Nov 2026, "benefit from precise instructions" (the source unit had "very precise instructions").
