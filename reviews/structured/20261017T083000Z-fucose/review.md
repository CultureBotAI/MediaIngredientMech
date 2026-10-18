# Per-record structured review: Fucose (data/ingredients/mapped/Fucose.yaml)

- Review: 20261017T083000Z-fucose
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Fucose (data/ingredients/mapped/Fucose.yaml, record-ff36aee01dde27dd, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Fucose.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Fucose.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-ff36aee01dde27dd | data/ingredients/mapped/Fucose.yaml | maintained | Fucose |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-ff36aee01dde27dd | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-ff36aee01dde27dd | Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-ff36aee01dde27dd | Reconciled against predecessor batch review 20261011T024634Z-mim-reconcile-all-batch-06 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-ff36aee01dde27dd.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-ff36aee01dde27dd.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T17:08:07Z; reviewed SHA-256=e9f2c1661ed11a6bc80f2dc0ba4714218a9f071643d82f3abfd5d6d85f469601; current SHA-256=e9f2c1661ed11a6bc80f2dc0ba4714218a9f071643d82f3abfd5d6d85f469601; hash_changed=False. Reports=["reports/yaml_record_review/Fucose.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact fucose identity and final SSSOM payload pass, but CARBON_SOURCE is computational.

### Historical provisional-role concern

evidence: concern. Targets: record-ff36aee01dde27dd.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-95a39e75608ce2ae: Reassess prediction-only role support: Fucose

major / open / confirmed; issue key: mim-reconciliation-role-support-ff36aee01dde27dd.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-95a39e75608ce2ae

Reassess prediction-only role support: Fucose

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-f2277a1802ff3fa5 | data/ingredients/mapped/Fucose.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1027],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:33984","line":1029,"mapping_status":"MAPPED","ontology_id":"CHEBI:33984","preferred_term":"Fucose"}],"identifier":"CHEBI:33984","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":2,"edge_count":2,"occurrences":2},"occurrence_statistics":{"media_count":2,"total_occurrences":2},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:33984","ontology_label":"fucose","ontology_source":"CHEBI"},"preferred_term":"Fucose","sssom_rows":[{"data_row":1251,"object_id":"CHEBI:33984","object_label":"fucose","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Fucose","synonym_count":2} |
| ev-3f0c6179d96c1c0f | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1027] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-225bf371e308303c | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Fucose; data-row positions=[1251] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1251,"object_id":"CHEBI:33984","object_label":"fucose","other":"6-Deoxygalactose&#124;Fuc&#124;CAS:7724-73-4","predicate_id":"skos:exactMatch","subject_id":"MIM:Fucose","validation_method":"OAK+OLS:chebi&#124;CONFIRMED&#124;2026-07-07"}] |
| ev-4c0f675394d339c5 | docs/data/mapped_ingredients.csv; CSV lines=[1029] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:33984","line":1029,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"2","ontology_id":"CHEBI:33984","preferred_term":"Fucose","total_occurrences":"2"}] |
| ev-25145a8a4e6e7240 | reports/yaml_record_review/Fucose.md; &#96;data/ingredients/mapped/Fucose.yaml&#96;:2; Verdict:4; Identity:10; Validation:21; Evidence:34; Completeness:51; Recommended Edits:58 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-8e3763f0d305bbdd | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[637,1558] | context_only | [{"current_record_sha256":"e9f2c1661ed11a6bc80f2dc0ba4714218a9f071643d82f3abfd5d6d85f469601","finding_id":"SEM:7909db893a8cd70876c6","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"e9f2c1661ed11a6bc80f2dc0ba4714218a9f071643d82f3abfd5d6d85f469601","finding_id":"SEM:162b821de8052014ba2a","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-660df23b70616b54 | data/ingredients/mapped/Fucose.yaml; nutritional_roles[0] | supports | Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION: [{"field":"nutritional_roles[0]","role":{"confidence":0.7,"evidence":[{"curator_note":"Provisional role inferred from CHEBI is_a/has_role closure; review recommended.","reference_text":"Inferred from CHEBI ancestry: subclass/has_role of CHEBI:16646 (carbohydrate)","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"CARBON_SOURCE"}}] |
| ev-d0fa53b60f3996a5 | reviews/structured/20261011T024634Z-mim-reconcile-all-batch-06/review.yaml; findings[finding_id=f-95a39e75608ce2ae] | context_only | Predecessor structured review finding f-95a39e75608ce2ae in 20261011T024634Z-mim-reconcile-all-batch-06 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024634Z-mim-reconcile-all-batch-06.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-fucose
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Fucose (data/ingredients/mapped/Fucose.yaml)'
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
summary: Per-record structured review for Fucose (data/ingredients/mapped/Fucose.yaml,
  record-ff36aee01dde27dd, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Fucose.yaml
    sha256: e9f2c1661ed11a6bc80f2dc0ba4714218a9f071643d82f3abfd5d6d85f469601
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
  - path: reports/yaml_record_review/Fucose.md
    sha256: 76a24d2d9f735db10ad2a1a9af557cebff17b7f8c75db60336bb4c6727eb8ae9
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-ff36aee01dde27dd
  path: data/ingredients/mapped/Fucose.yaml
  label: Fucose
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Fucose.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Fucose.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Fucose.yaml selected from full-corpus
    review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-ff36aee01dde27dd
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-ff36aee01dde27dd
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-ff36aee01dde27dd
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024634Z-mim-reconcile-all-batch-06
    and semantic review dispositions on HEAD.
  target_ids:
  - record-ff36aee01dde27dd
evidence:
- evidence_id: ev-f2277a1802ff3fa5
  kind: record_content
  reference: data/ingredients/mapped/Fucose.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1027],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:33984","line":1029,"mapping_status":"MAPPED","ontology_id":"CHEBI:33984","preferred_term":"Fucose"}],"identifier":"CHEBI:33984","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":2,"edge_count":2,"occurrences":2},"occurrence_statistics":{"media_count":2,"total_occurrences":2},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:33984","ontology_label":"fucose","ontology_source":"CHEBI"},"preferred_term":"Fucose","sssom_rows":[{"data_row":1251,"object_id":"CHEBI:33984","object_label":"fucose","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Fucose","synonym_count":2}'
  snapshot_sha256: e9f2c1661ed11a6bc80f2dc0ba4714218a9f071643d82f3abfd5d6d85f469601
- evidence_id: ev-3f0c6179d96c1c0f
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1027]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-225bf371e308303c
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Fucose; data-row positions=[1251]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1251,"object_id":"CHEBI:33984","object_label":"fucose","other":"6-Deoxygalactose|Fuc|CAS:7724-73-4","predicate_id":"skos:exactMatch","subject_id":"MIM:Fucose","validation_method":"OAK+OLS:chebi|CONFIRMED|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-4c0f675394d339c5
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1029]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:33984","line":1029,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"2","ontology_id":"CHEBI:33984","preferred_term":"Fucose","total_occurrences":"2"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-25145a8a4e6e7240
  kind: prior_review
  reference: reports/yaml_record_review/Fucose.md
  locator: '`data/ingredients/mapped/Fucose.yaml`:2; Verdict:4; Identity:10; Validation:21;
    Evidence:34; Completeness:51; Recommended Edits:58'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 76a24d2d9f735db10ad2a1a9af557cebff17b7f8c75db60336bb4c6727eb8ae9
  quote: "Recommended Edits:\n- Major: either replace `nutritional_roles.CARBON_SOURCE`\
    \ in\n  `data/ingredients/mapped/Fucose.yaml` with inspected source-backed evidence\n\
    \  for fucose in media, or remove the unsupported role; then sync\n  `data/curated/mapped_ingredients.yaml`\
    \ and rerun strict validation."
- evidence_id: ev-8e3763f0d305bbdd
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[637,1558]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"e9f2c1661ed11a6bc80f2dc0ba4714218a9f071643d82f3abfd5d6d85f469601","finding_id":"SEM:7909db893a8cd70876c6","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"e9f2c1661ed11a6bc80f2dc0ba4714218a9f071643d82f3abfd5d6d85f469601","finding_id":"SEM:162b821de8052014ba2a","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-660df23b70616b54
  kind: record_content
  reference: data/ingredients/mapped/Fucose.yaml
  locator: nutritional_roles[0]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION:
    [{"field":"nutritional_roles[0]","role":{"confidence":0.7,"evidence":[{"curator_note":"Provisional
    role inferred from CHEBI is_a/has_role closure; review recommended.","reference_text":"Inferred
    from CHEBI ancestry: subclass/has_role of CHEBI:16646 (carbohydrate)","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"CARBON_SOURCE"}}]'
  snapshot_sha256: e9f2c1661ed11a6bc80f2dc0ba4714218a9f071643d82f3abfd5d6d85f469601
- evidence_id: ev-d0fa53b60f3996a5
  kind: prior_review
  reference: reviews/structured/20261011T024634Z-mim-reconcile-all-batch-06/review.yaml
  locator: findings[finding_id=f-95a39e75608ce2ae]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-95a39e75608ce2ae in 20261011T024634Z-mim-reconcile-all-batch-06
  snapshot_sha256: 14c3200be95fdc87fca16bb71628432f3c9aaf8a65356ed494efc776ebe8aa11
assessments:
- assessment_id: a-d3e1190805a62b5c
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-ff36aee01dde27dd
  evidence_ids:
  - ev-f2277a1802ff3fa5
  - ev-3f0c6179d96c1c0f
  - ev-225bf371e308303c
  - ev-4c0f675394d339c5
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-7c463f82e34b1da4
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-ff36aee01dde27dd
  evidence_ids:
  - ev-25145a8a4e6e7240
  - ev-f2277a1802ff3fa5
  - ev-8e3763f0d305bbdd
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T17:08:07Z;
    reviewed SHA-256=e9f2c1661ed11a6bc80f2dc0ba4714218a9f071643d82f3abfd5d6d85f469601;
    current SHA-256=e9f2c1661ed11a6bc80f2dc0ba4714218a9f071643d82f3abfd5d6d85f469601;
    hash_changed=False. Reports=["reports/yaml_record_review/Fucose.md"]. Full reports,
    including older originals behind refresh floors, are hashed inputs. Repeated refresh
    allegations are not counted as new defects. The narrative group is not a count
    of distinct scientific findings. Latest manifest note: The exact fucose identity
    and final SSSOM payload pass, but CARBON_SOURCE is computational.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-25145a8a4e6e7240
    - ev-f2277a1802ff3fa5
  - name: legacy-native-ids
    value: '["SEM:7909db893a8cd70876c6","SEM:162b821de8052014ba2a"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-f2277a1802ff3fa5
    - ev-25145a8a4e6e7240
    - ev-8e3763f0d305bbdd
- assessment_id: a-660df23b70616b54
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-ff36aee01dde27dd
  evidence_ids:
  - ev-25145a8a4e6e7240
  - ev-660df23b70616b54
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-25145a8a4e6e7240
    - ev-660df23b70616b54
findings:
- finding_id: rec-f-95a39e75608ce2ae
  issue_key: mim-reconciliation-role-support-ff36aee01dde27dd
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Fucose'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-ff36aee01dde27dd
  evidence_ids:
  - ev-25145a8a4e6e7240
  - ev-660df23b70616b54
  - ev-d0fa53b60f3996a5
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Fucose.yaml
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
    review_id: 20261011T024634Z-mim-reconcile-all-batch-06
    finding_id: f-95a39e75608ce2ae
actions:
- action_id: rec-action-95a39e75608ce2ae
  description: 'Reassess prediction-only role support: Fucose'
  finding_ids:
  - rec-f-95a39e75608ce2ae
  target_ids:
  - record-ff36aee01dde27dd
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Fucose.yaml
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
