#!/usr/bin/env python3
"""Generate every logo SVG in brand/agent/visual/assets/logos/ from visual-system.json.
Wordmarks are outlined from real OFL fonts (Noto Serif CJK TC Bold, Lexend Exa @500), so the
SVGs need no fonts installed. Requires: fontTools. Font paths below are this box's; edit FONT_* if needed."""
import json, pathlib
from fontTools.ttLib import TTFont, TTCollection
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.boundsPen import BoundsPen
from fontTools.pens.transformPen import TransformPen
from fontTools.varLib import instancer
ROOT = pathlib.Path(__file__).resolve().parent.parent
V = ROOT / "brand/agent/visual"; OUT = V / "assets/logos"; OUT.mkdir(parents=True, exist_ok=True)
vs = json.loads((V / "visual-system.json").read_text(encoding="utf-8"))
C = {k: v["hex"] for k, v in vs["color"].items()}
M = vs["mark"]; W, H, LW, G, TOP = M["width"], M["height"], M["line_weight"], M["line_gap"], M["top_line_y"]
FONT_CJK = ("/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc", "Noto Serif CJK TC")
FONT_LAT = V / "fonts/LexendExa-VariableFont_wght.ttf"
WORD_ZH, WORD_EN = "焙曲", "TONEROAST"

def line_y(n):  # top edge of line n counted from bottom (1..5)
    return TOP + (M["lines"] - n) * G

def stave(col, lw=LW, dx=0, dy=0):
    return [f'<rect x="{dx}" y="{dy+line_y(n)+(LW-lw)/2:.2f}" width="{W}" height="{lw}" fill="{col}"/>' for n in range(1, 6)]

def dot(col, dx=0, dy=0):
    r = G * M["ember_dot"]["radius_ratio_of_gap"]
    return f'<circle cx="{dx+W-r:.2f}" cy="{dy+TOP-G*M["ember_dot"]["cy_offset_above_top_line_ratio_of_gap"]:.2f}" r="{r:.2f}" fill="{col}"/>'

def sig_bars(col, dx=0, dy=0):
    b = []
    for space, (x0, x1) in zip(M["signature_bars"]["spaces_from_bottom"], M["signature_bars"]["x_ranges"]):
        y = line_y(space + 1) + LW  # space k sits between line k and k+1
        b.append(f'<rect x="{dx+W*x0:.2f}" y="{dy+y}" width="{W*(x1-x0):.2f}" height="{G-LW}" fill="{col}"/>')
    return b

def level_bar(n, col, dx=0, dy=0):
    h = G * M["level_bar"]["height_ratio_of_gap"]; x0 = W * M["level_bar"]["x_start"]
    y = line_y(n) + LW / 2 - h / 2
    return f'<rect x="{dx+x0:.2f}" y="{dy+y:.2f}" width="{W-x0:.2f}" height="{h:.2f}" fill="{col}"/>'

def svg(body, w, h, bg=None, title=""):
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w:.2f} {h:.2f}" width="{w:.0f}" height="{h:.0f}">',
         f'<title>{title} - TONEROAST concept, not final art</title>']
    if bg: s.append(f'<rect width="{w:.2f}" height="{h:.2f}" fill="{bg}"/>')
    return "\n".join(s + body + ["</svg>"]) + "\n"

# ---------- outlined text ----------
def load_fonts():
    cjk = next(f for f in TTCollection(FONT_CJK[0]).fonts if FONT_CJK[1] in f["name"].getDebugName(4))
    lat = instancer.instantiateVariableFont(TTFont(FONT_LAT), {"wght": 500})
    return cjk, lat
CJK, LAT = load_fonts()

def outline(font, text, tracking_em=0.0):
    """Return (list of (glyphname, x_offset)), ink bbox in font units (y up)."""
    gs = font.getGlyphSet(); cmap = font.getBestCmap(); upm = font["head"].unitsPerEm
    x = 0; items = []; bp = BoundsPen(gs)
    for i, ch in enumerate(text):
        g = cmap[ord(ch)]; items.append((g, x))
        tp = TransformPen(bp, (1, 0, 0, 1, x, 0)); gs[g].draw(tp)
        x += gs[g].width + (tracking_em * upm if i < len(text) - 1 else 0)
    return items, bp.bounds

def text_path(font, text, tracking_em, ink_top, ink_h=None, ink_w=None, x_left=0, col="#000"):
    """Place text so its ink box starts at x_left, top at ink_top, scaled to ink_h or ink_w."""
    items, (xmin, ymin, xmax, ymax) = outline(font, text, tracking_em)
    s = ink_h / (ymax - ymin) if ink_h else ink_w / (xmax - xmin)
    gs = font.getGlyphSet(); paths = []
    for g, ox in items:
        pen = SVGPathPen(gs)
        # font y-up -> svg y-down: y' = ink_top + (ymax - y)*s
        tp = TransformPen(pen, (s, 0, 0, -s, x_left + (ox - xmin) * s, ink_top + ymax * s)); gs[g].draw(tp)
        paths.append(pen.getCommands())
    return f'<path fill="{col}" d="{" ".join(paths)}"/>', (xmax - xmin) * s, (ymax - ymin) * s

files = {}
# ---------- symbol ----------
def symbol(line_col, bar_col, dot_col, bg=None, lw=LW):
    return stave(line_col, lw) + sig_bars(bar_col) + [dot(dot_col)]
files["symbol-char.svg"] = svg(symbol(C["kiln-char"], C["oolong-amber"], C["ember-red"]), W, H, title="Symbol")
files["symbol-reversed.svg"] = svg(symbol(C["rice-paper"], C["oolong-amber"], C["ember-red"]), W, H, bg=C["kiln-char"], title="Symbol reversed")
files["symbol-mono-char.svg"] = svg(symbol(C["kiln-char"], C["kiln-char"], C["kiln-char"]), W, H, title="Symbol mono char")
files["symbol-mono-paper.svg"] = svg(symbol(C["rice-paper"], C["rice-paper"], C["rice-paper"]), W, H, bg=C["kiln-char"], title="Symbol mono paper")
files["symbol-char-small.svg"] = svg(symbol(C["kiln-char"], C["oolong-amber"], C["ember-red"], lw=M["line_weight_small"]), W, H, title="Symbol small")
files["symbol-reversed-small.svg"] = svg(symbol(C["rice-paper"], C["oolong-amber"], C["ember-red"], lw=M["line_weight_small"]), W, H, bg=C["kiln-char"], title="Symbol reversed small")
# ---------- roast levels ----------
for n in range(1, 6):
    files[f"level-{n}.svg"] = svg(stave(C["kiln-char"]) + [level_bar(n, C["oolong-amber"]), dot(C["ember-red"])], W, H, title=f"Roast level {n}")
    files[f"level-{n}-reversed.svg"] = svg(stave(C["rice-paper"]) + [level_bar(n, C["oolong-amber"]), dot(C["ember-red"])], W, H, bg=C["kiln-char"], title=f"Roast level {n} reversed")
# ---------- wordmark + lockups ----------
TR = vs["type"]["families"]["wordmark-latin"]["tracking_em"]
def wordmark_block(x0, top, zh_h, gap_between, col):
    zh, zw, zh_ = text_path(CJK, WORD_ZH, 0.08, top, ink_h=zh_h, x_left=x0, col=col)
    # TONEROAST fitted to the same ink width as 焙曲
    _, (a, b, c, d) = outline(LAT, WORD_EN, TR)
    en_h = zw * (d - b) / (c - a)
    en, ew, eh = text_path(LAT, WORD_EN, TR, top + zh_h + gap_between, ink_w=zw, x_left=x0, col=col)
    return [zh, en], zw, zh_h + gap_between + eh, eh

def horizontal(line_col, word_col, bg=None):
    # 焙曲 ink: top of line 5 -> bottom of line 2.  TONEROAST: baseline on bottom edge of line 1.
    x0 = W + G; zh_top = line_y(5); zh_h = line_y(2) + LW - line_y(5)
    zh, zw, _ = text_path(CJK, WORD_ZH, 0.08, zh_top, ink_h=zh_h, x_left=x0, col=word_col)
    _, (a, b, c, d) = outline(LAT, WORD_EN, TR); en_h = zw * (d - b) / (c - a)
    en, _, _ = text_path(LAT, WORD_EN, TR, line_y(1) + LW - en_h, ink_w=zw, x_left=x0, col=word_col)
    body = symbol(line_col, C["oolong-amber"], C["ember-red"]) + [zh, en]
    return svg(body, x0 + zw, H, bg=bg, title="Lockup horizontal"), en_h

files["lockup-horizontal.svg"], en_h_h = horizontal(C["kiln-char"], C["kiln-char"])
files["lockup-horizontal-reversed.svg"], _ = horizontal(C["rice-paper"], C["rice-paper"], bg=C["kiln-char"])

def stacked(line_col, word_col, bg=None):
    body = symbol(line_col, C["oolong-amber"], C["ember-red"])
    wb, zw, bh, _ = wordmark_block(0, H + G, W * 0.48, G * 0.5, word_col)
    # centre wordmark under the mark
    shift = (W - zw) / 2
    body += [f'<g transform="translate({shift:.2f} 0)">' + "".join(wb) + "</g>"]
    return svg(body, W, H + G + bh, bg=bg, title="Lockup stacked")
files["lockup-stacked.svg"] = stacked(C["kiln-char"], C["kiln-char"])
files["lockup-stacked-reversed.svg"] = stacked(C["rice-paper"], C["rice-paper"], bg=C["kiln-char"])
wb, zw, bh, _ = wordmark_block(0, 0, 120, 18, C["kiln-char"])
files["wordmark.svg"] = svg(wb, zw, bh, title="Wordmark 焙曲 TONEROAST")
# ---------- clear space diagram ----------
pad = G; body = [f'<rect x="0" y="0" width="{W+2*pad}" height="{H+2*pad}" fill="none" stroke="{C["ember-red"]}" stroke-width="1" stroke-dasharray="4 4"/>',
                 f'<rect x="{pad}" y="{pad}" width="{W}" height="{H}" fill="none" stroke="{C["celadon-grey"]}" stroke-width="1"/>']
body += [f'<g transform="translate({pad} {pad})">' + "".join(symbol(C["kiln-char"], C["oolong-amber"], C["ember-red"])) + "</g>"]
body += [f'<rect x="0" y="{pad+line_y(5)}" width="{pad}" height="{G}" fill="{C["celadon-grey"]}" opacity="0.6"/>']
files["clear-space.svg"] = svg(body, W + 2 * pad, H + 2 * pad, bg=C["rice-paper"], title="Clear space = 1 line gap")
for name, s in files.items(): (OUT / name).write_text(s, encoding="utf-8")
print(len(files), "files ->", OUT)
