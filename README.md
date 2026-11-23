# Amazon Listing Rewrite Skill

**A free AI agent skill for Amazon sellers to audit listing copy, rewrite for Alexa for Shopping buyer questions, and compare competitor features.**

[简体中文](docs/zh-CN/README.md) · [Examples](docs/en/EXAMPLES.md) · [Claude setup](docs/en/CLAUDE-USAGE.md) · [Product requirements](docs/en/REQUIREMENTS.md) · [Listing Workbench](https://github.com/kurikiwoods-coder/amazon-listing-workbench)

## What you can do

Start with an ASIN, an Amazon product URL, or the copy you already have. When a web tool can read the matching detail page, the skill checks the marketplace, child ASIN, model, and variant. An ASIN alone opens a three-option menu after lookup. Include the task in your message to go straight to it.

| Workflow | Question it helps answer | What you get |
| --- | --- | --- |
| **1. Listing audit** | Which part of this listing should I review first? | Field-by-field copy scores, short quotes, and up to three priority fixes tied to specific fields. |
| **2. Alexa question-led rewrite** | Can a buyer tell how a feature works and when it applies? | Edited copy in the marketplace language, a before-and-after comparison, verified usage conditions, and field-length checks. |
| **3. Competitor research** | Which comparable products support the feature, and how clearly does each listing explain it? | A same-marketplace comparison of features, evidence, buyer questions, and how well each listing answers them. |

## Quick start

| Where you work | How to use it |
| --- | --- |
| **ChatGPT** | If Skills is available in your workspace, open **Plugins → Skills** and select the installed skill. To add a copy, use **Create → Upload from your computer**. [ChatGPT Skills help](https://help.openai.com/en/articles/20001066-skills-in-chatgpt) |
| **Codex** | Copy `SKILL.md`, `scripts/`, `agents/`, and `assets/` into `.agents/skills/amazon-listing-rewrite/` in your project or `~/.agents/skills/amazon-listing-rewrite/` for personal use. Invoke it with `$amazon-listing-rewrite`. [Codex Skills documentation](https://learn.chatgpt.com/docs/build-skills) |
| **Claude Code or Claude web app** | Use the local Skill folder in Claude Code or upload a ZIP to Claude. The setup guide includes the metadata and folder layout for each. [Claude setup](docs/en/CLAUDE-USAGE.md) |
| **A regular AI chat** | Attach `SKILL.md` or paste its contents, then send the listing and supporting facts. [Skill instructions](SKILL.md) |

Try either of these prompts. The skill explains its findings in Simplified Chinese by default. Ask for an English report if you prefer.

~~~text
Look up this Amazon US ASIN [ASIN]. Audit the fields you can verify and show the top three fixes. Give me the report in English.
~~~

~~~text
Rewrite only Bullet 1 for Amazon US. Buyers ask whether they can see protein with the app closed. I'll provide the current bullet and the setup instructions. Show the old and new text, explain the change, and check its length.
~~~

The worked example includes complete input, candidate copy, and a before-and-after check. [Examples](docs/en/EXAMPLES.md)

## Data and marketplaces

| What you have | How it is used |
| --- | --- |
| **Amazon URL or ASIN** | The URL identifies the marketplace. A bare ASIN uses the conversation's marketplace or starts with Amazon US, with the default stated in the report. Live lookup uses the host's available web tools and depends on page access. |
| **Copy, saved HTML, screenshots, manuals, or workbench export** | Work from the fields and product facts you can supply. A single bullet is enough for a targeted edit. |
| **Oxylabs category CSV** | Find candidate ASINs and listing URLs. Verify the product detail copy and specifications separately before auditing or comparing features. [Oxylabs project](https://github.com/oxylabs/amazon-scraper) |
| **Alexa test records** | Compare observed answers against verified product facts and record citations and product cards. A new test plan can be generated from supplied buyer questions. |

Audit scores cover fields with source copy. A rewrite preserves verified specifications, setup steps, and limitations. Length checks use the applicable marketplace, category, and field or A+ module. If a limit is unavailable, the report gives the measured length and flags the rule for review.

## Listing Workbench

In a workbench ASIN project, open **Listing Diagnostics → 导出 Alexa Skill 输入** to export the current copy, known facts, buyer questions, and audit evidence as Markdown. Give the export to the skill, review the proposed copy, and save the accepted version in the workbench for reassessment. [Amazon Listing Workbench](https://github.com/kurikiwoods-coder/amazon-listing-workbench)

## Repository guide

| Path | Contents |
| --- | --- |
| [SKILL.md](SKILL.md) | Agent instructions for lookup, audit, rewrite, and research. |
| [scripts/measure_fields.py](scripts/measure_fields.py) | Standard-library Python counter for characters or UTF-8 bytes. |
| [agents/](agents/) and [assets/](assets/) | OpenAI interface metadata and the skill icon. |
| [docs/en/](docs/en/) | English examples, Claude setup, and product requirements. |
| [docs/zh-CN/](docs/zh-CN/) | Chinese README and matching Chinese guides. |

| Guide | English | 简体中文 |
| --- | --- | --- |
| Examples | [EXAMPLES.md](docs/en/EXAMPLES.md) | [EXAMPLES.md](docs/zh-CN/EXAMPLES.md) |
| Claude setup | [CLAUDE-USAGE.md](docs/en/CLAUDE-USAGE.md) | [CLAUDE-USAGE.md](docs/zh-CN/CLAUDE-USAGE.md) |
| Product requirements | [REQUIREMENTS.md](docs/en/REQUIREMENTS.md) | [REQUIREMENTS.md](docs/zh-CN/REQUIREMENTS.md) |

## FAQ

**Do I need an API key?** Supplied copy and evidence can be analyzed without a marketplace API key. Web lookup and optional data-provider access depend on your agent and account.

**What if only some fields are visible?** Provide a listing snapshot, Seller Central export, or the individual text you want reviewed. Missing fields appear as unscored.

**What does the Alexa workflow check?** It checks whether the listing answers the buyer's question, then shows which sentence supports each answer. Actual Alexa answers and product cards can be reviewed from test records you supply.

## References

The listing methodology draws on buyer-question coverage, storefront health checks, and competitor discovery. The project documentation is organized around seller use cases and common workflows.

[Alexa Listing Optimizer](https://github.com/liangdabiao/amazon-listing-alexa-optimizer) · [Zach's Amazon Skills](https://github.com/zach22-1999/amazon-skills) · [Amazon Sorftime MCP Skills](https://github.com/liangdabiao/amazon-sorftime-research-MCP-skill) · [Nexscope Amazon Skills](https://github.com/nexscope-ai/Amazon-Skills)
