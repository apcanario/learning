claude-opus-5-5

# Applier notes: SCE7 · Transportation in practice (25 November 2026)

All 18 finding `current` strings occur exactly once in unit.md (checked by script). Findings f1 to f18 applied in memory in order, then X1 to X10: each X `current` occurs once at its point and overlaps no applied finding (out/build.py; result in out/unit-preview.md, for checking only).

## Decisions
- Apply: f1 to f6, f8 to f18 (17).
- Hold: f7 (1). The finding is right: the UN Treaty Collection status page (searched and fetched 25 Nov 2026) gives the Protocol to the CMR, adopted at Geneva on 5 July 1978, in force 28 December 1980, adding paragraphs to Art. 23. The fix names the status page with no link and no Sources entry. Repaired as X1 (same wording, linked, graded independent) with X2 (Sources entry).

Checks made at source (all search-returned addresses, fetched 25 Nov 2026):
- f3: Acocella et al. author's copy, Table 6: tender lead time (TLT) not significant in the tight market (nor in the soft, Table 5); the text names the significant tight-market behaviours without it.
- f4: ICAO 2024 revised limits: Art. 22(3) row reads 17, 22 (from 28 Dec 2019), 26 (from 28 Dec 2024). The page does not say "per kilogram"; the fix wording does not state the unit for 26 SDR, which is right.
- f8, f9: ATRI 1 July 2025 release attaches no year to the 16.7%; only the cost figure is tied to 2024.
- f10, f11: Sheffi (2004) has no "backhaul"; it has "back-and-forth movement" and the closed loop.
- f12: Chalmers record: studies in the English and Scandinavian languages after 1990, plus non-peer-reviewed Scandinavian reports.
- f18: DOI 10.1287/inte.1040.0075 printed on the author's copy.
- f13: case-facts.md and notes.md are not in this packet; applied on the report's citation of the writer's own note, since the fix only weakens the label.

## Could not verify list
1. Gartner definition tail "multimodal sourcing, planning and execution of the physical transport of goods": verified verbatim on the Gartner page. No entry.
2. Gartner planning list and analytics: verified. Planning reads "order and shipment consolidation, mode selection, route determination and carrier selection"; analytics names "on-time performance; emissions calculations; and costs by mode, customer, product line and location". The unit's paraphrase ("measures such as on-time performance and cost by mode") is faithful. No entry.
3. §6 step 7 "UN/EDIFACT's IFTSTA": the GS1 page gives "REFERENCE DIRECTORY : D.01B" and the functional definition, but does not say UN/EDIFACT. The EANCOM Part I page that might say so was refused by the harness: not checked, not retried. Marked unverified in §6 step 7 (X3), §7 table (X4) and the glossary (X5).
4. ICAO 26 SDR "per kilogram": the page does not say per kilogram; the f4 wording avoids the unit. No entry.
5. Laporte issue 4: verified on the IDEAS/RePEc record (Transportation Science 43(4), 408-416, DOI 10.1287/trsc.1090.0301). No entry.

## Flags and contradictions naming unit text
- Writer's contradiction 4 (FTL under Sheffi): X6 marks "FTL Europe" as a working term in the glossary row, in line with §2. The SCE1 replacement row itself is outside this packet.
- CSCMP measurement year: §12 already says the page does not state it. No change.
- X12 and UN/EDIFACT regional use: the unit already says not sourced. No change.
- Montreal limits and CMR 1978 Protocol: handled by f4 to f6 and X1, X2, X9.
- X7, X8 keep the opening note and Sources intro true, as two sources were opened on 25 Nov 2026. X10 brings the Unsure list in line with f8.

## Not done here
- sources.md (writer's log) should get two rows: ICAO 2024 revised limits (address as in f6; read: Art. 22 table, 17/22/26 SDR, effective 28 Dec 2024; 25 Nov 2026) and the UN Treaty Collection status page (address in X1; read: Protocol title, adoption 5 July 1978, entry into force 28 Dec 1980, Art. 23 amended; 25 Nov 2026). This packet is read-only outside out/.

## Should become syllabus flags
- Montreal Convention limits are revised every five years (Art. 24); current cargo limit 26 SDR from 28 Dec 2024. Affects SCE7 (fixed), SCE8 and any later unit on air carriage or documents.
- CMR 1978 Protocol amends Art. 23 for its parties; its text, amount and parties are unread. Affects SCE7, SCE10.
- IFTSTA as a UN/EDIFACT message is unverified (only GS1's page read). Affects SCE7 and SCE10 (and any unit naming EDIFACT messages).
- SCE2's six flow-map columns "fixed for SCE3, SCE7 and SCE9" against SCE7's brief (Party, Document). Affects SCE2, SCE7, SCE9.
- CSCMP figures without a measurement year. Affects SCE7, SCE16.
No held error; the one hold (f7) is repaired by X1.
