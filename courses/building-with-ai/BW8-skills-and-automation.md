---
code: BW8
title: Skills and automation
course: building-with-ai · BW · Building with AI
model: Opus 5.5
written: 2026-11-16
search: off
---

# BW8 · Skills and automation

This unit was written with search off. Searches were used only to re-verify the sources it cites and every product fact it carries, on 16 November 2026; each product fact (a limit, a feature, a plan, a date) carries the day it was read on the vendor's own page, and most of those pages show no date of their own. Each practice carries an evidence grade, as in BW1 to BW7: **measured** (a study or test with numbers), **documented practice** (a vendor or a named practitioner says to do it; nobody measured it here) or **stated opinion**. No page read for this unit publishes a measured rate at which skills trigger, so nothing about triggering here is graded measured.

What this unit assumes, by section, without restating it: the layers of a project and what loads every turn (BW1 §6 and §8; BW4 §1 and §2); the project structure and the monthly rot check (BW4, Deliverable Parts 1 to 4); the build order (BW5, Deliverable 2b); the verification protocol, its tiers, sample sizes and checker brief (BW6 §5 and Deliverable, steps C, E and F); and the pipeline form, its three kinds of gate and its run log (BW7 §3, §5 and §7). What it adds: how to turn one repeated procedure into a file the assistant loads on its own, how to prove it loads when it should, which of its steps a script must do, and which work can run on a clock without you.

## 1 · Three forms a reusable procedure takes, and how to choose

By the time you reach this unit you repeat several procedures: the checker brief of BW6, the stages of your BW7 pipeline, the rot check of BW4. Each can live in one of three forms, and they differ in one thing: when the text reaches the model's window (BW1 §1).

**A saved prompt.** A brief you keep in a file and paste, or attach, when you need it: BW3's ten templates are saved prompts. It enters the window only when you put it there, so it costs nothing in the chats that do not use it and it never fires by mistake. Its cost is that you must remember it exists and fetch it. Claude Code has a form of the same thing that you call by name: "Custom commands have been merged into skills", and a skill whose front matter sets `disable-model-invocation: true` is one Claude cannot load on its own, only you with `/name` ([Anthropic, *Extend Claude with skills*, Claude Code documentation](https://code.claude.com/docs/en/skills.md), read 16 Nov 2026; vendor).

**A project instruction.** Text that reaches every turn of every chat in one project (BW4 §1). It is the right home for a rule every chat must obey and the wrong home for a procedure: Claude Code's own rule for its instruction file is to move a multi-step procedure into a skill, which BW4 §1 applies to claude.ai's project instructions by inference. Academy (Academy case) is a library of self-study courses built by one person with Claude in October and November 2026; it is one project, so everything it shows is an anecdote. A structure audit of that project found project instructions that carried procedures and paraphrased the method file (Academy case file §1, §7; BW4 §7).

**A skill.** A folder the assistant reads in two steps: its name and description in every chat where it is installed, its body only when a request matches the description (§2). It costs a little in every chat, fires without being asked, and can carry scripts. Claude Code's documentation states when to make one: when you "keep pasting the same instructions, checklist, or multi-step procedure into chat", or when a section of the instruction file "has grown into a procedure rather than a fact" (*Extend Claude with skills*, read 16 Nov 2026; vendor, documented practice).

How to choose (stated opinion, each branch traced to the paragraphs above or to §7). A one-step instruction needs none of the three forms: it is a line in the brief that needs it (BW3).

```viz
{
  "kind": "decision",
  "root": {
    "q": "Must it hold in every chat of the project, whatever the task?",
    "tone": 4,
    "branches": [
      {"label": "yes", "to": {"outcome": "Project instruction: one rule", "tone": 3}},
      {"label": "no", "to": {
        "q": "Is it a procedure of several steps, done the same way each time?",
        "tone": 4,
        "branches": [
          {"label": "no", "to": {"outcome": "A line in the brief that needs it", "tone": 5}},
          {"label": "yes", "to": {
            "q": "Have you run it at least three times by hand?",
            "tone": 4,
            "branches": [
              {"label": "no", "to": {"outcome": "Saved prompt: run it and count", "tone": 2}},
              {"label": "yes", "to": {
                "q": "Should it start on its own when a request matches?",
                "tone": 4,
                "branches": [
                  {"label": "no", "to": {"outcome": "Saved prompt, called by name", "tone": 2}},
                  {"label": "yes", "to": {"outcome": "Skill", "tone": 1}}
                ]
              }}
            ]
          }}
        ]
      }}
    ]
  },
  "caption": "Choosing the form of a reusable procedure (§1 of this unit; stated opinion). The rule for instructions against skills is Claude Code's, in Extend Claude with skills, applied to claude.ai projects by BW4 §1; the count of three is §7's; the name-only form is Claude Code's disable-model-invocation, read 16 Nov 2026."
}
```

The last question matters more than it looks. A skill that fires on its own can fire on the wrong request (§3), and every installed skill adds its description to every chat (§2). A procedure you only ever start on purpose, such as a monthly check, loses nothing as a saved prompt.

## 2 · What a skill is, as its format defines it

The format has its own specification, published at agentskills.io: "A skill is a directory containing, at minimum, a `SKILL.md` file", with optional folders for scripts, references and assets ([Agent Skills, *Specification*](https://agentskills.io/specification.md), read 16 Nov 2026; the format's documentation, whose publisher the page does not name; graded here as vendor documentation, as the Sources list files it). `SKILL.md` is YAML front matter followed by Markdown. Two fields are required:

- **`name`**: at most 64 characters, lowercase letters, digits and hyphens only, not starting or ending with a hyphen, no two hyphens together, and it "Must match the parent directory name" (*Specification*).
- **`description`**: 1 to 1,024 characters; it "Describes what the skill does and when to use it", and should hold the keywords that help an agent pick it (*Specification*).

Anthropic's documentation of the same format adds two rules of its own: the name "Cannot contain reserved words: `anthropic`, `claude`", and neither field may hold XML tags; and it states the description requirement as "must include both what the Skill does and when Claude should use it" ([Anthropic, *Agent Skills*, Claude Platform Docs](https://platform.claude.com/docs/agents-and-tools/agent-skills/overview), read 16 Nov 2026; vendor). Both pages describe the same three-level loading, which BW1 §6 and BW4 §2 already use: at startup only the name and description, about 100 tokens a skill; the body when the skill is triggered, under 5,000 tokens; bundled files only when read, and for scripts "only their output enters context" (*Agent Skills*). The specification adds a size rule: keep `SKILL.md` "under 500 lines" and move detail into referenced files one level deep (*Specification*). All of this is documented practice; nobody has published a measurement of what happens past those sizes.

Where a skill lives decides who can load it. On 16 November 2026:

- **claude.ai.** Skills are on the Free, Pro, Max, Ultra, Team and Enterprise plans by the help page, while Anthropic's *Agent Skills* page lists custom skills, the kind the Deliverable uploads, on Pro, Max, Ultra, Team and Enterprise only (both read 16 Nov 2026); and "This feature requires code execution to be enabled"; individuals turn code execution on in Settings > Capabilities and switch skills on under Customize > Skills ([Claude Help Center, *Use skills in Claude*](https://support.claude.com/en/articles/12512180-use-skills-in-claude), read 16 Nov 2026; vendor). A custom skill is uploaded as a ZIP, and "The ZIP should contain the skill folder as its root (not a subfolder)" ([Claude Help Center, *How to create custom skills*](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills), read 16 Nov 2026; vendor).
- **Claude Code.** A personal skill sits in `~/.claude/skills/<name>/` and loads in your projects on that machine, "but not Cowork or cloud sessions"; a project skill sits in the repository's `.claude/skills/<name>/` and loads in sessions in that repository, "but not cloud threads in a project" (*Extend Claude with skills*, read 16 Nov 2026).
- **Network.** On claude.ai, skills "might have full, partial, or no network access" depending on settings; through the API they have none (*Agent Skills*, read 16 Nov 2026). A script inside a skill that must run everywhere uses nothing outside its own folder (§5).

> **Where sources disagree.** Anthropic's developer documentation says "Custom Skills do not sync across surfaces" and that Claude Code's skills are "filesystem-based and separate from both claude.ai and the API" (*Agent Skills*). Claude Code's own documentation says the skills enabled for your claude.ai account load in Cowork sessions, cloud sessions and terminal sessions signed in with that account, the last downloaded into `~/.claude/skills/synced/` from version 2.1.273 (*Extend Claude with skills*). Both were read on 16 Nov 2026. Read together: a skill uploaded to claude.ai is documented to reach Claude Code's cloud sessions by one page and not by the other, so the Deliverable also commits the folder to the repository, the route both pages document.

Anthropic's developer documentation warns about installing skills: "Use Skills only from trusted sources", because a malicious skill "can direct Claude to call tools or run code" against its stated purpose, and "Treat like installing software" (*Agent Skills*, read 16 Nov 2026; vendor). §8 turns that into rules for what you put in your own.

## 3 · How triggering works, and why the description matters more than the body

At the moment the model decides whether to use a skill, the body is not in its window. Only the name and description are (§2). The agentskills.io guide to descriptions puts the consequence in one line: "the description carries the entire burden of triggering" ([Agent Skills, *Optimizing skill descriptions*](https://agentskills.io/skill-creation/optimizing-descriptions.md), read 16 Nov 2026; the format's documentation). Anthropic's guide says the same at more length: Claude uses the description to choose among "potentially 100+ available Skills", and the rest of `SKILL.md` "provides the implementation details" ([Anthropic, *Skill authoring best practices*](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices.md), read 16 Nov 2026; vendor). A body the model never loads does nothing, however good it is. This is the fault BW1's diagnosis table sends here: a skill that fires when it should not, or fails to fire, is a description fault first (BW1, Deliverable Part 3).

**What the guidance asks of a description** (documented practice, vendor and format documentation, all read 16 Nov 2026):

- **What it does, and when to use it, in the words a request would contain.** "Be specific and include key terms"; Anthropic's bad examples are "Helps with documents", "Processes data" and "Does stuff with files" (*Skill authoring best practices*).
- **Lean towards firing.** "Err on the side of being pushy": list the contexts where the skill applies, including requests that do not name its domain (*Optimizing skill descriptions*).
- **Expect simple requests to bypass it.** Agents typically consult a skill only for a task beyond what they can do alone, so a one-step request "may not trigger a PDF skill even if the description matches perfectly" (*Optimizing skill descriptions*). A skill for a multi-step procedure is the case the description is for.
- **Put the use first.** Claude Code truncates the combined `description` and `when_to_use` text at 1,536 characters in its listing, a default it lets you change; with many skills it drops whole descriptions to fit a budget that "scales at 1% of the model's context window", starting with the skills you invoke least (*Extend Claude with skills*). The first words are the ones every surface keeps.

> **Where sources disagree.** Anthropic's guide says "Always write in third person", because "The description is injected into the system prompt" and a shifting point of view "can cause discovery problems"; its good example is "Processes Excel files and generates reports" (*Skill authoring best practices*). The agentskills.io guide says "Use imperative phrasing", "Use this skill when…" rather than "This skill does…" (*Optimizing skill descriptions*). Neither page cites a test. Read together: open in the third person with what the skill does, and end with a sentence that begins "Use when", as Anthropic's examples do; the agentskills.io guide's example begins "Use this skill when", which the Deliverable's `lint` does not accept.

**How long it may be.** The limits differ by surface, and the strictest decides:

```viz
{
  "kind": "compare",
  "unit": "",
  "max": 1536,
  "rows": [
    {"label": "This unit's skill (Deliverable)", "value": 193, "tone": 2},
    {"label": "claude.ai upload", "value": 200, "tone": 1},
    {"label": "Format specification and Claude Platform", "value": 1024, "tone": 3},
    {"label": "Claude Code listing cap", "value": 1536, "tone": 4}
  ],
  "caption": "Limits on a skill's description, in characters, by surface, against the Deliverable's own description (§3 of this unit). From Claude Help Center, How to create custom skills (200); Agent Skills, Specification, and Anthropic, Agent Skills (1,024); Anthropic, Extend Claude with skills (1,536, description and when_to_use combined, a default the page says is configurable). All read 16 Nov 2026."
}
```

The claude.ai help page gives the description as "(200 characters maximum)" (*How to create custom skills*, read 16 Nov 2026); the specification and Anthropic's platform page allow 1,024. A description meant to work on claude.ai is therefore written to 200 characters, with the trigger words first (stated opinion). The Deliverable's is 193.

**The front matter has to parse.** Claude Code reads the front matter only when the opening `---` is the first line of the file; when the YAML fails to parse, "the skill still loads with no fields set", so `/name` works and Claude "can't match against your `description`" (*Extend Claude with skills*, read 16 Nov 2026). The skill exists and never fires on its own. One way to break it (this unit's example; no page read says which way is commonest) is a colon followed by a space inside an unquoted value, which a strict YAML parser reads as a second key; double quotes around the description prevent it. The Deliverable's script checks this before upload (`check.py lint`).

**What a description cannot do.** It raises the chance that the skill loads; nothing makes it certain. Claude Code's troubleshooting for a skill that does not fire starts with "Check the description includes keywords users would naturally say", then checking that the skill is listed, rephrasing the request and calling the skill by name; for a skill that fires too often it says to make the description more specific or set `disable-model-invocation: true` (*Extend Claude with skills*, read 16 Nov 2026). The claude.ai help page's advice is the same in short: "Try being more explicit in your request" (*Use skills in Claude*, read 16 Nov 2026). When a step must happen every time, the description is the wrong tool (§8).

## 4 · Testing whether it triggers

Because no vendor publishes a trigger rate, the only rate you have is the one you measure on your own skill. The format's documentation gives a method (documented practice; *Optimizing skill descriptions*, read 16 Nov 2026):

1. **Write about twenty requests**, "8-10 that should trigger and 8-10 that shouldn't". Vary the should-trigger ones in phrasing, explicitness, detail and complexity; the most useful are those where the need is described without the skill's own words.
2. **Make the negatives near-misses**: requests that "share keywords or concepts with your skill but actually need something different". A request with no shared words tests nothing.
3. **Run each request three times**, because the same request can fire the skill on one run and not the next, and compute a trigger rate. A should-trigger request passes above 0.5; a should-not-trigger request passes below it.
4. **Hold some back.** About 60% of the set guides changes to the description; about 40% is kept aside and used only to see whether a change generalises. Five rounds of revision are usually enough, by the same page.

**How you see that it fired.** On claude.ai the help page says to "Review Claude's thinking to confirm it's loading the skill" (*How to create custom skills*, read 16 Nov 2026). In Claude Code, the agentskills.io page gives a script that runs each request with `claude -p` and JSON output and looks for a call to the Skill tool naming your skill (*Optimizing skill descriptions*). A third signal costs nothing on either surface: make the skill's first instruction a fixed first line of the reply, so a run that loaded it says so where you can see it (stated opinion; the Deliverable's skill opens every reply with its own name).

**What a passing set proves.** Little, at sixteen requests. On BW6 §5's arithmetic, sixteen clean runs bound a failure rate only below about 17% at 95% (1 − 0.05^(1/16) = 17.1%, this unit's arithmetic), and each request here is one draw of a different question, not sixteen draws of one. A passing set says the description is not badly wrong; the misfires you see in use say the rest. Keep the set, rerun it after every change to the description, and add each real misfire to it as a new row (stated opinion).

## 5 · Scripts inside a skill for the steps that must be exact

A skill's body is instructions, and instructions are followed with some probability (BW1 §6). For steps where an approximate result is a wrong result, the format offers something better: a script in the skill's `scripts/` folder, which the model runs and does not read. Anthropic's guide grades the choice by "degrees of freedom": low freedom, meaning a specific script with few or no parameters, where "Operations are fragile and error-prone", consistency is critical, or a specific sequence must be followed; and it says to "Prefer scripts for deterministic operations", since a prepared script is "more reliable than generated code", saves tokens and is consistent across uses (*Skill authoring best practices*, read 16 Nov 2026; vendor, documented practice). The specification asks that scripts be self-contained or document their dependencies, and "Include helpful error messages" (*Specification*). A script costs the window only what it prints (§2).

Which steps must be exact is already settled by earlier units. BW7 §3 calls them code gates: anything countable or matchable, such as a length, a required heading, a quotation found verbatim in its source. BW6's protocol has four more: counting the checkable claims, drawing the sample by number and never by eye, applying the decision rule with an acceptance number of zero, and computing what a clean sample proves (BW6 §5, Deliverable step C). BW2's routing table already says numbers come from code (BW2, row 2). The rule this unit uses (stated opinion, on those units and the guide above):

- **Every code gate runs before the first model stage**, so a model never spends its turn on an input that fails a check a script could make. A draft without a Sources list, with a private term in it, or with a quotation not found in the saved copy of its source, stops there.
- **A script makes every number and every draw**: N, the sample, the bound, the counts on the verdict line.
- **A script checks the model's own output against its form** before anyone reads it: every finding quotes text that occurs once in the draft; the counts on the last line match the findings.
- **A script writes the log line**, in BW7 §7's form, with a hash of each input file as its version, so the line says exactly what was read.
- **The judgement stays with the model, and the decision with you.** Whether a source supports a claim is the model's step; whether to apply a finding, and the final pass, are yours (BW7 §5).

The Academy case runs two scripts of this kind (anecdote). A script checks the course index after each filing chat writes its records, and restores every file if the check fails; another checks the public course's data against a list of private terms, and the course's fresh checker also checks each unit against that list (Academy case file §1, §7). The case file does not record when the terms check was added relative to the structure audit that found private terms in a public build (Academy case file §7), nor whether either script lives inside a skill `[NOT IN CASE FILE]`.

The Deliverable's skill puts the steps in this order:

```viz
{
  "kind": "flow",
  "steps": [
    {"label": "1 · Code gates", "note": "script: sources, terms, quotations", "tone": 3},
    {"label": "2 · List claims", "note": "script, then the model adds", "tone": 2},
    {"label": "3 · Draw", "note": "script: census or sample, by seed", "tone": 3},
    {"label": "4 · Check", "note": "the model opens each source", "tone": 2},
    {"label": "5 · Report", "note": "the model writes it", "tone": 2},
    {"label": "6 · Report gate", "note": "script: form, counts, rule C5", "tone": 3},
    {"label": "7 · Log", "note": "script: BW7 §7 line", "tone": 3},
    {"label": "8 · Your pass", "note": "verify, apply, publish", "tone": 1}
  ],
  "caption": "The stages of the Deliverable's check-against-sources skill, by who runs each (§5 of this unit): scripts for the exact steps, the model for the judgement, you for the decision. Built on BW6, Deliverable steps C to F, and BW7 §3 and §7."
}
```

## 6 · Scheduled tasks: what they can and cannot touch

A scheduled task is a saved prompt that runs on its own at set times, in a session that knows nothing of the chat that created it (BW1 §3). BW4 §1 placed it among the layers of a project; this section re-reads its limits on the day of writing, because the feature is in research preview and its pages change. Everything below was read on 16 Nov 2026 on Anthropic's page, *Automate work with scheduled tasks* ([Claude Code documentation](https://code.claude.com/docs/en/web-scheduled-tasks); vendor), unless another page is named.

**What it is.** "A cloud scheduled task, formerly a routine," is a saved Claude Code configuration of a prompt, one or more repositories and a set of connectors, run on Anthropic's cloud so that it keeps working when your computer is closed. The page says scheduled tasks "are in research preview" and that behaviour, limits and the API "may change". They are on the Pro, Max, Team and Enterprise plans, and you create them at claude.ai/code/routines, in the desktop app, or with `/schedule` in Claude Code.

**What a run can touch.**

- **The repositories you select.** "Each repository is cloned at the start of a run." Claude pushes to a branch prefixed `claude/` unless the prompt says otherwise. Branch protection on GitHub limits that, with one condition: "a rule that access can bypass doesn't block a run's push", so a rule your own connected account can bypass does nothing.
- **Skills.** A run "uses skills"; outside a project's threads these include the ones committed to the cloned repository.
- **Connectors, with writes.** All your connectors are included by default; "Remove any the task doesn't need", because Claude can use an included one during a run, "including writes". Anything done through them "appears as you".
- **The network its environment allows.** The default environment allows only an allowlist of package registries, cloud provider APIs and common development domains; requests to other hosts "fail with `403`". Connectors reach their services through Anthropic's servers and bypass that list.

**What it cannot touch, or cannot do.**

- **Your computer.** A cloud run works on a fresh clone and has no access to local files; that is a Desktop scheduled task, a separate feature that runs on your machine ([Anthropic, *Run prompts on a schedule*, Claude Code documentation](https://code.claude.com/docs/en/scheduled-tasks), comparison table, read 16 Nov 2026).
- **Ask you anything and wait for a quick answer.** A run starts in auto mode, where "a classifier model allows or blocks actions"; an action that still needs approval stops the run until you open it.
- **Treat its own prompt as your consent.** The fired prompt is "not live user input and can't act as approval or consent" for anything the run does.
- **Run more often than hourly.** "Expressions that run more often than once per hour are rejected." A run set exactly on the hour "can start several minutes late", so the page suggests a few minutes past it.
- **Run for free.** Runs "draw down subscription usage the same way interactive sessions do", and past 100 scheduled runs an hour on one account, a run waits until the hour resets.

The prompt "must be self-contained and explicit about what to do and what success looks like" (same page). The three ways Claude Code can schedule work differ in what they reach, by the comparison table as *Schedule recurring tasks in Claude Code Desktop* prints it ([Anthropic, Claude Code documentation](https://code.claude.com/docs/en/desktop-scheduled-tasks), read 16 Nov 2026; vendor). The copy of that table on *Run prompts on a schedule* gives the Desktop task's minimum interval as 1 minute and the cloud task's permission prompts as "No (runs autonomously)", so two of the vendor's own pages differ: a cloud task runs on Anthropic's cloud, needs neither your machine nor an open session, works on a fresh clone with no local files, starts in auto mode and runs at most hourly; a Desktop task runs on your machine, which must be on, needs no open session, reaches local files, has its permission prompts set per task, and runs at most hourly in its forms or every minute when Claude sets it; `/loop` runs on your machine, which must be on, inside an open session, reaches local files, takes that session's permissions and can repeat every minute (all by the Desktop page's table); a recurring `/loop` task expires seven days after it is created (*Run prompts on a schedule*, read 16 Nov 2026; vendor).

```viz
{
  "kind": "matrix",
  "cols": ["Cloud task", "Desktop task", "/loop"],
  "rows": [
    {"label": "Runs on", "cells": ["Anthropic's cloud", "your machine", "your machine"]},
    {"label": "Machine must be on", "cells": ["no", "yes", "yes"]},
    {"label": "Session must be open", "cells": ["no", "no", "yes"]},
    {"label": "Local files", "cells": [{"mark": "no: fresh clone", "tone": 1}, {"mark": "yes", "tone": 3}, {"mark": "yes", "tone": 3}]},
    {"label": "Permission prompts", "cells": ["auto mode", "set per task", "as the session"]},
    {"label": "Minimum interval", "cells": ["1 hour", "1 hour in forms, 1 minute by Claude", "1 minute"]}
  ],
  "caption": "Claude Code's three ways to schedule work, by what each reaches (§6 of this unit). From Anthropic, Schedule recurring tasks in Claude Code Desktop, its comparison table, read 16 Nov 2026 (vendor); the copy of the table on Run prompts on a schedule differs on two cells (§6). A /loop task also expires seven days after it is created, by Run prompts on a schedule."
}
```

**Which task to schedule.** A task that runs without you suits work that is mechanical, has a fixed input and a pass-or-fail result, and touches nothing it cannot undo (BW7 §3 and §6; stated opinion). BW4 built such a job and said this unit would automate it: the monthly rot check, whose steps 2, 3 and 6 are mechanical and whose steps 1, 4 and 5 need reading (BW4, Deliverable Part 2). The Deliverable schedules that, with one more mechanical check BW5 states by hand: no unit's Takes entry points to a unit below it in the build order (BW5, Deliverable 2b). Three of its parts stay with you, for reasons the page above gives: the reading steps need judgement; the comparison of the claude.ai instructions field with its canonical file needs claude.ai, which a cloud run cannot open; and the private-terms search needs a list that BW4 keeps outside the repository, which a cloud run, working on a fresh clone, cannot read. The run writes a report and a log line to a `claude/` branch, and you read it.

The skill itself is not scheduled, and the reason is its input: a fresh check starts when a draft is finished, which is an event, not a date. A check run on a timetable would find either nothing new or a draft that is not ready (stated opinion). It also opens every cited page, and the default environment allows only its allowlist (above).

## 7 · Counting the repeats before automating

A skill costs three things before it saves anything: the time to write it and its script, the time to test it (sixteen requests, three runs each, is 48 runs), and a description in the window of every chat where it is installed, about 100 tokens on Anthropic's figure (§2), whether or not that chat uses it. It also needs upkeep: every product fact inside it is dated and goes stale (§8). No source read for this unit measures any of these in hours, and the Academy case file records no hours per unit or per check (Academy case file §9).

So count before you build (stated opinion, built on the costs above and BW2 §7's habit of deciding from your own record):

1. **Count the runs.** Write down each time you do the procedure by hand, with the date and the minutes it took. The Claude Code documentation's trigger for a skill is repetition: you "keep pasting" the same procedure (§1). Software has a long-standing rule of thumb for the same decision, the rule of three: code repeated twice is left alone and extracted the third time; it is attributed to Don Roberts and was popularised by Martin Fowler's *Refactoring* (1999), as Wikipedia's article reports it ([Wikipedia, *Rule of three (computer programming)*](https://en.wikipedia.org/wiki/Rule_of_three_(computer_programming)), read 16 Nov 2026; the book itself was not read for this unit, so this is a reporter's account of a documented practice).
2. **Check that the runs were the same.** Three runs that each needed different steps are three briefs, not one procedure (BW7 §1: work whose steps change each time is a brief, not a pipeline).
3. **Do the arithmetic.** A skill pays when the runs ahead, times the minutes each saves, exceed the minutes to build, test and keep it. Illustrative arithmetic, unmeasured: a check that takes you 20 minutes to brief and run by hand and 5 with the skill saves 15 a run; if the skill takes four hours to write and test, it pays after 16 runs (240 ÷ 15).
4. **Count what a script saves separately.** A step a script does exactly (a count, a draw, a match) also removes a kind of error, which the minutes do not show.

**The case** (anecdote). The fresh check is the Academy case's most repeated procedure on its record: 36 drafts got one before filing, and 28 of them had at least one error (Academy case file §5). The case file describes it as one procedure: a context that has not seen the unit written, every cited claim against its source, findings graded and never edited (Academy case file §2); the checker's model varied across the 36 (Fable 5.1, Opus 5.5, Fable 5.2; §5). On the count, it passes; the case file does not record the minutes per check, or whether the case wrote the check as a skill `[NOT IN CASE FILE]`.

## 8 · What a skill must never hold

A skill is a file that loads into chats you have not planned, and it can run code (§2). Six things stay out of it.

1. **Keys, passwords and secrets.** "Don't hardcode sensitive information (API keys, passwords)" (*How to create custom skills*, read 16 Nov 2026; vendor). A skill is copied, zipped, uploaded and committed; anything in it travels with it. For a scheduled run, Claude Code's page sends API keys to the environment's network secrets rather than to visible variables (*Automate work with scheduled tasks*, read 16 Nov 2026).
2. **Private terms, and the list of them.** The case found private terms reaching a public build (Academy case file §7), and BW4 keeps the list outside the repository so the list itself is never built or pushed (BW4, Deliverable Part 1). A skill that checks for the terms reads the list from outside its own folder and never prints a term (the Deliverable's script prints "term #3 at line 120").
3. **Facts that change.** "Don't include information that will become outdated", or put it in a section marked as old (*Skill authoring best practices*, read 16 Nov 2026). Model names, prices and limits belong in the project's dated files, which the skill names by path (BW4 §5: one source of truth).
4. **A rule that must hold in every chat.** A skill loads only on a match (§3), so a standing rule placed there is absent from every chat that does not match; it belongs in the instructions (BW4 §1). And a rule that must hold every time, even inside the skill's own task, belongs in something that does not depend on the model: Claude Code's advice when Claude skips such a rule is to "move the rule into a hook", a script that runs on an event whatever the model does (*Extend Claude with skills*, read 16 Nov 2026; BW1 §6).
5. **A copy of another file.** A skill that restates the method in its own words is the paraphrased duplicate BW4 §6 names as the dangerous kind. It points to the file instead.
6. **Your final pass.** A skill reports and stops. Approving, applying, publishing and sending stay with you (BW7 §5), and a scheduled run's prompt cannot stand in for your consent (§6).

## 9 · On other tools

The principles of §1 to §8 (a procedure loaded on a match, a description that decides loading, a trigger test with near-misses, scripts for exact steps, unattended runs only for mechanical work, a count before building, nothing secret or stale in the file) need no particular product; the format itself is published as a specification any client can implement (§2). What is specific to a vendor, as read on 16 Nov 2026:

| Claim in this unit | Claude | ChatGPT and OpenAI | Gemini and Google |
|---|---|---|---|
| A skill is a folder with a `SKILL.md`; name and description decide when it is used (§2, §3) | [*Agent Skills*](https://platform.claude.com/docs/agents-and-tools/agent-skills/overview); [*Specification*](https://agentskills.io/specification.md) | "A SKILL.md file is the skill's playbook"; the name and description help ChatGPT recognise when a skill is relevant; a skill can also be called with @: [*Using skills*](https://openai.com/academy/skills) (OpenAI Academy, 10 Apr 2026) | Skills are reusable custom instructions; Gemini can "automatically run them whenever you enter a matching prompt", or you type `/` and the name: [Tokuno, *Let skills in Gemini tackle your most repetitive tasks*](https://blog.google/products-and-platforms/products/gemini/automate-tasks-with-skills/) (Google, 30 Sep 2026). No `SKILL.md` format named on the page |
| Description limit (§3) | 200 on claude.ai, 1,024 on the platform, 1,536 in Claude Code's listing | No limit stated on the page read | No limit stated on the pages read; a skill's files are limited to 100 MB, by the Gems transition page |
| A trigger test with near-misses (§4) | Format documentation, not Claude-specific: [*Optimizing skill descriptions*](https://agentskills.io/skill-creation/optimizing-descriptions.md) | No equivalent found on the page read | No equivalent found on the pages read |
| Scripts inside a skill (§5) | Code execution required on claude.ai (*Use skills in Claude*) | Not stated on the page read | Skills can hold reference files (text, PDFs, images); scripts not mentioned (Tokuno, 2026) |
| Scheduled runs (§6) | [*Automate work with scheduled tasks*](https://code.claude.com/docs/en/web-scheduled-tasks) | Not checked: OpenAI's help page on scheduled tasks failed to load on 16 Nov 2026 | Up to 10 active schedules; a schedule uses another app only if it is connected; responses are prepared in advance, so fast-changing data may not be current: [*Schedules in Gemini Apps*](https://support.google.com/gemini/answer/16316416?hl=en-GB) |
| Legacy form | None | None | **Gems are legacy.** On personal accounts of users 18 and over, Gems convert to skills and become read-only on 17 Nov 2026 and are removed on 17 Dec 2026; Workspace business, enterprise and non-profit accounts follow in March 2027, education in June 2027; under-18 accounts later, date not announced: [*About the transition from Gems to skills*](https://support.google.com/gemini/answer/18560919) (Gemini Apps Help, undated) |

A procedure kept as a Gem is a procedure kept in a feature with an end date. The procedure belongs in your own files (BW4 §5), with any product holding a copy.

## Deliverable · A skill that checks a draft against its sources, tested, with one scheduled task

Two parts. Part 1 is the skill built in full on the Academy case and ready to install: the folder, `SKILL.md`, its checking script, the install steps, a sixteen-request trigger test set, one scheduled task (the monthly rot check, with its own script) and the done-when lines. Part 2 is the template for your project; each blank says what goes in it. BW9's agents load a skill in this form: front matter that parses, a stop condition first, numbered steps each with its input, output and gate, scripts for the exact steps, a **Never** list and done-when lines.

Conventions, as in BW4 to BW7. Every fact about Academy comes from the Academy case file and is cited by section; where the case file holds no value, the text says `[NOT IN CASE FILE: …]`, a blank for the project's owner and never a claim. File paths follow BW4's Part 1 folders and BW7's Part 1 steps, which are those units' proposals; the case file names no paths. Product facts are as read on 16 Nov 2026; model names are from BW2's routing table, read 15 Nov 2026.

**What the skill takes from earlier units, and where it departs.** It is BW6's checker brief (Deliverable step E) turned into steps, and it keeps BW6's three tiers and their sample sizes (9, 14, 29), the census when a text has no more claims than its tier's sample, the acceptance number of zero, the early stop on an invented item, the sweep on STALE, and the five-item output form (BW6 §5; Deliverable steps C and E). Two changes, each for a script's sake: the claims table in item 1 carries a verdict column, so that a script can apply rule C5 rather than the model; and after one claim from every section, the extra draws are taken at random from all remaining claims, so larger sections give more draws in proportion, which is this unit's reading of BW6's "extra draws from the largest strata" in a form a script can repeat from its seed. It runs as stage 3 of BW7's Part 1 pipeline (the fresh check), with BW7's code gates first and BW7 §7's log line last, and it stops before stage 4: applying findings stays with the maintainer, whether a person or a model `[NOT IN CASE FILE]`.

**Routing rows** (BW2). The check is row 5, critique of a draft, in census mode, and row 9, an audit against sources, in sample mode: large, top rung, a model other than the writer's, Fable 5.2, high; override Opus 5.5, high, recorded as the writer's model. One chat runs the whole skill on one model, so the claim-listing step, which is row 2's kind of work (extraction to a table), runs on row 5's model; the script does the listing first, so the model only corrects it. Applying verified findings and checking a figure against the text have no BW2 row (BW7 borrowed row 5 for both, by analogy); this skill automates neither.

### Part 1 · On the Academy case

The case's fresh check: a separate context that has not seen the unit written checks every cited claim against its source and the deliverable against the brief, grades its findings error, should-fix or minor, and never edits; a maintainer verifies each finding and applies it as an exact replacement (Academy case file §2). Units are published as one website, as an artifact on claude.ai and on GitHub Pages (Academy case file §1), so the tier is 3. The failure kinds in the skill's settings are the ones the case's reports name (§5) and the pattern its first audit named (§3).

#### A · The folder

    check-against-sources/
      SKILL.md                the procedure (below), 122 lines, 193-character description
      scripts/
        check.py              the exact steps: lint, gate, claims, sample, redraw, report, recheck, log

Committed in the case's repository at `.claude/skills/check-against-sources/` (BW4's Part 1 folders hold no `.claude/`; this path is Claude Code's, §2), and uploaded to claude.ai as a ZIP. The private-terms list stays at `private-terms.txt` beside the repository, never inside it (BW4, Deliverable Part 1). Nothing else goes in the folder (§8).

#### B · `SKILL.md`

    ---
    name: check-against-sources
    description: "Checks a draft's claims against its cited sources, by census or tiered sample, and reports findings without editing it. Use when asked to check, fact-check or verify a text against its sources."
    ---

    # Check against sources

    One check per chat, in a context that did not write the draft. This skill reports. It never edits the draft, never applies a finding, never publishes or sends anything. Every step marked **script** is run with `scripts/check.py` in this skill's own folder (in Claude Code, `${CLAUDE_SKILL_DIR}/scripts/check.py`, because the session's working directory is the repository root), never done by eye.

    ## Settings

    Fill once per project; the steps below read them.

    - **Tier:** 3. The draft is published to anyone. (1: for you alone; 2: shared, or a decision rests on it; 3: published, sent to a client, or with legal, financial or health consequences.)
    - **Mode:** census. Every cited claim is checked, as the project's fresh check does. Use `sample` only when the maintainer asks for one.
    - **Also look for:** a figure the cited page does not carry; an author named wrongly; a law or product fact that has changed; a quotation the page does not hold; a count that does not add up; a product fact that differs between two of the vendor's own pages; a qualifier the source does not carry.
    - **Private-terms list:** `../private-terms.txt`, kept outside the repository. If it is not on disk where this chat runs, skip that gate and say so in the report; never ask for the list to be pasted or uploaded.
    - **Expected model:** the model on rows 5 and 9 of the project's BW2 routing table, read from that file (path: `[NOT IN CASE FILE: where the case keeps its routing table]`), never the writer's model. Record in the report the model and version you ran as.
    - **Report goes to:** `checks/<unit code>-fresh-check.md`, with `claims.tsv` and `sample.tsv` beside it in `checks/<unit code>/`.
    - **Run log:** `records/run-log.md`.

    ## 0 · Before anything

    1. First line of the reply: `check-against-sources · <the model and version this chat runs as> · tier <n>, <mode>`. If that model is not the expected one, or is the model that wrote the draft, say so in the same line.
    2. You need the draft as a file. The brief it was written from and saved copies of its sources are optional. If the draft is missing, ask for it; ask nothing else.
    3. Read only the draft, its brief and its sources. Never read the writer's conversation, notes or unsure list: the check exists because it has not seen them.

    ## 1 · Code gates (script, before any model stage)

    Run:

        python3 scripts/check.py gate <draft> --brief <brief> --terms <private-terms list> --sources <folder of saved sources>

    Leave out an option whose file you do not have; pass `--sources` only when every cited page is saved as text there, since a page left out reads as a missing quotation.

    - `gate: PASS` → go on.
    - `gate: FAIL` → stop. Report the failing lines and nothing else. No model stage runs on a draft that fails a gate. The script prints where a private term was found, never the term.

    Then log it:

        python3 scripts/check.py log --stage "1 Gate" --run 1 --inputs <draft> <brief> --model "none: script" --output "gate output" --gate "code: PASS" --by script --append <run log>

    ## 2 · List the claims (script, then you)

        python3 scripts/check.py claims <draft> --out claims.tsv

    The script lists every sentence with a number, a quotation or a link, numbered, by section. Read the list. In its `status` column, write `drop: <reason>` beside a row that is not a checkable claim (a heading, a template blank). Add, as new rows `A01`, `A02` …, every claim the script missed: a mechanism, a recommendation, or an attribution with no number, quotation or link. Never delete a row.

    ## 3 · Draw what you will check (script)

        python3 scripts/check.py sample claims.tsv --tier <tier> --out sample.tsv

    Add `--census` in census mode. The script uses the tier's sample size (9, 14 or 29), takes every claim when there are no more than that, and otherwise draws one claim from every section and the rest at random by seed. Copy its first three lines into the report. **Do not open any source before `sample.tsv` exists.** Never swap a drawn claim for another.

    ## 4 · Check each drawn claim (you)

    For each row of `sample.tsv`, in order:

    1. Open the cited source. A source you cannot open is UNVERIFIABLE, never FAIL; run `python3 scripts/check.py redraw claims.tsv sample.tsv <id>` for a replacement from the same section, and check that one too.
    2. Compare the claim with what the source says: the figure, the sample, the date, the population, the qualifiers. Look in particular for the kinds listed under **Also look for**.
    3. Check that the source is the original (a page that repeats a figure is a reporter) and that its class is labelled: peer-reviewed; preprint; vendor, dated; practice; benchmark with version and date.
    4. Verdict: PASS (the source holds it), FAIL (wrong, unsupported, miscited, stretched or invented), STALE (true when written, superseded now: give the newer value and its source) or UNVERIFIABLE.

    In sample mode, also check in full, outside the sample, every figure and citation in the draft's deliverable or closing section. In both modes, check the deliverable against the brief: present, in full, as named.

    ## 5 · Write the report

    Markdown, in this form and order; the script reads it.

        # Check · <draft name>

        ## 1 · Claims
        N = <count> (<dropped> dropped as not checkable)
        <the sample script's first three lines>
        | id | section | claim, exact | cited source | verdict |
        |---|---|---|---|---|
        | C012 | <section> | "<the claim>" | <link> | PASS |

        ## 2 · Findings
        - [error] [§<section>] · Current: "<exact text, found once in the draft>" · Problem: <what is wrong> · Fix: "<replacement>" · Basis: <link>, <where on the page>

        ## 3 · Confirmed
        - <id> · <link> · "<the words on the page that hold it, under 15 words, exact>"

        ## 4 · Invented items
        none

        Verdict: <keep|fix|rewrite> · errors <n> · should-fix <n> · minor <n> · checker: <model and version you ran as>

    Grades: an **error** is a claim the source does not support, a miscitation, an invented item, or a part of the brief missing from the draft; a **should-fix** is a stretch, a missing label or date, or a reporter cited for an original; anything else is **minor**. Findings run most serious first. Style is minor at most. Write "none" under a heading with nothing in it. No praise and no summary of the draft.

    ## 6 · Gate the report (script)

        python3 scripts/check.py report <report> --draft <draft> --sample sample.tsv

    - `report: FAIL` → fix the report's form (a missing row, a `Current` text that is not found exactly once, a count that does not match) and run it again, twice at most. Never change a verdict to make the report pass.
    - The script prints the decision under BW6's rule C5: FULL CHECK on any invented item or any FAIL in a sample (acceptance number zero); SWEEP on any STALE; USE IT, with the bound a clean sample gives; CENSUS DONE when every claim was checked.

    Then:

        python3 scripts/check.py recheck <report>
        python3 scripts/check.py log --stage "2 Check" --run 1 --inputs <draft> sample.tsv --model "<model and version you ran as>, <effort>" --output <report> --gate "<report gate result>; <decision>" --by "<model and version>" --append <run log>

    ## 7 · Hand over, then stop

    Reply with three lines and the report's path: the decision line, the verdict line, and the five claim ids from `recheck`, which the maintainer re-opens. Then stop. The maintainer verifies every FAIL and STALE at its source before applying any fix, applies each as an exact replacement, and makes the final pass. None of that is this skill's.

    ## Never

    - Edit the draft, apply a fix, publish, send, or write any file other than the report, `claims.tsv`, `sample.tsv` and the log line.
    - Give a verdict on a claim whose source you did not open.
    - Quote 15 words or more from a source.
    - Print a term from the private-terms list.
    - Hold a key, a password or a private fact in this folder.

    ## Done when

    - The gate passed, or its failure is the whole report.
    - `sample.tsv` existed before any source was opened.
    - Every drawn claim has one verdict, and every finding quotes text found once in the draft, with its fix and its basis.
    - `check.py report` printed `report: PASS` and a decision.
    - Two log lines were appended, and the reply named the five claims to re-check.

#### C · `scripts/check.py`

Python 3, standard library only, so it runs where a skill's network access is partial or none (§2). It was run before this unit was handed in, on a filed unit of this course as the draft (BW6, 192 candidate claims in 10 sections; a tier 3 sample of 29 drawn with seed 42), on mock reports that pass and fail each rule, on a skill whose unquoted description holds a colon, and on a private-terms list.

    #!/usr/bin/env python3
    """check.py: the exact steps of the check-against-sources skill.

    Python 3 standard library only: no network, no packages, so it runs in
    claude.ai's code-execution sandbox, in Claude Code and on your own machine.
    Every step here is one a model should not do by eye: counting, drawing a
    sample by number, matching text exactly, applying the decision rule, and
    writing the log line.

      lint    SKILL_DIR                          the skill's own front matter and body
      gate    DRAFT [--brief F] [--terms F] [--sources DIR]
                                                 code gates, run before any model stage
      claims  DRAFT --out claims.tsv             candidate checkable sentences, by section
      sample  claims.tsv --tier 1|2|3 [--seed N] [--census] --out sample.tsv
                                                 census, or stratified sample drawn by number
      redraw  claims.tsv sample.tsv ID [--seed N]
                                                 replace an UNVERIFIABLE claim from its section
      report  REPORT --draft DRAFT --sample sample.tsv
                                                 the checker's report against its form; rule C5
      recheck REPORT [--seed N]
                                                 five PASS verdicts for you to re-open
      log     --stage S --run N --inputs F [F ...] --model M --output F --gate G --by WHO
              [--append LOG]                     one run-log line

    Exit status: 0 pass, 1 fail, 2 usage or input error.
    """
    import argparse
    import datetime
    import hashlib
    import math
    import os
    import random
    import re
    import sys
    import unicodedata

    # Tiers and their rates to rule out: BW6 section 5 (stated opinion there).
    # n is the smallest sample whose clean result rules the rate out at 95%.
    TIER_RATE = {1: 0.30, 2: 0.20, 3: 0.10}
    VERDICTS = ("PASS", "FAIL", "STALE", "UNVERIFIABLE")
    SEVERITIES = ("error", "should-fix", "minor")
    RESERVED = ("anthropic", "claude")
    CLAUDE_AI_DESC_LIMIT = 200      # claude.ai help centre, read 16 Nov 2026
    SPEC_DESC_LIMIT = 1024          # Agent Skills specification, read 16 Nov 2026
    BODY_LINE_LIMIT = 500           # same specification
    CONFIRM_WORD_LIMIT = 15         # quotations in Confirmed lines stay under this


    def sample_size(tier):
        p = TIER_RATE[tier]
        return math.ceil(math.log(0.05) / math.log(1 - p))


    def upper_bound(n):
        """Largest failure rate still consistent with n clean draws, at 95%."""
        return 1 - 0.05 ** (1 / n) if n > 0 else 1.0


    def die(msg):
        print("ERROR: " + msg)
        sys.exit(2)


    def read(path):
        if not os.path.isfile(path):
            die(f"no such file: {path}")
        with open(path, encoding="utf-8") as f:
            return f.read()


    def norm(text):
        """Fold quotes, dashes and spacing so that exact matching ignores typography."""
        text = unicodedata.normalize("NFKC", text)
        for a, b in (("“", '"'), ("”", '"'), ("‘", "'"), ("’", "'"),
                     ("–", "-"), ("—", "-"), (" ", " ")):
            text = text.replace(a, b)
        return re.sub(r"\s+", " ", text).strip().lower()


    def short_hash(path):
        with open(path, "rb") as f:
            return hashlib.sha256(f.read()).hexdigest()[:7]


    # ---------------------------------------------------------------- lint

    def front_matter(text):
        lines = text.split("\n")
        if not lines or lines[0].strip() != "---":
            return None, "the opening --- is not the file's first line"
        try:
            end = lines.index("---", 1)
        except ValueError:
            return None, "no closing --- line"
        fields = {}
        for raw in lines[1:end]:
            if not raw.strip():
                continue
            m = re.match(r"^([a-z_-]+):\s*(.*)$", raw)
            if not m:
                return None, f"cannot read front matter line: {raw!r}"
            key, value = m.group(1), m.group(2)
            if value[:1] in "\"'":
                if len(value) < 2 or value[-1] != value[0]:
                    return None, f"{key}: opening quote is not closed on the same line"
                value = value[1:-1]
            elif ": " in value or " #" in value:
                return None, (f"{key}: an unquoted value holds ': ' or ' #', which a strict "
                              f"YAML parser rejects; put the value in double quotes")
            fields[key] = value
        return (fields, "\n".join(lines[end + 1:])), None


    def cmd_lint(a):
        skill_md = os.path.join(a.skill_dir, "SKILL.md")
        text = read(skill_md)
        parsed, err = front_matter(text)
        fails, notes = [], []
        if err:
            print("FAIL front matter: " + err)
            return 1
        fields, body = parsed
        name, desc = fields.get("name", ""), fields.get("description", "")
        folder = os.path.basename(os.path.abspath(a.skill_dir))
        if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", name) or len(name) > 64:
            fails.append("name: 1 to 64 lowercase letters, digits and single hyphens")
        if any(w in name for w in RESERVED):
            fails.append("name: holds a reserved word (anthropic, claude)")
        if name != folder:
            fails.append(f"name {name!r} does not match its folder {folder!r}")
        if not desc:
            fails.append("description: empty")
        if len(desc) > SPEC_DESC_LIMIT:
            fails.append(f"description: {len(desc)} characters, over {SPEC_DESC_LIMIT}")
        if re.search(r"<[A-Za-z/]", desc):
            fails.append("description: holds an XML tag")
        if "use when" not in desc.lower():
            fails.append("description: no 'Use when' clause saying when to use it")
        if len(desc) > CLAUDE_AI_DESC_LIMIT:
            notes.append(f"description: {len(desc)} characters, over claude.ai's {CLAUDE_AI_DESC_LIMIT}")
        body_lines = body.count("\n") + 1
        if body_lines >= BODY_LINE_LIMIT:
            fails.append(f"body: {body_lines} lines, not under {BODY_LINE_LIMIT}")
        for ref in sorted(set(re.findall(r"scripts/[\w.-]+", body))):
            if not os.path.isfile(os.path.join(a.skill_dir, ref)):
                fails.append(f"body names {ref}, which is not in the folder")
        print(f"name: {name} ({len(name)} characters)")
        print(f"description: {len(desc)} characters")
        print(f"body: {body_lines} lines")
        for n in notes:
            print("NOTE " + n)
        for f in fails:
            print("FAIL " + f)
        print("lint: " + ("FAIL" if fails else "PASS"))
        return 1 if fails else 0


    # ---------------------------------------------------------------- gate

    def quotations(text):
        """Quoted spans of four words or more, outside code."""
        spans = re.findall(r'"([^"\n]{3,}?)"|“([^”\n]{3,}?)”', strip_code(text))
        out = []
        for a_, b_ in spans:
            q = a_ or b_
            if len(q.split()) >= 4:
                out.append(q)
        return out


    def strip_code(text):
        text = re.sub(r"(?ms)^(```|~~~).*?^\1\s*$", "", text)
        return "\n".join(l for l in text.split("\n") if not l.startswith(("    ", "\t")))


    def cmd_gate(a):
        results = []
        draft = read(a.draft)
        results.append(("draft is readable and not empty", bool(draft.strip()), ""))
        has_sources = re.search(r"(?mi)^#{1,6}\s+sources\b", draft) is not None
        results.append(("draft has a Sources heading", has_sources, ""))
        links = re.findall(r"https?://[^\s)>\]]+", draft)
        results.append(("draft cites at least one link", len(links) > 0, f"{len(links)} links"))
        if a.brief:
            brief = read(a.brief)
            results.append(("brief is readable and not empty", bool(brief.strip()), ""))
        if a.terms:
            terms = [t.strip() for t in read(a.terms).split("\n")
                     if t.strip() and not t.strip().startswith("#")]
            hits = []
            low = draft.lower().split("\n")
            for i, term in enumerate(terms, 1):
                pat = re.compile(r"(?<!\w)" + re.escape(term.lower()) + r"(?!\w)")
                for ln, line in enumerate(low, 1):
                    if pat.search(line):
                        hits.append(f"term #{i} at line {ln}")
            # the terms themselves are never printed, so they do not enter the chat
            results.append(("no private term in the draft", not hits, "; ".join(hits)))
        if a.sources:
            if not os.path.isdir(a.sources):
                die(f"no such folder: {a.sources}")
            corpus = []
            for root, _, files in os.walk(a.sources):
                for fn in files:
                    if fn.endswith((".txt", ".md", ".html", ".htm")):
                        with open(os.path.join(root, fn), encoding="utf-8", errors="ignore") as f:
                            corpus.append(norm(re.sub(r"<[^>]+>", " ", f.read())))
            corpus = "\n".join(corpus)
            missing = []
            for q in quotations(draft):
                parts = [p for p in re.split(r"\s*(?:…|\.\.\.)\s*", q) if p.strip()]
                if not all(norm(p) in corpus for p in parts):
                    missing.append(q[:60])
            results.append(("every quotation is verbatim in the saved sources", not missing,
                            f"{len(missing)} not found: " + " | ".join(missing) if missing else ""))
        failed = 0
        for label, ok, detail in results:
            print(("PASS " if ok else "FAIL ") + label + (f" ({detail})" if detail else ""))
            failed += not ok
        print("gate: " + ("FAIL" if failed else "PASS"))
        return 1 if failed else 0


    # ---------------------------------------------------------------- claims

    def split_sentences(par):
        par = re.sub(r"\s+", " ", par).strip()
        return [s for s in re.split(r"(?<=[.!?])\s+(?=[A-Z“\"*\[(])", par) if s]


    def cmd_claims(a):
        lines = read(a.draft).split("\n")
        rows, stratum, in_fence, skip, buf = [], "Opening", False, False, []
        if lines and lines[0].strip() == "---":
            try:
                lines = lines[lines.index("---", 1) + 1:]
            except ValueError:
                pass

        def flush():
            if buf and not skip:
                for s in split_sentences(" ".join(buf)):
                    kinds = []
                    if re.search(r"\d", s):
                        kinds.append("number")
                    if re.search(r'["“”]', s):
                        kinds.append("quote")
                    if re.search(r"https?://|\]\(", s):
                        kinds.append("link")
                    if kinds:
                        rows.append((stratum, "+".join(kinds), s))
            buf.clear()

        for line in lines:
            if line.strip().startswith(("```", "~~~")):
                flush()
                in_fence = not in_fence
                continue
            if in_fence or line.startswith(("    ", "\t")):
                continue
            m = re.match(r"^(#{1,6})\s+(.*)$", line)
            if m:
                flush()
                if len(m.group(1)) <= 2:
                    title = m.group(2).strip()
                    skip = bool(re.match(r"(?i)^(sources|unsure list)\b", title))
                    stratum = title
                continue
            if line.startswith("|"):
                flush()
                if not re.fullmatch(r"[|\s:-]+", line) and not skip:
                    cells = [c.strip() for c in line.strip("|").split("|")]
                    buf.append(" | ".join(cells))
                    flush()
                continue
            if not line.strip():
                flush()
                continue
            buf.append(re.sub(r"^(>\s*|[-*]\s+|\d+\.\s+)", "", line.strip()))
        flush()
        with open(a.out, "w", encoding="utf-8") as f:
            f.write("id\tsection\tkind\tclaim\tstatus\n")
            for i, (st, kind, s) in enumerate(rows, 1):
                f.write(f"C{i:03d}\t{st}\t{kind}\t{s.replace(chr(9), ' ')}\t\n")
        strata = {}
        for st, _, _ in rows:
            strata[st] = strata.get(st, 0) + 1
        print(f"{len(rows)} candidate claims in {len(strata)} sections written to {a.out}")
        for st, c in strata.items():
            print(f"  {c:4d}  {st}")
        print("Next: read the list; mark a row that is not a checkable claim with "
              "'drop: <reason>' in its status column; add a claim the script missed "
              "(a mechanism, a recommendation, an attribution with no number, quotation "
              "or link) as a new row with an id A01, A02, ...")
        return 0


    # ---------------------------------------------------------------- sample

    def read_tsv(path):
        rows = []
        lines = read(path).rstrip("\n").split("\n")
        head = lines[0].split("\t")
        for line in lines[1:]:
            if not line.strip():
                continue
            cells = line.split("\t") + [""] * len(head)
            rows.append(dict(zip(head, cells)))
        return head, rows


    def write_tsv(path, head, rows):
        with open(path, "w", encoding="utf-8") as f:
            f.write("\t".join(head) + "\n")
            for r in rows:
                f.write("\t".join(r.get(h, "") for h in head) + "\n")


    def cmd_sample(a):
        if a.tier not in TIER_RATE:
            die("tier must be 1, 2 or 3")
        _, rows = read_tsv(a.claims)
        live = [r for r in rows if not r.get("status", "").lower().startswith("drop")]
        dropped = len(rows) - len(live)
        big_n, n = len(live), sample_size(a.tier)
        if big_n == 0:
            die("no claims to check")
        seed = a.seed if a.seed is not None else int(datetime.datetime.now().strftime("%Y%m%d%H%M%S"))
        rng = random.Random(seed)
        if a.census or big_n <= n:
            mode, chosen = "census", list(live)
        else:
            mode = "sample"
            strata = {}
            for r in live:
                strata.setdefault(r["section"], []).append(r)
            chosen = []
            for st in strata:                       # one from every section
                pick = rng.choice(strata[st])
                chosen.append(pick)
                strata[st].remove(pick)
            rest = [r for v in strata.values() for r in v]
            extra = max(0, n - len(chosen))         # then at random from all that remain,
            chosen += rng.sample(rest, min(extra, len(rest)))   # so larger sections give more
        head = ["id", "section", "claim", "mode"]
        write_tsv(a.out, head, [{"id": r["id"], "section": r["section"],
                                 "claim": r["claim"], "mode": mode} for r in chosen])
        k = len(chosen)
        print(f"N = {big_n} checkable claims ({dropped} dropped as not checkable)")
        print(f"tier {a.tier}: n = {n}; mode: {mode}; drawn: {k}; seed: {seed}")
        if mode == "sample":
            print(f"if all {k} pass: consistent with up to {upper_bound(k):.1%} failing (95%)")
            if k > n:
                print(f"note: {k - n} more than n, because every section gives one claim")
        print(f"sample written to {a.out}: record it before opening any source")
        return 0


    def cmd_redraw(a):
        _, rows = read_tsv(a.claims)
        head, sample = read_tsv(a.sample)
        target = [r for r in sample if r["id"] == a.id]
        if not target:
            die(f"{a.id} is not in the sample")
        taken = {r["id"] for r in sample}
        pool = [r for r in rows if r["section"] == target[0]["section"] and r["id"] not in taken
                and not r.get("status", "").lower().startswith("drop")]
        if not pool:
            print(f"no undrawn claim left in section {target[0]['section']!r}; "
                  f"{a.id} stays UNVERIFIABLE and is marked unsourced")
            return 1
        seed = a.seed if a.seed is not None else int(datetime.datetime.now().strftime("%Y%m%d%H%M%S"))
        pick = random.Random(seed).choice(pool)
        sample.append({"id": pick["id"], "section": pick["section"], "claim": pick["claim"],
                       "mode": sample[0].get("mode", "sample")})
        write_tsv(a.sample, head, sample)
        print(f"{pick['id']} added from section {pick['section']!r} (seed {seed}); "
              f"{a.id} stays in the sample as UNVERIFIABLE and is marked unsourced in the draft")
        return 0


    # ---------------------------------------------------------------- report

    def sections(text):
        marks = {}
        for i in range(1, 5):
            m = re.search(rf"(?m)^##\s*{i}\s*·", text)
            marks[i] = m.start() if m else None
        return marks


    def cmd_report(a):
        rep = read(a.report)
        draft_norm = norm(read(a.draft))
        _, sample = read_tsv(a.sample)
        sample_ids = [r["id"] for r in sample]
        fails = []
        marks = sections(rep)
        names = {1: "Claims", 2: "Findings", 3: "Confirmed", 4: "Invented items"}
        for i in range(1, 5):
            if marks[i] is None:
                fails.append(f"no '## {i} · {names[i]}' section")
        if any(marks[i] is None for i in marks):
            for f in fails:
                print("FAIL " + f)
            print("report: FAIL")
            return 1
        if not all(marks[i] < marks[i + 1] for i in range(1, 4)):
            fails.append("sections are not in the order 1, 2, 3, 4")
        part = {i: rep[marks[i]:(marks[i + 1] if i < 4 else len(rep))] for i in range(1, 5)}

        m = re.search(r"(?m)^N\s*=\s*(\d+)", part[1])
        if not m:
            fails.append("section 1 gives no 'N = <count>' line")
        verdict_of = {}
        for line in part[1].split("\n"):
            cells = [c.strip() for c in line.strip().strip("|").split("|")] if line.startswith("|") else []
            if cells and re.fullmatch(r"[CA]\d{2,}", cells[0]):
                verdict_of[cells[0]] = cells[-1].upper()
        missing = [i for i in sample_ids if i not in verdict_of]
        extra = [i for i in verdict_of if i not in sample_ids]
        if missing:
            fails.append("sampled claims with no row: " + ", ".join(missing))
        if extra:
            fails.append("rows for claims that were not drawn: " + ", ".join(extra))
        bad = [f"{i}={v}" for i, v in verdict_of.items() if v not in VERDICTS]
        if bad:
            fails.append("verdicts not PASS, FAIL, STALE or UNVERIFIABLE: " + ", ".join(bad))

        counts = {s: 0 for s in SEVERITIES}
        for line in part[2].split("\n"):
            if not line.startswith("- ["):
                continue
            sev = re.match(r"- \[([a-z-]+)\]", line).group(1)
            if sev not in SEVERITIES:
                fails.append(f"finding with unknown grade [{sev}]")
                continue
            counts[sev] += 1
            cur = re.search(r'Current: "(.*?)" · Problem:', line)
            if not cur:
                fails.append(f"finding without 'Current: \"...\" · Problem:': {line[:70]}")
            else:
                hits = draft_norm.count(norm(cur.group(1)))
                if hits != 1:
                    fails.append(f"Current text occurs {hits} times in the draft, not once: "
                                 f"{cur.group(1)[:60]}")
            if not re.search(r'· Fix: ".*?"', line):
                fails.append(f"finding without 'Fix: \"...\"': {line[:70]}")
            if not re.search(r"· Basis: .*https?://", line):
                fails.append(f"finding without a Basis link: {line[:70]}")

        for line in part[3].split("\n"):
            for q in re.findall(r'"([^"]+)"', line):
                if len(q.split()) >= CONFIRM_WORD_LIMIT:
                    fails.append(f"Confirmed quotation of {len(q.split())} words, "
                                 f"not under {CONFIRM_WORD_LIMIT}: {q[:50]}")

        inv_body = re.sub(r"(?m)^##.*$", "", part[4]).strip()
        inv_lines = [l for l in inv_body.split("\n") if l.strip() and not l.startswith("Verdict:")]
        invented = not (len(inv_lines) == 1 and inv_lines[0].strip().lower().rstrip(".") == "none")
        if not inv_lines:
            fails.append("section 4 is empty: write 'none' or list the invented items")
            invented = False

        last = [l for l in rep.strip().split("\n") if l.strip()][-1].strip()
        vm = re.fullmatch(r"Verdict: (keep|fix|rewrite) · errors (\d+) · should-fix (\d+) · "
                          r"minor (\d+) · checker: (.+)", last)
        if not vm:
            fails.append("last line is not 'Verdict: keep|fix|rewrite · errors n · "
                         "should-fix n · minor n · checker: <model and version>'")
        else:
            stated = dict(zip(SEVERITIES, map(int, vm.group(2, 3, 4))))
            if stated != counts:
                fails.append(f"last line counts {stated} differ from the findings {counts}")
            if vm.group(1) == "keep" and ("FAIL" in verdict_of.values() or counts["error"]):
                fails.append("verdict keep with a FAIL or an error")

        tally = {v: list(verdict_of.values()).count(v) for v in VERDICTS}
        census = bool(sample) and sample[0].get("mode") == "census"
        print("verdicts: " + ", ".join(f"{v} {tally[v]}" for v in VERDICTS))
        print("findings: " + ", ".join(f"{s} {counts[s]}" for s in SEVERITIES))
        unv = [i for i, v in verdict_of.items() if v == "UNVERIFIABLE"]
        if unv:
            print("UNVERIFIABLE (redraw each, and mark it unsourced): " + ", ".join(unv))
        # Rule C5 of BW6's protocol, acceptance number zero
        if invented:
            decision = "FULL CHECK: an invented item was found"
        elif census:
            decision = "CENSUS DONE: verify every FAIL and STALE at its source before applying"
        elif tally["FAIL"]:
            decision = "FULL CHECK: a sampled claim failed (acceptance number zero)"
        elif tally["STALE"]:
            decision = "SWEEP: re-read and date every fact in the draft that can change"
        else:
            k = tally["PASS"]
            decision = (f"USE IT: a clean sample of {k} is consistent with up to "
                        f"{upper_bound(k):.1%} failing (95%)")
        print("decision: " + decision)
        for f in fails:
            print("FAIL " + f)
        print("report: " + ("FAIL" if fails else "PASS"))
        return 1 if fails else 0


    def cmd_recheck(a):
        rep = read(a.report)
        passes = []
        for line in rep.split("\n"):
            cells = [c.strip() for c in line.strip().strip("|").split("|")] if line.startswith("|") else []
            if cells and re.fullmatch(r"[CA]\d{2,}", cells[0]) and cells[-1].upper() == "PASS":
                passes.append(cells[0])
        seed = a.seed if a.seed is not None else int(datetime.datetime.now().strftime("%Y%m%d%H%M%S"))
        pick = sorted(random.Random(seed).sample(passes, min(5, len(passes))))
        print(f"re-open the sources of these PASS verdicts yourself (seed {seed}): " + ", ".join(pick))
        if len(pick) == 5:
            print("five clean re-checks bound the checker's false-PASS rate below "
                  f"{upper_bound(5):.1%} (95%); one wrong PASS sends the check to be run again")
        return 0


    # ---------------------------------------------------------------- log

    def cmd_log(a):
        stamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        inputs = ", ".join(f"{os.path.basename(p)}@{short_hash(p)}" if os.path.isfile(p)
                           else f"{p}@missing" for p in a.inputs)
        line = (f"{stamp} · {a.stage} · run {a.run} · {inputs} · {a.model} · "
                f"{a.output} · {a.gate} · {a.by}")
        print(line)
        if a.append:
            new = not os.path.isfile(a.append)
            with open(a.append, "a", encoding="utf-8") as f:
                if new:
                    f.write("# Run log\n\nDate and time · Stage · run · Inputs@version · "
                            "Model, version and effort · Output · Gate and result · Who ran the gate\n\n")
                f.write(line + "\n")
        return 0


    def main(argv):
        p = argparse.ArgumentParser(prog="check.py", description=__doc__,
                                    formatter_class=argparse.RawDescriptionHelpFormatter)
        sub = p.add_subparsers(dest="cmd")
        s = sub.add_parser("lint"); s.add_argument("skill_dir")
        s = sub.add_parser("gate"); s.add_argument("draft"); s.add_argument("--brief")
        s.add_argument("--terms"); s.add_argument("--sources")
        s = sub.add_parser("claims"); s.add_argument("draft"); s.add_argument("--out", required=True)
        s = sub.add_parser("sample"); s.add_argument("claims"); s.add_argument("--tier", type=int, required=True)
        s.add_argument("--seed", type=int); s.add_argument("--census", action="store_true")
        s.add_argument("--out", required=True)
        s = sub.add_parser("redraw"); s.add_argument("claims"); s.add_argument("sample"); s.add_argument("id")
        s.add_argument("--seed", type=int)
        s = sub.add_parser("report"); s.add_argument("report"); s.add_argument("--draft", required=True)
        s.add_argument("--sample", required=True)
        s = sub.add_parser("recheck"); s.add_argument("report"); s.add_argument("--seed", type=int)
        s = sub.add_parser("log")
        for k in ("stage", "run", "model", "output", "gate", "by"):
            s.add_argument("--" + k, required=True)
        s.add_argument("--inputs", nargs="+", required=True); s.add_argument("--append")
        a = p.parse_args(argv)
        if not a.cmd:
            p.print_help()
            return 2
        return {"lint": cmd_lint, "gate": cmd_gate, "claims": cmd_claims, "sample": cmd_sample,
                "redraw": cmd_redraw, "report": cmd_report, "recheck": cmd_recheck,
                "log": cmd_log}[a.cmd](a)


    if __name__ == "__main__":
        sys.exit(main(sys.argv[1:]))

#### D · Install

**claude.ai** (read 16 Nov 2026: *Use skills in Claude*; *How to create custom skills*):

1. Settings > Capabilities: turn on code execution. On Team and Enterprise an owner enables it for the organisation first.
2. From the folder that holds `check-against-sources/`, run `python3 check-against-sources/scripts/check.py lint check-against-sources`. It must end `lint: PASS`. On the case it prints a 21-character name, a 193-character description (inside claude.ai's 200) and 119 body lines.
3. `zip -r check-against-sources.zip check-against-sources`, so that the folder is the ZIP's root.
4. Customize > Skills: upload the ZIP and switch the skill on.
5. Do not upload the private-terms list. On claude.ai the terms gate is skipped and the report says so; the case's own terms check runs by script on the course data (Academy case file §7).

**Claude Code** (read 16 Nov 2026: *Extend Claude with skills*):

1. Commit the folder at `.claude/skills/check-against-sources/` in the repository. It then loads in sessions in that repository and in scheduled runs that clone it, but not in cloud threads inside a project.
2. In a session, ask "What skills are available?"; the skill must be listed.
3. A skill switched on in claude.ai also loads in cloud and Cowork sessions, and in terminal sessions signed in with the account from version 2.1.273, by this page; the developer documentation says it does not (§2, disagreement). The committed copy is the route both document.

**Before the first real check: seed three errors** (BW6, Deliverable step F). Copy a filed unit, change three checkable claims so they no longer match their sources, note which, and run the skill on the copy in census mode. All three must appear as findings. Record the result in the run log.

#### E · Trigger test set

Sixteen requests: eight that should load the skill and eight near-misses that share its words and need something else (§4). On the case each is sent in a new chat in the course's project, with a unit attached where the request needs one. Requests marked **V** are the validation set (six of sixteen, about the 40% §4 gives): they are run, never used to rewrite the description.

| # | Request | Should load | Set |
|---|---|---|---|
| S1 | "Check this text against its sources." (a unit attached) | yes | train |
| S2 | "Fact-check BW6 before I file it: every claim against the page it cites." | yes | train |
| S3 | "Can you verify the numbers in this report against the studies it links to?" | yes | train |
| S4 | "Run the fresh check on the attached unit, tier 3, census." | yes | train |
| S5 | "I don't trust the citations in this research summary. Go through them and tell me which ones don't hold." | yes | train |
| S6 | "Sample 14 claims from this memo and check them against their sources; it goes to the board on Friday." | yes | V |
| S7 | "is every quote in here actually on the page it cites? file attached" | yes | V |
| S8 | "Before we publish: audit the claims in section 3 against their references." | yes | V |
| N1 | "Run the monthly rot check on the project." | no | train |
| N2 | "Proofread this draft for spelling and grammar." | no | train |
| N3 | "Find three sources that support this claim about sample sizes." | no | train |
| N4 | "Summarise these five sources in a page for my director." | no | train |
| N5 | "Critique the structure of this draft: does the argument hold?" | no | train |
| N6 | "Write the Sources list for this draft from the links in it." | no | V |
| N7 | "Check that the totals in this spreadsheet add up." | no | V |
| N8 | "Apply the findings in this check report to the draft." | no | V |

S1 is the request the skill exists for, a text checked against its sources. N1 is the scheduled task's job, N5 is BW3's template 3, N7 is a script's job (BW2, row 2), and N8 is stage 4 of BW7's pipeline, which this skill must never do.

**How to run it.** Each request three times, each in a new chat. Loaded means the reply's first line begins `check-against-sources ·` (the skill's step 0), confirmed on claude.ai in Claude's thinking and in Claude Code by a Skill tool call naming it (§4). Record a line per request: `#, runs loaded of 3, pass or fail`. A should-load request passes at 2 or 3 of 3; a near-miss passes at 0 or 1 of 3 (the 0.5 threshold of §4). If a train request fails, rewrite the description, keep it at 200 characters or fewer, run `lint` again, and rerun all sixteen; stop after five rewrites and look at the requests instead (§4).

#### F · The scheduled task: the monthly rot check

The job is BW4's rot check (Deliverable Part 2), with BW5's build-order check added (§6). The script runs the mechanical steps and lists the rest for you; the cloud run only runs it and commits its report.

**`build/rotcheck.py`** (BW4's `build/` folder holds the build scripts), tested on a mock repository laid out as BW4's Part 1, with a missing file, a superseded file outside `archive/`, a mirror that differs from its source, a private term in the built output, and a build order with two rows swapped; each was reported, and the term by number only.

    #!/usr/bin/env python3
    """rotcheck.py: the mechanical steps of the monthly rot check (BW4, Deliverable Part 2).

    Python 3 standard library only. It reads the repository and writes one report;
    it changes nothing else and fixes nothing it finds.

      python3 build/rotcheck.py --root . [--date YYYY-MM-DD] [--terms FILE --built DIR]

    Steps it runs:
      1a  INSTRUCTIONS.md is at most 400 words           (the word count only; the reading is yours)
      2   every file is in INDEX.md, every INDEX.md entry exists, nothing superseded sits outside archive/
      3   every mirror inside the repository matches its source byte for byte
      6   no private term in the built output             (only with --terms and --built: a local run)
      B   BUILD-ORDER.md: every "Takes from" entry sits higher than its own row (BW5, Deliverable 2b)
    Steps it lists for you: 1b (read the instructions), 3 (mirrors outside the repository),
    4 (duplicated rules), 5 (contradictions), and 6 when it was not run here.

    Writes records/rot/<date>.md and prints the run-log line. Exit 1 if a step fails.
    """
    import argparse
    import datetime
    import hashlib
    import os
    import re
    import sys

    IGNORE_DIRS = {".git", "__pycache__", "node_modules", ".venv"}
    IGNORE_FILES = {".DS_Store"}
    WORD_LIMIT = 400          # BW4, Deliverable Part 1 (stated opinion there)


    def read(path):
        with open(path, encoding="utf-8") as f:
            return f.read()


    def tables(text):
        """Every Markdown table in text, as (header cells, list of row cells)."""
        out, cur = [], []
        for line in text.split("\n") + [""]:
            if line.strip().startswith("|"):
                cur.append([c.strip() for c in line.strip().strip("|").split("|")])
            elif cur:
                if len(cur) >= 2 and re.fullmatch(r"[\s:|-]+", "|".join(cur[1])):
                    out.append((cur[0], cur[2:]))
                cur = []
        return out


    def column(header, word):
        for i, h in enumerate(header):
            if word.lower() in h.lower():
                return i
        return None


    def repo_files(root):
        found = []
        for d, dirs, files in os.walk(root):
            dirs[:] = [x for x in dirs if x not in IGNORE_DIRS]
            for f in files:
                if f not in IGNORE_FILES:
                    found.append(os.path.relpath(os.path.join(d, f), root).replace(os.sep, "/"))
        return sorted(found)


    def entry_path(cell):
        m = re.search(r"`([^`]+)`", cell)
        p = (m.group(1) if m else cell).strip()
        p = re.sub(r"(…|\.\.\.|\*).*$", "", p)      # archive/… covers the folder
        return p


    def covered(path, entries):
        for e in entries:
            if e and (path == e or (e.endswith("/") and path.startswith(e))):
                return True
        return False


    def step_1a(root):
        p = os.path.join(root, "INSTRUCTIONS.md")
        if not os.path.isfile(p):
            return "FAIL", "INSTRUCTIONS.md not found"
        words = len(read(p).split())
        return ("PASS" if words <= WORD_LIMIT else "FAIL"), f"{words} words (limit {WORD_LIMIT})"


    def step_2_3(root):
        p = os.path.join(root, "INDEX.md")
        if not os.path.isfile(p):
            return ("FAIL", "INDEX.md not found"), ("FAIL", "INDEX.md not found"), []
        found = [t for t in tables(read(p)) if column(t[0], "path") is not None]
        if not found:
            return ("FAIL", "INDEX.md has no table with a Path column"), ("FAIL", "no index table"), []
        header, rows = found[0]
        ip, ist, imi = column(header, "path"), column(header, "status"), column(header, "mirror")
        entries, problems = [], []
        for r in rows:
            if ip >= len(r):
                continue
            e = entry_path(r[ip])
            entries.append(e)
            status = r[ist].lower() if ist is not None and ist < len(r) else ""
            if e and not e.endswith("/") and not os.path.exists(os.path.join(root, e)):
                problems.append(f"listed but missing: {e}")
            if "superseded" in status and not e.startswith("archive/"):
                problems.append(f"superseded outside archive/: {e}")
        for f in repo_files(root):
            if not covered(f, entries):
                problems.append(f"not in INDEX.md: {f}")
        s2 = ("FAIL" if problems else "PASS",
              "; ".join(problems) if problems else f"{len(entries)} entries, every file listed")
        mirror_fail, by_hand = [], []
        if imi is not None:
            for r in rows:
                if imi >= len(r) or ip >= len(r):
                    continue
                src, cell = entry_path(r[ip]), r[imi]
                if not cell or cell.lower() in ("none", "n/a", "-"):
                    continue
                inside = [m for m in re.findall(r"`([^`]+)`", cell)
                          if os.path.isfile(os.path.join(root, m))]
                if inside:
                    for m in inside:
                        a_, b_ = os.path.join(root, src), os.path.join(root, m)
                        if not os.path.isfile(a_):
                            mirror_fail.append(f"{src}: source missing")
                            continue
                        if hashlib.sha256(open(a_, "rb").read()).digest() != \
                           hashlib.sha256(open(b_, "rb").read()).digest():
                            mirror_fail.append(f"{m} differs from {src}")
                else:
                    by_hand.append(f"{src} → {cell}")
        s3 = ("FAIL" if mirror_fail else "PASS",
              "; ".join(mirror_fail) if mirror_fail else "mirrors inside the repository match")
        return s2, s3, by_hand


    def step_6(terms_file, built):
        terms = [t.strip() for t in read(terms_file).split("\n")
                 if t.strip() and not t.strip().startswith("#")]
        hits = []
        for f in repo_files(built):
            try:
                text = read(os.path.join(built, f)).lower()
            except (UnicodeDecodeError, OSError):
                continue
            for i, t in enumerate(terms, 1):
                if re.search(r"(?<!\w)" + re.escape(t.lower()) + r"(?!\w)", text):
                    hits.append(f"term #{i} in {f}")      # never the term itself
        return ("FAIL" if hits else "PASS"), ("; ".join(hits) if hits else f"{len(terms)} terms, none found")


    def step_b(root):
        p = os.path.join(root, "BUILD-ORDER.md")
        if not os.path.isfile(p):
            return "SKIP", "no BUILD-ORDER.md"
        for header, rows in tables(read(p)):
            iu, it = column(header, "unit"), column(header, "takes")
            if iu is None or it is None:
                continue
            codes = [re.split(r"\s+·\s+|\s", r[iu].strip(), maxsplit=1)[0] for r in rows]
            problems = []
            for k, r in enumerate(rows):
                for want in re.findall(r"[A-Z]+-?[A-Z]*\d+", r[it] if it < len(r) else ""):
                    if want not in codes:
                        problems.append(f"{codes[k]} takes {want}, which is not in the table")
                    elif codes.index(want) >= k:
                        problems.append(f"{codes[k]} takes {want}, which sits at or below it")
            return ("FAIL" if problems else "PASS"), \
                   ("; ".join(problems) if problems else f"{len(rows)} units in order")
        return "FAIL", "BUILD-ORDER.md has no table with Unit and Takes columns"


    def main(argv):
        ap = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
        ap.add_argument("--root", default=".")
        ap.add_argument("--date", default=datetime.date.today().isoformat())
        ap.add_argument("--terms")
        ap.add_argument("--built")
        a = ap.parse_args(argv)
        root = os.path.abspath(a.root)
        results = [("1a · Instructions word count",) + step_1a(root)]
        s2, s3, by_hand = step_2_3(root)
        results.append(("2 · Index against folders",) + s2)
        results.append(("3 · Mirrors inside the repository",) + s3)
        if a.terms and a.built:
            results.append(("6 · Private terms in the built output",) + step_6(a.terms, a.built))
        results.append(("B · Build order",) + step_b(root))
        yours = ["1b · Read INSTRUCTIONS.md whole: no procedure; every sentence a rule or a pointer",
                 "4 · Duplicated rules: search for the three rules broken most often this month",
                 "5 · Contradictions: account-wide instructions beside the exceptions paragraph"]
        yours += [f"3 · Mirror outside the repository: {x}" for x in by_hand]
        if not (a.terms and a.built):
            yours.append("6 · Private terms: run locally with --terms and --built "
                         "(the list is kept outside the repository)")
        failed = [r for r in results if r[1] == "FAIL"]
        out_rel = f"records/rot/{a.date}.md"
        lines = [f"# Rot check · {a.date}", "", "| Step | Result | Detail |", "|---|---|---|"]
        lines += [f"| {s} | {res} | {d} |" for s, res, d in results]
        lines += ["", "## By hand (yours)", ""] + [f"- [ ] {y}" for y in yours]
        stamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        inputs = ", ".join(
            f"{n}@{hashlib.sha256(open(os.path.join(root, n), 'rb').read()).hexdigest()[:7]}"
            for n in ("INDEX.md", "INSTRUCTIONS.md", "BUILD-ORDER.md")
            if os.path.isfile(os.path.join(root, n)))
        verdict = ("FAIL at steps " + ", ".join(r[0].split(" ·")[0] for r in failed)) if failed else "PASS"
        log = (f"{stamp} · rot check · run 1 · {inputs} · none: script rotcheck.py · "
               f"{out_rel} · code: {verdict}; {len(yours)} by hand · script")
        lines += ["", "Run-log line:", "", log, ""]
        os.makedirs(os.path.join(root, "records", "rot"), exist_ok=True)
        with open(os.path.join(root, out_rel), "w", encoding="utf-8") as f:
            f.write("\n".join(lines))
        for s, res, d in results:
            print(f"{res:4}  {s}: {d}")
        print(f"by hand: {len(yours)} items, listed in {out_rel}")
        print(log)
        return 1 if failed else 0


    if __name__ == "__main__":
        sys.exit(main(sys.argv[1:]))

**Settings** (on *Automate work with scheduled tasks*, read 16 Nov 2026):

- **Name:** monthly rot check.
- **Repository:** the course repository only.
- **Connectors:** remove all of them. They are included by default and can write.
- **Environment:** Default, Trusted network. The run needs no outside host.
- **Schedule:** Custom, `7 7 1 * *`: 07:07 UTC on the first of each month (a five-field expression is read in UTC; begin it with `CRON_TZ=<your time zone>` to write local hours), a few minutes past the hour because a run set on the hour can start several minutes late. Create the task with a preset, then choose Custom in its edit dialog. Monthly is BW4's cadence.
- **Model:** the smallest the dialog offers. BW2 has no row for running a script and committing its output; row 1 (triage and reformatting, small, Haiku 5.5, low) is borrowed by analogy, because the run makes no judgement.
- **Branch protection:** on the default branch, with no bypass for your own account, since a rule your connected access can bypass does not block a run's push.

**The prompt**, self-contained, saying what success looks like:

> Run the monthly rot check of this repository. Step 1: run `python3 build/rotcheck.py --root .` from the repository root. It writes `records/rot/<today's date>.md` and prints a run-log line as its last line. Step 2: append that line, unchanged, to the end of `records/run-log.md`. Step 3: commit exactly those two files to a new branch named `claude/rot-<today's date>` and push it. Change no other file, fix nothing the report finds, use no connector, and send nothing. If the script cannot run (it prints a Python traceback and writes no report), push nothing and give its error as your last message; an exit status of 1 with the report written means a step failed, and the branch is still pushed. Success is one pushed branch with those two files changed, and your last message giving the script's PASS and FAIL lines.

**What the run leaves for you.** A branch with the report. You read its **By hand** list, which always holds steps 1b, 4 and 5, the mirror comparisons outside the repository (the claude.ai instructions field against `INSTRUCTIONS.md`), and step 6, the private-terms search, which you run locally with `--terms ../private-terms.txt --built <the built site folder>` because the list is outside the repository. Each FAIL becomes a backlog row (BW4, Deliverable Part 2), and you merge or delete the branch.

On the case `[NOT IN CASE FILE: whether the repository holds INDEX.md, INSTRUCTIONS.md and BUILD-ORDER.md in BW4's and BW5's form; the case file records the method, a backlog and a changelog, §1, §2]`. Until it does, the script reports those files as missing, which is itself the first finding. INDEX.md also needs rows for `.claude/skills/` and `records/`, or step 2 reports the committed skill and every earlier rot report as unlisted.

#### G · Done when

- [ ] `check.py lint` prints `lint: PASS`, with a description of 200 characters or fewer.
- [ ] The skill is switched on in Customize > Skills on claude.ai, and listed by "What skills are available?" in a Claude Code session on the repository.
- [ ] The trigger test is run three times per request: at least 15 of the 16 requests pass, S1 loads 3 of 3, and no near-miss loads 3 of 3; all six V requests pass (this unit's thresholds, stated opinion, on §4's method).
- [ ] The seeded-error run reports all three seeded errors.
- [ ] The first real check ends with `report: PASS` and a decision line, two log lines in `records/run-log.md`, and the five claim ids to re-check, which the maintainer re-opens before applying any finding.
- [ ] The scheduled task's first run pushes `claude/rot-<date>` with the report and one log line, and nothing else.
- [ ] Nothing in the skill folder is a key, a password or a private term, and its only product facts are the three limits in `check.py` that `lint` needs to run without a network, each dated in its comment; re-read them at each rot check (§8).

### Part 2 · Template: your skill

Copy Part 1's folder and both scripts unchanged. Fill the blanks below; keep everything else as it is unless your log gives you a reason to change it.

**The front matter.** Keep the name if it suits you (it must match the folder). Keep the description, or rewrite it in this form, in 200 characters or fewer:

    description: "[what it does, third person: Checks … against …, and reports … without editing it]. Use when asked to [the verbs your requests use: check, fact-check, verify] [the object: a text, a memo, a report] against its sources."

**The Settings section of `SKILL.md`:**

    - **Tier:** [1, 2 or 3, from BW6 §5: 1 for you alone; 2 shared or a decision rests on it; 3 published, sent to a client, or with legal, financial or health consequences].
    - **Mode:** [census, if you check every cited claim; or sample, if the tier's n is what you can afford].
    - **Also look for:** [the failure kinds your own checks have found, from your BW6 log; or "none yet"].
    - **Private-terms list:** [its path outside your project folder; or "none"].
    - **Expected model:** [the path of your BW2 routing table; the skill reads rows 5 and 9 there, so no model name is written here; a model other than the writer's].
    - **Report goes to:** [the folder and file name for check reports, e.g. checks/<name>-check.md].
    - **Run log:** [your run log, e.g. records/run-log.md].

**Install.** Part 1's steps, with your repository's path, or the claude.ai steps alone if you have no repository.

**Trigger test set.** Sixteen rows, in Part 1's table form:

| # | Request | Should load | Set |
|---|---|---|---|
| S1 | [*the plainest form of your request to check a text against its sources*] | yes | train |
| S2–S5 | [*four more, varied: one formal, one casual, one long with context, one that describes the need without the words "check" or "sources"*] | yes | train |
| S6–S8 | [*three more of the same kinds, kept aside*] | yes | V |
| N1–N5 | [*five near-misses from your own work that share the words "check", "sources", "draft" or "claims" and need something else: a proofread, a search for sources, a summary, a critique of structure, another of your skills*] | no | train |
| N6–N8 | [*three more near-misses, kept aside; include "apply these findings", which the skill must never do*] | no | V |

**Scheduled task.** Keep the rot-check script and prompt. Fill:

- Repository: [*your canonical repository, or "none: run the script by hand on the first of the month" if your project is not in one*]
- Schedule: [*a day of the month and a time a few minutes past the hour, written as cron in UTC (or after `CRON_TZ=<your time zone>`): minute, hour, day of the month, then `* *`*]
- Files the script expects: [*INDEX.md, INSTRUCTIONS.md and BUILD-ORDER.md from BW4 Part 3 and BW5 2b, or the names you gave them; edit the names where the script reads them, in `step_1a`, `step_2_3`, `step_b` and `main`, if they differ*]
- What stays by hand: [*steps 1b, 4, 5; mirrors outside the repository; the terms search, if your list is outside it*]

**Done when.** Part 1's seven lines, with your thresholds if you change them: [*the pass rule for the trigger test, and why*].

## Sources

All web pages read 16 November 2026. Most vendor documentation and help-centre pages show no exact date of their own; where a page gives one, it is listed.

**The format and Anthropic's documentation (vendor)**

- Agent Skills. *Specification*. agentskills.io (the format's documentation). https://agentskills.io/specification.md
- Agent Skills. *Optimizing skill descriptions*. agentskills.io (the format's documentation). https://agentskills.io/skill-creation/optimizing-descriptions.md
- Anthropic. *Agent Skills*. Claude Platform Docs. https://platform.claude.com/docs/agents-and-tools/agent-skills/overview
- Anthropic. *Skill authoring best practices*. Claude Platform Docs. https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices.md
- Anthropic. *Extend Claude with skills*. Claude Code documentation. https://code.claude.com/docs/en/skills.md
- Anthropic. *Automate work with scheduled tasks*. Claude Code documentation (research preview); read at https://code.claude.com/docs/en/web-scheduled-tasks?mode=reply. https://code.claude.com/docs/en/web-scheduled-tasks
- Anthropic. *Run prompts on a schedule*. Claude Code documentation. https://code.claude.com/docs/en/scheduled-tasks
- Anthropic. *Schedule recurring tasks in Claude Code Desktop*. Claude Code documentation. https://code.claude.com/docs/en/desktop-scheduled-tasks
- Claude Help Center. *Use skills in Claude*. Undated ("Updated this week" on 16 November 2026). https://support.claude.com/en/articles/12512180-use-skills-in-claude
- Claude Help Center. *How to create custom skills*. Undated ("Updated over a week ago" on 16 November 2026). https://support.claude.com/en/articles/12512198-how-to-create-custom-skills

**Other vendors (vendor)**

- OpenAI. *Using skills*. OpenAI Academy, 10 April 2026. https://openai.com/academy/skills
- Tokuno, D. *Let skills in Gemini tackle your most repetitive tasks*. Google, blog.google, 30 September 2026. https://blog.google/products-and-platforms/products/gemini/automate-tasks-with-skills/
- Google. *About the transition from Gems to skills*. Gemini Apps Help, undated; read at https://support.google.com/gemini/answer/18560919?hl=en-JS. https://support.google.com/gemini/answer/18560919
- Google. *Schedules in Gemini Apps*. Gemini Apps Help, undated. https://support.google.com/gemini/answer/16316416?hl=en-GB

**Practice, as reported**

- Wikipedia. *Rule of three (computer programming)*. A reporter's account of a practice attributed to Don Roberts and popularised in Martin Fowler's *Refactoring: Improving the Design of Existing Code* (Addison-Wesley, 1999), which was not read for this unit. https://en.wikipedia.org/wiki/Rule_of_three_(computer_programming)

**The case**

- Academy case file (`generator/data/building-with-ai/case-academy.md`), compiled 11 November 2026, with its later notes; cited by section: §1, §2, §3, §5, §7, §9.

**This course**

- Units cited by section: BW1 (§1, §3, §6, §8; Deliverable Part 3); BW2 (§7; routing table rows 1, 2, 5 and 9); BW3 (Deliverable: the ten templates, template 3); BW4 (§1, §2, §5, §6, §7; Deliverable Parts 1 and 2); BW5 (Deliverable 2b); BW6 (§5; Deliverable steps C, E and F); BW7 (§1, §3, §5, §6, §7; Deliverable Part 1).

## Unsure list

1. agentskills.io is called "the format's documentation" (§2, §3, §4) because Claude Code's skills page links it for the eval format and OpenAI's page calls SKILL.md an open standard; who publishes and maintains agentskills.io was not checked.
2. Help-centre wording was read through fetch summaries, not line by line: "(200 characters maximum)", "Don't hardcode sensitive information (API keys, passwords)", "The ZIP should contain the skill folder as its root (not a subfolder)", "Review Claude's thinking to confirm it's loading the skill" (How to create custom skills) and "This feature requires code execution to be enabled", "Try being more explicit in your request" (Use skills in Claude), all 16 Nov 2026.
3. Other vendors read through fetch summaries: OpenAI's "A SKILL.md file is the skill's playbook" and @-mention (Using skills, 10 Apr 2026); Tokuno's "automatically run them whenever you enter a matching prompt" (30 Sep 2026); the Gems dates and the 100 MB file limit (About the transition from Gems to skills, undated). OpenAI's scheduled-tasks help page failed to load (not checked, not retried); "What are skills?" (Claude Help Center) was refused and not re-read, so §1 relies on BW4 §1's reading of 15 Nov 2026.
4. Deliverable F assumes `python3` is available in a Claude Code cloud run's default environment; the scheduled-tasks page names a setup script for dependencies but no page read says which interpreters the default image holds.
5. Deliverable F: whether the scheduled-task dialog offers a choice of model (and Haiku 5.5 in it), and in which time zone a Custom cron expression is read, were not checked on the page.
6. Whether a skill's script on claude.ai can write the report, `claims.tsv` and `sample.tsv` to a path the user can then download, and whether they persist past the chat, was not checked; the skill was tested by running its script locally, not inside claude.ai or a Claude Code session.
7. The trigger test set has not been run: no request was sent to any model for this unit, so whether the 193-character description passes its own sixteen requests is unknown.
8. Rule of three (§7): attribution to Don Roberts and Fowler's Refactoring (1999) rests on Wikipedia's article; the book was not read.
9. The pass thresholds of the trigger test (15 of 16, S1 3 of 3, no near-miss 3 of 3), the proportional extra draws in `check.py sample`, the order of steps in the skill and the choice of the rot check as the scheduled task are this unit's design (stated opinion), not sourced rules.
10. Agent Skills (platform overview) says custom skills do not sync across surfaces; Extend Claude with skills says claude.ai account skills load in cloud, Cowork and signed-in terminal sessions (v2.1.273 or later). Which holds for a skill uploaded today was not tested.
Object: the check-against-sources skill folder (its SKILL.md and scripts/check.py), Deliverable Part 1, sections B and C

Fresh check 2026-11-16 (Opus 5.5 (claude-opus-5-5)): fix · 3 errors, 9 should-fix, 11 minor; report `audits/building-with-ai/fresh-check-BW8.md`

Correction 2026-11-16, found by the figure re-check of row W-BW8 (corrections check `audits/building-with-ai/corrections-2026-11-16-BW8-r3-BW8.md`, Changes 1 and 2).
