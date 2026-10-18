# Per-record structured review: Phenol (data/ingredients/mapped/Phenol.yaml)

- Review: 20261017T083000Z-phenol
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Phenol (data/ingredients/mapped/Phenol.yaml, record-445ad2adce29e3d8, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Phenol.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Phenol.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-445ad2adce29e3d8 | data/ingredients/mapped/Phenol.yaml | maintained | Phenol |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-445ad2adce29e3d8 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-445ad2adce29e3d8 | Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-445ad2adce29e3d8 | Reconciled against predecessor batch review 20261011T024638Z-mim-reconcile-all-batch-10 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-445ad2adce29e3d8.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-445ad2adce29e3d8.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T09:06:07Z; reviewed SHA-256=88331db9c69efce76716baa57f6a5a3952232fad09df9ea31d914f3fbf86e1ef; current SHA-256=88331db9c69efce76716baa57f6a5a3952232fad09df9ea31d914f3fbf86e1ef; hash_changed=False. Reports=["reports/yaml_record_review/Phenol.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI:15882 phenol identity and final synonyms pass, but CARBON_SOURCE is provisional.

### Historical provisional-role concern

evidence: concern. Targets: record-445ad2adce29e3d8.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-90afa817929478d2: Reassess prediction-only role support: Phenol

major / open / confirmed; issue key: mim-reconciliation-role-support-445ad2adce29e3d8.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-90afa817929478d2

Reassess prediction-only role support: Phenol

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-c8b1889a8fe42a66 | data/ingredients/mapped/Phenol.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1639],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:15882","line":1641,"mapping_status":"MAPPED","ontology_id":"CHEBI:15882","preferred_term":"Phenol"}],"identifier":"CHEBI:15882","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":7,"edge_count":7,"occurrences":7},"occurrence_statistics":{"media_count":7,"total_occurrences":7},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:15882","ontology_label":"phenol","ontology_source":"CHEBI"},"preferred_term":"Phenol","sssom_rows":[{"data_row":2234,"object_id":"CHEBI:15882","object_label":"phenol","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Phenol","synonym_count":12} |
| ev-49614111064698f4 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1639] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-6bb094867cc7871f | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Phenol; data-row positions=[2234] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":2234,"object_id":"CHEBI:15882","object_label":"phenol","other":"Benzenol&#124;Carbolsaeure&#124;Hydroxybenzene&#124;Karbolsaeure&#124;Oxybenzene&#124;PhOH&#124;Phenic acid&#124;Phenylic acid&#124;Phenylic alcohol&#124;acide carbolique&#124;acide phenique&#124;carbolic acid&#124;CAS:108-95-2","predicate_id":"skos:exactMatch","subject_id":"MIM:Phenol","validation_method":"OAK+OLS:chebi&#124;CONFIRMED&#124;2026-07-07"}] |
| ev-be39f84bcb6e4d54 | docs/data/mapped_ingredients.csv; CSV lines=[1641] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:15882","line":1641,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"7","ontology_id":"CHEBI:15882","preferred_term":"Phenol","total_occurrences":"7"}] |
| ev-ad90705ed9e72314 | reports/yaml_record_review/Phenol.md; &#96;data/ingredients/mapped/Phenol.yaml&#96;:2; Verdict:4; Identity:10; Validation:19; Evidence:30; Completeness:40; Recommended Edits:46 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-33ace67dd5e203fd | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1102,2018] | context_only | [{"current_record_sha256":"88331db9c69efce76716baa57f6a5a3952232fad09df9ea31d914f3fbf86e1ef","finding_id":"SEM:6891a3cfccac1b8d5b7d","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"88331db9c69efce76716baa57f6a5a3952232fad09df9ea31d914f3fbf86e1ef","finding_id":"SEM:9e426d4d649b9305cd8f","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-609de1e528cc2773 | data/ingredients/mapped/Phenol.yaml; nutritional_roles[0] | supports | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1639],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:15882","line":1641,"mapping_status":"MAPPED","ontology_id":"CHEBI:15882","preferred_term":"Phenol"}],"identifier":"CHEBI:15882","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":7,"edge_count":7,"occurrences":7},"occurrence_statistics":{"media_count":7,"total_occurrences":7},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:15882","ontology_label":"phenol","ontology_source":"CHEBI"},"preferred_term":"Phenol","sssom_rows":[{"data_row":2234,"object_id":"CHEBI:15882","object_label":"phenol","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Phenol","synonym_count":12} |
| ev-484640c10b4de8a3 | reviews/structured/20261011T024638Z-mim-reconcile-all-batch-10/review.yaml; findings[finding_id=f-90afa817929478d2] | context_only | Predecessor structured review finding f-90afa817929478d2 in 20261011T024638Z-mim-reconcile-all-batch-10 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024638Z-mim-reconcile-all-batch-10.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-phenol
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Phenol (data/ingredients/mapped/Phenol.yaml)'
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
summary: Per-record structured review for Phenol (data/ingredients/mapped/Phenol.yaml,
  record-445ad2adce29e3d8, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Phenol.yaml
    sha256: 88331db9c69efce76716baa57f6a5a3952232fad09df9ea31d914f3fbf86e1ef
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
  - path: reports/yaml_record_review/Phenol.md
    sha256: 2bf6f0174ccb1e0a613c45a7549e46ca22e79b6c21291e7ac28c94405145e733
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-445ad2adce29e3d8
  path: data/ingredients/mapped/Phenol.yaml
  label: Phenol
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Phenol.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Phenol.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Phenol.yaml selected from full-corpus
    review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-445ad2adce29e3d8
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-445ad2adce29e3d8
  evidence_ids:
  - ev-c8b1889a8fe42a66
  - ev-49614111064698f4
  - ev-6bb094867cc7871f
  - ev-be39f84bcb6e4d54
  - ev-609de1e528cc2773
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-445ad2adce29e3d8
  evidence_ids:
  - ev-c8b1889a8fe42a66
  - ev-33ace67dd5e203fd
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024638Z-mim-reconcile-all-batch-10
    and semantic review dispositions on HEAD.
  target_ids:
  - record-445ad2adce29e3d8
  evidence_ids:
  - ev-ad90705ed9e72314
  - ev-33ace67dd5e203fd
  - ev-484640c10b4de8a3
evidence:
- evidence_id: ev-c8b1889a8fe42a66
  kind: record_content
  reference: data/ingredients/mapped/Phenol.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1639],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:15882","line":1641,"mapping_status":"MAPPED","ontology_id":"CHEBI:15882","preferred_term":"Phenol"}],"identifier":"CHEBI:15882","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":7,"edge_count":7,"occurrences":7},"occurrence_statistics":{"media_count":7,"total_occurrences":7},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:15882","ontology_label":"phenol","ontology_source":"CHEBI"},"preferred_term":"Phenol","sssom_rows":[{"data_row":2234,"object_id":"CHEBI:15882","object_label":"phenol","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Phenol","synonym_count":12}'
  snapshot_sha256: 88331db9c69efce76716baa57f6a5a3952232fad09df9ea31d914f3fbf86e1ef
- evidence_id: ev-49614111064698f4
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1639]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-6bb094867cc7871f
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Phenol; data-row positions=[2234]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":2234,"object_id":"CHEBI:15882","object_label":"phenol","other":"Benzenol|Carbolsaeure|Hydroxybenzene|Karbolsaeure|Oxybenzene|PhOH|Phenic
    acid|Phenylic acid|Phenylic alcohol|acide carbolique|acide phenique|carbolic acid|CAS:108-95-2","predicate_id":"skos:exactMatch","subject_id":"MIM:Phenol","validation_method":"OAK+OLS:chebi|CONFIRMED|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-be39f84bcb6e4d54
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1641]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:15882","line":1641,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"7","ontology_id":"CHEBI:15882","preferred_term":"Phenol","total_occurrences":"7"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-ad90705ed9e72314
  kind: prior_review
  reference: reports/yaml_record_review/Phenol.md
  locator: '`data/ingredients/mapped/Phenol.yaml`:2; Verdict:4; Identity:10; Validation:19;
    Evidence:30; Completeness:40; Recommended Edits:46'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 2bf6f0174ccb1e0a613c45a7549e46ca22e79b6c21291e7ac28c94405145e733
  quote: "Recommended Edits:\n- Major: in `data/ingredients/mapped/Phenol.yaml`, either\
    \ replace\n  `nutritional_roles.CARBON_SOURCE` with cited source evidence that\
    \ supports\n  the carbon-source role for phenol, or remove the provisional role\
    \ facet until\n  source-backed role evidence is curated."
- evidence_id: ev-33ace67dd5e203fd
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1102,2018]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"88331db9c69efce76716baa57f6a5a3952232fad09df9ea31d914f3fbf86e1ef","finding_id":"SEM:6891a3cfccac1b8d5b7d","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"88331db9c69efce76716baa57f6a5a3952232fad09df9ea31d914f3fbf86e1ef","finding_id":"SEM:9e426d4d649b9305cd8f","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-609de1e528cc2773
  kind: record_content
  reference: data/ingredients/mapped/Phenol.yaml
  locator: nutritional_roles[0]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1639],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:15882","line":1641,"mapping_status":"MAPPED","ontology_id":"CHEBI:15882","preferred_term":"Phenol"}],"identifier":"CHEBI:15882","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":7,"edge_count":7,"occurrences":7},"occurrence_statistics":{"media_count":7,"total_occurrences":7},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:15882","ontology_label":"phenol","ontology_source":"CHEBI"},"preferred_term":"Phenol","sssom_rows":[{"data_row":2234,"object_id":"CHEBI:15882","object_label":"phenol","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Phenol","synonym_count":12}'
  snapshot_sha256: 88331db9c69efce76716baa57f6a5a3952232fad09df9ea31d914f3fbf86e1ef
- evidence_id: ev-484640c10b4de8a3
  kind: prior_review
  reference: reviews/structured/20261011T024638Z-mim-reconcile-all-batch-10/review.yaml
  locator: findings[finding_id=f-90afa817929478d2]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-90afa817929478d2 in 20261011T024638Z-mim-reconcile-all-batch-10
  snapshot_sha256: 8c3aa2fca1269d1dbbf6117e85dea5b0de5047a8505841641245bd7ee99b936d
assessments:
- assessment_id: a-cef641f670d39114
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-445ad2adce29e3d8
  evidence_ids:
  - ev-c8b1889a8fe42a66
  - ev-49614111064698f4
  - ev-6bb094867cc7871f
  - ev-be39f84bcb6e4d54
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-ba9caecabaa58288
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-445ad2adce29e3d8
  evidence_ids:
  - ev-ad90705ed9e72314
  - ev-c8b1889a8fe42a66
  - ev-33ace67dd5e203fd
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T09:06:07Z;
    reviewed SHA-256=88331db9c69efce76716baa57f6a5a3952232fad09df9ea31d914f3fbf86e1ef;
    current SHA-256=88331db9c69efce76716baa57f6a5a3952232fad09df9ea31d914f3fbf86e1ef;
    hash_changed=False. Reports=["reports/yaml_record_review/Phenol.md"]. Full reports,
    including older originals behind refresh floors, are hashed inputs. Repeated refresh
    allegations are not counted as new defects. The narrative group is not a count
    of distinct scientific findings. Latest manifest note: The exact CHEBI:15882 phenol
    identity and final synonyms pass, but CARBON_SOURCE is provisional.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-ad90705ed9e72314
    - ev-c8b1889a8fe42a66
  - name: legacy-native-ids
    value: '["SEM:6891a3cfccac1b8d5b7d","SEM:9e426d4d649b9305cd8f"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-c8b1889a8fe42a66
    - ev-ad90705ed9e72314
    - ev-33ace67dd5e203fd
- assessment_id: a-609de1e528cc2773
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-445ad2adce29e3d8
  evidence_ids:
  - ev-ad90705ed9e72314
  - ev-609de1e528cc2773
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-ad90705ed9e72314
    - ev-609de1e528cc2773
findings:
- finding_id: rec-f-90afa817929478d2
  issue_key: mim-reconciliation-role-support-445ad2adce29e3d8
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Phenol'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-445ad2adce29e3d8
  evidence_ids:
  - ev-ad90705ed9e72314
  - ev-609de1e528cc2773
  - ev-484640c10b4de8a3
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Phenol.yaml
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
    review_id: 20261011T024638Z-mim-reconcile-all-batch-10
    finding_id: f-90afa817929478d2
actions:
- action_id: rec-action-90afa817929478d2
  description: 'Reassess prediction-only role support: Phenol'
  finding_ids:
  - rec-f-90afa817929478d2
  target_ids:
  - record-445ad2adce29e3d8
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Phenol.yaml
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
