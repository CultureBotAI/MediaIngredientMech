# Per-record structured review: Mgcl2_X_7_H2o (data/ingredients/mapped/Mgcl2_X_7_H2o.yaml)

- Review: 20261017T083000Z-mgcl2-x-7-h2o
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Mgcl2_X_7_H2o (data/ingredients/mapped/Mgcl2_X_7_H2o.yaml, record-0780306277dec459, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Mgcl2_X_7_H2o.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Mgcl2_X_7_H2o.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-0780306277dec459 | data/ingredients/mapped/Mgcl2_X_7_H2o.yaml | maintained | Mgcl2_X_7_H2o |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-0780306277dec459 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-0780306277dec459 | Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-0780306277dec459 | Reconciled against predecessor batch review 20261011T024636Z-mim-reconcile-all-batch-08 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-0780306277dec459.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-0780306277dec459.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T03:09:28Z; reviewed SHA-256=b7be6c96f9c0db49038f31d4186149cff28469ccdc95c4ddd85dcc38279689cf; current SHA-256=b7be6c96f9c0db49038f31d4186149cff28469ccdc95c4ddd85dcc38279689cf; hash_changed=False. Reports=["reports/yaml_record_review/Mgcl2_X_7_H2o.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The local unresolved heptahydrate identity and close anhydrous parent rows pass, but MINERAL_SOURCE is still a provisional name-list role.

### Historical provisional-role concern

evidence: concern. Targets: record-0780306277dec459.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-852531fb1749d93e: Reassess prediction-only role support: MgCl2 x 7 H2O

major / open / confirmed; issue key: mim-reconciliation-role-support-0780306277dec459.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-852531fb1749d93e

Reassess prediction-only role support: MgCl2 x 7 H2O

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-65c4a6d4b2bb676a | data/ingredients/mapped/Mgcl2_X_7_H2o.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1395],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.compound:mgcl2_x_7_h2o","line":1397,"mapping_status":"MAPPED","ontology_id":"CHEBI:6636","preferred_term":"MgCl2 x 7 H2O"}],"identifier":"kgmicrobe.compound:mgcl2_x_7_h2o","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":19,"edge_count":19,"occurrences":19},"occurrence_statistics":{"media_count":19,"total_occurrences":19},"ontology_mapping":{"mapping_quality":"CLOSE_MATCH","ontology_id":"CHEBI:6636","ontology_label":"magnesium dichloride","ontology_source":"CHEBI"},"preferred_term":"MgCl2 x 7 H2O","sssom_rows":[{"data_row":1863,"object_id":"CHEBI:6636","object_label":"magnesium dichloride","predicate_id":"skos:closeMatch"},{"data_row":1864,"object_id":"kgmicrobe.compound:mgcl2_x_7_h2o","object_label":"MgCl2 x 7 H2O","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Mgcl2_X_7_H2o","synonym_count":8} |
| ev-4c6b19a9746c5ee4 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1395] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-259671ec49b6e411 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Mgcl2_X_7_H2o; data-row positions=[1863,1864] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1863,"object_id":"CHEBI:6636","object_label":"magnesium dichloride","other":"MgCl2 x 7H2O&#124;MgCl2x7H2O&#124;MgCl2  x 7 H2O","predicate_id":"skos:closeMatch","subject_id":"MIM:Mgcl2_X_7_H2o","validation_method":""},{"data_row":1864,"object_id":"kgmicrobe.compound:mgcl2_x_7_h2o","object_label":"MgCl2 x 7 H2O","other":"MgCl2 x 7H2O&#124;MgCl2x7H2O&#124;MgCl2  x 7 H2O","predicate_id":"skos:exactMatch","subject_id":"MIM:Mgcl2_X_7_H2o","validation_method":""}] |
| ev-1fa58e21fdc1963a | docs/data/mapped_ingredients.csv; CSV lines=[1397] | supports | Published identity and count rows inspected: [{"identifier":"kgmicrobe.compound:mgcl2_x_7_h2o","line":1397,"mapping_quality":"CLOSE_MATCH","mapping_status":"MAPPED","media_count":"19","ontology_id":"CHEBI:6636","preferred_term":"MgCl2 x 7 H2O","total_occurrences":"19"}] |
| ev-d7fe42bd3d45af2b | reports/yaml_record_review/Mgcl2_X_7_H2o.md; &#96;data/ingredients/mapped/Mgcl2_X_7_H2o.yaml&#96;:2; Verdict:4; Identity:14; Validation:27; Evidence:35; Completeness:50; Recommended Edits:58 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-ea3b05d736d4aeab | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[932,2071] | context_only | [{"current_record_sha256":"b7be6c96f9c0db49038f31d4186149cff28469ccdc95c4ddd85dcc38279689cf","finding_id":"SEM:945cf88ca506bab317a0","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"b7be6c96f9c0db49038f31d4186149cff28469ccdc95c4ddd85dcc38279689cf","finding_id":"SEM:b99044c5c4a06ceb2bc8","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-9a1f8188c064c496 | data/ingredients/mapped/Mgcl2_X_7_H2o.yaml; nutritional_roles[0] | supports | Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION: [{"field":"nutritional_roles[0]","role":{"confidence":0.8,"evidence":[{"curator_note":"Provisional role from a curated name-pattern rule; review recommended.","reference_text":"Inferred from curated media-role name pattern","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"MINERAL_SOURCE"}}] |
| ev-593f5295b92999b4 | reviews/structured/20261011T024636Z-mim-reconcile-all-batch-08/review.yaml; findings[finding_id=f-852531fb1749d93e] | context_only | Predecessor structured review finding f-852531fb1749d93e in 20261011T024636Z-mim-reconcile-all-batch-08 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024636Z-mim-reconcile-all-batch-08.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-mgcl2-x-7-h2o
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Mgcl2_X_7_H2o (data/ingredients/mapped/Mgcl2_X_7_H2o.yaml)'
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
summary: Per-record structured review for Mgcl2_X_7_H2o (data/ingredients/mapped/Mgcl2_X_7_H2o.yaml,
  record-0780306277dec459, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Mgcl2_X_7_H2o.yaml
    sha256: b7be6c96f9c0db49038f31d4186149cff28469ccdc95c4ddd85dcc38279689cf
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
  - path: reports/yaml_record_review/Mgcl2_X_7_H2o.md
    sha256: 61e30d3996e0e0307d3634f494b3df3ecc77facdd2c1e5721a481eca4fcfbea6
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-0780306277dec459
  path: data/ingredients/mapped/Mgcl2_X_7_H2o.yaml
  label: Mgcl2_X_7_H2o
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Mgcl2_X_7_H2o.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Mgcl2_X_7_H2o.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Mgcl2_X_7_H2o.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-0780306277dec459
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-0780306277dec459
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-0780306277dec459
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024636Z-mim-reconcile-all-batch-08
    and semantic review dispositions on HEAD.
  target_ids:
  - record-0780306277dec459
evidence:
- evidence_id: ev-65c4a6d4b2bb676a
  kind: record_content
  reference: data/ingredients/mapped/Mgcl2_X_7_H2o.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1395],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.compound:mgcl2_x_7_h2o","line":1397,"mapping_status":"MAPPED","ontology_id":"CHEBI:6636","preferred_term":"MgCl2
    x 7 H2O"}],"identifier":"kgmicrobe.compound:mgcl2_x_7_h2o","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":19,"edge_count":19,"occurrences":19},"occurrence_statistics":{"media_count":19,"total_occurrences":19},"ontology_mapping":{"mapping_quality":"CLOSE_MATCH","ontology_id":"CHEBI:6636","ontology_label":"magnesium
    dichloride","ontology_source":"CHEBI"},"preferred_term":"MgCl2 x 7 H2O","sssom_rows":[{"data_row":1863,"object_id":"CHEBI:6636","object_label":"magnesium
    dichloride","predicate_id":"skos:closeMatch"},{"data_row":1864,"object_id":"kgmicrobe.compound:mgcl2_x_7_h2o","object_label":"MgCl2
    x 7 H2O","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Mgcl2_X_7_H2o","synonym_count":8}'
  snapshot_sha256: b7be6c96f9c0db49038f31d4186149cff28469ccdc95c4ddd85dcc38279689cf
- evidence_id: ev-4c6b19a9746c5ee4
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1395]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-259671ec49b6e411
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Mgcl2_X_7_H2o; data-row positions=[1863,1864]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1863,"object_id":"CHEBI:6636","object_label":"magnesium
    dichloride","other":"MgCl2 x 7H2O|MgCl2x7H2O|MgCl2  x 7 H2O","predicate_id":"skos:closeMatch","subject_id":"MIM:Mgcl2_X_7_H2o","validation_method":""},{"data_row":1864,"object_id":"kgmicrobe.compound:mgcl2_x_7_h2o","object_label":"MgCl2
    x 7 H2O","other":"MgCl2 x 7H2O|MgCl2x7H2O|MgCl2  x 7 H2O","predicate_id":"skos:exactMatch","subject_id":"MIM:Mgcl2_X_7_H2o","validation_method":""}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-1fa58e21fdc1963a
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1397]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"kgmicrobe.compound:mgcl2_x_7_h2o","line":1397,"mapping_quality":"CLOSE_MATCH","mapping_status":"MAPPED","media_count":"19","ontology_id":"CHEBI:6636","preferred_term":"MgCl2
    x 7 H2O","total_occurrences":"19"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-d7fe42bd3d45af2b
  kind: prior_review
  reference: reports/yaml_record_review/Mgcl2_X_7_H2o.md
  locator: '`data/ingredients/mapped/Mgcl2_X_7_H2o.yaml`:2; Verdict:4; Identity:14;
    Validation:27; Evidence:35; Completeness:50; Recommended Edits:58'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 61e30d3996e0e0307d3634f494b3df3ecc77facdd2c1e5721a481eca4fcfbea6
  quote: "Recommended Edits:\n- Major: replace the provisional `MINERAL_SOURCE` role\
    \ with a supported role\n  assertion if this local source identity was imported\
    \ with a mineral-source\n  role, or remove the role facet from\n  `data/ingredients/mapped/Mgcl2_X_7_H2o.yaml`."
- evidence_id: ev-ea3b05d736d4aeab
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[932,2071]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"b7be6c96f9c0db49038f31d4186149cff28469ccdc95c4ddd85dcc38279689cf","finding_id":"SEM:945cf88ca506bab317a0","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"b7be6c96f9c0db49038f31d4186149cff28469ccdc95c4ddd85dcc38279689cf","finding_id":"SEM:b99044c5c4a06ceb2bc8","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-9a1f8188c064c496
  kind: record_content
  reference: data/ingredients/mapped/Mgcl2_X_7_H2o.yaml
  locator: nutritional_roles[0]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION:
    [{"field":"nutritional_roles[0]","role":{"confidence":0.8,"evidence":[{"curator_note":"Provisional
    role from a curated name-pattern rule; review recommended.","reference_text":"Inferred
    from curated media-role name pattern","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"MINERAL_SOURCE"}}]'
  snapshot_sha256: b7be6c96f9c0db49038f31d4186149cff28469ccdc95c4ddd85dcc38279689cf
- evidence_id: ev-593f5295b92999b4
  kind: prior_review
  reference: reviews/structured/20261011T024636Z-mim-reconcile-all-batch-08/review.yaml
  locator: findings[finding_id=f-852531fb1749d93e]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-852531fb1749d93e in 20261011T024636Z-mim-reconcile-all-batch-08
  snapshot_sha256: 4dd969b7020555cc2250a236d6fded134bedf3add1e1c5c72d269e98f9ae001b
assessments:
- assessment_id: a-0bfb847c3c401e7c
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-0780306277dec459
  evidence_ids:
  - ev-65c4a6d4b2bb676a
  - ev-4c6b19a9746c5ee4
  - ev-259671ec49b6e411
  - ev-1fa58e21fdc1963a
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-d33aecd0339830b8
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-0780306277dec459
  evidence_ids:
  - ev-d7fe42bd3d45af2b
  - ev-65c4a6d4b2bb676a
  - ev-ea3b05d736d4aeab
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T03:09:28Z;
    reviewed SHA-256=b7be6c96f9c0db49038f31d4186149cff28469ccdc95c4ddd85dcc38279689cf;
    current SHA-256=b7be6c96f9c0db49038f31d4186149cff28469ccdc95c4ddd85dcc38279689cf;
    hash_changed=False. Reports=["reports/yaml_record_review/Mgcl2_X_7_H2o.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The local unresolved
    heptahydrate identity and close anhydrous parent rows pass, but MINERAL_SOURCE
    is still a provisional name-list role.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-d7fe42bd3d45af2b
    - ev-65c4a6d4b2bb676a
  - name: legacy-native-ids
    value: '["SEM:945cf88ca506bab317a0","SEM:b99044c5c4a06ceb2bc8"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-65c4a6d4b2bb676a
    - ev-d7fe42bd3d45af2b
    - ev-ea3b05d736d4aeab
- assessment_id: a-9a1f8188c064c496
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-0780306277dec459
  evidence_ids:
  - ev-d7fe42bd3d45af2b
  - ev-9a1f8188c064c496
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-d7fe42bd3d45af2b
    - ev-9a1f8188c064c496
findings:
- finding_id: rec-f-852531fb1749d93e
  issue_key: mim-reconciliation-role-support-0780306277dec459
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: MgCl2 x 7 H2O'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-0780306277dec459
  evidence_ids:
  - ev-d7fe42bd3d45af2b
  - ev-9a1f8188c064c496
  - ev-593f5295b92999b4
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Mgcl2_X_7_H2o.yaml
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
    finding_id: f-852531fb1749d93e
actions:
- action_id: rec-action-852531fb1749d93e
  description: 'Reassess prediction-only role support: MgCl2 x 7 H2O'
  finding_ids:
  - rec-f-852531fb1749d93e
  target_ids:
  - record-0780306277dec459
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Mgcl2_X_7_H2o.yaml
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
