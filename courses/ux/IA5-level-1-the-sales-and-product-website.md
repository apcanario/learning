---
code: IA5
title: Level 1 · the sales and product website
course: ux · IA · Information Architecture
model: Opus 5.5
written: 2026-11-03
search: off
---

# IA5 · Level 1 · the sales and product website

The first four units built the tools: IA1 the surfaces map and the shared vocabulary, IA2 the artefact catalogue and the notation, IA3 the evidence a structure is judged by and the labelling checklist, IA4 the organisation schemes, the object map and the benefits taxonomy. This unit spends them on the simplest of Perqo's three surfaces, perqo.com, the one IA1 called a shallow website hierarchy (IA1, section 5). It inventories and audits the site, chooses its structure, and hands three artefacts to the people who build and fill it: the content inventory, the sitemap and the page-template catalogue. Every figure uses IA2's notation (IA2, section 5 and the notation sheet); on a figure of one surface every box takes that surface's tone, so every perqo.com box is tone 1.

The filed units handed this one five questions by name. Where each is answered:

| Handed on by | The question | Answered in |
|---|---|---|
| IA1, Deliverable (surfaces map); IA2, section 5.3 | perqo.com's top-level areas, Book a demo among the global routes, and what crosses to Admin and the app | sections 2.4 and 5.5; Deliverable B |
| IA2, Deliverable (decision table); IA2, section 5.3 | the inventory at F2 before any redesign and at F3 as the migration list; the sitemap at F1, F2 and F3; IA2's inventory and sitemap slices extended | section 1; section 6; Deliverables A and B |
| IA3, Deliverable (checklist) | IA5's labels judged by the labelling checklist | Deliverable B, B.2 |
| IA4, section 5 (addressing rules) | one organisation system traced through navigation, filters, search and URLs on perqo.com | section 5.1; Deliverables B and C |
| IA4, Deliverable A (object map) and B ("What IA5 and DD-IA3 take") | inventory and templates built on IA4's objects and the benefits taxonomy's identifiers, Help centre articles tagged with F-CAT values, nothing renamed except under R9 | section 3.3; Deliverables A and C |

## 1 · Running a content inventory and audit

### 1.1 · Two passes over the same list

IA2 set the distinction and the outcome per item: an inventory lists what exists, an audit judges it, and each item ends as keep, update or remove (Anna Kaley, "Content Inventory and Auditing 101", Nielsen Norman Group, 27 September 2020, [nngroup.com/articles/content-audits](https://www.nngroup.com/articles/content-audits/); IA2, section 1.1). The two standard works on the method make the same split, and both follow the audit with a further step.

Kristina Halvorson and Melissa Rach give the audit its own chapter, "Audit: Take a close-up look at your current content", followed by one on "Analysis: Your content lives in a complicated world" (*Content Strategy for the Web*, 2nd ed., New Riders, 2012, chs 5 and 6; contents and index in the publisher's sample, [ptgmedia.pearsoncmg.com](https://ptgmedia.pearsoncmg.com/images/9780321808301/samplepages/0321808304.pdf)). The book's index separates "quantitative inventories" from "qualitative audits", the latter with two subtypes, "best practices assessment" and "strategic assessment"; lists "content sampling" with the factors that decide a sample (objectives, depth, maintenance frequency, updates, users, traffic); and has an entry for "rolling audits" (same index). Under the quantitative inventory's audit data the index names IDs, formats, language, last update date, technical home, title and topics, traffic, URLs and usage statistics; among the qualitative audit's factors it names accuracy, actionability, branding, business value, findability, knowledge level, messaging, target audience, usability, and voice and tone (same index). The chapters' text was not read for this unit, so it cites the book for this structure and these field names only.

Donna Spencer's *A Practical Guide to Information Architecture* (2nd ed., UX Mastery, 2014, [uxmastery.com](https://uxmastery.com/coming-soon-a-practical-guide-to-information-architecture-second-edition/)) puts the same division into its part 3, "Understanding content", where chapter 11 is "Content You Have" and chapter 12 "Content You Need", before "Communicating About Content", "Content Planning" and "Classification Schemes" (chs 13 to 15; contents from the edition's front matter). The order is the point a team can use: what exists, then what is missing, then how it will be classified. An inventory that stops at what exists cannot propose a structure, because the structure has to hold the content the site still lacks.

So a working method has three passes, each with its own question:

1. **Inventory (quantitative).** What is there? One row per page or file, with the fields below, filled from the live site. No judgement yet.
2. **Audit (qualitative).** Is each item any good, for whom, and against what? Each row gets keep, update or remove, with the reason and an owner for each update (Kaley 2020).
3. **Gap analysis.** What does the site need that it does not have? New rows, marked with a fourth status, *new*, so the list becomes the migration list engineering builds from (IA2, section 1.1: F3 as the migration list). The status is an addition to IA2's three, declared here as IA2's rule "Keep the notation; extend the legend" requires (IA2, section 4).

Kaley gives two working rules for scope: choose one that "fits your organization's needs and your team's capacity", and if the volume is too large, "start with a manageable yet impactful subset", for example the content most used or supporting top tasks; she adds that "spreadsheets tend to work best for content inventories and audits" (Kaley 2020). Halvorson and Rach's "content sampling" and "rolling audits" are the same answer for large sites: audit a defined sample now and the rest on a schedule (index, as above). perqo.com is small enough for a full inventory, and the deliverable is one.

### 1.2 · What to record per item

The fields below are the union of Kaley's list (title, URL, owner, topic, format, last-modified date, metadata, location of source files), Halvorson and Rach's quantitative fields, and the fields this course needs for the structure work that follows. The last group is the course's addition, and each field in it is tied to the unit that requires it.

| Field | Pass | Why it is recorded | Source |
|---|---|---|---|
| ID | inventory | the item's address in every later artefact; kept when the item moves | Halvorson and Rach 2012, index; IA2, section 4 |
| Title, as the page shows it | inventory | the label people meet | Kaley 2020 |
| URL | inventory | where it lives now; the redirect source if it moves | Kaley 2020; Halvorson and Rach 2012, index |
| Format | inventory | page or file (IA2's `file` tag) | Kaley 2020 |
| Last modified | inventory | how stale it is | Kaley 2020; Halvorson and Rach 2012, index |
| Traffic | inventory | which items matter first when time is short | Halvorson and Rach 2012, index; Kaley 2020 (scope) |
| Owner | inventory | who updates it, and who is asked | Kaley 2020 |
| Audience | audit | whom it is written for | Halvorson and Rach 2012, index ("target audience") |
| Audit outcome and reason | audit | keep, update, remove, new | Kaley 2020; this unit (new) |
| Page type | structure | its place in the hierarchy: IA2's tags | IA2, section 5.2 |
| Template | structure | which layout of modules builds it (section 3) | this unit |
| F-CAT tags | structure | which benefit categories it is about | IA4, Deliverable B |
| Redirect to | structure | where its old URL points when it moves or goes | IA4, section 5 |
| Indexed | structure | whether search engines may list it (section 5.1) | Google documentation, section 5.1 |

```viz
{"kind": "matrix", "caption": "Inventory structure: the fields of one inventory row, grouped by the pass that fills each, with the status a field takes at F2 (the audit before redesign) and F3 (the migration list); supports the decision on which columns a perqo.com inventory carries (section 1.2). Fields from Kaley, 'Content Inventory and Auditing 101', NN/g, 2020; Halvorson and Rach, Content Strategy for the Web, 2nd ed., 2012, index to ch. 5; the structure fields from IA2, section 5.2, IA4, Deliverable B and section 5, and this unit. Every row is tone 1, perqo.com, the one surface inventoried. Perqo is fictional.", "cols": ["Pass", "F2 audit", "F3 migration"], "rows": [
 {"label": "ID", "tone": 1, "cells": ["inventory", "record", "stable"]},
 {"label": "Title", "tone": 1, "cells": ["inventory", "record", "final label"]},
 {"label": "URL", "tone": 1, "cells": ["inventory", "record", "final address"]},
 {"label": "Format", "tone": 1, "cells": ["inventory", "record", "record"]},
 {"label": "Last modified", "tone": 1, "cells": ["inventory", "record", null]},
 {"label": "Traffic", "tone": 1, "cells": ["inventory", "record", null]},
 {"label": "Owner", "tone": 1, "cells": ["inventory", "record", "named"]},
 {"label": "Audience", "tone": 1, "cells": ["audit", "judge", "record"]},
 {"label": "Audit outcome", "tone": 1, "cells": ["audit", "keep, update, remove", "plus new"]},
 {"label": "Page type", "tone": 1, "cells": ["structure", null, "tag"]},
 {"label": "Template", "tone": 1, "cells": ["structure", null, "T-ID"]},
 {"label": "F-CAT tags", "tone": 1, "cells": ["structure", null, "CAT-ID"]},
 {"label": "Redirect to", "tone": 1, "cells": ["structure", null, "ID"]},
 {"label": "Indexed", "tone": 1, "cells": ["structure", null, "yes or no"]}]}
```

The fidelity decides which fields are filled. At F2, before the redesign, the inventory and audit fields are recorded and the audience is judged; the structure fields stay empty, because no structure has been chosen yet. At F3, the migration list, the ID is stable, the title and URL are the final ones, the owner is named, the outcome may also be new, and the structure fields carry a page-type tag, a template ID, CAT identifiers, a redirect target's ID and yes or no for indexing; format and audience are carried over as recorded; traffic and last-modified dates are dropped, because the migration needs neither.

Two things follow for the reader of someone else's inventory. An inventory without an owner column cannot be acted on, because every update needs a person (Kaley 2020). And an inventory sorted by URL reads as a sitemap and carries today's structure into tomorrow's without anyone deciding to (IA2, section 1.1); the structure fields are filled after the structure is chosen, never copied from the URLs.

### 1.3 · What the perqo.com audit found

Deliverable A is the full inventory. Read as an audit, it shows four kinds of finding, each a pattern a reader can look for in any marketing site's inventory (Perqo, fictional):

- **Vocabulary drift.** The Perqo app product page (S-1.2) calls the allocation "allowance", a variant term; perqo.com's preferred term is Benefits budget (IA1, Deliverable). "Why was my claim rejected?" (H-2.1.2) says "refund" where the app says Claim (IA2, section 5.3). Both fail IA3's D2.
- **Duplicates and orphans.** A Features page (S-1.6) and a PDF brochure (S-1.7) repeat the three product pages in older words. A campaign page from an ended campaign (L-02) is still live.
- **Facts out of date.** A customer story (S-3.4) is about a company that is no longer a Perqo client; a customer story is about a client (IA4, Deliverable A, R-19).
- **Gaps.** The Help centre has no article on the card and none on what each category covers, though the search log's top queries include "gym" with zero results (IA3, section 5.2); there is no buyer page for the benefit categories at all.

## 2 · Audience, task or topic: three structures for a B2B software site

IA4 catalogued the schemes and the criteria for choosing one (IA4, sections 1.1 and 1.2). A marketing site's top level is usually built on one of three ambiguous schemes: by audience, by task or by topic. Each has a case on a B2B software site, and each has evidence against it.

### 2.1 · Audience-based

The structure asks the visitor who they are: For HR teams, For finance teams, For employees, For merchants. Before choosing a page, the visitor must pick a role. Its case on a B2B site is that buyers in different roles want different arguments: at Perqo, a buyer is "typically someone in HR or finance" (IA1, section 5), and finance cares about budgets and reports where HR cares about policies and approvals.

The evidence against it is direct. Katie Sherwin's NN/g article gives five problems: "people don't always fall neatly into a single category, nor are they able to quickly self-identify"; a bare group label such as "Faculty" does not say whether the content is about the group or for it (she notes that adding "for" clarifies it); self-identifying adds a step and pulls people out of their task; people worry that "the information they see might be incomplete or incorrect", wondering whether another group gets a better offer; and content that applies to several groups is either duplicated or linked from several places, leaving people to check whether the versions differ ("Audience-Based Navigation: 5 Reasons to Avoid It", Nielsen Norman Group, 7 September 2015, [nngroup.com/articles/audience-based-navigation](https://www.nngroup.com/articles/audience-based-navigation/)). Its labels name a role and leave the content behind them unsaid, which fails IA3's A1. Her recommendation, NN/g guidance: "Only use audience-based navigation when the content truly justifies it", that is, when the content is unique to the group, the groups are mutually exclusive and named in plain words, and preferably as secondary navigation (Sherwin 2015). GOV.UK's team reported the same from its own research: users did not map neatly onto groups, a label such as "professionals" was read in more than one way, and people skipped content they needed because it was labelled for someone else; it settled on labels that describe a topic's content (Cath Richardson, "'Hey, you there': the trouble with audience-based navigation", Inside GOV.UK blog, 18 July 2014, [insidegovuk.blog.gov.uk](https://insidegovuk.blog.gov.uk/2014/07/18/hey-you-there-the-trouble-with-audience-based-navigation/); a government team's account of qualitative research, practice).

On perqo.com the duplication problem is concrete, and it is the comparison's deciding row below. Pricing and the customer stories matter to both HR and finance buyers, so an audience top level would carry them twice, and IA1's buyer is one person who may be in either role.

### 2.2 · Task-based

The structure names what the visitor came to do: See how it works, Check the price, Read customer stories, Get help, Book a demo. The visitor reads a phrase and matches it to their need. Its case comes from top-tasks practice. Gerry McGovern defines top tasks as "the small set of tasks (usually less than 10, often less than five) that matter most to your customers", found by gathering a long list, shortlisting it with stakeholders, and asking customers to vote; in his Cisco example "three tasks got as much of the vote as the bottom 44", and he reports the same concentration in every one of the 400-plus such projects he has run ("What Really Matters: Focusing on Top Tasks", A List Apart, April 2015, republished by Center Centre, 20 January 2016, [articles.centercentre.com](https://articles.centercentre.com/?p=877); practice, a consultant's own data). The European Commission's web guide states the institutional version: it adopted a task-based architecture in 2014, arguing that it "avoids making users think" and avoids "content duplication and unnecessary maintenance costs" (European Commission, "Reasons for building a task-based information architecture", Europa Web Guide, undated, [commission.europa.eu](https://commission.europa.eu/resources-partners/europa-web-guide/planning-your-web-presence/architecture-and-navigation/task-based-information-architecture_en); institutional guidance).

The case against it on a sales site is in the labels. A buyer's tasks are few and close together (understand, compare, trust, contact), so task labels tend to start with verbs of the same kind, and IA3 found conversational "I want to…" and call-to-action labels among the low-scent faults (Laubheimer, "3 Common IA Mistakes", NN/g, 2023; IA3, section 1.2). "See how it works" and "Check the price" start with words that do not tell them apart, which fails IA3's A2 (Nielsen, "First 2 Words", NN/g, 2009; IA3, section 1.2). Two of the tasks, booking a demo and signing in, are single actions, and they work well as task labels because each is one destination.

### 2.3 · Topic-based

The structure names the subjects a buyer asks about: Product, Pricing, Customers, Help centre, with Book a demo and Sign in beside them. The visitor picks a subject. Its case on a B2B software site is that a buyer researching a product moves between a small number of subjects that every product in the category shares, and arrives at each from search with a subject in mind (section 4.2). Its risk is the one IA3 named for every topic label: internal or branded words that a newcomer does not know (Nielsen, "Use Old Words When Writing for Findability", NN/g, 2006; Farrell, "Search-Log Analysis", NN/g, 2017; IA3, section 4.2). A topic called "Features" or named after an internal product line has that fault; "Pricing" and "Customers" do not.

```viz
{"kind": "matrix", "caption": "Three candidate structures for perqo.com's top level compared; supports the decision on which scheme the top level uses (section 2). Audience-based problems from Sherwin, 'Audience-Based Navigation: 5 Reasons to Avoid It', NN/g, 2015, and Richardson, Inside GOV.UK, 2014; task-based case from McGovern, 'What Really Matters', 2015 (practice); label tests from IA3's checklist, A1 and A2 (Nielsen, 'First 2 Words', NN/g, 2009). Rows tone 1, perqo.com; tone 6 marks a fault found in this comparison. Perqo is fictional.", "cols": ["Audience", "Task", "Topic"], "rows": [
 {"label": "Top level", "tone": 1, "cells": ["For HR teams, For finance teams, For employees, For merchants", "See how it works, Check the price, Read customer stories, Get help, Book a demo", "Product, Pricing, Customers, Help centre, Book a demo, Sign in"]},
 {"label": "Visitor must first", "tone": 1, "cells": [{"mark": "pick a role", "tone": 6}, "read a phrase", "pick a subject"]},
 {"label": "Pricing and stories", "tone": 1, "cells": [{"mark": "repeated under HR and finance", "tone": 6}, "one place each", "one place each"]},
 {"label": "Label scent (A1, A2)", "tone": 1, "cells": [{"mark": "names a role", "tone": 6}, {"mark": "verbs first: weak first words", "tone": 6}, "names content"]},
 {"label": "Used on perqo.com for", "tone": 1, "cells": ["Help centre, For merchants", "Book a demo, Sign in", "the top level"]}]}
```

### 2.4 · The choice for perqo.com

IA4 separated a hybrid that mixes schemes in one list, which fails C1, from schemes layered by level, each level of one kind, which passes (IA4, section 1.1). perqo.com uses the layered form (Perqo, fictional):

- **The top level is by topic**: Product, Pricing, Customers, Help centre, the areas IA1 set (IA1, Deliverable).
- **Two utility routes are by task**: Book a demo and Sign in, which IA2 added to the global routes and IA1 placed (IA2, section 5.3). Each is a single destination, so its label is the action and passes A1.
- **Audience is used only where the content is unique to one audience**, which is Sherwin's condition: inside the Help centre, where IA1 split For HR and finance teams from For employees (IA1, section 2.3), and on one footer page, For merchants (section 2.5).

That keeps IA1's top-level areas exactly as set. The top level is one kind of thing (C1); the task routes sit apart from it in the header, as IA2's navigation model already drew them (IA2, section 5.3).

### 2.5 · The one audience page outside the Help centre

The merchant side exists, and IA3 and IA4 gave it its first facts: merchants accept the Perqo card and can publish offers (IA3, Deliverable; IA4, Deliverable A). A merchant has questions no buyer, HR manager or employee has: how to accept the card, how to publish an offer. The content is unique to the group and the group knows itself, which meets Sherwin's condition, so perqo.com has one page, For merchants (Perqo, fictional), owned by the partnerships team and reached from the footer. Its label passes the test GOV.UK's research failed for "professionals" (Richardson 2014): nobody who is not a merchant reads "For merchants" as theirs.

## 3 · Page types, pages and templates

### 3.1 · Page types versus pages

IA2 set the rule that a structural sitemap's box is a page type or a group, with many pages of one type drawn as one stack, after Brown's note that site maps "increasingly represent page types or templates in addition to (or instead of) specific pages" (Brown, *Communicating Design*, 2nd ed., 2011, ch. 5; Garrett's page stack, *Quick Reference*; IA2, section 1.3). The inventory is the other side of that rule: it lists pages, one row each, and the sitemap draws types. The two meet in one column, the page type, which IA2 fixed as a closed list of tags: `home`, `section`, `index`, `detail`, `stack`, `form`, `file`, `external` (IA2, section 5.2).

A page type says where a page sits and what it does in the structure: a section page lands a group, an index lists items, a detail page is one item. It does not say what is on the page. Two detail pages, the Perqo card product page and a help article, share a tag and share almost nothing else.

### 3.2 · Templates as the unit of IA on a site

A template is the layout of modules that builds every page of one kind. Brad Frost's *Atomic Design* draws the distinction a team needs: templates are "page-level documents" that focus on content structure, and pages are "specific instances of a template" that replace that structure "with real representative content" (Brad Frost, *Atomic Design*, 2016, ch. 2, "Atomic Design Methodology"; outline at [atomicdesign.bradfrost.com](https://atomicdesign.bradfrost.com/outline)). The Polar Bear book covers the content-side artefact, content models, for "connecting and managing granular content" (Rosenfeld, Morville and Arango, 4th ed., 2015, ch. 13; IA2, section 1.5).

On this unit's reading, the template is where most IA decisions on a website take effect, for four reasons. Each module a template requires is a decision of one of the four systems, made once and repeated on every page built from it:

- **Organisation.** A template fixes which metadata fields a page carries. If the help-article template has an F-CAT field, every article is classified; if it does not, none is, whatever the taxonomy says.
- **Labelling.** A template fixes which headings and fixed labels appear. The page heading that must confirm the link that led to it (IA3, A3; Budiu, NN/g, 2020) is a template rule.
- **Navigation.** A template fixes the routes: whether a page carries the global header, a breadcrumb, related articles. Contextual navigation on a site is mostly template modules filled from metadata, the "Related Link" lists Cardello says IA metadata can generate (Cardello, NN/g, 2014; IA2, section 1.3).
- **Search.** A template fixes what is indexed and what a result shows.

That is why the template catalogue is a deliverable of its own, with a different reader from the sitemap: engineering builds templates, and content fills pages. A site of 52 inventory rows and 17 templates (Deliverables A and C) has 17 places where a structural decision is built, and up to 52 where it is repeated.

### 3.3 · Templates and IA4's objects

IA4's object map gave perqo.com four objects: the help article, the customer story, the demo request and, through customer stories, the client (IA4, Deliverable A, O-14 to O-16 and O-01). The template catalogue follows them. Each object that has many instances gets a detail template whose required modules are the object's attributes: the help-article template (T-16) shows the article's audience and its last-modified date, two of O-14's attributes (IA4, Deliverable A.1), and the F-CAT tags IA4 asked IA5 to give every article (IA4, Deliverable B); the customer-story template (T-08) carries the client it is about (R-19) and, new here, F-CAT tags, so the Customers index can be filtered by category. The demo request is a form (T-09) whose fields are O-16's attributes: name, work email, company, number of employees. No object is renamed: the labels on perqo.com are IA1's perqo.com column (Benefits budget, Card payments, Claims, Policies, Teams and groups) and IA4's (Customers, Perqo card, Book a demo). The benefit categories stay taxonomy terms, as IA4 required (IA4, section 4.3): they appear on perqo.com as pages built from one template, T-04, each bound to its F-CAT identifier, and never as an object.

## 4 · Depth, breadth, and the home-page and landing-page problem

### 4.1 · Depth and breadth on a marketing site

IA4 set out the evidence: deeper link hierarchies took longer in Zaphiris's five structures over 64 pages and in Larson and Czerwinski's over 512 documents, a medium breadth beat the broadest shallow structure, and no study supports a fixed number of items per level (IA4, section 2.1). Applied to perqo.com, the evidence says little the site needs: its deepest path is four levels below Home (Home, Help centre, For employees, Claims, an article), and every buyer page is within three. The decisions it does bear on are two. The four benefit categories go one level below a Benefits page under Product, which keeps Product's own list at five short items, where flat lists "tend to work well if you have distinct, recognizable categories" (Whitenton, NN/g, 2013; IA4, section 2.1). And the Help centre keeps IA1's two levels, audience then task, above its articles, and adds no third grouping level, because each added level is one more choice that must carry scent (IA3, section 6.2).

### 4.2 · The home-page problem

Steve Krug gives the home page a chapter of its own, "The Big Bang Theory of Web Design", and treats it as the page that has to tell a first-time visitor what the site is and what it is for (*Don't Make Me Think, Revisited*, 3rd ed., New Riders, 2014, ch. 7; practice). The structural problem it creates is the one IA3 called internal politics: a structure decides which teams and offers are visible (Rosenfeld, Morville and Arango 2015, ch. 6; IA3, section 3.2), and the home page is the most visible place on the site. On perqo.com, marketing wants the campaign, partnerships want the merchant offers, support wants the Help centre and sales wants Book a demo (Perqo, fictional; the partnerships team's request for placings is IA3's, Deliverable).

The structural answer is to give the home page a template with fixed slots, each tied to a route the sitemap already holds, so a request for home-page space becomes a request for a module in a slot. The home template (T-01) requires one statement of what Perqo is and whom it is for, the three surfaces, the four categories and the Book a demo route; a campaign gets an optional slot that links to its landing page and is removed when the campaign ends. The audit finding on the current home page (S-0) is that its opening line says neither what Perqo is nor who buys it, so it gets an update.

### 4.3 · The landing-page problem

Most visitors to a marketing site do not start at Home. Mark Baker's book on topic-based writing puts it in one line: "People don't arrive at your site, they arrive at your pages" (*Every Page Is Page One: Topic-Based Writing for Technical Communication and the Web*, XML Press, 2013; the line from the book's site, [everypageispageone.com](https://everypageispageone.com/the-book); practice). Jakob Nielsen's foraging account adds the mechanism: each site is a patch, and people leave it when the scent falls (Nielsen, NN/g, 2003; IA3, section 1.1).

So every page on perqo.com is a landing page for someone, and every template has to do part of the home page's job. The catalogue enforces three modules on every template a visitor can arrive at from outside: the global header, which shows the site's top level and its two task routes; a page heading that says what the page is in the visitor's words (IA3, A1 and A3); and, on every indexed page except Home and the Help centre's home, a breadcrumb, which shows where the page sits. A help article reached from a search engine therefore tells an employee it is in the Help centre, under For employees, under Claims, before they read a word of it.

## 5 · What other functions bring, and how the sitemap records it

A sitemap drawn only from the content and the users will be overruled by constraints it did not record. Five come from other functions on a sales site. For each: what the constraint is, the source that sets it, and where the sitemap or the inventory records it.

### 5.1 · Search-engine structure

Google's documentation for site owners asks for URLs that use "readable words rather than long ID numbers", hyphens between words, and "words in your audience's language", with unnecessary parameters trimmed ("URL Structure Best Practices for Google Search", Google Search Central, page updated 21 October 2026, [developers.google.com](https://developers.google.com/search/docs/crawling-indexing/url-structure); vendor documentation, checked 3 November 2026). When a page's URL changes, it recommends "a permanent server-side redirect whenever possible", which the indexing pipeline uses "as a signal that the redirect target should be canonical" ("Redirects and Google Search", page updated 14 April 2026, [developers.google.com](https://developers.google.com/search/docs/crawling-indexing/301-redirects); vendor documentation). A page marked `noindex` is dropped "entirely from Google Search results, regardless of whether other sites link to it" ("Block Search Indexing with noindex", page updated 10 December 2025, [developers.google.com](https://developers.google.com/search/docs/crawling-indexing/block-indexing); vendor documentation). Berners-Lee's older rule sits under all three: "Cool URIs don't change", and a topic name in a URI binds it to a classification (W3C, 1998; IA4, section 5).

IA4 set the Perqo rule that meets these: catalogue pages and filters address values by stable identifier, and a renamed or moved Help centre page keeps a redirect from its old address (IA4, section 5). On perqo.com the two requirements meet in the benefit-category pages. Google asks for readable words; IA4 asks that a category be addressed by its identifier so a rename breaks no link. The category page's URL carries both, the identifier first and the preferred term after it: perqo.com/product/benefits/cat-hea/health (Perqo, fictional). The identifier decides which page opens; if the term is renamed under IA4's R9, the old address redirects to the new one, and the identifier never changes.

How the artefacts record it: the inventory carries URL, Redirect to and Indexed for every row (section 1.2); the sitemap at F3 carries each box's ID, and the ID carries the URL in the inventory. The XML file the Sitemaps protocol describes, which shares only the name with this artefact (IA2, section 1.3), is generated from the inventory's indexed rows, so engineering never maintains a second list.

### 5.2 · Campaign landing pages

Marketing runs campaigns, and a campaign wants its own page: one message, one call to action, reached from an advert or an email. The structural risk is that each campaign leaves a page behind, and the audit found one (L-02). The Perqo rule (Perqo, fictional): a campaign page lives under perqo.com/lp/, is `noindex`, appears in no navigation, uses the campaign template (T-12), and carries an owner and an end date in the inventory; at the end date it is removed and its address redirects to the page that answers the same question. It keeps the global header, because a visitor from an advert has arrived at one page with no view of the rest of the site (Baker 2013).

The sitemap records campaign pages as a conditional stack, IA2's conditional area: one box tagged `stack` whose note opens with the condition in square brackets, "[campaign live]" (IA2, section 5.1). The decision whether a request becomes a campaign page, a new page in the sitemap or an addition to a page that exists is a rule, so it is drawn as a decision tree. First: will the page outlive one campaign? If not, it is a campaign page under /lp/, noindex, in no navigation, with an owner and an end date. If it will: does it answer a question no live page answers? If not, it is added to the page that answers it, which is how the audit's duplicates (section 1.3) are avoided. If it does: is its content unique to one audience? If so, it is an audience page, from the footer or inside the Help centre (section 2.1's condition); if not, it is a new page under its topic, with an ID and a template.

```viz
{"kind": "decision", "caption": "Decision tree: where a request for a new perqo.com page goes; supports the decision on whether a page enters the sitemap (section 5.2). Questions and outcomes tone 1, perqo.com. Campaign rule from this section; the audience condition from Sherwin, NN/g, 2015 (section 2.1); the merge rule from the audit's duplicates (section 1.3). Perqo is fictional.", "root": {"q": "Will the page outlive one campaign?", "tone": 1, "branches": [
 {"label": "yes", "to": {"q": "Does it answer a question no live page answers?", "tone": 1, "branches": [
  {"label": "yes", "to": {"q": "Is its content unique to one audience?", "tone": 1, "branches": [
   {"label": "yes", "to": {"outcome": "Audience page, from the footer or inside the Help centre", "tone": 1}},
   {"label": "no", "to": {"outcome": "New page under its topic, with an ID and a template", "tone": 1}}]}},
  {"label": "no", "to": {"outcome": "Add it to the page that answers it", "tone": 1}}]}},
 {"label": "no", "to": {"outcome": "Campaign page under /lp/: noindex, no navigation, owner and end date", "tone": 1}}]}}
```

### 5.3 · Localisation

perqo.com is published in one language today, English (Perqo, fictional); which markets come next is DD-IA3's to set. The constraint a sitemap has to anticipate now is the one Google's documentation sets for localised versions: each version "must list itself as well as all other language versions", and "If two pages don't both point to each other, the tags will be ignored"; an `x-default` value names the page for visitors no version matches ("Localized Versions of your Pages", Google Search Central, page updated 21 September 2026, [developers.google.com](https://developers.google.com/search/docs/specialty/international/localized-versions); vendor documentation, checked 3 November 2026). The URL documentation gives a country subdirectory, example.com/de/, as one structure for a multi-regional site (Google, "URL Structure Best Practices", 2026).

Every version of a page must point to every other, so the site needs one key that is the same in every language. The inventory's ID is that key: S-1.4.2 is the Learning page in every language, whatever its title and its slug become. Two rules follow, and the deliverables apply them. Identifiers carry no words of any language. And the template catalogue marks the modules whose content differs by market as well as by language (prices, legal text, app-store links), because those are the modules a translator cannot fill (Deliverable C, the localisation column). DD-IA3 takes both.

### 5.4 · The pricing page

A sales team may prefer to keep prices off the site and route buyers to a call. The NN/g evidence is against it. Hoa Loranger reports that business customers name pricing as the information they most need online and that "In our studies, we watch participants go to competitors' sites when websites do not show prices"; where exact prices are hard to show she recommends sample prices, typical scenarios or ranges ("State the Price to Give B2B Sites a Competitive Advantage", Nielsen Norman Group, 1 December 2013, [nngroup.com/articles/show-price](https://www.nngroup.com/articles/show-price/)). Therese Fessenden's recommendation is "Show the price; and if the price is variable, offer common pricing scenarios", adding that "the first site to show a price can anchor users' expectations" ("What B2B Designers Can Learn from B2C About Building Trust", Nielsen Norman Group, 1 September 2019, [nngroup.com/articles/b2b-trust-from-b2c](https://www.nngroup.com/articles/b2b-trust-from-b2c/)). Loranger's article reports observations from NN/g's usability studies without figures; both are NN/g guidance built on observation.

The audit found the current Pricing page (S-2) saying "Contact us for pricing" (Perqo, fictional). The structural decision is that Pricing stays a level-1 page in the global header, as IA1 set it, never behind the demo form, and its template (T-05) requires a plan comparison and a worked pricing scenario. Perqo has two plans, each with a published price per employee per month (Perqo, fictional; the plan names and the amounts are left free). The sitemap records the decision by where Pricing sits; the template records it by its required modules.

### 5.5 · The sign-up and log-in boundary

Where a product lets visitors sign up on the website, the website's last page and the product's first screen meet in the middle of a flow, and the sitemap has to show who owns each side. Perqo has no self-serve sign-up and no free trial (Perqo, fictional): a client starts after a contract, which IA1 drew as the line from perqo.com to Admin (IA1, Deliverable). Three routes cross the boundary. The one that leaves the site, Sign in, is drawn with IA2's `external` tag and a "→ see" note (IA2, section 5.2); the other two stay on perqo.com and are drawn as its pages:

- **Book a demo**, the conversion route, stays on perqo.com: a form (S-4) and a confirmation page (S-4.1). The demo request goes to sales and does not reach Admin (IA4, Deliverable A, O-16). Fessenden's advice applies to the form: say why each field is asked, because people trust a request that comes with a reason (Fessenden 2019). The template (T-09) requires a reason line.
- **Sign in** leaves for Perqo Admin, for HR and finance managers (IA1, section 5; IA2, section 5.3).
- **Get the Perqo app** (S-6) gives employees the download links, which IA1 listed among what crosses from perqo.com to the app (IA1, Deliverable). Employees do not sign in on perqo.com; they join from the invitation HR sends from Admin (IA1, Deliverable).

One assumption sits on this boundary (Perqo, fictional; assumed): an employee who wants the app may press Sign in and land on Admin's sign-in screen. Whether they do is testable from Admin's failed sign-ins and from the Help centre's search log (IA3, section 5.2); until it is tested, the fix belongs to Admin's surface, a line on its sign-in screen pointing employees to Get the Perqo app, and is passed to IA7 as proposed. (Note, 3 November 2026: IA7 takes the proposal with one change, in its Deliverable C, C.5: Admin's Sign in (AD-0) carries the line "Looking for your benefits? Get the Perqo app", linking to S-6, for everyone from the first view; the assumption itself stays untested.)

## 6 · How the sitemap is read, and the fidelity each reader needs

IA1 set the rule that every deliverable names its readers and the decision it supports; IA2 set three fidelities, F1 sketch, F2 working and F3 specification, and gave the sitemap F1 in discovery (top two levels), F2 in design (every group and page type) and F3 for build (identifiers) (IA1, section 4; IA2, sections 1.0 and 1.3). On a sales site the three readers who use the sitemap most are marketing, engineering and the content writer. They read the same drawing for different things, and each needs a different fidelity.

**Marketing** reads the sitemap for what a buyer sees and where the conversion routes sit: the top level and its labels, the place of Pricing, Customers and Book a demo, and where campaigns go. F1 or F2 is enough; marketing argues about the top two levels, and the page-by-page detail would hide the argument. What it also needs is the label table (B.2), because the labels are what it argues about. Tankala's point that a sitemap leaves detail out on purpose so the discussion stays manageable fits this reader (Tankala, NN/g, 2023; IA1, section 4).

**Engineering** reads it for what to build and route: every box's ID, page type and template, the URLs, the redirects, which pages are indexed, and every `external` box, because each one is a hand-off to another system. Only F3 serves, and the drawing is never enough alone: the inventory carries the URL, redirect and index columns the drawing has no room for. A box without an ID cannot be cited in a ticket (IA2, section 4).

**The content writer** reads it for where a piece goes and what surrounds it: the page's parent (which sets its breadcrumb and its context), its template (which sets the modules to fill), its owner and audience, its F-CAT tags, and the word the site uses for each thing (IA1, Deliverable, the perqo.com column). F2 is the drawing's level; the writer's real document is the inventory row plus the template entry.

```viz
{"kind": "matrix", "caption": "Readers of the perqo.com sitemap: what each reads for, the fidelity each needs, and the artefact that carries what the drawing cannot; supports the decision on which version of the sitemap goes to whom (section 6). Fidelities from IA2, sections 1.0 and 1.3; detail left out on purpose from Tankala, NN/g, 2023. Every row tone 1, perqo.com. Perqo is fictional.", "cols": ["Reads for", "Fidelity", "Also needs"], "rows": [
 {"label": "Marketing", "tone": 1, "cells": ["top level, labels, Pricing, Customers, Book a demo, campaigns", "F1 or F2", "the label table (B.2)"]},
 {"label": "Engineering", "tone": 1, "cells": ["IDs, page types, templates, external boxes", "F3", "inventory: URL, redirect, indexed"]},
 {"label": "Content writer", "tone": 1, "cells": ["parent, template, owner, audience, F-CAT tags, site's words", "F2", "inventory row and template entry"]}]}
```

Brown's phrase for a sitemap is "one view" (Brown 2011, ch. 5). On a sales site the useful consequence is that the team ships one sitemap at three fidelities from one source: the F3 drawing with its IDs is the source, and the F1 or F2 version for marketing is the same drawing cut to two levels, so the three readers never argue from three different maps.

## Deliverable · A · The perqo.com content inventory

*Face of this artefact (IA2, the notation sheet): content inventory and audit of perqo.com, every page and file, at fidelity F3 as the migration list (IA2, Deliverable: F2 before redesign, F3 as the migration list); decision: what the redesigned site keeps, changes, removes and adds, and where each removed address points; readers: content and support (owners), engineering (IDs, URLs, redirects, indexing), marketing, product management; leaves out: traffic and last-modified dates (recorded in the working spreadsheet, not set for the course), page copy, Perqo Admin and the Perqo app; owner: the IA designer with marketing; version 1, dated 3 November 2026; Perqo is fictional.*

Every page and owner below is invented for the running example (Perqo, fictional); rows marked "(IA2)" or "(IA3)" keep facts set there. Status is the audit outcome (Kaley 2020), with *new* for pages the gap analysis adds (section 1.1). Audience: Buyer (a buyer at a prospective client, IA1, section 5), HR and finance (managers at a client), Employee, Merchant, Everyone. F-CAT gives the benefit-category identifiers a page is about (IA4, Deliverable B); "all" means all four top-level values; a dash means none. Indexed is yes unless the row says no. Removed rows redirect to the ID given.

### A.1 · Site pages

| ID | Page | URL (perqo.com) | Type | Template | Audience | Owner | F-CAT | Status |
|---|---|---|---|---|---|---|---|---|
| S-0 | Home | / | home | T-01 | Buyer | Marketing | all | update: opening line says neither what Perqo is nor who buys it |
| S-1 | Product | /product | section | T-02 | Buyer | Marketing | – | update: add Benefits and Security to its list |
| S-1.1 | Perqo Admin | /product/admin | detail | T-03 | Buyer | Marketing | – | keep |
| S-1.2 | Perqo app | /product/app | detail | T-03 | Buyer | Marketing | – | update: says "allowance"; the site's term is Benefits budget |
| S-1.3 | Perqo card | /product/card | detail | T-03 | Buyer | Marketing | – | keep |
| S-1.4 | Benefits | /product/benefits | section | T-02 | Buyer | Content team | all | new |
| S-1.4.1 | Health | /product/benefits/cat-hea/health | detail | T-04 | Buyer | Content team | CAT-HEA | new |
| S-1.4.2 | Learning | /product/benefits/cat-lea/learning | detail | T-04 | Buyer | Content team | CAT-LEA | new |
| S-1.4.3 | Mobility | /product/benefits/cat-mob/mobility | detail | T-04 | Buyer | Content team | CAT-MOB | new |
| S-1.4.4 | Meals | /product/benefits/cat-mea/meals | detail | T-04 | Buyer | Content team | CAT-MEA | new |
| S-1.5 | Security | /product/security | detail | T-06 | Buyer | Product | – | keep |
| S-1.6 | Features | /features | detail | none | Buyer | Marketing | – | remove: repeats S-1.1 to S-1.3; redirect to S-1 |
| S-1.7 | Perqo brochure | /files/perqo-brochure.pdf | file | none | Buyer | Marketing | – | remove: out of date, content in S-1.1 to S-1.3; redirect to S-1 |
| S-2 | Pricing | /pricing | detail | T-05 | Buyer | Marketing, with Sales | – | update: says "Contact us for pricing"; show both plans' prices and a worked scenario |
| S-3 | Customers | /customers | index | T-07 | Buyer | Marketing | – | keep |
| S-3.1 | Customer story: a software consultancy | /customers/software-consultancy | detail | T-08 | Buyer | Marketing | CAT-LEA | keep |
| S-3.2 | Customer story: a logistics group | /customers/logistics-group | detail | T-08 | Buyer | Marketing | CAT-MOB | keep |
| S-3.3 | Customer story: a design studio | /customers/design-studio | detail | T-08 | Buyer | Marketing | CAT-HEA | update: ends with no Book a demo route |
| S-3.4 | Customer story: a retail chain | /customers/retail-chain | detail | T-08 | Buyer | Marketing | CAT-MEA | remove: no longer a Perqo client; redirect to S-3 |
| S-4 | Book a demo | /demo | form | T-09 | Buyer | Sales | – | update: drop the phone field sales does not use; add the reason line |
| S-4.1 | Demo request received | /demo/thanks | detail | T-10 | Buyer | Sales | – | keep; indexed: no |
| S-5 | Sign in | leaves for Perqo Admin | external | none | HR and finance | Product | – | keep |
| S-6 | Get the Perqo app | /app | detail | T-06 | Employee | Support | – | keep |
| S-7 | For merchants | /merchants | detail | T-06 | Merchant | Partnerships | – | keep |
| S-8 | About Perqo | /about | detail | T-06 | Buyer | Marketing | – | keep |
| S-9 | Contact | /contact | form | T-09 | Everyone | Marketing | – | keep |
| S-10 | Privacy policy | /privacy | detail | T-11 | Everyone | Legal | – | keep |
| S-11 | Terms of service | /terms | detail | T-11 | Everyone | Legal | – | keep |
| S-12 | Cookie policy | /cookies | detail | T-11 | Everyone | Legal | – | keep |

### A.2 · Campaign pages

| ID | Page | URL (perqo.com) | Type | Template | Audience | Owner | F-CAT | Status |
|---|---|---|---|---|---|---|---|---|
| L-01 | Learning budgets for engineering teams | /lp/learning-budgets | detail | T-12 | Buyer | Marketing | CAT-LEA | keep until the campaign's end date, then redirect to S-1.4.2; indexed: no |
| L-02 | Benefits for hybrid teams | /lp/hybrid-teams | detail | T-12 | Buyer | Marketing | all | remove: campaign ended; redirect to S-1.4; indexed: no |

### A.3 · Help centre

| ID | Page | URL (perqo.com/help) | Type | Template | Audience | Owner | F-CAT | Status |
|---|---|---|---|---|---|---|---|---|
| H-0 | Help centre | / | index | T-13 | HR and finance; Employee | Support | – | keep |
| H-0.1 | Search results | /search | index | T-14 | HR and finance; Employee | Support | – | update: map IA4's variant terms as synonyms (IA3, D3); indexed: no |
| H-1 | For HR and finance teams | /hr-finance | section | T-15 | HR and finance | Support | – | keep |
| H-1.1 | Budgets | /hr-finance/budgets | section | T-15 | HR and finance | Support | all | keep |
| H-1.1.1 | Setting a budget for an employee group (IA2) | /hr-finance/budgets/set-a-budget | detail | T-16 | HR and finance | Support | all | keep |
| H-1.1.2 | Budget periods explained | /hr-finance/budgets/budget-periods | detail | T-16 | HR and finance | Support | all | keep |
| H-1.2 | Policies | /hr-finance/policies | section | T-15 | HR and finance | Support | all | keep |
| H-1.2.1 | Creating an employee group and its policy | /hr-finance/policies/create-a-group | detail | T-16 | HR and finance | Support | – | keep |
| H-1.2.2 | Choosing which categories are open | /hr-finance/policies/open-categories | detail | T-16 | HR and finance | Support | all | keep |
| H-1.2.3 | Setting the auto-approve limit | /hr-finance/policies/auto-approve-limit | detail | T-16 | HR and finance | Support | – | keep |
| H-1.2.4 | Approval rules (IA2) | /hr-finance/policies/approval-rules.pdf | file | none | HR and finance | Product | – | remove: replaced by H-1.2.5; redirect to H-1.2.5 |
| H-1.2.5 | How approval rules work | /hr-finance/policies/how-approval-rules-work | detail | T-16 | HR and finance; Employee | Support | – | new; also listed under H-2.1 |
| H-1.3 | Approvals | /hr-finance/approvals | section | T-15 | HR and finance | Support | – | new |
| H-1.3.1 | Approving and rejecting claims | /hr-finance/approvals/approve-or-reject | detail | T-16 | HR and finance | Support | – | new |
| H-2 | For employees | /employees | section | T-15 | Employee | Support | – | keep |
| H-2.1 | Claims | /employees/claims | section | T-15 | Employee | Support | all | keep |
| H-2.1.1 | How to claim back a receipt (IA2) | /employees/claims/claim-a-receipt | detail | T-16 | Employee | Support | all | keep |
| H-2.1.2 | Why was my claim rejected? (IA2) | /employees/claims/claim-rejected | detail | T-16 | Employee | Support | – | update: says "refund"; the app says Claim |
| H-2.1.3 | What you can claim in each category | /employees/claims/what-you-can-claim | detail | T-16 | Employee | Support, with Content team | all | new: examples from the catalogue |
| H-2.1.4 | Claiming fitness: gym, classes and pool entry | /employees/claims/claiming-fitness | detail | T-16 | Employee | Support | CAT-HEA-FIT | new: answers the zero-result query "gym" (IA3) |
| H-2.2 | Balance | /employees/balance | section | T-15 | Employee | Support | all | new: takes the address H-2.2.1 held |
| H-2.2.1 | Your balance explained (IA2) | /employees/balance/your-balance-explained | detail | T-16 | Employee | Support | all | update: moves from /employees/balance; redirect kept |
| H-2.2.2 | Why can't I use money from another category? | /employees/balance/one-category | detail | T-16 | Employee | Support | all | new |
| H-2.3 | Card | /employees/card | section | T-15 | Employee | Support | – | new |
| H-2.3.1 | Freezing and unfreezing your card | /employees/card/freeze | detail | T-16 | Employee | Support | – | new |
| H-2.3.2 | Where you can pay with the Perqo card | /employees/card/where-to-pay | detail | T-16 | Employee | Support | all | new |

Two rows record a move IA4's rules govern. As the site stands, the Balance topic has one article, and the topic link opens it at the address IA2 gave it, perqo.com/help/employees/balance (IA2, section 5.3). With a second article (H-2.2.2) the topic needs its own page, so H-2.2 takes that address and H-2.2.1 moves, keeping a redirect from its old one (IA4, section 5). And H-1.2.5, which replaces IA2's PDF, is an article both audiences need, so it is listed under both, as IA4 set for such articles (IA4, section 1.2): its address stays under Policies, and the Claims section lists it, so one page has one URL and two routes.

### A.4 · The audit in numbers

| Area | Keep | Update | Remove | New | Rows |
|---|---|---|---|---|---|
| Site pages (A.1) | 15 | 6 | 3 | 5 | 29 |
| Campaign pages (A.2) | 1 | 0 | 1 | 0 | 2 |
| Help centre (A.3) | 12 | 3 | 1 | 10 | 26 |
| Total | 28 | 9 | 5 | 15 | 57 |

Of the 42 rows on the site today (pages, files and the Sign in route), 28 stay as they are, 9 change and 5 go; 15 are added, so the redesigned site has 52.

```viz
{"kind": "matrix", "numeric": true, "tone": 1, "min": 0, "max": 15, "scale_label": "pages", "caption": "Audit summary: the perqo.com inventory's rows by area and audit outcome, shaded by count; supports the decision on where the redesign's work lies (Deliverable A, A.4). Outcomes keep, update and remove from Kaley, 'Content Inventory and Auditing 101', NN/g, 2020; new added in section 1.1. Tone 1, perqo.com. Perqo is fictional; every count from the tables A.1 to A.3.", "cols": ["Keep", "Update", "Remove", "New"], "rows": [
 {"label": "Site pages", "tone": 1, "cells": [15, 6, 3, 5]},
 {"label": "Campaign pages", "tone": 1, "cells": [1, 0, 1, 0]},
 {"label": "Help centre", "tone": 1, "cells": [12, 3, 1, 10]}]}
```

**What the inventory hands on.** IA8 takes the crossing rows (S-5, the one `external` row, and S-6, whose download links leave for the app stores) as perqo.com's crossings in its surface layer; IA10 takes the owner column as the content touchpoint; DD-IA3 takes the IDs as the key every language version shares (section 5.3).

## Deliverable · B · The perqo.com sitemap

*Face of this artefact (IA2, the notation sheet): structural sitemap of perqo.com, the redesigned site, at fidelity F3, with an ID on every box and a template on every box but the external one; decision: what exists on perqo.com, under what, built from which template; readers: marketing (cut to two levels, F1 or F2), engineering (F3), content (F2), product management, sales; leaves out: removed pages (Deliverable A), URLs, redirects and indexing (Deliverable A), page content, the navigation components, Perqo Admin and the Perqo app beyond the routes into them; owner: the IA designer; version 1, dated 3 November 2026; Perqo is fictional.*

### B.1 · The sitemap

It extends IA2's F2 sitemap and keeps everything in it (IA2, section 5.3): Home over Product, Pricing, Customers, Help centre, Book a demo and Sign in; Product's three surface pages; Customers over a stack of customer stories, one page per client (IA2, section 5.3); the Help centre split by audience and then by task; Sign in leaving for Perqo Admin. It adds what this unit sets: the Benefits section with its four category pages and Security under Product; the demo confirmation; the footer pages; the Approvals and Card topics in the Help centre; search results; and campaign pages as a conditional stack. Each box's note gives its ID and template (Sign in, the external box, has no template), so engineering can cite it. Footer pages are marked "footer" in their notes: the footer is a route, outside the levels; the word extends IA2's note vocabulary under its rule "Keep the notation; extend the legend" (IA2, section 4), and the caption declares it, since the sitemap kind carries no legend of its own. The three legal pages are drawn as one stack, Legal pages, and each Help centre topic's articles as one stack named for the topic (Budget articles, Policy articles, Claim articles, Balance articles, Card articles).

```viz
{"kind": "sitemap", "stack_from": 2, "caption": "Sitemap: perqo.com as redesigned, F3, page types tagged, an ID in every note and a template in every note but Sign in's, many pages of one type drawn as one stack; supports the decision on what exists on the site and what builds each page (Deliverable B). Every box is tone 1, perqo.com. The bracketed note on Campaign pages is IA2's conditional area; the one external box, Sign in, leaves the site, with '→ see' to its destination; 'footer' in a note marks a page reached from the footer, outside the levels (a word added under IA2's rule 'Keep the notation; extend the legend', IA2, section 4); the five footer boxes (seven pages, the three legal pages drawn as one stack) are Home's children like the six global routes, since the sitemap kind draws one set of rows under the root, and only their notes tell them apart. The Campaign pages stack hangs from Home for the same reason; its note, 'no navigation', marks it as off the hierarchy. Removed pages are not drawn. Perqo is fictional; Home, its six global routes, Product's three pages, Customers and the Help centre's audience and task levels from IA1, section 2.3, and IA2, section 5.3; the rest from Deliverable A.", "root": {"label": "Home", "type": "home", "note": "S-0 · T-01", "tone": 1, "children": [
 {"label": "Product", "type": "section", "note": "S-1 · T-02", "tone": 1, "children": [
  {"label": "Perqo Admin", "type": "detail", "note": "S-1.1 · T-03", "tone": 1},
  {"label": "Perqo app", "type": "detail", "note": "S-1.2 · T-03", "tone": 1},
  {"label": "Perqo card", "type": "detail", "note": "S-1.3 · T-03", "tone": 1},
  {"label": "Benefits", "type": "section", "note": "S-1.4 · T-02", "tone": 1, "children": [
   {"label": "Health", "type": "detail", "note": "S-1.4.1 · T-04 · CAT-HEA", "tone": 1},
   {"label": "Learning", "type": "detail", "note": "S-1.4.2 · T-04 · CAT-LEA", "tone": 1},
   {"label": "Mobility", "type": "detail", "note": "S-1.4.3 · T-04 · CAT-MOB", "tone": 1},
   {"label": "Meals", "type": "detail", "note": "S-1.4.4 · T-04 · CAT-MEA", "tone": 1}]},
  {"label": "Security", "type": "detail", "note": "S-1.5 · T-06", "tone": 1}]},
 {"label": "Pricing", "type": "detail", "note": "S-2 · T-05", "tone": 1},
 {"label": "Customers", "type": "index", "note": "S-3 · T-07", "tone": 1, "children": [
  {"label": "Customer stories", "type": "stack", "note": "S-3.1 to S-3.3 · T-08 · one per client", "tone": 1}]},
 {"label": "Help centre", "type": "index", "note": "H-0 · T-13", "tone": 1, "children": [
  {"label": "Search results", "type": "index", "note": "H-0.1 · T-14", "tone": 1},
  {"label": "For HR and finance teams", "type": "section", "note": "H-1 · T-15", "tone": 1, "children": [
   {"label": "Budgets", "type": "section", "note": "H-1.1 · T-15", "tone": 1, "children": [
    {"label": "Budget articles", "type": "stack", "note": "H-1.1.1, H-1.1.2 · T-16", "tone": 1}]},
   {"label": "Policies", "type": "section", "note": "H-1.2 · T-15", "tone": 1, "children": [
    {"label": "Policy articles", "type": "stack", "note": "H-1.2.1 to H-1.2.3, H-1.2.5 · T-16; H-1.2.5 also listed under Claims", "tone": 1}]},
   {"label": "Approvals", "type": "section", "note": "H-1.3 · T-15", "tone": 1, "children": [
    {"label": "Approving and rejecting claims", "type": "detail", "note": "H-1.3.1 · T-16", "tone": 1}]}]},
  {"label": "For employees", "type": "section", "note": "H-2 · T-15", "tone": 1, "children": [
   {"label": "Claims", "type": "section", "note": "H-2.1 · T-15", "tone": 1, "children": [
    {"label": "Claim articles", "type": "stack", "note": "H-2.1.1 to H-2.1.4 · T-16; also lists H-1.2.5", "tone": 1}]},
   {"label": "Balance", "type": "section", "note": "H-2.2 · T-15", "tone": 1, "children": [
    {"label": "Balance articles", "type": "stack", "note": "H-2.2.1, H-2.2.2 · T-16", "tone": 1}]},
   {"label": "Card", "type": "section", "note": "H-2.3 · T-15", "tone": 1, "children": [
    {"label": "Card articles", "type": "stack", "note": "H-2.3.1, H-2.3.2 · T-16", "tone": 1}]}]}]},
 {"label": "Book a demo", "type": "form", "note": "S-4 · T-09", "tone": 1, "children": [
  {"label": "Demo request received", "type": "detail", "note": "S-4.1 · T-10", "tone": 1}]},
 {"label": "Sign in", "type": "external", "note": "S-5 · → see Perqo Admin", "tone": 1},
 {"label": "Get the Perqo app", "type": "detail", "note": "S-6 · T-06 · footer", "tone": 1},
 {"label": "For merchants", "type": "detail", "note": "S-7 · T-06 · footer", "tone": 1},
 {"label": "About Perqo", "type": "detail", "note": "S-8 · T-06 · footer", "tone": 1},
 {"label": "Contact", "type": "form", "note": "S-9 · T-09 · footer", "tone": 1},
 {"label": "Legal pages", "type": "stack", "note": "S-10 to S-12 · T-11 · footer", "tone": 1},
 {"label": "Campaign pages", "type": "stack", "note": "[campaign live] L-01 · T-12 · no navigation", "tone": 1}]}}
```

### B.2 · The labels, judged by IA3's checklist

IA3's labelling checklist is the test for every label above (IA3, Deliverable). The labels this unit sets or keeps at the top two levels, item by item:

| Label | A1 names what is behind it | A2 first word tells it apart | D1 users' words | D2 one label, one thing | Verdict |
|---|---|---|---|---|---|
| Product | yes: the three surfaces and the categories | yes | yes | yes | keep (IA1) |
| Pricing | yes | yes | yes | yes | keep (IA1) |
| Customers | yes: the customer stories | yes | yes | yes | keep (IA1) |
| Help centre | yes | yes | yes | yes | keep (IA1) |
| Book a demo | yes: the one form | yes | yes | yes | keep (IA2) |
| Sign in | yes for HR and finance; assumed: an employee may read it as theirs (section 5.5) | yes | yes | yes | keep; test |
| Benefits | yes: the four categories | yes | yes | yes: the app's Benefits tab holds the same four once IA3's C1 fix removes Perks | new |
| Security | yes | yes | yes | yes | keep |
| Get the Perqo app | yes | yes: "Get" is the only verb in the footer | yes | yes | keep |
| For merchants | yes: the content is for merchants (Sherwin 2015) | yes: no other footer label starts with "For" | yes | yes | keep |
| Features (removed) | no: repeats Product | yes | no: an internal word for the product list | no: a second name for Product | remove (S-1.6) |

The Help centre's audience and topic labels are IA1's and IA2's and are kept; the topics added here, Approvals and Card, are the names Admin and the app already use for the same areas (IA1, Deliverable), which passes D2 across surfaces.

### B.3 · How the organisation system shows up on perqo.com

IA4 asked that one organisation decision be traceable through navigation, filters, search and URLs (IA4, section 5). The benefit-category facet, F-CAT, on perqo.com (Perqo, fictional):

| Where | How F-CAT shows up | Rule |
|---|---|---|
| Navigation | the four category pages under Product, Benefits (S-1.4.1 to S-1.4.4) | IA4, section 5: hierarchy to routes |
| Filters | the Customers index filters stories by F-CAT; a value with no story is hidden | Hearst 2006 (IA4, section 3.2); IA4, B.4, R5 |
| Search | the Help centre's search maps every variant term in IA4's B.2 to its value, so "gym" finds CAT-HEA-FIT's articles | Furnas and others 1987 (IA3, section 4.2); IA3, D3 |
| URLs | each category page's address carries its identifier, then its term: /product/benefits/cat-hea/health | IA4, section 5; Google, URL structure (section 5.1) |
| Metadata | every help article and customer story carries F-CAT tags, a template field (T-08, T-16) | IA4, "What IA5 and DD-IA3 take" |

## Deliverable · C · The perqo.com page-template catalogue

*Face of this artefact (IA2, the notation sheet): page-template catalogue for perqo.com, F3, every template with its purpose, page type, required and optional modules and the pages it builds; decision: what engineering builds once and content fills many times; readers: engineering (build), content (what to fill), marketing (what each page can hold), DD-IA3 (what localisation changes); leaves out: visual design, the modules' internal layout, copy; owner: the IA designer with engineering; version 1, dated 3 November 2026; Perqo is fictional.*

### C.1 · The modules

Every template is built from these modules (Perqo, fictional). A module is named once and used by ID; a change to a module changes every template that uses it.

| ID | Module | What it holds | Rule it carries |
|---|---|---|---|
| M-01 | Global header | Product, Pricing, Customers, Help centre, Book a demo, Sign in | global routes, on every page a visitor can arrive at (section 4.3) |
| M-02 | Footer | Get the Perqo app, For merchants, About Perqo, Contact, the three legal pages | the footer routes (Deliverable B) |
| M-03 | Breadcrumb | the path from Home | shows where a landed-on page sits (section 4.3) |
| M-04 | Page heading and summary | the page's title, the same words as the label that led to it, and one sentence | IA3, A1 and A3 |
| M-05 | Book a demo | the route to S-4 | the conversion route |
| M-06 | Surface tiles | Perqo Admin, Perqo app, Perqo card | IA1's surfaces, in perqo.com's words |
| M-07 | Category tiles | the four F-CAT top-level values | F-CAT by identifier (IA4, Deliverable B) |
| M-08 | Catalogue examples | the catalogue items under one F-CAT value, in basic-level words | IA3, C2; hidden when no item holds the value (IA4, R5) |
| M-09 | Story teaser | one customer story, chosen by F-CAT | R-19: a story is about a client |
| M-10 | Plan comparison | the two plans and their prices per employee per month | Loranger 2013; Fessenden 2019 |
| M-11 | Pricing scenario | one worked example of a client's cost | Fessenden 2019: "common pricing scenarios" |
| M-12 | Questions and answers | short answers on the page's subject | none beyond the page's own |
| M-13 | Related help articles | articles sharing the page's F-CAT tags or topic | contextual routes from metadata (Cardello 2014) |
| M-14 | Story body | the client, what they set up, the outcome | R-19 |
| M-15 | Form with reasons | O-16's fields, each with why it is asked | Fessenden 2019 |
| M-16 | Next steps | what happens after a form is sent, and when | none beyond the page's own |
| M-17 | Audience chooser | For HR and finance teams, For employees | IA1, section 2.3 |
| M-18 | Help search box | search inside the Help centre only | IA2, section 5.3 |
| M-19 | Topic list | a section's topics or articles | the hierarchy's local routes |
| M-20 | Article body | the article's text | none beyond the page's own |
| M-21 | Article facts | audience, F-CAT tags, last updated | O-14's attributes (IA4, Deliverable A) |
| M-22 | Also listed under | the second section that lists the article | IA4, section 1.2; one URL, two routes |
| M-23 | Was this helpful | a yes-or-no question sent to the owner | Perqo's own feedback route; no effect is claimed |
| M-24 | App download links | the app-store links | IA1: perqo.com passes the download link to the app |
| M-25 | Legal text with version date | the policy and the date it took effect | none beyond the page's own |
| M-26 | Results list | search results, with a zero-result message that offers the topic lists | Farrell 2017 (IA3, section 5.2) |
| M-27 | Campaign message | one offer and one route | section 5.2 |

### C.2 · The templates

| ID | Template | Type | Purpose | Required modules | Optional modules | Builds | Localisation |
|---|---|---|---|---|---|---|---|
| T-01 | Home | home | say what Perqo is and for whom; route to every area | M-01, M-04, M-06, M-07, M-05, M-02 | M-09; one campaign slot linking to an L- page | S-0 | language only |
| T-02 | Section landing | section | land a group and list what is in it | M-01, M-03, M-04, M-19, M-02 | M-06 or M-07 (by section), M-05 | S-1, S-1.4 | language only |
| T-03 | Product page | detail | sell one surface | M-01, M-03, M-04, M-05, M-02 | M-09, M-12, M-13 | S-1.1 to S-1.3 | language only |
| T-04 | Benefit category | detail | show a buyer what one category covers, bound to its F-CAT identifier | M-01, M-03, M-04, M-08, M-05, M-02 | M-09, M-12 | S-1.4.1 to S-1.4.4 | language; M-08's items may differ by market |
| T-05 | Pricing | detail | show what Perqo costs | M-01, M-03, M-04, M-10, M-11, M-05, M-02 | M-12 | S-2 | market: M-10 and M-11 |
| T-06 | Standard page | detail | one page of company or practical information | M-01, M-03, M-04, M-02 | M-24 (required on S-6), M-05, M-12 | S-1.5, S-6, S-7, S-8 | language; M-24 by market |
| T-07 | Story index | index | list customer stories, filtered by F-CAT | M-01, M-03, M-04, M-19, M-02 | M-05 | S-3 | language only |
| T-08 | Customer story | detail | one client's story, tagged with F-CAT | M-01, M-03, M-04, M-14, M-05, M-02 | M-13 | S-3.1 to S-3.3 | language only |
| T-09 | Form | form | collect one request | M-01, M-03, M-04, M-15, M-02 | none | S-4, S-9 | language only |
| T-10 | Confirmation | detail | confirm a request and say what happens next | M-01, M-04, M-16, M-02 | M-13 | S-4.1 | language only |
| T-11 | Legal | detail | one policy | M-01, M-03, M-04, M-25, M-02 | none | S-10 to S-12 | market: M-25 |
| T-12 | Campaign landing | detail | one campaign message; off the hierarchy, noindex | M-01, M-04, M-27, M-05, M-02 | M-09, M-07 | L-01 | language only |
| T-13 | Help centre home | index | send each audience to its section | M-01, M-04, M-18, M-17, M-02 | none | H-0 | language only |
| T-14 | Help search results | index | show results for a query; noindex | M-01, M-04, M-18, M-26, M-02 | none | H-0.1 | language; synonyms per language (DD-IA3) |
| T-15 | Help section | section | list an audience's topics or a topic's articles | M-01, M-03, M-04, M-18, M-19, M-02 | none | H-1, H-1.1 to H-1.3, H-2, H-2.1 to H-2.3 | language only |
| T-16 | Help article | detail | answer one question for one audience | M-01, M-03, M-04, M-18, M-20, M-21, M-13, M-23, M-02 | M-22 (required when cross-listed) | every H-x.y.z article | language only |
| T-17 | Page not found | none | tell a visitor the address is gone and give the routes on | M-01, M-04, M-02 | M-18 | no inventory row: shown for any address with no page and no redirect | language only |

```viz
{"kind": "matrix", "caption": "Template catalogue: perqo.com's seventeen templates against the seven modules most of them share, required or optional; supports the decision on what engineering builds once and what each page must carry (Deliverable C). Templates as page-level structure from Frost, Atomic Design, 2016, ch. 2; the header, heading and breadcrumb on every arrival page from Baker, Every Page Is Page One, 2013, and IA3, A1 and A3; Book a demo and the pricing modules from Fessenden, NN/g, 2019. Rows tone 1, perqo.com. Perqo is fictional; every mark from the table C.2.", "cols": ["Header", "Heading", "Breadcrumb", "Demo", "Related help", "Help search", "Footer"], "rows": [
 {"label": "T-01 Home", "tone": 1, "cells": ["req", "req", null, "req", null, null, "req"]},
 {"label": "T-02 Section landing", "tone": 1, "cells": ["req", "req", "req", "opt", null, null, "req"]},
 {"label": "T-03 Product page", "tone": 1, "cells": ["req", "req", "req", "req", "opt", null, "req"]},
 {"label": "T-04 Benefit category", "tone": 1, "cells": ["req", "req", "req", "req", null, null, "req"]},
 {"label": "T-05 Pricing", "tone": 1, "cells": ["req", "req", "req", "req", null, null, "req"]},
 {"label": "T-06 Standard page", "tone": 1, "cells": ["req", "req", "req", "opt", null, null, "req"]},
 {"label": "T-07 Story index", "tone": 1, "cells": ["req", "req", "req", "opt", null, null, "req"]},
 {"label": "T-08 Customer story", "tone": 1, "cells": ["req", "req", "req", "req", "opt", null, "req"]},
 {"label": "T-09 Form", "tone": 1, "cells": ["req", "req", "req", null, null, null, "req"]},
 {"label": "T-10 Confirmation", "tone": 1, "cells": ["req", "req", null, null, "opt", null, "req"]},
 {"label": "T-11 Legal", "tone": 1, "cells": ["req", "req", "req", null, null, null, "req"]},
 {"label": "T-12 Campaign landing", "tone": 1, "cells": ["req", "req", null, "req", null, null, "req"]},
 {"label": "T-13 Help centre home", "tone": 1, "cells": ["req", "req", null, null, null, "req", "req"]},
 {"label": "T-14 Help search results", "tone": 1, "cells": ["req", "req", null, null, null, "req", "req"]},
 {"label": "T-15 Help section", "tone": 1, "cells": ["req", "req", "req", null, null, "req", "req"]},
 {"label": "T-16 Help article", "tone": 1, "cells": ["req", "req", "req", null, "req", "req", "req"]},
 {"label": "T-17 Page not found", "tone": 1, "cells": ["req", "req", null, null, null, "opt", "req"]}],
 "legend": [{"mark": "req", "means": "required on every page the template builds", "tone": 1}, {"mark": "opt", "means": "optional", "tone": 1}]}
```

**What the catalogue hands on.** Engineering builds seventeen templates and twenty-seven modules for the redesigned site's 52 rows. Content fills pages by inventory row and template. DD-IA3 takes the localisation column: the modules marked by market (M-10, M-11, M-24, M-25) need a decision per market, the rest a translation. IA8 takes the external routes, IA10 the owners. A new page goes through the decision tree in section 5.2 and enters the inventory with an ID, a template and an owner before it enters the sitemap.

## Sources

- Baker, Mark. *Every Page Is Page One: Topic-Based Writing for Technical Communication and the Web*. XML Press, 2013. Book site at [everypageispageone.com/the-book](https://everypageispageone.com/the-book) (practice).
- Berners-Lee, Tim. "Cool URIs Don't Change". W3C, 1998 (W3C style guidance). [w3.org/Provider/Style/URI](https://w3.org/Provider/Style/URI)
- Brown, Dan M. *Communicating Design: Developing Web Site Documentation for Design and Planning*. 2nd ed. New Riders, 2011. Ch. 5.
- Budiu, Raluca. "Information Scent: How Users Decide Where to Go Next". Nielsen Norman Group, 2 February 2020. [nngroup.com/articles/information-scent](https://www.nngroup.com/articles/information-scent/)
- Cardello, Jen. "The Difference Between Information Architecture (IA) and Navigation". Nielsen Norman Group, 22 June 2014. [nngroup.com/articles/ia-vs-navigation](https://www.nngroup.com/articles/ia-vs-navigation/)
- European Commission. "Reasons for building a task-based information architecture". Europa Web Guide, undated (institutional guidance). [commission.europa.eu](https://commission.europa.eu/resources-partners/europa-web-guide/planning-your-web-presence/architecture-and-navigation/task-based-information-architecture_en)
- Farrell, Susan. "Search-Log Analysis: The Most Overlooked Opportunity in Web UX Research". Nielsen Norman Group, 30 July 2017. [nngroup.com/articles/search-log-analysis](https://www.nngroup.com/articles/search-log-analysis/)
- Fessenden, Therese. "What B2B Designers Can Learn from B2C About Building Trust". Nielsen Norman Group, 1 September 2019. [nngroup.com/articles/b2b-trust-from-b2c](https://www.nngroup.com/articles/b2b-trust-from-b2c/)
- Frost, Brad. *Atomic Design*. 2016. Ch. 2, "Atomic Design Methodology". Outline at [atomicdesign.bradfrost.com/outline](https://atomicdesign.bradfrost.com/outline)
- Furnas, George W., Thomas K. Landauer, Louis M. Gomez and Susan T. Dumais. "The Vocabulary Problem in Human-System Communication". *Communications of the ACM* 30, no. 11 (1987): 964 to 971. [cacm.acm.org](https://cacm.acm.org/research/the-vocabulary-problem-in-human-system-communication)
- Garrett, Jesse James. *Visual Vocabulary Quick Reference*. Undated one-page PDF. [jjg.net/ia/visvocab/files/garrett_ia_quickref.pdf](http://www.jjg.net/ia/visvocab/files/garrett_ia_quickref.pdf)
- Google Search Central. "Block Search Indexing with noindex". Page updated 10 December 2025 (vendor documentation, checked 3 November 2026). [developers.google.com/search/docs/crawling-indexing/block-indexing](https://developers.google.com/search/docs/crawling-indexing/block-indexing)
- Google Search Central. "Localized Versions of your Pages". Page updated 21 September 2026 (vendor documentation, checked 3 November 2026). [developers.google.com/search/docs/specialty/international/localized-versions](https://developers.google.com/search/docs/specialty/international/localized-versions)
- Google Search Central. "Redirects and Google Search". Page updated 14 April 2026 (vendor documentation, checked 3 November 2026). [developers.google.com/search/docs/crawling-indexing/301-redirects](https://developers.google.com/search/docs/crawling-indexing/301-redirects)
- Google Search Central. "URL Structure Best Practices for Google Search". Page updated 21 October 2026 (vendor documentation, checked 3 November 2026). [developers.google.com/search/docs/crawling-indexing/url-structure](https://developers.google.com/search/docs/crawling-indexing/url-structure)
- Halvorson, Kristina, and Melissa Rach. *Content Strategy for the Web*. 2nd ed. New Riders, 2012. Chs 5, "Audit", and 6, "Analysis"; contents and index in the publisher's sample at [ptgmedia.pearsoncmg.com](https://ptgmedia.pearsoncmg.com/images/9780321808301/samplepages/0321808304.pdf).
- Hearst, Marti A. "Clustering versus Faceted Categories for Information Exploration". *Communications of the ACM* 49, no. 4 (2006): 59 to 61. [flamenco.ischool.berkeley.edu/papers/cacm06.pdf](https://flamenco.ischool.berkeley.edu/papers/cacm06.pdf)
- Kaley, Anna. "Content Inventory and Auditing 101". Nielsen Norman Group, 27 September 2020. [nngroup.com/articles/content-audits](https://www.nngroup.com/articles/content-audits/)
- Krug, Steve. *Don't Make Me Think, Revisited: A Common Sense Approach to Web Usability*. 3rd ed. New Riders, 2014. Ch. 7, "The Big Bang Theory of Web Design". Contents at [oreilly.com](https://oreilly.com/library/view/dont-make-me/9780133597271) (practice).
- Laubheimer, Page. "3 Common IA Mistakes (that Are All Due to Low Information Scent)". Nielsen Norman Group, 16 April 2023. [nngroup.com/articles/3-ia-mistakes](https://www.nngroup.com/articles/3-ia-mistakes/)
- Loranger, Hoa. "State the Price to Give B2B Sites a Competitive Advantage". Nielsen Norman Group, 1 December 2013. [nngroup.com/articles/show-price](https://www.nngroup.com/articles/show-price/)
- McGovern, Gerry. "What Really Matters: Focusing on Top Tasks". A List Apart, April 2015; republished by Center Centre, 20 January 2016. [articles.centercentre.com/?p=877](https://articles.centercentre.com/?p=877) (practice).
- Nielsen, Jakob. "Information Foraging: Why Google Makes People Leave Your Site Faster". Nielsen Norman Group, 29 June 2003. [nngroup.com/articles/information-foraging-leave-site](https://www.nngroup.com/articles/information-foraging-leave-site/)
- Nielsen, Jakob. "Use Old Words When Writing for Findability". Nielsen Norman Group, 27 August 2006. [nngroup.com/articles/web-writing-use-search-keywords](https://www.nngroup.com/articles/web-writing-use-search-keywords/)
- Nielsen, Jakob. "First 2 Words: A Signal for the Scanning Eye". Nielsen Norman Group, 6 April 2009. [nngroup.com/articles/first-2-words-a-signal-for-scanning](https://nngroup.com/articles/first-2-words-a-signal-for-scanning)
- Richardson, Cath. "'Hey, you there': the trouble with audience-based navigation". Inside GOV.UK blog, 18 July 2014. [insidegovuk.blog.gov.uk](https://insidegovuk.blog.gov.uk/2014/07/18/hey-you-there-the-trouble-with-audience-based-navigation/) (a government team's account; practice).
- Rosenfeld, Louis, Peter Morville and Jorge Arango. *Information Architecture: For the Web and Beyond*. 4th ed. O'Reilly, 2015. Chs 6 and 13. Contents at [oreilly.com](https://www.oreilly.com/library/view/information-architecture-4th/9781491913529/).
- Sherwin, Katie. "Audience-Based Navigation: 5 Reasons to Avoid It". Nielsen Norman Group, 7 September 2015. [nngroup.com/articles/audience-based-navigation](https://www.nngroup.com/articles/audience-based-navigation/)
- Spencer, Donna. *A Practical Guide to Information Architecture*. 2nd ed. UX Mastery, 2014. Part 3, chs 11 to 15. Publisher's announcement at [uxmastery.com](https://uxmastery.com/coming-soon-a-practical-guide-to-information-architecture-second-edition/).
- Tankala, Samhita. "Information Architecture vs. Sitemaps". Nielsen Norman Group, 3 September 2023. [nngroup.com/articles/information-architecture-sitemaps](https://www.nngroup.com/articles/information-architecture-sitemaps/)
- Whitenton, Kathryn. "Flat vs. Deep Website Hierarchies". Nielsen Norman Group, 10 November 2013. [nngroup.com/articles/flat-vs-deep-hierarchy](https://www.nngroup.com/articles/flat-vs-deep-hierarchy/)
- Cited through the filed units, for claims made there: Larson and Czerwinski 1998; Zaphiris 2000 (IA4, Sources); Sitemaps.org protocol (IA2, Sources).

## Perqo facts set by this unit

Every fact below is a course convention (Perqo, fictional), never evidence about the world. Each keeps every registered fact; none renames an IA1 to IA4 label.

| Fact | Set in | Left free |
|---|---|---|
| perqo.com's top level is by topic (Product, Pricing, Customers, Help centre), with Book a demo and Sign in as task routes in the header; audience is used only inside the Help centre and on For merchants | section 2.4 | the navigation components and header design |
| For merchants (S-7), a footer page owned by the partnerships team | section 2.5; Deliverable A | its content; the merchant side's own surface |
| Product holds Perqo Admin, Perqo app, Perqo card (IA2), plus a Benefits section with one page per F-CAT top-level value (S-1.4.1 to S-1.4.4, owned by the content team) and Security (S-1.5, owned by Product) | Deliverables A and B | category pages for narrower terms (none: R7 keeps two levels; no page per narrower term is set) |
| A category page's URL carries its identifier, then its preferred term: /product/benefits/cat-hea/health; a rename under R9 redirects the old address | section 5.1; Deliverable B, B.3 | the URL form in other languages (DD-IA3) |
| perqo.com page IDs: S- for site pages, L- for campaign pages, H- for the Help centre (IA2's scheme kept); the full inventory of 57 rows, 42 pages and files today and 52 after the redesign, with the type, template, audience, owner, F-CAT tags and status of each | Deliverable A | traffic and last-modified dates for all but IA2's rows |
| Owners on perqo.com: Marketing, Sales, Support, Product, Partnerships, Legal, Content team | Deliverable A | named people (none may be named) |
| Audit findings: S-1.2 says "allowance"; a Features page (S-1.6) and a brochure PDF (S-1.7) duplicate Product; Pricing says "Contact us for pricing"; the home page's opening line says neither what Perqo is nor who buys it; Book a demo asks for a phone number sales does not use; customer story S-3.4 is about a former client; campaign page L-02 outlived its campaign | section 1.3; Deliverable A | the pages' copy |
| Four customer stories today (a software consultancy, a logistics group, a design studio, a retail chain), three after the audit; each tagged with one F-CAT value | Deliverable A | client names; the stories' content |
| Perqo has two plans, each with a published price per employee per month | section 5.4 | plan names and amounts |
| Perqo has no self-serve sign-up and no free trial; a client starts after a contract | section 5.5 | the contract's terms |
| Get the Perqo app (S-6), owned by support, holds the download links; employees join from HR's invitation and do not sign in on perqo.com | section 5.5; Deliverable A | the app stores named |
| Assumed, untested: an employee may press Sign in and land on Admin's sign-in screen; proposed for IA7: a line there pointing employees to Get the Perqo app | section 5.5 | the test's result; IA7's decision (taken with one change, IA7, C.5, 3 Nov 2026) |
| perqo.com is published in English only today | section 5.3 | which markets and languages come next (DD-IA3) |
| Campaign pages live under /lp/, are noindex, appear in no navigation, use T-12, carry an owner and an end date, and redirect at the end; L-01 "Learning budgets for engineering teams" is live | section 5.2; Deliverable A | campaign dates and channels |
| Help centre additions: Approvals topic under For HR and finance teams (H-1.3, H-1.3.1); Card topic under For employees (H-2.3, two articles); articles H-1.2.5 (replaces the PDF, listed under both audiences), H-2.1.3, H-2.1.4 (tagged CAT-HEA-FIT, answers "gym"), H-2.2.2; Balance gets its own topic page at /help/employees/balance and H-2.2.1 moves with a redirect; H-0.1 search results page, noindex | Deliverable A | the articles' text |
| New attributes: a help article (O-14) and a customer story (O-15) carry F-CAT tags | section 3.3 | how many tags an item may carry |
| The template catalogue: seventeen templates, T-01 to T-17, and twenty-seven modules, M-01 to M-27, with the required and optional modules of each; the Customers index filters stories by F-CAT; help articles carry a "Was this helpful" question sent to the owner | Deliverable C | visual design; module layout |
| New status value *new* in inventories, beside keep, update and remove | section 1.1 | none |

## Unsure list

- Halvorson and Rach 2012, chs 5 and 6: chapter titles and the audit field names are from the publisher's sample (contents and index); the chapters' text was not read.
- Spencer 2014: chapter titles and order from the edition's front matter in an excerpt; the content of chs 11 to 15 was not seen, so no claim is made about what they recommend beyond their order.
- Krug 2014, ch. 7: the chapter title is checked from the contents; that it treats the home page as the page that must say what the site is and is for is from knowledge of the book, not re-read.
- Baker 2013: the year is from the publisher's announcement URL in a search result, not from the book; the quoted line is from the book's own site.
- Frost 2016: the template and page definitions are from the book's online outline; the chapter number for them (ch. 2) is inferred from the outline's chapter list.
- McGovern: the A List Apart original's date (April 2015) is as the Center Centre republication states it; the A List Apart page was not opened.
- European Commission web guide: undated page; the 2014 adoption year is the page's own statement.
- Loranger 2013: reports NN/g usability-study observations without sample sizes; the claim that business customers rank pricing as the most needed information is NN/g's, with no study figure given.
- NN/g "Homepage design principles" could not be read (rate-limited); nothing from it is cited.
- Google Search Central pages: "updated" dates as printed on each page when fetched on 3 November 2026; they change.
- Fresh check 2026-11-03 (Fable 5.1): fix · 2 errors, 3 should-fix, 5 minor; all applied; figure 4 fixed from the check and passed re-check 1; figure 6 fixed from the check, from re-check 1 and from re-check 2, and passed on re-check 3, its fourth check; figures 1, 2, 3, 5 and 7 passed; report `audits/ux/fresh-check-IA5.md`.
