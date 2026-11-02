# Layout

Values: `visual-system.json` → `layout`, `space`, `radius`. Tokens: `--stave-gap-*`, `--space-*`, `--margin-screen`, `--print-safe`, `--print-bleed`.

## The stave is the grid

Every format has a stave gap token. The stave's five lines are the strongest horizontals on the surface, and
other elements align to them: type baselines or ink edges land on a line, blocks start on a line.

| Format | Size | Stave gap token | Margin |
| --- | --- | --- | --- |
| Front panel (RTE carton) | 70 × 120 mm + 3 mm bleed | `--stave-gap-front_panel` | `--print-safe` + 3 mm inner = 6 mm from trim |
| Poster | 1080 × 1440 px (3:4); A2 in print | `--stave-gap-poster` / `--stave-gap-poster_a2` | `--margin-screen` × width |
| Social | 1080 × 1350 px (4:5) | `--stave-gap-social` | same |
| Web band | full width | `--stave-gap-web` | 12 columns |

## Composition

- **Asymmetric, left-aligned.** Type starts on the left margin. The ember lives at the right end of the stave.
- **One stave per surface.** It crosses the full width into the bleed.
- **Scale contrast over decoration:** one very large element (焙曲, a numeral or the score) against very small mono
  data. Nothing medium-sized competing.
- **Empty paper is a feature.** At least a third of a surface is rice paper with nothing on it.
- **Radius 0** everywhere. Rules (hairlines) only to separate data blocks.

## Formats we do not have yet

Back panel, side panels, web page, deck. Build them from these rules and flag them for review.

## When the rules don't cover it

Put the stave first, at the format's gap, then remove things until the surface still reads.
