# Per-record structured review: D-Leucrose (data/ingredients/mapped/D-Leucrose.yaml)

- Review: 20261017T083000Z-d-leucrose
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for D-Leucrose (data/ingredients/mapped/D-Leucrose.yaml, record-c71e87911f55c0ba, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/D-Leucrose.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/D-Leucrose.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-c71e87911f55c0ba | data/ingredients/mapped/D-Leucrose.yaml | maintained | D-Leucrose |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-c71e87911f55c0ba | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-c71e87911f55c0ba | Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-c71e87911f55c0ba | Reconciled against predecessor batch review 20261011T024633Z-mim-reconcile-all-batch-05 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-c71e87911f55c0ba.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-c71e87911f55c0ba.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T13:16:11Z; reviewed SHA-256=4afb61c4b4524c13a6b58fabcad62553162dccf1a3a4032e09ded3602cfc7083; current SHA-256=4afb61c4b4524c13a6b58fabcad62553162dccf1a3a4032e09ded3602cfc7083; hash_changed=False. Reports=["reports/yaml_record_review/D-Leucrose.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The CAS fallback identity, PubChem chemistry, 0/0 count, and final SSSOM row pass, but the carbon role is only computationally supported.

### Historical provisional-role concern

evidence: concern. Targets: record-c71e87911f55c0ba.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-970dc93d7fdb960b: Reassess prediction-only role support: D-Leucrose

major / open / confirmed; issue key: mim-reconciliation-role-support-c71e87911f55c0ba.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-970dc93d7fdb960b

Reassess prediction-only role support: D-Leucrose

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-c00217ce6aca093d | data/ingredients/mapped/D-Leucrose.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[818],"raw_equal":true},"docs_rows":[{"identifier":"cas:7158-70-5","line":820,"mapping_status":"MAPPED","ontology_id":"cas:7158-70-5","preferred_term":"D-Leucrose"}],"identifier":"cas:7158-70-5","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"FALLBACK_REGISTRY","ontology_id":"cas:7158-70-5","ontology_label":"D-Leucrose","ontology_source":"CAS"},"preferred_term":"D-Leucrose","sssom_rows":[{"data_row":897,"object_id":"cas:7158-70-5","object_label":"D-Leucrose","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:D-Leucrose","synonym_count":0} |
| ev-6c1c7262822122aa | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [818] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-bf64e9a8b57d38f8 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:D-Leucrose; data-row positions=[897] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":897,"object_id":"cas:7158-70-5","object_label":"D-Leucrose","other":"CAS:7158-70-5","predicate_id":"skos:exactMatch","subject_id":"MIM:D-Leucrose","validation_method":"none&#124;UNKNOWN_TERM&#124;2026-07-07"}] |
| ev-8d069f8fdfa5e437 | docs/data/mapped_ingredients.csv; CSV lines=[820] | supports | Published identity and count rows inspected: [{"identifier":"cas:7158-70-5","line":820,"mapping_quality":"FALLBACK_REGISTRY","mapping_status":"MAPPED","media_count":"0","ontology_id":"cas:7158-70-5","preferred_term":"D-Leucrose","total_occurrences":"0"}] |
| ev-f04b0fc9be2f815e | reports/yaml_record_review/D-Leucrose.md; &#96;data/ingredients/mapped/D-Leucrose.yaml&#96;:2; Verdict:4; Identity:11; Validation:24; Evidence:44; Completeness:59; Recommended Edits:70 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-0f275503529c15dc | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[470,1995] | context_only | [{"current_record_sha256":"4afb61c4b4524c13a6b58fabcad62553162dccf1a3a4032e09ded3602cfc7083","finding_id":"SEM:0757583f7095ff196408","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"4afb61c4b4524c13a6b58fabcad62553162dccf1a3a4032e09ded3602cfc7083","finding_id":"SEM:3de20dd2aa39479d38e3","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-2e8be252d8f3b6b8 | data/ingredients/mapped/D-Leucrose.yaml; nutritional_roles[0] | supports | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[818],"raw_equal":true},"docs_rows":[{"identifier":"cas:7158-70-5","line":820,"mapping_status":"MAPPED","ontology_id":"cas:7158-70-5","preferred_term":"D-Leucrose"}],"identifier":"cas:7158-70-5","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"FALLBACK_REGISTRY","ontology_id":"cas:7158-70-5","ontology_label":"D-Leucrose","ontology_source":"CAS"},"preferred_term":"D-Leucrose","sssom_rows":[{"data_row":897,"object_id":"cas:7158-70-5","object_label":"D-Leucrose","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:D-Leucrose","synonym_count":0} |
| ev-3c736ca3b63c880c | reviews/structured/20261011T024633Z-mim-reconcile-all-batch-05/review.yaml; findings[finding_id=f-970dc93d7fdb960b] | context_only | Predecessor structured review finding f-970dc93d7fdb960b in 20261011T024633Z-mim-reconcile-all-batch-05 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024633Z-mim-reconcile-all-batch-05.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-d-leucrose
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: D-Leucrose (data/ingredients/mapped/D-Leucrose.yaml)'
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
summary: Per-record structured review for D-Leucrose (data/ingredients/mapped/D-Leucrose.yaml,
  record-c71e87911f55c0ba, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/D-Leucrose.yaml
    sha256: 4afb61c4b4524c13a6b58fabcad62553162dccf1a3a4032e09ded3602cfc7083
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
  - path: reports/yaml_record_review/D-Leucrose.md
    sha256: 6cb41522162eafc06d496f56566a7bb6587e994c4bb864d48bc5e50641e6c5c9
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-c71e87911f55c0ba
  path: data/ingredients/mapped/D-Leucrose.yaml
  label: D-Leucrose
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/D-Leucrose.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/D-Leucrose.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/D-Leucrose.yaml selected from full-corpus
    review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-c71e87911f55c0ba
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-c71e87911f55c0ba
  evidence_ids:
  - ev-c00217ce6aca093d
  - ev-6c1c7262822122aa
  - ev-bf64e9a8b57d38f8
  - ev-8d069f8fdfa5e437
  - ev-2e8be252d8f3b6b8
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-c71e87911f55c0ba
  evidence_ids:
  - ev-c00217ce6aca093d
  - ev-0f275503529c15dc
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024633Z-mim-reconcile-all-batch-05
    and semantic review dispositions on HEAD.
  target_ids:
  - record-c71e87911f55c0ba
  evidence_ids:
  - ev-f04b0fc9be2f815e
  - ev-0f275503529c15dc
  - ev-3c736ca3b63c880c
evidence:
- evidence_id: ev-c00217ce6aca093d
  kind: record_content
  reference: data/ingredients/mapped/D-Leucrose.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[818],"raw_equal":true},"docs_rows":[{"identifier":"cas:7158-70-5","line":820,"mapping_status":"MAPPED","ontology_id":"cas:7158-70-5","preferred_term":"D-Leucrose"}],"identifier":"cas:7158-70-5","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"FALLBACK_REGISTRY","ontology_id":"cas:7158-70-5","ontology_label":"D-Leucrose","ontology_source":"CAS"},"preferred_term":"D-Leucrose","sssom_rows":[{"data_row":897,"object_id":"cas:7158-70-5","object_label":"D-Leucrose","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:D-Leucrose","synonym_count":0}'
  snapshot_sha256: 4afb61c4b4524c13a6b58fabcad62553162dccf1a3a4032e09ded3602cfc7083
- evidence_id: ev-6c1c7262822122aa
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [818]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-bf64e9a8b57d38f8
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:D-Leucrose; data-row positions=[897]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":897,"object_id":"cas:7158-70-5","object_label":"D-Leucrose","other":"CAS:7158-70-5","predicate_id":"skos:exactMatch","subject_id":"MIM:D-Leucrose","validation_method":"none|UNKNOWN_TERM|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-8d069f8fdfa5e437
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[820]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"cas:7158-70-5","line":820,"mapping_quality":"FALLBACK_REGISTRY","mapping_status":"MAPPED","media_count":"0","ontology_id":"cas:7158-70-5","preferred_term":"D-Leucrose","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-f04b0fc9be2f815e
  kind: prior_review
  reference: reports/yaml_record_review/D-Leucrose.md
  locator: '`data/ingredients/mapped/D-Leucrose.yaml`:2; Verdict:4; Identity:11; Validation:24;
    Evidence:44; Completeness:59; Recommended Edits:70'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 6cb41522162eafc06d496f56566a7bb6587e994c4bb864d48bc5e50641e6c5c9
  quote: "Recommended Edits:\n- In `data/ingredients/mapped/D-Leucrose.yaml`, either\
    \ replace the\n  computational `CARBON_SOURCE` evidence with direct CultureBotHT\
    \ or\n  source-backed media-role evidence for this ingredient, or remove the role\n\
    \  facet; then rerun strict validation and the final SSSOM build."
- evidence_id: ev-0f275503529c15dc
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[470,1995]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"4afb61c4b4524c13a6b58fabcad62553162dccf1a3a4032e09ded3602cfc7083","finding_id":"SEM:0757583f7095ff196408","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"4afb61c4b4524c13a6b58fabcad62553162dccf1a3a4032e09ded3602cfc7083","finding_id":"SEM:3de20dd2aa39479d38e3","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-2e8be252d8f3b6b8
  kind: record_content
  reference: data/ingredients/mapped/D-Leucrose.yaml
  locator: nutritional_roles[0]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[818],"raw_equal":true},"docs_rows":[{"identifier":"cas:7158-70-5","line":820,"mapping_status":"MAPPED","ontology_id":"cas:7158-70-5","preferred_term":"D-Leucrose"}],"identifier":"cas:7158-70-5","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"FALLBACK_REGISTRY","ontology_id":"cas:7158-70-5","ontology_label":"D-Leucrose","ontology_source":"CAS"},"preferred_term":"D-Leucrose","sssom_rows":[{"data_row":897,"object_id":"cas:7158-70-5","object_label":"D-Leucrose","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:D-Leucrose","synonym_count":0}'
  snapshot_sha256: 4afb61c4b4524c13a6b58fabcad62553162dccf1a3a4032e09ded3602cfc7083
- evidence_id: ev-3c736ca3b63c880c
  kind: prior_review
  reference: reviews/structured/20261011T024633Z-mim-reconcile-all-batch-05/review.yaml
  locator: findings[finding_id=f-970dc93d7fdb960b]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-970dc93d7fdb960b in 20261011T024633Z-mim-reconcile-all-batch-05
  snapshot_sha256: 7549030a5b50ed98868ff3497507fdfbfecd07cd858c76738f734521fa9d3603
assessments:
- assessment_id: a-228226d0401771a1
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-c71e87911f55c0ba
  evidence_ids:
  - ev-c00217ce6aca093d
  - ev-6c1c7262822122aa
  - ev-bf64e9a8b57d38f8
  - ev-8d069f8fdfa5e437
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-d16f529787c09dbb
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-c71e87911f55c0ba
  evidence_ids:
  - ev-f04b0fc9be2f815e
  - ev-c00217ce6aca093d
  - ev-0f275503529c15dc
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T13:16:11Z;
    reviewed SHA-256=4afb61c4b4524c13a6b58fabcad62553162dccf1a3a4032e09ded3602cfc7083;
    current SHA-256=4afb61c4b4524c13a6b58fabcad62553162dccf1a3a4032e09ded3602cfc7083;
    hash_changed=False. Reports=["reports/yaml_record_review/D-Leucrose.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The CAS fallback
    identity, PubChem chemistry, 0/0 count, and final SSSOM row pass, but the carbon
    role is only computationally supported.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-f04b0fc9be2f815e
    - ev-c00217ce6aca093d
  - name: legacy-native-ids
    value: '["SEM:0757583f7095ff196408","SEM:3de20dd2aa39479d38e3"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-c00217ce6aca093d
    - ev-f04b0fc9be2f815e
    - ev-0f275503529c15dc
- assessment_id: a-2e8be252d8f3b6b8
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-c71e87911f55c0ba
  evidence_ids:
  - ev-f04b0fc9be2f815e
  - ev-2e8be252d8f3b6b8
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-f04b0fc9be2f815e
    - ev-2e8be252d8f3b6b8
findings:
- finding_id: rec-f-970dc93d7fdb960b
  issue_key: mim-reconciliation-role-support-c71e87911f55c0ba
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: D-Leucrose'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-c71e87911f55c0ba
  evidence_ids:
  - ev-f04b0fc9be2f815e
  - ev-2e8be252d8f3b6b8
  - ev-3c736ca3b63c880c
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/D-Leucrose.yaml
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
    finding_id: f-970dc93d7fdb960b
actions:
- action_id: rec-action-970dc93d7fdb960b
  description: 'Reassess prediction-only role support: D-Leucrose'
  finding_ids:
  - rec-f-970dc93d7fdb960b
  target_ids:
  - record-c71e87911f55c0ba
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/D-Leucrose.yaml
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
