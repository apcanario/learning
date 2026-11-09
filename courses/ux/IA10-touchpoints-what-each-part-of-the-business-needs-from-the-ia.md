---
code: IA10
title: Touchpoints: what each part of the business needs from the IA
course: ux · IA · Information Architecture
model: Opus 5.5
written: 2026-11-09
search: off
---

# IA10 · Touchpoints: what each part of the business needs from the IA

IA4 to IA8 built the IA of Perqo (Perqo, fictional), the flexible-benefits platform this course runs on, and IA9 put that work into a product cycle with owners, consulted and informed functions, reviews and a decision log. Every face in those units names its readers, and IA9's tables name the functions that own, are consulted on and are told of each step. None of them says what each of those functions asks of the IA, which artefact answers it, cut to which fidelity, in what format, and in which meeting or document the exchange happens. This unit does. It covers the published practice on communicating design to an audience, labelled as practice; for each function that touches the IA, its question, its artefact, its fidelity and format, and its forum; the risk of building a client's org chart into the product; the failure modes of each touchpoint and how the IA records a disagreement; and the same object map read by engineering and by sales. The deliverable is the Perqo touchpoint matrix, with its forums, and three one-page IA briefs, for product management, engineering and sales, each built from the same Perqo IA and saying only what that audience needs.

Every figure uses IA2's notation (IA2, section 5.2 and the notation sheet). This unit draws three of its six tones. Tone 5, shared, carries most figures, because a touchpoint reads artefacts of every surface. Tone 1, perqo.com, carries the sales reading of the object map, which is drawn in perqo.com's words, and the owners of perqo.com's pages. Tone 6, a stop, marks a position that a decision did not take.

What the filed units hand on, and where this unit uses it:

| From | What it hands on | Used in |
|---|---|---|
| IA1, section 4 | every deliverable names the decision it supports and its readers; the six touchpoints and what each reads for | sections 1 and 2 |
| IA2, sections 1.0 and 3; the decision table's readers column; the notation sheet's Readers field | F1 to F3; the five faults; which reader each artefact serves | sections 1.3 and 3; Deliverable A |
| IA4, Deliverables A and B | the object map; the benefits taxonomy and its rules R1 to R10 | sections 2.3 and 3 |
| IA5, section 5; "What the inventory hands on"; "What the catalogue hands on" | what marketing, search, localisation, pricing and sign-in bring; the owner column as the content touchpoint | section 2.3; the owners figure |
| IA6, the task inventory, app map and wireflows | the app's screens, states and entries | sections 2.6 and 2.7; BR-2 |
| IA7, Deliverables A to D and section 6 | model names, the role-by-section matrix, the navigation model, the claim's transitions; the IA against the data model | sections 2.2 and 2.8; BR-2 |
| IA8, D.3, CL-1 to CL-6, the J- table and D.5 | the rules in words for sales; the purchase lifecycle for sales and the client; what each touchpoint must be told when a join changes; the reading guide | sections 2.4, 2.5, 2.7 and 3; A.3; BR-3 |
| IA9, Deliverables A, C and D; section 4.1 | when each function enters a cycle; its standing duties; the decision log's "told" field; the routing rule | sections 4 and 5; Deliverable A; DL-011 to DL-015 |
| IA5 to IA9, the assumption tables | which function's reading of an artefact each assumption depends on | "What later units take" |

## 1 · What a touchpoint is, and the published practice on communicating design

### 1.1 · Readers, questions and the one view

IA1 set the rule this unit rests on: an IA deliverable is one view, chosen for a decision, with named readers, and it says on its face what it leaves out (IA1, section 4; Brown, *Communicating Design*, 2nd ed., New Riders, 2011, ch. 5; Tankala, "Information Architecture vs. Sitemaps", NN/g, 3 September 2023). IA1 also gave each of the course goal's six touchpoints a reason to read: product management for scope and priority, engineering for what must be built and how labels map to the model, content for where each piece lives and what it is called, sales for how the product will be shown and named to a buyer, support for how a customer will describe where they are, the client for whether its own structure fits (IA1, section 4).

A **touchpoint**, in this course, is a function of the business that depends on the IA for a decision of its own, with five things fixed for it: the question it asks, the artefact that answers it, the fidelity and format it can read, and the meeting or document where the exchange happens. The brief for this unit widens IA1's six into nine groups: product management; engineering; content, marketing and localisation; sales and pre-sales; customer success and onboarding; support; clients; legal, security and compliance; leadership. At Perqo (Perqo, fictional) the nine become twelve functions, because content, marketing and localisation are separate owners on perqo.com (IA5, Deliverable A), and legal and security read different artefacts (section 2.8). In the figures they go by short names: Product management, Engineering, Content team, Marketing, Localisation, Sales, Customer success, Support, Clients, Legal, Security, Leadership.

### 1.2 · Brown: deliverables as conversation, and the brief as a form

Dan Brown's *Communicating Design* is the field's book on this exchange, and what it says is practice: the author's account of what works, with no measurement behind it. Its preface calls documentation "the underbelly of web design", something that "helps project team members communicate with each other", and says documents "serve as milestones" (Brown 2011, preface to the second edition, [oreilly.com, preface](https://www.oreilly.com/library/view/communicating-design-developing/9780131385399/pr02.html)). Its second part opens with a definition of a deliverable as a document submitted during a project to facilitate communication, "capture decisions, and stimulate conversation", and Brown says the first edition treated the artefacts "as separate deliverables", where he now has "a greater sensitivity to how deliverables and the design process work together to move a project along" (Brown 2011, ch. 8, "Deliverable Basics", [oreilly.com, ch. 8](https://www.oreilly.com/library/view/communicating-design-developing/9780131385399/ch08.html)). Chapter 2 carries sections headed "Challenges in Communicating Design" and "Presenting Design" (Brown 2011, contents, [oreilly.com, contents](https://www.oreilly.com/library/view/communicating-design-developing/9780131385399/bk01-toc.html)); only the headings were seen for this unit, and nothing is drawn from their text.

Chapter 9 gives the form this unit's deliverable uses. A design brief is "A document describing the design problem and establishing a foundation of objectives, principles, and requirements"; to varying degrees it "Articulates the objectives of the project", "Positions the project in a larger context", "States the design problem", "Establishes other parameters, like timing", "Summarizes any inputs, like technical, content, or user requirements" and "Defines the direction or approach the designers will take" (Brown 2011, ch. 9, "Design Briefs", [oreilly.com, ch. 9](https://www.oreilly.com/library/view/communicating-design-developing/9780131385399/ch09.html)). Brown's brief is written at a project's start, for the whole team. This unit takes its parts and changes two things: an IA brief is written for one function, and it is re-issued when the IA changes, from the same source as every other brief.

### 1.3 · Brown: conflict and collaboration

Brown's later book, *Designing Together: The Collaboration and Conflict Management Handbook for Creative Professionals* (New Riders, June 2013, [oreilly.com, Designing Together](https://www.oreilly.com/library/view/designing-together-the/9780133390957/)), treats the people side of the same exchange; it is practice. Its theory part opens: "Conflict and collaboration are two complex dynamics"; "With conflict, teams must recognize how difficult conversations contribute to the design process"; "With collaboration, teams must embrace virtues that lead to productive habits" (Brown 2013, Part II, [oreilly.com, Part II](https://www.oreilly.com/library/view/designing-together-the/9780133390957/part02.html)). Chapter 7 puts the relation in one line: "If conflict is the engine, then collaboration is the oil" (Brown 2013, ch. 7, [oreilly.com, ch. 7](https://www.oreilly.com/library/view/designing-together-the/9780133390957/ch07.html)). Its chapters on conflict separate "Healthy vs. Unhealthy Conflict" and ask "What Causes Conflict?", under "Internal Sources of Conflict" and "External Sources of Conflict" (Brown 2013, contents); the publisher's description lists 46 conflict management techniques and 31 diagnoses of difficult situations (same page). Scott Berkun's foreword opens: "Successful design projects require effective collaboration and healthy conflict" (reproduced in Berkun, "Book review: Designing Together", scottberkun.com, 27 June 2013, [scottberkun.com, review](https://scottberkun.com/2013/book-review-designing-together/); practice). For this unit the useful reading is narrow: a touchpoint will disagree with the IA, the disagreement is part of the work, and section 4 gives it a place in the record.

### 1.4 · Who is consulted and who is told

Maria Rosala's NN/g article on stakeholder analysis defines a stakeholder as "anyone who has interest in your project" and plots stakeholders on a power-interest matrix with four quadrants: those with high power and high interest "need to be managed closely"; with high power and low interest, "It's important to ensure these stakeholders are happy"; with low power and high interest, keep them informed, by inviting them to research, debriefs and design critiques; with low power and low interest, "you should monitor them regularly" ("Stakeholder Analysis for UX Projects", Nielsen Norman Group, 18 April 2021, [nngroup.com, stakeholder analysis](https://www.nngroup.com/articles/stakeholder-analysis/); NN/g guidance). IA9's owner, consulted and informed columns are a finer version of the same sort (IA9, Deliverable A). On this unit's reading, Rosala's quadrants add one thing: the format follows the quadrant. A function that is managed closely reads the artefact itself; one that must be kept satisfied reads one page; one that is kept informed reads the decisions and is invited to the sessions where they are tested.

### 1.5 · Translation: one source, cut and renamed

IA5 set the mechanism for serving several readers from one artefact: the team ships one sitemap at three fidelities from one source, the F3 drawing with identifiers, cut to two levels for marketing, "so the three readers never argue from three different maps" (IA5, section 6). IA8 did the same for a rule: one tree, one table for engineering and one sentence for sales, from one source (IA8, section 4.1). This unit calls the operation **translation** and gives it two moves, both from those rules:

- **Cut**: drop the elements the reader's decision does not need, by level or by layer (IA2, section 1.0; IA8, section 5.2). A cut never adds an element the source lacks.
- **Rename**: replace the model name with the name the reader's surface uses, from the vocabulary (IA1, section 2.4; IA8, D.1's shared-objects table). A rename never changes what an element means.

A translated artefact cites the source's version on its face, so a reader holding a brief can tell when it is stale. Five formats cover what Perqo's functions read, each defined by what it carries (Perqo, fictional): **F3 tables cited by identifier** (the object-relationship map's model names, the DT- tables, the transitions); **a drawing cut to levels** (a sitemap at two levels, the whole interaction map); **sentences in words** (IA8's rule in words, D.3); **a one-page brief** (Brown's brief form, for one function, Deliverable B); and **an entry in a release note or a decision log's told line** (IA9, W-14 and D.3).

## 2 · What each function asks of the IA

Each subsection gives the function's question, the artefact that answers it, the fidelity and format it can read, and its forum. The forums are Perqo's meetings and documents, FO-01 to FO-09, set out in Deliverable A, A.2; four of them hold IA9's reviews.

### 2.1 · Product management

**Question:** what does this change touch, and what must be decided before it is built? It covers scope, the roadmap, requirements, and the impact of a change. Garrett's planes overlap in time, so structure work begins while scope is still open, and IA9 drew the consequence: a sitemap started after the requirements are signed has lost the overlap where the structure shows a requirement missing or doubled (IA9, section 1.2; Garrett, *The Elements of User Experience*, 2nd ed., New Riders, 2011, ch. 2). IA8 named the map's third purpose as scope decisions: with lifecycles and rules on one sheet, product management sees which surfaces, stages and rules a change touches before it is estimated (IA8, section 1).

**Artefact:** the interaction map's surface layer and its J- table (IA8, D.1 and D.4), read through IA9's impact list, which names the surfaces, objects, J- rows and DT- rules a piece of work touches (IA9, W-05). **Fidelity and format:** F2 with identifiers; an impact list citing identifiers, and the one-page brief BR-1. **Forums:** the IA review (FO-01), where product management sits and signs off rule changes and two-surface changes (IA9, section 4.1), and the debt triage it owns each quarter (IA9, RV-10).

### 2.2 · Engineering

**Question:** what objects, names, routes, permissions and rules do we build, and which of them can we not change alone? It covers the data model, routing, permissions, API and event naming and the shared vocabulary. IA7 drew the line between the IA and the data model at Perqo: one table shown as two objects, one action writing many records, computed attributes, views with no table, fields with no screen (IA7, section 6.1). It took Evans's ubiquitous language as the rule that holds the two together: "Use the model as the backbone of a language", and "Recognize that a change in the language is a change to the model" (Evans, *Domain-Driven Design Reference*, Domain Language, 2015; IA7, section 6.2).

**Artefact:** the F3 artefacts. The object-relationship map with model names (IA7, Deliverable A, A.2); the navigation model's pages and addresses (IA7, C.1; IA6, B.4; IA5, Deliverable A); the role-by-section matrix with the calls to action it is read from (IA7, B and A.4); the decision tables DT-1 to DT-3 with the Unique hit policy (IA8, D.3); and the claim's transitions T1 to T6 (IA7, D.1). **API and event naming** follows from Evans's rule (Perqo, fictional; proposed for engineering to confirm): a resource takes the object's model name, and an event takes the model name and the state the object enters, so the event for T3 names `claim` and Approved; the strings are engineering's. **Fidelity and format:** F3; tables cited by identifier in each story (IA9, section 2.3), and the brief BR-2. **Forums:** the story check and the release note (FO-02; IA9, RV-01 and RV-02), and the IA review (FO-01), where engineering sits because a rename is a change to the model (IA9, section 4.1).

### 2.3 · Content, marketing and localisation

**Content team.** **Question:** what is each thing called on each surface, where does each page live, and which template fills it? **Artefact:** the controlled vocabulary with each surface's name (IA2, section 5.3; IA8, D.1), the benefits taxonomy, which the content team owns (IA4, Deliverable B; IA9, section 4.1), the inventory row and the template entry, which IA5 called the writer's real document (IA5, section 6). **Fidelity:** F2 for the vocabulary, F3 for the inventory and the taxonomy's identifiers. **Forum:** the vocabulary and content review (FO-03), which holds IA9's RV-07 and RV-08.

**Marketing.** **Question:** what does a buyer see first, under which labels, and where do campaigns and indexing go? **Artefact:** perqo.com's sitemap cut to two levels, with the label table (IA5, section 6 and B.2), the inventory's URL, redirect and indexed columns, and the campaign rule: a page under /lp/, noindex, in no navigation, with an owner and an end date (IA5, sections 5.1 and 5.2). Search-engine structure enters the IA as vendor documentation: Google's guidance asks for readable URLs and permanent redirects (Google Search Central, as cited in IA5, section 5.1; vendor documentation, checked 3 November 2026). **Fidelity:** F1 or F2 (IA5, section 6). **Forum:** FO-03, where marketing is consulted on the rolling audit (IA9, RV-08).

**Localisation.** **Question:** what key does every language version share, and what changes by market? **Artefact:** the inventory's IDs, which carry no words of any language, and the template catalogue's localisation column, where the modules marked by market (M-10, M-11, M-24, M-25) need a decision per market (IA5, section 5.3 and "What the catalogue hands on"). **Fidelity:** F3. perqo.com is published in English only (IA5, section 5.3), so at Perqo this touchpoint is dormant: the row in the matrix is conditional, [when a second language is added], and DD-IA3 sets its forum.

**The owner column.** IA5 handed this unit its inventory's owner column as the content touchpoint (IA5, "What the inventory hands on"). Counted over the 52 rows of the redesigned site, each row counted once under its first-named owner (S-2, "Marketing, with Sales", under Marketing; H-2.1.3, "Support, with Content team", under Support), the owners are: Support 26, Marketing 13, Content team 5, Legal 3, Product 2, Sales 2, Partnerships 1 (Perqo, fictional; from IA5, Deliverable A, A.1 to A.3). Half of perqo.com is support's, because the Help centre is (A.3); the content touchpoint at Perqo is two functions with most of the pages and five with a few each.

```viz
{"kind": "compare", "max": 30, "caption": "Owners of perqo.com's pages: the 52 rows of the redesigned site by owner, each row counted once under its first-named owner; supports the decision on which functions the content touchpoint must reach (section 2.3). Counted from IA5, Deliverable A, A.1 to A.3 (removed rows excluded); 'Product' is IA5's owner name for product management. Every bar tone 1, perqo.com. Perqo is fictional.",
 "rows": [
  {"label": "Support", "value": 26, "tone": 1},
  {"label": "Marketing", "value": 13, "tone": 1},
  {"label": "Content team", "value": 5, "tone": 1},
  {"label": "Legal", "value": 3, "tone": 1},
  {"label": "Product", "value": 2, "tone": 1},
  {"label": "Sales", "value": 2, "tone": 1},
  {"label": "Partnerships", "value": 1, "tone": 1}]}
```

### 2.4 · Sales and pre-sales

**Question:** how do we tell the story of the system, run the demo, and answer a proposal or a tender without promising what the product does not do? IA8 named what sales needs from the system map: the decision trees with their words for sales, and the purchase lifecycle (IA8, D.3 and "What later units take"). Its sixth practice for a rule is a sentence for sales, because sales explains the rule to a buyer and the Help centre article carries the same words (IA8, section 4.1), and IA9 made sales a function told of every decision that changes what perqo.com or a rule says (IA9, Deliverable A).

**Artefact:** the purchase lifecycle CL-1 to CL-6 (IA8, section 3.2); the rules DT-1 to DT-3 in words (IA8, D.3); the surfaces map at F1, three surfaces and what crosses between them (IA1, Deliverable; IA8, D.1); and, for tenders, which ask who may see what, the role-by-section matrix in words (IA7, Deliverable B). **The demo path** (Perqo, fictional) follows the lifecycles in their order, each step named by identifier so that a change to any step reaches sales through the J- table: Product (S-1); a policy's open categories and limit (AD-3.1); Set budgets (AD-2.2); Invite employees (AD-1.3); Join (A-0.1); Home (A-1); New claim over the limit (A-3.1); Approvals (AD-4); the approved Claim (A-3.4); Budget use (AD-5.3). **Fidelity and format:** F1 for the story, F2 for the rules in words; sentences, the demo path and the brief BR-3. **Forum:** the pre-sales briefing (FO-04), monthly, and the release note.

### 2.5 · Customer success and onboarding

**Question:** how should this client be configured, and what does each of its admin users need to learn? At Perqo (Perqo, fictional) the setup staff IA8 placed outside the surfaces (IA8, section 3.2) are the customer success team, which sets up the client and its account owner at CL-3 and supports the account owner through CL-4 and CL-5. **Artefact:** the onboarding order (client and account owner, admin users, groups and policies, budgets, invitations, joining; IA8, section 3.2), the role-by-section matrix (IA7, B), and DT-1 and DT-2 as tables, because a client's policy settings are their inputs (IA8, D.3). **Format:** a **configuration workbook** per client (Perqo, fictional): one table per onboarding step, with a row per employee group giving its policy's open categories, its auto-approve limit and its covered items, then its budgets per category and period; and a **training path** per role, built from the Help centre's articles for HR and finance teams: for an HR manager, H-1.2.1, H-1.2.2, H-1.2.3, H-1.2.5 and H-1.3.1; for a finance manager, H-1.1.1 and H-1.1.2 (IA5, A.3). The account owner's own work (Company, Admins, Activity log; IA7, section 3.4) has no Help centre article: drawing the training paths found that gap, and it is logged for support. **Fidelity:** F2. **Forum:** the onboarding handover (FO-05), once per new client and at each renewal (CL-6).

### 2.6 · Support

**Question:** where is this person, why did this outcome happen, and where does the structure fail? IA8's reading guide says support reads the lifecycle layer to place a caller in a stage, and each tree stops at the first question that ends the path "so support can say at which question a case stopped" (IA8, D.5). IA9 set support's tags: surface, screen or page identifier, and for a rule the DT- tree, read monthly (IA9, section 6.2; RV-05), after Chisnell's account of the call centre as a source of data (Chisnell, danachisnell.com, 24 July 2016; IA9, section 6.2; practice).

**Artefact:** the tag list, and a **where-things-go-wrong table** drawn from the filed IA (Perqo, fictional): the stops of DT-1 to DT-3 (IA8, D.3), the claim's rejections T1, T4 and T5 with their reasons (IA7, D.1), the exceptions EX-1 to EX-4 (IA7, D.2), the screen states that block an action (IA6, B.5; the category with no allocation, IA8, section 4.2), and the open gaps G-5 to G-7 (IA8, section 1). Each row names where the person is when it happens and what the screen says. **Fidelity:** F3 identifiers. **Forum:** the ticket and log read (FO-06), which holds IA9's RV-04 and RV-05; support also sits in the IA review (FO-01).

### 2.7 · Clients

**Question:** do these words, roles and rules fit our people, and what changes for our staff? IA9 gave clients three points in a cycle: consulted on Admin's labels and structure (W-06), participants in tests (W-09), and told of Admin changes their staff will see (W-14). Those are vocabulary, validation and notice. Co-creation is the fourth: the Design Council's Develop phase draws on "co-designing with a range of different people" (Design Council, "Framework for Innovation", checked 9 November 2026; IA9, section 1.1).

**The org-chart risk.** A client asked how the product should be organised will often describe itself: its departments, its approval chain, its job titles. Marieke McCloskey's NN/g analysis of 77 intranet IAs reports that intranets "are initially structured to mimic the organizational configuration of the company", that "whenever the institution reorganizes, the navigation must also change", and that "Task-based structures often better withstood organizational change than intranets organized by department" ("Intranet Information Architecture (IA) Trends", Nielsen Norman Group, 23 February 2014, [nngroup.com, intranet IA trends](https://www.nngroup.com/articles/intranet-information-architecture-ia/)). The finding is about intranets, where the organisation is the user's own; a backoffice that encodes one client's org chart breaks the same way when that client reorganises, and fails every other client from the start. Donna Spencer's practitioner article names the reader's side of it: staff "can't find information if they don't know who is responsible for it" ("Why are intranets structured like the organisational chart?", Step Two, 3 April 2005, [steptwo.com.au, org chart](https://www.steptwo.com.au/papers/cmb_orgchart/); practice). Melvin Conway's 1968 thesis, that organisations which design systems "are constrained to produce designs which are copies of the communication structures of these organizations", is the older form of the same warning, aimed at the builder's organisation ("How Do Committees Invent?", *Datamation*, 1968, as quoted in Adrian Colyer, "How do committees invent?", the morning paper, 13 December 2019, [blog.acolyer.org, Conway](https://blog.acolyer.org/2019/12/13/how-do-committees-invent/)).

Perqo's IA already holds a client's structure where a reorganisation cannot reach the navigation (Perqo, fictional). A client's departments enter as employee groups, records each with one policy (IA4, Deliverable A, R-02 to R-04); Admin's top level is by object and work queue, the same for every client (IA7, section 4.2). A reorganisation moves employees between groups, a call to action HR already has (IA4, A.3: employee -> move to group); it changes no page. The rule for the client touchpoint follows: **a client's structure enters as data, its words enter as variants, and a request to mirror its approval chain enters as a decision log entry**. A client that wants line managers to approve claims is asking for roles scoped to some employee groups, which IA7 left free (IA7, section 3.2); the request is logged with the client's position and decided by the routing rule.

**Artefact and format:** the vocabulary as a word list for consultation (F1), the role-by-section matrix and DT-2 in words (F2), and the release note for notice. **Forums:** the client validation session (FO-07), held in a cycle that touches Admin's labels or roles (IA9, W-06 and W-09), and the release note (FO-02).

### 2.8 · Legal, security and compliance

**Legal. Question:** what personal data does each object hold, who sees it, what is recorded when it changes, and what is asked of the person? Perqo's objects hold personal data, and one category holds more: the Health category covers therapy sessions, which an employee usually claims (IA4, Deliverable B, BI-003, usual way to pay: Claim), so a claim's receipt can show that an employee saw a therapist. Where the EU's General Data Protection Regulation applies, its Article 9(1) puts "data concerning health" among the special categories of personal data whose processing is prohibited except under the conditions of Article 9(2) (Regulation (EU) 2016/679, Article 9, as adopted, [legislation.gov.uk, GDPR art. 9](https://www.legislation.gov.uk/eur/2016/679/article/9/adopted); legal text). Perqo's markets are left free (IA5, section 5.3), so whether it applies is legal's question; what the IA owes legal is a view that lets the question be asked object by object.

**Artefact:** a **data view** (Perqo, fictional), a cut of IA7's attributes table (IA7, A.2) with two columns added for legal's reading: the data category of each attribute, and the roles that see it, read from the role-by-section matrix (IA7, B); with the audit entry (O-17), which records who changed what, before and after, as History and the Activity log (IA7, section 5.3). The app's device permissions belong here too: the camera is asked for when the employee taps Take a photo, and notifications once, after the first claim (IA6, section 4.4). Retention is open in two places the filed units left free: how long audit entries are kept (IA7) and how long a former client's records are kept (IA8, section 3.2). **Fidelity:** F3. **Format:** the data view, a table.

**Security. Question:** which role may see and do what, and is every permission written once? IA7 set the rule that permissions are written once, on the calls to action, and both the role matrix and the access-control configuration are read from them, which protects "the client, who signs off what each role can do, and security, who build it" (IA7, section 6.3). **Artefact:** the role-by-section matrix with the calls to action it is read from (IA7, B and A.4), at F3 for build. **Forum, for both:** the privacy and security review (FO-08), consulted on each change that adds an attribute holding personal data or changes a role's mark (DL-014).

### 2.9 · Leadership

**Question:** what is the system, where is it weak, and what is decided and what is open? At Perqo (Perqo, fictional) leadership is placed in Rosala's keep-satisfied quadrant, high power and low interest in the IA's detail, and is given one page (Rosala 2021). **Artefact:** the one-page map (Perqo, fictional): IA8's whole interaction map, the index figure that names each layer and points to its full figure (IA8, D.4); the open gaps G-5 to G-7 with their owners (IA8, section 1; IA12); the count of IA debt, decision log entries accepted and not applied, from the quarter's triage (IA9, RV-10); and the decisions since the last page, by DL- identifier. **Fidelity:** F1, with identifiers so a question can be followed down. **Format:** one page. **Forum:** the leadership quarterly (FO-09), after RV-10.

## 3 · The artefact-to-audience map, and one translation

### 3.1 · Which artefact each function reads, and at what fidelity

IA2's decision table gives each artefact its readers (IA2, the artefact decision table); IA5 to IA8's faces name theirs; section 2 adds legal, security, customer success and leadership. The map below joins them: one row per artefact, one column per group of the brief, the cell the fidelity that function reads it at, or "words" where the function reads the artefact as sentences. Content in the map stands for the content team, marketing and localisation together, and Legal, security for those two. The rows use short names: Inventory, Vocabulary, Taxonomy, Sitemap, Navigation model, Wireflow, Decision tree and State diagram are IA9's (IA9, section 3.2); Relationship map is the object-relationship map; Role matrix is the role-by-section matrix (IA7, B); Lifecycles are IA8's CL- and EL- swimlanes; Interaction map is the cross-surface interaction map, which IA9 calls the cross-surface map. An empty cell is an artefact the function does not read.

```viz
{"kind": "matrix", "caption": "Artefact-to-audience map: which function reads each artefact of Perqo's IA, and at what fidelity; supports the decision on which cut of an artefact goes to whom (section 3.1). Readers from IA2's artefact decision table and the faces of IA5 to IA8 (IA5, Deliverables A and B; IA6, Deliverable B; IA7, Deliverables A to D; IA8, Deliverable); legal, security, customer success and leadership from section 2 of this unit. Content stands for the content team, marketing and localisation; Legal, security for those two. Every row tone 5, shared: each artefact is read across functions. Perqo is fictional.",
 "cols": ["Product management", "Engineering", "Content", "Sales", "Customer success", "Support", "Clients", "Legal, security", "Leadership"],
 "rows": [
  {"label": "Inventory", "tone": 5, "cells": ["F2", "F3", "F3", null, null, "F3", null, "F2", null]},
  {"label": "Vocabulary", "tone": 5, "cells": [null, "F3", "F3", "F2", "F2", "F2", "F1", null, null]},
  {"label": "Taxonomy", "tone": 5, "cells": ["F2", "F3", "F3", "words", "F2", null, "F2", null, null]},
  {"label": "Sitemap", "tone": 5, "cells": ["F2", "F3", "F2", "F1", null, "F2", null, null, null]},
  {"label": "Navigation model", "tone": 5, "cells": [null, "F2", "F2", null, null, "F2", null, null, null]},
  {"label": "Relationship map", "tone": 5, "cells": ["F2", "F3", null, "words", null, null, "F2", "F3", null]},
  {"label": "Role matrix", "tone": 5, "cells": ["F2", "F3", null, "words", "F2", "F2", "F2", "F3", null]},
  {"label": "Wireflow", "tone": 5, "cells": [null, "F3", "F2", null, null, "F2", null, null, null]},
  {"label": "Decision tree", "tone": 5, "cells": ["F2", "F3", "words", "words", "F2", "F2", "words", null, null]},
  {"label": "State diagram", "tone": 5, "cells": [null, "F3", "F2", null, null, "F2", "F2", null, null]},
  {"label": "Lifecycles", "tone": 5, "cells": ["F2", null, null, "F1", "F2", "F2", "F1", null, "F1"]},
  {"label": "Interaction map", "tone": 5, "cells": ["F2", "F2", "F2", "F1", "F1", "F2", "F1", null, "F1"]}],
 "legend": [
  {"mark": "F1", "means": "sketch: the shape and the main names", "tone": 5},
  {"mark": "F2", "means": "working: complete for its scope, in the product's words", "tone": 5},
  {"mark": "F3", "means": "specification: identifiers, every condition, citable in a ticket", "tone": 5},
  {"mark": "words", "means": "read as sentences: the rule or the object said in the reader's words", "tone": 5}]}
```

Read down a column and a function's reading list appears: engineering reads nine of the twelve artefacts at F3; sales reads four in words, three as sketches and the vocabulary at F2; leadership reads two, both as sketches. Read across a row and an artefact's audiences appear: the decision tree has seven readers in three forms, which is why IA8 drew it as a tree, a table and a sentence from one source (IA8, section 4.1). The empty cells say what a function never needs: sales reads neither the wireflows nor the state diagram, because the screens and transitions are what the demo shows and the rules in words explain; leadership never needs any F3 artefact.

### 3.2 · The same object map, read by engineering and by sales

The translation example takes one slice of IA4's object map, the six objects of a claim and a card payment and their relationships (IA4, Deliverable A, A.2: R-03, R-04, R-05, R-08, R-09, R-10, R-13), and cuts and renames it twice. Engineering's cut keeps the model names IA7 set (IA7, A.2), so its boxes are titled employee_group, policy, employee, allocation, transaction type claim and transaction type card payment, the fields its rules read, the relationship identifiers and the counts. Sales' cut keeps the boxes and the lines, drops the counts and the identifiers, and renames each element into the words a buyer meets: perqo.com's word where perqo.com has one (IA8, D.1), Admin's where it does not, because the buyer's HR and finance staff will use Admin.

| Element | Engineering reads | Sales says |
|---|---|---|
| employee group (O-03) | `employee_group` | Teams and groups |
| policy (O-04) | `policy`: `open_categories`, `auto_approve_limit` | Policies: which categories are open; the auto-approve limit |
| employee (O-05) | `employee`: `status` | Employees |
| allocation (O-06) | `allocation`: `category`, `period`, `amount`, `spent` | Benefits budget: per category, per period; what's left |
| transaction, type claim (O-07) | `transaction` type claim: `status`, `rejection_reason`, `decided_by` | Claims: approved at once up to your limit |
| transaction, type card payment (O-08) | `transaction` type card payment: `merchant_id`, `category` | Card payments: taken at the till if within budget |
| R-03 | R-03 follows, 1 and 1 | follows one |
| R-04 | R-04 contains, 1 and 1..* | includes |
| R-05 | R-05 holds, 1 and 1..* | gets one per category |
| R-08 | R-08 submits, 1 and 0..* | makes |
| R-09 | R-09 is checked against, 0..* and 1 | checked against |
| R-10, R-13 | R-10 spends from; R-13 spends from; 0..* and 1 | paid from |

Every word in the sales column is the vocabulary's or the rule's: the perqo.com labels are IA1's and IA4's, "the auto-approve limit" is the policy's attribute (IA4, A.1), "approved at once up to your limit" is DT-2's sentence cut to its first clause (IA8, D.3), "taken at the till if within budget" is DT-3's row 4 in words (IA8, D.3), and "what's left" is the remaining attribute, which IA7 records as computed (IA7, A.2). The translation adds no claim the source lacks. It loses three things, and the brief for sales says so: the counts (a team follows exactly one policy; an employee holds one budget per open category); the difference between the two kinds of transaction in the model, which sales never needs; and the card payment's other ways to end, the declines of DT-3, which sales reaches through the rules in words.

```viz
{"kind": "objects", "caption": "Translation, engineering's cut: six objects of IA4's object map with IA7's model names, the fields the rules read, relationship IDs and counts (UML multiplicity), F3; supports the decision on what engineering builds and which relationships a change to one object reaches (section 3.2). Every box tone 5, shared: the data model. Lines relate, read left to right on a level line and top to bottom otherwise, unless a triangle marks the other way. Objects and relationships from IA4, Deliverable A, A.2; model names and fields from IA7, Deliverable A, A.2. Perqo is fictional.",
 "objects": [
  {"id": "group", "title": "employee_group", "tone": 5, "attrs": ["O-03"]},
  {"id": "policy", "title": "policy", "tone": 5, "attrs": ["O-04", "open_categories", "auto_approve_limit"]},
  {"id": "employee", "title": "employee", "tone": 5, "attrs": ["O-05", "status"]},
  {"id": "claim", "title": "transaction type claim", "tone": 5, "attrs": ["O-07", "status", "rejection_reason", "decided_by"]},
  {"id": "payment", "title": "transaction type card payment", "tone": 5, "attrs": ["O-08", "merchant_id", "category"]},
  {"id": "alloc", "title": "allocation", "tone": 5, "attrs": ["O-06", "category", "period", "amount", "spent"]}],
 "rows": [["group", "employee", "payment"], ["policy", "claim", "alloc"]],
 "links": [
  {"from": "group", "to": "policy", "label": "R-03 follows", "from_card": "1", "to_card": "1"},
  {"from": "group", "to": "employee", "label": "R-04 contains", "from_card": "1", "to_card": "1..*"},
  {"from": "employee", "to": "claim", "label": "R-08 submits", "from_card": "1", "to_card": "0..*"},
  {"from": "claim", "to": "policy", "label": "R-09 is checked against", "from_card": "0..*", "to_card": "1", "dir": "to"},
  {"from": "claim", "to": "alloc", "label": "R-10 spends from", "from_card": "0..*", "to_card": "1"},
  {"from": "payment", "to": "alloc", "label": "R-13 spends from", "from_card": "0..*", "to_card": "1"},
  {"from": "employee", "to": "alloc", "label": "R-05 holds", "from_card": "1", "to_card": "1..*"}]}
```

The same six boxes and seven lines, as sales reads them.

```viz
{"kind": "objects", "caption": "Translation, sales' cut: the same six objects and seven relationships as engineering's cut, renamed into the words a buyer meets (perqo.com's labels where perqo.com has one, Admin's otherwise) with counts and identifiers dropped; F1; supports the decision on how sales explains what Perqo holds (section 3.2). Every box tone 1, perqo.com: the figure is drawn in perqo.com's vocabulary. Lines relate, read left to right on a level line and top to bottom otherwise, unless a triangle marks the other way. Labels from IA8, D.1's shared-objects table and IA4, Deliverable A, A.1; rule words from IA8, D.3 (DT-2, DT-3). Perqo is fictional.",
 "objects": [
  {"id": "group", "title": "Teams and groups", "tone": 1, "attrs": []},
  {"id": "policy", "title": "Policies", "tone": 1, "attrs": ["which categories are open", "the auto-approve limit"]},
  {"id": "employee", "title": "Employees", "tone": 1, "attrs": []},
  {"id": "claim", "title": "Claims", "tone": 1, "attrs": ["approved at once up to your limit"]},
  {"id": "payment", "title": "Card payments", "tone": 1, "attrs": ["taken at the till if within budget"]},
  {"id": "alloc", "title": "Benefits budget", "tone": 1, "attrs": ["per category, per period", "what's left"]}],
 "rows": [["group", "employee", "payment"], ["policy", "claim", "alloc"]],
 "links": [
  {"from": "group", "to": "policy", "label": "follows one"},
  {"from": "group", "to": "employee", "label": "includes"},
  {"from": "employee", "to": "claim", "label": "makes"},
  {"from": "claim", "to": "policy", "label": "checked against", "dir": "to"},
  {"from": "claim", "to": "alloc", "label": "paid from"},
  {"from": "payment", "to": "alloc", "label": "paid from"},
  {"from": "employee", "to": "alloc", "label": "gets one per category"}]}
```

The two figures are one source. A change to R-09, to the auto-approve limit or to the label Benefits budget changes both, which is why IA8's J- table lists who is told when a join changes and Deliverable A, A.3 turns it into a list of functions.

## 4 · Failure modes, and how the IA records a disagreement

### 4.1 · How each touchpoint fails

Each touchpoint fails in a way the filed units have already met at Perqo or named as a risk. The table names the failure, what it costs and the guard that a filed rule or this unit sets. None of these failures has been measured; the costs are the mechanisms the filed units describe.

| Function | Failure | What it costs | Guard |
|---|---|---|---|
| Product management | scope set and estimated before the structure is drawn | a join missed: IA8 found seven gaps only when the layers were laid together (IA8, section 1) | the impact list before estimation (IA9, W-05) |
| Engineering | the schema read into the labels, or the IA "fixed" to match the schema | one table shown as one object where people need two (IA7, section 6.1) | every divergence written down; the vocabulary first (IA7, section 6.3) |
| Content team | a label drifts on one surface | IA2's fault 5: one thing, two names, no mapping (IA2, section 3) | rename through the vocabulary (IA2, section 4) |
| Marketing | a page made outside the sitemap | duplicates and leftovers: S-1.6, S-1.7, L-02 (IA5, section 1.3) | the new-page decision tree (IA5, section 5.2) |
| Localisation | identifiers that carry words | language versions that cannot point to each other (IA5, section 5.3) | IDs without words (IA5, section 5.3) |
| Sales | the product promised beyond its IA | a buyer told of a trial or a feature Perqo lacks (IA5, section 5.5) | BR-3's "What Perqo does not do"; the told line |
| Customer success | a client's approval chain configured by workaround, with groups made to stand for approvers | a reorganisation rewrites groups and policies at once (McCloskey 2014) | requests outside the IA logged as DL entries at FO-05 |
| Support | tickets with no location | signals nobody can place on the IA (IA9, section 6.2) | tags by identifier (IA9, RV-05) |
| Clients | one client's words or approval chain built into everyone's product | the org-chart risk of section 2.7 | structure as data, words as variants, requests as DL entries |
| Legal | consulted after the build | personal data shown to a role that need not see it | FO-08 consulted before the decision (DL-014) |
| Security | permissions written twice, in the matrix and in the configuration | the two drift apart (IA7, section 6.3) | permissions written once, on the calls to action |
| Leadership | the one-page map read as a plan or a promise | open gaps taken for decided | the face's "leaves out" and the open gaps on the page |

Two failures cut across every row. The first is a translation that adds a claim: a brief that says more than its source, which no one can trace back. The guard is section 1.5's rule that a cut adds nothing and a rename changes no meaning, and the face of every brief cites the source's version. The second is a function told nothing, or told too late to act. The guard is the told field and the J- list (Deliverable A, A.3).

### 4.2 · A disagreement, recorded

A function will disagree with a decision about the IA. Brown's position is that such conflict is part of design work, and he separates healthy from unhealthy conflict (Brown 2013, ch. 4, contents; practice). The IA's contribution is a record: what each function wanted, why, and what would reopen the question, so that the next person to raise it starts from the record and the loser of the argument can see that their position was heard and answered.

Perqo already has one such record, without the form. The partnerships team asked for card offers on Home and in Benefits; IA6 recorded the request and gave it neither placing, on IA3's criteria, and named the test that would settle it: whether the filtered route from each category finds offers as well as a Home banner did (IA6, B.6). Every part of a recorded disagreement is there: the function, its position, the reason it was not taken, and what would reopen it. IA9's decision log has fields for the alternatives considered and the reason for a decision (IA9, D.3), and no field for whose alternative each was.

This unit adds one (DL-011, Perqo, fictional): **positions**. For each function that disagrees with a proposed change, the entry records the function, its position in one line, its reason, and the evidence that would reopen the decision; the decision's reason must answer each position. A position not taken is kept with the entry, and its reopening test goes to IA12's assumption register when it is a test with people. The disagreement goes through IA9's routing rule unchanged: the decider is the one section 4.1 of IA9 names, and the function with the position speaks at that forum (IA9, D.1). The path has seven steps, and it adds no decider and no step to IA9's change control (IA9, D.2), only what the record holds: (1) **Object to a proposal**, any function, at its forum or in writing; (2) **Record the position** on the DL entry: function, position, reason, what would reopen it; (3) **Route to who decides** (→ see IA9, D.1); (4) **Hear the position**: the function speaks at the forum that decides; (5) **Decide, with the reason**, which answers each position; (6) **Tell the function**, through its forum and the told field; (7) **Keep the position**, when it is not taken, with its reopening test.

```viz
{"kind": "flow", "per_row": 2, "caption": "How Perqo's IA records a disagreement: from a function's objection to its position kept with the decision; supports the decision on what must be on record before a contested change counts as decided (section 4.2). The flow kind draws no branch, so the position not taken is a bracketed condition in the last step's note. Positions field set by DL-011 (this unit); routing and change control from IA9, section 4 and Deliverable D; the precedent from IA6, B.6 (the partnerships team's request). Conflict as part of design work from Brown, Designing Together, 2013 (practice). Tone 5 shared; tone 6 a stop: a position the decision did not take. Perqo is fictional.",
 "steps": [
  {"label": "Object to a proposal", "note": "any function, at its forum or in writing", "tone": 5},
  {"label": "Record the position", "note": "DL entry: function, position, reason, what would reopen it", "tone": 5},
  {"label": "Route to who decides", "note": "→ see IA9, D.1", "tone": 5},
  {"label": "Hear the position", "note": "the function speaks at the forum that decides", "tone": 5},
  {"label": "Decide, with the reason", "note": "the reason answers each position", "tone": 5},
  {"label": "Tell the function", "note": "through its forum; the told field", "tone": 5},
  {"label": "Keep the position", "note": "[not taken] kept with its reopening test", "tone": 6}]}
```

### 4.3 · A disagreement now open: who may open a receipt

Drawing the data view for legal (section 2.8) found one disagreement, logged as DL-015 (Perqo, fictional). IA7 lets every admin user see a claim, receipt included (IA7, A.1, O-07, seen by all; A.2, `receipt_file`). A therapy session is claimed under Health (IA4, B.3, BI-003), and its receipt names what was bought. Legal's position: a receipt can reveal data concerning health, so only the HR manager deciding a claim waiting in Approvals should open its receipt, and finance should see a claim's amount, category and status only. Product management's position: a claim is checked against its policy (R-09), and the HR manager deciding a claim over the limit reads the receipt to judge it (IA7, D.1, T3 and T4); any restriction must leave that reading possible. The two positions are compatible on the reading above, since HR's check happens in Approvals; the entry records both, routes the change to the IA review because it changes a role's mark in the role-by-section matrix, consults FO-08, and leaves the decision to that review. It is proposed, and no artefact changes until it is decided.

## 5 · When each function enters a Perqo cycle, and its standing duties

IA9 named, for each step of a Perqo cycle, the function that owns it, those consulted and those informed (IA9, Deliverable A), and for each review its owner and those consulted (IA9, Deliverable C). Read by function, those columns say when each touchpoint enters a cycle and what it does once the IA is in use. The reading below takes the columns as they stand; it adds only the functions this unit separates out (marketing, customer success, legal, security, leadership), whose entry points are the forums of Deliverable A.

| Function | Owns (IA9) | Consulted on (IA9) | Told of (IA9) | Forums (this unit) |
|---|---|---|---|---|
| Product management | W-05, W-07, W-15 (paths), W-16; RV-06, RV-10, RV-12 | W-01, W-04, W-06, W-09, W-10, W-12, W-17; RV-01, RV-11 | W-02, W-08, W-14 | FO-01, FO-02, FO-09 (owner) |
| Engineering | none | W-04, W-05, W-07, W-08, W-10, W-11, W-12, W-14, W-16; RV-01, RV-02, RV-06, RV-07, RV-10, RV-12 | W-01, W-03, W-06, W-09, W-17 | FO-01, FO-02, FO-08 |
| Content team | W-03, W-13 (labels, vocabulary); RV-07, RV-08 | W-02, W-06, W-08, W-10; RV-04 | W-01, W-11, W-14, W-15, W-17 | FO-01, FO-03 (owner) |
| Marketing | none | W-02 (perqo.com); RV-08 | none in IA9 | FO-03 |
| Sales | none | W-03, W-06 (perqo.com); RV-03, RV-12 | W-04, W-05, W-08, W-10, W-13, W-14, W-17 | FO-04 |
| Customer success | none in IA9 | none in IA9 | none in IA9 | FO-05 (owner), FO-07 |
| Support | W-13 (articles), W-15 (logs, tickets); RV-04, RV-05 | W-01, W-02, W-03, W-04, W-08, W-09, W-10, W-14; RV-02, RV-07, RV-11 | W-05, W-06, W-07, W-11, W-16, W-17 | FO-01, FO-06 (owner) |
| Clients | none | W-03, W-06 (Admin's labels), W-09 (participants); RV-03, RV-12 | W-10, W-14 (Admin changes), W-17 | FO-07 |
| Legal, security | none in IA9 | none in IA9 | none in IA9 | FO-08 |
| Leadership | none in IA9 | none in IA9 | none in IA9 | FO-09 |

Three readings follow. Engineering owns no step and is consulted on fifteen, which is the shape of a function that is managed closely in Rosala's terms: it reads the artefacts themselves, at F3, in every sprint. Sales owns nothing, is consulted on four and is told of seven, which is the keep-informed quadrant: it needs decisions, in words, on a cadence, and the pre-sales briefing exists to give them. And four functions appear nowhere in IA9's tables: customer success, legal, security and leadership; marketing appears only as consulted, on perqo.com's inventory. IA9 built its workflow on the course goal's six touchpoints (IA9, Deliverable, the note after the face); this unit adds the forums through which the other four enter, and DL-013 lets every face name them as readers.

## Deliverable · A · The Perqo touchpoint matrix

*Face of this artefact (IA2, the notation sheet): touchpoint matrix of Perqo, a table with a matrix figure, in four parts: A.1, one row per function, TP-01 to TP-12, with its question, artefact, fidelity, format, meeting, owner and cadence; A.2, the forums and documents, FO-01 to FO-09; A.3, who is told when each join J-01 to J-14 changes; A.4, the decision log entries DL-011 to DL-015. Fidelity F2 (complete for its scope; identifiers stable). Decision: what each function asks of the IA, what it is given, cut to what, where and how often. Readers: the IA designer, and every function named in it, each for its own row; DD-IA3 for the forums. Leaves out: named people, the meetings' length, localisation's forum (DD-IA3), the validation methods (IA11). Owner: the IA designer; version 1, dated 9 November 2026; built from IA4 to IA9 as filed on 9 November 2026; every forum and cadence set here is assumed until tested ("What later units take"); Perqo is fictional.*

### A.1 · The matrix

Every row is a Perqo convention (Perqo, fictional). Fidelity is IA2's (F1 sketch, F2 working, F3 specification); "words" means the artefact read as sentences. Owner is the function that prepares the exchange and keeps the row current. Identifiers are IA4 to IA9's and this unit's.

| ID | Function | Question | Artefact | Fidelity | Format | Meeting | Owner | Cadence |
|---|---|---|---|---|---|---|---|---|
| TP-01 | Product management | What does this change touch, and what must be decided before it is built? | interaction map and J- table (IA8, D.1, D.4); impact list (IA9, W-05) | F2, identifiers | impact list; BR-1 | FO-01 IA review; FO-09 | IA designer | each cycle; quarterly |
| TP-02 | Engineering | What objects, names, routes, permissions and rules do we build, and which can we not change alone? | relationship map with model names; addresses; role matrix; DT- tables; T1 to T6 (IA7; IA8, D.3) | F3 | tables cited in stories; BR-2 | FO-02 story check; FO-01 IA review | IA designer | each story; each release |
| TP-03 | Content team | What is each thing called on each surface, where does each page live, and which template fills it? | vocabulary; taxonomy; inventory; templates (IA4, B; IA5, A and C) | F2 vocabulary; F3 inventory | inventory rows; vocabulary table | FO-03 vocabulary review | content team | quarterly; each rename |
| TP-04 | Marketing | What does a buyer see first, under which labels, and where do campaigns and indexing go? | sitemap cut to two levels; label table; URL, redirect, indexed columns (IA5) | F1 or F2 | two-level sitemap | FO-03 vocabulary review | IA designer | quarterly; each campaign |
| TP-05 | Localisation | What key does every language version share, and what changes by market? | inventory IDs; localisation column (IA5, C) | F3 | inventory and catalogue columns | none yet (DD-IA3) | content team | [when a second language is added] |
| TP-06 | Sales | How do we tell the story, run the demo and answer a tender truthfully? | CL-1 to CL-6; DT- rules in words; surfaces map; role matrix in words (IA8; IA7, B) | F1 story; F2 rules | BR-3; demo path | FO-04 pre-sales briefing | IA designer | monthly; each rule change |
| TP-07 | Customer success | How should this client be configured, and what does each admin user need to learn? | onboarding order; role matrix (IA8, 3.2; IA7, B); DT-1, DT-2 tables; H-1 articles | F2 | configuration workbook; training paths | FO-05 onboarding handover | customer success | each new client; each renewal |
| TP-08 | Support | Where is this person, why did this outcome happen, and where does the structure fail? | ticket tags; where-things-go-wrong table (DT- stops, T1, T4, T5, EX-, G-) | F3 identifiers | tag list; table | FO-06 ticket and log read; FO-01 | support | monthly; quarterly logs |
| TP-09 | Clients | Do these words, roles and rules fit our people, and what changes for our staff? | word list; role matrix; DT-2 in words; release note | F1 words; F2 roles | session materials; release note | FO-07 validation session; FO-02 | IA designer, with customer success | each cycle touching Admin; each release |
| TP-10 | Legal | What personal data does each object hold, who sees it, and what is recorded? | data view (IA7, A.2 with data category and roles); O-17 | F3 | data view | FO-08 privacy and security review | IA designer | each data or role change; quarterly |
| TP-11 | Security | Which role may see and do what, and is every permission written once? | role matrix with calls to action (IA7, B, A.4) | F3 | matrix and table | FO-08 privacy and security review | IA designer | each role change |
| TP-12 | Leadership | What is the system, where is it weak, and what is decided and open? | one-page map: whole interaction map, G-5 to G-7, IA debt, decisions | F1 | one page | FO-09 leadership quarterly | product management | quarterly, after RV-10 |

The matrix as a figure, its columns the five that carry a mark per row (the question, owner and full artefact are in the table).

```viz
{"kind": "matrix", "caption": "The Perqo touchpoint matrix: for each function, the artefact it is given, at what fidelity, in what format, in which forum and how often; supports the decision on what each part of the business receives from the IA (Deliverable A, A.1; sections 2.1 to 2.9). The question, owner and full artefact of each row are in table A.1. Artefacts and fidelities from IA2's decision table, IA5, section 6, IA7, Deliverables A to D, IA8, D.1 to D.5 and IA9, Deliverables A and C; forums from A.2; the format follows the function's place in Rosala's power-interest matrix (NN/g, 2021). Every row tone 5, shared. Perqo is fictional.",
 "cols": ["Artefact", "Fidelity", "Format", "Meeting", "Cadence"],
 "rows": [
  {"label": "Product management", "tone": 5, "cells": ["interaction map and J- table", "F2, identifiers", "impact list; BR-1", "FO-01 IA review; FO-09", "each cycle; quarterly"]},
  {"label": "Engineering", "tone": 5, "cells": ["relationship map with model names", "F3", "tables cited in stories; BR-2", "FO-02 story check; FO-01 IA review", "each story; each release"]},
  {"label": "Content team", "tone": 5, "cells": ["vocabulary; taxonomy; inventory; templates", "F2 vocabulary; F3 inventory", "inventory rows; vocabulary table", "FO-03 vocabulary review", "quarterly; each rename"]},
  {"label": "Marketing", "tone": 5, "cells": ["sitemap cut to two levels", "F1 or F2", "two-level sitemap", "FO-03 vocabulary review", "quarterly; each campaign"]},
  {"label": "Localisation", "tone": 5, "cells": ["inventory IDs; localisation column", "F3", "inventory and catalogue columns", "none yet (DD-IA3)", "[when a second language is added]"]},
  {"label": "Sales", "tone": 5, "cells": ["CL-1 to CL-6; DT- rules in words", "F1 story; F2 rules", "BR-3; demo path", "FO-04 pre-sales briefing", "monthly; each rule change"]},
  {"label": "Customer success", "tone": 5, "cells": ["onboarding order; role matrix", "F2", "configuration workbook; training paths", "FO-05 onboarding handover", "each new client; each renewal"]},
  {"label": "Support", "tone": 5, "cells": ["ticket tags; where-things-go-wrong table", "F3 identifiers", "tag list; table", "FO-06 ticket and log read; FO-01", "monthly; quarterly logs"]},
  {"label": "Clients", "tone": 5, "cells": ["word list; role matrix; DT-2 in words", "F1 words; F2 roles", "session materials; release note", "FO-07 validation session; FO-02", "each cycle touching Admin; each release"]},
  {"label": "Legal", "tone": 5, "cells": ["data view", "F3", "data view", "FO-08 privacy and security review", "each data or role change; quarterly"]},
  {"label": "Security", "tone": 5, "cells": ["role matrix with calls to action", "F3", "matrix and table", "FO-08 privacy and security review", "each role change"]},
  {"label": "Leadership", "tone": 5, "cells": ["one-page map", "F1", "one page", "FO-09 leadership quarterly", "quarterly, after RV-10"]}]}
```

### A.2 · The forums and documents

Each forum is a meeting or a document (Perqo, fictional). FO-01, FO-02, FO-03 and FO-06 hold IA9's reviews and documents under one name each; the other five are set here. Each row gives what DD-IA3 needs to extend it: who chairs or writes it, who takes part, what goes in, what comes out, and when.

| ID | Forum or document | Kind | Chair or writer | Takes part | Inputs | Outputs | When |
|---|---|---|---|---|---|---|---|
| FO-01 | IA review (IA9, section 4.1) | meeting | IA designer | product management, engineering, content team, support | DL entries routed to it; J- and X- rows (RV-03) | DL entries decided, with positions answered | each release touching two surfaces; quarterly; when a change is routed to it |
| FO-02 | Story check and release note (IA9, RV-01, RV-02, W-14) | documents | IA designer (check); engineering (note) | product management, engineering, support; clients read the note | stories citing identifiers; DL entries applied | stories held or passed; the release note's IA changes, with Admin changes for clients | each story; each release |
| FO-03 | Vocabulary and content review (IA9, RV-07, RV-08) | meeting | content team | support, engineering, marketing, page owners | new variants from FO-06; a slice of the inventory | DL entries; synonyms loaded; inventory rows updated | quarterly; on a new variant or before a redesign |
| FO-04 | Pre-sales briefing | meeting | IA designer, with product management | sales | BR-3; DL entries whose told line names sales; questions from tenders | BR-3 re-issued when its source changed; questions logged as proposed DL entries | monthly; and within a week of a decision that changes a rule or perqo.com |
| FO-05 | Onboarding handover | meeting and document | customer success | the client's account owner; the IA designer when a request touches the IA | the configuration workbook; training paths; the client's requests | the workbook agreed; requests logged as proposed DL entries | each new client (CL-3 to CL-4); each renewal (CL-6) |
| FO-06 | Ticket and log read (IA9, RV-04, RV-05) | meeting | support | IA designer, content team | ticket tags; the Help centre's search logs | hypotheses for IA11; variant terms for FO-03 | monthly (tickets); quarterly (logs) |
| FO-07 | Client validation session | meeting | IA designer | admin users from at least two clients; customer success | word lists; the role matrix; DT-2 in words; candidate structures | words and roles confirmed or logged; test results (IA11) | in each cycle touching Admin's labels or roles (IA9, W-06, W-09) |
| FO-08 | Privacy and security review | meeting | IA designer | legal, security, engineering | the data view; the role matrix; proposed DL entries that add personal data or change a role's mark | positions recorded on the entry before it is decided (DL-014) | each such entry; quarterly |
| FO-09 | Leadership quarterly | document, then meeting | product management | leadership; IA designer | the one-page map; RV-10's debt count; decisions of the quarter | questions logged as proposed DL entries | quarterly, after RV-10 |

FO-07 takes admin users from at least two clients, so that one client's words or structure are heard beside another's (section 2.7).

### A.3 · Who is told when a join changes

IA8's rule is that a change to any identifier in a J- row is not done until the other cells of that row have been checked (IA8, D.5). The decision log's told field records who heard of it (IA9, D.3). This table joins them: for each join, the functions beyond the IA review's members who must be told when it changes, and the forum that tells them (Perqo, fictional; DL-012).

| Join (IA8, D.4) | Told | Through |
|---|---|---|
| J-01 status | customer success; clients | FO-02 release note; FO-05 |
| J-02 limit | sales; customer success; clients | FO-04; FO-05; FO-02 |
| J-03 Claims | clients | FO-02 |
| J-04 Approvals | customer success; clients; legal | FO-05; FO-02; FO-08 |
| J-05 invite | customer success; clients | FO-05; FO-02 |
| J-06 Purchase | clients; legal | FO-02; FO-08 |
| J-07 decline | clients | FO-02 |
| J-08 categories | sales; marketing; customer success; clients | FO-04; FO-03; FO-05; FO-02 |
| J-09 card | customer success; clients; security | FO-05; FO-02; FO-08 |
| J-10 contract | sales; customer success; legal; leadership | FO-04; FO-05; FO-08; FO-09 |
| J-11 sign-in | marketing; security | FO-03; FO-08 |
| J-12 demo | sales; marketing | FO-04; FO-03 |
| J-13 rule words | sales; customer success | FO-04; FO-05 |
| J-14 budgets | customer success; clients | FO-05; FO-02 |

### A.4 · Decision log entries

The changes this unit makes to how Perqo's IA is kept, in IA9's format (IA9, D.3; Perqo, fictional). Each is proposed at the date of this unit and is decided where the Decided by column says.

| ID | Change | Raised by, from | Touches | Decided by | Status |
|---|---|---|---|---|---|
| DL-011 | The decision log gains a field, positions: for each function that disagrees, its position, reason and what would reopen the decision; the decision's reason answers each position | IA10, section 4.2; the precedent of IA6, B.6 | IA9, D.3 (the log's fields) | IA designer (inside the log; renames nothing) | proposed |
| DL-012 | The told field names, for each function told, the forum or document (FO-) and the date; A.3 is the list of who is told when each join changes | IA10, section 5 and A.3 | IA9, D.3; IA8, D.4 | IA designer | proposed |
| DL-013 | The face's Readers field may name any of the twelve functions TP-01 to TP-12; IA2's six touchpoints are kept as groups | IA10, section 1.1 | IA2, the notation sheet; every face, by dated amendment | IA review (a field every artefact carries) | proposed |
| DL-014 | A proposed change that adds an attribute holding personal data, or changes a role's mark, is consulted at FO-08 before it is decided; the decider stays the one IA9, D.1 names | IA10, section 2.8 | IA9, D.1 and D.2 | IA review; product management signs off (a rule on routing) | proposed |
| DL-015 | Only the HR manager deciding a claim waiting in Approvals opens its receipt; finance sees a claim's amount, category and status only. Positions: legal (health data in receipts); product management (HR reads the receipt to decide, R-09) | IA10, section 4.3, from the data view | IA7, A.1 (O-07), B; IA8, J-04 | IA review, after FO-08 | proposed |

## Deliverable · B · Three one-page IA briefs

*Face of these artefacts (IA2, the notation sheet): three IA briefs, BR-1 for product management, BR-2 for engineering, BR-3 for sales, each a translation (section 1.5) of the same source: IA4, Deliverable A (amended 9 November 2026), IA5, Deliverables A to C (version 1, 3 November 2026), IA6, Deliverables A to C (amended 9 November 2026), IA7's Deliverable (amended 9 November 2026), IA8's Deliverable (version 1, 9 November 2026) and IA9's Deliverable (version 1, 9 November 2026). Form after Brown's design brief (Communicating Design, 2nd ed., 2011, ch. 9; practice), written for one function each. Fidelity: BR-1 F2, BR-2 F3 by reference, BR-3 F1 with the rules at F2. Decision: what each function must know of the IA to do its own work. Leaves out: everything its reader does not need, as each brief's last section says. Owner: the IA designer; version 1, dated 9 November 2026; re-issued when its source changes; Perqo is fictional.*

### BR-1 · Perqo IA brief for product management

**What this is.** One page on Perqo's IA for product management: what it holds, how to read the impact of a change, what is open and where you decide. Source versions are on the face; Perqo is fictional.

**The system, as layers.** Three surfaces and a merchant side. perqo.com sells and helps (52 rows after the redesign; IA5). Perqo Admin is where a client's HR and finance managers configure and decide (pages AD-0 to AD-6; IA7). The Perqo app is where employees see balances, pay and claim (screens A-0 to A-5; IA6). Two lifecycles run across them: the client's, CL-1 Evaluate to CL-6 Renew or churn, and the employee's, EL-1 Enrol to EL-6 Review, each period. Three rules decide what happens: DT-1 eligibility, DT-2 approval routing, DT-3 spend limits. Fourteen joins, J-01 to J-14, tie the layers (IA8).

**How to scope a change.** Before estimating, list what it touches by identifier: surfaces and pages (S-, AD-, A-, H-), objects and relationships (O-, R-), joins (J-), rules (DT-). That list is the impact list (IA9, W-05). A change that touches a rule or two surfaces goes to the IA review, and you sign it off; a change that renames a label goes to the IA review with the vocabulary changed first; anything inside one surface that renames nothing, the IA designer decides (IA9, D.1). A story enters a sprint only when the artefact it builds from is at F3 for its part (IA9, Deliverable B).

**What already constrains the roadmap.** A new top-level benefit category is a product decision with finance and the client, because it creates an allocation for every employee in every group that opens it (IA4, R8). The benefits taxonomy keeps two levels (R7). Invite employees stays unavailable for a group until its budgets for the period are set (IA8, section 3.2). Admin has no global search; each long list has a find field (IA7, section 4.5). Roles cover the whole client; scoping a role to some groups is open (IA7).

**What is open, with an owner.** G-5, how a leaver learns of a claim decided after they left; G-6, which allocations an employee keeps when moved to another group mid-period; G-7, money unspent at a period's end (IA8). DL-015, who may open a claim's receipt, is proposed and awaits the IA review after FO-08. The account owner's tasks have no Help centre article.

**What you own.** The impact list (W-05), the story map's backbone under the IA's identifiers (W-07), analytics paths (W-15, RV-06), IA debt triage each quarter (RV-10), the rules review on trigger (RV-12), and the leadership page (FO-09).

**Where you will hear.** FO-01, the IA review; FO-02, the release note; the decision log's told line. This brief leaves out model names, screens and labels (BR-2 and the vocabulary hold them) and sales' words (BR-3).

### BR-2 · Perqo IA brief for engineering

**What this is.** One page on Perqo's IA for engineering: what the F3 artefacts hold, which names are fixed, which you may not change alone, and what is open. Every element is cited by identifier; the tables named are the specification. Perqo is fictional.

**Objects and names.** The model names are IA7's (A.2): `client`, `admin_user`, `employee_group`, `policy`, `employee`, `allocation`, `transaction` (type claim or card payment), `card`, `catalogue_item`, `audit_entry`; IA8 added `card_decline` (O-18), outside the transactions. One table, two objects: claims and card payments are one `transaction` table with a type field, and two objects in every surface (IA7, section 6.1). Remaining is computed as amount less spent and stored nowhere; spent counts approved and paid claims and card payments, never a waiting claim (IA7, A.2). Proposed names still to confirm: `closed` on the allocation and `contract_end_date` on the client (IA9, D.3: DL-005, DL-006).

**One thing, several labels.** The model keeps `allocation`; Admin says Budget, the app Balance, perqo.com Benefits budget (IA8, D.1). Labels are recorded translations of the model name, never a second concept; use the model name in code, tickets and conversation (IA7, section 6.2).

**Rules and transitions.** Build from the tables, Unique hit policy: DT-1 (five rows), DT-2 (five rows, with T1 to T5), DT-3 (four rows) (IA8, D.3). The claim moves only by T1 to T6, each writing an audit entry; no transition leaves Rejected or Paid (IA7, D.1). EX-1: an HR manager never decides their own claim. EX-2: on HR's approval the balance is checked again (T5).

**Routes and addresses.** Addresses put the identifier first: Admin's /employees/{employee ID} and its kin (IA7, C.1); the app's perqo.com/app/ entries E-1 to E-8 (IA6, B.4); perqo.com's category pages /product/benefits/cat-hea/health (IA5). A moved page keeps a redirect. Analytics record each app screen and Admin page by identifier (IA9, section 6.3).

**Permissions.** Written once, on the calls to action (IA7, A.4); the role-by-section matrix and the access-control configuration are both read from them (IA7, B; section 6.3). Hidden, disabled with a reason, or read only: IA7, B.2.

**Events and APIs (proposed).** A resource takes the object's model name; an event takes the model name and the state entered. The strings are yours.

**What you may not change alone.** An identifier, a label, a model name that a label maps to, a rule's outcome, a transition: each is a DL entry through the IA review (IA9, D.1), vocabulary first. Every story cites the identifiers it touches (IA9, section 2.3).

**Open.** G-5 to G-7 (IA8); DL-015 may change who opens `receipt_file`. This brief leaves out sales' words, the lifecycles' business stages and visual design.

### BR-3 · Perqo IA brief for sales

**What this is.** One page on how Perqo is put together, in the words a buyer meets, with the rules you can say and the things you must not promise. Perqo is fictional.

**The story in one paragraph.** A client gives each employee a benefits budget, per category (Health, Learning, Mobility, Meals) and per period. HR and finance set it up in Perqo Admin: teams and groups, each with its policy (which categories are open, the auto-approve limit, what is covered), then budgets. Employees join from an invitation, see what's left in each category in the Perqo app, and spend it two ways: with the Perqo card at the till, or by paying another way and making a claim. Reports show spend by category, by group and by budget use.

**The rules, in words** (IA8, D.3; the Help centre says the same, H-1.2.5).
- Approvals: "A claim within the category's balance and at or under your limit is approved at once; over the limit, one of your HR managers decides, never the person claiming, and Perqo checks the balance again when they approve."
- Spending: a card payment is taken at the till if the card is active, the category is open and the budget covers it; otherwise it is declined, and the employee is told why unless the card was cancelled.
- Who can spend: an employee spends in a category only when the contract is in force, they have joined, the category is open to their group and its budget for the period is set.

**How a client starts** (CL-1 to CL-6, IA8). Evaluate on perqo.com; a demo (there is no free trial); a contract; onboarding in Admin, in order: admin users, groups and policies, budgets, invitations; then each period runs. Renewal sets a new contract end date; at churn, sign-in ends and cards are cancelled the day after it.

**The demo path.** Product (S-1); a policy's open categories and limit (AD-3.1); Set budgets (AD-2.2); Invite employees (AD-1.3); Join (A-0.1); Home (A-1); a claim over the limit (A-3.1); Approvals (AD-4); the approved claim (A-3.4); Budget use (AD-5.3).

**For tenders.** Roles: HR managers decide claims and manage employees and policies; finance managers set budgets and see all five reports; one account owner manages company details and admin users and reads the Activity log. Every change is recorded with who, what, before and after. Each client has at least two HR managers. Security page: S-1.5. Data and privacy questions go to legal through FO-08.

**What Perqo does not do.** No self-serve sign-up and no free trial; perqo.com in English only; no search across Admin; no Approvals for finance; roles cannot be limited to some groups; merchants have no surface of their own beyond accepting the card and publishing offers; unspent money at a period's end and mid-period moves between groups are not yet decided. Pricing: two plans, each with a published price per employee per month (Pricing, S-2).

**Where you will hear of changes.** FO-04, monthly, and within a week of a decision that changes a rule or perqo.com. This brief leaves out model names, counts and screens' states.

## What later units take

**IA11** tests what this unit sets. Every practice is assumed, with its test:

| Practice or assumption | Where | Test (IA11) | What changes if it fails |
|---|---|---|---|
| Each function's question is the one it asks | section 2; A.1 | interviews with each function, asking what decision it last needed the IA for | the question and artefact in that row |
| Sales can explain the rules from BR-3 | BR-3; section 3.2 | IA8's test: sales explains DT-2 to a buyer in a recorded demo, and the buyer restates it | the rules' words, or BR-3's order |
| Engineering can build from BR-2's references without a meeting | BR-2 | the questions engineering raises at FO-02, counted per release | BR-2's sections, or the F3 tables it points to |
| The translation loses nothing a reader needs | section 3.2 | ask each reader a question answerable from the source only, with only the brief in hand (after IA8, D.5's test) | the cut |
| Positions recorded reduce reopened decisions | DL-011 | DL entries reopened or superseded within a quarter, before and after, read at RV-10 | the positions field |
| Clients' structure enters as data without loss | section 2.7 | interviews with account owners at FO-05; configuration requests logged per client | employee groups, or role scoping (left free) |

**IA12** delivers an IA when inputs are missing. The touchpoint matrix names which function's input is missing when one is: a row whose forum has not met, or whose function has not been consulted, is an input IA12's assumption register marks as absent, with the function named and the test from the table above.

**DD-IA2** writes the business case. It takes BR-3 and the leadership page (FO-09) as two of its audiences, and the touchpoint matrix as the list of functions a case for IA work must speak to.

**DD-IA3** takes the forums FO-01 to FO-09 as the governance forums it extends for several languages and markets, TP-05 as the localisation row it brings to life, and DL-011 to DL-015 as the log's state at this unit's date.

## Perqo facts set by this unit

Every fact below is a course convention (Perqo, fictional), never evidence about the world. Each keeps every registered fact; none renames an IA1 to IA9 label, object, attribute or relationship.

| Fact | Set in | Left free |
|---|---|---|
| Twelve functions touch the IA: product management, engineering, content team, marketing, localisation, sales, customer success, support, clients, legal, security, leadership | section 1.1; A.1 | named people |
| Perqo's setup staff (IA8, section 3.2) are the customer success team, which sets up the client and account owner at CL-3 and supports the account owner through CL-4 and CL-5 | section 2.5 | the team's size |
| Localisation has no forum until a second language is added | section 2.3; TP-05 | its forum (DD-IA3) |
| Rows TP-01 to TP-12 with question, artefact, fidelity, format, meeting, owner and cadence | Deliverable A, A.1 | none |
| Forums and documents FO-01 to FO-09; FO-01, FO-02, FO-03 and FO-06 hold IA9's reviews; FO-07 takes admin users from at least two clients | Deliverable A, A.2 | the meetings' length |
| Who is told when each join J-01 to J-14 changes, and through which forum | Deliverable A, A.3 | none |
| The demo path: S-1, AD-3.1, AD-2.2, AD-1.3, A-0.1, A-1, A-3.1, AD-4, A-3.4, AD-5.3 | section 2.4; BR-3 | the demo's data |
| A configuration workbook per client; training paths by role from the H-1 articles (HR: H-1.2.1, H-1.2.2, H-1.2.3, H-1.2.5, H-1.3.1; finance: H-1.1.1, H-1.1.2) | section 2.5 | the workbook's layout |
| Open fault: no Help centre article covers the account owner's tasks | section 2.5 | the article (support) |
| The where-things-go-wrong table for support | section 2.6 | none |
| The data view for legal: IA7's attributes with data category and the roles that see each | section 2.8 | the categories' names |
| Event naming, proposed for engineering to confirm: a resource takes the model name, an event the model name and the state entered | section 2.2; BR-2 | the strings |
| The one-page map for leadership: the whole interaction map, G-5 to G-7, the IA debt count, the quarter's decisions | section 2.9 | none |
| Briefs BR-1 to BR-3, re-issued when their source changes | Deliverable B | none |
| Decision log entries DL-011 to DL-015, proposed | Deliverable A, A.4 | their decisions |

## Sources

- Berkun, Scott. "Book review: Designing Together". scottberkun.com, 27 June 2013 (reproduces his foreword; practice). [scottberkun.com, review](https://scottberkun.com/2013/book-review-designing-together/)
- Brown, Dan M. *Communicating Design: Developing Web Site Documentation for Design and Planning*. 2nd ed. New Riders, 2011 (published September 2010). Preface; ch. 2 contents; ch. 8, "Deliverable Basics"; ch. 9, "Design Briefs" (practice). [oreilly.com, preface](https://www.oreilly.com/library/view/communicating-design-developing/9780131385399/pr02.html); [oreilly.com, contents](https://www.oreilly.com/library/view/communicating-design-developing/9780131385399/bk01-toc.html); [oreilly.com, ch. 8](https://www.oreilly.com/library/view/communicating-design-developing/9780131385399/ch08.html); [oreilly.com, ch. 9](https://www.oreilly.com/library/view/communicating-design-developing/9780131385399/ch09.html)
- Brown, Dan M. *Designing Together: The Collaboration and Conflict Management Handbook for Creative Professionals*. New Riders, June 2013. Contents and publisher's description; Part II opening; ch. 7 opening (practice). [oreilly.com, Designing Together](https://www.oreilly.com/library/view/designing-together-the/9780133390957/); [oreilly.com, Part II](https://www.oreilly.com/library/view/designing-together-the/9780133390957/part02.html); [oreilly.com, ch. 7](https://www.oreilly.com/library/view/designing-together-the/9780133390957/ch07.html)
- Colyer, Adrian. "How do committees invent?" the morning paper, 13 December 2019 (summary of Conway 1968, quoted for Conway's thesis). [blog.acolyer.org, Conway](https://blog.acolyer.org/2019/12/13/how-do-committees-invent/)
- Conway, Melvin E. "How Do Committees Invent?" *Datamation*, 1968 (not read; quoted through Colyer 2019).
- European Union. Regulation (EU) 2016/679 (General Data Protection Regulation), Article 9, as adopted (legal text). [legislation.gov.uk, GDPR art. 9](https://www.legislation.gov.uk/eur/2016/679/article/9/adopted)
- McCloskey, Marieke. "Intranet Information Architecture (IA) Trends". Nielsen Norman Group, 23 February 2014. [nngroup.com, intranet IA trends](https://www.nngroup.com/articles/intranet-information-architecture-ia/)
- Rosala, Maria. "Stakeholder Analysis for UX Projects". Nielsen Norman Group, 18 April 2021. [nngroup.com, stakeholder analysis](https://www.nngroup.com/articles/stakeholder-analysis/)
- Spencer, Donna. "Why are intranets structured like the organisational chart?" Step Two, 3 April 2005 (practice). [steptwo.com.au, org chart](https://www.steptwo.com.au/papers/cmb_orgchart/)
- Cited through the filed units, for claims made there: Chisnell, "Call centers as a source of data", 2016 (IA9; practice); Design Council, "Framework for Innovation", checked 9 November 2026 (IA9); Evans, *Domain-Driven Design Reference*, 2015 (IA7); Garrett, *The Elements of User Experience*, 2nd ed., 2011, ch. 2 (IA9); Google Search Central, "URL Structure Best Practices" and "Redirects and Google Search", 2026 (IA5; vendor documentation); Tankala, "Information Architecture vs. Sitemaps", NN/g, 2023 (IA1). Full references in IA1, IA5, IA7 and IA9, Sources.

## Unsure list

- Brown 2011, ch. 2: only the section headings "Challenges in Communicating Design" and "Presenting Design" were seen; nothing is drawn from their text.
- Brown 2011, ch. 8: the opening definition was read through a page summary that gave "facilitate" misspelled; the unit quotes only "capture decisions, and stimulate conversation".
- Brown 2013, chs 4 and 5: "Healthy vs. Unhealthy Conflict" and the sources of conflict are section headings only; the four virtues of chapter 8 could not be read and are not named.
- Brown 2013: the counts of techniques and diagnoses are from the publisher's description; the book's text behind them was not seen.
- Conway 1968: the quotation and the year are as Colyer gives them; the month, pages and original wording were not checked.
- GDPR Article 9(1): "data concerning health" is from knowledge of the text; the fetched page was summarised and confirmed health data among the categories without giving the phrase.
- McCloskey 2014: the quotations were read through a page summary; the 77 intranets are the report's sample, and the finding is about intranets, applied to a backoffice on this unit's reading.
- Rosenfeld, Morville and Arango 2015, ch. 13, has a section "Guidelines for Diagramming an Information Architecture"; its text was not seen and is not used.
- The owner counts (section 2.3) assume each row counted once under its first-named owner; IA5 does not say how to count shared ownership.
- Object: the Perqo touchpoint matrix, sections 2 and 5 and Deliverable A
