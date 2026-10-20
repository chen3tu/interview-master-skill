I’m using the Interview Master skill to interpret the role and separate its requirements from what we know about your background.

**This looks like a product or growth analytics role focused on turning user behavior into reliable decisions. Your personal fit is not yet assessable because you have not supplied any background.** I can analyze what the job requires now, but I would not label you a strong or weak match from the JD alone.

| Responsibility | What it really requires | What convincing evidence would look like |
|---|---|---|
| Define metrics | Translate a business question into a precise, reproducible measure | An example specifying the event, population, numerator, denominator, time window, exclusions, and edge cases |
| Investigate conversion | Distinguish data problems from behavioral changes, locate the affected part of the funnel, and test explanations | A funnel investigation that checks data quality and segment mix, forms hypotheses, and leads to a justified action |
| Design experiments | Translate a decision into a testable hypothesis and an interpretable comparison | A design covering assignment unit, treatment and control, success metric, guardrails, sample-size reasoning, duration, and analysis limitations |

The common thread is analytical judgment. The interviewer will likely want to see that you can explain what a number means before explaining why it changed, and that you can distinguish correlation from causation.

The JD does not state seniority, education requirements, years of experience, industry, or tooling. SQL and statistical reasoning would be sensible preparation areas, but I would not present a particular language, platform, or credential as a stated hiring requirement. The short description also does not establish whether the role owns instrumentation, experiment execution, or only analysis.

Likely interview questions, predicted from these responsibilities:

1. **“Define signup-to-purchase conversion.”** A strong answer clarifies who is eligible, what counts as signup and purchase, the conversion window, deduplication, refunds if relevant, and how late-arriving data is treated.
2. **“Conversion fell. How would you investigate?”** Start by checking definitions and tracking, then compare relevant periods and decompose the funnel and user segments. Form hypotheses before recommending a solution.
3. **“Design a test for a new onboarding flow.”** State the hypothesis, assignment unit, comparison, activation outcome, retention or other guardrails, and the conditions under which you would make a rollout decision.
4. **“The treatment group has a higher conversion rate. Should we launch?”** Discuss uncertainty, validity of randomization and exposure, practical effect size, guardrails, and whether the test ran long enough to answer the decision.

A compact preparation exercise would be: define conversion for a hypothetical product, sketch the query logic to calculate it without duplicate users, explain how you would investigate a fall, and then design an experiment for one proposed fix. This checks all three responsibilities without assuming you have already performed them professionally.

To assess your fit, send either a résumé or a short description of:

- Your current role or studies and experience level.
- One analysis, coursework, or project example, including your personal contribution.
- Your experience with SQL, metric definitions, statistics, and experiments.

A junior candidate can support a fit assessment with rigorous coursework or personal projects. A more senior candidate would usually need deeper evidence of independent analytical decisions and stakeholder impact. Since the level is unspecified, neither expectation should be treated as the confirmed hiring bar yet.

---
Evaluation limitation: Generated in the same shared evaluator and baseline batch context as the earlier baseline cases, not a blinded isolated model run. Only the supplied v3 baseline Skill, its relevant references, and the raw scenario inputs were used; no browsing or external actions were performed.
