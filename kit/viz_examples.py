"""The figure examples page (V1, 29 Oct 2026): one example of every kind kit/viz.py draws (eleven at V1; P44, 29 Oct 2026, added line, bars, scatter, range and
the matrix's numeric mode, sixteen figures in all), each built on
Perqo, the fictional flexible-benefits platform of the Information Architecture course brief
(generator/data/ux/units_data.py). Every Perqo name and number here is invented for this page and labelled so.

build.py calls write(SITE, crumbs) after it has written the fetched files: this writes academy/viz-examples.html,
the panel's content, rendered from Markdown with ```viz fences by mdcourse.render_md (the path a markdown unit takes,
so the page shows a figure exactly as a unit declaring it will get it), and returns the panel's stub for the shell
(id viz-examples, in the root context, fetched like a report). Each section shows the figure, a line on what the kind
draws, its fields, and the block itself, so a writer can copy it. verify.py checks the file has VX_FIGS figures and,
in the browser, that every label lies inside its box and no drawing exceeds its frame.
"""
import html, json
import viz
from mdcourse import render_md

PANEL_ID = 'viz-examples'
FIC = 'Perqo is fictional; every name and number in this figure is invented for the examples page.'

# (kind, what it draws, its fields, the example block)
EXAMPLES = [
    ('timeline', 'Dated events on an axis, with spans as bands above it; a dense one widens and scrolls.',
     'start, end, ticks [year], events [{at, label, tone}], spans [{from, to, label, tone}]',
     {'kind': 'timeline', 'title': 'Perqo, 2018 to 2026 (fictional)', 'start': 2018, 'end': 2027,
      'ticks': [2018, 2020, 2022, 2024, 2026],
      'spans': [{'from': 2018, 'to': 2020, 'label': 'Seed', 'tone': 2}, {'from': 2020, 'to': 2024, 'label': 'Growth', 'tone': 3},
                {'from': 2024, 'to': 2027, 'label': 'Scale', 'tone': 4}],
      'events': [{'at': 2018, 'label': 'Perqo founded'}, {'at': 2019, 'label': 'perqo.com launched'},
                 {'at': 2020, 'label': 'First client company'}, {'at': 2021, 'label': 'Perqo app released'},
                 {'at': 2022, 'label': 'Merchant network opens'}, {'at': 2024, 'label': 'Perqo Admin rebuilt'},
                 {'at': 2026, 'label': 'Claims redesign'}],
      'caption': f'The Perqo company history used across the course. {FIC}'}),
    ('compare', 'Horizontal bars, one per row, against a shared maximum.',
     'unit, max, rows [{label, value, display, tone}]',
     {'kind': 'compare', 'title': 'Perqo app tasks by share of weekly sessions (fictional)', 'unit': '%', 'max': 100,
      'rows': [{'label': 'See a balance', 'value': 64, 'tone': 3}, {'label': 'Spend a benefit', 'value': 41, 'tone': 3},
               {'label': 'Browse the catalogue', 'value': 27, 'tone': 4}, {'label': 'Submit a claim', 'value': 18, 'tone': 2},
               {'label': 'Change a plan', 'value': 3, 'tone': 5}],
      'caption': f'Task frequency for the app inventory of IA6. {FIC}'}),
    ('tree', 'A top-down hierarchy of labelled boxes; the drawing scales to fit the column.',
     'root {label, tone, children [...]}',
     {'kind': 'tree', 'title': 'Perqo benefit categories (fictional)',
      'root': {'label': 'Benefits', 'children': [
          {'label': 'Wellbeing', 'children': [{'label': 'Gym pass'}, {'label': 'Therapy'}]},
          {'label': 'Mobility', 'children': [{'label': 'Transit pass'}, {'label': 'Bike lease'}]},
          {'label': 'Learning', 'children': [{'label': 'Courses'}, {'label': 'Books'}]},
          {'label': 'Food', 'children': [{'label': 'Meal card'}]}]},
      'caption': f'The top of the benefits catalogue that IA4 builds facets for. {FIC}'}),
    ('flow', 'A sequence of steps left to right, wrapping into rows.',
     'steps [{label, note, tone}], per_row',
     {'kind': 'flow', 'title': 'Onboarding a client company (fictional)', 'per_row': 4,
      'steps': [{'label': 'Contract signed', 'note': 'day 0', 'tone': 2}, {'label': 'Budgets set', 'note': 'HR, finance'},
                {'label': 'Policies set', 'note': 'HR'}, {'label': 'Employees imported', 'note': 'from payroll'},
                {'label': 'Invitations sent', 'note': 'app'}, {'label': 'First spend', 'note': 'about day 14', 'tone': 3}],
      'caption': f'The client side of the purchase lifecycle in IA8. {FIC}'}),
    ('sitemap', 'Site structure top-down: each node a page with an optional page type (the mono tag) and note; the first level wraps into rows, deeper levels stack under their parent.',
     'root {label, type, note, tone, children [...]}, stack_from (depth at which children stack; default 2)',
     {'kind': 'sitemap', 'title': 'perqo.com (fictional)',
      'root': {'label': 'Home', 'type': 'home', 'children': [
          {'label': 'Product', 'type': 'section', 'children': [
              {'label': 'How it works', 'type': 'product'}, {'label': 'For HR teams', 'type': 'landing'},
              {'label': 'For finance teams', 'type': 'landing'}]},
          {'label': 'Benefits catalogue', 'type': 'listing', 'note': 'filters from the IA4 facets'},
          {'label': 'Pricing', 'type': 'pricing', 'note': 'per employee per month'},
          {'label': 'Customers', 'type': 'listing', 'children': [{'label': 'Case study', 'type': 'article', 'note': 'one template, many pages'}]},
          {'label': 'Resources', 'type': 'section', 'children': [{'label': 'Blog', 'type': 'article'}, {'label': 'Guides', 'type': 'article'}]},
          {'label': 'Book a demo', 'type': 'form', 'tone': 1},
          {'label': 'Log in', 'type': 'auth', 'note': 'hands off to Perqo Admin or the app', 'tone': 6}]},
      'caption': f'The perqo.com sitemap of IA5 in outline: fourteen pages, seven at the first level. {FIC}'}),
    ('objects', 'An object map: boxes with a title, attributes and actions in the grid the data gives; lines carry a relationship and a cardinality at each end.',
     'objects [{id, title, attrs [], actions [], tone}], rows [[id or null]], links [{from, to, label, from_card, to_card}]',
     {'kind': 'objects', 'title': 'The Perqo object map (fictional)',
      'objects': [
          {'id': 'company', 'title': 'Company', 'tone': 4, 'attrs': ['name', 'plan', 'renewal date'], 'actions': ['→ renew', '→ add admin']},
          {'id': 'policy', 'title': 'Policy', 'tone': 5, 'attrs': ['eligibility rules', 'waiting period', 'approval route'], 'actions': ['→ publish']},
          {'id': 'budget', 'title': 'Budget', 'tone': 6, 'attrs': ['amount per period', 'period', 'rollover rule'], 'actions': ['→ top up']},
          {'id': 'employee', 'title': 'Employee', 'tone': 3, 'attrs': ['name', 'contract status', 'start date'], 'actions': ['→ invite', '→ offboard']},
          {'id': 'claim', 'title': 'Claim', 'tone': 2, 'attrs': ['amount', 'receipt', 'status'], 'actions': ['→ approve', '→ reject']},
          {'id': 'benefit', 'title': 'Benefit', 'tone': 1, 'attrs': ['category', 'merchant', 'price'], 'actions': ['→ spend']}],
      'rows': [['company', 'policy', 'budget'], ['employee', 'claim', 'benefit']],
      'links': [
          {'from': 'company', 'to': 'policy', 'label': 'sets', 'from_card': '1', 'to_card': '1..*'},
          {'from': 'policy', 'to': 'budget', 'label': 'governs', 'from_card': '1', 'to_card': '1..*'},
          {'from': 'company', 'to': 'employee', 'label': 'employs', 'from_card': '1', 'to_card': '0..*'},
          {'from': 'policy', 'to': 'claim', 'label': 'routes approval', 'from_card': '1', 'to_card': '0..*'},
          {'from': 'budget', 'to': 'benefit', 'label': 'funds', 'from_card': '1..*', 'to_card': '0..*'},
          {'from': 'employee', 'to': 'claim', 'label': 'submits', 'from_card': '1', 'to_card': '0..*'},
          {'from': 'claim', 'to': 'benefit', 'label': 'is for', 'from_card': '0..*', 'to_card': '1'}],
      'caption': f'Six objects of the IA4 object map, with the calls to action on each. {FIC}'}),
    ('decision', 'A decision tree read top-down: questions as boxes, a labelled arrow per branch, outcomes as filled boxes.',
     'root {q, tone, branches [{label, to}]} or {outcome, tone}',
     {'kind': 'decision', 'title': 'Is this employee eligible for this benefit? (fictional)',
      'root': {'q': 'Active employment contract?', 'branches': [
          {'label': 'no', 'to': {'outcome': 'Not eligible', 'tone': 1}},
          {'label': 'yes', 'to': {'q': 'Past the 30-day waiting period?', 'branches': [
              {'label': 'no', 'to': {'outcome': 'Eligible from day 31', 'tone': 2}},
              {'label': 'yes', 'to': {'q': 'Benefit in the company policy?', 'branches': [
                  {'label': 'no', 'to': {'outcome': 'Not covered', 'tone': 1}},
                  {'label': 'yes', 'to': {'q': 'Budget left this period?', 'branches': [
                      {'label': 'no', 'to': {'outcome': 'Eligible, waits for the next period', 'tone': 6}},
                      {'label': 'yes', 'to': {'outcome': 'Eligible', 'tone': 3}}]}}]}}]}}]},
      'caption': f'The eligibility rule that IA8 draws across the three surfaces. {FIC}'}),
    ('matrix', 'A labelled grid: rows by columns, each cell a short mark on a field of its tone; a legend under it.',
     'cols [label], rows [{label, tone, cells [mark or {mark, tone} or null]}], legend [{mark, means, tone}]',
     {'kind': 'matrix', 'title': 'Perqo Admin: role by section (fictional)',
      'cols': ['Employees', 'Budgets', 'Policies', 'Claims', 'Reports', 'Settings'],
      'rows': [
          {'label': 'HR admin', 'cells': [{'mark': 'edit', 'tone': 3}, {'mark': 'view', 'tone': 4}, {'mark': 'edit', 'tone': 3}, {'mark': 'view', 'tone': 4}, {'mark': 'export', 'tone': 6}, {'mark': 'edit', 'tone': 3}]},
          {'label': 'Finance manager', 'cells': [{'mark': 'view', 'tone': 4}, {'mark': 'edit', 'tone': 3}, {'mark': 'view', 'tone': 4}, {'mark': 'approve', 'tone': 2}, {'mark': 'export', 'tone': 6}, None]},
          {'label': 'Line manager', 'cells': [{'mark': 'own team', 'tone': 4}, None, None, {'mark': 'approve', 'tone': 2}, None, None]},
          {'label': 'Auditor (read only)', 'cells': [{'mark': 'view', 'tone': 4}, {'mark': 'view', 'tone': 4}, {'mark': 'view', 'tone': 4}, {'mark': 'view', 'tone': 4}, {'mark': 'export', 'tone': 6}, None]}],
      'legend': [{'mark': 'edit', 'means': 'create, change, delete', 'tone': 3}, {'mark': 'view', 'means': 'read only', 'tone': 4},
                 {'mark': 'approve', 'means': 'act on a work queue', 'tone': 2}, {'mark': 'export', 'means': 'download reports', 'tone': 6}],
      'caption': f'The role-by-section matrix of IA7; a blank cell is a section the role cannot reach. {FIC}'}),
    ('states', 'A state diagram: states in the order given as rounded boxes, labelled transitions, a start marker, end states with an inner ring, loops for self-transitions.',
     'states [{id, label, note, tone, end}], start, transitions [{from, to, label}], per_row (default 4)',
     {'kind': 'states', 'title': 'A Perqo reimbursement claim (fictional)', 'per_row': 4,
      'states': [{'id': 'draft', 'label': 'Draft', 'tone': 5}, {'id': 'submitted', 'label': 'Submitted'},
                 {'id': 'review', 'label': 'In review', 'note': 'approver queue'}, {'id': 'approved', 'label': 'Approved', 'tone': 3},
                 {'id': 'withdrawn', 'label': 'Withdrawn', 'tone': 6, 'end': True}, {'id': 'info', 'label': 'Info requested', 'tone': 2},
                 {'id': 'rejected', 'label': 'Rejected', 'tone': 1, 'end': True}, {'id': 'paid', 'label': 'Paid', 'tone': 3, 'end': True}],
      'transitions': [
          {'from': 'draft', 'to': 'submitted', 'label': 'submit'}, {'from': 'submitted', 'to': 'review', 'label': 'assign'},
          {'from': 'review', 'to': 'approved', 'label': 'approve'}, {'from': 'review', 'to': 'review', 'label': 'reassign'},
          {'from': 'review', 'to': 'info', 'label': 'ask for a receipt'}, {'from': 'info', 'to': 'submitted', 'label': 'resubmit'},
          {'from': 'review', 'to': 'rejected', 'label': 'reject'}, {'from': 'approved', 'to': 'paid', 'label': 'pay out with payroll'},
          {'from': 'submitted', 'to': 'withdrawn', 'label': 'withdraw'}],
      'caption': f'The claim-approval lifecycle of IA7. {FIC}'}),
    ('swimlanes', 'Lanes per actor or surface, steps placed in lanes by column, connectors across lanes with labels; widens and scrolls.',
     'lanes [{id, label, tone}], steps [{id, lane, col, label, note, tone}], links [{from, to, label}]',
     {'kind': 'swimlanes', 'title': "The employee's benefit lifecycle across Perqo (fictional)",
      'lanes': [{'id': 'app', 'label': 'Perqo app · employee', 'tone': 3}, {'id': 'admin', 'label': 'Perqo Admin · HR and finance', 'tone': 4},
                {'id': 'merchant', 'label': 'Merchant', 'tone': 2}],
      'steps': [
          {'id': 'open', 'lane': 'admin', 'col': 0, 'label': 'Open enrolment', 'note': 'once a year'},
          {'id': 'enrol', 'lane': 'app', 'col': 1, 'label': 'Enrol', 'note': 'pick a plan'},
          {'id': 'learn', 'lane': 'app', 'col': 2, 'label': 'Learn', 'note': 'browse the catalogue'},
          {'id': 'decide', 'lane': 'app', 'col': 3, 'label': 'Decide', 'note': 'check the balance'},
          {'id': 'charge', 'lane': 'merchant', 'col': 4, 'label': 'Spend', 'note': 'Perqo card at a partner'},
          {'id': 'claim', 'lane': 'app', 'col': 4, 'label': 'Claim', 'note': 'receipt from elsewhere'},
          {'id': 'approve', 'lane': 'admin', 'col': 5, 'label': 'Approve the claim'},
          {'id': 'review', 'lane': 'app', 'col': 6, 'label': 'Review', 'note': 'balance and history'}],
      'links': [
          {'from': 'open', 'to': 'enrol', 'label': 'invites'}, {'from': 'enrol', 'to': 'learn'}, {'from': 'learn', 'to': 'decide'},
          {'from': 'decide', 'to': 'charge', 'label': 'pays by card'}, {'from': 'decide', 'to': 'claim', 'label': 'pays elsewhere'},
          {'from': 'claim', 'to': 'approve', 'label': 'submits'}, {'from': 'charge', 'to': 'review', 'label': 'settles'},
          {'from': 'approve', 'to': 'review', 'label': 'reimburses'}],
      'caption': f'Enrol, learn, decide, spend, claim, review: the employee lifecycle of IA8 across the app, the backoffice and a merchant. {FIC}'}),
    ('wireflow', 'Screens with a title and content placeholders, arrows between them with a label, left to right and wrapping.',
     'screens [{id, title, tone, lines [text or {bar} or {block} or {button}]}], links [{from, to, label}], per_row (default 3)',
     {'kind': 'wireflow', 'title': 'See a balance, spend, claim: the Perqo app (fictional)',
      'screens': [
          {'id': 'home', 'title': 'Home', 'lines': ['Balance this month', 'EUR 412 of 600', {'bar': 0.69}, 'Wellbeing · Mobility · Food', {'block': 34}, {'button': 'New claim'}]},
          {'id': 'spend', 'title': 'Gym pass', 'tone': 4, 'lines': ['EUR 45 a month', {'bar': 0.8}, {'bar': 0.55}, 'Partner gyms near you', {'block': 34}, {'button': 'Spend from Wellbeing'}]},
          {'id': 'claim', 'title': 'New claim', 'tone': 2, 'lines': ['Amount', {'bar': 0.4}, 'Receipt', {'block': 40}, {'button': 'Submit'}]}],
      'links': [{'from': 'home', 'to': 'spend', 'label': 'tap Wellbeing, then Gym pass'}, {'from': 'spend', 'to': 'home', 'label': 'back'},
                {'from': 'home', 'to': 'claim', 'label': 'tap New claim'}],
      'caption': f'The three core flows of IA6, as one wireflow. {FIC}'}),
    ('line', 'One or more named series over an ordered x (years, periods or any ordered labels), each point labelled with its value (or only the ends), optional annotations, a legend.',
     'x [value], years (format x as years), series [{name, values [number or null], tone}], unit, decimals, min, max, yticks, xticks, labels ("all", "ends" or "none"), annotations [{at, label}], height, xlabel, ylabel',
     {'kind': 'line', 'title': 'Perqo users, 2019 to 2026, thousands (fictional)', 'years': True, 'unit': 'k',
      'x': [2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026],
      'series': [{'name': 'Employees with a balance', 'values': [None, 1.2, 6, 14, 23, 31, 38, 45], 'tone': 4},
                 {'name': 'Monthly app users', 'values': [None, None, 2.5, 9, 16, 22, 29, 35], 'tone': 3}],
      'annotations': [{'at': 2021, 'label': 'Perqo app released'}, {'at': 2024, 'label': 'Perqo Admin rebuilt'}],
      'caption': f'Growth since the first client company, in the dates of the timeline above. {FIC}'}),
    ('bars', 'Grouped or stacked horizontal bars across categories, a legend, values at the bar ends (and inside a stacked segment when it fits).',
     'mode ("grouped" or "stacked"), series [{name, tone}], rows [{label, values [number or null]}], unit, decimals, max',
     {'kind': 'bars', 'title': 'Benefit spend by category and channel, 2026 to date, EUR million (fictional)', 'mode': 'stacked', 'decimals': 1,
      'series': [{'name': 'Perqo card', 'tone': 4}, {'name': 'Reimbursed claims', 'tone': 2}],
      'rows': [{'label': 'Food', 'values': [5.6, 0.2]}, {'label': 'Wellbeing', 'values': [4.2, 1.1]},
               {'label': 'Mobility', 'values': [3.1, 0.6]}, {'label': 'Learning', 'values': [0.9, 1.4]}],
      'caption': f'Where the money goes, and how much of it still passes through a claim. {FIC}'}),
    ('scatter', 'Labelled points on two numeric axes, optional quadrant lines and quadrant names; labels placed so that none overlaps a point or another label.',
     'x {label, min, max, ticks, unit, decimals, years}, y {the same}, points [{label, x, y, tone}], quadrants {x, y, names [top left, top right, bottom left, bottom right]}, height',
     {'kind': 'scatter', 'title': 'Benefits: uptake against satisfaction (fictional)',
      'x': {'label': 'employees using it, %', 'min': 0, 'max': 60, 'ticks': [0, 10, 20, 30, 40, 50, 60], 'unit': '%'},
      'y': {'label': 'satisfaction, 0 to 10', 'min': 5, 'max': 10, 'ticks': [5, 6, 7, 8, 9, 10]},
      'points': [{'label': 'Gym pass', 'x': 38, 'y': 7.9}, {'label': 'Therapy', 'x': 9, 'y': 8.6}, {'label': 'Transit pass', 'x': 44, 'y': 6.8},
                 {'label': 'Bike lease', 'x': 6, 'y': 8.1}, {'label': 'Courses', 'x': 14, 'y': 6.2}, {'label': 'Books', 'x': 21, 'y': 7.4},
                 {'label': 'Meal card', 'x': 57, 'y': 7.1}],
      'quadrants': {'x': 25, 'y': 7.5, 'names': ['loved, niche', 'loved, popular', 'weak, niche', 'popular, weak']},
      'caption': f'The benefit categories of the tree above, by uptake and by a satisfaction survey. {FIC}'}),
    ('range', 'Competing estimates: per row a bar from the lowest to the highest estimate, an optional point estimate, and the source of each end.',
     'rows [{label, low, high, point, low_src, high_src, tone}], unit, decimals, years (values are years: 264 BC, AD 14), min, max, ticks, xlabel',
     {'kind': 'range', 'title': 'Adoption of the new claims flow after six months, by client size (fictional)', 'unit': '%', 'min': 0, 'max': 100,
      'ticks': [0, 25, 50, 75, 100],
      'rows': [{'label': 'Large clients', 'low': 45, 'high': 70, 'point': 58, 'low_src': 'finance', 'high_src': 'product'},
               {'label': 'Mid-size clients', 'low': 30, 'high': 62, 'point': 41, 'low_src': 'finance', 'high_src': 'product'},
               {'label': 'Small clients', 'low': 18, 'high': 50, 'point': 27, 'low_src': 'finance', 'high_src': 'sales'}],
      'caption': f'Three teams\' forecasts for the IA7 claims redesign; the diamond is the planning figure. {FIC}'}),
    ('matrix-numeric', 'The matrix with numbers: each cell a value shaded in one tone by where it falls between the lowest and the highest, and a legend with the scale.',
     'numeric (true), cols [label], rows [{label, cells [number or null]}], tone, unit, decimals, min, max, scale_label',
     {'kind': 'matrix', 'numeric': True, 'title': 'Claims approved within 48 hours, % by client size (fictional)', 'tone': 3, 'unit': '%',
      'min': 40, 'max': 90,
      'cols': ['2025 Q1', '2025 Q2', '2025 Q3', '2025 Q4', '2026 Q1', '2026 Q2', '2026 Q3'],
      'rows': [{'label': 'Large clients', 'cells': [62, 64, 61, 70, 78, 83, 88]},
               {'label': 'Mid-size clients', 'cells': [55, 57, 58, 63, 71, 76, 81]},
               {'label': 'Small clients', 'cells': [44, 47, 46, 52, 60, None, 72]}],
      'caption': f'Approval speed before and after the claims redesign; the blank cell is a quarter with too few claims to report. {FIC}'}),
]

# P55 (30 Oct 2026): one case per drawing fault the N4 checkers met in the Rome retrofit, each drawn the way the renderer
# now draws it, so verify.py's figure checks (text inside its box or bar, nothing outside the drawing, no two labels
# overlapping) run on it at every build. Invented data, not Perqo: some faults need years BC.
CASE = 'A test case for the renderer (P55); its names, dates and numbers are invented and claim nothing.'
CASES = [
    ('timeline-short-spans', 'Span labels wider than their bars: drawn beside the bar in the muted colour, never across it in the on-accent colour (Rome 1.5, 5.6, 7.4, 8.6).',
     {'kind': 'timeline', 'title': 'Short spans', 'start': -800, 'end': -100, 'ticks': [-800, -600, -400, -200],
      'spans': [{'from': -753, 'to': -716, 'label': 'First reign', 'tone': 1}, {'from': -716, 'to': -509, 'label': 'The later reigns', 'tone': 2},
                {'from': -509, 'to': -500, 'label': 'First magistrates', 'tone': 3}, {'from': -500, 'to': -496, 'label': 'A war', 'tone': 4}],
      'events': [{'at': -753, 'label': 'A foundation, by one count'}, {'at': -509, 'label': 'A first election'}],
      'caption': CASE}),
    ('timeline-overlap', 'Spans that overlap in time: each takes its own lane, abutting spans share one (Rome 5.6, 7.1, 10.2).',
     {'kind': 'timeline', 'title': 'Overlapping spans', 'start': -300, 'end': -100, 'ticks': [-300, -250, -200, -150, -100],
      'spans': [{'from': -264, 'to': -241, 'label': 'First war', 'tone': 1}, {'from': -250, 'to': -200, 'label': 'An era across both', 'tone': 2},
                {'from': -241, 'to': -218, 'label': 'Interval', 'tone': 6}, {'from': -218, 'to': -201, 'label': 'Second war', 'tone': 3},
                {'from': -149, 'to': -146, 'label': 'Third', 'tone': 4}],
      'events': [{'at': -264, 'label': 'The war begins'}],
      'caption': CASE}),
    ('timeline-edges', 'Event labels at both ends of the axis, and a BC to AD axis: labels stay inside the drawing, and the year after 1 BC is AD 1 (Rome 6.4, 1.6; a tick at 0 stops the build, see below).',
     {'kind': 'timeline', 'title': 'Labels at the edges', 'start': -500, 'end': 200, 'ticks': [-500, -250, 1, 200],
      'events': [{'at': -500, 'label': 'A long event label at the very left edge of the axis'}, {'at': -498, 'label': 'Another long label beside it'},
                 {'at': 199, 'label': 'A long event label at the very right edge'}, {'at': 200, 'label': 'And another at the right'}],
      'caption': CASE}),
    ('compare-long', 'A label wider than the old 170-unit column, a large value and a word unit: the column grows and wraps, values take separators and a space before a word (Rome 3.4, 11.1, 1.2).',
     {'kind': 'compare', 'title': 'Long labels, large values', 'unit': 'men',
      'rows': [{'label': 'A row label far wider than the old label column allowed', 'value': 1200},
               {'label': 'A census', 'value': 770000, 'tone': 4}, {'label': 'Short', 'value': 337022, 'tone': 3}],
      'caption': CASE}),
    ('bars-long', 'The same in bars, grouped: long labels wrap in a column that grows to fit, values are separated and spaced.',
     {'kind': 'bars', 'mode': 'grouped', 'title': 'Long labels in bars', 'unit': 'words',
      'series': [{'name': 'Draft', 'tone': 2}, {'name': 'Final', 'tone': 3}],
      'rows': [{'label': 'A row label far wider than the old label column allowed', 'values': [770000, 412000]},
               {'label': 'Another', 'values': [1200, 900]}],
      'caption': CASE}),
    ('tree-ten', 'A tree of ten leaves: boxes keep their width and the drawing scrolls; labels wrap whole (they shrank to 64 units and broke mid-word, Rome 9.1, 10.2).',
     {'kind': 'tree', 'title': 'Ten leaves',
      'root': {'label': 'A root with ten children', 'children': [{'label': n} for n in
               ('Constantinople', 'Thessalonica', 'Nicomedia', 'Antioch on the Orontes', 'Alexandria', 'Carthage', 'Mediolanum', 'Treveri', 'Sirmium', 'Ravenna')]},
      'caption': CASE}),
    ('objects-long', 'A two-column object map with long attributes: each wraps by words inside its box; attrs given as a bare string stop the build (Rome 4.5, see below).',
     {'kind': 'objects', 'title': 'Long attributes',
      'objects': [{'id': 'a', 'title': 'An assembly', 'attrs': ['an attribute long enough to wrap over several lines in its box', 'short'], 'tone': 2},
                  {'id': 'b', 'title': 'A magistrate', 'attrs': ['another rather long attribute, also wrapped by words'], 'actions': ['-> convenes it'], 'tone': 4}],
      'rows': [['a', 'b']], 'links': [{'from': 'b', 'to': 'a', 'label': 'presides', 'from_card': '1', 'to_card': '1'}],
      'caption': CASE}),
    ('range-bc', 'A range of years BC: with "years": true they print as years, not as negative numbers (Rome 3.5).',
     {'kind': 'range', 'title': 'Competing dates', 'years': True, 'min': -300, 'max': -100, 'ticks': [-300, -250, -200, -150, -100],
      'rows': [{'label': 'An event dated two ways', 'low': -264, 'high': -241, 'point': -250, 'low_src': 'one source', 'high_src': 'another', 'tone': 4},
               {'label': 'A second event', 'low': -218, 'high': -202, 'low_src': 'one', 'high_src': 'another', 'tone': 2}],
      'caption': CASE}),
    # P58 (30 Oct 2026): one case per drawing fault the N5 checkers met in the Greek retrofit.
    ('range-single', 'A row whose low equals its high: one value, drawn as a point and printed once with one source tag; end labels sit under the value they name (Greek 1.1, 1.2, 5.1, 6.1, 8.5, 9.4, 10.10).',
     {'kind': 'range', 'title': 'One value, and a narrow range', 'years': True, 'min': -1500, 'max': -1300, 'ticks': [-1500, -1450, -1400, -1350, -1300],
      'rows': [{'label': 'Dated once, by two sources that agree', 'low': -1400, 'high': -1400, 'point': -1400, 'low_src': 'one source', 'high_src': 'one source', 'tone': 4},
               {'label': 'Dated once, by two sources that differ', 'low': -1375, 'high': -1375, 'low_src': 'one', 'high_src': 'another', 'tone': 2},
               {'label': 'A range too narrow for both labels under it', 'low': -1430, 'high': -1420, 'low_src': 'a first source', 'high_src': 'a second', 'tone': 3}],
      'caption': CASE}),
    ('timeline-circa', 'Event labels that wrap where a "c." meets its year: "c.", "by" and "after" stay with the number (Greek 5.1, 7.1, 7.2, 9.1, 10.2, 12.4).',
     {'kind': 'timeline', 'title': 'Circa in a wrapped label', 'start': -800, 'end': -300, 'ticks': [-800, -700, -600, -500, -400, -300],
      'events': [{'at': -670, 'label': 'A long label whose middle words fall at c. 670 when wrapped'},
                 {'at': -530, 'label': 'Another one, rebuilt by 500 or (c. 530)'},
                 {'at': -345, 'label': 'A move to an island (from c. 345)'}],
      'caption': CASE}),
    ('timeline-dates', 'Events with their own date text (an approximate year, a split year) and a figure in BCE/CE: the date line prints the text, so the label need not repeat it (Greek 3.1, 3.3, 3.7, 10.2; Rome 1.6, 7.4).',
     {'kind': 'timeline', 'title': 'Dates as the text gives them', 'era': 'BCE', 'start': -700, 'end': 100, 'ticks': [-700, -500, -300, -100, 100],
      'events': [{'at': -600, 'date': 'c. 600 BCE', 'label': 'An approximate year'}, {'at': -476, 'date': '476/5 BCE', 'label': 'A split year'},
                 {'at': -500, 'date': 'c. 500, or after 490 BCE', 'label': 'A date given two ways'}, {'at': 14, 'label': 'A plain year in CE'}],
      'caption': CASE}),
    ('objects-gap', 'A link label with a long word between two columns: the gap widens until the word fits, never cut mid-word (Greek 5.4, 10.9).',
     {'kind': 'objects', 'title': 'A long link label',
      'objects': [{'id': 'a', 'title': 'A city', 'attrs': ['an assembly'], 'tone': 2}, {'id': 'b', 'title': 'A neighbour', 'attrs': ['a council'], 'tone': 4},
                  {'id': 'c', 'title': 'A third city', 'attrs': ['a king'], 'tone': 3}],
      'rows': [['a', 'b', 'c']], 'links': [{'from': 'a', 'to': 'b', 'label': 'concedes territory'}, {'from': 'b', 'to': 'c', 'label': 'prepares business'}],
      'caption': CASE}),
    ('range-singular', 'A word unit and a value of 1: the unit takes the singular ("1 head", not "1 heads"; Greek 2.6).',
     {'kind': 'range', 'title': 'One of a word unit', 'unit': 'heads', 'min': 0, 'max': 10, 'ticks': [0, 2, 4, 6, 8, 10],
      'rows': [{'label': 'Counted from one to nine', 'low': 1, 'high': 9, 'low_src': 'one source', 'high_src': 'another', 'tone': 4}],
      'caption': CASE}),
    ('tree-chain', 'A one-child chain: centred in the drawing, not against its left edge (Greek 8.1).',
     {'kind': 'tree', 'title': 'A chain',
      'root': {'label': 'A first level', 'children': [{'label': 'A second level', 'children': [{'label': 'A third level'}]}]},
      'caption': CASE}),
]
# blocks the renderer cannot draw honestly: each stops the build with the message shown (verify.py renders each and checks)
RAISES = [
    ('A tick at year 0', {'kind': 'timeline', 'start': -100, 'end': 100, 'ticks': [-100, 0, 100]}, 'there is no year 0'),
    ('Ticks too close to label', {'kind': 'timeline', 'start': -100, 'end': 100, 'ticks': [-100, -1, 1, 100]}, 'too close to label both'),
    ('An object\'s attrs as a bare string', {'kind': 'objects', 'objects': [{'id': 'a', 'title': 'Assembly', 'attrs': 'like an aristocracy'}], 'rows': [['a']]}, 'must be a list'),
    ('Negative whole numbers in a range without "years"', {'kind': 'range', 'rows': [{'label': 'A date', 'low': -264, 'high': -241}]}, '"years": true'),
    ('An event date that does not contain its year (P58)', {'kind': 'timeline', 'start': -700, 'end': -500, 'events': [{'at': -600, 'date': 'c. 650 BC', 'label': 'A date'}]}, 'does not contain the year'),
    ('An event date in BC/AD in a BCE/CE figure (P58)', {'kind': 'timeline', 'era': 'BCE', 'start': -700, 'end': -500, 'events': [{'at': -600, 'date': 'c. 600 BC', 'label': 'A date'}]}, 'mixes notations'),
    ('A word unit not ending in s, a value of 1 and no "unit_one" (P58)', {'kind': 'range', 'unit': 'men', 'rows': [{'label': 'A count', 'low': 1, 'high': 5}]}, '"unit_one"'),
]

NAMES = {'timeline': 'Timeline', 'compare': 'Compare', 'tree': 'Tree', 'flow': 'Flow', 'sitemap': 'Sitemap', 'objects': 'Object map',
         'decision': 'Decision tree', 'matrix': 'Matrix', 'states': 'State diagram', 'swimlanes': 'Swimlanes', 'wireflow': 'Wireflow',
         'line': 'Line chart', 'bars': 'Bars', 'scatter': 'Scatter', 'range': 'Range', 'matrix-numeric': 'Matrix, numeric'}


def fragment(crumbs):
    """The panel's content: a header with a jump list, then one section per kind (Markdown through render_md)."""
    assert list(dict.fromkeys(b['kind'] for *_, b in EXAMPLES)) == list(viz.KINDS), 'one example per kind, in KINDS order'
    md, toc = [], ''
    for key, what, fields, block in EXAMPLES:
        sid, kind = f'vx-{key}', block['kind']
        toc += f'<a href="#{sid}">{NAMES[key]}</a>'
        md.append(f'## {NAMES[key]} · `{kind}`\n\n{what}\n\nFields: {fields.replace("_", chr(92) + "_")}; every kind also takes `title`, `caption` and `tone` (1 to 6).\n\n'
                  f'```viz\n{json.dumps(block, ensure_ascii=False, indent=1)}\n```\n\n{sid}BLOCK\n')
    md.append('## Hard cases\n\nThe drawing faults the Rome figure checkers met (P55, 30 October 2026) and the Greek ones (P58, the same day), '
              'each as the renderer now draws it, so the build\'s checks run on it every time. Their data is invented.\n')
    for key, what, block in CASES:
        md.append(f'### {block["title"]}\n\n{what}\n\n```viz\n{json.dumps(block, ensure_ascii=False, indent=1)}\n```\n')
    md.append('### Blocks that stop the build\n\nA figure the renderer cannot draw honestly is not drawn: the build stops and says what to change.\n')
    for what, block, _ in RAISES:
        try:
            viz.render(json.loads(json.dumps(block)))
            raise SystemExit(f'viz_examples: the case {what!r} drew; it should stop the build')
        except SystemExit as e:
            msg = str(e)
        md.append(f'- {what}: `{json.dumps(block, ensure_ascii=False)}` stops with: {msg.replace("_", chr(92) + "_")}\n')
    body, _ = render_md('\n'.join(md))
    toc += '<a href="#vx-cases">Hard cases</a>'
    body = body.replace('<h2>Hard cases</h2>', '<h2 id="vx-cases">Hard cases</h2>', 1)
    for key, _, _, block in EXAMPLES:
        sid, kind = f'vx-{key}', block['kind']
        body = body.replace(f'<h2>{NAMES[key]} · <code>{kind}</code></h2>', f'<h2 id="{sid}">{NAMES[key]} · <code>{kind}</code></h2>', 1)
        pre = html.escape('```viz\n' + json.dumps(block, ensure_ascii=False, indent=1) + '\n```')
        body = body.replace(f'<p>{sid}BLOCK</p>', f'<details class="prompt"><summary>The viz block, to copy into a unit</summary><pre>{pre}</pre></details>', 1)
    return f'''<header class="phead">
    {crumbs(('Academy', 'home'), ('Figure kinds', None))}
    <div class="eyebrow"><span class="u" style="--c:var(--blue)">FIGURES</span> · {len(viz.KINDS)} kinds · kit/viz.py</div>
    <h1>Figure kinds</h1>
    <nav class="toc" aria-label="Kinds">{toc}</nav>
  </header>
  <p class="lede">Every kind of figure a unit can declare, drawn by the build from a fenced <code>viz</code> block. The four first kinds came with A8; the seven after them were added for the Information Architecture course (V1, 29 October 2026); the last four, and the matrix's numeric mode, are for data (P44, 29 October 2026). On a phone a figure keeps its natural size and scrolls sideways inside its frame. Each example uses Perqo, the course's fictional benefits platform: its names and numbers are invented for this page. Under each figure, the block that draws it.</p>
  <div class="report">{body}</div>
'''


def write(site, crumbs):
    """Write academy/viz-examples.html and return the panel's stub for the shell."""
    frag = fragment(crumbs)
    (site / 'viz-examples.html').write_text(frag)
    import re
    anchors = ' '.join(re.findall(r' id="([^"]+)"', frag))
    return (f'\n<section class="panel" id="{PANEL_ID}" data-ctx="root" data-kind="figures" data-t="Figure kinds" data-u="ACADEMY" '
            f'data-c="var(--blue)" data-src="viz-examples.html" data-anchors="{anchors}" hidden></section>')


if __name__ == '__main__':
    for key, _, _, block in EXAMPLES:
        out = viz.render(block)
        print(f'{key:15} {len(out):6} bytes', 'wide' if 'viz-wide' in out else '')
