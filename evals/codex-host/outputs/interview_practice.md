# Activation decline: interview practice and work sample

This is an offline worked practice case using the four aggregates you supplied.
It is not a claim about your previous employment or an experiment you conducted.
The preparation follows the project's interview-master data-analysis module.

## Your positioning

Your stated background is basic SQL, a course retention dashboard, and no
production experiment experience. No job description or hiring market was supplied.
The useful preparation priorities here are defining metrics, calculating rates
correctly, diagnosing composition changes, explaining uncertainty, and choosing
the next analysis. Your dashboard experience is relevant context; its technical
details, your exact contribution, and any measured impact remain unspecified.

A factual opening you can practice:

“I have basic SQL skills and have worked on a course retention dashboard. I have
not run a production experiment. For this case, I would start by checking the
metric definition, calculate activation rates by channel, and then reconcile them
with the overall rate.”

## Complete spoken answer

Rehearsal target: about two minutes; timing has not been measured.

“Both statements are correct. Overall activation fell because the traffic mix
shifted toward the channel with the lower activation rate. This is an example of
Simpson’s paradox.

“Last week, organic activation was 200 divided by 1,000, or 20%, and paid
activation was 100 divided by 1,000, or 10%. Together, that was 300 activations
from 2,000 users, or 15%.

“This week, organic improved to 110 divided by 500, or 22%, and paid improved
to 180 divided by 1,500, or 12%. But the combined result was 290 activations
from 2,000 users, or 14.5%.

“The key is that paid traffic grew from half of all users to three quarters.
Paid still has the lower activation rate, so it carries more weight in this
week’s overall result.

“To separate the changes, I would hold the channel mix at last week’s 50/50
split. This week’s channel rates would then give an activation rate of 17%.
That is a two-percentage-point improvement at a fixed mix. Moving to this
week’s actual mix lowers that figure by 2.5 percentage points, leaving a net
decline of half a percentage point.

“Before recommending a change, I would verify that both weeks use the same
eligible-user definition, channel attribution, activation event, and follow-up
window. I would then examine why the channel mix changed and compare paid
acquisition costs with downstream retention and value.

“I would report the actual overall rate alongside the channel rates and a
fixed-mix comparison. These figures explain the aggregate decline, but they do
not establish why either channel improved or prove that a product change caused
the improvement.”

## Work sample brief

Task: reconcile the dashboard decline with the channel improvements, write a
decision memo, and reproduce the calculations in SQL.

Inputs: the four rows below. No user-level events, costs, revenue, experiment
assignments, or additional weeks were supplied.

Constraints: work offline; use only supplied data; state assumptions; do not
infer causal effects or invent candidate achievements.

Assume that each denominator represents eligible users in a signup cohort,
channels are mutually exclusive and exhaustive, and activation is measured over
the same complete observation window. The actual definition and window were not
provided. If the counts instead refer to unrelated calendar-week events, the
cohort interpretation must be revisited.

| Week | Channel | Eligible users | Activated users | Activation rate | User share |
|---|---|---:|---:|---:|---:|
| Last | Organic | 1,000 | 200 | 20% | 50% |
| Last | Paid | 1,000 | 100 | 10% | 50% |
| Last | Total | 2,000 | 300 | 15% | 100% |
| This | Organic | 500 | 110 | 22% | 25% |
| This | Paid | 1,500 | 180 | 12% | 75% |
| This | Total | 2,000 | 290 | 14.5% | 100% |

## Reference calculation

Overall rate = sum of (channel share × channel activation rate).

- Last week: 0.50 × 20% + 0.50 × 10% = 15%.
- This week: 0.25 × 22% + 0.75 × 12% = 14.5%.
- This week's rates at last week's mix: 0.50 × 22% + 0.50 × 12% = 17%.
- Rate component: 17% − 15% = +2 percentage points.
- Mix component: 14.5% − 17% = −2.5 percentage points.
- Total change: +2 − 2.5 = −0.5 percentage points.

In symbols, let w0 and w1 be old and new channel shares, and r0 and r1 the
corresponding rates. Sum across channels:

    R1 − R0 = Σ w0(r1 − r0) + Σ (w1 − w0)r1

This decomposition changes rates first, then weights. In general, attribution
between components depends on the chosen path. Here, reversing the order gives
the same components because both channels' rates increased by exactly two
percentage points: old rates at the new mix give 12.5%, followed by a rise to
14.5%.

The overall decline is 0.5 percentage points, or about 3.33% relative to the
previous 15% rate. Activations fell by 10, despite an unchanged total user count.
An unweighted average of 22% and 12% gives 17%, which is a standardized comparison,
not this week's actual rate.

## Runnable SQL

Open `work_sample.sql` in a fresh SQLite database or connection and run the entire
file. It creates only a temporary input table and produces three result sets:
channel metrics, actual overall metrics, and the decomposition.

If the SQLite command-line program is installed, from this folder run:

    sqlite3 -header -column :memory: < work_sample.sql

Expected final row:

| last_week_pct | this_week_pct | fixed_old_mix_pct | old_rates_new_mix_pct | within_channel_component_pp | mix_component_pp | net_change_pp |
|---:|---:|---:|---:|---:|---:|---:|
| 15 | 14.5 | 17 | 12.5 | 2 | -2.5 | -0.5 |

Explain the SQL aloud:

“Each input row is a channel-week aggregate. First, I sum eligible users by week.
Then I join those totals to calculate each channel's share. For the overall rate,
I divide total activations by total eligible users. I use decimal arithmetic to
avoid integer division. Finally, I pair the weeks by channel and calculate the
fixed-mix comparison.”

This query assumes the same two channels exist in both weeks. If a channel appears
or disappears, its missing rate is undefined; do not silently drop it with the
inner join. Reconcile channel coverage and choose an explicit comparison policy.
For a zero-user channel, return an undefined rate, not zero.

## Decision memo

Observed result: total activation decreased from 15% to 14.5%, while organic
increased from 20% to 22% and paid increased from 10% to 12%. Total users remained
at 2,000; total activations decreased from 300 to 290.

Explanation: paid share rose from 50% to 75%. The mix change contributed −2.5
percentage points under the stated decomposition, outweighing the +2-point
within-channel contribution. This is an accounting explanation, not causal
attribution.

Recommendation: do not use this aggregate decline alone to justify a product
rollback or an acquisition budget cut. Validate measurement, investigate the
volume changes, and assess acquisition economics. Report actual activation,
activation counts, channel rates, and the standardized rate together.

Next analyses, in priority order:

1. Reconcile measurement. Confirm stable eligibility, deduplication, event
   instrumentation, time zones, attribution, and complete follow-up windows.
   Recompute both weeks under a consistent definition if any rule changed.
2. Explain volume changes. Organic users fell by 500 and paid users rose by 500.
   Inspect campaign delivery, spend, source attribution, and tracking changes.
   These are hypotheses to check, not established causes.
3. Test whether channel-level gains conceal further mix shifts. Compare campaign,
   device, geography, and new-versus-returning cohorts where relevant. Prefer
   preselected business-relevant segments to indiscriminate slicing.
4. Evaluate the business decision. Obtain paid spend, cost per activated user,
   downstream retention, and contribution value using mature comparable cohorts.
   A lower activation rate alone does not establish lower profitability.

Monitoring: track the actual business outcome and a fixed reference-mix metric.
Choose and document the reference population. Standardization helps comparison
but does not remove confounding inside channels or substitute for an experiment.

## Follow-up answers

**“Why not say the product improved?”**

“The observed rates improved within each channel, but this is a before-and-after
comparison. Audience composition, seasonality, attribution, or measurement could
also have changed. I can describe the improvement, but I cannot attribute it to
the product from these four rows.”

**“Should we reduce paid acquisition?”**

“I would not decide from activation rate alone. I would examine spend, cost per
activated user, downstream retention, and contribution value. Paid acquisition
may still be worthwhile, and moving volume to organic may not be feasible. The
17% fixed-mix figure is a comparison, not a forecast that we can achieve by
reallocating a budget.”

**“Are the channel improvements statistically significant?”**

“These calculations establish the observed differences, not their statistical
reliability or persistence. I would first check whether users are independent,
whether the same users appear in both periods, and whether measurement is stable.
Then I would choose a suitable uncertainty estimate. Even a statistically clear
before-and-after difference would not establish a product effect.”

**“What if this week's users have had less time to activate?”**

“Then the rates are not directly comparable. I would define a common activation
window after signup and compare only cohorts with complete follow-up, or use an
appropriate method for incomplete observation. I would label the current result
as provisional until the measurement is comparable.”

**“How would you query raw event data?”**

“I would start with one row per eligible user, with signup time and acquisition
channel. I would count a user as activated if at least one qualifying event
occurred within the agreed window after signup. I would aggregate events to the
user level before joining, or use an existence check, and retain users with no
activation. I would reconcile user counts before and after the join.”

Checks: repeated activation events must count once; a user with no event must
remain in the denominator; events before signup or after the window must not
qualify; ineligible users must be excluded; immature cohorts must not silently
be treated as failures. The supplied aggregates cannot validate these conditions.

**“Have you run an A/B test?”**

“I have not run a production A/B test. My relevant project experience is a course
retention dashboard, and I have basic SQL skills. As a proposed approach, I would
define the hypothesis, eligible population, and primary metric; randomly assign
eligible users to control and treatment; and use a common observation window.
I would predefine the sample-size plan and stopping rule, monitor guardrails, and
check assignment and tracking quality. I would compare outcomes according to
assignment and report the effect with uncertainty. I would not use this
before-and-after case as evidence that I have run an experiment.”

For this case, a hypothetical onboarding experiment could use activation within
a pre-agreed window as its primary outcome, with retention and support burden
as guardrails. Randomize within acquisition channels if channel balance is
important. Specify the minimum meaningful effect and sample-size calculation
before launching; no numeric sample size is justified by the case alone.
Do not repeatedly stop at a favorable conventional significance result.

**“How does your retention dashboard relate to this?”**

“I have worked on a course retention dashboard. For this case, I would apply
cohort-based reasoning: define who enters the denominator, allow a comparable
follow-up period, and inspect segment composition before interpreting an
aggregate trend. I would describe the specific dashboard checks I actually
performed separately from checks I am proposing here.”

Before expanding this into a project story, add only facts you can support:
your exact contribution, the dashboard's retention definition, one real SQL or
data-quality issue, and what the dashboard was used for. No impact figure was
supplied, so this packet does not invent one.

## Alternative and changed conditions

Alternative presentation: show a two-panel report with actual outcomes on one
side and rates standardized to a fixed reference population on the other.
Actual outcomes answer what happened; standardization answers how rates compare
under the specified weights. The reference mix is a reporting choice, and using
last week's mix is convenient for this case rather than universally preferable.

Changed condition: channel attribution rules changed halfway through this week.

Reference response: “I would suspend the claim that like-for-like channel
performance improved. I would reconstruct both periods under the same attribution
rules if raw data allows it. If only channel labels changed, overall counts may
remain valid, but the channel decomposition is not a reliable comparison. If
deduplication or eligibility also changed, I would revalidate the overall rate.”

## Practice and evaluation

Suggested 20-minute practice:

1. Explain the result aloud without looking at the script.
2. Recalculate every rate and weight, then run the SQL in a fresh connection.
3. Explain the −0.5-point change using +2 points and −2.5 points.
4. Answer the paid-budget and experiment questions in your own words.
5. Revisit the conclusion after the attribution-change scenario.

Self-check anchors:

- Arithmetic: totals are 300/2,000 and 290/2,000; rates are correctly weighted.
- Diagnosis: explain the shift toward paid traffic; naming the paradox alone
  is insufficient.
- Measurement: identify denominator, attribution, and observation-window risks.
- Judgment: distinguish descriptive decomposition, uncertainty, and causality.
- Action: name the next evidence needed for a business decision.
- Communication: use “percentage points” correctly and make no unsupported
  claims about your experience.

These are practice criteria, not an employer's official rubric or a hiring
prediction. The reference solution is delivered; you have not yet submitted a
practice answer, so your execution and spoken performance have not been assessed.

Material unresolved facts: the activation definition, eligibility rules,
observation window, attribution stability, and acquisition economics. For further
personal tailoring, the job description and your precise dashboard contribution
would help. Next useful action: give a two-minute explanation from memory and
then defend your recommendation if the channel labels changed.
