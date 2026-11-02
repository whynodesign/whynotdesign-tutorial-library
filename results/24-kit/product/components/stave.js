/* TONEROAST stave helpers. Every number is read from tokens.css (generated from visual-system.json).
   No values are hard-coded here except data passed in by the caller.  CONCEPT / EXAMPLE ONLY. */
(function () {
  const css = () => getComputedStyle(document.documentElement);
  const tok = (n) => css().getPropertyValue("--" + n).trim();
  const num = (n) => parseFloat(tok(n));
  const C = (n) => tok(n); // colour token
  // line n (1..5, from bottom): y of the line's top edge, inside a stave whose top line is at `top`
  const lineY = (n, top, gap) => top + (num("mark-lines") - n) * gap;

  /** Five full-width lines. opts: {x, top, width, gap, weight, color} */
  function lines(o) {
    let s = "";
    for (let n = 1; n <= num("mark-lines"); n++) {
      const y = o.crisp ? Math.round(lineY(n, o.top, o.gap)) : lineY(n, o.top, o.gap);
      const h = o.crisp ? Math.max(1, Math.round(o.weight)) : o.weight; // crisp: snap to whole px on screen
      s += `<rect x="${o.x || 0}" y="${y}" width="${o.width}" height="${h}" fill="${o.color}"/>`;
    }
    return s;
  }
  /** The ember dot, above the top line at the right end of the stave. */
  function ember(o) {
    const r = o.gap * num("mark-dot-r");
    return `<circle cx="${(o.x || 0) + o.width - r - (o.dotInset || 0)}" cy="${o.top - o.gap * num("mark-dot-offset")}" r="${r}" fill="${C("ember-red")}"/>`;
  }
  /** Roast-level note bar on line n. opts: {x, top, width, gap, weight, level, xStart?, xEnd?} */
  function levelBar(o) {
    const h = o.gap * num("mark-level-height");
    const x0 = (o.x || 0) + o.width * (o.xStart ?? num("mark-level-x-start"));
    const x1 = (o.x || 0) + o.width * (o.xEnd ?? 1);
    const y = lineY(o.level, o.top, o.gap) + o.weight / 2 - h / 2;
    return `<rect x="${x0}" y="${y}" width="${x1 - x0}" height="${h}" fill="${C("oolong-amber")}"/>`;
  }
  /** Standalone mark (signature or level) at a given pixel width. */
  function mark({ width = 240, level = null, reversed = false, small = null } = {}) {
    const k = width / num("mark-width"), gap = num("mark-line-gap") * k, top = num("mark-top-line-y") * k;
    const useSmall = small ?? width < num("mark-small-threshold-px");
    const weight = (useSmall ? num("mark-line-weight-small") : num("mark-line-weight")) * k;
    const H = num("mark-height") * k, line = reversed ? C("rice-paper") : C("kiln-char");
    let body = lines({ top, width, gap, weight, color: line, crisp: true });
    if (level) body += levelBar({ top, width, gap, weight, level });
    else { // signature: 3 equal bars stepping up through spaces 1-3 (see visual-system.json mark.signature_bars)
      [[0, .34], [.33, .67], [.66, 1]].forEach(([a, b], i) => {
        const y = lineY(i + 2, top, gap) + weight;
        body += `<rect x="${width * a}" y="${y}" width="${width * (b - a)}" height="${gap - weight}" fill="${C("oolong-amber")}"/>`;
      });
    }
    body += ember({ top, width, gap });
    return `<svg xmlns="http://www.w3.org/2000/svg" width="${width}" height="${H}" viewBox="0 0 ${width} ${H}">${reversed ? `<rect width="${width}" height="${H}" fill="${C("kiln-char")}"/>` : ""}${body}</svg>`;
  }
  /** The Roast Score: rounds as bars on their intensity line, rests as fixed gaps.
      data: {rounds:[{h, line}], rests:[days]} ; opts: {x, top, width, gap, weight, labels:true, labelColor} */
  function score(data, o) {
    const rest = o.gap * num("score-rest-gap");
    const n = data.rounds.length, totalH = data.rounds.reduce((a, r) => a + r.h, 0);
    const avail = o.width - rest * (n - 1);
    const h = o.gap * num("score-bar-height");
    let x = o.x || 0, s = "", lab = "";
    data.rounds.forEach((r, i) => {
      const w = avail * r.h / totalH, y = lineY(r.line, o.top, o.gap) + o.weight / 2 - h / 2;
      s += `<rect x="${x}" y="${y}" width="${w}" height="${h}" fill="${C("oolong-amber")}"/>`;
      if (o.labels !== false) {
        const ly = lineY(1, o.top, o.gap) + o.gap * 0.9;
        lab += `<text x="${x}" y="${ly}" font-family="${tok("font-mono").replace(/"/g, "'")}" font-size="${o.labelSize || 14}" fill="${o.labelColor || C("kiln-char")}" letter-spacing="0.08em">${i + 1} 回 · ${r.h} h</text>`;
        if (i < n - 1) lab += `<text x="${x + w + rest / 2}" y="${ly + (o.labelSize || 14) * 1.6}" text-anchor="middle" font-family="${tok("font-mono").replace(/"/g, "'")}" font-size="${(o.labelSize || 14) * 0.85}" fill="${o.labelColor || C("kiln-char")}" opacity="0.7">歇 ${data.rests[i]} 日</text>`;
      }
      x += w + rest;
    });
    return s + lab;
  }
  const params = new URLSearchParams(location.search);
  if (params.has("noflag")) document.addEventListener("DOMContentLoaded", () => document.body.classList.add("noflag"));
  window.TR = { tok, num, lineY, lines, ember, levelBar, mark, score, params };
})();
