# Actual Codex host evidence

These synthetic scenarios were run in the real Codex CLI against the extracted rc.2 package, not simulated by the parent conversation.

- [Acceptance report](../reports/codex-acceptance.md): criteria, outcomes, environment failures and limits.
- `inputs/`: actual scenario prompts.
- `outputs/`: generated final responses and delivered work samples. Local links were remapped for this repository; answer content was not improved after execution.
- [Event summary](events-summary.json): completed tool commands, exit codes, output digests, file changes and terminal states. Home/workspace paths are redacted. Hidden reasoning, account data and global logs are excluded.

Original CLI event streams remain in the local acceptance workspace. The public summary is deliberately narrower than those logs. Three sessions share context within their respective continuation turns; do not treat every turn as an independent trial.
