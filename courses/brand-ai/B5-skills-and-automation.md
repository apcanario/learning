---
code: B5
title: Skills and automation
course: brand-ai · B · Using AI to Build a Brand
model: Opus 5.5
written: 2026-10-29
search: off
---

# B5 · Skills and automation

The evidence in this unit is of three kinds, labelled where it appears. **Product documentation** is Anthropic's developer documentation, its Claude Code documentation and its help centre, each page opened on 29 October 2026; most help-centre pages carry only a relative "updated" label, so they are cited for that day. **Vendor guidance** is Anthropic's advice on writing skills, which states what it recommends and publishes no measurement behind it. **His setup** is the list of skills installed in his claude.ai account on 29 October 2026, the four skills kept as source in `apcanario/learning/skills/`, and what was observed in his claude.ai session that day; these are cited as "his installed skill list, 29 Oct 2026" or "observed", and cannot be opened by anyone else. Search was off; it was used only to check the skill format, the description limits, how skills load on each surface, scheduled tasks, custom connectors, GitHub's file-size limits and YouTube's title limit. What a context window is, which layers put text into it and what each costs are in B1 (§1, §6, §7) and B4 (§1, §3); this unit assumes them. B2 sets the model for each task, B3 the prompt templates the skill's steps are built from, and A3 the journey system the skill automates.

## 1 · What a skill is

A skill is a folder with one required file, `SKILL.md`. Anthropic's engineering post that introduced the format defines it in one sentence: "A skill is a directory containing a SKILL.md file" ([Zhang, Lazuka and Murag, *Equipping agents for the real world with Agent Skills*, Anthropic Engineering, 16 Oct 2025](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills); vendor guidance). The file has two parts.

**The front matter**, a block of YAML between two `---` lines at the top, holds the skill's `name` and `description`. The developer documentation sets the rules: the name has at most 64 characters, "only lowercase letters, numbers, and hyphens", and may not contain "anthropic" or "claude"; the description "Must be non-empty", has at most 1,024 characters, may not contain XML tags, and "must include both what the Skill does and when Claude should use it" ([Anthropic, *Agent Skills*](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview); product documentation).

**The body**, everything after the front matter, is the procedure: instructions in Markdown, written for the model. The folder may also hold other files, such as reference documents and scripts, which the body points to.

What makes a skill different from a long prompt is when each part is read. The documentation calls it progressive disclosure and gives three levels (same page):

| Level | When it is loaded | Cost, by Anthropic's figure | What it is |
|---|---|---|---|
| 1 · Metadata | "Always (at startup)" | "~100 tokens per Skill" | The name and description |
| 2 · Instructions | "When Skill is triggered" | "Under 5k tokens" | The body of `SKILL.md` |
| 3 · Resources | "As needed" | "None until accessed" | Bundled files; scripts run, and "only their output enters context" |

That is the property B4 §2 and §3 placed in the warm layer: a skill costs about a hundred tokens in every chat and its full weight only in the chats that use it. B4 §3 measured his four repository skills at 724 to 1,110 words, inside Anthropic's "under 5k tokens".

Three facts about where a skill lives, each from the same documentation and each consequential for him:

1. **Skills do not sync.** "Custom Skills do not sync across surfaces." A skill uploaded to claude.ai is not available through the API, and "Claude Code Skills are filesystem-based and separate from both claude.ai and the API" ([Agent Skills](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)). A skill he wants in claude.ai chats and in Claude Code sessions is uploaded once, if the Claude Code documentation is read, or twice, if the developer documentation is: see the disagreement box in §2.
2. **On claude.ai a skill needs code execution.** The help centre says skills require "code execution to be enabled", are switched on under Settings > Capabilities, and that "Custom skills you upload aren't visible to colleagues until you share them" ([Claude Help Center, *Use skills in Claude*](https://support.claude.com/en/articles/12512180-use-skills-in-claude)). The same page, as read on 29 Oct 2026, said skills "operate in Claude's secure sandboxed environment with no data persistence between sessions" (the sentence was not on the page on 16 Nov 2026): a skill cannot remember anything from one chat to the next. Whatever it needs to carry forward has to be written to a file somewhere else.
3. **In Claude Code a skill is a folder on disk.** Personal skills live in `~/.claude/skills/<skill-name>/SKILL.md` and reach "All your projects on this machine, but not Cowork or cloud sessions"; project skills live in a repository's `.claude/skills/` and reach "Sessions in this repository" ([Claude Code docs, *Skills*](https://code.claude.com/docs/en/skills)). A skill committed to a repository therefore travels with the repository into the cloud sessions and scheduled tasks that clone it, except cloud threads inside a Claude Code project, which the same page says do not load a repository's `.claude/skills/` (§4).

Anthropic's own warning about installing skills applies to his plugin list: "Use Skills only from trusted sources: those you created yourself or obtained from Anthropic", because "a malicious Skill can direct Claude to call tools or run code in ways that don't match the Skill's stated purpose" ([Agent Skills](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)). The documentation's advice is to treat a skill "like installing software".

## 2 · How triggering works, and why the description matters more than the body

The model decides to use a skill by reading its description and nothing else. At level 1 only the name and description are in the window; the body enters "When you request something that matches a Skill's description" ([Agent Skills](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)). His own session shows the same thing: the installed skills reach the model as a list of names and descriptions, and a skill's body is loaded only when the model calls a Skill tool with that name (observed in his claude.ai session, 29 Oct 2026). The consequence is the one fact this section exists to state: **a body the model never loads does nothing**, however good it is, and the only text that decides whether it loads is the description.

Anthropic's best-practice page says so directly: "The description is critical for skill selection: Claude uses it to choose the right Skill from potentially 100+ available Skills. Your description must provide enough detail for Claude to determine when to select this Skill, whereas the rest of `SKILL.md` provides the implementation details" ([Anthropic, *Skill authoring best practices*](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices); vendor guidance). The engineering post: "Pay special attention to the `name` and `description` of your skill" ([Anthropic Engineering, 16 Oct 2025](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)). Neither page describes the selection mechanism beyond this, and no Anthropic page read for this unit publishes a measured trigger rate.

**What the guidance asks of a description.** Four points, all vendor guidance from the best-practice page unless marked:

- **Third person.** "The description is injected into the system prompt, and inconsistent point-of-view can cause discovery problems." Good: "Processes Excel files and generates reports"; avoid: "I can help you process Excel files".
- **What it does and when to use it, with the words a request would contain.** "Be specific and include key terms." The page's bad examples are "Helps with documents", "Processes data" and "Does stuff with files".
- **Lean towards triggering.** Anthropic's skill-creator skill, its own tool for writing skills, says "currently Claude has a tendency to 'undertrigger' skills -- to not use them when they'd be useful", and asks authors to make descriptions "a little bit 'pushy'" ([anthropics/skills, `skill-creator/SKILL.md`](https://github.com/anthropics/skills/blob/main/skills/skill-creator/SKILL.md); vendor guidance).
- **Expect simple requests to bypass the skill.** The same file: "Claude only consults skills for tasks it can't easily handle on its own — simple, one-step queries like 'read this PDF' may not trigger a skill even if the description matches perfectly." Complex, multi-step or specialised requests "reliably trigger skills when the description matches." The word "reliably" carries no figure.

**How long a description can be.** The limits differ by surface, and the differences matter for anything he writes.

> **Where sources disagree.** The developer documentation allows 1,024 characters ([Agent Skills](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)). The claude.ai help page on creating custom skills gives "200 characters maximum" ([Claude Help Center, *How to create custom skills*](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills)). Claude Code truncates "the combined `description` and `when_to_use` text" at 1,536 characters by default in its skill listing, and when a user has many skills it "drops some descriptions to fit the listing's character budget", which "scales at 1% of the model's context window" ([Claude Code docs, *Skills*](https://code.claude.com/docs/en/skills)). Read together: a description that must work on claude.ai is kept to 200 characters, with the trigger words first, because that is the strictest limit and the first words are the ones every surface keeps.

```viz
{
 "kind": "compare",
 "title": "Description length limits, in characters",
 "unit": "",
 "rows": [
  {
   "label": "journey-chain description",
   "value": 186,
   "tone": 2
  },
  {
   "label": "claude.ai help page",
   "value": 200,
   "tone": 4
  },
  {
   "label": "Developer docs",
   "value": 1024,
   "tone": 3
  },
  {
   "label": "Claude Code listing",
   "value": 1536,
   "tone": 3
  }
 ],
 "caption": "The limits on a skill's description by surface, against the Deliverable's own description. §2, from Anthropic, <a href=\"https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview\"><em>Agent Skills</em></a> (1,024), Claude Help Center, <a href=\"https://support.claude.com/en/articles/12512198-how-to-create-custom-skills\"><em>How to create custom skills</em></a> (200) and Claude Code docs, <a href=\"https://code.claude.com/docs/en/skills\"><em>Skills</em></a> (1,536, description and when_to_use combined); all opened 29 Oct 2026. The 186 is this unit's Deliverable A."
}
```

> **Where sources disagree.** The developer documentation says custom skills do not sync and that Claude Code skills are "filesystem-based and separate from both claude.ai and the API". The Claude Code documentation says the opposite for his account's skills: "In a Cowork or cloud session, Claude Code loads the skills enabled for your claude.ai account", and terminal sessions signed in with the account download them too ([Claude Code docs, *Skills*, "Skills synced from claude.ai"](https://code.claude.com/docs/en/skills)). Read together: a skill uploaded to claude.ai reaches his cloud sessions and scheduled tasks; committing it to the repository's `.claude/skills/` is a second route the same page documents for "cloud sessions other than project threads", and the one that does not depend on the sync.

**What a description cannot do.** It cannot force a skill to run every time. The Claude Code page's own troubleshooting for a skill that does not trigger begins with "Check the description includes keywords users would naturally say" and "Try rephrasing your request to match the description more closely", and ends with invoking it by name ([Claude Code docs, *Skills*](https://code.claude.com/docs/en/skills)); the claude.ai help page suggests the same: "Try being more explicit in your request", for example "Use my brand guidelines skill to create a presentation" ([*Using skills in Claude*](https://support.claude.com/en/articles/12512180-using-skills-in-claude)). The reliable trigger is a fixed opening word he always types. The skill in the Deliverable is built on one: every session note starts with "Take".

**The front matter has to parse.** Claude Code "reads the frontmatter only when the opening `---` is the file's first line", and "If the frontmatter YAML is malformed, Claude Code loads the skill body with empty metadata, so `/skill-name` still works but Claude can't match against your `description`" ([Claude Code docs, *Skills*](https://code.claude.com/docs/en/skills)). A colon followed by a space inside an unquoted value is the commonest way to break YAML. One of his four repository skills has one: `audit-units`'s description reads "Run a Learning Project audit with Fable 5.1: the four-unit …", and a strict YAML parser (PyYAML 6.0.3) rejects that front matter with "mapping values are not allowed here"; the other three parse (checked by script on `skills/*/SKILL.md`, 29 Oct 2026). His claude.ai account lists the skill with its description (his installed skill list, 29 Oct 2026), so the claude.ai uploader evidently tolerates it; how it parses is undocumented. In Claude Code, on the documented rule, the skill would load without a description and never fire on its own. The fix is to put the description in double quotes, which the Deliverable's skill does.

**How to test a description.** Anthropic's guidance is to build tests before the body: "Create evaluations BEFORE writing extensive documentation", three scenarios at least, tested "with all the models you plan to use it with" ([best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)). For triggering specifically, the skill-creator file asks for about 20 test requests, 8 to 10 that should trigger and 8 to 10 that should not, and says the useful negatives are "near-misses — queries that share keywords or concepts with the skill but actually need something different" ([`skill-creator/SKILL.md`](https://github.com/anthropics/skills/blob/main/skills/skill-creator/SKILL.md)). The help centre's version is lighter: "Try several different prompts that should trigger it" and check the model's thinking to confirm it loaded the skill ([*How to create custom skills*](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills)). The Deliverable ships its test set.

## 3 · How his existing plugin skills fire

His account lists 19 installed skills with their descriptions (his installed skill list, 29 Oct 2026). Read against §2, they share five features. Counts are by script on the descriptions as listed.

**1. Most are longer than the claude.ai help page allows.** The 19 descriptions run from 170 to 495 characters, 6,217 in all, a mean of 327; 16 are over 200. At B1 §2's arithmetic of about 2.7 characters per token that is roughly 2,300 tokens in every chat, in line with B4 §3's estimate from Anthropic's 100 tokens per skill. They were installed as plugin skills, and whether the 200-character limit applies to that route is undocumented; that they all appear in his list shows they were accepted. The cost to him is in the listing, which is paid every turn (B1 §2), and in the risk that a surface truncates them: Claude Code keeps the first 1,536 characters and drops whole descriptions when the listing overflows its budget (§2). None of his is near 1,536; the budget rule is the one to watch as the list grows.

**2. Eleven name the words he says.** "brain dump", "/dump", "should I", "which one", "torn between", "shutdown", "wrap the week", "what should I watch tonight": eleven of the 19 descriptions quote the phrases that should fire them. That is the guidance's "include key terms" (§2) in its most concrete form, and it is why those skills fire on the phrase. His course skill `write-unit` carries no quoted phrase but names the codes he types ("B1, A3, Rome 11.3"), which does the same job.

**3. Six are written to over-fire.** "Trigger even when not explicitly invoked" (`brain-dump-processor`), "Trigger aggressively" (`shutdown-ritual`, `decompression-mode`), "Trigger even if he doesn't explicitly ask for a decision" (`pedro-decision-forcer`), "Use whenever …" (`curiosity-inbox`), "even if they don't say the word" (`market-competitors`). That is the skill-creator's "pushy" advice taken at full strength. Its cost is collisions: a pushy skill wins requests that belonged to another. Two of his are pushy about the same kinds of input. `brain-dump-processor` fires on "a wall of text with multiple unrelated threads", and a dictated take after a long run can read exactly like that. `curiosity-inbox` fires on "a topic that's clearly orthogonal to the current thread". A journey workflow that takes pasted transcripts has to claim them first, in its description and with a fixed opening word, or the triage skill will take them (the Deliverable does both).

**4. Five fire on the clock.** `shutdown-ritual` ("after 18:00 Lisbon on a workday"), `decompression-mode` ("after 21:30 Lisbon time"), `sunday-three` ("between Sunday 18:00–22:00 Lisbon time"), `friday-fifteen` ("Friday 16:00–19:00 Lisbon") and `hyperfocus-rider` ("crosses meal times … or the 22:30 sleep window"). A time condition can only work if the current time is in the window. The model has no clock of its own; in his session the current time is available through a tool the model has to call (observed in his claude.ai session, 29 Oct 2026). Whether the time is inserted into every claude.ai chat is undocumented. A clock trigger is therefore a request for the model to check the time first, on every message, before it knows whether the skill matters. The phrase triggers in the same descriptions are the dependable half.

**5. Three depend on another skill firing them.** `pre-mortem` ("Auto-trigger when the Reversibility Classifier flags one-way door") and `weighted-matrix` ("Auto-suppressed by the Reversibility Classifier") refer to a classifier, and no skill of that name is installed (his installed skill list, 29 Oct 2026). `trip-frame` says "Pre-mortem auto-fires for trips >€2000 or >7 days". No page read for this unit documents a way for one skill to fire or suppress another; each loads on its own description (§2). The classifier clauses cost tokens and fire nothing; the `trip-frame` clause works only if the model reads it as an instruction to load `pre-mortem` as well, which is undocumented. The fix is to write the condition into the description that should fire, in words a request would contain ("hard-to-reverse", "over €2000").

```viz
{
 "kind": "compare",
 "title": "Of his 19 installed skills",
 "unit": "",
 "max": 19,
 "rows": [
  {
   "label": "Over 200 characters",
   "value": 16,
   "tone": 4
  },
  {
   "label": "Quote the words he says",
   "value": 11,
   "tone": 2
  },
  {
   "label": "Written to over-fire",
   "value": 6,
   "tone": 5
  },
  {
   "label": "Fire on the clock",
   "value": 5,
   "tone": 5
  },
  {
   "label": "Depend on another skill",
   "value": 3,
   "tone": 5
  }
 ],
 "caption": "How many of his 19 installed skills show each of the five features read against §2. §3, counted by script on the descriptions in his installed skill list in claude.ai, 29 Oct 2026 (observed; not a published source)."
}
```

**The decision cluster.** Four skills claim decisions: `pedro-decision-forcer` (any "should I", 2 or more options), `weighted-matrix` (3 or more options and 3 or more criteria), `decision-council` (an "important decision", no trigger phrase) and `pre-mortem` (irreversible ones). Their descriptions separate them by thresholds the model has to judge, and `decision-council`'s description, the shortest at 170 characters, names no trigger at all. Which of the four fires on a given request is undocumented and untested. The test set method in §2 is how he would find out: ten near-miss requests across the four, run once, with the model's choice recorded.

**What his four repository skills do differently.** `write-unit`, `file-unit`, `audit-units` and `new-course` have descriptions of 185 to 251 characters, start with the action, name their object ("one course unit in the Learning Project", "a finished Learning Project unit"), and end with a "Use when" sentence. Their bodies open with a stop condition: §1 of `write-unit` is "Check you may start", and of `audit-units` "Check you may run" (`skills/*/SKILL.md`). That is the shape DD-B3 §5 asked B5 to take: an outcome description, with the check that says a step is done and what the step may not touch. The Deliverable copies it.

## 4 · Scheduled tasks: what they can and cannot touch

A scheduled task is a saved prompt that runs on its own, in a new session, at set times. B1 §7 drew the consequence that matters most: "A scheduled task knows nothing of the chat that created it." B4 §1 listed the kinds. Two concern him.

**Claude Code cloud tasks.** "A cloud scheduled task, formerly a routine, is a saved Claude Code configuration: a prompt, one or more repositories, and a set of connectors, packaged once and run automatically", on Anthropic's infrastructure, "so they keep working when your laptop is closed" ([Claude Code docs, *Automate work with scheduled tasks*](https://code.claude.com/docs/en/web-scheduled-tasks); product documentation, labelled research preview). From the same page, as of 29 October 2026:

- **Can touch: the repositories selected.** "Each repository is cloned at the start of a run." The run "uses skills", and those include "the ones committed to the cloned repository". It pushes to "a branch prefixed with `claude/` unless your prompt directs it to push to another branch"; branch protection on GitHub is how he limits that.
- **Can touch: the connectors included, with writes.** "All of your connected MCP connectors are included by default. Remove any the task doesn't need: Claude can use an included connector during a run, including writes." Anything done through them "appears as you".
- **Can touch: the network the environment allows.** The default environment allows only an allowlist of package registries and development domains; requests to other hosts "fail with `403`". Connectors bypass that allowlist because they go "through Anthropic's servers".
- **Cannot touch: his computer.** Cloud tasks run in a VM; local files and apps belong to Desktop scheduled tasks, a separate feature.
- **Cannot ask him anything mid-run, in practice.** Runs start in auto mode, where "a classifier model allows or blocks actions"; a run still "stops and waits" on an action that needs approval, and the answer comes only when he opens the run. His session's own note on scheduled tasks says the same: an unattended run "usually has nobody to approve" (observed in his claude.ai session, 29 Oct 2026).
- **Cannot be approved by its own prompt.** "The fired prompt is therefore not live user input and can't act as approval or consent for actions during the run."
- **Limits.** The prompt "must be self-contained and explicit about what to do and what success looks like"; schedules more often than hourly are rejected; a run on the hour "can start several minutes late"; runs "draw down subscription usage the same way interactive sessions do".

**Cowork tasks.** In the desktop app, "Each scheduled task runs as its own Cowork session"; tasks "have access to the same capabilities as regular Cowork tasks, including connected tools, skills, and installed plugins"; they "run on their cadence even when your computer is asleep", and "If a scheduled task requires local files or apps, it will only run locally" ([Claude Help Center, *Schedule recurring tasks in Claude Cowork*](https://support.claude.com/en/articles/13854387-schedule-recurring-tasks-in-cowork)). The page names an "approval mode" without explaining its options.

**What that means for the journey chain.** Four lines, each from the facts above:

1. **A scheduled task can draft, and only he can publish.** Every step of the chain ends in something public: an upload, a post, an email to the list. A run that can reach YouTube, Instagram or a mail connector can publish as him without a human in the loop. Willison's lethal trifecta, as DD-B3 §2.3 set it out, is private data plus untrusted content plus the ability to send; a run holding his takes and a Gmail connector has two of the three. The chain's task gets no connectors at all.
2. **It needs its inputs in the repository.** The run sees only what it clones. Takes recorded on his phone reach the run only once they are committed (§5).
3. **It needs a check it can run without him.** A task that cannot tell pass from fail hands him a draft he must check in full, which saves nothing. The skill ships a script for that (Deliverable, `check_quotes.py`), following Claude Code's best-practice line that DD-B3 §2.1 quotes: "Give Claude something it can run that comes back pass or fail."
4. **One step qualifies.** The weekly journal entry (step 2) has a fixed input (the week's takes), a fixed output (one file), a mechanical check, and a reader who reads it anyway (A3's checklist C budgets the reading). The record and the script need his judgement in the same sitting (A3 §6 puts them in the Friday outline hour); the titles, the Short and the email go public. Those stay in chats he opens.

The weekly task is in the Deliverable, with DD-B3's four guards for unattended runs (operating rule 7): one folder it may change, a fixed cap (one run a week), a pass/fail check, and keep-or-revert (a `claude/` branch he merges or deletes).

## 5 · The GitHub vault and pcblueprint as backends

A skill keeps nothing between sessions (§1). Every step of the chain reads files and writes files, so the chain needs a place that does keep them. A3 §1 handed this unit the question: "Where the folders live, and how the chain reads them, is B5's."

### The vault

His course already runs on one: `apcanario/learning`, where `courses/<course>/` holds every filed unit and every chat clones the repository and ends with a commit and push (`method.md`, Home; B4 §2). The journey chain uses the same pattern in a separate repository.

**Pick: a new private repository for the journey text; footage stays out of git.**
- The course build publishes `kit/academy/` to a public site (B4 F15); takes do not belong near it.
- GitHub blocks files over 100 MiB and recommends repositories "ideally less than 1 GB" ([GitHub Docs, *About large files on GitHub*](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github)).
- Cloud sessions and scheduled tasks clone a GitHub repository and push to it (§4).

Override if: he already keeps his takes in another store that a chat can read and write, and wants one store; then `season.md`'s paths point there and the scheduled task is dropped.

The repository's name is his choice; this unit writes `journey` as a placeholder. Its layout, one folder per season:

    journey/
      .claude/skills/journey-chain/      the skill (Deliverable), for Claude Code sessions and scheduled tasks
      season-2-half-marathon/
        season.md                        label, target, syllabus by fortnight, what stays out
        takes/2026-11-03-easy-run.md     step 1
        entries/2026-11-03.md            step 2
        records/2026-11-20.md            step 3
        episodes/ep01/script.md          step 4
        episodes/ep01/titles.md          step 5
        episodes/ep01/shorts.md          step 6
        emails/2026-11-26.md             step 7
        numbers/                         exports from pcblueprint (below)

Footage and screenshots stay in the per-session folders A3 §1 set up, wherever his editor reads them; `season.md` records the path. The repository holds only text.

**How each surface reaches the vault.** As documented on 29 October 2026:

- **claude.ai chat with the GitHub integration** reads only: selected files are added to the chat or project, "Only files (names and contents) in a repo on a specific branch are synced", updates arrive with "Sync now", and "The repositories must fit within Claude's context window" ([Claude Help Center, *Use the GitHub integration*](https://support.claude.com/en/articles/10167454)). The page says nothing about writing. A chat reached this way can read a week's takes and give back the entry's text, which he saves.
- **A Claude Code cloud session** clones and pushes. It can be started from the browser or "the **Code** tab in the Claude app" on his phone ([Claude Code docs, *Use Claude Code in the cloud*](https://code.claude.com/docs/en/claude-code-on-the-web)). A take pasted into such a session on the repository, starting with "Take", is filed by the skill as step 1 and committed in the same minute. That is the capture route this unit recommends; that it fits his evenings is untested.
- **A scheduled task** clones the repository on every run and pushes to a `claude/` branch (§4).

### pcblueprint

pcblueprint ("The Protocol") is his own data infrastructure, built in April 2026: a REST API serving his workouts (562 and more), biometrics and biographical archive, across three repositories (archive, website, Android app); AIssistant, a personal agent on his NAS built on DeepSeek and Telegram, already uses it as a backend (observed in his claude.ai session, 29 Oct 2026). He built it as a deliberate act against forgetting ("Só morre quem é esquecido"), which is the brand thesis's "records the process so he does not forget it" in another form.

For the chain it is the source of numbers: a session's distance, pace or a weigh-in. There are three ways to put those numbers in front of a model, and the documentation decides between them.

1. **A custom connector.** claude.ai can connect to a remote MCP server, but "your MCP server must be reachable over the public internet from Anthropic's IP ranges", and servers "behind a VPN, or blocked by a firewall won't connect" ([Claude Help Center, *Get started with custom connectors using remote MCP*](https://support.claude.com/en/articles/11175166)). pcblueprint is a REST API, not an MCP server, so this route means writing an MCP wrapper and exposing his biometric archive to the internet. The same page warns that connectors reach "arbitrary services that have not been verified by Anthropic".
2. **A direct call from a cloud session or scheduled task.** The default environment blocks hosts outside its allowlist (§4); his API would have to be added to a custom environment's allowed domains, with its key stored as a network secret ([*Automate work with scheduled tasks*](https://code.claude.com/docs/en/web-scheduled-tasks)). The run would then hold his biometric data and his takes together.
3. **An export file.** A script, run by him or by AIssistant, writes the numbers a fortnight needs into `numbers/` as a small file; the chain reads that file like any other input.

**Pick: the export file.**
- Numbers come from code, never from a model (B2, "Biometrics parsing"; B1 §5).
- Nothing in his archive faces the internet for this.
- The record shows exactly which numbers the episode used.

Override if: DD-B1, which owns agents, recommends a connector with a reasoned threat model; then route 1, with the connector added to chats only, never to the scheduled task. (DD-B1 §3, 2 Nov 2026, set out the threat model and does not recommend one; route 3 stands.)

The export script is B2's: Haiku 5.5 writes and maintains it; the script does the parsing. Which numbers are published is A4's question (A3 §1), and until A4 is filed the skill publishes none (its `publish_numbers` list starts empty).

## 6 · When a skill is worth writing, and when a saved preference is enough

His account has three places to put a standing instruction: the preferences (every chat), a Project's instructions (every chat in that Project), and a skill (the chats whose request matches). B4 §1's table gives each layer's scope; the help centre draws the line in one sentence each: custom instructions "apply broadly to all your conversations", projects hold "static background knowledge", and skills "are task-specific and only load when relevant, making them better for specialized workflows" ([Claude Help Center, *What are skills?*](https://support.claude.com/en/articles/12512176-what-are-skills)). Claude Code's documentation states the dividing rule for its own instruction file in terms that transfer: keep it "to facts Claude should hold in every session", and "If an entry is a multi-step procedure or only matters for one part of the codebase, move it to a skill" ([Claude Code docs, *How Claude remembers your project*](https://code.claude.com/docs/en/memory); vendor guidance, applied to claude.ai by analogy as in B4 §1).

From those sources, the test is four questions, in order. The questions are my synthesis; each traces to a source above.

| Question | If yes | If no |
|---|---|---|
| Must it hold in every chat, whatever the task? | Preference (or Project instruction, if only in one Project) | Next question |
| Is it more than one sentence of procedure, with steps in an order? | Next question | A line in a B3 template, typed when needed |
| Does it recur at least weekly, the same way each time? | Next question | A B3 template, pasted when needed |
| Can each step's output be checked against something other than his taste? | Skill | B3 template; he is the check |

Two corollaries. A rule about tone, format or decision style is a preference, however often it matters, because it is true in every chat; that is why his tone rules sit in his preferences (B1 §6; B3 §4). And a procedure he runs once a season is a template, because the description it would add costs tokens in every chat of every week (§3) for a body loaded four times a year.

**Applied to his workflows.** The journey chain passes all four: it is seven steps in a fixed order, runs every week of a season (A3, checklist B to E), and each step has a mechanical check (every quotation in the source; a word limit; one Short; three titles). None of his 19 installed skills covers it. Shōmen posts (B3 template 6) pass the first three questions and fail the fourth, since the check is his eye on two locked styles; they stay a template. The weekly email alone would fail the second question; it earns its place only as step 7 of the chain.

**What a skill cannot carry.** It cannot pick the model: on claude.ai the model and effort are set in the chat before the first message (B2 §7), and a skill can only say which it expects. The skill below names the model for each step in its table and says so in its first line when the chat runs on another; the decision stays his. B7, still to be written, owns the content pipeline's model choices; until it is filed the skill uses B2's rows.

## Deliverable · The journey-chain skill, with install steps

Built for the chain A3 fixed: dictated takes after each session, a weekly journal entry, a fortnightly record, the episode script, titles, the Short and the weekly email. Each step is one of B3's templates turned into an outcome description: the artefact, the check that says it is done, and what the step may not touch, with no reasoning scripted (DD-B3 §5).

```viz
{
 "kind": "flow",
 "steps": [
  {
   "label": "1 · Take",
   "note": "After each session"
  },
  {
   "label": "2 · Journal entry",
   "note": "After the week's last session"
  },
  {
   "label": "3 · Record",
   "note": "Friday, week A"
  },
  {
   "label": "4 · Script",
   "note": "Friday, week A"
  },
  {
   "label": "5 · Titles",
   "note": "Tuesday, week A"
  },
  {
   "label": "6 · Shorts cut list",
   "note": "Wednesday, week A"
  },
  {
   "label": "7 · Weekly email",
   "note": "Thursday, every week"
  }
 ],
 "caption": "The seven steps of the journey chain and when each runs; each reads the files the step before it wrote. Drawn from this unit's Deliverable A (the skill's step table, §0), built on the chain A3 fixed (A3, checklists D and E)."
}
```

**Where it follows the filed units over the brief.** The brief names the chain; A3 revised three of its numbers, and the skill takes A3's:

- **Episode length: about 10 minutes, 12 at most.** A3's brief gave 10–20 minutes; A3 §2 set "about 10 minutes, 12 at most" from A2's editing hours.
- **Shorts: one per episode.** A3's brief gave two or three; A3 §3 set one from A2 §4's reading of the AIR Media-Tech and Metricool data (vendor, correlational).
- **Email: weekly, 300 words or fewer.** A3 §3 sets one email a week, the episode week with the video and one lesson, the other week a note, and "300 words or fewer" as his rule.

The days are A3's checklist D and E (Friday record and script, Tuesday titles and publishing, Wednesday Short, Thursday email). The models are B2's rows; titles and the Short have no B2 row and take B3 template 5's analogy (Sonnet 5.5, low). The 100-character title limit is YouTube's: the Data API's `snippet.title` "has a maximum length of 100 characters" ([YouTube Data API, *Videos*](https://developers.google.com/youtube/v3/docs/videos); product documentation).

### A · The files

Two files, in one folder named `journey-chain` (the folder name must match the skill name: [*Using skills in Claude*](https://support.claude.com/en/articles/12512180-using-skills-in-claude)).

**`journey-chain/SKILL.md`** (163 lines, 12,406 characters, about 4,600 tokens at 2.7 characters per token, inside Anthropic's "under 5k tokens" and its "under 500 lines"; the description is 186 characters, inside claude.ai's 200):

    ---
    name: journey-chain
    description: "Runs one step of Pedro's journey chain: take, journal entry, fortnight record, episode script, titles, Shorts cut list, weekly email. Use when a message starts with Take or names a step."
    ---

    # Journey chain

    One step per chat. Each step reads the files the step before it wrote and writes one file. Nothing is published by this skill: every output is a draft he reads, corrects and publishes himself.

    ## 0. Before any step

    1. Name the step. If the request does not make it clear, the step is the earliest one whose input exists and whose output does not. A message that starts with "Take" is a take (step 1): a session note, however unstructured; it is never a brain dump.
    2. First line of the reply: `Step <n> · <name> · <model>, <effort>` from the table below. If this chat runs on a different model, say so in that line.
    3. Read `season.md` (template in §8). If it is missing, write it with him first; it is the only step that asks questions.
    4. Read only the inputs the step names. Never read footage, screenshots or anything outside the season folder.

    | Step | When (weeks run Tuesday to Monday) | Input | Output file | Model, effort |
    |---|---|---|---|---|
    | 1 · Take | After each session | One transcript | `takes/<date>-<session>.md` | Haiku 5.5, low |
    | 2 · Journal entry | After the week's last session | The week's takes | `entries/<date of the week's Tuesday>.md` | Sonnet 5.5, medium |
    | 3 · Record | Friday, week A | The fortnight's entries | `records/<Friday date>.md` | Opus 5.5, medium |
    | 4 · Script | Friday, week A | The record and the takes | `episodes/ep<nn>/script.md` | Opus 5.5, medium |
    | 5 · Titles | Tuesday, week A, before publishing | The final script of the episode going out | `episodes/ep<nn>/titles.md` | Sonnet 5.5, low |
    | 6 · Shorts cut list | Wednesday, week A | The final script, with the episode timestamps he adds after the edit | `episodes/ep<nn>/shorts.md` | Sonnet 5.5, low |
    | 7 · Weekly email | Thursday, every week | The latest entry; in an episode week, also the record the episode was cut from; links | `emails/<send date>.md` | Sonnet 5.5, low |

    Paths are inside the season folder. In a session with the repository, write the file and commit it as `<season> step <n>: <file>`. In a chat without it, give the file's full text in one block with its path above it, for him to save.

    ## Rules for every step

    - His words stay his. Quote takes and entries word for word; reorder and cut freely; rewrite nothing he said. A sentence you wrote is marked `[C]` (or `[NEW]` in a script) and is one sentence at most.
    - Quote in the language he spoke. A translation is marked `[TR]` beside the original.
    - Every failure, miss and skipped session in the input stays in the output at the weight the input gives it. Add no lesson, no reframing, no encouragement.
    - Numbers come only from a take, an entry, or a pcblueprint export file in `numbers/`, quoted as given. If a figure needs arithmetic, write the arithmetic as a short script, run it, and give its output; never compute in prose.
    - Nothing on the `leave_out` list in `season.md` appears in any output. Other people appear only by their role in a session.
    - A weight or health number goes into a script, title, Short or email only if `season.md` lists that kind of number under `publish_numbers`. The list stays empty until he sets his disclosure policy.
    - Avoid in every output: jokes he did not make; a closing line about believing in yourself; asking anyone to subscribe or share; emoji.
    - End the reply with one line: `Next: step <n> · <name> · <model>, <effort> · due <day>`.

    ## 1 · Take

    TASK: File one dictated take as a dated note.

    OUTPUT: front matter `date`, `session` (run, long run, test, weigh-in, karate, coaching, history), `journey`; then three headings, `What I did`, `What did not work`, `What changes next session`, each holding his sentences from the transcript in his order; then `Transcript` with the transcript unchanged.

    CONSTRAINTS: Remove filler words only under the three headings; the `Transcript` section keeps everything. A prompt he did not answer gets `(not said)`. Never fill a heading from inference.

    DONE WHEN: all three headings exist; every sentence under them occurs in the transcript; the transcript is unchanged.

    MAY NOT: merge two sessions into one file; correct a number he said.

    ## 2 · Journal entry

    TASK: Write one dated entry for the week from its takes.

    OUTPUT: front matter `week` (the Tuesday), `journeys`; then `What happened` (dated bullets, oldest first, one line each, each ending with his quoted sentence), `What went wrong`, `What changed`, `Numbers` (only those in the takes or `numbers/`, each with its date and file).

    CONSTRAINTS: One bullet per session at most. A week with no takes for a journey says so in one line. A week with no takes at all gets an entry that says so.

    DONE WHEN: every bullet has a date and a quotation found in the takes; every "What did not work" item from the takes is under `What went wrong`; `check_quotes.py` passes.

    MAY NOT: edit a take; carry anything from an earlier entry unless this week's takes repeat it.

    ## 3 · Record

    TASK: Write one dated record of the fortnight from its entries.

    OUTPUT: five sections. (1) What happened: dated bullets, oldest first. (2) What I said at the time: exact quotations, each with its date. (3) What went wrong: every failure or setback the entries record. (4) What changed between the first entry and the last. (5) Open questions the entries raise and do not settle. Then (6) Syllabus step: the step `season.md` names for this fortnight, and one line on whether the entries show it reached, missed or partly reached, with the quotation that shows it.

    CONSTRAINTS: Use only the entries. Where two entries disagree, give both with their dates. Keep every failure at the weight the entries give it.

    DONE WHEN: every bullet has a date; every quotation appears word for word in the entries; every failure is in section 3; nothing appears that the entries do not contain, except lines marked `[C]`; `check_quotes.py` passes.

    MAY NOT: name a miss the entries do not name; soften one they do.

    ## 4 · Script

    TASK: Cut the script for episode <nn> from the record and the fortnight's takes.

    READER: a viewer who has never heard of him, arriving from browse or suggested, deciding in the first 30 seconds whether the title was true.

    OUTPUT:
    1. Hook, the first 30 seconds: the lines that make the working title true, with the season label said once.
    2. Where this sits: one line placing the episode in the syllabus ("week <n> of <total>", from `season.md`). In a season's first episode, the syllabus in full instead.
    3. Chapters: for each, a title of a few words and a one-line purpose, then its lines in order. At least three chapters; the first starts at 00:00.
    4. The miss: one thing that did not work, named in his words, in its own chapter or inside one.
    5. Ending: the last line, from the takes. In a finale, the artefact, then the next season's name, target and opener date.
    6. Gaps: every line he must record, shot he must film or claim that needs a source before it goes on camera.
    Mark every line `[T<n> mm:ss]` (take, with timestamp where the transcript has one), `[R]` (record) or `[NEW]`.

    CONSTRAINTS: Planned runtime about 10 minutes, 12 at most; flag any cut that would run longer. A `[NEW]` line is one sentence and bridges two of his lines; he rewrites every one. Keep the doubts and failures the takes contain. No claim of fact not in the takes or the record; no training advice; no invented jokes; no subscribe request.

    DONE WHEN: every line carries an origin mark; the hook makes the working title true within 30 seconds of speech; exactly one miss is named; at least three chapters; every gap is listed; `check_quotes.py` passes against the takes and the record.

    MAY NOT: change the record; promise an outcome the takes do not contain.

    ## 5 · Titles

    TASK: Write three title options for episode <nn>, for one Test & Compare run.

    OUTPUT: a table, three rows: Title | Angle | The line from the first 30 seconds that makes it true (quoted, with its mark) | Thumbnail text (only if he gives a word limit).

    CONSTRAINTS: Every title ends with the season label in the form `season.md` gives and is 100 characters or fewer including it. Three different angles on the same episode. Each must be true of the first 30 seconds. English unless he asks for a Portuguese variant. His register, from his two published titles: "Sometimes You Win, Sometimes You Learn To Lose" and "Being a Better Athlete Made Me a Worse Person".

    AVOID: a promise the episode does not keep; a question it does not answer; "you won't believe", "the truth about", "nobody tells you"; whole words in capitals for volume; any time, weight or result the script does not state.

    DONE WHEN: three rows, three angles; every row quotes its hook line; every title is 100 characters or fewer, counted in code.

    MAY NOT: edit the script to fit a title.

    ## 6 · Shorts cut list

    TASK: Choose the one Short for episode <nn> and list the cut.

    OUTPUT: (1) The pick: start and end timestamps in the final cut, 30 to 60 seconds; its first line and last line, quoted; why it stands alone without the episode, in one line; the vertical-crop check (is the subject in the centre third in every shot of the cut). (2) Two reserves, same fields, used only if the pick fails the crop check. (3) The Short's title, 100 characters or fewer, ending with the season label. (4) Related video: episode <nn>.

    CONSTRAINTS: One Short per episode. Never two published from one episode. The cut must make sense to someone who has not seen the episode. It may contain the miss.

    DONE WHEN: one pick and at most two reserves; each 30 to 60 seconds by its timestamps; the related video is set to the episode; quotations pass `check_quotes.py`.

    MAY NOT: propose new footage; join two separate moments into one Short.

    ## 7 · Weekly email

    TASK: Write this week's email for <send date>.

    READER: subscribers to the list. Some follow one journey only; all of them chose to receive it.

    OUTPUT: one subject line and one alternative; then the body under the heading `## Body`, 300 words or fewer; links as plain web links, one per item. Episode week: (1) the lead journey, what happened, in his words, with one lesson he stated in the record; (2) one line on each other live journey in `season.md`, only if something moved; (3) the episode, with its link. Off week: (1) a note from the lead journey, in his words; (2) one line on each other live journey, only if something moved; (3) the latest episode's link. Nothing else.

    CONSTRAINTS: Every fact comes from the material named in the table. Quote him where it has his words. Failures and missed weeks stay in, stated plainly. British English. No Shōmen promotion unless he asks for it in this request.

    AVOID: "I hope you're well"; "exciting news"; any line asking for shares; motivational sign-offs.

    DONE WHEN: one lead journey; `check_quotes.py --max-words 300` passes; every link is one he gave; every fact is in the material.

    MAY NOT: send, schedule or upload anything; add a journey that is not in `season.md`.

    ## 8 · `season.md` template

    ```
    ---
    season: 2
    label: <the exact suffix every title ends with, set before the season; {n} is the episode number>
    lead: half marathon
    target: sub-1:45 half marathon
    race: <date, or "not set">
    first_upload: <date>
    episodes_planned: <n>
    other_live: [weight, history course, karate coaching]
    leave_out: [<topics that stay out of every output>]
    publish_numbers: []
    footage: <where the session folders with clips and screenshots live>
    ---
    ## Syllabus, one step per fortnight
    | Fortnight | Week A starts | Step | Episode |
    |---|---|---|---|
    | 1 | <date> | <step> | ep01 |
    ```

    ## 9 · Checking quotations

    `scripts/check_quotes.py` (in this skill's folder) is run as `python3 scripts/check_quotes.py OUTPUT SOURCE [SOURCE ...] [--max-words N]`. It passes when every quotation of four words or more in OUTPUT occurs word for word in the sources, ignoring case and punctuation, and, with `--max-words`, the `## Body` section is within the limit. Run it where code execution is available and report PASS or the failing lines. Where it is not available, check every quotation by eye against the source and say that the check was by eye. An output that fails is fixed before it is handed over.

**`journey-chain/scripts/check_quotes.py`** (Python 3, standard library only; tested on 29 Oct 2026 against a sample take and an output with one invented quotation, which it caught):

    #!/usr/bin/env python3
    """Check a journey-chain output against its sources.

    usage: python3 check_quotes.py OUTPUT SOURCE [SOURCE ...] [--max-words N]

    Passes when every quoted span in OUTPUT ("..." or curly quotes, four words or
    more) occurs word for word in the SOURCE files, ignoring case, punctuation and
    line breaks. With --max-words, also fails when the section under the heading
    "## Body" (or the whole file, if it has none) is longer than N words.
    Prints PASS or FAIL with every failing line; exit code 0 or 1.
    A quotation that spans a line break in OUTPUT is not checked; keep each quotation on one line.
    """
    import re
    import sys


    def words(text):
        text = text.replace("’", "'").replace("‘", "'")
        return re.findall(r"[0-9a-zà-ÿ']+", text.lower())


    def main(argv):
        max_words = None
        if "--max-words" in argv:
            i = argv.index("--max-words")
            max_words = int(argv[i + 1])
            argv = argv[:i] + argv[i + 2:]
        if len(argv) < 2:
            print(__doc__)
            return 2
        out = open(argv[0], encoding="utf-8").read()
        src = " " + " ".join(words(" ".join(open(p, encoding="utf-8").read() for p in argv[1:]))) + " "
        fails = []
        for q in re.findall(r'"([^"\n]+)"|“([^”\n]+)”', out):
            span = q[0] or q[1]
            w = words(span)
            if len(w) >= 4 and " " + " ".join(w) + " " not in src:
                fails.append("not in sources: “" + span + "”")
        if max_words is not None:
            m = re.search(r"^## Body\s*$(.*?)(?=^## |\Z)", out, re.M | re.S)
            n = len(words(m.group(1) if m else out))
            if n > max_words:
                fails.append("body is %d words; limit %d" % (n, max_words))
        print("FAIL" if fails else "PASS")
        for f in fails:
            print("  " + f)
        return 1 if fails else 0


    if __name__ == "__main__":
        sys.exit(main(sys.argv[1:]))

### B · Install

**claude.ai (chats, including the phone app).** As documented on 29 October 2026 ([*Using skills in Claude*](https://support.claude.com/en/articles/12512180-using-skills-in-claude); [*How to create custom skills*](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills)):

1. Settings > Capabilities: turn on "Code execution and file creation" (skills need it, and the script needs it to run).
2. Make the ZIP with the folder at its root: `zip -r journey-chain.zip journey-chain` from the folder that contains `journey-chain/`. "The ZIP should contain the skill folder as its root (not a subfolder)."
3. In the Skills section, "Upload skill", choose the ZIP, and switch the skill on (the creating page names the place as Customize > Skills).
4. Run the test set (C) in a new chat outside the Learning Project, since the skill has nothing to do with the course (B2, "Run small tasks in a light chat").

**Claude Code (cloud sessions, the phone's Code tab, the scheduled task).** The skill enabled on claude.ai loads in cloud sessions and scheduled tasks by the Claude Code documentation (§2, disagreement); the same folder is also committed to the journey repository at `.claude/skills/journey-chain/`, so the task runs even if the sync does not. Every session and scheduled run that clones the repository then has it ([*Skills*](https://code.claude.com/docs/en/skills); [*Automate work with scheduled tasks*](https://code.claude.com/docs/en/web-scheduled-tasks)).

**Before the first take.** Create `season-2-half-marathon/season.md` from the template in the skill's §8: the label, the target, the syllabus by fortnight from A3's checklist A, and `publish_numbers: []` until A4 is filed. The first request in a new chat, "Take" with nothing else, makes the skill ask for it.

### C · Test set

Run each line once in a new chat after installing; record whether the skill loaded (the reply's first line names a step) and which skill fired if another did. Built to the skill-creator's method (§2): should-trigger requests in different phrasings, and near-misses that share words with the skill. Two misses on either list mean the description is rewritten and the set run again.

Should trigger:

1. "Take. Long run, 16 k. Legs fine until 12, then the left calf went. Walked twice. Next time gel at 8."
2. "Take — easy 6 k, nothing to report except I went out too fast again."
3. "Write this week's journal entry from the takes in season 2."
4. "Do the fortnight record for weeks 3 and 4."
5. "Cut the script for episode 3 from the record and the takes."
6. "Titles for ep 2, it goes out Tuesday."
7. "Which bit of episode 2 should be the Short?"
8. "Thursday email, off week."

Should not trigger (near-misses):

1. "Brain dump: work stuff, the race, Shōmen stock, the history course, dentist." (`brain-dump-processor`)
2. "Write a Shōmen post about the new gi in both styles." (B3 template 6)
3. "Draft a reply to the race organiser about my bib number." (`pedro-voice-drafter`)
4. "Should I race a spring half or wait for a summer one?" (`pedro-decision-forcer`)
5. "What should I watch tonight, 90 minutes?" (`queue-match`)
6. "Wrap the week." (`friday-fifteen`)
7. "Write unit B6." (`write-unit`)
8. "Write me a training plan for a sub-1:45 half." (no skill; and no training advice belongs in the chain)

### D · The weekly scheduled task

One Claude Code cloud task, created at claude.ai/code/routines or with `/schedule` ([*Automate work with scheduled tasks*](https://code.claude.com/docs/en/web-scheduled-tasks)). Settings, each with its reason:

- **Repository:** the journey repository only (the run sees nothing else).
- **Connectors:** remove all of them; they are included by default and can write (§4).
- **Environment:** Default, Trusted network; it needs no outside host.
- **Model:** Sonnet 5.5, the model of step 2 (B2, "Journal entries").
- **Schedule:** weekly, Tuesday 07:10 Lisbon time: the morning after the week ends (weeks run Tuesday to Monday, A3 Deliverable 2), a few minutes past the hour because runs on the hour can start late.
- **Branch protection** on the default branch, with no bypass for administrators, so the run can only push its `claude/` branch: the documentation says a rule his connected GitHub access can bypass "doesn't block a run's push".

The prompt, self-contained as the documentation requires:

> Clone the journey repository. Find the season folder whose `season.md` has the latest `first_upload` date. Using the journey-chain skill in `.claude/skills/journey-chain/`, run step 2 (journal entry) for the week that ended yesterday: the week runs Tuesday to Monday, and the input is every file in that season's `takes/` dated inside the week. Write only `entries/<Tuesday date>.md` in that season folder; change no other file. Run `python3 .claude/skills/journey-chain/scripts/check_quotes.py` on the entry against the week's takes. If it passes, commit the entry to a new branch named `claude/entry-<Tuesday date>` and push it. If it fails, fix the entry and run the check again, at most twice; if it still fails, push the branch anyway with `CHECK FAILED` as the first line of the entry. If the week has no takes, write an entry that says so and push it the same way. Use no connector and send nothing. Success is one pushed branch with one new file and the check's result in the run's last message.

He reads the entry on the branch in his quarter-hour (A3 §6; checklist C), corrects it, and merges or deletes the branch. If two consecutive runs need more than five minutes of correction each, the task is paused and step 2 goes back to a chat he opens (DD-B3, operating rule 6: two misses, then a new brief).

### E · Done when

The skill is installed when: the ZIP uploads and the skill appears switched on; at least seven of the eight should-trigger requests name a step in their first line; at most one of the eight near-misses does; the folder is committed at `.claude/skills/journey-chain/` in the journey repository; and the scheduled task's first run pushes a `claude/entry-…` branch with the check's result.

## Sources

All web sources opened 29 October 2026.

- Anthropic. *Agent Skills* (overview). Claude Platform docs. https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview
- Anthropic. *Skill authoring best practices*. Claude Platform docs. https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices
- Anthropic. `skill-creator/SKILL.md`, in the repository anthropics/skills (GitHub). https://github.com/anthropics/skills/blob/main/skills/skill-creator/SKILL.md
- Zhang, Barry, Keith Lazuka and Mahesh Murag. *Equipping agents for the real world with Agent Skills*. Anthropic Engineering, 16 October 2025. https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills
- Claude Code docs. *Skills*. https://code.claude.com/docs/en/skills
- Claude Code docs. *Automate work with scheduled tasks* (research preview). https://code.claude.com/docs/en/web-scheduled-tasks
- Claude Code docs. *Use Claude Code in the cloud*. https://code.claude.com/docs/en/claude-code-on-the-web
- Claude Code docs. *How Claude remembers your project* (Memory). https://code.claude.com/docs/en/memory
- Claude Help Center. *Use skills in Claude* (article 12512180). https://support.claude.com/en/articles/12512180-use-skills-in-claude
- Claude Help Center. *How to create custom skills* (article 12512198). https://support.claude.com/en/articles/12512198-how-to-create-custom-skills
- Claude Help Center. *What are skills?* (article 12512176). https://support.claude.com/en/articles/12512176-what-are-skills
- Claude Help Center. *Schedule recurring tasks in Claude Cowork* (article 13854387). https://support.claude.com/en/articles/13854387-schedule-recurring-tasks-in-cowork
- Claude Help Center. *Get started with custom connectors using remote MCP* (article 11175166). https://support.claude.com/en/articles/11175166
- Claude Help Center. *Use the GitHub integration* (article 10167454). https://support.claude.com/en/articles/10167454
- GitHub Docs. *About large files on GitHub*. https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github
- YouTube Data API. *Videos* resource (`snippet.title`, "maximum length of 100 characters"), the basis of the skill's title limit. https://developers.google.com/youtube/v3/docs/videos
- His setup, cited as observed, not as published sources: his installed skill list in claude.ai, 29 October 2026 (19 skills with their descriptions); his claude.ai session, 29 October 2026 (skills listed by name and description, bodies loaded by a Skill tool; the time read through a tool; scheduled-task behaviour); pcblueprint and AIssistant as described in that session; `apcanario/learning` at commit `30b2157`: `skills/write-unit/SKILL.md`, `skills/file-unit/SKILL.md`, `skills/audit-units/SKILL.md`, `skills/new-course/SKILL.md`, `docs/method.md` (Home), `docs/courses-index.md`.
- Filed units cited by section: A2 · Audience and platform economics (§4, §6, Deliverable 2); A3 · The journey system (§1, §2, §3, §6, Deliverables 1 and 2); B1 · Mental model (§2, §5, §7); B2 · Choosing the model (§7, routing table); B3 · Prompting that holds up (§4, §5, templates 3, 4, 5, 6, 10); B4 · Context engineering (§1, §2, §3, F15); DD-B3 · Deep dive: how the best practitioners use the tool (§2.1, §2.3, §5, operating rules 6 and 7).

## Unsure list

1. **Description limit on claude.ai.** The help centre gives 200 characters; the developer documentation gives 1,024; 16 of his 19 installed plugin skills exceed 200 and are listed anyway. Which limit applies to a skill uploaded as a ZIP today was not tested; the skill's 186-character description is inside both.
2. **How claude.ai parses front matter.** The unquoted colon in `audit-units`'s description fails strict YAML, and the documented consequence (no description, no automatic triggering) is Claude Code's; claude.ai lists the skill with its description, so its uploader tolerates the colon by some rule that is undocumented.
3. **Trigger reliability has no figure.** "Undertrigger" and "reliably trigger" are Anthropic's words in the skill-creator file, with no measurement published; the test set's pass thresholds (seven of eight, at most one of eight) are my rule.
4. **Whether the current time reaches every claude.ai chat** is undocumented; the argument that clock-based triggers are fragile rests on the observation that his session reads the time through a tool.
5. **Which of his four decision skills fires** on a given request is untested; the overlap in §3 is read from the descriptions only.
6. **Skills in cloud sessions started from the phone.** The scheduled-tasks page says runs use skills committed to the cloned repository; that an interactive cloud session from the Code tab loads `.claude/skills/` is documented for "cloud sessions other than project threads" (Claude Code docs, *Skills*), and was not tested.
7. **pcblueprint's endpoints, hosting and network exposure** are not documented in any source this unit could open; the three routes in §5 are argued from Anthropic's connector and environment rules, not from his system's design.
8. **The journey repository does not exist yet**; its name (`journey`) and layout are this unit's proposal, and the capture route through the phone's Code tab is untested against his evenings.
9. **The Shorts step's model** (Sonnet 5.5, low) and the titles step's model have no B2 row; both are analogies from B3 template 5, and B7 may change them.
10. **Scheduled tasks are in research preview**; the branch prefix, connector defaults, auto-mode behaviour and hourly limits the task relies on may change.

Fresh check 29 Oct 2026 (Fable 5.1): fix · 1 error, 4 should-fix, 5 minor; all applied; report `audits/brand-ai/fresh-check-B5.md`.

Erratum 2026-11-16, found by BW8's writer (confirmed by its fresh check; corrections check `audits/building-with-ai/corrections-2026-11-16-BW8-B5-BW4.md`, Changes 1 to 5).
