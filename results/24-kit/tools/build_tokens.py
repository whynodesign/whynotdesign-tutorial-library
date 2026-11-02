#!/usr/bin/env python3
"""Generate brand/agent/visual/tokens.css and motion.json from visual-system.json.
Usage: python3 tools/build_tokens.py   (from the kit root). No dependencies."""
import json, pathlib
ROOT = pathlib.Path(__file__).resolve().parent.parent
V = ROOT / "brand/agent/visual"
vs = json.loads((V / "visual-system.json").read_text(encoding="utf-8"))
out = ["/* Generated from visual-system.json by tools/build_tokens.py. Do not edit.",
       "   Change the value in visual-system.json and regenerate, so the two never disagree.",
       "   CONCEPT / EXAMPLE ONLY - fictional brand 焙曲 / TONEROAST. */", "", ":root {"]
def sec(t): out.append(f"\n  /* {t} */")
def var(k, v): out.append(f"  --{k}: {v};")
sec("color")
for k, c in vs["color"].items():
    var(k, c["hex"])
    r, g, b = (int(c["hex"][i:i+2], 16) for i in (1, 3, 5)); var(k + "-rgb", f"{r} {g} {b}")
sec("type families")
fallback = {"display-cjk": '"Noto Serif CJK TC", "Source Han Serif TC", serif',
            "body-cjk": '"Noto Sans CJK TC", "Source Han Sans TC", sans-serif',
            "wordmark-latin": "sans-serif", "mono": '"Noto Sans TC", "Noto Sans CJK TC", ui-monospace, monospace'}
for k, f in vs["type"]["families"].items():
    var(f"font-{k}", f'"{f["family"]}", {fallback[k]}'); var(f"weight-{k}", f["weight"])
var("tracking-wordmark", f'{vs["type"]["families"]["wordmark-latin"]["tracking_em"]}em')
sec("type scale (px)")
for k, s in vs["type"]["scale_px"].items():
    var(f"text-{k}-size", f'{s["size"]}px'); var(f"text-{k}-line", s["line"])
    var(f"text-{k}-tracking", f'{s["tracking_em"]}em'); var(f"text-{k}-family", f'var(--font-{s["family"]})')
sec("type scale (print pt)")
for k, s in vs["type"]["scale_print_pt"].items():
    if not k.startswith("_"): var(f"print-{k}", f"{s}pt")
sec("space")
for i, s in enumerate(vs["space"]["scale"]): var(f"space-{i}", f"{s}px")
sec("radius / effects")
var("radius", f'{vs["radius"]["all"]}px'); var("shadow", vs["effects"]["shadow"])
var("grain-opacity", vs["effects"]["paper_grain"]["opacity"])
sec("mark geometry (ratios of mark width / line gap)")
m = vs["mark"]
for k in ("width", "height", "lines", "line_weight", "line_gap", "top_line_y", "line_weight_small"): var(f"mark-{k.replace('_','-')}", m[k])
var("mark-level-x-start", m["level_bar"]["x_start"]); var("mark-level-height", m["level_bar"]["height_ratio_of_gap"])
var("mark-dot-r", m["ember_dot"]["radius_ratio_of_gap"]); var("mark-dot-offset", m["ember_dot"]["cy_offset_above_top_line_ratio_of_gap"])
var("mark-min-px", f'{m["min_size"]["screen_px_width"]}px'); var("mark-small-threshold-px", f'{m["small_threshold_px"]}px')
sec("score")
var("score-bar-height", vs["score"]["round_bar_height_ratio_of_gap"]); var("score-rest-gap", vs["score"]["rest_gap_ratio_of_gap"])
sec("layout")
for k, v in vs["layout"]["stave_gap_px"].items(): var(f"stave-gap-{k}", f"{v}px")
for k, v in vs["layout"]["stave_gap_mm"].items(): var(f"stave-gap-{k}", f"{v}mm")
var("margin-screen", vs["layout"]["margins"]["screen_ratio_of_width"])
var("print-safe", f'{vs["layout"]["margins"]["print_safe_mm"]}mm'); var("print-bleed", f'{vs["layout"]["margins"]["print_bleed_mm"]}mm')
sec("motion")
mo = vs["motion"]
var("fps", mo["fps"])
for k, v in mo["duration_ms"].items(): var(f"dur-{k.replace('_','-')}", f"{v}ms")
for k, v in mo["easing"].items(): var(f"ease-{k}", v)
for k, v in mo["stagger_ms"].items(): var(f"stagger-{k.replace('_','-')}", f"{v}ms")
sp = mo["spring"]["note_land"]; var("spring-stiffness", sp["stiffness"]); var("spring-damping", sp["damping"]); var("spring-mass", sp["mass"])
out.append("}\n")
(V / "tokens.css").write_text("\n".join(out), encoding="utf-8")
motion = {"_generated": "from visual-system.json by tools/build_tokens.py - do not edit", **mo}
(V / "motion.json").write_text(json.dumps(motion, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
(ROOT / "product/components/motion.js").write_text("/* Generated from visual-system.json by tools/build_tokens.py - do not edit */\nwindow.MOTION = " + json.dumps(mo, ensure_ascii=False) + ";\n", encoding="utf-8")
print("wrote", V / "tokens.css", "and", V / "motion.json", f"({len(out)} lines css)")
