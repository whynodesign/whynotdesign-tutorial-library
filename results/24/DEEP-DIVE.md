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

---

## 作者 X 上的其他相关内容（2026-11-01 PT 补充）

> **范围：** 只读，用 x 工具读取，没有发帖、回复、点赞、关注或私信。
> - @emmettshine 的原创帖：116 条，覆盖 2025-12-09 到 2026-10-30，时间线接口最早只返回到 2025-12。
> - 他的回复：用关键词搜了约 45 条。
> - 公司号 @littleplainsxo（https://x.com/littleplainsxo ，简介 "We're a branding and experience design studio for consumer-centric, tech-enabled startups, based out of New York."）：39 条。
> - 三篇核心长文的引用帖：58 条。
> - 话题搜索（"agentic brand system"、"Little Plains" 等）和单帖展开若干。
> - 合计读了 **291 条不重复的帖子**，以及 **10 篇 X 长文全文**（其中 Emmett 和 Little Plains 的 6 篇）。
> - **保留 24 条有方法内容的**，按主题分组如下。纯宣传、致谢名单、生活帖、招聘帖都跳过了。
> - 引文照抄原文（含原文的拼写错误）。每条后面一行写它对 whynotdesign 有什么用。

### 1. 解决什么问题（作者在 X 上补充的角度）

1. **2026-01-22**｜长文《I Went to Harvard to Talk About AI & Branding》｜https://x.com/emmettshine/status/2014335297849266593
   > "You can’t ask a general system for a specialized outcome without giving it the world in which it operates. Context isn’t overhead. It’s leverage."
   - 用处：说明 kit 的价值在于提供「上下文」，不在模板本身。可以直接用作 whynotdesign 对客户解释 kit 的话术。
2. **2026-09-30**｜长文《Agentic Systems Are the Future of Brands》（X 版）｜https://x.com/littleplainsxo/status/2105274281110196509
   > "Give the same assignment to an agent and it guesses at a much higher rate. The result may look completely competent. However, each unsupported choice moves the work a little closer to what a generic product would do. It’s not slop, it’s just…mid."
   - 用处：kit 要防的不是「AI 垃圾」，而是平庸。这也是我们做包装 kit 时最该防的问题。

### 2. 步骤拆解和工具参数原文（按主题）

#### A. kit 结构和组件格式（新内容最多）

3. **2026-06-03**｜回答 @cicadadesign「组件是 HTML 还是 React」｜https://x.com/emmettshine/status/2062177524512072134
   > "In the kit, components live as HTML/CSS/SVG as the source-of-truth reference, because that’s the format an agent can read and build from in any environment. For product, we then have the agent convert to React (or Vue, etc.) on output. The HTML version is the spec, the React version is the build ~"
   - 用处：**会改我们的计划**。组件先写成 HTML/CSS/SVG 作为规格，React 只是产出物。包装和印刷物没有 React，用 HTML+SVG 就够了。
4. **2026-06-05**｜回答 @7x7er「组件属性怎么写」｜https://x.com/emmettshine/status/2062745820265345191
   > "Web Components are more technically correct, but plain HTML is more legible to an agent reading the kit cold. Component properties live alongside as a tokens.json (the variable knobs) and a usage.md (the rules). The agent reads all three together when generating 🙏"
   - 用处：给出了每个组件的三件套：`component.html` + `tokens.json` + `usage.md`。可以直接套到「罐标」「外箱」「吊牌」这类包装组件上。
5. **2026-09-30**｜回答 @timscullin「系统存在哪」｜https://x.com/emmettshine/status/2105369253121601577
   > "The entire system lives in a git repo of files: md files for verbal, JSON for tokens, React for components. And then any agent can pull from and build from this!"
   - 用处：交付载体是 git 仓库。注意它和第 3 条（HTML 是规格）是不同阶段的说法：9 月的 Sonata kit 确实带 React 组件。
6. **2026-09-30**｜回答 @faris「这只是设计」｜https://x.com/emmettshine/status/2105344858726813880
   > "hey! that's not true ~ there is a ton in the article, and in the kits on: strategy, copywriting, tone of voice, target demo, user journey mapping, etc. ~ visuals probably grab more of the attention, but this is a holistic brand system."
   - 用处：kit 不只是视觉。策略、文案、受众、用户旅程都要写进去。
7. **2026-02-18**｜回答 @athianandam｜https://x.com/emmettshine/status/2024163703390720253
   > "I think service providers or creative specialists will be producing markdown first, that then exports to human guidelines!"
   - 用处：先写 Markdown，再从 Markdown 导出给人看的规范 PDF，而不是反过来。
8. **2026-02-18**｜回答 @jackieberardo｜https://x.com/emmettshine/status/2024233832170344583
   > "it's not even that hard or time consuming, it's more a conceptual breakthrough (we now have two types of creative partners) than a complex workflow."
   - 用处：作者自己说 2 月这版（chunk 法）不难做。真正的工作量在 9 月版的视觉 token、组件和 QA。

#### B. 拿 kit 下指令、HTML 设计规范

9. **2026-04-18**｜Emmett 用 Claude Design 做的 .html 设计规范 v1（附 43 秒视频）｜https://x.com/emmettshine/status/2045630916316352906
   > "took the LP site (and our in dev beta site) files + the LP wiki in notion, made a .md file for design, added in our JJannon font + logo."
   - 用处：最小可行做法是「网站文件 + wiki → 一份 design.md + 字体 + logo → 交给 Claude Design 出 HTML 规范」。我们可以先这样给 whynotdesign 自己做一份。
10. **2026-05-13**｜长文《The HTML Brand》（X 版）｜https://x.com/emmettshine/status/2054539694097015171
    > "We put the final packet into Cursor and typed a single prompt: \"generate me an HTML landing page based on the atomic design system and strategy.\""
    > "Change a primary color: update one CSS variable. Change a motion curve: edit the JSON. Re-upload to Claude Design and the whole guideline regenerates against the new values."
    - 用处：给出了原文用的那一句 prompt，以及「改数值 → 规范自动重新生成」的循环。
11. **2026-05-13**｜同一篇长文｜https://x.com/emmettshine/status/2054539694097015171
    > "It will also gravitate toward the median of what the inputs allowed. Correctness and originality are not the same thing."
    > "If the atomic kit is the library, magic_trick.md is the set a great DJ puts together for a specific room on a specific night."
    - 用处：解释了为什么要有 magic_trick.md：kit 只保证「对」，不保证「好」，招牌创意必须由人来放。
12. **2026-05-04**｜回答 @0xCharlota｜https://x.com/emmettshine/status/2051379610772812290
    > "going to publish something hopefully next week on how we're using claude / claude design / figma for agentically building (not autonomously) both brand decks and interactive site html / css guides"
    - 用处：他说的是「agent 协助做」，不是全自动。预告的文章就是 9 天后发的 The HTML Brand。

#### C. 交付前用全新 agent 做 QA、上线后维护

13. **2026-07-25**｜回答 @0xCharlota｜https://x.com/emmettshine/status/2081159764193558786
    > "We have to stress test agentic kits before final handoff, either internally, or with the client, to ensure they land right. TBH sometimes there are pleasant surprises, but overall this (newer) part of the process requires increasingly considered QA and stress-testing"
    - 用处：QA 越来越重。报价时要单列「kit 压力测试」这一项工时。
14. **2026-09-30**｜长文 X 版｜https://x.com/littleplainsxo/status/2105274281110196509
    > "We look at what it gets right and where it makes something up. If it gets a decision wrong, we add what’s missing to the kit or make it clearer which file to read."
    > "kits shouldn't be assembled during the last week of a project. Set them up at the beginning."
    - 用处：两个硬规则。全新 agent 出错，就补 kit；kit 从项目第一周开始搭，不要最后一周才拼。
15. **2026-09-30**｜同一篇长文｜同上链接
    > "Another client added recipes and automated checks to its kit, then used the kit to rebuild its Figma component library and compare the result with the library its designers had made."
    > "Maintenance, right now is be the hardest part of this work."
    - 用处：客户会自己往 kit 里加 recipes 和自动检查。作者承认维护是最难的部分，我们的报价要包含维护。

#### D. Claude Code、Figma、MCP、Notion 工作流

16. **2026-08-19**｜长文《Bypassing Figma & Building a Knowledge Product》｜https://x.com/emmettshine/status/2090060814816260469
    > "We used Figma to build our v1 stylesheet, design system, and atomic kit, and those became the language we fed to coding agents."
    > "Idea from Slack, Wisprflow, or transcribed from a meeting / Rough lab in Codex or Claude Code / Shared URL / Supercut feedback, MCP into Linear, then a ticket, then a pull request"
    > "Human input > agentic modeling > human curation."
    - 用处：Figma 只用来定视觉语言，产品在代码里做。MCP 的用处是把反馈接进 Linear。和我们「Figma 定稿 → 代码出图」的流程一致。
17. **2026-08-19**｜同一篇长文｜同上链接
    > "Write Your Fast Layer by Hand — Four to six documents covering who you are, how you work, what people always ask, and how the agent should behave. Do this before you touch embeddings. It's the single most valuable part of the whole project."
    > "Models improvise, renderers don't."
    - 用处：可以做 whynotdesign 自己的工作室知识库。先手写 4–6 份核心文档，项目事实用模板渲染出来，不让模型写。
18. **2026-09-09**｜Notion 案例长帖｜https://x.com/emmettshine/status/2097719975637045433
    > "Every engagement starts with a custom deep research agent we built. It takes everything we have on a new client, plus public information and market research, and writes a full deep dive on the company, the founders, the space, and where the real opportunity sits. It lands as a Notion doc, saves out as Markdown, and loads into a shared team project in our LLM"
    > "Before anyone at Little Plains builds or operates an internal agent, they write down what it's for, how it works, what information it can use, and where a person stays in control."
    - 用处：kit 的「前一步」是每个项目开工时的深度调研 agent，以及每个内部 agent 的书面说明。这两样都可以照做。
19. **2026-09-09**｜回答 @aritrogh｜https://x.com/emmettshine/status/2097748025363812455
    > "@NotionHQ has good MCP/APIs that we pump in and out of other systems so we can manually or automagically hit. We have a pretty advanced setup with multiple multiplayer agents operating off of data residing in Notion"
    - 用处：MCP 在他们那里主要用来连接 Notion 和其他系统，不是专门的品牌 MCP。

#### E. 生成式出图流程（和包装摄影最相关）

20. **2026-04-22**｜长文《Last Mile Agentic Image Editing》（656 收藏）｜https://x.com/emmettshine/status/2047012859108851845
    > "Models drifted. Small objects broke. Upholstery softened. Wood grain wandered. Perspective got slippery. Resolution ceilings showed up quickly. The final 10–20% routinely required manual intervention."
    > "getting one usable hero often meant running 20–40 generations"
    > "The approved empty room stayed fixed as Image 1, then rugs, furniture, lighting, tabletop, and decor assets were wired in together so the model had to solve global illumination, contact shadows, and spatial relationships across the full scene in a single pass."
    > "routing the empty room plus the ecommerce assets into a GPT 5.4 text node that generated structured JSON for Nano Banana Pro"
    - 文中给出的 JSON 结构（照抄部分字段）：
      - `"base_image": {"image_1_role": "Approved empty room. Keep architecture, perspective, and lighting logic anchored to this image."}`
      - `"camera": {"lens": "40mm", "distortion": "none", "ratio": "3:2 landscape"...}`
      - `"placements": [{"image": "Image 2", "object": "rug", "instruction": "Cover most of the floor plane..."}]`
      - `"constraints": ["Render all products in one pass rather than progressive compositing.", ... "Do not invent extra furniture."]`
    - 用处：**可以直接用到焙曲产品图**。流程是：先定空场景，再把罐、袋、杯一次性放进去；用 JSON 写清镜头、摆放位置和约束；最后 10–20% 用 Photoshop 精修。多机位用 2x2 联系表生成；视频用 Veo 3.1 Ingredients，喂 3 张 9:16 裁切图。
21. **2026-01-27**｜引用 Flora｜https://x.com/emmettshine/status/2016242478479745314
    > "Almost every piece of work @littleplainsxo outputs goes through Flora at some point in the process now."
    - 另见 2026-03-26 Conception 案例 https://x.com/emmettshine/status/2037182970696458536 ："My mom painted textures, colors, and compositions throughout the project, scanning them in as she went and the @littleplainsxo team took those originals into custom node-based workflows to generatively build new scenes"
    - 用处：先有手绘或实拍原料，再用节点式工作流扩展。这和我们手作茶的调性很合。

#### F. 定价和服务包装

22. **2025-11-04**｜公司号「Generative Sprints」｜https://x.com/littleplainsxo/status/1985743242873200658
    > "Over the past six months, we’ve been engineering a new kind of process; one that fuses AI, brand, and deep market analysis into a single sprint. We call them Generative Sprints."
    - 2026-05-13 回复 @mtramos：https://x.com/emmettshine/status/2054713104513032344 ，原文 "I think pricing models are going to get pretty experimental this year which I’m excited for"
    - 用处：服务可以打包成固定周期的 sprint。定价作者自己还在试。
23. **2026-08-19**｜回复 @allanyu_（官网公开价格）｜https://x.com/emmettshine/status/2090092099571941541
    > "ya i wanted to make sure pricing was on there, even if it's not 100% accurate it's like ...so helpful vs atelier closed door intimidating"
    - 用处：官网放一个大概价格区间，可以降低询价门槛。whynotdesign 可以参考。

#### G. 案例（kit 已交付的客户）

24. **2026-10-20**｜Permanence Bio｜https://x.com/emmettshine/status/2112544775404417048
    > "@littleplainsxo built a custom responsive logo system tool for the toroid logo to hold up across every output, in full detail on a conference poster, or simplified down to a business card."
    > "Alongside the launch site, we delivered the brand as an agentic brand system, so their growing team can keep building on their own."
    - 回复 @samcroswell：https://x.com/emmettshine/status/2112594154564014405 ，原文 "we turned it over to the client specifically for that use case - so they can pick and choose what and where. it also is agentically-integrated as well"
    - 用处：kit 里可以放一个「响应式 logo 工具」，按尺寸和输出自动切换繁简版本。对包装从大外箱到小封签的场景很有用。
    - 其他提到 kit 的客户：Sonata（2026-07-15，https://x.com/emmettshine/status/2077373547807170856 ）、Haven（https://x.com/emmettshine/status/2112971853299937523 ）、Type（见《The HTML Brand》）。

### 3. 别人做的版本（回复和引用里）

- **@Sebastian98MM**（2026-09-30，https://x.com/Sebastian98MM/status/2105288045586948100 ）
  > "I set up a skill and repo in their GitHub where they can build different brand collateral, like social media posts, web pages, and  others assets with guidance on how to build new ones."
  > "The system will ask them for thoughts or grades and opinions on the output and then distill those things back into the system to continuously improve it."
  > "a majority of it was, honestly, spent on QAing, doing different checks, going through, and figuring out what's missing by getting it to a fresh agent."
  - 用处：比 Little Plains 多了一个「打分反馈 → 回写进 kit」的循环。他自己说还没验证过。
- **@0xCharlota**（2026-07-24，https://x.com/0xCharlota/status/2080643669204320538 ）
  > "A brand identity built against no real touchpoint is a brand identity that was never tested."
  > "So I always recommend coupling brand identity with at least one live surface: a full landing page, a deck, a set of social templates, posters."
  - 用处：kit 必须至少配一个真实落地物来验证。对我们来说就是一张真实的包装成品。
- **@wajishow**（2026-06-11，日文，https://x.com/wajishow/status/2065085509819650184 ）
  > "ビジュアル的なアウトプットはまずこれをベースにHTMLで出すようにすると、外に出せるレベルに質が高くて高速な0→1ができる。"
  - 他照 HTML Brand 做了一版，附图，没有文件。
- **@trq212**（前 Claude Code 团队成员，2026-05-08，长文《Using Claude Code: The Unreasonable Effectiveness of HTML》，34,562 收藏，https://x.com/trq212/status/2052809885763747935 ）
  > "to match your own companies style, you can create a single design system HTML file by pointing Claude at your codebase. You can then use that design system file as a reference for other html files."
  - 《The HTML Brand》正文引用了这篇。
- **@msllrs**（Lovable 设计师，2026-06-17，长文《a color system that disappears》，https://x.com/msllrs/status/2067186699701002607 ）
  > "the entire token set (surfaces, foregrounds, borders, intents, glows, shadows, gradients) is derived from 3 inputs: a neutral seed, a contrast value, and an accent."
  > "the fix isn't a better prompt, its a smaller surface. so were cutting the system down to a handful of tokens that are hard to misuse."
  - 用处：给 agent 用的 token 应该「少而难用错」。这对 visual-system.json 的设计很有参考价值。
- **@DanBatten**（Little Plains 合作者，2026-02-18，https://x.com/DanBatten/status/2024197323652550981 ）
  > "The act of breaking a brand down into these packets forces a level of clarity and precision that most traditional brand systems never achieve."
- **Flora 创始人 @weberwongwong**（2026-09-30，https://x.com/weberwongwong/status/2105291420135481588 ）
  > "We’re working with them to make agentic brand systems accessible for any agency &amp; in-house team"
  - 用处：说明「Flora 下个月的新功能」就是把 agentic brand system 做成产品。值得关注它上线。
- 只有观点、没有方法（列出备查）：
  - @borakaizen：https://x.com/borakaizen/status/2024137846898962940
  - @opanteraos（葡语）：https://x.com/opanteraos/status/2063018862216433826
  - @llm_kv（中文摘要）：https://x.com/llm_kv/status/2064910879905415493
  - @Iruhdam24（HueGrid 把它做成服务）：https://x.com/Iruhdam24/status/2113303100685484467
  - @JoshLowman（附 Google Doc，没打开，帖子是训练营推广）：https://x.com/JoshLowman/status/2075986104960917976

### 4. 讲清的、省略的、可能夸大的

- **讲清了：**
  - 组件格式：HTML 是规格，React 是产出；每个组件配 tokens.json 和 usage.md。
  - QA 方法：全新 agent 出错就补 kit；kit 从第一周开始搭。
  - 出图流程有具体的 JSON 结构和模型名。
  - 维护是最难的部分。
- **有矛盾的地方：**
  - 6 月说组件以 HTML 为准，9 月说 "React for components"，Sonata kit 里也确实是 .tsx。合理的理解是规格和产出两层都有，但作者没有统一说明。
  - "open source" 的说法见第 4 节前文，实际没有开源仓库。
- **读不到：**
  - 4 月 18 日 .html 设计规范的 43 秒视频（只拿到视频链接，没看画面）。
  - 2025-12-22《Software > Systems > Societies》的 Loom 和 Figma 演示稿（https://x.com/emmettshine/status/2003104017178648741 ，链接没打开）。
  - Ingredient AI 案例页 https://littleplains.com/projects/ingredient-ai 和 Flora 案例 https://flora.ai/case-studies/little-plains （这次没打开）。
  - Last Mile 长文里的 18 张配图。
  - 2 月文章里 Baba 示例的配图。
  - @Sebastian98MM 和 @wajishow 的成品文件，都没有公开。
  - 时间线接口最早只到 2025-12-09，更早的帖子这次没读。

### 5. 对 whynotdesign 的用法（kit 计划要改的地方）

1. **组件改用三件套。** `components/<名称>/component.html`（HTML/CSS/SVG）+ `tokens.json` + `usage.md`。包装组件包括罐标、封签、外箱侧标、吊牌。不再默认写 React；网页要用时再让 agent 转。
2. **增加一个 `recipes/` 目录，放产品图配方。** 照 Last Mile 的 JSON 结构写 `packshot.json`：
   - base_image：空场景
   - camera
   - style
   - placements：罐、袋、杯分别是 Image 2、3、4
   - constraints
   
   流程：先定场景，再一次性放入产品，最后用 Photoshop 精修。
3. **token 要少而难用错。** 参考 msllrs 的做法：只暴露少量语义 token，例如 `ink`、`paper`、`roast-accent`，色阶不对 agent 开放。
4. **QA 写进报价。** 交付前让全新 agent 做 3 件东西（罐标、落地页、社媒图），出错就补 kit；另外至少做一个真实包装打样来验证。
5. **（可选）加反馈回写循环。** 参考 @Sebastian98MM，在 how-to-prompt.md 末尾加「给本次输出打分 → 记进 `feedback.md` → 定期由人合并进规则」。
6. **（可选）工作室知识库。** 参考 Bypassing Figma 一文，手写 4–6 份核心文档：我们是谁、怎么做、常见问题、agent 怎么答。

### 6. 一句结论

**值得试，结论不变，计划要调整。** X 上补到的最有用的三点：组件以 HTML 加 tokens.json 加 usage.md 为准、产品图的 JSON 配方、token 要少而难用错。这三点都能直接改进给焙曲做的 kit。仍然没有可下载的官方模板。

#### 和上一轮相比

- **新增：**
  - 组件格式的问答（第 3、4 条）。
  - QA 和压力测试的补充（第 13 条）。
  - Last Mile 出图 JSON 和整套流程（第 20 条）。
  - Bypassing Figma 的工作流和知识库八步（第 16、17 条）。
  - Notion 加 MCP 的项目开工方式（第 18、19 条）。
  - 公开价格和 sprint 的做法（第 22、23 条）。
  - 响应式 logo 工具（第 24 条）。
  - 其他人的版本，尤其是反馈回写和「少 token」两点。
- **仍然读不到：** 见第 4 节。
- **是否改变 kit 计划：** 改。第 5 节第 1–4 条加入焙曲 kit 的计划。
