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

## Maintainer's notes (U-12 chat, 10 November 2026)

Each finding was verified before it was applied, against the unit, the filed units and, for the one outside source a finding added, the maintainer's own search and fetch under the web rule:

- 1 (error): holds. IA11, A.2: rows 15 to 19 and 21 to 24 go to the register and concern no Admin structure, nine rows; applied as given.
- 2 (error): holds. The closing assumption tables are IA6's ("What IA8 and IA11 take"), IA7's, IA8's, IA9's and IA10's, five in all; IA5 holds none and IA11 none; A.2's opening sentence gathers IA7 to IA10's rows, IA5's sign-in assumption among IA7's. Applied as given.
- 3 (error): holds. "yes" and "no" occur only in the decision figure; the sentence the fix adds traces every branch of the declaration as drawn. Applied as given; the declaration is unchanged, so the figure is re-checked on the new text.
- 4: holds. IA11, section 7 gives C0 and C1 with no employee reachable; section 6.4 gives C5 to "production records of the behaviour itself", and IA11's own AN- reads (Deliverable D, SG-A) stand at C5. Applied as given.
- 5: holds against IA10, A.1 (TP-06: BR-3 and the demo path, monthly; TP-07: the role matrix, DT-1 and DT-2, each new client; TP-09: word list and role matrix, each cycle touching Admin). Applied as given.
- 6: holds against the unit's section 4.1 rule (sits in the IA review above consulted). Applied in C.1 and in the scatter; the quadrant and the 6, 2, 3 and 1 counts stand; figure 6 reopened and re-checked.
- 7, 8: hold against Deliverable C's face and D.1. Applied as given.
- 9: holds. IA7, section 4.3 (the wireflow's "The next waiting claim opens") and A.4 (catalogue item, "-> view *new* in Admin", HR and finance managers). Applied as the checker's first option, the sentence, so the counts 42, 49, 16 and the owners stand.
- 10: holds; both quotations stand word for word in IA10, section 1.3. Applied as given.
- 11: holds. Maintainer's search for the first edition's contents returned oreilly.com/library/view/just-enough-research/9780133964394/; its fetch lists chapter 4's sections "Put an MBA Out of Work", "Who are Stakeholders?", "Interviewing Stakeholders" and "What to do with Stakeholder Analysis". Applied with that page linked in the sentence; the first edition's Sources line gains "Contents" with the same link, and the Hall line of the unsure list now reads "the contents of both editions", both made stale by the fix.
- 12 to 14: hold (AR-39 is read at RV-06 and RV-04; AR-43 to AR-49 record no IA7 decision; the register writes "records kept"). Applied as given, in the text and in figure 1's declaration; figure 1 re-checked.
- 15 to 24: hold (IA7, section 4.1, "almost one for one"; IA11, A.2 rows 5 to 7 and section 2.6; the unit's section 3.2 and AR-43; Deliverable B's face; IA9, section 4.4; IA10, section 4.3, which records DL-015 as a disagreement whose positions it reads as compatible, so "two of conflict" stands; IA8, section 1's gaps table; Deliverable C's face; section 5; the brief's tone rule). Applied as given.

No finding was a "no change required" minor. Every Current occurred once before its replacement (checked by script).

## Figure re-checks

Each report is the re-checker's hand-back, verbatim, extracted by script from its transcript (the `SubagentHandback` call); each re-checker was a fresh Opus 5.5 agent (claude-opus-5-5 in its transcript) given only the unit's text with its figures taken out, the captions, the figure's declaration, IA2 and the frames sheets `verify.py --shots` saved for page `read-ux-ia12`; transcript checks: no web, memory, Projects, connector, Artifact or Agent tool; every path inside its folder.

### Figure 1, check 2

**IA12 figure 1 (objects), check 2: PASS. The three fixes from check 1 hold. I found three minors, two of them in the figure, and no layout faults at any width or theme.**

There is a memory snapshot and the Project's instructions in my context. I did not use them as sources. The only sources were the files in `/home/claude/agents/ia12-fig1-check2`. The harness refused the report file write, so this message is the whole report.

**(7) Content and notation**
- **Kind and section:** objects, in section 3.2, "What a register row holds".
- **Check 1's fixes are in place:**
  - Row to review is `0..2`. It matches "is read at no more than two reviews". AR-39's Read at is "RV-06; RV-04"; every other row has one review or "none".
  - Row to decision is `0..1`. It matches "Each row records at most one IA7 decision".
  - The input attribute reads `input: records kept or absent`. It matches the paragraph word for word.
- **Labels traced:** every title, attribute, action, verb and count traces to the paragraph before the figure (line 121, "A register row holds its AR- identifier; ... Its actions are -> raise the rung and -> mark not run ..."). The decision end's `1` traces to "one row per structural decision or assumption". Every owner in Deliverable B is a function or the IA designer.
- **Tones:** tones 4 and 5 are named in the unit's intro (line 14) and in the paragraph. No tone 6 is drawn.
- **Kind fits the data:** six things and their relationships suit the objects kind.
- **IA2 notation:**
  - Relationship verbs read left to right on the level line and top to bottom on the others.
  - "records" reads right to left, so it carries the solid triangle pointing at IA7 decision.
  - Actions are written "-> verb", and nothing is dashed.
  - `0..1` and `0..2` are not in IA2's sheet, which lists only 1, 0..* and 1..*. They are valid UML, and the text says "in UML's notation", so this is not a fault.
- **Caption:** it says what the figure shows and the decision it supports. It names section 3.2 and Deliverable B, the sources of each field, and "Perqo is fictional".

**(8) As drawn**
- I opened every frames sheet: 320, 360, 390, 430, tablet and desktop, in dark and light.
- In every sheet, text stays inside its boxes, nothing overlaps, and the caption sits under the figure.
- Desktop and tablet show the whole figure in one frame.
- On the phone widths the figure scrolls sideways in its frame and shows the cue "scroll sideways for the whole figure". The last frame shows the test and review boxes in full.
- Labels that fade at the frame's edge are the renderer's scroll fade, not a fault.
- On the cream light theme, the tone 4 blue and tone 5 violet are distinct and readable.

**Findings**

[minor] figure 1; Current: `{"from": "row", "to": "dl", "label": "changes through", "from_card": "1..*", "to_card": "0..*"}`; Problem: the `1..*` at the register-row end says every decision log entry changes at least one register row. The text never says this, and the unit's own record contradicts it. DL-001 to DL-016 name no register rows. D.1's "Register rows (proposed)" field is dropped if DL-017 is declined. Fix: `{"from": "row", "to": "dl", "label": "changes through", "from_card": "0..*", "to_card": "0..*"}`. The paragraph's list "1, 0..1, 0..2, 0..* and 1..*" still holds after the change, because the test line keeps 1..*.

[minor] figure 1; Current: `"AD-, O-, R-, T- identifiers"` (declaration) and `its AD-, O-, R-, T- identifiers` (paragraph, line 121); Problem: no "T-" identifier appears anywhere in the unit. The register cites IA7's transitions as T1, T5 and T6, for example AR-15: "HR's approval checks the balance again, T5". The figure's label traces only to this one line of the paragraph. Fix: declaration `"AD-, O-, R- and T identifiers"`; paragraph `its AD-, O-, R- and T identifiers`.

[minor] figure 1 (the fault is in the unit's text, not the figure); Current: `"V- plan row, or IA11 method section"`; Problem: the attribute matches section 3.2's Test field ("one V- row of IA11's plan, or the IA11 method section that specifies the test"). Deliverable B does not: AR-04, AR-05, AR-09, AR-12 and AR-49 cite tests marked "none of IA11's methods", and no Admin row cites a V- row. Fix (only if 3.2's Test field is amended to match): `"V- plan row, IA11 method section, or none of IA11's methods"`.

figure 1: PASS

**Maintainer:** PASS. Its three minors verified and applied, since each corrects text the figure draws: the row-to-entry count `1..*` became `0..*` (no statement in the unit has every entry change a register row, and DL-001 to DL-016 name none); "AD-, O-, R-, T- identifiers" became "AD-, O-, R- and T identifiers" in the paragraph and the declaration (the only T- in the unit is inside DT-2; IA7's transitions are T1 to T6); the third in part: one Admin row does cite a plan row (AR-38 cites V-10; the note's "no Admin row cites a V- row" does not hold), but ten rows cite "none of IA11's methods", which section 3.2's Test field, the paragraph and the test box left out, so all three now name it. A correction to the text a figure draws reopens it: third check by a new agent.

### Figure 5, check 2

# IA12 figure 5 (decision), check 2

Figure 5 passes. I found one minor issue in the caption and no errors or should-fix items. The FIX from check 1 is resolved: the added A.2 sentence now traces every yes and no branch, and the declaration matches it.

I saw a memory snapshot and the Project instructions in my context and did not use them. I used only the files in /home/claude/agents/ia12-fig5-check2.

## (7) Content
- **Kind and section:** decision, in Deliverable A, A.2 "The tree". The figure marker is at line 256 of unit-without-figures.md, after the A.2 paragraph.
- **Questions:** all five are word for word in A.2: "The questions: "Do the requirements for it hold still?"; "Has the owner of the answer given it?"; "Is the content it organises there, and trusted?"; "Can you test it with the people it is for?"; "Is there a record of use: a log, tickets, paths?"."
- **Outcomes:** all six are word for word in A.2: "The outcomes: "Shifting requirements: fix the backbone only, log each version"; "Stakeholder shortage: write a default as a DL entry, escalate"; "Content shortage: structure from the objects and the data model; audit"; "Test it (IA11); record the rung reached"; "Read it at its RV- review; hold at C1"; "Hold at C0, labelled assumed; name the test"." The first three also match A.1's move column and A.3's headings exactly.
- **Branch labels and wiring:** traced to the sentence added after check 1: "Each question has two answers, yes and no: a no to any of the first three ends at that shortage's move and a yes goes on to the next question; at the fourth, yes ends at the test and no goes on to the fifth, where yes ends at the review and no at C0." The declaration matches it branch by branch:
  - question 1, no: Shifting requirements
  - question 2, no: Stakeholder shortage
  - question 3, no: Content shortage
  - question 4, yes: Test it
  - question 5, yes: Read it
  - question 5, no: Hold at C0
- **Identifiers:** IA11, RV-, DL, C0 and C1 all appear in the unit's text:
  - C0 and C1: sections 2 and 3.3
  - RV-: the "Read at" field in 3.2
  - DL: 4.4, step 3
- **Tones:** every box is tone 5. The unit says: "Every box is tone 5, shared, because the tree serves any surface." Tone 6 is not drawn and is not needed, because no outcome is a path that fails.
- **Caption:** it says what the figure shows and names the section (Deliverable A, A.2) and its sources. The one mismatch is in the findings below.
- **Kind fits the data:** a rule with branches is a decision.
- **IA2 notation:** the figure follows it.
  - Question boxes are outlined and outcomes are filled.
  - Branch labels are "yes" and "no", with yes always on the left.
  - Labels are in sentence case, nothing is dashed, and "assumed" appears as a word.
  - IA2 lets a question box be "a decision a named person makes". Deliverable A's face names that person, the IA designer.

## (8) As drawn
I opened every frames sheet: desktop, tablet, and phones at 320, 360, 390 and 430, in dark and light. I judged light on cream.
- **Desktop and tablet:** the whole figure fits in one frame. All text is inside its boxes, nothing overlaps, and the caption is under the figure. On cream, the filled violet outcomes with white text and the pale lilac questions with dark text both read clearly.
- **Phones:**
  - The drawing is wider than the column. It scrolls 442, 402, 372 and 332 px at 320, 360, 390 and 430.
  - It scrolls inside its frame, with the cue line "scroll sideways for the whole figure" above the caption.
  - Every box comes into view across the frames: "Test it" in the first frame, the root and "Shifting requirements" in the last.
  - No text sits outside a box, nothing overlaps and nothing is out of reach.
- **Phone opening frame:** at every phone width the opening frame shows the lower left of the tree, not the root, which sits at the right. This comes from where the renderer opens the frame and from the decision kind putting yes on the left. It is not a fault of the figure.
- **"Read it at its RV- review":** this box wraps after "RV-" at every width. It still reads as the text is written.

## Findings
[minor] figure 5; Current: `Shortages and symptoms from section 1;`; Problem: the caption says symptoms are a data source, but no symptom is drawn in the figure (the symptoms are in A.1's table, not in the tree); Fix: `Shortages from section 1;`

figure 5: PASS

The report is also saved at /home/claude/agents/ia12-fig5-check2/out/report.md.

**Maintainer:** PASS; its loop ends. Its one minor (the caption's "Shortages and symptoms from section 1") would change the declaration once more, and every word it touches is traced (section 1 holds the shortages and their symptoms, from which the tree's questions are drawn); recorded, not applied. Its notes on the phone's opening frame (the tree's lower left, the root at the right) and on the wrap after "RV-" rest on the renderer; recorded, not applied.

### Figure 6, check 2

## IA12 figure 6 (scatter), check 2: FIX

Figure 6 needs one caption fix. One section number in its caption is not in the unit (error), and the caption names the wrong subsection (minor). Every point matches the C.1 table, including the change that moved Legal's power to 6, and the figure renders cleanly at every width in both themes.

I saw a memory snapshot and the Project's instructions in my context and did not use them. Writing out/report.md was refused by the harness ("Subagents should return findings as text"), so this reply is the only copy of the report.

### (7) Content

**Kind and section.** Scatter, in Deliverable C, C.2 "The map" (unit lines 385–389). Its data comes from the C.1 table (lines 368–381).

**Points.** All twelve points match C.1 (power is y, interest is x):

| Point | x, y | C.1 row |
|---|---|---|
| Product management | 7, 9 | `\| TP-01 \| Product management \| 9 \| 7 \| Manage closely \|` |
| Engineering | 9, 7 | `\| TP-02 \| Engineering \| 7 \| 9 \| Manage closely \|` |
| Content team | 8, 7 | `\| TP-03 \| Content team \| 7 \| 8 \| Manage closely \|` |
| Marketing | 6, 2 | `\| TP-04 \| Marketing \| 2 \| 6 \| Keep informed \|` |
| Localisation | 1, 1 | `\| TP-05 \| Localisation \| 1 \| 1 \| Monitor \|` |
| Sales | 7, 3 | `\| TP-06 \| Sales \| 3 \| 7 \| Keep informed \|` |
| Customer success | 8, 4 | `\| TP-07 \| Customer success \| 4 \| 8 \| Keep informed \|` |
| Support | 9, 6 | `\| TP-08 \| Support \| 6 \| 9 \| Manage closely \|` |
| Clients | 4, 8 | `\| TP-09 \| Clients \| 8 \| 4 \| Keep satisfied \|` |
| Legal | 6, 6 | `\| TP-10 \| Legal \| 6 \| 6 \| Manage closely \|` |
| Security | 7, 6 | `\| TP-11 \| Security \| 6 \| 7 \| Manage closely \|` |
| Leadership | 2, 10 | `\| TP-12 \| Leadership \| 10 \| 2 \| Keep satisfied \|` |

- **Legal (the changed value):** power 6 is above 5, so Legal stays in Manage closely, as the table says.
- **Quadrant counts** match line 383: `Six functions are managed closely, two kept satisfied, three kept informed and one monitored.`

**Axes, ticks and quadrants**
- They trace to line 387: `"Interest in the IA's detail" (across) and "Power over the IA" (up), on 0 to 10 with ticks at 0, 5 and 10, the quadrants named as Rosala names them: Keep satisfied, Manage closely, Monitor, Keep informed`.
- The split at 5 traces to line 366: `split at 5 on each scale`.
- Each quadrant is drawn in the right corner: Keep satisfied top-left, Manage closely top-right, Monitor bottom-left, Keep informed bottom-right.

**Tone.** Tone 5 is named at line 387: `Every point is tone 5, shared`. The figure draws no tone 6.

**Kind fit.** The data is two measures, so scatter is the right kind. Line 492 lists the stakeholder map as `scatter (power by interest)`. Tone 5 is used as IA2 defines it ("shared").

**Caption sources**
- Rosala, title, NN/g and 2021 trace to lines 58 and 534.
- IA10, section 2.9 and IA10, section 5 trace to line 158.
- IA9, 4.1 and D.1, IA10, A.2, and IA10, A.1 trace to line 366.
- `IA10, section 1.1` is not in the unit (first finding below).

### Findings

[error] figure 6; Current: `functions from IA10, section 1.1 and A.1`; Problem: the unit never cites IA10, section 1.1 (it cites only IA11's, IA2's and IA4's sections 1.1 / 4.3). Its sources table gives the twelve functions as `IA10, sections 1.3, 1.4, 2.7, 4.2 and 4.3; Deliverable A | twelve functions, TP-01 to TP-12`, and C.1 cites `(IA10, A.1)`. The section number cannot be traced. Fix, in the declaration and in captions.md: `functions from IA10, A.1`

[minor] figure 6; Current: `who is asked when an answer is missing (Deliverable C, C.1)`; Problem: the figure sits in C.2 "The map"; C.1 is where its data comes from, and the caption already names C.1 in that role later on. Fix: `who is asked when an answer is missing (Deliverable C, C.2, from C.1)`

Replacement caption value for the declaration, with both fixes applied:
`"caption": "Stakeholder map: Perqo's twelve functions placed by power and interest in the IA's detail, with Rosala's four quadrants; supports the decision on how each function is engaged and who is asked when an answer is missing (Deliverable C, C.2, from C.1). Quadrants from Rosala, 'Stakeholder Analysis for UX Projects', NN/g, 2021; functions from IA10, A.1; leadership's placement from IA10, section 2.9; engineering's and sales' quadrants as IA10, section 5 reads them; every other placement set in C.1 by section 4.1's rule (power from IA9, section 4.1 and D.1, and IA10, A.2; interest from IA10, A.1). Every point tone 5, shared. Perqo is fictional."`

### (8) As drawn

I opened every frames sheet: 320, 360, 390, 430, tablet and desktop, each in dark and in light (judged on cream). No drawing fault.

- **Fit and scrolling.** Desktop and tablet fit in one frame. On phones the figure scrolls in its frame, with the cue line `scroll sideways for the whole figure`: 5 frames at 320 px, 4 at 360, 4 at 390, 3 at 430.
- **Labels.** Every label can be read whole in at least one frame. Labels cut at the frame edge in the middle frames come from the screenshot run's fixed scroll steps, which is renderer behaviour, not a fault of the figure.
- **Legal at 6,6** sits clearly above the dashed 5 line, with no overlap with Security or the quadrant line.
- **Leadership's dot** sits on the top border at power 10. Its label sits below and to the right and reads clearly.
- **Overlap and caption.** Nothing overlaps, and the caption is under the figure in every frame.
- **Light theme.** Dots, labels and quadrant names all read on cream.

figure 6: FIX

**Maintainer:** Applied as given, verified against the unit: "IA10, section 1.1" occurs nowhere else in the unit, which takes the twelve functions from IA10, A.1 (C.1); the caption now reads "functions from IA10, A.1" and names C.2 as the figure's place, C.1 as its data's. A caption is part of the declaration, so the figure is checked a third time by a new agent.

### Figure 1, check 3

IA12 figure 1 (objects), check 3: PASS, with two minor findings that change wording only.

The harness refused the write to out/report.md, so this reply is the only copy of the report. A memory snapshot and the Project instructions were in my context; I saw them and did not use them as a source.

**(7) Content**
- **Kind and section:** objects, in section 3.2 "What a register row holds". The figure marker is at line 123, under the prose declaration at line 121. The kind fits the data: things and their relationships.
- **Labels:** every box title, attribute, action, relationship label and count is in line 121, word for word apart from articles:
  - "A **register row** holds its AR- identifier; the decision or assumption; the evidence, its kind labelled; the rung: C0 to C5; the input: records kept or absent; the fix: backbone or open; and the status: not run, or the verdict. Its actions are -> raise the rung and -> mark not run."
  - "Each row records at most one **IA7 decision** (its section or deliverable, and its AD-, O-, R- and T identifiers) … is settled by at least one **test** …; is owned by one **owner** …; is read at no more than two reviews, each a **review** (RV-04, RV-05 or RV-06, with its cadence and owner (IA9)); and changes through **decision log entries** (DL- identifier, status, positions (DL-011, proposed), register rows (DL-017, proposed)). Counts at the line ends are 1, 0..1, 0..2, 0..* and 1..* in UML's notation."
- **Counts:** each traces to the text.
  - 0..1 at IA7 decision: "at most one".
  - 1 at the row end of "records": "one row per structural decision or assumption" (line 105).
  - 1..* at test: "at least one".
  - 1 at owner: "owned by one".
  - 0..2 at review: "no more than two".
  - 0..* at the other ends.
  - Deliverable B bears out the review count: the most any row has is two (AR-39, "RV-06; RV-04"), and only RV-04 to RV-06 appear.
- **Field values:** they match the section 3.2 table (lines 107 to 119):
  - Test: "one V- row of IA11's plan, or the IA11 method section…, or "none of IA11's methods" with the method named".
  - Input: "records kept" or absent.
  - Status: not run, or the verdict.
  - The decision log entry's status field is in the D.1 template (line 425).
- **Tones:** tone 4 for IA7 decision and tone 5 for the rest, both named at lines 14 and 121. The figure draws no tone 6, and the text gives tone 6 to figure 2 only, so nothing is missing.
- **Caption:** it names the artefact, what it shows, the decision it supports, section 3.2 and Deliverable B. Every source in it traces to the text:
  - Bland and Osterwalder 2019, section 2.1: line 99.
  - IA11, section 6.4: line 113.
  - IA11, Deliverable A, A.1 and A.2: line 114.
  - IA9, Deliverable C: line 116.
  - IA10, A.1: line 115.
  - IA9, D.3: the D.1 template, lines 412 to 425.
  - DL-011 and DL-017, proposed: lines 416 and 418.
  - It also says Perqo is fictional.
- **IA2 notation:** followed.
  - Objects have filled title bands; actions sit after a rule line and read "-> verb".
  - Lines have no heads, with counts at each end.
  - "is settled by" reads left to right on a level line, and the three lower links read top to bottom.
  - "records" reads right to left on a level line, so it carries the small solid triangle pointing at IA7 decision, as IA2 section 5.2 requires.
  - Titles are lower-case data-model names, and "proposed" is written as a note.

**(8) As drawn**
I opened every frames sheet (320, 360, phone 390, 430, tablet and desktop, dark and light) and the opening frames.
- **Desktop and tablet:** one frame, the whole figure fits. Text sits inside the boxes, nothing overlaps, and the caption is under the figure.
- **Phones:** the figure scrolls in its frame, with "scroll sideways for the whole figure" under it and the caption after that.
  - The last frame shows the test and review boxes whole: 442 of 442 px at 320, 402 at 360, 372 at 390 and 332 at 430.
  - The register row, decision log entry, owner and IA7 decision boxes are each whole in at least one frame.
  - The fades at the edges are the scroll mask.
- **Light theme on cream:** every box, label and count is legible.
- **Opening frame at 390:** the sticky section bar clips the top. This is the known behaviour for a figure taller than the viewport, not a fault of the figure.

**Findings**
- [minor] figure 1; Current: `"V- plan row, IA11 method section, or none of IA11's methods"`; Problem: section 3.2's text has "or none of IA11's methods, with the method named" (line 121; table, line 114: "with the method named (an interview, a legal reading)"). Without that qualifier the box can read as "no test", which contradicts the 1..* count beside it. Fix: `{"id": "test", "title": "test", "tone": 5, "attrs": ["V- plan row, IA11 method section, or none of IA11's methods, the method named", "forum where it runs", "rung it reaches"]}`
- [minor] figure 1; Current: `Object map: the structure of the assumption register, one row per structural decision with its evidence,`; Problem: section 3.2 says "one row per structural decision or assumption" (line 105). The figure's 0..1 at IA7 decision exists because some rows record no decision ("the rows from other units' tables and the open questions record none"), and the caption's wording hides that. Fix: `Object map: the structure of the assumption register, one row per structural decision or assumption with its evidence,`

figure 1: PASS

Crops and composite sheets are in /home/claude/agents/ia12-fig1-check3/out/.

**Maintainer:** PASS; its loop ends after three checks. Its two minors would change the declaration once more and every word they touch is already traced (section 3.2's table and paragraph give "none of IA11's methods, with the method named"; "structural decision" is the register's own phrase, and the paragraph before the figure says which rows record none): recorded, not applied (U-7's rule, 4 Nov 2026).

### Figure 6, check 3

IA12 figure 6, check 3: PASS. Two minor findings, neither blocking. The harness refused the write to out/report.md, so this reply is the whole report.

Seen and not used: a memory snapshot, the Project instructions and the Project doc list were in my context. I drew nothing from them.

(7) Content
- Kind and place: a scatter, in Deliverable C, C.2 ("[figure 6 taken out ...]" sits under "### C.2 · The map", line 389). The unit's own rows give the kind: D.5 has "| Stakeholder map | scatter (power by interest) |" (line 492). Two measures call for a scatter, so the kind fits.
- Axes: "Interest in the IA's detail" and "Power over the IA", 0 to 10 with ticks 0, 5 and 10. This matches C.2 word for word: 'by "Interest in the IA's detail" (across) and "Power over the IA" (up), on 0 to 10 with ticks at 0, 5 and 10'.
- Quadrants: they are split at 5. C.1 says "split at 5 on each scale". Their names are "Keep satisfied, Manage closely, Monitor, Keep informed", which is C.2's own list. As drawn, Keep satisfied is top left, Manage closely top right, Monitor bottom left and Keep informed bottom right. That matches C.1's definitions: Keep satisfied is "power above 5, interest 5 or less", and so on.
- The twelve points, as x = interest and y = power, each against its row in the C.1 table. All twelve match.
  - Product management (7,9): "| TP-01 | Product management | 9 | 7 |"
  - Engineering (9,7): "| TP-02 | Engineering | 7 | 9 |"
  - Content team (8,7): "| TP-03 | Content team | 7 | 8 |"
  - Marketing (6,2): "| TP-04 | Marketing | 2 | 6 |"
  - Localisation (1,1): "| TP-05 | Localisation | 1 | 1 |"
  - Sales (7,3): "| TP-06 | Sales | 3 | 7 |"
  - Customer success (8,4): "| TP-07 | Customer success | 4 | 8 |"
  - Support (9,6): "| TP-08 | Support | 6 | 9 |"
  - Clients (4,8): "| TP-09 | Clients | 8 | 4 |"
  - Legal (6,6): "| TP-10 | Legal | 6 | 6 |". This reflects the move to 6, and it falls in Manage closely as the row says.
  - Security (7,6): "| TP-11 | Security | 6 | 7 |"
  - Leadership (2,10): "| TP-12 | Leadership | 10 | 2 |"
- Quadrant counts: the drawing gives 6 / 2 / 3 / 1. C.1 says "Six functions are managed closely, two kept satisfied, three kept informed and one monitored." No point sits on a split line.
- Tone: every point is tone 5. Line 14 names it: "Tone 5, shared, carries most figures, because ... the stakeholders serve every surface". C.2 says: "Every point is tone 5, shared". The figure draws no tone 6, and line 14 names tone 6 only for the ladder. That is correct.
- Caption: it says what the figure shows, names its place ("Deliverable C, C.2, from C.1") and names its sources. Each source traces to the unit's text:
  - Rosala 2021: section 4.1 and the Sources list
  - "functions from IA10, A.1": C.1, "interest from the fidelity it reads (IA10, A.1)", and the TP-11 row "(IA10, A.1, TP-11)"
  - "leadership's placement from IA10, section 2.9": section 4.1 and C.1
  - "engineering's and sales' quadrants as IA10, section 5 reads them": C.1, "engineering's and sales' quadrants are those IA10 read from IA9's tables (IA10, section 5)"
  - "power from IA9, section 4.1 and D.1, and IA10, A.2; interest from IA10, A.1": C.1 word for word
  The caption no longer cites any IA10 section the unit does not cite.
- Notation (IA2, section 5): the tones are used as IA2 defines them. IA2 sets no scatter-specific symbols ("further kinds for dates and numbers").

(8) As drawn
- Desktop and tablet, dark and light: one frame each, and the whole figure fits. Every label clears its dot and its neighbours. Engineering's label sits above its dot, clear of "Content team". The quadrant names sit inside the plot corners and the caption sits under the figure. On cream the dots, labels and dashed splits all read clearly.
- Phone 320 (5 frames), 360 (4), 390 (4) and 430 (3), dark and light: the figure is wider than its column. It scrolls in its frame, the "scroll sideways for the whole figure" cue line shows in every frame and the caption sits under it.
  - The last frame shows the right edge in full: Manage closely, Support, Customer success, Keep informed, the 10 tick and the whole x-axis label.
  - The first frame shows the left edge in full: the y-axis label, Keep satisfied and Monitor.
  - Every label is whole in at least one frame. Nothing overlaps.
  - Labels faded or cut at the frame edges mid-scroll ("Clie", "Customer su", "egal") come from the scroll frame's edge fade and the fixed screenshot steps. They are not a fault of the figure.
- Opening frames: at 320 and 360 the sticky section bar covers the plot's upper middle. This is the known clipping in the opening-frame shot, not a fault. At 430 the opening frame shows the plot whole up to the 5 tick.

Findings
- [minor] figure 6; Current: `leadership's placement from IA10, section 2.9`; Problem: IA10, section 2.9 gives leadership a quadrant ("leadership in the keep-satisfied quadrant", section 4.1). The plotted numbers (10, 2) are set in C.1 by this unit, so "placement" claims more for IA10 than the unit quotes. The unit's C.1 uses the same wording ("Leadership's placement is IA10's"), so the caption matches the unit. Fix it only if C.1 is reworded the same way; Fix: `leadership's quadrant from IA10, section 2.9`
- [minor] figure 6; Current: the quadrant split lines are drawn dashed; Problem: IA2's legend sets "No dashed lines: nothing is drawn dashed; a condition is written". The scatter renderer draws its split lines dashed, and the declaration cannot change that. This rests on renderer behaviour, not on the figure; Fix: none in the declaration; `none (renderer: kit scatter split lines; outside this figure)`

figure 6: PASS

Files I made are in /home/claude/agents/ia12-fig6-check3/out/: the frame-sheet crops (*-part*.png, *-pair-part*.png) and openers.png.

**Maintainer:** PASS; its loop ends after three checks. Its first minor is conditional on rewording C.1, and C.1's "Leadership's placement is IA10's" holds: IA10, section 2.9 places leadership in the keep-satisfied quadrant, which the unit's section 4.1 reports as "IA10 already placed one Perqo function"; recorded, not applied. Its second rests on the renderer (the scatter kind draws its quadrant splits dashed; the declaration cannot change it) and is recorded, not applied.
