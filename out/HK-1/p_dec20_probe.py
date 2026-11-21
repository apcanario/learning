"""P-DEC20 probe (never the main tree). Two modes:
  fieldnotes <copy-root> <n>: after out/DEC-C/p_dec11_template.py, give the template test's course home-composting n units
     (HC3..HCn: dummy units of about 1,250 words in the template test's sentences, each written on its own day), so the
     fieldnotes edition's course home has n written rises. Run in ascending n from a fresh template test.
  sce <copy-root> <n>: SCE2..SCEn as copies of SCE1's text under their own code and title (SCE1 is written), so SCE's
     home has n written rises among its 20; and editions/sce-probe.toml, an edition of SCE alone (marketing-ai's rules).
"""
import pathlib, re, sys, tomllib
mode, root, n = sys.argv[1], pathlib.Path(sys.argv[2]).resolve(), int(sys.argv[3])
assert root != pathlib.Path('/home/claude/learning'), 'never in the main tree'
S = ['A heap works when the mix of materials, the water and the air are kept in balance over the weeks.',
     'Brown materials such as dry leaves, straw and torn cardboard give the microbes carbon and keep the heap open.',
     'Green materials such as vegetable peelings, coffee grounds and fresh grass clippings give them nitrogen and water.',
     'Too many greens make a wet, sour heap; too many browns make a dry heap that barely changes for months.',
     'Turning the heap with a fork lets air in, and the microbes that need air work faster than those that do not.',
     'A handful squeezed hard should give a drop or two of water and no more, like a wrung sponge.',
     'Chop large pieces before they go in, because small pieces offer more surface for the microbes to work on.']
def body(heads):
    return '\n'.join(f'## {h}\n\n' + '\n\n'.join(' '.join(S[(p + k) % len(S)] for k in range(7)) for p in range(3)) + '\n' for h in heads)

if mode == 'fieldnotes':
    C = root / 'courses/home-composting'
    ct = (C / 'course.toml').read_text(); br = (C / 'briefs.md').read_text(); ci = root / 'docs/courses-index.md'; cit = ci.read_text()
    for k in range(3, n + 1):
        code = f'HC{k}'
        if (C / f'{code}-dummy.md').exists(): continue
        ct = ct.replace("  ['HC2', 'Opus 5.5', 'off'],\n", "  ['HC2', 'Opus 5.5', 'off'],\n" + f"  ['{code}', 'Opus 5.5', 'off'],\n", 1) if k == 3 else \
             ct.replace(f"  ['HC{k-1}', 'Opus 5.5', 'off'],\n", f"  ['HC{k-1}', 'Opus 5.5', 'off'],\n  ['{code}', 'Opus 5.5', 'off'],\n", 1)
        ct = ct.replace('\n[[pack.changelog]]', f"\n[[pack.courses.units]]\ncode = '{code}'\ntitle = 'Dummy unit {k}'\nscope = 'Probe only.'\ndeliverable = 'a probe sheet'\n\n[[pack.changelog]]", 1)
        br += f'\n## {code}\n\nUnit {code}, Dummy unit {k}. Probe only. Deliverable: a probe sheet.\n'
        (C / f'{code}-dummy.md').write_text(f'---\ncode: {code}\ntitle: Dummy unit {k}\ncourse: home-composting · HC · Home composting\nmodel: Opus 5.5\n'
            f'written: 2026-11-{20 - k:02d}\nsearch: off\nintro: Unit {code}, P-DEC20 probe.\n---\n\n# {code} · Dummy unit {k}\n\n'
            + body(['1 · One', '2 · Two', '3 · Three']) + '\n## Sources\n\n- None cited; probe.\n')
        cit = cit.rstrip('\n') + f'\n| {k} | {code} | HC | Dummy unit {k} | written {20 - k} Nov 2026 | Opus 5.5 | off | `courses/home-composting/{code}-dummy.md` |\n'
    (C / 'course.toml').write_text(ct); (C / 'briefs.md').write_text(br); ci.write_text(cit)
elif mode == 'sce':
    C = root / 'courses/supply-chain-execution'
    src = (C / 'SCE1-the-map-the-words-and-the-evidence.md').read_text()
    fm, text = src.split('---', 2)[1:]
    for f in C.glob('*-dummy.md'): f.unlink()
    for k in range(2, n + 1):   # SCE1 is written; SCE2..SCEn get SCE1's body under their own code and title
        code = f'SCE{k}'
        title = re.search(rf"code = '{code}'\ntitle = (['\"])(.*?)\1", (C / 'course.toml').read_text()).group(2)
        head = re.sub(r'^code: .*$', f'code: {code}', fm, flags=re.M)
        head = re.sub(r'^title: .*$', f'title: {title}', head, flags=re.M)
        head = re.sub(r'^intro: .*$', f'intro: P-DEC20 probe copy of SCE1 under {code}.', head, flags=re.M)
        (C / f'{code}-dummy.md').write_text('---' + head + '---' + text.replace('# SCE1 · The map, the words and the evidence', f'# {code} · {title}', 1))
    m = (root / 'editions/marketing-ai.toml').read_text()   # its own [[rules]], as marketing-ai's (academy's brand rules name courses it lacks)
    (root / 'editions/sce-probe.toml').write_text('title = "SCE probe"\ncourses = ["supply-chain-execution"]\nomit = ["changelog", "backlog", "build", "figures", "planned"]\nsite = "editions/sce-probe"\nbrand = "academy"\n\n' + m[m.index('[[rules]]'):])
else:
    raise SystemExit('mode?')
