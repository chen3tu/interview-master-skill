# Contributing / 贡献指南

Use an issue or PR to describe a concrete failure, missing role capability or language problem. Chinese and English contributions are welcome. Supply synthetic or carefully de-identified examples, never full personal résumés, private employer material or unpublished interviews.

## Runtime changes
Keep shared routing in SKILL.md; put conditional detail in focused references. Every runtime resource must be reachable from the entrypoint and available inside the release payload. Prefer one source of truth over translated duplicate rule sets. User-facing language is controlled by the language contract.

For a role module include actual work goals, principles, procedures, level differences, a complete worked example, alternatives, failure/change conditions and evaluation. Five question titles with STAR hints are not sufficient.
Mark hypothetical data. Do not imply official employer rubrics, unsupported success rates or past experience.

## Language changes
Test headings as well as body text, meaning/ownership preservation, numerical units, mixed-language coaching, switching mid-session and market assumptions. Separate language feedback from professional competence. Do not claim native-level validation without appropriate reviewers.

## Verification
Run:
~~~sh
python3 -m unittest discover -s tests -v
python3 scripts/validate_repository.py
~~~
If changing packaging, build twice and check reproducibility and package contents. If changing behavior, run realistic cases from evals/cases.json or add a demonstrated failing case. Preserve actual outputs and disclose model/tool limits. A text keyword check cannot prove the skill behaves correctly.

## Licensing and review
Write original material or document compatible provenance. A publicly visible repository is not automatically permissively licensed. Do not import restricted third-party questions, diagrams or personal data.

Describe the user-visible before/after behavior and relevant verification in the PR. Small, coherent changes are easier to review; preserve unrelated work.
