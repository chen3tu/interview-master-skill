# Product decision: collaborative onboarding
All organizations, users and numbers below are synthetic. This is a reference work sample, not candidate history.

## Task and inputs
A B2B workspace product has 1,000 new admin signups per month. 600 create a workspace, 240 invite a teammate, and 120 complete a shared task in seven days. Support interviews suggest confusion about invitation permissions, but the sample includes only 8 users who contacted support. You have two engineers for two weeks. Sales asks for an AI onboarding assistant; support asks for clearer permissions.

Deliver a one-page decision, a scoped flow, acceptance criteria and validation plan. Clarify whether shared-task completion predicts durable value; treat it as a provisional activation measure.

## Reference approach
The largest observed stage loss is not automatically the best opportunity: compare reach, recoverable friction, implementation effort and user intent. First inspect event definitions and invitation errors, then interview successful and unsuccessful administrators, not only support callers. Determine whether an invite is needed for each customer type.

Choose a reversible permission/preview improvement as an initial hypothesis: show who can invite, what an invite grants, and a preview of the teammate experience. Include pending, expired, already-member and permission-denied states. Non-goals: redesign all onboarding or introduce an autonomous assistant without evidence it solves the problem.

Acceptance: an eligible admin can invite and see delivery/pending state; an unauthorized user receives a clear route to request permission; duplicate actions do not send repeated invitations; failed sends are recoverable; keyboard users can complete the flow. Engineering confirms what can fit the two-week scope.

Primary evaluation: seven-day shared-task completion per eligible new workspace, not clicks on the redesigned button. Guardrails: support contacts, unwanted invitations and permission incidents. Agree the comparison and observation window before launch. If randomization by workspace is feasible, use it to avoid mixing collaborators across variants. Sample size and duration require baseline variance and meaningful effect, not an invented "two weeks is enough" rule.

## Alternative and decision
A manual onboarding session could reveal problems faster for a small segment; it is useful for discovery but has service cost. A guided checklist may beat permission work if investigation shows users do not know the next task. An AI assistant adds complexity and error modes; reconsider it only if actual tasks need language understanding and simpler approaches fail.

## Spoken demonstration
"I would first validate what activation means and where users get blocked. These funnel counts suggest invitation deserves investigation, but they do not prove the cause. With two engineers, I would test a small permission-and-preview change, define recoverable error states, and measure completed collaboration rather than invitation clicks. I would compare outcomes by workspace and monitor support load and permission problems. If the main barrier turned out to be unclear next steps, I would change the solution rather than defend the initial idea."

This is a hypothetical decision answer. Do not present it as a shipped personal project.

## Pressure variation
Invitation rate rises, but shared-task completion stays flat and support contacts rise.
Response: do not declare success. Inspect whether low-intent users were pushed into inviting, separate invitation failures from task friction, check instrumentation and compare cohorts. Pause expansion if permission/support guardrails are breached. Diagnose before adding more prompts.

## Evaluation and next drill
Junior: states a user problem, clean denominator and testable small scope.
Independent: connects states, delivery and comparison to a decision.
Senior: weighs strategy, service capacity, segment differences and reversibility.
Weak: assumes the requested AI feature is the solution or claims causal improvement from the raw funnel.
Next drill: write the rejected alternative and the observation that would make you choose it.
