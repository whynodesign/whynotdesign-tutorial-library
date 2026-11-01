# 36 · @Salmaaboukarr 刀版 → Blender 折盒动画（GPT 6 Astra 提示词）
来源：https://x.com/Salmaaboukarr/status/2096612394281603144 。提示词全文、原帖参考刀版 `source/dieline_ref.png`、演示视频 `source/demo.mp4` 都在 `source/`。

## 结论：部分跑通（我替代了 GPT 6 Astra）
- apt 源报 500，装不了包；改从 download.blender.org 下载官方 **Blender 4.2.23 LTS** 便携版，放在 `/workspace/tools/`。
- 我没有 GPT 6 Astra。按原帖方法：把提示词和刀版交给大模型（这里是我），让它写 Blender Python，然后在 Blender 里无头运行。所以测的是「LLM 写 Blender 脚本」这条路能不能通，**不能代表 GPT 6 Astra 本身的水平**。
- 输入刀版：用第 85 条 open-dieline 导出的焙曲 RTE 70 × 45 × 120（`input_dieline_from85.png`）。尺寸从导出文件里读，没用提示词默认的 300 × 300 × 95。

## 实际产出
| 文件 | 说明 |
|---|---|
| `fold_carton.py` | 生成的 Blender 脚本，约 90 行；尺寸写在文件顶部，方便改，假设条件记在 `dieline_root["ASSUMPTIONS"]` |
| `toneroast_rte_fold.blend` | 可编辑模型：每块面板一个铰链枢轴，0.45 mm 实体化厚度，有关键帧 |
| `toneroast_fold_unfold.mp4` | 540 × 540、30 fps、8 秒、240 帧：折合 → 停留 → 展开（Cycles CPU） |
| `key_0001/0050/0090/0125.png` | 关键帧（平展 / 墙板折起 / 盖子合到一半 / 闭合） |
| `screenshot.png` | 四张关键帧拼图 |

## 核对
- 100% 时盒子能闭合，盖子正好盖住开口。插舌和防尘翼简化成梯形，没有锁扣。
- 糊边折进内侧，但没有和后片粘在一起。面板厚度不参与碰撞，局部会穿插。

## 原帖讲清楚的
- 提示词结构很好：参考优先级、面板清单、「没给尺寸就用 300 × 300 × 95 并标成假设」、尺寸要方便修改。

## 省略或夸大
- 提示词是给翻盖邮购盒（mailer）写的，面板清单换成别的盒型要自己改。
- 作者自己在回复里承认动画「not perfect, quick test」。有评论指出原视频里的盒子侧边少了双层壁。
- 演示依赖 GPT 6 Astra 自动驱动 Blender，换别的模型能不能一次成功，原帖没说。

## 对 whynotdesign 有没有用
中（3/5）：可以做「刀模 → 折盒」的提案动画和技术展示。前提是刀模来自 85、86、87 这类参数化工具，而且要有人检查脚本。

## 授权风险
Blender 是 GPL，但渲染出来的东西归使用者，可以商用。动画里的 mark 和文字来自 exp09 的实验资产，不是最终品牌。

## 发布说明（GitHub 图库）
- 这些结果是**概念草稿**，不是定稿。
- 所有刀模 / 刀版都只是**原型级**，投产前必须和刀模厂打样校对。
- 所有 logo / mark 都**没有做商标检索**，不是可注册的商标定稿。
