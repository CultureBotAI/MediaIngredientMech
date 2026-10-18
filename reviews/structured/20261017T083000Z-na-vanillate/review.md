# Per-record structured review: Na-vanillate (data/ingredients/mapped/Na-vanillate.yaml)

- Review: 20261017T083000Z-na-vanillate
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Na-vanillate (data/ingredients/mapped/Na-vanillate.yaml, record-1ab34fe74a6ec342, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Na-vanillate.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Na-vanillate.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-1ab34fe74a6ec342 | data/ingredients/mapped/Na-vanillate.yaml | maintained | Na-vanillate |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-1ab34fe74a6ec342 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-1ab34fe74a6ec342 | Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-1ab34fe74a6ec342 | Reconciled against predecessor batch review 20261011T024637Z-mim-reconcile-all-batch-09 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-1ab34fe74a6ec342.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-1ab34fe74a6ec342.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T05:01:32Z; reviewed SHA-256=9ddd9edfd7d77a47df419c9239e9b99e99e24c41e9e8949a5ae65fde6afab385; current SHA-256=9ddd9edfd7d77a47df419c9239e9b99e99e24c41e9e8949a5ae65fde6afab385; hash_changed=False. Reports=["reports/yaml_record_review/Na-vanillate.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI:132748 sodium vanillate identity, structure, occurrence count, synonyms, and final exact row pass, but CARBON_SOURCE is provisional.

### Historical provisional-role concern

evidence: concern. Targets: record-1ab34fe74a6ec342.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-6575df5edeb084de: Reassess prediction-only role support: Na-vanillate

major / open / confirmed; issue key: mim-reconciliation-role-support-1ab34fe74a6ec342.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-6575df5edeb084de

Reassess prediction-only role support: Na-vanillate

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-71839a060c186070 | data/ingredients/mapped/Na-vanillate.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1476],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:132748","line":1478,"mapping_status":"MAPPED","ontology_id":"CHEBI:132748","preferred_term":"Na-vanillate"}],"identifier":"CHEBI:132748","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":3,"edge_count":3,"occurrences":3},"occurrence_statistics":{"media_count":3,"total_occurrences":3},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:132748","ontology_label":"sodium vanillate","ontology_source":"CHEBI"},"preferred_term":"Na-vanillate","sssom_rows":[{"data_row":1982,"object_id":"CHEBI:132748","object_label":"sodium vanillate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Na-vanillate","synonym_count":2} |
| ev-9050c95cea28b636 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1476] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-75b345fc10b8e8c7 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Na-vanillate; data-row positions=[1982] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1982,"object_id":"CHEBI:132748","object_label":"sodium vanillate","other":"sodium 4-hydroxy-3-methoxybenzoate&#124;CAS:28508-48-7","predicate_id":"skos:exactMatch","subject_id":"MIM:Na-vanillate","validation_method":"OAK+OLS:chebi&#124;SYNONYM_ENRICH&#124;2026-07-07"}] |
| ev-4b3b30e9b203bda0 | docs/data/mapped_ingredients.csv; CSV lines=[1478] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:132748","line":1478,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"3","ontology_id":"CHEBI:132748","preferred_term":"Na-vanillate","total_occurrences":"3"}] |
| ev-9656d159cec9e375 | reports/yaml_record_review/Na-vanillate.md; &#96;data/ingredients/mapped/Na-vanillate.yaml&#96;:2; Verdict:4; Identity:10; Validation:19; Evidence:26; Completeness:38; Recommended Edits:44 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-881ee80926bb21d5 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[984,1577] | context_only | [{"current_record_sha256":"9ddd9edfd7d77a47df419c9239e9b99e99e24c41e9e8949a5ae65fde6afab385","finding_id":"SEM:6f281a6a06e2b2f6444e","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"9ddd9edfd7d77a47df419c9239e9b99e99e24c41e9e8949a5ae65fde6afab385","finding_id":"SEM:d11f0dbb4c82da05db54","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-81a43ad8b5551552 | data/ingredients/mapped/Na-vanillate.yaml; nutritional_roles[0] | supports | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1476],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:132748","line":1478,"mapping_status":"MAPPED","ontology_id":"CHEBI:132748","preferred_term":"Na-vanillate"}],"identifier":"CHEBI:132748","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":3,"edge_count":3,"occurrences":3},"occurrence_statistics":{"media_count":3,"total_occurrences":3},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:132748","ontology_label":"sodium vanillate","ontology_source":"CHEBI"},"preferred_term":"Na-vanillate","sssom_rows":[{"data_row":1982,"object_id":"CHEBI:132748","object_label":"sodium vanillate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Na-vanillate","synonym_count":2} |
| ev-d04db2e7c8d8bde6 | reviews/structured/20261011T024637Z-mim-reconcile-all-batch-09/review.yaml; findings[finding_id=f-6575df5edeb084de] | context_only | Predecessor structured review finding f-6575df5edeb084de in 20261011T024637Z-mim-reconcile-all-batch-09 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024637Z-mim-reconcile-all-batch-09.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-na-vanillate
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Na-vanillate (data/ingredients/mapped/Na-vanillate.yaml)'
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
summary: Per-record structured review for Na-vanillate (data/ingredients/mapped/Na-vanillate.yaml,
  record-1ab34fe74a6ec342, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Na-vanillate.yaml
    sha256: 9ddd9edfd7d77a47df419c9239e9b99e99e24c41e9e8949a5ae65fde6afab385
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
  - path: reports/yaml_record_review/Na-vanillate.md
    sha256: f840af65245afc618be1dec0e218219adc15f1aed90de499c9ff098f5e9fbef1
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-1ab34fe74a6ec342
  path: data/ingredients/mapped/Na-vanillate.yaml
  label: Na-vanillate
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Na-vanillate.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Na-vanillate.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Na-vanillate.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-1ab34fe74a6ec342
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-1ab34fe74a6ec342
  evidence_ids:
  - ev-71839a060c186070
  - ev-9050c95cea28b636
  - ev-75b345fc10b8e8c7
  - ev-4b3b30e9b203bda0
  - ev-81a43ad8b5551552
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-1ab34fe74a6ec342
  evidence_ids:
  - ev-71839a060c186070
  - ev-881ee80926bb21d5
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024637Z-mim-reconcile-all-batch-09
    and semantic review dispositions on HEAD.
  target_ids:
  - record-1ab34fe74a6ec342
  evidence_ids:
  - ev-9656d159cec9e375
  - ev-881ee80926bb21d5
  - ev-d04db2e7c8d8bde6
evidence:
- evidence_id: ev-71839a060c186070
  kind: record_content
  reference: data/ingredients/mapped/Na-vanillate.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1476],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:132748","line":1478,"mapping_status":"MAPPED","ontology_id":"CHEBI:132748","preferred_term":"Na-vanillate"}],"identifier":"CHEBI:132748","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":3,"edge_count":3,"occurrences":3},"occurrence_statistics":{"media_count":3,"total_occurrences":3},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:132748","ontology_label":"sodium
    vanillate","ontology_source":"CHEBI"},"preferred_term":"Na-vanillate","sssom_rows":[{"data_row":1982,"object_id":"CHEBI:132748","object_label":"sodium
    vanillate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Na-vanillate","synonym_count":2}'
  snapshot_sha256: 9ddd9edfd7d77a47df419c9239e9b99e99e24c41e9e8949a5ae65fde6afab385
- evidence_id: ev-9050c95cea28b636
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1476]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-75b345fc10b8e8c7
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Na-vanillate; data-row positions=[1982]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1982,"object_id":"CHEBI:132748","object_label":"sodium
    vanillate","other":"sodium 4-hydroxy-3-methoxybenzoate|CAS:28508-48-7","predicate_id":"skos:exactMatch","subject_id":"MIM:Na-vanillate","validation_method":"OAK+OLS:chebi|SYNONYM_ENRICH|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-4b3b30e9b203bda0
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1478]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:132748","line":1478,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"3","ontology_id":"CHEBI:132748","preferred_term":"Na-vanillate","total_occurrences":"3"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-9656d159cec9e375
  kind: prior_review
  reference: reports/yaml_record_review/Na-vanillate.md
  locator: '`data/ingredients/mapped/Na-vanillate.yaml`:2; Verdict:4; Identity:10;
    Validation:19; Evidence:26; Completeness:38; Recommended Edits:44'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: f840af65245afc618be1dec0e218219adc15f1aed90de499c9ff098f5e9fbef1
  quote: "Recommended Edits:\n- Major: in `data/ingredients/mapped/Na-vanillate.yaml`,\
    \ either remove\n  `nutritional_roles.CARBON_SOURCE` or replace its computational\
    \ placeholder\n  with source-backed evidence from maintained occurrence, role-text,\
    \ or\n  literature inputs. Rerun strict validation and the role/output SSSOM checks\n\
    \  after the role facet changes."
- evidence_id: ev-881ee80926bb21d5
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[984,1577]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"9ddd9edfd7d77a47df419c9239e9b99e99e24c41e9e8949a5ae65fde6afab385","finding_id":"SEM:6f281a6a06e2b2f6444e","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"9ddd9edfd7d77a47df419c9239e9b99e99e24c41e9e8949a5ae65fde6afab385","finding_id":"SEM:d11f0dbb4c82da05db54","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-81a43ad8b5551552
  kind: record_content
  reference: data/ingredients/mapped/Na-vanillate.yaml
  locator: nutritional_roles[0]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1476],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:132748","line":1478,"mapping_status":"MAPPED","ontology_id":"CHEBI:132748","preferred_term":"Na-vanillate"}],"identifier":"CHEBI:132748","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":3,"edge_count":3,"occurrences":3},"occurrence_statistics":{"media_count":3,"total_occurrences":3},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:132748","ontology_label":"sodium
    vanillate","ontology_source":"CHEBI"},"preferred_term":"Na-vanillate","sssom_rows":[{"data_row":1982,"object_id":"CHEBI:132748","object_label":"sodium
    vanillate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Na-vanillate","synonym_count":2}'
  snapshot_sha256: 9ddd9edfd7d77a47df419c9239e9b99e99e24c41e9e8949a5ae65fde6afab385
- evidence_id: ev-d04db2e7c8d8bde6
  kind: prior_review
  reference: reviews/structured/20261011T024637Z-mim-reconcile-all-batch-09/review.yaml
  locator: findings[finding_id=f-6575df5edeb084de]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-6575df5edeb084de in 20261011T024637Z-mim-reconcile-all-batch-09
  snapshot_sha256: cf46750874f1303863883723934bbe8b09ece8d62b1785ceab64bb0342a3cf11
assessments:
- assessment_id: a-3054cc24f15a6c05
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-1ab34fe74a6ec342
  evidence_ids:
  - ev-71839a060c186070
  - ev-9050c95cea28b636
  - ev-75b345fc10b8e8c7
  - ev-4b3b30e9b203bda0
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-461ec6236231578a
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-1ab34fe74a6ec342
  evidence_ids:
  - ev-9656d159cec9e375
  - ev-71839a060c186070
  - ev-881ee80926bb21d5
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T05:01:32Z;
    reviewed SHA-256=9ddd9edfd7d77a47df419c9239e9b99e99e24c41e9e8949a5ae65fde6afab385;
    current SHA-256=9ddd9edfd7d77a47df419c9239e9b99e99e24c41e9e8949a5ae65fde6afab385;
    hash_changed=False. Reports=["reports/yaml_record_review/Na-vanillate.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The exact CHEBI:132748
    sodium vanillate identity, structure, occurrence count, synonyms, and final exact
    row pass, but CARBON_SOURCE is provisional.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-9656d159cec9e375
    - ev-71839a060c186070
  - name: legacy-native-ids
    value: '["SEM:6f281a6a06e2b2f6444e","SEM:d11f0dbb4c82da05db54"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-71839a060c186070
    - ev-9656d159cec9e375
    - ev-881ee80926bb21d5
- assessment_id: a-81a43ad8b5551552
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-1ab34fe74a6ec342
  evidence_ids:
  - ev-9656d159cec9e375
  - ev-81a43ad8b5551552
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-9656d159cec9e375
    - ev-81a43ad8b5551552
findings:
- finding_id: rec-f-6575df5edeb084de
  issue_key: mim-reconciliation-role-support-1ab34fe74a6ec342
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Na-vanillate'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-1ab34fe74a6ec342
  evidence_ids:
  - ev-9656d159cec9e375
  - ev-81a43ad8b5551552
  - ev-d04db2e7c8d8bde6
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Na-vanillate.yaml
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
    finding_id: f-6575df5edeb084de
actions:
- action_id: rec-action-6575df5edeb084de
  description: 'Reassess prediction-only role support: Na-vanillate'
  finding_ids:
  - rec-f-6575df5edeb084de
  target_ids:
  - record-1ab34fe74a6ec342
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Na-vanillate.yaml
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
