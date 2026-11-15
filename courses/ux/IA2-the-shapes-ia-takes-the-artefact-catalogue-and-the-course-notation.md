---
code: IA2
title: "The shapes IA takes: the artefact catalogue and the course notation"
course: ux · IA · Information Architecture
model: Opus 5.5
written: 2026-10-30
search: off
---

# IA2 · The shapes IA takes: the artefact catalogue and the course notation

## 1 · The catalogue: ten artefacts and the question each answers

IA1 set the rule this unit builds on: an IA deliverable is one view, chosen for a decision, with named readers, and it states on its face what it leaves out (IA1, section 4; Brown, *Communicating Design*, 2nd ed., 2011, ch. 5; Tankala, NN/g, 2023). The field's own lists of those views are short. Rosenfeld, Morville and Arango's chapter on documentation calls sitemaps and wireframes "the two most common types of IA diagrams", and goes on to content mapping and inventory, content models, controlled vocabularies and style guides (*Information Architecture: For the Web and Beyond*, 4th ed., O'Reilly, 2015, ch. 13). Dan Brown's book gives a chapter each to personas, concept models, site maps, flowcharts and wireframes (Brown 2011, chs 3 to 7). A product team with a backoffice and an app needs more than either list: it also has objects, rules and lifecycles to draw, and journeys that cross surfaces.

This unit catalogues ten artefacts, in six families. A family is a set of artefacts that answer the same kind of question and are drawn with the same figure kind in this course's notation (section 5).

| Family | Artefacts | The kind of question |
|---|---|---|
| Inventories and vocabularies | content inventory and audit; taxonomy and controlled vocabulary | What do we have, and what is each thing called? |
| Structure | sitemap; navigation model | Where does each thing live, and how do people get there? |
| Objects | object map; object-relationship map | What is the system made of, and how do its parts relate? |
| Flows | user flow, task flow, wireflow | What steps does a person take, on which screens? |
| Rules and lifecycles | decision tree; state diagram | What does the system decide, and what states can a thing be in? |
| Journeys across actors and surfaces | service blueprint; cross-surface interaction map | Who does what, where, and what crosses between them? |

### 1.0 · Three fidelities

Each entry below says what fidelity the artefact needs at which stage. This course uses three levels. They are a course convention, set here so later units can name them; the published sources distinguish fidelity per artefact (Rosenfeld, Morville and Arango separate "High-Level Architecture Sitemaps" from "Detailed Sitemaps", 2015, ch. 13) but do not give one scale for all of them.

- **F1, sketch.** The shape and the main names only. Every assumption is marked. Made in hours, to argue about.
- **F2, working.** Complete for its stated scope; labels in the product's own vocabulary; conditions and exceptions shown. Made to agree on.
- **F3, specification.** Every element has a stable identifier, every condition and state is shown, and the artefact carries an owner, a version and a date. Made to build from and to keep.

The readers named below are the six touchpoints of the course goal, as IA1 section 4 first described what each reads for: product management, engineering, content, sales, support and the client.

### 1.1 · Content inventory and content audit

**The question.** What content exists, where, who owns it, and is it any good?

Anna Kaley's NN/g article separates the two halves. An inventory is "a list of every piece of digital content you currently have, captured at either the page or asset level"; an audit "examines, assesses, and evaluates the quality of the content listed in the inventory". She recommends inventory fields (title, URL, owner, topic, format, last-modified date, metadata, location of source files) and an audit outcome per item of keep, update or remove, with an owner for each update ("Content Inventory and Auditing 101", Nielsen Norman Group, 27 September 2020, [nngroup.com/articles/content-audits](https://www.nngroup.com/articles/content-audits/)). Rosenfeld, Morville and Arango treat content mapping and inventory as part of IA documentation (2015, ch. 13).

- **Readers.** Content and support, first; product management for scope; the client when their own content is migrated.
- **Fidelity.** F2 at the start of any redesign of an existing surface (an inventory is only useful when complete for its scope); F3 when it becomes the migration list engineering builds from.
- **Not to be mistaken for:** a sitemap. An inventory lists what exists today, item by item; a sitemap proposes where things will live. An inventory sorted by URL looks like a hierarchy and is read as one, which carries today's structure into tomorrow's without anyone deciding to.

### 1.2 · Taxonomy and controlled vocabulary

**The question.** What is each thing called, which other words mean the same, and how do the terms nest?

The US standard for controlled vocabularies, ANSI/NISO Z39.19-2005 (R2010), *Guidelines for the Construction, Format, and Management of Monolingual Controlled Vocabularies*, names four kinds of controlled vocabulary: lists, synonym rings, taxonomies and thesauri ([niso.org](https://niso.org/publications/ansiniso-z3919-2005-r2010)). Rosenfeld, Morville and Arango's chapter 10 covers synonym rings, authority files, classification schemes and thesauri, the three semantic relationships (equivalence, hierarchical, associative) and preferred terms, and says that "In many large metadata-driven products, controlled vocabularies have become the glue that holds the systems together" (2015, ch. 10). Page Laubheimer defines a taxonomy as "A closed list of acceptable terms that are arranged hierarchically and are used to describe and classify content", and places it backstage: the taxonomy maps the concepts used to describe content, where the IA structure maps where content lives and the navigation is the frontstage layer people see ("Taxonomy 101: Definition, Best Practices, and How It Complements Other IA Work", Nielsen Norman Group, 3 July 2022, [nngroup.com/articles/taxonomy-101](https://www.nngroup.com/articles/taxonomy-101/)). Heather Hedden's *The Accidental Taxonomist* (3rd ed., Information Today, 2022) is a book-length guide to building one.

- **Readers.** Content and engineering (the terms become metadata, filters and search synonyms); support (the variant terms are the words customers use); sales (the preferred terms are the words on the website).
- **Fidelity.** F1 as a word list in discovery; F2 once the labels are agreed; F3 when engineering builds search, filters or tagging on it.
- **Not to be mistaken for:** the navigation. A taxonomy may hold far more terms than any menu shows, and its hierarchy is for classifying, so it need not match the order people browse in (Laubheimer 2022). IA1's mapping of one data-model entity to two labels (section 2.4) is a small controlled vocabulary.

### 1.3 · Sitemap (structural)

**The question.** What exists on this surface, how is it grouped, and what sits under what?

Brown defines a site map as "A visual representation of the relationships between different pages on a web site", lists its other names ("Also known as a structural model, taxonomy, hierarchy, navigation model, or site structure"), and notes that "site maps increasingly represent page types or templates in addition to (or instead of) specific pages" (Brown 2011, ch. 5). Garrett said the same of his own practice in 2003: he often uses his notation "to diagram navigational relationships between abstract classes of pages" (interview by Dan Brown, Boxes and Arrows, 11 December 2003, [boxesandarrows.com](https://boxesandarrows.com/the-visual-vocabulary-three-years-later-an-interview-with-jesse-james-garrett/)). The structural sitemap this course uses follows them: a box is a page type or a group, and many pages of one type are one box. A page-by-page sitemap of a help centre with four hundred articles has four hundred boxes and shows less structure than one with twelve.

- **Readers.** Product management (scope), engineering (templates and routes), content (where each piece goes), sales (how the website is shown to buyers).
- **Fidelity.** F1 in discovery, top two levels only; F2 in design, every group and page type; F3 for build, with identifiers that engineering and content can cite.
- **Not to be mistaken for:** the navigation. A sitemap "is only a visual display of the hierarchy and organization of your content" (Tankala, NN/g, 2023); the navigation is the interface built on the IA, and on this unit's reading it shows part of the hierarchy at a time and adds routes the hierarchy does not have, such as the "Related Link" lists that Cardello says IA metadata can generate (Cardello, NN/g, 2014). Nor is it the XML file a website publishes for search engines under the Sitemaps protocol ([sitemaps.org/protocol.html](https://www.sitemaps.org/protocol.html)), which shares only the name.

### 1.4 · Navigation model

**The question.** By which routes can a person reach each thing, from where?

Rosenfeld, Morville and Arango split navigation into embedded systems (global, local and contextual navigation) and supplemental systems (sitemaps, indexes, guides, configurators and search) (2015, ch. 8, section headings). In this course's words: global navigation is present everywhere on a surface; local navigation moves within one area; contextual navigation is a link inside content to related content; supplemental navigation stands outside the main structure and lets people reach things another way. A navigation model records which of these routes exist and where each leads. Its natural form is a table: rows are the routes, columns the surfaces.

- **Readers.** Engineering (which components and routes to build), content (which items need contextual links), support (how a customer got somewhere).
- **Fidelity.** F2 in design, before navigation components are chosen; Cardello's recommendation is a first pass at the IA before choosing the components that must hold it (Cardello 2014). F3 is rarely needed: by build time the routes live in the sitemap's identifiers and the screens.
- **Not to be mistaken for:** the menu design. The model says which routes exist; whether a route is a tab bar, a drawer or a link is navigation design (IA1, section 2.1).

### 1.5 · Object map and object-relationship map

**The question.** What things does the system hold, what does each carry, what can people do to it, and how are the things related?

Sophia V. Prater, writing in *A List Apart*, describes object-oriented UX as "putting object design before procedural action design": the objects come from the user's mental model, and the actions are defined after them ("Object-Oriented UX", A List Apart, 20 October 2015, [alistapart.com/article/object-oriented-ux](https://alistapart.com/article/object-oriented-ux/); practice). Her object-mapping method runs in four steps: extract the objects from the nouns in the goals, define each object's core content, nest objects inside each other to find the cross-links (which, she argues, define contextual navigation), and rank each object's elements (same article). Rosenfeld, Morville and Arango's chapter 13 covers a related artefact, content models, for "connecting and managing granular content" (2015, ch. 13). This course draws two grades of the same artefact. An *object map* lists the objects with their attributes and actions. An *object-relationship map* adds the lines between them, each with a verb and a count at each end. The counts use the multiplicity notation of UML, the modelling standard engineering teams already read (Object Management Group, *Unified Modeling Language*, version 2.5.1, December 2017, [omg.org/spec/UML/2.5.1](https://www.omg.org/spec/UML/2.5.1)): 1 is exactly one, 0..* any number including none, 1..* at least one.

- **Readers.** Engineering first (it is the conversation about the data model, held in the user's terms); product management (what the product is made of); the client (whether their own structure, groups, policies and approval chains, fits).
- **Fidelity.** F1 in discovery, nouns and the main lines; F2 in design, every attribute that a screen shows and every action; F3 when it is the agreed mapping to the data model, with each object's model name beside its label.
- **Not to be mistaken for:** the database schema. The map uses the names people meet; the schema uses engineering's names and may split or join things for storage (IA1, section 2.4; Cooper and others, *About Face*, 4th ed., 2014, ch. 1).

### 1.6 · User flow, task flow and wireflow

**The question.** What steps does a person take to reach a goal, and on which screens?

Kate Kaplan defines a user flow as "A set of interactions that describe the typical or ideal set of steps needed to accomplish a common task", performed with a product, and separates it from a user journey, "A scenario-based sequence of the steps that a user takes in order to accomplish a high-level goal" across channels and over time ("User Journeys vs. User Flows", Nielsen Norman Group, 16 April 2023, [nngroup.com/articles/user-journeys-vs-user-flows](https://www.nngroup.com/articles/user-journeys-vs-user-flows/)). Brown's chapter title is Flowcharts, and he gives the other names: "Also known as flows, user flows, process charts"; a flowchart "may not reveal all the details of the interactions, but it does offer a comprehensive view of the user experience for a particular objective" (Brown 2011, ch. 6). Page Laubheimer describes the wireflow: "Wireflows are a combination of wireframes and flowcharts", "well suited for representing dynamic changes on one or few pages inside an app" ("Wireflows: A UX Deliverable for Workflows and Apps", Nielsen Norman Group, 4 December 2016, [nngroup.com/articles/wireflows](https://www.nngroup.com/articles/wireflows/)).

The terms "user flow" and "task flow" are used loosely in practice, and Brown's list of aliases shows that the published sources treat them as one family. This course separates them by scope, as a convention: a **user flow** follows one kind of user from an entry point to a goal, with the branches that kind of user can meet; a **task flow** follows one task along its main path, with no entry points and no branches by user type; a **wireflow** draws a task flow as the screens themselves, when what changes on the screen is the point.

- **Readers.** Engineering and design (what to build, screen by screen); support (where a person can get stuck); product management (where the task starts and ends).
- **Fidelity.** F1 task flows in discovery; F2 user flows in design, with the failure paths; wireflows at F2 to F3 for build of a dynamic screen sequence.
- **Not to be mistaken for:** a journey map, which covers a goal over time and across channels (Kaplan 2023), nor for a decision tree. Kaplan's definition says "typical or ideal": a user flow is the expected path, and the rules that send a person elsewhere belong in a decision tree.

### 1.7 · Decision tree

**The question.** Given these facts, which outcome does the system produce?

Garrett's notation has a symbol for this: the conditional branch, "when the system (not based on user action) must select one path" (Garrett, *Visual Vocabulary Quick Reference*, [jjg.net](http://www.jjg.net/ia/visvocab/files/garrett_ia_quickref.pdf)). In a flow, the branch is one diamond and its outcomes are lines leaving it. A decision tree is that branch drawn out in full: every question the system asks, in order, and every outcome. This course makes it a separate artefact because a benefits platform's hardest IA questions are rules (who may claim what, when an approval is needed), and those rules are invisible in the flow until a person hits one.

- **Readers.** Engineering (the rule to implement); product management and the client (whether the rule is the one they mean); support (why a customer got the outcome they got).
- **Fidelity.** F2 in design; F3 for build, where every branch is complete and every outcome is named as the screen names it.
- **Not to be mistaken for:** a flow. A decision tree has no screens; it is the system's logic, and where that logic waits on a person's decision (HR's approval in section 5.3), that decision is one question box in the person's tone, Garrett's decision point beside his conditional branch. Nor is it a state diagram: a tree decides once; a lifecycle records where a thing is over time.

### 1.8 · State diagram

**The question.** What states can a thing be in, and what moves it from one to the next?

The diagram is older than the web. David Harel's statecharts "extend conventional state-transition diagrams with essentially three elements", which add nested states, parallel components and communication between them ("Statecharts: A Visual Formalism for Complex Systems", *Science of Computer Programming* 8, 1987, pp. 231 to 274). This course uses the plain state-transition diagram: states as boxes, transitions as labelled arrows, a marked start and marked end states. IA1 named the states of a Perqo claim (Perqo, fictional): submitted, approved, rejected, paid (IA1, section 5).

- **Readers.** Engineering (the status field and its allowed changes); content and support (what each status is called on each surface, and what a person can do in it); the client (when money moves).
- **Fidelity.** F2 in design, every state a person can see; F3 for build, every transition with who or what triggers it.
- **Not to be mistaken for:** a flow. A flow is what a person does; a lifecycle is what happens to a thing, whoever acts on it. A claim stays submitted while the employee who made it is asleep.

### 1.9 · Service blueprint

**The question.** For one journey, who does what, in front of the customer and behind, and what supports it?

Sarah Gibbons defines it for NN/g: "A service blueprint is a diagram that visualizes the relationships between different service components", "people, props (physical or digital evidence), and processes", "directly tied to touchpoints in a specific customer journey". Her blueprint has lanes of customer actions, frontstage actions, backstage actions and processes, with evidence as a further layer, separated by the line of interaction, the line of visibility and the line of internal interaction ("Service Blueprints: Definition", Nielsen Norman Group, 27 August 2017, [nngroup.com/articles/service-blueprints-definition](https://www.nngroup.com/articles/service-blueprints-definition/)). The technique goes back to G. Lynn Shostack's "Designing Services That Deliver" (*Harvard Business Review*, January 1984, [hbr.org](https://hbr.org/1984/01/designing-services-that-deliver)); James Kalbach gives it a chapter as one of the primary diagram types (*Mapping Experiences*, 2nd ed., O'Reilly, 2020, ch. 10).

- **Readers.** Support and operations (the backstage work); product management; the client (their own staff are backstage actors).
- **Fidelity.** F1 in discovery, to find where the backstage breaks; F2 when a change to the service is designed. It rarely needs F3; its build detail moves into flows, rules and lifecycles.
- **Not to be mistaken for:** an IA artefact in the narrow sense. It shows people and processes more than structure. It is in this catalogue because it is where the structure's seams show: every crossing of the line of visibility is a place where a label or a status has to mean the same thing on both sides.

### 1.10 · Cross-surface interaction map

**The question.** Across all the surfaces, which things are shared, what does each surface call them, and what passes between surfaces?

This is the course's own artefact, named in the course goal; no standard work defines it under this name. Its ground is the cross-channel problem that the fourth edition of the Polar Bear book wrote into its definition ("digital, physical, and cross-channel ecosystems", Rosenfeld, Morville and Arango 2015, ch. 2) and that Resmini and Rosati made the subject of *Pervasive Information Architecture* (Morgan Kaufmann, 2011). IA1's Perqo surfaces map was its first draft (IA1, Deliverable). The map joins the surfaces to the objects they share: each surface is a box with its top-level areas, each shared object is a box with its name on each surface, and the lines say what crosses. Later units join it to the decision trees and lifecycles, as the course goal says.

- **Readers.** All six: it is the one artefact every touchpoint reads, each for its own row of the vocabulary.
- **Fidelity.** F1 at the start of any work that touches more than one surface; F2 kept current through design; F3 as the canonical vocabulary engineering maps to.
- **Not to be mistaken for:** a sitemap of everything. It holds the top level of each surface and nothing below; the sitemaps hold the rest.

## 2 · The published notations, and what they standardise

A notation is a fixed set of shapes, lines and label rules with a fixed meaning each, so that a reader who has never met the author can read the diagram. Two have standing in this field.

### 2.1 · Garrett's visual vocabulary

Jesse James Garrett's *A visual vocabulary for describing information architecture and interaction design* was first released in October 2000 and revised since ([jjg.net/ia/visvocab](http://www.jjg.net/ia/visvocab/); Brown 2003). Its one-page *Quick Reference* names its elements. The units: "Pages are the fundamental unit of presentation on the Web, not (necessarily) a unit of implementation", and a file is content delivered for use outside the browser. The groups: "A page stack indicates a group of functionally identical pages whose navigational properties are immaterial"; a file stack; "An area is used to identify a group of pages that share one or more common attributes"; conditional areas, flow areas and iterative areas. The logic: "A decision point is used to model when one user action may generate one of a number of results"; "A conditional branch is when the system (not based on user action) must select one path"; conditional selectors, concurrent sets and clusters. The connections: "Relationships between elements are depicted with simple lines"; "Connectors use arrows to convey directionality, indicating how the user will move through the system"; "We use a crossbar on the opposite end of the arrow to prohibit upstream movement"; "A conditional connector is used when a path may or may not be presented to the user"; and "Continuation points allow us to separate our diagrams into easily digestible sections" (Garrett, *Quick Reference*).

What it standardises, then: the units of a structure and a flow, how they group, where the logic branches, and which way a person may move. In the 2003 interview Garrett named two of its properties. It "treats the page as something of a black box": what happens inside a page cannot be drawn. And "the complexity of the representation is proportional to the complexity of the system being described"; he said, "I haven't ever encountered a system I couldn't describe in the vocabulary". He did not ask for conformance: "Take the parts that can help you do your job, don't worry about the rest" (Brown 2003). The article introducing the interview describes the vocabulary as tool-independent, adaptable to any diagramming software and medium (Brown 2003).

What it leaves out, on this unit's reading of the *Quick Reference*: objects and their relationships (it has no element for a thing with attributes), lifecycles (it has decision points but no state), and actors (it has no lane). Those are the three families a product with a backoffice needs most, which is why this course takes its object, state and lane conventions from elsewhere (UML's multiplicities, Harel's state diagrams, Gibbons's blueprint lanes).

### 2.2 · Brown's site maps and flowcharts

Dan Brown's *Communicating Design* (2nd ed., New Riders, 2011, published September 2010) standardises the framing of each artefact: what it is for and whom it serves. Its chapter 2, "Diagram Basics", opens with a section on the "Anatomy of a Design Diagram" and says it "lays a theoretical foundation from which you can build all the diagrams in the first half of this book" (Brown 2011, ch. 2). Each artefact chapter then opens the same way, with an at-a-glance summary and a section on purpose: for site maps, "A site map shows how all the information on a web site fits together. It provides the project team with one view of how the site will be constructed" (ch. 5); for flowcharts, "Flowcharts visualize a process, usually centered around a specific task or function" and, on the web, "often represent a series of screens that collect and display information to the users" (ch. 6).

Two things in those openings matter to a reader of other people's artefacts. Brown's list of other names for a site map, "a structural model, taxonomy, hierarchy, navigation model, or site structure" (ch. 5), puts three of this unit's separate artefacts (sitemap, taxonomy, navigation model) under one name: a team that says "sitemap" may mean any of them. And his note that site maps "increasingly represent page types or templates in addition to (or instead of) specific pages" (ch. 5) means a reader has to find out, for each box, which of the two it is. Section 3 makes both of those into faults to check (faults 1 and 3).

### 2.3 · What the two give this course

Garrett gives the course its symbols for structure and flow, and the principle that a notation is a means to communicate with colleagues. Brown gives it the framing: each artefact says what it is for and for whom, and is one view. Neither covers objects, lifecycles or lanes. Neither covers colour, which matters here because the course's figures use six tones; the accessibility standard sets the constraint: "Color is not used as the only visual means of conveying information", in the words of WCAG 2.2, Success Criterion 1.4.1 (W3C Recommendation, 12 December 2024, [w3.org/TR/WCAG22](https://www.w3.org/TR/WCAG22/)). In this notation every tone's meaning is also carried by words: a lane name, a type tag, a caption.

## 3 · Reading an artefact someone else made: the five faults to look for first

An artefact handed over by another designer, a consultancy or a product manager claims something about the system. The reader's job is to say what it claims and what it leaves out (the course goal). Five faults are the ones to look for first. The list is this unit's synthesis, and each fault is tied to the source that makes it a fault; it is craft practice, not a measured finding.

1. **No stated decision, reader, scope or date.** Brown's "one view" and Tankala's point that a sitemap deliberately leaves detail out (Brown 2011, ch. 5; Tankala 2023) mean an artefact without a stated purpose cannot be judged complete or incomplete. Check first which artefact it is (Brown's aliases mean "sitemap" can name a taxonomy or a navigation model), the decision it supports, its readers, what it leaves out and when it was last true. An undated sitemap of a live product is a claim about some past version of it.
2. **An undeclared or inconsistent notation.** A notation exists so readers share "a common language" (Garrett, in Brown 2003). Look for a legend. Then check that one shape means one thing throughout: a box that is a page in one corner and a feature in another, or an arrow that is a click in one place and a data feed in another, makes every line of the diagram ambiguous.
3. **Mixed levels.** Pages beside page types (Brown 2011, ch. 5), screens beside objects, one area drawn to its leaves beside another drawn to its first level. Garrett's page stack exists to make the level explicit ("functionally identical pages", *Quick Reference*). Mixed levels make a diagram look balanced when the system is not, and make counts meaningless.
4. **Missing conditions and unhappy paths.** Kaplan's definition of a user flow says "typical or ideal" (Kaplan 2023), and a flow drawn to that definition shows only that path. Garrett gave conditions their own symbols (conditional connectors, conditional areas, conditional branches) because whether a path is shown depends on who the user is and what holds. Check what happens to each kind of user, at each rule, and when something fails. If no arrow ends anywhere unpleasant, the artefact has left something out.
5. **Labels that drift from the vocabulary.** The diagram calls a thing one name, the screens another, the help article a third. IA1 set the rule that one thing with two labels is safe only when the mapping is written down (IA1, section 2.4), and Rosenfeld, Morville and Arango write that in many large metadata-driven products controlled vocabularies "have become the glue that holds the systems together" (2015, ch. 10). Check each label against the product and the vocabulary; an unmapped synonym is a defect to report.

## 4 · Editing an artefact without breaking what others rely on

An artefact that has been handed around is depended on: engineering tickets cite its nodes, the content inventory cites its sections, support's articles name its screens, a client has signed off a version of it. Rosenfeld, Morville and Arango describe IA style guides as "capturing your past decisions and guiding your future ones" (2015, ch. 13); an artefact in use is part of that record. The rules below are this course's practice, each with the dependency it protects.

- **Keep identifiers stable.** At F3 every node has an identifier (section 1.0). A moved node keeps it; a removed node's identifier is retired, never reused. Protects: engineering tickets and the content inventory, which cite nodes by identifier.
- **Mark changes as proposed until agreed.** Add the word "proposed" to a new or changed element's note, and leave the current element visible until the change is accepted. Protects: every reader who has already agreed to the current version, including the client.
- **Rename through the vocabulary.** Change a label in the controlled vocabulary first, with the old term kept as a variant, then in the diagrams. Protects: support and search, which still meet the old word from customers; taxonomy terms reach users through search suggestions and filters (Laubheimer 2022).
- **Split rather than cram.** When an addition would double a diagram's size, move a part into its own figure and leave a continuation point to it, Garrett's device for "easily digestible sections" (*Quick Reference*). Protects: the readers who used the diagram at its old size.
- **Keep the notation; extend the legend.** If a new symbol is needed, add it to the legend with its meaning before using it. Garrett's own advice is to take what helps (Brown 2003); the course's rule is that what is taken is declared. Protects: everyone reading section 3's fault 2.
- **Re-stamp the face.** Update the version, the date, the owner and the line saying what the artefact leaves out (IA1, section 4). Protects: the reader who arrives a year later. *Note, 9 November 2026: IA9 (section 4.4) set when a change earns a new version. A change that would break a citation (an identifier retired or moved to another parent, a label renamed, a relationship or transition removed, a rule's outcome changed) makes a new version; any other change is a dated amendment, and each amendment names its decision log entry, so the face reads "version N, dated D; amended D2 (DL-nnn)" (IA9, Deliverable D).*

## 5 · The course notation

### 5.1 · How it is derived, and what it is reduced to

The course notation takes Garrett's units, groups, logic and connections, Brown's framing, UML's multiplicities, Harel's states and Gibbons's lanes, and reduces them to what the course's figure kinds can draw. Every figure in this course is declared as data and drawn at build time by one of a fixed set of kinds: sitemap, tree, objects, flow, wireflow, decision, states, swimlanes and matrix for structure, and further kinds for dates and numbers. A symbol the kinds cannot draw becomes a label rule. The reductions are these:

| Garrett element | In the course notation |
|---|---|
| Page | a box in a sitemap, with a type tag (section 5.2) |
| File | a box tagged `file` |
| Page stack, file stack, iterative area | one box tagged `stack`, with a note saying what repeats |
| Area | a box tagged `section` with its children, or a lane |
| Conditional area | a box whose note opens with the condition in square brackets |
| Decision point, conditional branch | a question box in a decision tree, or a bracketed condition on a flow arrow |
| Connector | a line without a head where it means contains or relates; an arrow where it means movement |
| Arrow with crossbar | an arrow labelled "(no way back)" |
| Conditional connector | an arrow whose label is the condition in square brackets |
| Continuation point | a note "→ see" and the name of the figure or node it continues in |
| Concurrent set, cluster, conditional selector, flow area, flow reference | not drawn; written in the figure's note or the caption |

Two things are added that Garrett did not need: tones, each tied to a surface or a role, and a caption rule.

### 5.2 · The rules

**Tones.** Six tones, each with one meaning, the same in every figure. Tone 1: perqo.com. Tone 2: the merchant side and anything outside Perqo. Tone 3: the Perqo app and the employee. Tone 4: Perqo Admin and the HR and finance managers who use it. Tone 5: shared, meaning the data model, the Perqo system, and any object or term that lives on more than one surface; in a figure of one surface, every box takes that surface's tone, as in the sitemap and the object-relationship map below. Tone 6: a stop, meaning a path that ends without success, or a fault found in a review. Tones are set explicitly wherever a kind would otherwise colour by position (a sitemap gives each first-level branch its own tone by default), because position means nothing in this notation; children inherit their parent's tone. No tone is the only carrier of its meaning (WCAG 2.2, 1.4.1): the surface is also named in the lane, the box or the caption. These six tones keep IA1's assignments for the three surfaces (1, 4 and 3); IA1's other figures predate the notation.

**Shapes.** Each kind's shapes have one meaning. A square-cornered box with a small type tag is a page or page type (sitemap). A box with a filled title band is an object; its attributes sit below the title and its actions after a rule line (objects). An outlined box with branches leaving it is a question; a filled box is an outcome (decision). A rounded box is a state; an inner ring marks an end state; a dot with an arrow marks the start (states). A frame with a title bar is a screen; its bars and blocks are placeholder text and areas, and a button is a control (wireflow). A band across the figure is a lane: one actor or surface, and the steps in it are theirs (swimlanes). A plain box in a tree is a term or a group. In a matrix, a row is an item, a column a dimension, and a marked cell the value where they meet.

**Lines.** A line without a head means contains (sitemap, tree) or relates (objects); a small solid triangle beside a relationship's label is not a head, and shows only which way the label reads (see **Labels**). An arrow means movement or change: a person moves, the system acts, a state changes. An arrow from a box back to itself is an action that leaves the thing as it was. Nothing is drawn dashed; a condition is written.

**Labels.** Box labels are the product's own words, as they appear on the surface, in sentence case. Page-type tags come from a fixed list: `home`, `section` (a landing page for a group), `index` (a list of items), `detail` (one item), `stack` (many pages of one type), `form`, `file`, `external` (leaves this surface). An arrow's label in a flow is the person's action ("tap Submit") or the system's event ("pay out"). A relationship's label is a verb that reads from left to right on a level line and from top to bottom otherwise ("submits"), with a count at each end; the boxes are placed so that every label reads that way where they can, and a label that cannot carries a small solid triangle pointing at the object it reads towards. An object's action reads "-> verb". A condition is written in square brackets. In decision trees the branch labels are "yes" and "no", "yes" always on the left. Status words go in a note: "assumed" for a fact not yet evidenced, "proposed" for a change not yet agreed. On a shared object, the data-model name is the title, in lower case, and each surface's name is a line "Surface: Label", which is IA1's vocabulary mapping drawn (IA1, section 2.4).

**Captions.** Every figure's caption names the artefact, says what it shows and the decision it supports, names the section of the unit it draws and the sources cited there, and for Perqo says that Perqo is fictional.

The legend, drawn in the notation's own matrix kind:

```viz
{"kind": "matrix", "caption": "The course notation: legend (section 5.2); supports reading and drawing every figure from IA3 on. Shapes, lines and label rules as set in section 5.2, derived from Garrett's Visual Vocabulary Quick Reference, Brown, Communicating Design, 2nd ed., 2011, chs 5 and 6, UML 2.5.1 multiplicities, Harel 1987 and Gibbons 2017. The tones are added (section 5.1); neither Garrett nor Brown covers colour (section 2.3), and no tone is the only carrier of its meaning (WCAG 2.2, 1.4.1). Perqo is fictional. The six tone rows show each tone; the rows below them are drawn in tone 5 only because the figure kind colours every cell, and there the tone carries no meaning.", "cols": ["Drawn as", "Means"], "rows": [{"label": "Tone 1", "tone": 1, "cells": ["tone 1", "perqo.com"]}, {"label": "Tone 2", "tone": 2, "cells": ["tone 2", "the merchant side and anything outside Perqo"]}, {"label": "Tone 3", "tone": 3, "cells": ["tone 3", "the Perqo app and the employee"]}, {"label": "Tone 4", "tone": 4, "cells": ["tone 4", "Perqo Admin and the HR and finance managers who use it"]}, {"label": "Tone 5", "tone": 5, "cells": ["tone 5", "shared: the data model, the Perqo system, any object or term on more than one surface; in a figure of one surface, every box takes that surface's tone"]}, {"label": "Tone 6", "tone": 6, "cells": ["tone 6", "a stop: a path that ends without success, or a fault found in a review"]}, {"label": "Page or page type", "tone": 5, "cells": ["square-cornered box with a type tag", "one page, or one type of page; the tag names the type"]}, {"label": "Object", "tone": 5, "cells": ["box with a filled title band", "a thing the system holds; attributes below, actions after the rule line"]}, {"label": "Surface", "tone": 5, "cells": ["box with a filled title band, in a surface's tone", "one surface in a cross-surface map; its top-level areas below the title"]}, {"label": "Question", "tone": 5, "cells": ["outlined box with branches", "a question the system asks, or a decision a named person makes"]}, {"label": "Outcome", "tone": 5, "cells": ["filled box", "where a decision ends"]}, {"label": "State", "tone": 5, "cells": ["rounded box", "a state; inner ring: an end state; dot and arrow: the start"]}, {"label": "Screen", "tone": 5, "cells": ["frame with a title bar", "one screen; bars and blocks are placeholders, and a button is a control"]}, {"label": "Lane", "tone": 5, "cells": ["band across the figure", "one actor or surface; the steps in it are theirs"]}, {"label": "Term or group", "tone": 5, "cells": ["plain box in a tree", "a term or a group in a hierarchy"]}, {"label": "Row, column, cell", "tone": 5, "cells": ["matrix", "an item, a dimension, the value where they meet"]}, {"label": "Line without a head", "tone": 5, "cells": ["plain line", "contains or relates"]}, {"label": "Arrow", "tone": 5, "cells": ["line with a head", "movement or change: a person moves, the system acts, a state changes"]}, {"label": "Arrow to itself", "tone": 5, "cells": ["arrow from a box back to itself", "an action that leaves the thing as it was"]}, {"label": "No dashed lines", "tone": 5, "cells": ["nothing is drawn dashed", "a condition is written"]}, {"label": "Type tag", "tone": 5, "cells": ["home, section, index, detail, stack, form, file, external", "the page's type"]}, {"label": "Relationship label", "tone": 5, "cells": ["verb on a line", "reads from left to right on a level line, from top to bottom otherwise, unless a triangle marks the other way"]}, {"label": "Triangle by a label", "tone": 5, "cells": ["small solid triangle by a relationship label", "the label reads towards the object the triangle points at"]}, {"label": "yes, no", "tone": 5, "cells": ["branch labels", "yes always on the left"]}, {"label": "Surface: Label", "tone": 5, "cells": ["line in a shared object", "that surface's name for it; the title is the data-model name, in lower case"]}, {"label": "[condition]", "tone": 5, "cells": ["square brackets", "the path or the box exists only when this holds"]}, {"label": "1, 0..*, 1..*", "tone": 5, "cells": ["count at a line's end", "exactly one; any number including none; at least one"]}, {"label": "-> verb", "tone": 5, "cells": ["line in an object box", "an action someone can take on the object"]}, {"label": "→ see", "tone": 5, "cells": ["note", "continues in another figure or node"]}, {"label": "(no way back)", "tone": 5, "cells": ["arrow label", "the person cannot return along this arrow"]}, {"label": "assumed, proposed", "tone": 5, "cells": ["word in a note", "not yet evidenced; not yet agreed"]}]}
```

### 5.3 · The notation at work: one example per family

Each example below is small on purpose: one Perqo fragment (Perqo, fictional) per family, enough to show the rules. Later units build each artefact in full.

**Inventories and vocabularies.** This family is drawn as tables, and the notation's rules for it are the table rules in the notation sheet below: one row per item, a stable identifier first, the product's own words in the label column, status words in the last column. A slice of the perqo.com Help centre inventory with its audit (Perqo, fictional), using Kaley's fields and her keep, update or remove outcome (Kaley 2020). The Help centre is split by audience and then by task, as IA1 set it (IA1, section 2.3); support owns the articles.

| ID | Title | URL | Owner | Topic | Format | Last modified | Audit |
|---|---|---|---|---|---|---|---|
| H-2.1.1 | How to claim back a receipt | perqo.com/help/employees/claims/claim-a-receipt | Support | Claims | article | 2026-09-14 | keep |
| H-2.1.2 | Why was my claim rejected? | perqo.com/help/employees/claims/claim-rejected | Support | Claims | article | 2025-11-03 | update: says "refund", the app says Claim |
| H-2.2.1 | Your balance explained | perqo.com/help/employees/balance | Support | Balance | article | 2026-02-20 | keep |
| H-1.1.1 | Setting a budget for an employee group | perqo.com/help/hr-finance/budgets/set-a-budget | Support | Budgets | article | 2026-06-01 | keep |
| H-1.2.4 | Approval rules | perqo.com/help/hr-finance/policies/approval-rules.pdf | Product | Policies | file | 2024-05-10 | remove: replaced by an article |

And a slice of the controlled vocabulary (Perqo, fictional): the preferred term in each surface's words, the variant terms people use, and the hierarchy of the benefit categories. The four categories are IA1's; the narrower terms are new here.

| Preferred term (app) | Admin term | Variant terms | Broader term | Narrower terms |
|---|---|---|---|---|
| Claim | Claim | refund, reimbursement, expense | transaction (data model) | none |
| Balance | Budget | allowance, credit | allocation (data model) | none |
| Health | Health | wellbeing | Benefit category | Fitness, Therapy |
| Learning | Learning | education, training | Benefit category | Courses, Books |
| Mobility | Mobility | transport, commuting | Benefit category | Public transport, Bike |
| Meals | Meals | food | Benefit category | Restaurants, Groceries |

**Structure.** The perqo.com sitemap at F2 (Perqo, fictional). Home leads to Product, Pricing, Customers, Help centre, Book a demo and Sign in. Product has one page each for Perqo Admin, Perqo app and Perqo card. Customers is an index over Customer stories, one page per client. The Help centre splits into For HR and finance teams and For employees, then by task, as the inventory's URLs show: Budgets and Policies under For HR and finance teams, Claims and Balance under For employees, each a stack of its articles (Budget articles, Policy articles, Claim articles, Balance articles). Sign in leaves the website for Perqo Admin. Every box is tone 1, because the whole map is one surface.

```viz
{"kind": "sitemap", "caption": "Sitemap (structure family): the perqo.com structure at F2, page types tagged and many-of-a-kind pages drawn as one stack; supports the decision on where a new page belongs (section 5.3). Perqo is fictional; Help centre split from IA1, section 2.3; page-type and stack conventions from Brown 2011, ch. 5, and Garrett's Quick Reference.", "stack_from": 2, "root": {"label": "Home", "type": "home", "tone": 1, "children": [{"label": "Product", "type": "section", "tone": 1, "children": [{"label": "Perqo Admin", "type": "detail"}, {"label": "Perqo app", "type": "detail"}, {"label": "Perqo card", "type": "detail"}]}, {"label": "Pricing", "type": "detail", "tone": 1}, {"label": "Customers", "type": "index", "tone": 1, "children": [{"label": "Customer stories", "type": "stack", "note": "one page per client"}]}, {"label": "Help centre", "type": "index", "tone": 1, "children": [{"label": "For HR and finance teams", "type": "section", "children": [{"label": "Budgets", "type": "section", "children": [{"label": "Budget articles", "type": "stack"}]}, {"label": "Policies", "type": "section", "children": [{"label": "Policy articles", "type": "stack"}]}]}, {"label": "For employees", "type": "section", "children": [{"label": "Claims", "type": "section", "children": [{"label": "Claim articles", "type": "stack"}]}, {"label": "Balance", "type": "section", "children": [{"label": "Balance articles", "type": "stack"}]}]}]}, {"label": "Book a demo", "type": "form", "tone": 1}, {"label": "Sign in", "type": "external", "note": "→ see Perqo Admin", "tone": 1}]}}
```

The navigation model for the same fragment is a table (Perqo, fictional; route types from Rosenfeld, Morville and Arango 2015, ch. 8):

| Route type | perqo.com | Perqo Admin | Perqo app |
|---|---|---|---|
| Global | Product, Pricing, Customers, Help centre, Book a demo, Sign in, on every page | Employees, Budgets, Policies, Approvals, Reports, Settings | Home, Benefits, Claims, Card, Account |
| Local | the audience sections inside the Help centre | the policies inside Policies, one per employee group | the four categories inside Benefits |
| Contextual | from a help article to the related task's articles | from an employee's record to the claims they made | from the Claims screen to the claim articles in the Help centre |
| Supplemental | search inside the Help centre | none | none |

The global routes are IA1's top-level areas, with Book a demo added on perqo.com; the contextual routes from an employee's record to their claims and from the app's Claims screen to the Help centre are IA1's (sections 2.2 and 2.3); the rest are new here.

**Objects.** The core objects of Perqo Admin as an object-relationship map at F2 (Perqo, fictional). An employee group follows one policy, and the policy belongs to that group. The group contains its employees. Finance sets budgets per employee group and period (IA1, section 5), and each employee holds one per open category and period: the allocation that IA1 mapped to Budget in Admin and Balance in the app (IA1, section 2.4). An employee submits claims; each claim is checked against the group's policy and spends from a budget. The policy carries its open categories and an auto-approve limit: a claim at or under the limit is approved without HR, a claim over it waits in Approvals. An employee group carries its name; an employee, a name and a work email; a budget, an amount for one category and period; a claim, an amount, a category, a receipt and a status. A group contains one or more employees (1..*); an employee submits any number of claims, including none (0..*); and any number of claims are checked against one policy and spend from one budget. The actions are the ones HR and finance take: edit a policy, invite employees, move an employee to a group, set a budget, approve or reject a claim.

```viz
{"kind": "objects", "caption": "Object-relationship map (objects family): the core objects of Perqo Admin with attributes, actions and counts at F2, every box in tone 4 because the figure shows one surface; supports the decision on what Admin holds and how its parts relate (section 5.3). Each relationship reads from left to right on a level line, from top to bottom otherwise. Perqo is fictional; relationships and attributes from this section and IA1, section 5; counts in UML 2.5.1 multiplicity notation; object-first method from Prater 2015.", "objects": [{"id": "policy", "title": "Policy", "tone": 4, "attrs": ["open categories", "auto-approve limit"], "actions": ["-> edit"]}, {"id": "group", "title": "Employee group", "tone": 4, "attrs": ["name"], "actions": ["-> invite employees"]}, {"id": "claim", "title": "Claim", "tone": 4, "attrs": ["amount", "category", "receipt", "status"], "actions": ["-> approve", "-> reject"]}, {"id": "employee", "title": "Employee", "tone": 4, "attrs": ["name", "work email"], "actions": ["-> move to group"]}, {"id": "budget", "title": "Budget", "tone": 4, "attrs": ["amount", "category", "period"], "actions": ["-> set"]}], "rows": [["group", "employee", null], [null, "claim", "budget"], ["policy", null, null]], "links": [{"from": "group", "to": "policy", "label": "follows", "from_card": "1", "to_card": "1"}, {"from": "group", "to": "employee", "label": "contains", "from_card": "1", "to_card": "1..*"}, {"from": "employee", "to": "claim", "label": "submits", "from_card": "1", "to_card": "0..*"}, {"from": "claim", "to": "policy", "label": "is checked against", "from_card": "0..*", "to_card": "1"}, {"from": "claim", "to": "budget", "label": "spends from", "from_card": "0..*", "to_card": "1"}, {"from": "employee", "to": "budget", "label": "holds", "from_card": "1", "to_card": "1..*"}]}
```

**Flows.** Submitting a claim in the Perqo app as a wireflow at F2 (Perqo, fictional). From the Claims screen, which lists claims by status (Submitted, Paid), the employee taps New claim. The New claim screen asks for a category (only the categories open to their group appear), an amount and a receipt; they tap Continue. Check and submit shows the category and amount and the balance after the claim; from there they can tap Edit, which returns to New claim, or tap Submit, after which there is no way back to edit. Claim submitted shows the status, Submitted. What happens next is the claim's lifecycle, drawn below.

```viz
{"kind": "wireflow", "caption": "Wireflow (flows family): an employee submits a claim in the Perqo app, F2; supports the decision on which screens the task needs and where it cannot be undone (section 5.3). Perqo is fictional; wireflow form from Laubheimer, NN/g, 2016; the no-way-back label stands for Garrett's crossbar (Quick Reference).", "per_row": 4, "screens": [{"id": "list", "title": "Claims", "tone": 3, "lines": ["Submitted", {"bar": 0.8}, "Paid", {"bar": 0.6}, {"button": "New claim"}]}, {"id": "form", "title": "New claim", "tone": 3, "lines": ["Category", {"bar": 0.7}, "Amount", {"bar": 0.4}, "Receipt", {"block": 30}, {"button": "Continue"}]}, {"id": "review", "title": "Check and submit", "tone": 3, "lines": ["Category and amount", {"bar": 0.7}, "Balance after", {"bar": 0.5}, {"button": "Edit"}, {"button": "Submit"}]}, {"id": "done", "title": "Claim submitted", "tone": 3, "lines": ["Status: Submitted", "→ see claim lifecycle"]}], "links": [{"from": "list", "to": "form", "label": "tap New claim"}, {"from": "form", "to": "review", "label": "tap Continue"}, {"from": "review", "to": "form", "label": "tap Edit"}, {"from": "review", "to": "done", "label": "tap Submit (no way back)"}]}
```

**Rules.** What the Perqo system decides when a claim is submitted, as a decision tree at F2 (Perqo, fictional). First: is the amount within the employee's balance? If not, the claim is rejected, over balance. If it is: is the amount at or under the policy's auto-approve limit? If so, it is approved automatically. If not, it waits in Approvals, where HR decides: if HR approves, it is approved; if not, it is rejected by HR. The questions the system asks and the approvals are tone 5, the Perqo system; HR's question is tone 4, Admin; the two rejections are tone 6, the stops.

```viz
{"kind": "decision", "caption": "Decision tree (rules family): how the Perqo system routes a submitted claim, F2; supports the decision on which claims need HR (section 5.3). Perqo is fictional; the auto-approve limit as set in this section; a decision tree is Garrett's conditional branch drawn out in full (Quick Reference).",
 "root": {"q": "Amount within the employee's balance?", "tone": 5, "branches": [
  {"label": "yes", "to": {"q": "At or under the policy's auto-approve limit?", "tone": 5, "branches": [
    {"label": "yes", "to": {"outcome": "Approved automatically", "tone": 5}},
    {"label": "no", "to": {"q": "Waits in Approvals: HR approves?", "tone": 4, "branches": [
      {"label": "yes", "to": {"outcome": "Approved", "tone": 5}},
      {"label": "no", "to": {"outcome": "Rejected by HR", "tone": 6}}]}}]}},
  {"label": "no", "to": {"outcome": "Rejected, over balance", "tone": 6}}]}}
```

**Lifecycles.** The same claim as a state diagram at F2 (Perqo, fictional), with IA1's four states. A claim starts as Submitted; a claim over the auto-approve limit stays there while it waits in Approvals. It moves to Approved when it is approved, by the rule or by HR, and from Approved to Paid when Perqo pays out. From Submitted it can instead move to Rejected, by the rule or by HR. Paid and Rejected are end states. Submitted, Approved and Paid are tone 5, because a claim's status is shown on both Admin and the app; Rejected is tone 6, a stop.

```viz
{"kind": "states", "caption": "State diagram (rules and lifecycles family): the lifecycle of a Perqo claim, F2; supports the decision on which statuses each surface shows and what moves a claim between them (section 5.3). Perqo is fictional; the four states from IA1, section 5; the plain state-transition form that Harel 1987 extends.", "per_row": 3, "states": [{"id": "submitted", "label": "Submitted", "note": "[over limit] waits in Approvals", "tone": 5}, {"id": "approved", "label": "Approved", "tone": 5}, {"id": "paid", "label": "Paid", "tone": 5, "end": true}, {"id": "rejected", "label": "Rejected", "tone": 6, "end": true}], "transitions": [{"from": "submitted", "to": "approved", "label": "approve, by rule or HR"}, {"from": "approved", "to": "paid", "label": "pay out"}, {"from": "submitted", "to": "rejected", "label": "reject, by rule or HR"}]}
```

**Journeys across actors and surfaces: the service blueprint.** One claim over the auto-approve limit, as a blueprint at F1 (Perqo, fictional), in Gibbons's four lanes (Gibbons 2017). In the employee actions lane, the employee pays for a course and keeps the receipt (the evidence), then submits the claim. Frontstage, the Perqo app's New claim form is what they use. Backstage, out of the employee's sight, HR approves in Approvals. Under both, the Perqo system checks policy and balance, sends the claim to HR when it is over the limit, pays out once it is approved, and the app shows Paid. The line of visibility runs between the frontstage and backstage lanes; the swimlanes kind draws every lane boundary alike, so the lane names carry it.

```viz
{"kind": "swimlanes", "caption": "Service blueprint (journeys family): one Perqo claim over the auto-approve limit, F1; supports the decision on where the backstage work sits and where it crosses the line of visibility (section 5.3). Perqo is fictional; lanes from Gibbons, 'Service Blueprints: Definition', NN/g, 2017.",
 "lanes": [
  {"id": "emp", "label": "Employee actions", "tone": 3},
  {"id": "app", "label": "Frontstage: Perqo app", "tone": 3},
  {"id": "hr", "label": "Backstage: HR in Perqo Admin", "tone": 4},
  {"id": "sys", "label": "Processes: Perqo system", "tone": 5}
 ],
 "steps": [
  {"id": "pay", "lane": "emp", "col": 0, "label": "Pays for a course", "note": "evidence: receipt"},
  {"id": "sub", "lane": "emp", "col": 1, "label": "Submits claim"},
  {"id": "form", "lane": "app", "col": 1, "label": "New claim form"},
  {"id": "rule", "lane": "sys", "col": 2, "label": "Checks policy and balance"},
  {"id": "appr", "lane": "hr", "col": 3, "label": "Approves in Approvals"},
  {"id": "out", "lane": "sys", "col": 4, "label": "Pays out"},
  {"id": "paid", "lane": "app", "col": 5, "label": "Shows Paid"}
 ],
 "links": [
  {"from": "pay", "to": "sub"},
  {"from": "sub", "to": "form", "label": "uses"},
  {"from": "form", "to": "rule", "label": "submit"},
  {"from": "rule", "to": "appr", "label": "[over limit]"},
  {"from": "appr", "to": "out", "label": "approve"},
  {"from": "out", "to": "paid", "label": "status Paid"}
 ]}
```

**Journeys across actors and surfaces: the cross-surface interaction map.** IA1's Perqo surfaces map, redrawn in the notation at F1 (section 1.10: F1 at the start of any work that touches more than one surface), with three of the five shared objects in IA1's vocabulary table (allocation, transaction of type claim, and policy) added as boxes of their own (IA1, Deliverable). The three surfaces keep their top-level areas and their actions, and the lines between them say what IA1's table says crosses: perqo.com passes a signed contract and signed-in users to Admin, and the download link and help articles to the app (IA1, Deliverable). IA1's single line from Admin to the app, "budgets, policies, invites, decisions", is split: Admin still passes invites and decisions to the app directly; budgets and policies now pass through the shared objects that carry them. Admin sets the allocation, which the app shows as Balance; Admin sets the policy, which the app does not show as such; the app shows the policy's effect as open categories and approval rules. The app submits claims; a claim is checked against the policy and spends from the allocation, and Admin approves in Approvals the claims over the limit. As in the object-relationship map above, any number of claims (0..*) are checked against one policy (1) and spend from one allocation (1). Each shared box lists its name on each surface as IA1's vocabulary table gives it (on perqo.com: Policies, Claims, Benefits budget), in tone 5. This is the start of the course's cross-surface interaction map; later units add the decision trees and lifecycles to it.

```viz
{"kind": "objects", "caption": "Cross-surface interaction map (journeys family): IA1's Perqo surfaces map redrawn in the course notation, with three shared objects and their names on each surface, F1 (section 1.10); tones as in section 5.2: perqo.com tone 1, Perqo Admin tone 4, Perqo app tone 3, shared objects tone 5; supports the decision on which surface and under which name a thing belongs (section 5.3). Lines read from left to right on a level line, from top to bottom otherwise, unless a triangle marks the other way. Perqo is fictional; surfaces, top-level areas, actions, what passes between the surfaces and each surface's names from IA1, Deliverable; the lines to the shared objects, the split of IA1's Admin-to-app line, the counts and the condition from this section.", "objects": [{"id": "site", "title": "perqo.com", "tone": 1, "attrs": ["Product", "Pricing", "Customers", "Help centre", "Sign in"], "actions": ["-> book a demo", "-> find help"]}, {"id": "admin", "title": "Perqo Admin", "tone": 4, "attrs": ["Employees", "Budgets", "Policies", "Approvals", "Reports", "Settings"], "actions": ["-> configure", "-> approve", "-> report"]}, {"id": "app", "title": "Perqo app", "tone": 3, "attrs": ["Home", "Benefits", "Claims", "Card", "Account"], "actions": ["-> see balance", "-> spend", "-> claim"]}, {"id": "policy", "title": "policy", "tone": 5, "attrs": ["Admin: Policy", "app: not shown", "perqo.com: Policies"]}, {"id": "claim", "title": "transaction, type claim", "tone": 5, "attrs": ["Admin: Claim", "app: Claim", "perqo.com: Claims"]}, {"id": "alloc", "title": "allocation", "tone": 5, "attrs": ["Admin: Budget", "app: Balance", "perqo.com: Benefits budget"]}], "rows": [["site", "admin", null, null], [null, null, null, "policy"], [null, "app", null, "claim"], ["alloc", null, null, null]], "links": [{"from": "admin", "to": "claim", "label": "approves in Approvals [over the limit]"}, {"from": "site", "to": "admin", "label": "passes a signed contract and signed-in users to"}, {"from": "site", "to": "app", "label": "passes the download link and help articles to"}, {"from": "admin", "to": "app", "label": "passes invites and decisions to"}, {"from": "app", "to": "claim", "label": "submits"}, {"from": "claim", "to": "policy", "label": "is checked against", "from_card": "0..*", "to_card": "1", "dir": "to"}, {"from": "claim", "to": "alloc", "label": "spends from", "from_card": "0..*", "to_card": "1"}, {"from": "admin", "to": "alloc", "label": "sets"}, {"from": "admin", "to": "policy", "label": "sets"}, {"from": "app", "to": "alloc", "label": "shows as Balance"}, {"from": "app", "to": "policy", "label": "shows the policy's effect as open categories and approval rules", "dir": "to"}]}
```

## Deliverable · The course notation sheet

*One page. Every figure in this course from IA3 on uses it. Put it beside any artefact you hand over, or cite it in the artefact's caption.*

**Tones** (section 5.2). One meaning each; set on every element; never the only carrier of the meaning (WCAG 2.2, 1.4.1).

| Tone | Means |
|---|---|
| 1 | perqo.com |
| 2 | the merchant side and anything outside Perqo |
| 3 | the Perqo app and the employee |
| 4 | Perqo Admin and the HR and finance managers who use it |
| 5 | shared: the data model, the Perqo system, any object or term on more than one surface; in a figure of one surface, every box takes that surface's tone |
| 6 | a stop: a path that ends without success, or a fault found in a review |

**Shapes** (section 5.2; units from Garrett's *Quick Reference*).

| Symbol | Kind | Means |
|---|---|---|
| Square-cornered box with a type tag | sitemap | one page or one type of page (Garrett: page) |
| Box tagged `stack`, note says what repeats | sitemap | many pages of one type (Garrett: page stack, iterative area) |
| Box tagged `section` with children | sitemap | a group of pages that share something (Garrett: area) |
| Plain box | tree | a term or a group in a hierarchy |
| Box with a filled title band | objects | a thing the system holds; attributes below the title |
| Line after the attributes, then "-> verb" lines | objects | the actions someone can take on it |
| Box with a filled title band, in a surface's tone | objects | one surface in a cross-surface map; its top-level areas below the title |
| Outlined box with branches | decision | a question the system asks, or a decision a named person makes (Garrett: conditional branch; decision point) |
| Filled box | decision | an outcome, where the decision ends |
| Rounded box | states | a state |
| Rounded box with an inner ring | states | an end state |
| Dot with an arrow | states | the start |
| Frame with a title bar | wireflow | one screen |
| Bar, block, button inside a frame | wireflow | placeholder text, placeholder area, a control |
| Band across the figure with a name | swimlanes | one actor or surface; the steps in it are theirs |
| Box in a lane | swimlanes | one step by that actor or on that surface |
| Row, column, marked cell | matrix | an item, a dimension, the value where they meet |

**Lines** (section 5.2; connectors from Garrett's *Quick Reference*).

| Symbol | Means |
|---|---|
| Line without a head (sitemap, tree) | contains: the lower box is inside the upper |
| Line without a head (objects) | relates; read its label from left to right on a level line, from top to bottom otherwise, unless a triangle by the label marks the other way |
| Small solid triangle by a relationship label | the label reads towards the object the triangle points at; it is not a head |
| Arrow | movement or change: a person moves, the system acts, a state changes (Garrett: connector with arrow) |
| Arrow from a box back to itself | the action leaves the thing in the same state |
| No dashed lines | a condition is written, never drawn |

**Labels** (section 5.2).

| Rule | Means |
|---|---|
| Box label in the product's own words, sentence case | what the person sees on that surface |
| Type tag: `home`, `section`, `index`, `detail`, `stack`, `form`, `file`, `external` | the page's type: home page; landing page of a group; list of items; one item; many pages of one type; form; file for use outside the browser; leaves this surface |
| Flow arrow label: an action or an event | what the person does ("tap Submit") or what the system does ("pay out") |
| Relationship label: a verb, read from left to right on a level line, from top to bottom otherwise, or towards the object a triangle by it points at | how the two objects relate ("submits") |
| 1, 0..*, 1..* at a line's end | exactly one; any number including none; at least one (UML multiplicity) |
| [condition] | the path or the box exists only when this holds (Garrett: conditional connector, conditional area) |
| "yes" left, "no" right | branch order in every decision tree |
| (no way back) | the person cannot return along this arrow (Garrett: crossbar) |
| → see *name* | continues in that figure or node (Garrett: continuation point) |
| "assumed" in a note | a fact not yet evidenced |
| "proposed" in a note | a change not yet agreed |
| Data-model name in lower case, surface names as "Surface: Label" | the vocabulary mapping on a shared object (IA1, section 2.4) |

**Tables** (inventories and vocabularies; section 5.3).

| Rule | Means |
|---|---|
| Stable identifier in the first column | the item's address; kept when the item moves, retired when it is removed |
| Label column in the product's own words | what the person sees |
| Status in the last column: keep, update, remove (inventories) | the audit outcome (Kaley 2020); an update names what changes |
| Preferred term, variant terms, broader term, narrower terms (vocabularies) | equivalence and hierarchy (Rosenfeld, Morville and Arango 2015, ch. 10) |

**The face of every artefact** (IA1, section 4; section 4 of this unit).

| Field | Means |
|---|---|
| Artefact name and family | what kind of view this is |
| Decision it supports | the question it answers |
| Readers | which of the six touchpoints it is for |
| Leaves out | what a reader must not look for in it |
| Fidelity | F1 sketch, F2 working, F3 specification (section 1.0) |
| Owner, version, date, amendments (DL-) | who keeps it, when it was last true, and each dated amendment with its decision log entry (IA9, section 4.4; note, 9 November 2026) |
| Sources and the Perqo label | where its facts come from; "Perqo is fictional" for the running example |

## Deliverable · The artefact decision table

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

## Sources

- Brown, Dan M. *Communicating Design: Developing Web Site Documentation for Design and Planning*. 2nd ed. New Riders, 2011 (published September 2010). Chs 2, 3 to 7; ch. 5, Site Maps; ch. 6, Flowcharts. Contents at [informit.com](https://www.informit.com/store/communicating-design-developing-web-site-documentation-9780321712462).
- Brown, Dan. "The Visual Vocabulary Three Years Later: An Interview with Jesse James Garrett". Boxes and Arrows, 11 December 2003. [boxesandarrows.com/the-visual-vocabulary-three-years-later-an-interview-with-jesse-james-garrett](https://boxesandarrows.com/the-visual-vocabulary-three-years-later-an-interview-with-jesse-james-garrett/) (interview; practice).
- Cardello, Jen. "The Difference Between Information Architecture (IA) and Navigation". Nielsen Norman Group, 22 June 2014. [nngroup.com/articles/ia-vs-navigation](https://www.nngroup.com/articles/ia-vs-navigation/)
- Cooper, Alan, Robert Reimann, David Cronin and Christopher Noessel. *About Face: The Essentials of Interaction Design*. 4th ed. Wiley, 2014. Ch. 1.
- Garrett, Jesse James. "A visual vocabulary for describing information architecture and interaction design". First released October 2000, revised since. [jjg.net/ia/visvocab](http://www.jjg.net/ia/visvocab/)
- Garrett, Jesse James. *Visual Vocabulary Quick Reference*. Undated one-page PDF. [jjg.net/ia/visvocab/files/garrett_ia_quickref.pdf](http://www.jjg.net/ia/visvocab/files/garrett_ia_quickref.pdf)
- Gibbons, Sarah. "Service Blueprints: Definition". Nielsen Norman Group, 27 August 2017. [nngroup.com/articles/service-blueprints-definition](https://www.nngroup.com/articles/service-blueprints-definition/)
- Harel, David. "Statecharts: A Visual Formalism for Complex Systems". *Science of Computer Programming* 8 (1987): 231 to 274.
- Hedden, Heather. *The Accidental Taxonomist*. 3rd ed. Information Today, 2022. [books.infotoday.com](https://books.infotoday.com/Ebooks/489_The-Accidental-Taxonomist-Third-Edition.htm)
- Kaley, Anna. "Content Inventory and Auditing 101". Nielsen Norman Group, 27 September 2020. [nngroup.com/articles/content-audits](https://www.nngroup.com/articles/content-audits/)
- Kalbach, James. *Mapping Experiences: A Complete Guide to Customer Alignment Through Journeys, Blueprints, and Diagrams*. 2nd ed. O'Reilly, 2020. Ch. 10, Service Blueprints. [oreilly.com](https://www.oreilly.com/library/view/mapping-experiences-2nd/9781492076629/)
- Kaplan, Kate. "User Journeys vs. User Flows". Nielsen Norman Group, 16 April 2023. [nngroup.com/articles/user-journeys-vs-user-flows](https://www.nngroup.com/articles/user-journeys-vs-user-flows/)
- Laubheimer, Page. "Wireflows: A UX Deliverable for Workflows and Apps". Nielsen Norman Group, 4 December 2016. [nngroup.com/articles/wireflows](https://www.nngroup.com/articles/wireflows/)
- Laubheimer, Page. "Taxonomy 101: Definition, Best Practices, and How It Complements Other IA Work". Nielsen Norman Group, 3 July 2022. [nngroup.com/articles/taxonomy-101](https://www.nngroup.com/articles/taxonomy-101/)
- NISO. *ANSI/NISO Z39.19-2005 (R2010): Guidelines for the Construction, Format, and Management of Monolingual Controlled Vocabularies*. National Information Standards Organization, 2005, reaffirmed 2010 (standard). [niso.org/publications/ansiniso-z3919-2005-r2010](https://niso.org/publications/ansiniso-z3919-2005-r2010)
- Object Management Group. *Unified Modeling Language*, version 2.5.1. December 2017 (standard). [omg.org/spec/UML/2.5.1](https://www.omg.org/spec/UML/2.5.1)
- Prater, Sophia V. "Object-Oriented UX". A List Apart, 20 October 2015. [alistapart.com/article/object-oriented-ux](https://alistapart.com/article/object-oriented-ux/) (practice).
- Resmini, Andrea, and Luca Rosati. *Pervasive Information Architecture: Designing Cross-Channel User Experiences*. Morgan Kaufmann, 2011.
- Rosenfeld, Louis, Peter Morville and Jorge Arango. *Information Architecture: For the Web and Beyond*. 4th ed. O'Reilly, 2015. Chs 2, 8, 10, 13. Contents at [oreilly.com](https://www.oreilly.com/library/view/information-architecture-4th/9781491913529/).
- Shostack, G. Lynn. "Designing Services That Deliver". *Harvard Business Review*, January 1984. [hbr.org/1984/01/designing-services-that-deliver](https://hbr.org/1984/01/designing-services-that-deliver)
- Sitemaps.org. "Sitemaps XML format" (protocol documentation, page dated 21 November 2016). [sitemaps.org/protocol.html](https://www.sitemaps.org/protocol.html)
- Tankala, Samhita. "Information Architecture vs. Sitemaps". Nielsen Norman Group, 3 September 2023. [nngroup.com/articles/information-architecture-sitemaps](https://www.nngroup.com/articles/information-architecture-sitemaps/)
- W3C. *Web Content Accessibility Guidelines (WCAG) 2.2*. W3C Recommendation, 12 December 2024 (standard). Success Criterion 1.4.1, Use of Color. [w3.org/TR/WCAG22](https://www.w3.org/TR/WCAG22/)

## Unsure list

- Garrett's vocabulary dated 2002 in the course brief: the revision history on jjg.net could not be fetched (robots blocked); the unit says only "first released October 2000, revised since".
- Garrett's Quick Reference quotations were read through a text extraction of the PDF; the PDF is undated, so the version it represents is not known.
- That the Quick Reference has no element for objects, states or actors is this unit's reading of the seventeen elements in that extraction.
- Brown, Communicating Design, chs 2, 5, 6: only the chapter openings (at-a-glance, purpose, the opening of "Anatomy of a Design Diagram") were seen; claims are kept to them.
- Rosenfeld, Morville and Arango, chs 8, 10, 13: section headings and chapter introductions seen; the glosses of global, local, contextual and supplemental navigation are this unit's, not the book's wording.
- UML 2.5.1 as the source of the 1, 0..*, 1..* multiplicity notation: from knowledge; the clause of the specification was not checked.
- Prater 2015: the A List Apart page now names the author Sophia V. Prater; that she published it as Sophia Voychehovski is inferred from the site's author URL and is left out of the text.
- Shostack 1984 as the origin of the service blueprint: the HBR page and a summary were seen, not the article's text; volume and pages omitted.
- Harel 1987: the three added elements (nested states, parallel components, communication) paraphrased from the abstract.
- The "unit that builds it" column of the decision table: codes from the course's units list (IA4 to IA8, DD-IA3); where no unit ships the artefact by name, the unit that ships its nearest form is named, with that form in brackets.
- Fresh check 2026-10-30 (Opus 5.5): fix · 3 errors, 10 should-fix, 17 minor; all applied; report `audits/ux/fresh-check-IA2.md`
