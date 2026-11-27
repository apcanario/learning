claude-opus-5-5

# Filer notes, W-SCE8 (27 Nov 2026): what the chat must do by hand

records.json written by out/make.py (json.dump). 8 case_lines, 16 flag_rows (F87 to F102), 4 flags_carried (F2, F62, F67, F71), 3 index_edits.

## Flag statuses to set by hand (the template inserts every new row as open)

1. F87 (the corrections to SCE1 and SCE7): set Status to
   `resolved (W-SCE8, 27 Nov 2026: 9 corrections to SCE1 passed and applied, audits/supply-chain-execution/corrections-2026-11-27-C-SCE8.md; 1 follow-on correction to SCE7 passed and applied, audits/supply-chain-execution/corrections-2026-11-27-C-SCE8-SCE7.md)`
   and delete the leading "RESOLVED in W-SCE8: " from its Flag cell if the chat prefers the plain form.
2. F84 (quality review of SCE8): set Status to
   `resolved (W-SCE8: reviewed 27 Nov 2026 by a fresh Opus 5.5 agent, keep, 0 error, 2 should-fix, 10 minor; report audits/supply-chain-execution/quality-review-SCE8-2026-11-27.md; 11 applied, f2 held and repaired as extra fix X1, plus X2 and X3, all applied)`.
   It is not in flags_carried, because flags_carried cannot set a row resolved.
3. F71's Flag cell: append `(Since W-SCE8, 27 Nov 2026, SCE1 rests the routing guide on Acocella et al. only.)` (F87's Proposed cell says so; flags_carried sets only its status).
4. F6, F64, F73, F75, F77, F54: left unchanged in their status cells; each has a new row with what remains (F88, F89, F90, F91, F92, F93). If the chat wants their status cells to point to the new rows, suggested wording: F6 `carried, partly met (W-SCE8: payment placed in the TMS by Gartner's glossary; how a carrier is paid still unsourced; remainder F88)`; F64 `open; carried (W-SCE8: remainder F89)`; F73 `open (W-SCE8: not met; F90)`; F75 `SCE8 part done and SCE1 corrected (F87); bibliography part open (F91)`; F77 `open (W-SCE8: partly; F92)`; F54 `open; decide before W-SCE9 (F93)`.

## Quality-review rows not raised (decide by the rule, kit/next_prompt.py --quality)

Counted from the Affects cells of F1 to F86 and F87 to F102 (excluding quality-review rows; all statuses; the same method gives SCE7's filer's 12, 6 and 10 for SCE8, SCE9 and SCE16): SCE9 8 (F85 exists), SCE10 24, SCE13 10, SCE16 15 (F86 exists), SCE17 16, DD-SCE1 6, DD-SCE2 5. SCE10, SCE13, SCE17 and DD-SCE1 are over 5 with no quality-review row; SCE10 and SCE17 were already over 5 before W-SCE7 and W-SCE7 raised none for them, so the rule's scope is not clear from the packet. I raised none; the chat raises them if the rule requires (form of F84 to F86).

## Unit text to fix before or at filing (same chat, the unit is not yet filed)

- Unsure item 6 (in unit.md's Unsure list and in unsure.md) still says "the current text of 49 CFR §371.3 was not read directly; the unit states only the agency's account". Since the quality-review applier's X1 and X2, section 4 and deliverable B row 10 cite §371.3 read in the Legal Information Institute's copy. Suggested replacement: "6. FMCSA's broker-transparency notice: whether the proposal became a final rule was not checked; 49 CFR §371.3 was read in the Legal Information Institute's copy, which shows no currency date." (Raised as part of F95.)
- The unit's "## Unsure list" section carries a stray line "claude-opus-5-5" and an H1 "# Unsure: SCE8" copied from unsure.md; check that the build renders it as the earlier filed units do.
- The fresh-check line ends the Unsure list ("fix · 1 errors"): "1 errors" is the line's form; it must match audits/supply-chain-execution/fresh-check-SCE8.md's verdict line.
- Source log (sources.md, not in the packet): add lines for the two addresses the quality-review applier opened and cited, both returned verbatim by WebSearch and opened 27 Nov 2026: govinfo FR Doc. 2024-27115 (https://govinfo.gov/content/pkg/FR-2024-11-20/pdf/2024-27115.pdf) and Cornell LII 49 CFR §371.3 (https://www.law.cornell.edu/cfr/text/49/371.3).
- kit/private_terms.py was run by no agent: it must run at the build (the dated vendor list in section 8, F1). The records name no vendor company.

## Counts and their sources

- Words: 13,044 from stats/1-writer.json (at hand-in); the unit after the fixes was not recounted by the stats script, so the records say "at hand-in".
- Sources: 24 entries in unit.md counted by script (stats: 23 at hand-in; the quality-review applier added 49 CFR §371.3; the govinfo address went into the existing FMCSA entry).
- Fresh check: report.md verdict line (fix, 1 error, 4 should-fix, 11 minor) and applier 1's notes (16 findings, 14 applied, 2 held, 3 extra fixes).
- Quality review: the chat's note in notes.md and applier 2's notes (keep, 0 error, 2 should-fix, 10 minor; 11 applied, 1 held, 3 extra fixes); "12 findings" is 11 + 1.
- Corrections: C-SCE8 summary "Passed 9 ... Failed 0. New 2" (9 includes the 2 new); C-SCE8-SCE7 "Passed: 1. Failed: 0. New: 0."

## Other

- The index status cell copies SCE7's row form; the staleness row is added after SCE6's (search on, written + six months: 27 May 2027), as file-unit §6 asks; the example (SCE7, search off) has none.
- Object: none (unsure.md); the page gets no relief, recorded under "None" by p96_uses.py.
- Publish identifiers: the records say "Published: see the row's close".
