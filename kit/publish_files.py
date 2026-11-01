"""Print the fetched files of the built site (reports, syllabi, briefs and bibliography pages, history course homes) for the Artifact tool's `files` (docs/academy.md A2).

python3 publish_files.py [--edition NAME]

P80 (1 Nov 2026): --edition NAME prints the fetched files of that edition's build (`EDITIONS[NAME]['site']`, e.g.
editions/greece, from `python3 build.py --edition NAME`), for a publish to the edition's own artifact
(`EDITIONS[NAME]['artifact']`), with `file_path` = that folder's index.html and `root` = that folder.
Publish Academy, the artifact half: read https://claude.ai/artifact/WwmQpUSqAUJvrcmLczppEH with the Artifact tool,
then publish with that `url`, `file_path` = kit/academy/index.html, `root` = kit/academy and `files` = the JSON list
printed here (each path is published as spelled, relative to the shell, which is the path the shell fetches). One
publish carries at most 255 files; when there are more, this prints one list per line and each line after the first
goes in another publish to the same `url`. A file that has left the build stays on the artifact until it is passed
as null in a `files` map ({"greece/r-9.9.html": null}). Then ./deploy.sh.
"""
import json, pathlib, sys
from courses import EDITIONS

ED = sys.argv[sys.argv.index('--edition') + 1] if '--edition' in sys.argv else 'academy'
if ED not in EDITIONS:
    raise SystemExit(f'no edition {ED!r} in courses.py EDITIONS: {", ".join(EDITIONS)}')
SITE = pathlib.Path(__file__).resolve().parent / EDITIONS[ED]['site']
BATCH = 255
files = sorted(str(f.relative_to(SITE)) for f in SITE.rglob('*') if f.is_file() and f.name != 'index.html')
if not files:
    raise SystemExit(f'no built site in {SITE.name}/: run python3 build.py' + (f' --edition {ED}' if ED != 'academy' else '') + ' first')
for k in range(0, len(files), BATCH):
    print(json.dumps(files[k:k + BATCH]))
