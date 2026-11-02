#!/usr/bin/env python3
"""Lint the kit: generated files are fresh, Markdown carries no stray hex values, every logo has <= 1 ember,
every string on the anchor is in the whitelist. Exit 1 on failure."""
import json, pathlib, re, subprocess, sys, hashlib
R = pathlib.Path(__file__).resolve().parent.parent; V = R / "brand/agent/visual"; bad = []
h = lambda p: hashlib.md5(p.read_bytes()).hexdigest()
gen = [V / "tokens.css", V / "motion.json", R / "product/components/motion.js"]
before = [h(p) for p in gen]; subprocess.run([sys.executable, R / "tools/build_tokens.py"], check=True, capture_output=True)
if before != [h(p) for p in gen]: bad.append("generated files were stale (now regenerated) - commit them")
for md in (R / "brand").rglob("*.md"):
    if md.name in ("how-to-prompt.md",): continue
    for m in re.findall(r"#[0-9A-Fa-f]{6}\b", md.read_text(encoding="utf-8")): bad.append(f"hex {m} in {md.relative_to(R)} (name the token instead)")
ember = json.loads((V / "visual-system.json").read_text())["color"]["ember-red"]["hex"]
for svg in (V / "assets/logos").glob("*.svg"):
    n = svg.read_text().count(f'fill="{ember}"')
    if n > 1: bad.append(f"{svg.name}: {n} ember fills")
wl = (R / "brand/agent/verbal/concepts.md").read_text(encoding="utf-8")
anchor = (R / "product/components/anchor.html").read_text(encoding="utf-8")
for s in ["焙火如樂譜", "ROAST LIKE A SCORE", "炭焙烏龍 · CHARCOAL-ROASTED OOLONG", "焙次 No. 017 · 焙度 4 · 6 回"]:
    if s not in anchor: bad.append(f"anchor no longer shows '{s}' - update this check")
    if f"`{s}`" not in wl and s not in wl: bad.append(f"anchor string '{s}' missing from whitelist")
print("\n".join(bad) or "kit OK"); sys.exit(1 if bad else 0)
