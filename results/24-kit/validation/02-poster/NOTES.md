# 02 · Poster 1080 × 1440 — 焙次 No. 021

**Files:** `poster-021.html` (source, built on `product/components/poster.html`), `poster-021.png` (1080 × 1440 render). Data: `../batch-021.js`.

## Files read (in order)
1. `brand/magic_trick.md` (already read for 01)
2. `brand/readme.md` routing: poster → magic_trick, graphic-elements, layout, typography
3. `brand/agent/visual/graphic-elements.md` (Roast Score)
4. `brand/agent/visual/layout.md`
5. `brand/agent/visual/typography.md`
6. `brand/agent/visual/brandmark.md` (the poster uses the logo)
7. `brand/agent/visual/effects.md` (grain)
8. `product/components/poster.html`, `stave.js` `TR.score()`, `brand/agent/visual/visual-system.json` → `score`
9. Reference render `product/components/screenshots/poster_017.png`
10. Already read for 01: `brand/agent/verbal/concepts.md`, `color.md`, `tokens.css`

## Decisions where the kit was silent
- **The Roast Score of batch 021 is the only image.** No photography or AI image was used. The kit says none is required, and the stave must be drawn in code. I didn't read art-direction.md or how-to-prompt.md because no image model was used.
- **Headline = whitelist tagline** `焙火如樂譜` / `ROAST LIKE A SCORE`. I wrote no new headline: concepts.md says new copy needs human approval.
- **The last round's line equals the level** (the last 3 rounds are on line 3). Both kit examples end the score on the level's line (017 → 4, 018 → 5), so I treated "level = highest/final round intensity" as the convention. The kit never says this.
- **The logo is the wordmark (焙曲 / TONEROAST), not the symbol**, because the stave already carries the ember (one-ember rule).
- **Kept the concept flag** `CONCEPT / EXAMPLE ONLY · FICTIONAL ROAST DATA · NOT FINAL ART` because the data is invented.
- The ember sits at the right **margin** end of the stave (inside the bars' margins), as in the reference component.

## Invented data (FICTIONAL — must be replaced by the real roast log)
| Round | Hours | Line (intensity) | Rest after |
| --- | --- | --- | --- |
| 1 回 | 8 h | 2 | 歇 7 日 |
| 2 回 | 10 h | 2 | 歇 10 日 |
| 3 回 | 10 h | 3 | 歇 10 日 |
| 4 回 | 12 h | 3 | 歇 14 日 |
| 5 回 | 8 h | 3 | — |
Total 48 h of roasting and 41 days of rests. Bar widths are proportional to hours (computed by `TR.score`).

## Checks
5 lines, edge to edge ✓ · one ember ✓ · 5 amber bars, each one a round ✓ · rests are fixed gaps with mono labels ✓ · 3 type voices (serif display, wordmark, mono) ✓ · more than ⅓ of the surface is empty paper ✓.

## Kit gaps noticed
- `stave.js` draws the `歇 n 日` labels at `opacity 0.7`. color.md says "no … transparency of brand colours". This is a small conflict in the kit. I left the component unchanged.
- magic_trick says the ember sits "at the right end of the stave", but the stave bleeds off the edge. The component puts the ember at the right margin. I followed the component.
