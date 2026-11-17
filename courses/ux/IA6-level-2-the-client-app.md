---
code: IA6
title: Level 2 · the client app
course: ux · IA · Information Architecture
model: Opus 5.5
written: 2026-11-03
search: off
---

# IA6 · Level 2 · the client app

IA5 spent the first five units' tools on perqo.com, the shallow website. This unit spends them on the second surface, the Perqo app (Perqo, fictional), which IA1 called small and task-driven, with an IA problem of reduction: deciding what an employee needs on one screen, and naming it in their words (IA1, section 5). It covers task analysis as the ground an app's IA stands on, the app map and how it differs from a sitemap, the mobile navigation patterns and the evidence on each, four decisions that look like interface detail and are IA (progressive disclosure, empty states, error states, permissions), the step from a user flow to a wireflow, and how the app stays consistent with the website's labels and the backoffice's objects. The deliverable is the Perqo app's task inventory, its app map, and three core flows drawn as wireflows. Every figure uses IA2's notation (IA2, section 5 and the notation sheet); on a figure of one surface every box takes that surface's tone, so every app box is tone 3, and tone 6, IA2's stop, marks a state where the path ends without success, or a fault found in a review (IA2, section 5.2).

The filed units handed this one eight questions by name. Where each is answered:

| Handed on by | The question | Answered in |
|---|---|---|
| IA3, Deliverable (the as-is navigation, its sitemap, the verdicts table) | every fix in the "Fix (for IA6)" column made in the app map | Deliverable B, B.2 |
| IA3, "What IA6 keeps" | every label the checklist passed kept | Deliverable B, B.2 and B.6 |
| IA3, "What this hands on" | navigation chosen by A1 to A5, B1, B2, F1 and F2 | section 3.5 |
| Register, "Proposed for IA6, not facts yet" (from IA3) | each proposal taken or struck | Deliverable B, B.1 |
| IA4, Deliverable A (object map; A.3 calls to action; "Views are not objects"; "What the map hands on"); the figure note "Rank attributes and calls to action"; section 5's addressing rules | screens that agree with the objects; complexity and priority of the app's calls to action; Home in the app map and wireflows; flows from claim, card, allocation, offer and notification; attributes ranked; deep links that follow the addressing rules | section 6; Deliverable A, A.2; Deliverable B, B.3 and B.4; Deliverable C |
| IA4, "What IA5 and DD-IA3 take" | the catalogue items on each category screen as its examples (IA3, C2) | Deliverable B, B.3 |
| IA2, decision table (user flow, task flow, wireflow · IA6); section 5.3's claim wireflow; the notation sheet | the three artefacts, the claim wireflow extended and kept consistent | section 5; Deliverable C, C.3 |
| IA5 (Benefits and its four categories, the Help centre's audiences and topics, the preferred terms, Get the Perqo app, S-6) | labels consistent with perqo.com; the app's entry points | section 6; Deliverable B, B.4 |

## 1 · Task analysis as the basis of an app's IA

### 1.1 · What a task analysis records

Maria Rosala's NN/g article defines the method in one line: "Task analysis is the systematic study of how users complete tasks to achieve their goals" ("Task Analysis: Support Users in Achieving Their Goals", Nielsen Norman Group, 20 September 2020, [nngroup.com/articles/task-analysis](https://www.nngroup.com/articles/task-analysis/)). She describes two stages: gathering information on goals and tasks by observing and speaking with users or subject-matter experts (her methods include contextual inquiry, critical-incident interviews, record keeping, activity sampling and simulations), then analysing the tasks, structuring what was observed by order, hierarchy, frequency, cognitive demands and physical requirements, usually as a diagram. The most common diagram is the hierarchical task analysis, which starts from a goal and a scenario, breaks the goal into tasks and the tasks into subtasks, and records in "plans" the order and the conditions under which steps are done (Rosala 2020). JoAnn Hackos and Janice Redish's *User and Task Analysis for Interface Design* (Wiley, 1998) is the book-length treatment of the same method for interface design; this unit draws no claim from it.

For an app's IA, three of Rosala's dimensions do the work, and this unit adds a fourth from Perqo's domain:

- **The task**, named in the person's words and tied to the object it acts on. The objects and their calls to action are IA4's (IA4, Deliverable A, A.3), so each task row names its object and call to action.
- **Frequency**: how often the task is done. It decides what sits on the first screen and what one level down (section 1.2).
- **Sequence**: what comes before and after the task. It decides which screens link to which, and it becomes the flows (section 5).
- **Money at stake**: whether a failure costs the person money or a wrong charge. In a benefits app a rare task can matter more than a frequent one, so priority is frequency raised by consequence. Rosala does not name this dimension; it is this unit's addition for the domain.

The inventory also records the actor and the surface, because a task in the app often depends on one done elsewhere: an employee's claim over the limit waits on HR in Perqo Admin, and a card payment happens at a merchant's till (Perqo, fictional; IA2, section 5.3; IA4, Deliverable A).

### 1.2 · Frequency and sequence decide placement

The measured case for placing by frequency comes from menu research. Andrew Sears and Ben Shneiderman moved the few most frequently chosen items to the top of menus, above the rest, and in field studies "performance times were reduced by 17 to 58% depending on the site and menus"; in a controlled experiment split menus were significantly faster than alphabetical ones and preferred ("Split Menus: Effectively Using Selection Frequency to Organize Menus", *ACM Transactions on Computer-Human Interaction* 1, no. 1, 1994, pp. 27 to 51, abstract, [pure.psu.edu](https://pure.psu.edu/en/publications/split-menus-effectively-using-selection-frequency-to-organize-men/)). The result is about desktop pull-down menus; the step to an app's first screen is this unit's inference, and a short one: the first screen and the tab bar are the app's top-of-menu.

Jakob Nielsen's rule for progressive disclosure says the same from the other end: the initial display must hold what people frequently need, and "Progressive disclosure defers advanced or rarely used features to a secondary screen" ("Progressive Disclosure", Nielsen Norman Group, 3 December 2006, [nngroup.com/articles/progressive-disclosure](https://nngroup.com/articles/progressive-disclosure/); NN/g guidance). Gerry McGovern's top-tasks practice, which IA5 used for the website, reports that a few tasks take a share of the vote out of all proportion to their number (in one vote, three of 67 tasks took the first quarter of it), and that the same pattern has emerged in every one of the more than 400 such projects he has run (McGovern, "What Really Matters: Focusing on Top Tasks", A List Apart, April 2015, republished by Center Centre, 20 January 2016, [articles.centercentre.com](https://articles.centercentre.com/?p=877); practice, a consultant's own data; IA5, section 2.2).

Sequence decides the links. A task whose next step is nearly always the same task (check the Learning balance, then claim a course) earns a direct route between the two screens, so the person does not climb back to a tab to start the second. A task whose steps are independent of each other suits staged disclosure, "a variant in which users step through a linear sequence of options, with a subset displayed at each step" (Nielsen 2006); Nielsen adds that staging is useful when the steps have little interaction between them and a problem when they depend on each other. New claim followed by Check and submit (IA2, section 5.3) is a staged sequence of two.

### 1.3 · Organising by task rather than by feature: the evidence and its limits

An app organised by feature has a top level that names the organisation's parts: the scanner, the wallet, the perks programme, the documents library. An app organised by task has a top level that names the clusters of things people come to do. The evidence for the second is real and indirect.

- **People come to do a task.** John Carroll and Mary Beth Rosson's "paradox of the active user" described what IBM's user studies of the early 1980s kept finding; in Nielsen's summary, "Users never read manuals but start using the software immediately", and "They are motivated to get started and to get their immediate task done" (Nielsen, "Paradox of the Active User", Nielsen Norman Group, 4 October 1998, [nngroup.com/articles/paradox-of-the-active-user](https://www.nngroup.com/articles/paradox-of-the-active-user/), reporting Carroll and Rosson, "The Paradox of the Active User", in J. M. Carroll, ed., *Interfacing Thought: Cognitive Aspects of Human-Computer Interaction*, MIT Press, 1987; the original was not seen). A structure that names the organisation's features asks the person to learn the system first.
- **A feature structure is the implementation model on the screen.** Cooper and his co-authors argue that a product whose represented model follows how the software is built, and not the user's mental model, is hard to use (*About Face*, 4th ed., Wiley, 2014, ch. 1; IA3, section 2.1).
- **Scent is judged from the person's goal.** People choose the link whose words best predict what they are after and leave when the prediction fails (Card and others, *CHI 2001*; Budiu, NN/g, 2020; IA3, section 1). A goal arrives in the person's words for the task and its object; a feature name the organisation coined carries no scent until it is learned (Nielsen, "Use Old Words When Writing for Findability", NN/g, 2006; IA3, section 4.2).
- **NN/g's navigation guidance ties one pattern to task-based products.** Raluca Budiu writes that a navigation hub "can work well in task-based websites and apps" ("Basic Patterns for Mobile Navigation: A Primer", Nielsen Norman Group, 15 November 2015, [nngroup.com/articles/mobile-navigation-patterns](https://www.nngroup.com/articles/mobile-navigation-patterns/); NN/g guidance).

The limit: this unit knows of no controlled study that compares a task-organised app navigation with a feature-organised one on the same content. The case rests on the observations above, on the scent research, and on practice. It is a strong case, and it is not a measurement.

Two cautions keep the rule from going wrong. Task-based does not mean verb labels: IA5 found that task labels on a website tend to start with verbs of the same kind and fail IA3's A2 (IA5, section 2.2; Nielsen, "First 2 Words", NN/g, 2009), and Laubheimer counts conversational "I want to…" labels among the low-scent faults ("3 Common IA Mistakes", NN/g, 16 April 2023; IA3, section 1.2). And tasks overlap, so a strict tree of tasks duplicates screens. The working rule this unit takes from those findings: **organise by task, label by the object the task acts on.** Each top-level destination is the home of one cluster of tasks and carries the name of the object those tasks act on, in the person's word for it; each task starts from exactly one such home, and a task whose sequence crosses two homes gets a direct route between them.

The Perqo app's five tabs already pass that rule (Perqo, fictional): Home (seeing where the money stands), Benefits (finding what is covered), Claims (getting money back), Card (paying and checking purchases) and Account (one's own details and messages) each name an object or a place in the employee's words (IA1, section 5). The as-is faults IA3 found were feature and organisation labels slipped in beside them: "Perks" and "Discover" for a partnerships programme, "Documents" for a library Product keeps for HR (IA3, Deliverable, C1, C4, D1). This unit removes those and keeps the tabs.

### 1.4 · A task analysis without research

Rosala's first stage is observation and interviews. Perqo has none yet for the app (Perqo, fictional), so this unit runs the analysis from desk sources and labels every result assumed, as IA12 will ask of any IA built without research:

- **The goals and calls to action in IA4's object map**: the employee's goal statement ("See my balance per category, pay with my card, claim back a receipt, see my purchases, read notifications, find card offers") and the calls to action on each object (IA4, sections 4.2 and A.3).
- **The Help centre's search log**: "refund", "allowance", "rejected claim", "gym" and "approval" are tasks and objects in employees' own words (IA3, section 5.2).
- **The as-is app's faults**, each a task that the structure made hard (IA3, Deliverable).
- **Frequencies**, which no source gives. IA3 assumed that the app is opened a few times a month (IA3, section 6.2); Deliverable A gives each task an assumed frequency inside that, to be replaced by measured use (IA11).

One task drawn as a hierarchical task analysis, in Rosala's form, shows what the inventory's "comes after" column summarises (Perqo, fictional):

- **0 · Get money back for a course paid another way** (goal)
  - 1 · Check that the course is covered and how much is left in Learning (Benefits, Learning)
  - 2 · Pay for the course and keep the receipt (outside the app)
  - 3 · Submit the claim
    - 3.1 · Open New claim
    - 3.2 · Choose Learning
    - 3.3 · Enter the amount
    - 3.4 · Add the receipt: 3.4.1 take a photo, or 3.4.2 choose a file
    - 3.5 · Check and submit
  - 4 · Follow the claim to Paid
- **Plan 0**: do 2, then 3, then 4; do 1 before 2 when unsure whether the course is covered.
- **Plan 3.4**: do 3.4.1 if the camera may be used; otherwise 3.4.2.
- **Plan 4**: wait for the notification; if the claim is Rejected, read why.

The plans are where the IA decisions hide. Plan 0 says Learning's screen needs a route to New claim with Learning already chosen; plan 3.4 says the receipt field needs two ways in (section 4.4); plan 4 says a rejected claim must be readable where claims are listed (IA3, B2).

## 2 · The app map, and how it differs from a sitemap

IA2 defined the structural sitemap as a drawing of what exists on a surface and what sits under what, with a box for each page or page type (IA2, section 1.3; Brown, *Communicating Design*, 2nd ed., 2011, ch. 5). IA3 drew the as-is app as a sitemap, which was enough to judge its labels. To build an app from, a sitemap leaves out four things an app has, and this course's app map adds them. The name "app map" has no fixed definition in the standard works this unit cites; the definition below is this course's convention.

| | Sitemap (IA2, IA5) | App map (this unit) |
|---|---|---|
| A box is | a page or a page type, with a URL | a screen, with an identifier and an address that links can open (section 6.3) |
| One box can be | one state | a screen in several states, each written as a [condition] in its note |
| Layers | none | modals and system prompts over a screen, marked "modal" in the note |
| Ways in | the home page, search engines, links | each named entry, marked "entry:" in the note: opening the app, a notification, an invitation, a link from perqo.com |
| Global routes | header and footer | the tab bar, on every screen but the sign-in screens and modals |
| Leaves to another artefact | flows | flows (the wireflows) and lifecycles (the claim's state diagram, IA2, section 5.3) |

Each addition has a source in the course's notation or the literature. **States**: Garrett's vocabulary already had the conditional area, a group of pages shown only when a condition holds, which IA2 reduced to a box whose note opens with the condition in square brackets (IA2, section 5.1). On an app the condition more often changes one screen than hides a page: the Claims screen with no claims, the Card screen before a card is issued. **Modals**: Laubheimer notes that the next step in a wireflow need not be a new page; it can be the same page showing a result, such as "a confirmation popup, a color change, or an error message" ("Wireflows: A UX Deliverable for Workflows and Apps", Nielsen Norman Group, 4 December 2016, [nngroup.com/articles/wireflows](https://www.nngroup.com/articles/wireflows/)). A map that omits the layers omits screens people make decisions on. **Entry points**: Android's documentation describes deep links as letting apps "bring users directly into your app content from links they have tapped, such as from web browsing, search, notifications and more" (Android Developers, "About deep links", page updated 28 October 2026, [developer.android.com/training/app-links](https://developer.android.com/training/app-links); platform documentation). A person who arrives from a notification lands on a screen below the top of a tab, with no route walked to get there, so that screen has to confirm where they are on its own (IA3, A3). **The persistent tab bar**: Budiu lists persistence as the tab bar's advantage, since it stays on screen as the person scrolls (Budiu 2015), which makes the tab bar a route from every screen that carries it.

The notation is kept; three note words and one identifier scheme are added, under IA2's rule "Keep the notation; extend the legend" (IA2, section 4): "modal" (a layer over its parent screen, closed to return to it); "entry:" followed by the way in; "on Home" for an element that sits on its parent screen (IA3's as-is sitemap drew Balance and Recent activity that way, and said so in its caption); and screen identifiers A-0 to A-5, A for app, beside IA5's S-, L- and H- (IA5, Deliverable A). The type tags stay IA2's eight.

## 3 · Mobile navigation patterns, on the evidence

### 3.1 · Tab bar

A tab bar is a row of labelled destinations at the bottom of the screen, present on every screen of the app. Budiu's primer gives its case: tab bars are persistent, visible however far the person scrolls, and suit products with relatively few navigation options; past five options, "it's hard to fit them in a tab or navigation bar" (Budiu 2015). Android's design guidance gives the range as platform documentation: "The navigation bar can hold three to five navigation destinations across the same hierarchy level" (Android Developers, "Layouts and navigation patterns", page updated 22 October 2026, [developer.android.com](https://developer.android.com/design/ui/mobile/guides/layout-and-content/layout-and-nav-patterns?hl=en); platform documentation). Apple's guidance describes the component in the same terms: "A tab bar lets people navigate between top-level sections of your app" (Apple, Human Interface Guidelines, "Tab bars", undated, [developer.apple.com](https://developer.apple.com/design/human-interface-guidelines/tab-bars); platform documentation; only the page's description could be read).

Where the bar sits matters for reach. Steven Hoober recorded 1,333 observations of people using phones in public places, 780 of them touching the screen; of those, 49% held the phone in one hand, 36% cradled it and 15% used two hands ("How Do Users Really Hold Mobile Devices?", UXmatters, 18 February 2013, [uxmatters.com](https://www.uxmatters.com/mt/archives/2013/02/how-do-users-really-hold-mobile-devices.php?); a practitioner's observational study, practice). Android's guidance gives reach as the reason the bottom bar is preferred to a drawer opened from the top: the drawer "isn't as ideal as the navigation bar. This is because users must reach for the top bar on compact sizes" (Android Developers 2026).

A threshold from NN/g needs reading with care. Kara Pernice and Raluca Budiu advise that "If your site has 4 or fewer top-level navigation links, display them as visible links", and that with more than four "the only reasonable solution is to hide some of these" ("Hamburger Menus and Hidden Navigation Hurt UX Metrics", Nielsen Norman Group, 26 June 2016, [nngroup.com/articles/hamburger-menus](https://www.nngroup.com/articles/hamburger-menus/)). That advice is about the top navigation of mobile websites. Budiu's primer allows that with four or five main options it may make sense to keep them all visible all the time (Budiu 2015), and the platform range runs to five. The Perqo app keeps five tabs, every one a label IA3's checklist passed (IA3, "What IA6 keeps"); a sixth would be past every source's range.

### 3.2 · Hub and spoke

A hub-and-spoke app opens on a screen of routes, and each route leads to a task that ends back at the hub. Budiu's assessment: the hub "can work well in task-based websites and apps", especially where people do one task per visit and rarely move across the navigation tree; its cost is that it "incurs an extra step (back to the hub) for each use of the navigation" (Budiu 2015; NN/g guidance); and, on this unit's reading, a home screen that is a hub spends its space on navigation.

The Perqo app is a partial case. Most visits are assumed to be one or two tasks begun from Home or from a notification (Perqo, fictional; assumed, Deliverable A), which is the hub's condition; but two of the top tasks run in sequence across tabs (check a balance, then claim; read a notification, then the claim), which is where a hub's extra step costs. The design takes the hub's strength without its cost: Home carries routes to the top tasks (each category balance opens its category, and New claim is a labelled button), and the tab bar stays, so no task needs a return to Home first.

### 3.3 · Hierarchical drill-down

A drill-down moves from a list to an item to its detail, one level at a time, and back the same way. This unit found no NN/g study of drill-down on phones to cite; the evidence is the depth evidence IA4 set out. Deeper structures slowed people in every study IA4 reviewed (Zaphiris 2000; Larson and Czerwinski 1998; IA4, section 2.1), and Kathryn Whitenton's NN/g guidance is that "All other things being equal, deep hierarchies are more difficult to use" ("Flat vs. Deep Website Hierarchies", NN/g, 10 November 2013; IA4, section 2.1). For disclosure inside a task, Nielsen's limit is explicit: "In practice, designs that go beyond 2 disclosure levels typically have low usability" (Nielsen 2006). None of these studies measured scrolling on a phone, the cost breadth pays there; IA4 left that gap unsourced, and so does this unit.

The Perqo app uses drill-down inside a tab only, and at most two levels below the tab: Claims, then a claim; Card, then Purchases, then a purchase (Deliverable B). New claim, Check and submit and Claim submitted are three screens under Claims, and they are a staged sequence the person moves through once, which Nielsen separates from disclosure levels (Nielsen 2006).

### 3.4 · The hamburger menu, on the evidence

A hamburger menu hides the destinations behind an icon, usually three lines, that opens a list. Budiu credits it with holding "a fairly large number of navigation options" and names its cost: "it is less discoverable"; it "is best suited for content-heavy, browse-mostly sites and apps", supported by navigation in other ways (Budiu 2015). Pernice and Budiu measured the cost. In a study of 179 participants on six live sites, people used hidden navigation in 27% of the cases on desktop, against 48% for visible navigation and 50% for combined navigation (some links visible, the rest hidden); on mobile, hidden navigation was used in 57% of the cases and combined navigation in 86% (visible-only navigation was not tested on mobile). Discoverability of content fell by more than a fifth with hidden navigation; tasks took at least 39% longer on desktop with it, and 15% longer on mobile than with combined navigation; and people rated hidden navigation harder, 2.6 against 2.3 for combined and 2.1 for visible, on a scale from 1, easy, to 7, difficult (Pernice and Budiu 2016). The study was of websites; on this unit's reading, an app with a small set of destinations is the case their recommendation points to, with the destinations kept visible.

The icon itself fails IA3's A4 when it carries no text, since few icons are recognised without a label (Harley, "Icon Usability", NN/g, 2014; IA3, section 1.2). The Perqo app has no hamburger menu.

### 3.5 · Choosing Perqo's pattern by IA3's criteria

IA3 handed this unit its criteria for choosing navigation: A1 to A5 (scent), B1 and B2 (mental models), F1 and F2 (findability) (IA3, "What this hands on"). Four of them decide between patterns; the rest are properties of the labels and hold, or fail, whatever the pattern. A1 (labels name what is behind them), A2 (first words tell labels apart), A3 (the destination confirms the label) and A5 (one label, one destination) are tested on the labels in Deliverable B. B2 (a thing findable in every state) is a property of how the Claims list groups claims (IA3, B2), which any pattern can carry. The four that separate the patterns, with the two facts about each pattern they are judged on:

- **Where the destinations are, and the evidence on use**: on every screen for a tab bar (Budiu 2015); on the hub for a hub, with an extra step per use (Budiu 2015); one level at a time for a drill-down, where depth slows people (section 3.3); behind an icon for a hamburger menu, used in 57% of cases on mobile against 86% for combined navigation (Pernice and Budiu 2016). Visible links alone were not tested on mobile (section 3.4).
- **A4, text with every icon**: a tab bar's icons carry their labels under them; a hub's routes and a drill-down's rows are labelled; the hamburger's trigger is an icon that often has no text (Harley 2014).
- **B1, the units the system acts on shown where the decision is made**: the four category balances must be on the first screen and on New claim (IA3, B1). A tab bar's Home can show the four balances, and so can a hub; a drill-down shows them only on the level they sit on; a hidden menu hides them until it is opened.
- **F1, every choice unambiguous at every level**: a tab bar is one level of tabs and a hub one level of routes; a drill-down adds one more choice per level, each of which must carry scent (Larson and Czerwinski 1998; IA3, section 6.2); a menu is one list, if it is labelled.
- **F2, everything needed reachable from where the person is**: yes for a tab bar, since the tabs persist; only from the hub for a hub; only by going back for a drill-down; only after opening the menu for a hamburger, and Pernice and Budiu measured how often people do not open it.
- **Room for the destinations**: three to five for a bar (Android Developers 2026; Budiu 2015); as many as the hub holds; any number for a drill-down, at the cost of levels; a fairly large number for a menu (Budiu 2015).

Figure 1 names its rows in short: Destinations: where and Destinations: room for the first and last of these, Evidence on use, and each criterion by its ID and a gloss (A4 · icon text, B1 · units in view, F1 · unambiguous, F2 · reachable); its last row, In the Perqo app, is the decision below. Tone 6 marks a fault against one of the four criteria, or the measured cost behind it.

```viz
{"kind": "matrix", "caption": "Navigation-pattern comparison: four mobile navigation patterns against the evidence and the IA3 criteria that separate them, for the Perqo app; supports the decision on the app's global navigation (section 3.5). Tab bar, hub and hamburger from Budiu, 'Basic Patterns for Mobile Navigation: A Primer', NN/g, 2015; use figures from Pernice and Budiu, 'Hamburger Menus and Hidden Navigation Hurt UX Metrics', NN/g, 2016 (179 participants, websites); three to five destinations from Android Developers, 'Layouts and navigation patterns', 2026 (platform documentation); depth from Larson and Czerwinski, 1998, and Zaphiris, 2000 (through IA4, section 2.1), and Nielsen, 'Progressive Disclosure', NN/g, 2006; criteria A4, B1, F1, F2 from IA3, Deliverable; the Perqo row from the decision under the figure and section 3.3; the hamburger's unlabelled icon from Harley, 'Icon Usability', NN/g, 2014. Rows tone 3, the app; tone 6 marks a fault against an IA3 criterion, or the measured cost behind one. Perqo is fictional.", "cols": ["Tab bar", "Hub and spoke", "Drill-down", "Hamburger menu"], "rows": [
 {"label": "Destinations: where", "tone": 3, "cells": ["on every screen", "on the hub", "one level at a time", "behind an icon"]},
 {"label": "Destinations: room", "tone": 3, "cells": ["three to five", "as many as the hub holds", "any, at the cost of levels", "a fairly large number"]},
 {"label": "Evidence on use", "tone": 3, "cells": ["visible links: not tested on mobile", "an extra step per use", {"mark": "depth slows people", "tone": 6}, {"mark": "used in 57% of cases on mobile, against 86% for combined", "tone": 6}]},
 {"label": "A4 · icon text", "tone": 3, "cells": ["labels under icons", "labelled routes", "labelled rows", {"mark": "the icon often has no text", "tone": 6}]},
 {"label": "B1 · units in view", "tone": 3, "cells": ["Home can show the four balances", "the hub can show them", {"mark": "only on the level they sit on", "tone": 6}, {"mark": "hidden until opened", "tone": 6}]},
 {"label": "F1 · unambiguous", "tone": 3, "cells": ["one level of tabs", "one level of routes", {"mark": "one more choice per level", "tone": 6}, "one list, if labelled"]},
 {"label": "F2 · reachable", "tone": 3, "cells": ["yes: the tabs persist", {"mark": "only from the hub", "tone": 6}, {"mark": "only by going back", "tone": 6}, {"mark": "only after opening the menu", "tone": 6}]},
 {"label": "In the Perqo app", "tone": 3, "cells": ["the five tabs", "Home's routes to the top tasks", "inside a tab, two levels at most", "not used"]}],
 "legend": [{"mark": "tone 3", "means": "the Perqo app", "tone": 3}, {"mark": "tone 6", "means": "a fault against an IA3 criterion, or the measured cost behind one", "tone": 6}]}
```

The decision (Perqo, fictional): a tab bar of IA3's five tabs as the global routes; Home as a partial hub, with routes to the top tasks; drill-down inside a tab, no deeper than two levels; no hidden menu.

## 4 · Progressive disclosure, empty states, error states and permissions as IA decisions

Each of these four looks like a screen-level detail, and each decides what exists where, under what condition, and by which route the person goes on: the questions an app map answers. The per-screen record is Deliverable B, B.5.

### 4.1 · Progressive disclosure

Nielsen sets two requirements: "You must get the right split between initial and secondary features", the initial display holding what people frequently need; and "It must be obvious how users progress from the primary to the secondary disclosure levels", with a control that sets clear expectations of what lies behind it (Nielsen 2006; NN/g guidance). The first is an IA decision about which attributes of an object sit where; it is the ranking IA4 left to this unit (IA4, section 4.1 figure note; Deliverable A, A.2). The second is a labelling decision, judged by IA3's A1.

At Perqo (Perqo, fictional), the allocation carries category, period, amount, spent and remaining (IA4, Deliverable A, O-06). Home shows two of them for each open category, the category and what remains, because the decision the employee makes from Home is whether a purchase or a claim fits (IA3, B1). The category screen shows the other three, and What's covered. Home drops the one total of the as-is: it is a sum the system never checks a claim against (IA3, section 2.3), and showing it beside the four balances keeps the one-pot model alive.

### 4.2 · Empty states

An empty state is a screen with nothing to show yet: no claims, no purchases, no categories open. NN/g has an article on empty states in applications; it could not be read for this unit, and nothing is cited from it. The rule below is this unit's synthesis from IA3's evidence. A screen reached by a label must confirm the label on arrival (IA3, A3; Budiu 2020); an empty list that shows nothing confirms nothing, and the person cannot tell an empty list from a broken one. So each empty state says three things: what will appear here, why it is empty now, and the route to the next step (IA3, F2). Two rules from IA4 decide where an empty state should not appear at all. A filter value with no items is hidden, so no option leads to an empty result (IA4, Deliverable B, R5; Hearst 2006); and a route whose destination would be empty for everyone in the person's position is withheld, by the same reasoning.

At Perqo (Perqo, fictional): Claims with no claims says that claims will appear here once submitted, links to "How to claim back a receipt" (H-2.1.1) and offers New claim; Home in a group with no category open says that the employer's HR team chooses which categories are open, and links to Help; the route "Card offers in Meals" appears on the Meals screen only when Meals has an offer (R5).

### 4.3 · Error states

Tim Neusesser and Evan Sunwall's NN/g guidelines put an error message near the error's source, say what went wrong without blame, and go further: "Merely stating the problem is also not enough; offer some potential remedies"; and "Let users correct errors by editing their original action instead of starting over" ("Error-Message Guidelines", Nielsen Norman Group, 14 May 2023, [nngroup.com/articles/error-message-guidelines](https://www.nngroup.com/articles/error-message-guidelines/); NN/g guidance). Each of those is an IA decision once it is applied to a flow: where the message sits (on which screen, by which field), which route the remedy offers, and what state the person's input is kept in.

At Perqo (Perqo, fictional) three error states matter, and the IA decision in each is the route out:

- **A claim over the category's balance.** The rule rejects a claim whose amount is over the chosen category's balance (IA2, section 5.3; IA3, section 2.3). Letting the employee submit it, only to see Rejected, turns a rule the app knows in advance into a surprise. Check and submit therefore shows the state "More than your Learning balance", with Edit as the only route forward, and the form keeps what was entered.
- **No connection.** Home shows the last balances it loaded, with the time they were loaded, and Claims and Purchases show their last lists the same way. A blank screen would fail A3; a stale balance shown without its time would mislead.
- **A missing or unreadable receipt.** The message sits by the Receipt field on New claim, and the amount and category stay as entered.

### 4.4 · Permissions

An app meets two kinds of permission, and both are IA decisions about what exists for whom.

**Platform permissions.** The operating system asks the person before an app may use the camera or, where the platform requires it, send notifications. Android's documentation, as platform guidance: "Ask for a permission in context, when the user starts to interact with the feature that requires it"; "Don't block the user"; and "If the user denies or revokes a permission that a feature needs, gracefully degrade your app so that the user can continue using your app, possibly by disabling the feature that requires the permission" (Android Developers, "Request runtime permissions", page updated 28 October 2026, [developer.android.com, runtime permissions](https://developer.android.com/training/permissions/requesting); platform documentation). At Perqo (Perqo, fictional): the camera is asked for when the employee taps Take a photo on New claim, and if it is refused, Choose a file stays; notifications are asked for once, after the first claim is submitted, the moment an employee has a reason to want them, and the prompt says what they are for (get told when a claim is approved, rejected or paid), with Allow and Not now as its two answers. Refusing notifications loses nothing that cannot be found: every claim's state shows in Claims and every message in Notifications.

**Business permissions**, set in Perqo Admin and carried to the app as what exists. IA1 put it as policies reaching the app "as open categories and approval rules" (IA1, Deliverable). The IA choice for each is between hiding the thing, showing it disabled, and showing it with an explanation, and the deciding question is whether the person can act on the explanation. At Perqo (Perqo, fictional):

- A category closed to the employee's group is not shown (IA2, section 5.3: only the open categories appear), and so neither is a cross-listing whose home category is closed, nor an offer for an item in a closed category: the employee could not spend from it.
- The policy's auto-approve limit is shown as a rule where the claim is made, "Claims over the limit need HR approval", with the limit read from the group's policy (IA3, C4), because the employee can act on it: a claim over the limit will wait for HR, and the employee knows that before submitting.
- An employee with no card yet (IA4, R-11 allows 0..1) sees the Card tab in the state "Your Perqo card has not been issued yet", with claims still open to them; hiding the tab would change the global routes from one employee to the next.
- A Frozen card shows its state and Unfreeze card on the Card screen (IA4, A.3).

## 5 · From user flow to wireflow

IA2 separated three artefacts by scope (IA2, section 1.6). A **user flow** follows one kind of user from an entry point to a goal, with the branches that kind of user can meet; Kate Kaplan's NN/g definition calls it "A set of interactions that describe the typical or ideal set of steps needed to accomplish a common task" ("User Journeys vs. User Flows", NN/g, 16 April 2023; IA2, section 1.6). A **task flow** follows one task along its main path. A **wireflow** draws a task flow as the screens themselves; Laubheimer calls it "a design-specification format that combines wireframe-style page layout designs" with "a simplified flowchart-like way of representing interactions", suited to apps and dynamic sites that "have few overall pages, but change the content and layout dynamically"; he keeps the flowchart for "complex workflows and interactions with multiple steps or paths", which lacks page context (Laubheimer 2016; NN/g guidance).

When each is the right artefact, by the question asked (IA2, Deliverable, decision table):

| Question | Artefact | Why that one |
|---|---|---|
| Which steps and branches does this task have, before any screen exists? | user flow, as a flow | it is cheap to argue about; the branches are the content (IA2, section 3, fault 4) |
| What is the main path of one task? | task flow | discovery; no screens needed yet |
| Which screens does the task need, and what changes on them? | wireflow | the change on the screen is the point (Laubheimer 2016) |
| Which outcome does the system produce from these facts? | decision tree | the rule belongs in its own artefact (IA2, section 1.7) |

A user flow becomes a wireflow in five moves, each this course's practice drawn from the sources above:

1. **Each step that happens on a screen becomes a screen**; a step outside the app (paying at a till, waiting for HR) becomes a screen of the other surface in its tone, or a note.
2. **Each branch becomes either a second screen or a state of the same screen.** A branch that changes what the person can do next is a state, written in square brackets in the title ("Check and submit [over the balance]"); Laubheimer's point that the next step may be the same page with an error or a confirmation is the warrant (Laubheimer 2016).
3. **Each arrow is labelled with the control that triggers it**, in the person's action ("tap Continue"), because "the arrows clearly indicate the clickable 'hotspots' (or targets) that lead to the next step" (Laubheimer 2016); the label must match a button on the screen it leaves, which tests A5 and A1 on the drawing itself.
4. **Each screen shows only what the decision on it needs**, as placeholders; a wireflow is not a visual design (IA2, section 5.2).
5. **The failure paths stay.** Kaplan's "typical or ideal" path is the user flow's default and the reason IA2 named missing unhappy paths as a fault (IA2, section 3, fault 4).

The claim task, first as a user flow, in the order of the hierarchical task analysis in section 1.4 (Perqo, fictional). The employee pays and keeps the receipt, outside the app; opens New claim from Claims, Home or a category screen; enters category, amount and receipt, choosing a file if the camera is refused; reaches Check and submit, where an amount over the category's balance sends them back to edit it; submits, with no way back. Perqo then checks the claim: at or under the limit it is approved automatically, over the limit HR decides in Approvals (IA2, section 5.3). The employee sees the outcome in Claims: Approved, then Paid, or Rejected, with the reason to read. The flow kind draws no branches, so each branch is a bracketed condition in its step's note, as IA3 drew its loop (IA3, section 1.1); the system's step is tone 5, the employee's tone 3.

```viz
{"kind": "flow", "per_row": 2, "caption": "User flow: an employee submits a claim in the Perqo app, F2, branches as bracketed conditions in the notes because the flow kind draws no branches; supports the decision on which screens and states the claim wireflow needs (section 5). Steps from section 1.4's task analysis; the rule from IA2, section 5.3 and IA3, section 2.3; user flow as defined by Kaplan, 'User Journeys vs. User Flows', NN/g, 2023. Tone 3 the employee and the app, tone 5 the Perqo system. Perqo is fictional.", "steps": [
 {"label": "Pay and keep the receipt", "note": "outside the app", "tone": 3},
 {"label": "Open New claim", "note": "from Claims, Home or a category screen", "tone": 3},
 {"label": "Enter category, amount and receipt", "note": "[camera refused] choose a file", "tone": 3},
 {"label": "Check and submit", "note": "[over the category's balance] edit the amount", "tone": 3},
 {"label": "Submit", "note": "(no way back)", "tone": 3},
 {"label": "Perqo checks the claim", "note": "[at or under the limit] approved automatically; [over the limit] HR decides in Approvals", "tone": 5},
 {"label": "See the outcome in Claims", "note": "[Approved] then Paid; [Rejected] read why", "tone": 3}]}
```

Deliverable C draws the same task as a wireflow (C.3), and the comparison shows what the step adds: the over-balance branch becomes a state of Check and submit, the camera branch becomes two buttons on New claim, and the outcome becomes two states of one Claim screen reached from a notification.

## 6 · Keeping the app consistent with the website and the backoffice

### 6.1 · Why, and which kind of consistency

Andrea Resmini and Luca Rosati give consistency a chapter of its own among five heuristics for information architecture across channels, beside place-making, resilience, reduction and correlation (*Pervasive Information Architecture: Designing Cross-Channel User Experiences*, Morgan Kaufmann, 2011, chs 3 to 8, ch. 5 "Consistency"; chapter titles from the publisher's contents, [shop.elsevier.com](https://shop.elsevier.com/books/pervasive-information-architecture/resmini/978-0-12-382094-5); the chapter's text was not read for this unit). NN/g separates internal consistency, "within a product or a family of products", from external consistency with conventions (Krause, NN/g, 2021; IA3, section 4.3), and WCAG requires that components with the same function within a set of pages are identified consistently (SC 3.2.4; IA3, section 4.3). Perqo's three surfaces are a family of products in Krause's sense, and the employee meets two of them: the app and the Help centre on perqo.com.

The rule IA1 set is the one that makes consistency possible across surfaces that use different words: one thing may carry a different label on each surface only when the mapping is written down (IA1, section 2.4). The object map is where it is written (IA4, Deliverable A). So the app's consistency has three tests: each app screen shows an object the map holds, under that object's app label; each Help centre route from the app uses the Help centre's own title for its destination; and no app label is a variant term the vocabulary maps away.

### 6.2 · The app's labels against the map and the website

Every label below is the app's (Perqo, fictional). The objects and their surface labels are IA4's; the Help centre topics and articles are IA5's.

| App label | Object (IA4) | Perqo Admin | perqo.com | Help centre route from the app |
|---|---|---|---|---|
| Balance (per category, on Home and each category screen) | allocation, O-06 | Budget | Benefits budget | Your balance explained, H-2.2.1; Why can't I use money from another category?, H-2.2.2 |
| Health, Learning, Mobility, Meals | F-CAT values CAT-HEA, CAT-LEA, CAT-MOB, CAT-MEA (a taxonomy term, not an object: IA4, section 4.3) | the same | Benefits, S-1.4.1 to S-1.4.4 | What you can claim in each category, H-2.1.3 |
| What's covered | catalogue item, O-13 | Covered items | the Benefits pages | H-2.1.3 |
| Claim; New claim; Submitted, Approved, Rejected, Paid | transaction, type claim, O-07 | Claim; the same states | Claims | Help with claims (H-2.1); Why was my claim rejected?, H-2.1.2 |
| Claims over the limit need HR approval | policy, O-04 (auto-approve limit) | Policy | Policies | How approval rules work, H-1.2.5 (listed under both audiences) |
| Purchase; Purchases | transaction, type card payment, O-08 | Card payment | Card payments | Where you can pay with the Perqo card, H-2.3.2 |
| Card; Card details; Freeze card | card, O-09 | Perqo card, status only (IA7) | Perqo card | Freezing and unfreezing your card, H-2.3.1 |
| Card offers | offer, O-12 | not shown | not shown | none |
| Notifications | notification, O-10 | not shown (IA7) | not shown | none |
| Profile | employee, O-05 | Employees | not shown | none |
| Help | help article, O-14 | not shown | Help centre | For employees, H-2 |

Words the app does not use, each with its reason: "allowance" and "credit" (variants of Balance: IA2, section 5.3; IA5, section 1.3), "refund", "reimbursement" and "expense" (variants of Claim), "Budget" (Admin's label), "Approvals" (Admin's area, and the Help centre's Approvals topic, H-1.3, sits under For HR and finance teams; the employee meets the rule, through H-1.2.5, which IA5 listed under both audiences), "Pending" (a second word for Submitted: IA3, D2), "Perks" and "Discover" (IA3, C1 and D1), "Documents" (IA3, A1 and C4). IA5's note in its labels table that the app's Benefits tab holds the same four categories as perqo.com's Benefits section once Perks is removed holds (IA5, Deliverable B, B.2).

### 6.3 · Addresses and deep links

IA4 set Perqo's addressing rules: catalogue pages and filters address values by stable identifier, and a renamed or moved Help centre page keeps a redirect from its old address (IA4, section 5; Berners-Lee, "Cool URIs Don't Change", W3C, 1998). IA5 applied them to perqo.com, with category pages addressed by identifier then preferred term, /product/benefits/cat-hea/health (IA5, section 5.1). An app's screens need addresses too, so that a notification, an invitation or a Help centre article can open a screen directly. Both platforms document links on the company's own web domain that open the matching content in the app: with Android's App Links verified, "deep links to your website can immediately open corresponding content in your app" (Android Developers, "About deep links", 2026); Apple's universal links "link directly to content within your app" (Apple Developer Documentation, "Allowing apps and websites to link to your content", undated, [developer.apple.com](https://developer.apple.com/documentation/xcode/allowing-apps-and-websites-to-link-to-your-content); platform documentation).

The rule this unit sets (Perqo, fictional): every app screen has an address under perqo.com/app/, in IA5's form (identifier first, then the preferred term where a term is part of the address); with the app installed the address opens the screen; without it, the address serves Get the Perqo app (S-6, perqo.com/app), so the fallback for every app link is the page that gets the employee the app (IA5, section 5.5). Claim and purchase addresses carry the item's identifier; the Card offers filter carries the category's identifier, never its label (IA4, section 5). The addresses are in Deliverable B, B.4.

## Deliverable · A · The Perqo app task inventory

*Face of this artefact (IA2, the notation sheet): task inventory of the Perqo app, with the tasks of other actors that the app depends on, at fidelity F2; decision: what the app's first screen, tabs and routes are ordered by; readers: product management (priority), design (placement), engineering (which screen each task starts on), support (where an employee can be stuck); leaves out: measured frequencies (every frequency is assumed), Admin's own tasks beyond those the app shows, the merchant side's surface; owner: the IA designer; version 1, dated 3 November 2026; Perqo is fictional.*

### A.1 · The tasks

Frequencies are per employee and assumed (Perqo, fictional), within IA3's assumption that the app is opened a few times a month (IA3, section 6.2): several tasks often share one visit, and paying with the card does not open the app at all. Priority is frequency raised by money at stake (section 1.1): P1 tasks start on Home or one tap from it; P2 tasks are one tab and one tap away; P3 tasks may sit two levels down. Screen IDs are Deliverable B's.

| ID | Task (the employee's words) | Object and call to action (IA4) | Actor | Surface | Frequency (assumed) | Comes after | Money at stake | Priority | Starts on |
|---|---|---|---|---|---|---|---|---|---|
| T-01 | Pay with my card | card payment (R-12, R-14) | employee | the card at a merchant's till; the app before and after | 8 a month | T-02 or T-07 | yes | P1 | A-2.1 to A-2.4 before; A-4.2.1 after |
| T-02 | See my balance per category | allocation -> see balance | employee | app | 3 a month | opening the app | yes, indirectly | P1 | A-1 |
| T-03 | Read a notification | notification -> open | employee | app | 2 a month | T-06, T-14 | no | P2 | entry: a notification; A-5.2 |
| T-04 | Check a purchase | card payment -> view | employee | app | 1.5 a month | T-01 | yes: a wrong charge | P2 | A-4.2 |
| T-05 | Track a claim | claim -> view *new* | employee | app | 1.5 a month | T-06 | yes | P1 | A-3; entry: a notification |
| T-06 | Submit a claim | claim -> submit | employee | app | 1 a month | paying another way and keeping the receipt; T-02 | yes | P1 | A-1, A-3, A-2.1 to A-2.4 |
| T-07 | Find what's covered | catalogue item -> view *new* | employee | app | 0.5 a month | before T-01 or T-06 | yes, indirectly | P2 | A-2 |
| T-08 | Find card offers | offer -> view | employee | app | 0.5 a month | before T-01 | no | P3 | A-4.3; A-2.1 to A-2.4 |
| T-09 | Read a help article | help article -> read | employee | perqo.com Help centre, from the app | 0.3 a month | T-02, T-05, T-06 | no | P3 | the external routes in Deliverable B |
| T-10 | Freeze or unfreeze my card | card -> freeze; -> unfreeze | employee | app | 0.1 a month | a lost or found card | yes: a lost card | P2 | A-4.4 |
| T-11 | See my profile | employee -> view profile | employee | app | 0.1 a month | none | no | P3 | A-5.1 |
| T-12 | Join from HR's invitation | employee -> invite (HR); joined in the app | employee | email, then the app or S-6 | once | T-17 | no | P1: nothing else works without it | A-0.1 |
| T-13 | Set allocations for a group | allocation -> set for a group | finance manager | Admin, Budgets | each period | none | yes | outside the app | shows as Balance on A-1 and A-2.1 to A-2.4 |
| T-14 | Approve or reject a claim over the limit | claim -> approve; -> reject | HR manager | Admin, Approvals | per claim over the limit | T-06 | yes | outside the app | shows as Approved or Rejected on A-3 and A-3.4 |
| T-15 | Take a card payment | merchant takes card payment (R-14) | merchant | the till | per payment | T-01 | yes | outside the app | shows as a Purchase on A-4.2.1 |
| T-16 | Pay out an approved claim | the lifecycle's "pay out" (IA2, section 5.3) | Perqo system | none | per approved claim | approval by rule or by T-14 | yes | outside the app | shows as Paid on A-3 |
| T-17 | Invite an employee | employee -> invite | HR manager | Admin, Employees | per new employee | none | no | outside the app | starts T-12 |

Two calls to action are new here, both by the employee: claim -> view (tracking a claim, for which IA4's table gave the employee only submit, and HR approve and reject) and catalogue item -> view (What's covered, which IA4 placed on the category screen without an employee action). Both extend IA4's A.3 and rename nothing (IA4, "What IA7 may do with it").

The employee's tasks ranked by assumed frequency:

```viz
{"kind": "compare", "caption": "Task inventory, ranked: the Perqo employee's tasks by assumed frequency per employee per month, F2; supports the decision on what sits on Home and in the tab bar (Deliverable A, A.1). Every frequency is assumed, within IA3's assumption that the app is opened a few times a month (IA3, section 6.2), and is replaced by measured use in IA11; placement by frequency from Sears and Shneiderman, ACM TOCHI 1(1), 1994, and Nielsen, 'Progressive Disclosure', NN/g, 2006. Every bar is tone 3, the employee and the app; paying with the card happens at a merchant's till and does not open the app. Perqo is fictional.", "unit": "a month", "max": 10, "rows": [
 {"label": "Pay with my card", "value": 8, "tone": 3},
 {"label": "See my balance per category", "value": 3, "tone": 3},
 {"label": "Read a notification", "value": 2, "tone": 3},
 {"label": "Check a purchase", "value": 1.5, "tone": 3},
 {"label": "Track a claim", "value": 1.5, "tone": 3},
 {"label": "Submit a claim", "value": 1, "tone": 3},
 {"label": "Find what's covered", "value": 0.5, "tone": 3},
 {"label": "Find card offers", "value": 0.5, "tone": 3},
 {"label": "Read a help article", "value": 0.3, "tone": 3},
 {"label": "Freeze or unfreeze my card", "value": 0.1, "tone": 3},
 {"label": "See my profile", "value": 0.1, "tone": 3},
 {"label": "Join from HR's invitation", "value": 0, "display": "once", "tone": 3}]}
```

What the ranking decides (Perqo, fictional): Home carries the four balances (T-02) and New claim (T-06); a notification opens its claim directly (T-03, T-05); Purchases sits one tap into Card (T-04); Freeze card stays one tap into Card although it is rare, because a lost card costs money (T-10); Card offers and Profile sit one level down (T-08, T-11).

### A.2 · The app's calls to action, ranked

IA4 left the complexity and priority of each call to action to this unit, and the ranking of attributes to interaction design (IA4, Deliverable A, A.3; section 4.1 figure). The columns follow Prater's CTA inventory (Prater, "OOUX: A Foundation for Interaction Design", A List Apart, 19 April 2016; IA4, section 4.1). Complexity is this unit's three grades: low, one tap and no rule read; medium, one screen of input, one rule read or a confirmation step; high, several screens, a rule and a step with no way back. The attribute order is the order on the screen where the call to action lives, first to last; attributes not listed stay one level down (section 4.1).

| Object | Call to action | Who | Where | Complexity | Priority | Attributes, in screen order | Open question (for) |
|---|---|---|---|---|---|---|---|
| allocation | -> see balance | employee | A-1; A-2.1 to A-2.4 | low | P1 | Home: category, remaining. Category screen: remaining, spent, amount, period | do employees read four balances as four pots? (IA11) |
| transaction, type claim | -> submit | employee | A-3.1 to A-3.3 | high | P1 | New claim: category, the category's balance, amount, receipt, the rule. Check and submit: category, amount, balance after | is the rule line understood before submitting? (IA11) |
| transaction, type claim | -> view *new* | employee | A-3; A-3.4 | low | P1 | Claims list: status (the group), amount, category, date submitted. Claim: status, amount, category, date submitted, receipt, the reason when Rejected | is a rejected claim found in Claims? (IA11) |
| transaction, type card payment | -> view | employee | A-4.2; A-4.2.1 | low | P2 | merchant, amount, date, category; on the purchase, the category's balance after | decided: as a notification (IA8, section 4.5, 9 Nov 2026) |
| card | -> view card details | employee | A-4.1 | low | P3 | last four digits, status | none |
| card | -> freeze; -> unfreeze | employee | A-4.4 | medium (a modal to confirm) | P2 | status, then the action | none |
| offer | -> view | employee | A-4.3 | low | P3 | title, discount, merchant, valid until | are offers found under Card and from the categories? (IA11) |
| notification | -> open | employee | A-5.2; entry: a notification | low | P2 | message, date; opens the claim it is about (or, since IA8, section 4.5, 9 Nov 2026, the screen a declined payment needs) | where do employees look for past messages? (IA11) |
| catalogue item | -> view *new* | employee | A-2.1 to A-2.4 | low | P2 | narrower term, then its items by name; cross-listings last, each naming its home category | are the far members found? (IA11) |
| employee | -> view profile | employee | A-5.1 | low | P3 | name, work email | none |

## Deliverable · B · The Perqo app map

*Face of this artefact (IA2, the notation sheet): app map of the Perqo app, the to-be for IA3's as-is navigation, at fidelity F2 with F3's identifiers on every screen; decision: what screens the app has, under which tab, in which states, with which modals, and by which ways in; readers: design and engineering (screens, states, addresses), product management (scope), content (labels and empty-state text), support (where an employee lands); leaves out: visual design, the flows (Deliverable C), the claim's lifecycle (IA2, section 5.3; IA8), Perqo Admin and perqo.com beyond the routes into them, the sign-in method; owner: the IA designer; version 1, dated 3 November 2026; amended 9 November 2026 (DL-004, DL-008; IA9, section 4.5); every placement marked assumed is untested; Perqo is fictional.*

**Fidelity and departure.** IA2's decision table gives a sitemap F2 in design and F3 for build (IA2, Deliverable). This map is F2 and carries one F3 element, an identifier on every screen, because IA8 will join the map to Admin and the lifecycles by screen, and deep links need addresses (section 6.3). IA4 departed from IA2 the same way for the taxonomy (IA4, Deliverable B).

### B.1 · The proposals IA3 left for this unit, decided

Each proposal in the register's "Proposed for IA6, not facts yet" (from IA3's Deliverable), with the decision. Every one is taken, and each becomes a fact (Perqo, fictional).

| Proposal (IA3) | Decision | How it is applied |
|---|---|---|
| Rename the offers list "Card offers" and give it one placing | taken | one screen, Card offers (A-4.3), under Card; each category screen has a route to it, filtered to that category, shown only when the category has offers (B.6 explains why this is one placing) |
| Show the four category balances on Home | taken | Home's Balance shows each open category with what remains; the one total is dropped (section 4.1) |
| Group Claims by all four states | taken | Submitted, Approved, Rejected, Paid, newest first in each (IA4, section 1.2) |
| Label the "+" "New claim" | taken | a button with the text New claim on Home, on Claims and on each category screen, all opening A-3.1 |
| "Your balance explained" for the balance link | taken | the link opens H-2.2.1 at its new address, /help/employees/balance/your-balance-explained (IA5, Deliverable A) |
| Help opens For employees | taken | Account's Help opens H-2, perqo.com/help/employees |
| The rule "Claims over the limit need HR approval" on New claim, the limit read from the group's policy | taken | on New claim, with a link to How approval rules work, H-1.2.5 |
| Documents removed | taken | Account holds Profile, Notifications and Help |

### B.2 · IA3's fixes, applied

Every row of IA3's verdicts table, with its fix and where the app map makes it (IA3, Deliverable, "The checklist applied to the as-is Perqo app").

| IA3 item | Fix (for IA6), as IA3 wrote it | Made in the app map |
|---|---|---|
| A1 | rename the balance link "Your balance explained"; rename the offers list "Card offers"; remove Documents | Home's link (A-1); Card offers (A-4.3); Account has no Documents (A-5) |
| A2 | "Your balance explained" starts with the subject; the other labels need no change | every passed label kept (below) |
| A3 | the renamed link matches its page; Help opens For employees directly | Your balance explained → H-2.2.1; Help → H-2; each external route carries its destination's title |
| A4 | label the "+" "New claim" | New claim, a text button (A-1) |
| A5 | each link carries its own destination's name | no two routes with the same text open different screens; New claim opens A-3.1 from every screen that carries it |
| B1 | the four category balances on Home; the chosen category's balance on New claim and on Check and submit | A-1; A-3.1; A-3.2 |
| B2 | group Claims by all four states | A-3; the Claim screen (A-3.4) shows the reason when Rejected |
| C1 | remove Perks; Benefits holds the four categories only | A-2 |
| C2 | under each narrower term, the policy's examples in basic-level words | A-2.1 to A-2.4 carry the catalogue items (IA4, Deliverable B, B.3) as the example client's policy covers them |
| C3 | far members listed in both places with the covered category named; the second places tested | yoga class in Learning, cookery course in Meals, bike helmet in Health, each "covered under" its home, marked assumed (IA4, R6) |
| C4 | one placing for offers, recorded as a business request; the rule in the employee's terms where the claim is made | Card offers, one screen (A-4.3), the partnerships team's request recorded in B.6; the rule on A-3.1 |
| D1 | remove Documents and Perks; "Card offers" names what the list holds | A-5; A-2; A-4.3 |
| D2 | Submitted everywhere; one label for offers in one place | Recent activity on Home says Submitted; Card offers only |
| D3 | IA2's variant terms to the Help centre search as synonyms | outside the app: the Help centre's search results page (H-0.1), set by IA5; the app has no search |
| E1 | no search in the app for now | none added |
| E2 | support reads the For employees log each quarter | outside the app (IA5; IA12) |
| E3 | keep | Claims, Purchases and Notifications keep their past items |
| F1 | fixed by A1, A4 and C1; the tabs stay | the five tabs; Home's elements each name their destination |
| F2 | fixed by C4 and B2 | the rule on A-3.1; rejected claims in A-3 |

Every label IA3 passed is kept: the five tabs Home, Benefits, Claims, Card and Account; Balance; Health, Learning, Mobility and Meals and their narrower terms; New claim; Check and submit; Help with claims; Card details, Purchases and Freeze card; Profile, Notifications and Help; Submitted and Paid, joined by Approved and Rejected; and Recent activity, which passed A2 (IA3, "What IA6 keeps"; A2's verdict). The labels this unit adds are Your balance explained and Card offers (both IA3's), Join, Sign in, Claim submitted (IA2's), Claim, Purchase, Take a photo, Choose a file, Unfreeze card (IA4's call to action), and the titles of the Help centre articles the app links to (IA5's).

### B.3 · The map

The map in the notation (Perqo, fictional): square-cornered boxes with IA2's type tags, every box tone 3, the app. The root is the surface, since the tab bar is not a screen; its children are Join and sign in (A-0), which holds the two sign-in screens, and the five tabs. Notes carry the screen identifier, any [condition], "modal" for a layer, "entry:" for a way in, and "on Home" for elements that sit on Home. Every route that leaves the app from a screen's default state is tagged `external` with a "→ see" note to its Help centre page; the routes that appear only in a state are in B.5, except the Rejected claim's link Why was my claim rejected? (H-2.1.2), given with A-3.4 below. The category screens carry the example client's covered items, which this unit extends from IA3's six to IA4's twelve (Perqo, fictional): the example client's policy covers every item in the catalogue's sample, BI-001 to BI-012: under Health, gym membership, yoga class and swimming pool entry (Fitness) and therapy session (Therapy); under Learning, coding course and cookery course (Courses) and book (Books); under Mobility, train pass (Public transport) and bike helmet and bike repair (Bike); under Meals, restaurant meal (Restaurants) and groceries (Groceries) (IA4, Deliverable B, B.3).

```viz
{"kind": "sitemap", "stack_from": 2, "caption": "App map: the Perqo app as designed (to-be), F2 with an identifier on every screen, page types tagged; supports the decision on which screens exist, under which tab, in which states, with which modals and ways in (Deliverable B). Every box is tone 3, the app. Notes carry the screen ID (A-), a [condition] for a state (IA2's conditional area), 'modal' for a layer over the screen, 'entry:' for a way in and 'on Home' for an element that sits on Home, words added in section 2 under IA2's rule 'Keep the notation; extend the legend' (IA2, section 4). Routes that leave the app from a screen's default state are tagged external with '→ see' their Help centre page; '→ see' with a screen ID points to a screen drawn elsewhere on the map. Check and submit and Claim submitted follow New claim in a staged sequence; all three are screens under Claims (section 3.3). Cross-listings marked assumed follow IA4, rule R6. Perqo is fictional; the tabs, the categories, New claim, Check and submit and Claim submitted from IA1 and IA2, section 5.3; the fixes from IA3, Deliverable; the objects and catalogue items from IA4, Deliverables A and B; the Help centre pages from IA5, Deliverable A; the rest from this Deliverable.", "root": {"label": "Perqo app", "note": "tab bar: the global routes; entries in B.4", "tone": 3, "children": [
 {"label": "Join and sign in", "type": "section", "note": "A-0 · [signed out]", "tone": 3, "children": [
  {"label": "Join", "type": "form", "note": "A-0.1 · entry: HR's invitation", "tone": 3},
  {"label": "Sign in", "type": "form", "note": "A-0.2 · entry: opening the app, signed out", "tone": 3}]},
 {"label": "Home", "type": "home", "note": "A-1 · entry: opening the app", "tone": 3, "children": [
  {"label": "Balance", "type": "detail", "note": "on Home: each open category and what remains → see A-2.1 to A-2.4", "tone": 3},
  {"label": "Your balance explained", "type": "external", "note": "→ see H-2.2.1", "tone": 3},
  {"label": "Recent activity", "type": "index", "note": "on Home: purchases and claims, newest first; Submitted", "tone": 3},
  {"label": "New claim", "type": "form", "note": "on Home: a button → see A-3.1", "tone": 3}]},
 {"label": "Benefits", "type": "index", "note": "A-2 · the four categories only; each category, entry: a link", "tone": 3, "children": [
  {"label": "Health", "type": "detail", "note": "A-2.1 · Fitness: gym membership, yoga class, swimming pool entry; Therapy: therapy session; also: bike helmet, covered under Mobility (assumed)", "tone": 3},
  {"label": "Learning", "type": "detail", "note": "A-2.2 · Courses: coding course, cookery course; Books: book; also: yoga class, covered under Health (assumed)", "tone": 3},
  {"label": "Mobility", "type": "detail", "note": "A-2.3 · Public transport: train pass; Bike: bike helmet, bike repair", "tone": 3},
  {"label": "Meals", "type": "detail", "note": "A-2.4 · Restaurants: restaurant meal; Groceries: groceries; also: cookery course, covered under Learning (assumed)", "tone": 3},
  {"label": "What you can claim in each category", "type": "external", "note": "on each category screen → see H-2.1.3", "tone": 3}]},
 {"label": "Claims", "type": "index", "note": "A-3 · Submitted, Approved, Rejected, Paid; newest first", "tone": 3, "children": [
  {"label": "New claim", "type": "form", "note": "A-3.1 · entry: a Help centre link · Claims over the limit need HR approval", "tone": 3, "children": [
   {"label": "How approval rules work", "type": "external", "note": "→ see H-1.2.5", "tone": 3}]},
  {"label": "Check and submit", "type": "form", "note": "A-3.2 · after A-3.1 · [over the balance] Edit only", "tone": 3},
  {"label": "Claim submitted", "type": "detail", "note": "A-3.3 · after A-3.2 · [first claim] modal: the notifications prompt", "tone": 3},
  {"label": "Claim", "type": "detail", "note": "A-3.4 · entry: a notification · [Rejected] the reason", "tone": 3},
  {"label": "Help with claims", "type": "external", "note": "→ see H-2.1", "tone": 3}]},
 {"label": "Card", "type": "section", "note": "A-4 · [no card issued] not issued yet", "tone": 3, "children": [
  {"label": "Card details", "type": "detail", "note": "A-4.1 · last four digits; status, Active or Frozen", "tone": 3},
  {"label": "Purchases", "type": "index", "note": "A-4.2 · newest first", "tone": 3, "children": [
   {"label": "Purchase", "type": "detail", "note": "A-4.2.1 · merchant, amount, date, category; balance after", "tone": 3}]},
  {"label": "Card offers", "type": "index", "note": "A-4.3 · entry: a link, filtered · filter by category", "tone": 3},
  {"label": "Freeze card", "type": "form", "note": "A-4.4 · modal: confirm; Unfreeze card when Frozen", "tone": 3},
  {"label": "Where you can pay with the Perqo card", "type": "external", "note": "→ see H-2.3.2", "tone": 3},
  {"label": "Freezing and unfreezing your card", "type": "external", "note": "→ see H-2.3.1", "tone": 3}]},
 {"label": "Account", "type": "section", "note": "A-5", "tone": 3, "children": [
  {"label": "Profile", "type": "detail", "note": "A-5.1", "tone": 3},
  {"label": "Notifications", "type": "index", "note": "A-5.2 · each opens its claim", "tone": 3},
  {"label": "Help", "type": "external", "note": "→ see H-2 For employees", "tone": 3}]}]}}
```

Each screen, in words, with its content in the order of A.2 (Perqo, fictional):

- **A-0 Join and sign in.** Join (A-0.1) opens from HR's invitation and confirms the employer's name and the employee's work email; Sign in (A-0.2) is for an employee who has joined and is signed out. The tab bar is not shown on either. The sign-in method is left to engineering and security.
- **A-1 Home.** Balance: each open category with what remains, each opening its category screen; the link Your balance explained; Recent activity, the latest purchases and claims mixed, newest first, with claim statuses in the Claims words (Submitted, never Pending), each item opening its Purchase or Claim; the New claim button.
- **A-2 Benefits.** The four categories open to the employee's group, nothing else. Each category screen (A-2.1 to A-2.4) shows the category's balance (remaining, spent, amount, period), What's covered (each narrower term with the covered catalogue items under it in basic-level words), the cross-listed far members after them, each naming its home ("Yoga class: covered under Health"), the route "Card offers in Learning" when the category has offers, New claim with the category already chosen, and the link What you can claim in each category (H-2.1.3).
- **A-3 Claims.** The four state groups, newest first in each; New claim; Help with claims. New claim (A-3.1) asks for a category (open ones only), shows that category's balance, asks for the amount and the receipt (Take a photo, or Choose a file), and shows the rule "Claims over the limit need HR approval", with the group's limit and a link to How approval rules work. Check and submit (A-3.2) shows category, amount and the balance after, with Edit and Submit. Claim submitted (A-3.3) shows the status Submitted and, for a claim over the limit, that HR decides. Claim (A-3.4) shows status, amount, category, date submitted and the receipt; when Rejected, the reason (over the balance, or by HR) and the link Why was my claim rejected?.
- **A-4 Card.** Card details (A-4.1: the last four digits and the status, Active or Frozen, IA4's card attributes), Purchases (A-4.2, newest first) and each Purchase (A-4.2.1: merchant, amount, date, category and the category's balance after), Card offers (A-4.3: offers for items in the open categories, filterable by category, each with title, discount, merchant and valid until), Freeze card (A-4.4: a modal asks to confirm; on a Frozen card the action reads Unfreeze card). Links Where you can pay with the Perqo card (H-2.3.2) and Freezing and unfreezing your card (H-2.3.1) sit on Card.
- **A-5 Account.** Profile (name, work email), Notifications (each about one claim and opening it: IA4, Deliverable A), Help (For employees). *Note, 9 November 2026: since IA8 (section 4.5) a notification can also be about a declined card payment, opening the merchant's category screen (A-2.1 to A-2.4; Meals in C.2) for a balance or Card for a Frozen card (E-8).*

The tab bar stays on every screen except Join, Sign in and the modals. A claim in progress is kept, as entered, when the employee moves to another tab and back, by the same reasoning as Neusesser and Sunwall's rule on preserving input (Neusesser and Sunwall 2023).

### B.4 · Entry points and addresses

Every way into the app, where it lands and its address (Perqo, fictional; rules from section 6.3; IA4, section 5).

| ID | Entry | From | Lands on | Address |
|---|---|---|---|---|
| E-1 | Opening the app | the phone | Home, A-1; Sign in, A-0.2, when signed out | perqo.com/app/home |
| E-2 | HR's invitation | an email to the employee's work email, sent from Admin (IA4, A.3: employee -> invite) | Join, A-0.1; without the app, Get the Perqo app, S-6 | perqo.com/app/join/{invitation} |
| E-3 | Getting the app | Get the Perqo app, S-6, on perqo.com (IA5, section 5.5) | the app store, then E-2 | perqo.com/app |
| E-4 | A notification about a claim | the phone's notifications, or Notifications, A-5.2 | Claim, A-3.4 | perqo.com/app/claims/{claim ID} |
| E-5 | A link from a Help centre article | for example How to claim back a receipt, H-2.1.1 | New claim, A-3.1 | perqo.com/app/claims/new |
| E-6 | A link to a category | for example What you can claim in each category, H-2.1.3 | the category screen | perqo.com/app/benefits/cat-lea/learning (identifier, then term, as IA5's /product/benefits/cat-lea/learning) |
| E-7 | A link to offers in a category | a category screen, or a Help centre article | Card offers, filtered | perqo.com/app/card/offers?category=cat-mea |
| E-8 | A notification about a declined card payment (IA8, section 4.5; note, 9 November 2026) | the phone's notifications, or Notifications, A-5.2 | the merchant's category screen (A-2.1 to A-2.4; Meals in C.2) for a balance; Card, A-4, for a Frozen card | none set |

The app's ways in start where IA5 left them: employees get the app from S-6 and join from HR's invitation, and they do not sign in on perqo.com (IA5, section 5.5). IA5's assumption that an employee may press perqo.com's Sign in and land on Admin's sign-in screen stays with IA7, which owns that screen; the app adds no route to it. (Note, 3 November 2026: IA7 takes IA5's proposal with one change, in its Deliverable C, C.5, and sets Admin's names for card and notification in its section 2.3, which the table in section 6.2 now gives.) The other screens' addresses follow the same form: /app/benefits, /app/claims, /app/card, /app/card/purchases/{purchase ID}, /app/account. A screen that moves keeps a redirect from its old address (IA4, section 5).

### B.5 · Screen states

The states of each screen that has one, by the four decisions of section 4 (Perqo, fictional); a screen with none is left out. An empty state says what will appear, why it is empty and the next route; an error state names its remedy and keeps the input; a permission state degrades without blocking; "shown later" is what progressive disclosure keeps back: one level down, or below the screen's first content.

| Screen | Empty | Error | Permission | Shown later |
|---|---|---|---|---|
| Home, A-1 | [no category open] HR chooses the open categories; Help | [no connection] the last balances, with their time | none | spent, amount and period, on the category screen |
| Category screen, A-2.1 to A-2.4 | [balance used up] no balance left this period; Why can't I use money from another category?; [no allocation this period] Your budget for this period is not set yet | none | [category closed] not shown | cross-listings, after the home items |
| Claims, A-3 | [no claims] How to claim back a receipt; New claim | [no connection] the last list, with its time | none | the claim, on tap |
| New claim, A-3.1 | none | [receipt missing] by the Receipt field; input kept | [camera refused] Choose a file | the limit, in the rule line |
| Check and submit, A-3.2 | none | [over the balance] Edit only | none | none |
| Claim submitted, A-3.3 | none | none | [first claim] the notifications prompt | none |
| Card, A-4 | [no card issued] not issued yet; claims still work | none | none | card details, on tap |
| Purchases, A-4.2 | [no purchases] Where you can pay with the Perqo card | [no connection] the last list, with its time | none | the purchase, on tap |
| Card offers, A-4.3 | [no offers] the route is hidden | none | [category closed] its offers not shown | the filter by category |
| Notifications, A-5.2 | [none yet] what will appear here | none | [not allowed] how to allow notifications | the claim, on tap |

*Note, 9 November 2026: the category screen's second empty state, for a category open to the group with no allocation for the period, added from IA8's decision (IA8, section 4.2; decision log DL-008, IA9, Deliverable D); no payment or claim is possible there.*

```viz
{"kind": "matrix", "caption": "Screen states: the empty, error and permission states of the Perqo app screens that have them, and what each shows later, F2; supports the decision on what each screen shows under each condition and by which route the employee goes on (Deliverable B, B.5). Conditions in square brackets, as IA2's conditional area; empty-state rule this unit's synthesis from IA3, A3 and F2; the category screen's [no allocation this period] state from IA8, section 4.2 (decision log DL-008, IA9, Deliverable D; note, 9 November 2026); error states from Neusesser and Sunwall, 'Error-Message Guidelines', NN/g, 2023; permissions from Android Developers, 'Request runtime permissions', 2026 (platform documentation); the closed category from IA2, section 5.3, the card not yet issued from IA4, R-11, and the hidden offers route from IA4, Deliverable B, R5 (section 4); disclosure from Nielsen, 'Progressive Disclosure', NN/g, 2006. Rows tone 3, the app, keyed 'app'; tone 6 marks a stop, keyed 'stop', a state in which the path ends without success until something changes (IA2, section 5.2). The stops: Home's [no category open] and [no connection]; the category screen's [balance used up] and [no allocation this period]; Claims' and Purchases' [no connection]; New claim's [receipt missing]; Check and submit's [over the balance]; Card's [no card issued]. A blank cell is \"none\" in B.5's table. Perqo is fictional.", "cols": ["Empty", "Error", "Permission", "Shown later"], "rows": [
 {"label": "Home", "tone": 3, "cells": [{"mark": "[no category open] HR chooses the open categories; Help", "tone": 6}, {"mark": "[no connection] the last balances, with their time", "tone": 6}, null, "spent, amount and period, on the category screen"]},
 {"label": "Category screen", "tone": 3, "cells": [{"mark": "[balance used up] no balance left this period; Why can't I use money from another category?; [no allocation this period] Your budget for this period is not set yet", "tone": 6}, null, "[category closed] not shown", "cross-listings, after the home items"]},
 {"label": "Claims", "tone": 3, "cells": ["[no claims] How to claim back a receipt; New claim", {"mark": "[no connection] the last list, with its time", "tone": 6}, null, "the claim, on tap"]},
 {"label": "New claim", "tone": 3, "cells": [null, {"mark": "[receipt missing] by the Receipt field; input kept", "tone": 6}, "[camera refused] Choose a file", "the limit, in the rule line"]},
 {"label": "Check and submit", "tone": 3, "cells": [null, {"mark": "[over the balance] Edit only", "tone": 6}, null, null]},
 {"label": "Claim submitted", "tone": 3, "cells": [null, null, "[first claim] the notifications prompt", null]},
 {"label": "Card", "tone": 3, "cells": [{"mark": "[no card issued] not issued yet; claims still work", "tone": 6}, null, null, "card details, on tap"]},
 {"label": "Purchases", "tone": 3, "cells": ["[no purchases] Where you can pay with the Perqo card", {"mark": "[no connection] the last list, with its time", "tone": 6}, null, "the purchase, on tap"]},
 {"label": "Card offers", "tone": 3, "cells": ["[no offers] the route is hidden", null, "[category closed] its offers not shown", "the filter by category"]},
 {"label": "Notifications", "tone": 3, "cells": ["[none yet] what will appear here", null, "[not allowed] how to allow notifications", "the claim, on tap"]}],
 "legend": [{"mark": "app", "means": "the Perqo app", "tone": 3}, {"mark": "stop", "means": "the path ends without success here", "tone": 6}]}
```

*Note, 17 November 2026: this figure's key no longer prints the drawing's tone names; each swatch now names what its cells mean, and the caption says so (carried proposal CP-3, row S-BW; re-checked by a fresh Opus 5.5 agent from its frames). No cell changed.*

### B.6 · Where this map departs from IA3, and why

- **The Balance total is dropped.** IA3's B1 fix asked for the four category balances on Home under Balance and said nothing of the total. This map removes it, because the total is the one-pot model IA3 found the fault in, and a figure the system never checks a claim against has no decision to support (section 4.1; IA3, section 2.3).
- **"One placing" for offers is read as one screen with routes to it.** IA3's C4 and D2 fixes ask for one placing and one label. Card offers is one screen with one label, under Card, because an offer is a discount for paying with the Perqo card and the Card tab holds card things (C1). Each category screen links to it, filtered to its category, because an employee looking at Meals is where a Meals offer is useful (IA3, F2), and IA4 classified offers by benefit category for exactly that filter (IA4, sections 1.2 and 5). The route goes to the same screen, so D2 holds: one thing, one label, one place. Home's offers banner is gone. The partnerships team asked for offers on Home and in Benefits (IA3, Deliverable); this map records that request and gives it neither placing, for C1 and C4, and whether the filtered route finds offers as well as a Home banner did is a test for IA11.
- **A Claim screen is added.** IA3's as-is had no claim detail; B2's fix groups the list, and a rejected claim needs a place to show its reason. The screen is also where a notification lands (B.4, E-4).
- **Check and submit gains a state.** IA2's wireflow went from Check and submit to Submit with no over-balance branch (IA2, section 5.3); the rule rejects such a claim (IA2, section 5.3; IA3, section 2.3). The state prevents the rejection (section 4.3). The rule itself is unchanged.
- **Recent activity is kept.** IA3's list of the labels IA6 keeps left it out when IA3 was filed (the list was corrected on 3 November 2026), but its A2 verdict passed it, and its fault was the word Pending (D2), which is fixed. It is a view of two objects, as IA4 said Home is (IA4, section 4.3), and it routes to each item.

## Deliverable · C · Three core flows as wireflows

*Face of these artefacts (IA2, the notation sheet): three wireflows of the Perqo app, at fidelity F2, each with its failure paths; decision: which screens each core task needs, what changes on them, and where the task can stop; readers: design and engineering (screens and states to build), support (where an employee gets stuck), product management (where each task starts and ends); leaves out: visual design, the claim's decision tree and lifecycle (IA2, section 5.3; IA8), Admin's screens (IA7), the merchant's surface beyond the till; owner: the IA designer; version 1, dated 3 November 2026; C.2 amended 9 November 2026 (DL-004; IA8, section 4.5; the decision log entry added by IA9, section 4.5); Perqo is fictional.*

IA2's decision table gives this unit the user flow and the task flow "as wireflows" (IA2, Deliverable): each wireflow below follows one task's main path, as a task flow does, and carries the branches and failure paths of a user flow at F2. Each wireflow uses IA2's screen notation: a frame with a title bar is one screen, bars and blocks are placeholder text and areas, a button is a control, and an arrow is labelled with the action or the condition that moves the person (IA2, section 5.2; Laubheimer 2016). A screen title with a [condition] is a state of that screen. Two screens per row keep each drawing legible on a phone, scrolled sideways.

### C.1 · See a balance

The employee opens the app on Home and sees each open category with what remains (Perqo, fictional). Tapping Your balance explained opens H-2.2.1 on perqo.com. Tapping Learning opens its category screen: the Learning balance, What's covered with its items, the cross-listed yoga class naming its home, and New claim. When the Learning balance is used up, the same screen says so, and its link Why can't I use money from another category? opens H-2.2.2, the article IA5 wrote for the employee who has money in Meals and none in Learning (IA5, Deliverable A). The tab bar takes the employee back to Home. The empty and offline states of Home are in B.5.

```viz
{"kind": "wireflow", "per_row": 2, "caption": "Wireflow: an employee sees a balance in the Perqo app, F2, with the used-up state of a category screen; supports the decision on which screens the task needs and how a category's balance is read (Deliverable C, C.1). Tone 3 the app; tone 1 perqo.com, for the two Help centre articles (H-2.2.1, H-2.2.2, IA5, Deliverable A); tone 6 a state where the path stops. The yoga class cross-listing is assumed (IA4, rule R6). Wireflow form from Laubheimer, NN/g, 2016; screens from Deliverable B. Perqo is fictional.", "screens": [
 {"id": "home", "title": "Home", "tone": 3, "lines": ["Balance", "Health", {"bar": 0.6}, "Learning", {"bar": 0.3}, "Mobility", {"bar": 0.4}, "Meals", {"bar": 0.8}, {"button": "Your balance explained"}, "Recent activity", {"bar": 0.7}, {"button": "New claim"}]},
 {"id": "learning", "title": "Learning", "tone": 3, "lines": ["Learning balance", {"bar": 0.3}, "What's covered", "Courses: coding course, cookery course", "Books: book", "Yoga class: covered under Health", {"button": "New claim"}]},
 {"id": "explained", "title": "Your balance explained", "tone": 1, "lines": ["perqo.com · For employees · Balance", {"bar": 0.9}, {"block": 40}]},
 {"id": "usedup", "title": "Learning [balance used up]", "tone": 6, "lines": ["Learning balance: 0", "No Learning balance left this period", {"button": "Why can't I use money from another category?"}, "What's covered", {"bar": 0.6}]},
 {"id": "onecat", "title": "Why can't I use money from another category?", "tone": 1, "lines": ["perqo.com · For employees · Balance", {"bar": 0.9}, {"block": 40}]}],
 "links": [
  {"from": "home", "to": "learning", "label": "tap Learning"},
  {"from": "learning", "to": "home", "label": "tap Home"},
  {"from": "home", "to": "explained", "label": "tap Your balance explained"},
  {"from": "learning", "to": "usedup", "label": "[Learning balance used up]"},
  {"from": "usedup", "to": "onecat", "label": "tap Why can't I use money from another category?"}]}
```

### C.2 · Spend a benefit

Spending is done with the Perqo card at a merchant's till; the app's part is before and after (Perqo, fictional; IA1, section 5). From Home the employee taps Meals, sees the Meals balance and what's covered, and either taps Card offers in Meals to see the offers for Meals items or goes straight to a merchant. At the till, a card payment spends from the allocation of the merchant's category (IA4, Deliverable A). This unit sets what happens when it cannot (Perqo, fictional): a payment over the balance of the merchant's category, or with the card Frozen, is declined at the till. A taken payment appears in Purchases, newest first, as a Purchase with its merchant, amount, date, category and the category's balance after. A declined attempt moves no money, so it is not a card payment and is not in Purchases; the employee sees the decline at the till, and the Card screen shows a Frozen card with Unfreeze card. *Note, 9 November 2026: this unit proposed to IA8 whether a declined attempt should reach the app (A.2); IA8 decided it (IA8, section 4.5): a declined attempt sends a notification, "Card payment declined", naming the merchant, the amount and the reason, and opening the Meals screen for a balance (Meals [after a decline] in the wireflow below, the ordinary Meals screen reached from the notification) or Card for a Frozen card; the wireflow below carries the two routes, and the till is drawn in tone 2, the merchant side.*

```viz
{"kind": "wireflow", "per_row": 2, "caption": "Wireflow: an employee spends a benefit with the Perqo card, F2, from the Meals balance and Card offers to the till and the Purchase, with the declined path and the decline notification's two routes back into the app; supports the decision on what the app shows before and after a card payment (Deliverable C, C.2). Tone 3 the app; tone 2 the merchant side, for the till; tone 6 the declined payment, where the spending ends without success, the notification's two routes leading on in the app. A card payment spends from the allocation of the merchant's category (IA4, Deliverable A); the decline rule from this section; the decline notification's two routes from IA8, section 4.5 (note, 9 November 2026). The cookery course cross-listing is assumed (IA4, rule R6). Wireflow form from Laubheimer, NN/g, 2016; screens from Deliverable B. Perqo is fictional.", "screens": [
 {"id": "home", "title": "Home", "tone": 3, "lines": ["Balance", "Health", {"bar": 0.6}, "Learning", {"bar": 0.3}, "Mobility", {"bar": 0.4}, "Meals", {"bar": 0.8}, "Recent activity", {"bar": 0.7}]},
 {"id": "meals", "title": "Meals", "tone": 3, "lines": ["Meals balance", {"bar": 0.8}, "What's covered", "Restaurants: restaurant meal", "Groceries: groceries", "Cookery course: covered under Learning", {"button": "Card offers in Meals"}, {"button": "New claim"}]},
 {"id": "offers", "title": "Card offers", "tone": 3, "lines": ["Filter: Meals", "Title and discount", {"bar": 0.7}, "Merchant, valid until", {"bar": 0.5}, "Title and discount", {"bar": 0.6}]},
 {"id": "till", "title": "At the till", "tone": 2, "lines": ["Merchant's till", {"block": 30}, "Pay with the Perqo card"]},
 {"id": "purchase", "title": "Purchase", "tone": 3, "lines": ["Merchant", {"bar": 0.6}, "Amount and date", {"bar": 0.5}, "Category: Meals", "Meals balance after", {"bar": 0.6}]},
 {"id": "declined", "title": "Declined at the till", "tone": 6, "lines": ["Payment declined", "[over the Meals balance] or [card Frozen]"]},
 {"id": "frozen", "title": "Card [Frozen]", "tone": 3, "lines": ["Card details", "Status: Frozen", {"button": "Unfreeze card"}, {"button": "Purchases"}]},
 {"id": "mealsback", "title": "Meals [after a decline]", "tone": 3, "lines": ["Meals balance", {"bar": 0.1}, "What's covered"]}],
 "links": [
  {"from": "home", "to": "meals", "label": "tap Meals"},
  {"from": "meals", "to": "offers", "label": "tap Card offers in Meals"},
  {"from": "meals", "to": "till", "label": "pay at a Meals merchant"},
  {"from": "offers", "to": "till", "label": "pay at the offer's merchant"},
  {"from": "till", "to": "purchase", "label": "[within the Meals balance, card Active] open Card, Purchases"},
  {"from": "till", "to": "declined", "label": "[over the Meals balance, or card Frozen]"},
  {"from": "declined", "to": "mealsback", "label": "notification: Card payment declined [over the Meals balance]"},
  {"from": "declined", "to": "frozen", "label": "notification: Card payment declined [card Frozen]"}]}
```

### C.3 · Submit a reimbursement claim

This extends IA2's claim wireflow and keeps every screen, label and arrow in it: Claims, New claim, Check and submit and Claim submitted; tap New claim, tap Continue, tap Edit back to New claim, and tap Submit with no way back (IA2, section 5.3). It adds what IA3's fixes and this unit's decisions require (Perqo, fictional). Claims lists all four states, with Help with claims. New claim shows the chosen category's balance, two ways to add the receipt, and the rule "Claims over the limit need HR approval". When the amount is over the category's balance, Continue opens Check and submit in its over-balance state, with Edit as the only route. Claim submitted shows Submitted and, on the first claim, Done opens the notifications prompt, a modal that either answer closes. Later, when the claim moves, the notification opens the Claim screen: Approved (then Paid, by the lifecycle IA2 drew), or Rejected with its reason and the link Why was my claim rejected?.

```viz
{"kind": "wireflow", "per_row": 2, "caption": "Wireflow: an employee submits a reimbursement claim in the Perqo app, F2, extending IA2, section 5.3's claim wireflow (Claims, New claim, Check and submit, Claim submitted; Edit back; Submit with no way back) with IA3's B1, B2 and C4 fixes, the over-balance state, the notifications prompt and the Claim screen's outcomes; supports the decision on which screens and states the claim task needs and where it cannot be undone (Deliverable C, C.3). Tone 3 the app; tone 6 a state where the path stops. The rule from IA2, section 5.3 and IA3, section 2.3; the no-way-back label stands for Garrett's crossbar (IA2, section 5.1); wireflow form from Laubheimer, NN/g, 2016; screens from Deliverable B. Perqo is fictional.", "screens": [
 {"id": "list", "title": "Claims", "tone": 3, "lines": ["Submitted", {"bar": 0.7}, "Approved", {"bar": 0.5}, "Rejected", {"bar": 0.3}, "Paid", {"bar": 0.8}, {"button": "Help with claims"}, {"button": "New claim"}]},
 {"id": "form", "title": "New claim", "tone": 3, "lines": ["Category", {"bar": 0.6}, "Learning balance", {"bar": 0.4}, "Amount", {"bar": 0.4}, "Receipt", {"button": "Take a photo"}, {"button": "Choose a file"}, "Claims over the limit need HR approval", {"button": "Continue"}]},
 {"id": "review", "title": "Check and submit", "tone": 3, "lines": ["Category and amount", {"bar": 0.7}, "Learning balance after", {"bar": 0.5}, {"button": "Edit"}, {"button": "Submit"}]},
 {"id": "over", "title": "Check and submit [over the balance]", "tone": 6, "lines": ["Category and amount", {"bar": 0.7}, "More than your Learning balance", {"button": "Edit"}]},
 {"id": "done", "title": "Claim submitted", "tone": 3, "lines": ["Status: Submitted", "[over the limit] HR decides", {"button": "Done"}]},
 {"id": "notify", "title": "Notifications prompt (modal)", "tone": 3, "lines": ["[first claim only]", "Get told when your claim is approved, rejected or paid", {"button": "Allow"}, {"button": "Not now"}, "[either answer closes it]"]},
 {"id": "approved", "title": "Claim [Approved]", "tone": 3, "lines": ["Status: Approved", "Amount, category, date submitted", {"bar": 0.6}, "Receipt", {"block": 24}, "Then Paid → see the claim's lifecycle (IA2, section 5.3)"]},
 {"id": "rejected", "title": "Claim [Rejected]", "tone": 6, "lines": ["Status: Rejected", "Rejected by HR, or over the balance", {"button": "Why was my claim rejected?"}]}],
 "links": [
  {"from": "list", "to": "form", "label": "tap New claim"},
  {"from": "form", "to": "review", "label": "tap Continue"},
  {"from": "review", "to": "form", "label": "tap Edit"},
  {"from": "form", "to": "over", "label": "tap Continue [over the balance]"},
  {"from": "over", "to": "form", "label": "tap Edit"},
  {"from": "review", "to": "done", "label": "tap Submit (no way back)"},
  {"from": "done", "to": "notify", "label": "[first claim] tap Done"},
  {"from": "done", "to": "approved", "label": "later: tap the notification [approved]"},
  {"from": "done", "to": "rejected", "label": "later: tap the notification [rejected]"}]}
```

A claim can still end Rejected, over the balance, when the category's balance changes between Check and submit and Submit, for example by a card payment in the same category; the Claim screen names that reason.

## What IA8 and IA11 take

**IA8** takes the app map (B.3, with B.4's entry points and addresses) and the three wireflows (C.1 to C.3) as the app's layer of the cross-surface interaction map. The joins it will need are named on the map: each external route to its Help centre page (IA5's IDs), each entry to its source on Admin or perqo.com (E-2 to Admin's invite, E-3 to S-6), each claim state on A-3 and A-3.4 to the claim's state diagram and decision tree (IA2, section 5.3), and the Purchase to the card payment's category rule (IA4, Deliverable A). One question is proposed to IA8 and left unset here: whether a declined card attempt should reach the app, as a notification or a record, which would extend the notification beyond claims and the data model beyond movements of money. *Note, 9 November 2026: IA8 decided it, as a notification and no record in Purchases, with a new object, the declined attempt (O-18), outside the transactions (IA8, section 4.5).*

**IA11** tests this IA. Every assumption in it, with the test it needs (the methods are IA11's to specify; the pass mark is set there):

| Assumption | Where | Test (IA11) | What changes if it fails |
|---|---|---|---|
| The task frequencies and their ranking | Deliverable A | product analytics by task after launch; before launch, a diary study with employees | what sits on Home and one tap from it |
| Most visits are one or two tasks begun from Home or a notification | section 3.2 | session paths in analytics | Home's routes; the case for the hub |
| Employees read the four balances as four pots | A-1, A-2.1 to A-2.4 | a usability task: with money in Meals only, can you claim this course? | Home's layout; the balance wording |
| Employees find a rejected claim in Claims | A-3 | first-click test from Home: your claim was turned down; where would you look? (IA3, "What this hands on") | the Claims grouping |
| The far members are found by their cross-listings | A-2.1, A-2.2, A-2.4 | tree test of the Benefits tree with yoga class, cookery course and bike helmet (IA3, C3; IA4, R6) | each cross-listing kept or removed |
| Card offers are found under Card and from the category screens | A-4.3 | tree test and first-click test | the placing (B.6) |
| The rule line is understood before submitting | A-3.1 | usability test: which of two claims waits for HR? | the rule's wording and place |
| Profile, Notifications and Help are found under Account | A-5 | tree test | Notifications' placing |
| Asking for notifications after the first claim gets more employees to allow them than asking at first run | A-3.3 | a comparison of the two timings in analytics, by the share who allow | the prompt's timing |
| An employee who installs the app from the invitation can join | E-2, A-0.1 | usability test of the join path on a phone without the app | whether Join needs another way in |
| Employees understand a declined payment from the balance they saw | C.2 | interviews after a decline; support's tickets (IA12 as proxy) | the decline notification's wording and route (IA8, section 4.5, 9 Nov 2026) |
| The renamed labels predict their pages (A1 to A3) | every label in B.2 | tree test and first-click test (IA3, "What this hands on") | the labels |

## Perqo facts set by this unit

Every fact below is a course convention (Perqo, fictional), never evidence about the world. Each keeps every registered fact; none renames an IA1 to IA5 label. IA3's eight proposals for IA6 become facts as B.1 applies them.

| Fact | Set in | Left free |
|---|---|---|
| The app's screens carry IDs A-0 to A-5 (A-0 Join and sign in, A-0.1 Join, A-0.2 Sign in; A-1 Home; A-2 Benefits, A-2.1 to A-2.4 the categories; A-3 Claims, A-3.1 New claim, A-3.2 Check and submit, A-3.3 Claim submitted, A-3.4 Claim; A-4 Card, A-4.1 Card details, A-4.2 Purchases, A-4.2.1 Purchase, A-4.3 Card offers, A-4.4 Freeze card; A-5 Account, A-5.1 Profile, A-5.2 Notifications) | Deliverable B | visual design |
| Every app screen has an address under perqo.com/app/, identifier first; with the app installed it opens the screen, without it the address serves Get the Perqo app (S-6); entries E-1 to E-7, and E-8 since IA8 (section 4.5, 9 Nov 2026) | section 6.3; Deliverable B, B.4 | the identifiers' format for claims and purchases |
| Home shows each open category with what remains, no total; Recent activity mixes purchases and claims, newest first, and says Submitted | section 4.1; Deliverable B | how many items Recent activity shows |
| Each category screen shows the balance (remaining, spent, amount, period), What's covered with the covered catalogue items under each narrower term, cross-listed far members naming their home (assumed), the route to Card offers in that category when it has offers, New claim with the category chosen, and the link What you can claim in each category (H-2.1.3) | Deliverable B, B.3 | the order of items within a narrower term |
| Card carries the links Where you can pay with the Perqo card (H-2.3.2) and Freezing and unfreezing your card (H-2.3.1) | Deliverable B, B.3 | none |
| The example client's policy covers all twelve sample catalogue items, BI-001 to BI-012 (extends IA3's six) | Deliverable B, B.3 | other clients' policies |
| Card offers is one screen under Card (A-4.3), filterable by category by identifier, listing only offers for items in the employee's open categories; Home has no offers banner; the partnerships team's request for two placings is recorded and not met | Deliverable B, B.1 and B.6 | the number of offers |
| Claims groups by Submitted, Approved, Rejected, Paid, newest first in each; the Claim screen (A-3.4) shows status, amount, category, date submitted, receipt and, when Rejected, the reason (over the balance, or by HR): a new claim attribute, rejection reason | Deliverable B | the wording of each reason |
| New claim shows the chosen category's balance, takes the receipt by Take a photo or Choose a file, and shows "Claims over the limit need HR approval" with the group's limit and a link to H-1.2.5 | section 4; Deliverable C, C.3 | the limit's amount |
| Check and submit, when the amount is over the category's balance, shows "More than your Learning balance" (in the chosen category's name) with Edit only | section 4.3; Deliverable C, C.3 | none |
| The camera is asked for when the employee taps Take a photo; notifications are asked for once, after the first claim is submitted | section 4.4 | the prompt's wording beyond its purpose |
| A card payment over the balance of the merchant's category, or with the card Frozen, is declined at the till; a declined attempt is not a card payment and is not in Purchases; the app shows it as a notification (IA8, section 4.5, 9 Nov 2026) | Deliverable C, C.2 | the notice's wording |
| An employee with no card issued sees the Card tab in the state "Your Perqo card has not been issued yet" | section 4.4 | when cards are issued |
| A category closed to the group is not shown, nor any cross-listing or offer that belongs to it | section 4.4 | none |
| Without a connection, Home, Claims and Purchases show their last loaded content with the time it was loaded | section 4.3 | none |
| The tab bar shows on every screen except Join, Sign in and modals; a claim in progress is kept when the employee changes tab | Deliverable B, B.3 | none |
| HR's invitation is an email to the employee's work email with a link that opens Join (A-0.1), or S-6 without the app; Join confirms the employer's name and the work email | Deliverable B, B.4 | the sign-in method |
| Task frequencies per employee, assumed: pay with the card 8 a month; see the balance 3; read a notification 2; check a purchase and track a claim 1.5 each; submit a claim 1; find what's covered and find card offers 0.5 each; read a help article 0.3; freeze or unfreeze the card and see the profile 0.1 each; join once | Deliverable A | measured use (IA11) |
| New calls to action by the employee: claim -> view; catalogue item -> view | Deliverable A | none |
| Complexity and priority of the app's calls to action, and the attribute order on each screen, as in A.2 | Deliverable A, A.2 | none |

## Sources

- Android Developers. "About deep links". Page updated 28 October 2026 (platform documentation, checked 3 November 2026). [developer.android.com/training/app-links](https://developer.android.com/training/app-links)
- Android Developers. "Layouts and navigation patterns". Page updated 22 October 2026 (platform documentation, checked 3 November 2026). [developer.android.com/design/ui/mobile/guides/layout-and-content/layout-and-nav-patterns](https://developer.android.com/design/ui/mobile/guides/layout-and-content/layout-and-nav-patterns?hl=en)
- Android Developers. "Request runtime permissions". Page updated 28 October 2026 (platform documentation, checked 3 November 2026). [developer.android.com, runtime permissions](https://developer.android.com/training/permissions/requesting)
- Apple. Human Interface Guidelines, "Tab bars". Undated (platform documentation; only the page's description could be read, 3 November 2026). [developer.apple.com/design/human-interface-guidelines/tab-bars](https://developer.apple.com/design/human-interface-guidelines/tab-bars)
- Apple Developer Documentation. "Allowing apps and websites to link to your content". Undated (platform documentation; only the page's description could be read, 3 November 2026). [developer.apple.com/documentation/xcode/allowing-apps-and-websites-to-link-to-your-content](https://developer.apple.com/documentation/xcode/allowing-apps-and-websites-to-link-to-your-content)
- Budiu, Raluca. "Basic Patterns for Mobile Navigation: A Primer". Nielsen Norman Group, 15 November 2015. [nngroup.com/articles/mobile-navigation-patterns](https://www.nngroup.com/articles/mobile-navigation-patterns/)
- Carroll, John M., and Mary Beth Rosson. "The Paradox of the Active User". In J. M. Carroll, ed., *Interfacing Thought: Cognitive Aspects of Human-Computer Interaction*. MIT Press, 1987 (not seen; cited as reported by Nielsen 1998).
- Hackos, JoAnn T., and Janice C. Redish. *User and Task Analysis for Interface Design*. Wiley, 1998 (no claim drawn from it).
- Hoober, Steven. "How Do Users Really Hold Mobile Devices?" UXmatters, 18 February 2013. [uxmatters.com/mt/archives/2013/02/how-do-users-really-hold-mobile-devices.php](https://www.uxmatters.com/mt/archives/2013/02/how-do-users-really-hold-mobile-devices.php?) (a practitioner's observational study; practice).
- Laubheimer, Page. "Wireflows: A UX Deliverable for Workflows and Apps". Nielsen Norman Group, 4 December 2016. [nngroup.com/articles/wireflows](https://www.nngroup.com/articles/wireflows/)
- McGovern, Gerry. "What Really Matters: Focusing on Top Tasks". A List Apart, April 2015; republished by Center Centre, 20 January 2016. [articles.centercentre.com/?p=877](https://articles.centercentre.com/?p=877) (practice).
- Neusesser, Tim, and Evan Sunwall. "Error-Message Guidelines". Nielsen Norman Group, 14 May 2023. [nngroup.com/articles/error-message-guidelines](https://www.nngroup.com/articles/error-message-guidelines/)
- Nielsen, Jakob. "Paradox of the Active User". Nielsen Norman Group, 4 October 1998. [nngroup.com/articles/paradox-of-the-active-user](https://www.nngroup.com/articles/paradox-of-the-active-user/)
- Nielsen, Jakob. "Progressive Disclosure". Nielsen Norman Group, 3 December 2006. [nngroup.com/articles/progressive-disclosure](https://nngroup.com/articles/progressive-disclosure/)
- Pernice, Kara, and Raluca Budiu. "Hamburger Menus and Hidden Navigation Hurt UX Metrics". Nielsen Norman Group, 26 June 2016. [nngroup.com/articles/hamburger-menus](https://www.nngroup.com/articles/hamburger-menus/)
- Prater, Sophia V. "OOUX: A Foundation for Interaction Design". A List Apart, 19 April 2016. [alistapart.com/article/ooux-a-foundation-for-interaction-design](https://alistapart.com/article/ooux-a-foundation-for-interaction-design/) (practice).
- Resmini, Andrea, and Luca Rosati. *Pervasive Information Architecture: Designing Cross-Channel User Experiences*. Morgan Kaufmann, 2011. Chs 3 to 8; ch. 5, "Consistency". Contents at [shop.elsevier.com](https://shop.elsevier.com/books/pervasive-information-architecture/resmini/978-0-12-382094-5).
- Rosala, Maria. "Task Analysis: Support Users in Achieving Their Goals". Nielsen Norman Group, 20 September 2020. [nngroup.com/articles/task-analysis](https://www.nngroup.com/articles/task-analysis/)
- Sears, Andrew, and Ben Shneiderman. "Split Menus: Effectively Using Selection Frequency to Organize Menus". *ACM Transactions on Computer-Human Interaction* 1, no. 1 (1994): 27 to 51. Record and abstract at [pure.psu.edu](https://pure.psu.edu/en/publications/split-menus-effectively-using-selection-frequency-to-organize-men/)
- Cited through the filed units, for claims made there: Garrett, *Visual Vocabulary Quick Reference* (conditional area, crossbar); Berners-Lee 1998; Brown 2011, ch. 5; Budiu 2020; Card and others 2001; Cooper and others 2014, ch. 1; Harley 2014; Hearst 2006; Kaplan 2023; Krause 2021; Larson and Czerwinski 1998; Laubheimer 2023 ("3 Common IA Mistakes"); Nielsen 2006 ("Use Old Words"); Nielsen 2009; Whitenton 2013; Zaphiris 2000; WCAG SC 3.2.4 (IA2, IA3, IA4 and IA5, Sources).

## Unsure list

- Rosala 2020: the definition is quoted; the stages, the methods and the HTA description were read through a summary of the page, so their wording here is paraphrase.
- Sears and Shneiderman 1994: the 17 to 58% figure and the controlled-experiment result are from the abstract on a university record; the paper itself was not read.
- Carroll and Rosson 1987: cited as reported by Nielsen 1998; the chapter was not seen.
- Hackos and Redish 1998: bibliographic details from knowledge; no chapter was checked, so no claim is drawn from it.
- Pernice and Budiu 2016: the percentages, ratings and the two recommendations were read through a summary of the page; "more than a fifth" paraphrases the reported discoverability drop.
- Budiu 2015: the quoted phrases and the pattern list were read through a summary of the page; that the primer gives hierarchical drill-down no study of its own is this unit's reading of that summary.
- Apple's "Tab bars" and "Allowing apps and websites to link to your content" pages returned no body text; only their descriptions are quoted, and nothing else is claimed from them.
- Resmini and Rosati 2011: only the chapter titles were seen; nothing is claimed about the content of ch. 5.
- That a universal link or App Link address opens an ordinary web page when the app is absent is from knowledge of the platforms; the fetched pages describe only the in-app case. Perqo's fallback to S-6 is a Perqo rule; no platform claim is made for it.
- Not checked: NN/g's article on empty states in application design (rate-limited twice); nothing from it is cited. Polson and Lewis 1990 on label-following: only the bibliographic record was seen; not cited.
- Fresh check 2026-11-03 (Fable 5.1): fix · 2 errors, 4 should-fix, 11 minor; 16 applied (one as far as it held), one not applied (the pointer to IA4, section 1.2, holds); figure 1 fixed twice and passed on its third check; figures 4 and 5 fixed three times and passed on their fourth check; figure 8 fixed from the check, passed its second check, was changed from that check's notes and passed again on its fourth; figures 2, 3, 6 and 7 passed; report `audits/ux/fresh-check-IA6.md`.
- Note, 9 November 2026 (IA8, section 4.5): C.2, its wireflow (figure 7), A.2's open-question cell, B.4 (entry E-8), the A-5 entry, the facts and assumption rows and "What IA8 and IA11 take" carry IA8's decision on the declined attempt; figure 7 changed and was checked again by two fresh Opus 5.5 agents (FIX on the text, then PASS); report `audits/ux/fresh-check-IA8.md`.

Figure note 2026-11-17 (P109, row H-4): figure 5's caption now says a blank cell is "none" in B.5's table (it read as if no cell were blank). Prose unchanged; re-checked by a fresh Opus 5.5 agent (`kit/reviews/p84/`).
