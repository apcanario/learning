"""F-PB checkpoint (c): apply one unit's errata as exact replacements, add the dated note, set the progress line, commit, push.
usage: apply.py <code> [--check]   (code PB1..DD-PB2; 'A4:<code>' applies Audit 4's errata for that unit)
Every erratum is validated before anything is written: kind erratum, Current on one line and occurring once, Fix different,
Basis present. An erratum that fails validation is not applied and is listed for syllabus-flags / Corrections. If a
replacement fails after validation the unit file is reverted with git checkout."""
import sys, json, pathlib, subprocess, re
ROOT = pathlib.Path('/home/claude/learning'); FP = ROOT / 'audits/personal-brand/f-pb'
arg = sys.argv[1]; check = '--check' in sys.argv
a4 = arg.startswith('A4:'); code = arg.split(':')[-1]
AUD = {'PB1':1,'PB2':1,'PB3':1,'PB4':1,'PB5':2,'PB6':2,'PB7':2,'PB8':2,'PB9':3,'PB10':3,'DD-PB1':3,'DD-PB2':3}
n = 4 if a4 else AUD[code]
src = FP / ('audit-4' if a4 else code) / 'errata.json'
items = [x for x in json.loads(src.read_text()) if x.get('unit') == code]
unit = next(f for f in (ROOT / 'courses/personal-brand').glob('*.md') if f.name.startswith(code + '-'))
skip = set(json.loads((FP / 'skip.json').read_text())) if (FP / 'skip.json').exists() else set()
t = unit.read_text(); ok, bad, flags = [], [], []
for x in items:
    cur, fix = x.get('current', ''), x.get('fix', '')
    if x.get('kind') != 'erratum': flags.append(x); continue
    why = None
    if x['id'] in skip: why = 'held by the chat (see skip.json)'
    elif not cur or t.count(cur) != 1: why = f'Current occurs {t.count(cur) if cur else 0} times'
    elif '\n' in cur: why = 'Current spans lines'
    elif cur == fix or not fix.strip(): why = 'no change in Fix'
    elif not x.get('basis'): why = 'no basis'
    (bad if why else ok).append((x, why))
print(f'{arg}: {len(ok)} to apply, {len(bad)} not applied, {len(flags)} flags')
for x, why in bad: print('  NOT', x['id'], why)
for x, _ in ok: print('  ', x['id'], x.get('severity'), '| fig' if x.get('figure') else '', '\n     -', x['current'][:230].replace('\n', '\\n'), '\n     +', x['fix'][:330].replace('\n', '\\n'))
for x in flags: print('  FLAG', x['id'], (x.get('fix') or x.get('basis') or '')[:200].replace('\n', ' '))
if check: sys.exit()
res = dict(applied=[x['id'] for x, _ in ok], not_applied=[dict(id=x['id'], why=w) for x, w in bad], flags=[x['id'] for x in flags], figures=[x['id'] for x, _ in ok if x.get('figure')])
try:
    # apply in the order given; re-count before each, since an earlier fix may touch a later Current
    for x, _ in ok:
        assert t.count(x['current']) == 1, x['id'] + ' no longer occurs once'
        t = t.replace(x['current'], x['fix'])
    if ok:
        ids = ', '.join(x['id'] for x, _ in ok)
        what = ' '.join(f"{x['id']} ({x.get('section', '').strip()}: {x.get('severity')})" for x, _ in ok)
        kind = 'the final audit, a full read of the course' if a4 else 'stratified-sample audit'
        t = t.rstrip('\n') + f"\n\nErratum 15 Nov 2026, Audit {n} ({kind}; Fable 5.2, row F-PB): {len(ok)} exact replacement{'s' if len(ok) != 1 else ''} applied, {ids}; each is quoted with its source in `audits/personal-brand/audit-{n}.md`.\n"
        unit.write_text(t)
except Exception as e:
    subprocess.run(['git', '-C', str(ROOT), 'checkout', '--', str(unit)], check=True)
    res = dict(applied=[], not_applied=[dict(id=x['id'], why=f'unit reverted: {e}') for x, _ in ok + bad], flags=res['flags'], figures=[])
    ok = []
ap = FP / 'applied.json'; A = json.loads(ap.read_text()) if ap.exists() else {}
A[arg] = res; ap.write_text(json.dumps(A, indent=1) + '\n')
pf = ROOT / 'audits/personal-brand/F-PB-progress.md'; p = pf.read_text()
state = f"errata applied ({len(res['applied'])} applied, {len(res['not_applied'])} not applied, {len(res['flags'])} flags)" if res['applied'] or not res['not_applied'] else 'errata not applied: ' + '; '.join(f"{b['id']} {b['why']}" for b in res['not_applied'])
if a4:
    p = p.rstrip('\n') + f"\n- Audit 4 errata, {code}: {state}\n"
else:
    assert p.count(f'- {code}: report saved') == 1, 'progress line not at report saved'
    p = p.replace(f'- {code}: report saved', f'- {code}: {state}')
pf.write_text(p)
msg = f"F-PB: {arg} errata, Audit {n}: {len(res['applied'])} applied ({', '.join(res['applied']) or 'none'}), {len(res['not_applied'])} not applied, {len(res['flags'])} flags\n\nCo-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>\nClaude-Session: https://claude.ai/code/session_01KMmgQyNZfTSHF35S2ivXpn"
subprocess.run(['git', '-C', str(ROOT), 'add', '-A'], check=True)
subprocess.run(['git', '-C', str(ROOT), 'commit', '-q', '-m', msg], check=True)
r = subprocess.run(['git', '-C', str(ROOT), '-c', 'push.negotiate=true', 'push', '-q', 'origin', 'main'], capture_output=True, text=True)
print('committed; push rc', r.returncode)
