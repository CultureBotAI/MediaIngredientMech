# Per-record structured review: Flavensomycin (data/ingredients/mapped/Flavensomycin.yaml)

- Review: 20261017T083000Z-flavensomycin
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Flavensomycin (data/ingredients/mapped/Flavensomycin.yaml, record-79137a63046012e5, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Flavensomycin.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Flavensomycin.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-79137a63046012e5 | data/ingredients/mapped/Flavensomycin.yaml | maintained | Flavensomycin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-79137a63046012e5 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-79137a63046012e5 | Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-79137a63046012e5 | Reconciled against predecessor batch review 20261011T024634Z-mim-reconcile-all-batch-06 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-79137a63046012e5.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-79137a63046012e5.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T16:44:04Z; reviewed SHA-256=a26badaf8b7012b2d2bb02895c1350dccd9b6b3eedd947f9bc2eb26a64d9f382; current SHA-256=a26badaf8b7012b2d2bb02895c1350dccd9b6b3eedd947f9bc2eb26a64d9f382; hash_changed=False. Reports=["reports/yaml_record_review/Flavensomycin.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The local placeholder identity and final SSSOM row pass, but SELECTIVE_AGENT is computational.

### Historical provisional-role concern

evidence: concern. Targets: record-79137a63046012e5.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-0cd13d5e29b5bfc7: Reassess prediction-only role support: Flavensomycin

major / open / confirmed; issue key: mim-reconciliation-role-support-79137a63046012e5.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-0cd13d5e29b5bfc7

Reassess prediction-only role support: Flavensomycin

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-1ea5ad991c91e351 | data/ingredients/mapped/Flavensomycin.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1009],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.compound:flavensomycin","line":1011,"mapping_status":"MAPPED","ontology_id":"kgmicrobe.compound:flavensomycin","preferred_term":"Flavensomycin"}],"identifier":"kgmicrobe.compound:flavensomycin","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"PLACEHOLDER","ontology_id":"kgmicrobe.compound:flavensomycin","ontology_label":"Flavensomycin","ontology_source":"kgmicrobe.compound"},"preferred_term":"Flavensomycin","sssom_rows":[{"data_row":1215,"object_id":"kgmicrobe.compound:flavensomycin","object_label":"Flavensomycin","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Flavensomycin","synonym_count":0} |
| ev-ccd12b5880d5c193 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1009] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-850013e3946b985e | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Flavensomycin; data-row positions=[1215] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1215,"object_id":"kgmicrobe.compound:flavensomycin","object_label":"Flavensomycin","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Flavensomycin","validation_method":"none&#124;UNKNOWN_TERM&#124;2026-07-07"}] |
| ev-b1314d27c9cc89cb | docs/data/mapped_ingredients.csv; CSV lines=[1011] | supports | Published identity and count rows inspected: [{"identifier":"kgmicrobe.compound:flavensomycin","line":1011,"mapping_quality":"PLACEHOLDER","mapping_status":"MAPPED","media_count":"0","ontology_id":"kgmicrobe.compound:flavensomycin","preferred_term":"Flavensomycin","total_occurrences":"0"}] |
| ev-b805a290b661ad07 | reports/yaml_record_review/Flavensomycin.md; &#96;data/ingredients/mapped/Flavensomycin.yaml&#96;:2; Verdict:4; Identity:11; Validation:25; Evidence:36; Completeness:57; Recommended Edits:64 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-30b6d33bd4ebf59b | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[620,1467] | context_only | [{"current_record_sha256":"a26badaf8b7012b2d2bb02895c1350dccd9b6b3eedd947f9bc2eb26a64d9f382","finding_id":"SEM:44a3f407cf648eff5c2b","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"a26badaf8b7012b2d2bb02895c1350dccd9b6b3eedd947f9bc2eb26a64d9f382","finding_id":"SEM:5d3f94edadfb0efe4cc7","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-a8bdf537d1e6ab14 | data/ingredients/mapped/Flavensomycin.yaml; physicochemical_roles[0] | supports | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1009],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.compound:flavensomycin","line":1011,"mapping_status":"MAPPED","ontology_id":"kgmicrobe.compound:flavensomycin","preferred_term":"Flavensomycin"}],"identifier":"kgmicrobe.compound:flavensomycin","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"PLACEHOLDER","ontology_id":"kgmicrobe.compound:flavensomycin","ontology_label":"Flavensomycin","ontology_source":"kgmicrobe.compound"},"preferred_term":"Flavensomycin","sssom_rows":[{"data_row":1215,"object_id":"kgmicrobe.compound:flavensomycin","object_label":"Flavensomycin","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Flavensomycin","synonym_count":0} |
| ev-6d6915057a39386d | reviews/structured/20261011T024634Z-mim-reconcile-all-batch-06/review.yaml; findings[finding_id=f-0cd13d5e29b5bfc7] | context_only | Predecessor structured review finding f-0cd13d5e29b5bfc7 in 20261011T024634Z-mim-reconcile-all-batch-06 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024634Z-mim-reconcile-all-batch-06.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-flavensomycin
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Flavensomycin (data/ingredients/mapped/Flavensomycin.yaml)'
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
summary: Per-record structured review for Flavensomycin (data/ingredients/mapped/Flavensomycin.yaml,
  record-79137a63046012e5, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Flavensomycin.yaml
    sha256: a26badaf8b7012b2d2bb02895c1350dccd9b6b3eedd947f9bc2eb26a64d9f382
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
  - path: reports/yaml_record_review/Flavensomycin.md
    sha256: 292e491f2174942f6d3b6a8e531439ee5615acce1df4e987ef1c2669c7091ad7
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-79137a63046012e5
  path: data/ingredients/mapped/Flavensomycin.yaml
  label: Flavensomycin
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Flavensomycin.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Flavensomycin.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Flavensomycin.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-79137a63046012e5
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-79137a63046012e5
  evidence_ids:
  - ev-1ea5ad991c91e351
  - ev-ccd12b5880d5c193
  - ev-850013e3946b985e
  - ev-b1314d27c9cc89cb
  - ev-a8bdf537d1e6ab14
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-79137a63046012e5
  evidence_ids:
  - ev-1ea5ad991c91e351
  - ev-30b6d33bd4ebf59b
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024634Z-mim-reconcile-all-batch-06
    and semantic review dispositions on HEAD.
  target_ids:
  - record-79137a63046012e5
  evidence_ids:
  - ev-b805a290b661ad07
  - ev-30b6d33bd4ebf59b
  - ev-6d6915057a39386d
evidence:
- evidence_id: ev-1ea5ad991c91e351
  kind: record_content
  reference: data/ingredients/mapped/Flavensomycin.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1009],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.compound:flavensomycin","line":1011,"mapping_status":"MAPPED","ontology_id":"kgmicrobe.compound:flavensomycin","preferred_term":"Flavensomycin"}],"identifier":"kgmicrobe.compound:flavensomycin","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"PLACEHOLDER","ontology_id":"kgmicrobe.compound:flavensomycin","ontology_label":"Flavensomycin","ontology_source":"kgmicrobe.compound"},"preferred_term":"Flavensomycin","sssom_rows":[{"data_row":1215,"object_id":"kgmicrobe.compound:flavensomycin","object_label":"Flavensomycin","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Flavensomycin","synonym_count":0}'
  snapshot_sha256: a26badaf8b7012b2d2bb02895c1350dccd9b6b3eedd947f9bc2eb26a64d9f382
- evidence_id: ev-ccd12b5880d5c193
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1009]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-850013e3946b985e
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Flavensomycin; data-row positions=[1215]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1215,"object_id":"kgmicrobe.compound:flavensomycin","object_label":"Flavensomycin","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Flavensomycin","validation_method":"none|UNKNOWN_TERM|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-b1314d27c9cc89cb
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1011]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"kgmicrobe.compound:flavensomycin","line":1011,"mapping_quality":"PLACEHOLDER","mapping_status":"MAPPED","media_count":"0","ontology_id":"kgmicrobe.compound:flavensomycin","preferred_term":"Flavensomycin","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-b805a290b661ad07
  kind: prior_review
  reference: reports/yaml_record_review/Flavensomycin.md
  locator: '`data/ingredients/mapped/Flavensomycin.yaml`:2; Verdict:4; Identity:11;
    Validation:25; Evidence:36; Completeness:57; Recommended Edits:64'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 292e491f2174942f6d3b6a8e531439ee5615acce1df4e987ef1c2669c7091ad7
  quote: "Recommended Edits:\n- Major: either replace `physicochemical_roles.SELECTIVE_AGENT`\
    \ in\n  `data/ingredients/mapped/Flavensomycin.yaml` with source-backed role evidence\n\
    \  or remove the role, sync `data/curated/mapped_ingredients.yaml`, and rerun\n\
    \  strict validation plus the final SSSOM invariant gates."
- evidence_id: ev-30b6d33bd4ebf59b
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[620,1467]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"a26badaf8b7012b2d2bb02895c1350dccd9b6b3eedd947f9bc2eb26a64d9f382","finding_id":"SEM:44a3f407cf648eff5c2b","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"a26badaf8b7012b2d2bb02895c1350dccd9b6b3eedd947f9bc2eb26a64d9f382","finding_id":"SEM:5d3f94edadfb0efe4cc7","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-a8bdf537d1e6ab14
  kind: record_content
  reference: data/ingredients/mapped/Flavensomycin.yaml
  locator: physicochemical_roles[0]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1009],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.compound:flavensomycin","line":1011,"mapping_status":"MAPPED","ontology_id":"kgmicrobe.compound:flavensomycin","preferred_term":"Flavensomycin"}],"identifier":"kgmicrobe.compound:flavensomycin","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"PLACEHOLDER","ontology_id":"kgmicrobe.compound:flavensomycin","ontology_label":"Flavensomycin","ontology_source":"kgmicrobe.compound"},"preferred_term":"Flavensomycin","sssom_rows":[{"data_row":1215,"object_id":"kgmicrobe.compound:flavensomycin","object_label":"Flavensomycin","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Flavensomycin","synonym_count":0}'
  snapshot_sha256: a26badaf8b7012b2d2bb02895c1350dccd9b6b3eedd947f9bc2eb26a64d9f382
- evidence_id: ev-6d6915057a39386d
  kind: prior_review
  reference: reviews/structured/20261011T024634Z-mim-reconcile-all-batch-06/review.yaml
  locator: findings[finding_id=f-0cd13d5e29b5bfc7]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-0cd13d5e29b5bfc7 in 20261011T024634Z-mim-reconcile-all-batch-06
  snapshot_sha256: 14c3200be95fdc87fca16bb71628432f3c9aaf8a65356ed494efc776ebe8aa11
assessments:
- assessment_id: a-9b6f0334b55e72fd
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-79137a63046012e5
  evidence_ids:
  - ev-1ea5ad991c91e351
  - ev-ccd12b5880d5c193
  - ev-850013e3946b985e
  - ev-b1314d27c9cc89cb
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-c9385df7ef772529
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-79137a63046012e5
  evidence_ids:
  - ev-b805a290b661ad07
  - ev-1ea5ad991c91e351
  - ev-30b6d33bd4ebf59b
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T16:44:04Z;
    reviewed SHA-256=a26badaf8b7012b2d2bb02895c1350dccd9b6b3eedd947f9bc2eb26a64d9f382;
    current SHA-256=a26badaf8b7012b2d2bb02895c1350dccd9b6b3eedd947f9bc2eb26a64d9f382;
    hash_changed=False. Reports=["reports/yaml_record_review/Flavensomycin.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The local placeholder
    identity and final SSSOM row pass, but SELECTIVE_AGENT is computational.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-b805a290b661ad07
    - ev-1ea5ad991c91e351
  - name: legacy-native-ids
    value: '["SEM:44a3f407cf648eff5c2b","SEM:5d3f94edadfb0efe4cc7"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-1ea5ad991c91e351
    - ev-b805a290b661ad07
    - ev-30b6d33bd4ebf59b
- assessment_id: a-a8bdf537d1e6ab14
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-79137a63046012e5
  evidence_ids:
  - ev-b805a290b661ad07
  - ev-a8bdf537d1e6ab14
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-b805a290b661ad07
    - ev-a8bdf537d1e6ab14
findings:
- finding_id: rec-f-0cd13d5e29b5bfc7
  issue_key: mim-reconciliation-role-support-79137a63046012e5
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Flavensomycin'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-79137a63046012e5
  evidence_ids:
  - ev-b805a290b661ad07
  - ev-a8bdf537d1e6ab14
  - ev-6d6915057a39386d
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Flavensomycin.yaml
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
    review_id: 20261011T024634Z-mim-reconcile-all-batch-06
    finding_id: f-0cd13d5e29b5bfc7
actions:
- action_id: rec-action-0cd13d5e29b5bfc7
  description: 'Reassess prediction-only role support: Flavensomycin'
  finding_ids:
  - rec-f-0cd13d5e29b5bfc7
  target_ids:
  - record-79137a63046012e5
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Flavensomycin.yaml
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
