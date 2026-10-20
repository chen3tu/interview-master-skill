# Data diagnosis: mix shift
Synthetic observations for a work sample.

## Input
Week A: organic 1,000 eligible users / 200 activations; paid 1,000 / 100.
Week B: organic 500 / 110; paid 1,500 / 180.
The dashboard says total activation fell from 15% to 14.5%. Marketing says both channels improved.
Deliver a reconciliation, next queries and a decision memo.

## Calculation
A: 300 / 2,000 = 15%.
B: 290 / 2,000 = 14.5%.
Organic improves from 20% to 22%; paid from 10% to 12%.
At the old 50/50 mix, B's rates would yield 17%. At B's 25/75 mix, A's rates would yield 12.5%.
Both observations can be true: channel mix moved toward the lower-activation channel. This decomposition describes the data; it does not establish the cause of channel-level improvements.

## Data contract and query
Assume users has one row per eligible user with id, cohort_week and acquisition_channel. events can contain repeated activation events. Count unique eligible users, not joined rows:

~~~sql
WITH activated AS (
  SELECT DISTINCT user_id FROM events WHERE event_type = 'activation'
)
SELECT u.cohort_week, u.acquisition_channel,
       COUNT(*) AS eligible,
       SUM(CASE WHEN a.user_id IS NOT NULL THEN 1 ELSE 0 END) AS activated
FROM users u
LEFT JOIN activated a ON a.user_id = u.id
WHERE u.eligible = 1
GROUP BY u.cohort_week, u.acquisition_channel;
~~~

This simplified query assumes the input events have already been restricted to the agreed activation window for each user. In production, join the event timestamp to each user's signup time and window; do not use an unrestricted lifetime activation event. Check uniqueness, late events, timezone and changes in channel attribution. Test repeated activation events, no events and users outside eligibility.

## Reference recommendation
Do not rollback the product simply because the aggregate fell. First verify the event/eligibility contract and channel attribution, then report within-channel rates and the mix decomposition. Compare paid acquisition's downstream value and cost; more paid volume may be worthwhile even with lower activation, or may not be.

Alternative: standardize rates to a fixed mix for product monitoring while keeping actual-volume metrics for business performance. Neither alone answers all business questions. For a product-effect claim use a credible experimental or quasi-experimental design with explicit assumptions.

## Spoken demonstration
"I would reconcile the aggregation before looking for a broken feature. Both channels improved, but the paid share increased and paid users have a lower activation rate. I would show the weighted-rate calculation, check consistent cohorts and instrumentation, then examine acquisition quality and economics. That explains the dashboard discrepancy; it does not prove the product caused either channel's improvement."

## Changed condition and evaluation
Channel labels were revised midway through week B: recompute a stable definition or mark comparisons unreliable. Do not keep the neat explanation despite contradictory measurement evidence.
Junior: correct denominators and arithmetic.
Independent: catches mix and join/window issues, proposes discriminating checks.
Senior: chooses complementary metrics and makes a decision under measurement uncertainty.
Next drill: explain the same result to a nontechnical manager in the requested language without hiding the caveat.
