# Interview Master

**Turn real experience into interview answers you can explain, defend and practice.**

A multilingual interview skill for **Codex, WorkBuddy, Claude and agents supporting Agent Skills**. Use the same package to prepare tailored answers and worked exercises, learn professional methods, and practice adaptive interviews.

[中文](README.md) · [Installation and compatibility](docs/compatibility.md) · [Capability changes](docs/capability-upgrade-v4.md) · [Codex acceptance](evals/reports/codex-acceptance.md) · [Contributing](CONTRIBUTING.md)

> **v4.0.0-rc.2 is a local candidate awaiting maintainer acceptance.** It has not been pushed or published to GitHub. Format portability and verified host behavior are reported separately.

## Start with one request

After installation, provide your job description and experience:

```text
Use interview-master to prepare me for this role.
Give me complete preparation, with Chinese explanations and English answers.
Produce a useful draft and full tailored answers first, then batch key fact checks.
Do not turn participation into ownership or invent missing results.
```

You receive role priorities, evidence mapping, an introduction, project answers, targeted questions and a useful next exercise. Missing facts are handled according to their effect on the task.

## Choose your preparation pace

| Need | Mode | First useful output |
|---|---|---|
| “The interview is tomorrow; I have 40 minutes” | Sprint | Priority risks, usable answers and a recap |
| “Give me the full preparation packet” | Complete | A concrete draft before consolidated questions |
| “Teach the method, then let me try” | Coach | Explanation, worked solution, tradeoffs and practice |
| “Start a pressure interview” | Mock | One question at a time, with adaptive follow-ups |

Ask directly for an introduction, résumé edit, questions for the interviewer, debrief, salary preparation or offer comparison. Choose questions, outlines, full answers or a learning packet. Standard, challenging and high pressure are independent of mode.

## One package, multiple agents

| Agent | Installation | Validation |
|---|---|---|
| Codex | Project `.agents/skills/interview-master/` | CLI project installation and 10 bounded checks passed; see [results](evals/reports/codex-acceptance.md) |
| WorkBuddy | Skills management → add → upload local package | Official import route checked; no client execution claimed |
| Claude | Import the full ZIP through its supported skill interface | Available installation route; this candidate has not been run in the client |
| Other Agent Skills hosts | Their skill directory or importer | Reuse the format, then verify discovery, references and behavior |

Install the entire `interview-master/` folder, including `SKILL.md` and `references/`. No host-specific API, MCP server or runtime script is required. See [host-specific instructions](docs/compatibility.md), including official sources and update guidance.

For Codex, start in the project and ask it to use the project-local interview-master and identify the loaded entrypoint. If a global older version shares the name, select the intended project path. The remote published version is not yet this local candidate.

## Languages without changing the facts

Set coaching, answer and mock languages separately, and switch while preserving the current question. Hiring market is an independent setting.

```text
Prepare everything in English, including headings and worked examples.
Interview me in English. Give feedback in Chinese when we finish.
Use Chinese explanations and natural English model answers.
Ahora solo español. Continúa con la pregunta pendiente.
```

“Contributed to” must not become “led.” Moving from 15% to 18% is 3 percentage points. Professional reasoning and language clarity receive separate feedback. Text does not establish pronunciation, eye contact or actual speaking speed. Chinese, English, Spanish and French have reviewed samples; this is not native-language certification.

## Learn how to solve the work

| Direction | Focus | Worked example |
|---|---|---|
| Product | Problem selection, priorities, validation and delivery | [Product decision](references/examples/product_decision.md) |
| Operations/growth | Segmentation, execution, costs, retention and attribution | [Campaign decision](references/examples/operations_growth.md) |
| Data | Metric definitions, SQL, experiments and decisions | [Mix-shift diagnosis](references/examples/data_diagnosis.md) |
| Engineering | Backend, frontend, mobile and AI applications | [Migration](references/examples/backend_migration.md), [client state](references/examples/frontend_mobile.md) |
| AI product | Task value, autonomy, human review and evaluation | [AI workflow](references/examples/ai_workflow.md) |
| Management | Resource choices, dependencies, feedback and team mechanisms | [Management decision](references/examples/management_decision.md) |

Modules include complete approaches, alternatives, failure conditions and level-specific anchors. Other roles use provisional JD adaptation rather than a claimed mature specialist module. [Role catalogue](references/role_catalog.md)

## A concrete example

Synthetic input: “I helped coordinate an onboarding checklist. Engineering wrote the code. My résumé says conversion went from 15% to 18%, but causality is unverified.”

A usable answer preserves those boundaries:

> I contributed to coordinating the onboarding checklist, while engineering was responsible for the code. My résumé reports conversion rising from 15% to 18%, a 3-percentage-point increase. I cannot establish that the checklist caused that change.

The next practice probes your specific contribution and how to validate impact. It does not fill the evidence gap with invented achievements. [Full pause/language example](evals/outputs/fresh-package-language-pause.md)

## Evidence and limits

- 17 deterministic tests cover repository and release invariants.
- The rc.1 behavioral record contains 36 categories, eight v3 baseline cases, six paired role comparisons and two fresh package scenarios: 58 reviewed outputs.
- rc.2 is installed into a real Codex project skill directory for host acceptance. [Results and limitations](evals/reports/codex-acceptance.md)

The baseline also produced good first-turn answers. These samples do not prove consistent speed improvements or higher hiring success. Read the [capability change explanation](docs/capability-upgrade-v4.md) for implemented mechanisms versus demonstrated outcomes.

## Common questions

**No browsing or file writing?** Work from supplied evidence, identify research gaps, and deliver complete text plus a continuation summary in chat.

**Want the answer during a mock?** Say “Pause; explain and show an example.” Resuming keeps the current question; performance after viewing a model answer is guided practice.

**Will it guarantee an offer?** No. Generated material, completed practice and observed competence are separate states.

**Will an update overwrite my résumé?** Keep candidate materials outside the skill folder. Update or roll back the skill package while preserving submitted versions and edits. [Migration](docs/migration-v4.md)

## Build and contribute

From the repository root:

```sh
python3 -m unittest discover -s tests -v
python3 scripts/validate_repository.py
python3 scripts/build_release.py --version 4.0.0-rc.2 --output-dir dist
```

The archive is `dist/interview-master-v4.0.0-rc.2.zip`. Evaluations, development documents and candidate sessions are excluded from the runtime package.

Contribute reproducible failures, language corrections or role modules with complete solutions. [Guide](CONTRIBUTING.md) · [Roadmap](docs/roadmap.md) · [Changelog](CHANGELOG.md) · [21-project research](docs/source-notes.md) · [README design sources](docs/readme-design-notes.md)

MIT. Linked material retains its own license. Keep personal facts outside the public repository. The skill does not independently apply for jobs, contact people or publish candidate materials.
