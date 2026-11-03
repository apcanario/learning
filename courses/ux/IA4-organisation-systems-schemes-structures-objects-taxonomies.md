---
code: IA4
title: Organisation systems: schemes, structures, objects, taxonomies
course: ux · IA · Information Architecture
model: Opus 5.5
written: 2026-11-03
search: off
---

# IA4 · Organisation systems: schemes, structures, objects, taxonomies

IA1 named the organisation system as the first of the four systems of an information architecture: how content is grouped, and by which scheme (IA1, section 1.1). IA3 gave the evidence a grouping is judged by, and handed this unit four of its checklist items as the criteria for choosing one: C1, is each group one kind of thing; C2, where a group's label is a superordinate term, does the group show basic-level examples; C3, does every far member have a route from the other group people are expected to look in; C4, is each group organised from the person's perspective, with any group that exists for an internal reason named as such (IA3, Deliverable). This unit uses those four, by their codes, to choose schemes and structures. It then builds the two artefacts IA2's decision table assigned to it: the object map ("What does the system hold, and what can people do to it?") and the taxonomy ("How do the terms nest?") (IA2, Deliverable, the artefact decision table). Every figure uses IA2's notation (IA2, section 5 and the notation sheet).

## 1 · Organisation schemes

### 1.1 · Exact and ambiguous

The Polar Bear book's chapter 6, "Organization Systems", divides organisation schemes into two kinds under two headings, "Exact Organization Schemes" and "Ambiguous Organization Schemes", and then treats organisation structures separately, under "The Hierarchy: A Top-Down Approach", "The Database Model: A Bottom-Up Approach" and "Hypertext", followed by "Social Classification" (Rosenfeld, Morville and Arango, *Information Architecture: For the Web and Beyond*, 4th ed., O'Reilly, 2015, ch. 6, [oreilly.com](https://oreilly.com/library/view/information-architecture-4th/9781491913529/ch06.html)). The distinction matters because it separates two decisions a team often makes as one. A scheme is the rule that decides which items share a group (by name, by date, by subject). A structure is the shape the groups are arranged in (a tree, a set of independent facets, a web of links). This section covers schemes, section 2 structures.

In this course's words: an **exact** scheme divides content into groups that do not overlap, by a property every item has exactly one value of, so that placing an item needs no judgement. An **ambiguous** scheme divides content by meaning, so that placing an item is a judgement, and different people judge differently. IA3 already set out why meaning-based grouping is hard: the chapter's four challenges, Ambiguity, Heterogeneity, Differences in Perspectives and Internal Politics (IA3, section 3.2), and the prototype structure of categories, which makes central members easy to place and far members easy to miss (IA3, sections 3.1 and 3.3). This unit builds on those and does not repeat them.

The exact schemes the chapter names are three. Richard Saul Wurman had proposed a similar short list in *Information Anxiety* (Doubleday, 1989): his "five ultimate hat racks", later abbreviated LATCH, for location, alphabet, time, category and continuum, the last later renamed hierarchy; a reviewer notes their resemblance to the facets of Ranganathan's colon classification (D. Ben Woods, review of *Information Anxiety*, UXmatters, 18 March 2019, [uxmatters.com](https://uxmatters.com/mt/archives/2019/03/book-review-information-anxiety.php); a review, cited for its description of the book). Location, alphabet and time are the exact three.

- **Alphabetical.** Items in the order of their names. It works when the person knows the item's name, and in the word the list uses. Furnas and colleagues found that two people chose the same term for an object with a probability under 0.20 (Furnas, Landauer, Gomez and Dumais, *Communications of the ACM* 30, no. 11, 1987; IA3, section 4.2), so an alphabetical list is exact for the system and ambiguous for the person who has to guess the first letter. An A to Z index works when its entries include the variants people use.
- **Chronological.** Items in date order. It suits content whose date is what people ask about: news, a history, a statement of transactions. It is exact because every item has one date; it answers "what happened recently" and fails "where is the thing about X".
- **Geographical.** Items by place. It suits content that differs by place (a branch, a law, a delivery area) and people who know where they are.

On ordering inside a menu, one result reported from early menu research is that alphabetical ordering of selections beat functional ("logical") ordering, which beat random ordering (Card 1982, as reported in the abstract of "Menu Structure and Ordering of Menu Selection: Independent or Interactive Effects?", *ACM SIGCHI Bulletin* 18, no. 2, October 1986, [unpaywall.org](https://unpaywall.org/10.1145%2F15683.1044100); the 1982 study itself was not seen). The same abstract reports that Snowberry and others (1983) found breadth superior "only with consistent ordering of selections within levels" (same abstract). The finding is about selecting a known target from a menu, the case alphabetical order is built for.

The ambiguous schemes are four, with the hybrid, which the chapter treats in its own section, as a fifth here.

- **Topic.** Items by subject. Perqo's four benefit categories, Health, Learning, Mobility and Meals (Perqo, fictional), are a topic scheme (IA3, section 3.2). It is the scheme people expect for browsing a subject they cannot yet name, and the one most exposed to the ambiguity and prototype effects IA3 described.
- **Task.** Items by what the person is trying to do. It suits a product used for a small set of recurring jobs. Its risk is that tasks overlap and are phrased as actions; Laubheimer counts conversational "I want to…" labels among the low-scent faults ("3 Common IA Mistakes", Nielsen Norman Group, 16 April 2023, [nngroup.com/articles/3-ia-mistakes](https://www.nngroup.com/articles/3-ia-mistakes/); IA3, section 1.2).
- **Audience.** Items by who they are for. It works when the audiences are distinct, know which one they belong to, and want different content. It fails when content serves both, because the item must then be duplicated or one audience must cross into the other's area.
- **Metaphor.** Items arranged after something familiar from elsewhere (a desktop, a shop, a wallet). Cooper and his co-authors argue that metaphors rarely scale beyond their first few features and that most interface conventions are learned idioms whose value does not depend on resembling anything (*About Face*, 4th ed., Wiley, 2014, ch. 13, "Metaphors, Idioms, and Affordances"). On that argument a metaphor is a scheme for a small surface or a single screen, chosen for orientation, and retired when the content outgrows it.
- **Hybrid.** Two or more schemes mixed in one set of choices. The fault is the mixing within one list: a person scanning a list must first work out what kind of list it is, which is IA3's heterogeneity point (IA3, section 3.3, C1). Layering schemes at different levels (audience first, then task, as the Help centre does) is a combination of schemes, each level of one kind, and passes C1.

The catalogue, as a tree, with the place each scheme is used at Perqo (Perqo, fictional). The examples: Perqo Admin's Employees list is ordered alphabetically by name, and the Perqo app's Purchases and Claims lists are ordered newest first (both set here); geographical and metaphor schemes are not used at Perqo; the four benefit categories in the app's Benefits are the topic scheme; the Help centre on perqo.com is split first by audience (For HR and finance teams, For employees) and then by task (IA1, section 2.3); and the app's as-is Benefits list, four categories with "Perks" as a fifth item, is a hybrid that fails C1 (IA3, Deliverable).

```viz
{"kind": "tree", "caption": "Tree: the catalogue of organisation schemes, with where each is used at Perqo; supports the decision on which scheme a content set gets (section 1.1). Scheme names and the exact and ambiguous split from Rosenfeld, Morville and Arango, Information Architecture: For the Web and Beyond, 4th ed., 2015, ch. 6, headings; examples from this section, IA1, section 2.3, and IA3, Deliverable. Tone 5 marks the scheme terms, which apply on every surface; each example takes its surface's tone (1 perqo.com, 3 the Perqo app, 4 Perqo Admin) and tone 6 marks a fault found in a review. Geographical and Metaphor have no example because Perqo uses neither. Perqo is fictional.", "root": {"label": "Organisation schemes", "tone": 5, "children": [
 {"label": "Exact", "tone": 5, "children": [
  {"label": "Alphabetical", "tone": 5, "children": [{"label": "Admin: Employees, by name", "tone": 4}]},
  {"label": "Chronological", "tone": 5, "children": [{"label": "App: Purchases and Claims, newest first", "tone": 3}]},
  {"label": "Geographical", "tone": 5}]},
 {"label": "Ambiguous", "tone": 5, "children": [
  {"label": "Topic", "tone": 5, "children": [{"label": "App: Health, Learning, Mobility, Meals", "tone": 3}]},
  {"label": "Task", "tone": 5, "children": [{"label": "Help centre: by task", "tone": 1}]},
  {"label": "Audience", "tone": 5, "children": [{"label": "Help centre: For HR and finance teams, For employees", "tone": 1}]},
  {"label": "Metaphor", "tone": 5},
  {"label": "Hybrid", "tone": 5, "children": [{"label": "As-is Benefits: four categories and Perks", "tone": 6}]}]}]}}
```

### 1.2 · Choosing a scheme by C1 to C4

The criteria IA3 handed on are questions about the person, so they do not all favour one kind of scheme. C1 (one kind of thing per group) and C4 (the person's perspective) favour exact schemes wherever the person thinks in the exact property: an employee looking for last month's claim thinks in dates. C2 and C3 apply only to ambiguous schemes, where they set the price of choosing one: an ambiguous scheme is right only if the team will also supply the examples (C2) and the second routes (C3) it needs. A working rule follows, and it is this unit's synthesis of IA3's evidence: use an exact scheme when the person already knows the property and wants an item they can name (Spencer's known-item seeking, IA3, section 5.1); use an ambiguous scheme when the person comes with a need and not a name, and budget for C2 and C3 when you do.

Applied to six Perqo content sets (Perqo, fictional):

| Content set | Scheme chosen | C1 | C2 | C3 | C4 |
|---|---|---|---|---|---|
| Benefits in the app | Topic: the four categories | pass once Perks leaves the list (IA3, C1 fix) | needs the catalogue's examples under each narrower term (Deliverable B) | needs the cross-listings for far members (Deliverable B, rule R6) | pass: categories are how the policy covers spending |
| Claims in the app | Exact: by state (Submitted, Approved, Rejected, Paid), newest first in each | pass | not applicable | not applicable | pass: IA3's B2 fix groups by all four states |
| Purchases in the app | Chronological, newest first | pass | not applicable | not applicable | pass: a purchase is remembered by when it happened |
| Help centre on perqo.com | Audience, then task | pass: each level one kind | not applicable at the audience level | articles both audiences need are listed in both (set here) | pass: an HR manager and an employee know which they are |
| Employees in Perqo Admin | Alphabetical by name, filtered by employee group | pass | not applicable | not applicable | pass: HR looks people up by name |
| Card offers in the app (the label IA3 proposed) | Topic: the same benefit categories, through the catalogue (Deliverable B) | pass | the offer names the item it is for | an offer is filed under its item's one category | named as a business request: the partnerships team asked for offers to be shown (IA3, C4) |

The last row reuses the benefits taxonomy for a second content set. That is the strongest argument for building the taxonomy as a separate artefact: one classification serves the benefits screens, the offers list, the Help centre's search synonyms and Admin's policy editor (section 5).

## 2 · Organisation structures

### 2.1 · Hierarchy, and the breadth-versus-depth evidence

The chapter calls the hierarchy "a top-down approach" (Rosenfeld, Morville and Arango 2015, ch. 6, heading): groups are designed first and items are placed into them. Every hierarchy has a shape, the number of choices at each level (breadth) against the number of levels (depth), and that shape is one of the few IA questions with a long run of experiments behind it.

The menu studies of the 1980s set the direction. Miller tested 64 target items arranged in four structures and reported that "as depth increased so did response time to select the desired item"; Kiger repeated the work with five structures of 64 items and found time and errors rising with depth, with a structure of 4 choices then 16 the fastest and least error-prone; Snowberry, Parkinson and Sisson found search time improving as depth fell and breadth rose (Miller 1981, Kiger 1984 and Snowberry, Parkinson and Sisson 1983, all as reported by Zaphiris 2000, below; the original papers were not seen). Landauer and Nachbar's experiments showed selection time rising with the logarithm of breadth, which on Dix's analysis means that doubling the choices on a screen costs much less than adding a level (Landauer and Nachbar, CHI '85, as reported by Alan Dix, "Menu Breadth: Not a Case of Miller's 7+/-2", companion page to *Human-Computer Interaction*, 3rd ed., 2003; page dated 2010, [hcibook.com](https://hcibook.com/e3/online/menu-breadth); a textbook author's page, labelled as such). Dix adds that George Miller's "seven plus or minus two", often quoted as a limit on menu length, does not apply, because a person scanning a menu does not have to remember the items: "they are there in front of you" (Dix 2010).

The web studies followed. Panayiotis Zaphiris tested five link hierarchies, each over the same 64 end pages, with 17 participants, and found that "task completion time increases as the depth of the web site structure increases" ("Depth Vs Breadth in the Arrangement of Web Links", *Proceedings of the Human Factors and Ergonomics Society 44th Annual Meeting*, 2000, pp. 139 to 144, [ktisis.cut.ac.cy](https://ktisis.cut.ac.cy/bitstream/20.500.14279/2872/6/Zaphiris2000-Depth_Vs_Breath.pdf)). His mean task times, in seconds: 2 links a page, 6 levels, 36.0; 4 links a page, 3 levels, 32.2; 16 then 4, 2 levels, 32.4; 4 then 16, 2 levels, 21.0; 8 links a page, 2 levels, 20.3. The difference in time was significant; the difference in errors was not, because there were very few errors (Zaphiris 2000). The spread was wide (the standard deviations run from 11.3 to 27.9 seconds), and the sample is small, so the result is a direction more than a measurement.

```viz
{"kind": "compare", "caption": "Compare: breadth versus depth, mean task time to reach a target in five link structures over the same 64 pages; supports the decision on how many levels a hierarchy gets (section 2.1). Data from Zaphiris, 'Depth Vs Breadth in the Arrangement of Web Links', Proceedings of the HFES 44th Annual Meeting, 2000, 17 participants; times differed significantly, errors did not. Every bar is tone 5, since the figure is about structures on any surface; the deepest structure, 2 links a page over 6 levels, is the slowest.", "unit": "s", "max": 40, "decimals": 1, "rows": [
 {"label": "2 links a page, 6 levels", "value": 36.0, "tone": 5},
 {"label": "4 links a page, 3 levels", "value": 32.2, "tone": 5},
 {"label": "16 then 4, 2 levels", "value": 32.4, "tone": 5},
 {"label": "4 then 16, 2 levels", "value": 21.0, "tone": 5},
 {"label": "8 links a page, 2 levels", "value": 20.3, "tone": 5}]}
```

Kevin Larson and Mary Czerwinski tested 512 documents in three structures: three levels of 8 links each; 16 links at the top and 32 at the second level; and 32 at the top and 16 at the second. Users "performed reliably slowest and were most lost when the number of links was held to 8", and were "fastest and least lost with the website with 16 top-level items", though not reliably faster than with 32 (Mary P. Czerwinski and Kevin Larson, "Cognition and the Web: Moving from Theory to Web Design", Microsoft Research, [microsoft.com](https://www.microsoft.com/en-us/research/wp-content/uploads/2002/01/HFandtheWebChapter.pdf), reporting their CHI 98 study). The CHI 98 abstract puts the result in one line: "increased depth did harm search performance on the web", and "a medium condition of depth and breadth outperformed the broadest shallow web structure overall" ("Web Page Design: Implications of Memory, Structure and Scent for Information Retrieval", *CHI 98*, ACM, 1998, pp. 25 to 32, [microsoft.com/research](https://www.microsoft.com/en-us/research/publication/web-page-design-implications-memory-structure-scent-information-retrieval/); IA3, section 6.2). Katz and Byrne found that on novel sites browsing depended on both the breadth and the scent of the menus (IA3, section 5.1).

Kathryn Whitenton's NN/g article turns the evidence into guidance: "All other things being equal, deep hierarchies are more difficult to use"; flat hierarchies "tend to work well if you have distinct, recognizable categories"; but when a level has few categories, "they tend to be more generic and, thus, more confusing", while "users can also become overwhelmed with long, cluttered menus"; and "going too far to either extreme will backfire" ("Flat vs. Deep Website Hierarchies", Nielsen Norman Group, 10 November 2013, [nngroup.com/articles/flat-vs-deep-hierarchy](https://www.nngroup.com/articles/flat-vs-deep-hierarchy/)). NN/g guidance; the article cites no study, and the studies above are this unit's grounding for it.

What the evidence supports, and what it does not. It supports a default: prefer breadth to depth, up to the point where a level's labels stop being distinct, because each added level is one more choice that must carry scent (IA3, section 6.2). It does not support any fixed number of items per level. The studies used lists of known targets on desktop screens, and Larson and Czerwinski's best case was a medium one; Zaphiris's two 2-level structures with the same 64 pages differed by eleven seconds depending on which level was broad. On a phone, breadth costs scrolling, which none of these studies measured; that is a gap, and this unit leaves it unsourced. The Perqo app's tab bar of five, with the four categories one level below (Perqo, fictional), is shallow by every one of these measures; its faults were scent faults (IA3), and a deeper structure would not have fixed them.

### 2.2 · Polyhierarchy

A strict hierarchy gives every item one parent. Page Laubheimer defines the alternative: "A polyhierarchy refers to a graph structure in which at least some child nodes have more than one parent nodes" ("Polyhierarchies Improve Findability for Ambiguous IA Categories", Nielsen Norman Group, 13 May 2018, [nngroup.com/articles/polyhierarchy](https://www.nngroup.com/articles/polyhierarchy/)). The Polar Bear book places polyhierarchy in its chapter on thesauri and controlled vocabularies, beside faceted classification (Rosenfeld, Morville and Arango 2015, ch. 10, headings, [oreilly.com](https://www.oreilly.com/library/view/information-architecture-4th/9781491913529/ch10.html)). Laubheimer gives the benefit, that "having the same product category appear in multiple places supports several different mental models", and three costs: breadcrumbs, which show one canonical path that may not be the one the person took; disorientation in hierarchies deeper than a few levels if breadcrumbs are dropped; and cognitive load, since "too many parents for any given node increase cognitive load and make navigation difficult". His recommendation, NN/g guidance: add a second parent only where research such as closed card sorting, tree testing or usability testing shows people reasonably expect the item there, and for large collections with heavy overlap, use faceted search instead (Laubheimer 2018).

Polyhierarchy is the structural form of IA3's C3 fix. The cookery course, the yoga class and the bike helmet (Perqo, fictional) are far members of their categories, each with an assumed second place an employee looks (IA3, section 3.3). Listing each in both places is a polyhierarchy of display. One constraint at Perqo keeps the money single-parented: a claim is checked against the balance of one category (IA3, section 2.3), so each item has one home category, and the second listing only points to it ("Cookery course: covered under Learning", IA3, C3). Deliverable B writes that as rule R6.

### 2.3 · The database model and faceted structures

The chapter's second structure is "The Database Model: A Bottom-Up Approach" (Rosenfeld, Morville and Arango 2015, ch. 6, heading). In this course's words: items are described by fields (metadata), and the groups are made at the time of asking, by selecting and sorting on those fields. Admin's Employees list, ordered by name and filtered by employee group (Perqo, fictional), is a database structure: no one designs a page for "employees in the Engineering group"; the filter produces it.

A faceted structure is the database model with its fields designed as independent classifications. The idea is older than the web: S. R. Ranganathan's Colon Classification, first published in 1933, built subjects by combining values from separate facets, and its fourth edition (1952) named five fundamental categories, "personality, matter, energy, space, and time, famously known as PMEST" (M. P. Satija, "Colon Classification (CC)", *ISKO Encyclopedia of Knowledge Organization*, version 2.0, 2017, [isko.org](https://isko.org/cyclo/colon_classification)). Marti Hearst describes its interface form: "a set of category hierarchies each of which corresponds to a different facet (dimension or feature type)", where "each item in the collection can be assigned many labels from the hierarchies", and choosing values "builds up a complex query that is a conjunction of disjunctions over subhierarchies"; for browsing tasks, such interfaces are "overwhelmingly preferred" over keyword search and result lists, and they show "previews of where to go next" while "avoiding empty results sets" ("Clustering versus Faceted Categories for Information Exploration", *Communications of the ACM* 49, no. 4, 2006, pp. 59 to 61, [flamenco.ischool.berkeley.edu](https://flamenco.ischool.berkeley.edu/papers/cacm06.pdf)). The measured study behind that preference: 32 art history students explored 35,000 fine-arts images, and 90% preferred the faceted metadata interface overall, 97% said it helped them learn more about the collection, 75% found it more flexible and 72% found it easier to use than a standard baseline (Ka-Ping Yee, Kirsten Swearingen, Kevin Li and Marti Hearst, "Faceted Metadata for Image Search and Browsing", *CHI 2003*, ACM, 2003, abstract, [unpaywall.org](https://unpaywall.org/10.1145%2F642611.642681)). Hearst names the drawback: "by far the greatest drawback is the fact that in most cases the category hierarchies are built by hand" (Hearst 2006). A faceted structure is a taxonomy someone has to maintain, which is why Deliverable B carries rules.

### 2.4 · Hypertext

The chapter's third structure is "Hypertext" (Rosenfeld, Morville and Arango 2015, ch. 6, heading): items joined by links that cross the groups. It is the structure of contextual navigation, and its strength is that it follows the person's associations; its weakness is that a web of links has no shape a person can hold, so it is used on top of a hierarchy or a database, rarely alone. Prater's object mapping produces hypertext directly: nesting objects inside each other finds the cross-links, which, she argues, define contextual navigation (Prater 2015; IA2, section 1.5). A Help centre article that links to the task's other articles, and the route from an employee's record in Admin to the claims they made (IA2, section 5.3), are both hypertext.

### 2.5 · How real systems combine them

No surface of any size uses one structure. The combinations at Perqo (Perqo, fictional), each a structure chosen for one content set:

| Structure | Where at Perqo | Why this structure there |
|---|---|---|
| Hierarchy | the app's tab bar and the four categories under Benefits; perqo.com's top level; the Help centre's audience and task levels | few, distinct groups that people browse (Whitenton 2013) |
| Polyhierarchy | far members of a category listed in a second category (Deliverable B, R6) | ambiguous items with an assumed second place (Laubheimer 2018; IA3, C3) |
| Database | Admin's Employees and Approvals lists; the app's Claims and Purchases lists | many items of one kind, each with fields people sort and filter by |
| Faceted | the benefits catalogue (Deliverable B) | items described on several independent dimensions (Hearst 2006) |
| Hypertext | contextual routes: an employee's record to their claims; the Claims screen to the claim articles; article to article | routes that follow the relationships between objects (Prater 2015) |

## 3 · Faceted classification, controlled vocabularies and the taxonomy

### 3.1 · Metadata and the controlled vocabulary underneath

A database or faceted structure is only as good as the values in its fields. The Polar Bear book's chapter 10 opens with metadata, then controlled vocabularies (with sections on synonym rings, authority files and classification schemes), then thesauri, the three semantic relationships (equivalence, hierarchical, associative), preferred terms (with sections on term form, selection, definition and specificity), polyhierarchy and faceted classification (Rosenfeld, Morville and Arango 2015, ch. 10, headings). IA2 introduced the relationships and the US standard for controlled vocabularies, ANSI/NISO Z39.19 (IA2, section 1.2), and built a first slice of Perqo's vocabulary on them (IA2, section 5.3). This unit adds what IA2 did not cover: a faceted classification is a set of controlled vocabularies, one per facet, and every rule that keeps a vocabulary sound (one preferred term per concept, variants recorded, a defined scope) applies to each facet separately.

Heather Hedden's *The Accidental Taxonomist* is the practitioner's book-length guide. Its third edition shifts its emphasis from the traditional thesaurus model of terms to the SKOS model of concepts and adds a chapter on ontologies (publisher's description, Information Today, November 2022, [books.infotoday.com](https://books.infotoday.com/Ebooks/489_The-Accidental-Taxonomist-Third-Edition.htm)). The shift matters for a product team in one way: a concept has an identifier and several labels, which is exactly IA1's mapping of one data-model entity to a label per surface (IA1, section 2.4). The chapter contents of the third edition were not checked, so this unit cites the book for its scope and no chapter-level claim.

### 3.2 · What makes a facet sound

The rules below are the ones Deliverable B applies. Each is tied to its source; together they are this unit's synthesis, and they are practice, not a measured finding.

- **A facet answers one question about the item.** Hearst's facets are each "a different facet (dimension or feature type)", and her recipe example has four: dish type, ingredient type, cooking method and cuisine type (Hearst 2006). A facet that answers two questions ("type and price") cannot be combined freely with the others.
- **A facet is a property of the item.** A value that depends on who is asking or on another object (which client covers it, how much was spent) belongs to that other object. This is this unit's rule, from the database model: the field must be on the record it describes.
- **Each facet declares whether an item takes one value or several.** Hearst's items carry "many labels from the hierarchies" (Hearst 2006); whether a given facet allows several is a design decision, and at Perqo the benefit-category facet allows one, because money moves by it (section 2.2).
- **No value is shown that holds no items.** Faceted interfaces earn their preference partly by "avoiding empty results sets" (Hearst 2006).
- **Values are in the users' words, with the variants mapped.** Two people rarely choose the same word, and unlimited aliasing gives several-fold improvements (Furnas and others 1987); employees' words arrive in the search log (IA3, section 5.2).

### 3.3 · Taxonomy and folksonomy

IA2 gave Laubheimer's definition of a taxonomy, "A closed list of acceptable terms that are arranged hierarchically and are used to describe and classify content" (Laubheimer, "Taxonomy 101", Nielsen Norman Group, 3 July 2022, [nngroup.com/articles/taxonomy-101](https://www.nngroup.com/articles/taxonomy-101/); IA2, section 1.2). The word "closed" is the difference from a folksonomy. Thomas Vander Wal, who proposed the word on 24 July 2004 in a discussion on an information architects' mailing list, defines it: "Folksonomy is the result of personal free tagging of information and objects (anything with a URL) for one's own retrieval" (Thomas Vander Wal, "Folksonomy", vanderwal.net, 2 February 2007, [vanderwal.net/folksonomy.html](https://vanderwal.net/folksonomy.html); the author's own account). The Polar Bear book treats the phenomenon under "Social Classification" (2015, ch. 6, heading).

The differences, side by side:

| | Taxonomy | Folksonomy |
|---|---|---|
| Who assigns terms | the organisation, by rules | each person, for their own retrieval (Vander Wal 2007) |
| Term list | closed: a term is added by a decision (Laubheimer 2022) | open: any tag a person types |
| Variants | mapped to one preferred term | left as they are |
| Hierarchy | yes | none, beyond what patterns emerge |
| What it is good for | consistent filters, navigation, search, reporting | showing the words people actually use |

A folksonomy is not chaos. Scott Golder and Bernardo Huberman, studying a collaborative bookmarking system, "discovered regularities in user activity, tag frequencies, kinds of tags used" and "a remarkable stability in the relative proportions of tags within a given URL" ("Usage Patterns of Collaborative Tagging Systems", *Journal of Information Science* 32, no. 2, 2006, pp. 198 to 208, [doi.org/10.1177/0165551506062337](https://journals.sagepub.com/doi/10.1177/0165551506062337)). Stable tag proportions mean a folksonomy converges on the words a community uses for a thing, which is what a taxonomist needs for preferred and variant terms.

Perqo has no tagging (Perqo, fictional), and a benefits product should not hand its money-moving classification to free tags: a claim needs one category. It does have a folk vocabulary: the Help centre's search log, where employees type "refund", "allowance" and "gym" (IA3, section 5.2). The working arrangement this unit sets is a closed taxonomy fed by the open vocabulary: the search log and support's tickets are read for words, and those words enter the taxonomy as variant terms under Deliverable B's rules (R3 and R4).

## 4 · Object-oriented UX: the nouns before the pages

### 4.1 · The method

IA2 introduced Sophia V. Prater's object-oriented UX: "putting object design before procedural action design", with objects drawn from the user's mental model, in four steps: extract the objects from the nouns in the goals, define each object's core content, nest objects to find the cross-links, and rank each object's elements (Prater, "Object-Oriented UX", A List Apart, 20 October 2015, [alistapart.com/article/object-oriented-ux](https://alistapart.com/article/object-oriented-ux/); IA2, section 1.5). Her follow-up article takes the object map from the first as given, each object's core content, metadata and nested objects marked on it and ranked, and adds the actions in a workshop run object by object. Calls to action are "the main entry points to interaction flows", and "A CTA Inventory is just a fancy list of potential CTAs organized around your objects", which serves as "a bridge from big-picture OOUX to detailed interaction design"; the team brainstorms the actions object by object, then records for each one why it exists, who triggers it, where it lives, its complexity, its priority and its open questions (Prater, "OOUX: A Foundation for Interaction Design", A List Apart, 19 April 2016, [alistapart.com/article/ooux-a-foundation-for-interaction-design](https://alistapart.com/article/ooux-a-foundation-for-interaction-design/); practice). She later named the whole sequence: "ORCA stands for objects, relationships, calls to actions, and attributes" (interview by Thomas Betts, "Object-Oriented UX with Sophia Prater", InfoQ podcast, 6 May 2024, [infoq.com](https://www.infoq.com/podcasts/object-oriented-ux-sophia-prater/); interview, practice). The 2015 article defines content before nesting; the ORCA acronym puts relationships second. The order is a working order, and the figure follows the 2015 article with the 2016 CTA step added.

```viz
{"kind": "flow", "per_row": 2, "caption": "Flow: object mapping, the steps, with Perqo's first nouns; supports the decision on what a product holds before any page is drawn (section 4.1). Steps from Prater, 'Object-Oriented UX', A List Apart, 2015 (objects from nouns, core content, nesting, ranking) and 'OOUX: A Foundation for Interaction Design', A List Apart, 2016 (CTA inventory); ORCA from Prater's interview, InfoQ, 2024. Every step is tone 5 because the objects it finds are shared across Perqo's surfaces. Perqo is fictional.", "steps": [
 {"label": "Extract objects from the nouns in the goals", "note": "claim, allocation, policy, card, offer", "tone": 5},
 {"label": "Define core content and metadata", "note": "the attributes of each object", "tone": 5},
 {"label": "Nest objects in each other", "note": "the relationships, and the contextual routes", "tone": 5},
 {"label": "List the calls to action on each object", "note": "who triggers each, and where it lives", "tone": 5},
 {"label": "Rank attributes and calls to action", "note": "→ see interaction design (IA6)", "tone": 5}]}
```

### 4.2 · Finding Perqo's nouns

The nouns come from goal statements, one per role and surface. This unit's (Perqo, fictional), with the nouns marked:

| Role and surface | Goal | Nouns |
|---|---|---|
| Buyer, perqo.com | See what Perqo covers, read a **customer story**, send a **demo request** | customer story, demo request |
| HR manager, Admin | Create **employee groups**, give each a **policy** with its open categories and **covered items**, invite **employees**, approve **claims** over the limit | employee group, policy, catalogue item, employee, claim |
| Finance manager, Admin | Set each group's **budget** per category and period, read spend in **reports** | allocation (Admin: Budget), report |
| Employee, app | See my **balance** per category, pay with my **card**, claim back a **receipt**, see my **purchases**, read **notifications**, find **card offers** | allocation (app: Balance), card, claim, card payment (app: Purchase), notification, offer |
| Merchant | Accept the **card**, publish **offers** | merchant, offer, card payment |
| Support, perqo.com | Keep the **help articles** current | help article |

Two words in that table are labels and not objects: Budget and Balance are the same allocation (IA1, section 2.4), and Purchase is a card payment. The object map uses the data-model name as the title and each surface's label as a line, as IA2's notation requires (IA2, section 5.2). Receipt is a noun and stays an attribute of claim: this unit's test is whether anyone finds, lists or acts on the thing apart from its parent, and nobody browses receipts. Report is a noun and is left off the map, for the reason in section 4.3.

### 4.3 · Where it stops

Prater's own article names the first limit: "OOUX and a CTA Inventory will not help you design the interactions themselves" (Prater 2016). In the interview she places the method's strength in core concepts, "these concepts that don't change", and calls the question of where the map lives and which copy is the source of truth once the design changes "a tough question" (Prater, in Betts 2024). Four further limits show on Perqo, on this unit's reading.

- **Views are not objects.** Admin's Reports and the app's Home are arrangements of objects (allocations and transactions summed by group and period; balances and recent activity). Mapping them as objects puts a screen on the object map; they belong in the app map and the wireflows (IA6) and Admin's navigation model (IA7).
- **Rules and lifecycles sit outside it.** The map can give a claim a status attribute and a policy an auto-approve limit; it cannot show which claims wait for HR or what moves a claim from Submitted to Paid. Those are IA2's decision tree and state diagram (IA2, section 5.3), joined to the map in IA8.
- **Terms are not objects.** A benefit category has a screen in the app, but it is a value the allocation, the catalogue item and the offer are classified by. Modelled as an object, it would duplicate the taxonomy and invite two sources of truth. It stays in the taxonomy (Deliverable B), and the objects carry it as an attribute.
- **The nouns are a hypothesis.** Prater draws objects from the user's mental model (Prater 2015), and IA3 showed the gap between what the system holds and what people believe (IA3, section 2.3). A map written at a desk, as this one is, records the team's model. Its objects are labelled assumed until a test (IA11) confirms that people name and group them this way.

## 5 · Where an organisation system shows up

The same organisation decision appears in four places, and a reader of any IA artefact should be able to trace it through all four.

- **Navigation.** The top of a hierarchy becomes the global routes, its next level the local routes, and the object relationships the contextual routes (Rosenfeld, Morville and Arango 2015, ch. 8, headings; IA2, section 1.4 and the navigation model in section 5.3).
- **Filters.** Each facet becomes a filter, each value an option, and the rule against empty values becomes the rule that an option with no items is hidden or shown with zero (Hearst 2006). A single-valued facet suits a single-choice filter; a multi-valued one, a multi-choice filter.
- **Search.** The controlled vocabulary becomes the synonym list (Furnas and others 1987; IA3, D3), and the facets refine the results, the "conjunction of disjunctions" Hearst describes (Hearst 2006).
- **URLs.** A path that names groups records the classification. Tim Berners-Lee's advice, published by the W3C: "Cool URIs don't change", and "when you use a topic name in a URI you are binding yourself to some classification"; he lists subject, status, author and file extension among the things to leave out (Tim Berners-Lee, "Cool URIs Don't Change", W3C, 1998, [w3.org/Provider/Style/URI](https://w3.org/Provider/Style/URI); W3C style guidance). The Help centre's URLs, such as perqo.com/help/employees/claims/claim-a-receipt (IA2, section 5.3), bind the audience-then-task scheme into every address, so a change to the scheme is a change to the URLs. This unit's rule for Perqo (Perqo, fictional): catalogue pages and filters address values by their stable identifiers (Deliverable B), and a renamed or moved Help centre page keeps a redirect from its old address.

One decision traced through the four (Perqo, fictional): the benefit-category facet. Navigation: the four categories are the local routes inside Benefits. Filters: Admin's policy editor and the app's Card offers list filter by category. Search: "gym" in the Help centre maps to Fitness, under Health. URLs: a category is addressed by its identifier, CAT-HEA, so renaming its label does not break a link.

## Deliverable · A · The Perqo object map

*Face of this artefact (IA2, the notation sheet): object map of the whole Perqo product, with relationships and counts, so at IA2's object-relationship grade, at fidelity F2; decision: what Perqo holds, what each thing carries, what people can do to it and how the things relate, before any page is drawn; readers: engineering, product management, the client, content (for the labels); leaves out: rules and lifecycles (IA2, section 5.3; IA8), screens and views (IA5, IA6), Admin's permissions and its data-model mapping at F3 (IA7), the merchant side's own surface; owner: the IA designer; version 1, dated 3 November 2026; every object is assumed until tested (section 4.3); Perqo is fictional.*

**Fidelity and departure.** IA2's decision table gives the object map F1 in discovery and F2 in design, and puts the lines with counts in a separate grade, the object-relationship map, built for Perqo Admin in IA7 (IA2, Deliverable). The brief for this unit asks for relationships across the whole product, so this map draws them at F2, with counts in UML multiplicity notation (IA2, section 1.5). It departs from IA2's table there, and only there. It does not reach F3: data-model names are given where the course has set them, and IA7 adds the full mapping for Admin.

**What IA7 may do with it.** Add Admin objects, attributes, relationships and calls to action, and take the Admin part to F3. It renames nothing here: every object, attribute and relationship label below is meant to last, and a rename goes through the vocabulary first, with the old label kept as a variant (IA2, section 4).

### A.1 · Objects

Every object below is invented for the running example (Perqo, fictional). New facts are marked *new*; the others come from IA1 to IA3 and the register. Tones: 1 perqo.com only, 2 the merchant side, 3 the app only, 4 Admin only, 5 shared across surfaces (IA2, section 5.2).

| ID | Object (data-model name) | Tone | Admin | App | perqo.com | Merchant side | Attributes |
|---|---|---|---|---|---|---|---|
| O-01 | client *new* | 5 | Company, in Settings *new* | not shown | Customers (as customer stories) | not shown | name; contract start date *new* |
| O-02 | admin user *new* | 4 | Admins, in Settings *new* | not shown | not shown (signs in through Sign in) | not shown | name; work email; role (HR manager or finance manager) |
| O-03 | employee group | 5 | Employee group | not shown | Teams and groups | not shown | name |
| O-04 | policy | 5 | Policy | not shown; its effect shows as open categories and approval rules | Policies | not shown | open categories; auto-approve limit; covered items *new* |
| O-05 | employee | 5 | Employees | Profile, in Account | not shown | not shown | name; work email |
| O-06 | allocation | 5 | Budget | Balance | Benefits budget | not shown | category; period; amount; spent *new*; remaining *new* |
| O-07 | transaction, type claim | 5 | Claim | Claim | Claims | not shown | amount; category; receipt; status (Submitted, Approved, Rejected, Paid); date submitted *new* |
| O-08 | transaction, type card payment | 5 | Card payment | Purchase | Card payments | the sale *new* | amount; date; merchant; category *new* |
| O-09 | card *new* | 5 | not set (IA7) | Card | Perqo card | accepted at the till | last four digits; status (Active, Frozen) *new* |
| O-10 | notification *new* | 3 | not set (IA7) | Notifications, in Account | not shown | not shown | message; date; the claim it is about |
| O-11 | merchant *new* | 2 | not shown | merchant name on a Purchase *new* | not shown | the merchant | name; benefit category (one narrower term, assigned by Perqo) *new*; accepts the Perqo card |
| O-12 | offer *new* | 5 | not shown | Card offers (as-is: Perks and Discover; IA3's proposed label) | not shown | published by the merchant | title; discount; valid until; catalogue item; merchant |
| O-13 | catalogue item *new* | 5 | Covered items, in Policies *new* | What's covered, on each category screen | not shown | not shown | ID; name; the four facet values (Deliverable B); variant terms |
| O-14 | help article | 1 | not shown | Help with claims and Help open it | Help centre article | not shown | ID; title; URL; audience; topic; owner; format; last modified (IA2, section 5.3) |
| O-15 | customer story *new* | 1 | not shown | not shown | Customer stories | not shown | title; URL; client |
| O-16 | demo request *new* | 1 | not shown | not shown | Book a demo | not shown | name; work email; company; number of employees *new* |

The facts set here, in prose (Perqo, fictional). Finance sets the allocation for every employee in a group at once, by category and period, which is what IA1 called setting "budgets per employee group and period"; the object is still one allocation per employee, category and period (IA1, section 2.4). Each merchant that accepts the Perqo card is assigned one narrower term of the benefit-category facet by Perqo, and a card payment at that merchant spends from the employee's allocation in that term's category. The Perqo card can be frozen and unfrozen by the employee. A notification is about one claim. An offer is for one catalogue item, published by one merchant. The catalogue's content is owned by Perqo's content team; a policy covers items from it. Book a demo creates a demo request that the sales team follows up; demo requests are not in Admin.

### A.2 · Relationships

| ID | From | Relationship | To | Counts (from, to) |
|---|---|---|---|---|
| R-01 | client | has | admin user | 1, 1..* |
| R-02 | client | has | employee group | 1, 1..* |
| R-03 | employee group | follows | policy | 1, 1 |
| R-04 | employee group | contains | employee | 1, 1..* |
| R-05 | employee | holds | allocation | 1, 1..* |
| R-06 | policy | opens the categories of | allocation | 1, 0..* |
| R-07 | policy | covers | catalogue item | 0..*, 0..* |
| R-08 | employee | submits | transaction, type claim | 1, 0..* |
| R-09 | transaction, type claim | is checked against | policy | 0..*, 1 |
| R-10 | transaction, type claim | spends from | allocation | 0..*, 1 |
| R-11 | employee | holds | card | 1, 0..1 |
| R-12 | card | is used for | transaction, type card payment | 1, 0..* |
| R-13 | transaction, type card payment | spends from | allocation | 0..*, 1 |
| R-14 | merchant | takes | transaction, type card payment | 1, 0..* |
| R-15 | transaction, type claim | triggers | notification | 1, 0..* |
| R-16 | merchant | publishes | offer | 1, 0..* |
| R-17 | offer | is for | catalogue item | 0..*, 1 |
| R-18 | help article | explains | policy, allocation, claim, card, catalogue item | 0..*, 0..* |
| R-19 | customer story | is about | client | 0..1, 1 |
| R-20 | demo request | leads to | client | 0..*, 0..1 |

R-03, R-04, R-05, R-08, R-09 and R-10 are IA2's (IA2, section 5.3); R-06 follows from IA1's rule that HR switches categories on per group (IA1, Deliverable); the rest are new. R-11's 0..1 allows an employee whose card has not been issued.

### A.3 · Calls to action

Each object's calls to action, with who triggers each and where it lives, in the columns of Prater's CTA inventory (Prater 2016). Complexity and priority are left to IA6, which designs the flows.

| Object | Call to action | Who | Where |
|---|---|---|---|
| client | -> edit company details *new* | admin user (role not set: IA7) | Admin, Settings |
| admin user | -> add *new* | admin user (role not set: IA7) | Admin, Settings |
| employee group | -> create *new*; -> invite employees | HR manager | Admin, Employees |
| policy | -> edit; -> add covered items *new* | HR manager | Admin, Policies |
| employee | -> invite; -> move to group | HR manager | Admin, Employees |
| employee | -> view profile | employee | App, Account |
| allocation | -> set for a group | finance manager | Admin, Budgets |
| allocation | -> see balance | employee | App, Home and Benefits |
| transaction, type claim | -> submit | employee | App, Claims (New claim) |
| transaction, type claim | -> approve; -> reject | HR manager | Admin, Approvals |
| transaction, type card payment | -> view | employee | App, Card (Purchases) |
| transaction, type card payment | -> view in a report | finance manager | Admin, Reports |
| card | -> view card details; -> freeze; -> unfreeze *new* | employee | App, Card |
| notification | -> open | employee | App, Account (Notifications) |
| merchant | -> publish offer | merchant | merchant side (surface not set) |
| offer | -> view | employee | App, Card offers |
| catalogue item | -> add item; -> edit item *new* | Perqo content team | catalogue (internal; surface not set) |
| help article | -> read | anyone | perqo.com, Help centre |
| help article | -> update | support | perqo.com, Help centre |
| customer story | -> read | buyer | perqo.com, Customers |
| demo request | -> submit | buyer | perqo.com, Book a demo |
| demo request | -> follow up *new* | sales | outside Perqo's surfaces |

### A.4 · The map, drawn

Split in three figures, as IA2's rule "split rather than cram" requires (IA2, section 4), with "→ see" lines where an object continues in another figure. The first holds the setup that HR and finance do in Admin: client, admin users, employee groups, policies, employees and allocations (R-01 to R-06).

```viz
{"kind": "objects", "caption": "Object map, figure 1 of 3, setup: the objects HR and finance configure, with attributes, calls to action and counts (UML multiplicity), F2; supports the decision on what Perqo holds before any page is drawn (Deliverable A). Tones as in IA2, section 5.2: 5 shared, 4 Perqo Admin only. Shared objects carry the data-model name as title and a 'Surface: Label' line per surface. Lines read left to right on a level line, top to bottom otherwise. Perqo is fictional; R-03 to R-05 from IA2, section 5.3; the rest set in Deliverable A; object-first method from Prater, A List Apart, 2015 and 2016.", "objects": [
 {"id": "client", "title": "client", "tone": 5, "attrs": ["Admin: Company", "perqo.com: Customers", "name", "contract start date"], "actions": ["-> edit company details"]},
 {"id": "admin", "title": "admin user", "tone": 4, "attrs": ["Admin: Admins", "name", "work email", "role"], "actions": ["-> add"]},
 {"id": "group", "title": "employee group", "tone": 5, "attrs": ["Admin: Employee group", "perqo.com: Teams and groups", "name"], "actions": ["-> create (HR)", "-> invite employees (HR)"]},
 {"id": "policy", "title": "policy", "tone": 5, "attrs": ["Admin: Policy", "app: not shown", "perqo.com: Policies", "open categories", "auto-approve limit", "covered items"], "actions": ["-> edit (HR)", "-> add covered items (HR)"]},
 {"id": "employee", "title": "employee", "tone": 5, "attrs": ["Admin: Employees", "app: Profile", "name", "work email"], "actions": ["-> invite (HR)", "-> move to group (HR)", "-> view profile (employee)", "→ see figure 2"]},
 {"id": "alloc", "title": "allocation", "tone": 5, "attrs": ["Admin: Budget", "app: Balance", "perqo.com: Benefits budget", "category", "period", "amount", "spent", "remaining"], "actions": ["-> set for a group (finance)", "-> see balance (employee)", "→ see figure 2"]}],
 "rows": [["client", "admin"], ["group", "policy"], ["employee", "alloc"]],
 "links": [
  {"from": "client", "to": "admin", "label": "has", "from_card": "1", "to_card": "1..*"},
  {"from": "client", "to": "group", "label": "has", "from_card": "1", "to_card": "1..*"},
  {"from": "group", "to": "policy", "label": "follows", "from_card": "1", "to_card": "1"},
  {"from": "group", "to": "employee", "label": "contains", "from_card": "1", "to_card": "1..*"},
  {"from": "employee", "to": "alloc", "label": "holds", "from_card": "1", "to_card": "1..*"},
  {"from": "policy", "to": "alloc", "label": "opens the categories of", "from_card": "1", "to_card": "0..*"}]}
```

The second holds spending: the employee's card, card payments and claims, the allocation they spend from, the merchant that takes card payments, the policy a claim is checked against and the notifications a claim triggers (R-08 to R-15).

```viz
{"kind": "objects", "caption": "Object map, figure 2 of 3, spending: the objects an employee spends and claims with, and the merchant that takes card payments, F2; supports the decision on what the app and the merchant side hold and how money moves between objects (Deliverable A). Tones as in IA2, section 5.2: 5 shared, 3 the Perqo app only, 2 the merchant side. A triangle by a label marks a label that reads right to left. Perqo is fictional; R-08 to R-10 from IA2, section 5.3; the rest set in Deliverable A; counts in UML multiplicity notation.", "objects": [
 {"id": "employee", "title": "employee", "tone": 5, "attrs": ["→ see figure 1"]},
 {"id": "card", "title": "card", "tone": 5, "attrs": ["app: Card", "perqo.com: Perqo card", "last four digits", "status"], "actions": ["-> view card details", "-> freeze", "-> unfreeze"]},
 {"id": "merchant", "title": "merchant", "tone": 2, "attrs": ["name", "benefit category", "accepts the Perqo card"], "actions": ["-> publish offer", "→ see figure 3"]},
 {"id": "claim", "title": "transaction, type claim", "tone": 5, "attrs": ["Admin: Claim", "app: Claim", "perqo.com: Claims", "amount", "category", "receipt", "status", "date submitted"], "actions": ["-> submit (employee)", "-> approve (HR)", "-> reject (HR)"]},
 {"id": "alloc", "title": "allocation", "tone": 5, "attrs": ["→ see figure 1"]},
 {"id": "payment", "title": "transaction, type card payment", "tone": 5, "attrs": ["Admin: Card payment", "app: Purchase", "perqo.com: Card payments", "amount", "date", "merchant", "category"], "actions": ["-> view (employee)", "-> view in a report (finance)"]},
 {"id": "notif", "title": "notification", "tone": 3, "attrs": ["app: Notifications", "message", "date"], "actions": ["-> open"]},
 {"id": "policy", "title": "policy", "tone": 5, "attrs": ["→ see figure 1"]}],
 "rows": [["employee", "card", "merchant"], ["claim", "alloc", "payment"], ["notif", "policy", null]],
 "links": [
  {"from": "employee", "to": "card", "label": "holds", "from_card": "1", "to_card": "0..1"},
  {"from": "employee", "to": "claim", "label": "submits", "from_card": "1", "to_card": "0..*"},
  {"from": "claim", "to": "alloc", "label": "spends from", "from_card": "0..*", "to_card": "1"},
  {"from": "payment", "to": "alloc", "label": "spends from", "from_card": "0..*", "to_card": "1", "dir": "to"},
  {"from": "card", "to": "payment", "label": "is used for", "from_card": "1", "to_card": "0..*"},
  {"from": "merchant", "to": "payment", "label": "takes", "from_card": "1", "to_card": "0..*"},
  {"from": "claim", "to": "notif", "label": "triggers", "from_card": "1", "to_card": "0..*"},
  {"from": "claim", "to": "policy", "label": "is checked against", "from_card": "0..*", "to_card": "1"}]}
```

The third holds the catalogue, the merchant side and perqo.com: the policy's covered items, the offers merchants publish for them, the help articles, and the customer stories and demo requests that relate to clients (R-07, R-16 to R-20).

```viz
{"kind": "objects", "caption": "Object map, figure 3 of 3, catalogue, merchants and perqo.com, F2; supports the decision on how the benefits catalogue, merchant offers and website content attach to the product's objects (Deliverable A). Tones as in IA2, section 5.2: 5 shared, 2 the merchant side, 1 perqo.com only. A triangle by a label marks a label that reads right to left or bottom to top. Perqo is fictional; every object and relationship set in Deliverable A; the help article's attributes from IA2, section 5.3, with audience added; the catalogue item's facets from Deliverable B.", "objects": [
 {"id": "policy", "title": "policy", "tone": 5, "attrs": ["→ see figure 1"]},
 {"id": "item", "title": "catalogue item", "tone": 5, "attrs": ["Admin: Covered items", "app: What's covered", "ID", "name", "facet values", "variant terms"], "actions": ["-> add item (content team)", "-> edit item (content team)"]},
 {"id": "offer", "title": "offer", "tone": 5, "attrs": ["app: Card offers", "title", "discount", "valid until"], "actions": ["-> view (employee)"]},
 {"id": "merchant", "title": "merchant", "tone": 2, "attrs": ["→ see figure 2"]},
 {"id": "article", "title": "help article", "tone": 1, "attrs": ["ID", "title", "URL", "audience", "topic", "owner", "format", "last modified", "→ see claim, allocation, card, catalogue item"], "actions": ["-> read", "-> update (support)"]},
 {"id": "story", "title": "customer story", "tone": 1, "attrs": ["title", "URL"], "actions": ["-> read (buyer)"]},
 {"id": "client", "title": "client", "tone": 5, "attrs": ["→ see figure 1"]},
 {"id": "demo", "title": "demo request", "tone": 1, "attrs": ["name", "work email", "company", "number of employees"], "actions": ["-> submit (buyer)", "-> follow up (sales)"]}],
 "rows": [["policy", "item", "offer", "merchant"], ["article", null, null, null], ["story", "client", "demo", null]],
 "links": [
  {"from": "policy", "to": "item", "label": "covers", "from_card": "0..*", "to_card": "0..*"},
  {"from": "offer", "to": "item", "label": "is for", "from_card": "0..*", "to_card": "1", "dir": "to"},
  {"from": "merchant", "to": "offer", "label": "publishes", "from_card": "1", "to_card": "0..*", "dir": "to"},
  {"from": "article", "to": "policy", "label": "explains", "from_card": "0..*", "to_card": "0..*", "dir": "to"},
  {"from": "story", "to": "client", "label": "is about", "from_card": "0..1", "to_card": "1"},
  {"from": "demo", "to": "client", "label": "leads to", "from_card": "0..*", "to_card": "0..1", "dir": "to"}]}
```

**What the map hands on.** IA6 designs the app's flows from the calls to action on claim, card, allocation, offer and notification. IA7 extends the Admin objects (client, admin user, employee group, policy, employee, allocation, claim, card payment) to F3 with permissions and model names. IA8 joins the claim's status attribute to its state diagram and decision tree, and the policy's auto-approve limit to the rule that reads it.

## Deliverable · B · The Perqo benefits catalogue taxonomy

*Face of this artefact (IA2, the notation sheet): faceted taxonomy of the Perqo benefits catalogue, at fidelity F2 with F3's stable identifiers on every facet, value and item; decision: how catalogue items are classified, filtered, searched and addressed, and what it takes to add a value; readers: content (owner), engineering (filters, search synonyms, identifiers), support (variant terms), sales (the preferred terms on perqo.com), product management; leaves out: which client covers which item (that is the policy, Deliverable A, R-07), prices, approval (decided by the policy's limit), and the full item list beyond the twelve sample items; owner: Perqo content team; version 1, dated 3 November 2026; Perqo is fictional.*

**What the catalogue is (Perqo, fictional).** The benefits catalogue is Perqo's list of the things an employee can spend benefits on, each a catalogue item (O-13). A client's policy covers items from it (R-07). The catalogue's classification is the one place an item's benefit category is decided; the example client's placings in IA3 (gym membership under Health, Fitness, and so on) are the catalogue's (IA3, section 3.3). Its uses: the examples on each category screen in the app (IA3's C2 fix), the variant terms for the Help centre search (IA3's D3 fix), the covered-items picker in Admin's Policies, the filter on Card offers, and the category of each merchant (O-11).

**Fidelity and departure.** IA2's decision table gives a taxonomy F2 in design and F3 when built into metadata (IA2, Deliverable). This one is F2, and departs in one respect: every facet, value and item already carries a stable identifier, an F3 element, because IA5 and DD-IA3 will cite them and IA2's rule is that identifiers are kept when things move (IA2, section 4).

### B.1 · Facets

| ID | Facet | The question it answers | Values per item | Shape | Used by |
|---|---|---|---|---|---|
| F-CAT | Benefit category | Which allocation pays for it? | exactly one narrower term (and so one category) | hierarchy, two levels | app Benefits, Admin Policies, Card offers, merchants, claim category |
| F-PAY | Usual way to pay | Can the employee usually pay with the Perqo card, or do they claim it back? | one or both | flat | app What's covered; Help centre |
| F-TYP | Purchase type | How is it bought? | one or more | flat | app What's covered; Admin Policies filter |
| F-CHN | Channel | Where is it bought? | one or both | flat | app What's covered; Card offers filter |

Considered and not made facets, with the reason (section 3.2): approval (decided by the policy's auto-approve limit and the amount, so it belongs to the policy); price (varies by merchant); which clients cover the item (a relationship, R-07); merchant (a relationship, through offers, R-17).

### B.2 · Values

The benefit-category facet. The four categories and their narrower terms are IA1's and IA2's, with IA2's variant terms; the identifiers and the variants marked *new* are set here.

| ID | Preferred term | Broader term | Variant terms | Scope note |
|---|---|---|---|---|
| CAT-HEA | Health | none (top level) | wellbeing | physical and mental health |
| CAT-HEA-FIT | Fitness | Health | gym, sport *new* | exercise: memberships, classes, entries |
| CAT-HEA-THE | Therapy | Health | counselling *new* | sessions with a therapist |
| CAT-LEA | Learning | none (top level) | education, training | learning anything, work-related or not |
| CAT-LEA-COU | Courses | Learning | none: "class" is excluded (rule R4) | taught courses, online or in person |
| CAT-LEA-BOO | Books | Learning | e-books *new* | books in any format |
| CAT-MOB | Mobility | none (top level) | transport, commuting | getting around |
| CAT-MOB-PUB | Public transport | Mobility | train, bus *new* | tickets and passes for public transport |
| CAT-MOB-BIK | Bike | Mobility | cycling *new* | bikes, their equipment and repair |
| CAT-MEA | Meals | none (top level) | food | food and eating |
| CAT-MEA-RES | Restaurants | Meals | eating out *new* | meals bought ready to eat |
| CAT-MEA-GRO | Groceries | Meals | supermarket *new* | food bought to cook |

```viz
{"kind": "tree", "caption": "Taxonomy: the benefit-category facet of the Perqo benefits catalogue, two levels, with value identifiers, F2; supports the decision on which category and allocation an item belongs to (Deliverable B). Every box is tone 5 because the terms are shared across Admin, the app and perqo.com. Categories and narrower terms from IA1, Deliverable, and IA2, section 5.3; identifiers set in Deliverable B; relationships per Rosenfeld, Morville and Arango, 4th ed., 2015, ch. 10. Perqo is fictional.", "root": {"label": "Benefit category (F-CAT)", "tone": 5, "children": [
 {"label": "Health (CAT-HEA)", "tone": 5, "children": [{"label": "Fitness (CAT-HEA-FIT)", "tone": 5}, {"label": "Therapy (CAT-HEA-THE)", "tone": 5}]},
 {"label": "Learning (CAT-LEA)", "tone": 5, "children": [{"label": "Courses (CAT-LEA-COU)", "tone": 5}, {"label": "Books (CAT-LEA-BOO)", "tone": 5}]},
 {"label": "Mobility (CAT-MOB)", "tone": 5, "children": [{"label": "Public transport (CAT-MOB-PUB)", "tone": 5}, {"label": "Bike (CAT-MOB-BIK)", "tone": 5}]},
 {"label": "Meals (CAT-MEA)", "tone": 5, "children": [{"label": "Restaurants (CAT-MEA-RES)", "tone": 5}, {"label": "Groceries (CAT-MEA-GRO)", "tone": 5}]}]}}
```

The flat facets (all new here):

| ID | Facet | Preferred term | Variant terms | Scope note |
|---|---|---|---|---|
| PAY-CRD | Usual way to pay | Perqo card | card | merchants selling it usually accept the Perqo card |
| PAY-CLM | Usual way to pay | Claim | refund, reimbursement, expense (IA2) | usually paid another way and claimed back |
| TYP-SUB | Purchase type | Subscription | membership | paid again each period |
| TYP-SIN | Purchase type | Single purchase | one-off | paid once, used once or kept |
| TYP-PAS | Purchase type | Pass | ticket, season ticket | prepaid for a period or a number of uses |
| CHN-INP | Channel | In person | in store | bought at a place |
| CHN-ONL | Channel | Online | internet | bought on a website or app |

### B.3 · The catalogue items, classified

Twelve sample items (Perqo, fictional). The six from IA3 keep the categories IA3 gave them; the other six are new. "Also listed under" is the polyhierarchy of display: it adds a route, while the home category still decides which allocation pays (rule R6); each one is IA3's assumed second place, untested.

| ID | Item | Benefit category | Narrower term | Usual way to pay | Purchase type | Channel | Also listed under |
|---|---|---|---|---|---|---|---|
| BI-001 | Gym membership | Health | Fitness | Perqo card, Claim | Subscription | In person | none |
| BI-002 | Yoga class | Health | Fitness | Perqo card, Claim | Single purchase, Pass | In person, Online | Learning (assumed) |
| BI-003 | Therapy session | Health | Therapy | Claim | Single purchase | In person, Online | none |
| BI-004 | Coding course | Learning | Courses | Perqo card, Claim | Single purchase | Online, In person | none |
| BI-005 | Cookery course | Learning | Courses | Perqo card, Claim | Single purchase | In person | Meals (assumed) |
| BI-006 | Book | Learning | Books | Perqo card, Claim | Single purchase | In person, Online | none |
| BI-007 | Train pass | Mobility | Public transport | Perqo card, Claim | Pass | In person, Online | none |
| BI-008 | Bike helmet | Mobility | Bike | Perqo card, Claim | Single purchase | In person, Online | Health (assumed) |
| BI-009 | Bike repair | Mobility | Bike | Perqo card | Single purchase | In person | none |
| BI-010 | Restaurant meal | Meals | Restaurants | Perqo card | Single purchase | In person | none |
| BI-011 | Groceries | Meals | Groceries | Perqo card | Single purchase | In person, Online | none |
| BI-012 | Swimming pool entry | Health | Fitness | Perqo card, Claim | Single purchase, Pass | In person | none |

```viz
{"kind": "matrix", "caption": "Facet grid: twelve Perqo catalogue items against the catalogue's facets, F2; supports the decision on how each item is filtered, searched and shown, and where a far member gets a second route (Deliverable B). Rows tone 5, shared terms; tone 3 marks a cross-listing shown in the app, assumed and untested (IA3, section 3.3; rule R6). Faceted structure from Hearst, CACM 49(4), 2006; polyhierarchy from Laubheimer, NN/g, 2018. Perqo is fictional; the first six items' categories from IA3, section 3.3, the rest from Deliverable B.", "cols": ["Category", "Narrower term", "Usual way to pay", "Purchase type", "Channel", "Also listed under"], "rows": [
 {"label": "Gym membership", "tone": 5, "cells": ["Health", "Fitness", "Perqo card, Claim", "Subscription", "In person", null]},
 {"label": "Yoga class", "tone": 5, "cells": ["Health", "Fitness", "Perqo card, Claim", "Single purchase, Pass", "In person, Online", {"mark": "Learning (assumed)", "tone": 3}]},
 {"label": "Therapy session", "tone": 5, "cells": ["Health", "Therapy", "Claim", "Single purchase", "In person, Online", null]},
 {"label": "Coding course", "tone": 5, "cells": ["Learning", "Courses", "Perqo card, Claim", "Single purchase", "Online, In person", null]},
 {"label": "Cookery course", "tone": 5, "cells": ["Learning", "Courses", "Perqo card, Claim", "Single purchase", "In person", {"mark": "Meals (assumed)", "tone": 3}]},
 {"label": "Book", "tone": 5, "cells": ["Learning", "Books", "Perqo card, Claim", "Single purchase", "In person, Online", null]},
 {"label": "Train pass", "tone": 5, "cells": ["Mobility", "Public transport", "Perqo card, Claim", "Pass", "In person, Online", null]},
 {"label": "Bike helmet", "tone": 5, "cells": ["Mobility", "Bike", "Perqo card, Claim", "Single purchase", "In person, Online", {"mark": "Health (assumed)", "tone": 3}]},
 {"label": "Bike repair", "tone": 5, "cells": ["Mobility", "Bike", "Perqo card", "Single purchase", "In person", null]},
 {"label": "Restaurant meal", "tone": 5, "cells": ["Meals", "Restaurants", "Perqo card", "Single purchase", "In person", null]},
 {"label": "Groceries", "tone": 5, "cells": ["Meals", "Groceries", "Perqo card", "Single purchase", "In person, Online", null]},
 {"label": "Swimming pool entry", "tone": 5, "cells": ["Health", "Fitness", "Perqo card, Claim", "Single purchase, Pass", "In person", null]}],
 "legend": [{"mark": "tone 5", "means": "a catalogue term, shared across surfaces", "tone": 5}, {"mark": "tone 3", "means": "a cross-listing in the app, assumed", "tone": 3}]}
```

### B.4 · The rules for adding a value

A value is added, renamed or retired only by the content team, as a proposed change reviewed with support and engineering (IA2, section 4: mark changes as proposed until agreed). Each rule carries its source.

- **R1 · The value answers its facet's question.** A proposed value is tested against the question in B.1; a value that answers another question is a new facet or nothing (Hearst 2006; section 3.2).
- **R2 · In F-CAT, values do not overlap.** A new narrower term must not hold items an existing term already holds, because every item has exactly one narrower term and a claim reads one category's balance (IA3, section 2.3). An item that seems to belong to two is placed in one and cross-listed under R6.
- **R3 · The preferred term is the employee's word, at the basic level where it can be.** It is checked against the Help centre search log and support's tickets before it is adopted (Nielsen 2006 and Rosch and others 1976, both as applied in IA3, sections 3.1 and 4.2; Farrell 2017, IA3, section 5.2).
- **R4 · Every value carries its variants, and each variant points to one value.** Variants go to the Help centre search as synonyms (Furnas and others 1987; IA3, D3). A word that would pull an item into another category is not made a variant: "class" is excluded from Courses because "yoga class" is a Fitness item (IA3, section 3.3).
- **R5 · A value is added only when items hold it.** It needs at least two catalogue items at the time it is added (Perqo, fictional: the content team's threshold), and a value that loses its last item is hidden from filters, so no option leads to an empty result (Hearst 2006).
- **R6 · A second listing needs evidence, and points to the home.** An item is listed under a second category only when a test shows people look for it there (Laubheimer 2018); until then it is marked "assumed" (IA3, C3). The listing names the home category ("Cookery course: covered under Learning", IA3, C3) and never changes which allocation pays.
- **R7 · F-CAT keeps two levels.** A new narrower term is added beside its siblings; no third level is added, because each level is one more choice that must carry scent, and depth slowed people in every study in section 2.1 (Zaphiris 2000; Larson and Czerwinski 1998; Whitenton 2013).
- **R8 · A new top-level category is a product decision.** It creates a new allocation for every employee in every group that opens it (Deliverable A, R-05 and R-06), so it goes to product management, finance and the client, not only to the content team (this unit's rule, from the object map).
- **R9 · Identifiers are stable.** A value keeps its identifier when it is renamed or moved; a retired value's identifier is never reused; a rename keeps the old term as a variant (IA2, section 4). URLs and filters address values by identifier (section 5; Berners-Lee 1998).
- **R10 · A new facet passes the not-a-facet test.** A property that depends on the policy, the amount, the merchant or the client is not a facet of the catalogue (section 3.2; B.1).

**What IA5 and DD-IA3 take.** IA5 builds the perqo.com content inventory and sitemap on these identifiers, with the Help centre's articles tagged with F-CAT values; IA6 puts the catalogue items on each category screen as its examples (IA3, C2). DD-IA3 takes the controlled vocabulary further, from these preferred and variant terms. Neither renames a value except under R9.

## Sources

- Berners-Lee, Tim. "Cool URIs Don't Change". W3C, 1998 (W3C style guidance). [w3.org/Provider/Style/URI](https://w3.org/Provider/Style/URI)
- Betts, Thomas. "Object-Oriented UX with Sophia Prater" (podcast interview). InfoQ, 6 May 2024. [infoq.com/podcasts/object-oriented-ux-sophia-prater](https://www.infoq.com/podcasts/object-oriented-ux-sophia-prater/) (interview; practice).
- Cooper, Alan, Robert Reimann, David Cronin and Christopher Noessel. *About Face: The Essentials of Interaction Design*. 4th ed. Wiley, 2014. Ch. 13, "Metaphors, Idioms, and Affordances".
- Czerwinski, Mary P., and Kevin Larson. "Cognition and the Web: Moving from Theory to Web Design". Microsoft Research, undated chapter manuscript. [microsoft.com](https://www.microsoft.com/en-us/research/wp-content/uploads/2002/01/HFandtheWebChapter.pdf)
- Dix, Alan. "Menu Breadth: Not a Case of Miller's 7+/-2". Companion page to Dix, Finlay, Abowd and Beale, *Human-Computer Interaction*, 3rd ed., 2003 (page dated 2010). [hcibook.com/e3/online/menu-breadth](https://hcibook.com/e3/online/menu-breadth) (textbook author's page).
- Furnas, George W., Thomas K. Landauer, Louis M. Gomez and Susan T. Dumais. "The Vocabulary Problem in Human-System Communication". *Communications of the ACM* 30, no. 11 (1987): 964 to 971. [cacm.acm.org](https://cacm.acm.org/research/the-vocabulary-problem-in-human-system-communication)
- Golder, Scott A., and Bernardo A. Huberman. "Usage Patterns of Collaborative Tagging Systems". *Journal of Information Science* 32, no. 2 (2006): 198 to 208. [journals.sagepub.com/doi/10.1177/0165551506062337](https://journals.sagepub.com/doi/10.1177/0165551506062337)
- Hearst, Marti A. "Clustering versus Faceted Categories for Information Exploration". *Communications of the ACM* 49, no. 4 (2006): 59 to 61. [flamenco.ischool.berkeley.edu/papers/cacm06.pdf](https://flamenco.ischool.berkeley.edu/papers/cacm06.pdf)
- Hedden, Heather. *The Accidental Taxonomist*. 3rd ed. Information Today, November 2022. Publisher's description at [books.infotoday.com](https://books.infotoday.com/Ebooks/489_The-Accidental-Taxonomist-Third-Edition.htm).
- Larson, Kevin, and Mary Czerwinski. "Web Page Design: Implications of Memory, Structure and Scent for Information Retrieval". *CHI 98*, ACM, 1998, pp. 25 to 32. [microsoft.com/en-us/research](https://www.microsoft.com/en-us/research/publication/web-page-design-implications-memory-structure-scent-information-retrieval/)
- Laubheimer, Page. "Polyhierarchies Improve Findability for Ambiguous IA Categories". Nielsen Norman Group, 13 May 2018. [nngroup.com/articles/polyhierarchy](https://www.nngroup.com/articles/polyhierarchy/)
- Laubheimer, Page. "Taxonomy 101: Definition, Best Practices, and How It Complements Other IA Work". Nielsen Norman Group, 3 July 2022. [nngroup.com/articles/taxonomy-101](https://www.nngroup.com/articles/taxonomy-101/)
- Laubheimer, Page. "3 Common IA Mistakes (that Are All Due to Low Information Scent)". Nielsen Norman Group, 16 April 2023. [nngroup.com/articles/3-ia-mistakes](https://www.nngroup.com/articles/3-ia-mistakes/)
- "Menu Structure and Ordering of Menu Selection: Independent or Interactive Effects?" *ACM SIGCHI Bulletin* 18, no. 2 (October 1986), abstract. [unpaywall.org/10.1145/15683.1044100](https://unpaywall.org/10.1145%2F15683.1044100) (authors not checked; cited for its report of Card 1982 and Snowberry and others 1983).
- Prater, Sophia V. "Object-Oriented UX". A List Apart, 20 October 2015. [alistapart.com/article/object-oriented-ux](https://alistapart.com/article/object-oriented-ux/) (practice).
- Prater, Sophia V. "OOUX: A Foundation for Interaction Design". A List Apart, 19 April 2016. [alistapart.com/article/ooux-a-foundation-for-interaction-design](https://alistapart.com/article/ooux-a-foundation-for-interaction-design/) (practice).
- Rosenfeld, Louis, Peter Morville and Jorge Arango. *Information Architecture: For the Web and Beyond*. 4th ed. O'Reilly, 2015. Chs 6, 8 and 10. Ch. 6 at [oreilly.com](https://oreilly.com/library/view/information-architecture-4th/9781491913529/ch06.html); ch. 10 at [oreilly.com](https://www.oreilly.com/library/view/information-architecture-4th/9781491913529/ch10.html).
- Satija, M. P. "Colon Classification (CC)". *ISKO Encyclopedia of Knowledge Organization*, version 2.0, 2017. [isko.org/cyclo/colon_classification](https://isko.org/cyclo/colon_classification)
- Vander Wal, Thomas. "Folksonomy". vanderwal.net, 2 February 2007. [vanderwal.net/folksonomy.html](https://vanderwal.net/folksonomy.html) (the author's own account; practice).
- Whitenton, Kathryn. "Flat vs. Deep Website Hierarchies". Nielsen Norman Group, 10 November 2013. [nngroup.com/articles/flat-vs-deep-hierarchy](https://www.nngroup.com/articles/flat-vs-deep-hierarchy/)
- Woods, D. Ben. "Book Review: Information Anxiety". UXmatters, 18 March 2019. [uxmatters.com](https://uxmatters.com/mt/archives/2019/03/book-review-information-anxiety.php) (review; cited for its description of Wurman 1989).
- Wurman, Richard Saul. *Information Anxiety*. Doubleday, 1989.
- Yee, Ka-Ping, Kirsten Swearingen, Kevin Li and Marti Hearst. "Faceted Metadata for Image Search and Browsing". *CHI 2003*, ACM, 2003. [unpaywall.org/10.1145/642611.642681](https://unpaywall.org/10.1145%2F642611.642681)
- Zaphiris, Panayiotis. "Depth Vs Breadth in the Arrangement of Web Links". *Proceedings of the Human Factors and Ergonomics Society 44th Annual Meeting*, 2000, pp. 139 to 144. [ktisis.cut.ac.cy](https://ktisis.cut.ac.cy/bitstream/20.500.14279/2872/6/Zaphiris2000-Depth_Vs_Breath.pdf) (also the source for Miller 1981, Kiger 1984 and Snowberry, Parkinson and Sisson 1983 as reported).
- Cited through the filed units, for claims made there: Farrell 2017; Katz and Byrne 2003; Nielsen 2006; Rosch and others 1976; Rosch and Mervis 1975; Spencer 2006 (IA3, Sources); NISO Z39.19-2005 (R2010); Object Management Group, UML 2.5.1 (IA2, Sources).

## Unsure list

- Rosenfeld, Morville and Arango 2015, chs 6 and 10: only the section headings were seen; the glosses of exact and ambiguous schemes and of the database model are this unit's, from knowledge of the chapter. At the fresh check the three exact and four ambiguous schemes, with Hybrids in a section of their own, were confirmed in the 3rd edition's published excerpt; the database model's gloss was not checked against the text.
- Cooper and others 2014: the chapter number (13) and title "Metaphors, Idioms, and Affordances" were confirmed at the fresh check from a bookseller's contents listing; the argument is paraphrased, not re-read.
- Miller 1981, Kiger 1984 and Snowberry, Parkinson and Sisson 1983 are cited as reported by Zaphiris 2000; the originals were not seen.
- Landauer and Nachbar 1985 is cited as reported by Dix 2010; Card 1982 as reported in a 1986 SIGCHI Bulletin abstract whose authors were not checked.
- Zaphiris 2000: the matching of the five mean times to their structures was made from a text extraction of the paper's table, whose column headings were garbled; the fresh check confirmed the matching against the paper's discussion.
- Larson and Czerwinski 1998: the structures (8 by 8 by 8, 16 by 32, 32 by 16 over 512 documents) are from the authors' later chapter manuscript, not from the CHI paper itself.
- Prater 2015: the four steps and the quotation were taken from IA2's reading of the article; the fresh check re-read the article and confirmed both.
- Hedden 2022: the third edition's chapter contents were not seen; only the publisher's description.
- Yee and others 2003: authors from knowledge; the figures from the abstract on the DOI page. Dix's page is tied to the 3rd edition of his textbook by its URL; its own date is its copyright line, 2010. Woods's review: its title, "Book Review: Information Anxiety", confirmed at the fresh check.
- Not checked: Spencer, A Practical Guide to Information Architecture, 2nd ed. (the page redirected and was not followed); Google's documentation on faceted navigation URLs (page body not returned); neither is cited.
