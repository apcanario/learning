"""P84: list every figure whose drawing changed between two builds of Academy (each figure of each page, in order,
compared as built). Usage: python3 changed.py <before academy dir> <after academy dir>"""
import re, sys, pathlib
a, b = map(pathlib.Path, sys.argv[1:3])
FIG = re.compile(r'<figure class="viz viz-([\w-]+)[^"]*">.*?</figure>', re.S)
def figs(p):
    return [(m.group(1), m.group(0)) for m in FIG.finditer(p.read_text())] if p.exists() else []
out = []
for f in sorted(b.rglob('*.html')):
    rel = f.relative_to(b); old, new = figs(a / rel), figs(f)
    if len(old) != len(new):
        out.append(f'{rel}: {len(old)} figures before, {len(new)} after'); continue
    for i, ((k, o), (_, n)) in enumerate(zip(old, new), 1):
        if o != n:
            out.append(f'{rel} figure {i} ({k})')
print('\n'.join(out)); print(f'# {len(out)} changed', file=sys.stderr)
