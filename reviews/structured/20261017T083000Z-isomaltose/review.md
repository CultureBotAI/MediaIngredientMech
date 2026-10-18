# Per-record structured review: Isomaltose (data/ingredients/mapped/Isomaltose.yaml)

- Review: 20261017T083000Z-isomaltose
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Isomaltose (data/ingredients/mapped/Isomaltose.yaml, record-954063b3026fbf9a, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Isomaltose.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Isomaltose.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-954063b3026fbf9a | data/ingredients/mapped/Isomaltose.yaml | maintained | Isomaltose |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-954063b3026fbf9a | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-954063b3026fbf9a | Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-954063b3026fbf9a | Reconciled against predecessor batch review 20261011T024635Z-mim-reconcile-all-batch-07 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-954063b3026fbf9a.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-954063b3026fbf9a.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T20:52:29Z; reviewed SHA-256=e43dd40cf6d94f70f53b8e1c3ae4a324eb3aba3651b0473040679f165ce3d32b; current SHA-256=e43dd40cf6d94f70f53b8e1c3ae4a324eb3aba3651b0473040679f165ce3d32b; hash_changed=False. Reports=["reports/yaml_record_review/Isomaltose.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact isomaltose identity, CAS alias, structure fields, exact synonym, and final SSSOM row pass, but CARBON_SOURCE is only a provisional ChEBI-ancestry assertion.

### Historical provisional-role concern

evidence: concern. Targets: record-954063b3026fbf9a.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-fff06409463dd0bd: Reassess prediction-only role support: Isomaltose

major / open / confirmed; issue key: mim-reconciliation-role-support-954063b3026fbf9a.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-fff06409463dd0bd

Reassess prediction-only role support: Isomaltose

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-1d1ebeacd016a05e | data/ingredients/mapped/Isomaltose.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1175],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:28189","line":1177,"mapping_status":"MAPPED","ontology_id":"CHEBI:28189","preferred_term":"Isomaltose"}],"identifier":"CHEBI:28189","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:28189","ontology_label":"isomaltose","ontology_source":"CHEBI"},"preferred_term":"Isomaltose","sssom_rows":[{"data_row":1504,"object_id":"CHEBI:28189","object_label":"isomaltose","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Isomaltose","synonym_count":1} |
| ev-d4cf8086d590375c | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1175] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-7d961f2dc07147ef | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Isomaltose; data-row positions=[1504] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1504,"object_id":"CHEBI:28189","object_label":"isomaltose","other":"alpha-D-glucopyranosyl-(1-&gt;6)-D-glucopyranose&#124;CAS:499-40-1","predicate_id":"skos:exactMatch","subject_id":"MIM:Isomaltose","validation_method":"OAK+OLS:chebi&#124;CONFIRMED&#124;2026-07-07"}] |
| ev-7406eed76892e72a | docs/data/mapped_ingredients.csv; CSV lines=[1177] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:28189","line":1177,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:28189","preferred_term":"Isomaltose","total_occurrences":"0"}] |
| ev-ac1768e4df2f4817 | reports/yaml_record_review/Isomaltose.md; &#96;data/ingredients/mapped/Isomaltose.yaml&#96;:2; Verdict:4; Identity:10; Validation:22; Evidence:35; Completeness:53; Recommended Edits:60 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-4198670ca624e78c | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[752,1694] | context_only | [{"current_record_sha256":"e43dd40cf6d94f70f53b8e1c3ae4a324eb3aba3651b0473040679f165ce3d32b","finding_id":"SEM:68c3725d1f0ed98d4cbb","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"e43dd40cf6d94f70f53b8e1c3ae4a324eb3aba3651b0473040679f165ce3d32b","finding_id":"SEM:df5636a882590543c687","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-d8a9370580a69a35 | data/ingredients/mapped/Isomaltose.yaml; nutritional_roles[0] | supports | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1175],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:28189","line":1177,"mapping_status":"MAPPED","ontology_id":"CHEBI:28189","preferred_term":"Isomaltose"}],"identifier":"CHEBI:28189","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:28189","ontology_label":"isomaltose","ontology_source":"CHEBI"},"preferred_term":"Isomaltose","sssom_rows":[{"data_row":1504,"object_id":"CHEBI:28189","object_label":"isomaltose","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Isomaltose","synonym_count":1} |
| ev-11b978e9d61a9156 | reviews/structured/20261011T024635Z-mim-reconcile-all-batch-07/review.yaml; findings[finding_id=f-fff06409463dd0bd] | context_only | Predecessor structured review finding f-fff06409463dd0bd in 20261011T024635Z-mim-reconcile-all-batch-07 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024635Z-mim-reconcile-all-batch-07.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-isomaltose
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Isomaltose (data/ingredients/mapped/Isomaltose.yaml)'
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
summary: Per-record structured review for Isomaltose (data/ingredients/mapped/Isomaltose.yaml,
  record-954063b3026fbf9a, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Isomaltose.yaml
    sha256: e43dd40cf6d94f70f53b8e1c3ae4a324eb3aba3651b0473040679f165ce3d32b
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
  - path: reports/yaml_record_review/Isomaltose.md
    sha256: e3c74de406bc9573a29912dc3cc72959b9e65ffcf61a73e0c23841f88100dca0
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-954063b3026fbf9a
  path: data/ingredients/mapped/Isomaltose.yaml
  label: Isomaltose
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Isomaltose.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Isomaltose.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Isomaltose.yaml selected from full-corpus
    review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-954063b3026fbf9a
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-954063b3026fbf9a
  evidence_ids:
  - ev-1d1ebeacd016a05e
  - ev-d4cf8086d590375c
  - ev-7d961f2dc07147ef
  - ev-7406eed76892e72a
  - ev-d8a9370580a69a35
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-954063b3026fbf9a
  evidence_ids:
  - ev-1d1ebeacd016a05e
  - ev-4198670ca624e78c
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024635Z-mim-reconcile-all-batch-07
    and semantic review dispositions on HEAD.
  target_ids:
  - record-954063b3026fbf9a
  evidence_ids:
  - ev-ac1768e4df2f4817
  - ev-4198670ca624e78c
  - ev-11b978e9d61a9156
evidence:
- evidence_id: ev-1d1ebeacd016a05e
  kind: record_content
  reference: data/ingredients/mapped/Isomaltose.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1175],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:28189","line":1177,"mapping_status":"MAPPED","ontology_id":"CHEBI:28189","preferred_term":"Isomaltose"}],"identifier":"CHEBI:28189","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:28189","ontology_label":"isomaltose","ontology_source":"CHEBI"},"preferred_term":"Isomaltose","sssom_rows":[{"data_row":1504,"object_id":"CHEBI:28189","object_label":"isomaltose","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Isomaltose","synonym_count":1}'
  snapshot_sha256: e43dd40cf6d94f70f53b8e1c3ae4a324eb3aba3651b0473040679f165ce3d32b
- evidence_id: ev-d4cf8086d590375c
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1175]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-7d961f2dc07147ef
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Isomaltose; data-row positions=[1504]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1504,"object_id":"CHEBI:28189","object_label":"isomaltose","other":"alpha-D-glucopyranosyl-(1->6)-D-glucopyranose|CAS:499-40-1","predicate_id":"skos:exactMatch","subject_id":"MIM:Isomaltose","validation_method":"OAK+OLS:chebi|CONFIRMED|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-7406eed76892e72a
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1177]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:28189","line":1177,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:28189","preferred_term":"Isomaltose","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-ac1768e4df2f4817
  kind: prior_review
  reference: reports/yaml_record_review/Isomaltose.md
  locator: '`data/ingredients/mapped/Isomaltose.yaml`:2; Verdict:4; Identity:10; Validation:22;
    Evidence:35; Completeness:53; Recommended Edits:60'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: e3c74de406bc9573a29912dc3cc72959b9e65ffcf61a73e0c23841f88100dca0
  quote: "Recommended Edits:\n- Major: remove `nutritional_roles.CARBON_SOURCE` unless\
    \ an inspected\n  CultureMech, FEBA, Hans80, or literature source can support\
    \ isomaltose as a\n  carbon source, then rerun strict, term, round-trip, id-label,\
    \ component, and\n  SSSOM validation."
- evidence_id: ev-4198670ca624e78c
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[752,1694]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"e43dd40cf6d94f70f53b8e1c3ae4a324eb3aba3651b0473040679f165ce3d32b","finding_id":"SEM:68c3725d1f0ed98d4cbb","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"e43dd40cf6d94f70f53b8e1c3ae4a324eb3aba3651b0473040679f165ce3d32b","finding_id":"SEM:df5636a882590543c687","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-d8a9370580a69a35
  kind: record_content
  reference: data/ingredients/mapped/Isomaltose.yaml
  locator: nutritional_roles[0]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1175],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:28189","line":1177,"mapping_status":"MAPPED","ontology_id":"CHEBI:28189","preferred_term":"Isomaltose"}],"identifier":"CHEBI:28189","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:28189","ontology_label":"isomaltose","ontology_source":"CHEBI"},"preferred_term":"Isomaltose","sssom_rows":[{"data_row":1504,"object_id":"CHEBI:28189","object_label":"isomaltose","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Isomaltose","synonym_count":1}'
  snapshot_sha256: e43dd40cf6d94f70f53b8e1c3ae4a324eb3aba3651b0473040679f165ce3d32b
- evidence_id: ev-11b978e9d61a9156
  kind: prior_review
  reference: reviews/structured/20261011T024635Z-mim-reconcile-all-batch-07/review.yaml
  locator: findings[finding_id=f-fff06409463dd0bd]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-fff06409463dd0bd in 20261011T024635Z-mim-reconcile-all-batch-07
  snapshot_sha256: 408ad5bf1e58ddc25c06da54ed69bc719d6d61336a106fc7534b0954417618be
assessments:
- assessment_id: a-9e55359f9931fd20
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-954063b3026fbf9a
  evidence_ids:
  - ev-1d1ebeacd016a05e
  - ev-d4cf8086d590375c
  - ev-7d961f2dc07147ef
  - ev-7406eed76892e72a
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-847f5c14b6fca1ab
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-954063b3026fbf9a
  evidence_ids:
  - ev-ac1768e4df2f4817
  - ev-1d1ebeacd016a05e
  - ev-4198670ca624e78c
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T20:52:29Z;
    reviewed SHA-256=e43dd40cf6d94f70f53b8e1c3ae4a324eb3aba3651b0473040679f165ce3d32b;
    current SHA-256=e43dd40cf6d94f70f53b8e1c3ae4a324eb3aba3651b0473040679f165ce3d32b;
    hash_changed=False. Reports=["reports/yaml_record_review/Isomaltose.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The exact isomaltose
    identity, CAS alias, structure fields, exact synonym, and final SSSOM row pass,
    but CARBON_SOURCE is only a provisional ChEBI-ancestry assertion.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-ac1768e4df2f4817
    - ev-1d1ebeacd016a05e
  - name: legacy-native-ids
    value: '["SEM:68c3725d1f0ed98d4cbb","SEM:df5636a882590543c687"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-1d1ebeacd016a05e
    - ev-ac1768e4df2f4817
    - ev-4198670ca624e78c
- assessment_id: a-d8a9370580a69a35
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-954063b3026fbf9a
  evidence_ids:
  - ev-ac1768e4df2f4817
  - ev-d8a9370580a69a35
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-ac1768e4df2f4817
    - ev-d8a9370580a69a35
findings:
- finding_id: rec-f-fff06409463dd0bd
  issue_key: mim-reconciliation-role-support-954063b3026fbf9a
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Isomaltose'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-954063b3026fbf9a
  evidence_ids:
  - ev-ac1768e4df2f4817
  - ev-d8a9370580a69a35
  - ev-11b978e9d61a9156
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Isomaltose.yaml
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
    review_id: 20261011T024635Z-mim-reconcile-all-batch-07
    finding_id: f-fff06409463dd0bd
actions:
- action_id: rec-action-fff06409463dd0bd
  description: 'Reassess prediction-only role support: Isomaltose'
  finding_ids:
  - rec-f-fff06409463dd0bd
  target_ids:
  - record-954063b3026fbf9a
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Isomaltose.yaml
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
