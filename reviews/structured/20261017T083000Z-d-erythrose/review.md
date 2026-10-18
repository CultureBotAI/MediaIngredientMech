# Per-record structured review: D-erythrose (data/ingredients/mapped/D-erythrose.yaml)

- Review: 20261017T083000Z-d-erythrose
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for D-erythrose (data/ingredients/mapped/D-erythrose.yaml, record-d1cb2826675694b6, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/D-erythrose.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/D-erythrose.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-d1cb2826675694b6 | data/ingredients/mapped/D-erythrose.yaml | maintained | D-erythrose |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-d1cb2826675694b6 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-d1cb2826675694b6 | Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-d1cb2826675694b6 | Reconciled against predecessor batch review 20261011T024633Z-mim-reconcile-all-batch-05 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-d1cb2826675694b6.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-d1cb2826675694b6.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T13:33:32Z; reviewed SHA-256=a88ca4706c61451cbd11c5334ac4002438af9173af7e0f30f40e400f3a4c6f25; current SHA-256=a88ca4706c61451cbd11c5334ac4002438af9173af7e0f30f40e400f3a4c6f25; hash_changed=False. Reports=["reports/yaml_record_review/D-erythrose.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI identity, structure fields, 0/0 count, and final SSSOM synonym payload pass, but the carbon role is computational.

### Historical provisional-role concern

evidence: concern. Targets: record-d1cb2826675694b6.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-8ad3fc5c12a0ce5b: Reassess prediction-only role support: D-erythrose

major / open / confirmed; issue key: mim-reconciliation-role-support-d1cb2826675694b6.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-8ad3fc5c12a0ce5b

Reassess prediction-only role support: D-erythrose

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-fcbaac0c420b4eb4 | data/ingredients/mapped/D-erythrose.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[831],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:27904","line":833,"mapping_status":"MAPPED","ontology_id":"CHEBI:27904","preferred_term":"D-erythrose"}],"identifier":"CHEBI:27904","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:27904","ontology_label":"D-erythrose","ontology_source":"CHEBI"},"preferred_term":"D-erythrose","sssom_rows":[{"data_row":927,"object_id":"CHEBI:27904","object_label":"D-erythrose","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:D-erythrose","synonym_count":2} |
| ev-a2d5132e9d2ee200 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [831] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-6fd0d91976254bbd | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:D-erythrose; data-row positions=[927] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":927,"object_id":"CHEBI:27904","object_label":"D-erythrose","other":"(2R,3R)-2,3,4-trihydroxybutanal&#124;D-erythro-tetrose&#124;CAS:583-50-6","predicate_id":"skos:exactMatch","subject_id":"MIM:D-erythrose","validation_method":"OAK+OLS:chebi&#124;CONFIRMED&#124;2026-07-07"}] |
| ev-d37784ae6303c6b4 | docs/data/mapped_ingredients.csv; CSV lines=[833] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:27904","line":833,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:27904","preferred_term":"D-erythrose","total_occurrences":"0"}] |
| ev-05cee8c8c917cd05 | reports/yaml_record_review/D-erythrose.md; &#96;data/ingredients/mapped/D-erythrose.yaml&#96;:2; Verdict:4; Identity:12; Validation:25; Evidence:45; Completeness:60; Recommended Edits:68 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-92c3ebbc3acbaa6e | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[491,1499] | context_only | [{"current_record_sha256":"a88ca4706c61451cbd11c5334ac4002438af9173af7e0f30f40e400f3a4c6f25","finding_id":"SEM:5225106a5a9445136f3b","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"a88ca4706c61451cbd11c5334ac4002438af9173af7e0f30f40e400f3a4c6f25","finding_id":"SEM:9d95180b18aa58fa1899","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-78b43b44f77ca659 | data/ingredients/mapped/D-erythrose.yaml; nutritional_roles[0] | supports | Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION: [{"field":"nutritional_roles[0]","role":{"confidence":0.7,"evidence":[{"curator_note":"Provisional role inferred from CHEBI is_a/has_role closure; review recommended.","reference_text":"Inferred from CHEBI ancestry: subclass/has_role of CHEBI:16646 (carbohydrate)","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"CARBON_SOURCE"}}] |
| ev-f3806584f24d9b61 | reviews/structured/20261011T024633Z-mim-reconcile-all-batch-05/review.yaml; findings[finding_id=f-8ad3fc5c12a0ce5b] | context_only | Predecessor structured review finding f-8ad3fc5c12a0ce5b in 20261011T024633Z-mim-reconcile-all-batch-05 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024633Z-mim-reconcile-all-batch-05.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-d-erythrose
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: D-erythrose (data/ingredients/mapped/D-erythrose.yaml)'
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
summary: Per-record structured review for D-erythrose (data/ingredients/mapped/D-erythrose.yaml,
  record-d1cb2826675694b6, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/D-erythrose.yaml
    sha256: a88ca4706c61451cbd11c5334ac4002438af9173af7e0f30f40e400f3a4c6f25
    role: target
  - path: reviews/structured/20261011T024633Z-mim-reconcile-all-batch-05/review.yaml
    sha256: 7549030a5b50ed98868ff3497507fdfbfecd07cd858c76738f734521fa9d3603
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
  - path: reports/yaml_record_review/D-erythrose.md
    sha256: 7df28a310204f024c620b03fba4661fd8ada1fbd30cf531965b6fb88104dae95
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-d1cb2826675694b6
  path: data/ingredients/mapped/D-erythrose.yaml
  label: D-erythrose
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/D-erythrose.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/D-erythrose.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/D-erythrose.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-d1cb2826675694b6
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-d1cb2826675694b6
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-d1cb2826675694b6
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024633Z-mim-reconcile-all-batch-05
    and semantic review dispositions on HEAD.
  target_ids:
  - record-d1cb2826675694b6
evidence:
- evidence_id: ev-fcbaac0c420b4eb4
  kind: record_content
  reference: data/ingredients/mapped/D-erythrose.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[831],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:27904","line":833,"mapping_status":"MAPPED","ontology_id":"CHEBI:27904","preferred_term":"D-erythrose"}],"identifier":"CHEBI:27904","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:27904","ontology_label":"D-erythrose","ontology_source":"CHEBI"},"preferred_term":"D-erythrose","sssom_rows":[{"data_row":927,"object_id":"CHEBI:27904","object_label":"D-erythrose","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:D-erythrose","synonym_count":2}'
  snapshot_sha256: a88ca4706c61451cbd11c5334ac4002438af9173af7e0f30f40e400f3a4c6f25
- evidence_id: ev-a2d5132e9d2ee200
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [831]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-6fd0d91976254bbd
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:D-erythrose; data-row positions=[927]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":927,"object_id":"CHEBI:27904","object_label":"D-erythrose","other":"(2R,3R)-2,3,4-trihydroxybutanal|D-erythro-tetrose|CAS:583-50-6","predicate_id":"skos:exactMatch","subject_id":"MIM:D-erythrose","validation_method":"OAK+OLS:chebi|CONFIRMED|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-d37784ae6303c6b4
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[833]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:27904","line":833,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:27904","preferred_term":"D-erythrose","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-05cee8c8c917cd05
  kind: prior_review
  reference: reports/yaml_record_review/D-erythrose.md
  locator: '`data/ingredients/mapped/D-erythrose.yaml`:2; Verdict:4; Identity:12;
    Validation:25; Evidence:45; Completeness:60; Recommended Edits:68'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 7df28a310204f024c620b03fba4661fd8ada1fbd30cf531965b6fb88104dae95
  quote: "Recommended Edits:\n- In `data/ingredients/mapped/D-erythrose.yaml`, either\
    \ replace the\n  computational `CARBON_SOURCE` evidence with direct, source-backed\
    \ media-role\n  evidence for D-erythrose, or remove the role facet; then rerun\
    \ strict\n  validation and the final SSSOM gates."
- evidence_id: ev-92c3ebbc3acbaa6e
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[491,1499]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"a88ca4706c61451cbd11c5334ac4002438af9173af7e0f30f40e400f3a4c6f25","finding_id":"SEM:5225106a5a9445136f3b","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"a88ca4706c61451cbd11c5334ac4002438af9173af7e0f30f40e400f3a4c6f25","finding_id":"SEM:9d95180b18aa58fa1899","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-78b43b44f77ca659
  kind: record_content
  reference: data/ingredients/mapped/D-erythrose.yaml
  locator: nutritional_roles[0]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION:
    [{"field":"nutritional_roles[0]","role":{"confidence":0.7,"evidence":[{"curator_note":"Provisional
    role inferred from CHEBI is_a/has_role closure; review recommended.","reference_text":"Inferred
    from CHEBI ancestry: subclass/has_role of CHEBI:16646 (carbohydrate)","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"CARBON_SOURCE"}}]'
  snapshot_sha256: a88ca4706c61451cbd11c5334ac4002438af9173af7e0f30f40e400f3a4c6f25
- evidence_id: ev-f3806584f24d9b61
  kind: prior_review
  reference: reviews/structured/20261011T024633Z-mim-reconcile-all-batch-05/review.yaml
  locator: findings[finding_id=f-8ad3fc5c12a0ce5b]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-8ad3fc5c12a0ce5b in 20261011T024633Z-mim-reconcile-all-batch-05
  snapshot_sha256: 7549030a5b50ed98868ff3497507fdfbfecd07cd858c76738f734521fa9d3603
assessments:
- assessment_id: a-ad204b995006fd3e
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-d1cb2826675694b6
  evidence_ids:
  - ev-fcbaac0c420b4eb4
  - ev-a2d5132e9d2ee200
  - ev-6fd0d91976254bbd
  - ev-d37784ae6303c6b4
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-edabad6ff6b5588b
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-d1cb2826675694b6
  evidence_ids:
  - ev-05cee8c8c917cd05
  - ev-fcbaac0c420b4eb4
  - ev-92c3ebbc3acbaa6e
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T13:33:32Z;
    reviewed SHA-256=a88ca4706c61451cbd11c5334ac4002438af9173af7e0f30f40e400f3a4c6f25;
    current SHA-256=a88ca4706c61451cbd11c5334ac4002438af9173af7e0f30f40e400f3a4c6f25;
    hash_changed=False. Reports=["reports/yaml_record_review/D-erythrose.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The exact CHEBI
    identity, structure fields, 0/0 count, and final SSSOM synonym payload pass, but
    the carbon role is computational.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-05cee8c8c917cd05
    - ev-fcbaac0c420b4eb4
  - name: legacy-native-ids
    value: '["SEM:5225106a5a9445136f3b","SEM:9d95180b18aa58fa1899"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-fcbaac0c420b4eb4
    - ev-05cee8c8c917cd05
    - ev-92c3ebbc3acbaa6e
- assessment_id: a-78b43b44f77ca659
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-d1cb2826675694b6
  evidence_ids:
  - ev-05cee8c8c917cd05
  - ev-78b43b44f77ca659
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-05cee8c8c917cd05
    - ev-78b43b44f77ca659
findings:
- finding_id: rec-f-8ad3fc5c12a0ce5b
  issue_key: mim-reconciliation-role-support-d1cb2826675694b6
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: D-erythrose'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-d1cb2826675694b6
  evidence_ids:
  - ev-05cee8c8c917cd05
  - ev-78b43b44f77ca659
  - ev-f3806584f24d9b61
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/D-erythrose.yaml
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
    review_id: 20261011T024633Z-mim-reconcile-all-batch-05
    finding_id: f-8ad3fc5c12a0ce5b
actions:
- action_id: rec-action-8ad3fc5c12a0ce5b
  description: 'Reassess prediction-only role support: D-erythrose'
  finding_ids:
  - rec-f-8ad3fc5c12a0ce5b
  target_ids:
  - record-d1cb2826675694b6
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/D-erythrose.yaml
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
  with lineage to 20261011T024633Z-mim-reconcile-all-batch-05.
```
