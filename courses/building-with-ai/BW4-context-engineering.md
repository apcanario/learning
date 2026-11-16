---
code: BW4
title: Context engineering
course: building-with-ai
model: Opus 5.5
written: 2026-11-15
search: off
---

# BW4 · Context engineering

The web sources this unit cites were re-read on 15 November 2026 (exceptions are in the Unsure list), and every product fact (a limit, a feature, a setting) carries that reading date; most help-centre pages show no exact date of their own. Each practice carries an evidence grade, as in BW1 to BW3: **measured** (a study or test with numbers), **documented practice** (a vendor or a named practitioner says to do it; nobody measured it here) or **stated opinion**. What a context window is, why every turn re-sends the whole chat, what persists between chats and why no instruction layer is enforced are in BW1 (§1, §2, §3, §6); when a drifting conversation should be restarted is BW3 §5. This unit assumes both and turns to the project around the chat: which layer holds what, what each costs, and how to keep the whole from going stale.

## 1 · The layers a project offers, and what belongs in each

BW1 §8 mapped the layers of a current assistant by what they put in the window. Here the question is the next one: given how each layer reaches the window, what should you put in it. The table states the answer for Claude; the paragraphs under it give the evidence, layer by layer (all read 15 Nov 2026).

| Layer | Reaches | Enters the window | What belongs there | What does not |
|---|---|---|---|---|
| Account-wide instructions | Every chat on the account | Every turn | Rules about you that hold in every project: register, format habits | Anything true of one project only |
| Project instructions | Every chat in one project | Every turn | The few rules every chat in the project must obey, and where everything else is | Procedures, lists that change, copies of other files |
| Project knowledge (files) | Every chat in one project | Whole while small; searched once the project nears the window limit | Reference every chat needs whole: the rules, the map, the current queue | Records, superseded drafts, anything a chat can be pointed to when it needs it |
| Memory | Account, plus one store per project | As the app inserts it; how much is not stated | Facts about you that come up unprompted | Rules, and anything already in a file |
| Skills | Account (claude.ai); a machine or a repository (Claude Code: [*Extend Claude with skills*](https://code.claude.com/docs/en/skills), read 16 Nov 2026) | Name and description every turn; body when a request matches | One procedure for one kind of task | Facts and standing rules |
| Connectors and tools | Account | By setting: at the start, by Claude's choice, or when searched for | Live access to a service a task uses | Services no task in the project uses |
| Scheduled tasks | Account | Their own session, run by run | Unattended, repeatable jobs with a clear outcome | Work that needs a judgement mid-run |

The "Reaches" and "Enters" columns are documented; the last two columns are this unit's synthesis of the sources below (stated opinion).

**Account-wide and project instructions.** Anthropic's help centre says instructions set in your profile are "applied to all of your conversations with Claude", that project instructions "only apply to chats within that project", and that the two can be used independently or in combination; it states no order of precedence between them ([Claude Help Center, *Understanding Claude's personalization features*](https://support.claude.com/en/articles/10185728-understanding-claude-s-personalization-features), read 15 Nov 2026; vendor). BW1 §6 drew the consequence: a rule written in both is paid for twice, and two rules that disagree leave the model to settle it with no documented rule. So a project's exceptions to your account-wide habits have to be written into the project's own instructions (§6).

**Project knowledge.** Files uploaded to a project are used across all its chats, and the same page says context is otherwise "not shared across chats within a project" ([Claude Help Center, *How can I create and manage projects?*](https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects), read 15 Nov 2026; vendor). Whether a file arrives whole depends on the project's size, which is §3.

**Memory.** BW1 §3 gives what memory stores and where: each project has its own memory, used beside your memory from chats outside projects, and the help centre does not say how much of it enters a given chat (BW1 §3, read there 15 Nov 2026). The page on memory refused the fetch for this unit, so nothing about memory is added here beyond BW1. What follows for structure is an inference: memory is text a model wrote about your chats, so it is the wrong home for a rule you need held exactly (stated opinion).

**Skills.** Anthropic's developer documentation gives the loading rule in three levels: a skill's metadata is loaded always, at startup, at about 100 tokens a skill; its instructions load when the skill is triggered, at under 5,000 tokens; its bundled resources cost nothing until accessed ([Anthropic, *Agent Skills*](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview), read 15 Nov 2026; vendor). The help centre draws the boundary in one line each: projects hold "static background knowledge" that is "always loaded", custom instructions apply broadly, and skills are "task-specific and only load when relevant" ([Claude Help Center, *What are skills?*](https://support.claude.com/en/articles/12512176-what-are-skills), read 15 Nov 2026; vendor). Writing a skill well is BW8.

**Connectors.** "Each connector takes up space in a conversation." Three modes are documented: in Auto, the default, Claude decides which connectors to load from what you are working on; in Always available, every connector loads at the start of every conversation; in On demand, a connector is not loaded until Claude searches for it from your request. The same page recommends On demand when conversations hit length limits ([Claude Help Center, *Manage Claude's tool access*](https://support.claude.com/en/articles/13730515-manage-claude-s-tool-access), dated 16 Mar 2026, read 15 Nov 2026; vendor).

**Scheduled tasks.** In Claude Code, a cloud scheduled task (the feature was formerly called routines) is a saved configuration of a prompt, one or more repositories and a set of connectors; each repository is cloned at the start of every run, each run opens as a new session, and the prompt "must be self-contained and explicit about what to do and what success looks like". All your connectors are included by default unless you remove them; schedules more frequent than hourly are rejected; the feature is in research preview ([Anthropic, *Automate work with scheduled tasks*](https://code.claude.com/docs/en/web-scheduled-tasks), read 15 Nov 2026; vendor). The page describes the work it suits as "unattended, repeatable, and tied to a clear outcome". A scheduled run knows nothing of the chat that created it (BW1 §3): everything it needs has to be in the prompt or in the repository.

**The rule that sorts them.** Claude Code's documentation states the dividing rule for its own instruction file, `CLAUDE.md`: keep it to facts Claude should hold in every session, and if an entry is a multi-step procedure or only matters for one part of the work, move it to a skill or a path-scoped rule (a rule file that applies only when Claude works on files matching the paths it names) ([Anthropic, *How Claude remembers your project*](https://code.claude.com/docs/en/memory), read 15 Nov 2026; vendor, written for Claude Code). The page also says such instructions are context and "not a hard enforcement layer" (same page). Applying the rule to claude.ai's project instructions is this unit's inference, on the ground BW1 §6 gives: every layer reaches the model the same way, as text in the window. Grade: documented practice for Claude Code; stated opinion for the transfer.

## 2 · What loads every turn, what loads on demand, and what each costs

Three ways into the window cover every layer in §1.

- **Every turn.** Account-wide and project instructions, each skill's name and description, connectors in Always available mode, and project files while the project is small. Paid for on every turn of every chat.
- **When matched or searched.** A skill's body when a request matches its description; project files once the project is in retrieval mode; connectors in Auto mode (the default) as Claude decides, and in On demand mode when searched for; memory and chat search as the app chooses.
- **When named.** A file in a folder or repository that a chat reads because you, or the brief, gave its path.

The labels are this unit's. Anthropic's Applied AI team describes the same choice as context loaded up front against context retrieved "just in time": an agent can keep "lightweight identifiers" such as file paths and load the data behind them when it needs it, and a hybrid strategy retrieves some data up front for speed and leaves the rest to exploration. Its worked example is Claude Code, where `CLAUDE.md` files are "naively dropped into context up front" while search tools let it "retrieve files just-in-time" ([Rajasekaran, Dixon, Ryan and Hadfield, *Effective context engineering for AI agents*, Anthropic, 29 Sep 2025](https://anthropic.com/engineering/effective-context-engineering-for-ai-agents), read 15 Nov 2026; vendor; documented practice).

```viz
{
  "kind": "matrix",
  "caption": "When each layer of a Claude project enters the context window, by the three ways named in §2 of this unit (the labels are this unit's). Two layers change column with a setting or a size: connectors by tool-access mode (Claude Help Center, Manage Claude's tool access) and project files at the retrieval switch (Claude Help Center, Retrieval augmented generation (RAG) for projects); skills from Anthropic, Agent Skills. All read 15 Nov 2026, as cited in §1 and §3.",
  "cols": ["Every turn", "When matched or searched", "When named"],
  "rows": [
    {"label": "Account-wide instructions", "cells": ["●", null, null]},
    {"label": "Project instructions", "cells": ["●", null, null]},
    {"label": "Skill name and description", "cells": ["●", null, null]},
    {"label": "Skill body", "cells": [null, "●", null]},
    {"label": "Project files", "tone": 4, "cells": [{"mark": "while small", "tone": 4}, {"mark": "retrieval mode", "tone": 4}, null]},
    {"label": "Connectors", "tone": 4, "cells": [{"mark": "Always available", "tone": 4}, {"mark": "Auto, On demand", "tone": 4}, null]},
    {"label": "Memory and chat search", "cells": [null, "●", null]},
    {"label": "Files in a folder or repository", "cells": [null, null, "by path"]}
  ],
  "legend": [{"mark": "●", "means": "the column §2 gives this layer"}]
}
```

Each way of loading has a cost of a different kind.

**Every turn costs tokens and attention.** Every turn re-sends the whole window (BW1 §2), so a standing layer is paid once per turn. Illustrative arithmetic, unmeasured: Anthropic's model page gave 1M tokens as roughly 555,000 words for its current tokenizer (BW1 §2, read there 15 Nov 2026; not on the page on 16 Nov 2026), about 1.8 tokens a word; a 400-word instruction is then about 720 tokens, and over a 30-turn chat about 21,600 tokens of input, before anything else is counted. Twenty installed skills add about 2,000 tokens a turn on Anthropic's per-skill figure (BW1 §6). On claude.ai the cost is softened: "Content in projects is cached and counts less against your limits when reused", and "Caches expire after a period of inactivity" ([Claude Help Center, *Usage limit best practices*](https://support.claude.com/en/articles/9797557-usage-limit-best-practices), read 15 Nov 2026; vendor). Caching lowers what the text costs against your limit. Nothing on the page says it lowers the attention the text draws (BW1 §2). What it buys: certainty that the text is there.

**On demand costs reliability.** A skill body, a retrieved passage or a connector arrives only if a description matches or a search finds it. Skills fire on their description alone (BW1 §6); retrieval returns passages, which is §3. What it buys: a window that carries nothing until it is needed. A procedure that fires on a recognisable request belongs here; a rule that must hold in every chat does not.

**By name costs a deliberate fetch.** A chat that reads a file by path spends one tool call, and the file then sits in the window for the rest of the chat (BW1 §8). What it buys: nothing arrives that the chat did not ask for, and the map of what exists (an index of paths, §5) can be small enough to load every turn.

The working rule (stated opinion, on the sources above): put in the every-turn layers only what every chat must obey whole; put procedures where they load on a match; leave everything else in files a chat is pointed to by name.

## 3 · What happens to a large knowledge set

Project knowledge does not stay whole as it grows. Anthropic's help centre says that when project knowledge "approaches the context window limit", Claude automatically enables retrieval mode (retrieval-augmented generation, RAG): it uses a project knowledge search tool to retrieve relevant information from the uploaded documents, which lets a project hold up to ten times more; when the knowledge drops below the threshold again, "Claude can automatically convert back to context-based processing". The feature is on paid plans (Pro, Max, Ultra, Team and Enterprise) ([Claude Help Center, *Retrieval augmented generation (RAG) for projects*](https://support.claude.com/en/articles/11473015-retrieval-augmented-generation-rag-for-projects), read 15 Nov 2026; vendor). The page publishes no threshold figure. On paid plans the newest models have windows up to 1M tokens and others 500K or 200K (BW1 §1, read there 15 Nov 2026), so the point at which a project switches depends on the model you chat with, and the page does not say whether it is per model.

Two of Anthropic's own pages then describe project knowledge differently: the skills page says projects hold background knowledge that is "always loaded" ([*What are skills?*](https://support.claude.com/en/articles/12512176-what-are-skills)), the retrieval page says a large project is searched. Read together, "always loaded" holds only below the switch.

**What changes in retrieval mode.** A chat no longer sees your files. It sees the passages a search returned for the request in front of it. Three consequences follow, each an inference from the documented mechanism and the evidence cited (stated opinion where not marked).

1. **A checklist arrives in pieces.** A rule set that only works when every item is checked (a sourcing standard, a definition of done) may arrive as the two items most similar to the request. A file that must be read whole has to sit in a project small enough to load whole, or be read by name.
2. **Old versions compete with new ones.** Search runs over everything in the knowledge. A superseded draft of a file is, by construction, a passage similar to the current one: the kind Chroma's study called a distractor, which lowered accuracy further in its tests of 18 models (BW1 §2; vendor research, measured on models of mid-2025).
3. **Failures start upstream of the model.** Scott Barnett and colleagues, from three retrieval systems they built (in research, education and biomedicine), name seven failure points. Three happen before the model reads anything: the answer is not in the documents at all (missing content), it is in them but ranked too low to be returned (missed the top-ranked documents), or it is returned but dropped when the passages are consolidated (not in context). The fourth happens in the model: the answer is in the window and the model fails to extract it (not extracted). The other three are in the answer: a wrong format, an answer too general or too narrow (incorrect specificity), and an incomplete answer. They conclude that "validation of a RAG system is only feasible during operation" ([Barnett, Kurniawan, Thudumu, Brannelly and Abdelrazek, "Seven Failure Points When Engineering a Retrieval Augmented Generation System", CAIN 2024; arXiv:2401.05856](https://arxiv.org/abs/2401.05856); peer-reviewed experience report; in the biomedical case the answers were generated by GPT-4). Their systems were built by engineers who chose the search; in a claude.ai project the search is the vendor's and you cannot inspect it, so the points are a checklist of where to look, not a measurement of your project (this unit's inference).

```viz
{
  "kind": "flow",
  "caption": "Where a retrieved answer can fail, in the order a request travels: the seven failure points of Barnett et al., Seven Failure Points When Engineering a Retrieval Augmented Generation System (CAIN 2024; arXiv:2401.05856), as §3 of this unit reports them; the grouping into five steps is this unit's.",
  "steps": [
    {"label": "Missing content", "note": "not in the documents at all", "tone": 1},
    {"label": "Missed the top-ranked documents", "note": "ranked too low to be returned", "tone": 1},
    {"label": "Not in context", "note": "dropped when the passages are consolidated", "tone": 1},
    {"label": "Not extracted", "note": "the model fails to extract it", "tone": 4},
    {"label": "In the answer", "note": "wrong format; incorrect specificity; incomplete", "tone": 3}
  ]
}
```

**What to do about it** (stated opinion, on the evidence above). Keep the project's every-turn knowledge to the files every chat needs whole, small enough that the project stays below the switch with the model you use most; take superseded versions out of the knowledge, not just out of use; and when an answer matters, name the file in the request, which turns a search into a read. The symptom BW1's diagnosis table lists, a large project answering from the wrong file (BW1, Deliverable Part 3), is the first one to expect.

## 4 · When to start a new chat, and when not to

BW3 §5 gives the restart rule for a drifting conversation: a different task, the same issue corrected twice, requirements changed, or a chat long enough to have been summarised. Each rests on Claude Code's guidance and on Laban and colleagues' measurement that a brief given in pieces does worse than the same brief given whole (BW3 §5). This section adds what project structure changes about that rule.

**A new chat is only as good as what it can find.** Across chats nothing persists except what a layer re-inserts (BW1 §3). So the real question before restarting is where the old chat's state will be read from. Anthropic's Applied AI team calls the habit structured note-taking, with the example of an agent "maintaining a NOTES.md file", and pairs it with sub-agents that take focused tasks "with clean context windows" ([*Effective context engineering for AI agents*](https://anthropic.com/engineering/effective-context-engineering-for-ai-agents), read 15 Nov 2026; vendor; documented practice). In project terms: a chat ends by writing its state into a file the next chat is pointed to, and the next chat starts from that file and the brief, never from the old transcript.

**The case.** In Academy (Academy case), a library of self-study courses built by one person with Claude in October and November 2026 and this course's running example, every chat works one row of a backlog, a finished row moves to a changelog, and each chat ends by writing the prompt for the next (Academy case file §2). Each unit is written in a new chat or a fresh agent context that sees only its brief and the units already filed, for the stated reason that leaked context is how a course starts repeating itself (§2). When writer agents were lost to container restarts, the third writer of one deep dive resumed from the second's working files (§7). One project, an anecdote: it shows the practice run and surviving a lost session, and nothing about whether it beats the alternative, since no unit was written without the method (§9). The case file holds no count of how often a chat was abandoned and its brief rewritten after a miss.

**When not to start a new chat** (stated opinion, built on the sources named in each item).

1. **The next step needs material only this chat holds.** Applying a reviewer's findings to a draft, one by one, needs the current draft and the findings together. A new chat needs both pasted again: the same tokens, plus a chance of pasting the wrong version.
2. **The history is the valuable part.** Claude Code's guide makes this the counter-case to its own restart advice: deep in one complex problem, the accumulated context helps (BW3 §5).
3. **The pause is short.** Project content is cached and counts less against your limits when reused, and the cache expires after inactivity ([*Usage limit best practices*](https://support.claude.com/en/articles/9797557-usage-limit-best-practices), read 15 Nov 2026). Whether a new chat in the same project keeps that cache is not stated on the page; treat any saving as unknown.

Whichever way it goes, the test is the same: could a fresh chat do the next step from the files alone? If not, write the missing state into a file before you leave.

## 5 · One source of truth and its mirrors

A project with more than one copy of a file has to know which copy is right. The rule this unit uses: every piece of content has one canonical home; every other copy is a mirror that names its source, is refreshed by a stated step, and is never edited in place. It restates a principle from software, Andy Hunt and Dave Thomas's DRY ("don't repeat yourself"): every piece of knowledge should have one authoritative representation in a system (Hunt and Thomas, *The Pragmatic Programmer*, Addison-Wesley, 1999, section "The Evils of Duplication"; not opened for this unit; named practitioners; documented practice in software, stated opinion as applied here).

**Where mirrors come from in an assistant project.** Three places, all documented.

- **Project knowledge copied from a folder or repository.** An uploaded file is a copy; it does not change when the original does. Claude's GitHub integration adds selected repository files to project knowledge, and refreshing them is manual: the help page says you can click "Sync now" to fetch the latest changes and asks you to refresh "periodically"; it also requires that the repositories "must fit within Claude's context window" ([Claude Help Center, *Use the GitHub integration*](https://support.claude.com/en/articles/10167454-use-the-github-integration), read 15 Nov 2026; vendor).
- **Instructions pasted from a file.** If the project instructions are also kept as a file, one of the two is the mirror, and nothing syncs them.
- **Anything published.** A website, a shared document or a report built from your files is a mirror that other people read. A mistake in the source reaches it at the next build.

**A pointer beats a copy, with one exception.** Claude Code lets an instruction file import another with `@path`, and its documentation is plain about the cost: imported files load at launch, so splitting into imports "does not reduce context" ([*How Claude remembers your project*](https://code.claude.com/docs/en/memory), read 15 Nov 2026; vendor). An import is still better than a pasted copy, because there is one text to edit. A pointer in prose ("the sourcing rules are in `method/sourcing.md`") is cheaper again: the chat reads the file by name only when it needs it (§2). The exception is a rule every chat must obey whole: it belongs in the every-turn layer, once, and the file version becomes the mirror.

**The case.** Academy keeps everything in one private repository: the course texts, the briefs, the build scripts, the method, a backlog and a changelog; its website is built from the repository by script, and no page is styled by hand (Academy case file §1). Units declare their figures as data and a script draws them (§6). Both are outputs produced from one source by a step, never edited in place. One project, an anecdote; it shows the arrangement can be run by one person.


## 6 · How a project rots, and how to see it early

A project rots when the text the model reads stops matching the work. The brief names three kinds; each has a documented mechanism and an early sign.

**Stale files.** A file that was right when written and was never retired keeps arriving: in the every-turn layers, on every turn; in retrieval mode, as a distractor (§3). Anthropic's usage help page advises regularly cleaning up project files you no longer use ([Claude Help Center, *How do usage and length limits work?*](https://support.claude.com/en/articles/11647753-understanding-usage-and-length-limits), read 15 Nov 2026; vendor). Claude Code's documentation asks you to review its instruction files "periodically to remove outdated or conflicting instructions" ([*How Claude remembers your project*](https://code.claude.com/docs/en/memory), read 15 Nov 2026). Early sign: an answer that follows last month's version of a rule, or cites a file you replaced. Every file has a life: it is drafted, adopted as current and listed in the index, replaced and so superseded, then moved out to the archive, out of every layer. Rot is a superseded file that is still in the project.

```viz
{
  "kind": "states",
  "per_row": 4,
  "start": "draft",
  "caption": "The life of a project file as §6 of this unit describes it (the stages are this unit's): rot is a superseded file still in the project, where it reaches the window every turn or as a retrieval distractor (§3). The archive step is what the monthly rot check in the Deliverable enforces.",
  "states": [
    {"id": "draft", "label": "Draft", "tone": 5},
    {"id": "current", "label": "Current", "note": "listed in the index", "tone": 2},
    {"id": "superseded", "label": "Superseded", "note": "still in the project: rot", "tone": 1},
    {"id": "archived", "label": "Archived", "note": "out of every layer", "tone": 3, "end": true}
  ],
  "transitions": [
    {"from": "draft", "to": "current", "label": "adopted"},
    {"from": "current", "to": "superseded", "label": "replaced"},
    {"from": "superseded", "to": "archived", "label": "moved out"}
  ]
}
```

**Duplicated rules.** A rule written in two places is paid twice where both load every turn, and it drifts the moment one copy is edited. Exact copies can be found by searching for a phrase. Paraphrases cannot, and they are the dangerous kind: two wordings of one rule, with nothing to say which wins (BW1 §6). More rules also cost adherence on their own: in Jaroslawicz and colleagues' test of 20 models, the best reached 68% accuracy at 500 instructions, with a bias towards earlier ones (BW3 §2; preprint, measured on 2025 models). Early sign: the output follows one rule and breaks another (BW1, Deliverable Part 3).

**Instructions that contradict each other.** Claude Code's documentation: "if two instructions contradict each other, Claude may pick one arbitrarily" ([*How Claude remembers your project*](https://code.claude.com/docs/en/memory), read 15 Nov 2026; vendor, written for Claude Code). On claude.ai no precedence between account-wide and project instructions is documented (§1), so the Claude Code sentence is the nearest documented description; applying it there is this unit's inference. The commonest collision is between layers written at different times for different purposes: an account-wide habit (short answers, bullets, a preferred output container) against a project's need (a long report, a file in a folder). Early sign: the format changes from one chat to the next with no change in the request.

**Seeing it early** (stated opinion, on the mechanisms above). Rot accumulates between sessions, and nobody reads a file to look for it. Two things catch it: the symptoms in BW1's diagnosis table, noticed as they happen (one rule followed and another broken; a large project answering from the wrong file; two of your own files giving different values), and a short check on a fixed day. The Deliverable's rot check takes fifteen minutes a month. Its steps are mechanical enough that BW8 automates them.

## 7 · The Academy case's structure audit

A structure audit of the Academy project itself made seventeen findings (Academy case file §7). The case file names two of them: project instructions that carried procedures and paraphrased the method file, and private terms reaching a public build (§7). It does not list the other fifteen, so this unit works through the two it names. One project, one audit: an anecdote, which illustrates the mechanisms in §1 to §6 and is evidence of nothing beyond itself.

**Instructions that carried procedures and paraphrased the method file.** Two faults from §1 and §6 in one layer. Procedures in project instructions load on every turn whether the task needs them or not, where Claude Code's own rule sends a multi-step procedure to a skill (§1). A paraphrase of the method file is the duplicate no phrase search finds: the method says it one way, the instructions another, and the model reads both with no rule for which wins (§6; BW1 §6). The fix the rule implies is this unit's (stated opinion): the instructions keep the rules every chat must obey, in the words of their one home, and point to the method for the rest.

**Private terms reaching a public build.** A mirror fault (§5). The site is built from the repository by script (Academy case file §1), so anything in the repository that the build reads reaches the published site at the next build. A rule about what goes into the texts does not check what the build renders; only a check on the output does (stated opinion). For anything pushed to a repository on GitHub, taking a term out later is harder than keeping it out: GitHub's documentation warns that if you only rewrite your history and force-push, the commits with the sensitive data may still be reachable in clones or forks, through their hashes in cached views, and through pull requests that reference them ([GitHub Docs, *Removing sensitive data from a repository*](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository), read 15 Nov 2026; vendor). A check that would catch it is a search of the built output for a list of private terms before publishing; it is step 6 of the rot check below. The case file does not say how the finding was found or fixed.

Both findings are of the kinds §6 predicts, and neither is visible from inside a single chat: each shows only when two files, or a file and its mirror, are read side by side. That is the argument for a scheduled check over vigilance (stated opinion).

## 8 · On other tools

The principles in §1 to §7 (layers that load every turn or on demand, retrieval as selection, a new chat that is only as good as its files, one source of truth, rot as stale, duplicated or contradictory text) hold for any current assistant: each follows from the window mechanism in BW1. The detail is Claude's. Below, each Claude-specific claim with the equivalent where the other vendor's own documentation was found, all read 15 Nov 2026. OpenAI's help-centre pages on projects, on connectors, on connecting GitHub and on scheduled tasks failed to load and were not checked; the ChatGPT column rests on two OpenAI Academy pages.

| Claim in this unit | Claude | ChatGPT (OpenAI) | Gemini (Google) |
|---|---|---|---|
| Account-wide and project instructions; no documented precedence (§1) | [*Personalization features*](https://support.claude.com/en/articles/10185728-understanding-claude-s-personalization-features) | A project holds chats, files and instructions; precedence against account-wide instructions not stated: [*Using projects in ChatGPT*](https://openai.com/academy/projects) (10 Apr 2026) | A notebook keeps its sources, instructions and chat; precedence not stated: [*Organize your projects with notebooks in Gemini Apps*](https://support.google.com/gemini/answer/16972047?hl=en) |
| Large project knowledge switches to retrieval (§3) | [*RAG for projects*](https://support.claude.com/en/articles/11473015-retrieval-augmented-generation-rag-for-projects) | How project files are searched is not stated on the page read | Up to 600 sources, by plan; how they enter a chat is not stated: [*Organize your projects with notebooks*](https://support.google.com/gemini/answer/16972047?hl=en) |
| Per-project memory (§1, via BW1 §3) | BW1 §3 | Project-only memory keeps chats to the project's own conversations: [*Using projects in ChatGPT*](https://openai.com/academy/projects) | No equivalent found in the pages read |
| Skills: description loaded, body on a match (§1, §2) | [*Agent Skills*](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview) | A skill's name and description help ChatGPT recognise when to use it: [*Using skills*](https://openai.com/academy/skills) (10 Apr 2026) | Skills, reusable custom instructions applied when relevant; on personal accounts (users 18 and over) Gems become read-only on 17 Nov 2026, are removed on 17 Dec 2026 and move to skills: [*About the transition from Gems to skills*](https://support.google.com/gemini/answer/18560919?hl=en) |
| Connector loading modes (§1) | [*Manage Claude's tool access*](https://support.claude.com/en/articles/13730515-manage-claude-s-tool-access) | Not checked: the help-centre page on connectors found by search on 15 Nov 2026 failed to load | On work or school accounts, Gemini Apps automatically use an app the Workspace administrator has enabled, and you can select one by typing `@` in the prompt box: [*Use apps connected to Gemini with a work or school Google Account*](https://support.google.com/gemini/answer/14959807?authuser=2) (Gemini Apps Help, read 15 Nov 2026) |
| Scheduled tasks (§1) | [*Automate work with scheduled tasks*](https://code.claude.com/docs/en/web-scheduled-tasks) | Not checked: the help-centre page on scheduled tasks found by search on 15 Nov 2026 failed to load | Recurring scheduled actions, up to 10 active at a time: [*Schedules in Gemini Apps*](https://support.google.com/gemini/answer/16316416?hl=en-GB) |
| Instruction file for a coding agent; imports load at launch (§5) | [*How Claude remembers your project*](https://code.claude.com/docs/en/memory) | Not checked for this unit | GEMINI.md files are concatenated and sent to the model with every prompt; `@file.md` imports break a large file into smaller components; the page notes that Gemini CLI was replaced by Antigravity CLI on 18 June 2026: [*Provide context with GEMINI.md files*](https://geminicli.com/docs/cli/gemini-md/) (Gemini CLI docs, updated 18 Jun 2026, read 15 Nov 2026) |
| Repository mirrored into project knowledge, refreshed by hand (§5) | [*Use the GitHub integration*](https://support.claude.com/en/articles/10167454-use-the-github-integration) | Not checked: the help-centre page on connecting GitHub found by search on 15 Nov 2026 failed to load | One repository per chat, up to 5,000 files and 100 MB; changes to the repository aren't synced to Gemini: [*Import a GitHub repository & ask about it in the Gemini web app*](https://support.google.com/gemini/answer/16176929?hl=en) (Gemini Apps Help, read 15 Nov 2026) |

The research in §3 is not Claude-specific: Barnett and colleagues' biomedical case generated its answers with GPT-4, and the distractor finding in BW1 §2 tested models from several vendors.

## Deliverable · A project structure and a monthly rot check

Four parts. Part 1 is the project-structure template worked on the Academy case: folders, an instruction file with a word limit, an index file and a table of what goes where. Part 2 is the rot check, a fifteen-minute monthly procedure, worked on the same case. Parts 3 and 4 are the same two as templates for your project. BW5 specifies your project into Part 3's structure; BW8 automates Part 4's mechanical steps.

Two rules govern the worked parts. Every fact about Academy comes from the Academy case file and is cited by section. Where the case file does not hold a value the template needs, the cell says `[NOT IN CASE FILE: …]`; those blanks are for the project's owner to fill, and nothing in them is a claim. The layout, file names and rules proposed for the case are this unit's proposal (stated opinion, built on §1 to §7), marked as such.

### Part 1 · Project structure, on the Academy case

**Folders** (this unit's proposal; the contents are the case file's, the names are not).

```
academy/                      the one private repository: source of truth (case file §1)
  INDEX.md                    the map: every file, its status, its layer, its mirror
  INSTRUCTIONS.md             the canonical text of the project instructions (≤ 400 words)
  method/                     the method (case file §2) and the sourcing checklist (§2)
  briefs/<course>/            one brief per unit, never reworded (§2)
  courses/<course>/           filed units (§1)
  build/                      build scripts; the site is built from here (§1)
  records/
    backlog.md                one row per chat (§2)
    changelog.md              finished rows (§2)
    audits/                   fresh checks and audits (§2, §3, §4)
  archive/                    superseded files, out of every layer (§6 of this unit)

private-terms.txt             kept outside the repository: the list step 6 searches for
```

**The instruction file, with its word limit.** Limit: 400 words. Grade: stated opinion. The reasons: the text loads on every turn (§2), about 720 tokens at 400 words on BW1 §2's conversion; the rot check reads it whole, and at 238 words a minute, the average silent reading rate for English non-fiction in Marc Brysbaert's meta-analysis of 190 studies with 18,573 participants ([Brysbaert, "How many words do we read per minute? A review and meta-analysis of reading rate", *Journal of Memory and Language* 109, 2019, 104047](https://doi.org/10.1016/j.jml.2019.104047); peer-reviewed; measured), 400 words take under two minutes; and Claude Code's own target for its instruction file, under 200 lines ([*How Claude remembers your project*](https://code.claude.com/docs/en/memory), read 15 Nov 2026; BW1 §2), is set for a file that also carries build commands, conventions and the project layout. Worked on the case (this unit's proposal; 222 words by a whitespace count):

> **Reader and purpose.** This project writes self-study course units. The reader, goal, sourcing standard and tone are in each brief's shared preamble; use them as written.
>
> **Where things are.** The repository is canonical. `INDEX.md` lists every file with its path and status; read a file by its path when the task needs it. Project knowledge holds only the files `INDEX.md` marks as mirrored.
>
> **Rules for every chat.**
> 1. One unit per chat or fresh agent context. A writer sees only its brief and the units already filed.
> 2. Use the brief as written. Never reword it.
> 3. Every cited claim is sourced where it is made. Before handing in, run the sourcing checklist in `method/` and list up to ten claims you could not verify.
> 4. A checker never sees the unit being written. It reports findings and never edits.
> 5. Record the model that actually wrote each unit.
> 6. Nothing private goes into a unit, a brief or any data the build renders.
>
> **Ending a chat.** Mark the backlog row done, move it to the changelog, and write the prompt for the next row, as `method/` says.
>
> **Where this project departs from my account-wide instructions.** Units and records are Markdown files in the repository, long-form where the brief says so. That overrides any account-wide rule about length, bullets or output containers.

Each numbered rule is the case file's (§1: sources cited in place; §2: one context per unit, briefs never reworded, the writer's own pass, the fresh check, the model recorded; §7: private terms in a public build, as this unit's fix); the last paragraph is this unit's fix for the collision §6 describes.

**The index file** (this unit's proposal; rows are examples, values the case file does not hold are marked).

| Path | What it is | Status | Layer | Mirror and refresh step | Last checked |
|---|---|---|---|---|---|
| `INSTRUCTIONS.md` | Project instructions, canonical text | current | every turn (pasted into the instructions field) | Instructions field; paste after every edit | [NOT IN CASE FILE: date] |
| `method/method.md` | The method (case file §2) | current | by name | [NOT IN CASE FILE: whether mirrored] | [NOT IN CASE FILE: date] |
| `method/sourcing.md` | The sourcing checklist (§2) | current | by name; whole | none | [NOT IN CASE FILE: date] |
| `records/backlog.md` | Queue of chats (§2) | current | by name | none | [NOT IN CASE FILE: date] |
| `build/` | Build scripts (§1) | current | by name | Published site, rebuilt by script (§1) | [NOT IN CASE FILE: date] |
| `archive/…` | Superseded files | archived | none | none | n/a |

**What goes where** (the "should hold" column is this unit's proposal; "holds now" is what the case file records).

| Layer | Should hold, for Academy | Holds now | Reason (section of this unit) |
|---|---|---|---|
| Account-wide instructions | The owner's register and format habits, with no project rule in them | [NOT IN CASE FILE] | §1, §6: one home per rule |
| Project instructions | The 222-word text above | Carried procedures and paraphrased the method file, at the structure audit (case file §7) | §1, §7 |
| Project knowledge | Only files every chat must read whole, below the retrieval switch | [NOT IN CASE FILE: files, size, retrieval mode] | §3 |
| Memory | Nothing the project depends on; rules live in files | [NOT IN CASE FILE: the record does not say whether memory was on, §9] | §1 |
| Skills | One per repeated procedure: writing a unit, checking a unit, filing a unit | [NOT IN CASE FILE] | §1, BW8 |
| Connectors | Only those a procedure uses | [NOT IN CASE FILE] | §1, §2 |
| Scheduled tasks | The mechanical steps of the rot check (Part 2), once BW8 is reached | [NOT IN CASE FILE] | §6, BW8 |
| Repository | Everything else, canonical | Everything: texts, briefs, scripts, method, backlog, changelog (case file §1) | §5 |

### Part 2 · The rot check on the Academy case: fifteen minutes, once a month

Run it on a fixed day, in a new chat or by hand, with the repository open. Record the date and every finding as one changelog row. The times are this unit's budget (stated opinion); they assume the structure in Part 1.

```viz
{
  "kind": "flow",
  "caption": "The monthly rot check of the Deliverable, Part 2, as six steps with this unit's time budget (stated opinion), fifteen minutes in all; each step checks one kind of rot named in §5 and §6 of this unit.",
  "steps": [
    {"label": "1 · Instructions", "note": "2 min", "tone": 2},
    {"label": "2 · Index against folders", "note": "3 min", "tone": 2},
    {"label": "3 · Mirrors", "note": "3 min", "tone": 4},
    {"label": "4 · Duplicated rules", "note": "3 min", "tone": 4},
    {"label": "5 · Contradictions", "note": "2 min", "tone": 1},
    {"label": "6 · Published output", "note": "2 min", "tone": 1}
  ]
}
```

1. **Instructions (2 min).** Read `INSTRUCTIONS.md` whole. Pass if it is at most 400 words, holds no multi-step procedure, and every sentence either states a rule or points to a file. A sentence that restates the method in other words fails. On Academy, this is the step that would have caught the first named audit finding (case file §7). Result: [NOT IN CASE FILE: no run recorded].
2. **Index against folders (3 min).** List the repository's files. Pass if every file is in `INDEX.md`, every entry exists, and no file marked superseded is outside `archive/`. Result: [NOT IN CASE FILE].
3. **Mirrors (3 min).** For each row of `INDEX.md` with a mirror, compare the mirror with its source (the instructions field against `INSTRUCTIONS.md`; each project-knowledge copy against its file, or press "Sync now" if it comes through the GitHub integration, §5). Pass if they match. Result: [NOT IN CASE FILE].
4. **Duplicated rules (3 min).** Take the three rules broken most often this month (from the changelog or the checkers' findings). Search the repository for a key phrase of each and for its subject. Pass if each rule is stated in one file and pointed to everywhere else. Result: [NOT IN CASE FILE].
5. **Contradictions (2 min).** Read the account-wide instructions beside the last paragraph of `INSTRUCTIONS.md`. Pass if every account-wide habit that would collide with the project's output (length, format, container, hand-off) is named there as an exception. Result: [NOT IN CASE FILE].
6. **Published output (2 min).** Search the built site, before publishing, for every term in `private-terms.txt`, which is kept outside the repository so the list itself is never built or pushed. Pass if nothing is found. On Academy, this is the step that would have caught the second named audit finding (case file §7). Result: [NOT IN CASE FILE].

A failed step becomes a backlog row with its fix, worked in its own chat (case file §2). If a fix touches a file that loads every turn, rerun step 1 afterwards.

### Part 3 · Template: your project's structure

Copy, fill every blank, delete what does not apply. Each blank says what goes in it.

**Folders**

```
[project-name]/               [where the canonical copy lives: a folder, a synced drive, a repository]
  INDEX.md                    the map: every file, status, layer, mirror, last checked
  INSTRUCTIONS.md             canonical text of the project instructions, at most 400 words
  [rules folder]/             [the rules your outputs must meet: a style guide, a checklist, a definition of done]
  [inputs folder]/            [briefs, source material, data the work starts from]
  [outputs folder]/           [the finished artefacts: reports, units, posts, code]
  records/                    [the queue of work and the log of what was done, with dates]
  archive/                    superseded files, out of every layer
  [private list, outside the folder]   [terms that must never appear in anything you publish, if you publish]
```

**Instruction file** (at most 400 words)

> **Reader and purpose.** [*one sentence: what this project produces and for whom*]
>
> **Where things are.** [*the canonical location*] is canonical. `INDEX.md` lists every file with its path and status; read a file by its path when the task needs it. Project knowledge holds only the files `INDEX.md` marks as mirrored.
>
> **Rules for every chat.** [*at most eight numbered rules, each one that every chat must obey and that can be checked against the output; a procedure goes in a skill or a rules file, and is pointed to here*]
>
> **Ending a chat.** [*what a chat writes before it ends, and where, so the next chat can start from the file*]
>
> **Where this project departs from my account-wide instructions.** [*each account-wide habit that collides with this project's outputs, named, with what replaces it here*]

**Index file**

| Path | What it is | Status | Layer | Mirror and refresh step | Last checked |
|---|---|---|---|---|---|
| [*file path*] | [*one line*] | [*draft, current, superseded or archived*] | [*every turn, on a match, by name, or none*] | [*where a copy lives and the step that refreshes it, or "none"*] | [*date of the last rot check that read it*] |

**What goes where**

| Layer | What it should hold in your project | What it holds now | Change to make |
|---|---|---|---|
| Account-wide instructions | [*habits that hold in every project*] | [*what is there today*] | [*what moves out or in*] |
| Project instructions | [*the rules every chat must obey, pointers to the rest*] | [*today, with its word count*] | [*cut to 400 words*] |
| Project knowledge | [*only files every chat needs whole*] | [*file count and whether the project is in retrieval mode*] | [*files to remove*] |
| Memory | [*facts about you that come up unprompted, if memory is on*] | [*on or off; per-project setting*] | [*any rule found in memory, moved to a file*] |
| Skills | [*one per repeated procedure*] | [*installed skills*] | [*procedures to move out of the instructions*] |
| Connectors | [*services a procedure uses*] | [*connected services and the loading mode*] | [*remove, or switch to On demand*] |
| Scheduled tasks | [*mechanical checks, from BW8 on*] | [*existing tasks*] | [*none until BW8*] |
| Canonical store | [*everything else*] | [*where it lives today*] | [*what to move into it*] |

### Part 4 · Template: your monthly rot check

Day of the month: [*a fixed day*]. Record each run as one dated row in [*your log file*].

1. **Instructions (2 min).** Read [*instruction file*] whole. Pass if at most 400 words, no procedure, every sentence a rule or a pointer.
2. **Index against folders (3 min).** Pass if every file in [*canonical location*] is in the index, every index entry exists, and nothing superseded sits outside `archive/`.
3. **Mirrors (3 min).** For each mirror in the index ([*list them: project knowledge copies, pasted instructions, a published site*]), compare it with its source. Pass if they match.
4. **Duplicated rules (3 min).** For the three rules broken most often this month ([*where you find them: your log, a reviewer's notes*]), search for each. Pass if each lives in one file.
5. **Contradictions (2 min).** Read your account-wide instructions beside the project's exceptions paragraph. Pass if every collision is named.
6. **Published output (2 min).** [*If you publish:*] search [*the output location*] for every term in [*your private list, kept outside the folder*]. Pass if nothing is found. [*If you do not publish, write "not applicable" and skip.*]

Failures: [*where a failed step becomes a task, and who works it*].

## Sources

All web pages read on 15 November 2026. Anthropic's help-centre pages show no exact date unless one is given below.

**Vendor documentation and statements: Anthropic**

- Claude Help Center. *Understanding Claude's personalization features*. https://support.claude.com/en/articles/10185728-understanding-claude-s-personalization-features
- Claude Help Center. *How can I create and manage projects?* https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects
- Claude Help Center. *Retrieval augmented generation (RAG) for projects*. https://support.claude.com/en/articles/11473015-retrieval-augmented-generation-rag-for-projects
- Claude Help Center. *What are skills?* https://support.claude.com/en/articles/12512176-what-are-skills
- Claude Help Center. *Manage Claude's tool access*. 16 March 2026. https://support.claude.com/en/articles/13730515-manage-claude-s-tool-access
- Claude Help Center. *Usage limit best practices*. https://support.claude.com/en/articles/9797557-usage-limit-best-practices
- Claude Help Center. *How do usage and length limits work?* https://support.claude.com/en/articles/11647753-understanding-usage-and-length-limits
- Claude Help Center. *Use the GitHub integration*. https://support.claude.com/en/articles/10167454-use-the-github-integration
- Anthropic. *Agent Skills*. Claude Platform Docs. https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview
- Anthropic. *How Claude remembers your project*. Claude Code Docs. https://code.claude.com/docs/en/memory
- Anthropic. *Automate work with scheduled tasks*. Claude Code Docs. https://code.claude.com/docs/en/web-scheduled-tasks
- Anthropic. *Extend Claude with skills*. Claude Code Docs. https://code.claude.com/docs/en/skills
- Rajasekaran, P., Dixon, E., Ryan, C. and Hadfield, J. (Anthropic Applied AI team). *Effective context engineering for AI agents*. Anthropic Engineering, 29 September 2025. https://anthropic.com/engineering/effective-context-engineering-for-ai-agents

**Vendor documentation: OpenAI, Google, GitHub**

- OpenAI. *Using projects in ChatGPT*. OpenAI Academy, 10 April 2026. https://openai.com/academy/projects
- OpenAI. *Using skills*. OpenAI Academy, 10 April 2026. https://openai.com/academy/skills
- Google. *Organize your projects with notebooks in Gemini Apps*. Gemini Apps Help. https://support.google.com/gemini/answer/16972047?hl=en
- Google. *About the transition from Gems to skills*. Gemini Apps Help. https://support.google.com/gemini/answer/18560919?hl=en
- Google. *Schedules in Gemini Apps*. Gemini Apps Help. https://support.google.com/gemini/answer/16316416?hl=en-GB
- Google. *Use apps connected to Gemini with a work or school Google Account*. Gemini Apps Help. https://support.google.com/gemini/answer/14959807?authuser=2
- Google. *Import a GitHub repository & ask about it in the Gemini web app*. Gemini Apps Help. https://support.google.com/gemini/answer/16176929?hl=en
- Google. *Provide context with GEMINI.md files*. Gemini CLI docs, updated 18 June 2026. https://geminicli.com/docs/cli/gemini-md/
- GitHub Docs. *Removing sensitive data from a repository*. https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository

**Research and practice**

- Barnett, S., Kurniawan, S., Thudumu, S., Brannelly, Z. and Abdelrazek, M. "Seven Failure Points When Engineering a Retrieval Augmented Generation System". CAIN 2024; arXiv:2401.05856 (version read). https://arxiv.org/abs/2401.05856 (peer-reviewed experience report)
- Brysbaert, M. "How many words do we read per minute? A review and meta-analysis of reading rate". *Journal of Memory and Language* 109 (2019): 104047. doi:10.1016/j.jml.2019.104047. https://doi.org/10.1016/j.jml.2019.104047 (peer-reviewed)
- Hunt, A. and Thomas, D. *The Pragmatic Programmer: From Journeyman to Master*. Addison-Wesley, 1999 (practice; the DRY principle).

**This course and the case**

- BW1 · Mental model, §1, §2, §3, §6, §8 and Deliverable Part 3; BW3 · Briefing: prompts that hold up, §2 and §5.
- Academy case file (`generator/data/building-with-ai/case-academy.md`), compiled 11 November 2026; cited by section, §1, §2, §6, §7, §9.

## Unsure list

1. Claude Help Center article 11647753 is listed as *How do usage and length limits work?*, the title BW1 gives it; the fetch for this unit returned no headline, so the title was not checked against the page on 15 Nov 2026 (the cleanup and "Tools and connectors are token-intensive" statements were read).
2. Memory (§1, What goes where): the help-centre memory page refused the fetch; everything said about memory rests on BW1 §3, not re-read for this unit.
3. Hunt and Thomas, *The Pragmatic Programmer* (1999): the DRY principle is paraphrased from memory of the book, which was not opened; only secondary pages repeating its wording were seen in search.
4. Barnett et al.: read in the arXiv version through a summarising fetch; CAIN 2024 acceptance rests on the conference listing returned by search, not opened. That the biomedical case's answers were generated by GPT-4 comes from the same fetch.
5. Brysbaert (2019): the 238 words-per-minute figure, 190 studies and 18,573 participants were read on a bibliographic page's copy of the abstract (bibbase.org), not on the journal's page.
6. The retrieval switch (§3): the RAG page publishes no threshold and does not say whether the switch depends on the model's window; the unit's statement that it depends on the model you chat with is inference from "approaches the context window limit" and the per-model window sizes in BW1 §1.
7. Whether a new chat in the same project keeps the project-content cache (§4) is not stated on the page read.
8. The token arithmetic in §2 and the Deliverable (about 1.8 tokens a word; 720 tokens for 400 words) is this unit's division of BW1 §2's figure (1M tokens ≈ 555,000 words), unmeasured on real instruction text.
9. ChatGPT: the help-centre pages on projects, on connectors, on connecting GitHub and on scheduled tasks failed to load, and OpenAI's AGENTS.md page redirected; those cells in §8 say "Not checked". The ChatGPT column rests on two OpenAI Academy pages.
10. The 400-word limit, the six-step rot check and its minute budget are this unit's proposals (stated opinion); none was timed or tested on a real project.
Object: none

Fresh check 2026-11-15 (claude-opus-5-5): fix · 2 errors, 5 should-fix, 5 minor; report `audits/building-with-ai/fresh-check-BW4.md`

Correction 2026-11-16, found by BW8's writer (corrections check `audits/building-with-ai/corrections-2026-11-16-BW8-B5-BW4.md`, Changes 6 and 7).

Correction 2026-11-16, found by BW10's writer (corrections check `audits/building-with-ai/corrections-2026-11-16-BW10-B8-BW1-BW4.md`, Change 4).
