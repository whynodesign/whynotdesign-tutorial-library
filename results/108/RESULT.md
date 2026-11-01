# 108 · 归藏 product-video-skill — RESULT
**状态：跑通**（自带的 delivery 检查还剩 2 条 error，原因见下）

## 实际产出
- `project/renders/technical-demo.mp4`：skill 自带示例，10 秒，原样渲染，证明流程能跑
- `toneroast_108.mp4`：1920×1080，7 秒，有声（就是 `project/renders/toneroast_108.mp4`）
  - `src/shots/toneroast.jsx`：开场标题 → RoastPicker 组件（onDrive 里真的执行 click()，焙度从 2 切到 4）→ lockup
  - 补充文件：`film.css`、`DIRECTION.md`、`plan.json`
- 声音：配乐是 skill 示例乐谱 `score-example-keys.py` 截到 7 秒。skill 明确说要改写、不要照搬示例，这里是直接复用，**属于偷懒**。click / resolve 音效用 `mix_audio.py` 放置
- 其他：静帧在 `project/renders/`，`check_delivery.json`，`keyframe.png`，`qa.json`

## QA
- 空白帧：0.333 秒和 2.467 秒各 1 帧（转场时纸面露出来一帧）
- 修过：第一帧空白（tl.set 在 0 秒加 immediateRender 造成）→ 让 `.shot-intro` 默认可见，把初始状态的 set 移到海报帧之后；交叉淡化时开场和组件重叠、5 帧纸面空档 → 重新排时间
- `check_delivery.py` 剩下 2 条 error：
  1. 「中文标题默认用无衬线」：品牌规定用 Noto Serif TC，**故意不改**
  2. 「推广片至少要一条有证据的功能宣称」：虚构品牌没有真实宣称，**不编**

## 来源讲清楚了的
- 镜头规划 → JSX 镜头 → 驱动真实交互 → 渲染 → 混音 → 交付检查，整条链路脚本齐全
- 交付检查真的会挑毛病，而且会写明自己的局限（不判断审美、不听声音）

## 漏了 / 夸大的
- 整体是为「软件更新片」设计的：功能宣称、UI 组件、中文无衬线这些规则对茶品牌是反的
- 示例乐谱很容易被直接照搬
- 安装链很重：React、three、esbuild、Playwright

## 对 whynotdesign 品牌 / 包装 / 字体工作有没有用
中等（3/5）。适合给 app 或数字产品做功能片。品牌和包装片要先关掉好几条规则。

## 授权风险
- 主仓库是 **AGPL-3.0**：拿来改给客户交付或做网络服务，要注意开源义务
- CodePilot 那部分是 **BSL-1.1**，有商用限制
- 不用 Remotion
- GSAP 用的是免费的 Standard License（不是 OSI 开源授权）

## 发布说明（GitHub 图库）
- 这些结果是**概念草稿**，不是定稿。
- 所有刀模 / 刀版都只是**原型级**，投产前必须和刀模厂打样校对。
- 所有 logo / mark 都**没有做商标检索**，不是可注册的商标定稿。
- 音频说明：原片的配乐直接复用了 skill 的示例乐谱，这里只发布**去掉音轨的静音版** `toneroast_108_silent.mp4`。
- 授权说明：归藏 product-video-skill 主仓库是 **AGPL-3.0**（CodePilot 部分是 BSL-1.1）。这里只放我们生成的成片和关键帧，**不包含它的任何源码**。
