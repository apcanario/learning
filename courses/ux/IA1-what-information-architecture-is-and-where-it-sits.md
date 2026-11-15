---
code: IA1
title: What information architecture is, and where it sits
course: ux · IA · Information Architecture
model: Opus 5.5
written: 2026-10-30
search: off
---

# IA1 · What information architecture is, and where it sits

## 1 · Four definitions, and what each one includes and leaves out

Ask four designers what information architecture is and you will get four answers, and most of the disagreement in a product team about who owns "the IA" comes from people holding different ones without saying so. The field's standard works give four definitions worth holding side by side. Each draws the boundary in a different place, and each is useful for a different job.

### 1.1 Rosenfeld, Morville and Arango: four systems

The book the field calls the Polar Bear book, Louis Rosenfeld, Peter Morville and Jorge Arango's *Information Architecture: For the Web and Beyond* (4th ed., O'Reilly, 2015), opens its chapter 2, "Defining Information Architecture", with four definitions rather than one:

1. "The structural design of shared information environments."
2. "The synthesis of organization, labeling, search, and navigation systems within digital, physical, and cross-channel ecosystems."
3. "The art and science of shaping information products and experiences to support usability, findability, and understanding."
4. "An emerging discipline and community of practice focused on bringing principles of design and architecture to the digital landscape."

The second definition is the one teams can use, because it names parts. Part II of the book is built on it: its introduction says it will examine "four systems that are shared by most interactive information environments", and it gives each its own chapter (ch. 6, Organization Systems; ch. 7, Labeling Systems; ch. 8, Navigation Systems; ch. 9, Search Systems), followed by ch. 10 on thesauri, controlled vocabularies and metadata, the machinery underneath labelling and search (Rosenfeld, Morville and Arango 2015, Part II and chs 6 to 10).

In a sentence each, as this course will use them:

- **Organisation system:** how content is grouped, and by what scheme (topic, task, audience, time, alphabet).
- **Labelling system:** what each group and item is called, in headings, links, menu entries and index terms.
- **Navigation system:** how people browse and move, through the menus, links and paths that let them travel the structure.
- **Search system:** how people query and read results, including what is indexed and how results are presented.

```viz
{"kind": "tree", "caption": "The four systems of an information architecture (section 1.1). Drawn from Rosenfeld, Morville and Arango, Information Architecture: For the Web and Beyond, 4th ed., 2015, Part II, chs 6 to 9; the one-line glosses are this unit's.", "root": {"label": "Information architecture", "tone": 1, "children": [
 {"label": "Organisation system", "tone": 2, "children": [{"label": "How content is grouped"}]},
 {"label": "Labelling system", "tone": 3, "children": [{"label": "What each group and item is called"}]},
 {"label": "Navigation system", "tone": 4, "children": [{"label": "How people browse and move"}]},
 {"label": "Search system", "tone": 5, "children": [{"label": "How people query and read results"}]}]}}
```

What this definition includes: the whole apparatus of finding. It also includes the invisible parts, which is the point of the book's chapter 5 ("The Anatomy of an Information Architecture"), whose opening states that "a well-designed information architecture is invisible to users", and whose section headings separate browsing aids, search aids and "invisible" components (Rosenfeld, Morville and Arango 2015, ch. 5). Chapter 2 places the four systems inside a frame of three things they must answer to, with sections headed Context, Content and Users (ch. 2). The book also warns against the narrow reading: it raises the question "But isn't information architecture about making sitemaps, wireframes, and website navigation menus?" and answers that those are important elements but "there is much more to this story!" (ch. 2).

What it leaves out, on this unit's reading: the four systems are named for the act of finding and understanding information. They say little about things that change state and the work people do on them. A Perqo claim (Perqo, fictional) that moves from submitted to approved to paid is content the organisation system must place and the labelling system must name, but the moves between its states are not one of the four systems. Garrett, below, gives that territory a separate name.

### 1.2 Covert: sense-making, and information, content and data

Abby Covert's *How to Make Sense of Any Mess: Information Architecture for Everybody* (self-published, 2014) widens the definition to anything people arrange. On her own site she states it as: "Information architecture (IA) is the way we arrange the parts of something to make it understandable as a whole" ([abbycovert.com, *Make Sense*](https://abbycovert.com/make-sense/), checked 30 Oct 2026). The book's seven chapters run as a method rather than a taxonomy of parts: Identify the Mess, State Your Intent, Face Reality, Choose a Direction, Measure the Distance, Play with Structure, Prepare to Adjust (same page).

The distinction Covert draws that a product team most needs is between information, content and data. In an excerpt from the book published as "What's Information?" (Abby Covert, UX Magazine, 22 January 2015, [uxmag.com/articles/whats-information](https://uxmag.com/articles/whats-information)), she says information "isn't a *thing*": "It's whatever a user interprets from the arrangement or sequence of things they encounter." Data and content are the things: "Data is facts, observations, and questions about something", and "Content can be cookies, words, documents, images, videos, or whatever you're arranging or sequencing." She adds that "the absence of content or data can be just as *informing* as the presence."

The consequence for practice is direct. What a team ships is content and data in an arrangement; the information is what each person makes of that arrangement. An empty Perqo balance screen informs the employee of something (no budget, or not yet), whether or not anyone designed that message.

What Covert's definition includes: everything, at any scale, physical or digital, and the people doing the interpreting. What it leaves out: a boundary. If IA is any arrangement of parts for understanding, it gives a team no way to say where IA ends and interface, content or data work begins. That is a deliberate choice for a book addressed to "everybody"; it is a weakness when the question in the room is whose decision a menu label is.

### 1.3 Arango: the architecture of information environments

Jorge Arango's *Living in Information: Responsible Design for Digital Places* (Two Waves Books, 2018) takes the architectural half of the term literally. In the excerpt of its chapter 6, "Architecture", he defines the field as "the area of practice and field of study that concerns itself with the design of information environments" (Jorge Arango, "Living in Information: Responsible Design for Digital Places, a Book Excerpt", UX Magazine, 14 August 2019, [uxmag.com](https://uxmag.com/articles/living-in-information-responsible-design-for-digital-places-a-book-excerpt)). The environments are software as much as websites: of products such as Slack and Android he writes, "These things are also information environments; through their language and structures, they create contexts that change how people understand the world, think, and act." Where architects arrange physical forms, designers of information environments do it "by arranging semantic elements such as icons, labels, buttons, and links" (same excerpt).

The book's ten chapters show its scope: Environments, Context, Incentives, Engagement, Technology, Architecture, Structure, Systems, Sustainability, Gardening ([Rosenfeld Media, *Living in Information*](https://rosenfeldmedia.com/books/living-in-information/)). What it includes that the others do not: the business incentives that shape an environment, and its life over time, in the chapters on sustainability and gardening. What it leaves out: method at the level of artefacts. None of its chapters is about a diagram type; a designer who wants to know how to draw a sitemap goes elsewhere.

### 1.4 Garrett: the structure plane, between scope and skeleton

Jesse James Garrett's *The Elements of User Experience* (2nd ed., New Riders, 2011) is the definition most product teams have met, usually as a diagram. It stacks five planes from abstract to concrete, and its chapter titles name them and their contents: ch. 3, The Strategy Plane: Product Objectives and User Needs; ch. 4, The Scope Plane: Functional Specifications and Content Requirements; ch. 5, The Structure Plane: Interaction Design and Information Architecture; ch. 6, The Skeleton Plane: Interface Design, Navigation Design, and Information Design; ch. 7, The Surface Plane: Sensory Design (Garrett 2011, contents).

Garrett's original one-page diagram of 30 March 2000 ([jjg.net/elements/pdf/elements.pdf](https://www.jjg.net/elements/pdf/elements.pdf)) splits every plane into two columns, "Web as software interface" and "Web as hypertext system", and defines each element in a line. Information architecture, on the hypertext side of the structure plane, is "structural design of the information space to facilitate intuitive access to content". Its twin on the software side, interaction design, is "development of application flows to facilitate user tasks, defining how the user interacts with site functionality". One plane up, navigation design is "design of interface elements to facilitate the user's movement through the information architecture", and interface design is "design of interface elements to facilitate user interaction with functionality" (Garrett 2000). The same diagram puts functional specifications on the software side of the scope plane and content requirements on the hypertext side, and sets information design on the skeleton plane in both columns, beside interface design and beside navigation design (Garrett 2000).

```viz
{"kind": "matrix", "caption": "Garrett's five planes with information architecture located on the structure plane, shaded (section 1.4). Plane names and contents from the chapter titles of Garrett, The Elements of User Experience, 2nd ed., 2011, chs 3 to 7; the two columns, and the placing in them of the scope, structure and skeleton elements, from Garrett's diagram of 30 March 2000; the strategy and surface rows give only the chapter titles' contents, set in both columns.", "cols": ["Web as software interface", "Web as hypertext system"],
 "rows": [
  {"label": "Surface", "cells": ["Sensory design", "Sensory design"]},
  {"label": "Skeleton", "cells": ["Interface design, information design", "Navigation design, information design"]},
  {"label": "Structure", "tone": 2, "cells": ["Interaction design", {"mark": "Information architecture", "tone": 2}]},
  {"label": "Scope", "cells": ["Functional specifications", "Content requirements"]},
  {"label": "Strategy", "cells": ["Product objectives, user needs", "Product objectives, user needs"]}
 ]}
```

What Garrett's placing includes: a clear position. IA sits above the decisions about what content is required (scope) and below the decisions about which interface elements present it (skeleton). Navigation design is a separate element one plane up, defined as movement *through* the information architecture, so the diagram itself separates the two. What it leaves out: in the 2000 diagram IA lives only in the hypertext column, and the flows of a task-heavy product belong to interaction design. For a product like Perqo Admin, which is mostly tasks on objects, that split leaves IA with less than the team needs from it, and later units of this course take back the object structure that sits under both columns.

### 1.5 Holding the four together

Read together, the four definitions agree on one thing and differ on scope. They agree that IA is structure: the arrangement of parts, their names and the routes between them, below the level of what any one screen looks like. They differ on how far it reaches. Garrett's is the narrowest, Rosenfeld, Morville and Arango's the most complete inventory of parts, Covert's the broadest in scale, and Arango's the broadest in time and consequence. This course uses the four systems as its inventory of parts, Garrett's plane as its position in the stack, Covert's distinction between information and its material, and Arango's insistence that an environment is lived in over time.

## 2 · Four lines a designer has to hold

Every one of the definitions above leaves IA next to some other discipline, and most failures of ownership happen at those borders. Four lines matter in a product team. For each, one worked example on Perqo (Perqo, fictional): a flexible-benefits platform whose client companies give each employee a benefits budget to spend across categories, with three surfaces, perqo.com (the sales and product website), Perqo Admin (the backoffice where a client's HR and finance managers configure budgets, policies, approvals and reports) and the Perqo app (the employee app for seeing balances and spending benefits).

### 2.1 IA and navigation design

Jen Cardello draws this line for Nielsen Norman Group ("The Difference Between Information Architecture (IA) and Navigation", 22 June 2014, [nngroup.com/articles/ia-vs-navigation](https://www.nngroup.com/articles/ia-vs-navigation/)). IA shapes the interface without appearing in it, and it is documented in spreadsheets and diagrams. Navigation is the set of interface components (global, local and utility navigation, breadcrumbs, filters, related links, footers) that help people find information and functionality and encourage them to take desirable actions. IA informs navigation; the two are not the same. Her recommendation, labelled here as NN/g guidance, is to make at least a first pass at the IA before choosing navigation components, because a component chosen for its looks may not hold the structure: she gives the example of an inverted-L navigation, which she says can hold a site no more than four tiers deep.

**Worked example (Perqo, fictional).** The Perqo app groups everything an employee can spend on into four benefit categories, Health, Learning, Mobility and Meals, and treats Claims (receipts the employee asks to be reimbursed for) as their own object, separate from card purchases. That is IA: an organisation decision (by category, with claims apart) and a labelling decision (these four names). Whether the app shows the categories as a row of tabs on its Home screen, as a list under a Benefits tab, or as filters on one feed is navigation design. The team can swap a tab bar for a menu without changing the IA. If it renames Claims to Refunds, or folds claims into one Activity feed with card purchases, it has changed the IA, even if no navigation component moved.

### 2.2 IA and the user interface

Garrett's planes put the line here: interface design is on the skeleton plane, "design of interface elements to facilitate user interaction with functionality", and information architecture is the structure beneath it (Garrett 2000; Garrett 2011, chs 5 and 6). IA says what exists, how it is grouped and what it is called; the interface decides which controls present it on a given screen.

**Worked example (Perqo, fictional).** In Perqo Admin, the IA decision is that Approvals is a top-level area holding every claim awaiting a decision, that each claim is also reachable from the record of the employee who made it, and that pending claims are grouped by policy. The interface decisions are whether pending claims show as a table or as cards, where the bulk-approve control sits, how a rejected claim's reason is entered and how the row looks on a narrow screen. A redesign of the Approvals table that keeps the area, its grouping and its two routes in has changed the UI and left the IA as it was. A proposal to remove the route from the employee record is an IA change, even if it is drawn as a wireframe.

### 2.3 IA and content strategy

Kristina Halvorson and Melissa Rach's *Content Strategy for the Web* (2nd ed., New Riders, 2012) divides content strategy into a quad of four components. Chapter 8 covers the two content components: substance, "What content do you need and why?", and structure, "How will your content be prioritized, organized, formatted, and displayed?" Chapter 9 covers the two people components: workflow, "What processes, tools, and human resources are required for content initiatives to launch successfully and maintain ongoing quality", and governance, how the key decisions about content are made (Halvorson and Rach 2012, chs 8 and 9).

The overlap is in the quad's own words: "organized" sits inside content strategy's structure component. So the books leave the line to the team. A workable division: content strategy owns whether a piece of content should exist, what it says, who keeps it current and who decides; IA owns where it lives in the structure, what it and its group are called, and how people reach it.

**Worked example (Perqo, fictional).** perqo.com has a Help centre used by both HR managers and employees. Content strategy decides that there will be an article on how an employee claims back a receipt, that the support team owns it and reviews it each quarter, and that it uses the employee's words. IA decides that the Help centre is split first by audience (For HR and finance teams, For employees) and then by task, that this article sits under For employees, Claims, and that it is also reachable from the Claims screen of the app. If the team has no content strategist, the IA work still has to ask the substance and governance questions, and should say in its deliverable that it has assumed the answers.

### 2.4 IA and the engineering data model

The data model is how engineering stores the system: entities, fields and relations, chosen for integrity and performance. Alan Cooper and his co-authors name the cost of letting it show through: an interface that follows the implementation model of the software, rather than the mental model of the person using it, is hard to use, and the represented model, what the product presents, should sit close to the user's mental model (Cooper, Reimann, Cronin and Noessel, *About Face: The Essentials of Interaction Design*, 4th ed., Wiley, 2014, ch. 1, "Implementation Models and Mental Models", p. 16). IA is a large part of that represented model: the groupings and names people meet. It is not obliged to mirror the schema, and it must still be buildable from it.

**Worked example (Perqo, fictional).** Engineering stores every movement of money in one table of transactions, with a type field that is either card payment or claim, and stores each employee's money as an allocation per benefit category per period. The IA presents those as Purchases and Claims, two separate lists, because employees do two different things with them (a purchase is done; a claim waits for approval). Admin calls the allocation a Budget, because HR and finance set it; the app calls the same number a Balance, because the employee spends it. One entity, two labels, each correct for its reader. The line is held when the IA deliverable records the mapping (allocation in the model, Budget in Admin, Balance in the app), so engineering can build it and nobody "fixes" the labels to match the schema.

## 3 · Why IA exists as a discipline

Two lines of descent meet in the term, and both still show in how teams talk about IA.

The first is architectural. Andrea Resmini and Luca Rosati's history ("A Brief History of Information Architecture", *Journal of Information Architecture*, vol. 3, no. 2, 2011, pp. 33 to 46, [journalofia.org](https://journalofia.org/volume3/issue2/03-resmini)) traces "architecture" in computing to a 1964 IBM paper on the System/360 that defined architecture as "the conceptual structure and functional behavior", and reports that in 1970 a group at Xerox PARC was set up to develop technology supporting the "architecture of information". The modern use they date to Richard Saul Wurman's address at the American Institute of Architects conference of 1976, and they report Morville's later statement that Wurman had coined the expression "information architect" in 1975 (Resmini and Rosati 2011). Wurman chaired that 1976 convention, in Philadelphia, and his framing was about cities whose public information was not public (Molly Wright Steenson, blog post, 1 October 2010, [girlwonder.com](https://www.girlwonder.com/2010/10/you-really-wish-you-could-attend-these-conferences.html); a historian's blog, labelled as such). Asked in 2004 why he chose "architecture" over the existing term "information design", Wurman said, in substance, that architecture was the clearer word for systems that have to work and perform (interview by Dirk Knemeyer, InfoDesign, January 2004, [bogieland.com](https://www.bogieland.com/specials/wurman_interview.html)). His book *Information Architects* (Graphis, 1997) collected work in that sense.

The second line is library science, and it is the one that produced the practice of IA on the web. Resmini and Rosati describe Rosenfeld and Morville teaching early courses on the internet by 1994, bringing a library and information science view of the problem: how to organise, label and retrieve large bodies of content. Their book *Information Architecture for the World Wide Web* (O'Reilly, 1998), known as the Polar Bear book for the animal on its cover, "hit the shelves, and information architecture went mainstream" (Resmini and Rosati 2011). The two lines did not merge comfortably: Resmini and Rosati quote Morville's reaction to Wurman's 1997 book, "this is not information architecture, this is information design" (same article). The Polar Bear book went through a second edition (2002) and a third (2006) under the same title; the fourth (2015) added Arango as an author and changed the title to *For the Web and Beyond*, with "digital, physical, and cross-channel ecosystems" written into its second definition (Rosenfeld, Morville and Arango 2015, ch. 2). That widening had been argued in Resmini and Rosati's own *Pervasive Information Architecture: Designing Cross-Channel User Experiences* (Morgan Kaufmann, 2011).

```viz
{"kind": "timeline", "caption": "How information architecture became a discipline (section 3). Dates from Resmini and Rosati, 'A Brief History of Information Architecture', Journal of Information Architecture 3(2), 2011, and from the editions of Rosenfeld and Morville's book and of Resmini and Rosati 2011.", "start": 1960, "end": 2020, "ticks": [1960, 1970, 1980, 1990, 2000, 2010, 2020],
 "events": [
  {"at": 1964, "label": "IBM System/360 paper"},
  {"at": 1970, "label": "Xerox PARC group"},
  {"at": 1976, "label": "Wurman's AIA conference address"},
  {"at": 1994, "label": "Rosenfeld and Morville teaching"},
  {"at": 1998, "label": "Polar Bear book, 1st ed."},
  {"at": 2011, "label": "Pervasive Information Architecture"},
  {"at": 2015, "label": "4th ed., For the Web and Beyond"}]}
```

Why the history matters to a working designer: the library line gives IA its method for finding (organisation, labelling, navigation, search), and the architectural line gives it its claim on understanding and on the shape of the whole place. A team that thinks of IA only as the menu has inherited half of the first line and none of the second.

## 4 · What an IA deliverable is for, which decision it supports, and who reads it

IA is invisible by design (Rosenfeld, Morville and Arango 2015, ch. 5), so the deliverable is the only form in which a team can see it, argue about it and agree to it. Cardello makes the same point from the other side: IA is documented in spreadsheets and diagrams (Cardello 2014).

The standard works list what those documents are. Rosenfeld, Morville and Arango's chapter 13 ("Design and Documentation") covers sitemaps (high-level and detailed), wireframes, content mapping and inventory, content models, controlled vocabularies, and information architecture style guides (2015, ch. 13). Dan Brown's *Communicating Design* (2nd ed., New Riders, 2011) gives a chapter each to personas, concept models, site maps, flowcharts and wireframes (chs 3 to 7). He defines a site map as "A visual representation of the relationships between different pages on a web site" and says "It provides the project team with one view of how the site will be constructed" (Brown 2011, ch. 5). Garrett published a notation for drawing such diagrams, *A visual vocabulary for describing information architecture and interaction design* ([jjg.net/ia/visvocab](http://www.jjg.net/ia/visvocab/)), first released in October 2000 and revised since ("The Visual Vocabulary Three Years Later: An Interview with Jesse James Garrett", Boxes and Arrows, 11 December 2003, [boxesandarrows.com](https://boxesandarrows.com/the-visual-vocabulary-three-years-later-an-interview-with-jesse-james-garrett/)); IA2 sets this course's own notation.

Two things follow from those sources, and they shape every deliverable in this course.

**A deliverable is one view, chosen for a decision.** Brown's phrase is "one view". Samhita Tankala's NN/g article on sitemaps makes the corollary explicit: a sitemap represents the IA and is drawn after it, and it deliberately leaves out much of the detail gathered during IA work so that discussion with stakeholders stays manageable ("Information Architecture vs. Sitemaps", 3 September 2023, [nngroup.com](https://www.nngroup.com/articles/information-architecture-sitemaps/)). So the useful question about any IA artefact is which decision it is meant to support, and what it leaves out to support it. Cardello's sequencing gives one decision directly: the first-pass IA exists so the team can choose navigation components that will hold the structure (Cardello 2014). Others in this course follow the same pattern: a sitemap supports the decision about what exists and where; a vocabulary table supports the decision about what things are called; an object map supports the decision about what the system is made of and how its parts relate.

**A deliverable has named readers.** Brown's reader is the project team (Brown 2011, ch. 5). In a product organisation that team divides, and the course goal names six touchpoints this course will build on: product management, engineering, content, sales, support and clients. Each reads an IA document for a different decision. Product management reads it for scope and priority; engineering for what must be built and how the labels map to the model (section 2.4); content for where each piece lives and what it is called (section 2.3); sales for how the product will be shown and named to a buyer; support for how a customer will describe where they are; the client for whether their own structure (departments, policies, approval chains) fits. Which artefact serves which reader is the work of later units; the rule this unit sets is that every IA deliverable states, on its face, the decision it supports and who is meant to read it.

## 5 · A first look at IA across three surfaces: Perqo

Perqo (Perqo, fictional) is one product with three surfaces, each built for different people, each with a different kind of information architecture. Who uses which:

- A **buyer at a prospective client** (typically someone in HR or finance choosing a benefits provider) uses perqo.com to understand the product, see pricing and book a demo.
- An **HR manager** at a client uses Perqo Admin to manage the employee list, set policies (which categories are open, what needs approval), invite employees and approve claims. They reach Admin through Sign in on perqo.com.
- A **finance manager** at a client uses Perqo Admin to set budgets per employee group and period and to read spend reports, through the same sign-in.
- An **employee** uses the Perqo app to see their balance, spend with the Perqo card at merchants, and claim back receipts. They meet perqo.com only for help articles and the link to download the app.

A merchant side exists (the shops where the card is accepted); this unit leaves it unmapped, and later units add it where they need it.

```viz
{"kind": "matrix", "caption": "The Perqo surfaces and who uses each (section 5). Perqo is fictional; roles and surfaces as invented in this unit's section 5.", "cols": ["perqo.com", "Perqo Admin", "Perqo app"],
 "rows": [
  {"label": "Buyer at a prospective client", "tone": 1, "cells": [{"mark": "primary", "tone": 2}, null, null]},
  {"label": "HR manager", "tone": 4, "cells": ["sign in", {"mark": "primary", "tone": 2}, null]},
  {"label": "Finance manager", "tone": 4, "cells": ["sign in", {"mark": "primary", "tone": 2}, null]},
  {"label": "Employee", "tone": 3, "cells": ["help, download", null, {"mark": "primary", "tone": 2}]}
 ],
 "legend": [{"mark": "primary", "means": "the surface built for this person", "tone": 2}, {"mark": "sign in", "means": "passes through on the way to another surface"}]}
```

The three surfaces carry three kinds of IA, and the four systems weigh differently in each.

**perqo.com** is a website in the sense the Polar Bear book was written for. Its IA is mostly organisation and labelling: a shallow hierarchy (Product, Pricing, Customers, Help centre), labels written for a buyer who does not yet know Perqo's vocabulary, and a search system that matters mainly in the Help centre. Its sitemap is the artefact that fits it, and a later unit builds that sitemap.

**Perqo Admin** is a backoffice: few pages, many objects, and permissions that decide who sees what. Its top-level areas are Employees, Budgets, Policies, Approvals, Reports and Settings. The four systems still apply, but most of the hard IA questions are about objects and their relations (a policy belongs to an employee group; a claim is checked against a policy and spends from a budget) and about states (a claim submitted, approved, rejected, paid). Those are the questions section 1.1 found the four systems saying least about, and Garrett assigned to interaction design (section 1.4). A sitemap of Admin would list its areas and miss most of its structure.

**The Perqo app** is small and task-driven. Its top level is Home (the balance), Benefits, Claims, Card and Account. Its IA problem is reduction: deciding what an employee needs on one screen, and naming it in their words (Balance, where Admin says Budget; section 2.4).

The three IAs are joined, because the same things cross them. A budget set in Admin is a balance in the app. A policy set in Admin decides whether an employee's claim goes straight through or waits. The category names that HR switches on in Admin are the names the employee sees. The Help centre on perqo.com answers questions about both of the other surfaces. One journey shows the joins:

```viz
{"kind": "swimlanes", "caption": "One Perqo journey across the three surfaces (section 5). Perqo is fictional; steps as described in this unit's section 5.",
 "lanes": [{"id": "site", "label": "perqo.com", "tone": 1}, {"id": "admin", "label": "Perqo Admin", "tone": 4}, {"id": "app", "label": "Perqo app", "tone": 3}],
 "steps": [
  {"id": "demo", "lane": "site", "col": 0, "label": "Book a demo"},
  {"id": "policy", "lane": "admin", "col": 1, "label": "Set budgets and policies"},
  {"id": "invite", "lane": "admin", "col": 2, "label": "Invite employees"},
  {"id": "open", "lane": "app", "col": 3, "label": "See balance"},
  {"id": "claim", "lane": "app", "col": 4, "label": "Submit claim"},
  {"id": "approve", "lane": "admin", "col": 5, "label": "Approve claim"},
  {"id": "report", "lane": "admin", "col": 6, "label": "Read spend report"}
 ],
 "links": [{"from": "demo", "to": "policy", "label": "contract"}, {"from": "policy", "to": "invite"}, {"from": "invite", "to": "open", "label": "invites"}, {"from": "open", "to": "claim"}, {"from": "claim", "to": "approve", "label": "queues"}, {"from": "approve", "to": "report"}]}
```

A buyer books a demo on perqo.com; once the client has signed, its finance manager sets budgets and its HR manager sets policies in Admin; HR invites employees; an employee opens the app and sees a balance; the employee submits a claim; the claim queues in Admin's Approvals for HR; finance reads the resulting spend in Reports. Every arrow in that journey crosses a surface, and every crossing is a place where a label, a grouping or a state has to mean the same thing on both sides. This is the cross-channel problem that the fourth edition wrote into its definition and that Resmini and Rosati made the subject of *Pervasive Information Architecture* (section 3). It is also why this course goes past the sitemap: the artefact that holds Perqo together has to show the surfaces, the objects they share and the routes between them, which is the cross-surface interaction map the course goal names.

## Deliverable · Information architecture: a definition sheet for a product team

*One page. Hand it over at the start of any project that will touch structure.*

**What IA is.** Information architecture is the structural design of a product's information: what it contains, how that is grouped, what each part is called, and how people find their way to it, arranged so that the people using it can understand it as a whole. (Built from Rosenfeld, Morville and Arango 2015, ch. 2; Covert, *Make Sense*; Garrett 2000.) It sits below the interface and above the list of required content and functions (Garrett 2011, chs 4 to 6). Users do not see it; they see its effects (Rosenfeld, Morville and Arango 2015, ch. 5).

**What IA is not.**
- **Navigation.** Navigation is the set of interface components that let people move through the IA; the IA is the organisation, structure and naming beneath them (Cardello 2014). Swapping one menu component for another leaves the IA as it was; changing what is grouped or what it is called changes it (this unit's rule, section 2.1).
- **The user interface.** The interface decides which controls present the structure on a screen; the IA is the structure beneath it (Garrett 2000). A table redesign leaves the IA as it was; removing a route to an item changes it (this unit's rule, section 2.2).
- **Content strategy.** Content strategy decides whether content should exist, what it says, and who keeps it current. IA decides where it lives, what it is called and how people reach it. The two overlap on structure, and the team says who owns the overlap (Halvorson and Rach 2012, chs 8 and 9).
- **The data model.** The data model is how the system stores things. The IA is how people meet them. The closer what people meet sits to their mental model, the easier the product is to use (Cooper and others 2014, ch. 1). The two need not match, and the mapping between them is written down (this unit's rule, section 2.4).

**The four systems** (Rosenfeld, Morville and Arango 2015, chs 6 to 9).
- **Organisation:** how content is grouped, and by which scheme.
- **Labelling:** what each group and item is called.
- **Navigation:** how people browse and move through the structure.
- **Search:** how people query, what is indexed and how results are presented.

**The five questions an IA answers.**
1. **What is in it?** The content, data and functions the product holds (Garrett 2011, ch. 4; Cardello 2014).
2. **How is it grouped?** The organisation scheme and structure (organisation system).
3. **What is each thing called?** The labels, consistent across every surface that shows the same thing (labelling system).
4. **How do people get to it?** By browsing and by searching (navigation and search systems).
5. **For whom, and in what context?** Which users, which content, which business and technical context the arrangement is built to hold (Rosenfeld, Morville and Arango 2015, ch. 2, Context, Content, Users).

**Every IA deliverable states on its face:** the decision it supports, who is meant to read it, and what it leaves out (Brown 2011, ch. 5; Tankala 2023).

## Deliverable · The Perqo surfaces map

*Perqo is fictional. This map is the base later units build on; IA2 redraws it in the course notation.*

```viz
{"kind": "objects", "caption": "The Perqo surfaces map: three surfaces, their top-level areas, the jobs each serves and what passes between them (Deliverable; section 5). Perqo is fictional; every label as invented in section 5 of this unit.",
 "objects": [
  {"id": "site", "title": "perqo.com", "tone": 1, "attrs": ["Product", "Pricing", "Customers", "Help centre", "Sign in"], "actions": ["-> book a demo", "-> find help"]},
  {"id": "admin", "title": "Perqo Admin", "tone": 4, "attrs": ["Employees", "Budgets", "Policies", "Approvals", "Reports", "Settings"], "actions": ["-> configure", "-> approve", "-> report"]},
  {"id": "app", "title": "Perqo app", "tone": 3, "attrs": ["Home", "Benefits", "Claims", "Card", "Account"], "actions": ["-> see balance", "-> spend", "-> claim"]}
 ],
 "rows": [[null, "site", null], ["admin", null, "app"]],
 "links": [
  {"from": "site", "to": "admin", "label": "contract, sign in"},
  {"from": "site", "to": "app", "label": "download, help"},
  {"from": "admin", "to": "app", "label": "budgets, policies, invites, decisions"}
 ]}
```

**The surfaces (Perqo, fictional).**

| Surface | Built for | Job | Top-level areas | Kind of IA | Hardest IA question |
|---|---|---|---|---|---|
| perqo.com | Buyers at prospective clients; HR managers, finance managers and employees in passing | Explain and sell the product; route signed-in users; answer help questions | Product, Pricing, Customers, Help centre, Sign in | Shallow website hierarchy; labels for people who do not yet know Perqo's terms | How to split the Help centre between two audiences who ask about two different surfaces |
| Perqo Admin | HR managers and finance managers at client companies | Configure budgets, policies and approvals; manage employees; report on spend | Employees, Budgets, Policies, Approvals, Reports, Settings | Object-heavy backoffice; permissions decide what each role sees | How objects relate (group, policy, budget, claim) and how a claim moves through its states |
| Perqo app | Employees at client companies | See the balance; spend with the card; claim back receipts | Home, Benefits, Claims, Card, Account | Small, task-driven; one screen at a time | What to show first, and in the employee's own words |

**Benefit categories (Perqo, fictional):** Health, Learning, Mobility, Meals. Switched on per employee group by HR in Policies; shown to the employee under Benefits.

**What crosses between surfaces.**

| From | To | What crosses | Where it can break |
|---|---|---|---|
| perqo.com | Perqo Admin | A signed contract; HR and finance sign in | The buyer's words on the site and the configuration words in Admin differ |
| perqo.com | Perqo app | Download link; help articles for employees | A help article names a screen the app calls something else |
| Perqo Admin | Perqo app | Budgets (as balances), policies (as open categories and approval rules), invitations, approval decisions | One thing carries two labels without a written mapping |

**One thing, three names: the shared vocabulary so far (Perqo, fictional).**

| Data model | Perqo Admin | Perqo app | perqo.com |
|---|---|---|---|
| allocation (per employee, category, period) | Budget | Balance | Benefits budget |
| transaction, type card payment | Card payment | Purchase | Card payments |
| transaction, type claim | Claim | Claim | Claims |
| policy | Policy | (not shown; its effect shows as open categories and approval rules) | Policies |
| employee group | Employee group | (not shown) | Teams and groups |

**Users of the map.** Product management, to see which surface a feature touches; engineering, for the vocabulary mapping; content and support, for which surface a help article is about; sales, for the words used on perqo.com; the client, to check that the roles and areas fit how their own HR and finance teams work. The decision it supports: on which surface, and under which name, a new piece of content or function belongs. What it leaves out: the merchant side, each surface's pages below the top level, the objects inside Admin and their states, and every flow except the one journey in section 5. Later units add them.

## Sources

- Arango, Jorge. *Living in Information: Responsible Design for Digital Places*. Two Waves Books, 2018. Contents at [rosenfeldmedia.com/books/living-in-information](https://rosenfeldmedia.com/books/living-in-information/).
- Arango, Jorge. "Living in Information: Responsible Design for Digital Places, a Book Excerpt" (ch. 6, Architecture). UX Magazine, 14 August 2019. [uxmag.com/articles/living-in-information-responsible-design-for-digital-places-a-book-excerpt](https://uxmag.com/articles/living-in-information-responsible-design-for-digital-places-a-book-excerpt)
- Brown, Dan M. *Communicating Design: Developing Web Site Documentation for Design and Planning*. 2nd ed. New Riders, 2011 (published September 2010, copyright 2011). Chs 3 to 7.
- Cardello, Jen. "The Difference Between Information Architecture (IA) and Navigation". Nielsen Norman Group, 22 June 2014. [nngroup.com/articles/ia-vs-navigation](https://www.nngroup.com/articles/ia-vs-navigation/)
- Cooper, Alan, Robert Reimann, David Cronin and Christopher Noessel. *About Face: The Essentials of Interaction Design*. 4th ed. Wiley, 2014. Ch. 1, "Implementation Models and Mental Models", p. 16.
- Covert, Abby. *How to Make Sense of Any Mess: Information Architecture for Everybody*. Self-published, 2014. Definition and contents at [abbycovert.com/make-sense](https://abbycovert.com/make-sense/) (checked 30 Oct 2026).
- Covert, Abby. "What's Information?" (excerpt from *How to Make Sense of Any Mess*). UX Magazine, 22 January 2015. [uxmag.com/articles/whats-information](https://uxmag.com/articles/whats-information)
- Garrett, Jesse James. "The Elements of User Experience" (diagram). 30 March 2000. [jjg.net/elements/pdf/elements.pdf](https://www.jjg.net/elements/pdf/elements.pdf)
- Garrett, Jesse James. "A visual vocabulary for describing information architecture and interaction design". First released October 2000, revised since. [jjg.net/ia/visvocab](http://www.jjg.net/ia/visvocab/)
- "The Visual Vocabulary Three Years Later: An Interview with Jesse James Garrett". Boxes and Arrows, 11 December 2003. [boxesandarrows.com/the-visual-vocabulary-three-years-later-an-interview-with-jesse-james-garrett](https://boxesandarrows.com/the-visual-vocabulary-three-years-later-an-interview-with-jesse-james-garrett/) (interview; practice).
- Garrett, Jesse James. *The Elements of User Experience: User-Centered Design for the Web and Beyond*. 2nd ed. New Riders, 2011. Chs 3 to 7.
- Halvorson, Kristina, and Melissa Rach. *Content Strategy for the Web*. 2nd ed. New Riders, 2012. Chs 8 and 9.
- Knemeyer, Dirk. "Richard Saul Wurman: The InfoDesign interview". InfoDesign, January 2004. [bogieland.com/specials/wurman_interview.html](https://www.bogieland.com/specials/wurman_interview.html) (interview; practice).
- Resmini, Andrea, and Luca Rosati. "A Brief History of Information Architecture". *Journal of Information Architecture* 3, no. 2 (2011): 33 to 46. [journalofia.org/volume3/issue2/03-resmini](https://journalofia.org/volume3/issue2/03-resmini)
- Resmini, Andrea, and Luca Rosati. *Pervasive Information Architecture: Designing Cross-Channel User Experiences*. Morgan Kaufmann, 2011.
- Rosenfeld, Louis, and Peter Morville. *Information Architecture for the World Wide Web*. O'Reilly, 1998 (2nd ed. 2002; 3rd ed. 2006).
- Rosenfeld, Louis, Peter Morville and Jorge Arango. *Information Architecture: For the Web and Beyond*. 4th ed. O'Reilly, 2015. Chs 2, 5, 6 to 10, 13. Contents at [oreilly.com](https://www.oreilly.com/library/view/information-architecture-4th/9781491913529/).
- Steenson, Molly Wright. "You really wish you could attend these conferences". Blog post, 1 October 2010. [girlwonder.com](https://www.girlwonder.com/2010/10/you-really-wish-you-could-attend-these-conferences.html) (blog; practice).
- Tankala, Samhita. "Information Architecture vs. Sitemaps". Nielsen Norman Group, 3 September 2023. [nngroup.com/articles/information-architecture-sitemaps](https://www.nngroup.com/articles/information-architecture-sitemaps/)
- Wurman, Richard Saul. *Information Architects*. Graphis, 1997.

## Unsure list

- Garrett's 2000 diagram places "information design" in both columns of the skeleton plane: read from a text extraction of the PDF, not from the drawn layout.
- Garrett, Elements 2nd ed. and Brown, Communicating Design 2nd ed. are dated 2011 per the course brief and catalogue copyright; O'Reilly lists Brown's as September 2010.
- Cooper and others, About Face 4th ed., ch. 1, p. 16: section location verified from the contents; the represented-model argument is from knowledge of the section, not re-read.
- Halvorson and Rach's governance component: paraphrased; the source's full question was not seen.
- Title and year of Garrett's visual vocabulary (2002) from knowledge; the page could not be fetched.
- Wurman's 1975 coinage of "information architect" is reported by Resmini and Rosati from Morville; the 1975 AIA Journal article was not seen.
- Wurman's "public information is not public" framing of the 1976 convention is as reported by Steenson from the conference brochure.
- Wurman's 2004 interview answer is paraphrased from a summary, not quoted.
- Polar Bear book 2nd (2002) and 3rd (2006) edition years from knowledge and O'Reilly catalogue entries, not from the title pages.
- Two Waves Books as the publisher of Living in Information, from knowledge; the publisher's page does not print it.
- Fresh check 2026-10-30 (Opus 5.5): keep · 0 errors, 4 should-fix, 7 minor; all applied; report `audits/ux/fresh-check-IA1.md`
