# 85 · open-dieline（BrownBear127）
来源：https://github.com/BrownBear127/open-dieline （v1.4.1，clone 于 2026-11-01）
测试品牌：焙曲 / TONEROAST 50g 茶叶盒，反插式尾封盒（RTE）L70 × W45 × D120 mm，纸厚 0.45 mm

## 结论：跑通
- `npm install` → `npx vitest run`：106 个测试文件、2356 个测试全过 → `vite build` 成功。
- 本地起 `vite preview`，用 Playwright 按用户操作改参数（胶水脚本 `drive_ui.cjs` / `fold_mid.cjs`，只点界面，不改仓库代码）。

## 实际产出
| 文件 | 说明 |
|---|---|
| `toneroast_rte_70x45x120.svg` | 标准 SVG（切割/压痕/半刀/标注分层） |
| `toneroast_rte_70x45x120.manufacturing.svg` | 制造模式 SVG（0.25 线宽、去标注） |
| `toneroast_rte_70x45x120.dxf` | R12 DXF，图层 CUT / CREASE / HALFCUT |
| `params_used.json` | 实际生效参数（插舌 12、插舌间隙 0.95 自动随纸厚算、防尘翼 14、糊边 12） |
| `ui_design.png` = `screenshot.png` | 刀模设计界面 |
| `ui_fold_p0/p45/p75/100.png` | 内置 3D 折盒预览（白卡 / 牛皮） |

## 尺寸核对（非生产级，仅原型）
- 展开 243.8 × 234.0 mm。面板宽 70 / 45.45 / 70.45 / 45.9 mm：随纸厚做了周长补偿，符合 RTE 做法。
- 上下盖高 45 = W，插舌 12，防尘翼 14（约 W 的 1/3）。盖能盖住开口，能折合；3D 预览也折得上。
- 没做实物打样。刀模厂没有校对过。DXF 不做 y 轴翻转（作者在源码注释里说明了）。

## 原帖/README 讲清楚的
- 盒型只有 RTE 和天地盒三件套，README 写明「正式生产前请与刀模厂校对打样」。
- 纸厚补偿、DXF 分层、拼版估算的限制（单向收缩、不计共刀/丝向）都写得很老实。

## 省略或夸大
- 「以真实生产刀模逆向量测校准」：校准样本没有公开，无法复核。
- 盒型很少，没有挂孔盒、飞机盒、抽屉盒。

## 对 whynotdesign 有没有用
有用（4/5）：小批量茶盒、文具盒要快速出可打样的 RTE 刀模，并在 3D 里看比例。界面本身也是好的设计参考。

## 授权风险（重要）
**PolyForm Noncommercial 1.0.0：只限非商业使用。** whynotdesign 拿它做客户项目算商业使用，要先写信到 hello@konvolut.art 谈授权。线上版 tool.konvolut.art 同样受这个限制。

## 发布说明（GitHub 图库）
- 这些结果是**概念草稿**，不是定稿。
- 所有刀模 / 刀版都只是**原型级**，投产前必须和刀模厂打样校对。
- 所有 logo / mark 都**没有做商标检索**，不是可注册的商标定稿。
- 授权说明：open-dieline 是 **PolyForm Noncommercial 1.0.0**，只限非商业使用，商用要先向作者谈授权。这里只放我们生成的刀模和截图，**不包含它的任何源码**。
