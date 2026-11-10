---
code: DD-IA3
title: "Deep dive: taxonomy and governance at scale"
course: ux · IA · Information Architecture
model: Opus 5.5
written: 2026-11-10
search: off
---

# DD-IA3 · Deep dive: taxonomy and governance at scale

IA4 built the benefits catalogue taxonomy of Perqo (Perqo, fictional), the flexible-benefits platform this course runs on, with its four facets, twelve benefit-category values and the rules R1 to R10 for adding one. IA9 set who may change the IA and how: the routing rule, the change-control flow, the decision log and the version rule. IA10 named the twelve functions that touch the IA and the forums where each meets it, FO-01 to FO-09, and left one function, localisation, with no forum until a second language is added. This unit takes those three to scale. It covers what an enterprise taxonomy is and how it differs from a navigation hierarchy; the metadata and shared vocabulary that product, content, data and engineering must hold in common; who owns the IA, the taxonomy and each label; change control for a taxonomy and for the IA; localisation and the labels that do not survive translation; the failure modes of a structure at scale and how to detect them; and the documented practice of three organisations that publish their taxonomy or its governance, read against their own publications on 10 November 2026. The deliverable is the Perqo governance model, the taxonomy change-request process in full, and a controlled-vocabulary starter of the twenty terms every surface must share.

Search was off for this unit: it is written from the field's standard works and the filed units, and the web was used only to verify the standards' numbers and dates on their publishers' pages and the documented practice of the organisations cited. Every page so read is dated "read 10 November 2026" where it is cited.

Every figure uses IA2's notation (IA2, section 5.2 and the notation sheet). This unit draws four of its six tones. Tone 5, shared, carries most figures, because a taxonomy and its governance sit under every surface. Tone 3, the Perqo app, carries the navigation column of the first figure, whose examples are the app's. Tone 2, anything outside Perqo, carries GOV.UK's figures. Tone 6, a stop, marks a proposed term that is declined.

What the filed units hand on, and where this unit uses it:

| From | What it hands on | Used in |
|---|---|---|
| IA2, sections 1.2, 3 and 4; the notation sheet; the decision table's controlled-vocabulary row, "§5.3 vocabulary · DD-IA3" | the controlled vocabulary as an artefact; fault 5 (labels that drift); rename through the vocabulary; the face | sections 1, 2 and 6; Deliverable C |
| IA4, sections 3 and 5; Deliverable B and "What IA5 and DD-IA3 take" | the taxonomy, its facets, preferred and variant terms, R1 to R10; the controlled vocabulary taken further, nothing renamed except under R9 | sections 1, 4, 6 and 7; Deliverables B and C |
| IA5, sections 3.3 and 5.3; Deliverables A and C | identifiers as the key every language version shares; the localisation column (modules M-10, M-11, M-24, M-25 by market); T-14's synonyms per language; the URL form in other languages; which markets come next | section 5; Deliverable B, B.4 |
| IA7, sections 6.2 and 6.3; IA8, D.1 | Evans's ubiquitous language; the model name as the team's word and surface labels as recorded translations; the shared objects and their names | section 2; Deliverable C |
| IA9, section 4 and Deliverable D; "What later units take" | the routing rule, the flow, the log's format and statuses, the version rule, as the base to extend for languages and markets | sections 3 and 4; Deliverables A and B |
| IA10, sections 2.3 and A.2; the open-questions table; "What later units take" | FO-01 to FO-09; TP-05, localisation, dormant, "none yet (DD-IA3)"; DL-011 to DL-015 | section 3; Deliverable A |
| IA11, sections 6.4 and 7 | the confidence ladder, C0 to C5; TP-05 held at C0 with DD-IA3 named | Deliverable A, A.6 |
| IA12, sections 3.4 and 4.4; Deliverables C and D; "What later units take" | the stakeholder map; the escalation procedure; the decision log template with "decide at"; DL-017 to DL-019; the register's process part, left unfilled | Deliverables A and B |
| DD-IA1, section 2 and "What later units take" | GOV.UK's taxonomy principles beside R1 to R10; GOV.UK's governance costs; the Stripe and Airbnb localisation observations; eBay's versioned category trees per market | sections 3 to 7 |
| DD-IA2, Deliverables A, B and D | the measurement model as the forums' reads, M-07 and M-12 to M-14 per language; the business-case template and its number rule; DL-021 and DL-022 | Deliverables A and B |
| Register, "Free: ... (DD-IA3)" | localisation's forum; the URL form in other languages; T-14's synonyms per language; which markets and languages come next | Deliverables A and B; "Perqo facts set by this unit" |

## 1 · What an enterprise taxonomy is, and how it differs from a navigation hierarchy

### 1.1 · The taxonomy, and the vocabularies around it

IA2 gave the course its definition. Page Laubheimer's is "A closed list of acceptable terms that are arranged hierarchically and are used to describe and classify content", and he places it backstage: the taxonomy maps the concepts used to describe content, where the IA structure maps where content lives and the navigation is the frontstage layer people see ("Taxonomy 101", Nielsen Norman Group, 3 July 2022, [nngroup.com, taxonomy 101](https://www.nngroup.com/articles/taxonomy-101/); IA2, section 1.2). The US standard for controlled vocabularies puts the taxonomy in a family: ANSI/NISO Z39.19 "Presents guidelines and conventions for the contents, display, construction, testing, maintenance, and management of monolingual controlled vocabularies", and focuses on vocabularies "used for the representation of content objects in knowledge organization systems including lists, synonym rings, taxonomies, and thesauri" (NISO, *ANSI/NISO Z39.19-2005 (R2010)*, publication page, [niso.org, Z39.19](https://niso.org/publications/ansiniso-z3919-2005-r2010), read 10 November 2026; standard). Rosenfeld, Morville and Arango give the same family a chapter, with synonym rings, authority files, classification schemes and thesauri, the three semantic relationships (equivalence, hierarchical, associative) and preferred terms, and say of it: "In many large metadata-driven products, controlled vocabularies have become the glue that holds the systems together" (*Information Architecture: For the Web and Beyond*, 4th ed., O'Reilly, 2015, ch. 10; IA2, section 1.2; IA4, section 3.1).

An **enterprise taxonomy**, in this course's words, is one taxonomy that every system and surface of an organisation classifies by, so that a term means the same thing wherever it is stored, filtered, searched, reported or shown. The definition is this unit's; it names what the sources above describe at the scale of one product. Heather Hedden's *The Accidental Taxonomist* is the practitioner's book-length guide, and its third edition shifts its emphasis from the thesaurus model of terms to the SKOS model of concepts (publisher's description, Information Today, November 2022, [books.infotoday.com, Accidental Taxonomist](https://books.infotoday.com/Ebooks/489_The-Accidental-Taxonomist-Third-Edition.htm), read 10 November 2026; IA4, section 3.1). The shift matters at scale: a concept carries an identifier and several labels, so one concept can be named differently by surface and by language without becoming two concepts.

Perqo's benefit-category facet, F-CAT, is enterprise in this sense (Perqo, fictional). It is used by the app's Benefits, Admin's Policies, Card offers, each merchant's category and each claim's category (IA4, Deliverable B, B.1); by the Help centre's articles and the customer stories, which carry F-CAT tags (IA5, section 3.3); and by Admin's report Spend by category (IA7, section 4.6). Money moves by it: a claim reads one category's balance (IA3, section 2.3).

### 1.2 · How it differs from a navigation hierarchy

Laubheimer's point that a taxonomy "need not match the order people browse in" (IA2, section 1.2, after Laubheimer 2022) is the first difference, and Perqo shows the rest. The app's navigation hierarchy is five tabs, Home, Benefits, Claims, Card and Account, with the four categories one level below Benefits (IA6, Deliverable B). The taxonomy holds twelve F-CAT values, four categories and eight narrower terms, with their variant terms (IA4, B.2), and three flat facets besides. The eight narrower terms are not places a person navigates to: they appear as groups inside each category's What's covered list (IA6, Deliverable B, B.3). The flat facets appear in no navigation at all, only as the facts shown about each item and as filters (IA4, B.1). And perqo.com's Help centre is navigated by audience and then by task, while its articles are classified by F-CAT (IA2, section 5.3; IA5, section 3.3): one taxonomy, several navigation hierarchies, none of them a copy of it.

The two also change differently, are owned differently and are addressed differently. A change to a tab or a top level of a navigation sends the structure to a test before and after (IA9, Deliverable C, RV-11). A change to a taxonomy value reaches every item tagged with it, every filter, every search synonym and every address built on it, which is why IA4's R9 keeps identifiers stable and keeps a renamed term as a variant (IA4, B.4). The IA designer owns the canonical IA artefacts, the navigation among them; the benefits taxonomy is the content team's (IA9, section 4.1). And a navigation node is addressed by its screen or page identifier (A-2.1 is a category screen; IA6, Deliverable B), a taxonomy value by its own identifier (CAT-HEA; IA4, B.2).

The figure sets the two side by side, one row per difference, with Perqo's case in each cell. Answers: what it is about, and what else means the same; where a person can go from here. Built for: tags, filters, search, reports; people moving on one surface. Size: every term: 12 F-CAT values and their variants; what fits a screen: 5 tabs, 4 categories. Shape: facets, a hierarchy inside each; a tree per surface, with routes across it. Changes by: a DL entry; identifiers kept; a release; a test before and after. Owner: content team; IA designer. Surfaces: backstage, under every surface; one surface each. Addressed by: identifier: CAT-HEA; screen or page: A-2.1. The taxonomy column is tone 5, shared; the navigation column is tone 3, because its examples are the app's. In the legend, tone 5 is "the taxonomy: shared, under every surface" and tone 3 "the navigation: the Perqo app's examples".

```viz
{"kind": "matrix", "caption": "Enterprise taxonomy against navigation hierarchy: eight differences, each with Perqo's case; supports the decision on which of the two a proposed change touches, and so who decides it (section 1.2). Taxonomy as backstage and navigation as frontstage from Laubheimer, 'Taxonomy 101', NN/g, 2022 (through IA2, section 1.2); the taxonomy's facets, values, identifiers and owner from IA4, Deliverable B; the app's tabs and screen identifiers from IA6, Deliverable B; the test before and after from IA9, Deliverable C, RV-11; owners from IA9, section 4.1. Rows tone 5; the taxonomy column tone 5, shared; the navigation column tone 3, the Perqo app. Perqo is fictional.", "cols": ["Enterprise taxonomy", "Navigation hierarchy"], "rows": [
 {"label": "Answers", "tone": 5, "cells": [{"mark": "what it is about, and what else means the same", "tone": 5}, {"mark": "where a person can go from here", "tone": 3}]},
 {"label": "Built for", "tone": 5, "cells": [{"mark": "tags, filters, search, reports", "tone": 5}, {"mark": "people moving on one surface", "tone": 3}]},
 {"label": "Size", "tone": 5, "cells": [{"mark": "every term: 12 F-CAT values and their variants", "tone": 5}, {"mark": "what fits a screen: 5 tabs, 4 categories", "tone": 3}]},
 {"label": "Shape", "tone": 5, "cells": [{"mark": "facets, a hierarchy inside each", "tone": 5}, {"mark": "a tree per surface, with routes across it", "tone": 3}]},
 {"label": "Changes by", "tone": 5, "cells": [{"mark": "a DL entry; identifiers kept", "tone": 5}, {"mark": "a release; a test before and after", "tone": 3}]},
 {"label": "Owner", "tone": 5, "cells": [{"mark": "content team", "tone": 5}, {"mark": "IA designer", "tone": 3}]},
 {"label": "Surfaces", "tone": 5, "cells": [{"mark": "backstage, under every surface", "tone": 5}, {"mark": "one surface each", "tone": 3}]},
 {"label": "Addressed by", "tone": 5, "cells": [{"mark": "identifier: CAT-HEA", "tone": 5}, {"mark": "screen or page: A-2.1", "tone": 3}]}],
 "legend": [{"mark": "tone 5", "means": "the taxonomy: shared, under every surface", "tone": 5}, {"mark": "tone 3", "means": "the navigation: the Perqo app's examples", "tone": 3}]}
```

### 1.3 · The standards for thesauri and knowledge organisation systems

Four standards govern this ground: Z39.19, cited in section 1.1, and the three below. Each is cited as its publisher gives it; none of the publishers' pages read for this unit lists clauses, so no clause is cited.

- **ISO 25964-1:2011**, *Information and documentation — Thesauri and interoperability with other vocabularies — Part 1: Thesauri for information retrieval*, edition 1, August 2011. Its abstract: it "gives recommendations for the development and maintenance of thesauri intended for information retrieval applications", "is applicable to monolingual and multilingual thesauri", "also provides a data model and recommended format for the import and export of thesaurus data", and anticipates the needs of other applications "among its recommendations for thesaurus management". The page says it "was last reviewed and confirmed in 2022" and marks it "to be revised" (ISO, [iso.org, ISO 25964-1](https://www.iso.org/standard/53657.html), read 10 November 2026; standard).
- **ISO 25964-2:2013**, *Part 2: Interoperability with other vocabularies*, edition 1, March 2013, confirmed in 2023. It "gives recommendations for the establishment and maintenance of mappings between multiple thesauri, or between thesauri and other types of vocabularies" (ISO, [iso.org, ISO 25964-2](https://www.iso.org/standard/53658.html?browse=tc), read 10 November 2026; standard).
- **SKOS**, *Simple Knowledge Organization System Reference*, W3C Recommendation, 18 August 2009. Section 5 defines the lexical labels, preferred, alternative and hidden, with two integrity conditions that matter here: S13, the three label properties "are pairwise disjoint properties", and S14, "A resource has no more than one value of `skos:prefLabel` per language tag". Section 6 defines `skos:notation`, "used to assign a notation as a typed literal", a code such as an identifier. Section 7 gives "seven properties in SKOS for associating notes with concepts", among them the scope, change and history notes. Section 8 relates concepts: `skos:broader` and `skos:narrower` "assert a direct hierarchical link", `skos:related` "an associative link". Section 10 holds the mapping properties between concept schemes (W3C, [w3.org, SKOS Reference](https://www.w3.org/TR/2009/REC-skos-reference-20090818), read 10 November 2026, the first 100,000 characters of the page; standard).

Z39.19's title limits it to monolingual vocabularies, which is why a product that adds a language reaches for ISO 25964-1, whose scope names multilingual thesauri.

What a product team takes from the three, on this unit's reading, is a data model more than a procedure. A concept has a code (SKOS's notation; IA4's CAT-HEA), one preferred label per language (S14), any number of alternative labels (IA4's variant terms), broader and narrower links (F-CAT's two levels), notes that record its scope and its history, and mappings to other schemes. One Perqo fact does not fit SKOS's core directly: Perqo gives one concept a preferred term per surface in the same language, Budget in Admin and Balance in the app for the allocation (IA1, section 2.4), and S14 allows one preferred label per language tag. The vocabulary in Deliverable C therefore records each surface's label in its own column; a team that exports it to SKOS has to decide where those columns go, and that decision is left to engineering.

## 2 · Metadata and the shared vocabulary across product, content, data and engineering

A taxonomy reaches the product through metadata: the fields on each record that hold its terms. IA4 traced one organisation decision through four places, navigation, filters, search and URLs (IA4, section 5). At scale there are two more readers, data and engineering, and each reads the same terms for its own purpose.

- **Product** reads the terms as scope. A new top-level category creates an allocation for every employee in every group that opens it, so it is a product decision (IA4, B.4, R8).
- **Content** reads them as labels. Each concept has a preferred term on each surface and its variants (IA2, section 5.3; IA8, D.1's shared-objects table).
- **Data** reads them as dimensions. Admin's Spend by category groups transactions by F-CAT (IA7, section 4.6); product analytics record each screen and page view by identifier (IA9, section 6.3); IA10 proposed that an event take the model name and the state entered (IA10, section 2.2).
- **Engineering** reads them as names in the model. IA7 took Eric Evans's ubiquitous language as the rule that holds the model and the words together: "Use the model as the backbone of a language", and "Recognize that a change in the language is a change to the model" (Evans, *Domain-Driven Design Reference*, Domain Language, 2015; IA7, section 6.2). Evans asks for one language within a bounded context. IA7 read Perqo's three labels for one allocation as compatible with that on one rule: the model name is the team's word, and the surface labels are recorded translations of it, "never a second concept" (IA7, section 6.2). IA8 named the catalogue and its taxonomy as a candidate bounded context of its own, owned by the content team and joined to the rest at R-07 and R-17 (IA8, D.1).

Lisa Welchman's subtitle is *Digital Governance by Design*, and her publisher's page defines the discipline: "Digital governance is a discipline that focuses on establishing clear accountability for digital strategy, policy, and standards" (Rosenfeld Media, *Managing Chaos*, publisher's page, FAQ, [rosenfeldmedia.com, Managing Chaos](https://rosenfeldmedia.com/?p=187514), read 10 November 2026). In her chapter on standards she writes: "Your standards are the tactical manifestation of your strategy" (Welchman, "Stopping the Infighting About Digital Standards", A List Apart, 3 March 2015, an excerpt of *Managing Chaos*, ch. 5, [alistapart.com, digital standards](https://alistapart.com/article/stopping-the-infighting-about-digital-standards/), read 10 November 2026; practice). IA9 already called the IA a standard in her sense, a shared structure many teams build on (IA9, section 4.1). The shared vocabulary is the most widely read part of that standard: support reads it in tickets, sales in demos, engineering in code, finance in reports.

On this unit's reading, "by design" means the vocabulary is built so that each of the four readers finds its own column in one record, and none keeps a private list. One row per concept: its identifier, its model name, its preferred term on each surface (and, once a second language exists, in each language), its variants, its definition, and its owner. That is the form of Deliverable C. A product that keeps four lists, one per function, keeps four vocabularies, and IA2's fifth fault, one thing with two names and no mapping, is the condition it will be in (IA2, section 3).

## 3 · Ownership: who owns the IA, the taxonomy and each label

### 3.1 · Welchman's framework

Welchman's book is practice: an author's account from consulting work, with case studies and no measurement. Its contents, as the publisher lists them, run from "The Basics of Digital Governance" through "Your Digital Team: Where They Are and What They Do", "Digital Strategy: Aligning Expertise and Authority", "Staying on Track with Digital Policy", "Stopping the Infighting About Digital Standards" and "Five Digital Governance Design Factors" to "Getting it Done", "The Decision to Govern Well" and three case studies, multinational business-to-business, government and higher education (publisher's page, read 10 November 2026). Two of those chapters were read for this unit, chapter 5 in the A List Apart excerpt and chapter 7 in a sample chapter (Welchman, "Managing Chaos: Digital Governance by Design", UXmatters, 4 May 2015, [uxmatters.com, sample chapter](https://www.uxmatters.com/mt/archives/2015/05/managing-chaos-digital-governance-by-design.php), read 10 November 2026; practice). Chapters 2 and 6, where the publisher's titles show the book treats where the team sits and the factors that shape a framework, were not read, and this unit names none of the organisational models they may describe.

What the two read chapters set out is a framework, and its parts are these. Governance is accountability for three things: strategy, policy and standards (publisher's FAQ). "Your digital governance framework is just that—a framework for decision making" (Welchman 2015, ch. 7). Standards have a steward: "An organization's digital standards steward's job is to establish and maintain a standards-compliant environment", and "In the best of cases, the organizational standards steward is not an enforcer" (Welchman 2015, ch. 5). Authority is named in advance: "knowing who has the authority to define standards saves time" (same). Compliance has four conditions, standards "defined and documented", "disseminated", "implemented", and "measured and managed", the measuring done "in a consistent and automated way", with the expectation that "you'll never have 100% compliance" (same). And the failure she names is one of telling: "Frequently, resources aren't told that a standard has changed until the standard is violated" (same). The chapter names a "core digital team" and an "extended digital team", and asks that standards be written down so the extended team can follow them (same).

### 3.2 · What each part is owned by at Perqo

Halvorson and Rach make governance one of content strategy's four components, the way key decisions about content are made (*Content Strategy for the Web*, 2nd ed., New Riders, 2012, ch. 9; IA1, section 2.3; IA9, section 4.1). The filed units already answer most of the ownership question for Perqo (Perqo, fictional); one part was left split, and one was left empty.

- **The IA.** The IA designer owns the canonical artefacts and the decision log; the IA review decides changes that touch a rule or two surfaces, rename a label or retire an identifier; product management signs off rule and two-surface changes (IA9, section 4.1 and D.1).
- **The taxonomy.** The content team owns it and decides its values, as a proposed change reviewed with support and engineering under R1 to R10; a new top-level category also goes to product management, finance and the client (IA4, B.4; IA9, D.1).
- **The vocabulary, left split.** IA9's workflow names the content team as owner of "labels, vocabulary" when the words are put in place (IA9, Deliverable A, W-13) and of the vocabulary review (RV-07), while its section 4.1 gives the IA designer every canonical artefact other than the taxonomy. A vocabulary with two owners has none in Welchman's sense: nobody is its steward. DL-024 proposes the content team as the vocabulary's steward, with the IA designer keeping the model-name column with engineering.
- **Each label, left empty.** No filed unit names who answers for one term. Deliverable C gives each term an owner by one rule: **a term is owned by the owner of the artefact that defines it, and a term whose meaning is a rule or a contract term is owned by product management**. An object's term is the IA designer's, because the object map defines it (IA4, A; IA9, section 4.1); a taxonomy term is the content team's (IA4, B); a claim's status, the auto-approve limit and the period are product management's, because a change to any of them changes a rule's outcome, which product management signs off (IA9, D.1), and the period's end is G-7, which product management owns (IA12, B.6). The owner keeps the definition true and is asked first about a change; the decider is still the one D.1 names.
- **Each language, left empty.** Localisation has no forum until a second language is added (IA10, section 2.3, TP-05). Deliverable A gives it one, FO-10, and a role, the language owner, both dormant until then.

Mapped onto Welchman's framework, on this unit's reading: strategy is leadership's and product management's (which markets, which categories); policy is the routing rule and the consultation rules (IA9, D.1; DL-014, proposed); standards are the notation, the vocabulary, the taxonomy rules and the version rule. The core team is the IA designer, the content team and, once there is a second language, localisation; every other function applies the standards and sits in the extended team. The figure of decision rights is in Deliverable A, A.2.

### 3.3 · One organisation's documented split: GOV.UK

The Government Digital Service publishes how GOV.UK's topic taxonomy is owned. Its principles say: "GDS manages the topic taxonomy based on feedback from a variety of sources"; publishers can "suggest new topics, or changes to existing topics"; and "Publishing teams are responsible for making sure the content they publish is tagged accurately" (GDS, "GOV.UK Taxonomy principles", published 13 June 2019, updated 9 September 2026, [gov.uk, taxonomy principles](https://www.gov.uk/government/publications/govuk-topic-taxonomy-principles/govuk-taxonomy-principles), read 10 November 2026; publisher's documentation). In 2019 a GOV.UK product manager described how the work was divided when the dedicated taxonomy team paused for other work: "taxonomy change requests will be handled by content support", "improvements to content tagging quality and the structure of the taxonomy will sit in the navigation team", and "improvements to the tagging interface will form part of the publishing workflow team's work"; the same post says "We know that we need to do more to make it easier for publishers to tag their content accurately" (Si Stephens-Manassiev, "An update on the GOV.UK taxonomy", Inside GOV.UK, 12 February 2019, [insidegovuk.blog.gov.uk, taxonomy update](https://insidegovuk.blog.gov.uk/2019/02/12/an-update-on-the-gov-uk-taxonomy/), read 10 November 2026; practice, a maker's account). DD-IA1 read the same post as GOV.UK's documented governance cost (DD-IA1, section 2).

Three roles are separated in that account: who handles a request, who owns the structure, and who owns the tool that applies it. They map onto Perqo without a new function: the content team handles requests and owns the structure (IA4, B.4), and engineering owns the tool, the covered-items picker in Admin's Policies and the catalogue's own surface, which IA4 left unset (IA4, A.3). What the GOV.UK account adds is the warning in its last sentence: the people who tag are not the people who own the taxonomy, and accuracy is theirs to keep. At Perqo the taggers are support (Help centre articles) and marketing (customer stories) (IA5, Deliverable A), the content team (catalogue items; IA4, A.3), and Perqo itself, which assigns each merchant its narrower term (IA4, A.1); so the drift checks of section 6 read their tags as well as the taxonomy.

## 4 · Change control for a taxonomy and for the IA

### 4.1 · What a taxonomy change has that an IA change does not

IA9's change control covers every change to the IA: raise, log as proposed, check the impact by identifier, J- row, X- crossing and DT- rule, route, decide, change the vocabulary first, change the artefacts and re-stamp each face, tell the informed functions, close as applied (IA9, D.2). A taxonomy change runs the same steps and adds one: migration. Changing a value changes nothing on its own; every item, article, story, offer, merchant and synonym that carries the old value has to be moved, and each address built on it redirected. The two standards whose scope covers maintenance say so in their titles and abstracts, Z39.19's "maintenance, and management" and ISO 25964-1's "development and maintenance" and "thesaurus management" (section 1.3), and SKOS gives a concept notes to carry its change and history (section 1.3).

The documented practice shows three ways an organisation runs migration and tells its readers.

- **GOV.UK changes topics one at a time.** "The taxonomy is flexible": topics can be added "if a new subject area emerges", removed "if they become redundant", renamed, merged or split (GDS, taxonomy principles, read 10 November 2026). When policies and policy areas were retired in 2019 they were "removed and redirected to equivalent topics", the front-end links to them removed, and subscribers to their email alerts sent one email suggesting equivalent topics (Stephens-Manassiev 2019). GOV.UK's developer documentation says the topics, "taxons" in code, are stored as content items that "can be in either draft state or published", managed in the Content Tagger application by users with the "GDS Editor" permission (GOV.UK Developer Documentation, "How the topic taxonomy works", last updated 4 May 2022, [docs.publishing.service.gov.uk, taxonomy](https://docs.publishing.service.gov.uk/manual/taxonomy.html), read 10 November 2026; platform documentation, which warns that it "may be out of date").
- **eBay versions a tree per market.** "Approximately 20 eBay marketplaces each use a default category tree", which is "subject to change as categories are added, expanded, consolidated, or removed (users are notified of any changes)"; a client retrieves the tree's version and compares "the categoryTreeVersion field to the one you have cached" (eBay Developers Program, "Finding categories for a listing", [developer.ebay.com, sell categories](https://www.developer.ebay.com/api-docs/sell/static/metadata/sell-categories.html), read 10 November 2026; platform documentation). DD-IA1 read the same page on the same day (DD-IA1, "What later units take").
- **Shopify releases the whole taxonomy on a calendar.** Its standard product taxonomy, "an open-source comprehensive, global standard for product classification", is versioned by date, "in sync with Shopify's API release schedule", with "a stable release every 3 months at most, at the beginning of the quarter"; anyone may "Submit a taxonomy tree change request" or a pull request "against the source-of-truth files"; and "mappings" are "rules that can be used to convert between categories and attributes" (Shopify, product-taxonomy repository, README, [github.com, Shopify product taxonomy](https://github.com/Shopify/product-taxonomy), read 10 November 2026, version badge 2026-10; vendor documentation).

The three differ in who reads the taxonomy. GOV.UK's readers are its own publishers and the public, and it changes topic by topic. eBay's and Shopify's readers include outside software that stores the categories, so each publishes a version a client can compare, and Shopify publishes mappings from one version to the next. Perqo's readers today are its own surfaces, its functions and its merchants' category assignments; no software outside Perqo reads the taxonomy (Perqo, fictional, set here; the catalogue's own surface is unset, IA4, A.3). So Perqo keeps IA9's version rule for the taxonomy's face, a new version when a change breaks a citation and a dated amendment otherwise (IA9, section 4.4), and does not adopt a release calendar. If an outside reader is added, such as a merchant integration, the versioned release eBay and Shopify document is the form to adopt; that is recorded as an open condition in Deliverable B.

### 4.2 · A term's lifecycle

The operations a taxonomy change can make are six: add, rename, move, merge, split and retire (the list GDS publishes, with move added for a value that changes its parent). Each moves a term through a lifecycle, which the figure draws (Perqo, fictional; built on IA4's R9 and IA9's log statuses). A term starts **Proposed**, logged as a DL entry and in no filter. It becomes **Active** when it is accepted and applied: it is in tags, filters, search and URLs. A rename leaves it Active, its old label kept as a variant (R9), which the notation draws as an arrow from the state back to itself (IA2, section 5.2). A merge, a split or a retirement, once accepted, makes it **Deprecated**: no new item is tagged with it, its items are migrating, and its addresses redirect. When the last item has migrated it is **Retired**, and its identifier is never reused (R9). A proposal refused is **Declined**, kept with its reason (IA9, section 4.3). Retired and Declined are end states; Declined is tone 6, a stop, and every other state is tone 5, shared. The figure's states carry these notes: Proposed, "a DL entry; in no filter"; Active, "tags, filters, search, URLs"; Deprecated, "no new tags; items migrating; addresses redirect"; Declined, "kept, with its reason"; Retired, "identifier never reused". Its transitions read "accepted and applied" (Proposed to Active), "decided: no" (Proposed to Declined), "rename: old label kept as a variant" (Active to itself), "merge, split or retire accepted" (Active to Deprecated) and "last item migrated" (Deprecated to Retired). A move changes a value's parent; it is not drawn as a state, because the term stays Active, and under IA9's rule it makes a new version (IA9, section 4.4).

```viz
{"kind": "states", "per_row": 3, "caption": "State diagram: the lifecycle of a term in Perqo's taxonomy and vocabulary; supports the decision on what a term may be used for at each point of a change (section 4.2). Operations from GDS, 'GOV.UK Taxonomy principles' (read 10 November 2026), with move added; stable identifiers and the renamed term kept as a variant from IA4, Deliverable B, R9; Proposed and Declined from IA9, section 4.3; the arrow to itself from IA2, section 5.2. Tone 5 shared; tone 6 a stop, a proposal refused. Perqo is fictional.", "start": "proposed", "states": [
 {"id": "proposed", "label": "Proposed", "note": "a DL entry; in no filter", "tone": 5},
 {"id": "active", "label": "Active", "note": "tags, filters, search, URLs", "tone": 5},
 {"id": "deprecated", "label": "Deprecated", "note": "no new tags; items migrating; addresses redirect", "tone": 5},
 {"id": "declined", "label": "Declined", "note": "kept, with its reason", "tone": 6, "end": true},
 {"id": "retired", "label": "Retired", "note": "identifier never reused", "tone": 5, "end": true}],
 "transitions": [
 {"from": "proposed", "to": "active", "label": "accepted and applied"},
 {"from": "proposed", "to": "declined", "label": "decided: no"},
 {"from": "active", "to": "active", "label": "rename: old label kept as a variant"},
 {"from": "active", "to": "deprecated", "label": "merge, split or retire accepted"},
 {"from": "deprecated", "to": "retired", "label": "last item migrated"}]}
```

### 4.3 · Change control for the IA, at scale

The IA's own change control stays IA9's, and three things change when the IA holds several languages and markets. The impact step counts language versions: a renamed label is one change in the log and one change per language on the screens, and IA9's "applied" means every place is changed (IA9, section 4.3), so a change is not applied while any live language still shows the old label. The told step reaches functions per language: a change sales hears of at FO-04 in one market is heard by each market's sales. And the version rule holds per artefact, in every language alike: a translated label added where none existed adds without breaking, a dated amendment; a translated label renamed breaks citations in that language's articles and support scripts, a new version (IA9, section 4.4). Deliverable B writes the process in full.

## 5 · Localisation, and the labels that do not survive translation

### 5.1 · One key for every language

IA5 set the rule this section builds on. perqo.com is published in English only, and each language version of a page must list itself and every other version, or, in Google's documentation as IA5 cites it, "If two pages don't both point to each other, the tags will be ignored" ("Localized Versions of your Pages", Google Search Central, as cited in IA5, section 5.3; vendor documentation, checked 3 November 2026). So the site needs one key the same in every language, and the inventory's identifier is it: S-1.4.2 is the Learning page in every language, "whatever its title and its slug become"; identifiers carry no words of any language (IA5, section 5.3).

DD-IA1 brought two observations of real products to this rule, both of 10 November 2026. Stripe's English (UK) documentation writes the API value `cancelled` where its unlocalised pages write `canceled`: an identifier that took a language's spelling. And a web search returned Airbnb's help article on pending reservations at the same number, 2810, on seven country domains: a stable key across language versions (DD-IA1, "What later units take"; only the airbnb.com page was read there). The first is the fault IA5's rule exists to prevent; the second is the rule kept.

Perqo's own identifiers raise one honest question. CAT-HEA is built from the first letters of an English word. It is a code, SKOS's notation (section 1.3), never shown as a label, and R9 forbids changing it; so it stays as it is in every language, and nobody translates "cat-hea" (Perqo, fictional). The rule for new identifiers is IA5's, without exception: no word of any language in an identifier created from today. The twelve existing F-CAT codes are kept under R9, because changing them would break every address and filter built on them (IA4, section 5).

### 5.2 · What does not survive translation

A label is a short string, and short strings change most in translation. The W3C's internationalisation article "Text size in translation" says that "text will normally expand, but note carefully how the smaller the source message, the higher the likely translation length", and reports IBM's average expansion for English into European languages: 200 to 300% for text up to 10 characters, 180 to 200% for 11 to 20, falling to 130% over 70 characters ("IBM in their Guidelines to design global solutions", as the article attributes them). Its example is a label: "views" becomes "visualizzazioni" in Italian, "a ratio of 3" (W3C Internationalization, "Text size in translation", [w3.org, text size in translation](https://www.w3.org/International/articles/article-text-size/index.en), read 10 November 2026; the page as read shows no date; standards body's guidance, reporting IBM's figures). Perqo's five tab labels are 4 to 8 characters long (Home, Benefits, Claims, Card, Account; IA6, Deliverable B), the band where IBM's figures put the largest expansion. A tab bar that fits in English is the first structure to test in a new language, and IA9's trigger already applies: a change to a tab sends the structure to a test before and after (RV-11).

Four further things do not travel, each from a filed rule.

1. **Variant terms.** Furnas and his colleagues found that two people chose the same term for an object with a probability under 0.20 (Furnas, Landauer, Gomez and Dumais, *Communications of the ACM* 30, no. 11, 1987; IA3, section 4.2; IA4, section 1.1). A language's variants are the words its speakers type, and IA4's source for them is the search log and support's tickets (IA4, section 3.3). A translated list of English variants is a guess at another population's words; each language's variants come from that language's logs and tickets, which is what T-14's "synonyms per language" means (IA5, Deliverable C).
2. **Exclusions.** R4 excludes "class" from Courses because "yoga class" is a Fitness item (IA4, B.4). The exclusion is a fact about English. In another language the word that pulls an item into the wrong category is another word, so R4 is run again for every language.
3. **Preferred terms at the basic level.** R3 asks for the employee's word, at the basic level where it can be (IA4, B.4). The basic-level word is found in each language's users, so a translated preferred term is assumed until that language's test confirms it (IA11's ladder: C0 until tested; IA11, section 6.4).
4. **Market facts inside a page.** IA5's localisation column marks the modules a translator cannot fill because they differ by market: plan comparison and pricing scenario (M-10, M-11), app-store links (M-24), legal text with its version date (M-25); and T-04's catalogue examples (M-08) may differ by market (IA5, Deliverable C, C.1 and C.2). Each needs a decision per market, by the module's owner, before the page goes live there.

### 5.3 · Languages and markets are separate keys

eBay's documentation shows a market with a tree of its own, about 20 marketplaces each with "a default category tree" (section 4.1). Shopify's shows one tree with translations, "translations to various languages in the `localizations` directory" (Shopify README, read 10 November 2026). Perqo takes Shopify's form for its taxonomy, on a reason of its own (Perqo, fictional): F-CAT is how money moves, a claim reads one category's balance and a new category creates an allocation for every employee who has it open (IA3, section 2.3; IA4, R8), so a market with a different category tree would be a different product. Markets differ in what a policy covers and what a page carries; the categories are the same in every market: a client's policy covers catalogue items (IA4, A.2, R-07), and the market-marked modules carry the rest. A proposal for a market-specific category is a new top-level category under R8 and goes to the IA review.

A language and a market are therefore two keys on every record that varies. A label varies by language; a module's content varies by market; a catalogue item's presence varies by policy, and so by client. The vocabulary in Deliverable C keys labels by surface and language; the inventory keys pages by identifier, with a market column where a market-marked module is used (Deliverable B, B.4).

## 6 · The failure modes at scale, and how to detect them

Four failures recur when a structure grows across surfaces, functions and languages. For each, the evidence that it happens, its Perqo instance, and the check that would detect it. None of the checks has been measured at Perqo; each is set as practice in Deliverable A, A.4, and assumed until tested (Deliverable A, A.6).

**Drift.** One thing acquires two names, and the mapping between them is never written (IA2, section 3, fault 5). DD-IA1 found it on the one site of its five whose makers publish rules for their vocabulary: GOV.UK's topic list reads "Births, deaths, marriages and care" where its navigation menu reads "Births, death, marriages and care" (DD-IA1, section 2, read 10 November 2026). Perqo has had it twice: the Help centre article H-2.1.2 said "refund" where the app says Claim (IA2, section 5.3), and the product page S-1.2 said "allowance" (IA5, section 1.3). Welchman's compliance conditions give the detection its form: measured "in a consistent and automated way" (Welchman 2015, ch. 5). **Check:** at each release, every label on the screens and pages the release changed is compared with the vocabulary's preferred term for that surface and language; a label in the vocabulary's "avoid" column is a finding (RV-13, Deliverable A, A.4).

**Duplication.** Two structures, or two terms, hold the same thing. In 2021 GDS described GOV.UK's three topic systems, "a set of around 200 topics", "a set of around 400 topics" and "a set of around 4,000 cross-cutting topics", and wrote: "This triple-system, which has substantial duplication, causes confusion for users"; publishers "currently need to tag their content to multiple topics, and to multiple topic systems", and the team was "in the early stages of thinking about how we might bring together mainstream topics, specialist topics and the taxonomy into a single tagging system" (Sam Dub, "Our plans to improve navigation on GOV.UK", GDS blog, 17 May 2021, [gds.blog.gov.uk, navigation plans](https://gds.blog.gov.uk/2021/05/17/our-plans-to-improve-navigation-on-gov-uk), read 10 November 2026; practice, a maker's account). The figure draws the three as GDS counted them: Mainstream topics, around 200; Specialist topics, around 400; Taxonomy topics, around 4,000, the taxonomy's "cross-cutting topics". Perqo's instances were smaller: a Features page and a brochure that duplicated Product (S-1.6, S-1.7; IA5, section 1.3), and the offers list shown twice, as "Discover" and as "Perks" (IA3, Deliverable). **Check:** each quarter, every variant that points to two values (R4 forbids it), every label used by two concepts, and every pair of inventory rows bound to one identifier (RV-07, extended in Deliverable A, A.4).

```viz
{"kind": "compare", "unit": "topics", "max": 4000, "caption": "Duplication at scale: GOV.UK's three topic systems in 2021, each counted as GDS gave it; supports the decision on whether a second classification may be added beside an existing one (section 6). Data from Dub, 'Our plans to improve navigation on GOV.UK', GDS blog, 17 May 2021 (read 10 November 2026): around 200 mainstream topics, around 400 specialist topics and around 4,000 taxonomy topics, a 'triple-system, which has substantial duplication'. Every bar tone 2: a product outside Perqo. Credit: GOV.UK, Government Digital Service.", "rows": [
 {"label": "Mainstream topics", "value": 200, "display": "around 200", "tone": 2},
 {"label": "Specialist topics", "value": 400, "display": "around 400", "tone": 2},
 {"label": "Taxonomy topics", "value": 4000, "display": "around 4,000", "tone": 2}]}
```

**The org chart leaking into the structure.** IA10 set out the evidence: Marieke McCloskey's analysis of 77 intranet IAs found that intranets "are initially structured to mimic the organizational configuration of the company", that "whenever the institution reorganizes, the navigation must also change", and that "Task-based structures often better withstood organizational change than intranets organized by department" (McCloskey, "Intranet Information Architecture (IA) Trends", Nielsen Norman Group, 23 February 2014; IA10, section 2.7); Conway's thesis is the older form of the warning (Conway 1968, as quoted by Colyer 2019; IA10, section 2.7). GOV.UK's principles write the guard into its naming rules: topics must "be subject areas (not tasks, audience types, names of departments, government initiatives, or content types)" (GDS, taxonomy principles, read 10 November 2026). At Perqo the leak has two sources. A client's structure was given its rule by IA10: "a client's structure enters as data, its words enter as variants, and a request to mirror its approval chain enters as a decision log entry" (IA10, section 2.7). Perqo's own structure has no rule yet, and one request is on record: the partnerships team asked for offers on Home and in Benefits (IA6, B.6). **Check:** each year, and whenever Perqo or a client reorganises, every term and top-level label is read against the list of Perqo's functions and of client group names; a term that names a team is a finding, and every term owner is confirmed to exist (RV-16).

**Orphan categories.** A value that holds nothing, or holds too much, or that nobody owns. GOV.UK's principles set both ends: "A topic should have between 2 and 12 child topics (or none)", "Single child topics can either be merged with the parent topic, pulled up to the same level as the parent topic or sibling topics and a new parent topic should be added", and "Topics with too many or too few content items should be reviewed to see if the taxonomy needs to be more or less granular" (GDS, taxonomy principles, read 10 November 2026). In 2019 GOV.UK reported its untagged content as a measure of the same thing: "the amount of untagged content has stopped growing (and is actually decreasing as a percentage)" (Stephens-Manassiev 2019; the post gives no figures). Perqo's R5 covers the low end, a value needs at least two items and is hidden from filters when it loses its last one (IA4, B.4), and nothing covers the high end. An orphan also arises when an owner goes: a term whose owner has left has no one to ask. **Check:** each quarter, items per value, articles and stories per F-CAT tag, untagged items, and values outside R5 and the proposed R12 (RV-14).

## 7 · Documented practice, verified against its publications

Three organisations publish their taxonomy or how it is governed, and each publication was read on 10 November 2026: GDS for GOV.UK (principles, a maker's blog post, developer documentation), eBay (developer documentation of its category trees), and Shopify (its open-source taxonomy's README). None publishes a measure of whether its governance works; GDS's posts give counts of topic systems and describe trends, and the other two describe mechanisms. They are cited as practice and documentation, never as evidence about Perqo.

DD-IA1 handed this unit GOV.UK's principles to set beside IA4's rules. The table does that, each principle in GDS's words, the Perqo rule that meets it, and what Perqo takes (Perqo, fictional).

| GOV.UK principle (GDS 2019, updated 2026) | IA4's rule | What Perqo takes |
|---|---|---|
| "A topic should have between 2 and 12 child topics (or none)" | R7: F-CAT keeps two levels; each category has two narrower terms today (B.2) | nothing new: R7 is stricter on depth; the count of children per category is not limited, and the test of a longer list is a tree test (RV-11) |
| "The maximum number of topics at any level should ideally be around 12" | none; four categories at the top level | nothing new: R8 makes every new category a product decision |
| "Content should be tagged to the lowest possible level of the taxonomy"; "should not be tagged to both a topic and its parent" | R2: every item has exactly one narrower term, and so one category | already met (DD-IA1, section 2) |
| "be disambiguated if there is more than one topic with the same name - use qualifiers in brackets" | none | R11, proposed: a preferred term used by two concepts takes a qualifier in brackets in the vocabulary, and the duplication check reads for it (DL-026) |
| topics "be subject areas (not tasks, audience types, names of departments, ...)" | R1 and R10: a value answers its facet's question, and a property of the policy, amount, merchant or client is not a facet | the owner check of RV-16 adds Perqo's own functions to the test |
| "reflect user language where possible"; "be written in plain English" | R3: the employee's word, checked against the search log and tickets | R3 run per language (section 5.2) |
| "Topics with too many or too few content items should be reviewed" | R5: at least two items; an empty value hidden | R12, proposed: a value above a size set by the content team is reviewed for a split at RV-14 (DL-026) |
| "GDS manages the topic taxonomy"; publishers "suggest new topics, or changes" | IA4, B.4: the content team decides, reviewed with support and engineering; anyone may propose (IA9, D.1) | already met; the request form is Deliverable B, B.1 |

eBay and Shopify add what GOV.UK does not need: a version a reader outside the organisation can compare (eBay's `categoryTreeVersion`), a calendar for releases and a published mapping between versions (Shopify), and, for eBay, a tree per market (section 4.1). Section 5.3 gives the reason Perqo keeps one tree; the open condition in Deliverable B gives the moment Perqo would add a published version.

What these publications cannot show: how many change requests each receives, how long one takes, how accurate the tagging is, or whether the structure helps people find things. GDS's 2019 sentence on tagging accuracy is the closest any comes, and it reports a need with no result.

## Deliverable · A · The Perqo governance model

*Face of this artefact (IA2, the notation sheet): governance model for Perqo's IA, taxonomy and vocabulary, in six parts: A.1 the roles; A.2 the decision rights, with a matrix figure; A.3 the forums, FO-01 to FO-09 as IA10 set them and FO-10 added; A.4 the cadence, with RV-13 to RV-16 added to IA9's RV-01 to RV-12 and the measurement model's reads per forum, with a matrix figure; A.5 escalation; A.6 the assumption register's process part, AR-50 to AR-64. Fidelity F2 (complete for its scope; identifiers stable). Decision: who decides, applies, is consulted on and is told of each kind of change, where, and how often the structure is checked for drift. Readers: the IA designer, the content team, product management, localisation, leadership, and every function named in a row. Leaves out: named people, the meetings' length, which markets and languages come next (leadership's decision, A.5), the business case for any of it (DD-IA2's template, Deliverable B, B.1). Owner: the IA designer; version 1, dated 10 November 2026; every role, forum, review and threshold set here is assumed until tested (A.6); every change it makes to a filed artefact is proposed in DL-023 to DL-026 (Deliverable B, B.6), so no filed artefact changes until each is decided. Perqo is fictional.*

### A.1 · The roles

Every role is held by one of IA10's twelve functions or by the IA designer, as IA9 named it (Perqo, fictional). The last column is this unit's mapping onto Welchman's framework (section 3.1).

| Role | Held by | Owns | Decides | Framework (section 3.2) |
|---|---|---|---|---|
| Strategy owner | leadership | which markets and languages come next | a new market or language | strategy |
| Rule owner | product management | the rule terms of the vocabulary (Deliverable C) | signs off rule and two-surface changes (IA9, D.1) | strategy, policy |
| IA review | the IA designer (chair), product management, engineering, content team, support (IA9, section 4.1) | none | renames, retired identifiers, rule and two-surface changes, a new top-level category (R8) | policy |
| IA designer | the IA designer | the canonical IA artefacts other than the taxonomy and the vocabulary; the decision log; the object terms (Deliverable C) | changes inside one surface that rename nothing (IA9, D.1) | core team |
| Vocabulary steward | content team (DL-024) | the controlled vocabulary; the benefits taxonomy (IA4, B); the taxonomy terms | taxonomy values and variants, by R1 to R12 | core team; standards steward |
| Term owner | the owner of the artefact that defines the term (section 3.2) | one term's definition (Deliverable C) | nothing alone: asked first about a change | core or extended team |
| Language owner | localisation, one per live language [when a second language is added] | that language's labels and variants | a term's label in that language | core team |
| Market module owner | the owner of each market-marked module: marketing with sales (M-10, M-11, on Pricing, S-2), support (M-24, on S-6), legal (M-25) (IA5, Deliverable A) | that module's content per market | that content | extended team |
| Applier | engineering (model names, synonyms loaded, redirects); support, marketing and the content team (tags on articles, stories and items) | the tags and loads they make | nothing alone | extended team |
| Signal reader | support (logs, tickets; IA9, RV-04, RV-05), product management (paths, RV-06) | the reads | nothing alone: findings are hypotheses (IA9, section 6.4) | extended team |

### A.2 · The decision rights

For each kind of change: who decides, who signs off, who chairs, who applies it, who is consulted and who is told (Perqo, fictional). "Product mgmt" in the figure is product management. Each row follows IA9's D.1 and IA4's B.4 where those already decide it; the rows for a language, a translation and a market are new.

| Change | Decides | Signs off | Chairs | Applies | Consulted | Told |
|---|---|---|---|---|---|---|
| New variant | content team | none | none | engineering (synonyms loaded) | support; engineering; localisation | none |
| New value (narrower term or flat-facet value) | content team | none | none | content team (items retagged) | support; engineering; localisation | product management; clients (J-08, FO-02) |
| New category (top level, R8) | IA review | product management | IA designer | content team; engineering | clients (R8); localisation | none beyond J-08's list |
| Rename term | IA review | none | IA designer | content team (vocabulary first); localisation (each language) | none beyond the review | clients |
| Retire ID | IA review | none | IA designer | content team (migration); engineering (redirects); localisation | none beyond the review | clients |
| Rule change (DT-) | IA review | product management | IA designer | engineering | legal, when personal data is touched (DL-014) | clients |
| New language | leadership | none | none | localisation | product management; localisation; legal | IA review; content team |
| Translate term | localisation | none | none | engineering (synonyms per language) | content team; support | none |
| Market module | the module's owner (A.1) | none | none | content team | localisation; legal | sales (FO-04) |

The figure draws the first eight rows by function; the market module row, whose decider differs by module, stays in the table. Row labels are short forms of the table's: New variant, New value, New category, Rename term, Retire ID, Rule change, New language, Translate term. The marks: decides, "takes the decision (IA9, D.1)"; signs off, "a rule or two-surface change is not decided without it"; chairs, "runs the forum that decides"; applies, "changes the vocabulary, the items or the system"; consulted, "heard before the decision"; told, "informed after it, through its forum". Every row is tone 5, shared.

```viz
{"kind": "matrix", "caption": "The Perqo governance model, decision rights: for eight kinds of change, which function decides, signs off, chairs, applies, is consulted or is told; supports the decision on where a proposed change to the taxonomy, the vocabulary or the IA goes (Deliverable A, A.2). Rows from IA9, D.1 (renames, retired identifiers, rules, the IA review), IA4, Deliverable B, B.4 (values and variants, R8 for a new category) and IA10, A.3 (J-08's told list); the language and translation rows set in A.2; DL-014 (IA10, proposed) for legal. Accountability for strategy, policy and standards after Welchman, Managing Chaos, 2015 (practice). Every row tone 5, shared. Perqo is fictional.", "cols": ["IA designer", "IA review", "Content team", "Localisation", "Engineering", "Support", "Product mgmt", "Clients", "Legal", "Leadership"], "rows": [
 {"label": "New variant", "tone": 5, "cells": [null, null, "decides", "consulted", "applies", "consulted", null, null, null, null]},
 {"label": "New value", "tone": 5, "cells": [null, null, "decides", "consulted", "consulted", "consulted", "told", "told", null, null]},
 {"label": "New category", "tone": 5, "cells": ["chairs", "decides", "applies", "consulted", "applies", null, "signs off", "consulted", null, null]},
 {"label": "Rename term", "tone": 5, "cells": ["chairs", "decides", "applies", "applies", null, null, null, "told", null, null]},
 {"label": "Retire ID", "tone": 5, "cells": ["chairs", "decides", "applies", "applies", "applies", null, null, "told", null, null]},
 {"label": "Rule change", "tone": 5, "cells": ["chairs", "decides", null, null, "applies", null, "signs off", "told", "consulted", null]},
 {"label": "New language", "tone": 5, "cells": [null, "told", "told", "consulted", null, null, "consulted", null, "consulted", "decides"]},
 {"label": "Translate term", "tone": 5, "cells": [null, null, "consulted", "decides", "applies", "consulted", null, null, null, null]}],
 "legend": [{"mark": "decides", "means": "takes the decision (IA9, D.1)", "tone": 5}, {"mark": "signs off", "means": "a rule or two-surface change is not decided without it", "tone": 5}, {"mark": "chairs", "means": "runs the forum that decides", "tone": 5}, {"mark": "applies", "means": "changes the vocabulary, the items or the system", "tone": 5}, {"mark": "consulted", "means": "heard before the decision", "tone": 5}, {"mark": "told", "means": "informed after it, through its forum", "tone": 5}]}
```

The figure draws one mark per cell, so where the table names a function twice it draws the stronger part. In "New variant" engineering is consulted and loads the synonym: the figure draws "applies". In "New value" the content team decides and retags the items: the figure draws "decides"; engineering is consulted and does not apply, because a narrower term reaches the system only through tags, and the synonyms load with the value's variants, which is the first row. In "New language" localisation is consulted and then sets the language up: the figure draws "consulted", because the decision is leadership's.

### A.3 · The forums

FO-01 to FO-09 keep IA10's identifiers, names, chairs and cadences (IA10, Deliverable A, A.2). This unit adds to what five of them take in and put out, and adds one, FO-10 (DL-023, proposed). Each addition is proposed; IA10's table changes only when DL-023 and DL-024 are decided.

| ID | Forum | What this unit adds to it |
|---|---|---|
| FO-01 | IA review | decides renames, retired identifiers and new categories with their impact per language (Deliverable B); reads RV-13's drift findings once a quarter |
| FO-02 | Story check and release note | the release note names, per language, each label changed; RV-13 runs at each release |
| FO-03 | Vocabulary and content review | the vocabulary's steward (DL-024); takes RV-14's counts and the duplication check (RV-07 extended); decides new values and variants; reads M-07 and M-12 to M-14 for the variants they suggest |
| FO-04 | Pre-sales briefing | sales in each market told of category and label changes in its language (J-08, J-13) |
| FO-09 | Leadership quarterly | decides a new market or language; reads RV-16's owner check once a year |
| FO-10 | Language and market review *new* | below |

**FO-10, the language and market review** (Perqo, fictional). Kind: meeting. Chair: the language owner, one per live language. Takes part: the content team, support (that language's logs and tickets), legal (M-25), the owners of M-10, M-11 and M-24 for that market, the IA designer when a request touches the IA. Inputs: each change FO-03 or FO-01 decided since the last meeting, with its labels to translate; RV-15's per-language search read; the market-marked modules due in that market. Outputs: labels and variants in that language, each marked tested or assumed; market modules filled; proposed DL entries for anything that would change the IA. When: once before a language goes live, then quarterly, and within one release of any rename. Dormant until leadership decides a second language at FO-09; until then, TP-05's row stays at C0 (IA11, section 7) and the content team holds every language question.

### A.4 · The cadence

IA9's twelve reviews stand (IA9, Deliverable C). Four are added, each detecting one failure of section 6, and RV-07 is extended to detect duplication (Perqo, fictional; DL-024, proposed). Thresholds are set here and assumed until tested (A.6).

| ID | Review | Detects | Checks | Cadence | Trigger | Owner | Output |
|---|---|---|---|---|---|---|---|
| RV-07 (extended) | Vocabulary | duplication | as IA9 set it, plus: every variant that points to two values; every label used by two concepts without a qualifier (R11, proposed); every pair of inventory rows bound to one identifier | quarterly | a new variant | content team | DL entries; synonyms loaded |
| RV-13 | Label drift check | drift | every label on the screens and pages a release changed, against the vocabulary's preferred term for its surface and language; any label in an "avoid" column | each release | a rename: the release that ships it | content team | build debt logged as DL entries |
| RV-14 | Term counts | orphans, over-broad values | items per F-CAT value; articles and stories per F-CAT tag; untagged items, articles and stories; values with fewer than two items (R5); values above R12's size | quarterly | a value added or a client's catalogue changed | content team | proposals to merge, split or hide; untagged items tagged |
| RV-15 | Search per language | untranslated or unfound labels | M-07, M-12, M-13 and M-14 for each language's Help centre search (DD-IA2, A.2); zero-result queries per language; queries in one language that match another's variant | quarterly, per language | a language added: the next month's log | support | variants for FO-10; hypotheses for IA11 |
| RV-16 | Owner check | org chart, orphan ownership | every term owner and language owner exists; no term or top-level label names a Perqo team or a client's group | yearly | a reorganisation at Perqo; a client's request to mirror its structure | IA designer | owners reassigned; DL entries |

The measurement model's reads, by forum (DD-IA2, Deliverable A): FO-06 reads M-07 and M-12 to M-15, per language once the Help centre has more than one; FO-03 reads M-07 and M-12 to M-14 for the variants they suggest; FO-10 reads RV-15's per-language results; FO-01 receives the reads of M-16 to M-19 for Admin, which go to it from RV-06 when a target is missed (DD-IA2, A.2); FO-09 reads what DL-022 proposes. No read decides a change on its own: a lagging change is a hypothesis at C1 (DD-IA2, A.3, rule 5).

The drift-detection cadence, drawn: one row per check, its owner in the cell where it runs. Label drift, RV-13: each release, content team; on trigger, content team [a rename]. Term counts, RV-14: quarterly, content team; on trigger, content team [a value added]. Duplicates, RV-07 extended: quarterly, content team; on trigger, content team [a new variant]. Language search, RV-15: quarterly, support [two languages or more]; on trigger, support [a language added]. Owner check, RV-16: yearly, IA designer; on trigger, IA designer [a reorganisation]. Ticket tags, IA9's RV-05: monthly, support. Face audit, IA9's RV-09: quarterly, IA designer. Every row tone 5, shared.

```viz
{"kind": "matrix", "caption": "Drift-detection cadence: the checks that detect drift, duplication, orphans and the org chart leaking into Perqo's taxonomy and vocabulary, by when each runs, with its owner in the cell (a condition in square brackets: the check runs then only when it holds); supports the decision on who looks for which failure, and when (section 6; Deliverable A, A.4). RV-13 to RV-16 and the extension of RV-07 set in A.4; RV-05 and RV-09 from IA9, Deliverable C; measurement 'in a consistent and automated way' after Welchman, A List Apart, 2015 (practice); sizes reviewed at both ends after GDS, 'GOV.UK Taxonomy principles' (read 10 November 2026). Every row tone 5, shared. Perqo is fictional.", "cols": ["Each release", "Monthly", "Quarterly", "Yearly", "On trigger"], "rows": [
 {"label": "Label drift", "tone": 5, "cells": ["content team", null, null, null, "content team [a rename]"]},
 {"label": "Term counts", "tone": 5, "cells": [null, null, "content team", null, "content team [a value added]"]},
 {"label": "Duplicates", "tone": 5, "cells": [null, null, "content team", null, "content team [a new variant]"]},
 {"label": "Language search", "tone": 5, "cells": [null, null, "support [two languages or more]", null, "support [a language added]"]},
 {"label": "Owner check", "tone": 5, "cells": [null, null, null, "IA designer", "IA designer [a reorganisation]"]},
 {"label": "Ticket tags", "tone": 5, "cells": [null, "support", null, null, null]},
 {"label": "Face audit", "tone": 5, "cells": [null, null, "IA designer", null, null]}]}
```

### A.5 · Escalation

IA12's procedure applies unchanged when the owner of an answer does not give it: name the owner, ask once in the owner's format, write the question as a proposed DL entry with a default and the meeting that decides it, ship the default labelled, decide at that meeting with silence recorded as "not given", and show the risk where the owner reads (IA12, section 4.4). Three cases arise in this model, each with its default (Perqo, fictional).

- **A term owner who does not answer.** The content team, as steward, proposes the default at FO-03: the term keeps its current definition, and the change waits as proposed with the FO-03 meeting named.
- **No language owner.** While TP-05 is dormant, the content team holds every language question. When a language goes live without a language owner, a label not yet translated shows the English preferred term and is marked "untranslated" in the vocabulary; the change that needs it stays accepted and is not applied (Deliverable B, B.4).
- **No decision on markets.** Which markets and languages come next is leadership's, a strategy question in Welchman's sense (section 3.1), and it stays free in this unit for that reason. Product management asks at FO-09; the default is no second language, which builds nothing that assumes one, and FO-10 stays dormant.

### A.6 · The register's process part

IA12 filled the assumption register for Admin and left its process part unfilled: nine rows IA11's table A.2 sends to the register that do not concern Admin (rows 15 to 19 and 21 to 24), IA8's one-year test of J- rows, and localisation's TP-05 (IA12, section 3.4). They are entered here, with this unit's own assumptions after them, in IA12's fields cut to the ten a reader needs (IA12, section 3.2). Every row is at C0 and not run on 10 November 2026 (Perqo, fictional). The counts of rows owned per function in IA12's stakeholder map cover the Admin part; the process part's owners below are added to them at the next FO-09, when the map is revised (IA12, Deliverable C; DL-024).

| ID | Assumption | From | Rung | Test | Owner | Read at | Input | Fix | Status |
|---|---|---|---|---|---|---|---|---|---|
| AR-50 | the trees' words let sales explain the rules (BR-3) | IA11, A.2, row 15 | C0 | IA8's recorded-demo restatement test, at FO-04 | IA designer | FO-04 | kept | open | not run |
| AR-51 | readers can read one layer, or one brief, alone | row 16 | C0 | IA8's one-layer question test (IA8, D.5) | IA designer | FO-01 | kept | open | not run |
| AR-52 | stories citing identifiers keep build debt down | row 17 | C0 | RV-02's share of built screens that differ from their F3 artefact, quarter to quarter | product management | RV-10 | kept | open | not run |
| AR-53 | the F3 gate does not slow delivery | row 18 | C0 | stories held at RV-01, read at RV-10 | product management | RV-10 | kept | open | not run |
| AR-54 | a quarterly face audit keeps record debt from building | row 19 | C0 | DL entries accepted and not applied, at RV-10 | product management | RV-10 | kept | open | not run |
| AR-55 | the routing rule sends changes to the right decider | row 21 | C0 | DL entries reopened or superseded within a quarter | product management | RV-10 | kept | open | not run |
| AR-56 | each function's question is the one it asks | row 22 | C0 | interviews with each function | IA designer | FO-09 | absent: FO-09 has not met (IA12, section 3.4) | open | not run |
| AR-57 | engineering can build from BR-2 without a meeting | row 23 | C0 | questions raised at FO-02, counted per release | IA designer | FO-02 | kept | open | not run |
| AR-58 | positions recorded reduce reopened decisions | row 24 | C0 | DL entries reopened within a quarter, before and after DL-011 | product management | RV-10 | kept | open | not run |
| AR-59 | a reader a year later can trust a J- row without opening every surface map | IA8, section 6 | C0 | one year after a J- row is checked, a reader answers a question from the row alone and is checked against the surface maps | IA designer | RV-03 | kept | open | not run |
| AR-60 | localisation's question is the key every language shares and what changes by market (TP-05) | IA10, A.1; IA11, section 7 | C0 | interviews with the language owner at the first FO-10 | content team, until a language owner exists | FO-10 | absent: dormant until a second language | open | not run |
| AR-61 | a term owner answers a change request within one FO-03 cycle | A.1 (this unit) | C0 | time from proposed to decided for taxonomy and vocabulary DL entries | content team | RV-10 | kept | open | not run |
| AR-62 | RV-13 finds label drift before support's tickets do | A.4 (this unit) | C0 | for two quarters, labels found by RV-13 against labels found first by RV-05's tags | content team | RV-05 | kept | open | not run |
| AR-63 | a translated preferred term is found as well as the English one | section 5.2 (this unit) | C0 | IA11's tree test TT-1 in the new language against the English results, at C3 | language owner | RV-11 | absent: no second language | backbone | not run |
| AR-64 | variants taken from a language's own logs serve better than translated English variants | section 5.2 (this unit) | C0 | M-07 for that language before and after the log-derived variants are loaded (RV-15) | support | RV-15 | absent: no second language | open | not run |

## Deliverable · B · The taxonomy change-request process

*Face of this artefact (IA2, the notation sheet): process specification for a change to Perqo's benefits taxonomy or controlled vocabulary, in any language or market, extending IA9's change control (section 4 and Deliverable D) and IA12's decision log template (Deliverable D): B.1 the request, B.2 the operations, B.3 the flow, with a flow figure, B.4 languages and markets, B.5 who is told, B.6 the decision log entries DL-023 to DL-026. Fidelity F3 for the form and the operations (ready to use), F2 for the language rules (no second language is live). Decision: what a change to a term must carry, who decides it, what must move with it and who must hear of it, before it counts as made. Readers: the content team (steward), the IA designer, the IA review, engineering, localisation, support, sales. Leaves out: changes to the IA that touch no term, which run IA9's D.2 unchanged; the decisions on DL-023 to DL-026; money. Owner: the content team; version 1, dated 10 November 2026; every step is assumed until AR-61 and AR-62 are read. Perqo is fictional.*

### B.1 · The request

A change request is a decision log entry in IA12's template (IA12, Deliverable D, D.1), with five fields added for a term. Fields marked (proposed) depend on an entry not yet decided: positions on DL-011, register rows on DL-017, told with forum and date on DL-012, and the five term fields on DL-025.

| Field | What to write | Rule |
|---|---|---|
| ID, change, raised by and from | as IA12's template | IA9, D.3 |
| Operation (proposed) | add, rename, move, merge, split or retire (B.2) | section 4.2 |
| Terms (proposed) | each identifier touched (CAT-, PAY-, TYP-, CHN-, O-, VOC-), with its current and proposed preferred term per surface | IA4, R9 |
| Reach (proposed) | the counts of what carries each term: catalogue items (BI-), merchants, offers, help articles and customer stories by F-CAT tag, addresses, synonyms, reports, J- rows (J-08 for categories) | IA8, D.4; RV-14 |
| Languages and markets (proposed) | each live language, with the label to change or translate; each market whose modules or catalogue examples change | section 5; B.4 |
| Cost, when asked (proposed) | DD-IA2's business-case template, every number measured, sourced, context or assumed | DD-IA2, Deliverable B |
| Touches, register rows, alternatives, positions, decided by, decide at, decision, version effect, places to apply, told, supersedes, status | as IA12's template | IA12, D.1 |

Anyone may raise a request (IA9, D.1): support from a ticket or a zero-result query, sales from a buyer's word, a client from its policy, the content team from RV-14. GDS's principle that publishers "suggest" and GDS manages (section 3.3) is the same division; at Perqo the request goes to FO-03, where the content team logs it.

### B.2 · The operations

Six operations, each with its effect on the identifier, the version, the migration it needs and who decides (Perqo, fictional). Version effects follow IA9's rule: a change that breaks a citation makes a new version of the taxonomy's face, anything else a dated amendment (IA9, section 4.4).

| Operation | Identifier | Version effect | Migration | Decides |
|---|---|---|---|---|
| Add | a new identifier, with no word of any language in it (IA5, section 5.3) | amendment | at least two items tagged before it shows (R5); variants loaded per language; labels translated or marked untranslated | content team (a narrower term or flat value); IA review with product management's sign-off, finance and the client (a category, R8) |
| Rename | kept (R9) | new version | old label kept as a variant in every language; every surface label, article and synonym changed; addresses keep the identifier and redirect the old slug | IA review, vocabulary first |
| Move (new parent) | kept (R9) | new version | items keep the value; the parent's counts and filters change; addresses redirect when the parent is in the path; for an F-CAT value, the allocation that pays for its items changes, which changes a rule's outcome | IA review; product management signs off for F-CAT |
| Merge | the one kept stays; the other is deprecated, then retired (section 4.2) | new version | items retagged to the one kept; the retired term's labels kept as its variants; addresses redirect to the kept value | IA review |
| Split | the old one is deprecated; new identifiers for the parts | new version | every item reclassified, one part each (R2); each part needs two items (R5); addresses of the old value redirect to its parent until the parts have pages | IA review |
| Retire | never reused (R9) | new version | items retagged or removed; addresses redirect to the parent or the nearest value, as GOV.UK redirected its retired policy areas to "equivalent topics" (Stephens-Manassiev 2019) | IA review |

A change to a flat facet (F-PAY, F-TYP, F-CHN) touches no allocation, so a move there needs no product sign-off. A change to F-CAT always reaches money: claims read one category's balance (IA3, section 2.3) and each merchant spends from its category (IA4, A.1), so the impact field names every merchant whose narrower term moves.

### B.3 · The flow

The flow extends IA9's (IA9, D.2): migration is a step of its own, and every step counts each live language. Its steps, with the note each carries in the figure:

1. **Propose.** Any function; the request form (B.1); DL entry proposed.
2. **Check the impact.** Every identifier, item, page, synonym and language version.
3. **Route.** → see the decision rights (A.2).
4. **Decide.** [declined] logged with its reason; ends here.
5. **Change the vocabulary first.** Every language; old label kept as a variant.
6. **Migrate.** Retag, redirect, reload synonyms, re-stamp faces.
7. **Tell.** The told list (B.5); the release note; each language.
8. **Close.** Applied when every language version is done.

The flow kind draws no branch, so the declined path is the bracketed condition in step 4's note, as in IA9's figure. Every step is tone 5, shared.

```viz
{"kind": "flow", "per_row": 2, "caption": "Change-control flow for a term: how a change to Perqo's taxonomy or vocabulary is proposed, checked, routed, decided, applied first in the vocabulary, migrated, told and closed, in every live language; supports the decision on what must happen before a term's change counts as made (Deliverable B, B.3). Extends IA9's change-control flow (IA9, section 4.2 and D.2) with the migration step and the per-language rule of B.4; the request form from IA12, Deliverable D; redirects to equivalent topics after GDS (Stephens-Manassiev, Inside GOV.UK, 2019, read 10 November 2026). The flow kind draws no branch, so the declined path is a bracketed condition in the Decide step's note. Every step tone 5, shared. Perqo is fictional.", "steps": [
 {"label": "Propose", "note": "any function; the request form (B.1); DL entry proposed", "tone": 5},
 {"label": "Check the impact", "note": "every identifier, item, page, synonym and language version", "tone": 5},
 {"label": "Route", "note": "→ see the decision rights (A.2)", "tone": 5},
 {"label": "Decide", "note": "[declined] logged with its reason; ends here", "tone": 5},
 {"label": "Change the vocabulary first", "note": "every language; old label kept as a variant", "tone": 5},
 {"label": "Migrate", "note": "retag, redirect, reload synonyms, re-stamp faces", "tone": 5},
 {"label": "Tell", "note": "the told list (B.5); the release note; each language", "tone": 5},
 {"label": "Close", "note": "applied when every language version is done", "tone": 5}]}
```

### B.4 · Languages and markets

The rules a change follows once Perqo has more than one language (Perqo, fictional). Until then they are dormant, and only rule 1 applies, to every identifier created from today.

1. **Identifiers carry no words.** Every new identifier is a code with no word of any language in it; existing identifiers, CAT-HEA among them, are kept under R9 and never translated (section 5.1).
2. **One preferred term per surface per language.** The vocabulary gains a column per live language for each surface label (Deliverable C, C.2). A label not yet translated shows the English preferred term and is marked "untranslated"; the change that needs it stays accepted and is not applied, until the label exists (A.5).
3. **Variants per language, from that language.** Each language's variants come from its own search log and tickets (RV-15; IA4, section 3.3), and R4's exclusions are re-run for it. T-14, the Help search results template, loads the synonyms of the visitor's language only (IA5, Deliverable C).
4. **Addresses.** English keeps the root and every existing address, because an address that changes breaks every link to it (Berners-Lee, "Cool URIs Don't Change", W3C, 1998; IA4, section 5). Each other language takes a subdirectory, the structure Google's documentation gives for a multi-regional site, example.com/de/, applied here to languages (IA5, section 5.3). A category page's address in another language is perqo.com/{language}/{section path in that language}/cat-hea/{preferred term in that language}; the page is found by its identifier, and any other path that carries the identifier redirects permanently to the current one. Every language version of a page lists every other, keyed by its inventory ID (IA5, section 5.3).
5. **Markets.** A market changes no category (section 5.3). Before a page goes live in a market, the owner of each market-marked module on it fills it for that market: M-10 and M-11 (marketing with sales), M-24 (support), M-25 (legal); and T-04's catalogue examples (M-08) show the items that market's clients' policies cover. The inventory gains a market column for the rows that use them.
6. **Measures.** M-07 and M-12 to M-14 are read per language from the month a language goes live (RV-15; DD-IA2, A.2).
7. **An outside reader.** If software outside Perqo comes to read the taxonomy, such as a merchant integration, the taxonomy publishes a version number with each release and a mapping from the last, as eBay and Shopify document (section 4.1); this is a condition with no decision attached, recorded on DL-025.

### B.5 · Who is told

IA10's list of who is told when a join changes stands (IA10, A.3). For a term the told list adds these, each through its forum (Perqo, fictional).

| Change | Told | Through |
|---|---|---|
| any rename, merge, split or retirement | support (articles, scripts, tags); every language owner | FO-06; FO-10 |
| an F-CAT value (J-08) | sales, marketing, customer success, clients, as IA10 lists; each market's sales | FO-04; FO-03; FO-05; FO-02 |
| an Admin label | clients, in the release note, in each live language | FO-02 |
| a market module | sales in that market; legal for M-25 | FO-04; FO-08 |
| a new language | every function | FO-09; then FO-10 |

Welchman's warning is the reason this table exists: "resources aren't told that a standard has changed until the standard is violated" (section 3.1). A change is closed only when the told field names every function above with its forum and date (DL-012, proposed).

### B.6 · The decision log entries

The log stands at DL-022 on 10 November 2026: DL-001 to DL-010 applied (IA9, D.3), DL-011 to DL-022 proposed and undecided (IA10, A.4; IA11; IA12, Deliverable D; DD-IA1; DD-IA2, Deliverable D). This unit adds four, each proposed, in IA12's template. No filed artefact changes until each is decided; when one is, the vocabulary changes first and each face it names is re-stamped by IA9's rule (IA9, section 4.4).

| Field | DL-023 |
|---|---|
| Change | Localisation's forum: FO-10, the language and market review (A.3), is added to IA10's forums; TP-05's meeting becomes "FO-10 [when a second language is added]"; the language owner role is added (A.1) |
| Raised by, from | DD-IA3, Deliverable A; IA10's TP-05, "none yet (DD-IA3)" |
| Touches | IA10, Deliverable A, A.1 (TP-05) and A.2 (a new row); IA12, Deliverable C, C.1 (TP-05's forum and format) and C.3 (the Monitor row); no J- row |
| Register rows (proposed) | AR-60 |
| Alternatives considered | localisation as a standing item of FO-03 (the vocabulary review would then decide market modules, which are not its owners'); no forum until a language is chosen (leaves the first language to be launched without one) |
| Positions (proposed) | none recorded |
| Decided by | IA review: the forum takes in legal and sales and decides labels on every surface (IA9, D.1) |
| Decide at | FO-01, the IA review's next meeting |
| Decision, date, reason | not decided |
| Version effect | dated amendments to IA10, Deliverable A and IA12, Deliverable C: both add, neither breaks a citation |
| Places to apply | IA10, A.1, TP-05's Meeting cell: "FO-10 language and market review [when a second language is added]"; IA10, A.2: FO-10's row as in A.3 of this unit; IA12, C.1, TP-05's forum: "FO-10 (dormant)"; each not done |
| Told | product management, engineering, content team, support at FO-01; leadership at FO-09 |
| Supersedes, superseded by | none |
| Status | proposed |

| Field | DL-024 |
|---|---|
| Change | The controlled vocabulary (Deliverable C) is a canonical artefact whose steward is the content team; each term has an owner by section 3.2's rule; reviews RV-13 to RV-16 are added and RV-07 extended (A.4); the register's process part, AR-50 to AR-64, is entered (A.6) |
| Raised by, from | DD-IA3, section 3.2: the vocabulary has two owners in IA9 (section 4.1 and W-13) |
| Touches | IA9, section 4.1 (the artefacts the IA designer owns) and Deliverable C (RV-07 and four new rows); IA2, the decision table's controlled-vocabulary row (its example becomes Deliverable C); IA12, Deliverable B (rows AR-50 to AR-64) and C.1 (rows owned per function); no J- row |
| Register rows (proposed) | AR-61, AR-62 |
| Alternatives considered | the IA designer as owner of the vocabulary (it would own every word on every surface, and the content team, which puts the words in place, would own none); one owner per surface (four vocabularies, section 2) |
| Positions (proposed) | none recorded; the content team to be asked at the next FO-03 |
| Decided by | IA review, product management signs off: it changes who decides a class of change (IA9, D.1) |
| Decide at | FO-01, after the next FO-03 |
| Decision, date, reason | not decided |
| Version effect | dated amendments to IA9, section 4.1 and Deliverable C, IA2's decision table and IA12, Deliverable B: none retires an identifier, renames a label, removes a relationship or changes a rule's outcome (IA9, section 4.4) |
| Places to apply | IA9, section 4.1: "the canonical IA artefacts, other than the benefits taxonomy and the controlled vocabulary (the content team's)"; IA9, C: RV-07's Checks extended and rows RV-13 to RV-16; IA2, the decision table's controlled-vocabulary row: "§5.3 vocabulary · DD-IA3, Deliverable C"; IA12, B: AR-50 to AR-64; IA12, C.1: rows owned per function, revised at the next FO-09; each not done |
| Told | every member of the IA review at FO-01; support at FO-06; leadership at FO-09 |
| Supersedes, superseded by | none |
| Status | proposed |

| Field | DL-025 |
|---|---|
| Change | The taxonomy change-request process (Deliverable B) extends IA9's change control for terms: the request's five term fields (B.1), the six operations (B.2), the migration step (B.3), and the language and market rules with the URL form in other languages and T-14's synonyms per language (B.4) |
| Raised by, from | DD-IA3, sections 4 and 5; IA9, "What later units take" (DD-IA3); IA5, section 5.3 and B.3 (the URL form left free) |
| Touches | IA9, D.2 and D.3; IA12, D.1 (five fields); IA5, Deliverable B, B.3 (category page URLs) and Deliverable C, T-14; IA4, B.4, R9 (no change: the rule is applied as it stands); J-08 |
| Register rows (proposed) | AR-63, AR-64 |
| Alternatives considered | run term changes through IA9's D.2 unchanged (migration has no step and no owner); a release calendar for the taxonomy, as Shopify publishes (no outside reader yet: B.4, rule 7) |
| Positions (proposed) | none recorded |
| Decided by | IA review, product management signs off: it changes the change control on every surface (IA9, D.1) |
| Decide at | FO-01, the IA review's next meeting |
| Decision, date, reason | not decided |
| Version effect | dated amendments to IA9, Deliverable D, IA12, Deliverable D and IA5, Deliverables B and C: each adds; no citation breaks, because English keeps every address |
| Places to apply | IA9, D.2: "migrate" added after "change the artefacts" for a change to a term, and "every live language" in the impact and close steps; IA12, D.1: the five term fields; IA5, B.3: the URL form in other languages (B.4, rule 4); IA5, C.2, T-14's Localisation cell: "language; synonyms of the visitor's language only, from that language's logs (DD-IA3)"; each not done |
| Told | product management, engineering, content team, support at FO-01; sales at FO-04; marketing at FO-03 |
| Supersedes, superseded by | none |
| Status | proposed |

| Field | DL-026 |
|---|---|
| Change | IA4's rules for adding a value gain two: R11, a preferred term used by two concepts takes a qualifier in brackets in the vocabulary; R12, a value holding more than 40 catalogue items, or a top-level category holding more than half of them, is reviewed for a split at RV-14 |
| Raised by, from | DD-IA3, section 7: GOV.UK's naming and size principles set beside R1 to R10 (DD-IA1, "What later units take") |
| Touches | IA4, Deliverable B, B.4; no J- row |
| Register rows (proposed) | none: R12's numbers are a threshold for a review, assumed, and the review reads them |
| Alternatives considered | no upper size (R5 covers only the low end); GOV.UK's 2 to 12 children (R7 already limits depth, and Perqo's categories have two children each) |
| Positions (proposed) | none recorded |
| Decided by | content team, as a change to its taxonomy's rules reviewed with support and engineering (IA4, B.4) |
| Decide at | FO-03, the vocabulary and content review's next meeting |
| Decision, date, reason | not decided |
| Version effect | a dated amendment to IA4, Deliverable B: two rules added, none changed |
| Places to apply | IA4, B.4: R11 and R12 after R10; not done |
| Told | IA review at FO-01; support at FO-06 |
| Supersedes, superseded by | none |
| Status | proposed |

## Deliverable · C · The Perqo controlled-vocabulary starter

*Face of this artefact (IA2, the notation sheet): controlled vocabulary of Perqo, the twenty terms every surface must share, each with its identifier, model name, preferred term on each surface, definition, synonyms to avoid and owner; fidelity F2 with F3's identifiers on every term (F3 when the variants are loaded as search synonyms, IA9, Deliverable B). Decision: what each shared thing is called, on which surface, what it means, which words are never used as its label, and who answers for it. Readers: content, engineering, support, sales, localisation, product management. Leaves out: the eight narrower terms and the flat facets' values (IA4, Deliverable B, B.2, whose preferred and variant terms stand), the states of the card and the employee beyond the names in C.1, labels in other languages (none is live), Admin's page names and the app's screen names (IA6, IA7). Owner: the content team as steward (DL-024, proposed; until it is decided, IA9's owners stand); version 1, dated 10 November 2026; every definition is assumed until the readers it names have agreed it (IA9, section 3.2: fidelity rises only through agreement). Perqo is fictional.*

### C.1 · The twenty terms

Every term the filed units already fix keeps its filed preferred terms and its filed identifier: the objects' O- identifiers (IA4, A.1) and the categories' CAT- identifiers (IA4, B.2). Three terms had no identifier and take one here, VOC-01 to VOC-03 (Perqo, fictional). Surface columns give each surface's preferred term, from IA1, IA2, IA4 and IA8's shared-objects table; "not shown" means the surface does not name it. "Synonyms to avoid" are never used as a label on any surface; where IA2 or IA4 records them as variant terms they stay loaded as search synonyms, which is R4's rule. Words marked *new* are set here; the rest are filed. Owners follow section 3.2's rule.

| ID | Term (model name) | Admin | App | perqo.com | Definition | Synonyms to avoid | Owner |
|---|---|---|---|---|---|---|---|
| O-01 | client | Company | not shown | Customers | a company that has a contract with Perqo for its employees' benefits, from its contract start date to its contract end date | account, alone (the app's Account is the employee's own; account owner is a role); organisation *new* | IA designer |
| O-02 | admin user | Admins; each with a role: HR manager, finance manager; one also account owner | not shown | For HR and finance teams (the Help centre's audience) | a person at a client who signs in to Perqo Admin, with the role HR manager or finance manager; exactly one is also the client's account owner | user, alone; manager, alone *new* | IA designer |
| O-03 | employee group | Employee group | not shown | Teams and groups | a set of a client's employees who follow one policy; a client's departments enter as groups, and a group need not be a department (IA10, section 2.7) | department; team, in Admin and the app *new* | IA designer |
| O-04 | policy | Policy | not shown; its effect shows as open categories and "Claims over the limit need HR approval" | Policies | the rules one employee group follows: its open categories, its auto-approve limit and its covered items | rules, as a label; plan (Pricing's plans are Perqo's prices) *new* | IA designer |
| O-05 | employee | Employees; Invited, Active, Left | Profile (the employee's own record) | not shown | a person at a client who is invited to the Perqo app and spends benefits; belongs to one employee group | user; member; staff *new* | IA designer |
| O-06 | allocation | Budget (one group's allocations for a category and period, or one employee's on their record) | Balance | Benefits budget | the amount one employee may spend in one category in one period, with what is spent and what remains | allowance, credit (IA2's variants); wallet *new* | IA designer |
| VOC-01 | period (an attribute of the allocation) | period | period | per period, in sales' words (BR-3) | the span of time an allocation covers; its length is left free (register) | month, year, cycle (the product cycle of IA9 is another thing) *new* | product management |
| F-CAT | benefit category | category; open categories | Benefits; each category by name | Benefits | one of the four top-level values of the benefit-category facet; an employee holds one allocation per open category and period | perk (the as-is "Perks" was the offers list, IA3); benefit type *new* | content team |
| CAT-HEA | Health | Health | Health | Health | physical and mental health (IA4, B.2) | wellbeing (IA2's variant); wellness *new* | content team |
| CAT-LEA | Learning | Learning | Learning | Learning | learning anything, work-related or not (IA4, B.2) | education, training (IA2's variants) | content team |
| CAT-MOB | Mobility | Mobility | Mobility | Mobility | getting around (IA4, B.2) | transport, commuting (IA2's variants) | content team |
| CAT-MEA | Meals | Meals | Meals | Meals | food and eating (IA4, B.2) | food (IA2's variant) | content team |
| O-13 | catalogue item | Covered items, in Policies | What's covered, on each category screen | the catalogue examples on each category page (M-08) | one thing an employee can spend benefits on, classified by the four facets, with one narrower term and so one category (IA4, B.3) | product (perqo.com's Product is Perqo itself); perk *new* | content team |
| O-07 | transaction, type claim | Claim | Claim | Claims | a request by an employee to be paid back for a receipt, checked against the group's policy and spending from one allocation | refund, reimbursement, expense (IA2's variants) | IA designer |
| VOC-02 | claim status | Submitted, Approved, Rejected, Paid | the same four | not shown | where a claim is in its lifecycle; Paid and Rejected are end states (IA2, section 5.3) | Pending (the as-is app's word, IA3); Declined (a declined attempt at the till is another thing, IA8, section 4.5) | product management |
| VOC-03 | auto-approve limit (an attribute of the policy) | auto-approve limit | the limit, in "Claims over the limit need HR approval" | the auto-approve limit (BR-3) | the amount at or under which a claim within its category's balance is approved without HR (IA8, DT-2); its amount is left free (register) | threshold; cap *new* | product management |
| O-08 | transaction, type card payment | Card payment, in Reports | Purchase | Card payments | a payment with the Perqo card at a merchant that accepts it, spending from the allocation of that merchant's category | transaction (the model's word, never a label); charge *new* | IA designer |
| O-09 | card | Perqo card: Active, Frozen, Not issued, Cancelled | Card | Perqo card | the payment card Perqo issues to an employee, at most one per employee | Blocked, Locked (the state is Frozen); debit card *new* | IA designer |
| O-11 | merchant | not shown | the merchant's name on a Purchase | For merchants | a business that accepts the Perqo card, assigned one narrower term by Perqo | vendor; partner (the partnerships team's word for its relationship) *new* | IA designer |
| O-12 | offer | not shown | Card offers | not shown | a discount a merchant publishes for Perqo cardholders, for one catalogue item | Perks, Discover (the as-is labels, IA3); deal *new* | IA designer |

Several terms are not shown on some surface and are still shared, because each surface depends on them: the policy's effect is what the app shows as open categories and the rule line (IA1; IA6, Deliverable C), and the merchant and the offer reach the app through Purchases and Card offers (IA8, D.1, X-10).

### C.2 · How the vocabulary is used and kept

1. **A label on any surface is the term's preferred term for that surface.** A new label is a new term or a rename, and goes through Deliverable B.
2. **A synonym to avoid is never a label.** Where it is a recorded variant it stays a search synonym, pointing to one term (R4); RV-13 reads every release for it.
3. **The model name is the team's word** in code, tickets and conversation between design and engineering, and the surface labels are its recorded translations (IA7, section 6.2). Engineering keeps the model-name column with the IA designer.
4. **A language column is added per live language,** one preferred term per surface per language (SKOS, section 5, S14, read 10 November 2026; B.4, rule 2), and each cell is marked tested or assumed.
5. **Each term's owner keeps its definition true** and is asked first about a change; the decider is the one A.2 names.
6. **A term used by two concepts takes a qualifier in brackets** (R11, proposed; DL-026). None of the twenty needs one today.

### C.3 · Why these twenty

The twenty are the concepts that appear on at least two of Perqo's surfaces or functions and that a surface's label could drift from: the ten objects IA4 drew in tone 5, shared (IA4, A.1: client, employee group, policy, employee, allocation, claim, card payment, card, offer, catalogue item); the admin user and the merchant, which cross between Admin and perqo.com and between the merchant side and the app; the benefit-category facet and its four categories, which every surface classifies by; and three terms whose words reach every surface through a rule: the period, the claim's status and the auto-approve limit. The eight narrower terms are left in IA4's table, where their preferred and variant terms already stand, because they are shown only inside the app's What's covered and the catalogue (section 1.2).

## What later units take

DD-IA3 is the course's last unit. **The final audit** takes the twenty terms of Deliverable C as the check of every label in the vocabulary against the filed units' labels, each term's filed identifier kept; the decision rights of A.2 against IA9's D.1, which they must not contradict; DL-023 to DL-026 as the log's state at this unit's date, beside DL-011 to DL-022, all proposed; the register's process part, AR-50 to AR-64, as the rows the audit's sample may draw from; and section 7's table, whose every GOV.UK principle is quoted from the publication read on 10 November 2026. The governance model and the change-request process are built to be used without the rest of the course: each row cites the unit that defines it.

## Perqo facts set by this unit

Every fact below is a course convention (Perqo, fictional), never evidence about the world. Each keeps every registered fact; none renames an IA1 to IA12, DD-IA1 or DD-IA2 label, object, attribute or relationship. DL-023 to DL-026 are proposed, so no filed artefact changes at this unit's filing.

| Fact | Set in | Left free |
|---|---|---|
| A term is owned by the owner of the artefact that defines it, and a term whose meaning is a rule or a contract term by product management; the owner is asked first, and the decider is IA9's D.1's | section 3.2; Deliverable C | none |
| The roles: strategy owner (leadership), rule owner (product management), vocabulary steward (content team, DL-024), term owner, language owner (localisation, one per live language), market module owner, applier, signal reader | Deliverable A, A.1 | named people |
| The decision rights for nine kinds of change, as A.2 gives them | Deliverable A, A.2 | none |
| FO-10, the language and market review, with its chair, members, inputs, outputs and cadence; dormant until leadership decides a second language at FO-09; TP-05's meeting FO-10 (DL-023, proposed) | Deliverable A, A.3 | its meetings' length |
| Additions to FO-01, FO-02, FO-03, FO-04 and FO-09 as A.3 gives them | Deliverable A, A.3 | none |
| Reviews RV-13 label drift check, RV-14 term counts, RV-15 search per language, RV-16 owner check, and RV-07 extended to duplication, with checks, cadences, triggers and owners | Deliverable A, A.4 | none |
| The measurement model's reads by forum, per language once there are two | Deliverable A, A.4 | every result |
| Escalation defaults: a term keeps its definition while its owner is silent; an untranslated label shows the English term, marked "untranslated", and its change stays accepted; no second language until leadership decides | Deliverable A, A.5 | which markets and languages come next (leadership's decision, A.5) |
| The register's process part: AR-50 to AR-64, every row at C0 and not run on 10 November 2026 | Deliverable A, A.6 | the results |
| The request's five term fields; the six operations with their identifier, version, migration and decider; the flow's eight steps; the told list for terms | Deliverable B, B.1 to B.3, B.5 | none |
| Perqo keeps one taxonomy for every market; a market changes what policies cover and what market-marked modules hold, never a category | section 5.3; Deliverable B, B.4 | none |
| Identifiers created from today carry no word of any language; CAT-HEA and the other existing codes are kept and never translated | section 5.1; Deliverable B, B.4 | none |
| English keeps the root and every address; another language takes a language subdirectory; a category page is perqo.com/{language}/{section path in that language}/cat-hea/{preferred term in that language}, found by its identifier, other paths redirecting | Deliverable B, B.4 | the language tags' form |
| T-14 loads the synonyms of the visitor's language only, from that language's logs and tickets (DL-025, proposed) | Deliverable B, B.4 | none |
| No software outside Perqo reads the taxonomy today; a published version and mapping only when one does | section 4.1; Deliverable B, B.4, rule 7 | whether one ever does |
| DL-023 to DL-026, proposed; R11 and R12 proposed in DL-026, R12's thresholds 40 items and half of the catalogue | Deliverable B, B.6 | their decisions |
| The controlled-vocabulary starter: twenty terms with definitions, synonyms to avoid and owners; VOC-01 period, VOC-02 claim status, VOC-03 auto-approve limit; the synonyms marked *new* | Deliverable C | the period's length and the limit's amount (register) |

## Sources

- Berners-Lee, Tim. "Cool URIs Don't Change". W3C, 1998 (W3C style guidance; cited through IA4, section 5). [w3.org, cool URIs](https://w3.org/Provider/Style/URI)
- Dub, Sam. "Our plans to improve navigation on GOV.UK". GDS blog, 17 May 2021, read 10 November 2026 (practice, a maker's account). [gds.blog.gov.uk, navigation plans](https://gds.blog.gov.uk/2021/05/17/our-plans-to-improve-navigation-on-gov-uk)
- eBay Developers Program. "Finding categories for a listing". Read 10 November 2026 (platform documentation). [developer.ebay.com, sell categories](https://www.developer.ebay.com/api-docs/sell/static/metadata/sell-categories.html)
- Evans, Eric. *Domain-Driven Design Reference: Definitions and Pattern Summaries*. Domain Language, 2015 (cited through IA7, section 6.2). [domainlanguage.com, DDD Reference](https://domainlanguage.com/wp-content/uploads/2016/05/DDD_Reference_2015-03.pdf)
- Furnas, George W., Thomas K. Landauer, Louis M. Gomez and Susan T. Dumais. "The Vocabulary Problem in Human-System Communication". *Communications of the ACM* 30, no. 11 (1987): 964 to 971 (cited through IA3, section 4.2, and IA4, section 1.1). [cacm.acm.org, vocabulary problem](https://cacm.acm.org/research/the-vocabulary-problem-in-human-system-communication)
- GOV.UK Developer Documentation. "How the topic taxonomy works". Last updated 4 May 2022, read 10 November 2026 (platform documentation; the page warns it may be out of date). [docs.publishing.service.gov.uk, taxonomy](https://docs.publishing.service.gov.uk/manual/taxonomy.html)
- Government Digital Service. "GOV.UK Taxonomy principles". Published 13 June 2019, updated 9 September 2026, read 10 November 2026 (publisher's documentation). [gov.uk, taxonomy principles](https://www.gov.uk/government/publications/govuk-topic-taxonomy-principles/govuk-taxonomy-principles)
- Halvorson, Kristina, and Melissa Rach. *Content Strategy for the Web*. 2nd ed. New Riders, 2012. Ch. 9 (cited through IA1, section 2.3, and IA9, section 4.1).
- Hedden, Heather. *The Accidental Taxonomist*. 3rd ed. Information Today, November 2022. Publisher's description, read 10 November 2026. [books.infotoday.com, Accidental Taxonomist](https://books.infotoday.com/Ebooks/489_The-Accidental-Taxonomist-Third-Edition.htm)
- ISO. *ISO 25964-1:2011, Information and documentation — Thesauri and interoperability with other vocabularies — Part 1: Thesauri for information retrieval*. Edition 1, August 2011; confirmed 2022. Publisher's page, read 10 November 2026 (standard). [iso.org, ISO 25964-1](https://www.iso.org/standard/53657.html)
- ISO. *ISO 25964-2:2013, Information and documentation — Thesauri and interoperability with other vocabularies — Part 2: Interoperability with other vocabularies*. Edition 1, March 2013; confirmed 2023. Publisher's page, read 10 November 2026 (standard). [iso.org, ISO 25964-2](https://www.iso.org/standard/53658.html?browse=tc)
- Laubheimer, Page. "Taxonomy 101: Definition, Best Practices, and How It Complements Other IA Work". Nielsen Norman Group, 3 July 2022 (cited through IA2, section 1.2). [nngroup.com, taxonomy 101](https://www.nngroup.com/articles/taxonomy-101/)
- McCloskey, Marieke. "Intranet Information Architecture (IA) Trends". Nielsen Norman Group, 23 February 2014 (cited through IA10, section 2.7). [nngroup.com, intranet IA trends](https://www.nngroup.com/articles/intranet-information-architecture-ia/)
- NISO. *ANSI/NISO Z39.19-2005 (R2010): Guidelines for the Construction, Format, and Management of Monolingual Controlled Vocabularies*. Publication page, dated 13 May 2010, read 10 November 2026 (standard). [niso.org, Z39.19](https://niso.org/publications/ansiniso-z3919-2005-r2010)
- Rosenfeld Media. *Managing Chaos: Digital Governance by Design*, by Lisa Welchman. Publisher's page: contents and FAQ, read 10 November 2026. [rosenfeldmedia.com, Managing Chaos](https://rosenfeldmedia.com/?p=187514)
- Rosenfeld, Louis, Peter Morville and Jorge Arango. *Information Architecture: For the Web and Beyond*. 4th ed. O'Reilly, 2015. Ch. 10 (cited through IA2, section 1.2, and IA4, section 3.1). [oreilly.com, ch. 10](https://www.oreilly.com/library/view/information-architecture-4th/9781491913529/ch10.html)
- Shopify. product-taxonomy repository, README. GitHub, version badge 2026-10, read 10 November 2026 (vendor documentation). [github.com, Shopify product taxonomy](https://github.com/Shopify/product-taxonomy)
- Stephens-Manassiev, Si. "An update on the GOV.UK taxonomy". Inside GOV.UK, 12 February 2019, read 10 November 2026 (practice, a maker's account). [insidegovuk.blog.gov.uk, taxonomy update](https://insidegovuk.blog.gov.uk/2019/02/12/an-update-on-the-gov-uk-taxonomy/)
- W3C. *SKOS Simple Knowledge Organization System Reference*. W3C Recommendation, 18 August 2009. Sections 5 to 8 and 10; integrity conditions S13 and S14. Read 10 November 2026 (standard). [w3.org, SKOS Reference](https://www.w3.org/TR/2009/REC-skos-reference-20090818)
- W3C Internationalization. "Text size in translation". Undated as read, 10 November 2026 (standards body's guidance; reports IBM's figures). [w3.org, text size in translation](https://www.w3.org/International/articles/article-text-size/index.en)
- Welchman, Lisa. "Stopping the Infighting About Digital Standards". A List Apart, 3 March 2015, excerpt of *Managing Chaos*, ch. 5. Read 10 November 2026 (practice). [alistapart.com, digital standards](https://alistapart.com/article/stopping-the-infighting-about-digital-standards/)
- Welchman, Lisa. "Managing Chaos: Digital Governance by Design". UXmatters, 4 May 2015, sample chapter of *Managing Chaos*, ch. 7, "Getting It Done". Read 10 November 2026 (practice). [uxmatters.com, sample chapter](https://www.uxmatters.com/mt/archives/2015/05/managing-chaos-digital-governance-by-design.php)
- Cited through the filed units, for claims made there: Colyer, "How do committees invent?", the morning paper, 2019, for Conway 1968 (IA10); Google Search Central, "Localized Versions of your Pages", checked 3 November 2026 (IA5; vendor documentation); DD-IA1's observations of 10 November 2026 of GOV.UK's labels, Stripe's documentation and Airbnb's help article (DD-IA1, section 2 and "What later units take"). Full references in IA5, IA10 and DD-IA1, Sources.

## Unsure list

- Welchman, *Managing Chaos*: only chapter 5 (the A List Apart excerpt) and chapter 7 (the UXmatters sample chapter) were read, with the publisher's contents and FAQ; chapters 2 and 6, which the titles show treat the team's placement and five design factors, were not read, so the organisational models the book may describe are not named. That the excerpt is chapter 5 is the A List Apart page's statement.
- The ISO, NISO and W3C pages read list no clauses; no clause is cited for ISO 25964-1, ISO 25964-2 or Z39.19. The Z39.19 text itself was not opened (the PDF on NISO's site refused the fetch).
- SKOS: only the first 100,000 of the page's 182,857 characters were read; section 10's definitions of the mapping properties were not reached, and the names of the change and history notes are as the fetch reported section 7.3's list.
- ISO 25964-1's page marks the standard "to be revised"; whether a new edition has been published since was not checked.
- Hedden, 3rd ed.: the chapter contents were not seen (the library record found was the 2nd edition's); the book is cited only for its scope as the publisher describes it.
- W3C, "Text size in translation": the page as read gave no author or date; IBM's figures are reported by the W3C, and IBM's guidelines were not seen.
- GOV.UK's developer documentation is dated 4 May 2022 and warns it may be out of date; the draft and published states of taxons are cited as it gives them, with no claim that they are current.
- Shopify's README gives no release date for the version on its badge (2026-10); the cadence is as the README states it.
- The Stripe and Airbnb observations are DD-IA1's of 10 November 2026 and were not re-read for this unit.
- Object: the Perqo controlled vocabulary, sections 2 and 5 and Deliverable C
