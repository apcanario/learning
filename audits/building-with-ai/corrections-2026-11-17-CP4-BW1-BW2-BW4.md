Checker: claude-opus-5-5. Corrections check of corrections.md (29 changes to BW1, BW2 and BW4) against case-academy.md, briefs BW1, BW2, BW4, syllabus-flags.md and sourcing-standard.md Part 1 and Part 6. Script: every Current occurs exactly once in its file, and all 29 apply in sequence; the three New blocks below also apply in sequence in place of the changes they replace (the PASS changes plus New 1 to 3). No replacement holds an em dash; en dashes appear only in date ranges, as in the case file; spelling is British; no American -ize, -or or -er form found. No private term found by reading; kit/private_terms.py is not in the packet and was not run. BW8, BW9 and BW10 were not in the packet, so no change was checked against them. PASS 26, FAIL 3, New 3.

## Change 1
File: BW1-mental-model.md, Deliverable Part 3, diagnosis table, row "A large project answers from the wrong file", Academy case instance (F4)
Current:
````
| No instance in the case file | BW4 |
````
Replacement:
````
| No instance in the case file: its project knowledge held 33 files, 907,260 characters (about 363,000 tokens), and whether it ran in retrieval mode was not known (§7); the record does not say whether any failure was traced to retrieval mode (§9) | BW4 |
````
Result: FAIL. The facts hold (case file §7, line 144; §9, line 245), but 'its project knowledge' follows 'No instance in the case file:', so 'its' reads as the case file's knowledge; the case file has none. 'whether it ran' has the same referent. See New 1.
Syllabus: F4 names this row (row 11 of BW1's case diagnosis table); no brief changed; no other filed unit in the packet contradicted.

## Change 2
File: BW1-mental-model.md, Deliverable Part 3, diagnosis table, row "The usage limit is reached early", Academy case instance (F4)
Current:
````
No instance in the case file (it holds no measure of usage spent, §9)
````
Replacement:
````
The largest history writing session (28 reports) stopped twice on usage limits and resumed both times; an audit chat was stopped by a shorter-window limit of the auditing model after 18% of that model's weekly allowance (§7); no measure of usage per unit (§9)
````
Result: PASS. Case file §7 (line 147): the 28-report session stopped twice and resumed; an audit chat stopped by a shorter-window limit after 18% of the auditing model's weekly allowance. §9 (line 247): no usage per unit. Reads in place in the Academy case instance column.
Syllabus: no conflict: F4 names this row (row 12); no brief changed; no unit contradicted.

## Change 3
File: BW2-choosing-the-model-and-the-effort.md, §5, The case (F18)
Current:
````
(case file §2; the file does not record the writer of each draft)
````
Replacement:
````
(case file §2; case file §5 records Opus 5.5 as the writer of all 36 drafts)
````
Result: PASS. Case file §5 (line 152): every one of the 36 was written by Opus 5.5. The sentence that follows ('a fresh context of the writer's own model') still holds and is now supported per draft.
Syllabus: no conflict: F18 (and F103) name the writer of each of the 36 drafts; BW2 brief unchanged; no unit contradicted.

## Change 4
File: BW2-choosing-the-model-and-the-effort.md, §5, figure caption (F18)
Current:
````
The method names Opus 5.5 as the writer (case file §2); the writer of each draft is not recorded.
````
Replacement:
````
The method names Opus 5.5 as the writer (case file §2), and case file §5 records it as the writer of every draft.
````
Result: PASS. Figure caption; the fact is now in the unit's text (Change 3), so the figure adds no fact. Case file §2 (line 23) and §5 (line 152). JSON string stays valid (no quotation mark added).
Syllabus: no conflict: F18; no brief changed.

## Change 5
File: BW2-choosing-the-model-and-the-effort.md, Deliverable Part 1, row 2 (Extraction to a table), last column (F18)
Current:
````
Totals of 58 errors, 237 should-fix and 303 minor; no model recorded for compiling them |
````
Replacement:
````
Totals of 58 errors, 237 should-fix and 303 minor; no model recorded for compiling them. The history courses' curated bibliographies were extracted by Sonnet 5.5 agents, one per unit group (§2) |
````
Result: PASS. Case file §2 (line 150), labelled Extraction: the curated bibliographies of the 137 history reports were made by Sonnet 5.5 agents, one per unit group. 'no model recorded for compiling them' stays true of the §5 totals.
Syllabus: no conflict: F18 names extraction; no brief changed; no unit contradicted.

## Change 6
File: BW2-choosing-the-model-and-the-effort.md, Deliverable Part 1, row 4 (A long first draft), last column (F18)
Current:
````
| Opus 5.5 writes (§2); the effort used is not recorded |
````
Replacement:
````
| Opus 5.5 writes (§2) and wrote all 36 fresh-checked drafts (§5); unit-writing chats of 28 Oct to 2 Nov 2026: 14 of 15 on Opus 5.5, 1 switched (§8); the first history course's 78 reports: 55 by Fable 5.1, 23 by Opus 5.5 (§2); the effort used is recorded in none of 53 chats reviewed (§2, §9) |
````
Result: PASS. §5 (line 152): all 36 by Opus 5.5. §8 (line 148): unit writing 15 chats, Opus 5.5 14, switched 1, over the 53 chats of 28 Oct to 2 Nov 2026. §2 (line 244): first history course 55 Fable 5.1, 23 Opus 5.5. §2 (line 151) and §9 (line 246): effort recorded in none of 53.
Syllabus: no conflict: F18 names the writing model and effort; no brief changed.

## Change 7
File: BW2-choosing-the-model-and-the-effort.md, Deliverable Part 1, row 7 (Deep research), last column (F18)
Current:
````
| The agents' model is not recorded.
````
Replacement:
````
| The agents were Fable 5.1 research agents, on 27 Oct 2026 (§3).
````
Result: PASS. Case file §3 (line 153): the research report was written on 27 Oct 2026 across five tracks by Fable 5.1 research agents. The rest of the cell is unchanged and reads on.
Syllabus: no conflict: F18 names the research agents' model; no brief changed.

## Change 8
File: BW2-choosing-the-model-and-the-effort.md, Deliverable Part 1, row 8 (A code change), last column (F18)
Current:
````
| No model recorded for code changes |
````
Replacement:
````
| No model recorded for code changes alone; infrastructure chats (build, repository, publishing, method and skill files) of 28 Oct to 2 Nov 2026: 15, of which 5 on Opus 5.5, 8 on Fable 5.1, 2 switched; none of the 53 on Sonnet 5.5 or Haiku 5.5 (§8) |
````
Result: PASS. Case file §8 (line 148): infrastructure (build, repository, publishing, method and skill files) 15, Opus 5.5 5, Fable 5.1 8, switched 2; none of 53 on Sonnet 5.5 or Haiku 5.5. 'the 53' points back to row 4's '53 chats reviewed' (Change 6).
Syllabus: no conflict: F18 names code changes; no brief changed.

## Change 9
File: BW2-choosing-the-model-and-the-effort.md, Deliverable Part 1, row 9 (An audit against sources), last column (F18)
Current:
````
| Fable 5.1 audits (§2); Audit 2:
````
Replacement:
````
| Fable 5.1 audits (§2); Audits 1 and 2 ran on Fable 5.1, the public marketing course's four audits on Fable 5.2 (14–15 Nov 2026), and no audit of the private courses or the UX course after Audit 2 (§4); Audit 2:
````
Result: PASS. Case file §4 (line 154): Audits 1 and 2 on Fable 5.1 (28 and 29 Oct 2026); the public marketing course's four audits on Fable 5.2 (14–15 Nov 2026); no audit of the private courses or the UX course after Audit 2. The terms are the case file's own (§1, line 10 and line 141). 'ran' is understood in the last clause; reads in place.
Syllabus: no conflict: F18 names audits after Fable 5.2's release; no brief changed.

## Change 10
File: BW2-choosing-the-model-and-the-effort.md, Deliverable Part 1, row 10 (A plan or spec), last column (F18)
Current:
````
| No model recorded for syllabus work |
````
Replacement:
````
| Syllabus design chats of 28 Oct to 2 Nov 2026: 2, both Fable 5.1 (§8); the UX syllabus review on Fable 5.1 (3 Nov 2026), the two public courses created on Fable 5.2 (11–12 Nov 2026), and syllabus chats on Fable from 15 Nov 2026 (§2) |
````
Result: PASS. §8 (line 148): syllabus design 2, Fable 5.1 2. §2 (line 149): UX syllabus review on Fable 5.1 (3 Nov 2026), the two public courses created on Fable 5.2 (11–12 Nov 2026), and from 15 Nov 2026 course design and syllabus chats run on Fable (a rule of the method, stated as such by the case file; the replacement's wording is a fair reading).
Syllabus: no conflict: F18 names syllabus work; the row's routing (Opus 5.5) stays this unit's proposal under the Deliverable's opening (line 360); no brief changed.

## Change 11
File: BW2-choosing-the-model-and-the-effort.md, Deliverable Part 1, Sources for Part 1 (F18)
Current:
````
The case file holds no record of cost per unit, of the plan used, or of which model ran triage, extraction, summaries, searching, code or syllabus work (§9; §7 note).
````
Replacement:
````
The case file holds no record of cost per unit or of the plan used (§9; §7 note), or of which model ran triage, summaries or searching apart from writing; it records the models of extraction and syllabus work (§2, §8), of infrastructure chats (§8), of the research agents (§3), of the audits (§4) and of the 36 drafts' writer (§5).
````
Result: PASS. Matches the cells as changed: models now recorded for extraction (§2, line 150), syllabus (§2 line 149, §8 line 148), infrastructure (§8), research agents (§3), audits (§4), the 36 drafts' writer (§5); still none for triage, summaries or searching apart from writing; cost and plan in §9 (lines 245, 247) and the §7 note (line 114).
Syllabus: no conflict: F18; no brief changed.

## Change 12
File: BW2-choosing-the-model-and-the-effort.md, Unsure list, item 10 (F18)
Current:
````
that the writer of every one of those drafts was Opus 5.5 rests on case file §2's general statement, not on a per-unit record.
````
Replacement:
````
that the writer of every one of those drafts was Opus 5.5 rests on case file §5, which records it from the course index's unit tables (line added 17 Nov 2026).
````
Result: PASS. Case file §5 (line 152) records it from the course index's unit tables; the line sits under the header of lines added 17 Nov 2026 (line 140).
Syllabus: no conflict: F18 / F103; no brief changed.

## Change 13
File: BW4-context-engineering.md, §5, The case (F28)
Current:
````
Both are outputs produced from one source by a step, never edited in place. One project, an anecdote;
````
Replacement:
````
Both are outputs produced from one source by a step, never edited in place. Its mirrors still lagged (§7): two units filed on 29 Oct 2026 were not in the Project's knowledge list seen the same day, although the filing procedure required the re-upload; after two units were filed in one chat (12–13 Nov 2026), ten Project copies were stale and were re-uploaded from the repository by a separate correction row the next day; a prompt corrected in the repository after a publish stayed uncorrected on the site's Backlog page until the next publish; and in five filing sessions the site was published as the claude.ai artifact but not deployed to GitHub Pages until a later row. The method's rule of 15 Nov 2026: each chat that works a row rewrites the Project copies of the backlog and changelog in full, and units are not mirrored (§7). One project, an anecdote;
````
Result: PASS. Case file §7: line 177 (29 Oct units missing from the knowledge list the same day, though the re-upload was required), line 179 (ten copies stale after two units filed in one chat, 12–13 Nov 2026, re-uploaded by a separate correction row the next day), line 180 (prompt corrected after a publish stayed uncorrected on the Backlog page until the next publish), line 181 (five filing sessions published as the artifact, not deployed to GitHub Pages; later rows deployed it), line 182 (the mirror rule of 15 Nov 2026). 'Its mirrors' reads as the one source's mirrors; acceptable in place.
Syllabus: no conflict: F28 names BW4 §5's case example of mirror lag; no brief changed; no unit contradicted.

## Change 14
File: BW4-context-engineering.md, §7, opening paragraph (F26)
Current:
````
The case file names two of them: project instructions that carried procedures and paraphrased the method file, and private terms reaching a public build (§7). It does not list the other fifteen, so this unit works through the two it names.
````
Replacement:
````
The case file lists all seventeen, each with its layer, its fix and its severity, and gives their status on 16 Nov 2026: 12 still applied, 2 were done and 3 no longer applied (§7). This section works through two of them: project instructions that carried procedures and paraphrased the method file, and private terms reaching a public build (§7).
````
Result: FAIL. 'each with its layer, its fix and its severity' is not correct for all seventeen: F6 (line 164) has 'no fix' and no severity. The status counts are right (line 176: 12 still apply, 2 done, 3 no longer apply). See New 2.
Syllabus: F26 names BW4 §7 and the seventeen findings; the BW4 brief ('its seventeen findings') is better met, not changed.

## Change 15
File: BW4-context-engineering.md, §7, Private terms reaching a public build (F26)
Current:
````
The case file does not say how the finding was found or fixed.
````
Replacement:
````
The case file does not say how the finding was found. The audit's fix was a build-time redaction list kept outside both repositories, an erratum, a verify-script check and the owner's decision on the public repository's history; on 16 Nov 2026 a terms list and a checker existed, and the erratum, the scan's scope and the decision were not shown (§7).
````
Result: PASS. Case file §7, F15 (line 173): fix a build-time redaction list kept outside both repositories, an erratum, a verify-script check and the owner's decision on the public repository's history; status 16 Nov 2026 residual: a terms list and a checker exist; the erratum, the scan's scope and the decision not shown. Stated as the audit's fix, so it does not contradict line 209 (the list now sits in the private repository).
Syllabus: no conflict: F26; no brief changed.

## Change 16
File: BW4-context-engineering.md, Deliverable Part 1, What goes where, Account-wide instructions, Holds now (F26)
Current:
````
| The owner's register and format habits, with no project rule in them | [NOT IN CASE FILE] |
````
Replacement:
````
| The owner's register and format habits, with no project rule in them | At the structure audit, three preferences that collided with the Project's work: a format rule, a concision rule and a rule against volunteering next steps; no longer applying on 16 Nov 2026 (case file §7, audit F5) |
````
Result: FAIL. Case file §7, F5 (line 163) gives the status as 'no longer applies (reading)'; the replacement drops the qualifier and states it as fact, where Change 28 keeps it ('by the fix list's reading'). Otherwise correct. See New 3.
Syllabus: F26 names the Holds now column; no brief changed.

## Change 17
File: BW4-context-engineering.md, Deliverable Part 1, What goes where, Project instructions, Holds now (F26)
Current:
````
| Carried procedures and paraphrased the method file, at the structure audit (case file §7) |
````
Replacement:
````
| Carried procedures and paraphrased the method file, at 675 words, at the structure audit; 862 words, the finding still applying, on 16 Nov 2026 (case file §7, audit F7) |
````
Result: PASS. Case file §7, F7 (line 165): 675 words at the audit; still applies, grown to 862 words on 16 Nov 2026.
Syllabus: no conflict: F26; no brief changed.

## Change 18
File: BW4-context-engineering.md, Deliverable Part 1, What goes where, Project knowledge, Holds now (F26)
Current:
````
[NOT IN CASE FILE: files, size, retrieval mode]
````
Replacement:
````
At the structure audit, 33 files, 907,260 characters (about 363,000 tokens), mostly files no chat needed whole, and a second copy of the project instructions; whether it ran in retrieval mode was not known; filed units removed on 15 Nov 2026 (case file §7, audit F1, F2)
````
Result: PASS. Case file §7: line 144 (33 files, 907,260 characters, about 363,000 tokens; retrieval mode not known), F1 (line 159: mostly files no chat needed whole; filed units removed 15 Nov 2026), F2 (line 160: the instructions also uploaded as a knowledge file). Dated to the structure audit.
Syllabus: no conflict: F26 (and F27) name the knowledge cell; no brief changed.

## Change 19
File: BW4-context-engineering.md, Deliverable Part 1, What goes where, Memory, Holds now (F26)
Current:
````
[NOT IN CASE FILE: the record does not say whether memory was on, §9]
````
Replacement:
````
Account memory flowing into the Project beside its own memory store, on the setup as of 28 Oct 2026; the memory tool called in 6 of 53 chats reviewed; the setting not visible in the records on 16 Nov 2026 (case file §7, audit F13; §9)
````
Result: PASS. Case file §7, line 143 (account memory flowed into the Project beside its own memory store on the setup as of 28 Oct 2026; 6 of 53 chats show the memory tool called; setting not visible 16 Nov 2026), F13 (line 171); §9 (line 255).
Syllabus: no conflict: F26 (and F27) name the memory cell; no brief changed.

## Change 20
File: BW4-context-engineering.md, Deliverable Part 1, What goes where, Skills, Holds now (F26 (F62))
Current:
````
| One per repeated procedure: writing a unit, checking a unit, filing a unit | [NOT IN CASE FILE] |
````
Replacement:
````
| One per repeated procedure: writing a unit, checking a unit, filing a unit | Four skills kept in the repository, for writing a unit, running a fresh check or audit, filing a unit and starting a course, installed on the owner's account by hand (case file §7) |
````
Result: PASS. Case file §7, Skills (line 200): four skills in the repository, for writing a unit, running a fresh check or audit, filing a unit and starting a course, installed on the owner's account by hand.
Syllabus: no conflict: F26 names the Holds now column (F62, F27 the skills fact); no brief changed; BW8 not in the packet, so not checked against it.

## Change 21
File: BW4-context-engineering.md, Deliverable Part 1, What goes where, Connectors, Holds now (F26)
Current:
````
| Only those a procedure uses | [NOT IN CASE FILE] |
````
Replacement:
````
| Only those a procedure uses | Eight connected and none used by a Project procedure, at the structure audit; still so on 16 Nov 2026, by the fix list's reading (case file §7, audit F14) |
````
Result: PASS. Case file §7, F14 (line 172): eight connected, no Project procedure used one; still applies (reading), stated as 'by the fix list's reading'.
Syllabus: no conflict: F26; no brief changed.

## Change 22
File: BW4-context-engineering.md, Deliverable Part 1, What goes where, Scheduled tasks, Holds now (F26 (F64))
Current:
````
| The mechanical steps of the rot check (Part 2), once BW8 is reached | [NOT IN CASE FILE] |
````
Replacement:
````
| The mechanical steps of the rot check (Part 2), once BW8 is reached | None, on the setup as of 28 Oct 2026 or in the records of 16 Nov 2026; the weekly rot check the audit proposed was not created (case file §7, audit F16) |
````
Result: PASS. Case file §7, Scheduled tasks (line 202) and F16 (line 174): none on the setup as of 28 Oct 2026 or in the records of 16 Nov 2026; the weekly rot check B4 (the audit) proposed was not created.
Syllabus: no conflict: F26 (F64); no brief changed; BW8, BW9 not in the packet.

## Change 23
File: BW4-context-engineering.md, Deliverable Part 2, opening paragraph (F63)
Current:
````
they assume the structure in Part 1.
````
Replacement:
````
they assume the structure in Part 1. On Academy no file named `INDEX.md` or `INSTRUCTIONS.md` appears in the records; their equivalents are `docs/courses-index.md` and `docs/project-instructions.md`, a copy of the Project's instructions field (case file §1).
````
Result: PASS. Case file §1, Layout names (line 201): no INDEX.md or INSTRUCTIONS.md in the records; equivalents docs/courses-index.md and docs/project-instructions.md (a copy of the Project's instructions field).
Syllabus: no conflict: F63 names BW4 Deliverable Part 2 and asks how the names map; no brief changed.

## Change 24
File: BW4-context-engineering.md, Deliverable Part 2, step 1, Result (F26)
Current:
````
Result: [NOT IN CASE FILE: no run recorded].
````
Replacement:
````
Result: no run recorded (case file §7: the weekly rot check the structure audit proposed was not created). The audit's finding of this kind, F7, still applied on 16 Nov 2026, the instructions having grown from 675 to 862 words (§7).
````
Result: PASS. Case file §7, line 202 (the weekly rot check not created; no rot-check run in the records) and F7 (line 165).
Syllabus: no conflict: F26 names the Part 2 results; no brief changed.

## Change 25
File: BW4-context-engineering.md, Deliverable Part 2, step 2, Result (F26)
Current:
````
no file marked superseded is outside `archive/`. Result: [NOT IN CASE FILE].
````
Replacement:
````
no file marked superseded is outside `archive/`. Result: no run recorded (case file §7). The audit's F9, stale files and lines still read as current (an old hand-off note, retired page blocks rendered on the site, a wrong due date, a contradictory lane heading, two references to a retired build script), still applied on 16 Nov 2026, one of its five parts done (§7).
````
Result: PASS. Case file §7, F9 (line 167): the five parts as listed; still applies, one of five parts done.
Syllabus: no conflict: F26; no brief changed.

## Change 26
File: BW4-context-engineering.md, Deliverable Part 2, step 3, Result (F26)
Current:
````
Pass if they match. Result: [NOT IN CASE FILE].
````
Replacement:
````
Pass if they match. Result: no run recorded (case file §7). The audit's F3, a knowledge copy that already lagged the repository, was done by 16 Nov 2026 (units are no longer mirrored, and every chat rewrites the copies it changes); its F11, a theme reaching the build through a hand copy that no check compared, still applied, by the fix list's reading (§7).
````
Result: PASS. Case file §7, F3 (line 161: done; units no longer mirrored, every chat rewrites the copies it changes) and F11 (line 169: still applies, reading, kept as 'by the fix list's reading').
Syllabus: no conflict: F26; no brief changed.

## Change 27
File: BW4-context-engineering.md, Deliverable Part 2, step 4, Result (F26)
Current:
````
stated in one file and pointed to everywhere else. Result: [NOT IN CASE FILE].
````
Replacement:
````
stated in one file and pointed to everywhere else. Result: no run recorded (case file §7). The audit's F8, four prose copies of the list of units that search, in three versions, still applied on 16 Nov 2026 (§7).
````
Result: PASS. Case file §7, F8 (line 166): four prose copies of the list of units that search, in three versions; still applies.
Syllabus: no conflict: F26; no brief changed.

## Change 28
File: BW4-context-engineering.md, Deliverable Part 2, step 5, Result (F26)
Current:
````
is named there as an exception. Result: [NOT IN CASE FILE].
````
Replacement:
````
is named there as an exception. Result: no run recorded (case file §7). The audit's F5, three account preferences (a format rule, a concision rule and a rule against volunteering next steps) colliding with the Project's work, no longer applied on 16 Nov 2026, by the fix list's reading (§7).
````
Result: PASS. Case file §7, F5 (line 163): three preferences (format, concision, against volunteering next steps); no longer applies (reading), kept as 'by the fix list's reading'.
Syllabus: no conflict: F26; no brief changed.

## Change 29
File: BW4-context-engineering.md, Deliverable Part 2, step 6, Result (F26)
Current:
````
the second named audit finding (case file §7). Result: [NOT IN CASE FILE].
````
Replacement:
````
the second named audit finding (case file §7). Result: no run recorded as a rot check; since 11–12 Nov 2026 a script fails the build on a private term in a public course, and the private-terms check is one of the scripts that must pass before a publish (case file §7, §1). The audit's F15 still applied on 16 Nov 2026 as a residual: a terms list and a checker existed; the erratum, the scan's scope and the decision on the public repository's history were not shown (§7).
````
Result: PASS. Case file §7, line 199 (the script failing the build on a private term in a public course, added 11–12 Nov 2026), §1 line 196 (the private-terms check among the scripts that must pass before a publish), F15 (line 173: residual, as stated).
Syllabus: no conflict: F26; no brief changed; BW4's own proposal (list kept outside the repository) left as its proposal.

## New 1
File: BW1-mental-model.md, Deliverable Part 3, diagnosis table, row "A large project answers from the wrong file", Academy case instance (F4)
Current:
````
| No instance in the case file | BW4 |
````
Replacement:
````
| No instance in the case file: the Project's knowledge held 33 files, 907,260 characters (about 363,000 tokens), and whether the Project ran in retrieval mode was not known (§7); the record does not say whether any failure was traced to retrieval mode (§9) | BW4 |
````
Result: PASS. Replaces Change 1. The referent is the Project, as in case file §7 (line 144: 'the Project's knowledge held 33 files'; 'whether the Project ran in retrieval mode ... was not known'); §9 (line 245).
Syllabus: no conflict: F4, row 11 of BW1's case diagnosis table; no brief changed.

## New 2
File: BW4-context-engineering.md, §7, opening paragraph (F26)
Current:
````
The case file names two of them: project instructions that carried procedures and paraphrased the method file, and private terms reaching a public build (§7). It does not list the other fifteen, so this unit works through the two it names.
````
Replacement:
````
The case file lists all seventeen, each with its layer and, for sixteen of them, its fix and its severity, and gives their status on 16 Nov 2026: 12 still applied, 2 were done and 3 no longer applied (§7). This section works through two of them: project instructions that carried procedures and paraphrased the method file, and private terms reaching a public build (§7).
````
Result: PASS. Replaces Change 14. Case file §7, F1 to F17 (lines 159 to 175: F6 alone has no fix and no severity) and status line 176.
Syllabus: no conflict: F26; no brief changed.

## New 3
File: BW4-context-engineering.md, Deliverable Part 1, What goes where, Account-wide instructions, Holds now (F26)
Current:
````
| The owner's register and format habits, with no project rule in them | [NOT IN CASE FILE] |
````
Replacement:
````
| The owner's register and format habits, with no project rule in them | At the structure audit, three preferences that collided with the Project's work: a format rule, a concision rule and a rule against volunteering next steps; no longer applying on 16 Nov 2026, by the fix list's reading (case file §7, audit F5) |
````
Result: PASS. Replaces Change 16. Case file §7, F5 (line 163): status 'no longer applies (reading)'; the qualifier kept, as in Change 28.
Syllabus: no conflict: F26; no brief changed.
