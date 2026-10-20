# AI support workflow: product and engineering
Synthetic scenario. No candidate experience or real model benchmark is implied.

## Task
A support team receives repetitive product questions and account-specific change requests. A maintained help centre exists, but some articles are stale. Incorrect account changes are costly. The team wants "an autonomous support agent".
Output differs by role: product candidates deliver task choice and rollout/evaluation; engineers deliver a bounded workflow and recovery design.

## Product reference
Separate information lookup from account mutations. Start with grounded draft answers for human review on a bounded set of common questions. Compare with improved search/templates; AI is worthwhile only if it improves useful resolution enough to justify errors, review cost and latency.

Create an evaluation set from appropriately permitted, de-identified examples: straightforward lookup, ambiguous requests, conflicting/stale sources, unsupported claims and action requests. Define a valid answer as correct for the current source, relevant, appropriately bounded and useful to the user. A citation alone does not prove support.

Measure task success, serious errors, unsupported answers, escalation and reviewer effort. Track cost per successfully resolved case, including rework, not only tokens. Set rollout gates with stakeholders based on actual risk tolerance and baseline results. A small offline set cannot establish safety for all users.

Expose sources and an easy escalation path. Begin with human approval for account changes; removing review requires separate evidence and an authorization design.

## Engineering reference
A deterministic first version: authenticate and authorize context → classify lookup vs action/unsupported → retrieve permitted current material → compose an answer with evidence → check support/constraints → return or escalate.
Treat retrieved text as data, not instructions to invoke tools or reveal secrets. Document freshness and access constraints. If retrieval fails, do not fabricate a confident answer.

For actions, require a valid tool contract, explicit authorization, idempotency key and audit trail. Handle timeout with unknown outcome by checking operation status before retrying a mutation. Store bounded task state; don't rely on conversation prose as the sole transaction record.

Trace retrieval quality, answer support and tool outcomes separately. Keep evaluation cases stable while adding newly found failure cases. Compare workflow vs more dynamic agent control only if branching needs cannot be handled simply and the recovery plan remains understandable.

## Alternatives
Search-only: lower autonomy, may be enough for clear questions.
Human-drafted templates: cheaper but less flexible.
Agentic tool selection: may address variable multi-step tasks, with higher evaluation and recovery demands.
Choose based on observed task needs, not the popularity of an architecture.

## Spoken answers
Product: "I would not start by automating all support. I would separate informational tasks from costly account changes, compare an AI draft assistant with better search, and evaluate useful resolution, serious errors and reviewer effort. I would roll out a bounded task set with escalation before considering more autonomy."
Engineering: "I would make the source and authorization boundaries explicit, then build a traceable workflow. Retrieval failures should escalate, and mutations need idempotent execution plus status recovery. I would evaluate retrieval, answer grounding and action correctness separately so a good average score cannot hide a dangerous failure."

## Pressure
The offline average improves but the account-action subset gets worse. Keep mutations gated, investigate that subset and do not use the aggregate to authorize rollout.
Junior: distinguishes tasks and failure types.
Independent: provides an executable evaluation/recovery design.
Senior: balances service economics, governance, change management and operational responsibility.
AI-product candidates need not write model kernels; AI-engineering candidates should explain concrete control/state boundaries.
