# Frontend engineering

| Capability | Procedure | Evidence / tradeoff / failure |
|---|---|---|
| Interaction/state | Model loading, success, empty, error, retry and stale states; separate server from local state | State diagram; concurrent responses can overwrite newer intent |
| Accessibility | Use semantic controls, labels, keyboard flow and focus recovery; test meaningful tasks | Interaction test; visual success can still exclude keyboard users |
| Performance | Measure user-visible delay, identify network/render/work bottleneck and reduce it | Before/after test plan; optimizing a synthetic score may miss the actual task |
| Data integration | Specify API errors, cancellation, pagination, validation and cache invalidation | Contract tests; optimistic UI needs failure reconciliation |
| Architecture/delivery | Choose component boundaries from ownership and change patterns; monitor release cohorts | Maintainable design; abstraction too early can increase complexity |

Levels: junior implements correct states; independent diagnoses cross-component issues and validates real user paths; senior manages design-system/platform tradeoffs and migration.

Question: "Search shows results for the previous query—how do you fix and test it?" Trace request order and state commits; a solution can discard stale response IDs or cancel requests, but must handle errors and accessibility.

Use the frontend task in [client samples](examples/frontend_mobile.md). Do not infer frontend ability from distributed-system terminology alone.

## Interview drills

**The page passes a visual review but users cannot finish checkout.**
"I would test the actual task with keyboard navigation, focus transitions, labels and error recovery as well as the visual path. I would inspect whether validation errors are understandable and whether focus reaches the relevant field or status. I would add tests for the failed interaction, not just another screenshot."
Follow-up: a modal traps focus after an async error. Trace lifecycle and focus restoration; do not label the problem solved by a color change.

**Would you introduce a shared state library?**
"I would first identify which state needs to be shared, how often it changes and where synchronization errors occur. Local interaction state and server-derived data can have different lifecycles. I would compare a small explicit boundary with a broader abstraction, and choose the least complex approach that preserves correctness and remains testable as the product evolves."
Junior: correct local behavior; independent: handles cross-component consistency; senior: evaluates migration and team maintenance costs.
