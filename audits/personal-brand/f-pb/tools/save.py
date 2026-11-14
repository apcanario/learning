"""F-PB checkpoint (b): save one auditor's report into the repo, record its usage, set its progress line, commit, push.
usage: save.py <code> <tokens> <tool_uses> <minutes> [note]"""
import sys, json, shutil, pathlib, subprocess, re
ROOT = pathlib.Path('/home/claude/learning'); PK = pathlib.Path('/home/claude/fpb')
code, tokens, tools, minutes = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), float(sys.argv[4])
note = sys.argv[5] if len(sys.argv) > 5 else ''
src = PK / ('A4' if code == 'Audit 4' else code) / 'out'
dst = ROOT / 'audits/personal-brand/f-pb' / ('audit-4' if code == 'Audit 4' else code); dst.mkdir(parents=True, exist_ok=True)
got = []
for f in ('audit.md', 'errata.json', 'claims.json', 'stats.json'):
    if (src / f).exists(): shutil.copy(src / f, dst / f); got.append(f)
assert 'audit.md' in got, 'no audit.md'
first = (dst / 'audit.md').read_text().splitlines()[0]
m = re.search(r'claude-[a-z0-9-]+', first)
model = m.group(0) if m else first
up = ROOT / 'audits/personal-brand/f-pb/usage.json'
u = json.loads(up.read_text()); u['units'][code] = dict(tokens=tokens, tool_uses=tools, minutes=minutes, model_stated=model, files=got, note=note)
up.write_text(json.dumps(u, indent=1) + '\n')
pf = ROOT / 'audits/personal-brand/F-PB-progress.md'
t = pf.read_text(); n = t.count(f'- {code}: pending')
assert n == 1 or f'- {code}: report saved' in t, 'progress line'
pf.write_text(t.replace(f'- {code}: pending', f'- {code}: report saved'))
verdict = ''
try: verdict = json.loads((dst / 'stats.json').read_text()).get('verdict', '')
except Exception: pass
msg = f"F-PB: {code} report saved ({model}; {verdict}; {tokens} tokens, {tools} tool uses, {minutes:g} min)\n\nCo-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>\nClaude-Session: https://claude.ai/code/session_01KMmgQyKuvCKpHpSB9xzQYA"
subprocess.run(['git', '-C', str(ROOT), 'add', '-A'], check=True)
subprocess.run(['git', '-C', str(ROOT), 'commit', '-q', '-m', msg], check=True)
r = subprocess.run(['git', '-C', str(ROOT), '-c', 'push.negotiate=true', 'push', '-q', 'origin', 'main'], capture_output=True, text=True)
print(code, 'saved', got, '| model:', model, '| push rc', r.returncode, r.stderr.strip()[-200:])
