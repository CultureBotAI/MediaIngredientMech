# Per-record structured review: P-hydroxybenzoate (data/ingredients/mapped/P-hydroxybenzoate.yaml)

- Review: 20261017T083000Z-p-hydroxybenzoate
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for P-hydroxybenzoate (data/ingredients/mapped/P-hydroxybenzoate.yaml, record-d895aeed1a5a11ee, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/P-hydroxybenzoate.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/P-hydroxybenzoate.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-d895aeed1a5a11ee | data/ingredients/mapped/P-hydroxybenzoate.yaml | maintained | P-hydroxybenzoate |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-d895aeed1a5a11ee | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-d895aeed1a5a11ee | Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-d895aeed1a5a11ee | Reconciled against predecessor batch review 20261011T024637Z-mim-reconcile-all-batch-09 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-d895aeed1a5a11ee.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-d895aeed1a5a11ee.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T08:05:42Z; reviewed SHA-256=a5f785e7184586ae4885404a4e2ebe55f659611eb01f70edc35a6a6093149a73; current SHA-256=a5f785e7184586ae4885404a4e2ebe55f659611eb01f70edc35a6a6093149a73; hash_changed=False. Reports=["reports/yaml_record_review/P-hydroxybenzoate.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The CHEBI:17879 4-hydroxybenzoate identity passes, but CARBON_SOURCE is only provisional.

### Historical provisional-role concern

evidence: concern. Targets: record-d895aeed1a5a11ee.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-ab273bc3288a2ec1: Reassess prediction-only role support: p-Hydroxybenzoate

major / open / confirmed; issue key: mim-reconciliation-role-support-d895aeed1a5a11ee.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-ab273bc3288a2ec1

Reassess prediction-only role support: p-Hydroxybenzoate

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-d6b92e6a43da464a | data/ingredients/mapped/P-hydroxybenzoate.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1603],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:17879","line":1605,"mapping_status":"MAPPED","ontology_id":"CHEBI:17879","preferred_term":"p-Hydroxybenzoate"}],"identifier":"CHEBI:17879","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":6,"edge_count":6,"occurrences":6},"occurrence_statistics":{"media_count":6,"total_occurrences":6},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:17879","ontology_label":"4-hydroxybenzoate","ontology_source":"CHEBI"},"preferred_term":"p-Hydroxybenzoate","sssom_rows":[{"data_row":2165,"object_id":"CHEBI:17879","object_label":"4-hydroxybenzoate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:P-hydroxybenzoate","synonym_count":1} |
| ev-32349fc026276066 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1603] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-4ef2e1a63bda33cc | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:P-hydroxybenzoate; data-row positions=[2165] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":2165,"object_id":"CHEBI:17879","object_label":"4-hydroxybenzoate","other":"CAS:456-23-5","predicate_id":"skos:exactMatch","subject_id":"MIM:P-hydroxybenzoate","validation_method":"OAK+OLS:chebi&#124;CONFIRMED&#124;2026-07-07"}] |
| ev-58e61b4fdc09c04d | docs/data/mapped_ingredients.csv; CSV lines=[1605] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:17879","line":1605,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"6","ontology_id":"CHEBI:17879","preferred_term":"p-Hydroxybenzoate","total_occurrences":"6"}] |
| ev-d34dbb73453abc12 | reports/yaml_record_review/P-hydroxybenzoate.md; &#96;data/ingredients/mapped/P-hydroxybenzoate.yaml&#96;:2; Verdict:4; Identity:10; Validation:19; Evidence:28; Completeness:41; Recommended Edits:46 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-bb55ca5292543e51 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1085,1890] | context_only | [{"current_record_sha256":"a5f785e7184586ae4885404a4e2ebe55f659611eb01f70edc35a6a6093149a73","finding_id":"SEM:5127936f3252ed404d7b","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"a5f785e7184586ae4885404a4e2ebe55f659611eb01f70edc35a6a6093149a73","finding_id":"SEM:317bca3e681ca061ecfe","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-2f9f4207ed1a9661 | data/ingredients/mapped/P-hydroxybenzoate.yaml; nutritional_roles[0] | supports | Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION: [{"field":"nutritional_roles[0]","role":{"confidence":0.6,"evidence":[{"curator_note":"Provisional in-session LLM role assignment; review recommended.","reference_text":"Assigned by in-session Claude reasoning (no external API)","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"CARBON_SOURCE"}}] |
| ev-d699051797ee7bbf | reviews/structured/20261011T024637Z-mim-reconcile-all-batch-09/review.yaml; findings[finding_id=f-ab273bc3288a2ec1] | context_only | Predecessor structured review finding f-ab273bc3288a2ec1 in 20261011T024637Z-mim-reconcile-all-batch-09 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024637Z-mim-reconcile-all-batch-09.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-p-hydroxybenzoate
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: P-hydroxybenzoate (data/ingredients/mapped/P-hydroxybenzoate.yaml)'
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
summary: Per-record structured review for P-hydroxybenzoate (data/ingredients/mapped/P-hydroxybenzoate.yaml,
  record-d895aeed1a5a11ee, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/P-hydroxybenzoate.yaml
    sha256: a5f785e7184586ae4885404a4e2ebe55f659611eb01f70edc35a6a6093149a73
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
  - path: reports/yaml_record_review/P-hydroxybenzoate.md
    sha256: a73af9d36f0a37e55a8718ebeba998bbd9a6e16c472f20a80e2665d7140889e5
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-d895aeed1a5a11ee
  path: data/ingredients/mapped/P-hydroxybenzoate.yaml
  label: P-hydroxybenzoate
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/P-hydroxybenzoate.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/P-hydroxybenzoate.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/P-hydroxybenzoate.yaml selected
    from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-d895aeed1a5a11ee
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-d895aeed1a5a11ee
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-d895aeed1a5a11ee
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024637Z-mim-reconcile-all-batch-09
    and semantic review dispositions on HEAD.
  target_ids:
  - record-d895aeed1a5a11ee
evidence:
- evidence_id: ev-d6b92e6a43da464a
  kind: record_content
  reference: data/ingredients/mapped/P-hydroxybenzoate.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1603],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:17879","line":1605,"mapping_status":"MAPPED","ontology_id":"CHEBI:17879","preferred_term":"p-Hydroxybenzoate"}],"identifier":"CHEBI:17879","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":6,"edge_count":6,"occurrences":6},"occurrence_statistics":{"media_count":6,"total_occurrences":6},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:17879","ontology_label":"4-hydroxybenzoate","ontology_source":"CHEBI"},"preferred_term":"p-Hydroxybenzoate","sssom_rows":[{"data_row":2165,"object_id":"CHEBI:17879","object_label":"4-hydroxybenzoate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:P-hydroxybenzoate","synonym_count":1}'
  snapshot_sha256: a5f785e7184586ae4885404a4e2ebe55f659611eb01f70edc35a6a6093149a73
- evidence_id: ev-32349fc026276066
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1603]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-4ef2e1a63bda33cc
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:P-hydroxybenzoate; data-row positions=[2165]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":2165,"object_id":"CHEBI:17879","object_label":"4-hydroxybenzoate","other":"CAS:456-23-5","predicate_id":"skos:exactMatch","subject_id":"MIM:P-hydroxybenzoate","validation_method":"OAK+OLS:chebi|CONFIRMED|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-58e61b4fdc09c04d
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1605]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:17879","line":1605,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"6","ontology_id":"CHEBI:17879","preferred_term":"p-Hydroxybenzoate","total_occurrences":"6"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-d34dbb73453abc12
  kind: prior_review
  reference: reports/yaml_record_review/P-hydroxybenzoate.md
  locator: '`data/ingredients/mapped/P-hydroxybenzoate.yaml`:2; Verdict:4; Identity:10;
    Validation:19; Evidence:28; Completeness:41; Recommended Edits:46'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: a73af9d36f0a37e55a8718ebeba998bbd9a6e16c472f20a80e2665d7140889e5
  quote: "Recommended Edits:\n- Major: in `data/ingredients/mapped/P-hydroxybenzoate.yaml`,\
    \ either replace\n  `nutritional_roles.CARBON_SOURCE` with cited experimental\
    \ or recipe evidence,\n  or remove the provisional role facet until source-backed\
    \ role evidence is\n  curated."
- evidence_id: ev-bb55ca5292543e51
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1085,1890]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"a5f785e7184586ae4885404a4e2ebe55f659611eb01f70edc35a6a6093149a73","finding_id":"SEM:5127936f3252ed404d7b","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"a5f785e7184586ae4885404a4e2ebe55f659611eb01f70edc35a6a6093149a73","finding_id":"SEM:317bca3e681ca061ecfe","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-2f9f4207ed1a9661
  kind: record_content
  reference: data/ingredients/mapped/P-hydroxybenzoate.yaml
  locator: nutritional_roles[0]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION:
    [{"field":"nutritional_roles[0]","role":{"confidence":0.6,"evidence":[{"curator_note":"Provisional
    in-session LLM role assignment; review recommended.","reference_text":"Assigned
    by in-session Claude reasoning (no external API)","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"CARBON_SOURCE"}}]'
  snapshot_sha256: a5f785e7184586ae4885404a4e2ebe55f659611eb01f70edc35a6a6093149a73
- evidence_id: ev-d699051797ee7bbf
  kind: prior_review
  reference: reviews/structured/20261011T024637Z-mim-reconcile-all-batch-09/review.yaml
  locator: findings[finding_id=f-ab273bc3288a2ec1]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-ab273bc3288a2ec1 in 20261011T024637Z-mim-reconcile-all-batch-09
  snapshot_sha256: cf46750874f1303863883723934bbe8b09ece8d62b1785ceab64bb0342a3cf11
assessments:
- assessment_id: a-fbe761d880ea3929
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-d895aeed1a5a11ee
  evidence_ids:
  - ev-d6b92e6a43da464a
  - ev-32349fc026276066
  - ev-4ef2e1a63bda33cc
  - ev-58e61b4fdc09c04d
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-96dbfb9a098a67bf
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-d895aeed1a5a11ee
  evidence_ids:
  - ev-d34dbb73453abc12
  - ev-d6b92e6a43da464a
  - ev-bb55ca5292543e51
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T08:05:42Z;
    reviewed SHA-256=a5f785e7184586ae4885404a4e2ebe55f659611eb01f70edc35a6a6093149a73;
    current SHA-256=a5f785e7184586ae4885404a4e2ebe55f659611eb01f70edc35a6a6093149a73;
    hash_changed=False. Reports=["reports/yaml_record_review/P-hydroxybenzoate.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The CHEBI:17879
    4-hydroxybenzoate identity passes, but CARBON_SOURCE is only provisional.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-d34dbb73453abc12
    - ev-d6b92e6a43da464a
  - name: legacy-native-ids
    value: '["SEM:5127936f3252ed404d7b","SEM:317bca3e681ca061ecfe"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-d6b92e6a43da464a
    - ev-d34dbb73453abc12
    - ev-bb55ca5292543e51
- assessment_id: a-2f9f4207ed1a9661
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-d895aeed1a5a11ee
  evidence_ids:
  - ev-d34dbb73453abc12
  - ev-2f9f4207ed1a9661
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-d34dbb73453abc12
    - ev-2f9f4207ed1a9661
findings:
- finding_id: rec-f-ab273bc3288a2ec1
  issue_key: mim-reconciliation-role-support-d895aeed1a5a11ee
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: p-Hydroxybenzoate'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-d895aeed1a5a11ee
  evidence_ids:
  - ev-d34dbb73453abc12
  - ev-2f9f4207ed1a9661
  - ev-d699051797ee7bbf
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/P-hydroxybenzoate.yaml
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
    review_id: 20261011T024637Z-mim-reconcile-all-batch-09
    finding_id: f-ab273bc3288a2ec1
actions:
- action_id: rec-action-ab273bc3288a2ec1
  description: 'Reassess prediction-only role support: p-Hydroxybenzoate'
  finding_ids:
  - rec-f-ab273bc3288a2ec1
  target_ids:
  - record-d895aeed1a5a11ee
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/P-hydroxybenzoate.yaml
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
