"""P-DEC8 check: every file that differs between the before and after trees differs only by removal of the
S-NOAUDIT clause, and the set of differing files is exactly the expected set (out/DEC-C/expected.md).

  python3 out/DEC-C/check_dec8.py <before-root> <after-root>
    each root holds academy/ and marketing-ai/ (before: copies taken before the change; after: kit/academy and
    kit/editions/marketing-ai). Word-level diffs go to out/DEC-C/diffs/. Exit 1 on any other difference.
"""
import difflib, hashlib, pathlib, re, sys

HERE = pathlib.Path(__file__).resolve().parent
CLAUSE = ("; audits are the data file's AUDIT_LOG, the record of the audits run before the Fable stage closed "
          "(S-NOAUDIT, 15 Nov 2026)")
EXPECTED = {
    'academy/building-with-ai-bw/built.html',
    'academy/sport-psychology-sp/built.html',
    'academy/supply-chain-execution-sce/built.html',
    'academy/ux-ia/built.html',
    'marketing-ai/building-with-ai-bw/built.html',
}


def tree(root):
    return {p.relative_to(root).as_posix(): p for p in root.rglob('*') if p.is_file()}


def words(s):
    return re.findall(r'\S+|\s+', s)


def main(before, after):
    before, after = pathlib.Path(before), pathlib.Path(after)
    out = HERE / 'diffs'
    out.mkdir(exist_ok=True)
    fails, differing = [], []
    for ed in ('academy', 'marketing-ai'):
        b, a = tree(before / ed), tree(after / ed)
        for k in sorted(set(b) | set(a)):
            key = f'{ed}/{k}'
            if k not in b or k not in a:
                fails.append(f'{key}: {"added" if k not in b else "removed"}')
                continue
            if hashlib.sha256(b[k].read_bytes()).digest() == hashlib.sha256(a[k].read_bytes()).digest():
                continue
            differing.append(key)
            if key not in EXPECTED:
                fails.append(f'{key}: differs, not in expected.md')
            bt, at = b[k].read_text(), a[k].read_text()
            wd = [l for l in difflib.unified_diff(words(bt), words(at), lineterm='', n=6)]
            (out / (key.replace('/', '__') + '.worddiff.txt')).write_text('\n'.join(wd) + '\n')
            n = bt.count(CLAUSE)
            if n != 1:
                fails.append(f'{key}: clause occurs {n} times before, expected 1')
            elif bt.replace(CLAUSE, '', 1) != at:
                fails.append(f'{key}: differs by more than the clause')
            else:
                print(f'ok  {key}: differs only by removal of the clause')
    for key in sorted(EXPECTED - set(differing)):
        fails.append(f'{key}: expected to differ, unchanged')
    # files with audit_log rows keep the clause
    for key in ('academy/brand-a/built.html', 'academy/brand-b/built.html', 'academy/personal-brand-pb/built.html',
                'marketing-ai/personal-brand-pb/built.html'):
        if CLAUSE not in (after / key).read_text():
            fails.append(f'{key}: clause missing (course has audit_log rows)')
        else:
            print(f'ok  {key}: keeps the clause')
    print(f'{len(differing)} differing files')
    for f in fails:
        print('FAIL', f)
    print('P-DEC8 check:', 'FAILED' if fails else 'PASSED')
    return 1 if fails else 0


if __name__ == '__main__':
    sys.exit(main(*sys.argv[1:3]))
