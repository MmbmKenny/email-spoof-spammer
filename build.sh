#!/usr/bin/env bash
# Assemble the public website into ./public for static hosting
# (Cloudflare Pages / GitHub Pages / Netlify). No framework, no dependencies.
# Only the landing page + demos are published — internal docs, the CRM, and
# .claude are deliberately excluded so they are never served publicly.
set -euo pipefail

OUT="public"
rm -rf "$OUT"
mkdir -p "$OUT"

# Landing page becomes the site root (index.html). Its demo paths are relative
# to the landing/ folder ("../demos/"); rewrite them to be root-relative.
sed 's#\.\./demos/#demos/#g' landing/index.html > "$OUT/index.html"

# Demos
cp -r demos "$OUT/demos"
# The demo gallery links back to ../landing/index.html; at the site root the
# landing page is ../index.html.
sed -i 's#\.\./landing/index.html#../index.html#g' "$OUT/demos/index.html"

# Optional niceties
: > "$OUT/.nojekyll"   # in case of GitHub Pages, disable Jekyll processing

echo "Built $OUT/ :"
find "$OUT" -type f | sort
