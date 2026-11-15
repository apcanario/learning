# W-BW3 · corrections check (BW3)

Checker: claude-opus-5-5, 15 Nov 2026. Each Current below was counted in its file and occurs exactly once.

## 1 · Source error 1 (B3 §2, "Where sources disagree")

FILE: courses/brand-ai/B3-prompting-that-holds-up.md (packet copy: sources-B3.md, line 67)

Current:
```
and that this "differs from GPT models, which benefit from very precise instructions"
```
Replacement:
```
and that this "differs from GPT models, which benefit from precise instructions"
```
PASS. Source: OpenAI, *Prompt engineering*, https://developers.openai.com/api/docs/guides/prompt-engineering (search returned this URL; fetched 15 Nov 2026). The page reads: "Generally speaking, reasoning models will provide better results on tasks with only high-level guidance." and "This differs from GPT models, which benefit from precise instructions." The word "very" is not on the page. The other quotation in the same B3 sentence ("reasoning models will provide better results on tasks with only high-level guidance") matches the page and is left alone. "very precise" occurs once in sources-B3.md, so no second occurrence needs a correction.

**Syllabus:** no conflict. The change affects only the private source unit. BW3 §2 (line 62) already quotes the corrected wording. No brief relies on the word.

## 2 · F3: BW1 §8 layer map names no unit

FILE: courses/building-with-ai/BW1-*.md (packet copy: BW1.md, line 206)

Current:
```
The map below names the layers this course uses; later units fill them in.
```
Replacement:
```
The map below names the layers this course uses; later units fill them in (erratum 15 Nov 2026: the chat in BW3 and BW4; projects, memory, and tools and connectors in BW4, memory also in BW10; skills in BW8; agents in BW9).
```
PASS. Briefs:
- BW3: "how a long conversation drifts, and when to restart".
- BW4: "the layers a project offers (instructions, knowledge files, memory, skills, tools and connectors, scheduled tasks) and what belongs in each"; "when to start a new chat and when not to".
- BW10: "which material belongs in memory, in a project, in a private store or nowhere".
- BW8: "what a skill is as its format's own documentation defines it, how triggering works".
- BW9: "what an agent is against a chat (tools, loops, autonomy)"; "subagents and isolated contexts".

**Syllabus:** no conflict. BW1's brief says the layers are "a map the later units fill in", and the replacement only names those units. No brief relies on §8 naming no unit.

## 3 · F3: diagnosis table, Part 3, row "Two vendor pages, or two of your own files, give different values"

FILE: BW1 (packet line 356)

Current:
```
| A product fact that differed between two of the vendor's own pages (§5) | BW6 |
```
Replacement:
```
| A product fact that differed between two of the vendor's own pages (§5) | BW4, BW6 (erratum 15 Nov 2026: was BW6) |
```
PASS. The row covers two cases. BW6's brief covers the vendor-pages case ("how to read a research report (the hierarchy of sources, vendor data, ...)"). It does not cover the case of two of your own files. BW4's brief does: "one source of truth and its mirrors; how a project rots (stale files, duplicated rules, instructions that contradict each other)".

**Syllabus:** no conflict. BW1's Gives line ("the diagnosis table BW3, BW4 and BW6 point back to") still holds. BW6 keeps the row.

## 4 · F3: diagnosis table, Part 4, same row

FILE: BW1 (packet line 373)

Current:
```
| Name the authoritative source; record the conflict | BW6 |
```
Replacement:
```
| Name the authoritative source; record the conflict | BW4, BW6 (erratum 15 Nov 2026: was BW6) |
```
PASS. The evidence is the same as in change 3. Part 4 says the first four columns are the course's shared vocabulary, so the two tables have to agree.

**Syllabus:** no conflict. The reason is the same as in change 3.

## 5 · F3: diagnosis table, Part 3, row "A skill fires when it should not, or fails to fire"

FILE: BW1 (packet line 358)

Current:
```
| Vendor documentation: [*Agent Skills*](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview.md) | No instance in the case file | BW4 |
```
Replacement:
```
| Vendor documentation: [*Agent Skills*](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview.md) | No instance in the case file | BW8 (erratum 15 Nov 2026: was BW4) |
```
PASS. The row's cause is "Skills trigger on their description alone" and its fix is "Rewrite the description". BW8's brief covers exactly this: "how triggering works and why the description matters more than the body; testing whether it triggers". BW4's brief names skills only as one layer among those a project offers, "and what belongs in each". Triggering is not in it.

**Syllabus:** minor tension, not a contradiction. BW1's Gives line names "the diagnosis table BW3, BW4 and BW6 point back to". After this change BW4 has one row fewer to point back to, and BW8 is not named in that line. BW8's brief takes "BW4, BW6, BW7", not BW1, so no brief relies on this row naming BW4.

## 6 · F3: diagnosis table, Part 4, same row

FILE: BW1 (packet line 376)

Current:
```
| Rewrite the description | BW4 |
```
Replacement:
```
| Rewrite the description | BW8 (erratum 15 Nov 2026: was BW4) |
```
PASS. The evidence is the same as in change 5.

**Syllabus:** the same minor tension as in change 5.

## 7 · F3: diagnosis table, Part 3, row "The usage limit is reached early"

FILE: BW1 (packet line 360)

Current:
```
| No instance in the case file (it holds no measure of usage spent, §9) | BW4 |
```
Replacement:
```
| No instance in the case file (it holds no measure of usage spent, §9) | BW4, BW10 (erratum 15 Nov 2026: was BW4) |
```
PASS. BW10's brief is about this symptom: "what a subscription measures and how its usage windows work ... what burns usage for no gain (re-reading large files, giant pastes, chats that never end, research run twice); when a new chat is cheaper". BW4 stays because its brief covers part of the row: "what loads every turn against what loads on demand, and the cost of each". BW10 takes BW1, so it can point back to the row.

**Syllabus:** no conflict. BW10 "Takes: ... BW1, BW2, BW4, BW9".

## 8 · F3: diagnosis table, Part 4, same row

FILE: BW1 (packet line 378)

Current:
```
| New chat per task; fewer connectors | BW4 |
```
Replacement:
```
| New chat per task; fewer connectors | BW4, BW10 (erratum 15 Nov 2026: was BW4) |
```
PASS. The evidence is the same as in change 7.

**Syllabus:** no conflict.

## Not corrected

- BW1 row "A new chat does not know something said in an earlier chat" (BW4): correct as routed. BW4 covers "the layers a project offers (instructions, knowledge files, memory ...) and what belongs in each".
- BW1 row "An instruction given early in a long chat stops being followed" (BW3, BW4): correct as routed. BW3 covers "how a long conversation drifts, and when to restart"; BW4 covers "when to start a new chat". BW3 §5 treats it.
- BW1 row "A long attached document is used unevenly" (BW3): correct as routed. BW3 covers "where the question sits in a long prompt"; BW3 §4 treats it, and its fix agrees with BW1's "question last".
- BW1 rows "confident claim with no source", "cited page does not say", "out of date" (BW6): correct as routed. BW6 covers "how models fail (confident, specific, wrong; stale facts presented as current; invented citations)" and checking against sources.
- BW1 row "The same request gives materially different answers" (BW6): left unchanged. No brief names run-to-run variation. BW1 §5 ties it to checking ("One good answer is one draw"), which fits BW6's "know what a clean sample proves". The routing is arguable, but it does not send the row to a unit that plainly cannot treat it.
- BW1 row "The output follows one rule and breaks another" (BW4): correct as routed. BW4 covers "instructions that contradict each other".
- BW1 row "A large project answers from the wrong file" (BW4): correct as routed. BW4 covers "what happens to a large knowledge set (retrieval)".
- BW1 Unsure list item 1: left unchanged. It is a dated record of what BW1's writer had, and it is still true as a record. The errata above settle the question it raises.
- BW1 §8 note bullets and table rows: unchanged. The only gap was the missing unit codes (change 2).
- Contradictions between BW3 and BW1/BW2: none found. BW3 §4's "TASK first, material in tags, TASK again at the end" agrees with BW1's "put the question after the material". BW3's model lines match BW2 Part 1: row 2 small · Haiku 5.5, high; row 3 mid · Sonnet 5.5, medium; row 4 large · Opus 5.5, high; row 5 Fable 5.2, high; rows 6 and 7 Opus 5.5 medium and xhigh; row 8 mid · Sonnet 5.5, medium; row 9 large, top rung · Fable 5.2, high; row 10 Opus 5.5, high.
- F10: no correction. BW1 §5 says temperature, top_p and top_k are not supported on Claude 4.7 and later and that a non-default value returns an error (dated 15 Nov 2026). BW3 says "On current Claude models temperature cannot be set (BW1 §5)" and labels Laban et al.'s temperature-0 result as measured on 2025 models. These agree. BW2 says nothing about sampling controls.
- BW3-notes "Not carried" items (the B3 citation of the Fable 5.1 guide; Google's *Prompt design strategies*): no correction. They are not errors in B3, only items left out of BW3.

Changes: 8 proposed, 8 pass, 0 fail, 0 syllabus conflicts (changes 5 and 6 carry a minor tension, noted)
