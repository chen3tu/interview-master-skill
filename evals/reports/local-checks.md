# Local verification log

2026-10-20; run in the v4 checkout. These are tool checks, not behavioral or host installation tests.

## unittest

```text
test_archive_contains_only_skill_payload (test_build_release.BuildReleaseTests.test_archive_contains_only_skill_payload) ... ok
test_development_and_candidate_files_are_not_packaged (test_build_release.BuildReleaseTests.test_development_and_candidate_files_are_not_packaged) ... ok
test_repeated_builds_have_identical_hashes (test_build_release.BuildReleaseTests.test_repeated_builds_have_identical_hashes) ... ok
test_runtime_dependency_on_repository_document_is_rejected (test_build_release.BuildReleaseTests.test_runtime_dependency_on_repository_document_is_rejected) ... ok
test_symlinked_payload_file_is_rejected (test_build_release.BuildReleaseTests.test_symlinked_payload_file_is_rejected) ... ok
test_broken_markdown_relative_link_is_reported (test_validate_repository.ValidateRepositoryTests.test_broken_markdown_relative_link_is_reported) ... ok
test_documentation_reference_example_is_not_a_runtime_dependency (test_validate_repository.ValidateRepositoryTests.test_documentation_reference_example_is_not_a_runtime_dependency) ... ok
test_existing_file_outside_repository_is_not_runtime_dependency (test_validate_repository.ValidateRepositoryTests.test_existing_file_outside_repository_is_not_runtime_dependency) ... ok
test_malformed_skill_frontmatter_is_reported (test_validate_repository.ValidateRepositoryTests.test_malformed_skill_frontmatter_is_reported) ... ok
test_missing_reference_literal_is_reported (test_validate_repository.ValidateRepositoryTests.test_missing_reference_literal_is_reported) ... ok
test_missing_required_file_is_reported (test_validate_repository.ValidateRepositoryTests.test_missing_required_file_is_reported) ... ok
test_nested_unicode_reference_and_cycle_are_supported (test_validate_repository.ValidateRepositoryTests.test_nested_unicode_reference_and_cycle_are_supported) ... ok
test_orphan_runtime_reference_is_reported (test_validate_repository.ValidateRepositoryTests.test_orphan_runtime_reference_is_reported) ... ok
test_references_replaced_by_file_is_reported (test_validate_repository.ValidateRepositoryTests.test_references_replaced_by_file_is_reported) ... ok
test_required_file_replaced_by_directory_is_reported (test_validate_repository.ValidateRepositoryTests.test_required_file_replaced_by_directory_is_reported) ... ok
test_runtime_reference_cannot_depend_on_unbundled_document (test_validate_repository.ValidateRepositoryTests.test_runtime_reference_cannot_depend_on_unbundled_document) ... ok
test_valid_repository_has_no_errors (test_validate_repository.ValidateRepositoryTests.test_valid_repository_has_no_errors) ... ok

----------------------------------------------------------------------
Ran 17 tests in 0.067s

OK
```

## skill-creator quick_validate

```text
Skill is valid!
```


## Final documentation and artifact check

Repository validation passed; git diff --check returned no errors. All 58 actual output files retained. Final ZIP hash unchanged after documentation updates. Fresh evaluators read the exact 41 payload files in the final ZIP.

## rc.2 final artifact and documentation check

2026-10-20. After the host-neutral runtime change, the 17 unit tests passed again. The final documentation check returned `Repository validation passed.` and `git diff --check` returned no errors. Skill-creator returned `Skill is valid!`.

The rc.2 ZIP remains 64,049 bytes, SHA-256 `466d5b10bf400edbb42ccf17c687b529454f205aa921107931b80b0671342ee2`. Every one of its 41 payload files matches both the final runtime source and the actual Codex project installation byte for byte. A bounded scan of the new host evidence and delivery reports found no local home path, local username or private-key marker. This is not a comprehensive secret-detection guarantee.

Real-host checks are documented separately in [Codex acceptance](codex-acceptance.md): 10 bounded criteria passed in three sessions, seven completed turns and one quota-interrupted initial turn. Environment interruptions and the generated SQL verifier's initial failure remain disclosed.
