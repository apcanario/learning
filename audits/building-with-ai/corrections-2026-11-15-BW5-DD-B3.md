---
kind: corrections-check
row: W-BW5
course: building-with-ai
date: 2026-11-15
model: claude-opus-5-5
units: [DD-B3, BW3]
chat: https://claude.ai/code/session_01KMmgQxb5xyzkrLHQ6hh6WQ
---

The checker's report, verbatim, saved before any change was applied.

Model: claude-opus-5-5
Verdict: 2 pass, 1 fail, 0 syllabus conflicts

Web reads, 16 Nov 2026, each URL taken verbatim from a WebSearch in this run:
- https://code.claude.com/docs/en/best-practices.md (the `.md` page BW3 and BW5 cite)
- https://code.claude.com/docs/en/best-practices?ref=t01.li (the HTML page DD-B3 cites, `.../best-practices`; the search returned it only with a `?ref=` parameter, so this is the closest copy fetched)
- https://harper.blog/2025/02/16/my-llm-codegen-workflow-atm/
- https://kiro.dev/blog/introducing-kiro/

Script counts: every Current below occurs exactly once in its file. The changes do not overlap.

## Change 1
File: DD-B3-deep-dive-how-the-best-practitioners-use-the-tool.md, §2.1, "Claude Code best practices", third bullet under "What the current page keeps". Count: 1.
Current:
```
then "start a fresh session to build from it."
```
Replacement:
```
then "start a fresh session to execute it" (page read 15 Nov 2026).
```
Result: FAIL. DD-B3 cites the HTML page `https://code.claude.com/docs/en/best-practices` (no `.md`). On 16 Nov 2026 that page, fetched with the `?ref=` parameter, holds the quoted words verbatim: "Once `SPEC.md` exists, start a fresh session to build from it, so the build begins with a clean context and a written definition of done." The `.md` URL that the writer and the fresh checker read serves a different version of the page. That version has "Once the spec is complete, start a fresh session to execute it." and none of the other wording in DD-B3 §2.1, such as "What you can stop doing", "comes back pass or fail", "without having watched it being written" or "`/clear` plus one new prompt". All of that wording is on the HTML page. DD-B3's quotation is therefore correct for the page it cites. Make no change.
Source: "Once `SPEC.md` exists, start a fresh session to build from it, so the build begins with a clean context and a written definition of done." (https://code.claude.com/docs/en/best-practices?ref=t01.li, read 16 Nov 2026). Against: "Once the spec is complete, start a fresh session to execute it." (https://code.claude.com/docs/en/best-practices.md, read 16 Nov 2026).
Syllabus: no conflict. Because the change fails, nothing changes. Proposed flag: Anthropic serves two different texts of *Best practices for Claude Code*, one at `.../best-practices` and one at `.../best-practices.md`. BW3 (§5, §6, On other tools) and BW5 (§1, §11, Sources) quote and cite the `.md` text, and they quote it correctly. DD-B3 quotes and cites the HTML text, and it also quotes correctly. Any unit that quotes this page should name which URL it read, and the staleness check should re-read the same URL.

## Change 2
File: DD-B3-deep-dive-how-the-best-practitioners-use-the-tool.md, §2.5, "Harper Reed (16 February 2025)". Count: 1.
Current:
```
have a reasoning model turn the spec into a plan of small, test-driven prompts (`prompt_plan.md`) and a checklist
```
Replacement:
```
have a reasoning model turn the spec into a plan of "small, iterative chunks that build on each other" (`prompt_plan.md`), in a test-driven variant or a plain one, and a checklist
```
Result: PASS. Reed gives two planning prompts, one for TDD and one without it. Both contain the quoted sentence. Only the TDD prompt asks for steps implemented "in a test-driven manner", so DD-B3's "test-driven" presents one variant as if it were the whole method. The writer's replacement had no comma before "and a checklist". I widened the Current to include that phrase and added the comma, so that the list stays readable. The words and the claim are otherwise as the writer gave them.
Source: "Then, once you have a solid plan, break it down into small, iterative chunks that build on each other." (in both prompts) and, in the TDD prompt only, "a series of prompts for a code-generation LLM that will implement each step in a test-driven manner." (https://harper.blog/2025/02/16/my-llm-codegen-workflow-atm/, read 16 Nov 2026)
Syllabus: no conflict. DD-B3 is a private source unit. BW5 §1 already presents Reed without the test-driven framing. No brief in briefs/ and no line of case-academy.md depends on "test-driven". Source error 3 is dropped, as the fresh check said, and I confirm the drop: the page reads "Your codegen tool should be able to check off the `todo.md` while processing. This is good for keeping state across sessions."

## Change 3
File: DD-B3-deep-dive-how-the-best-practitioners-use-the-tool.md, §2.5, "AWS Kiro (14 July 2025)". Count: 1.
Current:
```
then tasks "linked to requirements"
```
Replacement:
```
then tasks ordered by their dependencies, each linked to requirements
```
Result: PASS, with one word amended. The page does not hold the phrase "linked to requirements", so the quotation marks are wrong. I used the unquoted variant, as the fresh check directed, except that the writer's "each linked to a requirement" becomes "each linked to requirements". The page says "links each to requirements". The singular would add a one-requirement-per-task limit that the source does not state. The S3 card in DD-B3's appendix ("tasks linked to requirements", unquoted) already matches and needs no change.
Source: "Kiro generates tasks and sub-tasks, sequences them correctly based on dependencies, and links each to requirements." (Nikhil Swaminathan and Deepak Singh, 14 Jul 2025, https://kiro.dev/blog/introducing-kiro/, read 16 Nov 2026)
Syllabus: no conflict. BW5's own presentation of Kiro is not touched, and no brief depends on the quotation.

## Not a text change 1
Item B (Contradiction 1, BW3 Deliverable, "Conventions": "One brief per chat. If the first output misses, change the brief and open a new chat (§5)."). BW3's text is right and stays unchanged. The rule is BW3's restart rule for a single brief. It rests on BW3 §5, which reads Claude Code's guide ("Run `/clear` and start fresh with a more specific prompt that incorporates what you learned", .md page, confirmed 16 Nov 2026) and Laban §7.4. BW3's brief asks for briefing a single task. Its Gives line ("the brief form BW5 uses per unit") does not ask BW3 to state project-level change control. BW5 §5 already quotes BW3 exactly and narrows the rule for a specified project: the brief still changes and the unit still restarts in a new context, but the change goes through a flag, a boundary, a new version and a decision-log entry (§9). The two units are consistent, so the conflict is only apparent and is resolved in BW5's text. Contradiction 1 cites no outside source beyond the BW3 and BW5 text and the Claude Code page above. Flag: an optional forward pointer in BW3's convention ("(in a specified project, through BW5 §9)") is a syllabus decision about forward references in a course read in order. Decide it at the next review, or refuse it. No text change in this run.

## Not a text change 2
Item C (Contradiction 2). The BW5 brief's preamble says "Deliverables are built twice: in full on the case …", and its deliverable is "worked on the Academy case as it was specified". case-academy.md holds the method's rules (§2: a goal in one sentence, three measurable outcomes, eight to twelve units, one brief per unit, a shared preamble) but no spec document, non-goals, preamble or brief text, unit list in build order, or decision dates. This is a brief and case-file matter, not an error in BW5's text: BW5 reconstructs from §2 and marks each gap [NOT IN CASE FILE], as the brief allows ("never infer a fact about the case that the file does not hold … list it in the notes as a need"). Flag: a need against the case file. It joins F19 (open), which asks for a real preamble and unit brief, and adds a course's unit list with Takes and Gives, any recorded non-goals and the dates of the decisions in BW5 Deliverable 1e. No text change.

New: none. A note on Change 1's Syllabus line proposes a flag (two served texts of the Claude Code page). It is not a text error: every unit quotes the version it cites correctly.
