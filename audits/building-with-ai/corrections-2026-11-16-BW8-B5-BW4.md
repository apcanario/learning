---
kind: corrections-check
row: W-BW8
course: building-with-ai
date: 2026-11-16
model: claude-opus-5-5
units: [B5, BW4]
chat: https://claude.ai/code/session_01KMmgQy4zywM5ERbdfFcK6a
---

The checker's report, verbatim from its report file, saved before any change was applied.

claude-opus-5-5

# W-BW8 corrections check (16 Nov 2026)

All sources re-read 16 Nov 2026 by WebSearch then WebFetch at a URL the search returned verbatim:
- https://support.claude.com/en/articles/12512180-use-skills-in-claude (H1 "Use skills in Claude")
- https://code.claude.com/docs/en/skills (H1 "Extend Claude with skills"; read in two parts, offset 0 and 100000)

Every Current below was counted by python3 in its file: each occurs exactly once.

## Change 1
File: B5-skills-and-automation.md
Current:
```
[Claude Help Center, *Using skills in Claude*](https://support.claude.com/en/articles/12512180-using-skills-in-claude)
```
Replacement:
```
[Claude Help Center, *Use skills in Claude*](https://support.claude.com/en/articles/12512180-use-skills-in-claude)
```
Result: PASS. The page at https://support.claude.com/en/articles/12512180-use-skills-in-claude (slug returned by search, fetched 16 Nov 2026) has the H1 "Use skills in Claude". This closes the fresh checker's gap: it fetched `-use-skills`, not this slug.
Syllabus: no conflict. B5 is a private source unit. BW8's brief re-verifies everything it carries over. A dated note will be appended by script (not included here). Out of scope and left unchanged: three more in-text links in B5 use the old title and slug, in §2 "What a description cannot do", Deliverable "Two files…" and the claude.ai install section. See Notes.

## Change 2
File: B5-skills-and-automation.md
Current:
```
*Using skills in Claude* (article 12512180). https://support.claude.com/en/articles/12512180-using-skills-in-claude
```
Replacement:
```
*Use skills in Claude* (article 12512180). https://support.claude.com/en/articles/12512180-use-skills-in-claude
```
Result: PASS. Same source as Change 1. H1 "Use skills in Claude" at https://support.claude.com/en/articles/12512180-use-skills-in-claude. This is the Sources entry named in source error 1 ("§1 item 2 and Sources").
Syllabus: no conflict. Private unit: a dated note will be appended by script.

## Change 3
File: B5-skills-and-automation.md
Current:
```
"Custom skills you upload are private to your individual account"
```
Replacement:
```
"Custom skills you upload aren't visible to colleagues until you share them"
```
Result: PASS. The page says: "Custom skills you upload aren't visible to colleagues until you share them." https://support.claude.com/en/articles/12512180-use-skills-in-claude. The old sentence is gone. I quote the page's whole sentence rather than the writer's split form, so the surrounding "and that …" clause still reads. The writer's added clause "sharing is on the Team and Enterprise plans" is dropped, because the fresh checker did not confirm it and corrections.md drops any clause it did not confirm. For the record, my own fetch does show "On Team and Enterprise plans, you can share skills you've created with specific colleagues, groups" and "On all other plans, each person uploads skills to their own account". The main chat may treat this as a proposal for a later pass. I did not apply it.
Syllabus: no conflict. Private unit: a dated note will be appended by script.

## Change 4
File: B5-skills-and-automation.md
Current:
```
The same page says skills "operate in Claude's secure sandboxed environment with no data persistence between sessions": a
```
Replacement:
```
The same page, as read on 29 Oct 2026, said skills "operate in Claude's secure sandboxed environment with no data persistence between sessions" (the sentence was not on the page on 16 Nov 2026): a
```
Result: PASS. My fetch of https://support.claude.com/en/articles/12512180-use-skills-in-claude on 16 Nov 2026: "The article doesn't address data persistence between sessions." The 29 Oct reading cannot be re-checked now. That date matches B5's own dating ("all opened 29 Oct 2026"; "As documented on 29 October 2026"). The writer's replacement ended in a full stop, which would leave ".: a skill cannot remember…". So the absence note goes in parentheses, and the colon and B5's following gloss stay attached to the dated quotation. Nothing else in the gloss changes.
Syllabus: no conflict. Private unit: a dated note will be appended by script.

## Change 5
File: B5-skills-and-automation.md
Current:
```
at 1,536 characters in its skill listing
```
Replacement:
```
at 1,536 characters by default in its skill listing
```
Result: PASS. https://code.claude.com/docs/en/skills, "Skill descriptions are cut short": "each entry's combined text is capped at 1,536 characters regardless of budget. The cap is configurable with `skillListingMaxDescChars`." The same section says: "When the listing overflows, Claude Code drops descriptions starting with the skills you invoke least". The writer did not ask for that clause in the text, and it is not added.
Syllabus: no conflict. Private unit: a dated note will be appended by script. Out of scope and left unchanged: B5's figure caption ("(1,536, description and when_to_use combined)") and §3 item 1 ("Claude Code keeps the first 1,536 characters") also state the cap without "by default". See Notes.

## Change 6
File: BW4-context-engineering.md
Current:
```
| Skills | Account |
```
Replacement:
```
| Skills | Account (claude.ai); a machine or a repository (Claude Code: [*Extend Claude with skills*](https://code.claude.com/docs/en/skills), read 16 Nov 2026) |
```
Result: PASS. https://code.claude.com/docs/en/skills, the table of where skills live:
- Personal: "All your projects on this machine, but not Cowork or cloud sessions"
- Project: "Sessions in this repository, but not cloud threads in a project"
- claude.ai account: "Cowork sessions, cloud sessions, and terminal sessions where you sign in with that account"

The wording is the writer's. I added the inline citation and its date because BW4 states that the "Reaches" column is documented, and BW4 does not cite this page anywhere (checked: 0 occurrences of code.claude.com/docs/en/skills). BW4's §1 heading dates its readings 15 Nov 2026, so the cell carries its own date. The page also shows that claude.ai account skills reach Claude Code terminal sessions signed in with that account. The new wording does not exclude this, and nothing beyond the writer's wording is added.
Syllabus: no conflict. BW4's brief asks for "the layers a project offers (… skills …) and what belongs in each"; the change refines a cell and does not alter what belongs there. No later brief (BW8, BW9, BW10) relies on "Account" for skills. F31, F32 and F38 concern the rot check, not this cell. The case file says nothing about skills.

## Change 7
File: BW4-context-engineering.md
Current:
```
- Anthropic. *Automate work with scheduled tasks*. Claude Code Docs. https://code.claude.com/docs/en/web-scheduled-tasks
```
Replacement:
```
- Anthropic. *Automate work with scheduled tasks*. Claude Code Docs. https://code.claude.com/docs/en/web-scheduled-tasks
- Anthropic. *Extend Claude with skills*. Claude Code Docs. https://code.claude.com/docs/en/skills
```
Result: PASS. H1 "Extend Claude with skills" at https://code.claude.com/docs/en/skills. This is the bibliography entry for the source Change 6 cites, which contradiction 1 itself cites. No other source is added. The list is not alphabetical, so the entry is appended after the last Anthropic Claude Code entry. Drop this change if Change 6 is not applied.
Syllabus: no conflict.

## Not a text change 1
Source error 5 (B5 §2, "The front matter has to parse"). No change. https://code.claude.com/docs/en/skills still says, under Troubleshooting: "If the frontmatter YAML is malformed, Claude Code loads the skill body with empty metadata, so `/skill-name` still works but Claude can't match against your `description`." The front-matter reference also says: "If the YAML between the markers doesn't parse, the skill still loads with no fields set". Both were confirmed 16 Nov 2026.
Proposed flag: none. It is recorded only so that no later pass flags it.

## Not a text change 2
Contradiction 2 (BW7 §9 "BW8 turns the procedure into something that runs itself"; BW7 Deliverable intro "BW8 turns a procedure in this form into a skill and a scheduled run"). The remedy is a flag, not a text change. The writer states that no text is wrong and proposes no wording. BW8 turns one stage of BW7's pipeline (the fresh check) into a skill and schedules BW4's rot check. That agrees with F32 (BW8's scheduled task is the rot check) and F55 (code gates before any model stage; final pass stays human).
Proposed flag:
- Units: BW7, BW8.
- Flag: tension. BW7's two forward pointers promise that BW8 automates the whole procedure. BW8 makes one stage (stage 3, the fresh check) a skill and schedules BW4's rot check, not a pipeline stage. A fresh check starts on an event, not a date, and needs outside hosts the default cloud environment does not allow (BW8 §6).
- Proposed change for a later corrections pass: BW7 §9 "BW8 turns one stage of the procedure, the fresh check, into a skill"; Deliverable intro "BW8 turns one stage in this form into a skill and schedules a different, date-driven check".

## Not a text change 3
Contradiction 3 (BW6 Deliverable step C2, "extra draws from the largest strata until the sample reaches *n*"). The remedy is a flag. BW6's rule is a method statement, not a sourced fact that a source contradicts, and BW8 states its departure in its own Deliverable. The same rule appears in four places in BW6:
- §2 step 2: "then more from the largest until the sample reaches its size"
- Deliverable C2
- the filled case text: "extra draws from the largest sections"
- the template blank: "extra draws from the largest strata"

Changing one would leave the others inconsistent, which goes beyond what this correction names. The writer's test, a literal "largest first" rule sending 20 of 29 draws to BW6's Deliverable, was done by script in BW8's chat and is not re-checkable from this packet.
Proposed flag:
- Units: BW6, BW8.
- Flag: tension (stratified draw). BW6 says extra draws go "from the largest strata". BW8's script draws one per stratum, then the rest at random from all remaining claims, so larger strata get more in proportion, and states this as a departure.
- Proposed change for a later corrections pass: in all four BW6 places, replace "then more/extra draws from the largest strata/sections" with "then the rest at random from all remaining claims, so larger strata get more in proportion".
- ⚠ The proposed BW6 change touches BW6's §2, Deliverable C2, its filled case text and its template.

## Not a text change 4
Contradiction 4 (BW3 template 9 "one in ten" against BW6 §5 acceptance number zero). No change. This is already F44 in syllabus-flags.md ("Tension (sampling threshold)", units BW3, BW5, BW6, BW8). BW8 follows BW6 and says so. No new flag is needed. F44 should gain a note that BW8 follows BW6's zero acceptance number.

## Notes (outside scope, not applied)
- B5 still uses the old title and slug `*Using skills in Claude*` / `12512180-using-skills-in-claude` in three in-text links the correction did not name: §2 "What a description cannot do", Deliverable "Two files, in one folder…" and the claude.ai install section ("As documented on 29 October 2026"). Applying Changes 1–2 alone leaves B5 with mixed titles. These are proposals for a later pass. B5 is private, and BW8 does not cite it.
- B5's figure caption and §3 item 1 state the 1,536 cap without "by default". Proposal as above.
- The Team and Enterprise sharing clause is confirmed by this check's own fetch (see Change 3). It is a proposal for a later pass, because the rule in corrections.md excluded it here.
