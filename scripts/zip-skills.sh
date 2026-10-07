#!/bin/sh
# Zip each skill for an upload-only environment (ChatGPT: Skills > Create >
# Upload from your computer). Writes dist/<skill>.zip with the skill's folder at
# the top of the archive. Usage: sh scripts/zip-skills.sh [skill ...]
set -eu
cd "$(dirname "$0")/.."
mkdir -p dist
[ "$#" -gt 0 ] || set -- $(cd skills && ls -d */ | tr -d /)
for s in "$@"; do
  [ -f "skills/$s/SKILL.md" ] || { echo "no skill named $s" >&2; exit 1; }
  rm -f "dist/$s.zip"
  (cd skills && zip -qr "../dist/$s.zip" "$s" -x '*/evals/*' '*/.DS_Store' '*/__pycache__/*')
  echo "dist/$s.zip"
done
