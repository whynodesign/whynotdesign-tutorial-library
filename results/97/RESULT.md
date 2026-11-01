# 97 · Glyphs-mcp（thierryc）
来源：https://github.com/thierryc/Glyphs-mcp/ （v2.5.0，clone 于 2026-11-01）

## 结论：跑不通（缺 macOS 和 Glyphs 4）
- README 写明：v2 只支持 **Glyphs 4**，Glyphs 3 要用另一个 v1.11.0 版本。安装包是 macOS 的 `Glyphs-MCP-2.5.0.dmg`，要先装 Glyphs 4（可以试用，也可以用正式授权），再通过 Glyphs 插件管理器装 Python。
- 本机是 Debian Linux。我试着在 venv 里装 `requirements-dev.txt`，好跑仓库自带的离线测试，结果失败：`error: PyObjC requires macOS to build`（`pip_error_excerpt.txt`，完整日志在 `pip_install_full.log`）。所以连离线单元测试都跑不了。
- 没下载 DMG，没申请 Glyphs 试用，没注册任何账号。

## 实际产出
- `screenshot.png`：安装失败的记录图。
- 没有字体文件。

## README 讲清楚的
- 架构是 Glyphs 内桥接插件，加独立的 MCP 侧车。提供 21 个数据/操作工具：开字体、读字形、间距、kerning、OpenType feature 诊断、导出静态/可变/网页字体。
- 每次编辑都可以撤销，保存要单独授权。版本限制说得很清楚。

## 省略或夸大
- 没有夸大，但 README 很长、版本历史很绕（v1/v2、Glyphs 3/4），新用户上手成本高。
- 需要付费软件：第 42 条帖子里写 Glyphs 3 是 €319。Glyphs 4 的价格这次没查。

## 对 whynotdesign 有没有用
潜力 4/5，实测 0：如果工作室有 Mac 和 Glyphs 授权，这是让 agent 帮忙做间距、kerning、feature 检查的最完整方案。想试的话，要在何宇軒自己的 Mac 上装 Glyphs 4 和 Glyphs MCP.app。
没装 Glyphs 的话，替代方案是第 98 条 fontforge-mcp（Linux 已跑通）。

## 授权风险
仓库是 Apache-2.0，可以商用；Glyphs 本体是付费授权。

## 发布说明（GitHub 图库）
- 这些结果是**概念草稿**，不是定稿。
- 所有刀模 / 刀版都只是**原型级**，投产前必须和刀模厂打样校对。
- 所有 logo / mark 都**没有做商标检索**，不是可注册的商标定稿。
