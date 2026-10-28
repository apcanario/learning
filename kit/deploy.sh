#!/usr/bin/env bash
# Deploy the built Academy site to GitHub Pages through the public repo apcanario/academy.
#
#   cd kit && python3 build.py && python3 verify.py && ./deploy.sh
#
# `learning` stays private; only the build output travels. The script clones or pulls apcanario/academy into a
# sibling folder of this repo (override with ACADEMY_DIR), replaces its contents with the build, commits and pushes
# to main. Pages is set to serve main at the root, so the site is live at https://apcanario.github.io/academy/ a
# minute or so after the push. (First time only: switching Pages on in the repo's settings does not start a build by
# itself; the first push after that does, which this script makes. 28 Oct 2026.) Nothing else goes into that repo: the kit, the reports and the docs are in `learning`.
#
# Two build shapes (docs/academy.md A2, P10):
#   - before the split: the single page personal-mythology.html, copied in as index.html;
#   - after the split: the folder kit/academy/ (index.html as the shell plus one file per report under
#     <course>/r-<id>.html, fetched by relative path), copied in whole. The shell cannot work without the report
#     files beside it, so the whole tree travels, and files that left the build are removed from the repo.
# The folder wins when it exists. "Publish Academy" means the artifact first, then this script.
set -euo pipefail

KIT="$(cd "$(dirname "$0")" && pwd)"
PAGE="$KIT/personal-mythology.html"
SITE="$KIT/academy"
REMOTE="https://github.com/apcanario/academy"
ACADEMY_DIR="${ACADEMY_DIR:-$(cd "$KIT/../.." && pwd)/academy}"
URL="https://apcanario.github.io/academy/"

if [ -d "$SITE" ] && [ -s "$SITE/index.html" ]; then
  SHAPE="site"; INDEX="$SITE/index.html"
else
  SHAPE="page"; INDEX="$PAGE"
  [ -s "$PAGE" ] || { echo "no built page at $PAGE and no site at $SITE: run python3 build.py first" >&2; exit 1; }
fi
grep -q '<title>Academy</title>' "$INDEX" || { echo "$INDEX is not the Academy page (title)" >&2; exit 1; }

if [ -d "$ACADEMY_DIR/.git" ]; then
  git -C "$ACADEMY_DIR" fetch origin
  if git -C "$ACADEMY_DIR" show-ref --verify --quiet refs/remotes/origin/main; then
    git -C "$ACADEMY_DIR" checkout -q main 2>/dev/null || git -C "$ACADEMY_DIR" checkout -q -b main
    git -C "$ACADEMY_DIR" reset -q --hard origin/main
  fi
else
  git clone "$REMOTE" "$ACADEMY_DIR"
fi
cd "$ACADEMY_DIR"
git symbolic-ref -q HEAD refs/heads/main >/dev/null 2>&1 || git checkout -q -b main 2>/dev/null || true

# replace the published tree with the build: everything but .git and README.md goes, then the build is copied in
find . -mindepth 1 -maxdepth 1 ! -name .git ! -name README.md -exec rm -rf {} +
if [ "$SHAPE" = site ]; then
  cp -R "$SITE"/. .
else
  cp "$PAGE" index.html
fi
touch .nojekyll
if [ ! -f README.md ]; then
  printf '# Academy\n\nThe built site of the Academy, published at %s. Build output only: the source is the private repo apcanario/learning (`kit/`), and everything here is written by `kit/deploy.sh`. Do not edit here.\n' "$URL" > README.md
fi

git add -A
if git diff --cached --quiet; then
  echo "nothing to deploy: $URL already has this build"
  exit 0
fi
SRC="$(git -C "$KIT" rev-parse --short HEAD 2>/dev/null || echo unknown)"
if [ "$SHAPE" = site ]; then
  WHAT="$(find . -type f ! -path './.git/*' ! -name README.md ! -name .nojekyll | wc -l | tr -d ' ') files, $(du -sk --exclude=.git . | cut -f1) KB"
else
  WHAT="$(wc -c < index.html) bytes"
fi
git -c user.name="${GIT_AUTHOR_NAME:-$(git -C "$KIT" config user.name || echo deploy)}" \
    -c user.email="${GIT_AUTHOR_EMAIL:-$(git -C "$KIT" config user.email || echo deploy@localhost)}" \
    commit -q -m "Academy build from learning@$SRC ($SHAPE, $WHAT)"
git push -u origin main
echo "pushed ($SHAPE): $URL"
