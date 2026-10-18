# Per-record structured review: Glycerol_Mono-oleate (data/ingredients/mapped/Glycerol_Mono-oleate.yaml)

- Review: 20261017T083000Z-glycerol-mono-oleate
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Glycerol_Mono-oleate (data/ingredients/mapped/Glycerol_Mono-oleate.yaml, record-13a57002e46ca2a8, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Glycerol_Mono-oleate.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Glycerol_Mono-oleate.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-13a57002e46ca2a8 | data/ingredients/mapped/Glycerol_Mono-oleate.yaml | maintained | Glycerol_Mono-oleate |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-13a57002e46ca2a8 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-13a57002e46ca2a8 | Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-13a57002e46ca2a8 | Reconciled against predecessor batch review 20261011T024634Z-mim-reconcile-all-batch-06 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-13a57002e46ca2a8.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-13a57002e46ca2a8.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T18:16:29Z; reviewed SHA-256=5f0ffcba2d2cd18e6e874b0e9e414398b734b95fff4f9013d1ad9dac67de2d7e; current SHA-256=5f0ffcba2d2cd18e6e874b0e9e414398b734b95fff4f9013d1ad9dac67de2d7e; hash_changed=False. Reports=["reports/yaml_record_review/Glycerol_Mono-oleate.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact monooleoylglycerol identity and final SSSOM row pass, but SURFACTANT is computational.

### Historical provisional-role concern

evidence: concern. Targets: record-13a57002e46ca2a8.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-f5f6680da0f8ddd4: Reassess prediction-only role support: Glycerol mono-oleate

major / open / confirmed; issue key: mim-reconciliation-role-support-13a57002e46ca2a8.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-f5f6680da0f8ddd4

Reassess prediction-only role support: Glycerol mono-oleate

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-f372f84f2f7f5844 | data/ingredients/mapped/Glycerol_Mono-oleate.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1071],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:75937","line":1073,"mapping_status":"MAPPED","ontology_id":"CHEBI:75937","preferred_term":"Glycerol mono-oleate"}],"identifier":"CHEBI:75937","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":3,"edge_count":3,"occurrences":3},"occurrence_statistics":{"media_count":3,"total_occurrences":3},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:75937","ontology_label":"monooleoylglycerol","ontology_source":"CHEBI"},"preferred_term":"Glycerol mono-oleate","sssom_rows":[{"data_row":1336,"object_id":"CHEBI:75937","object_label":"monooleoylglycerol","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Glycerol_Mono-oleate","synonym_count":5} |
| ev-8eaca4e3e95bd0fd | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1071] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-e9d1157dbe23f342 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Glycerol_Mono-oleate; data-row positions=[1336] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1336,"object_id":"CHEBI:75937","object_label":"monooleoylglycerol","other":"(9Z-octadecenoyl)-glycerol&#124;MG[18:1(omega-9)]&#124;mono-(9Z)-octadecenoylglycerol&#124;oleoylglycerol&#124;CAS:129784-87-8","predicate_id":"skos:exactMatch","subject_id":"MIM:Glycerol_Mono-oleate","validation_method":"OAK+OLS:chebi&#124;SYNONYM_ENRICH&#124;2026-07-07"}] |
| ev-e955060a19a84773 | docs/data/mapped_ingredients.csv; CSV lines=[1073] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:75937","line":1073,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"3","ontology_id":"CHEBI:75937","preferred_term":"Glycerol mono-oleate","total_occurrences":"3"}] |
| ev-6de15f7578a80b19 | reports/yaml_record_review/Glycerol_Mono-oleate.md; &#96;data/ingredients/mapped/Glycerol_Mono-oleate.yaml&#96;:2; Verdict:4; Identity:11; Validation:21; Evidence:28; Completeness:50; Recommended Edits:56 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-9bbbd5f079e0aed6 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[689,1860] | context_only | [{"current_record_sha256":"5f0ffcba2d2cd18e6e874b0e9e414398b734b95fff4f9013d1ad9dac67de2d7e","finding_id":"SEM:f8328ef1f915d2d62828","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"5f0ffcba2d2cd18e6e874b0e9e414398b734b95fff4f9013d1ad9dac67de2d7e","finding_id":"SEM:83e9d62dd2d4313461f4","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-5bfebf033d0ca519 | data/ingredients/mapped/Glycerol_Mono-oleate.yaml; physicochemical_roles[0] | supports | Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION: [{"field":"physicochemical_roles[0]","role":{"confidence":0.6,"evidence":[{"curator_note":"Provisional in-session LLM role assignment; review recommended.","reference_text":"Assigned by in-session Claude reasoning (no external API)","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"SURFACTANT"}}] |
| ev-369875dd1ecdfab1 | reviews/structured/20261011T024634Z-mim-reconcile-all-batch-06/review.yaml; findings[finding_id=f-f5f6680da0f8ddd4] | context_only | Predecessor structured review finding f-f5f6680da0f8ddd4 in 20261011T024634Z-mim-reconcile-all-batch-06 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024634Z-mim-reconcile-all-batch-06.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-glycerol-mono-oleate
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Glycerol_Mono-oleate (data/ingredients/mapped/Glycerol_Mono-oleate.yaml)'
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
summary: Per-record structured review for Glycerol_Mono-oleate (data/ingredients/mapped/Glycerol_Mono-oleate.yaml,
  record-13a57002e46ca2a8, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Glycerol_Mono-oleate.yaml
    sha256: 5f0ffcba2d2cd18e6e874b0e9e414398b734b95fff4f9013d1ad9dac67de2d7e
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
  - path: reports/yaml_record_review/Glycerol_Mono-oleate.md
    sha256: cb166d00031c902ebdeb7ee720b7b1d9c77186a42bc2ffcda78b5ed6f933fadc
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-13a57002e46ca2a8
  path: data/ingredients/mapped/Glycerol_Mono-oleate.yaml
  label: Glycerol_Mono-oleate
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Glycerol_Mono-oleate.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Glycerol_Mono-oleate.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Glycerol_Mono-oleate.yaml selected
    from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-13a57002e46ca2a8
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-13a57002e46ca2a8
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-13a57002e46ca2a8
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024634Z-mim-reconcile-all-batch-06
    and semantic review dispositions on HEAD.
  target_ids:
  - record-13a57002e46ca2a8
evidence:
- evidence_id: ev-f372f84f2f7f5844
  kind: record_content
  reference: data/ingredients/mapped/Glycerol_Mono-oleate.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1071],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:75937","line":1073,"mapping_status":"MAPPED","ontology_id":"CHEBI:75937","preferred_term":"Glycerol
    mono-oleate"}],"identifier":"CHEBI:75937","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":3,"edge_count":3,"occurrences":3},"occurrence_statistics":{"media_count":3,"total_occurrences":3},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:75937","ontology_label":"monooleoylglycerol","ontology_source":"CHEBI"},"preferred_term":"Glycerol
    mono-oleate","sssom_rows":[{"data_row":1336,"object_id":"CHEBI:75937","object_label":"monooleoylglycerol","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Glycerol_Mono-oleate","synonym_count":5}'
  snapshot_sha256: 5f0ffcba2d2cd18e6e874b0e9e414398b734b95fff4f9013d1ad9dac67de2d7e
- evidence_id: ev-8eaca4e3e95bd0fd
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1071]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-e9d1157dbe23f342
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Glycerol_Mono-oleate; data-row positions=[1336]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1336,"object_id":"CHEBI:75937","object_label":"monooleoylglycerol","other":"(9Z-octadecenoyl)-glycerol|MG[18:1(omega-9)]|mono-(9Z)-octadecenoylglycerol|oleoylglycerol|CAS:129784-87-8","predicate_id":"skos:exactMatch","subject_id":"MIM:Glycerol_Mono-oleate","validation_method":"OAK+OLS:chebi|SYNONYM_ENRICH|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-e955060a19a84773
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1073]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:75937","line":1073,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"3","ontology_id":"CHEBI:75937","preferred_term":"Glycerol
    mono-oleate","total_occurrences":"3"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-6de15f7578a80b19
  kind: prior_review
  reference: reports/yaml_record_review/Glycerol_Mono-oleate.md
  locator: '`data/ingredients/mapped/Glycerol_Mono-oleate.yaml`:2; Verdict:4; Identity:11;
    Validation:21; Evidence:28; Completeness:50; Recommended Edits:56'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: cb166d00031c902ebdeb7ee720b7b1d9c77186a42bc2ffcda78b5ed6f933fadc
  quote: "Recommended Edits:\n- Major: remove `physicochemical_roles.SURFACTANT` from\n\
    \  `data/ingredients/mapped/Glycerol_Mono-oleate.yaml`, or replace its\n  provisional\
    \ computational evidence with inspected source evidence that\n  specifically supports\
    \ glycerol mono-oleate functioning as a surfactant in\n  this medium-ingredient\
    \ context."
- evidence_id: ev-9bbbd5f079e0aed6
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[689,1860]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"5f0ffcba2d2cd18e6e874b0e9e414398b734b95fff4f9013d1ad9dac67de2d7e","finding_id":"SEM:f8328ef1f915d2d62828","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"5f0ffcba2d2cd18e6e874b0e9e414398b734b95fff4f9013d1ad9dac67de2d7e","finding_id":"SEM:83e9d62dd2d4313461f4","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-5bfebf033d0ca519
  kind: record_content
  reference: data/ingredients/mapped/Glycerol_Mono-oleate.yaml
  locator: physicochemical_roles[0]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION:
    [{"field":"physicochemical_roles[0]","role":{"confidence":0.6,"evidence":[{"curator_note":"Provisional
    in-session LLM role assignment; review recommended.","reference_text":"Assigned
    by in-session Claude reasoning (no external API)","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"SURFACTANT"}}]'
  snapshot_sha256: 5f0ffcba2d2cd18e6e874b0e9e414398b734b95fff4f9013d1ad9dac67de2d7e
- evidence_id: ev-369875dd1ecdfab1
  kind: prior_review
  reference: reviews/structured/20261011T024634Z-mim-reconcile-all-batch-06/review.yaml
  locator: findings[finding_id=f-f5f6680da0f8ddd4]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-f5f6680da0f8ddd4 in 20261011T024634Z-mim-reconcile-all-batch-06
  snapshot_sha256: 14c3200be95fdc87fca16bb71628432f3c9aaf8a65356ed494efc776ebe8aa11
assessments:
- assessment_id: a-8559d68314865073
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-13a57002e46ca2a8
  evidence_ids:
  - ev-f372f84f2f7f5844
  - ev-8eaca4e3e95bd0fd
  - ev-e9d1157dbe23f342
  - ev-e955060a19a84773
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-90a59c9ab4ceab53
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-13a57002e46ca2a8
  evidence_ids:
  - ev-6de15f7578a80b19
  - ev-f372f84f2f7f5844
  - ev-9bbbd5f079e0aed6
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T18:16:29Z;
    reviewed SHA-256=5f0ffcba2d2cd18e6e874b0e9e414398b734b95fff4f9013d1ad9dac67de2d7e;
    current SHA-256=5f0ffcba2d2cd18e6e874b0e9e414398b734b95fff4f9013d1ad9dac67de2d7e;
    hash_changed=False. Reports=["reports/yaml_record_review/Glycerol_Mono-oleate.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The exact
    monooleoylglycerol identity and final SSSOM row pass, but SURFACTANT is computational.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-6de15f7578a80b19
    - ev-f372f84f2f7f5844
  - name: legacy-native-ids
    value: '["SEM:f8328ef1f915d2d62828","SEM:83e9d62dd2d4313461f4"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-f372f84f2f7f5844
    - ev-6de15f7578a80b19
    - ev-9bbbd5f079e0aed6
- assessment_id: a-5bfebf033d0ca519
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-13a57002e46ca2a8
  evidence_ids:
  - ev-6de15f7578a80b19
  - ev-5bfebf033d0ca519
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-6de15f7578a80b19
    - ev-5bfebf033d0ca519
findings:
- finding_id: rec-f-f5f6680da0f8ddd4
  issue_key: mim-reconciliation-role-support-13a57002e46ca2a8
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Glycerol mono-oleate'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-13a57002e46ca2a8
  evidence_ids:
  - ev-6de15f7578a80b19
  - ev-5bfebf033d0ca519
  - ev-369875dd1ecdfab1
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Glycerol_Mono-oleate.yaml
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
    finding_id: f-f5f6680da0f8ddd4
actions:
- action_id: rec-action-f5f6680da0f8ddd4
  description: 'Reassess prediction-only role support: Glycerol mono-oleate'
  finding_ids:
  - rec-f-f5f6680da0f8ddd4
  target_ids:
  - record-13a57002e46ca2a8
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Glycerol_Mono-oleate.yaml
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
