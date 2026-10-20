# Backend and systems

| Capability | Procedure | Evidence / tradeoff / failure |
|---|---|---|
| Request/API design | Define caller, contract, validation, auth boundary, errors and idempotency needs | Request trace and examples; retries can duplicate side effects |
| Data/state | Model entities, invariants, transaction boundaries, consistency and retention | Schema and invariant checks; convenience joins can obscure ownership |
| Capacity/performance | Estimate workload using stated assumptions, identify bottleneck, measure before optimizing | Capacity model and test plan; average latency hides tails |
| Reliability | Enumerate failures, dependency timeouts, retry budgets, degradation and observability | Failure matrix and recovery criteria; retries may amplify load |
| Migration | Define compatibility, sequencing, backfill, reconciliation, cutover and rollback | Reversible plan; rollback is unsafe after incompatible writes |
| Delivery/security | Review access boundaries, secrets, deploy stages and operational ownership | Tests/runbook; do not trade correctness away for a benchmark |

Levels: junior traces a request and tests local correctness; independent owns service invariants and failure handling; senior designs migration, cost and cross-team operational tradeoffs.

Question: "Move data without interrupting writes." Ask which source is authoritative at each stage and how divergent records are detected. Valid alternatives depend on traffic, data model and acceptable lag; no universal queue/cache stack is required.

[Migration sample](examples/backend_migration.md) provides a complete reasoning task. Implementation-specific APIs, versions or numeric limits must be checked in official documentation before relying on them.

## Interview drills

**A client retries a timed-out write.**
"I would distinguish timeout from confirmed failure: the server may have committed the operation. I would use an operation identity and a defined idempotency scope so a retry can recover the previous outcome rather than duplicate the side effect. The identity's lifetime, payload consistency and concurrent requests need tests; storing a key without an atomic relationship to the effect may still leave a race."
Follow-up: the operation includes an external service. Explain which guarantees the external boundary supports and how to reconcile an unknown outcome, rather than promise a cross-system transaction.

**Latency increased after a deployment.**
"I would compare affected requests and deployment cohorts, check tail latency and errors, and trace time across dependencies and local work. I would form a discriminating hypothesis before changing cache, thread count or capacity. If the release correlates with user harm and rollback is safe, I would contain impact while preserving evidence, then verify recovery and root cause."
Levels: junior identifies where time is spent; independent tests hypotheses and contains harm; senior balances reliability, observability cost and rollout mechanisms.
