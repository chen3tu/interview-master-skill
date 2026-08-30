# Interview Master Repository Optimization Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make the Interview Master repository installable, self-validating, secure, and ready for structured community contributions.

**Architecture:** Keep the Skill content unchanged and add a standard-library Python validation/build layer around it. GitHub Actions runs the same commands used locally, while repository templates and README changes expose clear installation and contribution paths.

**Tech Stack:** Markdown, Python 3 standard library, `unittest`, GitHub Actions, GitHub CLI

**Spec:** `docs/plans/2026-08-30-github-optimization-design.md`

## Global Constraints

- Do not change the interview methodology or reference content in this optimization.
- Add no Python package dependencies; all validation and packaging use the standard library.
- The release asset must be a ZIP containing a single top-level `interview-master/` folder with `SKILL.md` and `references/`.
- All repository file changes are delivered through `chore/github-optimization` and a Pull Request.
- Do not commit generated files under `dist/`.

---

### Task 1: Repository validator and tests

**Files:**
- Create: `scripts/validate_repository.py`
- Create: `tests/test_validate_repository.py`

**Interfaces:**
- Produces: `validate_repository(root: pathlib.Path) -> list[str]`, returning human-readable errors and an empty list on success.
- Produces: CLI exit code `0` on success and `1` with one error per line on failure.

- [ ] **Step 1: Write failing unit tests**

Cover a valid temporary repository, a missing required file, malformed `SKILL.md` frontmatter, a missing Markdown relative link, and a missing backtick reference such as `references/example.md`.

- [ ] **Step 2: Run the tests and confirm the missing module failure**

Run: `python3 -m unittest discover -s tests -v`

Expected: FAIL because `scripts.validate_repository` does not exist.

- [ ] **Step 3: Implement the validator**

Use `pathlib`, `re`, and `urllib.parse`. Require `README.md`, `SKILL.md`, `CHANGELOG.md`, `CONTRIBUTING.md`, `LICENSE`, and `references/`; require frontmatter keys `name` and `description`; validate local Markdown links and all literal `references/*.md` paths without following external URLs or anchors.

- [ ] **Step 4: Verify the tests and current repository**

Run: `python3 -m unittest discover -s tests -v`

Run: `python3 scripts/validate_repository.py`

Expected: all tests pass and the repository reports `Repository validation passed.`

- [ ] **Step 5: Commit**

Run: `git add scripts/validate_repository.py tests/test_validate_repository.py && git commit -m "test: add repository validation"`

### Task 2: Automated checks and community health files

**Files:**
- Create: `.github/workflows/validate.yml`
- Create: `.github/ISSUE_TEMPLATE/bug.yml`
- Create: `.github/ISSUE_TEMPLATE/feature.yml`
- Create: `.github/ISSUE_TEMPLATE/config.yml`
- Create: `.github/PULL_REQUEST_TEMPLATE.md`
- Create: `SECURITY.md`

**Interfaces:**
- Consumes: the validator CLI and unit-test command from Task 1.
- Produces: a `Validate` workflow for pushes to `main` and all pull requests.

- [ ] **Step 1: Add the workflow**

Use `actions/checkout@v4`, then run `python3 -m unittest discover -s tests -v` and `python3 scripts/validate_repository.py`. Grant workflow contents read-only permission.

- [ ] **Step 2: Add structured contribution forms**

The bug form must request the affected stage, observed behavior, expected behavior, reproduction prompt with sensitive data removed, and environment. The feature form must request problem, proposed workflow, affected role/stage, and alternatives. Disable blank issues and point support questions to Discussions.

- [ ] **Step 3: Add PR and security guidance**

The PR template must check scope, privacy, reference links, validator execution, and CHANGELOG relevance. `SECURITY.md` must instruct users not to publish personal interview data or vulnerabilities in Issues and to use GitHub private vulnerability reporting.

- [ ] **Step 4: Validate and commit**

Run: `python3 scripts/validate_repository.py`

Run: `git diff --check`

Expected: both commands exit `0`.

Run: `git add .github SECURITY.md && git commit -m "chore: add community health and CI"`

### Task 3: README installation and project navigation

**Files:**
- Modify: `README.md`
- Modify: `CONTRIBUTING.md`

**Interfaces:**
- Consumes: the `Validate` workflow name and the planned `v3.0.0` release asset.
- Produces: accurate ZIP installation instructions and visible contribution/security links.

- [ ] **Step 1: Replace the nonexistent `.skill` instructions**

Point users to `releases/latest`, instruct them to download `interview-master-v3.0.0.zip`, and document Claude's `Customize > Skills > Upload a skill` flow. Retain the Claude Project and System Prompt alternatives.

- [ ] **Step 2: Add badges and navigation**

Add Release, Validate, License, Stars, and Forks badges. Add links for Issues, Discussions, contributing, security, and changelog. Add a short privacy note telling users to redact personal/company-sensitive interview information.

- [ ] **Step 3: Align contribution instructions**

Replace the manual-only local test section with the validator and unit-test commands, while retaining a Claude Project smoke-test step for behavioral changes.

- [ ] **Step 4: Validate and commit**

Run: `python3 scripts/validate_repository.py`

Run: `git diff --check`

Expected: both commands exit `0`.

Run: `git add README.md CONTRIBUTING.md && git commit -m "docs: improve installation and project navigation"`

### Task 4: Reproducible release ZIP

**Files:**
- Create: `scripts/build_release.py`
- Create: `tests/test_build_release.py`
- Modify: `.gitignore`

**Interfaces:**
- Produces: `build_release(root: pathlib.Path, version: str, output_dir: pathlib.Path) -> pathlib.Path`.
- Produces: `dist/interview-master-v3.0.0.zip` with deterministic file order and timestamps.

- [ ] **Step 1: Write failing packaging tests**

Assert the ZIP has exactly one top-level `interview-master/` directory, includes `SKILL.md` and every file under `references/`, excludes repository-only files, and produces identical SHA-256 hashes across two builds.

- [ ] **Step 2: Run the tests and confirm the missing module failure**

Run: `python3 -m unittest tests.test_build_release -v`

Expected: FAIL because `scripts.build_release` does not exist.

- [ ] **Step 3: Implement deterministic ZIP creation**

Use `zipfile.ZipFile` with deflate compression, sorted paths, a fixed ZIP timestamp, UTF-8 filenames, and executable bits disabled. Accept `--version` and `--output-dir` CLI arguments.

- [ ] **Step 4: Ignore generated output and verify**

Add `dist/` to `.gitignore`.

Run: `python3 -m unittest discover -s tests -v`

Run: `python3 scripts/build_release.py --version 3.0.0`

Run: `unzip -l dist/interview-master-v3.0.0.zip`

Expected: tests pass and the archive contains only the Skill folder payload.

- [ ] **Step 5: Commit**

Run: `git add .gitignore scripts/build_release.py tests/test_build_release.py && git commit -m "build: add reproducible skill package"`

### Task 5: Final branch verification and Pull Request

**Files:**
- Modify: `docs/superpowers/plans/2026-08-30-repository-optimization.md` checkbox state only if tracking is committed.

**Interfaces:**
- Consumes: all prior task outputs.
- Produces: a reviewable GitHub Pull Request targeting `main`.

- [ ] **Step 1: Run the full local verification**

Run: `python3 -m unittest discover -s tests -v`

Run: `python3 scripts/validate_repository.py`

Run: `python3 scripts/build_release.py --version 3.0.0`

Run: `git diff --check origin/main...HEAD`

Expected: every command exits `0`.

- [ ] **Step 2: Review branch state**

Run: `git status --short --branch`

Run: `git log --oneline origin/main..HEAD`

Expected: clean branch with focused commits and no generated ZIP tracked.

- [ ] **Step 3: Push and open the PR**

Run: `git push -u origin chore/github-optimization`

Run: `gh pr create --repo chen3tu/interview-master-skill --base main --head chore/github-optimization --title "chore: improve repository installation and maintenance" --body "## Summary
- add repository validation and deterministic release packaging
- improve installation and community documentation
- add community health files and CI

## Verification
- python3 -m unittest discover -s tests -v
- python3 scripts/validate_repository.py
- python3 scripts/build_release.py --version 3.0.0"`

Expected: GitHub returns the new PR URL.

- [ ] **Step 4: Verify CI**

Run: `gh pr checks --watch chore/github-optimization --repo chen3tu/interview-master-skill`

Expected: the `Validate` workflow passes.
