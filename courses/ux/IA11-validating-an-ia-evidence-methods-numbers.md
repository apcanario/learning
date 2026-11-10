---
code: IA11
title: "Validating an IA: evidence, methods, numbers"
course: ux · IA · Information Architecture
model: Opus 5.5
written: 2026-11-10
search: off
---

# IA11 · Validating an IA: evidence, methods, numbers

IA5 to IA10 built and placed the IA of Perqo (Perqo, fictional), and IA6 to IA10 each ended with a table of assumptions with a column headed "Test (IA11)". This unit supplies those tests. It covers the methods that test an IA and what each one proves and leaves unproved: open, closed and hybrid card sorting, tree testing, first-click testing, search-log analysis, analytics path and funnel review, and task-based usability testing of a built navigation; the published evidence on how many participants each needs, with vendor guidance labelled as such; the metrics (success, directness, first click, time, agreement) and how to read them; how to run each method cheaply and remotely with no particular tool; how a result becomes an IA change, and when it is too weak to act on; and what to do when no user can be reached, which is IA12's ground. The worked examples are a pilot run on the Perqo app (Perqo, fictional). The deliverable is a validation plan for the Perqo app IA from IA6, the tree-test script and the closed card-sort protocol in full, and an analysis template for each method in the plan that needs one.

Every figure uses IA2's notation (IA2, section 5.2 and the notation sheet). This unit draws three of its six tones. Tone 3, the Perqo app and the employee, carries the pilot's results, since every participant is an employee and every task is in the app. Tone 5, shared, carries the methods and the confidence ladder, because a method serves any surface. Tone 6, a stop, marks the tree-test failures and the one pilot result whose interval lies wholly below its pass mark.

What the filed units hand on, and where this unit uses it:

| From | What it hands on | Used in |
|---|---|---|
| IA3, sections 1, 3.2, 5.2, 6.1; Deliverable; "What this hands on" | scent and the foraging threshold; Tankala's warning on card sorts; the search log as hypotheses; tree testing as the measure of findability; C3, B2, A1 to A3 and E2 left to tests | sections 2.1, 2.2, 2.4; Deliverable A, V-04, V-05, V-12, V-13 |
| IA3, section 6.2, and IA4, section 2.1; IA4, section 4.3; IA4, Deliverable B, R6 | breadth against depth; the object nouns "labelled assumed until a test (IA11)"; a second listing only on evidence | sections 2.2, 6.2; Deliverable A, V-05, V-14 |
| IA3, Deliverable (the as-is navigation) | the app as it stood before IA6, the "before" of a before-and-after test | Deliverable A, V-01, V-17; Deliverable B, B.6 |
| IA6, Deliverables A to C; "What IA8 and IA11 take" | the task inventory and frequencies; the app map A-0 to A-5, entries E-1 to E-8, states, wireflows; twelve assumptions with their tests | section 4; the whole Deliverable |
| IA9, section 6, RV-04 to RV-06, RV-11, W-09 and W-17 | production signals as hypotheses; the structure test before and after a change; the steps where tests run and where their inputs are handed on | sections 1.1, 6.1 and 7; Deliverable A |
| IA7, "What IA8 and later units take"; IA8, IA9 and IA10, "What later units take" | the tests named for IA11 on Admin, the system map, the process and the touchpoints; G-5; FO-06 and FO-07; TP-05 | sections 6.1 and 7; Deliverable A.2 |

## 1 · What a test can prove about an IA

### 1.1 · A claim, a question, a method

An IA built at a desk is a set of claims about people: that they will name a thing as the map does, look for it where the tree puts it, and choose the label that leads there. IA4 said this of its own map, "Its objects are labelled assumed until a test (IA11) confirms that people name and group them this way" (IA4, section 4.3), and IA6 to IA10 said it of every row in their assumption tables. A test answers one question about one part of the structure, and the method follows from the question. A team that starts from the method ("let's run a card sort") gets an answer to whichever question that method happens to answer.

Three kinds of question come up, and they need three kinds of method:

- **How do people group and name these things?** Asked before a structure exists, or when its categories are in doubt. The methods are generative: open and hybrid card sorts. Jakob Nielsen draws the line in one sentence: "Card sorting is a generative method", where a usability test evaluates a design that exists ("Card Sorting: How Many Users to Test", Nielsen Norman Group, 18 July 2004, [nngroup.com, card sort users](https://www.nngroup.com/articles/card-sorting-how-many-users-to-test/)).
- **Can people find things in this structure?** Asked of a structure that exists, drawn or built. The methods are evaluative: closed card sort, tree test, first-click test, usability test. Samhita Tankala separates the two structure methods by stage: card sorting is "typically conducted early in the design process", and a tree test "evaluates a hierarchical category structure" (Tankala, "Card Sorting vs. Tree Testing", NN/g, 23 February 2024, as cited in IA9, section 6.4).
- **What do people do with the built product?** Asked after release. The methods read records of use: search logs, analytics paths and funnels, support tickets. IA9 made these Perqo's production signals and gave them their status, after Rosenfeld: each record says what happened and never why, so each finding is a hypothesis for a test with people (IA9, section 6; IA3, section 5.2, after Mausser, UXmatters, 2011).

### 1.2 · The metrics, defined once

DD-IA2 will build a measurement model on these tests, and IA12 will cite a test for each assumption. Both need each metric to have one definition, used the same way in every test. The definitions below are this unit's; where a source defines the metric, the definition keeps the source's meaning and says so.

| ID | Metric | Definition | Read with | Source of the definition |
|---|---|---|---|---|
| M-01 | Success rate | participants who ended a task on a node, screen area or outcome the script marks correct, divided by participants who attempted it; a skip counts as a failure | a 95% adjusted-Wald interval (section 3.4) | Laubheimer, NN/g, 2024: "The percentage of users who found the right category (or categories) for that task" |
| M-02 | Directness | participants who succeeded without going back up the tree, divided by participants who attempted the task | the same interval | Laubheimer 2024: "The percentage of users who went to the right category immediately" |
| M-03 | First-click correctness | participants whose first choice lies on a path to a correct answer, divided by participants who attempted the task | the same interval | Laubheimer 2024 ("first click"); Bailey and others 2009 |
| M-04 | Time on task | the median time in seconds from the task's start to its answer, for successful attempts; the median for all attempts reported beside it | read only beside M-01; never alone | Laubheimer 2024 defines time as the average; this unit uses the median, because a few slow attempts move a mean (this unit's choice) |
| M-05 | Placement share | in a closed sort, participants who placed a card in a category, divided by participants who sorted the card | the same interval | this unit's definition; Sauro, MeasuringU, 2012, plans precision on "the percent of users who place cards in each category" |
| M-06 | Pair similarity | in any sort, participants who placed two cards in the same group, divided by participants who sorted both; a card left in "Not sure" is in no group | read as a matrix, never one cell at a time | this unit's definition; the similarity matrix as in Katsanos and others 2019 and Lantz and others 2019 |
| M-07 | Zero-result rate | searches returning no result, divided by all searches, in one period; per query, the count of searches returning no result | compared period with period | after Farrell, NN/g, 2017 (IA3, section 5.2) |
| M-08 | Task frequency | starts of a task (its first screen view, mapped from screen identifier to task) per active employee per month | compared with the assumed frequency | this unit's definition, on IA9's screen-view records (IA9, section 6.3) |
| M-09 | Short-visit share | sessions with one or two task starts whose first screen is Home (A-1) or a notification's landing (E-4, E-8), divided by all sessions | the same interval | this unit's definition of IA6's assumption (IA6, section 3.2) |
| M-10 | Opt-in share | employees who answer Allow at the notifications prompt, divided by employees shown it | the interval of a difference when two timings are compared | this unit's definition |
| M-11 | Problem frequency | participants in a usability round who showed a given problem, divided by participants in the round | read as a count, with section 6.1's rule | after Nielsen and Landauer's per-participant proportion (Nielsen, NN/g, 2000) |

## 2 · The methods, and what each does and does not prove

### 2.1 · Card sorting: open, closed and hybrid

In a card sort, participants put cards, each naming one item of content, into groups. Jeff Sauro's definitions of the two classic forms: in an open sort "Users are asked to sort items into a group and make up their own groups and give the groups a name"; in a closed sort "Users sort items into previously defined category names" ("10 Things to Know about Card Sorting", MeasuringU, 3 April 2012, [measuringu.com, card sorting](https://measuringu.com/card-sorting/); practice, a consultancy's article). A hybrid sort sits between them: in one research tool's documentation, "Researchers provide starting categories, but participants can add their own" (dscout, "Card sort questions", help centre, undated, [help.dscout.com, card sort](https://help.dscout.com/study-basics/question-types/card-sort-questions); vendor documentation, cited only for the definition; the same page calls the closed sort "Best for validating an existing categorical structure").

Donna Spencer's *Card Sorting: Designing Usable Categories* (Rosenfeld Media, 2009) is the book-length treatment; its chapters run from choosing the method (ch. 4) and the people (ch. 6) through making the cards and managing the sort (chs 7 and 8) to exploratory and statistical analysis (chs 9 and 10) ([rosenfeldmedia.com, Card Sorting](https://rosenfeldmedia.com/?p=187469), contents). Its text was not read for this unit. A review in *User Experience* magazine reports that it explains open and closed sorting and when to use each, prefers physical cards to software, starts its analysis with entering the data in a spreadsheet, covers cluster analysis and multidimensional scaling, and warns that statistical analysis "can produce such nice outputs that it is easy to get drawn into a simple answer" (Gerry Gaffney, "Deal Them Again: Card Sorting Revisited", *User Experience* 8, no. 3, 2009, [oldmagazine.uxpa.org, review](https://oldmagazine.uxpa.org/?p=5384); a book review, practice).

What each form proves, and what it does not:

- **An open sort** shows how a group of people clusters the content and what they call the clusters. It does not show that a structure built from those clusters can be navigated: the participants never navigated anything. Its result is the input to a structure, and the structure then needs an evaluative test.
- **A closed sort** shows whether people put each item where an existing scheme puts it, and how many put it somewhere else. It measures agreement with a scheme the team chose, so it cannot show a better scheme the team did not offer.
- **A hybrid sort** shows the same as a closed sort, plus the groups people add when the given ones do not fit. Those added groups are the gaps in the scheme; they are not yet a tested part of it.
- **Every sort can measure the wording.** IA3 recorded Tankala's warning: participants "sometimes tend to group cards with similar keywords rather than conceptually organize them carefully" (Tankala, "Card Sorting: Pushing Users Beyond Terminology Matches", NN/g, 14 June 2024; IA3, section 3.2). A card that shares a word with a category name is placed by the word. The protocol in Deliverable C rewrites the one Perqo card that would (C.2).

### 2.2 · Tree testing

Page Laubheimer defines the tree test as "An evaluation of a hierarchical category structure, or tree, by having users find the locations in the tree where specific resources or features can be found"; the menu participants see is "completely devoid of visual styling and content", and the test "focuses exclusively on evaluating the findability of key resources in your category structure" ("Tree Testing: Evaluate Menu Labels and Categories", Nielsen Norman Group, 6 August 2023, [nngroup.com, tree testing](https://nngroup.com/articles/tree-testing/)). IA3 took this definition as the way findability is measured (IA3, section 6.1).

The method began on paper. A Boxes and Arrows article describes it with index cards: the top three or four levels of a classification copied onto cards, one card per level of labels; around 15 information-seeking tasks, one per card; ten to fifteen 30-minute one-on-one sessions; the participant shown the top card and asked where they would go, with no word on whether an answer is right; the last selection recorded for each task ("Measuring the Success of a Classification System", Iain Barker, Boxes and Arrows, 24 April 2007, [boxesandarrows.com, classification](https://boxesandarrows.com/measuring-the-success-of-a-classification-system/); practice). The author calls the numbers "indicative", useful for judgement and not statistically valid, and makes a point every later source repeats in other words: for a new structure, which location counts as correct is the evaluator's decision (the same article).

What a tree test proves: whether the labels and the grouping of a hierarchy lead people to an item, measured as success, directness and first click (section 1.2), and at which level a path goes wrong. That last matters because of the breadth-and-depth evidence: deeper structures slowed people in every study IA4 reviewed, and each added level is one more choice that must carry scent (Zaphiris 2000 and Larson and Czerwinski 1998, through IA4, section 2.1; IA3, section 6.2). A tree test shows the level at which the scent ran out, which neither a sort nor a log can. What it does not prove: anything the screen adds. No visual design, no content on the page, no search, and no scent from what surrounds a label, which IA3 showed a person reads together with the label itself (Budiu, NN/g, 2020; IA3, section 1.2). A label that fails in a tree test may pass on a screen where its neighbours explain it, and the reverse.

### 2.3 · First-click testing

A first-click test shows a participant a screen (a wireframe, a design or the built product) and a task, and records where they tap or click first. Robert Bailey, Cari Wolfson, Janice Nall and Sanjay Koyani report its rationale from tests across several websites: "if the user's first click was correct, the chances of getting the overall scenario correct was .87"; "if the first click was incorrect, the chance of eventually getting the scenario correct was only .46"; the ratio of the two averaged 1.9, with a range from 1.4 to 2.7 ("Performance-Based Usability Testing: Metrics That Have the Greatest Impact for Improving a System's Usability", in M. Kurosu, ed., *Human Centered Design, HCII 2009*, LNCS 5619, Springer, 2009, pp. 3 to 12, [link.springer.com, Bailey 2009](https://link.springer.com/content/pdf/10.1007/978-3-642-02806-9_1.pdf)). The paper does not give the number of participants or studies behind the figures, which limits what can be drawn from them. They also report that first-click scenarios are cheap: "over 100 FirstClick scenarios" fitted in the time a traditional one-hour test gives to 10 to 15 (Bailey and others 2009). Laubheimer gives the same reason for reading first clicks in a tree test: "The first click is critical because it often predicts whether a user will be successful in finding the right item" ("Tree Testing Part 2: Interpreting the Results", Nielsen Norman Group, 19 January 2024, [nngroup.com, tree test results](https://nngroup.com/articles/interpreting-tree-test-results/)).

What it proves: where people start on a real layout, with its scent from position, grouping and neighbouring words. What it does not: that the task is completed. The .87 is a likelihood across many scenarios, and one task's first click says nothing certain about the rest of its path.

### 2.4 · Search-log analysis

Louis Rosenfeld's *Search Analytics for Your Site: Conversations with Your Customers* (Rosenfeld Media, 2011) is the standard work; its analysis chapters are pattern analysis (ch. 3), failure analysis (ch. 4), session analysis (ch. 5), audience analysis (ch. 6) and goal-based analysis (ch. 7), followed by chapters on improving search, navigation and metadata, and content (chs 8 to 10) ([rosenfeldmedia.com, Search Analytics](https://rosenfeldmedia.com/books/search-analytics), contents; the chapters' text was not read). The publisher's page states the premise: "Search queries are gold: they are real data that show us exactly what users are searching for in their own words." IA3 set out what a log shows, after Farrell: zero-result queries, frequent queries for things the site holds (a structure that hides them), frequent queries for things it lacks (a content gap), and reformulations in one session (a failed search); and her advice to read several months so that a campaign's spike is not taken for a pattern (Farrell, NN/g, 2017; IA3, section 5.2).

What it proves: what people who searched asked for, in their words, and which searches failed. What it does not: why they searched, what the people who did not search did, or whether a fix worked for anyone who no longer needs to search. At Perqo the log is the Help centre's, on perqo.com; the app has no search (IA6, B.2, E1), so the log shows the app's failures only when employees leave the app to look for help (IA3, section 5.1).

### 2.5 · Analytics paths and funnels

Product analytics record what people did, at the scale of everyone who used the product. Jen Cardello names three uses: issue indication, investigation and triangulation (Cardello, NN/g, 2013; IA9, section 6.3). For an IA, two shapes in the records matter. A **path** is the sequence of screens in a session: a loop between two screens, a detour through Help, an exit just after a label. A **funnel** is the share of people who reach each step of a fixed sequence, such as New claim, Check and submit, Claim submitted (A-3.1 to A-3.3), and the step where most leave. Perqo's analytics record each app screen view by screen identifier (Perqo, fictional; IA9, section 6.3), so a path can be read in the app map's own terms.

What it proves: frequencies, paths and drop-offs, measured on everyone, with no recruiting. What it does not: intent. A session that opens Notifications twice may be a person who could not find a message or one who read it twice. And a funnel's drop-off at Check and submit may be the over-balance state doing its job (IA6, section 4.3). Records also carry confounds a test controls: a release, a campaign, a new client's onboarding.

### 2.6 · Task-based usability testing of a built navigation

A usability test gives a participant realistic tasks on the product, or a working prototype of it, and observes where they succeed, where they hesitate and what they say. Nielsen's case for small rounds rests on a model he built with Thomas Landauer: one participant finds a share L of the problems, "31%, averaged across a large number of projects we studied", so five participants find about 85% of them, and three rounds of five, each after fixing what the last found, beat "a single monster study with 15 users" ("Why You Only Need to Test with 5 Users", Nielsen Norman Group, 18 March 2000, [nngroup.com, 5 users](https://nngroup.com/articles/why-you-only-need-to-test-with-5-users/), reporting Nielsen and Landauer 1993, not seen). He adds the conditions: several highly distinct groups of users need their own participants, and quantitative studies need more (Nielsen 2000). Steve Krug's version for teams with no research budget: "Testing one user early in the project is better than testing 50 near the end", and "Testing one user is 100 percent better than testing none" (*Don't Make Me Think, Revisited*, 3rd ed., New Riders, 2014, excerpt at [peachpit.com, Krug](https://www.peachpit.com/articles/article.aspx?p=2209313); practice).

What it proves: whether real tasks succeed on the whole system (labels, screens, content and rules together) and why they fail, from what people do and say. What it does not prove at five participants is a rate. Five people find problems; they do not measure how often a problem occurs (section 3.3).

### 2.7 · Choosing the method by the question

Figure 1 puts the eight methods side by side. Its rows are the methods of sections 2.1 to 2.6, its cells short forms of what those sections say, the participant numbers section 3's and the cheapest forms section 5's. Every row is tone 5, since a method serves any surface.

```viz
{"kind": "matrix", "caption": "Method selection: eight methods that test an IA, against the question each answers, what it proves, what it does not, the participants it needs and its cheapest form; supports the choice of method for each assumption in the validation plan (section 2.7; Deliverable A). Card sorts from Nielsen, NN/g, 2004, Sauro, MeasuringU, 2012 (practice), dscout's documentation (vendor, for the hybrid sort) and Tankala, NN/g, 2024 (through IA3); tree test from Laubheimer, NN/g, 2023 and 2024, and Boxes and Arrows (practice); first click from Bailey and others, HCII 2009; search logs from Rosenfeld 2011 and Farrell, NN/g, 2017 (through IA3); analytics from Cardello, NN/g, 2013 (through IA9); usability testing from Nielsen, NN/g, 2000, and Krug 2014; participant numbers from section 3; cheapest forms from section 5. Every row tone 5, shared: a method serves any surface. The closed sort's 50 is the Perqo plan's (section 3.1); Perqo is fictional.", "cols": ["Answers", "Proves", "Does not prove", "Participants", "Cheapest form"], "rows": [
 {"label": "Open sort", "tone": 5, "cells": ["how people group and name the content", "the groups and names a population makes", "that a structure built on them is findable", "15 to 30", "paper cards and a spreadsheet"]},
 {"label": "Closed sort", "tone": 5, "cells": ["which given category people put each item in", "agreement with an existing scheme", "a better scheme nobody offered", "50 in the Perqo plan; about 193 for a 7% margin", "a form with one choice per card"]},
 {"label": "Hybrid sort", "tone": 5, "cells": ["whether a given scheme has gaps", "the groups people add to it", "that the added groups are findable", "as an open sort", "a form with a free-text 'another group' choice"]},
 {"label": "Tree test", "tone": 5, "cells": ["can people find items in this hierarchy", "findability of labels and grouping", "visual design, content, search", "50 or more per tree", "index cards, moderated"]},
 {"label": "First click", "tone": 5, "cells": ["is the first move on this screen right", "where people start on a real layout", "that the task is completed", "as a tree test", "a screen image on a video call"]},
 {"label": "Search logs", "tone": 5, "cells": ["what people ask for, in their words", "demand and failed searches", "why, or what non-searchers did", "none: the log", "an exported log and a spreadsheet"]},
 {"label": "Analytics", "tone": 5, "cells": ["what people did in production", "frequencies, paths and drop-offs at scale", "intent", "none: the records", "screen views by identifier"]},
 {"label": "Usability test", "tone": 5, "cells": ["can people do real tasks on the built thing, and why not", "problems and their causes", "a stable rate at five", "5 per round, several rounds", "a video call and a prototype"]}],
 "legend": [{"mark": "tone 5", "means": "shared: a method serves any surface", "tone": 5}]}
```

The rule for choosing, from sections 1.1 and 2.1 to 2.6: name the question first; if no structure exists, sort; if one exists, test it (tree test for the hierarchy, first click for a screen, usability test for the whole task); if the product is live, read the records for the hypotheses and test those with people. IA9 set the order for production signals in the same direction: a signal about a structure that exists goes to a test of that structure, and to a card sort only when the test shows the categories themselves are wrong (IA9, section 6.4).

## 3 · Sample sizes and reliability

### 3.1 · Card sorts: the published studies

Three studies measure how many participants a card sort needs, and all three measure the same thing: how stable the similarity matrix is (M-06), the table of how often each pair of cards was grouped together.

- **Tullis and Wood (2004).** Nielsen reports their study at Fidelity Investments: 168 participants sorted the same cards, and smaller samples were drawn at random from the whole set and compared with it. The correlations with the full result were 0.75 at 5 participants, 0.90 at 15, 0.95 at 30 and 0.98 at 60; "Tullis and Wood recommend testing 20–30 users for card sorting." Nielsen's own advice is 15, with about 30 for large, well-funded projects: "I think that correlations of 0.90 (for 15 users) or maybe 0.93 (for 20) are good enough for most practical purposes" (Nielsen 2004; the paper, "How Many Users Are Enough for a Card-Sorting Study?", presented at the UPA conference in 2004, was not seen). Sauro gives the same study's result as correlations "above .93" at 20 to 30 (Sauro 2012).
- **Lantz and others (2019).** Ethan Lantz and colleagues compared card-sort data with pairwise similarity judgements of the same stimuli, treated as the gold standard, and found that "approximately 10–15 participants provided optimal estimation of the similarity matrix", with little gained beyond that (Ethan Lantz, Jared W. Keeley, Michael C. Roberts, Maria Elena Medina-Mora, Pratap Sharan and Geoffrey M. Reed, "Card Sorting Data Collection Methodology: How Many Participants Is Most Efficient?", *Journal of Classification* 36, no. 3, 2019, pp. 649 to 658, abstract, [ideas.repec.org, Lantz 2019](https://ideas.repec.org/a/spr/jclass/v36y2019i3d10.1007_s00357-018-9292-8.html)).
- **Katsanos and others (2019).** Christos Katsanos and colleagues ran six open sorts with 140 participants, three on a travel website's content and three on an online shop's, each study with 16 to 34 participants, and compared the studies with each other. The similarity matrices correlated strongly (Mantel r from 0.609 to 0.930, all p < 0.001), and the navigation schemes cut from them agreed on 63.2% to 92.7% of items; they conclude that this "justifies why a practitioner may only run one study instead of multiple", for participants of similar profile (their participants were technology-savvy students and practitioners) ("Cross-study Reliability of the Open Card Sorting Method", *CHI '19 Extended Abstracts*, ACM, 2019; preprint at [arxiv.org, 1903.08644](https://arxiv.org/pdf/1903.08644)).

What the three support: 15 to 30 participants give a similarity matrix, and the groups read from it, that a second study of similar people would largely reproduce. None of the three studied a hybrid sort; its added groups are read as an open sort's are, so this unit gives it the open sort's numbers (this unit's reasoning, unsourced). What they do not support is a precise share for one card in one category, which is what a closed sort's decision turns on (M-05). That is a proportion, and its precision depends on the sample in the way every proportion's does (section 3.4). Sauro makes the point with a number: "to have a margin of error of around 7% you should plan on having around 193 participants" (Sauro 2012). A closed sort run to decide placements therefore needs the sample of a quantitative test, and the Perqo plan gives CS-1 50 participants, the tree test's sample, so both run in one session (Deliverable A).

### 3.2 · Tree tests: guidance, and no study

This unit found no peer-reviewed study of how many participants a tree test needs. The numbers in use are guidance:

- **NN/g:** "Typically, 50+ participants per tree are needed for a quantitative study to achieve reasonably narrow confidence intervals" (Laubheimer 2024), said of studies comparing trees; for qualitative tree testing, Laubheimer writes that it "requires only a few participants" (Laubheimer 2023).
- **A practitioner's guide:** Dave O'Brien's *Tree Testing for Websites* advises "Aim for about 50 participants per user group": at 30 patterns start to show but small effects cannot be told from outliers, at 50 to 100 they become clear, and beyond that returns diminish; when each participant does only some of the tasks, the sample grows by the ratio, so 20 tasks at 10 per participant need about 100 participants for 50 answers a task (O'Brien, "How many participants?", *Tree Testing for Websites*, ch. 9, last updated 27 August 2024, [treetesting.atlassian.net, participants](https://treetesting.atlassian.net/wiki/spaces/TTFW/pages/1310747/How+many+participants); practice).
- **The paper method:** ten to fifteen sessions, read as indicative (Boxes and Arrows, practice).

Fifty participants per tree, per user group, is therefore a convention of guidance and practice, and section 3.4 shows what it buys: an interval about 22 points wide around a success rate of 80%.

### 3.3 · First clicks and usability tests

No study this unit found sets a sample for a first-click test; its result is a proportion (M-03), so the reasoning of sections 3.2 and 3.4 applies, and the Perqo plan gives it the tree test's 50. For usability tests, Nielsen's five per round is for finding problems; for quantitative studies that measure usability metrics, his follow-up articles put the number at 20 (Nielsen 2000, as the article itself points to them). Five is the right number for one question, which problems exist and why, and the wrong one for another, how often a task succeeds.

### 3.4 · What a number is worth: the interval

James Lewis and Jeff Sauro's advice to practitioners: "Always compute a confidence interval, as it is more informative than a point estimate"; for completion rates they recommend a 95% adjusted-Wald interval for most usability work, and an adjustment whenever the sample is under 20 ("When 100% Really Isn't 100%: Improving the Accuracy of Small-Sample Estimates of Completion Rates", *Journal of Usability Studies* 1, no. 3, May 2006, pp. 136 to 150, [uxpajournal.org, Lewis and Sauro 2006](https://uxpajournal.org/wp-content/uploads/sites/7/pdf/JUS_Lewis_May2006.pdf)). Their book carries the method through confidence intervals (ch. 3), comparison with a goal (ch. 4) and sample sizes (chs 6 and 7) (Sauro and Lewis, *Quantifying the User Experience: Practical Statistics for User Research*, 2nd ed., Morgan Kaufmann, 2016, contents at [schweitzer-online.de, Sauro and Lewis](https://www.schweitzer-online.de/en/buch/Sauro/Quantifying-User-Experience/9780128023082/A35053706/); the chapters' text was not read).

The adjusted-Wald interval, as computed in this unit: with x successes out of n and z = 1.96 for 95%, add z²/2 (about 2) to the successes and z² (about 4) to the attempts, take p = (x + 1.92) / (n + 3.84), and the interval is p ± 1.96 × √(p(1 − p) / (n + 3.84)), cut at 0% and 100%. Every interval in this unit and its templates is computed this way. Lewis and Sauro put 1.645 in place of 1.96 when x = 0 or x = n, where one side of the interval is fixed, for the Wilson point estimate at the interval's centre; this unit keeps 1.96 for every interval's ends, the more cautious choice for a perfect score. The same observed rate of 80% gives these intervals at five sample sizes:

| Successes | Observed | 95% adjusted-Wald interval | Width |
|---|---|---|---|
| 4 of 5 | 80% | 36.0% to 98.0% | 62 points |
| 8 of 10 | 80% | 47.9% to 95.4% | 47.5 points |
| 16 of 20 | 80% | 57.8% to 92.5% | 34.7 points |
| 40 of 50 | 80% | 66.8% to 88.9% | 22.1 points |
| 80 of 100 | 80% | 71.0% to 86.7% | 15.7 points |

The interval measures one error only: the chance that a random sample of this size misses the true rate. It cannot measure a sample drawn from the wrong people, a task worded to give the answer away, or a tree that differs from the product. Those are section 6.3's reasons a result is too weak, and no sample size fixes them.

## 4 · Reading the numbers, on the Perqo pilot

### 4.1 · The pilot

Before the planned run, Perqo piloted the tree-test script (TT-1) and the closed card-sort protocol (CS-1) with 12 employees of the example client (Perqo, fictional), recruited through the client's HR team, in remote one-to-one sessions of 30 minutes over a video call, the tree test first, then the sort. A moderator read the instructions, watched, and asked after each task what the participant had expected to find. The pilot's purpose was the script: whether the tasks read as intended, which answers count as correct, and how long a session takes. Its numbers are read here as the worked example of reading, with the rule of section 6.3 that a pilot's numbers do not change the IA. The median times were 9 minutes for TT-1 and 6 minutes for CS-1 (Perqo, fictional).

The pilot changed the script in one place. On T2 (a turned-down receipt), two participants chose Recent activity on Home and explained that a claim from last week would show there with its status, which the app map confirms: Recent activity lists recent claims, each opening its Claim screen (IA6, Deliverable B, B.3). Recent activity (TN-04) was added to T2's correct nodes. Which locations count as correct is the evaluator's decision for a new structure (Boxes and Arrows, practice), and a decision made after seeing data can flatter a result; so the change is recorded in the script with its reason, and T2's pilot success is reported both ways: 11 of 12 with TN-04, 9 of 12 without it (Perqo, fictional; this unit's rule).

### 4.2 · Success, directness, first click and time

Figure 2 draws the pilot's tree-test result: for each task of TT-1 (Deliverable B, B.3), the participants who succeeded in tone 3 and those who failed in tone 6, counts of 12. The task names are the short names in the script.

```viz
{"kind": "bars", "mode": "stacked", "caption": "Tree-test result: the Perqo TT-1 pilot, 12 employees of the example client, success and failure per task as counts of 12; supports reading a tree test's result and the decision on which tasks the planned run must settle (section 4.2; Deliverable D, TT-A). Success and failure as defined by M-01 (section 1.2, after Laubheimer, 'Tree Testing Part 2', NN/g, 2024); T2 counts Recent activity as correct, added after the pilot (section 4.1). Tone 3 the employee and the app, for successes; tone 6 a stop, for failures. A pilot from one client: no bar here decides an IA change (section 6.3). Perqo and its pilot are fictional.", "max": 12, "series": [{"name": "Success", "tone": 3}, {"name": "Failure", "tone": 6}], "rows": [
 {"label": "T1 Train pass balance", "values": [12, 0]},
 {"label": "T2 Turned-down receipt", "values": [11, 1]},
 {"label": "T3 Yoga class", "values": [12, 0]},
 {"label": "T4 Cookery course", "values": [11, 1]},
 {"label": "T5 Bike helmet", "values": [10, 2]},
 {"label": "T6 Restaurant deals", "values": [9, 3]},
 {"label": "T7 Past message", "values": [4, 8]},
 {"label": "T8 Approval rule", "values": [10, 2]},
 {"label": "T9 Lost card", "values": [11, 1]},
 {"label": "T10 How balances work", "values": [9, 3]}]}
```

Four readings, each with the source that licenses it:

- **Success with directness.** T6 (Restaurant deals) had 9 successes and 7 direct ones: two participants found the deals only after backing out of a wrong branch. Laubheimer's example of the gap: "Even though 74% of users eventually found the right answer, only 50% took a direct path" (Laubheimer 2024). A task with high success and low directness has labels that people find in the end and doubt on the way; in an app opened a few times a month (IA3, section 6.2), every doubtful tap is one the foraging threshold says some people will not spend (IA3, section 1.1).
- **First click.** T7 (Past message: "Last week the app told you a payment at a shop had not gone through") had 4 successes, and 8 of 12 first clicks went to Card: six participants ended on Purchases and two on Card details. Laubheimer's diagnosis: when success is low but first clicks are right, the subcategory labels need to be more distinct; when first clicks are spread across several areas, the item may belong in more than one place, and when that happens on many tasks the scheme itself is in question (Laubheimer 2024). The Boxes and Arrows article reads first clicks the same way: poor first-click success points to the top-level labels, good first clicks with poor final success to the second level. T7's first clicks are concentrated, all on one wrong tab, which points at the top level: employees look for a message about a payment where payments are.
- **Which correct node.** On the far-member tasks the correct nodes include the cross-listing, so the result says where people looked first. T4 (Cookery course): 7 chose Learning, the home category, and 4 chose Meals, where the cross-listing sits. That split is the evidence R6 asks for before a second listing is kept (IA4, Deliverable B, R6), and section 4.4 reads it against the rule.
- **Time.** The median times of successful attempts ran from 7 seconds (T9, Lost card) to 21 seconds (T7). Time is read only beside success: T7's 21 seconds belong to four people who found the message after looking elsewhere. Bailey and his colleagues found a correlation of .82 between page views and the time taken to complete a scenario (Bailey and others 2009), so a slow task is usually a wandering one, which directness already shows. Laubheimer recommends t-tests for comparing times between trees (Laubheimer 2024); with 12 participants this unit compares none.

The full table, with directness, first clicks, correct nodes chosen and times, is the filled template in Deliverable D, TT-A.

### 4.3 · Agreement: placement and similarity

CS-1 asked each participant to place 12 cards, one for each item of the example client's policy, in Health, Learning, Mobility, Meals or Not sure (Deliverable C). Figure 3 draws the placement shares (M-05) as a numeric matrix: one row per card in the card's own words, one column per category, each cell the share of the 12 participants who put the card there, shaded in tone 3, the employee. "Dinner at a restaurant" is the card for the catalogue item restaurant meal, reworded so that it shares no word with Meals (section 2.1; Deliverable C, C.2).

```viz
{"kind": "matrix", "numeric": true, "tone": 3, "unit": "%", "min": 0, "max": 100, "decimals": 0, "scale_label": "share of the 12 participants", "caption": "Card-sort result, placement: the Perqo CS-1 pilot, a closed sort by 12 employees of the example client, each cell the share who placed the card in the category (M-05); supports reading a closed sort and the decision on which cross-listings the planned run must settle (section 4.3; Deliverable D, CS-A). Cards are the example client's twelve covered items, BI-001 to BI-012 (IA4, Deliverable B, B.3; IA6, B.3), in the card wording of Deliverable C, C.2; categories from IA2, section 5.3. Shaded in tone 3, the employee. A pilot from one client: no cell here decides an IA change (section 6.3). Perqo and its pilot are fictional.", "cols": ["Health", "Learning", "Mobility", "Meals", "Not sure"], "rows": [
 {"label": "Gym membership", "cells": [100, 0, 0, 0, 0]},
 {"label": "Yoga class", "cells": [75, 25, 0, 0, 0]},
 {"label": "Therapy session", "cells": [92, 0, 0, 0, 8]},
 {"label": "Swimming pool entry", "cells": [100, 0, 0, 0, 0]},
 {"label": "Coding course", "cells": [0, 100, 0, 0, 0]},
 {"label": "Cookery course", "cells": [0, 58, 0, 42, 0]},
 {"label": "Book", "cells": [0, 100, 0, 0, 0]},
 {"label": "Train pass", "cells": [0, 0, 100, 0, 0]},
 {"label": "Bike helmet", "cells": [17, 0, 75, 0, 8]},
 {"label": "Bike repair", "cells": [0, 0, 100, 0, 0]},
 {"label": "Dinner at a restaurant", "cells": [0, 0, 0, 100, 0]},
 {"label": "Groceries", "cells": [0, 0, 0, 100, 0]}]}
```

The placements in counts of 12 (Perqo, fictional): eight cards were placed in their home category by everyone; therapy session by 11, with one in Not sure; yoga class by 9 in Health and 3 in Learning; cookery course by 7 in Learning and 5 in Meals; bike helmet by 9 in Mobility, 2 in Health and 1 in Not sure. The three far members IA3 named, and only those, were placed in a second category (IA3, section 3.3), each towards the second place IA3 assumed.

The similarity matrix (M-06) reads the same sort without the category names: for each pair of cards, the share of participants who put both in one group. Figure 4 draws it for the six items of IA3, section 3.3, shaded in tone 3; a card with itself is left blank, and a card in Not sure is in no group, which is why bike helmet's cells against gym membership and train pass do not add to 100. The other cells follow from who placed what (Perqo, fictional): the 3 who placed yoga class in Learning put it with coding course (25%), and 2 of them had also placed cookery course in Learning (17%); the 2 who placed bike helmet in Health put it with gym membership (17%), and both had yoga class in Health too (17%).

```viz
{"kind": "matrix", "numeric": true, "tone": 3, "unit": "%", "min": 0, "max": 100, "decimals": 0, "scale_label": "share of the 12 participants", "caption": "Card-sort result, similarity matrix: the Perqo CS-1 pilot, 12 employees, each cell the share who placed both cards in one category (M-06), for the six items of IA3, section 3.3; a card with itself is blank; a card in Not sure is in no group. Supports reading a sort's clusters apart from the category labels (section 4.3; Deliverable D, CS-A). Similarity matrix as used by Katsanos and others, CHI '19 Extended Abstracts, and Lantz and others, Journal of Classification, 2019. Shaded in tone 3, the employee. A pilot from one client: no cell decides an IA change (section 6.3). Perqo and its pilot are fictional.", "cols": ["Gym membership", "Yoga class", "Coding course", "Cookery course", "Train pass", "Bike helmet"], "rows": [
 {"label": "Gym membership", "cells": [null, 75, 0, 0, 0, 17]},
 {"label": "Yoga class", "cells": [75, null, 25, 17, 0, 17]},
 {"label": "Coding course", "cells": [0, 25, null, 58, 0, 0]},
 {"label": "Cookery course", "cells": [0, 17, 58, null, 0, 0]},
 {"label": "Train pass", "cells": [0, 0, 0, 0, null, 75]},
 {"label": "Bike helmet", "cells": [17, 17, 0, 0, 75, null]}]}
```

Read as clusters, the matrix shows two firm pairs (gym membership with yoga class at 75%, train pass with bike helmet at 75%) and one loose one (coding course with cookery course at 58%): the cookery course is the item least tied to its home. Two cautions govern any reading of such a matrix. Its cells are not independent of each other, which is why Katsanos and his colleagues compared matrices with Mantel tests (Katsanos and others 2019); and a dendrogram drawn from it is a picture of one clustering method's choices, which Sauro calls subjective "especially when there isn't high agreement between users" (Sauro 2012). Spencer's warning about outputs too neat to doubt (Gaffney 2009) applies to the picture more than to the table.

### 4.4 · Pass, fail or undecided

A result decides something only against a mark set before the test. The Perqo plan sets them (Perqo, fictional; this unit's rule, Deliverable A): a task's success rate passes when the lower end of its 95% interval is at or above the mark, fails when the upper end is below it, and is undecided otherwise. The mark follows IA6's priority: 80% for a P1 task, 70% for a P2 or P3 task (IA6, Deliverable A, A.1). A cross-listing is kept when the lower end of the share looking in the second category is at or above 15%, removed when the upper end is below 15%, and undecided otherwise. A home placement is confirmed when the lower end of the home share is at or above 50%. For scale, Sauro's practice data put the average completion rate of usability tasks at 78%, across 1,189 tasks from 115 tests with 3,472 users, with a top quartile above 92% and a bottom quartile below 49% ("What Is A Good Task-Completion Rate?", MeasuringU, 21 March 2011, [measuringu.com, task completion](https://measuringu.com/task-completion/); practice, a consultancy's data); those were tasks on full interfaces, and a tree test strips the screen's help away (section 2.2).

At 50 participants the rule needs these counts (computed from section 3.4's formula): a 70% mark passes at 42 or more successes and fails at 28 or fewer; an 80% mark passes at 46 or more and fails at 34 or fewer; a cross-listing is kept at 13 or more and removed at 2 or fewer; a home placement is confirmed at 32 or more. Everything between is undecided. The band is wide, and it is the honest width of 50 answers.

Figure 5 draws six intervals from the pilot and one for comparison. The rows are named by the result each gives: three tree-test successes (T1, 12 of 12; T2, 11 of 12; T7, 4 of 12), the cookery course's share in Meals from the sort (5 of 12) and from the tree (4 of 12), the yoga class's share in Learning from the tree (3 of 12), and 40 of 50, any task at 80%. Rows are tone 3; T7's row is tone 6, because its interval lies wholly below its mark.

```viz
{"kind": "range", "unit": "%", "min": 0, "max": 100, "ticks": [0, 15, 50, 70, 80, 100], "decimals": 1, "caption": "Confidence intervals: 95% adjusted-Wald intervals for six Perqo pilot results and one comparison, each with its observed share as the point, except T1, whose observed 100% is its high end; supports the decision on which results are strong enough to act on (section 4.4). Interval method from Lewis and Sauro, Journal of Usability Studies, 2006, computed as in section 3.4; ticks at the plan's marks: 15% (cross-listing), 50% (home placement), 70% and 80% (task success). Tone 3 the employee and the app; tone 6 a stop, the one result whose interval lies wholly below its mark (T7, mark 70%). Pilot results from Deliverable D, TT-A and CS-A; '40 of 50' from section 3.4's table. Perqo and its pilot are fictional.", "rows": [
 {"label": "T1 success, 12 of 12", "low": 71.8, "high": 100, "tone": 3},
 {"label": "T2 success, 11 of 12", "low": 62.5, "high": 100, "point": 91.7, "tone": 3},
 {"label": "T7 success, 4 of 12", "low": 13.6, "high": 61.2, "point": 33.3, "tone": 6},
 {"label": "Cookery in Meals, sort, 5 of 12", "low": 19.3, "high": 68.1, "point": 41.7, "tone": 3},
 {"label": "Cookery in Meals, tree, 4 of 12", "low": 13.6, "high": 61.2, "point": 33.3, "tone": 3},
 {"label": "Yoga in Learning, tree, 3 of 12", "low": 8.3, "high": 53.9, "point": 25.0, "tone": 3},
 {"label": "Any task, 40 of 50", "low": 66.8, "high": 88.9, "point": 80.0, "tone": 3}]}
```

What the figure says, row by row (Perqo, fictional):

- **T1, 12 of 12, does not pass.** Its lower end is 71.8%, under T1's 80% mark. Twelve successes in twelve cannot show that a P1 task clears 80%; by section 3.4's formula, no perfect score can until 19 participants.
- **T2, 11 of 12, is undecided.** It looks like a pass and is not one; without the added node it would be 9 of 12 (section 4.1).
- **T7, 4 of 12, fails its 70% mark.** The upper end, 61.2%, is below the mark: even this small sample shows that most employees do not look under Account for a past message. A small sample can show a large failure, because a large effect moves the whole interval; it can show a pass only at the extreme: at 12 participants nothing short of 12 of 12 clears a 70% mark (T3 does), and nothing clears 80%.
- **The cookery course in Meals** clears the 15% cross-listing mark in the sort (lower end 19.3%) and misses it in the tree (lower end 13.6%). Two methods, one question, two verdicts: the evidence is undecided until the planned run.
- **The yoga class in Learning**, 3 of 12, is undecided: its interval runs from 8.3% to 53.9%.
- **40 of 50** is the planned run's resolution at 80%: an interval of 22.1 points, from 66.8% to 88.9%. Against a 70% mark it is undecided; at 50 participants a 70% mark passes from 42 successes (84%).

## 5 · Running each method cheaply and remotely

Every method in this unit can be run on paper, or with a video call, a form and a spreadsheet; none needs a specialised tool, though tools that automate the recording exist for each. What each needs, at the least:

- **Closed or hybrid card sort.** Paper cards and category headers on a table for in-person sessions; remotely, a form with one question per card and the categories as its choices (closed), plus a free-text "another group" choice (hybrid). Record one row per participant and one column per card in a spreadsheet; M-05 is a count per column, M-06 a count per pair. Spencer prefers physical cards and sorting in teams (Gaffney 2009); a remote form gives individual sorts, which is what CS-1 asks for.
- **Open card sort.** The same, with blank headers the participant names. The analysis is heavier: the names must be read and grouped before counting, and the similarity matrix needs every pair counted (section 4.3).
- **Tree test.** On index cards, moderated, as the Boxes and Arrows article describes; remotely, either a moderator reads the tree level by level over a video call and the participant says where they would go, or the tree is built as a set of linked plain pages, one level per page, with a "I'd find it here" link on each node and a log of the pages visited. Laubheimer notes that the quantitative tree test "is often executed as a remote, unmoderated study" (Laubheimer 2023). Record the path, the final node, the time and any skip, per participant per task.
- **First-click test.** A screen image shown on a video call, the participant asked to point and say where they would tap, the moderator noting the spot against the screen's areas; or, unmoderated, the image as a page whose areas are links, each recording which was chosen. Bailey and his colleagues' point that first-click tasks are fast (section 2.3) is what makes 50 participants affordable.
- **Search-log analysis.** An export of the queries for one period, one row per search, with the results count; group the queries that express one need, sort by frequency, list the zero-result ones (Farrell 2017; IA3, section 5.2). Remove personal identifiers before the log is shared (Farrell 2017).
- **Analytics paths and funnels.** The screen views by identifier, per session (IA9, section 6.3), read as sequences: a count of sessions by first screen, the share reaching each step of a funnel, the loops between two screens.
- **Usability test.** A video call, the participant's own phone shared to the screen or held to its camera, a prototype or the built app on a test account, a moderator and a note-taker; five participants a round (Nielsen 2000).

Recruiting is the cost that does not shrink. Perqo's employees are reached only through their employers (Perqo, fictional), so every test with employees goes through the client's HR, arranged by customer success, the team that supports each client's account owner (IA10, section 2.5). Two rules from the evidence govern who is asked. The participants must be the people the structure is for: Nielsen's distinct user groups each need their own (Nielsen 2000), and HR managers, who work in Admin and its words daily (IA1, Deliverable; IA3, section 6.2, assumed), are not stand-ins for employees. And they should come from more than one client, since Katsanos and his colleagues found studies agreeing only for participants of similar profile (Katsanos and others 2019), and one client's policy and words are one profile (IA10, section 2.7, on clients' words).

## 6 · From result to IA change, and when a result is too weak

### 6.1 · What each verdict does to the IA

IA9 set the loop a result closes: a hypothesis is raised from a signal or an assumption; a test confirms or fails the structure; a confirmed structure closes the hypothesis in the decision log "as declined, with the test as its reason", and a failed one raises a change that runs the change-control flow (IA9, sections 4.2 and 6.4). RV-11 runs the structure test before and after any change to a top level or a tab (IA9, Deliverable C). This unit adds what each verdict does (Perqo, fictional; this unit's rules):

| Verdict | From | What happens to the IA |
|---|---|---|
| Pass | interval wholly at or above the mark | the assumption's "assumed" is removed from the artefact's note, citing the plan row (V-) and the test's date; any DL entry proposing a change to that part closes as declined, with the test as its reason (IA9, section 6.4) |
| Fail | interval wholly below the mark | a DL entry is proposed for the failing part, citing the result; the change is tested before it is applied, on the same tasks (RV-11) |
| Undecided | interval across the mark | nothing in the IA changes; the assumption stays "assumed", now with the result attached; the next step is a larger sample, a second method, or IA12's register |
| Problem seen (usability) | a problem shown by 2 or more of 5 participants (M-11) | logged as a fault with the screen identifier, and a DL entry proposed; the next round tests the fix |
| Problem seen once | 1 of 5 | logged and watched in the next round; no change |

The usability rule (two of five) is this unit's working threshold, built on Nielsen and Landauer's model of a share of problems found per participant (Nielsen 2000): by the binomial arithmetic, a problem that one participant in three meets shows in two or more of five a little more often than not (54% of the time), and a problem seen once may be one person's. The arithmetic and the threshold are this unit's.

The plan in the Deliverable is the artefact of IA9's W-09, "Test the candidates and label what is untested", whose output is "test plans and results (IA11)"; its signal reads feed W-17, which hands the next cycle "hypotheses to IA11's tests" (IA9, Deliverable A).

### 6.2 · A failed result names the fault, and leaves the fix open

T7's pilot result says employees do not look under Account for a past message about a payment. It does not say where the message should go. Two diagnostics narrow the options: concentrated wrong first clicks point to the top level (the Boxes and Arrows article, practice), Laubheimer reads the first clicks of a low-success task as the places where the item could be moved or at least cross-listed, and an item people look for in more than one place may be listed in more than one place, a polyhierarchy he reserves for items a substantial share of people look for under more than one parent (Laubheimer 2024, read in summary; IA4, section 2.2, on polyhierarchy). Two candidate fixes follow, each with its own cost: list Notifications also under Card, or add to Purchases a line pointing to declined-payment messages in Notifications. Neither changes IA8's decision that a declined attempt is not a purchase and is not in Purchases (IA8, section 4.5); both add a route. Which works is a second test, and the plan names it: a variant tree, TT-1b, run beside TT-1 on T7, compared by a two-proportion test, which is the test Laubheimer recommends for comparing success between trees (Laubheimer 2024). The proposal is DL-016, proposed (Deliverable A, V-08).

### 6.3 · Six reasons a result is too weak to act on

1. **The interval crosses the mark.** Section 4.4's undecided band. More participants, or a second method, are the remedies.
2. **The sample is from the wrong people, or from one place.** The interval assumes a random sample from the people the structure is for; twelve employees of one client are a convenience sample of one profile (section 5). This is why the Perqo pilot decides nothing in the IA even where its intervals are clear: T7's failure becomes a proposal and a test (section 6.2), and the cookery course's clear sort result becomes a prediction for the planned run.
3. **The task gave the answer away.** Laubheimer: tasks "should avoid using terms that give away the answers" (Laubheimer 2023). TT-1's T9 (Lost card) cannot avoid the word card, which is both the employee's word and the tab's label (IA3, D1), so its success is read as an upper estimate, and its failure would be serious.
4. **The test measured something other than the question.** A card sort answers how people group; it cannot settle where they look in a built navigation (section 2.1; Tankala, as cited in IA9, section 6.4). A tree test answers where people look in a text-only hierarchy; it cannot settle whether a screen's content confirms the label on arrival (IA3, A3). A result is read for its own question only.
5. **The correct answers were chosen after the data.** Section 4.1's T2 change: legitimate when reasoned and recorded, and reported both ways.
6. **The method contradicts another, or the records.** The cookery course's two verdicts (section 4.4). Two methods that disagree leave the question open; neither is chosen because it gives the answer the team wanted.

### 6.4 · The confidence ladder

The six reasons and section 3's numbers sort evidence into rungs, each licensing a kind of decision and no more. The ladder is this unit's construct; each rung's limits come from the sections cited in it. IA12 and DD-IA2 cite rungs by identifier, C0 to C5.

| Rung | Evidence | Can decide | Cannot decide | At Perqo (Perqo, fictional) |
|---|---|---|---|---|
| C0 Assumed | reasoning at a desk, from the literature and the domain | a labelled default, marked "assumed" (IA2, section 5.2) | anything a person would do | IA6's task frequencies (IA6, Deliverable A) |
| C1 Signal | a log, ticket tags or paths, read once | what to test next (IA9, section 6.4) | why, or the fix | the zero results for "gym" (IA3, section 5.2) |
| C2 Observed | a small test with people: a usability round, a pilot, a moderated tree test | that a problem exists, and its cause (section 2.6) | a rate, or a pass (section 3.4) | the TT-1 pilot, 12 employees |
| C3 Measured | a planned test from the right people, its interval clear of a mark set beforehand | a label, a placement, a cross-listing | a top level on one method alone | TT-1 and CS-1 at 50 (planned) |
| C4 Converging | two methods of different kinds that agree | a change to a tab or a top level (IA9, RV-11) | how it performs in use | TT-1 with CS-1 on a cross-listing; FC-1 with ticket tags |
| C5 Confirmed in use | production records of the behaviour itself, or before and after a release | closing the DL entry as applied and confirmed | why it worked | AN-1 one quarter after release |

Figure 6 draws the ladder, rows in tone 5, shared, since the rungs serve any surface, and the Perqo column in tone 3, the employee, since every example is evidence about employees (the search log is the Help centre's, on perqo.com: section 2.4).

```viz
{"kind": "matrix", "caption": "Confidence ladder: six rungs of evidence for an IA decision, from assumed to confirmed in use, with what each can and cannot decide and its Perqo example; supports the decision on whether a result is strong enough to act on (section 6.4). Rungs this unit's construct: C0 from IA2, section 5.2 ('assumed'); C1 from IA9, section 6.4, and Rosenfeld through IA3, section 5.2; C2 from Nielsen, NN/g, 2000, and section 3.4; C3 from Lewis and Sauro, Journal of Usability Studies, 2006, and Laubheimer, NN/g, 2024; C4 from section 6.3 and IA9, RV-11; C5 from IA9, section 6.3. Rows tone 5, shared; the Perqo column tone 3, the employee. Perqo is fictional.", "cols": ["Rung", "Evidence", "Can decide", "Cannot decide", "At Perqo"], "rows": [
 {"label": "C0", "tone": 5, "cells": ["Assumed", "reasoning at a desk", "a labelled default", "anything a person would do", {"mark": "IA6's task frequencies", "tone": 3}]},
 {"label": "C1", "tone": 5, "cells": ["Signal", "a log, ticket tags or paths, read once", "what to test next", "why, or the fix", {"mark": "the zero results for 'gym'", "tone": 3}]},
 {"label": "C2", "tone": 5, "cells": ["Observed", "a small test with people", "that a problem exists, and its cause", "a rate, or a pass", {"mark": "the TT-1 pilot, 12 employees", "tone": 3}]},
 {"label": "C3", "tone": 5, "cells": ["Measured", "a planned test from the right people, its interval clear of a mark set beforehand", "a label, a placement, a cross-listing", "a top level on one method alone", {"mark": "TT-1 and CS-1 at 50 (planned)", "tone": 3}]},
 {"label": "C4", "tone": 5, "cells": ["Converging", "two methods of different kinds that agree", "a change to a tab or a top level", "how it performs in use", {"mark": "TT-1 with CS-1 on a cross-listing; FC-1 with ticket tags", "tone": 3}]},
 {"label": "C5", "tone": 5, "cells": ["Confirmed in use", "production records of the behaviour itself, or before and after a release", "closing the DL entry as applied and confirmed", "why it worked", {"mark": "AN-1 one quarter after release", "tone": 3}]}],
 "legend": [{"mark": "tone 5", "means": "shared: the rungs serve any surface", "tone": 5}, {"mark": "tone 3", "means": "the employee: every Perqo example", "tone": 3}]}
```

## 7 · No access to users: the bridge to IA12

When no employee can be reached, the ladder says what is left: C0 and C1. A team can still read the records (logs, tickets, paths) and the literature, label every result at its rung, and name the test that would lift it. That is the practice IA3 began with the search log, "proxy evidence, useful when no one can be interviewed, and labelled as proxy" (IA3, section 5.2), and IA9 built into its reviews: RV-04 (search log), RV-05 (ticket tags) and RV-06 (analytics paths) each produce hypotheses for this unit's methods, read at FO-06, support's ticket and log read (IA9, Deliverable C; IA10, Deliverable A, A.2).

Three cautions keep proxy evidence honest:

- **A proxy is not a cheaper test.** Colleagues sorting cards are a sample of people who know the product's words; on Nielsen's distinct-groups condition (Nielsen 2000) they test the team's model, which is the C0 claim the test was meant to check.
- **A record of use shows only those who used it.** A search log holds no employee who gave up before searching (section 2.4); an analytics path holds no employee who never opened the app.
- **An absent rung is recorded.** Where the plan below cannot be run (a client declines to let its employees take part, or no new joiner is available for the join test), the plan row stays, marked not run, and the assumption goes to IA12's register at its current rung with the row's test named. IA10's TP-05 is the case already on file: localisation has no forum and no test until a second language is added (IA10, Deliverable A, A.1), so its assumptions sit in the register, at C0, with DD-IA3 named.

## Deliverable · A · The Perqo app validation plan, scripts and templates

*Face of this artefact (IA2, the notation sheet): validation plan for the Perqo app IA (IA6, Deliverables A to C), with its scripts and analysis templates, at fidelity F3 for the scripts (ready to run) and F2 for the plan; decision: which test settles each assumption of the app IA, with which participants, by which rule, at what cost; readers: the IA designer (runs the tests), product management (cost, priority), customer success and clients' HR (recruiting), support (ticket tags), engineering (analytics queries); leaves out: Perqo Admin's and perqo.com's tests (handed to IA12's register in A.2, with a reason each), the full run's results, the visual design of any test material; owner: the IA designer; version 1, dated 10 November 2026; the pilot results in D are fictional and decide nothing in the IA; Perqo is fictional.*

### A.1 · The validation plan

Each row is one test of one or more assumptions of the app IA (Perqo, fictional). "What decides" gives the metric (section 1.2), the mark and the rule (section 4.4, at 50 participants: a 70% mark passes at 42 or more and fails at 28 or fewer; an 80% mark passes at 46 or more and fails at 34 or fewer; a cross-listing is kept at 13 or more and removed at 2 or fewer). Costs are in staff time and participants' time; recruiting goes through clients' HR, arranged by customer success (section 5). "Rung" is the rung the test reaches when it passes or fails (section 6.4). Every row cites its source assumption.

| ID | Question (assumption, where) | Method | Participants | What decides | Cost | Rung |
|---|---|---|---|---|---|---|
| V-01 | Are the assumed task frequencies and their ranking right? (IA6, Deliverable A) | AN-1: analytics, task starts per employee per month (M-08), on the app as it stands now (IA3's as-is) and one quarter after release; card payments per employee from the transactions table | every active employee's records for one quarter; no recruiting | measured M-08 replaces each assumed frequency; Home's placement holds while T-02 is the most frequent task in the app; a P2 or P3 task measured above a P1 task goes to FO-01 as a proposed DL entry | product management 1 day; engineering 0.5 day per read | C5 |
| V-02 | Are most visits one or two tasks begun from Home or a notification? (IA6, section 3.2) | AN-2: analytics session paths, short-visit share (M-09) | every session in one quarter | holds when the interval's lower end is above 50%; fails when its upper end is below 50%, and Home's routes go to FO-01 | product management 1 day | C5 |
| V-03 | Do employees read the four balances as four pots? (IA6, A-1, A-2.1 to A-2.4; IA3, B1) | UT-1, task U1: moderated remote usability test | 5 employees a round, two rounds, none from the pilot | M-11: a participant who would pay a Learning course from Meals money shows the fault; 2 or more of 5 → fault and a proposed DL entry on Home's layout or wording; round 2 tests the change | IA designer 3 days a round; 5 × 45 minutes a round | C2 |
| V-04 | Do employees find a rejected claim in Claims? (IA6, A-3; IA3, B2) | TT-1, task T2; FC-1, task F1 | 50 (TT-1); 50 others (FC-1) | M-01 on T2 against 80%, and M-03 on F1 against 80%; the share choosing Rejected (TN-16) read for where people look first | within TT-1 and FC-1 | C3; C4 when both agree |
| V-05 | Are the far members found by their cross-listings? (IA6, A-2.1, A-2.2, A-2.4; IA3, C3; IA4, R6) | TT-1, tasks T3 to T5; CS-1 | the same 50, half sorting first | each cross-listing kept when both methods put the lower end of the second category's share at or above 15%; removed when both put the upper end below 15%; otherwise undecided and still "assumed"; home placement confirmed at a lower end of 50% in CS-1 | within TT-1; CS-1 adds 6 minutes a participant | C4 when both agree; C3 on one |
| V-06 | Are Card offers found under Card and from the category screens? (IA6, A-4.3, B.6) | TT-1, task T6; FC-1, tasks F2 and F4 | as V-04 | M-01 on T6 against 70%; M-03 on F2 and F4 against 70%; the split between Card offers (TN-23) and Card offers in Meals (TN-11); the comparison with the as-is Home banner, which B.6 left to this unit, is V-17 | within TT-1 and FC-1 | C3; C4 when TT-1 and FC-1 agree |
| V-07 | Is the rule line understood before submitting? (IA6, A-3.1) | UT-1, task U2 | as V-03 | M-11: a participant who picks the wrong claim as the one waiting for HR shows the fault; 2 of 5 rule | within UT-1 | C2 |
| V-08 | Are Profile, Notifications and Help found under Account? (IA6, A-5) | TT-1, tasks T7 and T10; TT-1b if DL-016 is accepted | 50 (TT-1); 50 others (TT-1b, three tasks) | M-01 on T7 and T10 against 70%; TT-1b against TT-1 on T7 by a two-proportion test | within TT-1; TT-1b 1 day and 50 × 3 minutes | C3; C4 with FC-1's F5 |
| V-09 | Does asking for notifications after the first claim get more employees to allow them than asking at first run? (IA6, A-3.3) | AN-3: a comparison of the two timings, employees assigned at random, opt-in share (M-10) | every employee joining at any client in one quarter | the 95% interval of the difference (after the first claim minus at first run): above zero keeps the timing; below zero moves the prompt to first run; across zero keeps the timing, undecided | engineering 2 days; product management 1 day | C5 |
| V-10 | Can an employee who installs the app from the invitation join? (IA6, E-2, A-0.1) | UT-1, task U3, on the participant's own phone without the app | 5 new joiners at a client in onboarding (CL-4), one round | 2 of 5 rule on the join path; any participant who cannot join without help is a fault | IA designer 2 days; 5 × 30 minutes | C2 |
| V-11 | Do employees understand a declined payment from the balance they saw, and act on the notice? (IA6, C.2; IA8, section 4.5) | five short interviews within a week of a decline; TK-1: ticket tags on declines (E-8), before and after the notice | 5 employees who had a decline, through their HR | a misreading in 2 of 5 → proposed DL entry on the notice's wording or route; TK-1 read as C1 beside it | IA designer 1.5 days; 5 × 20 minutes; support within RV-05 | C2; C4 with TK-1 |
| V-12 | Do the renamed labels predict their pages? (IA6, B.2; IA3, A1 to A3) | TT-1, tasks T6 and T10; FC-1, task F3 | as V-04 | M-01 on T6 and T10 against 70%; M-03 on F3 against 70% | within TT-1 and FC-1 | C3; C4 when both agree |
| V-13 | Do the Help centre's top queries still fail after the fixes? (IA3, E2 and section 5.2; IA9, section 6.1 and RV-04) | LG-1: the next quarter's For employees log | none: the log | M-07 per query for "allowance" and "gym", the two that returned zero results (IA3, section 5.2), and the rank of "refund": a query still returning zero results goes to FO-03 as a synonym or content fault; a frequent query for a thing the app holds becomes a TT-1 or FC-1 task next cycle | within RV-04 | C1 |
| V-14 | Do employees name and group the app's objects as IA4's map does? (IA4, section 4.3, app side) | no card sort: settled through TT-1's object labels (V-08, V-12) and the words in LG-1 and TK-1 | as those rows | as those rows; an object label that fails in TT-1 is the object map's fault as well as the label's | none beyond those rows | as those rows |
| V-15 | Do support's ticket tags locate problems on the app's screens? (IA9, RV-05 and its IA11 table) | TK-1's most-tagged A- screens for one quarter, set beside FC-1's results on the same screens | none beyond FC-1 | tags kept as a locator when the screens FC-1 fails are among the five most-tagged; otherwise the tag set goes to FO-06 for review | support 0.5 day | C4 |
| V-16 | Do employees allow notifications early enough to see a decline? (IA8, section 4.5) | AN-4: the opt-in share (M-10) among employees at their first decline | every employee with a first decline in one quarter | when the interval's upper end is below 50%, a DL entry proposes asking at the first decline too | engineering 1 day | C5 |
| V-17 | Is the app as designed at least as findable as the app it replaces, on the tasks whose answers, or the tab around them, changed? (IA9, RV-11, triggered by IA6's changes to Home, Benefits, Claims and Account; IA6, B.6, the offers banner) | TT-0: IA3's as-is tree (Deliverable B, B.6), tasks T2, T6, T7, T8 and T10, compared with TT-1 on the same tasks | 50 employees who take neither TT-1 nor FC-1 | per task, a two-proportion test on M-01 (Laubheimer 2024): a task whose 95% interval of the difference (TT-1 minus TT-0) lies wholly below zero is a fault of the redesign and a proposed DL entry; T6 answers B.6's question on the banner | IA designer 1.5 days; 50 × 6 minutes | C3 |

**Why V-14 has no card sort.** The app's structure exists, and IA9 set the order for a structure that exists: test it first, and sort only when the test shows the categories are wrong (IA9, section 6.4; Tankala, as cited there). A sort of the app's objects would answer how employees would group them, a question IA6 has already answered by design; TT-1 asks whether they can find them as designed.

**Order and dependencies.** TT-1 and CS-1 run first, in one unmoderated session per participant, 50 employees from at least two clients whose groups have all four categories open, at least 15 of them joined in the last three months; half sort first, half tree-test first, and if the halves differ beyond their intervals, the two are reported apart. FC-1 runs with 50 other employees, and TT-0 with 50 more, because people who have just walked one tree on the same tasks would know the answers in the next. UT-1's first round runs on the built app or a prototype of it; its second, after round one's fixes. AN-1 to AN-4 run on the records; LG-1 and TK-1 within RV-04 and RV-05. Employees of clients' HR and finance teams are screened out (section 5). Each participant gives consent to the recording of their answers and their time, and no answer is stored with a name.

**DL-016 (proposed).** From the TT-1 pilot's T7, 4 of 12 against a 70% mark (Deliverable D, TT-A): employees look for a past message about a payment under Card. Proposal: run TT-1b beside TT-1, a variant tree identical but for one node, Notifications listed also under Card as "Payment messages" (opening A-5.2); compare T7 by a two-proportion test; the result decides between that listing, a line on Purchases pointing to the messages, and no change. Neither changes IA8's decision that a declined attempt is not in Purchases (IA8, section 4.5). Proposed by the IA designer; routed to FO-01 (IA9, section 4.1); told: product management, support.

### A.2 · Tests named for IA11 outside the app IA: where each goes

Every row of IA7 to IA10's assumption tables that names a test for IA11, with IA5's sign-in assumption that IA7's table carries, and where each goes and why; the rows the plan above takes are marked "plan". "Register" is IA12's assumption register; the method column names the section of this unit that specifies the method, so the register can cite one test per row.

| # | From | Assumption | Goes to | Method (section) | Why there |
|---|---|---|---|---|---|
| 1 | IA7 | the sizing client's volumes | register; DD-IA2 | analytics on live clients (2.5) | Admin and the business case, not the app |
| 2 | IA7 | HR's and finance's most frequent work decides their landing pages | register | analytics, first actions after sign-in, RV-06 (2.5) | Admin |
| 3 | IA7 | in-list find serves known-item seeking | register | usability test with HR managers at FO-07 (2.6) | Admin |
| 4 | IA7 (and IA4, section 4.3, Admin side) | HR and finance recognise their objects and names | register | hybrid card sort with admin users from at least two clients at FO-07 (2.1) | Admin's labels belong to FO-07's cycle (IA10, A.2) |
| 5 | IA7 | a finance manager does not need Approvals | register | interviews with finance managers (none of this unit's methods) | a need, not findability |
| 6 | IA7 | HR does not need individual card payments | register | interviews; ticket tags as C1 (2.4 for the reading) | a need, not findability |
| 7 | IA7 | the account owner fits how clients assign admin rights | register | interviews at onboarding, FO-05 | a contract and role question |
| 8 | IA7 | the list-detail layout keeps HR's place in the queue | register | usability test of a run of ten decisions (2.6) | Admin |
| 9 | IA7 (IA5's sign-in assumption) | the sign-in line reaches employees who land on Admin | register | analytics of Admin's failed sign-ins, RV-06, and the search log, RV-04 (2.4, 2.5) | Admin's screen; C1 until a test with employees |
| 10 | IA8 | the decline notice is understood and acted on | plan, V-11 | | the app |
| 11 | IA8 | employees allow notifications early enough to see a decline | plan, V-16 | | the app |
| 12 | IA8 | inviting only after budgets are set does not delay onboarding | register | analytics, time from contract to first join; onboarding interviews (2.5) | Admin and the client lifecycle |
| 13 | IA8 | the leaver rules fit clients' contracts | register | interviews with clients and HR managers | a contract question |
| 14 | IA8, G-5 | how a leaver learns of a decided claim | register, as an open question with an owner | interviews with HR managers; tickets from former employees (2.4) | the leaver cannot be reached in the app |
| 15 | IA8; IA10 | the trees' words let sales explain the rules (BR-3) | register | IA8's recorded-demo restatement test, at FO-04 | a comprehension test of a brief, not of a structure |
| 16 | IA8; IA10 | readers can read one layer, or one brief, alone | register | IA8's one-layer question test (D.5) | a reading test of an artefact |
| 17 | IA9 | stories citing identifiers keep build debt down | register | RV-02's share of built screens that differ from their F3 artefact, compared from quarter to quarter | a process measure |
| 18 | IA9 | the F3 gate does not slow delivery | register | stories held at RV-01, read at RV-10 | a process measure |
| 19 | IA9 | a quarterly face audit keeps record debt from building | register | DL entries accepted and not applied, at RV-10 | a process measure |
| 20 | IA9 | ticket tags locate problems on the IA | plan, V-15, for the app's screens; register for Admin's | | the app's half is cheap beside FC-1 |
| 21 | IA9 | the routing rule sends changes to the right decider | register | DL entries reopened or superseded, at RV-10 | a process measure |
| 22 | IA10 | each function's question is the one it asks | register | interviews with each function | a touchpoint question |
| 23 | IA10 | engineering can build from BR-2 without a meeting | register | questions raised at FO-02, counted per release | a process measure |
| 24 | IA10 | positions recorded reduce reopened decisions | register | DL entries reopened within a quarter, before and after DL-011 | a process measure |
| 25 | IA10 | clients' structure enters as data without loss | register | interviews with account owners at FO-05 | a client question |

IA10's forums carry two of these streams: FO-06 (the ticket and log read) produces the hypotheses that feed V-13, V-15 and the next cycle's rows, and FO-07 (the client validation session) is where rows 3, 4 and 8 run with admin users from at least two clients (IA10, Deliverable A, A.2). TP-05's row stays dormant: localisation has no forum and no test until a second language (IA10, A.1; section 7).

## Deliverable · B · Tree-test script TT-1

*TT-1, version 2 (after the pilot: T2's correct nodes extended, section 4.1). Unmoderated online, or moderated over a video call for the paper or reading form (section 5). One session: instructions, a warm-up, ten tasks in random order, two closing questions. Median 9 minutes in the moderated pilot (Perqo, fictional).*

### B.1 · Screener and consent

1. Do you work for a company that gives you a Perqo benefits budget? (yes continues)
2. Do you work in your company's HR or finance team? (yes ends the session, with thanks)
3. Which of these can you spend on: Health, Learning, Mobility, Meals? (all four continue; the tree shows all four)
4. When did you join your company? (record: in the last three months, or earlier; quota at least 15 of 50 in the last three months)
5. Consent: "We will record which options you choose and how long each task takes. We will not store your name with your answers. You can stop at any time." (agree continues)

### B.2 · Instructions, read or shown to the participant

"Thank you for helping. We are testing how the Perqo app is organised, not you; there are no wrong answers. You will see a list of the app's sections as plain text, with no pictures. For each task, click through the list to where you would expect to find the answer, then choose 'I'd find it here'. You can go back up at any time. If you have no idea, choose 'Skip this task'. Please don't search elsewhere; we want your first instinct."

Moderated form, added: "Think aloud if you can: say what you are looking for and why you choose each option. I won't tell you whether an answer is right."

### B.3 · The tree

The text-only tree of the Perqo app as designed (IA6, Deliverable B, B.3), each node with its tree identifier (TN-) and the screen or page it stands for. Elements on Home are nodes under Home. Left out, because no task can end on them: Join and sign in (A-0), which a signed-in employee does not see; the screens reached only inside a flow or from a list item (Check and submit, Claim submitted, Claim, Purchase); and How approval rules work, a link on New claim. The four Claims groups are nodes, since the Claims screen shows them. The routes leaving the app (H-) are nodes, since an employee may choose them. Under Meals, the route Card offers in Meals appears because the example client's offers are in Meals only (Perqo, fictional), and the route shows only for a category with offers (IA6, B.5).

| ID | Node, as shown | Parent | Stands for |
|---|---|---|---|
| TN-00 | Perqo app | none (not selectable) | the tab bar |
| TN-01 | Home | TN-00 | A-1 |
| TN-02 | Balance | TN-01 | on A-1: each open category and what remains |
| TN-03 | Your balance explained | TN-01 | H-2.2.1 |
| TN-04 | Recent activity | TN-01 | on A-1 |
| TN-05 | New claim | TN-01 | A-3.1, from Home |
| TN-06 | Benefits | TN-00 | A-2 |
| TN-07 | Health | TN-06 | A-2.1 |
| TN-08 | Learning | TN-06 | A-2.2 |
| TN-09 | Mobility | TN-06 | A-2.3 |
| TN-10 | Meals | TN-06 | A-2.4 |
| TN-11 | Card offers in Meals | TN-10 | A-4.3, filtered (E-7) |
| TN-12 | What you can claim in each category | TN-06 | H-2.1.3 |
| TN-13 | Claims | TN-00 | A-3 |
| TN-14 | Submitted | TN-13 | A-3, its group |
| TN-15 | Approved | TN-13 | A-3, its group |
| TN-16 | Rejected | TN-13 | A-3, its group |
| TN-17 | Paid | TN-13 | A-3, its group |
| TN-18 | New claim | TN-13 | A-3.1 |
| TN-19 | Help with claims | TN-13 | H-2.1 (it also lists H-1.2.5) |
| TN-20 | Card | TN-00 | A-4 |
| TN-21 | Card details | TN-20 | A-4.1 |
| TN-22 | Purchases | TN-20 | A-4.2 |
| TN-23 | Card offers | TN-20 | A-4.3 |
| TN-24 | Freeze card | TN-20 | A-4.4 |
| TN-25 | Where you can pay with the Perqo card | TN-20 | H-2.3.2 |
| TN-26 | Freezing and unfreezing your card | TN-20 | H-2.3.1 |
| TN-27 | Account | TN-00 | A-5 |
| TN-28 | Profile | TN-27 | A-5.1 |
| TN-29 | Notifications | TN-27 | A-5.2 |
| TN-30 | Help | TN-27 | H-2, For employees |

TT-1b, if DL-016 is accepted: the same tree with one node added, TN-31 "Payment messages", under Card (TN-20), standing for A-5.2. Tasks: the warm-up, T7 and T2, in random order after the warm-up.

### B.4 · The tasks

Each task is written in the employee's words and avoids the label it targets (Laubheimer 2023); where that is impossible, the note says so. The correct nodes are the answers that reach the outcome in the app as designed; the "read" column is what the analysis takes from the task beyond M-01. Marks from section 4.4 by IA6's priority.

| ID | Short name | Task, as shown | Correct nodes | Mark | Tests | Read |
|---|---|---|---|---|---|---|
| W | Warm-up | You want to check which email address the app has for you. | TN-28 | not scored | the participant's grasp of the tree | none |
| T1 | Train pass balance | You want to know how much you have left to spend on a train pass. | TN-09, TN-02 | 80% (T-02, P1) | IA6, B1 fix on Home; V-14 | which node: the category or Home's Balance |
| T2 | Turned-down receipt | A receipt you sent in to be paid back was turned down last week. You want to see why. | TN-16, TN-29, TN-04 (added after the pilot) | 80% (T-05, P1) | V-04 | share at TN-16; reported with and without TN-04 |
| T3 | Yoga class | You have signed up for a weekly yoga class and want to check that your employer will pay for it. | TN-07, TN-08 | 70% (T-07, P2) | V-05 | share at TN-08, the cross-listing |
| T4 | Cookery course | You want to take a cookery course and check that it is covered. | TN-08, TN-10 | 70% (T-07, P2) | V-05 | share at TN-10, the cross-listing |
| T5 | Bike helmet | You need a new helmet for cycling to work and want to see whether you can spend your benefits on it. | TN-09, TN-07 | 70% (T-07, P2) | V-05 | share at TN-07, the cross-listing |
| T6 | Restaurant deals | You heard that some restaurants give money off when you pay with your work benefits. Find where those deals are listed. | TN-23, TN-11 | 70% (T-08, P3) | V-06, V-12 | split between TN-23 and TN-11 |
| T7 | Past message | Last week the app told you a payment at a shop had not gone through. You want to read that message again. | TN-29 | 70% (T-03, P2) | V-08 | first clicks; wrong final nodes |
| T8 | Approval rule | Before sending in a large receipt, you want to know whether someone at your employer has to approve it first. | TN-18, TN-05, TN-19, TN-30 | 80% (T-06, P1) | V-07 (where people look; understanding is U2) | which route |
| T9 | Lost card | You think you left your Perqo card in a taxi. Stop anyone from using it. | TN-24 | 70% (T-10, P2) | V-08 for Card's grouping | the word "card" cannot be avoided: success is an upper estimate |
| T10 | How balances work | You want to understand how the money shown in the app works. | TN-03, TN-30 | 70% (T-09, P3) | V-12 (Your balance explained) | which route; the pilot's wording added "and what it can be spent on", which made TN-12 a defensible answer (section 6.3, reason 4), and was cut after the pilot, so T10's pilot result understates success |

T2's correct nodes: a rejected claim is reached in Claims (TN-16), from its notification (TN-29, which opens the claim: IA6, E-4), or from Recent activity while it is recent (TN-04). T8's: the rule shows on New claim from either route (TN-05, TN-18), and How approval rules work (H-1.2.5) is listed under Help with claims (TN-19) and reached from Help (TN-30) through For employees (IA5, Deliverable A).

### B.5 · Closing questions, and what is recorded

After the last task: "Was any task hard to understand? Which, and why?" (free text) and "Is there anything in the app you looked for and did not see?" (free text). Recorded per participant: identifier (no name), client, joined in the last three months (yes or no), order (tree first or sort first), and per task the path of nodes, the final node or skip, and the time from the task's start to the answer.

### B.6 · TT-0: the as-is tree, for V-17

TT-0 is IA3's as-is navigation of the Perqo app (IA3, Deliverable, the as-is sitemap), drawn as a text-only tree with the same screener, instructions and closing questions as TT-1, and five of its tasks in the same words: T2, T6, T7, T8 and T10, after the warm-up. Its nodes, by path: Home (Balance; Learn more; Recent activity; Discover; +), Benefits (Health; Learning; Mobility; Meals; Perks), Claims (Submitted; Paid; New claim, with Check and submit under it; Help with claims), Card (Card details; Purchases; Freeze card), Account (Profile; Notifications; Documents, with Approval rules under it; Help). The as-is labels are shown as the as-is app showed them, the first "Learn more" being the one under Balance and the "+" shown as the character itself; the second "Learn more", under Discover, is left out, since it opened the same offers list (IA3, Deliverable).

| Task | Correct nodes on TT-0 | Why |
|---|---|---|
| T2 Turned-down receipt | Account › Notifications | rejected claims were not listed in Claims and appeared only in Notifications (IA3, Deliverable) |
| T6 Restaurant deals | Home › Discover; Benefits › Perks | the offers list had these two placings (IA3, Deliverable) |
| T7 Past message | Account › Notifications | as TT-1 |
| T8 Approval rule | Account › Documents › Approval rules; Account › Help | the rule was in the PDF H-1.2.4 under Documents, and in the Help centre reached from Help (IA3, Deliverable) |
| T10 How balances work | Home › Learn more; Account › Help | the first Learn more opened H-2.2.1 (IA3, section 1.2) |

## Deliverable · C · Closed card-sort protocol CS-1

*CS-1, version 1. Unmoderated online as a form, or moderated with paper cards (section 5). Same participants and screener as TT-1 (B.1); half sort before the tree test, half after. Median 6 minutes in the moderated pilot (Perqo, fictional).*

### C.1 · Instructions, read or shown to the participant

"Your employer's Perqo budget is split into four categories: Health, Learning, Mobility and Meals. Below are things people spend benefits on. For each one, choose the category where you would expect your employer to cover it. Choose one category for each. If you can't decide, choose 'Not sure'. There are no right answers; we want to know what you would expect."

Moderated form: the four category cards and a "Not sure" card are laid out; the twelve cards are handed over shuffled; the participant may think aloud; the moderator records the final placement of each card.

### C.2 · The cards

One card per item of the example client's policy, BI-001 to BI-012 (IA4, Deliverable B, B.3; IA6, B.3). Each card's text is the item in basic-level words (IA3, C2); one card is reworded so that no card shares a word with a category name, after Tankala's finding that participants match keywords (section 2.1). Cards are shown in a new random order for each participant.

| Card | Card text | Catalogue item | Home category (policy) | Second place (IA6, assumed) |
|---|---|---|---|---|
| C-01 | Gym membership | BI-001 | Health | none |
| C-02 | Yoga class | BI-002 | Health | Learning |
| C-03 | Therapy session | BI-003 | Health | none |
| C-04 | Coding course | BI-004 | Learning | none |
| C-05 | Cookery course | BI-005 | Learning | Meals |
| C-06 | Book | BI-006 | Learning | none |
| C-07 | Train pass | BI-007 | Mobility | none |
| C-08 | Bike helmet | BI-008 | Mobility | Health |
| C-09 | Bike repair | BI-009 | Mobility | none |
| C-10 | Dinner at a restaurant | BI-010, restaurant meal (reworded: "meal" matches Meals) | Meals | none |
| C-11 | Groceries | BI-011 | Meals | none |
| C-12 | Swimming pool entry | BI-012 | Health | none |

### C.3 · The categories

Health, Learning, Mobility, Meals (F-CAT's four top-level values: IA4, Deliverable B), and Not sure. The narrower terms are not shown, since the decision the employee makes in the app is between the four categories (IA6, B.3), and adding them would turn a closed sort of four into one of twelve. "Not sure" exists so that a participant who cannot place a card is not forced to guess; a card in Not sure counts in no category (M-05, M-06).

### C.4 · What is recorded

Per participant: identifier (no name), client, joined in the last three months, order; per card, the category chosen. After the sort, one free-text question: "Which card was hardest to place, and why?"

## Deliverable · D · Analysis templates

Each template is a table to fill per run, with its formulas and its decision rule, shown filled with the pilot where the pilot ran (Perqo, fictional; the pilot decides nothing in the IA: section 6.3).

### TT-A · Tree test

Per task: x = successes, n = attempts (a skip is a failure); success M-01 = x / n; interval by section 3.4's formula; verdict by section 4.4 (pass, fail, undecided); directness M-02 = direct successes / n; first click M-03 = first choices on a path to a correct node / n; correct node chosen, as counts; median time M-04 of successful attempts, in seconds; wrong final nodes, as counts. Then, per far-member task, the cross-listing share = choices of the cross-listing node / n, with its interval and the 15% rule. A comparison of two trees (TT-1b) uses a two-proportion test on M-01 and M-02 (Laubheimer 2024).

The TT-1 pilot, n = 12 for every task:

| Task | Mark | Success | Observed | 95% interval | Verdict | Direct | First click right | Correct nodes chosen | Wrong final nodes | Median time (s) |
|---|---|---|---|---|---|---|---|---|---|---|
| T1 Train pass balance | 80% | 12 | 100% | 71.8 to 100 | undecided | 11 | 12 | Mobility 8, Balance 4 | none | 11 |
| T2 Turned-down receipt | 80% | 11 (9 without TN-04) | 91.7% | 62.5 to 100 | undecided | 9 | 11 | Rejected 6, Notifications 3, Recent activity 2 | Purchases 1 | 14 |
| T3 Yoga class | 70% | 12 | 100% | 71.8 to 100 | pass (pilot: held) | 10 | 12 | Health 9, Learning 3 | none | 8 |
| T4 Cookery course | 70% | 11 | 91.7% | 62.5 to 100 | undecided | 9 | 11 | Learning 7, Meals 4 | Balance 1 | 10 |
| T5 Bike helmet | 70% | 10 | 83.3% | 54.0 to 96.5 | undecided | 8 | 10 | Mobility 9, Health 1 | Where you can pay with the Perqo card 2 | 12 |
| T6 Restaurant deals | 70% | 9 | 75.0% | 46.1 to 91.7 | undecided | 7 | 11 | Card offers 5, Card offers in Meals 4 | Meals 2, Balance 1 | 16 |
| T7 Past message | 70% | 4 | 33.3% | 13.6 to 61.2 | fail (pilot: DL-016 proposed) | 3 | 4 | Notifications 4 | Purchases 6, Card details 2 | 21 |
| T8 Approval rule | 80% | 10 | 83.3% | 54.0 to 96.5 | undecided | 7 | 10 | New claim under Claims 4, Help with claims 3, Help 2, New claim on Home 1 | What you can claim in each category 2 | 18 |
| T9 Lost card | 70% | 11 | 91.7% | 62.5 to 100 | undecided | 11 | 12 | Freeze card 11 | Freezing and unfreezing your card 1 | 7 |
| T10 How balances work | 70% | 9 | 75.0% | 46.1 to 91.7 | undecided | 7 | 10 | Your balance explained 6, Help 3 | What you can claim in each category 2, Balance 1 | 15 |

Cross-listing shares in the pilot (the 15% rule): T3, Learning 3 of 12, 25.0%, interval 8.3 to 53.9, undecided; T4, Meals 4 of 12, 33.3%, interval 13.6 to 61.2, undecided; T5, Health 1 of 12, 8.3%, interval 0.0 to 37.5, undecided.

What the pilot hands the planned run: T7 is the one task predicted to fail, and DL-016's variant goes with it; the cookery course's two methods disagree; T3's 12 of 12 clears its 70% mark and is held as a pilot result; every other task is undecided at 12.

### CS-A · Closed card sort

Per card: n = participants who sorted it; home share M-05 = placements in the home category / n, with its interval, confirmed at a lower end of 50%; second-place share = placements in IA6's assumed second category / n, with its interval and the 15% rule; other placements and Not sure, as counts. Then the similarity matrix M-06 for the cards in question, each cell the participants who placed both cards in one category divided by n; read for firm pairs and for the cards least tied to their home, never as a dendrogram alone (section 4.3). Then the convergence check for V-05: for each cross-listing, the verdict from CS-1 beside the verdict from TT-1 (T3 to T5); a cross-listing is decided only where the two agree.

The CS-1 pilot, n = 12 (the eight cards everyone placed at home are given together):

| Card | Home | Home share | 95% interval | Home verdict | Second place | Second share | 95% interval | Cross-listing verdict | Other |
|---|---|---|---|---|---|---|---|---|---|
| C-02 Yoga class | Health | 9 (75.0%) | 46.1 to 91.7 | undecided | Learning | 3 (25.0%) | 8.3 to 53.9 | undecided | none |
| C-03 Therapy session | Health | 11 (91.7%) | 62.5 to 100 | confirmed | none | | | | Not sure 1 |
| C-05 Cookery course | Learning | 7 (58.3%) | 31.9 to 80.7 | undecided | Meals | 5 (41.7%) | 19.3 to 68.1 | keep (pilot: held; TT-1 disagrees) | none |
| C-08 Bike helmet | Mobility | 9 (75.0%) | 46.1 to 91.7 | undecided | Health | 2 (16.7%) | 3.5 to 46.0 | undecided | Not sure 1 |
| C-01, C-04, C-06, C-07, C-09, C-10, C-11, C-12 | as C.2 | 12 each (100%) | 71.8 to 100 | confirmed | none | | | | none |

Convergence for V-05 in the pilot: yoga class, undecided in both; cookery course, keep in CS-1 and undecided in TT-1, so undecided; bike helmet, undecided in both.

### FC-A · First-click test FC-1

*FC-1: six tasks on F2 screen images of the app as designed (IA6, Deliverable C's wireflow screens), one screen per task, unmoderated or over a video call (section 5); 50 employees who have not taken TT-1, screened as B.1.*

| ID | Screen | Task, as shown | Correct areas | Mark | Plan row |
|---|---|---|---|---|---|
| F1 | Home, A-1 | A receipt you sent in to be paid back was turned down. Where would you tap to see why? | the Claims tab; the Account tab; the claim's line in Recent activity | 80% | V-04 |
| F2 | Home, A-1 | You want money off at a restaurant for paying with your work benefits. Where would you tap? | the Card tab; the Meals line under Balance | 70% | V-06 |
| F3 | Home, A-1 | You want to understand how the money shown here works. Where would you tap? | Your balance explained; the Account tab | 70% | V-12 |
| F4 | Meals, A-2.4 | You want money off at a restaurant for paying with your work benefits. Where would you tap? | Card offers in Meals; the Card tab | 70% | V-06 |
| F5 | Home, A-1 | Last week the app told you a payment at a shop had not gone through. Where would you tap to read that message again? | the Account tab | 70% | V-08, V-15 |
| F6 | Claims, A-3 | Before sending in a large receipt, you want to know whether someone at your employer must approve it. Where would you tap? | New claim; Help with claims | 80% | V-07 (where people look; U2 tests understanding) |

Per task: M-03 = clicks in a correct area / n, with its interval and verdict by section 4.4; the wrong areas, as counts, each named by its element on the screen; median time to the click (M-04, all clicks). Per screen: the elements no one chose, read against IA3's checklist item F2 ("Is everything a person needs for a task reachable by a route from where they are when they need it?"). For V-15: the screens whose tasks fail, set beside TK-1's five most-tagged A- screens for the same quarter.

| Task | n | Clicks in a correct area | M-03 | 95% interval | Verdict | Wrong areas (counts) | Median time to click (s) |
|---|---|---|---|---|---|---|---|
| F1 to F6 | | | | | | | |

### UT-A · Usability test UT-1

*UT-1: moderated over a video call, the participant's own phone shared or held to the camera; the built app on a test account or a clickable prototype of it; tasks U1 and U2 in each round with five employees, U3 in its own round with five new joiners (Deliverable A, V-03, V-07, V-10).*

| ID | Task, as told to the participant | Set-up | Watch for |
|---|---|---|---|
| U1 | "You paid for an online coding course yourself. Can you get that money back from your benefits? Show me how you'd check." | test account with Learning at 0 and Meals with money left | whether the participant reads Meals money as available for the course; the words they use for the money |
| U2 | "Here are two receipts, one small and one large. Which of them would someone at your employer have to approve before you're paid? How can you tell?" | the group's limit shown on New claim; one receipt under it, one over | whether the participant finds and reads the rule line before choosing |
| U3 | "Here is the email your HR team sent you. Get yourself set up so you can use your benefits." | the participant's own phone without the app; an invitation email to a test work address | each step from the email's link through S-6, the app store and Join; where they stop |

Per participant per task: completed without help, with help, or not; the problem seen, with the screen identifier where it happened (A-, S-); what the participant said, in their words; severity: blocks the task, slows it, or neither (this unit's three grades). Per round: each problem with its count of participants (M-11) and the section 6.1 rule applied (2 or more of 5: fault and DL proposal; 1 of 5: watched).

| Round | Task | Participant | Completed | Problem (screen) | In their words | Severity |
|---|---|---|---|---|---|---|
| 1 | U1 | P1 to P5 | | | | |

### SG-A · Signal reads: AN-1 to AN-4, LG-1, TK-1

Per read: ID; record (analytics, the search log, ticket tags); period, and the period it is compared with; metric (M-07 to M-10); numerator and denominator, each defined as in section 1.2; value, and, for a share, its interval; the hypothesis it raises, in one sentence naming the screen or page identifier; the plan row or next cycle's test it goes to; rung (C1 for a single read that raises a hypothesis about the structure; C5 for a read that measures in use the behaviour the assumption is about, as AN-2 to AN-4 do, or a before-and-after read of a released change). Reads are presented at FO-06 (logs and tickets) or FO-01 (paths) (IA10, A.2).

| ID | Record | Period | Metric | Numerator | Denominator | Value (interval) | Hypothesis | Goes to | Rung |
|---|---|---|---|---|---|---|---|---|---|
| AN-1 | analytics; transactions | one quarter | M-08 | task starts | active employees × months | | | V-01 | C5 |
| AN-2 | analytics | one quarter | M-09 | short visits from A-1 or E-4, E-8 | sessions | | | V-02 | C5 |
| AN-3 | analytics | one quarter of joiners | M-10, two arms | Allow, per arm | shown, per arm | difference (interval) | | V-09 | C5 |
| AN-4 | analytics | one quarter | M-10 at first decline | allowed at first decline | employees with a first decline | | | V-16 | C5 |
| LG-1 | the For employees search log | the quarter after the fixes | M-07 per query | zero-result searches for "allowance", "gym" | all searches for each | | | V-13 | C1 |
| TK-1 | ticket tags (RV-05) | one quarter | tags per A- screen; tags on declines (E-8) | tickets tagged | all app tickets | | | V-11, V-15 | C1 |

## What later units take

**IA12** works without inputs. It takes the confidence ladder (C0 to C5) as the rung each assumption in its register is held at, and the plan (V-01 to V-17) and table A.2 as the test each assumption cites: every row of IA6 to IA10's assumption tables, with IA5's sign-in assumption and IA4's object nouns, now names either a plan row or a method section of this unit, so each register row can cite one test. It also takes section 7's rule that a test not run leaves its row in place, marked not run, with the assumption at its current rung.

**DD-IA2** writes the business case for IA work. It takes the metrics M-01 to M-11 as its measurement model, each with one definition and one interval method (section 1.2 and section 3.4); the plan's cost column as the cost of evidence; the rungs as the strength each claimed benefit rests on; and the sizing client's volumes (IA7) as the assumed load AN-1 to AN-4 will replace with measured figures.

## Perqo facts set by this unit

Every fact below is a course convention (Perqo, fictional), never evidence about the world. Each keeps every registered fact; none renames an IA1 to IA10 label, object, attribute or relationship. DL-016 is proposed, so no filed artefact changes at this unit's filing.

| Fact | Set in | Left free |
|---|---|---|
| Metrics M-01 to M-11, each with one definition and its reading | section 1.2 | none |
| The confidence ladder, rungs C0 to C5 | section 6.4 | none |
| Intervals are 95% adjusted-Wald; a mark is set before a test; verdicts pass, fail, undecided by the interval's ends | sections 3.4, 4.4 | none |
| Marks: task success 80% for a P1 task, 70% for P2 and P3; a cross-listing kept at a lower end of 15%, removed at an upper end below 15%; a home placement confirmed at a lower end of 50%; usability: a problem in 2 or more of 5 is a fault | sections 4.4, 6.1 | marks for Admin's and perqo.com's tests |
| The pilot: 12 employees of the example client, recruited through its HR, remote moderated sessions of 30 minutes, TT-1 then CS-1; median times 9 and 6 minutes; results as in Deliverable D, TT-A and CS-A | section 4.1; Deliverable D | the full run's results |
| T2's correct nodes extended to Recent activity (TN-04) after the pilot | section 4.1 | none |
| The example client's card offers are in Meals only | Deliverable B, B.3 | the number of offers |
| Tree node identifiers TN-00 to TN-30 (TN-31 in TT-1b) | Deliverable B, B.3 | none |
| Scripts and protocols TT-1 (version 2), TT-1b (if DL-016 is accepted), TT-0 (IA3's as-is tree), CS-1, FC-1, UT-1; card identifiers C-01 to C-12; task identifiers W, T1 to T10, F1 to F6, U1 to U3 | Deliverable B to D | none |
| Validation plan rows V-01 to V-17, with participants, rules and costs; reads AN-1 to AN-4, LG-1, TK-1; templates TT-A, CS-A, FC-A, UT-A, SG-A | Deliverable A, D | when each row runs |
| IA6's changes to the app's tabs trigger RV-11's before-and-after test, run as V-17 | Deliverable A | none |
| Recruitment: employees through clients' HR, arranged by customer success; at least two clients, all four categories open; at least 15 of 50 joined in the last three months; HR and finance staff screened out; TT-1 with CS-1, FC-1 and TT-0 each take different employees; no answer stored with a name | section 5; Deliverable A | incentives |
| Costs in staff days and participants' minutes, as in the plan | Deliverable A | money |
| DL-016, proposed: TT-1b with "Payment messages" (TN-31) under Card, against TT-1 on T7 | section 6.2; Deliverable A | its decision |
| Where each test named for IA11 outside the app IA goes (A.2, rows 1 to 25) | Deliverable A, A.2 | the tests' results |

## Sources

- Bailey, Robert W., Cari A. Wolfson, Janice Nall and Sanjay Koyani. "Performance-Based Usability Testing: Metrics That Have the Greatest Impact for Improving a System's Usability". In M. Kurosu, ed., *Human Centered Design, HCII 2009*, LNCS 5619. Springer, 2009, pp. 3 to 12. [link.springer.com, Bailey 2009](https://link.springer.com/content/pdf/10.1007/978-3-642-02806-9_1.pdf)
- Barker, Iain. "Measuring the Success of a Classification System". Boxes and Arrows, 24 April 2007 (practice). [boxesandarrows.com, classification](https://boxesandarrows.com/measuring-the-success-of-a-classification-system/)
- dscout. "Card sort questions". Help centre, undated (vendor documentation, checked 10 November 2026). [help.dscout.com, card sort](https://help.dscout.com/study-basics/question-types/card-sort-questions)
- Gaffney, Gerry. "Deal Them Again: Card Sorting Revisited" (review of Spencer 2009). *User Experience* 8, no. 3 (2009) (practice). [oldmagazine.uxpa.org, review](https://oldmagazine.uxpa.org/?p=5384)
- Katsanos, Christos, Nikolaos Tselios, Nikolaos Avouris, Stavros Demetriadis, Ioannis Stamelos and Lefteris Angelis. "Cross-study Reliability of the Open Card Sorting Method". *CHI '19 Extended Abstracts*, ACM, 2019. Preprint at [arxiv.org, 1903.08644](https://arxiv.org/pdf/1903.08644)
- Krug, Steve. *Don't Make Me Think, Revisited: A Common Sense Approach to Web Usability*. 3rd ed. New Riders, 2014. Excerpt at [peachpit.com, Krug](https://www.peachpit.com/articles/article.aspx?p=2209313) (practice).
- Lantz, Ethan, Jared W. Keeley, Michael C. Roberts, Maria Elena Medina-Mora, Pratap Sharan and Geoffrey M. Reed. "Card Sorting Data Collection Methodology: How Many Participants Is Most Efficient?" *Journal of Classification* 36, no. 3 (2019): 649 to 658. Record at [ideas.repec.org, Lantz 2019](https://ideas.repec.org/a/spr/jclass/v36y2019i3d10.1007_s00357-018-9292-8.html)
- Laubheimer, Page. "Tree Testing: Evaluate Menu Labels and Categories". Nielsen Norman Group, 6 August 2023. [nngroup.com, tree testing](https://nngroup.com/articles/tree-testing/)
- Laubheimer, Page. "Tree Testing Part 2: Interpreting the Results". Nielsen Norman Group, 19 January 2024. [nngroup.com, tree test results](https://nngroup.com/articles/interpreting-tree-test-results/)
- Lewis, James R., and Jeff Sauro. "When 100% Really Isn't 100%: Improving the Accuracy of Small-Sample Estimates of Completion Rates". *Journal of Usability Studies* 1, no. 3 (May 2006): 136 to 150. [uxpajournal.org, Lewis and Sauro 2006](https://uxpajournal.org/wp-content/uploads/sites/7/pdf/JUS_Lewis_May2006.pdf)
- Nielsen, Jakob. "Why You Only Need to Test with 5 Users". Nielsen Norman Group, 18 March 2000. [nngroup.com, 5 users](https://nngroup.com/articles/why-you-only-need-to-test-with-5-users/)
- Nielsen, Jakob. "Card Sorting: How Many Users to Test". Nielsen Norman Group, 18 July 2004. [nngroup.com, card sort users](https://www.nngroup.com/articles/card-sorting-how-many-users-to-test/)
- Nielsen, Jakob, and Thomas K. Landauer. "A Mathematical Model of the Finding of Usability Problems". *Proceedings of INTERCHI '93*, ACM, 1993 (not seen; cited as reported by Nielsen 2000; title and venue from knowledge).
- O'Brien, Dave. "How many participants?" *Tree Testing for Websites*, ch. 9, "Recruiting participants". Last updated 27 August 2024 (practice). [treetesting.atlassian.net, participants](https://treetesting.atlassian.net/wiki/spaces/TTFW/pages/1310747/How+many+participants)
- Rosenfeld, Louis. *Search Analytics for Your Site: Conversations with Your Customers*. Rosenfeld Media, 2011. Chs 3 to 10, contents and publisher's description. [rosenfeldmedia.com, Search Analytics](https://rosenfeldmedia.com/books/search-analytics)
- Sauro, Jeff. "What Is A Good Task-Completion Rate?" MeasuringU, 21 March 2011 (practice, a consultancy's data). [measuringu.com, task completion](https://measuringu.com/task-completion/)
- Sauro, Jeff. "10 Things to Know about Card Sorting". MeasuringU, 3 April 2012 (practice). [measuringu.com, card sorting](https://measuringu.com/card-sorting/)
- Sauro, Jeff, and James R. Lewis. *Quantifying the User Experience: Practical Statistics for User Research*. 2nd ed. Morgan Kaufmann, 2016. Chs 3, 4, 6 and 7, contents. [schweitzer-online.de, Sauro and Lewis](https://www.schweitzer-online.de/en/buch/Sauro/Quantifying-User-Experience/9780128023082/A35053706/)
- Spencer, Donna. *Card Sorting: Designing Usable Categories*. Rosenfeld Media, 2009. Chs 4, 6 to 10, contents. [rosenfeldmedia.com, Card Sorting](https://rosenfeldmedia.com/?p=187469)
- Tullis, Thomas, and Larry Wood. "How Many Users Are Enough for a Card-Sorting Study?" Presented at the UPA conference, 2004 (not seen; cited as reported by Nielsen 2004 and Sauro 2012).
- Cited through the filed units, for claims made there: Budiu, "Information Scent", NN/g, 2020 (IA3); Cardello, "Three Uses for Analytics in User-Experience Practice", NN/g, 2013 (IA9); Farrell, "Search-Log Analysis", NN/g, 2017 (IA3); Larson and Czerwinski, "Web Page Design: Implications of Memory, Structure and Scent for Information Retrieval", CHI 98, 1998 (IA3, IA4); Laubheimer, "Polyhierarchies Improve Findability for Ambiguous IA Categories", NN/g, 2018 (IA4); Mausser, "Site Search Analytics: A Conversation with Lou Rosenfeld", UXmatters, 2011 (IA3; practice); Tankala, "Card Sorting: Pushing Users Beyond Terminology Matches", NN/g, 2024 (IA3); Tankala, "Card Sorting vs. Tree Testing", NN/g, 2024 (IA9); Zaphiris, "Depth Vs Breadth in the Arrangement of Web Links", HFES 44th Annual Meeting, 2000 (IA4). Full references in IA3, IA4 and IA9, Sources.

## Unsure list

- Tullis and Wood 2004: the 168 participants, the correlations and the recommendation are as Nielsen 2004 and Sauro 2012 report them; the paper was not seen, and the authors' first names are from knowledge.
- Nielsen and Landauer 1993: the title and venue in Sources are from knowledge; the 31% is as Nielsen 2000 reports it. Gaffney's first name is from knowledge; the review's page gave "G.".
- Katsanos and others 2019: read in the authors' arXiv preprint; the published extended abstract's pages were not checked.
- Lantz and others 2019: read in the abstract on a bibliographic record; the stimuli and the studies the authors reanalysed were not seen, so how far their 10 to 15 carries to product content is not known.
- Krug 2014: the two quotations are from the publisher's excerpt; which chapter of the book they come from was not confirmed.
- The adjusted-Wald formula as written in section 3.4 (adding about two successes and four attempts) is from knowledge; Lewis and Sauro 2006 recommend the interval, and their text was read only in summary by the writer; the fresh check of 10 November 2026 read the paper's centre, (x + z²/2)/(n + z²), and its 1.645 for x = 0 or x = n, which section 3.4 now states.
- Laubheimer 2024: the definitions quoted were read through a summary of the page; the diagnostics in sections 4.2 and 6.2 are paraphrased from it, not quoted.
- Spencer 2009 and Rosenfeld 2011: only the chapter titles and the publishers' pages were seen; every claim about their content is through Gaffney's review (Spencer) or the publisher's description (Rosenfeld).
- Not checked: Tankala, "Card Sorting vs. Tree Testing" (rate-limited; cited only through IA9); Faulkner 2003 on usability sample sizes (the record returned no text; not cited); Wood and Wood 2008 in the Journal of Usability Studies (the page served another issue; not cited).
- Object: the Perqo app's tree as tested, TN-00 to TN-30, sections 4.1 to 4.4 and Deliverable B, B.3
- Fresh check 2026-11-10 (Fable 5.2; a Fable 5.1 fresh check is owed, P49): fix · 2 error, 13 should-fix, 10 minor; all applied as verified (finding 8 in part, the paper's 1.645 being for its point estimate); figures 2, 3 and 5 passed; figures 1, 4 and 6 fixed and checked again, each passing its third check; report `audits/ux/fresh-check-IA11.md`
