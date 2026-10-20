# Interview Master v4.0.0-rc.2 — maintainer-accepted prerelease

This candidate makes interview preparation configurable across modes, roles and languages, with a host-neutral Agent Skill package for Codex, WorkBuddy, Claude and compatible agents.

## What changed

- Choose sprint, complete preparation, coaching or mock interview; output depth and pressure remain independent.
- Map job responsibilities to tasks, evidence and targeted questions; collect unresolved facts after a usable draft.
- Practice with deeper product, operations/growth, data, technical, AI product and management modules and seven synthetic worked examples.
- Pause pressure interviews immediately, explain and demonstrate, then resume the pending question without treating the demonstration as the candidate's performance.
- Configure coaching, answers and mock language separately; retain numbers, contribution boundaries and unknown causality when switching languages.
- Use one self-contained runtime package with host-specific installation instructions and explicit capability fallbacks.

## Evidence

17 automated tests, deterministic packaging, 58 prior reviewed behavior outputs and actual rc.2 Codex CLI execution are recorded in the [release check](../evals/reports/v4-release-check.md). See the [Codex acceptance report](../evals/reports/codex-acceptance.md) for individual criteria, interrupted attempts, recoveries and limits.

WorkBuddy and Claude client execution has not been tested. No stable speed advantage over v3, hiring-success improvement or universal language reliability is claimed.

## Install and migrate

Use the complete `interview-master/` directory from the ZIP. Follow [host-specific installation](compatibility.md) and [migration guidance](migration-v4.md). Candidate résumés, facts and sessions belong outside the Skill directory; replacing the runtime must not replace user data.

Archive: `interview-master-v4.0.0-rc.2.zip`  
SHA-256: `466d5b10bf400edbb42ccf17c687b529454f205aa921107931b80b0671342ee2`

**Maintainer acceptance: 2026-10-20.** The maintainer explicitly authorized GitHub publication. This prerelease retains the exact runtime payload tested in Codex. [Publication record](publication-v4-rc2.md).
