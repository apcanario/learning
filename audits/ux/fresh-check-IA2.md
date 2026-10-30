---
audit: fresh check
unit: IA2 · The shapes IA takes: the artefact catalogue and the course notation
course: ux · IA · Information Architecture
model: Opus 5.5 (search on; a Fable 5.1 fresh check is owed, row P49)
date: 2026-10-30
chat: own Opus 5.5 agent context, not shown the writing (P31), in session https://claude.ai/code/session_01KMmgR2TPyBo2wmSxXi3WQy
verdict: fix · 3 errors, 10 should-fix, 17 minor
---

# Fresh check · IA2 · The shapes IA takes: the artefact catalogue and the course notation

The checker's final report, verbatim. Checked with Opus 5.5, not Fable 5.1: Pedro deferred Fable checks on 29 Oct 2026, and the Fable 5.1 fresh check that replaces this one is owed (backlog row P49).

# Fresh check · IA2 · The shapes IA takes: the artefact catalogue and the course notation

Checker: Opus 5.5, isolated context (P31), 30 Oct 2026, live search. A Fable 5.1 fresh check is still owed (row P49). Inputs: the files in this folder only. One URL could not be opened: https://linkinghub.elsevier.com/retrieve/pii/0167642387900359 (Harel 1987 at the publisher; the permission request timed out). Harel was checked against a copy of the paper at the University of Edinburgh instead. jjg.net blocks robots for the visual vocabulary index page; the Quick Reference PDF was read.

## (1) Coverage

- Catalogue: content inventory and audit: covered (1.1).
- Sitemap, structural rather than page-by-page: covered (1.3).
- Object map and object-relationship map: covered (1.5).
- Taxonomy and controlled vocabulary: covered (1.2).
- User flow, task flow, wireflow: covered (1.6). The split between user flow and task flow is labelled as a course convention.
- Decision tree: covered (1.7). Its definition contradicts the unit's own example (should-fix below).
- State diagram: covered (1.8).
- Navigation model with global, local, contextual and supplemental routes: covered (1.4, and the table in 5.3).
- Service blueprint: covered (1.9).
- Cross-surface interaction map: covered (1.10).
- For each artefact, its readers, the fidelity it needs at each stage and what it must not be mistaken for: covered. Every entry has all three, and the F1/F2/F3 scale is labelled as a course convention.
- Published notations, Garrett's visual vocabulary and Brown's site map and flowchart chapters, and what each standardises: covered (2.1, 2.2). The brief dates Garrett's vocabulary 2002; the unit gives "first released October 2000, revised since", which Brown 2003 supports, and its unsure list notes that the date could not be confirmed. That is acceptable.
- How to read someone else's artefact, and the five faults: covered (3).
- How to edit one without breaking what others rely on: covered (4).
- The single course notation, derived from Garrett and Brown and reduced to the figure kinds: covered (5.1, 5.2).
- Figures, one per artefact family plus the legend: thin for one family. Inventories and vocabularies is shown as tables, not a viz figure; the unit says so and sets table rules. The unit already has eight figures, the brief's maximum, so no finding is raised. The legend itself is incomplete (should-fix, section 7).
- Deliverable 1, the course notation sheet: covered, with four companion edits below.
- Deliverable 2, the artefact decision table: thin. The "unit of this course that builds it" column is a placeholder in every row (should-fix).

## (2) Accuracy (starting from the writer's unsure list)

- Garrett, Quick Reference, all ten quotations (page, page stack, area, decision point, conditional branch, relationships, connectors, crossbar, conditional connector, continuation points): PASS. The PDF is undated, as the unit says. http://www.jjg.net/ia/visvocab/files/garrett_ia_quickref.pdf
- Garrett's vocabulary "first released in October 2000 and revised since": PASS (Brown 2003: "In October 2000, Jesse James Garrett introduced..."; "has evolved the vocabulary over time"). The 2002 date in the brief: unverifiable (jjg.net index blocked to robots).
- That the Quick Reference has no element for objects, states or actors: PASS. All 17 elements were checked, and none is a thing with attributes, a state or a lane. This is labelled as the unit's reading.
- Brown 2003 interview: "black box", "proportional to the complexity", "haven't ever encountered a system", "Take the parts that can help you do your job, don't worry about the rest", "common language", "abstract classes of pages": PASS. All are Garrett's own words (JJG). "tool-independent" and "any diagramming software as well as any medium" are in the article's introduction: PASS. https://boxesandarrows.com/the-visual-vocabulary-three-years-later-an-interview-with-jesse-james-garrett/
- Brown, Communicating Design, 2nd ed., New Riders: September 2010, copyright 2011: PASS (InformIT). Ch. 5 definition, aliases, "increasingly represent page types or templates", "A site map shows how all the information...", "one view": PASS. Ch. 6 aliases, "may not reveal all the details... comprehensive view", "Flowcharts visualize a process...", "often represent a series of screens...": PASS. Chs 5 and 6 each have an At-A-Glance and a Purpose section: PASS. Ch. 2 is "Diagram Basics": PASS. The "theoretical foundation" quotation is truncated and overstated (minor finding). The "Anatomy of a Design Diagram" heading is unverifiable: the preview shows only "Anatomy ...".
- Rosenfeld, Morville and Arango, 4th ed., ch. 13: "the two most common types of IA diagrams", "capturing your past decisions and guiding your future ones", "connecting and managing granular content", and the headings High-Level Architecture Sitemaps and Detailed Sitemaps: PASS. Ch. 8, embedded systems (global, local, contextual) and supplemental systems (sitemaps, indexes, guides, configurators, search): PASS. Ch. 10 coverage: PASS. The "glue" quotation: FAIL, qualifier dropped (should-fix). Ch. 2, "digital, physical, and cross-channel ecosystems": PASS.
- UML 2.5.1, December 2017: PASS (OMG page). The multiplicity notation 1, 0..*, 1..*: PASS against a secondary source (uml-diagrams.org, which cites UML 2.4.1). The clause of the 2.5.1 specification was not opened, as the unsure list says.
- Prater, "Object-Oriented UX", A List Apart, 20 Oct 2015, by-line Sophia V. Prater, "putting object design before procedural action design", the four steps, and nesting defining "implicitly, the contextual navigation": PASS. The page metadata uses the name Voychehovski; the unit leaves it out, correctly.
- Shostack, HBR, January 1984: PASS for the date and author. The HBR page does not show the blueprint text. That it is the origin of the service blueprint is unverifiable from the page cited; a secondary source supports it (Wikipedia, "Service blueprint", citing HBR 62(1), 133 to 139).
- Harel 1987, Science of Computer Programming 8, pp. 231 to 274, "extend conventional state-transition diagrams with essentially three elements" (hierarchy, concurrency, communication): PASS. https://www.inf.ed.ac.uk/teaching/courses/seoc/2006_2007/resources/statecharts.pdf
- Kaley, NN/g, 27 Sep 2020: the definitions, eight inventory fields and keep/update/remove with an owner per update: PASS.
- Laubheimer, Taxonomy 101, NN/g, 3 Jul 2022: the definition and the backstage/frontstage framing: PASS. "need not match the order people browse in": PASS as a paraphrase of "often very different than the IA structure or the navigation". Terms reaching users through search suggestions and filters: PASS.
- Laubheimer, Wireflows, NN/g, 4 Dec 2016: both quotations PASS.
- Kaplan, NN/g, 16 Apr 2023: both definitions PASS.
- Gibbons, NN/g, 27 Aug 2017: definition fragments, four lanes plus evidence, three lines: PASS.
- Kalbach, Mapping Experiences, 2nd ed., O'Reilly, 2020: ch. 10 Service Blueprints, under "Part 3. Primary Diagram Types in Detail": PASS. Subtitle "A Complete Guide to Customer Alignment Through Journeys, Blueprints, and Diagrams": PASS.
- NISO Z39.19-2005 (R2010): the title and the four kinds (lists, synonym rings, taxonomies, thesauri): PASS.
- Hedden, The Accidental Taxonomist, 3rd ed., Information Today, 2022: PASS.
- Sitemaps.org protocol page dated 21 Nov 2016: PASS.
- WCAG 2.2, W3C Recommendation 12 Dec 2024, SC 1.4.1 quotation: PASS.
- Cardello 2014, a first pass at the IA before choosing components: PASS. Cardello and Tankala cited for "menus ... add routes the hierarchy does not have": FAIL, a stretch beyond both sources (should-fix).
- Tankala, NN/g, 3 Sep 2023: a sitemap deliberately leaves out detail: PASS.
- "Neither covers colour" (Garrett, Brown): unverifiable. Brown ch. 2 was not readable past its opening; the Quick Reference names no colour element.

## (3) Figures: every number says whose figure it is

- The unit carries no statistics. Its numbers are edition years, dates, page ranges and the notation's own counts (1, 0..*, 1..*), which section 1.5 attributes to UML 2.5.1. PASS. The Perqo dates in the inventory table are labelled (Perqo, fictional). PASS.

## (4) Labels

- Practice sources are labelled: Prater (practice), Brown 2003 (interview; practice). Vendor and standards documentation is labelled: NISO, OMG, W3C, Sitemaps.org (protocol documentation). PASS.
- Course conventions are labelled as conventions: the fidelity scale, the user flow and task flow split, the cross-surface map, the rules in section 4. PASS.
- The five faults are labelled as synthesis and craft practice. PASS. Two unsourced frequency claims sit inside that section ("most misreadings", "most flows"): minor findings.
- No correlational data, no anecdote and no real company's IA are asserted. PASS.
- Perqo is labelled (Perqo, fictional) at its first use (section 1.8) and in every Perqo example and figure caption. PASS.

## (5) Deliverable

- The course notation sheet is present in full: tones, shapes, lines, labels, tables and the face of every artefact. It follows from sections 2 and 5 and can be used alone. Four companion edits keep it in line with the section 5.2 fixes, and one adds a missing surface symbol.
- The artefact decision table is present, but its "built in" column is a placeholder in every row, so the deliverable is short of what the brief asks for (should-fix, with the codes from course-units.md).
- Neither deliverable adds an unsourced claim. PASS.

## (6) Pointers to IA1 and Perqo facts

Errata: none to check (no audit has run on this course).

- "IA1 set the rule ... states on its face what it leaves out (IA1, section 4)": PASS (IA1, section 4, and the Deliverable line "Every IA deliverable states on its face").
- "the six touchpoints ... as IA1 section 4 first described what each reads for": PASS.
- "IA1's mapping of one data-model entity to two labels (section 2.4)" and the rule that the mapping is written down: PASS.
- "whether a route is a tab bar, a drawer or a link is interface design (IA1, section 2.1)": FAIL, minor. IA1 calls it navigation design.
- "IA1 named the states of a Perqo claim: submitted, approved, rejected, paid (IA1, section 5)": PASS.
- "IA1's Perqo surfaces map was its first draft (IA1, Deliverable)", and IA1's own line "IA2 redraws it in the course notation": PASS.
- Help centre split by audience then by task; support owns the claim article (IA1, section 2.3): PASS.
- Contextual routes, employee record to claims (IA1, 2.2) and app Claims screen to Help centre (IA1, 2.3): PASS.
- Admin areas (Employees, Budgets, Policies, Approvals, Reports, Settings), app areas (Home, Benefits, Claims, Card, Account), perqo.com areas: PASS. Book a demo is listed as a global route on perqo.com and called one of IA1's top-level areas: FAIL, minor.
- The four benefit categories (Health, Learning, Mobility, Meals) and categories switched on per group in Policies: PASS.
- Vocabulary: allocation as Budget (Admin), Balance (app), Benefits budget (perqo.com); transaction of type claim as Claim, Claim, Claims; policy as Policy, not shown, Policies: PASS. "the three shared objects from IA1's vocabulary table": FAIL, minor (IA1 has five).
- A policy belongs to an employee group; a claim is checked against a policy and spends from a budget (IA1, section 5): PASS. Finance sets budgets per employee group and period (IA1, section 5): PASS.
- IA1's line from Admin to the app, "budgets, policies, invites, decisions": quoted correctly. The redraw drops the policy-to-app crossing that IA1's table records (error, figure 8).
- New Perqo facts introduced here (auto-approve limit, over-balance rejection, Perqo card product page, Customer stories, inventory IDs and dates) do not contradict IA1. PASS.

## (7) Figures

- Figure 1 · matrix · section 5.2 (the legend): FIX (should-fix). Every label traces to 5.2, but the legend leaves out several 5.2 rules. The caption names no decision and does not say Perqo is fictional, though the cells name Perqo's surfaces. The kind fits (items by sections: matrix). Replacement JSON is in the findings list.
- Figure 2 · sitemap · section 5.3 Structure: FIX (error). Traced: Home, Product, Pricing, Customers, Help centre, Book a demo, Sign in, Perqo Admin, Perqo app, Perqo card, Customer stories ("one page per client"), For HR and finance teams, For employees, Claims, Claim articles, "→ see Perqo Admin". Not in the text: "HR and finance articles", "grouped by task". The figure also mixes levels. The kind fits (hierarchy: sitemap). The caption passes.
- Figure 3 · objects · section 5.3 Objects (object-relationship map): FIX (error). Traced: the object names, "open categories", "auto-approve limit", all six actions, "belongs to", "contains", "submits", "is checked against", "spends from", "holds", and the counts 1 and 1..* on "holds". Not in the text: "name", "work email", Budget "amount", 1..* on "contains", 0..* on "submits". Two relationships read backwards. The kind fits (things and relationships: objects). The caption passes.
- Figure 4 · wireflow · section 5.3 Flows: FIX (minor). Every screen title, line, button and arrow label traces to the Flows paragraph. The arrow "edit" breaks the flow-label rule and has no control on its screen. The kind fits (screens: wireflow). The caption passes.
- Figure 5 · decision · section 5.3 Rules: PASS. Every question and outcome traces to the Rules paragraph ("Amount within the employee's balance?", "At or under the policy's auto-approve limit?", "Approved automatically", "Waits in Approvals: HR approves?", "Approved", "Rejected by HR", "Rejected, over balance"). The tones are as stated and "yes" is on the left. The kind fits (a rule with branches: decision). The caption passes. (Its HR step conflicts with the definition in 1.7; the fix is in the text.)
- Figure 6 · states · section 5.3 Lifecycles: FIX (minor). Traced: Submitted, Approved, Paid, Rejected, "approve, by rule or HR", "pay out", "reject, by rule or HR", "waits in Approvals". The note overstates who waits, and the caption attributes the plain form to Harel. The kind fits (a lifecycle: states).
- Figure 7 · swimlanes · section 5.3 Journeys (service blueprint): PASS. Every lane, step, note and link traces to the blueprint paragraph ("Pays for a course", "evidence: receipt", "Submits claim", "New claim form", "uses", "submit", "Checks policy and balance", "[over limit]", "Approves in Approvals", "approve", "Pays out", "Shows Paid", "status Paid"). The lanes are Gibbons's four. The kind fits (a journey across actors: swimlanes). The caption names the artefact, the decision, the section, the source and that Perqo is fictional.
- Figure 8 · objects · section 5.3 Journeys (cross-surface interaction map): FIX (error). Every box label and attribute traces to IA1's surfaces map and vocabulary table, and every link label traces to the paragraph. Three lines read backwards, and IA1's policy-to-app crossing is missing. The kind fits (things and relationships: objects). The caption passes.

All eight original blocks and all six replacement blocks render with this folder's viz.py (python3 -c "import json, viz; viz.render(...)"). No replacement raises.

## Findings

1. [error] [figure] 5.3 Objects (object-relationship map); Current: the whole viz block below (it occurs once); Problem: Read by any rule a reader can apply, two of the six relationships state the opposite of the text. "submits" runs on a level line from Claim (left) to Employee (right), so it reads "Claim submits Employee"; "is checked against" runs up from Claim to Policy above it, so read top-down it says "Policy is checked against Claim". The objects kind draws no arrowheads, so the data's from/to order cannot be seen. The figure also carries labels and counts that the text does not give: the attributes "name" and "work email", Budget's "amount", and the counts 1..* on "contains" and 0..* on "submits". The companion text fix for those is below (section 5.3 Objects paragraph). Fix: replace the whole block, fences included, with the block given; Basis: Unit's own text, section 5.3 ("An employee submits claims; each claim is checked against the group's policy"); renderer viz.py objects(), which draws links with _line and no head. Re-laid out and rendered without error with this folder's viz.py.

Current:
```viz
{"kind": "objects", "caption": "Object-relationship map (objects family): the core objects of Perqo Admin with attributes, actions and counts at F2; supports the decision on what Admin holds and how its parts relate (section 5.3). Perqo is fictional; relationships from IA1, section 5, and this unit; counts in UML 2.5.1 multiplicity notation; object-first method from Prater 2015.",
 "objects": [
  {"id": "policy", "title": "Policy", "tone": 4, "attrs": ["open categories", "auto-approve limit"], "actions": ["-> edit"]},
  {"id": "group", "title": "Employee group", "tone": 4, "attrs": ["name"], "actions": ["-> invite employees"]},
  {"id": "claim", "title": "Claim", "tone": 4, "attrs": ["amount", "category", "receipt", "status"], "actions": ["-> approve", "-> reject"]},
  {"id": "employee", "title": "Employee", "tone": 4, "attrs": ["name", "work email"], "actions": ["-> move to group"]},
  {"id": "budget", "title": "Budget", "tone": 4, "attrs": ["amount", "category", "period"], "actions": ["-> set"]}
 ],
 "rows": [["policy", "group"], ["claim", "employee"], ["budget", null]],
 "links": [
  {"from": "policy", "to": "group", "label": "belongs to", "from_card": "1", "to_card": "1"},
  {"from": "group", "to": "employee", "label": "contains", "from_card": "1", "to_card": "1..*"},
  {"from": "employee", "to": "claim", "label": "submits", "from_card": "1", "to_card": "0..*"},
  {"from": "claim", "to": "policy", "label": "is checked against", "from_card": "0..*", "to_card": "1"},
  {"from": "claim", "to": "budget", "label": "spends from", "from_card": "0..*", "to_card": "1"},
  {"from": "employee", "to": "budget", "label": "holds", "from_card": "1", "to_card": "1..*"}
 ]}
```
Fix:
```viz
{"kind": "objects", "caption": "Object-relationship map (objects family): the core objects of Perqo Admin with attributes, actions and counts at F2, every box in tone 4 because the figure shows one surface; supports the decision on what Admin holds and how its parts relate (section 5.3). Each relationship reads from left to right on a level line, from top to bottom otherwise. Perqo is fictional; relationships and attributes from this section and IA1, section 5; counts in UML 2.5.1 multiplicity notation; object-first method from Prater 2015.", "objects": [{"id": "policy", "title": "Policy", "tone": 4, "attrs": ["open categories", "auto-approve limit"], "actions": ["-> edit"]}, {"id": "group", "title": "Employee group", "tone": 4, "attrs": ["name"], "actions": ["-> invite employees"]}, {"id": "claim", "title": "Claim", "tone": 4, "attrs": ["amount", "category", "receipt", "status"], "actions": ["-> approve", "-> reject"]}, {"id": "employee", "title": "Employee", "tone": 4, "attrs": ["name", "work email"], "actions": ["-> move to group"]}, {"id": "budget", "title": "Budget", "tone": 4, "attrs": ["amount", "category", "period"], "actions": ["-> set"]}], "rows": [[null, "group", null], ["employee", "claim", "policy"], [null, "budget", null]], "links": [{"from": "group", "to": "policy", "label": "follows", "from_card": "1", "to_card": "1"}, {"from": "group", "to": "employee", "label": "contains", "from_card": "1", "to_card": "1..*"}, {"from": "employee", "to": "claim", "label": "submits", "from_card": "1", "to_card": "0..*"}, {"from": "claim", "to": "policy", "label": "is checked against", "from_card": "0..*", "to_card": "1"}, {"from": "claim", "to": "budget", "label": "spends from", "from_card": "0..*", "to_card": "1"}, {"from": "employee", "to": "budget", "label": "holds", "from_card": "1", "to_card": "1..*"}]}
```

2. [error] [figure] 5.3 Journeys (cross-surface interaction map); Current: the whole viz block below (it occurs once); Problem: Three lines read the wrong way round. "is checked against" runs on a level line from claim (middle) to policy (left), so it reads "policy is checked against claim"; "shown as Balance" runs up from allocation to the app, so read top-down it says "app shown as Balance allocation"; "queues in Approvals" runs up from claim to Admin. The redraw also drops one crossing that IA1 records: IA1's line from Admin to the app carried policies "as open categories and approval rules" (IA1, Deliverable, What crosses between surfaces), and here no line joins policy to the app. The companion text fix is below (section 5.3, cross-surface paragraph). Fix: replace the whole block, fences included, with the block given; Basis: IA1, Deliverable, table What crosses between surfaces (row Perqo Admin to Perqo app: "Budgets (as balances), policies (as open categories and approval rules), invitations, approval decisions"); viz.py objects(). Rendered without error with this folder's viz.py.

Current:
```viz
{"kind": "objects", "caption": "Cross-surface interaction map (journeys family): IA1's Perqo surfaces map redrawn in the course notation, with three shared objects and their names on each surface, F1; supports the decision on which surface and under which name a thing belongs (section 5.3). Perqo is fictional; surfaces, areas and vocabulary from IA1, section 5 and Deliverable.",
 "objects": [
  {"id": "site", "title": "perqo.com", "tone": 1, "attrs": ["Product", "Pricing", "Customers", "Help centre", "Sign in"], "actions": ["-> book a demo", "-> find help"]},
  {"id": "admin", "title": "Perqo Admin", "tone": 4, "attrs": ["Employees", "Budgets", "Policies", "Approvals", "Reports", "Settings"], "actions": ["-> configure", "-> approve", "-> report"]},
  {"id": "app", "title": "Perqo app", "tone": 3, "attrs": ["Home", "Benefits", "Claims", "Card", "Account"], "actions": ["-> see balance", "-> spend", "-> claim"]},
  {"id": "policy", "title": "policy", "tone": 5, "attrs": ["Admin: Policy", "app: not shown", "perqo.com: Policies"]},
  {"id": "claim", "title": "transaction, type claim", "tone": 5, "attrs": ["Admin: Claim", "app: Claim", "perqo.com: Claims"]},
  {"id": "alloc", "title": "allocation", "tone": 5, "attrs": ["Admin: Budget", "app: Balance", "perqo.com: Benefits budget"]}
 ],
 "rows": [[null, "site", null], ["admin", null, "app"], ["policy", "claim", "alloc"]],
 "links": [
  {"from": "site", "to": "admin", "label": "contract, sign in"},
  {"from": "site", "to": "app", "label": "download, help"},
  {"from": "admin", "to": "app", "label": "invites, decisions"},
  {"from": "admin", "to": "alloc", "label": "sets"},
  {"from": "admin", "to": "policy", "label": "sets"},
  {"from": "alloc", "to": "app", "label": "shown as Balance"},
  {"from": "app", "to": "claim", "label": "submits"},
  {"from": "claim", "to": "policy", "label": "is checked against"},
  {"from": "claim", "to": "alloc", "label": "spends from"},
  {"from": "claim", "to": "admin", "label": "queues in Approvals"}
 ]}
```
Fix:
```viz
{"kind": "objects", "caption": "Cross-surface interaction map (journeys family): IA1's Perqo surfaces map redrawn in the course notation, with three shared objects and their names on each surface, F1; supports the decision on which surface and under which name a thing belongs (section 5.3). Each line reads from left to right on a level line, from top to bottom otherwise. Perqo is fictional; surfaces, areas and vocabulary from IA1, section 5 and Deliverable.", "objects": [{"id": "site", "title": "perqo.com", "tone": 1, "attrs": ["Product", "Pricing", "Customers", "Help centre", "Sign in"], "actions": ["-> book a demo", "-> find help"]}, {"id": "admin", "title": "Perqo Admin", "tone": 4, "attrs": ["Employees", "Budgets", "Policies", "Approvals", "Reports", "Settings"], "actions": ["-> configure", "-> approve", "-> report"]}, {"id": "app", "title": "Perqo app", "tone": 3, "attrs": ["Home", "Benefits", "Claims", "Card", "Account"], "actions": ["-> see balance", "-> spend", "-> claim"]}, {"id": "policy", "title": "policy", "tone": 5, "attrs": ["Admin: Policy", "app: not shown", "perqo.com: Policies"]}, {"id": "claim", "title": "transaction, type claim", "tone": 5, "attrs": ["Admin: Claim", "app: Claim", "perqo.com: Claims"]}, {"id": "alloc", "title": "allocation", "tone": 5, "attrs": ["Admin: Budget", "app: Balance", "perqo.com: Benefits budget"]}], "rows": [[null, "site", null], ["admin", null, "app"], ["claim", null, "alloc"], [null, "policy", null]], "links": [{"from": "site", "to": "admin", "label": "contract, sign in"}, {"from": "site", "to": "app", "label": "download, help"}, {"from": "admin", "to": "app", "label": "invites, decisions"}, {"from": "admin", "to": "alloc", "label": "sets"}, {"from": "admin", "to": "policy", "label": "sets"}, {"from": "app", "to": "alloc", "label": "shows as Balance"}, {"from": "app", "to": "policy", "label": "shows its effect as open categories and approval rules"}, {"from": "app", "to": "claim", "label": "submits"}, {"from": "claim", "to": "policy", "label": "is checked against"}, {"from": "claim", "to": "alloc", "label": "spends from"}, {"from": "admin", "to": "claim", "label": "approves in Approvals"}]}
```

3. [error] [figure] 5.3 Structure (sitemap); Current: the whole viz block below (it occurs once); Problem: The label "HR and finance articles" and its note "grouped by task" do not appear in the unit's text. The figure also shows the fault the unit lists as fault 3, mixed levels: For HR and finance teams goes straight to a stack of articles, while For employees has a task level (Claims). And it leaves out task groups that the unit's own inventory URLs give: hr-finance/budgets, hr-finance/policies and employees/balance. The companion text fix is below (section 5.3 Structure paragraph). Fix: replace the whole block, fences included, with the block given; Basis: Unit's own text: section 3, fault 3 ("one area drawn to its leaves beside another drawn to its first level"); section 5.3, inventory rows H-1.1.1, H-1.2.4 and H-2.2.1; IA1, section 2.3 ("split first by audience ... and then by task"). Rendered without error with this folder's viz.py.

Current:
```viz
{"kind": "sitemap", "caption": "Sitemap (structure family): the perqo.com structure at F2, page types tagged and many-of-a-kind pages drawn as one stack; supports the decision on where a new page belongs (section 5.3). Perqo is fictional; Help centre split from IA1, section 2.3; page-type and stack conventions from Brown 2011, ch. 5, and Garrett's Quick Reference.", "stack_from": 2,
 "root": {"label": "Home", "type": "home", "tone": 1, "children": [
  {"label": "Product", "type": "section", "tone": 1, "children": [
    {"label": "Perqo Admin", "type": "detail"}, {"label": "Perqo app", "type": "detail"}, {"label": "Perqo card", "type": "detail"}]},
  {"label": "Pricing", "type": "detail", "tone": 1},
  {"label": "Customers", "type": "index", "tone": 1, "children": [
    {"label": "Customer stories", "type": "stack", "note": "one page per client"}]},
  {"label": "Help centre", "type": "index", "tone": 1, "children": [
    {"label": "For HR and finance teams", "type": "section", "children": [
      {"label": "HR and finance articles", "type": "stack", "note": "grouped by task"}]},
    {"label": "For employees", "type": "section", "children": [
      {"label": "Claims", "type": "section", "children": [
        {"label": "Claim articles", "type": "stack"}]}]}]},
  {"label": "Book a demo", "type": "form", "tone": 1},
  {"label": "Sign in", "type": "external", "note": "→ see Perqo Admin", "tone": 1}]}}
```
Fix:
```viz
{"kind": "sitemap", "caption": "Sitemap (structure family): the perqo.com structure at F2, page types tagged and many-of-a-kind pages drawn as one stack; supports the decision on where a new page belongs (section 5.3). Perqo is fictional; Help centre split from IA1, section 2.3; page-type and stack conventions from Brown 2011, ch. 5, and Garrett's Quick Reference.", "stack_from": 2, "root": {"label": "Home", "type": "home", "tone": 1, "children": [{"label": "Product", "type": "section", "tone": 1, "children": [{"label": "Perqo Admin", "type": "detail"}, {"label": "Perqo app", "type": "detail"}, {"label": "Perqo card", "type": "detail"}]}, {"label": "Pricing", "type": "detail", "tone": 1}, {"label": "Customers", "type": "index", "tone": 1, "children": [{"label": "Customer stories", "type": "stack", "note": "one page per client"}]}, {"label": "Help centre", "type": "index", "tone": 1, "children": [{"label": "For HR and finance teams", "type": "section", "children": [{"label": "Budgets", "type": "section", "children": [{"label": "Budget articles", "type": "stack"}]}, {"label": "Policies", "type": "section", "children": [{"label": "Policy articles", "type": "stack"}]}]}, {"label": "For employees", "type": "section", "children": [{"label": "Claims", "type": "section", "children": [{"label": "Claim articles", "type": "stack"}]}, {"label": "Balance", "type": "section", "children": [{"label": "Balance articles", "type": "stack"}]}]}]}, {"label": "Book a demo", "type": "form", "tone": 1}, {"label": "Sign in", "type": "external", "note": "→ see Perqo Admin", "tone": 1}]}}
```

4. [should-fix] [deliverable] 5.2 Labels; Current: "A relationship's label is a verb read from the first object to the second ("submits"), with a count at each end."; Problem: The objects kind draws relationships as lines with no head, so a reader cannot see which object is "first". The rule cannot be applied by reading the figure, and two figures in this unit read backwards because of it (see the errors above). Fix: "A relationship's label is a verb that reads from left to right on a level line and from top to bottom otherwise ("submits"), with a count at each end; the boxes are placed so that every label reads that way."; Basis: viz-kinds.md, objects ("a link is a line with a label and a cardinality at each end"); viz.py objects().
5. [should-fix] [deliverable] 5.2 Tones; Current: "Tone 5: shared, meaning the data model, the Perqo system, and any object or term that lives on more than one surface."; Problem: Taken literally, the rule makes Claim and Budget tone 5 in the Admin object-relationship map, because they live on Admin and the app, yet that figure draws them in tone 4. Meanwhile the sitemap paragraph sets the opposite rule ("Every box is tone 1, because the whole map is one surface"). The notation has to say which rule wins. Fix: "Tone 5: shared, meaning the data model, the Perqo system, and any object or term that lives on more than one surface; in a figure of one surface, every box takes that surface's tone, as in the sitemap and the object-relationship map below."; Basis: Unit's own text, section 5.3 Structure ("Every box is tone 1, because the whole map is one surface") and the object-relationship map block (every object "tone": 4).
6. [should-fix] [accuracy] 1.7 Decision tree; Current: "A decision tree has no screens and no user steps; it is the system's logic."; Problem: The unit's own decision tree in section 5.3 contains a person's step: "Waits in Approvals: HR approves?", drawn in HR's tone 4. In Garrett's terms that is a decision point (a user action with several results), not a conditional branch ("not based on user action"). The definition contradicts the example it introduces. Fix: "A decision tree has no screens; it is the system's logic, and where that logic waits on a person's decision (HR's approval in section 5.3), that decision is one question box in the person's tone, Garrett's decision point beside his conditional branch."; Basis: Garrett, Visual Vocabulary Quick Reference, decision point and conditional branch entries, http://www.jjg.net/ia/visvocab/files/garrett_ia_quickref.pdf; the unit's decision block, section 5.3.
7. [should-fix] [attribution] 1.3 Sitemap, Not to be mistaken for; Current: "A sitemap shows the hierarchy; the menus show part of it at a time and add routes the hierarchy does not have (Cardello, NN/g, 2014; Tankala, NN/g, 2023)."; Problem: Neither cited article says that menus show part of the hierarchy at a time or add routes the hierarchy lacks. Tankala says a sitemap "is only a visual display of the hierarchy and organization of your content". Cardello says IA metadata can generate "Related Link" lists. The added-routes point is a reading of Cardello's remark, not his statement. Fix: "A sitemap "is only a visual display of the hierarchy and organization of your content" (Tankala, NN/g, 2023); the navigation is the interface built on the IA, and on this unit's reading it shows part of the hierarchy at a time and adds routes the hierarchy does not have, such as the "Related Link" lists that Cardello says IA metadata can generate (Cardello, NN/g, 2014)."; Basis: Tankala, "Information Architecture vs. Sitemaps", NN/g, 3 Sep 2023, https://www.nngroup.com/articles/information-architecture-sitemaps/; Cardello, "The Difference Between Information Architecture (IA) and Navigation", NN/g, 22 Jun 2014, https://www.nngroup.com/articles/ia-vs-navigation/
8. [should-fix] [accuracy] 1.2 Taxonomy and controlled vocabulary; Current: "and says "controlled vocabularies have become the glue that holds the systems together" (2015, ch. 10)"; Problem: The quotation drops the book's qualifier. The full sentence reads "In many large metadata-driven products, controlled vocabularies have become the glue that holds the systems together." Cut short, it reads as a general claim. Fix: "and says that "In many large metadata-driven products, controlled vocabularies have become the glue that holds the systems together" (2015, ch. 10)"; Basis: Rosenfeld, Morville and Arango, 4th ed., 2015, ch. 10 opening, https://www.oreilly.com/library/view/information-architecture-4th/9781491913529/ch10.html
9. [should-fix] [deliverable] Deliverable · The artefact decision table; Current: the text below (it occurs once); Problem: The brief requires the column "unit of this course that builds it". Every row reads "at filing", which is a placeholder. The course's units list gives each code: IA5 ships the perqo.com content inventory and sitemap; IA4 the object map and the faceted taxonomy; IA6 the wireflows; IA7 the object-relationship map, navigation model and approval state diagram; IA8 the decision trees, lifecycle swimlanes and interaction map; DD-IA3 the controlled vocabulary starter. No unit ships a user flow, task flow or service blueprint by name, so the nearest form is named. Fix: the text below; Basis: course-units.md (IA4 to IA8, DD-IA3, "Ships" lines); brief.md ("question asked → artefact → fidelity → reader → unit of this course that builds it").

Current:
```
*Start from the question you have been asked. Fidelity is given by stage (section 1.0: F1 sketch, F2 working, F3 specification). The last column gives this unit's example, then the unit of this course that builds the artefact in full. The course's build order was not among this unit's inputs, so that unit's code is entered at filing ("at filing" below); no code is guessed.*

| Question asked | Artefact | Figure kind | Fidelity by stage | Reader | Example · built in |
|---|---|---|---|---|---|
| What content do we have, and is it any good? | Content inventory and audit | table | F2 before any redesign; F3 as the migration list | content, support, product management, client | §5.3 inventory · at filing |
| What is each thing called, and which words mean the same? | Controlled vocabulary | table | F1 word list in discovery; F2 once labels agreed; F3 for search, filters, tagging | content, engineering, support, sales | §5.3 vocabulary · at filing |
| How do the terms nest? | Taxonomy | tree, or table | F2 in design; F3 when built into metadata | content, engineering | §5.3 vocabulary · at filing |
| What exists on this surface, and what sits under what? | Sitemap (structural) | sitemap | F1 top two levels in discovery; F2 every group and page type in design; F3 with identifiers for build | product management, engineering, content, sales | §5.3 sitemap · at filing |
| By which routes can a person reach each thing? | Navigation model | table or matrix | F2 before navigation components are chosen | engineering, content, support | §5.3 navigation table · at filing |
| What does the system hold, and what can people do to it? | Object map | objects | F1 nouns in discovery; F2 attributes and actions in design | engineering, product management | §5.3 object map · at filing |
| How are the system's things related, and how many of each? | Object-relationship map | objects | F2 in design; F3 as the agreed mapping to the data model | engineering, product management, client | §5.3 object map · at filing |
| What steps does one kind of user take to a goal, branches included? | User flow | flow or wireflow | F2 in design, with failure paths | design, engineering, support, product management | none here · at filing |
| What is the main path of one task? | Task flow | flow | F1 in discovery | design, product management | none here · at filing |
| Which screens does a task need, and what changes on them? | Wireflow | wireflow | F2 in design; F3 for build of a dynamic sequence | design, engineering, support | §5.3 wireflow · at filing |
| Given these facts, which outcome does the system produce? | Decision tree | decision | F2 in design; F3 for build, every branch complete | engineering, product management, client, support | §5.3 decision tree · at filing |
| What states can a thing be in, and what moves it? | State diagram | states | F2 every visible state in design; F3 every trigger for build | engineering, content, support, client | §5.3 state diagram · at filing |
| For one journey, who does what, front and back, and what supports it? | Service blueprint | swimlanes | F1 in discovery; F2 when the service changes | support, product management, client | §5.3 blueprint · at filing |
| Across surfaces, what is shared, what is it called on each, and what crosses? | Cross-surface interaction map | objects (with swimlanes for a journey) | F1 at the start of cross-surface work; F2 kept current; F3 as the canonical vocabulary | all six touchpoints | §5.3 cross-surface map · at filing |
| Is this artefact someone handed me sound? | none: review it | the five faults (section 3) | at every handover | the designer receiving it | §3 |
```
Fix:
```
*Start from the question you have been asked. Fidelity is given by stage (section 1.0: F1 sketch, F2 working, F3 specification). The last column gives this unit's example, then the unit of this course that builds the artefact in full. Where no unit ships the artefact under its own name, the unit that ships its nearest form is named, with that form in brackets.*

| Question asked | Artefact | Figure kind | Fidelity by stage | Reader | Example · built in |
|---|---|---|---|---|---|
| What content do we have, and is it any good? | Content inventory and audit | table | F2 before any redesign; F3 as the migration list | content, support, product management, client | §5.3 inventory · IA5 |
| What is each thing called, and which words mean the same? | Controlled vocabulary | table | F1 word list in discovery; F2 once labels agreed; F3 for search, filters, tagging | content, engineering, support, sales | §5.3 vocabulary · DD-IA3 |
| How do the terms nest? | Taxonomy | tree, or table | F2 in design; F3 when built into metadata | content, engineering | §5.3 vocabulary · IA4 |
| What exists on this surface, and what sits under what? | Sitemap (structural) | sitemap | F1 top two levels in discovery; F2 every group and page type in design; F3 with identifiers for build | product management, engineering, content, sales | §5.3 sitemap · IA5 |
| By which routes can a person reach each thing? | Navigation model | table or matrix | F2 before navigation components are chosen | engineering, content, support | §5.3 navigation table · IA7 |
| What does the system hold, and what can people do to it? | Object map | objects | F1 nouns in discovery; F2 attributes and actions in design | engineering, product management | §5.3 object map · IA4 |
| How are the system's things related, and how many of each? | Object-relationship map | objects | F2 in design; F3 as the agreed mapping to the data model | engineering, product management, client | §5.3 object map · IA7 |
| What steps does one kind of user take to a goal, branches included? | User flow | flow or wireflow | F2 in design, with failure paths | design, engineering, support, product management | none here · IA6 (as wireflows) |
| What is the main path of one task? | Task flow | flow | F1 in discovery | design, product management | none here · IA6 (as wireflows) |
| Which screens does a task need, and what changes on them? | Wireflow | wireflow | F2 in design; F3 for build of a dynamic sequence | design, engineering, support | §5.3 wireflow · IA6 |
| Given these facts, which outcome does the system produce? | Decision tree | decision | F2 in design; F3 for build, every branch complete | engineering, product management, client, support | §5.3 decision tree · IA8 |
| What states can a thing be in, and what moves it? | State diagram | states | F2 every visible state in design; F3 every trigger for build | engineering, content, support, client | §5.3 state diagram · IA7 |
| For one journey, who does what, front and back, and what supports it? | Service blueprint | swimlanes | F1 in discovery; F2 when the service changes | support, product management, client | §5.3 blueprint · IA8 (as lifecycle swimlanes) |
| Across surfaces, what is shared, what is it called on each, and what crosses? | Cross-surface interaction map | objects (with swimlanes for a journey) | F1 at the start of cross-surface work; F2 kept current; F3 as the canonical vocabulary | all six touchpoints | §5.3 cross-surface map · IA8 |
| Is this artefact someone handed me sound? | none: review it | the five faults (section 3) | at every handover | the designer receiving it | §3 |
```

10. [should-fix] [figure] 5.2 The legend; Current: the whole viz block below (it occurs once); Problem: The caption breaks the unit's own caption rule (section 5.2): it names no decision the figure supports and does not say Perqo is fictional, though its cells name perqo.com, Perqo Admin and the Perqo app. The caption also says the legend gives "Tones, shapes, lines and label rules as set in section 5.2", but several of those rules are missing: the plain box of a tree, the matrix row, column and cell, the arrow from a box back to itself, the page-type tags, how a relationship label reads, the yes-left branch order and the "Surface: Label" lines. With the tone, decision-tree and reading-direction fixes above, three of its rows also change. Fix: replace the whole block, fences included, with the block given; Basis: Unit's own text, section 5.2 (Shapes, Lines, Labels, Captions). Rendered without error with this folder's viz.py.

Current:
```viz
{"kind": "matrix", "caption": "The course notation: legend (section 5.2). Tones, shapes, lines and label rules as set in section 5.2, derived from Garrett's Visual Vocabulary Quick Reference, Brown, Communicating Design, 2nd ed., 2011, chs 5 and 6, UML 2.5.1 multiplicities, Harel 1987 and Gibbons 2017. The six tone rows show each tone; the rows below them are drawn in tone 5 only because the figure kind colours every cell, and there the tone carries no meaning.", "cols": ["Drawn as", "Means"],
 "rows": [
  {"label": "Tone 1", "tone": 1, "cells": ["tone 1", "perqo.com"]},
  {"label": "Tone 2", "tone": 2, "cells": ["tone 2", "the merchant side and anything outside Perqo"]},
  {"label": "Tone 3", "tone": 3, "cells": ["tone 3", "the Perqo app and the employee"]},
  {"label": "Tone 4", "tone": 4, "cells": ["tone 4", "Perqo Admin and the HR and finance managers who use it"]},
  {"label": "Tone 5", "tone": 5, "cells": ["tone 5", "shared: the data model, the Perqo system, any object or term on more than one surface"]},
  {"label": "Tone 6", "tone": 6, "cells": ["tone 6", "a stop: a path that ends without success, or a fault found in a review"]},
  {"label": "Page or page type", "tone": 5, "cells": ["square-cornered box with a type tag", "one page, or one type of page; the tag names the type"]},
  {"label": "Object", "tone": 5, "cells": ["box with a filled title band", "a thing the system holds; attributes below, actions after the rule line"]},
  {"label": "Question", "tone": 5, "cells": ["outlined box with branches", "a question the system asks"]},
  {"label": "Outcome", "tone": 5, "cells": ["filled box", "where a decision ends"]},
  {"label": "State", "tone": 5, "cells": ["rounded box", "a state; inner ring: an end state; dot and arrow: the start"]},
  {"label": "Screen", "tone": 5, "cells": ["frame with a title bar", "one screen; bars and blocks are placeholders"]},
  {"label": "Lane", "tone": 5, "cells": ["band across the figure", "one actor or surface; the steps in it are theirs"]},
  {"label": "Line without a head", "tone": 5, "cells": ["plain line", "contains or relates"]},
  {"label": "Arrow", "tone": 5, "cells": ["line with a head", "movement or change: a person moves, the system acts, a state changes"]},
  {"label": "[condition]", "tone": 5, "cells": ["square brackets", "the path exists only when this holds"]},
  {"label": "1, 0..*, 1..*", "tone": 5, "cells": ["count at a line's end", "exactly one; any number including none; at least one"]},
  {"label": "-> verb", "tone": 5, "cells": ["line in an object box", "an action someone can take on the object"]},
  {"label": "→ see", "tone": 5, "cells": ["note", "continues in another figure or node"]},
  {"label": "(no way back)", "tone": 5, "cells": ["arrow label", "the person cannot return along this arrow"]},
  {"label": "assumed, proposed", "tone": 5, "cells": ["word in a note", "not yet evidenced; not yet agreed"]}
 ]}
```
Fix:
```viz
{"kind": "matrix", "caption": "The course notation: legend (section 5.2); supports reading and drawing every figure from IA3 on. Tones, shapes, lines and label rules as set in section 5.2, derived from Garrett's Visual Vocabulary Quick Reference, Brown, Communicating Design, 2nd ed., 2011, chs 5 and 6, UML 2.5.1 multiplicities, Harel 1987 and Gibbons 2017. Perqo is fictional. The six tone rows show each tone; the rows below them are drawn in tone 5 only because the figure kind colours every cell, and there the tone carries no meaning.", "cols": ["Drawn as", "Means"], "rows": [{"label": "Tone 1", "tone": 1, "cells": ["tone 1", "perqo.com"]}, {"label": "Tone 2", "tone": 2, "cells": ["tone 2", "the merchant side and anything outside Perqo"]}, {"label": "Tone 3", "tone": 3, "cells": ["tone 3", "the Perqo app and the employee"]}, {"label": "Tone 4", "tone": 4, "cells": ["tone 4", "Perqo Admin and the HR and finance managers who use it"]}, {"label": "Tone 5", "tone": 5, "cells": ["tone 5", "shared: the data model, the Perqo system, any object or term on more than one surface; in a figure of one surface, every box takes that surface's tone"]}, {"label": "Tone 6", "tone": 6, "cells": ["tone 6", "a stop: a path that ends without success, or a fault found in a review"]}, {"label": "Page or page type", "tone": 5, "cells": ["square-cornered box with a type tag", "one page, or one type of page; the tag names the type"]}, {"label": "Object", "tone": 5, "cells": ["box with a filled title band", "a thing the system holds; attributes below, actions after the rule line"]}, {"label": "Surface", "tone": 5, "cells": ["box with a filled title band, in a surface's tone", "one surface in a cross-surface map; its top-level areas below the title"]}, {"label": "Question", "tone": 5, "cells": ["outlined box with branches", "a question the system asks, or a decision a named person makes"]}, {"label": "Outcome", "tone": 5, "cells": ["filled box", "where a decision ends"]}, {"label": "State", "tone": 5, "cells": ["rounded box", "a state; inner ring: an end state; dot and arrow: the start"]}, {"label": "Screen", "tone": 5, "cells": ["frame with a title bar", "one screen; bars and blocks are placeholders"]}, {"label": "Lane", "tone": 5, "cells": ["band across the figure", "one actor or surface; the steps in it are theirs"]}, {"label": "Term or group", "tone": 5, "cells": ["plain box in a tree", "a term or a group in a hierarchy"]}, {"label": "Row, column, cell", "tone": 5, "cells": ["matrix", "an item, a dimension, the value where they meet"]}, {"label": "Line without a head", "tone": 5, "cells": ["plain line", "contains or relates"]}, {"label": "Arrow", "tone": 5, "cells": ["line with a head", "movement or change: a person moves, the system acts, a state changes"]}, {"label": "Arrow to itself", "tone": 5, "cells": ["arrow from a box back to itself", "an action that leaves the thing as it was"]}, {"label": "Type tag", "tone": 5, "cells": ["home, section, index, detail, stack, form, file, external", "the page's type"]}, {"label": "Relationship label", "tone": 5, "cells": ["verb on a line", "reads from left to right on a level line, from top to bottom otherwise"]}, {"label": "yes, no", "tone": 5, "cells": ["branch labels", "yes always on the left"]}, {"label": "Surface: Label", "tone": 5, "cells": ["line in a shared object", "that surface's name for it; the title is the data-model name"]}, {"label": "[condition]", "tone": 5, "cells": ["square brackets", "the path or the box exists only when this holds"]}, {"label": "1, 0..*, 1..*", "tone": 5, "cells": ["count at a line's end", "exactly one; any number including none; at least one"]}, {"label": "-> verb", "tone": 5, "cells": ["line in an object box", "an action someone can take on the object"]}, {"label": "→ see", "tone": 5, "cells": ["note", "continues in another figure or node"]}, {"label": "(no way back)", "tone": 5, "cells": ["arrow label", "the person cannot return along this arrow"]}, {"label": "assumed, proposed", "tone": 5, "cells": ["word in a note", "not yet evidenced; not yet agreed"]}]}
```

11. [should-fix] [figure] 5.3 Journeys, cross-surface paragraph (companion to the cross-surface map FIX); Current: "Admin sets the policy, which the app does not show as such (its effect shows as open categories and approval rules). The app submits claims; a claim is checked against the policy, spends from the allocation and queues in Approvals."; Problem: The replacement figure's labels "shows its effect as open categories and approval rules" and "approves in Approvals" must appear in the text. Fix: "Admin sets the policy, which the app does not show as such; the app shows its effect as open categories and approval rules. The app submits claims; a claim is checked against the policy and spends from the allocation, and Admin approves in Approvals the claims over the limit."; Basis: Sourcing standard Part 1 ("every label, date and number in it appears in the unit's own sourced text"); IA1, Deliverable, What crosses between surfaces.
12. [should-fix] [figure] 5.3 Objects paragraph (companion to the object-relationship map FIX); Current: "The actions are the ones HR and finance take: edit a policy, invite employees, move an employee to a group, set a budget, approve or reject a claim."; Problem: The figure's attributes "name" (group and employee), "work email" and Budget's "amount", and the counts 1..* (contains) and 0..* (submits, is checked against, spends from), are not in the text. Fix: "An employee group carries its name; an employee, a name and a work email; a budget, an amount for one category and period; a claim, an amount, a category, a receipt and a status. A group contains one or more employees (1..*); an employee submits any number of claims, including none (0..*); and any number of claims are checked against one policy and spend from one budget. The actions are the ones HR and finance take: edit a policy, invite employees, move an employee to a group, set a budget, approve or reject a claim."; Basis: Sourcing standard Part 1, figure rule; IA1, Deliverable, vocabulary table (allocation per employee, category, period).
13. [should-fix] [figure] 5.3 Structure paragraph (companion to the sitemap FIX); Current: "The Help centre splits into For HR and finance teams and For employees; under For employees, Claims holds the claim articles."; Problem: The replacement figure's task groups and stacks have to be in the text. They come from the inventory's URLs in the same section. Fix: "The Help centre splits into For HR and finance teams and For employees, then by task, as the inventory's URLs show: Budgets and Policies under For HR and finance teams, Claims and Balance under For employees, each a stack of its articles (Budget articles, Policy articles, Claim articles, Balance articles)."; Basis: Unit's own section 5.3 inventory rows (URLs perqo.com/help/hr-finance/budgets/..., /hr-finance/policies/..., /employees/claims/..., /employees/balance); IA1, section 2.3.
14. [minor] [accuracy] 1.4 Navigation model (pointer to IA1); Current: "whether a route is a tab bar, a drawer or a link is interface design (IA1, section 2.1)"; Problem: IA1, section 2.1 calls the choice between tabs, a list under a tab and filters navigation design, not interface design. IA1, section 2.2 covers interface design. Fix: "whether a route is a tab bar, a drawer or a link is navigation design (IA1, section 2.1)"; Basis: IA1, section 2.1 ("Whether the app shows the categories as a row of tabs ... is navigation design").
15. [minor] [accuracy] 5.3 Structure, navigation model (Perqo consistency); Current: "The global routes are IA1's top-level areas;"; Problem: The perqo.com global row includes Book a demo. IA1's top-level areas for perqo.com are Product, Pricing, Customers, Help centre and Sign in; IA1 has "book a demo" only as an action. Fix: "The global routes are IA1's top-level areas, with Book a demo added on perqo.com;"; Basis: IA1, section 5 and Deliverable, surfaces table (Top-level areas column) and surfaces map ("-> book a demo").
16. [minor] [accuracy] 5.3 Journeys, cross-surface paragraph (pointer to IA1); Current: "with the three shared objects from IA1's vocabulary table added as boxes of their own"; Problem: IA1's vocabulary table has five rows (allocation; transaction, type card payment; transaction, type claim; policy; employee group). "the three" suggests it has three. Fix: "with three of the five shared objects in IA1's vocabulary table (allocation, transaction of type claim, and policy) added as boxes of their own"; Basis: IA1, Deliverable, "One thing, three names" table.
17. [minor] [accuracy] 2.2 Brown; Current: "and says it "lays a theoretical foundation from which you can build all the diagrams" in the chapters that follow (Brown 2011, ch. 2)"; Problem: Brown's sentence continues "in the first half of this book". The diagram chapters are 3 to 7; chapters 8 to 12 are deliverables. "the chapters that follow" overstates it. Fix: "and says it "lays a theoretical foundation from which you can build all the diagrams in the first half of this book" (Brown 2011, ch. 2)"; Basis: Brown, Communicating Design, 2nd ed., ch. 2 opening, https://www.oreilly.com/library/view/communicating-design-developing/9780131385399/ch02.html; contents at https://www.oreilly.com/library/view/communicating-design-developing/9780131385399/
18. [minor] [accuracy] 3 Fault 5; Current: "and Rosenfeld, Morville and Arango call the controlled vocabulary the "glue" between systems (2015, ch. 10)"; Problem: Same qualifier dropped as in section 1.2: the book says this of "many large metadata-driven products". Fix: "and Rosenfeld, Morville and Arango write that in many large metadata-driven products controlled vocabularies "have become the glue that holds the systems together" (2015, ch. 10)"; Basis: Rosenfeld, Morville and Arango, 4th ed., 2015, ch. 10, https://www.oreilly.com/library/view/information-architecture-4th/9781491913529/ch10.html
19. [minor] [label] 3 Reading an artefact; Current: "Five faults account for most misreadings."; Problem: "most misreadings" is a frequency claim with no source. The next sentence correctly labels the list as craft practice. Fix: "Five faults are the ones to look for first."; Basis: Sourcing standard Part 4 ("Practice is labelled as practice; measured findings are kept separate from craft advice").
20. [minor] [label] 3 Fault 4; Current: "Kaplan's definition of a user flow says "typical or ideal" (Kaplan 2023), and most flows show only that."; Problem: "most flows show only that" is an unsourced frequency claim; Kaplan's article does not say it. Fix: "Kaplan's definition of a user flow says "typical or ideal" (Kaplan 2023), and a flow drawn to that definition shows only that path."; Basis: Kaplan, "User Journeys vs. User Flows", NN/g, 16 Apr 2023, https://www.nngroup.com/articles/user-journeys-vs-user-flows/
21. [minor] [figure] 5.3 Flows paragraph (companion to the wireflow FIX); Current: "from there they can edit, which returns to New claim"; Problem: The flow's arrow label "edit" breaks the unit's own rule that a flow arrow's label is the person's action ("tap Submit"), and the Check and submit screen has no Edit control. Fix: "from there they can tap Edit, which returns to New claim"; Basis: Unit's own text, section 5.2 Labels ("An arrow's label in a flow is the person's action ("tap Submit")").
22. [minor] [figure] 5.3 Flows (wireflow); Current: the whole viz block below (it occurs once); Problem: As above: add the Edit control to Check and submit, and label the arrow "tap Edit". Fix: replace the whole block, fences included, with the block given; Basis: Unit's own text, section 5.2 Labels. Rendered without error with this folder's viz.py.

Current:
```viz
{"kind": "wireflow", "caption": "Wireflow (flows family): an employee submits a claim in the Perqo app, F2; supports the decision on which screens the task needs and where it cannot be undone (section 5.3). Perqo is fictional; wireflow form from Laubheimer, NN/g, 2016; the no-way-back label stands for Garrett's crossbar (Quick Reference).", "per_row": 4,
 "screens": [
  {"id": "list", "title": "Claims", "tone": 3, "lines": ["Submitted", {"bar": 0.8}, "Paid", {"bar": 0.6}, {"button": "New claim"}]},
  {"id": "form", "title": "New claim", "tone": 3, "lines": ["Category", {"bar": 0.7}, "Amount", {"bar": 0.4}, "Receipt", {"block": 30}, {"button": "Continue"}]},
  {"id": "review", "title": "Check and submit", "tone": 3, "lines": ["Category and amount", {"bar": 0.7}, "Balance after", {"bar": 0.5}, {"button": "Submit"}]},
  {"id": "done", "title": "Claim submitted", "tone": 3, "lines": ["Status: Submitted", "→ see claim lifecycle"]}
 ],
 "links": [
  {"from": "list", "to": "form", "label": "tap New claim"},
  {"from": "form", "to": "review", "label": "tap Continue"},
  {"from": "review", "to": "form", "label": "edit"},
  {"from": "review", "to": "done", "label": "tap Submit (no way back)"}
 ]}
```
Fix:
```viz
{"kind": "wireflow", "caption": "Wireflow (flows family): an employee submits a claim in the Perqo app, F2; supports the decision on which screens the task needs and where it cannot be undone (section 5.3). Perqo is fictional; wireflow form from Laubheimer, NN/g, 2016; the no-way-back label stands for Garrett's crossbar (Quick Reference).", "per_row": 4, "screens": [{"id": "list", "title": "Claims", "tone": 3, "lines": ["Submitted", {"bar": 0.8}, "Paid", {"bar": 0.6}, {"button": "New claim"}]}, {"id": "form", "title": "New claim", "tone": 3, "lines": ["Category", {"bar": 0.7}, "Amount", {"bar": 0.4}, "Receipt", {"block": 30}, {"button": "Continue"}]}, {"id": "review", "title": "Check and submit", "tone": 3, "lines": ["Category and amount", {"bar": 0.7}, "Balance after", {"bar": 0.5}, {"button": "Edit"}, {"button": "Submit"}]}, {"id": "done", "title": "Claim submitted", "tone": 3, "lines": ["Status: Submitted", "→ see claim lifecycle"]}], "links": [{"from": "list", "to": "form", "label": "tap New claim"}, {"from": "form", "to": "review", "label": "tap Continue"}, {"from": "review", "to": "form", "label": "tap Edit"}, {"from": "review", "to": "done", "label": "tap Submit (no way back)"}]}
```

23. [minor] [accuracy] 5.3 Lifecycles paragraph; Current: "A claim starts as Submitted, and stays there while it waits in Approvals."; Problem: Only claims over the auto-approve limit wait in Approvals; the unit's own decision tree approves the rest automatically. Fix: "A claim starts as Submitted; a claim over the auto-approve limit stays there while it waits in Approvals."; Basis: Unit's own section 5.3, Objects paragraph ("a claim at or under the limit is approved without HR, a claim over it waits in Approvals") and decision block.
24. [minor] [figure] 5.3 Lifecycles (state diagram); Current: the whole viz block below (it occurs once); Problem: The note "waits in Approvals" applies to every Submitted claim, which the decision tree contradicts. The caption says "state-transition form as in Harel 1987", but Harel's paper extends the plain form this course uses, as section 1.8 itself says. Fix: replace the whole block, fences included, with the block given; Basis: Harel 1987 abstract ("extend conventional state-transition diagrams with essentially three elements"), https://www.inf.ed.ac.uk/teaching/courses/seoc/2006_2007/resources/statecharts.pdf; unit section 1.8. Rendered without error with this folder's viz.py.

Current:
```viz
{"kind": "states", "caption": "State diagram (rules and lifecycles family): the lifecycle of a Perqo claim, F2; supports the decision on which statuses each surface shows and what moves a claim between them (section 5.3). Perqo is fictional; the four states from IA1, section 5; state-transition form as in Harel 1987.", "per_row": 3,
 "states": [
  {"id": "submitted", "label": "Submitted", "note": "waits in Approvals", "tone": 5},
  {"id": "approved", "label": "Approved", "tone": 5},
  {"id": "paid", "label": "Paid", "tone": 5, "end": true},
  {"id": "rejected", "label": "Rejected", "tone": 6, "end": true}
 ],
 "transitions": [
  {"from": "submitted", "to": "approved", "label": "approve, by rule or HR"},
  {"from": "approved", "to": "paid", "label": "pay out"},
  {"from": "submitted", "to": "rejected", "label": "reject, by rule or HR"}
 ]}
```
Fix:
```viz
{"kind": "states", "caption": "State diagram (rules and lifecycles family): the lifecycle of a Perqo claim, F2; supports the decision on which statuses each surface shows and what moves a claim between them (section 5.3). Perqo is fictional; the four states from IA1, section 5; the plain state-transition form that Harel 1987 extends.", "per_row": 3, "states": [{"id": "submitted", "label": "Submitted", "note": "[over limit] waits in Approvals", "tone": 5}, {"id": "approved", "label": "Approved", "tone": 5}, {"id": "paid", "label": "Paid", "tone": 5, "end": true}, {"id": "rejected", "label": "Rejected", "tone": 6, "end": true}], "transitions": [{"from": "submitted", "to": "approved", "label": "approve, by rule or HR"}, {"from": "approved", "to": "paid", "label": "pay out"}, {"from": "submitted", "to": "rejected", "label": "reject, by rule or HR"}]}
```

25. [minor] [deliverable] Deliverable · Notation sheet, Shapes; Current: the text below (it occurs once); Problem: The cross-surface map draws each surface as an objects box (section 1.10: "each surface is a box with its top-level areas"), but the sheet has no symbol for it. A box with a title band is otherwise "a thing the system holds". Fix: the text below; Basis: Unit's own section 1.10 and the cross-surface map block.

Current:
```
| Line after the attributes, then "-> verb" lines | objects | the actions someone can take on it |
```
Fix:
```
| Line after the attributes, then "-> verb" lines | objects | the actions someone can take on it |
| Box with a filled title band, in a surface's tone | objects | one surface in a cross-surface map; its top-level areas below the title |
```

26. [minor] [deliverable] Deliverable · Notation sheet, Shapes (companion to the section 1.7 fix); Current: "| Outlined box with branches | decision | a question the system asks (Garrett: conditional branch) |"; Problem: HR's approval in the unit's decision tree is a person's decision: Garrett's decision point, not his conditional branch. Fix: "| Outlined box with branches | decision | a question the system asks, or a decision a named person makes (Garrett: conditional branch; decision point) |"; Basis: Garrett, Quick Reference, http://www.jjg.net/ia/visvocab/files/garrett_ia_quickref.pdf
27. [minor] [deliverable] Deliverable · Notation sheet, Tones (companion to the section 5.2 tone fix); Current: "| 5 | shared: the data model, the Perqo system, any object or term on more than one surface |"; Problem: As for the section 5.2 tone rule. Fix: "| 5 | shared: the data model, the Perqo system, any object or term on more than one surface; in a figure of one surface, every box takes that surface's tone |"; Basis: Unit's own section 5.3 Structure paragraph.
28. [minor] [deliverable] Deliverable · Notation sheet, Lines (companion to the section 5.2 relationship fix); Current: "| Line without a head (objects) | relates; read its label from the first-named object to the second |"; Problem: "first-named" cannot be seen in a drawing with no arrowheads. Fix: "| Line without a head (objects) | relates; read its label from left to right on a level line, from top to bottom otherwise |"; Basis: viz.py objects().
29. [minor] [deliverable] Deliverable · Notation sheet, Labels (companion to the section 5.2 relationship fix); Current: "| Relationship label: a verb, read from first to second | how the two objects relate ("submits") |"; Problem: As above. Fix: "| Relationship label: a verb, read from left to right on a level line, from top to bottom otherwise | how the two objects relate ("submits") |"; Basis: viz.py objects().
30. [minor] [deliverable] Unsure list (companion to the decision table fix); Current: "- The "unit that builds it" column of the decision table: the course's build order was not among this unit's inputs, so it reads "set at filing"."; Problem: This line no longer holds once the codes are entered, and it misquotes the table's own placeholder ("at filing", not "set at filing"). Fix: "- The "unit that builds it" column of the decision table: codes from the course's units list (IA4 to IA8, DD-IA3); where no unit ships the artefact by name, the unit that ships its nearest form is named, with that form in brackets."; Basis: course-units.md.

## Confirmed

- Kaley, inventory and audit definitions, fields, keep/update/remove, owner per update. NN/g, 27 Sep 2020, https://www.nngroup.com/articles/content-audits/
- Laubheimer, taxonomy definition; backstage, IA structure and navigation frontstage; terms reaching users through search suggestions and facets. NN/g, 3 Jul 2022, https://www.nngroup.com/articles/taxonomy-101/
- Laubheimer, both wireflow quotations. NN/g, 4 Dec 2016, https://www.nngroup.com/articles/wireflows/
- Kaplan, user flow and user journey definitions. NN/g, 16 Apr 2023, https://www.nngroup.com/articles/user-journeys-vs-user-flows/
- Gibbons, service blueprint definition, lanes, evidence, three lines. NN/g, 27 Aug 2017, https://www.nngroup.com/articles/service-blueprints-definition/
- Cardello, first pass at the IA before choosing navigation components. NN/g, 22 Jun 2014, https://www.nngroup.com/articles/ia-vs-navigation/
- Tankala, a sitemap leaves out detail gathered in IA work. NN/g, 3 Sep 2023, https://www.nngroup.com/articles/information-architecture-sitemaps/
- Garrett, Quick Reference, ten quotations word for word; undated. http://www.jjg.net/ia/visvocab/files/garrett_ia_quickref.pdf
- Garrett, Quick Reference, elements: page, file, page stack, file stack, area, conditional, flow and iterative areas, flow reference, continuation, concurrent set, decision point, conditional branch, conditional selector, cluster, connectors, conditional connectors; none for objects, states or actors. Same URL.
- Brown 2003 interview: October 2000 release; evolved since; every Garrett quotation in sections 1.3, 2.1, 3 and 4; tool-independent. https://boxesandarrows.com/the-visual-vocabulary-three-years-later-an-interview-with-jesse-james-garrett/
- Brown, Communicating Design, 2nd ed., New Riders, 15 Sep 2010, copyright 2011. https://www.informit.com/store/communicating-design-developing-web-site-documentation-9780321712462
- Brown, chs 3 to 7: personas, concept models, site maps, flowcharts, wireframes; ch. 2 Diagram Basics. https://www.oreilly.com/library/view/communicating-design-developing/9780131385399/
- Brown, ch. 5: definition, aliases, page types or templates, purpose sentence, "one view", At-A-Glance and Purpose sections. https://www.oreilly.com/library/view/communicating-design-developing/9780131385399/ch05.html
- Brown, ch. 6: aliases, "may not reveal all the details ... comprehensive view", purpose sentences, At-A-Glance and Purpose sections. https://www.oreilly.com/library/view/communicating-design-developing/9780131385399/ch06.html
- Rosenfeld, Morville and Arango, ch. 13: "the two most common types of IA diagrams", "capturing your past decisions and guiding your future ones", "connecting and managing granular content", High-Level Architecture Sitemaps and Detailed Sitemaps headings. https://www.oreilly.com/library/view/information-architecture-4th/9781491913529/ch13.html
- Rosenfeld, Morville and Arango, ch. 8 headings: embedded (global, local, contextual) and supplemental (sitemaps, indexes, guides, configurators, search). https://www.oreilly.com/library/view/information-architecture-4th/9781491913529/
- Rosenfeld, Morville and Arango, ch. 10: synonym rings, authority files, classification schemes, thesauri; equivalence, hierarchical, associative; preferred terms. https://www.oreilly.com/library/view/information-architecture-4th/9781491913529/ch10.html
- Rosenfeld, Morville and Arango, ch. 2: "digital, physical, and cross-channel ecosystems". https://www.oreilly.com/library/view/information-architecture-4th/9781491913529/ch02.html
- Prater, "Object-Oriented UX", A List Apart, 20 Oct 2015: quotation, four steps, nesting implies contextual navigation. https://alistapart.com/article/object-oriented-ux/
- OMG, UML 2.5.1, December 2017. https://www.omg.org/spec/UML/2.5.1
- Multiplicity 1, 0..*, 1..* meaning exactly one, zero or more, at least one (secondary source, UML 2.4.1). https://uml-diagrams.org/multiplicity.html
- Harel 1987, Science of Computer Programming 8, 231 to 274; "extend conventional state-transition diagrams with essentially three elements"; hierarchy, concurrency, communication. https://www.inf.ed.ac.uk/teaching/courses/seoc/2006_2007/resources/statecharts.pdf
- Shostack, "Designing Services That Deliver", HBR, January 1984. https://hbr.org/1984/01/designing-services-that-deliver
- Kalbach, Mapping Experiences, 2nd ed., O'Reilly, November 2020, ch. 10 Service Blueprints in Part 3 Primary Diagram Types in Detail. https://www.oreilly.com/library/view/mapping-experiences-2nd/9781492076629/
- NISO Z39.19-2005 (R2010): title; lists, synonym rings, taxonomies and thesauri. https://niso.org/publications/ansiniso-z3919-2005-r2010
- Hedden, The Accidental Taxonomist, 3rd ed., Information Today, 2022. https://books.infotoday.com/Ebooks/489_The-Accidental-Taxonomist-Third-Edition.htm
- Sitemaps.org protocol page, last updated 21 Nov 2016. https://www.sitemaps.org/protocol.html
- W3C, WCAG 2.2, Recommendation 12 Dec 2024; SC 1.4.1 text. https://www.w3.org/TR/WCAG22/
- IA1 pointers: section 4 (face of a deliverable, six readers); section 2.4 (one entity, two labels); section 2.3 (Help centre split, support owns the article); section 2.2 (employee record to claims); section 5 (claim states; policy belongs to a group; budgets per group and period); Deliverable (surfaces map, areas, actions, vocabulary rows). IA1-what-information-architecture-is-and-where-it-sits.md
- Figures 5 (decision) and 7 (swimlanes): every label traced to the unit's text; kind and caption pass. unit.md, section 5.3
- All eight viz blocks parse and render with viz.py. viz.py in this folder

IA2 · fix · 3 error, 10 should-fix, 17 minor
