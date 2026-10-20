# Backend migration without lost writes
Synthetic system-design exercise.

## Task and constraints
Move customer preferences from store A to store B while writes remain available. The system accepts 200 writes/second at peak. A remains authoritative initially. Reads may lag by up to five seconds; confirmed writes must not be lost. Both stores support a per-record version field. You may change application code but cannot atomically transact across both databases. The numbers are task assumptions, not benchmarks.

Deliver request flow, stages, invariants, failure handling, cutover/rollback criteria and observability.

## Reference design
Do not use uncoordinated dual writes as if they were atomic. One possible approach commits the business update plus a durable change record in A's transactional boundary, if A supports it; otherwise explicitly choose a supported durable change capture mechanism and verify its guarantees. The migration cannot assume this ability silently.

Consume changes into B with idempotent application using record/version identifiers. Define ordering per entity and reject stale versions. Include deletion/tombstone behavior. Record durable checkpoints and monitor lag, failures and reconciliation discrepancies.

Backfill a consistent snapshot or record a change-log position that permits reconciliation with concurrent writes. A newer streamed update must not be overwritten by older backfill data. Reconcile logical records and invariants, not just row counts.

Stages:
1. Instrument current behavior and test recovery.
2. Backfill and continuously apply changes while A remains authoritative.
3. Shadow reads from B; compare normalized values without affecting user responses.
4. Canary reads with a fallback; watch correctness and lag.
5. Change write authority only after a defined compatibility/recovery plan and verified catch-up.

## Invariants and validation
A confirmed write is durably represented in the source and replay path. B converges within the required lag under the agreed workload. Retries do not apply an operation twice. Older versions do not win. Test worker crash, replay, backlog growth, deletion, partial outage and schema mismatch.

Accept cutover only after reconciliation errors are understood, lag remains within the agreed target over representative workload, and the rollback procedure has been exercised. Time duration is chosen from actual workload evidence, not a universal number.

## Alternatives and rollback
A brief write pause may simplify final cutover if the business later permits it; presently it violates the stated availability requirement. Keeping A authoritative longer reduces cutover risk but retains operational cost.

Before B accepts independent writes, routing reads back to A can be simple. After authority changes, rollback needs a verified reverse/synchronization path or a controlled recovery procedure. Do not promise "just switch back" and lose B-only writes.

## Spoken demonstration
"I would make the source of truth explicit at every stage. Since the two stores cannot share a transaction, ordinary dual writes leave a loss window. I would use a durable replay path supported by the source, version-aware application in the destination, and reconciliation during backfill. I would move reads gradually, then switch write authority only with tested recovery and acceptable lag. Rollback after that point requires preserving writes made in the new store."

## Pressure and rubric
Backlog grows faster than workers drain it. Estimate sustainable throughput, investigate bottlenecks, protect source availability and delay cutover; adding workers can worsen source load.
Junior: coherent request/state path and failure handling.
Independent: replay, ordering, backfill race and reconciliation.
Senior: authority transitions, safe rollback, operational ownership and resource tradeoffs.
Next drill: draw the source-of-truth and replay boundary for each stage.
