#!/bin/bash
# Re-render every component screenshot + the anchor. Run after build_tokens.py / make_marks.py.
cd "$(dirname "$0")/.." && C=product/components && S=$C/screenshots
tools/render.sh $C/roast-badge.html $S/roast-badge.png 1200 640
for spec in "017 paper" "009 celadon" "018 char"; do set -- $spec
  SCALE=4 tools/render.sh $C/label-front.html $S/label-front_$1_$2.png 288 477 "?batch=$1&ground=$2"; done
SCALE=4 tools/render.sh $C/label-front.html $S/label-front_017_paper_guides.png 288 477 "?batch=017&ground=paper&guides"
tools/render.sh $C/poster.html $S/poster_017.png 1080 1440
tools/render.sh $C/poster.html $S/poster_017_noflag.png 1080 1440 "?noflag"
tools/render.sh $C/social-card.html $S/social-card_018.png 1080 1350
for t in 700 1450 2200 5000; do tools/render.sh $C/motion-unit.html $S/motion-unit_t$t.png 1080 1080 "?t=$t"; done
tools/render.sh $C/anchor.html brand/agent/visual/assets/anchor/anchor.png 1600 1200
cp brand/agent/visual/assets/anchor/anchor.png $S/anchor.png
