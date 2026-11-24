claude-opus-5-5

Verdict: corrections W-SCE6 · 9 pass (C-SCE5-3 with an amendment), 0 fail

# W-SCE6 corrections check: C-SCE5-1 to C-SCE5-9 (all in SCE1)

Target file: files/SCE1-the-map-the-words-and-the-evidence.md. Each Current was counted programmatically. corrections.md writes `\|` in the table rows (C2 to C5); with the escapes read as plain `|`, every Current occurs exactly once.

Sources read live on 24 Nov 2026:
- Scriven, Interact Analysis, in *Supply & Demand Chain Executive*, 22 Feb 2023 (sdcexec.com, article 22724398).
- FRED series EXPEF493ALLEST, EXPGAPEF493ALLEST, EXPECFEF493ALLEST and EXPAOOEF493ALLEST. Direct curl was refused by the proxy (403), so I read them through the web fetch tool.
- de Vries, de Koster & Stam 2016, IJPR abstract (research.vu.nl).
- de Vries, de Koster & Stam 2016, POMS abstract (repub.eur.nl/pub/96216).
- The 2015 ERIM working paper ERS-2015-009-LIS (repub.eur.nl/pub/78365).

I did not resolve doi.org/10.1080/00207543.2015.1064184 myself because the fetch needed an approval that nobody gave. The VU page gives the article as IJPR 54(8), 2260–2274, 2016.

Arithmetic:
- 7,975 / 23,883 = 0.3339, so "about a third" is correct.
- (7,975 + 1,895) / 23,883 = 9,870 / 23,883 = 0.4133, so 41% is correct.

All four figures match FRED for 2012.

## C-SCE5-1
Current: Occurs once (§4, WCS/WES bullet, line 78).
Replacement: as proposed.
Source: PASS. In the article (by Reuben Scriven of Interact Analysis, dated 22 Feb 2023): WCS systems are "used to control the flow of goods across fixed automation"; "The WES orchestrates the timing and location of warehouse workflows"; most eWES are "truly 'embedded' into the WMS". Both quotations are verbatim, and "most embedded WES sit in the WMS" is a fair paraphrase. SCE5 §7 grades the article analyst.
Syllabus: No contradiction. It matches the SCE1 brief (neighbouring systems "and where each sits") and SCE5 §7. It closes flag F5's action. No case fact touches it. No later brief relies on SCE1's undefined wording. One small tension: "below the WMS" sits beside "most embedded WES sit in the WMS"; SCE5's own flow diagram (WMS above WES above WCS) treats this as layering, so it is consistent.
Verdict: APPLY

## C-SCE5-2
Current: Occurs once (Deliverable B glossary, line 275).
Replacement: as proposed.
Source: PASS. The WCS line is Scriven's wording. The WES line combines two of the article's phrases: "controlling the timing and location of order processing" and "orchestrates the timing and location of warehouse workflows". It is an accurate paraphrase. The embedded-WES clause is as in C-SCE5-1. It matches SCE5's glossary rows 318–319.
Syllabus: No contradiction. It fulfils F5. It keeps one row, so the glossary stays at 39 rows and the intro's count does not change. No later brief relies on the old row.
Verdict: APPLY

## C-SCE5-3
Current: Occurs once (§11, line 186).
Replacement: as proposed.
Source: PASS on every figure. FRED gives these 2012 values, all in millions of dollars from the US Census Bureau: EXPEF493ALLEST, "Total Expense for Warehousing and Storage ... (DISCONTINUED)": 23,883. EXPGAPEF493ALLEST, gross annual payroll: 7,975. EXPECFEF493ALLEST, "Employer's Cost for Fringe Benefits" (Service Annual Survey): 1,895. So 33.4% and 41.3% are correct.
Wording flaw: "the other expense lines were not opened" is not accurate. SCE5 §8 also opened "All Other Operating Expenses" (EXPAOOEF493ALLEST, 2012: 4,388, confirmed on FRED today). That line is smaller than payroll. What was not opened is the remainder, about $9,625 million by subtraction, which exceeds payroll, so "largest" is still not shown. SCE5 §9's own summary carries the same loose wording.
Suggested amendment: replace "the other expense lines were not opened" with "of the other lines, only 'all other operating expenses' ($4,388 million) was opened; the remaining $9,625 million was not".
The row also drops SCE5's scope note: US firms whose business is warehousing, with in-house warehouses and Europe not covered. Adding "US" before "warehousing firms" is optional.
Syllabus: No contradiction. It matches SCE5 §8 and §9 and F2's carried note. SCE16 (Money) costs software lines, not warehouse labour, so nothing it relies on changes. No case fact touches it.
Verdict: APPLY (with the amendment above, so the row does not say no other line was opened)

## C-SCE5-4
Current: Occurs once (§11, line 188).
Replacement: as proposed.
Source: PASS. The IJPR abstract (research.vu.nl) describes a field experiment "with 101 participants"; says "(PbV) performs better than RF-terminal picking"; contains no percentage.
Syllabus: No contradiction. It matches SCE5 §3 and §9 and self-check item 5. Sourcing gap: the row adds a live DOI link to a source that is not in SCE1's Sources (see New).
Verdict: APPLY

## C-SCE5-5
Current: Occurs once (§11, line 189).
Replacement: as proposed.
Source: PASS. POMS abstract: competition raises productivity under parallel picking; zone picking is more productive under cooperation; "No effects on order picking quality were identified." 2015 working paper, read today: zone picking, orders with an error (least-squares means): 19.1% under competition, 31.6% under cooperation; dynamic zone picking: 29.6% under competition, 14.4% under cooperation; the method-by-incentive interaction on quality was significant (F = 6.47, p < .01); quality was studied "from a more exploratory perspective". So "error rates that differed by condition" is supported. "Up to 7%", the eight managers and the 17 pickers are taken from SCE5 §5. The correction cites none of these sources itself, and I did not reopen them.
Syllabus: No contradiction. It matches SCE5 §§4, 5 and 9. Flag F47 names this correction as the agreed handling, with no other text change.
Verdict: APPLY

## C-SCE5-6
Current: Occurs once (Deliverable C, Independent worked example, line 304).
Replacement: as proposed.
Source: PASS. The evidence is the same as C-SCE5-5. The sentence that follows in the file ("The abstract does not state the sample...") still reads correctly after the insertion.
Syllabus: No contradiction. The grade key is what every later unit uses, but the grade and the test are unchanged; only the example gets a caveat. Consistent with F47.
Verdict: APPLY

## C-SCE5-7
Current: Occurs once (front-matter intro, line 8).
Replacement: as proposed.
Source: PASS, checked against the file. The C4 row already reads "Tested in SCE4 §10". After C-SCE5-3 to C-SCE5-5, the claims fall as follows: set against sources: C1, C2, C10 (opened here), C4 (SCE4), C3, C5, C6 (SCE5), which is 7; still "Not searched here": C7, C8, C9, C11, C12, C13, C14, which is 7. The total is 14, so the count is right. This holds only if C-SCE5-3, -4 and -5 are applied together with it.
Syllabus: No contradiction with the SCE1 brief as F2 reads it. F2 itself stays open, which is not this correction's matter.
Verdict: APPLY (only together with C-SCE5-3, -4 and -5)

## C-SCE5-8
Current: Occurs once (front-matter intro, line 8).
Replacement: as proposed.
Source: PASS. Consistent with the Scriven verification above and SCE5 §7's grade. After C-SCE5-1 and -2, SCE1's glossary and §4 do carry the analyst definitions, credited to SCE5. "Not sourced here" stays true in the sense that SCE1 itself opened nothing, but the wording sits slightly against the new glossary row. This does not block the correction.
Syllabus: No contradiction (F5).
Verdict: APPLY

## C-SCE5-9
Current: Occurs once (front-matter intro, abstract-only claims, line 8).
Replacement: as proposed.
Source: PASS. The evidence is the same as C-SCE5-5. In the working paper's quality analysis the method-by-incentive interaction was significant, and the cell rates are those given there.
Syllabus: No contradiction (F47).
Verdict: APPLY

## New
- SCE1 Sources (line 332 onward) lists only the 2016 POMS article among the sources these corrections bring in. After C-SCE5-1 to -5, SCE1 cites four sources that are not in its Sources list: Scriven 2023; the Census Service Annual Survey via FRED; de Vries et al. 2016 IJPR, which C-SCE5-4 cites with a live DOI link; the 2015 working paper. This breaks sourcing-standard.md Part 1, line 24: every source a unit cites must be listed with a full reference. The C4 row, already applied from SCE4, has the same gap (Kull et al. 2013 and the WERC infographic are cited but not listed). Fix: add these entries to SCE1 Sources, copied from SCE5 Sources lines 345, 347, 355 and 358, or drop the IJPR link and cite "SCE5 §3" only.
- SCE5 §9, C3 row (line 167) and self-check item 9 (line 199): "other lines not opened" is inaccurate. SCE5 §8 opened "All Other Operating Expenses", which FRED's EXPAOOEF493ALLEST gives as $4,388 million for 2012, confirmed today. The correct statement is that the remainder, about $9,625 million, was not opened.
- SCE5 unsure item 5 says the $4,388 million figure "could not be re-fetched at the quality review". It was re-read today on FRED (EXPAOOEF493ALLEST, 2012: 4,388), so that unsure item can close.
- Flag F47 is open, waiting for a reading that settles whether the abstract or the working paper holds. The working paper itself, read today, reports a significant method-by-incentive interaction on quality (F = 6.47, p < .01), so the difference is more than a table artefact. Whether the published POMS full text keeps this result is still unchecked.

---
Saved by the main chat, 24 Nov 2026: the checker's report text as returned (the harness refused it a report file); where the checker wrote "as proposed" for a Current or Replacement, the text is that of C-SCE5-n in the W-SCE6 prompt (BACKLOG Corrections), shortened here only for the file; the report body is otherwise unchanged. The amendment to C-SCE5-3 and the four New items were applied by the main chat as the checker stated them.
