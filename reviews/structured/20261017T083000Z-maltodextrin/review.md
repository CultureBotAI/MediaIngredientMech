# Per-record structured review: Maltodextrin (data/ingredients/mapped/Maltodextrin.yaml)

- Review: 20261017T083000Z-maltodextrin
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Maltodextrin (data/ingredients/mapped/Maltodextrin.yaml, record-521c77db3812fd7a, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Maltodextrin.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Maltodextrin.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-521c77db3812fd7a | data/ingredients/mapped/Maltodextrin.yaml | maintained | Maltodextrin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-521c77db3812fd7a | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-521c77db3812fd7a | Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-521c77db3812fd7a | Reconciled against predecessor batch review 20261011T024636Z-mim-reconcile-all-batch-08 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-521c77db3812fd7a.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-521c77db3812fd7a.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T01:27:59Z; reviewed SHA-256=0dd1be3b08fab491189a693781600195c8854e04b8b090eed69df17072c0ab5f; current SHA-256=0dd1be3b08fab491189a693781600195c8854e04b8b090eed69df17072c0ab5f; hash_changed=False. Reports=["reports/yaml_record_review/Maltodextrin.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI:25140 identity, occurrence count, empty other field, and final SSSOM row pass, but CARBON_SOURCE is provisional.

### Historical provisional-role concern

evidence: concern. Targets: record-521c77db3812fd7a.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-9303a408608808ba: Reassess prediction-only role support: Maltodextrin

major / open / confirmed; issue key: mim-reconciliation-role-support-521c77db3812fd7a.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-9303a408608808ba

Reassess prediction-only role support: Maltodextrin

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-50fb2ac30bdde1a0 | data/ingredients/mapped/Maltodextrin.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1339],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:25140","line":1341,"mapping_status":"MAPPED","ontology_id":"CHEBI:25140","preferred_term":"Maltodextrin"}],"identifier":"CHEBI:25140","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":1,"edge_count":1,"occurrences":1},"occurrence_statistics":{"media_count":1,"total_occurrences":1},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:25140","ontology_label":"maltodextrin","ontology_source":"CHEBI"},"preferred_term":"Maltodextrin","sssom_rows":[{"data_row":1766,"object_id":"CHEBI:25140","object_label":"maltodextrin","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Maltodextrin","synonym_count":0} |
| ev-8953e391dc07832e | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1339] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-ddc5d2f491e1dfe9 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Maltodextrin; data-row positions=[1766] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1766,"object_id":"CHEBI:25140","object_label":"maltodextrin","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Maltodextrin","validation_method":"OAK+OLS:chebi&#124;CONFIRMED&#124;2026-07-07"}] |
| ev-02fb76409e18aa19 | docs/data/mapped_ingredients.csv; CSV lines=[1341] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:25140","line":1341,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"1","ontology_id":"CHEBI:25140","preferred_term":"Maltodextrin","total_occurrences":"1"}] |
| ev-2d35908e8a426432 | reports/yaml_record_review/Maltodextrin.md; &#96;data/ingredients/mapped/Maltodextrin.yaml&#96;:2; Verdict:4; Identity:12; Validation:21; Evidence:28; Completeness:34; Recommended Edits:41 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-f3aeb204902ea0fe | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[893,1543] | context_only | [{"current_record_sha256":"0dd1be3b08fab491189a693781600195c8854e04b8b090eed69df17072c0ab5f","finding_id":"SEM:10dfc4816342ddc810c5","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"0dd1be3b08fab491189a693781600195c8854e04b8b090eed69df17072c0ab5f","finding_id":"SEM:2d8187416f2447f5824f","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-a808534acc7d9dc2 | data/ingredients/mapped/Maltodextrin.yaml; nutritional_roles[0] | supports | Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION: [{"field":"nutritional_roles[0]","role":{"confidence":0.7,"evidence":[{"curator_note":"Provisional role inferred from CHEBI is_a/has_role closure; review recommended.","reference_text":"Inferred from CHEBI ancestry: subclass/has_role of CHEBI:16646 (carbohydrate)","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"CARBON_SOURCE"}}] |
| ev-6510f750083c1a05 | reviews/structured/20261011T024636Z-mim-reconcile-all-batch-08/review.yaml; findings[finding_id=f-9303a408608808ba] | context_only | Predecessor structured review finding f-9303a408608808ba in 20261011T024636Z-mim-reconcile-all-batch-08 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024636Z-mim-reconcile-all-batch-08.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-maltodextrin
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Maltodextrin (data/ingredients/mapped/Maltodextrin.yaml)'
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
summary: Per-record structured review for Maltodextrin (data/ingredients/mapped/Maltodextrin.yaml,
  record-521c77db3812fd7a, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Maltodextrin.yaml
    sha256: 0dd1be3b08fab491189a693781600195c8854e04b8b090eed69df17072c0ab5f
    role: target
  - path: reviews/structured/20261011T024636Z-mim-reconcile-all-batch-08/review.yaml
    sha256: 4dd969b7020555cc2250a236d6fded134bedf3add1e1c5c72d269e98f9ae001b
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
  - path: reports/yaml_record_review/Maltodextrin.md
    sha256: ca1b8afe1ae8ff653e59e3c98e1f257583ed067c0a5847afec248c28138268b2
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-521c77db3812fd7a
  path: data/ingredients/mapped/Maltodextrin.yaml
  label: Maltodextrin
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Maltodextrin.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Maltodextrin.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Maltodextrin.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-521c77db3812fd7a
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-521c77db3812fd7a
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-521c77db3812fd7a
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024636Z-mim-reconcile-all-batch-08
    and semantic review dispositions on HEAD.
  target_ids:
  - record-521c77db3812fd7a
evidence:
- evidence_id: ev-50fb2ac30bdde1a0
  kind: record_content
  reference: data/ingredients/mapped/Maltodextrin.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1339],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:25140","line":1341,"mapping_status":"MAPPED","ontology_id":"CHEBI:25140","preferred_term":"Maltodextrin"}],"identifier":"CHEBI:25140","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":1,"edge_count":1,"occurrences":1},"occurrence_statistics":{"media_count":1,"total_occurrences":1},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:25140","ontology_label":"maltodextrin","ontology_source":"CHEBI"},"preferred_term":"Maltodextrin","sssom_rows":[{"data_row":1766,"object_id":"CHEBI:25140","object_label":"maltodextrin","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Maltodextrin","synonym_count":0}'
  snapshot_sha256: 0dd1be3b08fab491189a693781600195c8854e04b8b090eed69df17072c0ab5f
- evidence_id: ev-8953e391dc07832e
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1339]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-ddc5d2f491e1dfe9
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Maltodextrin; data-row positions=[1766]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1766,"object_id":"CHEBI:25140","object_label":"maltodextrin","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Maltodextrin","validation_method":"OAK+OLS:chebi|CONFIRMED|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-02fb76409e18aa19
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1341]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:25140","line":1341,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"1","ontology_id":"CHEBI:25140","preferred_term":"Maltodextrin","total_occurrences":"1"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-2d35908e8a426432
  kind: prior_review
  reference: reports/yaml_record_review/Maltodextrin.md
  locator: '`data/ingredients/mapped/Maltodextrin.yaml`:2; Verdict:4; Identity:12;
    Validation:21; Evidence:28; Completeness:34; Recommended Edits:41'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: ca1b8afe1ae8ff653e59e3c98e1f257583ed067c0a5847afec248c28138268b2
  quote: "Recommended Edits:\n- Remove `CARBON_SOURCE` unless source-backed evidence\
    \ for maltodextrin as a\n  media carbon source can be attached."
- evidence_id: ev-f3aeb204902ea0fe
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[893,1543]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"0dd1be3b08fab491189a693781600195c8854e04b8b090eed69df17072c0ab5f","finding_id":"SEM:10dfc4816342ddc810c5","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"0dd1be3b08fab491189a693781600195c8854e04b8b090eed69df17072c0ab5f","finding_id":"SEM:2d8187416f2447f5824f","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-a808534acc7d9dc2
  kind: record_content
  reference: data/ingredients/mapped/Maltodextrin.yaml
  locator: nutritional_roles[0]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION:
    [{"field":"nutritional_roles[0]","role":{"confidence":0.7,"evidence":[{"curator_note":"Provisional
    role inferred from CHEBI is_a/has_role closure; review recommended.","reference_text":"Inferred
    from CHEBI ancestry: subclass/has_role of CHEBI:16646 (carbohydrate)","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"CARBON_SOURCE"}}]'
  snapshot_sha256: 0dd1be3b08fab491189a693781600195c8854e04b8b090eed69df17072c0ab5f
- evidence_id: ev-6510f750083c1a05
  kind: prior_review
  reference: reviews/structured/20261011T024636Z-mim-reconcile-all-batch-08/review.yaml
  locator: findings[finding_id=f-9303a408608808ba]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-9303a408608808ba in 20261011T024636Z-mim-reconcile-all-batch-08
  snapshot_sha256: 4dd969b7020555cc2250a236d6fded134bedf3add1e1c5c72d269e98f9ae001b
assessments:
- assessment_id: a-4eabee65f26c6e2c
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-521c77db3812fd7a
  evidence_ids:
  - ev-50fb2ac30bdde1a0
  - ev-8953e391dc07832e
  - ev-ddc5d2f491e1dfe9
  - ev-02fb76409e18aa19
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-b1281bc63a5f9225
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-521c77db3812fd7a
  evidence_ids:
  - ev-2d35908e8a426432
  - ev-50fb2ac30bdde1a0
  - ev-f3aeb204902ea0fe
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T01:27:59Z;
    reviewed SHA-256=0dd1be3b08fab491189a693781600195c8854e04b8b090eed69df17072c0ab5f;
    current SHA-256=0dd1be3b08fab491189a693781600195c8854e04b8b090eed69df17072c0ab5f;
    hash_changed=False. Reports=["reports/yaml_record_review/Maltodextrin.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The exact CHEBI:25140
    identity, occurrence count, empty other field, and final SSSOM row pass, but CARBON_SOURCE
    is provisional.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-2d35908e8a426432
    - ev-50fb2ac30bdde1a0
  - name: legacy-native-ids
    value: '["SEM:10dfc4816342ddc810c5","SEM:2d8187416f2447f5824f"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-50fb2ac30bdde1a0
    - ev-2d35908e8a426432
    - ev-f3aeb204902ea0fe
- assessment_id: a-a808534acc7d9dc2
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-521c77db3812fd7a
  evidence_ids:
  - ev-2d35908e8a426432
  - ev-a808534acc7d9dc2
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-2d35908e8a426432
    - ev-a808534acc7d9dc2
findings:
- finding_id: rec-f-9303a408608808ba
  issue_key: mim-reconciliation-role-support-521c77db3812fd7a
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Maltodextrin'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-521c77db3812fd7a
  evidence_ids:
  - ev-2d35908e8a426432
  - ev-a808534acc7d9dc2
  - ev-6510f750083c1a05
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Maltodextrin.yaml
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
    review_id: 20261011T024636Z-mim-reconcile-all-batch-08
    finding_id: f-9303a408608808ba
actions:
- action_id: rec-action-9303a408608808ba
  description: 'Reassess prediction-only role support: Maltodextrin'
  finding_ids:
  - rec-f-9303a408608808ba
  target_ids:
  - record-521c77db3812fd7a
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Maltodextrin.yaml
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
  with lineage to 20261011T024636Z-mim-reconcile-all-batch-08.
```
