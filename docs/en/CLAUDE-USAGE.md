# Use the skill in Claude

[Project home](../../README.md) · [简体中文](../zh-CN/CLAUDE-USAGE.md) · [Examples](EXAMPLES.md)

| Environment | Install once | Start a request |
| --- | --- | --- |
| **Claude Code** | Place the skill folder under a project or personal `.claude/skills/` directory. | Use `/amazon-listing-rewrite` or ask in plain language. |
| **Claude web app** | Upload a ZIP containing the skill folder and enable it. | Ask in plain language for a listing audit, a rewrite, or a competitor comparison. |
| **Claude chat with an attachment** | Attach `SKILL.md` to the conversation. | Ask Claude to apply the instructions to the copy and evidence you provide. |

## Claude Code

1. Download or clone the repository. From the repository home page, **Code → Download ZIP** gives you the source files.
2. In the project you use with Claude Code, create `.claude/skills/amazon-listing-rewrite/`. For a personal installation across local projects, use `~/.claude/skills/amazon-listing-rewrite/`.
3. Copy `SKILL.md` into that folder. Copy `scripts/measure_fields.py` into the folder's `scripts/` subdirectory so Claude can run the exact length check when Python is available.
4. Start a Claude Code session in the project and invoke the skill.

~~~text
/amazon-listing-rewrite Audit the supplied Amazon US title and first bullet. Quote the evidence for the top fix and give me the report in English.
~~~

The expected project layout is `.claude/skills/amazon-listing-rewrite/SKILL.md` and `.claude/skills/amazon-listing-rewrite/scripts/measure_fields.py`. See the official guide for personal, project, and organization skill locations. [Claude Code Skills](https://code.claude.com/docs/en/skills)

## Claude web app

1. Make a local folder named `amazon-listing-rewrite` and copy `SKILL.md` and `scripts/measure_fields.py` into it, keeping the `scripts/` directory.
2. In your local copy of `SKILL.md`, replace the opening YAML block with the one below and keep the rest of the instructions. The shorter description fits Claude's 200-character limit for custom skill descriptions.
3. Compress the folder itself so `amazon-listing-rewrite/` is the top-level entry inside the ZIP. Inside that folder, `SKILL.md` is next to `scripts/`.
4. Enable code execution and file creation in Claude settings. In an organization workspace, the workspace owner may control this capability. Go to **Customize → Skills**, use **+ → Create skill → Upload a skill**, and select the ZIP. Check that the uploaded skill is enabled.

~~~yaml
---
name: amazon-listing-rewrite
description: Look up Amazon ASINs, score listing copy, rewrite for Alexa for Shopping buyer questions, compare competitor features, and check field lengths against applicable rules.
---
~~~

The repository copy can also be pasted or attached directly to a Claude conversation. For a persistent web installation, use the folder and ZIP steps above. [Claude custom skill packaging](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills) · [Enable and upload skills](https://support.claude.com/en/articles/12512180-use-skills-in-claude)

## Send a first request

~~~text
Use Amazon Listing Rewrite to improve only Bullet 1 for my Amazon US listing. I'll supply the original text, the product manual excerpt, and the buyer question. Return a candidate bullet, the reasons for each change, and the length check in English.
~~~

For an ASIN lookup, state the marketplace and include a URL if you have one. Lookup depends on the web tools enabled for that session and which sources they can read. If a detail page cannot be verified, attach the relevant copy, a product screenshot, or a Listing Workbench export. With supplied materials, the audit and rewrite can run without a marketplace API key.

## Verify setup

| What you see | What to check |
| --- | --- |
| Slash command is missing in Claude Code | Start the session in a project that contains the expected `.claude/skills/` path, or check the personal path. Confirm the filename and folder name. |
| Claude rejects the ZIP | Inspect the top-level folder, use the shorter YAML description shown above, and check that code execution and skills are enabled. |
| Claude finds the model but only reads part of the listing | Supply the missing text for the exact ASIN and variant. Ask it to mark still-unavailable fields as unscored. |
| You want the report in English | Add “Give me the report in English.” Candidate listing copy follows the target marketplace language unless you ask otherwise. |
