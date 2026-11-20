"""S-DEC0 (20 Nov 2026) · the byte baseline for the decoupling refactor (docs/decoupling.md).

  python3 kit/baseline.py           builds the academy and greece editions and writes kit/baseline.json: the sha256
                                    of every file each build writes
  python3 kit/baseline.py --check   rebuilds both and lists every file that differs from kit/baseline.json
                                    (added, removed, changed); exit 1 if any does, 0 if none

What each build writes (kit/build.py):
  academy  kit/academy/ (the site), kit/README.md (the size table), kit/bibliography/ (biblio.py's README) and each
           history course's `bibliography` folder (biblio.py's unit-<n>.md beside the curated r-<id>.md; S-DEC5,
           courses/<id>/bibliography/, kit/bibliography/<id>/ before)
  greece   kit/editions/<site>/ (courses.py EDITIONS['greece']['site'], ignored by git)
Paths in the manifest are relative to kit/ (a file outside it, such as a course's bibliography, as ../<path>), sorted; the manifest holds no time or machine detail, so the same tree
gives the same file.
"""
import hashlib, json, os, pathlib, subprocess, sys, time

K = pathlib.Path(__file__).resolve().parent
MANIFEST = K / 'baseline.json'
EDITION_NAMES = ('academy', 'greece')
sys.path.insert(0, str(K))
from courses import EDITIONS, HISTORY, path as cpath


def outputs(edition):
    """The roots one edition's build writes, relative to kit/."""
    roots = [K / EDITIONS[edition]['site']]
    if edition == 'academy':
        roots += [K / 'README.md', K / 'bibliography'] + [cpath(c, 'bibliography') for c in HISTORY]
    return roots


def build(edition):
    t = time.time()
    r = subprocess.run([sys.executable, 'build.py', '--edition', edition], cwd=K, capture_output=True, text=True)
    if r.returncode:
        sys.stdout.write(r.stdout)
        sys.stderr.write(r.stderr)
        raise SystemExit(f'build.py --edition {edition} failed ({r.returncode})')
    return time.time() - t


def hashes(edition):
    out = {}
    for root in outputs(edition):
        files = [root] if root.is_file() else sorted(p for p in root.rglob('*') if p.is_file())
        for f in files:
            if '__pycache__' in f.parts:
                continue
            out[pathlib.Path(os.path.relpath(f, K)).as_posix()] = hashlib.sha256(f.read_bytes()).hexdigest()
    return dict(sorted(out.items()))


def run():
    got = {}
    for e in EDITION_NAMES:
        secs = build(e)
        got[e] = hashes(e)
        print(f'{e}: built in {secs:.0f} s, {len(got[e])} files')
    return got


if __name__ == '__main__':
    check = '--check' in sys.argv
    if check and not MANIFEST.exists():
        raise SystemExit(f'no {MANIFEST.name}: run baseline.py without --check first')
    got = run()
    if not check:
        MANIFEST.write_text(json.dumps({'editions': got}, indent=1, sort_keys=True) + '\n')
        print(f'wrote {MANIFEST.relative_to(K.parent)}: ' + ', '.join(f'{e} {len(h)} files' for e, h in got.items()))
        sys.exit(0)
    base = json.loads(MANIFEST.read_text())['editions']
    bad = 0
    for e in sorted(set(base) | set(got)):
        b, g = base.get(e, {}), got.get(e, {})
        added = sorted(set(g) - set(b))
        removed = sorted(set(b) - set(g))
        changed = sorted(p for p in set(b) & set(g) if b[p] != g[p])
        for tag, ps in (('added', added), ('removed', removed), ('changed', changed)):
            for p in ps:
                print(f'{e}: {tag} {p}')
        n = len(added) + len(removed) + len(changed)
        bad += n
        print(f'{e}: {len(g)} files, {n} differ' + (f' ({len(added)} added, {len(removed)} removed, {len(changed)} changed)' if n else ''))
    print('baseline: clean' if not bad else f'baseline: {bad} files differ')
    sys.exit(1 if bad else 0)
