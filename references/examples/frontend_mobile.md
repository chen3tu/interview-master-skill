# Client work samples
Both tasks are synthetic and share a shopping-list product. They require different evidence from a backend capacity exercise.

## A. Frontend: stale search results

Input: the user types "milk", then "oat milk". The second request returns first, but the older request later replaces it. Slow connections and keyboard-only users must be supported.
Output: state flow, proposed fix and tests.

Reference: assign each query a monotonically changing request identity; only commit a response if it belongs to the current query. Cancellation can save work but is not by itself proof that a late response cannot arrive. Keep query text, pending state, result data and error state explicit. Debounce can reduce traffic, but does not solve out-of-order responses.

Preserve focus while results change; use labelled search controls and appropriate status announcements. Distinguish no results from loading or failure. On failure, retain recoverable intent and offer retry without silently displaying stale results as current.

Tests: force requests to resolve in reverse order; clear the query mid-flight; trigger an error then retry; navigate suggestions with keyboard; check loading and empty states. Performance: inspect actual typing-to-useful-result delay and request count under representative conditions.

Alternative: cache by query for quick repeat queries, with an explicit freshness rule. It still needs current-query identity. Avoid a global state framework merely to fix one race if local state is sufficient.

Spoken demonstration: "I would first reproduce the ordering problem, then guard state updates by the current query identity. I might cancel old requests to reduce work, but I would still reject stale responses. I would test reversed completion order, cleared input and failures, and ensure result updates don't disrupt keyboard navigation."

Pressure: the requirement now allows cached results immediately. Label cached/current status where meaningful, revalidate and preserve the current-query guard.
Junior: recognizes the race and writes targeted tests.
Independent: handles failure, cache and accessibility states.
Senior: chooses shared abstractions and rollout measurement without unnecessary complexity.

## B. Mobile: offline list edits

Input: two devices can edit the same item while offline; one changes quantity, the other deletes it. Users must not silently lose work after restart. Output: local state and sync protocol, conflict UX, resource considerations and tests.

Reference: save local changes durably with operation IDs and base versions. Show pending/synced/conflict states. On reconnect send queued operations with deduplication and bounded retry. The server accepts compatible versions or returns current state for resolution. For delete-vs-edit, choose and disclose a product policy: for example, offer restore/reapply from a recoverable conflict rather than silently discarding the edit. The correct policy depends on the domain.

A server-time last-write-wins policy is simpler but can lose intentional edits; client clocks are not a reliable sole ordering rule. Automated field merges help independent changes but cannot always resolve deletion or semantic conflicts.

Persist the queue before showing a durable-save confirmation. Recover it after termination. Batch nonurgent sync where appropriate and measure battery/network cost rather than keeping constant polling. Test duplicate delivery, partial sync, restart, offline edits on both devices and permission revoked before reconnect.

Spoken demonstration: "I would distinguish a locally saved edit from a server-synced edit. Each queued operation needs an identity and a base version so retries and conflicts are explicit. For delete-versus-edit, I would preserve recoverable work and apply a clear product rule rather than claim synchronization can always merge it automatically."

Pressure: the app is terminated after sending but before receiving acknowledgement. Retry the durable operation with the same ID; do not create a new operation and duplicate its effect.
Junior: explicit local/pending/error states.
Independent: durable recovery, duplicate delivery and conflicts.
Senior: resolves product consistency, battery, compatibility and operational tradeoffs.
Next drill: show the same conflict to a user in one sentence in the chosen language, without implementation jargon.
