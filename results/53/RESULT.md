# 53 · twoclipping「$10K Launch Videos」— RESULT
**状态：跑通**
来源：X 长文 2104446706741825818，用 x get_posts_by_ids 读的全文，内含 3 段 XML prompt、风格句、studio 测试和 Mixkit 下载 prompt。之前在 `/workspace/nova-motion-test/twoclipping-*` 测的是另一条帖（2103273003555402193，UI morph），这次按本文的 prompt #1（订餐 launch film）改成 TONEROAST。

## 实际产出
- **studio 测试**（step 2 原 prompt）：`studio_test/studio_test.mp4`，黑圆点用弹簧变成药丸，2 秒，60 fps；首尾帧是 `first.png`、`last.png`
- **Mixkit 素材**（step 3）：免注册，直接下载成功，存在 `assets/`
  - 配乐：「Cat Walk」，也就是 prompt 的默认曲（371）
  - 音效 6 个：click、whoosh、typing、pop、success、impact，都是页面上 `-preview.mp3` 的链接。这是否就是「Download」按钮给的同一个文件，**没有确认**
  - 曲目和音效的配对是从页面 HTML 解析的，曲名可能有错位
- **节拍分析**：`analyze.py`（胶水代码，用 numpy 算频谱通量和自相关），输出 `beatgrid.json`
  - 129.2 BPM，和 prompt 写的 130 一致
  - 有两个 drop，在约 29.8 秒和 88.7 秒。脚本自动挑的是 88.7 秒；我用 RMS 曲线人工改成第一个 drop（29.768 秒）
- **成片** `toneroast_53.mp4`
  - 规格：1920×1080，8 秒，60 fps，每帧 8 个子帧，用 ffmpeg tmix 混合（prompt 指定）
  - 画面：`film/index.html`，单个 canvas 的 seek(t)
  - 声音：Mixkit 音效按测到的峰值放置，配乐从 26.053 秒开始，让 drop 落在第 8 拍；loudnorm 后 **-13.6 LUFS**
  - 其他：`keyframe.png`、`qa.json`、`pop_scan.txt`
- **结构**（prompt #1 压缩到 17 拍）：
  1. ask：放大约 2.3× 看输入框，按 seed 的键盘节奏打出「想要炭焙重一點、/回甘長的烏龍。」
  2. send：琥珀色涟漪把文字变成气泡，镜头拉远，手机边框从屏幕边缘长出来
  3. think：送出键变成炭炉，在第 4–7 拍各抛一次茶叶
  4. drop：琥珀色在 0.35 秒内铺满全屏，5 张焙度卡炸开，横条滑到「焙度 4」并升起「最合適」
  5. 选中的卡片飞进对话；回复文字升起；光标点「加入購物車」→ 转圈 → ✓ 已加入
  6. 黑色按钮长成整页 → 「焙度，寫在五條線上。」→ 五线谱画出，余烬点沿线滑行 → 焙曲 / TONEROAST 擦出
- **品牌对 prompt 的偏离**：
  - 不用 iridescent glow，改成细的琥珀 / 余烬旋转描边，因为品牌禁 glow
  - 不用 Pexels 食物照，卡片是色块 + 五线谱，标「示例 EXAMPLE」
  - 字体用品牌字，不用 Geist；只有 mark 那一下用 pop 代替 sparkle

## QA
- 第一版：6.55–6.58 秒有 3 帧全黑（按钮标签已经退出、标题还没进来）→ 标题提前 0.1 秒进场，整片重渲
- 最终版：ffmpeg 空白帧 0，最长静止 0.3 秒
- pop 扫描：相邻帧差值超过前后 3 倍的尖峰 0 处（prompt build 第 6 条）
- 中途静帧修过：卡片横条没对正焙度 4、「最合適」药丸来不及出现、结尾标签和标题重叠、lockup 被裁

## 来源讲清楚了的
- 每段 prompt 都是同一个结构：inputs / direction / structure / build / gotchas / start
- gotchas 很实用：4 个子帧会出残影要用 8 个、铺色至少 0.35 秒否则像闪光、每层都要设 z-index
- 「先给 beat map 和 4 张静帧，再写全片」的流程

## 漏了 / 夸大的
- 标题「$10K / $15K 品质」、「0 effort」是夸大：这次做 8 秒就要拍子规划、几轮静帧修改和约 8 分钟渲染（3840 张截图）
- 「做出来和 $15k 片分不出来」没有根据
- 风格默认是 SaaS / app 发布片：聊天 UI、食物照、iridescent glow。对茶品牌只能硬套「对话找茶」的故事
- 「永远用真实音效、自己合成的很廉价」只是作者的个人偏好
- 文末是 affiliatenetwork.com 的导流广告
- 也把功劳归给「Opus 5.5」

## 对 whynotdesign 品牌 / 包装 / 字体工作有没有用
中等（3/5）。gotchas 和 Mixkit + 节拍分析流程能直接复用。叙事模板偏 app 发布，品牌和包装片要换故事。

## 授权风险
- prompt 原文没有写授权条款，自用风险低
- **Mixkit**（以下根据二手资料整理，官网授权弹窗没抓到全文）：
  - Sound Effects Free License：可商用，但必须放在更大的作品里，不能单独再分发
  - Stock Music Free License：可用于网络、社群、广告；**不能用于电视 / 广播、游戏、CD / DVD**，也不能混成纯音乐作品
  - 客户交付前要核对官方条款
- 不用 Remotion，字体 OFL

## 发布说明（GitHub 图库）
- 这些结果是**概念草稿**，不是定稿。
- 所有刀模 / 刀版都只是**原型级**，投产前必须和刀模厂打样校对。
- 所有 logo / mark 都**没有做商标检索**，不是可注册的商标定稿。
- 音频说明：原片用了 Mixkit 的配乐和音效（Stock Music 授权不能用于电视 / 广播等），这里只发布**去掉音轨的静音版** `toneroast_53_silent.mp4`。
