# Interview Master

[中文](README.md) · [Contributing](CONTRIBUTING.md) · [Changelog](CHANGELOG.md)

A multilingual interview-preparation skill built around real candidate evidence and the target job. Produce useful preparation, learn professional methods, and practice adaptive interviews.

**Development candidate: v4.0.0-rc.1, not a published stable release.** See the [validation status](evals/reports/v4-release-check.md).

## Choose the way you prepare

- **Sprint:** focus on the most important answers and risks.
- **Complete preparation:** receive a usable draft before a consolidated fact check.
- **Coaching:** learn through examples or attempt the problem first.
- **Mock interview:** one question at a time, adaptive follow-ups, immediate pause when requested.

Ask directly for an introduction, project answer, reverse questions, salary preparation or offer comparison. Choose questions only, outlines, full answers or a learning packet. Pressure intensity is independent.

## Languages

Specify coaching, answer and mock languages independently:

~~~text
Prepare everything in English, including headings.
Interview me in English; explain feedback in Chinese.
Use Chinese explanations and natural English model answers.
Réponds uniquement en français pour cette préparation.
~~~

Facts, ownership, numbers and uncertainty must survive translation. Hiring market is separate from language. Language clarity is evaluated separately from professional reasoning. Text alone cannot establish pronunciation, eye contact or actual speaking pace.

Chinese and English have explicit examples. Additional languages use the same contract; quality depends on the host model and validation is limited to the documented cases.

## Professional depth

Modules cover product, operations/growth, data analysis, engineering, AI product and management. Engineering includes backend, frontend, mobile and AI application work. Synthetic work samples include complete approaches, alternatives, failure conditions and evaluation anchors.

A full packet can include role priorities, a JD/evidence matrix, introductions, project answers, tailored questions with answers, professional teaching, work samples, reverse questions and a recap. Unknown historical metrics remain unknown; they do not block unrelated preparation.

Other roles use explicitly provisional JD adaptation. Generated materials are not proof that practice occurred or that a candidate will be hired.

## Build and use

~~~sh
python3 -m unittest discover -s tests -v
python3 scripts/validate_repository.py
python3 scripts/build_release.py --version 4.0.0-rc.1 --output-dir dist
~~~

The ZIP contains the full skill folder with SKILL.md and references. Keep references alongside the entrypoint. Claude's upload instructions and prerequisites are documented in its [official guide](https://support.claude.com/en/articles/12512180-use-skills-in-claude), checked on 2026-10-20. This does not claim a live installation test of this candidate.

No mandatory runtime CLI or account service. Without browsing, preparation proceeds from supplied evidence; without file writing, use chat output and a continuation summary.

[Migration](docs/migration-v4.md) · [Evaluation](evals/README.md) · [Sources](docs/source-notes.md) · [Roadmap](docs/roadmap.md)

Keep résumés and sessions outside the installed skill and public repository. Nothing is automatically sent or published. MIT; linked third-party content retains its own terms.
