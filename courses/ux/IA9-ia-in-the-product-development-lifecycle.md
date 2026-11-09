---
code: IA9
title: IA in the product development lifecycle
course: ux · IA · Information Architecture
model: Opus 5.5
written: 2026-11-09
search: off
---

# IA9 · IA in the product development lifecycle

IA5 to IA8 built the IA of Perqo (Perqo, fictional), the flexible-benefits platform this course runs on: the perqo.com inventory, sitemap and template catalogue (IA5), the app's task inventory, app map and wireflows (IA6), Perqo Admin's object-relationship map, role matrix, navigation model and claim state diagram (IA7), and the interaction map that joins them (IA8). Each was dated, versioned and handed on. This unit puts that work in time. It covers where IA work sits in the published models of the design and product process, and what goes wrong when it is treated as a phase; how IA works inside an agile delivery, and how IA debt builds up; when each artefact in IA2's catalogue is done at each stage, and how its fidelity rises; who may change the IA, how a change is proposed, recorded and told, and the decision log that holds it; how an IA is kept current, on what cadence and on what triggers; and which signals in production say the IA is failing, with the loop forward to IA11's validation methods. The deliverable is Perqo's IA workflow across one product cycle, the definition of done for each artefact, the maintenance cadence, and the change control with its decision log.

Every figure uses IA2's notation (IA2, section 5.2 and the notation sheet), and this unit draws five of its six tones. Tone 5, shared, carries most figures here, because process work spans every surface and every function. Tone 6, a stop, marks a change that is declined. One figure, of the signals read in production, keeps IA2's surface tones: tone 1 for perqo.com (the Help centre's search), tone 3 for the Perqo app, tone 4 for Perqo Admin, and tone 5 for the support tickets, which reach every surface. Tone 2, the merchant side, is not drawn.

A search of the filed units for "IA9" finds no question handed to this unit by name. What the filed units hand on, and where this unit uses it:

| From | What it hands on | Used in |
|---|---|---|
| IA2, sections 1.0, 1.1 to 1.10, 3 and 4; the notation sheet; the decision table | the three fidelities, the catalogue, the five faults, the rules for changing an artefact, the face fields, fidelity by stage | sections 3 and 4; Deliverable B |
| IA1, sections 1.4 and 4 | Garrett's planes; every deliverable names its decision and readers | sections 1.2 and 3 |
| IA3, section 5.2 and checklist item E2 | the Help centre's search log as a production signal; support reads the For employees log each quarter | section 6.1; Deliverable C |
| IA5 to IA7, the faces and the sections that hand on to later units ("What the inventory hands on", "What IA8 and IA11 take", "What IA8 and later units take") | the owners, versions and dates of Perqo's artefacts; the dated notes of 3 and 9 November 2026 | sections 2.4 and 4.5; Deliverable D |
| IA8, section 6 | four practices for keeping the map current, among them the review at each release touching two surfaces and quarterly | section 5; Deliverable C |
| IA5 to IA8, every assumption table that names IA11 or IA12 | the tests each assumption needs, and support's tickets and analytics as proxies | section 6; Deliverable C |
| Register, "Not yet set" | Perqo's release rhythm, who owns the IA, a decision log's identifiers | sections 2.3, 4.1 and 4.3; "Perqo facts set by this unit" |

## 1 · Where IA work sits in the published process models

### 1.1 · The Double Diamond

The UK Design Council's Double Diamond, "Launched in 2004" in the Council's own account, has four phases ("Framework for Innovation", Design Council, undated page, checked 9 November 2026, [designcouncil.org.uk, framework for innovation](https://www.designcouncil.org.uk/resources/framework-for-innovation/); organisation's methodology). The first diamond is Discover, understanding the problem by "speaking to and spending time with people who are affected by the issues", then Define, where those insights frame the challenge anew. The second is Develop, generating answers, drawing on outside inspiration and "co-designing with a range of different people", then Deliver, testing at "small-scale", dropping what fails and refining what works. The page says three things about time that matter here: the process is not linear, as the arrows on its diagram show; learning about the underlying problem can send a team back to the beginning; and ideas are never fully finished, because products and services keep "iteratively improving" on feedback (same page).

In the Double Diamond, IA work has a place in every phase, on this unit's reading of the phases against IA2's catalogue. In Discover, the IA work is an inventory of what exists, a read of the logs and tickets, the nouns of an object map and a word list: content, words and objects found, all at F1 except the inventory, which is only useful complete for its scope (IA2, section 1.1). In Define, the top levels and the vocabulary are agreed, moving from F1 to F2: the frame of the challenge, in IA terms, is which surfaces, objects and terms the work touches. In Develop, the F2 artefacts are drawn and tested, as candidate structures. In Deliver, the artefacts reach F3, with identifiers and versions, because Deliver is where engineering builds. The Council's last point, that ideas are never fully finished, names a stage its four phases do not draw: after Deliver, the product is improved on feedback, and so is its IA, kept by reviews and signals (sections 5 and 6).

### 1.2 · Garrett's planes in time

IA1 placed IA on Garrett's structure plane, between scope below and skeleton above (IA1, section 1.4; Garrett, *The Elements of User Experience*, 2nd ed., New Riders, 2011, chs 3 to 7). The planes are a model of dependency, abstract at the bottom and concrete at the top, and Garrett also says how they relate in time. His original diagram of 30 March 2000 runs a time axis beside the planes, from conception at the abstract end to completion at the concrete end, and states that the model does not describe a development process and does not define roles in a team (Garrett, "The Elements of User Experience", diagram, 2000, [jjg.net, elements diagram](https://www.jjg.net/elements/pdf/elements.pdf)). In the book he rejects the reading that work on each plane must finish before work on the next can start; the dependency he asks for is weaker, that work on a plane cannot finish before work on the plane below it has finished, so the planes overlap in time (Garrett 2011, ch. 2, "Meet the Elements").

Put in time, the five planes give this schedule. During discovery the team works on strategy, and scope begins. As the problem is defined, scope is worked and structure begins. In development, structure is worked and skeleton begins. In delivery, skeleton and surface are worked and structure finishes, because it cannot finish before scope has. Garrett's model stops at completion; what happens to a structure after launch is outside the model, which by its own statement is not a process (Garrett 2000).

So IA starts before scope is settled and finishes only when scope does. A team that starts the sitemap after the requirements are signed has lost the plane's overlap with scope, where the structure most often shows that a requirement is missing or doubled.

### 1.3 · Discovery, definition, delivery: the two tracks

A third model comes from product management: two tracks run at once. Marty Cagan's name for it is dual-track agile: a discovery track whose purpose is "quickly generating validated product backlog items", beside a delivery track for "generating releasable software" ("Dual-Track Agile", Silicon Valley Product Group, 17 September 2012, [svpg.com, dual-track agile](https://svpg.com/dual-track-agile); practice); he later preferred the names continuous discovery and continuous delivery (same page). Jeff Patton, who taught with Cagan, credits the term to Desirée Sy's 2007 paper "Adapting Usability Investigations for Agile User-centered Design" and quotes her: "...designers need to communicate every day with developers" ("Dual Track Development is not Duel Track", Jeff Patton & Associates, 10 May 2017, updated 12 April 2023, [jpattonassociates.com, dual track](https://jpattonassociates.com/dual-track-development/); practice). Patton's own gloss: "Discovery and development are shown in two tracks because they're two kinds of work, and two kinds of thinking", done by one team, and "Discovery work happens concurrently and continuously with development work"; once work moves into development, discovery is not over: "Keep measuring and learning even after you ship" (Patton 2017).

The peer-reviewed literature arrives at the same structure. Manuel Brhel, Hendrik Meth, Alexander Maedche and Karl Werder reviewed published work on combining user-centred design with agile development and named five principles: "Separate Product Discovery and Product Creation", "Iterative and Incremental Design and Development", "Parallel Interwoven Creation Tracks", "Continuous Stakeholder Involvement" and "Artifact-Mediated Communication" ("Exploring principles of user-centered agile software development: A literature review", *Information and Software Technology* 61, 2015, pp. 163 to 181, [doi.org, Brhel 2015](https://doi.org/10.1016/j.infsof.2015.01.004)). The review reports what the literature recommends and describes; it does not measure whether teams that follow the principles ship better structures.

Discovery, definition and delivery in this model are kinds of work running side by side, with definition the hand-over point where a discovered answer becomes a backlog item. IA work sits in both tracks: candidate structures in discovery, one step ahead of delivery; F3 artefacts in delivery, cited by the stories engineering builds; and the reading of production signals, which Patton's "after you ship" puts back into discovery.

### 1.4 · IA located in all three

The three models, set against one cycle of five stages: the four phases of the Double Diamond and a fifth, Run, for the product after release. The cells name what each model has at each stage and what the IA work is; every cell is from sections 1.1 to 1.3.

```viz
{"kind": "matrix", "caption": "Process models with IA located: the Double Diamond's phases, Garrett's planes in time and the two tracks, set against one cycle of five stages, with the IA work at each; supports the decision on when IA work starts and that it does not stop at release (section 1.4). Double Diamond from the Design Council, 'Framework for Innovation' (checked 9 November 2026); planes in time from Garrett's diagram of 2000 and The Elements of User Experience, 2nd ed., 2011, ch. 2; two tracks from Cagan 2012, Patton 2017 and Brhel and others 2015; the IA work and fidelities from IA2, sections 1.0 to 1.10, on this unit's reading. Every row tone 5, shared: the work spans every surface.",
 "cols": ["Double Diamond", "Garrett's planes", "Two tracks", "IA work"],
 "rows": [
  {"label": "Discover", "tone": 5, "cells": ["the problem, with the people affected", "strategy; scope begins", "discovery", "inventory (F2); logs, nouns, word list (F1)"]},
  {"label": "Define", "tone": 5, "cells": ["the challenge framed", "scope; structure begins", "discovery", "top levels and vocabulary agreed: F1 to F2"]},
  {"label": "Develop", "tone": 5, "cells": ["answers generated and co-designed", "structure; skeleton begins", "discovery, ahead of delivery", "F2 artefacts, tested"]},
  {"label": "Deliver", "tone": 5, "cells": ["tested small, refined", "skeleton and surface; structure finishes", "delivery", "F3: identifiers, versions"]},
  {"label": "Run", "tone": 5, "cells": ["after Deliver: improved on feedback", "outside the model", "discovery continues", "kept: reviews and signals"]}]}
```

### 1.5 · What is wrong with treating IA as a phase

A phase has an entry, an exit and a hand-over: the IA is drawn, signed off and passed to the next team. The field's standard text can be read that way. The fourth edition of the Polar Bear book orders its part on getting IA done as Research, Strategy, then Design and Documentation (Rosenfeld, Morville and Arango, *Information Architecture: For the Web and Beyond*, 4th ed., O'Reilly, 2015, Part III, chs 11 to 13, contents at [oreilly.com, book contents](https://oreilly.com/library/view/information-architecture-4th/9781491913529)), and chapter 13 opens by saying that when you move from research and strategy into design "the landscape shifts dramatically" ([oreilly.com, ch. 13](https://www.oreilly.com/library/view/information-architecture-4th/9781491913529/ch13.html)). Read as a teaching order, that is sound; read as a schedule, it puts IA in one block of time. Four things go wrong with the schedule reading, each on a source above.

1. **The models do not support it.** The Design Council says its process is not linear and its ideas never finished (section 1.1); Garrett says his model is not a process and that the planes overlap (section 1.2); Patton says discovery runs "concurrently and continuously" (section 1.3). A phase plan for IA is a reading none of the three makes.
2. **A phase ends; the dependants of an artefact do not.** IA2 listed who depends on an artefact in use: engineering tickets cite its nodes, the content inventory cites its sections, support's articles name its screens, a client has signed off a version of it (IA2, section 4). After a phase ends those readers keep reading the version signed off, while the product moves. At Perqo the move was fast: within six days of IA4 to IA7 being dated 3 November 2026, IA8's decisions of 9 November changed artefacts in three of them (IA4, IA6 and IA7; section 2.4).
3. **One phase means one fidelity.** IA2 gave each artefact a fidelity by stage, F1 in discovery, F2 in design, F3 for build (IA2, section 1.0 and the decision table). A phase that produces "the IA" produces it at one fidelity, too detailed to argue about early or too thin to build from late.
4. **The IA is a debt-prone area after launch.** Anna Kaley lists information architecture, "navigation structures and content classification", among the areas where UX debt builds up, and lists among its causes "Skipping user testing", "Design by committee", "Acquiring or merging with other products" and "Poor communication or documentation" ("UX Debt: How to Identify, Prioritize, and Resolve", Nielsen Norman Group, 11 November 2018, [nngroup.com, UX debt](https://www.nngroup.com/articles/ux-debt/)). Each of them can act after a phase has closed: a merger, a committee deciding a later change, a later change shipped untested or undocumented.

Jorge Arango gives the life of an information environment over time two chapters, "Sustainability" and "Gardening" (*Living in Information*, Two Waves Books, 2018; IA1, section 1.3). The rest of this unit is the method for that second life, at the level of artefacts.

## 2 · IA in an agile delivery

### 2.1 · What the evidence and the named practice say

The evidence is thin and of one kind. Brhel and his co-authors' review (section 1.3) is the peer-reviewed source this unit has: it finds separate discovery and creation tracks, run in parallel, and communication through artefacts among the principles of the literature, and it does not test them. The rest is named practice, labelled as such.

- **The whole before the parts.** Jon Aizlewood names the failure: "Frankensteining occurs when products or services created using Agile become fragmented or disjointed". His remedy is a "best first pass", a rough sketch of the whole product laid out in sequence before sprint-level detail, with regular points in each sprint to zoom out ("Agile and design: how to avoid Frankensteining your product", Clearleft, 24 July 2019, [clearleft.com, Frankensteining](https://clearleft.com/thinking/agile-and-design-how-to-avoid-frankensteining-your-product); practice).
- **Time for the big picture.** Damon Dimmick: "The rapid pace of UX design in the agile world can lead to shortsighted design decisions", a "design tunnel vision" he answers with a design spike, a period set aside for design questions in which development work those questions affect pauses ("Fitting Big-Picture UX Into Agile Development", *Smashing Magazine*, 6 November 2012, [smashingmagazine.com, design spikes](https://www.smashingmagazine.com/2012/11/design-spikes-fit-big-picture-ux-agile-development/); practice).
- **Debt on the backlog.** Kaley recommends tracking UX-debt items in the backlog, added directly or from a spreadsheet first, with the same severity indicators as other items, ranking them by user value and effort, tracking them with technical debt, and holding recurring reviews where anyone can raise one (Kaley 2018; NN/g guidance).

What the IA adds to these is a reason the whole matters more for structure than for screens. A screen designed in one sprint can be redesigned in another. A label, an identifier or a parent chosen in one sprint is cited by the next sprint's stories, the Help centre's articles and the search synonyms (IA2, section 4), so each sprint that cites it adds a place a later change must reach.

### 2.2 · The backbone drawn before stories are cut

Jeff Patton's story map orders user stories along two dimensions: user activities across, roughly in the order a user performs them, and stories down, by priority; its first row across is a "walking skeleton", "a barebones but usable version of the product" (Agile Alliance, "What is Story Mapping?", Agile Glossary, 17 December 2015, modified 9 March 2023, [agilealliance.org, story mapping](https://www.agilealliance.org/?p=5003329); practice). Patton's book calls the row of activities across the top the backbone of the map (Patton, *User Story Mapping*, O'Reilly, 2014; practice). The glossary dates the idea to Patton's articles of 2005 and 2008 (Agile Alliance).

The story map's backbone is a sequence of what people do. The IA's backbone is what they do it on and through: the top levels of each surface and the objects those levels hold. Both have to exist before the stories are cut, for the same reason: a story cut without them names a screen or a thing nobody has placed. This course's practice, drawing on Aizlewood's best first pass:

- **Before the first story of a cycle is written, draw the touched surfaces' top levels and the object map at F1 in Discover, and agree their top levels in Define.** For work on Perqo's app, the app map's tabs (A-1 to A-5) and the objects of IA4 already exist; a new cycle checks them against the work and marks what it adds as proposed (IA2, section 4).
- **Hang the story map under the IA's identifiers.** Each activity in the story map's backbone names the screens or pages it happens on (A-, AD-, S-, H-) and the objects it acts on (O-). A story then inherits its identifiers from its column.
- **Keep the F3 rows one sprint ahead of the stories that build them**, which is Sy's two tracks applied to the artefacts: the wireflow, the transitions and the decision table a story needs are at F3 before the story enters a sprint (section 3).

### 2.3 · The IA kept alongside the backlog

Brhel and his co-authors' fifth principle, artefact-mediated communication (section 1.3), is the reason the IA lives beside the backlog, where the stories that cite it are. At Perqo (Perqo, fictional), engineering delivers in sprints and releases at the end of each sprint; each release note lists the surfaces the release touches, and the sprint's length is left free. Three rules tie the IA to that backlog, set here as Perqo practice (Perqo, fictional):

- **Every story cites the IA identifiers it touches**: the screen, page or route (A-, AD-, S-, H-, X-), the object and relationship (O-, R-), the rule or transition (DT-; T1 to T6). A story that would create a new identifier, label or route cites the decision log entry that proposes it (section 4.3).
- **An IA debt item is a backlog item**, tagged "IA debt", citing the decision log entry or the signal it comes from (section 2.4), and ranked with the rest (Kaley 2018).
- **A story cannot enter a sprint while the artefact it builds from is below F3** for the part the story touches (section 3.1).

These are tool-agnostic: a backlog on cards, in a spreadsheet or in any tracker can hold an identifier, a tag and a link.

### 2.4 · IA debt, and how it accrues

Kaley defines UX debt by analogy with technical debt, which she credits to Ward Cunningham in 1992: problems that stay in the experience after a fast, easy or careless solution is shipped (Kaley 2018). She notes that "Inconsistencies in the UI can be considered UX debt, but not always", and excludes intended variations such as A/B test variants (same article). This course uses a narrower term for its own subject. **IA debt** is the gap between the IA as decided and the IA as recorded or shipped, in three kinds:

- **Record debt.** A decision has been taken and logged, and some artefact that depends on it still shows the old state. Its interest: every reader of that artefact builds on the old state.
- **Build debt.** The product as shipped differs from the F3 artefact: a screen, label or route a story added without a decision. Its interest: the artefact stops being a true account of the product, so readers stop trusting it.
- **Open faults.** A fault is known and logged and has no decision: a gap left free, a zero-result query nobody has acted on. Its interest is paid by the people using the product.

No study known to this unit measures what IA debt costs; the case rests on the mechanism above and on the record below.

Perqo's own artefacts show record debt accruing, in the filed units' dated notes (Perqo, fictional). On 9 November 2026 IA8 took decisions that changed artefacts dated 3 November (IA8, "Perqo facts set by this unit"). Where they were applied:

- **Applied in full, face re-stamped:** IA6's wireflows. C.2 and its figure changed, and the face reads "version 1, dated 3 November 2026; C.2 amended 9 November 2026 (IA8, section 4.5)" (IA6, Deliverable C). This is IA2's rule "Re-stamp the face" followed (IA2, section 4).
- **Applied, face not re-stamped:** IA6's app map gained entry E-8 and a note on A-5 (IA6, Deliverable B, B.3 and B.4), and its face still reads "version 1, dated 3 November 2026" with no amendment. IA4's object map gained a dated note under its figure (IA4, Deliverable A, after A.4), and its face is unchanged.
- **Recorded as a note, not applied in the artefact:** IA7's Admin IA carries IA8's answers in a dated note under "What IA8 and later units take" and in its facts row, while its F3 object-relationship map still lists the card's states as "Active, Frozen (IA4)" (IA7, Deliverable A, A.1, row O-09; section 5.1's table), its model fields still give card status as `active`, `frozen` with no `cancelled`, the allocation with no closed attribute and the client with no contract end date (A.2), and its calls to action list -> invite employees with no condition (A.4). IA6's screen states table has no state for a category open with no allocation for the period, which IA8 set as "a new state of IA6's category screen" (IA6, Deliverable B, B.5; IA8, section 4.2).

An engineer who builds Admin's card status from IA7's F3 map, which its face calls "the agreed mapping to the data model", builds it without Cancelled. That is the interest on record debt, and nothing in IA7's own deliverable warns the engineer. Section 4.5 says what this unit changes so that a face would warn them, and Deliverable D logs each unapplied place as an entry. *Note, 9 November 2026: the filing of this unit applied every place listed above and re-stamped the faces by section 4.4's rule, so IA4's, IA6's and IA7's artefacts no longer carry this debt (section 4.5; Deliverable D, the note after D.3).*

## 3 · When an IA artefact is done

### 3.1 · A definition of done, borrowed and changed

Scrum gives the term. The Scrum Guide's Definition of Done is "a formal description of the state of the Increment when it meets the quality measures required for the product" (Schwaber and Sutherland, *The Scrum Guide*, as quoted by Scrum.org, "What is a Definition of Done?", undated, [scrum.org, definition of done](https://www.scrum.org/resources/what-definition-done); practice framework; the page names no edition of the Guide), and Scrum.org adds, in its own words, that "If a Product Backlog Item does not meet the Definition of Done, it cannot be released yet" (same page). Two parts carry over to IA. A definition of done is written down in advance, so "done" is checked against a list and not argued each time. And it gates something: in Scrum, release; for an IA artefact, the use the next stage makes of it.

Two parts change. An IA artefact has three dones, one per fidelity, because IA2 made fidelity a matter of stage (IA2, section 1.0): F1 is done when it is good enough to argue about, F2 when it is good enough to agree on, F3 when it is good enough to build from and keep. And an artefact in use has a fourth state, kept: true of the product as of its face's date, and true after that date only under the cadence of section 5.

Every artefact, at every fidelity, is done only when six things hold. Each comes from a filed rule:

1. **The face is complete**: name and family, decision, readers, what it leaves out, fidelity, owner, version and date (IA2, the notation sheet; IA1, section 4).
2. **It passes IA2's five faults** when read by someone who did not make it: a stated decision, reader, scope and date; a declared and consistent notation; one level at a time; conditions and unhappy paths; labels that match the vocabulary (IA2, section 3).
3. **Every assumption is marked "assumed", with the test that would settle it**, which is what IA5 to IA8's assumption tables do for IA11 and IA12.
4. **The notation is kept**, and any new symbol is in the legend before it is used (IA2, section 4).
5. **Every label is in the controlled vocabulary**, under its surface's name (IA2, section 3, fault 5).
6. **Every change since the last version has a decision log entry that names this artefact** (section 4.3).

The criteria for each artefact at each fidelity are in Deliverable B, usable without this unit.

### 3.2 · How fidelity rises across the stages

IA2's decision table gives each artefact its fidelity by stage, in three stages: discovery, design and build (IA2, the artefact decision table). Against the five stages of section 1.4, on this unit's reading: Discover is IA2's discovery; Define and Develop split IA2's design, with Define agreeing the top levels and the vocabulary and Develop completing and testing the rest; Deliver is IA2's build; Run is new, and in it an artefact is kept. Define is the first half of IA2's design stage, so an artefact IA2 gives F2 in design reaches it in Develop; in Define the structures stay at F1 while their top levels are agreed, and the vocabulary, which IA2 gives F2 "once labels agreed", reaches F2 there. Three rules govern the rise.

- **Fidelity rises only through agreement.** An artefact moves from F1 to F2 when the readers IA2 names for it have agreed it, and from F2 to F3 when engineering can cite each element in a ticket (IA2, sections 1.0 and 4). A designer cannot move an artefact up a fidelity alone.
- **Some artefacts hand over instead of rising.** A task flow at F1 becomes a user flow at F2; a user flow's build detail goes into the wireflow; an object map becomes the object-relationship map at F3 (IA2, sections 1.5 and 1.6). The grid marks where an artefact continues as another.
- **Some artefacts never need F3.** IA2 gave the navigation model F2, its routes living at build time in the sitemap's identifiers and the screens, and the service blueprint F2 at most, its build detail moving into flows, rules and lifecycles (IA2, sections 1.4 and 1.9).

The grid's rows use short names for IA2's catalogue: inventory (the content inventory and audit), vocabulary (the controlled vocabulary), taxonomy, sitemap (with IA6's app map, the sitemap's form for an app), navigation model, object map, relationship map (the object-relationship map), user flow, task flow, wireflow, decision tree, state diagram, blueprint (the service blueprint) and cross-surface map (the cross-surface interaction map). A cell gives the fidelity the artefact is done at in that stage, "kept" when it is under the cadence, "as" and the artefact it continues in, or nothing.

```viz
{"kind": "matrix", "caption": "Artefact by stage: the fidelity at which each artefact of IA2's catalogue is done in each stage of a cycle, and where it is kept; supports the decision on what an artefact must be before the next stage uses it (section 3.2). Fidelity by stage from IA2's artefact decision table and sections 1.0 to 1.10, with IA2's design stage split into Define and Develop and the Run stage added on this unit's reading; 'kept' means under the cadence of section 5 and Deliverable C. Every row tone 5, shared.",
 "cols": ["Discover", "Define", "Develop", "Deliver", "Run"],
 "rows": [
  {"label": "Inventory", "tone": 5, "cells": ["F2", null, null, "F3", "kept"]},
  {"label": "Vocabulary", "tone": 5, "cells": ["F1", "F2", "F2", "F3", "kept"]},
  {"label": "Taxonomy", "tone": 5, "cells": [null, null, "F2", "F3", "kept"]},
  {"label": "Sitemap", "tone": 5, "cells": ["F1", "F1", "F2", "F3", "kept"]},
  {"label": "Navigation model", "tone": 5, "cells": [null, null, "F2", "F2", "kept"]},
  {"label": "Object map", "tone": 5, "cells": ["F1", "F1", "F2", "as relationship map", null]},
  {"label": "Relationship map", "tone": 5, "cells": [null, null, "F2", "F3", "kept"]},
  {"label": "Task flow", "tone": 5, "cells": ["F1", "F1", "as user flow", null, null]},
  {"label": "User flow", "tone": 5, "cells": [null, null, "F2", "as wireflow", null]},
  {"label": "Wireflow", "tone": 5, "cells": [null, null, "F2", "F3", "kept"]},
  {"label": "Decision tree", "tone": 5, "cells": [null, null, "F2", "F3", "kept"]},
  {"label": "State diagram", "tone": 5, "cells": [null, null, "F2", "F3", "kept"]},
  {"label": "Blueprint", "tone": 5, "cells": ["F1", "F1", "F2", null, "kept"]},
  {"label": "Cross-surface map", "tone": 5, "cells": ["F1", "F1", "F2", "F2, F3 identifiers", "kept"]}],
 "legend": [{"mark": "F1", "means": "sketch: to argue about", "tone": 5}, {"mark": "F2", "means": "working: to agree on", "tone": 5}, {"mark": "F3", "means": "specification: to build from and keep", "tone": 5}, {"mark": "kept", "means": "true as of its face's date, under the cadence", "tone": 5}]}
```

Two cells depart from IA2 and say why. The cross-surface map's Deliver cell is IA8's choice, F2 with F3's identifiers on every element, because the map is kept current more than it is built from (IA8, Deliverable, the face). And the blueprint is kept in Run, though IA2 gave it no build fidelity, because IA8's lifecycle swimlanes are the blueprint's form at Perqo and their J- rows are reviewed each quarter (IA8, section 6).

## 4 · Versioning and change

### 4.1 · Who may change the IA

An IA in use has readers who have agreed to a version of it (IA2, section 4), so a change needs someone with the standing to make it. Lisa Welchman's book on digital governance names the problem: governance is "establishing clear accountability for digital strategy, policy, and standards", and one of its chapters is "Stopping the Infighting About Digital Standards" (*Managing Chaos: Digital Governance by Design*, Rosenfeld Media, 2015, ch. 5; publisher's description, [rosenfeldmedia.com, Managing Chaos](https://rosenfeldmedia.com/?p=187514)). Halvorson and Rach make governance one of content strategy's four components, the way key decisions about content are made (*Content Strategy for the Web*, 2nd ed., New Riders, 2012, ch. 9; IA1, section 2.3). The IA is a standard in Welchman's sense: a shared structure many teams build on, which therefore needs a named owner and a named way to change it.

At Perqo (Perqo, fictional), anyone may propose a change, and who decides it depends on what it reaches. The IA designer, already the owner on the faces of most of IA4 to IA8's artefacts (the benefits taxonomy is the content team's; IA5's inventory and template catalogue are shared with marketing and with engineering), owns the canonical artefacts other than the taxonomy, and the decision log. The **IA review** is the group that holds IA8's review: the IA designer (who chairs it), product management, engineering, the content team and support; sales and clients are told of its decisions and do not sit in it (Perqo, fictional). The routing rule:

- **A change to a rule, or one that touches two surfaces, goes to the IA review, and product management signs it off.** A rule (DT-1 to DT-3) is set on one surface and felt on another (IA8, section 4.1), and a two-surface change moves a J- row (IA8, section 6). A new top-level benefit category is one of these, and by IA4's rule R8 also goes to finance and the client (IA4, Deliverable B, B.4).
- **A change that renames a label or retires an identifier goes to the IA review**, and the vocabulary changes first (IA2, section 4; IA7, section 6.3). Evans's rule, "Recognize that a change in the language is a change to the model", is why engineering sits in that review (Evans, *Domain-Driven Design Reference*, 2015; IA7, section 6.2).
- **A value in the benefits taxonomy is the content team's**, as a proposed change reviewed with support and engineering under R1 to R10 (IA4, Deliverable B, B.4).
- **Anything else, inside one surface and renaming nothing, the IA designer decides**, and logs it.

The rule as a decision tree, in the order its questions are asked; every outcome is logged (section 4.3).

```viz
{"kind": "decision", "caption": "Decision tree: who decides a change to Perqo's IA; supports the decision on where a proposed change goes (section 4.1). Questions ordered widest reach first. Routing set in section 4.1 (Perqo, fictional), on IA8, sections 4.1 and 6 (rules and J- rows), IA2, section 4 and IA7, section 6.3 (vocabulary first), and IA4, Deliverable B, B.4 (the content team's rules R1 to R10, and R8 for a new top-level category). Governance as named accountability from Welchman 2015. Every box tone 5, shared: the routing applies to every surface. Perqo is fictional.",
 "root": {"q": "Changes a rule (DT-) or touches two surfaces?", "tone": 5, "branches": [
  {"label": "yes", "to": {"outcome": "IA review decides; product management signs off", "tone": 5}},
  {"label": "no", "to": {"q": "Renames a label or retires an identifier?", "tone": 5, "branches": [
   {"label": "yes", "to": {"outcome": "IA review decides; vocabulary first", "tone": 5}},
   {"label": "no", "to": {"q": "A value in the benefits taxonomy?", "tone": 5, "branches": [
    {"label": "yes", "to": {"outcome": "Content team decides, by R1 to R10", "tone": 5}},
    {"label": "no", "to": {"outcome": "IA designer decides", "tone": 5}}]}}]}}]}}
```

### 4.2 · How a change is proposed, recorded and communicated

IA2 set the rules for editing an artefact others rely on: keep identifiers stable, mark changes as proposed until agreed, rename through the vocabulary, split rather than cram, keep the notation and extend the legend, re-stamp the face (IA2, section 4). They say how to edit. A change also needs a path from the person who raises it to the readers who must hear of it, and IA8's connections table already says who those readers are for any element: "A change to any identifier in a J- row is not done until the other cells of that row have been checked" (IA8, Deliverable, D.5). The flow below is this course's practice, set as Perqo's (Perqo, fictional). Its steps:

1. **Raise a change.** Any function, from a signal, a story or a client.
2. **Log it as proposed** in the decision log, with a DL- identifier; the current version of every artefact stays visible until the change is accepted (IA2, section 4).
3. **Check the impact**: the identifiers it touches, the J- rows and X- crossings that cite them, the DT- rules that read them (IA8, D.4).
4. **Route it to who decides**, by section 4.1.
5. **Decide.** A declined change is logged with its reason and ends here.
6. **Change the vocabulary first**, with the old term kept as a variant (IA2, section 4).
7. **Change the artefacts**: identifiers kept, each changed artefact's face re-stamped (section 4.4).
8. **Tell the readers**: the functions the entry lists as informed, in the release note when it ships.
9. **Close the entry** as applied, once every place it names is changed; a later entry that replaces it links back to it.

```viz
{"kind": "flow", "per_row": 2, "caption": "Change-control flow: how a change to Perqo's IA is raised, logged, decided, applied and told; supports the decision on what must happen before a change counts as made (section 4.2). The flow kind draws no branch, so the declined path is a bracketed condition in the Decide step's note. Steps set in section 4.2 (Perqo, fictional), on IA2, section 4 (proposed until agreed, vocabulary first, identifiers kept, re-stamp the face) and IA8, Deliverable, D.4 and D.5 (J- rows checked); the log after Nygard's decision records, as Fowler describes them (2026). Every step tone 5, shared. Perqo is fictional.",
 "steps": [
  {"label": "Raise a change", "note": "any function: a signal, a story, a client", "tone": 5},
  {"label": "Log it as proposed", "note": "DL- entry; the current version stays visible", "tone": 5},
  {"label": "Check the impact", "note": "identifiers, J- rows, X- crossings, DT- rules", "tone": 5},
  {"label": "Route to who decides", "note": "→ see the decision tree, section 4.1", "tone": 5},
  {"label": "Decide", "note": "[declined] logged with its reason; ends here", "tone": 5},
  {"label": "Change the vocabulary first", "note": "old term kept as a variant", "tone": 5},
  {"label": "Change the artefacts", "note": "identifiers kept; each face re-stamped", "tone": 5},
  {"label": "Tell the readers", "note": "the informed functions; the release note", "tone": 5},
  {"label": "Close the entry", "note": "applied; a superseding entry links back", "tone": 5}]}
```

### 4.3 · The decision log

Software architecture has a published form for this. Martin Fowler describes the architecture decision record, a term he credits to Michael Nygard in 2011, as "a short document that captures and explains a single decision": the decision first, its context and the trade-offs, the serious alternatives, its consequences, and a status such as proposed, accepted or superseded; once accepted, a record "should not be modified if the decision is changed, but linked to a superseding decision" ("Architecture Decision Record", martinfowler.com, 24 March 2026, [martinfowler.com, decision record](https://www.martinfowler.com/bliki/ArchitectureDecisionRecord.html); practice). Rosenfeld, Morville and Arango give the IA's own version a goal in the same terms: style guides "for capturing your past decisions and guiding your future ones" (2015, ch. 13).

Perqo's IA decision log is one list of entries, kept by the IA designer, each with an identifier DL-001 onward, never reused (Perqo, fictional). An entry holds: what is proposed, in one line; who raised it and from what (a signal, a story, a unit's decision); the artefacts and identifiers it touches, and the J- rows; the alternatives considered; who decides, by section 4.1; the decision, the date and the reason; the places it must be applied, each marked done or not; the functions told and when; and the entry it supersedes or that supersedes it. An entry has five statuses. Fowler's three are kept; two are added. **Declined** is the end of a proposal the decider refused, kept so the same proposal is not raised blind. **Applied** separates a decision taken from a decision carried out, which is the line section 2.4 drew between a decision and its record debt: an entry stays accepted, and counts as IA debt, until every place it names is changed.

```viz
{"kind": "states", "per_row": 3, "caption": "State diagram: the lifecycle of an entry in Perqo's IA decision log; supports the decision on when a change counts as decided, as made and as replaced (section 4.3). Proposed, accepted and superseded, and the rule that an accepted entry is superseded, never edited, from Fowler's account of Nygard's architecture decision records (2026); declined and applied added in section 4.3. Tone 5 shared; tone 6 a stop, a proposal refused. Perqo is fictional.",
 "states": [
  {"id": "proposed", "label": "Proposed", "note": "the current version stays visible", "tone": 5},
  {"id": "accepted", "label": "Accepted", "note": "IA debt until applied", "tone": 5},
  {"id": "applied", "label": "Applied", "note": "every place changed", "tone": 5},
  {"id": "declined", "label": "Declined", "note": "kept, with its reason", "tone": 6, "end": true},
  {"id": "superseded", "label": "Superseded", "note": "links to the later entry", "tone": 5, "end": true}],
 "transitions": [
  {"from": "proposed", "to": "accepted", "label": "decided: yes"},
  {"from": "proposed", "to": "declined", "label": "decided: no"},
  {"from": "accepted", "to": "applied", "label": "last place changed"},
  {"from": "applied", "to": "superseded", "label": "a later entry replaces it"},
  {"from": "accepted", "to": "superseded", "label": "replaced before applied"}]}
```

### 4.4 · Versions and the face

IA4 to IA8's artefacts carry "version 1" and a date on their faces, and IA2's rule says to update the version and the date when an artefact changes (IA2, section 4). It does not say when a change earns a new version and when a dated amendment is enough. Software has a convention for that question. Semantic Versioning increments "MAJOR version when you make incompatible API changes", "MINOR version when you add functionality in a backward compatible manner" and "PATCH version when you make backward compatible bug fixes" (Tom Preston-Werner, *Semantic Versioning 2.0.0*, [semver.org](https://semver.org/); specification). An IA artefact's readers are its API: the tickets, inventories, articles and sign-offs that cite it.

Perqo's rule takes the distinction and drops the third number (Perqo, fictional). **A new version** when an accepted change would break a citation: an identifier retired or moved to another parent, a label renamed, a relationship or transition removed, a rule's outcome changed. **A dated amendment** when it adds without breaking: a new element, a new state, a new attribute, a note. The face then reads, after IA6's wireflows (IA6, Deliverable C): "version N, dated D; amended D2 (DL-nnn), D3 (DL-nnn)", so a reader can go from the face to the entries that explain each change.

### 4.5 · What this unit changes in the filed units

This unit changes how filed artefacts are kept, in three places; the filing chat applies them to the filed units.

1. **IA2, section 4, "Re-stamp the face", and the notation sheet's face field "Owner, version, date"** gain the rule of section 4.4: a new version for a change that breaks a citation, a dated amendment otherwise, each amendment naming its decision log entry; and the field reads "Owner, version, date, amendments (DL-)".
2. **The faces of three filed artefacts are re-stamped** under that rule, each with an amendment of 9 November 2026: IA4, Deliverable A (DL-004 to DL-006); IA6, Deliverable B (DL-004, DL-008); IA7, the Deliverable (DL-005 to DL-007). None needs a new version: IA8's decisions added states, attributes and conditions and renamed nothing (IA8, "Perqo facts set by this unit").
3. **The places Deliverable D logs as not yet applied** are listed there, entry by entry, with the change each needs. They follow from decisions IA8 took and the register holds, so the filing chat can apply them without a new decision; the model field names they need are proposed in D.3 for engineering to confirm.

*Note, 9 November 2026: the filing chat applied all three, with a dated note in each place: IA2, section 4 and the notation sheet; the faces of IA4, Deliverable A, IA6, Deliverable B and IA7's Deliverable, and IA6's wireflows (Deliverable C, whose amendment now names DL-004) and IA7's navigation model (Deliverable C, for C.4); and every place D.3 lists, with the client's contract end date drawn in IA7's object-relationship figure (A.5), which holds the client's attributes.*

## 5 · IA as a living document: the maintenance cadence

IA8 set four practices for keeping its map current: change it where it changes and cite by identifier, change the vocabulary first, mark proposals, and review on a trigger as well as a date, at each release that touches two surfaces and each quarter (IA8, section 6). IA3's checklist added one for the Help centre: support reads the For employees search log each quarter and records each finding as a hypothesis (IA3, Deliverable, E2; IA6, Deliverable B, B.2). This section extends them to every artefact, and Deliverable C sets the cadence out in full.

A review has three parts, and the cadence gives each: **what is reviewed and against what**, **how often and on what trigger**, and **who owns it**. The published advice supports both dates and triggers. Kaley recommends recurring team reviews where anyone can raise debt (Kaley 2018). Susan Farrell recommends reading several months of a search log, so that a campaign's spike is not taken for a pattern (Farrell, "Search-Log Analysis", NN/g, 2017; IA3, section 5.2): a log read too often misleads, which, on this unit's reading, argues for a quarterly read. Halvorson and Rach's index has an entry for "rolling audits" (2012, index; IA5, section 1.1); the chapter was not read, and this unit takes from the term only its plain sense, an audit run one slice at a time. A trigger is what makes a review happen when the date is far: IA8's "each release touching two surfaces" is one (IA8, section 6).

Four kinds of review cover the catalogue (Perqo, fictional), each with its cadence in Deliverable C:

- **Delivery checks**, at each story and each release: the story check (each story cites its identifiers; every new identifier or label has an entry) and the release check (every entry the release carries is applied, each changed face is re-stamped, and the built screens match the F3 artefacts). These catch build debt as it happens.
- **Structure reviews**, at each release touching two surfaces and quarterly: the cross-surface review of IA8's J- rows and X- crossings, and the face audit, which compares every artefact's face date with the last decision log entry that names it. These catch record debt.
- **Signal reads**, monthly or quarterly: the Help centre's search log, support's tickets and the analytics paths of section 6. These find open faults.
- **Content and vocabulary reviews**, quarterly: a rolling audit of a slice of perqo.com's inventory, and the vocabulary checked against new variants from the logs and tickets under IA4's rules. Each also runs before any redesign (IA2, section 1.1: an inventory at F2 before any redesign).

Two triggers outrank the calendar. A change to a top level or a tab sends the structure to a test before and after (section 6.4). A change to a client's contract terms, a policy option or a decline reason sends the decision trees DT-1 to DT-3 and their J- rows to the rules review (IA8, D.3 and D.4).

The cadence below shows when each review runs and who owns it; a cell names the owner where a review runs at that cadence. Row names are Deliverable C's.

```viz
{"kind": "matrix",
 "caption": "Maintenance cadence: each review of Perqo's IA by when it runs, with its owner in the cell (a condition in square brackets: the review runs at that cadence only when it holds; Deliverable C, RV-03 and RV-06); supports the decision on who checks what, and when, once the IA is in use (section 5; Deliverable C). Cadence and owners set in section 5 and Deliverable C (Perqo, fictional), extending IA8, section 6 (each release touching two surfaces, quarterly) and IA3's item E2 (support reads the log each quarter); quarterly log reading on this unit's reading of Farrell, NN/g, 2017; rolling audits from Halvorson and Rach 2012, index; recurring debt reviews from Kaley, NN/g, 2018. Every row tone 5, shared.",
 "cols": ["Each story", "Each release", "Monthly", "Quarterly", "On trigger"],
 "rows": [
  {"label": "Story check", "tone": 5, "cells": ["IA designer", null, null, null, null]},
  {"label": "Release check", "tone": 5, "cells": [null, "IA designer", null, null, null]},
  {"label": "Cross-surface review", "tone": 5, "cells": [null, "IA review [touching two surfaces]", null, "IA review", null]},
  {"label": "Face audit", "tone": 5, "cells": [null, null, null, "IA designer", null]},
  {"label": "Search log", "tone": 5, "cells": [null, null, null, "support", "support"]},
  {"label": "Support tickets", "tone": 5, "cells": [null, null, "support", null, "support"]},
  {"label": "Analytics paths", "tone": 5, "cells": [null, "product management [screens it changed]", null, "product management", null]},
  {"label": "Vocabulary", "tone": 5, "cells": [null, null, null, "content team", "content team"]},
  {"label": "Rolling audit", "tone": 5, "cells": [null, null, null, "content team", "content team"]},
  {"label": "Debt triage", "tone": 5, "cells": [null, null, null, "product management", null]},
  {"label": "Structure test", "tone": 5, "cells": [null, null, null, null, "IA designer"]},
  {"label": "Rules review", "tone": 5, "cells": [null, null, null, null, "product management"]}]}
```

## 6 · Signals that the IA is failing in production

A structure fails in use in three ways a team can see without asking anyone: people search for what they could not find, people ask support what they could not work out, and people move through the product in paths that loop, stall or leave. Each leaves a record. None of the three records says why, so each signal is a hypothesis for IA11's methods, which is the status IA3 gave the search log (IA3, section 5.2, after Rosenfeld in Mausser, UXmatters, 2011).

### 6.1 · Search logs

IA3 set out what a log shows, after Farrell: zero-result queries, which show wanted information the search cannot find; frequent queries for something the site holds, which show a structure that hides it; frequent queries for something the site lacks, a content gap; and reformulations in one session, a failed search (Farrell 2017; IA3, section 5.2). Perqo's Help centre has search and logs it (IA3, section 5.2; Perqo, fictional), and its one read so far shows the full loop a signal should run. Each of the five top queries of IA3's quarter has since been acted on in a filed unit:

| Query (IA3) | What it suggested | Acted on in |
|---|---|---|
| refund | the article uses the variant term the app does not | H-2.1.2 marked for update (IA2, section 5.3; IA5, Deliverable A) |
| allowance | a variant of Balance with no synonym in search | variants go to the Help centre search as synonyms (IA4, Deliverable B, R4) |
| rejected claim | the app's Claims list did not show rejected claims | Claims grouped by all four states (IA6, Deliverable B, B.1) |
| gym | a basic-level word with no article or synonym | H-2.1.4, which answers "gym" (IA5, Deliverable A) |
| approval | the rule that decides a claim is not shown where the claim is made | H-1.2.5, and the rule line on New claim (IA5, Deliverable A; IA6, Deliverable B, B.1) |

The loop is not closed by the changes. The next quarter's log says whether "allowance" and "gym" still return nothing, which is a proxy; whether employees now find what they wanted is a test with people (section 6.4).

### 6.2 · Support tickets

Dana Chisnell calls the call centre "one of the richest sources of data about frustration": callers contact support about every stage of a relationship, so tickets reach problems a scenario-bound usability test can miss; the categories calls are routed into show where problems cluster; and the callers' own words are worth noting ("Call centers as a source of data", danachisnell.com, 24 July 2016, modified 9 April 2025, [danachisnell.com, call centers](https://danachisnell.com/call-centers-as-a-source-of-data/); practice). At Perqo, support's tickets already feed variant terms into the taxonomy (IA4, section 3.3), and IA6 to IA8 name them as the proxy test for four assumptions, among them that employees understand a declined payment and that HR does not need individual card payments (IA6, IA7 and IA8, the assumption tables).

A ticket can be read against the IA only if it says where the person was. This unit sets a practice for that (Perqo, fictional): support tags each ticket with the surface and the screen or page identifier it is about (A-, AD-, S-, H-) and, where it concerns a rule, the DT- tree, and reads the tags each month. A tag that rises after a release that touched its screen is a trigger (Deliverable C).

### 6.3 · Analytics paths

Jen Cardello names three uses for analytics in UX practice: "Issue indication: Notifying the team of potential problems reaching goals", "Investigation: Identifying potential causes of issues" and "Triangulation: Adding data to supplement qualitative research" ("Three Uses for Analytics in User-Experience Practice", Nielsen Norman Group, 17 November 2013, [nngroup.com, analytics uses](https://www.nngroup.com/articles/analytics-user-experience/)). For the IA the first two matter most: a path that loops between two screens, a screen reached mostly from search or from Help rather than its route, an exit just after a label is read. Perqo's product analytics record each app screen view by its screen identifier and each Admin page view by its page identifier (Perqo, fictional), which the addresses do not give by themselves: IA6's and IA7's addresses carry at most a record's or a category's identifier, never the screen's or the page's (IA6, section 6.3 and Deliverable B, B.4; IA7, Deliverable C, C.1), so the analytics map each address pattern to its A- or AD- identifier. IA6 and IA7 named the paths their assumptions need read: session paths for whether most app visits are one or two tasks begun from Home or a notification, and the first actions after sign-in for whether HR's and finance's most frequent work is what their landing pages, Approvals and Budgets, assume (IA6, "What IA8 and IA11 take"; IA7, "What IA8 and later units take"). Admin's failed sign-ins are a fourth record, named by IA5 and IA7 for one assumption: whether employees land on Admin's sign-in screen (AD-0) looking for the app (IA5, section 5.5; IA7, Deliverable C, C.5).

### 6.4 · From signal to IA11

Every signal is read for what it shows and becomes a hypothesis about one part of the structure, which a method of IA11 then tests with people before an artefact changes. The methods themselves are IA11's to specify; the filed units have already named which fits which assumption. Samhita Tankala separates the two structure methods by stage: card sorting is "typically conducted early in the design process", a discovery method, and a tree test "evaluates a hierarchical category structure", existing or proposed ("Card Sorting vs. Tree Testing", Nielsen Norman Group, 23 February 2024, [nngroup.com, card sort vs tree test](https://nngroup.com/articles/card-sorting-tree-testing-differences)). So a signal from production, which is about a structure that exists, goes first to a test of that structure, a tree test or the first-click test IA3 and IA6 named for the app's labels, and to a card sort only when the test shows the categories themselves are wrong.

```viz
{"kind": "matrix",
 "caption": "Production signals: what each record shows about Perqo's IA, the hypothesis it raises, the test it goes to and the artefact a failed test changes; supports the decision on what to do with a signal before changing the structure (section 6). Records, what each shows and the hypothesis it raises from sections 6.1 to 6.3 and Deliverable C, RV-04 to RV-06; the artefacts a failed test changes from section 6.1's table, sections 6.2 and 6.3 and Deliverable D, D.3 (DL-002); search-log reading from Farrell, NN/g, 2017 (IA3, section 5.2); tickets from Chisnell 2016 (practice); analytics uses from Cardello, NN/g, 2013; tests from section 6.4, methods by stage from Tankala, NN/g, 2024, and for tickets the IA11 table in 'What later units take'. Tone 1 perqo.com (the Help centre), tone 3 the Perqo app, tone 4 Perqo Admin, tone 5 shared: tickets reach every surface. Perqo is fictional.",
 "cols": ["Shows", "Hypothesis", "Test (IA11)", "Changes"],
 "rows": [
  {"label": "Search log", "tone": 1, "cells": ["zero results, frequent queries, reformulations", "a structure hides what is wanted, or a content gap", "tree test or first-click test", "vocabulary and search synonyms; Help centre articles (H-)"]},
  {"label": "App paths", "tone": 3, "cells": ["loops, detours through Help or search, exits", "most app visits are not one or two tasks begun from Home or a notification", "tree test or first-click test of the app's labels", "the app's labels and routes (A-)"]},
  {"label": "Admin paths", "tone": 4, "cells": ["first actions after sign-in; failed sign-ins", "landing pages miss HR's and finance's most frequent work; employees look for the app on AD-0", "tree test or first-click test of Admin's structure", "the landing pages; AD-0, the sign-in screen (DL-002)"]},
  {"label": "Support tickets", "tone": 5, "cells": ["tags by screen, page or DT- tree; the words people use", "problems cluster on the tagged screen, page or rule", "first-click tests on the same screens", "the tagged screen, page or DT- tree"]}]}
```

The loop runs back as well as forward. A test that confirms the structure closes the hypothesis in the decision log as declined, with the test as its reason; a test that fails it raises a change, which runs the flow of section 4.2. Where no test can be run, IA12's assumption register holds the hypothesis as assumed, with its test named, until one can (IA8, "What later units take").

## Deliverable · The Perqo IA workflow, definitions of done and maintenance cadence

*Face of this artefact (IA2, the notation sheet): process specification for Perqo's IA, in four parts: A, the IA workflow across one product cycle, W-01 to W-17; B, the definition of done for each artefact in IA2's catalogue, at each fidelity; C, the maintenance cadence, RV-01 to RV-12; D, the change control: the routing rule, the flow, the decision log's format and its first entries, DL-001 to DL-010. Fidelity F2 (complete for its scope; every identifier stable). Decision: what IA work each stage of a Perqo cycle does, with which artefact, who owns it and who is consulted and told; when each artefact is done; how the IA is kept current; how a change is made. Readers: the IA designer, product management, engineering, content, sales, support and clients (each row names its own); IA10 for the touchpoints; IA11 and IA12 for the signals and assumptions; DD-IA3 for change control at scale. Leaves out: the validation methods (IA11), work without research or stakeholders (IA12), localisation (DD-IA3), the sprint's length, named people. Owner: the IA designer; version 1, dated 9 November 2026; every cadence and every practice set here is assumed until tested ("What later units take"); Perqo is fictional.*

The functions in the owner, consulted and informed columns are the course goal's six (product management, engineering, content, sales, support, clients), with the IA designer, who owns the artefacts, and the IA review (section 4.1). Content means the content team; marketing, which co-owns perqo.com's inventory (IA5, Deliverable A), is consulted where perqo.com is touched.

### A · The IA workflow across one Perqo product cycle

One cycle (Perqo, fictional) runs Discover, Define, Develop and Deliver on the two tracks of section 1.3, with discovery one step ahead of delivery, and then Run, where the product is in use and the next cycle's signals are read. Identifiers are those of IA4 to IA8 and this unit.

| ID | Stage | IA activity | Artefact (fidelity) | Owner | Consulted | Informed |
|---|---|---|---|---|---|---|
| W-01 | Discover | Read the signals and the open decision log entries that opened the cycle | RV-04 to RV-06 outputs; DL entries proposed or accepted; open gaps (G-5 to G-7) | IA designer | support; product management | content; engineering |
| W-02 | Discover | Inventory and audit everything the work touches, on every surface it reaches | content inventory and audit (F2): S-, H-, A-, AD- rows with owner and status | IA designer | content; support; marketing for perqo.com | product management |
| W-03 | Discover | Collect the words people use for the things the work touches | controlled vocabulary (F1): a word list, each word with its source (log, ticket, client, sales) | content | support; sales; clients | engineering |
| W-04 | Discover | Find the nouns and the crossings | object map (F1); cross-surface map (F1) for the touched surfaces; service blueprint (F1) where backstage work changes | IA designer | engineering; product management; support | sales |
| W-05 | Define | Frame the scope in IA terms: which surfaces, objects, J- rows and DT- rules the work touches | an impact list citing identifiers; a DL entry for each proposed structural change | product management | IA designer; engineering | support; sales |
| W-06 | Define | Agree the top levels and the labels | sitemap or app map (F1, top two levels); controlled vocabulary (F2: preferred term per surface, variants) | IA designer | content; product management; clients for Admin's labels; sales for perqo.com's | support; engineering |
| W-07 | Define | Draw the story map's backbone under the IA's identifiers before any story is cut | story map: each activity names its screens or pages and objects (section 2.2) | product management | IA designer; engineering | support |
| W-08 | Develop | Draw the candidate structures | sitemap or app map, navigation model, object map, user flows with failure paths, decision trees, state diagrams (all F2) | IA designer | engineering; content; support | product management; sales |
| W-09 | Develop | Test the candidates and label what is untested | test plans and results (IA11); assumptions with their tests (IA12's register) | IA designer | product management; clients and employees as participants; support | engineering |
| W-10 | Develop | Decide: take each proposed change through the routing rule; re-stamp the faces | DL entries accepted or declined; every changed face re-stamped (D.1, D.2) | IA designer, chairing the IA review | product management; engineering; content; support | sales; clients |
| W-11 | Deliver | Take what the next sprint builds to F3, one sprint ahead | wireflows, object-relationship map with model names, decision tables, state transitions, sitemap identifiers (F3) | IA designer | engineering | content; support |
| W-12 | Deliver | Check each story against the IA before it enters a sprint (RV-01) | stories citing identifiers; DL entries for anything new | IA designer | product management; engineering | none |
| W-13 | Deliver | Put the words in place: labels, Help centre articles, search synonyms | vocabulary (F3: synonyms loaded); Help centre articles (H-) | content (labels, vocabulary); support (articles) | IA designer | sales |
| W-14 | Deliver | Check the release (RV-02); for a release touching two surfaces, the cross-surface review (RV-03) | DL entries closed as applied; faces re-stamped; J- rows checked; release note listing IA changes | IA designer | engineering; support | all six; clients for changes their staff will see in Admin |
| W-15 | Run | Read the signals on the cadence (RV-04 to RV-06) | search log read; ticket tags; analytics paths; each finding a hypothesis | support (logs, tickets); product management (paths) | IA designer | content |
| W-16 | Run | Triage the IA debt (RV-10) | DL entries accepted and not applied; open faults ranked by value and effort | product management | IA designer; engineering | support |
| W-17 | Run | Hand the next cycle its inputs | hypotheses to IA11's tests; assumptions to IA12's register; proposed DL entries | IA designer | product management | all six |

Clients are touched at three points: consulted on Admin's labels and structure (W-06), as participants in tests (W-09), and told of Admin changes their staff will see (W-14). Admin changes are announced to clients in the release note (Perqo, fictional). Sales is consulted for the words buyers use (W-03, W-06) and told of every decision that changes what perqo.com or a rule says (W-10, W-14), because sales explains the rules to buyers (IA8, section 4.1).

### B · The definition of done for each artefact

**Every artefact, at every fidelity, is done only when** (section 3.1): (1) its face is complete, including any amendments with their DL entries; (2) it passes IA2's five faults when read by someone who did not make it; (3) every assumption is marked "assumed" with the test that would settle it; (4) the notation is kept and any new symbol is in the legend first; (5) every label is in the controlled vocabulary; (6) every change since the last version has a DL entry naming this artefact.

**Each fidelity adds** (IA2, section 1.0): F1, the shape and main names, every assumption marked, reviewed with the readers named for its stage; F2, complete for its stated scope, in the product's vocabulary, with conditions and exceptions, agreed by the functions consulted for it (W-10); F3, a stable identifier on every element, every condition and state shown, citable by engineering in a ticket.

**An artefact in Run is kept when** its face's date is no older than its last scheduled review (Deliverable C) and no DL entry that names it is accepted and not applied.

| Artefact (IA2) | Done at F1 when | Done at F2 when | Done at F3 when | Perqo's, now |
|---|---|---|---|---|
| Content inventory and audit (1.1) | not used: an inventory is useful only complete for its scope | every item in scope listed with its ID, title, URL, owner, topic and format (Kaley's fields, IA2, section 1.1) and an audit status of keep, update, remove or new, with an owner for each update | adds type, template, audience and F-CAT tags to every row, a redirect target to every removed row, and indexing; it is the migration list engineering builds from | IA5, Deliverable A: F3, version 1, 3 November 2026 |
| Controlled vocabulary (1.2) | a word list, each word with its source (log, ticket, client, sales) | each thing has its preferred term per surface, its variants, broader and narrower terms; content and support have agreed it | every term carries an identifier; variants are loaded as search synonyms; every surface label maps to one model name | IA2, section 5.3 and IA6, section 6.2: F2; DD-IA3 builds it further |
| Taxonomy (1.2) | not used (IA2 gives it F2 in design) | facets pass the not-a-facet test; values do not overlap; the rules for adding a value are written | every facet, value and item has an identifier, used in URLs and filters | IA4, Deliverable B: F2 with F3 identifiers |
| Sitemap, and app map (1.3; IA6) | the top two levels, with page types | every group and page type tagged; for an app, every screen's states, modals and entries | an identifier and a template on every box; URLs, redirects and indexing in the inventory | IA5, Deliverable B: F3; IA6, Deliverable B: F2 with F3 identifiers |
| Navigation model (1.4) | not used | every route type on every surface, each route landing on an identifier; done before navigation components are chosen | rarely needed: the routes live in the sitemap's identifiers | IA2, section 5.3; IA7, Deliverable C: F2 with F3 identifiers |
| Object map (1.5) | the nouns and the main lines | every attribute a screen shows and every action, with who takes it | continues as the object-relationship map | IA4, Deliverable A: F2 |
| Object-relationship map (1.5) | not used | every relationship with a verb and a count at each end | every object and attribute carries its model name, agreed with engineering; every relationship an identifier | IA7, Deliverable A: F3, with record debt (DL-005 to DL-007) |
| Task flow (1.6) | the main path of one task, start to end, named as in the task inventory | continues as a user flow | not used | none drawn; IA6 builds tasks as wireflows (IA2, decision table) |
| User flow (1.6) | not used | every entry point, a branch for each kind of user, and every failure path ending somewhere named | continues as the wireflow | IA6, section 5 |
| Wireflow (1.6) | not used | every screen with its identifier, the failure screens, and where the task cannot be undone | every state of each screen and the text of each error and empty state | IA6, Deliverable C: F2, C.2 amended 9 November 2026 |
| Decision tree (1.7) | the rule in one sentence, in words | every question with two answers, "yes" on the left; every outcome named as the surface names it | a table with one row per path and the Unique hit policy; each outcome mapped to its transition or reason; the sentence for sales | IA8, DT-1 to DT-3: F3 |
| State diagram (1.8) | not used | every state a person sees, with its name on each surface | every transition with its trigger, actor and condition, and what is recorded | IA7, Deliverable D: F3 |
| Service blueprint (1.9) | the lanes, the line of visibility named, the evidence | every step of the changed service, each naming the screen or page it happens on | not used: its build detail moves into flows, rules and lifecycles | IA2, section 5.3: F1; IA8, CL-1 to CL-6 and EL-1 to EL-6 |
| Cross-surface interaction map (1.10) | the surfaces' top levels, the shared objects and the crossings | every crossing with its X- identifier; the layers and their J- rows | the canonical vocabulary engineering maps to | IA8, Deliverable: F2 with F3 identifiers |

**The gate.** A story that builds from an artefact enters a sprint only when that artefact is at F3 for the part the story touches, or at F2 where B gives the artefact no F3 (the navigation model, the blueprint) (section 2.3).

### C · The maintenance cadence

Each review (Perqo, fictional), with what it checks, when it runs, what else triggers it, who owns it and what it produces. Every review ends in decision log entries or none; a review that finds nothing records the date it ran on the faces it checked.

| ID | Review | Checks | Cadence | Trigger | Owner | Consulted | Output |
|---|---|---|---|---|---|---|---|
| RV-01 | Story check | each story cites the identifiers it touches; anything new has a DL entry; the artefact it builds from is at the fidelity B requires | each story, before it enters a sprint | none | IA designer | product management; engineering | DL entries proposed; stories held |
| RV-02 | Release check | every DL entry the release carries is applied; each changed face is re-stamped; the built screens and pages match the F3 artefacts | each release | none | IA designer | engineering; support | DL entries closed as applied; build debt logged |
| RV-03 | Cross-surface review | each J- row and X- crossing against the surface maps it cites (IA8, section 6) | quarterly | each release touching two surfaces | IA review | sales; clients where a crossing reaches them | J- and X- rows confirmed or DL entries |
| RV-04 | Search log | the Help centre's logs for both audiences: zero results, frequent queries, reformulations, grouped by need (IA3, section 5.2) | quarterly | a release that renames a label: the next month's log, for the old word | support | content; IA designer | hypotheses for IA11; variant terms for RV-07 |
| RV-05 | Support tickets | ticket tags by surface, screen or page and DT- tree; the words people use | monthly | a tag that rises after a release touched its screen | support | IA designer | hypotheses for IA11; variant terms for RV-07 |
| RV-06 | Analytics paths | loops, detours through Help or search, exits; first actions after sign-in; Admin's failed sign-ins | quarterly across all screens | each release, for the screens it changed | product management | IA designer; engineering | hypotheses for IA11; IA6 and IA7's analytics assumptions read |
| RV-07 | Vocabulary | new variants from RV-04 and RV-05 against IA4's rules R1 to R10; synonyms in search | quarterly | a new variant; a new client's terms; a proposed F-CAT value | content team | support; engineering | DL entries; synonyms loaded |
| RV-08 | Rolling audit | one slice of perqo.com's inventory: status, owner, F-CAT tags, redirects | quarterly | before any redesign of a surface: a full audit at F2 | content team | page owners; marketing | inventory rows updated; DL entries |
| RV-09 | Face audit | each artefact's face date against the last DL entry that names it | quarterly | none | IA designer | none | faces re-stamped; record debt logged |
| RV-10 | Debt triage | DL entries accepted and not applied; open gaps; open faults from RV-04 to RV-06 | quarterly | none | product management | IA designer; engineering | IA debt ranked by value and effort on the backlog (Kaley 2018) |
| RV-11 | Structure test | the touched structure, before and after, by IA11's method | on trigger only | a change to a top level or a tab; a hypothesis from RV-04 to RV-06 | IA designer | product management; support | results; DL entries confirmed or declined |
| RV-12 | Rules review | DT-1 to DT-3 and every J- row with a cell in the decision layer (IA8, D.4) | on trigger only | a change to contract terms, a policy option or a decline reason | product management | engineering; sales; clients | DT- trees and tables amended; DL entries |

### D · The change control

**D.1 · Who decides** (section 4.1). Anyone may propose. A change to a rule, or one touching two surfaces: the IA review decides, product management signs off; a new top-level benefit category also goes to finance and the client (IA4, R8). A rename or a retired identifier: the IA review decides, vocabulary first. A value in the benefits taxonomy: the content team, by R1 to R10. Anything else, inside one surface and renaming nothing: the IA designer. Every decision is logged.

**D.2 · The flow, and the face** (sections 4.2 and 4.4). Raise; log as proposed; check the impact by identifier, J- row, X- crossing and DT- rule; route; decide (a declined change is logged with its reason); change the vocabulary first; change the artefacts, keeping identifiers and re-stamping each face; tell the informed functions; close the entry as applied. A change that breaks a citation (an identifier retired or moved, a label renamed, a relationship or transition removed, a rule's outcome changed) makes a new version; any other change is a dated amendment. The face reads "version N, dated D; amended D2 (DL-nnn)".

**D.3 · The decision log.** One list, kept by the IA designer. Each entry: ID (DL-001 onward, never reused); the change in one line; raised by and from what; artefacts and identifiers touched, and J- rows; alternatives considered; who decides; decision, date and reason; places to apply, each done or not; functions told and when; superseded by or supersedes. Statuses: proposed, accepted, declined, applied, superseded; an accepted entry is superseded, never edited. The first ten entries record the decisions the filed units have taken, from their dated notes (Perqo, fictional):

| ID | Change | Decided by, date | Applied in | Not yet applied | Status |
|---|---|---|---|---|---|
| DL-001 | IA3's eight proposals for the app (Card offers in one placing, four balances on Home, Claims by four states, New claim labelled, Your balance explained, Help opens For employees, the rule line on New claim, Documents removed) | IA6, Deliverable B, B.1; 3 November 2026 | IA6, Deliverable B; IA3's "What IA6 keeps" note | none | applied |
| DL-002 | Admin's sign-in screen carries "Looking for your benefits? Get the Perqo app" for everyone (IA5's proposal, taken with one change) | IA7, Deliverable C, C.5; 3 November 2026 | IA7, C.5; IA5, section 5.5 note; IA6, B.4 note | none | applied |
| DL-003 | Admin shows the card as "Perqo card", status only; Admin does not show notifications | IA7, section 2.3; 3 November 2026 | IA7, Deliverable A; IA4, Deliverable A, the note on "What IA7 may do with it"; IA6, section 6.2 | none | applied |
| DL-004 | A declined card attempt sends a notification and makes no record in Purchases; object O-18, relationship R-25, entry E-8 | IA8, section 4.5; 9 November 2026 | IA6, C.2 and its face, B.4, A-5, A.2, facts and assumption rows; IA4, note after A.4 | the faces of IA6, Deliverable B and IA4, Deliverable A: amendment lines | accepted |
| DL-005 | On Left: card Cancelled, allocations closed, claims still decided, the remainder reported as unspent | IA8, section 3.4; 9 November 2026 | IA7, facts row and the note in "What IA8 and later units take"; IA4, note after A.4 | IA7, A.1 row O-09 and section 5.1's table: add Cancelled; IA7, A.2: O-09 status value `cancelled`, O-06 attribute closed → `closed` (proposed names); IA7, section 2.3: Cancelled beside Active, Frozen, Not issued; faces of IA4, A and IA7 | accepted |
| DL-006 | Client attribute contract end date, read only on Company (AD-6.1); churn the day after it | IA8, section 3.2; 9 November 2026 | IA4, note after A.4 | IA7, A.2: O-01 contract end date → `contract_end_date` (proposed name); IA7, A.5, figure 1, the client box's attributes; faces of IA4, A and IA7 | accepted |
| DL-007 | Invite employees unavailable for a group until its budgets for the current period are set, shown disabled with "Set this group's budgets first" | IA8, section 3.2; 9 November 2026 | IA7, the note in "What IA8 and later units take" | IA7, A.4: the condition on employee group -> invite employees and employee -> invite; IA7, C.4: the condition on Invite employees (AD-1.3); face of IA7 | accepted |
| DL-008 | A category open with no allocation for the period shows "Your budget for this period is not set yet"; no payment or claim there | IA8, section 4.2; 9 November 2026 | IA8, DT-1 | IA6, B.5: a new Empty-state row on the category screen, "[no allocation this period] Your budget for this period is not set yet"; face of IA6, Deliverable B | accepted |
| DL-009 | The model keeps `allocation`; Admin keeps the label Budget | IA8, Deliverable, D.1; 9 November 2026 | IA7, the note in "What IA8 and later units take" | none | applied |
| DL-010 | The version and amendment rule for faces (section 4.4), applied to IA2, section 4 and the notation sheet | IA9, section 4.5; proposed 9 November 2026 | none yet | IA2, section 4 and the notation sheet; then DL-004 to DL-008's face lines | proposed |

DL-004 to DL-008 are Perqo's IA debt at the date of this unit: decisions accepted and not applied everywhere. DL-010 is decided by the filing of this unit; once it is applied, the faces DL-004 to DL-008 name can be re-stamped by its rule.

*Note, 9 November 2026: the filing of this unit accepted and applied DL-010 and applied every place in the column "Not yet applied", so DL-004 to DL-008 and DL-010 are now applied and the debt above is cleared (section 4.5's note). The table keeps the state at the unit's date, as the log keeps its history.*

## What later units take

**IA10** builds the briefs for the touchpoints. It takes Deliverable A's owner, consulted and informed columns, by function, as the list of when each touchpoint enters a Perqo cycle; Deliverable C's owners and consulted functions as each touchpoint's standing duties once the IA is in use; and the decision log's "told" field as the record of what each touchpoint has been told.

**IA11** specifies the validation methods. It takes the signals of section 6 and RV-04 to RV-06 as the production source of its hypotheses, RV-11 as the trigger for a structure test before and after a change, and the rule that a confirmed hypothesis closes as declined with the test as its reason (section 6.4). Every practice this unit sets is assumed, with its test:

| Practice or assumption | Where | Test (IA11) | What changes if it fails |
|---|---|---|---|
| Stories citing identifiers keeps build debt down | section 2.3; RV-01 | at RV-02, the share of built screens that differ from their F3 artefact, compared from quarter to quarter | the story check, or the gate on F3 |
| The F3 gate does not slow delivery | section 2.3; B, the gate | product management's record of stories held at RV-01, read at RV-10 | the gate relaxed to F2 for some artefacts |
| A quarterly face audit keeps record debt from building | RV-09 | the count of DL entries accepted and not applied, at each RV-10 | a face check at each release |
| Ticket tags locate problems on the IA | section 6.2; RV-05 | support's tags compared with first-click tests on the same screens | the tag set |
| The routing rule sends changes to the right decider | section 4.1 | the DL entries reopened or superseded within a quarter, read at RV-10 | the rule's questions or their order |

**IA12** works without inputs. Its assumption register takes the cadence as its loop back: each review in Deliverable C can settle the assumptions whose test is a log, a ticket tag or a path, so the register names, for each assumption, the RV- review that will read it.

**DD-IA3** takes the change control (section 4; Deliverable D) as the base it extends for change at scale: the routing rule, the flow, the log's format and statuses, and the version rule, to be extended for several languages and markets, where one change runs through every language version of a page (IA5, section 5.3).

## Perqo facts set by this unit

Every fact below is a course convention (Perqo, fictional), never evidence about the world. Each keeps every registered fact; none renames an IA1 to IA8 label, object, attribute or relationship.

| Fact | Set in | Left free |
|---|---|---|
| A Perqo cycle runs Discover, Define, Develop and Deliver, with discovery one step ahead of delivery, then Run | section 1.4; Deliverable A | none |
| Engineering delivers in sprints and releases at the end of each sprint; each release note lists the surfaces it touches; Admin changes clients' staff will see are announced to clients in the release note | section 2.3; Deliverable A, W-14 | the sprint's length |
| Every story cites the IA identifiers it touches; IA debt items are backlog items tagged "IA debt"; a story enters a sprint only when the artefact it builds from is at F3 for its part (F2 for the navigation model and the blueprint) | section 2.3; Deliverable B | none |
| The IA designer owns the canonical IA artefacts, other than the benefits taxonomy (the content team's), and the decision log | section 4.1 | none |
| The IA review: the IA designer (chair), product management, engineering, the content team, support; it holds IA8's review; sales and clients are told of its decisions | section 4.1 | none |
| The routing rule for changes (D.1) | section 4.1 | none |
| The change-control flow (D.2) | section 4.2 | none |
| The decision log: identifiers DL-001 onward, never reused; its fields; statuses proposed, accepted, declined, applied, superseded; entries DL-001 to DL-010 | section 4.3; Deliverable D, D.3 | none |
| A new version for a change that breaks a citation; a dated amendment naming its DL entry otherwise | section 4.4 | none |
| Proposed model names, for engineering to confirm: card status value `cancelled`; allocation attribute closed → `closed`; client attribute contract end date → `contract_end_date` | Deliverable D, D.3 (DL-005, DL-006) | the final names |
| Support tags each ticket with the surface, the screen or page identifier and, for a rule, the DT- tree, and reads the tags monthly | section 6.2; RV-05 | the tag set beyond these |
| Product analytics record each app screen view by screen identifier and each Admin page view by page identifier | section 6.3 | what else is recorded |
| The Help centre's logs for both audiences are read quarterly by support (extends IA3's E2, which named the For employees log) | section 5; RV-04 | none |
| Workflow rows W-01 to W-17; reviews RV-01 to RV-12 with their cadences, triggers and owners | Deliverables A and C | none |

## Sources

- Agile Alliance. "What is Story Mapping?" Agile Glossary, 17 December 2015, modified 9 March 2023 (practice). [agilealliance.org, story mapping](https://www.agilealliance.org/?p=5003329)
- Aizlewood, Jon. "Agile and design: how to avoid Frankensteining your product". Clearleft, 24 July 2019 (practice). [clearleft.com, Frankensteining](https://clearleft.com/thinking/agile-and-design-how-to-avoid-frankensteining-your-product)
- Brhel, Manuel, Hendrik Meth, Alexander Maedche and Karl Werder. "Exploring principles of user-centered agile software development: A literature review". *Information and Software Technology* 61 (2015): 163 to 181 (abstract read). [doi.org, Brhel 2015](https://doi.org/10.1016/j.infsof.2015.01.004)
- Cagan, Marty. "Dual-Track Agile". Silicon Valley Product Group, 17 September 2012 (practice). [svpg.com, dual-track agile](https://svpg.com/dual-track-agile)
- Cardello, Jen. "Three Uses for Analytics in User-Experience Practice". Nielsen Norman Group, 17 November 2013. [nngroup.com, analytics uses](https://www.nngroup.com/articles/analytics-user-experience/)
- Chisnell, Dana. "Call centers as a source of data". danachisnell.com, 24 July 2016, modified 9 April 2025 (practice). [danachisnell.com, call centers](https://danachisnell.com/call-centers-as-a-source-of-data/)
- Design Council. "Framework for Innovation". Undated page, checked 9 November 2026 (organisation's methodology). [designcouncil.org.uk, framework for innovation](https://www.designcouncil.org.uk/resources/framework-for-innovation/)
- Dimmick, Damon. "Fitting Big-Picture UX Into Agile Development". *Smashing Magazine*, 6 November 2012 (practice). [smashingmagazine.com, design spikes](https://www.smashingmagazine.com/2012/11/design-spikes-fit-big-picture-ux-agile-development/)
- Fowler, Martin. "Architecture Decision Record". martinfowler.com, 24 March 2026 (practice; credits Michael Nygard, "Documenting Architecture Decisions", 2011, not read). [martinfowler.com, decision record](https://www.martinfowler.com/bliki/ArchitectureDecisionRecord.html)
- Garrett, Jesse James. "The Elements of User Experience" (diagram). 30 March 2000. [jjg.net, elements diagram](https://www.jjg.net/elements/pdf/elements.pdf)
- Garrett, Jesse James. *The Elements of User Experience: User-Centered Design for the Web and Beyond*. 2nd ed. New Riders, 2011. Ch. 2, "Meet the Elements"; chs 3 to 7.
- Kaley, Anna. "UX Debt: How to Identify, Prioritize, and Resolve". Nielsen Norman Group, 11 November 2018. [nngroup.com, UX debt](https://www.nngroup.com/articles/ux-debt/)
- Patton, Jeff. "Dual Track Development is not Duel Track". Jeff Patton & Associates, 10 May 2017, updated 12 April 2023 (practice; quotes Sy 2007). [jpattonassociates.com, dual track](https://jpattonassociates.com/dual-track-development/)
- Patton, Jeff. *User Story Mapping: Discover the Whole Story, Build the Right Product*. O'Reilly, 2014 (practice).
- Preston-Werner, Tom. *Semantic Versioning 2.0.0* (specification). [semver.org](https://semver.org/)
- Rosenfeld, Louis, Peter Morville and Jorge Arango. *Information Architecture: For the Web and Beyond*. 4th ed. O'Reilly, 2015. Part III, chs 11 to 13. Contents at [oreilly.com, book contents](https://oreilly.com/library/view/information-architecture-4th/9781491913529); ch. 13 at [oreilly.com, ch. 13](https://www.oreilly.com/library/view/information-architecture-4th/9781491913529/ch13.html).
- Schwaber, Ken, and Jeff Sutherland. *The Scrum Guide*. As quoted by Scrum.org (the page names no edition), "What is a Definition of Done?", undated (practice framework). [scrum.org, definition of done](https://www.scrum.org/resources/what-definition-done)
- Sy, Desirée. "Adapting Usability Investigations for Agile User-centered Design". *Journal of Usability Studies* 2, no. 3 (2007) (not read; cited as Patton 2017 quotes and credits it).
- Tankala, Samhita. "Card Sorting vs. Tree Testing". Nielsen Norman Group, 23 February 2024. [nngroup.com, card sort vs tree test](https://nngroup.com/articles/card-sorting-tree-testing-differences)
- Welchman, Lisa. *Managing Chaos: Digital Governance by Design*. Rosenfeld Media, 2015. Ch. 5 (publisher's description and contents). [rosenfeldmedia.com, Managing Chaos](https://rosenfeldmedia.com/?p=187514)
- Cited through the filed units, for claims made there: Arango, *Living in Information*, 2018 (IA1); Evans, *Domain-Driven Design Reference*, 2015 (IA7); Farrell, "Search-Log Analysis", NN/g, 2017 (IA3); Halvorson and Rach, *Content Strategy for the Web*, 2nd ed., 2012, ch. 9 and index (IA1, IA5); Mausser, "Site Search Analytics: A Conversation with Lou Rosenfeld", UXmatters, 2011 (IA3; interview, practice); Kaley, "Content Inventory and Auditing 101", NN/g, 2020 (IA2). Full references in IA1, IA2, IA3, IA5 and IA7, Sources.

## Unsure list

- Garrett 2000: the time axis from conception to completion and the statement that the model does not describe a development process or define roles are from knowledge of the diagram; they were not re-checked against jjg.net for this unit.
- Garrett 2011, ch. 2: that work on a plane cannot finish before work on the plane below has finished, and that Garrett rejects finish-before-start, is paraphrased from knowledge of the book; the wording and page were not checked.
- Patton 2014: that the book calls the row of activities the backbone was written from knowledge; the Agile Alliance glossary, which was read, does not use the word. The fresh check found the book's index entry "backbone (story map)" and its section "Distill Your Map to Make a Backbone" ([oreilly.com, story mapping index](https://www.oreilly.com/library/view/user-story-mapping/9781491904893/ix01.html)).
- Sy 2007: volume and issue from knowledge; the paper was not read, and only Patton's quotation of it is used.
- Brhel and others 2015: the five principles are quoted from the abstract as indexed; the review's method and findings beyond the abstract were not read.
- Scrum Guide: the Definition of Done is quoted as Scrum.org's page gives it, and the page names no edition; the Guide itself was not opened.
- Fowler 2026: the page's date as the fetch reported it; Nygard's 2011 article was not read.
- Kaley 2018: the UX-debt definition is paraphrased; the quoted causes and the phrase "navigation structures and content classification" are as the page was read through a summary.
- Rosenfeld, Morville and Arango 2015, ch. 13: only the chapter's preview and headings were seen.
- Object: the Perqo IA decision log, section 4.3 and Deliverable D
