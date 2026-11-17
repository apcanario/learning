# Corrections check, syllabus review BW-1 (row S-BW), 17 Nov 2026

Checker: claude-opus-5-5. Every Current confirmed by script to occur exactly once in its file (python, str.count == 1 for all 13).

## Change 1
File: BW7-pipelines-raw-material-to-finished-output.md, §9, last sentence (F60)
Current:
````
BW8 turns the procedure into something that runs itself.
````
Replacement:
````
BW8 turns one stage of the procedure, the fresh check, into a skill.
````
Result: PASS — Current occurs once (BW7 §9, end of 'Two limits' paragraph). Replacement is F60's proposed wording verbatim. BW8 makes "stage 3 of BW7's Part 1 pipeline (the fresh check)" a skill (BW8 Deliverable intro), and BW7's own Part 1 names stage "3 Fresh check", so "one stage of the procedure, the fresh check" is accurate. Reads in place: "...gates run by you or by a script; BW8 turns one stage of the procedure, the fresh check, into a skill."
Syllabus: no conflict — agrees with BW8 §6 ("The skill itself is not scheduled") and the BW7/BW8 briefs.

## Change 2
File: BW7-pipelines-raw-material-to-finished-output.md, Deliverable intro (F60)
Current:
````
BW8 turns a procedure in this form into a skill and a scheduled run;
````
Replacement:
````
BW8 turns one stage in this form into a skill and schedules a different, date-driven check;
````
Result: PASS — Current occurs once (BW7 Deliverable intro). F60's wording verbatim. BW8 schedules "the monthly rot check" of BW4 (BW8 §6, "Which task to schedule"), a date-driven check different from the skill, and says a fresh check "starts when a draft is finished, which is an event, not a date". Reads in place before "BW9 decides which of its steps an agent may take."
Syllabus: no conflict — matches BW8 §6 and Deliverable F; F32's answer (BW8's choice stands) in proposal §4 agrees.

## Change 3
File: BW6-research-and-verification.md, §2 step 2 (F61)
Current:
````
Draw at least one claim from every stratum, then more from the largest until the sample reaches its size.
````
Replacement:
````
Draw at least one claim from every stratum, then the rest at random from all remaining claims, so larger strata get more in proportion, until the sample reaches its size.
````
Result: PASS — Current occurs once (BW6 §2 step 2). F61's wording. Matches BW8's `check.py sample`: one per section, then `rng.sample(rest, ...)` "so larger sections give more". Grammatical. "in proportion" holds in expectation, which is what the script does; acceptable as a method statement (F61: "a method statement, not a sourced fact"). BW6 §2's later sentence "A simple random sample of the same size can miss a whole section; a stratified one cannot" still holds.
Syllabus: no conflict — the four BW6 places and BW8 now state one rule; no other filed unit in files/ states the old rule (grep 'largest' finds only the four BW6 places).

## Change 4
File: BW6-research-and-verification.md, §2 step 3 (F61, companion)
Current:
````
3. **Draw by number, never by eye.** Number the claims in each stratum and pick with a random number.
````
Replacement:
````
3. **Draw by number, never by eye.** Number the claims and pick each draw with a random number: within its stratum for each stratum's first claim, from all remaining claims for the rest.
````
Result: PASS — Current occurs once (BW6 §2 step 3). Companion to Change 3: the old "Number the claims in each stratum" fits only within-stratum draws; the new text covers both kinds of draw. Grammatical. Step 5's "drawn again from the same stratum" for UNVERIFIABLE is a replacement draw and is unaffected; BW8's `redraw` does the same ("a replacement from the same section").
Syllabus: no conflict.

## Change 5
File: BW6-research-and-verification.md, Deliverable C2 (F61)
Current:
````
One claim per stratum, then extra draws from the largest strata until the sample reaches *n*; within a stratum, by random number.
````
Replacement:
````
One claim per stratum, then the rest at random from all remaining claims, so larger strata get more in proportion, until the sample reaches *n*; by random number.
````
Result: PASS — Current occurs once (BW6 Deliverable C2). Same rule as Change 3; the dropped "within a stratum" is right because the extra draws are no longer within a stratum. Reads: "...until the sample reaches *n*; by random number." Terse but grammatical in the checklist style.
Syllabus: no conflict.

## Change 6
File: BW6-research-and-verification.md, Deliverable, filled case text (F61)
Current:
````
then extra draws from the largest sections, by random number.
````
Replacement:
````
then the rest at random from all remaining claims, so larger sections get more in proportion, by random number.
````
Result: PASS — Current occurs once (BW6 filled case text, line beginning "Check every cited claim (census)"). Reads: "it is 29 claims: one per section, the deliverable as its own section, then the rest at random from all remaining claims, so larger sections get more in proportion, by random number." "at random ... by random number" is slightly redundant but not wrong; it keeps the parallel with C2 and the template.
Syllabus: no conflict.

## Change 7
File: BW6-research-and-verification.md, Deliverable, template (F61)
Current:
````
then extra draws from the largest strata, by random number"]
````
Replacement:
````
then the rest at random from all remaining claims, so larger strata get more in proportion, by random number"]
````
Result: PASS — Current occurs once (BW6 template, inside the [FILL: ...] quotation). The closing `"]` is kept, so the FILL bracket stays balanced. Same rule as Changes 3, 5, 6.
Syllabus: no conflict.

## Change 8
File: BW8-skills-and-automation.md, Deliverable, 'What the skill takes' (F61, companion)
Current:
````
Two changes, each for a script's sake: the claims table in item 1 carries a verdict column, so that a script can apply rule C5 rather than the model; and after one claim from every section, the extra draws are taken at random from all remaining claims, so larger sections give more draws in proportion, which is this unit's reading of BW6's "extra draws from the largest strata" in a form a script can repeat from its seed.
````
Replacement:
````
One change, for a script's sake: the claims table in item 1 carries a verdict column, so that a script can apply rule C5 rather than the model. After one claim from every section, the extra draws are taken at random from all remaining claims, so larger sections give more draws in proportion, as BW6 states the rule (corrected 17 Nov 2026), in a form a script can repeat from its seed.
````
Result: PASS — Current occurs once (BW8 Deliverable, 'What the skill takes from earlier units, and where it departs'). With BW6 corrected, the draw is no longer a departure, so "One change" is right; the verdict column remains the only departure. Grammatical; "as BW6 states the rule (corrected 17 Nov 2026)" is true once Changes 3 to 7 are applied, so this change must be applied together with them. The next sentence ("It runs as stage 3 of BW7's Part 1 pipeline ...") follows unchanged.
Syllabus: no conflict — depends on Changes 3–7 being applied in the same pass.

## Change 9
File: BW8-skills-and-automation.md, Unsure list item 9 (F61, companion)
Current:
````
the proportional extra draws in `check.py sample`, 
````
Replacement:
````

````
Result: PASS — Current (with its trailing space) occurs once (BW8 Unsure list item 9). Deleting it leaves "9. The pass thresholds of the trigger test (15 of 16, S1 3 of 3, no near-miss 3 of 3), the order of steps in the skill and the choice of the rot check as the scheduled task are this unit's design (stated opinion), not sourced rules." Grammatical. Correct to remove: after Changes 3–8 the proportional draw is BW6's rule, not BW8's design.
Syllabus: no conflict — depends on Changes 3–8.

## Change 10
File: BW3-briefing-prompts-that-hold-up.md, Conventions (F42)
Current:
````
- One brief per chat. If the first output misses, change the brief and open a new chat (§5).
````
Replacement:
````
- One brief per chat. If the first output misses, change the brief and open a new chat (§5). In a specified project, where briefs are not reworded once work starts, the miss is raised as a flag and the brief changes at a boundary (BW5 §5, §9).
````
Result: PASS — Current occurs once (BW3 Conventions). Replacement restates F42's own resolution ("in a specified project the miss is raised as a flag and the brief changes at a boundary (BW5 §5, §9)"). BW5 §5 has the paragraph "This rule and BW3's restart rule" ("the miss is recorded as a flag, the brief is changed at a boundary as a new version") and BW5 §9 is "How a spec is allowed to change" (the flag-and-review rule: "A flag waits for a boundary"). "briefs are not reworded once work starts" matches BW5 §5's heading "never reworded once work has started". Grammatical.
Syllabus: no conflict — forward pointer from BW3 to BW5 only; BW3's one-off rule stands.

## Change 11
File: DD-BW2-deep-dive-one-project-with-its-numbers.md, §7, 'A publish that had to be repeated' (F99)
Current:
````
**A publish that had to be repeated.** The case file records none. It says the site is published in two places after each filing, first as an artifact on claude.ai and then on GitHub Pages (§1, note), and that a script restores every file if the course index check fails (§1, note); it records no failed or repeated publish. If one happened, it is not in the record.
````
Replacement:
````
**A publish that had to be repeated.** The site is published in two places after each filing, first as an artifact on claude.ai and then on GitHub Pages (§1, note), and a script restores every file if the course index check fails (§1, note). The case file records one repeated publish and one retriggered deploy (§7, added 17 Nov 2026): a layout fault found after a publish on 4 Nov 2026 was fixed and the site published a second time the same day, neither the change's checker nor the verify script having caught it; and on 9 Nov 2026 a GitHub Pages run failed with no job run and was retriggered with an empty commit. It also records publishes the tool first refused until the named files were read or checked against the build, and deploys that did not run when attaching the public repository was refused (§7).
````
Result: PASS — Current occurs once (DD-BW2 §7). Each clause matches the case file lines dated 17 Nov 2026: "§7 · A publish repeated (the kit changelog, 4 Nov 2026): a layout fault found after a site change was published was fixed, rebuilt, verified and published a second time the same day; neither the change's checker nor the verify script had caught it"; "§7 · A failed deploy (the kit changelog, 9 Nov 2026): one GitHub Pages run failed with no job run; an empty commit retriggered it"; "§7 · Publishes refused at first ... the named files were read (in one entry, 191 files listed and eight compared), found equal to the build, and the publish made" (rendered "read or checked against the build", as the review's finding 12 corrected it); "§7 · Deploys missed ... did not run because attaching the public repository was refused or denied". The §1 notes it keeps are unchanged. Grammatical. "one repeated publish" is the case file's count (one such line).
Syllabus: no conflict — the DD-BW2 brief asks for "a publish that had to be repeated" and the record now holds one; the following paragraph's "Four of the six" counts the table rows above, which this paragraph is outside, so it still reads true. DD-BW3 is not in files/ (only its brief), so whether DD-BW3 repeats "records none" was not checked here.

## Change 12
File: DD-BW2-deep-dive-one-project-with-its-numbers.md, Deliverable Part 1 G (F99)
Current:
````
Repeated publish: not recorded.
````
Replacement:
````
Repeated publish: 1, and 1 failed deploy retriggered (§7, added 17 Nov 2026).
````
Result: PASS — Current occurs once (DD-BW2 Deliverable Part 1 G, last sentence). Matches Change 11 and the case lines of 4 and 9 Nov 2026. Telegraphic, like the rest of Part 1 G ("2 writers lost to restarts ...").
Syllabus: no conflict.

## Change 13
File: BW9-agents.md, §8, the case line (F52)
Current:
````
each unit written by one model from a brief, checked by a fresh context and audited by sample (Academy case file §1, §2)
````
Replacement:
````
with a method of one brief per unit, a fresh check and sample audits that the case file records as run on part of the library (Academy case file §1, §2, §5, §9)
````
Result: PASS — Current occurs once (BW9 §8, opening sentence). Replacement is the A1/F98/F112 wording, which every open brief in briefs/ now carries in its preamble ("with a method of one brief per unit, a fresh check and sample audits that the case file records as run on part of the library"). Reads: "...in October and November 2026, with a method of one brief per unit, a fresh check and sample audits that the case file records as run on part of the library (Academy case file §1, §2, §5, §9). It is one project by one person..." Case file supports it: fresh check on 36 marketing/AI/UX drafts (§5), audits 3 onward not run (§9); the 17 Nov §5 lines add that the second history course's 79 reports were "all checked by a fresh agent" and the history review measured units "written without a checker", so "part of the library" still holds.
Syllabus: no conflict — matches the briefs' preamble and DD-BW2's opening (DD-BW2 has "one brief per unit, and a fresh check and sample audits", with an extra "and"; the difference is stylistic).

## Check only (F89)

Finding: BW7's date is wrong as the working paper's date; it is not shown to be a second posting.

- beSpacific, post dated 19 Sep 2023 (https://www.bespacific.com/?p=100639, returned by search, read 17 Nov 2026): gives the SSRN citation of "Working Paper No. 24-013" (Harvard Business School Technology & Operations Mgt. Unit), abstract 4573321, with the date "(September 15, 2023)". The paper was therefore public on SSRN by 19 Sep 2023, three days before BW7's 22 Sep 2023.
- weiterbildungsblog.de, post dated 10 Oct 2023 (https://weiterbildungsblog.de/?p=13291, returned by search): lists the paper as "18. September 2023", which agrees with the publisher's 18 Sep 2023.
- A source-list page (https://global-agent-truth.lovable.app/..., returned by search): "September 2023", "working paper 24-013". Labourline: "2023", "24-013".
- No source a search returned gives 22 Sep 2023.
- Not checked: the SSRN abstract page (https://papers.ssrn.com/abstract=4573321) failed at its site; the MIT copy of the PDF that BW7 links was refused by the tool; the d3.harvard.edu result redirected (to aiinstitute.hbs.edu) and was not followed. None was retried. So whether 22 Sep 2023 is a later SSRN revision date could not be checked. Nothing returned supports it as a date of WP 24-013 or of its first posting: 15 Sep 2023 is the SSRN citation date and 18 Sep 2023 the posting date.

The replacement uses the month, which every returned source supports, and does not depend on which revision the MIT PDF is (two places; BW7's §4 table cell "HBS working paper, 2023" needs no change):

## New 1
File: BW7-pipelines-raw-material-to-finished-output.md, §3 item 4, the citation of Dell'Acqua et al.
Current:
````
Harvard Business School Working Paper 24-013, 22 Sep 2023]
````
Replacement:
````
Harvard Business School Working Paper 24-013, September 2023]
````

## New 2
File: BW7-pipelines-raw-material-to-finished-output.md, Sources, the Dell'Acqua et al. entry
Current:
````
Harvard Business School Working Paper 24-013, 22 September 2023.
````
Replacement:
````
Harvard Business School Working Paper 24-013, September 2023.
````

Each Current occurs once in BW7 (confirmed by script); "22 Sep" occurs nowhere else in BW7 or in the other files of the packet. If the owner prefers a day, 15 Sep 2023 (the SSRN citation date) is the one a returned source states for WP 24-013. A second check is owed before applying (proposal B6).

## Not a text change

1. Changes 8 and 9 assume Changes 3 to 7: BW8's "as BW6 states the rule (corrected 17 Nov 2026)" is false if any BW6 change is held back. Apply the seven together or not at all.
2. BW6 §2 step 2 and the other three places now say larger strata get more "in proportion". With random draws from the pooled remainder this is true in expectation, not exactly; acceptable for a method statement, and it is what BW8's script does.
3. DD-BW2 §7: the next paragraph ("Four of the six are failures of the record") counts only the table rows. With a repeated publish and a failed deploy now in the record, a later pass may want to say whether they belong to the "failures of the record" or the output; no text is wrong.
4. DD-BW3 is not in files/, so whether its §7 or Part D repeats DD-BW2's "records none" on the repeated publish could not be checked here (F99 names DD-BW3 among the units touched). This belongs with CP-4.
5. BW9 §8's new wording and DD-BW2's opening differ by one "and" ("one brief per unit, and a fresh check"); the briefs' preamble has no "and", as Change 13 has. Stylistic only.
6. F89's other part (BW7 calls it a working paper, since published in Organization Science) was already applied on 16 Nov 2026. One returned page (synapsesocial.com) gives the journal article's publication date as 11 Mar 2026; not read on the journal's own page, so not proposed.
