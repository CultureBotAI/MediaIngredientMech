# Per-record structured review: Pyruvate (data/ingredients/mapped/Pyruvate.yaml)

- Review: 20261017T083000Z-pyruvate
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Pyruvate (data/ingredients/mapped/Pyruvate.yaml, record-16de1463f5ba062b, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Pyruvate.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Pyruvate.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-16de1463f5ba062b | data/ingredients/mapped/Pyruvate.yaml | maintained | Pyruvate |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-16de1463f5ba062b | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-16de1463f5ba062b | Role assertions on nutritional_roles[0], nutritional_roles[1] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-16de1463f5ba062b | Reconciled against predecessor batch review 20261011T024638Z-mim-reconcile-all-batch-10 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-16de1463f5ba062b.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-16de1463f5ba062b.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T11:22:00Z; reviewed SHA-256=c1cb5e1036729676abf5b6a7e0b6d2a0bb2f62c2dc8c0e662c082488986322e1; current SHA-256=c1cb5e1036729676abf5b6a7e0b6d2a0bb2f62c2dc8c0e662c082488986322e1; hash_changed=False. Reports=["reports/yaml_record_review/Pyruvate.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI:15361 pyruvate identity passes, but CARBON_SOURCE and ENERGY_SOURCE are provisional.

### Historical provisional-role concern

evidence: concern. Targets: record-16de1463f5ba062b.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-8695f8c1be2e183f: Reassess prediction-only role support: Pyruvate

major / open / confirmed; issue key: mim-reconciliation-role-support-16de1463f5ba062b.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-8695f8c1be2e183f

Reassess prediction-only role support: Pyruvate

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-82daa9cde6c28d1f | data/ingredients/mapped/Pyruvate.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1733],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:15361","line":1735,"mapping_status":"MAPPED","ontology_id":"CHEBI:15361","preferred_term":"Pyruvate"}],"identifier":"CHEBI:15361","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":30,"edge_count":30,"occurrences":30},"occurrence_statistics":{"media_count":30,"total_occurrences":30},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:15361","ontology_label":"pyruvate","ontology_source":"CHEBI"},"preferred_term":"Pyruvate","sssom_rows":[{"data_row":2396,"object_id":"CHEBI:15361","object_label":"pyruvate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Pyruvate","synonym_count":2} |
| ev-22bfcfd327e73248 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1733] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-91bc7cf132e5ef74 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Pyruvate; data-row positions=[2396] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":2396,"object_id":"CHEBI:15361","object_label":"pyruvate","other":"2-oxopropanoate&#124;CAS:57-60-3","predicate_id":"skos:exactMatch","subject_id":"MIM:Pyruvate","validation_method":"OAK+OLS:chebi&#124;CONFIRMED&#124;2026-07-07"}] |
| ev-4ed6cef692505e5d | docs/data/mapped_ingredients.csv; CSV lines=[1735] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:15361","line":1735,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"30","ontology_id":"CHEBI:15361","preferred_term":"Pyruvate","total_occurrences":"30"}] |
| ev-7d43e51903c19783 | reports/yaml_record_review/Pyruvate.md; &#96;data/ingredients/mapped/Pyruvate.yaml&#96;:2 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-ea3eedeea74a21e0 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1157,1758,1929] | context_only | [{"current_record_sha256":"c1cb5e1036729676abf5b6a7e0b6d2a0bb2f62c2dc8c0e662c082488986322e1","finding_id":"SEM:808e8ab3bff2a49506d0","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"c1cb5e1036729676abf5b6a7e0b6d2a0bb2f62c2dc8c0e662c082488986322e1","finding_id":"SEM:e6fa84352d4865488611","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"c1cb5e1036729676abf5b6a7e0b6d2a0bb2f62c2dc8c0e662c082488986322e1","finding_id":"SEM:4668380336897bcad7ec","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-c6c425793a4e8c48 | data/ingredients/mapped/Pyruvate.yaml; nutritional_roles[0], nutritional_roles[1] | supports | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1733],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:15361","line":1735,"mapping_status":"MAPPED","ontology_id":"CHEBI:15361","preferred_term":"Pyruvate"}],"identifier":"CHEBI:15361","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":30,"edge_count":30,"occurrences":30},"occurrence_statistics":{"media_count":30,"total_occurrences":30},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:15361","ontology_label":"pyruvate","ontology_source":"CHEBI"},"preferred_term":"Pyruvate","sssom_rows":[{"data_row":2396,"object_id":"CHEBI:15361","object_label":"pyruvate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Pyruvate","synonym_count":2} |
| ev-b5849c35ff0487ac | reviews/structured/20261011T024638Z-mim-reconcile-all-batch-10/review.yaml; findings[finding_id=f-8695f8c1be2e183f] | context_only | Predecessor structured review finding f-8695f8c1be2e183f in 20261011T024638Z-mim-reconcile-all-batch-10 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024638Z-mim-reconcile-all-batch-10.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-pyruvate
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Pyruvate (data/ingredients/mapped/Pyruvate.yaml)'
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
summary: Per-record structured review for Pyruvate (data/ingredients/mapped/Pyruvate.yaml,
  record-16de1463f5ba062b, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Pyruvate.yaml
    sha256: c1cb5e1036729676abf5b6a7e0b6d2a0bb2f62c2dc8c0e662c082488986322e1
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
  - path: reports/yaml_record_review/Pyruvate.md
    sha256: 82968aa05a82a8a49eff30128bb844ed833377eae7f02644df689376b78593c6
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-16de1463f5ba062b
  path: data/ingredients/mapped/Pyruvate.yaml
  label: Pyruvate
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Pyruvate.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Pyruvate.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Pyruvate.yaml selected from full-corpus
    review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-16de1463f5ba062b
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-16de1463f5ba062b
  evidence_ids:
  - ev-82daa9cde6c28d1f
  - ev-22bfcfd327e73248
  - ev-91bc7cf132e5ef74
  - ev-4ed6cef692505e5d
  - ev-c6c425793a4e8c48
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0], nutritional_roles[1] rely only
    on COMPUTATIONAL_PREDICTION or empty evidence.
  target_ids:
  - record-16de1463f5ba062b
  evidence_ids:
  - ev-82daa9cde6c28d1f
  - ev-ea3eedeea74a21e0
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024638Z-mim-reconcile-all-batch-10
    and semantic review dispositions on HEAD.
  target_ids:
  - record-16de1463f5ba062b
  evidence_ids:
  - ev-7d43e51903c19783
  - ev-ea3eedeea74a21e0
  - ev-b5849c35ff0487ac
evidence:
- evidence_id: ev-82daa9cde6c28d1f
  kind: record_content
  reference: data/ingredients/mapped/Pyruvate.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1733],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:15361","line":1735,"mapping_status":"MAPPED","ontology_id":"CHEBI:15361","preferred_term":"Pyruvate"}],"identifier":"CHEBI:15361","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":30,"edge_count":30,"occurrences":30},"occurrence_statistics":{"media_count":30,"total_occurrences":30},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:15361","ontology_label":"pyruvate","ontology_source":"CHEBI"},"preferred_term":"Pyruvate","sssom_rows":[{"data_row":2396,"object_id":"CHEBI:15361","object_label":"pyruvate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Pyruvate","synonym_count":2}'
  snapshot_sha256: c1cb5e1036729676abf5b6a7e0b6d2a0bb2f62c2dc8c0e662c082488986322e1
- evidence_id: ev-22bfcfd327e73248
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1733]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-91bc7cf132e5ef74
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Pyruvate; data-row positions=[2396]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":2396,"object_id":"CHEBI:15361","object_label":"pyruvate","other":"2-oxopropanoate|CAS:57-60-3","predicate_id":"skos:exactMatch","subject_id":"MIM:Pyruvate","validation_method":"OAK+OLS:chebi|CONFIRMED|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-4ed6cef692505e5d
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1735]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:15361","line":1735,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"30","ontology_id":"CHEBI:15361","preferred_term":"Pyruvate","total_occurrences":"30"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-7d43e51903c19783
  kind: prior_review
  reference: reports/yaml_record_review/Pyruvate.md
  locator: '`data/ingredients/mapped/Pyruvate.yaml`:2'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 82968aa05a82a8a49eff30128bb844ed833377eae7f02644df689376b78593c6
- evidence_id: ev-ea3eedeea74a21e0
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1157,1758,1929]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"c1cb5e1036729676abf5b6a7e0b6d2a0bb2f62c2dc8c0e662c082488986322e1","finding_id":"SEM:808e8ab3bff2a49506d0","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"c1cb5e1036729676abf5b6a7e0b6d2a0bb2f62c2dc8c0e662c082488986322e1","finding_id":"SEM:e6fa84352d4865488611","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"c1cb5e1036729676abf5b6a7e0b6d2a0bb2f62c2dc8c0e662c082488986322e1","finding_id":"SEM:4668380336897bcad7ec","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-c6c425793a4e8c48
  kind: record_content
  reference: data/ingredients/mapped/Pyruvate.yaml
  locator: nutritional_roles[0], nutritional_roles[1]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1733],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:15361","line":1735,"mapping_status":"MAPPED","ontology_id":"CHEBI:15361","preferred_term":"Pyruvate"}],"identifier":"CHEBI:15361","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":30,"edge_count":30,"occurrences":30},"occurrence_statistics":{"media_count":30,"total_occurrences":30},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:15361","ontology_label":"pyruvate","ontology_source":"CHEBI"},"preferred_term":"Pyruvate","sssom_rows":[{"data_row":2396,"object_id":"CHEBI:15361","object_label":"pyruvate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Pyruvate","synonym_count":2}'
  snapshot_sha256: c1cb5e1036729676abf5b6a7e0b6d2a0bb2f62c2dc8c0e662c082488986322e1
- evidence_id: ev-b5849c35ff0487ac
  kind: prior_review
  reference: reviews/structured/20261011T024638Z-mim-reconcile-all-batch-10/review.yaml
  locator: findings[finding_id=f-8695f8c1be2e183f]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-8695f8c1be2e183f in 20261011T024638Z-mim-reconcile-all-batch-10
  snapshot_sha256: 8c3aa2fca1269d1dbbf6117e85dea5b0de5047a8505841641245bd7ee99b936d
assessments:
- assessment_id: a-2abdd6519102224b
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-16de1463f5ba062b
  evidence_ids:
  - ev-82daa9cde6c28d1f
  - ev-22bfcfd327e73248
  - ev-91bc7cf132e5ef74
  - ev-4ed6cef692505e5d
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-9e24c15915a4c475
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-16de1463f5ba062b
  evidence_ids:
  - ev-7d43e51903c19783
  - ev-82daa9cde6c28d1f
  - ev-ea3eedeea74a21e0
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T11:22:00Z;
    reviewed SHA-256=c1cb5e1036729676abf5b6a7e0b6d2a0bb2f62c2dc8c0e662c082488986322e1;
    current SHA-256=c1cb5e1036729676abf5b6a7e0b6d2a0bb2f62c2dc8c0e662c082488986322e1;
    hash_changed=False. Reports=["reports/yaml_record_review/Pyruvate.md"]. Full reports,
    including older originals behind refresh floors, are hashed inputs. Repeated refresh
    allegations are not counted as new defects. The narrative group is not a count
    of distinct scientific findings. Latest manifest note: The exact CHEBI:15361 pyruvate
    identity passes, but CARBON_SOURCE and ENERGY_SOURCE are provisional.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-7d43e51903c19783
    - ev-82daa9cde6c28d1f
  - name: legacy-native-ids
    value: '["SEM:808e8ab3bff2a49506d0","SEM:e6fa84352d4865488611","SEM:4668380336897bcad7ec"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-82daa9cde6c28d1f
    - ev-7d43e51903c19783
    - ev-ea3eedeea74a21e0
- assessment_id: a-c6c425793a4e8c48
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-16de1463f5ba062b
  evidence_ids:
  - ev-7d43e51903c19783
  - ev-c6c425793a4e8c48
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-7d43e51903c19783
    - ev-c6c425793a4e8c48
findings:
- finding_id: rec-f-8695f8c1be2e183f
  issue_key: mim-reconciliation-role-support-16de1463f5ba062b
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Pyruvate'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-16de1463f5ba062b
  evidence_ids:
  - ev-7d43e51903c19783
  - ev-c6c425793a4e8c48
  - ev-b5849c35ff0487ac
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Pyruvate.yaml
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
    review_id: 20261011T024638Z-mim-reconcile-all-batch-10
    finding_id: f-8695f8c1be2e183f
actions:
- action_id: rec-action-8695f8c1be2e183f
  description: 'Reassess prediction-only role support: Pyruvate'
  finding_ids:
  - rec-f-8695f8c1be2e183f
  target_ids:
  - record-16de1463f5ba062b
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Pyruvate.yaml
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
