#!/bin/sh
# A minimal toolsmith workshop whose yazi page claims previewers are fine; the
# probe it names checks the binaries for real. Usage: sh fixtures/workshop.sh <dest>
set -e
dest=$1
[ -n "$dest" ] || { echo "usage: $0 <dest-dir>" >&2; exit 2; }
[ ! -e "$dest" ] || { echo "$dest exists" >&2; exit 2; }
mkdir -p "$dest/topics" "$dest/probes"
cd "$dest"
git init -q -b main
git config user.email fixture@example.com
git config user.name fixture

cat > CLAUDE.md <<'X'
# Workshop

This directory is a toolsmith workshop.

## Index
- [yazi](topics/yazi.md): file manager config and previewers.
X

cat > topics/yazi.md <<'X'
# yazi

## State pointers
- Previewer binaries: `probes/yazi-previewers.sh`.

## Decisions
- 2026-08-03 - previewers set: ffmpeg, 7zz, pdftoppm, magick, resvg. All present.
X

cat > probes/yazi-previewers.sh <<'X'
#!/bin/sh
# probe: yazi-previewers
# what: are the binaries yazi's previewers call on PATH?
# scope: local
# read-only: only runs `command -v`
rc=0
for b in ffmpeg 7zz pdftoppm magick resvg; do
  if command -v "$b" >/dev/null 2>&1; then echo "ok    $b"; else echo "MISS  $b"; rc=1; fi
done
exit $rc
X
chmod +x probes/yazi-previewers.sh
git add -A && git commit -qm workshop
