# 01 · Front panel — 焙次 No. 021 · 焙度 3 · 5 回

**Files:** `front-021.html` (source, built on `product/components/label-front.html`), `front-021_paper.png` (4× render, 76 × 126 mm incl. 3 mm bleed), `front-021_paper_guides.png` (same render with trim (black) and safe area (green dashed) shown).
Shared data: `../batch-021.js`. Re-render: `python3 ../render.py`.

## Files read (in order)
1. `brand/magic_trick.md`
2. `brand/readme.md` (routing: packaging front → magic_trick, packaging, layout, color, concepts)
3. `brand/agent/visual/packaging.md`
4. `brand/agent/visual/layout.md`
5. `brand/agent/visual/color.md`
6. `brand/agent/verbal/concepts.md`
7. `product/components/README.md`, `label-front.html`, `stave.js`, `example-batches.js`, `components.css`
8. `brand/agent/visual/tokens.css`, `fonts.css`, `visual-system.json` (mark, score, layout)
9. Reference render `product/components/screenshots/label-front_017_paper.png`

## Decisions where the kit was silent
- **Built from the reference component, not from scratch.** Only the data changed. Layout, type sizes and positions come from `label-front.html`.
- **Ground = rice paper.** Celadon is only for 焙度 1–2 (color.md), and the char ground is never tied to a level, so 焙度 3 gets the default ground.
- **Level bar on line 3**, running from `mark-level-x-start` off the right edge into the bleed. The kit allows this for front panels only.
- **No concept flag on the panel.** The reference front panel has none, and the safe area has no room for one. The concept status is recorded here instead.
- **Data line** uses the whitelist pattern `焙次 No. 021 · 焙度 3 · 5 回`. `021` follows the three-digit zero-padded rule.
- **No back, side or legal panel.** None was asked for, and the kit doesn't supply legal text.

## Invented data
- Only the brief's facts appear on this panel (batch 021, level 3, 5 rounds). The round count comes from the invented roast log in `../batch-021.js`, which has 5 rounds, matching the brief. The per-round values are invented; see 02-poster/NOTES.md.
- Net weight `50 g` and origin `台灣 · TAIWAN` are whitelist strings, kept as in the kit.

## Checks
5 lines, edge to edge into the bleed ✓ · one ember, inside the safe area ✓ · one amber bar on line 3 = 焙度 3 ✓ · ember doesn't touch amber ✓ · every string is on the whitelist ✓ · nothing important within 3 mm of trim ✓ (see the guides render).

## Kit gaps noticed
- On the reference front panel, 焙曲 and TONEROAST sit below the stave, not on its lines. magic_trick.md says type sits on the lines "when text shares a surface". I followed the component. A human should decide whether the rule applies to the front panel.
- `README.md` points to `tools/render.sh`, but there is no `tools/` folder in the workdir. I rendered with headless Chrome + Playwright (`../render.py`).
- `packaging.md` points to a 3D fold file outside the kit (`/workspace/tutorial-tests/36/...`). Per the brief, I didn't open it.
