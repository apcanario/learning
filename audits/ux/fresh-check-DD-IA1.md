---
audit: fresh check
unit: DD-IA1 · Deep dive: five information architectures read closely
course: ux · IA · Information Architecture
model: Fable 5.2 (claude-fable-5-2, confirmed from the agent's transcript; live search). The session's "fable" model is Fable 5.2, not the Fable 5.1 method §4 names, so by the rule as written a Fable 5.1 fresh check of DD-IA1 is owed to the Fable stage (P49)
date: 2026-11-10
chat: own Fable 5.2 agent context, not shown the writing (P31), launched by the U-13 chat (Opus 5.5 as the orchestrating chat; the writer ran on Opus 5.5) in session https://claude.ai/code/session_01KMmgR2s9DAyAaZMK4k4ay4
verdict: fix · 2 error, 12 should-fix, 20 minor
---

The checker's final report, verbatim: its hand-back message, extracted by script from its transcript (the `SubagentHandback` call). The harness refused its one write to `out/report.md`, so the hand-back is the record. It checked an exact copy of the unit as committed at 3d3b4ab (sha256 2897b00221358d45ef13a9c99700718641e7206381d44f6d1a70681f8ecaf9ad, two copies, confirmed by the checker at its start and end). Transcript checks (U-13 chat): no tool named `mcp__*`, Projects, Artifact, connector or Agent; 32 searches and 42 fetches of 34 URLs, every fetched URL returned verbatim by an earlier WebSearch in its transcript; no redirect followed, no fetch refused; eight fetches repeated a URL already fetched successfully (recorded, not a breach, as at U-10 to U-12); every path inside its folder.

Fresh check of DD-IA1 · run as Fable 5.2 (claude-fable-5-2), 10 November 2026. The method names Fable 5.1 for this check, so a Fable 5.1 fresh check of DD-IA1 is owed.

Not a source: my context carried a memory listing (three file names with one-line descriptions), the Project's instructions and a skills list. I used none of them and called no memory, past-chat, Projects, connector, Artifact, Agent or mcp__ tool. Nothing was published.

Hashes: both unit files matched sha256.txt (2897b002…caf9ad) at the start and at the end; neither was edited.

Report file: /home/claude/w/check/out/report.md was NOT written. The Write tool refused it ("Subagents should return findings as text, not write report files") and I did not work around the refusal. This message is the whole report. My scripts are in /home/claude/w/check/out/scratch (counts.py, viz.py, viz2.py, currents.txt).

Web rule: every source was opened by WebSearch first, then WebFetch on a URL one of my searches returned, verbatim. No fetch was refused, redirected or timed out. One maker's document the unit does not cite was opened because a search returned it (Airbnb's 2026 autumn update, finding 4).

Every Current below occurs exactly once in DD-IA1-readonly-copy.md (checked with grep -F -c and a substring count).

## 1 · Coverage (brief DD-IA1)

- Five products spanning the four levels (public site; consumer app; backoffice; marketplace with a purchase lifecycle; several surfaces): covered.
- Read only from public screens and makers' publications, cited: covered. No public talk is used; the brief lists talks as one allowed kind, so nothing is missing.
- Per product (scheme and structure, labelling, navigation model, search, objects, lifecycle, the shaping decision, what it got right, where it strains): covered for GOV.UK, Stripe and Shopify. Thin, and said to be thin, for Monzo (no lifecycle published; tab bar not documented) and Airbnb (labelling: category names not read; search: rests on a 2022 release, see finding 4; structure: home page not readable).
- The comparison across the five: covered (section 7, figures 7 and 8).
- Figures, each product's IA redrawn with the date observed: covered for GOV.UK, Monzo, Stripe (two) and Shopify. Thin for Airbnb: its one figure is a four-box lifecycle at group level; the structure its makers document (four tabs, three kinds of booking, categories) is not drawn. The unit is at the brief's cap of eight figures.
- Deliverable (five readings; comparison table with all eight named columns): covered, in full. Deliverable C and DL-020 go beyond the brief and follow from the readings.
- Length: 13,789 words outside the viz blocks, by script, against the preamble's 2,000 to 6,000. In line with the filed units' sizes; noted, not a finding.

## 2 · Findings

1. [error] [figure] section 7, figure 8. Current: ` {"label": "Shopify", "tone": 2, "cells": ["admin, channels, POS", "four status sets", "products available by default", "POS shows online orders"]}],` and, in the paragraph before it, Current: `Shopify: admin, channels, POS; four status sets; products available by default; POS shows online orders.` Problem: the figure puts a crossing in the Connections column. Section 7's own text calls it "one crossing", says only one maker "publishes a connection" (Stripe) and concludes that what a published map leaves out "is the connections". In IA8 a crossing is the surface layer (D.1, X-01 to X-13) and a connection is a J- row joining two layers (D.4). The figure contradicts the text and the pointer. Fix: ` {"label": "Shopify", "tone": 2, "cells": ["admin, channels, POS, online orders on POS", "four status sets", "products available by default", {"mark": "none in the pages read", "tone": 6}]}],` and `Shopify: admin, channels, POS, online orders on POS; four status sets; products available by default; none in the pages read.` Basis: DD-IA1 section 7, "Against the Perqo interaction map"; vault IA8, D.1 and D.4.

2. [error] [accuracy] Deliverable C, "From GOV.UK: the onboarding journey". Current: `and three have none in IA5's inventory (the account owner's own tasks, the open fault IA10 logged; adding admin users; inviting employees)` Problem: IA8's step 1 is "Perqo sets up the client and its account owner", which is Perqo's task (IA8, section 3.2; IA7, section 3.4). The fault IA10 logged is that the account owner's own work (Company, Admins, Activity log) has no article, and adding admin users is that work, step 2. The parenthesis gives the IA10 fault to the wrong step and counts it apart from the step it belongs to. Fix: `and three have none in IA5's inventory (step 1, which Perqo's own staff do with the client; adding admin users, part of the account owner's work, whose missing article is the open fault IA10 logged; inviting employees)` Basis: vault IA8, section 3.2; IA7, section 3.4; IA10, section 2.5.

3. [should-fix] [deliverable] Deliverable C, DL-020, and the facts table. Current: `each with its articles: 1 Set up your company and account owner;` and Current: `| The step names: Set up your company and account owner;` Problem: the page is addressed to HR and finance teams and its first step names a task Perqo's staff do (finding 2). Fix: `each with its articles: 1 Perqo sets up your company and account owner;` and `| The step names: Perqo sets up your company and account owner;` Basis: vault IA8, section 3.2; IA10, section 2.5 (customer success sets up the client and its account owner at CL-3).

4. [should-fix] [accuracy] section 5, Search; Deliverable B; figure 7; section 7; Sources. Problem: the reading of Airbnb's search rests on the release of 11 May 2022. Airbnb's newsroom post of 30 September 2026, before the unit's date, says: "Search across homes, experiences, and services using your own words or voice with our new search bar." The unit's present-tense "the place box" is the 2022 state. Both dates: 11 May 2022 (the unit's source) and 30 September 2026 (read 10 November 2026). Five edits.
   a. Current: `The search's fields, filters and results were not read.` Fix: `The search's fields, filters and results were not read. A later release changes the box itself: "Search across homes, experiences, and services using your own words or voice with our new search bar" (Airbnb, "Airbnb 2026 autumn update", newsroom, 30 September 2026, [news.airbnb.com, 2026 autumn update](https://news.airbnb.com/en-uk/airbnb-2026-autumn-update), read 10 November 2026; vendor's account). The place box above is the search as its makers described it in May 2022; the new bar was not seen.`
   b. Current: `| the place box, whose limit the makers gave as the reason for categories |` Fix: `| in 2022 the place box, whose limit the makers gave as the reason for categories; since 30 September 2026 a bar that takes the guest's own words or voice across homes, experiences and services (not seen) |`
   c. Current: `"a place in the search box"` Fix: `"place box 2022, own words 2026"` and, in the paragraph before figure 7, Current: `database; a place in the search box; categories beside place;` Fix: `database; place box 2022, own words 2026; categories beside place;`
   d. Current: `Airbnb's is the place box its makers argued was not enough;` Fix: `Airbnb's was the place box its makers argued in 2022 was not enough, and since September 2026 a bar that takes the guest's own words;`
   e. Current: `- Airbnb. "Now there's even more to Airbnb". Resources for hosting, 20 May 2026 (vendor's account).` Fix: a new line before it, `- Airbnb. "Airbnb 2026 autumn update". Airbnb newsroom, 30 September 2026 (vendor's account). [news.airbnb.com, 2026 autumn update](https://news.airbnb.com/en-uk/airbnb-2026-autumn-update)`, then the existing line unchanged: `- Airbnb. "Now there's even more to Airbnb". Resources for hosting, 20 May 2026 (vendor's account).`
   Basis: Airbnb newsroom, 30 September 2026, https://news.airbnb.com/en-uk/airbnb-2026-autumn-update.

5. [should-fix] [accuracy] section 4, Lifecycle and "What it got right". Current: `the first three API statuses all show as **Incomplete**,` Problem: the mapping table itself, apart from its edge-case sentence, gives other Dashboard statuses for these rows: under `requires_payment_method` and under `requires_action` the payment status "can also be Partially paid, Waiting on funding or Failed", and a cancelled intent "might show Failed". "All show as Incomplete" and "many to one" say less than the table. Fix: `the first three API statuses show as **Incomplete** (the table adds that under `requires_payment_method` and `requires_action` the status can also be **Partially paid**, **Waiting on funding** or **Failed**),` and Current: `and in a mapping that is many to one:` Fix: `and in a mapping that is many to one in its main line, with the exceptions the table lists:` Basis: Stripe, "Payment status updates", English (UK), https://docs.stripe.com/payments/payment-intents/verifying-status?locale=en-GB.

6. [should-fix] [figure] section 4, figure 4. Current: `attempt fails, such as a decline, back to Requires payment method; and cancel.` and, in the caption, Current: `Only the moves the pages state are drawn.` Problem: the page states that a failed attempt "returns to `requires_payment_method`" without naming the status it leaves; the figure draws it from Processing only. The page says "You can cancel a PaymentIntent before it reaches a `processing` or `succeeded` state" (and from `processing` for six bank-debit methods); the figure draws cancel from Requires payment method only. Two origins are the unit's choice, and the caption says otherwise. Fix: `attempt fails, such as a decline, back to Requires payment method, a move the page states without naming the status it leaves, drawn here from Processing as this unit's reading; and cancel, which the page allows before a PaymentIntent reaches Processing or Succeeded and which is drawn once, from Requires payment method.` and `Only the moves the pages state are drawn; where a page does not name the status a move leaves (the failed attempt, the cancellation), the origin drawn is this unit's reading.` Basis: Stripe, "How Payment Intents and Setup Intents work", https://docs.stripe.com/payments/intents.md.

7. [should-fix] [label] section 3, Scheme and structure. Current: `this reading rests on Monzo's own help pages and blog, read on 10 November 2026.` Problem: "Your guide to the home screen" is Monzo's English page for Spain (footer "Spain | English", operator Monzo Bank Europe DAC, Sucursal en España). The "Save tab" is named only there, and "Savings & Investments" only on the UK page. The body joins two markets' pages into one app map and says so only in the Unsure list. Fix: `this reading rests on Monzo's own help pages and blog, read on 10 November 2026. One of them, "Your guide to the home screen", is Monzo's English-language page for Spain (monzo.com/en-es), and the "Save tab" is named only there; the other two help pages are at the UK address, so the structure below joins two markets' pages and may match neither app exactly.` Basis: https://monzo.com/en-es/help/using-monzo/help-home-screen; https://monzo.com/help/app-help/finding-features-new-homescreen.

8. [should-fix] [accuracy] section 2, "What it got right", and Deliverable A, RD-03. Current: `a merger of three systems announced in 2021 and not finished in the posts read` Problem: Dub wrote "We're in the early stages of thinking about how we might bring together mainstream topics, specialist topics and the taxonomy into a single tagging system." That is not an announced merger. Fix: `a merger of the three systems that GDS wrote in 2021 it was in "the early stages of thinking about", and that no post read reports finished` and Current: `the merger not finished in the posts read` Fix: `the merger, at "the early stages of thinking" in 2021, not reported finished in the posts read` Basis: Dub, GDS blog, 17 May 2021, https://gds.blog.gov.uk/2021/05/17/our-plans-to-improve-navigation-on-gov-uk.

9. [should-fix] [accuracy] section 2, "What it got right", and Deliverable C, "From GOV.UK: one taxonomy". Current: `and on two points they say the same: tag at the lowest level, never to a topic and its parent (taxonomy principles, 2019; IA4, Deliverable B, R2)` Problem: IA4's R2 reads "In F-CAT, values do not overlap … every item has exactly one narrower term". It is a rule about catalogue items and overlapping values; it says nothing of a topic and its parent, and nothing of Help centre articles. "Say the same" overstates it. Fix: `and on one point they meet: GOV.UK tags content to the lowest possible level and never to both a topic and its parent, and IA4 gives every catalogue item exactly one narrower term, and so one category (taxonomy principles, 2019; IA4, Deliverable B, B.1 and B.4, R2)` and Current: `GOV.UK's principles and IA4's rules agree on tagging at the lowest level and never to a parent (taxonomy principles, 2019; IA4, B.4, R2), so a reviewer who meets a Perqo article tagged to both Health and Fitness has a fault to report under both.` Fix: `GOV.UK's principles tag at the lowest level and never to a topic and its parent, and IA4 gives every catalogue item exactly one narrower term (taxonomy principles, 2019; IA4, B.1 and B.4, R2). IA4's rule is written for catalogue items, so for a Perqo article tagged to both Health and Fitness a reviewer has GOV.UK's principle as a default at C0 and no filed Perqo rule.` Basis: vault IA4, B.1 (F-CAT row) and B.4, R2; IA5, A.3 (the F-CAT column of articles).

10. [should-fix] [figure] section 2, figure 1, caption. Current: `and from GDS's own documents (Dub, GDS blog, 2021; GOV.UK taxonomy principles, 2019);` Problem: the figure draws "more than 4 million searches a month" (Fraser and Crusellas 2024) and the step by step pages' "end to end journeys" (GOV.UK Design System); the caption names neither source. Fix: `and from GDS's own documents (Dub, GDS blog, 2021; GOV.UK taxonomy principles, 2019; Fraser and Crusellas, Inside GOV.UK, 2024, for the searches a month; GOV.UK Design System, Step by step navigation);` Basis: sourcing-standard Part 1 (a caption says where its data comes from); DD-IA1 section 2.

11. [should-fix] [figure] sections 3 and 4, figures 2 and 3, notation. Problem: IA2's tag `home` means the home page. The filed app and backoffice maps draw the surface as an untyped root and tag its Home screen `home` (IA3; IA6, B.3: "The root is the surface, since the tab bar is not a screen"; IA7, Deliverable C). Figures 2 and 3 tag the surface `home` and its Home `section`. Six edits.
   a. Current: `"root": {"label": "Monzo app", "type": "home", "tone": 2,` Fix: `"root": {"label": "Monzo app", "tone": 2,`
   b. Current: ` {"label": "Home", "type": "section", "tone": 2, "note": "layout set by the customer", "children": [` Fix: ` {"label": "Home", "type": "home", "tone": 2, "note": "layout set by the customer", "children": [`
   c. Current: `Monzo app (`home`), its note "tab bar not fully named in the pages read", leads to Home (`section`, "layout set by the customer")` Fix: `Monzo app, the surface, drawn without a type tag as IA6 draws the Perqo app (IA6, B.3), its note "tab bar not fully named in the pages read", leads to Home (`home`, "layout set by the customer")`
   d. Current: `"root": {"label": "Dashboard", "type": "home", "tone": 2, "children": [` Fix: `"root": {"label": "Dashboard", "tone": 2, "children": [`
   e. Current: ` {"label": "Home", "type": "section", "tone": 2, "note": "analytics; Your overview widgets"},` Fix: ` {"label": "Home", "type": "home", "tone": 2, "note": "analytics; Your overview widgets"},`
   f. Current: `Dashboard (`home`) leads to Home (`section`, "analytics; Your overview widgets")` Fix: `Dashboard, the surface, drawn without a type tag as IA7 draws Perqo Admin (IA7, Deliverable C), leads to Home (`home`, "analytics; Your overview widgets")`
   Basis: vault IA2, section 5.2, Labels, and the notation sheet; IA6, B.3; IA7, Deliverable C.

12. [should-fix] [accuracy] section 4, Navigation model. Current: `The global routes are the sidebar's sections and the search;` Problem: the next paragraph calls search "the Dashboard's strongest supplemental route", Deliverable B lists it as supplemental, and IA7, section 4.1 gives search as a supplemental route. The section contradicts itself. Fix: `The global routes are the sidebar's sections; the search is a supplemental route, read in the next paragraph;` Basis: DD-IA1 section 4, Search, and Deliverable B; vault IA7, section 4.1.

13. [should-fix] [accuracy] section 5, "What it got right". Current: `so a host influences it only through what they write,` Problem: the release says listings are analysed by machine learning, reviewed by a curation team and given a final check. It does not say a host has no other way to affect a category; "only" asserts more than Airbnb published. Fix: `so, on the pages read, what a host writes and photographs is the documented input to it,` Basis: Airbnb newsroom, 11 May 2022, https://news.airbnb.com/2022-summer-release/; sourcing-standard Part 4.

14. [should-fix] [attribution] section 6, "What later units take", figure 6 caption, Sources: two page titles. Problem: the page at help.shopify.com/en/manual/shopify-admin/shopify-admin-overview is titled "Navigating the Shopify admin" as fetched on 10 November 2026 (a search index still lists the older title "Shopify admin overview"; I cannot date the change). The eBay page is titled "Finding categories for a listing"; "Sell categories" is its address slug.
   a. Current: `(Shopify Help Center, "Shopify admin overview", [help.shopify.com, admin overview]` Fix: `(Shopify Help Center, "Navigating the Shopify admin", [help.shopify.com, admin overview]`
   b. Current: `- Shopify Help Center. "Shopify admin overview", undated` Fix: `- Shopify Help Center. "Navigating the Shopify admin", undated`
   c. Current: `(Shopify admin overview; Sales channels; Manage sales channels;` Fix: `(Navigating the Shopify admin; Sales channels; Managing sales channels;`
   d. Current: `(eBay Developers Program, "Sell categories", [` Fix: `(eBay Developers Program, "Finding categories for a listing", [`
   e. Current: `- eBay Developers Program. "Sell categories", undated` Fix: `- eBay Developers Program. "Finding categories for a listing", undated`
   Basis: https://help.shopify.com/en/manual/shopify-admin/shopify-admin-overview; https://www.developer.ebay.com/api-docs/sell/static/metadata/sell-categories.html.

15. [minor] [attribution] section 6 and Sources. Current: `(Shopify Help Center, "Manage sales channels", [` and Current: `- Shopify Help Center. "Manage sales channels", undated` Problem: the page's title and heading read "Managing sales channels". Fix: `(Shopify Help Center, "Managing sales channels", [` and `- Shopify Help Center. "Managing sales channels", undated` Basis: https://help.shopify.com/en/manual/online-sales-channels/manage?sh_rd=1.

16. [minor] [accuracy] section 3, Objects. Current: `the card (one per account, with its number, CVC and a freeze)` Problem: the pages name a Card button on each account; neither says an account has one card. Fix: `the card (reached from a Card button on each account, with its number, CVC and a freeze)` Basis: https://monzo.com/help/app-help/finding-features-new-homescreen.

17. [minor] [accuracy] sections 3 and 7, pointer to IA3's B1. Current: `the units the customer acts on are shown where the decision is made (IA3, checklist B1)` and Current: `shows the first screen as the place where the units the customer acts on must sit` Problem: B1 asks about "the units the system acts on, at the place where the person makes the decision those units govern". Fix: `the units the system acts on are shown where the person makes the decision they govern (IA3, checklist B1)` and `shows the first screen as the place where the units the system acts on must sit` Basis: vault IA3, checklist B1; IA6, section 3.5.

18. [minor] [attribution] section 4, "What it got right". Current: `it is IA1's "Surface: Label" mapping (IA1, section 2.4)` Problem: IA1, section 2.4 sets the mapping; the line "Surface: Label" is IA2's way of drawing it. Fix: `it is IA1's vocabulary mapping, which IA2 draws as a line "Surface: Label" (IA1, section 2.4; IA2, section 5.2)` Basis: vault IA2, section 5.2, Labels.

19. [minor] [attribution] "What later units take", DD-IA2. Current: `(IA11, section 3.4), so a business case` Problem: the interval is section 3.4; the mark set before the test is section 4.4 (IA11's own facts row cites both). Fix: `(IA11, sections 3.4 and 4.4), so a business case` Basis: vault IA11, sections 3.4 and 4.4, and its facts table.

20. [minor] [attribution] Deliverable C, the onboarding journey. Current: `(IA8, section 3.2), and IA10 gave each role` Problem: the quoted words are the row of IA8's facts table (and IA10, section 2.5); section 3.2's body gives the order as six numbered steps in other words. Fix: `(IA8, "Perqo facts set by this unit", for section 3.2), and IA10 gave each role` Basis: vault IA8, section 3.2 and the facts table.

21. [minor] [accuracy] section 5, Lifecycle. Current: `One status was read in full.` Problem: the article gives Pending two causes; the unit reports one. The second has its own time limit and outcome and supports the same lesson. Fix: `One status was read in full. The article gives it two causes: a host who has not yet answered, read here, and a guest whose identity verification is not complete, who has 12 hours before the reservation is cancelled.` Basis: Airbnb Help Center, article 2810, https://www.airbnb.com/help/article/2810 (the second cause read through a summary, so it is paraphrased).

22. [minor] [accuracy] section 5, "What it got right". Current: `A request that nobody answers ends at Expired within 24 hours` Problem: it expires when 24 hours pass without a response. Fix: `A request that nobody answers ends at Expired after 24 hours` Basis: article 2810.

23. [minor] [style] section 2, Labelling. Current: `And one label drifts within a page:` Problem: the sentence then gives two labels (Births, deaths; Transparency). Fix: `And two labels drift within a page:` Basis: the sentence itself; gov.uk as fetched 10 November 2026.

24. [minor] [figure] introduction, tones. Current: `marks the paths that end without success in a lifecycle and the strains this reading finds.` Problem: figure 8 also draws tone 6 for "none in the pages read", a third use the declaration does not cover (the figure's own paragraph names it). Fix: `marks the paths that end without success in a lifecycle, the strains this reading finds and, in section 7's second figure, a layer in which the pages read publish nothing, the gap this review finds in a published map.` Basis: vault IA2, section 5.2, Tones (one meaning each).

25. [minor] [figure] sections 2 and 3, facts that appear only in a figure's own paragraph. Current: `GOV.UK (`home`), with Popular on GOV.UK; Featured in its note,` and Current: `Activity (`index`, "latest and upcoming payments; See all")` Problem: "Popular on GOV.UK", "Featured" and "See all" are in no sourced sentence of their sections (the same holds for "Your overview" in figure 3's Home note). All are right as fetched. Fix: `GOV.UK (`home`), with Popular on GOV.UK; Featured in its note, two headings of the home page as read on 10 November 2026,` and `Activity (`index`, "latest and upcoming payments; See all", See all being the link the finding-features page names for the full list of payments)` Basis: https://gov.uk; https://monzo.com/help/app-help/finding-features-new-homescreen; https://docs.stripe.com/dashboard/basics?locale=en-US.

26. [minor] [label] sections 4 and 6, vendor label missing where a source is first cited (it is in the Sources list). Five Currents: `(https://docs.stripe.com/payments/payment-intents/verifying-status?locale=en-GB), read 10 November 2026)`; `(https://docs.stripe.com/dashboard/search?locale=en-US), read 10 November 2026)`; `(https://help.shopify.com/en/manual/sell-online), read 10 November 2026)`; `(https://help.shopify.com/en/manual/online-sales-channels/manage?sh_rd=1), read 10 November 2026)`; `(https://help.shopify.com/en/manual/sell-in-person/shopify-pos/order-management/search-orders), read 10 November 2026)`. Fix, for the first: `(https://docs.stripe.com/payments/payment-intents/verifying-status?locale=en-GB), read 10 November 2026; vendor documentation)`, and the same ending, `; vendor documentation)` in place of the final `)`, on the other four. Basis: sourcing-standard Part 4.

27. [minor] [accuracy] section 6, Labelling. Current: `the page says channels are installed from the Shopify App Store but appear` Problem: the page says "some sales channels are installed through the Shopify App Store". Fix: `the page says some channels are installed through the Shopify App Store but appear` Basis: https://help.shopify.com/en/manual/online-sales-channels/manage?sh_rd=1.

28. [minor] [style] section 7. Current: `Each publishes pieces of one layer, and one publishes a connection.` Problem: the next sentences list two or three layers for GOV.UK, Stripe, Airbnb and Shopify. Fix: `Each publishes pieces of one or more layers, and one publishes a connection.` Basis: the paragraph itself.

29. [minor] [figure] section 6, figure 6. Current: `and "POS: #1-1005 when offline".` and Current: `"POS: #1-1005 when offline"]}` Problem: the text and the page give two cases, offline or without payment. Fix: `and "POS: #1-1005 offline or unpaid".` and `"POS: #1-1005 offline or unpaid"]}` Basis: https://help.shopify.com/en/manual/sell-in-person/shopify-pos/order-management/search-orders.

30. [minor] [figure] section 1, the table of five. Current: `a public site with more than half a million pages, whose makers` Problem: the number carries no owner or year where it first appears. Fix: `a public site with more than half a million pages (GDS's figure, 2021; section 2), whose makers` Basis: Dub 2021.

31. [minor] [style] section 2, Labelling. Current: `on the most governed site of the five` Problem: an unsourced superlative. Fix: `on the one site of the five whose makers publish rules for its vocabulary` Basis: sourcing-standard Part 1.

32. [minor] [deliverable] Deliverable C, DL-020. Current: `an optional module in the help-article template, T-16.` Problem: IA5's modules carry identifiers, M-01 to M-27; the new module has none, so no later entry can cite it. Fix: `an optional module in the help-article template, T-16, numbered M-28 after IA5's M-01 to M-27 (proposed).` If taken, the facts table's first row gains the same identifier. This sets a new Perqo identifier, so it is the writer's or Pedro's call. Basis: vault IA5, Deliverable C, C.1.

33. [minor] [accuracy] section 4, Lifecycle. Current: `the unlocalised lifecycle page and the search page write it `canceled`` Problem: the search page was read at its English (US) address, as the Unsure list says. Fix: `the unlocalised lifecycle page and the English (US) search page write it `canceled`` Basis: https://docs.stripe.com/dashboard/search?locale=en-US.

34. [minor] [style] section 7, "By scheme and structure". Current: `Four of the five organise their first level by object or account: Monzo by account, Stripe and Shopify by object type, Airbnb by place.` Problem: a place is neither an object nor an account. Fix: `Four of the five organise their first level by an exact property: Monzo by account, Stripe and Shopify by object type, Airbnb by place.` Basis: vault IA4, section 1.1 (exact schemes).

## 3 · Accuracy: the Unsure list, item by item

- GOV.UK topic lists and label variants: PASS. gov.uk and gov.uk/browse fetched 10 November 2026: 16 topics; body "Births, deaths, marriages and care", navigation menu "Births, death, marriages and care"; "Transparency documents" in one Government activity list, "Transparency" in the others; the eight-link list ends "How government works", "Get involved". Which list is the menu is the extraction's attribution in my fetch too.
- Benefits children from the content API: PASS. document_type mainstream_browse_page; second_level_ordering "curated"; eight children, seven opening "Benefits and financial support" (counted by script); public_updated_at 2018-05-16. The live page gov.uk/browse/benefits lists the same eight with "Manage an existing benefit, payment or claim" first, so "the eighth" is the record's order only.
- Richardson's reply of 4 February 2025: PASS, quoted exactly.
- Monzo pages undated, en-es: PASS as a caution; see finding 7.
- Stripe search at its en-US address: PASS; fetched there.
- Stripe mapping on the English (UK) page, `cancelled`: PASS.
- Airbnb statuses under the four headings not loaded: unverifiable, as for the writer. My fetch of article 363 returned the four headings and nothing under them. That Pending is pre-trip stays the unit's assumption, marked.
- The 55 categories in November 2026: unverifiable; not observed by me either.
- Shopify POS fields and filters: PASS, including "Filters apply only to the Orders list."
- Figure 6's counts and the shaping decisions are the unit's reading: so labelled in the text.

## 4 · Confirmed (source opened 10 November 2026)

- GOV.UK home: "Services and information", 16 topics; Government activity's eight links; "Menu" and "Search GOV.UK"; headings "Popular on GOV.UK" and "Featured". https://gov.uk; https://gov.uk/browse
- Content API: 16 top-level browse pages; the Benefits record's link keys include children, top_level_browse_pages, primary_publishing_organisation, available_translations. https://www.gov.uk/api/content/browse/benefits
- Taxonomy principles, published 13 June 2019: all five quoted strings present (two as headings); "sidebar links and breadcrumbs on content pages"; qualifiers in brackets for a name used twice. https://www.gov.uk/government/publications/govuk-topic-taxonomy-principles/govuk-taxonomy-principles
- Step by step pattern: all four quotations; "More user research is needed"; undated. https://design-system.service.gov.uk/patterns/step-by-step-navigation
- Dub, 17 May 2021: around 200, 400 and 4,000 topics; three menu bars; "This triple-system, which has substantial duplication, causes confusion for users"; "more than half a million pages, and in 2021 has averaged 17.8 million users a week"; "around 15% use topic pages to navigate"; "tag their content to multiple topics, and to multiple topic systems". https://gds.blog.gov.uk/2021/05/17/our-plans-to-improve-navigation-on-gov-uk
- Fraser, Sutter and Stockford, 23 October 2024: "one of the main ways"; Vertex AI Search; live "at the end of February" (2024 by the post's date); 14%, 11%, 8% exactly as quoted; A/B test; no interval or sample size. https://insidegovuk.blog.gov.uk/2024/10/23/a-new-search-engine-for-gov-uk/
- Fraser and Crusellas, 12 December 2024: "more than 4 million times a month"; "a single panel above the search results"; "only a small minority of people selected filters"; 55% of searches where suggestions were shown. https://insidegovuk.blog.gov.uk/2024/12/12/making-it-quicker-and-easier-to-search-on-gov-uk
- Stephens-Manassiev, 12 February 2019, a product manager on GOV.UK: all four quotations; July 2018; the three teams named for DD-IA3. https://insidegovuk.blog.gov.uk/2019/02/12/an-update-on-the-gov-uk-taxonomy/
- Richardson, 31 January 2025: A/B test, grid against list; the quoted sentence; "Most viewed" renamed from "Popular tasks" after user research; all 16 topic pages; multivariate tests; no figures. https://insidegovuk.blog.gov.uk/2025/01/31/rolling-out-simpler-ways-to-navigate-gov-uks-topic-pages
- Monzo home screen guide (Spain, English), undated: accounts at the top; Activity; Pots "as a list or with images"; "Save tab: Find your Savings Pots here"; the "+" sentence; profile photo top left; "checking your balance". https://monzo.com/en-es/help/using-monzo/help-home-screen
- Monzo finding features, undated: Card button per account, card number and CVC, freeze; three dots (adding money, statements, scheduling payments); Pots "right under the Activity section"; Savings & Investments under Pots; edit layout under Settings; "See all". https://monzo.com/help/app-help/finding-features-new-homescreen
- Monzo search changes, undated: all quotations; export (PDF, CSV, XLSX) and location filters removed. https://monzo.com/help/app-help/unified-search-changes-web
- White, 1 November 2023 and 6 November 2023: every quotation; more than 1,000 customers; 4 major and 2 minor experiments over 7 months; more than 8 million people; no method or result. https://monzo.com/blog/the-new-and-improved-home-screen; https://monzo.com/blog/how-we-built-the-new-home-screen
- Stripe Web Dashboard: first section and its five pages; Shortcuts; Products (Connect, Payments, Billing, Reporting) and More's list; settings in three categories; Transactions links to dashboard.stripe.com/payments; customer details; Product catalog; the "?" key; Organizations; levels of access; "in 14 languages". https://docs.stripe.com/dashboard/basics?locale=en-US
- Stripe Dashboard search: 26 object types, account to transfer (counted from the table); `charge` "A payment (identical to `payment`)"; field filters, range operators, hyphen negation, `is:refunded`; identifiers; the bookmark sentence; `status:canceled`. https://docs.stripe.com/dashboard/search?locale=en-US
- Stripe intents: six states and `requires_capture`; the decline sentence; "can't be undone"; capture to `processing` or `succeeded` "depending on the payment method". https://docs.stripe.com/payments/intents.md
- Stripe payment status (en-GB): "summarises the payment but doesn't include the additional details"; the mapping rows; the edge-case sentence exactly; the Payments page; JSON through Workbench Inspector; `cancelled`. https://docs.stripe.com/payments/payment-intents/verifying-status?locale=en-GB
- Airbnb, 11 May 2022: 55 categories, 4 million unique homes, both search quotations, machine learning, curation team, final check, "by what makes them unique", over-tourism, around 40% more listings, 14 categories. https://news.airbnb.com/2022-summer-release/
- Airbnb, 13 May 2025: "book homes, experiences, and services — all in one place"; Explore, Trips, Messages, Profile with the two quoted descriptions. https://news.airbnb.com/product-releases/airbnb-2025-summer-release/
- Airbnb hosting page, 20 May 2026: title, date, the map sentence, the tips sentence. https://www.airbnb.co.uk/resources/hosting-homes/a/now-theres-even-more-to-airbnb-763
- Airbnb help 363: title and the four group headings. https://www.airbnb.com/help/article/363
- Airbnb help 2810: title; Pending until the host responds; 24 hours; Declined or Expired; refund to the original payment method. https://www.airbnb.com/help/article/2810
- Shopify admin page: "Core aspects of your Shopify business, including orders, products, and customers"; "Sales channels and apps"; search results filtered by category "such as Orders or Apps". https://help.shopify.com/en/manual/shopify-admin/shopify-admin-overview
- Shopify sales channels: the quoted sentence; Online Store, Point of sale, Shop, social channels, Google, marketplaces. https://help.shopify.com/en/manual/sell-online
- Shopify managing channels: the three quoted sentences; listed in the sidebar and in Settings; shown as Sales channels and not as Apps. https://help.shopify.com/en/manual/online-sales-channels/manage?sh_rd=1
- Shopify POS orders: the Orders screen sentence; "#1-1005"; the search fields; the three filters; filters not applied to search results; the navigation bar; the global search over orders and drafts. https://help.shopify.com/en/manual/sell-in-person/shopify-pos/order-management/search-orders
- Shopify order statuses: 3 order, 9 payment plus Expiring (a badge, "two days before the deadline for capturing payment") and Unpaid (a grouping of Authorized, Pending, Expired, Partially paid), 7 fulfillment, 4 return; the "views" sentence. https://help.shopify.com/en/manual/orders/order-status
- Shopify app navigation: all six quotations. https://shopify.dev/docs/apps/design/navigation.md
- eBay: the three quoted passages. https://www.developer.ebay.com/api-docs/sell/static/metadata/sell-categories.html
- Airbnb article 2810 at the same number on several country domains: PASS for the pattern (my search returned it on airbnb.com, .ca, .co.in, .jp, .dk, .com.br and others); unverifiable for .se, which my search did not return.
- Counts by script: RD-01 to RD-15, 15 rows, 5, 2, 3, 3, 2 by product, every rung C0; 8 viz blocks; 31 linked sources in the body, the same 31 in Sources, 32 entries with the line of works cited through filed units; no link text is a long bare path; "(Perqo, fictional)" on Perqo's first use; DL-020's fields are IA12's template D.1, all fourteen; DL-020, H-1.4, /hr-finance/setting-up and RD- are used nowhere in IA1 to IA12 or the register, so each is free.
- Pointers confirmed against the vault: IA2 section 3 (five faults, in the order used), section 4 (rename through the vocabulary; note of 9 November 2026), section 5.2 (tones 2, 5 and 6, quoted exactly), sections 1.5, 1.8 and 5.3; IA3 checklist A2, A4, D2, E1, E2, sections 4.1, 4.2, 5.1 and the E1 trigger quoted exactly; IA4 sections 1.1, 1.2, 2.1, 2.3, 4.1, R1 to R10; IA5 A.3 (H-1.1.1, H-1.1.2, H-1.2.1 to H-1.2.3, S-6, T-16), section 5.3; IA6 sections 3.2 and 3.5, Deliverable B; IA7 sections 4.1 to 4.5, 5.2 EX-3 ("is not a state"), 6.2, "a global search, role-scoped"; IA8 D.1 to D.4 (X-01 to X-13, CL-1 to CL-6, EL-1 to EL-6, DT-1 to DT-3, J-01 to J-14, J-01 as the status join), sections 1, 4.1 and 5.1; IA9 D.1, D.3 (DL-001 to DL-010), section 4.4; IA10 section 2.5, FO-01, FO-05, DL-012; IA11 sections 2.6 and 6.4, M-01 to M-11, M-07; IA12 section 2 (both quotations, C0), section 3.2, section 5, Deliverable A ("structure from the objects and the data model"), Deliverable B AR-34, Deliverable D D.1.

## 5 · Figures (whose number), labels, deliverable, public-site rules, errata

- Whose figure: every number names its owner where it is argued; one first use does not (finding 30).
- Labels: makers' accounts, vendor documentation, design-system guidance and "this unit's reading" are labelled; five first citations lack the label (finding 26). No anecdote or correlational data is used as evidence; every lesson is held at C0.
- Deliverable: present in full, usable alone, follows from the readings; edits in findings 2, 3, 4b, 8, 9, 32.
- Public-site rules: real products and makers named; observations dated; screens not seen named per product; no private person named (the people named are bylined authors of the posts cited); no personal fact about the reader. One assertion goes past what was published (finding 13).
- Perqo: labelled on first use; DL-020 is the next free number; consistent with IA1 to IA12 and the register except findings 2 and 3.
- Errata: the folder holds no audit report, and hub.py records Audits 1 to 3 as owed with none run, so no erratum exists to apply. The one dated amendment the unit leans on (IA2, section 4, note of 9 November 2026) is in the filed IA2.

## 6 · Figures, one by one

1. sitemap, section 2 (GOV.UK). Kind fits a hierarchy. Every label, number and date is in the unit's text; tones 2 and 6 named. FIX: caption sources (finding 10); note facts only in the figure's paragraph (finding 25).
2. sitemap, section 3 (Monzo app map). Kind fits. Labels traced; tone 2 named; caption names section, sources, date and credit. FIX: root and Home type tags (finding 11a to 11c).
3. sitemap, section 4 (Stripe sidebar). Kind fits. Labels traced; tones 2 and 6 named. FIX: root and Home type tags (finding 11d to 11f).
4. states, section 4 (PaymentIntent). Kind fits a lifecycle; no transition spans more than one row. Labels traced. FIX: the text and caption on the two origins the pages do not state (finding 6).
5. states, section 5 (Airbnb reservation). Kind fits; the mixed levels are declared in the text and the caption; "(assumed)" is in the note. Labels traced; tones 2 and 6 named; caption complete. PASS.
6. objects, section 6 (Shopify). Kind fits things and relationships; the upward label carries its triangle; counts declared as the unit's reading; a line without counts has precedent in IA2's and IA8's cross-surface maps. FIX: caption titles (finding 14c); one attribute (finding 29).
7. matrix, section 7 (comparison). Kind fits items by dimensions; row labels short; cells traced to sections 2 to 6. FIX: the Airbnb search cell (finding 4c).
8. matrix, section 7 (layers). Kind fits; tones 2, 5 and 6 named in its paragraph. FIX: the Shopify row (finding 1); the tone 6 declaration (finding 24).

DD-IA1 · verdict: fix · 2 error, 12 should-fix, 20 minor.

---

## Maintainer's notes (U-13 chat, 10 November 2026)

**Verification.** Every finding was verified before it was applied. Against the filed units: 1 (IA8, D.1 and D.4: a crossing is the surface layer, a connection a J- row), 2 and 3 (IA8, CL-3: Perqo sets up the client with its first admin user as account owner; IA7, section 3.4: the account owner adds admin users; IA10, section 2.5 and its open fault), 9 (IA4, B.4, R2 is a rule for catalogue items), 11 (IA6, B.3 and IA7, Deliverable C draw the surface as an untyped root and its Home as `home`; IA2, section 5.2's tag list), 12 (IA7, section 4.1: search a supplemental route), 17 (IA3, checklist B1), 18 (IA2, section 5.2 and its legend row), 19 (IA11, sections 3.4 and 4.4), 20 (IA8, its facts table's onboarding row), 32 (IA5, C.1, M-01 to M-27). Against the outside sources, each by the maintainer's own search and a fetch of a URL that search returned: 4 (Airbnb newsroom, "Airbnb 2026 autumn update", 30 September 2026, news.airbnb.com/en-uk), 5 (Stripe, "Payment status updates", en-GB), 6 (Stripe, "How Payment Intents and Setup Intents work"), 7 (Monzo's en-es page: footer Spain, Monzo Bank Europe DAC, Sucursal en España), 8 (Dub, GDS blog, 17 May 2021), 14 (Shopify's page titled "Navigating the Shopify admin"; eBay's page titled "Finding categories for a listing"), 15 and 27 ("Managing sales channels"; "some sales channels are installed through the Shopify App Store"), 16 and 25 (Monzo, finding features: a Card button "for each account"; "See all"), 21 and 22 (Airbnb article 2810: two causes, 12 hours for identity verification; expiry after 24 hours), 23 and 25 (gov.uk: "Births, deaths" against "Births, death"; "Transparency documents" against "Transparency"; the headings "Popular on GOV.UK" and "Featured"), 29 (Shopify POS: offline or without payment). Finding 13 holds on the unit's own text, since no source read states the "only" it removes; the maintainer's searches did not return the unit's own address for the 2022 release, and a fetch of the other address a search returned (product-releases/airbnb-2022-summer-release) did not mention the placement method, so the method itself rests on the writer's and the checker's reading of that page. Findings 10, 24, 26, 28, 30, 31, 33 and 34 are about the unit's own text and were checked against it.

**Applied.** All 34 findings, as 62 exact replacements by script, each Current found once when applied; finding 32's M-28 carried into DL-020's "Touches" and "Places to apply" rows and its facts-table row; two unsure lines made stale by findings 4 and 7 changed with them. The parser that took each Fix from this report stopped finding 5's Fix at its first inner code span, so the applied text broke off after `requires_payment_method`; four figure re-checkers reported the broken sentence, and it was replaced with finding 5's Fix exactly as written above. No other Fix was cut (checked by script: no other parsed Fix holds an odd number of backticks, and no line of the unit outside a figure does).

**Count.** Two errors: the verdict is fix by the count rule.

**Figures.** Figure 5 passed and was unchanged by the fixes; figures 1, 2, 3, 4, 6, 7 and 8 were changed by findings and went to fresh Opus 5.5 re-checkers, each given only the unit without its figures, the captions, the figure's declaration, IA2 and the frames sheets `verify.py --shots <dir> --page read-ux-dd-ia1` saved. Their reports follow, verbatim, each extracted by script from the agent's `SubagentHandback` call. Transcript checks (U-13 chat): each ran on claude-opus-5-5; no web, memory, Projects, connector, Artifact, Agent or `mcp__` tool; every path inside its own folder.

### Figure 1, re-check 1 (Opus 5.5)

Figure 1 (sitemap): FIX

Findings

1. [should-fix] Topic pages: the tone 6 is carried by colour alone
Current (declaration.json): `"note": "the taxonomy; reached from content pages' sidebar and breadcrumbs"`
Problem: IA2 §5.2 says "No tone is the only carrier of its meaning". The other tone 6 box, Benefits and financial support pages, says its strain in its note ("7 of 8 labels open with the same four words"). Topic pages does not, and the caption says only "tone 6: a strain found in this reading", so a reader cannot tell what the strain is. The strain is in the text, line 64: "in 2021 there were three topic systems" (Dub 2021, which the caption already cites).
Fix (declaration.json): `"note": "the taxonomy, one of three topic systems in 2021; reached from content pages' sidebar and breadcrumbs"`
Matching text change. Current (unit-without-figures.md, line 66): `carry "the taxonomy; reached from content pages' sidebar and breadcrumbs"`. Fix: `carry "the taxonomy, one of three topic systems in 2021; reached from content pages' sidebar and breadcrumbs"`

2. [minor] Content pages: a 2021 count is drawn without its date
Current (declaration.json): `"note": "more than half a million pages"`
Problem: the figure says it was redrawn from pages read on 10 November 2026. This count is GDS's 2021 figure (line 42: "GDS's figure, 2021"; line 54: Dub 2021). The caption lists Dub 2021 but does not tie it to this note, though it does tie Fraser and Crusellas to the searches count.
Fix (declaration.json): `"note": "more than half a million pages (2021)"`
Matching text change. Current (unit-without-figures.md, line 66): `Content pages (`stack`) "more than half a million pages"`. Fix: `Content pages (`stack`) "more than half a million pages (2021)"`

3. [error] Unit text, section 4, Lifecycle (line 104, not this figure): a broken parenthetical
Current (unit-without-figures.md): ``**Incomplete** (the table adds that under `requires_payment_method `processing` as **Pending**``
Problem: the parenthesis is never closed and a backtick is unmatched, so the clause stops mid-sentence and the code span runs into `processing`. Line 108 refers to "the exceptions the table lists", so the lost clause probably stated one of them.
Fix: ``**Incomplete**, `processing` as **Pending**``
If the exception should stay, restore the clause from the Payment status updates page; I could not see that page.

4. [minor] Unit text, line 66: the note's text is not quoted
Current (unit-without-figures.md): `with Popular on GOV.UK; Featured in its note`
Problem: every other note in the paragraph is in quotation marks. Without them this reads as a broken sentence.
Fix: `with "Popular on GOV.UK; Featured" in its note`

Renderer-only notes (not faults in the figure):
- At 320 and 360 px the figure scrolls sideways (70 px and 30 px). The edge fade hides text in each single frame, but every label and note is readable across the two frames.
- On tablet and desktop the six children of the root wrap into a row of four and a row of two because of the width.
- The desktop dark opening frame is clipped at the top by the sticky section bar. The desktop frames sheet shows the whole figure.

Confirmed
- Every label, type tag and note in the declaration occurs in line 66 as drawn: GOV.UK `home`; Services and information `section`, 16 topics; Benefits `section`; Benefits and financial support pages `stack` with "7 of 8 labels open with the same four words", tone 6; Manage an existing benefit, payment or claim `section`; 15 other topics `stack` with "Births, deaths, marriages and care to Working, jobs and pensions"; Government activity `section`, 8 links; Departments and News `index`; 6 more links `stack`; Search GOV.UK `index` with "more than 4 million searches a month"; Topic pages `stack`, tone 6; Step by step pages `stack` with "end to end journeys"; Content pages `stack`. Line 66 also says "Every other box is tone 2".
- The counts match section 2: 16 topics and the 8 Government activity links listed in line 50 (16 − 1 = 15 other topics; 8 − 2 = 6 more links); "Seven of the eight children of Benefits" (line 52); "more than 4 million times a month" (line 56); "more than half a million pages" (line 54).
- Caption: it names the artefact, what the figure shows, the decision it supports, section 2, the date observed (10 November 2026) and the credit (GOV.UK, Government Digital Service). Every source it cites is cited in section 2: gov.uk, gov.uk/browse, the content API record, Dub 2021, taxonomy principles 2019, Fraser and Crusellas 2024, and Step by step navigation.
- Kind: a hierarchy of pages drawn as a sitemap fits the data.
- Notation: the type tags are all from IA2's fixed list; tone 2 and tone 6 are used in their IA2 meanings; the unit's text names both tones (line 14), and the caption names both.
- Matrix check (step 5): not applicable to a sitemap.
- Frames, at 320, 360, 390 and 430 px, tablet and desktop, dark and light (light judged on cream): text stays inside its boxes, nothing overlaps, nothing is cut off beyond the renderer effects noted above, and the drawing is whole. Tone 6 can be told from tone 2 in both themes by its olive fill and yellow border, though the difference is subtle in light.
- I saw a memory snapshot and the Project instructions in my context. I used neither, and no web, memory, Projects or mcp__ tool. I read only files in /home/claude/w/rc/r1-fig1. I wrote only crops, to /home/claude/w/rc/r1-fig1/crops/.

*Maintainer's note.* Applied: findings 1, 2 and 4 (the note now names the three topic systems of 2021; the 2021 date on half a million pages; the home note quoted); finding 3 is the section 4 sentence repaired with fresh-check finding 5's Fix. Renderer notes recorded, not applied. Reopened for round 2.

### Figure 2, re-check 1 (Opus 5.5)

Figure 2 (sitemap): FIX

The figure itself is sound. Every label, type tag and note is traced to the unit text, the kind and tone are right, and it draws whole at every width and theme. The verdict is FIX because of one should-fix in the caption. Findings 2 and 3 are minor.

1. [should-fix] Current (declaration.json): `the tab bar is drawn only as far as the pages name it.`
   Problem: The map joins pages from two markets, and the caption doesn't say so. Section 3 states that "the 'Save tab' is named only there" (Monzo's English-language page for Spain). It adds that "the structure below joins two markets' pages and may match neither app exactly". The unsure list repeats this. The figure draws Save tab as a top-level box, but the caption presents the map as simply "the Monzo app's structure". A reader who sees only the figure loses this caveat.
   Fix: `the tab bar is drawn only as far as the pages name it, and the Save tab is named only on Monzo's English-language page for Spain, so the map joins two markets' pages.`

2. [minor] Current (declaration.json): `White, Monzo blog, 2023`
   Problem: The unit cites two White posts from 2023 (1 November and 6 November), so this citation doesn't say which one. The Home note "layout set by the customer" rests on both: "order and level of detail can be changed" is from 1 November, and customers controlling "what they see on their Home screen" is from 6 November.
   Fix: `White, Monzo blog, 1 and 6 November 2023`

3. [minor] Current (declaration.json): `"label": "+", "type": "form"` (and in unit-without-figures.md: `+ (`form`,`)
   Problem: The home screen guide describes "+" as opening a choice: "open a new account, create a new Pot, apply for a loan, or more". That is a launcher for several flows, not one form. IA2 defines `form` as a form and `section` as "a landing page for a group". The tag is traced to the text, so this is a judgement call rather than a mismatch.
   Fix (optional, change both together): `"label": "+", "type": "section"` and `+ (`section`,`

Confirmed:
- Root "Monzo app", note "tab bar not fully named in the pages read". Traced to line 88: "Monzo app, the surface, drawn without a type tag as IA6 draws the Perqo app (IA6, B.3), its note "tab bar not fully named in the pages read"". IA6 isn't in my folder, so I could not check the IA6 precedent.
- Home `home`, "layout set by the customer". Line 88: "leads to Home (`home`, "layout set by the customer")".
- Save tab `section`, "Savings Pots". Line 88: "Save tab (`section`, "Savings Pots")". Line 72 also: a "Save tab" is where to "Find your Savings Pots".
- Help `section`. Line 88: "and Help (`section`)".
- Accounts `index`, "at the top; Card button on each". Line 88: "Home holds Accounts (`index`, "at the top; Card button on each")".
- Activity `index`, "latest and upcoming payments; See all". Line 88: "Activity (`index`, "latest and upcoming payments; See all", See all being the link the finding-features page names…)".
- Pots `index`, "list or images". Line 88: "Pots (`index`, "list or images")".
- Savings & Investments `section`. Line 88: "Savings & Investments (`section`)".
- Profile `section`, "top left: Settings; Edit layout". Line 88: "Profile (`section`, "top left: Settings; Edit layout")".
- + `form`, "open an account, create a Pot, apply for a loan". Line 88: "+ (`form`, "open an account, create a Pot, apply for a loan")".
- Search `index`, "also on Help; transactions, payees". Line 88: "and Search (`index`, "also on Help; transactions, payees")".
- Tone 2 on every box. Line 88: "Every box is tone 2."
- The figure draws no number, date or identifier beyond the labels and notes above.
- Caption: says what is shown and names section 3. It cites only sources the unit cites: the three Monzo help pages (one title shortened) and White 2023.
- Caption: credits Monzo and gives the date observed, 10 November 2026. It declares that the screens were not seen.
- Kind: a sitemap fits the data, which is a hierarchy of app, top-level areas and Home's areas.
- Notation: the tags used (`home`, `section`, `index`, `form`) are all on IA2's fixed list.
- Notation: tone 2 is set explicitly on every box, so tones don't colour by position. Tone 2 has one meaning. The unit names it in line 14: "Tone 2, "the merchant side and anything outside Perqo"". The caption says "Tone 2: a product outside Perqo". The figure draws no tone 6.
- Matrix checks: do not apply to a sitemap.
- Frames, desktop: frame 1 of 1 is whole in light and dark. The opening frame is clipped at the top by the sticky section bar. That is how the renderer lays out the page, not a figure fault.
- Frames, tablet, phone 390 and phone 430: frame 1 of 1 is whole. Text sits inside its boxes, with no overlap and nothing cut off.
- Frames, phone 360 and phone 320: the drawing is 30 px and 70 px wider than the viewport, and the right edges are cut in frame 1. Frame 2, scrolled sideways, shows them whole, and a "scroll sideways for the whole figure" hint is drawn. Read across the two frames, every box and note is complete. That comes from the renderer stacking nodes and keeping notes on one line at these widths, not from the declaration.
- Light frames read correctly on cream.
- Unit text: no error found in section 3 or in the lines that bear on figure 2.
- Context: a memory snapshot and project instructions were in my context. I used neither. I read only files in /home/claude/w/rc/r1-fig2. I made temporary crops of two frame sheets there and deleted them, and edited nothing.

*Maintainer's note.* Applied: findings 1 and 2 (the caption names the two markets' pages and both White posts' dates) and finding 3 ("+" tagged `section`, in the declaration and the text: IA2's `section` is a landing page for a group, and the page names a choice of several flows). Reopened for round 2.

### Figure 3, re-check 1 (Opus 5.5)

Figure 3 (sitemap): FIX

1. [should-fix] Current (unit-without-figures.md): `The two tone 6 boxes are the two meanings of product; every other box is tone 2.` Also current (declaration.json): `{"label": "Transactions", "type": "index", "tone": 2, "note": "address: /payments"}`
Problem: The Labelling paragraph says "Two labels strain against IA3's D2". The first is the Products / Product catalog pair. The second is "Transactions" opening /payments, which the docs also call "the Payments page". The caption defines tone 6 as "a strain found in this reading", but only the product pair gets tone 6, so the Transactions strain the text names is drawn as tone 2. The tone's one meaning is applied to one strain and not the other.
Fix (declaration.json): `{"label": "Transactions", "type": "index", "tone": 6, "note": "address: /payments"}`. Fix (unit text): `Three boxes are tone 6, the labels that strain: the two meanings of product, and Transactions, whose page is /payments; every other box is tone 2.` Also change `Transactions (`index`, "address: /payments")` to `Transactions (`index`, "address: /payments", tone 6)`.

2. [should-fix] Current (unit-without-figures.md): `Home (`home`, "analytics; Your overview widgets")`. Also current (declaration.json): `{"label": "Home", "type": "home", "tone": 2, "note": "analytics; Your overview widgets"}`
Problem: The note appears in the text only in the paragraph that describes the figure. The sourced account in section 4 lists Home but never says it holds analytics or "Your overview" widgets, and it attributes nothing about Home's contents to Web Dashboard. So the figure draws a claim that the unit's sourced text does not state.
Fix: drop the note. Text becomes `Home (`home`)` and the declaration becomes `{"label": "Home", "type": "home", "tone": 2}`. The other way to fix it is to add a sentence to "Scheme and structure" that quotes Web Dashboard on Home's contents, but only if the writer holds that quote; I could not check it from my folder.

3. [minor] Current (unit-without-figures.md): `The sidebar, as figure 3 draws it.` Also current (declaration.json caption): `the Stripe Dashboard's sidebar and settings as Stripe's documentation describes them`
Problem: The figure also draws Search (index) as a child of Dashboard. The text never places search in the sidebar; it calls search a supplemental route, sourced to Dashboard search. Neither the lead-in nor the caption covers that box.
Fix (text): `The sidebar, Settings and search, as figure 3 draws them.` Fix (caption): `the Stripe Dashboard's sidebar, settings and search as Stripe's documentation describes them`

4. [error, in the unit's own text, section 4 Lifecycle; this is figure 4's material, not figure 3's] Current (unit-without-figures.md): `the first three API statuses show as **Incomplete** (the table adds that under `requires_payment_method `processing` as **Pending**`
Problem: A clause has been lost. The parenthesis never closes and the backtick after `requires_payment_method` is missing, so the sentence breaks and the code spans after it render wrongly.
Fix: `the first three API statuses show as **Incomplete**, `processing` as **Pending**`. If the writer has the dropped clause about `requires_payment_method`, it can be put back as a parenthesis closed before the comma.

Confirmed:
- Labels and type tags traced to unit line 110, which quotes every one exactly as drawn: Dashboard (no tag), Home `home`, Balances `index`, Transactions `index`, Customers `index`, Customer details `detail`, Product catalog `index` tone 6, Shortcuts `section`, Products `section` tone 6, Connect, Payments, Billing and Reporting `section`, More `stack`, Settings `section`, Search `index`.
- Notes traced to line 110, which quotes all of them: "address: /payments", "subscriptions, payments, payment methods, invoices, quotes", "your products and prices", "pinned and recently visited pages", "Stripe's products", "Workflows, Tax, Identity, Atlas, Issuing and others", "Personal, Account, Product", "is: filters, field filters, object IDs".
- Most notes are also backed by the sourced body (section 4, Scheme and structure / Labelling / Search): /payments ("dashboard.stripe.com/payments"); the customer-details list ("including subscriptions, payments, payment methods, invoices, and quotes"); "products and prices for your business"; "your pinned and most recently visited pages"; the More list (Workflows ... Climate); "Personal, Account, and Product"; the `is:` and field filters and identifiers. Home's note is the exception (finding 2).
- The figure draws no number or date beyond the caption's 10 November 2026, which the unit uses throughout.
- Caption: says what the figure shows; names section 4; names its sources (Web Dashboard; Perform searches in the Dashboard), both cited in section 4 and in Sources; gives the date observed, 10 November 2026; credits Stripe; says the Dashboard sits behind a sign-in and was not seen. Its tone 2 and tone 6 meanings match the unit's opening paragraph.
- Kind: a sitemap fits a hierarchy of sidebar sections and their children.
- Notation: every type tag is on IA2's fixed list (section 5.2). The `stack` box for More carries a note saying what repeats. The untagged root is explained in the text ("as IA7 draws Perqo Admin"). Tones are set explicitly. Tone 6 does not carry its meaning alone: line 110 names the tone 6 boxes. The unit's own text names both tones drawn (tone 2 and tone 6, opening paragraph).
- Matrix checks (item 5): not applicable.
- Frames, every width and theme: text sits inside its boxes, nothing overlaps, and the drawing is whole.
  - 390, 430, tablet and desktop: the whole figure fits in one frame.
  - 320 (70 px sideways scroll) and 360 (30 px): the figure scrolls sideways, with a "scroll sideways for the whole figure" hint, and frames 1 and 2 together show every box whole. The cut text at the edge in frame 1 is that scroll, not clipping.
  - Light frames on cream: the tone 6 boxes (olive) are distinct from the tone 2 boxes (orange-brown).
- Renderer-only, layout notes, not faults in the figure:
  - On desktop and tablet, the sitemap wraps the root's children into rows by width, so Search sits alone on a third row.
  - The desktop and tablet opening frames are clipped at the top by the sticky section bar.
  - On phones the figure stacks from level 1, as the declaration's `phone.stack_from: 1` sets.
- Inputs: I read only files in /home/claude/w/rc/r1-fig3 and wrote image crops only to /home/claude/w/rc/r1-fig3/crops. My context held a memory snapshot and Project instructions; I used neither, and used no web, memory, Projects or mcp__ tools.

*Maintainer's note.* Applied: finding 1 (Transactions tone 6, the text names three tone 6 boxes); finding 2 by its second route, a sourced sentence: the maintainer's own search and fetch of Stripe's Web Dashboard page (en-US) confirm Home "provides analytics and charts about your business performance" and its widgets under Your overview, so section 4 now says so and the note stays; finding 3 (lead-in and caption name search); finding 4 as for figure 1. Reopened for round 2.

### Figure 4, re-check 1 (Opus 5.5)

Figure 4 (states): FIX

1. [error] The unit's own text (section 4, Lifecycle paragraph), in unit-without-figures.md
Current: `the first three API statuses show as **Incomplete** (the table adds that under `requires_payment_method `processing` as **Pending**`
Problem: the parenthesis opens and never closes, and the clause inside it stops partway ("the table adds that under `requires_payment_method" then nothing). Some text was lost. A stray backtick also breaks the code spans that follow. The figure is unaffected, but the sentence that sets out the mapping the figure draws is garbled.
Fix: `the first three API statuses show as **Incomplete**, `processing` as **Pending**` (or restore the lost clause about requires_payment_method from the Payment status updates table and close the parenthesis; the source page is outside this folder, so this check cannot say what that clause was).

2. [should-fix] The caption, in declaration.json
Current: `where a page does not name the status a move leaves (the failed attempt, the cancellation), the origin drawn is this unit's reading.`
Problem: this is true of the failed attempt. It is not quite true of the cancellation. The text says the page allows cancel "before a PaymentIntent reaches Processing or Succeeded", so the page does name the statuses a cancel can leave, several of them. Drawing it from Requires payment method only is this unit's choice of one among them.
Fix: `where a page does not name the status a move leaves (the failed attempt) or allows several (the cancellation, drawn once), the origin drawn is this unit's reading.`

3. [minor] The caption, in declaration.json
Current: `State diagram (lifecycles family)`
Problem: IA2 names the family "Rules and lifecycles" (section 1 table), and its own state-diagram caption says "rules and lifecycles family". IA2 never uses "lifecycles family". (Figure 5's caption has the same wording; it is outside this check.)
Fix: `State diagram (rules and lifecycles family)`

4. [should-fix, renderer layout only] In the frames
Current: `customer provides payment information` and `[additional action, such as 3D Secure]` (in declaration.json)
Problem: at every width and in both themes the renderer breaks words inside these transition labels: "informati / on" and "[additiona / l action,". This comes from the renderer wrapping a long label in a narrow gap between two states. It is not a fault in the data.
Fix: no change to the declaration. The renderer's label wrap should break only between words. If the renderer cannot change, `[additional action, e.g. 3D Secure]` is not available, because the label must stay as the text states it.

Confirmed:
- State labels all appear in unit-without-figures.md line 114, as drawn: "Requires payment method, Requires confirmation and Requires action each carry...", "Processing", "Requires capture", "Succeeded, an end state", "Canceled, an end state in tone 6".
- Notes appear as drawn on line 114: "Dashboard: Incomplete" (x3), "Dashboard: Pending", "Dashboard: Uncaptured or Partial capture", "Dashboard: Succeeded", "Dashboard: Cancelled; can't be undone".
- Transition labels appear as drawn on line 114: "customer provides payment information; [additional action, such as 3D Secure]; [asynchronous method] actions handled; [separate capture] actions handled; capture, to Processing or to Succeeded ...; payment flow complete; attempt fails, such as a decline, back to Requires payment method ... drawn here from Processing ...; and cancel ... drawn once, from Requires payment method."
- The figure has nine transitions and the text states nine, with the same origins and targets. The direct card path to Succeeded is left out, as the text says.
- The caption says what the figure shows, cites section 4 and two sources the unit cites (Stripe, "How Payment Intents and Setup Intents work"; "Payment status updates"), credits Stripe and gives the date read (10 November 2026).
- The kind fits: a lifecycle drawn as states.
- Notation follows IA2 §5.2: rounded boxes for states, an inner ring on both end states (Canceled, Succeeded), a start dot with an arrow, solid arrows only, conditions in square brackets, box labels in the product's words in sentence case.
- Tones: tone 2 on every state except Canceled, which is tone 6, one meaning each. The unit's text names both: line 14 for tone 2 and for tone 6 as "a path that ends without success", and line 114 for "Canceled ... in tone 6".
- Item 5 (matrix) does not apply.
- Frames (desktop, tablet, phone 320/360/390/430, dark and light, light judged on cream): text stays inside its boxes, nothing overlaps, and the drawing is whole across the scrolled frames at every width. The only fault is the mid-word wraps in finding 4.
- The phone opening frame is clipped by the sticky section bar. That comes from the renderer and the page layout, not the figure.
- The phone frames scroll sideways in fixed steps (3 to 4 frames), which comes from the screenshot run.

I saw a memory snapshot, Project instructions and attached-project context in my context. I used none of them. I read only files in /home/claude/w/rc/r1-fig4, and wrote crops only to /home/claude/w/rc/r1-fig4/crops/.

*Maintainer's note.* Applied: finding 1 as for figure 1; finding 2 (the caption says the cancellation's origin is one of several the page allows); finding 3 ("rules and lifecycles family", IA2's family name), applied to figure 5's caption as well, which reopens figure 5. Finding 4 was a renderer fault and was fixed in the renderer: `states` in `kit/viz.py` now widens its gap to the longest word of any transition label (a label between two states wrapped at 52 px and `_wrap` broke wider words inside). A build before and after, compared file by file, changed two pages: this unit and Brand + AI A4, whose one states figure had "harassme / nt" broken the same way and now reads "harassment", the rest of A4 byte-identical. A4's figure is reopened. Reopened for round 2.

### Figure 6, re-check 1 (Opus 5.5)

Figure 6 (objects): FIX

Findings

1. [should-fix] The POS to order line has no counts.
   Current (declaration.json): `{"from": "pos", "to": "order", "label": "shows POS and online orders"}`
   Problem: IA2 section 5.2, Labels, says a relationship's label carries "a count at each end", and the legend's "1, 0..*, 1..*" row sets those counts. Every other line in the figure has counts. This one is drawn bare, and the text states none for it.
   Fix (declaration.json): `{"from": "pos", "to": "order", "label": "shows POS and online orders", "from_card": "1", "to_card": "0..*"}`
   Fix (unit-without-figures.md, line 158), Current `Shopify POS shows POS and online orders;` becomes `Shopify POS shows any number of POS and online orders (1 to 0..*);`. The figure's caption and line 318 of the Unsure list already say the counts are this unit's reading.

2. [should-fix] A note in the order box looks like a "Surface: Label" line.
   Current (declaration.json; the same string, in quotes, occurs once in unit-without-figures.md, line 158): `"POS: #1-1005 offline or unpaid"`
   Problem: in IA2 section 5.2, a line "Surface: Label" on a shared object means "that surface's name for it" (also in the legend's "Surface: Label" row). Read that way, the line says the point-of-sale app calls the order "#1-1005 offline or unpaid". What the line actually means is an identifier form the app uses for some orders.
   Fix (both files): `"POS number #1-1005 if offline or unpaid"`

3. [minor] The artefact name in the caption differs from IA2's name for it.
   Current (declaration.json): `Cross-surface map (journeys family)`
   Problem: IA2 names the artefact "Cross-surface interaction map" (section 1.10, and the caption of IA2's own example). The caption rule asks that the caption name the artefact.
   Fix: `Cross-surface interaction map (journeys family)`

4. [minor] The shared objects carry no per-surface name lines. IA2 section 1.10 and the Labels rule give each shared object "its name on each surface" as "Surface: Label" lines. The order and product boxes have none. The text supplies only the admin's lower-case "orders, products" and the POS "Orders screen", so adding these lines would also need text. Optional, and no exact replacement is offered. The lower-case data-model titles `order` and `product` do follow the rule.

5. [minor, renderer] Three points that come from how the renderer lays out the figure, not from the declaration:
   - The triangle on "is available on" is drawn on the line itself and reads like an arrowhead. IA2 says it is "not a head".
   - The two "0..*" counts by the product box's top-left corner (the admin–product and product–channel ends) sit close together. Which line each belongs to has to be read from its position. They do not overlap at any width.
   - The phone opening frames are clipped at the top by the sticky section bar.

Confirmed
- Box "Shopify POS": line 158 reads `Shopify POS lists the Orders screen and "filters: sale type, sale location, delivery type", with the action "-> search orders".`
- Box "Shopify admin": line 158 reads `Shopify admin lists "orders, products, customers", "analytics, marketing, discounts", "Sales channels and apps" and Settings, with the action "-> search, filtered by category".`
- Box "sales channel": line 158 reads `The sales channel lists Online Store, Point of sale, Shop and "social, Google, marketplaces".`
- Box "order": line 158 reads `The order lists "order status: 3 values", "payment status: 9 values, plus Expiring and Unpaid", "fulfillment status: 7 values", "return status: 4 values" and "POS: #1-1005 offline or unpaid".` The counts match line 152: 3 order, 9 payment (plus Expiring and Unpaid), 7 fulfillment and 4 return statuses.
- Box "product": line 158 reads `The product lists "availability per channel".`
- Line "connects" 1 / 1..*: line 158 reads `The admin connects one or more sales channels (1 to 1..*)`.
- Line "shows POS and online orders": line 158 reads `Shopify POS shows POS and online orders`. Source at line 150: "All your POS and online orders display on the Orders screen".
- Lines "manages" 1 / 0..* (two): line 158 reads `the admin manages any number of orders and any number of products (1 to 0..* each)`.
- Line "is available on" 0..* / 0..* with the triangle: line 158 reads `any number of products are available on any number of sales channels (0..* to 0..*), the line labelled "is available on", which reads upwards, towards the channel, so it carries the triangle`.
- The figure draws no date. The caption's "10 November 2026" matches line 142 and the unit's header line 14.
- Caption: it says what the figure shows, names section 6, and lists five Help Center pages, all cited in section 6 and in Sources. It cites nothing the unit does not, gives the date observed, credits Shopify, and says the admin and POS app were not seen (line 142).
- Kind: objects fits surfaces and shared objects with relationships, as IA2 section 1.10 says and as IA2's own cross-surface example uses.
- Relationship reading direction: the level line reads left to right, the top-to-bottom lines read downwards, and the one upward label carries the triangle (IA2 5.2, Labels).
- Tones: every box is tone 2, which line 14 names ("Tone 2, 'the merchant side and anything outside Perqo', carries every box of the five real products") and line 158 repeats ("Every box is tone 2"). Tone 6 and tone 5 are not drawn. Putting the shared objects in tone 2 rather than tone 5 is the unit's declared choice and stays within one meaning per tone. Actions are drawn as "-> verb", and titles are lower case for the objects.
- Matrix check (item 5): does not apply.
- Frames: at desktop, tablet and phone 320, 390 and 430 px, dark and light (light judged on cream), the text sits inside its boxes, nothing overlaps or is cut off, and the sideways-scroll frames together cover the whole drawing. The 360 px sheets were not opened.
- Unit text (item 7): no errors found in section 6 apart from finding 1's missing count and finding 2's note.
- I made one crop inside my folder to view the phone 430 sheet and deleted it afterwards.
- A memory snapshot and the Project instructions were present in my context. I used neither and read nothing outside the folder.

*Maintainer's note.* Applied: finding 1 (counts 1 to 0..* on the POS to order line, and in the text); finding 2 (the note reads "POS number #1-1005 if offline or unpaid", in the declaration and the text); finding 3 ("Cross-surface interaction map", IA2's name). Finding 4 offers no exact replacement and would need text the sources do not give: recorded, not applied. Finding 5 rests on the renderer: recorded, not applied. Reopened for round 2.

### Figure 7, re-check 1 (Opus 5.5)

Figure 7 (matrix): PASS

The figure itself is correct. There is one error in the unit's text, outside the figure, and one minor wording point.

1. [error] The unit's text, section 4, Lifecycle paragraph (not the figure)
Current (unit-without-figures.md, occurs once): `show as **Incomplete** (the table adds that under `requires_payment_method `processing` as **Pending**`
Problem: the parenthesis never closes and a code span is left open. The sentence about the table's edge case breaks off, and the mapping list that follows runs into it. The mapping cannot be read as written.
Fix: `show as **Incomplete**, `processing` as **Pending**` (this removes the broken clause; the sentence's later caveat on edge cases already covers it). If the writer has the lost clause, they can restore it as a closed parenthesis instead.

2. [minor] Airbnb's Strain cell
Current (declaration.json, occurs once): `placement inferred from listing text`
Problem: section 5 says the category is inferred from "its text and photos" and from "titles, written descriptions, photo captions". "Listing text" leaves out the photos. The cell does match the line-174 description word for word, so check 1 passes.
Fix: `placement inferred from listing content`, with the same change in unit-without-figures.md line 174 (`placement inferred from listing text` occurs once there).

What I confirmed:
- **Check 1, labels:** every column label, row label and cell occurs as drawn in the line-174 paragraph: "The rows are GOV.UK, Monzo, Stripe, Airbnb and Shopify, in tone 2; the columns are Level, Scheme, Structure, Search, Shaping decision and Strain." Each row's cells are quoted there in order. For example: "GOV.UK: IA5 website; topic; hierarchy and taxonomy; site search, filters; navigation from one taxonomy; three topic systems." and "Airbnb: IA8 lifecycle; place, then category; database; place box 2022, own words 2026; categories beside place; placement inferred from listing text." The Monzo, Stripe and Shopify rows match the same way.
- **Check 1, legend:** the legend matches: 'The legend reads "tone 2: a product outside Perqo" and "tone 6: a strain found in this reading".'
- **Check 1, numbers and dates:** none is drawn without support. "2022" rests on the 2022 release (section 5); "2026" rests on "Airbnb 2026 autumn update", 30 September 2026 (section 5) and on section 7's "since September 2026".
- **Cells traced to sections 2 to 6:**
  - GOV.UK: topic scheme (s2); "three topic systems" (s2: "in 2021 there were three topic systems").
  - Monzo: "by account first, then by time" and "Home, is a summary" (s3); "moved features need a help page" (s3: "the makers wrote a page to find them again").
  - Stripe: "two meanings of product" (s4 figure 3 text).
  - Shopify: "four status sets" (s6 strain); "one admin for every channel" (s6 shaping decision).
  - Deliverable B gives the same values in fuller form.
- **Check 2, caption:** it says what is shown, names section 7 and Deliverable B, and gives the source as sections 2 to 6 and the makers' documents cited there, read on 10 November 2026. It cites nothing the unit does not cite. A product credit is not needed, because no single product's structure is redrawn; the date is given.
- **Check 2, family:** "structure family" is defensible, since the dimensions are structural. IA2's catalogue has no "comparison" artefact, so the family is a convention here, not an IA2 entry.
- **Check 3:** the kind fits. These are items (five products) by dimensions (six columns), which IA2 section 5.2 says a matrix is for.
- **Check 4, tones:** tone 2 is used for products outside Perqo and tone 6 for the strain cells, one meaning each and consistent with IA2's sheet ("anything outside Perqo"; "a fault found in a review"). The unit names both tones: line 14 for tone 2, and for tone 6 "the strains this reading finds"; line 174 says "The Strain column is tone 6." No type tags apply to a matrix. The tone is not the only carrier of meaning: the column header "Strain" and the legend also carry it.
- **Check 5, row labels:** they are short (longest "Shopify" or "GOV.UK"), and each is named in the line-174 sentence and in the section 2 to 6 headings. On 320 px the pinned label column leaves about two cell columns visible, and the cells keep room.
- **Check 6, frames:** I checked desktop, tablet, phone 320/360/390/430, dark and light. Text sits inside every cell, nothing overlaps or is cut off, and all six columns appear across the phone scroll frames (four frames at 320, three at 390). The light theme's tone 2 (warm beige) and tone 6 (greyer tan) can be told apart on cream; the dark theme's brown and olive likewise.
- **Check 6, renderer-only effects:** on phones the cells fade under the pinned label column and at the right edge, and the legend scrolls with the figure, so at the last frame only "...d in this reading" shows. The legend is whole across the frames. Both effects come from the renderer's sideways-scroll layout, not from the figure.
- **Inputs:** I saw a memory snapshot and the Project instructions in my context and used none of them. I used only files in /home/claude/w/rc/r1-fig7; my crops are in /home/claude/w/rc/r1-fig7/crops.

*Maintainer's note.* Passed. Finding 1 as for figure 1. Finding 2 corrects text the figure draws ("listing text" against section 5's "text and photos"): applied in the declaration and the text, so the figure is reopened for round 2.

### Figure 8, re-check 1 (Opus 5.5)

Figure 8 (matrix): FIX

The fix verdict comes from one should-fix. Every value the figure draws is stated in the text, and the frames render cleanly. A separate error in section 4's text is reported as finding 4.

1. [should-fix] Current (unit-without-figures.md, line 178): `GOV.UK: 16 topics; taxonomy principles; step by step journeys; none in the pages read; none in the pages read.` The same pattern appears in `Stripe: sidebar; 26 is: types; PaymentIntent statuses;` and `Airbnb: four tabs; 55 categories (2022); four status groups;`. Also in declaration.json: `"16 topics; taxonomy principles"`, `"sidebar; 26 is: types"`, `"four tabs; 55 categories (2022)"`.
   Problem: line 178 uses the semicolon both between cells and inside a cell. So the GOV.UK, Stripe and Airbnb sentences list five values for four columns, and a reader of the text cannot tell which value belongs to which column. The Shopify sentence avoids this by using commas inside its cell.
   Fix: in declaration.json replace `"16 topics; taxonomy principles"` with `"16 topics, taxonomy principles"`, `"sidebar; 26 is: types"` with `"sidebar, 26 is: types"`, and `"four tabs; 55 categories (2022)"` with `"four tabs, 55 categories (2022)"`. In the unit text replace `16 topics; taxonomy principles; step by step` with `16 topics, taxonomy principles; step by step`, `sidebar; 26 is: types;` with `sidebar, 26 is: types;`, and `four tabs; 55 categories (2022);` with `four tabs, 55 categories (2022);`.

2. [minor] Current (unit-without-figures.md, line 172): `Monzo publishes its surface's areas and nothing in the other layers.`
   Problem: section 3 says "the pages draw two states, upcoming and done". So the figure's Monzo cell "none in the pages read" in the lifecycle layer, and this sentence, need the reason they hold: no lifecycle is published, only a list label.
   Fix: `Monzo publishes its surface's areas and nothing in the other layers: Activity's "latest and upcoming payments" names two states but publishes no lifecycle.`

3. [minor] Current (declaration.json): `{"mark": "tone 6", "means": "none in the pages read", "tone": 6}`. In the unit text: `"tone 6: none in the pages read"`.
   Problem: the legend repeats a cell value instead of giving tone 6's meaning. IA2 defines tone 6 as "a stop, meaning a path that ends without success, or a fault found in a review", and line 14 of the unit ties this use to "the gap this review finds in a published map". Figure 7's legend does state the meaning ("a strain found in this reading"). Some of these cells, such as Monzo's, which sits behind a sign-in, reflect what could be read rather than a fault in the product, so the legend should state the meaning it applies.
   Fix: in declaration.json, `{"mark": "tone 6", "means": "a gap found in this reading: none in the pages read", "tone": 6}`. In the unit text, `"tone 6: a gap found in this reading: none in the pages read"`.

4. [error, unit text, item 7] Current (unit-without-figures.md, line 104): `the first three API statuses show as **Incomplete** (the table adds that under `requires_payment_method `processing` as **Pending**`
   Problem: the sentence is broken. A parenthesis and a code span are left open, and the clause after "under `requires_payment_method`" is missing, so the Markdown renders incorrectly.
   Fix: `the first three API statuses show as **Incomplete**, `processing` as **Pending**`. If the page read stated a qualifier for `requires_payment_method`, the writer should restore it from that page. I cannot source what it said.

5. [minor, unit text, item 7] Current (unit-without-figures.md, line 319): `- Object: the Stripe PaymentIntent and its Dashboard status mapping, section 4`
   Problem: this is a stray line in the Unsure list. It names no uncertainty.
   Fix: delete the line (``).

Confirmed:
- Columns: "Surface layer, Lifecycle layer, Decision layer and Connections" (line 178).
- Perqo row: "Perqo map (IA8): D.1, X-01 to X-13; D.2, CL- and EL-; D.3, DT-1 to DT-3; D.4, J-01 to J-14." (line 178). These are consistent with line 172 (X-01 to X-13, CL-1 to CL-6 and EL-1 to EL-6, DT-1 to DT-3, J-01 to J-14).
- GOV.UK cells: "16 topics; taxonomy principles; step by step journeys; none in the pages read; none in the pages read" (line 178). The values are stated, but the cell boundaries are ambiguous (finding 1).
- Monzo cells: "Home's areas; none in the pages read, in the other three columns" (line 178).
- Stripe cells: "sidebar; 26 is: types; PaymentIntent statuses; none in the pages read; status mapping table" (line 178). This matches section 4's 26 `is:` types and the mapping table.
- Airbnb cells: "four tabs; 55 categories (2022); four status groups; 24 hours, then Expired; none in the pages read" (line 178). This matches sections 5 and 7.
- Shopify cells: "admin, channels, POS, online orders on POS; four status sets; products available by default; none in the pages read" (line 178). This matches line 172.
- Tone assignment: "Each "none in the pages read" is tone 6; the other cells of the five take their row's tone 2" (line 178). The Perqo row is tone 5 (lines 14 and 178).
- Legend text matches line 178 exactly: "tone 5: the Perqo map (Perqo is fictional)", "tone 2: a product outside Perqo", "tone 6: none in the pages read".
- Caption: it names section 7 and the sources (IA8, Deliverable, D.1 to D.4; sections 2 to 6; read 10 November 2026), all of which the unit cites (lines 26 and 172). It marks Perqo as fictional. A comparison matrix redraws no product structure, so no product credit is needed.
- Kind: matrix fits, with items (the Perqo map and five products) set against dimensions (three layers and their connections).
- Notation: tones 2, 5 and 6 each match IA2 section 5.2. All three are named in the unit's text (lines 14 and 178). A matrix uses no type tags.
- Row labels: the longest is "Perqo map (IA8)". At 320 px the pinned label column leaves about half the width for cells, and every label is traced to line 178.
- Frames, all widths and both themes: text sits inside its cells, nothing overlaps, and nothing is cut off except by the intended sideways scroll. At 320 the sheet has 5 frames, at 430 it has 3, and tablet and desktop are whole in one frame. The fading cell edges, the legend cut at the frame edge and the fixed scroll steps come from the renderer's scroller, not the figure.
- Light theme on cream: tone 2 (peach) and tone 6 (khaki) are close but can be told apart, and the cell words carry the meaning (WCAG 1.4.1). This is a theme.css matter, not this figure's.
- Context: a memory snapshot and project instructions were present in my context. I used neither. I read only files in /home/claude/w/rc/r1-fig8 and wrote crops only to /home/claude/w/rc/r1-fig8/crops.

*Maintainer's note.* Applied: findings 1, 2 and 3 (commas inside the three cells, in the declaration and the text; the Monzo sentence; the legend's meaning for tone 6) and finding 4 as for figure 1. Finding 5 (delete the Object line) not applied: the Object line closes the unsure list by method.md section 4 and write-unit section 5 (P96). Reopened for round 2.

**Round 2.** Every DD-IA1 figure was re-checked, figure 5 because the family name in its caption changed, and Brand + AI A4's states figure because the renderer change redrew it. Fresh Opus 5.5 agents, the same inputs as round 1 from a new build's frames (the A4 agent: A4 without its figures, its captions, its figure 2's declaration and frames, told what the renderer change was). Transcript checks: each claude-opus-5-5; no web or forbidden tool; every path inside its folder, and the figure 7 agent's one read under `/root/.claude/` its own saved result, by the exact path its result gave.

### Figure 1, re-check 2 (Opus 5.5)

Figure 1 (sitemap): FIX

1. [should-fix] Current (declaration.json): `{"label": "6 more links", "type": "stack", "tone": 2}`
   Problem: IA2, section 5.1 says a page stack is "one box tagged `stack`, with a note saying what repeats". The notation sheet says the same: "Box tagged `stack`, note says what repeats". This stack has no note. Every other stack in the figure has one. The six links are also of different kinds, so without a note the reader cannot tell what the box holds. Section 2 already names the six: "Guidance and regulation", "Research and statistics", "Policy papers and consultations", "Transparency", "How government works" and "Get involved".
   Fix: `{"label": "6 more links", "type": "stack", "tone": 2, "note": "Guidance and regulation to Get involved"}`
   Make the matching change in unit-without-figures.md. Current: `and 6 more links (`stack`)`. Fix: `and 6 more links (`stack`, "Guidance and regulation to Get involved")`

2. [minor] Current (unit-without-figures.md): `leads to six groups`
   Problem: two of the six root children are not groups. Search GOV.UK is a single `index` page and Content pages is a `stack` of pages. "Leads to" also suggests the home page links to all six. The text itself says topic pages are "reached from content pages' sidebar and breadcrumbs". In IA2 notation a line without a head means "contains", not "links to".
   Fix: `holds six parts`

Confirmed:
- Each of these labels and notes occurs exactly as drawn in the text. All of them are in the line beginning "The structure, as figure 1 draws it." (section 2, line 66 of unit-without-figures.md):
  - GOV.UK (`home`), "Popular on GOV.UK; Featured"
  - Services and information (`section`, 16 topics); Benefits (`section`)
  - Benefits and financial support pages (`stack`, "7 of 8 labels open with the same four words", tone 6)
  - Manage an existing benefit, payment or claim (`section`)
  - 15 other topics (`stack`, "Births, deaths, marriages and care to Working, jobs and pensions")
  - Government activity (`section`, 8 links); Departments (`index`); News (`index`); 6 more links (`stack`)
  - Search GOV.UK (`index`), "more than 4 million searches a month"
  - Topic pages (`stack`, tone 6), "the taxonomy, one of three topic systems in 2021; reached from content pages' sidebar and breadcrumbs"
  - Step by step pages (`stack`), "end to end journeys"
  - Content pages (`stack`), "more than half a million pages (2021)"
  - "Every other box is tone 2."
- The numbers agree with the section 2 body:
  - 16 topics: Benefits plus 15 others.
  - 8 links: 8 listed, which is 2 drawn plus 6.
  - 7 of 8: seven children start with "Benefits and financial support" (four words); the eighth is "Manage…".
  - "more than 4 million times a month" (Fraser and Crusellas 2024).
  - Three topic systems and more than half a million pages, 2021 (Dub 2021).
  - Sidebar links and breadcrumbs (taxonomy principles, 2019).
  - "end to end journey" (Design System).
- Caption:
  - It says what the figure shows and names section 2.
  - Its sources are gov.uk, gov.uk/browse, the Benefits content API record, Dub 2021, the taxonomy principles 2019, Fraser and Crusellas 2024, and the Design System's Step by step navigation. Every one is cited in section 2 and listed in Sources. It cites nothing the unit does not.
  - It gives the date observed (10 November 2026) and the credit (GOV.UK, Government Digital Service), and names the decision it supports.
  - The source document is titled "GOV.UK Taxonomy principles" with a capital T; the caption's lower-case "taxonomy" is not an error.
- Kind: a hierarchy of pages, so a sitemap fits.
- Notation:
  - The type tags `home`, `section`, `index` and `stack` are all from IA2's fixed list.
  - Two tones are used: tone 2 for outside Perqo and tone 6 for a fault found in a review. Each has one meaning, and tones are set explicitly, not by position.
  - The unit's own text names both tones (intro paragraph, line 14, and line 66), tone 6 included.
  - Tone 6 is not the only carrier of its meaning: the notes of both tone-6 boxes state the strain.
- Matrix check: not applicable (sitemap).
- Frames, every width (phone 320, 360, 390, 430, tablet, desktop) in both themes:
  - Text sits inside its boxes, nothing overlaps, and the drawing is whole.
  - Light frames read clearly on cream. The tone 6 olive fill is told apart from the tone 2 tan in both themes, though the difference is subtle.
- Renderer-only notes, not errors in the figure:
  - On desktop and tablet the root's six children wrap into two rows by width.
  - Phones (stack_from 1) draw a vertical indented list. At 320 px (70 px) and 360 px (30 px) the figure scrolls sideways; the second frame shows the right edges whole.
  - The desktop light opening frame is clipped at the top by the sticky section bar. The frames sheet shows the whole figure.
- Unit text: no other error found in section 2 or in the related Sources and Unsure entries.
- I saw a memory snapshot and the attached Project's instructions in my context and used neither. I read only files in /home/claude/w/rc/r2-fig1. I made two crops there to inspect the 320 px frames and deleted them afterwards.

*Maintainer's note.* FIX. Applied: finding 1 (the `stack` box gets the note "Guidance and regulation to Get involved", in the declaration and the text, as IA2, section 5.1 requires) and finding 2 ("holds six parts"). Reopened for round 3.

### Figure 2, re-check 2 (Opus 5.5)

Figure 2 (sitemap): PASS

There is one minor finding. It does not block the pass.

Findings

1. [minor] The caption shortens a source title.
   - Current (declaration.json, occurs once): `We're changing how search works;`
   - Problem: the unit gives this source's full title as "We're changing how search works in the Monzo app" (section 3 and Sources). The caption cuts it to "We're changing how search works". The source can still be identified, but the title is not given as the unit cites it. The same shortened text is in captions.md.
   - Fix: `We're changing how search works in the Monzo app;`

What I confirmed

- **Labels and notes match the text exactly.** Every one occurs in unit-without-figures.md line 88 ("The app map, as figure 2 draws it. …"):
  - root "Monzo app", no type tag, note "tab bar not fully named in the pages read"
  - Home (`home`, "layout set by the customer"); Save tab (`section`, "Savings Pots"); Help (`section`)
  - Accounts (`index`, "at the top; Card button on each")
  - Activity (`index`, "latest and upcoming payments; See all")
  - Pots (`index`, "list or images")
  - Savings & Investments (`section`)
  - Profile (`section`, "top left: Settings; Edit layout")
  - + (`section`, "open an account, create a Pot, apply for a loan")
  - Search (`index`, "also on Help; transactions, payees")
  - "Every box is tone 2."
- **No extra content.** The figure draws nothing the text does not state. It has no numbers or dates.
- **The facts behind the boxes are in section 3.** Line 72 gives accounts at the top, Activity, Pots as a list or images, Savings & Investments, the Save tab and the Card button. Line 74 gives what "+" opens. Line 76 gives the profile photo top left, the layout edit, and that the tab bar is not named. Line 78 gives search on Home and Help, transactions and payees.
- **Caption content.** It says what the figure shows and names section 3. Every source it names is cited in section 3: the three Monzo help pages, and White, Monzo blog, 1 and 6 November 2023.
- **Caption credit and limits.** It credits Monzo and the date observed (10 November 2026). It states the sign-in limit and the two-market join, which matches line 72 and the Unsure list.
- **Kind.** A hierarchy of app, areas and Home's parts, so a sitemap fits.
- **Notation.**
  - The type tags (`home`, `section`, `index`) are all from IA2 section 5.2's fixed list.
  - The root has no tag; line 88 explains this ("drawn without a type tag as IA6 draws the Perqo app").
  - Every box sets tone 2 explicitly. It has one meaning, and unit line 14 names it ("the merchant side and anything outside Perqo").
  - The figure draws no tone 6, and nothing in it needs tone 6.
- **Matrix rules.** Not applicable; this figure is a sitemap.
- **Frames: whole and readable at every width and theme.** Nothing overlaps, and text sits inside its boxes.
  - Desktop and tablet: one frame each. Home's seven children are stacked in a column; Save tab and Help sit beside Home.
  - Phone 390 and 430: one frame each, fully stacked.
  - Phone 320 (70 px sideways scroll) and 360 (30 px): two frames each. Together they show every note in full, including "See all", "apply for a loan" and "payees". The right-edge fade and the "scroll sideways for the whole figure" line are the renderer's cue for this scroll.
  - Renderer-only notes: the desktop opening frame has the root and Home row clipped by the sticky section bar; that is the renderer, and the frame sheet shows the whole figure. The sideways steps on 320 and 360 also come from the renderer.
- **Light theme.** Boxes read correctly on cream.
- **Unit text.** I found no error in section 3 or the other passages I checked.
- **Scope.**
  - I read only my folder. I wrote crops of the phone 320 and 360 frame sheets into it: phone320-dark-a.png, phone320-dark-b.png, phone320-light-a.png, phone320-light-b.png, phone360-dark-a.png, phone360-dark-b.png, phone360-light-a.png and phone360-light-b.png, all in /home/claude/w/rc/r2-fig2.
  - My context held a memory snapshot and Project instructions. I used neither, and no web, memory, Project or mcp__ tool.

*Maintainer's note.* PASS: the loop ends. The minor (the caption's shortened title of Monzo's search page) would change the declaration once more and every word it touches is traced: recorded, not applied.

### Figure 3, re-check 2 (Opus 5.5)

Figure 3 (sitemap): PASS

Findings

1. [minor] Current (declaration.json, caption): `(Stripe docs: Web Dashboard; Perform searches in the Dashboard)`
   Problem: The tone-6 Transactions box and its note "address: /payments" rest on the section 4 labelling sentence. That sentence cites both Web Dashboard and "Payment status updates": "(Web Dashboard; Stripe, "Payment status updates", ... read 10 November 2026; vendor documentation)". The caption lists only Web Dashboard and Dashboard search, so it may leave out a source the drawn strain depends on. This matters only if the /payments address or "the Payments page" comes from the second page; the text does not say which page supplies which.
   Fix: `(Stripe docs: Web Dashboard; Payment status updates; Perform searches in the Dashboard)`. The same change goes in captions.md, Figure 3.

2. [minor] Current (declaration.json): `"note": "Stripe's products"`
   Problem: In the light (e-ink cream) theme, the tone 6 boxes (olive fill and border) and the tone 2 boxes (tan fill, rust border) are only slightly different. Nothing in a tone-6 box says it marks a strain, and the caption names tone 6's meaning without saying which boxes carry it. IA2 §5.2 says "No tone is the only carrier of its meaning". For Transactions ("address: /payments") and the pair Product catalog / Products ("your products and prices" / "Stripe's products"), the notes do imply the strain, so this is borderline.
   Fix (optional): leave it as is, or make the strain explicit in the unit text and the declaration together: `"note": "Stripe's products; strain: two meanings of product"`. Section 4's figure paragraph would then change `Products (`section`, "Stripe's products", tone 6)` to `Products (`section`, "Stripe's products; strain: two meanings of product", tone 6)`.

Confirmed
- Root "Dashboard", tone 2, no type tag: text line 110 has "Dashboard, the surface, drawn without a type tag as IA7 draws Perqo Admin (IA7, Deliverable C)".
- Home `home`, "analytics; Your overview widgets": line 110 has "Home (`home`, "analytics; Your overview widgets")".
- Balances `index`: line 110 has "Balances (`index`)".
- Transactions `index`, tone 6, "address: /payments": line 110 has "Transactions (`index`, "address: /payments", tone 6)".
- Customers `index` holding Customer details `detail`, "subscriptions, payments, payment methods, invoices, quotes": line 110 has "Customers (`index`), which holds Customer details (`detail`, "subscriptions, payments, payment methods, invoices, quotes")".
- Product catalog `index`, tone 6, "your products and prices": line 110 has "Product catalog (`index`, "your products and prices", tone 6)".
- Shortcuts `section`, "pinned and recently visited pages": line 110 has "Shortcuts (`section`, "pinned and recently visited pages")". The quote from the source in line 94 is "your pinned and most recently visited pages"; the note paraphrases it, unquoted, and matches line 110.
- Products `section`, tone 6, "Stripe's products", with Connect, Payments, Billing, Reporting (`section`) and More (`stack`, "Workflows, Tax, Identity, Atlas, Issuing and others"): line 110 has "Products (`section`, "Stripe's products", tone 6), which holds Connect, Payments, Billing and Reporting (each `section`) and More (`stack`, "Workflows, Tax, Identity, Atlas, Issuing and others")". Line 94 gives the full More list.
- Settings `section`, "Personal, Account, Product": line 110 has "Settings (`section`, "Personal, Account, Product")".
- Search `index`, "is: filters, field filters, object IDs": line 110 has "Search (`index`, "is: filters, field filters, object IDs")".
- Tones: line 110 has "Three boxes are tone 6 ... every other box is tone 2". The declaration matches: Transactions, Product catalog and Products are tone 6, the rest tone 2, and Products' children are set to tone 2 explicitly.
- The figure draws no number or date beyond the text. The date in the caption, 10 November 2026, matches the unit's lines 14 and 94.
- Caption: it says what the figure shows (sidebar, settings, search), names section 4, gives both sources (each in the unit's Sources) and the date read, says the Dashboard was not seen, and credits Stripe.
- Kind: the sidebar is a hierarchy, so a sitemap fits.
- Notation: every tag (home, index, detail, section, stack) is on IA2's fixed list, and a page box without a tag matches the unit's stated convention for a surface. Tone 2 and tone 6 each have one meaning, consistent with IA2 §5.2 ("Tone 2: the merchant side and anything outside Perqo"; "Tone 6: a stop, meaning a path that ends without success, or a fault found in a review"). The unit's line 14 names both, tone 6 included, as "the strains this reading finds".
- Type choices that are this unit's reading: Shortcuts tagged `section` with no children, More tagged `stack` for the other products, Search tagged `index`. All are consistent with the text and with IA2's tag definitions; not an error.
- Matrix check (item 5): not applicable.
- Frames, desktop and tablet, dark and light: one frame, whole, with no overlap and all text inside its box. Search sits alone on a third row. That comes from the renderer wrapping the root's children into rows by width, not from the figure.
- Frames, phone 320 and 360: the figure scrolls sideways (70 px at 320) and carries the hint "scroll sideways for the whole figure". Across the two frames every note sits inside its box and nothing is cut off. The clipping you see in one frame comes from the screenshot run's fixed scroll steps.
- Frames, phone 390 and 430: one frame, whole and stacked, text inside every box, in both themes. I opened the 430 light sheet and judged it on cream; I did not open the 360 or 390 sheets or any phone opening frame.
- Opening frames: the desktop light opening frame has its top hidden under the sticky section bar. That is the renderer's sticky bar, not a figure fault; the frames sheet shows the whole figure.
- Unit text: no error found in section 4 or in the lines describing figure 3.
- Context: a memory snapshot and project instructions were in my context. I used neither. I read only files in my folder; the two crops (crop320a.png, crop320b.png) were made inside it.

*Maintainer's note.* PASS: the loop ends. Both minors (a third source in the caption; an optional strain note) would change the declaration once more and touch words already traced: recorded, not applied.

### Figure 4, re-check 2 (Opus 5.5)

Figure 4 (states): PASS

I found no errors. The three minor findings below are optional.

1. [minor] Current, in unit-without-figures.md: `Canceled, an end state in tone 6, "Dashboard: Cancelled; can't be undone".`
Problem: section 4's paragraph on figure 4 names tone 6 but does not say the other six states are tone 2. The paragraphs on figures 3, 5 and 6 each say so. Tone 2 is named only in the intro (line 14) and in the caption. Check 4 is met, but less directly than for the other figures.
Fix: `Canceled, an end state in tone 6, "Dashboard: Cancelled; can't be undone"; the other states are tone 2.`

2. [minor] Current, in unit-without-figures.md: `carries every box of the five real products, because all five are outside Perqo`
Problem: tone 2 does not carry every box of the five products. The same paragraph says tone 6 marks paths that end without success and strains, and figure 4's Canceled box (like figure 3's three strain boxes and figure 5's end state) is tone 6. This is an error in the unit's own text, not in the figure.
Fix: `carries every box of the five real products that tone 6 does not mark, because all five are outside Perqo`

3. [minor] Current, in declaration.json (the same string occurs once in the unit text, line 114): `Dashboard: Cancelled; can't be undone`
Problem: a reader can take the whole note as the Dashboard's label. In fact "Cancelled" comes from the mapping table on Payment status updates, and "can't be undone" comes from the lifecycle page, How Payment Intents and Setup Intents work (line 104). The figure is accurate to the text, so this is about clarity only.
Fix, optional, in both the declaration and line 114: `Dashboard: Cancelled; cancellation can't be undone`

Confirmed:
- States: all seven labels occur in unit line 114 exactly as drawn: "Requires payment method, Requires confirmation and Requires action"; "Processing"; "as Requires capture"; "Succeeded, an end state"; "Canceled, an end state in tone 6".
- Notes: all occur in line 114 exactly as drawn: "each carry "Dashboard: Incomplete""; "Processing carries "Dashboard: Pending""; "Requires capture "Dashboard: Uncaptured or Partial capture""; ""Dashboard: Succeeded""; ""Dashboard: Cancelled; can't be undone"".
- Transitions: all nine labels occur in line 114 exactly as drawn: "customer provides payment information; [additional action, such as 3D Secure]; [asynchronous method] actions handled; [separate capture] actions handled; capture, to Processing or to Succeeded "depending on the payment method"; payment flow complete; attempt fails, such as a decline, back to Requires payment method, ... drawn here from Processing ...; and cancel, ... drawn once, from Requires payment method".
- Moves match the text: failure from Processing, cancel from Requires payment method, capture to both Processing and Succeeded, and no direct card path to Succeeded ("so it is not drawn").
- Figure draws no number, date or identifier beyond those above.
- Caption: names the artefact and its family, what it shows and the decision it supports, and section 4. Both sources it cites are in the unit's Sources list and cited in section 4. It gives the date read (10 November 2026), credits Stripe, and declares the two origins that are the unit's own reading.
- Kind: states fits a lifecycle.
- Notation: rounded boxes; start dot and arrow; inner ring on the two end states (Succeeded, Canceled); arrows for state changes; conditions in square brackets; nothing dashed; no type tags, as is right for a state diagram.
- Notes in "Surface: Label" form match the vocabulary mapping that section 4 ties to IA2 section 5.2.
- Tones: tone 2 for outside Perqo; tone 6 only on Canceled, an end without success. Each has one meaning, and both are named in the caption and the text (line 14; line 114 for tone 6).
- Spelling: "Canceled" (state) versus "Cancelled" (Dashboard) is explained in the text and the Unsure list.
- Check 5 (matrix) does not apply.
- Frames at tablet and desktop, dark and light: whole figure in one frame. All text sits inside its boxes; no overlaps, nothing cut off. The tone 6 box is distinct on cream and on dark. No line crossings.
- Frames at phone 320, 360, 390 and 430, dark and light: the figure scrolls sideways (4 frames at 320 and 360, 3 at 390 and 430) and is whole across the frames. The faded edges and part-boxes at the frame edges are the renderer's scroll cut.
- Renderer-only, not a figure error: on phones the figure opens scrolled to 58 px; the start dot is still visible in frame 1. The screenshot run steps in fixed increments.
- Sources used: I read only my folder (unit-without-figures.md, captions.md, declaration.json, IA2.md, frames/) and wrote crops only to /home/claude/w/rc/r2-fig4/crops.
- Context: I saw a memory snapshot and the Project instructions in my context and used neither. I used no web, memory, Projects or mcp__ tool.

*Maintainer's note.* PASS: the loop ends. Findings 1 and 2 are on the unit's text and were verified and applied (section 4 names the other states' tone 2; the introduction says tone 2 carries every box "that tone 6 does not mark"); the declaration is unchanged. Finding 3 is optional wording of a note already traced: recorded, not applied.

### Figure 5, re-check 2 (Opus 5.5)

Figure 5 (states): PASS

Findings

1. [minor] Current (declaration.json): `What is the pending status for a reservation?`
Problem: the caption shortens the source's title. The unit cites it as `What is the "pending" status for a reservation?` in section 5 and in Sources, article 2810. The caption drops the quotation marks around "pending", so the caption and the unit name the source differently.
Fix: `What is the \"pending\" status for a reservation?` (in the JSON string; it renders as What is the "pending" status for a reservation?)

2. [minor, the unit's own text] Current (unit-without-figures.md): `One status was read in full. The article gives it two causes:`
Problem: the sentence before this one cites only "Understanding your reservation status" (article 363), so "The article" first reads as that page. The two causes actually come from the pending article (2810), which is cited only at the end of the next sentence.
Fix: `One status was read in full, Pending, in the help centre's article on it. That article gives it two causes:`

Confirmed
- The state label `Pre-trip statuses` occurs in section 5 as "Pre-trip statuses" (in the four headings and in "Pre-trip statuses starts, with the note…").
- The state label `During-trip status` occurs in section 5: "During-trip status".
- The state label `Post-trip statuses` occurs in section 5 ("then Post-trip statuses, an end state"), so drawing it as an end state is in the text.
- The state label `Canceled, declined, or expired statuses` occurs in section 5: "ends at Canceled, declined, or expired statuses, an end state in tone 6".
- The note `includes Pending (assumed): the host has 24 hours to accept or decline` matches section 5 word for word ("with the note "includes Pending (assumed): the host has 24 hours to accept or decline""). It is backed by "the host "has 24 hours to accept or decline the request"", and the Unsure list marks the assumption.
- The note `Declined or Expired: payment refunded` matches section 5 word for word ("with the note "Declined or Expired: payment refunded""). It is backed by "becomes "Declined" or "Expired" and "your payment will be refunded…"".
- The transition label `host declines, or no response within 24 hours` matches section 5 word for word ("a path labelled "host declines, or no response within 24 hours""). The pre to during and during to post moves carry no label, and none is stated.
- Tones: tone 2 on three boxes and tone 6 on the stop match section 5 ("an end state in tone 6… The other boxes are tone 2"). The intro paragraph names both tones as IA2 defines them, tone 6 included.
- Caption: it names the artefact and family, says what is shown and the decision ("what a two-sided purchase lifecycle must name"), and names section 5 and the two help-centre pages section 5 cites. It credits Airbnb, gives the date observed (10 November 2026) and states what was not seen. It cites nothing the unit does not cite.
- Kind: a lifecycle drawn as states fits the data. The mixed-level choice (groups drawn as states) is declared in the unit's text as IA2's third fault, so the reader is warned.
- Notation, checked against IA2 section 5.2 and the legend: rounded boxes, an inner ring on both end states, a start dot with an arrow, solid arrows only, no type tags (correct for states), "assumed" as a status word in a note, and box labels in the product's own words.
- Frames, phone 320, 360, 390 and 430, tablet and desktop, dark and light (light judged on cream): text sits inside every box, nothing overlaps or is cut off, and the drawing is whole across the frames at every width. At phone widths the figure scrolls sideways with a fade at the edges and the screenshot run steps through fixed offsets; that is how the renderer lays the figure out, not a fault in the figure. Tone 6 (olive with a double ring) reads as distinct from tone 2 in both themes.
- Matrix check (item 5): not applicable to a states figure.
- Sources: I read only files in /home/claude/w/rc/r2-fig5. A memory snapshot and project instructions were in my context; I used neither. No web, memory, Projects, Artifact or mcp__ tool was used.

*Maintainer's note.* PASS: the loop ends. Finding 1 (the caption's quotation marks) touches words already traced: recorded, not applied. Finding 2 is on the unit's text, verified (the sentence before names article 363) and applied.

### Figure 6, re-check 2 (Opus 5.5)

Figure 6 (objects): FIX

1. [error] Current: `Shopify POS shows any number of POS and online orders (1 to 0..*)` (unit-without-figures.md, section 6, the "as figure 6 draws them" paragraph). Problem: the figure draws the line label "shows POS and online orders", and that exact string is not in the text. The other three verbs ("connects", "manages", "is available on") do occur exactly as drawn. Fix: `Shopify POS shows POS and online orders, any number of them (1 to 0..*)`

2. [minor] Current: `{"from": "product", "to": "channel", "label": "is available on", "from_card": "0..*", "to_card": "0..*", "dir": "to"}` (declaration.json). Problem: at every width the product end of this line has a "0..*" stacked just under the "0..*" at the product end of the admin "manages" line. The two counts do not overlap, but a reader cannot easily tell which count belongs to which line. Both values are 0..*, so the reading does not change. This comes from how the renderer places the counts, not from the data. Fix: `{"from": "channel", "to": "product", "label": "offers", "from_card": "0..*", "to_card": "0..*"}`. This is optional. If used, the text's `the line labelled "is available on", which reads upwards, towards the channel, so it carries the triangle` must become `the line labelled "offers", which reads from top to bottom`, and the Fix has to be checked against the rendered frames again.

Confirmed:
- Box titles "Shopify POS", "Shopify admin", "sales channel", "order", "product" all occur in section 6's figure paragraph.
- POS box: "Orders screen", "filters: sale type, sale location, delivery type" and "-> search orders" occur verbatim.
- Admin box: "orders, products, customers", "analytics, marketing, discounts", "Sales channels and apps", "Settings" and "-> search, filtered by category" occur verbatim.
- Channel box: "Online Store", "Point of sale", "Shop" and "social, Google, marketplaces" occur verbatim.
- Order box: "order status: 3 values", "payment status: 9 values, plus Expiring and Unpaid", "fulfillment status: 7 values", "return status: 4 values" and "POS number #1-1005 if offline or unpaid" occur verbatim.
- Product box: "availability per channel" occurs verbatim.
- The status counts match the Lifecycle paragraph: order status 3 (Open, Archived, Canceled), payment status 9 plus Expiring and Unpaid, fulfillment status 7, return status 4.
- "#1-1005" matches the Labelling paragraph.
- All counts are drawn as the text states them: 1 to 1..* (connects); 1 to 0..* (shows; manages, twice); 0..* to 0..* (is available on).
- The caption says what the figure shows and names section 6. Its five sources are all in the unit's own text and its Sources list. It is dated 10 November 2026, credits Shopify, and says the admin and the POS app were not seen. "Counts are this unit's reading" agrees with the Unsure list.
- Kind: objects fits things and relationships. IA2's decision table gives the cross-surface interaction map as kind objects, in the journeys family.
- Notation: surface and object boxes have filled title bands, shared objects have lower-case titles, actions are written "-> verb", and the counts use UML multiplicities (IA2, section 1.5). No page-type tags are used, which is correct for this kind.
- Label direction: "connects" reads left to right on a level line. "shows POS and online orders" and both "manages" read top to bottom. "is available on" reads upwards and carries the triangle, as IA2, section 5.2 requires.
- Tones: the figure uses tone 2 only, and IA2 defines it as "anything outside Perqo". The unit names it ("Every box is tone 2.") and so does the caption. Tone 6 is not drawn.
- Matrix check: does not apply (this figure is objects).
- Frames: I checked phone 320, 360, 390 and 430, tablet and desktop, in dark and light (light on cream). Text sits inside its boxes, nothing is cut off, and the drawing is whole across the scroll frames.
  - On phones the figure scrolls sideways, and the "scroll sideways for the whole figure" hint shows. The faded right and left edges in the middle frames are the renderer's scroll fade, not clipping.
  - The final frame (for example 442 of 442 px at 320) shows the right column whole.
  - The tablet and desktop frames show the whole figure.
- Unit text: I found no further error in section 6. Its citations of IA2, section 1.5 (UML) and IA2, section 1.8 (Harel's parallel components) match IA2.
- Memory and context: I saw a memory snapshot and Project instructions in my context and used neither. I read only the files in /home/claude/w/rc/r2-fig6. I wrote crops of the frame sheets to /home/claude/w/rc/r2-fig6/crops/ and edited nothing.

*Maintainer's note.* FIX. Finding 1 holds: round 1's text change no longer gave the drawn label "shows POS and online orders" word for word; the text now does ("Shopify POS shows POS and online orders, any number of them (1 to 0..*)"), the declaration unchanged. Finding 2 is optional and rests on how the renderer places counts: recorded, not applied. Reopened for round 3.

### Figure 7, re-check 2 (Opus 5.5)

Figure 7 (matrix): FIX

1. [should-fix] Current (declaration.json, caption): `Rows tone 2: products outside Perqo; tone 6: a strain found in this reading.`
Problem: The caption and the legend both name Perqo, and the caption's decision ("which real product to read for which Perqo surface") is about Perqo, but the caption never says Perqo is fictional. IA2 §5.2, Captions, requires a caption to say "for Perqo ... that Perqo is fictional". Figure 8's caption says it; figure 7's does not.
Fix: `Rows tone 2: products outside Perqo; tone 6: a strain found in this reading. Perqo is fictional.`

2. [should-fix] Current (declaration.json, caption): `Every cell is drawn from sections 2 to 6 and the makers' documents cited there, read on 10 November 2026.`
Problem: The Shaping decision column is not drawn from the makers' documents. The unit's Unsure list says: "The counts on figure 6's lines, and each product's shaping decision, are this unit's reading of the makers' documents; no maker names a single shaping decision." As written, the caption credits a whole column of this unit's own reading to the makers.
Fix: `Every cell is drawn from sections 2 to 6 and the makers' documents cited there, read on 10 November 2026; each shaping decision is this unit's reading, as no maker names one.`

3. [minor] Current (declaration.json, caption): `"caption": "Comparison (structure family)`
Problem: "Comparison" is not one of IA2's ten artefacts. IA2 §1 lists the structure family as sitemap and navigation model. The unit names this artefact "The comparison table" (Deliverable B).
Fix: `"caption": "Comparison table (structure family)`

4. [minor, rests on the theme] In the light (e-ink, cream) frames, the tone 2 fill (peach) and the tone 6 fill (khaki) are close in value and hard to tell apart. The meaning does not rest on tone alone, because the Strain column header and the legend also carry it, so WCAG 1.4.1 is met. No change to the figure is needed. If the pair is changed, the change belongs in theme.css.

5. [minor, rests on the renderer] On the phone at 320 px, the pinned label column takes about 40% of the width even though the longest row label is seven characters ("Shopify"). That leaves room for about one and a half cells per frame. Every cell is still readable as the reader scrolls (4 frames at 320 px, 3 at 430 px). The legend scrolls with the table, so in some frames it is cut at the edge. Both come from the matrix renderer's layout, not from the declaration.

Confirmed:
- Every drawn string occurs in unit-without-figures.md exactly as drawn. They are all on line 174 ("The comparison, as figure 7 draws it. The rows are GOV.UK, Monzo, Stripe, Airbnb and Shopify, in tone 2; the columns are Level, Scheme, Structure, Search, Shaping decision and Strain. GOV.UK: IA5 website; topic; hierarchy and taxonomy; site search, filters; navigation from one taxonomy; three topic systems. Monzo: IA6 app; by account, then time; summary on Home; one search, Home and Help; Home set by the customer; moved features need a help page. Stripe: IA7 backoffice; by object, then product; database; global, typed filters; the API's objects are the Dashboard's; two meanings of product. Airbnb: IA8 lifecycle; place, then category; database; place box 2022, own words 2026; categories beside place; placement inferred from listing content. Shopify: IA8 surfaces; by object; one admin, many channels; admin search by category; one admin for every channel; four status sets. The Strain column is tone 6. The legend reads "tone 2: a product outside Perqo" and "tone 6: a strain found in this reading".").
- No number or date appears in the frames that the text does not state (IA5 to IA8, 2022, 2026).
- Each strain cell traces to a sentence in its section:
  - GOV.UK: "in 2021 there were three topic systems" (§2)
  - Monzo: "a page exists to tell customers where things are ... The makers wrote a page to find them again" (§3)
  - Stripe: "the two meanings of product" (§4, line 110)
  - Airbnb: "A listing's category is inferred from its text and photos" (§5)
  - Shopify: "an order carries four status sets" (§6)
- The other cells agree with Deliverable B's columns, in shorter form.
- Row labels (GOV.UK, Monzo, Stripe, Airbnb, Shopify) are the five products named in the unit's opening and in §7, and each is at most seven characters long.
- The caption says what the figure shows, names section 7 and Deliverable B, and cites only sections 2 to 6 and the documents cited there. A matrix comparing products is not a redrawn product structure, so it needs no product credit or observed date beyond the reading date it gives.
- Kind: five items against six dimensions is a matrix, which fits.
- Notation:
  - Rows are tone 2, which matches IA2's "anything outside Perqo".
  - Strain cells are tone 6, which matches IA2's "a fault found in a review". The unit names both tones on line 5 ("Tone 6 ... marks ... the strains this reading finds") and on line 174.
  - No type tags apply to a matrix.
  - Each tone has one meaning.
- Frames, at desktop, tablet and phones 320, 360, 390 and 430 px, dark and light: text sits inside its cells, nothing overlaps, no cell text is cut off, and the drawing is whole across the scroll frames.
- Unit text: I found no error in the passages read for this check (§7, Deliverables A and B, the Unsure list, Sources).
- I saw a memory snapshot and project instructions in my context. I used neither. I read only files in /home/claude/w/rc/r2-fig7 and one saved tool result under /root/.claude/. I wrote three crops in the folder (crop320_f1.png, crop320_f4.png, crop320_f2_light.png) and two more (crop430_last.png, crop390_open.png) in /home/claude/w/rc/r2-fig7.

*Maintainer's note.* FIX. Applied: findings 1, 2 and 3 (the caption says Perqo is fictional and that each shaping decision is this unit's reading; "Comparison table"). Findings 4 and 5 rest on the theme and the renderer: recorded, not applied. Reopened for round 3.

### Figure 8, re-check 2 (Opus 5.5)

Figure 8 (matrix): PASS

Findings

1. [minor] Current: `"D.2, CL- and EL-"` (declaration.json, once; the same words occur once in unit-without-figures.md line 178 as `D.2, CL- and EL-;`). Problem: the cell shows bare ID prefixes. The unit's own prose (line 172) gives the ranges: "the client's CL-1 to CL-6 and the employee's EL-1 to EL-6". The other three Perqo cells all give ranges (X-01 to X-13, DT-1 to DT-3, J-01 to J-14), so this cell is the odd one out. Fix: `"D.2, CL-1 to CL-6, EL-1 to EL-6"` in declaration.json. In line 178 of the unit, replace `D.2, CL- and EL-;` with `D.2, CL-1 to CL-6, EL-1 to EL-6;`. The cell will then wrap to two lines like its neighbours.

2. [minor] Current: `"sidebar, 26 is: types"` (declaration.json, once). Problem: the cell matches the text, but it is hard to read. Section 4 (line 100) says "`is:` with one of 26 object types". Fix: `"sidebar, 26 is: object types"` in declaration.json. In line 178 of the unit, replace `sidebar, 26 is: types;` with `sidebar, 26 is: object types;`.

3. [minor, renderer layout only] There is no Current text, because this is not a content fault. On phones the legend sits inside the sideways-scrolling figure, so it scrolls with it. In the opening frame at 320 px (both themes), the "tone 2" entry is off-screen to the right and the tone 6 text is cut at "none in t". At 430 px, tone 2 is cut at "a produ". Both are whole once scrolled (320 frames 2 and 3). Later 320 frames show stray legend fragments at the left edge ("ıap (Perqo is fictional)", "qo"), also from the scroll. This comes from how the renderer lays out a matrix legend, not from the declaration. Fix: none in this figure. If it matters, it is a renderer question: the legend could sit outside the scroll area.

Confirmed
- Columns `Surface layer`, `Lifecycle layer`, `Decision layer`, `Connections`: unit line 178, "The columns are Surface layer, Lifecycle layer, Decision layer and Connections."
- Perqo row `Perqo map (IA8)`, `D.1, X-01 to X-13`, `D.2, CL- and EL-`, `D.3, DT-1 to DT-3`, `D.4, J-01 to J-14`: line 178, "Perqo map (IA8): D.1, X-01 to X-13; D.2, CL- and EL-; D.3, DT-1 to DT-3; D.4, J-01 to J-14." Also backed by line 172 (the IA8 layers and ID ranges).
- GOV.UK `16 topics, taxonomy principles`, `step by step journeys`, none, none: line 178, "GOV.UK: 16 topics, taxonomy principles; step by step journeys; none in the pages read; none in the pages read." Backed by lines 54 and 172.
- Monzo `Home's areas`, then none in the other three: line 178, "Monzo: Home's areas; none in the pages read, in the other three columns." Backed by line 172.
- Stripe `sidebar, 26 is: types`, `PaymentIntent statuses`, none, `status mapping table`: line 178, "Stripe: sidebar, 26 is: types; PaymentIntent statuses; none in the pages read; status mapping table." Backed by line 100 (26 object types) and line 172 (status mapping as the join).
- Airbnb `four tabs, 55 categories (2022)`, `four status groups`, `24 hours, then Expired`, none: line 178, "Airbnb: four tabs, 55 categories (2022); four status groups; 24 hours, then Expired; none in the pages read." Backed by lines 122, 130 and 172.
- Shopify `admin, channels, POS, online orders on POS`, `four status sets`, `products available by default`, none: line 178, "Shopify: admin, channels, POS, online orders on POS; four status sets; products available by default; none in the pages read." Backed by line 172 (one cross-surface default, one crossing) and line 232 (the channel default).
- Tones: line 178, "Each "none in the pages read" is tone 6; the other cells of the five take their row's tone 2". The declaration matches this cell by cell.
- Legend: line 178, "tone 5: the Perqo map (Perqo is fictional)", "tone 2: a product outside Perqo" and "tone 6: a gap found in this reading: none in the pages read". All three match the declaration exactly.
- Caption: it says what the figure shows and names section 7. It names its sources as IA8, Deliverable, D.1 to D.4 (the unit cites IA8, Deliverable, D.1 to D.5 in its table, line 26) and sections 2 to 6, read on 10 November 2026. It cites nothing the unit does not cite. It redraws no product structure, so no product credit is needed (figure 7 is the same).
- Kind: matrix fits, with items (the Perqo map and five products) by dimensions (three layers plus connections), as IA2 section 5.2 defines it: "a row is an item, a column a dimension, and a marked cell the value where they meet".
- Notation: tone 2 matches IA2 ("the merchant side and anything outside Perqo"). Tone 5 for the Perqo map matches "shared... the Perqo system". Tone 6 matches "a fault found in a review", which the unit applies to a gap in a published map (line 14). Each tone has one meaning in the figure. All three tones, tone 6 included, are named in the unit's text (lines 14 and 178). A matrix has no type tags.
- Row labels: the longest is "Perqo map (IA8)" at 15 characters. At 320 px the pinned label column takes about 45% of the width and leaves a full cell visible. Each label is traced to line 178.
- Frames: I checked desktop and tablet in both themes and phones at 320 and 430 px in both themes (opening frames and frame sheets). Text sits inside its cells, nothing overlaps, and every column is reached across the scroll frames. In light (cream), tones 2 and 6 are close but still told apart, and the words "none in the pages read" carry the meaning in any case.
- Unit text: I found no error in the passages on this figure. Line 172 calls the layers "actor and lifecycle layer" and "decision-tree layer", while the columns say "Lifecycle layer" and "Decision layer". The shorter names are stated at line 178, so this is not an error.
- Context: a memory snapshot and project instructions were present in my context. I used none of them, and I used only the files in /home/claude/w/rc/r2-fig8 (crops written to /home/claude/w/rc/r2-fig8/crops).

*Maintainer's note.* PASS: the loop ends. Minors 1 and 2 would change the declaration once more and every word they touch is traced ("CL- and EL-" and "26 is: types" stand in the text as drawn): recorded, not applied. Minor 3 rests on the renderer: recorded.

### Brand + AI A4, figure 2 (states), re-check after the renderer change (Opus 5.5)

A4 figure 2 (states): PASS

No word is broken inside any more. The former "harassme / nt" split is gone at every width and theme, and "harassment" sits whole on its own line under "change or". The two findings below are wording condensations. Neither is a factual error, and neither has to be fixed for the figure to pass.

Findings

1. [minor] Current: `"label": "platform change or harassment"` (declaration.json). Problem: the text says "a platform change or a wave of harassment can push them back" (unit-without-figures.md line 83). The label shortens this, so it is not drawn word for word from the text, though the meaning is the same and the caption gives the full wording. Fix (optional): `"label": "platform change or a wave of harassment"`. The renderer now widens the gap to fit the longest word, so the longer label will not break.

2. [minor] Current: `"note": "metrics as validation"` (declaration.json). Problem: the text says "metrics as the main source of validation" (line 83), and the note drops "the main source of". Fix (optional): `"note": "metrics as main source of validation"`.

Confirmed
- "Large audience": line 83, "After a creator reaches a large audience, "audience entanglement" sets in".
- "usually begins", on the arrow from Large audience to Dysfunctional: line 83, "It usually begins as *dysfunctional entanglement*".
- "Dysfunctional entanglement": line 83, "*dysfunctional entanglement*: oppressive dependence on audience reactions, metrics as the main source of validation".
- "Functional entanglement" and "balanced dependence": line 83, "Some creators reach *functional entanglement*, a balanced dependence in which they draw meaning from the audience".
- "some creators reach", on the arrow from Dysfunctional to Functional: line 83, "Some creators reach *functional entanglement*".
- The arrow back from Functional to Dysfunctional: line 83, "Creators cycle between the two; a platform change or a wave of harassment can push them back."
- The figure draws no numbers. The start dot is the declared start state, audience.
- Caption: it says what the figure shows (the cycle: begins dysfunctional, some reach functional, pushed back). It names §3, and its source (Pillemer, Harrison, Murphy and Park, ASQ 71(1), online 18 Dec 2025, as summarised in the abstract and by PsyPost, 20 Feb 2026) matches line 80 and Sources line 250.
- Kind: states fits. The data is a lifecycle with an entry state, a forward step and a return step.
- Desktop and tablet, dark and light: one frame holds the whole figure. Text sits inside its boxes, labels are clear of the arrows, both arrows join their states, nothing overlaps or is cut off. The light frames read correctly on cream.
- Phones 320, 360, 390 and 430, dark and light: the figure scrolls sideways, with a "scroll sideways for the whole figure" note. Across the stacked frames every state, label and arrow appears whole at least once, and no word is broken inside. The fading or clipped box edges in the middle frames come from the horizontal-scroll viewport and its edge fade. That is how the renderer lays the figure out, not a defect in the figure.
- No error seen in the unit's own text in §3 (lines 74–105).
- A memory snapshot and Project instructions were in my context. I used neither, and I read nothing outside /home/claude/w/rc/r2-a4.

*Maintainer's note.* PASS: the loop ends; the word is whole at every width. Both minors would change A4's declaration, which this row does not otherwise touch, and every word is traced to A4's text and caption: recorded, not applied. A4's text, figures' declarations, written date and word count are unchanged.

**Round 3.** Figures 1, 6 and 7, fresh Opus 5.5 agents, the same inputs from a new build's frames. Transcript checks: each claude-opus-5-5; no web or forbidden tool; every path inside its folder.

### Figure 1, re-check 3 (Opus 5.5)

Figure 1 (sitemap): FIX

1. [should-fix] Current: `{"label": "Topic pages", "type": "stack", "tone": 6,` (declaration.json, once), together with `Topic pages (`stack`, tone 6)` (unit-without-figures.md, line 66, once).
Problem: the box is the topic taxonomy, but the unit's own text uses "topic pages" for the 16 mainstream browse topics drawn under Services and information. Line 64 reads "the 2025 change from a grid to a list on the 16 topic pages" and "the topic taxonomy pages don't form part of our current phase of work" (Richardson 2025). A reader who reads the figure next to section 2 will take this tone-6 box for the 16 topics. That clashes with IA3's D2 (one thing, one label), which is the fault section 2 itself raises against GOV.UK. The maker's own words for the taxonomy's pages occur in the text: "the topic taxonomy pages" (line 64).
Fix: in declaration.json `{"label": "Topic taxonomy pages", "type": "stack", "tone": 6,`; in unit-without-figures.md line 66 `Topic taxonomy pages (`stack`, tone 6)`.

Confirmed:
- `GOV.UK` (home): line 66, "GOV.UK (`home`)". Line 50 gives the home page at gov.uk.
- Root note "Popular on GOV.UK; Featured": line 66, "with "Popular on GOV.UK; Featured" in its note, two headings of the home page as read on 10 November 2026". These two headings are stated only in this figure-description paragraph, not in the section's prose. The figure matches that paragraph exactly.
- "Services and information", section, "16 topics": line 50, "Under "Services and information" it lists 16 topics".
- "Benefits", section: line 50, "the Benefits page is a record of type `mainstream_browse_page` whose eight children are curated".
- "Benefits and financial support pages", stack, tone 6, "7 of 8 labels open with the same four words": line 52, "Seven of the eight children of Benefits begin with the same four words, "Benefits and financial support"". Line 66 gives the same label and note.
- "Manage an existing benefit, payment or claim", section: line 52, "the eighth is "Manage an existing benefit, payment or claim"".
- "15 other topics", stack, "Births, deaths, marriages and care to Working, jobs and pensions": line 50, "from "Benefits" and "Births, deaths, marriages and care" to "Visas and immigration" and "Working, jobs and pensions"". Line 66 gives the same.
- "Government activity", section, "8 links": line 50 lists eight links, from "Departments" to "Get involved". Line 66 has "Government activity (`section`, 8 links)".
- "Departments" and "News", both index: line 50, ""Departments", "News"".
- "6 more links", stack, "Guidance and regulation to Get involved": line 50 lists the six links in that order. Line 66 gives the same.
- "Search GOV.UK", index, "more than 4 million searches a month": line 54, "the header's "Menu" and "Search GOV.UK""; line 56, "more than 4 million times a month" (Fraser and Crusellas 2024). Line 66 gives the same.
- Topic pages note, "the taxonomy, one of three topic systems in 2021; reached from content pages' sidebar and breadcrumbs": line 64, "in 2021 there were three topic systems"; line 50, "reached from content pages, through sidebar links and breadcrumbs". Line 66 gives it verbatim.
- "Step by step pages", stack, "end to end journeys": line 54, "presents an end to end journey in logical steps". Line 66 gives the same.
- "Content pages", stack, "more than half a million pages (2021)": line 54, "more than half a million pages ... in 2021" (Dub 2021). Line 66 gives the same.
- Tones: line 66 says "Every other box is tone 2", which matches the declaration (only the two stacks named above are tone 6).
- Caption: it names the artefact (sitemap, structure family), what it shows, the decision it supports and section 2. Every source it names is cited in section 2: gov.uk, gov.uk/browse, the content API record, Dub 2021, the taxonomy principles 2019, Fraser and Crusellas 2024, and the Design System's step by step page. It cites nothing the unit does not. It gives the date observed (10 November 2026) and credits GOV.UK, Government Digital Service.
- Kind: a sitemap fits a site hierarchy.
- Notation: every type tag (home, section, index, stack) is on IA2's fixed list, and each stack's note says what repeats. Tone 2 means outside Perqo and tone 6 means a fault found in a review, as IA2 sets them. Line 14 names both tones as this unit uses them, tone 6 included ("the strains this reading finds"). Tones are set explicitly rather than by position.
- Matrix check (item 5): not applicable; this is a sitemap.
- Frames: in every width and theme, text sits inside its boxes, nothing overlaps, and the drawing is whole across the frames. Tone 6 (olive) is distinct from tone 2 (rust) on the cream light theme and in dark.
- Frames, renderer layout only: on desktop and tablet the root's six children wrap into two rows by width. On the desktop opening frame the sticky section bar clips the top, so the root box is hidden; the frame sheet shows it whole.
- Frames, renderer layout only: at 320 px and 360 px the stacked phone layout scrolls sideways over two frames (70 px and 30 px). The right edge fades in frame 1, and frame 2 shows the remaining text. At 390 px, 430 px, tablet and desktop the figure fits in one frame.
- Unit text (item 7): I found no error in the text bearing on figure 1. Section 2's facts agree with the figure-description paragraph and with Deliverables A and B.
- Context: a memory snapshot and the Project's instructions were in my context; I used neither, and read nothing outside my folder.

*Maintainer's note.* FIX. The finding holds: section 2 uses "topic pages" for the 16 browse topics and quotes the maker's "the topic taxonomy pages" for the taxonomy. Applied in the declaration and the text ("Topic taxonomy pages"). Reopened for round 4.

### Figure 6, re-check 3 (Opus 5.5)

Figure 6 (objects): PASS

Findings

1. [minor] The two shared objects do not carry IA2's "Surface: Label" lines.
Current (declaration.json): `{"id": "order", "title": "order", "tone": 2, "attrs": ["order status: 3 values",`
Problem: IA2 section 5.2 (Labels) says that on a shared object the title is the data-model name in lower case, "and each surface's name is a line 'Surface: Label'". The figure gets the lower-case titles right ("order", "product") but gives no surface names, even though the caption says the figure supports the decision on "how each surface shows them". The unit's text does give one surface name: POS lists orders on its "Orders screen" (section 6, Objects). For now that name sits only as an attribute of the Shopify POS box. This is not an error, because the text does not set a per-surface name for every surface.
Fix (optional; change both places together): in declaration.json, `{"id": "order", "title": "order", "tone": 2, "attrs": ["POS: Orders screen", "order status: 3 values",`. In unit-without-figures.md line 158, replace `The order lists "order status: 3 values",` with `The order lists "POS: Orders screen", "order status: 3 values",`.

2. [minor] A layout point that comes from the renderer. Two "0..*" counts sit next to each other above the product box, one for "manages" and one for "is available on". At every width and in both themes they stack close together, so it takes a second look to see which count belongs to which line. Neither overlaps the other or a line. I am reporting it as renderer placement, not as a declaration error.
Current (declaration.json): `{"from": "admin", "to": "product", "label": "manages", "from_card": "1", "to_card": "0..*"}`
Fix: none needed in the data. If the renderer allows, place the admin–product end count further along its diagonal.

3. [minor] Error in the unit's text, not in the figure. The last line of the Unsure list is not an unsure item. It looks like leftover text.
Current (unit-without-figures.md, line 319): `- Object: the Stripe PaymentIntent and its Dashboard status mapping, section 4`
Problem: it states nothing uncertain. It reads like a stray note from an object list, and section 4 already covers the mapping.
Fix: delete the line (replace with ``).

Confirmed

- "Shopify POS", "Orders screen", "filters: sale type, sale location, delivery type" and "-> search orders" all occur in line 158: `Shopify POS lists the Orders screen and "filters: sale type, sale location, delivery type", with the action "-> search orders".`
- "Shopify admin", "orders, products, customers", "analytics, marketing, discounts", "Sales channels and apps", "Settings" and "-> search, filtered by category" all occur in line 158: `Shopify admin lists "orders, products, customers", "analytics, marketing, discounts", "Sales channels and apps" and Settings, with the action "-> search, filtered by category".`
- "sales channel", "Online Store", "Point of sale", "Shop" and "social, Google, marketplaces" occur in line 158: `The sales channel lists Online Store, Point of sale, Shop and "social, Google, marketplaces".`
- The five attribute lines of the order occur in line 158: `The order lists "order status: 3 values", "payment status: 9 values, plus Expiring and Unpaid", "fulfillment status: 7 values", "return status: 4 values" and "POS number #1-1005 if offline or unpaid".` The counts match section 6's lists: 3 order statuses (Open, Archived, Canceled); 9 payment statuses plus Expiring and Unpaid; 7 fulfillment statuses; 4 return statuses. #1-1005 matches section 6, Labelling.
- "availability per channel" occurs in line 158: `The product lists "availability per channel".`
- "connects", 1 to 1..*: `The admin connects one or more sales channels (1 to 1..*)`.
- "shows POS and online orders", 1 to 0..*: `Shopify POS shows POS and online orders, any number of them (1 to 0..*)`.
- "manages", 1 to 0..*, twice: `the admin manages any number of orders and any number of products (1 to 0..* each)`.
- "is available on", 0..* to 0..*, with the triangle: `any number of products are available on any number of sales channels (0..* to 0..*), the line labelled "is available on", which reads upwards, towards the channel, so it carries the triangle.` In the frames the triangle points at sales channel.
- Reading direction: "connects" is level and reads left to right. "shows POS and online orders" and both "manages" lines read top to bottom. Only "is available on" reads against the rule, and it carries the triangle, as IA2 section 5.2 requires.
- Caption says what the figure shows, names section 6, and lists only the five Help Center pages that section 6 cites. It credits Shopify, gives the date observed (10 November 2026), says the admin and POS app were not seen, says the counts are the unit's reading in UML notation (the text cites IA2, section 1.5), and explains tone 2.
- Kind: objects fits surfaces plus shared objects with counted relationships. It is the kind IA2 section 5.3 uses for its own cross-surface interaction map, and the artefact IA2 section 1.10 defines.
- Notation: the boxes have title bands, attributes, and actions after a rule line. Actions use the "-> verb" form, counts use UML multiplicity, shared-object titles are lower case, and no line is dashed.
- Tones: every box is tone 2. Line 158 says "Every box is tone 2", and line 14 defines tone 2 as "the merchant side and anything outside Perqo". This unit keeps tone 5 for the Perqo map only, so using tone 2 for Shopify's shared objects is consistent. No tone 6 is drawn.
- Matrix check (step 5): not applicable.
- Frames: at phone 320, 360, 390 and 430, tablet and desktop, in dark and in light on cream, text sits inside its boxes and nothing overlaps. Across the scrolled frames the drawing is whole at every width (320: 5 frames, 360: 4, 430: 3), and tablet and desktop show all of it in one view. Renderer-only effects: on phones the figure scrolls sideways in fixed steps with edge fades, and in the phone opening frame the sticky section bar covers the top of the figure.
- Sources: I used only the files in /home/claude/w/rc/r3-fig6 and crops I made in /home/claude/w/rc/r3-fig6/crops. My context contained a memory snapshot and project instructions; I used neither.

*Maintainer's note.* PASS: the loop ends. Finding 1 (an optional "POS: Orders screen" line) would change the declaration once more and its words are traced: recorded, not applied. Finding 2 rests on the renderer's placement of counts: recorded. Finding 3 (delete the Object line) not applied: the line closes the unsure list by method (P96).

### Figure 7, re-check 3 (Opus 5.5)

Figure 7 (matrix): PASS

Findings
1. [minor] Unit text, not the figure.
   Current: `- Object: the Stripe PaymentIntent and its Dashboard status mapping, section 4` (unit-without-figures.md, line 319, the last line of the Unsure list; it occurs once)
   Problem: It is a stray line. It records no uncertainty, matches no other entry in the Unsure list, and reads like a leftover note or field from drafting.
   Fix: `` (delete the line)

2. [minor] A rendering note that comes from the theme, not the declaration. In both themes tone 6 (Strain column, tone 6 legend swatch) is close to tone 2. In light it is grey-beige against tan; in dark it is olive-brown against brown. The meaning is still carried by words (the column header "Strain" and the legend), so WCAG 1.4.1 is met and the declaration needs no change.
   Current: `{"mark": "tone 6", "means": "a strain found in this reading", "tone": 6}` (declaration.json)
   Problem: Tone 6 is hard to tell from tone 2 at a glance. This rests on design/theme.css, not on this figure.
   Fix: `{"mark": "tone 6", "means": "a strain found in this reading", "tone": 6}` (no change to the figure; if the contrast is wanted, raise the tone 2/tone 6 contrast in theme.css as a separate row)

Confirmed
- Item 1, labels: every column header, row label, cell and legend entry occurs in unit-without-figures.md line 174, exactly as drawn. The line includes "the columns are Level, Scheme, Structure, Search, Shaping decision and Strain". It gives each row in full; for example, "GOV.UK: IA5 website; topic; hierarchy and taxonomy; site search, filters; navigation from one taxonomy; three topic systems." and "Airbnb: IA8 lifecycle; place, then category; database; place box 2022, own words 2026; categories beside place; placement inferred from listing content.". It also says "The legend reads "tone 2: a product outside Perqo" and "tone 6: a strain found in this reading"". The figure draws nothing the text does not state. The frames match the declaration.
- Item 1, faithfulness: the cells match sections 2 to 6:
  - Navigation from one taxonomy: §2, line 62.
  - Three topic systems: §2, line 64.
  - Summary on Home and moved features need a help page: §3, lines 72 and 86.
  - Two meanings of product: §4, line 96.
  - Place box 2022, own words 2026: §5, line 126.
  - Placement inferred from listing content: §5, lines 128 and 134.
  - Four status sets: §6, line 156.
  - "Topic" for GOV.UK simplifies Deliverable B's "topic for services; by department and document type…". This is consistent with §7 line 166.
- Item 2, caption: it names the artefact and family ("Comparison table (structure family)"), what it shows, the decision ("which real product to read for which Perqo surface", the same as Deliverable B's decision), the sections (section 7; Deliverable B; cells from sections 2 to 6), the sources ("the makers' documents cited there") and the date read (10 November 2026). It flags the shaping decisions as the unit's reading, which matches the Unsure list line 318, and it ends "Perqo is fictional". It cites only sections and sources the unit cites. It redraws no single product's structure, so no product credit is due.
- Item 3, kind: a matrix fits five items across six dimensions.
- Item 4, notation: matrix rows are items, columns are dimensions and cells are values (IA2 §5.2). No type tags apply. Tone 2 is used for products outside Perqo and tone 6 for strains found in a review, one meaning each and consistent with IA2's notation sheet. The unit names both tones on line 14 ("Tone 2, "the merchant side and anything outside Perqo"…"; "Tone 6… marks… the strains this reading finds") and again on line 174.
- Item 5, matrix row labels: the labels are GOV.UK, Monzo, Stripe, Airbnb and Shopify, all short. At 320 px the pinned label column leaves room for about two cell columns per frame. Each label is traced to line 174, "The rows are GOV.UK, Monzo, Stripe, Airbnb and Shopify, in tone 2".
- Item 6, frames: I checked phone 320 (all 4 frames, light), phone 390 (dark), phone 430 opening (dark), tablet (dark) and desktop (light). Text sits inside its cells, nothing overlaps, and no cell text is cut off. The full table is seen across the scroll frames at every width I checked. On phones the legend's tone 6 entry and the right-hand columns are clipped in the opening frame because the figure scrolls sideways ("scroll sideways for the whole figure"); this is the renderer's layout, and the later frames show them whole. The fade at the scroll edge is also the renderer's.
- Item 7, unit text: the only text error found is finding 1.
- Context: my context held a memory snapshot and Project instructions. I used neither. I read only files in my folder and wrote crops only to /home/claude/w/rc/r3-fig7/crops/.

*Maintainer's note.* PASS: the loop ends. Finding 1 (delete the Object line) not applied, as for figure 6. Finding 2 rests on the theme's tones 2 and 6 and asks no change to the figure: recorded, not applied.
