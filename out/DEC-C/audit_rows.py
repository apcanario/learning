import tomllib, pathlib
for p in sorted(pathlib.Path('courses').glob('*/course.toml')):
    t = tomllib.loads(p.read_text())
    pk = t.get('pack')
    if pk is None: print(p.parent.name, 'no pack (not markdown)'); continue
    print(p.parent.name, 'audit_log rows:', len(pk.get('audit_log', [])))
