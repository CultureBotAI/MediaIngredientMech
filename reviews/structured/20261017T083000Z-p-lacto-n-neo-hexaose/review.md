# Per-record structured review: P-lacto-N-neo-hexaose (data/ingredients/mapped/P-lacto-N-neo-hexaose.yaml)

- Review: 20261017T083000Z-p-lacto-n-neo-hexaose
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for P-lacto-N-neo-hexaose (data/ingredients/mapped/P-lacto-N-neo-hexaose.yaml, record-fc1d28acbb122abf, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/P-lacto-N-neo-hexaose.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/P-lacto-N-neo-hexaose.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-fc1d28acbb122abf | data/ingredients/mapped/P-lacto-N-neo-hexaose.yaml | maintained | P-lacto-N-neo-hexaose |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-fc1d28acbb122abf | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-fc1d28acbb122abf | Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-fc1d28acbb122abf | Reconciled against predecessor batch review 20261011T024637Z-mim-reconcile-all-batch-09 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-fc1d28acbb122abf.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-fc1d28acbb122abf.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T08:05:42Z; reviewed SHA-256=ce65952dd839e7457fc89c9a85e2407c5cbce33d308c780e4abc73c98bd7d0c2; current SHA-256=ce65952dd839e7457fc89c9a85e2407c5cbce33d308c780e4abc73c98bd7d0c2; hash_changed=False. Reports=["reports/yaml_record_review/P-lacto-N-neo-hexaose.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The CAS 64309-00-8 fallback identity passes, but CARBON_SOURCE is only provisional.

### Historical provisional-role concern

evidence: concern. Targets: record-fc1d28acbb122abf.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-242bbd06bac59ce1: Reassess prediction-only role support: p-lacto-N-neo-hexaose

major / open / confirmed; issue key: mim-reconciliation-role-support-fc1d28acbb122abf.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-242bbd06bac59ce1

Reassess prediction-only role support: p-lacto-N-neo-hexaose

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-eaa6fa8e6d313ed4 | data/ingredients/mapped/P-lacto-N-neo-hexaose.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1604],"raw_equal":true},"docs_rows":[{"identifier":"cas:64309-00-8","line":1606,"mapping_status":"MAPPED","ontology_id":"cas:64309-00-8","preferred_term":"p-lacto-N-neo-hexaose"}],"identifier":"cas:64309-00-8","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"FALLBACK_REGISTRY","ontology_id":"cas:64309-00-8","ontology_label":"p-lacto-N-neo-hexaose","ontology_source":"CAS"},"preferred_term":"p-lacto-N-neo-hexaose","sssom_rows":[{"data_row":2168,"object_id":"cas:64309-00-8","object_label":"p-lacto-N-neo-hexaose","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:P-lacto-N-neo-hexaose","synonym_count":0} |
| ev-85712cc5df93ab71 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1604] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-14f8c8455445aafb | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:P-lacto-N-neo-hexaose; data-row positions=[2168] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":2168,"object_id":"cas:64309-00-8","object_label":"p-lacto-N-neo-hexaose","other":"CAS:64309-00-8","predicate_id":"skos:exactMatch","subject_id":"MIM:P-lacto-N-neo-hexaose","validation_method":"none&#124;UNKNOWN_TERM&#124;2026-07-07"}] |
| ev-17e2235abf673561 | docs/data/mapped_ingredients.csv; CSV lines=[1606] | supports | Published identity and count rows inspected: [{"identifier":"cas:64309-00-8","line":1606,"mapping_quality":"FALLBACK_REGISTRY","mapping_status":"MAPPED","media_count":"0","ontology_id":"cas:64309-00-8","preferred_term":"p-lacto-N-neo-hexaose","total_occurrences":"0"}] |
| ev-3cce0bb930ce2f1d | reports/yaml_record_review/P-lacto-N-neo-hexaose.md; &#96;data/ingredients/mapped/P-lacto-N-neo-hexaose.yaml&#96;:2; Verdict:4; Identity:10; Validation:21; Evidence:29; Completeness:45; Recommended Edits:52 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-d52341c94bbf840f | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1086,1747] | context_only | [{"current_record_sha256":"ce65952dd839e7457fc89c9a85e2407c5cbce33d308c780e4abc73c98bd7d0c2","finding_id":"SEM:9cd1bbedfede7a2771b2","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"ce65952dd839e7457fc89c9a85e2407c5cbce33d308c780e4abc73c98bd7d0c2","finding_id":"SEM:ffc0d4d6f3ad596d2c0d","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-37baf30b6f44ac4e | data/ingredients/mapped/P-lacto-N-neo-hexaose.yaml; nutritional_roles[0] | supports | Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION: [{"field":"nutritional_roles[0]","role":{"confidence":0.8,"evidence":[{"curator_note":"Provisional role from a curated name-pattern rule; review recommended.","reference_text":"Inferred from curated media-role name pattern","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"CARBON_SOURCE"}}] |
| ev-fe4017538a592597 | reviews/structured/20261011T024637Z-mim-reconcile-all-batch-09/review.yaml; findings[finding_id=f-242bbd06bac59ce1] | context_only | Predecessor structured review finding f-242bbd06bac59ce1 in 20261011T024637Z-mim-reconcile-all-batch-09 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024637Z-mim-reconcile-all-batch-09.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-p-lacto-n-neo-hexaose
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: P-lacto-N-neo-hexaose (data/ingredients/mapped/P-lacto-N-neo-hexaose.yaml)'
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
summary: Per-record structured review for P-lacto-N-neo-hexaose (data/ingredients/mapped/P-lacto-N-neo-hexaose.yaml,
  record-fc1d28acbb122abf, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/P-lacto-N-neo-hexaose.yaml
    sha256: ce65952dd839e7457fc89c9a85e2407c5cbce33d308c780e4abc73c98bd7d0c2
    role: target
  - path: reviews/structured/20261011T024637Z-mim-reconcile-all-batch-09/review.yaml
    sha256: cf46750874f1303863883723934bbe8b09ece8d62b1785ceab64bb0342a3cf11
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
  - path: reports/yaml_record_review/P-lacto-N-neo-hexaose.md
    sha256: 20153f8ea3c3cbc79ba1830d453fef732d4543ae9a1a408b6720b1b782ce4780
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-fc1d28acbb122abf
  path: data/ingredients/mapped/P-lacto-N-neo-hexaose.yaml
  label: P-lacto-N-neo-hexaose
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/P-lacto-N-neo-hexaose.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/P-lacto-N-neo-hexaose.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/P-lacto-N-neo-hexaose.yaml selected
    from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-fc1d28acbb122abf
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-fc1d28acbb122abf
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-fc1d28acbb122abf
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024637Z-mim-reconcile-all-batch-09
    and semantic review dispositions on HEAD.
  target_ids:
  - record-fc1d28acbb122abf
evidence:
- evidence_id: ev-eaa6fa8e6d313ed4
  kind: record_content
  reference: data/ingredients/mapped/P-lacto-N-neo-hexaose.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1604],"raw_equal":true},"docs_rows":[{"identifier":"cas:64309-00-8","line":1606,"mapping_status":"MAPPED","ontology_id":"cas:64309-00-8","preferred_term":"p-lacto-N-neo-hexaose"}],"identifier":"cas:64309-00-8","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"FALLBACK_REGISTRY","ontology_id":"cas:64309-00-8","ontology_label":"p-lacto-N-neo-hexaose","ontology_source":"CAS"},"preferred_term":"p-lacto-N-neo-hexaose","sssom_rows":[{"data_row":2168,"object_id":"cas:64309-00-8","object_label":"p-lacto-N-neo-hexaose","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:P-lacto-N-neo-hexaose","synonym_count":0}'
  snapshot_sha256: ce65952dd839e7457fc89c9a85e2407c5cbce33d308c780e4abc73c98bd7d0c2
- evidence_id: ev-85712cc5df93ab71
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1604]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-14f8c8455445aafb
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:P-lacto-N-neo-hexaose; data-row positions=[2168]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":2168,"object_id":"cas:64309-00-8","object_label":"p-lacto-N-neo-hexaose","other":"CAS:64309-00-8","predicate_id":"skos:exactMatch","subject_id":"MIM:P-lacto-N-neo-hexaose","validation_method":"none|UNKNOWN_TERM|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-17e2235abf673561
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1606]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"cas:64309-00-8","line":1606,"mapping_quality":"FALLBACK_REGISTRY","mapping_status":"MAPPED","media_count":"0","ontology_id":"cas:64309-00-8","preferred_term":"p-lacto-N-neo-hexaose","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-3cce0bb930ce2f1d
  kind: prior_review
  reference: reports/yaml_record_review/P-lacto-N-neo-hexaose.md
  locator: '`data/ingredients/mapped/P-lacto-N-neo-hexaose.yaml`:2; Verdict:4; Identity:10;
    Validation:21; Evidence:29; Completeness:45; Recommended Edits:52'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 20153f8ea3c3cbc79ba1830d453fef732d4543ae9a1a408b6720b1b782ce4780
  quote: "Recommended Edits:\n- Major: in `data/ingredients/mapped/P-lacto-N-neo-hexaose.yaml`,\
    \ either\n  replace `nutritional_roles.CARBON_SOURCE` with cited experimental\
    \ or recipe\n  evidence, or remove the provisional role facet until source-backed\
    \ role\n  evidence is curated."
- evidence_id: ev-d52341c94bbf840f
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1086,1747]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"ce65952dd839e7457fc89c9a85e2407c5cbce33d308c780e4abc73c98bd7d0c2","finding_id":"SEM:9cd1bbedfede7a2771b2","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"ce65952dd839e7457fc89c9a85e2407c5cbce33d308c780e4abc73c98bd7d0c2","finding_id":"SEM:ffc0d4d6f3ad596d2c0d","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-37baf30b6f44ac4e
  kind: record_content
  reference: data/ingredients/mapped/P-lacto-N-neo-hexaose.yaml
  locator: nutritional_roles[0]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION:
    [{"field":"nutritional_roles[0]","role":{"confidence":0.8,"evidence":[{"curator_note":"Provisional
    role from a curated name-pattern rule; review recommended.","reference_text":"Inferred
    from curated media-role name pattern","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"CARBON_SOURCE"}}]'
  snapshot_sha256: ce65952dd839e7457fc89c9a85e2407c5cbce33d308c780e4abc73c98bd7d0c2
- evidence_id: ev-fe4017538a592597
  kind: prior_review
  reference: reviews/structured/20261011T024637Z-mim-reconcile-all-batch-09/review.yaml
  locator: findings[finding_id=f-242bbd06bac59ce1]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-242bbd06bac59ce1 in 20261011T024637Z-mim-reconcile-all-batch-09
  snapshot_sha256: cf46750874f1303863883723934bbe8b09ece8d62b1785ceab64bb0342a3cf11
assessments:
- assessment_id: a-e14f8a72130b7dc1
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-fc1d28acbb122abf
  evidence_ids:
  - ev-eaa6fa8e6d313ed4
  - ev-85712cc5df93ab71
  - ev-14f8c8455445aafb
  - ev-17e2235abf673561
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-35a4b621a5098f93
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-fc1d28acbb122abf
  evidence_ids:
  - ev-3cce0bb930ce2f1d
  - ev-eaa6fa8e6d313ed4
  - ev-d52341c94bbf840f
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T08:05:42Z;
    reviewed SHA-256=ce65952dd839e7457fc89c9a85e2407c5cbce33d308c780e4abc73c98bd7d0c2;
    current SHA-256=ce65952dd839e7457fc89c9a85e2407c5cbce33d308c780e4abc73c98bd7d0c2;
    hash_changed=False. Reports=["reports/yaml_record_review/P-lacto-N-neo-hexaose.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The CAS
    64309-00-8 fallback identity passes, but CARBON_SOURCE is only provisional.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-3cce0bb930ce2f1d
    - ev-eaa6fa8e6d313ed4
  - name: legacy-native-ids
    value: '["SEM:9cd1bbedfede7a2771b2","SEM:ffc0d4d6f3ad596d2c0d"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-eaa6fa8e6d313ed4
    - ev-3cce0bb930ce2f1d
    - ev-d52341c94bbf840f
- assessment_id: a-37baf30b6f44ac4e
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-fc1d28acbb122abf
  evidence_ids:
  - ev-3cce0bb930ce2f1d
  - ev-37baf30b6f44ac4e
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-3cce0bb930ce2f1d
    - ev-37baf30b6f44ac4e
findings:
- finding_id: rec-f-242bbd06bac59ce1
  issue_key: mim-reconciliation-role-support-fc1d28acbb122abf
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: p-lacto-N-neo-hexaose'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-fc1d28acbb122abf
  evidence_ids:
  - ev-3cce0bb930ce2f1d
  - ev-37baf30b6f44ac4e
  - ev-fe4017538a592597
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/P-lacto-N-neo-hexaose.yaml
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
    review_id: 20261011T024637Z-mim-reconcile-all-batch-09
    finding_id: f-242bbd06bac59ce1
actions:
- action_id: rec-action-242bbd06bac59ce1
  description: 'Reassess prediction-only role support: p-lacto-N-neo-hexaose'
  finding_ids:
  - rec-f-242bbd06bac59ce1
  target_ids:
  - record-fc1d28acbb122abf
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/P-lacto-N-neo-hexaose.yaml
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
  with lineage to 20261011T024637Z-mim-reconcile-all-batch-09.
```
