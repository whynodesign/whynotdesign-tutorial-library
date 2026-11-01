# 98 · fontforge-mcp（LHxis）
来源：https://github.com/LHxis/fontforge-mcp （clone 于 2026-11-01）

## 结论：跑通
- apt 源报 500，装不了 `python3-fontforge`；改用 FontForge 官方 AppImage **20251009**，解包到 `/workspace/tools/`。
- 写了一个 3 行的胶水脚本 `/workspace/tools/ffpython`：把 AppImage 内嵌的 Python 3.10 当成解释器，用 `FFPYTHON` 指过去。这正是 README 支持的做法。
- venv 装 `requirements.txt` → `bridge.py` 找到解释器 → `selftest.py` **13/13 通过**（MCP 握手、30 个工具、生成 TTF/OTF/WOFF2、预览、出错后服务不崩）。
- 实测：用 Python MCP 客户端走真正的 MCP stdio 协议（和 Claude Code 是同一条路径；胶水脚本 `mcp_session.py`）。把焙曲 5 个焙度 mark（`exp09/svg/level_1–5.svg`）做成图标字体。每一次调用都记在 `mcp_transcript.md`。

## 实际产出
| 文件 | 说明 |
|---|---|
| `TONEROAST-RoastMarks.ttf` / `.woff2` | 图标字体：U+E000–E004 对应 level_1–5，数字 `1`–`5` 也映射到对应焙度 |
| `work/TONEROAST-RoastMarks.sfd` | FontForge 源文件 |
| `preview_13_ff_preview.png` | 字形「three」的轮廓图（带控制点） |
| `preview_14_ff_preview.png` | 全字形表 |
| `preview_15_ff_preview.png` | 文本「12345」渲染 |
| `screenshot.png` | 三张拼图 |

## 实测观察
- 第一次 `ff_validate` 报 10 个「non-integral coordinates」。按工具提示跑 `ff_clean_glyph(round_coords=True)` 后变成 0 个问题。这个工具链会自己暴露问题，也会告诉你怎么修。
- **字体是单色的**：mark 里的琥珀色块和红点全变成黑色，色块还和谱线合并了。要彩色得做 COLR 字体，这次没测。
- `ff_import_svg_folder` 会把 PUA 字形缩到 78% 的 ascender 高，用 `ff_import_svg` 导入的数字字形不会缩，两组大小不一致。字形左右边距都是 0，连排时会贴在一起，要再跑 `ff_auto_metrics` 或手动设边距。

## README 讲清楚的
- 为什么要拆成两个进程、每个系统怎么装、先跑 `bridge.py` 和 `selftest.py` 再注册，都写得很清楚，是这批里文档最好的之一。

## 省略或夸大
- 「design fonts」：实际是「从 SVG 路径或 SVG 文件组装和修字体」，AI 不会替你画好字形。

## 对 whynotdesign 有没有用
高（4/5）：可以把品牌图形或图标做成字体（网页、包装系统里用）。也能批量修轮廓、导 WOFF2、出字样，不需要 Glyphs，Linux 和 Mac 都能用。

## 授权风险
代码 MIT，FontForge GPLv3，生成的字体归使用者。字体里的 mark 是 Exp09 的实验资产，不是正式 VI。

## 发布说明（GitHub 图库）
- 这些结果是**概念草稿**，不是定稿。
- 所有刀模 / 刀版都只是**原型级**，投产前必须和刀模厂打样校对。
- 所有 logo / mark 都**没有做商标检索**，不是可注册的商标定稿。
