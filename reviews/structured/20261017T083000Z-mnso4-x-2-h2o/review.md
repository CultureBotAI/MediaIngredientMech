# Per-record structured review: Mnso4_X_2_H2o (data/ingredients/mapped/Mnso4_X_2_H2o.yaml)

- Review: 20261017T083000Z-mnso4-x-2-h2o
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Mnso4_X_2_H2o (data/ingredients/mapped/Mnso4_X_2_H2o.yaml, record-b4a98a3100fb1fdb, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Mnso4_X_2_H2o.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Mnso4_X_2_H2o.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-b4a98a3100fb1fdb | data/ingredients/mapped/Mnso4_X_2_H2o.yaml | maintained | Mnso4_X_2_H2o |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-b4a98a3100fb1fdb | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-b4a98a3100fb1fdb | Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-b4a98a3100fb1fdb | Reconciled against predecessor batch review 20261011T024636Z-mim-reconcile-all-batch-08 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-b4a98a3100fb1fdb.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-b4a98a3100fb1fdb.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T03:43:09Z; reviewed SHA-256=d04fb330a92fadc0116466870120fa51aae3d80a5bee1d1499c1c594dbe0c10d; current SHA-256=d04fb330a92fadc0116466870120fa51aae3d80a5bee1d1499c1c594dbe0c10d; hash_changed=False. Reports=["reports/yaml_record_review/Mnso4_X_2_H2o.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI:86356 dihydrate identity and final row pass, but concentration-qualified labels still publish in final SSSOM other and TRACE_ELEMENT is still provisional.

### Historical provisional-role concern

evidence: concern. Targets: record-b4a98a3100fb1fdb.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-72a9fb8495fd1f02: Reassess prediction-only role support: MnSO4 x 2 H2O

major / open / confirmed; issue key: mim-reconciliation-role-support-b4a98a3100fb1fdb.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-72a9fb8495fd1f02

Reassess prediction-only role support: MnSO4 x 2 H2O

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-acd0ad4d7dd8b9c8 | data/ingredients/mapped/Mnso4_X_2_H2o.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1416],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:86356","line":1418,"mapping_status":"MAPPED","ontology_id":"CHEBI:86356","preferred_term":"MnSO4 x 2 H2O"}],"identifier":"CHEBI:86356","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":42,"edge_count":42,"occurrences":42},"occurrence_statistics":{"media_count":42,"total_occurrences":42},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:86356","ontology_label":"manganese(II) sulfate dihydrate","ontology_source":"CHEBI"},"preferred_term":"MnSO4 x 2 H2O","sssom_rows":[{"data_row":1896,"object_id":"CHEBI:86356","object_label":"manganese(II) sulfate dihydrate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Mnso4_X_2_H2o","synonym_count":10} |
| ev-a961a69cac81632c | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1416] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-021cc7fb4139977b | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Mnso4_X_2_H2o; data-row positions=[1896] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1896,"object_id":"CHEBI:86356","object_label":"manganese(II) sulfate dihydrate","other":"MnSO4 . 2H2O&#124;MnSO4 x 2 H2O (0.1% w/v)&#124;MnSO4 x 2 H2O (1% solution)&#124;MnSO4.2H2O&#124;MnSO4\u00b72H2O&#124;manganese(2+) sulfate dihydrate&#124;manganese(2+) sulphate dihydrate&#124;manganese(II) sulphate dihydrate&#124;manganese(2+) sulfate--water (1/2)","predicate_id":"skos:exactMatch","subject_id":"MIM:Mnso4_X_2_H2o","validation_method":"OAK+OLS:chebi&#124;SYNONYM_ENRICH&#124;2026-07-07"}] |
| ev-5ce38e3a85ac0a02 | docs/data/mapped_ingredients.csv; CSV lines=[1418] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:86356","line":1418,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"42","ontology_id":"CHEBI:86356","preferred_term":"MnSO4 x 2 H2O","total_occurrences":"42"}] |
| ev-b8e673abe709c09d | reports/yaml_record_review/Mnso4_X_2_H2o.md; &#96;data/ingredients/mapped/Mnso4_X_2_H2o.yaml&#96;:2; Verdict:4; Identity:13; Validation:24; Evidence:31; Completeness:39; Recommended Edits:48 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-f743d012faa199f1 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[951,1984] | context_only | [{"current_record_sha256":"d04fb330a92fadc0116466870120fa51aae3d80a5bee1d1499c1c594dbe0c10d","finding_id":"SEM:000d73eafca16a91c985","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"d04fb330a92fadc0116466870120fa51aae3d80a5bee1d1499c1c594dbe0c10d","finding_id":"SEM:81e19fd78680fafeea03","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-50f863c668ee5871 | data/ingredients/mapped/Mnso4_X_2_H2o.yaml; nutritional_roles[0] | supports | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1416],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:86356","line":1418,"mapping_status":"MAPPED","ontology_id":"CHEBI:86356","preferred_term":"MnSO4 x 2 H2O"}],"identifier":"CHEBI:86356","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":42,"edge_count":42,"occurrences":42},"occurrence_statistics":{"media_count":42,"total_occurrences":42},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:86356","ontology_label":"manganese(II) sulfate dihydrate","ontology_source":"CHEBI"},"preferred_term":"MnSO4 x 2 H2O","sssom_rows":[{"data_row":1896,"object_id":"CHEBI:86356","object_label":"manganese(II) sulfate dihydrate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Mnso4_X_2_H2o","synonym_count":10} |
| ev-5bea0fc3789d02c3 | reviews/structured/20261011T024636Z-mim-reconcile-all-batch-08/review.yaml; findings[finding_id=f-72a9fb8495fd1f02] | context_only | Predecessor structured review finding f-72a9fb8495fd1f02 in 20261011T024636Z-mim-reconcile-all-batch-08 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024636Z-mim-reconcile-all-batch-08.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-mnso4-x-2-h2o
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Mnso4_X_2_H2o (data/ingredients/mapped/Mnso4_X_2_H2o.yaml)'
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
summary: Per-record structured review for Mnso4_X_2_H2o (data/ingredients/mapped/Mnso4_X_2_H2o.yaml,
  record-b4a98a3100fb1fdb, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Mnso4_X_2_H2o.yaml
    sha256: d04fb330a92fadc0116466870120fa51aae3d80a5bee1d1499c1c594dbe0c10d
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
  - path: reports/yaml_record_review/Mnso4_X_2_H2o.md
    sha256: 032a77905fd2fc138ee15a863b80ea02d927f4034e0e19e01187d386bd5f2430
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-b4a98a3100fb1fdb
  path: data/ingredients/mapped/Mnso4_X_2_H2o.yaml
  label: Mnso4_X_2_H2o
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Mnso4_X_2_H2o.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Mnso4_X_2_H2o.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Mnso4_X_2_H2o.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-b4a98a3100fb1fdb
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-b4a98a3100fb1fdb
  evidence_ids:
  - ev-acd0ad4d7dd8b9c8
  - ev-a961a69cac81632c
  - ev-021cc7fb4139977b
  - ev-5ce38e3a85ac0a02
  - ev-50f863c668ee5871
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-b4a98a3100fb1fdb
  evidence_ids:
  - ev-acd0ad4d7dd8b9c8
  - ev-f743d012faa199f1
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024636Z-mim-reconcile-all-batch-08
    and semantic review dispositions on HEAD.
  target_ids:
  - record-b4a98a3100fb1fdb
  evidence_ids:
  - ev-b8e673abe709c09d
  - ev-f743d012faa199f1
  - ev-5bea0fc3789d02c3
evidence:
- evidence_id: ev-acd0ad4d7dd8b9c8
  kind: record_content
  reference: data/ingredients/mapped/Mnso4_X_2_H2o.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1416],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:86356","line":1418,"mapping_status":"MAPPED","ontology_id":"CHEBI:86356","preferred_term":"MnSO4
    x 2 H2O"}],"identifier":"CHEBI:86356","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":42,"edge_count":42,"occurrences":42},"occurrence_statistics":{"media_count":42,"total_occurrences":42},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:86356","ontology_label":"manganese(II)
    sulfate dihydrate","ontology_source":"CHEBI"},"preferred_term":"MnSO4 x 2 H2O","sssom_rows":[{"data_row":1896,"object_id":"CHEBI:86356","object_label":"manganese(II)
    sulfate dihydrate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Mnso4_X_2_H2o","synonym_count":10}'
  snapshot_sha256: d04fb330a92fadc0116466870120fa51aae3d80a5bee1d1499c1c594dbe0c10d
- evidence_id: ev-a961a69cac81632c
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1416]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-021cc7fb4139977b
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Mnso4_X_2_H2o; data-row positions=[1896]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1896,"object_id":"CHEBI:86356","object_label":"manganese(II)
    sulfate dihydrate","other":"MnSO4 . 2H2O|MnSO4 x 2 H2O (0.1% w/v)|MnSO4 x 2 H2O
    (1% solution)|MnSO4.2H2O|MnSO4\u00b72H2O|manganese(2+) sulfate dihydrate|manganese(2+)
    sulphate dihydrate|manganese(II) sulphate dihydrate|manganese(2+) sulfate--water
    (1/2)","predicate_id":"skos:exactMatch","subject_id":"MIM:Mnso4_X_2_H2o","validation_method":"OAK+OLS:chebi|SYNONYM_ENRICH|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-5ce38e3a85ac0a02
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1418]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:86356","line":1418,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"42","ontology_id":"CHEBI:86356","preferred_term":"MnSO4
    x 2 H2O","total_occurrences":"42"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-b8e673abe709c09d
  kind: prior_review
  reference: reports/yaml_record_review/Mnso4_X_2_H2o.md
  locator: '`data/ingredients/mapped/Mnso4_X_2_H2o.yaml`:2; Verdict:4; Identity:13;
    Validation:24; Evidence:31; Completeness:39; Recommended Edits:48'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 032a77905fd2fc138ee15a863b80ea02d927f4034e0e19e01187d386bd5f2430
  quote: "Recommended Edits:\n- Major: mark concentration-qualified MnSO4 x 2 H2O\
    \ strings as\n  `REJECTED_LABEL`, or otherwise filter them from final SSSOM `other`.\n\
    - Major: add source-backed evidence that MnSO4 x 2 H2O is used as a trace\n  element\
    \ source in media, or remove the provisional `TRACE_ELEMENT` role."
- evidence_id: ev-f743d012faa199f1
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[951,1984]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"d04fb330a92fadc0116466870120fa51aae3d80a5bee1d1499c1c594dbe0c10d","finding_id":"SEM:000d73eafca16a91c985","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"d04fb330a92fadc0116466870120fa51aae3d80a5bee1d1499c1c594dbe0c10d","finding_id":"SEM:81e19fd78680fafeea03","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-50f863c668ee5871
  kind: record_content
  reference: data/ingredients/mapped/Mnso4_X_2_H2o.yaml
  locator: nutritional_roles[0]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1416],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:86356","line":1418,"mapping_status":"MAPPED","ontology_id":"CHEBI:86356","preferred_term":"MnSO4
    x 2 H2O"}],"identifier":"CHEBI:86356","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":42,"edge_count":42,"occurrences":42},"occurrence_statistics":{"media_count":42,"total_occurrences":42},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:86356","ontology_label":"manganese(II)
    sulfate dihydrate","ontology_source":"CHEBI"},"preferred_term":"MnSO4 x 2 H2O","sssom_rows":[{"data_row":1896,"object_id":"CHEBI:86356","object_label":"manganese(II)
    sulfate dihydrate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Mnso4_X_2_H2o","synonym_count":10}'
  snapshot_sha256: d04fb330a92fadc0116466870120fa51aae3d80a5bee1d1499c1c594dbe0c10d
- evidence_id: ev-5bea0fc3789d02c3
  kind: prior_review
  reference: reviews/structured/20261011T024636Z-mim-reconcile-all-batch-08/review.yaml
  locator: findings[finding_id=f-72a9fb8495fd1f02]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-72a9fb8495fd1f02 in 20261011T024636Z-mim-reconcile-all-batch-08
  snapshot_sha256: 4dd969b7020555cc2250a236d6fded134bedf3add1e1c5c72d269e98f9ae001b
assessments:
- assessment_id: a-b813e9880c6009c2
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-b4a98a3100fb1fdb
  evidence_ids:
  - ev-acd0ad4d7dd8b9c8
  - ev-a961a69cac81632c
  - ev-021cc7fb4139977b
  - ev-5ce38e3a85ac0a02
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-f03a2a88e37dde40
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-b4a98a3100fb1fdb
  evidence_ids:
  - ev-b8e673abe709c09d
  - ev-acd0ad4d7dd8b9c8
  - ev-f743d012faa199f1
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T03:43:09Z;
    reviewed SHA-256=d04fb330a92fadc0116466870120fa51aae3d80a5bee1d1499c1c594dbe0c10d;
    current SHA-256=d04fb330a92fadc0116466870120fa51aae3d80a5bee1d1499c1c594dbe0c10d;
    hash_changed=False. Reports=["reports/yaml_record_review/Mnso4_X_2_H2o.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The exact CHEBI:86356
    dihydrate identity and final row pass, but concentration-qualified labels still
    publish in final SSSOM other and TRACE_ELEMENT is still provisional.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-b8e673abe709c09d
    - ev-acd0ad4d7dd8b9c8
  - name: legacy-native-ids
    value: '["SEM:000d73eafca16a91c985","SEM:81e19fd78680fafeea03"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-acd0ad4d7dd8b9c8
    - ev-b8e673abe709c09d
    - ev-f743d012faa199f1
- assessment_id: a-50f863c668ee5871
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-b4a98a3100fb1fdb
  evidence_ids:
  - ev-b8e673abe709c09d
  - ev-50f863c668ee5871
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-b8e673abe709c09d
    - ev-50f863c668ee5871
findings:
- finding_id: rec-f-72a9fb8495fd1f02
  issue_key: mim-reconciliation-role-support-b4a98a3100fb1fdb
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: MnSO4 x 2 H2O'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-b4a98a3100fb1fdb
  evidence_ids:
  - ev-b8e673abe709c09d
  - ev-50f863c668ee5871
  - ev-5bea0fc3789d02c3
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Mnso4_X_2_H2o.yaml
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
    finding_id: f-72a9fb8495fd1f02
actions:
- action_id: rec-action-72a9fb8495fd1f02
  description: 'Reassess prediction-only role support: MnSO4 x 2 H2O'
  finding_ids:
  - rec-f-72a9fb8495fd1f02
  target_ids:
  - record-b4a98a3100fb1fdb
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Mnso4_X_2_H2o.yaml
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
