# Concepts, naming and the whitelist

## The whitelist (exact strings)

These are the only strings that may appear on product surfaces, posters, social cards and the anchor
without a human writing new copy. **Copy them character for character.** The same strings appear on
`agent/visual/assets/anchor/anchor.png`; an image model will mix any near-variant with the anchor's
version (Exp09), so never "improve" them.

| Use | String (exact) | Notes |
| --- | --- | --- |
| Chinese name | `焙曲` | Two characters, no space. |
| Latin name | `TONEROAST` | One word, all caps, never "Tone Roast", "ToneRoast", "TONE ROAST". |
| Tagline zh | `焙火如樂譜` | Traditional 樂譜. |
| Tagline en | `ROAST LIKE A SCORE` | Written in caps in the source. |
| Product zh | `炭焙烏龍` | |
| Product en | `CHARCOAL-ROASTED OOLONG` | Hyphenated. |
| Level zh | `焙度 1` … `焙度 5` | Space before the numeral. |
| Level en | `ROAST LEVEL 1` … `ROAST LEVEL 5` | |
| Batch | `焙次 No. 017` | Three digits, zero-padded; `No.` with capital N and a period. |
| Rounds | `6 回` | Count of rounds in the batch. |
| Round label (score) | `1 回 · 8 h` | Round number · hours. |
| Rest label (score) | `歇 7 日` | |
| Origin | `台灣 · TAIWAN` | |
| Net weight | `50 g` | |
| Combined data line | `焙次 No. 017 · 焙度 4 · 6 回` | Order is fixed: batch · level · rounds. |
| Short data line | `焙度 4 · 6 回` | When the batch number is shown elsewhere on the surface. |
| Product line | `炭焙烏龍 · CHARCOAL-ROASTED OOLONG` | One-line form; on a front panel set as two lines. |

Separator everywhere: ` · ` (space, U+00B7, space).

## Glossary

| Term | Means | Don't say |
| --- | --- | --- |
| 焙次 / batch | One charcoal roast run, numbered | 批號, lot |
| 焙度 1–5 / roast level | 1 light → 5 deepest | 輕焙/重焙 alone without the number |
| 回 / round | One pass over the charcoal | 次, pass |
| 歇 / rest | The pause between rounds | 冷卻期 |
| 譜 / score | The drawn roast log | chart, graph, melody |

## Writing a new line

New headlines follow the pattern **one concrete fact + one sensory word**, ≤ 6 字 for headlines:
「十日一歇」, 「炭香收尾」. Run every new string past a human before it reaches an image prompt or the anchor,
and add it to this table when approved.

## When the rules don't cover it

If a surface seems to need text that is not here, leave the space empty and flag it. Empty is on-brand;
an invented claim is not.
