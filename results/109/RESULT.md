# 109 · motionmaxxing — RESULT
**状态：跑通**

## 实际产出
- `toneroast_109.mp4`：1080×1080，6 秒，`--grain 0.04`，无声。另有 `toneroast_109.mp4.events.json`
- `film/index.html`：用的是仓库自带的 Motion runtime（复制到 `film/runtime`）
- 构思：焙度从第 1 线爬到第 5 线，余烬光逐渐变强 → f135 硬切，带 3× 的 snap（五线谱交接成 mark）→ lockup 从放大状态进场
- 其他：`look/sheet.jpg`、`look_report.txt`、`lint_report.txt`、`stills/`、`keyframe.png`、`qa.json`

## QA
- look.py：G0、G2、G3 都 PASS。末尾停留 0.17 秒（停在运动中途）
- 平均每帧亮度变化 1.7/255，**低于人工片的范围**（中位数 6.8），说明画面偏静
- lint G5 PASS 的代价：TONEROAST 的字距从 .34em 降到 .04em。C2 规则会把字距 ≥ 0.05em 的全大写字当成 AI 腔，这和 Exp09 的宽字距 wordmark 冲突
- 修过：y/top 关键帧冲突；G3 的 CTA 占比 33% → 硬切挪到 f135；C2 → 降字距
- ffmpeg 空白帧 0

## 来源讲清楚了的
- 量化门槛：空帧、结尾停留、CTA 占比、运动量对照人工片
- 「AI 腔」清单：角落小标签、宽字距大写、mono 小字、状态点……能逼人跳出模板感

## 漏了 / 夸大的
- 声音要 ElevenLabs key，没有 key 就做不了（没注册，所以无声）
- 仓库在推广 FinalMotion 付费产品
- lint 规则太一刀切，品牌本身的宽字距也会被判 fail

## 对 whynotdesign 品牌 / 包装 / 字体工作有没有用
有用（4/5）。look.py 和 lint.mjs 可以单独拿来检查任何片子。但 C2 规则要对品牌 wordmark 开例外。

## 授权风险
- Apache-2.0，可商用，保留 NOTICE
- 不用 Remotion
- 音频要 ElevenLabs，那是付费第三方服务

## 发布说明（GitHub 图库）
- 这些结果是**概念草稿**，不是定稿。
- 所有刀模 / 刀版都只是**原型级**，投产前必须和刀模厂打样校对。
- 所有 logo / mark 都**没有做商标检索**，不是可注册的商标定稿。
