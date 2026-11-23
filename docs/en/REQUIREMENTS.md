# Amazon Listing Rewrite Skill product requirements

[Project home](../../README.md) · [简体中文](../zh-CN/REQUIREMENTS.md) · [Worked example](EXAMPLES.md)

## Product goal

Give Amazon sellers and listing reviewers an evidence-based way to decide what to fix, draft the change, and check whether a buyer can now get the right answer. Support an individual field from any category, with marketplace- and category-specific checks where rules and sources are available.

## Seller needs covered

| Seller need | Current workflow | Result |
| --- | --- | --- |
| I have an ASIN and want to check I am looking at the right version. | **Product lookup** uses the marketplace and child variant. | An identity card with brand, model, variant, sources, dates, and available fields. |
| I have only a title and one bullet. I need to know which line is worth fixing. | **Listing audit** scores the submitted or verified fields. | A score for each available field, the assessed scope, and prioritized edits tied to quotes. |
| An Alexa answer missed an important condition about our product. | **Question-led rewrite** identifies the missing condition and checks it against the facts. | Candidate copy, the reason for each change, length checks, and reassessment on the same question. |
| I need to understand how alternative products handle the same buying need. | **Competitor research** compares the features and how clearly each listing answers. | A comparison table with model, capabilities, conditions, quotes, links, dates, and answerability scores. |
| I have records of real Alexa tests or earlier listing versions. | **Evidence review and reassessment** use the supplied records or a workbench export. | Labeled observations, copied quotes, and comparable before-and-after results. |

## Input and evidence requirements

| Input | Required handling |
| --- | --- |
| **Amazon product URL** | Resolve the retail marketplace and ASIN. Confirm the selected child variant matches the requested item before making product claims. |
| **Bare ASIN** | Use the marketplace requested in the conversation. Otherwise, start with US and label the default. With web access, look up the product before showing the three workflows. |
| **Listing text or saved evidence** | Accept a single field or a complete listing, including pasted copy, screenshots, saved HTML, a manual, or a Listing Workbench Markdown export. Record the source and relevant date. |
| **Oxylabs category CSV** | Read the ASIN, title, URL, image URL, and price as candidate data. Deduplicate by marketplace and child ASIN. Use matching detail sources for the actual listing or feature assessment. |
| **Seller rules or Alexa records** | Use the applicable marketplace and category evidence or the user's observed test records. Keep the quoted question, timestamp, and conditions attached to the observation. |

Track each field as **verified, captured but pending verification, unavailable, confirmed absent, or not applicable**. Record the archive capture date separately from retrieval time. A manufacturer manual or user-confirmed test for the same variant can establish a product fact. Reviews, Q&A, and competitor products can identify buyer needs.

If a website requests authentication, verification, or refuses access, end that lookup and continue with authorized data or the user's source material. If the listing and selected variant disagree, show both identifiers and ask which variant to use.

## Functional requirements

### Listing audit

- Score each field that has source copy on four criteria worth 25 points each. Check the direct answer, specificity, facts and boundaries, and clarity.
- Average the assessed field scores. Report the assessed scope and leave missing modules unscored. For a before-and-after comparison, use the fields scored in both versions.
- Quote the original and cite the field location. Mark verified fact or rule conflicts P0, gaps in important buyer answers P1, and lower-impact clarity edits P2.
- Report buyability observations such as shipping or Buy Box availability separately when requested. Record the marketplace, time, and conditions under which they were visible.

### Alexa question-led rewrite

- Convert a buyer question into checkable conditions. Describe what the product does, the required setup or action, and when the answer applies.
- Keep the rewrite within the requested fields. Tie each change to verified product facts and surface open questions beside the draft. Provide copy in the target marketplace language.
- Show the original, candidate copy, reason and source, length result, and reassessment on the same question set. Mark uncertain answers for review.
- A suggested test question is labeled as a proposal. For supplied Alexa test records, capture entry point, locale, session conditions, answer, sources, target ASIN, and sponsorship status. Compute answer correctness on the rounds that can be judged and show the sample size. Review recommendation appearances independently.

### Competitor research

- Use the user's comparison set when supplied. Otherwise, look for two to five suitable same-marketplace alternatives with verifiable evidence. Report the actual sample size and why each item was included.
- Show each product's feature status, steps or specifications, conditions, quote, and source. Preserve an explicit unknown when evidence is insufficient.
- Score each comparable question from 0 to 2. Clear and accurate answers score 2, partial answers score 1, and an absent or contradicted answer within the assessed scope scores 0. Use N/A when the relevant material is unavailable. Compare overall percentages using the questions assessable across the comparison set.
- Identify where each question came from, such as a buyer review, a user-recorded Alexa test, or a suggested prompt. Record frequency only when the source supports it.

### Field-length validation

- Resolve the marketplace, category, field, effective date, and unit. Apply limits at the right level, such as each bullet or each A+ text box.
- Report exact counts against the confirmed limit. Support both inclusive and strict limits and UTF-8 byte counts where applicable.
- If the rule is unresolved, give the measured length and label the rule for review. Review the final text in Seller Central before publishing.

## Acceptance checks

| Scenario | Expected result |
| --- | --- |
| Bare ASIN with a readable detail page | The response shows the actual marketplace and child variant, links the evidence, lists the fields, and offers the three workflows. |
| ASIN lookup with a blocked or unavailable detail page | The response says which source was accessible, labels gaps, and requests a matching copy or export where needed. |
| Title and one bullet provided, A+ unavailable | Scores cover the supplied text. A+ appears as unscored. |
| Source title length is 76 and the applicable cap is 75 | The source is flagged over the cap and the candidate is counted again. A candidate at 75 passes an inclusive cap. |
| Search Terms measured under a strict 250-byte example rule | 249 UTF-8 bytes pass. 250 bytes are over the limit. The applicable live rule is checked independently. |
| First-time setup requires an app and daily use is supported with the app closed | The draft preserves both facts and any saved-item condition. Bluetooth and network requirements follow the evidence. |
| A competitor explicitly says it lacks the feature | Its capability status reflects that fact. The page can still receive full points for a clear and accurate answer. |
| Alexa observations are unavailable | The output provides proposed questions and the listing answerability assessment. |

## System boundaries and later work

The skill runs in the host assistant. It can work with provided files and any authorized product data tools available to that host. Review and publish approved drafts in Seller Central. Use the workbench when a project needs saved snapshots, candidate versions, or reassessments.

Potential later work includes reusable category checks, structured import of test records, and linking each approved version to observed Alexa and Amazon experiment results. These additions depend on source access and comparable test conditions. [Listing Workbench](https://github.com/kurikiwoods-coder/amazon-listing-workbench)
