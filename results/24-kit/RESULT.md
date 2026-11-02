# #24-kit · 焙曲 / TONEROAST agentic brand kit（照 Little Plains 9 月版 Sonata 结构）

- 日期：2026-11-01（PT）。制作：AI 创作实验室。
- 状态：**kit 已做完；验收已跑（2026-11-01，结果见文末 Validation，产出在 `validation/`）**，见文末「Validation」。
- 性质：**概念 / 示例，不是商用定稿。** 焙曲、TONEROAST 都**没做商标检索**（10-31 只做过网页粗查）。示例里的焙次数据是虚构的。
- 结构依据：`../24/DEEP-DIVE.md`，加上站内 `data/sonata-kit.js` 的文件清单和各文件标题（2026-11-01 读取，只借结构，没抄内容）。

## 做了什么

| 部分 | 文件 | 说明 |
|---|---|---|
| 路由 | `brand/readme.md` | 「做什么 → 读哪些文件」表，目录树，数值只在 JSON，字体授权表（中文字体只引用不打包，写明 OFL 和下载源） |
| 招牌手法 | `brand/magic_trick.md` | 五线谱 = 带真实焙火数据的图表：Symbol / Level / Score 三种读法，硬规则、Do/Don't |
| 下指令 | `brand/how-to-prompt.md` | A. 怎么驱动 agent；B. 怎么给生图/视频模型写提示词：3 个模板（无字底图、单张应用、视频氛围底片）、负面清单、10 条 QA，三种审计结论 |
| 文案 | `brand/agent/verbal/positioning.md`、`voice-and-tone.md`、`concepts.md` | 双语规则（繁中在前、间隔符 ` · `、数字用 DM Mono）、禁用词、**文字白名单**（逐字），命名表 |
| 视觉规则 | `brand/agent/visual/*.md` | brandmark、color、typography、layout、graphic-elements、art-direction、effects、motion、**packaging** |
| 唯一数值源 | `brand/agent/visual/visual-system.json` | 色（HEX + CMYK 估算 + Lab 目标）、对比度、字体与字阶、间距、圆角 0、mark 几何、Roast Score、版式、动效节拍与弹簧 |
| 生成物 | `tokens.css`、`motion.json`、`product/components/motion.js` | 由 `tools/build_tokens.py` 生成，已运行并保存 |
| 字体 | `brand/agent/visual/fonts/` | Lexend Exa、DM Mono（OFL，附许可文本）；Noto Serif/Sans TC 只引用；`FONTS.md` |
| Logo | `assets/logos/`（22 个 SVG） | 主 mark、反白、单色、小尺寸加粗版、焙度 1–5（含反白）、横/竖组合、字标、安全距离图；`tools/make_marks.py` 从 JSON 生成，字标用真字体转曲 |
| 素材 | `assets/anchor/anchor.png`、`swatches/`、`textures/`、`dieline/` | **全部用代码生成，没有 AI 图**；刀模来自 #85 |
| 组件 | `product/components/`（HTML + `stave.js`） | 焙度徽章、包装正面 70×120 mm、乐谱海报、社媒卡、5 秒品牌动效（可 seek）、锚点板 |
| 工具 | `tools/` | `build_tokens.py`、`make_marks.py`、`make_assets.py`、`check_kit.py`（检查生成物是否过期、md 里有没有散落的 hex、每个 logo 最多一颗余烬、锚点文字是否都在白名单）、`render*.sh` |

### 截图（全部在 `product/components/screenshots/`）
- `label-front_017_paper.png`、`label-front_009_celadon.png`、`label-front_018_char.png`、`label-front_017_paper_guides.png`（4× 渲染，带出血线和安全区）
- `poster_017.png`（另有给锚点用的无标记版 `poster_017_noflag.png`）
- `social-card_018.png`、`roast-badge.png`
- `motion-unit_t700/t1450/t2200/t5000.png` + `motion-unit_5s.mp4`（150 帧 @30fps，逐帧 seek 渲染）
- `anchor.png`、`dieline-overlay.png`

## 招牌手法（magic trick）的关键决定
1. **一个图形，三种读法**：主 mark（3 根台阶条）、焙度标（第 n 线上 1 根条）、焙次乐谱（每回一根条，放在当回火力那条线上，宽度按小时比例；歇是固定间隔，用 mono 写「歇 n 日」）。
2. **每根琥珀条都要对应一个数字**，说不出数字就删。焙度只用位置表达，不换色、不变粗。
3. **每个画面只有一颗余烬红点**。画面上已经有带点的五线谱时，logo 改用字标或单色 mark，不出现第二颗点。
4. **五线贯穿整个画面并出血**；只有正面的焙度条可以从右边出血。
5. **文字挂在线上**：组合标里「焙曲」从第 5 线顶到第 2 线底，TONEROAST 的基线压第 1 线；大号焙度数字站在第 1 线上，字高等于整个谱高。
6. **五线谱只用代码画，不交给模型画**（Exp09 里 5 线提示词出过 6、7 线）。AI 只出无字、无线的底图。
7. 动效「Stave → Note → Ember」：线从下往上依次画出，音符条**沿自己那条线从右边滑入**（时间在乐谱上是从左往右走的），落位用弹簧，点亮余烬，字标出现，然后静止约 2.1 秒。只跑一次，不循环。

## 实验教训落在哪里
| 教训 | 写进的地方 |
|---|---|
| 白名单文字要和锚点逐字一致 | `concepts.md` 白名单；锚点只放白名单文字和 hex；`check_kit.py` 会检查 |
| 想保留的应用要在锚点上出现一次 | 锚点上放了米纸正面、**青瓷灰**正面、海报、深色社媒卡 |
| 单张应用比 3×3 板好 | `how-to-prompt.md` A、B 两部分都写了；模板 2 只做单张 |
| 文字用代码或真字体排（D+B） | 模板 1 是默认路线；`art-direction.md` 的编辑流程 |
| 避免素材网站感，要写品牌少见的具体特征 | 「可数的特征」规则、负面清单、QA 第 8 条（遮住五线谱测试） |

## 和 Sonata 结构相比
**照搬的结构**
- `readme.md` 的写法：路由表、目录树、「两份文件存数值」、怎么用 tokens、字体授权。
- `magic_trick.md` 的四节：Why it is the signature / Where it lives / The rules that keep it working / Getting it right the first time。
- `how-to-prompt.md`：Starting / What to expect / Prompts that work / Prompts that do not / When the agent gets it wrong / Checking the result。
- `agent/verbal/` 三份文件，`agent/visual/` 八份同名规则文件，`visual-system.json` 生成 `tokens.css`（文件头写明「Do not edit」），另有 `motion.json`、`fonts.css`、`fonts/` 和许可文本，`assets/logos` 黑白两套。

**改动和补充的**
- 生成脚本我们自己写（Sonata 的 `tools/gen-tokens.py` 没公开），叫 `build_tokens.py`。
- `visual-system.json` 的字段结构是我们自己设计的。Sonata 的 JSON 读不到，404。
- motion 数值也放进 `visual-system.json`，`motion.json` 由它生成。Sonata 的 motion.json 是不是生成的，看不到。
- 组件是 HTML，不是 React .tsx；只有 5 个加 1 个锚点板，Sonata 有 15 个界面组件。我们的组件偏印刷和营销物料。
- 新增：`packaging.md`、CMYK 估算和 Lab 专色目标、生图/视频提示词部分（B）、代码渲染的锚点图、`check_kit.py`（参考了 @micka_design「把 md 规则转成 lint」的回复）、每份文件结尾的「When the rules don't cover it」（对应 Sonata 说的「规范没写到时怎么判断」）。
- kit 正文用英文，品牌文字用繁中。原因：品牌规定不能出现简体字，规则文档如果用简体写，agent 容易把简体字带进文案；英文也最贴近 Sonata 和生图模型的提示语言。给宇軒看的说明（本文件）用中文。
- 没做：guidelines PDF、Figma 版本、单独的 product kit 仓库。

## 未解决 / 已知问题
- **字体只是实验用字**，最终由宇軒选。中文字体没打包，没装 Noto CJK TC 的机器会回退到别的字体。
- **CMYK 是通用 SWOP ICC 估算**，没打样。专色只给了 Lab 目标，**没有选 Pantone 或 DIC 色号**。窯炭色按 profile 换算总墨量 291%，规则里改成文字用 K100。
- **刀模用的是 open-dieline，PolyForm 非商业授权**，客户项目要先拿授权或让刀模厂出。正面和背面的对应是我们假设的。
- 动效终帧的字标用 HTML 文字近似排，和转曲 SVG 组合标差约 2 px；以 SVG 为准。
- 没有背面、侧面、网页组件；「青瓷灰小袋」实际是沿用了纸盒正面的版式，不是真正的小袋规格。
- 没有任何摄影。Exp09 那张 AI 底图已排除。
- 法规标示内容（成分、保存期限、厂商等）没写，只预留了区域。
- 招牌手法里新加的部分（Roast Score、文字挂线、一画面一点）是实验室的设计提案，**审美要宇軒拍板**。

## Validation（待填 — 由一个没有任何项目背景的新 agent 来做）

**流程（照 Little Plains 的做法）：** 只给它 `brand/` 和 `product/` 两个文件夹，不给本文件、不给任何聊天记录。每件东西先出一版，不让它一次做到完美。

**给新 agent 的指令（原样粘贴）：**
> Read the TONEROAST brand kit in `brand/` (components in `product/components/`). Start with `brand/magic_trick.md`, then follow the routing table in `brand/readme.md`. Make three new things, one at a time, and save each with a short note of which files you read:
> 1. A front panel for a new batch: 焙次 No. 021, 焙度 3, 5 回.
> 2. A poster (1080×1440) for the same batch.
> 3. A 5-second brand motion piece (MP4 or a seekable HTML) for the same batch.
> Do not ask me questions; where the kit does not cover something, decide, and write down the decision.

| # | 产出 | 新 agent 读了哪些文件 | 遵守了 | 跑偏了 | 是哪条规则没写清 | 结论（APPROVED / CORRECTION REQUIRED / REJECT） |
|---|---|---|---|---|---|---|
| 1 | 包装正面 `validation/01-front/` | magic_trick、readme、packaging、layout、color、concepts、front 组件、stave.js、tokens/fonts/visual-system.json、017 参考图 | 五线、焙度条在第 3 线并右侧出血、一颗余烬、文字全在白名单、无简体、数值全取 token、米纸底（青瓷灰只给焙度 1–2，判断对） | 「焙曲 / TONEROAST」在五线谱下方，没挂在线上 | layout.md 说「文字挂在线上」，但 017 参考组件本身就放在线下：规则和组件互相矛盾，新 agent 跟组件走 | APPROVED（规则与组件冲突需 kit 方修） |
| 2 | 海报 1080×1440 `validation/02-poster/` | 以上 + graphic-elements、typography、brandmark、effects、poster 组件、017 海报参考 | 焙次乐谱读法正确（1–2 回在第 2 线，3–5 回在第 3 线，宽度按小时）、标语用白名单原文、logo 改用字标避开第二颗余烬、虚构数据已标注 | 「歇 n 日」70% 透明度（stave.js 的写法，违反 color.md「品牌色不透明」）；余烬在右边距而不在谱线右端 | stave.js 与 color.md 冲突；余烬位置规则与 poster 组件冲突 | CORRECTION REQUIRED（两处来自 kit 自身，不是 agent 犯错） |
| 3 | 5 秒动效 `validation/03-motion/`（150 帧 30fps MP4 + 4 关键帧 + 可 seek HTML） | 以上 + motion.md、motion.json、motion.js、motion 组件 | 节拍完全按 motion.json；改用 kit 允许的「产品版」：单根焙度条沿第 3 线滑入；一颗余烬；结尾静止；标「CONCEPT · NOT FINAL ART」 | 数据行自行放大到 20 px（kit 14 px 在 1080 画幅里太小）；未做 reduced-motion 版；动效里五线不贯穿画面 | motion.md 没写最小字号、五线贯穿是否适用动效；reduced-motion 只有描述没有组件 | APPROVED（有备注） |

**验收总结（2026-11-01）**
- 结构这一层有效：新 agent 零背景、没提一个问题，三件东西的招牌手法（五线谱 + 焙度位置 + 单颗余烬）全部守住，白名单文字零偏差，零简体字，虚构数据主动标注。
- 跑偏全部来自 kit 自身：规则文档和参考组件冲突时，agent 一律跟组件走（3 处）。结论：**组件比文字规则权重更高**，以后修规则必须同步修组件。
- 漏洞：kit 引用的 `tools/` 不在 brand/ 与 product/ 里（新 agent 自己重写了渲染脚本）；packaging.md 指向 kit 外的 #36 折盒文件。
- 没测到的：新 agent 判断「不需要 AI 图」，没读 how-to-prompt.md，所以**生图 / 生视频路线（D+B 模板、负面清单、QA）这次没被验收**。要验它，得另出一道必须用生图的题（如带摄影的包装场景图）。
- 待修清单：统一「文字挂线」规则与 front 组件；去掉 stave.js 的 70% 透明或在 color.md 里开例外；定余烬位置；motion.md 补最小字号和 reduced-motion 组件；把 tools/ 并入 kit 或在 readme 写明；packaging.md 去掉外部路径。

**检查清单**：五条线、焙度条在第 3 线、只有一颗余烬、文字逐字在白名单、没有简体字、没有负面清单里的元素、数值都来自 token、5 回和数据对得上（新 agent 得自己编 021 的数据，看它有没有标「虚构」）。
