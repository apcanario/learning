"""F-PB part 2: apply the chat-worked held errata (f-pb/chat/errata.json) one unit at a time, commit, push."""
import json, pathlib, subprocess, sys
ROOT = pathlib.Path('/home/claude/learning'); FP = ROOT / 'audits/personal-brand/f-pb'
E = json.loads((FP / 'chat/errata.json').read_text())
for code in sys.argv[1:]:
    unit = next(f for f in (ROOT / 'courses/personal-brand').glob('*.md') if f.name.startswith(code + '-'))
    t = unit.read_text(); A0 = json.loads((FP / 'applied.json').read_text()).get('chat:' + code, {}).get('applied', []); items = [x for x in E if x['unit'] == code and x['id'] not in A0]
    for x in items:
        assert t.count(x['current']) == 1, x['id']; t = t.replace(x['current'], x['fix'])
    ids = ', '.join(f"{x['id']} ({x['from_']})" for x in items)
    t = t.rstrip('\n') + f"\n\nErratum 15 Nov 2026, held errata of Audits 1 to 4 worked by the chat (Opus 5.5, row F-PB part 2, each checked at source): {len(items)} exact replacement{'s' if len(items)!=1 else ''} applied, {ids}; listed in `audits/personal-brand/f-pb/chat/errata.json`.\n"
    unit.write_text(t)
    A = json.loads((FP / 'applied.json').read_text()); A['chat:' + code] = dict(applied=A0 + [x['id'] for x in items], not_applied=[], flags=[], figures=[x['id'] for x in items if x.get('figure')])
    (FP / 'applied.json').write_text(json.dumps(A, indent=1) + '\n')
    pf = ROOT / 'audits/personal-brand/F-PB-progress.md'
    pf.write_text(pf.read_text().rstrip('\n') + f"\n- Held errata worked by the chat, {code}: errata applied ({len(items)} applied: {ids})\n")
    msg = f"F-PB: {code} held errata worked by the chat: {ids}\n\nCo-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>\nClaude-Session: https://claude.ai/code/session_01KMmgQyNZfTSHF35S2ivXpn"
    subprocess.run(['git', '-C', str(ROOT), 'add', '-A'], check=True)
    subprocess.run(['git', '-C', str(ROOT), 'commit', '-q', '-m', msg], check=True)
    r = subprocess.run(['git', '-C', str(ROOT), '-c', 'push.negotiate=true', 'push', '-q', 'origin', 'main'], capture_output=True, text=True)
    print(code, len(items), 'applied; push rc', r.returncode, r.stderr[-200:])
