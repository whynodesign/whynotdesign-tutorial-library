# Packaging

> Concept / example. Nothing here is a production spec. Every number marked *est.* must be confirmed with the
> die-maker and printer on a physical proof. Labelling text required by law is **not** provided by this kit.

## 1 · The carton

Reverse tuck end (RTE) carton for 50 g, **L 70 × W 45 × D 120 mm**, board 0.45 mm.

| File (`assets/dieline/`) | What |
| --- | --- |
| `toneroast_rte_70x45x120.svg` | Dieline with layers CUT / CREASE / HALFCUT + dimensions |
| `toneroast_rte_70x45x120.manufacturing.svg` | Same, 0.25 line, no annotations |
| `toneroast_rte_70x45x120.dxf` | R12 DXF, layers CUT / CREASE / HALFCUT (y axis not flipped) |
| `params_used.json` | Tuck 12, dust flap 14, glue flap 12, tuck clearance 0.95 (auto from board thickness) |
| `dieline-overlay.svg` | Our overlay: panel names, 3 mm bleed (red dashed), 3 mm safe (magenta) |

- Flat size 243.8 × 234.0 mm. Panel widths 70 / 45.45 / 70.45 / 45.9 mm (thickness compensation).
- **Panel assignment (our assumption, confirm with die-maker):** x 0–70 = FRONT, 70–115.45 = SIDE A,
  115.45–185.9 = BACK, 185.9–231.8 = SIDE B, glue flap on the left of FRONT.
- 3D fold check: `/workspace/tutorial-tests/36/toneroast_fold_unfold.mp4` (Blender, test #36) — outside this kit.

> **Licence warning.** The dieline was generated with **open-dieline** (github.com/BrownBear127/open-dieline,
> v1.4.1), licensed **PolyForm Noncommercial 1.0.0**. Using it, or its outputs, for a client job may count as
> commercial use; our #85 test notes record hello@konvolut.art as the contact for a commercial licence. For a real job, have the
> die-maker draw the dieline or obtain a licence first.

## 2 · Bleed, safe area, artwork zones

| Token | Value | Rule |
| --- | --- | --- |
| `--print-bleed` | 3 mm | Every background and **every stave line** runs 3 mm past trim |
| `--print-safe` | 3 mm | No type or ember within 3 mm of trim or a crease |
| Inner design margin | +3 mm (6 mm from trim) | Where type starts on the front (see `label-front.html`) |

- Front panel: stave (gap `--stave-gap-front_panel`), level bar, ember, 焙曲 / TONEROAST, product, data line, origin, weight.
  Reference build: `product/components/label-front.html` (renders 76 × 126 mm incl. bleed; `?guides` shows trim/safe).
- Back panel: Roast Score of the batch (small), roaster's note ≤ 60 字, legal block, barcode zone.
- Sides carry the batch data line in mono, horizontal, and the level mark small.
- Tuck lid: blank or the mono symbol. Bottom: blank.
- **Barcode zone (back):** reserve ≈ 38 × 26 mm (EAN-13 at 100% nominal is 37.29 × 25.93 mm incl. quiet zones),
  printed K100 on unprinted paper, never on amber or celadon, never reduced below the printer's minimum magnification.
- **Legal block (back):** reserve a zone; the content (name, ingredients, origin, net weight, best-before, producer,
  storage, any other mandatory items) depends on the selling market's food-labelling law. Not written here.

## 3 · Colour build (*est.*)

| Colour | Build | Notes |
| --- | --- | --- |
| Rice paper | **The stock** (uncoated, natural/cream board close to the swatch) | If only white board is available, print a tint (CMYK est. in JSON) and proof — it will look flatter |
| Kiln char | K100 for text and stave lines; rich black only for large solids (est. C40 M40 Y40 K100) | Profile conversion gave 291% TAC; too heavy for uncoated |
| Oolong amber | **Spot**, matched to `lab_target` ΔE00 ≤ 2 | No Pantone/DIC reference chosen yet; pick from the printer's physical guide on the actual stock |
| Ember red | **Spot**, matched to `lab_target` | Same. It is one small dot, so a spot is cheap insurance against batch-to-batch drift |
| Celadon grey | CMYK est. or the stock (light-roast SKUs) | A celadon-coloured board is an option for 焙度 1–2 |

A 3-colour job (K + amber spot + ember spot) on cream uncoated board covers the default carton.
Uncoated stock darkens and dulls ink; proof before approving any colour.

## 4 · Finishes (工藝) — suggestions, all to be tested

- **Yes:** uncoated board; optional blind deboss of the five stave lines on the front (check minimum line width
  and spacing with the finisher — 0.35 mm lines at 6 mm gap may need thickening); matte water-based varnish if scuffing is an issue.
- **No:** gold or silver foil, gloss lamination, spot-UV on the ember, holograms, embossed calligraphy.
- Inner bag: tea must be in a food-safe inner pouch; the carton is not a food-contact layer.

## 5 · Print checks (before sending files)

1. Dieline on its own layer, as a named spot colour set to **overprint and non-printing**.
2. All type outlined or fonts embedded; CJK fonts licensed for the job (`readme.md` → Fonts).
3. Stave lines and backgrounds extend 3 mm into bleed; nothing important within 3 mm of trim or a crease.
4. Exactly one ember dot on each visible panel set (front + its adjacent side do not both carry an ember at the same height when folded).
5. Level bar on the correct line for the SKU (焙度 n = line n from bottom) — check against the batch sheet.
6. Small text (< 10 pt) and lines are K100 only, not rich black. TAC under the printer's limit (uncoated is often lower than coated).
7. Spot colours named consistently; no RGB, no unused swatches.
8. Images ≥ 300 ppi at 100%; any AI image flagged and replaced before commercial print.
9. Barcode scanned from a proof.
10. Physical fold test of a white sample (or the #36 Blender fold) before the full run.

## When the rules don't cover it

Ask the printer first, then choose the option with fewer inks and fewer finishes.
