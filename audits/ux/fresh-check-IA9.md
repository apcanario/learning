---
audit: fresh check
unit: IA9 · IA in the product development lifecycle
course: ux · IA · Information Architecture
model: Fable 5.1 (claude-fable-5-1, confirmed from the agent's transcript; live search; no Fable 5.1 fresh check is owed for IA9)
date: 2026-11-09
chat: own Fable 5.1 agent context, not shown the writing (P31), launched by the U-9 chat (Opus 5.5 as the orchestrating chat; the writer ran on Opus 5.5) in session https://claude.ai/code/session_01KMmgQz1yCxz1MA9CnHKKjQ
verdict: fix · 1 error, 3 should-fix, 8 minor
---

The checker's final report, verbatim: its hand-back message, extracted by script from its transcript (the `SubagentHandback` call). Its own `out/report.md` differs from the hand-back in two places (the hand-back adds a sentence naming that file in its "Checked" paragraph and rewords one parenthesis in the Scrum Guide finding's Problem), so the hand-back is the record. The maintainer's note follows the report.

# Fresh check · IA9 · IA in the product development lifecycle

Model running this check: Fable 5.1 (claude-fable-5-1).

Checked: C/unit/IA9-ia-in-the-product-development-lifecycle.md (524 lines, read in full); against the brief (generator/data/ux/units_data.py, IA9 entry; brief.txt), sourcing-standard Part 1 and Part 4, the filed units IA1 to IA8 in C/vault, perqo-facts.md, figure-kinds.txt, IA2's notation (section 5 and the notation sheet). No audit report read. Checksums: both copies match sha256.txt before and after the check. render.py: 7 figures, 0 errors. The report is also at /tmp/claude-0/-home-claude/e1d0222c-65c5-5625-aa10-282b96a89303/scratchpad/u9/c/out/report.md, identical to this text.

## Findings

- [error] [figure] 6.3 and figure 7; Current: `whether employees land on Admin's sign-in screen looking for the app (IA5, section 5.5; IA7, Deliverable C, C.5)`; Problem: figure 7's cell "navigation model, AD-0" carries the identifier AD-0, which appears nowhere in the unit's text (the text says only "Admin's sign-in screen"); a figure label not in the text; Fix: `whether employees land on Admin's sign-in screen (AD-0) looking for the app (IA5, section 5.5; IA7, Deliverable C, C.5)`; Basis: IA7, Deliverable C, C.1 ("AD-0 Sign in") and C.5, in C/vault; sourcing-standard Part 1, "A figure adds no fact".
- [should-fix] [attribution] 3.1; Current: `The Scrum Guide's Definition of Done is "a formal description of the state of the Increment when it meets the quality measures required for the product", and "If a Product Backlog Item does not meet the Definition of Done, it cannot be released yet" (Schwaber and Sutherland, *The Scrum Guide*, November 2020, as quoted by Scrum.org, "What is a Definition of Done?", undated, [scrum.org, definition of done](https://www.scrum.org/resources/what-definition-done); practice framework).`; Problem: Scrum.org's page attributes only the first quotation to the Scrum Guide and names no edition; the second sentence is the page's own wording, not a quotation of the Guide (which the unsure list says was not opened); the unit puts both in the Guide's mouth; Fix: `The Scrum Guide's Definition of Done is "a formal description of the state of the Increment when it meets the quality measures required for the product" (Schwaber and Sutherland, *The Scrum Guide*, as quoted by Scrum.org, "What is a Definition of Done?", undated, [scrum.org, definition of done](https://www.scrum.org/resources/what-definition-done); practice framework; the page names no edition of the Guide), and Scrum.org adds, in its own words, that "If a Product Backlog Item does not meet the Definition of Done, it cannot be released yet" (same page).`; Basis: https://www.scrum.org/resources/what-definition-done (fetched 9 November 2026: "The Scrum Guide says the Definition of Done is a formal description of the state of the Increment..."; the "cannot be released yet" sentence is unattributed page text).
- [should-fix] [accuracy] 6.3; Current: `which the addresses already allow, since every app and Admin address carries its identifier first (IA6, section 6.3; IA7, Deliverable C, C.1)`; Problem: a stretch of the filed units. IA6's addresses are perqo.com/app/home, /app/claims/new, /app/benefits/cat-lea/learning: "identifier first" there is the category's identifier before its term, and no address carries the screen identifier (A-1). IA7's are /employees/{employee ID}, /policies/{policy ID}: the record's identifier, not the page's (AD-1.1). So the addresses do not give the screen or page identifier the analytics are said to record; Fix: `which the addresses do not give by themselves: IA6's and IA7's addresses carry a record's or a category's identifier, not the screen's or the page's (IA6, section 6.3 and Deliverable B, B.4; IA7, Deliverable C, C.1), so the analytics map each address pattern to its A- or AD- identifier`; Basis: IA6, section 6.3 and B.4 (E-1 to E-8 addresses); IA7, Deliverable C, C.1 ("Admin's addresses follow IA4's rule, identifier first: /employees/{employee ID}, ..."), in C/vault.
- [should-fix] [deliverable] Deliverable D, D.3, row DL-006; Current: ``IA7, A.2: O-01 contract end date → `contract_end_date` (proposed name); IA7, A.1 row O-01; faces of IA4, A and IA7``; Problem: IA7's A.1 table has no attribute column (ID, object, Admin label and place, volume, lifecycle, work queue, seen by, changed by), so its row O-01 has nothing to receive a contract end date; the second place in IA7 that lists the client's attributes is A.5, figure 1, the client box ("name", "contract start date"); Fix: ``IA7, A.2: O-01 contract end date → `contract_end_date` (proposed name); IA7, A.5, figure 1, the client box's attributes; faces of IA4, A and IA7``; Basis: IA7, Deliverable A, A.1 (columns) and A.5, figure 1 (client box attrs), in C/vault.
- [minor] [attribution] 1.5; Current: `contents at [oreilly.com, book contents](https://oreilly.com/library/view/~/9781491913529))`; Problem: the address with "~" is not the publisher's address for the book's contents and could not be checked (no search returned it); the address a search returns, and IA1 and IA2 cite, is the one below; Fix: `contents at [oreilly.com, book contents](https://oreilly.com/library/view/information-architecture-4th/9781491913529))`; Basis: https://oreilly.com/library/view/information-architecture-4th/9781491913529 (fetched: Part III "Getting Information Architecture Done", 11 Research, 12 Strategy, 13 Design and Documentation).
- [minor] [attribution] Sources, Rosenfeld, Morville and Arango; Current: `Contents at [oreilly.com, book contents](https://oreilly.com/library/view/~/9781491913529);`; Problem: same address as above; Fix: `Contents at [oreilly.com, book contents](https://oreilly.com/library/view/information-architecture-4th/9781491913529);`; Basis: as above.
- [minor] [attribution] 1.3; Current: `Marty Cagan named it dual-track agile`; Problem: Cagan's own page says "Jeff Patton first shared with me the term 'Dual-Track Scrum'"; Cagan's contribution is his variant of the name, not the naming; Fix: `Marty Cagan's name for it is dual-track agile`; Basis: https://svpg.com/dual-track-agile (fetched 9 November 2026).
- [minor] [label] 2.1; Current: `Kaley recommends adding UX-debt items directly to the backlog, ranking them by user value and effort`; Problem: Kaley gives two routes, directly to the backlog or a spreadsheet first, and warns that direct addition risks items being overlooked; "recommends adding directly" overstates; Fix: `Kaley recommends tracking UX-debt items in the backlog, added directly or from a spreadsheet first, with the same severity indicators as other items, ranking them by user value and effort`; Basis: https://www.nngroup.com/articles/ux-debt/ (fetched 9 November 2026).
- [minor] [attribution] 2.3; Current: `the rule or transition (DT-, T-)`; Problem: IA7's Deliverable D names the claim's transitions T1 to T6 (no hyphen), and IA8 cites them so; "T-" names an identifier series no filed unit uses; Fix: `the rule or transition (DT-; T1 to T6)`; Basis: IA7, Deliverable D, D.1 and section 5.2 ("T5"); IA8, D.4 ("T1 to T6"), in C/vault.
- [minor] [attribution] section 1, the hand-on table; Current: `IA5 to IA7, the faces and the "What later units take" sections`; Problem: no filed unit before IA8 has a section of that name: IA5's are "What the inventory hands on" and its siblings, IA6's is "What IA8 and IA11 take", IA7's "What IA8 and later units take"; Fix: `IA5 to IA7, the faces and the sections that hand on to later units ("What the inventory hands on", "What IA8 and IA11 take", "What IA8 and later units take")`; Basis: IA5, Deliverable A, A.4; IA6 and IA7 headings, in C/vault.
- [minor] [style] Sources, "Cited through the filed units"; Current: `Mausser, "Site Search Analytics: A Conversation with Lou Rosenfeld", UXmatters, 2011 (IA3; interview, practice). Full references in IA1, IA3, IA5 and IA7, Sources.`; Problem: Deliverable B cites Kaley 2020 through IA2 ("Kaley's fields, IA2, section 1.1") and the line omits it and IA2; Fix: `Mausser, "Site Search Analytics: A Conversation with Lou Rosenfeld", UXmatters, 2011 (IA3; interview, practice); Kaley, "Content Inventory and Auditing 101", NN/g, 2020 (IA2). Full references in IA1, IA2, IA3, IA5 and IA7, Sources.`; Basis: the unit's Deliverable B, first row; IA2, section 1.1 and Sources.
- [minor] [figure] figure 6, caption (section 5); Current: `each review of Perqo's IA by when it runs, with its owner in the cell;`; Problem: the Cross-surface review and Analytics paths cells under "Each release" are the triggered runs of RV-03 (only at a release touching two surfaces) and RV-06 (for the screens a release changed), while the column head reads as every release; the caption does not say so; Fix: `each review of Perqo's IA by when it runs, with its owner in the cell (under Each release, the Cross-surface review runs only at a release touching two surfaces, and Analytics paths only for the screens the release changed: Deliverable C, RV-03 and RV-06);`; Basis: the unit's Deliverable C, RV-03 and RV-06, trigger column.

## Confirmed

- Design Council, "Framework for Innovation": "Launched in 2004"; Discover, Define, Develop, Deliver; "speaking to and spending time with people who are affected by the issues"; "co-designing with a range of different people"; "small-scale"; "iteratively improving"; "not a linear process as the arrows on the diagram show"; "send them back to the beginning"; "no idea is ever 'finished'"; page undated. PASS. https://www.designcouncil.org.uk/resources/framework-for-innovation/
- Cagan, "Dual-Track Agile", SVPG, 17 September 2012: "quickly generating validated product backlog items"; "generating releasable software"; later used Continuous Discovery and Continuous Delivery. PASS. https://svpg.com/dual-track-agile
- Patton, "Dual Track Development is not Duel Track", 10 May 2017, updated 12 April 2023: credits and quotes Sy's 2007 paper ("designers need to communicate every day with developers"); "two kinds of work, and two kinds of thinking"; "Discovery work happens concurrently and continuously with development work"; "Keep measuring and learning even after you ship"; taught a class with Cagan. PASS. https://jpattonassociates.com/dual-track-development/
- Brhel, Meth, Maedche and Werder 2015: Information and Software Technology 61, pp. 163 to 181, DOI 10.1016/j.infsof.2015.01.004. PASS on the reference. https://publikationen.bibliothek.kit.edu/1000077582 (also https://researchr.org/publication/BrhelMMW15, https://kups.ub.uni-koeln.de/9879/)
- Rosenfeld, Morville and Arango 2015: Part III "Getting Information Architecture Done", 11 Research, 12 Strategy, 13 Design and Documentation; ch. 13 opens "When you cross the bridge from research and strategy into design, the landscape shifts dramatically"; "Style guides for capturing your past decisions and guiding your future ones". PASS. https://oreilly.com/library/view/information-architecture-4th/9781491913529 ; https://www.oreilly.com/library/view/information-architecture-4th/9781491913529/ch13.html
- Kaley, "UX Debt", NN/g, 11 November 2018: tech debt "Originally devised by Ward Cunningham in 1992"; UX debt "any ongoing problems in the experience due to launching a fast, easy, or careless solution"; "Inconsistencies in the UI can be considered UX debt, but not always"; A/B variants excluded; "Information architecture (navigation structures and content classification)" among debt-prone areas; causes "Skipping user testing", "Design by committee", "Acquiring or merging with other products", "Poor communication or documentation"; user value and effort; reduce tech and UX debt together; recurring reviews open to the team. PASS. https://www.nngroup.com/articles/ux-debt/
- Aizlewood, Clearleft, 24 July 2019: "Frankensteining occurs when products or services created using Agile become fragmented or disjointed"; "Do a best first pass"; "zoom out points into each sprint". PASS. https://clearleft.com/thinking/agile-and-design-how-to-avoid-frankensteining-your-product
- Dimmick, Smashing Magazine, 6 November 2012: "The rapid pace of UX design in the agile world can lead to shortsighted design decisions"; "design tunnel vision"; "any development work that could be affected by the spike temporarily ceases". PASS. https://www.smashingmagazine.com/2012/11/design-spikes-fit-big-picture-ux-agile-development/
- Agile Alliance, "What is Story Mapping?", published 17 December 2015, modified 9 March 2023: two dimensions; "walking skeleton", "a barebones but usable version of the product"; origins in Patton's 2005 and 2008 articles; does not use "backbone". PASS. https://agilealliance.org/?p=5003329
- Patton, User Story Mapping, O'Reilly, 2014: index entry "backbone (story map)" and section "Distill Your Map to Make a Backbone". PASS (settles the unsure-list item). https://www.oreilly.com/library/view/user-story-mapping/9781491904893/ix01.html
- Scrum.org, "What is a Definition of Done?": "a formal description of the state of the Increment when it meets the quality measures required for the product", attributed to the Scrum Guide. PASS for that quotation (the second is the finding above). https://www.scrum.org/resources/what-definition-done
- Welchman, Managing Chaos: ch. 5 "Stopping the Infighting About Digital Standards"; "establishing clear accountability for digital strategy, policy, and standards". PASS. https://rosenfeldmedia.com/?p=187514
- Fowler, "Architecture Decision Record", martinfowler.com, 24 March 2026: "captures and explains a single decision relevant to a product or ecosystem"; Nygard coined the term in 2011; "should not be modified if the decision is changed, but linked to a superseding decision"; statuses proposed, accepted, superseded; decision, context, trade-offs, alternatives, consequences. PASS. https://www.martinfowler.com/bliki/ArchitectureDecisionRecord.html
- Semantic Versioning 2.0.0, Tom Preston-Werner: the three MAJOR, MINOR, PATCH lines as quoted. PASS. https://semver.org/
- Chisnell, "Call centers as a source of data", 24 July 2016, modified 9 April 2025: "One of the richest sources of data about frustration is the call center"; "anything from on boarding to off boarding"; dominant categories; "Take note of how callers ask their questions". PASS. https://danachisnell.com/call-centers-as-a-source-of-data/
- Cardello, "Three Uses for Analytics in User-Experience Practice", NN/g, 17 November 2013: the three uses as quoted. PASS. https://www.nngroup.com/articles/analytics-user-experience/
- Tankala, "Card Sorting vs. Tree Testing", NN/g, 23 February 2024: "typically conducted early in the design process"; "A tree test evaluates a hierarchical category structure"; existing or proposed. PASS. https://nngroup.com/articles/card-sorting-tree-testing-differences
- Through the filed units (C/vault): Arango's chapters "Sustainability" and "Gardening" (IA1, section 1.3); Garrett's planes and IA1, sections 1.4 and 4; Evans, "a change in the language is a change to the model" (IA7, section 6.2); Farrell on reading several months of a log (IA3, section 5.2); Halvorson and Rach, ch. 9 governance (IA1, section 2.3) and the "rolling audits" index entry (IA5, section 1.1); Rosenfeld in Mausser, findings as hypotheses (IA3, section 5.2). PASS.
- Pointers to the filed units, all as the units say: IA2 sections 1.0 to 1.10, 3, 4, 5.2, the notation sheet and the decision table (five faults, six editing rules, fidelities by stage, blueprint "as lifecycle swimlanes", navigation model F2); IA3, section 5.2 and E2 (five queries refund, allowance, rejected claim, gym, approval; support reads the For employees log each quarter; first-click and tree tests named); IA4, Deliverable A face (version 1, 3 November 2026; note of 9 November after A.4), Deliverable B face (owner the content team), B.4 rules R1 to R10 and R8, R4, section 3.3; IA5 faces (inventory "the IA designer with marketing", templates "the IA designer with engineering"), section 5.5 note, 5.3, H-2.1.2, H-2.1.4, H-1.2.5; IA6 Deliverable B face unamended, B.1, B.3 note on A-5, B.4 E-8 and the 3 November note, B.5 (no "no allocation" state), Deliverable C face "C.2 amended 9 November 2026 (IA8, section 4.5)", section 6.3, "What IA8 and IA11 take" (session paths; tickets as proxy); IA7 face ("the agreed mapping to the data model"; version 1, 3 November), A.1 O-09 "Active, Frozen (IA4)", A.2 (`active`, `frozen`; no closed; no contract end date), A.4 invite employees unconditioned, C.1 AD-1.3, C.2 landing pages, C.4, C.5, section 2.3 (Active, Frozen, Not issued), section 5.1 table, 6.2, 6.3, the 9 November note and facts row, the assumption table (first actions after sign-in; tickets as proxy; failed sign-ins); IA8 sections 3.2, 3.4, 4.1 ("set on one surface and felt on another"; sales explains the rules), 4.2 ("a new state of IA6's category screen"), 4.5, 6 (four practices; quarterly and two-surface review), the face (F2 with F3 identifiers; version 1, 9 November 2026), D.1, D.4, D.5 ("A change to any identifier in a J- row is not done until the other cells of that row have been checked"), "What later units take" (two ticket-proxy rows, so four across IA6 to IA8), "Perqo facts set by this unit" (renames nothing). Section 4.5 and Deliverable D's rows and faces hold, apart from the DL-006 pointer above.
- Perqo: every Perqo fact set is in the unit's facts table; each is in the register's "Not yet set" or extends a registered fact and says so (E2 extended to both audiences); none contradicts IA1 to IA8 or perqo-facts.md; "(Perqo, fictional)" on first use (paragraph 1) and at each new fact. No personal fact about the reader; no private person named (every named person is a published author).
- Figures: every tone drawn (1, 3, 4, 5, 6) is named in the text (paragraph 2 and each figure's section); all seven captions name what the figure shows, its section and its sources; matrix row labels are short (longest "Admin paths, sign-ins", "Cross-surface review") and each traces to a sentence of the text; no link text is a bare path.

## Figures

1. matrix, section 1.4. Labels: Discover, Define, Develop, Deliver, Run and every cell trace to sections 1.1 to 1.3 ("inventory (F2)" to section 5, "IA2, section 1.1: an inventory at F2 before any redesign"; "outside the model" to 1.2; "discovery continues" to 1.3). Caption names the figure, section 1.4 and the sources. Kind fits (models by stages: matrix). PASS.
2. matrix, section 3.2. Fourteen rows are the short names listed in 3.2; every cell traces to 3.2's three rules, IA2's decision table and the two departures named ("F2, F3 identifiers"; blueprint "kept"); legend F1/F2/F3/kept traces to 3.1 and IA2, section 1.0. Caption names section 3.2, IA2's table and sections, and Deliverable C. Kind fits. PASS.
3. decision, section 4.1. Three questions and four outcomes trace to 4.1's four routing bullets; "yes" left; every box tone 5, named in the text. Caption names section 4.1 and sources. Kind fits (a rule with branches). PASS.
4. flow, section 4.2. Nine steps and notes trace to steps 1 to 9; "→ see" and "[declined]" follow IA2's notation and the caption says why the branch is a bracketed condition. Caption names section 4.2 and sources. Kind fits (a sequence). PASS.
5. states, section 4.3. Five states trace to the five statuses; transitions trace to 4.3, 4.2 step 9 and D.3 ("an accepted entry is superseded, never edited"); tone 6 on Declined named in the text and caption. Caption names section 4.3 and Fowler. Kind fits (a lifecycle). PASS.
6. matrix, section 5 and Deliverable C. Twelve rows are RV-01 to RV-12's names; every owner cell traces to Deliverable C. Caption names section 5, Deliverable C and the sources. Kind fits. FIX (minor): the caption clarification given in the findings (Current `each review of Perqo's IA by when it runs, with its owner in the cell;`, Fix as above).
7. matrix, section 6. Rows trace to 6.1 to 6.3; tones 1, 3, 4, 5 named in the text and caption; "Shows", "Hypothesis", "Test (IA11)" cells trace to 6.1 to 6.4 and the filed units' assumption tables. One label, "AD-0", is not in the unit's text: FIX (error). Replacement: the text edit in the findings (add "(AD-0)" to 6.3's sentence on Admin's sign-in screen); the JSON then stands as it is. Caption names section 6 and the sources. Kind fits.

## Coverage (brief items)

Published models: Double Diamond covered (1.1); Garrett's planes in time covered (1.2); discovery, definition, delivery covered (1.3, 1.4); what is wrong with a phase covered (1.5). Agile delivery: backbone before stories covered (2.2); IA alongside the backlog covered (2.3); IA debt and how it accrues covered (2.4); evidence and named practice labelled covered (2.1, every practitioner source marked practice; Brhel marked a review that does not test). Definition of done per artefact covered (3.1, Deliverable B, every artefact of IA2's catalogue); how fidelity rises covered (3.2). Versioning and change: who may change covered (4.1); proposed, recorded, communicated covered (4.2); decision log covered (4.3, D.3); versions covered (4.4). Living document and cadence (what, how often, trigger) covered (5, Deliverable C). Signals: search logs, support tickets, analytics paths covered (6.1 to 6.3); loop to IA11 covered (6.4). Figures asked for: process models with IA located (fig. 1), artefact-by-stage grid (fig. 2), change-control flow (fig. 4), maintenance cadence (fig. 6): all present, plus three. Deliverable: workflow with stage, activity, artefact, owner, consulted, informed (A, W-01 to W-17); definition of done per artefact (B); cadence with review, trigger, owner (C): present in full, follow from the evidence, usable alone. Nothing missing or thin. Length: about 12,700 words outside the figure blocks, above the brief's 2,000 to 6,000 band; the brief says not to cut to a target, so this is noted, not a finding.

## Unverifiable

- Garrett 2000 diagram (jjg.net): the time axis and the statement that the model is not a development process and defines no roles. No search returned the jjg.net address; the one copy found is on a course site, which is not fetched. Already in the unit's unsure list.
- Garrett 2011, ch. 2: the overlap of planes and the finish-before rule. Book text not online; the Peachpit and Boxes and Arrows pages a search returned carry no excerpt. In the unsure list.
- Brhel and others 2015: the five principles as quoted. Five repository pages fetched (Mannheim and Stuttgart blocked by a bot check; KIT, Cologne and researchr carry no abstract; ITU redirected and was not followed; Bohrium behind a firewall). The reference itself is confirmed. In the unsure list.
- Sy 2007, Journal of Usability Studies 2(3): the two uxpajournal.org addresses a search returned now show the current issue, not the 2007 one. In the unsure list.
- The Scrum Guide's edition (November 2020): the Scrum.org page names none. In the unsure list.

## Other checks

- Errata: no audit report was read, as the task says; every pointer to IA1 to IA8 was read against C/vault instead (see Confirmed and the findings).
- Exact text: every Current above occurs exactly once in C/unit/IA9-ia-in-the-product-development-lifecycle.md (checked by exact-string count; the DL-006 Current, which contains a backtick, is given in double backticks).
- Public site: no personal fact beyond the brief and the filed units; no private person named.
- Notation: every figure in IA2's notation; tone meanings named in the text (tone 6 included); row labels short enough for a phone; no bare-path link text.
- Render: python3 render.py unit/IA9-ia-in-the-product-development-lifecycle.md: figures 1 to 7 ok, 0 errors; nothing written into unit/.
- Checksums: unit/ and readonly/ both 67b06d152b22ef0649705f1771ae323e0a2985f2892ca797e82c92220dfc5ed6, matching sha256.txt, before and after the check.

IA9 · fix · 1 error, 3 should-fix, 8 minor

## Maintainer's note (U-9 chat, 9 November 2026)

Each finding was verified before it was applied as an exact replacement by script (each Current occurring once in the filed unit).

- Finding 1 (error, figure 7's "AD-0"): held; IA7, C.1 gives AD-0 as Admin's sign-in page. Applied; figure 7 was then checked again (below).
- Finding 2 (the Scrum Guide's two quotations): held. The maintainer's search returned scrum.org's "What is a Definition of Done?" (fetched): the page attributes the definition to the Scrum Guide, names no edition, and gives "If a Product Backlog Item does not meet the Definition of Done, it cannot be released yet" in its own words. Applied; the Sources line and the unsure line, which named the November 2020 edition, were aligned with it.
- Finding 3 (the addresses and the identifiers analytics record): held, against IA6, section 6.3 and B.4 and IA7, C.1. Applied with one narrowing: perqo.com/app/home and /app/claims/new carry no identifier at all, so the sentence says the addresses carry "at most" a record's or a category's identifier, "never" the screen's or the page's.
- Finding 4 (DL-006's pointer to IA7's A.1 row O-01): held; A.1 has no attribute column, and A.5's figure 1 holds the client's attributes. Applied, and the filing drew the attribute there (below).
- Findings 5 and 6 (O'Reilly's address): held; the maintainer's search returned oreilly.com/library/view/information-architecture-4th/9781491913529 (fetched: the 4th edition's page, Part III with chapters 11 to 13). Applied in the text and Sources.
- Finding 7 (Cagan and the name): held; svpg.com's "Dual-Track Agile" (search-returned, fetched, 17 September 2012) credits Jeff Patton with "Dual-Track Scrum". Applied.
- Finding 8 (Kaley's two routes to the backlog): held; nngroup.com's "UX Debt" (search-returned, fetched) gives a backlog item or label, or a spreadsheet first, and warns of items lost or deprioritised. Applied.
- Findings 9 to 12 (T1 to T6; the hand-on sections' names; Kaley 2020 through IA2; figure 6's caption): held against IA2, IA5, IA6, IA7 and IA8 in the vault and the unit's Deliverable C. Applied; figure 6 was then checked again (below).
- Found with the check and applied: the unsure line on Patton's backbone now cites the book's index entry "backbone (story map)" and its section "Distill Your Map to Make a Backbone" (oreilly.com, search-returned and fetched by the maintainer).
- Verdict fix (1 error); no rewrite.

Section 4.5 and Deliverable D, applied at filing. IA2, section 4's "Re-stamp the face" and the notation sheet's face field gained the version and amendment rule (DL-010), with a dated note. The faces of IA4, Deliverable A (DL-004 to DL-006), IA6, Deliverable B (DL-004, DL-008), IA7's Deliverable (DL-005 to DL-007) and IA7's navigation model (DL-007, C.4) were re-stamped "amended 9 November 2026"; IA6's wireflows' existing amendment now names DL-004. The places D.3 listed were applied, each with a dated note: IA7, section 2.3, section 5.1's table and A.1 (card status Cancelled), A.2 (`cancelled`, `closed`, `contract_end_date`, the last two marked proposed), A.4 and C.4 (the invite condition), A.5's figure 1 (the client's contract end date); IA6, B.5's table and figure (the second empty state of the category screen). IA9 gained dated notes in sections 2.4 and 4.5 and under D.3 saying the debt it recorded is cleared; its table keeps the state at the unit's date. The register gained "Set by IA9".

The renderer. Two faults the re-checks found were fixed in `kit/viz.py`, with the builds before and after compared file by file: a matrix column is never drawn narrower than its longest word or hyphen-separated piece (IA6's B.5 split "notifications" once its Empty cell grew), and the two counts of a level line in an objects figure never meet (IA7's "0..*0..*"). Only read-ia6, read-ia7 and read-ia9 changed. Renderer notes recorded and not applied, since no declaration can meet them: at 320 px (and at 360 for some), a matrix column wider than the room beside the pinned label column is never whole in a sampled frame; the fade beside the pinned label column runs through a matrix's legend and dims a letter mid-scroll; the opening-frame shots are covered by the sticky section bar (P44); the objects kind has no field for a line's R- identifier.

Figure re-checks. Each by a fresh Opus 5.5 agent given only the unit's text without its figures, the captions, the declaration, IA2 and the frames sheets of `verify.py --shots`; each hand-back extracted by script and saved below, verbatim. Minors that would change a passed figure's declaration once more were recorded, not applied, where every word they touch already traces (IA9 figure 6: "[for the screens it changed]"; IA7 figure 4: the work queue's and approve selected's sources, the "Admin:" lines' places); minors on the text were applied (IA9's opening paragraph names tone 5 for figure 7).

- IA9 figure 6 (matrix, the maintenance cadence): FIX at the fresh check (caption), FIX at its second check (the two conditional cells bracketed, the caption's parenthesis and its Farrell source reworded), PASS at its third.
- IA9 figure 7 (matrix, production signals): FIX at the fresh check (AD-0), FIX at its second (cells not in the text; labels too long for 320 px: redrawn), FIX at its third (one Hypothesis cell; the caption's sources), PASS at its fourth.
- IA6 figure 5 (matrix, screen states, changed by DL-008): FIX at its first check (caption; the renderer's word split), FIX at its second (the caption's other sources; the stops listed in words), PASS at its third.
- IA7 figure 3 (objects, figure 1 of 2, changed by DL-006 and DL-007): FIX at its first check (colliding counts, the caption, the invite conditions, "→ see figure 2 of 2"), FIX at its second (the admin user's continuation; the caption; the places "in Employees", "in Policies" added by the maintainer), FIX at its third (the caption's sources for IA4's objects, the catalogue items' volume and resend invitation; the maintainer also changed "configure" to "configure or, for the catalogue item, read"), PASS at its fourth.
- IA7 figure 4 (objects, figure 2 of 2; its "→ see figure 1" made "→ see figure 1 of 2" by the maintainer to match figure 3): FIX at its first check (`closed`, the decision condition, the audit entry's volume, A.1's wording), PASS at its second.

Transcripts, checked by script: no re-checker used a web, memory, Projects, connector, Artifact or Agent tool; each read and wrote inside its own folder, but for one that listed the browser install directory (`~/.cache/ms-playwright`) to find Chromium for its own screenshots, recorded; the other flagged paths were HTML tags, arithmetic and relative paths in its scripts. The harness refused every re-checker's `out/report.md`, so each hand-back is its one copy.

## Figure re-check reports, verbatim

Each the agent's hand-back, extracted by script from its transcript; in the order the checks ran within each figure.

### IA9 figure 6, second check

IA9 "IA in the product development lifecycle", figure 6: second check. I edited nothing in the unit. My scratch files are in /tmp/claude-0/-home-claude/e1d0222c-65c5-5625-aa10-282b96a89303/scratchpad/u9/f-ia9-6/out/, and the replacement block is in /tmp/claude-0/-home-claude/e1d0222c-65c5-5625-aa10-282b96a89303/scratchpad/u9/f-ia9-6/out/fig6-fix.md. The harness would not let me write out/report.md (subagents must return findings as text), so this message is the whole report.

**Figure 6.** Kind `matrix`. It is in section 5, "IA as a living document: the maintenance cadence", at the line "[figure 6 is drawn here]" (unit-text line 226). Section 5 introduces it: "The cadence below shows when each review runs and who owns it; a cell names the owner where a review runs at that cadence. Row names are Deliverable C's."

**Labels traced** (all from Deliverable C's table, unit-text lines 329–340):
- **Columns.** `Each story` comes from RV-01 "each story, before it enters a sprint". `Each release` comes from RV-02 "each release". `Monthly` comes from RV-05 "monthly". `Quarterly` comes from RV-03 to RV-10 "quarterly". `On trigger` comes from the Trigger column and from RV-11 and RV-12 "on trigger only".
- **Story check:** `IA designer` under Each story. RV-01: "| Story check | … | each story, before it enters a sprint | none | IA designer |". Correct.
- **Release check:** `IA designer` under Each release. RV-02: "| each release | none | IA designer |". Correct.
- **Cross-surface review:** `IA review` under Quarterly and under Each release. RV-03: "| quarterly | each release touching two surfaces | IA review |". Correct, but the Each release cell is conditional (see Notation).
- **Face audit:** `IA designer` under Quarterly. RV-09: "| quarterly | none | IA designer |". Correct.
- **Search log:** `support` under Quarterly and On trigger. RV-04: "| quarterly | a release that renames a label: the next month's log, for the old word | support |". Correct.
- **Support tickets:** `support` under Monthly and On trigger. RV-05: "| monthly | a tag that rises after a release touched its screen | support |". Correct.
- **Analytics paths:** `product management` under Each release and Quarterly. RV-06: "| quarterly across all screens | each release, for the screens it changed | product management |". Correct, but the Each release cell is conditional (see Notation).
- **Vocabulary:** `content team` under Quarterly and On trigger. RV-07: "| quarterly | a new variant; a new client's terms; a proposed F-CAT value | content team |". Correct.
- **Rolling audit:** `content team` under Quarterly and On trigger. RV-08: "| quarterly | before any redesign of a surface: a full audit at F2 | content team |". Correct.
- **Debt triage:** `product management` under Quarterly. RV-10: "| quarterly | none | product management |". Correct.
- **Structure test:** `IA designer` under On trigger. RV-11: "| on trigger only | … | IA designer |". Correct.
- **Rules review:** `product management` under On trigger. RV-12: "| on trigger only | … | product management |". Correct.

No cell is missing and none is invented. The figure has no dates or numbers.

**Caption.** It names the artefact ("Maintenance cadence"). It says what the figure shows and the decision it supports ("who checks what, and when, once the IA is in use"). It names the section ("section 5; Deliverable C") and says "Perqo, fictional". Its sources trace to the text:
- "IA8, section 6 (each release touching two surfaces, quarterly)": line 211, "at each release that touches two surfaces and each quarter (IA8, section 6)".
- "IA3's item E2 (support reads the log each quarter)": line 211, "support reads the For employees search log each quarter … (IA3, Deliverable, E2 …)".
- Farrell, NN/g, 2017: line 213.
- Halvorson and Rach 2012, index: line 213, "Halvorson and Rach's index has an entry for 'rolling audits' (2012, index …)".
- Kaley, NN/g, 2018: line 213 and Sources line 419 (Nielsen Norman Group, 11 November 2018).

The caption added at the first check now covers the two qualified cells, and it matches RV-03 and RV-06. Caption: pass.

**Kind.** The data is items (reviews) set against sections (cadences), and the method gives `matrix` for "items by sections". Pass.

**Tone.** Every row is tone 5 and no tone 6 is drawn. Line 14 gives tone 5 its meaning: "Tone 5, shared, carries most figures here, because process work spans every surface and every function." Pass.

**Frames.**
- **Phone 390, dark and light.** There are 3 frames, scrolled to 0, 164 and 242 of 242 px. The pinned label column stays in view in every frame and leaves about two cell columns of room. Every row label is whole, including the longest, "Cross-surface review". Each column is shown whole in at least one frame: Each story and Each release in frame 1, Monthly and Quarterly in frame 2, Quarterly and On trigger in frame 3. Cell text wraps inside its cell ("product management", "content team", "IA designer"). Nothing overlaps.
- **Phone, scroll edges.** The fade at the scroll edges dims the first letters of the Quarterly cells in frame 3 ("IA review", "management"). Those letters stay readable, and the same cells are clear in frame 2.
- **Desktop 1280 and tablet, dark and light.** The whole figure fits in one frame. Everything is legible and nothing is clipped.
- **Phone 320 (extra width).** There are 4 frames. The pinned label column takes over half the width, so only about one cell column is visible at a time, and Each release is never whole in a single sampled frame. Every visible label is still legible.

**Notation (IA2).** Row = item, column = dimension, marked cell = the value where they meet; that matches the notation sheet's line "Row, column, marked cell | matrix". The tone use matches section 5.2. Labels are in sentence case.

It fails on conditions. Two cells under Each release exist only when a condition holds:
- Cross-surface review (RV-03: "each release touching two surfaces").
- Analytics paths (RV-06: "each release, for the screens it changed").

IA2 writes a condition in square brackets at the element it governs:
- Section 5.2: "A condition is written in square brackets."
- Notation sheet: "[condition] | the path or the box exists only when this holds (Garrett: conditional connector, conditional area)".
- Section 5.1: "Conditional area | a box whose note opens with the condition in square brackets".

This course's figure 4 follows the same rule ("the declined path is a bracketed condition in the Decide step's note"). Here the condition is written only in the caption's prose, without brackets, and not at the cell. The cells themselves read `IA review` and `product management` with no qualifier. On a phone, frame 1 opens on exactly those two cells, and the caption sits below twelve rows. This is the misreading the first check flagged. A matrix cell has no note, so the bracket goes in the cell's mark.

**Replacement.** It changes two cells and the caption's parenthesis. I rendered it with render.py without error ("figure 1: matrix ok (11749 chars)", "1 figures, 0 errors"). I also rendered it in Chrome with theme.css at 390 and 1280 px, dark and light. Both bracketed cells wrap inside the Each release column (4 lines at 390 px), legibly and without overlap.

- Current cell (row Cross-surface review, column Each release): `IA review`. Replacement: `IA review [touching two surfaces]`. Traced to RV-03 "each release touching two surfaces".
- Current cell (row Analytics paths, column Each release): `product management`. Replacement: `product management [screens it changed]`. Traced to RV-06 "each release, for the screens it changed".
- Current caption parenthesis: `(under Each release, the Cross-surface review runs only at a release touching two surfaces, and Analytics paths only for the screens the release changed: Deliverable C, RV-03 and RV-06)`. Replacement: `(a condition in square brackets: the review runs at that cadence only when it holds; Deliverable C, RV-03 and RV-06)`.

IA9 "IA in the product development lifecycle" figure 6: FIX

Whole replacement declaration:

```viz
{"kind": "matrix", "caption": "Maintenance cadence: each review of Perqo's IA by when it runs, with its owner in the cell (a condition in square brackets: the review runs at that cadence only when it holds; Deliverable C, RV-03 and RV-06); supports the decision on who checks what, and when, once the IA is in use (section 5; Deliverable C). Cadence and owners set in section 5 and Deliverable C (Perqo, fictional), extending IA8, section 6 (each release touching two surfaces, quarterly) and IA3's item E2 (support reads the log each quarter); quarterly log reading after Farrell, NN/g, 2017; rolling audits from Halvorson and Rach 2012, index; recurring debt reviews from Kaley, NN/g, 2018. Every row tone 5, shared.", "cols": ["Each story", "Each release", "Monthly", "Quarterly", "On trigger"], "rows": [{"label": "Story check", "tone": 5, "cells": ["IA designer", null, null, null, null]}, {"label": "Release check", "tone": 5, "cells": [null, "IA designer", null, null, null]}, {"label": "Cross-surface review", "tone": 5, "cells": [null, "IA review [touching two surfaces]", null, "IA review", null]}, {"label": "Face audit", "tone": 5, "cells": [null, null, null, "IA designer", null]}, {"label": "Search log", "tone": 5, "cells": [null, null, null, "support", "support"]}, {"label": "Support tickets", "tone": 5, "cells": [null, null, "support", null, "support"]}, {"label": "Analytics paths", "tone": 5, "cells": [null, "product management [screens it changed]", null, "product management", null]}, {"label": "Vocabulary", "tone": 5, "cells": [null, null, null, "content team", "content team"]}, {"label": "Rolling audit", "tone": 5, "cells": [null, null, null, "content team", "content team"]}, {"label": "Debt triage", "tone": 5, "cells": [null, null, null, "product management", null]}, {"label": "Structure test", "tone": 5, "cells": [null, null, null, null, "IA designer"]}, {"label": "Rules review", "tone": 5, "cells": [null, null, null, null, "product management"]}]}
```

Notes
- **Caption wording, Farrell (minor).** "quarterly log reading after Farrell, NN/g, 2017" is slightly stronger than the text. Line 213 says Farrell recommends "several months" and that this argues for a quarterly read "on this unit's reading". A closer wording would be `quarterly log reading on this unit's reading of Farrell, NN/g, 2017`. Not a FIX.
- **Row order (minor).** The rows do not follow Deliverable C's RV order: Face audit (RV-09) is fourth, Vocabulary comes before Rolling audit, and Debt triage is tenth. The order follows section 5's grouping of the reviews into kinds, and section 5 says "Row names are Deliverable C's", not their order. Not a fault.
- **Renderer note: opening frames.** In the phone and desktop opening frames, the page's sticky section header covers the matrix's column header row. The capture scrolls the figure top under the bar. The frame sheets show the header row in full. This is page layout, not the declaration.
- **Renderer note: phone 320.** At 320 px the pinned label column takes over half the width, leaving room for about one cell column, so no single sampled frame shows Each release whole. The row names are fixed by Deliverable C, so the declaration cannot meet this.
- **Renderer note: scroll-edge fade.** The fade dims the first letters of the Quarterly cells in phone frame 3 (dark and light). They stay readable.

### IA9 figure 6, third check

**IA9 "IA in the product development lifecycle", figure 6: third check**

**Kind and section.** The kind is `matrix`. It sits in section 5, "IA as a living document: the maintenance cadence", directly after the line: "The cadence below shows when each review runs and who owns it; a cell names the owner where a review runs at that cadence. Row names are Deliverable C's." It draws Deliverable C, RV-01 to RV-12.

**Labels traced** (all in unit-text.md, Deliverable C table, unless another section is named):

*Columns*
- `Each story`: RV-01, "each story, before it enters a sprint".
- `Each release`: RV-02, "each release".
- `Monthly`: RV-05, "monthly". Section 5 also has "Signal reads, monthly or quarterly".
- `Quarterly`: RV-03, RV-04 and RV-07 to RV-10, "quarterly"; RV-06, "quarterly across all screens".
- `On trigger`: RV-11 and RV-12, "on trigger only"; the Trigger column of RV-04, -05, -07 and -08.

*Rows.* All 12 match Deliverable C's Review column word for word: Story check, Release check, Cross-surface review, Face audit, Search log, Support tickets, Analytics paths, Vocabulary, Rolling audit, Debt triage, Structure test, Rules review.

*Cells* (21 marked; no numbers or dates):
- Story check, `IA designer` (Each story): RV-01, "each story, before it enters a sprint | none | IA designer".
- Release check, `IA designer` (Each release): RV-02, "each release | none | IA designer".
- Cross-surface review:
  - `IA review [touching two surfaces]` (Each release) and `IA review` (Quarterly): RV-03, "quarterly | each release touching two surfaces | IA review".
  - Section 5 also says: "IA8's 'each release touching two surfaces' is one (IA8, section 6)".
- Face audit, `IA designer` (Quarterly): RV-09, "quarterly | none | IA designer".
- Search log, `support` (Quarterly and On trigger): RV-04, "quarterly | a release that renames a label: the next month's log, for the old word | support".
- Support tickets, `support` (Monthly and On trigger): RV-05, "monthly | a tag that rises after a release touched its screen | support".
- Analytics paths, `product management [screens it changed]` (Each release) and `product management` (Quarterly): RV-06, "quarterly across all screens | each release, for the screens it changed | product management".
- Vocabulary, `content team` (Quarterly and On trigger): RV-07, "quarterly | a new variant; a new client's terms; a proposed F-CAT value | content team".
- Rolling audit, `content team` (Quarterly and On trigger): RV-08, "quarterly | before any redesign of a surface: a full audit at F2 | content team".
- Debt triage, `product management` (Quarterly): RV-10, "quarterly | none | product management".
- Structure test, `IA designer` (On trigger): RV-11, "on trigger only | a change to a top level or a tab; ... | IA designer".
- Rules review, `product management` (On trigger): RV-12, "on trigger only | a change to contract terms, a policy option or a decline reason | product management".

Every blank cell is also correct: no review runs at a cadence or on a trigger that Deliverable C does not give it. No label, date or number is untraced.

**Caption.**

Current: `Maintenance cadence: each review of Perqo's IA by when it runs, with its owner in the cell (a condition in square brackets: the review runs at that cadence only when it holds; Deliverable C, RV-03 and RV-06); supports the decision on who checks what, and when, once the IA is in use (section 5; Deliverable C). Cadence and owners set in section 5 and Deliverable C (Perqo, fictional), extending IA8, section 6 (each release touching two surfaces, quarterly) and IA3's item E2 (support reads the log each quarter); quarterly log reading on this unit's reading of Farrell, NN/g, 2017; rolling audits from Halvorson and Rach 2012, index; recurring debt reviews from Kaley, NN/g, 2018. Every row tone 5, shared.`

It says what the figure shows and the decision it supports, names section 5 and Deliverable C, and says Perqo is fictional. Each source matches the text:
- IA8: section 5 has "review on a trigger as well as a date, at each release that touches two surfaces and each quarter (IA8, section 6)".
- IA3 E2: section 5 has "support reads the For employees search log each quarter ... (IA3, Deliverable, E2; ...)".
- Farrell: section 5 has "a log read too often misleads, which, on this unit's reading, argues for a quarterly read" (Farrell, "Search-Log Analysis", NN/g, 2017).
- Halvorson and Rach: section 5 has "Halvorson and Rach's index has an entry for 'rolling audits' (2012, index; ...)". The caption keeps "index", which is honest because the text says the chapter was not read.
- Kaley: section 5 has "Kaley recommends recurring team reviews where anyone can raise debt (Kaley 2018)". Sources list it as Nielsen Norman Group, 11 November 2018.
- The bracket parenthesis matches the two bracketed cells, which are the triggers of RV-03 and RV-06.

Caption: pass.

**Kind.** The data is items by sections (reviews by cadence), so `matrix` fits. Pass.

**Frames** (all 24 images looked at; the mid-scroll frames were cropped for a closer look):
- **Desktop 1280, dark and light:** one frame, the whole figure fits. Every header, row label and cell is legible. The two-line bracketed cells wrap inside their cells with no overlap and nothing clipped.
- **Tablet, dark and light:** one frame, the whole figure fits, all legible.
- **Phone 390, dark and light:** three frames (scroll 0, 164 and 242 of 242 px). The row labels stay pinned in every frame.
  - Frame 1 shows Each story and Each release whole. Both bracketed cells read in full; the edge fade dims the last letter of "designer", "management" and "it", but they stay legible.
  - Frame 2 shows Monthly and Quarterly whole.
  - Frame 3 shows On trigger whole; Quarterly sits under the pinned column's fade and is still legible.
  - The pinned column takes about 45% of the width and leaves room for two columns.
- **Phone 430, dark and light:** three frames. Every column is whole in at least one frame, all legible.
- **Phone 360, dark and light:** three frames (0, 149, 272).
  - Each story, Monthly and On trigger are whole in some frame.
  - Each release (with both bracketed cells) and Quarterly are cut at the right in one frame and at the left in the next, so neither is whole in any sampled frame.
- **Phone 320, dark and light:** four frames (0, 129, 258, 312).
  - The pinned label column takes about 58% of the width, which leaves room for about one column.
  - Each release, Monthly and Quarterly are never whole in a sampled frame. Only Each story and On trigger are.
  - The figure is still readable by scrolling continuously.

At 320 and 360 the cause is the width of the pinned label column, set by the longest row label "Cross-surface review", together with the half-frame sampling step. The declaration cannot fix this without renaming a row, which would break "Row names are Deliverable C's." So it is a renderer note, not a FIX (see Notes).

**Tones.** Only tone 5 is drawn; empty cells are the neutral fill, and tone 6 is not drawn. The unit's text gives tone 5's meaning: "Tone 5, shared, carries most figures here, because process work spans every surface and every function." (introduction). IA2 5.2 also has "Tone 5: shared, meaning the data model, the Perqo system, and any object or term that lives on more than one surface".

**Notation** (IA2, section 5.2 and the notation sheet):
- Matrix rule: "In a matrix, a row is an item, a column a dimension, and a marked cell the value where they meet." Here the review is the item, the cadence the dimension, the owner the value.
- Brackets: "A condition is written in square brackets." The notation sheet has "[condition] | the path or the box exists only when this holds". Both conditions are bracketed at the cell they govern.
- Labels are in sentence case and no dashes are drawn.
- No tone is the only carrier of meaning: the caption names the tone.

Notation: pass.

IA9 "IA in the product development lifecycle" figure 6: PASS

(The current declaration renders through render.py without error: "figure 1: matrix ok".)

**Notes**
- Wording: `[screens it changed]` reads more as a scope than as a condition that "holds". RV-06 has "each release, for the screens it changed", and "it" (the release) changing screens works as the condition. If a later edit is made anyway, `product management [for the screens it changed]` would follow RV-06 word for word. This is not a fault.
- Tones: two rows are reviews of one surface: Rolling audit (perqo.com's inventory) and Search log (the Help centre, drawn in tone 1 in figure 7). Here they are drawn in tone 5. The intro sentence quoted above covers this ("process work spans every surface and every function"), and the caption states the tone. It is consistent with the unit; noted only because figure 7 tones the same records by surface.
- Renderer: at phone 320 and 360 the pinned label column (about 58% and 47% of the width) leaves the cell window barely wider than one column. With frames half a frame apart, Each release and Quarterly (and Monthly at 320) are whole in no sampled frame. Capping or wrapping the pinned row labels below about 400 px, or a finer frame step, would meet it. This lies in the renderer's layout, not the declaration.
- Process: I could not save a report in out/: writing out/report.md was refused ("Subagents should return findings as text"), so this message is the only copy. My crops and a render-check file (current.md) are in out/.

### IA9 figure 7, second check

IA9 "IA in the product development lifecycle", figure 7: **FIX**. The AD-0 fault is closed, but most of the Hypothesis, Test and Changes cells are still not in the unit's text, and at 320 px the cells have too little room. A replacement declaration is at the end of this report; it renders with render.py without error.

**Kind and section.** `matrix`, drawn after the first paragraph of section 6.4 ("From signal to IA11"), in section 6 ("Signals that the IA is failing in production").

## 1 · Labels, dates and numbers traced to the unit's text

The figure has no dates. Its only identifier is AD-0.

**Column heads**
- `Shows`, `Hypothesis`, `Test (IA11)`, `Changes`: traced. Section 6.4: "Every signal is read for what it shows and becomes a hypothesis about one part of the structure, which a method of IA11 then tests with people before an artefact changes."

**Row labels**
- `Help centre search`: traced. Section 6.1: "Perqo's Help centre has search and logs it". Opening section: "tone 1 for perqo.com (the Help centre's search)".
- `App paths`: traced as a compound. Section 6.3: "session paths for whether most app visits are one or two tasks …". RV-06 is "Analytics paths".
- `Admin paths, sign-ins`: traced. Section 6.3: "the first actions after sign-in …" and "Admin's failed sign-ins are a fourth record".
- `Support tickets`: traced. This is the heading of section 6.2 and RV-05's review name.

**Cells that trace**
- `zero results, variants, reformulations`: section 6.1 has "zero-result queries … reformulations in one session, a failed search". The 6.1 table has "allowance | a variant of Balance with no synonym in search".
- `tree test, first-click test`: section 6.4 has "goes first to a test of that structure, a tree test or the first-click test IA3 and IA6 named for the app's labels".
- `loops, detours through Help, exits`: RV-06 has "loops, detours through Help or search, exits".
- `first actions after sign-in; failed sign-ins`: section 6.3, as quoted above.
- `AD-0` (in `navigation model, AD-0`): now traced. Section 6.3 has "whether employees land on Admin's sign-in screen (AD-0) looking for the app (IA5, section 5.5; IA7, Deliverable C, C.5)". The fault the first check found is closed.

**Cells that are close paraphrases (not counted as errors)**
- `a label or route hides a thing`: section 6.1 has "frequent queries for something the site holds, which show a structure that hides it".
- `vocabulary, Help centre structure`: the 6.1 table has "variants go to the Help centre search as synonyms", and RV-04's output is "variant terms for RV-07".

**Cells not in the unit's text (errors)**
1. `a route or screen is misplaced`. "Misplaced" is not in the unit. The nearest line is section 6.3: "a screen reached mostly from search or from Help rather than its route".
2. `usability test; tree test of the app map`. The unit never names a usability test as the test for any signal. Its only use of the phrase is section 6.2, where Chisnell says tickets "reach problems a scenario-bound usability test can miss". "Tree test of the app map" is not stated either: section 6.4 names "a tree test or the first-click test IA3 and IA6 named for the app's labels".
3. `a landing page or the sign-in line is wrong`. "Landing pages" traces to section 6.3: "whether HR's and finance's most frequent work is what their landing pages, Approvals and Budgets, assume". "The sign-in line" is not in the unit. The text's hypothesis is "whether employees land on Admin's sign-in screen (AD-0) looking for the app".
4. `usability test; interviews with HR and finance`. Not in the unit. "Interview" appears only once, in Sources, describing Mausser's piece ("interview, practice").
5. `navigation model` (in `navigation model, AD-0`). Section 6 never names the navigation model as what a failed Admin test changes.
6. `where people stop, in their words`. "In their words" traces to section 6.2: "the callers' own words are worth noting". "Where people stop" is not in the unit. The text has "show where problems cluster" and "A ticket can be read against the IA only if it says where the person was."
7. `a rule or a status is unclear`. "Rule" traces to section 6.2: "where it concerns a rule, the DT- tree". "A status is unclear" is not stated. The nearest line is "employees understand a declined payment".
8. `interviews; usability test`. Not in the unit. The test the unit gives for tickets is in the IA11 table of "What later units take": "Ticket tags locate problems on the IA | section 6.2; RV-05 | support's tags compared with first-click tests on the same screens".
9. `decision trees, state names, articles`. "State names" is not in the unit. "Decision trees" traces only as the "DT- tree" of section 6.2.
10. `app map, wireflows`. Section 6 never names these as what a failed path test changes.

The caption sources the Test column to "tests as named in IA5 to IA8's assumption tables". That is outside this unit's text. Section 6.4 says only "the filed units have already named which fits which assumption" and does not list them, so the column cannot be traced in this unit.

## 2 · Caption

Current: `Production signals: what each record shows about Perqo's IA, the hypothesis it raises, the test it goes to and the artefact a failed test changes; supports the decision on what to do with a signal before changing the structure (section 6). Search-log reading from Farrell, NN/g, 2017 (IA3, section 5.2); tickets from Chisnell 2016 (practice); analytics uses from Cardello, NN/g, 2013; tests as named in IA5 to IA8's assumption tables, methods by stage from Tankala, NN/g, 2024. Tone 1 perqo.com (the Help centre), tone 3 the Perqo app, tone 4 Perqo Admin, tone 5 shared: tickets reach every surface. Perqo is fictional.`

The caption says what the figure shows, the decision it supports, the section and the sources. It meets the caption rule, but its source for the tests ("IA5 to IA8's assumption tables") is the untraceable source behind errors 2, 4 and 8. It changes with the replacement.

## 3 · Kind

`matrix`: records (items) against four dimensions, which is "items by sections". The kind fits.

## 4 · The figure as the reader sees it (frames/)

- **Desktop 1280, dark and light.** One frame; the whole figure fits. Every label is legible, nothing is clipped or overlaps, and the caption is whole.
- **Tablet, dark and light.** One frame; the whole figure fits. Legible, with no clipping or overlap.
- **Phone 390, dark and light.** Four frames, at 0, 164, 328 and 372 of 372 px.
  - The row labels stay pinned and legible in every frame. The pinned column is 154 px of a 328 px frame (47 %), set by the longest label, `Admin paths, sign-ins`.
  - Shows is whole in frame 1, Hypothesis in frame 2 and Changes in frame 4.
  - **Test (IA11) is not whole in any frame.** It is cut by the right fade in frame 2 and sits partly under the pin in frame 3. A reader scrolling by hand can bring it into view, because the 174 px of room is wider than the 111 px column.
  - Text under the fades stays legible.
- **Phone 360** (extra sheet). Four frames. Shows and Test are not whole in any frame.
- **Phone 320** (extra sheet). Five frames.
  - The pinned column (154 px) leaves 104 px for cells in a 258 px frame. **No column is whole in any frame**: every cell is cut by the pin, the fade or both.
  - At this width the pinned label column does not leave its cells room.
  - The declaration causes this: viz.py sizes the label column to the longest row label plus 20. Shortening the labels is part of the FIX.
- **Phone 430** (extra sheet). Three frames. Labels are pinned. Hypothesis is not whole in a sampled frame.
- **Tones.** Tones 1, 3, 4 and 5 are drawn; tone 6 is not.
  - The opening section gives each tone's meaning: "Tone 5, shared, carries most figures here, because process work spans every surface and every function. … One figure, of the signals read in production, keeps IA2's surface tones: tone 1 for perqo.com (the Help centre's search), tone 3 for the Perqo app, tone 4 for Perqo Admin."
  - Tone 5 on Support tickets is supported by section 6.2, where tickets are tagged "(A-, AD-, S-, H-)", so they reach every surface.
  - No tone is the only carrier of its meaning, because the caption names each surface.

## 5 · Notation (IA2, section 5 and the notation sheet)

The figure is in IA2's notation.
- IA2, section 5.2: "In a matrix, a row is an item, a column a dimension, and a marked cell the value where they meet."
- The tones follow 5.2: 1 perqo.com, 3 the app, 4 Admin, 5 shared. Labels are in sentence case.
- The caption meets 5.2's Captions rule: it names the artefact, what it shows, the decision, the section and the sources, and says Perqo is fictional.
- Nothing is dashed, and there are no status words.

## Verdict

IA9 "IA in the product development lifecycle" figure 7: FIX

The replacement declaration below fixes three things:
- Every cell is drawn from the unit's text: sections 6.1 to 6.4, RV-04 to RV-06, the IA11 table, W-13 and DL-002.
- The caption sources the tests to this unit (section 6.4 and the IA11 table), not to IA5 to IA8.
- The row labels are shorter. This narrows the pinned column from 154 to 118 px, so at 320 px the cells get 140 px of room instead of 104.

It renders with render.py without error ("figure 1: matrix ok; 1 figures, 0 errors"). It is saved at /tmp/claude-0/-home-claude/e1d0222c-65c5-5625-aa10-282b96a89303/scratchpad/u9/f-ia9-7/out/fig7-replacement.md.

`{"kind": "matrix", "caption": "Production signals: what each record shows about Perqo's IA, the hypothesis it raises, the test it goes to and the artefact a failed test changes; supports the decision on what to do with a signal before changing the structure (section 6). Records and what each shows from sections 6.1 to 6.3 and Deliverable C, RV-04 to RV-06; search-log reading from Farrell, NN/g, 2017 (IA3, section 5.2); tickets from Chisnell 2016 (practice); analytics uses from Cardello, NN/g, 2013; tests from section 6.4, methods by stage from Tankala, NN/g, 2024, and for tickets the IA11 table in 'What later units take'. Tone 1 perqo.com (the Help centre), tone 3 the Perqo app, tone 4 Perqo Admin, tone 5 shared: tickets reach every surface. Perqo is fictional.", "cols": ["Shows", "Hypothesis", "Test (IA11)", "Changes"], "rows": [{"label": "Search log", "tone": 1, "cells": ["zero results, frequent queries, reformulations", "a structure hides what is wanted, or a content gap", "tree test or first-click test", "vocabulary and search synonyms; Help centre articles (H-)"]}, {"label": "App paths", "tone": 3, "cells": ["loops, detours through Help or search, exits", "a screen is reached from search or Help, not by its route", "tree test or first-click test of the app's labels", "the app's labels and routes (A-)"]}, {"label": "Admin paths", "tone": 4, "cells": ["first actions after sign-in; failed sign-ins", "landing pages miss HR's and finance's most frequent work; employees look for the app on AD-0", "tree test or first-click test of Admin's structure", "the landing pages; AD-0, the sign-in screen (DL-002)"]}, {"label": "Support tickets", "tone": 5, "cells": ["tags by screen, page or DT- tree; the words people use", "problems cluster on the tagged screen, page or rule", "first-click tests on the same screens", "the tagged screen, page or DT- tree"]}]}`

**Where each replacement cell comes from**
- `Search log`: section 6.1 heading "Search logs" and RV-04's review name "Search log".
- `zero results, frequent queries, reformulations`: RV-04, "zero results, frequent queries, reformulations".
- `a structure hides what is wanted, or a content gap`: section 6.1, "which show a structure that hides it; … a content gap".
- `vocabulary and search synonyms; Help centre articles (H-)`: the 6.1 table ("variants go to the Help centre search as synonyms"; "H-2.1.4, which answers 'gym'") and W-13 ("Help centre articles (H-)").
- `loops, detours through Help or search, exits`: RV-06.
- `a screen is reached from search or Help, not by its route`: section 6.3, "a screen reached mostly from search or from Help rather than its route".
- `tree test or first-click test of the app's labels`: section 6.4.
- `the app's labels and routes (A-)`: section 6.4 ("the app's labels"), section 6.3 ("its route") and section 6.2's identifiers ("A-, AD-, S-, H-").
- `Admin paths` and `first actions after sign-in; failed sign-ins`: section 6.3.
- `landing pages miss HR's and finance's most frequent work; employees look for the app on AD-0`: section 6.3, "whether HR's and finance's most frequent work is what their landing pages, Approvals and Budgets, assume" and "whether employees land on Admin's sign-in screen (AD-0) looking for the app".
- `tree test or first-click test of Admin's structure`: section 6.4, "a signal from production, which is about a structure that exists, goes first to a test of that structure, a tree test or the first-click test".
- `the landing pages; AD-0, the sign-in screen (DL-002)`: section 6.3 and D.3, DL-002, "Admin's sign-in screen carries 'Looking for your benefits? Get the Perqo app'".
- `tags by screen, page or DT- tree; the words people use`: RV-05, "ticket tags by surface, screen or page and DT- tree; the words people use".
- `problems cluster on the tagged screen, page or rule`: section 6.2, "show where problems cluster" and "where it concerns a rule, the DT- tree".
- `first-click tests on the same screens`: the IA11 table, "support's tags compared with first-click tests on the same screens".
- `the tagged screen, page or DT- tree`: section 6.2.

**How the replacement looks.** I rendered it in headless Chrome with design/theme.css, at the verify script's scroll positions; the sheets are in F/out as sheet-320/360/390/1280-dark/light.png. The theme's web fonts were not loaded, so the fallback monospace wraps slightly differently from verify.py.
- Desktop 1280: every cell is whole and legible, with no overlap.
- Phone 390, dark and light: labels pinned at 118 px, and every column is wholly in view in at least one of the four sampled frames.
- Phone 320: Shows and Changes are whole. Hypothesis (166 px) is wider than the 140 px of room, so it is never whole at once (see the renderer notes).

## Notes

- **Alternative to the FIX.** If the writer would rather keep the current cells (usability tests, interviews with HR and finance, state names, navigation model, app map and wireflows), the text must say them. That means a sentence in section 6.4 naming, for each record, the test and the artefact it changes. The caption must then source them to that sentence, not to "IA5 to IA8's assumption tables". As the unit stands, the replacement above is the fix.
- **Renderer note (sampling).** verify.py samples phone frames half a frame apart. At 390 px with the current declaration, Test (IA11) falls between frames 2 and 3 and is never whole in a sampled frame, although a reader can scroll it into view. The fault is in how frames are sampled, not in the figure.
- **Renderer note (phone 320).** viz.py sizes matrix columns to fill the 700-unit width in proportion to their text, whatever room a phone leaves past the pinned column. At 320 px the frame is 258 px, so the room past any pin is small. A column wider than that room (166 px in the replacement) is never wholly in view. The declaration can only narrow the pin, which the replacement does.
- **Renderer note (left fade).** When a cell starts exactly at the pin's edge, the theme's 36 px left fade (`--stick-m` + 36px) lies over the cell's first characters. This shows in the frame-2 Hypothesis column at 390 px in the current frames. The text stays legible. This is theme behaviour.
- **Minor.** The replacement's `tags by screen, page or DT- tree` drops RV-05's "surface" to keep the column narrow. The caption's "tone 5 shared: tickets reach every surface" still carries the surface meaning.
- **Report file not written.** The harness refused the write to F/out/report.md (subagents return findings as text). This message is the whole report.

### IA9 figure 7, third check

Figure 7 fails this third check on two counts, both fixable in the declaration and caption:
1. One Hypothesis cell holds what a record shows, not a hypothesis.
2. The caption does not name where two columns come from.

The 320 px layout is still poor, but that is the renderer's, not the figure's (see Notes).

**IA9 "IA in the product development lifecycle", figure 7: matrix, section 6.4 ("From signal to IA11").**

## 1. Labels traced to the unit's text

**Columns.** `Shows`, `Hypothesis`, `Test (IA11)`, `Changes` trace to 6.4: "becomes a hypothesis about one part of the structure, which a method of IA11 then tests".

**Row labels.**
- `Search log`: RV-04 "Search log"; 6.1 heading "Search logs".
- `App paths`, `Admin paths`: shortened forms that split RV-06 "Analytics paths" by surface. 6.3: "Perqo's product analytics record each app screen view by its screen identifier and each Admin page view by its page identifier". They trace.
- `Support tickets`: 6.2 heading; RV-05.

**Search log row (tone 1)**
- `zero results, frequent queries, reformulations`: RV-04 "zero results, frequent queries, reformulations, grouped by need".
- `a structure hides what is wanted, or a content gap`: 6.1 "frequent queries for something the site holds, which show a structure that hides it; frequent queries for something the site lacks, a content gap".
- `tree test or first-click test`: 6.4 "goes first to a test of that structure, a tree test or the first-click test IA3 and IA6 named for the app's labels".
- `vocabulary and search synonyms; Help centre articles (H-)`: 6.1 table "variants go to the Help centre search as synonyms", "H-2.1.2 marked for update", "H-2.1.4", "H-1.2.5"; RV-07 "synonyms loaded".

**App paths row (tone 3)**
- `loops, detours through Help or search, exits`: RV-06, verbatim.
- `a screen is reached from search or Help, not by its route`: **ERROR.**
  - The words are in 6.3, but 6.3 gives them as something a path *shows*, not as a hypothesis: "For the IA the first two matter most: a path that loops between two screens, a screen reached mostly from search or from Help rather than its route, an exit just after a label is read."
  - In the Hypothesis column the cell repeats the Shows cell beside it ("detours through Help or search").
  - It is not "a hypothesis about one part of the structure" (6.4).
  - The hypothesis the text does give for app paths is missing: 6.3 "session paths for whether most app visits are one or two tasks begun from Home or a notification". The Admin row takes its hypothesis from the matching IA7 sentence; the App row should do the same.
- `tree test or first-click test of the app's labels`: 6.4 "a tree test or the first-click test IA3 and IA6 named for the app's labels".
- `the app's labels and routes (A-)`: 6.3 "rather than its route", "an exit just after a label is read", "map each address pattern to its A- or AD- identifier".

**Admin paths row (tone 4)**
- `first actions after sign-in; failed sign-ins`: RV-06 "first actions after sign-in; Admin's failed sign-ins".
- `landing pages miss HR's and finance's most frequent work; employees look for the app on AD-0`: 6.3 "whether HR's and finance's most frequent work is what their landing pages, Approvals and Budgets, assume" and "whether employees land on Admin's sign-in screen (AD-0) looking for the app". 6.3 now states AD-0, so the fault the fresh check found is gone.
- `tree test or first-click test of Admin's structure`: the 6.4 rule, as above.
- `the landing pages; AD-0, the sign-in screen (DL-002)`: 6.3 "their landing pages, Approvals and Budgets"; D.3 "DL-002 | Admin's sign-in screen carries 'Looking for your benefits? Get the Perqo app'".

**Support tickets row (tone 5)**
- `tags by screen, page or DT- tree; the words people use`: RV-05 "ticket tags by surface, screen or page and DT- tree; the words people use".
- `problems cluster on the tagged screen, page or rule`: 6.2 "the categories calls are routed into show where problems cluster"; "where it concerns a rule, the DT- tree".
- `first-click tests on the same screens`: IA11 table "support's tags compared with first-click tests on the same screens".
- `the tagged screen, page or DT- tree`: 6.2 "tags each ticket with the surface and the screen or page identifier ... and, where it concerns a rule, the DT- tree"; the line after the figure, "a test that fails it raises a change".

There are no dates. The only numbers are inside identifiers (`AD-0`, `DL-002`), both traced above.

## 2. Caption

It says what the figure shows, gives the decision and names "section 6". It names sources for the records, what each shows, the tests, Farrell, Chisnell, Cardello, Tankala and the IA11 table.

**Should-fix:** it names no source for the Hypothesis or Changes columns. Changes draws on 6.1's table and on Deliverable D, D.3 (`DL-002`), and neither is named. The D.3 the redraw used never reached the caption.

## 3. Kind

Items (four production records) by sections (shows, hypothesis, test, changes): matrix fits.

## 4. Frames

**Desktop 1280 and tablet, dark and light.** One frame each; the whole figure fits. Every label and cell is legible, with no clipping or overlap, and the four tones are distinct in both themes.

**Phone 390, dark and light (4 frames, scroll 0 to 372).**
- The pinned label column (117.8 px) stays in view in every frame, and each label sits on one line.
- Shows is whole in frame 1, Test in frame 3 (soft edge fade only) and Changes in frame 4.
- Hypothesis is never whole in a frame. In frame 2 (scroll 164) its left 18 px lies under the label plate, hiding the first letters of the Admin cell ("nding pages", "equent work", "ok for the app"); in frame 1 its right part is cut off.
- A reader scrolling to about 146 px sees it whole, so this is where the frames were taken, not a fault the reader meets.

**Phone 360.** Every column is whole in some frame, with soft edge fades. Legible.

**Phone 320 (5 frames).** No column is ever whole in a frame.
- The renderer shares a 700-unit width among the columns (140, 166, 133 and 119 px wide); the sticky label column takes 118 px, leaving 140 px for cells before the 36 px fade on each side.
- Hypothesis and Test can only be read in two halves (frames 2 and 3, then 3 and 4).
- The declaration cannot fix this: shorter row labels only widen the columns, and shorter cells only move width between columns. Renderer note.

**Tones** drawn are 1, 3, 4 and 5. Their meaning is in the unit's opening paragraph: "One figure, of the signals read in production, keeps IA2's surface tones: tone 1 for perqo.com (the Help centre's search), tone 3 for the Perqo app, tone 4 for Perqo Admin." and "Tone 5, shared, carries most figures here, because process work spans every surface and every function." Tone 5 for tickets is supported by 6.2's "(A-, AD-, S-, H-)". Tone 6 is not drawn.

## 5. Notation (IA2)

The figure is IA2's matrix: "Row, column, cell: an item, a dimension, the value where they meet." Tones follow IA2 (1 perqo.com, 3 the app, 4 Admin, 5 shared). The Help centre is under perqo.com in IA2's sitemap. Each tone is also named in the caption, as WCAG 1.4.1 requires. Nothing is drawn dashed, and identifiers keep their prefixes. Conforms.

IA9 "IA in the product development lifecycle" figure 7: FIX

Two changes:
1. **App paths Hypothesis cell.** Current: `a screen is reached from search or Help, not by its route`. Replacement: `most app visits are not one or two tasks begun from Home or a notification`.
2. **Caption.** Current: `Records and what each shows from sections 6.1 to 6.3 and Deliverable C, RV-04 to RV-06;`. Replacement: `Records, what each shows and the hypothesis it raises from sections 6.1 to 6.3 and Deliverable C, RV-04 to RV-06; the artefacts a failed test changes from section 6.1's table, sections 6.2 and 6.3 and Deliverable D, D.3 (DL-002);`.

Column widths are unchanged (140.4, 165.9, 132.9 and 119.0, as now), so the phone behaviour is the same; the App row gains one line. render.py reported "figure 1: matrix ok; 1 figures, 0 errors". The file is /tmp/claude-0/-home-claude/e1d0222c-65c5-5625-aa10-282b96a89303/scratchpad/u9/f2-ia9-7/out/fig7-replacement.md.

Replacement declaration:

`{"kind": "matrix", "caption": "Production signals: what each record shows about Perqo's IA, the hypothesis it raises, the test it goes to and the artefact a failed test changes; supports the decision on what to do with a signal before changing the structure (section 6). Records, what each shows and the hypothesis it raises from sections 6.1 to 6.3 and Deliverable C, RV-04 to RV-06; the artefacts a failed test changes from section 6.1's table, sections 6.2 and 6.3 and Deliverable D, D.3 (DL-002); search-log reading from Farrell, NN/g, 2017 (IA3, section 5.2); tickets from Chisnell 2016 (practice); analytics uses from Cardello, NN/g, 2013; tests from section 6.4, methods by stage from Tankala, NN/g, 2024, and for tickets the IA11 table in 'What later units take'. Tone 1 perqo.com (the Help centre), tone 3 the Perqo app, tone 4 Perqo Admin, tone 5 shared: tickets reach every surface. Perqo is fictional.", "cols": ["Shows", "Hypothesis", "Test (IA11)", "Changes"], "rows": [{"label": "Search log", "tone": 1, "cells": ["zero results, frequent queries, reformulations", "a structure hides what is wanted, or a content gap", "tree test or first-click test", "vocabulary and search synonyms; Help centre articles (H-)"]}, {"label": "App paths", "tone": 3, "cells": ["loops, detours through Help or search, exits", "most app visits are not one or two tasks begun from Home or a notification", "tree test or first-click test of the app's labels", "the app's labels and routes (A-)"]}, {"label": "Admin paths", "tone": 4, "cells": ["first actions after sign-in; failed sign-ins", "landing pages miss HR's and finance's most frequent work; employees look for the app on AD-0", "tree test or first-click test of Admin's structure", "the landing pages; AD-0, the sign-in screen (DL-002)"]}, {"label": "Support tickets", "tone": 5, "cells": ["tags by screen, page or DT- tree; the words people use", "problems cluster on the tagged screen, page or rule", "first-click tests on the same screens", "the tagged screen, page or DT- tree"]}]}`

## Notes

- **Renderer note (320 px):** with a 118 px sticky column, a 166 px widest column and 36 px fades on both sides, no matrix column is ever whole at 320 px. The renderer would need to cap matrix column widths on phones, or give the matrix a phone drawing of its own as bars already has (svg.viz-alt).
- **Frame sampling (390 px):** the frames are half a frame apart and none catches the Hypothesis column whole, though a reader can see it whole at about 146 px.
- **Minor:** `(DL-002)` in the Admin Changes cell names the entry already applied. Under D.3 ("an accepted entry is superseded, never edited"), a failed test would raise a new entry that supersedes DL-002. Wording only.
- **Minor:** the Search log Changes cell leaves out the two app changes 6.1's table also lists ("Claims grouped by all four states"; "the rule line on New claim"). It is incomplete, not wrong.
- **Minor:** the unit's opening tone paragraph names tones 1, 3 and 4 for this figure but not tone 5; the caption covers it.
- I could not write out/report.md: the tool refused it because subagents return their findings as text. The only files written were the replacement and its crops in out/.

### IA9 figure 7, fourth check

**Figure 7: PASS.** Every label traces to the unit's text, the caption is complete, the kind fits and the frames are legible at every width and theme. Nothing needs changing; there are four notes at the end, one of them a renderer note.

**Kind and section.** `matrix`, in section 6.4 ("From signal to IA11"). It comes after the Tankala paragraph and before "The loop runs back as well as forward."

**Labels traced** (all in unit-text.md)

Column headers:
- `Shows`: 6.4, "Every signal is read for what it shows".
- `Hypothesis`: 6.4, "and becomes a hypothesis about one part of the structure".
- `Test (IA11)`: the IA11 table header in "What later units take", "| Test (IA11) |"; also 6.4, "which a method of IA11 then tests".
- `Changes`: 6.4, "before an artefact changes"; the IA11 table, "What changes if it fails".

Row labels:
- `Search log`: RV-04, "| RV-04 | Search log |"; 6.1 heading "Search logs".
- `Support tickets`: RV-05, "| RV-05 | Support tickets |"; 6.2 heading.
- `App paths` and `Admin paths`: shortened forms. RV-06 and the 6.3 heading say "Analytics paths". 6.3 splits them by surface: "Perqo's product analytics record each app screen view by its screen identifier and each Admin page view by its page identifier", and "IA6 and IA7 named the paths their assumptions need read: session paths … and the first actions after sign-in". Each label is traced in sense, not verbatim (note 2).

Search log row (tone 1):
- `zero results, frequent queries, reformulations`: RV-04, "zero results, frequent queries, reformulations, grouped by need".
- `a structure hides what is wanted, or a content gap`: 6.1, "frequent queries for something the site holds, which show a structure that hides it; frequent queries for something the site lacks, a content gap"; and "zero-result queries, which show wanted information the search cannot find".
- `tree test or first-click test`: 6.4, "a tree test or the first-click test IA3 and IA6 named for the app's labels".
- `vocabulary and search synonyms; Help centre articles (H-)`: 6.1 table, "variants go to the Help centre search as synonyms", "H-2.1.2 marked for update"; W-13, "vocabulary (F3: synonyms loaded); Help centre articles (H-)".

App paths row (tone 3):
- `loops, detours through Help or search, exits`: RV-06, "loops, detours through Help or search, exits".
- `most app visits are not one or two tasks begun from Home or a notification`: 6.3, "session paths for whether most app visits are one or two tasks begun from Home or a notification". The cell states the failing case of that assumption, as a hypothesis should.
- `tree test or first-click test of the app's labels`: 6.4, "a tree test or the first-click test IA3 and IA6 named for the app's labels".
- `the app's labels and routes (A-)`: 6.3, "a screen reached mostly from search or from Help rather than its route, an exit just after a label is read"; "map each address pattern to its A- or AD- identifier".

Admin paths row (tone 4):
- `first actions after sign-in; failed sign-ins`: RV-06, "first actions after sign-in; Admin's failed sign-ins".
- `landing pages miss HR's and finance's most frequent work; employees look for the app on AD-0`: 6.3, "whether HR's and finance's most frequent work is what their landing pages, Approvals and Budgets, assume"; "whether employees land on Admin's sign-in screen (AD-0) looking for the app".
- `tree test or first-click test of Admin's structure`: 6.4, as above; Deliverable A, "consulted on Admin's labels and structure (W-06)".
- `the landing pages; AD-0, the sign-in screen (DL-002)`: 6.3, "their landing pages"; D.3, "DL-002 | Admin's sign-in screen carries 'Looking for your benefits? Get the Perqo app'".

Support tickets row (tone 5):
- `tags by screen, page or DT- tree; the words people use`: RV-05, "ticket tags by surface, screen or page and DT- tree; the words people use".
- `problems cluster on the tagged screen, page or rule`: 6.2, "the categories calls are routed into show where problems cluster"; "the screen or page identifier it is about … and, where it concerns a rule, the DT- tree".
- `first-click tests on the same screens`: IA11 table, "support's tags compared with first-click tests on the same screens".
- `the tagged screen, page or DT- tree`: 6.2, "tags each ticket with the surface and the screen or page identifier … the DT- tree"; 6.4, "a test that fails it raises a change". See note 4.

There are no dates or numbers in the cells. AD-0 and DL-002 trace as quoted above.

**Caption** (Current, unchanged): `Production signals: what each record shows about Perqo's IA, the hypothesis it raises, the test it goes to and the artefact a failed test changes; supports the decision on what to do with a signal before changing the structure (section 6). …`
- It says what the figure shows and the decision it supports, and names section 6.
- It sources every column: Records, Shows and Hypothesis to 6.1–6.3 and RV-04 to RV-06; Changes to 6.1's table, 6.2, 6.3 and D.3 (DL-002); the tests to 6.4, Tankala 2024 and the IA11 table.
- It names Farrell 2017, Chisnell 2016 and Cardello 2013, each cited in sections 6.1 to 6.3. It gives the meaning of each tone and ends "Perqo is fictional."
- Complete.

**Kind.** Four records, each read across four dimensions, is items by sections, so a matrix fits.

**Tones.** All four drawn tones are given meanings in the unit's opening paragraph: "One figure, of the signals read in production, keeps IA2's surface tones: tone 1 for perqo.com (the Help centre's search), tone 3 for the Perqo app, tone 4 for Perqo Admin, and tone 5 for the support tickets, which reach every surface." Tone 6 is not drawn.

**What the frames show** (every opening frame and frame sheet, dark and light, at phone 390, 320, 360 and 430, tablet and desktop)
- **Phone 390, both themes (4 frames, 0 to 372 px):** the row labels stay pinned on their plate in every frame. Frame 1 shows Shows whole, frame 2 Hypothesis, frame 3 Test (IA11) and frame 4 Changes. Cells slide under the left fade, which starts past the pinned column, and nothing overlaps. Every column fits whole in the about 207 units the pinned column leaves free, including Hypothesis at 165.9. Text is legible in both themes.
- **Phone 360 (4 frames) and 430 (3 frames):** the same, and every column fits whole.
- **Phone 320 (5 frames):** labels pinned and legible, nothing clipped or overlapping. No frame shows a whole Hypothesis cell (renderer note 1).
- **Tablet and desktop, both themes:** one frame, the whole figure fits. All 16 cells, 4 headers and 4 labels are legible. Rows are equal height and nothing overlaps or clips.

**Notation** (IA2, section 5.2 and the notation sheet)
- "In a matrix, a row is an item, a column a dimension, and a marked cell the value where they meet": records are the rows, the four dimensions are the columns.
- Tones keep their IA2 meanings (1 perqo.com, 3 app, 4 Admin, 5 shared, "any object or term that lives on more than one surface").
- No tone is the only carrier of meaning: the surface is named in the row labels "App paths" and "Admin paths" and in the caption.
- The caption follows IA2's caption rule: artefact, what it shows, decision, section, sources, "Perqo is fictional".
- There are no lines, shapes or conditions to check. The figure is in IA2's notation.

The declaration renders with render.py: "figure 1: matrix ok, 1 figures, 0 errors" (copy at out/current.md).

IA9 "IA in the product development lifecycle" figure 7: PASS

**Notes**
1. **Renderer note, phone 320.** The pinned column is 117.8 units wide, which leaves about 137 units for cells. Hypothesis is 165.9 wide and Shows 140.4, so no frame at 320 shows a whole Hypothesis cell, and the reader scrolls partway through a line. Nothing is clipped or overlapping. The declaration cannot fix this: the renderer spreads four text columns across 700 units, and shorter row labels would only widen the columns. Every column fits at 360, 390 and 430.
2. **Shortened labels.** "App paths" and "Admin paths" are not verbatim; the unit's own name is "Analytics paths" (6.3, RV-06). They are traced in sense to 6.3's app and Admin paths. Not an error.
3. **Admin row grouping.** It holds failed sign-ins, which 6.3 calls "a fourth record". RV-06 groups them the same way under Analytics paths, so this is consistent, but "paths" fits them loosely.
4. **Ticket row sources.** The test cell borrows the IA11 table's test, but in that table a failure changes "the tag set" (the tagging practice). The figure's Changes cell instead follows 6.2 and 6.4: a failed test changes the tagged screen, page or tree. This is consistent with the figure's logic, and the caption cites the IA11 table only for the test. A first-click test also reaches screens, not DT- rules, while the hypothesis includes rules. Minor wording; no FIX.

I edited nothing in F. My only writes were out/current.md (the render check) and crop images, which I deleted. The harness refused out/report.md, so this reply is the whole report.

### IA6 figure 5, first check

## IA6 "Level 2 · the client app" figure 5: fresh figure check (9 November 2026)

The figure needs one fix: the caption does not name the source of the state added on 9 November. Every label traces to the unit, the kind fits and the notation conforms. The added cell also makes the renderer break a word in two in another column, which I report as a renderer note (Notes, 1).

**Figure.** Figure 5 is a `matrix` in Deliverable B, B.5 (screen states). It sits straight after the dated note that follows B.5's table.

### (7) Labels traced to the unit's text

**Columns.** `Empty`, `Error`, `Permission`, `Shown later` are B.5's own headers: "| Screen | Empty | Error | Permission | Shown later |".

**Rows.** The row labels are B.5's screen names with the screen IDs dropped. Each cell matches its row in the table word for word. A `null` cell stands for the table's "none".

- `Home`: "| Home, A-1 | [no category open] HR chooses the open categories; Help | [no connection] the last balances, with their time | none | spent, amount and period, on the category screen |". Matches.
- `Category screen` (the changed row): "| Category screen, A-2.1 to A-2.4 | [balance used up] no balance left this period; Why can't I use money from another category?; [no allocation this period] Your budget for this period is not set yet | none | [category closed] not shown | cross-listings, after the home items |". Matches, including the added state.
  - The added state is also given in the note: "*Note, 9 November 2026: the category screen's second empty state, for a category open to the group with no allocation for the period, added from IA8's decision (IA8, section 4.2; decision log DL-008, IA9, Deliverable D); no payment or claim is possible there.*"
- `Claims`: "| Claims, A-3 | [no claims] How to claim back a receipt; New claim | [no connection] the last list, with its time | none | the claim, on tap |". Matches.
- `New claim`: "| New claim, A-3.1 | none | [receipt missing] by the Receipt field; input kept | [camera refused] Choose a file | the limit, in the rule line |". Matches.
- `Check and submit`: "| Check and submit, A-3.2 | none | [over the balance] Edit only | none | none |". Matches.
- `Claim submitted`: "| Claim submitted, A-3.3 | none | none | [first claim] the notifications prompt | none |". Matches.
- `Card`: "| Card, A-4 | [no card issued] not issued yet; claims still work | none | none | card details, on tap |". Matches.
- `Purchases`: "| Purchases, A-4.2 | [no purchases] Where you can pay with the Perqo card | [no connection] the last list, with its time | none | the purchase, on tap |". Matches.
- `Card offers`: "| Card offers, A-4.3 | [no offers] the route is hidden | none | [category closed] its offers not shown | the filter by category |". Matches.
- `Notifications`: "| Notifications, A-5.2 | [none yet] what will appear here | none | [not allowed] how to allow notifications | the claim, on tap |". Matches.

**Legend.**
- `tone 3`, "the Perqo app": "every app box is tone 3".
- `tone 6`, "a stop: the path ends without success here": "tone 6, IA2's stop, marks a state where the path ends without success, or a fault found in a review (IA2, section 5.2)".

The figure has no dates or numbers. **No label is untraced.**

### Caption

The caption says what the figure shows and names its section ("Deliverable B, B.5"). Every source it names traces to section 4:
- Neusesser and Sunwall, "14 May 2023".
- Android Developers, "page updated 28 October 2026".
- Nielsen 2006.
- IA3 A3 and F2, section 4.2.

**Fault.** The added state `[no allocation this period] Your budget for this period is not set yet` comes from IA8, section 4.2 (DL-008, IA9, Deliverable D). The caption does not name that source. Its only empty-state source is "this unit's synthesis from IA3, A3 and F2", which covers the rule, not this decision.

Figure 7's caption, also amended on 9 November 2026, does name its IA8 source: "from IA8, section 4.5 (note, 9 November 2026)". This is a should-fix: **FIX, caption**.

### Kind

Screens (items) by four kinds of state (sections) is a `matrix`. **The kind fits.**

### (8) Frames

**Desktop and tablet, dark and light.** Each sheet is "Frame 1 of 1 (the whole figure fits)".
- Every label is legible.
- Nothing is clipped and nothing overlaps.
- The changed Category screen cell under Empty wraps to four lines inside its band.

**One fault, at every width and in both themes.** In the Permission column, "notifications" is split as "notificat / ions" in two cells:
- Claim submitted: `[first claim] the notifications prompt`
- Notifications: `[not allowed] how to allow notifications`

The split is new with this change. With the pre-change cell, the word renders whole. The new four-line Empty cell makes the renderer take width from Permission, down to the width of the header's longest word only. Nothing in the declaration sets column widths, so it cannot avoid this and keep B.5's words. It is a renderer note (Notes, 1), not a FIX.

**Phone, dark and light: 390 (4 frames), 320 (5), 360 (4) and 430 (3).** I viewed every frame of every sheet.
- The row labels stay pinned at every scroll position.
- The pinned label column takes about 40% of the width at 390 and about half at 320. The cells still have room to be read one column at a time.
- Every cell is legible in the frame where its column is in view.

**Tones.** Only tone 3 and tone 6 are drawn; the text and the legend give both meanings, as quoted above. The tone 6 cells are:
- Home: empty and error.
- Category screen: empty.
- Claims, New claim, Check and submit and Purchases: error.
- Card: empty.

Each is a state where the path ends without success until something changes. For the added state, the text says "no payment or claim is possible there". The permission states stay tone 3, as "a permission state degrades without blocking" requires.

### (9) Notation

The figure follows IA2, section 5.2, and the notation sheet. **It conforms.**
- In a matrix, "a row is an item, a column a dimension, and a marked cell the value where they meet".
- "A condition is written in square brackets", which is the reduction of the conditional area.
- Tone 3 is the app and tone 6 is a stop.
- Labels are the product's own words, in sentence case.

IA6 "Level 2 · the client app" figure 5: FIX

**Replacement caption.** Only the caption changes:

`Screen states: the empty, error and permission states of the Perqo app screens that have them, and what each shows later, F2; supports the decision on what each screen shows under each condition and by which route the employee goes on (Deliverable B, B.5). Conditions in square brackets, as IA2's conditional area; empty-state rule this unit's synthesis from IA3, A3 and F2; the category screen's [no allocation this period] state from IA8, section 4.2 (decision log DL-008, IA9, Deliverable D; note, 9 November 2026); error states from Neusesser and Sunwall, 'Error-Message Guidelines', NN/g, 2023; permissions from Android Developers, 'Request runtime permissions', 2026 (platform documentation); disclosure from Nielsen, 'Progressive Disclosure', NN/g, 2006. Rows tone 3, the app; tone 6 marks a stop, a state in which the path ends without success until something changes (IA2, section 5.2). Blank cells: none, as in B.5's table. Perqo is fictional.`

**Replacement JSON, the whole declaration.** render.py gave "figure 1: matrix ok (14308 chars) / 1 figures, 0 errors". It is saved at /tmp/claude-0/-home-claude/e1d0222c-65c5-5625-aa10-282b96a89303/scratchpad/u9/f-ia6-5/out/replacement.json.

`{"kind": "matrix", "caption": "Screen states: the empty, error and permission states of the Perqo app screens that have them, and what each shows later, F2; supports the decision on what each screen shows under each condition and by which route the employee goes on (Deliverable B, B.5). Conditions in square brackets, as IA2's conditional area; empty-state rule this unit's synthesis from IA3, A3 and F2; the category screen's [no allocation this period] state from IA8, section 4.2 (decision log DL-008, IA9, Deliverable D; note, 9 November 2026); error states from Neusesser and Sunwall, 'Error-Message Guidelines', NN/g, 2023; permissions from Android Developers, 'Request runtime permissions', 2026 (platform documentation); disclosure from Nielsen, 'Progressive Disclosure', NN/g, 2006. Rows tone 3, the app; tone 6 marks a stop, a state in which the path ends without success until something changes (IA2, section 5.2). Blank cells: none, as in B.5's table. Perqo is fictional.", "cols": ["Empty", "Error", "Permission", "Shown later"], "rows": [{"label": "Home", "tone": 3, "cells": [{"mark": "[no category open] HR chooses the open categories; Help", "tone": 6}, {"mark": "[no connection] the last balances, with their time", "tone": 6}, null, "spent, amount and period, on the category screen"]}, {"label": "Category screen", "tone": 3, "cells": [{"mark": "[balance used up] no balance left this period; Why can't I use money from another category?; [no allocation this period] Your budget for this period is not set yet", "tone": 6}, null, "[category closed] not shown", "cross-listings, after the home items"]}, {"label": "Claims", "tone": 3, "cells": ["[no claims] How to claim back a receipt; New claim", {"mark": "[no connection] the last list, with its time", "tone": 6}, null, "the claim, on tap"]}, {"label": "New claim", "tone": 3, "cells": [null, {"mark": "[receipt missing] by the Receipt field; input kept", "tone": 6}, "[camera refused] Choose a file", "the limit, in the rule line"]}, {"label": "Check and submit", "tone": 3, "cells": [null, {"mark": "[over the balance] Edit only", "tone": 6}, null, null]}, {"label": "Claim submitted", "tone": 3, "cells": [null, null, "[first claim] the notifications prompt", null]}, {"label": "Card", "tone": 3, "cells": [{"mark": "[no card issued] not issued yet; claims still work", "tone": 6}, null, null, "card details, on tap"]}, {"label": "Purchases", "tone": 3, "cells": ["[no purchases] Where you can pay with the Perqo card", {"mark": "[no connection] the last list, with its time", "tone": 6}, null, "the purchase, on tap"]}, {"label": "Card offers", "tone": 3, "cells": ["[no offers] the route is hidden", null, "[category closed] its offers not shown", "the filter by category"]}, {"label": "Notifications", "tone": 3, "cells": ["[none yet] what will appear here", null, "[not allowed] how to allow notifications", "the claim, on tap"]}], "legend": [{"mark": "tone 3", "means": "the Perqo app", "tone": 3}, {"mark": "tone 6", "means": "a stop: the path ends without success here", "tone": 6}]}`

### Notes

1. **Renderer: word split in a narrowed column.** This one came with the 9 November change.
   - Cause: in `matrix()` (kit/viz.py, around line 1483), the width-balancing step gives a column a floor of its header's longest word only, never its cells' longest word. `_balanced` then splits "notifications" as "notificat/ions" in the Permission column, at every width and theme.
   - Evidence: rendering the pre-change Category screen cell keeps the word whole.
   - Suggested renderer fix: add the column's longest cell word to the floor `hmin`.
2. **Renderer: the legend on phones.** The legend sits inside the drawing that scrolls sideways, so it slides under the pinned label column. From frame 2 on, only fragments show ("ls without success here", "t success here") and the tone 3 chip is out of view. It is whole in frame 1.
3. **Renderer: a hidden header at 320.** In frame 1 at phone 320, the Empty header is centred beyond the visible part of the column and does not show until frame 2.
4. **Page, not figure: the opening frames.** On desktop and phone, the page's sticky header and section bar cover the figure's top rows (Home, Category screen) at the opening scroll position. The frames sheets show the figure whole.

I edited nothing. My scratch files (crops and renders) are in /tmp/claude-0/-home-claude/e1d0222c-65c5-5625-aa10-282b96a89303/scratchpad/u9/f-ia6-5/out. Writing out/report.md was refused ("Subagents should return findings as text"), so this message is the whole report.

### IA6 figure 5, second check

**IA6 "Level 2 · the client app" figure 5: fresh check (P31, an isolated context). I read only inside F and wrote only in F/out. Nothing in the unit was edited.**

The verdict is FIX, and the caption is the only thing to change. Every cell traces to B.5's table and the kind is right. The phone frames show three faults in the renderer, which the declaration cannot fix; they are under Notes.

**Figure 5: kind and section.** It is a `matrix` in Deliverable B, B.5 (Screen states), drawn just below B.5's table and its note dated 9 November 2026.

**Labels traced** (I compared every cell against B.5's table by script; all 40 match).
- Columns `Empty`, `Error`, `Permission`, `Shown later` come from the table header: "| Screen | Empty | Error | Permission | Shown later |".
- The row labels are the table's screen names without their IDs. For example, "| Home, A-1 |", "| Category screen, A-2.1 to A-2.4 |", "| Check and submit, A-3.2 |", "| Claim submitted, A-3.3 |" and "| Notifications, A-5.2 |". The other screens (Claims, New claim, Card, Purchases, Card offers) follow the same pattern.
- Cells, examples:
  - `[no category open] HR chooses the open categories; Help` matches "| Home, A-1 | [no category open] HR chooses the open categories; Help |".
  - `[balance used up] no balance left this period; Why can't I use money from another category?; [no allocation this period] Your budget for this period is not set yet` matches the Category screen row word for word.
  - `[receipt missing] by the Receipt field; input kept`, `[over the balance] Edit only` and `[first claim] the notifications prompt` each match their row.
  - The other 25 marked cells match their rows exactly.
- Every `null` sits where the table says "none". That covers all 15 blank cells.
- The added state is backed by the note: "*Note, 9 November 2026: the category screen's second empty state … added from IA8's decision (IA8, section 4.2; decision log DL-008, IA9, Deliverable D)*".
- The figure has no dates or numbers apart from the IDs in its caption. Those are covered above.

**Tones.**
- Tone 3, unit text line 12: "on a figure of one surface every box takes that surface's tone, so every app box is tone 3".
- Tone 6, same line: "tone 6, IA2's stop, marks a state where the path ends without success, or a fault found in a review (IA2, section 5.2)".
- The nine tone-6 cells fit that meaning:
  - Home: [no category open] and [no connection]
  - Category screen: [balance used up] and [no allocation this period]
  - Claims: [no connection]
  - New claim: [receipt missing]
  - Check and submit: [over the balance]
  - Card: [no card issued]
  - Purchases: [no connection]
- The states that offer a way on are tone 3. These are [no claims], [no purchases], [none yet], [camera refused] and [not allowed].

**Caption.**
- It says what the figure shows, the decision it supports, the section (Deliverable B, B.5) and the fidelity (F2), and that "Perqo is fictional". It now names the source of the added state (IA8, section 4.2 and DL-008), which was the first check's FIX.
- Still missing: the sources of the business-permission and card states. The unit gives them in section 4: "(IA2, section 5.3: only the open categories appear)" for [category closed]; "(IA4, R-11 allows 0..1)" for [no card issued]; and "(IA4, Deliverable B, R5; Hearst 2006)" with "only when Meals has an offer (R5)" for [no offers] the route is hidden. That is a should-fix, by the same standard the first check applied.

**Kind.** Items (screens) by sections (state types) is a matrix. It fits.

**Frames.**
- **Desktop 1280, dark and light:** one frame, the whole figure fits. Every label is legible, nothing is clipped or overlapping, and "notifications" is on one line in both its cells.
- **Tablet, dark and light:** one frame, same result.
- **Phone 430:** three frames. Row labels stay pinned and every column can be read whole.
- **Phone 390, 360 and 320, dark and light:** 4, 4 and 5 frames.
  - Row labels stay pinned in every frame, and the Permission and Shown later columns read whole. The "notifications" split is gone.
  - The Empty column cannot be read whole at any scroll position. The pinned label column is 133.3 units wide, so the frame leaves about 195 units for cells at 390, about 165 at 360 and about 125 at 320. The Empty column is 240.7 units wide and its longest lines are about 225. So a line like "allocation this period] Your budget" has its start hidden under the label column before its end comes into view.
  - At 320 the Error column, about 116 units of text, only just fits.
  - The declaration cannot fix this, because the screen names set the label width and the renderer sets the column widths. It is under Notes.

**Notation (IA2 section 5 and the notation sheet).**
- A row is an item, a column a dimension and a marked cell the value; conditions are in square brackets; tones 3 and 6 carry their IA2 meanings; nothing is dashed.
- One breach: the notation sheet says tones are "never the only carrier of the meaning (WCAG 2.2, 1.4.1)", and section 5.2 says "No tone is the only carrier of its meaning". In this figure, which states are stops is shown by tone alone. No cell says so and the caption only defines tone 6. Naming the stops in the caption, as IA2 allows, meets the rule without changing any cell, so the cells still match B.5 word for word.

IA6 "Level 2 · the client app" figure 5: FIX

Replacement caption. The rest of the declaration is unchanged. The whole declaration is in `F/out/replacement.md` and render.py drew it without error ("figure 1: matrix ok (14164 chars)", "1 figures, 0 errors").

`Screen states: the empty, error and permission states of the Perqo app screens that have them, and what each shows later, F2; supports the decision on what each screen shows under each condition and by which route the employee goes on (Deliverable B, B.5). Conditions in square brackets, as IA2's conditional area; empty-state rule this unit's synthesis from IA3, A3 and F2; the category screen's [no allocation this period] state from IA8, section 4.2 (decision log DL-008, IA9, Deliverable D; note, 9 November 2026); error states from Neusesser and Sunwall, 'Error-Message Guidelines', NN/g, 2023; permissions from Android Developers, 'Request runtime permissions', 2026 (platform documentation); the closed category from IA2, section 5.3, the card not yet issued from IA4, R-11, and the hidden offers route from IA4, Deliverable B, R5 (section 4); disclosure from Nielsen, 'Progressive Disclosure', NN/g, 2006. Rows tone 3, the app; tone 6 marks a stop, a state in which the path ends without success until something changes (IA2, section 5.2). The stops: Home's [no category open] and [no connection]; the category screen's [balance used up] and [no allocation this period]; Claims' and Purchases' [no connection]; New claim's [receipt missing]; Check and submit's [over the balance]; Card's [no card issued]. Blank cells: none, as in B.5's table. Perqo is fictional.`

**Notes**
- **Renderer note, Empty column on phones:** at 320, 360 and 390 px the Empty column (240.7 units) is wider than the room the pinned label column leaves (about 125, 165 and 195 units), so its longest lines are never whole on screen. The fix belongs in `matrix()` in `kit/viz.py`: on a phone, either cap a column at the frame width minus the pinned column, or wrap the row labels narrower.
- **Renderer note, legend:** the fade at the pinned column's edge runs the full height of the figure, legend included. At 390 it hides the "t" of "path" in the tone 6 entry ("a stop: the pa h ends"), and dims the same words at 360 and 320. At 320 the tone 6 legend entry is also wider than the frame, so it is never whole in one frame.
- **Capture note:** the opening frames for desktop and tablet were captured with the page's sticky header over the figure's first rows. The frame sheets for those widths show the whole figure clean, so this comes from how verify takes the opening shot, not from the figure.
- **Minor:** the row labels leave out B.5's screen IDs (A-1, A-2.1 to A-2.4, …). The caption could say they are left out, but the rows still trace.
- The restart summary is in `/tmp/claude-0/-home-claude/e1d0222c-65c5-5625-aa10-282b96a89303/scratchpad/u9/f2-ia6-5/out/report.md`. The replacement is in `/tmp/claude-0/-home-claude/e1d0222c-65c5-5625-aa10-282b96a89303/scratchpad/u9/f2-ia6-5/out/replacement.md`.

### IA6 figure 5, third check

IA6 "Level 2 · the client app", figure 5: fresh check (third check since the 9 November 2026 change)

I couldn't save the report to F/out/report.md because the harness refuses report files from subagents, so it is all here. My scratch crops and a render of the current declaration are in /tmp/claude-0/-home-claude/e1d0222c-65c5-5625-aa10-282b96a89303/scratchpad/u9/f3-ia6-5/out/. I edited nothing.

**Kind and section.** The kind is `matrix`. It sits in Deliverable B, B.5 "Screen states", directly under B.5's table and the note dated 9 November 2026 (unit-text.md line 409).

**Labels traced to the unit's text.** Every label, column and cell is taken word for word from B.5's table (unit-text.md lines 394–405). Blank cells (`null`) stand for the table's "none".

- **Columns.** `Empty`, `Error`, `Permission`, `Shown later` come from the header "| Screen | Empty | Error | Permission | Shown later |".
- **Home.** "| Home, A-1 | [no category open] HR chooses the open categories; Help | [no connection] the last balances, with their time | none | spent, amount and period, on the category screen |". All of it matches; the row label drops the ID.
- **Category screen.** "| Category screen, A-2.1 to A-2.4 | [balance used up] no balance left this period; Why can't I use money from another category?; [no allocation this period] Your budget for this period is not set yet | none | [category closed] not shown | cross-listings, after the home items |". It matches. The added state is backed by the note: "the category screen's second empty state, for a category open to the group with no allocation for the period, added from IA8's decision (IA8, section 4.2; decision log DL-008, IA9, Deliverable D)".
- **Claims.** "| Claims, A-3 | [no claims] How to claim back a receipt; New claim | [no connection] the last list, with its time | none | the claim, on tap |". It matches.
- **New claim.** "| New claim, A-3.1 | none | [receipt missing] by the Receipt field; input kept | [camera refused] Choose a file | the limit, in the rule line |". It matches.
- **Check and submit.** "| Check and submit, A-3.2 | none | [over the balance] Edit only | none | none |". It matches.
- **Claim submitted.** "| Claim submitted, A-3.3 | none | none | [first claim] the notifications prompt | none |". It matches.
- **Card.** "| Card, A-4 | [no card issued] not issued yet; claims still work | none | none | card details, on tap |". It matches.
- **Purchases.** "| Purchases, A-4.2 | [no purchases] Where you can pay with the Perqo card | [no connection] the last list, with its time | none | the purchase, on tap |". It matches.
- **Card offers.** "| Card offers, A-4.3 | [no offers] the route is hidden | none | [category closed] its offers not shown | the filter by category |". It matches.
- **Notifications.** "| Notifications, A-5.2 | [none yet] what will appear here | none | [not allowed] how to allow notifications | the claim, on tap |". It matches.
- **Legend.** `tone 3` "the Perqo app" and `tone 6` "a stop: the path ends without success here". See the tones below.
- **Dates and numbers.** The figure draws none.

No label is missing from the text, so there are no errors.

**Caption.** It names the artefact ("Screen states"), what it shows, the decision it supports, the section "(Deliverable B, B.5)", fidelity F2, and "Perqo is fictional". Each source it names traces to the unit:
- **Square brackets as IA2's conditional area.** IA2 §5.1: "Conditional area | a box whose note opens with the condition in square brackets".
- **Empty-state rule.** Line 166: "The rule below is this unit's synthesis from IA3's evidence … (IA3, A3 …) … (IA3, F2)".
- **[no allocation this period].** The note on line 407.
- **Error states.** Neusesser and Sunwall, NN/g 2023, line 172.
- **Permissions.** Android Developers, "Request runtime permissions", line 184.
- **Closed category.** Line 188: "(IA2, section 5.3: only the open categories appear)". The same line covers the Card offers [category closed] state ("nor an offer for an item in a closed category").
- **Card not yet issued.** Line 190: "(IA4, R-11 allows 0..1)".
- **Hidden offers route.** Line 166: "(IA4, Deliverable B, R5; Hearst 2006)" and line 168: "(R5)".
- **Disclosure.** Nielsen 2006, line 160.

The caption's list of stops matches the tone-6 cells exactly, eight cells covering nine states: Home Empty and Error; Category screen Empty (two states); Claims Error; New claim Error; Check and submit Error; Card Empty; Purchases Error. Both faults from the second check are fixed: the closed-category, card and offers sources are named, and the stops are listed in words. The first check's fixes also hold: the added state is sourced, and no word is split. The caption passes.

**Kind.** The data is items (ten screens) across dimensions (four kinds of state), which is "items by sections: matrix". It is not a lifecycle, so `states` does not apply. The kind fits.

**Tones.** Both tones are ones the unit's text explains:
- Tone 3 (rows and plain cells), line 12: "on a figure of one surface every box takes that surface's tone, so every app box is tone 3".
- Tone 6 (eight cells, the legend chip), line 12: "tone 6, IA2's stop, marks a state where the path ends without success, or a fault found in a review (IA2, section 5.2)".

No other tone is drawn. Blank cells use the renderer's neutral track, which the caption explains ("Blank cells: none, as in B.5's table").

**What the frames show.** I looked at every opening frame and every frame sheet, dark and light: desktop 1280, tablet, phone 390, and also 320, 360 and 430.

- **Desktop and tablet, dark and light.** One frame; the whole figure fits. Every label is legible, with no clipping and no overlap. Tone 3 and tone 6 are easy to tell apart in both themes, and the legend and caption are whole. In the desktop opening frame the page's sticky header covers the Home and Category screen rows; that comes from where the frame was taken on the page, not from the figure. The frame sheet shows those rows clear.
- **Phone 390, dark and light.** Four frames (0, 164, 328 and 372 of 372 px).
  - The row labels stay pinned in view in every frame.
  - The pinned column is 133 units (`--stick:133.3px`), which leaves about 209 px for cells.
  - The Error, Permission and Shown later columns are each shown whole in some frame (frames 2, 3 and 4).
  - The Empty column is 240.7 units wide, wider than that 209 px. No frame shows an Empty cell whole; a reader gets each one by scrolling across frames 1 and 2. There is no overlap and no text outside its cell.
  - In frame 2 the fade at the pinned column's edge also covers the legend, which is not pinned, and dims "path" to "pa h" in "a stop: the path ends…". The full legend text can be pieced together across frames 1 to 3.
- **Phone 360 and 430.** The same picture as 390. At 360 the legend reads "the ▒ath ends"; at 430 the Empty column is still clipped across frames 1 and 2.
- **Phone 320.** Five frames. The pinned column takes about half the frame, leaving about 130 px for cells. Empty cells can only be read across two frames, and Error cells fill the window from edge to edge. Everything is still legible, with no overlap.

None of these faults can be fixed in the declaration; they are listed as renderer notes below.

**Notation (IA2 §5 and the notation sheet).**
- The matrix follows IA2's rule: "In a matrix, a row is an item, a column a dimension, and a marked cell the value where they meet."
- Conditions are in square brackets: "[condition] | the path or the box exists only when this holds".
- Labels use the product's words in sentence case.
- Tones are set explicitly, one meaning each, as on the sheet: "6 | a stop: a path that ends without success, or a fault found in a review". Tone is never the only carrier of meaning, because the caption lists every stop.
- No dashed lines, no arrows.

It is drawn in IA2's notation.

IA6 "Level 2 · the client app" figure 5: PASS

Notes
- **Renderer note: legend under the fade.** On phones (320 to 430), the fade at the pinned label column's edge (shell.js/theme) runs the full height of the figure, through the legend row, which is not pinned. In mid-scroll frames it dims letters of the tone 6 legend: "the pa h ends" at 390, "the ▒ath" at 360. Fix: end the fade at the bottom of the label column, which is where `viz-lblbg` ends (height 642, legend at y 654).
- **Renderer note: Empty column too wide for phones.** The matrix gives its widest column what is left of the 700 units (Empty is 240.7). That is wider than the room the 133-unit pinned column leaves on a phone (about 209 px at 390, about 130 px at 320), so no Empty cell is ever whole in one frame. The renderer could cap a wrapping column at the phone's cell window. The declaration can't set column widths.
- **Opening-frame capture.** In the desktop and phone opening frames, the page's sticky header sits over the top rows. This is about where verify takes the frame, not about the figure.
- **Judgement worth a look, not a FIX.** Tone 6 on the three [no connection] states is the figure's own call: B.5 and section 4.3 don't name them as stops. Section 4.3 designs them to show "the last balances … with the time they were loaded", which is partial success, and it gives [receipt missing] a remedy. The caption's wording, "until something changes", covers both, and the caption lists them. If the author means "stop" in IA2's stricter sense, those cells could go to tone 3. The figure is consistent as drawn.
- **Minor wording.** The caption doesn't say outright that the data is B.5's table; it points there only through "(Deliverable B, B.5)" and "as in B.5's table". That is enough.

Nothing in this report came from memory.

### IA7 figure 3, first check

# IA7 "Level 3 · the backoffice", figure 3: fresh figure check

**Verdict: FIX.** The main fault is in what the reader sees (check 8): the two counts on the policy–catalogue item line run into each other at every width and in both themes. There is also one caption should-fix (check 7) and two notation fixes (check 9). The full report is at /tmp/claude-0/-home-claude/e1d0222c-65c5-5625-aa10-282b96a89303/scratchpad/u9/f-ia7-3/out/report.md, and the replacement is in out/fig3-replacement.md in the same folder.

## Kind and section
- **Kind:** `objects`.
- **Section:** Deliverable A, A.5 "The map, drawn", figure 1 of 2.

## Labels traced (quoted from the unit)
Every label is in the unit's text.

**client**
- `client`, `O-01`, `Admin: Company, in Settings`, `volume: 1`: A.1 "| O-01 | client (`client`) | Company, in Settings | 1 |".
- `name`, `contract start date`, `contract end date`: A.2 "O-01 client | name → `name`; contract start date → `contract_start_date`; contract end date (IA8) → `contract_end_date` (proposed)", plus the A.2 note "*Note, 9 November 2026: three fields added from IA8's decisions … the client's `contract_end_date`*".
- `-> edit company details (owner)`: A.4 "| client | -> edit company details | account owner *new* (section 3.4) |".

**admin user**
- `admin user`, `O-02`, `Admin: Admins, in Settings`, `volume: 3`: A.1 "| O-02 | admin user (`admin_user`) | Admins, in Settings | 3 *new* |".
- `name`, `work email`, `role`, `account owner`, `status`: A.2.
- `-> add` / `-> remove` / `-> change role` / `-> make account owner (owner)`: A.4 "| admin user | -> add | account owner *new* |" and "| admin user | -> remove *new*; -> change role *new*; -> make account owner *new* | account owner |".

**employee group**
- `employee group`, `O-03`, `volume: 14`, `queue: No budget for next period`: A.1 "| O-03 | employee group (`employee_group`) | Employee group, in Employees | 14 *new* | none | No budget for next period *new* |".
- `name`: A.2.
- `-> create (HR)`, `-> invite employees (HR)`: A.4 "| employee group | -> create; -> invite employees (only once the group's budgets for the current period are set; IA8, section 3.2) | HR manager |".

**employee**
- `employee`, `O-05`, `Admin: Employees`, `volume: 1,200`, `queue: Not joined`: A.1 "| O-05 | employee (`employee`) | Employees | 1,200 *new* | Invited, Active, Left *new* | Not joined *new* |".
- `name`, `work email`, `status`: A.2.
- `→ see figure 2`: A.5, 'with "→ see" lines where an object continues in the other'.
- `-> invite`, `-> move to group`: A.4 "| employee | -> invite (only into a group whose budgets for the current period are set; IA8, section 3.2); -> move to group | HR manager |".
- `-> resend invitation`, `-> mark as left`: A.4 "| employee | -> resend invitation *new*; -> mark as left *new* | HR manager |".

**policy**
- `policy`, `O-04`, `Admin: Policy`, `volume: 14`: A.1 "| O-04 | policy (`policy`) | Policy, in Policies | 14, one per group (R-03) |".
- `open categories`, `auto-approve limit`, `covered items`: A.2.
- `-> edit (HR)`, `-> add covered items (HR)`: A.4 "| policy | -> edit; -> add covered items | HR manager |".

**catalogue item**
- `catalogue item`, `O-13`, `Admin: Covered items, in Policies`, `volume: 12 in the sample`: A.1 "| O-13 | catalogue item (`catalogue_item`) | Covered items, in Policies | 12 in the sample (IA4) |".
- `ID`, `name`, `facet values`: A.2 "ID → `id`; name → `name`; the four facet values → `facets`".
- `-> view (HR, finance)`: A.4 "| catalogue item | -> view *new* in Admin | HR manager, finance manager |".

**Links (all from A.3)**
- R-01 "| client | has | admin user | 1, 1..* |".
- R-02 "| client | has | employee group | 1, 1..* |".
- R-03 "| employee group | follows | policy | 1, 1 |".
- R-04 "| employee group | contains | employee | 1, 1..* |".
- R-07 "| policy | covers | catalogue item | 0..*, 0..* |".
- R-21 "| admin user | is also | employee | 0..1, 0..1 |".

These match A.5's list, "R-01 to R-04, R-07, R-21". Every relationship label reads the right way: left to right on a level line, top to bottom otherwise.

## Caption
The caption names the artefact, what it shows, the decision it supports, the section (Deliverable A), that volumes are assumed, the tone, the reading direction, its sources, and "Perqo is fictional".

**Should-fix:** it does not give a source for the attribute added on 9 November, "contract end date". A.2 gives it as "(IA8)", and the A.2 note gives "IA8, sections 3.2 and 3.4; decision log DL-005 and DL-006". None of the caption's listed sources covers it.

## Kind
`objects` fits: the data is things and the relationships between them.

## Frames
I looked at desktop 1280 and tablet (one frame each, the whole figure fits) and at phones 390, 320, 360 and 430 (three or four sideways frames each, opening at 78), in dark and light.

**FIX:** in every sheet, the counts on the R-07 line between policy and catalogue item collide and print as `0..*0..*`, with the asterisk touching the zero. A 6x crop confirms it (out/crop-desk-covers-dark.png).
- The cause is the renderer's layout: the gap between two boxes on a level line widens for a long label but never for the counts at its ends. At the default gap the two count centres are only 16 units apart, which is less than the width of one "0..*".
- The declaration can avoid it, so this is a FIX, not only a renderer note: put catalogue item under policy, so R-07 is drawn as a vertical line.

**Everything else is clean:**
- All other labels are legible in both themes, and nothing else overlaps.
- In the middle phone frames the scroll edge fades out part of a box, but every box is shown whole in another frame.
- The only tone drawn is tone 4. Its meaning is in the text, line 14: "Admin's boxes take tone 4, Perqo Admin; on a figure of one surface every box takes that surface's tone (IA2, section 5.2)". A.5 repeats it. There is no tone 6.

## Notation
The figure follows IA2's notation:
- each box has a title band, then attributes, a rule line, and "-> verb" actions;
- lines have no heads and none is dashed;
- counts use UML multiplicity notation;
- the title is the model name in lower case, with an "Admin: Label" line;
- "assumed" for the volumes is in the caption.

Two fixes:

**(a) `→ see figure 2` points two ways.** It is meant to point to the map's figure 2 of 2 (the unit's figure 4). But the unit's own figure 2 is the employee state diagram, which has no policy in it. IA2's notation sheet says "→ see *name*: continues in that figure or node". The fix uses the captions' own name: `→ see figure 2 of 2`.

**(b) The invite actions are missing the condition A.4 gained on 9 November.** A.4 now says invite only works "only once the group's budgets for the current period are set", and C.4 says until then Invite employees "is shown disabled". This figure is the F3 map that permissions are read from (section 6.3: "Permissions are written once, on the calls to action"), and IA2 writes a condition in square brackets. The fix adds A.4's wording, word for word, in brackets.

IA7 "Level 3 · the backoffice" figure 3: FIX

**Replacement.** This is the whole declaration. `python3 render.py out/fig3-replacement.md` gave "figure 1: objects ok (10552 chars) / 1 figures, 0 errors". I also took screenshots with theme.css at 1280 and 390 px, dark and light (out/new-*.png): the counts sit clear and nothing is clipped.

`{"kind": "objects", "caption": "Object-relationship map, figure 1 of 2, setup: the Admin objects HR and the account owner configure, with IDs, Admin labels, attributes, volumes for the sizing client (assumed), work queues, calls to action with their roles and conditions, and counts in UML multiplicity notation, F3 (model names in A.2); supports the decision on what Admin holds and who changes it (Deliverable A). Every box tone 4, Perqo Admin, because the figure shows one surface. Lines read left to right on a level line, top to bottom otherwise. R-01 to R-04 and R-07 from IA4, Deliverable A, labels and counts kept; R-21, the account owner, employee status and the volumes set in section 2.2 and section 3.4; contract end date from IA8, sections 3.2 and 3.4, as A.2 and its note of 9 November 2026 give it (DL-005 and DL-006); the condition on inviting from IA8, section 3.2, as A.4 gives it (DL-007, Deliverable C, C.4); object-first method from Prater, A List Apart, 2015 and 2016. Perqo is fictional.", "objects": [{"id": "client", "title": "client", "tone": 4, "attrs": ["O-01", "Admin: Company, in Settings", "name", "contract start date", "contract end date", "volume: 1"], "actions": ["-> edit company details (owner)"]}, {"id": "admin", "title": "admin user", "tone": 4, "attrs": ["O-02", "Admin: Admins, in Settings", "name", "work email", "role", "account owner", "status", "volume: 3"], "actions": ["-> add (owner)", "-> remove (owner)", "-> change role (owner)", "-> make account owner (owner)"]}, {"id": "group", "title": "employee group", "tone": 4, "attrs": ["O-03", "Admin: Employee group", "name", "volume: 14", "queue: No budget for next period"], "actions": ["-> create (HR)", "-> invite employees (HR) [only once the group's budgets for the current period are set]"]}, {"id": "employee", "title": "employee", "tone": 4, "attrs": ["O-05", "Admin: Employees", "name", "work email", "status", "volume: 1,200", "queue: Not joined", "→ see figure 2 of 2"], "actions": ["-> invite (HR) [only into a group whose budgets for the current period are set]", "-> resend invitation (HR)", "-> move to group (HR)", "-> mark as left (HR)"]}, {"id": "policy", "title": "policy", "tone": 4, "attrs": ["O-04", "Admin: Policy", "open categories", "auto-approve limit", "covered items", "volume: 14", "→ see figure 2 of 2"], "actions": ["-> edit (HR)", "-> add covered items (HR)"]}, {"id": "item", "title": "catalogue item", "tone": 4, "attrs": ["O-13", "Admin: Covered items, in Policies", "ID", "name", "facet values", "volume: 12 in the sample"], "actions": ["-> view (HR, finance)"]}], "rows": [["client", "admin"], ["group", "employee"], ["policy", null], ["item", null]], "links": [{"from": "client", "to": "admin", "label": "has", "from_card": "1", "to_card": "1..*"}, {"from": "client", "to": "group", "label": "has", "from_card": "1", "to_card": "1..*"}, {"from": "admin", "to": "employee", "label": "is also", "from_card": "0..1", "to_card": "0..1"}, {"from": "group", "to": "employee", "label": "contains", "from_card": "1", "to_card": "1..*"}, {"from": "group", "to": "policy", "label": "follows", "from_card": "1", "to_card": "1"}, {"from": "policy", "to": "item", "label": "covers", "from_card": "0..*", "to_card": "0..*"}]}`

**What changed:**
- `rows`: catalogue item moves to its own fourth row under policy, which removes the count collision (check 8).
- Both invite actions carry A.4's condition in brackets (check 9).
- `→ see figure 2` becomes `→ see figure 2 of 2` in the employee and policy boxes (check 9).
- The caption adds "and conditions", plus sources for contract end date and for the invite condition (check 7).

Every other label, count and tone is unchanged.

## Notes
- **Minor:** `Admin: Employee group` and `Admin: Policy` leave out the place A.1 gives ("in Employees", "in Policies"); the client, admin user and catalogue item boxes include theirs. A.5 asks only for "the label people see", so I left this as it is.
- **Minor:** box titles write model names as words (`admin user`) where A.1 has `admin_user`. That is the course convention, as in IA2's own figures ("transaction, type claim"), so it is not an error.
- **Minor:** the "(proposed)" in A.2 is on the model field name `contract_end_date`, which the figure does not show, so the figure needs no "proposed".
- **Optional:** fix (b), the invite conditions, is a judgement call. The collision fix and the caption fix stand without it if it is dropped.
- **Renderer note:** in `objects()` in viz.py, the gap between boxes on a level line widens for a long label and for a direction mark, but not for the counts at its ends. So "0..*" at both ends of a level line will always collide at the default 56-unit gap. The gap needs to be at least 40 + half of each count's width + 4.
- **Renderer note:** in the opening screenshots, the page's sticky reader header covers the top of the figure. That is page chrome at the saved scroll position, not the figure; the frame sheets show the figure clear.

Everything is in /tmp/claude-0/-home-claude/e1d0222c-65c5-5625-aa10-282b96a89303/scratchpad/u9/f-ia7-3/out/:
- report.md
- fig3-replacement.md
- new-*.png and old-*.png (screenshots of the replacement and the current figure)
- crop-desk-covers-*.png
- sheet-* and contact-* (slices of the frame sheets)

### IA7 figure 3, second check

## IA7 "Level 3 · the backoffice", figure 3: FIX

Two things are wrong:
- **Missing continuation line.** The admin user box has no "→ see figure 2 of 2", although the admin user continues in figure 2.
- **Caption sourcing.** The caption names the work queues but gives no source for them. It also gives no source for admin user status.

Everything else passes: every label traced to the text, the kind, the frames at every width and theme, and the tones and notation. The replacement JSON is at the end, and it renders without error.

**Kind and section.** `objects`. It sits in Deliverable A, A.5 "The map, drawn", as the first of two figures.

### Labels, numbers and counts traced
- **client.**
  - `O-01` and `Admin: Company, in Settings`: A.1 "| O-01 | client (`client`) | Company, in Settings | 1 |".
  - `name`, `contract start date`, `contract end date`: A.2 "name → `name`; contract start date → `contract_start_date`; contract end date (IA8) → `contract_end_date` (proposed)".
  - `volume: 1`: A.1, as above.
  - `-> edit company details (owner)`: A.4 "| client | -> edit company details | account owner *new*".
- **admin user.**
  - `O-02`, `Admin: Admins, in Settings`, `volume: 3`: A.1 "| O-02 | admin user (`admin_user`) | Admins, in Settings | 3 *new*".
  - `name`, `work email`, `role`, `account owner`, `status`: A.2 "name → `name`; work email → `work_email`; role … account owner *new* → `is_account_owner`; status *new*".
  - `-> add / remove / change role / make account owner (owner)`: A.4 "| admin user | -> add | account owner" and "-> remove *new*; -> change role *new*; -> make account owner *new* | account owner".
- **employee group.**
  - `O-03`, `Admin: Employee group`, `volume: 14`, `queue: No budget for next period`: A.1 "| O-03 | employee group (`employee_group`) | Employee group, in Employees | 14 *new* | none | No budget for next period *new*".
  - `name`: A.2.
  - `-> create (HR)` and `-> invite employees (HR) [only once the group's budgets for the current period are set]`: A.4 "| employee group | -> create; -> invite employees (only once the group's budgets for the current period are set; IA8, section 3.2) | HR manager".
- **employee.**
  - `O-05`, `Admin: Employees`, `volume: 1,200`, `queue: Not joined`: A.1 "| O-05 | employee (`employee`) | Employees | 1,200 *new* | Invited, Active, Left *new* | Not joined *new*".
  - `name`, `work email`, `status`: A.2.
  - `-> invite (HR) [only into a group whose budgets for the current period are set]` and `-> move to group (HR)`: A.4 line 343.
  - `-> resend invitation (HR)` and `-> mark as left (HR)`: A.4 line 344.
  - `→ see figure 2 of 2`: A.5 says the second figure holds "the employee's card, claims and allocations" (R-05, R-08, R-11).
- **policy.**
  - `O-04`, `Admin: Policy`, `volume: 14`: A.1 "| O-04 | policy (`policy`) | Policy, in Policies | 14, one per group (R-03)".
  - `open categories`, `auto-approve limit`, `covered items`: A.2.
  - `-> edit (HR)` and `-> add covered items (HR)`: A.4 "| policy | -> edit; -> add covered items | HR manager".
  - `→ see figure 2 of 2`: A.5, "the policy a claim is checked against".
- **catalogue item.**
  - `O-13`, `Admin: Covered items, in Policies`, `volume: 12 in the sample`: A.1 "| O-13 | catalogue item (`catalogue_item`) | Covered items, in Policies | 12 in the sample (IA4)".
  - `ID`, `name`, `facet values`: A.2 "ID → `id`; name → `name`; the four facet values → `facets`".
  - `-> view (HR, finance)`: A.4 "| catalogue item | -> view *new* in Admin | HR manager, finance manager".
- **Role abbreviations.** A.1: "HR (HR manager), finance (finance manager), owner (account owner)".
- **Links.** All six match A.3, and A.5 says this figure holds exactly "R-01 to R-04, R-07, R-21".

| Line | A.3 row | Counts |
|---|---|---|
| client `has` admin user | R-01 | 1, 1..* |
| client `has` employee group | R-02 | 1, 1..* |
| employee group `follows` policy | R-03 | 1, 1 |
| employee group `contains` employee | R-04 | 1, 1..* |
| policy `covers` catalogue item | R-07 | 0..*, 0..* |
| admin user `is also` employee | R-21 | 0..1, 0..1 |

**Error: a missing "→ see".**
- The admin user also appears in figure 2:
  - A.5: "The second holds … the admin user who decides a claim … (R-05, R-08 to R-13, R-22 to R-24)".
  - Figure 4's caption covers R-22 ("is decided by admin user") and R-24.
- A.5 sets the rule: "Split in two figures … with "→ see" lines where an object continues in the other."
- The employee and policy boxes carry the line; the admin user box does not.
- The client and employee group do not appear in figure 2 ("R-06 and R-23's other objects are in A.3 only"), so they rightly have none.

### Caption
It names the artefact and fidelity, says what the figure shows and which decision it supports, names the section (Deliverable A) and says "Perqo is fictional". Every source it gives checks against the text:
- R-01 to R-04 and R-07 from IA4.
- R-21, the account owner, employee status and volumes: sections 2.2 and 3.4.
- Contract end date: A.2 and its note of 9 November 2026 (line 305, DL-005 and DL-006).
- The condition on inviting: A.4, and C.4 line 449 "decision log DL-007".
- Prater 2015 and 2016: section 2.1.

What is missing (should-fix):
- **Work queues.** The caption lists "work queues" among what the figure shows but gives no source. `queue: No budget for next period` and `queue: Not joined` were set in section 4.2 ("Deliverable C, C.4 adds two: Not joined … and No budget for next period") and in C.4.
- **Admin user status.** The box's `status` is a new attribute set in section 2.2 ("**Admin user status.** Active or Removed"). The caption sources only employee status.

### Kind
`objects` is right for things and relationships.

### The frames
I looked at every frame. At every width and in both themes:
- every label is legible;
- nothing is clipped or overlapping;
- every count's text stays clear of every other count (the earlier fault where counts ran together is gone);
- the edge fade covers text only at a scroll edge, and the next frame shows that text whole.

| Width | Frames | What they show |
|---|---|---|
| Desktop 1280, dark and light | 1 of 1, whole figure fits | All six boxes, six lines, counts and caption clear. The opening screenshot has the page's sticky header across the middle of the figure; the frames sheet shows that is page chrome over a scrolled page, not a figure fault. |
| Tablet, dark and light | 1 of 1, fits | Clean. |
| Phone 390, dark and light | 3 frames (78, 242, 372 of 372 px) | Frame 1: left column whole. Frame 2: the "has" and "contains" level lines, both counts and the "is also" line clear. Frame 3: right column whole, including "-> make account owner (owner)" and the invite condition. |
| Phone 320 | 4 frames | Same pattern, nothing clipped. |
| Phone 360 | 4 frames | Same pattern, nothing clipped. |
| Phone 430 | 3 frames | Same pattern, nothing clipped. |

**Tones.** Only tone 4 is drawn. Its meaning is stated in the unit: "Admin's boxes take tone 4, Perqo Admin; on a figure of one surface every box takes that surface's tone (IA2, section 5.2)" (intro), and "Every box is tone 4, Perqo Admin, because the map shows one surface" (A.5). There is no matrix and no tone 6.

### Notation (IA2, section 5 and the notation sheet)
It follows IA2 throughout:
- object boxes with a filled title band;
- the title is the model name in lower case;
- "Admin: Label" lines;
- actions written `-> verb`, after a rule line;
- conditions in square brackets;
- lines without heads, with counts in UML multiplicity at each end;
- every label reads left to right on a level line and top to bottom otherwise, so no triangle is needed;
- `→ see` continuation lines (except the one missing above);
- "assumed" is in the caption.

IA7 "Level 3 · the backoffice" figure 3: FIX

### Replacement JSON
I rendered it with `python3 render.py out/fig3-fix.md`: "figure 1: objects ok … 1 figures, 0 errors".
- **What changed:** `→ see figure 2 of 2` is added to the admin user box, and the caption now sources admin user status and the work queues.
- **Layout check:** The new line moves everything below row 1 down 14 units and makes no other change to the layout.
- **Screenshots:** The desktop shots (1280, dark and light) are clean. The phone shot at 390 px was taken without the site's opening-scroll script, so it is not a like-for-like phone frame.

```viz
{"kind": "objects", "caption": "Object-relationship map, figure 1 of 2, setup: the Admin objects HR and the account owner configure, with IDs, Admin labels, attributes, volumes for the sizing client (assumed), work queues, calls to action with their roles and conditions, and counts in UML multiplicity notation, F3 (model names in A.2); supports the decision on what Admin holds and who changes it (Deliverable A). Every box tone 4, Perqo Admin, because the figure shows one surface. Lines read left to right on a level line, top to bottom otherwise. R-01 to R-04 and R-07 from IA4, Deliverable A, labels and counts kept; R-21, the account owner, employee and admin user status and the volumes set in section 2.2 and section 3.4; the work queues from section 4.2 and Deliverable C, C.4; contract end date from IA8, sections 3.2 and 3.4, as A.2 and its note of 9 November 2026 give it (DL-005 and DL-006); the condition on inviting from IA8, section 3.2, as A.4 gives it (DL-007, Deliverable C, C.4); object-first method from Prater, A List Apart, 2015 and 2016. Perqo is fictional.", "links": [{"from": "client", "to": "admin", "label": "has", "from_card": "1", "to_card": "1..*"}, {"from": "client", "to": "group", "label": "has", "from_card": "1", "to_card": "1..*"}, {"from": "admin", "to": "employee", "label": "is also", "from_card": "0..1", "to_card": "0..1"}, {"from": "group", "to": "employee", "label": "contains", "from_card": "1", "to_card": "1..*"}, {"from": "group", "to": "policy", "label": "follows", "from_card": "1", "to_card": "1"}, {"from": "policy", "to": "item", "label": "covers", "from_card": "0..*", "to_card": "0..*"}], "objects": [{"id": "client", "title": "client", "tone": 4, "attrs": ["O-01", "Admin: Company, in Settings", "name", "contract start date", "contract end date", "volume: 1"], "actions": ["-> edit company details (owner)"]}, {"id": "admin", "title": "admin user", "tone": 4, "attrs": ["O-02", "Admin: Admins, in Settings", "name", "work email", "role", "account owner", "status", "volume: 3", "→ see figure 2 of 2"], "actions": ["-> add (owner)", "-> remove (owner)", "-> change role (owner)", "-> make account owner (owner)"]}, {"id": "group", "title": "employee group", "tone": 4, "attrs": ["O-03", "Admin: Employee group", "name", "volume: 14", "queue: No budget for next period"], "actions": ["-> create (HR)", "-> invite employees (HR) [only once the group's budgets for the current period are set]"]}, {"id": "employee", "title": "employee", "tone": 4, "attrs": ["O-05", "Admin: Employees", "name", "work email", "status", "volume: 1,200", "queue: Not joined", "→ see figure 2 of 2"], "actions": ["-> invite (HR) [only into a group whose budgets for the current period are set]", "-> resend invitation (HR)", "-> move to group (HR)", "-> mark as left (HR)"]}, {"id": "policy", "title": "policy", "tone": 4, "attrs": ["O-04", "Admin: Policy", "open categories", "auto-approve limit", "covered items", "volume: 14", "→ see figure 2 of 2"], "actions": ["-> edit (HR)", "-> add covered items (HR)"]}, {"id": "item", "title": "catalogue item", "tone": 4, "attrs": ["O-13", "Admin: Covered items, in Policies", "ID", "name", "facet values", "volume: 12 in the sample"], "actions": ["-> view (HR, finance)"]}], "rows": [["client", "admin"], ["group", "employee"], ["policy", null], ["item", null]]}
```

The replacement is also saved in the folder, at /tmp/claude-0/-home-claude/e1d0222c-65c5-5625-aa10-282b96a89303/scratchpad/u9/f2-ia7-3/out/fig3-fix.md. I could not write out/report.md: the harness refused report files, so this reply is the whole report.

### Notes (not a FIX)
- **Place in the "Admin:" lines.** Four boxes give the label with its place ("Company, in Settings", "Admins, in Settings", "Covered items, in Policies", and "Employees", which is the place itself). Two drop the place that A.1 gives: `Admin: Employee group` (A.1: "Employee group, in Employees") and `Admin: Policy` (A.1: "Policy, in Policies"). Both trace, and A.5 says the line "gives the label people see", so this is not an error. The figure would read more evenly if those two also carried ", in Employees" and ", in Policies", or if every box dropped the place.
- **Renderer / page note.** In the desktop opening screenshot, the page's sticky section header covers the middle of the figure. This is page chrome at that scroll position, not a figure fault, and the frames sheet shows the figure whole.
- **First check's points.** All four items the first check reported are now resolved in the declaration:
  - the catalogue item's counts no longer run together (it now sits under policy);
  - the contract end date and the invite condition are sourced in the caption;
  - both invite actions carry the bracketed condition;
  - "→ see" reads "→ see figure 2 of 2".

### IA7 figure 3, third check

**IA7 "Level 3 · the backoffice", figure 3: fresh figure check (P31; isolated context; nothing edited)**

**Figure 3: its kind and section.** The kind is `objects`. It sits in Deliverable A, A.5 "The map, drawn", and is figure 1 of 2. Six boxes in four rows: client and admin user; employee group and employee; policy; catalogue item. Six lines.

**Every label, date and number traced to the unit's text.** Every label, ID and count in the figure is in the unit's text. There are no dates.

- **client box**
  - `O-01`, `Admin: Company, in Settings`, `volume: 1`: A.1, "| O-01 | client (`client`) | Company, in Settings | 1 |".
  - `name`, `contract start date`, `contract end date`: A.2, "name → `name`; contract start date → `contract_start_date`; contract end date (IA8) → `contract_end_date` (proposed)".
  - `-> edit company details (owner)`: A.4, "client | -> edit company details | account owner *new* (section 3.4)". The abbreviation is A.1's: "owner (account owner)".
- **admin user box**
  - `O-02`, `Admin: Admins, in Settings`, `volume: 3`: A.1, "| O-02 | admin user (`admin_user`) | Admins, in Settings | 3 *new*".
  - `name`, `work email`, `role`, `account owner`, `status`: A.2, "name …; work email …; role (HR manager or finance manager) …; account owner *new* → `is_account_owner`; status *new* → `status` (`active`, `removed`)".
  - `→ see figure 2 of 2`: A.5, "with "→ see" lines where an object continues in the other"; figure 2 of 2 holds "the admin user who decides a claim".
  - `-> add`, `-> remove`, `-> change role`, `-> make account owner`, all `(owner)`: A.4, "admin user | -> add | account owner *new*" and "admin user | -> remove *new*; -> change role *new*; -> make account owner *new* | account owner".
- **employee group box**
  - `O-03`, `Admin: Employee group, in Employees`, `volume: 14`, `queue: No budget for next period`: A.1, "| O-03 | employee group (`employee_group`) | Employee group, in Employees | 14 *new* | none | No budget for next period *new*".
  - `name`: A.2, "O-03 employee group | name → `name`".
  - `-> create (HR)`, `-> invite employees (HR) [only once the group's budgets for the current period are set]`: A.4, "employee group | -> create; -> invite employees (only once the group's budgets for the current period are set; IA8, section 3.2) | HR manager".
- **employee box**
  - `O-05`, `Admin: Employees`, `volume: 1,200`, `queue: Not joined`: A.1, "| O-05 | employee (`employee`) | Employees | 1,200 *new* | Invited, Active, Left *new* | Not joined *new*".
  - `name`, `work email`, `status`: A.2.
  - `→ see figure 2 of 2`: A.5, "the employee's card, claims and allocations".
  - `-> invite (HR) [only into a group whose budgets for the current period are set]`, `-> move to group (HR)`: A.4, "employee | -> invite (only into a group whose budgets for the current period are set; IA8, section 3.2); -> move to group | HR manager".
  - `-> resend invitation (HR)`, `-> mark as left (HR)`: A.4, "employee | -> resend invitation *new*; -> mark as left *new* | HR manager".
- **policy box**
  - `O-04`, `Admin: Policy, in Policies`, `volume: 14`: A.1, "| O-04 | policy (`policy`) | Policy, in Policies | 14, one per group (R-03)".
  - `open categories`, `auto-approve limit`, `covered items`: A.2.
  - `→ see figure 2 of 2`: A.5, "the policy a claim is checked against".
  - `-> edit (HR)`, `-> add covered items (HR)`: A.4, "policy | -> edit; -> add covered items | HR manager".
- **catalogue item box**
  - `O-13`, `Admin: Covered items, in Policies`, `volume: 12 in the sample`: A.1, "| O-13 | catalogue item (`catalogue_item`) | Covered items, in Policies | 12 in the sample (IA4)".
  - `ID`, `name`, `facet values`: A.2, "ID → `id`; name → `name`; the four facet values → `facets`".
  - `-> view (HR, finance)`: A.4, "catalogue item | -> view *new* in Admin | HR manager, finance manager".
- **Lines (A.3)**
  - `has` 1 / 1..*: "| R-01 | client | has | admin user | 1, 1..* |".
  - `has` 1 / 1..*: "| R-02 | client | has | employee group | 1, 1..* |".
  - `follows` 1 / 1: "| R-03 | employee group | follows | policy | 1, 1 |".
  - `contains` 1 / 1..*: "| R-04 | employee group | contains | employee | 1, 1..* |".
  - `covers` 0..* / 0..*: "| R-07 | policy | covers | catalogue item | 0..*, 0..* |".
  - `is also` 0..1 / 0..1: "| R-21 *new* | admin user | is also | employee | 0..1, 0..1 |".
- **Placement.** Each line reads left to right on a level line and top to bottom otherwise. No line needs a direction triangle.

**The caption.** It says what the figure shows and names its section (Deliverable A, A.5). Most of its sourcing checks out:
- R-21, the account owner, the two statuses and the volumes: sections 2.2 and 3.4.
- The work queues: section 4.2 ("Deliverable C, C.4 adds two: Not joined … and No budget for next period") and C.4.
- Contract end date: A.2 and its note of 9 November 2026, which cites DL-005 and DL-006.
- The condition on inviting: A.4 and C.4 ("IA8, section 3.2; decision log DL-007").
- Prater 2015 and 2016: section 2.1.
- The tone sentence matches A.5.

It fails the sourcing rule in three places. **Should-fix:**
1. **Most of the figure has no source in the caption.** The caption gives IA4 only "R-01 to R-04 and R-07". The objects, their O- IDs, their Admin labels, IA4's attributes and IA4's calls to action with their roles (create, invite employees, edit, add covered items, invite, move to group) are left unsourced. The unit gives these to IA4:
   - Section 2.1: "IA4's identifiers, O-01 to O-16 and R-01 to R-20, are kept".
   - Section 2.2: "Every object below keeps its IA4 label, attributes and relationships".
   - A.4: "IA4's kept and this unit's added".
2. **One volume is credited to the wrong source.** `volume: 12 in the sample` is IA4's (A.1: "12 in the sample (IA4)"), but the caption puts it under "the volumes set in section 2.2".
3. **`-> resend invitation` has no source.** It is set in section 4.4: "employee -> resend invitation, for selected employees (HR, in Not joined)".

**The kind.** Things and their relationships → `objects`. The kind fits.

**The frames at each width and theme.**
- **Desktop, dark and light.** One frame, the whole figure fits. Every label is legible, and nothing is clipped or overlapping. The opening captures show the page's sticky header across the middle of the figure; that is page chrome over a capture taller than the screen, and the sheet frame is clean.
- **Tablet, dark and light.** One frame, the whole figure fits. Every label is legible, nothing is clipped or overlapping. Counts, line labels and the wrapped bracketed conditions stay clear of each other.
- **Phone 390, dark and light.** Three frames; the figure opens at 78 of 372 px.
  - Frame 1 shows the whole left column: client, employee group, policy, catalogue item, and the has, follows and covers lines with their counts.
  - Frame 3 shows the whole right column: admin user, employee and the "is also" line with its counts.
  - Frame 2 cuts both columns at the edges, with the scroll fade.
  - Every label appears whole in at least one frame, and nothing overlaps. Grey action text on the light box fill is legible.
- **Phone 320, 360 and 430** (extra sheets). The same holds: the left column is whole in frame 1 and the right column whole in a late frame (320: frame 3 at 336 px; 360: frame 3; 430: frame 3).
- **Tones.** Only tone 4 is drawn. A.5 gives its meaning: "Every box is tone 4, Perqo Admin, because the map shows one surface". No tone 6.

**The notation (IA2, section 5 and the notation sheet).**
- Boxes have a filled title band, attributes below it, a rule line, then "-> verb" actions.
- Lines have no heads and mean "relates". Each label is a verb read left to right or top to bottom, with UML counts at both ends.
- Conditions are in square brackets.
- Continuations are written "→ see figure 2 of 2".
- The title is the data-model name in lower case, with an "Admin: Label" line.
- One surface, so every box takes that surface's tone.
- Nothing is dashed.

The figure is in IA2's notation.

IA7 "Level 3 · the backoffice" figure 3: FIX

**Replacement caption.** Only the sources part changes:
`Object-relationship map, figure 1 of 2, setup: the Admin objects HR and the account owner configure, with IDs, Admin labels, attributes, volumes for the sizing client (assumed), work queues, calls to action with their roles and conditions, and counts in UML multiplicity notation, F3 (model names in A.2); supports the decision on what Admin holds and who changes it (Deliverable A). Every box tone 4, Perqo Admin, because the figure shows one surface. Lines read left to right on a level line, top to bottom otherwise. The objects, their IDs, Admin labels and attributes, and the calls to action with their roles from IA4, Deliverable A, kept (sections 2.1 and 2.2), with this unit's additions as A.1 to A.4 mark them; R-01 to R-04 and R-07 from IA4, Deliverable A, labels and counts kept; the catalogue items' volume from IA4, as A.1 gives it; R-21, the account owner and its calls to action, employee and admin user status and the other volumes set in section 2.2 and section 3.4; resend invitation from section 4.4; the work queues from section 4.2 and Deliverable C, C.4; contract end date from IA8, sections 3.2 and 3.4, as A.2 and its note of 9 November 2026 give it (DL-005 and DL-006); the condition on inviting from IA8, section 3.2, as A.4 gives it (DL-007, Deliverable C, C.4); object-first method from Prater, A List Apart, 2015 and 2016. Perqo is fictional.`

**Replacement declaration.** I rendered it with render.py: "figure 1: objects ok (11131 chars) / 1 figures, 0 errors". The current declaration also renders cleanly (10810 chars).
`{"kind": "objects", "caption": "Object-relationship map, figure 1 of 2, setup: the Admin objects HR and the account owner configure, with IDs, Admin labels, attributes, volumes for the sizing client (assumed), work queues, calls to action with their roles and conditions, and counts in UML multiplicity notation, F3 (model names in A.2); supports the decision on what Admin holds and who changes it (Deliverable A). Every box tone 4, Perqo Admin, because the figure shows one surface. Lines read left to right on a level line, top to bottom otherwise. The objects, their IDs, Admin labels and attributes, and the calls to action with their roles from IA4, Deliverable A, kept (sections 2.1 and 2.2), with this unit's additions as A.1 to A.4 mark them; R-01 to R-04 and R-07 from IA4, Deliverable A, labels and counts kept; the catalogue items' volume from IA4, as A.1 gives it; R-21, the account owner and its calls to action, employee and admin user status and the other volumes set in section 2.2 and section 3.4; resend invitation from section 4.4; the work queues from section 4.2 and Deliverable C, C.4; contract end date from IA8, sections 3.2 and 3.4, as A.2 and its note of 9 November 2026 give it (DL-005 and DL-006); the condition on inviting from IA8, section 3.2, as A.4 gives it (DL-007, Deliverable C, C.4); object-first method from Prater, A List Apart, 2015 and 2016. Perqo is fictional.", "links": [{"from": "client", "to": "admin", "label": "has", "from_card": "1", "to_card": "1..*"}, {"from": "client", "to": "group", "label": "has", "from_card": "1", "to_card": "1..*"}, {"from": "admin", "to": "employee", "label": "is also", "from_card": "0..1", "to_card": "0..1"}, {"from": "group", "to": "employee", "label": "contains", "from_card": "1", "to_card": "1..*"}, {"from": "group", "to": "policy", "label": "follows", "from_card": "1", "to_card": "1"}, {"from": "policy", "to": "item", "label": "covers", "from_card": "0..*", "to_card": "0..*"}], "objects": [{"id": "client", "title": "client", "tone": 4, "attrs": ["O-01", "Admin: Company, in Settings", "name", "contract start date", "contract end date", "volume: 1"], "actions": ["-> edit company details (owner)"]}, {"id": "admin", "title": "admin user", "tone": 4, "attrs": ["O-02", "Admin: Admins, in Settings", "name", "work email", "role", "account owner", "status", "volume: 3", "→ see figure 2 of 2"], "actions": ["-> add (owner)", "-> remove (owner)", "-> change role (owner)", "-> make account owner (owner)"]}, {"id": "group", "title": "employee group", "tone": 4, "attrs": ["O-03", "Admin: Employee group, in Employees", "name", "volume: 14", "queue: No budget for next period"], "actions": ["-> create (HR)", "-> invite employees (HR) [only once the group's budgets for the current period are set]"]}, {"id": "employee", "title": "employee", "tone": 4, "attrs": ["O-05", "Admin: Employees", "name", "work email", "status", "volume: 1,200", "queue: Not joined", "→ see figure 2 of 2"], "actions": ["-> invite (HR) [only into a group whose budgets for the current period are set]", "-> resend invitation (HR)", "-> move to group (HR)", "-> mark as left (HR)"]}, {"id": "policy", "title": "policy", "tone": 4, "attrs": ["O-04", "Admin: Policy, in Policies", "open categories", "auto-approve limit", "covered items", "volume: 14", "→ see figure 2 of 2"], "actions": ["-> edit (HR)", "-> add covered items (HR)"]}, {"id": "item", "title": "catalogue item", "tone": 4, "attrs": ["O-13", "Admin: Covered items, in Policies", "ID", "name", "facet values", "volume: 12 in the sample"], "actions": ["-> view (HR, finance)"]}], "rows": [["client", "admin"], ["group", "employee"], ["policy", null], ["item", null]]}`

The replacement is also saved as /tmp/claude-0/-home-claude/e1d0222c-65c5-5625-aa10-282b96a89303/scratchpad/u9/f3-ia7-3/out/fix.json, with the rendered test file at /tmp/claude-0/-home-claude/e1d0222c-65c5-5625-aa10-282b96a89303/scratchpad/u9/f3-ia7-3/out/fix.md. Frame crops are in /tmp/claude-0/-home-claude/e1d0222c-65c5-5625-aa10-282b96a89303/scratchpad/u9/f3-ia7-3/out/crops/. I did not write the report to F/out/report.md: the tool refused report files from a subagent, so this reply is the report.

**Notes**
- **Renderer note: relationship IDs.** F3 asks for "a stable identifier on every element" (IA2, section 1.0), but no line carries its R- ID. The objects kind has no per-link id field, and putting an ID into the label would break "labels and counts kept" and IA2's verb-label rule. The R- IDs are reachable only through the caption and A.3.
- **Renderer note: phone 320 scroll end.** At full scroll (frame 4, 442 px) the right column is cut on its left with blank space to its right, so the scroll runs past the drawing's right edge. Every label is still whole in frame 3, so this is not a FIX.
- **Minor wording: model names.** A.5 says "each title is the model name in lower case". For admin user, employee group and catalogue item, the title is A.1's object name; the model name is `admin_user`, `employee_group`, `catalogue_item`. They differ only by the underscore, and model names are given in A.2.
- **Minor wording: "configure".** The caption calls these "the Admin objects HR and the account owner configure", but the catalogue item is changed by "Perqo content team (outside Admin)" (A.1). HR only views it and adds it to a policy.
- **Notation, minor: "assumed".** IA2 puts status words "in a note". The objects kind has no note field, so "assumed" for the volumes is carried only by the caption and A.1, not inside the boxes.

### IA7 figure 3, fourth check

IA7 "Level 3 · the backoffice", figure 3: fresh figure check (fourth since 9 Nov 2026)

The tool refused my write to F/out/report.md because subagents may not write report files, so this reply is the only copy of the report. Scratch files are in /tmp/claude-0/-home-claude/e1d0222c-65c5-5625-aa10-282b96a89303/scratchpad/u9/f4-ia7-3/out: the frame crops are in out/fr/, and out/current.md is the current declaration wrapped for render.py.

**Kind and section**
`objects`, in Deliverable A, A.5 "The map, drawn". Its placeholder is at line 358 of unit-text.md, after "The first figure holds the setup: client, admin users, employee groups, employees, policies and the catalogue items policies cover (R-01 to R-04, R-07, R-21)."

**Labels and numbers traced**

*Titles.* A.5 says "each title is the model name in lower case". The A.1 Object column gives:
- `client`: "O-01 | client (`client`)"
- `admin user`: "O-02 | admin user (`admin_user`)"
- `employee group`: "O-03 | employee group (`employee_group`)"
- `employee`: "O-05 | employee (`employee`)"
- `policy`: "O-04 | policy (`policy`)"
- `catalogue item`: "O-13 | catalogue item (`catalogue_item`)"

*client*
- `O-01` and `Admin: Company, in Settings`: A.1.
- `name`, `contract start date`, `contract end date`: A.2 "name → `name`; contract start date → `contract_start_date`; contract end date (IA8) → `contract_end_date` (proposed)".
- `volume: 1`: A.1 "| 1 |".
- `-> edit company details (owner)`: A.4 "client | -> edit company details | account owner *new*", and A.1 "owner (account owner)".

*admin user*
- `O-02` and `Admin: Admins, in Settings`: A.1.
- `name`, `work email`, `role`, `account owner`, `status`: A.2 "name → `name`; work email → `work_email`; role … → `role`; account owner *new* → `is_account_owner`; status *new* → `status`".
- `volume: 3`: A.1 "3 *new*"; section 2.2 "with three admin users".
- `→ see figure 2 of 2`: line 360 says figure 2 holds "the admin user who decides a claim".
- `-> add (owner)`: A.4 "admin user | -> add | account owner".
- `-> remove (owner)`, `-> change role (owner)`, `-> make account owner (owner)`: A.4 "-> remove *new*; -> change role *new*; -> make account owner *new* | account owner".

*employee group*
- `O-03` and `Admin: Employee group, in Employees`: A.1.
- `name`: A.2 "O-03 employee group | name → `name`".
- `volume: 14`: A.1 "14 *new*"; section 2.2 "1,200 employees in 14 employee groups".
- `queue: No budget for next period`: A.1 Work queue column; C.4 row "No budget for next period | employee group".
- `-> create (HR)` and `-> invite employees (HR) [only once the group's budgets for the current period are set]`: A.4 "employee group | -> create; -> invite employees (only once the group's budgets for the current period are set; IA8, section 3.2) | HR manager".

*employee*
- `O-05` and `Admin: Employees`: A.1 "| Employees |".
- `name`, `work email`, `status`: A.2.
- `volume: 1,200`: A.1 "1,200 *new*".
- `queue: Not joined`: A.1; C.4.
- `→ see figure 2 of 2`: line 360 says figure 2 holds "the employee's card, claims and allocations".
- `-> invite (HR) [only into a group whose budgets for the current period are set]` and `-> move to group (HR)`: A.4 "employee | -> invite (only into a group whose budgets for the current period are set; IA8, section 3.2); -> move to group | HR manager".
- `-> resend invitation (HR)` and `-> mark as left (HR)`: A.4 "employee | -> resend invitation *new*; -> mark as left *new* | HR manager".

*policy*
- `O-04` and `Admin: Policy, in Policies`: A.1.
- `open categories`, `auto-approve limit`, `covered items`: A.2.
- `volume: 14`: A.1 "14, one per group (R-03)".
- `→ see figure 2 of 2`: line 360 says figure 2 holds "the policy a claim is checked against".
- `-> edit (HR)` and `-> add covered items (HR)`: A.4 "policy | -> edit; -> add covered items | HR manager".

*catalogue item*
- `O-13` and `Admin: Covered items, in Policies`: A.1.
- `ID`, `name`, `facet values`: A.2 "ID → `id`; name → `name`; the four facet values → `facets`".
- `volume: 12 in the sample`: A.1 "12 in the sample (IA4)".
- `-> view (HR, finance)`: A.4 "catalogue item | -> view *new* in Admin | HR manager, finance manager".

*Links (A.3)*
- client `has` admin user, `1`, `1..*`: "R-01 | client | has | admin user | 1, 1..*"
- client `has` employee group, `1`, `1..*`: "R-02 | client | has | employee group | 1, 1..*"
- admin user `is also` employee, `0..1`, `0..1`: "R-21 *new* | admin user | is also | employee | 0..1, 0..1"
- employee group `contains` employee, `1`, `1..*`: "R-04 | … | contains | employee | 1, 1..*"
- employee group `follows` policy, `1`, `1`: "R-03 | employee group | follows | policy | 1, 1"
- policy `covers` catalogue item, `0..*`, `0..*`: "R-07 | policy | covers | catalogue item | 0..*, 0..*"

All six relationships A.5 assigns to this figure (R-01 to R-04, R-07, R-21) are drawn, and no others. The three "→ see figure 2 of 2" lines match line 360's list of what figure 2 holds. Client, employee group and catalogue item rightly carry none. No label, date or number is untraced.

**Caption**
The caption:
- names the artefact (object-relationship map, figure 1 of 2), what it shows, the fidelity (F3), the decision it supports ("what Admin holds and who changes it") and the section (Deliverable A);
- states the tone and the reading rule;
- names a source for each element, and each checks against the text:
  - IA4, Deliverable A for the objects, IDs, labels, attributes, calls to action and R-01 to R-04, R-07;
  - IA4, as A.1 gives it, for the catalogue items' volume;
  - sections 2.2 and 3.4 for R-21, the account owner, the two statuses and the other volumes;
  - section 4.4 for resend invitation;
  - section 4.2 and C.4 for the queues;
  - IA8, as A.2 and its note of 9 November 2026 give it (DL-005, DL-006), for contract end date;
  - IA8, as A.4 gives it (DL-007, C.4), for the invite condition;
  - Prater 2015 and 2016;
- ends "Perqo is fictional".

Complete.

**Kind**
Things and relationships, so `objects`, the kind the method names. It fits.

**Frames**
- **Desktop (728 px column) and tablet, dark and light.** One frame each; the whole figure fits. Every box, label, count and wrapped bracketed condition is legible, with no overlap or clipping. The level lines (has, contains) read left to right; the vertical lines (has, is also, follows, covers) read top to bottom.
- **Phone 390, dark and light.** Three frames (scrolled to 78, 242 and 372 of 372).
  - Frame 1 shows the left column whole: client, employee group, policy and catalogue item, with has, follows and covers and their counts.
  - Frame 2 shows the has and contains labels on the level lines, with both counts whole.
  - Frame 3 shows admin user and employee whole, with is also and both 0..1 counts.
  - Every label is whole in at least one frame. The edge fade only softens text while it is mid-scroll.
- **Phone 320, 360 and 430, dark and light.** Four, four and three frames. The same holds; the right column is whole in frame 3 at each width.
- **Tones.** Only tone 4 is drawn, on every box. Its meaning is stated at line 356, "Every box is tone 4, Perqo Admin, because the map shows one surface", and at line 14, "Admin's boxes take tone 4, Perqo Admin". No tone 6 is drawn.

**Notation (IA2, section 5 and the notation sheet)**
The figure conforms:
- boxes have filled title bands, attributes below the title and "-> verb" actions after the rule line;
- lines have no heads, each with a verb and a UML count at each end;
- every label reads left to right on a level line and top to bottom otherwise, so no triangle is needed;
- conditions are in square brackets, and continuations are written "→ see";
- with one surface, every box takes its tone;
- titles are model names in lower case, each with an "Admin: Label" line;
- nothing is dashed.

The current declaration renders with render.py without error ("figure 1: objects ok").

IA7 "Level 3 · the backoffice" figure 3: PASS

**Notes**
- **Renderer note.** At 320 and 360 px the sideways scroll runs about 70 px past the drawing's right edge. The last frame therefore clips the left side of the admin user and employee boxes, with empty space to their right. Every label is whole in the frame before, so the reader loses nothing. The cause is the renderer's centring in the 700-unit width (P50), not the declaration.
- **Capture note.** The opening-frame files (not the frame sheets) at desktop, tablet and phone widths show the page's sticky header bar painted across the middle of the figure. The frame sheets do not show it. This comes from the verify script's full-element capture, not from what a reader sees.
- **Minor: no relationship IDs on the lines.** The relationship lines carry no R-IDs, while IA2, section 1.0 says that at F3 "every element has a stable identifier". The unit chose this in A.5 ("every relationship, drawn or not, is in A.3"), the caption names R-01 to R-04, R-07 and R-21, and each line is unique by its verb and its two ends. Not a FIX.
- **Minor: model names written in words.** Titles write model names with spaces (`admin user`, not `admin_user`). IA2's own examples write model names in words too ("transaction, type claim"). Not a FIX.

### IA7 figure 4, first check

IA7 "Level 3 · the backoffice", figure 4: fresh check (P31, isolated context). I edited nothing outside F/out.

**Figure 4: kind and section.** The kind is `objects`, an object-relationship map. It sits in Deliverable A, A.5 "The map, drawn", as figure 2 of 2. A.5 says what it holds: "money, decisions and the record of them: the employee's card, claims and allocations, card payments, the admin user who decides a claim, the policy a claim is checked against, and the audit entry (R-05, R-08 to R-13, R-22 to R-24). R-06 and R-23's other objects are in A.3 only."

**Labels and numbers, each traced to the unit's text**

Continuation stubs:
- `employee` `O-05`, `policy` `O-04` and `admin user` `O-02` match A.1.
- `→ see figure 1 of 2` matches A.5: 'with "→ see" lines where an object continues in the other'. It also matches figure 3's caption, "figure 1 of 2". The renamed continuation lines are correct.

`card`:
- `O-09` and `Admin: Perqo card, status only` match A.1: "Perqo card, on the employee's record *new*: status only".
- `status` matches A.2: "status → `status` (`active`, `frozen`, `cancelled`)". The box names the attribute, not its values, so the new Cancelled needs no change here.
- `volume: up to 1,200` matches A.1: "up to 1,200".
- `-> view status (HR)` matches A.4: "card | -> view status *new* | HR manager".

`transaction, type claim`:
- `O-07` and `Admin: Claim` match A.1.
- amount, category, receipt, status, date submitted, rejection reason, decided by and rejection note match A.2's O-07 row. All eight are there.
- `volume: 1,200 a month` is from A.1, "about 1,200 a month, about 180 waiting", and section 2.2, "about 1,200 claims a month". The figure drops "about" and leaves out "about 180 waiting".
- `queue: Approvals` matches A.1.
- `-> approve (HR)`, `-> reject (HR)` and `-> approve selected (HR)` come from A.4: "HR manager, never on their own claim". The condition is dropped.
- `-> view (HR, finance)` matches A.4: "HR manager, finance manager".

`allocation`:
- `O-06` and `Admin: Budget` match A.1: "Budget, in Budgets".
- category, period, amount, spent and remaining match A.2.
- A.2's row also has "closed (IA8) → `closed` (proposed), set when the employee is Left", with the note "Note, 9 November 2026: three fields added … the allocation's `closed`". **closed is missing from the box.** It is the only attribute that A.2 lists and does not mark "not shown in Admin" yet the figure leaves out. Every other box carries all of its A.2 attributes, and figure 3's caption shows that figure 3 took in its own 9 November field (contract end date).
- `volume: up to 4,800 a period` matches A.1.
- `-> set for a group (finance)` matches A.4.

`transaction, type card payment`:
- `O-08` and `Admin: Card payment, in Reports` match A.1.
- amount, date, merchant and category match A.2.
- `volume: 9,600 a month` is from A.1, "about 9,600 a month". "about" is dropped.
- `-> view in a report (finance)` matches A.4.

`audit entry`:
- `O-17` and `Admin: History; Activity log` match A.1: "History, on each detail page; Activity log, in Settings".
- who, action, object and its ID, date and time, and before and after match A.2.
- **There is no volume**, though A.1 gives "one per change" and A.5 says "Each box carries its ID, its volume and its work queue".
- `-> view (as the record; owner for the log)` comes from A.4, "any role that may see the record; account owner for the Activity log", and A.1, "History: any role that sees the record; Activity log: owner". "As the record" is not the text's wording and does not say what it means.

Links (all against A.3):
- holds 1, 0..1 (R-11); submits 1, 0..* (R-08); holds 1, 1..* (R-05); spends from 0..*, 1 (R-10); spends from 0..*, 1 with dir to (R-13); is used for 1, 0..* (R-12); is checked against 0..*, 1 (R-09).
- is decided by 0..*, 0..1 matches R-22: "(0..* to 0..1; none when the rule decides)".
- records a change to 0..*, 1 with dir to matches R-23. It is drawn to the claim only, as A.5 says.
- is made by 0..*, 0..1 matches R-24.
- Every verb and count matches.

**The caption** names the artefact and says what it shows. It names the decision it supports and the section (Deliverable A), gives its sources, and says "Perqo is fictional". It does not credit the source of `closed` once that is added (IA8 / DL-005, DL-006). It says "calls to action with their roles and counts" but carries no conditions. Both are updated in the replacement.

**The kind.** Things and relationships call for `objects`, so the kind fits.

**What the frames show**
- **Desktop 1280 px, dark and light:** one frame, the whole figure fits. Every label is legible and nothing is clipped or overlapping. The triangles on "spends from" (pointing to allocation) and "records a change to" (pointing up to the claim) point the right way, and the counts sit clear of each other.
- **Phone 390 px, dark and light:** four frames, scrolled 0, 164, 328 and 372 of 372 px, opening at 0. Each box, label and count appears whole in at least one frame: "is decided by" in frame 2; "is used for", the second "spends from" and "is made by" in frames 3 and 4. Only the scroll fade softens the edges. Nothing overlaps.
- **Tablet, dark and light:** one frame, clean.
- **Phone 320:** I looked at the opening frame only. It is consistent with the others.
- **Tones:** every box is tone 4. Line 14 says "Admin's boxes take tone 4, Perqo Admin; on a figure of one surface every box takes that surface's tone", and A.5 says "Every box is tone 4, Perqo Admin, because the map shows one surface". Tone 6 is not drawn.

**The notation (IA2, 5.2)**
- Titles are model names in lower case, each with a "Surface: Label" line. Actions are written "-> verb". Counts use UML multiplicities. There are no dashed lines. Triangles appear only on labels that read right to left or bottom to top. Continuations use "→ see".
- It fails on one point. IA2 says "A condition is written in square brackets" and that F3 means "every condition and state is shown", yet the claim actions leave out the A.4 condition "never on their own claim".

IA7 "Level 3 · the backoffice" figure 4: FIX

Replacement: the whole declaration. I rendered it with render.py with no error ("figure 1: objects ok, 1 figures, 0 errors") and screenshotted it at 1280 and 390 px in dark and light. The layout and lines are unchanged and nothing is clipped or overlapping.

`{"kind": "objects", "caption": "Object-relationship map, figure 2 of 2, money, decisions and the audit trail: the Admin objects money moves through, who decides a claim and what records each change, with IDs, Admin labels, attributes, volumes for the sizing client (assumed), work queues, calls to action with their roles and conditions, and counts in UML multiplicity notation, F3 (model names in A.2); supports the decision on what Admin shows about spending and who answers for each decision (Deliverable A). Every box tone 4, Perqo Admin. Lines read left to right on a level line, top to bottom otherwise; a triangle by a label marks a label that reads right to left or bottom to top. R-05, R-08 to R-13 from IA4, Deliverable A, labels and counts kept; rejection reason from IA6, Deliverable B; R-22 to R-24, the audit entry (O-17), decided by, rejection note, the volumes and the Perqo card label set in sections 2.2, 2.3 and 5.3; the allocation's closed from IA8, sections 3.2 and 3.4, as A.2 and its note of 9 November 2026 give it (DL-005 and DL-006); the condition on deciding a claim from section 3.3, as A.4 gives it. Perqo is fictional.", "objects": [{"id": "employee", "title": "employee", "tone": 4, "attrs": ["O-05", "→ see figure 1 of 2"]}, {"id": "card", "title": "card", "tone": 4, "attrs": ["O-09", "Admin: Perqo card, status only", "status", "volume: up to 1,200"], "actions": ["-> view status (HR)"]}, {"id": "policy", "title": "policy", "tone": 4, "attrs": ["O-04", "→ see figure 1 of 2"]}, {"id": "claim", "title": "transaction, type claim", "tone": 4, "attrs": ["O-07", "Admin: Claim", "amount", "category", "receipt", "status", "date submitted", "rejection reason", "decided by", "rejection note", "volume: about 1,200 a month, about 180 waiting", "queue: Approvals"], "actions": ["-> approve (HR) [never on their own claim]", "-> reject (HR) [never on their own claim]", "-> approve selected (HR) [never on their own claim]", "-> view (HR, finance)"]}, {"id": "alloc", "title": "allocation", "tone": 4, "attrs": ["O-06", "Admin: Budget", "category", "period", "amount", "spent", "remaining", "closed", "volume: up to 4,800 a period"], "actions": ["-> set for a group (finance)"]}, {"id": "payment", "title": "transaction, type card payment", "tone": 4, "attrs": ["O-08", "Admin: Card payment, in Reports", "amount", "date", "merchant", "category", "volume: about 9,600 a month"], "actions": ["-> view in a report (finance)"]}, {"id": "audit", "title": "audit entry", "tone": 4, "attrs": ["O-17", "Admin: History; Activity log", "who", "action", "object and its ID", "date and time", "before and after", "volume: one per change"], "actions": ["-> view (History: any role that sees the record; Activity log: owner)"]}, {"id": "admin", "title": "admin user", "tone": 4, "attrs": ["O-02", "→ see figure 1 of 2"]}], "rows": [["employee", "card", null], ["claim", "alloc", "payment"], ["policy", "audit", "admin"]], "links": [{"from": "employee", "to": "card", "label": "holds", "from_card": "1", "to_card": "0..1"}, {"from": "employee", "to": "claim", "label": "submits", "from_card": "1", "to_card": "0..*"}, {"from": "employee", "to": "alloc", "label": "holds", "from_card": "1", "to_card": "1..*"}, {"from": "claim", "to": "alloc", "label": "spends from", "from_card": "0..*", "to_card": "1"}, {"from": "payment", "to": "alloc", "label": "spends from", "from_card": "0..*", "to_card": "1", "dir": "to"}, {"from": "card", "to": "payment", "label": "is used for", "from_card": "1", "to_card": "0..*"}, {"from": "claim", "to": "policy", "label": "is checked against", "from_card": "0..*", "to_card": "1"}, {"from": "claim", "to": "admin", "label": "is decided by", "from_card": "0..*", "to_card": "0..1"}, {"from": "audit", "to": "claim", "label": "records a change to", "from_card": "0..*", "to_card": "1", "dir": "to"}, {"from": "audit", "to": "admin", "label": "is made by", "from_card": "0..*", "to_card": "0..1"}]}`

What the replacement changes:
- Adds `closed` to the allocation box.
- Writes `[never on their own claim]` on the three decision actions.
- Adds `volume: one per change` to the audit entry box.
- Restores "about" on the claim and card-payment volumes, and adds "about 180 waiting" (A.1).
- Rewrites the audit entry's action to A.1's wording.
- Updates the caption as described above.

The links, rows and tones are unchanged.

Notes
- Relationship IDs (R-xx) are not on the lines. The caption and A.3 carry them. F3's "stable identifier on every element" would want them on the lines, but the `objects` kind has no link ID field. This is a renderer note, not a FIX.
- The volumes are not marked "assumed" in the boxes, only in the caption. IA2 puts status words in a note, and the `objects` kind has no note field, so the caption is the only place it can go.
- `Admin: Perqo card, status only` and `Admin: Card payment, in Reports` put a qualifier or a place on the "Surface: Label" line, which should give only the label. The wording is minor and the text supports it.
- The three repeated `[never on their own claim]` lines could be shortened if the unit prefers, but each condition belongs on its own action.
- The opening-frame screenshots on desktop and phone show the page's sticky header over the top of the figure. That is page chrome in the capture, not the figure, and the frame sheets are clean.

Files are in /tmp/claude-0/-home-claude/e1d0222c-65c5-5625-aa10-282b96a89303/scratchpad/u9/f2-ia7-4/out:
- report.md
- fig4-replacement.json
- fig4-replacement.md
- fig4-dark-1280.png
- fig4-light-1280.png
- fig4-dark-390.png
- fig4-light-390.png

### IA7 figure 4, second check

## Verdict
IA7 "Level 3 · the backoffice" figure 4: PASS

Every label and count traces to the unit, the caption and the kind pass, the frames are clean at every width and theme, and it is drawn in IA2's notation. Three notes follow at the end; none is a fix. The report could not be written to F/out/report.md because the harness blocked the report file, so it is here in full.

## Kind and section
Kind `objects`. It sits in Deliverable A, A.5 "The map, drawn", the second of the two figures: "The second holds money, decisions and the record of them: the employee's card, claims and allocations, card payments, the admin user who decides a claim, the policy a claim is checked against, and the audit entry (R-05, R-08 to R-13, R-22 to R-24)."

## Labels, dates and numbers traced
The figure has no dates. Every box is `tone 4`.

**employee**
- `employee` and `O-05` come from A.1: "O-05 | employee (`employee`)".
- `→ see figure 1 of 2` comes from A.5: "with "→ see" lines where an object continues in the other ... The first figure holds the setup: ... employees, policies".

**card**
- `card` and `O-09` come from A.1: "O-09 | card (`card`)".
- `Admin: Perqo card, status only` comes from A.1: "Perqo card, on the employee's record *new*: status only", and section 2.3: "Card (O-09): shown, as "Perqo card", status only".
- `status` comes from A.2: "O-09 card | status → `status`". The last four digits are rightly left out (A.2: "not shown in Admin").
- `volume: up to 1,200` comes from A.1: "up to 1,200".
- `-> view status (HR)` comes from A.4: "card | -> view status *new* | HR manager".

**claim**
- `transaction, type claim` and `O-07` come from A.1: "O-07 | transaction, type claim".
- `Admin: Claim` comes from A.1: "Claim, on the employee's record; listed in Approvals".
- The eight attributes are `amount`, `category`, `receipt`, `status`, `date submitted`, `rejection reason`, `decided by` and `rejection note`. They are A.2's O-07 row, in the same order: "amount → ...; category → ...; receipt → ...; status → ...; date submitted → ...; rejection reason (IA6) → ...; decided by *new* → ...; rejection note *new* → ...".
- `volume: about 1,200 a month, about 180 waiting` comes from A.1: "about 1,200 a month, about 180 waiting".
- `queue: Approvals` comes from A.1's work queue column: "Approvals".
- The three decision actions are `-> approve (HR) [never on their own claim]`, `-> reject (HR) [never on their own claim]` and `-> approve selected (HR) [never on their own claim]`. They come from A.4: "-> approve; -> reject | HR manager, never on their own claim" and "-> approve selected *new* | HR manager, never on their own claim".
- `-> view (HR, finance)` comes from A.4: "-> view *new* in Admin | HR manager, finance manager".

**allocation**
- `allocation` and `O-06` come from A.1.
- `Admin: Budget` comes from A.1: "Budget, in Budgets".
- `category`, `period`, `amount`, `spent`, `remaining` and `closed` are A.2's O-06 row. A.2 gives the last as "closed (IA8) → `closed` (proposed)".
- `volume: up to 4,800 a period` comes from A.1: "up to 4,800 a period".
- `-> set for a group (finance)` comes from A.4: "allocation | -> set for a group | finance manager".

**card payment**
- `transaction, type card payment` and `O-08` come from A.1.
- `Admin: Card payment, in Reports` comes from A.1: "Card payment, in Reports".
- `amount`, `date`, `merchant` and `category` are A.2's O-08 row.
- `volume: about 9,600 a month` comes from A.1: "about 9,600 a month".
- `-> view in a report (finance)` comes from A.4: "-> view in a report | finance manager".

**audit entry**
- `audit entry` and `O-17` come from A.1: "O-17 | audit entry (`audit_entry`)".
- `Admin: History; Activity log` comes from A.1: "History, on each detail page; Activity log, in Settings".
- `who`, `action`, `object and its ID`, `date and time` and `before and after` are A.2's O-17 row.
- `volume: one per change` comes from A.1: "one per change".
- `-> view (History: any role that sees the record; Activity log: owner)` is in A.1's words: "History: any role that sees the record; Activity log: owner". A.4 gives the same: "-> view | any role that may see the record; account owner for the Activity log".

**admin user and policy**
- `admin user` and `O-02`, and `policy` and `O-04`, come from A.1.
- Both carry `→ see figure 1 of 2`, from A.5.

**Links**, each checked against A.3 (label, then counts from end and to end):

| Figure | A.3 |
|---|---|
| `holds` 1 / 0..1 | R-11: "holds \| card \| 1, 0..1" |
| `submits` 1 / 0..* | R-08: "1, 0..*" |
| `holds` 1 / 1..* | R-05: "1, 1..*" |
| `spends from` 0..* / 1, claim to allocation | R-10: "0..*, 1" |
| `spends from` 0..* / 1, card payment to allocation, `dir: to` | R-13: "0..*, 1" |
| `is used for` 1 / 0..* | R-12: "1, 0..*" |
| `is checked against` 0..* / 1 | R-09: "0..*, 1" |
| `is decided by` 0..* / 0..1 | R-22: "0..*, 0..1" |
| `records a change to` 0..* / 1, audit entry to claim, `dir: to` | R-23: "0..*, 1" |
| `is made by` 0..* / 0..1 | R-24: "0..*, 0..1" |

Every relationship A.5 names for this figure is drawn. Nothing is drawn that A.5 keeps out ("R-06 and R-23's other objects are in A.3 only").

All five fixes from the first check are in place:
- the allocation's `closed`;
- `[never on their own claim]` on all three decision actions;
- `volume: one per change` on the audit entry;
- "about" on the claim and card payment volumes;
- the audit entry's view action in A.1's words.

The continuation lines read `→ see figure 1 of 2`. Errors: none.

## Caption
`Object-relationship map, figure 2 of 2, money, decisions and the audit trail: ... Perqo is fictional.`

The caption:
- names the artefact and says what the figure shows;
- gives the fidelity, F3;
- names the decision it supports;
- names the section, Deliverable A;
- names the sources: IA4, Deliverable A; IA6, Deliverable B; sections 2.2, 2.3, 3.3 and 5.3; IA8 through A.2 and its note of 9 November 2026 (DL-005, DL-006); A.4;
- says Perqo is fictional.

Its tone statement and its triangle reading rule match the figure. The caption passes.

## Kind
Things and relationships call for `objects`, so the kind fits.

## The figure as the reader sees it
**Desktop, 1280 px, dark and light.** One frame; the whole figure fits.
- Every label is legible. Nothing is clipped. No label, count or plate overlaps another or a box.
- Both triangles are clear. The one by "spends from" points left at the allocation. The one by "records a change to" sits on its line and points at the claim.
- In the opening screenshot the page's sticky header and section bar cover part of the figure. That is page chrome at that scroll position, not the figure; the frame sheet is clean.

**Tablet, dark and light.** One frame, clean.

**Phone, 390 px, dark and light.** Four frames, at 0, 164, 328 and 372 of 372 px; the figure opens at 0.
- Every box is whole in at least one frame: employee, claim and policy in frame 1; card, allocation and audit entry in frame 2; card payment and admin user in frame 4.
- Every link label, count and triangle is legible in some frame.
- The edge fades are the scroll cue; whatever they cover is whole in another frame.
- "scroll sideways for the whole figure" is shown. Nothing overlaps.

**Phones at 320, 360 and 430 px (dark sheets).** Five, four and three frames, with the same result.

**Tones.** Only tone 4 is drawn. The text gives its meaning twice:
- A.5: "Every box is tone 4, Perqo Admin, because the map shows one surface".
- The introduction: "Admin's boxes take tone 4, Perqo Admin; on a figure of one surface every box takes that surface's tone (IA2, section 5.2)".

No tone 6 is drawn. The figure is not a matrix, so the matrix tests do not apply.

## Notation (IA2, section 5 and the notation sheet)
- Titles are data-model names in lower case, each with an "Admin: Label" line.
- Attributes sit above the rule line and `-> verb` actions below it.
- Conditions are in square brackets, and counts use UML multiplicity.
- Lines are plain, with no heads and no dashes.
- Labels read left to right on a level line and top to bottom otherwise. The two that cannot each carry a triangle pointing at the object they read towards: "spends from" (card payment to allocation, right to left) and "records a change to" (audit entry to claim, bottom to top).
- Continuations use the sheet's "→ see *name*" form.

The current declaration renders with `render.py` without error ("figure 1: objects ok").

## Notes
1. **Two sources the caption does not name.**
   - The work queue `queue: Approvals` is IA1's, through section 4.2 ("Approvals is IA1's").
   - Three of the calls to action are this unit's additions: `-> approve selected` (section 4.4), the claim's `-> view` (A.4, *new*) and `-> view status` (section 2.3).

   Figure 3's caption does name its queues' source. All of these are in Deliverable A, which this caption names, so it is minor wording, not a fix. If wanted, add "the work queue from section 4.2; approve selected from section 4.4" after "set in sections 2.2, 2.3 and 5.3".
2. **The "Admin:" lines are inconsistent.** `Admin: Card payment, in Reports` keeps A.1's place, while `Admin: Claim`, `Admin: Budget` and `Admin: History; Activity log` drop it. `Admin: Perqo card, status only` puts a scope qualifier in the label line. All are A.1's words, so this is minor.
3. **The continuation boxes carry less than A.5 says each box carries.** A.5 says "Each box carries its ID, its volume and its work queue". The employee, policy and admin user boxes carry only their ID and `→ see figure 1 of 2`, which the continuation note covers. Only the claim has a work queue in A.1, and the figure shows it.

Files are in /tmp/claude-0/-home-claude/e1d0222c-65c5-5625-aa10-282b96a89303/scratchpad/u9/f3-ia7-4/out:
- current.md (the current declaration, rendered)
- ph-dark-0.png to ph-dark-5.png
- ph-light-0.png to ph-light-5.png
- ph-light-rest.png
- tab-dark.png
- tab-light.png
- phone320-dark-sheet.png
- phone360-dark-sheet.png
- phone430-dark-sheet.png
