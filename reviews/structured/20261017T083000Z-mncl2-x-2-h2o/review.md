# Per-record structured review: Mncl2_X_2_H2o (data/ingredients/mapped/Mncl2_X_2_H2o.yaml)

- Review: 20261017T083000Z-mncl2-x-2-h2o
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Mncl2_X_2_H2o (data/ingredients/mapped/Mncl2_X_2_H2o.yaml, record-e5f54c96163d2705, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Mncl2_X_2_H2o.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Mncl2_X_2_H2o.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-e5f54c96163d2705 | data/ingredients/mapped/Mncl2_X_2_H2o.yaml | maintained | Mncl2_X_2_H2o |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-e5f54c96163d2705 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-e5f54c96163d2705 | Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-e5f54c96163d2705 | Reconciled against predecessor batch review 20261011T024636Z-mim-reconcile-all-batch-08 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-e5f54c96163d2705.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-e5f54c96163d2705.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T03:39:29Z; reviewed SHA-256=9e38605be2e4e3efd447015efb67703002c295e408467e81fa66e9f224e1ff7b; current SHA-256=9e38605be2e4e3efd447015efb67703002c295e408467e81fa66e9f224e1ff7b; hash_changed=False. Reports=["reports/yaml_record_review/Mncl2_X_2_H2o.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI:131395 manganese chloride dihydrate identity, structure, hydrate grounding, occurrence count, and final SSSOM row pass, but TRACE_ELEMENT is still provisional.

### Historical provisional-role concern

evidence: concern. Targets: record-e5f54c96163d2705.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-9c940818549c04da: Reassess prediction-only role support: MnCl2 x 2 H2O

major / open / confirmed; issue key: mim-reconciliation-role-support-e5f54c96163d2705.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-9c940818549c04da

Reassess prediction-only role support: MnCl2 x 2 H2O

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-5096f787dcc973de | data/ingredients/mapped/Mncl2_X_2_H2o.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1411],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:131395","line":1413,"mapping_status":"MAPPED","ontology_id":"CHEBI:131395","preferred_term":"MnCl2 x 2 H2O"}],"identifier":"CHEBI:131395","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":40,"edge_count":40,"occurrences":40},"occurrence_statistics":{"media_count":40,"total_occurrences":40},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:131395","ontology_label":"manganese(II) chloride dihydrate","ontology_source":"CHEBI"},"preferred_term":"MnCl2 x 2 H2O","sssom_rows":[{"data_row":1890,"object_id":"CHEBI:131395","object_label":"manganese(II) chloride dihydrate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Mncl2_X_2_H2o","synonym_count":9} |
| ev-4c346cbe67609444 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1411] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-3b6469095f6db297 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Mncl2_X_2_H2o; data-row positions=[1890] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1890,"object_id":"CHEBI:131395","object_label":"manganese(II) chloride dihydrate","other":"MnCl2\u00b72H2O&#124;MnCl2\uff0e2H2O&#124;manganese chloride dihydrate&#124;manganese dichloride dihydrate&#124;manganese(2+) chloride dihydrate&#124;dichloromanganese--water (1/2)&#124;manganese(2+) chloride--water (1/2)","predicate_id":"skos:exactMatch","subject_id":"MIM:Mncl2_X_2_H2o","validation_method":"OAK+OLS:chebi&#124;SYNONYM_ENRICH&#124;2026-07-07"}] |
| ev-46b68ec706ca1aed | docs/data/mapped_ingredients.csv; CSV lines=[1413] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:131395","line":1413,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"40","ontology_id":"CHEBI:131395","preferred_term":"MnCl2 x 2 H2O","total_occurrences":"40"}] |
| ev-d55b54e74a68b0d8 | reports/yaml_record_review/Mncl2_X_2_H2o.md; &#96;data/ingredients/mapped/Mncl2_X_2_H2o.yaml&#96;:2; Verdict:4; Identity:12; Validation:23; Evidence:30; Completeness:38; Recommended Edits:45 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-6639dd1b14e00e32 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[948,1620] | context_only | [{"current_record_sha256":"9e38605be2e4e3efd447015efb67703002c295e408467e81fa66e9f224e1ff7b","finding_id":"SEM:8b9a018c17c2973f9390","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"9e38605be2e4e3efd447015efb67703002c295e408467e81fa66e9f224e1ff7b","finding_id":"SEM:7e0c9d9a46bab9dd599e","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-7f67d83fed37606b | data/ingredients/mapped/Mncl2_X_2_H2o.yaml; nutritional_roles[0] | supports | Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION: [{"field":"nutritional_roles[0]","role":{"confidence":0.8,"evidence":[{"curator_note":"Provisional role from a curated name-pattern rule; review recommended.","reference_text":"Inferred from curated media-role name pattern","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"TRACE_ELEMENT"}}] |
| ev-18e395017d798e23 | reviews/structured/20261011T024636Z-mim-reconcile-all-batch-08/review.yaml; findings[finding_id=f-9c940818549c04da] | context_only | Predecessor structured review finding f-9c940818549c04da in 20261011T024636Z-mim-reconcile-all-batch-08 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024636Z-mim-reconcile-all-batch-08.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-mncl2-x-2-h2o
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Mncl2_X_2_H2o (data/ingredients/mapped/Mncl2_X_2_H2o.yaml)'
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
summary: Per-record structured review for Mncl2_X_2_H2o (data/ingredients/mapped/Mncl2_X_2_H2o.yaml,
  record-e5f54c96163d2705, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Mncl2_X_2_H2o.yaml
    sha256: 9e38605be2e4e3efd447015efb67703002c295e408467e81fa66e9f224e1ff7b
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
  - path: reports/yaml_record_review/Mncl2_X_2_H2o.md
    sha256: 067288edc9586cda87bfe364f17e5c3a4816ddacfe2007fdeadc51b596b6067f
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-e5f54c96163d2705
  path: data/ingredients/mapped/Mncl2_X_2_H2o.yaml
  label: Mncl2_X_2_H2o
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Mncl2_X_2_H2o.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Mncl2_X_2_H2o.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Mncl2_X_2_H2o.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-e5f54c96163d2705
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-e5f54c96163d2705
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-e5f54c96163d2705
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024636Z-mim-reconcile-all-batch-08
    and semantic review dispositions on HEAD.
  target_ids:
  - record-e5f54c96163d2705
evidence:
- evidence_id: ev-5096f787dcc973de
  kind: record_content
  reference: data/ingredients/mapped/Mncl2_X_2_H2o.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1411],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:131395","line":1413,"mapping_status":"MAPPED","ontology_id":"CHEBI:131395","preferred_term":"MnCl2
    x 2 H2O"}],"identifier":"CHEBI:131395","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":40,"edge_count":40,"occurrences":40},"occurrence_statistics":{"media_count":40,"total_occurrences":40},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:131395","ontology_label":"manganese(II)
    chloride dihydrate","ontology_source":"CHEBI"},"preferred_term":"MnCl2 x 2 H2O","sssom_rows":[{"data_row":1890,"object_id":"CHEBI:131395","object_label":"manganese(II)
    chloride dihydrate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Mncl2_X_2_H2o","synonym_count":9}'
  snapshot_sha256: 9e38605be2e4e3efd447015efb67703002c295e408467e81fa66e9f224e1ff7b
- evidence_id: ev-4c346cbe67609444
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1411]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-3b6469095f6db297
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Mncl2_X_2_H2o; data-row positions=[1890]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1890,"object_id":"CHEBI:131395","object_label":"manganese(II)
    chloride dihydrate","other":"MnCl2\u00b72H2O|MnCl2\uff0e2H2O|manganese chloride
    dihydrate|manganese dichloride dihydrate|manganese(2+) chloride dihydrate|dichloromanganese--water
    (1/2)|manganese(2+) chloride--water (1/2)","predicate_id":"skos:exactMatch","subject_id":"MIM:Mncl2_X_2_H2o","validation_method":"OAK+OLS:chebi|SYNONYM_ENRICH|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-46b68ec706ca1aed
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1413]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:131395","line":1413,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"40","ontology_id":"CHEBI:131395","preferred_term":"MnCl2
    x 2 H2O","total_occurrences":"40"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-d55b54e74a68b0d8
  kind: prior_review
  reference: reports/yaml_record_review/Mncl2_X_2_H2o.md
  locator: '`data/ingredients/mapped/Mncl2_X_2_H2o.yaml`:2; Verdict:4; Identity:12;
    Validation:23; Evidence:30; Completeness:38; Recommended Edits:45'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 067288edc9586cda87bfe364f17e5c3a4816ddacfe2007fdeadc51b596b6067f
  quote: "Recommended Edits:\n- Major: add source-backed evidence that MnCl2 x 2 H2O\
    \ is used as a trace\n  element source in media, or remove the provisional `TRACE_ELEMENT`\
    \ role."
- evidence_id: ev-6639dd1b14e00e32
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[948,1620]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"9e38605be2e4e3efd447015efb67703002c295e408467e81fa66e9f224e1ff7b","finding_id":"SEM:8b9a018c17c2973f9390","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"9e38605be2e4e3efd447015efb67703002c295e408467e81fa66e9f224e1ff7b","finding_id":"SEM:7e0c9d9a46bab9dd599e","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-7f67d83fed37606b
  kind: record_content
  reference: data/ingredients/mapped/Mncl2_X_2_H2o.yaml
  locator: nutritional_roles[0]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION:
    [{"field":"nutritional_roles[0]","role":{"confidence":0.8,"evidence":[{"curator_note":"Provisional
    role from a curated name-pattern rule; review recommended.","reference_text":"Inferred
    from curated media-role name pattern","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"TRACE_ELEMENT"}}]'
  snapshot_sha256: 9e38605be2e4e3efd447015efb67703002c295e408467e81fa66e9f224e1ff7b
- evidence_id: ev-18e395017d798e23
  kind: prior_review
  reference: reviews/structured/20261011T024636Z-mim-reconcile-all-batch-08/review.yaml
  locator: findings[finding_id=f-9c940818549c04da]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-9c940818549c04da in 20261011T024636Z-mim-reconcile-all-batch-08
  snapshot_sha256: 4dd969b7020555cc2250a236d6fded134bedf3add1e1c5c72d269e98f9ae001b
assessments:
- assessment_id: a-2272b32159538d2f
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-e5f54c96163d2705
  evidence_ids:
  - ev-5096f787dcc973de
  - ev-4c346cbe67609444
  - ev-3b6469095f6db297
  - ev-46b68ec706ca1aed
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-2b39482a6fa5c7cb
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-e5f54c96163d2705
  evidence_ids:
  - ev-d55b54e74a68b0d8
  - ev-5096f787dcc973de
  - ev-6639dd1b14e00e32
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T03:39:29Z;
    reviewed SHA-256=9e38605be2e4e3efd447015efb67703002c295e408467e81fa66e9f224e1ff7b;
    current SHA-256=9e38605be2e4e3efd447015efb67703002c295e408467e81fa66e9f224e1ff7b;
    hash_changed=False. Reports=["reports/yaml_record_review/Mncl2_X_2_H2o.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The exact CHEBI:131395
    manganese chloride dihydrate identity, structure, hydrate grounding, occurrence
    count, and final SSSOM row pass, but TRACE_ELEMENT is still provisional.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-d55b54e74a68b0d8
    - ev-5096f787dcc973de
  - name: legacy-native-ids
    value: '["SEM:8b9a018c17c2973f9390","SEM:7e0c9d9a46bab9dd599e"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-5096f787dcc973de
    - ev-d55b54e74a68b0d8
    - ev-6639dd1b14e00e32
- assessment_id: a-7f67d83fed37606b
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-e5f54c96163d2705
  evidence_ids:
  - ev-d55b54e74a68b0d8
  - ev-7f67d83fed37606b
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-d55b54e74a68b0d8
    - ev-7f67d83fed37606b
findings:
- finding_id: rec-f-9c940818549c04da
  issue_key: mim-reconciliation-role-support-e5f54c96163d2705
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: MnCl2 x 2 H2O'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-e5f54c96163d2705
  evidence_ids:
  - ev-d55b54e74a68b0d8
  - ev-7f67d83fed37606b
  - ev-18e395017d798e23
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Mncl2_X_2_H2o.yaml
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
    finding_id: f-9c940818549c04da
actions:
- action_id: rec-action-9c940818549c04da
  description: 'Reassess prediction-only role support: MnCl2 x 2 H2O'
  finding_ids:
  - rec-f-9c940818549c04da
  target_ids:
  - record-e5f54c96163d2705
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Mncl2_X_2_H2o.yaml
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
