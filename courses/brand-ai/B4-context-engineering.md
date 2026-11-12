---
code: B4
title: Context engineering
course: brand-ai · B · Using AI to Build a Brand
model: Opus 5.5
written: 2026-10-29
search: off
---

# B4 · Context engineering

The evidence in this unit is of three kinds, labelled where it appears. **Product documentation** is Anthropic's help centre and developer documentation on how claude.ai and Claude Code behave; each page was opened on 29 October 2026 and is cited for that day, since most help-centre pages carry only a relative "updated" label. Where the documentation is silent, the unit says *undocumented*. **Vendor guidance** is Anthropic's advice on how to use its products, which states what it recommends without publishing a measurement. **His setup** is the Learning Project and its repository as they stood on 29 October 2026, at commit `b4fea09` of `apcanario/learning`; every size and count about it was measured from the repository by script, and each says how. A few facts were observed in the session that wrote this unit, which runs attached to the Project; they are labelled *observed* and cannot be opened as a source. The unit was written with search off; searches were used only to check product behaviour and find the real URL of each source. What a context window is, the 200K window on claude.ai, the 2.7-characters-per-token arithmetic, why every turn re-sends the whole chat, and the layer map of his setup are in B1 (§1, §2, §6, §7). Why a brief that arrives in pieces does worse, and why unrelated tasks belong in separate prompts, are in B3 (§4, §5). This unit assumes them.

## 1 · The layers in claude.ai, and what belongs in each

B1 §6 placed each layer in the context window by who writes it and how far it reaches. This section asks the next question: given what each layer is, what should go into it.

| Layer | Scope | When it enters the window | What belongs there | What does not |
|---|---|---|---|---|
| Profile preferences | Every chat on the account | Every chat | Rules about him that hold everywhere: tone, format, decision style | Anything true only in one Project |
| Project instructions | Chats in one Project | Every chat in the Project | The few rules that must hold in every chat of the Project, and where everything else is | Procedures, lists that change, copies of other files |
| Project files (knowledge) | Chats in one Project | Loaded whole while small; searched once near the window limit | Reference material every chat in the Project needs whole | Records, superseded drafts, build inputs, anything a chat can fetch by path |
| Memory | Account, plus one store per Project | Carried into new chats; how much is undocumented | Facts about him that come up unprompted | Rules, and anything already in a file |
| Skills | Account | Name and description every chat; body when a request matches | Multi-step procedures for one kind of task | Facts and standing rules |
| Connectors | Account | All at the start, or on demand, by setting | Live access to an outside service | Anything a chat never uses |
| Scheduled tasks | Account | Their own session, run by run | Unattended, repeatable jobs with a clear outcome | Work that needs a judgement mid-run |

The first three columns are documented; the last two are my synthesis of the sources for each row, as read on 29 October 2026:

**Preferences and project instructions.** Anthropic's help centre says preferences are "applied to all of your conversations with Claude" and that project instructions "only apply to chats within that project"; it states no order of precedence and says the features can be used "independently or in combination" ([Claude Help Center, *Understanding Claude's personalization features*](https://support.claude.com/en/articles/10185728); product documentation). The projects article says "Claude will use these instructions for all the chats within the project" ([Claude Help Center, *How can I create and manage projects?*](https://support.claude.com/en/articles/9519177)). Since no precedence is documented (B1 §6), a rule that the narrower layer must win has to be written into the narrower layer, and ideally into the wider one too. That is the fix in §5.

**Project files.** "Anything you upload to this space will be used across all of your chats within that project" ([projects article](https://support.claude.com/en/articles/9519177)). The same article adds the limit that matters for planning: "Context is not shared across chats within a project unless the information is added into the project knowledge base." Two help pages describe how the files reach a chat, and they do not say the same thing.

> **Where sources disagree.** Anthropic's skills article (22 September 2026) says projects "provide static background knowledge that's always loaded when you start chats within them" ([Claude Help Center, *What are skills?*](https://support.claude.com/en/articles/12512176-what-are-skills)). The retrieval article (10 September 2026) says that "When your project knowledge approaches the context window limit, Claude will automatically enable RAG mode", in which Claude uses a search tool and "retrieves only the most relevant information", and that a project can return to loading everything once its knowledge falls back below the threshold ([Claude Help Center, *Retrieval augmented generation (RAG) for projects*](https://support.claude.com/en/articles/11473015)). Read together: "always loaded" holds only below the threshold. Above it, project files are searched, and a chat sees the passages the search returns.

**Memory.** Claude "saves memory as a set of individual topics as you chat"; each project has its own memory, and inside a project "Claude uses the project's memory alongside your memory from chats outside of projects"; a project can be kept fully separate by turning off "Use account memory" on its page ([Claude Help Center, *Use Claude's chat search and memory to build on previous context*](https://support.claude.com/en/articles/11817273)). The article does not say how much of memory enters a given chat. B1 §3 covers what memory stores and excludes.

**Skills.** Anthropic's developer documentation gives the loading rule: a skill's name and description are loaded at startup into the system prompt, at about 100 tokens per skill; the body of `SKILL.md`, under 5,000 tokens, enters the window only when a request matches the description; bundled files cost nothing until read ([Anthropic, *Agent Skills*](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview); product documentation). The help centre draws the boundary between layers in one sentence each: custom instructions "apply broadly to all your conversations", projects hold "static background knowledge", and skills "are task-specific and only load when relevant, making them better for specialized workflows" ([*What are skills?*](https://support.claude.com/en/articles/12512176-what-are-skills)). The help page on using skills says Claude "automatically identifies and loads relevant skills based on your task" and does not say whether a skill can be switched on for one Project only ([Claude Help Center, *Using skills in Claude*](https://support.claude.com/en/articles/12512180-using-skills-in-claude)). On what he can read today, skills are an account-wide layer.

**Connectors.** "Each connector takes up space in a conversation." Three modes are documented. In "Auto", the default, "Claude decides dynamically which connectors to load based on what you're working on". In "Always available" mode, "All your connectors are loaded at the start of every conversation"; in "On demand" mode, "Connectors aren't loaded until Claude searches for the right one based on your request"; on-demand loading is recommended for libraries of ten or more connectors or when conversations hit length limits ([Claude Help Center, *Manage Claude's tool access*, 16 March 2026](https://support.claude.com/en/articles/13730515-manage-claude-s-tool-access)). The usage article adds: "Tools and connectors are token-intensive" ([Claude Help Center, usage and length limits](https://support.claude.com/en/articles/11647753)).

**Scheduled tasks.** Anthropic documents several kinds (Cowork, Claude Code cloud, Claude Code desktop and in-session); two matter here. In Cowork, "Each scheduled task runs as its own Cowork session", with connected tools, skills and plugins ([Claude Help Center, *Schedule recurring tasks in Claude Cowork*](https://support.claude.com/en/articles/13854387-schedule-recurring-tasks-in-cowork)). In Claude Code, a cloud scheduled task is "a saved Claude Code configuration: a prompt, one or more repositories, and a set of connectors"; each repository is cloned at the start of every run; each run opens as a new session; the documentation says "the prompt must be self-contained and explicit about what to do and what success looks like"; runs draw on his subscription usage, and schedules more frequent than hourly are rejected. The feature is labelled research preview ([Claude Code docs, *Automate work with scheduled tasks*](https://code.claude.com/docs/en/web-scheduled-tasks); product documentation). B1 §7 drew the consequence: a scheduled task knows nothing of the chat that created it. B5 covers what a task can and cannot touch.

The Claude Code documentation states the dividing rule for its own equivalent of project instructions in terms that transfer: keep the instruction file "to facts Claude should hold in every session", and "If an entry is a multi-step procedure or only matters for one part of the codebase, move it to a skill" ([Claude Code docs, *How Claude remembers your project*](https://code.claude.com/docs/en/memory); vendor guidance written for `CLAUDE.md`). Applying it to claude.ai project instructions is my analogy, as B1 §2 applied the same page's size guidance.

## 2 · Hot, warm and cold: why the vault/index split exists

The brief's word "temperature" needs a definition before it can be used. In this unit:

- **Hot** is text placed in the window at the start of every chat: preferences, project instructions, skill descriptions, connectors in "Always available" mode, and project files while the Project is below the retrieval threshold.
- **Warm** is text a search pulls in when a request seems to need it: project files in retrieval mode, memory, chat search, connectors and skills on demand.
- **Cold** is text outside the window until a chat fetches it by name: files in the repository, read by path after a clone.

Layer by layer, the three temperatures fall like this.

```viz
{
 "kind": "matrix",
 "caption": "Where each layer sits by temperature, as §2 defines hot, warm and cold (the labels are this unit's). Two layers change temperature with a setting or a size: connectors by tool-access mode (<a href=\"https://support.claude.com/en/articles/13730515-manage-claude-s-tool-access\">Claude Help Center, <em>Manage Claude's tool access</em></a>) and project files at the retrieval threshold (<a href=\"https://support.claude.com/en/articles/11473015\">Claude Help Center, <em>Retrieval augmented generation (RAG) for projects</em></a>); both as cited in §1.",
 "cols": [
  "Hot",
  "Warm",
  "Cold"
 ],
 "rows": [
  {
   "label": "Preferences",
   "cells": [
    "●",
    null,
    null
   ]
  },
  {
   "label": "Project instructions",
   "cells": [
    "●",
    null,
    null
   ]
  },
  {
   "label": "Skill descriptions",
   "cells": [
    "●",
    null,
    null
   ]
  },
  {
   "label": "Connectors",
   "tone": 4,
   "cells": [
    {
     "mark": "Always available",
     "tone": 4
    },
    {
     "mark": "On demand",
     "tone": 4
    },
    null
   ]
  },
  {
   "label": "Project files",
   "tone": 4,
   "cells": [
    {
     "mark": "below threshold",
     "tone": 4
    },
    {
     "mark": "retrieval mode",
     "tone": 4
    },
    null
   ]
  },
  {
   "label": "Skill bodies",
   "cells": [
    null,
    "●",
    null
   ]
  },
  {
   "label": "Memory",
   "cells": [
    null,
    "●",
    null
   ]
  },
  {
   "label": "Chat search",
   "cells": [
    null,
    "●",
    null
   ]
  },
  {
   "label": "Repository files",
   "cells": [
    null,
    null,
    "by path"
   ]
  }
 ],
 "legend": [
  {
   "mark": "●",
   "means": "the temperature §2 gives this layer"
  }
 ]
}
```

The labels are mine. Anthropic's engineering team describes the same choice as context loaded up front against context retrieved just in time: an agent can "maintain lightweight identifiers (file paths, stored queries, web links, etc.)" and load the data only when it needs it; its recommended middle course is a hybrid, "retrieving some data up front for speed, and pursuing further autonomous exploration at its discretion"; and Claude Code is its worked example, where "CLAUDE.md files are naively dropped into context up front" while "primitives like glob and grep allow it to navigate its environment and retrieve files just-in-time" ([Anthropic, *Effective context engineering for AI agents*, 29 Sep 2025](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents); vendor guidance).

His method already has that shape, and the reason is size. The method states where things live: everything is in the private repository; the Project "holds mirrors of `docs/`"; and "A chat clones the repo and ends with a commit" (`method.md`, Home). The vault, `courses/`, holds the finished units; `courses-index.md` holds, for every unit, its status, model, search flag and path. In the engineering post's terms the index is a file of lightweight identifiers, and the vault is what they point to.

The split is forced by arithmetic. The seven filed Brand + AI units in the vault come to 358,052 characters, and the 137 history reports in `kit/greece/` and `kit/rome/` to 3,484,164 (Unicode characters, both counted by script on 29 October 2026). At B1 §2's arithmetic of about 2.7 characters per token, the history reports alone are about 1.3 million tokens, more than six times the 200K window he has on claude.ai (B1 §1). No chat can hold the course; every chat can hold the map to it. B1 §7 put it as the vault being "the one store that never enters a chat by itself", fetched when a chat needs a file, and handed the question of which file belongs at which temperature to this unit.

The answer the evidence supports:

1. **Hot: what every chat must obey whole.** The rules (method, sourcing standard, reader), the map (the index) and the queue (the backlog). A checklist read in fragments is a different checklist; these files need to arrive whole, which only happens while the Project stays under the retrieval threshold (§1).
2. **Warm: facts about him that come up unpredictably.** That is what memory is for (§1).
3. **Cold: everything a chat can name before it needs it.** Units, reports, syllabi, research, audits, build code, records. The index names each one's path, so a chat that needs a unit can read it after cloning.

The Deliverable measures how far the Project has drifted from this, and the drift is large: the method says the Project mirrors `docs/`, while `SETUP.md` §2 tells him to upload the filed units, the superseded research and its five notes, the history kit's briefs and rubrics, the Rome syllabus, the theme and the Brand + AI data files as well.

## 3 · What loads every turn, what loads on demand, and what each costs

B1 §2 gave the mechanism: the model keeps nothing between turns, every turn re-sends the whole chat, and so every hot layer is paid once per turn, on every turn. On claude.ai the payment is drawn from his usage limit, and Anthropic's usage guidance names "Current conversation length" among the factors that draw it down ([Claude Help Center, *Usage limit best practices*, 22 Sep 2026](https://support.claude.com/en/articles/9797557-usage-limit-best-practices)). B2 §2 reported the one documented relief: project content is cached and counts less when reused. Anthropic's page adds that caches expire after inactivity, so the first message after a long break counts the content in full again.

His setup, layer by layer, as measured or documented on 29 October 2026:

| Layer | Loads | Size in his setup | Source of the size |
|---|---|---|---|
| Project instructions | Every turn | 4,421 characters, 675 words, 27 lines; about 1,600 tokens at 2.7 characters per token | `docs/project-instructions.md`, `wc -w`, character count by script |
| Preferences | Every turn | Unmeasured; the text is not in the repository | none |
| Skill descriptions | Every turn | About 100 tokens per skill (Anthropic's figure); his 4 repository skills and about 15 personal skills come to about 1,900 tokens, plus Anthropic's built-in skills, which this unit did not count | [Agent Skills](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview); count from the Learning Project's setup as of 28 October 2026 |
| Connectors | Every turn in "Always available"; when searched in "On demand" | Eight connectors plus a linked computer; per-connector size undocumented | [Tool access](https://support.claude.com/en/articles/13730515-manage-claude-s-tool-access) |
| Memory | Carried into new chats | Amount undocumented; *observed*: a listing of memory files with one-line descriptions arrives before the first message | [Memory](https://support.claude.com/en/articles/11817273) |
| Project files | Whole below the threshold; searched above it | 33 files, 907,260 characters, 127,263 words | Measured from the 33 repository files the Project mirrors (Deliverable, A) |
| Skill bodies | When a request matches | Under 5,000 tokens each (Anthropic's stated size); his four repository skills are 724 to 1,110 words | `wc -w` on `skills/*/SKILL.md` |
| Vault files | When a chat reads them | 358,052 characters for seven units | `wc -m` |

**The project files are no longer hot.** 907,260 characters is about 336,000 tokens at B1's 2.7 characters per token, and about 259,000 at the older 3.5 figure B1 also reports. Both exceed the 200K window. On the retrieval article's rule, a Project of that size runs in retrieval mode ([RAG for projects](https://support.claude.com/en/articles/11473015)). I cannot see the mode from the repository, so this is an inference from the documented rule and the measured size. What was observed is consistent with it but does not test it, since both observations come from Claude Code sessions, which list the Project's documents by name whatever their size (unsure list, 1): in B1's writing session a list of 24 documents arrived by name and five were then read in (B1 §1, observed 28 October); in this unit's session, a list of the Project's 33 documents arrived by name with an instruction to read or search them with a tool (*observed*, 29 October 2026).

Against the window, the knowledge looks like this.

```viz
{
 "kind": "compare",
 "unit": "k tokens",
 "caption": "Project knowledge against the window, in thousands of tokens (the knowledge figures are approximate): 907,260 characters at B1's 2.7 and its older 3.5 characters per token, against the 200K window on claude.ai (B1 §1). From §3; the size was measured by script from the 33 repository files the Project mirrors, at commit <code>b4fea09</code>, 29 October 2026 (Deliverable, A).",
 "rows": [
  {
   "label": "200K window",
   "value": 200,
   "tone": 3
  },
  {
   "label": "Knowledge at 3.5",
   "value": 259,
   "tone": 1
  },
  {
   "label": "Knowledge at 2.7",
   "value": 336,
   "tone": 1
  }
 ]
}
```

That changes what the Project knowledge is worth. In retrieval mode the method arrives as whatever passages a search returns for the request at hand. The sourcing checklist, which only works when every item is checked, may arrive as two items out of twelve. And the search runs over everything in the knowledge, including the superseded research that failed Audit 1 on 23 of 91 claims (`courses-index.md`) and that covers the same topics as the units that replaced it. B1 §2 reported Chroma's vendor finding that distractors, passages similar to the answer, lowered accuracy further; a superseded draft of the same material is a distractor in that exact sense.

**What each kind of loading costs, in his terms:**

- **Hot** costs tokens on every turn of every chat, and attention (B1 §2). It buys certainty that the text is there. It is worth it for the instructions, which are small, and for files every chat needs whole.
- **Warm** costs little until used, and costs reliability: the text is present only if a search or a match brings it in. Skill bodies are warm by design, and a procedure that fires on a recognisable request belongs there. Rules that must hold everywhere do not.
- **Cold** costs a deliberate fetch, a tool call that adds the file to the window from then on (B1 §7). It buys a clean window: nothing arrives that the chat did not name.

## 4 · When to start a new chat, and when not to

Start a new chat when one of these holds.

1. **The task changes.** B3 §5 gave the evidence for one artefact per prompt: each task's material is irrelevant context for the others, and the tasks want different models. A new task in an old chat carries the old task's material on every turn (§3).
2. **The first output missed.** B3 §4 reported Laban and colleagues' finding that a brief arriving in pieces does worse than one complete brief, and the paper's own advice to consolidate the requirements into one instruction and start a new conversation. Rewrite the brief and open a new chat.
3. **The chat is long.** Every turn re-sends everything before it (B1 §2). Anthropic's advice: "Try starting a new conversation if you're approaching your usage limit in a longer chat" ([usage and length limits](https://support.claude.com/en/articles/11647753)). When code execution is on, long chats are also summarised automatically, and summarising is lossy by definition (B1 §3).
4. **The next step must not see this one.** A checker or auditor that watched the unit being written is no longer independent. B2 §8 gave the evidence on self-preference, and the method requires a fresh checker "in a new chat that has not seen the unit written" (`method.md` §5).
5. **A unit starts.** "Never reuse a chat across units; leaked context is how a course starts repeating itself" (`method.md` §4).

The five conditions, read as one rule.

```viz
{
 "kind": "decision",
 "caption": "§4's rule for starting a new chat: any one of the five conditions means a new chat. Drawn from this unit's §4, which rests on B3 §4 and §5, B1 §2 and §3, B2 §8, <code>method.md</code> §4 and §5, and <a href=\"https://support.claude.com/en/articles/11647753\">Claude Help Center, usage and length limits</a>.",
 "root": {
  "q": "The task changes?",
  "tone": 4,
  "branches": [
   {
    "label": "yes",
    "to": {
     "outcome": "New chat",
     "tone": 2
    }
   },
   {
    "label": "no",
    "to": {
     "q": "The first output missed?",
     "tone": 4,
     "branches": [
      {
       "label": "yes",
       "to": {
        "outcome": "Rewrite the brief, new chat",
        "tone": 2
       }
      },
      {
       "label": "no",
       "to": {
        "q": "The chat is long?",
        "tone": 4,
        "branches": [
         {
          "label": "yes",
          "to": {
           "outcome": "New chat",
           "tone": 2
          }
         },
         {
          "label": "no",
          "to": {
           "q": "The next step must not see this one?",
           "tone": 4,
           "branches": [
            {
             "label": "yes",
             "to": {
              "outcome": "New chat",
              "tone": 2
             }
            },
            {
             "label": "no",
             "to": {
              "q": "A unit starts?",
              "tone": 4,
              "branches": [
               {
                "label": "yes",
                "to": {
                 "outcome": "New chat",
                 "tone": 2
                }
               },
               {
                "label": "no",
                "to": {
                 "outcome": "Stay in the chat",
                 "tone": 3
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
    }
   }
  ]
 }
}
```

Stay in the chat when one of these holds.

1. **The next step works on material only this chat has.** Applying a checker's findings as exact replacements, finding by finding, needs the current text and the finding list together. Moving them to a new chat means pasting both again, and the paste is the same tokens plus a chance to paste the wrong version.
2. **The step is a short follow-up on the same artefact,** for example a second pass on a caption, where the earlier output is the material.
3. **Work has paused briefly.** Anthropic's usage guidance says cached project content counts less when reused and that the cache expires after inactivity ([usage best practices](https://support.claude.com/en/articles/9797557-usage-limit-best-practices)). Whether starting a new chat in the same Project loses that cache is undocumented.

Whichever way it goes, a chat ends by writing its state somewhere a later chat can read. Anthropic's engineering post calls this structured note-taking and gives the example of "your custom agent maintaining a NOTES.md file"; its other technique for long work is to give "specialized sub-agents" focused tasks "with clean context windows" ([Effective context engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)). His method already does both. The backlog and changelog are the notes file (`method.md` §8), and one chat per unit, with the checker in its own chat, is the clean window. The weak point is the first: a new chat knows only what the last one wrote down. The Deliverable's finding F10 shows the notes are already a step behind.

## 5 · How a project rots, and how to stop it

A project rots when the text the model reads stops matching the work. The three kinds the brief names each have a documented mechanism.

**Stale files.** A file that was right when written and was never retired keeps arriving. Anthropic's usage article recommends removing project files no longer in use ([usage and length limits](https://support.claude.com/en/articles/11647753)). Claude Code's documentation lists what its own instruction audit looks for, among them "instructions written for older models, references to files or commands that don't exist, and files that contradict each other" ([Claude Code docs, *Memory*](https://code.claude.com/docs/en/memory); vendor guidance for Claude Code). His repository has all three: a hand-off note headed "Start here" that tells the next session to create a repository that now exists; a data file that still tells a chat to run audits "in the personal-assistant Project"; and two files that still tell the reader to run a build script retired on 28 October (Deliverable, F9).

**Duplicated rules.** A rule written in two places is paid twice where both are hot, and it drifts as soon as one copy is edited. Copies that are identical can be caught by a script. The dangerous ones are paraphrases, because no comparison flags them. His project instructions share only 20 eight-word sequences with `method.md`, 3% of their own, yet their Review and Backlog paragraphs restate §6 and §8 of the method in other words. The list of which units are written with search on exists in four prose copies, in three different versions (Deliverable, F8). B1 §6 flagged the tone rules repeated in his preferences and his project instructions.

**Instructions that contradict preferences.** Claude Code's documentation: "if two instructions contradict each other, Claude may pick one arbitrarily", followed by the advice to review periodically "to remove outdated or conflicting instructions" ([Claude Code docs, *Memory*](https://code.claude.com/docs/en/memory)). The claude.ai help centre states no precedence between preferences and project instructions ([personalisation features](https://support.claude.com/en/articles/10185728)), so the Claude Code sentence is the nearest documented description of what happens; applying it to claude.ai is my analogy, as in B3 §4. B3 §4 named one conflict: the preferences send anything with three or more sections to an HTML artifact, and a unit is a Markdown file. The Deliverable finds two more of the same kind (F5).

Three habits stop rot, and each traces to the sources above.

1. **One home per rule, and pointers everywhere else.** The method already applies this to course content ("each anecdote, dispute and self-test question has one home; the others point to it by number", `method.md` §3). Applied to rules, a fact such as which units search lives in one place (the index's Search column, which `kit/index_check.py` already checks against the data file) and every other mention points there.
2. **The narrower layer names its exceptions.** Since no precedence is documented, the Project instructions state where the Project departs from the preferences, in one paragraph.
3. **A scheduled check.** Rot accumulates between sessions, and nobody reads a file to look for it. The checks in the Deliverable are mechanical, which is the kind of work Anthropic's documentation describes scheduled tasks for: "unattended, repeatable, and tied to a clear outcome" ([scheduled tasks](https://code.claude.com/docs/en/web-scheduled-tasks)).

## Deliverable · Project-structure audit

The Learning Project and the repository `apcanario/learning` at commit `b4fea09`, 29 October 2026. Usable on its own: every finding names its file or layer, the evidence, the fix and an effort estimate. **Every effort figure is my estimate** of his time at the keyboard, with a chat doing the edits where the fix is a file change; it includes the commit and excludes rebuilding and publishing Academy unless the row says so.

### A · How this was measured

- **Project knowledge.** The 33 files in the Project's knowledge list (the Learning Project's setup as of 28 October 2026; the same 33 names, *observed* in this session on 29 October) were each mapped to the repository file it mirrors; all 33 exist in the repository. Sizes are Unicode characters counted by a Python script, and words, in the C locale (a UTF-8 locale counts five more in the instructions, 680, because it splits on the middle dot), by `wc -w`. The Project copies were not opened; the changelog records all 33 re-uploaded from the repository on 28 October, and repository files changed since then may differ from their Project copy.
- **Tokens** are B1 §2's arithmetic (about 2.7 characters per English token for Opus 5.5's tokenizer, unmeasured), with the 3.5 figure beside it where the difference matters.
- **Duplication.** Every pair of the 20 main method, skill, data and doc files was compared on shared eight-word sequences (lower-cased words, punctuation dropped). The two audit prompts were compared as exact strings. Paraphrase is invisible to this measure, so the semantic duplicates below were found by reading.
- **Contradictions** were found by reading the preferences (as reproduced in the context packet), the project instructions, `method.md`, `SETUP.md`, `docs/BACKLOG.md` and `hub.py` against each other, then confirming each with `grep`.
- **Public build.** The local build `kit/academy/`, which `kit/deploy.sh` pushes to the public Pages site, was searched for six private terms. The terms are not reproduced here. The live site was not opened (the fetch was refused).
- **Memory** contents were not read into this unit: the course is published, and memory is private.

### B · The layers: what each holds now, and what it should hold

| Layer | Holds now (29 Oct 2026) | Should hold |
|---|---|---|
| Preferences | Tone, format, decisions, calendar, hard rules; one line (anything with three or more sections goes in a dark-theme HTML artifact) that collides with the Project's files | The same, with one clause: "unless a Project's instructions say otherwise" |
| Project instructions | 13 paragraphs, 675 words: reader, purpose and repo layout, design rule, publishing steps, one chat per unit, models, briefs, output path, sourcing, review cadence, the four-step backlog procedure, tone, completeness | The rules every chat must obey, the Project's exceptions to the preferences, and pointers; procedures moved to skills and the method (C, F7) |
| Project knowledge | 33 files, 907,260 characters, above the window, so in retrieval mode by the documented rule | 5 files, 79,332 characters: `method.md`, `sourcing-standard.md`, `reader.md`, `courses-index.md`, `BACKLOG-chats.md` (F1) |
| Memory | Account memory plus a Project store; account memory feeds this Project | The Project store only (F13) |
| Skills | 4 repository skills, about 15 personal skills, Anthropic's built-ins; account-wide | No change found. The four repository skills hold the procedures and load on demand, which is the layer's purpose |
| Connectors | Eight plus a linked computer; no procedure in `docs/`, `skills/`, `SETUP.md` or the READMEs uses one (`grep`; the only mention is the hand-off note's built-in browser) | Set to load on demand (F14) |
| Scheduled tasks | None | One weekly rot check on the repository (F16, E) |
| Vault and repository | Canonical; units, reports, records, build | Unchanged, plus an `archive/` folder for retired notes (F9) |

### C · Findings

**F1 · Project knowledge is too large to load and mostly holds files no chat needs whole.** *Layer:* Project knowledge. *Evidence:* 33 files, 907,260 characters (about 336,000 tokens at 2.7 characters per token, about 259,000 at 3.5), against a 200K window (on 2 Nov 2026 the claude.ai window for the current models is disputed and may be 1M, which leaves this finding's retrieval-mode inference undetermined: B8 §1). By share of characters: the five filed units in it, 242,926 (26.8%); nine history-kit files, 221,633 (24.4%), of which `roman-syllabus.html` alone is 153,026; the superseded audience-growth research and its five notes, 197,753 (21.8%); build inputs (`hub.py`, `theme.css`, `design-README.md`, `units_data.py`), 114,550 (12.6%); records (`academy.md`, `pm-status-2026-10-28.md`, `CHANGELOG-chats.md`), 46,645 (5.1%); rules, map and queue, 79,332 (8.7%); `project-instructions.md`, 4,421 (0.5%). Filing, audit, kit and theme chats clone the repository first (`SETUP.md` §6 for history, §7, §8, §9; `method.md`, Home), so for them every one of the 28 files outside the rules set is already available cold. The exception is a Brand + AI writing chat: `SETUP.md` §6 says to paste the brief and "Attach nothing else", so today such a chat reads earlier units from the knowledge. `method.md` (Home) says the Project "holds mirrors of `docs/`", while `SETUP.md` §2 lists all 33. *Fix:* remove 28 files from the knowledge, keeping `method.md`, `sourcing-standard.md`, `reader.md`, `courses-index.md` and `claude/BACKLOG-chats.md`. At 79,332 characters (about 29,000 tokens at 2.7, under 15% of the window) the set is below the threshold, and on the retrieval article's rule the Project returns to loading whole files. Rewrite `SETUP.md` §2 to list the five; change `SETUP.md` §6 so a Brand + AI writing chat also clones `apcanario/learning` and reads the units it points back to by path, as the hand-off note's step 2 and this unit's own writing session already do; and change `skills/file-unit/SKILL.md` §6 to re-upload only `courses-index.md` after a filing. Nothing is lost: all 28 are in the repository. *Effort:* 40 minutes.

F1's shares, side by side.

```viz
{
 "kind": "compare",
 "unit": "%",
 "caption": "Project knowledge by share of its 907,260 characters, in the groups of finding F1 (Deliverable, C); the bar in its own tone is the rules, map and queue, the five files F1 keeps. Measured by script from the 33 repository files the Project mirrors, at commit <code>b4fea09</code>, 29 October 2026 (Deliverable, A).",
 "rows": [
  {
   "label": "Filed units",
   "value": 26.8,
   "tone": 1
  },
  {
   "label": "History-kit files",
   "value": 24.4,
   "tone": 1
  },
  {
   "label": "Superseded research",
   "value": 21.8,
   "tone": 1
  },
  {
   "label": "Build inputs",
   "value": 12.6,
   "tone": 1
  },
  {
   "label": "Rules, map, queue",
   "value": 8.7,
   "tone": 3
  },
  {
   "label": "Records",
   "value": 5.1,
   "tone": 1
  },
  {
   "label": "Project instructions",
   "value": 0.5,
   "tone": 1
  }
 ]
}
```

**F2 · The project instructions are also uploaded as a knowledge file.** *Layer:* Project knowledge. *Evidence:* `project-instructions.md` is in the knowledge list, and the same text is pasted into the instructions field (`docs/CHANGELOG.md`, row "Academy open questions closed"). The same 4,421 characters reach the Project twice, and the knowledge copy goes stale the moment the field is edited. *Fix:* remove it from the knowledge (part of F1). *Effort:* 1 minute.

**F3 · The knowledge mirror already lags the repository.** *Layer:* Project knowledge. *Evidence:* A1 and B3 were filed on 29 October (commits `a86b664`, `b4fea09`); neither is in the 33-file list *observed* in this session the same day, although `skills/file-unit/SKILL.md` §6 requires the re-upload. *Fix:* F1 removes units from the knowledge, so the lag disappears for them; for the five files that stay, add them through the GitHub integration if GitHub is connected to claude.ai, which adds selected repository files to the project knowledge and refreshes them with "Sync now" ([Claude Help Center, *Use the GitHub integration*](https://support.claude.com/en/articles/10167454)). *Effort:* 15 minutes, if the integration is available.

**F4 · Two different files are called `BACKLOG.md`.** *Layer:* repository and knowledge. *Evidence:* `docs/BACKLOG.md` is the queue of chats; `kit/BACKLOG.md` is the Rome writing prompt with the lane notes. The knowledge holds the kit's file under the bare name `BACKLOG.md` and the queue as `claude/BACKLOG-chats.md`. Across the repository, 39 references in 16 files say `BACKLOG.md` with no folder (`grep`, excluding the built site). The project instructions use the bare name once, for the history lane notes, after calling `docs/BACKLOG.md` "the one queue". *Fix:* rename `kit/BACKLOG.md` to `kit/LANES.md` and update the bare references. F1 already takes the kit file out of the knowledge. *Effort:* 45 minutes.

**F5 · Three of the preferences collide with the Project's work.** *Layer:* preferences and project instructions. *Evidence:* (a) the preferences send anything with three or more sections to a dark-theme HTML artifact, while a unit is a Markdown file in the vault (`method.md` §7; B3 §4); (b) the preferences ask for concise output, bullets and bold, with prose only when nuance needs it, while a unit is a long-form report of whatever length the topic needs (`method.md` §4); (c) the preferences say not to volunteer plans, next steps or reminders he did not ask for, while every chat that works a backlog row must hand over "the row that is next up" (project instructions; `method.md` §8). No precedence is documented ([personalisation features](https://support.claude.com/en/articles/10185728)). *Fix:* the "Scope" paragraph in the revised instructions below, plus one clause at the end of the preferences' format rule: "unless a Project's instructions say otherwise". *Effort:* 10 minutes.

**F6 · The design preferences and the theme agree.** *Layer:* preferences and `design/theme.css`. *Evidence:* the preferences' fonts and colours (DM Sans, Space Mono, #0a0a0c, #131316, #ff6b6b and the five secondary accents) are the theme's tokens, lines 40 to 46. *Fix:* none. Recorded so the next audit does not re-check it.

**F7 · The project instructions carry procedures and paraphrase the method.** *Layer:* project instructions. *Evidence:* of 675 words (`wc -w`), the Purpose paragraph (147 words) restates the repository layout in `README.md`; Publishing (56 words) restates `skills/file-unit/SKILL.md` §5.3; Backlog and changelog (133 words) restates `method.md` §8 steps 1 to 4; Review (66 words) restates `method.md` §6; Tone repeats the preferences (B1 §6). The eight-word comparison finds only 3% shared with `method.md`, so a change to the method will not be caught by a diff. The instructions are the one Project layer guaranteed in every chat, so this is where pointers pay most. *Fix:* replace the instructions with the text in D. Procedures stay in the skills and the method, which already hold them. *Effort:* 20 minutes.

**F8 · Which units search: four prose copies, three versions.** *Layer:* method, setup, data file. *Evidence:* `method.md` §4 (line 114): "A2, A6, A9 (written), A8, B2, B8, DD-A1", which omits DD-B3 and B1 (B1's front matter says `search: on`); `SETUP.md` §6 (line 38): "B2, A8, B8, DD-A1, DD-B3"; `hub.py` line 127: "A8, B2, B8, DD-A1, DD-B3"; `hub.py` line 139: "A2, A6, A9, A8, B2, B8, DD-B3", which omits DD-A1. The source, `hub.py` `ORDER`, gives DD-B3, A8, B8 and DD-A1 for units not yet written, and the vault's front matter gives the written ones; `kit/index_check.py` already checks the index's Search column against both. *Fix:* replace each prose list with "the Search column of `courses-index.md`". *Effort:* 15 minutes, plus the rebuild in F9b.

**F9 · Stale files and lines still read as current.** *Layer:* repository docs and the data file. *Evidence:* (a) `docs/handoffs/2026-10-28-brand-ai-handoff.md`, headed "Next session" and "Start here. The first job is to move this folder off zip files", tells the reader to create a repository named `learning-project` and lists a hub artifact retired on 28 October. (b) `hub.py` `BUILD_PICK` and `BUILD_BODY` (lines 116 to 141), labelled on the page as "kept as the v5.1 record", tell the reader to make a separate Project for the two courses and to review "in the personal-assistant Project"; `AUDIT_PROMPTS_NOTE` (line 156) says the same; all three are rendered into Academy (`kit/academy/index.html` carries "personal-assistant" four times). (c) `SETUP.md` §8 (line 47) says the first audit "is due after B1" and gives the staleness date as 27 April 2027, where `courses-index.md` gives 28 April 2027. (d) `docs/BACKLOG.md` heads its writing lane "(parallel; one unit per chat)" twelve lines after saying "The lanes no longer run in parallel." (e) Two more files still tell the reader to run `build_hub.py`, retired on 28 October: `design/README.md` step 3 and `generator/data/_template/hub.py` line 3, the template every new markdown course is copied from. *Fix:* (a) move the hand-off note to `docs/archive/`, with the status notes `docs/pm-status-2026-10-28.md` and `docs/academy.md` once their open rows are closed; (b) delete the three `hub.py` blocks and leave one line pointing to `method.md`, then rebuild, verify and publish Academy; (c), (d), (e) correct the lines. *Effort:* F9a, c, d, e: 20 minutes; F9b: 45 minutes including the rebuild and publish.

**F10 · The queue and the record are behind the work.** *Layer:* `docs/BACKLOG.md`, `docs/CHANGELOG.md`. *Evidence:* B3 and A1 were filed on 29 October, yet rows B-1 (B3) and B-3 (A1) are still in the queue, and the changelog has no row for either filing. The project instructions require the opposite: "no done row stays in the queue". The next chat reads the queue to know what is next (§4). *Fix:* move both rows to the changelog with date, model and result; recopy `claude/BACKLOG-chats.md`; this chat's row B-2 follows when B4 is filed. *Effort:* 10 minutes.

**F11 · The theme reaches the build through a hand copy.** *Layer:* build. *Evidence:* `kit/build.py` line 733 reads `kit/shell.css`, and the design rule is that `design/theme.css` is the stylesheet; six files tell the reader to `cp design/theme.css kit/shell.css`, and `kit/verify.py` has no check that the two match. They are identical today (`cmp`). *Fix:* have `build.py` read `../design/theme.css` directly and delete `shell.css`, or add a `cmp` failure to `verify.py`. *Effort:* 20 minutes.

**F12 · The two audit prompts live in two files.** *Layer:* method and data file. *Evidence:* the stratified-sample prompt (1,547 characters) and the staleness prompt in `method.md` §6 are identical, by string comparison, to the copies in `hub.py` `AUDIT_PROMPTS`; the two files share 384 eight-word sequences in all, 9% of `method.md`. Identical today, they will diverge at the first edit to either. *Fix:* the rot check in E compares them weekly. Generating the hub's copy from `method.md` at build time is the permanent fix. *Effort:* 5 minutes for the check (inside F16); 1 hour for the build change.

**F13 · Account memory flows into a Project whose output is published.** *Layer:* memory. *Evidence:* inside a project, Claude uses the project's memory "alongside your memory from chats outside of projects" unless "Use account memory" is turned off on the project's page ([memory](https://support.claude.com/en/articles/11817273)). Every unit is published on a public site, and the course's binding rule keeps private detail out of units; a writing chat that receives account memory has to apply that rule by hand on every turn. The reader facts a unit needs are in `reader.md` and the brief. *Fix:* turn off "Use account memory" for the Learning Project. *Effort:* 1 minute.

**F14 · Eight connectors are connected, and no Project procedure uses one.** *Layer:* connectors. *Evidence:* the Learning Project's setup as of 28 October 2026 lists Gmail, Google Calendar, Google Drive, Spotify, Vercel, Booking.com, Claude Docs and Claude in Chrome, plus a linked computer; a `grep` of `docs/`, `skills/`, `SETUP.md` and the READMEs finds no procedure that calls one. In "Always available" mode all of them load at the start of every chat ([tool access](https://support.claude.com/en/articles/13730515-manage-claude-s-tool-access)). Which mode he has set is not visible from the repository; the documented default is "Auto". The article's own table puts fewer than ten frequently used connectors under "Always available" and conversations that hit length limits under "On demand"; the pick below rests on the second row, since no Project procedure uses a connector. *Fix:* set tool access to "On demand". Pick: On demand. Override if: chats outside this Project start missing a connector they used to call unprompted; then "Auto". *Effort:* 2 minutes.

**F15 · The public build carries private material.** *Layer:* the build and the data it reads. *Evidence:* six private terms (personal names, a club, and lines about his employer) occur in three files of `kit/academy/`, the folder `kit/deploy.sh` pushes to the public Pages site: `index.html` (3 occurrences, from `hub.py` `FRAME` and a unit summary in `units_data.py`), `brand-a/briefs.html` (6, from the briefs in `units_data.py`) and `brand-b/read-b1.html` (1, from B1 §3). The terms are kept out of this unit. Two rules collide here: briefs are never reworded (project instructions, "Briefs"), and Academy is public. Removing the files from the site does not remove them from the public repository's history: GitHub's documentation says commits with sensitive data "may still be accessible elsewhere", in clones, forks and cached views, even after history is rewritten and force-pushed ([GitHub Docs, *Removing sensitive data from a repository*](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository)). *Fix:* (1) B1 §3: replace the name with "his disambiguation between two people with the same first name", as an erratum; (2) a build-time redaction list kept outside both repositories, which `mdcourse.py` applies to brief and frame text before rendering, so the briefs stay unreworded at source; (3) `verify.py` fails if any listed term reaches `kit/academy/`; (4) Pedro decides whether the public repository's history matters enough to rewrite. B8 sets the general privacy rules. *Effort:* 2 hours for (1) to (3), plus a rebuild and publish; (4) is his decision first.

**F16 · Nothing checks for rot between sessions.** *Layer:* scheduled tasks. *Evidence:* no scheduled task exists (setup as of 28 October 2026). F3, F9 and F10 each come from changes made on 28 or 29 October, the repository's first two days (commit dates). *Fix:* the weekly scheduled task in E. *Effort:* 20 minutes.

**F17 · The index, the one file every chat needs, is mostly a finished record.** *Layer:* `docs/courses-index.md`. *Evidence:* 38,595 characters, 268 lines; the complete Greece section is 12,325 characters and the 59 written Rome rows another 9,343, together 56% of the file; `kit/index_check.py` checks every row, so the tables cannot simply be cut. *Fix:* move finished courses to `docs/courses-index-archive.md`, teach `index_check.py` to read both files, keep the live index (about 17,000 characters) in the Project. *Effort:* 2 to 3 hours.

### D · Revised project instructions (for F5 and F7)

Pasted into the Project's instructions field in place of the current text; `docs/project-instructions.md` updated to match. Every rule in the current instructions is kept, by statement or by pointer; two are new and marked.

> **Reader.** One reader: Pedro, 35, Porto, ADHD; an educated adult who wants genuine depth, reads in order, on his phone, and checks the citations. The full profile is `reader.md`. Add nothing to it.
>
> **Scope over my preferences** (new). My saved preferences apply here except in three cases. Units, audits and docs are Markdown files in the repo, written in the form `method.md` sets, long-form where it says so; the HTML-artifact rule and the concise-format rule do not apply to them. Handing over the backlog at the end of a chat, with the next row named, is something I have asked for.
>
> **Where things are.** The private repo `apcanario/learning` is canonical. `method.md` is the method; `courses-index.md` is the map (what is written, what is next, the path of every file); `docs/BACKLOG.md` is the queue. A chat clones the repo, reads what it needs by path, and ends with a commit and push. Project knowledge holds five mirrors and nothing else.
>
> **Rules for every chat.** One chat per unit, with its deliverable; audits and filing get their own chats. Writing Opus 5.5, audit Fable 5.1, exceptions in the build order; record the model that actually wrote each unit. Use a brief as written (Brand + AI: the course's Briefs page; history: the module's syllabus prompt and lane note, with AGENT-SPEC.md and WRITER-BRIEF.md); never reword it. Apply `sourcing-standard.md` Part 1 plus the course's part; nothing invented. No unit starts while an audit is due or a REWRITE is open; units written with search on get the six-month staleness check (`method.md` §3, §6). A finished unit is filed at the vault path `method.md` §7 gives; a history unit also goes into the kit (§7 step 3). Every page is built by `kit/build.py` from `design/theme.css`; no page gets its own CSS. Publishing Academy means the artifact, then `deploy.sh` (`file-unit`). A chat that works a backlog row ends as `method.md` §8 says.
>
> **Public** (new). Academy is public. No private detail goes into a unit, a doc or any data the build renders.
>
> **Tone.** Beyond my preferences: no closing pleasantries, no motivational language.
>
> **Completeness.** A unit is written in full, with its deliverable built in full. Never outline it, summarise it or describe what it would contain.

### E · The rot check, weekly

Six checks, each a command run from the repository root; every one was run on 29 October 2026 and its result is the evidence above.

1. **Filed units still queued** (F10): for each `code:` in `courses/brand-ai/*.md`, `grep -q "| $c ·" docs/BACKLOG.md` must find nothing. On 29 October it found A1 and B3.
2. **Instructions to use retired things** (F9): `grep -rnIF -e "python3 build_hub.py" -e "personal-assistant Project" -e 'named `learning-project`' SETUP.md README.md design skills generator/data docs/method.md docs/project-instructions.md docs/handoffs` must find nothing. It found five lines in four files.
3. **Theme copy** (F11): `cmp design/theme.css kit/shell.css` must be silent. It was.
4. **Audit prompts** (F12): the text from "You are auditing four units" to the end of the block must be identical in `docs/method.md` and `generator/data/brand-ai/hub.py`, and likewise for "You are re-checking one unit". Both were.
5. **Knowledge budget** (F1): the five mirrored files must total under 110,000 characters (about 40,000 tokens at 2.7). They total 79,332.
6. **Private terms** (F15): `grep -rliFf <terms file> kit/academy` must list nothing, where the terms file lives outside both repositories. On the terms used for F15 it listed three files.

**Scheduled task** (Claude Code cloud task; repository `apcanario/learning`; no connectors; weekly). The documentation requires a self-contained prompt that says what success looks like ([scheduled tasks](https://code.claude.com/docs/en/web-scheduled-tasks)); check 6 needs the terms file; a cloud run could carry the terms as an environment variable, which the documentation says is visible to anyone who uses the environment, so it stays a filing step; the task's connectors, all included by default, are removed at creation. The prompt:

> Clone `apcanario/learning` and change nothing in it. Run these five checks from the repository root and report each as PASS or FAIL with the lines that fail. (1) For every file in `courses/brand-ai/`, read its `code:` front matter; FAIL if `docs/BACKLOG.md` has a row containing "| <code> ·". (2) FAIL if any file under `SETUP.md`, `README.md`, `design/`, `skills/`, `generator/data/`, `docs/method.md`, `docs/project-instructions.md` or `docs/handoffs/` contains the text "python3 build_hub.py", "personal-assistant Project" or "named `learning-project`". (3) FAIL if `cmp design/theme.css kit/shell.css` reports a difference. (4) FAIL if the block that starts "You are auditing four units" differs between `docs/method.md` and `generator/data/brand-ai/hub.py`, or the block that starts "You are re-checking one unit" does. (5) FAIL if `docs/method.md`, `docs/sourcing-standard.md`, `docs/reader.md`, `docs/courses-index.md` and `docs/BACKLOG.md` together exceed 110,000 characters. Then list every row of the "Staleness checks due" table in `docs/courses-index.md` whose due date falls within 30 days of today. Success is a report of five verdicts and the staleness list; make no commit.

### F · Fix list, ranked by effort

Effort is my estimate. Severity is my judgement of what each fault costs if left: **high** means it can put wrong or private text in front of a reader or a chat now; **medium** means it misleads a chat that reads the file; **low** means it costs tokens or tidiness.

| Rank | Fix | Changes | Effort (my estimate) | Severity | Finding |
|---|---|---|---|---|---|
| 1 | Turn off "Use account memory" for the Project | Project settings | 1 min | high | F13 |
| 2 | Remove `project-instructions.md` from the knowledge | Project knowledge | 1 min | low | F2 |
| 3 | Set tool access to On demand | Account settings | 2 min | low | F14 |
| 4 | Add the Project exceptions to the preferences' format rule; paste the Scope paragraph | Preferences; Project instructions | 10 min | medium | F5 |
| 5 | Move the B3 and A1 rows to the changelog; recopy the Project's backlog | `docs/BACKLOG.md`, `docs/CHANGELOG.md`, `claude/BACKLOG-chats.md` | 10 min | medium | F10 |
| 6 | Archive the hand-off note; fix the `SETUP.md` §8 line, the backlog lane header and the two `build_hub.py` instructions | `docs/handoffs/…`, `SETUP.md`, `docs/BACKLOG.md`, `design/README.md`, `generator/data/_template/hub.py` | 20 min | medium | F9a, c, d, e |
| 7 | Replace the project instructions with D | Project instructions; `docs/project-instructions.md` | 20 min | medium | F7 |
| 8 | Create the weekly rot-check task | Scheduled tasks | 20 min | medium | F16, F12 |
| 9 | Make the build read the theme, or make `verify.py` fail on a mismatch | `kit/build.py` or `kit/verify.py` | 20 min | low | F11 |
| 10 | Cut the knowledge to the five files; rewrite `SETUP.md` §2 and §6 and `file-unit` §6 | Project knowledge; `SETUP.md`; `skills/file-unit/SKILL.md` (re-save the skill to the account) | 40 min | high | F1 |
| 11 | Point the four search-on lists to the index | `docs/method.md`, `SETUP.md`, `hub.py` (rebuilt with rank 12) | 15 min | medium | F8 |
| 12 | Delete the v5.1 record blocks from `hub.py`; rebuild, verify, publish Academy | `generator/data/brand-ai/hub.py`; Academy | 45 min | medium | F9b |
| 13 | Mirror the five files through the GitHub integration, if connected (sync is manual: "Sync now") | Project knowledge | 15 min | low | F3 |
| 14 | Rename `kit/BACKLOG.md` and fix the bare references | `kit/`, 16 files | 45 min | low | F4 |
| 15 | Generate the hub's audit prompts from `method.md` | `kit/mdcourse.py`, `hub.py` | 1 h | low | F12 |
| 16 | Redact private terms at build time; B1 erratum; `verify.py` check; decide on the public history | `kit/mdcourse.py`, `kit/verify.py`, B1; Academy | 2 h, plus his decision | high | F15 |
| 17 | Split the index into live and archive | `docs/courses-index.md`, `kit/index_check.py` | 2–3 h | low | F17 |

Ranks 11 and 12 sit together because rank 11's `hub.py` edit needs rank 12's rebuild; doing them in one chat saves one rebuild and publish. The three high-severity fixes are ranks 1, 10 and 16. If he does nothing else, he should do those three.

## Writer's unsure list

Fresh check 29 Oct 2026 (Fable 5.1): fix · 0 errors, 7 should-fix, 9 minor; all applied; report `audits/brand-ai/fresh-check-B4.md`.

Audit 2 29 Oct 2026 (Fable 5.1, stratified sample): PASS · 0 of 6 sampled FAIL, 0 of 20 checked; no errata; report `audits/brand-ai/audit-2.md`.

1. **Retrieval mode is inferred.** The Project's 907,260 characters exceed the 200K window under either tokens-per-character figure, and the help centre says retrieval switches on near the limit; the mode itself is not visible from the repository, and the "observed" list of documents by name was seen in a Claude Code session attached to the Project, which may receive the knowledge differently from a claude.ai chat.
2. **The Project copies were not opened.** Sizes come from the repository files they mirror; any copy uploaded before a later repository change differs from what was measured.
3. **That the five-file set will load whole** rests on the retrieval article's statement that a project returns to in-context processing below the threshold; the threshold itself is not published.
4. **Claude Code guidance applied to claude.ai.** "May pick one arbitrarily", the procedure-to-skill rule and the instruction-audit checks are written for `CLAUDE.md`; their use for project instructions is my analogy.
5. **Connector and memory costs are undocumented.** Anthropic says each connector takes space and gives no figure; how much memory enters a chat is not stated. F13 and F14 rest on the documented direction, without a size.
6. **The skill count is approximate.** "About 15 personal skills" comes from the setup notes of 28 October; Anthropic's built-in skills were not counted, so the 1,900-token figure is a floor.
7. **The public site was not opened.** F15 is measured on the local build that `deploy.sh` pushes; the live Pages site may differ if a deploy was skipped.
8. **Whether a new chat in the same Project loses the project-content cache** is undocumented (§4).
9. **Effort and severity figures** are my estimates throughout, with no measurement behind them.
10. **Scheduled tasks are in research preview** according to the Claude Code documentation; the behaviour the rot-check task relies on may change.

## Sources

All web sources opened 29 October 2026.

- Anthropic. *Agent Skills*. Claude Platform docs. https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview
- Anthropic. *Effective context engineering for AI agents*. Anthropic Engineering, 29 September 2025. https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
- Claude Code docs. *How Claude remembers your project* (Memory). https://code.claude.com/docs/en/memory
- Claude Code docs. *Automate work with scheduled tasks*. https://code.claude.com/docs/en/web-scheduled-tasks
- Claude Help Center. *Understanding Claude's personalization features*. https://support.claude.com/en/articles/10185728
- Claude Help Center. *How can I create and manage projects?* https://support.claude.com/en/articles/9519177
- Claude Help Center. *Retrieval augmented generation (RAG) for projects*, 10 September 2026. https://support.claude.com/en/articles/11473015
- Claude Help Center. *Use Claude's chat search and memory to build on previous context*. https://support.claude.com/en/articles/11817273
- Claude Help Center. *What are skills?*, 22 September 2026. https://support.claude.com/en/articles/12512176-what-are-skills
- Claude Help Center. *Using skills in Claude*. https://support.claude.com/en/articles/12512180-using-skills-in-claude
- Claude Help Center. *Manage Claude's tool access*, 16 March 2026. https://support.claude.com/en/articles/13730515-manage-claude-s-tool-access
- Claude Help Center. *Usage and length limits* (article 11647753). https://support.claude.com/en/articles/11647753
- Claude Help Center. *Usage limit best practices*, 22 September 2026. https://support.claude.com/en/articles/9797557-usage-limit-best-practices
- Claude Help Center. *Schedule recurring tasks in Claude Cowork*. https://support.claude.com/en/articles/13854387-schedule-recurring-tasks-in-cowork
- Claude Help Center. *Use the GitHub integration*. https://support.claude.com/en/articles/10167454
- GitHub Docs. *Removing sensitive data from a repository*. https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository
- Learning Project files cited by name, at commit `b4fea09` of `apcanario/learning`, 29 October 2026: `docs/method.md` Home, §3, §4, §5, §6, §7, §8; `docs/project-instructions.md`; `docs/courses-index.md`; `docs/BACKLOG.md`; `docs/CHANGELOG.md`; `docs/handoffs/2026-10-28-brand-ai-handoff.md`; `SETUP.md` §2, §6, §8; `README.md`; `design/README.md`; `design/theme.css`; `generator/data/brand-ai/hub.py`; `generator/data/brand-ai/units_data.py`; `kit/build.py`; `kit/verify.py`; `kit/index_check.py`; `kit/deploy.sh`; `kit/academy/`; `skills/file-unit/SKILL.md`; B1 · Mental model (`B1-mental-model.md`) §1, §2, §3, §6, §7; B2 · Choosing the model (`B2-choosing-the-model.md`) §2, §8; B3 · Prompting that holds up (`B3-prompting-that-holds-up.md`) §4, §5. The Learning Project's setup as of 28 October 2026 (preferences, Project knowledge list, skills, connectors, scheduled tasks) is cited as observed, not as a published source.
