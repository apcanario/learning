---
code: IA3
title: How people find and understand things
course: ux · IA · Information Architecture
model: Opus 5.5
written: 2026-11-03
search: off
---

# IA3 · How people find and understand things

IA1 named the four systems an information architecture is made of (organisation, labelling, navigation and search) and IA2 gave the course a notation for drawing them. Neither said how to tell a good structure from a bad one. This unit supplies the evidence a structure is judged by: how people decide where to go next, what they believe the system is, how they sort things into groups, how they read labels, and when they type a query instead of following a link. Each section ends with what the evidence means for a structure, and the deliverable turns those consequences into a checklist and runs it over the navigation of the Perqo app as it stands today. Every figure here uses IA2's notation (IA2, section 5 and the notation sheet).

## 1 · Information foraging and information scent

### 1.1 · The theory

Information foraging theory was set out by Peter Pirolli and Stuart Card ("Information Foraging", *Psychological Review* 106, no. 4, 1999, pp. 643 to 675, [doi.org/10.1037/0033-295X.106.4.643](https://doi.org/10.1037/0033-295X.106.4.643)). Its abstract states the starting assumption: people adapt their strategies for seeking information, and where they can the environment they seek it in, so as to get valuable information at a lower cost. The paper builds three kinds of model on that assumption: patch models, for how long a person keeps working one cluster of information before moving to another; scent models, for how a person judges the value of information from the cues in front of them; and diet models, for which items a person decides to pursue at all. The theory is computed in a process model the authors call ACT-IF (Pirolli and Card 1999, abstract).

The term that matters most to a designer is scent. Card, Pirolli and colleagues define it in a later study of people using the web: "Information scent is the (imperfect) perception of the value, cost, or access path of information sources obtained from proximal cues", and on a web page those cues are things such as "link descriptors, images, contextual clues" (Stuart K. Card, Peter Pirolli, Mija Van Der Wege, Julie B. Morrison, Robert W. Reeder, Pamela K. Schraedley and Jenea Boshart, "Information Scent as a Driver of Web Behavior Graphs: Results of a Protocol Analysis Method for Web Usability", *CHI 2001*, ACM, [research.cs.vt.edu](https://research.cs.vt.edu/ns/cs5724papers/5.usageenvir.adaptation.card.infoscent.pdf)). The same study reports what people did as scent changed. They followed the links whose scent was high; they backtracked more often as scent fell; and when the scent at a site became low they switched to another site or to a search engine. The authors model this as a threshold: "So long as the potential rewards are above some threshold, then the user continues foraging at the site" (Card and others 2001).

Jakob Nielsen's NN/g article on the theory gives the same mechanism in the field's plainer words. A person estimates "a given hunt's likely success from the spoor", and "the scent must keep getting stronger and stronger, or people give up"; on the web, "each site is a patch"; and because moving between sites is cheap, the better search engines get at surfacing good sites, the less time people spend on any one of them ("Information Foraging: Why Google Makes People Leave Your Site Faster", Nielsen Norman Group, 29 June 2003, [nngroup.com/articles/information-foraging-leave-site](https://www.nngroup.com/articles/information-foraging-leave-site/)). He attributes the theory to the Palo Alto Research Center, "previously Xerox PARC", where Card, Pirolli and colleagues developed it (Nielsen 2003).

The loop the theory describes has four moves: enter a patch (a site, a screen or a list); read the cues (link labels, headings, the words around them); judge the scent (the likely value against the cost of getting there); then follow or leave: while the scent rises, follow the strongest cue into the next patch; when it falls, back up, search or leave. It is drawn here for the employee using the Perqo app (Perqo, fictional), so every box takes the app's tone:

```viz
{"kind": "flow", "per_row": 2, "caption": "Flow: the information-foraging loop, drawn for the employee in the Perqo app, so every step is tone 3; supports the decision on where in a structure scent has to be strong (section 1.1). Moves from Pirolli and Card, 'Information Foraging', Psychological Review 106(4), 1999 (patch, scent and diet models), and Card and others, CHI 2001 (proximal cues, backtracking, the threshold). The flow kind draws no arrow back to the first step and no branch, so the return is written as a '→ see' note and the two outcomes as bracketed conditions in the last step's note. Perqo is fictional.", "steps": [
 {"label": "Enter a patch", "note": "a site, a screen or a list", "tone": 3},
 {"label": "Read the cues", "note": "link labels, headings, the words around them", "tone": 3},
 {"label": "Judge the scent", "note": "likely value against the cost of getting there", "tone": 3},
 {"label": "Follow or leave", "note": "[scent rising] follow the strongest cue → see Enter a patch; [scent falling] back up, search or leave", "tone": 3}]}
```

What the theory predicts for a structure, in two parts. First, people judge a destination from its cues before they reach it, so the label and its surroundings are the whole of the evidence a person has at the moment of choice. Second, people leave when the scent falls below their threshold, which can happen long before they have exhausted what a structure holds; a structure can contain the right page and still lose the person one level above it. Both predictions rest on observed behaviour (Card and others 2001 is a protocol analysis of people's actions and remarks); the threshold itself is a model of that behaviour.

### 1.2 · What strong and weak scent look like in a label and a link

Raluca Budiu's NN/g article applies the theory to links. Scent "represents the user's imperfect estimate of the value that the source will deliver to the user", and it is "a relative concept": the same link can carry strong scent for one need and none for another. What shapes it is "the link label, the content that accompanies the link, the context in which the link appears, and any background knowledge" the person brings. Scent can also be lost on arrival: the good scent a link carried is wasted when the page it leads to does not confirm, on its first screen, that the person is in the right place, and then people "quickly decide that the page is not worth exploring any longer and simply leave" ("Information Scent: How Users Decide Where to Go Next", Nielsen Norman Group, 2 February 2020, [nngroup.com/articles/information-scent](https://www.nngroup.com/articles/information-scent/)).

Four pieces of NN/g evidence and guidance say what a strong label looks like.

- **The first words carry it.** In a study of 20 links from 20 sites with 80 participants, Nielsen tested how well people understood "the first 11 characters of a website's links and headlines". For 35% of the links, people who saw only those characters "hadn't the faintest idea of where the links would lead". The best link, "Gift Cards", let 85% predict its destination; the worst began with "Introducing", which "had no meaning", and none of the participants made a reasonable prediction from it. The weak links shared bland, generic words, made-up terms, and filler before the meaningful word ("First 2 Words: A Signal for the Scanning Eye", Nielsen Norman Group, 6 April 2009, [nngroup.com/articles/first-2-words-a-signal-for-scanning](https://nngroup.com/articles/first-2-words-a-signal-for-scanning)). This is a measured finding, for scanning in lists.
- **The label describes the destination.** Marieke McCloskey's guidance: "the most helpful link text describes the page that's being linked to"; avoid "Click here" and "Read more"; when people see the same link text twice they "assume that it goes to the same place"; and "The best links start with the most important words" ("Writing Hyperlinks: Salient, Descriptive, Start with Keyword", Nielsen Norman Group, 9 March 2014, [nngroup.com/articles/writing-links](https://www.nngroup.com/articles/writing-links/)). NN/g guidance, drawn from its usability studies.
- **Navigation labels name content, not actions or moods.** Page Laubheimer names three common faults, all of them low scent: vague calls to action ("Explore", "Connect"), forced parallel wording that bends a label to fit a pattern, and conversational labels such as "I want to…", which signal only that some tasks lie behind them. His test is that people "won't click on a category unless it's clear where they will go, *before* they click" ("3 Common IA Mistakes (that Are All Due to Low Information Scent)", Nielsen Norman Group, 16 April 2023, [nngroup.com/articles/3-ia-mistakes](https://www.nngroup.com/articles/3-ia-mistakes/)). NN/g guidance.
- **An icon alone carries little.** Aurora Harley: "There are a few icons that enjoy mostly universal recognition from users", and for the rest "a text label must be present alongside an icon to clarify its meaning in that particular context" ("Icon Usability", Nielsen Norman Group, 27 July 2014, [nngroup.com/articles/icon-usability](https://www.nngroup.com/articles/icon-usability/)). NN/g guidance.

The accessibility standard sets a floor under the same idea. WCAG's Success Criterion 2.4.4, Link Purpose (In Context), Level A, requires that "The purpose of each link can be determined from the link text alone or from the link text together with its programmatically determined link context, except where the purpose of the link would be ambiguous to users in general" (W3C, *Understanding SC 2.4.4*, [w3.org/WAI/WCAG21/Understanding/link-purpose-in-context](https://www.w3.org/WAI/WCAG21/Understanding/link-purpose-in-context); standard).

On the Perqo app's Home screen (Perqo, fictional), under the employee's balance, sits a link labelled "Learn more". It opens the Help centre article H-2.2.1, "Your balance explained", on perqo.com (IA2, section 5.3). A second "Learn more" sits under the offers banner on the same screen and opens a different place. Set against a label that names the page, the weak one fails on every count the sources above give:

| Test | "Learn more" | "Your balance explained" | Rests on |
|---|---|---|---|
| First two words | "Learn more": no subject | "Your balance": the subject | Nielsen 2009 |
| Names the destination | no | yes | McCloskey 2014; Budiu 2020 |
| Matches the page heading | no | yes: it is the article's title | Budiu 2020 (scent kept on arrival) |
| Unique on the screen | no: two on Home, two destinations | yes | McCloskey 2014 |
| Uses the employee's word | none | Balance, the app's preferred term (IA2 vocabulary) | Nielsen 2006 (section 4.2) |
| Purpose clear from the text alone | no | yes | WCAG 2.4.4 |

```viz
{"kind": "matrix", "caption": "Scent comparison: two labels for the same page, H-2.2.1 'Your balance explained' on perqo.com, as they would sit under the balance on the Perqo app's Home screen; supports the decision on which label the link carries (section 1.2). Rows are the tests in section 1.2's table, from Nielsen, 'First 2 Words', NN/g, 2009; McCloskey, 'Writing Hyperlinks', NN/g, 2014; Budiu, 'Information Scent', NN/g, 2020; Nielsen, 'Use Old Words', NN/g, 2006; and WCAG 2.4.4. Tone 6 marks a fault found in this review; tone 3 is the app, the only surface the labels sit on. Perqo is fictional.", "cols": ["Learn more", "Your balance explained"], "rows": [
 {"label": "First two words", "tone": 3, "cells": [{"mark": "no subject", "tone": 6}, "Your balance"]},
 {"label": "Names the destination", "tone": 3, "cells": [{"mark": "no", "tone": 6}, "yes"]},
 {"label": "Matches the page heading", "tone": 3, "cells": [{"mark": "no", "tone": 6}, "yes"]},
 {"label": "Unique on the screen", "tone": 3, "cells": [{"mark": "no: two on Home", "tone": 6}, "yes"]},
 {"label": "Uses the employee's word", "tone": 3, "cells": [{"mark": "none", "tone": 6}, "Balance"]},
 {"label": "Purpose clear from the text alone", "tone": 3, "cells": [{"mark": "no", "tone": 6}, "yes"]}],
 "legend": [{"mark": "tone 6", "means": "a fault found in this review", "tone": 6}, {"mark": "tone 3", "means": "the Perqo app", "tone": 3}]}
```

What scent means for a structure: every label in a navigation is a prediction about the page behind it, judged by people who scan from its first words; the page has to confirm the prediction on arrival; and a label that predicts nothing ("Learn more", "Discover", "Explore") costs the person a tap to find out, which the foraging threshold says many will not spend.

## 2 · Mental models: the user's and the system's

### 2.1 · Norman's three models

Don Norman's account, in *The Design of Everyday Things* (revised and expanded ed., Basic Books, 2013, ch. 1, sections "Conceptual Models" and "The System Image"), separates three things a team often talks about as one. The designer holds a conceptual model of how the product works. The person using it builds their own mental model from what they meet. Between them stands the system image: the product as built, with its labels, instructions and documentation, which is the only channel through which the designer's model reaches the person. When the system image does not make the designer's model clear and consistent, the person builds a wrong model, and acts on it (Norman 2013, ch. 1).

NN/g's definition puts the person's side in one line: "A mental model is what the user believes about the system (web, application, or other kind of product) at hand", and it helps the person "predict how a system will work". Megan Chan calls the gap between designers' and users' mental models one of "the biggest dilemmas in usability": designers know their own product in detail and so misjudge what is obvious, and much of a person's model of any one product comes from the others they use, since "Users spend most of their time on websites other than yours" ("Mental Models", Nielsen Norman Group, 26 January 2024, [nngroup.com/articles/mental-models](https://www.nngroup.com/articles/mental-models/)). Cooper and his co-authors add the engineering side: a product whose represented model follows the implementation model, how the software is built, instead of the user's mental model is hard to use (*About Face*, 4th ed., Wiley, 2014, ch. 1; IA1, section 2.4).

### 2.2 · Indi Young's mental models

Indi Young uses the term for something wider. Her *Mental Models: Aligning Design Strategy with Human Behavior* (Rosenfeld Media, 2008, [rosenfeldmedia.com/books/mental-models](https://rosenfeldmedia.com/books/mental-models/)) builds a mental model diagram from research with people about how they go about a purpose: the things they do and think are grouped into towers, and the towers into mental spaces, above a horizontal line; the organisation's existing content and features are placed below the line, under the towers they support; and the gaps, towers with nothing below them or features with no tower above, show where the organisation does not support what people do (summary from a review of the book, Anna Régeni, Ergomania, 3 April 2018, [ergomania.eu](https://ergomania.eu/indi-young-mental-models-review/), and from the book). Young described the diagram in her own words as one that "shows alignment between the things a person is doing and the ways an organization supports it" (comment on Chris Baum, "What Is Your Mental Model?", Boxes and Arrows, 14 February 2008, [boxesandarrows.com](https://boxesandarrows.com/what-is-your-mental-model/)).

The two senses answer different questions, on this unit's reading. Young's model is about the person's purpose and reasoning, and it exists before and apart from any product; it tells a team what a structure should serve. Norman's is about the person's belief of how this product works; it tells a team whether the structure it built is getting across. An IA needs both: the first to choose the groups, the second to check that the screens convey them.

### 2.3 · The gap at Perqo

In the Perqo data model (Perqo, fictional), an employee's money is an allocation per benefit category per period (IA1, section 2.4): four allocations, one per open category and period, for an employee whose group has all four open, and when a claim is submitted the system asks whether the amount is within the employee's balance (IA2, section 5.3). This unit extends that rule by fixing which balance the question reads (Perqo, fictional): the balance of the category the employee chose on the New claim form. The app's Home screen (Perqo, fictional) shows one Balance total on Home, the sum of the four category balances. The system image therefore says "one pot of money", and the designer's model says "four pots". An employee with money left in Meals and none in Learning who claims a course is rejected, over balance: a course claim is rejected while Home shows money left. From inside the employee's model, the rejection is arbitrary.

The claim lifecycle shows a second gap. The system has four states, Submitted, Approved, Rejected and Paid (IA1, section 5). The Claims screen lists claims in two groups, Submitted and Paid (IA2, section 5.3); in the app as it stands (Perqo, fictional), an approved claim stays in the Submitted group until it is paid, and a rejected claim leaves the list and appears only as a message in Notifications. An employee who reasons from the list (assumed: untested) concludes that a claim missing from the list is lost. The gap is that rejected claims cannot be found where claims are listed. Set side by side, the Perqo system, the app screens and the employee (assumed) differ on two things, money and claim status:

```viz
{"kind": "matrix", "caption": "Model gap: what the Perqo system holds (Norman's designer's model), what the app's screens show (the system image) and what an employee is assumed to conclude (the user's model), with the gap each produces; supports the decision on what the app's structure must make visible (section 2.3). Terms from Norman, The Design of Everyday Things, rev. ed., 2013, ch. 1. Tone 5 is the Perqo system, tone 3 the app and the employee, tone 6 a fault found in this review; the employee's column is assumed, not yet evidenced. Perqo is fictional; the allocation from IA1, section 2.4, the states from IA1, section 5, the Claims screen groups from IA2, section 5.3, the rest from this section.", "cols": ["Perqo system", "App screens", "Employee (assumed)", "Gap"], "rows": [
 {"label": "Money", "tone": 3, "cells": [{"mark": "four allocations, one per open category and period", "tone": 5}, "one Balance total on Home", "one pot of money", {"mark": "a course claim is rejected while Home shows money left", "tone": 6}]},
 {"label": "Claim status", "tone": 3, "cells": [{"mark": "Submitted, Approved, Rejected, Paid", "tone": 5}, "Submitted and Paid groups; rejected only in Notifications", "a claim missing from the list is lost", {"mark": "rejected claims cannot be found where claims are listed", "tone": 6}]}]}
```

What the evidence means for a structure: the structure is a large part of the system image, so the groups and labels a navigation shows are where the designer's model either reaches the person or does not. A structure has to show the units the system acts on (four category balances, four claim states) at the place where the person makes the decision those units govern.

## 3 · How people categorise

### 3.1 · Basic-level categories and prototype effects

Two findings from Eleanor Rosch's work in cognitive psychology bear on every navigation scheme.

**The basic level.** Rosch and her colleagues studied taxonomies of everyday things at three levels of inclusiveness (in their furniture taxonomy: furniture, chair, kitchen chair) and found that the middle level is special. Basic objects are "the most inclusive categories for which a concrete image of the category as a whole can be formed"; they are the first categorisations made in perceiving the environment, "the earliest categories sorted and earliest named by children", and the most codable and most used in language (Eleanor Rosch, Carolyn B. Mervis, Wayne D. Gray, David M. Johnson and Penny Boyes-Braem, "Basic Objects in Natural Categories", *Cognitive Psychology* 8, 1976, pp. 382 to 439, abstract, [cns.nyu.edu](https://www.cns.nyu.edu/~msl/courses/2223/Readings/Rosch-CogPsych1976.pdf)).

**Prototypes.** Categories are not sets of equal members. "Some chairs fit our idea or image of a chair better than others", and categories are "internally structured into a prototype (clearest cases, best examples of the category)", with other members ranged around it; in their words, "prototypicality is a function of the total cue validity of the attributes of items", and "family resemblance offers an alternative to criterial features in defining categories" (Eleanor Rosch and Carolyn B. Mervis, "Family Resemblances: Studies in the Internal Structure of Categories", *Cognitive Psychology* 7, no. 4, 1975, pp. 573 to 605, [courses.grainger.illinois.edu](https://courses.grainger.illinois.edu/cs440/fa2023/Quizzes/grad-readings/rosch-and-mervis.pdf)). George Lakoff's *Women, Fire, and Dangerous Things: What Categories Reveal about the Mind* (University of Chicago Press, 1987, [press.uchicago.edu](https://press.uchicago.edu/ucp/books/book/chicago/W/bo3632089.html)) built a theory of mind on these prototype effects: the mind and language build categories around prototypical examples, with other members extending out from the central cases (publisher's description).

These studies were run on objects and words, not on menus. The step to navigation is this unit's inference, and it is a short one. A navigation label for a group is usually a superordinate term (Health, Learning), for which, by Rosch's finding, no single image forms; the person arrives thinking of a basic-level thing (a gym, a train pass). They will place prototypical things quickly and stumble on members far from the prototype.

### 3.2 · The four challenges of organising information

The Polar Bear book's chapter on organisation systems opens with a section, "Challenges of Organizing Information", under four headings: Ambiguity, Heterogeneity, Differences in Perspectives and Internal Politics (Rosenfeld, Morville and Arango, *Information Architecture: For the Web and Beyond*, 4th ed., O'Reilly, 2015, ch. 6, [oreilly.com contents](https://www.oreilly.com/library/view/information-architecture-4th/9781491913529/part02.html)). In this course's words:

- **Ambiguity.** Words have more than one meaning, and things fit more than one group, so where an item goes is a judgement, and people judge differently.
- **Heterogeneity.** A collection holds items of different kinds and different granularity, and one scheme rarely suits all of them.
- **Differences in perspectives.** Whoever organises a structure organises it from their own view of the content, and the people using it hold other views.
- **Internal politics.** A structure decides which teams and which offers are visible, and that makes it a matter of influence inside the organisation.

The chapter then separates exact organisation schemes from ambiguous ones (ch. 6, headings); a scheme by topic, such as Perqo's four benefit categories, is of the ambiguous kind. One caution on the research method a team will reach for to settle such questions: in card sorts, participants "sometimes tend to group cards with similar keywords rather than conceptually organize them carefully", so a sort can reflect the card wording instead of the participants' model (Samhita Tankala, "Card Sorting: Pushing Users Beyond Terminology Matches", Nielsen Norman Group, 14 June 2024, [nngroup.com/articles/card-sorting-terminology-matches](https://www.nngroup.com/articles/card-sorting-terminology-matches/)). IA11 takes the methods up.

### 3.3 · What it means for a navigation scheme, shown on Perqo's benefits

Perqo's four categories, Health, Learning, Mobility and Meals, with their narrower terms (Health: Fitness, Therapy; Learning: Courses, Books; Mobility: Public transport, Bike; Meals: Restaurants, Groceries) are IA1's and IA2's (IA2, section 5.3). In the employee's world each holds basic-level things. The employee picks a category on the New claim form (IA2, section 5.3), and each client's policy (Perqo, fictional) lists what is covered under each category; the app's category screen (Perqo, fictional) shows the category's balance and a "What's covered" list of its narrower terms, with no examples.

Take six things an employee might claim for, as the example client's policy places them (Perqo, fictional); in the figure, each cell marked covered names the narrower term the item is covered under, and each cell marked may look here is a second place an employee may look. A gym membership (Health, Fitness), a train pass (Mobility, Public transport) and a coding course (Learning, Courses) are close to the prototypes of their categories. A cookery course is covered under Learning, Courses, and sits near Meals in meaning; a yoga class is covered under Health, Fitness, and its word "class" pulls it towards Learning; a bike helmet is covered under Mobility, Bike, and is also safety equipment, which pulls towards Health. For each far member there is a second place an employee may look; where that is, is assumed here and is the thing a test has to settle (IA11).

```viz
{"kind": "matrix", "caption": "Categorisation: six claimable things against Perqo's four benefit categories, showing where the example client's policy covers each and where an employee is assumed to look as well; supports the decision on which items each category screen names as examples and which need a route from a second category (section 3.3). Prototype structure from Rosch and Mervis, Cognitive Psychology 7(4), 1975; basic level from Rosch and others, Cognitive Psychology 8, 1976; ambiguity from Rosenfeld, Morville and Arango, 4th ed., 2015, ch. 6. Tone 3 is the app; tone 6 marks a place this review expects a failed look; every 'may look here' is assumed, to be tested. Perqo is fictional; categories and narrower terms from IA2, section 5.3; the items and the policy's placing of them from this section.", "cols": ["Health", "Learning", "Mobility", "Meals"], "rows": [
 {"label": "Gym membership", "tone": 3, "cells": ["covered: Fitness", null, null, null]},
 {"label": "Train pass", "tone": 3, "cells": [null, null, "covered: Public transport", null]},
 {"label": "Coding course", "tone": 3, "cells": [null, "covered: Courses", null, null]},
 {"label": "Cookery course", "tone": 3, "cells": [null, "covered: Courses", null, {"mark": "may look here", "tone": 6}]},
 {"label": "Yoga class", "tone": 3, "cells": ["covered: Fitness", {"mark": "may look here", "tone": 6}, null, null]},
 {"label": "Bike helmet", "tone": 3, "cells": [{"mark": "may look here", "tone": 6}, null, "covered: Bike", null]}],
 "legend": [{"mark": "covered", "means": "where the policy places the item, and its narrower term", "tone": 3}, {"mark": "may look here", "means": "a second place an employee is assumed to look", "tone": 6}]}
```

The consequences for a navigation scheme, each tied to its source:

- Name groups at the level people name things where the structure allows it, and where it does not (a benefits app needs its four superordinate categories), show basic-level examples inside each group, because the superordinate label raises no image of its members (Rosch and others 1976; this unit's inference).
- Expect prototypes to be found and far members to be missed, and give each far member a route from the group people will look in: a cross-listing, an example line, or a search synonym (Rosch and Mervis 1975; Furnas and others 1987 on aliasing, section 4.2).
- Keep each group to one kind of thing, because a heterogeneous group (a list of four benefit categories with a fifth item of another kind) forces a person to work out what the list is before choosing from it (Rosenfeld, Morville and Arango 2015, ch. 6, Heterogeneity; Laubheimer 2023, whose "Partner" example is a label over heterogeneous content).
- Organise from the person's perspective, and say in the deliverable when a group exists because a team asked for it (ch. 6, Differences in Perspectives, Internal Politics).

## 4 · Labelling

### 4.1 · The forms labels take

The Polar Bear book's labelling chapter starts from one sentence, "Labeling is a form of representation", and sorts labels into five varieties: labels as contextual links, labels as headings, labels within navigation systems, labels as index terms, and iconic labels (Rosenfeld, Morville and Arango 2015, ch. 7, section headings, [oreilly.com](https://www.oreilly.com/library/view/information-architecture-4th/9781491913529/ch07.html)). In the Perqo app (Perqo, fictional): "Your balance explained" is a contextual link; Claims at the top of its screen is a heading; Home, Benefits, Claims, Card and Account in the tab bar are navigation labels; the variant terms "allowance" and "refund" in IA2's controlled vocabulary are index terms, the words search should match (IA2, section 5.3); and the "+" on Home is an iconic label. Each form is read differently: a navigation label is scanned among its neighbours and judged by its first word or two (Nielsen 2009), a heading is read on arrival to confirm the choice (Budiu 2020), an index term is never seen and only matched.

### 4.2 · Why vocabulary mismatch happens

The measured finding at the root of this is old and strong. George Furnas, Thomas Landauer, Louis Gomez and Susan Dumais studied the words people chose spontaneously for objects in five application domains and found the variability "surprisingly large": "In every case two people favored the same term with probability <0.20." Their simulations showed that access through one designer's favourite word "will result in 80-90 percent failure rates in many common situations", and that the optimal strategy, "unlimited aliasing" (letting many words reach the same thing), gives "several-fold improvements" ("The Vocabulary Problem in Human-System Communication", *Communications of the ACM* 30, no. 11, 1987, pp. 964 to 971, abstract, [cacm.acm.org](https://cacm.acm.org/research/the-vocabulary-problem-in-human-system-communication)).

Three causes push a product's vocabulary further from its users' than chance alone would. Designers know the system's own words, and the gap between designers' and users' models is large (Chan 2024). Organisations name things for internal or marketing reasons: Nielsen advises "avoid made-up words in navigation menus, because users scan them for words they know", and "Play down marketese and internal vocabulary" ("Use Old Words When Writing for Findability", Nielsen Norman Group, 27 August 2006, [nngroup.com/articles/web-writing-use-search-keywords](https://www.nngroup.com/articles/web-writing-use-search-keywords/)). And the data model has words of its own that leak into screens (Cooper and others 2014, ch. 1). Susan Farrell's analysis of site-search logs finds the result: "Vocabulary mismatch problems happen a lot on websites that use branded terms" ("Search-Log Analysis: The Most Overlooked Opportunity in Web UX Research", Nielsen Norman Group, 30 July 2017, [nngroup.com/articles/search-log-analysis](https://www.nngroup.com/articles/search-log-analysis/)).

At Perqo (Perqo, fictional) the same allocation is "allocation" in the data model, Budget in Admin and Balance in the app, and employees also say "allowance" and "credit" (IA1, Deliverable; IA2, section 5.3). Furnas's finding says the variants will keep arriving whatever the app calls the thing, so the remedy is the one IA2 built: one preferred term per surface, with the variants recorded and fed to search as synonyms.

### 4.3 · The evidence on consistency and specificity

The evidence is of two strengths, and a designer should know which is which.

**Specificity** has measured support. Nielsen's 2009 study is a direct measurement: specific, front-loaded words ("Gift Cards") let most people predict a destination, and generic openers ("Introducing") let none do so (Nielsen 2009). Furnas and others 1987 is the measured case against relying on any single word, however specific. The guidance built on those findings is consistent across NN/g: "precise words are often better than short words" (Nielsen 2006); "Use clear, specific, and familiar wording for link labels", avoiding made-up words, jargon and abstract categories, and front-load key terms (Page Laubheimer, "Menu-Design Checklist: 17 UX Guidelines", Nielsen Norman Group, 7 June 2024, [nngroup.com/articles/menu-design](https://www.nngroup.com/articles/menu-design/)).

**Consistency** rests mostly on heuristics and standards. Nielsen's fourth usability heuristic reads "Users should not have to wonder whether different words, situations, or actions mean the same thing", and NN/g separates internal consistency, "within a product or a family of products", from external consistency with "established conventions in an industry or on the web at large" (Rachel Krause, "Maintain Consistency and Adhere to Standards (Usability Heuristic #4)", Nielsen Norman Group, 10 January 2021, [nngroup.com/articles/consistency-and-standards](https://www.nngroup.com/articles/consistency-and-standards/)). WCAG's Success Criterion 3.2.4, Consistent Identification, Level AA, requires that "Components that have the same functionality within a set of Web pages are identified consistently" (W3C, *Understanding SC 3.2.4*, [w3.org/WAI/WCAG20/Understanding/consistent-identification](https://www.w3.org/WAI/WCAG20/Understanding/consistent-identification); standard). McCloskey's observation that people assume identical link text leads to the same place (McCloskey 2014) is the behavioural reason both directions matter: one thing should carry one label, and one label should lead to one thing. The Polar Bear book's labelling guidelines argue for the same consistency across a labelling system (Rosenfeld, Morville and Arango 2015, ch. 7, "General Guidelines").

The limit to hold: consistency spreads a label; it does not make the label right. An app that labelled the allocation Budget on every screen would be consistent, and would still fail the employee, whose word is Balance (IA1, section 2.4); and an app that says Balance everywhere still needs "allowance" mapped for search.

## 5 · Search versus browse

### 5.1 · What the studies show

The early claim was that people sort into types. Nielsen reported in 1997 that "more than half of all users are search-dominant", "about a fifth of the users are link-dominant", and "the rest exhibit mixed behavior" ("Search and You May Find", Nielsen Norman Group, 14 July 1997, [nngroup.com/alertbox/9707b.html](https://www.nngroup.com/alertbox/9707b.html)). Jared Spool's team tested the claim on shopping sites: "we observed 30 users performing 121 different shopping tasks", and "there wasn't a single user out of 30 who always used the search engine first"; by site, "for 21% of the sites, every single user who visited only used search", "Thirty-two percent of the sites were link dominant", and "47% were not dominant to search or links". Spool reads the result as the site's design driving the behaviour more than any preference in the person, and adds that people said they always searched when they did not ("Are There Users Who Always Search?", UIE, 1 May 2001, [articles.centercentre.com](https://articles.centercentre.com/?p=15); practice: a consultancy's study, not peer-reviewed). The two disagree on what drives the choice, and the next study, a controlled one, finds the menus doing much of the driving.

Michael Katz and Michael Byrne ran controlled experiments on e-commerce sites and found that using site search was not faster or more accurate than browsing; that menu structure, the prominence of interface elements, information scent and the person's disposition all influenced whether people searched or browsed; and, on novel sites, that browsing was influenced by both the breadth and the scent of the menus. Their conclusion is a design rule: site search "should not be used to compensate for poor menu design" ("Effects of Scent and Breadth on Use of Site-Specific Search on E-Commerce Web Sites", *ACM Transactions on Computer-Human Interaction* 10, no. 3, 2003, pp. 198 to 220, abstract, [unpaywall.org](https://unpaywall.org/10.1145%2F937549.937551)).

Two further findings complicate the picture of search as a straight line to the target. Jaime Teevan and colleagues found, in a diary study of directed searches across email, files and the web, that "most of the search behavior we observed did not involve keyword search": people "navigated to their target with small, local steps using their contextual knowledge as a guide", even when they knew what they wanted, a pattern they call orienteering ("The Perfect Search Engine Is Not Enough: A Study of Orienteering Behavior in Directed Search", *CHI 2004*, ACM, [microsoft.com/research](https://www.microsoft.com/en-us/research/publication/perfect-search-engine-not-enough-study-orienteering-behavior-directed-search/)). Marcia Bates had argued earlier that a real search is "berrypicking": "the query itself (as well as the search terms used) is continually shifting", and searchers "gather information in bits and pieces instead of in one grand best retrieved set" ("The Design of Browsing and Berrypicking Techniques for the Online Search Interface", *Online Review* 13, no. 5, 1989, [pages.gseis.ucla.edu](https://pages.gseis.ucla.edu/faculty/bates/berrypicking.html)).

Donna Spencer gives practitioners a working frame for why the mix varies: four modes of seeking, known-item (the person knows what they want and the words for it), exploratory (some idea, not yet the words), "don't know what you need to know", and re-finding (returning to something already seen) ("Four Modes of Seeking Information and How to Design for Them", Boxes and Arrows, 14 March 2006, [boxesandarrows.com](https://boxesandarrows.com/four-modes-of-seeking-information-and-how-to-design-for-them/); practice). Known-item seeking with the right words suits search; the other three depend on browsing and on scent.

Taken together, for a structure: people search more when the menus give them weak scent, and search does not rescue them from a weak menu (Katz and Byrne 2003; Spool 2001 as practice); much finding is browsing in small steps even when the target is known (Teevan and others 2004); and whether a product needs search at all is the first question the Polar Bear book asks of a search system ("Does Your Product Need Search?", Rosenfeld, Morville and Arango 2015, ch. 9, heading). The Perqo app has no search (IA2, section 5.3); with five tabs and a few screens under each, that is defensible, provided its browsing carries scent. The Help centre on perqo.com does have search, and that is where the app's failures show.

### 5.2 · What search logs reveal about failed structures

The Polar Bear book lists search-log analysis among its user-research methods (Rosenfeld, Morville and Arango 2015, ch. 11, "Search Log Analysis"). Farrell calls it "one of the biggest missed opportunities in UX research" and names what a log shows. Zero-result queries "often indicate both misspellings and wanted information that the search engine can't find for some reason"; frequent queries for something the site holds point to a structure that hides it (her example is a store whose heating pads sat on a page under a name users would not expect); frequent queries for something the site does not hold are a content gap; and reformulated queries within one session signal a failed search. Her recommendations, NN/g guidance: log site search, read several months of data so a campaign's spike is not mistaken for a pattern, review the top queries and group those that express one need, add synonyms and misspellings, improve the no-results page, and remove personal identifiers before sharing a log (Farrell 2017).

Louis Rosenfeld, who wrote the book-length treatment (*Search Analytics for Your Site: Conversations with Your Customers*, Rosenfeld Media, 2011, [rosenfeldmedia.com](https://rosenfeldmedia.com/books/search-analytics/)), adds two points in an interview. Queries express needs "in their own words", which makes them closer to qualitative research than most analytics; and analytics show what happens without showing why, so findings from a log are hypotheses to be tested with people (Kristina Mausser, "Site Search Analytics: A Conversation with Lou Rosenfeld", UXmatters, 18 July 2011, [uxmatters.com](https://uxmatters.com/mt/archives/2011/07/site-search-analytics-a-conversation-with-lou-rosenfeld.php); interview, practice). That is the status IA12 gives search logs: proxy evidence, useful when no one can be interviewed, and labelled as proxy.

A slice of the Help centre's search log for the For employees section over one quarter (Perqo, fictional), its five most frequent queries in rank order, read for what each says about the app's structure:

| Rank | Query | What the search returned | What it suggests about the structure |
|---|---|---|---|
| 1 | refund | H-2.1.2, "Why was my claim rejected?", which says "refund" | Employees use IA2's variant term; the article does too, the app says Claim (IA2, section 5.3: already marked for update) |
| 2 | allowance | zero results | A variant of Balance with no synonym in search: Furnas's vocabulary problem, in the log |
| 3 | rejected claim | H-2.1.2 | Employees look outside the app for rejected claims, which the app's Claims list does not show (section 2.3; a hypothesis to test) |
| 4 | gym | zero results | A basic-level word for something covered under Health, Fitness; no article or synonym holds it (section 3.1) |
| 5 | approval | H-1.2.4, "Approval rules", a PDF written for HR | The rule that decides an employee's claim is not shown in the app where the claim is made |

Every row is a hypothesis about the structure; IA11 and IA12 say how each is tested.

## 6 · Findability and "don't make me think", with the limits of each

### 6.1 · Morville's findability

Peter Morville made findability a design quality in its own right. In his user-experience honeycomb, Findable is one of seven facets, beside Useful, Usable, Desirable, Accessible, Credible and Valuable, and his gloss is "We must strive to design navigable web sites and locatable objects, so users can find what they need" ("User Experience Design", Semantic Studios, 21 June 2004, [semanticstudios.com/user_experience_design](https://semanticstudios.com/user_experience_design/)). His book *Ambient Findability* (O'Reilly, September 2005, [oreilly.com](https://oreilly.com/library/view/ambient-findability/0596007655)) opens with a chapter, "Lost and Found", that defines findability as the quality of being locatable or navigable, the degree to which a particular object is easy to discover or locate, and the degree to which a system or environment supports navigation and retrieval (ch. 1). The definition joins the two halves of this unit: an object can be hard to find because its label carries no scent, and a system can be hard to navigate because its structure does not match its users' categories.

**The limits.** Findability says whether a thing can be found; it says nothing of whether, once found, the person understands it. Morville's own honeycomb makes findability one facet of seven, and the Polar Bear book gives finding and understanding a chapter each (Rosenfeld, Morville and Arango 2015, ch. 3, "Design for Finding", and ch. 4, "Design for Understanding"). Nielsen makes the same point about search listings: being found is the first step, and the person must still choose the listing and be served by the page (Nielsen 2006). The Perqo Balance on Home is perfectly findable, the first thing on the first screen, and it misleads (section 2.3). On this unit's reading, findability is a property of an object for a given task and person, so it is measured that way: a tree test measures it by "having users find the locations in the tree where specific resources or features can be found", with the visual design removed (Page Laubheimer, "Tree Testing: Evaluate Menu Labels and Categories", Nielsen Norman Group, 6 August 2023, [nngroup.com/articles/tree-testing](https://www.nngroup.com/articles/tree-testing/)).

### 6.2 · Krug's argument

Steve Krug's *Don't Make Me Think, Revisited* (3rd ed., New Riders, 2014) is the practitioner's statement of the same ground. Its first chapter is titled with its first law, "Don't make me think!"; its second, "How we really use the Web", argues from what Krug saw in usability tests that people scan pages, take the first reasonable option instead of the best, and muddle through without working out how things work (Krug 2014, chs 1 and 2). Its fourth chapter, "Animal, Vegetable, or Mineral?", states his second law, "It doesn't matter how many times I have to click, as long as each click is a mindless, unambiguous choice", and ties it to the "scent of information" (Krug 2014, ch. 4; excerpt at [peachpit.com](https://peachpit.com/articles/article.aspx?p=2170656)).

**The limits.** The book is argument from practice, a standard work and a persuasive one; its claims are Krug's observations from usability testing, and this unit cites it as practice. The second law says nothing about how a choice becomes mindless. That depends on the person's categories and vocabulary, which only research supplies (sections 2 and 3); the law states the target and leaves the method open. Its claim about clicks has partial measured support. NN/g reports that the "3-click rule" "has not been supported by data in any published studies to date", and cites Joshua Porter's 2003 test, in which drop-off did not increase past three clicks (Page Laubheimer, "The 3-Click Rule for Navigation Is False", Nielsen Norman Group, 11 August 2019, [nngroup.com/articles/3-click-rule](https://www.nngroup.com/articles/3-click-rule/)). But depth is not free: Kevin Larson and Mary Czerwinski found that "increased depth did harm search performance on the web", and that "a medium condition of depth and breadth outperformed the broadest shallow web structure overall" ("Web Page Design: Implications of Memory, Structure and Scent for Information Retrieval", *CHI 98*, ACM, 1998, pp. 25 to 32, [microsoft.com/research](https://www.microsoft.com/en-us/research/publication/web-page-design-implications-memory-structure-scent-information-retrieval/)). Each added level is one more choice that must stay unambiguous, and the deeper the structure, the harder that is to keep. Last, the book is about websites met by occasional visitors; on this unit's reading, a backoffice such as Perqo Admin, used daily by the same HR and finance managers, can ask more of its users' learning than Krug's readers' sites can, and an employee app opened a few times a month cannot.

## Deliverable · The findability and labelling checklist, applied to the as-is Perqo app

*For any structure, at review. Each item is a yes-or-no question about the structure, with the research it rests on. Below the checklist, it is applied item by item to the Perqo app's navigation as it stands. Perqo is fictional.*

### The as-is navigation (Perqo, fictional)

The navigation below is the Perqo app as it stands before IA6 (Perqo, fictional). It keeps everything IA1 and IA2 set: the tab bar, which carries the app's global routes, with its five tabs Home, Benefits, Claims, Card and Account; the four categories inside Benefits; the Claims screen grouped Submitted and Paid; New claim and Check and submit; the contextual route from the Claims screen to the claim articles; no search (IA1, section 5; IA2, section 5.3). It adds, as faults for the checklist to catch:

- **Home.** One Balance total, the sum of the four category balances, with a "Learn more" link under it to H-2.2.1 on perqo.com. A list of recent activity that mixes purchases and claims and shows a submitted claim as "Pending" (a claim shown as Pending). A banner labelled "Discover" that opens a list of offers. A "+" icon, with no text, that opens New claim.
- **Offers: the first merchant fact in the course.** Merchants that accept the Perqo card can publish offers (discounts for Perqo cardholders), which the app lists. The list is reached from Home's "Discover" banner, with a second "Learn more" under the banner, and again from the Benefits tab, where it sits as a fifth item labelled "Perks" below the four categories. The partnerships team asked for both placings.
- **Benefits.** Health, Learning, Mobility, Meals, then Perks. Each category screen shows its balance and a "What's covered" list of its narrower terms, with no examples.
- **Claims.** The Submitted and Paid groups; approved claims stay in Submitted until paid; rejected claims are not listed and appear only in Notifications. New claim asks for a category, an amount and a receipt; Check and submit follows. A link "Help with claims" opens the claim articles in the Help centre.
- **Card.** Card details, Purchases, Freeze card.
- **Account.** Profile, Notifications, Documents (which holds the "Approval rules" PDF, H-1.2.4, the file IA2's audit marked for removal), and Help, which opens the Help centre's home page on perqo.com, where both audiences start.

The as-is sitemap, in the notation: square-cornered boxes with type tags, every box in the app's tone 3, the faults the checklist finds in tone 6, and every route that leaves the app tagged `external` with a "→ see" note.

```viz
{"kind": "sitemap", "caption": "Sitemap: the Perqo app's navigation as it stands (as-is), F2, page types tagged; tone 3 is the app, tone 6 marks each element that fails an item of the checklist (item IDs in the notes); supports the decision on what IA6 replaces and what it keeps (Deliverable). The root names the surface and carries no type tag, because the tab bar is not a page; the five tabs are its children. Perqo is fictional; the tabs, the four categories, the Claims groups, New claim, Check and submit and the route to the claim articles from IA1, section 5, and IA2, section 5.3; every other element from this Deliverable.", "stack_from": 2, "root": {"label": "Perqo app", "note": "tab bar: global routes", "tone": 3, "children": [
 {"label": "Home", "type": "home", "tone": 3, "children": [
  {"label": "Balance", "type": "detail", "note": "one total; fails B1", "tone": 6},
  {"label": "Learn more", "type": "external", "note": "→ see H-2.2.1; fails A1, A2, A3, A5", "tone": 6},
  {"label": "Recent activity", "type": "index", "note": "claim shown as Pending; fails D2", "tone": 6},
  {"label": "Discover", "type": "index", "note": "offers; fails A1, D1, D2", "tone": 6},
  {"label": "+", "type": "form", "note": "→ see New claim; fails A4", "tone": 6}]},
 {"label": "Benefits", "type": "index", "tone": 3, "children": [
  {"label": "Health", "type": "detail", "note": "What's covered: no examples; fails C2, C3", "tone": 6},
  {"label": "Learning", "type": "detail", "note": "as Health", "tone": 6},
  {"label": "Mobility", "type": "detail", "note": "as Health", "tone": 6},
  {"label": "Meals", "type": "detail", "note": "as Health", "tone": 6},
  {"label": "Perks", "type": "index", "note": "offers again; fails C1, C4, D1, D2", "tone": 6}]},
 {"label": "Claims", "type": "index", "note": "Submitted, Paid; no rejected; fails B2, F2", "tone": 6, "children": [
  {"label": "New claim", "type": "form", "tone": 3, "children": [{"label": "Check and submit", "type": "form", "tone": 3}]},
  {"label": "Help with claims", "type": "external", "note": "→ see Claim articles", "tone": 3}]},
 {"label": "Card", "type": "section", "tone": 3, "children": [
  {"label": "Card details", "type": "detail", "tone": 3},
  {"label": "Purchases", "type": "index", "tone": 3},
  {"label": "Freeze card", "type": "form", "tone": 3}]},
 {"label": "Account", "type": "section", "tone": 3, "children": [
  {"label": "Profile", "type": "detail", "tone": 3},
  {"label": "Notifications", "type": "index", "tone": 3},
  {"label": "Documents", "type": "index", "note": "fails A1, C4, D1, F2", "tone": 6, "children": [{"label": "Approval rules", "type": "file", "note": "H-1.2.4, for HR", "tone": 6}]},
  {"label": "Help", "type": "external", "note": "→ see Help centre home; fails A3", "tone": 6}]}]}}
```

### The checklist

| ID | Ask of the structure | Rests on |
|---|---|---|
| **A · Scent** | | |
| A1 | Does every label name what is behind it, with no generic or call-to-action label ("Learn more", "Discover", "Explore")? | Card and others 2001 (scent from proximal cues); Budiu 2020; McCloskey 2014; Laubheimer 2023 |
| A2 | Does every label start with the word that tells it apart from its neighbours? | Nielsen 2009 (first 11 characters, 80 participants); McCloskey 2014; Laubheimer 2024 |
| A3 | Does every destination confirm, on its first screen, the label that led to it? | Budiu 2020 (scent lost on arrival); Card and others 2001 (backtracking as scent falls) |
| A4 | Does every icon that opens something carry a text label? | Harley 2014 |
| A5 | Does each label lead to one place, so that identical text never opens two destinations? | McCloskey 2014; WCAG 2.4.4 |
| **B · Mental models** | | |
| B1 | Does the structure show the units the system acts on, at the place where the person makes the decision those units govern? | Norman 2013, ch. 1 (system image); Cooper and others 2014, ch. 1 |
| B2 | Can the person find a thing in every state it can be in, where they already look for it? | Norman 2013, ch. 1; Chan 2024 (models predict how a system works) |
| **C · Categories** | | |
| C1 | Is each group one kind of thing? | Rosenfeld, Morville and Arango 2015, ch. 6 (Heterogeneity); Laubheimer 2023 |
| C2 | Where a group's label is a superordinate term, does the group show basic-level examples of what it holds? | Rosch and others 1976; this unit's inference (section 3.1) |
| C3 | Does every far member of a group have a route from the other group people are expected to look in? | Rosch and Mervis 1975 (prototypes); Rosenfeld, Morville and Arango 2015, ch. 6 (Ambiguity); Furnas and others 1987 (aliasing) |
| C4 | Is each group organised from the person's perspective, with any group that exists for an internal reason named as such in the deliverable? | Rosenfeld, Morville and Arango 2015, ch. 6 (Differences in Perspectives; Internal Politics) |
| **D · Labels and vocabulary** | | |
| D1 | Are labels in the users' words, with no internal, branded or made-up terms? | Nielsen 2006; Laubheimer 2024; Farrell 2017 |
| D2 | Does one thing carry one label, and one label mean one thing, across the surface? | Krause 2021 (heuristic 4); WCAG 3.2.4; McCloskey 2014 |
| D3 | Are the variant terms people use recorded and mapped to the preferred term, for search and for support? | Furnas and others 1987; Farrell 2017; IA2, section 1.2 |
| **E · Search and browse** | | |
| E1 | Does browsing reach every task without search, so that search is never the patch for a weak menu? | Katz and Byrne 2003; Spool 2001 (practice) |
| E2 | Where search exists, are its logs read for zero-result, reformulated and frequent queries, and each finding treated as a hypothesis to test? | Farrell 2017; Mausser 2011 (Rosenfeld, practice); Rosenfeld, Morville and Arango 2015, ch. 11 |
| E3 | Is re-finding supported: can a person return to what they have already seen or done? | Spencer 2006 (practice) |
| **F · Findability** | | |
| F1 | Is every choice on the path to a task unambiguous for the person making it, at every level? | Krug 2014, ch. 4 (practice); Larson and Czerwinski 1998 (depth) |
| F2 | Is everything a person needs for a task reachable by a route from where they are when they need it? | Morville 2004; Morville 2005, ch. 1 |

### The checklist applied to the as-is Perqo app (Perqo, fictional)

| ID | Verdict | What in the as-is decides it | Fix (for IA6) |
|---|---|---|---|
| A1 | **Fail** | "Learn more" (Home, twice), "Discover" (Home) and "Documents" (Account) name nothing behind them | Rename the balance link "Your balance explained"; rename the offers list "Card offers"; remove Documents (see C4) |
| A2 | **Fail** | "Learn more" opens with no subject; every other label passes (Home, Benefits, Claims, Card, Account, the four categories, New claim, Check and submit, Purchases, Freeze card, Profile, Notifications, Help) | "Your balance explained" starts with the subject; keep every other label as it is |
| A3 | **Fail** | "Learn more" opens a page titled "Your balance explained"; Account's Help opens the Help centre home, where the employee must first choose an audience | The renamed link matches its page; Help opens For employees directly |
| A4 | **Fail** | The "+" on Home has no text | Label it "New claim", the same words as the Claims screen's button |
| A5 | **Fail** | Two "Learn more" links on Home open two destinations | Each link carries its own destination's name (A1) |
| B1 | **Fail** | Home shows one Balance total; the system checks a claim against one category's balance (section 2.3) | Show the four category balances on Home under Balance; show the chosen category's balance on New claim and on Check and submit (IA2's Check and submit already shows the balance after the claim) |
| B2 | **Fail** | Approved claims hide in Submitted; rejected claims are only in Notifications (section 2.3) | Group the Claims list by all four states, Submitted, Approved, Rejected and Paid, as the lifecycle has them (IA1, section 5; IA2, section 5.3) |
| C1 | **Fail** | Perks, a list of merchant offers, sits in the list of benefit categories | Remove Perks from Benefits; Benefits holds the four categories only |
| C2 | **Fail** | "What's covered" lists narrower terms (Fitness, Therapy) with no examples; "gym" returns zero results in the Help centre (section 5.2) | Under each narrower term, show the policy's examples in basic-level words (gym membership, train pass, coding course), taken from the employee group's policy |
| C3 | **Fail** | A cookery course, a yoga class and a bike helmet have no route from the second category an employee is assumed to look in (section 3.3) | List far members in both places with the covered category named ("Cookery course: covered under Learning"); test the assumed second places (IA11) |
| C4 | **Fail** | Offers appear twice because the partnerships team asked; approval rules sit in Documents because Product holds them as a PDF for HR | One placing for offers, recorded in the deliverable as a business request; replace Documents with the rule in the employee's terms where the claim is made: "Claims over the limit need HR approval" on New claim, the limit read from the group's policy |
| D1 | **Fail** | "Documents", "Perks" and "Discover" are the organisation's words; employees search "approval", "allowance", "gym" (section 5.2) | Remove Documents and Perks; "Card offers" names what the list holds. Employee words go to D3 |
| D2 | **Fail** | A submitted claim is "Pending" on Home and Submitted on Claims; offers are "Discover" on Home and "Perks" in Benefits | Use Submitted everywhere; one label for offers, "Card offers", in one place, which IA6 chooses |
| D3 | **Fail** | IA2's vocabulary records "allowance" and "refund" as variants, but the Help centre's search does not map them: "allowance" returns zero results | Feed IA2's variant terms to the Help centre search as synonyms; add "gym" and the other basic-level examples from C2 as variants of their narrower terms |
| E1 | **Pass, with a watch** | The app has no search, and every task in the as-is is reachable by browsing; the faults above weaken scent on those routes without removing them | No search in the app for now; the decision is revisited when the Help centre log (E2) shows employees searching for things the app holds |
| E2 | **Fail** | The Help centre logs searches, and nobody reads them; the five queries in section 5.2 were found only for this review | Support reads the For employees log each quarter, groups the top queries, and records each finding as a hypothesis for IA11 and IA12 |
| E3 | **Pass** | Claims lists past claims; Purchases lists past purchases; Notifications holds past messages | Keep |
| F1 | **Fail** | On Home, three of five elements are ambiguous ("Learn more", "Discover", "+"); in Benefits, the fifth item is of another kind | Fixed by A1, A4 and C1; the tabs themselves pass and stay |
| F2 | **Fail** | The approval rule that decides a claim is reachable only through Account, Documents, a PDF written for HR; a rejected claim is reachable only through Notifications | Fixed by C4 and B2: the rule shows on New claim, rejected claims show in Claims |

**What IA6 keeps.** Every label that passes: the five tabs Home, Benefits, Claims, Card and Account; Balance as the app's preferred term; the four categories Health, Learning, Mobility and Meals and their narrower terms; New claim; Check and submit; Help with claims; Card details, Purchases and Freeze card; Profile, Notifications and Help; and the status names Submitted and Paid, joined by Approved and Rejected.

**What this hands on.** The criteria IA4 chooses organisation schemes by are C1 to C4; the criteria IA6 chooses navigation by are A1 to A5, B1, B2 and F1, F2. IA6 replaces the as-is navigation above and keeps the labels listed. The behaviours IA11's methods measure are the ones this checklist cannot settle from a desk: where employees look for far members (C3), whether they read a missing claim as lost (B2), and whether the renamed labels predict their pages (A1 to A3), by tree test and by first-click test. The Help centre log in section 5.2 is the proxy evidence IA12 works from when no research can be done, with each row labelled a hypothesis.

*Face of this artefact (IA2, the notation sheet): findability and labelling checklist with its application to the Perqo app as-is, F2; decision: what the app's navigation replaces and keeps; readers: design, product management, content, support; leaves out: Perqo Admin and perqo.com beyond the Help centre, visual design, any measured result (every "assumed" above is untested); owner: the IA designer; dated 3 November 2026; Perqo is fictional.*

## Sources

- Bates, Marcia J. "The Design of Browsing and Berrypicking Techniques for the Online Search Interface". *Online Review* 13, no. 5 (1989). [pages.gseis.ucla.edu/faculty/bates/berrypicking.html](https://pages.gseis.ucla.edu/faculty/bates/berrypicking.html)
- Baum, Chris. "What Is Your Mental Model?" Boxes and Arrows, 14 February 2008, with Indi Young's comment. [boxesandarrows.com/what-is-your-mental-model](https://boxesandarrows.com/what-is-your-mental-model/) (interview; practice).
- Budiu, Raluca. "Information Scent: How Users Decide Where to Go Next". Nielsen Norman Group, 2 February 2020. [nngroup.com/articles/information-scent](https://www.nngroup.com/articles/information-scent/)
- Card, Stuart K., Peter Pirolli, Mija Van Der Wege, Julie B. Morrison, Robert W. Reeder, Pamela K. Schraedley and Jenea Boshart. "Information Scent as a Driver of Web Behavior Graphs: Results of a Protocol Analysis Method for Web Usability". *CHI 2001*, ACM, 2001. [research.cs.vt.edu](https://research.cs.vt.edu/ns/cs5724papers/5.usageenvir.adaptation.card.infoscent.pdf)
- Chan, Megan. "Mental Models". Nielsen Norman Group, 26 January 2024. [nngroup.com/articles/mental-models](https://www.nngroup.com/articles/mental-models/)
- Cooper, Alan, Robert Reimann, David Cronin and Christopher Noessel. *About Face: The Essentials of Interaction Design*. 4th ed. Wiley, 2014. Ch. 1.
- Farrell, Susan. "Search-Log Analysis: The Most Overlooked Opportunity in Web UX Research". Nielsen Norman Group, 30 July 2017. [nngroup.com/articles/search-log-analysis](https://www.nngroup.com/articles/search-log-analysis/)
- Furnas, George W., Thomas K. Landauer, Louis M. Gomez and Susan T. Dumais. "The Vocabulary Problem in Human-System Communication". *Communications of the ACM* 30, no. 11 (1987): 964 to 971. [cacm.acm.org/research/the-vocabulary-problem-in-human-system-communication](https://cacm.acm.org/research/the-vocabulary-problem-in-human-system-communication)
- Harley, Aurora. "Icon Usability". Nielsen Norman Group, 27 July 2014. [nngroup.com/articles/icon-usability](https://www.nngroup.com/articles/icon-usability/)
- Katz, Michael A., and Michael D. Byrne. "Effects of Scent and Breadth on Use of Site-Specific Search on E-Commerce Web Sites". *ACM Transactions on Computer-Human Interaction* 10, no. 3 (2003): 198 to 220. [unpaywall.org/10.1145/937549.937551](https://unpaywall.org/10.1145%2F937549.937551)
- Krause, Rachel. "Maintain Consistency and Adhere to Standards (Usability Heuristic #4)". Nielsen Norman Group, 10 January 2021. [nngroup.com/articles/consistency-and-standards](https://www.nngroup.com/articles/consistency-and-standards/)
- Krug, Steve. *Don't Make Me Think, Revisited: A Common Sense Approach to Web Usability*. 3rd ed. New Riders, 2014. Chs 1, 2 and 4. Contents at [oreilly.com](https://oreilly.com/library/view/dont-make-me/9780133597271); ch. 4 excerpt at [peachpit.com](https://peachpit.com/articles/article.aspx?p=2170656) (practice).
- Lakoff, George. *Women, Fire, and Dangerous Things: What Categories Reveal about the Mind*. University of Chicago Press, 1987. [press.uchicago.edu](https://press.uchicago.edu/ucp/books/book/chicago/W/bo3632089.html)
- Larson, Kevin, and Mary Czerwinski. "Web Page Design: Implications of Memory, Structure and Scent for Information Retrieval". *CHI 98*, ACM, 1998, pp. 25 to 32. [microsoft.com/en-us/research](https://www.microsoft.com/en-us/research/publication/web-page-design-implications-memory-structure-scent-information-retrieval/)
- Laubheimer, Page. "The 3-Click Rule for Navigation Is False". Nielsen Norman Group, 11 August 2019. [nngroup.com/articles/3-click-rule](https://www.nngroup.com/articles/3-click-rule/)
- Laubheimer, Page. "3 Common IA Mistakes (that Are All Due to Low Information Scent)". Nielsen Norman Group, 16 April 2023. [nngroup.com/articles/3-ia-mistakes](https://www.nngroup.com/articles/3-ia-mistakes/)
- Laubheimer, Page. "Tree Testing: Evaluate Menu Labels and Categories". Nielsen Norman Group, 6 August 2023. [nngroup.com/articles/tree-testing](https://www.nngroup.com/articles/tree-testing/)
- Laubheimer, Page. "Menu-Design Checklist: 17 UX Guidelines". Nielsen Norman Group, 7 June 2024. [nngroup.com/articles/menu-design](https://www.nngroup.com/articles/menu-design/)
- Mausser, Kristina. "Site Search Analytics: A Conversation with Lou Rosenfeld". UXmatters, 18 July 2011. [uxmatters.com](https://uxmatters.com/mt/archives/2011/07/site-search-analytics-a-conversation-with-lou-rosenfeld.php) (interview; practice).
- McCloskey, Marieke. "Writing Hyperlinks: Salient, Descriptive, Start with Keyword". Nielsen Norman Group, 9 March 2014. [nngroup.com/articles/writing-links](https://www.nngroup.com/articles/writing-links/)
- Morville, Peter. "User Experience Design". Semantic Studios, 21 June 2004. [semanticstudios.com/user_experience_design](https://semanticstudios.com/user_experience_design/)
- Morville, Peter. *Ambient Findability*. O'Reilly, September 2005. Ch. 1, "Lost and Found". [oreilly.com](https://oreilly.com/library/view/ambient-findability/0596007655)
- Nielsen, Jakob. "Search and You May Find". Nielsen Norman Group, 14 July 1997. [nngroup.com/alertbox/9707b.html](https://www.nngroup.com/alertbox/9707b.html)
- Nielsen, Jakob. "Information Foraging: Why Google Makes People Leave Your Site Faster". Nielsen Norman Group, 29 June 2003. [nngroup.com/articles/information-foraging-leave-site](https://www.nngroup.com/articles/information-foraging-leave-site/)
- Nielsen, Jakob. "Use Old Words When Writing for Findability". Nielsen Norman Group, 27 August 2006. [nngroup.com/articles/web-writing-use-search-keywords](https://www.nngroup.com/articles/web-writing-use-search-keywords/)
- Nielsen, Jakob. "First 2 Words: A Signal for the Scanning Eye". Nielsen Norman Group, 6 April 2009. [nngroup.com/articles/first-2-words-a-signal-for-scanning](https://nngroup.com/articles/first-2-words-a-signal-for-scanning)
- Norman, Don. *The Design of Everyday Things*. Revised and expanded ed. Basic Books, 2013. Ch. 1, "Conceptual Models" and "The System Image". [jnd.org](https://jnd.org/the-design-of-everyday-things-revised-and-expanded/)
- Pirolli, Peter, and Stuart Card. "Information Foraging". *Psychological Review* 106, no. 4 (1999): 643 to 675. [doi.org/10.1037/0033-295X.106.4.643](https://doi.org/10.1037/0033-295X.106.4.643)
- Régeni, Anna. "Indi Young: Mental Models – review". Ergomania, 3 April 2018. [ergomania.eu/indi-young-mental-models-review](https://ergomania.eu/indi-young-mental-models-review/) (review; practice).
- Rosch, Eleanor, and Carolyn B. Mervis. "Family Resemblances: Studies in the Internal Structure of Categories". *Cognitive Psychology* 7, no. 4 (1975): 573 to 605. [courses.grainger.illinois.edu](https://courses.grainger.illinois.edu/cs440/fa2023/Quizzes/grad-readings/rosch-and-mervis.pdf)
- Rosch, Eleanor, Carolyn B. Mervis, Wayne D. Gray, David M. Johnson and Penny Boyes-Braem. "Basic Objects in Natural Categories". *Cognitive Psychology* 8 (1976): 382 to 439. [cns.nyu.edu](https://www.cns.nyu.edu/~msl/courses/2223/Readings/Rosch-CogPsych1976.pdf)
- Rosenfeld, Louis. *Search Analytics for Your Site: Conversations with Your Customers*. Rosenfeld Media, 2011. [rosenfeldmedia.com/books/search-analytics](https://rosenfeldmedia.com/books/search-analytics/)
- Rosenfeld, Louis, Peter Morville and Jorge Arango. *Information Architecture: For the Web and Beyond*. 4th ed. O'Reilly, 2015. Chs 3, 4, 6, 7, 9, 11. Contents at [oreilly.com](https://www.oreilly.com/library/view/information-architecture-4th/9781491913529/part02.html); ch. 7 at [oreilly.com](https://www.oreilly.com/library/view/information-architecture-4th/9781491913529/ch07.html).
- Spencer, Donna. "Four Modes of Seeking Information and How to Design for Them". Boxes and Arrows, 14 March 2006. [boxesandarrows.com](https://boxesandarrows.com/four-modes-of-seeking-information-and-how-to-design-for-them/) (practice).
- Spool, Jared M. "Are There Users Who Always Search?" UIE, 1 May 2001. [articles.centercentre.com/?p=15](https://articles.centercentre.com/?p=15) (practice).
- Tankala, Samhita. "Card Sorting: Pushing Users Beyond Terminology Matches". Nielsen Norman Group, 14 June 2024. [nngroup.com/articles/card-sorting-terminology-matches](https://www.nngroup.com/articles/card-sorting-terminology-matches/)
- Teevan, Jaime, Christine Alvarado, Mark S. Ackerman and David R. Karger. "The Perfect Search Engine Is Not Enough: A Study of Orienteering Behavior in Directed Search". *CHI 2004*, ACM, 2004. [microsoft.com/en-us/research](https://www.microsoft.com/en-us/research/publication/perfect-search-engine-not-enough-study-orienteering-behavior-directed-search/)
- W3C. *Understanding Success Criterion 2.4.4: Link Purpose (In Context)* (standard). [w3.org/WAI/WCAG21/Understanding/link-purpose-in-context](https://www.w3.org/WAI/WCAG21/Understanding/link-purpose-in-context)
- W3C. *Understanding Success Criterion 3.2.4: Consistent Identification* (standard). [w3.org/WAI/WCAG20/Understanding/consistent-identification](https://www.w3.org/WAI/WCAG20/Understanding/consistent-identification)
- Young, Indi. *Mental Models: Aligning Design Strategy with Human Behavior*. Rosenfeld Media, 2008. [rosenfeldmedia.com/books/mental-models](https://rosenfeldmedia.com/books/mental-models/)

## Unsure list

- Young 2008: the diagram's parts (tasks grouped into towers, towers into mental spaces, support aligned below the line, gaps) are from a review and from knowledge of the book; no chapter or page of the book was checked.
- Norman 2013, ch. 1: section headings "Conceptual Models" and "The System Image" checked on the author's contents page; the account of the three models is from knowledge of the chapter and a review of an earlier edition, not re-read.
- Rosenfeld, Morville and Arango 2015, ch. 6: only the four challenge headings were seen; the one-line gloss of each is this unit's, from knowledge of the chapter.
- Rosenfeld, Morville and Arango 2015, ch. 7, "General Guidelines": that the guidelines argue for consistency across a labelling system is from knowledge; only the heading was seen.
- Morville 2005, ch. 1: the three-part definition of findability is from knowledge of the book; a 2004 blog post quoting Morville gives its first part, "the quality of being locatable or navigable".
- Krug 2014, chs 1 and 2: the first law as the first chapter's title is checked from the contents; the scanning, satisficing and muddling-through argument of ch. 2 is from knowledge, not re-read in the 3rd ed.
- Katz and Byrne 2003: volume, issue and pages from a secondary reference list; the findings from the abstract only.
- Furnas and others 1987: the abstract was read; volume, issue and pages from knowledge.
- Bates 1989: volume and issue from the journal's issue listing; pages not checked, so omitted.
- Rosch and others 1976: the furniture, chair, kitchen chair example of the three levels is from knowledge of the paper; the abstract does not give it.
