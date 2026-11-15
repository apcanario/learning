---
audit: fresh check
unit: BW3 · Briefing: prompts that hold up
course: building-with-ai · Building with AI
model: Opus 5.5
date: 2026-11-15
chat: https://claude.ai/code/session_01KMmgR2X8gxiztAgknM3utG
verdict: fix · 0 errors, 8 should-fix, 11 minor
---

The checker's final report, verbatim, from its hand-back. Saved before any finding was applied.

Verdict: BW3 · fix · 0 error, 8 should-fix, 11 minor

claude-opus-5-5. The harness refused the write to out/report.md, so the full report follows.

# Fresh check · BW3 · Briefing: prompts that hold up

Checker: claude-opus-5-5, isolated agent context, packet only, live search 15 Nov 2026. There is no audit report, so the errata step was skipped. Fetch rule: WebSearch first, then WebFetch only of URLs that a search returned verbatim. Redirected or refused fetches are recorded as "not checked".

## (1) Coverage
- Four parts of a brief (§1): covered.
- Specificity against length (§2): covered.
- Output contracts (§3): covered.
- Examples and question position, evidence and vendor guidance labelled (§4): covered.
- Drift and when to restart (§5): covered.
- Common failures (§6): covered.
- What the literature measured, and on which models (§7): covered.
- "On other tools" (§8): covered.
- Deliverable: covered. All ten templates are present, each with a worked example, plus a blank form. Template 8 is worked on a neutral example that is labelled as invented.

## Findings
[should-fix] [accuracy] §6 opening; Current: "Three failures account for most first outputs that miss, on the evidence below."; Problem: no source in the unit counts how often first outputs miss or which failures cause them, so "most" is an unsourced quantitative claim (Part 1, Part 6); Fix: "Three failures recur in the vendor guidance and the studies below; no source read for this unit counts how often each causes a miss."; Basis: the unit's §6 and §7 cite no frequency data; sourcing-standard Parts 1 and 6.
[should-fix] [accuracy] §5 point 4; Current: "through a simulated user who never corrects the model"; Problem: the paper describes a simulator that reveals at most one shard per turn and rephrases it, and does not say the user "never corrects the model" (a stretch of the source); Fix: "through a simulated user that reveals one piece of the instruction per turn"; Basis: Laban et al. §3–§5, https://arxiv.org/pdf/2505.06120
[should-fix] [figure] §5 paragraph after the list; Current: "That result was measured on the models of 2025 through their APIs."; Problem: the temperature-0 result (§7.2, Table 3) was measured on GPT-4o and GPT-4o-mini only (29.7 and 30.5), and Part 6 requires naming the models; Fix: "That result was measured on GPT-4o and GPT-4o-mini through their APIs in 2025 (Table 3 of the paper)."; Basis: Laban et al. §7.2, Table 3, https://arxiv.org/pdf/2505.06120
[should-fix] [accuracy] §3 "The case"; Current: "It does show that a stated range did not bound a long output, which is what the evidence above predicts."; Problem: LIFEBench measured models following explicit length targets: they deteriorate on long targets and fall short of claimed maximum lengths. One unit running past a 2,000–6,000-word "guide" is not what that evidence predicts, and the sentence uses one anecdote to confirm a measured result; Fix: "It shows one output that ran past a stated range; that fits the evidence above that long length instructions are followed poorly, and it is an anecdote, not a test of it."; Basis: LIFEBench abstract ("deteriorate sharply beyond a certain threshold"; "almost all models fail to reach the vendor-claimed maximum output lengths"), https://proceedings.nips.cc/paper_files/paper/2025/hash/c84f00ccee3d35cee1901acb0e258dc7-Abstract-Datasets_and_Benchmarks_Track.html; Academy case file §1.
[should-fix] [deliverable] Template 4, decision memo; Current: "3. Recommendation: one option; at most three reasons, each twelve words or fewer, each pointing to evidence in 2."; Problem: the template has a BAD EXAMPLE with no good example beside it, which breaks the unit's own rule (§1, §4, Conventions, the brief form); Fix: "3. Recommendation: one option; at most three reasons, each twelve words or fewer, each pointing to evidence in 2. Shape of a good one: [FILL: one recommendation from a past memo that worked; the BAD EXAMPLE below is shown beside it]."; Basis: unit §1 "Examples, including negative ones" and §4 "Negative examples".
[should-fix] [label] Template 6, worked example; Current: "the owner, who wrote the method and set the audit rule, has not read the report, and will read this on a phone."; Problem: the case file does not say that the owner wrote the method, has not read the report, or reads on a phone. Part 6 and the brief forbid inferring case facts the file does not hold; Fix: "the owner, who decides whether the three units are rewritten."; Basis: Academy case file §2, §3.
[should-fix] [label] Template 10, worked example; Current: "the project's owner, who runs the build and reads short scripts but does not write them."; Problem: the case file says nothing about what code the owner reads or writes, or that the owner runs the build, so this is an invented case fact; Fix: "the project's owner, who decides whether the change goes in."; Basis: Academy case file §1, §6.
[should-fix] [attribution] §8 table, row "Say what to do"; Current: "Negative constraints at the end of the instruction: [Google Cloud page on Gemini 3]"; Problem: the Google page says where negative constraints go, which is not the same advice as "say what to do instead of what not to do", so the cell offers a different claim as the equivalent; Fix: "No equivalent found in the pages read (it says only where negative constraints go): [Google Cloud page on Gemini 3]"; Basis: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/start/gemini-3-prompting-guide ("negative constraints should be placed at the end of the instruction").
[minor] [accuracy] §1 Constraints; Current: "across pretrained, instruction-tuned and few-shot setups"; Problem: the paper evaluates four LM types, and the fourth is models fine-tuned on negated prompts; Fix: "across pretrained, instruction-tuned, few-shot and negation-fine-tuned setups"; Basis: https://proceedings.mlr.press/v203/jang23a.html
[minor] [attribution] Sources, Research; Current: "Shi, F. et al. (full author list not re-read for this unit)."; Problem: the full author list is on the paper's title page; Fix: "Shi, F., Chen, X., Misra, K., Scales, N., Dohan, D., Chi, E., Schärli, N. and Zhou, D."; Basis: https://arxiv.org/pdf/2302.00093
[minor] [attribution] Sources, The case; Current: "cited by section, §1 to §3, §5 to §7 and §9."; Problem: §4 is also cited, in template 1's worked example ("case file §4"); Fix: "cited by section, §1 to §7 and §9."; Basis: unit, template 1 worked example.
[minor] [deliverable] Template 4 worked example; Current: "OUTPUT: Markdown in this chat, at most 400 words: the decision asked; the two options, each with its cost, its risk and the evidence from the material; one recommendation with at most three reasons of twelve words or fewer; what would change it; unknowns."; Problem: the worked example also shows the bad example on its own; Fix: "OUTPUT: Markdown in this chat, at most 400 words: the decision asked; the two options, each with its cost, its risk and the evidence from the material; one recommendation with at most three reasons of twelve words or fewer; what would change it; unknowns. A good recommendation reads like this (invented, on another decision): \"Recommendation: B, move the review to Mondays. Reason: two of three missed reviews fell on Fridays (Options, B).\""; Basis: unit §4 rule on negative examples.
[minor] [accuracy] §6 Asking for a plan; Current: "the Sonnet 5.5 guide says the model tends to add tests, documentation and small supporting files nobody asked for"; Problem: the page limits this to coding ("Unrequested additions when coding"); Fix: "the Sonnet 5.5 guide says that, when coding, the model tends to add tests, documentation and small supporting files nobody asked for"; Basis: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-sonnet-5-5
[minor] [figure] §4 matrix; Current: "{"mark": "performance worst", "tone": 1}"; Problem: the text says "significantly worse" (§4) and "recalled worst" (§7), so "performance worst" is not the text's wording; Fix: "{"mark": "significantly worse", "tone": 1}"; Basis: unit §4 Research paragraph.
[minor] [figure] §5 decision; Current: ""q": "Did the requirements change, or was the chat summarised?","; Problem: the text's fourth condition is "has been summarised, or is long enough that it may be", and the figure drops the second half; Fix: ""q": "Did the requirements change, or was the chat summarised or near it?","; Basis: unit §5 "When to restart", fourth bullet.
[minor] [label] §3 What done looks like; Current: "read 15 Nov 2026; documented practice)"; Problem: the first citation of Best practices for Claude Code is not labelled vendor (Part 6); Fix: "read 15 Nov 2026; vendor; documented practice)"; Basis: sourcing-standard Part 6.
[minor] [label] §6 Stacking unrelated tasks; Current: "Fix: one artefact per brief."; Problem: the recommendation has no evidence grade (Part 6); Fix: "Fix (documented practice): one artefact per brief."; Basis: Part 6; Claude Code's "/clear between unrelated tasks".
[minor] [label] Template 4 worked example; Current: "the owner of the project, who sets the rules for every unit and decides before the next unit is filed."; Problem: "decides before the next unit is filed" is not in the case file; Fix: "the owner of the project, who sets the rule (case file §6)."; Basis: Academy case file §6.
[minor] [style] Template 2 worked example; Current: "one Markdown file, starting with the course's front matter."; Problem: "front matter" is a case detail the case file does not hold, and the public reader has not been told what it is; Fix: "one Markdown file."; Basis: Academy case file §1; brief.txt reader.

## Confirmed
- Anthropic, *Prompting best practices*: PASS on every quotation checked: new employee and colleague test; role "Even a single sentence makes a difference"; the ellipsis/TTS example and "Claude can generalize from the explanation"; the format line; the positive-instruction rule with both examples; "Include 3–5 examples" with <example> tags; 20k+ tokens, long data at the top, queries at the end "up to 30 percent in tests" with no method given; markdown matching; "Might skip detailed summaries…"; "suggest some changes"; "explicitly request it rather than relying on the model to infer"; "The more precisely you explain…"; chaining. https://platform.claude.com/en/docs/build-with-claude/prompt-engineering/claude-prompting-best-practices
- Claude, *Best practices for prompt engineering for 2026*, 10 Nov 2025: the three quotations. PASS. https://claude.com/resources/articles/best-practices-for-prompt-engineering
- *Prompting Claude Opus 5.5*: the generic-AI-look passage (frontend design), naming patterns to avoid, "extend the list if needed", removing think-carefully instructions in chat apps, "the effort level is the main control". PASS. https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5-5
- *Prompting Claude Fable 5.2*: "never" treated as absolute and the deletion example; style rules followed closely and choppy prose; "Effort has little effect on the length…". PASS. https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-2
- *Prompting Claude Sonnet 5.5*: open-ended requests; the suggested paragraph against unrequested additions. PASS, with the coding scope noted above.
- *Prompt engineering overview*: the three prerequisites, word for word. PASS. https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview
- *Reduce hallucinations*: "can drastically reduce false information" with no figure; quotes and sources for each claim; retract a claim that has no quote. PASS. https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations
- *Best practices for Claude Code*: PASS on every claim and quotation the unit uses: context fills and degrades; "forgetting"; the pass/fail check; evidence in place of assertion; the reviewer "will usually report some…"; the more-than-twice rule; the kitchen-sink session; explore/plan/implement and the one-sentence skip; valuable history. https://code.claude.com/docs/en/best-practices.md
- *How Claude remembers your project* (headline matches): three quotations. PASS. https://code.claude.com/docs/en/memory
- Rajasekaran, Dixon, Ryan and Hadfield, 29 Sep 2025, Applied AI team: all six quotations. PASS. https://anthropic.com/engineering/effective-context-engineering-for-ai-agents
- OpenAI Help Center 6654000: all six quotations. PASS. https://help.openai.com/en/articles/6654000
- OpenAI, *Prompt engineering*: high-level guidance for reasoning models; "which benefit from precise instructions"; context near the end; section order and caching; diverse inputs. PASS. https://developers.openai.com/api/docs/guides/prompt-engineering.md
- OpenAI, *Using GPT-6* (headline matches): don't stop at a plan; "a concrete, reviewable result"; the ban on named phrases. PASS. https://developers.openai.com/api/docs/guides/prompt-guidance
- Google Cloud, Gemini 3 guide: questions at the end after the data; the negative-constraints quotation; less verbose by default. PASS. https://docs.cloud.google.com/vertex-ai/generative-ai/docs/start/gemini-3-prompting-guide
- Zheng et al., Findings EMNLP 2024, 15126–15154: 162 roles, 2,410 questions, 4 model families, the quotation, automatic persona selection about as good as random. PASS.
- Min et al., EMNLP 2022, 11048–11064: "barely hurts performance", 12 models including GPT-3, the tasks and drivers. PASS.
- Jang, Ye and Seo, PMLR 203, 52–62: 9 tasks, the models, 125M–175B, the quotation. PASS.
- Shi et al., ICML 2023 / PMLR 202: "dramatically decreased", code-davinci-002 and text-davinci-003, the ignore instruction helps. PASS.
- Chia et al., arXiv 2311.09277: GPT-3.5-Turbo 0301; GSM8K 69.2→79.0, SVAMP 67.2→81.6, Bamboogle 40.8→56.8; better on all seven datasets. PASS.
- Levy, Jacoby and Goldberg, ACL 2024, 15339–15353: quotations; the trend appears in every version of the dataset; the abstract names no models. PASS.
- Jaroslawicz et al., arXiv 2507.11538: 500 instructions, 20 models from seven providers, 68%, bias towards earlier instructions. PASS. The NeurIPS 2025 page title was confirmed by search.
- LIFEBench, NeurIPS 2025 D&B: authors, 10,800 instances, EN/ZH, 16–8,192 words, 26 models, the quotation, "almost all" fall short of vendor maximums. PASS.
- Liu et al., TACL 12, 157–173: the finding and the tasks. PASS.
- Laban et al.: 39% across six tasks; 200,000+ conversations; "top open- and closed-weight"; the mechanism quotations; 15 models including Claude 3.7 Sonnet, GPT-4.1, o3 and Gemini 2.5 Pro; aptitude −15% (Fig. 1) and 16% (§6.2); unreliability +112%; temperature 0 leaves ~30% (§7.2); the three §7.4 quotations; ICLR 2026 (iclr.cc oral page, from search). PASS.
- Academy facts in §1–§3, §5, §6 and templates 1, 2, 3, 5, 7 and 9 match case file §1–§7 and §9. This includes the IA1 row and the totals 58/237/303 over 36 units.
- Not checked or unverifiable: Google *Long context* (ai.google.dev) redirected to aistudio.google.com, so the quotation and the date "last updated 15 Oct 2026" are unverified, and the link may now be stale. BW1 §2/§3/§5 and BW2's rows are not in the packet: the summarisation fact, temperature on Claude 4.7 and later, and the Model lines are unverifiable here.

## (7) Figures
1. Matrix, §4: FIX (minor). Every cell traces to §4 lines: "Put instructions at the beginning…"; "context… near the end… instructions and examples at the start"; "long documents near the top… queries at the end"; "query / question at the end"; "a one-line TASK first… material in tags… TASK repeated as the last line". The exception is Liu's "performance worst" (the text says "significantly worse"). The caption names the section and the sources. The kind (matrix) fits. Replacement cell: `{"label": "Liu et al. (measured)", "tone": 5, "cells": [null, {"mark": "significantly worse", "tone": 1}, null]}`
2. Decision, §5: FIX (minor). The questions and outcomes trace to the four "When to restart" bullets and to "Start a new chat, with a brief that consolidates…". The third question drops "or is long enough that it may be". The caption names the section and the sources. The kind (decision) fits. Replacement: `"q": "Did the requirements change, or was the chat summarised or near it?",`
3. Flow, Deliverable "The brief form": PASS. All eight labels and notes trace to the brief-form bullet list. The caption names the section and the grade. The kind (flow, a sequence) fits.

## (8) Writer's Source errors
1. B3 "very precise instructions": confirmed. OpenAI's page now reads "which benefit from precise instructions" (read 15 Nov 2026).

## (9) Part 6, line by line
- Sourced in place: holds, except §6 "most" (finding).
- Source kinds labelled: holds, except one missing "vendor" label (minor).
- Evidence grades: holds, except the §6 Fix lines (minor).
- Studies name their models and tasks, with inference flagged: holds, except Laban's temperature result (should-fix).
- Product facts dated: holds.
- "On other tools": present; one cell is not a true equivalent (should-fix).
- Carried claims re-verified: holds.
- No private-reader terms and no reference to the private course: holds. A search of the text found none.
- Case facts only from the case file: two worked-example reader lines break this (should-fix), plus one minor. The §3 case paragraph is used as confirmation (should-fix). Otherwise the case is labelled and treated as an anecdote.
- No inventions, quotations exact: holds.
- Deliverable on the case and as a template: holds.
- Not advice without evidence: holds.
- Links as links: holds. The Google Cloud URL carries a stray "?authuser=2" in five places. It is not listed as a finding because the string is not unique; strip it everywhere.

## (10) Read as the public persona
The unit works for the public reader who has read BW1 and BW2. One term leans on project knowledge: "front matter" (finding). The model names and "BW2, row N" lines depend on BW2, which is acceptable for a course read in order. The worked examples of templates 2, 3, 6, 7, 9 and 10 run on `[UNKNOWN]` slots (writer's Need 1), so they show the shape but cannot be run as written. No private-reader detail appears.

## (11) Attribution pass
Every Sources title I could see matches its page headline, every quotation matches its speaker and the source's exact words, and every figure is cited to the page that states it. One title could not be confirmed: Google *Long context* (redirect).

## Length
The body is about 6,450 words against a 2,000–6,000-word guide; I found no padding to cut. The deliverable is about 7,900 words. Its largest repetition is in templates 3 and 9, whose worked examples repeat the template with UNKNOWN in place of FILL. The brief requires a worked example for each template, so this is not a fault, but it is the first place to cut once the case file gains the real texts.

BW3 · fix · 0 error, 8 should-fix, 11 minor
