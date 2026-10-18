# Per-record structured review: Disodium_Glutarate (data/ingredients/mapped/Disodium_Glutarate.yaml)

- Review: 20261017T083000Z-disodium-glutarate
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Disodium_Glutarate (data/ingredients/mapped/Disodium_Glutarate.yaml, record-5f067810724889a6, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Disodium_Glutarate.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Disodium_Glutarate.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-5f067810724889a6 | data/ingredients/mapped/Disodium_Glutarate.yaml | maintained | Disodium_Glutarate |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-5f067810724889a6 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-5f067810724889a6 | Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-5f067810724889a6 | Reconciled against predecessor batch review 20261011T024633Z-mim-reconcile-all-batch-05 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-5f067810724889a6.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-5f067810724889a6.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T15:02:55Z; reviewed SHA-256=e669d06340e36f5ec14af33944ccd04b8d5e97b6ba5ce27c25387fb2442ca912; current SHA-256=e669d06340e36f5ec14af33944ccd04b8d5e97b6ba5ce27c25387fb2442ca912; hash_changed=False. Reports=["reports/yaml_record_review/Disodium_Glutarate.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The local CAS and MeSH parent rows pass, but the carbon-source role is computational.

### Historical provisional-role concern

evidence: concern. Targets: record-5f067810724889a6.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-2b353a479b90d808: Reassess prediction-only role support: Disodium Glutarate

major / open / confirmed; issue key: mim-reconciliation-role-support-5f067810724889a6.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-2b353a479b90d808

Reassess prediction-only role support: Disodium Glutarate

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-5a7a781a5ca05f62 | data/ingredients/mapped/Disodium_Glutarate.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[904],"raw_equal":true},"docs_rows":[{"identifier":"cas:13521-83-0","line":906,"mapping_status":"MAPPED","ontology_id":"mesh:C000730144","preferred_term":"Disodium Glutarate"}],"identifier":"cas:13521-83-0","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"NARROW_MATCH","ontology_id":"mesh:C000730144","ontology_label":"sodium glutarate","ontology_source":"MESH"},"preferred_term":"Disodium Glutarate","sssom_rows":[{"data_row":1062,"object_id":"mesh:C000730144","object_label":"sodium glutarate","predicate_id":"skos:broadMatch"},{"data_row":1063,"object_id":"cas:13521-83-0","object_label":"Disodium Glutarate","predicate_id":"skos:exactMatch"},{"data_row":1064,"object_id":"kgmicrobe.compound:disodium_glutarate","object_label":"Disodium Glutarate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Disodium_Glutarate","synonym_count":0} |
| ev-69d4d2da2f2a0e1b | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [904] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-d84452ad5616464c | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Disodium_Glutarate; data-row positions=[1062, 1063, 1064] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1062,"object_id":"mesh:C000730144","object_label":"sodium glutarate","other":"","predicate_id":"skos:broadMatch","subject_id":"MIM:Disodium_Glutarate","validation_method":"manual:reconcile_sssom&#124;PREDICATE&#124;2026-09-20"},{"data_row":1063,"object_id":"cas:13521-83-0","object_label":"Disodium Glutarate","other":"CAS:13521-83-0","predicate_id":"skos:exactMatch","subject_id":"MIM:Disodium_Glutarate","validation_method":"none&#124;UNKNOWN_TERM&#124;2026-07-07"},{"data_row":1064,"object_id":"kgmicrobe.compound:disodium_glutarate","object_label":"Disodium Glutarate","other":"CAS:13521-83-0","predicate_id":"skos:exactMatch","subject_id":"MIM:Disodium_Glutarate","validation_method":"none&#124;UNKNOWN_TERM&#124;2026-07-07"}] |
| ev-61073360fc872947 | docs/data/mapped_ingredients.csv; CSV lines=[906] | supports | Published identity and count rows inspected: [{"identifier":"cas:13521-83-0","line":906,"mapping_quality":"NARROW_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"mesh:C000730144","preferred_term":"Disodium Glutarate","total_occurrences":"0"}] |
| ev-e76725cc76db2e5b | reports/yaml_record_review/Disodium_Glutarate.md; &#96;data/ingredients/mapped/Disodium_Glutarate.yaml&#96;:2; Verdict:4; Identity:10; Validation:24; Evidence:43; Completeness:72; Recommended Edits:82 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-835151a15936c34c | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[544,1389] | context_only | [{"current_record_sha256":"e669d06340e36f5ec14af33944ccd04b8d5e97b6ba5ce27c25387fb2442ca912","finding_id":"SEM:8679c296babb96cec91b","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"e669d06340e36f5ec14af33944ccd04b8d5e97b6ba5ce27c25387fb2442ca912","finding_id":"SEM:ef927e327de99ec099ac","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-db3508b4c03ceec3 | data/ingredients/mapped/Disodium_Glutarate.yaml; nutritional_roles[0] | supports | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[904],"raw_equal":true},"docs_rows":[{"identifier":"cas:13521-83-0","line":906,"mapping_status":"MAPPED","ontology_id":"mesh:C000730144","preferred_term":"Disodium Glutarate"}],"identifier":"cas:13521-83-0","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"NARROW_MATCH","ontology_id":"mesh:C000730144","ontology_label":"sodium glutarate","ontology_source":"MESH"},"preferred_term":"Disodium Glutarate","sssom_rows":[{"data_row":1062,"object_id":"mesh:C000730144","object_label":"sodium glutarate","predicate_id":"skos:broadMatch"},{"data_row":1063,"object_id":"cas:13521-83-0","object_label":"Disodium Glutarate","predicate_id":"skos:exactMatch"},{"data_row":1064,"object_id":"kgmicrobe.compound:disodium_glutarate","object_label":"Disodium Glutarate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Disodium_Glutarate","synonym_count":0} |
| ev-dcecc3488d1ca368 | reviews/structured/20261011T024633Z-mim-reconcile-all-batch-05/review.yaml; findings[finding_id=f-2b353a479b90d808] | context_only | Predecessor structured review finding f-2b353a479b90d808 in 20261011T024633Z-mim-reconcile-all-batch-05 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024633Z-mim-reconcile-all-batch-05.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-disodium-glutarate
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Disodium_Glutarate (data/ingredients/mapped/Disodium_Glutarate.yaml)'
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
summary: Per-record structured review for Disodium_Glutarate (data/ingredients/mapped/Disodium_Glutarate.yaml,
  record-5f067810724889a6, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Disodium_Glutarate.yaml
    sha256: e669d06340e36f5ec14af33944ccd04b8d5e97b6ba5ce27c25387fb2442ca912
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
  - path: reports/yaml_record_review/Disodium_Glutarate.md
    sha256: 58e51ccdf0a9f79736e8ab16491e304a10ce79e2ddf245be8150cd988b1c5193
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-5f067810724889a6
  path: data/ingredients/mapped/Disodium_Glutarate.yaml
  label: Disodium_Glutarate
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Disodium_Glutarate.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Disodium_Glutarate.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Disodium_Glutarate.yaml selected
    from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-5f067810724889a6
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-5f067810724889a6
  evidence_ids:
  - ev-5a7a781a5ca05f62
  - ev-69d4d2da2f2a0e1b
  - ev-d84452ad5616464c
  - ev-61073360fc872947
  - ev-db3508b4c03ceec3
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-5f067810724889a6
  evidence_ids:
  - ev-5a7a781a5ca05f62
  - ev-835151a15936c34c
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024633Z-mim-reconcile-all-batch-05
    and semantic review dispositions on HEAD.
  target_ids:
  - record-5f067810724889a6
  evidence_ids:
  - ev-e76725cc76db2e5b
  - ev-835151a15936c34c
  - ev-dcecc3488d1ca368
evidence:
- evidence_id: ev-5a7a781a5ca05f62
  kind: record_content
  reference: data/ingredients/mapped/Disodium_Glutarate.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[904],"raw_equal":true},"docs_rows":[{"identifier":"cas:13521-83-0","line":906,"mapping_status":"MAPPED","ontology_id":"mesh:C000730144","preferred_term":"Disodium
    Glutarate"}],"identifier":"cas:13521-83-0","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"NARROW_MATCH","ontology_id":"mesh:C000730144","ontology_label":"sodium
    glutarate","ontology_source":"MESH"},"preferred_term":"Disodium Glutarate","sssom_rows":[{"data_row":1062,"object_id":"mesh:C000730144","object_label":"sodium
    glutarate","predicate_id":"skos:broadMatch"},{"data_row":1063,"object_id":"cas:13521-83-0","object_label":"Disodium
    Glutarate","predicate_id":"skos:exactMatch"},{"data_row":1064,"object_id":"kgmicrobe.compound:disodium_glutarate","object_label":"Disodium
    Glutarate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Disodium_Glutarate","synonym_count":0}'
  snapshot_sha256: e669d06340e36f5ec14af33944ccd04b8d5e97b6ba5ce27c25387fb2442ca912
- evidence_id: ev-69d4d2da2f2a0e1b
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [904]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-d84452ad5616464c
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Disodium_Glutarate; data-row positions=[1062, 1063, 1064]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1062,"object_id":"mesh:C000730144","object_label":"sodium
    glutarate","other":"","predicate_id":"skos:broadMatch","subject_id":"MIM:Disodium_Glutarate","validation_method":"manual:reconcile_sssom|PREDICATE|2026-09-20"},{"data_row":1063,"object_id":"cas:13521-83-0","object_label":"Disodium
    Glutarate","other":"CAS:13521-83-0","predicate_id":"skos:exactMatch","subject_id":"MIM:Disodium_Glutarate","validation_method":"none|UNKNOWN_TERM|2026-07-07"},{"data_row":1064,"object_id":"kgmicrobe.compound:disodium_glutarate","object_label":"Disodium
    Glutarate","other":"CAS:13521-83-0","predicate_id":"skos:exactMatch","subject_id":"MIM:Disodium_Glutarate","validation_method":"none|UNKNOWN_TERM|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-61073360fc872947
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[906]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"cas:13521-83-0","line":906,"mapping_quality":"NARROW_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"mesh:C000730144","preferred_term":"Disodium
    Glutarate","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-e76725cc76db2e5b
  kind: prior_review
  reference: reports/yaml_record_review/Disodium_Glutarate.md
  locator: '`data/ingredients/mapped/Disodium_Glutarate.yaml`:2; Verdict:4; Identity:10;
    Validation:24; Evidence:43; Completeness:72; Recommended Edits:82'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 58e51ccdf0a9f79736e8ab16491e304a10ce79e2ddf245be8150cd988b1c5193
  quote: "Recommended Edits:\n- Major: in `data/ingredients/mapped/Disodium_Glutarate.yaml`,\
    \ either remove\n  `nutritional_roles.CARBON_SOURCE` or replace it with inspected\n\
    \  formulation-specific evidence that directly supports this exact ingredient\n\
    \  as a carbon source.\n- Minor: refresh the SSSOM MeSH validation method so it\
    \ no longer reports\n  `UNKNOWN_TERM` after the prefix-specific OLS resolution."
- evidence_id: ev-835151a15936c34c
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[544,1389]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"e669d06340e36f5ec14af33944ccd04b8d5e97b6ba5ce27c25387fb2442ca912","finding_id":"SEM:8679c296babb96cec91b","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"e669d06340e36f5ec14af33944ccd04b8d5e97b6ba5ce27c25387fb2442ca912","finding_id":"SEM:ef927e327de99ec099ac","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-db3508b4c03ceec3
  kind: record_content
  reference: data/ingredients/mapped/Disodium_Glutarate.yaml
  locator: nutritional_roles[0]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[904],"raw_equal":true},"docs_rows":[{"identifier":"cas:13521-83-0","line":906,"mapping_status":"MAPPED","ontology_id":"mesh:C000730144","preferred_term":"Disodium
    Glutarate"}],"identifier":"cas:13521-83-0","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"NARROW_MATCH","ontology_id":"mesh:C000730144","ontology_label":"sodium
    glutarate","ontology_source":"MESH"},"preferred_term":"Disodium Glutarate","sssom_rows":[{"data_row":1062,"object_id":"mesh:C000730144","object_label":"sodium
    glutarate","predicate_id":"skos:broadMatch"},{"data_row":1063,"object_id":"cas:13521-83-0","object_label":"Disodium
    Glutarate","predicate_id":"skos:exactMatch"},{"data_row":1064,"object_id":"kgmicrobe.compound:disodium_glutarate","object_label":"Disodium
    Glutarate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Disodium_Glutarate","synonym_count":0}'
  snapshot_sha256: e669d06340e36f5ec14af33944ccd04b8d5e97b6ba5ce27c25387fb2442ca912
- evidence_id: ev-dcecc3488d1ca368
  kind: prior_review
  reference: reviews/structured/20261011T024633Z-mim-reconcile-all-batch-05/review.yaml
  locator: findings[finding_id=f-2b353a479b90d808]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-2b353a479b90d808 in 20261011T024633Z-mim-reconcile-all-batch-05
  snapshot_sha256: 7549030a5b50ed98868ff3497507fdfbfecd07cd858c76738f734521fa9d3603
assessments:
- assessment_id: a-80e0ffad71c135c0
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-5f067810724889a6
  evidence_ids:
  - ev-5a7a781a5ca05f62
  - ev-69d4d2da2f2a0e1b
  - ev-d84452ad5616464c
  - ev-61073360fc872947
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-fb2ed61d11fe4eca
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-5f067810724889a6
  evidence_ids:
  - ev-e76725cc76db2e5b
  - ev-5a7a781a5ca05f62
  - ev-835151a15936c34c
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T15:02:55Z;
    reviewed SHA-256=e669d06340e36f5ec14af33944ccd04b8d5e97b6ba5ce27c25387fb2442ca912;
    current SHA-256=e669d06340e36f5ec14af33944ccd04b8d5e97b6ba5ce27c25387fb2442ca912;
    hash_changed=False. Reports=["reports/yaml_record_review/Disodium_Glutarate.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The local
    CAS and MeSH parent rows pass, but the carbon-source role is computational.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-e76725cc76db2e5b
    - ev-5a7a781a5ca05f62
  - name: legacy-native-ids
    value: '["SEM:8679c296babb96cec91b","SEM:ef927e327de99ec099ac"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-5a7a781a5ca05f62
    - ev-e76725cc76db2e5b
    - ev-835151a15936c34c
- assessment_id: a-db3508b4c03ceec3
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-5f067810724889a6
  evidence_ids:
  - ev-e76725cc76db2e5b
  - ev-db3508b4c03ceec3
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-e76725cc76db2e5b
    - ev-db3508b4c03ceec3
findings:
- finding_id: rec-f-2b353a479b90d808
  issue_key: mim-reconciliation-role-support-5f067810724889a6
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Disodium Glutarate'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-5f067810724889a6
  evidence_ids:
  - ev-e76725cc76db2e5b
  - ev-db3508b4c03ceec3
  - ev-dcecc3488d1ca368
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Disodium_Glutarate.yaml
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
    finding_id: f-2b353a479b90d808
actions:
- action_id: rec-action-2b353a479b90d808
  description: 'Reassess prediction-only role support: Disodium Glutarate'
  finding_ids:
  - rec-f-2b353a479b90d808
  target_ids:
  - record-5f067810724889a6
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Disodium_Glutarate.yaml
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
