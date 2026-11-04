---
audit: fresh check
unit: IA7 · Level 3 · the backoffice
course: ux · IA · Information Architecture
model: Fable 5.1 (claude-fable-5-1, confirmed from the agent's transcript; live search; no Fable 5.1 fresh check is owed for IA7)
date: 2026-11-03
chat: own Fable 5.1 agent context, not shown the writing (P31), launched by the U-7 chat (Opus 5.5 as the orchestrating chat; the writer ran on Opus 5.5) in session https://claude.ai/code/session_01KMmgQygerD9DuZzZgKBHp1
verdict: fix · 0 errors, 6 should-fix, 3 minor
---

The checker's final report, verbatim: its hand-back message, extracted by script from its transcript (the `SubagentHandback` call). The harness refused the checker's write of its own `out/report.md`, so the hand-back is the one copy. The maintainer's note follows the report.

# Fresh check · IA7 · Level 3 · the backoffice

**Text exact.** `diff K/unit.md K/unit-readonly.md` printed nothing; `sha256sum K/unit.md` = 8d93079eaf6847ddaf7909ac0c75fe8878472c8788733ebc36b13021fdc33a25, equal to K/unit.sha256. The text checked is the filed unit. (The harness refused the write of K/out/report.md, so this reply is the one copy of the report.)

**Model.** Running as Fable 5.1 (claude-fable-5-1). No Fable 5.1 fresh check is owed for IA7.

**Scope.** Brief K/brief-IA7.txt; sourcing-standard Part 1 and Part 4; the register K/perqo-facts.md; the vault IA1 to IA6. No audit report exists for this course, so item (6) is the pointer check only. Rendered all eight figures with `python3 K/render.py K/unit.md K/out/figs` (8 figures, 0 errors) and rasterised them with a stand-in stylesheet to read them.

## Findings

- [should-fix] [attribution] section 1.1, table row "Users paid to be there"; Current: `Users paid to be there | an employee who opens the app a few times a month (IA3, section 6.2, assumed) | managers who use Admin daily as part of their job (IA3, section 6.2, assumed) |`; Problem: IA3, section 6.2 says Admin is "used daily by the same HR and finance managers" and the app is "opened a few times a month"; "as part of their job" is this unit's addition and the pointer to IA3 claims it. Fix: `Users paid to be there | an employee who opens the app a few times a month (IA3, section 6.2, assumed) | managers who use Admin daily (IA3, section 6.2, assumed) |`; Basis: K/vault/IA3-how-people-find-and-understand-things.md, section 6.2, last paragraph.
- [should-fix] [attribution] section 1.2; Current: `IA6 built it so that every screen confirms where the person is and what the next step is (IA6, sections 3 and 4).`; Problem: IA6, sections 3 and 4 choose the tab bar by IA3's criteria and set progressive disclosure, empty, error and permission states; no sentence there says every screen confirms where the person is and what the next step is (nearest: criterion F2, "everything needed reachable from where the person is", section 3.5, and "Sequence decides the links", section 1.2). The pointer says more than IA6 says. Fix: `IA6 built it on a tab bar, with everything needed reachable from where the person is and a direct route to the task that usually follows (IA6, sections 3.5 and 1.2).`; Basis: K/vault/IA6-level-2-the-client-app.md, section 3.5 (criterion F2) and section 1.2.
- [should-fix] [attribution] section 2.1; Current: `A thing with three instances is a short page; a thing with a thousand is a list that needs order, filters and find (Laubheimer 2022, section 4.3).`; Problem: Laubheimer's article is about tables and their filters; the rule that three instances make a page and a thousand a list is this unit's, and the citation attaches it to Laubheimer. Fix: `A thing with three instances is a short page; a thing with a thousand is a list that needs order, filters and find (this unit's rule; the table guidance is Laubheimer 2022, section 4.3).`; Basis: Laubheimer, "Data Tables: Four Major User Tasks", NN/g, 3 April 2022 (article body not fetched in this check: rate-limited twice; its four tasks confirmed through https://www.nngroup.com/topic/tables/?asset=articles and https://stephaniewalter.design/blog/essential-resources-design-complex-data-tables/).
- [should-fix] [accuracy] section 4.3, Detail; Current: `and on narrow widths the window shows "either the list or the detail", with back returning to the list`; Problem: the page says "Medium- and compact-width displays show either the list or the detail"; the quoted fragment is exact, but "narrow widths" is the unit's word for the page's two named width classes while "expanded widths" earlier in the sentence is the page's own class. Keep the page's terms. Fix: `and on medium and compact widths the window shows "either the list or the detail", with back returning to the list`; Basis: https://developer.android.com/develop/adaptive-apps/guides/canonical-layouts?authuser=0 (last updated 2026-10-22): "Medium- and compact-width displays show either the list or the detail, depending on user interaction with the app"; "When just the detail is visible, pressing the back button redisplays the list."
- [should-fix] [figure] Deliverable C, C.1 sitemap; Current: `{"label": "Edit policy", "type": "form", "note": "AD-3.1.1 · HR", "tone": 4}`; Problem: the page name "Edit policy" appears nowhere in the unit's prose or tables; section 4.3 says a form's name "starts with the verb the call to action uses" and A.4 gives policy -> edit at AD-3.1.1, but the label exists in the figure only (Part 1: a figure adds no fact). Fix (to the prose, section 4.3, Create, leaving the block as it is): replace `A form page reached from the list, with a name that starts with the verb the call to action uses: Create group, Invite employees, Set budgets, Add admin user.` with `A form page reached from the list, with a name that starts with the verb the call to action uses: Create group, Invite employees, Set budgets, Add admin user, Edit policy.`; Basis: K/unit.md section 4.3 and Deliverable A, A.4 ("policy | -> edit; -> add covered items | HR manager | Policies (AD-3.1.1; AD-3.1.2)").
- [should-fix] [figure] Deliverable C, C.1 sitemap; Current: `Admin's addresses follow IA4's rule, identifier first (IA4, section 5): /employees/{employee ID}`; Problem: eight page identifiers are in the sitemap only and nowhere in the unit's text: AD-1.2.1, AD-2.1, AD-3.1, AD-5, AD-5.1, AD-5.2, AD-5.3, AD-6.4 (script: every `AD-` id in the viz block against every id in prose and tables). The sitemap is the F3 identifier list, so the IDs are the deliverable's content; Part 1 still asks that a figure's labels appear in the text. Fix: `The identifiers, for citing (Perqo, fictional): AD-0 Sign in; AD-1 Employees, AD-1.1 Employee, AD-1.1.1 Claim, AD-1.2 Employee groups, AD-1.2.1 Employee group, AD-1.2.2 Create group, AD-1.3 Invite employees, AD-1.4 Not joined; AD-2 Budgets, AD-2.1 Budget, AD-2.2 Set budgets; AD-3 Policies, AD-3.1 Policy, AD-3.1.1 Edit policy, AD-3.1.2 Covered items; AD-4 Approvals; AD-5 Reports, AD-5.1 Spend by category, AD-5.2 Spend by employee group, AD-5.3 Budget use, AD-5.4 Claims by status, AD-5.5 Card payments; AD-6 Settings, AD-6.1 Company, AD-6.2 Admins, AD-6.2.1 Add admin user, AD-6.3 Activity log, AD-6.4 Your profile.

Admin's addresses follow IA4's rule, identifier first (IA4, section 5): /employees/{employee ID}`; Basis: the sitemap block in K/unit.md, Deliverable C, C.1; sourcing-standard Part 1, "A figure adds no fact".
- [minor] [coverage] section 1.1; Current: `| Many entity types | eight objects with the employee's calls to action (IA6, Deliverable A, A.2) | ten of IA4's objects, and one added here (Deliverable A) |`; Problem: Deliverable A, A.1 lists eleven of IA4's objects (O-01 to O-10 and O-13), one of which, O-10 notification, is "not shown"; "ten" holds only if O-10 is left out, and the row does not say so. Fix: `| Many entity types | eight objects with the employee's calls to action (IA6, Deliverable A, A.2) | ten of IA4's objects shown, one not shown, and one added here (Deliverable A) |`; Basis: K/unit.md Deliverable A, A.1 (script count: 12 rows, 11 of them IA4's).
- [minor] [figure] section 4.3, wireflow prose; Current: `The Approvals list opens on "Waiting for you" with its count, and shows the claims waiting`; Problem: the figure prints "Waiting for you: 9"; the 9 is traced only through section 2.2's "about 9 a working day", and the prose beside the figure should carry the number so the figure adds none. Fix: `The Approvals list opens on "Waiting for you" with its count (9, the sizing client's working day, section 2.2), and shows the claims waiting`; Basis: K/unit.md section 2.2 ("about 180 a month, about 9 a working day over 20 working days").
- [minor] [label] section 1.2; Current: `Cooper's argument is practice from a standard work, not a measured finding, and this unit uses it as practice.`; Problem: none in the label itself; noted because the unsure list says the posture account is "from knowledge of the book and a secondary summary of the third edition, not re-read in the fourth". The chapter, sections and pages were confirmed against the publisher's contents (below); the paraphrase is unverifiable against the chapter text, and the unit quotes nothing from it. Fix: none required; keep as is. Basis: https://wiley-vch.e-bookshelf.de/about-face-2765056.html

No errors found.

## Confirmed

- Kaplan, "8 Design Guidelines for Complex Applications", NN/g, 8 November 2020: title, author, date; the definition "any application supporting the broad, unstructured goals or nonlinear workflows of highly trained users in specialized domains" is introduced as "previously defined" (an earlier NN/g article), as the unit says; "support highly trained users with specialized knowledge"; "navigate and manage large underlying data sets"; "relying on them for their work"; "years or even decades using the same system"; "users often do not follow a known, sequential set of subtasks". PASS. https://www.nngroup.com/articles/complex-application-design/
- Laubheimer, "Data Tables: Four Major User Tasks", NN/g, 3 April 2022: title, date and the four tasks ("Find record(s) that fit specific criteria", "Compare data", "View, edit or add a single row's data", "Take action(s) on records") confirmed via the NN/g tables topic page and a third-party page citing the article. The article body was rate-limited twice and not fetched, so the author's name and the five inner quotations ("Filters need to be discoverable, quick, and powerful"; "Freeze header rows and header columns"; "A nonmodal side panel allows for the full display (and editing) of a single record"; "Batch actions usually involve a mechanism for selecting records (e.g., a checkbox for each record)"; "it's a convenient shortcut to have a single-click option to Select All") are unverifiable (not checked). https://www.nngroup.com/topic/tables/?asset=articles ; https://www.nngroup.com/news/item/top-10-ux-articles-of-2022/
- Ferraiolo, Sandhu, Gavrila, Kuhn and Chandramouli, "Proposed NIST Standard for Role-Based Access Control", ACM TISSEC 4(3), August 2001, pp. 224 to 274, DOI 10.1145/501978.501980; abstract's first sentence "In this article we propose a standard for role-based access control (RBAC)." PASS. https://csrc.nist.gov/pubs/journal/2001/08/proposed-nist-standard-for-rolebased-access-contro/final
- NIST RBAC FAQ (UNT web archive capture 20080917093055, as cited): "all access is through roles"; "A role is essentially a collection of permissions"; "all users receive permissions only through the roles to which they are assigned"; "adopted as INCITS 359-2004"; four components Core RBAC, Hierarchical RBAC, Static Separation of Duty Relations, Dynamic Separation of Duty Relations. PASS. The unit's "a third role a user can hold together with one of the others (NIST, RBAC FAQ)": the FAQ implies several roles per user ("activation of a subset of roles assigned to a user") without stating it; acceptable as a reading. The FAQ does not define a permission as an operation on an object, which the unit's unsure list already says. https://webarchive.library.unt.edu/eot2008/20080917093055/http:/csrc.nist.gov/groups/SNS/rbac/faq.html
- NIST glossary, least privilege, CNSSI 4009-2022: "A security principle that a system should restrict the access privileges of users (or processes acting on behalf of users) to the minimum necessary to accomplish assigned tasks." PASS. https://csrc.nist.gov/glossary/term/least_privilege?utm_source
- NIST glossary, Separation of Duty, NIST SP 800-192: "refers to the principle that no user should be given enough privileges to misuse the system on their own." PASS. https://csrc.nist.gov/glossary/term/Separation_of_Duty
- NIST glossary, audit trail, NIST SP 800-53 Rev. 5 (and SP 800-37 Rev. 2): "A chronological record that reconstructs and examines the sequence of activities surrounding or leading to a specific operation, procedure, or event in a security-relevant transaction from inception to final results." The unit quotes the opening and paraphrases the rest, as its unsure list says. PASS. https://csrc.nist.gov/glossary/term/audit_trail
- Evans, Domain-Driven Design Reference: Definitions and Pattern Summaries, 2015, CC BY 4.0: "Use the model as the backbone of a language."; "Commit the team to exercising that language relentlessly in all communication within the team and in the code."; "Within a bounded context, use the same language in diagrams, writing, and especially speech."; "Recognize that a change in the language is a change to the model." (all under Ubiquitous Language); "Explicitly define the context within which a model applies." (Bounded Context). PASS. https://domainlanguage.com/wp-content/uploads/2016/05/DDD_Reference_2015-03.pdf
- Evans, Domain-Driven Design, Addison-Wesley, published 20 August 2003, copyright 2004: ch. 2 "Communication and the Use of Language"; ch. 14 "Maintaining Model Integrity". PASS. https://www.pearson.com/en-gb/subject-catalog/p/domain-driven-design-tackling-complexity-in-the-heart-of-software/P200000009375
- Fowler, "Ubiquitous Language", martinfowler.com, 31 October 2006: "the practice of building up a common, rigorous language between developers and users". PASS. https://martinfowler.com/bliki/UbiquitousLanguage.html
- Android Developers, "Canonical layouts", last updated 2026-10-22: "Selection of a list item updates the detail pane to show the related content for the selected item."; expanded-width displays "accommodate both the list and detail at the same time"; "Medium- and compact-width displays show either the list or the detail"; "pressing the back button redisplays the list". PASS with the wording note above. https://developer.android.com/develop/adaptive-apps/guides/canonical-layouts?authuser=0
- Cooper, Reimann, Cronin and Noessel, About Face, 4th ed., Wiley, 2014: ch. 9 "Platform and Posture" p. 205, "Product Postures" p. 206, "Postures for the Desktop" p. 207; ch. 10 "Optimizing for Intermediates" p. 237, "Perpetual Intermediates" p. 238. Chapter, sections and pages PASS; the paraphrase of posture and of perpetual intermediates is unverifiable (chapter text not opened). https://wiley-vch.e-bookshelf.de/about-face-2765056.html
- Cited through the filed units, each read in the vault: IA1 section 5 ("object-heavy", "permissions decide what each role sees", "would list its areas and miss most of its structure"); IA1 section 2.2 (Approvals holds every claim awaiting a decision, grouped by policy, each claim reachable from the employee's record); IA1 section 2.4 (one transactions table with a type field; allocation, Budget, Balance; Cooper ch. 1 p. 16); IA2 sections 1.4, 1.5, 1.8, 4, 5.1, 5.2, 5.3 and the decision table ("F3 as the agreed mapping to the data model"; "every transition with who or what triggers it"; "Keep the notation; extend the legend"; "split rather than cram"; Admin's navigation column; the claim diagram's "[over limit] waits in Approvals"; tones 4, 5, 6; Harel 1987; UML 2.5.1); IA3 sections 2.3, 5.1, 5.2, 6.2; IA4 sections 1.1, 1.2, 2.2, 2.3, 2.4, 4.1, 4.2, 4.3, 5, Deliverable A ("What IA7 may do with it", O-09 and O-10 "not set (IA7)", R-01 to R-20 with counts, the two "role not set: IA7" rows, "What the map hands on"); IA5 section 5.5 and its register row; IA6 sections 1.2, 3.2, 4.4, 6.2, 6.3, Deliverable A (frequencies claim 1, card payment 8 a month; A.2 eight objects), Deliverable B (B.4 E-2: Join confirms the employer's name and the work email; rejection reason "over the balance, or by HR"), Deliverable C (C.2 declined at the till when Frozen or over the balance; C.3 the balance can change before Submit) and its face ("Admin's screens (IA7)"). All say what the unit says they say, except the three pointers in the findings.

## Figures (7)

All eight blocks render (0 errors). Every caption names the artefact, the section or deliverable, the sources, and "Perqo is fictional".

1. wireflow, section 4.3. Six screens; every line is stated in the paragraph before the block (Waiting for you, grouped by policy oldest first, Select, Find in list, Approve selected, the claim's fields and routes, "Another HR manager decides your own claim", the required note, "the next waiting claim opens", no way back on Approve and Reject claim). The count 9 is traced to section 2.2 only (minor finding). Kind fits (screens: wireflow). Tones 4 and 6 named. PASS (with the minor line).
2. states, section 5.1. Invited, Active, Left; "[after 14 days] in the Not joined queue"; transitions HR resends the invitation, employee joins (A-0.1), HR marks as left from Invited and from Active: all in the paragraph above. Kind fits (lifecycle: states). PASS.
3. objects, A.5 figure 1 of 2. Six boxes; every attribute, volume, queue and action traced to A.1, A.2, A.4; links R-01, R-02, R-21, R-04, R-03, R-07 with A.3's counts. Kind fits. PASS.
4. objects, A.5 figure 2 of 2. Eight boxes; links R-11, R-08, R-05, R-10, R-13, R-12, R-09, R-22, R-23 (to claim only, as the prose says), R-24, counts as in A.3. Kind fits. PASS.
5. matrix, Deliverable B. Rows HR manager, Finance manager, Account owner; the six areas; every mark and legend line in the B.1 table. Kind fits (items by sections: matrix). PASS.
6. sitemap, Deliverable C, C.1. Six areas in IA1's order plus Sign in; tone 4 throughout; IA2's type tags. FIX: "Edit policy" and eight page IDs are in the figure only; the two text additions in the findings fix it (no change to the block).
7. matrix, Deliverable C, C.2. Rows the six areas; cells abbreviate the C.2 routes table and C.4 queues, each traceable ("All employees, Employee groups and Not joined", "the current and the next period", "the five reports", "Company, Admins, Activity log and Your profile", the contextual routes, the roles from B.1). Kind fits. PASS.
8. states, Deliverable D, D.3. Four states; notes and transition labels (T1 to T6, EX-1) traced to D.1 and D.2; tones 5 and 6 named in the sentence before it. Kind fits. PASS.

## Extra checks

- **Counts and calculations** (a Python script run with `python3 -I` on K/unit.md): 1,200 × 1 = 1,200 claims a month; 1,200 × 8 = 9,600 card payments; 15% of 1,200 = 180; 180 / 20 = 9 a working day; 1,200 × 4 = 4,800 allocations: all as stated. A.1: 12 rows (11 of IA4's, O-01 to O-10 and O-13, plus O-17). A.3: 18 rows, 14 of IA4's that touch Admin plus R-21 to R-24 ("four new", as stated). A.4: 15 rows. D.1: six transitions; D.2: four exceptions. Reports: five views named, five in the sitemap (AD-5.1 to AD-5.5). Sitemap: 29 page IDs; every AD id cited in the text exists in the sitemap. Handed-questions table: 10 rows (nine handed by name plus "one more", as the text says). "Perqo facts set by this unit": 23 rows. "(Perqo, fictional)": 31 labels. The one count that is loose is "ten of IA4's objects" (minor finding).
- **Public-site rules.** No personal fact about any reader or person; no private person named. "(Perqo, fictional)" on first use (the introduction's first sentence). Perqo labels, IDs, states, rules and areas checked against IA1 to IA6 and the register: O-01 to O-16 and R-01 to R-20 kept with IA4's labels and counts; six areas in IA1's order; the claim's four states and IA2's transitions kept, T5 and EX-1 to EX-4 added as extensions; IA6's rejection reason kept; IA4's role attribute keeps its two values (account owner is a separate attribute); IA6's E-2 invitation agrees; IA3's category-balance rule agrees; the register's "Not yet set" items (roles beyond the two, volumes, Admin's pages below the top level, numbers) are exactly what this unit sets. No contradiction found. Every figure is in IA2's notation (tone 4 on single-surface figures; tone 5 on the shared claim statuses; tone 6 stops; "→ see"; "[condition]"; "(no way back)"; "-> verb"; UML counts; IA2's type tags; lower-case model names as titles with "Admin: Label" lines). Tones named in the text: 4, 5 and 6 (introduction; section 4.3; D.3). Matrix row labels short and traced (the three roles from B.1; the six areas from IA1). Link texts all of the form "site, topic"; none a long bare path.
- **Pointers to filed units.** Each cited section read; all hold except the three in the findings (IA3 section 6.2 "as part of their job"; IA6 "sections 3 and 4"; Laubheimer 2022 for the unit's own rule). "IA6, section 6.3 and B.4" for the sign-in assumption holds (B.4: "stays with IA7, which owns that screen"). "IA4, section 1.1" for alphabetical Employees holds; "IA4, section 1.2" for HR looking people up by name holds ("pass: HR looks people up by name").
- **Questions handed to IA7 by name** (grep of the vault and register for "IA7"): IA2's decision table (navigation model, object-relationship map, state diagram: Deliverables C, A, D); IA4 section 4.3 (Reports in the navigation model: section 4.6, C.1); IA4 Deliverable A face and "What IA7 may do with it" (permissions and data-model mapping at F3, rename nothing: A.1 to A.4); IA4 A.1 O-09 and O-10 names (section 2.3); IA4 A.3 the two roles (section 3.4, A.4); IA4 "What the map hands on" (the eight Admin objects to F3: A.1, A.2); IA5 section 5.5 and its register row (the sign-in line: C.5); IA6 section 6.2 (card and notification names: section 2.3); IA6 B.4 (Admin's sign-in screen: C.5); IA6 Deliverable C face (Admin's screens: C.1). All answered. The object-relationship map extends IA4's map for Admin (roles, volumes, lifecycles, work queues, O-17, R-21 to R-24) and renames none of IA4's objects, attributes or relationships: every A.1 and A.3 label compared with IA4's A.1 and A.2 by ID, identical.
- **Not checked** (unverifiable): the body of Laubheimer 2022 (rate-limited twice); the chapter text of Cooper 2014; the live NIST RBAC page (the unit cites the archive, which was opened).
- Nothing in memory, project context or any profile was used as a source.

## Verdict

IA7 · fix · errors 0, should-fix 6, minor 3.

## Figure 6 re-check 1 (Opus 5.5 agent, 3 November 2026; the second check of figure 6, sitemap: Admin's pages; given the unit without its figures, the captions and the frames sheets, nothing of the earlier reports; verbatim hand-back; the harness refused its `report.md` write, so the hand-back is the one copy)

Figure 6 (sitemap) of IA7 needs fixes. Nothing in it is wrong: every label, ID and note traces to a line of the unit. Four should-fixes remain: the FORM tag on Covered items, a [condition] the text promises but the figure never uses, type tags the text never names, and two sections missing from the caption's sources. I could not save the report as F/report.md (the write was refused), so this reply is the only copy. I opened all 12 sheets; the tall phone frame sheets I cut into pieces in F/crops/ to read them.

## (a) Findings

- **[should-fix] The Covered items page (AD-3.1.2) is tagged FORM, but it is not a form.**
  - The unit's rule for forms (line 169) is a name "that starts with the verb the call to action uses: Create group, Invite employees, Set budgets, Add admin user, Edit policy". "Covered items" has no verb.
  - Every role views the page: "catalogue item | -> view *new* in Admin | HR manager, finance manager | Policies, Covered items (AD-3.1.2)" (line 349), and O-13 is seen by "all" (line 282). It is a list with an HR add action.
  - Change the tag to `INDEX`.
  - The note says "HR edits", but the call to action is "-> add covered items" (line 340). New note: `AD-3.1.2 · HR adds; all view`.

- **[should-fix] Unit text line 396 says the notes carry "a [condition]", but no note uses square brackets, and the caption does not mention conditions.** Either use the brackets where the text gives a condition, or remove the promise:
  - Not joined note: `AD-1.4 · queue [Invited over 14 days]; HR` (the condition is in C.4, line 444: "invited more than 14 days ago").
  - Budgets note: `AD-2 · by group and period; queue [no budget for next period]`.
  - Or delete "a [condition]," from line 396.

- **[should-fix] Line 396 says "IA2's type tags" but this unit never names them.** The five tags drawn (SECTION, INDEX, STACK, DETAIL, FORM) appear nowhere in the unit as tags. In line 396, replace "a sitemap at F2 with identifiers, IA2's type tags and notation" with `a sitemap at F2 with identifiers, IA2's type tags (section, index, stack for one page per instance, detail, form) and notation`. I cannot check IA2's own definitions of the tags from this folder.

- **[should-fix] The caption's source list leaves out two sections.**
  - The account owner, and with it Admins, Add admin user and Company's "owner edits", is set in section 3.4 (line 126).
  - The Activity log and History are set in section 5.3 (line 227).
  - New end of the caption: `the rest set in sections 3.4, 4.2 to 4.6 and 5.3 and Deliverable C, C.4 and C.5. Perqo is fictional.`

- **[minor] The root note "global routes by role" sits above Sign in (AD-0), which is not a global route.** C.2 lists only the six areas as global routes (line 410). New root note: `the surface; AD-1 to AD-6 are global routes, by role`.

- **[minor] Line 396 says "Approvals, Reports and the Activity log open it there", but only Approvals has the note "opens claims → see AD-1.1.1".** Either add `AD-5.4 · opens claims → see AD-1.1.1` to Claims by status and `AD-6.3 · owner; opens records` to Activity log, or narrow line 396 to Approvals.

- **[minor] Not joined's "HR" comes from the queue's owner (line 444).** The text never says finance cannot reach the page, and finance can view Employees (line 373). If "owner" is meant as "reaches", add to C.2's local routes: `Not joined (HR)`.

- **[minor, unit text] The unit contradicts itself on who sees Company (AD-6.1).**
  - A.1 says Company is seen by "all" (line 272).
  - B.2 hides only Admins and the Activity log from everyone but the owner (line 386).
  - B.1 gives HR's and finance's Settings cell as "profile: Your profile" only (line 373).
  - The figure follows A.1. New B.1 Settings cells for HR and finance: `view: Company; profile: Your profile`.

## (b) Confirmed (label, then the line it comes from)

- **Root:** "Perqo Admin" with no tag (line 396: "the root names the surface and carries no type tag"); "global routes by role" (lines 146 and 410).
- **Sign in:** AD-0, "Looking for your benefits? Get the Perqo app → see S-6" (lines 400 and 453).
- **Employees and its pages:**
  - Employees, AD-1: by name; filter by group; find (lines 165, 187, 427).
  - Employee, AD-1.1: one per employee; claims, budgets, Perqo card status, History (lines 148, 167, 402).
  - Claim, AD-1.1.1: sits under the employee's record (lines 396, 402); "modal: Reject claim (HR)" (lines 173, 468).
  - Employee groups, AD-1.2 (lines 400, 428).
  - Employee group, AD-1.2.1: its policy, employees, budgets (line 148).
  - Create group, AD-1.2.2, HR (line 339).
  - Invite employees, AD-1.3, HR (lines 339, 341, 447).
  - Not joined, AD-1.4: queue, Invited over 14 days, HR (lines 157, 429, 444).
- **Budgets and its pages:**
  - Budgets, AD-2: by group and period; queue No budget for next period (lines 431, 445).
  - Budget, AD-2.1: one group, one period (line 402).
  - Set budgets, AD-2.2, finance (line 343).
- **Policies and its pages:**
  - Policies, AD-3: one per employee group (lines 144, 411).
  - Policy, AD-3.1: open categories, auto-approve limit, covered items, History (lines 274, 296).
  - Edit policy, AD-3.1.1, HR (line 340).
  - Covered items, AD-3.1.2 (lines 282, 340, 349; see the tag finding).
- **Approvals:** AD-4: queue; HR; by policy, oldest first; opens claims → see AD-1.1.1 (lines 110, 396, 433, 443).
- **Reports and its pages:**
  - Reports, AD-5: views (lines 191, 396).
  - AD-5.1 Spend by category, finance; AD-5.2 Spend by employee group, finance; AD-5.3 Budget use; AD-5.4 Claims by status; AD-5.5 Card payments, finance (line 191: "Finance sees all five. HR sees Budget use and Claims by status").
- **Settings and its pages:**
  - Settings, AD-6 (line 400).
  - Company, AD-6.1: owner edits (lines 272, 336).
  - Admins, AD-6.2: owner (lines 273, 386).
  - Add admin user, AD-6.2.1: owner (line 337).
  - Activity log, AD-6.3: owner (lines 227, 386).
  - Your profile, AD-6.4: every admin user (lines 268, 373).
- **Identifiers:** all 29 match the list in line 400, with the same labels and the same parents.
- **Tone:** one tone throughout, tone 4, named in lines 14 and 396.
- **Caption:** it says what the figure shows, names Deliverable C, C.1, gives its sources and says "Perqo is fictional". Only the source list is incomplete (finding above).
- **Kind:** the data is a hierarchy of pages, so a sitemap fits.

## (c) Renderer notes

- **Rows are not levels.** The renderer wraps the root's seven children into three rows by width: (Sign in, Employees, Budgets), (Policies, Approvals, Reports), (Settings). All seven are on one level. The left trunk that joins rows 2 and 3 runs straight down past Sign in, a page with no children, so at a glance it can read as Sign in's branch. This happens at every width. The declaration can fix it: list Sign in last and Employees first. That also keeps IA1's six areas in their order.
- **Desktop and tablet opening frames** are clipped by the sticky section bar, around the Employee group page. The figure is taller than the viewport, and the frames sheet ("frame 1 of 1") shows it whole. This is not a figure fault.
- **Phone (390 px):**
  - The figure is wider than its frame. It scrolls sideways inside the frame, and the cue line "scroll sideways for the whole figure" sits above the caption.
  - There are three frames, scrolled to 88, 252 and 372 of 372 px. Every box appears whole in at least one:
    - frame 1: Sign in, Employees, Policies, Policy, Edit policy, Covered items
    - frame 2: the root, the Employees subtree, Approvals, Settings and its children
    - frame 3: the Budgets and Reports subtrees
- **Legibility:** at desktop, tablet and phone, in both dark and light, all text sits inside its boxes, nothing overlaps, and the caption is under the figure.

## (d) Verdict

Figure 6: **FIX**, for the four should-fixes above.

Files are in /tmp/claude-0/-home-claude/523bc694-bc8b-5dd5-bdd8-2b916401be73/scratchpad/f6r1/crops/:
- phone-dark-0.png to phone-dark-5.png
- phone-light-0.png to phone-light-5.png
