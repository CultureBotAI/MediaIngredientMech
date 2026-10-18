# Per-record structured review: Fecl2_X_7_H2o (data/ingredients/mapped/Fecl2_X_7_H2o.yaml)

- Review: 20261017T083000Z-fecl2-x-7-h2o
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Fecl2_X_7_H2o (data/ingredients/mapped/Fecl2_X_7_H2o.yaml, record-4106c72f651c778e, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Fecl2_X_7_H2o.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Fecl2_X_7_H2o.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-4106c72f651c778e | data/ingredients/mapped/Fecl2_X_7_H2o.yaml | maintained | Fecl2_X_7_H2o |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-4106c72f651c778e | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-4106c72f651c778e | Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-4106c72f651c778e | Reconciled against predecessor batch review 20261011T024634Z-mim-reconcile-all-batch-06 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-4106c72f651c778e.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-4106c72f651c778e.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T16:13:20Z; reviewed SHA-256=83d19345b09f00f439ed3d36898c5ada8cf208514a7f9110fafc8e7fa086e491; current SHA-256=83d19345b09f00f439ed3d36898c5ada8cf208514a7f9110fafc8e7fa086e491; hash_changed=False. Reports=["reports/yaml_record_review/Fecl2_X_7_H2o.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The local unresolved hydrate identity and final SSSOM row shape pass, but IRON_SOURCE is computational.

### Historical provisional-role concern

evidence: concern. Targets: record-4106c72f651c778e.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-323e3cb51130e6d4: Reassess prediction-only role support: FeCl2 x 7 H2O

major / open / confirmed; issue key: mim-reconciliation-role-support-4106c72f651c778e.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-323e3cb51130e6d4

Reassess prediction-only role support: FeCl2 x 7 H2O

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-d550e810fe2aeade | data/ingredients/mapped/Fecl2_X_7_H2o.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[986],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.compound:fecl2_x_7_h2o","line":988,"mapping_status":"MAPPED","ontology_id":"CHEBI:30812","preferred_term":"FeCl2 x 7 H2O"}],"identifier":"kgmicrobe.compound:fecl2_x_7_h2o","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":9,"edge_count":9,"occurrences":9},"occurrence_statistics":{"media_count":9,"total_occurrences":9},"ontology_mapping":{"mapping_quality":"CLOSE_MATCH","ontology_id":"CHEBI:30812","ontology_label":"iron dichloride","ontology_source":"CHEBI"},"preferred_term":"FeCl2 x 7 H2O","sssom_rows":[{"data_row":1178,"object_id":"CHEBI:30812","object_label":"iron dichloride","predicate_id":"skos:closeMatch"},{"data_row":1179,"object_id":"kgmicrobe.compound:fecl2_x_7_h2o","object_label":"FeCl2 x 7 H2O","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Fecl2_X_7_H2o","synonym_count":5} |
| ev-ede203b03d236e7d | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [986] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-427c5b7818f8fe8c | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Fecl2_X_7_H2o; data-row positions=[1178, 1179] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1178,"object_id":"CHEBI:30812","object_label":"iron dichloride","other":"","predicate_id":"skos:closeMatch","subject_id":"MIM:Fecl2_X_7_H2o","validation_method":""},{"data_row":1179,"object_id":"kgmicrobe.compound:fecl2_x_7_h2o","object_label":"FeCl2 x 7 H2O","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Fecl2_X_7_H2o","validation_method":""}] |
| ev-38f6a88608927cea | docs/data/mapped_ingredients.csv; CSV lines=[988] | supports | Published identity and count rows inspected: [{"identifier":"kgmicrobe.compound:fecl2_x_7_h2o","line":988,"mapping_quality":"CLOSE_MATCH","mapping_status":"MAPPED","media_count":"9","ontology_id":"CHEBI:30812","preferred_term":"FeCl2 x 7 H2O","total_occurrences":"9"}] |
| ev-3e5b37b6bd9dd9be | reports/yaml_record_review/Fecl2_X_7_H2o.md; &#96;data/ingredients/mapped/Fecl2_X_7_H2o.yaml&#96;:2; Verdict:4; Identity:11; Validation:23; Evidence:30; Completeness:55; Recommended Edits:62 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-9031935fad15d7db | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[592,1686] | context_only | [{"current_record_sha256":"83d19345b09f00f439ed3d36898c5ada8cf208514a7f9110fafc8e7fa086e491","finding_id":"SEM:e6562b12b5dc334aa61a","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"83d19345b09f00f439ed3d36898c5ada8cf208514a7f9110fafc8e7fa086e491","finding_id":"SEM:1909b89bce4716900e97","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-563622ad31634ada | data/ingredients/mapped/Fecl2_X_7_H2o.yaml; nutritional_roles[0] | supports | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[986],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.compound:fecl2_x_7_h2o","line":988,"mapping_status":"MAPPED","ontology_id":"CHEBI:30812","preferred_term":"FeCl2 x 7 H2O"}],"identifier":"kgmicrobe.compound:fecl2_x_7_h2o","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":9,"edge_count":9,"occurrences":9},"occurrence_statistics":{"media_count":9,"total_occurrences":9},"ontology_mapping":{"mapping_quality":"CLOSE_MATCH","ontology_id":"CHEBI:30812","ontology_label":"iron dichloride","ontology_source":"CHEBI"},"preferred_term":"FeCl2 x 7 H2O","sssom_rows":[{"data_row":1178,"object_id":"CHEBI:30812","object_label":"iron dichloride","predicate_id":"skos:closeMatch"},{"data_row":1179,"object_id":"kgmicrobe.compound:fecl2_x_7_h2o","object_label":"FeCl2 x 7 H2O","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Fecl2_X_7_H2o","synonym_count":5} |
| ev-b52f893ef0530456 | reviews/structured/20261011T024634Z-mim-reconcile-all-batch-06/review.yaml; findings[finding_id=f-323e3cb51130e6d4] | context_only | Predecessor structured review finding f-323e3cb51130e6d4 in 20261011T024634Z-mim-reconcile-all-batch-06 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024634Z-mim-reconcile-all-batch-06.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-fecl2-x-7-h2o
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Fecl2_X_7_H2o (data/ingredients/mapped/Fecl2_X_7_H2o.yaml)'
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
summary: Per-record structured review for Fecl2_X_7_H2o (data/ingredients/mapped/Fecl2_X_7_H2o.yaml,
  record-4106c72f651c778e, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Fecl2_X_7_H2o.yaml
    sha256: 83d19345b09f00f439ed3d36898c5ada8cf208514a7f9110fafc8e7fa086e491
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
  - path: reports/yaml_record_review/Fecl2_X_7_H2o.md
    sha256: 5bee05224aa76eb1c86aa3f22574b10ac9423bbe419febe86429085c1d9c3b35
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-4106c72f651c778e
  path: data/ingredients/mapped/Fecl2_X_7_H2o.yaml
  label: Fecl2_X_7_H2o
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Fecl2_X_7_H2o.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Fecl2_X_7_H2o.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Fecl2_X_7_H2o.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-4106c72f651c778e
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-4106c72f651c778e
  evidence_ids:
  - ev-d550e810fe2aeade
  - ev-ede203b03d236e7d
  - ev-427c5b7818f8fe8c
  - ev-38f6a88608927cea
  - ev-563622ad31634ada
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-4106c72f651c778e
  evidence_ids:
  - ev-d550e810fe2aeade
  - ev-9031935fad15d7db
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024634Z-mim-reconcile-all-batch-06
    and semantic review dispositions on HEAD.
  target_ids:
  - record-4106c72f651c778e
  evidence_ids:
  - ev-3e5b37b6bd9dd9be
  - ev-9031935fad15d7db
  - ev-b52f893ef0530456
evidence:
- evidence_id: ev-d550e810fe2aeade
  kind: record_content
  reference: data/ingredients/mapped/Fecl2_X_7_H2o.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[986],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.compound:fecl2_x_7_h2o","line":988,"mapping_status":"MAPPED","ontology_id":"CHEBI:30812","preferred_term":"FeCl2
    x 7 H2O"}],"identifier":"kgmicrobe.compound:fecl2_x_7_h2o","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":9,"edge_count":9,"occurrences":9},"occurrence_statistics":{"media_count":9,"total_occurrences":9},"ontology_mapping":{"mapping_quality":"CLOSE_MATCH","ontology_id":"CHEBI:30812","ontology_label":"iron
    dichloride","ontology_source":"CHEBI"},"preferred_term":"FeCl2 x 7 H2O","sssom_rows":[{"data_row":1178,"object_id":"CHEBI:30812","object_label":"iron
    dichloride","predicate_id":"skos:closeMatch"},{"data_row":1179,"object_id":"kgmicrobe.compound:fecl2_x_7_h2o","object_label":"FeCl2
    x 7 H2O","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Fecl2_X_7_H2o","synonym_count":5}'
  snapshot_sha256: 83d19345b09f00f439ed3d36898c5ada8cf208514a7f9110fafc8e7fa086e491
- evidence_id: ev-ede203b03d236e7d
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [986]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-427c5b7818f8fe8c
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Fecl2_X_7_H2o; data-row positions=[1178, 1179]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1178,"object_id":"CHEBI:30812","object_label":"iron
    dichloride","other":"","predicate_id":"skos:closeMatch","subject_id":"MIM:Fecl2_X_7_H2o","validation_method":""},{"data_row":1179,"object_id":"kgmicrobe.compound:fecl2_x_7_h2o","object_label":"FeCl2
    x 7 H2O","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Fecl2_X_7_H2o","validation_method":""}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-38f6a88608927cea
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[988]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"kgmicrobe.compound:fecl2_x_7_h2o","line":988,"mapping_quality":"CLOSE_MATCH","mapping_status":"MAPPED","media_count":"9","ontology_id":"CHEBI:30812","preferred_term":"FeCl2
    x 7 H2O","total_occurrences":"9"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-3e5b37b6bd9dd9be
  kind: prior_review
  reference: reports/yaml_record_review/Fecl2_X_7_H2o.md
  locator: '`data/ingredients/mapped/Fecl2_X_7_H2o.yaml`:2; Verdict:4; Identity:11;
    Validation:23; Evidence:30; Completeness:55; Recommended Edits:62'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 5bee05224aa76eb1c86aa3f22574b10ac9423bbe419febe86429085c1d9c3b35
  quote: "Recommended Edits:\n- Major: either replace the provisional `IRON_SOURCE`\
    \ inference with\n  source-backed evidence or remove the role facet, sync\n  `data/curated/mapped_ingredients.yaml`,\
    \ regenerate downstream artifacts if\n  the role changes, and rerun strict validation."
- evidence_id: ev-9031935fad15d7db
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[592,1686]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"83d19345b09f00f439ed3d36898c5ada8cf208514a7f9110fafc8e7fa086e491","finding_id":"SEM:e6562b12b5dc334aa61a","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"83d19345b09f00f439ed3d36898c5ada8cf208514a7f9110fafc8e7fa086e491","finding_id":"SEM:1909b89bce4716900e97","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-563622ad31634ada
  kind: record_content
  reference: data/ingredients/mapped/Fecl2_X_7_H2o.yaml
  locator: nutritional_roles[0]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[986],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.compound:fecl2_x_7_h2o","line":988,"mapping_status":"MAPPED","ontology_id":"CHEBI:30812","preferred_term":"FeCl2
    x 7 H2O"}],"identifier":"kgmicrobe.compound:fecl2_x_7_h2o","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":9,"edge_count":9,"occurrences":9},"occurrence_statistics":{"media_count":9,"total_occurrences":9},"ontology_mapping":{"mapping_quality":"CLOSE_MATCH","ontology_id":"CHEBI:30812","ontology_label":"iron
    dichloride","ontology_source":"CHEBI"},"preferred_term":"FeCl2 x 7 H2O","sssom_rows":[{"data_row":1178,"object_id":"CHEBI:30812","object_label":"iron
    dichloride","predicate_id":"skos:closeMatch"},{"data_row":1179,"object_id":"kgmicrobe.compound:fecl2_x_7_h2o","object_label":"FeCl2
    x 7 H2O","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Fecl2_X_7_H2o","synonym_count":5}'
  snapshot_sha256: 83d19345b09f00f439ed3d36898c5ada8cf208514a7f9110fafc8e7fa086e491
- evidence_id: ev-b52f893ef0530456
  kind: prior_review
  reference: reviews/structured/20261011T024634Z-mim-reconcile-all-batch-06/review.yaml
  locator: findings[finding_id=f-323e3cb51130e6d4]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-323e3cb51130e6d4 in 20261011T024634Z-mim-reconcile-all-batch-06
  snapshot_sha256: 14c3200be95fdc87fca16bb71628432f3c9aaf8a65356ed494efc776ebe8aa11
assessments:
- assessment_id: a-5f7673dc7aeed6d6
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-4106c72f651c778e
  evidence_ids:
  - ev-d550e810fe2aeade
  - ev-ede203b03d236e7d
  - ev-427c5b7818f8fe8c
  - ev-38f6a88608927cea
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-7ebba927740ddfea
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-4106c72f651c778e
  evidence_ids:
  - ev-3e5b37b6bd9dd9be
  - ev-d550e810fe2aeade
  - ev-9031935fad15d7db
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T16:13:20Z;
    reviewed SHA-256=83d19345b09f00f439ed3d36898c5ada8cf208514a7f9110fafc8e7fa086e491;
    current SHA-256=83d19345b09f00f439ed3d36898c5ada8cf208514a7f9110fafc8e7fa086e491;
    hash_changed=False. Reports=["reports/yaml_record_review/Fecl2_X_7_H2o.md"]. Full
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
    - ev-3e5b37b6bd9dd9be
    - ev-d550e810fe2aeade
  - name: legacy-native-ids
    value: '["SEM:e6562b12b5dc334aa61a","SEM:1909b89bce4716900e97"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-d550e810fe2aeade
    - ev-3e5b37b6bd9dd9be
    - ev-9031935fad15d7db
- assessment_id: a-563622ad31634ada
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-4106c72f651c778e
  evidence_ids:
  - ev-3e5b37b6bd9dd9be
  - ev-563622ad31634ada
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-3e5b37b6bd9dd9be
    - ev-563622ad31634ada
findings:
- finding_id: rec-f-323e3cb51130e6d4
  issue_key: mim-reconciliation-role-support-4106c72f651c778e
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: FeCl2 x 7 H2O'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-4106c72f651c778e
  evidence_ids:
  - ev-3e5b37b6bd9dd9be
  - ev-563622ad31634ada
  - ev-b52f893ef0530456
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Fecl2_X_7_H2o.yaml
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
    finding_id: f-323e3cb51130e6d4
actions:
- action_id: rec-action-323e3cb51130e6d4
  description: 'Reassess prediction-only role support: FeCl2 x 7 H2O'
  finding_ids:
  - rec-f-323e3cb51130e6d4
  target_ids:
  - record-4106c72f651c778e
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Fecl2_X_7_H2o.yaml
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
