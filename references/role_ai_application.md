# AI application engineering

| Capability | Procedure | Output / tradeoff / failure |
|---|---|---|
| Architecture | Compare deterministic workflow with agentic control; bound allowed actions and stopping conditions | Request/control trace; more autonomy is not inherently better |
| Retrieval/context | Define source freshness, permissions, retrieval relevance and evidence presentation | Context/evidence contract; retrieved text may be stale or untrusted |
| Tools/state | Validate inputs, authorize actions, handle retries, maintain task state and idempotency | Tool/state design; a retry can repeat an external mutation |
| Evaluation | Separate retrieval, generation, tool correctness and end-to-end task success; keep a stable test set | Failure taxonomy; one aggregate score hides where the system breaks |
| Operations | Budget latency/cost, instrument traces without leaking sensitive data, define fallbacks | Runbook; silent fallback can give unsupported answers |
| Iteration | Compare changes against baseline and regressions; distinguish prompt, data and system failures | Change decision; hand-selected success examples are weak evidence |

Levels: junior builds a bounded traceable flow; independent handles failures and repeatable evaluation; senior controls deployment, access and operational tradeoffs at scale.

Question: "Why use an agent rather than a workflow?" Tie choice to branching uncertainty, tool needs, failure cost and recoverability. A simple workflow is a valid answer.
[AI workflow sample](examples/ai_workflow.md) separates product and engineering deliverables. Check official sources for current tool APIs; this module does not claim a specific library version is required.

## Interview drills

**A cited answer is wrong.**
"I would inspect whether retrieval found the right current source, whether the source supports the specific claim, and whether generation changed its meaning. Citation presence alone is not grounding. I would add the failure to the relevant retrieval or answer-support evaluation, then compare a targeted fix against regressions rather than simply enlarge the prompt."
Follow-up: sources disagree. Preserve the conflict and abstain/escalate where the task cannot tolerate guessing.

**A tool times out after possibly changing an account.**
"I would classify the outcome as unknown rather than failed. I would query operation status or reconcile using the tool's supported operation identity before retrying a mutation. If the tool cannot support that recovery, I would constrain the workflow and involve a human rather than claim exactly-once execution."
Levels: junior recognizes the side effect; independent implements bounded recovery; senior addresses authorization, audit and operational ownership across tools.
