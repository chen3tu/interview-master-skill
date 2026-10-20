# v4.0.0-rc.2 release check

2026-10-20. **Local candidate; user acceptance required before any GitHub push.**

## Candidate identity

- Baseline: `de3a72cd9493f09d3c33079587e37130b62cbd2b`.
- Branch: `upgrade/v4`, isolated checkout.
- Runtime commit: `918a20b0650494e283ed953660ade721130fbddf`.
- Archive: `dist/interview-master-v4.0.0-rc.2.zip`.
- SHA-256: `466d5b10bf400edbb42ccf17c687b529454f205aa921107931b80b0671342ee2`.
- Size: 64,049 bytes; 41 files: SKILL.md plus 40 references.
- `dist/manifest-rc2.json` records payload identity locally. Build artifacts remain ignored by Git; use the README build command to regenerate.

## Verification

| Check | Result |
|---|---|
| Unit tests | 17 passed after the host-neutral runtime change |
| Frontmatter | Skill-creator validator passed; cached dependency, no global installation |
| Runtime graph | All shipped references reachable and inside the runtime package |
| Deterministic build | Two rc.2 builds byte-identical |
| Installed payload | Actual Codex project installation matches all 41 ZIP payload files byte for byte |
| Prior behavior | 58 reviewed rc.1 outputs; [report](v4-behavior-report.md) |
| Actual Codex execution | Installed package loaded by three CLI sessions; all 10 bounded criteria passed, including preparation, file delivery, pressure/pause/language continuation, data work sample and direct offer comparison; exact current matrix in [host report](codex-acceptance.md) |
| English work sample | Generated SQL executed in SQLite; three result sets verified after correcting the generated validation script's SQL splitting |
| Documentation | Chinese/English README, host installation matrix, capability report, migration and contribution guidance updated |
| Research | 21 categorized interview-related projects; three high-star documentation examples, with explicit source and reuse boundaries |

## Remaining release gate and limits

**The maintainer must explicitly accept the candidate before GitHub publication.** Local validation does not imply that approval.

The user's updated scope chooses Codex as the primary acceptance host. This supersedes the original mandatory Claude gate without pretending that Claude was tested. WorkBuddy and Claude have documented installation paths but no live client validation. Codex desktop skill-picker behavior, old-workspace upgrades and cross-host state migration were not tested.

The original run was interrupted by account quota and later resumed; CLI WebSocket retries fell back to HTTP. A read-only resume correctly delivered text without claiming a saved file; a subsequent explicit workspace-write resume saved it. All exceptions and final per-case outcomes are documented in the host report.

No proven relative speed improvement, native-language certification, interview-success increase or long-session reliability estimate. v3 already performed well in the small baseline sample. See [capability explanation](../../docs/capability-upgrade-v4.md).

## Publication and rollback

No push, PR, merge or Release performed. Global public/personal skill installations and the original checkout remain unchanged; only the separate Codex acceptance project contains rc.2.

[Migration and rollback](../../docs/migration-v4.md) · [rc.2 release text](../../docs/release-v4-rc2.md) · [execution ledger](../../tasks/todo.md) · [historical rc.1 check](v4-rc1-release-check.md)
