I’m using the Interview Master skill’s attribution and metric-review guidance. I’ll start with a worked example, then turn it into an answer you can use.

**Worked example: conversion rises without either segment improving**

This is a hypothetical teaching example. None of these numbers are Lee’s project results.

Suppose an onboarding checklist and engineering changes launch between two periods. Each period contains 1,000 eligible new accounts, and conversion means completing the same meaningful activation event within seven days.

| Acquisition segment | Before: eligible / activated | Before rate | After: eligible / activated | After rate |
|---|---:|---:|---:|---:|
| High-intent channel | 200 / 40 | 20% | 400 / 80 | 20% |
| Lower-intent channel | 800 / 40 | 5% | 600 / 30 | 5% |
| Total | 1,000 / 80 | 8% | 1,000 / 110 | 11% |

The aggregate rate increased by **3 percentage points**, or **37.5% relative**: `(11% − 8%) / 8%`. However, neither channel’s conversion rate changed. More users came from the high-intent channel.

If we apply the old channel weights to the new segment rates, we get `20% × 20% + 80% × 5% = 8%`. In this constructed example, the aggregate increase is explained by the change in channel mix. It is not evidence that the checklist caused the increase.

A weak answer would be: “Conversion went up after the checklist, so the checklist worked.”

A stronger answer is:

> “Overall conversion rose from 8% to 11%, but the rate stayed unchanged within each of the two acquisition segments. The aggregate increase is explained by more high-intent users entering the funnel. I would not attribute it to the checklist on this evidence. I would test the checklist against a credible comparison while keeping the engineering experience consistent, then evaluate retention as well as activation.”

The decision is to withhold the causal claim and investigate the intervention’s effect. This does not prove the checklist is useless: the example does not identify every possible effect or mechanism. It shows why an overall before/after increase is insufficient.

**The method to reuse**

1. **Define what changed.** Specify the activation event, eligible population, denominator, deduplication rule, and observation window. Check that both periods use the same definitions and that every account has had enough time to convert.
2. **Separate delivery from outcome.** “We coordinated reviews” establishes an activity. “Conversion rose” establishes an observed outcome only if the calculation is reliable. “Our reviews caused conversion to rise” is a further claim that needs a credible comparison.
3. **Ask what else changed.** Channel mix, user characteristics, tracking, support activity, seasonality, and engineering releases could affect the result. Here, engineering changes are explicitly part of the supplied history.
4. **Build a counterfactual.** Where feasible, randomly assign eligible accounts before exposure to checklist versus existing onboarding while keeping the platform version the same. That estimates the incremental checklist effect under that platform experience. It does not separately identify the platform change’s effect. If both components need to be estimated, a suitable multi-group design could be considered if feasible.
5. **Check the downstream value.** Define retention using a stable eligible cohort and a meaningful return event, allow equal follow-up time, and examine relevant guardrails. An activation lift alone is not enough for this JD.
6. **State the limit of the evidence.** Without randomization, a credible quasi-experimental comparison may help, but its assumptions must be defended. Simply adjusting for channel mix does not remove all possible confounding.

**Your usable project answer, approximately 75 seconds**

> “I coordinated an onboarding checklist and weekly issue reviews with support, while engineering delivered the platform changes. My résumé lists a 20% conversion improvement, but I cannot currently verify the denominator, comparison period, or whether that was a relative change, so I should not present that figure as a confirmed result.
>
> “Even if I recovered and verified the increase, that alone would not show that my work caused it. I would need to check cohort comparability, tracking, acquisition mix, and the concurrent engineering changes. Where feasible, I would compare eligible accounts exposed to the checklist with comparable accounts on the same platform experience, using a sound assignment and measurement process.
>
> “I would also examine retention after a consistent follow-up window. What I can substantiate now is my coordination contribution; the size and cause of any conversion improvement remain unverified. The practice I would improve is agreeing on the measurement and comparison plan before rollout.”

Likely follow-ups:

- **“Are you saying your work had no impact?”** “No. I am saying the evidence available here does not establish its impact. Lack of attribution is different from proof of no effect.”
- **“Why not just use the 20% from your résumé?”** “Because I cannot explain or verify its calculation. Repeating it would make an unsupported claim sound established.”
- **“How would you apply this to our product?”** “I would first agree on what activation and retention mean for your user journey and usage cycle, then select the comparison design. I would not assume the same event or time window works for every product.”

Your main risk is moving directly from activity to causality. Practice the sequence: contribution → verified observation, if any → comparison → bounded conclusion. The worked example provides the pattern; you do not need to invent a past experiment to demonstrate that you understand it.

---
Evaluation limitation: Generated in the same shared evaluator and baseline batch context as the earlier baseline cases, not a blinded isolated model run. Only the supplied v3 baseline Skill, its relevant references, and the raw scenario inputs were used; no browsing or external actions were performed.
