# Graphic elements

There is one graphic system — the stave — and four elements on it. Code: `product/components/stave.js`.

## 1 · The stave
Five equal straight lines at the format's gap (`layout.md`). Weight: `mark.line_weight` scaled with the gap
(screen ≈ 3 px at 48–72 px gap; print ≈ 0.35 mm at 6 mm gap).

## 2 · The note bar (level)
One amber bar on line *n* = 焙度 *n*. Height = `mark.level_bar.height_ratio_of_gap` × gap. On a front panel it may
run off the right edge.

## 3 · The Roast Score (batch)
The batch log as notes (`visual-system.json` → `score`):
- one bar per round, on the line of that round's intensity (1–5);
- width proportional to the round's hours across the space left after rests;
- rests are fixed gaps (`score.rest_gap_ratio_of_gap` × gap) labelled `歇 n 日` in mono; never scaled by duration;
- round labels `n 回 · h h` under line 1, in mono;
- at most `score.max_rounds_drawn` rounds;
- the data must be real on a real product (all example data here is fictional).

## 4 · The ember
One dot, `mark.ember_dot` geometry, above the top line at the stave's right end, one per surface.

## When the rules don't cover it
If an element is not one of these four, it probably does not belong.
