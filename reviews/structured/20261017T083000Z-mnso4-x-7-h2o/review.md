# Per-record structured review: Mnso4_X_7_H2o (data/ingredients/mapped/Mnso4_X_7_H2o.yaml)

- Review: 20261017T083000Z-mnso4-x-7-h2o
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Mnso4_X_7_H2o (data/ingredients/mapped/Mnso4_X_7_H2o.yaml, record-4560fc6cc7fa4ad9, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Mnso4_X_7_H2o.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Mnso4_X_7_H2o.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-4560fc6cc7fa4ad9 | data/ingredients/mapped/Mnso4_X_7_H2o.yaml | maintained | Mnso4_X_7_H2o |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-4560fc6cc7fa4ad9 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-4560fc6cc7fa4ad9 | Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-4560fc6cc7fa4ad9 | Reconciled against predecessor batch review 20261011T024636Z-mim-reconcile-all-batch-08 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-4560fc6cc7fa4ad9.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-4560fc6cc7fa4ad9.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T03:47:06Z; reviewed SHA-256=16fbe26057f3eb769a2054daa6aa374c72af193ac29382246cf26a7eaaaba852; current SHA-256=16fbe26057f3eb769a2054daa6aa374c72af193ac29382246cf26a7eaaaba852; hash_changed=False. Reports=["reports/yaml_record_review/Mnso4_X_7_H2o.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The local MnSO4 x 7 H2O identity, curated parent narrow match, and dual final rows pass, but TRACE_ELEMENT is still provisional.

### Historical provisional-role concern

evidence: concern. Targets: record-4560fc6cc7fa4ad9.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-19770a0f4101119b: Reassess prediction-only role support: MnSO4 x 7 H2O

major / open / confirmed; issue key: mim-reconciliation-role-support-4560fc6cc7fa4ad9.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-19770a0f4101119b

Reassess prediction-only role support: MnSO4 x 7 H2O

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-72ba1836a658007a | data/ingredients/mapped/Mnso4_X_7_H2o.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1420],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.compound:mnso4_x_7_h2o","line":1422,"mapping_status":"MAPPED","ontology_id":"CHEBI:86360","preferred_term":"MnSO4 x 7 H2O"}],"identifier":"kgmicrobe.compound:mnso4_x_7_h2o","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":16,"edge_count":16,"occurrences":16},"occurrence_statistics":{"media_count":16,"total_occurrences":16},"ontology_mapping":{"mapping_quality":"NARROW_MATCH","ontology_id":"CHEBI:86360","ontology_label":"manganese(II) sulfate","ontology_source":"CHEBI"},"preferred_term":"MnSO4 x 7 H2O","sssom_rows":[{"data_row":1900,"object_id":"CHEBI:86360","object_label":"manganese(II) sulfate","predicate_id":"skos:broadMatch"},{"data_row":1901,"object_id":"kgmicrobe.compound:mnso4_x_7_h2o","object_label":"MnSO4 x 7 H2O","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Mnso4_X_7_H2o","synonym_count":10} |
| ev-36c891577a313392 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1420] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-569e7dc13ac267ad | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Mnso4_X_7_H2o; data-row positions=[1900, 1901] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1900,"object_id":"CHEBI:86360","object_label":"manganese(II) sulfate","other":"MnSO4 . 7H2O&#124;MnSO4 x 7H2O&#124;MnSO4.7H2O&#124;MnSO4\u00b77H2O","predicate_id":"skos:broadMatch","subject_id":"MIM:Mnso4_X_7_H2o","validation_method":"manual:reconcile_sssom&#124;PREDICATE&#124;2026-09-20"},{"data_row":1901,"object_id":"kgmicrobe.compound:mnso4_x_7_h2o","object_label":"MnSO4 x 7 H2O","other":"MnSO4 . 7H2O&#124;MnSO4 x 7H2O&#124;MnSO4.7H2O&#124;MnSO4\u00b77H2O","predicate_id":"skos:exactMatch","subject_id":"MIM:Mnso4_X_7_H2o","validation_method":""}] |
| ev-f98f73656fb1b92b | docs/data/mapped_ingredients.csv; CSV lines=[1422] | supports | Published identity and count rows inspected: [{"identifier":"kgmicrobe.compound:mnso4_x_7_h2o","line":1422,"mapping_quality":"NARROW_MATCH","mapping_status":"MAPPED","media_count":"16","ontology_id":"CHEBI:86360","preferred_term":"MnSO4 x 7 H2O","total_occurrences":"16"}] |
| ev-96aa1bd688b78f85 | reports/yaml_record_review/Mnso4_X_7_H2o.md; &#96;data/ingredients/mapped/Mnso4_X_7_H2o.yaml&#96;:2; Verdict:4; Identity:13; Validation:26; Evidence:35; Completeness:47; Recommended Edits:54 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-282174b2cf45fe6f | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[953,1532] | context_only | [{"current_record_sha256":"16fbe26057f3eb769a2054daa6aa374c72af193ac29382246cf26a7eaaaba852","finding_id":"SEM:d1b1f0b592ccfa035dba","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"16fbe26057f3eb769a2054daa6aa374c72af193ac29382246cf26a7eaaaba852","finding_id":"SEM:4002490ae93ae3180ce0","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-112045d1f4ff7909 | data/ingredients/mapped/Mnso4_X_7_H2o.yaml; nutritional_roles[0] | supports | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1420],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.compound:mnso4_x_7_h2o","line":1422,"mapping_status":"MAPPED","ontology_id":"CHEBI:86360","preferred_term":"MnSO4 x 7 H2O"}],"identifier":"kgmicrobe.compound:mnso4_x_7_h2o","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":16,"edge_count":16,"occurrences":16},"occurrence_statistics":{"media_count":16,"total_occurrences":16},"ontology_mapping":{"mapping_quality":"NARROW_MATCH","ontology_id":"CHEBI:86360","ontology_label":"manganese(II) sulfate","ontology_source":"CHEBI"},"preferred_term":"MnSO4 x 7 H2O","sssom_rows":[{"data_row":1900,"object_id":"CHEBI:86360","object_label":"manganese(II) sulfate","predicate_id":"skos:broadMatch"},{"data_row":1901,"object_id":"kgmicrobe.compound:mnso4_x_7_h2o","object_label":"MnSO4 x 7 H2O","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Mnso4_X_7_H2o","synonym_count":10} |
| ev-96c81d531e180843 | reviews/structured/20261011T024636Z-mim-reconcile-all-batch-08/review.yaml; findings[finding_id=f-19770a0f4101119b] | context_only | Predecessor structured review finding f-19770a0f4101119b in 20261011T024636Z-mim-reconcile-all-batch-08 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024636Z-mim-reconcile-all-batch-08.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-mnso4-x-7-h2o
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Mnso4_X_7_H2o (data/ingredients/mapped/Mnso4_X_7_H2o.yaml)'
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
summary: Per-record structured review for Mnso4_X_7_H2o (data/ingredients/mapped/Mnso4_X_7_H2o.yaml,
  record-4560fc6cc7fa4ad9, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Mnso4_X_7_H2o.yaml
    sha256: 16fbe26057f3eb769a2054daa6aa374c72af193ac29382246cf26a7eaaaba852
    role: target
  - path: reviews/structured/20261011T024636Z-mim-reconcile-all-batch-08/review.yaml
    sha256: 4dd969b7020555cc2250a236d6fded134bedf3add1e1c5c72d269e98f9ae001b
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
  - path: reports/yaml_record_review/Mnso4_X_7_H2o.md
    sha256: d305acb3946e1398321af57dd37e425474c0ba3f256e56468b55cf3bdf3a3177
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-4560fc6cc7fa4ad9
  path: data/ingredients/mapped/Mnso4_X_7_H2o.yaml
  label: Mnso4_X_7_H2o
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Mnso4_X_7_H2o.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Mnso4_X_7_H2o.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Mnso4_X_7_H2o.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-4560fc6cc7fa4ad9
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-4560fc6cc7fa4ad9
  evidence_ids:
  - ev-72ba1836a658007a
  - ev-36c891577a313392
  - ev-569e7dc13ac267ad
  - ev-f98f73656fb1b92b
  - ev-112045d1f4ff7909
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-4560fc6cc7fa4ad9
  evidence_ids:
  - ev-72ba1836a658007a
  - ev-282174b2cf45fe6f
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024636Z-mim-reconcile-all-batch-08
    and semantic review dispositions on HEAD.
  target_ids:
  - record-4560fc6cc7fa4ad9
  evidence_ids:
  - ev-96aa1bd688b78f85
  - ev-282174b2cf45fe6f
  - ev-96c81d531e180843
evidence:
- evidence_id: ev-72ba1836a658007a
  kind: record_content
  reference: data/ingredients/mapped/Mnso4_X_7_H2o.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1420],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.compound:mnso4_x_7_h2o","line":1422,"mapping_status":"MAPPED","ontology_id":"CHEBI:86360","preferred_term":"MnSO4
    x 7 H2O"}],"identifier":"kgmicrobe.compound:mnso4_x_7_h2o","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":16,"edge_count":16,"occurrences":16},"occurrence_statistics":{"media_count":16,"total_occurrences":16},"ontology_mapping":{"mapping_quality":"NARROW_MATCH","ontology_id":"CHEBI:86360","ontology_label":"manganese(II)
    sulfate","ontology_source":"CHEBI"},"preferred_term":"MnSO4 x 7 H2O","sssom_rows":[{"data_row":1900,"object_id":"CHEBI:86360","object_label":"manganese(II)
    sulfate","predicate_id":"skos:broadMatch"},{"data_row":1901,"object_id":"kgmicrobe.compound:mnso4_x_7_h2o","object_label":"MnSO4
    x 7 H2O","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Mnso4_X_7_H2o","synonym_count":10}'
  snapshot_sha256: 16fbe26057f3eb769a2054daa6aa374c72af193ac29382246cf26a7eaaaba852
- evidence_id: ev-36c891577a313392
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1420]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-569e7dc13ac267ad
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Mnso4_X_7_H2o; data-row positions=[1900, 1901]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1900,"object_id":"CHEBI:86360","object_label":"manganese(II)
    sulfate","other":"MnSO4 . 7H2O|MnSO4 x 7H2O|MnSO4.7H2O|MnSO4\u00b77H2O","predicate_id":"skos:broadMatch","subject_id":"MIM:Mnso4_X_7_H2o","validation_method":"manual:reconcile_sssom|PREDICATE|2026-09-20"},{"data_row":1901,"object_id":"kgmicrobe.compound:mnso4_x_7_h2o","object_label":"MnSO4
    x 7 H2O","other":"MnSO4 . 7H2O|MnSO4 x 7H2O|MnSO4.7H2O|MnSO4\u00b77H2O","predicate_id":"skos:exactMatch","subject_id":"MIM:Mnso4_X_7_H2o","validation_method":""}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-f98f73656fb1b92b
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1422]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"kgmicrobe.compound:mnso4_x_7_h2o","line":1422,"mapping_quality":"NARROW_MATCH","mapping_status":"MAPPED","media_count":"16","ontology_id":"CHEBI:86360","preferred_term":"MnSO4
    x 7 H2O","total_occurrences":"16"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-96aa1bd688b78f85
  kind: prior_review
  reference: reports/yaml_record_review/Mnso4_X_7_H2o.md
  locator: '`data/ingredients/mapped/Mnso4_X_7_H2o.yaml`:2; Verdict:4; Identity:13;
    Validation:26; Evidence:35; Completeness:47; Recommended Edits:54'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: d305acb3946e1398321af57dd37e425474c0ba3f256e56468b55cf3bdf3a3177
  quote: "Recommended Edits:\n- Major: add source-backed evidence that MnSO4 x 7 H2O\
    \ is used as a trace\n  element source in media, or remove the provisional `TRACE_ELEMENT`\
    \ role."
- evidence_id: ev-282174b2cf45fe6f
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[953,1532]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"16fbe26057f3eb769a2054daa6aa374c72af193ac29382246cf26a7eaaaba852","finding_id":"SEM:d1b1f0b592ccfa035dba","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"16fbe26057f3eb769a2054daa6aa374c72af193ac29382246cf26a7eaaaba852","finding_id":"SEM:4002490ae93ae3180ce0","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-112045d1f4ff7909
  kind: record_content
  reference: data/ingredients/mapped/Mnso4_X_7_H2o.yaml
  locator: nutritional_roles[0]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1420],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.compound:mnso4_x_7_h2o","line":1422,"mapping_status":"MAPPED","ontology_id":"CHEBI:86360","preferred_term":"MnSO4
    x 7 H2O"}],"identifier":"kgmicrobe.compound:mnso4_x_7_h2o","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":16,"edge_count":16,"occurrences":16},"occurrence_statistics":{"media_count":16,"total_occurrences":16},"ontology_mapping":{"mapping_quality":"NARROW_MATCH","ontology_id":"CHEBI:86360","ontology_label":"manganese(II)
    sulfate","ontology_source":"CHEBI"},"preferred_term":"MnSO4 x 7 H2O","sssom_rows":[{"data_row":1900,"object_id":"CHEBI:86360","object_label":"manganese(II)
    sulfate","predicate_id":"skos:broadMatch"},{"data_row":1901,"object_id":"kgmicrobe.compound:mnso4_x_7_h2o","object_label":"MnSO4
    x 7 H2O","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Mnso4_X_7_H2o","synonym_count":10}'
  snapshot_sha256: 16fbe26057f3eb769a2054daa6aa374c72af193ac29382246cf26a7eaaaba852
- evidence_id: ev-96c81d531e180843
  kind: prior_review
  reference: reviews/structured/20261011T024636Z-mim-reconcile-all-batch-08/review.yaml
  locator: findings[finding_id=f-19770a0f4101119b]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-19770a0f4101119b in 20261011T024636Z-mim-reconcile-all-batch-08
  snapshot_sha256: 4dd969b7020555cc2250a236d6fded134bedf3add1e1c5c72d269e98f9ae001b
assessments:
- assessment_id: a-c92fec7492c15651
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-4560fc6cc7fa4ad9
  evidence_ids:
  - ev-72ba1836a658007a
  - ev-36c891577a313392
  - ev-569e7dc13ac267ad
  - ev-f98f73656fb1b92b
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-29390256778cf259
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-4560fc6cc7fa4ad9
  evidence_ids:
  - ev-96aa1bd688b78f85
  - ev-72ba1836a658007a
  - ev-282174b2cf45fe6f
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T03:47:06Z;
    reviewed SHA-256=16fbe26057f3eb769a2054daa6aa374c72af193ac29382246cf26a7eaaaba852;
    current SHA-256=16fbe26057f3eb769a2054daa6aa374c72af193ac29382246cf26a7eaaaba852;
    hash_changed=False. Reports=["reports/yaml_record_review/Mnso4_X_7_H2o.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The local MnSO4
    x 7 H2O identity, curated parent narrow match, and dual final rows pass, but TRACE_ELEMENT
    is still provisional.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-96aa1bd688b78f85
    - ev-72ba1836a658007a
  - name: legacy-native-ids
    value: '["SEM:d1b1f0b592ccfa035dba","SEM:4002490ae93ae3180ce0"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-72ba1836a658007a
    - ev-96aa1bd688b78f85
    - ev-282174b2cf45fe6f
- assessment_id: a-112045d1f4ff7909
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-4560fc6cc7fa4ad9
  evidence_ids:
  - ev-96aa1bd688b78f85
  - ev-112045d1f4ff7909
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-96aa1bd688b78f85
    - ev-112045d1f4ff7909
findings:
- finding_id: rec-f-19770a0f4101119b
  issue_key: mim-reconciliation-role-support-4560fc6cc7fa4ad9
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: MnSO4 x 7 H2O'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-4560fc6cc7fa4ad9
  evidence_ids:
  - ev-96aa1bd688b78f85
  - ev-112045d1f4ff7909
  - ev-96c81d531e180843
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Mnso4_X_7_H2o.yaml
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
    review_id: 20261011T024636Z-mim-reconcile-all-batch-08
    finding_id: f-19770a0f4101119b
actions:
- action_id: rec-action-19770a0f4101119b
  description: 'Reassess prediction-only role support: MnSO4 x 7 H2O'
  finding_ids:
  - rec-f-19770a0f4101119b
  target_ids:
  - record-4560fc6cc7fa4ad9
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Mnso4_X_7_H2o.yaml
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
  with lineage to 20261011T024636Z-mim-reconcile-all-batch-08.
```
