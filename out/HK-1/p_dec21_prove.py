import pathlib, filecmp, re, difflib, html
A = pathlib.Path('/tmp/start/academy'); B = pathlib.Path('/home/claude/learning/kit/academy')
fa = {p.relative_to(A).as_posix() for p in A.rglob('*') if p.is_file()}
fb = {p.relative_to(B).as_posix() for p in B.rglob('*') if p.is_file()}
print('only in start:', sorted(fa - fb)); print('only in new:', sorted(fb - fa))
diff = sorted(f for f in fa & fb if (A / f).read_bytes() != (B / f).read_bytes())
print('differing files:', diff)
row = re.compile(r'<tr><td>Audit cadence</td>.*?</tr>', re.S)
def txt(s): return html.unescape(re.sub(r'<[^>]+>', ' | ', s)).strip()
for f in diff:
    if f == 'index.html': continue
    a, b = (A / f).read_text(), (B / f).read_text()
    ra, rb = row.findall(a), row.findall(b)
    assert len(ra) == len(rb) == 1, (f, len(ra), len(rb))
    same = a.replace(ra[0], 'ROW') == b.replace(rb[0], 'ROW')
    print(f'\n{f}: only the Audit cadence row differs: {same}')
    print('  OLD:', txt(ra[0])); print('  NEW:', txt(rb[0]))
for h in ('greece/built.html', 'rome/built.html'):
    print(h, 'unchanged:', (A / h).read_bytes() == (B / h).read_bytes())
# index.html: does it hold an Audit cadence row?
a, b = (A / 'index.html').read_text(), (B / 'index.html').read_text()
print('index.html Audit cadence rows start/new:', len(row.findall(a)), len(row.findall(b)), 'equal:', row.findall(a) == row.findall(b))
