---
code: IA8
title: Level 4 · the system map
course: ux · IA · Information Architecture
model: Opus 5.5
written: 2026-11-09
search: off
---

# IA8 · Level 4 · the system map

IA5, IA6 and IA7 each built the IA of one Perqo surface (Perqo, fictional): perqo.com, the sales and product website; the Perqo app, the employee's client app; and Perqo Admin, the backoffice where a client company's HR and finance managers configure budgets, policies, approvals and reports. Each map is sound on its own surface, and each ends at its edges with a list of joins it could not make: an invitation sent from Admin that lands in the app, a claim whose status Admin changes and the app shows, a rule set in Admin's Policies that decides what the employee can claim. This unit joins them. It covers why a system of several surfaces, actors and lifecycles needs a map above the surface maps; the two published forms that map draws on, pervasive information architecture and the service blueprint; the lifecycles that run through Perqo; the decision trees for the rules that cut across surfaces; how the surfaces, the trees and the lifecycles are drawn as one layered map that can still be read one layer at a time; and how the map stays current. The deliverable is the Perqo interaction map: the surface layer, the actor and lifecycle layer, the decision-tree layer, the connections between them, and a reading guide of one paragraph per layer.

Every figure uses IA2's notation (IA2, section 5.2 and the notation sheet). Tone 1 is perqo.com and the buyer on it; tone 2 the merchant side and anything outside Perqo; tone 3 the Perqo app and the employee; tone 4 Perqo Admin and the HR and finance managers who use it; tone 5 shared: the data model, the Perqo system, and any object, lifecycle or rule that lives on more than one surface; tone 6 a stop, a path that ends without success. One extension is declared under IA2's rule "Keep the notation; extend the legend" (IA2, section 4): Perqo's own staff who work outside the three surfaces (sales, and the setup of a new client) take tone 5 in a lane, because they act for Perqo across surfaces and no other tone means them; the lane name says who they are.

The filed units handed this one the questions below by name; a search of the vault for "IA8" found one more, IA6's open-question cell in its A.2 table, which is the declined-attempt question again. Where each is answered:

| Handed on by | The question | Answered in |
|---|---|---|
| IA7, "What IA8 and later units take" | Admin's invitation joined to the app's entry E-2; the claim's lifecycle (IA7, Deliverable D, T5, EX-1 to EX-4) joined to the app's Claims groups and Claim screen and to IA2's decision tree; Admin's labels against the app's and perqo.com's | Deliverable, D.1 (X-04, vocabulary), D.3 (DT-2), D.4 (J-01 to J-05) |
| IA7, sections 5.1 and 6.2; register, employee status | what happens to a leaver's allocations and card; whether the model takes Admin's word, Budget; where boundaries between models run | section 3.4; Deliverable, D.1, "Two decisions on the model" |
| IA6, "What IA8 and IA11 take" | the app map and the three wireflows as the app's layer; each external route to its Help centre page; E-2 to Admin's invite, E-3 to S-6; claim states on A-3 and A-3.4 to the lifecycle and tree; the Purchase to the card payment's category rule | Deliverable, D.1 (X-03 to X-06), D.4 (J-03, J-06) |
| IA6, C.2, A.2, facts row and assumption row; register | whether a declined card attempt reaches the app, and which of IA6's places the decision changes | section 4.5 |
| IA5, "What the inventory hands on" and "What the catalogue hands on" | S-5 and S-6 as perqo.com's crossings; the external routes | Deliverable, D.1 (X-01 to X-03) |
| IA4, section 4.3 and "What the map hands on" | the claim's status attribute joined to its state diagram and decision tree; the policy's auto-approve limit joined to the rule that reads it | Deliverable, D.4 (J-01, J-02) |
| IA2, decision table rows marked IA8; section 5.3 | the decision tree, the service blueprint as lifecycle swimlanes, the cross-surface interaction map, extending IA2's figures | sections 3 and 4; Deliverable |
| IA1, surfaces map and "what crosses between surfaces" | the surfaces and their crossings | Deliverable, D.1 |
| Register, "Not yet set" | the client company's purchase lifecycle; the employee's enrolment beyond IA6's invitation and Join and IA7's Invited state | sections 3.2 and 3.3 |
| The brief's Takes line and closing words | IA5 to IA7's IAs and IA2's blueprint and map entries, with Perqo facts consistent with IA4 to IA7 | throughout; "Perqo facts set by this unit" |

## 1 · Why a system needs a map above the surface maps

A sitemap, an app map and a navigation model each answer for one surface. IA2 gave the cross-surface interaction map its own question: across all the surfaces, which things are shared, what does each surface call them, and what passes between them (IA2, section 1.10). Its ground is the widening the fourth edition of the Polar Bear book wrote into its definition of IA, "digital, physical, and cross-channel ecosystems" (Rosenfeld, Morville and Arango, *Information Architecture: For the Web and Beyond*, 4th ed., O'Reilly, 2015, ch. 2; IA1, section 1.1). At Perqo (Perqo, fictional), the three surface maps hold 104 identified rows, pages and screens between them (IA5's 52 inventory rows after the redesign, IA6's 23 screen IDs, IA7's 29 page IDs), and every one of the hard questions the filed units passed on sits on a line between two of them. A map above them serves three purposes, each with a different reader.

**Shared understanding.** Sarah Gibbons's NN/g definition of the service blueprint, the nearest published artefact, says it "bridges crossdepartment efforts", showing overlaps and dependencies that departments working alone miss ("Service Blueprints: Definition", Nielsen Norman Group, 27 August 2017, [nngroup.com, blueprint definition](https://www.nngroup.com/articles/service-blueprints-definition/); NN/g guidance). James Kalbach's *Mapping Experiences* (2nd ed., O'Reilly, 2020) is built on the same purpose: its publisher's description says it shows how to "use alignment diagrams to turn valuable customer observations into actionable insight" ([oreilly.com, Mapping Experiences](https://www.oreilly.com/library/view/mapping-experiences-2nd/9781492076629/)). At Perqo the six touchpoints of the course goal each own a piece of one journey: sales the demo, support the Help centre, engineering the rules, product management the surfaces, content the labels, the client its own HR and finance staff. The map is the one artefact all six read (IA2, section 1.10).

**Gap-finding.** Gibbons calls blueprints "treasure maps that help businesses discover weaknesses", especially root causes that sit inside the organisation (Gibbons 2017). The mechanism is simple: a gap is a place where one surface's map ends with an arrow and the next surface's map has nothing for it to land on. Drawing the Perqo map for this unit found seven such places, listed below; two were already named as open questions by the filed units (G-1 by IA7, G-2 by IA6), and five were found only when the layers were laid together.

**Scope decisions.** IA1 named the decision its surfaces map supported: on which surface, and under which name, a new piece of content or function belongs (IA1, Deliverable). With the lifecycles and rules on the same map, product management can also see which surfaces, stages and rules a change touches before it is estimated. The declined-attempt notice decided in section 4.5 touches one rule, two surfaces, one object and one lifecycle stage, and the map shows all of them on one sheet.

The gaps the Perqo map found (Perqo, fictional), each with where it is decided. A figure would give each row tone 6, a stop: each is a path that ends without success until it is decided.

| ID | Gap | Found between | Decided in |
|---|---|---|---|
| G-1 | A leaver's remaining allocations and card have no rule | IA7's employee lifecycle (Left) and the app's Card and balances | section 3.4 |
| G-2 | A declined card attempt reaches nobody: the app shows nothing, Admin shows card status only | the till (merchant side) and the app (IA6, C.2) | section 4.5 |
| G-3 | HR can invite an employee into a group whose budgets for the period are not set; the employee joins to an app with nothing to spend | Admin's Invite employees (AD-1.3) and the app's Home (A-1) | section 3.2 |
| G-4 | A client whose contract ends has no defined end: admin users, employees and cards carry on | the purchase lifecycle and every surface | section 3.2 |
| G-5 | A leaver's claim decided after they leave sends a notification to an app they can no longer sign in to | IA7's EX-4 and the app's notification (E-4) | left free, named for IA11 (section 3.4) |
| G-6 | An employee moved to another group mid-period: which allocations they keep | IA7's move to group and IA4's allocation per category and period | left free (section 3.3) |
| G-7 | What happens to money unspent at a period's end | the allocation's period and the employee's Review stage | left free (section 3.3) |

## 2 · Two published forms the map draws on

### 2.1 · Pervasive and cross-channel information architecture

Andrea Resmini and Luca Rosati's *Pervasive Information Architecture: Designing Cross-Channel User Experiences* (Morgan Kaufmann, 2011) is the field's standard work on IA that spans channels. Its Part 2 is five heuristics, one chapter each after an introductory one: ch. 3, "Heuristics for a Pervasive Information Architecture"; ch. 4, "Place-making"; ch. 5, "Consistency"; ch. 6, "Resilience"; ch. 7, "Reduction"; ch. 8, "Correlation"; Part 3 applies them in ch. 9, "Designing Cross-channel User Experiences" (contents at [shop.elsevier.com, Pervasive IA](https://shop.elsevier.com/books/pervasive-information-architecture/resmini/978-0-12-382094-5)). The book's chapters were not read for this unit, as they were not for IA6 (IA6, section 6.1), so only one heuristic's definition is given here, through a later paper that quotes it. Jon Fisher, Simon Norris and Elizabeth Buie quote Resmini and Rosati: "Correlation relates to the capability of pervasive information architecture to convey pieces of information", "services and goods to help users achieve explicit goals or stimulate latent needs", and they report the book's split into internal correlation, "the semantic proximity of items within the same channel", and external correlation, "the semantic proximity between items belonging to different channels but connected to the same task, process or people" ("Sense-making in Cross-channel Design", *Journal of Information Architecture* 4, no. 2, 2012, pp. 5 to 30, [journalofia.org, cross-channel sense-making](https://journalofia.org/volume4/issue2/02-fisher/jofia-0402-02-fisher.pdf); peer-reviewed).

External correlation is the property a cross-surface map draws: two items on different surfaces, joined because one task, process or person connects them. This unit uses the five chapter names as five questions to put to each crossing on the map. The questions are this unit's, built from the names and from what the filed units already did under them, and are offered as practice:

- **Place-making:** does a person crossing know where they have arrived? (IA7's line on Admin's sign-in screen for an employee who arrives there by mistake answers it for X-02.)
- **Consistency:** does the thing keep its meaning, and is a change of label written down? (IA1's rule, IA6, section 6.1.)
- **Resilience:** does the crossing still work when one side is missing, such as the app not installed? (IA6's fallback of every app address to S-6.)
- **Reduction:** does the crossing carry only what the next surface needs? (IA7's Perqo card, status only.)
- **Correlation:** is each item linked to the items on other surfaces that the same task needs? (The external routes from app screens to Help centre articles.)

What pervasive IA gives the map: its unit of analysis is the ecosystem, and its correlation heuristic names the line between surfaces as a design object in itself. What it does not give: a diagram form. Neither the contents nor the quoted definition prescribes how to draw the ecosystem.

### 2.2 · The service blueprint

G. Lynn Shostack's "Designing Services That Deliver" (*Harvard Business Review*, January 1984, [hbr.org, Shostack 1984](https://hbr.org/1984/01/designing-services-that-deliver)) is the article the technique is traced to (IA2, section 1.9); the article's text was not read for this unit, and nothing is quoted from it. Mary Jo Bitner, Amy Ostrom and Felicia Morgan's later account in a management journal describes it as a technique that "is securely grounded in the customer's experience" and "allows the clear visualization of dynamic service processes" ("Service Blueprinting: A Practical Technique for Service Innovation", *California Management Review* 50, no. 3, 2008, [cmr.berkeley.edu, service blueprinting](https://cmr.berkeley.edu/2008/05/50-3-service-blueprinting-a-practical-technique-for-service-innovation/)).

NN/g gives the form most product teams use. Gibbons defines it: "A service blueprint is a diagram that visualizes the relationships between different service components", "directly tied to touchpoints in a specific customer journey"; its clusters are customer actions, frontstage actions, backstage actions and processes, with evidence as a further layer, separated by the line of interaction, the line of visibility and the line of internal interaction (Gibbons 2017; IA2, section 1.9). Her comparison of mapping methods places it after the journey map: "Think of service blueprints as a part two to customer journey maps", and "Blueprinting is an ideal approach to experiences that are omnichannel, involve multiple touchpoints" ("UX Mapping Methods Compared: A Cheat Sheet", Nielsen Norman Group, 5 November 2017, [nngroup.com, mapping cheat sheet](https://www.nngroup.com/articles/ux-mapping-cheat-sheet/)). Her five steps end on refining and distributing the blueprint, adding detail such as time and metrics, so that it can be shared ("The 5 Steps to Service Blueprinting", Nielsen Norman Group, 4 February 2018, [nngroup.com, five steps](https://www.nngroup.com/articles/5-steps-service-blueprinting/)). Kalbach gives the service blueprint the first chapter of his part on primary diagram types, before customer journey maps, experience maps, mental model diagrams and ecosystem models (Kalbach 2020, Part 3, chs 10 to 14, contents). All of this is NN/g guidance and a standard work's practice; none of it is a measured comparison of blueprints with other maps.

What the blueprint gives the map: lanes for actors, steps in time order, and the line of visibility as a place where a status must mean the same on both sides (IA2, section 1.9). What it does not give: the structure of each surface. A blueprint follows one journey; it does not say what Admin's six areas hold.

### 2.3 · What the map takes from each

The cross-surface interaction map is the course's own artefact; no standard work defines it under that name (IA2, section 1.10). From pervasive IA it takes the ecosystem as the unit and the crossing as a designed thing with five questions to ask of it. From the blueprint it takes lanes, time order and the line of visibility, and IA2 already assigned the blueprint to this unit "as lifecycle swimlanes" (IA2, Deliverable, decision table). From the surface units it takes the top level of each surface and every identifier, and from IA2 the decision tree and the state diagram. Section 5 says how they are stacked.

## 3 · The lifecycles that run through Perqo

A lifecycle is the course of one thing or one relationship through stages. IA2 separated the state diagram (where a thing is over time) from the flow (what a person does) (IA2, section 1.8). The system map needs both scales: two long lifecycles that run across months and surfaces, the client company's and the employee's, and the short object lifecycles that IA2 and IA7 drew (the claim, the employee's status), which sit inside them.

### 3.1 · The published models of the purchase decision, and their evidence

Three published models describe how an organisation or a person comes to buy. Each is named here with what stands behind it.

- **The hierarchy of effects.** Robert Lavidge and Gary Steiner's "A Model for Predictive Measurements of Advertising Effectiveness" (*Journal of Marketing*, 1961) proposed that a buyer moves through ordered steps from awareness to purchase. On this unit's knowledge it is a conceptual model offered to organise advertising measurement, not a study. The article was not read for this unit; its title, journal and year are given, and its description here is on the unsure list.
- **The consumer decision journey.** David Court, Dave Elzinga, Susan Mulder and Ole Jørgen Vetvik of McKinsey replaced the funnel with a loop of four phases: "initial consideration"; "active evaluation, or the process of researching potential purchases"; "closure, when consumers buy brands"; and "postpurchase, when consumers experience them". They write that "The funnel metaphor does help a good deal", and argue that it misses how consumers now decide ("The consumer decision journey", *McKinsey Quarterly*, 2009, no. 3, [mckinsey.com, decision journey](https://www.mckinsey.com/~/media/McKinsey/Business%20Functions/Marketing%20and%20Sales/Our%20Insights/The%20consumer%20decision%20journey/The%20consumer%20decision%20journey.pdf)). The evidence is a consultancy's study of the decisions of "almost 20,000 consumers across five industries and three continents" (automobiles, skin care, insurance, consumer electronics, mobile telecom), published in the firm's own journal and not peer-reviewed. It is about consumers, not companies buying software.
- **The B2B buying jobs.** Gartner names six "buying jobs" in a business purchase, "Problem Identification", "Solution Exploration", "Requirements Building", "Supplier Selection", "Validation" and "Consensus Creation", and describes a journey "that resembles more of a maze than a linear path" ("Gartner Says the Marketing-to-Sales Handoff Should No Longer Exist", press release, 9 October 2018, [gartner.com, buying jobs](https://www.gartner.com/en/newsroom/press-releases/2018-10-09-gartner-says-the-marketing-to-sales-handoff-should-no-longer-exist)). This is an analyst firm's press release; the page gives no survey figures and no method, so it is vendor material, not evidence that buyers behave this way.

What they share is the claim that a purchase is a sequence of stages with distinct information needs, and the later two add that the sequence loops and repeats. None of them was tested on a benefits platform, and none says how a vendor's surfaces should be arranged. The stages the brief names for a client company (evaluate, trial, contract, onboard, run, renew or churn) cover what Court and colleagues call closure and postpurchase in more detail, because that is where a software vendor's own surfaces carry the relationship. This unit uses the brief's stages and labels the published models as background.

### 3.2 · The client company's purchase lifecycle

The register left the purchase lifecycle of a client company free (register, "Not yet set"). This unit sets it (Perqo, fictional), keeping IA5's facts that Perqo has no self-serve sign-up and no free trial and that a client starts after a contract (IA5, section 5.5), and IA7's that Perqo sets up the client's first admin user as account owner (IA7, section 3.4).

| ID | Stage | Who | Where | What crosses to the next stage |
|---|---|---|---|---|
| CL-1 | Evaluate | a buyer at a prospective client | perqo.com: Product, Benefits, Pricing, Customers (S-1 to S-3) | interest; a demo request |
| CL-2 | Trial | the buyer and Perqo's sales team | perqo.com: Book a demo (S-4); the demo itself and sales' follow-up are outside the surfaces (IA4, A.3: demo request -> follow up) | Perqo has no free trial; the demo is this stage's form at Perqo |
| CL-3 | Contract | the client and Perqo's sales team | outside the surfaces | a signed contract; Perqo sets up the client (O-01) with its contract start and end dates and its first admin user as account owner |
| CL-4 | Onboard | the account owner, HR and finance | Perqo Admin | admin users, employee groups, policies, budgets, invitations, in the order below |
| CL-5 | Run | HR, finance, employees | Admin and the app, each period | budgets, claims, card payments, reports |
| CL-6 | Renew or churn | the client and Perqo's sales team | outside the surfaces; Admin's Company page | a new contract end date, or the client's end |

Three facts are new here (Perqo, fictional). The client gains a **contract end date**, beside IA4's contract start date, shown read only on Company (AD-6.1) to every admin user. A renewal sets a new end date. At **churn**, the day after the contract end date, no admin user and no employee of that client can sign in, and every card of the client is cancelled; the client's records are kept, for a period left free. On perqo.com, a customer story about a former client is removed with a redirect to Customers, as IA5's audit did for S-3.4 (IA5, Deliverable A).

Onboarding has an order, and drawing the lifecycle across lanes found G-3: IA7's Invite employees has no condition, so HR could invite an employee into a group whose budgets are not set, and the employee would join to a Home with nothing to spend. The decision (Perqo, fictional): **invite is unavailable for an employee group until its budgets for the current period are set**, shown disabled with the reason "Set this group's budgets first", which is IA7's rule for an action a role holds but cannot take now (IA7, section 3.2). It adds a condition to IA7's employee -> invite and employee group -> invite employees and removes nothing. The onboarding order: (1) Perqo sets up the client and its account owner; (2) the account owner adds admin users, at least two with the HR manager role (IA7, section 3.3); (3) HR creates employee groups and their policies; (4) finance sets budgets for the current period; (5) HR invites; (6) employees join.

The lifecycle as swimlanes, IA2's blueprint form taken across months (IA2, Deliverable, decision table). Lanes are actors on surfaces: the buyer on perqo.com (tone 1), Perqo's sales and setup staff outside the surfaces (tone 5, the extension declared above), the client's admin users in Admin (tone 4) and employees in the app (tone 3). Churn, and the removal of the client's customer story that follows it, are tone 6, a path that ends without success.

```viz
{"kind": "swimlanes", "caption": "Lifecycle swimlanes: the purchase lifecycle of a Perqo client company, CL-1 to CL-6, across perqo.com, Perqo's own staff, Perqo Admin and the Perqo app; supports the decision on which surface carries each stage and where the client's relationship crosses between them (section 3.2). Tone 1 perqo.com and the buyer; tone 5 Perqo's sales and setup staff working outside the surfaces (this unit's declared extension); tone 4 Perqo Admin; tone 3 the app; tone 6 a path that ends without success. Lanes and time order from the service blueprint (Gibbons, 'Service Blueprints: Definition', NN/g, 2017; IA2, section 1.9); stages from this unit's brief, with the published purchase models of section 3.1 as background; no free trial and the contract start from IA5, section 5.5; the account owner from IA7, section 3.4; the onboarding order, the contract end date and churn set in section 3.2. Perqo is fictional.",
 "lanes": [
  {"id": "site", "label": "Buyer on perqo.com", "tone": 1},
  {"id": "staff", "label": "Perqo staff: sales and setup", "tone": 5},
  {"id": "admin", "label": "Client's admin users in Perqo Admin", "tone": 4},
  {"id": "app", "label": "Employees in the Perqo app", "tone": 3}],
 "steps": [
  {"id": "eval", "lane": "site", "col": 0, "label": "CL-1 Evaluate", "note": "S-1 to S-3", "tone": 1},
  {"id": "demo", "lane": "site", "col": 1, "label": "CL-2 Trial: Book a demo", "note": "S-4; no free trial", "tone": 1},
  {"id": "follow", "lane": "staff", "col": 2, "label": "Demo and follow-up", "note": "outside the surfaces", "tone": 5},
  {"id": "contract", "lane": "staff", "col": 3, "label": "CL-3 Contract", "note": "client and account owner set up", "tone": 5},
  {"id": "onboard", "lane": "admin", "col": 4, "label": "CL-4 Onboard", "note": "admins, groups, policies, budgets, then invites", "tone": 4},
  {"id": "join", "lane": "app", "col": 5, "label": "Employees join", "note": "→ see EL-1", "tone": 3},
  {"id": "run", "lane": "admin", "col": 6, "label": "CL-5 Run", "note": "each period: budgets, approvals, reports", "tone": 4},
  {"id": "renew", "lane": "staff", "col": 7, "label": "CL-6 Renew", "note": "new contract end date", "tone": 5},
  {"id": "churn", "lane": "admin", "col": 8, "label": "CL-6 Churn", "note": "[after the contract end date] sign-in ends, cards cancelled", "tone": 6},
  {"id": "story", "lane": "site", "col": 9, "label": "Customer story removed", "note": "redirect to S-3", "tone": 6}],
 "links": [
  {"from": "eval", "to": "demo"},
  {"from": "demo", "to": "follow", "label": "demo request"},
  {"from": "follow", "to": "contract"},
  {"from": "contract", "to": "onboard", "label": "first admin user"},
  {"from": "onboard", "to": "join", "label": "invitations"},
  {"from": "join", "to": "run"},
  {"from": "run", "to": "renew", "label": "[renewed]"},
  {"from": "renew", "to": "run"},
  {"from": "run", "to": "churn", "label": "[not renewed]"},
  {"from": "churn", "to": "story"}]}
```

### 3.3 · The employee's benefit lifecycle

The employee's lifecycle runs inside the client's Run stage (CL-5), once per employee, and repeats each period (Perqo, fictional). Its six stages, with where each happens and what the filed units already set for it:

| ID | Stage | Where | What happens |
|---|---|---|---|
| EL-1 | Enrol | Admin (AD-1.3), email, the app (A-0.1) or S-6 | HR invites; the invitation (E-2) opens Join; the employee becomes Active (IA6, B.4; IA7, section 5.1); Perqo orders the card |
| EL-2 | Learn | the app (A-1, A-2.1 to A-2.4); the Help centre (What you can claim in each category, H-2.1.3; H-2.2.1) | balances per category, What's covered, the claim rule |
| EL-3 | Decide | the app (A-2.x, A-4.3) | pay with the card at a merchant, or pay another way and claim; Card offers |
| EL-4 | Spend | the merchant's till; the app (A-4.2.1) | a card payment, or a decline (section 4.4) |
| EL-5 | Claim | the app (A-3.1 to A-3.4); Admin (AD-4) | a claim, decided by the rule or by HR (section 4.3) |
| EL-6 | Review | the app (A-3, A-4.2, A-5.2) | Purchases, Claims and notifications; the next period's balances |

Enrolment beyond IA6's invitation and Join and IA7's Invited state is set here (Perqo, fictional): Perqo orders the employee's card when the employee becomes Active, and the app's Card tab shows IA6's state "Your Perqo card has not been issued yet" until Perqo issues it (IA6, section 4.4); how long issuing takes is left free. After Join, the employee lands on Home (A-1), whose balances exist because of the onboarding order in section 3.2. Two questions the lifecycle raises are left free and named: which allocations an employee keeps when HR moves them to another group in the middle of a period (G-6), and what happens to money unspent at a period's end (G-7). The figure draws one period: the stages left to right, each in the lane of the actor and surface where it happens, with the Help centre (tone 1), the merchant (tone 2), the Perqo system and the rules it applies (tone 5) and HR and finance in Admin (tone 4) beside the employee in the app (tone 3). The figure draws the decline and the Purchase as one step in the app, because both end in the app; the declines themselves are in DT-3 (section 4.4).

```viz
{"kind": "swimlanes", "caption": "Lifecycle swimlanes: one period of a Perqo employee's benefit lifecycle, EL-1 to EL-6, across the app, the Help centre, the merchant's till, the Perqo system and Perqo Admin; supports the decision on which surface and which rule each stage depends on (section 3.3). Tone 3 the app and the employee; tone 1 perqo.com's Help centre; tone 2 the merchant side; tone 5 the Perqo system; tone 4 Perqo Admin. Lanes from the service blueprint (Gibbons, NN/g, 2017; IA2, section 1.9); the invitation and Join from IA6, B.4 and IA7, section 5.1 and C.4; screens from IA6, Deliverable B; the rules from section 4 (DT-1 to DT-3); the card ordered on joining and the decline notice set in sections 3.3 and 4.5. Perqo is fictional.",
 "lanes": [
  {"id": "admin", "label": "HR and finance in Perqo Admin", "tone": 4},
  {"id": "app", "label": "Employee in the Perqo app", "tone": 3},
  {"id": "help", "label": "Help centre on perqo.com", "tone": 1},
  {"id": "till", "label": "Merchant at the till", "tone": 2},
  {"id": "sys", "label": "Perqo system", "tone": 5}],
 "steps": [
  {"id": "invite", "lane": "admin", "col": 0, "label": "HR invites", "note": "AD-1.3 [budgets set]", "tone": 4},
  {"id": "join", "lane": "app", "col": 1, "label": "EL-1 Enrol: Join", "note": "A-0.1; Active; card ordered", "tone": 3},
  {"id": "learn", "lane": "app", "col": 2, "label": "EL-2 Learn", "note": "A-1, A-2.1 to A-2.4", "tone": 3},
  {"id": "help", "lane": "help", "col": 3, "label": "What you can claim in each category", "note": "H-2.1.3", "tone": 1},
  {"id": "decide", "lane": "app", "col": 4, "label": "EL-3 Decide", "note": "card or claim; Card offers A-4.3", "tone": 3},
  {"id": "pay", "lane": "till", "col": 5, "label": "EL-4 Spend: pay", "note": "Perqo card", "tone": 2},
  {"id": "dt3", "lane": "sys", "col": 6, "label": "DT-3 spend limits", "tone": 5},
  {"id": "purchase", "lane": "app", "col": 7, "label": "Purchase, or decline notice", "note": "A-4.2.1; A-5.2", "tone": 3},
  {"id": "claim", "lane": "app", "col": 8, "label": "EL-5 Claim", "note": "A-3.1 to A-3.4", "tone": 3},
  {"id": "dt2", "lane": "sys", "col": 9, "label": "DT-2 approval routing", "tone": 5},
  {"id": "hr", "lane": "admin", "col": 10, "label": "HR decides", "note": "AD-4 [over the limit]", "tone": 4},
  {"id": "review", "lane": "app", "col": 11, "label": "EL-6 Review", "note": "A-3, A-4.2, A-5.2", "tone": 3},
  {"id": "budget", "lane": "admin", "col": 12, "label": "Finance sets next period", "note": "AD-2.2", "tone": 4}],
 "links": [
  {"from": "invite", "to": "join", "label": "invitation, E-2"},
  {"from": "join", "to": "learn"},
  {"from": "learn", "to": "help", "label": "external route"},
  {"from": "help", "to": "decide"},
  {"from": "decide", "to": "pay"},
  {"from": "pay", "to": "dt3"},
  {"from": "dt3", "to": "purchase"},
  {"from": "purchase", "to": "claim"},
  {"from": "claim", "to": "dt2", "label": "Submit"},
  {"from": "dt2", "to": "hr", "label": "[over the limit]"},
  {"from": "hr", "to": "review", "label": "notification, E-4"},
  {"from": "review", "to": "budget"}]}
```

### 3.4 · The object lifecycles inside them, and the leaver

Inside the two long lifecycles run the short ones the filed units drew: the claim's (Submitted, Approved, Rejected, Paid; IA2, section 5.3; IA7, Deliverable D, T1 to T6) and the employee's status (Invited, Active, Left; IA7, section 5.1). The card has the states Active and Frozen (IA4, A.1), and Admin shows Not issued when the employee holds none (IA7, section 2.3). Where the long and short lifecycles meet is where the leaver question sits.

IA7 left it open: when HR marks an employee as left, what happens to their remaining allocations and their card (IA7, section 5.1; register, employee status). The decision (Perqo, fictional), each part with its reason:

- **The Perqo card is cancelled at once.** A card left Active would let a leaver spend the client's money; a Frozen one could be unfrozen by its holder (IA4, A.3). Cancelled is a new card status, an extension of IA4's Active and Frozen that removes neither; Admin shows it on the employee's record beside Active, Frozen and Not issued (IA7, section 2.3). A cancelled card is declined at the till (section 4.4). An employee who leaves from Invited has no card, because Perqo orders it on joining (section 3.3).
- **The allocations are closed to new spending.** No card payment can spend from them (the card is cancelled) and no claim can be submitted (the leaver cannot sign in: IA7, section 5.1). Closed is a new allocation attribute, yes or no, set when its employee is Left.
- **Claims submitted before leaving are still decided** (IA7, EX-4), against the closed allocations, by the same rule and the same balance check (T3, T5); an approved claim is paid. That keeps IA7's exception and adds no state to the claim.
- **What remains is reported as unspent.** Finance sees it in Reports, Budget use (AD-5.3), and nothing is paid to the leaver beyond approved claims. Whether the client's contract treats unspent money otherwise is left free, with G-7.

The same rules apply to every employee at churn (section 3.2). One gap stays open and is named for IA11: a leaver whose claim is decided after leaving gets a notification in an app they can no longer open (G-5). Whether Perqo should email the decision, and to which address once the work email has gone, needs evidence about leavers that no filed unit has.

## 4 · Decision trees for the rules that cut across surfaces

### 4.1 · Drawing a tree that engineering can build and sales can explain

IA2 defined the decision tree as Garrett's conditional branch drawn out in full, "when the system (not based on user action) must select one path", with every question the system asks in order and every outcome (IA2, section 1.7; Garrett, *Visual Vocabulary Quick Reference*). A rule earns a tree on the system map when it is set on one surface and felt on another. Perqo has three: eligibility (who may spend from which category, set in Admin, felt in the app and at the till), approval routing (which claims wait for HR, set in Admin's policy, felt in the app's Claims), and spend limits (whether a card payment is taken, set by finance's budgets, felt at the till).

The two readers want different things from the same rule. Engineering needs every combination of inputs to land on exactly one outcome. The Object Management Group's Decision Model and Notation standard is built for that pairing of readers: its stated goal is "a common notation that is readily understandable by all business users", "from the business analysts needing to create initial decision requirements and then more detailed decision models", "to the technical developers responsible for automating the decisions in processes", and "finally, to the businesspeople who will manage and monitor those decisions" (OMG, *Decision Model and Notation*, version 1.5, August 2024, [omg.org, DMN 1.5](https://www.omg.org/spec/DMN/1.5/About-DMN); standards documentation). DMN's decision tables carry a hit policy; in one vendor's documentation of the standard, "A decision table has a hit policy that specifies what the results of the evaluation of a decision table consist of", and under the Unique policy "Only a single rule can be satisfied or no rule at all" (Camunda, "Hit policy", undated, [docs.camunda.io, hit policy](https://docs.camunda.io/docs/components/modeler/dmn/decision-table-hit-policy/); vendor documentation).

So each Perqo rule is drawn twice, from one source, and the course's practice for it has six parts, each tied to what it protects:

1. **Ask questions with two answers**, in IA2's order, "yes" on the left (IA2, section 5.2). Protects: engineering, who can read each question as one condition.
2. **Order the questions so that the cheapest stop comes first**, and say why in the caption. Protects: support, who can say at which question a case stopped.
3. **Name each outcome as the surface names it** ("Rejected, over the balance", the app's reason; IA6, Deliverable B), with the transition or the reason code beside it. Protects: content and support, who must find the same words on the screen; and engineering, who maps the outcome to a status (IA2, section 1.7: at F3 "every outcome is named as the screen names it").
4. **Give a person's decision its own box in the person's tone**, so a reader sees where the system waits (IA2, section 1.7). Protects: the client, whose staff are that box.
5. **Write the same rule as a table**, one row per path, with the Unique hit policy: every combination of answers matches exactly one row. Protects: engineering and test, who can check the table is complete; a tree hides a missing branch less well than a table hides a missing row.
6. **Give sales the tree's first line in words**, for example "A claim at or under your limit is approved at once; over it, one of your HR managers decides, never the claimant". Protects: sales, who explain the rule to a buyer, and the Help centre article that carries it (H-1.2.5).

Brown's account of flowcharts as the visualisation of "a process, usually centered around a specific task or function" (Brown, *Communicating Design*, 2nd ed., 2011, ch. 6; IA2, section 2.2) covers the tree's reading order; the table form is DMN's. The rest of the list is this course's practice, and no study is known to this unit that compares how well engineers and salespeople read trees against tables.

### 4.2 · Eligibility: who may spend from which category

The eligibility rule decides whether an employee may spend from a category at all (Perqo, fictional). It reads four things set on three surfaces: the client's contract (CL-3, CL-6), the employee's status (IA7, section 5.1), the policy's open categories (IA4, A.1) and the allocation for the current period (IA4, A.1). The questions run from the widest stop to the narrowest. A client after its contract end date stops everything; an employee who is Invited must join first and one who is Left cannot sign in (section 3.4); a category closed to the group is not shown in the app, nor any cross-listing or offer of it (IA6, section 4.4), and a card payment there is declined (section 4.4); a category open but with no allocation for the period shows its screen with the line "Your budget for this period is not set yet", a new state of IA6's category screen, and the employee can neither pay nor claim there until finance sets it (IA7's No budget for next period queue exists to prevent it). The system's questions and the eligible outcome are tone 5; the stops are tone 6.

```viz
{"kind": "decision", "caption": "Decision tree DT-1, eligibility: whether a Perqo employee may spend from a category, F3, every outcome named as the surface shows it; supports the decision on what the app shows and what the till accepts for each employee and category (section 4.2). Tone 5 the Perqo system's questions and the eligible outcome; tone 6 a stop. Questions ordered widest stop first (section 4.1). Contract end date and churn from section 3.2; employee status from IA7, section 5.1; open categories from IA4, A.1 and IA6, section 4.4; allocation per category and period from IA4, A.1; the 'not set yet' state set in section 4.2. Decision tree as Garrett's conditional branch drawn out (IA2, section 1.7). Perqo is fictional.",
 "root": {"q": "Client's contract in force?", "tone": 5, "branches": [
  {"label": "yes", "to": {"q": "Employee Active?", "tone": 5, "branches": [
   {"label": "yes", "to": {"q": "Category open in the group's policy?", "tone": 5, "branches": [
    {"label": "yes", "to": {"q": "Allocation set for this period?", "tone": 5, "branches": [
     {"label": "yes", "to": {"outcome": "Eligible: card and claims in this category", "tone": 5}},
     {"label": "no", "to": {"outcome": "Shown: budget for this period not set yet", "tone": 6}}]}},
    {"label": "no", "to": {"outcome": "Category not shown; card declined there", "tone": 6}}]}},
   {"label": "no", "to": {"outcome": "Invited: join first. Left: cannot sign in", "tone": 6}}]}},
  {"label": "no", "to": {"outcome": "Sign-in ended; cards cancelled", "tone": 6}}]}}
```

### 4.3 · Approval routing: which claims wait for HR

IA2 drew the rule on submission; IA7 took the claim's lifecycle to F3 and added the HR manager's own claim (EX-1) and the second balance check on approval (T5) (IA2, section 5.3; IA7, Deliverable D). The tree below extends IA2's figure with both and changes none of its questions or outcomes (Perqo, fictional). The amount is checked against the chosen category's balance (IA3, section 2.3), then against the policy's auto-approve limit (IA4, A.1), whose amount stays free. A claim over the limit waits in Approvals, where an HR manager other than the claimant decides (EX-1); if they approve, the system checks the balance again, because a waiting claim reserves nothing (IA7, EX-2), and a claim now over the balance is rejected (T5). A claim waiting more than five working days is marked Overdue in Approvals, which is a display rule and no branch (IA7, EX-3). Each outcome carries its transition from IA7, D.1. The system's questions and the approvals are tone 5, HR's question tone 4, the rejections tone 6.

```viz
{"kind": "decision", "caption": "Decision tree DT-2, approval routing: how the Perqo system routes a submitted claim, F3, each outcome with its transition (T1 to T5) and the app's reason; supports the decision on which claims need HR and why a claim ended as it did (section 4.3). Extends IA2, section 5.3's tree with IA7, Deliverable D's EX-1 (the claimant is never the decider) and T5 (the balance checked again on approval). Tone 5 the Perqo system and the approvals; tone 4 HR in Perqo Admin; tone 6 a stop. The category's balance from IA3, section 2.3; the auto-approve limit from IA4, A.1; reasons from IA6, Deliverable B. Perqo is fictional.",
 "root": {"q": "Amount within the category's balance?", "tone": 5, "branches": [
  {"label": "yes", "to": {"q": "At or under the policy's auto-approve limit?", "tone": 5, "branches": [
   {"label": "yes", "to": {"outcome": "Approved automatically (T2)", "tone": 5}},
   {"label": "no", "to": {"q": "Waits in Approvals: an HR manager, never the claimant, approves?", "tone": 4, "branches": [
    {"label": "yes", "to": {"q": "Still within the category's balance?", "tone": 5, "branches": [
     {"label": "yes", "to": {"outcome": "Approved (T3)", "tone": 5}},
     {"label": "no", "to": {"outcome": "Rejected, over the balance (T5)", "tone": 6}}]}},
    {"label": "no", "to": {"outcome": "Rejected by HR, with a note (T4)", "tone": 6}}]}}]}},
  {"label": "no", "to": {"outcome": "Rejected, over the balance (T1)", "tone": 6}}]}}
```

### 4.4 · Spend limits: whether a card payment is taken

A card payment at a merchant spends from the allocation of that merchant's category (IA4, Deliverable A), and IA6 set two reasons for a decline at the till: over that category's balance, or the card Frozen (IA6, C.2). This unit adds the two reasons the system map makes necessary (Perqo, fictional): the card Cancelled (a leaver or a churned client, sections 3.2 and 3.4), and the merchant's category not open to the employee's group, where no allocation exists to spend from (DT-1). Each merchant is assigned one narrower term by Perqo (IA4, A.1), so the category is known at the till. The questions run from the card, which the till reads first, to the amount. A taken payment becomes a card payment, which the app shows as a Purchase with the category's balance after (IA6, B.3); every decline triggers the notice decided in section 4.5, except on a Cancelled card, whose holder can no longer sign in. Tones as before: the system 5, the stops 6.

```viz
{"kind": "decision", "caption": "Decision tree DT-3, spend limits: whether a Perqo card payment is taken at the till, F3, every outcome named as the app shows it; supports the decision on what the till accepts and what the employee is told (section 4.4). Tone 5 the Perqo system's questions and the taken payment; tone 6 a stop. The category rule from IA4, Deliverable A; the over-balance and Frozen declines from IA6, Deliverable C, C.2; Cancelled and the closed category added in section 4.4; the decline notice from section 4.5. Perqo is fictional.",
 "root": {"q": "Card Active?", "tone": 5, "branches": [
  {"label": "yes", "to": {"q": "Merchant's category open to the employee's group?", "tone": 5, "branches": [
   {"label": "yes", "to": {"q": "Amount within that category's balance?", "tone": 5, "branches": [
    {"label": "yes", "to": {"outcome": "Taken: a card payment, shown as a Purchase", "tone": 5}},
    {"label": "no", "to": {"outcome": "Declined: over the balance; notice sent", "tone": 6}}]}},
   {"label": "no", "to": {"outcome": "Declined: category not open; notice sent", "tone": 6}}]}},
  {"label": "no", "to": {"outcome": "Declined: card Frozen (notice sent) or Cancelled", "tone": 6}}]}}
```

### 4.5 · The declined attempt: decided

IA6 left one question to this unit: whether a declined card attempt should reach the app, as a notification or a record, which would extend the notification beyond claims and the data model beyond movements of money (IA6, "What IA8 and IA11 take"). Three options were open: nothing in the app (IA6's current fact), a record in Purchases, or a notification.

**Decision: a notification, and no record in Purchases** (Perqo, fictional). Each declined attempt on a card that is not Cancelled sends the employee one notification, "Card payment declined", naming the merchant, the amount and the reason (over the Meals balance, in the category's name as IA6's over-balance line does; category not open to you; card Frozen), and opening the screen that explains it: the category screen for a balance or a closed category, Card for a Frozen card, where Unfreeze card is (IA6, C.2). The reasons, each with its source:

- **Purchases keeps its meaning.** A Purchase is a card payment, money that moved (IA1, section 2.4; IA4, A.1). A decline in the same list would give one label two meanings, which IA3's D2 and IA6's label rule exist to prevent (IA6, section 6.1).
- **The employee is told when the problem happens, with the remedy.** NN/g's error-message guidance asks that a message say what went wrong and how to fix it (Neusesser and Sunwall, "Error-Message Guidelines", NN/g, 2023; IA6, section 4.3). The till's own message is the merchant's, and the system map shows it is the only one the employee gets today.
- **Correlation across surfaces.** The till and the app are two channels connected to one task; linking them is what Resmini and Rosati's external correlation names (Fisher, Norris and Buie 2012).
- **HR stops being the only route.** IA7 showed Admin the card's status because the employee asks HR why a payment was declined (IA7, section 2.3); the notice answers the employee first, and Admin stays as it was (least privilege, IA7, section 3.3).

The cost is a new object and an extended one, recorded so the data model stays honest. A **declined attempt** (O-18, model `card_decline`) holds merchant, amount, category, reason and date; it is not a transaction, so the transactions table still holds only movements of money (IA1, section 2.4). It triggers one notification (R-25, declined attempt triggers notification, 1 to 1). The notification (O-10) is now about one claim or one declined attempt, extending IA4's "the claim it is about". Admin does not show declined attempts. The app's notifications prompt is still asked after the first claim (IA6, section 4.4), so an employee who has never claimed and never allowed notifications sees the notice in Notifications (A-5.2) only; whether to ask at the first decline as well is a test for IA11.

What the decision changes in IA6, so the maintainer can update it: all three places that carry it, and a fourth the search found. (1) Deliverable C, C.2: the wireflow's "Declined at the till" screen gains a route "notification: Card payment declined" to the Meals category screen, and to Card [Frozen], and the paragraph's last sentence becomes "a declined attempt sends a notification, decided by IA8". (2) The facts-table row "A card payment over the balance ... is not shown in the app (proposed for IA8) | Deliverable C, C.2 | IA8's decision" becomes "... a declined attempt is not a card payment and is not in Purchases; the app shows it as a notification (IA8, section 4.5)", left free "the notice's wording". (3) The assumption row "Employees understand a declined payment from the balance they saw | C.2 | ... | IA8's proposed notice" keeps its test and changes its last cell to "the decline notification's wording and route (IA8)". (4) Deliverable A, A.2's open-question cell "should a declined attempt be shown? (IA8)" becomes "decided: as a notification (IA8)". The register's line "(proposed for IA8) ... Free: IA8's decision" changes the same way.

## 5 · Layering: one map, read one layer at a time

### 5.1 · The layers and their order

A map that holds three surfaces, five actors, four lifecycles and three rules on one sheet is unreadable if everything is drawn at once. Edward Tufte gives "Layering and separation" a chapter of *Envisioning Information* (Graphics Press, 1990, ch. 3; contents at [centrecountylibrary.org, contents](https://search.centrecountylibrary.org/Record/284250/TOC)); the chapter was not read for this unit, and the method below is this course's practice. The system map is stacked in three layers and a set of connections, each layer with its own identifiers, its own figure kind and its own question:

| Layer | Holds | Identifiers | Figure kind | Question it answers |
|---|---|---|---|---|
| Surface layer | each surface's top level, the shared objects with their names per surface, and the crossings between surfaces | S-, AD-, A-, H- (the surface units); O-, R- (IA4, IA7); X- (this unit) | objects | what is shared, what each surface calls it, what crosses |
| Actor and lifecycle layer | the actors, the two long lifecycles and the object lifecycles inside them | CL-, EL- (this unit); T- (IA7) | swimlanes; states | who does what, in what order, on which surface |
| Decision-tree layer | the rules that cut across surfaces | DT- (this unit) | decision; table | given these facts, which outcome |
| Connections | each place where an element of one layer depends on an element of another | J- (this unit) | matrix | which layer to change when one changes |

The order is fixed, and the reason is dependency: the lifecycles happen on the surfaces and the rules decide moves in the lifecycles, so each layer is read with the one above it already known. Each layer's elements carry identifiers from the unit that set them, and the connections cite only identifiers. That is what lets a reader take one layer at a time: a layer can be read, printed or reviewed alone, and a connection always names both ends.

The stacking extends IA2's split rule, "split rather than cram", with "→ see" continuation points between figures (IA2, section 4). The whole map is drawn twice: as its layers (figures 1 to 7 of this unit) and as one figure that draws each layer's elements as boxes and the connections as lines (Deliverable, D.4). Tones keep their IA2 meanings in every layer, so a reader moving between layers sees the same surface in the same tone; the layer is said by the figure kind and the caption, never by colour.

### 5.2 · What to leave out

IA2 set the cross-surface map's limit: it "holds the top level of each surface and nothing below; the sitemaps hold the rest" (IA2, section 1.10), and IA1 that every artefact says what it leaves out (IA1, section 4), after Tankala's point that a sitemap deliberately leaves detail out so that discussion stays manageable (Tankala, NN/g, 2023; IA1, section 4). The system map applies that test to each layer (Perqo, fictional):

- **Surface layer:** pages and screens below the top level, except the ones a crossing starts or ends on (S-5, S-6, AD-0, AD-1.3, AD-4, A-0.1, A-3.4 and the like); those are named by identifier, never redrawn.
- **Lifecycle layer:** the screens of each step (the wireflows hold them: IA6, C.1 to C.3; IA7, section 4.3); every lifecycle that stays on one surface (the admin user's Active and Removed, IA7, section 5.1).
- **Decision layer:** rules that read and are felt on one surface only (Admin's role permissions, IA7, Deliverable B); amounts left free (the auto-approve limit, the period's length).
- **Everywhere:** visual design, volumes (IA7's sizing client stays in IA7), and anything outside Perqo's surfaces beyond the step that hands over to it (the demo, the contract, the card network).

A thing earns a place on the system map when it crosses a surface, an actor or a layer. Anything that stays on one surface stays on that surface's map.

## 6 · How the map stays current

A system map goes out of date at every crossing, because a change on any surface may move one of its lines. Four practices keep it current, each built on a filed rule.

- **Change it where it changes, and cite by identifier.** Every element of the map is an identifier from a surface map or this unit's X-, CL-, EL-, DT- and J- series, kept when the element moves and retired when it is removed (IA2, section 4). A surface map that changes an identifier the system map cites is not finished until the J- or X- row that cites it is changed in the same piece of work.
- **The vocabulary first.** A label changes in the controlled vocabulary, then in the map's "Surface: Label" lines, then on the screens (IA2, section 4), and by Evans's rule "a change in the language is a change to the model" the model name is checked at the same time (Evans, *Domain-Driven Design Reference*, 2015; IA7, section 6.2).
- **Mark proposals, and keep the decided version visible** until the change is agreed (IA2, section 4). The decline notice of section 4.5 became a decision when this unit was filed, and IA6 was updated in the same filing with a dated note at each of the four places section 4.5 names; the map's J-07 row says so.
- **Review it on a trigger as well as a date.** A review at each release that touches two surfaces, and one a quarter, checking each J- row against the surface maps it cites: Perqo practice (Perqo, fictional). Gibbons's last step, refining the blueprint and producing a version to share with stakeholders (Gibbons 2018), treats distribution as part of the work; the review trigger is this course's practice, not hers. Rosenfeld, Morville and Arango describe IA style guides as "capturing your past decisions and guiding your future ones" (2015, ch. 13; IA2, section 4), and the map's face carries its version and date for the same reason (IA2, section 4 and the notation sheet).

Arango gives the life of an information environment over time two chapters of *Living in Information*, "Sustainability" and "Gardening" (Two Waves Books, 2018; IA1, section 1.3). The practices above are this course's version of gardening for one artefact; their test is whether a reader a year later can trust a J- row without opening every surface map, and IA12's assumption register is where that test is kept.

## Deliverable · The Perqo interaction map

*Face of this artefact (IA2, the notation sheet): cross-surface interaction map of Perqo, at fidelity F2 with F3's identifiers on every element (IA2's decision table: F2 kept current), in three layers and their connections: D.1 the surface layer, D.2 the actor and lifecycle layer, D.3 the decision-tree layer, D.4 the connections, drawn as the whole, and D.5 the reading guide. Decision: what is shared across Perqo's surfaces and what each calls it, who does what across them in what order, which rules decide the moves, and which elements must change together; readers: all six touchpoints (product management for scope, engineering for rules, objects and joins, content for labels, sales for the rules in words and the purchase lifecycle, support for where a person is and why an outcome happened, the client for its staff's place in each lifecycle); leaves out: what section 5.2 lists; owner: the IA designer; version 1, dated 9 November 2026; every lifecycle stage and rule this unit sets is assumed until tested (IA11); Perqo is fictional.*

### D.1 · The surface layer

**The surfaces** are IA1's, with the top levels IA5 to IA7 kept (Perqo, fictional): perqo.com (tone 1) with Product, Pricing, Customers, Help centre, Book a demo and Sign in, and Get the Perqo app in its footer (IA5, Deliverable B), its pages S-0 to S-12 with the campaign pages L- and the Help centre's H- (IA5, A.1 to A.3); Perqo Admin (tone 4) with Employees, Budgets, Policies, Approvals, Reports and Settings, its pages AD-0 to AD-6 (IA7, Deliverable C); the Perqo app (tone 3) with Home, Benefits, Claims, Card and Account, its screens A-0 to A-5 (IA6, Deliverable B); and the merchant side (tone 2), the till where the card is taken, whose own surface stays unset.

**The crossings.** Every line between two surfaces, with where it starts and lands (Perqo, fictional). X-01 to X-03 are IA5's crossing rows; X-03 to X-06 are IA6's external routes and entries; X-04, X-07 to X-09 are IA1's Admin-to-app line split by what it carries. X-03 and X-04 each answer two sources; X-10 to X-13 are added here, X-11 new with this unit.

| ID | From | To | What crosses | Starts on | Lands on |
|---|---|---|---|---|---|
| X-01 | perqo.com | Admin | HR and finance sign in | Sign in, S-5 (`external`) | Sign in, AD-0 |
| X-02 | Admin | perqo.com | an employee who arrived on Admin by mistake | AD-0's line "Looking for your benefits? Get the Perqo app" | Get the Perqo app, S-6 |
| X-03 | perqo.com | app | the download links | S-6 | the app stores, then E-3 |
| X-04 | Admin | app | HR's invitation | Invite employees, AD-1.3 [the group's budgets set] | Join, A-0.1, by E-2; S-6 without the app |
| X-05 | app | perqo.com | the external routes, each to its Help centre page | A-1; A-2.1 to A-2.4; A-3; A-3.1; A-3.4; A-4; A-5 | H-2.2.1; H-2.1.3; H-2.1; H-1.2.5; H-2.1.2; H-2.3.1, H-2.3.2; H-2; and H-2.2.2 from a used-up category |
| X-06 | perqo.com | app | links from Help centre articles into the app | H-2.1.1; H-2.1.3; an article on offers | New claim, A-3.1 (E-5); a category screen (E-6); Card offers, filtered (E-7) |
| X-07 | Admin | app | budgets as balances; policies as open categories and the rule line | Set budgets, AD-2.2; Policy, AD-3.1 | Home, A-1; A-2.1 to A-2.4; New claim, A-3.1 |
| X-08 | app | Admin | claims over the limit | Check and submit, A-3.2 | Approvals, AD-4 |
| X-09 | Admin | app | claim decisions | AD-4; the Perqo system's rule | a notification (E-4) to Claim, A-3.4 |
| X-10 | merchant side | app | card payments; offers | the till; the merchant's offers | Purchase, A-4.2.1; Card offers, A-4.3 |
| X-11 | merchant side | app | declined attempts *new* | the till (DT-3) | a notification to the category screen or Card |
| X-12 | app | Admin | the card's status | Freeze card, A-4.4 | the employee's record, AD-1.1 (Perqo card, status only) |
| X-13 | perqo.com | Perqo staff | the demo request | Book a demo, S-4 | sales, outside the surfaces (CL-2) |

**The shared objects and their names**, IA1's vocabulary as IA4 to IA7 extended it, with this unit's additions marked *new* (Perqo, fictional). Each row is a "Surface: Label" line on the map (IA2, section 5.2).

| Object (model name) | Admin | App | perqo.com | Merchant side |
|---|---|---|---|---|
| allocation (`allocation`) | Budget | Balance | Benefits budget | not shown |
| transaction, type claim | Claim; Submitted, Approved, Rejected, Paid | Claim; the same states | Claims | not shown |
| transaction, type card payment | Card payment, in Reports | Purchase | Card payments | the sale |
| policy | Policy | not shown; open categories and "Claims over the limit need HR approval" | Policies | not shown |
| card | Perqo card: Active, Frozen, Not issued, Cancelled *new* | Card | Perqo card | accepted at the till |
| employee | Employees; Invited, Active, Left | Profile | not shown | not shown |
| client | Company, with contract end date *new* | not shown | Customers | not shown |
| declined attempt (`card_decline`) *new* | not shown | a notification, "Card payment declined" | not shown | the decline at the till |

**Two decisions on the model** (IA7, section 6.2, handed on).

- **The model keeps `allocation`; Admin keeps the label Budget.** IA7 asked whether the model should take Admin's word. It should not, on two grounds. First, the word means a different unit in Admin's speech: Admin's Budget page (AD-2.1) is one employee group's budgets for one period, set by finance at once for the whole group (IA4, A.1; IA7, C.1), while the model's allocation is one employee's, per category and period; taking "budget" as the model name would let a ticket about the group's set and a ticket about one employee's share use the same word. Second, the app's Balance and perqo.com's Benefits budget would become translations of an Admin label, where today all three are recorded translations of one model term, IA7's reading of Evans's ubiquitous language (IA7, section 6.2). The vocabulary records the distinction: "Budget (Admin): the allocations of one employee group, category and period; one employee's allocation on their record".
- **Where boundaries between models would run.** IA7 read Admin and the app as one bounded context with two presentations, and named the catalogue and the merchant side as candidates for contexts of their own, with the joins R-07, R-14, R-16 and R-17 (IA7, section 6.2). The system map confirms those lines and adds one: the **benefits context** (client, admin user, employee group, policy, employee, allocation, claim, card payment, card, notification, declined attempt, audit entry; Admin and the app); the **catalogue context** (catalogue item and the taxonomy, owned by Perqo's content team; joined at R-07, policy covers catalogue item, and R-17, offer is for catalogue item); the **merchant context** (merchant and offer, tone 2; joined at R-14, merchant takes card payment, R-16 and the till's decision DT-3); and the **website context** (help article, customer story, demo request, perqo.com; joined to the product only through links and R-18 to R-20). Whether to build them as separate models stays engineering's decision (IA7, section 6.2); the map marks each join as a crossing that must keep its identifiers.

The surface layer, drawn: the four surfaces with their top levels (perqo.com tone 1, Admin tone 4, the app tone 3, the merchant side tone 2), five shared objects with their names on Admin, the app and perqo.com (tone 5, shared), and the main crossings labelled by their X- identifiers; the line between perqo.com and the app carries crossings both ways (X-03 and X-06 into the app, X-05 out of it); the figure labels X-01, X-03 to X-07 and X-09, and X-02, X-08 and X-10 to X-13 are in the table only. Each surface box keeps IA1's actions as IA2 redrew them: perqo.com -> book a demo and -> find help; Admin -> configure, -> approve and -> report; the app -> see balance, -> spend and -> claim (IA1, Deliverable; IA2, section 5.3); the merchant side's is -> take card payments, from IA4's merchant takes card payment (IA4, A.2, R-14). The lines from a surface to a shared object keep IA2's: Admin sets the policy and decides the claims over the limit; the app submits claims, shows the allocation as Balance, and shows and freezes the card (IA2, section 5.3; IA4, A.3). The lines between the shared objects carry IA4's relationships with their counts, drawn 1 for one and 0..* for any number: a claim is checked against one policy, and a policy checks any number of claims (R-09); a claim spends from one allocation, and an allocation is spent from by any number of claims (R-10); a card is used for any number of card payments, and each card payment uses one card (R-12); a card payment spends from one allocation, and an allocation is spent from by any number of card payments (R-13); a merchant takes any number of card payments, and each is taken by one merchant (R-14) (IA4, A.2). Lines read left to right on a level line and top to bottom otherwise, unless a triangle by the label marks the other way.

```viz
{"kind": "objects", "caption": "Product map across surfaces: the surface layer of the Perqo interaction map, F2 with identifiers; the four surfaces with their top levels, five shared objects with their names on Admin, the app and perqo.com as 'Surface: Label' lines, and the main crossings labelled by ID, the line between perqo.com and the app carrying crossings both ways; supports the decision on which surface and under which name a thing belongs, and what crosses (Deliverable, D.1). Tone 1 perqo.com; tone 4 Perqo Admin; tone 3 the Perqo app; tone 2 the merchant side; tone 5 the shared objects. Lines read left to right on a level line, top to bottom otherwise, unless a triangle marks the other way. Extends IA2, section 5.3's cross-surface map and IA1's surfaces map; top levels from IA5 to IA7; objects, names and counts from IA4, Deliverable A and IA7, Deliverable A; crossings X-01 to X-13 from D.1's table. Perqo is fictional.",
 "objects": [
  {"id": "site", "title": "perqo.com", "tone": 1, "attrs": ["Product", "Pricing", "Customers", "Help centre", "Book a demo", "Sign in (S-5)", "Get the Perqo app (S-6)"], "actions": ["-> book a demo", "-> find help"]},
  {"id": "admin", "title": "Perqo Admin", "tone": 4, "attrs": ["Employees", "Budgets", "Policies", "Approvals", "Reports", "Settings"], "actions": ["-> configure", "-> approve", "-> report"]},
  {"id": "app", "title": "Perqo app", "tone": 3, "attrs": ["Home", "Benefits", "Claims", "Card", "Account"], "actions": ["-> see balance", "-> spend", "-> claim"]},
  {"id": "merchant", "title": "merchant side", "tone": 2, "attrs": ["the till", "offers"], "actions": ["-> take card payments"]},
  {"id": "policy", "title": "policy", "tone": 5, "attrs": ["Admin: Policy", "app: not shown", "perqo.com: Policies"]},
  {"id": "claim", "title": "transaction, type claim", "tone": 5, "attrs": ["Admin: Claim", "app: Claim", "perqo.com: Claims"]},
  {"id": "alloc", "title": "allocation", "tone": 5, "attrs": ["Admin: Budget", "app: Balance", "perqo.com: Benefits budget"]},
  {"id": "card", "title": "card", "tone": 5, "attrs": ["Admin: Perqo card", "app: Card", "perqo.com: Perqo card"]},
  {"id": "payment", "title": "transaction, type card payment", "tone": 5, "attrs": ["Admin: Card payment", "app: Purchase", "perqo.com: Card payments"]}],
 "rows": [["site", "admin", null, "policy"], [null, null, null, "claim"], ["app", null, null, "alloc"], ["card", "payment", "merchant", null]],
 "links": [
  {"from": "site", "to": "admin", "label": "X-01 Sign in"},
  {"from": "site", "to": "app", "label": "X-03 download; X-05, X-06 help"},
  {"from": "admin", "to": "app", "label": "X-04 invites; X-07; X-09 decisions"},
  {"from": "admin", "to": "policy", "label": "sets"},
  {"from": "admin", "to": "claim", "label": "decides [over the limit]"},
  {"from": "app", "to": "claim", "label": "submits", "dir": "to"},
  {"from": "claim", "to": "policy", "label": "is checked against", "from_card": "0..*", "to_card": "1", "dir": "to"},
  {"from": "claim", "to": "alloc", "label": "spends from", "from_card": "0..*", "to_card": "1"},
  {"from": "app", "to": "alloc", "label": "shows as Balance"},
  {"from": "app", "to": "card", "label": "shows; freezes"},
  {"from": "card", "to": "payment", "label": "is used for", "from_card": "1", "to_card": "0..*"},
  {"from": "merchant", "to": "payment", "label": "takes", "from_card": "1", "to_card": "0..*", "dir": "to"},
  {"from": "payment", "to": "alloc", "label": "spends from", "from_card": "0..*", "to_card": "1", "dir": "to"}]}
```

### D.2 · The actor and lifecycle layer

**The actors** (Perqo, fictional), each with the surface and tone it acts in: the buyer at a prospective client (perqo.com, tone 1); Perqo's sales and setup staff (outside the surfaces, tone 5 in a lane); the account owner, HR manager and finance manager (Admin, tone 4; IA7, section 3); the employee (the app, tone 3); the merchant (the till, tone 2); the Perqo system (tone 5).

**The lifecycles**, each drawn in this unit or a filed one:

| Lifecycle | Stages or states | Drawn in | Crosses |
|---|---|---|---|
| Client company (purchase) | CL-1 Evaluate, CL-2 Trial, CL-3 Contract, CL-4 Onboard, CL-5 Run, CL-6 Renew or churn | figure 1, section 3.2 | perqo.com, Perqo staff, Admin, the app |
| Employee (benefit) | EL-1 Enrol, EL-2 Learn, EL-3 Decide, EL-4 Spend, EL-5 Claim, EL-6 Review, each period | figure 2, section 3.3 | Admin, the app, the Help centre, the till, the Perqo system |
| Claim | Submitted, Approved, Rejected, Paid; T1 to T6; EX-1 to EX-4 | IA7, Deliverable D | the app (A-3, A-3.4), Admin (AD-4, AD-1.1.1), the Perqo system |
| Employee status | Invited, Active, Left | IA7, section 5.1 | Admin (sets it), the app (Join makes Active; Left ends sign-in), the card (Cancelled on Left) |
| Card | Active, Frozen, Cancelled *new*; Not issued when none is held | section 3.4; IA4, A.1 | the app (freeze), Admin (status), the till (DT-3) |

**Where they nest.** EL-1 to EL-6 run inside CL-5 for each employee. The employee's status moves at EL-1 (Invited to Active) and at leaving (Left), which closes EL-4 and EL-5 for that employee (section 3.4). The claim's lifecycle runs inside EL-5, and its notifications reach EL-6. CL-6's churn ends every employee's lifecycle of that client at once.

### D.3 · The decision-tree layer

Each rule as its table, with the Unique hit policy: every combination of answers matches exactly one row (section 4.1). The trees are figures 3 to 5. "Any" means the answer does not matter on that row (Perqo, fictional).

**DT-1 · Eligibility** (figure 3). Read by: the app (what A-1 and A-2 show), the till (DT-3), Admin (No budget for next period).

| Row | Contract in force | Employee Active | Category open | Allocation set | Outcome |
|---|---|---|---|---|---|
| 1 | no | any | any | any | Sign-in ended; cards cancelled |
| 2 | yes | no | any | any | Invited: join first; Left: cannot sign in |
| 3 | yes | yes | no | any | Category not shown; card declined there |
| 4 | yes | yes | yes | no | Shown: budget for this period not set yet |
| 5 | yes | yes | yes | yes | Eligible: card and claims in this category |

**DT-2 · Approval routing** (figure 4). Read by: the app (A-3.3, A-3.4 and the reason), Admin (AD-4), the claim's lifecycle (T1 to T5).

| Row | Within balance on submission | At or under the limit | HR manager (not the claimant) approves | Within balance on approval | Outcome | Transition |
|---|---|---|---|---|---|---|
| 1 | no | any | any | any | Rejected, over the balance | T1 |
| 2 | yes | yes | any | any | Approved automatically | T2 |
| 3 | yes | no | yes | yes | Approved | T3 |
| 4 | yes | no | no | any | Rejected by HR, with a note | T4 |
| 5 | yes | no | yes | no | Rejected, over the balance | T5 |

In words, for sales and the Help centre (H-1.2.5): "A claim within the category's balance and at or under your limit is approved at once; over the limit, one of your HR managers decides, never the person claiming, and Perqo checks the balance again when they approve."

**DT-3 · Spend limits** (figure 5). Read by: the till, the app (A-4.2.1 and the decline notice), the allocation's spent.

| Row | Card Active | Category open | Within balance | Outcome |
|---|---|---|---|---|
| 1 | no | any | any | Declined: card Frozen (notice sent) or Cancelled |
| 2 | yes | no | any | Declined: category not open; notice sent |
| 3 | yes | yes | no | Declined: over the balance; notice sent |
| 4 | yes | yes | yes | Taken: a card payment, shown as a Purchase |

### D.4 · The connections, and the whole

Each place where an element of one layer depends on an element of another (Perqo, fictional). A connection names both ends by identifier; when either end changes, the other is checked (section 6).

| ID | Short name | Surface layer | Actor and lifecycle layer | Decision layer | Handed on by |
|---|---|---|---|---|---|
| J-01 | status | claim status attribute (O-07) | claim states, T1 to T6 (IA7, D) | DT-2 outcomes | IA4, "What the map hands on" |
| J-02 | limit | policy's auto-approve limit (O-04; AD-3.1) | Submitted, waiting in Approvals | DT-2, second question | IA4, "What the map hands on" |
| J-03 | Claims | Claims groups (A-3) and Claim (A-3.4) | the four claim states; EL-5, EL-6 | DT-2 reasons on A-3.4 | IA6; IA7 |
| J-04 | Approvals | Approvals (AD-4) | T3, T4, T5; EX-1, EX-3 | DT-2, HR's question and the recheck | IA7 |
| J-05 | invite | Invite employees (AD-1.3), X-04, Join (A-0.1) | Invited to Active; EL-1; CL-4 | DT-1, Employee Active | IA6, E-2; IA7, C.4 |
| J-06 | Purchase | Purchase (A-4.2.1); card payment (O-08) | EL-4 | DT-3, the category rule | IA6; IA4, Deliverable A |
| J-07 | decline | decline notice, X-11 (A-5.2) | EL-4 | DT-3, the three declines | IA6, C.2 (decided, section 4.5) |
| J-08 | categories | open categories (O-04) to A-2 | EL-2, EL-3 | DT-1, Category open | IA1, X-07 |
| J-09 | card | card status (O-09; AD-1.1; A-4) | Left; Cancelled | DT-1, Employee Active; DT-3, Card Active | IA7, section 5.1 (decided, section 3.4) |
| J-10 | contract | Company (AD-6.1), contract end date | CL-3, CL-6 | DT-1, Contract in force | register (decided, section 3.2) |
| J-11 | sign-in | Sign in (S-5), Get the Perqo app (S-6), AD-0 | CL-4, EL-1 | none | IA5, inventory and catalogue |
| J-12 | demo | Book a demo (S-4); customer stories (S-3.x) | CL-1, CL-2, CL-6 | none | IA5; section 3.2 |
| J-13 | rule words | How approval rules work (H-1.2.5); New claim's rule line (A-3.1) | EL-2, EL-5 | DT-2 in words | IA6, B.1; section 4.1 |
| J-14 | budgets | Set budgets (AD-2.2); No budget for next period | CL-4, CL-5, EL-6 | DT-1, Allocation set | IA7, C.4; section 3.2 |

The same connections as a matrix, one row per connection and one column per layer, so the map can be read down one column, a layer at a time, or across one row, a join at a time. Row labels are the J- identifier and the short name in the table's second column; blank cells are layers a connection does not touch. Rows take tone 5, shared, because every connection crosses layers.

```viz
{"kind": "matrix", "caption": "Connections of the Perqo interaction map: each join J-01 to J-14 with the element it touches in each layer; supports the decision on which layers must change together when one element changes (Deliverable, D.4). Read down a column for one layer, across a row for one join. Rows tone 5, shared, because every connection crosses layers; a blank cell is a layer the join does not touch. Identifiers from IA4 to IA7 and this unit's sections 3 and 4; the layers from section 5.1. Perqo is fictional.",
 "cols": ["Surface layer", "Actor and lifecycle layer", "Decision layer"],
 "rows": [
  {"label": "J-01 status", "tone": 5, "cells": ["claim status, O-07", "claim states, T1 to T6", "DT-2 outcomes"]},
  {"label": "J-02 limit", "tone": 5, "cells": ["auto-approve limit, O-04", "waits in Approvals", "DT-2, second question"]},
  {"label": "J-03 Claims", "tone": 5, "cells": ["A-3, A-3.4", "four states; EL-5, EL-6", "DT-2 reasons"]},
  {"label": "J-04 Approvals", "tone": 5, "cells": ["AD-4", "T3, T4, T5; EX-1, EX-3", "HR's question; recheck"]},
  {"label": "J-05 invite", "tone": 5, "cells": ["AD-1.3, X-04, A-0.1", "Invited to Active; EL-1", "DT-1, Active"]},
  {"label": "J-06 Purchase", "tone": 5, "cells": ["A-4.2.1, O-08", "EL-4", "DT-3, category rule"]},
  {"label": "J-07 decline", "tone": 5, "cells": ["X-11, A-5.2", "EL-4", "DT-3 declines"]},
  {"label": "J-08 categories", "tone": 5, "cells": ["open categories to A-2", "EL-2, EL-3", "DT-1, open"]},
  {"label": "J-09 card", "tone": 5, "cells": ["O-09, AD-1.1, A-4", "Left; Cancelled", "DT-1; DT-3, card"]},
  {"label": "J-10 contract", "tone": 5, "cells": ["AD-6.1, end date", "CL-3, CL-6", "DT-1, contract"]},
  {"label": "J-11 sign-in", "tone": 5, "cells": ["S-5, S-6, AD-0", "CL-4, EL-1", null]},
  {"label": "J-12 demo", "tone": 5, "cells": ["S-4, S-3.x", "CL-1, CL-2, CL-6", null]},
  {"label": "J-13 rule words", "tone": 5, "cells": ["H-1.2.5, A-3.1", "EL-2, EL-5", "DT-2 in words"]},
  {"label": "J-14 budgets", "tone": 5, "cells": ["AD-2.2, queue", "CL-4, CL-5, EL-6", "DT-1, allocation"]}]}
```

The whole, in one figure: the surface layer's four surfaces in the top row, the client, claim and employee lifecycles in the middle row (the employee-status and card lifecycles sit under J-09), the decision trees in the bottom row, and the main connections as lines labelled by their J- identifiers. Each box names its layer in its first line and points to the figure that draws it in full, so the whole is read as an index to the layers. Lifecycles and trees that span surfaces take tone 5, shared; the surfaces keep their own tones: perqo.com 1, Admin 4, the app 3, the merchant side 2.

```viz
{"kind": "objects", "caption": "The Perqo interaction map, whole: the surface layer (top row), the actor and lifecycle layer (middle row) and the decision-tree layer (bottom row), with the main connections labelled by their J- IDs; supports the decision on where a change starts and which layers it reaches (Deliverable, D.4). Tone 1 perqo.com; tone 4 Perqo Admin; tone 3 the Perqo app; tone 2 the merchant side; tone 5 lifecycles and rules that span surfaces. Lines relate (no movement), read left to right on a level line and top to bottom otherwise. Each box points to the figure that draws its layer in full; layering from section 5.1; connections from D.4's table. Perqo is fictional.",
 "objects": [
  {"id": "site", "title": "perqo.com", "tone": 1, "attrs": ["surface layer", "S-0 to S-12; L-; H-", "→ see figure 6"]},
  {"id": "admin", "title": "Perqo Admin", "tone": 4, "attrs": ["surface layer", "AD-0 to AD-6", "→ see figure 6"]},
  {"id": "app", "title": "Perqo app", "tone": 3, "attrs": ["surface layer", "A-0 to A-5", "→ see figure 6"]},
  {"id": "merchant", "title": "merchant side", "tone": 2, "attrs": ["surface layer", "the till", "→ see figure 6"]},
  {"id": "cl", "title": "client lifecycle", "tone": 5, "attrs": ["lifecycle layer", "CL-1 to CL-6", "→ see figure 1"]},
  {"id": "claimlc", "title": "claim lifecycle", "tone": 5, "attrs": ["lifecycle layer", "Submitted, Approved, Rejected, Paid", "→ see IA7, D"]},
  {"id": "el", "title": "employee lifecycle", "tone": 5, "attrs": ["lifecycle layer", "EL-1 to EL-6", "→ see figure 2"]},
  {"id": "dt3", "title": "DT-3 spend limits", "tone": 5, "attrs": ["decision layer", "→ see figure 5"]},
  {"id": "dt2", "title": "DT-2 approval routing", "tone": 5, "attrs": ["decision layer", "→ see figure 4"]},
  {"id": "dt1", "title": "DT-1 eligibility", "tone": 5, "attrs": ["decision layer", "→ see figure 3"]}],
 "rows": [["site", "admin", "app", "merchant"], ["cl", "claimlc", "el", "dt3"], [null, "dt2", "dt1", null]],
 "links": [
  {"from": "site", "to": "cl", "label": "J-12 demo"},
  {"from": "admin", "to": "cl", "label": "J-10, J-14"},
  {"from": "admin", "to": "claimlc", "label": "J-04 Approvals"},
  {"from": "app", "to": "claimlc", "label": "J-03 Claims"},
  {"from": "app", "to": "el", "label": "J-05, J-08"},
  {"from": "merchant", "to": "dt3", "label": "the till"},
  {"from": "el", "to": "dt3", "label": "J-06, J-07"},
  {"from": "claimlc", "to": "dt2", "label": "J-01, J-02"},
  {"from": "el", "to": "dt1", "label": "J-09, J-14"}]}
```

### D.5 · Reading guide

**The surface layer.** Read it first, and read it as a vocabulary with routes. Start from figure 6 and the crossings table: each surface is a box with its top level and nothing below it, each shared object carries its name on each surface, and each crossing names the page or screen it leaves and the one it lands on. A product manager asks of it which surfaces a change touches; a content writer, which name the thing has on each; an engineer, which addresses and identifiers a crossing depends on. What it does not say is when anything happens or who decides; for those, go down a layer.

**The actor and lifecycle layer.** Read it second, left to right in time, one lane at a time. Figure 1 is the client's relationship with Perqo, from a buyer on perqo.com to renewal or churn; figure 2 is one employee's period, from the invitation to the next period's balances; the claim's and the employee's state diagrams (IA7) sit inside them. Each step names the surface it happens on by identifier, so a reader can go back up to the surface layer at any step. Support reads it to place a caller in a stage; the client reads it to find where its own HR and finance staff act; sales reads figure 1 for what happens after the contract. Where a step branches, the branch is a rule, and the rule is in the layer below.

**The decision-tree layer.** Read it third, one tree at a time, top to bottom, "yes" on the left. Each tree answers one question that is set on one surface and felt on another; each outcome uses the surface's own words and carries its transition or reason; each tree has a table with one row per path, which is what engineering builds and tests, and a sentence in words, which is what sales and the Help centre say. A tree stops at the first question that ends the path, so support can say at which question a case stopped.

**The connections.** Read them last, or first when something has changed. The J- table and its matrix list every place where an element of one layer depends on an element of another; read down a column to see everything one layer hands to the others, or across a row to see everything one join holds together. The whole-map figure is the index: it shows which lifecycle sits under which surface and which tree decides which lifecycle, and each box points to the figure that holds its layer in full. A change to any identifier in a J- row is not done until the other cells of that row have been checked.

## What later units take

**IA10** builds the briefs for the touchpoints from IA4 to IA8 (the course's units list); from this unit it takes the decision trees with their words for sales (D.3), the purchase lifecycle for sales and the client (CL-1 to CL-6), and the J- table as the list of what each touchpoint must be told when a join changes.

**IA11** tests it. Every assumption this unit adds, with its test:

| Decision or assumption | Where | Test (IA11) | What changes if it fails |
|---|---|---|---|
| The decline notice is understood and acted on | section 4.5 | interviews after a decline; support's tickets on declines before and after (IA12 as proxy) | the notice's wording, route or the choice of a record |
| Employees allow notifications early enough to see a decline | section 4.5 | the share of employees with notifications allowed at their first decline, from analytics | asking at the first decline too |
| Inviting only after budgets are set does not delay onboarding | section 3.2 | time from contract to first join, at onboarding interviews with clients | a warning in place of the block |
| The leaver rules fit clients' contracts | section 3.4 | interviews with clients at contract and with HR managers | the unspent amount's handling (G-7) |
| How a leaver learns of a decided claim | G-5 | interviews with HR managers; support's tickets from former employees | an email of the decision |
| The trees' words let sales explain the rules | D.3 | sales explains DT-2 to a buyer in a recorded demo; the buyer restates it | the words, or the tree's order |
| Readers can read one layer alone | D.5 | ask each touchpoint a question answerable from one layer only, with only that layer in hand | the layers' boundaries |

**IA12's assumption register** records the rows above with their tests, and keeps G-5, G-6 and G-7 as open questions with owners.

**DD-IA1** takes the Perqo interaction map as the artefact its comparison is made against: what a published map of a real product shows and leaves out, set beside this map's three layers and their connections.

## Perqo facts set by this unit

Every fact below is a course convention (Perqo, fictional), never evidence about the world. Each keeps every registered fact; none renames an IA1 to IA7 label, object, attribute or relationship.

| Fact | Set in | Left free |
|---|---|---|
| The client's purchase lifecycle: CL-1 Evaluate, CL-2 Trial (the demo; no free trial), CL-3 Contract, CL-4 Onboard, CL-5 Run, CL-6 Renew or churn | section 3.2 | the contract's terms |
| Client attribute contract end date (O-01), shown read only on Company (AD-6.1); a renewal sets a new end date | section 3.2 | none |
| Churn: from the day after the contract end date no admin user or employee of the client can sign in and every card of the client is cancelled; records are kept; a customer story about a former client is removed with a redirect to S-3 | section 3.2 | how long records are kept |
| Onboarding order: client and account owner, admin users, groups and policies, budgets, invitations, joining | section 3.2 | none |
| Invite employees is unavailable for a group until its budgets for the current period are set, shown disabled with "Set this group's budgets first" (extends IA7's employee -> invite and employee group -> invite employees) | section 3.2 | none |
| The employee's benefit lifecycle: EL-1 Enrol, EL-2 Learn, EL-3 Decide, EL-4 Spend, EL-5 Claim, EL-6 Review, each period, inside CL-5 | section 3.3 | the period's length |
| Perqo orders the card when the employee becomes Active; Card shows "not issued yet" until issued | section 3.3 | how long issuing takes |
| On Left: the card is Cancelled at once; the allocations are closed to new spending (allocation attribute closed); claims submitted before leaving are decided as usual and paid if approved; what remains is reported as unspent in Budget use | section 3.4 | the contract's treatment of unspent money; how a leaver learns of a decided claim (G-5) |
| Card status Cancelled (extends IA4's Active, Frozen); Admin shows Active, Frozen, Not issued, Cancelled | section 3.4 | none |
| A category open but with no allocation for the period shows "Your budget for this period is not set yet" (a new state of IA6's category screen); no payment or claim there | section 4.2 | none |
| Declines at the till: over the category's balance, card Frozen (IA6), card Cancelled, category not open to the group | section 4.4 | none |
| Eligibility (DT-1), approval routing (DT-2, extending IA2's tree with IA7's EX-1 and T5) and spend limits (DT-3), each as tree and table with the Unique hit policy | section 4; Deliverable, D.3 | the auto-approve limit's amount |
| Every declined attempt sends the employee a notification, "Card payment declined", with merchant, amount and reason, opening the category screen or Card; none on a Cancelled card; it is not shown in Purchases or in Admin | section 4.5 | the notice's wording |
| Object O-18, declined attempt (`card_decline`): merchant, amount, category, reason, date; not a transaction; R-25, declined attempt triggers notification (1, 1); notification (O-10) is about one claim or one declined attempt | section 4.5 | none |
| The model keeps `allocation`; Admin's Budget means one group's allocations for a category and period, or one employee's on their record | Deliverable, D.1 | none |
| Model boundaries as candidates: benefits, catalogue, merchant and website contexts, joined at R-07, R-14, R-16, R-17, R-18 to R-20 and DT-3 | Deliverable, D.1 | whether engineering builds them as separate models |
| Identifiers X-01 to X-13 (crossings), CL-1 to CL-6, EL-1 to EL-6, DT-1 to DT-3, J-01 to J-14, G-1 to G-7 | sections 1, 3, 4; Deliverable | none |
| Open gaps: a mid-period move to another group (G-6); money unspent at a period's end (G-7) | sections 1, 3.3 | both |
| Review of the interaction map at each release touching two surfaces, and quarterly | section 6 | none |

## Sources

- Bitner, Mary Jo, Amy Ostrom and Felicia Morgan. "Service Blueprinting: A Practical Technique for Service Innovation". *California Management Review* 50, no. 3 (Spring 2008). [cmr.berkeley.edu, service blueprinting](https://cmr.berkeley.edu/2008/05/50-3-service-blueprinting-a-practical-technique-for-service-innovation/)
- Camunda. "Hit policy". Undated (vendor documentation of the DMN standard, checked 9 November 2026). [docs.camunda.io, hit policy](https://docs.camunda.io/docs/components/modeler/dmn/decision-table-hit-policy/)
- Court, David, Dave Elzinga, Susan Mulder and Ole Jørgen Vetvik. "The consumer decision journey". *McKinsey Quarterly*, 2009, no. 3 (a consultancy's study in its own journal). [mckinsey.com, decision journey](https://www.mckinsey.com/~/media/McKinsey/Business%20Functions/Marketing%20and%20Sales/Our%20Insights/The%20consumer%20decision%20journey/The%20consumer%20decision%20journey.pdf)
- Fisher, Jon, Simon Norris and Elizabeth Buie. "Sense-making in Cross-channel Design". *Journal of Information Architecture* 4, no. 2 (2012): 5 to 30. [journalofia.org, cross-channel sense-making](https://journalofia.org/volume4/issue2/02-fisher/jofia-0402-02-fisher.pdf)
- Gartner. "Gartner Says the Marketing-to-Sales Handoff Should No Longer Exist". Press release, 9 October 2018 (analyst firm; vendor material). [gartner.com, buying jobs](https://www.gartner.com/en/newsroom/press-releases/2018-10-09-gartner-says-the-marketing-to-sales-handoff-should-no-longer-exist)
- Gibbons, Sarah. "Service Blueprints: Definition". Nielsen Norman Group, 27 August 2017. [nngroup.com, blueprint definition](https://www.nngroup.com/articles/service-blueprints-definition/)
- Gibbons, Sarah. "UX Mapping Methods Compared: A Cheat Sheet". Nielsen Norman Group, 5 November 2017. [nngroup.com, mapping cheat sheet](https://www.nngroup.com/articles/ux-mapping-cheat-sheet/)
- Gibbons, Sarah. "The 5 Steps to Service Blueprinting". Nielsen Norman Group, 4 February 2018. [nngroup.com, five steps](https://www.nngroup.com/articles/5-steps-service-blueprinting/)
- Kalbach, James. *Mapping Experiences: A Complete Guide to Customer Alignment Through Journeys, Blueprints, and Diagrams*. 2nd ed. O'Reilly, 2020. Part 3, chs 10 to 14 (contents and publisher's description). [oreilly.com, Mapping Experiences](https://www.oreilly.com/library/view/mapping-experiences-2nd/9781492076629/)
- Lavidge, Robert, and Gary Steiner. "A Model for Predictive Measurements of Advertising Effectiveness". *Journal of Marketing* 25, no. 6 (October 1961) (the article not read; see the unsure list).
- Object Management Group. *Decision Model and Notation* (DMN), version 1.5. August 2024 (standard). [omg.org, DMN 1.5](https://www.omg.org/spec/DMN/1.5/About-DMN)
- Resmini, Andrea, and Luca Rosati. *Pervasive Information Architecture: Designing Cross-Channel User Experiences*. Morgan Kaufmann, 2011. Part 2, chs 3 to 8; ch. 9 (contents only). [shop.elsevier.com, Pervasive IA](https://shop.elsevier.com/books/pervasive-information-architecture/resmini/978-0-12-382094-5)
- Shostack, G. Lynn. "Designing Services That Deliver". *Harvard Business Review*, January 1984 (the article's page only). [hbr.org, Shostack 1984](https://hbr.org/1984/01/designing-services-that-deliver)
- Tufte, Edward. *Envisioning Information*. Graphics Press, 1990. Ch. 3, "Layering and separation" (contents only). [centrecountylibrary.org, contents](https://search.centrecountylibrary.org/Record/284250/TOC)
- Cited through the filed units, for claims made there: Arango, *Living in Information*, 2018 (IA1); Brown, *Communicating Design*, 2nd ed., 2011, ch. 6 (IA2); Evans, *Domain-Driven Design Reference*, 2015 (IA7); Garrett, *Visual Vocabulary Quick Reference* (IA2); Neusesser and Sunwall, "Error-Message Guidelines", NN/g, 2023 (IA6); Rosenfeld, Morville and Arango, *Information Architecture: For the Web and Beyond*, 4th ed., 2015, chs 2 and 13 (IA1, IA2); Tankala, "Information Architecture vs. Sitemaps", NN/g, 2023 (IA1). Full references in IA1 to IA7, Sources.

## Unsure list

- Lavidge and Steiner 1961: title, journal, volume, issue and month from indexing records (scilit.net; archives.uah.edu); the article, its pages and its exact steps were not read.
- Resmini and Rosati 2011: only the contents were seen; correlation's definition is quoted as Fisher, Norris and Buie 2012 quote it; the five questions in section 2.1 are this unit's, from the chapter names.
- Shostack 1984: only the HBR page was seen; the article's text, and what it says about the line of visibility, were not read.
- Tufte 1990, ch. 3: only the title was seen in a library record; nothing from the chapter is claimed.
- Kalbach 2020: the contents and the publisher's description were read; no chapter's text.
- Court and others 2009: the base of almost 20,000 consumers is the article's own statement; the study's method was not examined.
- Camunda's hit-policy wording is a vendor's paraphrase of DMN; the DMN specification's own text on hit policies was not read.
- That no study compares trees with tables for engineers and salespeople is this unit's knowledge, not a search result.
- Fisher, Norris and Buie 2012: the journal's About page calls it "a peer-reviewed scholarly journal" (checked 9 November 2026); its printed pages run 5 to 30, though its cite-as line says 5 to 32.
- Bitner, Ostrom and Morgan 2008: only the abstract was read, not the text or pages; the journal's page lists the authors as Ostrom, Bitner, Morgan, and the order used here is the commonly cited one, from knowledge.
- Object: the Perqo interaction map, Deliverable (D.1 to D.5) and section 5
- Fresh check 2026-11-09 (Fable 5.1; no Fable 5.1 fresh check is owed): fix · 1 error, 3 should-fix, 9 minor; applied as verified but the search flag (kept off, as the build order sets it) and the Object line (kept, as a list item); figures 3, 4, 5 and 7 passed; figures 1, 2 and 8 fixed and passed their second check, figure 6 its third; report `audits/ux/fresh-check-IA8.md`
