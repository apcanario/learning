---
code: IA12
title: "When the inputs are missing: building the backbone anyway"
course: ux · IA · Information Architecture
model: Opus 5.5
written: 2026-11-10
search: off
---

# IA12 · When the inputs are missing: building the backbone anyway

IA4 to IA10 built and placed the IA of Perqo (Perqo, fictional), and IA11 named the tests that would settle it. Most of those tests have not run. No admin user from a client has sorted a card or walked a tree, and Perqo Admin's structure, which IA7 drew, stands on reasoning, on the filed units' decisions and on the literature they cite. That is the normal condition of IA work: the research is missing or weak, a stakeholder will not answer, the content is not written or cannot be trusted, and the requirements move. This unit covers the four shortages and their symptoms; proxy evidence, where to find it and what each kind cannot show; the IA treated as a set of hypotheses, recorded in an assumption register after Bland and Osterwalder's assumption mapping; stakeholder mapping and handling, including what to do when the person who owns an answer will not give it; the minimum viable IA, what must be fixed early because it is expensive to change and what can stay open; escalation, the written decision log and how to make the risk visible without blocking the team; and how the backbone stays revisable once evidence arrives. The deliverable is the incomplete-inputs playbook: the triage decision tree, the assumption register filled for Perqo Admin, the Perqo stakeholder map, and the one-page decision log template with three entries filled.

Every figure uses IA2's notation (IA2, section 5.2 and the notation sheet). This unit draws three of its six tones. Tone 5, shared, carries most figures, because the triage, the ladder, the register and the stakeholders serve every surface. Tone 4, Perqo Admin and the HR and finance managers who use it, carries what belongs to Admin: IA7's decisions in the register's structure, and the Perqo Admin column of the minimum viable IA. Tone 6, a stop, marks a rung of the evidence ladder that no proxy evidence reaches.

What the filed units hand on, and where this unit uses it:

| From | What it hands on | Used in |
|---|---|---|
| IA3, section 5.2, Deliverable E2 and "What this hands on" | the Help centre's search log as "proxy evidence, useful when no one can be interviewed, and labelled as proxy"; each row a hypothesis | sections 2 and 3; Deliverable B |
| IA7, sections 2 to 6, Deliverables A to D and its assumption table | Perqo Admin's structural decisions and nine assumptions with their tests | section 3.4; Deliverable B |
| IA8, "What later units take" and section 1 | its assumption rows, and G-5, G-6 and G-7 kept "as open questions with owners" | Deliverable B, B.5 and B.6 |
| IA9, sections 4 to 6 and Deliverables A to D | the change-control flow, the decision log DL-001 to DL-010 and its version rule, RV-01 to RV-12, W-09 and W-17, production signals; "the register names, for each assumption, the RV- review that will read it" | sections 6 and 7; Deliverables B and D |
| IA10, sections 1.3, 1.4, 2.7, 4.2 and 4.3; Deliverable A | twelve functions, TP-01 to TP-12, forums FO-01 to FO-09, the client rule, the positions field (DL-011), DL-011 to DL-015; leadership in Rosala's keep-satisfied quadrant; an input whose forum has not met is marked absent | section 4; Deliverables B, C and D |
| IA11, sections 1.2, 6.1, 6.4 and 7; Deliverable A, A.1 and A.2 | the confidence ladder C0 to C5, metrics M-01 to M-11, plan rows V-01 to V-17, table A.2's routing to this register, and the rule that a test not run leaves its row in place, marked not run, at its current rung | sections 3 and 7; Deliverables A and B |
| IA1, surfaces map; IA2, sections 3 and 4, the notation sheet and the decision table | the three surfaces; the five faults; editing rules; the face; the catalogue DL-017 proposes two rows for | sections 5 and 6; Deliverables |

The filed units left these questions to this unit by name. Where each is answered, or why it stays open:

| Left by | The question | Answered in, or open |
|---|---|---|
| IA3, section 5.2; Deliverable, "What this hands on" | work from the search log as proxy, each row a hypothesis | answered: section 2; register rows read at RV-04 (Deliverable B) |
| IA3, E2 | support's quarterly reading of the log feeds IA11 and IA12 | answered: RV-04 (IA9) is the reading; the register's "Read at" column names it |
| IA6, section 1.4 | an IA built without research labels every result assumed | answered: section 3; every register row carries its rung |
| IA6 and IA8, assumption tables ("IA12 as proxy") | support's tickets on declines as proxy for whether employees understand a decline | stays with IA11's plan: V-11 with TK-1, an app question; not in the Admin register |
| IA7, "What IA8 and later units take" | the nine assumptions, each with its test | answered: Deliverable B, rows AR-01, AR-02, AR-04, AR-19, AR-21, AR-29, AR-34, AR-37, AR-39 |
| IA8, section 6 | whether a reader a year later can trust a J- row, "kept" in this register | stays open: a test of the process, outside Admin; this unit fills the Admin part of the register only (section 3.4) |
| IA8, "What later units take"; IA10, section 2.9 | G-5, G-6 and G-7 as open questions with owners | answered: Deliverable B, B.6, each with an owner; G-7 is the worked escalation (section 4.4; DL-018) |
| IA9, "What later units take" | the RV- review that reads each assumption whose test is a log, a ticket tag or a path | answered: Deliverable B, "Read at" column |
| IA10, section 4.2 | a position not taken goes to the register when its reopening test is a test with people | answered: no such position concerns Admin today (section 4.3) |
| IA10, "What later units take" | an input whose forum has not met is marked absent, with the function named | answered: Deliverable B, "Input" column |
| IA11, sections 6.4 and 7; "What later units take" | rungs cited by identifier; one test per row; not run leaves the row at its rung; TP-05 at C0 with DD-IA3 named | answered for Admin: Deliverable B; TP-05's row stays open outside Admin (section 3.4) |

## 1 · Four shortages, and how each shows itself

A designer rarely meets one shortage at a time, and each has symptoms that show before anyone names it. The symptoms below are this unit's synthesis from the faults the filed units met at Perqo and from the sources cited with each; none has been measured as a predictor. The point of naming them is triage: the move that answers one shortage does nothing for another (Deliverable A).

### 1.1 · No research, or research that cannot be trusted

**Symptoms.** Statements about users with no source ("HR always starts from the employee"); personas made in a workshop from the team's memory; a test promised for later with no date; the organisation's words in the labels. IA3 found the last one in the Perqo app: "Documents", "Perks" and "Discover" were the organisation's words, while employees searched "approval", "allowance" and "gym" (IA3, Deliverable, D1). Research that exists can also fail: a sample from the wrong people or from one place, a task that gave the answer away, a method that measured another question (IA11, section 6.3). IA11's caution applies here in full: colleagues sorting cards test the team's own model, which is the claim the test was meant to check (IA11, section 7, on Nielsen's distinct-groups condition, Nielsen, NN/g, 2000).

**What it costs.** A structure built on the team's model is a set of claims about people that nobody has checked (IA4, section 4.3; IA11, section 1.1).

### 1.2 · Stakeholders absent, unwilling or in conflict

**Symptoms.** A decision reopened at each meeting; the owner of a question sending a delegate who cannot decide; two functions giving opposite answers to the same question; a question that has sat unanswered across several cycles. Perqo has examples of each kind on file (Perqo, fictional): the partnerships team asked for card offers on Home and in Benefits, and IA6 recorded the request and gave it neither placing (IA6, B.6); legal and product management hold different positions on who may open a claim's receipt (DL-015; IA10, section 4.3); and what happens to money unspent at a period's end, G-7, has been open since IA8 named it (IA8, section 1).

**What it costs.** Maria Rosala's NN/g article warns that stakeholders with high power and interest can "advertently or inadvertently stop, hinder, or block your project" ("Stakeholder Analysis for UX Projects", Nielsen Norman Group, 18 April 2021, [nngroup.com, stakeholder analysis](https://www.nngroup.com/articles/stakeholder-analysis/); NN/g guidance).

### 1.3 · No content, or content that cannot be trusted

**Symptoms.** Wireframes with placeholder text where labels and lists should be; an inventory with no owner per page; articles that contradict the product; a document written for one audience used by another. IA3 found two at Perqo: the article "Why was my claim rejected?" said "refund" where the app says Claim, and the approval rule employees needed was a PDF written for HR (IA3, section 5.2). IA5's audit found pages that duplicated others and a campaign page that outlived its campaign (IA5, section 1.3).

**What it costs.** A structure needs things to organise. Without them the designer organises guesses about content, and the labels are tested against nothing (IA2, section 1.1: an inventory at F2 before any redesign).

### 1.4 · Requirements that contradict or shift

**Symptoms.** Two documents that state different rules; a requirement that changes between the meeting and the minutes; a scope signed before the structure is drawn. IA10 named the last as product management's failure mode: "scope set and estimated before the structure is drawn", which at Perqo missed joins that only appeared when the layers were laid together (IA10, section 4.1; IA8, section 1). Garrett's planes overlap in time, so structure work begins while scope is open (IA9, section 1.2; Garrett, *The Elements of User Experience*, 2nd ed., 2011, ch. 2), and a moving scope is the normal state of that overlap.

**What it costs.** Everything built on the moving part moves with it. Section 5 says which parts of an IA can be built while requirements move and which cannot.

Dan Brown's *Designing Together* treats the people side of these shortages as design work: its chapters run from "The Role of Conflict in Design" and "Assessing Conflict: What's Really Wrong" to "Situations: Circumstances and Scenarios Common to Design Projects" and "Conflict Patterns: Behaviors for Reaching Resolutions", and the publisher's description lists 46 conflict management techniques and 31 diagnoses of difficult situations (New Riders, 2013, chs 4, 5, 9 and 11, contents and description, [informit.com, Designing Together](https://www.informit.com/store/designing-together-the-collaboration-and-conflict-management-9780321918635); practice). Only the contents and description were read for this unit, so it takes from the book only its framing: that diagnosing what is really wrong comes before choosing a move.

## 2 · Proxy evidence: where to find it and what each kind cannot show

Proxy evidence is any record or document that stands in for research with the people the structure is for. IA3 gave it its status at Perqo: the Help centre's search log is "proxy evidence, useful when no one can be interviewed, and labelled as proxy" (IA3, section 5.2), after Louis Rosenfeld's point that analytics show what happens without showing why, so findings from a log are hypotheses to be tested with people (Kristina Mausser, "Site Search Analytics: A Conversation with Lou Rosenfeld", UXmatters, 18 July 2011, as cited in IA3, section 5.2; interview, practice). IA11 then put a ceiling on it: with no user reachable, the ladder leaves C0 and C1 (IA11, section 7).

Bland and Osterwalder's account of evidence strength gives a second test for any proxy. "The strength of a piece of evidence determines how reliably the evidence helps support or refute a hypothesis"; opinions are beliefs, "When people say things like 'I would…,' 'I think _____ is important,' 'I believe…,' or 'I like…'", and facts are events, "When people say things like 'Last week I _____ ,' 'In that situation I usually _____ ,' or 'I spent _____ on'" (David J. Bland and Alexander Osterwalder, *Testing Business Ideas: A Field Guide for Rapid Experimentation*, Wiley, 2019, section 2.3, "Learn", subsection "Evidence", read in a preview on O'Reilly's platform, [oreilly.com, Learn](https://www.oreilly.com/library/view/testing-business-ideas/9781119551447/c02b.xhtml); practice from a standard work of product strategy). A record of what people did is a fact in their sense; a note of what someone said they would do is an opinion.

Each kind of proxy, where it is at Perqo, what it shows and what it cannot show. The highest rung is IA11's (section 6.4): C0 for reasoning at a desk, C1 for "a log, ticket tags or paths, read once", C5 for "production records of the behaviour itself".

| Proxy | At Perqo (Perqo, fictional) | Shows | Cannot show | Highest rung alone | Source |
|---|---|---|---|---|---|
| Support tickets | support's tickets, tagged by surface, A-, AD-, S- or H- identifier and DT- tree, read monthly (IA9, section 6.2; RV-05) | where people get stuck, in their own words, at every stage of the relationship | anyone who did not contact support; why the structure failed | C1 | Dana Chisnell, "Call centers as a source of data", 2016 (practice), as cited in IA9, section 6.2 |
| Search logs | the Help centre's logs for both audiences, read quarterly (IA9, RV-04) | zero-result queries, frequent queries for things held and not held, reformulations | why people searched; what non-searchers did (IA11, section 2.4) | C1 | Farrell, "Search-Log Analysis", NN/g, 2017, as cited in IA3, section 5.2 |
| Sales-call notes | questions from tenders and demos, logged at the pre-sales briefing, FO-04 (IA10, A.2) | what buyers ask about and the words they use | what employees or admin users do; most notes record what a buyer says they would do, an opinion in Bland and Osterwalder's sense | C0 | Bland and Osterwalder 2019, section 2.3; this unit's reasoning |
| Analytics | each Admin page view by AD- identifier and each app screen view by A- identifier (IA9, section 6.3); Admin's failed sign-ins | frequencies, paths, drop-offs, at the scale of everyone who used the product | intent (IA11, section 2.5); anyone who never opened the surface | C1 for a path read for a hypothesis; C5 where the assumption is about the behaviour itself, such as how often a page is used | Cardello, NN/g, 2013, as cited in IA9, section 6.3; IA11, section 6.4 |
| Competitors' public screens | the public pages and help centres of other benefits platforms; this unit names none | what others chose to show, and their words for shared things | whether it works for anyone; anything behind a sign-in, which is where a backoffice sits | C0 | this unit's reasoning; Erika Hall, *Just Enough Research*, 2nd ed., 2019, ch. 6, "Competitive Research" (title only); the course's sourcing rule on real companies' IA |
| The existing system's structure | IA1's six Admin areas; IA3's as-is app; IA5's audit of perqo.com | what was built and named, faults included | whether it was ever right: IA3's as-is held the organisation's words (IA3, D1) | C0 | IA2, section 1.1; IA3, Deliverable |
| The data model | one table of transactions with a type field; an allocation per employee, category and period (IA1, section 2.4) | what is stored and how records relate | how people think of it: the implementation model, which an interface should not follow (Cooper and others, *About Face*, 4th ed., 2014, ch. 1, p. 16, as cited in IA1, section 2.4) | C0 | IA1, section 2.4; IA7, section 6.1 |
| Documentation | Help centre articles; the configuration workbook per client (IA10, section 2.5); contracts | rules as someone wrote them down | whether they are current or followed; Hall: as an organisation grows, "The oral culture of how to get things done begins to outstrip the documentation" (*Just Enough Research*, 1st ed., A Book Apart, 2013, ch. 4, "Organizational Research", opening, [oreilly.com, ch. 4](https://www.oreilly.com/library/view/just-enough-research/9780133964394/ch04.html)) | C0 | Hall 2013, ch. 4 |

Three readings follow for Perqo Admin. First, Admin's own records are the strongest proxy it has: page views by AD- identifier and failed sign-ins can settle frequency questions at C5 without recruiting anyone, because the assumption and the record are about the same behaviour (IA11, section 6.4, C5; SG-A's rule for AN-1 to AN-4). Second, the Help centre's log is weaker for Admin than for the app: IA3's read was of the For employees log (IA3, section 5.2), and IA9 extended the quarterly read to both audiences (IA9, RV-04), so no read of the HR and finance log is on file. Third, every proxy above records people who used the product, and a backoffice's users are few: three admin users at the sizing client (IA7, section 2.2, assumed), so a single client's records are one profile (IA11, section 5, on Katsanos and others 2019).

## 3 · The IA as a set of hypotheses: the assumption register

### 3.1 · Assumption mapping

David Bland and Alexander Osterwalder's book sets a step before any experiment: write the hypotheses an idea rests on, then sort them. Its section 2.1, "Hypothesize", holds the technique it calls Assumptions Mapping (Bland and Osterwalder 2019, contents of section 2.1, seen in the same preview). Bland's own excerpt of it gives the two axes. Evidence runs from "have evidence" to "no evidence": "It's about having observable evidence, qualitative or quantitative, to support your hypothesis." Importance runs from "important" to "unimportant", and the team asks which hypothesis, "if proven wrong will cause our business idea to fail". Hypotheses are sorted by type, "Desirability: Does the market want this idea?", "Feasibility: Can we deliver at scale?" and "Viability: Is the idea profitable enough?", and near-term experiments go to the top-right quadrant, where hypotheses are "critical for success and yet have the least amount of evidence to support them" (David J. Bland, "How assumptions mapping can focus your teams on running experiments that matter", Strategyzer, 4 August 2020, an excerpt from the book, [strategyzer.com, assumptions mapping](https://strategyzer.com/library/how-assumptions-mapping-can-focus-your-teams-on-running-experiments-that-matter); practice).

The technique is for business ideas, and it is practice with no measurement behind it. Brought to an IA, on this unit's reading, it needs three changes. The hypotheses are the structural decisions, one per row, each tied to an artefact identifier, so a test result has a place to land. The evidence axis becomes IA11's ladder, C0 to C5, because the course already has a scale with defined rungs and a rule for what each may decide (IA11, section 6.4); a second scale would let two rungs mean one thing. And importance becomes a question this unit can answer from the artefacts: would a wrong answer be expensive to change once built? That question is section 5's, and its answer is two values, backbone and open.

### 3.2 · What a register row holds

The register is one table, one row per structural decision or assumption, with these fields (this unit's, Perqo, fictional):

| Field | Holds | From |
|---|---|---|
| ID | AR- and a number, never reused | IA2, section 4 (stable identifiers) |
| Decision or assumption | one line, in the artefact's words | Bland and Osterwalder's hypothesis, one per row |
| Source | the unit, section and deliverable that took it, with identifiers | IA9, section 2.3 (citing by identifier) |
| Evidence, and its kind | what supports it now, each item labelled: assumed, reasoning, a filed decision, guidance, a standard, practice, or proxy (named) | IA3, section 5.2 (labelled as proxy); IA11, section 1.1 |
| Rung | C0 to C5, cited by identifier | IA11, section 6.4 |
| Test | one V- row of IA11's plan, or the IA11 method section that specifies the test, with the forum where it runs | IA11, Deliverable A, A.1 and A.2 |
| Owner | the function that gets the test run, from IA9's owners and IA10's functions | IA9, Deliverables A and C; IA10, A.1 |
| Read at | the RV- review that reads it, when its test is a log, a ticket tag or a path | IA9, Deliverable C; "What later units take" |
| Input | on file, or absent with the TP- row and FO- forum named | IA10, "What later units take" |
| Fix | backbone (expensive to change once built) or open | section 5 |
| Status | not run, or the verdict with the plan row and date | IA11, sections 6.1 and 7 |

The register's structure as an object map, in IA2's notation. A **register row** holds its AR- identifier; the decision or assumption; the evidence, its kind labelled; the rung: C0 to C5; the input: on file or absent; the fix: backbone or open; and the status: not run, or the verdict. Its actions are -> raise the rung and -> mark not run. Each row records one **IA7 decision** (its section or deliverable, and its AD-, O-, R-, T- identifiers); is settled by at least one **test** (a V- plan row, or IA11 method section; the forum where it runs; the rung it reaches); is owned by one **owner** (a function (IA10, TP-) or the IA designer (IA9)); is read at no more than one **review** (RV-04, RV-05 or RV-06, with its cadence and owner (IA9)); and changes through **decision log entries** (DL- identifier, status, positions (DL-011, proposed), register rows (DL-017, proposed)). Counts at the line ends are 1, 0..*, 1..* and 0..1 in UML's notation. IA7's decision is tone 4, Perqo Admin; the rest are tone 5, shared.

```viz
{"kind": "objects", "caption": "Object map: the structure of the assumption register, one row per structural decision with its evidence, rung, test, owner, review and decision log entries; supports the decision on what a register row must hold before a structure ships on assumption (section 3.2; Deliverable B). Fields set in section 3.2: hypotheses one per row after Bland and Osterwalder, Testing Business Ideas, 2019, section 2.1; rungs from IA11, section 6.4; tests from IA11, Deliverable A, A.1 and A.2; reviews from IA9, Deliverable C; functions from IA10, A.1; decision log from IA9, D.3, with positions (DL-011) and register rows (DL-017) proposed. Tone 4 Perqo Admin; tone 5 shared. Counts in UML multiplicity notation. Perqo is fictional.",
 "objects": [
  {"id": "decision", "title": "IA7 decision", "tone": 4, "attrs": ["section or deliverable", "AD-, O-, R-, T- identifiers"]},
  {"id": "row", "title": "register row", "tone": 5, "attrs": ["AR- identifier", "decision or assumption", "evidence, its kind labelled", "rung: C0 to C5", "input: on file or absent", "fix: backbone or open", "status: not run, or the verdict"], "actions": ["-> raise the rung", "-> mark not run"]},
  {"id": "test", "title": "test", "tone": 5, "attrs": ["V- plan row, or IA11 method section", "forum where it runs", "rung it reaches"]},
  {"id": "owner", "title": "owner", "tone": 5, "attrs": ["a function (IA10, TP-) or the IA designer (IA9)"]},
  {"id": "dl", "title": "decision log entry", "tone": 5, "attrs": ["DL- identifier", "status", "positions (DL-011, proposed)", "register rows (DL-017, proposed)"]},
  {"id": "review", "title": "review", "tone": 5, "attrs": ["RV-04, RV-05 or RV-06", "cadence and owner (IA9)"]}],
 "rows": [["decision", "row", "test"], ["owner", "dl", "review"]],
 "links": [
  {"from": "row", "to": "decision", "label": "records", "from_card": "1", "to_card": "1", "dir": "to"},
  {"from": "row", "to": "test", "label": "is settled by", "from_card": "0..*", "to_card": "1..*"},
  {"from": "row", "to": "owner", "label": "is owned by", "from_card": "0..*", "to_card": "1"},
  {"from": "row", "to": "dl", "label": "changes through", "from_card": "1..*", "to_card": "0..*"},
  {"from": "row", "to": "review", "label": "is read at", "from_card": "0..*", "to_card": "0..1"}]}
```

A row's test is one test even where the row names two: a log read at C1 raises the hypothesis, and the test with people settles it. IA11 asked that each register row "can cite one test" (IA11, "What later units take"); the register cites the settling test first and the log second.

### 3.3 · The evidence ladder, as the register uses it

The register does not define a ladder of its own. It holds each row at one of IA11's rungs, and the figure below draws those rungs in three columns: IA11's evidence, the proxy that reaches it alone (section 2), and the register's move with a row at that rung. Rows are tone 5, shared: the rungs serve every surface. A cell in tone 6 is a stop: no proxy evidence reaches this rung.

- **C0 Assumed.** Reasoning at a desk. Proxy that reaches it: competitors' screens, the existing structure, the data model, documentation, sales' notes, stakeholders' statements. The register's move: ship as a labelled default; name the test.
- **C1 Signal.** A log, ticket tags or paths, read once. Proxy that reaches it: search logs, ticket tags, analytics paths. The register's move: name the RV- review; record the hypothesis.
- **C2 Observed.** A small test with people. Proxy that reaches it: none: it needs people. The register's move: a usability round at FO-07.
- **C3 Measured.** A planned test from the right people, its interval clear of a mark set beforehand. Proxy that reaches it: none: it needs people. The register's move: settle a label, a placement or a cross-listing.
- **C4 Converging.** Two methods of different kinds that agree. Proxy that reaches it: ticket tags, only beside a test with people. The register's move: license a change to a top level.
- **C5 Confirmed in use.** Production records of the behaviour itself. Proxy that reaches it: analytics of the behaviour itself. The register's move: close the DL entry as applied and confirmed.

```viz
{"kind": "matrix", "caption": "Evidence ladder: IA11's rungs C0 to C5 as the assumption register uses them, with the proxy evidence that can reach each rung alone and what the register does with a row at that rung; supports the decision on how far proxy evidence can carry an IA decision when no user can be reached (section 3.3). Rungs and their evidence from IA11, section 6.4, cited by identifier; proxies and their limits from section 2 (Farrell, NN/g, 2017, and Chisnell 2016, through IA3 and IA9; Cardello, NN/g, 2013, through IA9; Bland and Osterwalder 2019, section 2.3, on opinions and facts); the register's moves from IA11, sections 6.1 and 7, and IA9, Deliverable C. Rows tone 5, shared; tone 6 a stop: no proxy evidence reaches this rung. Perqo is fictional.", "cols": ["IA11's evidence", "Proxy that reaches it", "The register's move"], "rows": [
 {"label": "C0", "tone": 5, "cells": ["reasoning at a desk", "competitors' screens, the existing structure, the data model, documentation, sales' notes, stakeholders' statements", "ship as a labelled default; name the test"]},
 {"label": "C1", "tone": 5, "cells": ["a log, ticket tags or paths, read once", "search logs, ticket tags, analytics paths", "name the RV- review; record the hypothesis"]},
 {"label": "C2", "tone": 5, "cells": ["a small test with people", {"mark": "none: it needs people", "tone": 6}, "a usability round at FO-07"]},
 {"label": "C3", "tone": 5, "cells": ["a planned test from the right people, its interval clear of a mark set beforehand", {"mark": "none: it needs people", "tone": 6}, "settle a label, a placement or a cross-listing"]},
 {"label": "C4", "tone": 5, "cells": ["two methods of different kinds that agree", "ticket tags, only beside a test with people", "license a change to a top level"]},
 {"label": "C5", "tone": 5, "cells": ["production records of the behaviour itself", "analytics of the behaviour itself", "close the DL entry as applied and confirmed"]}],
 "legend": [{"mark": "tone 5", "means": "shared: the rungs serve every surface", "tone": 5}, {"mark": "tone 6", "means": "a stop: no proxy evidence reaches this rung", "tone": 6}]}
```

Two things in the figure matter for practice. A team with no access to users can still reach C5 for the questions that are about frequency or use, because the record is the behaviour; IA7's sizing-client volumes and its landing pages are such questions (Deliverable B, AR-02 and AR-37). And no amount of proxy evidence reaches C2 or C3, the rungs where labels and placements are decided (IA11, section 6.4): a label chosen without people stays at C0 or C1 however many logs agree with it.

### 3.4 · What the register shows for Perqo Admin

Deliverable B fills the register for Perqo Admin: every structural decision of IA7, the rows of IA7 to IA11's tables that name this register and concern Admin, and IA8's open questions G-5 to G-7 (Perqo, fictional). Three findings come from filling it.

- **Every row stands at C0 on 10 November 2026.** No test with Admin's users has run, and no read of a log, a ticket tag or a path about Admin is on file. IA7's decisions rest on IA4's objects, on IA1's and IA2's structure, on NN/g guidance, on standards (NIST's definitions of least privilege, separation of duty and an audit trail) and on practice (Cooper, Prater, Evans), as IA7 cites them; on IA11's ladder all of that is "reasoning at a desk, from the literature and the domain", C0.
- **The forums where most tests would run have not met.** No meeting of FO-05, FO-07, FO-08 or FO-09 is on record since IA10 set them on 9 November 2026 (Perqo, fictional). By IA10's rule, each row whose test runs there is marked absent, with the TP- row and the forum named.
- **Most rows can rise without recruiting.** Of the 49 rows, 28 have a test or a first read in Admin's own records or support's tickets, read at RV-05 or RV-06 (counted from Deliverable B's "Read at" column); those can reach C1, and the frequency questions C5, as soon as the records are read.

This unit fills the Admin part of the register only. Table A.2 of IA11 also sends to the register eleven rows that do not concern Admin: IA8's tests of the trees' words for sales and of reading one layer alone (rows 15 and 16), IA9's process measures (17 to 19 and 21), and IA10's touchpoint and process rows (22 to 24). They stay where A.2 sends them, at C0, for the register's process part; so do IA8's one-year test of J- rows (IA8, section 6) and localisation's dormant row, TP-05, which IA11 holds at C0 with DD-IA3 named (IA11, section 7). The app's assumptions are not here because IA11's plan already holds them (V-01 to V-17).

## 4 · Stakeholders: mapping, interviewing and disagreement

### 4.1 · Power, interest and attitude

Rosala defines a stakeholder as "anyone who has interest in your project or with whom you need to work with in some way", and maps stakeholders on a power-interest matrix with four quadrants: high power and high interest, "These stakeholders need to be managed closely"; high power and low interest, keep them satisfied and consult them; low power and high interest, keep them informed, by inviting them to research, debriefs and design critiques; low power and low interest, "you should monitor them regularly", since their position may change (Rosala 2021; NN/g guidance). She adds what the matrix leaves out: "One component that is missing in the power and interest matrix is attitude", and on sceptics with power, "these are the stakeholders you should spend the most energy on converting"; and "stakeholder mapping is not a one-time activity" (Rosala 2021).

IA10 already placed one Perqo function: leadership in the keep-satisfied quadrant, "high power and low interest in the IA's detail", given one page (IA10, section 2.9). IA10 also read two placements from IA9's tables without plotting them: engineering, consulted on fifteen steps and owning none, has "the shape of a function that is managed closely", and sales, consulted on four and told of seven, sits in "the keep-informed quadrant" (IA10, section 5). Deliverable C places all twelve functions by a rule this unit sets: **power** is how far a function can decide or stop a change to the IA (signs off, decides a class of change, sits in the IA review, is consulted before a decision, or is told); **interest** is how much of the IA's detail it reads, from the fidelity IA10's matrix gives it (F3 high, F2 middling, F1 or words low), lowered for a touchpoint that is dormant. Attitude is recorded only where a position is on file.

### 4.2 · Interviewing a stakeholder

A stakeholder interview is how an answer is asked for before it is escalated. Dan Brown's practitioner article on it says "Someone is a stakeholder when they care about the outcome of your project", and builds the script around three lines of questioning: domain ("I go into these conversations with the posture that they're the domain experts"), audience, and constraints ("Stakeholders, with their unique vantages in the organization, can expose constraints"). Among his questions: "Describe the purpose of this project in your own words", "What's the most important thing for us to get right?" and "How will you know if this is successful?" He treats organisational norms as "in need of validation", and the output as "raw materials for the design process"; he reports Erika Hall saying "the stakeholder conversations are the most important ones we have on any project" ("The Delicate Art of Interviewing Stakeholders", EightShapes on Medium, 11 July 2018, [medium.com, interviewing stakeholders](https://medium.com/eightshapes-llc/the-delicate-art-of-interviewing-stakeholders-d6496443cbec); practice). Hall's book gives organisational research its own chapter, "Organizational Research", in both editions (*Just Enough Research*, 2nd ed., A Book Apart, 2019, ch. 4, contents, [oreilly.com, 2nd ed.](https://www.oreilly.com/library/view/just-enough-research/9781492018032/); 1st ed., 2013, ch. 4); only its contents and the first edition's opening were seen for this unit.

For an IA, on this unit's reading, the constraints line matters most: the stakeholder knows the rule, the contract or the system limit that decides a structural question. Bland and Osterwalder's distinction applies to the answers: "In that situation I usually _____" is a fact about practice, "I think _____ is important" an opinion (Bland and Osterwalder 2019, section 2.3). The register records which it was, under the evidence's kind.

### 4.3 · Working with disagreement

IA10 gave disagreement a place in the record. DL-011, proposed, adds a positions field to the decision log: "For each function that disagrees with a proposed change, the entry records the function, its position in one line, its reason, and the evidence that would reopen the decision; the decision's reason must answer each position", and the disagreement runs through IA9's routing rule unchanged (IA10, section 4.2). Brown's position, which IA10 cites, is that conflict is part of design work, with healthy and unhealthy kinds (Brown 2013, ch. 4, contents; practice). Rosala's advice on sceptics with power is to spend energy on converting them (Rosala 2021).

Three positions are on file at Perqo, and none of them puts a test with people into the Admin register (Perqo, fictional). The partnerships team's request for offers on Home and in Benefits concerns the app, and its reopening test is already in IA11's plan, V-06 and V-17 (IA6, B.6; IA11, A.1). Legal's and product management's positions on DL-015 concern who may open a claim's receipt in Admin; the question they divide on goes to FO-08 and then to the IA review (IA10, section 4.3), and no test with people is named for it, so the register records the row (AR-22) with legal as owner and FO-08 as the absent input. The partnerships team is not one of IA10's twelve functions; Deliverable C keeps the twelve and notes it.

The client rule is the other guard against one stakeholder's view becoming the structure: "a client's structure enters as data, its words enter as variants, and a request to mirror its approval chain enters as a decision log entry" (IA10, section 2.7, after McCloskey's finding that department-organised intranets had to change at every reorganisation; McCloskey, NN/g, 2014, as cited in IA10). A client is a powerful stakeholder; its power reaches the IA through the log, where its position sits beside the others.

### 4.4 · When the owner of the answer will not give it

The hardest case is the one the register cannot route around: a structural question whose answer belongs to one function, which does not give it. No source read for this unit measures what works here. The procedure below is this unit's practice, built from IA9's change control and IA10's positions field, and from Rosala's and Brown's advice as practice:

1. **Name the owner.** Use the stakeholder map to say who owns the answer and in which forum it is decided (Deliverable C; IA9, D.1). A question with no owner is assigned one in the register first.
2. **Ask once, in the owner's format.** IA10's rule is that the format follows the quadrant: the artefact for those managed closely, one page for those kept satisfied, the decisions for those kept informed (IA10, section 1.4). Ask with the options and what each would change, by identifier.
3. **Write the question as a proposed DL entry with a default.** The default is the option cheapest to reverse: build nothing that assumes the answer (section 5). The entry names the forum and the meeting at which the default will be decided if no answer has come.
4. **Ship the default, labelled.** The register row stays at its rung, the artefact's note says "assumed" (IA2, section 5.2), and the release note says what is not decided (IA9, W-14). IA9's gate does not block this: an artefact is done when "every assumption is marked 'assumed' with the test that would settle it" (IA9, Deliverable B, item 3), so marking, not evidence, is what the gate checks.
5. **At the named meeting, decide by the routing rule.** The decider IA9's D.1 names decides the default; the owner's silence is recorded under positions as "not given", so a later answer starts from the record (IA10, section 4.2).
6. **Show the risk where the owner reads.** For leadership, that is the one-page map at FO-09 (DL-019, proposed).

At Perqo the worked case is G-7, money unspent at a period's end (Perqo, fictional). Its answer is a commercial term of the contract, which IA8 left free: "Whether the client's contract treats unspent money otherwise is left free, with G-7" (IA8, section 3.4); BR-3 already tells sales it is "not yet decided" (IA10, BR-3). The register gives the row to product management, with the answer owed by leadership and legal (Deliverable B, AR-49), and DL-018 writes the default: no surface says what happens to money left at a period's end, and Budget use reports it as unspent for its period, as IA8 set for a leaver's remainder (IA8, section 3.4).

## 5 · The minimum viable IA: what to fix early and what can stay open

An IA built without its inputs still has to be built, because engineering builds from it (IA9, Deliverable B, the gate). The question is which parts to fix now. This unit's criterion has two halves, each drawn from a filed rule. First, IA9's version rule says which changes break what others rely on: "A new version when an accepted change would break a citation: an identifier retired or moved to another parent, a label renamed, a relationship or transition removed, a rule's outcome changed", and a dated amendment for a change that "adds without breaking" (IA9, section 4.4). Second, the cost of a break grows with what depends on the element: the model, the permissions, the addresses outside the product, the words in support's and sales' mouths. A part that would break many citations if changed is the **backbone**, fixed early and tested first; a part that changes by adding is **open**.

Five parts are backbone, each for a reason a source gives:

- **Objects.** An object is a table, a model name and the noun every surface uses. Evans: "Recognize that a change in the language is a change to the model" (Evans, *Domain-Driven Design Reference*, 2015, as cited in IA7, section 6.2).
- **Roles.** Permissions are written once, on the calls to action, and both the role matrix and the access-control configuration are read from them; the client signs off what each role can do and security builds it (IA7, section 6.3).
- **Top-level structure.** IA9's structure test runs before and after any change to a top level or a tab (IA9, RV-11), and McCloskey found that intranets structured like the organisation had to change their navigation whenever the institution reorganised (McCloskey 2014, as cited in IA10, section 2.7).
- **Addresses.** Tim Berners-Lee: "A cool URI is one which does not change", and "URIs don't change: people change them"; designing an address to last mostly means leaving information out of it, so that nothing in it has a reason to change ("Cool URIs don't change", W3C Style, 1998, [w3.org, cool URIs](https://w3.org/Provider/Style/URI); standards documentation, an essay by the web's inventor). Perqo already puts the identifier first and keeps a redirect for a moved page (IA4, section 5; IA7, C.1).
- **The shared vocabulary.** A rename goes through the vocabulary first, with the old term kept as a variant, because support and search still meet the old word (IA2, section 4).

Everything else can stay open, provided its row in the register says so: lower-level labels (a rename is a new version, but it touches one surface), list orders and filters, landing pages, queue thresholds, which reports exist, bulk actions, and whether search is added. Each of these at Perqo Admin changes by adding or by a setting, and each has a test in the register that can be read from Admin's own records (Deliverable B).

The figure gives each part three columns: fix or open, what a late change costs, and where it is at Perqo Admin. Objects: fix; a late change costs the model, every surface's noun; at Perqo Admin, IA4's objects and O-17; AR-01, AR-12 to AR-14. Roles: fix; access configuration; the client's sign-off; HR, finance, account owner; AR-16, AR-17, AR-22, AR-23. Top level: fix; a test before and after (RV-11); six areas; AR-24. Addresses: fix; links from outside; redirects; identifier first; AR-36. Vocabulary: fix; support's and search's words; Budget, Claim, Employee group; AR-01, AR-14. Lower labels: open; one surface's screens; form names; AR-31. Lists: open; a setting; orders, filters, find; AR-30, AR-34. Queues: open; a threshold or a view; 14 days, five working days; AR-28, AR-41. Landing: open; a setting; Approvals, Budgets; AR-37. Reports: open; a view added; five views; AR-35. Rows are tone 5, shared; the Perqo Admin column is tone 4.

```viz
{"kind": "matrix", "caption": "Minimum viable IA: which parts of an IA to fix early because a late change breaks what depends on them, and which can stay open, with where each sits in Perqo Admin; supports the decision on what to build before the evidence arrives (section 5). Criterion from IA9, section 4.4 (what breaks a citation) and the dependents named in section 5: objects from Evans, Domain-Driven Design Reference, 2015, through IA7, section 6.2; roles from IA7, section 6.3; top level from IA9, RV-11, and McCloskey, NN/g, 2014, through IA10; addresses from Berners-Lee, W3C, 1998, and IA4, section 5; vocabulary from IA2, section 4. Register rows from Deliverable B. Rows tone 5, shared; the Perqo Admin column tone 4. Perqo is fictional.", "cols": ["Fix or open", "A late change costs", "At Perqo Admin"], "rows": [
 {"label": "Objects", "tone": 5, "cells": ["fix", "the model, every surface's noun", {"mark": "IA4's objects and O-17; AR-01, AR-12 to AR-14", "tone": 4}]},
 {"label": "Roles", "tone": 5, "cells": ["fix", "access configuration; the client's sign-off", {"mark": "HR, finance, account owner; AR-16, AR-17, AR-22, AR-23", "tone": 4}]},
 {"label": "Top level", "tone": 5, "cells": ["fix", "a test before and after (RV-11)", {"mark": "six areas; AR-24", "tone": 4}]},
 {"label": "Addresses", "tone": 5, "cells": ["fix", "links from outside; redirects", {"mark": "identifier first; AR-36", "tone": 4}]},
 {"label": "Vocabulary", "tone": 5, "cells": ["fix", "support's and search's words", {"mark": "Budget, Claim, Employee group; AR-01, AR-14", "tone": 4}]},
 {"label": "Lower labels", "tone": 5, "cells": ["open", "one surface's screens", {"mark": "form names; AR-31", "tone": 4}]},
 {"label": "Lists", "tone": 5, "cells": ["open", "a setting", {"mark": "orders, filters, find; AR-30, AR-34", "tone": 4}]},
 {"label": "Queues", "tone": 5, "cells": ["open", "a threshold or a view", {"mark": "14 days, five working days; AR-28, AR-41", "tone": 4}]},
 {"label": "Landing", "tone": 5, "cells": ["open", "a setting", {"mark": "Approvals, Budgets; AR-37", "tone": 4}]},
 {"label": "Reports", "tone": 5, "cells": ["open", "a view added", {"mark": "five views; AR-35", "tone": 4}]}]}
```

Bland and Osterwalder's top-right quadrant, important and without evidence, is therefore the backbone rows at C0. In Admin's register that is 25 rows (counted from Deliverable B's "Fix" column), every one at C0, and they are where the first FO-07 session should start.

## 6 · Escalation, the decision log and visible risk

A decision taken without its inputs is still a decision, and IA9's log is where it is kept. Its form comes from software architecture: Martin Fowler describes the architecture decision record as "a short document that captures and explains a single decision", with a status, and once accepted, a record "should not be modified if the decision is changed, but linked to a superseding decision" (Fowler, "Architecture Decision Record", martinfowler.com, 2026, as cited in IA9, section 4.3; practice). IA9 gave each Perqo entry its fields and five statuses, and IA10 proposed two more fields, positions (DL-011) and the forum and date on the told line (DL-012). Deliverable D is the one-page template that holds them, with DL-017 proposing a field that joins each entry to the register rows it rests on.

Escalation, at Perqo, adds no decider. IA9's routing rule already sends a change to the IA designer, the IA review, product management's sign-off or the content team (IA9, D.1); what this unit adds is the date. An entry raised for a missing answer names the meeting at which its default will be decided, and the meeting is a forum that already exists: FO-01 for a two-surface change, FO-09 for leadership (IA10, A.2).

Making the risk visible without blocking the team is three practices, each on an existing document (this unit's practice, Perqo, fictional):

- **On the artefact.** Every backbone element at C0 carries "assumed" in its note, as IA2's rule asks (IA2, section 5.2), and the face's leaves-out line names what is open.
- **In the release note.** A release that ships a default names it and its DL entry, as IA9's W-14 already lists IA changes in the release note.
- **On the leadership page.** The one-page map at FO-09 shows the register's count of rows by rung and by input, and each open question with its owner and the date its default was set (DL-019, proposed). A count is the form leadership reads: one page, F1 (IA10, section 2.9).

None of the three stops a story. IA9's gate checks that the artefact is at F3 and that its assumptions are marked (IA9, Deliverable B), and a marked assumption passes.

## 7 · Keeping the backbone revisable: the loop to IA9 and IA11

A register is worth keeping only if rows leave it. IA9 set the loop: W-09, "Test the candidates and label what is untested", outputs "test plans and results (IA11); assumptions with their tests (IA12's register)", and W-17, "Hand the next cycle its inputs", sends "hypotheses to IA11's tests; assumptions to IA12's register" (IA9, Deliverable A). IA11 set what a result does: a pass removes "assumed" and cites the plan row and date; a fail proposes a DL entry; an undecided result changes nothing and leaves the row with the result attached (IA11, section 6.1). And IA11 hands this unit "section 7's rule that a test not run leaves its row in place, marked not run, with the assumption at its current rung" (IA11, "What later units take").

The loop, step by step (this unit's practice, on IA9's and IA11's rules; Perqo, fictional):

1. **Record the row**: decision, evidence and its kind, rung, test, owner.
2. **Ship at its rung**: labelled assumed on the artefact's face.
3. **Read at its review**: RV-04, RV-05 or RV-06: a hypothesis at C1.
4. **Run the test**: [not run] the row stays, marked not run.
5. **Read the verdict**: pass, fail or undecided (IA11, 6.1).
6. **Log the change**: a DL entry; the change-control flow → see IA9, D.2.
7. **Re-stamp the face**: amendment or new version (IA9, 4.4).

```viz
{"kind": "flow", "per_row": 2, "caption": "The register's loop: how an assumption recorded at its rung is read, tested, decided and closed; supports the decision on what happens to a register row between cycles (section 7). Steps set in section 7 on IA9, W-09 and W-17, RV-04 to RV-06, Deliverable D, D.2 and section 4.4 (the version rule), and IA11, sections 6.1 and 7 (verdicts; a test not run leaves its row at its rung). The flow kind draws no branch, so the test not run is a bracketed condition in the fourth step's note. Every step tone 5, shared. Perqo is fictional.",
 "steps": [
  {"label": "Record the row", "note": "decision, evidence and its kind, rung, test, owner", "tone": 5},
  {"label": "Ship at its rung", "note": "labelled assumed on the artefact's face", "tone": 5},
  {"label": "Read at its review", "note": "RV-04, RV-05 or RV-06: a hypothesis at C1", "tone": 5},
  {"label": "Run the test", "note": "[not run] the row stays, marked not run", "tone": 5},
  {"label": "Read the verdict", "note": "pass, fail or undecided (IA11, 6.1)", "tone": 5},
  {"label": "Log the change", "note": "a DL entry; the change-control flow → see IA9, D.2", "tone": 5},
  {"label": "Re-stamp the face", "note": "amendment or new version (IA9, 4.4)", "tone": 5}]}
```

Two rules keep the backbone revisable while it waits. A backbone row changes only through the log, so an object, a role, a top-level area or an address is never changed in a sprint because a test came back (IA9, section 4.2). And a row whose test passes is closed in the register and in the artefact's note at once, citing the plan row and its date (IA11, section 6.1), so the register never holds a decision the artefact has already confirmed.

## Deliverable · A · The triage decision tree

*Face of this artefact (IA2, the notation sheet): triage decision tree for an IA decision taken with an input missing, with a table of the four shortages, their symptoms, the proxy evidence for each and the move; fidelity F2 (complete for its scope; every outcome named). Decision: which shortage a structural decision faces, and what to do about it before building. Readers: the IA designer, product management, and any function asked for an answer. Leaves out: the methods of each test (IA11), the stakeholders' placements (Deliverable C), the register itself (Deliverable B). Owner: the IA designer; version 1, dated 10 November 2026; the order of the questions and the symptoms are this unit's synthesis, assumed until tested; Perqo is fictional.*

### A.1 · The shortages, their symptoms and the move

| Shortage | Symptoms (section 1) | Proxy evidence (section 2) | The move |
|---|---|---|---|
| Shifting requirements | two documents state different rules; scope signed before the structure is drawn; a requirement changes between meeting and minutes | the decision log's history; documentation, at C0 | Shifting requirements: fix the backbone only, log each version |
| Stakeholder shortage | decisions reopened; a delegate who cannot decide; opposite answers from two functions; a question open across cycles | sales' notes and stakeholders' statements, at C0, labelled opinion or fact | Stakeholder shortage: write a default as a DL entry, escalate |
| Content shortage | placeholder text in wireframes; no owner per page; articles that contradict the product; a document for another audience | the existing structure, the data model, documentation, at C0 | Content shortage: structure from the objects and the data model; audit |
| Research shortage | claims about users with no source; workshop personas; the organisation's words in the labels; colleagues standing in for users | search logs, ticket tags, analytics paths, at C1; analytics of the behaviour itself, at C5 | Test it (IA11), or read the record, or hold at C0 labelled assumed |

### A.2 · The tree

Run the tree once for each structural decision. The questions are asked in the order of what each shortage blocks: a moving requirement makes any test wasted, a missing owner's answer may make a test unnecessary, missing content leaves nothing to test labels against, and only then does research decide (this unit's ordering). The questions: "Do the requirements for it hold still?"; "Has the owner of the answer given it?"; "Is the content it organises there, and trusted?"; "Can you test it with the people it is for?"; "Is there a record of use: a log, tickets, paths?". The outcomes: "Shifting requirements: fix the backbone only, log each version"; "Stakeholder shortage: write a default as a DL entry, escalate"; "Content shortage: structure from the objects and the data model; audit"; "Test it (IA11); record the rung reached"; "Read it at its RV- review; hold at C1"; "Hold at C0, labelled assumed; name the test". Every box is tone 5, shared, because the tree serves any surface.

```viz
{"kind": "decision", "caption": "Decision tree: triage of one structural decision taken with an input missing, from the four shortages to the move for each; supports the decision on what to do before building a part of the IA whose inputs are missing (Deliverable A, A.2). Shortages and symptoms from section 1; proxies and their rungs from section 2 and IA11, section 6.4; the moves from sections 3 to 6 (the register after Bland and Osterwalder, Testing Business Ideas, 2019; escalation on IA9, D.1, and IA10, section 4.2; the backbone from section 5); the order of the questions is this unit's. Every box tone 5, shared. Perqo is fictional.",
 "root": {"q": "Do the requirements for it hold still?", "tone": 5, "branches": [
  {"label": "yes", "to": {"q": "Has the owner of the answer given it?", "tone": 5, "branches": [
   {"label": "yes", "to": {"q": "Is the content it organises there, and trusted?", "tone": 5, "branches": [
    {"label": "yes", "to": {"q": "Can you test it with the people it is for?", "tone": 5, "branches": [
     {"label": "yes", "to": {"outcome": "Test it (IA11); record the rung reached", "tone": 5}},
     {"label": "no", "to": {"q": "Is there a record of use: a log, tickets, paths?", "tone": 5, "branches": [
      {"label": "yes", "to": {"outcome": "Read it at its RV- review; hold at C1", "tone": 5}},
      {"label": "no", "to": {"outcome": "Hold at C0, labelled assumed; name the test", "tone": 5}}]}}]}},
    {"label": "no", "to": {"outcome": "Content shortage: structure from the objects and the data model; audit", "tone": 5}}]}},
   {"label": "no", "to": {"outcome": "Stakeholder shortage: write a default as a DL entry, escalate", "tone": 5}}]}},
  {"label": "no", "to": {"outcome": "Shifting requirements: fix the backbone only, log each version", "tone": 5}}]}}
```

### A.3 · Each move, in full

- **Shifting requirements: fix the backbone only, log each version.** Build the five backbone parts of section 5 for what is stable, leave the moving part open, and write each version of the requirement as a DL entry so the history is on record (IA9, section 4.3). A backbone part that the moving requirement touches is held as a proposed entry, never built.
- **Stakeholder shortage: write a default as a DL entry, escalate.** Run section 4.4's six steps: name the owner, ask once in their format, write the default, ship it labelled, decide at the named meeting, show the risk.
- **Content shortage: structure from the objects and the data model; audit.** Draw the objects and their relationships from the data model and the existing structure, each labelled proxy (section 2), and inventory what content exists with an owner per item before any label is chosen (IA2, section 1.1; IA5, Deliverable A).
- **Test it (IA11); record the rung reached.** Choose the method by the question (IA11, section 2.7) and record the verdict and rung in the register.
- **Read it at its RV- review; hold at C1.** The read raises a hypothesis; the row names the test that would settle it (IA9, section 6.4).
- **Hold at C0, labelled assumed; name the test.** The row ships as a labelled default (IA11, section 6.4, C0).

A decision can meet more than one shortage. The tree stops at the first, because its move comes first; once that move is made, the tree is run again.

## Deliverable · B · The assumption register for Perqo Admin

*Face of this artefact (IA2, the notation sheet): assumption register for Perqo Admin, one row per structural decision of IA7 and per row of IA7 to IA11's tables that names this register and concerns Admin, with IA8's open questions G-5 to G-7; fidelity F2 (complete for its scope; every row an identifier, AR-01 to AR-49). Decision: on what evidence each part of Admin's IA stands, at which rung of IA11's ladder, what test would settle it, who owns that test, which review reads it, and which input is absent. Readers: the IA designer, product management, engineering, support, customer success, legal, security; leadership through the count on the one-page map (DL-019, proposed). Leaves out: the app's assumptions (IA11's plan, V-01 to V-17), perqo.com's, the process rows of IA11's A.2 (section 3.4), every result (none has run). Owner: the IA designer; version 1, dated 10 November 2026; every row is at C0 and not run at this date; Perqo is fictional.*

**How the rows were counted.** IA7 does not number its decisions. A row here is one decision IA7 states about Perqo Admin that could be reversed on its own, taken from IA7's sections 2 to 6 and its Deliverables A to D (the object-relationship map, the role-by-section matrix, the navigation model and the claim-approval state diagram). Where a deliverable's table repeats a section's decision, as A.4's calls to action and B.1's cells repeat the role decisions of section 3, the decision is counted once, under the section that took it, and the row cites both places. Four kinds of statement in IA7 are not counted, because they decide how the course's artefacts are drawn, or argue, and set nothing in Admin: the four columns added to the object map (section 2.1), the role-by-section matrix's entry in IA2's catalogue (section 3.5), the test for which objects get a state diagram and the table that applies it (section 5.1), and the posture argument (section 1.2); and of section 6.3's four practices, three are process, which IA9's change control holds, and the fourth, permissions written once, is counted (AR-17). The count: **42 rows from IA7, AR-01 to AR-42**: 15 for objects, attributes and the model (B.1), 8 for roles (B.2), 16 for navigation (B.3) and 3 for lifecycles (B.4). Forty-one are decisions; one, AR-02, the sizing client's volumes, is the assumption IA7's own table lists first. **Four rows from other units' tables, AR-43 to AR-46** (B.5), and **three open questions, AR-47 to AR-49** (B.6). **Total: 49 rows.**

IA7's assumption table, all nine rows, is in the register: volumes (AR-02), landing (AR-37), in-list find (AR-34), objects and names (AR-01), finance and Approvals (AR-19), HR and card payments (AR-21), the account owner (AR-04), list and detail (AR-29), the sign-in line (AR-39). Of IA11's table A.2, the rows that concern Admin are taken: rows 1 to 9 (IA7's nine), 12 (AR-43), 13 (AR-44), 14 (AR-47, G-5), 20 for Admin's half (AR-45) and 25 (AR-46). Rows 10 and 11 are app rows in IA11's plan (V-11, V-16); rows 15 to 19 and 21 to 24 do not concern Admin (section 3.4). IA6's assumption table is wholly the app's and in IA11's plan. IA8's G-5, G-6 and G-7 all touch Admin: G-5 at IA7's EX-4, G-6 at move to group, G-7 at Budget use (IA8, sections 1 and 3.4). DL-015, open, is carried by AR-22.

Columns: **Evidence** labels each item's kind; "proxy:" marks proxy evidence, as IA3, section 5.2 does. **Rung** is IA11's (section 6.4). **Test** names a V- row or the IA11 section that specifies the method, and A.2's row where A.2 routes it. **Owner** is a function of IA10's, or the IA designer (IA9, section 4.1). **Read at** names the RV- review for a test that is a log, a ticket tag or a path, and "none" otherwise. **Input** is "records kept" where Admin's own records serve (IA9, section 6.3), or "absent" with the TP- row and forum. **Fix** is section 5's. Every row's status is "not run, C0" at 10 November 2026, and is not repeated per row (Perqo, fictional).

### B.1 · Objects, attributes and the model (IA7, sections 2 and 6; Deliverable A)

| ID | Decision (IA7) | Evidence (kind) | Rung | Test | Owner | Read at | Input | Fix |
|---|---|---|---|---|---|---|---|---|
| AR-01 | Admin's objects are IA4's, labels and identifiers kept; its labels are the client's own words: employee group, policy, budget, claim (1.3, 2.2; A.1) | IA4's object map, a filed decision built by Prater's method (practice); no admin user consulted | C0 | hybrid card sort with admin users from at least two clients at FO-07 (IA11, 2.1; A.2 row 4) | IA designer | RV-04, for the words in the HR and finance log | absent: TP-09 Clients, FO-07 not met | backbone |
| AR-02 | The sizing client's volumes: 1,200 employees, 14 groups, about 1,200 claims and 9,600 card payments a month, 15% of claims over the limit (2.2; A.1) | assumed, derived from IA6's assumed frequencies | C0 | analytics on live clients (IA11, 2.5; A.2 row 1); can reach C5 | product management | RV-06 | records kept | open |
| AR-03 | Employee status Invited, Active, Left, with its lifecycle; Left an end state (2.2, 5.1; A.1, A.2) | filed decisions: IA6's Join (E-2), IA8's leaver rules; reasoning | C0 | usability test with HR managers of invite, resend and mark as left (IA11, 2.6) at FO-07; tickets tagged AD-1 and AD-1.4 as C1 | IA designer | RV-05 | absent: TP-09 Clients, FO-07 not met | backbone |
| AR-04 | One account owner per client, a power beside a role, with its powers; Company read only for every other admin user (2.2, 3.4; A.1, A.4; B.1) | standards: least privilege and separation of duty (NIST glossary); reasoning | C0 | interviews at onboarding, FO-05 (A.2 row 7; none of IA11's methods) | customer success | none | absent: TP-07 Customer success, FO-05 not met | backbone |
| AR-05 | Admin user status Active, Removed; a removed admin user's name stays on their decisions and changes (2.2, 5.3; A.2) | standard: NIST's definition of an audit trail | C0 | legal's reading of what the record keeps at FO-08; none of IA11's methods | legal | none | absent: TP-10 Legal, FO-08 not met | backbone |
| AR-06 | Claim attributes decided by and rejection note; a rejection needs a note (2.2; A.2; D.1) | filed decision: IA6's rejection reason; reasoning | C0 | usability test of a run of ten decisions, rejections included (IA11, 2.6; A.2 row 8); tickets on rejected claims tagged A-3.4 as C1 | IA designer | RV-05 | absent: TP-09 Clients, FO-07 not met | backbone |
| AR-07 | The audit entry, O-17, shown as History on each detail page and as the Activity log (2.2, 5.3; A.1) | standard: NIST's definition of an audit trail | C0 | review at FO-08 (TP-10, TP-11); page views of AD-6.3 and History (IA11, 2.5) | legal | RV-06 | absent: TP-10 Legal, FO-08 not met | backbone |
| AR-08 | R-21: an admin user is also an employee, matched by work email (2.2; A.3) | proxy: the data model; reasoning | C0 | records: share of admin users matched to an employee record (IA11, 2.5) | engineering | RV-06 | records kept | backbone |
| AR-09 | R-22 to R-24: a claim is decided by an admin user; an audit entry records a change and is made by an admin user (2.2; A.3) | reasoning from AR-06 and AR-07 | C0 | engineering confirms at FO-02, the story check; none of IA11's methods | engineering | none | records kept | backbone |
| AR-10 | Admin shows the card as "Perqo card", status only; last four digits not shown; Admin cannot change it (2.3; A.1; DL-003) | filed decision: IA6's decline rules; standard: least privilege (NIST) | C0 | interviews with HR managers at FO-07 (IA11, 2.6); tickets where a card question reaches HR, tagged AD-1.1, as C1 | support | RV-05 | absent: TP-09 Clients, FO-07 not met | open |
| AR-11 | Admin does not show notifications (2.3; DL-003) | reasoning | C0 | tickets where HR could not say what an employee was told, tagged AD-1.1 (IA11, 2.4 for the reading); G-5's interviews | support | RV-05 | records kept | open |
| AR-12 | The model names of objects and attributes as A.2 gives them; `closed` and `contract_end_date` proposed for engineering (A.2; 6.3; IA9, D.3) | practice: Evans's ubiquitous language | C0 | engineering confirms each name at FO-01; none of IA11's methods | engineering | none | records kept | backbone |
| AR-13 | One transaction table shown as two objects, Claim and Card payment; remaining computed; reports and queues views with no table (6.1) | proxy: the data model (IA1, 2.4), read against Cooper's implementation model (practice) | C0 | AR-01's hybrid sort with claim and card payment as separate cards (IA11, 2.1) | IA designer | none | absent: TP-09 Clients, FO-07 not met | backbone |
| AR-14 | Admin and the app one bounded context; Admin keeps the label Budget, the model `allocation` (6.2; DL-009) | practice: Evans | C0 | AR-01's sort for the label Budget; engineering's decision on contexts at FO-01 | engineering | none | absent: TP-09 Clients, FO-07 not met | backbone |
| AR-15 | A waiting claim reserves nothing; HR's approval checks the balance again, T5 (5.2; A.2; D.1, D.2, EX-2) | filed decision: IA6's check at submit; reasoning | C0 | records: T5 rejections a month (IA11, 2.5); tickets on claims rejected after waiting, tagged DT-2, as C1 | product management | RV-06 | records kept | backbone |

### B.2 · Roles (IA7, section 3; Deliverable B)

| ID | Decision (IA7) | Evidence (kind) | Rung | Test | Owner | Read at | Input | Fix |
|---|---|---|---|---|---|---|---|---|
| AR-16 | Three roles, HR manager, finance manager and account owner; every role covers the whole client; scoping by group left free (3.2, 3.4; B.1) | standard: RBAC (Ferraiolo and others 2001; NIST's FAQ) | C0 | interviews with account owners at FO-05; requests for line-manager approval logged per client (IA10, 2.7) | customer success | none | absent: TP-07 Customer success, FO-05 not met | backbone |
| AR-17 | Permissions written once, on the calls to action; the matrix and the access configuration read from them (3.1, 6.3; A.4) | standard: RBAC; reasoning | C0 | security compares the access configuration with A.4 at FO-08; none of IA11's methods | security | none | absent: TP-11 Security, FO-08 not met | backbone |
| AR-18 | A route a role can never use is hidden; an action it cannot take now is disabled with the reason; what it may see but not change is read only (3.2; B.2) | filed rule: IA6, 4.4; reasoning | C0 | usability test with HR and finance managers (IA11, 2.6) at FO-07; tickets of a missing button, tagged AD-, as C1 | IA designer | RV-05 | absent: TP-09 Clients, FO-07 not met | open |
| AR-19 | Approvals is not in the finance manager's navigation; finance reads waiting claims in Claims by status (3.2; B.1) | standard: least privilege (NIST); reasoning | C0 | interviews with finance managers (A.2 row 5; none of IA11's methods) at FO-07 | IA designer | none | absent: TP-09 Clients, FO-07 not met | open |
| AR-20 | Finance sees Employees and Policies read only; HR sees Budgets read only (3.2; B.1, B.2) | reasoning from R-06 | C0 | interviews with HR and finance managers at FO-07 | IA designer | none | absent: TP-09 Clients, FO-07 not met | open |
| AR-21 | HR sees Budget use and Claims by status, and not Card payments or the two spend reports (3.3, 4.6; B.1) | standard: least privilege (NIST) | C0 | interviews with HR managers; tickets as C1 (A.2 row 6; IA11, 2.4 for the reading) | IA designer | RV-05 | absent: TP-09 Clients, FO-07 not met | open |
| AR-22 | Every role sees a claim, its receipt included (A.1, O-07; A.2); DL-015 proposes otherwise | none recorded; positions of legal and product management on DL-015 (IA10, 4.3) | C0 | none of IA11's methods: a legal reading at FO-08, then the IA review decides DL-015 | legal | none | absent: TP-10 Legal, FO-08 not met | backbone |
| AR-23 | An HR manager cannot decide their own claim; every client has at least two HR managers (3.3; A.3, R-01; D.2, EX-1) | standard: separation of duty (NIST) | C0 | records at onboarding: clients set up with fewer than two HR managers, at FO-05; tickets on own-claim waits as C1 | customer success | RV-05 | absent: TP-07 Customer success, FO-05 not met | backbone |

### B.3 · Navigation (IA7, section 4; Deliverable C)

| ID | Decision (IA7) | Evidence (kind) | Rung | Test | Owner | Read at | Input | Fix |
|---|---|---|---|---|---|---|---|---|
| AR-24 | Six areas in IA1's order, none added or renamed, each an object area, a queue, views or setup (4.1; C.1, C.2) | proxy: the existing structure (IA1's surfaces map); NN/g guidance (Kaplan 2020; Laubheimer 2022) | C0 | tree test of Admin's structure with admin users from at least two clients (IA11, 2.2) at FO-07 | IA designer | none | absent: TP-09 Clients, FO-07 not met | backbone |
| AR-25 | Approvals shows the count of claims waiting for the viewer (4.1; C.2) | reasoning | C0 | usability test (IA11, 2.6) at FO-07 | IA designer | none | absent: TP-09 Clients, FO-07 not met | open |
| AR-26 | Contextual routes from the relationships, one for one (4.1; C.2) | practice: Prater | C0 | analytics: routes followed between AD- pages (IA11, 2.5) | product management | RV-06 | records kept | open |
| AR-27 | Every object type has a list and a detail; a detail has one place, a claim under its employee, and many routes (4.2; C.1) | NN/g guidance (Laubheimer 2022); filed rule: IA4's database structure | C0 | AR-24's tree test, with tasks to find a claim from Approvals and from the employee (IA11, 2.2) | IA designer | none | absent: TP-09 Clients, FO-07 not met | backbone |
| AR-28 | Work queues Approvals, Not joined after 14 days, and No budget for next period (4.2; C.4) | NN/g guidance (Laubheimer 2022); reasoning | C0 | analytics: time to clear each queue (IA11, 2.5) | product management | RV-06 | records kept | open |
| AR-29 | A detail opens beside its list; one at a time in a narrow window; Admin used in a desktop browser, assumed (4.3) | NN/g guidance (Laubheimer 2022); platform documentation (Android) | C0 | usability test of a run of ten decisions (A.2 row 8; IA11, 2.6) at FO-07 | IA designer | none | absent: TP-09 Clients, FO-07 not met | open |
| AR-30 | Each list's default order, filters and find field, as C.3 gives them (4.3; C.3) | filed rule: IA4's ordering; NN/g guidance | C0 | analytics: filter and sort use per list (IA11, 2.5) | product management | RV-06 | records kept | open |
| AR-31 | Create and edit forms named by their verb; a create ends on the new object's detail (4.3) | reasoning; practice: Cooper's intermediates | C0 | usability test (IA11, 2.6) at FO-07 | IA designer | none | absent: TP-09 Clients, FO-07 not met | open |
| AR-32 | A policy change applies to claims submitted after it (4.3) | reasoning | C0 | tickets on claims routed against a new policy, tagged DT-2, as C1 (IA11, 2.4 for the reading); RV-12 on the next policy option | product management | RV-05 | records kept | backbone |
| AR-33 | Bulk actions approve selected, move to group and resend invitation; rejection one at a time (4.4) | NN/g guidance (Laubheimer 2022) | C0 | analytics: share of approvals made by Approve selected (IA11, 2.5) | product management | RV-06 | records kept | open |
| AR-34 | No search across Admin; a find field on each long list (4.5) | practice: Spencer 2006; AR-02's assumed volumes | C0 | usability test with HR managers at FO-07: find this employee, find this claim from a support question (A.2 row 3; IA11, 2.6) | IA designer | none | absent: TP-09 Clients, FO-07 not met | open |
| AR-35 | Reports holds five views, each row a route to the records it sums (4.6) | filed rule: IA4's reports as views | C0 | analytics: views of AD-5.1 to AD-5.5 (IA11, 2.5) | product management | RV-06 | records kept | open |
| AR-36 | Pages AD-0 to AD-6 with their local routes; addresses identifier first; a redirect for a moved page (C.1, C.2) | filed rule: IA4's addresses; Berners-Lee 1998 | C0 | records: requests to retired addresses (IA11, 2.5); engineering confirms at FO-02 | engineering | RV-06 | records kept | backbone |
| AR-37 | HR lands on Approvals, finance on Budgets (C.2) | reasoning on assumed frequency (IA4, A.3) | C0 | analytics, first actions after sign-in (A.2 row 2; IA11, 2.5); can reach C5 | product management | RV-06 | records kept | open |
| AR-38 | HR invites from Invite employees, AD-1.3; the email carries the client's name and the Join link; resend sends it again; inviting waits for the group's budgets (5.1; C.4; DL-007) | filed decisions: IA6, E-2; IA8, 3.2 | C0 | V-10 for the employee's side; AR-43's read for Admin's (IA11, 2.5) | customer success | RV-06 | records kept | open |
| AR-39 | Admin's Sign in carries "Looking for your benefits? Get the Perqo app" for everyone (C.5; DL-002) | reasoning; IA5's untested assumption | C0 | analytics of Admin's failed sign-ins and the search log (A.2 row 9; IA11, 2.4 and 2.5) | product management | RV-06; RV-04 | records kept | open |

### B.4 · Lifecycles (IA7, section 5; Deliverable D)

| ID | Decision (IA7) | Evidence (kind) | Rung | Test | Owner | Read at | Input | Fix |
|---|---|---|---|---|---|---|---|---|
| AR-40 | The claim's four states kept; T1 to T6, each with trigger, actor and condition, each writing an audit entry; nothing leaves Rejected or Paid (5.2; D.1, D.3) | filed decisions: IA1's states, IA2's transitions; reasoning | C0 | tickets tagged DT-2 and A-3.4 as C1 (IA11, 2.4 for the reading); usability test of decisions (IA11, 2.6) | product management | RV-05 | records kept | backbone |
| AR-41 | A claim waiting more than five working days is marked Overdue, a display rule and not a state (5.2; D.2, EX-3) | reasoning | C0 | records: share of claims waiting over five working days (IA11, 2.5) | product management | RV-06 | records kept | open |
| AR-42 | A claim from an employee marked as left while it waits is still decided (D.2, EX-4) | filed decision: IA8, 3.4 | C0 | interviews with HR managers; tickets from former employees (A.2 row 14, with AR-47) | support | RV-05 | absent: TP-09 Clients, FO-07 not met | open |

### B.5 · Rows of other units' tables that concern Admin

| ID | Assumption (unit, table) | Evidence (kind) | Rung | Test | Owner | Read at | Input | Fix |
|---|---|---|---|---|---|---|---|---|
| AR-43 | Inviting only after budgets are set does not delay onboarding (IA8, 3.2; A.2 row 12) | reasoning | C0 | analytics, time from contract to first join (IA11, 2.5); onboarding interviews | customer success | RV-06 | records kept; interviews absent: TP-07, FO-05 not met | open |
| AR-44 | The leaver rules fit clients' contracts (IA8, 3.4; A.2 row 13) | reasoning | C0 | interviews with clients at contract and with HR managers; none of IA11's methods | customer success | none | absent: TP-07 Customer success, FO-05 not met | backbone |
| AR-45 | Ticket tags locate problems on Admin's pages (IA9, 6.2; A.2 row 20, Admin's half) | reasoning; practice: Chisnell 2016 | C0 | tags on AD- pages set beside a first-click test of Admin's screens with admin users (IA11, 2.3); C4 when both agree | support | RV-05 | absent: TP-09 Clients, FO-07 not met | open |
| AR-46 | A client's structure enters as data without loss (IA10, 2.7; A.2 row 25) | NN/g analysis (McCloskey 2014, through IA10); reasoning | C0 | interviews with account owners at FO-05; configuration requests logged per client | customer success | none | absent: TP-07 Customer success, FO-05 not met | backbone |

### B.6 · Open questions, with owners

IA8 left G-5 to G-7 free and asked that they be kept "as open questions with owners" (IA8, "What later units take"). Each owner is set here (Perqo, fictional), by IA9's routing rule: all three touch two surfaces or a rule, so the IA review decides and product management signs off (IA9, D.1), and product management owns each row. The function whose answer the decision needs is named beside it.

| ID | Open question | Answer needed from | Default until decided | Test | Owner | Read at | Input | Fix |
|---|---|---|---|---|---|---|---|---|
| AR-47 | G-5: how a leaver learns of a claim decided after they left (IA8, 1 and 3.4; A.2 row 14) | support; HR managers at clients | none set: IA8 left it free | interviews with HR managers; tickets from former employees (IA11, 2.4 for the reading) | product management | RV-05 | absent: TP-09 Clients, FO-07 not met | open |
| AR-48 | G-6: which allocations an employee keeps when moved to another group mid-period (IA8, 1 and 3.3) | finance managers at clients; customer success | none set: IA8 left it free | interviews with finance managers at FO-07; records: moves to group mid-period (IA11, 2.5) | product management | RV-06 | absent: TP-09 Clients, FO-07 not met | backbone |
| AR-49 | G-7: what happens to money unspent at a period's end (IA8, 1 and 3.3) | leadership, with legal: a commercial term | DL-018, proposed: no surface says; Budget use reports it as unspent | none of IA11's methods: a contract term, decided at FO-09 | product management | none | absent: TP-12 Leadership, FO-09 not met | backbone |

## Deliverable · C · The Perqo stakeholder map

*Face of this artefact (IA2, the notation sheet): stakeholder map of Perqo's IA, IA10's twelve functions placed by power and interest on a scale of 0 to 10, with Rosala's four quadrants, each function's touchpoint row, forum, format, position on record and the register rows it owns; fidelity F2. Decision: how each function is engaged, and who is asked when an answer is missing. Readers: the IA designer, product management, customer success. Leaves out: named people, attitudes not on record, the partnerships team (not one of IA10's functions). Owner: the IA designer; version 1, dated 10 November 2026; every placement is assumed until each function is interviewed (section 4.2), and the map is revised at each FO-09 (Rosala: mapping "is not a one-time activity"); Perqo is fictional.*

### C.1 · The placements

Each placement is a Perqo fact (Perqo, fictional), set by section 4.1's rule: power from what the function can decide or stop (IA9, section 4.1 and D.1; IA10, A.2), interest from the fidelity it reads (IA10, A.1). The quadrants are Rosala's, split at 5 on each scale: Manage closely (power and interest above 5), Keep satisfied (power above 5, interest 5 or less), Keep informed (power 5 or less, interest above 5), Monitor (both 5 or less). Leadership's placement is IA10's; engineering's and sales' quadrants are those IA10 read from IA9's tables (IA10, section 5).

| TP | Function | Power | Interest | Quadrant | Why (filed units) | Forum and format | Position on record | Register rows owned |
|---|---|---|---|---|---|---|---|---|
| TP-01 | Product management | 9 | 7 | Manage closely | signs off rule and two-surface changes (IA9, 4.1); reads F2 | FO-01, FO-09; impact list, BR-1 | DL-015: HR reads the receipt to decide (IA10, 4.3) | 15 |
| TP-02 | Engineering | 7 | 9 | Manage closely | sits in the IA review; consulted on fifteen steps (IA10, 5); reads F3 | FO-01, FO-02; F3 tables, BR-2 | none | 5 |
| TP-03 | Content team | 7 | 8 | Manage closely | decides taxonomy values (IA9, D.1); reads F2 and F3 | FO-01, FO-03; vocabulary, inventory | none | 0 |
| TP-04 | Marketing | 2 | 6 | Keep informed | consulted on perqo.com's inventory only (IA10, 5); reads F1 or F2 | FO-03; two-level sitemap | none | 0 |
| TP-05 | Localisation | 1 | 1 | Monitor | dormant until a second language (IA10, 2.3) | none yet (DD-IA3) | none | 0 |
| TP-06 | Sales | 3 | 7 | Keep informed | consulted on four steps, told of seven (IA10, 5); reads F1 and F2 | FO-04; BR-3, demo path | none | 0 |
| TP-07 | Customer success | 4 | 8 | Keep informed | configures each client (IA10, 2.5); in no IA9 table; reads F2 | FO-05, FO-07; workbook, training paths | none | 7 |
| TP-08 | Support | 6 | 9 | Manage closely | sits in the IA review; owns RV-04 and RV-05 (IA9, C); reads F3 identifiers | FO-01, FO-06; tags, table | none | 4 |
| TP-09 | Clients | 8 | 4 | Keep satisfied | sign off what each role can do (IA7, 6.3); read F1 words and F2 roles | FO-07, FO-02; session materials, release note | none | 0 |
| TP-10 | Legal | 7 | 6 | Manage closely | consulted before a change adding personal data (DL-014, proposed); reads the F3 data view, one slice | FO-08; data view | DL-015: only the deciding HR manager opens a receipt (IA10, 4.3) | 3 |
| TP-11 | Security | 6 | 7 | Manage closely | consulted on each role change (IA10, A.1, TP-11); reads the F3 role matrix, one slice | FO-08; matrix and table | none | 1 |
| TP-12 | Leadership | 10 | 2 | Keep satisfied | IA10's placement (IA10, 2.9); reads F1 | FO-09; one page | none | 0 |

The IA designer owns the remaining 14 rows of the register; it is IA9's owner of the canonical artefacts (IA9, section 4.1) and is not one of IA10's functions, so it is not placed. Six functions are managed closely, two kept satisfied, three kept informed and one monitored.

### C.2 · The map

The figure places the twelve functions by "Interest in the IA's detail" (across) and "Power over the IA" (up), on 0 to 10 with ticks at 0, 5 and 10, the quadrants named as Rosala names them: Keep satisfied, Manage closely, Monitor, Keep informed. Every point is tone 5, shared, because each function reads artefacts of every surface (IA10).

```viz
{"kind": "scatter", "caption": "Stakeholder map: Perqo's twelve functions placed by power and interest in the IA's detail, with Rosala's four quadrants; supports the decision on how each function is engaged and who is asked when an answer is missing (Deliverable C, C.1). Quadrants from Rosala, 'Stakeholder Analysis for UX Projects', NN/g, 2021; functions from IA10, section 1.1 and A.1; leadership's placement from IA10, section 2.9; engineering's and sales' quadrants as IA10, section 5 reads them; every other placement set in C.1 by section 4.1's rule (power from IA9, section 4.1 and D.1, and IA10, A.2; interest from IA10, A.1). Every point tone 5, shared. Perqo is fictional.", "height": 380,
 "x": {"label": "Interest in the IA's detail", "min": 0, "max": 10, "ticks": [0, 5, 10]},
 "y": {"label": "Power over the IA", "min": 0, "max": 10, "ticks": [0, 5, 10]},
 "quadrants": {"x": 5, "y": 5, "names": ["Keep satisfied", "Manage closely", "Monitor", "Keep informed"]},
 "points": [
  {"label": "Leadership", "x": 2, "y": 10, "tone": 5},
  {"label": "Clients", "x": 4, "y": 8, "tone": 5},
  {"label": "Product management", "x": 7, "y": 9, "tone": 5},
  {"label": "Engineering", "x": 9, "y": 7, "tone": 5},
  {"label": "Content team", "x": 8, "y": 7, "tone": 5},
  {"label": "Legal", "x": 6, "y": 7, "tone": 5},
  {"label": "Security", "x": 7, "y": 6, "tone": 5},
  {"label": "Support", "x": 9, "y": 6, "tone": 5},
  {"label": "Customer success", "x": 8, "y": 4, "tone": 5},
  {"label": "Sales", "x": 7, "y": 3, "tone": 5},
  {"label": "Marketing", "x": 6, "y": 2, "tone": 5},
  {"label": "Localisation", "x": 1, "y": 1, "tone": 5}]}
```

### C.3 · What each quadrant is given, and who is asked when an answer is missing

| Quadrant | Rosala's advice (NN/g, 2021) | At Perqo (Perqo, fictional) | When the answer is theirs and missing |
|---|---|---|---|
| Manage closely | "These stakeholders need to be managed closely" | the artefact itself, at F2 or F3, in their forum (IA10, 1.4) | ask at the forum they sit in (FO-01, FO-02, FO-03, FO-06, FO-08); a default as a proposed DL entry decided at the next meeting of that forum |
| Keep satisfied | keep them happy and consult them | one page (leadership, FO-09); session materials and the release note (clients, FO-07, FO-02) | one page with the options and the default; the default decided at the next FO-09, or FO-07 for clients, with the silence recorded as a position "not given" |
| Keep informed | invite them to research, debriefs and critiques | the decisions, in words, on a cadence (FO-04, FO-05) | their input is asked at their forum and recorded as evidence (opinion or fact, section 4.2); they do not hold a decision |
| Monitor | "you should monitor them regularly" | nothing until a trigger (localisation: a second language) | not applicable until the trigger; the row stays at C0 with DD-IA3 named (IA11, 7) |

The client rule holds for every quadrant: a client's structure enters as data, its words as variants, and a request to mirror its approval chain as a DL entry, decided by the routing rule with the client's position recorded (IA10, section 2.7). The partnerships team, whose request for offers on Home and in Benefits is the recorded disagreement of IA6, B.6, owns For merchants on perqo.com (IA5) and is not one of IA10's twelve; it is left off the map, and its position stays with V-06 and V-17 in IA11's plan.

## Deliverable · D · The decision log template, with three entries

*Face of this artefact (IA2, the notation sheet): one-page template for an entry in Perqo's IA decision log, keeping IA9's fields, statuses, routing and version rule (IA9, section 4 and Deliverable D; IA2, section 4, note of 9 November 2026) and IA10's positions field (DL-011, proposed), with a register-rows field (DL-017, proposed), and three entries filled, DL-017 to DL-019; fidelity F3 for the template (ready to fill). Decision: what an entry must hold before a change counts as decided, and how a decision taken without its inputs is recorded. Readers: the IA designer, the IA review, product management; every function named on an entry's told line. Leaves out: DL-001 to DL-016 (IA9, D.3; IA10, A.4; IA11, A.1), the decisions on DL-017 to DL-019. Owner: the IA designer; version 1, dated 10 November 2026; every entry here is proposed; Perqo is fictional.*

### D.1 · The template

One entry, one page. A field marked (proposed) depends on a DL entry not yet decided; if that entry is declined, the field is dropped and the rest of the template stands.

| Field | What to write | Rule |
|---|---|---|
| ID | DL- and the next number, never reused | IA9, D.3 |
| Change | the change in one line | IA9, D.3 |
| Raised by, from | the function or unit, and the signal, story, client request or missing answer that raised it | IA9, D.3 |
| Touches | the artefacts and identifiers it touches, and the J- rows | IA9, D.3; IA8, D.5 |
| Register rows (proposed) | the AR- rows the entry rests on or changes | DL-017 |
| Alternatives considered | each serious alternative in one line | IA9, D.3; Fowler's decision record |
| Positions (proposed) | for each function that disagrees: function, position in one line, reason, what would reopen the decision; a position not given is recorded as "not given" | DL-011; section 4.4 |
| Decided by | the decider IA9's D.1 names | IA9, D.1 |
| Decide at | the forum and meeting where it is decided, and for a missing answer, the meeting at which the default is decided | section 6 |
| Decision, date, reason | the reason answers each position | IA9, D.3; IA10, 4.2 |
| Version effect | a new version if it breaks a citation; a dated amendment otherwise | IA9, 4.4 |
| Places to apply | each place, marked done or not | IA9, D.3 |
| Told | each function told, with the forum (FO-) and the date (DL-012, proposed) | IA9, D.3; IA10, A.3 |
| Supersedes, superseded by | the linked entries; an accepted entry is superseded, never edited | IA9, D.3 |
| Status | proposed, accepted, declined, applied, superseded | IA9, 4.3 |

### D.2 · DL-017: the register beside the log

| Field | DL-017 |
|---|---|
| Change | The assumption register (IA12, Deliverable B) is a canonical IA artefact kept by the IA designer; the decision log gains a field, register rows; IA2's decision table gains two rows, for the register and the stakeholder map |
| Raised by, from | IA12, sections 3 and 7: the assumptions of IA5 to IA11 sit in nine "What later units take" tables, and IA11 had to gather 25 of them into one table (IA11, A.2) |
| Touches | IA9, D.3 (the log's fields) and section 4.1 (the artefacts the IA designer owns); IA2, the artefact decision table; no J- row |
| Register rows | AR-01 to AR-49 |
| Alternatives considered | keep assumptions in each unit's closing table (they scatter, and no review reads them together); a column on each artefact's face (the face would carry dozens of rows) |
| Positions | none recorded |
| Decided by | IA designer: inside the log and IA2's table, renaming nothing, touching no rule and no surface (IA9, D.1), as DL-011 and DL-012 are |
| Decide at | FO-01, the IA review's next meeting, where the IA designer reports it |
| Decision, date, reason | not decided |
| Version effect | dated amendments to IA9, Deliverable D and IA2's decision table: both add, neither breaks a citation |
| Places to apply | IA9, D.3: the list of fields gains "register rows (AR-)" after the artefacts touched; IA9, section 4.1: the register named among the artefacts the IA designer owns; IA2, the artefact decision table: two rows added, as in D.5 below; each not done |
| Told | product management, engineering, support, content team, at FO-01 |
| Status | proposed |

### D.3 · DL-018: a default for G-7, and its escalation

| Field | DL-018 |
|---|---|
| Change | Until G-7 is decided, no screen, label or Help centre article says what happens to money left at a period's end; Budget use (AD-5.3) reports it as unspent for its period, as IA8 set for a leaver's remainder |
| Raised by, from | IA12, section 4.4: the answer is a commercial term owed by leadership, open since IA8 named the gap on 9 November 2026 |
| Touches | Perqo Admin, AD-5.3 Budget use; the Perqo app, the category screens A-2.1 to A-2.4, which already show one period's balance (IA6, B.3); the Help centre's balance articles (H-2.2); BR-3's "not yet decided"; IA8, section 1, G-7; J-14 budgets |
| Register rows | AR-49 |
| Alternatives considered | wait to build period ends until leadership answers (blocks every period-end screen); assume money lapses and say so (decides a contract term in the product); assume it carries over (the same, the other way) |
| Positions | none yet: leadership is asked at the next FO-09, legal at FO-08; a position not given by the meeting that decides is recorded as "not given" |
| Decided by | IA review, product management signs off: two surfaces and a rule (IA9, D.1) |
| Decide at | the first FO-01 after the next FO-09; if leadership has answered, the answer replaces the default by a superseding entry |
| Decision, date, reason | not decided |
| Version effect | a dated amendment to IA8's Deliverable: it adds a note and breaks no citation |
| Places to apply | IA8, section 1, the gaps table, G-7's "Decided in" cell: "left free (section 3.3); default held by DL-018 (IA12)"; not done |
| Told | sales at FO-04 (BR-3 keeps "not yet decided"); customer success at FO-05; clients in the release note, FO-02; leadership at FO-09 |
| Status | proposed |

### D.4 · DL-019: the register's risk on the leadership page

| Field | DL-019 |
|---|---|
| Change | The one-page map for leadership (TP-12) adds the register's count of rows by rung and by input (absent or kept), and each open question with its owner and the date its default was set |
| Raised by, from | IA12, section 6: risk shown where leadership reads, without blocking delivery |
| Touches | IA10, section 2.9 and A.1, TP-12's artefact; FO-09's inputs (IA10, A.2) |
| Register rows | AR-01 to AR-49, as counts; AR-47 to AR-49 by name |
| Alternatives considered | send leadership the register itself (the wrong format for the quadrant, IA10, 1.4); report risk only in the release note (leadership does not read it) |
| Positions | none recorded |
| Decided by | IA designer, consulting product management, which prepares TP-12: inside one artefact, renaming nothing (IA9, D.1) |
| Decide at | FO-01, the IA review's next meeting |
| Decision, date, reason | not decided |
| Version effect | a dated amendment to IA10, Deliverable A |
| Places to apply | IA10, section 2.9, the artefact's list and A.1, TP-12's artefact cell: add "register counts by rung and input; open questions with owners and default dates"; A.2, FO-09's inputs: add "the register's counts"; each not done |
| Told | product management at FO-01; leadership at FO-09 |
| Status | proposed |

### D.5 · The two rows DL-017 would add to IA2's decision table

Under IA2's rule "Keep the notation; extend the legend" (IA2, section 4), as IA7 added the role-by-section matrix (IA7, section 3.5). Proposed with DL-017; no filed artefact changes until it is decided.

| Question asked | Artefact | Figure kind | Fidelity by stage | Reader | Example · built in |
|---|---|---|---|---|---|
| On what evidence does each part of the IA stand, and what would settle it? | Assumption register | table, with an objects figure for its structure | F2 from the first structure drawn; kept at every cycle (IA9, W-09, W-17) | IA designer, product management, engineering, support | Perqo Admin · IA12 |
| Who decides or must be told, and how is each engaged? | Stakeholder map | scatter (power by interest) | F1 at the start of a cycle; F2 once each function is interviewed | IA designer, product management | Perqo · IA12 |

Three facts about the log follow from the three entries (Perqo, fictional). None of DL-011 to DL-019 is decided at this unit's date, so the template's two proposed fields, positions and register rows, are filled here as they would be if accepted. No filed artefact changes at this unit's filing: every entry is proposed. And each entry names the meeting at which it is decided, which is the one thing a decision taken without its inputs needs that IA9's form did not ask for.

## What later units take

**DD-IA1** reads five information architectures closely. It takes the triage tree and section 2's proxy table as its lens on each: which inputs a published IA shows evidence of, which it rests on assumption, and what its public screens can and cannot show, under the course's rule that no real company's IA is asserted beyond its public screens and its own documents. The register's fields (section 3.2) are the form in which it records what each published artefact claims and what it leaves untested.

**DD-IA2** writes the measurement model and the business case for IA work, and takes IA7's Perqo Admin and IA11's metrics. From this unit it takes the Admin register as the list of assumptions a case for Admin's IA rests on, each with its rung as the strength of the claim; AR-02 (the sizing client's volumes) and AR-37 (landing pages) among the rows that records can lift to C5 without recruiting; the 25 backbone rows as the cost of being wrong that the case must price; and the count of absent inputs as the cost of evidence not yet bought.

**DD-IA3** takes taxonomy and governance to scale, and takes IA4's taxonomy, IA9's change control and IA10's forums. From this unit it takes the decision log template (Deliverable D) with its positions and register-rows fields and the "decide at" line, DL-017 to DL-019 as the log's state at this unit's date, the stakeholder map as the roster its forums extend to several languages and markets, and the escalation procedure of section 4.4 as the rule for an owner who does not answer. It also takes the register's process part, left unfilled here (section 3.4), with localisation's TP-05 at C0.

## Perqo facts set by this unit

Every fact below is a course convention (Perqo, fictional), never evidence about the world. Each keeps every registered fact; none renames an IA1 to IA11 label, object, attribute or relationship. DL-017 to DL-019 are proposed, so no filed artefact changes at this unit's filing.

| Fact | Set in | Left free |
|---|---|---|
| The assumption register's fields: ID (AR-), decision, source, evidence and its kind, rung (C0 to C5), test, owner, read at (RV-), input, fix (backbone or open), status | section 3.2 | none |
| The Admin register: AR-01 to AR-49; 42 rows from IA7 (B.1 15, B.2 8, B.3 16, B.4 3), 4 from other units' tables, 3 open questions; every row at C0 and not run on 10 November 2026 | Deliverable B | the results |
| Each register row's test, owner, review and input, as Deliverable B gives them | Deliverable B | when each test runs |
| Owners of G-5, G-6 and G-7: product management for each, with the answer needed from support and HR managers (G-5), finance managers and customer success (G-6), leadership with legal (G-7) | Deliverable B, B.6 | their decisions |
| No meeting of FO-05, FO-07, FO-08 or FO-09 is on record since 9 November 2026 | section 3.4 | when each first meets |
| Backbone and open: objects, roles, top-level structure, addresses and the shared vocabulary are fixed early; 25 backbone rows in Admin's register | section 5; Deliverable B | none |
| The triage tree's questions, their order and its six outcomes | Deliverable A | none |
| The stakeholder map: power and interest on 0 to 10 for each of the twelve functions, quadrants split at 5, as C.1 gives them; register rows owned per function | Deliverable C | named people; attitudes not on record |
| Questions from tenders and demos logged at FO-04 are Perqo's sales-call notes, a proxy at C0 | section 2 | none |
| The escalation procedure: name the owner, ask once in the owner's format, a default as a proposed DL entry with the meeting that decides it, ship it labelled, decide at that meeting with silence recorded as "not given", show the risk | section 4.4 | none |
| The decision log template's added line "decide at" | Deliverable D, D.1 | none |
| DL-017, proposed: the register as a canonical artefact kept by the IA designer; the log's field register rows; two rows in IA2's decision table | Deliverable D, D.2 and D.5 | its decision |
| DL-018, proposed: until G-7 is decided, no surface says what happens to money left at a period's end; Budget use reports it as unspent | Deliverable D, D.3 | its decision; G-7 itself |
| DL-019, proposed: the leadership page adds the register's counts by rung and input, and open questions with owners and default dates | Deliverable D, D.4 | its decision |

## Sources

- Berners-Lee, Tim. "Cool URIs don't change". W3C Style, 1998 (standards documentation, an essay). [w3.org, cool URIs](https://w3.org/Provider/Style/URI)
- Bland, David J. "How assumptions mapping can focus your teams on running experiments that matter". Strategyzer, 4 August 2020 (an excerpt from *Testing Business Ideas*; practice). [strategyzer.com, assumptions mapping](https://strategyzer.com/library/how-assumptions-mapping-can-focus-your-teams-on-running-experiments-that-matter)
- Bland, David J., and Alexander Osterwalder. *Testing Business Ideas: A Field Guide for Rapid Experimentation*. Wiley, 2019. Section 2.1, "Hypothesize" (contents: "Assumptions Mapping"); section 2.3, "Learn", subsection "Evidence", read in a preview on O'Reilly's platform (practice). [oreilly.com, Learn](https://www.oreilly.com/library/view/testing-business-ideas/9781119551447/c02b.xhtml)
- Brown, Dan M. *Designing Together: The Collaboration and Conflict Management Handbook for Creative Professionals*. New Riders, 2013. Contents (chs 4, 5, 9 and 11) and publisher's description (practice). [informit.com, Designing Together](https://www.informit.com/store/designing-together-the-collaboration-and-conflict-management-9780321918635)
- Brown, Dan. "The Delicate Art of Interviewing Stakeholders". EightShapes on Medium, 11 July 2018 (practice). [medium.com, interviewing stakeholders](https://medium.com/eightshapes-llc/the-delicate-art-of-interviewing-stakeholders-d6496443cbec)
- Hall, Erika. *Just Enough Research*. 1st ed. A Book Apart, 2013. Ch. 4, "Organizational Research", opening. [oreilly.com, ch. 4](https://www.oreilly.com/library/view/just-enough-research/9780133964394/ch04.html)
- Hall, Erika. *Just Enough Research*. 2nd ed. A Book Apart, October 2019. Contents: ch. 4, "Organizational Research"; ch. 6, "Competitive Research". [oreilly.com, 2nd ed.](https://www.oreilly.com/library/view/just-enough-research/9781492018032/)
- Rosala, Maria. "Stakeholder Analysis for UX Projects". Nielsen Norman Group, 18 April 2021. [nngroup.com, stakeholder analysis](https://www.nngroup.com/articles/stakeholder-analysis/)
- Cited through the filed units, for claims made there: Cardello, "Three Uses for Analytics in User-Experience Practice", NN/g, 2013 (IA9); Chisnell, "Call centers as a source of data", 2016 (IA9; practice); Cooper and others, *About Face*, 4th ed., 2014, ch. 1, p. 16 (IA1; IA7); Evans, *Domain-Driven Design Reference*, 2015 (IA7); Farrell, "Search-Log Analysis", NN/g, 2017 (IA3); Ferraiolo and others, "Proposed NIST Standard for Role-Based Access Control", 2001, and NIST's RBAC FAQ and glossary (IA7; standards documentation); Fowler, "Architecture Decision Record", martinfowler.com, 2026 (IA9; practice); Garrett, *The Elements of User Experience*, 2nd ed., 2011, ch. 2 (IA9); Kaplan, "8 Design Guidelines for Complex Applications", NN/g, 2020, and Laubheimer, "Data Tables: Four Major User Tasks", NN/g, 2022 (IA7); Katsanos and others, CHI '19 Extended Abstracts, 2019 (IA11); Mausser, "Site Search Analytics: A Conversation with Lou Rosenfeld", UXmatters, 2011 (IA3; practice); McCloskey, "Intranet Information Architecture (IA) Trends", NN/g, 2014 (IA10); Nielsen, "Why You Only Need to Test with 5 Users", NN/g, 2000 (IA11); Prater, A List Apart, 2015 and 2016 (IA4; IA7; practice); Spencer, "Four Modes of Seeking Information and How to Design for Them", Boxes and Arrows, 2006 (IA3; practice); Android Developers, "Canonical layouts" (IA7; platform documentation). Full references in IA1, IA3, IA4, IA7, IA9, IA10 and IA11, Sources.

## Unsure list

- Bland and Osterwalder 2019: that Assumptions Mapping sits in section 2.1, "Hypothesize", is from the preview's contents; the axes, the three types and the top-right rule are quoted from Bland's 2020 excerpt of the book; the book's page was not seen, and no page number was confirmed.
- Bland and Osterwalder 2019, section 2.3: the opinions-and-facts quotations are from a preview on O'Reilly's platform, which cut off before the evidence-strength list's later items; nothing beyond the first item is drawn on.
- Hall 2013 and 2019: only the contents of the second edition and the opening of the first edition's chapter 4 were seen; the O'Reilly copy of chapter 4 is taken to be the first edition from its record, which was not confirmed; nothing is drawn from either chapter's later text.
- Hall's line "the stakeholder conversations are the most important ones we have on any project" is quoted as Brown 2018 reports it; its original place was not found.
- Brown 2013: only the contents and the publisher's description were read; nothing is drawn from the chapters' text.
- Rosala 2021: the keep-satisfied and keep-informed advice is paraphrased from a summary of the page; the quoted phrases were returned as the page's words but the page was not read in full.
- Berners-Lee 1998: the advice to leave information out of an address is paraphrased from a summary of the page; the two quoted lines are its own.
- The four shortages' symptoms, the triage order, the backbone criterion and the escalation procedure are this unit's synthesis and practice; no source read for this unit measures any of them.
- Object: the assumption register for Perqo Admin, AR-01 to AR-49, Deliverable B
