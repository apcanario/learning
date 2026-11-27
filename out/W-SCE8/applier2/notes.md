claude-opus-5-5

# SCE8 applier notes (27 November 2026)

Findings: 11 apply, 1 hold. Extra fixes: 3 (X1 to X3), all apply. Every `current` was counted by script against unit.md and again after applying the findings in order, then the extra fixes in order: each occurs exactly once, and no extra fix overlaps an applied finding's text.

## Holds

- f2 (Deliverable B, row 10). The problem is real: the FMCSA notice the cell cites does not set out what the current record must contain. But the fix would leave the unit saying the contents were not read. I read 49 CFR §371.3 live (Legal Information Institute copy, returned by search): (a) the record of each transaction must show the consignor, the originating carrier, the bill of lading or freight bill number, the broker's compensation and who paid it, non-brokerage services and their compensation, and any freight charges collected with the date paid to the carrier; (c) each party to a brokered transaction may review it. Repaired as X1, with X2 adding the Sources entry.

## Could not verify: what was done

1. §1 Peer Insights TMS, same opening sentence and mandatory list: verified live (gartner.com market page; "Updated April 2026"; seven mandatory features including settlement). No change.
2. §9 92 products, no total review count: verified live ("Products 1 - 20 of 92"; only per-product rating counts). No change.
3. §9 product descriptions' tendering, audit and payment claims: verified live (descriptions quote load tendering, freight auditing and payment; automate tendering). No change.
4. §1 Gartner abstract page failing: consistent with the unit's own statement; nothing to verify. No change.
5. §2 rest of the VRS definition: fetch failed (client error), not retried, not fetched from a copy. Marked unverified (X3).
6. §2 GTM beside WMS and TMS (SCE1 §4): verified against filed SCE1 §4. No change.
7. §3.2 dispatcher "radio, phone or computer": verified live on O*NET 43-5032.00 ("Duties may include using radio, telephone, or computer to transmit assignments and compiling statistics and reports on work progress"). No change.
8. §3.3 ANSI accreditation: no source; cut by finding f12 (applied).
9. §5 990 and IFTSTA: verified against filed SCE7 §6, steps 3 and 7, including SCE7's unverified UN/EDIFACT status. No change.
10. §3.3 and card 3, 81.9% and 68.5%: verified against filed SCE7 §4. No change.
11. §4 49 U.S.C. §13102(2): verified against filed SCE7 §1 (2019 edition as SCE7 read it). No change.
12. §4 whether the FMCSA proposal became final: the unit already says this was not checked; a search returned press items only, none opened. No change; carry to flag.
13. Sources, 3PL study subtitle: verified live on the study PDF ("Navigating Change: Insights Into Evolving Dynamics in Supply Chain", 29th Annual Study). No change.
14. Sources, Rodrigue §7.4 overview page: verified live (title "7.4 – Logistics and Freight Distribution", author Rodrigue, links "Key Drivers for Third and Fourth Party Logistics Providers"; 3PL asset-based, 4PL non-asset-based). No change.
15. §4 Evangelista published version against manuscript: the DOI redirected to Emerald; not followed, not checked. The unit already says the author's manuscript was read, so no claim rests on the published version. No change.
16. "Listed in the notes": the filed SCE3 and SCE4 use the same convention for the writer's notes to the main chat (register additions and assumptions), so the pointers follow course practice. No change; the main chat should see that the notes exist and carry the three items (payment placement, F6; Olu as analyst; the core's assumed shipment plan).
17. private_terms.py: not in the packet, not run.

## For the filer

- Source-log lines are needed for two new addresses in the unit: govinfo FR Doc 2024-27115 (f10) and Cornell LII 49 CFR §371.3 (X1, X2). Both were returned verbatim by WebSearch and opened 27 November 2026 by this agent.
- Not a hold, but note: f7 and f11 are style fixes; f1 changes the §7 count from three to six.

## Possible syllabus flags

- New (from the report, narrowed): whether the 2024 broker-transparency NPRM (FMCSA-2023-0257) became final was not read; the current §371.3 contents are now read. Affects SCE8 §4 and deliverable B row 10, DD-SCE1 and any unit on brokers.
- F73 carries forward with the 10th edition (ISBN 9780357908549) now noted. Affects SCE7 §6, SCE8 §1, SCE10, SCE13.
- VRS definition wording unverified (X3). Affects SCE8 §2 and SCE10 if it reuses the definition.
- No held error or held should-fix remains open: f2 is repaired by X1.
