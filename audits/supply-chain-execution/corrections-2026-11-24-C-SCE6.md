claude-opus-5-5

Corrections check of C-SCE6-1 to C-SCE6-3 (target: files/SCE1-the-map-the-words-and-the-evidence.md), 24 Nov 2026. I counted every Current by script (python3, str.count) in the packet's SCE1 file, and each occurs once. I also applied the whole sequence (Changes 1 to 5, then New 1 and 2) in memory, and each Current still occurred once when its turn came.

## Change 1
Correction: C-SCE6-1
File: files/SCE1-the-map-the-words-and-the-evidence.md, §11 table, row C8
Current:
```
| C8 | Cloud software means no more upgrades. | Not searched here. | SCE6 |
```
Replacement:
```
| C8 | Cloud software means no more upgrades. | Tested in SCE6 §10: no source opened says upgrades end in the cloud. NIST's definition of SaaS (SP 800-145, 2011) leaves the customer no control of the underlying infrastructure or of individual application capabilities, apart from limited user-specific application configuration settings [independent], so the upgrade moves to the provider (inference); Gartner's 2022 WMS Magic Quadrant, read in a reprint, says service affects "upgrade cycles and TCO", calls multitenant against dedicated cloud a continuing debate, and says some vendors' microservices architecture "allows continuous upgrades" [analyst]; an ERP review finds SaaS often limits deep customisation and that customisation has shifted to interfaces and integrations (Abendroth et al. 2024) [independent], and Light (2001, abstract only) found that a customisation needs careful consideration for its potential impact on future maintenance [independent]. No independent source found for the claim. | SCE6 |
```
Result: PASS, with four wording repairs so the cell says no more than its sources and SCE6 §10. (1) NIST SP 800-145, section 2: "The consumer does not manage or control the underlying cloud infrastructure including network, servers, operating systems, storage, or even individual application capabilities, with the possible exception of limited user-specific application configuration settings." The standard does not itself say that the provider controls the application, so the proposed "gives the provider control of the application" now says what NIST says (SCE6 §3 quotes the same sentence). The move to the provider stays marked as inference. (2) Gartner, Magic Quadrant for WMS, 1 June 2022, G00755323 (S. Tunstall, D. Klappich, R. Narang), reprint: service contributes to implementation success and customer satisfaction, "as well as impacting upgrade cycles and TCO"; "there remains a continuing debate among vendors and buyers on whether multitenant SaaS is demonstrably better than dedicated cloud"; Market Overview: some vendors have "rewritten their WMS using a microservices architecture that allows continuous upgrades and extensibility". This part holds as proposed. (3) Abendroth et al. 2024: "Cloud-based ERPs, especially SaaS solutions, often have limited opportunities for deep customization"; abstract: "a shift from ERP code modification in on-premises systems to interface and integration customization in cloud ERP systems". I restored "often". I replaced "moves it to interfaces" with wording close to SCE6 §10, because the review reports a shift over 20 years of studies, not something SaaS does. (4) Light 2001, abstract (Salford repository): "careful consideration is required to determine whether a customization is viable given its potential impact upon future maintenance". I restored "potential", as in SCE6 §10. The closing sentence gains SCE6 §10's "for the claim", so it does not seem to contradict the [independent] sources in the same cell.
Syllabus: no conflict. The change does what F2 (carried) and F42 item 4 route by correction. SCE1's brief asks for each claim "stated as it circulates and then set against its evidence", and C8 now is. It keeps "No independent source found", as F59 requires until SCE14 or SCE16 finds a measurement. No vendor is named, and the 2022 report is said to be read in a reprint (Part 8).

## Change 2
Correction: C-SCE6-2
File: files/SCE1-the-map-the-words-and-the-evidence.md, front matter intro, claims sentence
Current:
```
 C1, C2 and C10 are set against what was opened here, C4 against SCE4, and C3, C5 and C6 against SCE5; the other seven are marked "not searched here" with the unit that tests each.
```
Replacement:
```
 C1, C2 and C10 are set against what was opened here, C4 against SCE4, C3, C5 and C6 against SCE5, and C8 against SCE6; the other six are marked "not searched here" with the unit that tests each.
```
Result: PASS against the filed unit. After Change 1, §11 sets eight of the fourteen claims against evidence. SCE6 §10 ends "**No independent source found** for the claim". The rows still marked "Not searched here" are C7, C9, C11, C12, C13 and C14, which makes six. This change applies only together with Change 1.
Syllabus: no conflict. The count matches §11 after Change 1, and F2's carried note records this sentence change.

## Change 3
Correction: C-SCE6-3
File: files/SCE1-the-map-the-words-and-the-evidence.md, Sources, Abendroth inserted before Bartholdi & Hackman
Current:
```
- Bartholdi, J. J., III & Hackman, S. T. *Warehouse & Distribution Science*, release 0.98, revised 28 August 2017. Chapters 1, 3, 4 and bibliography. https://www2.isye.gatech.edu/~jjb/wh/book/editions/wh-sci-0.98.pdf
```
Replacement:
```
- Abendroth, A., Bender, B. & Gronau, N. (2024). The Evolution of Original ERP Customization: A Systematic Literature Review of Technical Possibilities. In *Proceedings of the 26th International Conference on Enterprise Information Systems (ICEIS 2024)*, vol. 1, 17–27. https://doi.org/10.5220/0012305500003690 (read at https://scitepress.org/Papers/2024/123055/123055.pdf; opened by SCE6, 24 November 2026)
- Bartholdi, J. J., III & Hackman, S. T. *Warehouse & Distribution Science*, release 0.98, revised 28 August 2017. Chapters 1, 3, 4 and bibliography. https://www2.isye.gatech.edu/~jjb/wh/book/editions/wh-sci-0.98.pdf
```
Result: PASS against the publisher's record (the SciTePress paper page and PDF; Crossref's record would not open). Authors: "Adrian Abendroth, Benedict Bender, Norbert Gronau". Title as given. Proceedings: "Proceedings of the 26th International Conference on Enterprise Information Systems - Volume 1: ICEIS". Pages 17-27; DOI 10.5220/0012305500003690; 2024. The PDF footer reads "Volume 1", while the page metadata says Volume 2; the printed footer and the citation both say 1, so "vol. 1" stands. The entry is the same as SCE6's apart from the added "opened by SCE6, 24 November 2026", which the correction's notes invite.
Syllabus: no conflict. Part 1 asks that every source a unit cites be listed, and Change 1 cites this one. F58 already lists it for the seed bibliography.

## Change 4
Correction: C-SCE6-3
File: files/SCE1-the-map-the-words-and-the-evidence.md, Sources, 2022 Gartner WMS report after the index entry
Current:
```
- Gartner. Magic Quadrant and Critical Capabilities index (no headline shown), read 21 November 2026. https://www.gartner.com/magic-quadrant
```
Replacement:
```
- Gartner. Magic Quadrant and Critical Capabilities index (no headline shown), read 21 November 2026. https://www.gartner.com/magic-quadrant
- Gartner. "Magic Quadrant for Warehouse Management Systems". S. Tunstall, D. Klappich, R. Narang. Published 1 June 2022, ID G00755323. Reprint, read by SCE6 on 24 November 2026. https://dam.infor.com/api/public/content/d8957bc1ac164bf1843965deeaa7e26a?v=d2e94df6
```
Result: PASS against the reprint, opened at the address the search returned, which lacks the ?v= query. It shows "Magic Quadrant for Warehouse Management Systems", "Published 1 June 2022", "ID G00755323" and the analysts "Simon Tunstall, Dwight Klappich, Rishabh Narang". The entry matches SCE6's.
Syllabus: no conflict, with one build check. Part 8 asks that an analyst report say how it was read, and "Reprint" does. Under F1, the reprint sits on a vendor's asset server. SCE1, like SCE6, gives the address only as where the report was read and names no host vendor in its text. kit/private_terms.py must still pass SCE1 at build.

## Change 5
Correction: C-SCE6-3
File: files/SCE1-the-map-the-words-and-the-evidence.md, Sources, Light and Mell & Grance inserted before Meyr, Wagner & Rohde
Current:
```
- Meyr, H., Wagner, M. & Rohde, J. "Structure of Advanced Planning Systems".
```
Replacement:
```
- Light, B. (2001). The maintenance implications of the customization of ERP software. *Journal of Software Maintenance and Evolution: Research and Practice* 13(6), 415–429. https://doi.org/10.1002/smr.240 (abstract, read at https://salford-repository.worktribe.com/output/1471899/the-maintenance-implications-of-the-customization-of-erp-software; opened by SCE6, 24 November 2026)
- Mell, P. & Grance, T. *The NIST Definition of Cloud Computing*. NIST Special Publication 800-145, September 2011. https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-145.pdf (opened by SCE6, 24 November 2026)
- Meyr, H., Wagner, M. & Rohde, J. "Structure of Advanced Planning Systems".
```
Result: PASS. Mell & Grance, checked against NIST's own PDF: "Peter Mell", "Timothy Grance", "The NIST Definition of Cloud Computing", "Special Publication 800-145", "September 2011". Light, checked against the University of Utah journal index, because the publisher's and Crossref's records would not open: author Ben Light; the title as given; "Journal of Software Maintenance and Evolution: Research and Practice"; volume 13, number 6, pages 415--429; November 2001; DOI 10.1002/smr.240. The Salford record gives the journal as "Journal of Software Maintenance: Research and Practice", with the same volume, issue, pages and year, and shows no DOI. Both entries match SCE6's Sources plus the added date.
Syllabus: no conflict. Part 1 is met, and F58 records the same references and the same Salford/Utah difference.

## New 1
Correction: C-SCE6-3
File: files/SCE1-the-map-the-words-and-the-evidence.md, Sources, opening line
Current:
```
All addresses opened on 21 November 2026; the source log gives what was read at each.
```
Replacement:
```
All addresses opened on 21 November 2026, except the four entries marked as opened or read by SCE6 on 24 November 2026, whose reading SCE6's source log records; the source log gives what was read at each of the others.
```
Result: PASS. This fixes a fault the correction would create. After Changes 3 to 5 the line would be false for four entries that SCE6 opened on 24 November 2026 (SCE6 Sources: "All addresses opened on 24 November 2026"), and SCE1's source log does not hold them.
Syllabus: no conflict. Part 8 says: "Every reference in Sources is in the unit's source log with the address opened, what was read and the date". The new line says which log holds these four. Alternatively, the owner could add the four entries to SCE1's source log, outside this packet.

## New 2
Correction: C-SCE6-1
File: files/SCE1-the-map-the-words-and-the-evidence.md, front matter intro, "Abstract-only claims" list
Current:
```
and de Koster et al. (2007), whose figure of "as much as 55%" for picking cost appears in the abstract without a source (C2).
```
Replacement:
```
de Koster et al. (2007), whose figure of "as much as 55%" for picking cost appears in the abstract without a source (C2); and Light (2001), that a customisation needs careful consideration for its potential impact on future maintenance (C8, read in abstract by SCE6).
```
Result: PASS. This fixes a gap the correction would create. After Change 1, the C8 cell rests in part on Light (2001), read in abstract only. SCE6's intro says "Light (2001) was read in abstract only", and the Salford abstract reads "careful consideration is required to determine whether a customization is viable given its potential impact upon future maintenance". SCE1's intro list of abstract-only claims would not otherwise name it.
Syllabus: no conflict. Part 8: "A claim that rests on an abstract alone says so".

## Summary
Passed: 5 changes (Change 1 with its cell reworded to match NIST, Abendroth et al., Light and SCE6 §10). Failed: 0. New: 2 (both passed). Each Current occurs once and still occurs once in turn when applied in order.

## Could not verify
- Crossref and Wiley records for Light (2001), DOI 10.1002/smr.240: not opened. No Crossref or Wiley page came up in search, and a third-party copy redirected, so I did not follow it. The journal title and the DOI rest on the University of Utah index. The Salford record gives "Journal of Software Maintenance: Research and Practice" and no DOI.
- Crossref record for Abendroth et al. (2024), DOI 10.5220/0012305500003690: not opened. I checked it against the publisher's (SciTePress) page and PDF instead.
