# 在 Claude 使用 Skill

[项目首页](README.md) · [English](../en/CLAUDE-USAGE.md) · [使用示例](EXAMPLES.md)

| 使用环境 | 安装方式 | 怎么调用 |
| --- | --- | --- |
| **Claude Code** | 把 Skill 文件夹放到项目或个人的 `.claude/skills/`。 | 输入 `/amazon-listing-rewrite`，也可以直接说任务。 |
| **Claude 网页版** | 把 Skill 文件夹压成 ZIP，在 Claude 中上传并启用。 | 直接说要评分、改写或做竞品对比。 |
| **Claude 普通对话** | 在当前对话上传 `SKILL.md`。 | 要求 Claude 按文件里的流程处理原文和依据。 |

## Claude Code

1. 下载或克隆此仓库。也可以在 GitHub 首页通过 **Code → Download ZIP** 下载源文件。
2. 在要使用 Claude Code 的项目里创建 `.claude/skills/amazon-listing-rewrite/`。想在本机多个项目复用，可以放在个人目录 `~/.claude/skills/amazon-listing-rewrite/`。
3. 把 `SKILL.md` 放进 Skill 文件夹。将 `scripts/measure_fields.py` 一起放进其中的 `scripts/`，可在有 Python 的环境里精确计数。
4. 从项目目录启动 Claude Code，并调用 Skill。

~~~text
/amazon-listing-rewrite 帮我审核美国站这段标题和第一条五点。引用原文，告诉我最值得先改的地方。
~~~

项目里的完整路径是 `.claude/skills/amazon-listing-rewrite/SKILL.md` 和 `.claude/skills/amazon-listing-rewrite/scripts/measure_fields.py`。不同安装范围见官方说明。[Claude Code Skills 文档](https://code.claude.com/docs/en/skills)

## Claude 网页版

1. 本地新建 `amazon-listing-rewrite` 文件夹，放入 `SKILL.md` 和原相对路径下的 `scripts/measure_fields.py`。
2. 用下面的 YAML 替换本地副本开头的元数据，保留后面的指令全文。这个短描述符合 Claude 自定义 Skill 的 200 字符限制。
3. 压缩整个文件夹。打开 ZIP 后，第一层应看到 `amazon-listing-rewrite/`，其内部是 `SKILL.md` 和 `scripts/`。
4. 在 Claude 设置中启用代码执行和文件创建。组织工作区可能由管理员控制。进入 **Customize → Skills**，点 **+ → Create skill → Upload a skill**，选择 ZIP 并确认已启用。

~~~yaml
---
name: amazon-listing-rewrite
description: Look up Amazon ASINs, score listing copy, rewrite for Alexa for Shopping buyer questions, compare competitor features, and check field lengths against applicable rules.
---
~~~

只在当前对话使用时，可直接上传或粘贴仓库里的 `SKILL.md`。[Claude 自定义 Skill 打包说明](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills) · [启用和上传 Skill](https://support.claude.com/en/articles/12512180-use-skills-in-claude)

## 第一次怎么问

~~~text
用 Amazon Listing 改写 Skill，只改美国站第一条五点。我会给你原文、说明书和买家问句。请给候选稿、修改理由和字符数检查。
~~~

要查 ASIN 时，尽量补充目标站点和商品链接。联网查询取决于本次会话能使用的工具和能读取的来源。详情页无法核对时，可以补充原文、商品截图或 Listing 工作台导出。使用已有资料评分或改写，无需商品 API Key。

## 安装后如何检查

| 现象 | 检查方式 |
| --- | --- |
| Claude Code 找不到命令 | 确认从包含 `.claude/skills/` 的项目启动，或检查个人目录。核对文件夹名和 `SKILL.md`。 |
| Claude 网页版拒绝上传 | 核对 ZIP 顶层文件夹、短版 YAML 描述，以及代码执行和 Skills 开关。 |
| 能识别型号，但只读到部分字段 | 补充同 ASIN、同变体的资料，请它将仍缺失的字段标为未评分。 |
| 想要全英文报告 | 在请求里写「请用英文给我报告」。候选 Listing 文案默认使用目标站点语言。 |
