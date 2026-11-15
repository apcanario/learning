---
audit: fresh check
unit: BW4 · Context engineering
course: building-with-ai · Building with AI
model: claude-opus-5-5
date: 2026-11-15
chat: https://claude.ai/code/session_01KMmgQzjvLSGBCfKL6ycyBm
verdict: fix · 2 errors, 5 should-fix, 5 minor
---

The checker's final report, verbatim, from its hand-back. Saved before any finding was applied.

Verdict: BW4 · fix · 2 error, 5 should-fix, 5 minor

Model: claude-opus-5-5. The harness refused the report file (out/report.md), so the full report follows.

# BW4 · Context engineering · fresh check

I am a separate context and did not see the unit written. Packet: unit.md, brief.txt, notes.md, unsure.md, case-academy.md, sourcing-standard.md. Live search was on. Every web source below was reached by a search in this agent on 15 Nov 2026.

## (1) Coverage

- **Layers and what belongs in each** (instructions, knowledge files, memory, skills, tools and connectors, scheduled tasks): covered in §1. Memory rests on BW1 §3, and the unit says so.
- **Every turn against on demand, and the cost of each:** covered in §2. Auto, the default connector mode, is missing (should-fix 2).
- **Retrieval:** covered in §3.
- **New chat or not:** covered in §4.
- **One source of truth and its mirrors:** covered in §5.
- **Rot and early signs:** covered in §6.
- **The Academy structure audit and its seventeen findings:** thin. The case file names only two of the seventeen; the unit says so and works those two. The gap is in the case file, not the writing (notes, Needs 1).
- **Deliverable:** covered. It has folders, a 400-word instruction file, an index, a what-goes-where table and a six-step rot check. The steps add up to 2+3+3+3+2+2 = 15 minutes. It is built on the case and then given as templates.
- **On other tools:** present, but six cells say "Not checked" (should-fix 4 and 5).

## Findings

[error] [figure] §3, flow figure; Current: "{"label": "In the documents", "note": "missing content", "tone": 1},"; Problem: these labels are not in the unit's text: the stage labels "In the documents", "Ranked by search", "Placed in the window", "Read by the model" and "Written as the answer", and the paper's names "missing content", "missed the top-ranked documents" and "incorrect specificity". The text describes the failure points in its own words and never uses the paper's names. Fix: "apply should-fix 1 (which puts the names into §3), then replace the whole "steps" array with: "steps": [ {"label": "Missing content", "note": "not in the documents at all", "tone": 1}, {"label": "Missed the top-ranked documents", "note": "ranked too low to be returned", "tone": 1}, {"label": "Not in context", "note": "dropped when the passages are consolidated", "tone": 1}, {"label": "Not extracted", "note": "the model fails to extract it", "tone": 4}, {"label": "In the answer", "note": "wrong format; incorrect specificity; incomplete", "tone": 3} ]. In the caption, change "the grouping into five stages is this unit's" to "the grouping into five steps is this unit's""; Basis: Barnett et al., arXiv:2401.05856v1, FP1–FP7, https://arxiv.org/html/2401.05856v1

[error] [figure] §6, states figure; Current: "Every file has a life, and rot is a file that has reached its end and is still in the project."; Problem: the figure uses words that §6 does not hold. The transitions "adopted" and "moved out" and the note "listed in the index" are not in §6. "Draft", "Current", "Superseded" and "Archived" appear only in the Part 3 template. Fix: "Every file has a life: it is drafted, adopted as current and listed in the index, replaced and so superseded, then moved out to the archive, out of every layer. Rot is a superseded file that is still in the project."; Basis: sourcing-standard Part 1, figure rule. (The JSON then passes unchanged.)

[should-fix] [accuracy] §3, item 3; Current: "name seven failure points; four happen before the model writes anything"; Problem: the paper defines FP4 "Not Extracted" as the answer being in the context while the LLM fails to extract it. That is a failure inside the model, so only three of the seven happen upstream. "Four happen before the model writes anything" stretches the source. Fix: "name seven failure points. Three happen before the model reads anything: the answer is not in the documents at all (missing content), it is in them but ranked too low to be returned (missed the top-ranked documents), or it is returned but dropped when the passages are consolidated (not in context). The fourth happens in the model: the answer is in the window and the model fails to extract it (not extracted). The other three are in the answer: a wrong format, an answer too general or too narrow (incorrect specificity), and an incomplete answer."; Basis: https://arxiv.org/html/2401.05856v1 (replace the span from that phrase through "and an incomplete answer.")

[should-fix] [coverage] §2, "When matched or searched"; Current: "connectors in On demand mode; memory and chat search as the app chooses."; Problem: §2 says its three ways "cover every layer in §1", but it omits Auto, the default connector mode documented in §1. The matrix figure omits it too. Fix: "connectors in Auto mode (the default) as Claude decides, and in On demand mode when searched for; memory and chat search as the app chooses." In the matrix, change {"mark": "On demand", "tone": 4} to {"mark": "Auto, On demand", "tone": 4}; Basis: Claude Help Center, Manage Claude's tool access (16 Mar 2026), https://support.claude.com/en/articles/13730515-manage-claude-s-tool-access

[should-fix] [coverage] §8 table; Current: "| Instruction file for a coding agent; imports load at launch (§5) |"; Problem: the Gemini cell says "Not checked", but Gemini CLI documents an equivalent. Fix: change that row's last cell to "GEMINI.md files are concatenated and sent with every prompt; `@file.md` imports split a large file: [*Provide context with GEMINI.md files*](https://geminicli.com/docs/cli/gemini-md/) (Gemini CLI docs, read 15 Nov 2026)", and add the page to Sources. Leave the ChatGPT cell: OpenAI's AGENTS.md page redirected and was not checked; Basis: https://geminicli.com/docs/cli/gemini-md/

[should-fix] [coverage] §8 table; Current: "| Connector loading modes (§1) |"; Problem: five more cells say "Not checked": connectors for both vendors, ChatGPT scheduled tasks, the ChatGPT instruction file, and the GitHub mirror for both vendors. The brief requires either a citation or "no equivalent found". Fix: in the corrections pass, search each cell and cite the page, or write "No equivalent found in the vendor's documentation searched on [date]"; Basis: brief.txt; sourcing-standard Part 6.

[should-fix] [attribution] Deliverable Part 1, note under the instruction file; Current: "(§2: one context per unit, briefs never reworded, the writer's own pass, the fresh check, the model recorded;"; Problem: rule 3's first sentence ("Every cited claim is sourced where it is made") comes from case file §1 ("sources cited in place"), not §2. Fix: "(§1: sources cited in place; §2: one context per unit, briefs never reworded, the writer's own pass, the fresh check, the model recorded;"; Basis: Academy case file §1, §2.

[minor] [attribution] §5; Current: "(Hunt and Thomas, *The Pragmatic Programmer*, Addison-Wesley, 1999;"; Problem: there is no locator, and the book was not opened (unsure 3). Fix: "(Hunt and Thomas, *The Pragmatic Programmer*, Addison-Wesley, 1999, section "The Evils of Duplication"; not opened for this unit;"; Basis: sourcing-standard Part 1 (locator).

[minor] [style] §1; Current: "move it to a skill or a path-scoped rule ([Anthropic"; Problem: "path-scoped rule" is unexplained for a reader who may not write code. Fix: "move it to a skill or a path-scoped rule (an instruction file that applies only to one folder) ([Anthropic"; Basis: https://code.claude.com/docs/en/memory

[minor] [label] §7; Current: "That is the argument for a scheduled check over vigilance."; Problem: this is an inference from one anecdote, with no evidence grade. Fix: "That is the argument for a scheduled check over vigilance (stated opinion)."; Basis: sourcing-standard Part 6.

[minor] [style] opening; Current: "This unit was written with search off. Searches were used only to re-verify each source it cites"; Problem: this is the private course's process language. This course's brief asks writers to search for current facts, so "search off" reads to this reader as a contradiction. Fix: "Every source was re-read on 15 November 2026"; Basis: brief.txt

[minor] [style] §3; Current: "**Failures move upstream of the model.**"; Problem: after should-fix 1, only three of the seven failure points are upstream. Fix: "**Failures start upstream of the model.**"; Basis: arXiv:2401.05856v1

## (7) Figures

1. **matrix, §2: PASS.** Every label is in §2's text:
   - "each skill's name and description" and "A skill's body"
   - "while the project is small" and "once the project is in retrieval mode"
   - "Always available" and "On demand"
   - "memory and chat search as the app chooses"
   - "reads a file by path"

   The caption names the section and the sources. The kind fits (items by sections). If should-fix 2 is applied, update the On demand cell as given there.
2. **flow, §3: FIX.** See error 1; the replacement JSON is given there. The kind fits (a sequence).
3. **states, §6: FIX.** See error 2; it is a text fix. The kind fits (a lifecycle).
4. **flow, Deliverable Part 2: PASS.** The six step labels and the times 2/3/3/3/2/2 match steps 1–6. The caption names Part 2 and gives the grade.

## Confirmed

All read 15 Nov 2026.

- **Personalization features:** "applied to all of your conversations with Claude" and "only apply to chats within that project". The two can be used "independently or in combination", and no precedence is stated. https://support.claude.com/en/articles/10185728-understanding-claude-s-personalization-features
- **How can I create and manage projects?:** files are "used across all of your chats within that project". "Context is not shared across chats within a project" (the sentence goes on "unless … added into the project knowledge base"; the unit's "otherwise" covers this). https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects
- **Agent Skills:** metadata always loaded at startup, about 100 tokens a skill; instructions under 5k tokens; resources cost nothing until accessed. https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview
- **What are skills?:** "static background knowledge that's always loaded", "Custom instructions apply broadly" and "task-specific and only load when relevant". https://support.claude.com/en/articles/12512176-what-are-skills
- **Manage Claude's tool access:** dated March 16, 2026; "Each connector takes up space in a conversation."; Auto is the default; the Always available and On demand descriptions match; On demand is recommended when conversations hit length limits. https://support.claude.com/en/articles/13730515-manage-claude-s-tool-access
- **Automate work with scheduled tasks:**
  - The task is "formerly a routine", and is a prompt plus repositories plus connectors.
  - Each repository is cloned at the start of a run, and each run gets a new session.
  - The prompt "must be self-contained and explicit about what to do and what success looks like".
  - Connectors are included by default.
  - Schedules more often than hourly are rejected.
  - The feature is in research preview.
  - The work it suits: "unattended, repeatable, and tied to a clear outcome".

  https://code.claude.com/docs/en/web-scheduled-tasks
- **How Claude remembers your project:**
  - "Keep it to facts Claude should hold in every session"
  - "skill or a path-scoped rule instead"
  - "not a hard enforcement layer"
  - "does not reduce context, since imported files load at launch"
  - "if two rules contradict each other, Claude may pick one arbitrarily"
  - "periodically to remove outdated or conflicting instructions"
  - "target under 200 lines"
  - "build commands, conventions, project layout"

  https://code.claude.com/docs/en/memory
- **Effective context engineering for AI agents:** by Rajasekaran, Dixon, Ryan and Hadfield, Sep 29, 2025, "Written by Anthropic's Applied AI team". All the quoted phrases are on the page. https://anthropic.com/engineering/effective-context-engineering-for-ai-agents
- **Usage limit best practices:** both cache sentences are on the page, and nothing is said about whether a new chat keeps the cache. https://support.claude.com/en/articles/9797557-usage-limit-best-practices
- **How do usage and length limits work?:** the headline is confirmed, which resolves unsure 1. The cleanup advice is there, and so are the 1M / 500K / 200K windows on paid plans. https://support.claude.com/en/articles/11647753-understanding-usage-and-length-limits
- **Retrieval augmented generation (RAG) for projects:** "approaches the context window limit"; capacity "up to 10x"; "Claude can automatically convert back to context-based processing"; Pro, Max, Ultra, Team and Enterprise; no threshold is published. https://support.claude.com/en/articles/11473015-retrieval-augmented-generation-rag-for-projects
- **Use the GitHub integration:** "Sync now"; refresh "periodically"; "must fit within Claude's context window"; selected files go into project knowledge. https://support.claude.com/en/articles/10167454-use-the-github-integration
- **GitHub Docs, Removing sensitive data from a repository:** clones or forks, SHA-1 hashes in cached views, and pull requests are all named. https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository
- **Barnett et al.:**
  - The five authors are as listed.
  - The three cases are research, education and biomedical.
  - "validation of a RAG system is only feasible during operation"
  - GPT-4 generated the BioASQ answers.
  - The venue is the 3rd International Conference on AI Engineering (CAIN), April 2024.

  PASS except the FP4 point (should-fix 1). https://arxiv.org/abs/2401.05856v1
- **Brysbaert 2019:** 190 studies; 18,573 participants; 238 wpm for non-fiction; JML 109, 104047. https://bibbase.org/network/publication/brysbaert-howmanywordsdowereadperminuteareviewandmetaanalysisofreadingrate-2019
- **Jaroslawicz et al.** (cited via BW3 §2): 20 models; about 68% at 500 instructions; a bias toward earlier instructions; an arXiv preprint. https://arxiv.org/abs/2507.11538
- **Models overview** (cited via BW1 §2): "1M tokens is roughly 555k words or 2.5M Unicode characters on the current tokenizer". The unit's 1.8 tokens a word follows. https://platform.claude.com/docs/en/about-claude/models/overview.md
- **OpenAI Academy, Using projects** (April 10, 2026): a project holds chats, files and instructions; project-only memory exists; no precedence is stated. https://openai.com/academy/projects
- **OpenAI Academy, Using skills** (April 10, 2026): a skill's name and description "Help ChatGPT recognize when the skill is relevant". https://openai.com/academy/skills
- **Gemini, Organize your projects with notebooks in Gemini Apps:** a notebook keeps sources, instructions and discussions; up to 600 sources, by plan. https://support.google.com/gemini/answer/16972047?hl=en
- **Gemini, About the transition from Gems to skills:** personal accounts 18+; read-only 17 Nov 2026; removed 17 Dec 2026; skills are "reusable custom instructions". https://support.google.com/gemini/answer/18560919?hl=en
- **Gemini, Schedules in Gemini Apps:** the headline is confirmed; "up to 10 active schedules at a time". https://support.google.com/gemini/answer/16316416?hl=en-GB
- **Academy case facts** in §4, §5, §7 and the Deliverable all match case-academy.md §1, §2, §6, §7 and §9. The "(Academy case)" label appears at first use (§4), and the case is labelled an anecdote in §4, §5 and §7.
- **Instruction text:** 222 words by whitespace count, as the unit says.
- **Unverifiable:**
  - Chroma's 18-model distractor finding (via BW1 §2): the page redirected and the retry was refused.
  - Laban et al. (via BW3 §5): not checked.

## (3) Figures say whose

Yes. Every number names its source or is labelled this unit's arithmetic or budget.

## (4) Labels

Vendor sources are labelled vendor and dated. Barnett is labelled peer-reviewed, Jaroslawicz a preprint and Chroma vendor research. The case is labelled an anecdote. One ungraded line remains (§7, minor).

## (5) Deliverable

It is in full: built on the case with `[NOT IN CASE FILE]` blanks, then given as templates whose blanks say what goes in them. It follows from §1–§7, the limits and timings are graded stated opinion, and it can be used on its own.

## (6) Errata and pointers

No audit report was in the packet. BW1, BW3, BW5 and BW8 were not in the packet, so the pointers to them could not be checked. The pointers to the case file hold.

## (8) Writer's Source errors list (notes.md)

1. Confirmed: 11647753 gives 1M/500K/200K windows.
2. Confirmed: Models overview gives 2.5M characters per 1M tokens, and 11647753 gives the windows.
3. Confirmed: the page says "two rules contradict".
4. Confirmed: the audit list is absent from the page, and the "periodically" sentence is there.
5. Confirmed: the quotation stops before "or a path-scoped rule instead".
6. Confirmed: the page says "formerly a routine".
7. Confirmed: the headline is "How do usage and length limits work?".
8. Confirmed: 2.5 characters per token.

The Contradictions item (the BW1 §8 connector row) is also confirmed against Manage Claude's tool access.

## (9) Part 6, line by line

- Every claim with a number, mechanism or recommendation is sourced where it is made: yes.
- Source types are labelled: yes.
- Evidence grades: yes, except §7's last line (minor).
- Each study names its models and task, and transfers are marked as the unit's inference: yes.
- Product facts are dated: yes.
- "On other tools": present, but six cells say "Not checked" (should-fix 4 and 5).
- Claims carried over from the private course were re-verified: yes, and they hold.
- Private reader or private course: none. A grep for "B4", "Pedro", "Learning Project" and "Fable" finds nothing.
- Academy facts come from the case file, cited and labelled: yes.
- Nothing invented: none found.
- Deliverable on the case, then as a template: yes.
- Not advice without evidence: passes.
- Links given as links: yes; the one exception is the book by Hunt and Thomas.

## (10) Read as the brief's reader

The unit assumes nothing that only the private course's reader would know. These are the snags for this reader:

- "path-scoped rule" is unexplained (minor above).
- "force-push", "clones or forks" and "hashes" in §7 are jargon, though the point survives without them.
- "deep dive" (§4) relies on the course's DD units.
- The opening "written with search off" is process language (minor above).

BW4 · fix · error 2, should-fix 5, minor 5
