# Per-record structured review: Sialyllacto-N-tetraose_D (data/ingredients/mapped/Sialyllacto-N-tetraose_D.yaml)

- Review: 20261017T083000Z-sialyllacto-n-tetraose-d
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Sialyllacto-N-tetraose_D (data/ingredients/mapped/Sialyllacto-N-tetraose_D.yaml, record-26bcbd3cfaf22637, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Sialyllacto-N-tetraose_D.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Sialyllacto-N-tetraose_D.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-26bcbd3cfaf22637 | data/ingredients/mapped/Sialyllacto-N-tetraose_D.yaml | maintained | Sialyllacto-N-tetraose_D |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-26bcbd3cfaf22637 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-26bcbd3cfaf22637 | Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-26bcbd3cfaf22637 | Reconciled against predecessor batch review 20261011T024638Z-mim-reconcile-all-batch-10 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-26bcbd3cfaf22637.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-26bcbd3cfaf22637.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T13:59:34Z; reviewed SHA-256=e69b97faa37600d48b65806a9eee8d965f85ecb9d33189651babc8e7068e102a; current SHA-256=e69b97faa37600d48b65806a9eee8d965f85ecb9d33189651babc8e7068e102a; hash_changed=False. Reports=["reports/yaml_record_review/Sialyllacto-N-tetraose_D.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The CAS fallback identity, PubChem structure, and final SSSOM row pass, but CARBON_SOURCE is only provisional name-pattern inference.

### Historical provisional-role concern

evidence: concern. Targets: record-26bcbd3cfaf22637.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-42b990d41a5cea09: Reassess prediction-only role support: Sialyllacto-N-tetraose d

major / open / confirmed; issue key: mim-reconciliation-role-support-26bcbd3cfaf22637.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-42b990d41a5cea09

Reassess prediction-only role support: Sialyllacto-N-tetraose d

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-1f70e03370f0e956 | data/ingredients/mapped/Sialyllacto-N-tetraose_D.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1793],"raw_equal":true},"docs_rows":[{"identifier":"cas:100789-83-1","line":1795,"mapping_status":"MAPPED","ontology_id":"cas:100789-83-1","preferred_term":"Sialyllacto-N-tetraose d"}],"identifier":"cas:100789-83-1","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"FALLBACK_REGISTRY","ontology_id":"cas:100789-83-1","ontology_label":"Sialyllacto-N-tetraose d","ontology_source":"CAS"},"preferred_term":"Sialyllacto-N-tetraose d","sssom_rows":[{"data_row":2503,"object_id":"cas:100789-83-1","object_label":"Sialyllacto-N-tetraose d","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Sialyllacto-N-tetraose_D","synonym_count":0} |
| ev-e249d4b983ff3991 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1793] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-bb5988ac1181252f | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Sialyllacto-N-tetraose_D; data-row positions=[2503] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":2503,"object_id":"cas:100789-83-1","object_label":"Sialyllacto-N-tetraose d","other":"CAS:100789-83-1","predicate_id":"skos:exactMatch","subject_id":"MIM:Sialyllacto-N-tetraose_D","validation_method":"none&#124;UNKNOWN_TERM&#124;2026-07-07"}] |
| ev-2810100765fde752 | docs/data/mapped_ingredients.csv; CSV lines=[1795] | supports | Published identity and count rows inspected: [{"identifier":"cas:100789-83-1","line":1795,"mapping_quality":"FALLBACK_REGISTRY","mapping_status":"MAPPED","media_count":"0","ontology_id":"cas:100789-83-1","preferred_term":"Sialyllacto-N-tetraose d","total_occurrences":"0"}] |
| ev-926ed9a85c736b29 | reports/yaml_record_review/Sialyllacto-N-tetraose_D.md; &#96;data/ingredients/mapped/Sialyllacto-N-tetraose_D.yaml&#96;:2 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-012fb96537b07a82 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1193,2048] | context_only | [{"current_record_sha256":"e69b97faa37600d48b65806a9eee8d965f85ecb9d33189651babc8e7068e102a","finding_id":"SEM:a4bfda0d80d6e7579f9e","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"e69b97faa37600d48b65806a9eee8d965f85ecb9d33189651babc8e7068e102a","finding_id":"SEM:f0c3d3a41c1fde77ddf1","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-3aa1200e276e179e | data/ingredients/mapped/Sialyllacto-N-tetraose_D.yaml; nutritional_roles[0] | supports | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1793],"raw_equal":true},"docs_rows":[{"identifier":"cas:100789-83-1","line":1795,"mapping_status":"MAPPED","ontology_id":"cas:100789-83-1","preferred_term":"Sialyllacto-N-tetraose d"}],"identifier":"cas:100789-83-1","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"FALLBACK_REGISTRY","ontology_id":"cas:100789-83-1","ontology_label":"Sialyllacto-N-tetraose d","ontology_source":"CAS"},"preferred_term":"Sialyllacto-N-tetraose d","sssom_rows":[{"data_row":2503,"object_id":"cas:100789-83-1","object_label":"Sialyllacto-N-tetraose d","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Sialyllacto-N-tetraose_D","synonym_count":0} |
| ev-cf5bf3a0a7a88aee | reviews/structured/20261011T024638Z-mim-reconcile-all-batch-10/review.yaml; findings[finding_id=f-42b990d41a5cea09] | context_only | Predecessor structured review finding f-42b990d41a5cea09 in 20261011T024638Z-mim-reconcile-all-batch-10 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024638Z-mim-reconcile-all-batch-10.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-sialyllacto-n-tetraose-d
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Sialyllacto-N-tetraose_D (data/ingredients/mapped/Sialyllacto-N-tetraose_D.yaml)'
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
summary: Per-record structured review for Sialyllacto-N-tetraose_D (data/ingredients/mapped/Sialyllacto-N-tetraose_D.yaml,
  record-26bcbd3cfaf22637, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Sialyllacto-N-tetraose_D.yaml
    sha256: e69b97faa37600d48b65806a9eee8d965f85ecb9d33189651babc8e7068e102a
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
  - path: reports/yaml_record_review/Sialyllacto-N-tetraose_D.md
    sha256: 9def5c3a3ff0bc9417e84473c2c5a683ace74651960ba0219f01aa322d577f8d
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-26bcbd3cfaf22637
  path: data/ingredients/mapped/Sialyllacto-N-tetraose_D.yaml
  label: Sialyllacto-N-tetraose_D
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Sialyllacto-N-tetraose_D.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Sialyllacto-N-tetraose_D.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Sialyllacto-N-tetraose_D.yaml selected
    from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-26bcbd3cfaf22637
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-26bcbd3cfaf22637
  evidence_ids:
  - ev-1f70e03370f0e956
  - ev-e249d4b983ff3991
  - ev-bb5988ac1181252f
  - ev-2810100765fde752
  - ev-3aa1200e276e179e
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-26bcbd3cfaf22637
  evidence_ids:
  - ev-1f70e03370f0e956
  - ev-012fb96537b07a82
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024638Z-mim-reconcile-all-batch-10
    and semantic review dispositions on HEAD.
  target_ids:
  - record-26bcbd3cfaf22637
  evidence_ids:
  - ev-926ed9a85c736b29
  - ev-012fb96537b07a82
  - ev-cf5bf3a0a7a88aee
evidence:
- evidence_id: ev-1f70e03370f0e956
  kind: record_content
  reference: data/ingredients/mapped/Sialyllacto-N-tetraose_D.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1793],"raw_equal":true},"docs_rows":[{"identifier":"cas:100789-83-1","line":1795,"mapping_status":"MAPPED","ontology_id":"cas:100789-83-1","preferred_term":"Sialyllacto-N-tetraose
    d"}],"identifier":"cas:100789-83-1","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"FALLBACK_REGISTRY","ontology_id":"cas:100789-83-1","ontology_label":"Sialyllacto-N-tetraose
    d","ontology_source":"CAS"},"preferred_term":"Sialyllacto-N-tetraose d","sssom_rows":[{"data_row":2503,"object_id":"cas:100789-83-1","object_label":"Sialyllacto-N-tetraose
    d","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Sialyllacto-N-tetraose_D","synonym_count":0}'
  snapshot_sha256: e69b97faa37600d48b65806a9eee8d965f85ecb9d33189651babc8e7068e102a
- evidence_id: ev-e249d4b983ff3991
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1793]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-bb5988ac1181252f
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Sialyllacto-N-tetraose_D; data-row positions=[2503]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":2503,"object_id":"cas:100789-83-1","object_label":"Sialyllacto-N-tetraose
    d","other":"CAS:100789-83-1","predicate_id":"skos:exactMatch","subject_id":"MIM:Sialyllacto-N-tetraose_D","validation_method":"none|UNKNOWN_TERM|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-2810100765fde752
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1795]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"cas:100789-83-1","line":1795,"mapping_quality":"FALLBACK_REGISTRY","mapping_status":"MAPPED","media_count":"0","ontology_id":"cas:100789-83-1","preferred_term":"Sialyllacto-N-tetraose
    d","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-926ed9a85c736b29
  kind: prior_review
  reference: reports/yaml_record_review/Sialyllacto-N-tetraose_D.md
  locator: '`data/ingredients/mapped/Sialyllacto-N-tetraose_D.yaml`:2'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 9def5c3a3ff0bc9417e84473c2c5a683ace74651960ba0219f01aa322d577f8d
- evidence_id: ev-012fb96537b07a82
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1193,2048]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"e69b97faa37600d48b65806a9eee8d965f85ecb9d33189651babc8e7068e102a","finding_id":"SEM:a4bfda0d80d6e7579f9e","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"e69b97faa37600d48b65806a9eee8d965f85ecb9d33189651babc8e7068e102a","finding_id":"SEM:f0c3d3a41c1fde77ddf1","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-3aa1200e276e179e
  kind: record_content
  reference: data/ingredients/mapped/Sialyllacto-N-tetraose_D.yaml
  locator: nutritional_roles[0]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1793],"raw_equal":true},"docs_rows":[{"identifier":"cas:100789-83-1","line":1795,"mapping_status":"MAPPED","ontology_id":"cas:100789-83-1","preferred_term":"Sialyllacto-N-tetraose
    d"}],"identifier":"cas:100789-83-1","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"FALLBACK_REGISTRY","ontology_id":"cas:100789-83-1","ontology_label":"Sialyllacto-N-tetraose
    d","ontology_source":"CAS"},"preferred_term":"Sialyllacto-N-tetraose d","sssom_rows":[{"data_row":2503,"object_id":"cas:100789-83-1","object_label":"Sialyllacto-N-tetraose
    d","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Sialyllacto-N-tetraose_D","synonym_count":0}'
  snapshot_sha256: e69b97faa37600d48b65806a9eee8d965f85ecb9d33189651babc8e7068e102a
- evidence_id: ev-cf5bf3a0a7a88aee
  kind: prior_review
  reference: reviews/structured/20261011T024638Z-mim-reconcile-all-batch-10/review.yaml
  locator: findings[finding_id=f-42b990d41a5cea09]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-42b990d41a5cea09 in 20261011T024638Z-mim-reconcile-all-batch-10
  snapshot_sha256: 8c3aa2fca1269d1dbbf6117e85dea5b0de5047a8505841641245bd7ee99b936d
assessments:
- assessment_id: a-c79a57da5c610e5e
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-26bcbd3cfaf22637
  evidence_ids:
  - ev-1f70e03370f0e956
  - ev-e249d4b983ff3991
  - ev-bb5988ac1181252f
  - ev-2810100765fde752
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-7cdd729c5717c133
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-26bcbd3cfaf22637
  evidence_ids:
  - ev-926ed9a85c736b29
  - ev-1f70e03370f0e956
  - ev-012fb96537b07a82
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T13:59:34Z;
    reviewed SHA-256=e69b97faa37600d48b65806a9eee8d965f85ecb9d33189651babc8e7068e102a;
    current SHA-256=e69b97faa37600d48b65806a9eee8d965f85ecb9d33189651babc8e7068e102a;
    hash_changed=False. Reports=["reports/yaml_record_review/Sialyllacto-N-tetraose_D.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The CAS
    fallback identity, PubChem structure, and final SSSOM row pass, but CARBON_SOURCE
    is only provisional name-pattern inference.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-926ed9a85c736b29
    - ev-1f70e03370f0e956
  - name: legacy-native-ids
    value: '["SEM:a4bfda0d80d6e7579f9e","SEM:f0c3d3a41c1fde77ddf1"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-1f70e03370f0e956
    - ev-926ed9a85c736b29
    - ev-012fb96537b07a82
- assessment_id: a-3aa1200e276e179e
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-26bcbd3cfaf22637
  evidence_ids:
  - ev-926ed9a85c736b29
  - ev-3aa1200e276e179e
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-926ed9a85c736b29
    - ev-3aa1200e276e179e
findings:
- finding_id: rec-f-42b990d41a5cea09
  issue_key: mim-reconciliation-role-support-26bcbd3cfaf22637
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Sialyllacto-N-tetraose d'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-26bcbd3cfaf22637
  evidence_ids:
  - ev-926ed9a85c736b29
  - ev-3aa1200e276e179e
  - ev-cf5bf3a0a7a88aee
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Sialyllacto-N-tetraose_D.yaml
    role: maintained ingredient
  field_paths:
  - nutritional_roles[0]
  tags:
  - reconciliation
  - bundle-by-owner
  - role-support
  external_issues:
  - https://github.com/CultureBotAI/MediaIngredientMech/issues/718
  previous_occurrences:
  - repository: CultureBotAI/MediaIngredientMech
    review_id: 20261011T024638Z-mim-reconcile-all-batch-10
    finding_id: f-42b990d41a5cea09
actions:
- action_id: rec-action-42b990d41a5cea09
  description: 'Reassess prediction-only role support: Sialyllacto-N-tetraose d'
  finding_ids:
  - rec-f-42b990d41a5cea09
  target_ids:
  - record-26bcbd3cfaf22637
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Sialyllacto-N-tetraose_D.yaml
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
  with lineage to 20261011T024638Z-mim-reconcile-all-batch-10.
```
