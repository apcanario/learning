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
     'rows [{label, low, high, point, low_src, high_src, tone}], unit, decimals, min, max, ticks, xlabel',
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
    body, _ = render_md('\n'.join(md))
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
