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

## Not yet set (free for the unit that needs it)

The merchant side beyond IA3's card offers; pages below the top level on any surface beyond the fragments above; roles inside Admin beyond HR manager and finance manager; volumes (IA3 assumes frequencies of use only); the purchase lifecycle of a client company; the employee's enrolment; any number (budgets, limits, counts); any named person or client company (none may be real).
