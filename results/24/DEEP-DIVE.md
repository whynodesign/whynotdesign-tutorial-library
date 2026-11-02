# #24 深挖：Little Plains「Agentic Brand Systems」到底是什么

> 调研时间：2026-11-01（PT）。引文均为原文照抄，每条附链接。读不到的内容在第 4 节写明。
> 相关：我们的实测 [RESULT.md](RESULT.md)｜原帖 https://x.com/emmettshine/status/2024113482623258907 ｜站点 https://agentic.littleplains.com/

## 0. 先说结论：这是怎么回事

- **两篇东西，同一家公司，相隔 7 个月：**
  - **2026-02-18**：@emmettshine（Emmett，Little Plains 创始人，简介 "designer | founder: @littleplainsxo | @ginlane | 50+ launched startups, 7 exits"）发了 X 长文《A Guide to Building Brands for Humans & Agents》。我们 #24 测的就是这篇，讲的是「约 400 token 一块的 YAML/MD chunk + 检索规则」。
    - 原帖：https://x.com/emmettshine/status/2024113482623258907
    - 同文网页版：https://littleplains.com/writings/building-brand-systems-for-humans-and-agents-today
  - **2026-09-30**：Little Plains 上线 https://agentic.littleplains.com/ （标题 "Agentic Systems Are the Future of Brands"）。
    - 同日 X 长文：https://x.com/littleplainsxo/status/2105274281110196509
    - Emmett 的转发：https://x.com/emmettshine/status/2105275712135655654 （653 赞 / 1033 收藏）
    - 这是**升级版**：交付物不再是 YAML chunk，而是一个 git 仓库，里面是 Markdown 规则、一份 `visual-system.json`、由它生成的 `tokens.css`、字体/Logo/图片素材、React 组件，再配一份 PDF 规范。站点用真实客户 **Sonata**（sonata.health）的 kit 做展示。
- **性质：付费代理商服务的展示和营销页，不是开源工具。**
  - 9 月 26 日 Emmett 预告过 "open source a big drop"（https://x.com/emmettshine/status/2103639357836148913 ）。
  - 但实际放出来的是：
    - 站点上可以浏览的 Sonata kit 文件内容；
    - 文章里的示例。
  - **没有下载包，没有公开仓库：**
    - GitHub 组织 `Little-Plains` 的 public_repos 为 0（https://github.com/Little-Plains ）。
    - 站内截图显示仓库是 "little-plains / sonata-brand Private"。
  - 联系方式："Let's Talk… hello@littleplains.co"。

## 1. 解决什么问题

- **品牌资料散落在各个工具里，人和 AI 各用各的版本。** 站点原文：
  > "The thinking is in a strategy deck, the logo is in Air, the interface is in Figma, the techniques are in Flora, the campaign is in Canva, and the live product is in code."
  > "Everyone is trying to do good work. They are just working from different versions of the company."
  — https://agentic.littleplains.com/
- **交付以后客户天天回来问。** 原文：
  > "After project completion, their team sent us good questions almost every day. How should a hover state behave? Do these tokens map to Figma variables?… Each question exposed a decision that had been made during the work but had not made it into the handoff."
  — https://agentic.littleplains.com/
- **目标是让客户离开他们也能运转：**
  > "Our test is simple: the client should be able to operate without us."
  — https://agentic.littleplains.com/
- **为什么不交 PDF 或 PNG：**
  > "a flat raster export — PNG, JPEG, PDF — can be looked at but not built from"
  — https://littleplains.com/writings/the-html-brand-the-rise-of-input-based-outcomes

## 2. 步骤拆解（他们实际怎么做和交付）

1. **每个品牌单独设计 kit，不套模板。**
   > "At Little Plains, we do not have one standard kit for every brand."
   — https://agentic.littleplains.com/
2. **kit 写明每条规则的理由。**
   > "At Little Plains, we deliver kits as part of each engagement. They contains the brand's positioning and voice, the visual rules and assets, and the components people use to make new work. Importantly, the system explains why each rule exists, where they applies, and how to make a call when the guidelines don't cover it."
   — https://agentic.littleplains.com/
3. **数值只存在一个地方。** 视觉数值写进 JSON，CSS 由 JSON 生成，Markdown 里只按 token 名引用：
   > "On the visual side, `visual-system.json` holds the color, type, spacing, radius, and effects values. Those values generate `tokens.css`… Beside the brand kit is a product kit with real React components"
   — https://agentic.littleplains.com/
   > "`agent/visual/visual-system.json` is authoritative for every visual value… `tokens.css` is generated from it… The markdown files carry rules and reasoning, and name values by token only. That split is deliberate: a value lives in exactly one place, so a hex in a document can never drift from the hex in the code."
   — Sonata kit `brand/readme.md`（站内可读，来自 https://agentic.littleplains.com/ 页面加载的 `data/sonata-kit.js`）
   - `tokens.css` 第一行是 "/* Generated from visual-system.json by tools/gen-tokens.py. Do not edit…"
4. **用一个「magic trick」文件讲清品牌的招牌手法。** Sonata 的是花：
   > "# The flower becomes the room… One image doing two jobs, on a timer."
   - 文件里的硬规则包括 "**One flower per surface.**" 和 "**Never recolor it.**"（`brand/magic_trick.md`）
5. **附一份怎么给 AI 下指令的说明**（`brand/how-to-prompt.md`）：
   > "Read the Sonata brand kit in `brand/`. I am making a landing page for the Essential care plan. Start with `magic_trick.md` and `agent/verbal/`."
   > "Do not paste the tokens into the prompt… The files are the brief."
   > "**Iteration, not one shot.**"
   > "Point at the rule, not at the pixel."
   - 文件列出了没用的指令，例如 "Make it feel more premium."；最后有 7 个自查问题，例如 "does the page have its pause bands?"
6. **交付前用「全新的 agent」做 QA。**
   > "For QAing before we hand over a kit, we give the file to a fresh agent with no other project context and ask it to make something new."
   > "Don't one-shot a generative kit and expect production grade outputs!"
   — https://agentic.littleplains.com/
7. **交付内容和存放方式。**
   > "At handoff, the client gets the source files, the usable components, a way to browse the system, documentation, and training in the tools their team uses."
   — https://agentic.littleplains.com/
   - Emmett 回答「存在哪」：
     > "The entire system lives in a git repo of files: md files for verbal, JSON for tokens, React for components. And then any agent can pull from and build from this!"
     — https://x.com/emmettshine/status/2105369253121601577
8. **周期和定价。**
   - 周期从 12 周压到约 4 周的 sprint（见 https://littleplains.com/writings/the-html-brand-the-rise-of-input-based-outcomes ）。
   - 定价原文 "hybrid: scoped time and materials on the front end, ongoing licensing"（同上）。
   - Emmett 9 月的回复：
     > "pricing structure tbh we are testing with every week… We are not a software company but we are also not not selling software … tbd where this goes"
     — https://x.com/emmettshine/status/2105291577749094887

## 3. 工具和参数原文

### Sonata kit 目录（站内 `data/sonata-kit.js` 列出 52 个文件）

- `brand/readme.md`、`brand/how-to-prompt.md`、`brand/magic_trick.md`
- `brand/agent/verbal/`：`concepts.md`、`positioning.md`、`voice-and-tone.md`
- `brand/agent/visual/`：
  - 规则文档：`art-direction.md`、`brandmark.md`、`color.md`、`effects.md`、`graphic-elements.md`、`layout.md`、`motion.md`、`typography.md`
  - 数值与样式：`visual-system.json`、`tokens.css`、`motion.json`、`fonts.css`
  - `fonts/`：EB Garamond、Funnel Sans、JetBrains Mono，woff2 格式
  - `assets/`：logos 6 个 svg；imagery 3 张花的 webp；icons
- `product/src/components/`：Badge、Band、Bullet、Button、Card、Checkbox、Dropdown、NumberBullet、ProgressBar、PromoCode、ScrollCue、ScrollRail、Stages、TextField、Toggle（共 15 个 .tsx）

### readme 怎么写

- 适用范围：
  > "packaged to drop into Claude, Claude Code, or Cursor and build from: landing pages, campaigns, social, one-sheets, decks."
- 配套交付：
  > "Its sibling is the **product kit**… The **guidelines PDF**…"
- 不需要运行任何东西：
  > "There is nothing to run here. The kit is a set of files…"
- 有一张 "| You are writing | Read |" 路由表：
  - 写文案 → `agent/verbal/`，再看 `typography.md`
  - 做版式 → `layout.md`、`color.md`、`effects.md`
  - 用花 → `art-direction.md`、`motion.md`
  - 用 Logo → `brandmark.md`
- 字体许可写明：
  > "All three are SIL Open Font License 1.1 with no embedding restriction… They can be self-hosted and redistributed with what you build."

### token 写法

`tokens.css` 原文片段：`--white: #FFFFFF; --black-900: #2B2B2B; --cosmic-latte-100: #FFF8E7;`

### 定位文件

`positioning.md` 原文：
> "Sonata is a concierge medical practice and health technology company, built from scratch for the AI era. Sonata is your doctor, not a dashboard and not a disclaimer."
> "## Essence > We've got your back."

### 9 月文章里的目录结构（另一个客户 Type 的例子）

- `brand_atomic_system/`
  - `readme.md`、`magic_trick.md`、`human/`
  - `agent/verbal/{positioning.md, audience.yaml, messaging.md, differentiation.md, concepts.md, voice.md}`
  - `visual/{colors_and_type.css, fonts/ ← 5 OTFs, assets/, components/ ← 11 UI primitives, tokens/ ← 25 token specimens, motion/ (JSON, CSS)}`
  - `artifacts/web`、`artifacts/product`
- 文章原话 "An atomic kit is a brand world model."，并说明 "This is pretty new for us and in part pushed by what's possible through Claude Design"
- 来源：https://littleplains.com/writings/the-html-brand-the-rise-of-input-based-outcomes

### 2 月版本（我们 #24 测的那套）

- chunk 写法：
  - frontmatter 字段：`chunk_id / domain / category / subcategory / context_tags / depends_on / token_count: 380 / format / version / last_updated / status / summary`
  - 每块 "approximately 400 tokens each"，一套 "typically includes 15-20 chunks"
- `_retrieval-rules.yaml` 的 token_budget：website_copy 2000、blog_post 1800、social_media 1400
- 来源：https://littleplains.com/writings/building-brand-systems-for-humans-and-agents-today ，及原帖 https://x.com/emmettshine/status/2024113482623258907

### 和 Claude Code、Figma、MCP 的关系

- 2 月文章：
  > "Figma introduced Claude Code integration… your team creates in Claude Code using your structured brand files, sends it to Figma, your designer refines it on the canvas, then brings it back to code with Figma MCP."
- 9 月的站点：
  - 正文里没有出现 MCP 或 Claude Code。
  - 只演示了 kit 交给 agent 后做页面（"A founder put one of our kits into Cursor and asked it to make a landing page. The result used the right type, motion, interaction states, and voice."）。
  - 有一个 apply-system 动画，演示 agent 按规则排 Figma 画框。
- 结论：**没有专门的 MCP 服务或插件**。做法就是把文件夹交给 Claude、Cursor 等 agent 去读，Figma 只是来回编辑的一环。

### Flora

站点原文：
> "We're working with the talented team at Flora… new release from them coming next month."

另有 Emmett 介绍他们怎么用 Flora 的短片：https://x.com/emmettshine/status/2110802611394040228

## 4. 讲清的、省略的、可能夸大的

**讲清了：**
- 文件分工：Markdown 写规则和理由，JSON 是唯一数值来源，CSS 由 JSON 生成，另有 React 组件。
- 怎么下指令、怎么做 QA。
- Sonata 的大部分 kit 原文在站内能直接读到：31 个文本摘录里 29 个标记为完整（"more":false）。

**省略了、读不到的：**
- `visual-system.json`、`motion.json` 不在站内摘录里。直接访问 `https://agentic.littleplains.com/brand/agent/visual/visual-system.json` 返回 404。
- `concepts.md` 和 `positioning.md` 只给了前半段（"more":true，原文分别是 238 行和 69 行）。
- 字体、Logo、花图都只列了文件名，读不到文件本身。
- `tools/gen-tokens.py`（生成 token 的脚本）没有公开。
- 仓库 sonata-brand 是 Private，`gh api repos/little-plains/sonata-brand` 返回 404。
- guidelines PDF 读不到。
- 2 月文章里 12 个内部 agent 的完整文件也没有公开，只展示了 Donna 的 identity、soul、principles 片段。

**和宣传有出入的地方：**
- 9 月 26 日说 "open source a big drop"，实际是「公开展示内容」，没有许可证，也没有可下载的仓库。8 月 18 日也说过 "we're going to open-source a lot of how we built this tomorrow!"（https://x.com/emmettshine/status/2089731077652750671 ）。
- 400 token 是经验值，文章没有给出依据。
- 有读者质疑落地一致性。@leejdavies：
  > "I've spotted a fair few inconsistencies in application within seconds of visiting Sonata… Is all output agentic or overseen?"
  — https://x.com/leejdavies/status/2105404122820129274
  Emmett 回复：
  > "A lot is now being iterated and done by the in house team… it's an imperfect art still!"
  — https://x.com/emmettshine/status/2105416530326323366
- 也有人认为 Markdown 不够约束。@micka_design：
  > "I'm not sure .md file are enough. We're exploring translating design system .md rules into lint rules now."
  — https://x.com/micka_design/status/2024994126459191492

**我们的实测和真版的差距：**
- 我们按 2 月版做的是 YAML chunk 加检索规则，跑通了，产出了 1 张罐标图和 1 段文案。
- 真版（9 月）的重心已经转到：
  - 视觉 token 做到可以直接用的程度：JSON 加生成的 CSS；
  - 素材和组件可以直接拿来用；
  - readme 路由、magic_trick 和 how-to-prompt 这三份「操作说明」。
- 我们的 `identity/visual-system.json` 只是占位，没有做出 token、CSS、组件和素材，这是最大的差距。

## 5. 对 whynotdesign 的用法（自建版本）

做法：给每个客户交付一个「品牌 kit 仓库」，和 PDF 规范一起交。以焙曲为试点，目录如下：

```
brand/
  readme.md            # 作用：路由表（写文案/做包装/做海报/用 Logo 分别读哪些文件）+ 字体许可
  magic_trick.md       # 品牌的一个招牌手法 + 硬规则（例如「一面只放一个主图形」「不改色」）
  how-to-prompt.md     # 示范指令、无效指令、自查问题
  agent/verbal/        # positioning.md、voice-and-tone.md、concepts.md（中英双语）
  agent/visual/
    visual-system.json # 唯一数值来源：色值要同时写 HEX、CMYK、Pantone，另有字号、间距、圆角
    tokens.css         # 由 tools/gen-tokens.py 生成，禁止手改
    packaging.md       # 我们独有：刀模尺寸、出血、印刷工艺、材质、条码和法规信息区
    typography.md、color.md、layout.md、brandmark.md、art-direction.md
    assets/            # svg Logo、图形元素、产品图
    fonts/             # 只放可商用、可分发的字体，并附许可文件
tools/gen-tokens.py
```

**步骤：**
1. 把焙曲现有的 chunk 内容合并成上面的 Markdown 文件。
2. 写 `visual-system.json`，以及一个约 30 行的 `gen-tokens.py`。
3. 用「全新 agent、零上下文」做 QA：让它出 1 张罐标图、1 个落地页、1 条社媒文案，按自查问题打分。
4. 放进私有 GitHub 仓库交给客户，配一次培训。

**中文场景要注意：**
- 中文字体授权必须写进 readme。站酷、思源这类可分发，方正、汉仪通常不能随 kit 分发。
- 包装色值以 CMYK 和专色为准，屏幕 HEX 只作参考。

**商业上：** 可以学他们的定价方式，前期按范围收费，后期按年收 kit 的维护和授权费（"ongoing licensing"）。

## 6. 一句结论

**值得试。** 2 月的 chunk 法我们已经跑通。真正有价值的是 9 月这版的结构：数值只存在 JSON 一处，readme 做路由，magic_trick 讲招牌手法，how-to-prompt 教怎么下指令，交付前用全新 agent 做 QA。这些在站内基本能读到原文，可以照着给焙曲做一版完整 kit。但它**不是开源工具，也没有可下载的模板**，本质是 Little Plains 的付费交付物展示。
