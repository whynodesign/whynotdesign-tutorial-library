# 54 · HeyGen Motion-Graphics Skill (HyperFrames) — RESULT
**状态：跑通**（本地运行，没用 HeyGen 账号，也没付费）
来源：X 帖 2076381187640324427「Motion-Graphics Skill · Day 7 of 30」。帖子里的链接是 `github.com/heygen-com/hyperframes/tree/main/skills/motion-graphics`。

## 关键发现
- **这个 skill 已经不在 main 分支了。** 2026-10-21 的 commit 688229314f「publish seven knowledge skills … and retire the workflow skills」把它下架了
- 我从删除前最后一个 commit `388011b214`（2026-10-18）用 `git archive` 取回了完整原文，放在 `_repos_motion/hyperframes_motion-graphics_388011b214/skills/motion-graphics/`
- 现在帖子里的链接是 404，新版只剩通用的 `/hyperframes` skill

## 实际产出
- CLI：`npm i hyperframes@0.8.227`，装在 `54/node_modules`，只装在本目录，没装全局
- 初始化：`hyperframes init videos/toneroast-sting --example=blank --skip-skills --resolution=square --skill=motion-graphics`。加了 `--skip-skills`，**没有改动任何全局 skill**
- 按 skill 流程走了一遍：
  1. **Director**：`shot-plan.json`，类别 logo-reveal，`asset_needs` = 自带的 mark SVG
  2. **catalog 搜索**：`npx hyperframes catalog --query …`，挑了 `logo-brand-close`（字母依次落下，品牌句号最后落下）。没选 skill 指定的 `logo-outro`，因为它带 glow，品牌禁用
  3. **Builder**：`npx hyperframes add logo-brand-close`，再原地改了 4 处，都标了 `TONEROAST edit`：
     - lockup 下移
     - 字距改成 0.28em
     - 字重 500
     - 宽度改为 62cqw
     - 另外加了 tagline 字体变量
  4. 五线谱 mark 是手写的子合成 `compositions/mark.html`：线条依次画出，琥珀方块在 1.2 / 1.5 / 1.8 秒踩拍升起，余烬点在 2.0 秒落下
  5. **Verify**：`hyperframes check .` 通过（lint / runtime / layout / motion / contrast 31/31）；`hyperframes snapshot` 生成 contact sheet
  6. **Render**：`hyperframes render . --skill=motion-graphics -q high`，4.8 秒渲完
- 输出：`toneroast_54.mp4`，1080×1080，6 秒，30 fps，无声
- 其他：`hf_contact_sheet.jpg`、`keyframe.png`、`qa.json`

## QA
- ffmpeg 空白帧 0
- check 剩 1 条警告：`first_frame_empty`，就算第 0 帧已经画出 42% 的第一条线也还是报。另有 1 条 info：`audio_none`
- 自己看出的问题：
  - TONEROAST 的句号用 Lexend 的「.」，太小，而且被字距推得太远
  - 「焙曲」降成了小号 tagline，层级不对
  - 这两处都没再修

## 来源讲清楚了的
- 「先判断要不要搜索 → 选类别 → 先找素材 → 优先复用 catalog 区块」的决策链
- HF 合成契约：一个暂停的 GSAP timeline + `window.__timelines`
- check 和 snapshot 闸门真的有用，能抓出布局、对比度、首帧这类问题

## 漏了 / 夸大的
- 帖子说「描述目标就好，不用指定特效」。实际上 catalog 区块自带风格（深色底、渐变、glow），品牌化要手动改 CSS
- 帖子的链接已经失效（skill 被下架）
- 渲染时加 `--skill` 会把这次渲染记到他们的使用遥测里；我设了 `DO_NOT_TRACK=1` 和 `HYPERFRAMES_NO_TELEMETRY=1`
- 组件从 jsDelivr CDN 加载 GSAP，要联网
- CLI 里有 `cloud`、`billing`、`publish` 等付费或云端指令，**都没碰**

## 对 whynotdesign 品牌 / 包装 / 字体工作有没有用
有用（4/5）。catalog 里现成的 logo、lockup 区块，加上 check 闸门，做品牌 sting 很快。代价是每个区块都要先「去 HeyGen 味」。

## 授权风险
- HyperFrames 是 Apache-2.0，npm 包也是 Apache-2.0，可商用
- 不用 Remotion
- GSAP 用 Standard（免费）License，不是 OSI 开源
- 注意 HeyGen 的遥测；cloud 渲染是付费服务

## 发布说明（GitHub 图库）
- 这些结果是**概念草稿**，不是定稿。
- 所有刀模 / 刀版都只是**原型级**，投产前必须和刀模厂打样校对。
- 所有 logo / mark 都**没有做商标检索**，不是可注册的商标定稿。
