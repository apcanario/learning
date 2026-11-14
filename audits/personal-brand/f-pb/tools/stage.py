"""F-PB: stage one packet folder per unit and one for Audit 4, by script."""
import sys, re, shutil, pathlib, importlib.util
ROOT = pathlib.Path('/home/claude/learning'); OUT = pathlib.Path('/home/claude/fpb')
sys.path.insert(0, str(ROOT / 'kit'))
import mdcourse
spec = importlib.util.spec_from_file_location('pbhub', ROOT / 'generator/data/personal-brand/hub.py')
d = importlib.util.module_from_spec(spec); spec.loader.exec_module(d)
sc = d.COURSES[0]
units = {u[0]: u for u in sc['units']}
vault = {re.match(r'((?:DD-)?[A-Z]+\d+)-', f.name).group(1): f for f in sorted((ROOT / 'courses/personal-brand').glob('*.md'))}
CODES = ['PB1','PB2','PB3','PB4','PB5','PB6','PB7','PB8','PB9','PB10','DD-PB1','DD-PB2']
assert set(CODES) == set(vault) == set(units), (set(vault), set(units))
AUDIT = {**{c: 1 for c in CODES[:4]}, **{c: 2 for c in CODES[4:8]}, **{c: 3 for c in CODES[8:]}}
src = (ROOT / 'docs/sourcing-standard.md').read_text()
p1 = src[src.index('## Part 1'):src.index('## Part 2')]; p5 = src[src.index('## Part 5'):src.index('## Part 6')]
method = (ROOT / 'docs/method.md').read_text()
sec = method[method.index('### How: the stratified-sample audit'):]
verb = re.search(r'```\n(.*?)\n```', sec, re.S).group(1)
assert verb.startswith('You are auditing four units')
TPL = pathlib.Path('/home/claude/fpb-tools/auditor-prompt.md').read_text()
for c in CODES:
    p = OUT / c
    if (p / 'out').exists():   # resume: never wipe working files
        print('kept', c); continue
    (p / 'out').mkdir(parents=True); (p / 'others').mkdir()
    shutil.copy(vault[c], p / 'unit.md')
    (p / 'brief.txt').write_text(mdcourse.open_brief(d, sc, units[c]))
    (p / 'sourcing-parts-1-and-5.md').write_text(p1 + '\n' + p5)
    shutil.copy(ROOT / 'generator/data/personal-brand/case-facts.md', p / 'case-facts.md')
    shutil.copy(ROOT / f'audits/personal-brand/fresh-check-{c}.md', p / f'fresh-check-{c}.md')
    for o in CODES:
        if o != c: shutil.copy(vault[o], p / 'others' / vault[o].name)
    named = verb.replace('{list the four unit codes and their vault paths}', f'{c} · {units[c][1] if isinstance(units[c][1], str) else c}, `courses/personal-brand/{vault[c].name}` (in your folder as `unit.md`); this agent audits this one unit of the four of Audit {AUDIT[c]}, and the other three are each audited by their own agent')
    (p / 'PROMPT.md').write_text(TPL.replace('{VERBATIM}', named).replace('{CODE}', c).replace('{FOLDER}', str(p)).replace('{AUDIT}', str(AUDIT[c])).replace('{SEARCH}', dict((x[0], x[2]) for x in d.ORDER)[c]))
    print('staged', c, sum(1 for _ in p.rglob('*') if _.is_file()), 'files')
# Audit 4
p = OUT / 'A4'
if not (p / 'out').exists():
    (p / 'out').mkdir(parents=True); (p / 'units').mkdir(); (p / 'briefs').mkdir()
    for c in CODES:
        shutil.copy(vault[c], p / 'units' / vault[c].name)
        (p / 'briefs' / f'{c}-brief.txt').write_text(mdcourse.open_brief(d, sc, units[c]))
    shutil.copy(ROOT / 'generator/data/personal-brand/case-facts.md', p / 'case-facts.md')
    (p / 'course-goal-and-outcomes.md').write_text(f"# {d.NAME_PB}\n\n## Goal\n\n{sc['goal']}\n\n## Outcomes\n\n{sc['outcomes']}\n\n## Intro\n\n{sc['intro']}\n\n## Course note\n\n{d.COURSE_NOTE}\n\n## Preamble shared by every brief (holds the persona)\n\n{d.PRE.replace('{GOAL}', sc['goal'])}\n")
    (p / 'sourcing-parts-1-and-5.md').write_text(p1 + '\n' + p5)
    (p / 'PROMPT.md').write_text(pathlib.Path('/home/claude/fpb-tools/audit4-prompt.md').read_text().replace('{FOLDER}', str(p)))
    print('staged A4')
