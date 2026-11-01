# 107 · claude-motion-design — RESULT
**状态：跑通**

## 实际产出
- `toneroast_107.mp4`：1080×1080，6 秒，30 fps，每帧 6 个子帧做运动模糊，无声
- `film.html`：照 skill 的 seek(t) 模板写的；`render.py`：skill 自带的 `render_template.py`，只改了 URL、FPS=30、T=6、SUB=6、1080²
- `keyframe.png`：12 帧拼图；`probe/sheet.png`：探针 contact sheet；`render.log`；`qa.json`
- 内容：五条线依次画出 → 琥珀方块一级级升起 → 余烬点落下 → 遮罩里升起文字（焙曲 / TONEROAST / 副标）

## QA（ffmpeg）
- 空白帧：0–0.167 秒（开头是空纸面，是刻意的）。末尾停留 1.47 秒
- skill 自己的 probe 查到：跳变 0 处，闪烁 0 处
- 修过一处：副标的遮罩漏字 → 给遮罩设 line-height，再加 translate 140%

## 来源讲清楚了的
- seek(t) 确定性渲染契约，加上 Playwright 截图 → ffmpeg 的完整流程，脚本直接能跑
- 子帧运动模糊、闭式弹簧（damping ≥ 0.72）
- 禁用清单：每场一块平铺底色、卡通回弹等

## 漏了 / 夸大的
- 审美方向要自己给。skill 只管「别做难看」，不管「做得好看」
- 没有声音流程
- 默认偏「科技感发布片」，和茶、包装这类安静品牌要自己调

## 对 whynotdesign 品牌 / 包装 / 字体工作有没有用
有用（4/5）。纯 HTML + canvas，品牌字和色板都能原样用。动作克制，适合做 logo 动画和包装主视觉的动态版。

## 授权风险
- 仓库是 MIT，可商用，保留版权声明即可
- 不依赖 Remotion，没有 Remotion 公司授权问题
- 字体都是 OFL

## 发布说明（GitHub 图库）
- 这些结果是**概念草稿**，不是定稿。
- 所有刀模 / 刀版都只是**原型级**，投产前必须和刀模厂打样校对。
- 所有 logo / mark 都**没有做商标检索**，不是可注册的商标定稿。
