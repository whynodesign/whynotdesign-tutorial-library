#!/usr/bin/env python3
"""Procedural (NOT AI) assets: paper grain texture + swatch sheet. Also copies the dieline from test #85
and writes a dieline overlay with bleed / safe / panel names. Requires numpy, Pillow."""
import json, pathlib, shutil, re
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter
ROOT = pathlib.Path(__file__).resolve().parent.parent
V = ROOT / "brand/agent/visual"; A = V / "assets"
vs = json.loads((V / "visual-system.json").read_text(encoding="utf-8"))
# 1) grain: multi-scale noise + sparse fibres, neutral grey centred on 128, used at 5% multiply
rng = np.random.default_rng(17); S = 1024
n = rng.normal(0, 1, (S, S))
img = Image.fromarray(np.uint8(np.clip(128 + 18 * n, 0, 255))).filter(ImageFilter.GaussianBlur(0.6))
d = ImageDraw.Draw(img)
for _ in range(260):
    x, y = rng.uniform(0, S, 2); a = rng.uniform(0, np.pi); L = rng.uniform(6, 28)
    d.line([(x, y), (x + L * np.cos(a), y + L * np.sin(a))], fill=int(rng.uniform(95, 120)), width=1)
img.save(A / "textures/rice-paper-grain.png")
# 2) swatch sheet with proportion bar
C = vs["color"]; mono = str(V / "fonts/DMMono-Regular.ttf")
f = ImageFont.truetype(mono, 22); fs = ImageFont.truetype(mono, 16)
sheet = Image.new("RGB", (1600, 900), C["rice-paper"]["hex"]); d = ImageDraw.Draw(sheet)
x = 60
for k, c in C.items():
    d.rectangle([x, 60, x + 270, 520], fill=c["hex"], outline=C["kiln-char"]["hex"] if k == "rice-paper" else None)
    d.text((x, 540), k, font=f, fill=C["kiln-char"]["hex"])
    d.text((x, 575), c["hex"], font=fs, fill=C["kiln-char"]["hex"])
    d.text((x, 600), "CMYK est. " + "/".join(map(str, c["cmyk_estimate"])), font=fs, fill=C["kiln-char"]["hex"])
    d.text((x, 625), "Lab " + " ".join(map(str, c["lab_d50"])), font=fs, fill=C["kiln-char"]["hex"])
    d.text((x, 650), c["share"][:28], font=fs, fill=C["kiln-char"]["hex"])
    x += 300
# proportion bar: 65 / 24 / 10 / (celadon 0 in default) / 1
y0 = 720; total = 1480; x = 60
for k, p in (("rice-paper", .65), ("kiln-char", .24), ("oolong-amber", .10), ("ember-red", .01)):
    w = total * p; d.rectangle([x, y0, x + w, y0 + 80], fill=C[k]["hex"], outline=C["kiln-char"]["hex"]); x += w
d.text((60, 820), "default surface proportion 65 / 24 / 10 / 1  (celadon replaces part of rice-paper only on light-roast or secondary surfaces)", font=fs, fill=C["kiln-char"]["hex"])
d.text((60, 850), "CMYK = sRGB -> generic SWOP ICC estimate, NOT proofed. Concept only.", font=fs, fill=C["ember-red"]["hex"])
sheet.save(A / "swatches/swatch-sheet.png")
# 3) dieline from #85 (PolyForm Noncommercial output) + overlay
src = pathlib.Path("/workspace/tutorial-tests/85")
for n in ("toneroast_rte_70x45x120.svg", "toneroast_rte_70x45x120.dxf", "toneroast_rte_70x45x120.manufacturing.svg", "params_used.json"):
    if (src / n).exists(): shutil.copy(src / n, A / "dieline" / n)
raw = (A / "dieline/toneroast_rte_70x45x120.svg").read_text(encoding="utf-8")
vb = re.search(r'viewBox="([^"]+)"', raw).group(1); minx, miny, w, h = map(float, vb.split())
inner = raw.split(">", 2)[2].rsplit("</svg>", 1)[0] if raw.startswith("<?xml") else raw.split(">", 1)[1].rsplit("</svg>", 1)[0]
B = vs["layout"]["margins"]["print_bleed_mm"]; S_ = vs["layout"]["margins"]["print_safe_mm"]
panels = [("GLUE", -12, 0), ("FRONT 正面", 0, 70), ("SIDE A", 70, 115.45), ("BACK 背面", 115.45, 185.9), ("SIDE B", 185.9, 231.8)]
ov = []
for name, x0, x1 in panels[1:]:
    ov.append(f'<rect x="{x0-B}" y="{-B}" width="{x1-x0+2*B}" height="{120+2*B}" fill="none" stroke="#D8432B" stroke-width="0.25" stroke-dasharray="1.5 1"/>')
    ov.append(f'<rect x="{x0+S_}" y="{S_}" width="{x1-x0-2*S_}" height="{120-2*S_}" fill="none" stroke="#B03AA8" stroke-width="0.25"/>')
    ov.append(f'<text x="{(x0+x1)/2}" y="62" font-family="DM Mono, monospace" font-size="3.2" text-anchor="middle" fill="#1E1A17">{name}</text>')
ov.append(f'<text x="{minx+4}" y="{miny+h-14}" font-family="DM Mono, monospace" font-size="3" fill="#1E1A17">RTE 70x45x120 mm, 0.45 mm board. Source: open-dieline (test #85), PolyForm Noncommercial 1.0.0.</text>')
ov.append(f'<text x="{minx+4}" y="{miny+h-9}" font-family="DM Mono, monospace" font-size="3" fill="#1E1A17">Red dashed = bleed {B} mm, magenta = safe {S_} mm (overlay by TONEROAST kit). Front/back assignment to confirm with die-maker. NOT production.</text>')
out = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}mm" height="{h}mm" viewBox="{vb}">'
       f'<rect x="{minx}" y="{miny}" width="{w}" height="{h}" fill="#FFFFFF"/>{inner}<g id="OVERLAY">{"".join(ov)}</g></svg>')
(A / "dieline/dieline-overlay.svg").write_text(out, encoding="utf-8")
print("assets written")
