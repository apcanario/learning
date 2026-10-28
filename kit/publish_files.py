"""Print the report files of the built site for the Artifact tool's `files` (docs/academy.md A2).

python3 publish_files.py

Publish Academy, the artifact half: read https://claude.ai/artifact/WwmQpUSqAUJvrcmLczppEH with the Artifact tool,
then publish with that `url`, `file_path` = kit/academy/index.html, `root` = kit/academy and `files` = the JSON list
printed here (each path is published as spelled, relative to the shell, which is the path the shell fetches). One
publish carries at most 255 files; when there are more, this prints one list per line and each line after the first
goes in another publish to the same `url`. A report that has left the build stays on the artifact until it is passed
as null in a `files` map ({"greece/r-9.9.html": null}). Then ./deploy.sh.
"""
import json, pathlib

SITE = pathlib.Path(__file__).resolve().parent / 'academy'
BATCH = 255
files = sorted(str(f.relative_to(SITE)) for f in SITE.rglob('*') if f.is_file() and f.name != 'index.html')
if not files:
    raise SystemExit('no built site in academy/: run python3 build.py first')
for k in range(0, len(files), BATCH):
    print(json.dumps(files[k:k + BATCH]))
