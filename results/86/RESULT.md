# 86 · packaging-dieline-generator（NealZhouPanda）
来源：https://github.com/NealZhouPanda/packaging-dieline-generator （clone 于 2026-11-01）
测试品牌：焙曲 / TONEROAST 50g 茶叶盒，T004C 挂孔扣底盒，白卡 0.5 mm

## 结论：部分跑通
- `npm ci` → `npm test`：21 个测试文件、184 个测试全过 → `npm run build:offline` 生成 `release/包装刀模生成器.html`。
- 用 Playwright 打开离线 HTML，按用户操作选盒型、改尺寸、导出、导入贴图（胶水脚本 `drive2.cjs`；第一版导出脚本跑完后删了，导出文件保留）。
- **3D 折叠预览没验证**：在本机无 GPU 的无头 Chromium 里一点「3D」页签，页面就卡死，等 60 秒以上无响应，试了两次。是工具的问题还是环境的问题，无法区分。

## 实际产出
| 文件 | 说明 |
|---|---|
| `toneroast_T004C_70x50x120.svg` | 1:1 mm SVG（工具建议的原文件名是 `T004C_L70_W50_D120_C0.5_S2`） |
| `toneroast_T004C_70x50x120.pdf` | 带信息栏的 PDF（纸厚、纸型、刀模尺寸、过抛） |
| `pdf_preview.png` | PDF 预览 |
| `ui_dieline.png` | 结构页 |
| `ui_texture.png` = `screenshot.png` | 贴图页：导入 `_brand/flat_art_toneroast.png`（米纸＋5 线 mark＋TONEROAST） |

## 尺寸核对（非生产级）
- **T004C 的宽度下限是 50 mm**，45 会报错「T004C 宽须为 50–1200 mm」，所以这条改用 70 × 50 × 120（和 85/87 的 45 mm 不一样）。
- 竖向折线在 x = 0 / 70 / 120 / 190，面板依次是 50 / 70 / 50 / 70，加糊边。盖深约 50 = W，主体高 120。挂孔盖、扣底结构都在。几何上能折合，但没有实物打样。

## README 讲清楚的
- 7 种盒型，每种只适用自己的补偿规则；「首次投产前必须打样」；每张数量、装柜都只是估算。

## 省略或夸大
- 贴图是把整张图铺满展开图，要自己拖动对位，没有「按面板自动排版」。
- 白卡厚度只给 0.4–1.0 mm 几档，没有 0.45 mm。

## 对 whynotdesign 有没有用
有用（4/5）：中文界面，离线单个 HTML 就能用。PDF 带信息栏，方便发给印厂沟通。挂孔盒、扣底盒、飞机盒对茶包、文具周边很实用。

## 授权风险
代码 MIT，内嵌 Noto Sans SC 是 OFL 1.1，可以商用，风险低。

## 发布说明（GitHub 图库）
- 这些结果是**概念草稿**，不是定稿。
- 所有刀模 / 刀版都只是**原型级**，投产前必须和刀模厂打样校对。
- 所有 logo / mark 都**没有做商标检索**，不是可注册的商标定稿。
