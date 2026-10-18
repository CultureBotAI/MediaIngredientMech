# Per-record structured review: Setamycin (data/ingredients/mapped/Setamycin.yaml)

- Review: 20261017T083000Z-setamycin
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Setamycin (data/ingredients/mapped/Setamycin.yaml, record-417fc0dd3984cd3a, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Setamycin.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Setamycin.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-417fc0dd3984cd3a | data/ingredients/mapped/Setamycin.yaml | maintained | Setamycin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-417fc0dd3984cd3a | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-417fc0dd3984cd3a | Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-417fc0dd3984cd3a | Reconciled against predecessor batch review 20261011T024638Z-mim-reconcile-all-batch-10 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-417fc0dd3984cd3a.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-417fc0dd3984cd3a.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T13:40:35Z; reviewed SHA-256=242e8b33ab85ae73a82ed81fd58e039c1608dd07915f04eaf593f225a2531176; current SHA-256=242e8b33ab85ae73a82ed81fd58e039c1608dd07915f04eaf593f225a2531176; hash_changed=False. Reports=["reports/yaml_record_review/Setamycin.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact MeSH setamycin identity passes, but SELECTIVE_AGENT is only provisional name-pattern inference.

### Historical provisional-role concern

evidence: concern. Targets: record-417fc0dd3984cd3a.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-84ff7e58dcb7aa9c: Reassess prediction-only role support: Setamycin

major / open / confirmed; issue key: mim-reconciliation-role-support-417fc0dd3984cd3a.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-84ff7e58dcb7aa9c

Reassess prediction-only role support: Setamycin

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-73051ffc94239db2 | data/ingredients/mapped/Setamycin.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1790],"raw_equal":true},"docs_rows":[{"identifier":"mesh:C032953","line":1792,"mapping_status":"MAPPED","ontology_id":"mesh:C032953","preferred_term":"Setamycin"}],"identifier":"mesh:C032953","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"mesh:C032953","ontology_label":"setamycin","ontology_source":"MESH"},"preferred_term":"Setamycin","sssom_rows":[{"data_row":2495,"object_id":"mesh:C032953","object_label":"setamycin","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Setamycin","synonym_count":0} |
| ev-a288b196aed5cc2e | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1790] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-2f541e1f87ed0f61 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Setamycin; data-row positions=[2495] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":2495,"object_id":"mesh:C032953","object_label":"setamycin","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Setamycin","validation_method":"none&#124;UNKNOWN_TERM&#124;2026-07-07"}] |
| ev-378971414cc11a66 | docs/data/mapped_ingredients.csv; CSV lines=[1792] | supports | Published identity and count rows inspected: [{"identifier":"mesh:C032953","line":1792,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"mesh:C032953","preferred_term":"Setamycin","total_occurrences":"0"}] |
| ev-a9e9967cbf8d398e | reports/yaml_record_review/Setamycin.md; &#96;data/ingredients/mapped/Setamycin.yaml&#96;:2 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-fb3d3b3a132de9dd | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1189,1488] | context_only | [{"current_record_sha256":"242e8b33ab85ae73a82ed81fd58e039c1608dd07915f04eaf593f225a2531176","finding_id":"SEM:1993845b52e8b136d52e","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"242e8b33ab85ae73a82ed81fd58e039c1608dd07915f04eaf593f225a2531176","finding_id":"SEM:ccf046272ddd7536bfc5","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-9f2cb14af2cc4474 | data/ingredients/mapped/Setamycin.yaml; physicochemical_roles[0] | supports | Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION: [{"field":"physicochemical_roles[0]","role":{"confidence":0.8,"evidence":[{"curator_note":"Provisional role from a curated name-pattern rule; review recommended.","reference_text":"Inferred from curated media-role name pattern","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"SELECTIVE_AGENT"}}] |
| ev-cea5412b94c234cf | reviews/structured/20261011T024638Z-mim-reconcile-all-batch-10/review.yaml; findings[finding_id=f-84ff7e58dcb7aa9c] | context_only | Predecessor structured review finding f-84ff7e58dcb7aa9c in 20261011T024638Z-mim-reconcile-all-batch-10 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024638Z-mim-reconcile-all-batch-10.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-setamycin
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Setamycin (data/ingredients/mapped/Setamycin.yaml)'
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
summary: Per-record structured review for Setamycin (data/ingredients/mapped/Setamycin.yaml,
  record-417fc0dd3984cd3a, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Setamycin.yaml
    sha256: 242e8b33ab85ae73a82ed81fd58e039c1608dd07915f04eaf593f225a2531176
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
  - path: reports/yaml_record_review/Setamycin.md
    sha256: c3aa805db2a72d3aec44339bd7e02de4f5d8ff43a4cf13fb73eadbbdd6f2b2b6
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-417fc0dd3984cd3a
  path: data/ingredients/mapped/Setamycin.yaml
  label: Setamycin
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Setamycin.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Setamycin.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Setamycin.yaml selected from full-corpus
    review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-417fc0dd3984cd3a
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-417fc0dd3984cd3a
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-417fc0dd3984cd3a
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024638Z-mim-reconcile-all-batch-10
    and semantic review dispositions on HEAD.
  target_ids:
  - record-417fc0dd3984cd3a
evidence:
- evidence_id: ev-73051ffc94239db2
  kind: record_content
  reference: data/ingredients/mapped/Setamycin.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1790],"raw_equal":true},"docs_rows":[{"identifier":"mesh:C032953","line":1792,"mapping_status":"MAPPED","ontology_id":"mesh:C032953","preferred_term":"Setamycin"}],"identifier":"mesh:C032953","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"mesh:C032953","ontology_label":"setamycin","ontology_source":"MESH"},"preferred_term":"Setamycin","sssom_rows":[{"data_row":2495,"object_id":"mesh:C032953","object_label":"setamycin","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Setamycin","synonym_count":0}'
  snapshot_sha256: 242e8b33ab85ae73a82ed81fd58e039c1608dd07915f04eaf593f225a2531176
- evidence_id: ev-a288b196aed5cc2e
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1790]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-2f541e1f87ed0f61
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Setamycin; data-row positions=[2495]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":2495,"object_id":"mesh:C032953","object_label":"setamycin","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Setamycin","validation_method":"none|UNKNOWN_TERM|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-378971414cc11a66
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1792]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"mesh:C032953","line":1792,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"mesh:C032953","preferred_term":"Setamycin","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-a9e9967cbf8d398e
  kind: prior_review
  reference: reports/yaml_record_review/Setamycin.md
  locator: '`data/ingredients/mapped/Setamycin.yaml`:2'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: c3aa805db2a72d3aec44339bd7e02de4f5d8ff43a4cf13fb73eadbbdd6f2b2b6
- evidence_id: ev-fb3d3b3a132de9dd
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1189,1488]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"242e8b33ab85ae73a82ed81fd58e039c1608dd07915f04eaf593f225a2531176","finding_id":"SEM:1993845b52e8b136d52e","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"242e8b33ab85ae73a82ed81fd58e039c1608dd07915f04eaf593f225a2531176","finding_id":"SEM:ccf046272ddd7536bfc5","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-9f2cb14af2cc4474
  kind: record_content
  reference: data/ingredients/mapped/Setamycin.yaml
  locator: physicochemical_roles[0]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION:
    [{"field":"physicochemical_roles[0]","role":{"confidence":0.8,"evidence":[{"curator_note":"Provisional
    role from a curated name-pattern rule; review recommended.","reference_text":"Inferred
    from curated media-role name pattern","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"SELECTIVE_AGENT"}}]'
  snapshot_sha256: 242e8b33ab85ae73a82ed81fd58e039c1608dd07915f04eaf593f225a2531176
- evidence_id: ev-cea5412b94c234cf
  kind: prior_review
  reference: reviews/structured/20261011T024638Z-mim-reconcile-all-batch-10/review.yaml
  locator: findings[finding_id=f-84ff7e58dcb7aa9c]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-84ff7e58dcb7aa9c in 20261011T024638Z-mim-reconcile-all-batch-10
  snapshot_sha256: 8c3aa2fca1269d1dbbf6117e85dea5b0de5047a8505841641245bd7ee99b936d
assessments:
- assessment_id: a-45991daf3397002a
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-417fc0dd3984cd3a
  evidence_ids:
  - ev-73051ffc94239db2
  - ev-a288b196aed5cc2e
  - ev-2f541e1f87ed0f61
  - ev-378971414cc11a66
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-7bd82658f615cb20
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-417fc0dd3984cd3a
  evidence_ids:
  - ev-a9e9967cbf8d398e
  - ev-73051ffc94239db2
  - ev-fb3d3b3a132de9dd
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T13:40:35Z;
    reviewed SHA-256=242e8b33ab85ae73a82ed81fd58e039c1608dd07915f04eaf593f225a2531176;
    current SHA-256=242e8b33ab85ae73a82ed81fd58e039c1608dd07915f04eaf593f225a2531176;
    hash_changed=False. Reports=["reports/yaml_record_review/Setamycin.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The exact MeSH
    setamycin identity passes, but SELECTIVE_AGENT is only provisional name-pattern
    inference.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-a9e9967cbf8d398e
    - ev-73051ffc94239db2
  - name: legacy-native-ids
    value: '["SEM:1993845b52e8b136d52e","SEM:ccf046272ddd7536bfc5"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-73051ffc94239db2
    - ev-a9e9967cbf8d398e
    - ev-fb3d3b3a132de9dd
- assessment_id: a-9f2cb14af2cc4474
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-417fc0dd3984cd3a
  evidence_ids:
  - ev-a9e9967cbf8d398e
  - ev-9f2cb14af2cc4474
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-a9e9967cbf8d398e
    - ev-9f2cb14af2cc4474
findings:
- finding_id: rec-f-84ff7e58dcb7aa9c
  issue_key: mim-reconciliation-role-support-417fc0dd3984cd3a
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Setamycin'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-417fc0dd3984cd3a
  evidence_ids:
  - ev-a9e9967cbf8d398e
  - ev-9f2cb14af2cc4474
  - ev-cea5412b94c234cf
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Setamycin.yaml
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
    finding_id: f-84ff7e58dcb7aa9c
actions:
- action_id: rec-action-84ff7e58dcb7aa9c
  description: 'Reassess prediction-only role support: Setamycin'
  finding_ids:
  - rec-f-84ff7e58dcb7aa9c
  target_ids:
  - record-417fc0dd3984cd3a
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Setamycin.yaml
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
