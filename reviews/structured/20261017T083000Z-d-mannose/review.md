# Per-record structured review: D-mannose (data/ingredients/mapped/D-mannose.yaml)

- Review: 20261017T083000Z-d-mannose
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for D-mannose (data/ingredients/mapped/D-mannose.yaml, record-044cb1610442ce97, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/D-mannose.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/D-mannose.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-044cb1610442ce97 | data/ingredients/mapped/D-mannose.yaml | maintained | D-mannose |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-044cb1610442ce97 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-044cb1610442ce97 | Role assertions on nutritional_roles[1] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-044cb1610442ce97 | Reconciled against predecessor batch review 20261011T024633Z-mim-reconcile-all-batch-05 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-044cb1610442ce97.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-044cb1610442ce97.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T13:49:05Z; reviewed SHA-256=7f5c5fb56cf889813b006e3465aabe62c41a5752f0c2297e4b63cb0f75c0f937; current SHA-256=7f5c5fb56cf889813b006e3465aabe62c41a5752f0c2297e4b63cb0f75c0f937; hash_changed=False. Reports=["reports/yaml_record_review/D-mannose.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI identity, 12/12 count, carbon role, CAS token, and final SSSOM synonym payload pass, but the energy role is computational.

### Historical provisional-role concern

evidence: concern. Targets: record-044cb1610442ce97.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-e57bb85767f1ca62: Reassess prediction-only role support: D-Mannose

major / open / confirmed; issue key: mim-reconciliation-role-support-044cb1610442ce97.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-e57bb85767f1ca62

Reassess prediction-only role support: D-Mannose

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-aed133cc6f86cc5b | data/ingredients/mapped/D-mannose.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[840],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:16024","line":842,"mapping_status":"MAPPED","ontology_id":"CHEBI:16024","preferred_term":"D-Mannose"}],"identifier":"CHEBI:16024","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":12,"edge_count":12,"occurrences":12},"occurrence_statistics":{"media_count":12,"total_occurrences":12},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:16024","ontology_label":"D-mannose","ontology_source":"CHEBI"},"preferred_term":"D-Mannose","sssom_rows":[{"data_row":948,"object_id":"CHEBI:16024","object_label":"D-mannose","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:D-mannose","synonym_count":3} |
| ev-0e6c3e337e7da83f | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [840] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-9eba5ecbe40a405b | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:D-mannose; data-row positions=[948] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":948,"object_id":"CHEBI:16024","object_label":"D-mannose","other":"D-manno-hexose&#124;CAS:530-26-7","predicate_id":"skos:exactMatch","subject_id":"MIM:D-mannose","validation_method":"OAK+OLS:chebi&#124;CONFIRMED&#124;2026-07-07"}] |
| ev-a8780f97038bd869 | docs/data/mapped_ingredients.csv; CSV lines=[842] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:16024","line":842,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"12","ontology_id":"CHEBI:16024","preferred_term":"D-Mannose","total_occurrences":"12"}] |
| ev-dd55fb9adb32feea | reports/yaml_record_review/D-mannose.md; &#96;data/ingredients/mapped/D-mannose.yaml&#96;:2; Verdict:4; Identity:11; Validation:23; Evidence:42; Completeness:60; Recommended Edits:69 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-2f0ad2a6ed1361b7 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[504,1972] | context_only | [{"current_record_sha256":"7f5c5fb56cf889813b006e3465aabe62c41a5752f0c2297e4b63cb0f75c0f937","finding_id":"SEM:adaf596bd15ca1f129d3","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"7f5c5fb56cf889813b006e3465aabe62c41a5752f0c2297e4b63cb0f75c0f937","finding_id":"SEM:40b5ff31d88fd33546e3","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-25d95333892871cd | data/ingredients/mapped/D-mannose.yaml; nutritional_roles[1] | supports | Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION: [{"field":"nutritional_roles[1]","role":{"confidence":0.7,"evidence":[{"curator_note":"Provisional ENERGY_SOURCE added alongside CARBON_SOURCE; review recommended.","reference_text":"Canonical energy substrate (catabolised for energy)","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"ENERGY_SOURCE"}}] |
| ev-d291b9b950a36b4a | reviews/structured/20261011T024633Z-mim-reconcile-all-batch-05/review.yaml; findings[finding_id=f-e57bb85767f1ca62] | context_only | Predecessor structured review finding f-e57bb85767f1ca62 in 20261011T024633Z-mim-reconcile-all-batch-05 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024633Z-mim-reconcile-all-batch-05.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-d-mannose
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: D-mannose (data/ingredients/mapped/D-mannose.yaml)'
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
summary: Per-record structured review for D-mannose (data/ingredients/mapped/D-mannose.yaml,
  record-044cb1610442ce97, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/D-mannose.yaml
    sha256: 7f5c5fb56cf889813b006e3465aabe62c41a5752f0c2297e4b63cb0f75c0f937
    role: target
  - path: reviews/structured/20261011T024633Z-mim-reconcile-all-batch-05/review.yaml
    sha256: 7549030a5b50ed98868ff3497507fdfbfecd07cd858c76738f734521fa9d3603
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
  - path: reports/yaml_record_review/D-mannose.md
    sha256: 766d6fc671adf8fee7e8f48b5defca10d4f6fb5f533aa68f360936b67bb20305
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-044cb1610442ce97
  path: data/ingredients/mapped/D-mannose.yaml
  label: D-mannose
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/D-mannose.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/D-mannose.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/D-mannose.yaml selected from full-corpus
    review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-044cb1610442ce97
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-044cb1610442ce97
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[1] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-044cb1610442ce97
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024633Z-mim-reconcile-all-batch-05
    and semantic review dispositions on HEAD.
  target_ids:
  - record-044cb1610442ce97
evidence:
- evidence_id: ev-aed133cc6f86cc5b
  kind: record_content
  reference: data/ingredients/mapped/D-mannose.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[840],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:16024","line":842,"mapping_status":"MAPPED","ontology_id":"CHEBI:16024","preferred_term":"D-Mannose"}],"identifier":"CHEBI:16024","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":12,"edge_count":12,"occurrences":12},"occurrence_statistics":{"media_count":12,"total_occurrences":12},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:16024","ontology_label":"D-mannose","ontology_source":"CHEBI"},"preferred_term":"D-Mannose","sssom_rows":[{"data_row":948,"object_id":"CHEBI:16024","object_label":"D-mannose","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:D-mannose","synonym_count":3}'
  snapshot_sha256: 7f5c5fb56cf889813b006e3465aabe62c41a5752f0c2297e4b63cb0f75c0f937
- evidence_id: ev-0e6c3e337e7da83f
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [840]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-9eba5ecbe40a405b
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:D-mannose; data-row positions=[948]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":948,"object_id":"CHEBI:16024","object_label":"D-mannose","other":"D-manno-hexose|CAS:530-26-7","predicate_id":"skos:exactMatch","subject_id":"MIM:D-mannose","validation_method":"OAK+OLS:chebi|CONFIRMED|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-a8780f97038bd869
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[842]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:16024","line":842,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"12","ontology_id":"CHEBI:16024","preferred_term":"D-Mannose","total_occurrences":"12"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-dd55fb9adb32feea
  kind: prior_review
  reference: reports/yaml_record_review/D-mannose.md
  locator: '`data/ingredients/mapped/D-mannose.yaml`:2; Verdict:4; Identity:11; Validation:23;
    Evidence:42; Completeness:60; Recommended Edits:69'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 766d6fc671adf8fee7e8f48b5defca10d4f6fb5f533aa68f360936b67bb20305
  quote: "Recommended Edits:\n- In `data/ingredients/mapped/D-mannose.yaml`, remove\
    \ the provisional\n  `ENERGY_SOURCE` role or replace its `COMPUTATIONAL_PREDICTION`\
    \ evidence with\n  inspected claim-level evidence.\n- Regenerate synchronized\
    \ curated and SSSOM products, then rerun\n  `uv run --frozen python scripts/validate_strict.py`,\n\
    \  `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/D-mannose.yaml\
    \ -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord\
    \ --labels`,\n  `uv run --frozen python scripts/validate_id_label_correspondence.py\
    \ -c conf/id_label_targets.yaml`,\n  and `uv run --frozen python scripts/validate_sssom_invariants.py`."
- evidence_id: ev-2f0ad2a6ed1361b7
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[504,1972]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"7f5c5fb56cf889813b006e3465aabe62c41a5752f0c2297e4b63cb0f75c0f937","finding_id":"SEM:adaf596bd15ca1f129d3","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"7f5c5fb56cf889813b006e3465aabe62c41a5752f0c2297e4b63cb0f75c0f937","finding_id":"SEM:40b5ff31d88fd33546e3","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-25d95333892871cd
  kind: record_content
  reference: data/ingredients/mapped/D-mannose.yaml
  locator: nutritional_roles[1]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION:
    [{"field":"nutritional_roles[1]","role":{"confidence":0.7,"evidence":[{"curator_note":"Provisional
    ENERGY_SOURCE added alongside CARBON_SOURCE; review recommended.","reference_text":"Canonical
    energy substrate (catabolised for energy)","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"ENERGY_SOURCE"}}]'
  snapshot_sha256: 7f5c5fb56cf889813b006e3465aabe62c41a5752f0c2297e4b63cb0f75c0f937
- evidence_id: ev-d291b9b950a36b4a
  kind: prior_review
  reference: reviews/structured/20261011T024633Z-mim-reconcile-all-batch-05/review.yaml
  locator: findings[finding_id=f-e57bb85767f1ca62]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-e57bb85767f1ca62 in 20261011T024633Z-mim-reconcile-all-batch-05
  snapshot_sha256: 7549030a5b50ed98868ff3497507fdfbfecd07cd858c76738f734521fa9d3603
assessments:
- assessment_id: a-90add013ccf42292
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-044cb1610442ce97
  evidence_ids:
  - ev-aed133cc6f86cc5b
  - ev-0e6c3e337e7da83f
  - ev-9eba5ecbe40a405b
  - ev-a8780f97038bd869
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-53a183728b82c7e9
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-044cb1610442ce97
  evidence_ids:
  - ev-dd55fb9adb32feea
  - ev-aed133cc6f86cc5b
  - ev-2f0ad2a6ed1361b7
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T13:49:05Z;
    reviewed SHA-256=7f5c5fb56cf889813b006e3465aabe62c41a5752f0c2297e4b63cb0f75c0f937;
    current SHA-256=7f5c5fb56cf889813b006e3465aabe62c41a5752f0c2297e4b63cb0f75c0f937;
    hash_changed=False. Reports=["reports/yaml_record_review/D-mannose.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The exact CHEBI
    identity, 12/12 count, carbon role, CAS token, and final SSSOM synonym payload
    pass, but the energy role is computational.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-dd55fb9adb32feea
    - ev-aed133cc6f86cc5b
  - name: legacy-native-ids
    value: '["SEM:adaf596bd15ca1f129d3","SEM:40b5ff31d88fd33546e3"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-aed133cc6f86cc5b
    - ev-dd55fb9adb32feea
    - ev-2f0ad2a6ed1361b7
- assessment_id: a-25d95333892871cd
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-044cb1610442ce97
  evidence_ids:
  - ev-dd55fb9adb32feea
  - ev-25d95333892871cd
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-dd55fb9adb32feea
    - ev-25d95333892871cd
findings:
- finding_id: rec-f-e57bb85767f1ca62
  issue_key: mim-reconciliation-role-support-044cb1610442ce97
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: D-Mannose'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-044cb1610442ce97
  evidence_ids:
  - ev-dd55fb9adb32feea
  - ev-25d95333892871cd
  - ev-d291b9b950a36b4a
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/D-mannose.yaml
    role: maintained ingredient
  field_paths:
  - nutritional_roles[1]
  tags:
  - reconciliation
  - bundle-by-owner
  - role-support
  external_issues:
  - https://github.com/CultureBotAI/MediaIngredientMech/issues/718
  previous_occurrences:
  - repository: CultureBotAI/MediaIngredientMech
    review_id: 20261011T024633Z-mim-reconcile-all-batch-05
    finding_id: f-e57bb85767f1ca62
actions:
- action_id: rec-action-e57bb85767f1ca62
  description: 'Reassess prediction-only role support: D-Mannose'
  finding_ids:
  - rec-f-e57bb85767f1ca62
  target_ids:
  - record-044cb1610442ce97
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/D-mannose.yaml
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
  with lineage to 20261011T024633Z-mim-reconcile-all-batch-05.
```
