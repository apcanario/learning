#!/usr/bin/env bash
# Deploy the built Academy page to GitHub Pages through the public repo apcanario/academy.
#
#   cd kit && python3 build.py && python3 verify.py && ./deploy.sh
#
# `learning` stays private; only the built page travels. The script clones or pulls apcanario/academy into a
# sibling folder of this repo (override with ACADEMY_DIR), copies personal-mythology.html in as index.html with a
# .nojekyll beside it, commits and pushes to main. Pages is set to serve main at the root, so the page is live at
# https://apcanario.github.io/academy/ a minute or so after the push. Nothing else goes into that repo: the kit,
# the reports and the docs are in `learning`; the page is a build output.
set -euo pipefail

KIT="$(cd "$(dirname "$0")" && pwd)"
PAGE="$KIT/personal-mythology.html"
REMOTE="https://github.com/apcanario/academy"
ACADEMY_DIR="${ACADEMY_DIR:-$(cd "$KIT/../.." && pwd)/academy}"
URL="https://apcanario.github.io/academy/"

[ -s "$PAGE" ] || { echo "no built page at $PAGE: run python3 build.py first" >&2; exit 1; }
grep -q '<title>Academy</title>' "$PAGE" || { echo "$PAGE is not the Academy page (title)" >&2; exit 1; }

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

cp "$PAGE" index.html
touch .nojekyll
if [ ! -f README.md ]; then
  printf '# Academy\n\nThe built page of the Academy, published at %s. Build output only: the source is the private repo apcanario/learning (`kit/`), and this file and `index.html` are written by `kit/deploy.sh`. Do not edit here.\n' "$URL" > README.md
fi

git add index.html .nojekyll README.md
if git diff --cached --quiet; then
  echo "nothing to deploy: $URL already has this build"
  exit 0
fi
SRC="$(git -C "$KIT" rev-parse --short HEAD 2>/dev/null || echo unknown)"
SIZE="$(wc -c < index.html)"
git -c user.name="${GIT_AUTHOR_NAME:-$(git -C "$KIT" config user.name || echo deploy)}" \
    -c user.email="${GIT_AUTHOR_EMAIL:-$(git -C "$KIT" config user.email || echo deploy@localhost)}" \
    commit -q -m "Academy build from learning@$SRC ($SIZE bytes)"
git push -u origin main
echo "pushed: $URL"
