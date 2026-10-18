# Per-record structured review: Pustulan_B-1-6_Glucan (data/ingredients/mapped/Pustulan_B-1-6_Glucan.yaml)

- Review: 20261017T083000Z-pustulan-b-1-6-glucan
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Pustulan_B-1-6_Glucan (data/ingredients/mapped/Pustulan_B-1-6_Glucan.yaml, record-9bb06b3779261c65, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Pustulan_B-1-6_Glucan.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Pustulan_B-1-6_Glucan.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-9bb06b3779261c65 | data/ingredients/mapped/Pustulan_B-1-6_Glucan.yaml | maintained | Pustulan_B-1-6_Glucan |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-9bb06b3779261c65 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-9bb06b3779261c65 | Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-9bb06b3779261c65 | Reconciled against predecessor batch review 20261011T024638Z-mim-reconcile-all-batch-10 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-9bb06b3779261c65.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-9bb06b3779261c65.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T10:53:18Z; reviewed SHA-256=8ae5ce3760e3280ab9be5a7951e95384837e02d1dab7bff423b7c0e45cca9993; current SHA-256=8ae5ce3760e3280ab9be5a7951e95384837e02d1dab7bff423b7c0e45cca9993; hash_changed=False. Reports=["reports/yaml_record_review/Pustulan_B-1-6_Glucan.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The CAS and kgmicrobe exact rows preserve the narrow MESH-parent identity, but CARBON_SOURCE is provisional.

### Historical provisional-role concern

evidence: concern. Targets: record-9bb06b3779261c65.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-c5f9d5185ce4ce6f: Reassess prediction-only role support: Pustulan (b-1-6 glucan)

major / open / confirmed; issue key: mim-reconciliation-role-support-9bb06b3779261c65.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-c5f9d5185ce4ce6f

Reassess prediction-only role support: Pustulan (b-1-6 glucan)

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-ca4ec2edc696043c | data/ingredients/mapped/Pustulan_B-1-6_Glucan.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1716],"raw_equal":true},"docs_rows":[{"identifier":"cas:37331-28-5","line":1718,"mapping_status":"MAPPED","ontology_id":"mesh:C002076","preferred_term":"Pustulan (b-1-6 glucan)"}],"identifier":"cas:37331-28-5","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"NARROW_MATCH","ontology_id":"mesh:C002076","ontology_label":"pustulan","ontology_source":"MESH"},"preferred_term":"Pustulan (b-1-6 glucan)","sssom_rows":[{"data_row":2369,"object_id":"mesh:C002076","object_label":"pustulan","predicate_id":"skos:broadMatch"},{"data_row":2370,"object_id":"cas:37331-28-5","object_label":"Pustulan (b-1-6 glucan)","predicate_id":"skos:exactMatch"},{"data_row":2371,"object_id":"kgmicrobe.compound:pustulan_b-1-6_glucan","object_label":"Pustulan (b-1-6 glucan)","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Pustulan_B-1-6_Glucan","synonym_count":0} |
| ev-5ea180660d8abec3 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1716] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-81171b7342cdb2c8 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Pustulan_B-1-6_Glucan; data-row positions=[2369, 2370, 2371] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":2369,"object_id":"mesh:C002076","object_label":"pustulan","other":"","predicate_id":"skos:broadMatch","subject_id":"MIM:Pustulan_B-1-6_Glucan","validation_method":"manual:reconcile_sssom&#124;PREDICATE&#124;2026-09-20"},{"data_row":2370,"object_id":"cas:37331-28-5","object_label":"Pustulan (b-1-6 glucan)","other":"CAS:37331-28-5","predicate_id":"skos:exactMatch","subject_id":"MIM:Pustulan_B-1-6_Glucan","validation_method":"none&#124;UNKNOWN_TERM&#124;2026-07-07"},{"data_row":2371,"object_id":"kgmicrobe.compound:pustulan_b-1-6_glucan","object_label":"Pustulan (b-1-6 glucan)","other":"CAS:37331-28-5","predicate_id":"skos:exactMatch","subject_id":"MIM:Pustulan_B-1-6_Glucan","validation_method":"none&#124;UNKNOWN_TERM&#124;2026-07-07"}] |
| ev-1cfe47d75743179f | docs/data/mapped_ingredients.csv; CSV lines=[1718] | supports | Published identity and count rows inspected: [{"identifier":"cas:37331-28-5","line":1718,"mapping_quality":"NARROW_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"mesh:C002076","preferred_term":"Pustulan (b-1-6 glucan)","total_occurrences":"0"}] |
| ev-66de0074f4b0b15e | reports/yaml_record_review/Pustulan_B-1-6_Glucan.md; &#96;data/ingredients/mapped/Pustulan_B-1-6_Glucan.yaml&#96;:2 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-eb508fc483f37927 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1147,1698] | context_only | [{"current_record_sha256":"8ae5ce3760e3280ab9be5a7951e95384837e02d1dab7bff423b7c0e45cca9993","finding_id":"SEM:79267864a518a20097c5","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"8ae5ce3760e3280ab9be5a7951e95384837e02d1dab7bff423b7c0e45cca9993","finding_id":"SEM:235c2299fcb24cd1fe93","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-69e68989f29559f4 | data/ingredients/mapped/Pustulan_B-1-6_Glucan.yaml; nutritional_roles[0] | supports | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1716],"raw_equal":true},"docs_rows":[{"identifier":"cas:37331-28-5","line":1718,"mapping_status":"MAPPED","ontology_id":"mesh:C002076","preferred_term":"Pustulan (b-1-6 glucan)"}],"identifier":"cas:37331-28-5","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"NARROW_MATCH","ontology_id":"mesh:C002076","ontology_label":"pustulan","ontology_source":"MESH"},"preferred_term":"Pustulan (b-1-6 glucan)","sssom_rows":[{"data_row":2369,"object_id":"mesh:C002076","object_label":"pustulan","predicate_id":"skos:broadMatch"},{"data_row":2370,"object_id":"cas:37331-28-5","object_label":"Pustulan (b-1-6 glucan)","predicate_id":"skos:exactMatch"},{"data_row":2371,"object_id":"kgmicrobe.compound:pustulan_b-1-6_glucan","object_label":"Pustulan (b-1-6 glucan)","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Pustulan_B-1-6_Glucan","synonym_count":0} |
| ev-320c6d6cbfcbcd7f | reviews/structured/20261011T024638Z-mim-reconcile-all-batch-10/review.yaml; findings[finding_id=f-c5f9d5185ce4ce6f] | context_only | Predecessor structured review finding f-c5f9d5185ce4ce6f in 20261011T024638Z-mim-reconcile-all-batch-10 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024638Z-mim-reconcile-all-batch-10.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-pustulan-b-1-6-glucan
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Pustulan_B-1-6_Glucan (data/ingredients/mapped/Pustulan_B-1-6_Glucan.yaml)'
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
summary: Per-record structured review for Pustulan_B-1-6_Glucan (data/ingredients/mapped/Pustulan_B-1-6_Glucan.yaml,
  record-9bb06b3779261c65, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Pustulan_B-1-6_Glucan.yaml
    sha256: 8ae5ce3760e3280ab9be5a7951e95384837e02d1dab7bff423b7c0e45cca9993
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
  - path: reports/yaml_record_review/Pustulan_B-1-6_Glucan.md
    sha256: 22380443948d5d06cd3409f97c6a97b4ede11d3afc42afb205a674e0a26972c4
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-9bb06b3779261c65
  path: data/ingredients/mapped/Pustulan_B-1-6_Glucan.yaml
  label: Pustulan_B-1-6_Glucan
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Pustulan_B-1-6_Glucan.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Pustulan_B-1-6_Glucan.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Pustulan_B-1-6_Glucan.yaml selected
    from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-9bb06b3779261c65
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-9bb06b3779261c65
  evidence_ids:
  - ev-ca4ec2edc696043c
  - ev-5ea180660d8abec3
  - ev-81171b7342cdb2c8
  - ev-1cfe47d75743179f
  - ev-69e68989f29559f4
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-9bb06b3779261c65
  evidence_ids:
  - ev-ca4ec2edc696043c
  - ev-eb508fc483f37927
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024638Z-mim-reconcile-all-batch-10
    and semantic review dispositions on HEAD.
  target_ids:
  - record-9bb06b3779261c65
  evidence_ids:
  - ev-66de0074f4b0b15e
  - ev-eb508fc483f37927
  - ev-320c6d6cbfcbcd7f
evidence:
- evidence_id: ev-ca4ec2edc696043c
  kind: record_content
  reference: data/ingredients/mapped/Pustulan_B-1-6_Glucan.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1716],"raw_equal":true},"docs_rows":[{"identifier":"cas:37331-28-5","line":1718,"mapping_status":"MAPPED","ontology_id":"mesh:C002076","preferred_term":"Pustulan
    (b-1-6 glucan)"}],"identifier":"cas:37331-28-5","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"NARROW_MATCH","ontology_id":"mesh:C002076","ontology_label":"pustulan","ontology_source":"MESH"},"preferred_term":"Pustulan
    (b-1-6 glucan)","sssom_rows":[{"data_row":2369,"object_id":"mesh:C002076","object_label":"pustulan","predicate_id":"skos:broadMatch"},{"data_row":2370,"object_id":"cas:37331-28-5","object_label":"Pustulan
    (b-1-6 glucan)","predicate_id":"skos:exactMatch"},{"data_row":2371,"object_id":"kgmicrobe.compound:pustulan_b-1-6_glucan","object_label":"Pustulan
    (b-1-6 glucan)","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Pustulan_B-1-6_Glucan","synonym_count":0}'
  snapshot_sha256: 8ae5ce3760e3280ab9be5a7951e95384837e02d1dab7bff423b7c0e45cca9993
- evidence_id: ev-5ea180660d8abec3
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1716]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-81171b7342cdb2c8
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Pustulan_B-1-6_Glucan; data-row positions=[2369, 2370, 2371]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":2369,"object_id":"mesh:C002076","object_label":"pustulan","other":"","predicate_id":"skos:broadMatch","subject_id":"MIM:Pustulan_B-1-6_Glucan","validation_method":"manual:reconcile_sssom|PREDICATE|2026-09-20"},{"data_row":2370,"object_id":"cas:37331-28-5","object_label":"Pustulan
    (b-1-6 glucan)","other":"CAS:37331-28-5","predicate_id":"skos:exactMatch","subject_id":"MIM:Pustulan_B-1-6_Glucan","validation_method":"none|UNKNOWN_TERM|2026-07-07"},{"data_row":2371,"object_id":"kgmicrobe.compound:pustulan_b-1-6_glucan","object_label":"Pustulan
    (b-1-6 glucan)","other":"CAS:37331-28-5","predicate_id":"skos:exactMatch","subject_id":"MIM:Pustulan_B-1-6_Glucan","validation_method":"none|UNKNOWN_TERM|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-1cfe47d75743179f
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1718]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"cas:37331-28-5","line":1718,"mapping_quality":"NARROW_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"mesh:C002076","preferred_term":"Pustulan
    (b-1-6 glucan)","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-66de0074f4b0b15e
  kind: prior_review
  reference: reports/yaml_record_review/Pustulan_B-1-6_Glucan.md
  locator: '`data/ingredients/mapped/Pustulan_B-1-6_Glucan.yaml`:2'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 22380443948d5d06cd3409f97c6a97b4ede11d3afc42afb205a674e0a26972c4
- evidence_id: ev-eb508fc483f37927
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1147,1698]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"8ae5ce3760e3280ab9be5a7951e95384837e02d1dab7bff423b7c0e45cca9993","finding_id":"SEM:79267864a518a20097c5","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"8ae5ce3760e3280ab9be5a7951e95384837e02d1dab7bff423b7c0e45cca9993","finding_id":"SEM:235c2299fcb24cd1fe93","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-69e68989f29559f4
  kind: record_content
  reference: data/ingredients/mapped/Pustulan_B-1-6_Glucan.yaml
  locator: nutritional_roles[0]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1716],"raw_equal":true},"docs_rows":[{"identifier":"cas:37331-28-5","line":1718,"mapping_status":"MAPPED","ontology_id":"mesh:C002076","preferred_term":"Pustulan
    (b-1-6 glucan)"}],"identifier":"cas:37331-28-5","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"NARROW_MATCH","ontology_id":"mesh:C002076","ontology_label":"pustulan","ontology_source":"MESH"},"preferred_term":"Pustulan
    (b-1-6 glucan)","sssom_rows":[{"data_row":2369,"object_id":"mesh:C002076","object_label":"pustulan","predicate_id":"skos:broadMatch"},{"data_row":2370,"object_id":"cas:37331-28-5","object_label":"Pustulan
    (b-1-6 glucan)","predicate_id":"skos:exactMatch"},{"data_row":2371,"object_id":"kgmicrobe.compound:pustulan_b-1-6_glucan","object_label":"Pustulan
    (b-1-6 glucan)","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Pustulan_B-1-6_Glucan","synonym_count":0}'
  snapshot_sha256: 8ae5ce3760e3280ab9be5a7951e95384837e02d1dab7bff423b7c0e45cca9993
- evidence_id: ev-320c6d6cbfcbcd7f
  kind: prior_review
  reference: reviews/structured/20261011T024638Z-mim-reconcile-all-batch-10/review.yaml
  locator: findings[finding_id=f-c5f9d5185ce4ce6f]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-c5f9d5185ce4ce6f in 20261011T024638Z-mim-reconcile-all-batch-10
  snapshot_sha256: 8c3aa2fca1269d1dbbf6117e85dea5b0de5047a8505841641245bd7ee99b936d
assessments:
- assessment_id: a-6fe67c14bdfc80fc
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-9bb06b3779261c65
  evidence_ids:
  - ev-ca4ec2edc696043c
  - ev-5ea180660d8abec3
  - ev-81171b7342cdb2c8
  - ev-1cfe47d75743179f
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-7a0b1ce941405b33
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-9bb06b3779261c65
  evidence_ids:
  - ev-66de0074f4b0b15e
  - ev-ca4ec2edc696043c
  - ev-eb508fc483f37927
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T10:53:18Z;
    reviewed SHA-256=8ae5ce3760e3280ab9be5a7951e95384837e02d1dab7bff423b7c0e45cca9993;
    current SHA-256=8ae5ce3760e3280ab9be5a7951e95384837e02d1dab7bff423b7c0e45cca9993;
    hash_changed=False. Reports=["reports/yaml_record_review/Pustulan_B-1-6_Glucan.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The CAS
    and kgmicrobe exact rows preserve the narrow MESH-parent identity, but CARBON_SOURCE
    is provisional.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-66de0074f4b0b15e
    - ev-ca4ec2edc696043c
  - name: legacy-native-ids
    value: '["SEM:79267864a518a20097c5","SEM:235c2299fcb24cd1fe93"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-ca4ec2edc696043c
    - ev-66de0074f4b0b15e
    - ev-eb508fc483f37927
- assessment_id: a-69e68989f29559f4
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-9bb06b3779261c65
  evidence_ids:
  - ev-66de0074f4b0b15e
  - ev-69e68989f29559f4
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-66de0074f4b0b15e
    - ev-69e68989f29559f4
findings:
- finding_id: rec-f-c5f9d5185ce4ce6f
  issue_key: mim-reconciliation-role-support-9bb06b3779261c65
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Pustulan (b-1-6 glucan)'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-9bb06b3779261c65
  evidence_ids:
  - ev-66de0074f4b0b15e
  - ev-69e68989f29559f4
  - ev-320c6d6cbfcbcd7f
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Pustulan_B-1-6_Glucan.yaml
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
    review_id: 20261011T024638Z-mim-reconcile-all-batch-10
    finding_id: f-c5f9d5185ce4ce6f
actions:
- action_id: rec-action-c5f9d5185ce4ce6f
  description: 'Reassess prediction-only role support: Pustulan (b-1-6 glucan)'
  finding_ids:
  - rec-f-c5f9d5185ce4ce6f
  target_ids:
  - record-9bb06b3779261c65
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Pustulan_B-1-6_Glucan.yaml
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
