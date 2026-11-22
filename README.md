# Amazon Listing 改写 Skill

把 Amazon 商品标题、Item Highlights、五点、A+ 或商品描述交给 AI。它会找出哪些买家问题没有说清楚，引用对应原文，给出建议改写和理由，再用同一批问题复评。可以只改一条五点，也可以处理整份 Listing。任何类目都能从已经提供的内容开始。

[打开 Skill 指令](SKILL.md) · [打开 Amazon Listing 工作台](https://github.com/kurikiwoods-coder/amazon-listing-workbench)

## 1. 直接给 AI 用

1. 下载 [SKILL.md](SKILL.md) 并上传给 AI，也可以把文件全文粘贴进对话。
2. 上传或粘贴要改的 Listing 原文。已知时，附上站点、ASIN、精确型号或变体、已确认事实及来源。手头有真实买家问句或 Alexa 实测问句，也一起给出。
3. 发送下面的请求。只有一条英文原文时，先从这一条开始。

```text
请按 SKILL.md 诊断、改写并复核我提供的 Listing。
站点：Amazon US
型号或 ASIN：[填写已知信息]
改写范围：只改第 1 条五点
原文：[粘贴原文]
已确认事实及来源：[例如产品说明书「首次设置」一节]
优先回答的买家问题：[粘贴真实问句，有则提供]

请先指出卡住购买判断的地方，给出原文引文、英文改写和中文修改理由。
用同一问题对照改写前后的可回答性，最后给我可复制的候选文案。
```

如果只提供 ASIN 或链接，AI 能读取的内容取决于当前工具和访问权限。网页无法读取或变体无法核对时，粘贴对应型号的原文、上传截图或使用工作台导出。

## 2. 从工作台接着改

1. 在 [Amazon Listing 工作台](https://github.com/kurikiwoods-coder/amazon-listing-workbench) 打开 ASIN 项目，进入 **Listing 诊断 → 导出 Alexa Skill 输入**。
2. 将导出的 Markdown 与 Skill 一起交给 AI。导出可提供 Listing 快照、字段核验状态、产品事实、买家问句和诊断引文。
3. 核对 AI 给出的原文位置、英文候选稿和待核实事项。把通过核对的候选稿带回工作台，保存版本并复评。

两个仓库通过文档互链。工作台与 AI 对话之间使用 Markdown 导出和人工回填。

## 3. 加载为可重复调用的 Skill

| 使用环境 | 操作 |
| --- | --- |
| ChatGPT 的 Skills 功能 | 如果账号可用，在 **Plugins → Skills** 中查找已安装的 `amazon-listing-rewrite`，也可从 **Create → Upload from your computer** 使用本仓库的 Skill 文件。 |
| Codex | 将 `SKILL.md`、`agents/` 和 `assets/` 保持相对位置，放入当前项目的 `.agents/skills/amazon-listing-rewrite/`，或本人目录的 `~/.agents/skills/amazon-listing-rewrite/`。打开该项目后，用 `$amazon-listing-rewrite` 开始请求。 |
| 普通 AI 聊天 | 每次新开对话时上传 `SKILL.md` 或粘贴全文，再提供原文与依据信息。 |

[ChatGPT Skills 帮助](https://help.openai.com/en/articles/20001066-skills-in-chatgpt) · [Codex Skills 文档](https://learn.chatgpt.com/docs/build-skills)

## 4. 改写和复评规则

| 规则 | 怎么处理 |
| --- | --- |
| 先解决购买疑问 | 优先使用真实问句。缺少问句时，从已有文案拟定 3–5 个购买问题并标明来源。每项诊断给出字段、原文引文和影响。 |
| 以同一型号的事实为准 | 保留适用范围、参数和限制。原文中尚无依据的声明标为待核实。评论、竞品、其他变体和 AI 回答可用于发现问题。 |
| 按字段改 | 标题明确商品身份，Item Highlights 补充决策信息，五点逐条回答购买问题，A+ 或描述交代操作和使用边界。用户只指定一个字段时，改写范围跟随指定字段。 |
| 按实际原文评分 | 用户要求评分时，每个已提供的模块按直接回答、具体性、事实与边界、清晰与去重各 25 分。总分取已评分模块平均，缺失项标为未评分。总分差只比较共同模块。 |
| 复核规则与事实 | 字符数、用语和格式按适用站点、类目和生效规则核对。规则或资料还未确认时，列出具体核验项。后台 Search Terms 在用户要求时给备选。 |

## 5. 如何看结果

输出依次给出优先问题、原文和建议改写对照、可复制候选稿，以及同一组问句的前后判断。解释默认用简体中文，候选文案使用目标站点语言。

例如，若已核实某演示营养秤要先在 App 保存食物，之后选中已保存的食物才能在秤屏看热量，草稿就应明确这两个阶段。蓝牙断开与断网使用的能力分别留待核验。这个例子只演示如何保留条件，实际改写以目标型号资料为准。

候选稿由运营核对后人工发布。文案复评分用于对照表达改善。需要了解实际 Alexa for Shopping 表现时，在相同站点、入口和问句条件下分别记录回答、引用和目标商品卡。

## 仓库文件

- [SKILL.md](SKILL.md) 是 AI 执行指令。
- [agents/openai.yaml](agents/openai.yaml) 是调用界面配置。
- [assets/icon.svg](assets/icon.svg) 是 Skill 图标。
