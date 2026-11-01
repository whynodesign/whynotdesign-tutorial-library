# #78 brandpress（DiegoAmorimDev）— 实测结果

- 仓库：https://github.com/DiegoAmorimDev/brandpress · 授权 MIT
- **状态：跑通**。按 SKILL.md：读 anti-patterns → 画 5 个方向放在一张表上并写淘汰理由 → 选 1 个 → 照 README 的说法「复制 build_example.py，只改 CONSTANTS 和 symbol()」→ 一条命令出全套 → `qa.py` 自检 → 看图后再修。
- 依赖：pymupdf、fonttools、uharfbuzz（已装）。字体用 google/fonts 仓库里的 Noto Serif TC 变量字体，切出静态字重。

## 5 个方向（`explore_sheet.png`）与淘汰理由
1. 条纹茶球：两条横纹溢出了圆形（evenodd 的副作用），读起来像落日 / 球。
2. 焙度台阶：三根递增圆角条，读成「文字左对齐」的 UI 图标。
3. 渐强记号：两根张开的条，读成「<」小于号。
4. **窑口**（选定）：圆角方块 + 拱形窑口 + 一颗余烬。
5. 音环：圆环 + 偏心圆点，读成眼睛 / 唱片。
- 注意：4 和 #75 仓库自带的示例品牌「Kiln」（拱形窑口 + 余烬）几乎一样，熟悉感风险高，正式用之前要换掉或做出明显差异。

## 迭代
- v1：方法里的「缩小测试」不过关（只能缩到 64 px）。我把窑口加宽到 46、余烬缩到 r7，结果仍报 64 px。这个检查是用墨量变化来估计的，脚本注释也说「当提示看，要用眼睛确认」；我目测 32 px 能认，16 px 余烬基本消失。
- v2：我把主色设成和墨色一样的窑炭色，结果深色底上 mark 完全消失（封面、名片、反白锁定组合、图标），只剩一个余烬点。保留在 `output_v2_seed_eq_ink/` 作为反例。
- v3（最终）：主色改成乌龙琥珀，余烬改成余烬红。contrast 检查报琥珀 / 米纸 3.81:1，正文不及格。按 SKILL.md 的说法，这不是改颜色的理由，而是一条规则：「琥珀只用于形状，不用于正文」。

## 产出（/workspace/tutorial-tests/78/）
- `explore.py`（胶水，用仓库的 geometry 模块画 5 个方向）、`explore_sheet.png|svg`
- `build_toneroast.py`（由 build_example.py 复制，只改了常量、symbol() 和构造页说明文字）
- `output/`（19 个文件）：symbol / lockup / 反白 lockup，各有 svg、pdf、png；图标 16–1024 px；**名片 PDF**（85×55 mm、3 mm 出血、有 TrimBox）；**4 页品牌手册 PDF**
- `output_v1/`、`output_v2_seed_eq_ink/`：迭代留档
- `fonts/`：Noto Serif TC 变量字体和静态字重（OFL；交付时要附授权文件，本次未附）
- `screenshot.png`：手册 4 页 + 16/32/64 px 图标

## 原帖 / 仓库讲清楚的
- 「出文件，不出图片」这个定位兑现了：logo 是曲线，名片 PDF 有 TrimBox、BleedBox 和 3 mm 出血，qa 能检查有没有 `<text>`、TrimBox 和对比度。
- 「Traps that cost real time」里写的都是真坑（组透明度被忽略、Google Fonts CSS 拿到坏字体文件、变量字体只渲染默认字重）。
- 一条命令可复现；改品牌只改一个模块。中文字形能正确出曲线（焙曲的转曲正常）。

## 省略或夸大
- 示例默认主色和墨色不同；如果主色等于墨色，深底上 mark 会消失，但没有任何检查会报出来（qa 只查主色在米纸上的对比度）。
- 手册只有 4 页（封面、构造、颜色、应用），README 里说的「real brand manual」偏简略，没有误用、留白、字体页。
- 缩小测试是墨量估算，容易误报，需要看图判断。

## 对 whynotdesign 有没有用
- **对包装、印刷很有用**：带出血和 TrimBox 的 PDF 生成器，可以改造成我们自己的标签、名片、贴纸出图脚本；可复现，适合「mark 定稿后批量出印刷件」。
- 不适合做创意：mark 质量取决于你写的 geometry。
- **有用度：4/5**

## 授权风险
- MIT。Noto Serif TC 是 OFL，交付时要附 OFL.txt（仓库也提醒了）。
- logo 是概念，不是可注册商标，而且和 #75 的示例撞型；没做检索。

## 与 exp09 的对比
- exp09 的 mark 是用 make_mark.py 代码画的，思路和 brandpress 一样（几何参数写死在代码里）。brandpress 多了印刷级 PDF（出血和 TrimBox），这是 exp09 没有的；但 exp09 在 Figma 里的版面和设计感明显更强。

## 发布说明（GitHub 图库）
- 这些结果是**概念草稿**，不是定稿。
- 所有刀模 / 刀版都只是**原型级**，投产前必须和刀模厂打样校对。
- 所有 logo / mark 都**没有做商标检索**，不是可注册的商标定稿。
