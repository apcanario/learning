"""Rebuild the Personal Mythology site on design/theme.css.

The history kit (personal-mythology-kit.zip, unzipped) keeps its own build: build.py inlines the kit's
shell.css into personal-mythology.html. This script runs that build unchanged on a temporary copy of
the kit whose shell.css is replaced by design/theme.css, so the site is styled from the one theme.
Nothing in the kit is modified.

    python3 build_history.py /path/to/personal-mythology        # the unzipped kit folder
    -> hubs/personal-mythology.html

To make the kit's own builds match from now on, copy design/theme.css over the kit's shell.css
(the theme keeps every class name shell.css had). See README.md.
"""
import pathlib, shutil, subprocess, sys, tempfile

HERE = pathlib.Path(__file__).resolve().parent
THEME = HERE.parent / 'design' / 'theme.css'
OUT = HERE / 'hubs' / 'personal-mythology.html'

if len(sys.argv) != 2:
    sys.exit(__doc__)
kit = pathlib.Path(sys.argv[1]).resolve()
if not (kit / 'build.py').exists() or not (kit / 'shell.css').exists():
    sys.exit(f'{kit} is not the Personal Mythology kit folder (no build.py / shell.css)')

with tempfile.TemporaryDirectory() as tmp:
    work = pathlib.Path(tmp) / 'kit'
    shutil.copytree(kit, work, ignore=shutil.ignore_patterns('__pycache__'))
    shutil.copyfile(THEME, work / 'shell.css')
    r = subprocess.run([sys.executable, 'build.py'], cwd=work, capture_output=True, text=True)
    if r.returncode:
        sys.exit(r.stdout + r.stderr)
    OUT.parent.mkdir(exist_ok=True)
    shutil.copyfile(work / 'personal-mythology.html', OUT)
    print(r.stdout.strip())
print(f'wrote {OUT.relative_to(HERE)} ({OUT.stat().st_size:,} bytes), styled from {THEME.relative_to(HERE.parent)}')
