Checker: claude-opus-5-5. Corrections check (CP-5 second pass), 17 Nov 2026.

## Change 13
File: BW7-pipelines-raw-material-to-finished-output.md, Deliverable, conventions paragraph
Current:
````
File paths are this unit's naming, after BW4's Part 3 folders and BW5's `records/`; the case file names no paths.
````
Replacement:
````
File paths are this unit's naming, after BW4's Part 3 folders and BW5's `records/`; the paths of the case's own that the case file names (`docs/courses-index.md`, `docs/method.md`, `docs/CHANGELOG.md`, `docs/project-instructions.md`, `courses/building-with-ai/` and files under `audits/building-with-ai/`; Academy case file header, §1, §2, §5) are not used here.
````
Result: PASS - Current occurs once (BW7 line 256). A script over case-academy.md finds exactly these paths and no other: header line 3 "(`docs/courses-index.md`, `docs/method.md`, `docs/CHANGELOG.md`, ...)"; §1 line 122 "this course's folder is courses/building-with-ai/" (also 127, 134, 139); §1 line 201 "their equivalents are `docs/courses-index.md` (the index), `docs/project-instructions.md`"; §2 line 140 "(audits/building-with-ai/syllabus-review-BW-1-records.md)"; §5 line 135 "audits/building-with-ai/fresh-check-BW1.md to fresh-check-BW9.md". Section attributions correct. The Deliverable (lines 252-466) uses only its own paths (`briefs/<course>/`, `packets/<code>/`, `checks/`, `records/`), none of the case's, so "not used here" holds for the Deliverable; the case's audits/ paths appear only in the unit's correction footers (lines 504-512), outside the paragraph's scope. The old claim "the case file names no paths" is contradicted by those lines, so the change is warranted. British spelling; no em dash.
Syllabus: no conflict: F124 item 5 (names BW7's "the case file names no paths"), F53, F63, BW7 brief; consistent with BW8 Deliverable conventions (line 253, its paths are BW4's and BW7's proposals, the case's own named per §1) and BW5 line 295; DD-BW2, DD-BW3 make no path claim.

## Change 15
File: BW5-specifying-a-project.md, §9, "Choosing the boundary"
Current:
````
Academy runs a sample audit every four units (Academy case file §2), which gives a natural boundary. The case file records the method's backlog and proposal rules; it does not record a separate flag mechanism, how often the spec of a course changed, or at which points it was reviewed.
````
Replacement:
````
The method of Academy sets a sample audit every four units (Academy case file §2), a natural boundary; audits 3 onward had not run at 11 Nov 2026, and on 15 Nov 2026 the owner retired the four-unit audit (§9). Beside the method's backlog and proposal rules, the case file records a flag mechanism for this course: a chat that writes a unit raises a flag for each contradiction between units or briefs and each need the syllabus does not meet, and a flag that would change a brief waits for a syllabus review that the owner confirms, with no fixed date set; at 16 Nov 2026 none of 34 flags had been resolved by such a review (§2). It records syllabus reviews on 3 Nov 2026 (the UX course) and 17 Nov 2026 (this course) (§2), and not how often the spec of a course changed.
````
Result: PASS - Current occurs once (BW5 line 213). Supported: §2 line 21 "A sample audit every four units."; §9 line 113 "Audits 3 onward of the marketing, AI and UX courses had not run at 11 Nov 2026." (true of every audit at that date: the public marketing course's audits ran 14-15 Nov, line 154); §9 line 218 "on 15 Nov 2026 the owner closed that stage, retired the four-unit audit"; §2 line 116 "a chat that writes a unit raises a flag for each contradiction between units or briefs and each need the syllabus does not meet; a flag that would change a brief waits for a syllabus review that the owner confirms; the file sets no fixed date for a review. At 16 Nov 2026, before BW5's flags were added, 34 flags had been raised ... none had been resolved by a syllabus review."; §2 line 149 "the UX syllabus review ran on Fable 5.1 (3 Nov 2026)"; §2 line 140 "Added 17 Nov 2026 by this course's syllabus review (BW-1, row S-BW)"; §9 line 251 "no spec document". Note, not a failure: "none of 34 flags" drops line 116's "before BW5's flags were added"; the statement stays true (no review ran before 17 Nov), and DD-BW2 §4 line 45 keeps the qualifier. Consistent with BW5's own rule (line 183, the unit's synthesis) and line 241 (retired audit). British spelling; no em dash.
Syllabus: no conflict: F124 item 5 (BW5's flag-mechanism statements and the retired four-unit audit), F35, BW5 brief; agrees with DD-BW2 §4 line 45 and BW7 Part 1 line 265 (same retirement wording, case file §2, §9).

## Change 16
File: BW5-specifying-a-project.md, Deliverable Part 1f, closing sentence
Current:
````
The case file records proposals and the backlog-to-changelog move; it does not record a flag mechanism, so the Flags section is this unit's proposal.
````
Replacement:
````
The case file records proposals and the backlog-to-changelog move, and for this course flags raised for each contradiction between units or briefs and each need the syllabus does not meet, a flag that would change a brief waiting for a syllabus review the owner confirms (§2); the Flags section's place in the backlog and its row format are this unit's proposal.
````
Result: PASS - Current occurs once (BW5 line 390). Supported: §2 line 24 "a finished row moves to the changelog; a task the work uncovers is added as a proposed row and is not worked until the owner confirms it"; §2 line 116 "Syllabus flags (this course's syllabus-flags file): a chat that writes a unit raises a flag for each contradiction between units or briefs and each need the syllabus does not meet; a flag that would change a brief waits for a syllabus review that the owner confirms". The case keeps flags in a separate syllabus-flags file, so placing them as a Flags section of the backlog with this row format is rightly left as the unit's proposal. Agrees with Change 15. British spelling; no em dash.
Syllabus: no conflict: F124 item 5, F35, BW5 brief; agrees with DD-BW2 §4 line 45; BW7 lines 57, 272, 356 point to BW5 §9's rule and are unaffected.
