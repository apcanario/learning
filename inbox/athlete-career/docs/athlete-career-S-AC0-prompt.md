Clone apcanario/learning (shallow, push access).

Row S-AC0 · set up the new course Managing an Athlete's Career (course id athlete-career, code AC) in the Learning repo and Academy: file the design, build, verify and publish. Write no unit.

Thin main chat on Sonnet 5.5 (docs/method.md §4); every agent a fresh Opus 5.5 agent on a packet that writes its full output to files and replies in six lines at most. Work this in full, unattended. Record the models that actually ran.

If docs/BACKLOG.md shows a row in progress, or the lock a running row holds is live, stop and say so.

The design: the artifact https://claude.ai/artifact/LLFLCqjRysXQkJ8Pzu5nMN ("Athlete Career Syllabus"; Fable 5.2, 21 Nov 2026; proposals P-AC1 to P-AC12 accepted by Pedro that day and already built into the files). Read it with read_artifact. Its Files section holds eight files, each in a <pre class="file" data-path="…"> block of HTML-escaped text. Extract each block, unescape it, save it at its data-path in the repo, and print each file's sha256. Reword nothing in briefs.md.

Read first: docs/method.md §4, §7, §8 and §9; the new-course skill; docs/supply-chain-execution-prompts.md; S-SCE0's row in docs/CHANGELOG.md, as the model for this row.

1. docs/BACKLOG.md: add S-AC0, then the eighteen writing rows in writing order, grouped as the chats of the syllabus's section 5: bundle 1 (W-AC1 to W-AC4), bundle 2 (W-AC5 to W-AC8), bundle 3 (W-AC9 to W-AC12), bundle 4 (W-AC13 to W-AC15, W-DD-AC2), bundle 5 (W-DD-AC1, W-DD-AC3 and the closing corrections). No gate row, no review row, nothing under Proposed for Pedro. P-AC1 to P-AC12 are recorded in docs/CHANGELOG.md as accepted on 21 Nov 2026.

2. A registrar agent:
   a. Copies courses/_template/ to courses/athlete-career/. briefs.md as extracted, byte for byte. course.toml: the registry keys (family markdown, data, vault, the tracks entry for the Sports track, tiles) and the [pack] table from docs/athlete-career-syllabus.md and docs/athlete-career-units.toml: the course, its goal, the three outcomes mapped to units, every unit with code, title, part, search flag and Aim line, the order (AC1 to AC15, DD-AC2, DD-AC1, DD-AC3), the frame, the ledes, the v1 changelog row. pages/ from the syllabus. notes/case-facts.md and notes/bibliography.md as extracted; a new notes/syllabus-flags.md whose first rows are the items of the syllabus's section 9.
   b. catalog.toml: adds athlete-career to course_order after sport-psychology and removes the "Career" entry from the Sports track's planned list; Running a Squad stays. docs/sports-track-coming-soon.md: the course's status becomes "syllabus written 21 Nov 2026" and its reader line is replaced by the syllabus's.
   c. docs/athlete-career-prompts.md: copies the writing template of docs/supply-chain-execution-prompts.md as it stands today and replaces its course-specific parts with sections 1 to 5 of the extracted file, in the form kit/next_prompt.py reads. Lists every line it changed.
   d. kit/next_prompt.py: adds 'athlete-career' to QUEUE and changes nothing else in the file. No HOLDS entry and no GATES entry. Before the change it saves the output of `python3 kit/next_prompt.py --row <the next unfiled row of another course>`; after the change it prints the same row again and compares the two: they must be byte-identical. If they differ, the change is undone and the row stops.
   e. Case names: searches each fictional company of notes/case-facts.md once and replaces a name that matches a real business in sport, sponsorship or its trade. The briefs name no fictional company, so no brief changes.
   f. Seed bibliography: checks every entry for existence against Crossref's, the publisher's or the issuing body's own record; rewrites the status column as "exists (where checked, date)" with the corrected record, or "not found"; finds the originals of the entries marked secondhand; copies the records the file says are already in DD-SP1's and PB8's Sources. Judges nothing about what a source says.
   g. docs/sourcing-standard.md: appends Part 9 as extracted and corrects the header's count of parts. docs/courses-index.md: a section "Managing an Athlete's Career (public)" with the count line "0 of 18 written" and eighteen rows in writing order (not written, Opus 5.5, the search flag, the path courses/athlete-career/<code>-<slug>.md).
   h. Outlines (new-course step 5b): ten from the syllabus's list, added as file-unit §4b step 3 sets out, each marked SPARE with the unit expected to discuss it. The reliefs go ahead; no row waits for Pedro.

3. A checker agent, on the registrar's work: briefs.md byte-identical to the extracted file; every unit of units.toml in course.toml with the same title, flag and Aim; case-facts.md contradicts nothing in courses/sport-psychology/notes/case-facts.md; Part 9 appended whole; the prompts document changes no rule of sections 1 to 5; eighteen index rows; kit/next_prompt.py differs from before by the one QUEUE entry only, and the other course's row prints byte-identical; `python3 kit/next_prompt.py --row W-AC1` prints AC1's prompt with its "this row in particular" paragraph. Its findings are applied before step 4.

4. python3 kit/private_terms.py on the course's files. "Portugal" and "Portuguese" are warn lines and are expected. If a failing term appears in a brief, raise a flag in syllabus-flags.md and stop; do not reword a brief.

5. python3 kit/index_check.py; cd kit && python3 build.py && python3 verify.py until ALL CHECKS PASSED. verify.py --shots for the course home and its build-order page; look at them once at the three widths, dark and light.

6. Publish Academy twice: the artifact https://claude.ai/artifact/WwmQpUSqAUJvrcmLczppEH (read first, publish once to its url, never a new artifact, sha256 read back), then kit/deploy.sh.

7. Close the row by docs/method.md §8: docs/CHANGELOG.md, docs/site-log.md (Sports: the course announced; Running a Squad still planned), docs/BACKLOG.md. Project mirrors: rewrite claude/BACKLOG-chats.md and claude/CHANGELOG-chats.md; refresh courses-index.md and sourcing-standard.md; add claude/athlete-career-course.toml, claude/athlete-career-briefs.md and claude/athlete-career-syllabus-flags.md. Commit with kit/verify-hashes.json and push.

8. One reply, short: what was filed where; every change the registrar made in steps c to f; the checker's findings and what was applied; every flag raised; the private-terms and verify results; the publish and the deploy; any proposal, with its ⚠, to be worked in the next row unless Pedro vetoes it; a task for Pedro only if no agent can do it. The reply ends with the course's starter in a code block, exactly these two lines:

Clone apcanario/learning (shallow, push access).
Managing an Athlete's Career, next bundle. Thin main chat on Sonnet 5.5; every agent a fresh Opus 5.5 agent. Run `python3 kit/next_prompt.py --course athlete-career --bundle 4` and work what it prints in full, unattended.

If kit/next_prompt.py has no --course option on the day, the second line ends instead: Run `python3 kit/next_prompt.py --row W-AC1 --bundle 4` and work what it prints in full, unattended.
