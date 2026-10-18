# Per-record structured review: Sodium_D-Lactate (data/ingredients/mapped/Sodium_D-Lactate.yaml)

- Review: 20261017T083000Z-sodium-d-lactate
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Sodium_D-Lactate (data/ingredients/mapped/Sodium_D-Lactate.yaml, record-1dd74b059cec6ce3, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Sodium_D-Lactate.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Sodium_D-Lactate.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-1dd74b059cec6ce3 | data/ingredients/mapped/Sodium_D-Lactate.yaml | maintained | Sodium_D-Lactate |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-1dd74b059cec6ce3 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-1dd74b059cec6ce3 | Role assertions on nutritional_roles[0], nutritional_roles[1] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-1dd74b059cec6ce3 | Reconciled against predecessor batch review 20261011T024638Z-mim-reconcile-all-batch-11 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-1dd74b059cec6ce3.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-1dd74b059cec6ce3.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T14:59:34Z; reviewed SHA-256=5b9a8ec9f0371556ec5e88ab9e10ad5a6ad91407a7f608f16b33e3afd58bcbdb; current SHA-256=5b9a8ec9f0371556ec5e88ab9e10ad5a6ad91407a7f608f16b33e3afd58bcbdb; hash_changed=False. Reports=["reports/yaml_record_review/Sodium_D-Lactate.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The CAS fallback identity, PubChem structure, and final SSSOM row pass, but carbon/energy roles are provisional name-pattern claims.

### Historical provisional-role concern

evidence: concern. Targets: record-1dd74b059cec6ce3.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-2591100f88c79c49: Reassess prediction-only role support: Sodium D-Lactate

major / open / confirmed; issue key: mim-reconciliation-role-support-1dd74b059cec6ce3.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-2591100f88c79c49

Reassess prediction-only role support: Sodium D-Lactate

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-7bb86e3f9c7cfe9a | data/ingredients/mapped/Sodium_D-Lactate.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1828],"raw_equal":true},"docs_rows":[{"identifier":"cas:920-49-0","line":1830,"mapping_status":"MAPPED","ontology_id":"cas:920-49-0","preferred_term":"Sodium D-Lactate"}],"identifier":"cas:920-49-0","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":1,"total_occurrences":1},"ontology_mapping":{"mapping_quality":"FALLBACK_REGISTRY","ontology_id":"cas:920-49-0","ontology_label":"Sodium D-Lactate","ontology_source":"CAS"},"preferred_term":"Sodium D-Lactate","sssom_rows":[{"data_row":2553,"object_id":"cas:920-49-0","object_label":"Sodium D-Lactate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Sodium_D-Lactate","synonym_count":0} |
| ev-111686ccae6bd7a7 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1828] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-b43a86f141072f61 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Sodium_D-Lactate; data-row positions=[2553] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":2553,"object_id":"cas:920-49-0","object_label":"Sodium D-Lactate","other":"CAS:920-49-0","predicate_id":"skos:exactMatch","subject_id":"MIM:Sodium_D-Lactate","validation_method":"none&#124;UNKNOWN_TERM&#124;2026-07-07"}] |
| ev-6bc10070421d9f9a | docs/data/mapped_ingredients.csv; CSV lines=[1830] | supports | Published identity and count rows inspected: [{"identifier":"cas:920-49-0","line":1830,"mapping_quality":"FALLBACK_REGISTRY","mapping_status":"MAPPED","media_count":"1","ontology_id":"cas:920-49-0","preferred_term":"Sodium D-Lactate","total_occurrences":"1"}] |
| ev-f8240deda5fa6fca | reports/yaml_record_review/Sodium_D-Lactate.md; &#96;data/ingredients/mapped/Sodium_D-Lactate.yaml&#96;:2 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-d85da2d5f6273794 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1211,2028,2051] | context_only | [{"current_record_sha256":"5b9a8ec9f0371556ec5e88ab9e10ad5a6ad91407a7f608f16b33e3afd58bcbdb","finding_id":"SEM:a5c04cd0e6e76c2b91e5","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"5b9a8ec9f0371556ec5e88ab9e10ad5a6ad91407a7f608f16b33e3afd58bcbdb","finding_id":"SEM:7e5f297de8c35b63f4b1","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"5b9a8ec9f0371556ec5e88ab9e10ad5a6ad91407a7f608f16b33e3afd58bcbdb","finding_id":"SEM:1438c3a06a2e550a9f08","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-03bd415e2196b7d3 | data/ingredients/mapped/Sodium_D-Lactate.yaml; nutritional_roles[0], nutritional_roles[1] | supports | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1828],"raw_equal":true},"docs_rows":[{"identifier":"cas:920-49-0","line":1830,"mapping_status":"MAPPED","ontology_id":"cas:920-49-0","preferred_term":"Sodium D-Lactate"}],"identifier":"cas:920-49-0","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":1,"total_occurrences":1},"ontology_mapping":{"mapping_quality":"FALLBACK_REGISTRY","ontology_id":"cas:920-49-0","ontology_label":"Sodium D-Lactate","ontology_source":"CAS"},"preferred_term":"Sodium D-Lactate","sssom_rows":[{"data_row":2553,"object_id":"cas:920-49-0","object_label":"Sodium D-Lactate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Sodium_D-Lactate","synonym_count":0} |
| ev-b5c0cdbcac1203cf | reviews/structured/20261011T024638Z-mim-reconcile-all-batch-11/review.yaml; findings[finding_id=f-2591100f88c79c49] | context_only | Predecessor structured review finding f-2591100f88c79c49 in 20261011T024638Z-mim-reconcile-all-batch-11 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024638Z-mim-reconcile-all-batch-11.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-sodium-d-lactate
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Sodium_D-Lactate (data/ingredients/mapped/Sodium_D-Lactate.yaml)'
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
native_verdict: mapping_status=MAPPED; open=1; deferred=0
scientific_review: false
summary: Per-record structured review for Sodium_D-Lactate (data/ingredients/mapped/Sodium_D-Lactate.yaml,
  record-1dd74b059cec6ce3, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Sodium_D-Lactate.yaml
    sha256: 5b9a8ec9f0371556ec5e88ab9e10ad5a6ad91407a7f608f16b33e3afd58bcbdb
    role: target
  - path: reviews/structured/20261011T024638Z-mim-reconcile-all-batch-11/review.yaml
    sha256: a417d1bfc777756925990a4ecae1a6b539746c3606d042df7e1c29a218c62f8b
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
  - path: reports/yaml_record_review/Sodium_D-Lactate.md
    sha256: 2bb81803a6b9a7647ea042d8280e94d20586dbbeb0711108dea75dd6a61f3f7f
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-1dd74b059cec6ce3
  path: data/ingredients/mapped/Sodium_D-Lactate.yaml
  label: Sodium_D-Lactate
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Sodium_D-Lactate.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Sodium_D-Lactate.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Sodium_D-Lactate.yaml selected
    from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-1dd74b059cec6ce3
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-1dd74b059cec6ce3
  evidence_ids:
  - ev-7bb86e3f9c7cfe9a
  - ev-111686ccae6bd7a7
  - ev-b43a86f141072f61
  - ev-6bc10070421d9f9a
  - ev-03bd415e2196b7d3
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0], nutritional_roles[1] rely only
    on COMPUTATIONAL_PREDICTION or empty evidence.
  target_ids:
  - record-1dd74b059cec6ce3
  evidence_ids:
  - ev-7bb86e3f9c7cfe9a
  - ev-d85da2d5f6273794
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024638Z-mim-reconcile-all-batch-11
    and semantic review dispositions on HEAD.
  target_ids:
  - record-1dd74b059cec6ce3
  evidence_ids:
  - ev-f8240deda5fa6fca
  - ev-d85da2d5f6273794
  - ev-b5c0cdbcac1203cf
evidence:
- evidence_id: ev-7bb86e3f9c7cfe9a
  kind: record_content
  reference: data/ingredients/mapped/Sodium_D-Lactate.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1828],"raw_equal":true},"docs_rows":[{"identifier":"cas:920-49-0","line":1830,"mapping_status":"MAPPED","ontology_id":"cas:920-49-0","preferred_term":"Sodium
    D-Lactate"}],"identifier":"cas:920-49-0","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":1,"total_occurrences":1},"ontology_mapping":{"mapping_quality":"FALLBACK_REGISTRY","ontology_id":"cas:920-49-0","ontology_label":"Sodium
    D-Lactate","ontology_source":"CAS"},"preferred_term":"Sodium D-Lactate","sssom_rows":[{"data_row":2553,"object_id":"cas:920-49-0","object_label":"Sodium
    D-Lactate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Sodium_D-Lactate","synonym_count":0}'
  snapshot_sha256: 5b9a8ec9f0371556ec5e88ab9e10ad5a6ad91407a7f608f16b33e3afd58bcbdb
- evidence_id: ev-111686ccae6bd7a7
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1828]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-b43a86f141072f61
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Sodium_D-Lactate; data-row positions=[2553]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":2553,"object_id":"cas:920-49-0","object_label":"Sodium
    D-Lactate","other":"CAS:920-49-0","predicate_id":"skos:exactMatch","subject_id":"MIM:Sodium_D-Lactate","validation_method":"none|UNKNOWN_TERM|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-6bc10070421d9f9a
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1830]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"cas:920-49-0","line":1830,"mapping_quality":"FALLBACK_REGISTRY","mapping_status":"MAPPED","media_count":"1","ontology_id":"cas:920-49-0","preferred_term":"Sodium
    D-Lactate","total_occurrences":"1"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-f8240deda5fa6fca
  kind: prior_review
  reference: reports/yaml_record_review/Sodium_D-Lactate.md
  locator: '`data/ingredients/mapped/Sodium_D-Lactate.yaml`:2'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 2bb81803a6b9a7647ea042d8280e94d20586dbbeb0711108dea75dd6a61f3f7f
- evidence_id: ev-d85da2d5f6273794
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1211,2028,2051]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"5b9a8ec9f0371556ec5e88ab9e10ad5a6ad91407a7f608f16b33e3afd58bcbdb","finding_id":"SEM:a5c04cd0e6e76c2b91e5","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"5b9a8ec9f0371556ec5e88ab9e10ad5a6ad91407a7f608f16b33e3afd58bcbdb","finding_id":"SEM:7e5f297de8c35b63f4b1","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"5b9a8ec9f0371556ec5e88ab9e10ad5a6ad91407a7f608f16b33e3afd58bcbdb","finding_id":"SEM:1438c3a06a2e550a9f08","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-03bd415e2196b7d3
  kind: record_content
  reference: data/ingredients/mapped/Sodium_D-Lactate.yaml
  locator: nutritional_roles[0], nutritional_roles[1]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1828],"raw_equal":true},"docs_rows":[{"identifier":"cas:920-49-0","line":1830,"mapping_status":"MAPPED","ontology_id":"cas:920-49-0","preferred_term":"Sodium
    D-Lactate"}],"identifier":"cas:920-49-0","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":1,"total_occurrences":1},"ontology_mapping":{"mapping_quality":"FALLBACK_REGISTRY","ontology_id":"cas:920-49-0","ontology_label":"Sodium
    D-Lactate","ontology_source":"CAS"},"preferred_term":"Sodium D-Lactate","sssom_rows":[{"data_row":2553,"object_id":"cas:920-49-0","object_label":"Sodium
    D-Lactate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Sodium_D-Lactate","synonym_count":0}'
  snapshot_sha256: 5b9a8ec9f0371556ec5e88ab9e10ad5a6ad91407a7f608f16b33e3afd58bcbdb
- evidence_id: ev-b5c0cdbcac1203cf
  kind: prior_review
  reference: reviews/structured/20261011T024638Z-mim-reconcile-all-batch-11/review.yaml
  locator: findings[finding_id=f-2591100f88c79c49]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-2591100f88c79c49 in 20261011T024638Z-mim-reconcile-all-batch-11
  snapshot_sha256: a417d1bfc777756925990a4ecae1a6b539746c3606d042df7e1c29a218c62f8b
assessments:
- assessment_id: a-7245162605a300f8
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-1dd74b059cec6ce3
  evidence_ids:
  - ev-7bb86e3f9c7cfe9a
  - ev-111686ccae6bd7a7
  - ev-b43a86f141072f61
  - ev-6bc10070421d9f9a
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-109fee5094c56908
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-1dd74b059cec6ce3
  evidence_ids:
  - ev-f8240deda5fa6fca
  - ev-7bb86e3f9c7cfe9a
  - ev-d85da2d5f6273794
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T14:59:34Z;
    reviewed SHA-256=5b9a8ec9f0371556ec5e88ab9e10ad5a6ad91407a7f608f16b33e3afd58bcbdb;
    current SHA-256=5b9a8ec9f0371556ec5e88ab9e10ad5a6ad91407a7f608f16b33e3afd58bcbdb;
    hash_changed=False. Reports=["reports/yaml_record_review/Sodium_D-Lactate.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The CAS
    fallback identity, PubChem structure, and final SSSOM row pass, but carbon/energy
    roles are provisional name-pattern claims.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-f8240deda5fa6fca
    - ev-7bb86e3f9c7cfe9a
  - name: legacy-native-ids
    value: '["SEM:a5c04cd0e6e76c2b91e5","SEM:7e5f297de8c35b63f4b1","SEM:1438c3a06a2e550a9f08"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-7bb86e3f9c7cfe9a
    - ev-f8240deda5fa6fca
    - ev-d85da2d5f6273794
- assessment_id: a-03bd415e2196b7d3
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-1dd74b059cec6ce3
  evidence_ids:
  - ev-f8240deda5fa6fca
  - ev-03bd415e2196b7d3
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-f8240deda5fa6fca
    - ev-03bd415e2196b7d3
findings:
- finding_id: rec-f-2591100f88c79c49
  issue_key: mim-reconciliation-role-support-1dd74b059cec6ce3
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Sodium D-Lactate'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-1dd74b059cec6ce3
  evidence_ids:
  - ev-f8240deda5fa6fca
  - ev-03bd415e2196b7d3
  - ev-b5c0cdbcac1203cf
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Sodium_D-Lactate.yaml
    role: maintained ingredient
  field_paths:
  - nutritional_roles[0]
  - nutritional_roles[1]
  tags:
  - reconciliation
  - bundle-by-owner
  - role-support
  external_issues:
  - https://github.com/CultureBotAI/MediaIngredientMech/issues/718
  previous_occurrences:
  - repository: CultureBotAI/MediaIngredientMech
    review_id: 20261011T024638Z-mim-reconcile-all-batch-11
    finding_id: f-2591100f88c79c49
actions:
- action_id: rec-action-2591100f88c79c49
  description: 'Reassess prediction-only role support: Sodium D-Lactate'
  finding_ids:
  - rec-f-2591100f88c79c49
  target_ids:
  - record-1dd74b059cec6ce3
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Sodium_D-Lactate.yaml
    role: maintained ingredient
  acceptance_checks:
  - Address the exact fields/tokens and evidence gap described in this finding; preserve
    unrelated source labels and audit history.
  - Inspect the original preparation, organism, or mapping evidence where needed;
    do not promote a label/name-pattern inference to proof.
  - For an authorized fix, synchronize maintained surfaces, run focused validation,
    and save an evidence-backed successor citing this finding.
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
  with lineage to 20261011T024638Z-mim-reconcile-all-batch-11.
```
