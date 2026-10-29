"""The figure examples page (V1, 29 Oct 2026): one example of every kind kit/viz.py draws, eleven in all, each built on
Perqo, the fictional flexible-benefits platform of the Information Architecture course brief
(generator/data/ux/units_data.py). Every Perqo name and number here is invented for this page and labelled so.

build.py calls write(SITE, crumbs) after it has written the fetched files: this writes academy/viz-examples.html,
the panel's content, rendered from Markdown with ```viz fences by mdcourse.render_md (the path a markdown unit takes,
so the page shows a figure exactly as a unit declaring it will get it), and returns the panel's stub for the shell
(id viz-examples, in the root context, fetched like a report). Each section shows the figure, a line on what the kind
draws, its fields, and the block itself, so a writer can copy it. verify.py checks the file has eleven figures and,
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
]

NAMES = {'timeline': 'Timeline', 'compare': 'Compare', 'tree': 'Tree', 'flow': 'Flow', 'sitemap': 'Sitemap', 'objects': 'Object map',
         'decision': 'Decision tree', 'matrix': 'Matrix', 'states': 'State diagram', 'swimlanes': 'Swimlanes', 'wireflow': 'Wireflow'}


def fragment(crumbs):
    """The panel's content: a header with a jump list, then one section per kind (Markdown through render_md)."""
    assert [k for k, *_ in EXAMPLES] == list(viz.KINDS), 'one example per kind, in KINDS order'
    md, toc = [], ''
    for kind, what, fields, block in EXAMPLES:
        sid = f'vx-{kind}'
        toc += f'<a href="#{sid}">{NAMES[kind]}</a>'
        md.append(f'## {NAMES[kind]} · `{kind}`\n\n{what}\n\nFields: {fields.replace("_", chr(92) + "_")}; every kind also takes `title`, `caption` and `tone` (1 to 6).\n\n'
                  f'```viz\n{json.dumps(block, ensure_ascii=False, indent=1)}\n```\n\n{sid}BLOCK\n')
    body, _ = render_md('\n'.join(md))
    for kind, _, _, block in EXAMPLES:
        sid = f'vx-{kind}'
        body = body.replace(f'<h2>{NAMES[kind]} · <code>{kind}</code></h2>', f'<h2 id="{sid}">{NAMES[kind]} · <code>{kind}</code></h2>', 1)
        pre = html.escape('```viz\n' + json.dumps(block, ensure_ascii=False, indent=1) + '\n```')
        body = body.replace(f'<p>{sid}BLOCK</p>', f'<details class="prompt"><summary>The viz block, to copy into a unit</summary><pre>{pre}</pre></details>', 1)
    return f'''<header class="phead">
    {crumbs(('Academy', 'home'), ('Figure kinds', None))}
    <div class="eyebrow"><span class="u" style="--c:var(--blue)">FIGURES</span> · {len(EXAMPLES)} kinds · kit/viz.py</div>
    <h1>Figure kinds</h1>
    <nav class="toc" aria-label="Kinds">{toc}</nav>
  </header>
  <p class="lede">Every kind of figure a unit can declare, drawn by the build from a fenced <code>viz</code> block. The four first kinds came with A8; the seven after them were added for the Information Architecture course (V1, 29 October 2026). Each example uses Perqo, the course's fictional benefits platform: its names and numbers are invented for this page. Under each figure, the block that draws it.</p>
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
    for kind, _, _, block in EXAMPLES:
        out = viz.render(block)
        print(f'{kind:10} {len(out):6} bytes', 'wide' if 'viz-wide' in out else '')
