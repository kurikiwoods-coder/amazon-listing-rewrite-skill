# Amazon Listing 改写 Skill

**面向亚马逊卖家的免费 AI Skill，支持 Listing 评分、Alexa for Shopping 问句导向改写和竞品功能调研。**

[English](../../README.md) · [使用示例](EXAMPLES.md) · [Claude 使用指南](CLAUDE-USAGE.md) · [产品需求文档](REQUIREMENTS.md) · [Listing 工作台](https://github.com/kurikiwoods-coder/amazon-listing-workbench)

## 可以解决什么问题

输入 ASIN、商品链接，或粘贴现有文案。联网工具能读取对应详情页时，Skill 会先核对站点、子 ASIN、型号和变体。只发 ASIN 时，核对后会出现三个选项。已经知道要做什么，可以在第一句话里直接指定。

| 功能 | 适合解决的问题 | 你会拿到什么 |
| --- | --- | --- |
| **1. Listing 评分** | 哪个字段最值得先改？ | 逐字段文案分、原文短引和最多三个优先修改点。 |
| **2. Alexa 问句导向改写** | 买家能看懂这个功能怎么用、在什么条件下可用吗？ | 目标站点语言的候选文案、新旧对照、经核对的使用条件和字符数检查。 |
| **3. 竞品功能调研** | 同类商品有哪些功能，各自页面解释得清楚吗？ | 同站点功能对照、证据链接、买家问句及各页面的可回答性分。 |

## 快速开始

| 使用环境 | 怎么用 |
| --- | --- |
| **ChatGPT** | 工作区支持 Skills 时，在 **Plugins → Skills** 选择已安装的 Skill。新增时可使用 **Create → Upload from your computer**。[ChatGPT Skills 说明](https://help.openai.com/en/articles/20001066-skills-in-chatgpt) |
| **Codex** | 把 `SKILL.md`、`scripts/`、`agents/` 和 `assets/` 放到项目的 `.agents/skills/amazon-listing-rewrite/`，或个人目录的 `~/.agents/skills/amazon-listing-rewrite/`。用 `$amazon-listing-rewrite` 调用。[Codex Skills 说明](https://learn.chatgpt.com/docs/build-skills) |
| **Claude Code 或 Claude 网页版** | 在 Claude Code 使用本地 Skill 文件夹，或向 Claude 网页版上传 ZIP。指南列出两种方式的文件结构和元数据要求。[Claude 使用指南](CLAUDE-USAGE.md) |
| **普通 AI 聊天** | 上传或粘贴 `SKILL.md` 的全文，再提供 Listing 原文和依据。[查看 Skill 指令](../../SKILL.md) |

可以直接复制下面的请求。Skill 默认用简体中文解释，文案跟随目标站点语言。如需全英文报告，在请求里说明即可。

~~~text
查美国站 [ASIN]。只给能核对原文的字段打分，按优先级告诉我最值得改的三处。
~~~

~~~text
只改美国站第一条五点。买家想知道关闭 App 时能否看蛋白质。我会提供现有文案和设置说明。请对照新旧稿，给出修改理由并检查长度。
~~~

完整示例包含输入、候选稿和改写前后复评。[使用示例](EXAMPLES.md)

## 支持的数据和站点

| 你有的资料 | 怎么用 |
| --- | --- |
| **Amazon 链接或 ASIN** | 链接用实际域名定站点。只发 ASIN 时沿用当前对话的站点，无站点时先查美国站并注明。联网查询取决于当前 AI 的工具和商品页访问情况。 |
| **文案、已保存 HTML、截图、说明书或工作台导出** | 用已提供的字段和可核对的商品事实完成诊断。只改一条五点也可以。 |
| **Oxylabs 类目 CSV** | 筛选竞品 ASIN 和商品链接。评分或比较功能前，进一步核对对应详情文案和规格。[Oxylabs 项目](https://github.com/oxylabs/amazon-scraper) |
| **Alexa 实测记录** | 根据已核实事实检查回答，并记录引用和商品卡。只有买家问句时，也可以整理下一轮测试题。 |

只给有原文的字段打分。改写时保留已核实的规格、操作步骤和适用边界。字符数或字节数按站点、类目和字段核对，A+ 按具体模块核对。上限无法确认时，报告实际长度并标记规则待核。

## 搭配 Listing 工作台

在 ASIN 项目中进入 **Listing 诊断 → 导出 Alexa Skill 输入**，取得包含文案快照、已知事实、买家问句和诊断证据的 Markdown。交给 Skill 后，人工核对候选稿，再回到工作台保存和复评。[Amazon Listing 工作台](https://github.com/kurikiwoods-coder/amazon-listing-workbench)

## 项目结构

| 路径 | 内容 |
| --- | --- |
| [SKILL.md](../../SKILL.md) | 查询、评分、改写和调研的执行指令。 |
| [scripts/measure_fields.py](../../scripts/measure_fields.py) | 用 Python 标准库按字符或 UTF-8 字节计数。 |
| [agents/](../../agents/) 和 [assets/](../../assets/) | OpenAI 调用配置与 Skill 图标。 |
| [docs/en/](../en/) | 英文示例、Claude 指南和产品需求。 |
| [docs/zh-CN/](./) | 中文首页和对应文档。 |

| 文档 | 简体中文 | English |
| --- | --- | --- |
| 使用示例 | [EXAMPLES.md](EXAMPLES.md) | [EXAMPLES.md](../en/EXAMPLES.md) |
| Claude 使用指南 | [CLAUDE-USAGE.md](CLAUDE-USAGE.md) | [CLAUDE-USAGE.md](../en/CLAUDE-USAGE.md) |
| 产品需求文档 | [REQUIREMENTS.md](REQUIREMENTS.md) | [REQUIREMENTS.md](../en/REQUIREMENTS.md) |

## 常见问题

**一定要有 API Key 吗？** 处理你提供的文案和依据时，可直接运行。联网查询和可选的商品数据接口取决于所用 AI 和账号权限。

**只读到了部分字段怎么办？** 可以提供 Listing 快照、卖家后台导出或要改的一段文案。缺失字段标为未评分。

**Alexa 相关功能会检查什么？** 它会核对 Listing 能否回答买家问题，并指出每个答案的原文依据。你提供真实测试记录后，还可复核 Alexa 的答复与商品卡。

## 参考项目

买家问句覆盖、前台巡检和竞品发现参考了以下项目。文档以卖家的使用场景和工作流程组织。

[Alexa Listing 优化](https://github.com/liangdabiao/amazon-listing-alexa-optimizer) · [Zach 的 Amazon Skills](https://github.com/zach22-1999/amazon-skills) · [Amazon Sorftime MCP Skills](https://github.com/liangdabiao/amazon-sorftime-research-MCP-skill) · [Nexscope Amazon Skills](https://github.com/nexscope-ai/Amazon-Skills)
