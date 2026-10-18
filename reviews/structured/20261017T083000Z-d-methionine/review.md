# Per-record structured review: D-Methionine (data/ingredients/mapped/D-Methionine.yaml)

- Review: 20261017T083000Z-d-methionine
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for D-Methionine (data/ingredients/mapped/D-Methionine.yaml, record-ce5a82eb63d60da9, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/D-Methionine.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/D-Methionine.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-ce5a82eb63d60da9 | data/ingredients/mapped/D-Methionine.yaml | maintained | D-Methionine |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-ce5a82eb63d60da9 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-ce5a82eb63d60da9 | Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-ce5a82eb63d60da9 | Reconciled against predecessor batch review 20261011T024633Z-mim-reconcile-all-batch-05 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-ce5a82eb63d60da9.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-ce5a82eb63d60da9.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T13:16:11Z; reviewed SHA-256=4f5efa885ac3389c757f7fa257d2e620dec4d926480b7801090b2bf4b867cdec; current SHA-256=4f5efa885ac3389c757f7fa257d2e620dec4d926480b7801090b2bf4b867cdec; hash_changed=False. Reports=["reports/yaml_record_review/D-Methionine.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI identity, structure fields, 1/1 count, and final SSSOM row pass, but the amino-acid role is only computationally supported.

### Historical provisional-role concern

evidence: concern. Targets: record-ce5a82eb63d60da9.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-cfcffaac5e94597a: Reassess prediction-only role support: D-Methionine

major / open / confirmed; issue key: mim-reconciliation-role-support-ce5a82eb63d60da9.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-cfcffaac5e94597a

Reassess prediction-only role support: D-Methionine

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-0ee2b0e198da0f09 | data/ingredients/mapped/D-Methionine.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[822],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:16867","line":824,"mapping_status":"MAPPED","ontology_id":"CHEBI:16867","preferred_term":"D-Methionine"}],"identifier":"CHEBI:16867","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":1,"edge_count":1,"occurrences":1},"occurrence_statistics":{"media_count":1,"total_occurrences":1},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:16867","ontology_label":"D-methionine","ontology_source":"CHEBI"},"preferred_term":"D-Methionine","sssom_rows":[{"data_row":904,"object_id":"CHEBI:16867","object_label":"D-methionine","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:D-Methionine","synonym_count":0} |
| ev-d4e1d5bac7001289 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [822] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-005ef70b54b62c93 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:D-Methionine; data-row positions=[904] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":904,"object_id":"CHEBI:16867","object_label":"D-methionine","other":"CAS:348-67-4","predicate_id":"skos:exactMatch","subject_id":"MIM:D-Methionine","validation_method":"OAK+OLS:chebi&#124;CONFIRMED&#124;2026-07-07"}] |
| ev-94047ba0d16e2d1f | docs/data/mapped_ingredients.csv; CSV lines=[824] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:16867","line":824,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"1","ontology_id":"CHEBI:16867","preferred_term":"D-Methionine","total_occurrences":"1"}] |
| ev-7b8ed7150ec254a5 | reports/yaml_record_review/D-Methionine.md; &#96;data/ingredients/mapped/D-Methionine.yaml&#96;:2; Verdict:4; Identity:11; Validation:24; Evidence:41; Completeness:55; Recommended Edits:64 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-0e9fafc8e0d55f33 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[474,2076] | context_only | [{"current_record_sha256":"4f5efa885ac3389c757f7fa257d2e620dec4d926480b7801090b2bf4b867cdec","finding_id":"SEM:0ba01b8f18bd280ffbe5","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"4f5efa885ac3389c757f7fa257d2e620dec4d926480b7801090b2bf4b867cdec","finding_id":"SEM:d6e6e10659e44621c8b7","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-a858600100979f1c | data/ingredients/mapped/D-Methionine.yaml; nutritional_roles[0] | supports | Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION: [{"field":"nutritional_roles[0]","role":{"confidence":0.7,"evidence":[{"curator_note":"Provisional role inferred from CHEBI is_a/has_role closure; review recommended.","reference_text":"Inferred from CHEBI ancestry: subclass/has_role of CHEBI:33709 (amino acid)","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"AMINO_ACID_SOURCE"}}] |
| ev-96da67a55f265025 | reviews/structured/20261011T024633Z-mim-reconcile-all-batch-05/review.yaml; findings[finding_id=f-cfcffaac5e94597a] | context_only | Predecessor structured review finding f-cfcffaac5e94597a in 20261011T024633Z-mim-reconcile-all-batch-05 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024633Z-mim-reconcile-all-batch-05.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-d-methionine
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: D-Methionine (data/ingredients/mapped/D-Methionine.yaml)'
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
summary: Per-record structured review for D-Methionine (data/ingredients/mapped/D-Methionine.yaml,
  record-ce5a82eb63d60da9, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/D-Methionine.yaml
    sha256: 4f5efa885ac3389c757f7fa257d2e620dec4d926480b7801090b2bf4b867cdec
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
  - path: reports/yaml_record_review/D-Methionine.md
    sha256: 20fa2652f222b28f270d45ecafcc54d02d400d24c5f9fe6956e7e8ed9b0eea45
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-ce5a82eb63d60da9
  path: data/ingredients/mapped/D-Methionine.yaml
  label: D-Methionine
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/D-Methionine.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/D-Methionine.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/D-Methionine.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-ce5a82eb63d60da9
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-ce5a82eb63d60da9
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-ce5a82eb63d60da9
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024633Z-mim-reconcile-all-batch-05
    and semantic review dispositions on HEAD.
  target_ids:
  - record-ce5a82eb63d60da9
evidence:
- evidence_id: ev-0ee2b0e198da0f09
  kind: record_content
  reference: data/ingredients/mapped/D-Methionine.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[822],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:16867","line":824,"mapping_status":"MAPPED","ontology_id":"CHEBI:16867","preferred_term":"D-Methionine"}],"identifier":"CHEBI:16867","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":1,"edge_count":1,"occurrences":1},"occurrence_statistics":{"media_count":1,"total_occurrences":1},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:16867","ontology_label":"D-methionine","ontology_source":"CHEBI"},"preferred_term":"D-Methionine","sssom_rows":[{"data_row":904,"object_id":"CHEBI:16867","object_label":"D-methionine","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:D-Methionine","synonym_count":0}'
  snapshot_sha256: 4f5efa885ac3389c757f7fa257d2e620dec4d926480b7801090b2bf4b867cdec
- evidence_id: ev-d4e1d5bac7001289
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [822]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-005ef70b54b62c93
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:D-Methionine; data-row positions=[904]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":904,"object_id":"CHEBI:16867","object_label":"D-methionine","other":"CAS:348-67-4","predicate_id":"skos:exactMatch","subject_id":"MIM:D-Methionine","validation_method":"OAK+OLS:chebi|CONFIRMED|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-94047ba0d16e2d1f
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[824]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:16867","line":824,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"1","ontology_id":"CHEBI:16867","preferred_term":"D-Methionine","total_occurrences":"1"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-7b8ed7150ec254a5
  kind: prior_review
  reference: reports/yaml_record_review/D-Methionine.md
  locator: '`data/ingredients/mapped/D-Methionine.yaml`:2; Verdict:4; Identity:11;
    Validation:24; Evidence:41; Completeness:55; Recommended Edits:64'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 20fa2652f222b28f270d45ecafcc54d02d400d24c5f9fe6956e7e8ed9b0eea45
  quote: "Recommended Edits:\n- In `data/ingredients/mapped/D-Methionine.yaml`, either\
    \ replace the\n  computational `AMINO_ACID_SOURCE` evidence with direct CultureBotHT\
    \ or\n  source-backed media-role evidence for this ingredient, or remove the role\n\
    \  facet; then rerun strict validation and the final SSSOM build."
- evidence_id: ev-0e9fafc8e0d55f33
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[474,2076]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"4f5efa885ac3389c757f7fa257d2e620dec4d926480b7801090b2bf4b867cdec","finding_id":"SEM:0ba01b8f18bd280ffbe5","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"4f5efa885ac3389c757f7fa257d2e620dec4d926480b7801090b2bf4b867cdec","finding_id":"SEM:d6e6e10659e44621c8b7","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-a858600100979f1c
  kind: record_content
  reference: data/ingredients/mapped/D-Methionine.yaml
  locator: nutritional_roles[0]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION:
    [{"field":"nutritional_roles[0]","role":{"confidence":0.7,"evidence":[{"curator_note":"Provisional
    role inferred from CHEBI is_a/has_role closure; review recommended.","reference_text":"Inferred
    from CHEBI ancestry: subclass/has_role of CHEBI:33709 (amino acid)","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"AMINO_ACID_SOURCE"}}]'
  snapshot_sha256: 4f5efa885ac3389c757f7fa257d2e620dec4d926480b7801090b2bf4b867cdec
- evidence_id: ev-96da67a55f265025
  kind: prior_review
  reference: reviews/structured/20261011T024633Z-mim-reconcile-all-batch-05/review.yaml
  locator: findings[finding_id=f-cfcffaac5e94597a]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-cfcffaac5e94597a in 20261011T024633Z-mim-reconcile-all-batch-05
  snapshot_sha256: 7549030a5b50ed98868ff3497507fdfbfecd07cd858c76738f734521fa9d3603
assessments:
- assessment_id: a-f82b021c279988dc
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-ce5a82eb63d60da9
  evidence_ids:
  - ev-0ee2b0e198da0f09
  - ev-d4e1d5bac7001289
  - ev-005ef70b54b62c93
  - ev-94047ba0d16e2d1f
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-f66405f537134e1b
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-ce5a82eb63d60da9
  evidence_ids:
  - ev-7b8ed7150ec254a5
  - ev-0ee2b0e198da0f09
  - ev-0e9fafc8e0d55f33
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T13:16:11Z;
    reviewed SHA-256=4f5efa885ac3389c757f7fa257d2e620dec4d926480b7801090b2bf4b867cdec;
    current SHA-256=4f5efa885ac3389c757f7fa257d2e620dec4d926480b7801090b2bf4b867cdec;
    hash_changed=False. Reports=["reports/yaml_record_review/D-Methionine.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The exact CHEBI
    identity, structure fields, 1/1 count, and final SSSOM row pass, but the amino-acid
    role is only computationally supported.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-7b8ed7150ec254a5
    - ev-0ee2b0e198da0f09
  - name: legacy-native-ids
    value: '["SEM:0ba01b8f18bd280ffbe5","SEM:d6e6e10659e44621c8b7"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-0ee2b0e198da0f09
    - ev-7b8ed7150ec254a5
    - ev-0e9fafc8e0d55f33
- assessment_id: a-a858600100979f1c
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-ce5a82eb63d60da9
  evidence_ids:
  - ev-7b8ed7150ec254a5
  - ev-a858600100979f1c
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-7b8ed7150ec254a5
    - ev-a858600100979f1c
findings:
- finding_id: rec-f-cfcffaac5e94597a
  issue_key: mim-reconciliation-role-support-ce5a82eb63d60da9
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: D-Methionine'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-ce5a82eb63d60da9
  evidence_ids:
  - ev-7b8ed7150ec254a5
  - ev-a858600100979f1c
  - ev-96da67a55f265025
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/D-Methionine.yaml
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
    review_id: 20261011T024633Z-mim-reconcile-all-batch-05
    finding_id: f-cfcffaac5e94597a
actions:
- action_id: rec-action-cfcffaac5e94597a
  description: 'Reassess prediction-only role support: D-Methionine'
  finding_ids:
  - rec-f-cfcffaac5e94597a
  target_ids:
  - record-ce5a82eb63d60da9
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/D-Methionine.yaml
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
