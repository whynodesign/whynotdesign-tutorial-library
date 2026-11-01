# #73 logo-design-skill（kaankiziltug）— 实测结果

- 仓库：https://github.com/kaankiziltug/logo-design-skill · 授权 MIT（库里 1,400+ 个 logo SVG 是各自商标，仅供学习，见 TRADEMARKS.md）
- 测试日期：2026-11-01 · 虚构品牌：焙曲 / TONEROAST
- **状态：跑通（到方法规定的检查点）**。按 SKILL.md 的 fast track：写 brief → 列类目俗套 → 8–12 个一句话概念挑 3 个 → 黑白 SVG → `svg_audit.py` → 渲染看图 → 改一轮 → `concept_sheet.py` 出概念总览，然后**停在检查点**。完整 kit（配色、锁定组合、favicon、展示板）按方法要等客户选方向后才做，本次没做。

## 过程
- 概念（第 1 轮）：A 焙层 T（T 横笔叠三层）、B 窑口余烬（炭丘 + 余烬）、C 揉捻回旋（错开的两道弧）。
- 自己看图发现的问题（skill 要求的「readings / familiarity」检查起了作用）：
  - A 像日本邮政符号〒 → 第 2 轮改成「横笔 + 三段竖笔」（节拍）。
  - B 像人头半身像 → 改成炭丘 + 圆孔 + 一条灰线；第 2 轮看仍有「头盔 / 日出」读法。
  - C 像靶心 / 唱片，偏通用。
- 第 1 轮 concept sheet 里中文名和注释是方框（脚本用的字体没有中文），第 2 轮改用英文注释。lockup 里的「焙曲」是 `<text>`（探索阶段允许，已标注；定稿必须转曲）。
- 渲染：脚本默认的 headless Chrome 在本机卡住，装了 cairosvg 后正常（脚本自带的备用渲染器）。

## 产出（/workspace/tutorial-tests/73/）
- `svg/a|b|c-symbol(-v2).svg`、`*-lockup(-v2).svg`：3 个概念 × 2 轮
- `audit_round1.txt`、`audit_round2.txt`：svg_audit 结果（分数 98–100，都只是格式层面的分数）
- `concepts_r1.png`、`concepts_r2.png`：概念总览（含 64/32/16 px 实测）
- `preview_r2.html`：测试页（16 px、单色、反白、镜像等）
- `renders/*.png`
- `screenshot.png` = `concepts_r2.png`

## 原帖 / 仓库讲清楚的
- 流程非常完整：brief 模板、词图、类目俗套、mark 类型、几何构造、光学修正、16 px / 单色 / 反白测试、检查点话术、交付清单。
- 「先看再说」「检查点前不出 kit」「不能保证商标可注册」这些诚实规则写得很清楚。
- 脚本零依赖、确实能跑。

## 省略或夸大
- README 说「production-ready SVG」：脚本只检查格式（有没有 `<text>`、颜色数、锚点数），**不判断好不好看**；我的 B 方案 99 分，但读起来像头盔。
- logo 库偏科技（README 自己也承认），茶 / 食品类参考很少，`--refs-industry food` 返回 0 个参考。
- concept_sheet 不支持中文字体，中文品牌需要自己处理。
- SVG 是 agent「盲画」，质量上限取决于 agent 的几何能力；三个概念都偏简单几何，设计感一般。

## 对 whynotdesign 有没有用
- 有用的部分：检查清单（16 px、反白、误读、熟悉感测试）和「检查点前不出 kit」的节奏，可以直接放进我们的 logo 流程。
- 不适合直接出方案：几何 mark 偏素、偏通用，达不到工作室的设计水准。
- **有用度：3/5**

## 授权风险
- skill 本身 MIT，可用。
- AI / agent 画出来的 logo 只是概念草图，**不是可注册的商标定稿**；未做商标检索。

## 与 exp09 的对比
- exp09 用的是「谱线 + 音符条」mark（AI 锚点 + 代码重画）；这里的三个方向都没有走谱线，概念更多样，但单个 mark 的完成度和品牌感不如 exp09 的 C 路线。

## 发布说明（GitHub 图库）
- 这些结果是**概念草稿**，不是定稿。
- 所有刀模 / 刀版都只是**原型级**，投产前必须和刀模厂打样校对。
- 所有 logo / mark 都**没有做商标检索**，不是可注册的商标定稿。
