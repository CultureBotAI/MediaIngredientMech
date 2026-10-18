# Per-record structured review: Phosphomycin_Disodium_Salt (data/ingredients/mapped/Phosphomycin_Disodium_Salt.yaml)

- Review: 20261017T083000Z-phosphomycin-disodium-salt
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Phosphomycin_Disodium_Salt (data/ingredients/mapped/Phosphomycin_Disodium_Salt.yaml, record-9b5c335508dd6a03, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Phosphomycin_Disodium_Salt.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Phosphomycin_Disodium_Salt.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-9b5c335508dd6a03 | data/ingredients/mapped/Phosphomycin_Disodium_Salt.yaml | maintained | Phosphomycin_Disodium_Salt |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-9b5c335508dd6a03 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-9b5c335508dd6a03 | Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-9b5c335508dd6a03 | Reconciled against predecessor batch review 20261011T024638Z-mim-reconcile-all-batch-10 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-9b5c335508dd6a03.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-9b5c335508dd6a03.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T09:21:30Z; reviewed SHA-256=708c721ef6206ab2e92e3d797a8e632bb593840dc9c915a183fa9a594e37c61c; current SHA-256=708c721ef6206ab2e92e3d797a8e632bb593840dc9c915a183fa9a594e37c61c; hash_changed=False. Reports=["reports/yaml_record_review/Phosphomycin_Disodium_Salt.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The CAS fallback identity is sound, but SELECTIVE_AGENT is provisional.

### Historical provisional-role concern

evidence: concern. Targets: record-9b5c335508dd6a03.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-2b3e6c85c9fd295a: Reassess prediction-only role support: Phosphomycin disodium salt

major / open / confirmed; issue key: mim-reconciliation-role-support-9b5c335508dd6a03.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-2b3e6c85c9fd295a

Reassess prediction-only role support: Phosphomycin disodium salt

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-fc767d5cf5b64c96 | data/ingredients/mapped/Phosphomycin_Disodium_Salt.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1651],"raw_equal":true},"docs_rows":[{"identifier":"cas:26016-99-9","line":1653,"mapping_status":"MAPPED","ontology_id":"cas:26016-99-9","preferred_term":"Phosphomycin disodium salt"}],"identifier":"cas:26016-99-9","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"FALLBACK_REGISTRY","ontology_id":"cas:26016-99-9","ontology_label":"Phosphomycin disodium salt","ontology_source":"CAS"},"preferred_term":"Phosphomycin disodium salt","sssom_rows":[{"data_row":2252,"object_id":"cas:26016-99-9","object_label":"Phosphomycin disodium salt","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Phosphomycin_Disodium_Salt","synonym_count":0} |
| ev-4025e397ef148fa5 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1651] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-090ca11382eae041 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Phosphomycin_Disodium_Salt; data-row positions=[2252] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":2252,"object_id":"cas:26016-99-9","object_label":"Phosphomycin disodium salt","other":"CAS:26016-99-9","predicate_id":"skos:exactMatch","subject_id":"MIM:Phosphomycin_Disodium_Salt","validation_method":"none&#124;UNKNOWN_TERM&#124;2026-07-07"}] |
| ev-ad52004722217e47 | docs/data/mapped_ingredients.csv; CSV lines=[1653] | supports | Published identity and count rows inspected: [{"identifier":"cas:26016-99-9","line":1653,"mapping_quality":"FALLBACK_REGISTRY","mapping_status":"MAPPED","media_count":"0","ontology_id":"cas:26016-99-9","preferred_term":"Phosphomycin disodium salt","total_occurrences":"0"}] |
| ev-92bed7e5eb367047 | reports/yaml_record_review/Phosphomycin_Disodium_Salt.md; &#96;data/ingredients/mapped/Phosphomycin_Disodium_Salt.yaml&#96;:2; Verdict:4; Identity:10; Validation:20; Evidence:30; Completeness:42; Recommended Edits:49 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-1d176e301aaf0442 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1111,1375] | context_only | [{"current_record_sha256":"708c721ef6206ab2e92e3d797a8e632bb593840dc9c915a183fa9a594e37c61c","finding_id":"SEM:6e0d1dd054403bc0322c","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"708c721ef6206ab2e92e3d797a8e632bb593840dc9c915a183fa9a594e37c61c","finding_id":"SEM:b96091839c797e72b805","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-b764eb1575bd5f61 | data/ingredients/mapped/Phosphomycin_Disodium_Salt.yaml; physicochemical_roles[0] | supports | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1651],"raw_equal":true},"docs_rows":[{"identifier":"cas:26016-99-9","line":1653,"mapping_status":"MAPPED","ontology_id":"cas:26016-99-9","preferred_term":"Phosphomycin disodium salt"}],"identifier":"cas:26016-99-9","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"FALLBACK_REGISTRY","ontology_id":"cas:26016-99-9","ontology_label":"Phosphomycin disodium salt","ontology_source":"CAS"},"preferred_term":"Phosphomycin disodium salt","sssom_rows":[{"data_row":2252,"object_id":"cas:26016-99-9","object_label":"Phosphomycin disodium salt","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Phosphomycin_Disodium_Salt","synonym_count":0} |
| ev-7dd1245397d2c66d | reviews/structured/20261011T024638Z-mim-reconcile-all-batch-10/review.yaml; findings[finding_id=f-2b3e6c85c9fd295a] | context_only | Predecessor structured review finding f-2b3e6c85c9fd295a in 20261011T024638Z-mim-reconcile-all-batch-10 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024638Z-mim-reconcile-all-batch-10.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-phosphomycin-disodium-salt
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Phosphomycin_Disodium_Salt (data/ingredients/mapped/Phosphomycin_Disodium_Salt.yaml)'
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
summary: Per-record structured review for Phosphomycin_Disodium_Salt (data/ingredients/mapped/Phosphomycin_Disodium_Salt.yaml,
  record-9b5c335508dd6a03, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Phosphomycin_Disodium_Salt.yaml
    sha256: 708c721ef6206ab2e92e3d797a8e632bb593840dc9c915a183fa9a594e37c61c
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
  - path: reports/yaml_record_review/Phosphomycin_Disodium_Salt.md
    sha256: c1b0ec3d2408cd41d8a31348157185206e4fcbef83f9b057aa4f1bcff4a9f35c
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-9b5c335508dd6a03
  path: data/ingredients/mapped/Phosphomycin_Disodium_Salt.yaml
  label: Phosphomycin_Disodium_Salt
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Phosphomycin_Disodium_Salt.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Phosphomycin_Disodium_Salt.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Phosphomycin_Disodium_Salt.yaml
    selected from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-9b5c335508dd6a03
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-9b5c335508dd6a03
  evidence_ids:
  - ev-fc767d5cf5b64c96
  - ev-4025e397ef148fa5
  - ev-090ca11382eae041
  - ev-ad52004722217e47
  - ev-b764eb1575bd5f61
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-9b5c335508dd6a03
  evidence_ids:
  - ev-fc767d5cf5b64c96
  - ev-1d176e301aaf0442
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024638Z-mim-reconcile-all-batch-10
    and semantic review dispositions on HEAD.
  target_ids:
  - record-9b5c335508dd6a03
  evidence_ids:
  - ev-92bed7e5eb367047
  - ev-1d176e301aaf0442
  - ev-7dd1245397d2c66d
evidence:
- evidence_id: ev-fc767d5cf5b64c96
  kind: record_content
  reference: data/ingredients/mapped/Phosphomycin_Disodium_Salt.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1651],"raw_equal":true},"docs_rows":[{"identifier":"cas:26016-99-9","line":1653,"mapping_status":"MAPPED","ontology_id":"cas:26016-99-9","preferred_term":"Phosphomycin
    disodium salt"}],"identifier":"cas:26016-99-9","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"FALLBACK_REGISTRY","ontology_id":"cas:26016-99-9","ontology_label":"Phosphomycin
    disodium salt","ontology_source":"CAS"},"preferred_term":"Phosphomycin disodium
    salt","sssom_rows":[{"data_row":2252,"object_id":"cas:26016-99-9","object_label":"Phosphomycin
    disodium salt","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Phosphomycin_Disodium_Salt","synonym_count":0}'
  snapshot_sha256: 708c721ef6206ab2e92e3d797a8e632bb593840dc9c915a183fa9a594e37c61c
- evidence_id: ev-4025e397ef148fa5
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1651]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-090ca11382eae041
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Phosphomycin_Disodium_Salt; data-row positions=[2252]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":2252,"object_id":"cas:26016-99-9","object_label":"Phosphomycin
    disodium salt","other":"CAS:26016-99-9","predicate_id":"skos:exactMatch","subject_id":"MIM:Phosphomycin_Disodium_Salt","validation_method":"none|UNKNOWN_TERM|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-ad52004722217e47
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1653]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"cas:26016-99-9","line":1653,"mapping_quality":"FALLBACK_REGISTRY","mapping_status":"MAPPED","media_count":"0","ontology_id":"cas:26016-99-9","preferred_term":"Phosphomycin
    disodium salt","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-92bed7e5eb367047
  kind: prior_review
  reference: reports/yaml_record_review/Phosphomycin_Disodium_Salt.md
  locator: '`data/ingredients/mapped/Phosphomycin_Disodium_Salt.yaml`:2; Verdict:4;
    Identity:10; Validation:20; Evidence:30; Completeness:42; Recommended Edits:49'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: c1b0ec3d2408cd41d8a31348157185206e4fcbef83f9b057aa4f1bcff4a9f35c
  quote: "Recommended Edits:\n- Major: in `data/ingredients/mapped/Phosphomycin_Disodium_Salt.yaml`,\
    \ replace\n  `physicochemical_roles.SELECTIVE_AGENT` with source-backed evidence\
    \ or remove\n  the provisional role facet until it is curated."
- evidence_id: ev-1d176e301aaf0442
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1111,1375]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"708c721ef6206ab2e92e3d797a8e632bb593840dc9c915a183fa9a594e37c61c","finding_id":"SEM:6e0d1dd054403bc0322c","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"708c721ef6206ab2e92e3d797a8e632bb593840dc9c915a183fa9a594e37c61c","finding_id":"SEM:b96091839c797e72b805","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-b764eb1575bd5f61
  kind: record_content
  reference: data/ingredients/mapped/Phosphomycin_Disodium_Salt.yaml
  locator: physicochemical_roles[0]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1651],"raw_equal":true},"docs_rows":[{"identifier":"cas:26016-99-9","line":1653,"mapping_status":"MAPPED","ontology_id":"cas:26016-99-9","preferred_term":"Phosphomycin
    disodium salt"}],"identifier":"cas:26016-99-9","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"FALLBACK_REGISTRY","ontology_id":"cas:26016-99-9","ontology_label":"Phosphomycin
    disodium salt","ontology_source":"CAS"},"preferred_term":"Phosphomycin disodium
    salt","sssom_rows":[{"data_row":2252,"object_id":"cas:26016-99-9","object_label":"Phosphomycin
    disodium salt","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Phosphomycin_Disodium_Salt","synonym_count":0}'
  snapshot_sha256: 708c721ef6206ab2e92e3d797a8e632bb593840dc9c915a183fa9a594e37c61c
- evidence_id: ev-7dd1245397d2c66d
  kind: prior_review
  reference: reviews/structured/20261011T024638Z-mim-reconcile-all-batch-10/review.yaml
  locator: findings[finding_id=f-2b3e6c85c9fd295a]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-2b3e6c85c9fd295a in 20261011T024638Z-mim-reconcile-all-batch-10
  snapshot_sha256: 8c3aa2fca1269d1dbbf6117e85dea5b0de5047a8505841641245bd7ee99b936d
assessments:
- assessment_id: a-3051017676fc0c12
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-9b5c335508dd6a03
  evidence_ids:
  - ev-fc767d5cf5b64c96
  - ev-4025e397ef148fa5
  - ev-090ca11382eae041
  - ev-ad52004722217e47
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-41aae61d01c47a48
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-9b5c335508dd6a03
  evidence_ids:
  - ev-92bed7e5eb367047
  - ev-fc767d5cf5b64c96
  - ev-1d176e301aaf0442
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T09:21:30Z;
    reviewed SHA-256=708c721ef6206ab2e92e3d797a8e632bb593840dc9c915a183fa9a594e37c61c;
    current SHA-256=708c721ef6206ab2e92e3d797a8e632bb593840dc9c915a183fa9a594e37c61c;
    hash_changed=False. Reports=["reports/yaml_record_review/Phosphomycin_Disodium_Salt.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The CAS
    fallback identity is sound, but SELECTIVE_AGENT is provisional.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-92bed7e5eb367047
    - ev-fc767d5cf5b64c96
  - name: legacy-native-ids
    value: '["SEM:6e0d1dd054403bc0322c","SEM:b96091839c797e72b805"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-fc767d5cf5b64c96
    - ev-92bed7e5eb367047
    - ev-1d176e301aaf0442
- assessment_id: a-b764eb1575bd5f61
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-9b5c335508dd6a03
  evidence_ids:
  - ev-92bed7e5eb367047
  - ev-b764eb1575bd5f61
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-92bed7e5eb367047
    - ev-b764eb1575bd5f61
findings:
- finding_id: rec-f-2b3e6c85c9fd295a
  issue_key: mim-reconciliation-role-support-9b5c335508dd6a03
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Phosphomycin disodium salt'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-9b5c335508dd6a03
  evidence_ids:
  - ev-92bed7e5eb367047
  - ev-b764eb1575bd5f61
  - ev-7dd1245397d2c66d
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Phosphomycin_Disodium_Salt.yaml
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
    finding_id: f-2b3e6c85c9fd295a
actions:
- action_id: rec-action-2b3e6c85c9fd295a
  description: 'Reassess prediction-only role support: Phosphomycin disodium salt'
  finding_ids:
  - rec-f-2b3e6c85c9fd295a
  target_ids:
  - record-9b5c335508dd6a03
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Phosphomycin_Disodium_Salt.yaml
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
