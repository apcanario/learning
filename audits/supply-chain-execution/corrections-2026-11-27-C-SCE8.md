claude-opus-5-5

Corrections check of SCE8's Contradictions list (two items), 27 November 2026. Target: SCE1 only. Both checked against their sources live.

## Change 1
Correction: Contradictions 1 (SCE1 §2 step 7: FreightLab citation that no longer opens, flag F75, with F71)
File: files/SCE1-the-map-the-words-and-the-evidence.md, section 2, step 7
Current:
```
For truckload freight (a vehicle dedicated to one shipper's shipment from origin to destination; Sheffi 2004, as SCE7 §2 cites it), MIT's FreightLab describes shippers buying carrier service through contracting, bidding and assignment, with the results held in electronic catalogues called routing guides (pricing, assignments and priority logic), and exchanges used when the catalogue fails ([MIT FreightLab, "Optimization Based Transportation Procurement", read 21 Nov 2026](https://freightlab.mit.edu/optimization-based-transportation-procurement)) [practice].
```
Replacement:
```
For truckload freight (a vehicle dedicated to one shipper's shipment from origin to destination; Sheffi 2004, as SCE7 §2 cites it), a shipper's annual bid produces a **routing guide** for each lane: a primary carrier and backup carriers in order, with their contract prices, and the spot market when the guide is exhausted (Acocella, Caplice & Sheffi 2020, as read in SCE7 §3) [practice].
```
Result: PASS. The FreightLab address, returned by a search in this agent, answered 302 Found with a redirect to ctl.mit.edu; not followed, so "not checked", as the correction says. Acocella, Caplice and Sheffi (2020), author's copy at sheffi.mit.edu (returned by search, opened 27 Nov 2026): "shippers typically run annual national bid events"; "The shipper typically selects the lowest bidding carrier with which to enter a contract"; the routing guide is "an ordered list of backup carriers that had responded to the shipper's RFP"; "the shipper continues down the routing guide until one of the backup carriers accepts the load"; "If the routing guide fails, the shipper must turn to the spot market." Matches SCE7 §3, which places the routing guide per lane. Acocella et al. 2020 is already in SCE1's Sources, so no Sources entry is needed.
Syllabus: no conflict. Follows F71 (credit the routing guide to Acocella et al., never to Sheffi 2004) and F75; agrees with SCE7 §3 and its tender cascade; no brief change. Note for the filer: SCE7's glossary row "Routing guide" still credits "SCE1 (MIT FreightLab)", which becomes out of date (a pointer, not a contradiction of content; SCE7 is not a target of this list).

## Change 2
Correction: Contradictions 1 (SCE1 deliverable B, glossary row Shipper)
File: files/SCE1-the-map-the-words-and-the-evidence.md, deliverable B, glossary row Shipper
Current:
```
| Shipper | The company whose goods are moved and which buys the carriage | MIT FreightLab [practice] |
```
Replacement:
```
| Shipper | The company whose goods are moved and which buys the carriage | SCE7 §1 [course term] |
```
Result: PASS. The FreightLab source cannot be opened (302, above); SCE7 §1 gives the same definition ("The company whose goods move and which buys the carriage"), so the source cell no longer points at an unopened page. SCE7 §1 credits that line to SCE1's glossary, so the pointer is circular; "course term" says so honestly, as SCE1 already does for Carrier.
Syllabus: no conflict. The definition text is unchanged and agrees with SCE7 §1 and §2's table.

## Change 3
Correction: Contradictions 1 (SCE1 deliverable B, glossary row Routing guide)
File: files/SCE1-the-map-the-words-and-the-evidence.md, deliverable B, glossary row Routing guide
Current:
```
| Routing guide | A shipper's catalogue of carrier assignments, prices and priority for its lanes | MIT FreightLab [practice] |
```
Replacement:
```
| Routing guide | A shipper's catalogue of carrier assignments, prices and priority for its lanes | Acocella et al. 2020 [practice] (SCE7 §3) |
```
Result: PASS. Acocella et al. (2020), author's copy: the routing guide is "an ordered list of backup carriers that had responded to the shipper's RFP", after a primary that is "the lowest bidding carrier", with prices "set and held exclusively and privately between shippers and carriers". Assignments, prices and order (priority) are all there.
Syllabus: no conflict. Same source and grade as SCE7's glossary row and SCE1's Tender row.

## Change 4
Correction: Contradictions 1 (SCE1 Self-check 4)
File: files/SCE1-the-map-the-words-and-the-evidence.md, Self-check, question 4 (question and answer lines)
Current:
```
4. **What does a routing guide hold, according to MIT FreightLab?**
   Pricing, carrier assignments and priority logic from the shipper's procurement, with exchanges used when the catalogue fails (section 2).
```
Replacement:
```
4. **What does a routing guide hold?**
   For each lane, the primary carrier and backups in order with their contract prices; the spot market is used when the guide is exhausted (section 2; SCE7 §3).
```
Result: PASS. Agrees with Change 1's text and with Acocella et al. (2020): "the shipper continues down the routing guide until one of the backup carriers accepts the load"; "If the routing guide fails, the shipper must turn to the spot market." The correction gave the question and answer on one line; split here into the file's two-line form, wording unchanged.
Syllabus: no conflict. Agrees with SCE7 Self-check 3.

## Change 5
Correction: Contradictions 1 (the MIT FreightLab entry leaves SCE1's Sources)
File: files/SCE1-the-map-the-words-and-the-evidence.md, Sources
Current:
```
- MIT FreightLab, MIT Center for Transportation & Logistics. "Optimization Based Transportation Procurement". Undated. https://freightlab.mit.edu/optimization-based-transportation-procurement
- Scriven, R. (Interact Analysis).
```
Replacement:
```
- Scriven, R. (Interact Analysis).
```
Result: PASS. After Changes 1 to 4 SCE1 cites FreightLab nowhere (grep: its other occurrences are the four passages changed above and the figure caption, fixed in New 2), so under Part 1 ("nothing is listed that it does not cite") the entry goes.
Syllabus: no conflict. Closes F75 for SCE1 once filed; the bibliography's own FreightLab line is the Needs list's business, not this one.

## Change 6
Correction: Contradictions 2 (SCE1 deliverable B, glossary row Third-party logistics provider (3PL), Working definition cell)
File: files/SCE1-the-map-the-words-and-the-evidence.md, deliverable B, glossary row Third-party logistics provider (3PL)
Current:
```
| Third-party logistics provider (3PL) | A company that runs warehousing or freight for other companies | Bartholdi & Hackman §1.2 [practice] |
```
Replacement:
```
| Third-party logistics provider (3PL) | A company that runs warehousing or freight for other companies; textbooks differ on whether it must own the assets (Rodrigue, 6th ed., ch. 7, defines a 3PL as an asset-based company and a 4PL as a non-asset-based provider that mainly provides organisational expertise) [practice] | Bartholdi & Hackman §1.2 [practice] |
```
Result: PASS, as repaired. Rodrigue, *The Geography of Transport Systems*, 6th ed., ch. 7 "Trade, Logistics and Freight Distribution", §7.4 page "Key Drivers for Third and Fourth Party Logistics Providers" (returned by search, opened 27 Nov 2026): "A third-party logistics provider (3PL) is an asset-based company that offers logistics and supply chain management services"; 4PLs "are non-asset based, meaning that they mainly provide organizational expertise." Repair: the proposed "restricts the term to asset-based providers and calls non-asset ones 4PLs" stretches the source, which says 4PLs are non-asset based, not that every non-asset provider is a 4PL (the page also says "about 75% of all the 3PLs are also offering 4PLs services"); the replacement now states only what the page says, and adds the grade tag the course requires. The correction's own sentence that Tandric's freight desk is "a 4PL in freight" is not carried into SCE1, rightly.
Syllabus: no conflict. Not a brief change; SCE1 §5's sentence on 3PLs (the company to which another outsources warehousing) stays true; the register calls Tandric (fictional) a logistics provider that runs warehousing and a freight desk with no trucks, and the replacement names no case company; agrees with SCE8's glossary row 4PL (Rodrigue, ch. 7 [practice]).

## Change 7
Correction: Contradictions 2 (Sources entry for Rodrigue, which SCE1's Sources lacks)
File: files/SCE1-the-map-the-words-and-the-evidence.md, Sources (alphabetical, before Scriven)
Current:
```
- Scriven, R. (Interact Analysis).
```
Replacement:
```
- Rodrigue, J.-P. *The Geography of Transport Systems*, 6th edition. Routledge, 2024. ISBN 9781032380407. Chapter 7, "Trade, Logistics and Freight Distribution", §7.4, page "Key Drivers for Third and Fourth Party Logistics Providers". https://transportgeography.org/contents/chapter7/logistics-freight-distribution/3pl-4pl-logistics/ (the author's online text of the edition; opened by SCE8, 27 November 2026)
- Scriven, R. (Interact Analysis).
```
Result: PASS. Publisher's record (Routledge product page, returned by search, opened 27 Nov 2026): title "The Geography of Transport Systems", author Jean-Paul Rodrigue, 6th Edition, Routledge, copyright 2024 (released 29 April 2024), ISBN 9781032380407; chapter 7 "Trade, Logistics and Freight Distribution". The page's own labels: Sixth Edition, Chapter 7, "7.4 – Logistics and Freight Distribution". SCE8's source log row 20 records the reading. Place of publication left out: the publisher's page read gives none.
Syllabus: no conflict. Same reference as SCE8's Sources; no new source beyond the one the correction cites.

## New 1
Correction: follows from Change 7 (SCE1 Sources lead-in line counts the entries opened by later units)
File: files/SCE1-the-map-the-words-and-the-evidence.md, Sources, lead-in line
Current:
```
All addresses opened on 21 November 2026, except the four entries marked as opened or read by SCE6 and the four marked as opened by SCE7, all on 24 November 2026, whose reading SCE6's and SCE7's source logs record; the source log gives what was read at each of the others.
```
Replacement:
```
All addresses opened on 21 November 2026, except the four entries marked as opened or read by SCE6 and the four marked as opened by SCE7, all on 24 November 2026, whose reading SCE6's and SCE7's source logs record, and the one marked as opened by SCE8 on 27 November 2026, whose reading SCE8's source log records; the source log gives what was read at each of the others.
```
Result: PASS. Without it the lead-in says every other entry was opened on 21 November, which the Rodrigue entry (27 November) would make false. Removing FreightLab (opened 21 November) leaves the counts of SCE6 and SCE7 entries unchanged.
Syllabus: no conflict. A record line only.

## New 2
Correction: follows from Change 1 (the figure caption in section 2 credits the "routing guide" note to FreightLab)
File: files/SCE1-the-map-the-words-and-the-evidence.md, section 2, caption of the flow figure "One order, promise to delivery"
Current:
```
ch. 4, and MIT FreightLab's procurement page (read 21 Nov 2026)."}
```
Replacement:
```
ch. 4, and Acocella, Caplice and Sheffi (2020), as read in SCE7 §3."}
```
Result: PASS. Once Change 1 is applied, the figure's "routing guide" note rests on Acocella et al. (2020) in section 2's text; the caption must say where its data comes from (Part 1), and a caption naming a source the unit no longer cites would also break "nothing is listed that it does not cite". Same quotation as Change 1: the routing guide is "an ordered list of backup carriers that had responded to the shipper's RFP".
Syllabus: no conflict. Caption only; the figure's steps and labels are unchanged.

## Summary
Passed 9 (Changes 1 to 7, New 1 and 2; Change 6 as repaired). Failed 0. New 2.
For the filer, outside this list's targets: SCE7's glossary row "Routing guide" still names "SCE1 (MIT FreightLab)" in its source cell, and F71's text says SCE1 rests the routing guide on FreightLab; both go out of date once these changes are filed and need their own backlog row (SCE7 is a filed unit; this check changes nothing in it).

## Could not verify
- MIT FreightLab, "Optimization Based Transportation Procurement": 302 redirect to ctl.mit.edu; not followed, not checked (as the correction states).
- Nothing else: Acocella, Caplice & Sheffi (2020, author's copy), Rodrigue's 3PL/4PL page and Routledge's product page were all opened.
