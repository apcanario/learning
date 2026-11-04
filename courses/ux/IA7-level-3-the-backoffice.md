---
code: IA7
title: Level 3 · the backoffice
course: ux · IA · Information Architecture
model: Opus 5.5
written: 2026-11-03
search: off
---

# IA7 · Level 3 · the backoffice

IA5 built the IA of perqo.com, a shallow website, and IA6 the IA of the Perqo app, a small task-driven app. This unit builds the third surface, Perqo Admin (Perqo, fictional), the backoffice where a client company's HR and finance managers configure budgets, policies, approvals and reports. IA1 called it "object-heavy" and said that "permissions decide what each role sees", and that a sitemap of it "would list its areas and miss most of its structure" (IA1, section 5). This unit covers what makes a backoffice's IA different from a website's or an app's, object-relationship mapping for a system of many linked entities, roles and permissions as a layer of the IA, enterprise navigation built on lists, details and work queues, a state diagram for each object that has a lifecycle, and the boundary between the IA and the engineering data model. The deliverable is the Perqo Admin IA: the object-relationship map, the role-by-section matrix, the navigation model and the claim-approval state diagram.

Every figure uses IA2's notation (IA2, section 5 and the notation sheet). Admin's boxes take tone 4, Perqo Admin; on a figure of one surface every box takes that surface's tone (IA2, section 5.2). Two figures add tones of their own, and say so where they are drawn: the claim's state diagram keeps IA2's tone 5 for the statuses both Admin and the app show, and tone 6, IA2's stop, marks a path that ends without success.

The filed units and the brief handed this one the questions below by name; a search of the vault and the register for "IA7" found one more, the last row. Where each is answered:

| Handed on by | The question | Answered in |
|---|---|---|
| IA4, Deliverable A ("What IA7 may do with it"; "What the map hands on"); the brief's last sentence | extend the object map for Admin to F3, with permissions, model names, roles, volumes, lifecycles and work queues; keep O-01 to O-16 and R-01 to R-20; rename nothing | section 2; Deliverable A |
| IA4, A.3 | who triggers client -> edit company details and admin user -> add | section 3.4; Deliverable A, A.4 |
| IA4, A.1; IA6, section 6.2 | Admin's name for card (O-09) and notification (O-10) | section 2.3; Deliverable A, A.1 |
| IA4, section 4.3 | Reports as a view in Admin's navigation model | section 4.6; Deliverable C |
| IA2, decision table and section 5.3 | the navigation model, the object-relationship map and the state diagram for Admin, at the fidelity IA2 names, in the course notation | Deliverables A, C and D |
| IA5, section 5.5 and its register row; IA6, section 6.3 and B.4 | the line on Admin's sign-in screen pointing employees to Get the Perqo app: taken, changed or refused | Deliverable C, C.5 |
| IA6, B.4, E-2 | Admin's side of HR's invitation | section 5.1; Deliverable C, C.4 |
| IA1, surfaces map | Admin's six top-level areas as the start of its navigation model | section 4.1; Deliverable C |
| Register (claim lifecycle and rule); IA6 (rejection reason) | the claim-approval state diagram extends IA2's and IA1's and contradicts nothing | section 5.2; Deliverable D |
| Register, "Not yet set" | roles beyond HR manager and finance manager, volumes, Admin's pages below the top level, numbers | sections 2.2, 3.4; Deliverables A and C; "Perqo facts set by this unit" |
| IA4, Deliverable A's face; IA6, Deliverable C's face | Admin's permissions and data-model mapping at F3; Admin's screens | Deliverables A, B and C |

## 1 · What makes a backoffice different

### 1.1 · Five differences

A sales website is read by visitors who may never come back; an employee app is opened a few times a month (IA3, section 6.2, assumed). A backoffice is the tool someone uses to do their job. Kate Kaplan's NN/g guidelines for complex applications start from a definition NN/g had given before: "any application supporting the broad, unstructured goals or nonlinear workflows of highly trained users in specialized domains". Such applications "support highly trained users with specialized knowledge", help them "navigate and manage large underlying data sets", and have end users "relying on them for their work"; some users spend "years or even decades using the same system", and "users often do not follow a known, sequential set of subtasks" to reach their goal ("8 Design Guidelines for Complex Applications", Nielsen Norman Group, 8 November 2020, [nngroup.com, complex applications](https://www.nngroup.com/articles/complex-application-design/); NN/g guidance).

Read for its IA consequences, that definition gives five differences. Each is set against the app here, because IA6 is the unit the reader has just finished.

| Difference | Perqo app (IA6) | Perqo Admin (Perqo, fictional) | What it changes in the IA |
|---|---|---|---|
| Many entity types | eight objects with the employee's calls to action (IA6, Deliverable A, A.2) | ten of IA4's objects shown, one not shown, and one added here (Deliverable A) | the object-relationship map is the main artefact; a sitemap misses most of the structure (IA1, section 5) |
| Roles and permissions | one role, the employee | HR manager, finance manager and, from this unit, account owner | a role layer decides what each person sees, does and reaches (section 3) |
| Volumes | one person's own claims and purchases | every employee, claim and allocation of a client (section 2.2) | lists with filters, find and bulk actions; work queues (section 4) |
| Workflows | short tasks, begun from Home or a notification (IA6, section 3.2) | decisions that wait on a person, and changes many people depend on | a state diagram per lifecycle; approvals, exceptions and an audit trail (section 5) |
| Users paid to be there | an employee who opens the app a few times a month (IA3, section 6.2, assumed) | managers who use Admin daily (IA3, section 6.2, assumed) | the IA can ask more learning of its users, in exchange for speed on repeated work (section 1.2) |

### 1.2 · Sovereign posture, and the people paid to be there

Alan Cooper and his co-authors give the last difference a name. Their chapter "Platform and Posture" describes a product's posture as its behavioural stance: how much of a person's attention it asks for and for how long (*About Face: The Essentials of Interaction Design*, 4th ed., Wiley, 2014, ch. 9, pp. 205 to 236, sections "Product Postures" and "Postures for the Desktop"; contents at [e-bookshelf.de](https://wiley-vch.e-bookshelf.de/about-face-2765056.html)). A sovereign-posture product holds a person's attention for long, continuous stretches and is the main tool of their working day; a transient-posture product is called up for one function and put away. In the chapter's argument, the users of a sovereign product spend so long in it that they stop being beginners quickly, so the design can favour efficiency for people who know it: the whole screen, dense information, a restrained visual style (ch. 9). The next chapter, "Optimizing for Intermediates", makes the general point: most people who use a product regularly become and stay intermediates, neither beginners nor experts, and a product should be built for them (ch. 10, section "Perpetual Intermediates", p. 238).

Perqo's two product surfaces sit at opposite ends (Perqo, fictional). The app, opened a few times a month, is transient: IA6 built it on a tab bar, with everything needed reachable from where the person is and a direct route to the task that usually follows (IA6, sections 3.5 and 1.2). Admin, used daily by the same HR and finance managers (IA3, section 6.2, assumed), is sovereign. IA3 already drew the consequence for labels: Krug's case for labels that need no thought was made about websites met by occasional visitors, and a backoffice "can ask more of its users' learning" (IA3, section 6.2). Cooper's argument is practice from a standard work, not a measured finding, and this unit uses it as practice.

### 1.3 · What sovereign posture does not license

Two limits keep the argument honest. The first: a user who learns a structure still needed it to be learnable. Admin's users are domain experts in HR and finance, not in Perqo, so its labels must be the client's own words for its own things (employee group, policy, budget), which is what IA1's vocabulary already set (IA1, Deliverable). The second: posture is about attention and screen, and it says nothing about who may see what. A sovereign product with many users in different jobs needs the role layer of section 3 more than a transient one does, because the person spending all day in it will reach every route it shows them.

## 2 · Object-relationship mapping for a backoffice

### 2.1 · From the object map to the object-relationship map

IA2 drew two grades of the same artefact: an object map lists the objects with their attributes and actions; an object-relationship map adds the lines between them, each with a verb and a count at each end, in UML's multiplicity notation (IA2, section 1.5; Object Management Group, *Unified Modeling Language* 2.5.1, 2017). Its decision table gives the object-relationship map F2 in design and F3 "as the agreed mapping to the data model", and assigns it to this unit (IA2, Deliverable). IA4 drew Perqo's map across every surface at F2 with counts, from Sophia V. Prater's object-oriented UX method (nouns into objects, core content, nesting, calls to action; Prater, "Object-Oriented UX", A List Apart, 2015, and "OOUX: A Foundation for Interaction Design", A List Apart, 2016, both practice; IA4, section 4.1), and handed this unit the Admin part to take to F3 with permissions and model names (IA4, Deliverable A).

A backoffice asks four more things of each object than an app does, and the brief names them: roles, volumes, lifecycles and work queues. They are this unit's columns, added to IA4's, and each answers a design question the map cannot otherwise answer.

- **Roles: who may see it and who may change it.** The answer is the role layer (section 3), recorded on the object so that every screen showing the object inherits it.
- **Volumes: how many there are, and how fast they arrive.** A thing with three instances is a short page; a thing with a thousand is a list that needs order, filters and find (this unit's rule; the table guidance is Laubheimer 2022, section 4.3). Volumes are assumptions until measured, and are labelled so.
- **Lifecycle: whether it changes state.** An object with states gets a state diagram (section 5.1); one without needs only its attributes.
- **Work queue: whether anyone must act on some of them.** A queue is a list of one object filtered by state and owned by a role (section 4.2). Recording it on the object says where the work for that object waits.

F3 adds two things IA2 set for the grade: a stable identifier on every element, and each object's model name beside its label (IA2, sections 1.0 and 1.5). IA4's identifiers, O-01 to O-16 and R-01 to R-20, are kept; this unit's additions continue from O-17 and R-21.

### 2.2 · What this unit adds to the Admin objects

Every object below keeps its IA4 label, attributes and relationships; nothing is renamed (IA4, "What IA7 may do with it"). The additions, each invented for the running example (Perqo, fictional):

- **Volumes, for a sizing client.** Volumes are given for one client used here and by DD-IA2 to size Admin: 1,200 employees in 14 employee groups, with three admin users (two HR managers and one finance manager). It is not the example client of IA3 and IA6, whose policy those units described; that client's size is left free. From IA6's assumed frequency of one claim per employee a month (IA6, Deliverable A), the sizing client sees about 1,200 claims a month; from eight card payments per employee a month (same), about 9,600 card payments. Assuming 15% of claims are over the policy's auto-approve limit, about 180 a month wait in Approvals, about 9 a working day over 20 working days. Each employee holds one allocation per open category and period (IA3, section 2.3), so up to 4,800 allocations a period with all four categories open. Every volume here is assumed.
- **Employee status.** An employee is Invited when HR invites them, Active once they join in the app (Join, A-0.1; IA6, Deliverable B, B.4, E-2), and Left when HR marks them as left. It is a new attribute on O-05, with its own lifecycle (section 5.1).
- **Account owner.** One admin user per client is its account owner, a power held beside the HR manager or finance manager role (section 3.4). It is a new attribute on O-02, and IA4's role attribute keeps its two values.
- **Admin user status.** Active or Removed. A removed admin user can no longer sign in, and their name stays on every decision and change they made (section 5.3).
- **Two claim attributes for the decision.** Decided by (the admin user who decided, or the rule) and rejection note (HR's words to the employee when HR rejects), beside IA6's rejection reason (over the balance, or by HR).
- **One new object, the audit entry (O-17).** One record per change to an Admin object: who made it, what action, on which object, when, and the values before and after (section 5.3).
- **Four new relationships.** R-21: an admin user is also an employee (0..1 to 0..1), matched by work email, because HR and finance managers are employees of the client and may claim too. R-22: a claim is decided by an admin user (0..* to 0..1; none when the rule decides). R-23: an audit entry records a change to one object of Admin (0..* to 1). R-24: an audit entry is made by an admin user (0..* to 0..1; none when the Perqo system made the change).

### 2.3 · Card and notification: the two names IA4 left unset

IA4 left Admin's name for two objects unset, for this unit (IA4, A.1), and IA6 repeated the gap in its labels table (IA6, section 6.2); since 3 November 2026 both give the decisions below, with a dated note. The test for each is IA4's: does anyone in Admin find, list or act on the thing (IA4, section 4.2)?

- **Card (O-09): shown, as "Perqo card", status only.** HR is the person an employee asks why a payment was declined, and IA6 set that a payment is declined at the till when the card is Frozen or the payment is over the category's balance (IA6, Deliverable C, C.2). So the employee's record in Admin shows "Perqo card" with its status: Active, Frozen, or Not issued when the employee holds no card (R-11 allows 0..1). The label is perqo.com's (IA4, A.1), so no new term enters the vocabulary. The last four digits are not shown, and Admin cannot change the card: HR's one call to action on it is -> view status (Deliverable A, A.4), and freezing and unfreezing stay the employee's (IA4, A.3). Showing only what HR needs to answer the question applies least privilege to an attribute (section 3.3).
- **Notification (O-10): not shown.** A notification is a message to the employee about one claim (IA4, A.1). What HR needs to know about that claim is its status and history, which the claim and its audit entries hold (section 5.3). Showing the employee's messages in Admin would put a person's inbox in their employer's backoffice and add nothing HR acts on. Whether Admin sends HR any message of its own (a daily email of waiting claims, say) is left free.

## 3 · Roles and permissions as an IA layer

### 3.1 · Role-based access control, in the IA's terms

Engineering has a standard model for who may do what. David Ferraiolo, Ravi Sandhu, Serban Gavrila, Richard Kuhn and Ramaswamy Chandramouli's article opens: "In this article we propose a standard for role-based access control (RBAC)" ("Proposed NIST Standard for Role-Based Access Control", *ACM Transactions on Information and System Security* 4, no. 3, 2001, pp. 224 to 274, [doi.org, Ferraiolo 2001](https://doi.org/10.1145/501978.501980)). NIST's own summary of the model, as standards documentation: "all access is through roles"; "A role is essentially a collection of permissions"; and "all users receive permissions only through the roles to which they are assigned". The proposal was adopted as an American national standard, INCITS 359-2004, in four components: Core RBAC, Hierarchical RBAC, and static and dynamic separation of duty (NIST, "Role Based Access Control: Frequently Asked Questions", archived 2008, [NIST RBAC FAQ, archived](https://webarchive.library.unt.edu/eot2008/20080917093055/http:/csrc.nist.gov/groups/SNS/rbac/faq.html)).

The IA does not design the access-control system; engineering and security do. What the IA owns is the layer people meet: which roles exist and what they are called, and what each role sees, does and reaches in the structure. On this unit's reading of the RBAC model, the two meet at one point. A permission in RBAC is an operation on an object; a call to action in Prater's inventory is an action on an object with "who triggers it" recorded beside it (Prater 2016; IA4, A.3). The object map's calls to action, each with its role, are the permissions written in the user's words. That is why this unit records roles on the map itself (Deliverable A, A.4) and draws the role-by-section matrix from it.

### 3.2 · See, do, reach

A role decides three things in the IA, and each lands in a different artefact.

- **See: which objects and attributes the role's screens show.** It lands on the object-relationship map, as each object's "seen by" (Deliverable A, A.1). The Perqo card's last four digits are an attribute no Admin role sees (section 2.3).
- **Do: which calls to action the role holds.** It lands on the calls-to-action table, as "who" (Deliverable A, A.4).
- **Reach: which routes the role's navigation shows.** It lands in the navigation model, as a route that exists for some roles and not others (Deliverable C).

The three need not agree, and the IA decision is where they differ. IA6 set the rule for a thing a person cannot use: the choice is between hiding it, showing it disabled and showing it with an explanation, and the deciding question is whether the person can act on the explanation (IA6, section 4.4). Applied to roles, at Perqo (Perqo, fictional):

- **A route a role can never use is hidden.** Approvals is not in the finance manager's global navigation: no finance manager decides a claim (IA4, A.3), so the route would only ever lead to a list they cannot act on. What finance needs to know about waiting claims, their number and value, is in Reports, Claims by status.
- **An action a role holds but cannot take now is shown disabled, with the reason.** An HR manager looking at their own claim sees Approve and Reject unavailable, with the line "Another HR manager decides your own claim" (section 3.3). The person can act on that: they know who will decide.
- **What a role may see but not change is shown read only.** Finance sees policies and employees, without edit actions, because finance sets budgets per employee group and needs to know which categories each group's policy opens (R-06).

Each role also has a scope: which records it covers. At Perqo, every role covers its whole client (Perqo, fictional); scoping a role to some employee groups is a common enterprise need that this unit leaves free, because nothing in the brief or the filed units calls for it.

### 3.3 · Least privilege and separation of duty

Two security principles shape the role layer, and both have standard definitions. Least privilege: "a system should restrict the access privileges of users (or processes acting on behalf of users) to the minimum necessary to accomplish assigned tasks" (CNSSI 4009-2022, as given in NIST's glossary, [csrc.nist.gov, least privilege](https://csrc.nist.gov/glossary/term/least_privilege); standards documentation). Separation of duty "refers to the principle that no user should be given enough privileges to misuse the system on their own" (NIST SP 800-192, as given in NIST's glossary, [csrc.nist.gov, separation of duty](https://csrc.nist.gov/glossary/term/Separation_of_Duty)).

Each gives the IA a test. Least privilege asks of every cell of the role matrix whether the role needs it for its job, and it decided three Perqo cells (Perqo, fictional): HR does not see the Card payments report, which lists each employee's purchases, because no HR task needs individual purchases; no role sees the card's last four digits; and only the account owner manages admin users (section 3.4). Separation of duty asks where one person could both make and approve a request, and at Perqo that place is a claim: HR managers are employees too (R-21), and an HR manager who decided their own claim over the limit would approve their own spending. The rule (Perqo, fictional): an HR manager cannot decide their own claim; it waits in Approvals for another HR manager. Because the rule needs a second HR manager, every client has at least two admin users with the HR manager role. The rule is an exception in the claim's lifecycle (EX-1, Deliverable D).

### 3.4 · The account owner: who edits the company and adds admin users

IA4 left two calls to action without a role: client -> edit company details and admin user -> add, both in Settings (IA4, A.3). The choice is between giving them to an existing role and adding a power.

Giving them to every HR manager fails least privilege: an HR manager able to add admin users can add one with any role, so the power to approve claims (HR) and the power to set budgets (finance) could be joined in one person by that person's own act, which is what separation of duty exists to prevent (section 3.3). Giving them to finance has the same fault in the other direction. The decision (Perqo, fictional): each client has exactly one **account owner**, an admin user who also holds the HR manager or the finance manager role. The account owner, and only the account owner, edits the company details, adds and removes admin users, changes an admin user's role, reads the Activity log, and hands the ownership to another admin user (-> make account owner). At the start of a contract Perqo sets up the client's first admin user as account owner; the rest of a client's onboarding is left free.

Account owner is a power held beside a role: the person still does HR's or finance's work under their role. It is recorded as an attribute of the admin user (account owner, yes or no), which leaves IA4's role attribute with its two values. In RBAC's terms it is a third role a user can hold together with one of the others (NIST, RBAC FAQ); in the IA's terms it is one more row in the role matrix, and that is how the matrix draws it.

### 3.5 · The role-by-section matrix

The role-by-section matrix is the artefact that shows the layer: rows are roles, columns are the surface's sections, and each cell says what the role can see, do and reach there. IA2's catalogue has no entry for it, so this unit adds one, under IA2's rule "Keep the notation; extend the legend" (IA2, section 4):

| Question asked | Artefact | Figure kind | Fidelity by stage | Reader | Built in |
|---|---|---|---|---|---|
| Who can see, do and reach what, section by section? | Role-by-section matrix | matrix | F2 in design, one mark per cell; F3 for build, each mark traced to calls to action on the object map | engineering and security, the client, support, product management | IA7, Deliverable B |

The matrix is built in Deliverable B. Its readers read different things from it: engineering and security the permissions to build; the client whether its own people can do their jobs and only their jobs; support why a manager says a button is missing.

## 4 · Enterprise navigation

### 4.1 · Global, local and contextual routes in a backoffice

IA2 took the Polar Bear book's route types for the navigation model: global routes present everywhere on a surface, local routes within one area, contextual routes from one item to related items, and supplemental routes outside the main structure, among them search (Rosenfeld, Morville and Arango, *Information Architecture: For the Web and Beyond*, 4th ed., O'Reilly, 2015, ch. 8, headings; IA2, section 1.4). Its table gave Admin's global routes as IA1's six areas, Employees, Budgets, Policies, Approvals, Reports and Settings; its local routes as the policies inside Policies, one per employee group; its contextual route as the one from an employee's record to the claims they made; and no supplemental route (IA2, section 5.3).

This unit keeps all of that. The six areas stay as they are, in IA1's order, with no area added or renamed: each is either an object area (Employees, Budgets, Policies), a queue (Approvals), a set of views (Reports) or the client's own setup (Settings), and the objects of Deliverable A each have a home among them. Two things change around them, and both are extensions. The global routes a person sees depend on their role (section 3.2): a finance manager's navigation has five areas, without Approvals. And Approvals shows its count, the number of claims waiting for the person viewing it, because the count is what HR looks at the area for.

In a backoffice the contextual routes carry most of the movement. Prater argues that nesting objects inside each other finds the cross-links, and that the cross-links define contextual navigation (Prater 2015; IA4, section 2.4). Admin's relationships (Deliverable A, A.3) become its contextual routes almost one for one: an employee's record leads to their claims (R-08), their budgets (R-05) and their Perqo card's status (R-11); a claim leads to its employee, its policy (R-09) and its budget (R-10); an employee group leads to its policy (R-03), its employees (R-04) and its budgets; an audit entry leads to the record it changed (R-23). A relationship with no route is a question to ask: either nobody follows it, or a route is missing.

### 4.2 · Organised by objects and work queues

A website is organised around pages, because a visitor comes to read. A backoffice user comes to work through records: Kaplan's users manage "large underlying data sets" and do not follow "a known, sequential set of subtasks" (Kaplan 2020). Page Laubheimer's NN/g article on data tables names the four things people do with a table of records: "Find record(s) that fit specific criteria", "Compare data", "View, edit or add a single row's data" and "Take action(s) on records" ("Data Tables: Four Major User Tasks", Nielsen Norman Group, 3 April 2022, [nngroup.com, data tables](https://www.nngroup.com/articles/data-tables/); NN/g guidance). None of the four is "read a page". Each is an act on objects of one kind.

Two structures follow, and together they are how this unit organises Admin.

- **Every object type gets a list and a detail.** The list is IA4's database structure: items described by fields, the groups made at the time of asking by filtering and sorting (IA4, section 2.3). The detail is the object's own page, with its attributes, its calls to action and its contextual routes, and one address. A detail page belongs to its object, so it has one place in the structure and many routes to it: a claim's page sits under its employee's record (a claim belongs to one employee, R-08), and Approvals, Reports and the Activity log all open the same page. The cost is the one Laubheimer gives for any item with more than one parent: a breadcrumb shows one canonical path, which may not be the path the person took (Laubheimer, NN/g, 2018; IA4, section 2.2). Admin's answer is that a detail opened from a list opens beside the list, so the person's place stays in view (section 4.3).
- **Work that waits gets a queue.** A work queue is a list of one object type, filtered to the state in which someone must act, owned by the role that acts, ordered by what should be done first, and showing its count. Approvals is IA1's: every claim awaiting a decision, grouped by policy (IA1, section 2.2). Deliverable C, C.4 adds two: Not joined (employees still Invited after 14 days, for HR) and No budget for next period (employee groups with no budgets set for the coming period, for finance). A queue is a view, like a report: it holds no object of its own, so it is in the navigation model and nowhere on the object map (IA4, section 4.3).

The case for this organisation is a synthesis. Kaplan's definition and Laubheimer's four tasks are NN/g guidance built on observation; Prater's method is practice; the database structure is the Polar Bear book's (IA4, section 2.3). This unit knows of no controlled study comparing an object-and-queue backoffice with a page-organised one on the same content, so the organisation is argued, and the test of it is IA11's (what IA8 and later units take).

### 4.3 · List, detail, create and edit

Each object type's screens follow one pattern, so a person who has learnt one area has learnt the others: Cooper's intermediates (section 1.2) gain most from a pattern that repeats.

**List.** A table of the object, each row one record, showing the few attributes the person sorts, filters and recognises it by; the rest wait on the detail, as IA6 ranked the app's attributes (IA6, Deliverable A, A.2; Prater 2016). Laubheimer's guidance applies directly: "Filters need to be discoverable, quick, and powerful", and on a table larger than the screen, "Freeze header rows and header columns" (Laubheimer 2022). Each list has one default order, chosen by IA4's rule of the property the person thinks in: employees alphabetically by name, filtered by employee group (IA4, section 1.1), claims in Approvals oldest first.

**Detail.** The object's page: its attributes, its calls to action, its contextual routes and its History (section 5.3). On a wide window a detail opened from a list opens beside it. Laubheimer's guidance names the form, "A nonmodal side panel allows for the full display (and editing) of a single record" (Laubheimer 2022), and Android's platform documentation describes the same list-detail layout: on expanded widths "Selection of a list item updates the detail pane to show the related content for the selected item", and on medium and compact widths the window shows "either the list or the detail", with back returning to the list (Android Developers, "Canonical layouts", page updated 22 October 2026, [developer.android.com, canonical layouts](https://developer.android.com/develop/adaptive-apps/guides/canonical-layouts); platform documentation). Admin is used in a desktop browser (Perqo, fictional; assumed), and the narrow-window behaviour is its fallback.

**Create.** A form page reached from the list, with a name that starts with the verb the call to action uses: Create group, Invite employees, Set budgets, Add admin user, Edit policy. It ends on the new object's detail.

**Edit.** The detail's Edit opens the same form, filled. A change to a policy applies to claims submitted after it; claims already waiting keep the rule they were submitted under (Perqo, fictional), so that HR does not see a claim's route change after it has entered the queue. Every change is recorded in the object's History.

The list-detail pattern in Admin's busiest place, Approvals, drawn as a wireflow at F2 (Perqo, fictional). The Approvals list opens on "Waiting for you" with its count (9, the sizing client's working day, section 2.2), and shows the claims waiting, grouped by policy, oldest first, each with a box to select it (Select), a find field (Find in list) and Approve selected. Clicking a claim opens it beside the list: status, employee and employee group, amount, category, date submitted, the receipt, what remains in the category's budget, the policy's auto-approve limit, Approve and Reject, its History and a route to the employee's record. Approve moves the claim to Approved with no way back, and the next waiting claim opens. Reject opens a modal that asks for a note to the employee; Reject claim moves it to Rejected, with no way back. The HR manager's own claim opens in a state where Approve and Reject are unavailable, with "Another HR manager decides your own claim". Admin's screens take tone 4; the Rejected claim takes tone 6, a path that ends without success.

```viz
{"kind": "wireflow", "per_row": 2, "caption": "List-detail pattern: Approvals in Perqo Admin as a wireflow, F2; supports the decision on how HR moves through the queue of waiting claims, one by one or several at once, and where a decision cannot be undone (section 4.3). Tone 4 Perqo Admin; tone 6 a path that ends without success. List and detail beside each other from Laubheimer, 'Data Tables: Four Major User Tasks', NN/g, 2022, and Android Developers, 'Canonical layouts', 2026 (platform documentation); selection for batch actions from Laubheimer 2022; grouping by policy from IA1, section 2.2; the own-claim state from section 3.3; the no-way-back label stands for Garrett's crossbar (IA2, section 5.1); screen IDs from Deliverable C. Perqo is fictional.", "screens": [
 {"id": "list", "title": "Approvals", "tone": 4, "lines": ["Waiting for you: 9", "Grouped by policy, oldest first", "Select", {"bar": 0.8}, "Select", {"bar": 0.7}, "Select", {"bar": 0.6}, "Find in list", {"button": "Approve selected"}]},
 {"id": "own", "title": "Claim [your own claim]", "tone": 4, "lines": ["Status: Submitted", "Approve and Reject unavailable", "Another HR manager decides your own claim"]},
 {"id": "claim", "title": "Claim", "tone": 4, "lines": ["Status: Submitted", "Employee and employee group", {"bar": 0.6}, "Amount, category, date submitted", {"bar": 0.7}, "Receipt", {"block": 28}, "Remaining in the category's budget", {"bar": 0.4}, "Policy's auto-approve limit", {"button": "Approve"}, {"button": "Reject"}, "History", "Employee's record → see AD-1.1"]},
 {"id": "approved", "title": "Claim [Approved]", "tone": 4, "lines": ["Status: Approved", "Decided by: you", "Then Paid → see Deliverable D", "The next waiting claim opens"]},
 {"id": "reject", "title": "Reject claim (modal)", "tone": 4, "lines": ["Note to the employee (required)", {"block": 36}, {"button": "Reject claim"}, {"button": "Cancel"}]},
 {"id": "rejected", "title": "Claim [Rejected]", "tone": 6, "lines": ["Status: Rejected", "Reason: by HR, with your note", "The next waiting claim opens"]}],
 "links": [
  {"from": "list", "to": "claim", "label": "click a claim"},
  {"from": "list", "to": "own", "label": "[your own claim] click it"},
  {"from": "claim", "to": "approved", "label": "click Approve (no way back)"},
  {"from": "list", "to": "approved", "label": "[claims selected] click Approve selected (no way back)"},
  {"from": "claim", "to": "reject", "label": "click Reject"},
  {"from": "reject", "to": "rejected", "label": "click Reject claim (no way back)"}]}
```

### 4.4 · Bulk actions

Laubheimer's fourth task, acting on records, includes acting on several at once: "Batch actions usually involve a mechanism for selecting records (e.g., a checkbox for each record)", and "it's a convenient shortcut to have a single-click option to Select All" (Laubheimer 2022). In the IA a bulk action is a call to action on a set of objects, so it is recorded on the object map like any other, with its role. The question for each is whether every object in the set can take the same action with the same input.

At Perqo (Perqo, fictional) three bulk actions pass that test, each a new call to action: claim -> approve selected (HR, in Approvals); employee -> move to group, for selected employees (HR, in Employees); and employee -> resend invitation, for selected employees (HR, in Not joined). One fails it: rejection, because each rejection needs its own note to the employee, so claims are rejected one at a time. One bulk action was there from the start: finance sets the allocations of a whole group at once (IA4, Deliverable A), so Set budgets acts on up to hundreds of allocations in one form. A bulk approval runs the same checks as a single one on each claim, so one claim in a selection can end otherwise than the rest (T5, Deliverable D).

### 4.5 · Search inside the system

The first question the Polar Bear book asks of a search system is whether the product needs one ("Does Your Product Need Search?", Rosenfeld, Morville and Arango 2015, ch. 9, heading; IA3, section 5.1). IA2 gave Admin no supplemental route, and so no search (IA2, section 5.3). This unit keeps that, and gives every long list a find field instead.

The reasoning (Perqo, fictional). Most finding in Admin is known-item seeking, in Donna Spencer's term: the person knows what they want and the words for it (Spencer, Boxes and Arrows, 2006, practice; IA3, section 5.1). HR looks an employee up by name, from a question or a support conversation (IA4, section 1.2). That is served by a find field on the list that holds the item: Employees finds by name or work email, Approvals by employee name, Admins by name, the Activity log by person, object and date. Each find narrows its own list, which makes it part of the list's database structure (IA4, section 2.3); it adds no supplemental system. A search across every object type would be the supplemental route IA2 left out; at the sizing client's volumes (1,200 employees, 14 groups) the lists and their find fields serve, and the change is named for the day they do not: a global search over employees and claims, with results grouped by object type and shown only for the objects the person's role may see (section 3.2). Whether in-list find is enough is a test for IA11.

### 4.6 · Reports as views

IA4 kept Reports off the object map: a report is an arrangement of objects, "allocations and transactions summed by group and period", and belongs in Admin's navigation model (IA4, section 4.3). Here it is. Reports holds five views (Perqo, fictional): Spend by category, Spend by employee group, Budget use (each group's budgets against what has been spent), Claims by status, and Card payments (each card payment with its employee, merchant, category, amount and date). Each is a page with an identifier and an address, and no object ID. Every row of a report is a contextual route to the records it sums, so a number in a report can always be traced to the claims, card payments or allocations behind it. Finance sees all five. HR sees two, Budget use and Claims by status, and not the other three: Card payments lists individual spending, which no HR task needs (section 3.3), and the two spend reports serve finance's work alone.

## 5 · Workflows and states

### 5.1 · A state diagram for each object that has a lifecycle

IA2 drew the claim's lifecycle as a plain state-transition diagram, the form David Harel's statecharts extend ("Statecharts: A Visual Formalism for Complex Systems", *Science of Computer Programming* 8, 1987, pp. 231 to 274; IA2, section 1.8), and gave it F2 in design and F3 for build, "every transition with who or what triggers it" (IA2, Deliverable). In a backoffice, more than one object has a lifecycle, and each one gets its own diagram. The test for whether an object needs one is this unit's: draw a state diagram where a status decides what someone can do with the object, and where the object can leave a state by more than one route; record a status that has one way out as an attribute and a sentence. Applied to Admin's objects (Perqo, fictional):

| Object | States | Diagram? | Why |
|---|---|---|---|
| claim (O-07) | Submitted, Approved, Rejected, Paid (IA1; IA2) | yes, Deliverable D | four states, two end states, decisions by the rule and by HR, exceptions |
| employee (O-05) | Invited, Active, Left (this unit) | yes, below | what HR can do differs by state, and Invited has three ways out |
| card (O-09) | Active, Frozen (IA4) | no | the employee's own toggle; Admin only shows it (section 2.3) |
| admin user (O-02) | Active, Removed (this unit) | no | one transition, by the account owner |
| allocation, policy, employee group, client | none | no | they change values, not states; History records each change (section 5.3) |

The employee's lifecycle (Perqo, fictional). HR's invite creates the employee as Invited and sends HR's invitation, the email IA6 set as the app's entry E-2: to the employee's work email, with a link that opens Join (A-0.1), or Get the Perqo app (S-6) without the app; Join confirms the employer's name and the work email (IA6, Deliverable B, B.4). Admin's side agrees with it: HR invites from Employees, either one employee (employee -> invite) or several into one group (employee group -> invite employees), giving each one's name and work email; the employer's name the email carries is the client's name from Company (O-01). While Invited, HR can resend the invitation, which leaves the employee Invited; the employee joining in the app makes them Active. HR marks an employee as left, from Invited or from Active, and Left is an end state: the person can no longer sign in to the app. Claims they submitted before leaving are still decided; what happens to their remaining allocations and their card is left free, a cross-surface question for IA8. Admin's boxes take tone 4.

```viz
{"kind": "states", "per_row": 3, "caption": "State diagram: the lifecycle of an employee in Perqo Admin, F3, every transition with who triggers it; supports the decision on what HR can do with an employee in each state and which state the Not joined queue holds (section 5.1). Tone 4 Perqo Admin. Plain state-transition form as Harel 1987 extends it (IA2, section 1.8); the invitation and Join from IA6, Deliverable B, B.4, E-2; the states, the queue and the 14 days from this section and Deliverable C, C.4. Perqo is fictional.", "states": [
 {"id": "invited", "label": "Invited", "note": "[after 14 days] in the Not joined queue", "tone": 4},
 {"id": "active", "label": "Active", "tone": 4},
 {"id": "left", "label": "Left", "note": "can no longer sign in to the app", "tone": 4, "end": true}],
 "transitions": [
  {"from": "invited", "to": "invited", "label": "HR resends the invitation"},
  {"from": "invited", "to": "active", "label": "employee joins (A-0.1)"},
  {"from": "active", "to": "left", "label": "HR marks as left"},
  {"from": "invited", "to": "left", "label": "HR marks as left"}]}
```

### 5.2 · Approvals and exceptions

An approval is a state in which an object waits on a person's decision. Three things make it an IA question: where the waiting objects are listed (the queue, section 4.2), who may decide (the role layer, section 3), and what can happen to the object other than the decision (the exceptions). IA2's state diagram and decision tree drew the main path of a Perqo claim (IA2, section 5.3): on submission, a claim over the employee's balance is rejected; one at or under the policy's auto-approve limit is approved automatically; any other waits in Approvals, where HR approves or rejects it. Approved claims become Paid when Perqo pays out. The balance is the chosen category's (IA3, section 2.3), and a Rejected claim carries its reason, over the balance or by HR (IA6, Deliverable B).

Taking that diagram to F3 means writing each transition with its trigger, its actor and its condition (IA2, section 1.8), and then asking what else can happen. Three exceptions turn up at Perqo (Perqo, fictional), each an extension of IA2's diagram that adds a trigger or a condition and removes nothing:

- **EX-1, the claimant is an HR manager.** The claim waits in Approvals and only another HR manager may decide it (section 3.3). No new state: a condition on who may trigger the HR transitions.
- **EX-2, the balance has changed while the claim waited.** A claim waiting in Approvals does not reserve its amount: a category's spent counts approved and paid claims and card payments, not waiting claims (Perqo, fictional). So by the time HR approves, a card payment in the same category may have used the money. When an HR manager approves, the Perqo system checks the balance again, and a claim now over it moves to Rejected, over the balance. IA6 set the same check at the employee's end, between Check and submit and Submit (IA6, Deliverable C, C.3); this extends it to the moment of approval. It is a new trigger on IA2's Submitted-to-Rejected transition, T5.
- **EX-3, a claim waits too long.** A claim waiting more than five working days is marked Overdue in Approvals. Overdue is not a state: it changes the queue's order and look, and nothing anyone can do with the claim. Drawing it as a state would put a display rule into the lifecycle, and the diagram's readers (IA2, section 1.8: engineering, content, support, the client) would read a status field that does not exist.

The full transitions and exceptions are Deliverable D. Every decision is final in Admin: no transition leaves Approved except to Paid, and none leaves Rejected or Paid, as IA2's end states require.

### 5.3 · Audit trails

A backoffice where several people change records that money depends on needs to say who changed what. NIST's definition of an audit trail, as standards documentation: "A chronological record that reconstructs and examines the sequence of activities" surrounding or leading to an operation, procedure or event (NIST SP 800-53 Rev. 5, as given in NIST's glossary, [csrc.nist.gov, audit trail](https://csrc.nist.gov/glossary/term/audit_trail)).

For the IA, an audit trail is an object, with attributes, relationships and routes, so it goes on the map (Perqo, fictional): the audit entry, O-17, records one change: who (an admin user, or the Perqo system), the action, the object and its ID, the date and time, and the values before and after. Every transition in Deliverable D writes one, and so does every create, edit and removal in Admin. It is shown in two places, each a view: History, on every object's detail page, listing that object's entries newest first, seen by any role that may see the object; and the Activity log in Settings, listing every entry of the client, seen by the account owner. The audit entry is why decided by and the admin user's Removed status exist: a decision must keep its decider's name after the decider has left the client (section 2.2).

## 6 · The IA and the engineering data model

### 6.1 · Where the line runs

IA1 drew the line: the data model is how engineering stores the system, chosen for integrity and performance; the IA is how people meet it; and Cooper and his co-authors name the cost of an interface that follows the implementation model, where the represented model should sit close to the person's mental model (IA1, section 2.4; Cooper and others 2014, ch. 1, p. 16). In a backoffice the two sit closer than anywhere else, because the users manage the records themselves, and the temptation is to draw the IA as the schema with nicer names. Perqo's map shows where they part (Perqo, fictional):

- **One table, two objects.** The model stores every movement of money in one table of transactions with a type field (IA1, section 2.4); the IA has two objects, Claim and Card payment, because people do different things with them.
- **One action, many records.** Finance's Set budgets is one call to action on an employee group; in the model it writes one allocation per employee, category and period (IA4, Deliverable A).
- **Computed attributes.** Remaining is an attribute people read on the allocation; in the model it is computed from amount and spent, and stored nowhere.
- **Views with no table.** Reports and work queues are in the IA's navigation and nowhere in the model's tables; they are queries (sections 4.2 and 4.6).
- **Fields with no screen.** The model holds keys, foreign keys and the transaction's type field, which no screen shows.

### 6.2 · Evans's ubiquitous language

The idea that keeps the two aligned without making them one comes from Eric Evans's *Domain-Driven Design: Tackling Complexity in the Heart of Software* (Addison-Wesley, 2003), ch. 2, "Communication and the Use of Language" (contents at [pearson.com, contents](https://www.pearson.com/en-gb/subject-catalog/p/domain-driven-design-tackling-complexity-in-the-heart-of-software/P200000009375)). Evans's later summary of the pattern, published under an open licence, states it in a few lines: "Use the model as the backbone of a language"; "Commit the team to exercising that language relentlessly in all communication within the team and in the code"; "Within a bounded context, use the same language in diagrams, writing, and especially speech"; and "Recognize that a change in the language is a change to the model" (Eric Evans, *Domain-Driven Design Reference: Definitions and Pattern Summaries*, Domain Language, 2015, [domainlanguage.com, DDD Reference](https://domainlanguage.com/wp-content/uploads/2016/05/DDD_Reference_2015-03.pdf)). A bounded context is the limit of one model and its language: "Explicitly define the context within which a model applies" (same, "Bounded Context"; Evans 2003, ch. 14, "Maintaining Model Integrity"). Martin Fowler's gloss of the term is "building up a common, rigorous language between developers and users" ("Ubiquitous Language", martinfowler.com, 31 October 2006, [martinfowler.com, ubiquitous language](https://martinfowler.com/bliki/UbiquitousLanguage.html); practice).

Evans's book is about software design, and it addresses the language a team speaks with domain experts; it does not discuss the labels on a user interface. Bringing it to the IA is this unit's reading, and it has one tension at Perqo that the reader should see. Evans asks for one language within a bounded context, in diagrams, writing and speech. Perqo has three labels for one allocation: allocation in the model, Budget in Admin, Balance in the app (IA1, section 2.4). On this unit's reading the two are compatible if the team holds to one rule: the model name is the team's word, used in the code, the tickets, the F3 object map and the conversation between design and engineering; the surface labels are recorded translations of that word for each surface's readers, kept in the vocabulary and in the map's "Surface: Label" lines (IA2, section 5.2), and never a second concept. Where a surface label starts to mean something the model name does not, the language has changed, and by Evans's rule so has the model, and the vocabulary is where the change starts (IA2, section 4).

Admin sharpens the tension, because its users are the domain experts Evans means: HR and finance say "budget" for what finance sets. Whether engineering should take Budget as the model's name is a question for engineering and the IA designer together; this unit renames nothing (IA4, "What IA7 may do with it"), and records the question for IA8, which owns the vocabulary across surfaces.

Admin and the app read and write the same allocations, claims and policies, so on this unit's reading they are one bounded context with two presentations. The benefits catalogue, which Perqo's content team owns and classifies (IA4, Deliverable B), and the merchant side are candidates for contexts of their own; that is for engineering to decide, and the object map marks the joins (R-07, R-14, R-16, R-17) where a boundary would run.

### 6.3 · Keeping the two aligned

Four practices hold the line, each with the dependency it protects.

- **The F3 object map carries the model name of every object and attribute** (Deliverable A, A.2). Protects: engineering, which builds from it, and the IA, whose labels it maps (IA2, section 1.5).
- **A change of term goes through the vocabulary first**, with the old term kept as a variant, then into the map, the model and the screens (IA2, section 4). Protects: support and search, and Evans's rule that a change in the language is a change to the model.
- **Every deliberate divergence is written down**: one model table shown as two objects, a computed attribute, a view with no table (section 6.1). Protects: the next engineer, who would otherwise "fix" the IA to match the schema (IA1, section 2.4).
- **Permissions are written once, on the calls to action**, and both the role matrix and the access-control configuration are read from them (section 3.1). Protects: the client, who signs off what each role can do, and security, who build it.

## Deliverable · The Perqo Admin IA

*Face of this artefact (IA2, the notation sheet): the information architecture of Perqo Admin, in four parts: A, the object-relationship map at F3 (IA2's decision table: F3 as the agreed mapping to the data model); B, the role-by-section matrix at F2, one mark per cell, with a legend saying, for each mark, its calls to action, the pages and reports it opens, or what it stands for; C, the navigation model at F2 (IA2: before navigation components are chosen), with F3's identifiers on every page; D, the claim-approval state diagram at F3 (IA2: every trigger for build). Decision: what Admin holds, who may see, do and reach what, by which routes, and how a claim moves; readers: engineering and security (objects, model names, permissions, transitions), product management (scope), the client (whether its roles fit its people), support (where a manager is and what they can do), content (labels); leaves out: visual design and layout, the sign-in method, the merchant side and the catalogue's own surface, perqo.com and the app beyond the routes into them, measured volumes (every volume is assumed); owner: the IA designer; version 1, dated 3 November 2026; every object and placement is assumed until tested (IA4, section 4.3); Perqo is fictional.*

### Deliverable A · The object-relationship map

#### A.1 · Objects

Every Admin object of IA4's map, with IA4's label kept and this unit's columns added (Perqo, fictional). *New* marks a fact set by this unit. Volumes are for the sizing client (section 2.2) and assumed. "Seen by" and "changed by" name roles: HR (HR manager), finance (finance manager), owner (account owner); "all" means every admin user.

| ID | Object (model name) | Admin label and place | Volume, sizing client | Lifecycle | Work queue | Seen by | Changed by |
|---|---|---|---|---|---|---|---|
| O-01 | client (`client`) | Company, in Settings | 1 | none | none | all | owner *new* |
| O-02 | admin user (`admin_user`) | Admins, in Settings | 3 *new* | Active, Removed *new* | none | owner (all see their own profile) *new* | owner *new* |
| O-03 | employee group (`employee_group`) | Employee group, in Employees | 14 *new* | none | No budget for next period *new* | all | HR |
| O-04 | policy (`policy`) | Policy, in Policies | 14, one per group (R-03) | none; History records each change | none | all | HR |
| O-05 | employee (`employee`) | Employees | 1,200 *new* | Invited, Active, Left *new* | Not joined *new* | all | HR |
| O-06 | allocation (`allocation`) | Budget, in Budgets | up to 4,800 a period *new* | none | none | all | finance |
| O-07 | transaction, type claim (`transaction`, type claim) | Claim, on the employee's record; listed in Approvals | about 1,200 a month, about 180 waiting *new* | Submitted, Approved, Rejected, Paid (Deliverable D) | Approvals | all | HR (decision); Perqo system |
| O-08 | transaction, type card payment (`transaction`, type card payment) | Card payment, in Reports | about 9,600 a month *new* | none | none | finance *new* | nobody in Admin |
| O-09 | card (`card`) | Perqo card, on the employee's record *new*: status only | up to 1,200 | Active, Frozen (IA4) | none | HR *new* | nobody in Admin (the employee, in the app) |
| O-10 | notification | not shown *new* (section 2.3) | not applicable | none | none | nobody in Admin | nobody in Admin |
| O-13 | catalogue item (`catalogue_item`) | Covered items, in Policies | 12 in the sample (IA4) | none | none | all | Perqo content team (outside Admin) |
| O-17 | audit entry (`audit_entry`) *new* | History, on each detail page; Activity log, in Settings | one per change | none | none | History: any role that sees the record; Activity log: owner | nobody: written by the system |

O-11, O-12 and O-14 to O-16 are not in Admin (IA4, A.1), and are left as IA4 set them.

#### A.2 · Attributes and model names

Each attribute with IA4's label (or this unit's, marked *new*) and its model field (Perqo, fictional; the model names are invented here). Values are written as the model stores them.

| Object | Attribute → model field |
|---|---|
| O-01 client | name → `name`; contract start date → `contract_start_date` |
| O-02 admin user | name → `name`; work email → `work_email`; role (HR manager or finance manager) → `role` (`hr_manager`, `finance_manager`); account owner *new* → `is_account_owner`; status *new* → `status` (`active`, `removed`) |
| O-03 employee group | name → `name` |
| O-04 policy | open categories → `open_categories` (F-CAT identifiers, IA4, Deliverable B); auto-approve limit → `auto_approve_limit`; covered items → `covered_items` (catalogue item IDs, R-07) |
| O-05 employee | name → `name`; work email → `work_email`; status *new* → `status` (`invited`, `active`, `left`) |
| O-06 allocation | category → `category` (F-CAT identifier); period → `period`; amount → `amount`; spent → `spent` (approved and paid claims and card payments; waiting claims excluded, section 5.2); remaining → computed as amount less spent, not stored |
| O-07 claim | amount → `amount`; category → `category`; receipt → `receipt_file`; status → `status` (`submitted`, `approved`, `rejected`, `paid`); date submitted → `submitted_at`; rejection reason (IA6) → `rejection_reason` (`over_balance`, `by_hr`); decided by *new* → `decided_by` (an admin user ID, or `rule`); rejection note *new* → `rejection_note` |
| O-08 card payment | amount → `amount`; date → `occurred_at`; merchant → `merchant_id`; category → `category` |
| O-09 card | status → `status` (`active`, `frozen`); last four digits → `last_four` (not shown in Admin) |
| O-13 catalogue item | ID → `id`; name → `name`; the four facet values → `facets` (IA4, Deliverable B) |
| O-17 audit entry *new* | who → `actor_id` (an admin user ID, or `system`); action → `action`; object and its ID → `object_type`, `object_id`; date and time → `occurred_at`; before and after → `before`, `after` |

#### A.3 · Relationships

IA4's relationships that touch Admin, with their labels and counts as IA4 set them, and this unit's four (Perqo, fictional).

| ID | From | Relationship | To | Counts (from, to) | In Admin |
|---|---|---|---|---|---|
| R-01 | client | has | admin user | 1, 1..* | Settings, Admins; at least two HR managers per client *new* (section 3.3) |
| R-02 | client | has | employee group | 1, 1..* | Employees, Employee groups |
| R-03 | employee group | follows | policy | 1, 1 | group to policy and back |
| R-04 | employee group | contains | employee | 1, 1..* | group to its employees; Employees filtered by group |
| R-05 | employee | holds | allocation | 1, 1..* | employee's record, Budgets |
| R-06 | policy | opens the categories of | allocation | 1, 0..* | Set budgets offers only the group's open categories |
| R-07 | policy | covers | catalogue item | 0..*, 0..* | Policy, Covered items |
| R-08 | employee | submits | transaction, type claim | 1, 0..* | employee's record, Claims; a claim's page sits under it |
| R-09 | transaction, type claim | is checked against | policy | 0..*, 1 | claim to its policy; Approvals grouped by policy |
| R-10 | transaction, type claim | spends from | allocation | 0..*, 1 | claim shows what remains in its category's budget |
| R-11 | employee | holds | card | 1, 0..1 | employee's record, Perqo card status |
| R-12 | card | is used for | transaction, type card payment | 1, 0..* | not shown in Admin |
| R-13 | transaction, type card payment | spends from | allocation | 0..*, 1 | Reports, Card payments and Budget use |
| R-15 | transaction, type claim | triggers | notification | 1, 0..* | not shown in Admin |
| R-21 *new* | admin user | is also | employee | 0..1, 0..1 | matched by work email; decides EX-1 |
| R-22 *new* | transaction, type claim | is decided by | admin user | 0..*, 0..1 | claim, Decided by; none when the rule decides |
| R-23 *new* | audit entry | records a change to | client, admin user, employee group, policy, employee, allocation, claim | 0..*, 1 | History on each record; Activity log |
| R-24 *new* | audit entry | is made by | admin user | 0..*, 0..1 | none when the Perqo system made the change |

#### A.4 · Calls to action, with roles

Every Admin call to action, IA4's kept and this unit's added, with the role that triggers it and where it lives (Perqo, fictional). Page IDs are Deliverable C's. The two rows IA4 left without a role are the first two.

| Object | Call to action | Who | Where |
|---|---|---|---|
| client | -> edit company details | account owner *new* (section 3.4) | Settings, Company (AD-6.1) |
| admin user | -> add | account owner *new* (section 3.4) | Settings, Admins (AD-6.2.1) |
| admin user | -> remove *new*; -> change role *new*; -> make account owner *new* | account owner | Settings, Admins (AD-6.2) |
| employee group | -> create; -> invite employees | HR manager | Employees (AD-1.2.2; AD-1.3) |
| policy | -> edit; -> add covered items | HR manager | Policies (AD-3.1.1; AD-3.1.2) |
| employee | -> invite; -> move to group | HR manager | Employees (AD-1.3; AD-1, for one or selected employees) |
| employee | -> resend invitation *new*; -> mark as left *new* | HR manager | Employees (AD-1.1; AD-1.4, for one or selected employees) |
| allocation | -> set for a group | finance manager | Budgets (AD-2.2) |
| transaction, type claim | -> approve; -> reject | HR manager, never on their own claim | Approvals (AD-4), on the claim (AD-1.1.1) |
| transaction, type claim | -> approve selected *new* | HR manager, never on their own claim | Approvals (AD-4) |
| transaction, type claim | -> view *new* in Admin | HR manager, finance manager | the claim, under the employee's record (AD-1.1.1); Reports, Claims by status (AD-5.4) |
| transaction, type card payment | -> view in a report | finance manager | Reports, Card payments (AD-5.5) |
| card | -> view status *new* | HR manager | employee's record (AD-1.1) |
| catalogue item | -> view *new* in Admin | HR manager, finance manager | Policies, Covered items (AD-3.1.2) |
| audit entry *new* | -> view | any role that may see the record; account owner for the Activity log | History on each detail page; Settings, Activity log (AD-6.3) |

#### A.5 · The map, drawn

Split in two figures, IA2's rule "split rather than cram" (IA2, section 4), with "→ see" lines where an object continues in the other. Every box is tone 4, Perqo Admin, because the map shows one surface; each title is the model name in lower case and the "Admin: Label" line gives the label people see (IA2, section 5.2). Each box carries its ID, its volume and its work queue; model names of attributes are in A.2, and every relationship, drawn or not, is in A.3. The first figure holds the setup: client, admin users, employee groups, employees, policies and the catalogue items policies cover (R-01 to R-04, R-07, R-21).

```viz
{"kind": "objects", "caption": "Object-relationship map, figure 1 of 2, setup: the Admin objects HR and the account owner configure, with IDs, Admin labels, attributes, volumes for the sizing client (assumed), work queues, calls to action with their roles and counts in UML multiplicity notation, F3 (model names in A.2); supports the decision on what Admin holds and who changes it (Deliverable A). Every box tone 4, Perqo Admin, because the figure shows one surface. Lines read left to right on a level line, top to bottom otherwise. R-01 to R-04 and R-07 from IA4, Deliverable A, labels and counts kept; R-21, the account owner, employee status and the volumes set in section 2.2 and section 3.4; object-first method from Prater, A List Apart, 2015 and 2016. Perqo is fictional.", "objects": [
 {"id": "client", "title": "client", "tone": 4, "attrs": ["O-01", "Admin: Company, in Settings", "name", "contract start date", "volume: 1"], "actions": ["-> edit company details (owner)"]},
 {"id": "admin", "title": "admin user", "tone": 4, "attrs": ["O-02", "Admin: Admins, in Settings", "name", "work email", "role", "account owner", "status", "volume: 3"], "actions": ["-> add (owner)", "-> remove (owner)", "-> change role (owner)", "-> make account owner (owner)"]},
 {"id": "group", "title": "employee group", "tone": 4, "attrs": ["O-03", "Admin: Employee group", "name", "volume: 14", "queue: No budget for next period"], "actions": ["-> create (HR)", "-> invite employees (HR)"]},
 {"id": "employee", "title": "employee", "tone": 4, "attrs": ["O-05", "Admin: Employees", "name", "work email", "status", "volume: 1,200", "queue: Not joined", "→ see figure 2"], "actions": ["-> invite (HR)", "-> resend invitation (HR)", "-> move to group (HR)", "-> mark as left (HR)"]},
 {"id": "policy", "title": "policy", "tone": 4, "attrs": ["O-04", "Admin: Policy", "open categories", "auto-approve limit", "covered items", "volume: 14", "→ see figure 2"], "actions": ["-> edit (HR)", "-> add covered items (HR)"]},
 {"id": "item", "title": "catalogue item", "tone": 4, "attrs": ["O-13", "Admin: Covered items, in Policies", "ID", "name", "facet values", "volume: 12 in the sample"], "actions": ["-> view (HR, finance)"]}],
 "rows": [["client", "admin"], ["group", "employee"], ["policy", "item"]],
 "links": [
  {"from": "client", "to": "admin", "label": "has", "from_card": "1", "to_card": "1..*"},
  {"from": "client", "to": "group", "label": "has", "from_card": "1", "to_card": "1..*"},
  {"from": "admin", "to": "employee", "label": "is also", "from_card": "0..1", "to_card": "0..1"},
  {"from": "group", "to": "employee", "label": "contains", "from_card": "1", "to_card": "1..*"},
  {"from": "group", "to": "policy", "label": "follows", "from_card": "1", "to_card": "1"},
  {"from": "policy", "to": "item", "label": "covers", "from_card": "0..*", "to_card": "0..*"}]}
```

The second holds money, decisions and the record of them: the employee's card, claims and allocations, card payments, the admin user who decides a claim, the policy a claim is checked against, and the audit entry (R-05, R-08 to R-13, R-22 to R-24). R-06 and R-23's other objects are in A.3 only.

```viz
{"kind": "objects", "caption": "Object-relationship map, figure 2 of 2, money, decisions and the audit trail: the Admin objects money moves through, who decides a claim and what records each change, with IDs, Admin labels, attributes, volumes for the sizing client (assumed), work queues, calls to action with their roles and counts, F3 (model names in A.2); supports the decision on what Admin shows about spending and who answers for each decision (Deliverable A). Every box tone 4, Perqo Admin. Lines read left to right on a level line, top to bottom otherwise; a triangle by a label marks a label that reads right to left or bottom to top. R-05, R-08 to R-13 from IA4, Deliverable A, labels and counts kept; rejection reason from IA6, Deliverable B; R-22 to R-24, the audit entry (O-17), decided by, rejection note and the Perqo card label set in sections 2.2, 2.3 and 5.3. Perqo is fictional.", "objects": [
 {"id": "employee", "title": "employee", "tone": 4, "attrs": ["O-05", "→ see figure 1"]},
 {"id": "card", "title": "card", "tone": 4, "attrs": ["O-09", "Admin: Perqo card, status only", "status", "volume: up to 1,200"], "actions": ["-> view status (HR)"]},
 {"id": "policy", "title": "policy", "tone": 4, "attrs": ["O-04", "→ see figure 1"]},
 {"id": "claim", "title": "transaction, type claim", "tone": 4, "attrs": ["O-07", "Admin: Claim", "amount", "category", "receipt", "status", "date submitted", "rejection reason", "decided by", "rejection note", "volume: 1,200 a month", "queue: Approvals"], "actions": ["-> approve (HR)", "-> reject (HR)", "-> approve selected (HR)", "-> view (HR, finance)"]},
 {"id": "alloc", "title": "allocation", "tone": 4, "attrs": ["O-06", "Admin: Budget", "category", "period", "amount", "spent", "remaining", "volume: up to 4,800 a period"], "actions": ["-> set for a group (finance)"]},
 {"id": "payment", "title": "transaction, type card payment", "tone": 4, "attrs": ["O-08", "Admin: Card payment, in Reports", "amount", "date", "merchant", "category", "volume: 9,600 a month"], "actions": ["-> view in a report (finance)"]},
 {"id": "audit", "title": "audit entry", "tone": 4, "attrs": ["O-17", "Admin: History; Activity log", "who", "action", "object and its ID", "date and time", "before and after"], "actions": ["-> view (as the record; owner for the log)"]},
 {"id": "admin", "title": "admin user", "tone": 4, "attrs": ["O-02", "→ see figure 1"]}],
 "rows": [["employee", "card", null], ["claim", "alloc", "payment"], ["policy", "audit", "admin"]],
 "links": [
  {"from": "employee", "to": "card", "label": "holds", "from_card": "1", "to_card": "0..1"},
  {"from": "employee", "to": "claim", "label": "submits", "from_card": "1", "to_card": "0..*"},
  {"from": "employee", "to": "alloc", "label": "holds", "from_card": "1", "to_card": "1..*"},
  {"from": "claim", "to": "alloc", "label": "spends from", "from_card": "0..*", "to_card": "1"},
  {"from": "payment", "to": "alloc", "label": "spends from", "from_card": "0..*", "to_card": "1", "dir": "to"},
  {"from": "card", "to": "payment", "label": "is used for", "from_card": "1", "to_card": "0..*"},
  {"from": "claim", "to": "policy", "label": "is checked against", "from_card": "0..*", "to_card": "1"},
  {"from": "claim", "to": "admin", "label": "is decided by", "from_card": "0..*", "to_card": "0..1"},
  {"from": "audit", "to": "claim", "label": "records a change to", "from_card": "0..*", "to_card": "1", "dir": "to"},
  {"from": "audit", "to": "admin", "label": "is made by", "from_card": "0..*", "to_card": "0..1"}]}
```

### Deliverable B · The role-by-section matrix

*Face: role-by-section matrix of Perqo Admin, F2, one mark per cell, with a legend saying, for each mark, the calls to action in A.4, the pages and reports it opens, or what it stands for; decision: what each role sees, does and reaches in each section; readers: engineering and security, the client, support, product management; leaves out: scoping a role to some employee groups (left free, section 3.2), the sign-in method; owner: the IA designer; version 1, dated 3 November 2026; Perqo is fictional.*

#### B.1 · The matrix

Roles as rows, Admin's six areas as columns, IA1's order (Perqo, fictional). A blank cell means the area is not in that role's navigation. The account owner holds the HR manager or the finance manager role as well, so its row reads "as role" except in Settings.

| Role | Employees | Budgets | Policies | Approvals | Reports | Settings |
|---|---|---|---|---|---|---|
| HR manager | edit: create groups, invite, resend, move, mark as left | view | edit: policy, covered items | decide: approve, reject, approve selected, never on their own claim | some: Budget use, Claims by status | profile: Company read only, Your profile |
| Finance manager | view | set: set budgets for a group | view | (not in navigation) | all five reports | profile: Company read only, Your profile |
| Account owner | as role | as role | as role | as role | as role | manage: Company, Admins, Activity log, Your profile |

The figure draws the same matrix with a mark per cell and a legend. Its rows take tone 4, Perqo Admin.

```viz
{"kind": "matrix", "caption": "Role-by-section matrix: what each Perqo Admin role sees, does and reaches in each of Admin's six areas, F2, one mark per cell, with a legend saying, for each mark, the calls to action in Deliverable A, A.4, the pages and reports it opens, or what it stands for; supports the decision on what each role's navigation and screens hold (Deliverable B). Rows tone 4, Perqo Admin; a blank cell is an area not in that role's navigation. Areas from IA1's surfaces map; roles HR manager and finance manager from IA1, section 5, and IA4, A.1; account owner, the hidden Approvals route and separation of duty on own claims set in sections 3.2 to 3.4; the two reports HR sees set in section 4.6; role model from Ferraiolo and others, ACM Transactions on Information and System Security 4(3), 2001, and NIST's RBAC FAQ; least privilege and separation of duty from NIST's glossary. Perqo is fictional.", "cols": ["Employees", "Budgets", "Policies", "Approvals", "Reports", "Settings"], "rows": [
 {"label": "HR manager", "tone": 4, "cells": ["edit", "view", "edit", "decide", "some", "profile"]},
 {"label": "Finance manager", "tone": 4, "cells": ["view", "set", "view", null, "all", "profile"]},
 {"label": "Account owner", "tone": 4, "cells": ["as role", "as role", "as role", "as role", "as role", "manage"]}],
 "legend": [
  {"mark": "edit", "means": "employee group -> create, -> invite employees; employee -> invite, -> move to group, -> resend invitation, -> mark as left; policy -> edit, -> add covered items", "tone": 4},
  {"mark": "decide", "means": "-> approve, -> reject, -> approve selected [never on their own claim]", "tone": 4},
  {"mark": "set", "means": "-> set for a group (Set budgets)", "tone": 4},
  {"mark": "view", "means": "read only: no edit actions", "tone": 4},
  {"mark": "all", "means": "all five reports", "tone": 4},
  {"mark": "some", "means": "Budget use and Claims by status only", "tone": 4},
  {"mark": "profile", "means": "Company read only, and Your profile", "tone": 4},
  {"mark": "manage", "means": "client -> edit company details; admin user -> add, -> remove, -> change role, -> make account owner; Activity log, Your profile", "tone": 4},
  {"mark": "as role", "means": "what the holder's HR or finance role gives", "tone": 4}]}
```

#### B.2 · How each mark is shown

The three rules of section 3.2, applied (Perqo, fictional):

| Case | Shown as | Example |
|---|---|---|
| The role can never act or see there | hidden: no route | Approvals for a finance manager; the Card payments report for an HR manager; Admins and Activity log for anyone but the account owner |
| The role holds the action but cannot take it now | disabled, with the reason beside it | Approve and Reject on an HR manager's own claim: "Another HR manager decides your own claim" |
| The role may see but not change | read only: no edit actions | Policies and Employees for a finance manager; Budgets for an HR manager |

### Deliverable C · The navigation model

*Face: navigation model of Perqo Admin, F2 (IA2's decision table), with F3's identifiers on every page, AD-0 to AD-6, beside IA5's S-, L- and H- and IA6's A-; decision: by which routes each role reaches each object, list, queue and view; readers: engineering (routes and addresses), content (labels), support (where a manager is); leaves out: the components that carry the routes (navigation design, IA1, section 2.1), visual layout, Admin's domain; owner: the IA designer; version 1, dated 3 November 2026; Perqo is fictional.*

#### C.1 · Admin's pages

Admin's structure as a sitemap at F2 with identifiers, IA2's type tags (section, a landing page for a group; index, a list of items; stack, many pages of one type; detail, one item; form; IA2, section 5.2) and notation (Perqo, fictional). Notes carry the page ID, the roles that reach the page when not all do or the owner of its work queue, "queue" with the queue's [condition], "views" for the reports, "→ see" for a route drawn elsewhere, and, where it decides the page, what the page holds or how its list is ordered. A claim's page sits under its employee's record (section 4.2); Approvals and Claims by status open it there, and each entry of the Activity log opens its record. The six areas keep IA1's order, and Sign in comes last. Every box is tone 4, Perqo Admin; the root names the surface and carries no type tag, because the global navigation is not a page.

```viz
{"kind": "sitemap", "stack_from": 2, "caption": "Sitemap: Perqo Admin's pages at F2, with an identifier on every page (AD-0 to AD-6) and IA2's type tags; the structure the navigation model's routes run through; supports the decision on where each object's list, detail, create form, queue and view lives (Deliverable C, C.1). Every box tone 4, Perqo Admin. Notes give the page ID, roles where not all reach it or the owner of a queue, 'queue' with its [condition], 'views', and what a page holds or how its list is ordered where that decides it; '→ see' points to a page or surface drawn elsewhere. Six areas from IA1's surfaces map, kept; Policies one per employee group from IA2, section 5.3; Reports as views from IA4, section 4.3; the rest set in sections 3.2 to 3.4, 4.1 to 4.6 and 5.3, Deliverable A, A.1 and A.4, and Deliverable C, C.3 to C.5. Perqo is fictional.", "root": {"label": "Perqo Admin", "note": "the surface; AD-1 to AD-6 are global routes, by role", "tone": 4, "children": [
 {"label": "Employees", "type": "index", "note": "AD-1 · by name; filter by group, status; find", "tone": 4, "children": [
  {"label": "Employee", "type": "stack", "note": "AD-1.1 · one per employee; claims, budgets, Perqo card status (HR), History", "tone": 4, "children": [
   {"label": "Claim", "type": "stack", "note": "AD-1.1.1 · one per claim; modal: Reject claim (HR)", "tone": 4}]},
  {"label": "Employee groups", "type": "index", "note": "AD-1.2", "tone": 4, "children": [
   {"label": "Employee group", "type": "stack", "note": "AD-1.2.1 · its policy, employees, budgets", "tone": 4},
   {"label": "Create group", "type": "form", "note": "AD-1.2.2 · HR", "tone": 4}]},
  {"label": "Invite employees", "type": "form", "note": "AD-1.3 · HR", "tone": 4},
  {"label": "Not joined", "type": "index", "note": "AD-1.4 · queue [invited more than 14 days ago], owned by HR", "tone": 4}]},
 {"label": "Budgets", "type": "index", "note": "AD-2 · by group and period; queue No budget for next period [no budgets set for the next period], owned by finance", "tone": 4, "children": [
  {"label": "Budget", "type": "stack", "note": "AD-2.1 · one group, one period", "tone": 4},
  {"label": "Set budgets", "type": "form", "note": "AD-2.2 · finance", "tone": 4}]},
 {"label": "Policies", "type": "index", "note": "AD-3 · one per employee group", "tone": 4, "children": [
  {"label": "Policy", "type": "stack", "note": "AD-3.1 · open categories, auto-approve limit, covered items, History", "tone": 4, "children": [
   {"label": "Edit policy", "type": "form", "note": "AD-3.1.1 · HR", "tone": 4},
   {"label": "Covered items", "type": "index", "note": "AD-3.1.2 · HR adds; all view", "tone": 4}]}]},
 {"label": "Approvals", "type": "index", "note": "AD-4 · HR only; queue [over the policy's auto-approve limit]; by policy, oldest first; count on the global route; opens claims → see AD-1.1.1", "tone": 4},
 {"label": "Reports", "type": "section", "note": "AD-5 · views", "tone": 4, "children": [
  {"label": "Spend by category", "type": "index", "note": "AD-5.1 · finance", "tone": 4},
  {"label": "Spend by employee group", "type": "index", "note": "AD-5.2 · finance", "tone": 4},
  {"label": "Budget use", "type": "index", "note": "AD-5.3", "tone": 4},
  {"label": "Claims by status", "type": "index", "note": "AD-5.4 · opens claims → see AD-1.1.1", "tone": 4},
  {"label": "Card payments", "type": "index", "note": "AD-5.5 · finance", "tone": 4}]},
 {"label": "Settings", "type": "section", "note": "AD-6", "tone": 4, "children": [
  {"label": "Company", "type": "detail", "note": "AD-6.1 · owner edits", "tone": 4},
  {"label": "Admins", "type": "index", "note": "AD-6.2 · owner", "tone": 4, "children": [
   {"label": "Add admin user", "type": "form", "note": "AD-6.2.1 · owner", "tone": 4}]},
  {"label": "Activity log", "type": "index", "note": "AD-6.3 · owner; each entry opens its record", "tone": 4},
  {"label": "Your profile", "type": "detail", "note": "AD-6.4 · own profile", "tone": 4}]},
 {"label": "Sign in", "type": "form", "note": "AD-0 · line \"Looking for your benefits? Get the Perqo app\" → see S-6", "tone": 4}]}}
```

The identifiers, for citing (Perqo, fictional): AD-0 Sign in; AD-1 Employees, AD-1.1 Employee, AD-1.1.1 Claim, AD-1.2 Employee groups, AD-1.2.1 Employee group, AD-1.2.2 Create group, AD-1.3 Invite employees, AD-1.4 Not joined; AD-2 Budgets, AD-2.1 Budget, AD-2.2 Set budgets; AD-3 Policies, AD-3.1 Policy, AD-3.1.1 Edit policy, AD-3.1.2 Covered items; AD-4 Approvals; AD-5 Reports, AD-5.1 Spend by category, AD-5.2 Spend by employee group, AD-5.3 Budget use, AD-5.4 Claims by status, AD-5.5 Card payments; AD-6 Settings, AD-6.1 Company, AD-6.2 Admins, AD-6.2.1 Add admin user, AD-6.3 Activity log, AD-6.4 Your profile.

Admin's addresses follow IA4's rule, identifier first (IA4, section 5): /employees/{employee ID}, /employees/{employee ID}/claims/{claim ID}, /policies/{policy ID}, /budgets/{employee group ID}/{period}, /reports/claims-by-status (Perqo, fictional). A page that moves keeps a redirect from its old address. Admin's domain, and the identifiers' format, are left free.

#### C.2 · The routes

IA2's navigation table, Admin's column, at F2 (IA2, section 5.3; route types from Rosenfeld, Morville and Arango 2015, ch. 8). IA2's entries are kept; this unit's are marked *new* (Perqo, fictional).

| Route type | Perqo Admin |
|---|---|
| Global | Employees, Budgets, Policies, Approvals, Reports, Settings (IA1); by role *new*: a finance manager's navigation has no Approvals; Approvals shows the count of claims waiting for the viewer *new* |
| Local | the policies inside Policies, one per employee group (IA2); *new*: inside Employees, All employees (the Employees list, AD-1), Employee groups and Not joined; inside Budgets, the current and the next period; inside Reports, the five reports; inside Settings, Company, Admins, Activity log and Your profile; inside Approvals, none: it is one list, grouped by policy (IA1) |
| Contextual | from an employee's record to the claims they made (IA2); *new*: from an employee's record to their budgets and their Perqo card's status; from a claim to its employee, its policy and its budget; from an employee group to its policy, its employees and its budgets; from a budget to its employee group; from a policy to its employee group; from a report row to the records it sums; from an audit entry to the record it changed |
| Supplemental | none (IA2); each long list has a find field, part of the list (section 4.5) |

Where each person lands after signing in (*new*, Perqo, fictional): an HR manager on Approvals, a finance manager on Budgets, an account owner where their role lands them. The placing follows frequency, the rule IA6 took from Sears and Shneiderman's split menus and Nielsen's progressive disclosure (IA6, section 1.2): the most frequent work of each role is deciding claims for HR and setting budgets for finance (IA4, A.3), assumed until measured.

The same model as a matrix, one row per area of the global navigation: its local routes, its work queue, its contextual routes, and the roles that reach it with what each does there, from the role matrix (the supplemental row, none, is left out). An area with no work queue has a blank cell (C.4). A contextual route sits in the row of the area where it is followed most: a claim's routes are in Approvals, where HR opens claims, although the claim's page sits under Employees (C.1). Its rows take tone 4, Perqo Admin.

```viz
{"kind": "matrix", "caption": "Navigation model: Perqo Admin's six areas with their local routes, work queues, contextual routes, and the roles that reach each with their marks from Deliverable B, F2; supports the decision on which routes the navigation components must carry, for which role (Deliverable C, C.2). Rows tone 4, Perqo Admin. A blank cell is an area with no work queue (Deliverable C, C.4). The supplemental route, none, is left out (Deliverable C, C.2). Route types from Rosenfeld, Morville and Arango, 2015, ch. 8, through IA2, section 1.4; areas from IA1's surfaces map; IA2, section 5.3's Admin column kept; contextual routes from the relationships in Deliverable A, A.3, following Prater 2015; queues from Deliverable C, C.4; roles from Deliverable B. Perqo is fictional.", "cols": ["Local routes", "Work queue", "Contextual routes", "Roles"], "rows": [
 {"label": "Employees", "tone": 4, "cells": ["All employees, Employee groups, Not joined", "Not joined", "employee to claims, budgets, Perqo card status; group to policy, employees, budgets", "HR edit; finance view"]},
 {"label": "Budgets", "tone": 4, "cells": ["current period, next period", "No budget for next period", "budget to its employee group", "finance set; HR view"]},
 {"label": "Policies", "tone": 4, "cells": ["one per employee group", null, "policy to its employee group", "HR edit; finance view"]},
 {"label": "Approvals", "tone": 4, "cells": ["none: one list, grouped by policy", "Approvals, count on the global route", "claim to employee, policy, budget", "HR decide; not in finance's navigation"]},
 {"label": "Reports", "tone": 4, "cells": ["the five reports", null, "report row to the records it sums", "finance all five; HR some (two)"]},
 {"label": "Settings", "tone": 4, "cells": ["Company, Admins, Activity log, Your profile", null, "audit entry to its record", "account owner manage; others profile: Company read only, Your profile"]}]}
```

#### C.3 · Lists: order, filters, find, bulk actions

Every list in Admin, with its default order and what acts on it (Perqo, fictional; sections 4.3 to 4.5).

| Page | List of | Default order | Filters | Find | Bulk actions |
|---|---|---|---|---|---|
| AD-1 Employees | employees | name, alphabetical (IA4) | employee group; status | name or work email | move to group (HR) |
| AD-1.2 Employee groups | employee groups | name | none | name | none |
| AD-1.4 Not joined | employees, Invited over 14 days | oldest invitation first | employee group | name or work email | resend invitation; mark as left (HR) |
| AD-1.1 Employee, Claims | the employee's claims | by status, newest first in each, as the app's Claims (IA6) | status | none | none |
| AD-2 Budgets | employee groups by period | name | period | name | none: Set budgets is itself one action on a group |
| AD-3 Policies | policies | employee group name | none | none | none |
| AD-4 Approvals | claims waiting | grouped by policy (IA1), oldest first; Overdue marked | policy; category | employee name | approve selected (HR) |
| AD-5.4 Claims by status | claims | by status, newest first | status; employee group; category; period | employee name | none |
| AD-5.5 Card payments | card payments | newest first | employee group; category; period | employee name; merchant | none |
| AD-6.2 Admins | admin users | name | role; status | name | none |
| AD-6.3 Activity log | audit entries | newest first | person; object type; date | object ID | none |

#### C.4 · Work queues, and the invitation

| Queue | Object and state | Condition | Owner | Where | Order | Volume, sizing client | Cleared by |
|---|---|---|---|---|---|---|---|
| Approvals | claim, Submitted | over the policy's auto-approve limit; the viewer's own claim is listed, and only another HR manager can decide it (EX-1) | HR manager | AD-4; count on the global route | grouped by policy, oldest first; Overdue after five working days (EX-3) | about 9 a working day (assumed) | approve or reject (T3, T4); T5 |
| Not joined | employee, Invited | invited more than 14 days ago | HR manager | AD-1.4 | oldest invitation first | not set | resend invitation; mark as left |
| No budget for next period | employee group | no budgets set for the next period | finance manager | top of AD-2 | employee group name | up to 14 | set budgets |

HR's invitation, Admin's side of IA6's entry E-2 (IA6, Deliverable B, B.4). HR invites from Invite employees (AD-1.3), one employee or several into one group, each with a name and a work email; each becomes an employee in the state Invited (section 5.1). The invitation is an email to the work email, carrying the employer's name (the client's name, from Company, AD-6.1) and the link perqo.com/app/join/{invitation}, which opens Join (A-0.1) in the app, or Get the Perqo app (S-6) without it, as IA6 set. Resend invitation sends the same email again. How long an invitation stays valid is left free.

#### C.5 · The sign-in screen, and the proposal IA5 left

IA5 recorded an assumption, untested: an employee who wants the app may press Sign in on perqo.com and land on Admin's sign-in screen; it proposed for this unit a line there pointing employees to Get the Perqo app (IA5, section 5.5). IA6 left it with this unit, which owns that screen (IA6, section 6.3 and B.4).

**Decision: taken, with one change.** Admin's Sign in (AD-0) carries the line "Looking for your benefits? Get the Perqo app", linking to S-6, perqo.com/app (Perqo, fictional). The change: the line is on the screen for everyone, from the first view, not only after a failed sign-in. An employee who has landed in the wrong place may read the screen and leave without trying to sign in, and a line that appears only after a failure would never reach them. The words are the employee's: "benefits" is the app's tab and perqo.com's section (IA5, Deliverable B; IA6, Deliverable B). The cost is one line on a screen HR and finance see daily, which they learn to pass over (section 1.2). The assumption itself stays untested: the evidence IA5 named, Admin's failed sign-ins and the Help centre's search log (IA5, section 5.5; IA3, section 5.2), is for IA11 and IA12, and if no employee is ever found there, the line can go.

### Deliverable D · The claim-approval state diagram

*Face: state diagram of a Perqo claim at F3, every transition with its trigger, actor and condition, extending IA2, section 5.3's diagram and IA1's states; decision: what moves a claim, who may move it, and what is recorded when it moves; readers: engineering (the status field and its allowed changes), content and support (what each status and reason is called and what a person can do in it), the client (when money moves and who decided); leaves out: when Perqo pays out (the payout schedule is left free), the decision tree as a figure (IA2, section 5.3; IA8), the app's screens (IA6); owner: the IA designer; version 1, dated 3 November 2026; Perqo is fictional.*

#### D.1 · States and transitions

IA1's four states and IA2's transitions are kept: Submitted, Approved, Rejected, Paid, with Paid and Rejected end states; approve, by the rule or by HR; reject, by the rule or by HR; pay out (IA2, section 5.3). The rule is the register's, reading the chosen category's balance (IA3, section 2.3). This unit writes each transition at F3 and adds T5, marked *extension* (Perqo, fictional). Every transition writes an audit entry (O-17).

| ID | From | To | Trigger | Actor | Condition | Recorded on the claim |
|---|---|---|---|---|---|---|
| T1 | Submitted | Rejected | submission | Perqo system | the amount is over the chosen category's balance | rejection reason: over the balance; decided by: rule |
| T2 | Submitted | Approved | submission | Perqo system | within the balance, and at or under the policy's auto-approve limit | decided by: rule |
| T3 | Submitted | Approved | Approve, or Approve selected, in Approvals | HR manager, not the claimant (EX-1) | over the limit; the balance still covers the amount | decided by: the HR manager |
| T4 | Submitted | Rejected | Reject claim, with a note | HR manager, not the claimant (EX-1) | over the limit | rejection reason: by HR; rejection note; decided by: the HR manager |
| T5 *extension* | Submitted | Rejected | Approve, or Approve selected, in Approvals | Perqo system, on HR's approval | the amount is now over the category's balance (EX-2) | rejection reason: over the balance; decided by: rule |
| T6 | Approved | Paid | pay out | Perqo system | none | none beyond the audit entry |

A claim over the limit stays Submitted while it waits in Approvals (IA2's note "[over limit] waits in Approvals"). No transition leaves Rejected or Paid, and none returns a claim to Submitted.

#### D.2 · Exceptions

| ID | Exception | What happens | Status in the lifecycle |
|---|---|---|---|
| EX-1 *extension* | the claimant is an HR manager (R-21) | the claim waits in Approvals for another HR manager; the claimant sees Approve and Reject disabled, with "Another HR manager decides your own claim" | a condition on T3 and T4; no new state |
| EX-2 *extension* | the balance changed while the claim waited, since waiting claims reserve nothing | on HR's approval the Perqo system checks again; a claim now over the balance takes T5; in a bulk approval each claim is checked on its own | a new trigger, T5, on IA2's Submitted-to-Rejected transition |
| EX-3 *extension* | the claim has waited more than five working days | marked Overdue in Approvals, which is ordered oldest first | not a state: a display rule in the queue |
| EX-4 *extension* | the claimant is marked as left while the claim waits | the claim is still decided as usual | no change to the lifecycle |

#### D.3 · The diagram

The claim's lifecycle drawn at F3, the transitions labelled by their IDs and actors. Submitted, Approved and Paid take tone 5, because a claim's status is shown on both Admin and the app (IA2, section 5.3); Rejected takes tone 6, a path that ends without success.

```viz
{"kind": "states", "per_row": 2, "caption": "State diagram: the claim-approval lifecycle of a Perqo claim at F3, every transition with its ID and who triggers it, extending IA2, section 5.3's diagram (states from IA1, section 5) with T5 and the exceptions EX-1 and EX-2; supports the decision on what moves a claim, who may move it and what is recorded (Deliverable D). Tone 5 for the statuses Admin and the app both show; tone 6 a path that ends without success. The rule from IA2, section 5.3 and IA3, section 2.3; rejection reason from IA6, Deliverable B; T5, EX-1 and EX-2 set in section 5.2; separation of duty from NIST's glossary (SP 800-192); plain state-transition form as Harel 1987 extends it. Perqo is fictional.", "states": [
 {"id": "submitted", "label": "Submitted", "note": "[over the limit] waits in Approvals; [claimant is an HR manager] another HR manager decides (EX-1)", "tone": 5},
 {"id": "approved", "label": "Approved", "note": "decided by the rule or an HR manager", "tone": 5},
 {"id": "rejected", "label": "Rejected", "note": "reason: over the balance, or by HR with a note", "tone": 6, "end": true},
 {"id": "paid", "label": "Paid", "tone": 5, "end": true}],
 "transitions": [
  {"from": "submitted", "to": "approved", "label": "T2 rule; T3 HR manager approves"},
  {"from": "submitted", "to": "rejected", "label": "T1, T5 rule: over the balance; T4 HR manager rejects"},
  {"from": "approved", "to": "paid", "label": "T6 Perqo system pays out"}]}
```

## What IA8 and later units take

**IA8** takes this IA as the Admin layer of the cross-surface interaction map. The joins it will need are named here: Admin's invitation to the app's entry E-2 (Deliverable C, C.4); the claim's lifecycle (Deliverable D) to the app's Claims groups and Claim screen (IA6, Deliverable B) and to the decision tree IA2 drew, with T5 added; Admin's labels against the app's and perqo.com's through the object map's "Surface: Label" lines; and three cross-surface questions this unit leaves open: what happens to a leaver's remaining allocations and card (section 5.1); whether the model should take Admin's word, Budget, for the allocation (section 6.2); and where boundaries between models would run, at the catalogue and the merchant side (section 6.2).

**IA11** tests it. **IA12's assumption register** records its decisions and assumptions, each with its test:

| Decision or assumption | Where | Test (IA11) | What changes if it fails |
|---|---|---|---|
| Volumes of the sizing client: 1,200 employees, 14 groups, about 1,200 claims and 9,600 card payments a month, 15% of claims over the limit | section 2.2 | product analytics from live clients | the queue design; whether search is needed (section 4.5) |
| HR's most frequent work is deciding claims, finance's setting budgets, so each lands there | Deliverable C, C.2 | analytics of first actions after sign-in | the landing pages |
| In-list find serves known-item seeking at these volumes | section 4.5 | task-based usability test: find this employee, find this claim from a support question | a global search, role-scoped |
| HR and finance recognise their objects and their names (employee group, policy, budget, claim) | Deliverable A | card sort or interviews with HR and finance managers at clients | labels, through the vocabulary |
| A finance manager does not need Approvals | Deliverable B | interviews with finance managers | a read-only Approvals for finance |
| HR does not need individual card payments | section 3.3 | interviews with HR managers; support's tickets (IA12 as proxy) | the Card payments report for HR |
| The account owner fits how clients assign admin rights | section 3.4 | interviews with clients at onboarding | a second owner, or an owner without HR or finance work |
| The list-detail layout keeps HR's place in the queue | section 4.3 | usability test of a run of ten decisions | the detail on its own page |
| The sign-in line reaches employees who land on Admin | Deliverable C, C.5 | Admin's failed sign-ins; the Help centre's search log (IA5) | the line stays or goes |

**DD-IA2** takes this IA as the scope its business case is for, and the sizing client's volumes and queue numbers as the assumed load its case argues from, each to be replaced by measured figures.

## Perqo facts set by this unit

Every fact below is a course convention (Perqo, fictional), never evidence about the world. Each keeps every registered fact; none renames an IA1 to IA6 label, object, attribute or relationship.

| Fact | Set in | Left free |
|---|---|---|
| A sizing client, used for volumes here and by DD-IA2: 1,200 employees, 14 employee groups, three admin users (two HR managers, one finance manager); about 1,200 claims and 9,600 card payments a month; 15% of claims over the limit, about 180 a month, about 9 a working day over 20 working days; up to 4,800 allocations a period; it is not the example client of IA3 and IA6 | section 2.2 | the example client's size; measured volumes |
| Employee status: Invited, Active, Left; Left is an end state, after which the person cannot sign in to the app; claims submitted before leaving are still decided | sections 2.2, 5.1 | what happens to a leaver's allocations and card (IA8) |
| Account owner: exactly one per client, an admin user who also holds the HR manager or finance manager role; edits company details, adds and removes admin users, changes roles, reads the Activity log, hands ownership on; Perqo sets up the first admin user as account owner | section 3.4 | the rest of a client's onboarding |
| Admin user status: Active, Removed; a removed admin user's name stays on their decisions and changes | section 2.2 | none |
| Every client has at least two admin users with the HR manager role; an HR manager cannot decide their own claim | section 3.3; Deliverable D, EX-1 | none |
| Claim attributes decided by and rejection note; rejecting a claim needs a note to the employee | section 2.2; Deliverable D | the notes' wording |
| A waiting claim reserves nothing: spent counts approved and paid claims and card payments; on HR's approval the balance is checked again (T5) | section 5.2; Deliverable D | none |
| A claim waiting more than five working days is marked Overdue in Approvals | Deliverable D, EX-3 | none |
| Audit entry (O-17): who, action, object and its ID, date and time, before and after; shown as History on each detail page and as the Activity log in Settings | section 5.3 | how long entries are kept |
| Relationships R-21 (admin user is also employee), R-22 (claim is decided by admin user), R-23 (audit entry records a change to), R-24 (audit entry is made by admin user) | Deliverable A, A.3 | none |
| Admin's name for the card is "Perqo card", status only (Active, Frozen, Not issued), on the employee's record; Admin does not show notifications | section 2.3 | whether Admin sends HR messages of its own |
| Roles cover the whole client; the role-by-section matrix and the calls to action with their roles in Deliverables A and B; finance does not see Approvals; HR sees Budget use and Claims by status only | section 3; Deliverables A, B | scoping roles to employee groups |
| Every admin user sees Company (AD-6.1) read only; only the account owner edits it, and only the account owner reaches Admins and the Activity log | Deliverable A, A.1; Deliverable B | none |
| Admin's pages AD-0 to AD-6 as in C.1; addresses identifier first | Deliverable C, C.1 | Admin's domain; the identifiers' format |
| Reports holds five views: Spend by category, Spend by employee group, Budget use, Claims by status, Card payments | section 4.6 | the reports' columns beyond those named |
| Work queues: Approvals (HR), Not joined (HR, Invited over 14 days), No budget for next period (finance) | Deliverable C, C.4 | none |
| Bulk actions: approve selected; move to group; resend invitation; rejection one at a time | section 4.4 | none |
| No search across Admin; a find field on each long list | section 4.5 | when a global search is added |
| Landing after sign-in: HR on Approvals, finance on Budgets | Deliverable C, C.2 | none |
| A policy change applies to claims submitted after it | section 4.3 | none |
| Admin is used in a desktop browser (assumed); on a narrow window list and detail show one at a time | section 4.3 | none |
| Admin's sign-in screen carries "Looking for your benefits? Get the Perqo app", linking to S-6, for everyone (IA5's proposal, taken with one change) | Deliverable C, C.5 | the test's result |
| The invitation carries the client's name from Company and the Join link; Resend invitation sends it again | Deliverable C, C.4 | how long an invitation is valid |
| Model names of Admin's objects and attributes, as in A.2 | Deliverable A, A.2 | none |

## Sources

- Android Developers. "Canonical layouts". Page updated 22 October 2026 (platform documentation, checked 3 November 2026). [developer.android.com, canonical layouts](https://developer.android.com/develop/adaptive-apps/guides/canonical-layouts)
- Cooper, Alan, Robert Reimann, David Cronin and Christopher Noessel. *About Face: The Essentials of Interaction Design*. 4th ed. Wiley, 2014. Ch. 9, "Platform and Posture", pp. 205 to 236 (sections "Product Postures", p. 206, and "Postures for the Desktop", p. 207); ch. 10, "Optimizing for Intermediates", section "Perpetual Intermediates", p. 238. Contents at [e-bookshelf.de](https://wiley-vch.e-bookshelf.de/about-face-2765056.html).
- Evans, Eric. *Domain-Driven Design: Tackling Complexity in the Heart of Software*. Addison-Wesley, 2003. Ch. 2, "Communication and the Use of Language"; ch. 14, "Maintaining Model Integrity". Contents at [pearson.com, contents](https://www.pearson.com/en-gb/subject-catalog/p/domain-driven-design-tackling-complexity-in-the-heart-of-software/P200000009375).
- Evans, Eric. *Domain-Driven Design Reference: Definitions and Pattern Summaries*. Domain Language, 2015 (CC BY 4.0). "Ubiquitous Language"; "Bounded Context". [domainlanguage.com, DDD Reference](https://domainlanguage.com/wp-content/uploads/2016/05/DDD_Reference_2015-03.pdf)
- Ferraiolo, David F., Ravi Sandhu, Serban Gavrila, D. Richard Kuhn and Ramaswamy Chandramouli. "Proposed NIST Standard for Role-Based Access Control". *ACM Transactions on Information and System Security* 4, no. 3 (2001): 224 to 274. [doi.org, Ferraiolo 2001](https://doi.org/10.1145/501978.501980)
- Fowler, Martin. "Ubiquitous Language". martinfowler.com, 31 October 2006 (practice). [martinfowler.com, ubiquitous language](https://martinfowler.com/bliki/UbiquitousLanguage.html)
- Kaplan, Kate. "8 Design Guidelines for Complex Applications". Nielsen Norman Group, 8 November 2020. [nngroup.com, complex applications](https://www.nngroup.com/articles/complex-application-design/)
- Laubheimer, Page. "Data Tables: Four Major User Tasks". Nielsen Norman Group, 3 April 2022. [nngroup.com, data tables](https://www.nngroup.com/articles/data-tables/)
- NIST. "Role Based Access Control: Frequently Asked Questions". Computer Security Resource Center, archived 17 September 2008 (standards documentation). [NIST RBAC FAQ, archived](https://webarchive.library.unt.edu/eot2008/20080917093055/http:/csrc.nist.gov/groups/SNS/rbac/faq.html)
- NIST. Computer Security Resource Center glossary: "least privilege" (from CNSSI 4009-2022); "Separation of Duty" (from NIST SP 800-192); "audit trail" (from NIST SP 800-53 Rev. 5). Standards documentation, checked 3 November 2026. [csrc.nist.gov, least privilege](https://csrc.nist.gov/glossary/term/least_privilege); [csrc.nist.gov, separation of duty](https://csrc.nist.gov/glossary/term/Separation_of_Duty); [csrc.nist.gov, audit trail](https://csrc.nist.gov/glossary/term/audit_trail)
- Cited through the filed units, for claims made there: Cooper and others 2014, ch. 1, p. 16 (IA1); Harel 1987 (IA2); Krug, *Don't Make Me Think, Revisited*, 2014 (IA3; practice); Laubheimer 2018, "Polyhierarchies Improve Findability for Ambiguous IA Categories" (IA4); Nielsen 2006, "Progressive Disclosure" (IA6); Object Management Group, UML 2.5.1, 2017 (IA2); Prater 2015, "Object-Oriented UX", and 2016, "OOUX: A Foundation for Interaction Design", A List Apart (IA2, IA4; practice); Rosenfeld, Morville and Arango 2015, chs 8 and 9 (IA2, IA3); Sears and Shneiderman 1994 (IA6); Spencer 2006, "Four Modes of Seeking Information and How to Design for Them", Boxes and Arrows (IA3; practice); Garrett, *Visual Vocabulary Quick Reference* (crossbar; IA2). Full references in IA1 to IA6, Sources.

## Unsure list

- Cooper and others 2014, ch. 9: the chapter, its section titles and pages were checked in the publisher's contents; the account of sovereign and transient posture is from knowledge of the book and a secondary summary of the third edition, not re-read in the fourth, so it is paraphrased and nothing is quoted.
- Cooper and others 2014, ch. 10, "Perpetual Intermediates": the argument is from knowledge of the book; the section was not re-read.
- Evans 2003: chapter titles checked in the publisher's contents (published August 2003, copyright 2004); the quoted lines are from Evans's 2015 Reference, not from the 2003 book.
- Ferraiolo and others 2001: volume, issue, pages and date from an indexing record; the abstract's first sentence was read there; the article itself was not read.
- NIST's RBAC FAQ was read in a 2008 web archive; the live NIST page was not checked.
- NIST glossary audit trail: only the opening of the SP 800-53 Rev. 5 definition is quoted; the rest is paraphrased from the glossary page.
- That a permission in RBAC is an operation on an object is from knowledge of the RBAC model; the FAQ read for this unit says only that a role is a collection of permissions.
- Not checked: OWASP's guidance on sign-in error messages (the fetch was redirected); nothing from it is cited.
