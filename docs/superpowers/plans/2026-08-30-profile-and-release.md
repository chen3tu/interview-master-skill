# GitHub Profile and Release Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Improve the `chen3tu` profile and publish Interview Master v3.0.0 through a verified GitHub release.

**Architecture:** Apply repository settings only after the file PR is healthy, create a minimal profile repository without invented personal claims, then merge and publish the exact locally verified ZIP from the merged commit.

**Tech Stack:** Markdown, GitHub CLI, GitHub REST API, Git

**Spec:** `docs/plans/2026-08-30-github-optimization-design.md`

## Global Constraints

- Never expose tokens, email addresses, interview records, or private user data.
- Do not overwrite an existing remote repository, tag, release, branch, or concurrent commit.
- Profile copy may describe only evidence visible in the user's repositories.
- Release only after the Pull Request checks pass and the merged commit is identified.

---

### Task 1: Repository discoverability and security settings

**Files:** None; GitHub repository settings only.

**Interfaces:**
- Produces: topics `claude`, `claude-skills`, `interview`, `career`, `job-search`, `prompt-engineering`.
- Produces: enabled Discussions and Dependabot security updates.

- [ ] **Step 1: Re-read current settings**

Run: `gh api repos/chen3tu/interview-master-skill`

Expected: the viewer has admin permission and the repository is public.

- [ ] **Step 2: Apply metadata**

Run `gh repo edit` with the six topics, the existing description, Issues enabled, and Discussions enabled.

- [ ] **Step 3: Enable automated security fixes**

Run: `gh api --method PUT repos/chen3tu/interview-master-skill/automated-security-fixes`

- [ ] **Step 4: Verify settings**

Query the repository and automated-security-fixes endpoints; confirm topics, Discussions, secret scanning, push protection, and automated security fixes.

### Task 2: Profile README repository

**Files:**
- Create in a new local checkout: `README.md`

**Interfaces:**
- Produces: public profile repository `chen3tu/chen3tu` with a focused README.

- [ ] **Step 1: Confirm the repository is absent**

Run: `gh repo view chen3tu/chen3tu`

Expected: not found. If it exists, clone and inspect it instead of creating or overwriting.

- [ ] **Step 2: Create local README content**

Include the display name `chen333tu`, a concise focus on practical AI Skills and structured career workflows, a featured-project card for Interview Master, its 70+ Star signal without hard-coding an exact mutable count in prose, and links to repositories. Do not add unverified employer, location, contact, or expertise claims.

- [ ] **Step 3: Create and push the profile repository**

Initialize a local Git repository, commit `README.md`, create the remote with `gh repo create chen3tu/chen3tu --public --source . --remote origin --push`, and verify the rendered README through `gh repo view`.

### Task 3: Merge and v3.0.0 release

**Files:** None beyond the verified release artifact in `dist/`.

**Interfaces:**
- Consumes: passing PR, generated ZIP, and `CHANGELOG.md` v3.0.0 section.
- Produces: merged PR, annotated `v3.0.0` tag, GitHub Release, and ZIP asset.

- [ ] **Step 1: Reconfirm collision-free release state**

Run: `gh release view v3.0.0 --repo chen3tu/interview-master-skill`

Run: `git ls-remote --tags origin refs/tags/v3.0.0`

Expected: neither a release nor tag exists.

- [ ] **Step 2: Merge the healthy Pull Request**

Run: `gh pr merge chore/github-optimization --repo chen3tu/interview-master-skill --squash --delete-branch`

Expected: the PR reports merged and the remote feature branch is deleted.

- [ ] **Step 3: Build from the merged commit**

Update local `main` by fast-forward, rerun unit tests and repository validation, then run `python3 scripts/build_release.py --version 3.0.0`. Record the ZIP SHA-256 digest.

- [ ] **Step 4: Publish the release**

Create `v3.0.0` from the merged commit with release notes based on the existing CHANGELOG section and upload `dist/interview-master-v3.0.0.zip` using `gh release create`.

- [ ] **Step 5: Verify public release**

Run: `gh release view v3.0.0 --repo chen3tu/interview-master-skill --json tagName,isDraft,isPrerelease,assets,url`

Expected: a published non-prerelease release with one ZIP asset matching the locally recorded filename and digest after download.
