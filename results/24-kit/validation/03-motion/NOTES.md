# 03 · Brand motion 5 s — 焙次 No. 021 (product unit, 焙度 3)

**Files:** `motion-021.html` (seekable: `?t=ms`, `?clean`; built on `product/components/motion-unit.html`), `motion-021_5s.mp4` (1080 × 1080, 30 fps, 150 frames, 5.000 s, H.264), keyframes `motion-021_t700.png` (lines drawing), `_t1450.png` (level bar travelling in), `_t2200.png` (ember scaling), `_t5000.png` (hold / end frame). Re-render: `python3 ../render_motion.py`.

## Files read (in order)
1. `brand/readme.md` routing: brand motion → motion.md, motion.json, motion-unit.html
2. `brand/agent/visual/motion.md`
3. `brand/agent/visual/motion.json` and `product/components/motion.js` (same values)
4. `product/components/motion-unit.html`
5. Reference renders `product/components/screenshots/motion-unit_t5000.png`
6. Already read: magic_trick.md, brandmark.md, typography.md, stave.js, tokens.css, concepts.md

## Decisions where the kit was silent
- **Product unit, not signature unit.** motion.json allows "the single level bar in a product unit". For a batch piece I replaced the 3 signature bars with one 焙度 3 bar on line 3. It travels in from the right edge along line 3 and lands with spring `note_land`. Beat timing is unchanged (paper 0–300, lines 300–1120, note 1200–2000, ember 2100–2280, wordmark 2400–2860, hold to 5000).
- **The end frame is the level-3 mark + wordmark**, in the lockup-horizontal geometry. The kit only defines the lockup with the signature symbol. I used the level mark in its place, at the same size and position.
- **Added the batch data line** `焙次 No. 021 · 焙度 3 · 5 回` (whitelist pattern), in mono at 20 px under the stave. The kit has no data line in motion and no size for mono in video. I picked 20 px because label size (14 px) is too small in a 1080 frame. It enters as the third step of the wordmark beat: rise 8 px + fade, +120 ms (2 × the 60 ms container-then-text stagger), and finishes by 2800 ms. Then everything holds (more than 11 frames).
- **No Roast Score animation.** motion.md says "move less", and the score is the poster's job.
- **MP4 uses the `?clean` overlay** ("CONCEPT · NOT FINAL ART" bottom-right) rather than the timecode, so the video carries its concept flag.
- **Format 1080 × 1080**, as in the reference unit. The kit doesn't set an aspect ratio for motion.

## Invented data
- Only the brief's facts are shown (021, level 3, 5 rounds). The page loads `../batch-021.js`, whose per-round values are invented (see 02-poster/NOTES.md), but only the level and round count are used here.

## Checks
5 straight lines, bottom first ✓ · the bar moves horizontally only, no drop or rotation ✓ · one ember, scale only, no glow ✓ · plays once, no loop ✓ · no per-character animation of 焙曲 ✓ · last frame is a valid static lockup ✓.

## Kit gaps noticed
- `tools/render_motion.sh` is named in the kit but missing from the workdir. I wrote `../render_motion.py` instead (Playwright seeks `frame(t)` for each of 150 frames, then ffmpeg).
- In motion the stave is mark-width, not edge to edge. That's correct for a lockup, but magic_trick's "runs edge to edge" rule doesn't mention motion. A human should confirm.
- reduced-motion behaviour (show the hold frame, 280 ms cross-fade) is specified but not built into the reference HTML. I didn't add it either.
