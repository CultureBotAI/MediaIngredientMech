# Per-record structured review: Glebomycin (data/ingredients/mapped/Glebomycin.yaml)

- Review: 20261017T083000Z-glebomycin
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Glebomycin (data/ingredients/mapped/Glebomycin.yaml, record-ce7e7d8d3a8fcae8, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Glebomycin.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Glebomycin.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-ce7e7d8d3a8fcae8 | data/ingredients/mapped/Glebomycin.yaml | maintained | Glebomycin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-ce7e7d8d3a8fcae8 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-ce7e7d8d3a8fcae8 | Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-ce7e7d8d3a8fcae8 | Reconciled against predecessor batch review 20261011T024634Z-mim-reconcile-all-batch-06 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-ce7e7d8d3a8fcae8.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-ce7e7d8d3a8fcae8.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T17:41:23Z; reviewed SHA-256=f14ec57e02fe9731bb5318f0491635540564ec1e7d376d9509eb03ac4eeea1ed; current SHA-256=f14ec57e02fe9731bb5318f0491635540564ec1e7d376d9509eb03ac4eeea1ed; hash_changed=False. Reports=["reports/yaml_record_review/Glebomycin.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact NCIT synonym identity passes through external-prefix OLS validation, but SELECTIVE_AGENT is computational.

### Historical provisional-role concern

evidence: concern. Targets: record-ce7e7d8d3a8fcae8.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-c7719392ccc6798c: Reassess prediction-only role support: Glebomycin

major / open / confirmed; issue key: mim-reconciliation-role-support-ce7e7d8d3a8fcae8.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-c7719392ccc6798c

Reassess prediction-only role support: Glebomycin

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-1c6c06874dab2c90 | data/ingredients/mapped/Glebomycin.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1055],"raw_equal":true},"docs_rows":[{"identifier":"NCIT:C90636","line":1057,"mapping_status":"MAPPED","ontology_id":"NCIT:C90636","preferred_term":"Glebomycin"}],"identifier":"NCIT:C90636","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"NCIT:C90636","ontology_label":"Bluensomycin","ontology_source":"NCIT"},"preferred_term":"Glebomycin","sssom_rows":[{"data_row":1300,"object_id":"NCIT:C90636","object_label":"Bluensomycin","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Glebomycin","synonym_count":0} |
| ev-5964033693afdfae | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1055] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-606a029efc3bfe3f | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Glebomycin; data-row positions=[1300] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1300,"object_id":"NCIT:C90636","object_label":"Bluensomycin","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Glebomycin","validation_method":"none&#124;UNKNOWN_TERM&#124;2026-07-07"}] |
| ev-1d0fe5e27cc9ee6b | docs/data/mapped_ingredients.csv; CSV lines=[1057] | supports | Published identity and count rows inspected: [{"identifier":"NCIT:C90636","line":1057,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"NCIT:C90636","preferred_term":"Glebomycin","total_occurrences":"0"}] |
| ev-e81ae55417378a34 | reports/yaml_record_review/Glebomycin.md; &#96;data/ingredients/mapped/Glebomycin.yaml&#96;:2; Verdict:4; Identity:11; Validation:23; Evidence:35; Completeness:55; Recommended Edits:61 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-69ce5a509bede991 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[662,1464] | context_only | [{"current_record_sha256":"f14ec57e02fe9731bb5318f0491635540564ec1e7d376d9509eb03ac4eeea1ed","finding_id":"SEM:b37ae62735ee91b40c2c","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"f14ec57e02fe9731bb5318f0491635540564ec1e7d376d9509eb03ac4eeea1ed","finding_id":"SEM:7c1d85dae5be254b089c","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-fb6f0ccf46d50f13 | data/ingredients/mapped/Glebomycin.yaml; physicochemical_roles[0] | supports | Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION: [{"field":"physicochemical_roles[0]","role":{"confidence":0.8,"evidence":[{"curator_note":"Provisional role from a curated name-pattern rule; review recommended.","reference_text":"Inferred from curated media-role name pattern","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"SELECTIVE_AGENT"}}] |
| ev-6bb2f4e7302ce77d | reviews/structured/20261011T024634Z-mim-reconcile-all-batch-06/review.yaml; findings[finding_id=f-c7719392ccc6798c] | context_only | Predecessor structured review finding f-c7719392ccc6798c in 20261011T024634Z-mim-reconcile-all-batch-06 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024634Z-mim-reconcile-all-batch-06.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-glebomycin
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Glebomycin (data/ingredients/mapped/Glebomycin.yaml)'
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
summary: Per-record structured review for Glebomycin (data/ingredients/mapped/Glebomycin.yaml,
  record-ce7e7d8d3a8fcae8, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Glebomycin.yaml
    sha256: f14ec57e02fe9731bb5318f0491635540564ec1e7d376d9509eb03ac4eeea1ed
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
  - path: reports/yaml_record_review/Glebomycin.md
    sha256: 1e0f31606c3c02cbcb1d69c8cf460fc773363c0f48803443028c748e6fcb29d1
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-ce7e7d8d3a8fcae8
  path: data/ingredients/mapped/Glebomycin.yaml
  label: Glebomycin
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Glebomycin.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Glebomycin.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Glebomycin.yaml selected from full-corpus
    review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-ce7e7d8d3a8fcae8
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-ce7e7d8d3a8fcae8
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-ce7e7d8d3a8fcae8
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024634Z-mim-reconcile-all-batch-06
    and semantic review dispositions on HEAD.
  target_ids:
  - record-ce7e7d8d3a8fcae8
evidence:
- evidence_id: ev-1c6c06874dab2c90
  kind: record_content
  reference: data/ingredients/mapped/Glebomycin.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1055],"raw_equal":true},"docs_rows":[{"identifier":"NCIT:C90636","line":1057,"mapping_status":"MAPPED","ontology_id":"NCIT:C90636","preferred_term":"Glebomycin"}],"identifier":"NCIT:C90636","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"NCIT:C90636","ontology_label":"Bluensomycin","ontology_source":"NCIT"},"preferred_term":"Glebomycin","sssom_rows":[{"data_row":1300,"object_id":"NCIT:C90636","object_label":"Bluensomycin","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Glebomycin","synonym_count":0}'
  snapshot_sha256: f14ec57e02fe9731bb5318f0491635540564ec1e7d376d9509eb03ac4eeea1ed
- evidence_id: ev-5964033693afdfae
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1055]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-606a029efc3bfe3f
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Glebomycin; data-row positions=[1300]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1300,"object_id":"NCIT:C90636","object_label":"Bluensomycin","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Glebomycin","validation_method":"none|UNKNOWN_TERM|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-1d0fe5e27cc9ee6b
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1057]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"NCIT:C90636","line":1057,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"NCIT:C90636","preferred_term":"Glebomycin","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-e81ae55417378a34
  kind: prior_review
  reference: reports/yaml_record_review/Glebomycin.md
  locator: '`data/ingredients/mapped/Glebomycin.yaml`:2; Verdict:4; Identity:11; Validation:23;
    Evidence:35; Completeness:55; Recommended Edits:61'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 1e0f31606c3c02cbcb1d69c8cf460fc773363c0f48803443028c748e6fcb29d1
  quote: "Recommended Edits:\n- Major: replace `SELECTIVE_AGENT` with source-backed\
    \ evidence or remove the\n  role, then rerun strict validation."
- evidence_id: ev-69ce5a509bede991
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[662,1464]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"f14ec57e02fe9731bb5318f0491635540564ec1e7d376d9509eb03ac4eeea1ed","finding_id":"SEM:b37ae62735ee91b40c2c","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"f14ec57e02fe9731bb5318f0491635540564ec1e7d376d9509eb03ac4eeea1ed","finding_id":"SEM:7c1d85dae5be254b089c","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-fb6f0ccf46d50f13
  kind: record_content
  reference: data/ingredients/mapped/Glebomycin.yaml
  locator: physicochemical_roles[0]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION:
    [{"field":"physicochemical_roles[0]","role":{"confidence":0.8,"evidence":[{"curator_note":"Provisional
    role from a curated name-pattern rule; review recommended.","reference_text":"Inferred
    from curated media-role name pattern","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"SELECTIVE_AGENT"}}]'
  snapshot_sha256: f14ec57e02fe9731bb5318f0491635540564ec1e7d376d9509eb03ac4eeea1ed
- evidence_id: ev-6bb2f4e7302ce77d
  kind: prior_review
  reference: reviews/structured/20261011T024634Z-mim-reconcile-all-batch-06/review.yaml
  locator: findings[finding_id=f-c7719392ccc6798c]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-c7719392ccc6798c in 20261011T024634Z-mim-reconcile-all-batch-06
  snapshot_sha256: 14c3200be95fdc87fca16bb71628432f3c9aaf8a65356ed494efc776ebe8aa11
assessments:
- assessment_id: a-6c4fa0530f6b8f29
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-ce7e7d8d3a8fcae8
  evidence_ids:
  - ev-1c6c06874dab2c90
  - ev-5964033693afdfae
  - ev-606a029efc3bfe3f
  - ev-1d0fe5e27cc9ee6b
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-d98d09335f90dee6
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-ce7e7d8d3a8fcae8
  evidence_ids:
  - ev-e81ae55417378a34
  - ev-1c6c06874dab2c90
  - ev-69ce5a509bede991
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T17:41:23Z;
    reviewed SHA-256=f14ec57e02fe9731bb5318f0491635540564ec1e7d376d9509eb03ac4eeea1ed;
    current SHA-256=f14ec57e02fe9731bb5318f0491635540564ec1e7d376d9509eb03ac4eeea1ed;
    hash_changed=False. Reports=["reports/yaml_record_review/Glebomycin.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The exact NCIT
    synonym identity passes through external-prefix OLS validation, but SELECTIVE_AGENT
    is computational.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-e81ae55417378a34
    - ev-1c6c06874dab2c90
  - name: legacy-native-ids
    value: '["SEM:b37ae62735ee91b40c2c","SEM:7c1d85dae5be254b089c"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-1c6c06874dab2c90
    - ev-e81ae55417378a34
    - ev-69ce5a509bede991
- assessment_id: a-fb6f0ccf46d50f13
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-ce7e7d8d3a8fcae8
  evidence_ids:
  - ev-e81ae55417378a34
  - ev-fb6f0ccf46d50f13
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-e81ae55417378a34
    - ev-fb6f0ccf46d50f13
findings:
- finding_id: rec-f-c7719392ccc6798c
  issue_key: mim-reconciliation-role-support-ce7e7d8d3a8fcae8
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Glebomycin'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-ce7e7d8d3a8fcae8
  evidence_ids:
  - ev-e81ae55417378a34
  - ev-fb6f0ccf46d50f13
  - ev-6bb2f4e7302ce77d
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Glebomycin.yaml
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
    finding_id: f-c7719392ccc6798c
actions:
- action_id: rec-action-c7719392ccc6798c
  description: 'Reassess prediction-only role support: Glebomycin'
  finding_ids:
  - rec-f-c7719392ccc6798c
  target_ids:
  - record-ce7e7d8d3a8fcae8
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Glebomycin.yaml
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
