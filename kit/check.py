"""Check report fragments against AGENT-SPEC.md.

Usage: python3 check.py rome/r-1.4.html [more files]   (target taken from the prompt in the syllabus)
       python3 check.py --target 2500 path/to/file.html
Exit code 1 if any hard check fails. Length against the target is advisory (a soft note), never a failure.
"""
import re, sys, html, pathlib
from html.parser import HTMLParser

R = pathlib.Path(__file__).resolve().parent
ALLOWED = {'h2', 'h3', 'p', 'ul', 'ol', 'li', 'strong', 'em', 'blockquote', 'table', 'thead', 'tbody', 'tr', 'th', 'td',
           'div', 'pre', 'aside', 'details', 'summary', 'sub', 'sup', 'br'}
VOID = {'br'}
US = r'\b(?:color|honor|favor|labor|behavior|center|theater|defense|offense|catalog(?!ue)|traveled|traveling|modeled|fulfill(?!ed)|\w+?(?<!s)(?<!pr)(?<!se)iz(?:e|ed|es|ing|ation|ations))\b'

def prompt_for(path):
    m = re.match(r'r-([\d.]+)\.html$', path.name)
    course = {'greece': 'greek-syllabus.html', 'rome': 'roman-syllabus.html'}.get(path.parent.name)
    if not (m and course):
        return None
    pm = re.search(r'data-id="%s">.*?<pre>(.*?)</pre>' % re.escape(m.group(1)), (R / course).read_text(), re.S)
    return html.unescape(pm.group(1)) if pm else None

def capstone_for(path):
    """A module whose prompt asks for a "final examination" is a capstone: N questions in Parts, model answers, gaps, Carry forward."""
    pr = prompt_for(path) or ''
    if 'final examination' not in pr:
        return None
    n = re.search(r'(\d+)-question final examination', pr)
    return int(n.group(1)) if n else 40

def target_for(path):
    m = re.match(r'r-([\d.]+)\.html$', path.name)
    course = {'greece': 'greek-syllabus.html', 'rome': 'roman-syllabus.html'}.get(path.parent.name)
    if not (m and course):
        return None
    syl = (R / course).read_text()
    pm = re.search(r'data-id="%s">.*?<pre>(.*?)</pre>' % re.escape(m.group(1)), syl, re.S)
    t = re.search(r'about (\d+) words', html.unescape(pm.group(1))) if pm else None
    return int(t.group(1)) if t else None

class P(HTMLParser):
    def __init__(s):
        super().__init__(); s.stack = []; s.errs = []; s.tags = []
    def handle_starttag(s, tag, attrs):
        s.tags.append((tag, dict(attrs)))
        if tag not in ALLOWED: s.errs.append(f'disallowed <{tag}>')
        if 'style' in dict(attrs): s.errs.append(f'inline style on <{tag}>')
        if tag not in VOID: s.stack.append(tag)
    def handle_endtag(s, tag):
        if not s.stack or s.stack[-1] != tag:
            s.errs.append(f'unbalanced </{tag}> (open: {s.stack[-3:]})')
            if tag in s.stack:
                while s.stack and s.stack.pop() != tag: pass
        else:
            s.stack.pop()

def check_capstone(t, nq, hard, soft):
    """Capstone mode (logged in provenance artefacts): no word target, no Self-test; nq questions with model answers
    across the Parts, a gaps section with ten follow-up prompts, then Carry forward with 3 items."""
    h2 = re.findall(r'<h2>(.*?)</h2>', t)
    if h2[-2:] != ['Where the gaps will still be', 'Carry forward']:
        hard.append(f'capstone: last two h2 must be Where the gaps will still be, Carry forward (got {h2[-2:]})')
    if not h2 or not h2[0].startswith('How to sit'): soft.append('capstone: first section is not "How to sit this exam"')
    parts = [h for h in h2 if h.startswith('Part ')]
    if len(parts) < 4: hard.append(f'capstone: {len(parts)} Part sections (need A to D)')
    quizzes = re.findall(r'<ol class="quiz">(.*?)</ol>', t, re.S)
    nli = sum(len(re.findall(r'<li>', q)) for q in quizzes)
    nans = sum(len(re.findall(r'<details><summary>(?:Model answer|Answer)</summary><p>.*?</p></details></li>', q, re.S)) for q in quizzes)
    if nli != nq or nans != nq: hard.append(f'capstone: {nli} questions, {nans} well-formed model answers (need {nq}/{nq})')
    gaps = t.split('<h2>Where the gaps will still be</h2>')[-1].split('<h2>Carry forward</h2>')[0]
    if gaps.count('<pre class="tree">') != 10: soft.append(f'capstone: {gaps.count("<pre class=\"tree\">")} follow-up prompts in the gaps section (prompt asks for ten)')
    return len(h2) - 1


def check(path, target=None):
    t = path.read_text()
    hard, soft = [], []
    p = P(); p.feed(t); p.close()
    hard += p.errs
    if p.stack: hard.append(f'unclosed tags: {p.stack}')
    if re.search(r'<(style|script|html|head|body|h1)\b', t, re.I): hard.append('forbidden element')
    if not t.lstrip().startswith('<h2>'): hard.append('does not begin with <h2>')
    nq = capstone_for(path)
    if nq:
        body_h2 = check_capstone(t, nq, hard, soft)
        carry = re.search(r'<h2>Carry forward</h2>\s*<ol class="carry">(.*?)</ol>\s*$', t, re.S)
        if not carry or len(re.findall(r'<li>', carry.group(1))) != 3: hard.append('carry forward must have exactly 3 items, at the end')
        for tag, a in p.tags:
            c = a.get('class')
            if tag == 'div' and c != 'tbl': hard.append(f'div with class {c!r}')
            if tag == 'aside' and c != 'dispute': hard.append(f'aside with class {c!r}')
            if tag == 'pre' and c != 'tree': hard.append(f'pre with class {c!r}')
        n = len(re.sub(r'<[^>]+>', ' ', t).split())
        nd = len(re.findall(r'<aside class="dispute">', t))
        if t.count('—') > 3: soft.append(f'{t.count("—")} em dashes (house style uses colons and semicolons)')
        us = sorted(set(m.group(0) for m in re.finditer(US, re.sub(r'<[^>]+>', ' ', t), re.I)))
        if us: soft.append(f'possible US spellings: {us}')
        return n, nd, body_h2, hard, soft
    h2 = re.findall(r'<h2>(.*?)</h2>', t)
    if h2[-2:] != ['Self-test', 'Carry forward']: hard.append(f'last two h2 must be Self-test, Carry forward (got {h2[-2:]})')
    body_h2 = len(h2) - 2
    if not 6 <= body_h2 <= 10: soft.append(f'{body_h2} body sections (spec 6–10)')
    quiz = re.search(r'<h2>Self-test</h2>\s*<ol class="quiz">(.*?)</ol>\s*<h2>Carry forward</h2>', t, re.S)
    if not quiz: hard.append('quiz block malformed')
    else:
        q = quiz.group(1)
        nli = len(re.findall(r'<li>', q)); nd = len(re.findall(r'<details><summary>Answer</summary><p>.*?</p></details></li>', q, re.S))
        if nli != 10 or nd != 10: hard.append(f'self-test: {nli} items, {nd} well-formed answers (need 10/10)')
    carry = re.search(r'<h2>Carry forward</h2>\s*<ol class="carry">(.*?)</ol>\s*$', t, re.S)
    if not carry: hard.append('carry-forward block malformed or not at end')
    elif len(re.findall(r'<li>', carry.group(1))) != 3: hard.append('carry forward must have exactly 3 items')
    disputes = re.findall(r'<aside class="dispute">(.*?)</aside>', t, re.S)
    if len(disputes) < 3: hard.append(f'only {len(disputes)} dispute boxes')
    bad = [d[:40] for d in disputes if not d.startswith('<strong>Where sources disagree.</strong>')]
    if bad: hard.append(f'dispute boxes not starting with the required strong: {bad}')
    for tag, a in p.tags:
        if tag == 'table':
            pass
    if t.count('<table') != len(re.findall(r'<div class="tbl">\s*<table', t)): hard.append('table not wrapped in div.tbl')
    for tag, a in p.tags:
        c = a.get('class')
        if tag == 'div' and c != 'tbl': hard.append(f'div with class {c!r}')
        if tag == 'aside' and c != 'dispute': hard.append(f'aside with class {c!r}')
        if tag == 'pre' and c != 'tree': hard.append(f'pre with class {c!r}')
    body = re.split(r'<h2>\s*Self-test', t)[0]
    n = len(re.sub(r'<[^>]+>', ' ', body).split())
    if target:
        lo, hi = round(target * 0.9), round(target * 1.15)
        # Length is advisory (Pedro, 27 October 2026): the target is a goal, not a law; a topic takes the words it needs.
        if not lo <= n <= hi: soft.append(f'body {n} words against a target of {target} (guide {lo}–{hi}; advisory only)')
    us = sorted(set(m.group(0) for m in re.finditer(US, re.sub(r'<[^>]+>', ' ', t), re.I)))
    if us: soft.append(f'possible US spellings: {us}')
    if re.search(r'In this (report|module)|This report (will|covers)|we will (look|see)', t): soft.append('possible preamble')
    em = t.count('—')
    if em > 3: soft.append(f'{em} em dashes (house style uses colons and semicolons)')
    return n, len(disputes), body_h2, hard, soft

if __name__ == '__main__':
    args = sys.argv[1:]; tgt = None
    if args and args[0] == '--target': tgt = int(args[1]); args = args[2:]
    fail = False
    for a in args:
        path = pathlib.Path(a).resolve()
        target = tgt or target_for(path)
        n, nd, ns, hard, soft = check(path, target)
        status = 'OK' if not hard else 'FAIL'
        fail |= bool(hard)
        kind = f'capstone, {capstone_for(path)} questions' if capstone_for(path) else f'target {target}'
        print(f'{status} {path.name}: {n} words ({kind}), {ns} sections, {nd} disputes')
        for h in hard: print('  HARD', h)
        for s in soft: print('  soft', s)
    sys.exit(1 if fail else 0)
