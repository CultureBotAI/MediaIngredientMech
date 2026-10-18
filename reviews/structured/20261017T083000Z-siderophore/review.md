# Per-record structured review: Siderophore (data/ingredients/mapped/Siderophore.yaml)

- Review: 20261017T083000Z-siderophore
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Siderophore (data/ingredients/mapped/Siderophore.yaml, record-264b6e7dc7f1d452, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Siderophore.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Siderophore.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-264b6e7dc7f1d452 | data/ingredients/mapped/Siderophore.yaml | maintained | Siderophore |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-264b6e7dc7f1d452 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-264b6e7dc7f1d452 | Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-264b6e7dc7f1d452 | Reconciled against predecessor batch review 20261011T024638Z-mim-reconcile-all-batch-10 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-264b6e7dc7f1d452.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-264b6e7dc7f1d452.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-10-01T05:03:21Z; reviewed SHA-256=cff4bd849c6a45c2034fed99f63f2773d5a482ec3cbb4fba8ce33c878bf860b8; current SHA-256=cff4bd849c6a45c2034fed99f63f2773d5a482ec3cbb4fba8ce33c878bf860b8; hash_changed=False. Reports=["reports/yaml_record_review/20261001T050321Z-Siderophore.md","reports/yaml_record_review/Siderophore.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: Refreshed &#96;reports/yaml_record_review/Siderophore.md&#96; after the record changed from bd1a1c002069e81d5c10478e4f5c1db7791a06766531ded5c9ecf1573df8a43a to cff4bd849c6a45c2034fed99f63f2773d5a482ec3cbb4fba8ce33c878bf860b8; preserved the previous major finding floor pending targeted retirement.

### Historical provisional-role concern

evidence: concern. Targets: record-264b6e7dc7f1d452.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-1d2159e3c902a1ca: Reassess prediction-only role support: Siderophore

major / open / confirmed; issue key: mim-reconciliation-role-support-264b6e7dc7f1d452.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-1d2159e3c902a1ca

Reassess prediction-only role support: Siderophore

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-c8a7587fd79e6b00 | data/ingredients/mapped/Siderophore.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1795],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:26672","line":1797,"mapping_status":"MAPPED","ontology_id":"CHEBI:26672","preferred_term":"Siderophore"}],"identifier":"CHEBI:26672","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:26672","ontology_label":"siderophore","ontology_source":"CHEBI"},"preferred_term":"Siderophore","sssom_rows":[{"data_row":2502,"object_id":"CHEBI:26672","object_label":"siderophore","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Siderophore","synonym_count":1} |
| ev-ef8843265f365165 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1795] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-2c3d79e4444259da | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Siderophore; data-row positions=[2502] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":2502,"object_id":"CHEBI:26672","object_label":"siderophore","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Siderophore","validation_method":"OAK+OLS:chebi&#124;CONFIRMED&#124;2026-07-07"}] |
| ev-073160b3ef6634f7 | docs/data/mapped_ingredients.csv; CSV lines=[1797] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:26672","line":1797,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:26672","preferred_term":"Siderophore","total_occurrences":"0"}] |
| ev-26edea8c147379be | reports/yaml_record_review/20261001T050321Z-Siderophore.md; YAML Record Review: Siderophore:2; Target:10; Validation:20; Identity and Grounding:27; Evidence:36; Completeness:46; Findings:52; Recommended Edits:56; Follow-up Checks:61; Additional Notes:67 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-f4e9cdee8d71d0b7 | reports/yaml_record_review/Siderophore.md; &#96;data/ingredients/mapped/Siderophore.yaml&#96;:2 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-23c2943cc6df7840 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1194,1474] | context_only | [{"current_record_sha256":"cff4bd849c6a45c2034fed99f63f2773d5a482ec3cbb4fba8ce33c878bf860b8","finding_id":"SEM:7a17f3cbcbdfb4a61e0c","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"cff4bd849c6a45c2034fed99f63f2773d5a482ec3cbb4fba8ce33c878bf860b8","finding_id":"SEM:b74685e1c2b28bbfffa6","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-1a2380a49fe46490 | data/ingredients/mapped/Siderophore.yaml; physicochemical_roles[0] | supports | Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION: [{"field":"physicochemical_roles[0]","role":{"confidence":0.7,"evidence":[{"curator_note":"Provisional role inferred from CHEBI is_a/has_role closure; review recommended.","reference_text":"Inferred from CHEBI ancestry: subclass/has_role of CHEBI:38161 (chelator (role))","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"CHELATOR"}}] |
| ev-b2475dc99d758037 | reviews/structured/20261011T024638Z-mim-reconcile-all-batch-10/review.yaml; findings[finding_id=f-1d2159e3c902a1ca] | context_only | Predecessor structured review finding f-1d2159e3c902a1ca in 20261011T024638Z-mim-reconcile-all-batch-10 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024638Z-mim-reconcile-all-batch-10.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-siderophore
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Siderophore (data/ingredients/mapped/Siderophore.yaml)'
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
summary: Per-record structured review for Siderophore (data/ingredients/mapped/Siderophore.yaml,
  record-264b6e7dc7f1d452, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Siderophore.yaml
    sha256: cff4bd849c6a45c2034fed99f63f2773d5a482ec3cbb4fba8ce33c878bf860b8
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
  - path: reports/yaml_record_review/20261001T050321Z-Siderophore.md
    sha256: e7aa920c2a24777ecdc8a179804f587151eee9ac5ee19bcbfef08e2c237ea421
    role: context
  - path: reports/yaml_record_review/Siderophore.md
    sha256: 44d9c010aea715409d2b039285a4087f35bcc1fe7750f458c76082a12f5490cd
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-264b6e7dc7f1d452
  path: data/ingredients/mapped/Siderophore.yaml
  label: Siderophore
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Siderophore.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Siderophore.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Siderophore.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-264b6e7dc7f1d452
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-264b6e7dc7f1d452
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-264b6e7dc7f1d452
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024638Z-mim-reconcile-all-batch-10
    and semantic review dispositions on HEAD.
  target_ids:
  - record-264b6e7dc7f1d452
evidence:
- evidence_id: ev-c8a7587fd79e6b00
  kind: record_content
  reference: data/ingredients/mapped/Siderophore.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1795],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:26672","line":1797,"mapping_status":"MAPPED","ontology_id":"CHEBI:26672","preferred_term":"Siderophore"}],"identifier":"CHEBI:26672","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:26672","ontology_label":"siderophore","ontology_source":"CHEBI"},"preferred_term":"Siderophore","sssom_rows":[{"data_row":2502,"object_id":"CHEBI:26672","object_label":"siderophore","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Siderophore","synonym_count":1}'
  snapshot_sha256: cff4bd849c6a45c2034fed99f63f2773d5a482ec3cbb4fba8ce33c878bf860b8
- evidence_id: ev-ef8843265f365165
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1795]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-2c3d79e4444259da
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Siderophore; data-row positions=[2502]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":2502,"object_id":"CHEBI:26672","object_label":"siderophore","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Siderophore","validation_method":"OAK+OLS:chebi|CONFIRMED|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-073160b3ef6634f7
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1797]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:26672","line":1797,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:26672","preferred_term":"Siderophore","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-26edea8c147379be
  kind: prior_review
  reference: reports/yaml_record_review/20261001T050321Z-Siderophore.md
  locator: 'YAML Record Review: Siderophore:2; Target:10; Validation:20; Identity
    and Grounding:27; Evidence:36; Completeness:46; Findings:52; Recommended Edits:56;
    Follow-up Checks:61; Additional Notes:67'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: e7aa920c2a24777ecdc8a179804f587151eee9ac5ee19bcbfef08e2c237ea421
  quote: 'Findings:

    - **major**: The previous finding set in `reports/yaml_record_review/Siderophore.md`
    was tied to the prior record content; carry it forward as an unresolved curation
    floor until a targeted current review retires it. Previous summary: The exact
    CHEBI:26672 identity passes, but final SSSOM exports a raw produces surface form
    and CHELATOR is only provisional ChEBI-ancestry inference.


    Recommended Edits:

    - Resolve or explicitly retire the findings provisionally carried forward from
    `reports/yaml_record_review/Siderophore.md`.

    - After any edit, run `just sync-curated`, `just validate-strict data/ingredients/mapped/Siderophore.yaml`,
    `just validate-terms data/ingredients/mapped/Siderophore.yaml` where applicable,
    and `just qc-sssom`.'
- evidence_id: ev-f4e9cdee8d71d0b7
  kind: prior_review
  reference: reports/yaml_record_review/Siderophore.md
  locator: '`data/ingredients/mapped/Siderophore.yaml`:2'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 44d9c010aea715409d2b039285a4087f35bcc1fe7750f458c76082a12f5490cd
- evidence_id: ev-23c2943cc6df7840
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1194,1474]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"cff4bd849c6a45c2034fed99f63f2773d5a482ec3cbb4fba8ce33c878bf860b8","finding_id":"SEM:7a17f3cbcbdfb4a61e0c","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"cff4bd849c6a45c2034fed99f63f2773d5a482ec3cbb4fba8ce33c878bf860b8","finding_id":"SEM:b74685e1c2b28bbfffa6","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-1a2380a49fe46490
  kind: record_content
  reference: data/ingredients/mapped/Siderophore.yaml
  locator: physicochemical_roles[0]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION:
    [{"field":"physicochemical_roles[0]","role":{"confidence":0.7,"evidence":[{"curator_note":"Provisional
    role inferred from CHEBI is_a/has_role closure; review recommended.","reference_text":"Inferred
    from CHEBI ancestry: subclass/has_role of CHEBI:38161 (chelator (role))","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"CHELATOR"}}]'
  snapshot_sha256: cff4bd849c6a45c2034fed99f63f2773d5a482ec3cbb4fba8ce33c878bf860b8
- evidence_id: ev-b2475dc99d758037
  kind: prior_review
  reference: reviews/structured/20261011T024638Z-mim-reconcile-all-batch-10/review.yaml
  locator: findings[finding_id=f-1d2159e3c902a1ca]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-1d2159e3c902a1ca in 20261011T024638Z-mim-reconcile-all-batch-10
  snapshot_sha256: 8c3aa2fca1269d1dbbf6117e85dea5b0de5047a8505841641245bd7ee99b936d
assessments:
- assessment_id: a-11b76e1141dfc231
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-264b6e7dc7f1d452
  evidence_ids:
  - ev-c8a7587fd79e6b00
  - ev-ef8843265f365165
  - ev-2c3d79e4444259da
  - ev-073160b3ef6634f7
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-a6f656c6df732aa3
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-264b6e7dc7f1d452
  evidence_ids:
  - ev-26edea8c147379be
  - ev-f4e9cdee8d71d0b7
  - ev-c8a7587fd79e6b00
  - ev-23c2943cc6df7840
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-10-01T05:03:21Z;
    reviewed SHA-256=cff4bd849c6a45c2034fed99f63f2773d5a482ec3cbb4fba8ce33c878bf860b8;
    current SHA-256=cff4bd849c6a45c2034fed99f63f2773d5a482ec3cbb4fba8ce33c878bf860b8;
    hash_changed=False. Reports=["reports/yaml_record_review/20261001T050321Z-Siderophore.md","reports/yaml_record_review/Siderophore.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: Refreshed
    `reports/yaml_record_review/Siderophore.md` after the record changed from bd1a1c002069e81d5c10478e4f5c1db7791a06766531ded5c9ecf1573df8a43a
    to cff4bd849c6a45c2034fed99f63f2773d5a482ec3cbb4fba8ce33c878bf860b8; preserved
    the previous major finding floor pending targeted retirement.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-26edea8c147379be
    - ev-f4e9cdee8d71d0b7
    - ev-c8a7587fd79e6b00
  - name: legacy-native-ids
    value: '["SEM:7a17f3cbcbdfb4a61e0c","SEM:b74685e1c2b28bbfffa6"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-c8a7587fd79e6b00
    - ev-26edea8c147379be
    - ev-f4e9cdee8d71d0b7
    - ev-23c2943cc6df7840
- assessment_id: a-1a2380a49fe46490
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-264b6e7dc7f1d452
  evidence_ids:
  - ev-26edea8c147379be
  - ev-f4e9cdee8d71d0b7
  - ev-1a2380a49fe46490
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-26edea8c147379be
    - ev-f4e9cdee8d71d0b7
    - ev-1a2380a49fe46490
findings:
- finding_id: rec-f-1d2159e3c902a1ca
  issue_key: mim-reconciliation-role-support-264b6e7dc7f1d452
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Siderophore'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-264b6e7dc7f1d452
  evidence_ids:
  - ev-26edea8c147379be
  - ev-f4e9cdee8d71d0b7
  - ev-1a2380a49fe46490
  - ev-b2475dc99d758037
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Siderophore.yaml
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
    finding_id: f-1d2159e3c902a1ca
actions:
- action_id: rec-action-1d2159e3c902a1ca
  description: 'Reassess prediction-only role support: Siderophore'
  finding_ids:
  - rec-f-1d2159e3c902a1ca
  target_ids:
  - record-264b6e7dc7f1d452
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Siderophore.yaml
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
