# S-AC0 · `docs/athlete-career-prompts.md`: every line changed

Registrar, claude-opus-5-5, 23 Nov 2026. The file is the design file `inbox/athlete-career/docs/athlete-career-prompts.md` (sections 1 to 5), then "---", the heading "## Rows W-AC1 to W-DD-AC3 · write one unit", a note of what was replaced, the slots line, the template, and "### This row in particular" with section 3's eighteen paragraphs word for word in the four-column form `doc_parts()` reads. The template is the code block of `docs/supply-chain-execution-prompts.md` under "Rows W-SCE1 to W-DD-SCE2" as it stands in the repo today. Wherever a source line carries the owner's first name, this file and the prompts document write "the owner" (sentence-initial "The owner"): no repo file written by this row names the owner. That substitution is itself a change and is listed below where it falls.

## A. The design part (sections 1 to 5 and the lines above them)

### A1. design @@ -6 +6 @@

- **Was:** The writing template is not rewritten here. The repo holds a working one for a course of the same build, in `docs/supply-chain-execution-prompts.md` ("Rows W-SCE1 to W-DD-SCE2 · write one unit"), already corrected to the kit by S-SCE0 and W-SCE2. S-AC0 copies it as it stands on the day and replaces its course-specific parts (the course's name, code, slug and paths; Part 8 with Part 9; the two closing sections) with sections 1 to 5 below. Everything else in the template (the thin chat's rules, the agents and their order, the scripts, the checkpoint commits, the quality review, the close) stays as the repo has it.
- **Now:** The writing template is not rewritten here. The repo holds a working one for a course of the same build, in `docs/supply-chain-execution-prompts.md` ("Rows W-SCE1 to W-DD-SCE2 · write one unit"), already corrected to the kit by S-SCE0 and W-SCE2. S-AC0 copies it as it stands on the day and replaces its course-specific parts (the course's name, code, slug and paths; Part 8 with Part 11; the two closing sections) with sections 1 to 5 below. Everything else in the template (the thin chat's rules, the agents and their order, the scripts, the checkpoint commits, the quality review, the close) stays as the repo has it.

### A2. design @@ -41 +41 @@

- **Was:** It also runs the unit against Part 9 line by line and reads it as the reader in the preamble would.
- **Now:** It also runs the unit against Part 11 line by line and reads it as the reader in the preamble would.

### A3. design @@ -68 +68 @@

- **Owner's name only:** the design's line names the owner where this one says "the owner"; nothing else changed:
  ## 4 · The carry-forward rule (the owner, standing)

### A4. design @@ -72 +72 @@

- **Owner's name only:** the design's line names the owner where this one says "the owner"; nothing else changed:
  1. **What counts.** Any error, mistake, contradiction, unverified claim, missing source or unmet need, found before, during or after a unit is written: by the writer, the fresh checker, the applier, the filer, the corrections checker, a script, or the owner.

### A5. design @@ -87 +87 @@

- **Owner's name only:** the design's line names the owner where this one says "the owner"; nothing else changed:
  Set by the owner on 21 Nov 2026 (22:43). It replaces the six-session plan of P-AC12.

### A6. design @@ -114 +114 @@

- **Owner's name only:** the design's line names the owner where this one says "the owner"; nothing else changed:
  5. **No gate rows.** A point where the owner reads before more is written sits on a bundle boundary; his starting the next chat is the go. Nothing is his to close by hand. The natural place to read is after bundle 1, when the grade key, the roles declaration, the rules register and the minor's protocol exist; after bundle 2 the first sponsor units do.

### A7. design @@ -116 +116 @@

- **Owner's name only:** the design's line names the owner where this one says "the owner"; nothing else changed:
  7. **Replies.** A chat gives one reply. It ends with the starter in a code block, not with a long prompt. A task is left for the owner only where no agent can do it. A proposal is worked in the next row unless he vetoes it; a flag that would change a brief is the one thing that stays proposed, and it is listed in the reply.

### A8. design @@ -117,0 +118 @@

- **Owner's name only:** the design's line names the owner where this one says "the owner"; nothing else changed:
  


8 hunks. Nothing else in sections 1 to 5 differs from the design file (checked with `difflib`).

## B. The template (the code block under the new heading), against the Execution template

Each named replacement made by the generator, in template order: where it is, the text it replaced and the text now there.

### B1. template, opening paragraph (clone rule, section 5 rule 1)

- **Was:**

```
Right after cloning, run `python3 kit/land.py start <this row>`
```

- **Now:**

```
First, run `python3 kit/land.py start <this row>`
```

### B2. template, opening paragraph (course, paths, Part)

- **Was:**

```
of the public course Supply Chain Execution for Product Teams (`courses/supply-chain-execution/course.toml`: data `courses/supply-chain-execution/notes/`, vault `courses/supply-chain-execution/`, `docs/sourcing-standard.md` Parts 1 and 8; search {SEARCH})
```

- **Now:**

```
of the public course Managing an Athlete's Career (`courses/athlete-career/course.toml`: data `courses/athlete-career/notes/`, vault `courses/athlete-career/`, `docs/sourcing-standard.md` Parts 1 and 11; search {SEARCH})
```

### B3. template, opening paragraph (reply ends with the starter, section 5 rule 7)

- **Was:**

```
close the row and end with the next row's prompt.
```

- **Now:**

```
close the row and end the reply with the course's starter line.
```

### B4. template, carry-forward rule (section 4, word for word)

- **Was:**

```
**The carry-forward rule (the owner, standing; `docs/supply-chain-execution-prompts.md` §4, `docs/method.md` §9).** Nothing found goes unrecorded or waits for a later audit. It applies to every row of this course, the last included.

1. **What counts.** Any error, mistake, contradiction, unverified claim, missing source or unmet need, found before, during or after a unit is written: by the writer, the fresh checker, the applier, the filer, the corrections checker, a script, or the owner.
2. **About a unit already filed.** It goes into the next row's prompt as a correction, with the unit, the passage, what is wrong and the source. The next chat fixes it first, before it writes its own unit: each change is checked by a fresh agent against its source and the syllabus, applied as an exact replacement, and recorded.
3. **About a unit not yet written.** It becomes a flag in `syllabus-flags.md` naming every unit it affects, and it is printed in each of those units' prompts as a guideline for the writer. A flag that would change a brief is proposed, never applied by the chat that raised it.
4. **About the unit being written.** It is fixed in the same chat before filing. What cannot be fixed (a source that will not open) is cut or marked unverified in the unit, and carried as in 2.
5. **Every delivery ends with the next prompt.** The reply of every row closes with the prompt for the next unit in a code block, as `kit/next_prompt.py` prints it, already holding: every correction still open on a filed unit, every open flag that names the next unit, and any guideline of this prompt that the row showed needs updating, with the update made. A row that finds a rule of the template wrong or unworkable corrects it in `docs/supply-chain-execution-prompts.md`, says what it changed, and the next prompt carries the corrected text.
6. **Nothing is dropped silently.** A correction or flag leaves the next prompt only when it is resolved, with the row and the report that resolved it written beside it.
7. **The last row** (W-DD-SCE2) delivers a closing corrections prompt in place of a next unit's, listing every correction and flag still open.
```

- **Now:**

```
**The carry-forward rule (the owner, standing; `docs/athlete-career-prompts.md` §4, `docs/method.md` §9).** `docs/method.md` §9, with this course's names. It holds for every row, the last included.

1. **What counts.** Any error, mistake, contradiction, unverified claim, missing source or unmet need, found before, during or after a unit is written: by the writer, the fresh checker, the applier, the filer, the corrections checker, a script, or the owner.
2. **About an AC unit already filed.** It goes into the next row's prompt as a correction, with the unit, the passage, what is wrong and the source. The next chat fixes it first: each change is checked by a fresh agent against its source and the syllabus, applied as an exact replacement, and recorded.
3. **About an AC unit not yet written.** It becomes a flag in `courses/athlete-career/notes/syllabus-flags.md` naming every unit it affects, printed in each of those units' prompts. A flag that would change a brief is proposed, never applied by the chat that raised it.
4. **About the unit being written.** Fixed in the same chat before filing. What cannot be fixed is cut or marked unverified, and carried as in 2.
5. **Every row hands on to the next through the repo.** The next row's prompt, as `kit/next_prompt.py` prints it, holds every open correction, every open flag that names the next unit, and any rule of this document the row showed to be wrong, corrected here. Inside a bundle the chat runs it; at the end of a chat the reply ends with the starter (section 5), which prints it.
6. **Nothing is dropped silently.** A correction or flag leaves the next prompt only when resolved, with the row and the report that resolved it beside it.
7. **The last row** (W-DD-AC3) is followed, in the same chat, by the closing corrections (section 5, rule 6). A closing prompt is delivered only if something remains open, with the reason.

Two additions for this course:

8. **Sport Psychology's register.** A conflict between this course's case and `courses/sport-psychology/notes/case-facts.md` is a correction to this course. A fault found in a filed Sport Psychology unit goes under Corrections in `docs/BACKLOG.md`.
9. **Portugal.** A Portuguese text found changed since an earlier unit cited it is a correction to that unit.
```

### B5. template step 1b (audits path)

- **Was:**

```
its report saved as `audits/supply-chain-execution/corrections-<date>-<codes>.md`
```

- **Now:**

```
its report saved as `audits/athlete-career/corrections-<date>-<codes>.md`
```

### B6. template step 2 (Part, paths)

- **Was:**

```
`docs/sourcing-standard.md` Parts 1 and 8; the figure kinds; `courses/supply-chain-execution/notes/case-facts.md`; `courses/supply-chain-execution/notes/bibliography.md`
```

- **Now:**

```
`docs/sourcing-standard.md` Parts 1 and 11; the figure kinds; `courses/athlete-career/notes/case-facts.md`; `courses/athlete-career/notes/bibliography.md`
```

### B7. template step 3 (writer rules, section 1)

- **Was:**

```
- The writer rules of this course (`docs/supply-chain-execution-prompts.md` §1). The writer is one fresh Opus 5.5 agent with its packet and nothing else.
1. **Open before citing.** Every reference is found by a search and read at its publisher's page, its DOI address or the issuing body's own page before it carries a claim. The seed bibliography says only that an entry exists.
2. **Source log.** `out/sources.md`: one row per reference with the address opened, what was read (abstract, reprint or full text), the date, and the claims it carries. A reference that could not be opened is listed as not opened and carries nothing. A title is the article's own title, never a slug; a figure is cited to the paper that reports it, not to one that repeats it; each Sources entry is checked against the publisher's record before hand-in.
3. **Fewer, better.** Prefer one source read in full to three read in abstract. Do not cite to decorate. If a section's support is one textbook's account, grade it practice and say so.
4. **Grade every claim** by SCE1's key. From SCE2 on, the key arrives in the packet inside SCE1.
5. **Vendors.** Assess, rank, compare or recommend no real vendor, and map no real vendor's product line. Name a real vendor only to attribute a dated public statement to it, graded vendor-reported, or as an entry in a dated list from a named analyst report or an audited filing, every vendor on the list alike. Worked product examples use Halvern Systems, Varnby Software and Kestrow, from the case register, labelled fictional. Never say or hint which real company a fictional one resembles.
6. **Analyst reports.** Say how each was read. If only the abstract could be opened, the unit states only what the abstract states.
7. **No private figures.** No price, revenue, margin or win rate of a private company unless it published it. Where a brief asks for a cost line with no public figure, write "no public figure".
8. **The case** comes from `case-facts.md` only; invented facts go in the notes.
9. **Scope.** No AI features. No interview framing. No craft method taught. Nothing about the Project's owner, his employer, his role or his work.
10. **The two closing sections** before the deliverable: "On a site visit" and "Self-check", every answer drawn from the unit's sourced text.
11. **Flags and corrections.** A contradiction with a filed unit or a brief, a mistake noticed in a filed unit, or a need the syllabus does not meet, is written to `out/notes.md` (a contradiction or a mistake under **Contradictions**, a mistake with the quoted passage, what is wrong, the source and the exact replacement; a need under **Needs**), naming every unit it affects and with a proposed change, so that the filer writes it into `syllabus-flags.md` in that file's form. It is carried by the carry-forward rule above. The writer never rewords a brief.
12. **Hand-in.** The unit, `out/unit.md` (front matter, the unit, the deliverable, Sources); `out/sources.md`; `out/notes.md` with three lists, each item naming the unit codes it touches, an empty list written as "none": **Case facts** (rule 8), **Contradictions** and **Needs** (rule 11); the figures rendered; `out/unsure.md`, up to ten claims it is unsure of, closing with the `Object:` line; a reply of six lines at most (its model, the files it wrote, the counts of its lists, the number of references opened and not opened). `out/stats.json` is not the writer's: the chat writes it from these files with `python3 kit/thin.py stats`.
```

- **Now:**

```
- The writer rules of this course (`docs/athlete-career-prompts.md` §1). The writer is one fresh Opus 5.5 agent with its packet and nothing else.
1. **Open before citing.** Every reference is found by a search and read at its publisher's page, its DOI address or the issuing body's own page before it carries a claim. The seed bibliography says only that an entry exists.
2. **Source log.** `out/sources.md`: one row per reference with the address opened, what was read (abstract, summary or full text; for a law, the articles read), the date, and the claims it carries. A reference that could not be opened is listed as not opened and carries nothing. A title is the work's own title, never a slug; a figure is cited to the source that reports it, not to one that repeats it; each Sources entry is checked against the publisher's or issuing body's record before hand-in.
3. **Fewer, better.** Prefer one source read in full to three read in abstract. Do not cite to decorate. If a section's support is one textbook's account, grade it practice and say so.
4. **Reputable and verifiable only.** A law firm's note, a press report, a recruiting or agency site may lead you to a text; the text is what you read and cite. An interested party's page is evidence of what that party says, offers or requires, never of how things are.
5. **Grade every claim** by AC1's key. From AC2 on, the key arrives in the packet inside AC1.
6. **Rules are never the reader's.** Each rule or law is its issuing body's text, with its sport or country and the date read, followed by the question the reader puts to their own body.
7. **Portugal.** Where the brief has "In Portugal", read each text at the Diário da República or the body's own page, cite it in Portuguese with its article, give its sense in English as your translation, and label the section one country's worked example. The private-terms check fails on two Portuguese city names (the plain lines of `kit/private-terms.txt`): a source whose title or address holds one is cited without that word where the record allows, and otherwise raised under Needs, never reworded around.
8. **Money.** No fee, rate, commission or typical deal value unless a named source published it, with whose figure, sample, year and currency. Otherwise write "no public figure".
9. **Not advice.** The line once near the top. Legal and tax points are questions with the body or professional to ask. Nothing about investing.
10. **Minors.** Nothing on AC4's refusal list is proposed. From AC5 on, "If the athlete is under 18" closes the body before the Self-check and agrees with AC4.
11. **The roles.** Wherever the coach or the coach's business has a stake in the decision described, name the conflict and say who else decides. Never present the reader's good intentions, or working unpaid, as settling it.
12. **Real people and companies.** No real athlete, coach or family as an example of hardship or failure beyond what they published themselves or a court or inquiry states. No real agent, agency or sponsor assessed, ranked or recommended. Nothing about the Project's owner, his sport, his club, his athletes or his business.
13. **The case** comes from `case-facts.md` only, which carries Sport Psychology's facts; invented facts go in the notes. Sara's and Dani's referrals are respected in anything planned for them.
14. **The closing sections** before the deliverable: "Check before you act", then from AC5 on "If the athlete is under 18", then "Self-check", every answer drawn from the unit's sourced text.
15. **Flags and corrections.** A contradiction with a filed unit or a brief, a mistake noticed in a filed unit, or a need the syllabus does not meet, is written to `out/notes.md` (a contradiction or a mistake under **Contradictions**, a mistake with the quoted passage, what is wrong, the source and the exact replacement; a need under **Needs**), naming every unit it affects and with a proposed change. It is carried by the carry-forward rule above. The writer never rewords a brief.
16. **Hand-in.** As the template's hand-in rule: `out/unit.md`, `out/sources.md`, `out/notes.md` with its three lists (**Case facts**, **Contradictions**, **Needs**), the figures rendered, `out/unsure.md` closing with the `Object:` line, and a reply of six lines at most. The template's hand-in rule, which this rule names, in full: The unit, `out/unit.md` (front matter, the unit, the deliverable, Sources); `out/sources.md`; `out/notes.md` with three lists, each item naming the unit codes it touches, an empty list written as "none": **Case facts** (rule 13), **Contradictions** and **Needs** (rule 15); the figures rendered; `out/unsure.md`, up to ten claims it is unsure of, closing with the `Object:` line; a reply of six lines at most (its model, the files it wrote, the counts of its lists, the number of references opened and not opened). `out/stats.json` is not the writer's: the chat writes it from these files with `python3 kit/thin.py stats`.
```

### B8. template step 4 (checker passes, section 2)

- **Was:**

```
Beyond the skill's items it runs the seven passes of `docs/supply-chain-execution-prompts.md` §2 and reports each by name. One fresh Opus 5.5 agent that has not seen the unit written. It writes findings (error, should-fix, minor) and edits nothing. A reference that does not exist stops the row.
1. **References exist and match.** Every Sources entry against its publisher's or Crossref's record: authors, title, journal, year, volume, pages, DOI.
2. **Claims against sources.** Every cited claim opened and read against its source; "unverifiable" where the source will not open, never a pass.
3. **Grades.** Each grade against SCE1's key; a vendor's statement never carries more than vendor-reported; an abstract-only reading is said to be one.
4. **Vendors.** No real vendor assessed, ranked, compared, recommended or mapped; each real vendor named only as writer rule 5 allows; every list complete and alike; no private company's unpublished figure; no fictional vendor tied to a real one.
5. **The case.** Every case fact against `case-facts.md`; labelled fictional; never used as evidence.
6. **Scope and tone.** No AI features, no interview framing, no method teaching, nothing about the Project's owner or his employer; the preamble's tone rules; terms defined on first use.
7. **Deliverable and figures.** The deliverable against the brief's wording, built in full and then as a template; "On a site visit" and "Self-check" present and agreeing with the body; every figure's labels and numbers traced to the text.
It also runs the unit against Part 8 line by line and reads it as the reader in the preamble would.
```

- **Now:**

```
Beyond the skill's items it runs the seven passes of `docs/athlete-career-prompts.md` §2 and reports each by name. One fresh Opus 5.5 agent that has not seen the unit written, with live search. It writes findings (error, should-fix, minor) and edits nothing. A reference that does not exist stops the row.
1. **References exist and match.** Every Sources entry against its publisher's, Crossref's or its issuing body's record: authors, title, journal or publisher, year, volume, pages, DOI; for a law, its number, date and official-journal reference.
2. **Claims against sources.** Every cited claim opened and read against its source; samples and designs stated; an inference from famous athletes or large sponsorships to an unknown athlete labelled; "unverifiable" where the source will not open, never a pass.
3. **Grades.** Each grade against AC1's key; an interested party never graded research or data; an abstract-only reading said to be one.
4. **Rules and Portugal.** No rule or law stated as the reader's; each with its body, its sport or country and the date read; each "In Portugal" text read at its issuing page and fairly translated; no law firm's note or press report standing in for a text.
5. **Safety.** The not-advice line. Minors: nothing from the refusal list; "If the athlete is under 18" agrees with AC4. No supplement recommended. No real person in hardship beyond the rule; no real agent, agency or sponsor assessed. Nothing teaches getting around a rule. The roles conflict named where the coach or the coach's business has a stake. No money figure without source, sample, year and currency.
6. **The case, scope and tone.** Every case fact against `case-facts.md` and, through it, Sport Psychology's register; labelled fictional; never evidence. Nothing about the Project's owner. No coaching, psychology or audience-building method re-taught. The preamble's tone rules; terms defined on first use.
7. **Deliverable and figures.** The deliverable against the brief's wording, built in full on the named case and then as a template; the closing sections present and agreeing with the body; every figure's labels and numbers traced to the text.
It also runs the unit against Part 11 line by line and reads it as the reader in the preamble would.
```

### B9. template step 4 (origin of filed/)

- **Was:**

```
The packet holds the course's filed units (`filed/`, W-SCE2)
```

- **Now:**

```
The packet holds the course's filed units (`filed/`, from the Execution course's row W-SCE2)
```

### B10. template step 4 (audits path)

- **Was:**

```
saves the report as `audits/supply-chain-execution/fresh-check-{CODE}.md`
```

- **Now:**

```
saves the report as `audits/athlete-career/fresh-check-{CODE}.md`
```

### B11. template step 5 (origin)

- **Was:**

```
it works the report's could-not-verify list too (W-SCE2)
```

- **Now:**

```
it works the report's could-not-verify list too (from the Execution course's row W-SCE2)
```

### B12. template step 7 (path)

- **Was:**

```
Append every Contradiction and Need to `courses/supply-chain-execution/notes/syllabus-flags.md`
```

- **Now:**

```
Append every Contradiction and Need to `courses/athlete-career/notes/syllabus-flags.md`
```

### B13. template step 7 (brief flags, section 5 rule 7)

- **Was:**

```
Change no brief: `briefs.md` and the units in `course.toml` are edited only by a syllabus review that the owner confirms.
```

- **Now:**

```
Change no brief: a flag that would change a brief stays proposed and is listed in the reply (section 5, rule 7); `briefs.md` and the units in `course.toml` are edited only by a syllabus review that the owner confirms.
```

### B14. template step 8 (course line, example, path)

- **Was:**

```
`course:` as `supply-chain-execution · SCE · Supply Chain Execution for Product Teams`; `next_unit` in records.json is the bare code, `SCE2`) on `courses/supply-chain-execution/{CODE}-<slug>.md`
```

- **Now:**

```
`course:` as `athlete-career · AC · Managing an Athlete's Career`; `next_unit` in records.json is the bare code, `AC2`) on `courses/athlete-career/{CODE}-<slug>.md`
```

### B15. template step 10 (clone rule)

- **Was:**

```
the `kit/academy/` of the commit you cloned, saved outside the repo before any build
```

- **Now:**

```
the `kit/academy/` of the start commit that `out/<this row>/land-start.json` records, saved outside the repo before any build
```

### B16. template step 10 (clone rule)

- **Was:**

```
Then `./deploy.sh` once: clone `apcanario/academy` once (shallow, push access; if refused, carry on and ask the owner once at the end), set `ACADEMY_DIR` to the clone, and confirm with `gh run` that the deployment succeeded.
```

- **Now:**

```
Then `./deploy.sh` once (it reaches its deploy repository itself), and confirm with `gh run` that the deployment succeeded.
```

### B17. template step 11 (course code, mirrors, starter rows; section 5 rules 3 and 4)

- **Was:**

```
**11. Close** per `docs/method.md` §8, steps 1 to 5: the row moved to `docs/CHANGELOG.md` with the date, the models and a one-line result; its entry in `docs/site-log.md` moved from Next to Done ("{CODE}, {TITLE}, written"; "course SCE complete" on the last unit); corrections left open go to the Corrections section, proposals to Carried proposals with their ⚠ flags; the Project copies `claude/BACKLOG-chats.md` and `claude/CHANGELOG-chats.md` rewritten, and the course's three data mirrors (`claude/supply-chain-execution-course.toml`, `claude/supply-chain-execution-briefs.md`, `claude/supply-chain-execution-syllabus-flags.md`) refreshed when this row changed them, but only once they exist: S-SCE0 did not add them while sport-psychology's were in the Project (`docs/method.md` §8 step 4); the Project holds the data mirrors only of the course being written, and the row that files that course's last unit deletes them, so this course's are added by the row that files the last unit of whichever course is being written when they are due; a row of this course that finds them absent after that adds all three from their repo files (`project_write` with `local_path`); while sport-psychology's are still in the Project, none is written; {SAVE}.
```

- **Now:**

```
**11. Close** per `docs/method.md` §8, steps 1 to 5: the row moved to `docs/CHANGELOG.md` with the date, the models and a one-line result; its entry in `docs/site-log.md` moved from Next to Done ("{CODE}, {TITLE}, written"; "course AC complete" on the last unit); corrections left open go to the Corrections section, proposals to Carried proposals with their ⚠ flags; the Project copies `claude/BACKLOG-chats.md` and `claude/CHANGELOG-chats.md` rewritten, and the course's three data mirrors (`claude/athlete-career-course.toml`, `claude/athlete-career-briefs.md`, `claude/athlete-career-syllabus-flags.md`) refreshed when this row changed them (`docs/method.md` §8 step 4: the Project holds the data mirrors only of the course being written, and the row that files that course's last unit deletes them); a row of this course that finds them absent adds all three from their repo files (`project_write` with `local_path`), reading each existing path with `project_read` first; no long prompt is saved for this course: the first row of each group of four in `docs/BACKLOG.md` holds the course's starter line and the others "runs in the chat of <first row>" (section 5, rules 3 and 4), which `--save` keeps; {SAVE}.
```

### B18. template Reply (section 5, rule 7)

- **Was:**

```
**Reply:** what was filed where (words, figures, references opened and not opened); the fresh-check verdict and the result of each of the seven passes; each mistake corrected, in a line; each flag raised, with the units it affects and whether it blocks the next unit; the private-terms result; verify's result; the publish and the deploy; the choices taken; the backlog hand-off; every proposal listed with its ⚠ flag, and every task still open for the owner by hand (P-SCE1 of the syllabus and every row under Proposed of `docs/BACKLOG.md` marked for him, by row number, as the backlog holds them at the close; on 22 Nov 2026: P-SCE1, P-SCE6, P-NAV3 and P-DEC26), repeated in every reply until he marks it done; then {NEXTPROMPT} in a code block.
```

- **Now:**

```
**Reply** (section 5, rule 7): under the row's name, what was filed where (words, figures, references opened and not opened); the fresh-check verdict and the result of each of the seven passes; each mistake corrected, in a line; each flag raised, with the units it affects and whether it blocks the next unit; the private-terms result; verify's result; the publish and the deploy; the choices taken. Then, once for the chat: every proposal raised, each with what it does and a ⚠ on any disruption elsewhere (worked in the next row unless the owner vetoes it); every flag that would change a brief, which stays proposed; tasks for the owner, left only where no agent can do the task, and every row under Proposed of `docs/BACKLOG.md` marked for the owner, by row number, as the backlog holds them at the close, repeated in every reply until it is marked done; the backlog hand-off. The reply ends with the course's starter line in a code block, as `python3 kit/next_prompt.py --starter athlete-career` prints it, never a long prompt; on the last row it ends instead with {NEXTPROMPT} in a code block.
```

### B19. template step 3, rule 16 (after check, M2)

The appended hand-in rule carried the Execution course's rule numbers: "**Case facts** (rule 8), **Contradictions** and **Needs** (rule 11)" now "**Case facts** (rule 13), **Contradictions** and **Needs** (rule 15)", this course's The case and Flags and corrections.

## C. Line-level diff of the template (every line changed)

Line numbers are those of the code block (the Execution template on the left, this course's on the right). Owner-name substitutions in lines otherwise unchanged (the thin-chat paragraph's "ask the owner", step 1c's "unless the owner removed one", step 7's "that the owner confirms") appear here as changed lines.

```diff
--- supply-chain-execution template
+++ athlete-career template
@@ -2 +2 @@
-Right after cloning, run `python3 kit/land.py start <this row>` (it records the start commit and installs the push guard). Row {ROW} of `docs/BACKLOG.md`, in this chat: write, fresh-check and file unit {CODE}, "{TITLE}", of the public course Supply Chain Execution for Product Teams (`courses/supply-chain-execution/course.toml`: data `courses/supply-chain-execution/notes/`, vault `courses/supply-chain-execution/`, `docs/sourcing-standard.md` Parts 1 and 8; search {SEARCH}); correct every mistake the work finds; flag every contradiction or need that touches another unit; then build, verify, land (`kit/land.py land`), then publish Academy once from a fresh build of the landed HEAD (the artifact, then GitHub Pages), close the row and end with the next row's prompt.
+First, run `python3 kit/land.py start <this row>` (it records the start commit and installs the push guard). Row {ROW} of `docs/BACKLOG.md`, in this chat: write, fresh-check and file unit {CODE}, "{TITLE}", of the public course Managing an Athlete's Career (`courses/athlete-career/course.toml`: data `courses/athlete-career/notes/`, vault `courses/athlete-career/`, `docs/sourcing-standard.md` Parts 1 and 11; search {SEARCH}); correct every mistake the work finds; flag every contradiction or need that touches another unit; then build, verify, land (`kit/land.py land`), then publish Academy once from a fresh build of the landed HEAD (the artifact, then GitHub Pages), close the row and end the reply with the course's starter line.
@@ -6 +6 @@
-**This is a thin main chat** (method §4). (1) The chat runs on Sonnet 5.5 and the record says which model it ran as. The writer, the fresh checker, the applier, the filer and the corrections checker are each a fresh Agent on model opus, isolated on a packet (the harness may refuse `isolation: worktree`; then the Agent is launched without it and its isolation is the packet folder and its instructions, said in the record). (2) The chat never opens a unit, a report or a brief. It stages each packet with `python3 kit/thin.py stage <writer|checker|applier|filer> --row {ROW} <folder>`, launches the agent, and reads only the agent's reply, at most six lines, and the `out/stats.json` that `python3 kit/thin.py stats <out folder>` writes. Every agent writes its full output to files in its `out/` folder. (3) Scripts, not the chat, check the result: `kit/index_check.py`, `kit/private_terms.py`, the last line of `build.py`, `verify.py`, the publish read-back by sha256. (4) A checkpoint commit follows every agent's return, on `main`; it is landed at step 10 with `kit/land.py` (never a bare push). (5) No unit is uploaded to the Project. If the session's permission check refuses to run the repo's own scripts, stop, say so in one line and ask the owner; never work around it. Where a choice is open, take the most reasonable reading, say so in the record and carry on; ask only if blocked. Fix every error, should-fix and minor finding the work turns up in this chat.
+**This is a thin main chat** (method §4). (1) The chat runs on Sonnet 5.5 and the record says which model it ran as. The writer, the fresh checker, the applier, the filer and the corrections checker are each a fresh Agent on model opus, isolated on a packet (the harness may refuse `isolation: worktree`; then the Agent is launched without it and its isolation is the packet folder and its instructions, said in the record). (2) The chat never opens a unit, a report or a brief. It stages each packet with `python3 kit/thin.py stage <writer|checker|applier|filer> --row {ROW} <folder>`, launches the agent, and reads only the agent's reply, at most six lines, and the `out/stats.json` that `python3 kit/thin.py stats <out folder>` writes. Every agent writes its full output to files in its `out/` folder. (3) Scripts, not the chat, check the result: `kit/index_check.py`, `kit/private_terms.py`, the last line of `build.py`, `verify.py`, the publish read-back by sha256. (4) A checkpoint commit follows every agent's return, on `main`; it is landed at step 10 with `kit/land.py` (never a bare push). (5) No unit is uploaded to the Project. If the session's permission check refuses to run the repo's own scripts, stop, say so in one line and ask the owner; never work around it. Where a choice is open, take the most reasonable reading, say so in the record and carry on; ask only if blocked. Fix every error, should-fix and minor finding the work turns up in this chat.
@@ -8 +8 @@
-**The carry-forward rule (the owner, standing; `docs/supply-chain-execution-prompts.md` §4, `docs/method.md` §9).** Nothing found goes unrecorded or waits for a later audit. It applies to every row of this course, the last included.
+**The carry-forward rule (the owner, standing; `docs/athlete-career-prompts.md` §4, `docs/method.md` §9).** `docs/method.md` §9, with this course's names. It holds for every row, the last included.
@@ -10,7 +10,12 @@
-1. **What counts.** Any error, mistake, contradiction, unverified claim, missing source or unmet need, found before, during or after a unit is written: by the writer, the fresh checker, the applier, the filer, the corrections checker, a script, or the owner.
-2. **About a unit already filed.** It goes into the next row's prompt as a correction, with the unit, the passage, what is wrong and the source. The next chat fixes it first, before it writes its own unit: each change is checked by a fresh agent against its source and the syllabus, applied as an exact replacement, and recorded.
-3. **About a unit not yet written.** It becomes a flag in `syllabus-flags.md` naming every unit it affects, and it is printed in each of those units' prompts as a guideline for the writer. A flag that would change a brief is proposed, never applied by the chat that raised it.
-4. **About the unit being written.** It is fixed in the same chat before filing. What cannot be fixed (a source that will not open) is cut or marked unverified in the unit, and carried as in 2.
-5. **Every delivery ends with the next prompt.** The reply of every row closes with the prompt for the next unit in a code block, as `kit/next_prompt.py` prints it, already holding: every correction still open on a filed unit, every open flag that names the next unit, and any guideline of this prompt that the row showed needs updating, with the update made. A row that finds a rule of the template wrong or unworkable corrects it in `docs/supply-chain-execution-prompts.md`, says what it changed, and the next prompt carries the corrected text.
-6. **Nothing is dropped silently.** A correction or flag leaves the next prompt only when it is resolved, with the row and the report that resolved it written beside it.
-7. **The last row** (W-DD-SCE2) delivers a closing corrections prompt in place of a next unit's, listing every correction and flag still open.
+1. **What counts.** Any error, mistake, contradiction, unverified claim, missing source or unmet need, found before, during or after a unit is written: by the writer, the fresh checker, the applier, the filer, the corrections checker, a script, or the owner.
+2. **About an AC unit already filed.** It goes into the next row's prompt as a correction, with the unit, the passage, what is wrong and the source. The next chat fixes it first: each change is checked by a fresh agent against its source and the syllabus, applied as an exact replacement, and recorded.
+3. **About an AC unit not yet written.** It becomes a flag in `courses/athlete-career/notes/syllabus-flags.md` naming every unit it affects, printed in each of those units' prompts. A flag that would change a brief is proposed, never applied by the chat that raised it.
+4. **About the unit being written.** Fixed in the same chat before filing. What cannot be fixed is cut or marked unverified, and carried as in 2.
+5. **Every row hands on to the next through the repo.** The next row's prompt, as `kit/next_prompt.py` prints it, holds every open correction, every open flag that names the next unit, and any rule of this document the row showed to be wrong, corrected here. Inside a bundle the chat runs it; at the end of a chat the reply ends with the starter (section 5), which prints it.
+6. **Nothing is dropped silently.** A correction or flag leaves the next prompt only when resolved, with the row and the report that resolved it beside it.
+7. **The last row** (W-DD-AC3) is followed, in the same chat, by the closing corrections (section 5, rule 6). A closing prompt is delivered only if something remains open, with the reason.
+
+Two additions for this course:
+
+8. **Sport Psychology's register.** A conflict between this course's case and `courses/sport-psychology/notes/case-facts.md` is a correction to this course. A fault found in a filed Sport Psychology unit goes under Corrections in `docs/BACKLOG.md`.
+9. **Portugal.** A Portuguese text found changed since an earlier unit cited it is a correction to that unit.
@@ -20 +25 @@
-**1b. Corrections first** (`docs/public-courses.md` §3 rule 12), under that rule's limits, spelled out as (a) to (f) under the rows when there are any, each change checked by a fresh Agent on model opus against its source and the syllabus before it is applied, its report saved as `audits/supply-chain-execution/corrections-<date>-<codes>.md`:
+**1b. Corrections first** (`docs/public-courses.md` §3 rule 12), under that rule's limits, spelled out as (a) to (f) under the rows when there are any, each change checked by a fresh Agent on model opus against its source and the syllabus before it is applied, its report saved as `audits/athlete-career/corrections-<date>-<codes>.md`:
@@ -23 +28 @@
-**1c. Carried proposals**, worked now unless the owner removed one from this list:
+**1c. Carried proposals**, worked now unless the owner removed one from this list:
@@ -26 +31 @@
-**2. Stage the writer's packet** in one folder outside the repo with `python3 kit/thin.py stage writer --row {ROW} <folder>`. It holds: `brief.txt`, built by script with `open_brief` (the preamble, the Aim, Takes and Gives lines, the unit brief; never reworded, never retyped); `skills/write-unit/SKILL.md`; `docs/sourcing-standard.md` Parts 1 and 8; the figure kinds; `courses/supply-chain-execution/notes/case-facts.md`; `courses/supply-chain-execution/notes/bibliography.md`; every unit of this course already filed: {FILED}; `flags.txt`. The chat opens none of it.
+**2. Stage the writer's packet** in one folder outside the repo with `python3 kit/thin.py stage writer --row {ROW} <folder>`. It holds: `brief.txt`, built by script with `open_brief` (the preamble, the Aim, Takes and Gives lines, the unit brief; never reworded, never retyped); `skills/write-unit/SKILL.md`; `docs/sourcing-standard.md` Parts 1 and 11; the figure kinds; `courses/athlete-career/notes/case-facts.md`; `courses/athlete-career/notes/bibliography.md`; every unit of this course already filed: {FILED}; `flags.txt`. The chat opens none of it.
@@ -37 +42 @@
-- The writer rules of this course (`docs/supply-chain-execution-prompts.md` §1). The writer is one fresh Opus 5.5 agent with its packet and nothing else.
+- The writer rules of this course (`docs/athlete-career-prompts.md` §1). The writer is one fresh Opus 5.5 agent with its packet and nothing else.
@@ -39 +44 @@
-2. **Source log.** `out/sources.md`: one row per reference with the address opened, what was read (abstract, reprint or full text), the date, and the claims it carries. A reference that could not be opened is listed as not opened and carries nothing. A title is the article's own title, never a slug; a figure is cited to the paper that reports it, not to one that repeats it; each Sources entry is checked against the publisher's record before hand-in.
+2. **Source log.** `out/sources.md`: one row per reference with the address opened, what was read (abstract, summary or full text; for a law, the articles read), the date, and the claims it carries. A reference that could not be opened is listed as not opened and carries nothing. A title is the work's own title, never a slug; a figure is cited to the source that reports it, not to one that repeats it; each Sources entry is checked against the publisher's or issuing body's record before hand-in.
@@ -41,9 +46,13 @@
-4. **Grade every claim** by SCE1's key. From SCE2 on, the key arrives in the packet inside SCE1.
-5. **Vendors.** Assess, rank, compare or recommend no real vendor, and map no real vendor's product line. Name a real vendor only to attribute a dated public statement to it, graded vendor-reported, or as an entry in a dated list from a named analyst report or an audited filing, every vendor on the list alike. Worked product examples use Halvern Systems, Varnby Software and Kestrow, from the case register, labelled fictional. Never say or hint which real company a fictional one resembles.
-6. **Analyst reports.** Say how each was read. If only the abstract could be opened, the unit states only what the abstract states.
-7. **No private figures.** No price, revenue, margin or win rate of a private company unless it published it. Where a brief asks for a cost line with no public figure, write "no public figure".
-8. **The case** comes from `case-facts.md` only; invented facts go in the notes.
-9. **Scope.** No AI features. No interview framing. No craft method taught. Nothing about the Project's owner, his employer, his role or his work.
-10. **The two closing sections** before the deliverable: "On a site visit" and "Self-check", every answer drawn from the unit's sourced text.
-11. **Flags and corrections.** A contradiction with a filed unit or a brief, a mistake noticed in a filed unit, or a need the syllabus does not meet, is written to `out/notes.md` (a contradiction or a mistake under **Contradictions**, a mistake with the quoted passage, what is wrong, the source and the exact replacement; a need under **Needs**), naming every unit it affects and with a proposed change, so that the filer writes it into `syllabus-flags.md` in that file's form. It is carried by the carry-forward rule above. The writer never rewords a brief.
-12. **Hand-in.** The unit, `out/unit.md` (front matter, the unit, the deliverable, Sources); `out/sources.md`; `out/notes.md` with three lists, each item naming the unit codes it touches, an empty list written as "none": **Case facts** (rule 8), **Contradictions** and **Needs** (rule 11); the figures rendered; `out/unsure.md`, up to ten claims it is unsure of, closing with the `Object:` line; a reply of six lines at most (its model, the files it wrote, the counts of its lists, the number of references opened and not opened). `out/stats.json` is not the writer's: the chat writes it from these files with `python3 kit/thin.py stats`.
+4. **Reputable and verifiable only.** A law firm's note, a press report, a recruiting or agency site may lead you to a text; the text is what you read and cite. An interested party's page is evidence of what that party says, offers or requires, never of how things are.
+5. **Grade every claim** by AC1's key. From AC2 on, the key arrives in the packet inside AC1.
+6. **Rules are never the reader's.** Each rule or law is its issuing body's text, with its sport or country and the date read, followed by the question the reader puts to their own body.
+7. **Portugal.** Where the brief has "In Portugal", read each text at the Diário da República or the body's own page, cite it in Portuguese with its article, give its sense in English as your translation, and label the section one country's worked example. The private-terms check fails on two Portuguese city names (the plain lines of `kit/private-terms.txt`): a source whose title or address holds one is cited without that word where the record allows, and otherwise raised under Needs, never reworded around.
+8. **Money.** No fee, rate, commission or typical deal value unless a named source published it, with whose figure, sample, year and currency. Otherwise write "no public figure".
+9. **Not advice.** The line once near the top. Legal and tax points are questions with the body or professional to ask. Nothing about investing.
+10. **Minors.** Nothing on AC4's refusal list is proposed. From AC5 on, "If the athlete is under 18" closes the body before the Self-check and agrees with AC4.
+11. **The roles.** Wherever the coach or the coach's business has a stake in the decision described, name the conflict and say who else decides. Never present the reader's good intentions, or working unpaid, as settling it.
+12. **Real people and companies.** No real athlete, coach or family as an example of hardship or failure beyond what they published themselves or a court or inquiry states. No real agent, agency or sponsor assessed, ranked or recommended. Nothing about the Project's owner, his sport, his club, his athletes or his business.
+13. **The case** comes from `case-facts.md` only, which carries Sport Psychology's facts; invented facts go in the notes. Sara's and Dani's referrals are respected in anything planned for them.
+14. **The closing sections** before the deliverable: "Check before you act", then from AC5 on "If the athlete is under 18", then "Self-check", every answer drawn from the unit's sourced text.
+15. **Flags and corrections.** A contradiction with a filed unit or a brief, a mistake noticed in a filed unit, or a need the syllabus does not meet, is written to `out/notes.md` (a contradiction or a mistake under **Contradictions**, a mistake with the quoted passage, what is wrong, the source and the exact replacement; a need under **Needs**), naming every unit it affects and with a proposed change. It is carried by the carry-forward rule above. The writer never rewords a brief.
+16. **Hand-in.** As the template's hand-in rule: `out/unit.md`, `out/sources.md`, `out/notes.md` with its three lists (**Case facts**, **Contradictions**, **Needs**), the figures rendered, `out/unsure.md` closing with the `Object:` line, and a reply of six lines at most. The template's hand-in rule, which this rule names, in full: The unit, `out/unit.md` (front matter, the unit, the deliverable, Sources); `out/sources.md`; `out/notes.md` with three lists, each item naming the unit codes it touches, an empty list written as "none": **Case facts** (rule 13), **Contradictions** and **Needs** (rule 15); the figures rendered; `out/unsure.md`, up to ten claims it is unsure of, closing with the `Object:` line; a reply of six lines at most (its model, the files it wrote, the counts of its lists, the number of references opened and not opened). `out/stats.json` is not the writer's: the chat writes it from these files with `python3 kit/thin.py stats`.
@@ -51,9 +60,9 @@
-**4. The fresh check.** A separate fresh Agent on model opus that has not seen the writing, under the same agent rules, **with live search**: the prompt of `skills/audit-units` §3 with its figures paragraph, on a packet made with `python3 kit/thin.py stage checker --row {ROW} <folder> --unit out/unit.md --notes out/notes.md --unsure out/unsure.md --sources out/sources.md`. The packet holds the course's filed units (`filed/`, W-SCE2): the checker checks every pointer the unit makes to a filed unit, and every pointer to one of its own sections against that section's number. It writes `out/report.md` (or returns it as its reply, which the chat saves verbatim, the agent's line `Verdict: {CODE} · keep|fix|rewrite · counts` ahead of it) and replies in at most six lines. Beyond the skill's items it runs the seven passes of `docs/supply-chain-execution-prompts.md` §2 and reports each by name. One fresh Opus 5.5 agent that has not seen the unit written. It writes findings (error, should-fix, minor) and edits nothing. A reference that does not exist stops the row.
-1. **References exist and match.** Every Sources entry against its publisher's or Crossref's record: authors, title, journal, year, volume, pages, DOI.
-2. **Claims against sources.** Every cited claim opened and read against its source; "unverifiable" where the source will not open, never a pass.
-3. **Grades.** Each grade against SCE1's key; a vendor's statement never carries more than vendor-reported; an abstract-only reading is said to be one.
-4. **Vendors.** No real vendor assessed, ranked, compared, recommended or mapped; each real vendor named only as writer rule 5 allows; every list complete and alike; no private company's unpublished figure; no fictional vendor tied to a real one.
-5. **The case.** Every case fact against `case-facts.md`; labelled fictional; never used as evidence.
-6. **Scope and tone.** No AI features, no interview framing, no method teaching, nothing about the Project's owner or his employer; the preamble's tone rules; terms defined on first use.
-7. **Deliverable and figures.** The deliverable against the brief's wording, built in full and then as a template; "On a site visit" and "Self-check" present and agreeing with the body; every figure's labels and numbers traced to the text.
-It also runs the unit against Part 8 line by line and reads it as the reader in the preamble would. Before any fix, `python3 kit/thin.py save-report --row {ROW} --report out/report.md --model <the model it stated> --chat <this session's link> --date <today>` saves the report as `audits/supply-chain-execution/fresh-check-{CODE}.md`; `python3 kit/thin.py assemble out/unit.md out/unsure.md "<the line it prints>"` gives the unit its unsure list. A `rewrite` verdict sends the unit to a new writer from the same brief, once; a second stops the row with a note.
+**4. The fresh check.** A separate fresh Agent on model opus that has not seen the writing, under the same agent rules, **with live search**: the prompt of `skills/audit-units` §3 with its figures paragraph, on a packet made with `python3 kit/thin.py stage checker --row {ROW} <folder> --unit out/unit.md --notes out/notes.md --unsure out/unsure.md --sources out/sources.md`. The packet holds the course's filed units (`filed/`, from the Execution course's row W-SCE2): the checker checks every pointer the unit makes to a filed unit, and every pointer to one of its own sections against that section's number. It writes `out/report.md` (or returns it as its reply, which the chat saves verbatim, the agent's line `Verdict: {CODE} · keep|fix|rewrite · counts` ahead of it) and replies in at most six lines. Beyond the skill's items it runs the seven passes of `docs/athlete-career-prompts.md` §2 and reports each by name. One fresh Opus 5.5 agent that has not seen the unit written, with live search. It writes findings (error, should-fix, minor) and edits nothing. A reference that does not exist stops the row.
+1. **References exist and match.** Every Sources entry against its publisher's, Crossref's or its issuing body's record: authors, title, journal or publisher, year, volume, pages, DOI; for a law, its number, date and official-journal reference.
+2. **Claims against sources.** Every cited claim opened and read against its source; samples and designs stated; an inference from famous athletes or large sponsorships to an unknown athlete labelled; "unverifiable" where the source will not open, never a pass.
+3. **Grades.** Each grade against AC1's key; an interested party never graded research or data; an abstract-only reading said to be one.
+4. **Rules and Portugal.** No rule or law stated as the reader's; each with its body, its sport or country and the date read; each "In Portugal" text read at its issuing page and fairly translated; no law firm's note or press report standing in for a text.
+5. **Safety.** The not-advice line. Minors: nothing from the refusal list; "If the athlete is under 18" agrees with AC4. No supplement recommended. No real person in hardship beyond the rule; no real agent, agency or sponsor assessed. Nothing teaches getting around a rule. The roles conflict named where the coach or the coach's business has a stake. No money figure without source, sample, year and currency.
+6. **The case, scope and tone.** Every case fact against `case-facts.md` and, through it, Sport Psychology's register; labelled fictional; never evidence. Nothing about the Project's owner. No coaching, psychology or audience-building method re-taught. The preamble's tone rules; terms defined on first use.
+7. **Deliverable and figures.** The deliverable against the brief's wording, built in full on the named case and then as a template; the closing sections present and agreeing with the body; every figure's labels and numbers traced to the text.
+It also runs the unit against Part 11 line by line and reads it as the reader in the preamble would. Before any fix, `python3 kit/thin.py save-report --row {ROW} --report out/report.md --model <the model it stated> --chat <this session's link> --date <today>` saves the report as `audits/athlete-career/fresh-check-{CODE}.md`; `python3 kit/thin.py assemble out/unit.md out/unsure.md "<the line it prints>"` gives the unit its unsure list. A `rewrite` verdict sends the unit to a new writer from the same brief, once; a second stops the row with a note.
@@ -61 +70 @@
-**5. Apply.** A fresh applier agent (staged with `thin.py stage applier --row {ROW} <folder> --unit <unit> --report <report> --sources out/sources.md`) verifies each finding against the unit and the cited source and writes `out/apply.json` (`apply` or `hold`, with the reason); `python3 kit/thin.py apply <unit> fixes.json out/apply.json` applies it as exact replacements, the unit left unchanged if one fails, the applier re-run on the failures once. The applier's packet also gets the course's filed units and the writer's source log, and it works the report's could-not-verify list too (W-SCE2): each item is verified at its source or against the filed unit it points to, and what does not verify is cut or marked unverified in the unit by an exact replacement (`out/extra-fixes.json` and `out/extra-apply.json`, applied with `thin.py apply` after the findings). Every `hold` is recorded with its reason; a held error or should-fix is a flag. A figure that fails is fixed and re-checked by a new agent, as many times as it takes; figures are never dropped. Restarts: when the harness says it is resuming an agent, let it and say so in the record; if an agent is lost, re-run it from the start once; if lost again, start a fresh agent on the same packet that resumes from the lost run's working files. Look for agent transcripts (`.jsonl` under `/root/.claude/` or `/tmp/`); where they exist, check by script that each agent used no tool it was denied and read nothing outside its folder, and take its `"model"` field; where there are none, say so, and the model is the one the agent stated.
+**5. Apply.** A fresh applier agent (staged with `thin.py stage applier --row {ROW} <folder> --unit <unit> --report <report> --sources out/sources.md`) verifies each finding against the unit and the cited source and writes `out/apply.json` (`apply` or `hold`, with the reason); `python3 kit/thin.py apply <unit> fixes.json out/apply.json` applies it as exact replacements, the unit left unchanged if one fails, the applier re-run on the failures once. The applier's packet also gets the course's filed units and the writer's source log, and it works the report's could-not-verify list too (from the Execution course's row W-SCE2): each item is verified at its source or against the filed unit it points to, and what does not verify is cut or marked unverified in the unit by an exact replacement (`out/extra-fixes.json` and `out/extra-apply.json`, applied with `thin.py apply` after the findings). Every `hold` is recorded with its reason; a held error or should-fix is a flag. A figure that fails is fixed and re-checked by a new agent, as many times as it takes; figures are never dropped. Restarts: when the harness says it is resuming an agent, let it and say so in the record; if an agent is lost, re-run it from the start once; if lost again, start a fresh agent on the same packet that resumes from the lost run's working files. Look for agent transcripts (`.jsonl` under `/root/.claude/` or `/tmp/`); where they exist, check by script that each agent used no tool it was denied and read nothing outside its folder, and take its `"model"` field; where there are none, say so, and the model is the one the agent stated.
@@ -65 +74 @@
-**7. Syllabus flags.** Append every Contradiction and Need to `courses/supply-chain-execution/notes/syllabus-flags.md` (next number, date, raised by {CODE}, the units affected, the flag, the proposed change, status open); set to `carried` each flag this unit was given and dealt with. The writer's Case facts reach the table "Added by units" of `case-facts.md` through the filer at step 8 (`case_lines` in `records.json`, one row each, inserted by `thin.py insert`); the chat does not open the notes. Change no brief: `briefs.md` and the units in `course.toml` are edited only by a syllabus review that the owner confirms. If a flag means the next unit cannot be written as briefed, say so in the first line of the reply and write a syllabus-review prompt in place of the next unit's.
+**7. Syllabus flags.** Append every Contradiction and Need to `courses/athlete-career/notes/syllabus-flags.md` (next number, date, raised by {CODE}, the units affected, the flag, the proposed change, status open); set to `carried` each flag this unit was given and dealt with. The writer's Case facts reach the table "Added by units" of `case-facts.md` through the filer at step 8 (`case_lines` in `records.json`, one row each, inserted by `thin.py insert`); the chat does not open the notes. Change no brief: a flag that would change a brief stays proposed and is listed in the reply (section 5, rule 7); `briefs.md` and the units in `course.toml` are edited only by a syllabus review that the owner confirms. If a flag means the next unit cannot be written as briefed, say so in the first line of the reply and write a syllabus-review prompt in place of the next unit's.
@@ -67 +76 @@
-**7b. Proposals now** (`docs/public-courses.md` §3 rule 12): every correction to a filed unit or a record, and every kit fix the work needs, is made in this chat before the build, under that rule's limits, each change to a unit checked by a fresh Agent on model opus first. Only a brief change and a task for the owner stay *proposed*.
+**7b. Proposals now** (`docs/public-courses.md` §3 rule 12): every correction to a filed unit or a record, and every kit fix the work needs, is made in this chat before the build, under that rule's limits, each change to a unit checked by a fresh Agent on model opus first. Only a brief change and a task for the owner stay *proposed*.
@@ -69 +78 @@
-**8. File** per `skills/file-unit`, by a fresh filer agent and a script: front matter (model: `Opus 5.5`, the form `docs/courses-index.md` and `kit/index_check.py` use for the model the writer stated; `course:` as `supply-chain-execution · SCE · Supply Chain Execution for Product Teams`; `next_unit` in records.json is the bare code, `SCE2`) on `courses/supply-chain-execution/{CODE}-<slug>.md`; the filer, staged with `python3 kit/thin.py stage filer --row {ROW} <folder> --unit <unit> --notes <notes> --unsure <unsure> --report <report>`, writes `out/records.json` (the reading-page intro, saying what the unit is, how it was made and its known gaps, among them every reference not opened and every abstract-only claim; `STATUS`, `NEXT_UNIT`, `VERSION`, the hub `CHANGELOG` line, the case facts as `case_lines`, the flag rows, the `docs/courses-index.md` edits with a staleness row if search is on, both changelog entries, the `Object:` line); `python3 kit/thin.py insert out/records.json` inserts it and restores everything if it fails. Then `python3 kit/index_check.py` until it matches and `python3 kit/private_terms.py` prints OK.
+**8. File** per `skills/file-unit`, by a fresh filer agent and a script: front matter (model: `Opus 5.5`, the form `docs/courses-index.md` and `kit/index_check.py` use for the model the writer stated; `course:` as `athlete-career · AC · Managing an Athlete's Career`; `next_unit` in records.json is the bare code, `AC2`) on `courses/athlete-career/{CODE}-<slug>.md`; the filer, staged with `python3 kit/thin.py stage filer --row {ROW} <folder> --unit <unit> --notes <notes> --unsure <unsure> --report <report>`, writes `out/records.json` (the reading-page intro, saying what the unit is, how it was made and its known gaps, among them every reference not opened and every abstract-only claim; `STATUS`, `NEXT_UNIT`, `VERSION`, the hub `CHANGELOG` line, the case facts as `case_lines`, the flag rows, the `docs/courses-index.md` edits with a staleness row if search is on, both changelog entries, the `Object:` line); `python3 kit/thin.py insert out/records.json` inserts it and restores everything if it fails. Then `python3 kit/index_check.py` until it matches and `python3 kit/private_terms.py` prints OK.
@@ -73 +82 @@
-**10. Publish Academy once.** Before the build you publish, move the row to `docs/CHANGELOG.md`, move its entry in `docs/site-log.md` from Next to Done and {SAVEROW}, so the published Backlog and Changelog pages are current. **Land before you publish** (`docs/method.md` §10): commit everything above, then `python3 kit/land.py land <this row> --expected <file>`; publish only after it exits 0. Right before the publish, `git fetch` and require `git rev-parse HEAD` to equal `git rev-parse origin/main` (if main has moved, `git pull --ff-only` first), rebuild that HEAD (`cd kit && python3 build.py`) and publish that build, never one built before landing. Read the artifact https://claude.ai/artifact/WwmQpUSqAUJvrcmLczppEH first and compare the live page with the build you started from (`get_artifact` for the live version id; `list_files` for every file's sha256 against `sha256sum` of the start build's files, the `kit/academy/` of the commit you cloned, saved outside the repo before any build). Send only the files that differ from the live artifact's (their sha256 in `list_files`), found by script, and the shell inside the wrapper the live page carries (its first line and its closing `</body></html>`, taken from the saved live shell by script into a copy outside the repo), with `slug`, `base_version` and mode patch; read the sent files back and compare their sha256 with the build; never a new artifact, never forced. Then `./deploy.sh` once: clone `apcanario/academy` once (shallow, push access; if refused, carry on and ask the owner once at the end), set `ACADEMY_DIR` to the clone, and confirm with `gh run` that the deployment succeeded. The publish and deploy identifiers go into the records after the publish, committed and landed again with `kit/land.py`, without republishing.
+**10. Publish Academy once.** Before the build you publish, move the row to `docs/CHANGELOG.md`, move its entry in `docs/site-log.md` from Next to Done and {SAVEROW}, so the published Backlog and Changelog pages are current. **Land before you publish** (`docs/method.md` §10): commit everything above, then `python3 kit/land.py land <this row> --expected <file>`; publish only after it exits 0. Right before the publish, `git fetch` and require `git rev-parse HEAD` to equal `git rev-parse origin/main` (if main has moved, `git pull --ff-only` first), rebuild that HEAD (`cd kit && python3 build.py`) and publish that build, never one built before landing. Read the artifact https://claude.ai/artifact/WwmQpUSqAUJvrcmLczppEH first and compare the live page with the build you started from (`get_artifact` for the live version id; `list_files` for every file's sha256 against `sha256sum` of the start build's files, the `kit/academy/` of the start commit that `out/<this row>/land-start.json` records, saved outside the repo before any build). Send only the files that differ from the live artifact's (their sha256 in `list_files`), found by script, and the shell inside the wrapper the live page carries (its first line and its closing `</body></html>`, taken from the saved live shell by script into a copy outside the repo), with `slug`, `base_version` and mode patch; read the sent files back and compare their sha256 with the build; never a new artifact, never forced. Then `./deploy.sh` once (it reaches its deploy repository itself), and confirm with `gh run` that the deployment succeeded. The publish and deploy identifiers go into the records after the publish, committed and landed again with `kit/land.py`, without republishing.
@@ -75 +84 @@
-**11. Close** per `docs/method.md` §8, steps 1 to 5: the row moved to `docs/CHANGELOG.md` with the date, the models and a one-line result; its entry in `docs/site-log.md` moved from Next to Done ("{CODE}, {TITLE}, written"; "course SCE complete" on the last unit); corrections left open go to the Corrections section, proposals to Carried proposals with their ⚠ flags; the Project copies `claude/BACKLOG-chats.md` and `claude/CHANGELOG-chats.md` rewritten, and the course's three data mirrors (`claude/supply-chain-execution-course.toml`, `claude/supply-chain-execution-briefs.md`, `claude/supply-chain-execution-syllabus-flags.md`) refreshed when this row changed them, but only once they exist: S-SCE0 did not add them while sport-psychology's were in the Project (`docs/method.md` §8 step 4); the Project holds the data mirrors only of the course being written, and the row that files that course's last unit deletes them, so this course's are added by the row that files the last unit of whichever course is being written when they are due; a row of this course that finds them absent after that adds all three from their repo files (`project_write` with `local_path`); while sport-psychology's are still in the Project, none is written; {SAVE}.
+**11. Close** per `docs/method.md` §8, steps 1 to 5: the row moved to `docs/CHANGELOG.md` with the date, the models and a one-line result; its entry in `docs/site-log.md` moved from Next to Done ("{CODE}, {TITLE}, written"; "course AC complete" on the last unit); corrections left open go to the Corrections section, proposals to Carried proposals with their ⚠ flags; the Project copies `claude/BACKLOG-chats.md` and `claude/CHANGELOG-chats.md` rewritten, and the course's three data mirrors (`claude/athlete-career-course.toml`, `claude/athlete-career-briefs.md`, `claude/athlete-career-syllabus-flags.md`) refreshed when this row changed them (`docs/method.md` §8 step 4: the Project holds the data mirrors only of the course being written, and the row that files that course's last unit deletes them); a row of this course that finds them absent adds all three from their repo files (`project_write` with `local_path`), reading each existing path with `project_read` first; no long prompt is saved for this course: the first row of each group of four in `docs/BACKLOG.md` holds the course's starter line and the others "runs in the chat of <first row>" (section 5, rules 3 and 4), which `--save` keeps; {SAVE}.
@@ -77 +86 @@
-**Reply:** what was filed where (words, figures, references opened and not opened); the fresh-check verdict and the result of each of the seven passes; each mistake corrected, in a line; each flag raised, with the units it affects and whether it blocks the next unit; the private-terms result; verify's result; the publish and the deploy; the choices taken; the backlog hand-off; every proposal listed with its ⚠ flag, and every task still open for the owner by hand (P-SCE1 of the syllabus and every row under Proposed of `docs/BACKLOG.md` marked for him, by row number, as the backlog holds them at the close; on 22 Nov 2026: P-SCE1, P-SCE6, P-NAV3 and P-DEC26), repeated in every reply until he marks it done; then {NEXTPROMPT} in a code block.
+**Reply** (section 5, rule 7): under the row's name, what was filed where (words, figures, references opened and not opened); the fresh-check verdict and the result of each of the seven passes; each mistake corrected, in a line; each flag raised, with the units it affects and whether it blocks the next unit; the private-terms result; verify's result; the publish and the deploy; the choices taken. Then, once for the chat: every proposal raised, each with what it does and a ⚠ on any disruption elsewhere (worked in the next row unless the owner vetoes it); every flag that would change a brief, which stays proposed; tasks for the owner, left only where no agent can do the task, and every row under Proposed of `docs/BACKLOG.md` marked for the owner, by row number, as the backlog holds them at the close, repeated in every reply until it is marked done; the backlog hand-off. The reply ends with the course's starter line in a code block, as `python3 kit/next_prompt.py --starter athlete-career` prints it, never a long prompt; on the last row it ends instead with {NEXTPROMPT} in a code block.
```

## D. Below the template

- The note above the slots line ("Added by S-AC0 ...") and the slots line: new, in the form of the Execution and AI courses' documents (example codes W-AC4, AC4, read-ac4).
- "### This row in particular": section 3's 18 rows word for word, with a Unit column (the row code less "W-") and a Search column (from each paragraph's opening "Search on."/"Search off.", equal to the course's `order` for all 18).

