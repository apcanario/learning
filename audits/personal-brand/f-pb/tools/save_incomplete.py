"""F-PB: file a run that returned INCOMPLETE (no web search) without marking the unit saved. save_incomplete.py <code> <tokens> <tools> <minutes>"""
import sys, json, shutil, pathlib, subprocess
code, tok, tools, mins = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), float(sys.argv[4])
ROOT = pathlib.Path('/home/claude/learning'); FP = ROOT/'audits/personal-brand/f-pb'
d = FP/f'{code}-run1-no-search'; d.mkdir(exist_ok=True)
for f in ('audit.md','errata.json','claims.json','stats.json'):
    p = pathlib.Path(f'/home/claude/fpb/{code}/out/{f}')
    if p.exists(): shutil.copy(p, d/f)
u = json.loads((FP/'usage.json').read_text())
u['units'][f'{code} (run 1, no web search)'] = dict(tokens=tok, tool_uses=tools, minutes=mins, model_stated='claude-fable-5-2', note="INCOMPLETE: the turn's WebSearch budget (200 calls, shared by every agent) was used up; sources not opened; internal checks only")
(FP/'usage.json').write_text(json.dumps(u, indent=1)+'\n')
pf = ROOT/'audits/personal-brand/F-PB-progress.md'; t = pf.read_text()
assert t.count(f'- {code}: pending\n') == 1
pf.write_text(t.replace(f'- {code}: pending\n', f"- {code}: pending (run 1 returned without its source check: the turn's web search budget was used up; its report is saved in `f-pb/{code}-run1-no-search/`; to re-run with search from its recorded sample)\n"))
subprocess.run(['git','-C',str(ROOT),'add','-A'],check=True)
subprocess.run(['git','-C',str(ROOT),'commit','-q','-m',f"F-PB: {code} run 1 saved as incomplete (no web search: the turn's search budget was used up); {code} stays pending ({tok} tokens, {tools} tool uses, {mins:g} min)\n\nCo-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>\nClaude-Session: https://claude.ai/code/session_01KMmgQyKuvCKpHpSB9xzQYA"],check=True)
print(code, 'push', subprocess.run(['git','-C',str(ROOT),'-c','push.negotiate=true','push','-q','origin','main'],capture_output=True,text=True).returncode)
