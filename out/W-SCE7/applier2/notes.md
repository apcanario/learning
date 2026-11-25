claude-opus-5-5

# SCE7 applier notes, 25 Nov 2026

Counts: 17 apply, 2 hold (f5, f8, both repaired as extra fixes). 5 extra fixes (X1 to X5), all apply. Every `current` of fixes.json occurs once in unit.md. Applying the 17 findings and then X1 to X5 in order in memory: each extra `current` occurs once at that point and none overlaps a finding's text. No fix text has an em or en dash.

Checked live under the web rule (search first, fetched only addresses those searches returned): Eurostat news 10 Dec 2021 (no haulier, carrier or 3.5 t); road_go metadata ("a sample of hauliers"; under 3.5 t excluded; last updated 22 July 2026); CMR Art. 30(1) (consolidated text, jus.uio.no); FMCSA detention page (no "free time" or "agreed"; updated 3 Oct 2025); ICAO 2024 revised limits (26 SDR from 28 Dec 2024); Montreal Convention Art. 4 (EUR-Lex); Sheffi (2004) author's copy (no "routing guide"); 49 U.S.C. §13102 (Cornell copy). Filed units checked: SCE1 §3, matrix, Self-check 5 and glossary; SCE2 §3.1, §3.2 and flow maps; SCE3 §8 and deliverable C; SCE6 row 26. case-facts.md is not in the packet; register facts were checked as the filed units report them.

## Holds

- f5 (should-fix, coverage): the problem is real. The fix sends each missing measure to section 11, which defines measures but does not assign them to steps, and leaves out the missing system entries (steps 5 and 12). Repaired as X1, which points to section 10 (failures, all twelve steps), section 11 (definitions) and the deliverable maps (party, system touchpoint, measure, or "none sourced").
- f8 (minor, figure): the problem is real. The fix credits Sheffi (2004) for "routing guide", but the paper does not use the phrase (author's copy, checked live). §3 sources the routing guide to Acocella, Caplice and Sheffi (2020) only. Repaired as X2 without Sheffi.

## Could not verify, and the flags that name unit text

- ATRI 16.7% stated as 2024: the unit does not do this. §13, Self-check 8 and unsure item 9 already say the release states no year. No unit entry needed. The error is in the source log: sources.md row 17 reads "empty miles average 16.7% in 2024; §11 cost per mile 2024". The unit gives $2.336 in 2025 from the 15 Jul 2026 release (Sources entry for the 2026 release, §11). The filer should correct sources.md row 17: no year for 16.7%, and cost per mile 2025, from the 2026 release (row 18 or whichever row holds it). The log also puts the ICAO and 1978 Protocol rows under the "not opened" heading, as the report says; the filer should fix that too.
- §13 ATRI 2026 report excerpt had no empty-mile figure: the claim is about what the writer read, so it cannot be checked. A live search found the 2026 release and trade coverage (truckinginfo) that mention more deadhead miles but give no share. Nothing contradicts the unit, and it already words this as a limit. No entry.
- §13 "A later Eurostat news item could not be opened": the writer's claim cannot be checked, and the fresh check found later items (2023, 2024) that give no empty share. Restated as X3. The Statistics Explained "journey characteristics" page did not return the article (main page only), so it was not checked. At the staleness check, look for a newer empty share.
- §12 CSCMP year: the unit already says the page does not state the year. No entry.
- §6 steps 9 and 11, 49 CFR 377 current text: the unit already says "Whether the current text is the same was not checked". The checker found that the Cornell copy matches, with no amendment after 1997. No entry. The unit could drop the caveat after an eCFR read.
- §1 §13102 amendments after 2019: verified. The Cornell copy (live) gives (2), (8), (14) and (15) as the unit uses them, and the latest amendment is 2008 (Pub. L. 110-244 and 110-291), before the 2019 edition. No entry.
- §6 step 5 and §9 Bartholdi and Hackman via SCE2: verified against filed SCE2 §3.2 (30-minute windows; appointment scheduling among the basic WMS features, §4.3). No entry.
- §6 step 1 and §10 Kim via SCE3 §8: §6 step 1 verifies. In §10 row 1, the failure was attributed to Kim, while SCE3 §8 gives the missed cut-off as its own working description with no source. Narrowed in X4.
- §2 WCTR peer review and §6 step 7 IFTSTA as UN/EDIFACT: the unit already states both as unconfirmed. No entry.
- Owner check (kit/private_terms.py): this is not unit text. It was not run, and it is not in the packet.
- X5 (outside the report's list, same contradiction as f4): §5 said "SCE1's working placement of settlement in the ERP". Filed SCE1 places the settlement check in the TMS and keeps only payment in the ERP as a working placement. Changed to "payment".

## For syllabus flags

- No held error or should-fix stays unrepaired: f5 and f8 are carried by X1 and X2.
- Carried from the report and still open: where tendering sits is a working placement and needs a source (SCE1, SCE7, SCE8, SCE10). Whether the vendor rule covers real service providers such as Penske Logistics, named as the CSCMP report's presenter (SCE7, SCE16). SCE7 should be search-on for its staleness check (Gartner definition, eFTI dates, 49 CFR 377 and §13102 currency, CSCMP, ATRI and Montreal figures, and a newer Eurostat empty share) (SCE7). The writer's Needs 1 to 7 stand: European invoicing, payment, spot or contract source; freight-audit study; association measure definitions; ocean and intermodal sources (SCE7, SCE8, SCE10, SCE16).
- New, minor: SCE1's §2 step 7 and its intro cite "Sheffi 2004, as SCE7 §2 cites it" for truckload, which is correct. The routing guide in SCE1 rests on MIT FreightLab and Acocella et al., not on Sheffi (2004). Later units should not credit the routing guide to Sheffi (2004) (SCE8, SCE10).
