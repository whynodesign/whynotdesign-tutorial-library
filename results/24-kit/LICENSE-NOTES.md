# 授权与发布说明（#24-kit 焙曲 / TONEROAST agentic brand kit）

**概念草稿，不是商用定稿。** CMYK 是估算值（通用 SWOP ICC，没有打样）。专色还没定，只给了 Lab 目标，没有选 Pantone 或 DIC 色号。「焙曲」「TONEROAST」都没做商标检索。示例里的焙次数据是虚构的。

## 逐项授权

| 内容 | 授权 | 说明 |
|---|---|---|
| `brand/agent/visual/fonts/LexendExa-VariableFont_wght.ttf` | SIL OFL 1.1 | 许可全文见 `OFL-lexendexa.txt`。Reserved Font Name 是 "RevReading Lexend"，修改后的版本必须改名 |
| `brand/agent/visual/fonts/DMMono-*.ttf` | SIL OFL 1.1 | 许可全文见 `OFL-dmmono.txt` |
| 中文字体（Noto Serif TC、Noto Sans TC） | SIL OFL 1.1 | **没有打包**，只在 `fonts.css` 里用 `local()` 引用。仓库里没有任何中文字体文件 |
| `brand/agent/visual/assets/dieline/*` | 刀模几何由 open-dieline v1.4.1 生成（**PolyForm Noncommercial 1.0.0**） | 这里只放我们自己的输出文件（SVG、DXF、参数），**不含 open-dieline 的任何代码**。商用或给客户使用前，要先取得 open-dieline 的商用授权，或改由刀模厂出图 |
| logo、组件、锚点图、纹理、色板、截图、动效 | whynotdesign 自制 | 全部由本 kit 的代码生成，没有 AI 图 |
| `tools/`、`validation/` 里的脚本 | whynotdesign 自制 | 部分脚本写的是实验机上的路径（例如 `/workspace/...`），使用前要自行改掉 |
