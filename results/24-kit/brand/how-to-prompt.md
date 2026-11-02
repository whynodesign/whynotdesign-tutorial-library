# How to prompt with this kit

This kit is written for an agent to read. Point one at the `brand/` folder and it has the brand: values,
rules and the reasons behind them. This file covers two jobs:
**A.** driving a coding/design agent with the kit, and **B.** prompting image and video models, which
cannot read files and need the kit translated into a prompt.

## A. Driving an agent

### Starting

> Read the TONEROAST brand kit in `brand/`. I am making the front panel for 焙次 No. 021, 焙度 3.
> Start with `magic_trick.md`, then follow the routing table in `readme.md`.

That is enough. Do not paste hex values or rules into the prompt and do not summarise the kit for
the agent. **The files are the brief.**

### What to expect

- **Iteration, not one shot.** Pass 1 gets the system right (stave, colours, voices). Composition takes
  two or three rounds. Plan for it.
- **Say the visual logic first.** Before content, say which reading of the stave the surface uses
  (symbol, level or score), the format and its stave gap token, and where the one headline goes.
  A topic alone gives you a generic beige page.
- **One application at a time.** Ask for one front panel, then one poster. Single applications beat
  3×3 "brand boards": every extra cell is one more place to get the mark or a string wrong.

### Prompts that work

> Build a front panel for 焙次 No. 021 at 焙度 3 using `product/components/label-front.html`.
> Use only strings from `agent/verbal/concepts.md`.

> Make a poster whose only image is the Roast Score of batch 018 (see `graphic-elements.md`).
> Headline 焙火如樂譜. Check the ember count before you show me.

> Check this layout against `magic_trick.md`. List every amber bar and the number it encodes.

### Prompts that do not

> Make it feel more premium. · Make it more Taiwanese. · Add some tea vibes. · Make it pop.

None of these names a file, token or rule, so the agent falls back on its own taste (which here means
leaves, mountains and gold). Ask against the system: name the token, the rule or the file.

### When the agent gets it wrong

Point at the rule, not the pixel. "The level bar must sit on line 3 counted from the bottom
(`magic_trick.md`, *Level is position, only*)" fixes the class of error. "Move the orange bar down"
fixes one file and the next one comes back wrong.

## B. Prompting image and video models

Image models cannot count lines, cannot set Chinese reliably, and copy whatever is on a reference
image. So we use the **D+B route**: the model makes a **text-free, mark-free base** (photography,
paper, material, light); code or Figma then sets the stave, the type and the logo with real fonts
(`product/components/*`). AI-rendered glyphs and AI-drawn marks are never final.

### Lessons this section encodes (from whynotdesign Exp07–Exp10)

1. **Text on the reference = text in the output.** Any string the model sees on a reference image can
   appear in the output, mixed with the prompt's strings. A whitelisted string must be **identical,
   character for character,** to the string on the anchor. Prefer no text at all in the model's output.
2. **What is not on the anchor gets dropped.** Any colour or application you want kept must appear once on
   `assets/anchor/anchor.png`. (Exp09: celadon was missing from the anchor and vanished from every board.)
3. **The anchor's layout leaks.** Tell the model to reproduce the identity, not the sheet.
4. **Single applications beat 3×3 boards.**
5. **Concrete, countable traits beat adjectives.** "Five equal straight lines, bars on line 3" survives;
   "musical, crafted, warm" turns into stock assets. Describe the *unusual* things about this brand,
   precisely, and loosen the layout instead.
6. **No font names in image prompts.** Describe stroke contrast, serif shape, width, weight, tracking.
   Real font names go only into code/Figma.
7. **Fail → rerun from the original inputs.** Don't patch a failed image with more edits.

### Template 1 — text-free base image (default; for packaging shots, poster grounds, social backgrounds)

```text
<TASK>
Create ONE text-free photographic base image, {{aspect e.g. 4:5}}, for a concept layout. The image
will have type and a graphic composited on top later, so it must contain NO letters, numbers, logos,
symbols, lines, stripes, bars or labels anywhere.
</TASK>
<SUBJECT>
{{one subject, e.g. a small matte charcoal-black rectangular paper carton, 70 x 45 x 120 mm, plain,
unprinted, standing on a rice-paper-coloured uncoated card surface}}.
</SUBJECT>
<LIGHT_AND_MATERIAL>
Soft directional daylight from the upper left, long gentle shadow, matte uncoated paper with fine
visible fibres, warm off-white (#EFE8DA) ground, deep warm charcoal (#1E1A17), one small area of
oolong amber (#A8642A) only if it is the tea liquor itself.
</LIGHT_AND_MATERIAL>
<COMPOSITION>
{{principle only, e.g. subject in the lower left third; the upper 45% of the frame is empty
paper of the same colour as the ground, with no objects}}.
</COMPOSITION>
<REFERENCE_ROLES>
Reference image 1 (the TONEROAST anchor) controls ONLY: the colour palette and its proportions,
the paper texture, the amount of empty space. It must NOT control layout, subject or content, and
nothing on it may be copied: no lines, bars, dots, text, logo or panels from it.
</REFERENCE_ROLES>
<NEGATIVE>
{{paste the negative list below}}
</NEGATIVE>
```

### Template 2 — single application concept (only when the studio asks for an all-AI concept)

```text
<ROLE>Senior packaging designer presenting ONE concept image. Concept only, not final artwork.</ROLE>
<TASK>Using reference image 1 (the approved TONEROAST anchor), show ONE {{front panel of a
70 x 45 x 120 mm carton | A2 poster | 4:5 social post}}, flat and front-on.</TASK>
<IDENTITY - from the anchor, do not reinterpret>
Five equal, perfectly straight, horizontal charcoal lines crossing the whole surface edge to edge.
ONE oolong-amber bar sitting on the {{third}} line counted from the bottom, starting about 40% from
the left and running off the right edge. ONE small ember-red dot above the top line near the right
edge. Nothing else is red. Nothing else is amber.
Large Chinese wordmark: high-contrast serif, bold, wedge serifs, set horizontally, below the lines.
Latin wordmark under it: wide geometric sans, medium weight, all caps, very wide letter-spacing.
Small data text: monospaced.
</IDENTITY>
<TEXT_ALLOWLIST>
Only these strings, exactly as written, nothing else: "焙曲" "TONEROAST" {{e.g. "焙度 3"}}
(These strings appear on the anchor in exactly this form.) If unsure, leave text out.
</TEXT_ALLOWLIST>
<REFERENCE_ROLES>
The anchor controls: mark geometry (5 lines, bar on a line, one dot), colours and proportions, the
type voices, paper texture, white space. It does NOT control: this image's layout or crop.
Do not copy the anchor sheet, its swatches or its panels. Reproduce the identity, not the sheet.
If the text and the anchor disagree, the anchor wins.
</REFERENCE_ROLES>
<NEGATIVE>{{negative list}}</NEGATIVE>
```
After generation: **re-set every string and redraw the stave in code** before anyone sees it as a proposal.

### Template 3 — video (5 s brand unit)

Do not ask a video model for the logo animation: `product/components/motion-unit.html` renders it
deterministically (`tools/render_motion.sh`). Use a video model only for **text-free atmosphere plates**:

```text
5 seconds, locked-off camera, no cuts. {{e.g. close-up of charcoal embers glowing softly under a
layer of fine white ash in a shallow roasting basket, dim warm light}}. Slow, almost still; the only
motion is {{the glow breathing slightly}}. No text, no logos, no hands, no faces, no smoke plumes,
no sparks flying, no tea leaves, no steam. Colours: deep warm charcoal #1E1A17, ember #D8432B only
in the coals, warm off-white #EFE8DA nowhere except ash. Leave the right 40% of the frame dark and empty.
```
Then composite the stave and wordmark from `motion-unit.html` over it in the edit.

> Hex values in these templates are copied from `agent/visual/visual-system.json` because models cannot read tokens. If they ever disagree, the JSON wins.

### Negative list (paste into every image/video prompt)

```text
No text, letters, numbers, Chinese characters, logos, watermarks or labels (unless allowlisted).
No tea leaves, fresh green leaves, tea plants, mountains, terraces, clouds, mist, waterfalls.
No teapots, gaiwans, tea cups held by hands, bamboo, lotus, cranes, koi, lanterns.
No ink-wash painting, brush calligraphy, seals or chops, red-and-gold, gold foil, bokeh sparkles.
No musical notes, clefs, sheet music, piano keys, sound waves, equalisers.
No steam, smoke swirls, flames, sparks.
No gradients, drop shadows, glossy 3D render, plastic look, mockup frame, stock-photo styling.
No extra lines, stripes, bars or dots (the graphic is composited later).
```

### QA checklist (run on every output before showing it)

Score each 1–5 and give one verdict: **APPROVED / CORRECTION REQUIRED / REJECT AND REGENERATE**.
For corrections, write a PRESERVE list and a CORRECT list.

1. **Text:** is there any text the model drew? (Must be none, or only allowlisted strings, character-exact.)
2. **Stave:** exactly 5 equal straight lines, edge to edge? (If the model drew them, reject; composite in code.)
3. **Level:** is the bar on the right line, counted from the bottom?
4. **Ember:** exactly one ember-red dot on the surface, not touching amber?
5. **Colour:** only the five colours; rice paper dominant; no gradient?
6. **Cliché check:** any item from the negative list?
7. **Anchor leak:** does any part copy a module of the anchor (swatch bar, level row, panel)?
8. **Stock-asset test:** cover the stave with your hand. If what is left could be any tea brand, the
   surface relies on the stave alone (fine) — but if it *with* the stave still looks like a template,
   the composition is generic: push scale contrast (huge numeral or huge 焙曲 vs tiny mono data).
9. **Type:** are all final strings set in code/Figma with real fonts?
10. **Licence note:** is the output flagged as concept, with AI-generated parts named?
