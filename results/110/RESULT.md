# 110 · Animation-Workflow — RESULT
**状态：跑通**（修了 starter 自己的 bug，加了胶水文件）

## 实际产出
- `toneroast_110.mp4`：1920×1080，7 秒，Remotion CRF 10，无声（就是 `project/out/toneroast_110.mp4`）
- `project/out/example-1080p.mp4`：starter 自带示例
- 新增文件：
  - `projects/toneroast/spec.md`：照 spec 模板填的
  - `src/styles/brand.ts`
  - `compositions/Toneroast/{index.tsx, constants/timing.ts}`
- 胶水：starter 没有 `src/index.ts` 和 `Root.tsx`，是我补的
- 修 bug：TitleScene 引用 `'../../../../styles/typography'`，多了一层目录，改成 `../../../styles`
- 其他：`keyframe.png`、`qa.json`

## QA
- 空白帧：0–0.133 秒（开头渐入）
- mark 在 lockup 里偏小，没再修

## 来源讲清楚了的
- spec → timing 常量 → 合成的分层结构
- 「先写 spec 再写动画」的工作习惯

## 漏了 / 夸大的
- starter 直接 clone 下来跑不起来：缺入口文件，还有一处路径错
- README 写 MIT，仓库里却**没有 LICENSE 文件**
- 最后一次提交是 2026 年 2 月

## 对 whynotdesign 品牌 / 包装 / 字体工作有没有用
一般（2/5）。主要价值是 spec 模板。动画质量全看自己写，比 107 和 55 弱。

## 授权风险
- **Remotion 4.0.539：3 人以上的公司要买 Remotion Company License**，个人或 3 人以下免费
- 仓库没有 LICENSE 文件，严格讲默认是保留所有权利，README 写的 MIT 不能当作有效授权

## 发布说明（GitHub 图库）
- 这些结果是**概念草稿**，不是定稿。
- 所有刀模 / 刀版都只是**原型级**，投产前必须和刀模厂打样校对。
- 所有 logo / mark 都**没有做商标检索**，不是可注册的商标定稿。
