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
- **Proposed for IA6, not facts yet** (Deliverable): rename the offers list "Card offers" and give it one placing; show the four category balances on Home; group Claims by all four states; label the "+" "New claim"; "Your balance explained" for the balance link; Help opens For employees; the rule "Claims over the limit need HR approval" on New claim, the limit read from the group's policy; Documents removed. IA6 keeps the labels IA3's checklist passes (its "What IA6 keeps").

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
- **Assumed, untested** (§5.5): an employee may press Sign in and land on Admin's sign-in screen; proposed for IA7: a line there pointing employees to Get the Perqo app. Free: the test's result; IA7's decision.
- **Language** (§5.3): perqo.com is published in English only today. Free: which markets and languages come next (DD-IA3).
- **Campaign pages** (§5.2; Deliverable A): under /lp/, noindex, in no navigation, template T-12, each with an owner and an end date, redirected at the end; L-01 "Learning budgets for engineering teams" is live. Free: campaign dates and channels.
- **Help centre additions** (Deliverable A): Approvals topic under For HR and finance teams (H-1.3, H-1.3.1); Card topic under For employees (H-2.3, two articles); articles H-1.2.5 (replaces the PDF, listed under both audiences), H-2.1.3, H-2.1.4 (tagged CAT-HEA-FIT, answers "gym"), H-2.2.2; Balance gets its own topic page at /help/employees/balance and H-2.2.1 moves with a redirect; H-0.1 search results page, noindex. Free: the articles' text.
- **New attributes** (§3.3): a help article (O-14) and a customer story (O-15) carry F-CAT tags. Free: how many tags an item may carry.
- **The template catalogue** (Deliverable C): seventeen templates, T-01 to T-17, and twenty-seven modules, M-01 to M-27, with the required and optional modules of each; the Customers index filters stories by F-CAT; help articles carry a "Was this helpful" question sent to the owner. Free: visual design; module layout.
- **Status value "new"** (§1.1): in inventories, beside keep, update and remove.

## Not yet set (free for the unit that needs it)

The merchant side's own surface and anything of it beyond IA3's card offers and IA4's merchant and offer objects; pages below the top level on Admin and the app beyond the fragments above (perqo.com's are IA5's inventory); roles inside Admin beyond HR manager and finance manager; volumes (IA3 assumes frequencies of use only); the purchase lifecycle of a client company; the employee's enrolment; any number (budgets, limits, counts) beyond IA5's page, template and module counts; any named person or client company (none may be real).
