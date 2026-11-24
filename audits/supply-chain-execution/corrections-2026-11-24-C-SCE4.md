Verdict: corrections W-SCE5 · 5 pass, 0 fail

Model: claude-opus-5-5. Checked 24 Nov 2026, live search. Every Current was counted in the packet file: each occurs exactly once. No replacement altered.

## Change 1
File: SCE2-inbound-and-storage.md
Current:
```
a **hold** is a status on stock that keeps it in the record but blocks it from being allocated to orders until someone releases it.
```
Replacement:
```
a **hold** is a status on stock that keeps it in the record but blocks it from being allocated to orders until someone releases it. SCE4 §3 sources the process for one regulated setting, US drug manufacturing, where incoming components, containers and closures are stored under quarantine until tested or examined and released by the quality control unit (21 CFR 211.82(b), 211.84(a)) [independent]; for other goods, and for finished stock in a distribution warehouse, this remains a working description.
```
Result: PASS. eCFR 21 CFR Part 211 (up to date as of 6/16/2026), §211.82(b): "Components, drug product containers, and closures shall be stored under quarantine until they have been tested or examined, whichever is appropriate, and released."; §211.84(a): "Each lot ... shall be withheld from use until the lot has been sampled, tested, or examined, as appropriate, and released for use by the quality control unit." (Quarantine is from 211.82(b); "quality control unit" is from 211.84(a); both cited together, so correct.)
Syllabus: no conflict. SCE2 brief lists "quality hold" in the inbound sequence; the replacement names the region (US), as the brief's Regions rule asks. Flags F23/F43 call for exactly this text. The sentence before it in §3.5 ("This unit opened no source that describes a quality hold as a process") stays true of SCE2 itself.

## Change 2
File: SCE2-inbound-and-storage.md
Current:
```
| Quality hold | A status that keeps stock in the record but blocks it from orders until released | Working description; not sourced |
```
Replacement:
```
| Quality hold | A status that keeps stock in the record but blocks it from orders until released | Working description; sourced for incoming components in US drug manufacturing in SCE4 §3 (21 CFR 211.82, 211.84) [independent] |
```
Result: PASS. Same source as Change 1: §211.82(b) "shall be stored under quarantine until they have been tested or examined ... and released"; the sections apply to components, drug product containers and closures.
Syllabus: no conflict (F43 item 1).

## Change 3
File: SCE2-inbound-and-storage.md
Current:
```
The assignment itself is **slotting**;
```
Replacement:
```
The assignment itself is **slotting** (the research literature's **storage assignment**: SCE4 §6);
```
Result: PASS. Bartholdi and Hackman, release 0.98 (revised 28 Aug 2017), §8.6 "Limitations of the fluid model", use "slot" for assigning SKUs to storage: "we slotted over 6,000 SKUs for a major chain retailer". The research term is confirmed independently: de Koster, Le-Duc & Roodbergen (2007) abstract, "We focus on optimal (internal) layout design, storage assignment methods, routing methods, order batching and zoning." (repub.eur.nl/pub/11877). The B&H PDF was read with WebFetch; a direct curl download was refused by the proxy. SCE4 §6 is not in the packet, so the cross-reference target was not opened.
Syllabus: no conflict (F43 item 2: SCE2's broad use stays; only a cross-reference is added).

## Change 4
File: SCE2-inbound-and-storage.md
Current:
```
| Slotting | Assigning SKUs to locations, including which go forward | Course term |
```
Replacement:
```
| Slotting | Assigning SKUs to locations, including which go forward | Course term; see storage assignment (SCE4 §6) |
```
Result: PASS. B&H 0.98 §8.6: "Figure 8.8 shows typical results of the more powerful model, applied in this example to slot SKUs in a bay of flow rack". That backs the broad definition, including which SKUs go forward. The storage-assignment term is backed as in Change 3.
Syllabus: no conflict (F43 item 2).

## Change 5
File: SCE1-the-map-the-words-and-the-evidence.md
Current:
```
Not searched here; the one candidate study's abstract could not be opened (source log).
```
Replacement:
```
Tested in SCE4 §10: no independent source opened there reports the share of warehouse records that match the shelf, at 99.9% or any other level; the one distribution-centre study (Kull et al. 2013, read in full in the author's version) measures inaccuracy as a percentage of each SKU's on-hand stock instead [independent]. A 2025 vendor infographic presenting WERC's 2025 report gives best in class for count accuracy by location as at or above 99.5%, no sample stated [vendor-reported]. Store studies found 31% to 65% of records wrong, on different definitions [independent].
```
Result: PASS. Each part was checked against a source opened by search:
- Kull et al. 2013, author's version (core.ac.uk/download/213060804.pdf). It defines IRI as "the relative discrepancy between the SIR and the actual inventory on-hand of a stock-keeping unit (SKU)". The data come from a DC serving a US apparel retailer. No overall record-accuracy rate (99.9% or other) is reported.
- Hyster-Yale infographic (yale.com YALE-1520_WERC-DC-Metrics-infographic.pdf, ©2025). It defines the measure as "The accuracy, by location, of the physical inventory compared to the reported inventory", gives best in class as ">=99.5%", attributes this to the "2025 ... WERC DC Measures Report", and states no sample.
- Store studies: DeHoratius & Raman (2008) abstract (IDEAS/RePEc) says "Examining nearly 370,000 inventory records from 37 stores of one retailer, we find 65% to be inaccurate". DeHoratius et al. (2023) MSOM (edoc.ku.de author copy) says "we see just 31% of the items at dm showing nonzero discrepancies". The ECR report (2019, orca.cardiff.ac.uk) gives 59.54% of audited SKUs, inside the range.
Syllabus: no conflict with the claim's content; it matches F42 item 4 word for word. Two minor points against the SCE1 brief, neither of which makes the text wrong, so the replacement is unchanged:
- "Links are given as links (the DOI address for a paper)". Kull et al. is named without https://doi.org/10.1111/jbl.12019, while the cell's neighbours (C1, C6) carry links. If the main chat wants to follow this line, write "Kull et al. 2013 (https://doi.org/10.1111/jbl.12019), read in full in the author's version".
- "Give a number in its source's own terms, with whose figure it is, the sample and the year". The 31% and 65% store figures appear without their studies or samples. The cell defers to SCE4 §10 for these, which is acceptable for a cross-reference cell.
