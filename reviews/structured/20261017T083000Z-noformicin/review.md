# Per-record structured review: Noformicin (data/ingredients/mapped/Noformicin.yaml)

- Review: 20261017T083000Z-noformicin
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Noformicin (data/ingredients/mapped/Noformicin.yaml, record-d9c7fb255e88ecf5, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Noformicin.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Noformicin.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-d9c7fb255e88ecf5 | data/ingredients/mapped/Noformicin.yaml | maintained | Noformicin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-d9c7fb255e88ecf5 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-d9c7fb255e88ecf5 | Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-d9c7fb255e88ecf5 | Reconciled against predecessor batch review 20261011T024637Z-mim-reconcile-all-batch-09 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-d9c7fb255e88ecf5.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-d9c7fb255e88ecf5.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T07:04:54Z; reviewed SHA-256=18da53cc55fbe2d673f46c8fe45f530df5236bafb828f276a099a4de5f7c0f5a; current SHA-256=18da53cc55fbe2d673f46c8fe45f530df5236bafb828f276a099a4de5f7c0f5a; hash_changed=False. Reports=["reports/yaml_record_review/Noformicin.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact mesh:C005642 noformicin identity passes, but SELECTIVE_AGENT is only provisional.

### Historical provisional-role concern

evidence: concern. Targets: record-d9c7fb255e88ecf5.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-fecdee37ea2da28d: Reassess prediction-only role support: Noformicin

major / open / confirmed; issue key: mim-reconciliation-role-support-d9c7fb255e88ecf5.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-fecdee37ea2da28d

Reassess prediction-only role support: Noformicin

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-07ff1455db9ec883 | data/ingredients/mapped/Noformicin.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1576],"raw_equal":true},"docs_rows":[{"identifier":"mesh:C005642","line":1578,"mapping_status":"MAPPED","ontology_id":"mesh:C005642","preferred_term":"Noformicin"}],"identifier":"mesh:C005642","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"mesh:C005642","ontology_label":"noformicin","ontology_source":"MESH"},"preferred_term":"Noformicin","sssom_rows":[{"data_row":2112,"object_id":"mesh:C005642","object_label":"noformicin","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Noformicin","synonym_count":0} |
| ev-5e5a40908a9f916c | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1576] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-e72e1cb8331c8cb3 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Noformicin; data-row positions=[2112] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":2112,"object_id":"mesh:C005642","object_label":"noformicin","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Noformicin","validation_method":"none&#124;UNKNOWN_TERM&#124;2026-07-07"}] |
| ev-acd69e15680c7442 | docs/data/mapped_ingredients.csv; CSV lines=[1578] | supports | Published identity and count rows inspected: [{"identifier":"mesh:C005642","line":1578,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"mesh:C005642","preferred_term":"Noformicin","total_occurrences":"0"}] |
| ev-5acadddb85a22240 | reports/yaml_record_review/Noformicin.md; &#96;data/ingredients/mapped/Noformicin.yaml&#96;:2; Verdict:4; Identity:10; Validation:19; Evidence:25; Completeness:40; Recommended Edits:47 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-912dafc26e2185b9 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1071,1768] | context_only | [{"current_record_sha256":"18da53cc55fbe2d673f46c8fe45f530df5236bafb828f276a099a4de5f7c0f5a","finding_id":"SEM:7e71e001421a6eb45838","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"18da53cc55fbe2d673f46c8fe45f530df5236bafb828f276a099a4de5f7c0f5a","finding_id":"SEM:ca5794b70729f32b53fa","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-2d7489c5e7237a9f | data/ingredients/mapped/Noformicin.yaml; physicochemical_roles[0] | supports | Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION: [{"field":"physicochemical_roles[0]","role":{"confidence":0.8,"evidence":[{"curator_note":"Provisional role from a curated name-pattern rule; review recommended.","reference_text":"Inferred from curated media-role name pattern","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"SELECTIVE_AGENT"}}] |
| ev-53d32bc0414a2c6b | reviews/structured/20261011T024637Z-mim-reconcile-all-batch-09/review.yaml; findings[finding_id=f-fecdee37ea2da28d] | context_only | Predecessor structured review finding f-fecdee37ea2da28d in 20261011T024637Z-mim-reconcile-all-batch-09 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024637Z-mim-reconcile-all-batch-09.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-noformicin
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Noformicin (data/ingredients/mapped/Noformicin.yaml)'
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
summary: Per-record structured review for Noformicin (data/ingredients/mapped/Noformicin.yaml,
  record-d9c7fb255e88ecf5, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Noformicin.yaml
    sha256: 18da53cc55fbe2d673f46c8fe45f530df5236bafb828f276a099a4de5f7c0f5a
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
  - path: reports/yaml_record_review/Noformicin.md
    sha256: e4013e3c12620dce947cba9df604d69c8442545f61581dc2928dbdea6b617f0e
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-d9c7fb255e88ecf5
  path: data/ingredients/mapped/Noformicin.yaml
  label: Noformicin
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Noformicin.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Noformicin.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Noformicin.yaml selected from full-corpus
    review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-d9c7fb255e88ecf5
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-d9c7fb255e88ecf5
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-d9c7fb255e88ecf5
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024637Z-mim-reconcile-all-batch-09
    and semantic review dispositions on HEAD.
  target_ids:
  - record-d9c7fb255e88ecf5
evidence:
- evidence_id: ev-07ff1455db9ec883
  kind: record_content
  reference: data/ingredients/mapped/Noformicin.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1576],"raw_equal":true},"docs_rows":[{"identifier":"mesh:C005642","line":1578,"mapping_status":"MAPPED","ontology_id":"mesh:C005642","preferred_term":"Noformicin"}],"identifier":"mesh:C005642","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"mesh:C005642","ontology_label":"noformicin","ontology_source":"MESH"},"preferred_term":"Noformicin","sssom_rows":[{"data_row":2112,"object_id":"mesh:C005642","object_label":"noformicin","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Noformicin","synonym_count":0}'
  snapshot_sha256: 18da53cc55fbe2d673f46c8fe45f530df5236bafb828f276a099a4de5f7c0f5a
- evidence_id: ev-5e5a40908a9f916c
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1576]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-e72e1cb8331c8cb3
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Noformicin; data-row positions=[2112]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":2112,"object_id":"mesh:C005642","object_label":"noformicin","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Noformicin","validation_method":"none|UNKNOWN_TERM|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-acd69e15680c7442
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1578]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"mesh:C005642","line":1578,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"mesh:C005642","preferred_term":"Noformicin","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-5acadddb85a22240
  kind: prior_review
  reference: reports/yaml_record_review/Noformicin.md
  locator: '`data/ingredients/mapped/Noformicin.yaml`:2; Verdict:4; Identity:10; Validation:19;
    Evidence:25; Completeness:40; Recommended Edits:47'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: e4013e3c12620dce947cba9df604d69c8442545f61581dc2928dbdea6b617f0e
  quote: "Recommended Edits:\n- Major: in `data/ingredients/mapped/Noformicin.yaml`,\
    \ replace the\n  `SELECTIVE_AGENT` role evidence with inspected source-backed\
    \ evidence, or\n  remove the role until that evidence exists."
- evidence_id: ev-912dafc26e2185b9
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1071,1768]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"18da53cc55fbe2d673f46c8fe45f530df5236bafb828f276a099a4de5f7c0f5a","finding_id":"SEM:7e71e001421a6eb45838","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"18da53cc55fbe2d673f46c8fe45f530df5236bafb828f276a099a4de5f7c0f5a","finding_id":"SEM:ca5794b70729f32b53fa","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-2d7489c5e7237a9f
  kind: record_content
  reference: data/ingredients/mapped/Noformicin.yaml
  locator: physicochemical_roles[0]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION:
    [{"field":"physicochemical_roles[0]","role":{"confidence":0.8,"evidence":[{"curator_note":"Provisional
    role from a curated name-pattern rule; review recommended.","reference_text":"Inferred
    from curated media-role name pattern","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"SELECTIVE_AGENT"}}]'
  snapshot_sha256: 18da53cc55fbe2d673f46c8fe45f530df5236bafb828f276a099a4de5f7c0f5a
- evidence_id: ev-53d32bc0414a2c6b
  kind: prior_review
  reference: reviews/structured/20261011T024637Z-mim-reconcile-all-batch-09/review.yaml
  locator: findings[finding_id=f-fecdee37ea2da28d]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-fecdee37ea2da28d in 20261011T024637Z-mim-reconcile-all-batch-09
  snapshot_sha256: cf46750874f1303863883723934bbe8b09ece8d62b1785ceab64bb0342a3cf11
assessments:
- assessment_id: a-03c4c00b9421c862
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-d9c7fb255e88ecf5
  evidence_ids:
  - ev-07ff1455db9ec883
  - ev-5e5a40908a9f916c
  - ev-e72e1cb8331c8cb3
  - ev-acd69e15680c7442
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-e41476c4445e6437
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-d9c7fb255e88ecf5
  evidence_ids:
  - ev-5acadddb85a22240
  - ev-07ff1455db9ec883
  - ev-912dafc26e2185b9
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T07:04:54Z;
    reviewed SHA-256=18da53cc55fbe2d673f46c8fe45f530df5236bafb828f276a099a4de5f7c0f5a;
    current SHA-256=18da53cc55fbe2d673f46c8fe45f530df5236bafb828f276a099a4de5f7c0f5a;
    hash_changed=False. Reports=["reports/yaml_record_review/Noformicin.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The exact mesh:C005642
    noformicin identity passes, but SELECTIVE_AGENT is only provisional.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-5acadddb85a22240
    - ev-07ff1455db9ec883
  - name: legacy-native-ids
    value: '["SEM:7e71e001421a6eb45838","SEM:ca5794b70729f32b53fa"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-07ff1455db9ec883
    - ev-5acadddb85a22240
    - ev-912dafc26e2185b9
- assessment_id: a-2d7489c5e7237a9f
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-d9c7fb255e88ecf5
  evidence_ids:
  - ev-5acadddb85a22240
  - ev-2d7489c5e7237a9f
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-5acadddb85a22240
    - ev-2d7489c5e7237a9f
findings:
- finding_id: rec-f-fecdee37ea2da28d
  issue_key: mim-reconciliation-role-support-d9c7fb255e88ecf5
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Noformicin'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-d9c7fb255e88ecf5
  evidence_ids:
  - ev-5acadddb85a22240
  - ev-2d7489c5e7237a9f
  - ev-53d32bc0414a2c6b
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Noformicin.yaml
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
    review_id: 20261011T024637Z-mim-reconcile-all-batch-09
    finding_id: f-fecdee37ea2da28d
actions:
- action_id: rec-action-fecdee37ea2da28d
  description: 'Reassess prediction-only role support: Noformicin'
  finding_ids:
  - rec-f-fecdee37ea2da28d
  target_ids:
  - record-d9c7fb255e88ecf5
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Noformicin.yaml
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
