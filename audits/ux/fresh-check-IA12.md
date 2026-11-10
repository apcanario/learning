---
audit: fresh check
unit: IA12 · When the inputs are missing: building the backbone anyway
course: ux · IA · Information Architecture
model: Fable 5.2 (claude-fable-5-2, confirmed from the agent's transcript; live search). The session's "fable" model is Fable 5.2, not the Fable 5.1 method §4 names, so by the rule as written a Fable 5.1 fresh check of IA12 is owed to the Fable stage (P49)
date: 2026-11-10
chat: own Fable 5.2 agent context, not shown the writing (P31), launched by the U-12 chat (Opus 5.5 as the orchestrating chat; the writer ran on Opus 5.5) in session https://claude.ai/code/session_01KMmgQxTw6Ud6wu4ARE1zh3
verdict: fix · 3 error, 8 should-fix, 13 minor
---

The checker's final report, verbatim: its hand-back message, extracted by script from its transcript (the `SubagentHandback` call). Its own `out/report.md` holds only an early header (777 characters), so the hand-back is the record. It checked an exact copy of the unit as filed at commit 207db6c (sha256 d45a2878d61461f92e3bee06198a3c3b6529e7b55bdd049ce5e85bfcacff67e6, two copies, confirmed by the checker). Transcript checks (U-12 chat): no tool named `mcp__*`, Projects, Artifact, connector or Agent; every one of its ten WebFetch URLs was returned verbatim by an earlier WebSearch in its transcript; no redirect followed; no fetch refused; one URL (nngroup.com, stakeholder analysis) was fetched a second time after a successful fetch, recorded, not a breach (U-10's reading); every path inside its folder.

# Fresh check · IA12 · When the inputs are missing: building the backbone anyway

**Model.** Fable 5.2 (claude-fable-5-2). I am not Fable 5.1: a Fable 5.1 fresh check of IA12 is still owed.

**Hash.** `sha256sum` gives d45a2878d61461f92e3bee06198a3c3b6529e7b55bdd049ce5e85bfcacff67e6 for both `unit/IA12.md` and `unit/IA12-readonly-copy.md`, matching `unit/sha256.txt`. Neither copy was edited (re-hashed at the end).

**Context note.** My context held a memory listing and the Project's instructions. I saw them and used neither as a source. No memory, Projects, past-chat, connector, Artifact or Agent tool was called.

**How checked.** Read: sourcing-standard Parts 1 and 4, the brief (PRE, goal, AIMS, IA12's entry), figure-kinds.md, IA7 in full, and the cited sections of IA1 to IA6 and IA8 to IA11. Every Current below was run through `grep -F -c` on `unit/IA12.md`: each occurs exactly once. Counts were re-run by script in `out/` (`count.py`, `figs.py`, `ids.py`). The report file `out/report.md` holds only the header; this reply is the record.

**(6) Errata.** `audits/ux/` holds no audit report, so there are no errata to check. Pointers to filed units were checked instead (see Confirmed).

## Findings

1. [error] [figure] section 3.4; Current: `Table A.2 of IA11 also sends to the register eleven rows that do not concern Admin`; Problem: the sentence then lists rows 15 and 16, 17 to 19 and 21, and 22 to 24, which is nine rows. IA11 A.2 sends 23 rows to the register (all but 10 and 11); 14 concern Admin, 9 do not. Deliverable B's own text ("rows 15 to 19 and 21 to 24") also gives nine; Fix: `Table A.2 of IA11 also sends to the register nine rows that do not concern Admin`; Basis: IA11, Deliverable A, A.2, rows 1 to 25 (filed unit).

2. [error] [accuracy] Deliverable D, D.2, DL-017, "Raised by, from"; Current: `the assumptions of IA5 to IA11 sit in nine "What later units take" tables, and IA11 had to gather 25 of them into one table (IA11, A.2)`; Problem: the filed units hold five assumption tables, one each in IA6 to IA10. IA6's sits under "What IA8 and IA11 take"; IA5 has one assumption in prose (section 5.5); IA11 has none. A.2 gathers IA7 to IA10's rows only; Fix: `the assumptions of IA6 to IA10 sit in five closing tables, one per unit, and IA11 had to gather the 25 rows of IA7 to IA10's that name a test for it into one table (IA11, A.2)`; Basis: IA6 to IA10, closing tables; IA11, A.2's opening sentence.

3. [error] [figure] Deliverable A, A.2 (decision tree); Current: `"Is there a record of use: a log, tickets, paths?". The outcomes:`; Problem: the figure's branch labels "yes" and "no", and which answer leads to which outcome, are nowhere in the unit's text ("yes" occurs 0 times outside the viz block). No fact is wrong; the figure rule makes an untraced label an error; Fix: `"Is there a record of use: a log, tickets, paths?". Each question has two answers, yes and no: a no to any of the first three ends at that shortage's move and a yes goes on to the next question; at the fourth, yes ends at the test and no goes on to the fifth, where yes ends at the review and no at C0. The outcomes:`; Basis: the unit's own viz block, branch by branch.

4. [should-fix] [accuracy] section 2; Current: `IA11 then put a ceiling on it: with no user reachable, the ladder leaves C0 and C1 (IA11, section 7).`; Problem: the same section's table, section 3.3 and AR-02 and AR-37 then say records can reach C5, so the unit contradicts its own ceiling. IA11 itself allows C5 for a read of the behaviour itself; Fix: `IA11 then put a ceiling on it: with no user reachable, the ladder leaves C0 and C1 for any question about what people understand or where they look (IA11, section 7); the one exception is IA11's own, a record that measures in use the behaviour the assumption is about, which stands at C5 (IA11, section 6.4, and Deliverable D, SG-A).`; Basis: IA11, section 7; section 6.4, C5; SG-A.

5. [should-fix] [deliverable] Deliverable C, C.1; Current: `Leadership's placement is IA10's; engineering's and sales' quadrants are those IA10 read from IA9's tables (IA10, section 5).`; Problem: the placements do not follow from section 4.1's rule. Sales (F1 story, F2 rules) is at interest 7 and clients (F1 words, F2 roles) at 4; customer success (F2) is at 8, above product management (F2) at 7; Fix: `Leadership's placement is IA10's; engineering's and sales' quadrants are those IA10 read from IA9's tables (IA10, section 5). The rule orders the functions and does not give the number: where two functions read the same fidelities, the one that reads more of the IA, more often, is placed higher. Sales reads BR-3 and the demo path monthly (7); clients read a word list and the role matrix in a session held only in a cycle touching Admin (4); customer success reads the role matrix and both decision tables for every client it configures (8).`; Basis: IA10, A.1, rows TP-06, TP-07, TP-09 (fidelity and cadence columns).

6. [should-fix] [deliverable] Deliverable C, C.1 and C.2; Current: `| TP-10 | Legal | 7 | 6 |`; Problem: section 4.1 ranks "sits in the IA review" above "is consulted before a decision", yet legal (consulted, and only under DL-014, proposed) has power 7, above support (sits in the review) at 6; Fix: `| TP-10 | Legal | 6 | 6 |`, and in the scatter, Current: `{"label": "Legal", "x": 6, "y": 7, "tone": 5},` Fix: `{"label": "Legal", "x": 6, "y": 6, "tone": 5},`. The quadrant and the 6/2/3/1 counts do not change, and no point collides (Security is at 7, 6); Basis: the unit's section 4.1 rule; IA9, section 4.1 (the IA review's members); IA10, A.4, DL-014.

7. [should-fix] [deliverable] Deliverable D, D.5; Current: `F1 at the start of a cycle; F2 once each function is interviewed`; Problem: Deliverable C's face says the map is at F2 with every placement assumed until each function is interviewed, and none has been. By this cell the map would be F1; Fix: `F1 at the start of a cycle; F2 once every function is placed with its reason, each placement marked assumed until the function is interviewed`; Basis: Deliverable C's face; IA2, section 1.0 (F2 complete for its scope).

8. [should-fix] [deliverable] Deliverable D, D.2 to D.4; Current: `| Told | product management, engineering, support, content team, at FO-01 |`; Problem: the template's field "Supersedes, superseded by" is missing from all three filled entries; Fix: `| Told | product management, engineering, support, content team, at FO-01 |` followed by a new row `| Supersedes, superseded by | none |`. Same new row after Current: `| Told | sales at FO-04 (BR-3 keeps "not yet decided"); customer success at FO-05; clients in the release note, FO-02; leadership at FO-09 |` and after Current: `| Told | product management at FO-01; leadership at FO-09 |`; Basis: the unit's D.1; IA9, D.3.

9. [should-fix] [coverage] Deliverable B, "How the rows were counted"; Current: `and of section 6.3's four practices, three are process, which IA9's change control holds, and the fourth, permissions written once, is counted (AR-17).`; Problem: two IA7 decisions that could be reversed on their own have no row: after Approve or Reject the next waiting claim opens (IA7, section 4.3), and catalogue item -> view for HR and finance managers (IA7, A.4, marked new); Fix: `and of section 6.3's four practices, three are process, which IA9's change control holds, and the fourth, permissions written once, is counted (AR-17). Two smaller decisions of IA7 are carried inside rows and not counted on their own: after Approve or Reject the next waiting claim opens (section 4.3), with AR-29, and HR and finance managers view catalogue items under a policy's Covered items (A.4, catalogue item -> view), with AR-20.` The alternative is two new rows, which changes 42, 49, 16 and the owner counts; Basis: IA7, section 4.3 (wireflow text) and A.4.

10. [should-fix] [coverage] section 4.3; Current: `Brown's position, which IA10 cites, is that conflict is part of design work, with healthy and unhealthy kinds (Brown 2013, ch. 4, contents; practice).`; Problem: the brief names Designing Together for working with disagreement; the unit draws on chapter titles only, though IA10 already quotes the book's text; Fix: `Brown's position, which IA10 cites, is that conflict is part of design work, with healthy and unhealthy kinds: his theory part opens "With conflict, teams must recognize how difficult conversations contribute to the design process", and chapter 7 puts the relation in one line, "If conflict is the engine, then collaboration is the oil" (Brown 2013, Part II and ch. 7, as cited in IA10, section 1.3; ch. 4, contents; practice).`; Basis: IA10, section 1.3 (both quotations are there word for word; I did not reopen the book pages).

11. [should-fix] [coverage] section 4.2; Current: `only its contents and the first edition's opening were seen for this unit.`; Problem: the brief names Hall for interviewing; the unit uses a chapter title only. Coverage stays thin until the chapter is read; the contents at least show the chapter is about stakeholder interviews; Fix: `the first edition's chapter 4 has the sections "Who are Stakeholders?", "Interviewing Stakeholders" and "What to do with Stakeholder Analysis" (contents); only its contents and the first edition's opening were seen for this unit.`; Basis: https://www.oreilly.com/library/view/just-enough-research/9780133964394/ (contents; casing as the page listing returned it).

12. [minor] [figure] section 3.2 (object map); Current: `is read at no more than one **review** (RV-04, RV-05 or RV-06, with its cadence and owner (IA9))`; Problem: AR-39 is read at two reviews (RV-06; RV-04); Fix: `is read at no more than two reviews, each a **review** (RV-04, RV-05 or RV-06, with its cadence and owner (IA9))`; and Current: `{"from": "row", "to": "review", "label": "is read at", "from_card": "0..*", "to_card": "0..1"}` Fix: `{"from": "row", "to": "review", "label": "is read at", "from_card": "0..*", "to_card": "0..2"}`; Basis: Deliverable B, AR-39.

13. [minor] [figure] section 3.2 (object map); Current: `Each row records one **IA7 decision** (its section or deliverable, and its AD-, O-, R-, T- identifiers)`; Problem: AR-43 to AR-49 record no IA7 decision; Fix: `Each row records at most one **IA7 decision** (its section or deliverable, and its AD-, O-, R-, T- identifiers), and the rows from other units' tables and the open questions record none`; and Current: `{"from": "row", "to": "decision", "label": "records", "from_card": "1", "to_card": "1", "dir": "to"}` Fix: `{"from": "row", "to": "decision", "label": "records", "from_card": "1", "to_card": "0..1", "dir": "to"}`; and, with finding 12, Current: `Counts at the line ends are 1, 0..*, 1..* and 0..1 in UML's notation.` Fix: `Counts at the line ends are 1, 0..1, 0..2, 0..* and 1..* in UML's notation.`; Basis: Deliverable B, B.5 and B.6.

14. [minor] [deliverable] section 3.2 and Deliverable B; Current: `| Input | on file, or absent with the TP- row and FO- forum named | IA10, "What later units take" |`; Problem: the field is defined as "on file", the register writes "records kept", DL-019 writes "kept"; Fix: `| Input | "records kept" where the product's own records serve (IA9, section 6.3), or absent with the TP- row and FO- forum named | IA10, "What later units take" |`; and Current: `the input: on file or absent; the fix` Fix: `the input: records kept or absent; the fix`; and Current: `"input: on file or absent"` Fix: `"input: records kept or absent"`; Basis: Deliverable B, the Columns paragraph.

15. [minor] [accuracy] Deliverable B, AR-26; Current: `| AR-26 | Contextual routes from the relationships, one for one (4.1; C.2) |`; Problem: IA7 says "almost one for one"; Fix: `| AR-26 | Contextual routes from the relationships, almost one for one (4.1; C.2) |`; Basis: IA7, section 4.1.

16. [minor] [attribution] Deliverable B, AR-10; Current: `interviews with HR managers at FO-07 (IA11, 2.6); tickets where a card question reaches HR`; Problem: IA11 2.6 is task-based usability testing; IA11's A.2 calls interviews "none of this unit's methods", as AR-19 does; Fix: `interviews with HR managers at FO-07 (none of IA11's methods); tickets where a card question reaches HR`; Basis: IA11, section 2.6 and A.2, rows 5 to 7.

17. [minor] [deliverable] Deliverable B, AR-40; Current: `tickets tagged DT-2 and A-3.4 as C1 (IA11, 2.4 for the reading); usability test of decisions (IA11, 2.6) | product management | RV-05 | records kept | backbone |`; Problem: section 3.2 says the settling test is cited first and the log second, and a test with people has its input absent (as AR-43 marks); Fix: `usability test of decisions (IA11, 2.6) at FO-07; tickets tagged DT-2 and A-3.4 as C1 (IA11, 2.4 for the reading) | product management | RV-05 | records kept; usability test absent: TP-09, FO-07 not met | backbone |`. No stated count changes. AR-11 has the same order (tickets before G-5's interviews); Basis: the unit's section 3.2, last paragraph; AR-43.

18. [minor] [deliverable] Deliverable B, B.6; Current: `The function whose answer the decision needs is named beside it.`; Problem: B.6's rows have no Evidence or Rung cell, though the unit says every register row carries its rung; Fix: `The function whose answer the decision needs is named beside it. Each row stands at C0: no evidence on any of the three questions is on file, so the Evidence and Rung columns give way to the answer needed and the default.`; Basis: the unit's "Left by" table (IA6 row) and Deliverable B's face.

19. [minor] [deliverable] section 5; Current: `Everything else can stay open, provided its row in the register says so:`; Problem: six rows on states and rules are marked backbone though the text names only five backbone parts; Fix: `States and rules fall under the same criterion, since a transition removed or a rule's outcome changed breaks a citation (IA9, section 4.4): their rows are marked backbone with the object they belong to (AR-15, AR-32, AR-40, AR-44, AR-48, AR-49). Everything else can stay open, provided its row in the register says so:`; Basis: IA9, section 4.4; Deliverable B, Fix column.

20. [minor] [accuracy] section 1.2; Current: `Perqo has examples of each kind on file (Perqo, fictional):`; Problem: four symptoms are listed and three cases follow; none is a reopened decision or a delegate, and IA10 calls the DL-015 positions compatible; Fix: `Perqo has three cases on file, two of conflict and one of an answer not given (Perqo, fictional):`; Basis: IA6, B.6; IA10, section 4.3; IA8, section 1.

21. [minor] [accuracy] Deliverable D, D.3, DL-018; Current: `| Version effect | a dated amendment to IA8's Deliverable: it adds a note and breaks no citation |`; Problem: the place to apply is the gaps table in IA8's section 1, which is not in IA8's Deliverable; Fix: `| Version effect | a dated amendment to IA8, section 1's gaps table: it adds a note and breaks no citation |`; Basis: IA8, section 1 (gaps table, column "Decided in").

22. [minor] [label] "Perqo facts set by this unit"; Current: `| The stakeholder map: power and interest on 0 to 10 for each of the twelve functions, quadrants split at 5, as C.1 gives them; register rows owned per function | Deliverable C | named people; attitudes not on record |`; Problem: the new fact that the map is revised at each FO-09 (Deliverable C's face) is not listed; Fix: `| The stakeholder map: power and interest on 0 to 10 for each of the twelve functions, quadrants split at 5, as C.1 gives them; register rows owned per function; the map revised at each FO-09 | Deliverable C | named people; attitudes not on record |`; Basis: Deliverable C's face.

23. [minor] [deliverable] Deliverable A, A.3; Current: `Build the five backbone parts of section 5 for what is stable`; Problem: the playbook is not usable alone here: the five parts are not named; Fix: `Build the five backbone parts of section 5 (objects, roles, top-level structure, addresses, the shared vocabulary) for what is stable`; Basis: the unit's section 5.

24. [minor] [style] section 4.4, step 4; Current: `so marking, not evidence, is what the gate checks.`; Problem: an "X, not Y" construction, which the brief's tone rule excludes; Fix: `so the gate checks the marking and asks for no evidence.`; Basis: brief preamble, tone.

## (1) Coverage

- Four shortages and symptoms: covered (section 1).
- Proxy evidence, eight kinds with limits: covered (section 2; all eight named in the brief).
- IA as hypotheses, assumption register, Bland and Osterwalder cited: covered (section 3).
- Stakeholder mapping, power and interest: covered (4.1; Deliverable C).
- Interviewing: covered from Brown's 2018 article; Hall thin (finding 11).
- Working with disagreement, Designing Together: thin (finding 10).
- The owner who will not answer: covered (4.4; DL-018).
- Minimum viable IA, the five parts and what stays open: covered (section 5).
- Escalation, decision log, visible risk: covered (section 6).
- Loop to IA9 and IA11: covered (section 7).
- Four named figures: all present, plus two.
- Deliverable, four parts: all present in full. Register: IA7's decisions covered but for finding 9.

## (2) to (4) Accuracy, figures, labels

Outside sources: all eight opened, none refused, so nothing is unverifiable. Sources cited "through the filed units" were checked as pointers only (the filed unit says what IA12 says it says) and not reopened. Every number names whose it is except findings 1 and 2. Practice, NN/g guidance, standards documentation and this unit's own synthesis are labelled where used; no vendor or correlational data appears.

## (5) Deliverable

Present in full. Follows from the evidence except findings 5 to 9. Usable alone except finding 23.

## Script results

- Register: 49 rows, AR-01 to AR-49, no gaps or repeats. B.1 15, B.2 8, B.3 16, B.4 3 (42 from IA7); B.5 4; B.6 3.
- Fix column: 25 backbone, 24 open.
- Read at: 28 rows name RV-05 or RV-06; 29 name any review.
- Owners: product management 15, IA designer 14, customer success 7, engineering 5, support 4, legal 3, security 1. Matches C.1's column.
- Rungs: all 46 rows of B.1 to B.5 at C0; B.6 has no rung cell (finding 18). Every rung quoted in sections 2 and 3.3 matches IA11's 6.4 table.
- Quadrants: 6 manage closely, 2 keep satisfied, 3 keep informed, 1 monitor. All 12 scatter points equal C.1's numbers.
- IA7's nine assumption rows map to AR-02, 37, 34, 01, 19, 21, 04, 29, 39, in IA7's order.
- Rows with no source: none. Every AR-01 to AR-42 pointer opens on the IA7 section or deliverable it names; AR-43 to AR-46 match A.2 rows 12, 13, 20, 25; AR-47 to AR-49 match IA8's G-5 to G-7.
- Identifiers: every V-, RV-, W-, TP-, FO-, DL-, G-, AD-, E-, M-, J-, BR-, DT-, H-, A-, EX-, R-, O-, AN-, TK-, T and C identifier in the unit exists in the filed units, except DL-017 to DL-019, which are this unit's.
- Decision log: DL-017 continues from DL-016. Deciders follow IA9 D.1 (DL-017 and DL-019 IA designer, as DL-011; DL-018 IA review with product management's sign-off). Version effects follow IA9 4.4. Statuses are IA9's five.
- Perqo label: on first use in the opening sentence. New facts are all in the facts table except finding 22.
- Public-site rules: no personal fact about the reader, no private person named, no real company's IA asserted ("this unit names none").
- Tones: 4, 5 and 6 are the only ones drawn, and each is named in the text.
- Matrix row labels: 2 to 12 characters. Flow notes match the text word for word, "[not run]" and "→ see IA9, D.2" included.
- Links: no link text is a long bare path.

## (7) Figures

1. objects, section 3.2: FIX. Every title, attribute, action and link label traces to the paragraph before it. Three line replacements, from findings 12, 13 and 14: `{"from": "row", "to": "review", "label": "is read at", "from_card": "0..*", "to_card": "0..2"}`; `{"from": "row", "to": "decision", "label": "records", "from_card": "1", "to_card": "0..1", "dir": "to"}`; attribute `"input: records kept or absent"`. Caption and kind fit.
2. matrix, section 3.3 (evidence ladder): PASS. Every cell traces to the six bullets ("C2 Observed. A small test with people…"); legend tones 5 and 6 named in the text; caption names section and sources; kind fits.
3. matrix, section 5 (minimum viable IA): PASS. Every cell traces to the paragraph "The figure gives each part three columns…"; every AR- row cited carries the Fix value the row claims; caption and kind fit.
4. flow, section 7 (the loop): PASS. Seven labels and notes match the numbered list exactly; caption and kind fit.
5. decision, Deliverable A, A.2: FIX. Questions and outcomes trace; the branch labels do not. No JSON change: the fix is the prose sentence in finding 3.
6. scatter, Deliverable C, C.2: PASS as drawn. Axis labels, ticks 0, 5, 10, quadrant names and all 12 points trace to C.1 and the paragraph before the figure. If finding 6 is applied, replace `{"label": "Legal", "x": 6, "y": 7, "tone": 5},` with `{"label": "Legal", "x": 6, "y": 6, "tone": 5},`.

## Confirmed

- Rosala, "Stakeholder Analysis for UX Projects", NN/g, 18 April 2021: author, date, the stakeholder definition, "advertently or inadvertently stop, hinder, or block your project" (said of high power, high interest), "need to be managed closely", "you should monitor them regularly", the attitude sentence, "spend the most energy on converting", "not a one-time activity"; the keep-satisfied and keep-informed paraphrases. PASS. https://www.nngroup.com/articles/stakeholder-analysis/
- Bland, Strategyzer, 4 August 2020, an excerpt from the book: both axes, "if proven wrong will cause our business idea to fail", the three type questions, the top-right quadrant wording and near-term experiments. PASS. https://strategyzer.com/library/how-assumptions-mapping-can-focus-your-teams-on-running-experiments-that-matter
- Bland and Osterwalder, Testing Business Ideas, Wiley, 2019, section 2.3 "Learn": the evidence-strength sentence and the opinions and facts examples, word for word; contents list 2.1 "Hypothesize" with "Assumptions Mapping". PASS. https://www.oreilly.com/library/view/testing-business-ideas/9781119551447/c02b.xhtml
- Brown, "The Delicate Art of Interviewing Stakeholders", 11 July 2018: all nine quoted phrases, the three lines of questioning, Hall's line as Brown reports it. PASS. https://medium.com/eightshapes-llc/the-delicate-art-of-interviewing-stakeholders-d6496443cbec
- Brown, Designing Together, New Riders, 2013: chapters 4, 5, 9 and 11 titled as quoted; description lists "46 conflict management techniques" and "31 difficult situation diagnoses". PASS. https://www.informit.com/store/designing-together-the-collaboration-and-conflict-management-9780321918635
- Hall, Just Enough Research, ch. 4 "Organizational Research": "The oral culture of how to get things done begins to outstrip the documentation", after "As an organization grows, it becomes more complex". PASS; the page does not state the edition, but its nine-chapter contents differ from the second edition's ten. https://www.oreilly.com/library/view/just-enough-research/9780133964394/ch04.html
- Hall, 2nd ed., A Book Apart, October 2019: ch. 4 "Organizational Research", ch. 6 "Competitive Research". PASS. https://www.oreilly.com/library/view/just-enough-research/9781492018032/
- Berners-Lee, "Cool URIs don't change", 1998: both quoted lines; "Designing mostly means leaving information out". PASS. https://w3.org/Provider/Style/URI
- IA11 6.4: rung wording C0 to C5; "can cite one test"; section 7's not-run rule quoted exactly; 6.1's verdicts; A.2 row numbers and routing for every row the register cites; V-06, V-10, V-11, V-16, V-17 say what the unit says.
- IA9: the version rule and "adds without breaking" (4.4); gate item 3; W-09, W-14, W-17 wording; RV-04 quarterly, both audiences; RV-05 monthly; RV-06 with first actions and failed sign-ins; RV-11; D.1 routing; D.3 fields and five statuses; Fowler's two quotations; "the register names, for each assumption, the RV- review that will read it".
- IA10: twelve functions; TP-01 to TP-12 forums, formats and fidelities as C.1 gives them; FO-01 to FO-09; the DL-011 quotation exact; the client rule exact; leadership "high power and low interest in the IA's detail"; engineering "consulted on fifteen", sales "four" and "seven"; "scope set and estimated before the structure is drawn"; DL-011 to DL-015 proposed; BR-3's "not yet decided"; 46 and 31 in section 1.3.
- IA8: G-5 to G-7 and where each is left free; "Whether the client's contract treats unspent money otherwise is left free, with G-7" (3.4); "as open questions with owners"; section 6's one-year test; written 9 November 2026; J-14 budgets.
- IA3: the proxy-status sentence (5.2); D1's organisation words and employees' queries; "refund" and the HR PDF; E2; "What this hands on".
- IA1 2.4 (one transactions table with a type field; Cooper, ch. 1, p. 16); IA2 section 4 (vocabulary first; "Keep the notation; extend the legend"), 1.1 and the decision table's header; IA4 4.3 and section 5; IA5 1.3 and S-7's owner Partnerships; IA6 1.4 and B.6; IA7 6.2 (Evans) and 6.3 (permissions once; the client signs off).

IA12 · verdict: fix · 3 errors, 8 should-fix, 13 minor.
