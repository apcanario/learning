"""Register written reports: copy title and prompt from the course syllabus into its prompts index and record provenance.

python3 register.py rome "Opus 5.5" 0.1 0.2 1.4
Refuses any id whose fragment is missing or fails check.py.
"""
import sys, json, re, html, pathlib
from courses import HISTORY as COURSES
from check import check, target_for

R = pathlib.Path(__file__).resolve().parent
cid, model, ids = sys.argv[1], sys.argv[2], sys.argv[3:]
c = next(x for x in COURSES if x['id'] == cid)
syl = (R / c['syllabus']).read_text()
idx_path = R / c['prompts']; idx = json.load(open(idx_path))
prov = json.load(open(R / 'provenance.json')); prov.setdefault(cid, {})
order = re.findall(r'data-id="([\d.]+)"', syl)
for i in ids:
    f = R / c['frags'] / f'r-{i}.html'
    n, nd, ns, hard, soft = check(f, target_for(f))
    if hard:
        sys.exit(f'{i}: fails check.py: {hard}')
    m = re.search(r'data-id="%s">.*?<h3>(.*?)</h3>.*?<pre>(.*?)</pre>' % re.escape(i), syl, re.S)
    idx[i] = {'title': html.unescape(m.group(1)), 'prompt': html.unescape(m.group(2))}
    prov[cid][i] = model
    print(f'registered {cid} {i}: {n} words, {model}')
idx = {k: idx[k] for k in order if k in idx}
prov[cid] = {k: prov[cid][k] for k in order if k in prov[cid]}
json.dump(idx, open(idx_path, 'w'), indent=1, ensure_ascii=False)
json.dump(prov, open(R / 'provenance.json', 'w'), indent=1, ensure_ascii=False)
from review_due import status
print(status()[1])
