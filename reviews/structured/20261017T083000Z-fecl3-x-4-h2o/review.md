# Per-record structured review: Fecl3_X_4_H2o (data/ingredients/mapped/Fecl3_X_4_H2o.yaml)

- Review: 20261017T083000Z-fecl3-x-4-h2o
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Fecl3_X_4_H2o (data/ingredients/mapped/Fecl3_X_4_H2o.yaml, record-1cd0990bc987fd7b, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Fecl3_X_4_H2o.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Fecl3_X_4_H2o.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-1cd0990bc987fd7b | data/ingredients/mapped/Fecl3_X_4_H2o.yaml | maintained | Fecl3_X_4_H2o |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-1cd0990bc987fd7b | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-1cd0990bc987fd7b | Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-1cd0990bc987fd7b | Reconciled against predecessor batch review 20261011T024634Z-mim-reconcile-all-batch-06 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-1cd0990bc987fd7b.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-1cd0990bc987fd7b.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T16:13:20Z; reviewed SHA-256=35539ce2262b60cf377be78d8709ecb1b5cbee07d090e6cff2bc577abfc880b7; current SHA-256=35539ce2262b60cf377be78d8709ecb1b5cbee07d090e6cff2bc577abfc880b7; hash_changed=False. Reports=["reports/yaml_record_review/Fecl3_X_4_H2o.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The local unresolved hydrate identity and final SSSOM row shape pass, but IRON_SOURCE is computational.

### Historical provisional-role concern

evidence: concern. Targets: record-1cd0990bc987fd7b.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-c506049c69a16602: Reassess prediction-only role support: FeCl3 x 4 H2O

major / open / confirmed; issue key: mim-reconciliation-role-support-1cd0990bc987fd7b.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-c506049c69a16602

Reassess prediction-only role support: FeCl3 x 4 H2O

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-18995c7722c91624 | data/ingredients/mapped/Fecl3_X_4_H2o.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[988],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.compound:fecl3_x_4_h2o","line":990,"mapping_status":"MAPPED","ontology_id":"CHEBI:30808","preferred_term":"FeCl3 x 4 H2O"}],"identifier":"kgmicrobe.compound:fecl3_x_4_h2o","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":7,"edge_count":7,"occurrences":7},"occurrence_statistics":{"media_count":7,"total_occurrences":7},"ontology_mapping":{"mapping_quality":"CLOSE_MATCH","ontology_id":"CHEBI:30808","ontology_label":"iron trichloride","ontology_source":"CHEBI"},"preferred_term":"FeCl3 x 4 H2O","sssom_rows":[{"data_row":1181,"object_id":"CHEBI:30808","object_label":"iron trichloride","predicate_id":"skos:closeMatch"},{"data_row":1182,"object_id":"kgmicrobe.compound:fecl3_x_4_h2o","object_label":"FeCl3 x 4 H2O","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Fecl3_X_4_H2o","synonym_count":3} |
| ev-a8be7fc9424338cf | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [988] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-777ddd255d1e1615 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Fecl3_X_4_H2o; data-row positions=[1181, 1182] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1181,"object_id":"CHEBI:30808","object_label":"iron trichloride","other":"FeCl3\u00b74H2O","predicate_id":"skos:closeMatch","subject_id":"MIM:Fecl3_X_4_H2o","validation_method":""},{"data_row":1182,"object_id":"kgmicrobe.compound:fecl3_x_4_h2o","object_label":"FeCl3 x 4 H2O","other":"FeCl3\u00b74H2O","predicate_id":"skos:exactMatch","subject_id":"MIM:Fecl3_X_4_H2o","validation_method":""}] |
| ev-1c03927e72ef6310 | docs/data/mapped_ingredients.csv; CSV lines=[990] | supports | Published identity and count rows inspected: [{"identifier":"kgmicrobe.compound:fecl3_x_4_h2o","line":990,"mapping_quality":"CLOSE_MATCH","mapping_status":"MAPPED","media_count":"7","ontology_id":"CHEBI:30808","preferred_term":"FeCl3 x 4 H2O","total_occurrences":"7"}] |
| ev-0e44b8e1b14185a4 | reports/yaml_record_review/Fecl3_X_4_H2o.md; &#96;data/ingredients/mapped/Fecl3_X_4_H2o.yaml&#96;:2; Verdict:4; Identity:11; Validation:23; Evidence:30; Completeness:55; Recommended Edits:62 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-19606f217adfc0ec | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[594,1959] | context_only | [{"current_record_sha256":"35539ce2262b60cf377be78d8709ecb1b5cbee07d090e6cff2bc577abfc880b7","finding_id":"SEM:e31d8c1f7ada1f7ce2f6","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"35539ce2262b60cf377be78d8709ecb1b5cbee07d090e6cff2bc577abfc880b7","finding_id":"SEM:94c795e689daa9ee87cf","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-61e7e0ca3f328271 | data/ingredients/mapped/Fecl3_X_4_H2o.yaml; nutritional_roles[0] | supports | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[988],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.compound:fecl3_x_4_h2o","line":990,"mapping_status":"MAPPED","ontology_id":"CHEBI:30808","preferred_term":"FeCl3 x 4 H2O"}],"identifier":"kgmicrobe.compound:fecl3_x_4_h2o","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":7,"edge_count":7,"occurrences":7},"occurrence_statistics":{"media_count":7,"total_occurrences":7},"ontology_mapping":{"mapping_quality":"CLOSE_MATCH","ontology_id":"CHEBI:30808","ontology_label":"iron trichloride","ontology_source":"CHEBI"},"preferred_term":"FeCl3 x 4 H2O","sssom_rows":[{"data_row":1181,"object_id":"CHEBI:30808","object_label":"iron trichloride","predicate_id":"skos:closeMatch"},{"data_row":1182,"object_id":"kgmicrobe.compound:fecl3_x_4_h2o","object_label":"FeCl3 x 4 H2O","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Fecl3_X_4_H2o","synonym_count":3} |
| ev-732c0bfe45d92c6d | reviews/structured/20261011T024634Z-mim-reconcile-all-batch-06/review.yaml; findings[finding_id=f-c506049c69a16602] | context_only | Predecessor structured review finding f-c506049c69a16602 in 20261011T024634Z-mim-reconcile-all-batch-06 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024634Z-mim-reconcile-all-batch-06.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-fecl3-x-4-h2o
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Fecl3_X_4_H2o (data/ingredients/mapped/Fecl3_X_4_H2o.yaml)'
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
summary: Per-record structured review for Fecl3_X_4_H2o (data/ingredients/mapped/Fecl3_X_4_H2o.yaml,
  record-1cd0990bc987fd7b, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Fecl3_X_4_H2o.yaml
    sha256: 35539ce2262b60cf377be78d8709ecb1b5cbee07d090e6cff2bc577abfc880b7
    role: target
  - path: reviews/structured/20261011T024634Z-mim-reconcile-all-batch-06/review.yaml
    sha256: 14c3200be95fdc87fca16bb71628432f3c9aaf8a65356ed494efc776ebe8aa11
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
  - path: reports/yaml_record_review/Fecl3_X_4_H2o.md
    sha256: 6b2e750ac047bffdfd1a8ff67c46f47097f3da955e23249932ec1baa442af91c
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-1cd0990bc987fd7b
  path: data/ingredients/mapped/Fecl3_X_4_H2o.yaml
  label: Fecl3_X_4_H2o
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Fecl3_X_4_H2o.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Fecl3_X_4_H2o.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Fecl3_X_4_H2o.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-1cd0990bc987fd7b
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-1cd0990bc987fd7b
  evidence_ids:
  - ev-18995c7722c91624
  - ev-a8be7fc9424338cf
  - ev-777ddd255d1e1615
  - ev-1c03927e72ef6310
  - ev-61e7e0ca3f328271
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-1cd0990bc987fd7b
  evidence_ids:
  - ev-18995c7722c91624
  - ev-19606f217adfc0ec
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024634Z-mim-reconcile-all-batch-06
    and semantic review dispositions on HEAD.
  target_ids:
  - record-1cd0990bc987fd7b
  evidence_ids:
  - ev-0e44b8e1b14185a4
  - ev-19606f217adfc0ec
  - ev-732c0bfe45d92c6d
evidence:
- evidence_id: ev-18995c7722c91624
  kind: record_content
  reference: data/ingredients/mapped/Fecl3_X_4_H2o.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[988],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.compound:fecl3_x_4_h2o","line":990,"mapping_status":"MAPPED","ontology_id":"CHEBI:30808","preferred_term":"FeCl3
    x 4 H2O"}],"identifier":"kgmicrobe.compound:fecl3_x_4_h2o","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":7,"edge_count":7,"occurrences":7},"occurrence_statistics":{"media_count":7,"total_occurrences":7},"ontology_mapping":{"mapping_quality":"CLOSE_MATCH","ontology_id":"CHEBI:30808","ontology_label":"iron
    trichloride","ontology_source":"CHEBI"},"preferred_term":"FeCl3 x 4 H2O","sssom_rows":[{"data_row":1181,"object_id":"CHEBI:30808","object_label":"iron
    trichloride","predicate_id":"skos:closeMatch"},{"data_row":1182,"object_id":"kgmicrobe.compound:fecl3_x_4_h2o","object_label":"FeCl3
    x 4 H2O","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Fecl3_X_4_H2o","synonym_count":3}'
  snapshot_sha256: 35539ce2262b60cf377be78d8709ecb1b5cbee07d090e6cff2bc577abfc880b7
- evidence_id: ev-a8be7fc9424338cf
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [988]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-777ddd255d1e1615
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Fecl3_X_4_H2o; data-row positions=[1181, 1182]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1181,"object_id":"CHEBI:30808","object_label":"iron
    trichloride","other":"FeCl3\u00b74H2O","predicate_id":"skos:closeMatch","subject_id":"MIM:Fecl3_X_4_H2o","validation_method":""},{"data_row":1182,"object_id":"kgmicrobe.compound:fecl3_x_4_h2o","object_label":"FeCl3
    x 4 H2O","other":"FeCl3\u00b74H2O","predicate_id":"skos:exactMatch","subject_id":"MIM:Fecl3_X_4_H2o","validation_method":""}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-1c03927e72ef6310
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[990]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"kgmicrobe.compound:fecl3_x_4_h2o","line":990,"mapping_quality":"CLOSE_MATCH","mapping_status":"MAPPED","media_count":"7","ontology_id":"CHEBI:30808","preferred_term":"FeCl3
    x 4 H2O","total_occurrences":"7"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-0e44b8e1b14185a4
  kind: prior_review
  reference: reports/yaml_record_review/Fecl3_X_4_H2o.md
  locator: '`data/ingredients/mapped/Fecl3_X_4_H2o.yaml`:2; Verdict:4; Identity:11;
    Validation:23; Evidence:30; Completeness:55; Recommended Edits:62'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 6b2e750ac047bffdfd1a8ff67c46f47097f3da955e23249932ec1baa442af91c
  quote: "Recommended Edits:\n- Major: either replace the provisional `IRON_SOURCE`\
    \ inference with\n  source-backed evidence or remove the role facet, sync\n  `data/curated/mapped_ingredients.yaml`,\
    \ regenerate downstream artifacts if\n  the role changes, and rerun strict validation."
- evidence_id: ev-19606f217adfc0ec
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[594,1959]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"35539ce2262b60cf377be78d8709ecb1b5cbee07d090e6cff2bc577abfc880b7","finding_id":"SEM:e31d8c1f7ada1f7ce2f6","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"35539ce2262b60cf377be78d8709ecb1b5cbee07d090e6cff2bc577abfc880b7","finding_id":"SEM:94c795e689daa9ee87cf","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-61e7e0ca3f328271
  kind: record_content
  reference: data/ingredients/mapped/Fecl3_X_4_H2o.yaml
  locator: nutritional_roles[0]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[988],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.compound:fecl3_x_4_h2o","line":990,"mapping_status":"MAPPED","ontology_id":"CHEBI:30808","preferred_term":"FeCl3
    x 4 H2O"}],"identifier":"kgmicrobe.compound:fecl3_x_4_h2o","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":7,"edge_count":7,"occurrences":7},"occurrence_statistics":{"media_count":7,"total_occurrences":7},"ontology_mapping":{"mapping_quality":"CLOSE_MATCH","ontology_id":"CHEBI:30808","ontology_label":"iron
    trichloride","ontology_source":"CHEBI"},"preferred_term":"FeCl3 x 4 H2O","sssom_rows":[{"data_row":1181,"object_id":"CHEBI:30808","object_label":"iron
    trichloride","predicate_id":"skos:closeMatch"},{"data_row":1182,"object_id":"kgmicrobe.compound:fecl3_x_4_h2o","object_label":"FeCl3
    x 4 H2O","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Fecl3_X_4_H2o","synonym_count":3}'
  snapshot_sha256: 35539ce2262b60cf377be78d8709ecb1b5cbee07d090e6cff2bc577abfc880b7
- evidence_id: ev-732c0bfe45d92c6d
  kind: prior_review
  reference: reviews/structured/20261011T024634Z-mim-reconcile-all-batch-06/review.yaml
  locator: findings[finding_id=f-c506049c69a16602]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-c506049c69a16602 in 20261011T024634Z-mim-reconcile-all-batch-06
  snapshot_sha256: 14c3200be95fdc87fca16bb71628432f3c9aaf8a65356ed494efc776ebe8aa11
assessments:
- assessment_id: a-0d937528ff9f9665
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-1cd0990bc987fd7b
  evidence_ids:
  - ev-18995c7722c91624
  - ev-a8be7fc9424338cf
  - ev-777ddd255d1e1615
  - ev-1c03927e72ef6310
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-de76ec8068d9be04
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-1cd0990bc987fd7b
  evidence_ids:
  - ev-0e44b8e1b14185a4
  - ev-18995c7722c91624
  - ev-19606f217adfc0ec
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T16:13:20Z;
    reviewed SHA-256=35539ce2262b60cf377be78d8709ecb1b5cbee07d090e6cff2bc577abfc880b7;
    current SHA-256=35539ce2262b60cf377be78d8709ecb1b5cbee07d090e6cff2bc577abfc880b7;
    hash_changed=False. Reports=["reports/yaml_record_review/Fecl3_X_4_H2o.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The local unresolved
    hydrate identity and final SSSOM row shape pass, but IRON_SOURCE is computational.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-0e44b8e1b14185a4
    - ev-18995c7722c91624
  - name: legacy-native-ids
    value: '["SEM:e31d8c1f7ada1f7ce2f6","SEM:94c795e689daa9ee87cf"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-18995c7722c91624
    - ev-0e44b8e1b14185a4
    - ev-19606f217adfc0ec
- assessment_id: a-61e7e0ca3f328271
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-1cd0990bc987fd7b
  evidence_ids:
  - ev-0e44b8e1b14185a4
  - ev-61e7e0ca3f328271
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-0e44b8e1b14185a4
    - ev-61e7e0ca3f328271
findings:
- finding_id: rec-f-c506049c69a16602
  issue_key: mim-reconciliation-role-support-1cd0990bc987fd7b
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: FeCl3 x 4 H2O'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-1cd0990bc987fd7b
  evidence_ids:
  - ev-0e44b8e1b14185a4
  - ev-61e7e0ca3f328271
  - ev-732c0bfe45d92c6d
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Fecl3_X_4_H2o.yaml
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
    review_id: 20261011T024634Z-mim-reconcile-all-batch-06
    finding_id: f-c506049c69a16602
actions:
- action_id: rec-action-c506049c69a16602
  description: 'Reassess prediction-only role support: FeCl3 x 4 H2O'
  finding_ids:
  - rec-f-c506049c69a16602
  target_ids:
  - record-1cd0990bc987fd7b
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Fecl3_X_4_H2o.yaml
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
  with lineage to 20261011T024634Z-mim-reconcile-all-batch-06.
```
