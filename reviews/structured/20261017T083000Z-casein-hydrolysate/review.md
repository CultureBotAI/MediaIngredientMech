# Per-record structured review: Casein_hydrolysate (data/ingredients/mapped/Casein_hydrolysate.yaml)

- Review: 20261017T083000Z-casein-hydrolysate
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Casein_hydrolysate (data/ingredients/mapped/Casein_hydrolysate.yaml, record-53320d6c9c0582a1, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Casein_hydrolysate.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Casein_hydrolysate.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-53320d6c9c0582a1 | data/ingredients/mapped/Casein_hydrolysate.yaml | maintained | Casein_hydrolysate |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-53320d6c9c0582a1 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-53320d6c9c0582a1 | Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-53320d6c9c0582a1 | Reconciled against predecessor batch review 20261011T024632Z-mim-reconcile-all-batch-04 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-53320d6c9c0582a1.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-53320d6c9c0582a1.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T11:09:19Z; reviewed SHA-256=a61d7e5378b52c5798f9161e8a6a75d1d76da1e5af96275d6207ad15b8199e49; current SHA-256=a61d7e5378b52c5798f9161e8a6a75d1d76da1e5af96275d6207ad15b8199e49; hash_changed=False. Reports=["reports/yaml_record_review/Casein_hydrolysate.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact MICRO casein hydrolysate identity passes, but PROTEIN_SOURCE is only a provisional name-pattern prediction.

### Historical provisional-role concern

evidence: concern. Targets: record-53320d6c9c0582a1.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-8894f7771f457ca5: Reassess prediction-only role support: Casein hydrolysate

major / open / confirmed; issue key: mim-reconciliation-role-support-53320d6c9c0582a1.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-8894f7771f457ca5

Reassess prediction-only role support: Casein hydrolysate

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-dae0b70695983ca0 | data/ingredients/mapped/Casein_hydrolysate.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[664],"raw_equal":true},"docs_rows":[{"identifier":"MICRO:0001366","line":666,"mapping_status":"MAPPED","ontology_id":"MICRO:0001366","preferred_term":"Casein hydrolysate"}],"identifier":"MICRO:0001366","ingredient_type":"UNDEFINED_MIXTURE","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":54,"edge_count":54,"occurrences":54},"occurrence_statistics":{"media_count":54,"total_occurrences":54},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"MICRO:0001366","ontology_label":"casein hydrolysate","ontology_source":"MICRO"},"preferred_term":"Casein hydrolysate","sssom_rows":[{"data_row":660,"object_id":"MICRO:0001366","object_label":"casein hydrolysate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Casein_hydrolysate","synonym_count":1} |
| ev-05348f8d800faad5 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [664] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-4f2644e86fff8e5d | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Casein_hydrolysate; data-row positions=[660] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":660,"object_id":"MICRO:0001366","object_label":"casein hydrolysate","other":"Acid hydrolysate of casein","predicate_id":"skos:exactMatch","subject_id":"MIM:Casein_hydrolysate","validation_method":"none&#124;UNKNOWN_TERM&#124;2026-07-07"}] |
| ev-618b9f8c842114cf | docs/data/mapped_ingredients.csv; CSV lines=[666] | supports | Published identity and count rows inspected: [{"identifier":"MICRO:0001366","line":666,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"54","ontology_id":"MICRO:0001366","preferred_term":"Casein hydrolysate","total_occurrences":"54"}] |
| ev-d0d73cd62c6351e2 | reports/yaml_record_review/Casein_hydrolysate.md; &#96;data/ingredients/mapped/Casein_hydrolysate.yaml&#96;:2; Verdict:4; Identity:11; Validation:25; Evidence:46; Completeness:61; Recommended Edits:68 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-37c01559215e327c | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[368,1916] | context_only | [{"current_record_sha256":"a61d7e5378b52c5798f9161e8a6a75d1d76da1e5af96275d6207ad15b8199e49","finding_id":"SEM:052910925e7c2f06dcd9","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"a61d7e5378b52c5798f9161e8a6a75d1d76da1e5af96275d6207ad15b8199e49","finding_id":"SEM:b2d96b9bda2a2008e9a0","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-a9790757794bbc90 | data/ingredients/mapped/Casein_hydrolysate.yaml; nutritional_roles[0] | supports | Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION: [{"field":"nutritional_roles[0]","role":{"confidence":0.8,"evidence":[{"curator_note":"Provisional role from a curated name-pattern rule; review recommended.","reference_text":"Inferred from curated media-role name pattern","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"PROTEIN_SOURCE"}}] |
| ev-eb71639fcca8fd15 | reviews/structured/20261011T024632Z-mim-reconcile-all-batch-04/review.yaml; findings[finding_id=f-8894f7771f457ca5] | context_only | Predecessor structured review finding f-8894f7771f457ca5 in 20261011T024632Z-mim-reconcile-all-batch-04 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024632Z-mim-reconcile-all-batch-04.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-casein-hydrolysate
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Casein_hydrolysate (data/ingredients/mapped/Casein_hydrolysate.yaml)'
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
summary: Per-record structured review for Casein_hydrolysate (data/ingredients/mapped/Casein_hydrolysate.yaml,
  record-53320d6c9c0582a1, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Casein_hydrolysate.yaml
    sha256: a61d7e5378b52c5798f9161e8a6a75d1d76da1e5af96275d6207ad15b8199e49
    role: target
  - path: reviews/structured/20261011T024632Z-mim-reconcile-all-batch-04/review.yaml
    sha256: 304aa2f246d52fcfef2fb5165e9b4c0995c263df5e818c23b30e9d76e3ec55e3
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
  - path: reports/yaml_record_review/Casein_hydrolysate.md
    sha256: fea541f47ba08791bbada57eecdde23bcd781d2d9788de60c9f82280a5e84fe4
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-53320d6c9c0582a1
  path: data/ingredients/mapped/Casein_hydrolysate.yaml
  label: Casein_hydrolysate
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Casein_hydrolysate.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Casein_hydrolysate.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Casein_hydrolysate.yaml selected
    from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-53320d6c9c0582a1
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-53320d6c9c0582a1
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-53320d6c9c0582a1
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024632Z-mim-reconcile-all-batch-04
    and semantic review dispositions on HEAD.
  target_ids:
  - record-53320d6c9c0582a1
evidence:
- evidence_id: ev-dae0b70695983ca0
  kind: record_content
  reference: data/ingredients/mapped/Casein_hydrolysate.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[664],"raw_equal":true},"docs_rows":[{"identifier":"MICRO:0001366","line":666,"mapping_status":"MAPPED","ontology_id":"MICRO:0001366","preferred_term":"Casein
    hydrolysate"}],"identifier":"MICRO:0001366","ingredient_type":"UNDEFINED_MIXTURE","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":54,"edge_count":54,"occurrences":54},"occurrence_statistics":{"media_count":54,"total_occurrences":54},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"MICRO:0001366","ontology_label":"casein
    hydrolysate","ontology_source":"MICRO"},"preferred_term":"Casein hydrolysate","sssom_rows":[{"data_row":660,"object_id":"MICRO:0001366","object_label":"casein
    hydrolysate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Casein_hydrolysate","synonym_count":1}'
  snapshot_sha256: a61d7e5378b52c5798f9161e8a6a75d1d76da1e5af96275d6207ad15b8199e49
- evidence_id: ev-05348f8d800faad5
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [664]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-4f2644e86fff8e5d
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Casein_hydrolysate; data-row positions=[660]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":660,"object_id":"MICRO:0001366","object_label":"casein
    hydrolysate","other":"Acid hydrolysate of casein","predicate_id":"skos:exactMatch","subject_id":"MIM:Casein_hydrolysate","validation_method":"none|UNKNOWN_TERM|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-618b9f8c842114cf
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[666]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"MICRO:0001366","line":666,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"54","ontology_id":"MICRO:0001366","preferred_term":"Casein
    hydrolysate","total_occurrences":"54"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-d0d73cd62c6351e2
  kind: prior_review
  reference: reports/yaml_record_review/Casein_hydrolysate.md
  locator: '`data/ingredients/mapped/Casein_hydrolysate.yaml`:2; Verdict:4; Identity:11;
    Validation:25; Evidence:46; Completeness:61; Recommended Edits:68'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: fea541f47ba08791bbada57eecdde23bcd781d2d9788de60c9f82280a5e84fe4
  quote: "Recommended Edits:\n- Major: either replace the provisional\n  `nutritional_roles.PROTEIN_SOURCE`\
    \ evidence in\n  `data/ingredients/mapped/Casein_hydrolysate.yaml` with inspected\
    \ evidence for\n  this casein-hydrolysate scope, or remove the role, then rerun\
    \ strict\n  validation, SSSOM QC, aggregate roundtrip, and `git diff --check`."
- evidence_id: ev-37c01559215e327c
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[368,1916]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"a61d7e5378b52c5798f9161e8a6a75d1d76da1e5af96275d6207ad15b8199e49","finding_id":"SEM:052910925e7c2f06dcd9","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"a61d7e5378b52c5798f9161e8a6a75d1d76da1e5af96275d6207ad15b8199e49","finding_id":"SEM:b2d96b9bda2a2008e9a0","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-a9790757794bbc90
  kind: record_content
  reference: data/ingredients/mapped/Casein_hydrolysate.yaml
  locator: nutritional_roles[0]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION:
    [{"field":"nutritional_roles[0]","role":{"confidence":0.8,"evidence":[{"curator_note":"Provisional
    role from a curated name-pattern rule; review recommended.","reference_text":"Inferred
    from curated media-role name pattern","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"PROTEIN_SOURCE"}}]'
  snapshot_sha256: a61d7e5378b52c5798f9161e8a6a75d1d76da1e5af96275d6207ad15b8199e49
- evidence_id: ev-eb71639fcca8fd15
  kind: prior_review
  reference: reviews/structured/20261011T024632Z-mim-reconcile-all-batch-04/review.yaml
  locator: findings[finding_id=f-8894f7771f457ca5]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-8894f7771f457ca5 in 20261011T024632Z-mim-reconcile-all-batch-04
  snapshot_sha256: 304aa2f246d52fcfef2fb5165e9b4c0995c263df5e818c23b30e9d76e3ec55e3
assessments:
- assessment_id: a-a8d21564734a8b0b
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-53320d6c9c0582a1
  evidence_ids:
  - ev-dae0b70695983ca0
  - ev-05348f8d800faad5
  - ev-4f2644e86fff8e5d
  - ev-618b9f8c842114cf
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-0d55afa1c7db6f43
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-53320d6c9c0582a1
  evidence_ids:
  - ev-d0d73cd62c6351e2
  - ev-dae0b70695983ca0
  - ev-37c01559215e327c
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T11:09:19Z;
    reviewed SHA-256=a61d7e5378b52c5798f9161e8a6a75d1d76da1e5af96275d6207ad15b8199e49;
    current SHA-256=a61d7e5378b52c5798f9161e8a6a75d1d76da1e5af96275d6207ad15b8199e49;
    hash_changed=False. Reports=["reports/yaml_record_review/Casein_hydrolysate.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The exact
    MICRO casein hydrolysate identity passes, but PROTEIN_SOURCE is only a provisional
    name-pattern prediction.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-d0d73cd62c6351e2
    - ev-dae0b70695983ca0
  - name: legacy-native-ids
    value: '["SEM:052910925e7c2f06dcd9","SEM:b2d96b9bda2a2008e9a0"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-dae0b70695983ca0
    - ev-d0d73cd62c6351e2
    - ev-37c01559215e327c
- assessment_id: a-a9790757794bbc90
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-53320d6c9c0582a1
  evidence_ids:
  - ev-d0d73cd62c6351e2
  - ev-a9790757794bbc90
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-d0d73cd62c6351e2
    - ev-a9790757794bbc90
findings:
- finding_id: rec-f-8894f7771f457ca5
  issue_key: mim-reconciliation-role-support-53320d6c9c0582a1
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Casein hydrolysate'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-53320d6c9c0582a1
  evidence_ids:
  - ev-d0d73cd62c6351e2
  - ev-a9790757794bbc90
  - ev-eb71639fcca8fd15
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Casein_hydrolysate.yaml
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
    review_id: 20261011T024632Z-mim-reconcile-all-batch-04
    finding_id: f-8894f7771f457ca5
actions:
- action_id: rec-action-8894f7771f457ca5
  description: 'Reassess prediction-only role support: Casein hydrolysate'
  finding_ids:
  - rec-f-8894f7771f457ca5
  target_ids:
  - record-53320d6c9c0582a1
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Casein_hydrolysate.yaml
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
  with lineage to 20261011T024632Z-mim-reconcile-all-batch-04.
```
