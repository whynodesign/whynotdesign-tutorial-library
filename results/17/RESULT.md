# 17 · notdwd 12 秒 seek(t) prompt — RESULT
**状态：跑通**
来源：X 帖 2105031774904766641，用 x get_posts_by_ids 读的完整 note-tweet prompt。注意之前在 `/workspace/nova-motion-test` 测的是另一条帖（2104684539142648062，那条是 remake），这次按这条 prompt 重新做了一次。

## 实际产出
- `toneroast_17.mp4`：1920×1080，8 秒，有声
  - 画面：`film.html`（单个 canvas 的 seek(t)）+ `render.py`（Playwright，每帧截一张）
  - 声音：`sound.py` 按 `cues.json` 合成 tick / click / 上扬音 / thump，输出 `sound.wav`
- 换成品牌元素：
  - 原 prompt 的橙色 → 余烬红
  - 小球 → 五线谱上的余烬点，以八分音符节奏摆 8 个姿态
  - 标题「every frame is code」，句号就是最后落下的那个点
- 其他：`stills/`（prompt 要求的 5 张静帧）、`keyframe.png`、`qa.json`

## QA
- 按 prompt 的「5 张静帧 → 修最差的 3 处」做了一轮：
  1. 观看框在退场时露出来
  2. 观看框进场太晚
  3. 标题溢出（字号 150 → 108）+ 句号位置不对
- 另外修了一处自己写的 bug：`//` 注释把绘制代码吞掉了，标题因此不显示
- ffmpeg 空白帧 0，最长静止 0.37 秒

## 来源讲清楚了的
- seek(t) + 截图 + ffmpeg 的确定性管线
- 「先出静帧自评、再全量渲染」的循环
- 一个物体串起整片

## 漏了 / 夸大的
- 帖子把效果归功于「Opus 5.5」写的提示词。实际上关键在审美判断和修改轮次，提示词本身不保证质量
- 没给素材、字体和声音的具体做法

## 对 whynotdesign 品牌 / 包装 / 字体工作有没有用
有用（4/5）。「一个品牌元素贯穿全片」的结构很适合 logo 和包装动态。

## 授权风险
- prompt 是公开帖，没有写授权条款。我们用的是方法，代码是自己写的，风险低
- 不用 Remotion，字体 OFL

## 发布说明（GitHub 图库）
- 这些结果是**概念草稿**，不是定稿。
- 所有刀模 / 刀版都只是**原型级**，投产前必须和刀模厂打样校对。
- 所有 logo / mark 都**没有做商标检索**，不是可注册的商标定稿。
