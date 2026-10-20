I’m using the Interview Master skill’s technical and campus guidance. Both answers below are hypothetical design answers: neither candidate has supplied work history, so neither should present the scenario as a migration they personally delivered.

The correctness requirement is the same at both levels: **a successful migration must preserve acknowledged writes, including updates and deletes.** The difference is how much of the design, failure handling, and operational decision-making the candidate is expected to own.

| Dimension | Campus backend candidate | Senior backend candidate |
|---|---|---|
| Clarification | Ask whether a write pause is allowed and what “no lost writes” means | Define acknowledgement and durability semantics, transaction scope, downtime budget, scale, and rollback requirements |
| Design | Give a simple coherent migration and identify why copy-while-writing is unsafe | Design the snapshot/change-stream relationship, cutover ownership, consistency checks, and operational controls |
| Failure reasoning | Explain a write arriving during copy and what happens on a failed migration | Handle crashes, retries, replay ordering, deletions, lag, log retention, stale writers, and rollback after new writes |
| Validation | Verify contents and test writes around the transition | Validate at a common boundary, rehearse failures, define abort criteria, and make go/no-go ownership explicit |
| Communication | Show sound fundamentals and state limitations | Defend trade-offs and explain exactly when guarantees hold or cease to hold |

A campus candidate does not need to invent a complex distributed design to demonstrate judgment. A senior candidate should not rely on “dual-write and switch” without explaining partial failures.

**Campus worked answer: choose a controlled write pause**

Assumptions for this example: the application uses one logical authoritative datastore; the dataset can be copied during an accepted maintenance window; all writer paths can be stopped; and the destination supports the required data and transaction semantics.

Suggested spoken answer, approximately two minutes:

> “I would first confirm whether we can pause writes. If the data can be copied within an acceptable maintenance window, I would choose a controlled pause because it makes the consistency argument simpler.
>
> “I would prepare and test the destination schema and the application’s compatibility first. At migration time, I would stop admission of new writes across the application, workers, and administrative paths, then wait for in-flight transactions to finish or roll back. Requests that cannot be processed would receive a clear retryable response; I would not acknowledge writes that were not durably recorded.
>
> “Once the source is stable, I would take a consistent copy and import it into the destination. I would compare the actual data and relevant constraints rather than relying only on row counts. While writes remain paused, I would switch the configured datastore and fence old writers so a stale application process cannot continue writing to the source. I would verify the new connection and data before reopening writes.
>
> “If copy or validation failed before reopening, I would keep the original source authoritative and resume there after making sure the destination cannot accept writes. If the destination had already accepted new writes, I would not simply switch back, because the source would be missing those writes. That would need a separate reconciliation or reverse-transfer plan. If a full write pause were unacceptable, I would explain that this approach does not meet the availability requirement and discuss a change-log-based migration.”

Walk through a concrete hypothetical event: write W1 commits before the pause is fully established, so it must be present in the stable source and copied. Request W2 arrives after admission is closed, receives a retryable response, and is not acknowledged as successful. After cutover, a retry is accepted by the destination; an idempotency key prevents a retry of an already committed request from causing duplicate business effects where that is required.

Failure test: leave a background worker pointed at the source. If it can still commit after the cutover barrier, the design fails. It must be stopped or fenced, not merely omitted from the routing change.

Alternative: a consistent snapshot plus change capture reduces the long pause but introduces replay and cutover complexity. The campus answer earns credit by recognizing when its simpler assumption is unacceptable.

**Senior worked answer: snapshot plus durable change capture, then a brief fenced cutover**

Assumptions for this example: the source can expose a consistent snapshot tied to a durable change-log position; the log includes inserts, updates, and deletes and retains changes long enough for the migration; transformations preserve required semantics; and a brief final write pause is acceptable. If the datastore cannot provide these properties, the plan must change.

Suggested spoken answer, approximately three minutes:

> “I would start by defining the guarantee: every source transaction acknowledged as committed before cutover must be reflected in the destination at the handoff boundary, and subsequent acknowledged writes must be durable in the destination. I would also confirm whether we need cross-record transaction atomicity and whether a brief write pause is acceptable.
>
> “I would keep the source as the sole application write authority during backfill. I would create a consistent snapshot at a known log position, preserve the log from that position, and load the snapshot before replaying subsequent changes. Replay must handle inserts, updates, and deletes, preserve the ordering and transaction semantics the application requires, and be safe to retry. I would persist replay progress only after the corresponding destination changes commit; if a crash causes replay, idempotency must prevent duplicate effects.
>
> “During catch-up, I would monitor lag, log-retention headroom, failures, and data reconciliation. I would validate transformed records and business invariants at a consistent boundary, rather than compare independently changing datasets and assume differences are harmless. If the log gap became unrecoverable or validation failed, I would stop and re-establish a trustworthy baseline instead of guessing what was missed.
>
> “For cutover, I would block new source writes, drain in-flight transactions, and fence every source writer. I would record the final committed position and wait until the destination had applied through it. With writes still blocked, I would complete the final validation, switch the write authority and routing, and then reopen writes against the destination. Stale clients must be rejected by the fence; a routing update alone is not sufficient.
>
> “Before the destination accepts new writes, rollback can restore source authority under a controlled fence change. After it accepts writes, the source is stale. I would either fail forward or use a separately tested reverse synchronization and reconciliation procedure before any return. I would retain the old data and migration evidence until the recovery window closes and make the cutover and abort decisions explicit.”

Worked event sequence:

1. A consistent snapshot is taken at log position 100. The source remains the write authority.
2. An update at 101 and a delete at 102 occur while the snapshot is copied. Both remain in the durable log.
3. The snapshot is loaded, then 101 and 102 are applied. If replay crashes after applying 101 but before recording progress, replaying 101 must not apply a business increment twice. The implementation must use an appropriate idempotent representation or atomic deduplication scheme.
4. At the final pause, the source drains to position 150. The destination must apply through 150 before promotion. A lagging destination at 149 is a no-go, even if its row count looks plausible.
5. After promotion, new write W151 is acknowledged only by the destination. Returning immediately to the source would lose that acknowledged write from the authoritative state, so “flip the flag back” is not a safe rollback plan.

Key failure tests for the senior candidate:

- Crash the replay process around destination commit and checkpoint persistence; verify no omissions or duplicate business effects.
- Replay a delete and ensure a later snapshot load cannot resurrect it; loading the snapshot before replay is one way this example avoids that race.
- Delay replay beyond the log-retention horizon; migration must halt or rebootstrap rather than continue with a gap.
- Leave a stale source writer active; fencing must reject its writes after the authority change.
- Simulate a destination failure after it has accepted writes; demonstrate recovery without discarding them.

The tempting alternative is application-level dual writes. A source write may succeed while the destination write fails, so naive dual writes do not guarantee preservation or consistency. A transactional change log or outbox with replay can address that gap under explicit assumptions, but still needs a correct snapshot boundary and cutover process.

Useful follow-up questions are: “What if the replay checkpoint is lost?”, “What if a delete arrives during backfill?”, and “What exactly makes rollback unsafe after promotion?” For the campus candidate, look for a correct basic argument and awareness of limits. For the senior candidate, look for an explicit failure-safe protocol and operational decisions. These are expectations for the exercise, not evaluations of either person’s observed ability.

---
Evaluation limitation: Generated in the same shared evaluator and baseline batch context as the earlier baseline cases, not a blinded isolated model run. Only the supplied v3 baseline Skill, its relevant references, and the raw scenario inputs were used; no browsing or external actions were performed.
