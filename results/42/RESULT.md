# 42 · @alex_verem 推荐的 draw-your-font
来源：https://x.com/alex_verem/status/2083286890648899866 。帖子没有附仓库链接，我在 GitHub 搜到 **danilo-znamerovszkij/draw-your-font**（MIT，848★，npm 包 `draw-your-font` 0.1.0 指向同一个仓库）。

## 结论：跑通
- `npm install` → `npm test`：「e2e OK - synthetic photo became a valid TTF with correct metrics」。
- 没有真实手写照片，用 AI 生成一张「宣纸上的毛笔手写 A–Z」照片当输入（`input_handwriting_photo_AI.jpg`）。这样测的是工具链，测不出真实手写的难度。
- 按仓库 skill 的流程（segment → 看接触表 → 写 labels.json → build → 判断）：
  1. 原图直接 segment：「A」被深色木桌吃进一个整幅大块里，右上角也有杂块。
  2. 按 troubleshooting.md 的建议「把照片裁到只剩纸」（胶水：PIL 裁切），第二次「Z」又和纸张撕边粘在一起；再裁紧一点，第三次正好 26 个块，A–Z 一个一个对应。
  3. 我当视觉标注员写 `labels.json`，然后 build，出 TTF、WOFF2 和 CSS。

## 实际产出
| 文件 | 说明 |
|---|---|
| `TONEROASTHand.ttf` / `.woff2` / `.css` | 26 个大写字形，UPM 1000，大写高 700 |
| `input_cropped_to_paper.jpg` | 最终用的裁切输入 |
| `work/contact-1.png`、`glyphs.png`、`preview.png`、`preview_brand.png` | 接触表、字形表、预览 |
| `screenshot.png` | 原图、接触表、「TONEROAST CHARCOAL OOLONG 50G」预览拼图 |

## 实测观察
- 字形干净，笔触质感保留了，字距自然。
- **没有小写、数字和标点**，所以「50G」里的「50」显示成空白。没有 kerning（没有 kern 或 GPOS 表）。作者说这些留到 v2。
- 对背景很敏感：桌面和纸边都会被当成墨迹，要手动裁。

## 原帖讲清楚的
- 本地运行、MIT、一条命令出 TTF、AI 只负责标注不画字形，这些属实。

## 省略或夸大
- 「It handles messy photos」：本次 AI 照片要裁两次才成功，说明也不是完全不挑照片。
- 帖子没给仓库链接，GitHub 上还有好几个同名 fork 或仿制品，容易装错。
- 拿 Calligraphr、Fontself、Glyphs 的价格做对比，是营销式比较，功能根本不在一个级别。

## 对 whynotdesign 有没有用
中（3/5）：可以快速把手写或笔刷字做成「品牌手写体」原型，给包装手写标、门店小卡用。正式字体还要补字符、kerning 和中文（只支持拉丁字母）。

## 授权风险
工具 MIT。字体归手写者。本次输入是 AI 生成的手写图，正式使用请用真人手写稿，并确认书写者授权。

## 发布说明（GitHub 图库）
- 这些结果是**概念草稿**，不是定稿。
- 所有刀模 / 刀版都只是**原型级**，投产前必须和刀模厂打样校对。
- 所有 logo / mark 都**没有做商标检索**，不是可注册的商标定稿。
- 输入的手写照片是 **AI 生成的替代图**，不是真人手写稿；正式使用请用真人手写稿并确认书写者授权。
