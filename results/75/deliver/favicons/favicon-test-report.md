# Favicon test report

- **PASS** file favicon.svg
- **PASS** file favicon.ico
- **PASS** file favicon-16.png
- **PASS** file favicon-32.png
- **PASS** file favicon-48.png
- **PASS** file apple-touch-icon.png
- **PASS** file icon-192.png
- **PASS** file icon-512.png
- **PASS** file maskable-512.png
- **PASS** file site.webmanifest
- **PASS** file head-snippet.html
- **PASS** favicon.ico header
- **PASS** favicon.ico holds 16, 32 and 48 px — [(16, 16), (32, 32), (48, 48)]
- **PASS** favicon.ico entries are PNG data
- **PASS** favicon-16.png is 16x16 — (16, 16)
- **PASS** favicon-32.png is 32x32 — (32, 32)
- **PASS** favicon-48.png is 48x48 — (48, 48)
- **PASS** apple-touch-icon.png is 180x180 — (180, 180)
- **PASS** icon-192.png is 192x192 — (192, 192)
- **PASS** icon-512.png is 512x512 — (512, 512)
- **PASS** maskable-512.png is 512x512 — (512, 512)
- **PASS** manifest lists 192 and 512 icons — ['192x192', '512x512']
- **PASS** manifest has a maskable icon
- **PASS** manifest icon files exist
- **PASS** favicon.svg viewBox is square — 0 0 256 256
- **PASS** favicon.svg has no <text>/<image>/<foreignObject>
- **PASS** head snippet links the icons
- **PASS** maskable artwork stays inside the 80% safe-zone circle — 0 stray samples
- **PASS** 16 px favicon is not blank — 70% covered
- **ok** 16 px ink coverage between 8% and 85% — 70%
- **ok** no parts merge at 16 px — 1 blobs at 16 px vs 1 at 48 px
- **WARN** mark vs light tab contrast >= 3:1 — 1.25:1 (mean mark colour #ddc7ae)
- **ok** mark vs dark tab contrast >= 3:1 — 7.39:1 (mean mark colour #ddc7ae)

0 failed, 1 warnings. Warnings are heuristics (uncalibrated).
Not covered: how a real browser tab renders it. After deploying, open the site in Chrome and Safari once and check the tab, the bookmark and (iOS) the home-screen icon.