# 87 · design-os-origami（jangtrinh）
来源：https://github.com/jangtrinh/design-os-origami （clone 于 2026-11-01）
测试品牌：焙曲 / TONEROAST 50g 茶叶盒，tuck-box 70 × 45 × 120 mm，纸厚 0.45 mm，出血 3 mm

## 结论：跑通
按 skill（`skills/es-origami-cad/SKILL.md`）的 Build → Check → Look 流程跑：
- `scripts/self_check.py`：ok。
- `build.py --spec spec_toneroast.json --output-dir run1`：exit 0。
- `validate.py`：`ok`，exit 0。
- `look.py`：exit 0，L4–L8 都 PASS。它要求的浏览器缓存是我按 look.md 自己准备的：playwright 1.61.1、校验过 sha256 的 three r128、本机 Chromium 路径，放在 `87/browser-cache/`。

skill 规定的交付格式：
```
OUTPUT: /workspace/tutorial-tests/87/run1/
BUILD: build.py exit 0
VALIDATE: exit 0, ok
LOOK: exit 0, run1/evidence/look-sheet.png；L1–L3 人工看过：展开图完整，线型可区分（红=切，绿虚=压痕，品红=糊位），100% 时折成封闭盒
PHYSICAL_FOLD_FIT: NOT VERIFIED.
RECIPIENT_IMPORT: NOT VERIFIED.
```

## 实际产出（run1/）
| 文件 | 说明 |
|---|---|
| `TuckBox_70x45x120.svg` / `.dxf` | 展示用 SVG、R12 DXF |
| `TuckBox_70x45x120_printer.pdf` | 印刷交换 PDF，专色 CutContour / CreaseLine / Perforation / GlueArea / Bleed |
| `TuckBox_70x45x120_printer.dxf` | R2000 DXF |
| `TuckBox_70x45x120_viewer.html` | 自包含 3D 折叠查看器（需要联网加载 three.js CDN） |
| `artifact.json` | 源码、合同、产物哈希收据 |
| `evidence/look-sheet.png` = `../screenshot.png` | 25/50/75/100% 折叠检查表 |
| `../printer_pdf_preview.png` | 印刷 PDF 预览 |

## 尺寸核对（非生产级）
- 面板 45.2 / 70.2 / 45.2 / 70.2 mm，高 120，糊边 15。上盖 45.2 + 插舌 15（4 mm 斜角），防尘翼 36.2（约 0.8 × D）。盖深等于侧板宽，能折合。
- 插舌**没有摩擦扣或锁口**，防尘翼没有避让缺口。比 85 的 open-dieline 简单，实际插入可能偏松。

## README 讲清楚的
- skill 本身写得很严谨：`qualification: experimental-unqualified`，「不要说 should work」，物理折合和印厂导入都标 NOT VERIFIED。还承认纸厚补偿公式是启发式（0.45t），不是 π(R+Kt)/2。

## 省略或夸大
- README 首页写「production-ready」「cutter-ready」，和 skill 自己写的 experimental-unqualified 互相矛盾，以 skill 为准。
- 「13-check validation gate」只检查数学和文件结构（拓扑、图层、专色），不检查能不能真的插紧。

## 对 whynotdesign 有没有用
有用（3.5/5）：纯 Python，零依赖，可以在 agent 里批量出刀模和印刷 PDF，验证流程也是很好的范本。盒型细节比 85、86 粗糙，适合早期打样和 agent 自动化，不适合直接交给刀模厂。

## 授权风险
PolyForm Shield 1.0.0：可以商用，但**不能用来做和作者竞争的产品**。工作室拿它出客户刀模一般没问题；把它包装成对外的刀模工具或服务就有风险。

## 发布说明（GitHub 图库）
- 这些结果是**概念草稿**，不是定稿。
- 所有刀模 / 刀版都只是**原型级**，投产前必须和刀模厂打样校对。
- 所有 logo / mark 都**没有做商标检索**，不是可注册的商标定稿。
