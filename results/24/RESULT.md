# #24 @emmettshine《Brands for Humans & Agents》（Little Plains「双原生品牌系统」）— 实测结果

- 原帖：https://x.com/emmettshine/status/2024113482623258907（X 长文，2026-02-18，已用 x 公开读取）
- **状态：跑通**（方法本身是一套文件结构，不是工具）。按文章的方法给焙曲建了「Agent-First Brand Kit」：
  - 每个 chunk 约 400 token 以内，带 front matter（chunk_id、domain、context_tags、depends_on、version、status、summary）。
  - 用 `_retrieval-rules.yaml` 按任务决定加载哪些 chunk，并设 token 预算。
  - 然后实际用了一次：按 `packaging_label` 任务装配上下文，写生图提示词，出 1 张罐标图；按 `social_media` 任务写 1 段文案，并对照 chunk 自查。

## 产出（/workspace/tutorial-tests/24/）
- `brand-kit/`：
  - `positioning/positioning-core.yaml`
  - `messaging/voice-core.md`
  - `identity/visual-system.json`、`identity/terminology.yaml`
  - `guardrails/constraints-visual.yaml`、`guardrails/constraints-messaging.yaml`
  - `_retrieval-rules.yaml`（3 个任务：social_media / packaging_label / image_prompt）
- `assemble.py`（胶水：粗算 token，按任务装配上下文）、`assemble_log.txt`
- `context_*.txt`（3 个任务装配出的上下文）
- `label_from_chunks.jpg`：只按装配出的上下文写提示词生成的罐标图
- `social_caption_sample.md`、`screenshot.png`
- 文章里列的 15–20 个 chunk 只建了 6 个；persona、brand-values、voice-translations、messaging-framework 没建。

## 结果观察
- 罐标图**遵守了全部 guardrail**：没有茶叶、茶壶、山、书法、金箔，繁体中文，余烬红只有一个点，没有 logo（visual-system 里 logo=null，模型就没有乱编 symbol）。但烘焙记录「焙度 4 · 6 回」被并成了「焙度 4·6回」。
- 各 chunk 实测 71–328 token（粗估），三个任务装配后 305 / 748 / 403 token，都在预算内。
- 好处很直接：给生图模型或文案 agent 的上下文是**可控、可复用、可版本化**的，不用每次手写品牌描述。

## 原帖讲清楚的
- 两层交付：给人的（Figma、PDF、规范）和给 agent 的（Markdown、YAML、JSON），两者内容同源。
- chunk 化 + front matter + 按任务检索的规则，并给了 positioning-core.yaml 和 retrieval rules 的真实示例。
- 完整 chunk 清单（positioning / messaging / audience / identity / guardrails 五类）。

## 省略或夸大
- 文章主要讲文案和声音，**视觉部分只有一个 visual-system.json 的名字**，没有示例。对设计工作室来说，最关键的视觉规则（logo 用法、版式、摄影）怎么写成 chunk，文章没讲。
- 「400 token」是经验值，文章没给检索效果的对比。
- 文章后半段在讲他们的内部 agent（Donna 的 soul.md），和品牌系统关系不大。

## 对 whynotdesign 有没有用
- **有用**：whynotdesign 的 Muse Lab 和 v5 流程本来就靠提示词，把客户品牌整理成 chunk + 检索规则，可以直接喂给生图、文案和动效 agent。Thread Lab 之前提的 `brand.json` 就是这里的 visual-system chunk。
- 建议补一个视觉侧的 chunk 规范（logo 用法、版式、摄影、禁用项），这是文章空着的部分。
- **有用度：4/5**

## 授权风险
- 方法本身没有授权问题（文章里的示例属于 Little Plains，这里没有照抄内容，只用了结构）。
- 罐标图是 AI 生成的概念图，上面的文字不能当成品，「焙曲」字标要用真字体重排。

## 与 exp09 的对比
- exp09 的 template_brand_proposal.md（12 段）+ Brand Lock 表，本质上就是一个大 chunk。按这里的方法拆开后，可以按任务只加载需要的部分（例如生图只加载 visual + constraints），也能减少 exp09 里「锚点上的说明文字外溢进成品」的问题。

## 发布说明（GitHub 图库）
- 这些结果是**概念草稿**，不是定稿。
- 所有刀模 / 刀版都只是**原型级**，投产前必须和刀模厂打样校对。
- 所有 logo / mark 都**没有做商标检索**，不是可注册的商标定稿。
