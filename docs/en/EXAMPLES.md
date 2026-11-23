# Examples

[Project home](../../README.md) · [简体中文](../zh-CN/EXAMPLES.md) · [Claude setup](CLAUDE-USAGE.md)

## Walkthrough with supplied copy

This exercise uses a fictional nutrition scale and a synthetic manual excerpt. Run it in any supported assistant with the skill loaded or with `SKILL.md` attached. It uses only the supplied materials, so public product page access is optional.

### Copy this prompt

~~~text
Use the Amazon Listing Rewrite Skill. Give me the report in English.

Marketplace: Amazon US
Product: DemoCo Nutrition Kitchen Scale N1 (fictional)
Task: Audit the supplied title and Bullet 1, then rewrite only those two fields.
Title limit for this exercise: 75 characters including spaces

Title: DemoCo Smart Nutrition Kitchen Scale for Every Meal, Meal Prep and Daily Food Tracking with Calories and Protein
Bullet 1: Track meals with live calories and protein on the scale.

Verified facts from the fictional N1 manual:
1. Save foods to the scale in the app before using this feature.
2. While weighing, select a saved food on the scale.
3. With the app closed, the scale's screen can display calories and protein for that saved food.
4. Bluetooth-off and internet-off behavior have not been verified.

Priority buyer question: Can I see calories and protein on the scale with the app closed, and how do I set that up?

Score the supplied copy, show the priority issues and source quotes, check the rewritten field lengths, and reassess the same buyer question.
~~~

### Example response

**The first fix is to explain the setup and weighing steps in Bullet 1.** The current bullet names the nutrients but leaves the app and saved-food conditions unclear. The title also exceeds the exercise limit by 37 characters.

| Priority | Field and evidence | Proposed change |
| --- | --- | --- |
| P0 | Title, 112 characters against the supplied 75-character limit | Remove generic meal and tracking phrases. Keep the brand, model, product type, and what appears on the scale. |
| P1 | Bullet 1, “Track meals with live calories and protein on the scale.” | Add the initial app setup, the saved-food selection step, and the conditions for reading the screen with the app closed. |

**Candidate title**

~~~text
DemoCo Nutrition Kitchen Scale N1 with On-Scale Calories and Protein
~~~

**Candidate Bullet 1**

~~~text
Save foods to the scale in the app first. Then select a saved food on the scale to view calories and protein on its screen as you weigh with the app closed.
~~~

| Field | Before → after | Limit and result |
| --- | --- | --- |
| Title | 112 → 68 characters | At most 75 for this exercise. The candidate passes. |
| Bullet 1 | 56 → 156 characters | The category limit was not supplied. Check the rule before publishing. |
| A+, Item Highlights, and other fields | Unscored | This exercise supplies the title and one bullet. |

The following copy scores illustrate the same four checks before and after. Each check is out of 25. The overall score is the mean of the two assessed excerpts, rounded to one decimal place here.

| Field | Direct answer | Specificity | Facts and limits | Clarity | Total |
| --- | --- | --- | --- | --- | --- |
| Title before → after | 15 → 20 | 17 → 19 | 19 → 22 | 10 → 24 | 61 → 85 |
| Bullet 1 before → after | 12 → 25 | 10 → 24 | 14 → 25 | 20 → 24 | 56 → 98 |
| **Overall** | | | | | **58.5 → 91.5** |

**Reassess the buyer question.** The original copy partly answers it by naming calories and protein. The candidate answers it with the three conditions from the N1 manual. Save foods in the app first, select a saved food on the scale, then read the screen with the app closed. Bluetooth and internet behavior remain verification items. The scores describe this copy review.

## Start from just an ASIN

~~~text
Look up B0F1N26FT3 on Amazon US. Start with an identity card and tell me which listing fields you could verify. Then run a listing audit and show the highest-priority correction. Give me the report in English.
~~~

Expect a marketplace and variant check, source links, retrieval dates, and a list of visible fields. If live access is restricted, the assistant can use a matching archived snapshot or ask you for the text. Use the sources retrieved in that run to judge the page's current content.

## Compare competitor features

~~~text
Use the Amazon Listing Rewrite Skill to compare this ASIN with up to three same-marketplace alternatives. I care about first-time setup, using the product with the app closed, and what appears on the screen. Cite the relevant listing text and write a reusable buyer question for each feature. Score how clearly each page answers it.
~~~

Expect the physical feature and page answer to be reported for each product. For example, a listing can earn 2 out of 2 by clearly explaining that its nutrition data is available only in the app. An unavailable field gets N/A. Model-generated questions are labeled as suggested test prompts. Attach real Alexa records if you want an assessment of observed answers.
