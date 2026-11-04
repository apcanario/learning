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

## Figure 5 re-check 1 (Opus 5.5 agent, 3 November 2026; the second check of figure 5, matrix: the role-by-section matrix; given the unit without its figures, the captions and the frames sheets, nothing of the earlier reports; verbatim hand-back; the harness refused its `report.md` write, so the hand-back is the one copy)

Figure 5 (matrix), IA7: **FIX**. One legend note says something the unit's text does not, and the caption names the wrong section for one fact. Everything else in the figure traces to the text, and it reads correctly at every width and in both themes. The harness would not let me write F/report.md, so this message is the only copy.

## (a) Findings
- **[error] The `edit` legend note does not match the text.** The figure says "create, change, invite; in Employees also resend, move, mark as left". B.1 (line 372) gives HR's `edit` as "create groups, invite, resend, move, mark as left" in Employees and "policy, covered items" in Policies.
  - As drawn, the note says HR can invite in Policies.
  - It leaves out A.4's "-> add covered items" (line 340).
  - The phrase "create, change, invite" appears nowhere in the unit.
  - Replacement note: `Employees: create groups, invite, resend, move, mark as left; Policies: edit policy, add covered items`
- **[should-fix] The caption gives the wrong section for HR's two reports.** It says "the two reports HR sees … set in sections 3.2 to 3.4". They are set in section 4.6 (line 191: "HR sees Budget use and Claims by status, and not the other three"). Section 3.3 only removes Card payments.
  - Replacement clause: `account owner, the hidden Approvals route and separation of duty on own claims set in sections 3.2 to 3.4; the two reports HR sees set in section 4.6`
- **[minor] The unit's text disagrees with itself on fidelity.**
  - Section 3.5's catalogue row (line 136) says: "F2 in design, one mark per cell; F3 for build, each mark traced to calls to action on the object map".
  - Deliverable B's face (line 364) and the caption both say "F2, each mark traced to the calls to action in A.4", which is the F3 trait.
  - Fix one way or the other: either change the face and caption to `F2, one mark per cell, with a legend naming the calls to action in A.4`, or call the matrix F3 in both places.
- **[minor] The `decide` note does not use the unit's notation.** "never their own claim" is a condition, and the unit writes conditions in square brackets (line 396: "queue" with the queue's [condition]). Calls to action are written "-> verb" in A.4. Optional replacement: `-> approve, -> reject, -> approve selected [not their own claim]`. This is not required, because B.1's own table also uses bare verbs.

## (b) Confirmed
- **Columns** (EMPLOYEES, BUDGETS, POLICIES, APPROVALS, REPORTS, SETTINGS): line 370; line 368 ("Admin's six areas as columns, IA1's order").
- **Rows** (HR manager, Finance manager, Account owner): lines 372–374.
- **HR manager row** (edit / view / edit / decide / some / profile): line 372.
- **Finance manager row** (view / set / view / blank / all / profile): line 373.
  - The blank Approvals cell: line 373 "(not in navigation)"; line 368 "A blank cell means the area is not in that role's navigation"; line 110.
- **Account owner row** (as role ×5 / manage): line 374; line 368 ("its row reads 'as role' except in Settings").
- **`decide`**: line 372 "approve, reject, approve selected, except their own claims"; lines 344–345 "never on their own claim".
- **`set`**: line 373 "set: set budgets for a group"; line 343.
- **`view` "read only"**: line 388 "read only: no edit actions"; line 112.
- **`all` "all five reports"**: line 373; line 191 ("Reports holds five views").
- **`some`**: line 372 "some: Budget use, Claims by status"; line 526 "HR sees Budget use and Claims by status only".
- **`profile`**: lines 372–373 "Company read only, Your profile".
- **`manage`**: line 374 "Company, Admins, Activity log, Your profile"; line 126.
- **`as role`**: line 368 "holds the HR manager or the finance manager role as well"; line 128.
- **Tone**: line 376 "Its rows take tone 4, Perqo Admin"; line 14. The figure draws no other tone.
- **Caption sources**:
  - Ferraiolo et al., TISSEC 4(3), 2001, and NIST RBAC FAQ: line 96.
  - NIST glossary for least privilege and separation of duty: line 118.
  - A.4 trace: line 364. Deliverable B: line 362. IA1 surfaces map: line 27.
  - The caption says Perqo is fictional.
- **(c) Kind**: roles by sections is items by sections, so matrix fits. Section 3.5 (line 136) names it "matrix".

## (c) Renderer notes
- **Desktop and tablet, dark and light:** one frame, and the whole figure fits. All text is inside its boxes, nothing overlaps, and the caption sits under the figure.
- **Phone (390 px), dark and light:** the figure is 213 px wider than its frame. It scrolls inside the frame, and the cue line "scroll sideways for the whole figure" is shown.
  - Across frames 1–3, every column, every cell and the end of every legend line is visible.
  - The edge fade dims words at a frame's edge (for example "resend," and "mark as left"), but each one is fully legible in another frame.
- **Phone opening frame:** the sticky section bar "Deliverable · The Perqo Admin IA" covers the column-head row. Frame 1 of the frames sheet shows the heads whole. This comes from the renderer, and no change to the declaration would fix it.
- **Blank cell:** the empty Approvals cell is drawn as a neutral filled box, not a tone. That is the renderer's style for an empty cell, and the caption's "a blank cell is …" explains it.
- **Phone width:** the six columns set the width, not the legend.
  - The longer `edit` note proposed above fits at desktop and tablet. On phone it only lengthens a legend line that already scrolls.
  - Splitting the set / view / all legend row would not make the figure narrower.

## (d) Verdict
Figure 5: **FIX**. The `edit` legend note must be corrected, and the caption should cite section 4.6 for the two reports HR sees.

## Figure 6 re-check 2 (Opus 5.5 agent, 3 November 2026; the third check of figure 6, sitemap: Admin's pages; given the unit without its figures, the captions and the frames sheets, nothing of the earlier reports; verbatim hand-back; the harness refused its `report.md` write, so the hand-back is the one copy)

Figure 6 (sitemap), IA7: FIX. Every label, identifier and note in the drawing traces to the unit's text, so there are no errors. Two notes don't follow the queue notation that C.1 sets out, so they are should-fix, and there are two minor findings. The harness refused the write to F/report.md, so this reply is the only copy.

## (a) Findings
- [should-fix] **Approvals (AD-4): queue with no [condition].** The note says "queue" but gives no condition. C.1 requires one (line 396: `"queue" with the queue's [condition]`), and so does the caption ("'queue' with its [condition]"). The other two queues have one. The condition comes from C.4, line 443: "over the policy's auto-approve limit; never the viewer's own claim (EX-1)". Replacement note: `AD-4 · queue [over the auto-approve limit], owned by HR; by policy, oldest first; opens claims → see AD-1.1.1`
- [should-fix] **Budgets (AD-2): queue with no owner.** The note has the queue and its condition but no owner. Line 396 asks for "the owner of its work queue", and Not joined already shows one ("owned by HR"). The owner comes from C.4, line 445: "finance manager". Replacement note: `AD-2 · by group and period; queue [no budgets set for the next period], owned by finance`
- [minor] **Employee (AD-1.1): Perqo card status needs a role.** The note lists "Perqo card status" with no role. Only HR sees the card (A.1, line 280: O-09, "Seen by | HR *new*"), and a finance manager also reaches this page. Replacement note: `AD-1.1 · one per employee; claims, budgets, Perqo card status (HR), History`
- [minor] **Caption sources incomplete.** Three sources are missing from the list:
  - section 3.2: Approvals hidden from finance (lines 110 and 386)
  - section 4.1: global routes by role (line 146), and the employee group's routes to its policy, employees and budgets (line 148)
  - A.1: Your profile for every admin user (line 273)

  Replacement for the caption's last source clause: `the rest set in sections 3.2 to 3.4, 4.1 to 4.6 and 5.3, Deliverable A, A.1, and Deliverable C, C.4 and C.5.`

## (b) Confirmed
- **Identifiers:** all 28 drawn identifiers and page names match line 400 exactly, with none missing and none extra. They are AD-0; AD-1, 1.1, 1.1.1, 1.2, 1.2.1, 1.2.2, 1.3, 1.4; AD-2, 2.1, 2.2; AD-3, 3.1, 3.1.1, 3.1.2; AD-4; AD-5, 5.1 to 5.5; AD-6, 6.1, 6.2, 6.2.1, 6.3, 6.4.
- **Root:**
  - It names the surface and has no type tag (line 396: "the root names the surface and carries no type tag").
  - "AD-1 to AD-6 are global routes, by role" comes from line 410: "Global | Employees, … Settings (IA1); by role *new*".
- **Order:** the six areas in IA1's order, then Sign in last (line 396: "The six areas keep IA1's order, and Sign in comes last").
- **Employees area:**
  - AD-1 "by name; filter by group; find": line 427, "name, alphabetical | employee group; status | name or work email".
  - AD-1.1 "claims, budgets, Perqo card status, History": line 148, "leads to their claims (R-08), their budgets (R-05) and their Perqo card's status (R-11)". History is on lines 167 and 227.
  - AD-1.1.1 placed under the employee: line 396, "A claim's page sits under its employee's record".
  - AD-1.1.1 "modal: Reject claim (HR)": line 173, "Reject opens a modal …; Reject claim moves it to Rejected", and line 344 (HR manager).
  - AD-1.2.1 "its policy, employees, budgets": line 148, "an employee group leads to its policy (R-03), its employees (R-04) and its budgets".
  - AD-1.2.2 and AD-1.3 marked HR: line 339.
  - AD-1.4 "queue [invited more than 14 days ago], owned by HR": line 444.
- **Budgets area:**
  - AD-2 "by group and period": line 431. Its queue condition is from line 445.
  - AD-2.1 "one group, one period": line 402, "/budgets/{employee group ID}/{period}".
  - AD-2.2 marked finance: line 343.
- **Policies area:**
  - AD-3 "one per employee group": line 411.
  - AD-3.1's attributes and History: lines 296 and 275.
  - AD-3.1.1 and AD-3.1.2 marked HR: line 340.
  - AD-3.1.2 "all view": lines 282 and 349.
- **Approvals (AD-4):**
  - "HR; by policy, oldest first": line 443, and lines 386 and 410 (HR only).
  - "opens claims → see AD-1.1.1": line 396, "Approvals and Claims by status open it there".
- **Reports area:**
  - AD-5 "views": line 396.
  - AD-5.1, AD-5.2 and AD-5.5 marked finance, with AD-5.3 and AD-5.4 unmarked: line 191, "Finance sees all five. HR sees Budget use and Claims by status".
  - AD-5.4 "opens claims → see AD-1.1.1": lines 396 and 346.
- **Settings area:**
  - AD-6.1 "owner edits": lines 272 and 336.
  - AD-6.2 owner: lines 338 and 386.
  - AD-6.2.1 owner: line 337.
  - AD-6.3 "owner; each entry opens its record": lines 350 and 396.
  - AD-6.4 "every admin user": lines 273 and 411.
- **Sign in (AD-0):** "Looking for your benefits? Get the Perqo app → see S-6" matches line 453.
- **Notation:**
  - The type tags SECTION, INDEX, STACK, DETAIL and FORM are defined on line 396, and each box's tag fits its page.
  - "→ see" is defined on line 396.
  - Every box is tone 4 and no other tone is drawn (lines 14 and 396).
- **Caption (check b):** it says what the figure shows, names Deliverable C, C.1, names its sources and says Perqo is fictional. It passes, apart from the minor gap in the source list above.
- **Kind (check c):** the data is a hierarchy of pages, so sitemap is the right kind.

## (c) Renderer notes
- **Second row is not a level.** The renderer wraps the root's seven children into two rows. The second row (Approvals, Reports, Settings, Sign in) hangs from the root's own bracket, not from Employees, so it reads correctly. The declaration cannot change this without breaking IA1's order, which line 396 fixes.
- **Phone width scrolls correctly.** The figure is wider than its frame and scrolls inside it, with the cue line "scroll sideways for the whole figure" and the caption under it. Each box appears whole in at least one of the four frames (15, 179, 343 and 372 px). The root is cut at the right edge in the opening frame and shown whole in frame 2. This comes from the renderer only.
- **Empty space on phone.** There is a large gap under the Policies column because the first row is as tall as the Employees subtree. This comes from the renderer only.
- **Sticky bar.** The opening frames at every width are clipped by the sticky section bar because the figure is taller than the viewport. The frames sheets show it whole. This comes from the renderer only, and the declaration cannot fix it.
- **Tablet and desktop, dark and light:** the whole figure fits in one frame, all text sits inside its boxes, nothing overlaps and the caption sits under the figure.

## (d) Verdict
Figure 6: **FIX**. There are two should-fix findings (Approvals has no [condition]; Budgets' queue has no owner) and two minor findings. There are no errors.

## Figure 7 re-check 1 (Opus 5.5 agent, 3 November 2026; the second check of figure 7, matrix: the navigation model; given the unit without its figures, the captions and the frames sheets, nothing of the earlier reports; verbatim hand-back; the harness refused its `report.md` write, so the hand-back is the one copy)

**Figure 7 (matrix), unit IA7: FIX.** The unit's text doesn't say Approvals has no local route, but the figure draws it. One clause added to the text fixes it, and the drawing needs no change. All 36 cells, the row labels and the column heads were checked against the text; everything else traces. The harness refused the write to report.md, so this reply is the only copy.

## (a) Findings

- **[error]** The Approvals row's local-routes cell reads `none: one list, grouped by policy`. "Grouped by policy" is in the text (lines 157, 433, 443), but the text never says Approvals has no local route. Line 411 (C.2, the Local row) lists local routes for Policies, Employees, Budgets, Reports and Settings and leaves Approvals out. "None" can only be inferred from that gap and from AD-4 having no child pages (line 400). Fix the text, not the figure. In line 411, replace `inside Settings, Company, Admins, Activity log and Your profile |` with `inside Settings, Company, Admins, Activity log and Your profile; inside Approvals, none: it is one list, grouped by policy (IA1) |`.
- **[minor]** The Work queue column has three blank cells (Policies, Reports, Settings). They are drawn in a neutral fill, not tone 4, and the caption doesn't say what a blank means; figure 5's caption does this for its own blanks. Add this caption sentence after `Rows tone 4, Perqo Admin.`: `A blank cell is an area with no work queue (Deliverable C, C.4).`
- **[minor]** The figure doesn't show the count on Approvals' global route. Line 410 says "Approvals shows the count of claims waiting for the viewer" and line 443 says "AD-4; count on the global route". The caption frames the figure as "which routes the navigation components must carry". Change the Approvals work-queue cell `Approvals` to `Approvals, count on the global route`. This is optional if the figure is meant to cover only local routes, queues and contextual routes.

## (b) Confirmed

**Row labels and column heads**
- **Row labels** (Employees, Budgets, Policies, Approvals, Reports, Settings): line 410, "Global | Employees, Budgets, Policies, Approvals, Reports, Settings (IA1)". The order matches IA1's order (line 146).
- **LOCAL ROUTES, CONTEXTUAL ROUTES OUT:** line 144, "local routes within one area, contextual routes from one item to related items". Route types per line 406.
- **WORK QUEUE:** line 69, "Work queue: whether anyone must act on some of them", and the C.4 heading, line 439.
- **ROLES:** Deliverable B, lines 370–374.

**Local routes (line 411)**
- `All employees, Employee groups, Not joined`: "inside Employees, All employees, Employee groups and Not joined".
- `current period, next period`: "inside Budgets, the current and the next period".
- `one per employee group`: "the policies inside Policies, one per employee group (IA2)".
- `the five reports`: "inside Reports, the five reports".
- `Company, Admins, Activity log, Your profile`: "inside Settings, Company, Admins, Activity log and Your profile".
- The Approvals cell is only partly traced; see the error.

**Work queues (C.4)**
- `Not joined`: line 444, "Not joined | employee, Invited | ... | HR manager | AD-1.4".
- `No budget for next period`: line 445, "... | finance manager | top of AD-2".
- `Approvals`: line 443, "Approvals | claim, Submitted | ... | HR manager | AD-4".
- Blank for the other three areas: C.4 names only these three queues (lines 443–445; line 529).

**Contextual routes out (line 412; line 148 says the same)**
- Employees `employee to claims, budgets, card status; group to policy, employees, budgets`: "from an employee's record to the claims they made ... to their budgets and their Perqo card's status; ... from an employee group to its policy, its employees and its budgets". Employee groups sit under Employees (AD-1.2, line 400).
- Budgets `budget to its employee group`: "from a budget to its employee group".
- Policies `policy to its employee group`: "from a policy to its employee group".
- Approvals `claim to employee, policy, budget`: "from a claim to its employee, its policy and its budget".
- Reports `report row to the records it sums`: "from a report row to the records it sums" (also line 191).
- Settings `audit entry to its record`: "from an audit entry to the record it changed". The Activity log is AD-6.3.

**Roles (lines 372–374)**
- Employees `HR edit; finance view`: HR "edit: create groups, invite, ..."; finance "view".
- Budgets `finance set; HR view`: finance "set: set budgets for a group"; HR "view".
- Policies `HR edit; finance view`: HR "edit: policy, covered items"; finance "view".
- Approvals `HR decide`: HR "decide: approve, reject, approve selected, ..."; finance "(not in navigation)". Line 410: "a finance manager's navigation has no Approvals".
- Reports `finance all five; HR two`: finance "all five reports"; HR "some: Budget use, Claims by status". Line 191: "Finance sees all five. HR sees Budget use and Claims by status".
- Settings `owner all; others Company read only and Your profile`: account owner "manage: Company, Admins, Activity log, Your profile"; HR and finance "profile: Company read only, Your profile".

**Tone:** rows are tone 4, from line 417, "The same model as a matrix, one row per area. Its rows take tone 4, Perqo Admin.", and line 14. No other tone is drawn.

**Caption (b):** it says what the figure shows, names its section (Deliverable C, C.2) and sources, and says Perqo is fictional. It passes apart from the blank-cell sentence. Its sources match the text:
- Rosenfeld, Morville and Arango 2015, ch. 8, through IA2, section 1.4 (line 144).
- IA2, section 5.3's Admin column kept (line 406).
- Deliverable A, A.3, following Prater 2015 (line 148).
- C.4 and Deliverable B.

"IA1's surfaces map" is not in the unit's text, which says "IA1's six areas" (line 144). Figures 5 and 6 use the same phrase, so it is a reference to IA1 and not a finding against this figure.

**Kind (c):** a matrix fits. The data is six areas by route type, queue and role, and the text calls it "the same model as a matrix, one row per area" (line 417).

**Notation (d):** one tone, and it is named in the text. This matrix needs no page-type tags, "-> verb" or bracketed conditions. The one count in scope (Approvals) is not drawn; see the second minor finding.

## (c) Renderer notes

**Desktop and tablet, light and dark:** the whole figure fits in one frame. Text stays inside its boxes, nothing overlaps, the caption sits under the figure, and both themes are legible.

**Phone (390 px), light and dark:** the figure is 372 px wider than its frame and scrolls inside it.
- The area-label column stays fixed, the cue line "scroll sideways for the whole figure" shows, and the caption sits underneath.
- The four sampled frames (at 0, 164, 328 and 372 px) each show one column whole: Local routes in frame 1, Work queue in frame 2, Roles in frame 4.
- Contextual routes out is never whole in a sampled frame. Its left half is in frame 2 and its right half in frame 3, so every word shows in some frame. A reader stopping at about 230–260 px sees the column whole.
- Text dims where it fades at the frame edges, and the same text is clear in the next frame.

These phone notes depend only on how the renderer picks frames and fades the edges. The declaration could narrow that column by shortening the Employees contextual cell, for example to `employee to claims, budgets, card; group to policy, employees, budgets`. That isn't needed: four content columns can't fit 390 px with any labels, and the scroll and its cue work.

## (d) Verdict

Figure 7: **FIX**. The error is fixed by the line-411 clause in the unit's text. The two minor fixes are the caption sentence and the optional Approvals count.

## Figure 5 re-check 2 (Opus 5.5 agent, 3 November 2026; the third check of figure 5, matrix: the role-by-section matrix; given the unit without its figures, the captions and the frames sheets, nothing of the earlier reports; verbatim hand-back; the harness refused its `report.md` write, so the hand-back is the one copy)

Figure 5 (matrix) in IA7: FIX. The drawing matches the unit: every label, number and note traces to the text, the caption is complete, a matrix is the right kind, and it is legible at every width and theme. The one should-fix is that two legend entries do not name the calls to action the way the caption says they do. The harness refused the write to F/report.md, so this reply is the only copy.

## (a) Findings

- **[should-fix] Legend entries `edit` and `set` do not use A.4's calls to action in "-> verb" form.** The caption says the legend names "the calls to action in Deliverable A, A.4". The `decide` entry does this ("-> approve, -> reject, -> approve selected"). The `edit` and `set` entries give B.1's short forms instead ("create groups", "resend", "move"). Replacements:
  - `edit`: `Employees: -> create (employee group), -> invite, -> invite employees, -> resend invitation, -> move to group, -> mark as left; Policies: -> edit, -> add covered items`
  - `set`: `-> set for a group (Set budgets)`
  - Source rows in A.4: "employee group | -> create; -> invite employees", "employee | -> invite; -> move to group", "employee | -> resend invitation *new*; -> mark as left *new*", "policy | -> edit; -> add covered items", "allocation | -> set for a group".
- **[minor] The condition in the `decide` entry is worded differently from A.4.** It reads "[never their own claim]", while A.4 says "never on their own claim". Replacement: `[never on their own claim]`.
- **[minor] Unit text, B.1, the HR manager row's Approvals cell** says "except their own claims", which also differs from A.4. Replacement: `decide: approve, reject, approve selected, never on their own claim`.
- **[minor] At phone width, one word is never shown at full contrast.** The fade at the edge of the sticky row-label column dims legend text passing under it. The word "never" in the `decide` line is dimmed in frames 1 and 2, and in frame 3 "their" reads as "the r". It can still be read. The declaration could avoid this by putting the condition on its own line, or by giving `set`, `view` and `all` a row each.

## (b) Confirmed

- **Column heads** EMPLOYEES, BUDGETS, POLICIES, APPROVALS, REPORTS, SETTINGS, in this order: section 4.1, "IA1's six areas, Employees, Budgets, Policies, Approvals, Reports and Settings"; B.1 header row and "IA1's order".
- **Row labels** HR manager, Finance manager, Account owner: the B.1 rows, and section 3.4, "one more row in the role matrix, and that is how the matrix draws it".
- **HR manager row** (edit, view, edit, decide, some, profile): B.1, "edit: create groups, invite, resend, move, mark as left | view | edit: policy, covered items | decide: … except their own claims | some: Budget use, Claims by status | profile: Company read only, Your profile".
- **Finance manager row** (view, set, view, blank, all, profile): B.1, "view | set: set budgets for a group | view | (not in navigation) | all five reports | profile". The blank Approvals cell matches B.1, "A blank cell means the area is not in that role's navigation", and section 3.2, "Approvals is not in the finance manager's global navigation".
- **Account owner row** (as role five times, then manage): B.1, "its row reads "as role" except in Settings" and "manage: Company, Admins, Activity log, Your profile".
- **Legend `edit`**: the B.1 cells. "Edit policy" is AD-3.1.1 and appears in section 4.3; "add covered items" is in A.4.
- **Legend `decide`**: A.4, "-> approve; -> reject | HR manager, never on their own claim" and "-> approve selected *new*".
- **Legend `set`**, "set budgets for a group": B.1.
- **Legend `view`**, "read only": B.2, "read only: no edit actions", and section 3.2.
- **Legend `all`**, "all five reports": B.1, and section 4.6, "Finance sees all five".
- **Legend `some`**, "Budget use and Claims by status only": section 4.6, and the facts table, "HR sees Budget use and Claims by status only".
- **Legend `profile`** and **`manage`**: B.1 and section 3.4.
- **Legend `as role`**, "what the holder's HR or finance role gives": B.1, and section 3.4, "the person still does HR's or finance's work under their role".
- **(d) Tone:** every cell is drawn in one fill, which is tone 4. Line 376 says "Its rows take tone 4, Perqo Admin", and line 14 names tone 4. No other tone is drawn; the blank cell is an empty cell, not a tone.
- **(b) Caption:** it says what the figure shows and names Deliverable B. Its sources are all in the text:
  - areas from IA1's surfaces map (line 27);
  - roles from IA1, section 5, and IA4, A.1;
  - the hidden Approvals route, separation of duty and the account owner from sections 3.2 to 3.4;
  - HR's two reports from section 4.6;
  - Ferraiolo 2001 and the NIST RBAC FAQ from section 3.1, and the NIST glossary from section 3.3.
  
  It says "Perqo is fictional". No finding.
- **(c) Kind:** roles by sections is items by sections, so a matrix fits. No finding.

## (c) Renderer notes

- **Desktop and tablet, light and dark:** the figure fits in one frame. Text sits inside its boxes, nothing overlaps, and the caption is under the figure.
- **Phone, light and dark:** the figure is wider than its frame and scrolls sideways, with the cue line "scroll sideways for the whole figure". The frames at 0, 164 and 213 of 213 px between them show every column and every legend word. The row labels stay fixed while the rest scrolls, so the legend is cut at the left in frames 2 and 3, but every part is whole in some frame.
- **Phone opening frame:** the column-head row sits under the sticky section bar ("SECTION 7 OF 9"); the frames sheet shows the heads. This comes from the sticky bar, and the declaration cannot change it.
- **The fade at the edge of the label column** dims the "never" note above. This rests on the renderer; the declaration could avoid it by splitting the `decide` line or stacking `set`, `view` and `all`.
- **Legend layout:** the extra gap under the three-line `edit` entry and the packing of `set`, `view` and `all` onto one row are the renderer's choices.
- **Blank cell:** it is a lighter fill in light theme and a darker fill in dark theme, and reads as empty in both.

## (d) Verdict

Figure 5: FIX, for the one should-fix (`edit` and `set` legend entries into A.4's "-> verb" names).

## Figure 6 re-check 3 (Opus 5.5 agent, 3 November 2026; the fourth check of figure 6, sitemap: Admin's pages; given the unit without its figures, the captions and the frames sheets, nothing of the earlier reports; verbatim hand-back; the harness refused its `report.md` write, so the hand-back is the one copy)

**Figure 6 passes.** Every label, ID and note in the drawing traces to the unit's text. I found no error and no should-fix, only four optional minors. The report file was not saved because the harness refused the write, so this reply is the only copy.

I read all 12 sheets: desktop, tablet and phone (390 px), each dark and light, opening frames and frames sheets. The phone frames sheets were too tall to read whole, so I cut them into crops inside the folder (`.../f6r3/crops/`). Line numbers below refer to `F/unit-without-figures.md`.

## (a) Findings

- [minor] **AD-4 Approvals, queue condition is half there.** C.4 (line 443) gives the condition as "over the policy's auto-approve limit; never the viewer's own claim (EX-1)". The figure draws only the first half. Replacement note: `AD-4 · queue [over the policy's auto-approve limit; not the viewer's own claim], owned by HR; by policy, oldest first; opens claims → see AD-1.1.1`
  - A note on the unit's text, outside figure 6:
    - Section 4.3 (line 173) says "The HR manager's own claim opens in a state where Approve and Reject are unavailable".
    - Section 3.3 (line 120) says the own claim "waits in Approvals for another HR manager".
    - Neither contradicts C.4, but read in order they suggest the claim sits in the HR manager's own Approvals list. This needs checking against figure 1.
- [minor] **The Approvals count is not drawn.** Line 410 says "Approvals shows the count of claims waiting for the viewer" and line 443 says "AD-4; count on the global route". To add it, append `; count on the global route` to the AD-4 note. This is optional, because a sitemap draws pages, not navigation components.
- [minor] **Notes carry more than C.1 lists.** Line 396 lists what notes carry: page ID, roles or queue owner, "queue" with its [condition], "views" and "→ see". The notes also say what a page holds or how its list is ordered, for example "by name; filter by group; find", "claims, budgets, Perqo card status (HR), History", "modal: Reject claim (HR)" and "one group, one period". All of these are traced below.
  - Replacement for line 396's sentence: `Notes carry the page ID, the roles that reach the page when not all do or the owner of its work queue, "queue" with the queue's [condition], "views" for the reports, "→ see" for a route drawn elsewhere, and, where it decides the page, what the page holds or how its list is ordered.`
  - Matching caption sentence: `Notes give the page ID, roles where not all reach it or the owner of a queue, 'queue' with its [condition], 'views', what a page holds or how its list is ordered where that decides it; '→ see' points to a page or surface drawn elsewhere.`
- [minor] **Sign in note quotes the screen without quotation marks.** As drawn, the screen's wording reads like the note's own words. Replacement note: `AD-0 · line "Looking for your benefits? Get the Perqo app" → see S-6`

## (b) Confirmed

**Identifiers.** All 29 page IDs and names match line 400 one for one, from AD-0 Sign in to AD-6.4 Your profile. Nothing is missing or extra. The drawn order is Employees, Budgets, Policies, Approvals, Reports, Settings, Sign in, as line 396 says: "The six areas keep IA1's order, and Sign in comes last".

**Root and tags.**
- Root "Perqo Admin · the surface; AD-1 to AD-6 are global routes, by role", with no type tag. Line 396: "the root names the surface and carries no type tag". Line 410: "Global | Employees, Budgets, … Settings (IA1); by role *new*".
- Tags SECTION, INDEX, STACK, DETAIL and FORM are defined on line 396. No other tag is drawn.

**Employees area (AD-1)**

| Box and note | Traced to |
|---|---|
| AD-1 "by name; filter by group; find" | line 167 "employees alphabetically by name, filtered by employee group"; line 427 Find "name or work email" |
| AD-1.1 "one per employee; claims, budgets, Perqo card status (HR), History" | line 412 "to their budgets and their Perqo card's status"; line 348 "card \| -> view status \| HR manager \| … (AD-1.1)"; line 165 the detail holds "its History" |
| AD-1.1.1 "one per claim; modal: Reject claim (HR)" | line 173 "Reject opens a modal … Reject claim moves it to Rejected"; line 344 "approve; reject \| HR manager"; line 396 "A claim's page sits under its employee's record" |
| AD-1.2 | lines 400 and 428 |
| AD-1.2.1 "its policy, employees, budgets" | line 412 "from an employee group to its policy, its employees and its budgets" |
| AD-1.2.2 · HR and AD-1.3 · HR | line 339 "employee group \| -> create; -> invite employees \| HR manager \| Employees (AD-1.2.2; AD-1.3)" |
| AD-1.4 "queue [invited more than 14 days ago], owned by HR" | line 444 "invited more than 14 days ago \| HR manager \| AD-1.4" |

**Budgets area (AD-2)**

| Box and note | Traced to |
|---|---|
| AD-2 "by group and period; queue [no budgets set for the next period], owned by finance" | line 431 "employee groups by period"; line 445 "no budgets set for the next period \| finance manager \| top of AD-2" |
| AD-2.1 "one group, one period" | line 402 "/budgets/{employee group ID}/{period}"; line 411 "the current and the next period". The phrase is not verbatim, but the meaning is in the text. |
| AD-2.2 · finance | line 343 "allocation \| -> set for a group \| finance manager \| Budgets (AD-2.2)" |

**Policies area (AD-3)**

| Box and note | Traced to |
|---|---|
| AD-3 "one per employee group" | line 411 |
| AD-3.1 "open categories, auto-approve limit, covered items, History" | line 296 (the three attributes); line 275 "History records each change" |
| AD-3.1.1 · HR and AD-3.1.2 "HR adds; all view" | line 340 "policy \| -> edit; -> add covered items \| HR manager \| Policies (AD-3.1.1; AD-3.1.2)"; line 282 seen by "all"; line 349 |

**Approvals and Reports (AD-4, AD-5)**

| Box and note | Traced to |
|---|---|
| AD-4 "queue [over the policy's auto-approve limit], owned by HR; by policy, oldest first; opens claims → see AD-1.1.1" | line 443 (condition, "HR manager", "grouped by policy, oldest first"); line 396 "Approvals and Claims by status open it there" |
| AD-5 · views | line 396 "'views' for the reports"; line 191 "Reports holds five views" |
| AD-5.1 and AD-5.2 · finance; AD-5.3 with no role; AD-5.5 · finance | line 191 "Finance sees all five. HR sees Budget use and Claims by status"; line 347 |
| AD-5.4 "opens claims → see AD-1.1.1" | line 346 |

**Settings and Sign in (AD-6, AD-0)**

| Box and note | Traced to |
|---|---|
| AD-6.1 "owner edits" | line 336 "edit company details \| account owner \| … (AD-6.1)"; line 372 "Company read only" |
| AD-6.2 · owner and AD-6.2.1 · owner | lines 337 and 338; line 386 |
| AD-6.3 "owner; each entry opens its record" | line 396 "each entry of the Activity log opens its record"; line 350 |
| AD-6.4 "every admin user" | line 273 "all see their own profile"; line 268 "'all' means every admin user" |
| AD-0 "Looking for your benefits? Get the Perqo app → see S-6" | line 453 |

**Tone.** One tone, 4, on every box including the root. Line 14: "Admin's boxes take tone 4, Perqo Admin". Line 396: "Every box is tone 4". No other tone is drawn.

**Caption (check b): pass.** It says what the figure shows, names its section (Deliverable C, C.1) and its sources, and ends "Perqo is fictional." The sources all exist in the unit:
- IA1's surfaces map: line 27.
- IA2, section 5.3: line 411.
- IA4, section 4.3: line 23.
- Sections 3.2 to 3.4, 4.1 to 4.6 and 5.3, A.1, C.4 and C.5 are all present as headings.

**Kind (check c): pass.** A hierarchy of pages is a sitemap.

**Notation (check d): pass, apart from the minors.** Type tags follow line 396, conditions sit in square brackets, "→ see" is used as line 396 states, and the one tone drawn is named in the text. No "-> verb" is drawn, which is right for a sitemap.

**Legibility (check e): pass at every width and theme.**
- Desktop and tablet, dark and light: the whole figure fits one frame. All text is inside its box, nothing overlaps, and the caption is under the figure.
- Phone: the figure is 372 px wider than its frame and scrolls across 4 frames, with the cue line "scroll sideways for the whole figure" and the caption under it. Each box is whole in at least one frame:
  - Frame 1: the Employees column and Approvals.
  - Frames 1 and 2: the Budgets and Reports columns.
  - Frame 3: the Policies and Settings columns.
  - Frame 4: Sign in.

## (c) Renderer notes

These rest only on how the renderer lays the figure out.
- **Two rows of children.** The root's seven children wrap into two rows, the second hanging from a bus line down the left, so it can look like a deeper level. A row is not a level. The declaration cannot change this without breaking IA1's order, which line 396 keeps.
- **Blank band.** The tall Employees subtree leaves a large blank band under Budgets and Policies, which shows as a long empty stretch on phone frames 3 and 4. Shorter Employees notes would reduce it only slightly.
- **Opening frames clipped.** At every width and theme the sticky section bar ("Section 7 of 9") covers the second level, for example Claim and Edit policy. Every frames sheet shows those boxes whole. This is a page and renderer matter.
- **Faded edges on phone.** Boxes at a frame's edge fade out as the scroll cue; this is not a cut. Each faded box is whole in another frame, for example Sign in in frame 4 and Add admin user in frame 3.

## (d) Verdict

Figure 6 PASS.

## Figure 7 re-check 2 (Opus 5.5 agent, 3 November 2026; the third check of figure 7, matrix: the navigation model; given the unit without its figures, the captions and the frames sheets, nothing of the earlier reports; verbatim hand-back; the harness refused its `report.md` write, so the hand-back is the one copy)

Figure 7 (the navigation-model matrix in IA7): FIX. Two labels in the drawing are not written in the unit's text. The harness refused the write to F/report.md, so this reply is the only copy.

## (a) Findings

- [error] The column header `CONTEXTUAL ROUTES OUT`: the unit's text never says "routes out". Line 412 and section 4.1 (line 144) say "contextual routes", and only the caption adds "out". Fix it in one of two ways:
  - Change the drawing's header to `CONTEXTUAL ROUTES`.
  - Or keep the header and change line 417 to `The same model as a matrix, one row per area of the global navigation: its local routes, its work queue, its contextual routes out and the roles that reach it. Its rows take tone 4, Perqo Admin.` This also closes the minor note on line 417 below.
- [error] Roles cell, Reports row, `finance all five; HR two`: the number "two" for HR's reports is not in the unit's text. Line 191 names the reports ("HR sees Budget use and Claims by status, and not the other three") but never counts them. "the two reports HR sees" appears only in figure 5's caption. Fix it in one of two ways:
  - Change line 191 to `HR sees two, Budget use and Claims by status, and not the other three: ...`. This is the better fix because it keeps the cell short at phone width.
  - Or change the label to `finance all five; HR Budget use, Claims by status`.
- [minor] Line 417, `The same model as a matrix, one row per area.`, does not say what the four columns are, that the rows are the global routes, or that the C.2 table's Supplemental row is left out. The caption names the columns, but the text does not. Use the replacement line given in the first finding.
- [minor] Roles cell, Approvals row, `HR decide`: leaving finance out of this cell is the only place the figure shows line 410's *new* rule, "a finance manager's navigation has no Approvals". The cell is correct as it stands, because the caption says the column holds "the roles that reach each". If you want the rule shown explicitly, use `HR decide; not in finance's navigation`. This one is optional.

## (b) Confirmed

**Rows.** Employees, Budgets, Policies, Approvals, Reports, Settings come from line 410: "Global | Employees, Budgets, Policies, Approvals, Reports, Settings (IA1)".

**Local routes** (all from line 411):
- `All employees, Employee groups, Not joined`: "inside Employees, All employees, Employee groups and Not joined".
- `current period, next period`: "inside Budgets, the current and the next period".
- `one per employee group`: "the policies inside Policies, one per employee group (IA2)".
- `none: one list, grouped by policy`: "inside Approvals, none: it is one list, grouped by policy (IA1)".
- `the five reports`: "inside Reports, the five reports".
- `Company, Admins, Activity log, Your profile`: "inside Settings, Company, Admins, Activity log and Your profile".

**Work queue** (C.4, lines 443 to 445):
- `Not joined`: "Not joined | employee, Invited | … | AD-1.4".
- `No budget for next period`: "No budget for next period | employee group | … | top of AD-2".
- `Approvals, count on the global route`: "Approvals | claim, Submitted | … | AD-4; count on the global route". Line 410 also says "Approvals shows the count of claims waiting for the viewer".
- The blank cells for Policies, Reports and Settings are correct: C.4 has no queue in those areas, and the caption states the blank-cell rule.

**Contextual routes** (line 412; relationships in line 148):
- `employee to claims, budgets, card status; group to policy, employees, budgets`: "from an employee's record to the claims they made", "to their budgets and their Perqo card's status", "from an employee group to its policy, its employees and its budgets". "card status" also matches line 321, "R-11 … Perqo card status".
- `budget to its employee group`: "from a budget to its employee group".
- `policy to its employee group`: "from a policy to its employee group".
- `claim to employee, policy, budget`: "from a claim to its employee, its policy and its budget".
- `report row to the records it sums`: "from a report row to the records it sums".
- `audit entry to its record`: "from an audit entry to the record it changed". Line 437 places audit entries in the Activity log, inside Settings.

**Roles** (B.1, lines 372 to 374):
- Employees, `HR edit; finance view`: HR manager "edit: create groups, invite, …"; Finance manager "view".
- Budgets, `finance set; HR view`: Finance manager "set: set budgets for a group"; HR manager "view".
- Policies, `HR edit; finance view`: HR manager "edit: policy, covered items"; Finance manager "view".
- Approvals, `HR decide`: HR manager "decide: approve, reject, approve selected, …"; Finance manager "(not in navigation)".
- Reports, `finance all five; HR two`: Finance manager "all five reports"; HR manager "some: Budget use, Claims by status". "two" is not written (error above).
- Settings, `owner all; others Company read only and Your profile`: Account owner "manage: Company, Admins, Activity log, Your profile"; the other roles "profile: Company read only, Your profile".

**Tone.**
- Every filled cell is tone 4, matching line 417 ("Its rows take tone 4, Perqo Admin") and line 14, which names tone 4 for Admin.
- The empty cells use a neutral empty fill, not a tone.
- No other tone is drawn.

**Caption.**
- It says what the figure shows and at what fidelity (F2, matching line 406's "at F2").
- It names the decision and the section (Deliverable C, C.2), and it says "Perqo is fictional".
- Every source it names appears in the unit's text:
  - Rosenfeld, Morville and Arango 2015, ch. 8, through IA2, section 1.4: line 144.
  - IA1's surfaces map: line 27.
  - IA2, section 5.3's Admin column kept: line 406.
  - Deliverable A, A.3 relationships, following Prater 2015: line 148.
  - Queues from C.4: line 157 and C.4 itself.
  - Roles from Deliverable B: lines 370 to 374.

**Kind.** The data is areas by route types, which is items by sections, so a matrix fits.

**Notation.** Nothing in this figure calls for page-type tags, "→ verb", [conditions] or counts. The two counts it does carry are "five" and "two"; "two" is the error above.

**Legibility.**
- **Desktop and tablet, dark and light:** the whole figure fits in one frame. Text sits inside its boxes, nothing overlaps, and the caption is under the figure.
- **Phone, dark and light:** the figure is 372 px wider than its frame, so it scrolls in its frame.
  - The row-label column stays in place, and the cue line "scroll sideways for the whole figure" is under the figure.
  - Frames 1 to 4 (scrolled to 0, 164, 328 and 372 px) together show every cell, and the caption is under the figure.
  - The three lines of the Settings roles cell fit inside the box.

## (c) Renderer notes

- **Fade-edge glyph.** At phone width the cells slide under the fixed row-label column with a fade. In frame 2 (dark), a faint stray glyph from the Settings local-routes cell shows at the fade's edge. This comes from the renderer's scroll fade, not the declaration, and the declaration cannot fix it.
- **Header and Employees cell never whole in one frame.** At phone width no single frame shows the whole `CONTEXTUAL ROUTES OUT` header or the whole Employees contextual cell: frame 2 cuts them on the right and frame 3 on the left. Both fit at a scroll position between the sampled frames, so this rests only on where the frames are sampled. The shorter header `CONTEXTUAL ROUTES` from the first finding would also make the header fit in more frames.
- **Phone opening frame.** The opening frame cuts the Work queue column at its right edge. This is expected for a figure that scrolls sideways, and the cue line is there.

## (d) Verdict

Figure 7: FIX. Both errors can be fixed in the unit's text (lines 417 and 191) with the drawing left unchanged, or by editing the drawing's header and Reports roles cell instead.

## Figure 5 re-check 3 (Opus 5.5 agent, 3 to 4 November 2026; the fourth check of figure 5, matrix: the role-by-section matrix; given the unit without its figures, the captions and the frames sheets, nothing of the earlier reports; verbatim hand-back; the harness refused its `report.md` write, so the hand-back is the one copy)

Figure 5 (matrix) check: IA7, Level 3 · the backoffice. The verdict is FIX: two should-fix findings, two minor, no errors. Every label, mark and note in the drawing traces to the unit's text. Writing `F/report.md` was refused by the harness, so this reply is the only copy.

## (a) Findings

- **[should-fix] The `manage` key lists pages, not calls to action.**
  - The legend says "Company, Admins, Activity log, Your profile".
  - The caption, and the Deliverable B face at line 364, say the legend names "the calls to action in Deliverable A, A.4". A.4 gives the account owner's calls to action in Settings (lines 336 to 338).
  - Replace the key's note with `-> edit company details, -> add, -> remove, -> change role, -> make account owner; Activity log, Your profile`.

- **[should-fix] The caption's claim about the legend does not hold.** The keys `view`, `all`, `some`, `profile` and `as role` name pages, reports or a rule, not calls to action.
  - In the caption, replace `with a legend naming the calls to action in Deliverable A, A.4` with `with a legend naming, for each mark, the calls to action in Deliverable A, A.4 or the pages and reports it opens`.
  - The unit's Deliverable B face (line 364) needs the matching change: `with a legend naming, for each mark, the calls to action in A.4 or the pages and reports it opens`.

- **[minor] The `edit` key runs two columns' calls to action together.** The mark "edit" stands in both Employees and Policies, but the note splits them only by a semicolon.
  - Replace it with `-> create group, -> invite, -> move to group, -> resend invitation, -> mark as left (Employees); -> edit, -> add covered items (Policies)`.

- **[minor] The caption uses "ACM TISSEC 4(3)", a form the unit never uses.** The text and the Sources give the journal in full (lines 96 and 545).
  - Optional replacement: `role model from Ferraiolo and others, ACM Transactions on Information and System Security 4(3), 2001, and NIST's RBAC FAQ`.

## (b) Confirmed

**Headings and rows**
- **Column heads**, EMPLOYEES … SETTINGS in IA1's order. Line 370: "| Role | Employees | Budgets | Policies | Approvals | Reports | Settings |". Line 368: "Admin's six areas as columns, IA1's order".
- **Row labels** HR manager, Finance manager, Account owner: lines 372 to 374.
- **HR row** (edit, view, edit, decide, some, profile). Line 372: "edit: create groups, invite, resend, move, mark as left | view | edit: policy, covered items | decide: approve, reject, approve selected, never on their own claim | some: Budget use, Claims by status | profile: Company read only, Your profile".
- **Finance row** (view, set, view, blank, all, profile). Line 373: "view | set: set budgets for a group | view | (not in navigation) | all five reports | profile: …".
- **Account owner row** (as role five times, then manage). Line 374: "as role | as role | as role | as role | as role | manage: Company, Admins, Activity log, Your profile".
- **The blank cell.**
  - Line 368: "A blank cell means the area is not in that role's navigation".
  - Line 110: "Approvals is not in the finance manager's global navigation".
  - Line 146: "a finance manager's navigation has five areas, without Approvals".

**Legend keys**
- **`edit`**: A.4, lines 339 to 342.
  - "employee group | -> create; -> invite employees"
  - "policy | -> edit; -> add covered items"
  - "employee | -> invite; -> move to group"
  - "employee | -> resend invitation *new*; -> mark as left *new*"
  - "Create group" is the form's name (lines 169 and 400: "AD-1.2.2 Create group").
- **`decide`**, "-> approve, -> reject, -> approve selected [never on their own claim]".
  - Lines 344 and 345: "HR manager, never on their own claim".
  - The square-bracket condition follows the notation at line 396 ("queue" with the queue's [condition]).
  - The rule itself is at line 120.
- **`set`**, "-> set for a group (Set budgets)".
  - Line 343: "allocation | -> set for a group | finance manager | Budgets (AD-2.2)".
  - Line 400: "AD-2.2 Set budgets".
- **`view`**, "read only". Line 388: "The role may see but not change | read only: no edit actions | Policies and Employees for a finance manager; Budgets for an HR manager".
- **`all`**, "all five reports". Line 373, and line 191: "Finance sees all five."
- **`some`**, "Budget use and Claims by status only". Line 191: "HR sees two, Budget use and Claims by status". Also line 372.
- **`profile`**, "Company read only, and Your profile". Lines 372 and 373.
- **`manage`**, "Company, Admins, Activity log, Your profile". Line 374, and line 126 (the account owner "edits the company details, adds and removes admin users, changes an admin user's role, reads the Activity log").
- **`as role`**, "what the holder's HR or finance role gives".
  - Line 368: "holds the HR manager or the finance manager role as well, so its row reads 'as role' except in Settings".
  - Also line 128.

**Notation, kind and caption**
- **Tone (d).** Every mark cell and key is tone 4. Line 376: "Its rows take tone 4, Perqo Admin." Line 14: "Admin's boxes take tone 4". No other tone is drawn; the blank cell is a neutral empty fill.
- **Kind (c).** Roles by sections is items by sections, so a matrix fits. Line 136: "Role-by-section matrix | matrix | F2 in design, one mark per cell".
- **Caption (b).** It says what the figure shows and names its section (Deliverable B; sections 3.2 to 3.4 and 4.6). Its sources trace as follows:
  - IA1's surfaces map: line 27.
  - IA1, section 5 and IA4, A.1 for the roles: lines 12 and 294.
  - Ferraiolo 2001 and the NIST RBAC FAQ: line 96.
  - NIST's glossary: line 118.
  - It ends "Perqo is fictional."

## (c) Renderer notes

- **Desktop and tablet, both themes.** One frame ("the whole figure fits"). Text sits inside its boxes, nothing overlaps, and the caption is under the figure.
- **Phone, both themes: the figure scrolls.**
  - The figure is 213 px wider than its frame. It scrolls across three frames (0, 164 and 213 px), with the cue line "scroll sideways for the whole figure" above the caption.
  - Every cell and key note is fully shown in some frame. The SETTINGS column, the "all five reports" key and "[never on their own claim]" appear in full only in frames 2 and 3.
  - The edge fades on cut cells are the renderer's.
- **Phone, opening frame: the column heads are hidden.** They sit under the sticky section bar ("Section 7 of 9 · Deliverable"); the frames sheet shows them. This rests only on the renderer, and the declaration cannot change it.
- **Phone: key layout.** The renderer packs the short keys set, view and all on one line, which pushes `view` and `all` past the right edge of the opening frame.
  - The scroll itself comes from the six-column matrix, and shorter labels would not fit it into 390 px.
  - Declaring `view` and `all` before `decide`, or giving each its own line, would bring them into the opening frame.
- **Blank cell.** It is a neutral fill: light grey in light mode, near-background in dark mode. It reads as a cell in both themes, and the caption explains it.

## (d) Verdict

Figure 5: **FIX**.

## Figure 6 re-check 4 (Opus 5.5 agent, 3 to 4 November 2026; the fifth check of figure 6, sitemap: Admin's pages; given the unit without its figures, the captions and the frames sheets, nothing of the earlier reports; verbatim hand-back; the harness refused its `report.md` write, so the hand-back is the one copy)

Figure 6 (sitemap) check, IA7 · Level 3 · the backoffice. Verdict: **FIX**. There is one should-fix and no errors.

The harness refused the write to F/report.md (subagents may not write report files), so this reply is the only copy.

## (a) Findings

- **[should-fix] The Approvals (AD-4) note does not show that finance cannot reach the page.**
  - The note says only "owned by HR". Budgets uses the same wording ("owned by finance"), and every role reaches Budgets.
  - The caption says notes give "roles where not all reach it", so a reader will take Approvals to be reached by every role.
  - The unit says finance cannot reach it: "Approvals is not in the finance manager's global navigation" (line 110); "a finance manager's navigation has five areas, without Approvals" (line 146); B.1 marks it "(not in navigation)" (line 373).
  - This is the main reach decision of section 3.2, and the figure does not show it. Replacement note, which also shortens it:
    `AD-4 · HR only; queue [over the policy's auto-approve limit]; by policy, oldest first; count on the global route; opens claims → see AD-1.1.1`
- **[minor] The caption does not cite two of the figure's sources.**
  - The role marks on the forms and on Covered items ("HR", "finance", "owner", "HR adds; all view") come from A.4 (lines 336 to 349).
  - The list orders ("by name", "by group and period") come from C.3 (lines 427 and 431).
  - Replacement last sentence of the caption:
    `Six areas from IA1's surfaces map, kept; Policies one per employee group from IA2, section 5.3; Reports as views from IA4, section 4.3; the rest set in sections 3.2 to 3.4, 4.1 to 4.6 and 5.3, Deliverable A, A.1 and A.4, and Deliverable C, C.3 to C.5. Perqo is fictional.`
- **[minor] The Budgets queue has no name in the figure.**
  - The text names it "No budget for next period" (lines 157 and 445). Not joined and Approvals carry their names because they are pages.
  - Optional replacement note:
    `AD-2 · by group and period; queue No budget for next period [no budgets set for the next period], owned by finance`
  - The condition already traces as drawn, so the note can stay if the extra length is unwanted.
- **[minor, unit text] A route and its page have different names.**
  - C.2 (line 411) names a local route "All employees" inside Employees, but the page is "Employees" (AD-1) in line 400 and in the figure.
  - Replacement in C.2:
    `*new*: inside Employees, Employees (AD-1, all employees), Employee groups and Not joined`

## (b) Confirmed

| Figure label or note | Traced to |
|---|---|
| All 28 pages, AD-0 to AD-6.4, with their labels | The identifier list, line 400 (none missing, none extra) |
| Root "Perqo Admin · the surface; AD-1 to AD-6 are global routes, by role", no type tag | Line 396 (no type tag); lines 146 and 410 (routes by role) |
| Type tags SECTION, INDEX, STACK, DETAIL, FORM | Defined in line 396; every box fits its tag |
| Order: six areas in IA1's order, Sign in last | Line 396; line 144 |
| AD-1 "by name; filter by group; find" | Line 165; C.3, line 427 |
| AD-1.1 "one per employee; claims, budgets, Perqo card status (HR), History" | Line 148; O-09 seen by HR, line 280; History, line 167 |
| AD-1.1.1 "modal: Reject claim (HR)" | Line 173; A.4, line 344 |
| AD-1.2.1 "its policy, employees, budgets" | Line 148 |
| AD-1.2.2 "HR"; AD-1.3 "HR" | A.4, lines 339 and 341 |
| AD-1.4 "queue [invited more than 14 days ago], owned by HR" | C.4, line 444 |
| AD-2 queue condition, owned by finance | C.3, line 431; C.4, line 445 ("top of AD-2") |
| AD-2.1 "one group, one period" | Address in line 402 |
| AD-2.2 "finance" | A.4, line 343 |
| AD-3 "one per employee group" | Lines 144 and 411 |
| AD-3.1 attributes | A.2, line 296; line 167 |
| AD-3.1.1 "HR"; AD-3.1.2 "HR adds; all view" | A.4, lines 340 and 349; O-13 seen by all, line 282 |
| AD-4 queue, condition, order, count, "→ see AD-1.1.1" | C.4, line 443; line 396 |
| AD-5 "views" | Lines 191 and 396 |
| AD-5.1, AD-5.2, AD-5.5 "finance"; AD-5.3 and AD-5.4 unmarked | Line 191; line 526 |
| AD-5.4 "opens claims → see AD-1.1.1" | Line 396 |
| AD-6.1 "owner edits" | Line 272; B.1, line 372 |
| AD-6.2 and AD-6.2.1 "owner" | Lines 337, 338 and 386 |
| AD-6.3 "owner; each entry opens its record" | Lines 227 and 396 |
| AD-6.4 "every admin user" | Line 273 |
| AD-0 sign-in line "→ see S-6" | C.5, line 453 |

- **Tone:** every box is tone 4, as lines 14 and 396 say; no other tone is drawn.
- **Caption:** it says what the figure shows, names Deliverable C, C.1, names its sources and says Perqo is fictional. It sits under the figure at every width and in both themes.
- **Kind:** a sitemap fits a hierarchy of pages.

## (c) Renderer notes

None of these can be fixed in the figure's declaration.

- **Rows are not levels.** The root's seven children wrap into a row of three and a row of four. The second row (Approvals to Sign in) hangs off a long left-hand connector and can be misread as a level below Employees. Only fewer or narrower children would avoid this.
- **Phone width:**
  - The figure is wider than its frame, so it scrolls across four frames with the cue line "scroll sideways for the whole figure".
  - Every box is whole in at least one frame: the root and Budgets in frame 2; Policies, the Settings subtree and Sign in in frame 3.
  - The opening frame cuts the root at its right edge ("Perqo Ad…") because the root is centred over the full width.
- **Tablet and desktop:** the whole figure fits in one frame. The opening frames are clipped by the sticky section bar because the figure is taller than the viewport; the frames sheets show the whole figure.
- **Light and dark:** text stays inside its boxes, nothing overlaps, and borders and connectors are legible in both themes.

## (d) Verdict

Figure 6: **FIX**. The one should-fix is the Approvals note; there are no errors.

## Figure 7 re-check 3 (Opus 5.5 agent, 3 to 4 November 2026; the fourth check of figure 7, matrix: the navigation model; given the unit without its figures, the captions and the frames sheets, nothing of the earlier reports; verbatim hand-back; the harness refused its `report.md` write, so the hand-back is the one copy)

## Figure 7 (matrix) check: IA7, Deliverable C, C.2

**Verdict: figure 7 PASS.** There are three minor findings and no error or should-fix. The harness refused the write to `report.md`, so this reply is the only copy.

### (a) Findings

- **[minor] The Employees row says "card status", not Admin's label "Perqo card".** It is in the Contextual routes column. The unit sets Admin's name as "Perqo card" (line 525: "Admin's name for the card is "Perqo card", status only"). C.2 says "their Perqo card's status" (line 412).
  - Replacement cell: `employee to claims, budgets, Perqo card status; group to policy, employees, budgets`
- **[minor] Line 417 and the caption say the Roles column gives only "the roles that reach it".** The cells also carry what each role does there (edit, view, set, decide). Section 3.2 puts what a role does in the role matrix (Deliverable B) and what it reaches in the navigation model (Deliverable C) (lines 100–106). The values are correct and the caption credits them to Deliverable B; only the wording falls short.
  - Line 417 replacement: `The same model as a matrix, one row per area of the global navigation: its local routes, its work queue, its contextual routes, and the roles that reach it with what each does there, from the role matrix (the supplemental row, none, is left out). Its rows take tone 4, Perqo Admin.`
  - Caption opening replacement: `Navigation model: Perqo Admin's six areas with their local routes, work queues, contextual routes, and the roles that reach each with their marks from Deliverable B, F2;`
- **[minor] The caption does not say the supplemental route is left out; line 417 does.** This addition is optional. After "Rows tone 4, Perqo Admin." add: `The supplemental route, none, is left out (Deliverable C, C.2).`

### (b) Confirmed

**Column headings**
- LOCAL ROUTES, WORK QUEUE, CONTEXTUAL ROUTES and ROLES match line 417: "its local routes, its work queue, its contextual routes and the roles that reach it".

**Rows**
- Employees, Budgets, Policies, Approvals, Reports, Settings match line 410: "Global | Employees, Budgets, Policies, Approvals, Reports, Settings (IA1)".
- The rows follow IA1's order (line 144).

**Local routes** (line 411)

| Cell | Line 411 |
|---|---|
| "All employees, Employee groups, Not joined" | "inside Employees, All employees, Employee groups and Not joined" |
| "current period, next period" | "the current and the next period" |
| "one per employee group" | "the policies inside Policies, one per employee group" |
| "none: one list, grouped by policy" | "inside Approvals, none: it is one list, grouped by policy" |
| "the five reports" | "inside Reports, the five reports" |
| "Company, Admins, Activity log, Your profile" | "inside Settings, Company, Admins, Activity log and Your profile" |

**Work queue** (C.4, lines 441–445)
- "Not joined" matches line 444, where the queue sits at AD-1.4, under Employees.
- "No budget for next period" matches line 445, where it sits at "top of AD-2".
- "Approvals, count on the global route" matches line 443 ("AD-4; count on the global route") and line 410 ("Approvals shows the count of claims waiting for the viewer").
- Policies, Reports and Settings are blank because C.4 has only these three queues. The caption explains the blank cells.

**Contextual routes** (line 412; also line 148)

| Cell | Source |
|---|---|
| "employee to claims, budgets, card status" | "from an employee's record to the claims they made … to their budgets and their Perqo card's status" |
| "group to policy, employees, budgets" | "from an employee group to its policy, its employees and its budgets"; groups sit under Employees, AD-1.2 (line 400) |
| "budget to its employee group" | "from a budget to its employee group" |
| "policy to its employee group" | "from a policy to its employee group" |
| "claim to employee, policy, budget" | "from a claim to its employee, its policy and its budget"; in the Approvals row because Approvals opens the claim (line 396) |
| "report row to the records it sums" | "from a report row to the records it sums"; also line 190 |
| "audit entry to its record" | "from an audit entry to the record it changed"; in the Settings row because the Activity log is AD-6.3 |

**Roles** (lines 372–374, 386–388 and 190)

| Area | Cell | Source |
|---|---|---|
| Employees | "HR edit; finance view" | line 372 "edit: …"; line 373 "view" |
| Budgets | "finance set; HR view" | line 373 "set: set budgets for a group"; line 372 "view"; line 388 |
| Policies | "HR edit; finance view" | line 372 "edit: policy, covered items"; line 373 "view" |
| Approvals | "HR decide; not in finance's navigation" | line 372 "decide: …"; line 373 "(not in navigation)"; line 410 |
| Reports | "finance all five; HR two" | line 190: "Finance sees all five. HR sees two, Budget use and Claims by status" |
| Settings | "owner all; others Company read only and Your profile" | line 374 "manage: Company, Admins, Activity log, Your profile"; lines 372–373 "profile: Company read only, Your profile" |

**Caption**
- It says what the figure shows and names the section (Deliverable C, C.2).
- It gives the tone and what a blank cell means.
- Its sources all match the text:
  - Route types: Rosenfeld, Morville and Arango 2015, ch. 8, through IA2, section 1.4 (line 144).
  - Areas: IA1's surfaces map (line 27).
  - IA2, section 5.3's Admin column kept (lines 144 and 406).
  - Contextual routes: Deliverable A, A.3, following Prater 2015 (line 148).
  - Queues: C.4. Roles: Deliverable B.
- It ends "Perqo is fictional."

**Kind**
- Matrix is the right kind: the data is areas set against four columns, and the unit calls it a matrix (line 417).

**Notation**
- Every filled cell is tone 4, as stated on lines 14 and 417. No other tone is drawn.
- The blank cells are neutral and empty.
- Page-type tags, "-> verb" and [condition] do not apply to this kind. The one count is given in words that match line 443.

**Legibility**
- Desktop and tablet, dark and light: the figure fits in one frame. All text is inside its boxes, nothing overlaps, and the caption is under the figure.
- Phone, dark and light: the figure scrolls sideways (372 px) with the cue line "scroll sideways for the whole figure".
  - The row labels stay fixed while the columns scroll.
  - Frames 1–4 together show every cell in full.
  - The caption is under the figure.

### (c) Renderer notes

- At phone width the matrix is wider than its frame. The renderer scrolls it, keeps the row-label column fixed and fades cells at the frame's edge.
  - In the opening frame the WORK QUEUE column is cut at the right edge. Frames 2–4 show it and every other column in full, so this is acceptable.
- Column widths and how text wraps inside each cell come from the renderer, not from the figure's declaration.
- The neutral fill of the blank cells is the renderer's empty-cell style, not a tone. The caption's "A blank cell is…" sentence covers it.
- None of the three findings depends on layout. The longer "Perqo card status" label would only change how one cell wraps.

### (d) Verdict

**Figure 7: PASS.** None of the three minor findings blocks it.

## Figure 5 re-check 4 (Opus 5.5 agent, 4 November 2026; the fifth check of figure 5, matrix: the role-by-section matrix; given the unit without its figures, the captions and the frames sheets, nothing of the earlier reports; verbatim hand-back; the harness refused its `report.md` write, so the hand-back is the one copy)

The harness refused the write to F/report.md, so this reply is the only copy of the report.

# Figure 5 (matrix) check, IA7

Verdict: **FIX**. There are no errors, one should-fix in the `edit` legend entry and two minors.

## (a) Findings
- [should-fix] **Legend, mark `edit`: "-> create group" is not a call to action in A.4.**
  - A.4 has `employee group | -> create; -> invite employees` (line 339). The words "create group" appear only as B.1's "create groups" (line 372) and as the page name "Create group" (lines 169 and 400).
  - The caption says the legend names "the calls to action in Deliverable A, A.4", so this entry contradicts the caption.
  - The same entry also merges the Employees cell's actions with the Policies cell's actions, separated only by ";".
  - Replacement note: `group -> create, -> invite employees; employee -> invite, -> move to group, -> resend invitation, -> mark as left; policy -> edit, -> add covered items`
- [minor] **Legend, mark `manage`: "-> add, -> remove, -> change role" has no object.**
  - As drawn, "-> add" could be read as adding anything. A.4 lines 337 and 338 put these on admin user.
  - Replacement note: `-> edit company details; admin user -> add, -> remove, -> change role, -> make account owner; Activity log, Your profile`
- [minor] **Phone width: two legend lines are wider than 390 px.** The legend sits inside the matrix's sideways-scrolling frame. The `decide` line and the row holding `set`, `view` and `all` are too wide, so a reader has to scroll to finish one legend line. The declaration can fix this (see the renderer notes).

## (b) Confirmed
- **Columns** EMPLOYEES, BUDGETS, POLICIES, APPROVALS, REPORTS, SETTINGS: B.1's header (line 370) and IA1's six areas in order (line 144).
- **Rows** HR manager, Finance manager, Account owner: lines 372 to 374.
- **HR manager row** (edit, view, edit, decide, some, profile): line 372.
- **Finance manager row** (view, set, view, blank, all, profile): line 373.
  - The blank Approvals cell: line 368 ("A blank cell means the area is not in that role's navigation"), line 373 "(not in navigation)" and line 110.
- **Account owner row** (as role five times, then manage): line 374. "as role" is also in line 368.
- **Legend `edit`:**
  - "-> invite" and "-> move to group": line 341.
  - "-> resend invitation" and "-> mark as left": line 342.
  - "-> edit" and "-> add covered items": line 340.
  - "-> create group": see the should-fix above.
- **Legend `decide`:**
  - "-> approve" and "-> reject": line 344.
  - "-> approve selected": line 345.
  - "[never on their own claim]": lines 344, 345 and 372.
- **Legend `set`:** "-> set for a group" from line 343; "(Set budgets)" from line 400 (AD-2.2) and line 373.
- **Legend `view`, "read only":** lines 112 and 388.
- **Legend `all`, "all five reports":** line 373. The five reports are listed in line 191.
- **Legend `some`, "Budget use and Claims by status only":** line 526 ("HR sees Budget use and Claims by status only"), also lines 191 and 372.
- **Legend `profile`, "Company read only, and Your profile":** lines 372, 373 and 527.
- **Legend `manage`:**
  - "-> edit company details": line 336.
  - "-> add": line 337.
  - "-> remove", "-> change role" and "-> make account owner": line 338.
  - "Activity log, Your profile": line 374.
- **Legend `as role`, "what the holder's HR or finance role gives":** line 368 ("holds the HR manager or the finance manager role as well, so its row reads 'as role'"), also line 128.
- **Tone (d):**
  - Line 376: "Its rows take tone 4, Perqo Admin". Line 14 states the convention.
  - The figure draws only tone 4. The blank cell is a neutral empty fill, not a tone.
- **Notation (d):**
  - The "-> verb" form matches A.4 and line 98.
  - The condition is in square brackets, as the unit writes conditions at line 396 ("[condition]") and line 472 ("[over limit]").
  - The one count, "five", is from line 191.
- **Caption (b): complete.**
  - It says what the figure shows.
  - It names the section, Deliverable B, where B.1 draws the figure.
  - Every source it names is in the unit: IA1; IA4, A.1; sections 3.2 to 3.4 and 4.6; Ferraiolo 2001 (line 546); the NIST RBAC FAQ (line 550); the NIST glossary (line 551).
  - It says Perqo is fictional.
- **Kind (c):** roles by sections is a matrix, which fits the data.

## (c) Renderer notes
- **Desktop and tablet, dark and light:** one frame, and the whole figure fits. Text stays inside its boxes, nothing overlaps, and the caption is under the figure.
- **Phone, dark and light:**
  - Three frames, scrolled to 0, 164 and 213 of 213 px.
  - The cue line "scroll sideways for the whole figure" is present, the row labels stay pinned and the caption is under the figure.
  - Across the three frames, every cell and every legend word is clearly readable in at least one frame.
- **Phone, edge fade (renderer only):** the fade dims "[never on", "read on…" and the partly shown columns at the frame edge. Each dimmed part is clear in another frame.
- **Phone, opening frame (renderer only):** the sticky section bar clips the column headers and the top of the HR manager row. The frames sheet shows them in full.
- **Legend layout (the declaration could fix this):**
  - The renderer packs `set`, `view` and `all` onto one legend row by width, while every other mark gets its own row. This makes the phone overflow in the third finding.
  - The declaration could give each mark its own row and shorten the `decide` note to `-> approve, -> reject, -> approve selected [not own claim]`.
  - The legend would then fit 390 px, and only the matrix itself would scroll.
- **`manage` note:** its three lines sit tight under the `profile` legend row at every width, but nothing overlaps.

## (d) Verdict
Figure 5: **FIX**. Fix the `edit` legend entry so it uses A.4's calls to action and keeps each object's actions apart. The two minors are optional.

## Figure 6 re-check 5 (Opus 5.5 agent, 4 November 2026; the sixth check of figure 6, sitemap: Admin's pages; given the unit without its figures, the captions and the frames sheets, nothing of the earlier reports; verbatim hand-back; the harness refused its `report.md` write, so the hand-back is the one copy)

**Figure 6 (sitemap) passes.** There is one optional minor finding and nothing above it. The harness refused the write to F/report.md, so this reply is the only copy of the report.

## (a) Findings
- [minor] **Your profile (AD-6.4).** The note "every admin user" names a role where every role reaches the page. The caption and C.1 limit role notes to "roles where not all reach it" or a queue owner. The other pages every role reaches (Company AD-6.1, Budget use AD-5.3, Policies AD-3) carry no such note. Replace the note with `AD-6.4 · own profile`, which traces to A.1, O-02: "owner (all see their own profile)".

## (b) Confirmed
Each item in the drawing, with the unit line it traces to:
- **Root "Perqo Admin · the surface; AD-1 to AD-6 are global routes, by role"**, with no type tag.
  - C.1 (l.396): "the root names the surface and carries no type tag".
  - C.2 Global (l.410): "Employees, Budgets, Policies, Approvals, Reports, Settings (IA1); by role *new*".
- **Type tags SECTION, INDEX, STACK, DETAIL, FORM.** C.1 (l.396): "section … index … stack … detail … form".
- **Employees "AD-1 · by name; filter by group; find".**
  - l.165: "employees alphabetically by name, filtered by employee group".
  - C.3 (l.427): AD-1 row, with find by "name or work email".
- **Employee "AD-1.1 · one per employee; claims, budgets, Perqo card status (HR), History".**
  - l.148: "an employee's record leads to their claims (R-08), their budgets (R-05) and their Perqo card's status (R-11)".
  - A.1 O-09: seen by "HR".
  - l.167: the detail holds "its History".
- **Claim "AD-1.1.1 · one per claim; modal: Reject claim (HR)"**, drawn under Employee.
  - l.156: "a claim's page sits under its employee's record".
  - l.173: "Reject opens a modal … Reject claim moves it to Rejected".
  - T4 (l.468): actor "HR manager".
- **Employee groups "AD-1.2".** l.400; C.3 (l.428).
- **Employee group "AD-1.2.1 · its policy, employees, budgets".** l.148: "an employee group leads to its policy (R-03), its employees (R-04) and its budgets".
- **Create group "AD-1.2.2 · HR" and Invite employees "AD-1.3 · HR".** A.4 (l.339): "-> create; -> invite employees | HR manager | Employees (AD-1.2.2; AD-1.3)".
- **Not joined "AD-1.4 · queue [invited more than 14 days ago], owned by HR".** C.4 (l.444).
- **Budgets "AD-2 · by group and period; queue No budget for next period [no budgets set for the next period], owned by finance".**
  - C.3 (l.431): "employee groups by period".
  - C.4 (l.445): "no budgets set for the next period | finance manager | top of AD-2".
- **Budget "AD-2.1 · one group, one period".** l.402: "/budgets/{employee group ID}/{period}".
- **Set budgets "AD-2.2 · finance".** A.4 (l.343).
- **Policies "AD-3 · one per employee group".** l.144; C.2 (l.411).
- **Policy "AD-3.1 · open categories, auto-approve limit, covered items, History".** A.2 O-04 (l.296); A.1 O-04: "History records each change".
- **Edit policy "AD-3.1.1 · HR".** A.4 (l.340).
- **Covered items "AD-3.1.2 · HR adds; all view".** A.4 (l.340, l.349); A.1 O-13: seen by "all".
- **Approvals "AD-4 · HR only; queue [over the policy's auto-approve limit]; by policy, oldest first; count on the global route; opens claims → see AD-1.1.1".**
  - l.110: Approvals is not in the finance manager's global navigation.
  - C.4 (l.443).
  - l.396: "Approvals and Claims by status open it there".
- **Reports "AD-5 · views".** l.191: "Reports holds five views"; l.396: "'views' for the reports".
- **Report role notes.** l.191: "Finance sees all five. HR sees two, Budget use and Claims by status".
  - AD-5.1, AD-5.2 and AD-5.5 are marked "finance".
  - AD-5.3 has no role note, which is correct.
  - AD-5.4 reads "opens claims → see AD-1.1.1" (l.396).
- **Settings "AD-6".** l.400.
- **Company "AD-6.1 · owner edits".** l.527: "Every admin user sees Company (AD-6.1) read only; only the account owner edits it".
- **Admins "AD-6.2 · owner" and Activity log "AD-6.3 · owner; each entry opens its record".**
  - l.527: "only the account owner reaches Admins and the Activity log".
  - l.396: "each entry of the Activity log opens its record".
- **Add admin user "AD-6.2.1 · owner".** A.4 (l.337).
- **Your profile "AD-6.4 · every admin user".** B.1 (l.372 to 374); A.1 O-02. See the finding above.
- **Sign in "AD-0 · line "Looking for your benefits? Get the Perqo app" → see S-6"**, drawn last.
  - C.5 (l.453).
  - l.396: "Sign in comes last".
- **Area order.** Employees, Budgets, Policies, Approvals, Reports, Settings, as l.396 and l.144 give it ("keep IA1's order").
- **Completeness.** All 31 identifiers in l.400 are drawn, once each, and nothing else is drawn.
- **(d) Tone.** Every box is tone 4. l.14: "Admin's boxes take tone 4, Perqo Admin". l.396: "Every box is tone 4, Perqo Admin". No other tone appears.
- **(d) Notation.**
  - Every queue has its [condition] and its owner, as l.396 requires.
  - "→ see" is used for AD-1.1.1 and S-6.
  - The sitemap needs no "-> verb", since calls to action belong to A.4.
- **(b) Caption.**
  - It says what the figure shows: pages at F2, IDs AD-0 to AD-6, IA2's type tags.
  - It names the section (Deliverable C, C.1).
  - It names the sources: IA1's surfaces map, IA2 §5.3, IA4 §4.3, and §§3.2 to 3.4, 4.1 to 4.6 and 5.3, A.1, A.4 and C.3 to C.5.
  - It names tone 4 and says "Perqo is fictional."
  - It sits under the figure at every width and in both themes.
- **(c) Kind.** A hierarchy of pages is a sitemap, so the kind fits.

## (c) Renderer notes
- **Rows are not levels.** At every width the renderer wraps the root's seven children into two rows by width: Employees, Budgets and Policies, then Approvals, Reports, Settings and Sign in. The second row hangs from the root's left connector, so all seven are siblings. The declaration cannot change this short of fewer children, and nothing needs to change.
- **Desktop and tablet, light and dark.** The whole figure fits in one frame. All text stays inside its boxes, nothing overlaps, and the caption is under the figure.
- **Phone (390 px).** The figure is wider than its frame. It scrolls sideways across four frames (15, 179, 343 and 372 of 372 px), with the cue line "scroll sideways for the whole figure" above the caption. Every box appears whole in at least one frame, in both themes. The fade on boxes cut at a frame's edge is the scroll cue, not a clipping fault.
- **Phone opening frame.** The figure opens at 15 px, so the root ("Perqo Ad…") and the Budgets column are cut at the right edge until the reader scrolls. This is how the renderer places the figure, and no change to labels or order in the declaration would fix it.
- **Opening frames at every width.** The sticky section bar covers part of the tree: the Claim and Employee groups boxes, and on desktop and tablet the top of the Policies children. The frames sheets show these parts whole. This comes from the renderer only.

## (d) Verdict
Figure 6: **PASS**. The one minor finding can be taken or left.

## Figure 7 re-check 4 (Opus 5.5 agent, 4 November 2026; the fifth check of figure 7, matrix: the navigation model; given the unit without its figures, the captions and the frames sheets, nothing of the earlier reports; verbatim hand-back; the harness refused its `report.md` write, so the hand-back is the one copy)

Figure 7 (matrix, IA7 the backoffice, Deliverable C, C.2) checked. The verdict is FIX, for one should-fix. There are no errors. The harness refused the write of F/report.md, so this reply is the only copy of the report.

**(a) Findings**
- [should-fix] Roles column, Settings row. The cell reads `owner all; others Company read only and Your profile`. Nothing in the unit's text says "owner all". It is also not the owner's mark in Deliverable B, even though the caption says the roles come "with their marks from Deliverable B". B.1, line 374, gives the owner `manage: Company, Admins, Activity log, Your profile`, and lines 372–373 give the other roles `profile: Company read only, Your profile`. Replace the cell with `owner manage; others profile: Company read only, Your profile` (about the same length; three lines in the current cell).
- [minor] Roles column, Reports row. The cell reads `finance all five; HR two`. It traces to section 4.6, line 191 ("Finance sees all five. HR sees two"). But HR's Deliverable B mark is `some: Budget use, Claims by status` (line 372). This is the only other cell where the figure uses a count and not B's mark. To match the caption, use `finance all five; HR some: Budget use, Claims by status`. If that is too long, use `finance all five; HR some (two)`.
- [minor] Unit text, line 417. The text says what each column holds, but it never says what a blank cell means; only the caption does. After "(the supplemental row, none, is left out)." add `An area with no work queue has a blank cell (C.4).`

**(b) Confirmed**
- **Column heads.** LOCAL ROUTES, WORK QUEUE, CONTEXTUAL ROUTES, ROLES come from line 417: "its local routes, its work queue, its contextual routes, and the roles that reach it with what each does there".
- **Row labels.** Employees, Budgets, Policies, Approvals, Reports, Settings, in IA1's order, come from line 410 (C.2 Global) and line 146.
- **Local routes** (all line 411, C.2 Local):
  - "All employees, Employee groups, Not joined" ← "inside Employees, All employees (the Employees list, AD-1), Employee groups and Not joined"
  - "current period, next period" ← "inside Budgets, the current and the next period"
  - "one per employee group" ← "the policies inside Policies, one per employee group (IA2)"
  - "none: one list, grouped by policy" ← "inside Approvals, none: it is one list, grouped by policy (IA1)"
  - "the five reports" ← "inside Reports, the five reports"
  - "Company, Admins, Activity log, Your profile" ← "inside Settings, Company, Admins, Activity log and Your profile"
- **Work queue** (C.4 table):
  - "Not joined" ← line 444
  - "No budget for next period" ← line 445
  - "Approvals, count on the global route" ← line 443 "AD-4; count on the global route"; also line 410
  - Policies, Reports and Settings are blank, which is correct: C.4 has only three queues.
- **Contextual routes** (line 412; also line 148):
  - "employee to claims, budgets, Perqo card status; group to policy, employees, budgets" ← "from an employee's record to the claims they made … their budgets and their Perqo card's status … from an employee group to its policy, its employees and its budgets"
  - "budget to its employee group" ← "from a budget to its employee group"
  - "policy to its employee group" ← "from a policy to its employee group"
  - "claim to employee, policy, budget" ← "from a claim to its employee, its policy and its budget"
  - "report row to the records it sums" ← verbatim; also line 191
  - "audit entry to its record" ← "from an audit entry to the record it changed"
  - All eight routes in C.2 are drawn, none twice. Each is placed in the area that holds its source page (Employee groups AD-1.2 under Employees, Activity log AD-6.3 under Settings).
- **Roles** (B.1, lines 372–374):
  - Employees "HR edit; finance view" ← `edit: …` / `view`
  - Budgets "finance set; HR view" ← `set: set budgets for a group` / `view`
  - Policies "HR edit; finance view" ← `edit: policy, covered items` / `view`
  - Approvals "HR decide; not in finance's navigation" ← `decide: …` / `(not in navigation)`; also line 410 ("a finance manager's navigation has no Approvals") and line 110
  - Reports "finance all five; HR two" ← line 191 and line 373 "all five reports" (see the minor finding)
  - Settings "others Company read only and Your profile" ← lines 372–373. "owner all" is untraced (see the should-fix).
- **Caption (check b).** It says what the figure shows and names its section (Deliverable C, C.2, line 404). Each source it names is in the text:
  - Rosenfeld, Morville and Arango 2015, ch. 8, through IA2, section 1.4 (line 144)
  - IA2, section 5.3's Admin column kept (lines 144 and 406)
  - IA1's areas (line 410)
  - Deliverable A, A.3 relationships, following Prater 2015 (line 148)
  - C.4 for the queues, Deliverable B for the roles
  - Supplemental route left out (line 417)
  - Perqo is fictional: stated.
  - The caption passes, except that its claim "with their marks from Deliverable B" is not met by two cells.
- **Kind (check c).** A matrix fits: the items are the areas, and the columns are route types, queue and roles.
- **Notation (check d).**
  - Tone: one tone only, tone 4 Perqo Admin, which the text names at line 14 and line 417.
  - Blank cells use a neutral fill, not a tone.
  - No "-> verb", conditions in brackets or multiplicities are needed or drawn. The marks are B.1's, and the counts ("five", "two") are in the text.
- **Legibility (check e).**
  - Desktop and tablet, dark and light: the figure fits in one frame. Text stays inside the boxes, nothing overlaps, and the caption is underneath.
  - Phone, dark and light: the figure scrolls sideways in its frame (0 to 372 px, four frames), with the cue line "scroll sideways for the whole figure" and the caption below. The row-label column stays fixed.
  - On phone, every cell can be read in some frame, and frame 4 shows the ROLES column whole. The section bar does not clip the opening frame.

**(c) Renderer notes**
- **Phone, Contextual column.** The fixed label column on the left and the fade at the right edge partly cover the cells at each frame's edges. As a result, CONTEXTUAL ROUTES is never whole in a single phone frame; you read it across frames 2 and 3, which overlap. The renderer's 390 px layout causes this. A shorter Employees contextual cell in the declaration would ease it, for example `employee to claims, budgets, card status; group to policy, employees, budgets`. Nothing is lost as it stands, so this is not required.
- **Blank cells.** Their grey or near-black fill is the renderer's empty-cell style, not a tone. The caption gives their meaning.
- **Row heights.** These come from the renderer wrapping text at each column's width; they say nothing about the data.

**(d) Verdict**
Figure 7: **FIX**, for the Settings roles cell. Replace it with `owner manage; others profile: Company read only, Your profile`. The two minor items are optional.

Files read: everything in /tmp/claude-0/-home-claude/523bc694-bc8b-5dd5-bdd8-2b916401be73/scratchpad/f7r4/ (unit-without-figures.md, captions.md and all 12 sheets). I also wrote three working crops in that folder (crop-phone-f2-dark.png, crop-phone-f3-dark.png, crop-phone-f4-dark.png).

## Figure 5 re-check 5 (Opus 5.5 agent, 4 November 2026; the sixth check of figure 5, matrix: the role-by-section matrix; given the unit without its figures, the captions and the frames sheets, nothing of the earlier reports; verbatim hand-back; the harness refused its `report.md` write, so the hand-back is the one copy)

# Fresh figure check · IA7 · figure 5 (matrix)

The harness refused the write to F/report.md, so this reply is the only copy.

## (a) Findings

- **[minor]** The legend does not always do what the caption says it does.
  - The caption and Deliverable B's face (line 364) say the legend names, "for each mark, the calls to action in Deliverable A, A.4 or the pages and reports it opens".
  - Two marks name neither:
    - `view` ("read only")
    - `as role` ("what the holder's HR or finance role gives")
  - Both legend texts trace to the unit, so this is not an error.
  - Fix, either:
    - Change the caption and line 364's face to: `with a legend saying, for each mark, the calls to action in Deliverable A, A.4 or the pages and reports it opens, or what it stands for`
    - Or give `view` B.2's fuller wording: `read only: no edit actions`.

No errors. No should-fix.

## (b) Confirmed

**Columns** (shown in capitals by the renderer): Employees, Budgets, Policies, Approvals, Reports, Settings.
- B.1 table header, line 370.
- "Roles as rows, Admin's six areas as columns, IA1's order", line 368.
- The six areas named, line 144.

**Rows:** HR manager, Finance manager, Account owner. B.1, lines 372 to 374.

**Cells** (B.1, lines 372 to 374):
- **HR manager:** edit / view / edit / decide / some / profile.
  - Line 372: "edit: create groups, invite, resend, move, mark as left | view | edit: policy, covered items | decide: approve, reject, approve selected, never on their own claim | some: Budget use, Claims by status | profile: Company read only, Your profile".
- **Finance manager:** view / set / view / blank / all / profile.
  - Line 373: "view | set: set budgets for a group | view | (not in navigation) | all five reports | profile: …".
- **Account owner:** "as role" in five columns, then manage.
  - Line 374: "as role … | manage: Company, Admins, Activity log, Your profile".
- **The blank cell:**
  - Line 368: "A blank cell means the area is not in that role's navigation".
  - Line 110: "Approvals is not in the finance manager's global navigation".

**Legend:**
- **edit:** "employee group -> create, -> invite employees; employee -> invite, -> move to group, -> resend invitation, -> mark as left; policy -> edit, -> add covered items". A.4, lines 339 to 342.
- **decide:** "-> approve, -> reject, -> approve selected [never on their own claim]".
  - A.4, lines 344 to 345: "HR manager, never on their own claim".
  - The square brackets for a condition follow the unit's own convention: "'queue' with the queue's [condition]", line 396.
- **set:** "-> set for a group (Set budgets)".
  - A.4, line 343: "allocation | -> set for a group | finance manager | Budgets (AD-2.2)".
  - Line 400: "AD-2.2 Set budgets".
- **view:** "read only".
  - B.2, line 388: "read only: no edit actions | Policies and Employees for a finance manager; Budgets for an HR manager".
  - Line 112: "What a role may see but not change is shown read only".
- **all:** "all five reports".
  - Line 373.
  - Line 191: "Finance sees all five".
- **some:** "Budget use and Claims by status only".
  - Line 372.
  - Line 191: "HR sees two, Budget use and Claims by status".
- **profile:** "Company read only, and Your profile". Lines 372 to 373.
- **manage:** "client -> edit company details; admin user -> add, -> remove, -> change role, -> make account owner; Activity log, Your profile".
  - A.4, lines 336 to 338.
  - Line 374.
  - Line 126: "edits the company details, adds and removes admin users, changes an admin user's role, reads the Activity log, and hands the ownership … (-> make account owner)".
- **as role:** "what the holder's HR or finance role gives".
  - Line 368: "The account owner holds the HR manager or the finance manager role as well, so its row reads 'as role' except in Settings".
  - Line 128.

**Caption (check b).** It says what the figure shows, names where it sits in the unit and its sources, and says Perqo is fictional.
- **What it shows:** "role-by-section matrix … each of Admin's six areas, F2, one mark per cell". Lines 136 and 364.
- **Where it sits in the unit:** Deliverable B, and sections 3.2 to 3.4 and 4.6.
  - Hidden route: line 110.
  - Separation of duty on own claims: line 120.
  - Account owner: line 126.
  - The two reports HR sees: line 191.
- **Sources:**
  - IA1's surfaces map: line 27.
  - IA1, section 5: line 12.
  - IA4, A.1 role attribute: line 294.
  - Ferraiolo and others, *ACM TISSEC* 4(3), 2001, and NIST's RBAC FAQ: line 96.
  - NIST glossary for least privilege and separation of duty: line 118.
- **"Rows tone 4, Perqo Admin":** line 376.
- **"A blank cell is an area not in that role's navigation":** line 368.
- **"Perqo is fictional":** present.

**Kind (check c).** Roles by sections is items by sections, so matrix is the right kind. The unit's own catalogue row, line 136, also says "matrix".

**Notation (check d):**
- The only tone drawn is tone 4: blue-grey cells in light, dark slate in dark. Tone 4 is named at lines 14 and 376.
- The blank cell is a neutral empty fill, not a tone, and line 368 states it.
- Calls to action use "-> verb", and the condition sits in square brackets.
- Page-type tags and counts do not apply to this kind.

## (c) Renderer notes

**Desktop and tablet, light and dark:**
- The whole figure fits in one frame (frame 1 of 1).
- Text sits inside its boxes, nothing overlaps, and the caption is under the figure.
- The desktop opening frame is clipped by the sticky section bar ("Deliverable · The Perqo Admin IA"), which half covers the column headers. The frames sheet shows them whole. This is renderer layout only.

**Phone (390 px), light and dark:**
- The figure is 213 px wider than its frame. It scrolls sideways in its frame, and the cue line "scroll sideways for the whole figure" is present.
- Row labels stay pinned while the cells scroll.
- The opening frame is clipped by the sticky section bar: the column headers and the HR manager row are hidden. Frames 1 to 3 show them.
- Every cell and every legend word can be read in full in at least one frame:
  - Settings, profile and manage in frame 3.
  - "[never on their own claim]" across frames 2 and 3.
  - "read only" in frame 3.

**Phone, renderer quirk:**
- The fade at the edge of the pinned row-label column runs the full height of the figure, through the legend as well as the matrix.
- In frames 2 and 3 it dims legend text that passes under it ("[never", "read only", "their") in the middle of the frame, not at the frame's edge.
- Each dimmed word is clear in another frame, so nothing is lost.
- The declaration could only reduce this by shortening the widest legend lines: the `decide` line, and the `set` / `view` / `all` entries that the renderer packs onto one line. That is not needed, because the six columns force the sideways scroll anyway.

**Dark theme:** the blank cell (near-black fill) can be told apart from the filled cells and from the background. All text contrast is adequate.

## (d) Verdict

**Figure 5 PASS.** One minor caption note, optional; nothing blocks filing.

## Figure 6 re-check 6 (Opus 5.5 agent, 4 November 2026; the seventh check of figure 6, sitemap: Admin's pages; given the unit without its figures, the captions and the frames sheets, nothing of the earlier reports; verbatim hand-back; the harness refused its `report.md` write, so the hand-back is the one copy)

Figure 6 (sitemap) of IA7 passes. I found no error and no should-fix. Every label, ID and note in the drawing traces to the unit's text. There is one minor fix to the unit's own text (A.4) and one optional minor change to the figure. The harness refused the write to F/report.md, so this reply is the only copy.

## (a) Findings
- [minor] **Unit text, Deliverable A, A.4, the row "transaction, type claim | -> view *new* in Admin" (line 346).** It gives the employee's record the claim page's ID, AD-1.1.1. In the figure and in line 400, AD-1.1 is the Employee page and AD-1.1.1 is the Claim page. Replace `employee's record (AD-1.1.1); Reports, Claims by status (AD-5.4)` with `the claim, under the employee's record (AD-1.1.1); Reports, Claims by status (AD-5.4)`.
- [minor, optional] **AD-1 Employees note.** It names one filter, "filter by group". C.3 (line 427) gives two filters: "employee group; status". The note is not wrong. If the figure should match C.3: `AD-1 · by name; filter by group, status; find`.

## (b) Confirmed (drawing to unit text, by line)

**Root and order**
- **Root "Perqo Admin", no type tag:** line 396, "the root names the surface and carries no type tag, because the global navigation is not a page".
- **Root note "the surface; AD-1 to AD-6 are global routes, by role":** line 410, "Global | Employees, … Settings (IA1); by role *new*"; line 146; IDs from line 400.
- **Order Employees, Budgets, Policies, Approvals, Reports, Settings, then Sign in:** line 396, "The six areas keep IA1's order, and Sign in comes last".
- **Completeness:** all 30 IDs in line 400 are drawn, each under its parent, and nothing extra is drawn.

**Employees**
- **INDEX Employees, "AD-1 · by name; filter by group; find":** line 427; line 165.
- **STACK Employee, "AD-1.1 · one per employee; claims, budgets, Perqo card status (HR), History":** line 148 ("leads to their claims (R-08), their budgets (R-05) and their Perqo card's status (R-11)"); line 280 (card seen by "HR *new*"); line 348; History at lines 167 and 227.
- **STACK Claim, "AD-1.1.1 · one per claim; modal: Reject claim (HR)":**
  - line 173, "Reject opens a modal … Reject claim moves it to Rejected";
  - line 344, the HR manager;
  - lines 156 and 396, the claim page sits under the employee.
- **INDEX Employee groups, "AD-1.2":** lines 400 and 428.
- **STACK Employee group, "AD-1.2.1 · its policy, employees, budgets":** line 148.
- **FORM Create group, "AD-1.2.2 · HR":** line 339.
- **FORM Invite employees, "AD-1.3 · HR":** lines 339, 341 and 447.
- **INDEX Not joined, "AD-1.4 · queue [invited more than 14 days ago], owned by HR":** line 444.

**Budgets**
- **INDEX Budgets, "AD-2 · by group and period; queue No budget for next period [no budgets set for the next period], owned by finance":** lines 431 and 445 ("top of AD-2").
- **STACK Budget, "AD-2.1 · one group, one period":** line 402, "/budgets/{employee group ID}/{period}"; line 411.
- **FORM Set budgets, "AD-2.2 · finance":** line 343.

**Policies**
- **INDEX Policies, "AD-3 · one per employee group":** lines 411 and 432.
- **STACK Policy, "AD-3.1 · open categories, auto-approve limit, covered items, History":** line 296 (the O-04 attributes); line 275.
- **FORM Edit policy, "AD-3.1.1 · HR":** line 340.
- **INDEX Covered items, "AD-3.1.2 · HR adds; all view":** line 340; line 282 (seen by "all"); line 349.

**Approvals**
- **INDEX Approvals, "AD-4 · HR only; queue [over the policy's auto-approve limit]; by policy, oldest first; count on the global route; opens claims → see AD-1.1.1":**
  - line 443 gives the condition, the owner, "AD-4; count on the global route" and "grouped by policy, oldest first";
  - lines 110 and 373 support "HR only";
  - line 396, "Approvals and Claims by status open it there".

**Reports**
- **SECTION Reports, "AD-5 · views":** lines 191 and 146.
- **The finance tags on AD-5.1 Spend by category, AD-5.2 Spend by employee group and AD-5.5 Card payments, and AD-5.3 Budget use untagged:** line 191 ("Finance sees all five. HR sees two, Budget use and Claims by status"); line 386.
- **INDEX Claims by status, "AD-5.4 · opens claims → see AD-1.1.1":** line 396.

**Settings**
- **SECTION Settings, "AD-6":** line 400.
- **DETAIL Company, "AD-6.1 · owner edits":** lines 527 and 336.
- **INDEX Admins, "AD-6.2 · owner":** lines 386 and 338.
- **FORM Add admin user, "AD-6.2.1 · owner":** line 337.
- **INDEX Activity log, "AD-6.3 · owner; each entry opens its record":** lines 396 and 350.
- **DETAIL Your profile, "AD-6.4 · own profile":** line 273, "all see their own profile"; lines 372 and 411.

**Sign in**
- **FORM Sign in, "AD-0 · line "Looking for your benefits? Get the Perqo app" → see S-6":** line 453.

**Notation and tone**
- **Type tags SECTION, INDEX, STACK, DETAIL, FORM:** all defined at line 396.
- **Note conventions "queue" with [condition], "views", "→ see":** line 396.
- **Tone:** one tone throughout, tone 4, named in lines 14 and 396.

**Caption**
- It says what the figure shows.
- It names the section, Deliverable C, C.1.
- It names the sources, matching lines 144, 191 and 400 to 453.
- It ends "Perqo is fictional."
- It sits under the figure at every width and theme.

**Kind**
- Sitemap, for a hierarchy of pages. It fits.

## (c) Renderer notes
- **Rows are not levels.** The renderer wraps the root's seven children into two rows by width: Employees, Budgets and Policies, then Approvals, Reports, Settings and Sign in, placed below the Employees subtree. The trunk line still reaches every child, so all seven read as children of the root. The declaration cannot change this without breaking IA1's order, which the text fixes.
- **The sticky bars clip the opening frame** at every width and theme. On desktop and tablet the frame sheets show the whole figure in one frame.
- **On phone the figure scrolls sideways** across 4 frames, with the cue line "scroll sideways for the whole figure" in both themes.
  - The opening frame shows only part of the root, because the root is centred over the three-column first row.
  - Every box is whole in at least one frame.
- **On phone, frames 3 and 4 have a tall blank band** above the second row. It is caused by the height of the Employees subtree and is layout only. No shorter label would fix it while IA1's order holds.
- **Legibility:** at all three widths and in both themes, all text is inside its box and nothing overlaps.

## (d) Verdict
Figure 6 PASS.

## Figure 7 re-check 5 (Opus 5.5 agent, 4 November 2026; the sixth check of figure 7, matrix: the navigation model; given the unit without its figures, the captions and the frames sheets, nothing of the earlier reports; verbatim hand-back; the harness refused its `report.md` write, so the hand-back is the one copy)

I checked figure 7 (the navigation matrix in IA7, Deliverable C, C.2) against the unit text and all 12 sheets: phone, tablet and desktop, dark and light. It passes. There are no errors and no should-fix items, only two minor notes. The harness refused my write to F/report.md, so this reply is the only copy of the report.

## (a) Findings

- [minor] Roles column, Settings row: the cell says `owner manage`, but the unit's role name is "account owner" (sections 3.4 and B.1). In this unit "owner" also means a queue's owner (the C.4 "Owner" column) and the deliverable's owner ("owner: the IA designer"), so the short form is ambiguous. Replace the cell with `account owner manage; others profile: Company read only, Your profile`. The cell gets one word longer and still wraps inside its box at tablet and desktop width.
- [minor] Contextual routes, Approvals row: `claim to employee, policy, budget` sits in the Approvals row. But C.1 places a claim's page under its employee's record, and every other row puts a route under its object's home area. The placement is defensible, because the claim opens beside the Approvals list (section 4.3), but the unit never states the rule. A note on the unit's own text: in C.2, after "An area with no work queue has a blank cell (C.4).", add `A contextual route sits in the row of the area where it is followed most: a claim's routes are in Approvals, where HR opens claims, although the claim's page sits under Employees (C.1).`

## (b) Confirmed (each label traced to its line)

**Headings**
- Column heads LOCAL ROUTES / WORK QUEUE / CONTEXTUAL ROUTES / ROLES: C.2, "its local routes, its work queue, its contextual routes, and the roles that reach it with what each does there".
- Rows Employees, Budgets, Policies, Approvals, Reports, Settings, in IA1's order: C.2 Global row, "Employees, Budgets, Policies, Approvals, Reports, Settings (IA1)".

**Local routes**, from C.2's Local row: "inside Employees, All employees (the Employees list, AD-1), Employee groups and Not joined; inside Budgets, the current and the next period; inside Reports, the five reports; inside Settings, Company, Admins, Activity log and Your profile; inside Approvals, none: it is one list, grouped by policy (IA1)", and "the policies inside Policies, one per employee group (IA2)".
- `All employees, Employee groups, Not joined`
- `current period, next period`
- `one per employee group`
- `none: one list, grouped by policy`
- `the five reports`
- `Company, Admins, Activity log, Your profile`

**Work queue**, from the C.4 table:
- `Not joined`: "Not joined | employee, Invited | … | AD-1.4"
- `No budget for next period`: "No budget for next period | employee group | … | top of AD-2"
- `Approvals, count on the global route`: "Approvals | claim, Submitted | … | AD-4; count on the global route"
- The blank cells for Policies, Reports and Settings are the areas with no row in C.4. C.2 says: "An area with no work queue has a blank cell (C.4)."

**Contextual routes**, from C.2's Contextual row: "from an employee's record to the claims they made (IA2); new: from an employee's record to their budgets and their Perqo card's status; from a claim to its employee, its policy and its budget; from an employee group to its policy, its employees and its budgets; from a budget to its employee group; from a policy to its employee group; from a report row to the records it sums; from an audit entry to the record it changed".
- `employee to claims, budgets, Perqo card status; group to policy, employees, budgets`
- `budget to its employee group`
- `policy to its employee group`
- `claim to employee, policy, budget`
- `report row to the records it sums`
- `audit entry to its record`
- Every route listed in C.2 is drawn, and nothing beyond them.

**Roles**, from the B.1 table and section 4.6:
- Employees, `HR edit; finance view`: HR "edit: …", finance "view".
- Budgets, `finance set; HR view`: finance "set: set budgets for a group", HR "view".
- Policies, `HR edit; finance view`: HR "edit: policy, covered items", finance "view".
- Approvals, `HR decide; not in finance's navigation`: HR "decide: …", finance "(not in navigation)". C.2 also says "a finance manager's navigation has no Approvals".
- Reports, `finance all five; HR some (two)`: finance "all five reports", HR "some: Budget use, Claims by status". Section 4.6: "Finance sees all five. HR sees two".
- Settings, `owner manage; others profile: Company read only, Your profile`: account owner "manage: Company, Admins, Activity log, Your profile"; HR and finance "profile: Company read only, Your profile".

**Tone.** The rows are tone 4. C.2: "Its rows take tone 4, Perqo Admin". Line 14: "Admin's boxes take tone 4, Perqo Admin". No other tone is drawn.

**Caption (check b).** It says what the figure shows, gives F2, and names the decision and the section (Deliverable C, C.2). It ends "Perqo is fictional." Its sources all trace to the text:
- Rosenfeld, Morville and Arango 2015, ch. 8, via IA2, section 1.4: section 4.1.
- IA1's surfaces map: the register line 27 and section 4.1.
- "IA2, section 5.3's Admin column kept": C.2, "IA2's entries are kept".
- Deliverable A, A.3, following Prater 2015: section 4.1.
- C.4 and Deliverable B: as traced above.

**Kind (check c).** Areas by route types and roles is items by sections, so matrix is the right kind.

**Notation (check d).** A matrix carries no page-type tags, `-> verb` or [conditions]. The one count is given in a cell ("count on the global route"), as C.4 states it.

## (c) Renderer notes

- **Desktop and tablet, dark and light:** the whole figure fits in one frame. All text sits inside its boxes, nothing overlaps, and the caption is under the figure.
- **Phone (390 px), dark and light:** the figure is wider than its frame and scrolls sideways inside it. The cue "scroll sideways for the whole figure" is present in every frame. The four sampled frames (offsets 0, 164, 328 and 372 px) together show every cell in full.
- **Phone, partial columns:** this note rests only on how the renderer sizes columns and on the sampled offsets.
  - No single phone frame shows the Contextual routes column whole: it is cut at the right in frame 2 and at the left in frame 3.
  - The Approvals work-queue cell fades at the right edge of frame 1 ("count o") and is complete across frames 1 and 2.
  - A reader scrolling by hand can stop anywhere, and shorter labels could not fit five columns into 390 px. No change to the declaration is needed or could fully fix it.
- **Phone, opening frame:** the sticky section bar ("Deliverable · The Perqo Admin IA") overlaps only the figure's top padding. The column heads are visible just below it, and nothing is clipped.
- **Blank cells:** the renderer draws them as a neutral empty fill (light grey in light theme, near-background in dark), not as a tone. They are clearly different from the tone-4 cells in both themes, and the caption explains them.

## (d) Verdict

Figure 7: **PASS**. The two minor notes are optional.
