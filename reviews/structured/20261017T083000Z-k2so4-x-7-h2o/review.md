# Per-record structured review: K2so4_X_7_H2o (data/ingredients/mapped/K2so4_X_7_H2o.yaml)

- Review: 20261017T083000Z-k2so4-x-7-h2o
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for K2so4_X_7_H2o (data/ingredients/mapped/K2so4_X_7_H2o.yaml, record-11e5db9256585234, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/K2so4_X_7_H2o.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/K2so4_X_7_H2o.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-11e5db9256585234 | data/ingredients/mapped/K2so4_X_7_H2o.yaml | maintained | K2so4_X_7_H2o |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-11e5db9256585234 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-11e5db9256585234 | Role assertions on nutritional_roles[0], nutritional_roles[1] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-11e5db9256585234 | Reconciled against predecessor batch review 20261011T024635Z-mim-reconcile-all-batch-07 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-11e5db9256585234.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-11e5db9256585234.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T21:26:49Z; reviewed SHA-256=06849d90807f1547a48c88de5dc022b466ae9b506efd08fb6929b1b6192b3412; current SHA-256=06849d90807f1547a48c88de5dc022b466ae9b506efd08fb6929b1b6192b3412; hash_changed=False. Reports=["reports/yaml_record_review/K2so4_X_7_H2o.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The #344 local malformed-hydrate identity, close parent mapping, exact registry row, CAS removal, empty chemistry block, and final SSSOM rows pass, but nutritional roles remain unsupported.

### Historical provisional-role concern

evidence: concern. Targets: record-11e5db9256585234.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-2fc847ea2021497b: Reassess prediction-only role support: K2SO4 x 7 H2O

major / open / confirmed; issue key: mim-reconciliation-role-support-11e5db9256585234.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-2fc847ea2021497b

Reassess prediction-only role support: K2SO4 x 7 H2O

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-58294ac033b0d57b | data/ingredients/mapped/K2so4_X_7_H2o.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1192],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.compound:k2so4_x_7_h2o","line":1194,"mapping_status":"MAPPED","ontology_id":"CHEBI:32036","preferred_term":"K2SO4 x 7 H2O"}],"identifier":"kgmicrobe.compound:k2so4_x_7_h2o","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":4,"edge_count":4,"occurrences":4},"occurrence_statistics":{"media_count":4,"total_occurrences":4},"ontology_mapping":{"mapping_quality":"CLOSE_MATCH","ontology_id":"CHEBI:32036","ontology_label":"potassium sulfate","ontology_source":"CHEBI"},"preferred_term":"K2SO4 x 7 H2O","sssom_rows":[{"data_row":1530,"object_id":"CHEBI:32036","object_label":"potassium sulfate","predicate_id":"skos:closeMatch"},{"data_row":1531,"object_id":"kgmicrobe.compound:k2so4_x_7_h2o","object_label":"K2SO4 x 7 H2O","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:K2so4_X_7_H2o","synonym_count":2} |
| ev-444cd9996ada793b | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1192] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-a77aa5e35f3b90c4 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:K2so4_X_7_H2o; data-row positions=[1530, 1531] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1530,"object_id":"CHEBI:32036","object_label":"potassium sulfate","other":"K2SO4\u00b77H2O&#124;K2SO4\u30fb7H2O","predicate_id":"skos:closeMatch","subject_id":"MIM:K2so4_X_7_H2o","validation_method":""},{"data_row":1531,"object_id":"kgmicrobe.compound:k2so4_x_7_h2o","object_label":"K2SO4 x 7 H2O","other":"K2SO4\u00b77H2O&#124;K2SO4\u30fb7H2O","predicate_id":"skos:exactMatch","subject_id":"MIM:K2so4_X_7_H2o","validation_method":""}] |
| ev-79e3721899935eab | docs/data/mapped_ingredients.csv; CSV lines=[1194] | supports | Published identity and count rows inspected: [{"identifier":"kgmicrobe.compound:k2so4_x_7_h2o","line":1194,"mapping_quality":"CLOSE_MATCH","mapping_status":"MAPPED","media_count":"4","ontology_id":"CHEBI:32036","preferred_term":"K2SO4 x 7 H2O","total_occurrences":"4"}] |
| ev-3b1ebe9e824faaa1 | reports/yaml_record_review/K2so4_X_7_H2o.md; &#96;data/ingredients/mapped/K2so4_X_7_H2o.yaml&#96;:2; Verdict:4; Identity:11; Validation:23; Evidence:34; Completeness:55; Recommended Edits:63 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-f9e185eab2ad8ea8 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[763,1738,1754] | context_only | [{"current_record_sha256":"06849d90807f1547a48c88de5dc022b466ae9b506efd08fb6929b1b6192b3412","finding_id":"SEM:66d62765fa2ee14dc597","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"06849d90807f1547a48c88de5dc022b466ae9b506efd08fb6929b1b6192b3412","finding_id":"SEM:55150222a83d0bb1bc86","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"06849d90807f1547a48c88de5dc022b466ae9b506efd08fb6929b1b6192b3412","finding_id":"SEM:d1d0d85dcfbd20edb012","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-abc98e239e8bdc70 | data/ingredients/mapped/K2so4_X_7_H2o.yaml; nutritional_roles[0] | supports | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1192],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.compound:k2so4_x_7_h2o","line":1194,"mapping_status":"MAPPED","ontology_id":"CHEBI:32036","preferred_term":"K2SO4 x 7 H2O"}],"identifier":"kgmicrobe.compound:k2so4_x_7_h2o","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":4,"edge_count":4,"occurrences":4},"occurrence_statistics":{"media_count":4,"total_occurrences":4},"ontology_mapping":{"mapping_quality":"CLOSE_MATCH","ontology_id":"CHEBI:32036","ontology_label":"potassium sulfate","ontology_source":"CHEBI"},"preferred_term":"K2SO4 x 7 H2O","sssom_rows":[{"data_row":1530,"object_id":"CHEBI:32036","object_label":"potassium sulfate","predicate_id":"skos:closeMatch"},{"data_row":1531,"object_id":"kgmicrobe.compound:k2so4_x_7_h2o","object_label":"K2SO4 x 7 H2O","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:K2so4_X_7_H2o","synonym_count":2} |
| ev-51d38656a6847f88 | reviews/structured/20261011T024635Z-mim-reconcile-all-batch-07/review.yaml; findings[finding_id=f-2fc847ea2021497b] | context_only | Predecessor structured review finding f-2fc847ea2021497b in 20261011T024635Z-mim-reconcile-all-batch-07 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024635Z-mim-reconcile-all-batch-07.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-k2so4-x-7-h2o
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: K2so4_X_7_H2o (data/ingredients/mapped/K2so4_X_7_H2o.yaml)'
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
summary: Per-record structured review for K2so4_X_7_H2o (data/ingredients/mapped/K2so4_X_7_H2o.yaml,
  record-11e5db9256585234, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/K2so4_X_7_H2o.yaml
    sha256: 06849d90807f1547a48c88de5dc022b466ae9b506efd08fb6929b1b6192b3412
    role: target
  - path: reviews/structured/20261011T024635Z-mim-reconcile-all-batch-07/review.yaml
    sha256: 408ad5bf1e58ddc25c06da54ed69bc719d6d61336a106fc7534b0954417618be
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
  - path: reports/yaml_record_review/K2so4_X_7_H2o.md
    sha256: da55d559324f48e67800aadf4277aa5f8826c5554162e9f73738e0c79aa25038
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-11e5db9256585234
  path: data/ingredients/mapped/K2so4_X_7_H2o.yaml
  label: K2so4_X_7_H2o
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/K2so4_X_7_H2o.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/K2so4_X_7_H2o.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/K2so4_X_7_H2o.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-11e5db9256585234
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-11e5db9256585234
  evidence_ids:
  - ev-58294ac033b0d57b
  - ev-444cd9996ada793b
  - ev-a77aa5e35f3b90c4
  - ev-79e3721899935eab
  - ev-abc98e239e8bdc70
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0], nutritional_roles[1] rely only
    on COMPUTATIONAL_PREDICTION or empty evidence.
  target_ids:
  - record-11e5db9256585234
  evidence_ids:
  - ev-58294ac033b0d57b
  - ev-f9e185eab2ad8ea8
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024635Z-mim-reconcile-all-batch-07
    and semantic review dispositions on HEAD.
  target_ids:
  - record-11e5db9256585234
  evidence_ids:
  - ev-3b1ebe9e824faaa1
  - ev-f9e185eab2ad8ea8
  - ev-51d38656a6847f88
evidence:
- evidence_id: ev-58294ac033b0d57b
  kind: record_content
  reference: data/ingredients/mapped/K2so4_X_7_H2o.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1192],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.compound:k2so4_x_7_h2o","line":1194,"mapping_status":"MAPPED","ontology_id":"CHEBI:32036","preferred_term":"K2SO4
    x 7 H2O"}],"identifier":"kgmicrobe.compound:k2so4_x_7_h2o","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":4,"edge_count":4,"occurrences":4},"occurrence_statistics":{"media_count":4,"total_occurrences":4},"ontology_mapping":{"mapping_quality":"CLOSE_MATCH","ontology_id":"CHEBI:32036","ontology_label":"potassium
    sulfate","ontology_source":"CHEBI"},"preferred_term":"K2SO4 x 7 H2O","sssom_rows":[{"data_row":1530,"object_id":"CHEBI:32036","object_label":"potassium
    sulfate","predicate_id":"skos:closeMatch"},{"data_row":1531,"object_id":"kgmicrobe.compound:k2so4_x_7_h2o","object_label":"K2SO4
    x 7 H2O","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:K2so4_X_7_H2o","synonym_count":2}'
  snapshot_sha256: 06849d90807f1547a48c88de5dc022b466ae9b506efd08fb6929b1b6192b3412
- evidence_id: ev-444cd9996ada793b
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1192]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-a77aa5e35f3b90c4
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:K2so4_X_7_H2o; data-row positions=[1530, 1531]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1530,"object_id":"CHEBI:32036","object_label":"potassium
    sulfate","other":"K2SO4\u00b77H2O|K2SO4\u30fb7H2O","predicate_id":"skos:closeMatch","subject_id":"MIM:K2so4_X_7_H2o","validation_method":""},{"data_row":1531,"object_id":"kgmicrobe.compound:k2so4_x_7_h2o","object_label":"K2SO4
    x 7 H2O","other":"K2SO4\u00b77H2O|K2SO4\u30fb7H2O","predicate_id":"skos:exactMatch","subject_id":"MIM:K2so4_X_7_H2o","validation_method":""}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-79e3721899935eab
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1194]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"kgmicrobe.compound:k2so4_x_7_h2o","line":1194,"mapping_quality":"CLOSE_MATCH","mapping_status":"MAPPED","media_count":"4","ontology_id":"CHEBI:32036","preferred_term":"K2SO4
    x 7 H2O","total_occurrences":"4"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-3b1ebe9e824faaa1
  kind: prior_review
  reference: reports/yaml_record_review/K2so4_X_7_H2o.md
  locator: '`data/ingredients/mapped/K2so4_X_7_H2o.yaml`:2; Verdict:4; Identity:11;
    Validation:23; Evidence:34; Completeness:55; Recommended Edits:63'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: da55d559324f48e67800aadf4277aa5f8826c5554162e9f73738e0c79aa25038
  quote: "Recommended Edits:\n- Major: remove `nutritional_roles.SULFUR_SOURCE` and\n\
    \  `nutritional_roles.MINERAL_SOURCE` unless inspected database or literature\n\
    \  evidence supports those roles for this local unresolved hydrate label, then\n\
    \  rerun strict, term, round-trip, component, and SSSOM validation."
- evidence_id: ev-f9e185eab2ad8ea8
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[763,1738,1754]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"06849d90807f1547a48c88de5dc022b466ae9b506efd08fb6929b1b6192b3412","finding_id":"SEM:66d62765fa2ee14dc597","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"06849d90807f1547a48c88de5dc022b466ae9b506efd08fb6929b1b6192b3412","finding_id":"SEM:55150222a83d0bb1bc86","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"06849d90807f1547a48c88de5dc022b466ae9b506efd08fb6929b1b6192b3412","finding_id":"SEM:d1d0d85dcfbd20edb012","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-abc98e239e8bdc70
  kind: record_content
  reference: data/ingredients/mapped/K2so4_X_7_H2o.yaml
  locator: nutritional_roles[0]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1192],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.compound:k2so4_x_7_h2o","line":1194,"mapping_status":"MAPPED","ontology_id":"CHEBI:32036","preferred_term":"K2SO4
    x 7 H2O"}],"identifier":"kgmicrobe.compound:k2so4_x_7_h2o","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":4,"edge_count":4,"occurrences":4},"occurrence_statistics":{"media_count":4,"total_occurrences":4},"ontology_mapping":{"mapping_quality":"CLOSE_MATCH","ontology_id":"CHEBI:32036","ontology_label":"potassium
    sulfate","ontology_source":"CHEBI"},"preferred_term":"K2SO4 x 7 H2O","sssom_rows":[{"data_row":1530,"object_id":"CHEBI:32036","object_label":"potassium
    sulfate","predicate_id":"skos:closeMatch"},{"data_row":1531,"object_id":"kgmicrobe.compound:k2so4_x_7_h2o","object_label":"K2SO4
    x 7 H2O","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:K2so4_X_7_H2o","synonym_count":2}'
  snapshot_sha256: 06849d90807f1547a48c88de5dc022b466ae9b506efd08fb6929b1b6192b3412
- evidence_id: ev-51d38656a6847f88
  kind: prior_review
  reference: reviews/structured/20261011T024635Z-mim-reconcile-all-batch-07/review.yaml
  locator: findings[finding_id=f-2fc847ea2021497b]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-2fc847ea2021497b in 20261011T024635Z-mim-reconcile-all-batch-07
  snapshot_sha256: 408ad5bf1e58ddc25c06da54ed69bc719d6d61336a106fc7534b0954417618be
assessments:
- assessment_id: a-4739c77d69029611
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-11e5db9256585234
  evidence_ids:
  - ev-58294ac033b0d57b
  - ev-444cd9996ada793b
  - ev-a77aa5e35f3b90c4
  - ev-79e3721899935eab
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-11c2647a072f3826
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-11e5db9256585234
  evidence_ids:
  - ev-3b1ebe9e824faaa1
  - ev-58294ac033b0d57b
  - ev-f9e185eab2ad8ea8
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T21:26:49Z;
    reviewed SHA-256=06849d90807f1547a48c88de5dc022b466ae9b506efd08fb6929b1b6192b3412;
    current SHA-256=06849d90807f1547a48c88de5dc022b466ae9b506efd08fb6929b1b6192b3412;
    hash_changed=False. Reports=["reports/yaml_record_review/K2so4_X_7_H2o.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The #344 local
    malformed-hydrate identity, close parent mapping, exact registry row, CAS removal,
    empty chemistry block, and final SSSOM rows pass, but nutritional roles remain
    unsupported.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-3b1ebe9e824faaa1
    - ev-58294ac033b0d57b
  - name: legacy-native-ids
    value: '["SEM:66d62765fa2ee14dc597","SEM:55150222a83d0bb1bc86","SEM:d1d0d85dcfbd20edb012"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-58294ac033b0d57b
    - ev-3b1ebe9e824faaa1
    - ev-f9e185eab2ad8ea8
- assessment_id: a-abc98e239e8bdc70
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-11e5db9256585234
  evidence_ids:
  - ev-3b1ebe9e824faaa1
  - ev-abc98e239e8bdc70
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-3b1ebe9e824faaa1
    - ev-abc98e239e8bdc70
findings:
- finding_id: rec-f-2fc847ea2021497b
  issue_key: mim-reconciliation-role-support-11e5db9256585234
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: K2SO4 x 7 H2O'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-11e5db9256585234
  evidence_ids:
  - ev-3b1ebe9e824faaa1
  - ev-abc98e239e8bdc70
  - ev-51d38656a6847f88
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/K2so4_X_7_H2o.yaml
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
    review_id: 20261011T024635Z-mim-reconcile-all-batch-07
    finding_id: f-2fc847ea2021497b
actions:
- action_id: rec-action-2fc847ea2021497b
  description: 'Reassess prediction-only role support: K2SO4 x 7 H2O'
  finding_ids:
  - rec-f-2fc847ea2021497b
  target_ids:
  - record-11e5db9256585234
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/K2so4_X_7_H2o.yaml
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
  with lineage to 20261011T024635Z-mim-reconcile-all-batch-07.
```
