# Operations and growth

Product decisions have moved to [product management](role_product_manager.md). This module concerns execution systems, customer segments, channels and business operations.

| Capability | Method | Output / tradeoff / failure |
|---|---|---|
| Segmentation | Define lifecycle stage and needs using available behavior; validate that segments lead to different actions | Segment/action matrix; fewer actionable groups beat many arbitrary labels |
| Channel strategy | Match audience, message, touchpoint, eligibility, consent and cost; establish baseline | Channel plan; owned vs paid depends on reach and control, not fashion |
| Campaign/content execution | State promise, asset, owner, schedule, QA, service capacity and escalation | Operating checklist; an attractive campaign can fail when fulfillment cannot cope |
| Funnel and retention | Define eligible cohort and stage transitions; trace quality after conversion | Funnel/cohort report; incentives may increase low-quality activation |
| Attribution and economics | Separate gross outcome from incremental outcome; identify comparison, costs and cannibalization | Unit-economics view with uncertainty; platform last-click credit is not causality |
| Operational mechanisms | Use recurring issue review, handoff, playbook, exception tracking and learning | Sustainable routine; automation without ownership replicates errors faster |

Levels: junior executes and reports accurately; independent chooses segment/channel and adjusts from evidence; senior changes operating mechanisms and balances cross-channel/long-term economics.

Typical question: "The campaign lifted conversion; how do you know it was worth repeating?" Explain eligible population, comparison, downstream quality, incremental cost and capacity. If the historical candidate lacks these data, say so and show how they would evaluate a next campaign.

Use [growth sample](examples/operations_growth.md) and [data methods](role_data.md). For content, community, customer operations or commercial operations adapt actual work artifacts; do not assume every operator owns experimentation or engineering.

## Interview drills

**A high-converting channel is consuming support capacity.**
"I would compare incremental customer value with acquisition and service cost, then inspect which segments generate avoidable contacts. I would test whether clearer expectations or a better onboarding step reduces the burden before buying more traffic. If service capacity is the binding constraint, I would limit volume and prioritize the segment with the strongest supported economics rather than maximize conversions alone."
Teaching: do not divide all company support cost by one campaign without a defensible allocation. Track capacity and incremental workload separately.
Follow-up: retention is unknown. Recommend a limited pilot and downstream observation rather than an invented lifetime value.
Levels: junior reports costs accurately; independent changes targeting/execution; senior handles cross-channel constraints and durable service mechanisms.

**An activity has a fixed launch date and several dependencies.**
"I would work backward from the minimum user promise, identify critical assets and owners, and define a readiness check covering message, eligibility, landing flow, fulfillment and measurement. I would prepare an explicit reduced-scope fallback for a late dependency. After launch I would track failures and escalation ownership, then record what should change in the next run."
Weak answer: a timeline with no acceptance criteria or contingency. Variation: the landing page is delayed while messages are scheduled; halt or redirect the campaign coherently, do not send users into a broken journey.

**How would you improve retention without blanket discounts?**
"I would define which users are expected to return and when, then distinguish missing value, usability friction and lack of awareness. I would test a segment-specific intervention linked to the cause—such as timely guidance or service recovery—against a credible comparison. Discounts are one option, but I would assess their incremental cost and whether behavior persists when the incentive ends."
Follow-up: compare a cohort with equal observation time; a newer cohort cannot yet establish long-term retention.
