"""Register written reports: copy title and prompt from the course syllabus into its prompts index and record provenance.

python3 register.py rome "Opus 5.5" 0.1 0.2 1.4
Refuses any id whose vault file (courses/<course>/<id>-<slug>.md, P71-3) is missing or fails check.py.
P91 (4 Nov 2026): it also records the day it registers a report in provenance.json's `written` map (the date What's new
and the course's "How it was built" page show), unless the report already has one; `--date YYYY-MM-DD` gives another day.
"""
import sys, json, re, html, pathlib
from courses import HISTORY as COURSES, path as cpath, provenance, save_provenance
from check import check, target_for
import vault

R = pathlib.Path(__file__).resolve().parent
import datetime
args = sys.argv[1:]
day = datetime.date.today().isoformat()
if '--date' in args:
    k = args.index('--date'); day = datetime.date.fromisoformat(args[k + 1]).isoformat(); del args[k:k + 2]
cid, model, ids = args[0], args[1], args[2:]
c = next(x for x in COURSES if x['id'] == cid)
syl = cpath(c, 'syllabus').read_text()
idx_path = cpath(c, 'prompts'); idx = json.load(open(idx_path))
prov = provenance(); prov.setdefault(cid, {})   # S-DEC5: the course's own provenance file and kit/provenance.json
order = re.findall(r'data-id="([\d.]+)"', syl)
for i in ids:
    f = vault.report_path(c, i)
    if not f:
        sys.exit(f'{i}: no file {c["vault"]}/{i}-<slug>.md in the vault')
    n, nd, ns, hard, soft = check(f, target_for(f))
    if hard:
        sys.exit(f'{i}: fails check.py: {hard}')
    m = re.search(r'data-id="%s">.*?<h3>(.*?)</h3>.*?<pre>(.*?)</pre>' % re.escape(i), syl, re.S)
    idx[i] = {'title': html.unescape(m.group(1)), 'prompt': html.unescape(m.group(2))}
    prov[cid][i] = model
    prov.setdefault('written', {}).setdefault(cid, {}).setdefault(i, day)
    print(f'registered {cid} {i}: {n} words, {model}')
idx = {k: idx[k] for k in order if k in idx}
prov[cid] = {k: prov[cid][k] for k in order if k in prov[cid]}
w = prov.setdefault('written', {}).setdefault(cid, {}); prov['written'][cid] = {k: w[k] for k in order if k in w}
json.dump(idx, open(idx_path, 'w'), indent=1, ensure_ascii=False)
save_provenance(prov)
