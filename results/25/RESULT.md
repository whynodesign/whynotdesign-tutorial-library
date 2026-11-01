# #25 @shugarDadddy「Figma Brand Kit 插件提示词」（Logo Kit）— 实测结果

- 原帖：https://x.com/shugarDadddy/status/2081523586582335573（X 长文，2026-07-26）
- 提示词仓库：https://github.com/playbookTV/logokit（只有 README.md 一个文件，授权 **CC0 1.0**），已存为 `logokit_spec_README.md`。
- **状态：跑不通（核心步骤没执行）**。原方法是：在 Figma 文件里打开 **Agent 标签页**，粘贴规格，让 Figma 的 agent 生成插件，再对选中的 logo 运行。
  - **Figma 先试了一次**：`whoami` 正常（WhyNotDesign 团队，starter 计划）；`list_generative_plugins` 正常（库里 0 个插件）。也就是说读接口本次可用，没碰到额度报错。
  - 但 Figma 的 **Agent 标签页是 Figma 应用里的界面功能，MCP 里没有对应工具**。MCP 有 `create_generative_plugin`，但它只创建一个「画方块」的脚手架，要由我自己写完整的插件代码（TypeScript + UI，按规格估计上千行）。这超出了本次「不另写大段代码」的限制，所以没有创建插件（skill 也要求创建后必须写完，不能半途停）。
  - 没在浏览器里登录 Figma 去用 Agent 标签页（不代为登录或操作账号界面）。
- 本地替代：`screenshot.png` 是规格覆盖分析图（**不是插件产出**），列出 13 页文档结构里哪些页有规格、哪些只有页名。

## 规格阅读发现
- 13 页结构：Cover、Identity Overview、Logo Treatments、Clear Space、Minimum Size、Background Use、Recommended Usage、Brand Palette、Typography、Colour Scales、Accessibility & Pairings、Gradients、Notes。
- 写得最细的是字体（§4–§10，超过一半篇幅）、颜色命名（color-name-list + CIEDE2000）和作者署名；Logo 处理、留白、最小尺寸、背景使用这些交接核心页**只有页名，没有规格**。
- 文件里写着 `schemaVersion: 10` 和「existing v9 fields remain」，说明这是 **v10 增量规格**，前 9 版的内容不在仓库里。直接粘贴给 Figma agent，核心页只能靠 agent 自己补。
- 强制署名：要求在客户交付文档的封面和 Notes 页印上「Logo Kit by Leslie Williams · Ovalay Studios」并加链接，v10 不允许用户修改。这不适合给客户的交付件。

## 原帖讲清楚的
- 「提示词就是产品」：分享规格让别人在自己的 Figma 里生成插件；本地运行，不上传客户 logo。
- 现实提醒到位：生成的插件要测试、要反复调，「不是魔法咒语」；Figma agent 和生成式插件目前在 beta 期免费，之后可能变。
- 明确不做的事：不识别 logo 字体、不推断品牌策略。

## 省略或夸大
- 文章说「grab the full prompt」，但仓库里的是缺了前几版的增量规格（见上）。
- 没有说明生成要几轮、成功率多少；文章里的成品图是作者调过的结果。
- 强制署名的要求在文章正文里没有提。

## 对 whynotdesign 有没有用
- 思路有用：logo 定稿后自动出交接文档（留白、最小尺寸、背景、色板），能省苦工。
- 但这条路线要在 Figma 应用里操作，规格又不完整，而且强制署名。**同样的需求，#75 的 build_kit 已经能在本地出 13 页规范 PDF**，更可控。规格里的字体页、颜色命名规则可以当检查清单。
- **有用度：2/5**

## 授权风险
- 规格是 CC0，可以自由改，包括去掉署名。不过原作者在规格里写了署名要求，改掉之前最好想清楚。
- 插件本身不生成 logo；交付文档里如果用到 AI logo，仍然只是概念，不是可注册商标。

## 与 exp09 的对比
- exp09 在 Figma 里手搭了 Brand Kit 页（主 lockup、反白、色板、字体说明）；Logo Kit 想把这一步自动化，但本次没能生成插件，无法比较实际产出。

## 发布说明（GitHub 图库）
- 这些结果是**概念草稿**，不是定稿。
- 所有刀模 / 刀版都只是**原型级**，投产前必须和刀模厂打样校对。
- 所有 logo / mark 都**没有做商标检索**，不是可注册的商标定稿。
