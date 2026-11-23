# 使用示例

[项目首页](README.md) · [English](../en/EXAMPLES.md) · [Claude 使用指南](CLAUDE-USAGE.md)

## 用现有文案跑完整流程

这个练习使用虚构营养秤和模拟说明书。可以在支持的 AI 中选中 Skill，或随请求上传 `SKILL.md`。全部证据都在输入里，可以直接试用。

### 复制这段请求

~~~text
请用 Amazon Listing 改写 Skill。

站点：Amazon US
商品：DemoCo Nutrition Kitchen Scale N1（虚构）
任务：先审核，再只改标题和第一条五点。
本例标题上限：75 字符，含空格。

标题：DemoCo Smart Nutrition Kitchen Scale for Every Meal, Meal Prep and Daily Food Tracking with Calories and Protein
第一条五点：Track meals with live calories and protein on the scale.

虚构 N1 说明书核实了以下事实：
1. 开始用这个功能前，需先在 App 中把食物保存到秤上。
2. 称量时在秤上选择一项已保存的食物。
3. 关闭 App 时，秤屏可以显示该食物的热量和蛋白质。
4. 关闭蓝牙或断网后的表现尚未核实。

优先回答的买家问题：关闭 App 时，我能在秤屏直接看热量和蛋白质吗？第一次要怎么设置？

请给已有文案打分，列出最需要改的问题和原文依据。检查改写后的字段长度，再用同一问句复评。
~~~

### 示例输出

**先改第一条五点，把设置和称量步骤写清楚。** 原文提到了热量和蛋白质，但没有说什么时候需要 App、什么时候必须选择已保存的食物。标题也超出了本例上限 37 字符。

| 优先级 | 字段与依据 | 修改意见 |
| --- | --- | --- |
| P0 | 标题 112 字符，本例上限为 75 字符 | 删除泛泛的备餐和记录描述，保留品牌、型号、产品类型和可在秤屏查看的信息。 |
| P1 | 第一条五点写的是 “Track meals with live calories and protein on the scale.” | 补上首次用 App 保存、称量时选择已保存食物，以及关闭 App 时可在秤屏查看的条件。 |

**候选标题**

~~~text
DemoCo Nutrition Kitchen Scale N1 with On-Scale Calories and Protein
~~~

**第一条五点候选稿**

~~~text
Save foods to the scale in the app first. Then select a saved food on the scale to view calories and protein on its screen as you weigh with the app closed.
~~~

| 字段 | 原文 → 候选 | 上限和结果 |
| --- | --- | --- |
| 标题 | 112 → 68 字符 | 本例最多 75 字符，候选稿通过。 |
| 第一条五点 | 56 → 156 字符 | 类目上限待核，发布前确认。 |
| A+、Item Highlights 及其他字段 | 未评分 | 本例提供了标题和一条五点。 |

下面的示例分数按相同四项前后对照，每项满分 25。总分取两段已评文案的平均值，此处保留一位小数。

| 字段 | 直接回答 | 具体性 | 事实与边界 | 清晰与去重 | 总分 |
| --- | --- | --- | --- | --- | --- |
| 标题改前 → 改后 | 15 → 20 | 17 → 19 | 19 → 22 | 10 → 24 | 61 → 85 |
| 第一条五点改前 → 改后 | 12 → 25 | 10 → 24 | 14 → 25 | 20 → 24 | 56 → 98 |
| **整体** | | | | | **58.5 → 91.5** |

**用同一问句复评。** 原文只回答了可看哪些营养指标，属于部分支持。候选稿按 N1 说明书交代了三个条件。先用 App 保存食物，称量时从秤上选中该食物，然后在关闭 App 时看秤屏。蓝牙和网络的使用边界留待核实。表中分数用于对照文案质量。

## 只输入 ASIN

~~~text
查 Amazon 美国站 B0F1N26FT3。先确认商品和变体，列出你能核对的 Listing 字段。然后给现有字段打分，告诉我最值得先改的一处。
~~~

结果应给出站点、变体、来源链接、读取日期和可用字段。遇到访问限制时，可用同站点、同变体的归档，或补充原文。示例中的 ASIN 用于演示查询输入，实际页面以当次资料为准。

## 做竞品功能调研

~~~text
用 Amazon Listing 改写 Skill，给这个 ASIN 找最多三款同站点的可替代商品。我关心首次设置、关闭 App 能否使用、屏幕会显示什么。请引用说明这些功能的原文，每项给一个买家问法，再给各页面的可回答性打分。
~~~

每款商品都会列出功能是否具备，以及页面有没有说清楚。比如竞品明确写出营养数据只能在 App 中查看，页面也可以拿到该问题的 2 分。相关字段无法核对时标 N/A。AI 拟出的问法会标为候选测试题，附真实 Alexa 记录后可继续核对实际答复。
