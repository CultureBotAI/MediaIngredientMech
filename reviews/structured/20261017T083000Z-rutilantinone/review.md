# Per-record structured review: Rutilantinone (data/ingredients/mapped/Rutilantinone.yaml)

- Review: 20261017T083000Z-rutilantinone
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Rutilantinone (data/ingredients/mapped/Rutilantinone.yaml, record-1f5c121b98896c7f, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Rutilantinone.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Rutilantinone.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-1f5c121b98896c7f | data/ingredients/mapped/Rutilantinone.yaml | maintained | Rutilantinone |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-1f5c121b98896c7f | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-1f5c121b98896c7f | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-1f5c121b98896c7f | Reconciled against predecessor batch review 20261011T024638Z-mim-reconcile-all-batch-10 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-1f5c121b98896c7f.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-1f5c121b98896c7f.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T12:56:18Z; reviewed SHA-256=df697583f3a60cd1cf20ccf763c357f9a81e258cabec3da65141ad858a0d15cd; current SHA-256=df697583f3a60cd1cf20ccf763c357f9a81e258cabec3da65141ad858a0d15cd; hash_changed=False. Reports=["reports/yaml_record_review/Rutilantinone.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The CAS fallback resolves, but an exact CHEBI:108590 promotion candidate now exists.

## Findings

### rec-f-b6c923ec55afe45b: Historical review coverage and residual narrative: Rutilantinone

major / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-1f5c121b98896c7f.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T12:56:18Z; reviewed SHA-256=df697583f3a60cd1cf20ccf763c357f9a81e258cabec3da65141ad858a0d15cd; current SHA-256=df697583f3a60cd1cf20ccf763c357f9a81e258cabec3da65141ad858a0d15cd; hash_changed=False. Reports=["reports/yaml_record_review/Rutilantinone.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The CAS fallback resolves, but an exact CHEBI:108590 promotion candidate now exists.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-dcf5405d8793aad5 | data/ingredients/mapped/Rutilantinone.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1769],"raw_equal":true},"docs_rows":[{"identifier":"cas:21288-61-9","line":1771,"mapping_status":"MAPPED","ontology_id":"cas:21288-61-9","preferred_term":"Rutilantinone"}],"identifier":"cas:21288-61-9","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"FALLBACK_REGISTRY","ontology_id":"cas:21288-61-9","ontology_label":"Rutilantinone","ontology_source":"CAS"},"preferred_term":"Rutilantinone","sssom_rows":[{"data_row":2460,"object_id":"cas:21288-61-9","object_label":"Rutilantinone","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Rutilantinone","synonym_count":0} |
| ev-b35492af66a11c59 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1769] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-ee2a0f2764ace3be | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Rutilantinone; data-row positions=[2460] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":2460,"object_id":"cas:21288-61-9","object_label":"Rutilantinone","other":"CAS:21288-61-9","predicate_id":"skos:exactMatch","subject_id":"MIM:Rutilantinone","validation_method":"none&#124;UNKNOWN_TERM&#124;2026-07-07"}] |
| ev-7de66672b2f24b2f | docs/data/mapped_ingredients.csv; CSV lines=[1771] | supports | Published identity and count rows inspected: [{"identifier":"cas:21288-61-9","line":1771,"mapping_quality":"FALLBACK_REGISTRY","mapping_status":"MAPPED","media_count":"0","ontology_id":"cas:21288-61-9","preferred_term":"Rutilantinone","total_occurrences":"0"}] |
| ev-9b1a5a07353443df | reports/yaml_record_review/Rutilantinone.md; &#96;data/ingredients/mapped/Rutilantinone.yaml&#96;:2 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-a8dcde918023d555 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1180] | context_only | [{"current_record_sha256":"df697583f3a60cd1cf20ccf763c357f9a81e258cabec3da65141ad858a0d15cd","finding_id":"SEM:9b25c09c65c9ab07454b","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024638Z-mim-reconcile-all-batch-10.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-rutilantinone
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Rutilantinone (data/ingredients/mapped/Rutilantinone.yaml)'
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
summary: Per-record structured review for Rutilantinone (data/ingredients/mapped/Rutilantinone.yaml,
  record-1f5c121b98896c7f, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Rutilantinone.yaml
    sha256: df697583f3a60cd1cf20ccf763c357f9a81e258cabec3da65141ad858a0d15cd
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
  - path: reports/yaml_record_review/Rutilantinone.md
    sha256: 9f0336f39b1ef4363d42efe9cce2c7e1c59992ec8d40531da333cd1c69cf7bfa
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-1f5c121b98896c7f
  path: data/ingredients/mapped/Rutilantinone.yaml
  label: Rutilantinone
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Rutilantinone.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Rutilantinone.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Rutilantinone.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-1f5c121b98896c7f
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-1f5c121b98896c7f
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-1f5c121b98896c7f
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024638Z-mim-reconcile-all-batch-10
    and semantic review dispositions on HEAD.
  target_ids:
  - record-1f5c121b98896c7f
evidence:
- evidence_id: ev-dcf5405d8793aad5
  kind: record_content
  reference: data/ingredients/mapped/Rutilantinone.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1769],"raw_equal":true},"docs_rows":[{"identifier":"cas:21288-61-9","line":1771,"mapping_status":"MAPPED","ontology_id":"cas:21288-61-9","preferred_term":"Rutilantinone"}],"identifier":"cas:21288-61-9","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"FALLBACK_REGISTRY","ontology_id":"cas:21288-61-9","ontology_label":"Rutilantinone","ontology_source":"CAS"},"preferred_term":"Rutilantinone","sssom_rows":[{"data_row":2460,"object_id":"cas:21288-61-9","object_label":"Rutilantinone","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Rutilantinone","synonym_count":0}'
  snapshot_sha256: df697583f3a60cd1cf20ccf763c357f9a81e258cabec3da65141ad858a0d15cd
- evidence_id: ev-b35492af66a11c59
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1769]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-ee2a0f2764ace3be
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Rutilantinone; data-row positions=[2460]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":2460,"object_id":"cas:21288-61-9","object_label":"Rutilantinone","other":"CAS:21288-61-9","predicate_id":"skos:exactMatch","subject_id":"MIM:Rutilantinone","validation_method":"none|UNKNOWN_TERM|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-7de66672b2f24b2f
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1771]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"cas:21288-61-9","line":1771,"mapping_quality":"FALLBACK_REGISTRY","mapping_status":"MAPPED","media_count":"0","ontology_id":"cas:21288-61-9","preferred_term":"Rutilantinone","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-9b1a5a07353443df
  kind: prior_review
  reference: reports/yaml_record_review/Rutilantinone.md
  locator: '`data/ingredients/mapped/Rutilantinone.yaml`:2'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 9f0336f39b1ef4363d42efe9cce2c7e1c59992ec8d40531da333cd1c69cf7bfa
- evidence_id: ev-a8dcde918023d555
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1180]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"df697583f3a60cd1cf20ccf763c357f9a81e258cabec3da65141ad858a0d15cd","finding_id":"SEM:9b25c09c65c9ab07454b","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-cc77729b50adcdab
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-1f5c121b98896c7f
  evidence_ids:
  - ev-dcf5405d8793aad5
  - ev-b35492af66a11c59
  - ev-ee2a0f2764ace3be
  - ev-7de66672b2f24b2f
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-8aa32062e954710f
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-1f5c121b98896c7f
  evidence_ids:
  - ev-9b1a5a07353443df
  - ev-dcf5405d8793aad5
  - ev-a8dcde918023d555
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T12:56:18Z;
    reviewed SHA-256=df697583f3a60cd1cf20ccf763c357f9a81e258cabec3da65141ad858a0d15cd;
    current SHA-256=df697583f3a60cd1cf20ccf763c357f9a81e258cabec3da65141ad858a0d15cd;
    hash_changed=False. Reports=["reports/yaml_record_review/Rutilantinone.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The CAS fallback
    resolves, but an exact CHEBI:108590 promotion candidate now exists.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-9b1a5a07353443df
    - ev-dcf5405d8793aad5
  - name: legacy-native-ids
    value: '["SEM:9b25c09c65c9ab07454b"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-dcf5405d8793aad5
    - ev-9b1a5a07353443df
    - ev-a8dcde918023d555
findings:
- finding_id: rec-f-b6c923ec55afe45b
  issue_key: mim-reconciliation-historical-review-coverage-and-r-1f5c121b98896c7f
  category: provenance
  severity: major
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: Rutilantinone'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T12:56:18Z;
    reviewed SHA-256=df697583f3a60cd1cf20ccf763c357f9a81e258cabec3da65141ad858a0d15cd;
    current SHA-256=df697583f3a60cd1cf20ccf763c357f9a81e258cabec3da65141ad858a0d15cd;
    hash_changed=False. Reports=["reports/yaml_record_review/Rutilantinone.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The CAS fallback
    resolves, but an exact CHEBI:108590 promotion candidate now exists.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-1f5c121b98896c7f
  evidence_ids:
  - ev-9b1a5a07353443df
  - ev-dcf5405d8793aad5
  - ev-a8dcde918023d555
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Rutilantinone.yaml
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
