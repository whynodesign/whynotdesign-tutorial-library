#!/bin/bash
# Screenshot an HTML file with headless Chrome.  usage: tools/render.sh file.html out.png WIDTH HEIGHT [query]
# On this box Chrome must go through the glue wrapper (custom --user-data-dir hangs).
CHROME=${CHROME:-/workspace/tutorial-tests/_glue/google-chrome}
f=$(realpath "$1"); out=$(realpath -m "$2")
timeout 60 "$CHROME" --headless=new --no-sandbox --disable-gpu --hide-scrollbars --force-device-scale-factor=${SCALE:-1} \
  --allow-file-access-from-files --virtual-time-budget=4000 --window-size="$3,$4" --screenshot="$out" "file://$f$5" 2>/dev/null
ls -la "$out"
