# 5 · seeconvm One-Prompt breakdown — RESULT
**状态：跑通**
来源：X 长文 2106096193235259564「What the Viral 'One-Prompt' Videos Are Hiding」。从 fxtwitter 重建全文，存在 `source/article_full.md`（16 个 block）。

## 实际产出（全部在 `motion-studio/`，目录结构照 block 13）
- 文档：
  - `CLAUDE.md`（block 3 原文）
  - `brief.md`（block 5 的字段：FILM / ASSETS / VISUAL / HARD LINE / DELIVER）
  - `docs/style_guide.md`：「从自己的旧作取文法」（block 6），参考图是 `assets/` 里两张 Exp09 Figma 海报
  - `docs/shotlist.md`：block 7 的 HOOK / PROBLEM / REVEAL / PROOF / CLOSE，压缩到 8 秒
  - `docs/critique_prompt.txt`（block 12 原文）
- 画面：`src/index.html`，单 canvas 的 seek(t)，叠加弹簧（block 9），弹簧按类别分组
- 渲染与声音：`render.mjs` 和 `sfx.py` 沿用 55 号文章的脚本（seeconvm 这篇本身没给渲染代码）；音效由 `cues.json` 合成
- 输出：`out/final.mp4`，复制为 `../toneroast_5.mp4`：1080×1080，8 秒，30 fps，4 个子帧，有声，**-14.4 LUFS**
- 自评记录：
  - `reviews/round0_stills.png`、`round1_stills.png`、`round1.md`（两轮评分，各修了最差 3 处）
  - `reviews/contact.png`、`strip.png`、`phone_5.4s.png`
  - `reviews/determinism.txt`：8/8 帧两次渲染逐字节一致
- 内容：
  - 「烏龍，焙得多深？」→ 灰卡片「焙度：？」在 輕 / 重 之间翻
  - 光标点一下 → 一条线分裂成五线谱，琥珀条落到第 3 线
  - PROOF：焙度 1→2→4→5 踩拍，标「示例 · Example」
  - 窑炭面板从左推入，形成分栏（这是 Exp09 海报的版式文法）
  - 焙曲 / TONEROAST 落下，余烬点变成句号

## QA
- ffmpeg 空白帧 0，最长静止 0.63 秒
- 自评第 1 轮：hook 4、手机可读性 6、运动 7、变化 7、品牌准确度 7
- 自评第 2 轮：7 / 8 / 8 / 8 / 8
- 修过的 4 处：
  1. 第 0 帧只有一个点 → 加 hook 文案
  2. 线太细、数字太小 → 放大
  3. 结尾点和条撞在一起 → 点飞去当 TONEROAST 的句号
  4. 右边距不够
- 没修的：hook 还是靠一句问句，不是一个强画面
- 这是**结尾停住**的片子，不是循环片，所以没做 loop 检查

## 来源讲清楚了的
- 文章说穿了：爆款「一句 prompt 出片」背后其实是一整个工作室——brief、风格指南、镜头表、自评循环
- 「从参考取文法、不取主题」这一条特别好用

## 漏了 / 夸大的
- 没给渲染和声音的代码，要靠别的来源（这次用 55 的脚本）
- block 3 的规则「一种展示字、一种 UI 字」和品牌的三字体系统冲突，品牌优先
- 评分是自己打给自己的，有主观偏差

## 对 whynotdesign 品牌 / 包装 / 字体工作有没有用
很有用（4/5）。brief、风格指南、镜头表这套文件可以直接当作给客户做动态品牌的交付结构。成片本身中规中矩。

## 授权风险
- 文章里的模板文字没有写授权条款，自用风险低
- 参考的是自己的 Exp09 作品。暗面板用代码画炭纹，**不是 AI 照片**，因为 Exp09 照片的授权还不清楚
- 不用 Remotion，字体 OFL

## 发布说明（GitHub 图库）
- 这些结果是**概念草稿**，不是定稿。
- 所有刀模 / 刀版都只是**原型级**，投产前必须和刀模厂打样校对。
- 所有 logo / mark 都**没有做商标检索**，不是可注册的商标定稿。
