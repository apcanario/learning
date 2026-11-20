#!/usr/bin/env bash
# Deploy a built edition to GitHub Pages through its public repo (S-DEC3, 20 Nov 2026: every value from the edition).
#
#   cd kit && python3 build.py && python3 verify.py && ./deploy.sh              the default edition (catalog.toml
#                                                                               edition_order's first)
#   ./deploy.sh <edition>                                                       editions/<edition>.toml
#   ./deploy.sh [<edition>] --dry-run                                           print the plan; clone, write and push nothing
#
# What it reads from editions/<edition>.toml: `site` (the built folder, relative to kit/), `title` (the built page must
# carry <title>{title}</title>), `deploy_remote` (the public repo it pushes to; an edition without one is not deployed
# here) and `url` (where Pages serves it); from the edition's brand (brands/<brand>.toml): `name` (the commit message and
# the deploy repo's README) and `repo` (the source repo the README names).
#
# The source repo stays private; only the build output travels. The script clones or pulls the deploy remote into a
# sibling folder of this repo named after it (override with DEPLOY_DIR), replaces its contents with the build, commits
# and pushes to main. Pages is set to serve main at the root, so the site is live at the edition's `url` a minute or so
# after the push. (First time only: switching Pages on in the repo's settings does not start a build by itself; the
# first push after that does, which this script makes. 28 Oct 2026.) Nothing else goes into that repo.
#
# The build is the edition's folder (docs/academy.md A2): index.html, the shell, plus one file per report (and, since
# P20, per syllabus, briefs and bibliography page; since P22, per history course home) under <course>/, fetched by
# relative path. The shell cannot work without those files beside it, so the whole tree travels, and files that left
# the build are removed from the repo. Publishing an edition means its artifact first, then this script.
set -euo pipefail

KIT="$(cd "$(dirname "$0")" && pwd)"
DRY=0
EDITION=""
for a in "$@"; do
  case "$a" in
    --dry-run) DRY=1 ;;
    -*) echo "unknown option $a" >&2; exit 2 ;;
    *) EDITION="$a" ;;
  esac
done

# the edition's values, one per line: edition, site, title, deploy_remote, url, brand name, brand repo
mapfile -t V < <(cd "$KIT" && python3 - "$EDITION" <<'PY'
import sys
from courses import EDITIONS, DEFAULT_EDITION, brand
name = sys.argv[1] or DEFAULT_EDITION
if name not in EDITIONS:
    raise SystemExit(f'no edition {name!r}: {", ".join(EDITIONS)}')
ed, b = EDITIONS[name], brand(name)
for k in ('deploy_remote', 'url'):
    if not ed.get(k):
        raise SystemExit(f'editions/{name}.toml has no `{k}`: this edition is not deployed by deploy.sh')
for v in (name, ed['site'], ed['title'], ed['deploy_remote'], ed['url'], b['name'], b['repo']):
    print(v)
PY
)
[ "${#V[@]}" -eq 7 ] || exit 1
EDITION="${V[0]}"; SITE="$KIT/${V[1]}"; TITLE="${V[2]}"; REMOTE="${V[3]}"; URL="${V[4]}"; NAME="${V[5]}"; SRCREPO="${V[6]}"
SRCREPO="${SRCREPO#https://github.com/}"
# ACADEMY_DIR: the name before S-DEC3, still read because saved unit prompts in docs/BACKLOG.md set it (drop it once
# they are gone)
DEPLOY_DIR="${DEPLOY_DIR:-${ACADEMY_DIR:-$(cd "$KIT/../.." && pwd)/$(basename "$REMOTE" .git)}}"

HAVE=""
if [ -d "$DEPLOY_DIR/.git" ]; then
  HAVE="$(git -C "$DEPLOY_DIR" remote get-url origin 2>/dev/null || true)"
  # S-DEC5 checker: never write one edition into another edition's clone (DEPLOY_DIR / ACADEMY_DIR apply to every edition)
  [ "${HAVE%.git}" = "${REMOTE%.git}" ] || { echo "$DEPLOY_DIR is a clone of ${HAVE:-nothing}, not $REMOTE: set DEPLOY_DIR" >&2; exit 1; }
fi

INDEX="$SITE/index.html"
[ -s "$INDEX" ] || { echo "no built site at $SITE: run python3 build.py --edition $EDITION first" >&2; exit 1; }
grep -qF "<title>$TITLE</title>" "$INDEX" || { echo "$INDEX is not the $TITLE page (title)" >&2; exit 1; }

if [ "$DRY" = 1 ]; then
  echo "edition:  $EDITION"
  echo "site:     $SITE ($(find "$SITE" -type f | wc -l | tr -d ' ') files; title '$TITLE' found)"
  echo "remote:   $REMOTE"
  echo "into:     $DEPLOY_DIR ($([ -n "$HAVE" ] && echo "a clone of $HAVE" || echo "a new clone"))"
  echo "url:      $URL"
  echo "commit:   $NAME build from $(basename "$SRCREPO")@$(git -C "$KIT" rev-parse --short HEAD 2>/dev/null || echo unknown)"
  echo "dry run: nothing cloned, written or pushed"
  exit 0
fi

if [ -d "$DEPLOY_DIR/.git" ]; then
  git -C "$DEPLOY_DIR" fetch origin
  if git -C "$DEPLOY_DIR" show-ref --verify --quiet refs/remotes/origin/main; then
    git -C "$DEPLOY_DIR" checkout -q main 2>/dev/null || git -C "$DEPLOY_DIR" checkout -q -b main
    git -C "$DEPLOY_DIR" reset -q --hard origin/main
  fi
else
  git clone "$REMOTE" "$DEPLOY_DIR"
fi
cd "$DEPLOY_DIR"
git symbolic-ref -q HEAD refs/heads/main >/dev/null 2>&1 || git checkout -q -b main 2>/dev/null || true

# replace the published tree with the build: everything but .git and README.md goes, then the build is copied in
find . -mindepth 1 -maxdepth 1 ! -name .git ! -name README.md -exec rm -rf {} +
cp -R "$SITE"/. .
touch .nojekyll
if [ ! -f README.md ]; then
  printf '# %s\n\nThe built site of the %s, published at %s. Build output only: the source is the private repo %s (`kit/`), and everything here is written by `kit/deploy.sh`. Do not edit here.\n' "$NAME" "$NAME" "$URL" "$SRCREPO" > README.md
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
    commit -q -m "$NAME build from $(basename "$SRCREPO")@$SRC ($WHAT)"
git push -u origin main
echo "pushed ($WHAT): $URL"
