"""F-PB step 5: build audits/fable-stage-assessment-2026-11.md from f-pb/ (usage.json, each unit's stats.json and claims.json,
applied.json) and the vault's word and section counts. Rebuildable at any point; says PARTIAL while a unit is pending."""
import json, re, pathlib, collections, statistics as st
ROOT = pathlib.Path('/home/claude/learning'); FP = ROOT/'audits/personal-brand/f-pb'
CODES = ['PB1','PB2','PB3','PB4','PB5','PB6','PB7','PB8','PB9','PB10','DD-PB1','DD-PB2']
AUD = {c: 1 + i//4 for i, c in enumerate(CODES)}
SEARCH = {'PB1':'on','PB2':'off','PB3':'on','PB4':'off','PB5':'off','PB6':'on','PB7':'on','PB8':'on','PB9':'on','PB10':'off','DD-PB1':'on','DD-PB2':'off'}
U = json.loads((FP/'usage.json').read_text())['units']
AP = json.loads((FP/'applied.json').read_text()) if (FP/'applied.json').exists() else {}
def J(p):
    try: return json.loads(p.read_text())
    except Exception: return None
def wc(f): t = f.read_text(); return len(t.split()), len(re.findall(r'^## ', t, re.M))
rows, claims = [], []
for c in CODES:
    s, cl, u = J(FP/c/'stats.json'), J(FP/c/'claims.json'), U.get(c)
    if s and u and u.get('tokens'):
        cl = cl or []
        v = collections.Counter(x.get('verdict') for x in cl)
        r = dict(code=c, audit=AUD[c], search=SEARCH[c], words=s.get('words'), sections=s.get('sections'), cited=s.get('cited_claims_in_unit'),
                 sampled=sum(1 for x in cl if x.get('sampled')) or s.get('claims_sampled'), checked=len(cl) or s.get('claims_checked_total'),
                 fail=v.get('FAIL', 0), fail_s=sum(1 for x in cl if x.get('sampled') and x.get('verdict') == 'FAIL'), stale=v.get('STALE', 0), unv=v.get('unverifiable', 0),
                 tokens=u['tokens'], tools=u['tool_uses'], minutes=u['minutes'], searches=s.get('web_searches'), fetches=s.get('web_fetches'), verdict=str(s.get('verdict', ''))[:60],
                 applied=len(AP.get(c, {}).get('applied', [])), held=len(AP.get(c, {}).get('not_applied', [])), flags=len(AP.get(c, {}).get('flags', [])))
        rows.append(r)
        for x in cl: claims.append(dict(x, unit=c, search=SEARCH[c]))
done = [r['code'] for r in rows]; pending = [c for c in CODES if c not in done]
extra = {k: v for k, v in U.items() if k not in CODES}
tot = lambda k, rs=rows: sum(r[k] or 0 for r in rs)
def line(r): return f"| {r['code']} | {r['audit']} | {r['search']} | {r['words']:,} | {r['sections']} | {r['sampled']} | {r['checked']} | {r['fail']} ({r['fail_s']}) | {r['stale']} | {r['unv']} | {r['tokens']:,} | {r['tools']} | {r['minutes']:g} | {r['tokens']//max(r['checked'],1):,} | {r['applied']} / {r['held']} / {r['flags']} |"
out = []
W = out.append
W('# Fable stage: cost assessment after row F-PB (November 2026)\n')
W(f"Built by `audits/personal-brand/f-pb/tools/assess.py` from each auditor's completion notice (`f-pb/usage.json`) and its report files (`f-pb/<code>/stats.json`, `claims.json`). {'**PARTIAL: ' + str(len(done)) + ' of 12 unit audits are in; pending: ' + ', '.join(pending) + '.**' if pending else 'All twelve unit audits are in.'}\n")
W("**Meter readings.** At start: All models __% · Fable only __% (the prompt's first line arrived unfilled; Pedro had not entered the readings). After: to be read by Pedro from Settings > Usage and set against the token totals below.\n")
W("**Model.** Every auditor stated `claude-fable-5-2` (Fable 5.2, accepted by Pedro for this row on 14 Nov 2026). The chat that staged, saved, applied and recorded also ran as claude-fable-5-2; its own tokens are **not measured** here (no completion notice exists for the chat itself), and it carried each returned report in its context, so its share is not small.\n")
W('## 1 · Per unit\n')
W('| Unit | Audit | Search | Words | Sections | Sampled | Checked in all | FAIL (in sample) | STALE | Unverifiable | Tokens | Tool uses | Minutes | Tokens per claim checked | Errata applied / held / flags |\n|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|')
for r in rows: W(line(r))
W('\n## 2 · Totals\n')
W('| | Units | Words | Sampled | Checked | FAIL | STALE | Unverifiable | Tokens | Tool uses | Agent minutes | Tokens per claim checked | Tokens per 1,000 words |\n|---|---|---|---|---|---|---|---|---|---|---|---|---|')
def trow(name, rs):
    if not rs: return f'| {name} | 0 | | | | | | | | | | | |'
    return f"| {name} | {len(rs)} | {tot('words', rs):,} | {tot('sampled', rs)} | {tot('checked', rs)} | {tot('fail', rs)} | {tot('stale', rs)} | {tot('unv', rs)} | {tot('tokens', rs):,} | {tot('tools', rs)} | {tot('minutes', rs):.1f} | {tot('tokens', rs)//max(tot('checked', rs),1):,} | {1000*tot('tokens', rs)//max(tot('words', rs),1):,} |"
for n in (1, 2, 3): W(trow(f'Audit {n}', [r for r in rows if r['audit'] == n]))
W(trow('Unit audits, complete runs', rows))
ex_tok = sum(v.get('tokens') or 0 for v in extra.values())
for k, v in extra.items(): W(f"| {k} | | | | | | | | {v.get('tokens') or 0:,} | {v.get('tool_uses') or ''} | {v.get('minutes') or ''} | | |")
W(f"| **Row, all agents measured** | | | | | | | | **{tot('tokens') + ex_tok:,}** | | | | |")
W("\nThe chat's own share is unmeasured. Runs marked \"no web search\" spent their tokens reading and checking inside the folder only: the turn's web search budget (200 WebSearch calls per turn, shared by every agent) was used up by the first eight auditors, which is itself a finding for the planning of stage 5 (section 5).\n")
if rows:
    tpw = tot('tokens')/tot('words'); tpc = tot('tokens')/max(tot('checked'), 1); tpu = tot('tokens')/len(rows); spu = st.mean([r['searches'] or 0 for r in rows])
    lo = min(r['tokens']/r['words'] for r in rows); hi = max(r['tokens']/r['words'] for r in rows)
    W('## 3 · Projections\n')
    W(f"Rates from the {len(rows)} complete runs: {tpu:,.0f} tokens per unit (range {min(r['tokens'] for r in rows):,} to {max(r['tokens'] for r in rows):,}); {1000*tpw:,.0f} tokens per 1,000 words (range {1000*lo:,.0f} to {1000*hi:,.0f}); {tpc:,.0f} tokens per claim checked; {spu:.0f} web searches per unit. Tokens varied little with length (the largest unit cost {max(r['tokens'] for r in rows)/min(r['tokens'] for r in rows):.2f} times the smallest for {max(r['words'] for r in rows)/min(r['words'] for r in rows):.2f} times the words), so each projection gives a flat per-unit figure and a per-word figure; the truth should lie between them.\n")
    W('**(a) Sample audits still owed.**\n')
    W('| Set | Units | Words | Sections | Tokens at the per-unit rate | Tokens at the per-word rate | Searches at the per-unit rate |\n|---|---|---|---|---|---|---|')
    def setrow(name, files):
        ws = [wc(f) for f in files]; w = sum(a for a, b in ws); s = sum(b for a, b in ws)
        W(f"| {name} | {len(files)} | {w:,} | {s} | {tpu*len(files):,.0f} | {tpw*w:,.0f} | {spu*len(files):.0f} |"); return len(files), w
    g = lambda d, pats: sorted(f for f in (ROOT/'courses'/d).glob('*.md') if any(f.name.startswith(p + '-') for p in pats))
    setrow("Course B, seven unaudited (B5, B6, B7, B8, DD-B1, DD-B2, DD-B3)", g('brand-ai', ['B5','B6','B7','B8','DD-B1','DD-B2','DD-B3']))
    setrow("Course A, seven unaudited (A3, A4, A5, A7, A8, DD-A1, DD-A2)", g('brand-ai', ['A3','A4','A5','A7','A8','DD-A1','DD-A2']))
    setrow("User Experience, fifteen", sorted((ROOT/'courses/ux').glob('*.md')))
    rome = [f for f in sorted((ROOT/'courses/rome').glob('*.md')) if re.match(r'(11\.[3-8]|12\.[1-8]|13\.[3-8])-', f.name)]
    setrow("Rome, twenty flagged modules (11.3 to 11.8, 12.1 to 12.8, 13.3 to 13.8)", rome)
    W("\nCaveats: the private courses' units are of different lengths and source types than PB's; Rome's modules cite ancient texts and scholarship, where a claim is checked against a book or a passage, not a web page, and their full audit is the kit's scorecard, not this procedure, so the Rome line is the least reliable. Each set also needs its chat (staging, saving, applying, records), unmeasured here.\n")
    cited = {r['code']: r['cited'] for r in rows}
    for k in pending:
        s = J(FP/f'{k}-run1-no-search'/'stats.json')
        if s and s.get('cited_claims_in_unit'): cited[k] = s['cited_claims_in_unit']
    nc = sum(v or 0 for v in cited.values())
    ns = [v['tokens'] for k, v in extra.items() if 'no web search' in k and v.get('tokens')]
    upper = nc*tpc
    W(f"**(b) A full Fable fresh check of PB's twelve units.** The reports counted {nc:,} cited claims in {len(cited)} of the 12 units ({', '.join(f'{k} {v}' for k, v in cited.items())}). Upper estimate, at the average of {tpc:,.0f} tokens per claim checked: about {upper:,.0f} tokens{'' if len(cited) == 12 else ' for those units'}. That average carries each agent's fixed cost of reading the unit, its packet and the other eleven units' pointers, so it overstates.")
    if ns:
        fixed = st.mean(ns); marg = (tpu - fixed)/(tot('checked')/len(rows)); est = sum(fixed + marg*(v or 0) for v in cited.values())
        W(f"\nA closer estimate separates the two costs. The {len(ns)} runs that had no web search still cost {min(ns):,} to {max(ns):,} tokens each (mean {fixed:,.0f}): that is the cost of reading and of the internal checks (arithmetic, pointers, the register, figures, the deliverable). The complete runs averaged {tpu:,.0f} tokens for {tot('checked')/len(rows):.0f} claims checked, so opening sources cost about {marg:,.0f} tokens per claim on top. On that split a full check of the {len(cited)} counted units is about {est:,.0f} tokens ({fixed:,.0f} + {marg:,.0f} × its cited claims, per unit), roughly {est/(tpu*len(cited)):.1f} times their sample audits. The no-search runs did more internal checking than a searching run would, so the fixed part is somewhat overstated and the per-claim part understated; the true figure lies between the two estimates, nearer the lower.")
    W(f"\nSearches are the binding limit, not tokens: at the sample's {tot('searches')/max(tot('checked'),1):.2f} searches per claim checked, a full check of {nc:,} claims needs about {nc*tot('searches')/max(tot('checked'),1):,.0f} web searches, against a budget of 200 per turn shared by every agent in it.\n")
    W('## 4 · What the sample found, against what the Opus fresh checks had fixed\n')
    W('| Unit | Search | Checked | FAIL | per 100 | STALE | Unverifiable | Opus fresh check (verdict line of its report) |\n|---|---|---|---|---|---|---|---|')
    for r in rows:
        fc = (ROOT/f"audits/personal-brand/fresh-check-{r['code']}.md").read_text()
        m = re.search(r'^verdict:\s*(.+)$', fc, re.M)
        W(f"| {r['code']} | {r['search']} | {r['checked']} | {r['fail']} | {100*r['fail']/max(r['checked'],1):.1f} | {r['stale']} | {r['unv']} | {(m.group(1) if m else '')[:110]} |")
    def strat(name, key):
        W(f'\n| {name} | Checked | FAIL | per 100 | STALE | Unverifiable |\n|---|---|---|---|---|---|')
        g = collections.defaultdict(list)
        for x in claims: g[key(x)].append(x)
        for k in sorted(g, key=str):
            v = collections.Counter(x.get('verdict') for x in g[k]); n = len(g[k])
            W(f"| {k} | {n} | {v.get('FAIL',0)} | {100*v.get('FAIL',0)/n:.1f} | {v.get('STALE',0)} | {v.get('unverifiable',0)} |")
    strat('Search flag', lambda x: x['search']); strat('Claim kind', lambda x: x.get('kind')); strat('Sampled or also checked', lambda x: 'sampled' if x.get('sampled') else 'also checked')
    W('')
inc = pathlib.Path('/home/claude/fpb-tools/assessment-text.md')
W(inc.read_text() if inc.exists() else '## 5 · Reading and recommendation\n\nTo be written when the reports are in.\n')
(ROOT/'audits/fable-stage-assessment-2026-11.md').write_text('\n'.join(out) + '\n')
print('written;', len(done), 'units;', 'pending', pending)
