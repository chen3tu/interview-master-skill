# v4.0.0-rc.1 release check

2026-10-20. **Locally validated development candidate, not a formal release.** Live-host installation remains an open gate.

## Candidate identity

- Source baseline: de3a72cd9493f09d3c33079587e37130b62cbd2b, rechecked through GitHub before implementation.
- Working branch: upgrade/v4, isolated clone; original checkout preserved.
- Runtime source commit: 2b72fec0406e2578e40a4c2b8ab266307888c95f; tooling commit: 65af548.
- Archive: dist/interview-master-v4.0.0-rc.1.zip
- SHA-256: eb558fb64d0acacae9493a7406ae211bd6137d0da8a0485932168636a98929cf
- Size: 63,808 bytes; 41 files: SKILL.md plus 40 references.
- dist/manifest.json records the complete payload list and checks. Build outputs are intentionally ignored by Git; regenerate with the README command.

## Completed checks

| Check | Observed result |
|---|---|
| Baseline unit tests | 11 passed before changes |
| Current unit tests | 17 passed; see [raw log](local-checks.md) |
| Skill-creator frontmatter validator | Skill is valid; existing cached PyYAML used, no global install |
| Runtime graph | All runtime references exist inside the release payload and are reachable |
| Packaging | Two builds byte-identical; extracted runtime validation passed |
| Distribution boundary | Only runtime payload included; no tasks, eval outputs, candidate workspaces or development docs |
| Bounded identifier scan | No matches for local user path/name/personal-skill identifiers or private-key marker; synthetic samples manually reviewed |
| Behavior | 36 categories, eight v3 baseline cases, six paired role cases, two fresh package scenarios executed and reviewed; see [behavior report](v4-behavior-report.md) |
| Data sample | SQLite example checked with duplicates, absent events and ineligible users; event-window precondition documented |
| Arithmetic | Mix shift and fixed/target compensation reviewed; old salary arithmetic corrected |
| Documentation | Chinese/English README and migration reviewed; official Claude installation documentation checked |

The identifier scan is a bounded check, not a guarantee against every possible sensitive string. Examples were authored as synthetic teaching material. Backend and AI examples were reviewed as designs; no real service or load/failure test was run.

## Open gates and measured limits

1. **Live Claude installation not performed.** Documentation verification and direct reading of an extracted ZIP do not test installer registration, automatic activation, reference loading in Claude, or updates of an existing user workspace. No accessible live Claude session was used. Complete one preparation and one mock/pause scenario in the target host before declaring compatibility verified.
2. E01–E08 baseline cases and six fixed candidate/JD comparisons are complete; see [role comparison](role-comparison.md). The cases share evaluator context within batches and are small synthetic samples, not calibrated performance estimates.
3. E01 produced useful first-turn material with zero blocking intake in both v3 and v4. The planned relative speed improvement is not demonstrated. No latency or hiring-success claim is made.
4. Batch cases share context within each of three evaluators. Final source additions received two fresh package checks plus six fixed role cases, not a full rerun of every category. No native-language expert audit or long-conversation reliability estimate.
5. Candidate release notes and rollback guidance are ready, but live-host acceptance is still open. Keep rc.1 status.

## Publication and installed copies

No remote push, pull request, merge or Release was performed. Installed generic and personal skills remain unchanged. Review the candidate from this checkout and ZIP. [Migration and rollback](../../docs/migration-v4.md) preserve user résumés, facts and sessions outside the skill installation.

[Release text draft](../../docs/release-v4-rc1.md) · [Execution ledger](../../tasks/todo.md)
