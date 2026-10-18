# Per-record structured review: D-apiose (data/ingredients/mapped/D-apiose.yaml)

- Review: 20261017T083000Z-d-apiose
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for D-apiose (data/ingredients/mapped/D-apiose.yaml, record-21d663b87707d55a, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/D-apiose.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/D-apiose.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-21d663b87707d55a | data/ingredients/mapped/D-apiose.yaml | maintained | D-apiose |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-21d663b87707d55a | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-21d663b87707d55a | Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-21d663b87707d55a | Reconciled against predecessor batch review 20261011T024633Z-mim-reconcile-all-batch-05 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-21d663b87707d55a.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-21d663b87707d55a.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T13:26:28Z; reviewed SHA-256=9d7fa43e4284fda47f36c31b302cb466abcee6750058edcf9b0bcf14050a8367; current SHA-256=9d7fa43e4284fda47f36c31b302cb466abcee6750058edcf9b0bcf14050a8367; hash_changed=False. Reports=["reports/yaml_record_review/D-apiose.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI identity, structure fields, 0/0 count, and final SSSOM synonym payload pass, but the carbon role is computational.

### Historical provisional-role concern

evidence: concern. Targets: record-21d663b87707d55a.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-67f7fff90e41a97d: Reassess prediction-only role support: D-apiose

major / open / confirmed; issue key: mim-reconciliation-role-support-21d663b87707d55a.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-67f7fff90e41a97d

Reassess prediction-only role support: D-apiose

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-e179ef2d678b37a2 | data/ingredients/mapped/D-apiose.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[829],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:16689","line":831,"mapping_status":"MAPPED","ontology_id":"CHEBI:16689","preferred_term":"D-apiose"}],"identifier":"CHEBI:16689","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:16689","ontology_label":"D-apiose","ontology_source":"CHEBI"},"preferred_term":"D-apiose","sssom_rows":[{"data_row":923,"object_id":"CHEBI:16689","object_label":"D-apiose","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:D-apiose","synonym_count":1} |
| ev-9f0b8a04c961ec67 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [829] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-8c612e8dd5ba6e91 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:D-apiose; data-row positions=[923] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":923,"object_id":"CHEBI:16689","object_label":"D-apiose","other":"3-C-(hydroxymethyl)-D-glycero-tetrose&#124;CAS:639-97-4","predicate_id":"skos:exactMatch","subject_id":"MIM:D-apiose","validation_method":"OAK+OLS:chebi&#124;CONFIRMED&#124;2026-07-07"}] |
| ev-aa2a1b994b94c289 | docs/data/mapped_ingredients.csv; CSV lines=[831] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:16689","line":831,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:16689","preferred_term":"D-apiose","total_occurrences":"0"}] |
| ev-47068dcb9673180f | reports/yaml_record_review/D-apiose.md; &#96;data/ingredients/mapped/D-apiose.yaml&#96;:2; Verdict:4; Identity:11; Validation:25; Evidence:42; Completeness:57; Recommended Edits:65 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-c1c1d3ccf69522c8 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[487,2020] | context_only | [{"current_record_sha256":"9d7fa43e4284fda47f36c31b302cb466abcee6750058edcf9b0bcf14050a8367","finding_id":"SEM:784fa3b4070033300cc9","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"9d7fa43e4284fda47f36c31b302cb466abcee6750058edcf9b0bcf14050a8367","finding_id":"SEM:d8805b0adabec1e2a979","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-6728459bb92660c8 | data/ingredients/mapped/D-apiose.yaml; nutritional_roles[0] | supports | Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION: [{"field":"nutritional_roles[0]","role":{"confidence":0.7,"evidence":[{"curator_note":"Provisional role inferred from CHEBI is_a/has_role closure; review recommended.","reference_text":"Inferred from CHEBI ancestry: subclass/has_role of CHEBI:16646 (carbohydrate)","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"CARBON_SOURCE"}}] |
| ev-a3e2c796e5aa9dae | reviews/structured/20261011T024633Z-mim-reconcile-all-batch-05/review.yaml; findings[finding_id=f-67f7fff90e41a97d] | context_only | Predecessor structured review finding f-67f7fff90e41a97d in 20261011T024633Z-mim-reconcile-all-batch-05 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024633Z-mim-reconcile-all-batch-05.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-d-apiose
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: D-apiose (data/ingredients/mapped/D-apiose.yaml)'
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
summary: Per-record structured review for D-apiose (data/ingredients/mapped/D-apiose.yaml,
  record-21d663b87707d55a, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/D-apiose.yaml
    sha256: 9d7fa43e4284fda47f36c31b302cb466abcee6750058edcf9b0bcf14050a8367
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
  - path: reports/yaml_record_review/D-apiose.md
    sha256: 8d140200cee6988185c006bb18031980de4eca1ed2b584f810f0a6b93a244bea
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-21d663b87707d55a
  path: data/ingredients/mapped/D-apiose.yaml
  label: D-apiose
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/D-apiose.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/D-apiose.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/D-apiose.yaml selected from full-corpus
    review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-21d663b87707d55a
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-21d663b87707d55a
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-21d663b87707d55a
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024633Z-mim-reconcile-all-batch-05
    and semantic review dispositions on HEAD.
  target_ids:
  - record-21d663b87707d55a
evidence:
- evidence_id: ev-e179ef2d678b37a2
  kind: record_content
  reference: data/ingredients/mapped/D-apiose.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[829],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:16689","line":831,"mapping_status":"MAPPED","ontology_id":"CHEBI:16689","preferred_term":"D-apiose"}],"identifier":"CHEBI:16689","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:16689","ontology_label":"D-apiose","ontology_source":"CHEBI"},"preferred_term":"D-apiose","sssom_rows":[{"data_row":923,"object_id":"CHEBI:16689","object_label":"D-apiose","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:D-apiose","synonym_count":1}'
  snapshot_sha256: 9d7fa43e4284fda47f36c31b302cb466abcee6750058edcf9b0bcf14050a8367
- evidence_id: ev-9f0b8a04c961ec67
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [829]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-8c612e8dd5ba6e91
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:D-apiose; data-row positions=[923]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":923,"object_id":"CHEBI:16689","object_label":"D-apiose","other":"3-C-(hydroxymethyl)-D-glycero-tetrose|CAS:639-97-4","predicate_id":"skos:exactMatch","subject_id":"MIM:D-apiose","validation_method":"OAK+OLS:chebi|CONFIRMED|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-aa2a1b994b94c289
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[831]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:16689","line":831,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:16689","preferred_term":"D-apiose","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-47068dcb9673180f
  kind: prior_review
  reference: reports/yaml_record_review/D-apiose.md
  locator: '`data/ingredients/mapped/D-apiose.yaml`:2; Verdict:4; Identity:11; Validation:25;
    Evidence:42; Completeness:57; Recommended Edits:65'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 8d140200cee6988185c006bb18031980de4eca1ed2b584f810f0a6b93a244bea
  quote: "Recommended Edits:\n- In `data/ingredients/mapped/D-apiose.yaml`, either\
    \ replace the computational\n  `CARBON_SOURCE` evidence with direct CultureBotHT\
    \ or source-backed media-role\n  evidence for this ingredient, or remove the role\
    \ facet; then rerun strict\n  validation and the final SSSOM build."
- evidence_id: ev-c1c1d3ccf69522c8
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[487,2020]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"9d7fa43e4284fda47f36c31b302cb466abcee6750058edcf9b0bcf14050a8367","finding_id":"SEM:784fa3b4070033300cc9","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"9d7fa43e4284fda47f36c31b302cb466abcee6750058edcf9b0bcf14050a8367","finding_id":"SEM:d8805b0adabec1e2a979","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-6728459bb92660c8
  kind: record_content
  reference: data/ingredients/mapped/D-apiose.yaml
  locator: nutritional_roles[0]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION:
    [{"field":"nutritional_roles[0]","role":{"confidence":0.7,"evidence":[{"curator_note":"Provisional
    role inferred from CHEBI is_a/has_role closure; review recommended.","reference_text":"Inferred
    from CHEBI ancestry: subclass/has_role of CHEBI:16646 (carbohydrate)","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"CARBON_SOURCE"}}]'
  snapshot_sha256: 9d7fa43e4284fda47f36c31b302cb466abcee6750058edcf9b0bcf14050a8367
- evidence_id: ev-a3e2c796e5aa9dae
  kind: prior_review
  reference: reviews/structured/20261011T024633Z-mim-reconcile-all-batch-05/review.yaml
  locator: findings[finding_id=f-67f7fff90e41a97d]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-67f7fff90e41a97d in 20261011T024633Z-mim-reconcile-all-batch-05
  snapshot_sha256: 7549030a5b50ed98868ff3497507fdfbfecd07cd858c76738f734521fa9d3603
assessments:
- assessment_id: a-8b10218581f05916
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-21d663b87707d55a
  evidence_ids:
  - ev-e179ef2d678b37a2
  - ev-9f0b8a04c961ec67
  - ev-8c612e8dd5ba6e91
  - ev-aa2a1b994b94c289
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-ebf2b17dee226378
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-21d663b87707d55a
  evidence_ids:
  - ev-47068dcb9673180f
  - ev-e179ef2d678b37a2
  - ev-c1c1d3ccf69522c8
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T13:26:28Z;
    reviewed SHA-256=9d7fa43e4284fda47f36c31b302cb466abcee6750058edcf9b0bcf14050a8367;
    current SHA-256=9d7fa43e4284fda47f36c31b302cb466abcee6750058edcf9b0bcf14050a8367;
    hash_changed=False. Reports=["reports/yaml_record_review/D-apiose.md"]. Full reports,
    including older originals behind refresh floors, are hashed inputs. Repeated refresh
    allegations are not counted as new defects. The narrative group is not a count
    of distinct scientific findings. Latest manifest note: The exact CHEBI identity,
    structure fields, 0/0 count, and final SSSOM synonym payload pass, but the carbon
    role is computational.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-47068dcb9673180f
    - ev-e179ef2d678b37a2
  - name: legacy-native-ids
    value: '["SEM:784fa3b4070033300cc9","SEM:d8805b0adabec1e2a979"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-e179ef2d678b37a2
    - ev-47068dcb9673180f
    - ev-c1c1d3ccf69522c8
- assessment_id: a-6728459bb92660c8
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-21d663b87707d55a
  evidence_ids:
  - ev-47068dcb9673180f
  - ev-6728459bb92660c8
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-47068dcb9673180f
    - ev-6728459bb92660c8
findings:
- finding_id: rec-f-67f7fff90e41a97d
  issue_key: mim-reconciliation-role-support-21d663b87707d55a
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: D-apiose'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-21d663b87707d55a
  evidence_ids:
  - ev-47068dcb9673180f
  - ev-6728459bb92660c8
  - ev-a3e2c796e5aa9dae
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/D-apiose.yaml
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
    finding_id: f-67f7fff90e41a97d
actions:
- action_id: rec-action-67f7fff90e41a97d
  description: 'Reassess prediction-only role support: D-apiose'
  finding_ids:
  - rec-f-67f7fff90e41a97d
  target_ids:
  - record-21d663b87707d55a
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/D-apiose.yaml
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
