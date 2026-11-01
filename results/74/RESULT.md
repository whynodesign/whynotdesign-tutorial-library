# #74 brand-identity-skill（fatihaydost）— 实测结果

- 仓库：https://github.com/fatihaydost/brand-identity-skill · 授权 MIT（依赖 fonttools / uharfbuzz / skia-pathops，均为开源）
- **状态：部分跑通**。`check → init → fonts search → 写 sets.json → logos（两轮，每轮改一个缺陷）→ build` 全部跑完，出了比较板；但 build 报了 gate 没清（见下），按方法应修完 gate 再给客户看，本次没修。也停在检查点，没做 kit。
- 配置：2 套方案（方法默认 3 套，为省时间选了 2，这是方法允许的选项）；色板用 `keep`（品牌简介里已给定），logo 和字体用 `new`。语言 zh-Hant + en。

## 两套方案
- **A Tempo Rule**：只有字标。Archivo Narrow 700，大写，字距加宽；第一个 O 被一条「热线」横切。
- **B Grill Ember**（推荐）：琥珀色茶球放在三根炭色烤条上，配 Noto Serif TC 900 的「焙曲」字标。

## 过程中发现的
- 第 1 轮：A 的切口太细，64 px 以下就看不见了；A 的小图标（T 加一条线）又像〒。B 像「海上日出」。第 2 轮各修一个缺陷：A 切口加高、小图标改成被切开的 O；B 的茶球贴到烤条上。
- 自己设定的「热线」颜色（余烬红）在成品里没体现：切口只是挖空，并不上色。
- gate：
  - A：Archivo Narrow 没有中文字形（真问题，品牌要写繁中）。
  - A 和 B：都报「Noto Serif TC 缺『简』字」。这个字是简体，出现在繁中字表里，**我判断是仓库语言数据的误报**。
- 色板用 `keep` 时，脚本把五个颜色依次叫作 Primary / Accent / Ground，顺序不对，要手动改名。
- `logos` 先报了 gate（brand-2 不是色板角色），要在 sets.json 里显式写入保留的色板才能过。文档没写这一步。

## 产出（/workspace/tutorial-tests/74/toneroast/）
- `brief.json`、`sets.json`、`sets/A|B/…`（每套的 logo 构建文件、identity.json）
- `logo-sheet-r1.png`、`logo-sheet.png`：两轮 logo 联系表（大图、32/16 px、单色、反白）
- `board.png`、`board.html`、`review.png`、`table.md`：两套方案的比较板和比较表
- `screenshot.png` = `board.png`

## 原帖 / 仓库讲清楚的
- 一套方案用一个「机制」同时决定 mark、字体和颜色，这个思路讲得很清楚，也真的落进了数据结构（mechanism / expression_move / differs_by）。
- 「AI 默认值」清单很有价值：Fraunces、Inter、米色 + 赤陶 + 金色、名字的物件 + 隐藏字母 + 圆形。脚本会标出命中项，要求写理由。
- 测量和判断分得很清：对比度、字形覆盖、字体授权、16/32 px 渲染算 gate，其余标为 warning 或 judgement。

## 省略或夸大
- README 的示例图很漂亮，但那是作者挑过的结果；实际跑一次要 16–20 轮，配置细节多（色板 keep、轴名必须用规定词汇等），首次上手会踩坑。
- 中文支持只到「检查字形覆盖」：字标可以排「焙曲」，但字表本身有误报。
- 和 #73 一样，mark 是 agent 用基本图形拼的，设计感上限不高。

## 对 whynotdesign 有没有用
- 「一个机制管三件事」和「AI 默认值反射测试」可以直接用在提案思路和审稿上。
- 比较板的版式规整、可读，适合内部比稿；但 mark 本身不能代替设计师。
- **有用度：3/5**

## 授权风险
- MIT。字体全是 Google Fonts OFL（可以转曲进 logo）。
- 生成的 logo 只是概念，不是可注册商标；没做检索。

## 与 exp09 的对比
- exp09 的锚点 + Brand Lock 解决的是「多张图的一致性」；这个 skill 根本不经过生图模型，所以不存在漂移问题，但出来的东西是「规范板」而不是「提案视觉」。两者可以互补：这个 skill 定系统，exp09 的流程出氛围图。

## 发布说明（GitHub 图库）
- 这些结果是**概念草稿**，不是定稿。
- 所有刀模 / 刀版都只是**原型级**，投产前必须和刀模厂打样校对。
- 所有 logo / mark 都**没有做商标检索**，不是可注册的商标定稿。
