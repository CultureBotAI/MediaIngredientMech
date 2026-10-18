# Per-record structured review: Potassium_Phosphate_Dibasic_Trihydrate (data/ingredients/mapped/Potassium_Phosphate_Dibasic_Trihydrate.yaml)

- Review: 20261017T083000Z-potassium-phosphate-dibasic-trihydrate
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Potassium_Phosphate_Dibasic_Trihydrate (data/ingredients/mapped/Potassium_Phosphate_Dibasic_Trihydrate.yaml, record-150204e8aee0de9c, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Potassium_Phosphate_Dibasic_Trihydrate.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Potassium_Phosphate_Dibasic_Trihydrate.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-150204e8aee0de9c | data/ingredients/mapped/Potassium_Phosphate_Dibasic_Trihydrate.yaml | maintained | Potassium_Phosphate_Dibasic_Trihydrate |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-150204e8aee0de9c | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-150204e8aee0de9c | Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-150204e8aee0de9c | Reconciled against predecessor batch review 20261011T024638Z-mim-reconcile-all-batch-10 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-150204e8aee0de9c.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-150204e8aee0de9c.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T10:23:25Z; reviewed SHA-256=c4fb96e92fd3ccbe4aa107fea350c8444633f992cf4758b5f21a6f86c804bc14; current SHA-256=c4fb96e92fd3ccbe4aa107fea350c8444633f992cf4758b5f21a6f86c804bc14; hash_changed=False. Reports=["reports/yaml_record_review/Potassium_Phosphate_Dibasic_Trihydrate.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The CAS trihydrate identity and final exact registry rows pass, but BUFFER is a provisional role.

### Historical provisional-role concern

evidence: concern. Targets: record-150204e8aee0de9c.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-07d147555d10a4a6: Reassess prediction-only role support: Potassium phosphate dibasic trihydrate

major / open / confirmed; issue key: mim-reconciliation-role-support-150204e8aee0de9c.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-07d147555d10a4a6

Reassess prediction-only role support: Potassium phosphate dibasic trihydrate

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-b2d6a730993c859a | data/ingredients/mapped/Potassium_Phosphate_Dibasic_Trihydrate.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1694],"raw_equal":true},"docs_rows":[{"identifier":"cas:16788-57-1","line":1696,"mapping_status":"MAPPED","ontology_id":"mesh:C013216","preferred_term":"Potassium phosphate dibasic trihydrate"}],"identifier":"cas:16788-57-1","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":3,"edge_count":3,"occurrences":3},"occurrence_statistics":{"media_count":3,"total_occurrences":3},"ontology_mapping":{"mapping_quality":"NARROW_MATCH","ontology_id":"mesh:C013216","ontology_label":"potassium phosphate","ontology_source":"MESH"},"preferred_term":"Potassium phosphate dibasic trihydrate","sssom_rows":[{"data_row":2331,"object_id":"mesh:C013216","object_label":"potassium phosphate","predicate_id":"skos:broadMatch"},{"data_row":2332,"object_id":"cas:16788-57-1","object_label":"Potassium phosphate dibasic trihydrate","predicate_id":"skos:exactMatch"},{"data_row":2333,"object_id":"kgmicrobe.compound:potassium_phosphate_dibasic_trihydrate","object_label":"Potassium phosphate dibasic trihydrate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Potassium_Phosphate_Dibasic_Trihydrate","synonym_count":0} |
| ev-91a282b2254061e1 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1694] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-28fcac26ca1febf4 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Potassium_Phosphate_Dibasic_Trihydrate; data-row positions=[2331, 2332, 2333] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":2331,"object_id":"mesh:C013216","object_label":"potassium phosphate","other":"","predicate_id":"skos:broadMatch","subject_id":"MIM:Potassium_Phosphate_Dibasic_Trihydrate","validation_method":"manual:reconcile_sssom&#124;PREDICATE&#124;2026-09-20"},{"data_row":2332,"object_id":"cas:16788-57-1","object_label":"Potassium phosphate dibasic trihydrate","other":"CAS:16788-57-1","predicate_id":"skos:exactMatch","subject_id":"MIM:Potassium_Phosphate_Dibasic_Trihydrate","validation_method":"none&#124;UNKNOWN_TERM&#124;2026-07-07"},{"data_row":2333,"object_id":"kgmicrobe.compound:potassium_phosphate_dibasic_trihydrate","object_label":"Potassium phosphate dibasic trihydrate","other":"CAS:16788-57-1","predicate_id":"skos:exactMatch","subject_id":"MIM:Potassium_Phosphate_Dibasic_Trihydrate","validation_method":"none&#124;UNKNOWN_TERM&#124;2026-07-07"}] |
| ev-00ccbaf7d62df0a5 | docs/data/mapped_ingredients.csv; CSV lines=[1696] | supports | Published identity and count rows inspected: [{"identifier":"cas:16788-57-1","line":1696,"mapping_quality":"NARROW_MATCH","mapping_status":"MAPPED","media_count":"3","ontology_id":"mesh:C013216","preferred_term":"Potassium phosphate dibasic trihydrate","total_occurrences":"3"}] |
| ev-b952c6f9de7b200f | reports/yaml_record_review/Potassium_Phosphate_Dibasic_Trihydrate.md; &#96;data/ingredients/mapped/Potassium_Phosphate_Dibasic_Trihydrate.yaml&#96;:2 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-3c660e8c61753617 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1139,1649] | context_only | [{"current_record_sha256":"c4fb96e92fd3ccbe4aa107fea350c8444633f992cf4758b5f21a6f86c804bc14","finding_id":"SEM:2593fb1d358b9120e634","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"c4fb96e92fd3ccbe4aa107fea350c8444633f992cf4758b5f21a6f86c804bc14","finding_id":"SEM:cfe6e0ceefc44b4dc23c","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-b1121f1e42f5e198 | data/ingredients/mapped/Potassium_Phosphate_Dibasic_Trihydrate.yaml; physicochemical_roles[0] | supports | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1694],"raw_equal":true},"docs_rows":[{"identifier":"cas:16788-57-1","line":1696,"mapping_status":"MAPPED","ontology_id":"mesh:C013216","preferred_term":"Potassium phosphate dibasic trihydrate"}],"identifier":"cas:16788-57-1","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":3,"edge_count":3,"occurrences":3},"occurrence_statistics":{"media_count":3,"total_occurrences":3},"ontology_mapping":{"mapping_quality":"NARROW_MATCH","ontology_id":"mesh:C013216","ontology_label":"potassium phosphate","ontology_source":"MESH"},"preferred_term":"Potassium phosphate dibasic trihydrate","sssom_rows":[{"data_row":2331,"object_id":"mesh:C013216","object_label":"potassium phosphate","predicate_id":"skos:broadMatch"},{"data_row":2332,"object_id":"cas:16788-57-1","object_label":"Potassium phosphate dibasic trihydrate","predicate_id":"skos:exactMatch"},{"data_row":2333,"object_id":"kgmicrobe.compound:potassium_phosphate_dibasic_trihydrate","object_label":"Potassium phosphate dibasic trihydrate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Potassium_Phosphate_Dibasic_Trihydrate","synonym_count":0} |
| ev-a0950c368f3a2a4e | reviews/structured/20261011T024638Z-mim-reconcile-all-batch-10/review.yaml; findings[finding_id=f-07d147555d10a4a6] | context_only | Predecessor structured review finding f-07d147555d10a4a6 in 20261011T024638Z-mim-reconcile-all-batch-10 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024638Z-mim-reconcile-all-batch-10.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-potassium-phosphate-dibasic-trihydrate
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Potassium_Phosphate_Dibasic_Trihydrate (data/ingredients/mapped/Potassium_Phosphate_Dibasic_Trihydrate.yaml)'
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
summary: Per-record structured review for Potassium_Phosphate_Dibasic_Trihydrate (data/ingredients/mapped/Potassium_Phosphate_Dibasic_Trihydrate.yaml,
  record-150204e8aee0de9c, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Potassium_Phosphate_Dibasic_Trihydrate.yaml
    sha256: c4fb96e92fd3ccbe4aa107fea350c8444633f992cf4758b5f21a6f86c804bc14
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
  - path: reports/yaml_record_review/Potassium_Phosphate_Dibasic_Trihydrate.md
    sha256: 1f95c8c7ede205733756df4c5046af3e931cd9fad43325bb8847a368480355e7
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-150204e8aee0de9c
  path: data/ingredients/mapped/Potassium_Phosphate_Dibasic_Trihydrate.yaml
  label: Potassium_Phosphate_Dibasic_Trihydrate
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Potassium_Phosphate_Dibasic_Trihydrate.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Potassium_Phosphate_Dibasic_Trihydrate.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Potassium_Phosphate_Dibasic_Trihydrate.yaml
    selected from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-150204e8aee0de9c
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-150204e8aee0de9c
  evidence_ids:
  - ev-b2d6a730993c859a
  - ev-91a282b2254061e1
  - ev-28fcac26ca1febf4
  - ev-00ccbaf7d62df0a5
  - ev-b1121f1e42f5e198
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-150204e8aee0de9c
  evidence_ids:
  - ev-b2d6a730993c859a
  - ev-3c660e8c61753617
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024638Z-mim-reconcile-all-batch-10
    and semantic review dispositions on HEAD.
  target_ids:
  - record-150204e8aee0de9c
  evidence_ids:
  - ev-b952c6f9de7b200f
  - ev-3c660e8c61753617
  - ev-a0950c368f3a2a4e
evidence:
- evidence_id: ev-b2d6a730993c859a
  kind: record_content
  reference: data/ingredients/mapped/Potassium_Phosphate_Dibasic_Trihydrate.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1694],"raw_equal":true},"docs_rows":[{"identifier":"cas:16788-57-1","line":1696,"mapping_status":"MAPPED","ontology_id":"mesh:C013216","preferred_term":"Potassium
    phosphate dibasic trihydrate"}],"identifier":"cas:16788-57-1","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":3,"edge_count":3,"occurrences":3},"occurrence_statistics":{"media_count":3,"total_occurrences":3},"ontology_mapping":{"mapping_quality":"NARROW_MATCH","ontology_id":"mesh:C013216","ontology_label":"potassium
    phosphate","ontology_source":"MESH"},"preferred_term":"Potassium phosphate dibasic
    trihydrate","sssom_rows":[{"data_row":2331,"object_id":"mesh:C013216","object_label":"potassium
    phosphate","predicate_id":"skos:broadMatch"},{"data_row":2332,"object_id":"cas:16788-57-1","object_label":"Potassium
    phosphate dibasic trihydrate","predicate_id":"skos:exactMatch"},{"data_row":2333,"object_id":"kgmicrobe.compound:potassium_phosphate_dibasic_trihydrate","object_label":"Potassium
    phosphate dibasic trihydrate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Potassium_Phosphate_Dibasic_Trihydrate","synonym_count":0}'
  snapshot_sha256: c4fb96e92fd3ccbe4aa107fea350c8444633f992cf4758b5f21a6f86c804bc14
- evidence_id: ev-91a282b2254061e1
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1694]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-28fcac26ca1febf4
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Potassium_Phosphate_Dibasic_Trihydrate; data-row positions=[2331,
    2332, 2333]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":2331,"object_id":"mesh:C013216","object_label":"potassium
    phosphate","other":"","predicate_id":"skos:broadMatch","subject_id":"MIM:Potassium_Phosphate_Dibasic_Trihydrate","validation_method":"manual:reconcile_sssom|PREDICATE|2026-09-20"},{"data_row":2332,"object_id":"cas:16788-57-1","object_label":"Potassium
    phosphate dibasic trihydrate","other":"CAS:16788-57-1","predicate_id":"skos:exactMatch","subject_id":"MIM:Potassium_Phosphate_Dibasic_Trihydrate","validation_method":"none|UNKNOWN_TERM|2026-07-07"},{"data_row":2333,"object_id":"kgmicrobe.compound:potassium_phosphate_dibasic_trihydrate","object_label":"Potassium
    phosphate dibasic trihydrate","other":"CAS:16788-57-1","predicate_id":"skos:exactMatch","subject_id":"MIM:Potassium_Phosphate_Dibasic_Trihydrate","validation_method":"none|UNKNOWN_TERM|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-00ccbaf7d62df0a5
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1696]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"cas:16788-57-1","line":1696,"mapping_quality":"NARROW_MATCH","mapping_status":"MAPPED","media_count":"3","ontology_id":"mesh:C013216","preferred_term":"Potassium
    phosphate dibasic trihydrate","total_occurrences":"3"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-b952c6f9de7b200f
  kind: prior_review
  reference: reports/yaml_record_review/Potassium_Phosphate_Dibasic_Trihydrate.md
  locator: '`data/ingredients/mapped/Potassium_Phosphate_Dibasic_Trihydrate.yaml`:2'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 1f95c8c7ede205733756df4c5046af3e931cd9fad43325bb8847a368480355e7
- evidence_id: ev-3c660e8c61753617
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1139,1649]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"c4fb96e92fd3ccbe4aa107fea350c8444633f992cf4758b5f21a6f86c804bc14","finding_id":"SEM:2593fb1d358b9120e634","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"c4fb96e92fd3ccbe4aa107fea350c8444633f992cf4758b5f21a6f86c804bc14","finding_id":"SEM:cfe6e0ceefc44b4dc23c","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-b1121f1e42f5e198
  kind: record_content
  reference: data/ingredients/mapped/Potassium_Phosphate_Dibasic_Trihydrate.yaml
  locator: physicochemical_roles[0]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1694],"raw_equal":true},"docs_rows":[{"identifier":"cas:16788-57-1","line":1696,"mapping_status":"MAPPED","ontology_id":"mesh:C013216","preferred_term":"Potassium
    phosphate dibasic trihydrate"}],"identifier":"cas:16788-57-1","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":3,"edge_count":3,"occurrences":3},"occurrence_statistics":{"media_count":3,"total_occurrences":3},"ontology_mapping":{"mapping_quality":"NARROW_MATCH","ontology_id":"mesh:C013216","ontology_label":"potassium
    phosphate","ontology_source":"MESH"},"preferred_term":"Potassium phosphate dibasic
    trihydrate","sssom_rows":[{"data_row":2331,"object_id":"mesh:C013216","object_label":"potassium
    phosphate","predicate_id":"skos:broadMatch"},{"data_row":2332,"object_id":"cas:16788-57-1","object_label":"Potassium
    phosphate dibasic trihydrate","predicate_id":"skos:exactMatch"},{"data_row":2333,"object_id":"kgmicrobe.compound:potassium_phosphate_dibasic_trihydrate","object_label":"Potassium
    phosphate dibasic trihydrate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Potassium_Phosphate_Dibasic_Trihydrate","synonym_count":0}'
  snapshot_sha256: c4fb96e92fd3ccbe4aa107fea350c8444633f992cf4758b5f21a6f86c804bc14
- evidence_id: ev-a0950c368f3a2a4e
  kind: prior_review
  reference: reviews/structured/20261011T024638Z-mim-reconcile-all-batch-10/review.yaml
  locator: findings[finding_id=f-07d147555d10a4a6]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-07d147555d10a4a6 in 20261011T024638Z-mim-reconcile-all-batch-10
  snapshot_sha256: 8c3aa2fca1269d1dbbf6117e85dea5b0de5047a8505841641245bd7ee99b936d
assessments:
- assessment_id: a-6176205d47e748e3
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-150204e8aee0de9c
  evidence_ids:
  - ev-b2d6a730993c859a
  - ev-91a282b2254061e1
  - ev-28fcac26ca1febf4
  - ev-00ccbaf7d62df0a5
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-b632eb290c9f9f2b
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-150204e8aee0de9c
  evidence_ids:
  - ev-b952c6f9de7b200f
  - ev-b2d6a730993c859a
  - ev-3c660e8c61753617
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T10:23:25Z;
    reviewed SHA-256=c4fb96e92fd3ccbe4aa107fea350c8444633f992cf4758b5f21a6f86c804bc14;
    current SHA-256=c4fb96e92fd3ccbe4aa107fea350c8444633f992cf4758b5f21a6f86c804bc14;
    hash_changed=False. Reports=["reports/yaml_record_review/Potassium_Phosphate_Dibasic_Trihydrate.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The CAS
    trihydrate identity and final exact registry rows pass, but BUFFER is a provisional
    role.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-b952c6f9de7b200f
    - ev-b2d6a730993c859a
  - name: legacy-native-ids
    value: '["SEM:2593fb1d358b9120e634","SEM:cfe6e0ceefc44b4dc23c"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-b2d6a730993c859a
    - ev-b952c6f9de7b200f
    - ev-3c660e8c61753617
- assessment_id: a-b1121f1e42f5e198
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-150204e8aee0de9c
  evidence_ids:
  - ev-b952c6f9de7b200f
  - ev-b1121f1e42f5e198
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-b952c6f9de7b200f
    - ev-b1121f1e42f5e198
findings:
- finding_id: rec-f-07d147555d10a4a6
  issue_key: mim-reconciliation-role-support-150204e8aee0de9c
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Potassium phosphate dibasic trihydrate'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-150204e8aee0de9c
  evidence_ids:
  - ev-b952c6f9de7b200f
  - ev-b1121f1e42f5e198
  - ev-a0950c368f3a2a4e
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Potassium_Phosphate_Dibasic_Trihydrate.yaml
    role: maintained ingredient
  field_paths:
  - physicochemical_roles[0]
  tags:
  - reconciliation
  - bundle-by-owner
  - role-support
  external_issues:
  - https://github.com/CultureBotAI/MediaIngredientMech/issues/718
  previous_occurrences:
  - repository: CultureBotAI/MediaIngredientMech
    review_id: 20261011T024638Z-mim-reconcile-all-batch-10
    finding_id: f-07d147555d10a4a6
actions:
- action_id: rec-action-07d147555d10a4a6
  description: 'Reassess prediction-only role support: Potassium phosphate dibasic
    trihydrate'
  finding_ids:
  - rec-f-07d147555d10a4a6
  target_ids:
  - record-150204e8aee0de9c
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Potassium_Phosphate_Dibasic_Trihydrate.yaml
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
