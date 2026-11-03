---
audit: fresh check
unit: IA6 · Level 2 · the client app
course: ux · IA · Information Architecture
model: Fable 5.1 (claude-fable-5-1, confirmed from the agent's transcript; live search; no Fable 5.1 fresh check is owed for IA6)
date: 2026-11-03
chat: own Fable 5.1 agent context, not shown the writing (P31), launched by the U-6 chat (Opus 5.5 as the orchestrating chat; the writer ran on Opus 5.5) in session https://claude.ai/code/session_01KMmgR1ttN1rJJAjAFevg4K
verdict: fix · 2 errors, 4 should-fix, 11 minor
---

The checker's final report, verbatim: its hand-back message, extracted by script from its transcript (the `SubagentHandback` call). The harness refused the checker's write of its own `out/report.md` ("this reply is the copy"), so the hand-back is the one copy. The maintainer's note follows the report.

# Fresh check · IA6 · Level 2 · the client app (ux · IA · Information Architecture)

Integrity: `diff K/unit.md K/unit-readonly.md` → identical (no output). `sha256sum K/unit.md` → cb37953130eb8789af09e7adf6451c01b13121756362a485447c59200f1b8a11, equal to the value in K/unit.sha256.
Model: running as Fable 5.1 (claude-fable-5-1); no Fable 5.1 fresh check is owed for IA6.
Packet read: K/unit.md (17,193 words with figures; 14,311 without), K/brief-IA6.txt, K/generator/data/ux/units_data.py (PRE, AIMS["IA6"], the IA6 entry's fifth field) and hub.py (GOAL_IA), K/sourcing-part1-and-part4.md, K/perqo-facts.md, K/figure-kinds.md, K/vault/IA1 to IA5. No audit report exists for this course, so step (6) was the pointer check only. `python3 K/render.py K/unit.md K/out/figs`: 8 figures, 0 errors. (The write of K/out/report.md was refused by the harness; this reply is the copy.)

## (1) Coverage, against every item the brief names
- Task analysis as the basis of an app's IA (tasks, frequency, sequence; the evidence for organising by task rather than by feature): covered (1.1 to 1.4; the limit of the evidence stated in 1.3).
- The app map as distinct from a sitemap (screens, states and modals, entry points): covered (section 2: six-row comparison, sources for each addition, the notation extension under IA2 §4).
- Mobile navigation patterns: tab bar, hub-and-spoke, hierarchical drill-down, NN/g evidence on each, hamburger on the evidence: covered (3.1 to 3.4); drill-down reported honestly as having no NN/g study of its own, grounded in IA4's depth evidence.
- Progressive disclosure, empty states, error states, permissions as IA decisions: covered (4.1 to 4.4; per-screen record in B.5).
- How a user flow becomes a wireflow and when each is the right artefact: covered (section 5: four-row table, five moves, the claim user flow).
- Consistency with the website's labels and the backoffice's objects (IA4's object map): covered (section 6: the labels table, the excluded words, addresses and deep links).
- Figures the brief names: task inventory ranked (fig 3), app map (fig 4), three wireflows (figs 6 to 8), navigation-pattern comparison (fig 1); plus the claim user flow (fig 2) and screen states (fig 5). Eight, within three to eight.
- Deliverable: task inventory with tasks, frequency, actor, surface (A.1, 17 rows); app map in the course notation (B.3); three wireflows: see a balance, spend a benefit, submit a reimbursement claim (C.1 to C.3). Present.
- To-be for IA3's as-is: every passed label kept (B.2 closing paragraph), every fix applied (B.2, 19 rows), departures stated with reasons (B.6). Covered.
- Aim / Takes / Gives: takes IA4's object map, IA3's as-is and checklist, IA2's wireflow entry; gives the app map and wireflows to IA8 and a tested assumption list to IA11. Covered.
- Thin: 3.3 (drill-down), by necessity of the evidence; not a fault. Missing: nothing.

## (2) Accuracy: every source opened by WebSearch then WebFetch of the returned URL
- Rosala, "Task Analysis", NN/g, 20 Sep 2020: PASS. Definition verbatim; two stages; the five gathering methods; order, hierarchy, frequency, cognitive demands, physical requirements; HTA with goal and scenario, tasks, subtasks, plans.
- Sears and Shneiderman, TOCHI 1(1), 1994, pp. 27–51, abstract at pure.psu.edu: PASS. "performance times were reduced by 17 to 58% depending on the site and menus"; "significantly faster than alphabetic menus" and preferred; two field studies, one controlled experiment.
- Nielsen, "Progressive Disclosure", NN/g, 3 Dec 2006: unverifiable (not checked). The one fetch was rate-limited; not retried under the web rule. Five quotations in 1.2, 3.3 and 4.1 rest on it.
- McGovern, "What Really Matters", Center Centre, 20 Jan 2016 (A List Apart, April 2015): FAIL as a stretch (should-fix below). The page: three Cisco tasks got the first 25 percent of the vote and 44 tasks the last; "We have done this process over 400 times and the same patterns emerge every single time." It does not say a small set takes "most of people's votes".
- Nielsen, "Paradox of the Active User", NN/g, 4 Oct 1998: PASS. Both quotations verbatim; cites Carroll and Rosson 1987 in Carroll ed., Interfacing Thought, MIT Press; IBM user studies of the early 1980s.
- Carroll and Rosson 1987: not opened; the unit cites it as reported by Nielsen and says so; details match Nielsen's page. PASS as reported.
- Hackos and Redish, User and Task Analysis for Interface Design: PASS (Wiley catalogue: February 1998, ISBN 978-0-471-17831-6).
- Budiu, "Basic Patterns for Mobile Navigation: A Primer", NN/g, 15 Nov 2015: PASS for all six quoted phrases, the 4–5-options-visible point, tab-bar persistence while scrolling, and the absence of any drill-down pattern or study. One clause attributed to the page, that a hub's home screen "spends its space on navigation", was not found by the fetch: unverifiable (minor below).
- Android Developers, "Layouts and navigation patterns": PASS. "Last updated 2026-10-22 UTC"; both quotations verbatim.
- Apple HIG, "Tab bars": PASS. The quoted sentence is the page description; undated; no body returned, as the unit says.
- Hoober, UXmatters, 18 Feb 2013: PASS. 1,333 observations; 780 touching the screen; 49% one-handed, 36% cradled, 15% two-handed.
- Pernice and Budiu, "Hamburger Menus and Hidden Navigation Hurt UX Metrics", NN/g, 26 Jun 2016: PASS. 179 participants, 6 live websites; desktop hidden 27%, visible 48%, combo 50%; mobile hidden 57%, combo 86%, visible-only not tested on phones; discoverability more than 20% lower; at least 39% slower on desktop, 15% on mobile (vs combo); 2.6 / 2.3 / 2.1 on 1 easy to 7 difficult; both quoted recommendations verbatim; websites, not apps.
- Laubheimer, "Wireflows", NN/g, 4 Dec 2016: PASS. All six quoted phrases verbatim.
- Android Developers, "About deep links": PASS. "Last updated 2026-10-28 UTC"; both quotations verbatim; the page says nothing about the app-absent case, as the unsure list says.
- Neusesser and Sunwall, "Error-Message Guidelines", NN/g, 14 May 2023: PASS. Both quotations verbatim; the proximity and no-blame guidelines present.
- Android Developers, "Request runtime permissions": PASS. "Last updated 2026-10-28 UTC"; three quotations verbatim (the second is the first sentence of its bullet).
- Apple, "Allowing apps and websites to link to your content": PASS. "link directly to content within your app" is in the page description; undated; no body.
- Resmini and Rosati 2011, Elsevier shop page: PASS. Part 2 Heuristics = chs 3 to 8; ch. 4 Place-making, 5 Consistency, 6 Resilience, 7 Reduction, 8 Correlation; 2011.
- Cited through the filed units (Prater 2016, Kaplan 2023, Krause 2021, Harley 2014, Whitenton 2013, Larson and Czerwinski 1998, Nielsen 2006 "Use Old Words", Nielsen 2009, Laubheimer 2023, Berners-Lee 1998, Hearst 2006, WCAG 3.2.4, Brown 2011, Cooper 2014, Card and others 2001, Budiu 2020, Zaphiris 2000): each pointer checked against the vault text; each says what the filed unit says (see (6)).

## (3) Figures: every number says whose it is
Hoober's counts and shares; Pernice and Budiu's percentages and ratings with n; Sears and Shneiderman's 17 to 58%; Android's three to five; Pernice and Budiu's four; every Perqo frequency "assumed" and "(Perqo, fictional)"; catalogue items by IA4's identifiers. One count in the unit's own text is wrong (3.5, "Five of them": error below).

## (4) Labels
Platform documentation on every Android and Apple citation; Hoober "a practitioner's observational study, practice"; McGovern "practice, a consultant's own data"; Prater "practice"; NN/g guidance labelled as guidance and kept apart from the measured study (Pernice and Budiu, with n and the websites caveat); Resmini and Rosati's unread chapter declared; IA3's as-is and every frequency labelled assumed; no Perqo fact used as evidence about the world.

## (5) Deliverable
Present in full: A.1 (17 tasks with object and call to action, actor, surface, frequency, comes-after, money at stake, priority, start screen), A.2 (10 calls to action ranked), B.1 (8 proposals decided), B.2 (19 fixes applied), B.3 (the map: 30 boxes, 23 screen IDs, each screen in words), B.4 (7 entries with addresses), B.5 (10 screens' states), B.6 (5 departures), C.1 to C.3 (three wireflows with failure paths), the IA8/IA11 hand-on (12 assumptions, each with a test and what changes), the facts table (19 rows). It follows from the evidence (each placement cites the section that argued it) and is usable alone. A.1's priorities match the rule in its preamble, checked row by row.

## (6) Errata and pointers
No errata owed. Pointers checked and found to say what the filed unit says: IA1 §5 (small, task-driven, reduction; spend with the card at merchants), §2.4 (the written mapping), Deliverable (policies as open categories and approval rules); IA2 §1.3, §1.6 (Kaplan's quotation; the three-artefact convention), §1.7, §3 fault 4, §4 "Keep the notation; extend the legend", §5.1 (conditional area as a bracketed note; crossbar as "(no way back)"), §5.2 (eight type tags; tones), §5.3 (the claim wireflow's screens and arrows, checked against IA2's JSON; the rule; only open categories; H- rows), decision table (sitemap F2/F3; user and task flow "as wireflows"); IA3 §1.1, §1.2 (Laubheimer "I want to…"; Harley), §2.1 (Cooper), §2.3, §4.2, §4.3 (Krause; WCAG 3.2.4), §5.2 (the five queries), §6.2 (a few times a month; Larson and Czerwinski), Deliverable (every verdict and "Fix (for IA6)" cell; "What IA6 keeps"; "What this hands on"), the as-is sitemap caption (Balance and Recent activity "sit on Home itself"); IA4 §1.2 (offers filed by the catalogue's category), §2.1 (Whitenton verbatim; the scrolling gap left unsourced), §4.1 (Prater; the figure's "Rank attributes and calls to action → see interaction design (IA6)"), §4.2 (the employee goal statement verbatim), §4.3 ("Views are not objects"; Home a view; a category a term), §5 (addressing; Berners-Lee), Deliverable A (O-04 to O-14 labels and attributes; R-11 0..1; R-12, R-14; A.3 rows; "Complexity and priority are left to IA6"; "What IA7 may do with it"; "What the map hands on"), Deliverable B (fidelity departure; R5; R6; BI-001 to BI-012 with categories and cross-listings, which the map reproduces exactly; "What IA5 and DD-IA3 take"); IA5 §1.3 ("allowance" on S-1.2), §2.2 (McGovern; verb labels fail A2), §5.1 (/product/benefits/cat-hea/health), §5.5 (S-6; join from the invitation; the Sign-in assumption to IA7), Deliverable A (every ID and title used: H-0.1, H-1.2.5 under both audiences, H-1.3, H-2, H-2.1, H-2.1.1 to H-2.1.3, H-2.2.1 at its new address, H-2.2.2, H-2.3.1, H-2.3.2, S-1.4.1 to S-1.4.4, S-6), Deliverable B, B.2 (the Benefits-tab note). One pointer wrong: "newest first in each (IA4, section 1.2)" is IA4 §1.1 (minor below).

## (7) Figures, in order
1. matrix, section 3.5. Every row label, cell and legend entry traced to 3.5's bullets ("on every screen", "on the hub", "one level at a time", "behind an icon"; "three to five", "as many as the hub holds", "any number for a drill-down, at the cost of levels", "a fairly large number"; "Visible links alone were not tested on mobile"; "an extra step per use"; "depth slows people"; "used in 57% of cases on mobile against 86% for combined"; "icons carry their labels under them"; "a hub's routes and a drill-down's rows are labelled"; "often has no text"; "Home can show the four balances, and so can a hub"; "only on the level they sit on"; "hides them until it is opened"; "one level of tabs", "one level of routes", "one more choice per level", "one list, if it is labelled"; "yes ... the tabs persist", "only from the hub", "only by going back", "only after opening the menu") and the decision line ("a tab bar of IA3's five tabs"; "Home as a partial hub, with routes to the top tasks"; "drill-down inside a tab, no deeper than two levels"; "no hidden menu"). Caption names section 3.5 and every source. Kind fits (patterns by criteria). FIX (minor): legend says tone 6 is "a fault against an IA3 criterion", but two tone-6 cells sit in non-criterion rows ("behind an icon"; the 57% cell). Replacement in the findings.
2. flow, section 5. Each step and note traced to the paragraph before it ("pays and keeps the receipt, outside the app"; "opens New claim from Claims, Home or a category screen"; "choosing a file if the camera is refused"; "sends them back to edit it"; "submits, with no way back"; "at or under the limit it is approved automatically, over the limit HR decides in Approvals"; "Approved, then Paid, or Rejected, with the reason to read"). Caption names section 5, Kaplan, IA2 §5.3, IA3 §2.3, tones. Kind fits (a sequence; the branch-free kind declared). PASS.
3. compare, Deliverable A. Twelve bars equal A.1's frequencies (8, 3, 2, 1.5, 1.5, 1, 0.5, 0.5, 0.3, 0.1, 0.1, once) and task names. Caption names A.1, the assumption, IA3 §6.2, Sears and Shneiderman, Nielsen. Kind fits. PASS.
4. sitemap, Deliverable B. Every screen, ID, note, "→ see" and type tag (29 tags, all from IA2's eight) traced to B.3, B.4 and B.5, except nine catalogue item names on A-2.1 to A-2.4 (gym membership, swimming pool entry, therapy session, coding course, book, train pass, bike repair, restaurant meal, groceries), which the text gives only as "BI-001 to BI-012" with a pointer to IA4; the names and categories match IA4's B.3 exactly. Caption names Deliverable B and every source. Kind fits. FIX (should-fix): add the names to B.3's text; replacement in the findings; no JSON change.
5. matrix, B.5. Every cell equals the B.5 table. Caption names B.5 and the sources. Kind fits. FIX (should-fix): legend meaning "the path stops until the employee acts" does not fit the tone-6 cells "[no connection]" and "[no category open]"; IA2 §5.2 defines tone 6 as "a stop, meaning a path that ends without success, or a fault found in a review". Replacement in the findings; the edited JSON renders.
6. wireflow, C.1. Screens and arrows traced to C.1 and B.5 ("When the Learning balance is used up, the same screen says so"; "Why can't I use money from another category? opens H-2.2.2"; "The tab bar takes the employee back to Home"); the two tone-1 screens are IA5's H-2.2.1 and H-2.2.2 under For employees, Balance. "Courses: coding course, cookery course" and "Books: book" are covered by the fig 4 fix. Caption names C.1 and sources. Kind fits. PASS.
7. wireflow, C.2. Screens and arrows traced to C.2 (Meals balance and what's covered; Card offers in Meals; the till; Purchase with merchant, amount, date, category, balance after; declined over the Meals balance or card Frozen; Card screen with Unfreeze card) and A.2 (title, discount, merchant, valid until). "Restaurants: restaurant meal", "Groceries: groceries" covered by the fig 4 fix. Caption names C.2, tone 2 for the till, sources. Kind fits. PASS.
8. wireflow, C.3. Keeps IA2 §5.3's four screens and four arrows (checked against IA2's JSON). Additions traced to 4.3 ("More than your Learning balance", Edit only), 4.4 (the prompt and what it says), A.2 (the Claim screen's attributes), C.3 (Done; the notification opens the Claim screen). Caption names C.3, IA2 §5.3, IA3's fixes, Garrett's crossbar, Laubheimer. Kind fits. FIX (minor): the modal's buttons "Allow" and "Not now" are in no text; replacement adds them to 4.4.

## Findings
- [error] [figure] 3.5; Current: `Five of them decide between patterns; the rest are properties of the labels and hold, or fail, whatever the pattern.` (grep -F -c: 1); Problem: IA3 handed nine criteria (A1 to A5, B1, B2, F1, F2); the paragraph sets aside A1, A2, A3, A5 and B2, which leaves four (A4, B1, F1, F2); Fix: `Four of them decide between patterns; the rest are properties of the labels and hold, or fail, whatever the pattern.`; Basis: IA3, "What this hands on" (K/vault/IA3, line 319) and the unit's own next sentences.
- [error] [figure] 3.5; Current: `The five that separate the patterns:` (1); Problem: six bullets follow, four of them IA3 criteria and two facts about the patterns (where the destinations are; room for them); Fix: `The four that separate the patterns, with the two facts about each pattern they are judged on:`; Basis: the unit's own list; IA3, "What this hands on".
- [should-fix] [accuracy] 1.2; Current: `reports that a small set of tasks takes most of people's votes in every such project he has run` (1); Problem: the source says three Cisco tasks got the first 25 percent of the vote against 44 for the last, and the same pattern in over 400 projects; it does not say a small set takes most of the vote; Fix: `reports that a few tasks take a share of the vote out of all proportion to their number, the same pattern in every one of the 400-plus such projects he has run`; Basis: McGovern, Center Centre, https://articles.centercentre.com/?p=877 ("We have done this process over 400 times and the same patterns emerge every single time"); IA5 §2.2 reports it the same way.
- [should-fix] [figure] Deliverable B, B.3 (figs 4, 6, 7); Current: `the example client's policy covers every item in the catalogue's sample, BI-001 to BI-012.` (1); Problem: nine catalogue item names drawn on A-2.1 to A-2.4 (and on the Learning and Meals screens of figs 6 and 7) appear nowhere in the unit's text; Fix: `the example client's policy covers every item in the catalogue's sample, BI-001 to BI-012: under Health, gym membership, yoga class and swimming pool entry (Fitness) and therapy session (Therapy); under Learning, coding course and cookery course (Courses) and book (Books); under Mobility, train pass (Public transport) and bike helmet and bike repair (Bike); under Meals, restaurant meal (Restaurants) and groceries (Groceries) (IA4, Deliverable B, B.3).`; Basis: IA4, Deliverable B, B.3 (K/vault/IA4, lines 433 to 444); sourcing Part 1, "A figure adds no fact".
- [should-fix] [figure] Deliverable B, B.5, fig 5 caption; Current: `tone 6 marks a state where the path stops until the employee acts` (1); Problem: the tone-6 cells "[no connection]" (Home, Claims, Purchases) and "[no category open]" stop until the connection returns or HR acts, not until the employee acts; Fix: `tone 6 marks a stop, a state in which the path ends without success until something changes (IA2, section 5.2)`; Basis: IA2 §5.2 (K/vault/IA2, line 206: "Tone 6: a stop, meaning a path that ends without success, or a fault found in a review").
- [should-fix] [figure] Deliverable B, B.5, fig 5 legend; Current: `"means": "the path stops until the employee acts"` (1); Problem: as above; Fix: `"means": "a stop: the path ends without success here"`; Basis: IA2 §5.2; the edited block renders (checked with viz.render).
- [minor] [figure] 3.5, fig 1 caption; Current: `tone 6 marks a fault against an IA3 criterion. Perqo is fictional."` (1); Problem: tone 6 is also on "behind an icon" and the 57% cell, in rows that are not criteria; Fix: `tone 6 marks a fault against an IA3 criterion, or the measured cost behind one. Perqo is fictional."`; Basis: the figure's own rows 1 and 3.
- [minor] [figure] 3.5, fig 1 legend; Current: `{"mark": "tone 6", "means": "a fault against an IA3 criterion", "tone": 6}` (1); Problem: as above; Fix: `{"mark": "tone 6", "means": "a fault against an IA3 criterion, or the measured cost behind one", "tone": 6}`; Basis: as above; the edited block renders (checked).
- [minor] [attribution] Deliverable B, B.1; Current: `Submitted, Approved, Rejected, Paid, newest first in each (IA4, section 1.2)` (1); Problem: IA4 set the newest-first ordering in section 1.1; Fix: `Submitted, Approved, Rejected, Paid, newest first in each (IA4, section 1.1)`; Basis: K/vault/IA4, line 38 (section 1.1 runs to line 53); K/perqo-facts.md, "Orderings (§1.1)".
- [minor] [attribution] Deliverable A, A.1 closing paragraph; Current: `which IA4's table gave only HR's approve and reject` (1); Problem: IA4's A.3 also gives the employee's claim -> submit; only viewing was absent; Fix: `for which IA4's table gave the employee only submit, and HR approve and reject`; Basis: IA4, Deliverable A, A.3 (K/vault/IA4, lines 284 to 285).
- [minor] [accuracy] 3.2; Current: `its cost is that it "incurs an extra step (back to the hub) for each use of the navigation", and the home screen spends its space on navigation (Budiu 2015; NN/g guidance).` (1); Problem: the fetched article confirms the extra-step cost; the home-screen-space cost was not found on the page yet is attributed to Budiu; Fix: `its cost is that it "incurs an extra step (back to the hub) for each use of the navigation" (Budiu 2015; NN/g guidance); and, on this unit's reading, a home screen that is a hub spends its space on navigation.`; Basis: Budiu, NN/g, https://www.nngroup.com/articles/mobile-navigation-patterns/ (fetched 3 Nov 2026).
- [minor] [figure] 4.4 (fig 8); Current: `and the prompt says what they are for (get told when a claim is approved, rejected or paid).` (1); Problem: the modal's buttons "Allow" and "Not now" are in fig 8 and in no text; Fix: `and the prompt says what they are for (get told when a claim is approved, rejected or paid), with Allow and Not now as its two answers.`; Basis: sourcing Part 1, "A figure adds no fact".
- [minor] [deliverable] Perqo facts, row 1; Current: `(A-0 Join and sign in; A-1 Home;` (1); Problem: the map has A-0.1 Join and A-0.2 Sign in, which the row omits while listing every other sub-screen; Fix: `(A-0 Join and sign in, A-0.1 Join, A-0.2 Sign in; A-1 Home;`; Basis: fig 4 and B.3.
- [minor] [attribution] 6.3; Current: `IA4 set Perqo's addressing rules: pages and filters address values by stable identifier, and a renamed or moved page keeps a redirect from its old address (IA4, section 5` (1); Problem: IA4's rule is narrower (catalogue pages and filters; a renamed or moved Help centre page); the generalisation is this unit's; Fix: `IA4 set Perqo's addressing rules for perqo.com: catalogue pages and filters address values by stable identifier, and a renamed or moved Help centre page keeps a redirect from its old address (IA4, section 5`; Basis: K/vault/IA4, line 207.
- [minor] [label] 6.2; Current: `"Pending" (a fourth word for Submitted: IA3, D2)` (1); Problem: Pending is a second word for the one state Submitted; "fourth" has no referent; Fix: `"Pending" (a second word for Submitted: IA3, D2)`; Basis: IA3, Deliverable, D2 (K/vault/IA3, line 309).
- [minor] [deliverable] Deliverable A, A.2 preamble; Current: `medium, one screen of input or one rule read;` (1); Problem: the freeze/unfreeze row is graded "medium (a modal to confirm)", which neither clause covers; Fix: `medium, one screen of input, one rule read or a confirmation step;`; Basis: the unit's own A.2 table.
- [minor] [style] 1.1; Current: `this unit cites it for its scope only.` (1); Problem: a citation carrying no claim is padding; Fix: `this unit draws no claim from it.`; Basis: sourcing Part 1 (a source is cited for what it says); the brief, "do not pad".

## Confirmed (checked and found right)
- Rosala 2020: definition verbatim; stages, methods, dimensions, HTA. https://www.nngroup.com/articles/task-analysis/
- Sears and Shneiderman 1994: "17 to 58%"; faster than alphabetic and preferred; TOCHI 1(1), 27–51. https://pure.psu.edu/en/publications/split-menus-effectively-using-selection-frequency-to-organize-men/
- Nielsen 1998: both quotations; Carroll and Rosson 1987, Interfacing Thought, MIT Press; IBM, early 1980s. https://www.nngroup.com/articles/paradox-of-the-active-user/
- Budiu 2015: six quoted phrases; 4–5 options may stay visible; tab bars visible while scrolling; no drill-down study; 15 Nov 2015. https://www.nngroup.com/articles/mobile-navigation-patterns/
- Android, "Layouts and navigation patterns": both quotations; updated 2026-10-22. https://developer.android.com/design/ui/mobile/guides/layout-and-content/layout-and-nav-patterns?hl=en
- Apple HIG, "Tab bars": description sentence; undated; no body. https://developer.apple.com/design/human-interface-guidelines/tab-bars
- Hoober 2013: 1,333; 780; 49/36/15%; 18 Feb 2013. https://www.uxmatters.com/mt/archives/2013/02/how-do-users-really-hold-mobile-devices.php?
- Pernice and Budiu 2016: 179 participants, 6 sites; 27/48/50%; 57/86%, visible-only untested on mobile; >20% discoverability drop; ≥39% and 15% slower; 2.6/2.3/2.1 on 1–7; both recommendations verbatim; websites. https://www.nngroup.com/articles/hamburger-menus/
- Laubheimer 2016: six quoted phrases; 4 Dec 2016. https://www.nngroup.com/articles/wireflows/
- Android, "About deep links": both quotations; updated 2026-10-28; nothing on the app-absent case. https://developer.android.com/training/app-links
- Neusesser and Sunwall 2023: both quotations; proximity and no-blame headings; 14 May 2023. https://www.nngroup.com/articles/error-message-guidelines/
- Android, "Request runtime permissions": three quotations; updated 2026-10-28. https://developer.android.com/training/permissions/requesting
- Apple, "Allowing apps and websites to link to your content": phrase in the description; undated; no body. https://developer.apple.com/documentation/xcode/allowing-apps-and-websites-to-link-to-your-content
- Resmini and Rosati 2011: chs 3–8 Heuristics; ch. 5 Consistency; 2011. https://shop.elsevier.com/books/pervasive-information-architecture/resmini/978-0-12-382094-5
- Hackos and Redish: Wiley, February 1998, ISBN 978-0-471-17831-6. https://gov.wiley.com/WileyCDA/WileyTitle/productCd-0471178314.html
- McGovern: A List Apart April 2015, republished 20 Jan 2016; "over 400 times" (the unit's paraphrase is the stretch above). https://articles.centercentre.com/?p=877
- Every vault pointer listed under (6) except "IA4, section 1.2" for newest-first.
- Perqo: every label in the 6.2 table matches IA4's O-04 to O-14 and IA5's inventory; the twelve catalogue items, categories and cross-listings match IA4 B.3 and R6; tabs, categories, narrower terms, claim states and rule match the register; the register's eight proposals are each taken by name in B.1; every "Fix (for IA6)" cell has a row in B.2; every label in "What IA6 keeps" is in B.2's kept list; the departures (total dropped; "one placing" read as one screen with routes; Claim screen added; over-balance state; Recent activity kept) are stated with reasons in B.6; the claim wireflow keeps IA2 §5.3's screens and arrows; the app's screens agree with IA4's objects and calls to action, the two new calls to action marked new and in the facts table; every new fact is in the facts table; "(Perqo, fictional)" on first use (first sentence).
- Unverifiable (not checked): Nielsen, "Progressive Disclosure", NN/g, 2006 (fetch rate-limited; not retried).

## Extra checks
- Counts re-run by script: 17 task rows; 2 calls to action marked new in A.1 and 2 in A.2 (checked); 10 A.2 rows; 8 proposals in B.1 against 8 in the register (checked); 19 rows in B.2 against IA3's 19 items (checked); 30 boxes in the map, 29 tagged, 23 screen IDs A-0 to A-5.2 (checked; the facts row omits A-0.1 and A-0.2, minor above); 7 entries E-1 to E-7 (checked); 10 screens in B.5 and 10 rows in fig 5 (checked); 12 bars in fig 3 equal to A.1's 12 employee tasks and values (checked); 12 IA11 assumptions; 19 facts rows; 8 figures (checked, within 3 to 8); 8 handed-on questions in the intro table (checked); "three note words" (checked); "four things" a sitemap leaves out (checked); "five moves" (checked); "three error states" (checked); "two kinds of permission" (checked); "IA2's eight" type tags (checked; the map's 29 tags all drawn from them); "from IA3's six to IA4's twelve" items (checked); "Five of them ... The five that separate" (WRONG: four, and six bullets; error above); 19 source entries plus the cited-through line, each cited in the text, nothing listed uncited (checked). The unit claims no word count.
- Public site: no personal fact, no private person, no real company's IA asserted; owners are roles; Perqo declared fictional. Passes.
- Length: about 6,400 words of prose in sections 1 to 6 (6,900 with the intro; 7,244 with tables); deliverables 4,908 with tables; the brief's guide is 2,000 to 6,000. No section pads beyond the Hackos and Redish sentence (minor above); 1.4's HTA example and section 2's comparison table earn their length; B.3's prose restatement of the map is what a reader without the figure needs.
- Memory, Projects, connectors, artifacts, agents: not used. Nothing outside K was opened except the web pages listed, each reached by WebSearch then WebFetch of the returned URL.

IA6 · verdict: fix · errors 2 (one wrong count, stated in two sentences) · should-fix 4 · minor 11.

## Maintainer's note (U-6 chat, 3 November 2026)

The report above was saved verbatim from the checker's hand-back (extracted by script from the `SubagentHandback` call) before any finding was applied, and committed (`bec97ea`). The checker ran on `claude-fable-5-1`, confirmed from its transcript, so no Fable 5.1 fresh check is owed for IA6. Each finding was verified against the unit, the filed units (`courses/ux/`) and, for an outside source, by the maintainer's own search and fetch under the web rule (a URL fetched only when a search in the same context returned it). Each was then applied as an exact replacement by script, its `Current` occurring once.

- **Applied as given (14):** the two errors in section 3.5 (the count is four: IA3 hands on nine criteria and the paragraph sets aside A1, A2, A3, A5 and B2; checked against IA3's "What this hands on"); the catalogue items named in B.3 (checked against IA4, Deliverable B, B.3: twelve items, their categories and narrower terms); figure 5's caption and legend for tone 6 (checked against IA2, section 5.2, where tone 6 is "a stop, meaning a path that ends without success, or a fault found in a review"); figure 1's caption and legend; IA4's A.3 for the claim (the employee's submit row, checked); the Budiu sentence (the maintainer's search did not return the article's URL, so it was not opened again; the finding only detaches an attribution the checker could not find on the page, and was applied as given); the notifications prompt's two answers; the facts row's A-0.1 and A-0.2; "a second word for Submitted"; the medium grade's confirmation step; the Hackos and Redish sentence (and, to match it, its Sources line and unsure-list line).
- **Applied with the source's own figure (1):** McGovern. Searched ("Gerry McGovern "What Really Matters: Focusing on Top Tasks" Center Centre") and fetched the returned https://articles.centercentre.com/?p=877: "Three tasks got the first 25 percent of the vote", with 6, 14 and 44 tasks for the other quarters (67 in all), and "We have done this process over 400 times and the same patterns emerge every single time". The finding holds; the replacement states the figure: "(in one vote, three of 67 tasks took the first quarter of it), and that the same pattern has emerged in every one of the more than 400 such projects he has run".
- **Applied as far as it holds (1):** 6.3, IA4's addressing rule. IA4, section 5 states it as "This unit's rule for Perqo": catalogue pages and filters by identifier, a renamed or moved Help centre page redirected. The narrowing holds; "for perqo.com" does not, since the filters include the app's Card offers list (IA4, section 5), so the replacement leaves it out.
- **Not applied (1):** "newest first in each (IA4, section 1.2)". IA4's section 1.2 table has the row "Claims in the app | Exact: by state (Submitted, Approved, Rejected, Paid), newest first in each" (IA4, line 63), so the pointer is right; section 1.1 has the plain ordering. The pointer stands.

**Figures.** The check failed figures 1, 4, 5 and 8. Each was fixed and re-checked by a new Opus 5.5 agent given only the unit's text with its figures taken out, the captions and the frames sheets `verify.py --shots <dir> --page read-ux-ia6` saved for it (phone, tablet and desktop, dark and light). The re-checkers' hand-backs follow, each saved verbatim by script from its `SubagentHandback` call. The harness refused every re-checker's `out/report.md` write, so each hand-back is its one copy.
- Figure 1 (matrix, navigation patterns): FIX at the check; fixed; FIX at re-check 1 (one should-fix, six minor, all applied: three tones, a "can show", three caption corrections); PASS at re-check 2, its third check (two minor, applied: the row "In the Perqo app" and tone 6's meaning named in the text, and the Perqo row's source in the caption). Re-check 1's phone note (the pinned label column took most of the frame) was met in the declaration: shorter row labels ("Destinations: where" and the rest, each named in a sentence of section 3.5), which narrowed the pinned column from 187 to 142 px.
- Figure 4 (sitemap, the app map): FIX at the check (the catalogue item names, added to B.3's text); FIX at re-check 1 (one error, "Active" not in the text, added from IA4's card attributes; New claim, Check and submit and Claim submitted drawn as siblings under Claims with "after" notes; two missing external routes, H-1.2.5 and H-2.3.2, drawn, and the text narrowed to default-state routes; four minor, applied); FIX at re-check 2 (two should-fix: the routes to H-2.3.1 and H-2.1.3 that section 6.2 names, drawn and added to B.3; "entry:" on every B.4 entry's landing screen; one minor, the Rejected claim's link named in B.3; all applied); PASS at re-check 3, its fourth check (two minor, applied: the root's children worded as drawn; the Purchase note's balance after).
- Figure 5 (matrix, screen states): FIX at the check (tone 6's meaning); FIX at re-check 1 (three should-fix and two minor: tone 6 named in the text with IA2, section 5.2; the used-up, receipt-missing and no-card cells made tone 6 so the figure keeps its own rule; the caption's IA2 citation now traces to the text); FIX at re-check 2 (two minor, applied: "[not allowed] how to allow notifications" in the figure and the B.5 table; "Blank cells: none, as in B.5's table"); PASS at re-check 3, its fourth check (three minor: two applied, the caption and B.5's lead sentence and the definition of "shown later"; one not applied, the screen IDs back in the row labels, because re-check 1's phone note was met by dropping them, which narrowed the pinned column from 210 to 133 px, and B.5's table directly above gives every row its ID).
- Figure 8 (wireflow, submit a claim): FIX at the check (the modal's two answers, added to section 4.4); PASS at re-check 1, its second check (one should-fix on the text, tone 6 never named, applied in the introduction; three minor applied: "Then Paid → see the claim's lifecycle (IA2, section 5.3)", the modal's "[either answer closes it]", and "later:" on the two notification arrows). Because its declaration changed, it was checked again: FIX at re-check 2 (one error: the modal's title "Allow notifications?" was in no text, retitled "Notifications prompt (modal)"; one minor: "screens from Deliverable B" in the caption; both applied); PASS at re-check 3, its fourth check (one minor, applied: "legible on a phone, scrolled sideways").
- Figures 2, 3, 6 and 7 passed the check.

**Renderer notes recorded and not applied in the unit** (P44 and the row's rule): on figure 8, the return arrow "tap Edit" from the over-balance state runs through the label "tap Continue [over the balance]", whose words stay readable. That is the renderer's placement of the labels of two opposite vertical edges between one pair of screens. No label or order the declaration can carry clears it: every arrangement of the two-a-row layout keeps New claim and its over-balance state in one column, and the text names both arrows. Also recorded: the sitemap's root children wrap into two rows by width; the sticky section bar clips the opening frame of a figure taller than the viewport; a phone frame opens at the drawing's start or at its data-x0; a matrix legend scrolls with the drawing on a phone.

**What else the check led to.** IA3's "What IA6 keeps" left out Recent activity, which IA3's own A2 row passes and IA6 keeps. IA3 was corrected by exact replacement, with a dated note pointing to IA6's B.1, B.2 and B.6, and IA6's B.6 now says when the list was corrected. The register's "Proposed for IA6, not facts yet" list is decided (IA6, B.1: all eight taken) and IA6's facts are appended to the register under "Set by IA6". Filing's `verify.py` found the course bibliography 8 px wider than a phone. The cause was IA6's link text "developer.android.com/training/permissions/requesting", which has no break opportunity; the link text became "developer.android.com, runtime permissions" in both places. Nothing else changed.

**Transcript checks (by script).** Writer (Opus 5.5, `claude-opus-5-5`): no `mcp__*`, Projects, Artifact, connector or Agent tool; 19 searches and 18 fetches, each URL returned verbatim by an earlier search, no redirect target fetched. One breach of the web rule: the writer fetched the NN/g empty-states URL a second time after a rate-limited first fetch. Nothing in the unit rests on that page; it is in the unsure list as not checked. Every path the writer read or wrote was in its packet (the script's four flags were SVG text inside its own commands). Its hand-back's unit is byte-identical to its `out/` file. Checker (`claude-fable-5-1`): no forbidden tool; 19 searches and 17 fetches, each returned by an earlier search in its context, none repeated; every path in its packet (one mistyped `K=` assignment to a path that does not exist, read nothing and was reassigned in the same command); its `out/report.md` write was refused, so its hand-back is the one copy. Re-checkers (eleven, `claude-opus-5-5`): no forbidden tool, no web, every path in its own packet. One ran `cd /tmp` as a working directory for crops, with every file it opened or wrote inside its packet.

## Figure 1 re-check 1 (Opus 5.5 agent, 3 November 2026; the second check of figure 1, matrix: navigation patterns; given the unit without its figures, the captions and the frames sheets, nothing of the earlier reports; verbatim hand-back; the harness refused its `out/` write, so the hand-back is the one copy)

Figure check · IA6 "Level 2 · the client app" · figure 1 (matrix) · second check

Figure 1 is a matrix in section 3.5, "Choosing Perqo's pattern by IA3's criteria" (unit line 148), after the six bullets of lines 141-146. The kind fits: four patterns set against criteria and facts is "items by sections", which is a matrix.

Grid as drawn (desktop/tablet frame). Columns are TAB BAR · HUB AND SPOKE · DRILL-DOWN · HAMBURGER MENU. [6] marks a tone 6 cell; every other cell is tone 3.
- Where the destinations are: on every screen · on the hub · one level at a time · behind an icon [6]
- Room for destinations: three to five · as many as the hub holds · any, at the cost of levels · a fairly large number
- Evidence on use: visible links: not tested on mobile · an extra step per use · depth slows people · used in 57% of cases on mobile, against 86% for combined [6]
- A4 · text with every icon: labels under icons · labelled routes · labelled rows · the icon often has no text [6]
- B1 · units shown where the decision is made: Home shows the four balances · the hub can show them · only on the level they sit on · hidden until opened [6]
- F1 · every choice unambiguous at every level: one level of tabs · one level of routes · one more choice per level [6] · one list, if labelled
- F2 · reachable from where the person is: yes: the tabs persist · only from the hub [6] · only by going back [6] · only after opening the menu [6]
- In the Perqo app: the five tabs · Home's routes to the top tasks · inside a tab, two levels at most · not used
- Legend: tone 3 "the Perqo app"; tone 6 "a fault against an IA3 criterion, or the measured cost behind one"
(I confirmed the tones by sampling pixels in the desktop light frame: tone 3 cells are (200,222,219), tone 6 cells are (224,218,196).)

(a) Findings

- should-fix | style | figure 1, row "Evidence on use", column DRILL-DOWN; Current: `depth slows people` drawn tone 3; Problem: the legend says tone 6 marks "the measured cost behind" a fault, and in the same row the hamburger's measured cost is tone 6. The drill-down's cost is measured ("Deeper structures slowed people in every study IA4 reviewed (Zaphiris 2000; Larson and Czerwinski 1998 ...)"), and it is the cost behind the drill-down's tone-6 F1 and F2 cells. Drawn in tone 3, it tells the reader the drill-down's evidence carries no cost. Fix: draw `depth slows people` in tone 6 (label unchanged). Basis: unit line 127 "Deeper structures slowed people in every study IA4 reviewed"; line 141 "one level at a time for a drill-down, where depth slows people (section 3.3)"; caption "tone 6 marks a fault against an IA3 criterion, or the measured cost behind one".
- minor | style | figure 1, row "B1 · units shown where the decision is made", column DRILL-DOWN; Current: `only on the level they sit on` drawn tone 3; Problem: by the text's own test, B1 needs the balances "on the first screen and on New claim". A drill-down that shows them "only on the level they sit on" fails that test, as the hamburger's "hidden until opened" (tone 6) does. In tone 3 the cell reads as passing B1. Fix: draw `only on the level they sit on` in tone 6. Basis: unit line 143 "the four category balances must be on the first screen and on New claim (IA3, B1). A tab bar's Home can show the four balances, and so can a hub; a drill-down shows them only on the level they sit on; a hidden menu hides them until it is opened."
- minor | style | figure 1, row "Where the destinations are", column HAMBURGER MENU; Current: `behind an icon` drawn tone 6; Problem: this row is not an IA3 criterion and the cell is not a measured cost, so by the legend it should not be tone 6. The hamburger's measured cost is the next row's tone-6 "used in 57% ..." cell, and its criterion faults are the A4, B1 and F2 cells. In the same row the drill-down's "one level at a time" stays tone 3. Fix: draw `behind an icon` in tone 3. If the author keeps it tone 6, widen the legend instead: `tone 6 · a fault against an IA3 criterion, its cause, or the measured cost behind one`. Basis: unit line 141 "behind an icon for a hamburger menu"; legend "a fault against an IA3 criterion, or the measured cost behind one".
- minor | label | figure 1, row "B1 · units shown where the decision is made", column TAB BAR; Current: `Home shows the four balances`; Problem: the text says the pattern "can show" them, and the hub cell beside it reads "the hub can show them". "shows" presents Perqo's design choice as a property of the pattern; the last row already records Perqo's choice. Fix: `Home can show the four balances`. Basis: unit line 143 "A tab bar's Home can show the four balances, and so can a hub".
- minor | accuracy | caption 1; Current: `depth from Larson and Czerwinski, CHI 98, and Nielsen, 'Progressive Disclosure', NN/g, 2006`; Problem: "CHI 98" does not occur in the unit (grep -F -c "CHI 98" = 0). The unit cites "Larson and Czerwinski 1998", and Zaphiris 2000 for the same depth claim. Fix: `depth from Larson and Czerwinski, 1998, and Zaphiris, 2000 (through IA4, section 2.1), and Nielsen, 'Progressive Disclosure', NN/g, 2006`. Basis: unit line 127 "(Zaphiris 2000; Larson and Czerwinski 1998; IA4, section 2.1)".
- minor | accuracy | caption 1; Current: `criteria A4, B1, F1, F2 from IA3, Deliverable.`; Problem: the A4 hamburger cell "the icon often has no text" rests on Harley 2014, which the caption does not name. Fix: `criteria A4, B1, F1, F2 from IA3, Deliverable; the hamburger's unlabelled icon from Harley, 'Icon Usability', NN/g, 2014.` Basis: unit line 142 "the hamburger's trigger is an icon that often has no text (Harley 2014)".
- minor | accuracy | caption 1; Current: `Budiu, 'Basic Patterns for Mobile Navigation', NN/g, 2015`; Problem: the title is cut; the unit and its Sources give it as "Basic Patterns for Mobile Navigation: A Primer". Fix: `Budiu, 'Basic Patterns for Mobile Navigation: A Primer', NN/g, 2015`. Basis: unit line 57 and Sources "Budiu, Raluca. "Basic Patterns for Mobile Navigation: A Primer". Nielsen Norman Group, 15 November 2015."

The unit's own text needs no change. Section 3.5 says "Four of them decide between patterns", and the figure has exactly four criterion rows (A4, B1, F1, F2).

(b) Confirmed

Kind and place
- matrix in section 3.5: line 148 "[Figure 1 (matrix) is drawn here; its caption is in captions.md.]", under "### 3.5 · Choosing Perqo's pattern by IA3's criteria".

Column headers
- TAB BAR: line 111 "### 3.1 · Tab bar"
- HUB AND SPOKE: line 119 "### 3.2 · Hub and spoke"
- DRILL-DOWN: line 125 "### 3.3 · Hierarchical drill-down"
- HAMBURGER MENU: line 131 "### 3.4 · The hamburger menu, on the evidence"

Row labels
- Where the destinations are / Evidence on use: line 141 "**Where the destinations are, and the evidence on use**"
- Room for destinations: line 146 "**Room for the destinations**"
- A4 · text with every icon: line 142 "**A4, text with every icon**"
- B1 · units shown where the decision is made: line 143 "**B1, the units the system acts on shown where the decision is made**"
- F1 · every choice unambiguous at every level: line 144 "**F1, every choice unambiguous at every level**"
- F2 · reachable from where the person is: line 145 "**F2, everything needed reachable from where the person is**"
- In the Perqo app: line 150 "The decision (Perqo, fictional): a tab bar of IA3's five tabs as the global routes ..."

Cells
- on every screen: line 141 "on every screen for a tab bar (Budiu 2015)"
- on the hub: line 141 "on the hub for a hub"
- one level at a time: line 141 "one level at a time for a drill-down"
- behind an icon: line 141 "behind an icon for a hamburger menu"
- three to five: line 146 "three to five for a bar (Android Developers 2026; Budiu 2015)"; line 113 "The navigation bar can hold three to five navigation destinations"
- as many as the hub holds: line 146 "as many as the hub holds"
- any, at the cost of levels: line 146 "any number for a drill-down, at the cost of levels"
- a fairly large number: line 146 "a fairly large number for a menu (Budiu 2015)"
- visible links: not tested on mobile: line 141 "Visible links alone were not tested on mobile (section 3.4)"; line 133 "(visible-only navigation was not tested on mobile)"
- an extra step per use: line 141 "with an extra step per use (Budiu 2015)". This is Budiu's guidance, not a measurement, so tone 3 fits the legend.
- depth slows people: line 141 "where depth slows people (section 3.3)"
- used in 57% of cases on mobile, against 86% for combined: line 141 "used in 57% of cases on mobile against 86% for combined navigation (Pernice and Budiu 2016)"; line 133 "on mobile, hidden navigation was used in 57% of the cases and combined navigation in 86%"
- labels under icons: line 142 "a tab bar's icons carry their labels under them"
- labelled routes / labelled rows: line 142 "a hub's routes and a drill-down's rows are labelled"
- the icon often has no text: line 142 "the hamburger's trigger is an icon that often has no text (Harley 2014)"
- Home shows the four balances (see finding) / the hub can show them: line 143 "A tab bar's Home can show the four balances, and so can a hub"
- only on the level they sit on: line 143 "a drill-down shows them only on the level they sit on"
- hidden until opened: line 143 "a hidden menu hides them until it is opened"
- one level of tabs / one level of routes: line 144 "a tab bar is one level of tabs and a hub one level of routes"
- one more choice per level: line 144 "a drill-down adds one more choice per level"
- one list, if labelled: line 144 "a menu is one list, if it is labelled"
- yes: the tabs persist: line 145 "yes for a tab bar, since the tabs persist"
- only from the hub: line 145 "only from the hub for a hub"
- only by going back: line 145 "only by going back for a drill-down"
- only after opening the menu: line 145 "only after opening the menu for a hamburger"
- the five tabs: line 150 "a tab bar of IA3's five tabs as the global routes"
- Home's routes to the top tasks: line 150 "Home as a partial hub, with routes to the top tasks"; line 123 "Home carries routes to the top tasks"
- inside a tab, two levels at most: line 150 "drill-down inside a tab, no deeper than two levels"; line 129 "inside a tab only, and at most two levels below the tab"
- not used: line 150 "no hidden menu"; line 135 "The Perqo app has no hamburger menu."

Legend and notation
- tone 3, the Perqo app: line 12 "on a figure of one surface every box takes that surface's tone, so every app box is tone 3"
- The tone 6 legend text matches the caption: "tone 6 marks a fault against an IA3 criterion, or the measured cost behind one". The figure applies it as the caption says, except for the three tone findings above.

Caption elements
- says what it shows: "four mobile navigation patterns against the evidence and the IA3 criteria that separate them, for the Perqo app"
- names the section: "(section 3.5)"
- Budiu 2015: line 57 "("Basic Patterns for Mobile Navigation: A Primer", Nielsen Norman Group, 15 November 2015 ...)" (the caption cuts the title: see finding)
- Pernice and Budiu 2016, 179 participants, websites: line 117 "("Hamburger Menus and Hidden Navigation Hurt UX Metrics", Nielsen Norman Group, 26 June 2016 ...)"; line 133 "In a study of 179 participants on six live sites"; "The study was of websites"
- Android Developers 2026, platform documentation: line 113 "(Android Developers, "Layouts and navigation patterns", page updated 22 October 2026, ...; platform documentation)"
- Larson and Czerwinski: line 127 "Larson and Czerwinski 1998" ("CHI 98" is not in the unit: see finding)
- Nielsen 2006: line 46 "("Progressive Disclosure", Nielsen Norman Group, 3 December 2006"; line 127 "In practice, designs that go beyond 2 disclosure levels typically have low usability" (Nielsen 2006)
- criteria A4, B1, F1, F2 from IA3, Deliverable: line 139 "Four of them decide between patterns"; line 328 "(IA3, Deliverable, "The checklist applied to the as-is Perqo app")"
- Perqo is fictional: line 12 "the Perqo app (Perqo, fictional)"

Legibility as the reader sees it
- Desktop, light and dark: frame 1 of 1; the whole figure fits. Every label is whole, nothing overlaps, and the tones are distinct in both themes.
- Tablet, light and dark: frame 1 of 1; the whole figure fits. Every label is whole and nothing overlaps.
- Phone, light and dark: four frames, at 0, 164, 328 and 372 of 372 px.
  - The row labels stay pinned at the left.
  - TAB BAR, HUB AND SPOKE and DRILL-DOWN each come wholly into view at some scroll position. HAMBURGER MENU never does (renderer note 1).
  - The hint "scroll sideways for the whole figure" is shown.
  - Every word of every cell and of the legend can be scrolled to. A phone reader can follow the figure, but has to read the hamburger column in two halves.

(c) Renderer notes
1. Phone, both themes: the hamburger column never fits whole in the window.
   - The pinned row-label column takes about 56% of the 390 px width, which leaves about 149 css px for cells. The hamburger column is about 183 css px wide.
   - Frame 3 (328 px) cuts the right side: "used in 57% of cas / on mobile, agains / 86% for combined", "a fairly large numb", "hidden until opene".
   - Frame 4 (372 px, the end of the scroll) cuts the left side: "ehind an icon", "irly large number", "6% for combined", "dden until opened".
   - Every word can be scrolled to, so this comes from the layout.
   - The author has two possible levers, neither confirmable from these shots: keep every hamburger line to about 18 characters (the width of "labels under icons", the tab bar column's widest line, which fits the window whole), or shorten the row labels in case the pinned column sizes to its content. Re-shoot to check before treating either as a fix. Not counted.
2. Phone, both themes: the legend line runs past the pinned column. "tone 6 · a fault against an IA3 criterion, or the measured cost behind one" is cut in frames 1 and 2 and split under the fade in frame 3 ("beh d one"). It reads whole across frames 3 and 4. Not counted.
3. Opening frames: on phone (both themes) the figure opens at the drawing's start, showing only the TAB BAR column and the row labels, and the sticky section bar hides the column header row and the first row; the first visible row is "Room for destinations". On desktop the sticky section bar hides the header row (TAB BAR ... HAMBURGER MENU); the frames sheet shows it. The tablet opening frame shows the whole figure. Not counted.

(d) Figure 1: FIX · error 0 · should-fix 1 · minor 6

(The harness would not let me save this report to D/out/report.md. This reply is the only copy. I made a temporary crop folder at D/out/crops for zoomed reads and deleted it.)

## Figure 4 re-check 1 (Opus 5.5 agent, 3 November 2026; the second check of figure 4, sitemap: the app map; given the unit without its figures, the captions and the frames sheets, nothing of the earlier reports; verbatim hand-back; the harness refused its `out/` write, so the hand-back is the one copy)

IA6 figure 4 (sitemap), second fresh check. Sits in Deliverable B, B.3 "The map" (unit line 358). Kind: sitemap. Data shape: a hierarchy of screens. Kind fits.

(a) Findings

1. [error | label] Figure 4, box "Card details" (A-4.1). Current: `A-4.1 · last four digits; Active or Frozen`. Problem: the card state "Active" is not in the unit's text. The only "Active" in the file is in "paradox of the active user" (lines 54, 495, 501). The text gives this screen's attributes as `last four digits, status` (A.2 table, line 298) and the state word only as "Frozen" (`Frozen card shows its state`, line 189). Fix: change the note to `A-4.1 · last four digits, status`. Another option, if a state word is wanted: `A-4.1 · last four digits; status (Frozen or not)`. Basis: line 298 `| card | -> view card details | employee | A-4.1 | low | P3 | last four digits, status | none |`. Seen on every frame at every width and theme.

2. [should-fix | accuracy] Figure 4, Claims column. Current (figure): "Check and submit" (A-3.2) is drawn as a child of "New claim" (A-3.1), and "Claim submitted" (A-3.3) as a child of "Check and submit". That puts A-3.3 three levels below the Claims tab. Problem: the identifiers make A-3.1, A-3.2 and A-3.3 siblings under A-3. Elsewhere the map nests by identifier (A-4.2.1 under A-4.2). The text says these are three screens under Claims and that drill-down goes at most two levels below a tab. Text: `New claim, Check and submit and Claim submitted are three screens under Claims` (line 129, occurs once) and `at most two levels below the tab` (line 129, once). Fix: draw all five as direct children of Claims (A-3), in this order: New claim, Check and submit, Claim submitted, Claim, Help with claims. Give the sequence in the notes, as the reader would see it: "Check and submit" with `A-3.2 · after A-3.1 · [over the balance] Edit only`; "Claim submitted" with `A-3.3 · after A-3.2 · [first claim] modal: the notifications prompt`. If the author wants to keep the nesting to show the staged sequence, add to the caption: `Check and submit and Claim submitted are drawn under New claim to show the staged sequence; all three are screens under Claims (section 3.3).` Basis: line 129; line 467 (`A-3 Claims, A-3.1 New claim, A-3.2 Check and submit, A-3.3 Claim submitted, A-3.4 Claim`).

3. [should-fix | figure] Figure 4, external routes. Current (text, line 356): `Every route that leaves the app is tagged` (occurs once). Problem: two routes that leave the app and are always present on their screens are not drawn:
   - the Card tab's link to H-2.3.2: `A link Where you can pay with the Perqo card (H-2.3.2) sits on Card.` (line 366, once)
   - New claim's link to H-1.2.5: `with the group's limit and a link to How approval rules work` (line 365, once)
   The figure draws only three external routes: Your balance explained, Help with claims, Help. Fix (figure): add a child of "Card" (A-4) tagged EXTERNAL, label `Where you can pay with the Perqo card`, note `→ see H-2.3.2`. Add a child of "New claim" (A-3.1) tagged EXTERNAL, label `How approval rules work`, note `→ see H-1.2.5`. With fix 2 applied, New claim is otherwise a leaf, so this child is its only one. The external links that appear only in a state are H-2.1.1 (Claims empty), H-2.1.2 (Claim when Rejected) and H-2.2.2 (category used up). Either add them as EXTERNAL boxes with their [condition] in the note, or narrow the text. Fix (text, if the author leaves those three out): `Every route that leaves the app is tagged` → `Every route that leaves the app from a screen's default state is tagged` (the routes that appear only in a state are in B.5). Basis: lines 356, 365, 366, 395, 393/422 (H-2.2.2 on the used-up category screen).

4. [minor | label] Figure 4, box "New claim" under Home. Current: `→ see A-3.1`. Problem: this is the New claim button on Home (`the New claim button`, line 363, once), so it is an element that sits on Home. The unit's notation marks such elements `on Home` (line 107), and the sibling boxes Balance and Recent activity carry that note. This one does not. Fix: note `on Home: a button → see A-3.1`. Basis: line 107 (`"on Home" for an element that sits on its parent screen`), line 363.

5. [minor | label] Figure 4, box "Claim submitted" (A-3.3). Current: `[first claim] modal: allow notifications`. Problem: "allow notifications" is a paraphrase. The text calls the layer the notifications prompt (`Done opens the notifications prompt, a modal`, line 434, once; B.5 line 398 `[first claim] the notifications prompt`). Fix: `A-3.3 · [first claim] modal: the notifications prompt`. Basis: lines 398, 434.

6. [minor | style] Caption. Current: `words added under IA2's rule 'Keep the notation; extend the legend' (section 2)`. Problem: a reader can take "(section 2)" as IA2's section 2. The unit places the rule in IA2, section 4 (`under IA2's rule "Keep the notation; extend the legend" (IA2, section 4)`, line 107, once). The words are added in this unit's section 2. Fix: `words added in section 2 under IA2's rule 'Keep the notation; extend the legend' (IA2, section 4)`. Basis: line 107.

7. [minor | style] Caption and notation. Current (figure): "→ see" is used for internal pointers too: Balance `→ see A-2.1 to A-2.4`, and New claim under Home `→ see A-3.1`. Problem: the text and the caption name "→ see" only for routes that leave the app (`Routes that leave the app are tagged external with '→ see' their Help centre page`). The internal use is not in the legend the unit extends (line 107 lists "modal", "entry:", "on Home" and the identifiers). Fix (caption): after `...their Help centre page.` add `'→ see' with a screen ID points to a screen drawn elsewhere on the map.` Basis: line 107; line 356.

(b) Confirmed (each figure element traced to the text)

- Kind sitemap for a hierarchy of screens, in B.3: line 356 `The map in the notation (Perqo, fictional): square-cornered boxes with IA2's type tags, every box tone 3, the app.`
- Root "Perqo app · tab bar: the global routes; entries in B.4": line 356 `The root is the surface, since the tab bar is not a screen; its children are the sign-in screens and the five tabs.`; line 102 `| Global routes | header and footer | the tab bar...`; B.4 is the entries table (lines 371-385).
- SECTION Join and sign in, A-0 · [signed out]: line 362 `Sign in (A-0.2) is for an employee who has joined and is signed out.`; line 377 `Sign in, A-0.2, when signed out`.
- FORM Join, A-0.1 · entry: HR's invitation: line 378 `| E-2 | HR's invitation | ... | Join, A-0.1;`.
- FORM Sign in, A-0.2: line 467.
- HOME Home, A-1 · entry: opening the app: line 377 `| E-1 | Opening the app | the phone | Home, A-1;`.
- DETAIL Balance, on Home: each open category and what remains → see A-2.1 to A-2.4: line 363 `Balance: each open category with what remains, each opening its category screen`.
- EXTERNAL Your balance explained → see H-2.2.1: line 321 `the link opens H-2.2.1`.
- INDEX Recent activity, on Home: purchases and claims, newest first; Submitted: line 363 `Recent activity, the latest purchases and claims mixed, newest first, with claim statuses in the Claims words (Submitted, never Pending)`.
- FORM New claim → see A-3.1 (under Home): line 320 `a button with the text New claim on Home, on Claims and on each category screen, all opening A-3.1`.
- INDEX Benefits, A-2 · the four categories only: line 339 `remove Perks; Benefits holds the four categories only`.
- DETAIL Health, A-2.1 · Fitness: gym membership, yoga class, swimming pool entry; Therapy: therapy session: line 356 `under Health, gym membership, yoga class and swimming pool entry (Fitness) and therapy session (Therapy)`.
- Health · also: bike helmet, covered under Mobility (assumed): line 341 `bike helmet in Health, each "covered under" its home, marked assumed (IA4, R6)`.
- DETAIL Learning, A-2.2 · Courses: coding course, cookery course; Books: book: line 356 `under Learning, coding course and cookery course (Courses) and book (Books)`.
- Learning · also: yoga class, covered under Health (assumed): line 341 `yoga class in Learning`; line 364 `("Yoga class: covered under Health")`.
- DETAIL Mobility, A-2.3 · Public transport: train pass; Bike: bike helmet, bike repair: line 356 `under Mobility, train pass (Public transport) and bike helmet and bike repair (Bike)`.
- DETAIL Meals, A-2.4 · Restaurants: restaurant meal; Groceries: groceries: line 356 `under Meals, restaurant meal (Restaurants) and groceries (Groceries)`.
- Meals · also: cookery course, covered under Learning (assumed): line 341 `cookery course in Meals`.
- Twelve items, BI-001 to BI-012, each once in its home category: line 471 `The example client's policy covers all twelve sample catalogue items`.
- Cross-listings on A-2.1, A-2.2, A-2.4: line 452 `| The far members are found by their cross-listings | A-2.1, A-2.2, A-2.4 |`.
- INDEX Claims, A-3 · Submitted, Approved, Rejected, Paid; newest first: line 319 `Submitted, Approved, Rejected, Paid, newest first in each`.
- FORM New claim, A-3.1 · Claims over the limit need HR approval: line 323 `on New claim, with a link to How approval rules work`; line 365.
- FORM Check and submit, A-3.2 · [over the balance] Edit only: line 397 `| Check and submit, A-3.2 | none | [over the balance] Edit only |`.
- DETAIL Claim submitted, A-3.3 · [first claim] modal: line 398 `| Claim submitted, A-3.3 | none | none | [first claim] the notifications prompt |`; line 434 `Done opens the notifications prompt, a modal`.
- DETAIL Claim, A-3.4 · entry: a notification · [Rejected] the reason: line 380 `| E-4 | A notification about a claim | ... | Claim, A-3.4 |`; line 365 `when Rejected, the reason`.
- EXTERNAL Help with claims → see H-2.1: line 235 `Help with claims (H-2.1)`; line 365 `New claim; Help with claims`.
- SECTION Card, A-4 · [no card issued] not issued yet: line 399 `| Card, A-4 | [no card issued] not issued yet; claims still work |`.
- DETAIL Card details, A-4.1 · last four digits: line 298 (see finding 1 for "Active").
- INDEX Purchases, A-4.2 · newest first: line 366 `Purchases (A-4.2, newest first)`.
- DETAIL Purchase, A-4.2.1 · merchant, amount, date, category: line 366 `A-4.2.1: merchant, amount, date, category and the category's balance after` (the figure leaves out the last attribute; a subset, not an error).
- INDEX Card offers, A-4.3 · filter by category: line 366 `Card offers (A-4.3: ... filterable by category`.
- FORM Freeze card, A-4.4 · modal: confirm; Unfreeze card when Frozen: line 366 `Freeze card (A-4.4: a modal asks to confirm; on a Frozen card the action reads Unfreeze card)`.
- SECTION Account, A-5: line 324 `Account holds Profile, Notifications and Help`.
- DETAIL Profile, A-5.1: line 467.
- INDEX Notifications, A-5.2 · each opens its claim: line 367 `Notifications (each about one claim and opening it`.
- EXTERNAL Help → see H-2 For employees: line 322 `Account's Help opens H-2, perqo.com/help/employees`; line 367 `Help (For employees)`.
- No Documents, Perks or Discover box: line 244; line 324.
- Screen set and IDs A-0 to A-5 match the facts table: line 467.
- Caption, what it shows: "App map: the Perqo app as designed (to-be), F2 with an identifier on every screen, page types tagged": line 307 `app map of the Perqo app, the to-be for IA3's as-is navigation, at fidelity F2 with F3's identifiers on every screen`.
- Caption, decision: "which screens exist, under which tab, in which states, with which modals and ways in": line 307 `decision: what screens the app has, under which tab, in which states, with which modals, and by which ways in`.
- Caption, section named: "(Deliverable B)". The figure sits in B.3, line 358.
- Caption "Every box is tone 3, the app": line 356; line 12.
- Caption, note words (screen ID, [condition], 'modal', 'entry:', 'on Home'): line 107; line 356.
- Caption, external with '→ see': line 356.
- Caption, cross-listings assumed, IA4 rule R6: line 341.
- Caption, sources: tabs from IA1 (line 63 `(IA1, section 5)`); New claim, Check and submit from IA2 section 5.3 (line 48); Claim submitted IA2's (line 352); fixes from IA3, Deliverable (line 328); objects and catalogue items from IA4 (line 356 `(IA4, Deliverable B, B.3)`; line 228); Help centre pages from IA5, Deliverable A (line 321).
- Notation: every box is the same teal fill with a teal border in both themes (tone 3 throughout). Corners are square. Each box carries a type tag in caps above its label: SECTION, HOME, INDEX, DETAIL, FORM, EXTERNAL. Consistent with line 356.

(c) Renderer notes

- Desktop: in the opening frame (light and dark) the sticky section bar covers part of the figure (Learning and Recent activity are hidden behind it). In the frame sheet the whole figure fits in one frame, and every label is whole. Renderer behaviour, not a FIX.
- The root's six children wrap into two rows by width: Join and sign in, Home, Benefits; then Claims, Card, Account. A row is not a level; all six hang from the one root line. Renderer layout. Not a FIX, because no per_row change is needed for correctness.
- Tablet, light and dark: the whole figure fits in one frame. Labels are whole and nothing overlaps.
- Phone (390 px), light and dark: the figure scrolls sideways, three frames, at 58, 222 and 372 of 372 px, and opens at 58. A "scroll sideways for the whole figure" hint shows. Every box is whole in at least one frame: Join and sign in, Join, Sign in, Claims and its column in frame 1; the root, Home and its column, and Card and its column in frame 2; Benefits and the four categories, and Account and its column in frame 3. Text at the scroll edges fades or is cut within a frame. That is renderer behaviour; the reader can scroll to each such box. There is a large empty area under Join and sign in, because the Benefits column is tall. Renderer layout.
- A phone reader can follow it: each tab's column reads top to bottom inside one frame. Seeing one column beside another needs a sideways scroll. No change the author can make is required, though fix 2 above would shorten the Claims column's indent.
- Dark theme: borders and text keep contrast at every width. The connector lines are dim grey but visible.

(d) Figure 4: FIX. 1 error, 2 should-fix, 4 minor.

(The harness refused the write to D/out/report.md; this reply is the only copy. Working crops of the phone frame sheets were saved in /tmp/claude-0/-home-claude/014ca185-e160-5e84-b94e-99ea385f9b58/scratchpad/u6/rc1/fc4/out/crops/.)

## Figure 5 re-check 1 (Opus 5.5 agent, 3 November 2026; the second check of figure 5, matrix: screen states; given the unit without its figures, the captions and the frames sheets, nothing of the earlier reports; verbatim hand-back; the harness refused its `out/` write, so the hand-back is the one copy)

Figure 5 has 3 should-fix and 2 minor findings, no errors. Every cell matches the B.5 table word for word. The problems are in the colouring: two cells are tone 6 or tone 3 when the rule in the caption says otherwise, and one sentence in the unit text contradicts the figure. The packet does not include the figure's JSON, so I give the fixes as the reader would see them: the cell, its column and its tone.

**Figure 5 · matrix · Deliverable B, section B.5 "Screen states"** (marker at line 404, under the B.5 table, lines 391–402)

**Where things stand**
- **Kind:** a matrix fits. The data is items (10 screens) set out by sections (4 state types).
- **Labels:** every row label, column header and cell text appears in the unit's text (traced below).
- **Caption:** it says what the figure shows, names the section ("Deliverable B, B.5") and gives the sources. All its parts trace to the text.
- **Course notation:** square-bracket conditions are used throughout. The app's cells are tone 3, stops are tone 6, and grey means no such state. That is the notation the caption describes. The problem is that two cells are coloured against the caption's own rule for tone 6.

## (a) Findings

- **should-fix · style · Figure 5, row "Category screen, A-2.1 to A-2.4", column Empty**
  - Current: `[balance used up] no balance left this period; Why can't I use money from another category?` is drawn in tone 3.
  - Problem: the caption says tone 6 marks "a stop, a state in which the path ends without success until something changes". With the balance used up, nothing more can be spent or claimed in that category until the period renews. That is a stop by the caption's own definition. Figure 6's caption also names "the used-up state of a category screen" and "tone 6 a state where the path stops". So figure 5 colours the same state differently from figure 6.
  - Fix: set that cell's tone to 6 (tone field 3 → 6). The text stays the same.
  - Basis: line 422, "When the Learning balance is used up, the same screen says so, and its link Why can't I use money from another category? opens H-2.2.2". Figure 6's caption (captions.md). Desktop, tablet and phone frames, both themes: the cell is tone 3.

- **should-fix · accuracy · unit text, introduction (line 12)**
  - Current: `on a figure of one surface every box takes that surface's tone, so every app box is tone 3.`
  - Problem: figure 5 shows one surface, the app, but has five tone 6 boxes. Figures 1, 6 and 8 also use tone 6. The text states a rule the figures break, and the text never says what tone 6 marks; only the captions do. So the legend label "a stop: the path ends without success here" does not trace to the text.
  - Fix: `on a figure of one surface every box takes that surface's tone, so every app box is tone 3, except where tone 6 marks a fault or a stop, a state in which the path ends without success until something changes, as each figure's caption says.`
  - Basis: line 12 (grep -F -c = 1). The figure 5 frames, where tone 6 is on Home Empty and Error, Claims Error, Check and submit Error and Purchases Error.

- **should-fix · label · caption, figure 5**
  - Current: `tone 6 marks a stop, a state in which the path ends without success until something changes (IA2, section 5.2)`
  - Problem: the unit cites IA2 section 5.2 only for the screen notation and placeholders (lines 209 and 418). Nothing in the unit's text says IA2 section 5.2 defines tone 6 as a stop, so the citation does not trace. (Whether IA2's own text supports it is outside this packet.)
  - Fix: `tone 6 marks a stop, a state in which the path ends without success until something changes (this unit's use; IA2, section 5.2, for the screen notation)`. If IA2 section 5.2 does define the stop tone, leave the caption as it is and add that definition to the unit's text with the citation.
  - Basis: line 418, "Each wireflow uses IA2's screen notation: ... (IA2, section 5.2; Laubheimer 2016)". Line 209.

- **minor · style · Figure 5, row "New claim, A-3.1", column Error**
  - Current: `[receipt missing] by the Receipt field; input kept` is drawn in tone 3, while `[over the balance] Edit only` (Check and submit, Error) is tone 6.
  - Problem: both are input errors with the input kept and a remedy on the screen. In both, Continue or Submit is blocked until the employee changes something. One is coloured as a stop and the other is not, and nothing in the text says why.
  - Fix: either set the [receipt missing] cell to tone 6, or narrow the caption's definition to `tone 6 marks a stop, a state in which the path ends without success until something outside the employee's own input changes`. If you take the second route, also set [over the balance] to tone 3, which would contradict figure 8. So set [receipt missing] to tone 6.
  - Basis: lines 174 and 176: "with Edit as the only route forward, and the form keeps what was entered"; "The message sits by the Receipt field on New claim, and the amount and category stay as entered."

- **minor · style · Figure 5, row "Card, A-4", column Empty**
  - Current: `[no card issued] not issued yet; claims still work` is drawn in tone 3.
  - Problem: under the caption's rule, paying with the card is impossible until the card is issued, which is a stop for the Card tab. It is the same kind of state as [balance used up], where claiming in other categories still works.
  - Fix: either set the cell to tone 6, or leave it at tone 3 and keep the definition as it is. The unit's point is that claims stay open, so this is the author's call. Decide it together with the [balance used up] fix so the two are coloured by the same rule.
  - Basis: line 188, "sees the Card tab in the state 'Your Perqo card has not been issued yet', with claims still open to them".

## (b) Confirmed

- **Kind and section:** a matrix, in Deliverable B, B.5. Line 387 is `### B.5 · Screen states` and the marker is at line 404.
- **Column headers** (Empty, Error, Permission, Shown later): line 391, "| Screen | Empty | Error | Permission | Shown later |". Line 389: '"shown later" is what progressive disclosure keeps one level down'.
- **Row labels:** all 10 are in the B.5 table, lines 393–402.
  - Home, A-1: "| Home, A-1 |" (line 393, count 1)
  - Category screen, A-2.1 to A-2.4 (line 394, count 1)
  - Claims, A-3 (line 395)
  - New claim, A-3.1 (line 396)
  - Check and submit, A-3.2 (line 397)
  - Claim submitted, A-3.3 (line 398)
  - Card, A-4 (line 399)
  - Purchases, A-4.2 (line 400)
  - Card offers, A-4.3 (line 401)
  - Notifications, A-5.2 (line 402)
- **Cells:** every one matches its row in the B.5 table word for word.
  - **Home:**
    - Empty: "[no category open] HR chooses the open categories; Help"
    - Error: "[no connection] the last balances, with their time"
    - Shown later: "spent, amount and period, on the category screen" (line 393)
  - **Category screen:**
    - Empty: "[balance used up] no balance left this period; Why can't I use money from another category?"
    - Permission: "[category closed] not shown"
    - Shown later: "cross-listings, after the home items" (line 394)
  - **Claims:**
    - Empty: "[no claims] How to claim back a receipt; New claim"
    - Error: "[no connection] the last list, with its time"
    - Shown later: "the claim, on tap" (line 395)
  - **New claim:**
    - Error: "[receipt missing] by the Receipt field; input kept"
    - Permission: "[camera refused] Choose a file"
    - Shown later: "the limit, in the rule line" (line 396)
  - **Check and submit:** Error: "[over the balance] Edit only" (line 397)
  - **Claim submitted:** Permission: "[first claim] the notifications prompt" (line 398)
  - **Card:**
    - Empty: "[no card issued] not issued yet; claims still work"
    - Shown later: "card details, on tap" (line 399)
  - **Purchases:**
    - Empty: "[no purchases] Where you can pay with the Perqo card"
    - Error: "[no connection] the last list, with its time"
    - Shown later: "the purchase, on tap" (line 400)
  - **Card offers:**
    - Empty: "[no offers] the route is hidden"
    - Permission: "[category closed] its offers not shown"
    - Shown later: "the filter by category" (line 401)
  - **Notifications:**
    - Empty: "[none yet] what will appear here"
    - Permission: "[notifications not allowed] how to allow them"
    - Shown later: "the claim, on tap" (line 402)
- **Blank cells:** each blank cell is a "none" in the table (lines 393–402). The caption says "Blank cells: no such state".
- **Legend, tone 3 "the Perqo app":** line 12, "so every app box is tone 3"; line 356, "every box tone 3, the app".
- **Legend, tone 6 "a stop: the path ends without success here":** only in the caption, not in the unit's text (see the line 12 finding).
- **Caption parts:**
  - **"Conditions in square brackets, as IA2's conditional area":** line 105, "Garrett's vocabulary already had the conditional area ... which IA2 reduced to a box whose note opens with the condition in square brackets (IA2, section 5.1)". Line 99, "each written as a [condition] in its note".
  - **"empty-state rule this unit's synthesis from IA3, A3 and F2":** line 164, "The rule below is this unit's synthesis from IA3's evidence. A screen reached by a label must confirm the label on arrival (IA3, A3 ...) ... the route to the next step (IA3, F2)".
  - **"error states from Neusesser and Sunwall, 'Error-Message Guidelines', NN/g, 2023":** line 170 ("Error-Message Guidelines", Nielsen Norman Group, 14 May 2023) and line 500.
  - **"permissions from Android Developers, 'Request runtime permissions', 2026 (platform documentation)":** line 182 ("page updated 28 October 2026 ... platform documentation") and line 491.
  - **"disclosure from Nielsen, 'Progressive Disclosure', NN/g, 2006":** line 46 ("Progressive Disclosure", Nielsen Norman Group, 3 December 2006), line 158 and line 502.
  - **"supports the decision on what each screen shows under each condition and by which route the employee goes on":** line 154, "each decides what exists where, under what condition, and by which route the person goes on ... The per-screen record is Deliverable B, B.5".
  - **"F2":** line 307, "at fidelity F2".
  - **"Perqo is fictional":** line 389, "(Perqo, fictional)".
- **Tone 6 on [no category open], the three [no connection] cells and [over the balance]:** each fits the caption's definition.
  - Line 166: "the employer's HR team chooses which categories are open". HR has to act before anything opens.
  - Line 175: "Home shows the last balances it loaded, with the time". Current data waits on the connection.
  - Line 174: "with Edit as the only route forward".
- **Legibility:**
  - **Desktop:** the whole figure fits in one frame, light and dark. Labels are whole and nothing overlaps.
  - **Tablet:** the whole figure fits in one frame, light and dark. Labels are whole and nothing overlaps.
  - **Phone (390 px), light and dark:** it scrolls sideways (372 px) and says so ("scroll sideways for the whole figure"). The row labels stay fixed on the left, so each row stays named while scrolling. Every cell can be reached by scrolling. The legend reads whole in frame 2.
  - **Both themes:** the tone 6 cells and the grey blank cells are told apart in light and dark.

## (c) Renderer notes

- **Opening frame clipped by the header (renderer, not a fix).** At desktop, tablet and phone, the opening frame is partly covered by the page header and the section bar, which stay at the top of the screen. The Home row and part of the Category row are hidden under them in both themes. The frames sheet shows the whole figure.
- **Phone: the label column takes most of the width (renderer; a possible author fix).**
  - The fixed row-label column takes about 245 of 390 px, leaving about 125 px for the cells. The Empty column is about 170 px wide, so no Empty cell can be read whole in one position. "[no category open] HR chooses the open categories; Help", for example, has to be read across two scroll positions, with a fade on the right edge.
  - The captured frames (scrolled to 0, 164, 328 and 372) never show the right part of the Empty column or the Permission column whole. A reader can still scroll to them.
  - If that column is sized to its longest label, the author could shorten "Category screen, A-2.1 to A-2.4", for example to `Category, A-2.1 to A-2.4`, in both the B.5 table and the figure. That would widen the space for the cells. I cannot check from the screenshots whether it would make the Empty column fit. The same content is in the B.5 table just above.
- **Word split mid-word (renderer; a possible author fix).** At desktop and tablet, in both themes, the Notifications row's Permission cell breaks as "[notification / s not / allowed]". The column holds about 13 characters, and "[notifications" is 14, so any wording that starts with "[notifications" will break the same way. Rewording would mean changing the B.5 table and the figure together, and still has to fit the column. "cross- / listings" breaks at its own hyphen, which is fine.

## (d) Result

Figure 5: **FIX**. 0 error, 3 should-fix, 2 minor.

## Figure 8 re-check 1 (Opus 5.5 agent, 3 November 2026; the second check of figure 8, wireflow: submit a claim; given the unit without its figures, the captions and the frames sheets, nothing of the earlier reports; verbatim hand-back; the harness refused its `out/` write, so the hand-back is the one copy)

# Figure check · IA6 · figure 8 (wireflow) · second check

Figure 8 is a wireflow. It sits in Deliverable C, C.3 "Submit a reimbursement claim" (line 436). The kind fits: it shows the screens of one task, and rule 7 says "screens: wireflow".

## (a) Findings

1. [should-fix] [accuracy] unit text, line 12 (introduction); Current: `on a figure of one surface every box takes that surface's tone, so every app box is tone 3.`; Problem: figure 8 shows only one surface (the app), yet it draws two app boxes in tone 6: "Check and submit [over the balance]" and "Claim [Rejected]". Its caption explains this ("tone 6 a state where the path stops"). The unit's text never names tone 6 (`grep -F -c "tone 6"` = 0, "Tone 6" = 0). So the tone 6 used by the caption and the figure cannot be traced to the text, and line 12 contradicts it. Figures 5, 6 and 7 use tone 6 the same way. Fix: `on a figure of one surface every box takes that surface's tone, so every app box is tone 3, except a state where the path stops, which takes tone 6 (IA2, section 5.2).`; Basis: line 12; figure 8 at every width and theme, where those two boxes are drawn in the tone-6 ochre and every other box in tone 3 teal.

2. [minor] [label] figure 8, screen "Claim [Approved]", last line; Current (figure): "→ see claim lifecycle"; Problem: the phrase "claim lifecycle" does not appear in the text (`grep -F -c "claim lifecycle"` = 0). The text has "the claim's lifecycle" (lines 307 and 416) and, at line 434, "Approved (then Paid, by the lifecycle IA2 drew)". The figure also leaves out the Paid step that the text names. Fix: change the label to "Then Paid → see the claim's lifecycle (IA2, section 5.3)"; Basis: line 434 "Approved (then Paid, by the lifecycle IA2 drew)".

3. [minor] [figure] figure 8, screen "Allow notifications? (modal)"; Current (figure): the modal has the buttons "Allow" and "Not now" and no outgoing arrow; Problem: section 5, move 3 says "Each arrow is labelled with the control that triggers it". Section 2 defines a modal as "a layer over its parent screen, closed to return to it". The figure does not show where Allow or Not now lead, or where Done leads when it is not the first claim. Fix: add one arrow from the modal back to "Claim submitted" (or on to "Claims") labelled "tap Allow or Not now", or add the note line "closes to Claim submitted" inside the modal; Basis: line 107 "\"modal\" (a layer over its parent screen, closed to return to it)"; line 208.

4. [minor] [figure] figure 8, arrows "tap the notification [approved]" and "tap the notification [rejected]"; Current (figure): both arrows leave the "Claim submitted" screen; Problem: section 5, move 3 says "the label must match a button on the screen it leaves". Claim submitted has no notification on it; its only control is Done. The notification arrives later, on the phone (B.4, E-4). Fix: keep the arrows and change their labels to "later: tap the notification [approved]" and "later: tap the notification [rejected]", or add the note "entry: a notification" to the two Claim boxes, using the app map's "entry:" word; Basis: line 208 "the label must match a button on the screen it leaves"; line 380 "E-4 | A notification about a claim | ... | Claim, A-3.4"; line 434 "When the claim moves, the notification opens the Claim screen".

## (b) Confirmed

Screens and labels:
- "Claims" with "Submitted", "Approved", "Rejected", "Paid", "Help with claims", "New claim": line 434 "Claims lists all four states, with Help with claims."; line 365 "A-3 Claims. The four state groups, newest first in each; New claim; Help with claims."
- "New claim" with "Category", "Learning balance", "Amount", "Receipt", "Take a photo", "Choose a file", "Claims over the limit need HR approval", "Continue": line 434 "New claim shows the chosen category's balance, two ways to add the receipt, and the rule \"Claims over the limit need HR approval\"."; line 365 "asks for a category (open ones only), shows that category's balance, asks for the amount and the receipt (Take a photo, or Choose a file)".
- "Check and submit" with "Category and amount", "Learning balance after", "Edit", "Submit": line 365 "Check and submit (A-3.2) shows category, amount and the balance after, with Edit and Submit."
- "Check and submit [over the balance]" with "Category and amount", "More than your Learning balance", "Edit" (the only route): line 174 "Check and submit therefore shows the state \"More than your Learning balance\", with Edit as the only route forward"; line 434 "Continue opens Check and submit in its over-balance state, with Edit as the only route"; line 207 "(\"Check and submit [over the balance]\")".
- "Claim submitted" with "Status: Submitted", "[over the limit] HR decides", "Done": line 365 "Claim submitted (A-3.3) shows the status Submitted and, for a claim over the limit, that HR decides."
- "Allow notifications? (modal)" with "[first claim only]", "Get told when your claim is approved, rejected or paid", "Allow", "Not now": line 182 "notifications are asked for once, after the first claim is submitted ... the prompt says what they are for (get told when a claim is approved, rejected or paid), with Allow and Not now as its two answers"; line 434 "on the first claim, Done opens the notifications prompt, a modal".
- "Claim [Approved]" with "Status: Approved", "Amount, category, date submitted", "Receipt": line 365 "Claim (A-3.4) shows status, amount, category, date submitted and the receipt".
- "Claim [Rejected]" with "Status: Rejected", "Rejected by HR, or over the balance", "Why was my claim rejected?": line 365 "when Rejected, the reason (over the balance, or by HR) and the link Why was my claim rejected?"; line 434 "Rejected with its reason and the link Why was my claim rejected?".
- Learning as the example category: line 475 "shows \"More than your Learning balance\" (in the chosen category's name)".

Arrows:
- "tap New claim", "tap Continue", "tap Edit" (back to New claim), "tap Submit (no way back)": line 434 "tap New claim, tap Continue, tap Edit back to New claim, and tap Submit with no way back (IA2, section 5.3)".
- "tap Continue [over the balance]": line 434 "When the amount is over the category's balance, Continue opens Check and submit in its over-balance state".
- "tap Edit" from the over-balance state to New claim: line 434 "with Edit as the only route"; line 174 "the form keeps what was entered".
- "[first claim] tap Done": line 434 "on the first claim, Done opens the notifications prompt, a modal".
- "tap the notification [approved]", "tap the notification [rejected]": line 434 "When the claim moves, the notification opens the Claim screen: Approved ... or Rejected"; line 216 "the outcome becomes two states of one Claim screen reached from a notification".
- The camera branch drawn as two buttons: line 216 "the camera branch becomes two buttons on New claim".

Notation:
- A frame with a title bar for each screen, bars as placeholder text, buttons as controls, labelled arrows, and a [condition] in the title for a state: line 418 "a frame with a title bar is one screen, bars and blocks are placeholder text and areas, a button is a control, and an arrow is labelled with the action or the condition that moves the person ... A screen title with a [condition] is a state of that screen. Two screens per row keep each drawing legible on a phone." The figure is drawn this way, with two screens per row in five rows.
- "modal" in the title: line 107 "\"modal\" (a layer over its parent screen, closed to return to it)".
- Tone 3 for app screens: line 12 "so every app box is tone 3" (see finding 1 for tone 6).

Caption:
- It says what the figure shows: "an employee submits a reimbursement claim in the Perqo app, F2, extending IA2, section 5.3's claim wireflow (Claims, New claim, Check and submit, Claim submitted; Edit back; Submit with no way back)". Line 434: "This extends IA2's claim wireflow and keeps every screen, label and arrow in it: Claims, New claim, Check and submit and Claim submitted; tap New claim, tap Continue, tap Edit back to New claim, and tap Submit with no way back (IA2, section 5.3)."
- "IA3's B1, B2 and C4 fixes": line 337 "B1 | ... the chosen category's balance on New claim and on Check and submit | A-1; A-3.1; A-3.2"; line 338 "B2 | group Claims by all four states | A-3; the Claim screen (A-3.4) shows the reason when Rejected"; line 342 "C4 | ... the rule in the employee's terms where the claim is made | ... the rule on A-3.1".
- "the over-balance state, the notifications prompt and the Claim screen's outcomes": line 434.
- It names the section, "(Deliverable C, C.3)": heading line 432 "### C.3 · Submit a reimbursement claim".
- Decision, "which screens and states the claim task needs and where it cannot be undone": line 416 "decision: which screens each core task needs, what changes on them, and where the task can stop".
- Sources:
  - "The rule from IA2, section 5.3 and IA3, section 2.3": line 174 "The rule rejects a claim whose amount is over the chosen category's balance (IA2, section 5.3; IA3, section 2.3)".
  - "the no-way-back label stands for Garrett's crossbar (IA2, section 5.1)": line 508 "Garrett, *Visual Vocabulary Quick Reference* (conditional area, crossbar)"; line 105 cites IA2, section 5.1 for Garrett's vocabulary.
  - "wireflow form from Laubheimer, NN/g, 2016": line 193 and Sources line 498.
  - "F2": line 416 "three wireflows of the Perqo app, at fidelity F2".
  - "Perqo is fictional": line 434 "(Perqo, fictional)".
- Kind: a wireflow for screens, which fits.

Legibility as the reader sees it:
- Desktop, light and dark: the whole figure fits in one frame. Every screen title, body line and button is whole, no box overlaps another and the caption is whole. One label is crossed by a line (renderer note 1).
- Tablet, light and dark: the whole figure fits in one frame, the same as on desktop.
- Phone, light and dark:
  - The two columns scroll sideways, and the hint "scroll sideways for the whole figure" is shown. There are three frames, at 134, 298 and 372 of 372 px.
  - The left column is whole in frame 1 and the right column is whole in frames 2 and 3.
  - Every arrow label is whole in at least one frame. Frame 1 has "tap New claim", "tap Continue", "tap Edit", "tap Submit (no way back)", "[first claim] tap Done" and "tap the notification [approved]". "tap Continue [over the balance]", the right-hand "tap Edit" and "tap the notification [rejected]" appear across frames 1 to 3.
  - A phone reader can follow it row by row, left then right.
- The tones read in both themes. Tone 3 is the teal of the title bars and borders. Tone 6 is the ochre of "Check and submit [over the balance]" and "Claim [Rejected]", including their buttons.

## (c) Renderer notes

1. A vertical arrow line crosses the label "tap Continue [over the balance]". At every width and theme, the return arrow from "Check and submit [over the balance]" (its "tap Edit" arrow) runs through the middle of this label, through "tap", "[over" and "balance]". The words stay readable. The label also sits beside that upward return arrow, not beside the downward arrow it names, so the reader has to work out from the arrowheads which arrow it labels. This comes from how the renderer routes two arrows between the same pair of screens. A shorter label would not reliably clear the line, so this is not a FIX. If the renderer allows it, putting the labels of the return arrow and the forward arrow on opposite sides would solve it.
2. Desktop and tablet opening frames: the figure is taller than the viewport, so the sticky section bar covers part of the second row (Check and submit and the over-balance state) in the opening frame. The frames sheet shows the whole figure. Not a FIX.
3. Phone: the drawing opens at 134 of 372 px, with the right column cut at the edge. Scrolling sideways shows it whole. Not a FIX.

## (d) Verdict

Figure 8: PASS (labels traced, caption complete, kind fits, notation as the text describes). 0 errors, 1 should-fix (unit text, line 12: tone 6 is never named), 3 minor.

(The harness refused the write to D/out/report.md, so this reply is the only copy.)

## Figure 1 re-check 2 (Opus 5.5 agent, 3 November 2026; the third check of figure 1, matrix: navigation patterns; given the unit without its figures, the captions and the frames sheets, nothing of the earlier reports; verbatim hand-back; the harness refused its `out/` write, so the hand-back is the one copy)

# Figure check · IA6 figure 1 (matrix) · third check

Kind: matrix. Section: 3.5 · Choosing Perqo's pattern by IA3's criteria (placed after line 148 of D/unit-without-figures.md). Shape: four items (patterns) against eight sections (two facts, four criteria, the Perqo decision), so the kind is items by sections, and a matrix fits.

## (a) Findings

1. [minor] [label] Section 3.5, the sentence that names the figure's rows. Current: `and each criterion by its ID and a gloss (A4 · icon text, B1 · units in view, F1 · unambiguous, F2 · reachable).` Problem: the figure has eight rows. The sentence names seven and leaves out the last row, "In the Perqo app", whose cells come from the decision after the figure. The unit's text also defines tone 6 (line 14) only as "a state where the path ends without success, or a fault found in a review". The figure's legend and caption add "or the measured cost behind one", and the unit's text never says so. Fix: `and each criterion by its ID and a gloss (A4 · icon text, B1 · units in view, F1 · unambiguous, F2 · reachable); its last row, In the Perqo app, is the decision below. Tone 6 marks a fault against one of the four criteria, or the measured cost behind it.` Basis: line 148; line 14 `tone 6, IA2's stop, marks a state where the path ends without success, or a fault found in a review`; every frame shows the row "In the Perqo app" and the legend "tone 6 · a fault against an IA3 criterion, or the measured cost behind one". (Both Current strings occur once in the unit: grep -F -c = 1.)

2. [minor] [figure] The caption's sources. Current (caption): `criteria A4, B1, F1, F2 from IA3, Deliverable;` Problem: the caption gives no source for the row "In the Perqo app" ("the five tabs", "Home's routes to the top tasks", "inside a tab, two levels at most", "not used"). Those cells come from this section's decision and from section 3.3. The caption already names section 3.5 as the section the figure supports, so this is minor, not a should-fix. Fix (caption): `criteria A4, B1, F1, F2 from IA3, Deliverable; the Perqo row from the decision under the figure and section 3.3;` Basis: line 152 `a tab bar of IA3's five tabs as the global routes; Home as a partial hub, with routes to the top tasks; drill-down inside a tab, no deeper than two levels; no hidden menu`; line 129 `at most two levels below the tab`.

No errors. No label, date or number in the figure is missing from the unit's text.

## (b) Confirmed

Column heads
- TAB BAR: line 111 `### 3.1 · Tab bar`
- HUB AND SPOKE: line 119 `### 3.2 · Hub and spoke`
- DRILL-DOWN: line 125 `### 3.3 · Hierarchical drill-down`; line 141 `for a drill-down`
- HAMBURGER MENU: line 131 `### 3.4 · The hamburger menu, on the evidence`

Row labels
- Destinations: where / Destinations: room / Evidence on use / A4 · icon text / B1 · units in view / F1 · unambiguous / F2 · reachable: line 148 `Figure 1 names its rows in short: Destinations: where and Destinations: room for the first and last of these, Evidence on use, and each criterion by its ID and a gloss (A4 · icon text, B1 · units in view, F1 · unambiguous, F2 · reachable).`
- In the Perqo app: line 152 `The decision (Perqo, fictional): ...`; line 129 `The Perqo app uses drill-down inside a tab only` (the label is not in line 148: finding 1)

Row: Destinations: where (all tone 3)
- on every screen / on the hub / one level at a time / behind an icon: line 141 `on every screen for a tab bar (Budiu 2015); on the hub for a hub, with an extra step per use (Budiu 2015); one level at a time for a drill-down, where depth slows people (section 3.3); behind an icon for a hamburger menu`

Row: Destinations: room (all tone 3)
- three to five / as many as the hub holds / any, at the cost of levels / a fairly large number: line 146 `three to five for a bar (Android Developers 2026; Budiu 2015); as many as the hub holds; any number for a drill-down, at the cost of levels; a fairly large number for a menu (Budiu 2015)`. "any" stands for "any number", and the row label supplies the noun.

Row: Evidence on use
- visible links: not tested on mobile (tone 3): line 141 `Visible links alone were not tested on mobile (section 3.4).`; line 133 `(visible-only navigation was not tested on mobile)`
- an extra step per use (tone 3): line 141 `with an extra step per use (Budiu 2015)`. It is Budiu's guidance, not a measurement, so tone 3 agrees with the legend's "measured cost".
- depth slows people (tone 6): line 141 `where depth slows people (section 3.3)`; line 127 `Deeper structures slowed people in every study IA4 reviewed`. This is a measured cost.
- used in 57% of cases on mobile, against 86% for combined (tone 6): line 141 `used in 57% of cases on mobile against 86% for combined navigation (Pernice and Budiu 2016)`; line 133 `on mobile, hidden navigation was used in 57% of the cases and combined navigation in 86%`

Row: A4 · icon text
- labels under icons / labelled routes / labelled rows (tone 3): line 142 `a tab bar's icons carry their labels under them; a hub's routes and a drill-down's rows are labelled`
- the icon often has no text (tone 6): line 142 `the hamburger's trigger is an icon that often has no text (Harley 2014)`; line 135 `The icon itself fails IA3's A4 when it carries no text`

Row: B1 · units in view
- Home can show the four balances / the hub can show them (tone 3): line 143 `A tab bar's Home can show the four balances, and so can a hub`
- only on the level they sit on (tone 6): line 143 `a drill-down shows them only on the level they sit on`. It fails B1 (`the four category balances must be on the first screen and on New claim`).
- hidden until opened (tone 6): line 143 `a hidden menu hides them until it is opened`

Row: F1 · unambiguous
- one level of tabs / one level of routes (tone 3): line 144 `a tab bar is one level of tabs and a hub one level of routes`
- one more choice per level (tone 6): line 144 `a drill-down adds one more choice per level, each of which must carry scent (Larson and Czerwinski 1998; IA3, section 6.2)`. The depth cost Larson and Czerwinski measured stands behind it, so tone 6 agrees with the legend.
- one list, if labelled (tone 3): line 144 `a menu is one list, if it is labelled`

Row: F2 · reachable
- yes: the tabs persist (tone 3): line 145 `yes for a tab bar, since the tabs persist`
- only from the hub / only by going back / only after opening the menu (tone 6): line 145 `only from the hub for a hub; only by going back for a drill-down; only after opening the menu for a hamburger`

Row: In the Perqo app (all tone 3)
- the five tabs: line 152 `a tab bar of IA3's five tabs as the global routes`; line 117 `The Perqo app keeps five tabs`
- Home's routes to the top tasks: line 152 `Home as a partial hub, with routes to the top tasks`; line 123 `Home carries routes to the top tasks`
- inside a tab, two levels at most: line 152 `drill-down inside a tab, no deeper than two levels`; line 129 `at most two levels below the tab`
- not used: line 152 `no hidden menu`; line 135 `The Perqo app has no hamburger menu.`

Legend
- tone 3 · the Perqo app; tone 6 · a fault against an IA3 criterion, or the measured cost behind one. These agree with the caption `Rows tone 3, the app; tone 6 marks a fault against an IA3 criterion, or the measured cost behind one`. Line 14 sets the base, `every app box is tone 3, and tone 6, IA2's stop, marks ... a fault found in a review`; the "measured cost" extension is finding 1.

Caption elements
- Says what the figure shows: "four mobile navigation patterns against the evidence and the IA3 criteria that separate them, for the Perqo app".
- Names the section: "(section 3.5)" is line 137 `### 3.5 · Choosing Perqo's pattern by IA3's criteria`.
- Budiu, 'Basic Patterns for Mobile Navigation: A Primer', NN/g, 2015: Sources `Budiu, Raluca. "Basic Patterns for Mobile Navigation: A Primer". Nielsen Norman Group, 15 November 2015.`
- Pernice and Budiu, 'Hamburger Menus and Hidden Navigation Hurt UX Metrics', NN/g, 2016 (179 participants, websites): line 133 `In a study of 179 participants on six live sites`, `The study was of websites`; Sources `26 June 2016`.
- three to five destinations from Android Developers, 'Layouts and navigation patterns', 2026 (platform documentation): line 113 `"The navigation bar can hold three to five navigation destinations across the same hierarchy level" (Android Developers, "Layouts and navigation patterns", page updated 22 October 2026 ...; platform documentation)`
- depth from Larson and Czerwinski, 1998, and Zaphiris, 2000 (through IA4, section 2.1): line 127 `(Zaphiris 2000; Larson and Czerwinski 1998; IA4, section 2.1)`
- Nielsen, 'Progressive Disclosure', NN/g, 2006: line 127 `"In practice, designs that go beyond 2 disclosure levels typically have low usability" (Nielsen 2006)`; Sources `"Progressive Disclosure". Nielsen Norman Group, 3 December 2006.`
- criteria A4, B1, F1, F2 from IA3, Deliverable: line 139 `A1 to A5 (scent), B1 and B2 (mental models), F1 and F2 (findability)`; line 330 `(IA3, Deliverable, "The checklist applied to the as-is Pe...`
- the hamburger's unlabelled icon from Harley, 'Icon Usability', NN/g, 2014: line 135 `(Harley, "Icon Usability", NN/g, 2014; IA3, section 1.2)`
- Perqo is fictional: line 152 `(Perqo, fictional)`

Kind check: patterns (items) against rows (sections) is "items by sections", so the matrix is the right kind.

Notation check: every cell is tone 3 or tone 6, there are no type tags or other marks, and the legend names both tones. This matches line 14 and the caption. Each tone-6 cell (colours sampled from the frames) is either a fault the text states or a measured cost:
- Faults: A4 for the hamburger; B1 for drill-down and the hamburger; F2 for hub, drill-down and the hamburger.
- Measured costs: depth, from IA4's studies (in Evidence and in F1 for drill-down); 57% against 86%, from Pernice and Budiu.

The only cost in tone 3 is the hub's "an extra step per use", which is guidance, not a measurement, so it is not a fault.

Legibility, as the reader sees it
- Desktop, light and dark: one frame holds the whole figure. Every label is whole, nothing overlaps, both tones are clear in both themes, and the legend fits on one line.
- Tablet, light and dark: one frame holds the whole figure. Every label is whole and nothing overlaps.
- Phone (390 px), light and dark: the figure scrolls sideways across four frames (0, 164, 328, 372 of 372 px), with a "scroll sideways for the whole figure" hint. The row labels stay pinned on the left. Every cell and column head is whole in at least one frame (tab bar in frame 1, hub and drill-down in frame 2, hamburger in frames 3 to 4). The legend line scrolls with the figure, and the caption repeats it in full. Nothing that cannot be scrolled to is cut, and a phone reader can follow the figure row by row.

## (c) Renderer notes (not FIX; no change the author can make is needed)

- In the opening frame at every width and theme, the sticky section bar clips the column heads, and on the phone also the first row. The frame sheets show the whole head row once the reader scrolls.
- On the phone, the edges of the scrolling area fade, so the cells next to the pinned row labels are partly hidden in each frame, and the legend's tone-6 text runs past the first frame. Every cell and the legend can be read in full at some scroll position, and the caption repeats the legend.
- The phone opens at the drawing's start, the Tab bar column.

## (d) Verdict

Figure 1: PASS. 0 error, 0 should-fix, 2 minor.

(The harness refused the write to D/out/report.md; this reply is the only copy. To inspect the phone frames I wrote crops under D/out/: p2.png, p3.png, d4.png.)

## Figure 4 re-check 2 (Opus 5.5 agent, 3 November 2026; the third check of figure 4, sitemap: the app map; given the unit without its figures, the captions and the frames sheets, nothing of the earlier reports; verbatim hand-back; the harness refused its `out/` write, so the hand-back is the one copy)

# IA6 · figure 4 (sitemap) · fresh figure check 3

Figure 4 is a sitemap in Deliverable B, B.3 "The map" (unit line 360). The kind fits, because the data is a hierarchy: the surface, its tabs, and the screens under each tab. The caption says what the figure shows and names the sections: Deliverable B, section 2 for the note words, and section 3.3 for the staged sequence. It also names where the data comes from: IA1, IA2 section 5.3, IA3 Deliverable, IA4 Deliverables A and B, IA5 Deliverable A, and this Deliverable. The caption passes.

## (a) Findings

1. [should-fix] [accuracy] Figure 4, the Card (A-4) and Benefits (A-2) branches, and the B.3 prose.
   - Current: `| Freezing and unfreezing your card, H-2.3.1 |` and `| the Benefits pages | H-2.1.3 |` (section 6.2, column "Help centre route from the app").
   - Problem: section 6.2 lists two routes out of the app that neither the map nor B.3's screen list has:
     - Freezing and unfreezing your card (H-2.3.1), from Card.
     - What you can claim in each category (H-2.1.3), from the categories and What's covered.
     B.3 says `Every route that leaves the app from a screen's default state is tagged `external` with a "→ see" note to its Help centre page`, and the caption says the same, so the map is incomplete against the text. The map draws every other route in that column (H-2.2.1, H-2.1, H-1.2.5, H-2.3.2, H-2). H-2.2.2 and H-2.1.2 are routes that appear only in a state.
   - Fix, in the figure: add two boxes.
     - Under Card, after "Freeze card": tag `EXTERNAL`, title `Freezing and unfreezing your card`, note `→ see H-2.3.1`.
     - Under Benefits, after "Meals": tag `EXTERNAL`, title `What you can claim in each category`, note `on each category screen → see H-2.1.3`.
   - Fix, in the B.3 prose:
     - Current: `A link Where you can pay with the Perqo card (H-2.3.2) sits on Card.` Fix: `Links Where you can pay with the Perqo card (H-2.3.2) and Freezing and unfreezing your card (H-2.3.1) sit on Card.`
     - Current: `and New claim with the category already chosen.` Fix: `New claim with the category already chosen, and the link What you can claim in each category (H-2.1.3).`
   - Alternative, if the author does not mean these routes to exist: change the three 6.2 cells instead.
     - Current: `| Freezing and unfreezing your card, H-2.3.1 |` Fix: `| none |`
     - Current: `| Benefits, S-1.4.1 to S-1.4.4 | What you can claim in each category, H-2.1.3 |` Fix: `| Benefits, S-1.4.1 to S-1.4.4 | none (H-2.1.3 links in: B.4, E-6) |`
     - Current: `| the Benefits pages | H-2.1.3 |` Fix: `| the Benefits pages | none (H-2.1.3 links in: B.4, E-6) |`
   - Basis: unit lines 235, 236, 240, 358, 366, 368. No frame shows an H-2.3.1 or H-2.1.3 box.

2. [should-fix] [label] Figure 4, the notes of Sign in, New claim (A-3.1), the category screens and Card offers.
   - Current: `each named entry, marked "entry:" in the note: opening the app, a notification, an invitation, a link from perqo.com` (section 2 table).
   - Problem: the map marks "entry:" on only three of B.4's seven entries: Home (E-1), Join (E-2) and Claim (E-4). These ways in carry no "entry:", although section 2 says a link from perqo.com is marked that way:
     - Sign in (A-0.2), where E-1 lands when the employee is signed out.
     - New claim (A-3.1), E-5, reached from a Help centre article.
     - The category screens, E-6.
     - Card offers (A-4.3), E-7, opened filtered.
     The root's note "entries in B.4" points to the table but does not meet the rule section 2 states.
   - Fix, as the reader would see the notes:
     - Sign in: `A-0.2 · entry: opening the app, signed out`
     - New claim under Claims: `A-3.1 · entry: a Help centre link · Claims over the limit need HR approval`
     - Benefits: `A-2 · the four categories only; each category: entry: a Help centre link`
     - Card offers: `A-4.3 · entry: a link, filtered · filter by category`
   - Alternative, a text-only fix. Current: `each named entry, marked "entry:" in the note: opening the app, a notification, an invitation, a link from perqo.com` Fix: `the main entries, marked "entry:" in the note (opening the app, an invitation, a notification), and every entry with its landing and address in the entry table (B.4), links from perqo.com among them`
   - Basis: unit lines 101 and 379 to 385. The frames show the notes as "A-0.2" for Sign in, "A-3.1 · Claims over the limit need HR approval" for New claim, and "A-4.3 · filter by category" for Card offers.

3. [minor] [accuracy] The B.3 prose, for the Claim box (A-3.4).
   - Current: `the routes that appear only in a state are in B.5.`
   - Problem: in its Rejected state, the Claim screen has the route Why was my claim rejected? (H-2.1.2; lines 237, 367, 436). That is a state route, but B.5 has no row for Claim, A-3.4, and the map's Claim note carries only "[Rejected] the reason". So this one state route is in neither place B.3 points to.
   - Fix: `the routes that appear only in a state are in B.5, except the Rejected claim's link Why was my claim rejected? (H-2.1.2), given with A-3.4 below.`
   - Basis: unit lines 358, 367 and 393 to 404; frame note "A-3.4 · entry: a notification · [Rejected] the reason".

Every Current above occurs exactly once in D/unit-without-figures.md (checked with grep -F -c).

## (b) Confirmed

- Root "Perqo app · tab bar: the global routes; entries in B.4": "The root is the surface, since the tab bar is not a screen" (l. 358); "Global routes | header and footer | the tab bar, on every screen but the sign-in screens and modals" (l. 102); B.4 table (l. 377 to 385).
- SECTION "Join and sign in · A-0 · [signed out]": "A-0 Join and sign in, A-0.1 Join, A-0.2 Sign in" (l. 469); "Sign in (A-0.2) is for an employee who has joined and is signed out" (l. 364).
- FORM "Join · A-0.1 · entry: HR's invitation": "Join (A-0.1) opens from HR's invitation" (l. 364); E-2 (l. 380).
- FORM "Sign in · A-0.2": l. 364, 469.
- HOME "Home · A-1 · entry: opening the app": "E-1 | Opening the app | the phone | Home, A-1" (l. 379).
- DETAIL "Balance · on Home: each open category and what remains → see A-2.1 to A-2.4": "Balance: each open category with what remains, each opening its category screen" (l. 365).
- EXTERNAL "Your balance explained · → see H-2.2.1": "the link opens H-2.2.1" (l. 323); "Home's link (A-1)" (l. 334).
- INDEX "Recent activity · on Home: purchases and claims, newest first; Submitted": "Recent activity, the latest purchases and claims mixed, newest first, with claim statuses in the Claims words (Submitted, never Pending)" (l. 365).
- FORM "New claim · on Home: a button → see A-3.1": "a button with the text New claim on Home, on Claims and on each category screen, all opening A-3.1" (l. 322).
- INDEX "Benefits · A-2 · the four categories only": "The four categories open to the employee's group, nothing else" (l. 366); "Benefits holds the four categories only" (l. 341).
- DETAIL "Health · A-2.1 · Fitness: gym membership, yoga class, swimming pool entry; Therapy: therapy session; also: bike helmet, covered under Mobility (assumed)": "under Health, gym membership, yoga class and swimming pool entry (Fitness) and therapy session (Therapy)" (l. 358); "bike helmet in Health, each "covered under" its home, marked assumed (IA4, R6)" (l. 343).
- DETAIL "Learning · A-2.2 · Courses: coding course, cookery course; Books: book; also: yoga class, covered under Health (assumed)": "under Learning, coding course and cookery course (Courses) and book (Books)" (l. 358); "yoga class in Learning" (l. 343); "("Yoga class: covered under Health")" (l. 366).
- DETAIL "Mobility · A-2.3 · Public transport: train pass; Bike: bike helmet, bike repair": "under Mobility, train pass (Public transport) and bike helmet and bike repair (Bike)" (l. 358). Mobility has no cross-listing, which agrees with "A-2.1, A-2.2, A-2.4" (l. 454).
- DETAIL "Meals · A-2.4 · Restaurants: restaurant meal; Groceries: groceries; also: cookery course, covered under Learning (assumed)": "under Meals, restaurant meal (Restaurants) and groceries (Groceries)" (l. 358); "cookery course in Meals" (l. 343).
- Twelve items drawn (4 + 3 + 3 + 2): "extends from IA3's six to IA4's twelve ... BI-001 to BI-012" (l. 358).
- INDEX "Claims · A-3 · Submitted, Approved, Rejected, Paid; newest first": "Submitted, Approved, Rejected, Paid, newest first in each" (l. 321).
- FORM "New claim · A-3.1 · Claims over the limit need HR approval": "| taken | on New claim, with a link to How approval rules work, H-1.2.5 |" (l. 325).
- EXTERNAL "How approval rules work · → see H-1.2.5": l. 325, 367.
- FORM "Check and submit · A-3.2 · after A-3.1 · [over the balance] Edit only": "| Check and submit, A-3.2 | none | [over the balance] Edit only |" (l. 399).
- DETAIL "Claim submitted · A-3.3 · after A-3.2 · [first claim] modal: the notifications prompt": "| Claim submitted, A-3.3 | none | none | [first claim] the notifications prompt |" (l. 400); "the notifications prompt, a modal that either answer closes" (l. 436).
- "after A-3.1" and "after A-3.2" drawn as siblings under Claims: "New claim, Check and submit and Claim submitted are three screens under Claims, and they are a staged sequence" (l. 129).
- DETAIL "Claim · A-3.4 · entry: a notification · [Rejected] the reason": "E-4 | A notification about a claim | ... | Claim, A-3.4" (l. 382); "when Rejected, the reason" (l. 367).
- EXTERNAL "Help with claims · → see H-2.1": "New claim; Help with claims" (l. 367); "Help with claims (H-2.1)" (l. 237).
- SECTION "Card · A-4 · [no card issued] not issued yet": "| Card, A-4 | [no card issued] not issued yet; claims still work |" (l. 401).
- DETAIL "Card details · A-4.1 · last four digits; status, Active or Frozen": "Card details (A-4.1: the last four digits and the status, Active or Frozen" (l. 368).
- INDEX "Purchases · A-4.2 · newest first": "Purchases (A-4.2, newest first)" (l. 368).
- DETAIL "Purchase · A-4.2.1 · merchant, amount, date, category": "each Purchase (A-4.2.1: merchant, amount, date, category and the category's balance after)" (l. 368). The figure shortens the note; nothing in it is wrong.
- INDEX "Card offers · A-4.3 · filter by category": "Card offers (A-4.3: offers for items in the open categories, filterable by category" (l. 368).
- FORM "Freeze card · A-4.4 · modal: confirm; Unfreeze card when Frozen": "Freeze card (A-4.4: a modal asks to confirm; on a Frozen card the action reads Unfreeze card)" (l. 368).
- EXTERNAL "Where you can pay with the Perqo card · → see H-2.3.2": "A link Where you can pay with the Perqo card (H-2.3.2) sits on Card." (l. 368).
- SECTION "Account · A-5": "A-5 Account, A-5.1 Profile, A-5.2 Notifications" (l. 469).
- DETAIL "Profile · A-5.1": l. 369, 469.
- INDEX "Notifications · A-5.2 · each opens its claim": "Notifications (each about one claim and opening it" (l. 369).
- EXTERNAL "Help · → see H-2 For employees": "Account's Help opens H-2, perqo.com/help/employees" (l. 324).
- Home's children are in the order Balance, Your balance explained, Recent activity, New claim, as in l. 365.
- Caption "F2 with an identifier on every screen": "at fidelity F2 with F3's identifiers on every screen" (l. 309).
- Caption "Every box is tone 3, the app": "every box tone 3, the app" (l. 358). In every frame, all boxes have the same tone in both themes.
- Caption "Notes carry the screen ID (A-), a [condition] ..., 'modal' ..., 'entry:' ... and 'on Home' ..., words added in section 2 under IA2's rule 'Keep the notation; extend the legend' (IA2, section 4)": l. 107.
- Caption "Routes that leave the app from a screen's default state are tagged external with '→ see' their Help centre page": l. 358.
- Caption "'→ see' with a screen ID points to a screen drawn elsewhere on the map": as drawn on Balance (→ see A-2.1 to A-2.4) and on Home's New claim (→ see A-3.1).
- Caption "Check and submit and Claim submitted follow New claim in a staged sequence; all three are screens under Claims (section 3.3)": l. 129.
- Caption "Cross-listings marked assumed follow IA4, rule R6": l. 343.
- Caption sources:
  - "the tabs ... from IA1 and IA2, section 5.3": l. 63 (IA1, section 5); l. 354 ("Claim submitted (IA2's)").
  - "the fixes from IA3, Deliverable": l. 330.
  - "the objects and catalogue items from IA4, Deliverables A and B": l. 358.
  - "the Help centre pages from IA5, Deliverable A": l. 107, 323.
- Course notation, "square-cornered boxes with IA2's type tags" (l. 358): the boxes are square-cornered and tagged SECTION, HOME, INDEX, DETAIL, FORM or EXTERNAL. This packet does not list IA2's eight tags (l. 107), so I could not check that these six are among them.

## Legibility, by width and theme

- **Desktop, dark and light:** the whole figure fits in one frame (the frames sheet says "frame 1 of 1"). Every label is whole, nothing overlaps, and the connectors are clear.
- **Tablet, dark and light:** the whole figure fits ("frame 1 of 1"). Every label is whole and nothing overlaps.
- **Phone (390 px), dark and light:** the drawing is wider than the screen and scrolls sideways (372 px, opening at 68, across three frames), with the hint "scroll sideways for the whole figure".
  - Every box is whole in at least one frame:
    - Frame 1: Join and sign in, and the Home, Claims and Card columns.
    - Frame 2: Home, Benefits with its four categories, Card and Account.
    - Frame 3: Benefits, the categories, and Account with its three children.
  - No text overlaps. The box text is small at phone width but readable.
  - A phone reader can follow it: each tab's column runs vertically and reads top to bottom.
- **Notation as the unit describes it:** tone 3 throughout, a type tag on every box but the root, and the bracketed conditions, "modal", "entry:", "on Home" and "→ see" all drawn as section 2 and the caption describe, apart from the gaps in findings 1 and 2.

## (c) Renderer notes (not FIXes)

- The root's six children wrap by width into two rows of three: Join and sign in, Home, Benefits; then Claims, Card, Account. A row is not a level: all six are the root's children, as B.3 says.
- In the desktop opening frame, the figure is taller than the screen and the sticky section bar ("Section 8 of 11 · Deliverable · B · The Perqo app map") covers the middle of it: the lower Home and Learning boxes and the top of Mobility. The frames sheet shows the figure whole.
- The phone opening frame starts at the drawing's left edge (Join and sign in, Home, Claims, Card). Benefits and Account sit to the right, cut by the screen edge and faded until the reader scrolls. Everything is reachable by scrolling sideways. A per_row of 2 would reduce the sideways scrolling, but nothing fails without it.

## (d) Result

Figure 4: FIX. error 0, should-fix 2, minor 1.

## Figure 5 re-check 2 (Opus 5.5 agent, 3 November 2026; the third check of figure 5, matrix: screen states; given the unit without its figures, the captions and the frames sheets, nothing of the earlier reports; verbatim hand-back; the harness refused its `out/` write, so the hand-back is the one copy)

Figure check · IA6 · figure 5 (matrix) · third check

Kind and place: matrix, in Deliverable B, B.5 Screen states (unit line 406, directly after the B.5 table, lines 393-404). Rows: 10 screens. Columns: Empty, Error, Permission, Shown later. Legend: tone 3 "the Perqo app"; tone 6 "a stop: the path ends without success here".

(a) Findings

1. [minor] [label] figure 5, Notifications row, Permission cell (all three widths, both themes); Current: `[notifications not allowed] how to allow them`; Problem: the word breaks inside itself at every width, so the reader sees "[notification / s not / allowed] how / to allow them". The bracket plus "notifications" is 14 monospace characters and the Permission column holds about 12. The same word fits whole in "[first claim] the notifications prompt", where it has no bracket. The author can fix this with a shorter condition; the row already names the screen and the column already names the kind of state. Fix: change the figure cell to `[not allowed] how to allow notifications`, and the unit's B.5 row to match: Current: `| Notifications, A-5.2 | [none yet] what will appear here | none | [notifications not allowed] how to allow them | the claim, on tap |` → Fix: `| Notifications, A-5.2 | [none yet] what will appear here | none | [not allowed] how to allow notifications | the claim, on tap |` (the Current string occurs once: grep -F -c = 1); Basis: desktop, tablet and phone frames, light and dark, Notifications row, Permission column; unit line 404.

2. [minor] [label] figure 5 caption; Current: `Blank cells: no such state.`; Problem: in the Shown later column (Check and submit, Claim submitted), a blank does not mean "no such state". It means nothing is kept one level down. Shown later is not a state; line 391 defines it as "what progressive disclosure keeps one level down". Fix: `Blank cells: none, as in B.5's table.`; Basis: unit line 391, and lines 399-400, where Check and submit and Claim submitted read "none" under Shown later.

No error-level and no should-fix-level findings.

(b) Confirmed

Kind and section
- Kind fits the data: items (screens) by sections (state kinds) is a matrix. Line 391: "The states each screen can be in, by the four decisions of section 4".
- Section: Deliverable B, B.5 (line 389 "### B.5 · Screen states"). The caption names "(Deliverable B, B.5)".

Column labels
- EMPTY, ERROR, PERMISSION, SHOWN LATER: line 393 "| Screen | Empty | Error | Permission | Shown later |".

Row labels (the unit's screen names; the figure leaves out the table's identifiers)
- Home: line 395 "| Home, A-1 |"
- Category screen: line 396 "| Category screen, A-2.1 to A-2.4 |"
- Claims: line 397 "| Claims, A-3 |"
- New claim: line 398 "| New claim, A-3.1 |"
- Check and submit: line 399 "| Check and submit, A-3.2 |"
- Claim submitted: line 400 "| Claim submitted, A-3.3 |"
- Card: line 401 "| Card, A-4 |"
- Purchases: line 402 "| Purchases, A-4.2 |"
- Card offers: line 403 "| Card offers, A-4.3 |"
- Notifications: line 404 "| Notifications, A-5.2 |"

Cells (each matches the B.5 table word for word; every blank cell is "none" in the table)
- Home: "[no category open] HR chooses the open categories; Help" | "[no connection] the last balances, with their time" | blank | "spent, amount and period, on the category screen": line 395.
- Category screen: "[balance used up] no balance left this period; Why can't I use money from another category?" | blank | "[category closed] not shown" | "cross-listings, after the home items": line 396.
- Claims: "[no claims] How to claim back a receipt; New claim" | "[no connection] the last list, with its time" | blank | "the claim, on tap": line 397.
- New claim: blank | "[receipt missing] by the Receipt field; input kept" | "[camera refused] Choose a file" | "the limit, in the rule line": line 398.
- Check and submit: blank | "[over the balance] Edit only" | blank | blank: line 399.
- Claim submitted: blank | blank | "[first claim] the notifications prompt" | blank: line 400.
- Card: "[no card issued] not issued yet; claims still work" | blank | blank | "card details, on tap": line 401.
- Purchases: "[no purchases] Where you can pay with the Perqo card" | "[no connection] the last list, with its time" | blank | "the purchase, on tap": line 402.
- Card offers: "[no offers] the route is hidden" | blank | "[category closed] its offers not shown" | "the filter by category": line 403.
- Notifications: "[none yet] what will appear here" | blank | "[notifications not allowed] how to allow them" | "the claim, on tap": line 404.

Text that supports the cells (beyond the table)
- Home empty: line 168 "Home in a group with no category open says that the employer's HR team chooses which categories are open, and links to Help".
- Claims empty: line 168 "Claims with no claims says that claims will appear here once submitted, links to "How to claim back a receipt" (H-2.1.1) and offers New claim".
- Card offers empty: line 168 "the route "Card offers in Meals" appears on the Meals screen only when Meals has an offer (R5)".
- No connection: line 177 "Home shows the last balances it loaded, with the time they were loaded, and Claims and Purchases show their last lists the same way."
- Receipt missing: line 178 "The message sits by the Receipt field on New claim, and the amount and category stay as entered."
- Over the balance: line 176 "Check and submit therefore shows the state "More than your Learning balance", with Edit as the only route forward".
- Camera refused and the notifications prompt: line 184 "if it is refused, Choose a file stays; notifications are asked for once, after the first claim is submitted".
- Category closed: line 188 "A category closed to the employee's group is not shown ... nor an offer for an item in a closed category".
- Balance used up: line 424 "When the Learning balance is used up, the same screen says so, and its link Why can't I use money from another category? opens H-2.2.2".
- No card issued: line 105 "the Card screen before a card is issued"; line 480 "An employee with no card issued sees the Card tab in the state "Your Perqo card has not been issued yet"".
- Home's Shown later: line 162 "Home shows two of them for each open category, the category and what remains ... The category screen shows the other three".
- Category screen's Shown later: line 366 "the cross-listed far members after them, each naming its home".
- New claim's Shown later: line 367 "shows the rule "Claims over the limit need HR approval", with the group's limit".
- Card offers' Shown later: line 368 "Card offers (A-4.3: offers for items in the open categories, filterable by category ...)".

Notation and tones
- Tone 3 for the app, tone 6 for a stop: line 12 "every app box is tone 3, and tone 6, IA2's stop, marks a state where the path ends without success, or a fault found in a review (IA2, section 5.2)". The legend and the caption agree.
- Tone 6 is used consistently. Every Error cell is tone 6, and so is every Empty cell where the employee cannot go on until something changes: [no category open], [balance used up], [no card issued]. Every Empty cell that offers a route on is tone 3: [no claims], [no purchases], [no offers], [none yet]. Every Permission cell degrades without blocking (line 391: "a permission state degrades without blocking") and is tone 3. Every Shown later cell is tone 3. This fits the caption's "until something changes".
- Conditions in square brackets: line 105 "IA2 reduced to a box whose note opens with the condition in square brackets (IA2, section 5.1)". Every state cell opens with a [condition].
- The unit names no type tags or other marks for this figure, and the figure carries none.

Caption elements
- What it shows: "each Perqo app screen's empty, error and permission states and what it shows later": line 391.
- F2: line 309 "at fidelity F2".
- Decision: "what each screen shows under each condition and by which route the employee goes on": line 156 "what exists where, under what condition, and by which route the person goes on".
- Section: "(Deliverable B, B.5)": line 389.
- "Conditions in square brackets, as IA2's conditional area": line 105.
- "empty-state rule this unit's synthesis from IA3, A3 and F2": line 166 "The rule below is this unit's synthesis from IA3's evidence ... (IA3, A3; Budiu 2020) ... (IA3, F2)".
- "error states from Neusesser and Sunwall, 'Error-Message Guidelines', NN/g, 2023": line 172, and Sources "Neusesser, Tim, and Evan Sunwall. "Error-Message Guidelines". Nielsen Norman Group, 14 May 2023."
- "permissions from Android Developers, 'Request runtime permissions', 2026 (platform documentation)": line 184, and Sources "Android Developers. "Request runtime permissions". Page updated 28 October 2026 (platform documentation ...)".
- "disclosure from Nielsen, 'Progressive Disclosure', NN/g, 2006": line 160, and Sources "Nielsen, Jakob. "Progressive Disclosure". Nielsen Norman Group, 3 December 2006."
- "tone 6 marks a stop ... (IA2, section 5.2)": line 12.
- "Perqo is fictional": line 391 "(Perqo, fictional)".

Legibility by width and theme
- Desktop, light and dark: the whole figure fits in one frame. Every label is whole except finding 1. Nothing overlaps. Dark tones contrast well.
- Tablet, light and dark: the whole figure fits in one frame. Every label is whole except finding 1. Nothing overlaps.
- Phone (390 px), light and dark: the figure takes 4 frames across 372 px of sideways scroll. The row labels stay pinned on the left. Each column can be read in turn: Empty in frame 1, Error in frame 2, Permission in frame 3, Shown later in frame 4. A phone reader can follow it. Every cell is reachable by scrolling. Finding 1 applies here too.

(c) Renderer notes (layout only; none is a FIX)
- The opening frame at every width is clipped at the top by the sticky section bar. On desktop and tablet the Home row and the column headings are hidden under it. The frame sheets show the whole figure.
- On phone, the pinned row-label column takes about 40% of the width, and the Empty column is a little wider than the space left for cells. Its longest lines ("use money from another category?", "[no category open] HR chooses", "back a receipt; New claim") are never wholly visible at one scroll position. At 0 their right ends sit under the right-edge fade; by 164 their left part has passed under the pinned labels. A reader reads them with a small sideways scroll. The longest line ends in H-2.2.2's article title, which cannot be shortened, so no author change would fully fix this.
- On phone the legend scrolls with the figure. Its second item, "a stop: the path ends without success here", is cut across frames 1 and 2, and the left-edge fade dims one letter in frame 2. It is readable by scrolling.
- "cross- / listings," breaks at its own hyphen. That is a normal break, not a cut label.

(d) Figure 5: FIX (minor only). error 0, should-fix 0, minor 2.

Note on persistence: the harness refused the write to D/out/report.md, so this reply is the only copy. I wrote helper crops of the phone frame sheets to D/out/crops/ (inside the packet) for inspection only.

## Figure 8 re-check 2 (Opus 5.5 agent, 3 November 2026; the third check of figure 8, wireflow: submit a claim; given the unit without its figures, the captions and the frames sheets, nothing of the earlier reports; verbatim hand-back; the harness refused its `out/` write, so the hand-back is the one copy)

Figure 8 check: IA6 "Level 2 · the client app", figure 8 (wireflow). Third check, fresh. Packet: /tmp/claude-0/-home-claude/014ca185-e160-5e84-b94e-99ea385f9b58/scratchpad/u6/rc2/fc8

Kind and section: wireflow, in Deliverable C, C.3 "Submit a reimbursement claim". The marker is at line 438 of unit-without-figures.md. The sticky bar in the shots reads "Section 9 of 11 · Deliverable · C · Three core flows as wireflows". The kind fits the data: the figure shows screens, so it should be a wireflow (rule 7). The layout has two screens per row, as line 420 says: "Two screens per row keep each drawing legible on a phone."

(a) Findings

- [error] [label] figure 8, title of the modal screen. Current: `Allow notifications? (modal)`. Problem: the title "Allow notifications?" does not appear anywhere in the unit's text (grep -F -c "Allow notifications" = 0). The text calls this layer "the notifications prompt" (line 400, B.5: "[first claim] the notifications prompt"; line 436: "Done opens the notifications prompt, a modal that either answer closes") and names only its two answers, Allow and Not now. Fix (in the figure): change the screen title to `Notifications prompt (modal)`. Or keep the figure and fix the text: in section 4.4 replace `the prompt says what they are for (get told when a claim is approved, rejected or paid), with Allow and Not now as its two answers` (occurs once) with `the prompt, "Allow notifications?", says what they are for (get told when a claim is approved, rejected or paid), with Allow and Not now as its two answers`. Basis: line 184, line 400, line 436; every frame shows "Allow notifications? (modal)" as the right-hand screen of row 3.
- [minor] [accuracy] caption 8, the source of the screens. Current: `(IA2, section 5.1); wireflow form from Laubheimer, NN/g, 2016. Perqo is fictional.` (occurs once in captions.md). Problem: the caption names the sources of the rule, the notation and the form, but not where the screens come from. Figures 6 and 7, the unit's other two wireflows, both say "screens from Deliverable B", and every screen here is a Deliverable B screen (A-3, A-3.1 to A-3.4) plus the modal from B.5. Fix: `(IA2, section 5.1); wireflow form from Laubheimer, NN/g, 2016; screens from Deliverable B. Perqo is fictional.` Basis: captions.md, lines 11 and 13 against line 15; unit lines 367 and 400.

No should-fix findings. The kind fits, and the caption says what the figure shows and names its section (Deliverable C, C.3) and its rule sources.

(b) Confirmed (each label, number and caption element traced)

Screens and their contents:
- Claims: "Submitted", "Approved", "Rejected", "Paid", "Help with claims", "New claim". Line 367: "A-3 Claims. The four state groups, newest first in each; New claim; Help with claims." Line 436: "Claims lists all four states, with Help with claims."
- New claim: "Category", "Learning balance", "Amount", "Receipt", "Take a photo", "Choose a file", "Claims over the limit need HR approval", "Continue". Line 367: "New claim (A-3.1) asks for a category (open ones only), shows that category's balance, asks for the amount and the receipt (Take a photo, or Choose a file), and shows the rule "Claims over the limit need HR approval"". Line 436: "tap Continue". The Learning example is from line 176 and line 477: "More than your Learning balance" (in the chosen category's name).
- Check and submit: "Category and amount", "Learning balance after", "Edit", "Submit". Line 367: "Check and submit (A-3.2) shows category, amount and the balance after, with Edit and Submit."
- Check and submit [over the balance]: the title. Line 209: "("Check and submit [over the balance]")".
- In that state, "Category and amount", "More than your Learning balance", "Edit". Line 176: "Check and submit therefore shows the state "More than your Learning balance", with Edit as the only route forward". Line 399: "[over the balance] Edit only".
- Claim submitted: "Status: Submitted", "[over the limit] HR decides", "Done". Line 367: "Claim submitted (A-3.3) shows the status Submitted and, for a claim over the limit, that HR decides." Line 436: "on the first claim, Done opens the notifications prompt".
- Modal: "[first claim only]". Line 184: "notifications are asked for once, after the first claim is submitted".
- Modal: "Get told when your claim is approved, rejected or paid". Line 184: "the prompt says what they are for (get told when a claim is approved, rejected or paid)". Line 478 leaves "the prompt's wording beyond its purpose" free.
- Modal: "Allow", "Not now". Line 184: "with Allow and Not now as its two answers".
- Modal: "[either answer closes it]". Line 436: "a modal that either answer closes".
- Claim [Approved]: "Status: Approved", "Amount, category, date submitted", "Receipt". Line 367: "Claim (A-3.4) shows status, amount, category, date submitted and the receipt".
- Claim [Approved]: "Then Paid → see the claim's lifecycle (IA2, section 5.3)". Line 436: "Approved (then Paid, by the lifecycle IA2 drew)".
- Claim [Rejected]: "Status: Rejected", "Rejected by HR, or over the balance", "Why was my claim rejected?". Line 367: "when Rejected, the reason (over the balance, or by HR) and the link Why was my claim rejected?". Line 440: "the Claim screen names that reason".

Arrows:
- "tap New claim", "tap Continue", "tap Edit" (back to New claim), "tap Submit (no way back)". Line 436: "tap New claim, tap Continue, tap Edit back to New claim, and tap Submit with no way back".
- "tap Continue [over the balance]". Line 436: "When the amount is over the category's balance, Continue opens Check and submit in its over-balance state".
- "tap Edit" (from the over-balance state). Line 436: "with Edit as the only route". Line 176: "the form keeps what was entered".
- "[first claim] tap Done". Line 436: "on the first claim, Done opens the notifications prompt".
- "later: tap the notification [approved]" and "later: tap the notification [rejected]". Line 436: "Later, when the claim moves, the notification opens the Claim screen: Approved ... or Rejected". Line 218: "the outcome becomes two states of one Claim screen reached from a notification". Line 382, E-4: "Lands on Claim, A-3.4".
- Each control arrow's label matches a button on the screen it leaves (move 3, line 210): New claim on Claims; Continue on New claim; Edit and Submit on Check and submit; Edit on the over-balance state; Done on Claim submitted. The two "later:" arrows are labelled with a condition outside the app, which line 420 allows: "an arrow is labelled with the action or the condition that moves the person".

Caption elements:
- "extending IA2, section 5.3's claim wireflow (Claims, New claim, Check and submit, Claim submitted; Edit back; Submit with no way back)". Line 436: "This extends IA2's claim wireflow and keeps every screen, label and arrow in it: Claims, New claim, Check and submit and Claim submitted; tap New claim, tap Continue, tap Edit back to New claim, and tap Submit with no way back (IA2, section 5.3)".
- "IA3's B1, B2 and C4 fixes". Line 339: B1 "the chosen category's balance on New claim and on Check and submit | A-1; A-3.1; A-3.2". Line 340: B2 "group Claims by all four states | A-3; the Claim screen (A-3.4) shows the reason when Rejected". Line 344: C4 "the rule on A-3.1".
- "the over-balance state". Line 413: "Check and submit gains a state."
- "the notifications prompt". Line 400 and line 436.
- "the Claim screen's outcomes". Line 412: "A Claim screen is added." Line 436.
- "supports the decision on which screens and states the claim task needs and where it cannot be undone (Deliverable C, C.3)". Line 418: "decision: which screens each core task needs, what changes on them, and where the task can stop".
- "Tone 3 the app; tone 6 a state where the path stops". Line 12: "every app box is tone 3, and tone 6, IA2's stop, marks a state where the path ends without success". In the drawing, the over-balance state and Claim [Rejected] are drawn in tone 6 (olive in light, amber in dark), and every other screen is tone 3 (teal), at every width and theme.
- "The rule from IA2, section 5.3 and IA3, section 2.3". Line 176: "The rule rejects a claim whose amount is over the chosen category's balance (IA2, section 5.3; IA3, section 2.3)".
- "the no-way-back label stands for Garrett's crossbar (IA2, section 5.1)". Line 510: "Garrett, Visual Vocabulary Quick Reference (conditional area, crossbar)".
- "wireflow form from Laubheimer, NN/g, 2016". Line 195 and line 500.
- "Perqo is fictional". Line 12 and passim.

Notation:
- The figure follows line 420: "a frame with a title bar is one screen, bars and blocks are placeholder text and areas, a button is a control, and an arrow is labelled with the action or the condition that moves the person". Every screen is a title-bar frame, placeholders are grey bars or blocks, and controls are outlined buttons in monospace.
- States carry [condition] in the title, as line 420 says: "A screen title with a [condition] is a state of that screen". This applies to Check and submit [over the balance], Claim [Approved] and Claim [Rejected].
- The modal is marked "(modal)", the note word set at line 107.
- "→ see" is used on Claim [Approved], as caption 4 describes the mark.

Legibility, every width and theme:
- Desktop light and dark: the whole figure fits in one frame. Labels are whole and the text is small but readable.
- Tablet light and dark: one frame, clear.
- Phone light and dark: three sideways frames (scroll 134, 298 and 372 px of 372). The left column is whole at the opening frame and the right column is whole in frames 2 and 3, with the hint "scroll sideways for the whole figure". Every label can be reached and read, and a phone reader can follow the flow column by column.
- Dark theme: tone 6 (amber outline, brown title bar) and tone 3 (teal) both keep their contrast, and the arrows and labels are readable.

(c) Renderer notes (no FIX unless an author change would meet them)

- At every width and theme, the vertical line of the "tap Edit" return arrow (from Check and submit [over the balance] up to New claim) runs through the label "tap Continue [over the balance]". It strikes the "p" of "tap", the "[" of "[over the" and the "b" of "balance]". The words stay readable. The overlap comes from the renderer placing two opposite edges between the same pair of screens close together and centring the label on one of them. No shorter label that keeps the meaning is evidently narrow enough to clear the line, so this is not a FIX. Basis: desktop frame 1, tablet frame 1 (around y 1000 to 1070 at 3x), phone frames 2 and 3, light and dark.
- The edges "tap Submit (no way back)" and "later: tap the notification [approved]" leave their source screen at one x and arrive at another. The bend is hidden behind the label, so the line looks broken around the label. It is a layout effect and harmless.
- On desktop and tablet, the opening frame (not the scroll sheet) is cut across the row-1/row-2 arrows by the sticky header and section bar. The sheet shows the whole figure.
- The phone opening frame is clipped on the right: New claim, the over-balance state, the modal and Claim [Rejected] are cut at the screen edge. All of them can be reached by sideways scroll (frames 2 and 3). This comes from the two-per-row layout the text sets at line 420.

(d) Figure 8: FIX. 1 error, 0 should-fix, 1 minor.

## Figure 4 re-check 3 (Opus 5.5 agent, 3 November 2026; the fourth check of figure 4, sitemap: the app map; given the unit without its figures, the captions and the frames sheets, nothing of the earlier reports; verbatim hand-back; the harness refused its `out/` write, so the hand-back is the one copy)

Figure 4 (sitemap) in IA6 passes: no error, no should-fix, two minor findings. One is a wording mismatch in the unit's text; the other is an optional addition to one box's note.

# Figure check 4 · IA6 figure 4 (sitemap)

Kind: sitemap. Section: Deliverable B, B.3 "The map" (the figure's marker is at unit line 360).

## (a) Findings

- [minor] [accuracy] Deliverable B, B.3, paragraph before the figure; Current: `its children are the sign-in screens and the five tabs`; Problem: the figure's root has six children: one section box, "Join and sign in" (SECTION, A-0 · [signed out]), plus the five tabs. The sign-in screens Join (A-0.1) and Sign in (A-0.2) are one level down, under A-0, not children of the root, so the text and the drawing disagree about the level. Line 364 ("A-0 Join and sign in") is right; Fix: `its children are Join and sign in (A-0), which holds the two sign-in screens, and the five tabs`; Basis: unit line 358; tablet light sheet, top row (root → SECTION Join and sign in → FORM Join, FORM Sign in). `grep -F -c` returns 1.
- [minor] [label] figure 4, box "Purchase"; Current (the note as the reader sees it): `A-4.2.1 · merchant, amount, date, category`; Problem: the text gives the Purchase screen five contents and the note shows four. It leaves out "the category's balance after", the one attribute that ties a purchase to the allocation (the join IA8 takes). This is an omission, not an untraced label; Fix (note field): `A-4.2.1 · merchant, amount, date, category; balance after`; Basis: unit line 368 "each Purchase (A-4.2.1: merchant, amount, date, category and the category's balance after)" (`grep -F -c` returns 1); A.2 row, line 299, "on the purchase, the category's balance after".

Every label, ID and number in the figure traces to the unit's text (part b). The caption says what the figure shows, names its section (Deliverable B) and gives the sources. The kind fits: a hierarchy of screens under tabs is drawn as a sitemap.

## (b) Confirmed

Root and level 1
- "Perqo app" / "tab bar: the global routes; entries in B.4": line 358 "The root is the surface, since the tab bar is not a screen"; line 102 "Global routes | header and footer | the tab bar"; line 373 "### B.4 · Entry points and addresses".
- SECTION "Join and sign in" / "A-0 · [signed out]": line 364 "**A-0 Join and sign in.**" and "Sign in (A-0.2) is for an employee who has joined and is signed out"; line 379 "Sign in, A-0.2, when signed out".
- HOME "Home" / "A-1 · entry: opening the app": line 379 "E-1 | Opening the app | the phone | Home, A-1".
- INDEX "Benefits" / "A-2 · the four categories only; each category, entry: a link": line 341 "Benefits holds the four categories only"; line 366 "The four categories open to the employee's group, nothing else"; line 384 "E-6 | A link to a category | ... | the category screen".
- INDEX "Claims" / "A-3 · Submitted, Approved, Rejected, Paid; newest first": line 321 "Submitted, Approved, Rejected, Paid, newest first in each".
- SECTION "Card" / "A-4 · [no card issued] not issued yet": line 190 "the Card tab in the state "Your Perqo card has not been issued yet""; line 401 "[no card issued] not issued yet".
- SECTION "Account" / "A-5": line 369 "**A-5 Account.**"; line 326 "Account holds Profile, Notifications and Help".
- The five tabs: line 354 "the five tabs Home, Benefits, Claims, Card and Account".

Under Join and sign in
- FORM "Join" / "A-0.1 · entry: HR's invitation": line 364 "Join (A-0.1) opens from HR's invitation"; line 380, E-2.
- FORM "Sign in" / "A-0.2 · entry: opening the app, signed out": line 379 "Sign in, A-0.2, when signed out".

Under Home
- DETAIL "Balance" / "on Home: each open category and what remains → see A-2.1 to A-2.4": line 365 "Balance: each open category with what remains, each opening its category screen".
- EXTERNAL "Your balance explained" / "→ see H-2.2.1": line 323 "the link opens H-2.2.1"; line 336 "Your balance explained → H-2.2.1".
- INDEX "Recent activity" / "on Home: purchases and claims, newest first; Submitted": line 365 "Recent activity, the latest purchases and claims mixed, newest first, with claim statuses in the Claims words (Submitted, never Pending)".
- FORM "New claim" / "on Home: a button → see A-3.1": line 322 "a button with the text New claim on Home, on Claims and on each category screen, all opening A-3.1".

Under Benefits
- DETAIL "Health" / "A-2.1 · Fitness: gym membership, yoga class, swimming pool entry; Therapy: therapy session; also: bike helmet, covered under Mobility (assumed)": line 358 "under Health, gym membership, yoga class and swimming pool entry (Fitness) and therapy session (Therapy)"; line 343 "bike helmet in Health, each "covered under" its home, marked assumed (IA4, R6)".
- DETAIL "Learning" / "A-2.2 · Courses: coding course, cookery course; Books: book; also: yoga class, covered under Health (assumed)": line 358 "under Learning, coding course and cookery course (Courses) and book (Books)"; line 343 "yoga class in Learning"; line 366 "("Yoga class: covered under Health")".
- DETAIL "Mobility" / "A-2.3 · Public transport: train pass; Bike: bike helmet, bike repair": line 358 "under Mobility, train pass (Public transport) and bike helmet and bike repair (Bike)".
- DETAIL "Meals" / "A-2.4 · Restaurants: restaurant meal; Groceries: groceries; also: cookery course, covered under Learning (assumed)": line 358 "under Meals, restaurant meal (Restaurants) and groceries (Groceries)"; line 343 "cookery course in Meals".
- The four boxes hold twelve items: line 358 "BI-001 to BI-012"; line 473 "all twelve sample catalogue items".
- EXTERNAL "What you can claim in each category" / "on each category screen → see H-2.1.3": line 366 "the link What you can claim in each category (H-2.1.3)".

Under Claims
- FORM "New claim" / "A-3.1 · entry: a Help centre link · Claims over the limit need HR approval": line 383 "E-5 | A link from a Help centre article | ... | New claim, A-3.1"; line 367 "shows the rule "Claims over the limit need HR approval"".
- EXTERNAL "How approval rules work" / "→ see H-1.2.5" (under New claim): line 325 "on New claim, with a link to How approval rules work, H-1.2.5".
- FORM "Check and submit" / "A-3.2 · after A-3.1 · [over the balance] Edit only": line 399 "Check and submit, A-3.2 | none | [over the balance] Edit only"; line 129 (the staged sequence).
- DETAIL "Claim submitted" / "A-3.3 · after A-3.2 · [first claim] modal: the notifications prompt": line 400 "Claim submitted, A-3.3 | none | none | [first claim] the notifications prompt"; line 436 "Done opens the notifications prompt, a modal that either answer closes".
- DETAIL "Claim" / "A-3.4 · entry: a notification · [Rejected] the reason": line 382 "E-4 | A notification about a claim | ... | Claim, A-3.4"; line 367 "when Rejected, the reason (over the balance, or by HR)".
- EXTERNAL "Help with claims" / "→ see H-2.1": line 367 "New claim; Help with claims"; line 237 "Help with claims (H-2.1)".

Under Card
- DETAIL "Card details" / "A-4.1 · last four digits; status, Active or Frozen": line 368 "Card details (A-4.1: the last four digits and the status, Active or Frozen".
- INDEX "Purchases" / "A-4.2 · newest first": line 368 "Purchases (A-4.2, newest first)".
- DETAIL "Purchase" / "A-4.2.1 · merchant, amount, date, category": line 368. The fifth attribute is missing (finding 2).
- INDEX "Card offers" / "A-4.3 · entry: a link, filtered · filter by category": line 385 "E-7 | A link to offers in a category | ... | Card offers, filtered"; line 368 "filterable by category".
- FORM "Freeze card" / "A-4.4 · modal: confirm; Unfreeze card when Frozen": line 368 "Freeze card (A-4.4: a modal asks to confirm; on a Frozen card the action reads Unfreeze card)".
- EXTERNAL "Where you can pay with the Perqo card" / "→ see H-2.3.2" and EXTERNAL "Freezing and unfreezing your card" / "→ see H-2.3.1": line 368 "Links Where you can pay with the Perqo card (H-2.3.2) and Freezing and unfreezing your card (H-2.3.1) sit on Card".

Under Account
- DETAIL "Profile" / "A-5.1": line 469 "A-5.1 Profile".
- INDEX "Notifications" / "A-5.2 · each opens its claim": line 469 "A-5.2 Notifications"; line 369 "Notifications (each about one claim and opening it".
- EXTERNAL "Help" / "→ see H-2 For employees": line 324 "Account's Help opens H-2, perqo.com/help/employees"; line 369 "Help (For employees)".

Screen IDs
- The screen IDs drawn are exactly the set in line 469: A-0, A-0.1, A-0.2, A-1, A-2, A-2.1 to A-2.4, A-3, A-3.1 to A-3.4, A-4, A-4.1, A-4.2, A-4.2.1, A-4.3, A-4.4, A-5, A-5.1, A-5.2.
- Elements on Home and external routes carry no ID. That fits line 107 (IDs are for screens) and the caption's "identifier on every screen".
- Every default-state external route the text names is drawn: H-2.2.1, H-2.1.3, H-1.2.5, H-2.1, H-2.3.2, H-2.3.1, H-2.
- Routes that appear only in a state (H-2.1.1, H-2.2.2, H-2.1.2) are left to B.5 and the A-3.4 bullet, as line 358 says.

Notation
- Type tags shown: SECTION, HOME, INDEX, DETAIL, FORM, EXTERNAL, all within line 107 "The type tags stay IA2's eight".
- Note words, as defined in line 107 and the section 2 table (lines 99 to 101):
  - "modal": A-3.3, A-4.4.
  - "entry:": A-0.1, A-0.2, A-1, A-2, A-3.1, A-3.4, A-4.3.
  - "on Home": Balance, Recent activity, New claim.
  - [condition]: [signed out], [over the balance], [first claim], [Rejected], [no card issued].
- "→ see" with a screen ID (Balance → A-2.1 to A-2.4; New claim on Home → A-3.1), and "→ see" with an H- ID on every EXTERNAL box, as the caption describes.
- Tone: every box is drawn in one tone, tone 3 (teal on pale in light, teal on dark in dark). This matches line 12 "every app box is tone 3" and line 358 "every box tone 3, the app". The external boxes are routes from the app (tagged external), not the perqo.com pages themselves, so tone 3 agrees with the caption. Figure 6 draws the articles themselves in tone 1.

Caption elements
- What it shows, "App map: the Perqo app as designed (to-be), F2 with an identifier on every screen, page types tagged": line 309 "the to-be for IA3's as-is navigation, at fidelity F2 with F3's identifiers on every screen"; line 311.
- Decision and section, "(Deliverable B)": line 309 "decision: what screens the app has, under which tab, in which states, with which modals, and by which ways in".
- "Every box is tone 3, the app": line 358.
- "words added in section 2 under IA2's rule 'Keep the notation; extend the legend' (IA2, section 4)": line 107.
- "Routes that leave the app from a screen's default state are tagged external with '→ see' their Help centre page": line 358.
- "Check and submit and Claim submitted follow New claim in a staged sequence; all three are screens under Claims (section 3.3)": line 129.
- "Cross-listings marked assumed follow IA4, rule R6": line 343 "marked assumed (IA4, R6)".
- Sources:
  - The tabs and categories, from IA1: line 63 (IA1, section 5). New claim, Check and submit and Claim submitted, from IA2: line 354 (IA2's labels).
  - IA3's fixes: line 330 (B.2).
  - IA4's objects and catalogue items: line 358 "(IA4, Deliverable B, B.3)".
  - IA5's Help centre pages: line 323.
  - "Perqo is fictional": stated throughout.

Kind
- A hierarchy of screens under tabs, so sitemap is the right kind (rule 7: "a hierarchy: tree or sitemap").

Legibility
- Desktop, light and dark: the whole figure fits in one frame. All 36 boxes are whole, none overlap, and the connector lines are clear. The text is small at this width but whole and readable.
- Tablet, light and dark: the whole figure fits in one frame. Every label is sharp and whole, and the connector lines show in both themes.
- Phone (390 px), light and dark: the figure scrolls sideways across three frames (at 68, 232 and 372 of 372 px), with "scroll sideways for the whole figure" under the drawing.
  - Each column is whole in at least one frame: the left column (Join and sign in; Claims and its children) at 68, the middle column (Home; Card and its children, with Purchase indented) at 232, the right column (Benefits, the four categories, What you can claim; Account and its children) at 372.
  - Text cut at a frame edge is whole in another frame. Nothing overlaps, and contrast holds in both themes.
  - A phone reader can follow it: each tab's children run straight down one column.

## (c) Renderer notes (layout only, not a FIX)

- The sitemap wraps the root's six children into two rows of three by width: Join and sign in, Home, Benefits; then Claims, Card, Account. The second row is not a second level: all six hang from the same trunk under "Perqo app".
  - On phone and tablet, the long Benefits column pushes the second row far down, so Claims, Card and Account can look as if they sit below Benefits. The trunk line on the left shows their real parent.
  - Changing per_row would not change this much. The author need do nothing.
- The phone frame opens at 68 px, not at the drawing's start (0). The left trunk and the Join and sign in column are still whole at that position.
- At the right edge of the phone viewport, boxes cut by the edge fade out. This is the renderer's scroll cue, and those boxes are whole in the next frame.
- In the desktop opening frame, the sticky section bar ("SECTION 8 OF 11 · Deliverable · B · The Perqo app map") clips the figure around the Mobility box. The frames sheet shows the whole figure without it.

## (d) Verdict

Figure 4: PASS. 0 error, 0 should-fix, 2 minor (one on the unit's text, one optional addition to a note).

The harness refused the write to D/out/report.md, so this reply is the only copy. My image crops are in /tmp/claude-0/-home-claude/014ca185-e160-5e84-b94e-99ea385f9b58/scratchpad/u6/rc3/fc4/out/crops/.

## Figure 5 re-check 3 (Opus 5.5 agent, 3 November 2026; the fourth check of figure 5, matrix: screen states; given the unit without its figures, the captions and the frames sheets, nothing of the earlier reports; verbatim hand-back; the harness refused its `out/` write, so the hand-back is the one copy)

IA6 · figure 5 (matrix) · fresh figure check 4

Figure 5: kind matrix; section Deliverable B, B.5 · Screen states (placed at line 406, directly under B.5's table). Kind fits: screens (items) by four state types (sections) is "items by sections: matrix". All 10 row labels, 4 column heads and 26 filled cells trace word for word to B.5's table; the 14 blank cells are exactly the 14 "none" cells of that table. Caption names what it shows, the section and every source. Tones as the unit and caption name them. Legible at every width and theme, with the phone reader scrolling sideways under a sticky row-label column.

(a) Findings

1. minor · accuracy · captions.md, figure 5 caption, and B.5 lead sentence. Current (caption): `Screen states: each Perqo app screen's empty, error and permission states and what it shows later, F2;` Current (unit, grep -F -c = 1): `The states each screen can be in, by the four decisions of section 4 (Perqo, fictional).` Problem: the matrix has 10 rows, but the map (B.3) has more screens. Join A-0.1, Sign in A-0.2, Benefits A-2, Claim A-3.4, Card details A-4.1, Purchase A-4.2.1, Freeze card A-4.4, Account A-5 and Profile A-5.1 are not in it. "each screen" and "each Perqo app screen's" claim more than the figure and table show. (A-3.4's Rejected state is deliberately elsewhere, per B.3. Whether Benefits A-2 has a [no category open] state of its own is for the author to decide; if it does, it belongs in the table and the figure.) Fix (caption): `Screen states: the empty, error and permission states of the Perqo app screens that have them, and what each shows later, F2;` Fix (unit): `The states of each screen that has one, by the four decisions of section 4 (Perqo, fictional); a screen with none is left out.` Basis: captions.md line 9; unit lines 364-369 (the screens of B.3) against lines 395-404 (the 10 rows).

2. minor · accuracy · B.5 lead sentence, the definition of the column SHOWN LATER. Current (grep -F -c = 1): `"shown later" is what progressive disclosure keeps one level down.` Problem: 3 of the 9 filled SHOWN LATER cells are on the same screen, not one level down:
- Category screen: "cross-listings, after the home items" (line 366: they come after the home items, on the category screen).
- New claim: "the limit, in the rule line" (line 367: the rule line is on New claim).
- Card offers: "the filter by category" (line 368: Card offers is "filterable by category").
The column header in the figure takes its meaning from this sentence. Fix: `"shown later" is what progressive disclosure keeps back: one level down, or below the screen's first content.` Basis: unit lines 391, 396, 398, 403, 366-368; figure column SHOWN LATER, rows Category screen, New claim and Card offers (every frame).

3. minor · label · figure row labels. Current (figure rows): `Home`, `Category screen`, `Claims`, `New claim`, `Check and submit`, `Claim submitted`, `Card`, `Purchases`, `Card offers`, `Notifications`. Problem: B.5's table gives every row its screen ID ("Home, A-1" … "Notifications, A-5.2"). Deliverable B is "at fidelity F2 with F3's identifiers on every screen" (line 309), and figure 4 carries the IDs. The matrix drops them, so a reader cannot join a row to the map by ID. "Category screen" stands for four screens and "Card" could be read as Card details. This is optional: every label as drawn does trace to the text. Fix (row labels as the reader would see them): `Home, A-1`, `Category screen, A-2.1 to A-2.4`, `Claims, A-3`, `New claim, A-3.1`, `Check and submit, A-3.2`, `Claim submitted, A-3.3`, `Card, A-4`, `Purchases, A-4.2`, `Card offers, A-4.3`, `Notifications, A-5.2`. The rows are already two to four lines tall, so the wrapped labels fit the phone's sticky column without new rows. Basis: unit lines 309, 395-404.

No error. No should-fix.

(b) Confirmed

Kind and place
- Kind matrix, items (screens) by sections (state types): fits the rule.
- Placed in Deliverable B, B.5: line 406, `[Figure 5 (matrix) is drawn here ...]`, under `### B.5 · Screen states` (line 389).

Column heads
- EMPTY, ERROR, PERMISSION, SHOWN LATER: line 393, `| Screen | Empty | Error | Permission | Shown later |`.

Row labels
- Home: line 395, `| Home, A-1 |`.
- Category screen: line 396, `| Category screen, A-2.1 to A-2.4 |`.
- Claims: line 397, `| Claims, A-3 |`.
- New claim: line 398, `| New claim, A-3.1 |`.
- Check and submit: line 399, `| Check and submit, A-3.2 |`.
- Claim submitted: line 400, `| Claim submitted, A-3.3 |`.
- Card: line 401, `| Card, A-4 |`.
- Purchases: line 402, `| Purchases, A-4.2 |`.
- Card offers: line 403, `| Card offers, A-4.3 |`.
- Notifications: line 404, `| Notifications, A-5.2 |`.

Cells (each traced to B.5's table and, where noted, to section 4)
- Home, empty, "[no category open] HR chooses the open categories; Help": line 395. Also line 168, "Home in a group with no category open says that the employer's HR team chooses which categories are open, and links to Help".
- Home, error, "[no connection] the last balances, with their time": line 395. Also line 177, "Home shows the last balances it loaded, with the time they were loaded".
- Home, shown later, "spent, amount and period, on the category screen": line 395. Also line 162, "Home shows two of them ... The category screen shows the other three".
- Category screen, empty, "[balance used up] no balance left this period; Why can't I use money from another category?": line 396. The article title is also at line 234, "Why can't I use money from another category?, H-2.2.2".
- Category screen, permission, "[category closed] not shown": line 396. Also line 188, "A category closed to the employee's group is not shown".
- Category screen, shown later, "cross-listings, after the home items": line 396. Also line 366, "the cross-listed far members after them".
- Claims, empty, "[no claims] How to claim back a receipt; New claim": line 397. Also line 168, `links to "How to claim back a receipt" (H-2.1.1) and offers New claim`.
- Claims, error, "[no connection] the last list, with its time": line 397. Also line 177, "Claims and Purchases show their last lists the same way".
- Claims, shown later, "the claim, on tap": line 397.
- New claim, error, "[receipt missing] by the Receipt field; input kept": line 398. Also line 178, "The message sits by the Receipt field on New claim, and the amount and category stay as entered".
- New claim, permission, "[camera refused] Choose a file": line 398. Also line 184, "if it is refused, Choose a file stays".
- New claim, shown later, "the limit, in the rule line": line 398. Also line 189.
- Check and submit, error, "[over the balance] Edit only": line 399. Also line 176, "with Edit as the only route forward".
- Claim submitted, permission, "[first claim] the notifications prompt": line 400. Also line 184, "notifications are asked for once, after the first claim is submitted".
- Card, empty, "[no card issued] not issued yet; claims still work": line 401. Also line 190, "Your Perqo card has not been issued yet", with claims still open to them.
- Card, shown later, "card details, on tap": line 401.
- Purchases, empty, "[no purchases] Where you can pay with the Perqo card": line 402. The article title is also at line 239.
- Purchases, error, "[no connection] the last list, with its time": line 402.
- Purchases, shown later, "the purchase, on tap": line 402.
- Card offers, empty, "[no offers] the route is hidden": line 403. Also line 168, "appears on the Meals screen only when Meals has an offer (R5)".
- Card offers, permission, "[category closed] its offers not shown": line 403. Also line 188, "nor an offer for an item in a closed category".
- Card offers, shown later, "the filter by category": line 403.
- Notifications, empty, "[none yet] what will appear here": line 404.
- Notifications, permission, "[not allowed] how to allow notifications": line 404.
- Notifications, shown later, "the claim, on tap": line 404.

Blank cells
- All 14 blank cells match the 14 "none" cells of lines 395-404:
  - Home: permission.
  - Category screen: error.
  - Claims: permission.
  - New claim: empty.
  - Check and submit: empty, permission and shown later.
  - Claim submitted: empty, error and shown later.
  - Card: error and permission.
  - Purchases: permission.
  - Card offers: error.
  - Notifications: error.

Tones
- Rows tone 3: line 12, "every app box is tone 3".
- Tone 6 is a stop: line 12, "tone 6, IA2's stop, marks a state where the path ends without success, or a fault found in a review (IA2, section 5.2)".
- The 8 tone 6 cells are each a state that stops the path until something changes:
  - [no category open]
  - [balance used up]
  - [no card issued]
  - three [no connection] cells (Home, Claims, Purchases)
  - [receipt missing]
  - [over the balance]
- The tone 3 states each go on by a route or degrade (line 184, "Don't block the user"; line 166, an empty state names "the route to the next step"):
  - [no claims], [no purchases], [no offers], [none yet]
  - [category closed] (twice), [camera refused], [first claim], [not allowed]
- Legend: "tone 3 the Perqo app" and "tone 6 a stop: the path ends without success here" agree with line 12 and the caption.

Caption elements
- "F2": line 309, "at fidelity F2".
- "Deliverable B, B.5": lines 307 and 389.
- "Conditions in square brackets, as IA2's conditional area": line 105, "IA2 reduced to a box whose note opens with the condition in square brackets (IA2, section 5.1)".
- "empty-state rule this unit's synthesis from IA3, A3 and F2": line 166, "The rule below is this unit's synthesis from IA3's evidence ... (IA3, A3; Budiu 2020) ... (IA3, F2)".
- "Neusesser and Sunwall, 'Error-Message Guidelines', NN/g, 2023": lines 172 and 502.
- "Android Developers, 'Request runtime permissions', 2026 (platform documentation)": lines 184 and 493.
- "Nielsen, 'Progressive Disclosure', NN/g, 2006": lines 46, 160 and 504.
- "(IA2, section 5.2)" for the stop: line 12.
- "Blank cells: none, as in B.5's table": lines 395-404.
- "Perqo is fictional": line 391, "(Perqo, fictional)".

Legibility, as the reader sees it
- Desktop, dark and light: the whole figure fits in one frame. Every label is whole and nothing overlaps; each cell's text sits inside its cell. Tone 3 and tone 6 are distinct in both themes, and the blank cells read as empty grey.
- Tablet, dark and light: the whole figure fits in one frame. Labels whole, no overlap, both tones distinct in both themes.
- Phone, dark and light: 4 frames across 372 px of sideways scroll, marked "scroll sideways for the whole figure". The row-label column stays sticky, so the screen name stays in view while the reader crosses EMPTY, ERROR, PERMISSION and SHOWN LATER. Every cell is read whole in at least one frame:
  - EMPTY in frame 1.
  - ERROR in frame 2.
  - PERMISSION in frame 3.
  - SHOWN LATER in frame 4.
  A phone reader can follow it.

Notation
- The figure is drawn as the unit and caption name it: [condition] in square brackets opens each state cell, rows are tone 3, stops are tone 6, and the legend names both tones.
- No type tags are named for this figure and none are drawn, which is right for a matrix.

(c) Renderer notes (layout only; not FIX)
- Desktop and tablet opening frames: the sticky section bar covers the column heads and the Home row, and the Category screen row's top line is clipped. The frame sheets show that the whole figure fits once scrolled. Nothing for the author to change.
- Phone opening frame: the column head EMPTY and the Home row sit above and under the sticky header and section bar. The frame sheet shows them whole at scroll 0. Renderer layout.
- Phone legend: the legend scrolls inside the sideways scroller. In frame 1 "a stop: the path ends …" is cut at the right edge. In frame 2, the faded right edge of the sticky row-label column overlays one letter, so it reads "the pa h ends without success here" in both themes. The whole text is readable across frames 1-2, and the meaning is repeated in the caption. This is a renderer effect (legend inside the scroller, sticky column fade); a change to the unit's text cannot fix it.
- Phone: the SHOWN LATER header is cut ("SHOWN LA") in frame 3 and whole in frame 4. This is scroll position only.

(d) Figure 5: PASS. 0 error, 0 should-fix, 3 minor (two on the caption's and B.5's own wording, one optional set of row labels).

Note: the harness refused the write to D/out/report.md; this reply is the only copy. Phone frame sheets were cropped for reading into D/out/crops/ (phone-dark-0..3.png, phone-light-0..3.png).

## Figure 8 re-check 3 (Opus 5.5 agent, 3 November 2026; the fourth check of figure 8, wireflow: submit a claim; given the unit without its figures, the captions and the frames sheets, nothing of the earlier reports; verbatim hand-back; the harness refused its `out/` write, so the hand-back is the one copy)

IA6 · Level 2 · the client app: figure 8 (wireflow), fresh check 4

Figure: 8, kind wireflow, in Deliverable C, section C.3 "Submit a reimbursement claim" (marker at line 438 of D/unit-without-figures.md). The kind fits: the data is a set of screens, so the wireflow is the right kind.

(a) Findings

- [minor] [accuracy] Deliverable C intro, line 420; Current: `Two screens per row keep each drawing legible on a phone.`; Problem: at 390 px the two-column drawing does not fit the phone. A reader sees about one and a half screens and has to scroll sideways. The phone frames show the scroll range ("scrolled to 134 of 372 px; opens at 134") and the renderer's hint "scroll sideways for the whole figure". The drawing is legible at full type size, but only by scrolling, and the sentence does not say so; Fix: `Two screens per row keep each drawing legible on a phone, scrolled sideways.`; Basis: phone-read-ux-ia6-fig-08-wireflow-frames-light.png and -dark.png, frames 1 to 3.

No error or should-fix findings. Every label traces to the text, the caption is complete, and the kind fits.

(b) Confirmed (each label, number and caption element traced; quotes are from D/unit-without-figures.md)

Screens and their content
- Claims, with Submitted, Approved, Rejected, Paid: line 436, "Claims lists all four states, with Help with claims."; line 321, "Submitted, Approved, Rejected, Paid, newest first in each".
- Help with claims (button on Claims): line 436, "Claims lists all four states, with Help with claims."
- New claim (button on Claims): line 367, "A-3 Claims. The four state groups, newest first in each; New claim; Help with claims."
- New claim screen, Category / Learning balance / Amount / Receipt / rule, in that order: line 297, "New claim: category, the category's balance, amount, receipt, the rule"; line 436, "New claim shows the chosen category's balance, two ways to add the receipt, and the rule".
- "Learning" as the example category: line 176, "shows the state "More than your Learning balance"".
- Take a photo / Choose a file: line 367, "asks for the amount and the receipt (Take a photo, or Choose a file)"; line 218, "the camera branch becomes two buttons on New claim".
- "Claims over the limit need HR approval": line 436, "and the rule "Claims over the limit need HR approval"".
- Continue: line 436, "tap New claim, tap Continue, tap Edit back to New claim, and tap Submit with no way back".
- Check and submit, with Category and amount / Learning balance after / Edit / Submit: line 367, "Check and submit (A-3.2) shows category, amount and the balance after, with Edit and Submit."; line 297, "Check and submit: category, amount, balance after".
- Check and submit [over the balance], with Category and amount / More than your Learning balance / Edit only: line 209, "("Check and submit [over the balance]")"; line 176, "Check and submit therefore shows the state "More than your Learning balance", with Edit as the only route forward"; line 436, "Continue opens Check and submit in its over-balance state, with Edit as the only route."
- Claim submitted, with Status: Submitted / [over the limit] HR decides / Done: line 367, "Claim submitted (A-3.3) shows the status Submitted and, for a claim over the limit, that HR decides."; line 436, "on the first claim, Done opens the notifications prompt".
- Notifications prompt (modal), with [first claim only] / Get told when your claim is approved, rejected or paid / Allow / Not now / [either answer closes it]: line 436, "Done opens the notifications prompt, a modal that either answer closes"; line 184, "notifications are asked for once, after the first claim is submitted ... (get told when a claim is approved, rejected or paid), with Allow and Not now as its two answers".
- Claim [Approved], with Status: Approved / Amount, category, date submitted / Receipt / Then Paid → see the claim's lifecycle (IA2, section 5.3): line 367, "Claim (A-3.4) shows status, amount, category, date submitted and the receipt"; line 436, "Approved (then Paid, by the lifecycle IA2 drew)".
- Claim [Rejected], with Status: Rejected / Rejected by HR, or over the balance / Why was my claim rejected?: line 367, "when Rejected, the reason (over the balance, or by HR) and the link Why was my claim rejected?"; line 436, "or Rejected with its reason and the link Why was my claim rejected?".
- The two Claim states: line 218, "the outcome becomes two states of one Claim screen reached from a notification".

Arrows
- tap New claim; tap Continue; tap Edit (from Check and submit); tap Submit (no way back): line 436, "tap New claim, tap Continue, tap Edit back to New claim, and tap Submit with no way back (IA2, section 5.3)".
- tap Continue [over the balance]; tap Edit (from the over-balance state): line 436, "When the amount is over the category's balance, Continue opens Check and submit in its over-balance state, with Edit as the only route."
- [first claim] tap Done: line 436, "on the first claim, Done opens the notifications prompt".
- later: tap the notification [approved] / [rejected]: line 436, "Later, when the claim moves, the notification opens the Claim screen: Approved ... or Rejected"; line 382, E-4, "A notification about a claim ... Claim, A-3.4".

Notation
- A frame with a title bar is a screen, bars are placeholders, buttons are controls, arrows carry labels, and a bracketed title is a state: line 420, "a frame with a title bar is one screen, bars and blocks are placeholder text and areas, a button is a control, and an arrow is labelled with the action or the condition that moves the person ... A screen title with a [condition] is a state of that screen." All of these appear in every shot.
- Tone 3 for every app screen, including the modal: line 12, "every app box is tone 3". The teal frames and headers match.
- Tone 6 on the over-balance state and on Claim [Rejected]: line 12, "tone 6, IA2's stop, marks a state where the path ends without success". The olive/amber frames and headers match. No other tone is used, and the caption names only tones 3 and 6.

Caption elements
- What the figure shows: "an employee submits a reimbursement claim in the Perqo app, F2". Line 434 is the C.3 heading; line 418, "three wireflows of the Perqo app, at fidelity F2".
- "extending IA2, section 5.3's claim wireflow (Claims, New claim, Check and submit, Claim submitted; Edit back; Submit with no way back)": line 436, "This extends IA2's claim wireflow and keeps every screen, label and arrow in it".
- "with IA3's B1, B2 and C4 fixes": line 339, "B1 | ... the chosen category's balance on New claim and on Check and submit | A-1; A-3.1; A-3.2"; line 340, "B2 | group Claims by all four states | A-3; the Claim screen (A-3.4) shows the reason when Rejected"; line 344, C4, "the rule on A-3.1". All three are drawn.
- "the over-balance state, the notifications prompt and the Claim screen's outcomes": line 436, as quoted above.
- Decision and section, "(Deliverable C, C.3)": line 418, "decision: which screens each core task needs, what changes on them, and where the task can stop".
- Tones: "Tone 3 the app; tone 6 a state where the path stops": line 12.
- Sources: "The rule from IA2, section 5.3 and IA3, section 2.3": line 176, "(IA2, section 5.3; IA3, section 2.3)".
- "the no-way-back label stands for Garrett's crossbar (IA2, section 5.1)": line 510, "Garrett, *Visual Vocabulary Quick Reference* (conditional area, crossbar)"; line 105, "(IA2, section 5.1)".
- "wireflow form from Laubheimer, NN/g, 2016": lines 195 and 500.
- "screens from Deliverable B": line 367 (B.3).
- "Perqo is fictional": line 418.

(c) Renderer notes (layout only; none of them is a FIX)

- Struck-through, misplaced arrow label (all widths, both themes). The label "tap Continue [over the balance]" sits to the right of the vertical Edit edge that returns from Check and submit [over the balance] to New claim. That edge runs through the label's left edge: through the "p" of "tap", the "[" of "[over" and the "b" of "balance". The arrow the label belongs to, the downward edge into the over-balance state, is to the left of the Edit edge. A reader can still match it by its text, because the destination's title repeats "[over the balance]", but the label reads as if it belonged to the Edit edge. The cause is where the renderer puts labels on parallel vertical edges. No author change I can verify would fix it: a shorter label still starts where the edge crosses, since the first line "tap Continue" is the one struck. The fix belongs in the renderer's label offset. Basis: the tablet crops of both themes; the desktop light and dark frame 1 at around x 495–530, y 360–390; phone frame 2 of both themes.
- Desktop and tablet: the whole figure fits in one frame. In the opening frame the sticky section bar covers the lower part of the Check and submit row; it is clear in the frames sheet.
- Phone, 390 px: the drawing is wider than the viewport. It opens at 134 of 372 px, with the left column whole and the right column cut, and shows "scroll sideways for the whole figure". Frames 2 and 3 show the right column whole: New claim, Check and submit [over the balance], Notifications prompt, Claim [Rejected]. Every label can be scrolled to, and the type is at full size, so a phone reader can follow the figure. The sticky bar clips the opening frame across the Claim submitted / Notifications row.
- Dark and light: frames, tone 6 headers, placeholder bars and arrow labels are all legible in both. Arrow labels are mid-grey in dark and still readable.

(d) Figure 8: PASS. 0 error, 0 should-fix, 1 minor (a text note on line 420), plus 1 renderer legibility note (the struck "tap Continue [over the balance]" label), which is not a FIX.
