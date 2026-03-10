#!/bin/sh
set -eu

ROOT="/Users/zl/AMy/projects/amigos/file/资料汇总"

python3 "$ROOT/scripts/update_readme.py"

git -C "$ROOT" add README.md .gitignore 每周新闻汇总 scripts

if git -C "$ROOT" diff --cached --quiet; then
  echo "No changes to commit."
  exit 0
fi

git -C "$ROOT" commit -m "Update weekly news"
git -C "$ROOT" push -u origin HEAD
