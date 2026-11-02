# Colour

Values: `visual-system.json` → `color` (HEX, CMYK estimate, Lab target). Tokens: `--rice-paper`, `--kiln-char`,
`--oolong-amber`, `--celadon-grey`, `--ember-red`. Swatch sheet: `assets/swatches/swatch-sheet.png`.

## The proportion rule

Default surface: **rice paper ≈ 65 · kiln char ≈ 24 · oolong amber ≈ 10 · ember ≤ 1 (one dot)**.
Celadon replaces part of the rice paper only on light-roast (焙度 1–2) packs, sachets and secondary panels.
A dark surface (char ground) inverts paper and char; amber and ember stay the same size.

| Colour | Job | Never |
| --- | --- | --- |
| Rice paper 米紙 | Ground. Ideally the stock itself. | Pure white substitutes |
| Kiln char 窯炭 | Text, stave lines, dark grounds | Grey tints of it as a "softer" text colour |
| Oolong amber 烏龍琥珀 | Note bars, the score, a large numeral | Body text, backgrounds, outlines, decoration |
| Celadon grey 青瓷灰 | Light-roast ground, info panels | Text on rice paper (1.79:1), next to amber as a pair accent |
| Ember red 餘燼紅 | The one ember dot | Backgrounds, text, lines, a second dot, touching amber |

## Pairings and contrast

See `contrast_wcag` in the JSON. Body text only char-on-paper, char-on-celadon, or paper-on-char.
Amber type only at ≥ 24 px / 18 pt (≈ 3.8:1). No gradients, tints or transparency of brand colours, except the
paper-grain texture.

## Print

CMYK numbers in the JSON are **estimates** from a generic SWOP ICC profile, not proofed. Amber and ember should be
spot inks matched to their **Lab targets** (ΔE00 ≤ 2); no Pantone/DIC reference has been chosen yet. See `packaging.md`.

## When the rules don't cover it

Remove colour before adding it. If a fifth hue seems necessary, it is a sign the layout is doing too much.
