# Perqo: the register of invented facts

Perqo is the fictional flexible-benefits platform every unit of the IA course builds on. Each unit invents the facts it needs, labels each "(Perqo, fictional)" on first use, and keeps them consistent with the facts filed before it. This register lists every fact a filed unit has set, with the unit and section that set it, so a later unit can check consistency against one page instead of grepping the vault. It is appended at every filing (`skills/file-unit` §6) and goes into every writer's packet (`skills/write-unit` §2). Started 3 Nov 2026 (row S-1) from IA1 and IA2.

A fact here is a course convention, never evidence for a claim about the world. A later unit may extend a fact (add categories, states, pages) and must say so; it may not contradict one without the earlier unit being fixed in the same chat.

## The product (IA1 §2, §5)

- A flexible-benefits platform in the technology space. Client companies give each employee a benefits budget to spend across categories.
- Three surfaces: **perqo.com** (the sales and product website), **Perqo Admin** (the backoffice where a client's HR and finance managers configure budgets, policies, approvals and reports), **the Perqo app** (the employee app for seeing balances and spending benefits). A merchant side exists where a unit needs it; IA3 set its first fact (card offers, below).
- Money moves two ways: a card payment, or a claim (a receipt the employee asks to be reimbursed for). Claims are their own object, separate from card purchases (IA1 §2.1).

## Surfaces and their top-level areas (IA1, deliverable: the surfaces map)

| Surface | Built for | Top-level areas | Kind of IA |
|---|---|---|---|
| perqo.com | Buyers at prospective clients; HR, finance and employees in passing | Product, Pricing, Customers, Help centre, Sign in (IA2 §5.3 adds Book a demo to the global routes) | Shallow website hierarchy |
| Perqo Admin | HR managers and finance managers at client companies | Employees, Budgets, Policies, Approvals, Reports, Settings | Object-heavy backoffice; permissions decide what each role sees |
| Perqo app | Employees at client companies | Home, Benefits, Claims, Card, Account | Small, task-driven; one screen at a time |

- What crosses between surfaces (IA1): perqo.com → Admin: a signed contract, HR and finance sign in. perqo.com → app: download link, help articles for employees. Admin → app: budgets (as balances), policies (as open categories and approval rules), invitations, approval decisions.

## Benefit categories (IA1 §2.1, deliverable; IA2 §5.3 vocabulary)

- Four: **Health, Learning, Mobility, Meals**. Switched on per employee group by HR in Policies; shown to the employee under Benefits.
- Narrower terms (IA2 §5.3, controlled vocabulary): Health → Fitness, Therapy; Learning → Courses, Books; Mobility → Public transport, Bike; Meals → Restaurants, Groceries.
- Variant terms people use (IA2 §5.3): Health: wellbeing; Learning: education, training; Mobility: transport, commuting; Meals: food.

## The shared vocabulary: one thing, three names (IA1 deliverable; IA2 §5.3)

| Data model | Perqo Admin | Perqo app | perqo.com | Variants (IA2) |
|---|---|---|---|---|
| allocation (per employee, category, period) | Budget | Balance | Benefits budget | allowance, credit |
| transaction, type card payment | Card payment | Purchase | Card payments | |
| transaction, type claim | Claim | Claim | Claims | refund, reimbursement, expense |
| policy | Policy | not shown; its effect shows as open categories and approval rules | Policies | |
| employee group | Employee group | not shown | Teams and groups | |

## The data model (IA1 §2.4)

- Engineering stores every movement of money in one table of transactions with a type field, card payment or claim, and each employee's money as an allocation per benefit category per period.

## Objects in Perqo Admin (IA1 §2.2, §5; IA2 §5.3 object map at F2)

- Core objects: employee group, policy, employee, budget, allocation, claim. An employee group follows one policy and the policy belongs to that group; the group contains its employees; finance sets budgets per employee group and period; each employee holds one allocation per open category and period; an employee submits claims; each claim is checked against the group's policy.
- Approvals is a top-level area holding every claim awaiting a decision; each claim is also reachable from the record of the employee who made it; pending claims are grouped by policy (IA1 §2.2).

## The claim lifecycle and rules (IA1 §1.1, §5; IA2 §5.3)

- States: **Submitted, Approved, Rejected, Paid**. Paid and Rejected are end states. Approved → Paid when Perqo pays out.
- Rule on submission (IA2 §5.3 decision tree): amount within the employee's balance? no → Rejected, over balance. yes → at or under the policy's **auto-approve limit**? yes → Approved automatically; no → waits in Approvals, where HR approves (→ Approved) or not (→ Rejected by HR).
- Blueprint (IA2 §5.3, F1): for a claim over the auto-approve limit, the employee pays and keeps the receipt, submits in the app's New claim form; HR approves in Approvals backstage; the Perqo system checks policy and balance and sends the notifications.

## The Perqo app: screens and flows (IA1; IA2 §5.3 wireflow at F2)

- Claims screen lists claims by status (Submitted, Paid). New claim asks for a category (only the categories open to the employee's group appear), an amount and a receipt → Continue → Check and submit (category, amount, balance after the claim) → Edit returns to New claim, Submit ends the flow.
- Contextual route from the Claims screen to the claim articles in the Help centre (IA1 §2.3).
- Local routes: the four categories inside Benefits (IA2 §5.3).

## perqo.com: pages and the Help centre (IA1 §2.3; IA2 §5.3 sitemap and inventory)

- Home → Product, Pricing, Customers, Help centre, Book a demo, Sign in. Product has one page each for Perqo Admin, Perqo app and Perqo card. Customers is an index over Customer stories, one page per client.
- The Help centre is used by both HR managers and employees; it splits by audience, **For HR and finance teams** (Budgets, Policies) and **For employees** (Claims, Balance), then by task. Search exists inside the Help centre only.
- Inventory slice (IA2 §5.3; IDs H-x.y.z, URLs under perqo.com/help/employees/… and perqo.com/help/hr-finance/…): "How to claim back a receipt", "Why was my claim rejected?" (says "refund"; the app says Claim), "Your balance explained", "Setting a budget for an employee group", "Approval rules" (a PDF to be replaced by an article).

## Navigation model (IA2 §5.3)

- Global, local, contextual and supplemental routes per surface as in the table above; Admin's local routes are the policies inside Policies, one per employee group; Admin's contextual route runs from an employee's record to the claims they made; Admin and the app have no supplemental route.

## Set by IA3 (3 Nov 2026)

- **The claim rule reads one category's balance** (§2.3, extending IA2 §5.3's rule): "within the employee's balance" is the balance of the category chosen on New claim. An employee with all four categories open holds four allocations.
- **The as-is Perqo app** (§2.3, §3.3, Deliverable): the app as it stands before IA6, the structure IA6 replaces. It keeps every fact above and adds, as faults for IA3's checklist:
  - Home: one Balance total (the sum of the four category balances) with a "Learn more" link under it to H-2.2.1; a Recent activity list mixing purchases and claims that shows a submitted claim as "Pending"; a "Discover" banner opening the offers list, with a second "Learn more" under it; a "+" icon with no text that opens New claim.
  - Benefits: Health, Learning, Mobility, Meals, then a fifth item, "Perks" (the offers list again). Each category screen shows its balance and a "What's covered" list of its narrower terms, with no examples.
  - Claims: the Submitted and Paid groups; approved claims stay in Submitted until paid; rejected claims are not listed and appear only in Notifications (IA2 §5.3's state diagram assumed the app shows Approved; the as-is does not, and IA3's fix for B2 restores it). A link "Help with claims" opens the claim articles.
  - Card: Card details, Purchases, Freeze card. Account: Profile, Notifications, Documents (holding the "Approval rules" PDF, H-1.2.4) and Help (the Help centre's home page, where both audiences start).
- **The first merchant fact** (Deliverable): merchants that accept the Perqo card can publish offers (discounts for Perqo cardholders), which the app lists; reached from Home's "Discover" and again as "Perks" in Benefits, both placings asked for by the partnerships team.
- **Each client's policy lists what is covered under each category** (§3.3). The example client's policy: gym membership → Health, Fitness; train pass → Mobility, Public transport; coding course → Learning, Courses; cookery course → Learning, Courses; yoga class → Health, Fitness; bike helmet → Mobility, Bike. Assumed second places an employee looks (untested): cookery course → Meals; yoga class → Learning; bike helmet → Health.
- **The Help centre's search log** (§5.2, Deliverable E2): the For employees log for one quarter, top five queries in rank order: "refund" (returns H-2.1.2), "allowance" (zero results), "rejected claim" (H-2.1.2), "gym" (zero results), "approval" (H-1.2.4); no counts. The Help centre logs searches and nobody reads the logs.
- **Frequency of use, assumed** (§6.2): Perqo Admin is used daily by the same HR and finance managers; the employee app is opened a few times a month.
- **IA3's proposals for IA6, decided** (Deliverable; decided by IA6, Deliverable B, B.1, 3 Nov 2026): all eight taken and now facts (see "Set by IA6"): the offers list renamed "Card offers", one placing; the four category balances on Home; Claims grouped by all four states; the "+" labelled "New claim"; "Your balance explained" for the balance link; Help opens For employees; the rule "Claims over the limit need HR approval" on New claim, the limit read from the group's policy; Documents removed. IA6 keeps the labels IA3's checklist passes (its "What IA6 keeps", which names Recent activity since 3 Nov 2026).

## Set by IA4 (3 Nov 2026)

- **Orderings** (§1.1): Admin's Employees list is ordered alphabetically by name and filtered by employee group; the app's Purchases and Claims lists are ordered newest first.
- **Cross-listing** (§1.2): Help centre articles that both audiences need are listed under both audiences. Card offers are classified by the benefit categories, through the catalogue.
- **Vocabulary sources** (§3.3): Perqo has no user tagging; the Help centre search log and support's tickets feed variant terms into the taxonomy.
- **Addresses** (§5): catalogue pages and filters address values by stable identifier; a renamed or moved Help centre page keeps a redirect from its old address.
- **The object map** (Deliverable A; F2, covering every surface; IA7 extends it for Admin and renames nothing): sixteen objects, O-01 to O-16, among them the new client (Admin: Company, in Settings; perqo.com: Customers; name, contract start date), admin user (Admin: Admins, in Settings; name, work email, role HR manager or finance manager; on perqo.com signs in through Sign in), card (app: Card; perqo.com: Perqo card; last four digits; status Active or Frozen), notification (app: Notifications, in Account; message, date, the claim it is about), merchant (name; one narrower term assigned by Perqo; accepts the card; its name shows on a purchase), offer (title, discount, valid until; one catalogue item, one merchant; app: Card offers), catalogue item (Admin: Covered items, in Policies; app: What's covered; ID, name, the four facet values, variant terms), customer story (title, URL, client) and demo request (name, work email, company, number of employees; sales follows it up; not in Admin). New attributes on earlier objects: the policy's covered items; the allocation's spent and remaining; the claim's date submitted; the card payment's merchant and category; the help article's audience.
- **Relationships** (Deliverable A.2): R-01 to R-20 with counts (R-03, R-04, R-05, R-08, R-09 and R-10 are IA2's). New ones include: an employee holds 0..1 card; a card payment spends from one allocation; a merchant takes card payments; a claim triggers notifications; a merchant publishes offers; an offer is for one catalogue item; a policy covers catalogue items (0..*, 0..*); a help article explains policies, allocations, claims, cards and catalogue items; a customer story is about a client; a demo request leads to a client.
- **Rules** (Deliverable A): finance sets allocations for a whole group at once, by category and period; a card payment at a merchant spends from the allocation of that merchant's category; the employee can freeze and unfreeze the card; Perqo's content team owns the catalogue.
- **Calls to action** (Deliverable A.3): one table of 22 rows, each with who triggers it and where it lives (for example freeze and unfreeze card, add covered items, create group, edit company details, add admin user, follow up a demo request).
- **The benefits catalogue taxonomy** (Deliverable B): four facets, F-CAT (benefit category, two levels, the four categories and eight narrower terms with identifiers CAT-HEA, CAT-HEA-FIT and the rest), F-PAY (usual way to pay), F-TYP (purchase type) and F-CHN (channel), with value identifiers PAY-, TYP-, CHN-; twelve catalogue items, BI-001 to BI-012 (IA3's six and six new: therapy session, book, bike repair, restaurant meal, groceries, swimming pool entry); new variant terms gym, sport, counselling, e-books, train, bus, cycling, eating out, supermarket, and "class" excluded from Courses; rules R1 to R10 for adding a value, among them R5 (a new value needs at least two items: the content team's threshold) and R7 (F-CAT keeps two levels).
- **Benefit category stays a taxonomy term, not an object** (§4.3).

## Set by IA5 (3 Nov 2026)

Every fact below is a course convention (Perqo, fictional); IA5 keeps every registered fact and renames no IA1 to IA4 label. Two IA2 §5.3 inventory rows are extended, not changed: "Your balance explained" (H-2.2.1) moves from /help/employees/balance to /help/employees/balance/your-balance-explained with a redirect, so the Balance topic (H-2.2) takes the old address; "Approval rules" (H-1.2.4, the PDF) is replaced by the article H-1.2.5 with a redirect, as IA2 said it would be.

- **perqo.com's structure** (§2.4): the top level is by topic (Product, Pricing, Customers, Help centre), with Book a demo and Sign in as task routes in the header; audience is used only inside the Help centre and on For merchants. Free: the navigation components and header design.
- **For merchants** (§2.5; Deliverable A): S-7, a footer page owned by the partnerships team. Free: its content; the merchant side's own surface.
- **Product's pages** (Deliverables A and B): Perqo Admin, Perqo app, Perqo card (IA2), plus a Benefits section with one page per F-CAT top-level value (S-1.4.1 to S-1.4.4, owned by the content team) and Security (S-1.5, owned by Product). No page per narrower term (R7 keeps two levels).
- **Category page URLs** (§5.1; Deliverable B, B.3): the identifier, then the preferred term: /product/benefits/cat-hea/health; a rename under R9 redirects the old address. Free: the URL form in other languages (DD-IA3).
- **Page IDs** (Deliverable A): S- for site pages, L- for campaign pages, H- for the Help centre (IA2's scheme kept); the inventory has 57 rows, 42 pages and files on the site today and 52 after the redesign, each with type, template, audience, owner, F-CAT tags and status. Free: traffic and last-modified dates for all but IA2's rows.
- **Owners on perqo.com** (Deliverable A): Marketing, Sales, Support, Product, Partnerships, Legal, Content team. No named people.
- **Audit findings** (§1.3; Deliverable A): S-1.2 says "allowance"; a Features page (S-1.6) and a brochure PDF (S-1.7) duplicate Product; Pricing says "Contact us for pricing"; the home page's opening line says neither what Perqo is nor who buys it; Book a demo asks for a phone number sales does not use; customer story S-3.4 is about a former client; campaign page L-02 outlived its campaign. Free: the pages' copy.
- **Customer stories** (Deliverable A): four today (a software consultancy, a logistics group, a design studio, a retail chain), three after the audit; each tagged with one F-CAT value. Free: client names; the stories' content.
- **Plans** (§5.4): two, each with a published price per employee per month. Free: plan names and amounts.
- **No self-serve sign-up and no free trial** (§5.5): a client starts after a contract. Free: the contract's terms.
- **Get the Perqo app** (§5.5; Deliverable A): S-6, owned by support, holds the download links; employees join from HR's invitation and do not sign in on perqo.com. Free: the app stores named.
- **Assumed, untested** (§5.5): an employee may press Sign in and land on Admin's sign-in screen; IA5 proposed a line there pointing employees to Get the Perqo app, which IA7 took with one change (see "Set by IA7": the line is shown to everyone). Free: the test's result.
- **Language** (§5.3): perqo.com is published in English only today. Free: which markets and languages come next (DD-IA3).
- **Campaign pages** (§5.2; Deliverable A): under /lp/, noindex, in no navigation, template T-12, each with an owner and an end date, redirected at the end; L-01 "Learning budgets for engineering teams" is live. Free: campaign dates and channels.
- **Help centre additions** (Deliverable A): Approvals topic under For HR and finance teams (H-1.3, H-1.3.1); Card topic under For employees (H-2.3, two articles); articles H-1.2.5 (replaces the PDF, listed under both audiences), H-2.1.3, H-2.1.4 (tagged CAT-HEA-FIT, answers "gym"), H-2.2.2; Balance gets its own topic page at /help/employees/balance and H-2.2.1 moves with a redirect; H-0.1 search results page, noindex. Free: the articles' text.
- **New attributes** (§3.3): a help article (O-14) and a customer story (O-15) carry F-CAT tags. Free: how many tags an item may carry.
- **The template catalogue** (Deliverable C): seventeen templates, T-01 to T-17, and twenty-seven modules, M-01 to M-27, with the required and optional modules of each; the Customers index filters stories by F-CAT; help articles carry a "Was this helpful" question sent to the owner. Free: visual design; module layout.
- **Status value "new"** (§1.1): in inventories, beside keep, update and remove.

## Set by IA6 (3 Nov 2026)

From IA6's table "Perqo facts set by this unit", verbatim, with the section that sets each and what it leaves free.

- The app's screens carry IDs A-0 to A-5 (A-0 Join and sign in, A-0.1 Join, A-0.2 Sign in; A-1 Home; A-2 Benefits, A-2.1 to A-2.4 the categories; A-3 Claims, A-3.1 New claim, A-3.2 Check and submit, A-3.3 Claim submitted, A-3.4 Claim; A-4 Card, A-4.1 Card details, A-4.2 Purchases, A-4.2.1 Purchase, A-4.3 Card offers, A-4.4 Freeze card; A-5 Account, A-5.1 Profile, A-5.2 Notifications) (Deliverable B). Free: visual design.
- Every app screen has an address under perqo.com/app/, identifier first; with the app installed it opens the screen, without it the address serves Get the Perqo app (S-6); entries E-1 to E-7 (section 6.3; Deliverable B, B.4). Free: the identifiers' format for claims and purchases.
- Home shows each open category with what remains, no total; Recent activity mixes purchases and claims, newest first, and says Submitted (section 4.1; Deliverable B). Free: how many items Recent activity shows.
- Each category screen shows the balance (remaining, spent, amount, period), What's covered with the covered catalogue items under each narrower term, cross-listed far members naming their home (assumed), the route to Card offers in that category when it has offers, New claim with the category chosen, and the link What you can claim in each category (H-2.1.3) (Deliverable B, B.3). Free: the order of items within a narrower term.
- Card carries the links Where you can pay with the Perqo card (H-2.3.2) and Freezing and unfreezing your card (H-2.3.1) (Deliverable B, B.3).
- The example client's policy covers all twelve sample catalogue items, BI-001 to BI-012 (extends IA3's six) (Deliverable B, B.3). Free: other clients' policies.
- Card offers is one screen under Card (A-4.3), filterable by category by identifier, listing only offers for items in the employee's open categories; Home has no offers banner; the partnerships team's request for two placings is recorded and not met (Deliverable B, B.1 and B.6). Free: the number of offers.
- Claims groups by Submitted, Approved, Rejected, Paid, newest first in each; the Claim screen (A-3.4) shows status, amount, category, date submitted, receipt and, when Rejected, the reason (over the balance, or by HR): a new claim attribute, rejection reason (Deliverable B). Free: the wording of each reason.
- New claim shows the chosen category's balance, takes the receipt by Take a photo or Choose a file, and shows "Claims over the limit need HR approval" with the group's limit and a link to H-1.2.5 (section 4; Deliverable C, C.3). Free: the limit's amount.
- Check and submit, when the amount is over the category's balance, shows "More than your Learning balance" (in the chosen category's name) with Edit only (section 4.3; Deliverable C, C.3).
- The camera is asked for when the employee taps Take a photo; notifications are asked for once, after the first claim is submitted (section 4.4). Free: the prompt's wording beyond its purpose.
- A card payment over the balance of the merchant's category, or with the card Frozen, is declined at the till; a declined attempt is not a card payment and is not shown in the app (proposed for IA8) (Deliverable C, C.2). Free: IA8's decision.
- An employee with no card issued sees the Card tab in the state "Your Perqo card has not been issued yet" (section 4.4). Free: when cards are issued.
- A category closed to the group is not shown, nor any cross-listing or offer that belongs to it (section 4.4).
- Without a connection, Home, Claims and Purchases show their last loaded content with the time it was loaded (section 4.3).
- The tab bar shows on every screen except Join, Sign in and modals; a claim in progress is kept when the employee changes tab (Deliverable B, B.3).
- HR's invitation is an email to the employee's work email with a link that opens Join (A-0.1), or S-6 without the app; Join confirms the employer's name and the work email (Deliverable B, B.4). Free: the sign-in method.
- Task frequencies per employee, assumed: pay with the card 8 a month; see the balance 3; read a notification 2; check a purchase and track a claim 1.5 each; submit a claim 1; find what's covered and find card offers 0.5 each; read a help article 0.3; freeze or unfreeze the card and see the profile 0.1 each; join once (Deliverable A). Free: measured use (IA11).
- New calls to action by the employee: claim -> view; catalogue item -> view (Deliverable A).
- Complexity and priority of the app's calls to action, and the attribute order on each screen, as in A.2 (Deliverable A, A.2).

## Set by IA7 (3 Nov 2026)

From IA7's table "Perqo facts set by this unit", verbatim but for the layout (the section that sets each in brackets, then what it leaves free). IA7 keeps every registered fact and renames none of IA1 to IA6's labels, objects, attributes or relationships; it answers IA4's "not set (IA7)" cells and two "role not set: IA7" rows, and IA5's proposal for Admin's sign-in screen.

- A sizing client, used for volumes here and by DD-IA2: 1,200 employees, 14 employee groups, three admin users (two HR managers, one finance manager); about 1,200 claims and 9,600 card payments a month; 15% of claims over the limit, about 180 a month, about 9 a working day over 20 working days; up to 4,800 allocations a period; it is not the example client of IA3 and IA6 (section 2.2). Free: the example client's size; measured volumes.
- Employee status: Invited, Active, Left; Left is an end state, after which the person cannot sign in to the app; claims submitted before leaving are still decided (sections 2.2, 5.1). Free: what happens to a leaver's allocations and card (IA8).
- Account owner: exactly one per client, an admin user who also holds the HR manager or finance manager role; edits company details, adds and removes admin users, changes roles, reads the Activity log, hands ownership on; Perqo sets up the first admin user as account owner (section 3.4). Free: the rest of a client's onboarding.
- Admin user status: Active, Removed; a removed admin user's name stays on their decisions and changes (section 2.2).
- Every client has at least two admin users with the HR manager role; an HR manager cannot decide their own claim (section 3.3; Deliverable D, EX-1).
- Claim attributes decided by and rejection note; rejecting a claim needs a note to the employee (section 2.2; Deliverable D). Free: the notes' wording.
- A waiting claim reserves nothing: spent counts approved and paid claims and card payments; on HR's approval the balance is checked again (T5) (section 5.2; Deliverable D).
- A claim waiting more than five working days is marked Overdue in Approvals (Deliverable D, EX-3).
- Audit entry (O-17): who, action, object and its ID, date and time, before and after; shown as History on each detail page and as the Activity log in Settings (section 5.3). Free: how long entries are kept.
- Relationships R-21 (admin user is also employee), R-22 (claim is decided by admin user), R-23 (audit entry records a change to), R-24 (audit entry is made by admin user) (Deliverable A, A.3).
- Admin's name for the card is "Perqo card", status only (Active, Frozen, Not issued), on the employee's record; Admin does not show notifications (section 2.3). Free: whether Admin sends HR messages of its own.
- Roles cover the whole client; the role-by-section matrix and the calls to action with their roles in Deliverables A and B; finance does not see Approvals; HR sees Budget use and Claims by status only (section 3; Deliverables A, B). Free: scoping roles to employee groups.
- Admin's pages AD-0 to AD-6 as in C.1; addresses identifier first (Deliverable C, C.1). Free: Admin's domain; the identifiers' format.
- Reports holds five views: Spend by category, Spend by employee group, Budget use, Claims by status, Card payments (section 4.6). Free: the reports' columns beyond those named.
- Work queues: Approvals (HR), Not joined (HR, Invited over 14 days), No budget for next period (finance) (Deliverable C, C.4).
- Bulk actions: approve selected; move to group; resend invitation; rejection one at a time (section 4.4).
- No search across Admin; a find field on each long list (section 4.5). Free: when a global search is added.
- Landing after sign-in: HR on Approvals, finance on Budgets (Deliverable C, C.2).
- A policy change applies to claims submitted after it (section 4.3).
- Admin is used in a desktop browser (assumed); on a narrow window list and detail show one at a time (section 4.3).
- Admin's sign-in screen carries "Looking for your benefits? Get the Perqo app", linking to S-6, for everyone (IA5's proposal, taken with one change) (Deliverable C, C.5). Free: the test's result.
- The invitation carries the client's name from Company and the Join link; Resend invitation sends it again (Deliverable C, C.4). Free: how long an invitation is valid.
- Model names of Admin's objects and attributes, as in A.2 (Deliverable A, A.2).

## Not yet set (free for the unit that needs it)

The merchant side's own surface and anything of it beyond IA3's card offers and IA4's merchant and offer objects; pages on Admin beyond IA7's map, AD-0 to AD-6 (perqo.com's are IA5's inventory; the app's are IA6's map, A-0 to A-5); roles inside Admin beyond HR manager, finance manager and IA7's account owner, and scoping a role to some employee groups; volumes beyond IA7's sizing client (IA3 and IA6 assume frequencies of use only); the purchase lifecycle of a client company; the employee's enrolment beyond IA6's invitation and Join; any number (budgets, limits, amounts) beyond IA5's page, template and module counts and IA7's sizing-client volumes, 15% over the limit, five working days and 14 days; any named person or client company (none may be real).
