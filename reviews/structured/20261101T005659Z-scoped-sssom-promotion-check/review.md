# Scoped SSSOM correction and whole-candidate promotion decision

- Review: 20261101T005659Z-scoped-sssom-promotion-check
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-11-01T00:55:43.660755Z
- Finished UTC: 2026-11-01T00:56:59Z
- Reviewer: Codex /root (not_applicable)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: false

## Summary

Canonical 2,987 rows: nine changed, none added/removed. Ready diagnostic 2,980 rows: zero native rejects. Supported/withheld partition is 1,740/1,247; no approval is inferred from structural validation.

## Scope And Provenance

All rows of two exact SSSOM artifacts, checked mechanically; source-specific science is documented in separate native reviews.

Selection: Maintained canonical and safe-scope ready candidate only. The earlier final.sssom.tsv is a blocked-proposal artifact and excluded from this final assessment.
Coverage: full; 2 reviewed / 2 in the declared population.
Source: working_tree at Git base 4625afd492b6cf43e3b499d1425d2453d490009d.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| canonical | mappings/ingredient_mappings.sssom.tsv | generated | Scoped canonical correction, 2987 rows |
| candidate | output/sssom-scientific-audit/ready.sssom.tsv | generated | Safe-scope raw diagnostic candidate, 2980 rows; not promoted wholesale |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| ready generation | passed | True | candidate | Merged Claw d8f95e7 generated the safe-scope 2,980-row diagnostic candidate. |
| full qc ready | passed | True | canonical | Full native just qc passes after the blocked melezitose proposal was excluded. |
| ready candidate invariants | passed | True | candidate | Strict native invariants pass with zero reject rows; Rule K baseline allowances remain explicit. |
| ready candidate schema | passed | True | candidate | SSSOM JSON Schema, prefix completeness and strict CURIE validation pass. |
| ready candidate curie | passed | True | candidate | All 5,960 candidate CURIEs pass native syntax/prefix checks. |
| ready candidate products | passed | True | candidate | Native label policy reports zero flagged pairs, with configured no-adapter skips retained. |
| ready candidate b4 | passed | True | candidate | Native B4 finds no mismatches against actual read-only KG transforms; BTO/MICRO transforms unavailable. |
| ready source b4 | passed | True | canonical | Actual-directory B4 finds no canonical mismatches; same native missing-transform/absent-ID limits. |
| ready products | passed | True | canonical | Native configured product-label validation passes, retaining nonblocking warnings and adapter skips. |
| ready source reconcile | passed | True | canonical | No GAP, ORPHAN, STALE, predicate or grade drift. |
| ready source curie | passed | True | canonical | All 5,974 canonical CURIEs pass native syntax/prefix checks. |
| ready reviewed export | passed | True | canonical | Native release reproduces 1,740 supported and 1,247 withheld rows. |
| ready reviewed validate | passed | True | canonical | Native reviewed-release integrity and SSSOM validators pass. |
| canonical change audit | passed | True | canonical | Nine existing rows change; positions and 2,978 other rows preserved; one prior approval withdrawn. |
| ready promotion audit | passed | True | canonical, candidate | Every full-candidate row delta is inventoried; broad replacement is declined. |
| ready regressions | passed | True | canonical | 165 focused correction, receipt, invariant and reviewed-release tests pass on the final maintained scripts. |
| final correction lint retry | passed | True | canonical | Final maintained correction scripts, helper and tests pass Ruff. |
| merged generator tests | passed | True | candidate | 84 merged-generator identity/date/synonym regression tests pass. |

## Scientific And Domain Assessments

### Scoped canonical output preserves unrelated work

consistency: supported. Targets: canonical.

Only two carnitine rows and seven independently adjudicated alias cells change. The amide name is rejected in its sole YAML owner; the deferred DL-carnitine alias remains. All existing positions and 2,978 other row payloads survive.

### Safe-scope diagnostic output is mechanically valid

consistency: supported. Targets: candidate.

The ready candidate contains 2,980 rows, zero native invariant rejects and zero source reconciliation drift. Configured label skips and B4 missing-source limits remain; this result is not scientific approval.

### No wholesale replacement or inherited scientific approval

scope: supported. Targets: canonical, candidate.

Full replacement is declined: it would rewrite 2,364 payloads, drop ten rows and add three, including 1,329 currently supported payloads. The narrow correction uses the native receipt chain, withdraws one stale owner approval and preserves the remaining scientific backlog.

### Dependencies and protected surfaces remain intact

provenance: supported. Targets: canonical, candidate.

Melezitose and the protected workflow, unified mapping and cycle profile remain byte-identical to base. The proposed melezitose correction is archived as blocked on PR764. No shared Claw checkout mutation, bulk CultureMech import, paid provider call, cycle advance or supervisor binding is claimed.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ready_generation | reports/sssom_scientific_curation_20261101/generation/logs/ready_generation.log | supports | Merged Claw d8f95e7 generated the safe-scope 2,980-row diagnostic candidate. |
| full_qc_ready | reports/sssom_scientific_curation_20261101/generation/logs/full_qc_ready.log | supports | Full native just qc passes after the blocked melezitose proposal was excluded. |
| ready_candidate_invariants | reports/sssom_scientific_curation_20261101/generation/logs/ready_candidate_invariants.log | supports | Strict native invariants pass with zero reject rows; Rule K baseline allowances remain explicit. |
| ready_candidate_schema | reports/sssom_scientific_curation_20261101/generation/logs/ready_candidate_schema.log | supports | SSSOM JSON Schema, prefix completeness and strict CURIE validation pass. |
| ready_candidate_curie | reports/sssom_scientific_curation_20261101/generation/logs/ready_candidate_curie.log | supports | All 5,960 candidate CURIEs pass native syntax/prefix checks. |
| ready_candidate_products | reports/sssom_scientific_curation_20261101/generation/logs/ready_candidate_products.log | supports | Native label policy reports zero flagged pairs, with configured no-adapter skips retained. |
| ready_candidate_b4 | reports/sssom_scientific_curation_20261101/generation/logs/ready_candidate_b4.log | supports | Native B4 finds no mismatches against actual read-only KG transforms; BTO/MICRO transforms unavailable. |
| ready_source_b4 | reports/sssom_scientific_curation_20261101/generation/logs/ready_source_b4.log | supports | Actual-directory B4 finds no canonical mismatches; same native missing-transform/absent-ID limits. |
| ready_products | reports/sssom_scientific_curation_20261101/generation/logs/ready_products.log | supports | Native configured product-label validation passes, retaining nonblocking warnings and adapter skips. |
| ready_source_reconcile | reports/sssom_scientific_curation_20261101/generation/logs/ready_source_reconcile.log | supports | No GAP, ORPHAN, STALE, predicate or grade drift. |
| ready_source_curie | reports/sssom_scientific_curation_20261101/generation/logs/ready_source_curie.log | supports | All 5,974 canonical CURIEs pass native syntax/prefix checks. |
| ready_reviewed_export | reports/sssom_scientific_curation_20261101/generation/logs/ready_reviewed_export.log | supports | Native release reproduces 1,740 supported and 1,247 withheld rows. |
| ready_reviewed_validate | reports/sssom_scientific_curation_20261101/generation/logs/ready_reviewed_validate.log | supports | Native reviewed-release integrity and SSSOM validators pass. |
| canonical_change_audit | reports/sssom_scientific_curation_20261101/generation/logs/canonical_change_audit.log | supports | Nine existing rows change; positions and 2,978 other rows preserved; one prior approval withdrawn. |
| ready_promotion_audit | reports/sssom_scientific_curation_20261101/generation/logs/ready_promotion_audit.log | supports | Every full-candidate row delta is inventoried; broad replacement is declined. |
| ready_regressions | reports/sssom_scientific_curation_20261101/generation/logs/ready_regressions.log | supports | 165 focused correction, receipt, invariant and reviewed-release tests pass on the final maintained scripts. |
| final_correction_lint_retry | reports/sssom_scientific_curation_20261101/generation/logs/final_correction_lint_retry.log | supports | Final maintained correction scripts, helper and tests pass Ruff. |
| merged_generator_tests | reports/sssom_scientific_curation_20261101/generation/logs/merged_generator_tests.log | supports | 84 merged-generator identity/date/synonym regression tests pass. |
| inputs | reports/sssom_scientific_curation_20261101/generation/validation-inputs.json | supports | Exact current revisions and file hashes; KG and CultureMech are read-only comparison/input sources. |
| generation | reports/sssom_scientific_curation_20261101/generation/generation-receipt.json | supports | Standalone execution, isolated merged generator, separate baseline/blocked/ready artifacts and prior-stamp snapshots. |
| delta | reports/sssom_scientific_curation_20261101/generation/canonical-row-change-summary.json | supports | Full nine-row field deltas and prior/current release-boundary checks. |
| promotion | reports/sssom_scientific_curation_20261101/generation/ready-promotion-summary.json | supports | 2,364 changed, ten removed and three added candidate rows; 1,329 currently supported row payloads would change. |
| row-deltas | reports/sssom_scientific_curation_20261101/generation/ready-promotion-row-delta.json | supports | Every changed field, added row and removed row for the rejected whole-candidate replacement. |
| receipt | reports/sssom_completion_20260921/mapping_changes/issue669-1003-scoped-alias-corrections.json | supports | Eight owners, nine row changes, no additions/removals and no scientific approval carry. |
| subject-limits | reports/sssom_scientific_curation_20261101/generation/logs/ready_source_subjects.log | supports | Eighteen preexisting non-gating opaque-subject filename warnings; no new subject-identity ruling. |
| semantics | MAPPING_SEMANTICS.md | supports | Identity, predicate, registry and synonym contract. |

## Limits And Additional Notes

- Deterministic checks do not establish every chemical identity or publishable synonym. Rule K retains 38 explicit obligations.
- Native semantic integrity passes while scientific release remains FAIL: 1,733 blocking findings and 2,272 assertions, one more assertion after withdrawing a stale approval.
- B4 skips missing BTO/MICRO transforms and absent IDs; native product adapters also have explicit skips and nonblocking warnings.
- 18 opaque-subject filename warnings remain non-gating under the undecided subject contract.
- The complete diagnostic candidate and large external inputs remain local. Hashes, exact original paths and every candidate row delta are published.
- Earlier failed setup attempts, the blocked melezitose release attempt, and superseded intermediate validations remain diagnostic evidence, not final gate passes.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261101T005659Z-scoped-sssom-promotion-check
kind: repository
repository: CultureBotAI/MediaIngredientMech
title: Scoped SSSOM correction and whole-candidate promotion decision
started_at: '2026-11-01T00:55:43.660755Z'
finished_at: '2026-11-01T00:56:59Z'
reviewer:
  identity: Codex /root
  kind: agent
  independence: not_applicable
  independence_basis: Implementation coordinator; this is a mechanical author assessment.
    A separate agent reviews the final commit independently.
skill: .claude/skills/review-sssom-output/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: false
native_verdict: Mechanical gates pass; narrow correction only; full raw promotion
  declined; scientific release remains FAIL
summary: 'Canonical 2,987 rows: nine changed, none added/removed. Ready diagnostic
  2,980 rows: zero native rejects. Supported/withheld partition is 1,740/1,247; no
  approval is inferred from structural validation.'
source:
  git_revision: 4625afd492b6cf43e3b499d1425d2453d490009d
  state: working_tree
  inputs:
  - path: .github/workflows/qc-evidence.yaml
    sha256: 5814a583a571b3e622a493942dd5483656c7d69531485e560db7c8075e1d7751
    role: context
  - path: MAPPING_SEMANTICS.md
    sha256: 94aad13ea0fc3df82a37383f388f41432b607b04cac61ae5792ce1a381aef805
    role: context
  - path: data/curated/mapped_ingredients.yaml
    sha256: 56e9eae4e0dd282e9c5a5d6d8c972faa99ddda76127bb26a9df5f5934abce09d
    role: context
  - path: mappings/ingredient_mappings.sssom.tsv
    sha256: f408f36b9de77c2089a07907b40d6a27401087e13528f0597a6cf7b386048ac0
    role: target
  - path: mappings/other_cross_record_baseline.tsv
    sha256: 170368983e4105773348122d44da5417745e675dfa9151f72270f19da7a26008
    role: context
  - path: output/sssom-scientific-audit/ready.sssom.tsv
    sha256: 084fd8cfc300272a0dcb220ebc1ca2076aee83229e3847cf64e0c1ca1c37359b
    role: target
  - path: reports/sssom_completion_20260921/mapping_changes/issue669-1003-scoped-alias-corrections.json
    sha256: 00049aa1d2b19565020d4ecbec999fc723d2cf5954968ec6bf5cebdc0da73f34
    role: context
  - path: reports/sssom_completion_20260921/review.json
    sha256: 0cc2c8742f905458ebb15ed0195aa0744662f29d6019bad03690f8095904ac40
    role: context
  - path: src/mediaingredientmech/schema/mediaingredientmech.yaml
    sha256: bb43dee29b21fdee72a48022456e733e49e95824c4c09674f9b3165c290fe012
    role: context
  - path: workflow/mech-workflow.yaml
    sha256: 45d7c23d67f490cea6b31e336e5d2ac98b7ce8fa4e791bd9d3be092cfdb5a10d
    role: context
targets:
- target_id: canonical
  path: mappings/ingredient_mappings.sssom.tsv
  label: Scoped canonical correction, 2987 rows
  kind: generated
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/curated/mapped_ingredients.yaml
    role: Maintained source records; one guarded synonym correction
  - repository: CultureBotAI/MediaIngredientMech
    path: scripts/retire_reviewed_generated_aliases.py
    role: Guarded seven-token retirement, retaining every other row field
  - repository: CultureBotAI/culturebotai-claw
    path: scripts/build_mim_ingredient_sssom.py
    role: Merged d8f95e7 generator, isolated copy
- target_id: candidate
  path: output/sssom-scientific-audit/ready.sssom.tsv
  label: Safe-scope raw diagnostic candidate, 2980 rows; not promoted wholesale
  kind: generated
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/curated/mapped_ingredients.yaml
    role: Maintained source records after excluding the blocked melezitose proposal
  - repository: CultureBotAI/culturebotai-claw
    path: scripts/build_mim_ingredient_sssom.py
    role: Merged d8f95e7 generator, isolated copy
scope:
  description: All rows of two exact SSSOM artifacts, checked mechanically; source-specific
    science is documented in separate native reviews.
  selection: Maintained canonical and safe-scope ready candidate only. The earlier
    final.sssom.tsv is a blocked-proposal artifact and excluded from this final assessment.
  coverage: full
  population_size: 2
  reviewed_target_ids:
  - canonical
  - candidate
  exclusions:
  - target: Corpus-wide scientific identity, roles and components
    reason: Existing scientific holds and the 1,733-finding backlog remain.
  - target: Melezitose and sodium-perchlorate correction application
    reason: PR764 is required to supersede existing content-bound approvals safely.
  - target: Unified mapping rebuild and Cycle12
    reason: Owned by other open PRs; protected artifacts remain unchanged.
checks:
- check_id: ready_generation
  name: ready generation
  status: passed
  required: true
  summary: Merged Claw d8f95e7 generated the safe-scope 2,980-row diagnostic candidate.
  target_ids:
  - candidate
  evidence_ids:
  - ready_generation
  exit_code: 0
  expected_exit_code: 0
  command: cd /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/output/sssom-curation-20261101T003435Z/claw
    && uv run python ../locked_generation.py ready
  scope_note: Exact run and original evidence path retained in the adjacent command
    receipt.
- check_id: full_qc_ready
  name: full qc ready
  status: passed
  required: true
  summary: Full native just qc passes after the blocked melezitose proposal was excluded.
  target_ids:
  - canonical
  evidence_ids:
  - full_qc_ready
  exit_code: 0
  expected_exit_code: 0
  command: cd /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/output/sssom-curation-20261101T003435Z/mim
    && just qc
  scope_note: Exact run and original evidence path retained in the adjacent command
    receipt.
- check_id: ready_candidate_invariants
  name: ready candidate invariants
  status: passed
  required: true
  summary: Strict native invariants pass with zero reject rows; Rule K baseline allowances
    remain explicit.
  target_ids:
  - candidate
  evidence_ids:
  - ready_candidate_invariants
  exit_code: 0
  expected_exit_code: 0
  command: cd /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/output/sssom-curation-20261101T003435Z/mim
    && uv run python scripts/validate_sssom_invariants.py output/sssom-scientific-audit/ready.sssom.tsv
    --reject-tsv output/sssom-scientific-audit/ready-rejects.tsv
  scope_note: Exact run and original evidence path retained in the adjacent command
    receipt.
- check_id: ready_candidate_schema
  name: ready candidate schema
  status: passed
  required: true
  summary: SSSOM JSON Schema, prefix completeness and strict CURIE validation pass.
  target_ids:
  - candidate
  evidence_ids:
  - ready_candidate_schema
  exit_code: 0
  expected_exit_code: 0
  command: cd /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/output/sssom-curation-20261101T003435Z/mim
    && sssom validate -V JsonSchema -V PrefixMapCompleteness -V StrictCurieFormat
    output/sssom-scientific-audit/ready.sssom.tsv
  scope_note: Exact run and original evidence path retained in the adjacent command
    receipt.
- check_id: ready_candidate_curie
  name: ready candidate curie
  status: passed
  required: true
  summary: All 5,960 candidate CURIEs pass native syntax/prefix checks.
  target_ids:
  - candidate
  evidence_ids:
  - ready_candidate_curie
  exit_code: 0
  expected_exit_code: 0
  command: cd /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/output/sssom-curation-20261101T003435Z/mim
    && uv run python scripts/validate_published_curies.py output/sssom-scientific-audit/ready.sssom.tsv
  scope_note: Exact run and original evidence path retained in the adjacent command
    receipt.
- check_id: ready_candidate_products
  name: ready candidate products
  status: passed
  required: true
  summary: Native label policy reports zero flagged pairs, with configured no-adapter
    skips retained.
  target_ids:
  - candidate
  evidence_ids:
  - ready_candidate_products
  exit_code: 0
  expected_exit_code: 0
  command: cd /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/output/sssom-curation-20261101T003435Z/mim
    && uv run python scripts/validate_id_label_correspondence.py --config ../provenance/ready-candidate-id-label-config.yaml
    --report ../provenance/ready-candidate-label-drift.tsv
  scope_note: Exact run and original evidence path retained in the adjacent command
    receipt.
- check_id: ready_candidate_b4
  name: ready candidate b4
  status: passed
  required: true
  summary: Native B4 finds no mismatches against actual read-only KG transforms; BTO/MICRO
    transforms unavailable.
  target_ids:
  - candidate
  evidence_ids:
  - ready_candidate_b4
  exit_code: 0
  expected_exit_code: 0
  command: cd /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/output/sssom-curation-20261101T003435Z/mim
    && uv run python ../check_b4_actual.py output/sssom-scientific-audit/ready.sssom.tsv
    ready-candidate
  scope_note: Exact run and original evidence path retained in the adjacent command
    receipt.
- check_id: ready_source_b4
  name: ready source b4
  status: passed
  required: true
  summary: Actual-directory B4 finds no canonical mismatches; same native missing-transform/absent-ID
    limits.
  target_ids:
  - canonical
  evidence_ids:
  - ready_source_b4
  exit_code: 0
  expected_exit_code: 0
  command: cd /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/output/sssom-curation-20261101T003435Z/mim
    && uv run python ../check_b4_actual.py mappings/ingredient_mappings.sssom.tsv
    ready-source
  scope_note: Exact run and original evidence path retained in the adjacent command
    receipt.
- check_id: ready_products
  name: ready products
  status: passed
  required: true
  summary: Native configured product-label validation passes, retaining nonblocking
    warnings and adapter skips.
  target_ids:
  - canonical
  evidence_ids:
  - ready_products
  exit_code: 0
  expected_exit_code: 0
  command: cd /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/output/sssom-curation-20261101T003435Z/mim
    && just validate-products
  scope_note: Exact run and original evidence path retained in the adjacent command
    receipt.
- check_id: ready_source_reconcile
  name: ready source reconcile
  status: passed
  required: true
  summary: No GAP, ORPHAN, STALE, predicate or grade drift.
  target_ids:
  - canonical
  evidence_ids:
  - ready_source_reconcile
  exit_code: 0
  expected_exit_code: 0
  command: cd /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/output/sssom-curation-20261101T003435Z/mim
    && uv run python scripts/reconcile_sssom.py
  scope_note: Exact run and original evidence path retained in the adjacent command
    receipt.
- check_id: ready_source_curie
  name: ready source curie
  status: passed
  required: true
  summary: All 5,974 canonical CURIEs pass native syntax/prefix checks.
  target_ids:
  - canonical
  evidence_ids:
  - ready_source_curie
  exit_code: 0
  expected_exit_code: 0
  command: cd /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/output/sssom-curation-20261101T003435Z/mim
    && uv run python scripts/validate_published_curies.py
  scope_note: Exact run and original evidence path retained in the adjacent command
    receipt.
- check_id: ready_reviewed_export
  name: ready reviewed export
  status: passed
  required: true
  summary: Native release reproduces 1,740 supported and 1,247 withheld rows.
  target_ids:
  - canonical
  evidence_ids:
  - ready_reviewed_export
  exit_code: 0
  expected_exit_code: 0
  command: cd /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/output/sssom-curation-20261101T003435Z/mim
    && just export-reviewed-sssom
  scope_note: Exact run and original evidence path retained in the adjacent command
    receipt.
- check_id: ready_reviewed_validate
  name: ready reviewed validate
  status: passed
  required: true
  summary: Native reviewed-release integrity and SSSOM validators pass.
  target_ids:
  - canonical
  evidence_ids:
  - ready_reviewed_validate
  exit_code: 0
  expected_exit_code: 0
  command: cd /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/output/sssom-curation-20261101T003435Z/mim
    && just qc-reviewed-sssom
  scope_note: Exact run and original evidence path retained in the adjacent command
    receipt.
- check_id: canonical_change_audit
  name: canonical change audit
  status: passed
  required: true
  summary: Nine existing rows change; positions and 2,978 other rows preserved; one
    prior approval withdrawn.
  target_ids:
  - canonical
  evidence_ids:
  - canonical_change_audit
  exit_code: 0
  expected_exit_code: 0
  command: cd /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/output/sssom-curation-20261101T003435Z/mim
    && uv run python ../summarize_canonical_changes.py
  scope_note: Exact run and original evidence path retained in the adjacent command
    receipt.
- check_id: ready_promotion_audit
  name: ready promotion audit
  status: passed
  required: true
  summary: Every full-candidate row delta is inventoried; broad replacement is declined.
  target_ids:
  - canonical
  - candidate
  evidence_ids:
  - ready_promotion_audit
  exit_code: 0
  expected_exit_code: 0
  command: cd /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/output/sssom-curation-20261101T003435Z/mim
    && uv run python ../compare_promotion.py ready
  scope_note: Exact run and original evidence path retained in the adjacent command
    receipt.
- check_id: ready_regressions
  name: ready regressions
  status: passed
  required: true
  summary: 165 focused correction, receipt, invariant and reviewed-release tests pass
    on the final maintained scripts.
  target_ids:
  - canonical
  evidence_ids:
  - ready_regressions
  exit_code: 0
  expected_exit_code: 0
  command: cd /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/output/sssom-curation-20261101T003435Z/mim
    && uv run python -m pytest -q -o addopts= tests/test_reject_carnitinamide_synonym.py
    tests/test_retire_reviewed_generated_aliases.py tests/test_curation_receipt_collisions.py
    tests/test_mapping_change_receipt.py tests/test_sssom_pinned_invariants.py tests/test_sssom_other_cross_record.py
    tests/test_reviewed_sssom.py
  scope_note: Exact run and original evidence path retained in the adjacent command
    receipt.
- check_id: final_correction_lint_retry
  name: final correction lint retry
  status: passed
  required: true
  summary: Final maintained correction scripts, helper and tests pass Ruff.
  target_ids:
  - canonical
  evidence_ids:
  - final_correction_lint_retry
  exit_code: 0
  expected_exit_code: 0
  command: cd /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/output/sssom-curation-20261101T003435Z/mim
    && uvx ruff check scripts/reject_carnitinamide_synonym.py scripts/retire_reviewed_generated_aliases.py
    src/mediaingredientmech/curate/apply_receipt.py tests/test_reject_carnitinamide_synonym.py
    tests/test_retire_reviewed_generated_aliases.py tests/test_curation_receipt_collisions.py
  scope_note: Exact run and original evidence path retained in the adjacent command
    receipt.
- check_id: merged_generator_tests
  name: merged generator tests
  status: passed
  required: true
  summary: 84 merged-generator identity/date/synonym regression tests pass.
  target_ids:
  - candidate
  evidence_ids:
  - merged_generator_tests
  exit_code: 0
  expected_exit_code: 0
  command: cd /Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/output/sssom-curation-20261101T003435Z/claw
    && uv run python -m pytest -q --no-cov tests/test_sssom_identity_row.py tests/test_mim_synonym_scope.py
    tests/test_mim_sssom_header_dates.py tests/test_mapping_date.py
  scope_note: Exact run and original evidence path retained in the adjacent command
    receipt.
evidence:
- evidence_id: ready_generation
  kind: validation
  reference: reports/sssom_scientific_curation_20261101/generation/logs/ready_generation.log
  accessed_at: '2026-11-01T00:56:59Z'
  support: supports
  summary: Merged Claw d8f95e7 generated the safe-scope 2,980-row diagnostic candidate.
  snapshot_sha256: 53626cb4bd5b4ee0d1f9f3c765699a715c547b9ef86d6d690db54e0cbe063aa2
- evidence_id: full_qc_ready
  kind: validation
  reference: reports/sssom_scientific_curation_20261101/generation/logs/full_qc_ready.log
  accessed_at: '2026-11-01T00:56:59Z'
  support: supports
  summary: Full native just qc passes after the blocked melezitose proposal was excluded.
  snapshot_sha256: fd65fac9a3664cd17b8c5638dd2fd5ecf5e9f2a02c3b526099ee04a4e0fea49d
- evidence_id: ready_candidate_invariants
  kind: validation
  reference: reports/sssom_scientific_curation_20261101/generation/logs/ready_candidate_invariants.log
  accessed_at: '2026-11-01T00:56:59Z'
  support: supports
  summary: Strict native invariants pass with zero reject rows; Rule K baseline allowances
    remain explicit.
  snapshot_sha256: da6fb30dd91cf258d99add2860792fb92437f729b0fc5ffb72e54d0576eabe1a
- evidence_id: ready_candidate_schema
  kind: validation
  reference: reports/sssom_scientific_curation_20261101/generation/logs/ready_candidate_schema.log
  accessed_at: '2026-11-01T00:56:59Z'
  support: supports
  summary: SSSOM JSON Schema, prefix completeness and strict CURIE validation pass.
  snapshot_sha256: 6bb3a5fb4906f5382c09aa0eb0a8e6dbe45d2fe31c6dd726e030e30461fa4c2c
- evidence_id: ready_candidate_curie
  kind: validation
  reference: reports/sssom_scientific_curation_20261101/generation/logs/ready_candidate_curie.log
  accessed_at: '2026-11-01T00:56:59Z'
  support: supports
  summary: All 5,960 candidate CURIEs pass native syntax/prefix checks.
  snapshot_sha256: 33ac57376b5f63e4655c552ef55509d9e59976da881b77b2de784423308ed4c2
- evidence_id: ready_candidate_products
  kind: validation
  reference: reports/sssom_scientific_curation_20261101/generation/logs/ready_candidate_products.log
  accessed_at: '2026-11-01T00:56:59Z'
  support: supports
  summary: Native label policy reports zero flagged pairs, with configured no-adapter
    skips retained.
  snapshot_sha256: a995467de1a2f84846b87033a72040cdf52eff7455119ca3737efb7affbd2708
- evidence_id: ready_candidate_b4
  kind: validation
  reference: reports/sssom_scientific_curation_20261101/generation/logs/ready_candidate_b4.log
  accessed_at: '2026-11-01T00:56:59Z'
  support: supports
  summary: Native B4 finds no mismatches against actual read-only KG transforms; BTO/MICRO
    transforms unavailable.
  snapshot_sha256: 6efa5e7fee08c51f8b088780ae9d41c320e9ee91b79a3e310abd9d3f9f31df84
- evidence_id: ready_source_b4
  kind: validation
  reference: reports/sssom_scientific_curation_20261101/generation/logs/ready_source_b4.log
  accessed_at: '2026-11-01T00:56:59Z'
  support: supports
  summary: Actual-directory B4 finds no canonical mismatches; same native missing-transform/absent-ID
    limits.
  snapshot_sha256: 97ceab9f50979d6616921cec60efb1bc9056028bdf889b0dfe1abadc0ff8919a
- evidence_id: ready_products
  kind: validation
  reference: reports/sssom_scientific_curation_20261101/generation/logs/ready_products.log
  accessed_at: '2026-11-01T00:56:59Z'
  support: supports
  summary: Native configured product-label validation passes, retaining nonblocking
    warnings and adapter skips.
  snapshot_sha256: 1fa143fbbbdb204cfca441d722014ca3b2ab5eda915eb2f6de1b7dc997e1d335
- evidence_id: ready_source_reconcile
  kind: validation
  reference: reports/sssom_scientific_curation_20261101/generation/logs/ready_source_reconcile.log
  accessed_at: '2026-11-01T00:56:59Z'
  support: supports
  summary: No GAP, ORPHAN, STALE, predicate or grade drift.
  snapshot_sha256: 8bf18010d973e92de327bf8580964cbe3306206d7191c45a7b1731df9c7d61d7
- evidence_id: ready_source_curie
  kind: validation
  reference: reports/sssom_scientific_curation_20261101/generation/logs/ready_source_curie.log
  accessed_at: '2026-11-01T00:56:59Z'
  support: supports
  summary: All 5,974 canonical CURIEs pass native syntax/prefix checks.
  snapshot_sha256: 495b73a329d03edf71a3f67887a247da739c31cf2f9189d0215da04b950b0637
- evidence_id: ready_reviewed_export
  kind: validation
  reference: reports/sssom_scientific_curation_20261101/generation/logs/ready_reviewed_export.log
  accessed_at: '2026-11-01T00:56:59Z'
  support: supports
  summary: Native release reproduces 1,740 supported and 1,247 withheld rows.
  snapshot_sha256: f602b192fb439927282aa9896a4ed4f72cf437f701fecc1ed47e4c96793ab736
- evidence_id: ready_reviewed_validate
  kind: validation
  reference: reports/sssom_scientific_curation_20261101/generation/logs/ready_reviewed_validate.log
  accessed_at: '2026-11-01T00:56:59Z'
  support: supports
  summary: Native reviewed-release integrity and SSSOM validators pass.
  snapshot_sha256: 345855c3c8874bb9b593266acf3545eb085f12e24cca71edb1129c0b865ce4da
- evidence_id: canonical_change_audit
  kind: validation
  reference: reports/sssom_scientific_curation_20261101/generation/logs/canonical_change_audit.log
  accessed_at: '2026-11-01T00:56:59Z'
  support: supports
  summary: Nine existing rows change; positions and 2,978 other rows preserved; one
    prior approval withdrawn.
  snapshot_sha256: 185fcd1ea84f34a3211a60d5c72655dedf8d45f41cd0fa145bbf681da157eea5
- evidence_id: ready_promotion_audit
  kind: validation
  reference: reports/sssom_scientific_curation_20261101/generation/logs/ready_promotion_audit.log
  accessed_at: '2026-11-01T00:56:59Z'
  support: supports
  summary: Every full-candidate row delta is inventoried; broad replacement is declined.
  snapshot_sha256: 36028fce7c9ef231e07bd0fd1d313c7806bce174fdb50c7c9afd69103052cf09
- evidence_id: ready_regressions
  kind: validation
  reference: reports/sssom_scientific_curation_20261101/generation/logs/ready_regressions.log
  accessed_at: '2026-11-01T00:56:59Z'
  support: supports
  summary: 165 focused correction, receipt, invariant and reviewed-release tests pass
    on the final maintained scripts.
  snapshot_sha256: 2a6065129b4e252b8242c63ec16142290e850e4b0dcd0fe1a99405e3112928ac
- evidence_id: final_correction_lint_retry
  kind: validation
  reference: reports/sssom_scientific_curation_20261101/generation/logs/final_correction_lint_retry.log
  accessed_at: '2026-11-01T00:56:59Z'
  support: supports
  summary: Final maintained correction scripts, helper and tests pass Ruff.
  snapshot_sha256: 82b3e6a6c090a57601d22943bd23fca9218d1031dbe5a7b754092f9a156b4f18
- evidence_id: merged_generator_tests
  kind: validation
  reference: reports/sssom_scientific_curation_20261101/generation/logs/merged_generator_tests.log
  accessed_at: '2026-11-01T00:56:59Z'
  support: supports
  summary: 84 merged-generator identity/date/synonym regression tests pass.
  snapshot_sha256: cabe2feeb68a1ea765a124bc61004f15a9ecde65cb279c316e71a2ccccb9e2a9
- evidence_id: inputs
  kind: record_content
  reference: reports/sssom_scientific_curation_20261101/generation/validation-inputs.json
  accessed_at: '2026-11-01T00:56:59Z'
  support: supports
  summary: Exact current revisions and file hashes; KG and CultureMech are read-only
    comparison/input sources.
  snapshot_sha256: 1bc0b000953cc8077cb7a96cfe929964c7ed1dd93200029ab9ab129cc926718f
- evidence_id: generation
  kind: record_content
  reference: reports/sssom_scientific_curation_20261101/generation/generation-receipt.json
  accessed_at: '2026-11-01T00:56:59Z'
  support: supports
  summary: Standalone execution, isolated merged generator, separate baseline/blocked/ready
    artifacts and prior-stamp snapshots.
  snapshot_sha256: 3b4d14bb6fb0011595a8606435a8b9065fc56509f62baf35a6406e06fbfbde96
- evidence_id: delta
  kind: record_content
  reference: reports/sssom_scientific_curation_20261101/generation/canonical-row-change-summary.json
  accessed_at: '2026-11-01T00:56:59Z'
  support: supports
  summary: Full nine-row field deltas and prior/current release-boundary checks.
  snapshot_sha256: fb1c9d73e08194b964a73c1014828d90c4ac42c2b7a484711bdc243f2addf5d6
- evidence_id: promotion
  kind: record_content
  reference: reports/sssom_scientific_curation_20261101/generation/ready-promotion-summary.json
  accessed_at: '2026-11-01T00:56:59Z'
  support: supports
  summary: 2,364 changed, ten removed and three added candidate rows; 1,329 currently
    supported row payloads would change.
  snapshot_sha256: 36028fce7c9ef231e07bd0fd1d313c7806bce174fdb50c7c9afd69103052cf09
- evidence_id: row-deltas
  kind: record_content
  reference: reports/sssom_scientific_curation_20261101/generation/ready-promotion-row-delta.json
  accessed_at: '2026-11-01T00:56:59Z'
  support: supports
  summary: Every changed field, added row and removed row for the rejected whole-candidate
    replacement.
  snapshot_sha256: adbce1efb4812d77ce41fc3a2296d228b455a572572deb5ef89e391c22061d0a
- evidence_id: receipt
  kind: record_content
  reference: reports/sssom_completion_20260921/mapping_changes/issue669-1003-scoped-alias-corrections.json
  accessed_at: '2026-11-01T00:56:59Z'
  support: supports
  summary: Eight owners, nine row changes, no additions/removals and no scientific
    approval carry.
  snapshot_sha256: 00049aa1d2b19565020d4ecbec999fc723d2cf5954968ec6bf5cebdc0da73f34
- evidence_id: subject-limits
  kind: validation
  reference: reports/sssom_scientific_curation_20261101/generation/logs/ready_source_subjects.log
  accessed_at: '2026-11-01T00:56:59Z'
  support: supports
  summary: Eighteen preexisting non-gating opaque-subject filename warnings; no new
    subject-identity ruling.
  snapshot_sha256: a16772841d62c8f1f9be43c85a24d0e9c1e687b6ec493652fd2c5be113da7762
- evidence_id: semantics
  kind: authority
  reference: MAPPING_SEMANTICS.md
  accessed_at: '2026-11-01T00:56:59Z'
  support: supports
  summary: Identity, predicate, registry and synonym contract.
  snapshot_sha256: 94aad13ea0fc3df82a37383f388f41432b607b04cac61ae5792ce1a381aef805
assessments:
- assessment_id: bounded-canonical
  area: consistency
  topic: Scoped canonical output preserves unrelated work
  outcome: supported
  target_ids:
  - canonical
  evidence_ids:
  - delta
  - receipt
  - full_qc_ready
  - ready_source_reconcile
  - ready_products
  summary: Only two carnitine rows and seven independently adjudicated alias cells
    change. The amide name is rejected in its sole YAML owner; the deferred DL-carnitine
    alias remains. All existing positions and 2,978 other row payloads survive.
- assessment_id: candidate-validity
  area: consistency
  topic: Safe-scope diagnostic output is mechanically valid
  outcome: supported
  target_ids:
  - candidate
  evidence_ids:
  - generation
  - inputs
  - ready_candidate_invariants
  - ready_candidate_schema
  - ready_candidate_curie
  - ready_candidate_products
  - ready_candidate_b4
  summary: The ready candidate contains 2,980 rows, zero native invariant rejects
    and zero source reconciliation drift. Configured label skips and B4 missing-source
    limits remain; this result is not scientific approval.
- assessment_id: promotion-boundary
  area: scope
  topic: No wholesale replacement or inherited scientific approval
  outcome: supported
  target_ids:
  - canonical
  - candidate
  evidence_ids:
  - promotion
  - row-deltas
  - receipt
  - ready_reviewed_export
  - ready_reviewed_validate
  summary: 'Full replacement is declined: it would rewrite 2,364 payloads, drop ten
    rows and add three, including 1,329 currently supported payloads. The narrow correction
    uses the native receipt chain, withdraws one stale owner approval and preserves
    the remaining scientific backlog.'
- assessment_id: preservation
  area: provenance
  topic: Dependencies and protected surfaces remain intact
  outcome: supported
  target_ids:
  - canonical
  - candidate
  evidence_ids:
  - delta
  - generation
  - inputs
  - subject-limits
  summary: Melezitose and the protected workflow, unified mapping and cycle profile
    remain byte-identical to base. The proposed melezitose correction is archived
    as blocked on PR764. No shared Claw checkout mutation, bulk CultureMech import,
    paid provider call, cycle advance or supervisor binding is claimed.
findings: []
actions: []
limitations:
- Deterministic checks do not establish every chemical identity or publishable synonym.
  Rule K retains 38 explicit obligations.
- 'Native semantic integrity passes while scientific release remains FAIL: 1,733 blocking
  findings and 2,272 assertions, one more assertion after withdrawing a stale approval.'
- B4 skips missing BTO/MICRO transforms and absent IDs; native product adapters also
  have explicit skips and nonblocking warnings.
- 18 opaque-subject filename warnings remain non-gating under the undecided subject
  contract.
- The complete diagnostic candidate and large external inputs remain local. Hashes,
  exact original paths and every candidate row delta are published.
- Earlier failed setup attempts, the blocked melezitose release attempt, and superseded
  intermediate validations remain diagnostic evidence, not final gate passes.
links:
- https://github.com/CultureBotAI/MediaIngredientMech/issues/669
- https://github.com/CultureBotAI/MediaIngredientMech/issues/718
- https://github.com/CultureBotAI/MediaIngredientMech/issues/875
- https://github.com/CultureBotAI/MediaIngredientMech/issues/901
- https://github.com/CultureBotAI/MediaIngredientMech/issues/1003
- https://github.com/CultureBotAI/MediaIngredientMech/issues/1004
- https://github.com/CultureBotAI/MediaIngredientMech/issues/1005
- https://github.com/CultureBotAI/MediaIngredientMech/issues/1006
tags:
- sssom
- scoped-correction
- mechanical-review
- no-wholesale-promotion
```
