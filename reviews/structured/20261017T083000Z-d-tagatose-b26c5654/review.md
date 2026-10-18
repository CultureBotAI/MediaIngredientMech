# Per-record structured review: D-_-tagatose (data/ingredients/mapped/D-_-tagatose.yaml)

- Review: 20261017T083000Z-d-tagatose-b26c5654
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for D-_-tagatose (data/ingredients/mapped/D-_-tagatose.yaml, record-b26c5654b5b1faf6, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/D-_-tagatose.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/D-_-tagatose.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-b26c5654b5b1faf6 | data/ingredients/mapped/D-_-tagatose.yaml | maintained | D-_-tagatose |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-b26c5654b5b1faf6 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-b26c5654b5b1faf6 | Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-b26c5654b5b1faf6 | Reconciled against predecessor batch review 20261011T024633Z-mim-reconcile-all-batch-05 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-b26c5654b5b1faf6.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-b26c5654b5b1faf6.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T13:26:28Z; reviewed SHA-256=80df3f31b68b9a204f213badc49d094e386baa3ddc74dc8cb7e7e97ddb097590; current SHA-256=80df3f31b68b9a204f213badc49d094e386baa3ddc74dc8cb7e7e97ddb097590; hash_changed=False. Reports=["reports/yaml_record_review/D-_-tagatose.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The synonym-matched CHEBI identity, structure fields, 0/0 count, and final SSSOM CAS payload pass, but the carbon role is computational.

### Historical provisional-role concern

evidence: concern. Targets: record-b26c5654b5b1faf6.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-5084983a67daa283: Reassess prediction-only role support: D-(-)-tagatose

major / open / confirmed; issue key: mim-reconciliation-role-support-b26c5654b5b1faf6.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-5084983a67daa283

Reassess prediction-only role support: D-(-)-tagatose

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-0734352e2578a7c1 | data/ingredients/mapped/D-_-tagatose.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[803],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:4249","line":805,"mapping_status":"MAPPED","ontology_id":"CHEBI:4249","preferred_term":"D-(-)-tagatose"}],"identifier":"CHEBI:4249","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"SYNONYM_MATCH","ontology_id":"CHEBI:4249","ontology_label":"D-tagatopyranose","ontology_source":"CHEBI"},"preferred_term":"D-(-)-tagatose","sssom_rows":[{"data_row":921,"object_id":"CHEBI:4249","object_label":"D-tagatopyranose","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:D-_-tagatose","synonym_count":0} |
| ev-367e7043bac7f691 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [803] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-0134ef3e77024e9d | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:D-_-tagatose; data-row positions=[921] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":921,"object_id":"CHEBI:4249","object_label":"D-tagatopyranose","other":"CAS:87-81-0","predicate_id":"skos:exactMatch","subject_id":"MIM:D-_-tagatose","validation_method":"OAK+OLS:chebi&#124;SYNONYM_ENRICH&#124;2026-07-07"}] |
| ev-0773ae69996bb0d9 | docs/data/mapped_ingredients.csv; CSV lines=[805] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:4249","line":805,"mapping_quality":"SYNONYM_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:4249","preferred_term":"D-(-)-tagatose","total_occurrences":"0"}] |
| ev-690f1016bef27f20 | reports/yaml_record_review/D-_-tagatose.md; &#96;data/ingredients/mapped/D-_-tagatose.yaml&#96;:2; Verdict:4; Identity:11; Validation:25; Evidence:42; Completeness:56; Recommended Edits:64 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-3428a345304ae58e | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[485,1823] | context_only | [{"current_record_sha256":"80df3f31b68b9a204f213badc49d094e386baa3ddc74dc8cb7e7e97ddb097590","finding_id":"SEM:ee9687bb25ce38ff071e","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"80df3f31b68b9a204f213badc49d094e386baa3ddc74dc8cb7e7e97ddb097590","finding_id":"SEM:6a9d9a2fcb6a41d4e70f","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-789137d1d93b3eec | data/ingredients/mapped/D-_-tagatose.yaml; nutritional_roles[0] | supports | Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION: [{"field":"nutritional_roles[0]","role":{"confidence":0.7,"evidence":[{"curator_note":"Provisional role inferred from CHEBI is_a/has_role closure; review recommended.","reference_text":"Inferred from CHEBI ancestry: subclass/has_role of CHEBI:16646 (carbohydrate)","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"CARBON_SOURCE"}}] |
| ev-c276147a01cb9c07 | reviews/structured/20261011T024633Z-mim-reconcile-all-batch-05/review.yaml; findings[finding_id=f-5084983a67daa283] | context_only | Predecessor structured review finding f-5084983a67daa283 in 20261011T024633Z-mim-reconcile-all-batch-05 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024633Z-mim-reconcile-all-batch-05.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-d-tagatose-b26c5654
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: D-_-tagatose (data/ingredients/mapped/D-_-tagatose.yaml)'
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
summary: Per-record structured review for D-_-tagatose (data/ingredients/mapped/D-_-tagatose.yaml,
  record-b26c5654b5b1faf6, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/D-_-tagatose.yaml
    sha256: 80df3f31b68b9a204f213badc49d094e386baa3ddc74dc8cb7e7e97ddb097590
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
  - path: reports/yaml_record_review/D-_-tagatose.md
    sha256: ad2b5bddb5d14bb18b6d480dfed3050b1bdb40ad1488e5822aee72e4d1186675
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-b26c5654b5b1faf6
  path: data/ingredients/mapped/D-_-tagatose.yaml
  label: D-_-tagatose
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/D-_-tagatose.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/D-_-tagatose.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/D-_-tagatose.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-b26c5654b5b1faf6
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-b26c5654b5b1faf6
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-b26c5654b5b1faf6
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024633Z-mim-reconcile-all-batch-05
    and semantic review dispositions on HEAD.
  target_ids:
  - record-b26c5654b5b1faf6
evidence:
- evidence_id: ev-0734352e2578a7c1
  kind: record_content
  reference: data/ingredients/mapped/D-_-tagatose.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[803],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:4249","line":805,"mapping_status":"MAPPED","ontology_id":"CHEBI:4249","preferred_term":"D-(-)-tagatose"}],"identifier":"CHEBI:4249","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"SYNONYM_MATCH","ontology_id":"CHEBI:4249","ontology_label":"D-tagatopyranose","ontology_source":"CHEBI"},"preferred_term":"D-(-)-tagatose","sssom_rows":[{"data_row":921,"object_id":"CHEBI:4249","object_label":"D-tagatopyranose","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:D-_-tagatose","synonym_count":0}'
  snapshot_sha256: 80df3f31b68b9a204f213badc49d094e386baa3ddc74dc8cb7e7e97ddb097590
- evidence_id: ev-367e7043bac7f691
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [803]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-0134ef3e77024e9d
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:D-_-tagatose; data-row positions=[921]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":921,"object_id":"CHEBI:4249","object_label":"D-tagatopyranose","other":"CAS:87-81-0","predicate_id":"skos:exactMatch","subject_id":"MIM:D-_-tagatose","validation_method":"OAK+OLS:chebi|SYNONYM_ENRICH|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-0773ae69996bb0d9
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[805]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:4249","line":805,"mapping_quality":"SYNONYM_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:4249","preferred_term":"D-(-)-tagatose","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-690f1016bef27f20
  kind: prior_review
  reference: reports/yaml_record_review/D-_-tagatose.md
  locator: '`data/ingredients/mapped/D-_-tagatose.yaml`:2; Verdict:4; Identity:11;
    Validation:25; Evidence:42; Completeness:56; Recommended Edits:64'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: ad2b5bddb5d14bb18b6d480dfed3050b1bdb40ad1488e5822aee72e4d1186675
  quote: "Recommended Edits:\n- In `data/ingredients/mapped/D-_-tagatose.yaml`, either\
    \ replace the\n  computational `CARBON_SOURCE` evidence with direct CultureBotHT\
    \ or\n  source-backed media-role evidence for this ingredient, or remove the role\n\
    \  facet; then rerun strict validation and the final SSSOM build."
- evidence_id: ev-3428a345304ae58e
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[485,1823]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"80df3f31b68b9a204f213badc49d094e386baa3ddc74dc8cb7e7e97ddb097590","finding_id":"SEM:ee9687bb25ce38ff071e","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"80df3f31b68b9a204f213badc49d094e386baa3ddc74dc8cb7e7e97ddb097590","finding_id":"SEM:6a9d9a2fcb6a41d4e70f","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-789137d1d93b3eec
  kind: record_content
  reference: data/ingredients/mapped/D-_-tagatose.yaml
  locator: nutritional_roles[0]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION:
    [{"field":"nutritional_roles[0]","role":{"confidence":0.7,"evidence":[{"curator_note":"Provisional
    role inferred from CHEBI is_a/has_role closure; review recommended.","reference_text":"Inferred
    from CHEBI ancestry: subclass/has_role of CHEBI:16646 (carbohydrate)","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"CARBON_SOURCE"}}]'
  snapshot_sha256: 80df3f31b68b9a204f213badc49d094e386baa3ddc74dc8cb7e7e97ddb097590
- evidence_id: ev-c276147a01cb9c07
  kind: prior_review
  reference: reviews/structured/20261011T024633Z-mim-reconcile-all-batch-05/review.yaml
  locator: findings[finding_id=f-5084983a67daa283]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-5084983a67daa283 in 20261011T024633Z-mim-reconcile-all-batch-05
  snapshot_sha256: 7549030a5b50ed98868ff3497507fdfbfecd07cd858c76738f734521fa9d3603
assessments:
- assessment_id: a-c6600b0fc00f2ff8
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-b26c5654b5b1faf6
  evidence_ids:
  - ev-0734352e2578a7c1
  - ev-367e7043bac7f691
  - ev-0134ef3e77024e9d
  - ev-0773ae69996bb0d9
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-1b38a4b6d90bcfab
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-b26c5654b5b1faf6
  evidence_ids:
  - ev-690f1016bef27f20
  - ev-0734352e2578a7c1
  - ev-3428a345304ae58e
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T13:26:28Z;
    reviewed SHA-256=80df3f31b68b9a204f213badc49d094e386baa3ddc74dc8cb7e7e97ddb097590;
    current SHA-256=80df3f31b68b9a204f213badc49d094e386baa3ddc74dc8cb7e7e97ddb097590;
    hash_changed=False. Reports=["reports/yaml_record_review/D-_-tagatose.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The synonym-matched
    CHEBI identity, structure fields, 0/0 count, and final SSSOM CAS payload pass,
    but the carbon role is computational.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-690f1016bef27f20
    - ev-0734352e2578a7c1
  - name: legacy-native-ids
    value: '["SEM:ee9687bb25ce38ff071e","SEM:6a9d9a2fcb6a41d4e70f"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-0734352e2578a7c1
    - ev-690f1016bef27f20
    - ev-3428a345304ae58e
- assessment_id: a-789137d1d93b3eec
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-b26c5654b5b1faf6
  evidence_ids:
  - ev-690f1016bef27f20
  - ev-789137d1d93b3eec
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-690f1016bef27f20
    - ev-789137d1d93b3eec
findings:
- finding_id: rec-f-5084983a67daa283
  issue_key: mim-reconciliation-role-support-b26c5654b5b1faf6
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: D-(-)-tagatose'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-b26c5654b5b1faf6
  evidence_ids:
  - ev-690f1016bef27f20
  - ev-789137d1d93b3eec
  - ev-c276147a01cb9c07
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/D-_-tagatose.yaml
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
    finding_id: f-5084983a67daa283
actions:
- action_id: rec-action-5084983a67daa283
  description: 'Reassess prediction-only role support: D-(-)-tagatose'
  finding_ids:
  - rec-f-5084983a67daa283
  target_ids:
  - record-b26c5654b5b1faf6
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/D-_-tagatose.yaml
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
