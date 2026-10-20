# Mobile/client engineering

| Capability | Procedure | Evidence / tradeoff / failure |
|---|---|---|
| Offline state | Define local truth, queue mutations, explicit sync state and conflict policy | State machine; "retry later" alone cannot resolve conflicting edits |
| Networking | Design timeout, retry/backoff, cancellation and deduplication around connectivity | Failure tests; reconnect bursts can drain battery and duplicate actions |
| Lifecycle | Persist needed state across backgrounding, restart and interrupted work | Recovery trace; in-memory state may disappear mid-operation |
| Device resources | Measure bandwidth, memory, battery and storage on relevant device classes | Budget/test matrix; high-end simulator results may hide practical failures |
| Compatibility/UX | Consider old clients, accessibility, permissions and user-visible recovery | Upgrade and recovery plan; silent data loss is not graceful degradation |

Levels: junior implements explicit states and failure UI; independent handles sync/lifecycle invariants; senior makes platform, rollout and resource tradeoffs across device cohorts.

Question: "Two devices edit an offline item." State whether conflicts are acceptable, how identities and versions work, how the user sees resolution and what can be recovered. No single conflict policy fits every data type.

Use the mobile task in [client samples](examples/frontend_mobile.md). These are authored scenarios, not copied third-party architecture diagrams.

## Interview drills

**The user sees 'saved' but loses an edit after restart.**
"I would determine whether 'saved' meant only in-memory state, durable local storage or server acknowledgement. I would persist the mutation and recovery metadata before promising durable local save, then expose sync status separately. I would test termination before send, after send and before acknowledgement, reusing operation IDs when retrying."
Failure: using server reachability as a substitute for a durable local queue.

**Sync is correct but drains the battery.**
"I would measure which operations and wakeups drive the cost on relevant devices and connectivity patterns. I would batch nonurgent work and apply bounded retry/backoff while preserving urgent user-visible behavior. I would compare delay, bandwidth and battery effects rather than assume one polling interval suits every task."
Follow-up: users require immediate updates on foreground screens but not in the background. Separate those needs and verify lifecycle transitions.
