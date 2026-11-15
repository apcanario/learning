"""F-PB step 4: build audits/personal-brand/audit-1.md to audit-4.md from f-pb/<code>/audit.md, one front matter each."""
import json, pathlib
ROOT = pathlib.Path('/home/claude/learning'); FP = ROOT / 'audits/personal-brand/f-pb'
CODES = ['PB1','PB2','PB3','PB4','PB5','PB6','PB7','PB8','PB9','PB10','DD-PB1','DD-PB2']
S1 = 'https://claude.ai/code/session_01KMmgQyKuvCKpHpSB9xzQYA'; S2 = 'https://claude.ai/code/session_01KMmgQyNZfTSHF35S2ivXpn'
def stats(c):
    try: return json.loads((FP / c / 'stats.json').read_text())
    except Exception: return {}
for n in (1, 2, 3):
    cs = CODES[4*(n-1):4*n]
    have = [c for c in cs if (FP / c / 'audit.md').exists()]
    v = ' · '.join(f"{c} {str(stats(c).get('verdict','pending'))[:80]}" for c in cs)
    date = '2026-11-15' if n == 3 else '2026-11-14'
    chat = (f'one fresh Fable agent per unit, isolated on its packet, in session {S2} (row F-PB part 2; the four units\' first runs, without web search, in session {S1}, kept in `f-pb/<code>-run1-no-search/`)' if n == 3
            else f'one fresh Fable agent per unit, isolated on its packet, in session {S1} (row F-PB part 1)')
    fm = f"---\naudit: stratified-sample audit (Audit {n})\nunits: {', '.join(cs)}\ncourse: personal-brand · PB · Building a Personal Brand on Instagram and YouTube\nmodel: Fable 5.2 (claude-fable-5-2; accepted by Pedro for row F-PB, 14 Nov 2026), search on\ndate: {date}\nchat: {chat}\nverdicts: {v}\n---\n\n# Audit {n} · PB · {', '.join(cs)}\n\nBuilt by script (`f-pb/tools/build_audits.py`) from each agent's `out/audit.md`, saved verbatim under `audits/personal-brand/f-pb/<code>/` before any erratum was applied. Errata applied by `f-pb/tools/apply.py`; what was applied, held and flagged is in `f-pb/applied.json`.\n"
    body = ''.join(f"\n---\n\n<!-- {c}: f-pb/{c}/audit.md, verbatim -->\n\n" + (FP / c / 'audit.md').read_text().rstrip('\n') + '\n' for c in have)
    (ROOT / f'audits/personal-brand/audit-{n}.md').write_text(fm + body)
s4 = FP / 'audit-4/audit.md'
fm = f"---\naudit: final audit (Audit 4), a full read of the course against its goal\nunits: {', '.join(CODES)}\ncourse: personal-brand · PB · Building a Personal Brand on Instagram and YouTube\nmodel: Fable 5.2 (claude-fable-5-2; accepted by Pedro for row F-PB, 14 Nov 2026); no source re-checked\ndate: 2026-11-14\nchat: one fresh Fable agent with the twelve units, the briefs, the goal and outcomes and the register, in session {S1} (row F-PB part 1)\nverdicts: see the report's verdict on the course\n---\n\n"
(ROOT / 'audits/personal-brand/audit-4.md').write_text(fm + s4.read_text())
print('built audit-1..4')
