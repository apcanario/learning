---
audit: registration check
row: S-SP0 · Sport Psychology for Coaches
course: sport-psychology · SP · Sport Psychology for Coaches
model: claude-opus-5-5 (as the agent stated)
date: 2026-11-16
chat: https://claude.ai/code/session_01KMmgQyXGJJhkZb7nEAxmUo
verdict: PASS · 10 of 10
---

The registration checker's report, verbatim, from its hand-back. Saved before anything was fixed. A fresh Opus 5.5 agent that had not seen the registration, given the five attached files, the list of changed repo paths and the repository at commit d2d9b6c.

Model: claude-opus-5-5

1. PASS. Both files hash to sha256 f786fa130335b2e34e30a5f307900f199544ae694580eb7c75d9dd1aa104d335.

2. PASS. I took syllabus.md lines 109–131 (the bold Part 7 heading plus the 21 checklist lines, without the "To be appended…" instruction) and diffed them against the "## Part 7 · Sport Psychology for Coaches (…)" section at the end of sourcing-standard.md. They are identical, with 21 `- [ ]` lines. One form change: the bold heading `**Part 7 · …**` became a `## Part 7 · …` heading. The opening paragraph reads "Parts 2 to 7 are each course family's own rules…".

3. PASS. I imported hub.py and compared every field by script. All of these equal the syllabus: TITLE, BAR, BRAND_HTML, GOAL_SP (the section 3 Goal starting "by the end"), COURSES (one entry, key SP, slug sp, units is SP, and tile, intro and the 3 outcomes word for word in `<li><strong>`), COURSE_NOTE, ORDER, NEXT_UNIT 'SP1', STATUS {}, READINGS [], VERSION 'v1 · 16 Nov 2026', LEARN_NOTE, BUILD_PICK, and CHANGELOG v1 dated 2026-11-16 19:30. ORDER has 13 rows, all Opus 5.5, with search "on" only for SP9, DD-SP1 and DD-SP2. FRAME's three reasons, override and "Where the evidence pushes back" match word for word. One case change in FRAME: the syllabus pick "**Pick: a coach's course…**" is rendered as `<h2>Pick</h2>` followed by "A coach's course…", with a capital A. This is the same form as the building-with-ai hub.

4. PASS. `cmp` finds both files identical. bibliography.md is 37c78a9a…5d623 and case-facts.md is a57571ad…25bb in the repo and the packet.

5. PASS. `--list` shows W-SP1 (SP1, search off, not filed) as the first SP row. All 13 SP rows are listed as "not filed", in order W-SP1…W-SP10, W-DD-SP1, W-DD-SP2, W-DD-SP3.

6. PASS. I filled the template's slots by script and diffed the result against the `--row W-SP1` output.
   - **Equal:** every step (1, 1b, 1c, 2, 3, 4, 5, 6, 7, 7b, 8, 9, 10, 11, Reply) is printed. The SP1 paragraph is verbatim, and there is no step 5b. Every writer bullet of step 3, all seven checker passes and the Reply are identical to files/prompts.md. The safety-reader block in docs/sport-psychology-prompts.md also matches the original.
   - **Different:** exactly 7 lines (steps 1b, 4, 5, 7, 8, 9, 10), and each matches one of the seven listed corrections:
     - 1b: "limits, spelled out as (a) to (f) under the rows when there are any"
     - 4: "`plus out/sources.md`" became "`--sources out/sources.md`"
     - 5: the restart rule from W-DD-BW3 is inlined, with the transcript check and taking the `"model"` field
     - 7: case facts go through the filer's `case_lines` / `thin.py insert`
     - 8: `case_lines` is added to the records list
     - 9: "(check the id it prints)"
     - 10: the W-DD-BW3 publish procedure is inlined
   - I found no other difference. I could not check the step 5 and step 10 wording against the original W-DD-BW3 row, because that row has left the backlog.

7. PASS. W-SP9, W-DD-SP1 and W-DD-SP2 each print step 5b once, between step 5 and step 6. In each, it equals the safety-reader block of files/prompts.md with {CODE} filled, and the row's own paragraph is printed verbatim. W-SP10 and W-SP1 print no step 5b.

8. PASS. All four stage commands worked (rc 0) for W-SP1.
   - **writer:**
     - brief.txt equals `mdcourse.open_brief(hub, COURSES[0], SP1)`, checked by script. It contains the goal, has no {GOAL} slot, and has the Aim/Takes/Gives lines and the brief.
     - write-unit-SKILL.md and viz.py are identical to skills/write-unit/SKILL.md and kit/viz.py.
     - sourcing-standard.md holds the opening, Part 1 and Part 7 only, with 0 lines of Parts 2–6.
     - case-facts.md and bibliography.md are identical to the course's own files.
     - flags.txt is empty, since there are no flags.
     - It also holds course-map.txt (this course's 13 Aim/Gives lines).
     - There is no sources/ folder, no filed/ folder and no other course's case file.
   - **checker:** audit-units-SKILL.md, brief.txt (identical to the writer's), case-facts.md, notes.md, sources.md, sourcing-standard.md (Parts 1 and 7 only), unit.md, unsure.md.
   - **applier:** "1 findings". fixes.json reads {id f1, minor, style, §1, current "x", fix "z"}, with report.md and unit.md.
   - **filer:** hub.py (identical to the course's), case-facts.md, syllabus-flags.md, and index-rows.txt (the SP section plus its 13 rows). It also holds records.template.json, filer-rules.txt, notes.md, unsure.md, report.md, unit.md and an empty corrections/ folder.

9. PASS. All four stages worked (rc 0) for W-BW5.
   - **writer:** brief, case-academy.md, 13 filed BW units, sources/ (DD-B3 and its fresh check), and a sourcing standard with Parts 1–7.
   - **checker:** 7 files.
   - **applier:** 1 finding.
   - **filer:** includes 18 corrections reports.

10. PASS. The script printed "70 files, 0 private terms, 92 warnings: OK". The warnings are Portugal/ADHD terms in personal-brand files.

I changed nothing in the repository; git status is clean at d2d9b6c.

Verdict: PASS
