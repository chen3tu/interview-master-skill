# AI product management

| Capability | Procedure | Output / tradeoff / failure |
|---|---|---|
| Task choice | Identify user decision, error cost, task frequency and non-AI baseline | Task brief; rules/search/human service may be sufficient |
| Workflow | Define input, model role, user control, escalation and recovery | Journey and responsibility map; autonomy without controllable actions is a product risk |
| Evaluation | Build representative task sets including failures; specify usefulness, correctness and harm-sensitive criteria | Evaluation plan; impressive demos can hide hard cases |
| Economics | Compare end-to-end success cost, latency and service burden against baseline | Unit model; token cost alone excludes rework |
| Launch | Set quality/guardrail gates, small rollout, feedback collection and rollback | Launch decision; offline evaluation does not prove online benefit |
| Adoption | Clarify trust, user instruction, workflow fit and how feedback becomes action | Adoption plan; usage is not automatically user value |

Levels: junior scopes a useful task and recognizes limitations; independent defines evaluation and rollout tradeoffs; senior governs a portfolio and organizational impact.

Do not require model-training expertise unless the JD does. A strong answer explains when not to use AI and what a user can do when it fails.

Use [AI workflow](examples/ai_workflow.md), [data methods](role_data.md) and, only for implementation detail, [AI application engineering](role_ai_application.md).

## Interview drills

**The model demo is impressive; why not launch?**
"A demo shows that the system can succeed on selected tasks, not how often it succeeds for the target population. I would define representative success and failure cases, compare with the non-AI baseline, and measure reviewer effort and serious errors. I would choose a bounded rollout with escalation and explicit stop conditions instead of treating the demo as a quality estimate."
Follow-up: sparse real examples. Start with carefully labelled synthetic tests plus permitted realistic cases, then investigate distribution gaps; do not claim synthetic coverage equals production validation.

**Accuracy improves but users abandon the workflow.**
"I would inspect end-to-end usefulness: whether answers arrive in time, are actionable, fit the user's task and allow correction. A technically correct response can still create work or undermine trust. I would compare task completion, latency and rework across segments before deciding whether to improve the model, simplify the interface or remove the AI step."
Levels: junior distinguishes metrics; independent runs a diagnostic comparison; senior resolves quality/economics/organization tradeoffs.

**How do you decide whether human review is necessary?**
"I would start from the consequences and reversibility of an incorrect action, the evidence about failure modes and the quality of escalation. I would keep costly mutations gated until authorization, detection and recovery are demonstrated. Human review is itself a workflow that needs capacity and usable evidence; merely adding an approval button does not establish effective oversight."
Pressure: review cost erases savings. Narrow the automated task rather than quietly lowering the quality bar.
