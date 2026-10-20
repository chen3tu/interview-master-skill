# Data analysis and experimentation

Goal: turn an ambiguous business question into a reliable measurement and a decision. Distinguish analysis from ML research or data-platform engineering.

| Capability | Principle and procedure | Output / tradeoff / failure |
|---|---|---|
| Metric design | Define decision, event, eligible population, numerator, denominator, time window, unit and exclusions before calculating | Metric contract; choose actionable vs easily available proxies; averages can hide cohorts |
| Data quality | Check grain, uniqueness, joins, missingness, time zones and late arrivals; reconcile totals with a source | Quality report; quarantine uncertain rows rather than hide them; duplicated joins inflate conversion |
| SQL reasoning | State table grain, keys and time range; filter eligible population, deduplicate events, aggregate at entity level, then join | Query with edge cases; explain null/zero and repeat users; test counts before/after joins |
| Diagnosis | Confirm anomaly, segment by relevant changes, rank plausible causes and identify distinguishing evidence | Hypothesis tree and next query; avoid endless slicing or asserting cause from correlation |
| Experiment | Define estimand, randomization unit, exposure, primary outcome, guardrails and stopping rule before looking at results | Analysis plan; interference, selection and repeated peeking can invalidate interpretation |
| Action | Translate findings to a decision, uncertainty, expected mechanism and monitoring/rollback | Decision memo; prefer an uncertainty-reducing pilot over unsupported certainty |

Levels: junior defines grain and checks calculations; independent chooses comparison, catches confounders and makes a defensible recommendation; senior handles measurement systems, conflicting incentives and decisions under uncertainty.

Interview: "Conversion dropped—what would you examine first?" Start with instrumentation and denominator stability, then mix/behavior hypotheses. A strong answer states which observation would distinguish causes; a weak answer lists dashboards.

Do not demand the candidate remember an exact p-value. Explain assumptions and distinguish statistical uncertainty from business relevance. Use [diagnosis sample](examples/data_diagnosis.md); [module standard](competency_module_standard.md) defines the teaching contract.

## Interview drills

**A join doubles the dashboard's users.**
"I would state each table's grain and inspect key uniqueness before changing the query. If one row per user is being joined to several events, I would aggregate or deduplicate events according to the metric contract before joining, while retaining eligible users with no event. I would reconcile entity counts before and after the join and test legitimate repeated events separately from ingestion duplicates."
Teaching: COUNT(DISTINCT user_id) can hide a join problem without fixing summed revenue. Choose aggregation at the actual measure's grain.
Junior: catches multiplicity; independent: preserves metric semantics; senior: fixes the upstream contract and tests.

**An experiment looks positive after several daily checks.**
"I would return to the planned analysis and stopping rule rather than select the favorable day. I would inspect assignment, exposure, missingness and guardrails, then interpret uncertainty using a method appropriate to the design. If the decision requires repeated monitoring, I would plan for it rather than treating every repeated conventional test as independent confirmation."
Follow-up: a severe guardrail failure can justify stopping even when the primary endpoint is not conclusive. Do not claim a fixed sample count guarantees significance.

**A stakeholder asks for a yes/no answer with incomplete data.**
"I would separate what the data supports from the decisive uncertainty and state the cost of each mistaken action. If the action is reversible, I might recommend a small pilot with monitoring; if error is costly, I would prioritize the missing validation. I would say which new evidence would change the recommendation and when the decision will be reviewed."
Weak answer: either fabricating confidence or refusing all action until perfect data exists.
