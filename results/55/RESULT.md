# 55 · 0xclayo Motion Playbook — RESULT
**状态：跑通**
来源：X 长文 2111079749342675440。API 返回的 plain_text 把代码块丢了，所以用 fxtwitter 的 article blocks + entityMap 重建全文，存在 `source/article_full.md`（48 个 block）。

## 实际产出
- `toneroast_55.mp4`：1080×1080，8 秒，30 fps，有声，是按文章给的 X 导出规格再编码一次的版本；母版是 `out/final.mp4`（同一份画面，码率较高，所以两个文件不是逐字节相同）
- 从文章原样取出的代码：
  - `render.mjs`（block 18）
  - `sfx.py`（block 34）
  - `CLAUDE.md`（block 14、15）
  - `BANNED.txt`（block 9）
- 自己写的：
  - `spec.md`：照 L3 模板（block 7）填的
  - `stills.mjs`：胶水脚本
- `index.html`：用文章的 page kit 和 MOTION 常量。全片只有一个容器（琥珀条）一路变形：
  - mark → 「選擇焙度」药丸 → 五档滑杆，从 1 拖到 4 → 加载环 → 勾号 → toast「焙度 4·已加入」→ 回到 mark，形成循环
- 证据文件：
  - `out/contact.png`、`out/strip.png`、`out/phone.png`
  - `out/loop_check.mp4`
  - `keyframe.png`、`qa.json`
- 渲染：30 fps，`--sub 4`，用 tmix 在 120 fps 上混合子帧

## QA
- 响度 -14.6 LUFS
- 循环接缝差异 0.012，对比相邻帧中位数 0.104，接缝看不出来
- 确定性：两次渲染 `diff -r` 一致
- ffmpeg 空白帧 0
- critique 后修了 3 处：
  1. UI 在手机尺寸看不清 → 放大
  2. 勾号的缓动不对
  3. 拖完松手后光标瞬移 → 加了明确的松手弹簧

## 来源讲清楚了的
- 渲染契约、BANNED 清单、L1–L3 三级 spec 模板
- 叠加弹簧，所有值都是 t 的纯函数
- 子帧运动模糊、合成音效 + loudnorm
- 循环、手机尺寸、确定性三种检查

**这是 9 个来源里最完整、最能直接照抄的一份。**

## 漏了 / 夸大的
- 代码块在 X API 的纯文本里看不到，要自己去重建
- 也把功劳归给「Opus 5.5」
- 默认场景是 SaaS UI 变形，不改的话很容易做成「又一支 UI 动效片」

## 对 whynotdesign 品牌 / 包装 / 字体工作有没有用
很有用（5/5）。方法和检查流程可以直接搬进自己的动态品牌流程。

## 授权风险
- 文章里的代码片段没有写授权条款：内部用可以，要开源或卖模板之前先确认
- 不用 Remotion
- `node_modules` 是指向 108 的软链，只用了里面的 Playwright

## 发布说明（GitHub 图库）
- 这些结果是**概念草稿**，不是定稿。
- 所有刀模 / 刀版都只是**原型级**，投产前必须和刀模厂打样校对。
- 所有 logo / mark 都**没有做商标检索**，不是可注册的商标定稿。
