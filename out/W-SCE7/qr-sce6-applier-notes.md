claude-opus-5-5

# SCE6 applier notes, 24 Nov 2026

Every `current` in fixes.json occurs once in unit.md (checked by script). All findings, then extra fixes X1 to X7 in order, were applied in memory: each extra `current` occurs once at its point and none overlaps a finding's text. No fix contains an em dash.

Counts: 9 apply (f1 to f6, f9, f10, f12), 4 hold (f7, f8, f11, f13), each held finding repaired as an extra fix. 7 extra fixes in all (X1 to X4 repairs, X5 to X7 from the could-not-verify list).

## Checks made on review

- NIST SP 800-145 opened: "pooled to serve multiple consumers using a multi-tenant model" sits under the essential characteristic "Resource pooling"; the SaaS service model does not mention pooling or multi-tenancy. f1, f2 right.
- Gartner 2022 WMS Magic Quadrant reprint (dam.infor.com) opened: the five types sit under "Market Definition/Description". f4 to f6 right.
- filed SCE3 §§3.3, 3.6 and SCE5 §3; filed SCE4 §8 read for f7 to f9.
- case-facts.md is not in the packet; f3 and f10 were judged on the unit's own text (they only remove claims, and keep register facts the unit already states).

## Holds

- f7, f8 (W19 and deliverable B row 19): problem real (lights are taught in SCE5 §3, not SCE3), but the fix drops SCE3 §3.3, which teaches sort-while-pick, the "sort" of this step. Repaired as X1, X2: "(SCE3 §§3.3, 3.6; SCE5 §3)", the pattern W18 uses.
- f11 (fictional vendors on Gartner's types): the fix sets out to use Gartner's type names but writes "application vendors"; the type is "Application mega vendors". Repaired as X3.
- f13 (deliverable C blanks): the fix covers rows 2 to 29 but not the four bare blanks of the "new" row. Repaired as X4.

No hold is an error or should-fix left unfixed; all three should-fix findings were applied.

## Could not verify list

1. Michel (MMH), section 10 quotations, byline, address with "/software_tech": a search returned the article at a bare address; that fetch was refused (not retried, no copy used). Search confirms an MMH article of that title exists. Marked unverified in the unit (X6).
2. Gartner document 7780053 as the 2026 report: search returned it, titled only "Gartner Magic Quadrant Abstract"; the fetch was refused. Handled by f12 in section 8; Sources entry brought in line (X7).
3. Section 2 inclusion rules "a share of revenue or customers outside the vendor's home region": verified in the reprint (greater than 10% of WMS revenue "and/or" greater than 10% of customer base outside the home region). No change. The unit's Unsure item 2 could now be dropped.
4. Section 3 "dedicated or multitenant cloud SaaS": verified in the reprint as the example inside the bullet "Cloud architecture and deployment model options (e.g., dedicated or multitenant cloud SaaS)" under WMS Market Considerations, a topic that affects positioning. Wording made exact (X5).
5. Section 1 "and potentially RFID": verified on the Peer Insights page ("bar codes and potentially RFID or other scanning/sensing technologies"). No change.
6. B&H §4.6.1 phrasings: verified in the PDF. "The working life of a warehouse management system is generally greater than that of the computer language", "an accretion of many different computer languages", "hard to maintain or customize"; the client "or more likely a consultant" "must choose the logic from among the modules provided, or else have the software customized". No change; the "read through a summary" notes in sections 1 and 4 and Unsure item 4 are now stricter than needed.
7. Light DOI 10.1002/smr.240: not resolved at the publisher (a DOI-path viewer returned an empty page). The DOI is given by the Utah index and appears in other search listings for the article. Already marked in the unit's Unsure item 6. No change.
8. Source log: not in the packet. Noted, not fixed.

## Syllabus flags

None needed: no error or should-fix is held. Open owner flags F53 and F54 stand as the report describes (X3 only makes F53's wording use Gartner's type names).
