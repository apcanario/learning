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
# The build is the folder kit/academy/ (docs/academy.md A2): index.html, the shell, plus one file per report (and, since
# P20, per syllabus, briefs and bibliography page; since P22, per history course home) under <course>/, fetched by relative path. The shell cannot work without those files beside it, so the whole tree
# travels, and files that left the build are removed from the repo. (The single page personal-mythology.html was
# retired at A2.) "Publish Academy" means the artifact first, then this script.
set -euo pipefail

KIT="$(cd "$(dirname "$0")" && pwd)"
SITE="$KIT/academy"
REMOTE="https://github.com/apcanario/academy"
ACADEMY_DIR="${ACADEMY_DIR:-$(cd "$KIT/../.." && pwd)/academy}"
URL="https://apcanario.github.io/academy/"

INDEX="$SITE/index.html"
[ -s "$INDEX" ] || { echo "no built site at $SITE: run python3 build.py first" >&2; exit 1; }
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
cp -R "$SITE"/. .
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
WHAT="$(find . -type f ! -path './.git/*' ! -name README.md ! -name .nojekyll | wc -l | tr -d ' ') files, $(du -sk --exclude=.git . | cut -f1) KB"
git -c user.name="${GIT_AUTHOR_NAME:-$(git -C "$KIT" config user.name || echo deploy)}" \
    -c user.email="${GIT_AUTHOR_EMAIL:-$(git -C "$KIT" config user.email || echo deploy@localhost)}" \
    commit -q -m "Academy build from learning@$SRC ($WHAT)"
git push -u origin main
echo "pushed ($WHAT): $URL"
