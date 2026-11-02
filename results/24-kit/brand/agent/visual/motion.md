# Motion

Values: `motion.json` (generated from `visual-system.json` → `motion`). Reference build:
`product/components/motion-unit.html` (seekable with `?t=ms`), rendered by `tools/render_motion.sh` to
`product/components/screenshots/motion-unit_5s.mp4`.

## The signature move: Stave → Note → Ember (5 s, 150 frames @ 30 fps)

| Beat | ms | What |
| --- | --- | --- |
| paper | 0–300 | Rice paper only |
| lines | 300–1120 | Five lines draw left → right, bottom line first, `stagger.lines_bottom_to_top`, `dur.line_draw`, `ease.enter` |
| note | 1200–2000 | The 3 signature bars (or one level bar) travel in from the right edge **along their own line/space** and land with spring `note_land` (≈1–2% overshoot, one bounce max), `stagger.bars` |
| ember | 2100–2280 | The dot scales 0 → 1. No glow, no flicker, no particles |
| wordmark | 2400–2860 | 焙曲 then TONEROAST rise 8 px and fade in, container-then-text stagger |
| hold | 2860–5000 | Still. The last frame is a valid static lockup |

Why: the move *is* the trick — the score is written, then read. Bars move horizontally because time runs left to
right on a score; they never drop, bounce in from above, or rotate.

## Rules
- Runs **once**. No loops, no ambient pulsing ember.
- Lines never wobble, wave or draw by hand-jitter. The stave is ruled.
- No per-character animation of 焙曲. No 3D, no camera moves, no motion blur trails.
- Under `prefers-reduced-motion`: show the hold frame, 280 ms cross-fade.
- Title holds: any text stays fully still ≥ 11 frames before anything else moves.

## Interface motion
Hover `--dur-quick` `--ease-standard` (colour only, never size); reveal `--dur-base` `--ease-enter`;
dismiss `--dur-quick` `--ease-exit`.

## When the rules don't cover it
Move less. If a second move seems needed, make it the next beat of the score, left to right.
