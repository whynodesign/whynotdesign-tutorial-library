# Typography

Faces and ramp: `visual-system.json` → `type`. Tokens: `--font-*`, `--text-{level}-size|line|tracking|family`.
Licences: `../../readme.md` → Fonts.

## Four voices, max three per surface

| Voice | Face | Job |
| --- | --- | --- |
| Display 中文 | Noto Serif TC Bold | 焙曲, headlines (h1–display). Bold only. |
| Wordmark Latin | Lexend Exa 500, `--tracking-wordmark`, caps | TONEROAST only. Never for other words. |
| Mono | DM Mono | Numerals, labels, roast data, Latin small text. |
| Body 中文 | Noto Sans TC Regular | Sentences (back panels, captions, web). |

## The ramp

Screen (mirrors the JSON; the JSON wins): `caption 12 · label 14 · body 16 · lead 20 · h3 28 · h2 40 · h1 56 · display 96 · numeral 160` (px, by token).
Print: `--print-*` (pt). One headline per surface. Pick the level by job, not by space available.

## Numeral on the stave

A large level numeral stands **on line 1** and its cap height fills the stave: font size = stave height ÷ 0.7
(`type.numeral_on_stave`), colour amber. See `product/components/social-card.html`.

## Rules

- Chinese is set horizontally, left-aligned. Display tracking per token (≈ 0.04–0.08 em). No faux bold, no italic.
- Labels are written in caps **in the source**; CSS never changes case (DOM text must equal the whitelist string).
- Numerals are DM Mono, always, even inside Chinese text on product surfaces.
- Min print size `--print-legal-min` (studio default, check the market's labelling law).
- No brush, handwritten, "oriental" display or decorative faces. In image prompts, never name a font.

## When the rules don't cover it

Use mono at label size. It is never wrong.
