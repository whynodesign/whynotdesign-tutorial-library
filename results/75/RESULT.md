# #75 shadowtor/BrandDesign（brand-studio skill）— 实测结果

- 仓库：https://github.com/shadowtor/BrandDesign · 授权 MIT。它是 #73 logo-design-skill 和 #74 brand-identity-skill 的合并版，两个上游的 MIT 授权和商标说明都附在仓库里。
- **状态：部分跑通**。brief → 3 个黑白草图 → 审计和渲染 → 改一轮 → 概念总览 → 审稿包（`review_pack.py`）→ 选定方向后精修 → `compose_lockup.py` → brand.json → `build_kit.py`，全链路都跑完了，**出了整套 kit**。缺的两步：
  1. **独立审稿子 agent 没有跑**：本环境没法另起一个子 agent。`review/round-1/REVIEW-PACKET.md` 已经生成，可以交给另一个 agent 或人来审。
  2. **跳过了检查点的停顿**：方法要求先停下等客户选方向，为了测 kit，我直接用了推荐方案 C，这里说明一下。
- 照片 mockup（`--photo-mockups`，要从 mockups-design.com 下载第三方 PSD）没有开，只出了插画 mockup。

## 关键问题与临时绕法（胶水）
- 第一次跑 `build_kit.py` 时，logos、social、stationery、mockups、guidelines 全部失败（chrome produced no file）。
- 原因：本机 Chrome 一加 `--user-data-dir`（脚本每次都会新建一个临时 profile）就卡住不出图；不加就正常。
- 绕法：写了一个 5 行的包装脚本 `/workspace/tutorial-tests/_glue/google-chrome`，去掉这个参数、串行调用，放在 PATH 最前面。**仓库代码一行没改**。之后全部 stage 成功，约 50 秒。
- 这是本机环境的问题，不一定是仓库的 bug，但仓库对这种情况没有降级方案。

## 方案
- A Ember O：O 里压一颗余烬（像靶心 / 眼睛）。
- B Tuning Fork：音叉 T。字母测试不过关，读起来像 Y / Ψ，已标为风险。
- **C Kiln Metronome**（选定）：窑形梯形块里切出一根 15° 的摆杆槽，也就是节拍器。第 2 轮按 audit 的提示，把 76.5° 的近似角对齐到 75°。
- 注意：brandpress（#78）的 anti-patterns 写着「三角形里放一个记号 → 读作警示标志」，C 有这个风险。另外，仓库自带的示例品牌正好叫「Kiln」咖啡烘焙（拱形窑口 + 一颗余烬），**烘焙类目的 AI 方案很容易撞到这个示例**。

## 产出（/workspace/tutorial-tests/75/brand-studio/toneroast/）
- `brief.md`、`concepts/`（3 个概念 × 2 轮 SVG、Instrument Serif 转曲字标）、`concepts-r1.png`、`concepts.png`
- `review/round-1/REVIEW-PACKET.md`（独立审稿包，未送审）、`review/preview-r2.html|png`
- `final/`：symbol、wordmark、横 / 竖 / 方锁定组合、favicon 源、误用图
- `brand.json`
- `deliver/`（282 个文件）：
  - logo：5 种形态 × 5 种配色 × svg/png/jpg/pdf
  - favicons：全部通过；1 个 warning：浅色标签页上对比度只有 1.25:1
  - social：20 张头像和横幅
  - stationery：信纸、名片（出血）、签名
  - mockups：2 张插画（纸袋、托特包）。另外 4 项（标签、礼盒、纸袋、搪瓷杯）没有插画版，需要 PSD
  - tokens：CSS / SCSS / Tailwind / DTCG
  - guidelines：13 页 PDF
- `screenshot.png`：规范第 1、3、4、6、8 页和 merch 总览拼图

## 原帖 / 仓库讲清楚的
- 交付清单写得非常具体，而且真的都生成了：规范 PDF 里的误用页会画出「只有这个 mark 才会犯的错」（我加了「不要填满摆杆槽」）。
- 诚实条款清楚：商标检索没做、CMYK 只是屏幕换算、Pantone 留空、mockup 只能私下预览。

## 省略或夸大
- 「merch chosen for the business」：没有茶类别，最接近的是 food / coffee，要手写 merch 清单；而且不开 PSD 下载时大多数物件没有图（6 项只出了 2 项）。
- 中文：字标只有拉丁字母，kit 和规范里没有「焙曲」字标。规范 PDF 的中文色名能显示。
- 很依赖 Chrome 的 headless 截图；环境稍有问题，整套 kit 就失败，而且只报「chrome produced no file」，不说原因。
- 独立审稿要求子 agent，单 agent 环境做不了。

## 对 whynotdesign 有没有用
- **最有用的是 `build_kit.py`**：拿到定稿 mark 后，一条命令出全套格式文件、favicon、社媒尺寸、信纸、名片和规范 PDF，能省大量交付苦工。
- 概念阶段的 mark 质量和 #73 一样偏素，不建议用它出创意。建议的用法是：我们在 Figma 定稿 mark，再喂给 build_kit 出交付包。
- **有用度：4/5**

## 授权风险
- MIT。字体：Instrument Serif、Noto Serif TC，都是 OFL。
- logo 是 agent 画的概念，不是可注册商标；没做检索。
- 照片 mockup 用第三方 PSD，按对方站点授权只能私下预览（本次没用）。

## 与 exp09 的对比
- exp09 在 Figma 里手搭了 Brand Kit 页、社媒和海报；这里一条命令出了 282 个交付文件和 13 页规范，但视觉更像模板。可以组合使用：exp09 C 路线的 mark 定稿后，喂给 build_kit 出交付包。

## 发布说明（GitHub 图库）
- 这些结果是**概念草稿**，不是定稿。
- 所有刀模 / 刀版都只是**原型级**，投产前必须和刀模厂打样校对。
- 所有 logo / mark 都**没有做商标检索**，不是可注册的商标定稿。
