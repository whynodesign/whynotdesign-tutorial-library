#!/bin/bash
# Render the 5 s brand unit frame by frame (deterministic ?t=) and encode MP4. ~2 min on the box.
cd "$(dirname "$0")/.." && D=$(mktemp -d)
for f in $(seq 0 149); do t=$(python3 -c "print(round($f*1000/30,3))"); tools/render.sh product/components/motion-unit.html $D/f_$(printf %03d $f).png 1080 1080 "?t=$t&clean" >/dev/null; done
ffmpeg -y -loglevel error -framerate 30 -i $D/f_%03d.png -c:v libx264 -pix_fmt yuv420p -crf 18 product/components/screenshots/motion-unit_5s.mp4 && ls -la product/components/screenshots/motion-unit_5s.mp4
