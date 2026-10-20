# Product management

Goal: choose a user/business problem, commit limited delivery resources, and learn whether a shipped solution worked. Growth, platform and monetization roles share this process but differ in users, constraints and outcomes.

| Capability | Method | Output / alternatives / failure |
|---|---|---|
| Problem discovery | Identify user, job, friction and evidence; separate requests from needs; combine observations with behavioral data | Problem brief and unresolved assumptions; interview or instrument depending on uncertainty; vocal users can bias priorities |
| Prioritization | Compare options by expected outcome, evidence strength, reach, cost, dependencies and reversibility | Explicit choice and rejected option; avoid pretending rough scores are precise forecasts |
| Solution design | Map journey, happy path, exception states, permissions and dependencies; define acceptance criteria | Scoped solution with non-goals; manual service/process may beat a new feature |
| Delivery | Define owner, milestones, integration risks, rollout conditions and escalation | Delivery plan; trade scope for learning rather than promise all requirements |
| Validation | Specify outcome and guardrails, credible comparison and measurement period before rollout | Launch/iterate/stop decision; adoption is not automatically retention or revenue |
| Stakeholder judgment | Explain disagreement through goals, evidence and constraints; record who decides | Decision note; agreement without resolving ownership can delay delivery |

Levels: junior frames a scoped problem and tests assumptions; independent owns choices through rollout and evaluation; senior connects portfolio, strategy, platform costs and organizational decisions.

Question seeds: Which need did you reject? What changed your priority? How did engineering constraints change the solution? What would falsify the claimed result?
For each answer request an actual decision, alternatives and evidence; do not invent personal authority.

Use [product decision](examples/product_decision.md), [data methods](role_data.md), and [answer layers](competency_answer_template.md). For a platform role consider internal users, reliability and adoption cost; for monetization include customer value, willingness to pay and retention guardrails.

## Interview drills (hypothetical methods, not personal history)

**A feature is popular with sales but unsupported by user evidence. What do you do?**
"I would separate the commercial commitment from the proposed solution. I would identify which customer outcome matters, how many relevant customers share it and what evidence exists beyond the loudest request. Then I would compare a smaller product change, a manual service and doing nothing against opportunity cost and delivery risk. I would commit to a reversible test if it can resolve the decisive uncertainty, with an explicit decision owner and a date to revisit the choice."
Teaching: popularity of the request is a signal about stakeholder needs, not proof of user value. Ask whether the commitment is contractual, which changes constraints.
Follow-up: "The largest customer threatens to leave." Make the commercial exposure explicit without treating one customer's desired feature as the entire strategy.
Junior: asks about the need; independent: makes a scoped choice; senior: handles portfolio and customer concentration.

**You shipped on time but the outcome did not improve.**
"I would verify that users received the change and that measurement is valid, then inspect the mechanism between adoption and the outcome. If users do not adopt, investigate discoverability and relevance; if they adopt without benefit, examine whether the solution addressed the wrong friction. I would compare iteration with stopping, using evidence and opportunity cost rather than defend the sunk delivery effort."
Failure to avoid: declaring success from delivery or clicks. Drill: name one observation that would justify stopping instead of iterating.

**How do you write acceptance criteria?**
"I would specify who should be able to complete which task under what conditions, including failure and recovery states. I would distinguish release correctness from outcome evaluation: a feature can pass functional acceptance and still fail to create value. I would review the criteria with engineering and support so ownership, dependencies and edge cases are clear."
Follow-up: permission changes midway through an operation. Explain the state transition and recovery, not only the happy-path screen.
