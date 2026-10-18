# Per-record structured review: Phenethylamine_Hydrochloride (data/ingredients/mapped/Phenethylamine_Hydrochloride.yaml)

- Review: 20261017T083000Z-phenethylamine-hydrochloride
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Phenethylamine_Hydrochloride (data/ingredients/mapped/Phenethylamine_Hydrochloride.yaml, record-000897aa7bb53160, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Phenethylamine_Hydrochloride.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Phenethylamine_Hydrochloride.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-000897aa7bb53160 | data/ingredients/mapped/Phenethylamine_Hydrochloride.yaml | maintained | Phenethylamine_Hydrochloride |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-000897aa7bb53160 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-000897aa7bb53160 | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-000897aa7bb53160 | Reconciled against predecessor batch review 20261011T024638Z-mim-reconcile-all-batch-10 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-000897aa7bb53160.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-000897aa7bb53160.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T09:02:19Z; reviewed SHA-256=1283e083fbb866db9d9202fdb1b08fbbf2de4016993395ca5f18644e5fc0f320; current SHA-256=1283e083fbb866db9d9202fdb1b08fbbf2de4016993395ca5f18644e5fc0f320; hash_changed=False. Reports=["reports/yaml_record_review/Phenethylamine_Hydrochloride.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The free-base CHEBI:18397 identity passes, but final other exports the old hydrochloride label.

## Findings

### rec-f-e7c741b6bc88075d: Historical review coverage and residual narrative: Phenethylamine_Hydrochloride

major / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-000897aa7bb53160.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T09:02:19Z; reviewed SHA-256=1283e083fbb866db9d9202fdb1b08fbbf2de4016993395ca5f18644e5fc0f320; current SHA-256=1283e083fbb866db9d9202fdb1b08fbbf2de4016993395ca5f18644e5fc0f320; hash_changed=False. Reports=["reports/yaml_record_review/Phenethylamine_Hydrochloride.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The free-base CHEBI:18397 identity passes, but final other exports the old hydrochloride label.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-c536253de93aeb4b | data/ingredients/mapped/Phenethylamine_Hydrochloride.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1639],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:18397","line":1641,"mapping_status":"MAPPED","ontology_id":"CHEBI:18397","preferred_term":"2-phenylethylamine"}],"identifier":"CHEBI:18397","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"CAS_RN_LOOKUP","ontology_id":"CHEBI:18397","ontology_label":"2-phenylethylamine","ontology_source":"CHEBI"},"preferred_term":"2-phenylethylamine","sssom_rows":[{"data_row":2231,"object_id":"CHEBI:18397","object_label":"2-phenylethylamine","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Phenethylamine_Hydrochloride","synonym_count":3} |
| ev-93172f2f4eebe9e3 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1639] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-6ac704f1d1650d82 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Phenethylamine_Hydrochloride; data-row positions=[2231] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":2231,"object_id":"CHEBI:18397","object_label":"2-phenylethylamine","other":"2-phenylethanamine&#124;Phenethylamine Hydrochloride&#124;Beta-phenylethylamine&#124;CAS:64-04-0","predicate_id":"skos:exactMatch","subject_id":"MIM:Phenethylamine_Hydrochloride","validation_method":"OAK+OLS:chebi&#124;SYNONYM_ENRICH&#124;2026-07-07"}] |
| ev-e34c5ff42625128a | docs/data/mapped_ingredients.csv; CSV lines=[1641] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:18397","line":1641,"mapping_quality":"CAS_RN_LOOKUP","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:18397","preferred_term":"2-phenylethylamine","total_occurrences":"0"}] |
| ev-f8b319c8979d62fc | reports/yaml_record_review/Phenethylamine_Hydrochloride.md; &#96;data/ingredients/mapped/Phenethylamine_Hydrochloride.yaml&#96;:2; Verdict:4; Identity:10; Validation:19; Evidence:31; Completeness:41; Recommended Edits:47 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-c941239e354279b0 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1101] | context_only | [{"current_record_sha256":"1283e083fbb866db9d9202fdb1b08fbbf2de4016993395ca5f18644e5fc0f320","finding_id":"SEM:3efa3e4f41763110a70d","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024638Z-mim-reconcile-all-batch-10.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-phenethylamine-hydrochloride
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Phenethylamine_Hydrochloride (data/ingredients/mapped/Phenethylamine_Hydrochloride.yaml)'
started_at: '2026-10-17T08:25:00Z'
finished_at: '2026-10-17T08:30:00Z'
reviewer:
  identity: Antigravity
  kind: agent
  model: claude-opus-4-6
  independence: independent
  independence_basis: Independent per-record structured review and reconciliation
    against current HEAD and historical review inputs.
skill: review-yaml-record
completion: partial
verdict: needs_curation
native_verdict: mapping_status=MAPPED; open=0; deferred=1
scientific_review: false
summary: Per-record structured review for Phenethylamine_Hydrochloride (data/ingredients/mapped/Phenethylamine_Hydrochloride.yaml,
  record-000897aa7bb53160, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Phenethylamine_Hydrochloride.yaml
    sha256: 1283e083fbb866db9d9202fdb1b08fbbf2de4016993395ca5f18644e5fc0f320
    role: target
  - path: reviews/structured/20261011T024638Z-mim-reconcile-all-batch-10/review.yaml
    sha256: 8c3aa2fca1269d1dbbf6117e85dea5b0de5047a8505841641245bd7ee99b936d
    role: context
  - path: data/curated/mapped_ingredients.yaml
    sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
    role: context
  - path: mappings/ingredient_mappings.sssom.tsv
    sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
    role: context
  - path: docs/data/mapped_ingredients.csv
    sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
    role: context
  - path: reports/yaml_record_review/Phenethylamine_Hydrochloride.md
    sha256: 4ae5cf7d79ba8e588db0383a199fee3f32c4d61bc6bb98f4a58f86b05a876235
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-000897aa7bb53160
  path: data/ingredients/mapped/Phenethylamine_Hydrochloride.yaml
  label: Phenethylamine_Hydrochloride
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Phenethylamine_Hydrochloride.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Phenethylamine_Hydrochloride.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Phenethylamine_Hydrochloride.yaml
    selected from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-000897aa7bb53160
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-000897aa7bb53160
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-000897aa7bb53160
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024638Z-mim-reconcile-all-batch-10
    and semantic review dispositions on HEAD.
  target_ids:
  - record-000897aa7bb53160
evidence:
- evidence_id: ev-c536253de93aeb4b
  kind: record_content
  reference: data/ingredients/mapped/Phenethylamine_Hydrochloride.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1639],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:18397","line":1641,"mapping_status":"MAPPED","ontology_id":"CHEBI:18397","preferred_term":"2-phenylethylamine"}],"identifier":"CHEBI:18397","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"CAS_RN_LOOKUP","ontology_id":"CHEBI:18397","ontology_label":"2-phenylethylamine","ontology_source":"CHEBI"},"preferred_term":"2-phenylethylamine","sssom_rows":[{"data_row":2231,"object_id":"CHEBI:18397","object_label":"2-phenylethylamine","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Phenethylamine_Hydrochloride","synonym_count":3}'
  snapshot_sha256: 1283e083fbb866db9d9202fdb1b08fbbf2de4016993395ca5f18644e5fc0f320
- evidence_id: ev-93172f2f4eebe9e3
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1639]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-6ac704f1d1650d82
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Phenethylamine_Hydrochloride; data-row positions=[2231]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":2231,"object_id":"CHEBI:18397","object_label":"2-phenylethylamine","other":"2-phenylethanamine|Phenethylamine
    Hydrochloride|Beta-phenylethylamine|CAS:64-04-0","predicate_id":"skos:exactMatch","subject_id":"MIM:Phenethylamine_Hydrochloride","validation_method":"OAK+OLS:chebi|SYNONYM_ENRICH|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-e34c5ff42625128a
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1641]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:18397","line":1641,"mapping_quality":"CAS_RN_LOOKUP","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:18397","preferred_term":"2-phenylethylamine","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-f8b319c8979d62fc
  kind: prior_review
  reference: reports/yaml_record_review/Phenethylamine_Hydrochloride.md
  locator: '`data/ingredients/mapped/Phenethylamine_Hydrochloride.yaml`:2; Verdict:4;
    Identity:10; Validation:19; Evidence:31; Completeness:41; Recommended Edits:47'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 4ae5cf7d79ba8e588db0383a199fee3f32c4d61bc6bb98f4a58f86b05a876235
  quote: "Recommended Edits:\n- Major: in `data/ingredients/mapped/Phenethylamine_Hydrochloride.yaml`,\
    \ retype\n  or suppress the `Phenethylamine Hydrochloride` raw synonym so it remains\n\
    \  provenance for the #235 relabelling only and no longer appears in\n  `mappings/ingredient_mappings.sssom.tsv`;\
    \ rebuild the final SSSOM and rerun\n  `scripts/validate_sssom_invariants.py`."
- evidence_id: ev-c941239e354279b0
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1101]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"1283e083fbb866db9d9202fdb1b08fbbf2de4016993395ca5f18644e5fc0f320","finding_id":"SEM:3efa3e4f41763110a70d","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-677d6939f7cf7266
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-000897aa7bb53160
  evidence_ids:
  - ev-c536253de93aeb4b
  - ev-93172f2f4eebe9e3
  - ev-6ac704f1d1650d82
  - ev-e34c5ff42625128a
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-a04f69c0e978bf96
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-000897aa7bb53160
  evidence_ids:
  - ev-f8b319c8979d62fc
  - ev-c536253de93aeb4b
  - ev-c941239e354279b0
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T09:02:19Z;
    reviewed SHA-256=1283e083fbb866db9d9202fdb1b08fbbf2de4016993395ca5f18644e5fc0f320;
    current SHA-256=1283e083fbb866db9d9202fdb1b08fbbf2de4016993395ca5f18644e5fc0f320;
    hash_changed=False. Reports=["reports/yaml_record_review/Phenethylamine_Hydrochloride.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The free-base
    CHEBI:18397 identity passes, but final other exports the old hydrochloride label.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-f8b319c8979d62fc
    - ev-c536253de93aeb4b
  - name: legacy-native-ids
    value: '["SEM:3efa3e4f41763110a70d"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-c536253de93aeb4b
    - ev-f8b319c8979d62fc
    - ev-c941239e354279b0
findings:
- finding_id: rec-f-e7c741b6bc88075d
  issue_key: mim-reconciliation-historical-review-coverage-and-r-000897aa7bb53160
  category: provenance
  severity: major
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: Phenethylamine_Hydrochloride'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T09:02:19Z;
    reviewed SHA-256=1283e083fbb866db9d9202fdb1b08fbbf2de4016993395ca5f18644e5fc0f320;
    current SHA-256=1283e083fbb866db9d9202fdb1b08fbbf2de4016993395ca5f18644e5fc0f320;
    hash_changed=False. Reports=["reports/yaml_record_review/Phenethylamine_Hydrochloride.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The free-base
    CHEBI:18397 identity passes, but final other exports the old hydrochloride label.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-000897aa7bb53160
  evidence_ids:
  - ev-f8b319c8979d62fc
  - ev-c536253de93aeb4b
  - ev-c941239e354279b0
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Phenethylamine_Hydrochloride.yaml
    role: maintained ingredient
  field_paths:
  - curation_history
  tags:
  - reconciliation
  - bundle-by-owner
  - historical-review-coverage-and-r
  external_issues:
  - https://github.com/CultureBotAI/MediaIngredientMech/issues/718
actions: []
limitations:
- 'Read-only per-record structured review (scientific_review: false); no ingredient
  YAML, curated aggregate, or SSSOM files were modified.'
- Confirmed local evidence gaps and structural issues are recorded as open with bounded
  remediation actions; historical or source-context claims requiring primary recipe/literature
  verification remain deferred (provisional).
tags:
- record-review
- per-record
- reconciliation
- bundle-by-owner
notes:
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb)
  with lineage to 20261011T024638Z-mim-reconcile-all-batch-10.
```
