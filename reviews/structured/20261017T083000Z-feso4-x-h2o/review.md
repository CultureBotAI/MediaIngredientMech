# Per-record structured review: Feso4_X_H2o (data/ingredients/mapped/Feso4_X_H2o.yaml)

- Review: 20261017T083000Z-feso4-x-h2o
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Feso4_X_H2o (data/ingredients/mapped/Feso4_X_H2o.yaml, record-e122f4baea46aa5d, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Feso4_X_H2o.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Feso4_X_H2o.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-e122f4baea46aa5d | data/ingredients/mapped/Feso4_X_H2o.yaml | maintained | Feso4_X_H2o |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-e122f4baea46aa5d | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-e122f4baea46aa5d | Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-e122f4baea46aa5d | Reconciled against predecessor batch review 20261011T024634Z-mim-reconcile-all-batch-06 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-e122f4baea46aa5d.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-e122f4baea46aa5d.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T16:35:23Z; reviewed SHA-256=38ddf98ad77c0916960080a4220b37f853321c96f7fed30cfe4c4f7d00f8cc01; current SHA-256=38ddf98ad77c0916960080a4220b37f853321c96f7fed30cfe4c4f7d00f8cc01; hash_changed=False. Reports=["reports/yaml_record_review/Feso4_X_H2o.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact monohydrate identity and final SSSOM payload pass, but IRON_SOURCE is computational.

### Historical provisional-role concern

evidence: concern. Targets: record-e122f4baea46aa5d.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-1a924f577fb1f7ef: Reassess prediction-only role support: FeSO4 x H2O

major / open / confirmed; issue key: mim-reconciliation-role-support-e122f4baea46aa5d.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-1a924f577fb1f7ef

Reassess prediction-only role support: FeSO4 x H2O

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-6360a8da85ae503c | data/ingredients/mapped/Feso4_X_H2o.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1002],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:75834","line":1004,"mapping_status":"MAPPED","ontology_id":"CHEBI:75834","preferred_term":"FeSO4 x H2O"}],"identifier":"CHEBI:75834","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":12,"edge_count":12,"occurrences":12},"occurrence_statistics":{"media_count":12,"total_occurrences":12},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:75834","ontology_label":"iron(2+) sulfate monohydrate","ontology_source":"CHEBI"},"preferred_term":"FeSO4 x H2O","sssom_rows":[{"data_row":1204,"object_id":"CHEBI:75834","object_label":"iron(2+) sulfate monohydrate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Feso4_X_H2o","synonym_count":10} |
| ev-24e7702403286838 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1002] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-ecf3b02efc68b4e1 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Feso4_X_H2o; data-row positions=[1204] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1204,"object_id":"CHEBI:75834","object_label":"iron(2+) sulfate monohydrate","other":"FeSO4.H2O&#124;FeSO4\u30fbH2O&#124;ferrous sulfate monohydrate&#124;iron(II) sulfate monohydrate&#124;Feromax&#124;Feroritard&#124;Ferro-Gradumet&#124;Fespan&#124;iron(2+) sulfate--water (1/1)&#124;CAS:17375-41-6","predicate_id":"skos:exactMatch","subject_id":"MIM:Feso4_X_H2o","validation_method":"OAK+OLS:chebi&#124;CONFIRMED&#124;2026-07-07"}] |
| ev-c24762f027b5e590 | docs/data/mapped_ingredients.csv; CSV lines=[1004] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:75834","line":1004,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"12","ontology_id":"CHEBI:75834","preferred_term":"FeSO4 x H2O","total_occurrences":"12"}] |
| ev-8aecc9eab818795f | reports/yaml_record_review/Feso4_X_H2o.md; &#96;data/ingredients/mapped/Feso4_X_H2o.yaml&#96;:2; Verdict:4; Identity:11; Validation:25; Evidence:35; Completeness:56; Recommended Edits:65 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-5041e174c577060b | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[611,1683] | context_only | [{"current_record_sha256":"38ddf98ad77c0916960080a4220b37f853321c96f7fed30cfe4c4f7d00f8cc01","finding_id":"SEM:29c00ad67abbbd898e4f","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"38ddf98ad77c0916960080a4220b37f853321c96f7fed30cfe4c4f7d00f8cc01","finding_id":"SEM:2922b0a2c17cd3007e53","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-d405173a5c08cc6b | data/ingredients/mapped/Feso4_X_H2o.yaml; nutritional_roles[0] | supports | Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION: [{"field":"nutritional_roles[0]","role":{"confidence":0.8,"evidence":[{"curator_note":"Provisional role from a curated name-pattern rule; review recommended.","reference_text":"Inferred from curated media-role name pattern","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"IRON_SOURCE"}}] |
| ev-011cd06fa8bdb638 | reviews/structured/20261011T024634Z-mim-reconcile-all-batch-06/review.yaml; findings[finding_id=f-1a924f577fb1f7ef] | context_only | Predecessor structured review finding f-1a924f577fb1f7ef in 20261011T024634Z-mim-reconcile-all-batch-06 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024634Z-mim-reconcile-all-batch-06.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-feso4-x-h2o
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Feso4_X_H2o (data/ingredients/mapped/Feso4_X_H2o.yaml)'
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
summary: Per-record structured review for Feso4_X_H2o (data/ingredients/mapped/Feso4_X_H2o.yaml,
  record-e122f4baea46aa5d, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Feso4_X_H2o.yaml
    sha256: 38ddf98ad77c0916960080a4220b37f853321c96f7fed30cfe4c4f7d00f8cc01
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
  - path: reports/yaml_record_review/Feso4_X_H2o.md
    sha256: 55b9a536f5d54182a09beb150917f92c7537129a3920ff2a187e0d644bb61207
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-e122f4baea46aa5d
  path: data/ingredients/mapped/Feso4_X_H2o.yaml
  label: Feso4_X_H2o
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Feso4_X_H2o.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Feso4_X_H2o.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Feso4_X_H2o.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-e122f4baea46aa5d
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-e122f4baea46aa5d
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-e122f4baea46aa5d
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024634Z-mim-reconcile-all-batch-06
    and semantic review dispositions on HEAD.
  target_ids:
  - record-e122f4baea46aa5d
evidence:
- evidence_id: ev-6360a8da85ae503c
  kind: record_content
  reference: data/ingredients/mapped/Feso4_X_H2o.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1002],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:75834","line":1004,"mapping_status":"MAPPED","ontology_id":"CHEBI:75834","preferred_term":"FeSO4
    x H2O"}],"identifier":"CHEBI:75834","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":12,"edge_count":12,"occurrences":12},"occurrence_statistics":{"media_count":12,"total_occurrences":12},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:75834","ontology_label":"iron(2+)
    sulfate monohydrate","ontology_source":"CHEBI"},"preferred_term":"FeSO4 x H2O","sssom_rows":[{"data_row":1204,"object_id":"CHEBI:75834","object_label":"iron(2+)
    sulfate monohydrate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Feso4_X_H2o","synonym_count":10}'
  snapshot_sha256: 38ddf98ad77c0916960080a4220b37f853321c96f7fed30cfe4c4f7d00f8cc01
- evidence_id: ev-24e7702403286838
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1002]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-ecf3b02efc68b4e1
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Feso4_X_H2o; data-row positions=[1204]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1204,"object_id":"CHEBI:75834","object_label":"iron(2+)
    sulfate monohydrate","other":"FeSO4.H2O|FeSO4\u30fbH2O|ferrous sulfate monohydrate|iron(II)
    sulfate monohydrate|Feromax|Feroritard|Ferro-Gradumet|Fespan|iron(2+) sulfate--water
    (1/1)|CAS:17375-41-6","predicate_id":"skos:exactMatch","subject_id":"MIM:Feso4_X_H2o","validation_method":"OAK+OLS:chebi|CONFIRMED|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-c24762f027b5e590
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1004]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:75834","line":1004,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"12","ontology_id":"CHEBI:75834","preferred_term":"FeSO4
    x H2O","total_occurrences":"12"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-8aecc9eab818795f
  kind: prior_review
  reference: reports/yaml_record_review/Feso4_X_H2o.md
  locator: '`data/ingredients/mapped/Feso4_X_H2o.yaml`:2; Verdict:4; Identity:11;
    Validation:25; Evidence:35; Completeness:56; Recommended Edits:65'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 55b9a536f5d54182a09beb150917f92c7537129a3920ff2a187e0d644bb61207
  quote: "Recommended Edits:\n- Major: either replace `nutritional_roles.IRON_SOURCE`\
    \ in\n  `data/ingredients/mapped/Feso4_X_H2o.yaml` with source-backed role evidence\n\
    \  or remove the role, sync `data/curated/mapped_ingredients.yaml`, and rerun\n\
    \  strict validation plus the final SSSOM invariant gates."
- evidence_id: ev-5041e174c577060b
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[611,1683]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"38ddf98ad77c0916960080a4220b37f853321c96f7fed30cfe4c4f7d00f8cc01","finding_id":"SEM:29c00ad67abbbd898e4f","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"38ddf98ad77c0916960080a4220b37f853321c96f7fed30cfe4c4f7d00f8cc01","finding_id":"SEM:2922b0a2c17cd3007e53","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-d405173a5c08cc6b
  kind: record_content
  reference: data/ingredients/mapped/Feso4_X_H2o.yaml
  locator: nutritional_roles[0]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION:
    [{"field":"nutritional_roles[0]","role":{"confidence":0.8,"evidence":[{"curator_note":"Provisional
    role from a curated name-pattern rule; review recommended.","reference_text":"Inferred
    from curated media-role name pattern","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"IRON_SOURCE"}}]'
  snapshot_sha256: 38ddf98ad77c0916960080a4220b37f853321c96f7fed30cfe4c4f7d00f8cc01
- evidence_id: ev-011cd06fa8bdb638
  kind: prior_review
  reference: reviews/structured/20261011T024634Z-mim-reconcile-all-batch-06/review.yaml
  locator: findings[finding_id=f-1a924f577fb1f7ef]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-1a924f577fb1f7ef in 20261011T024634Z-mim-reconcile-all-batch-06
  snapshot_sha256: 14c3200be95fdc87fca16bb71628432f3c9aaf8a65356ed494efc776ebe8aa11
assessments:
- assessment_id: a-4602e32cb848fc71
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-e122f4baea46aa5d
  evidence_ids:
  - ev-6360a8da85ae503c
  - ev-24e7702403286838
  - ev-ecf3b02efc68b4e1
  - ev-c24762f027b5e590
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-ab742f577471ff94
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-e122f4baea46aa5d
  evidence_ids:
  - ev-8aecc9eab818795f
  - ev-6360a8da85ae503c
  - ev-5041e174c577060b
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T16:35:23Z;
    reviewed SHA-256=38ddf98ad77c0916960080a4220b37f853321c96f7fed30cfe4c4f7d00f8cc01;
    current SHA-256=38ddf98ad77c0916960080a4220b37f853321c96f7fed30cfe4c4f7d00f8cc01;
    hash_changed=False. Reports=["reports/yaml_record_review/Feso4_X_H2o.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The exact monohydrate
    identity and final SSSOM payload pass, but IRON_SOURCE is computational.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-8aecc9eab818795f
    - ev-6360a8da85ae503c
  - name: legacy-native-ids
    value: '["SEM:29c00ad67abbbd898e4f","SEM:2922b0a2c17cd3007e53"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-6360a8da85ae503c
    - ev-8aecc9eab818795f
    - ev-5041e174c577060b
- assessment_id: a-d405173a5c08cc6b
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-e122f4baea46aa5d
  evidence_ids:
  - ev-8aecc9eab818795f
  - ev-d405173a5c08cc6b
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-8aecc9eab818795f
    - ev-d405173a5c08cc6b
findings:
- finding_id: rec-f-1a924f577fb1f7ef
  issue_key: mim-reconciliation-role-support-e122f4baea46aa5d
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: FeSO4 x H2O'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-e122f4baea46aa5d
  evidence_ids:
  - ev-8aecc9eab818795f
  - ev-d405173a5c08cc6b
  - ev-011cd06fa8bdb638
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Feso4_X_H2o.yaml
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
    review_id: 20261011T024634Z-mim-reconcile-all-batch-06
    finding_id: f-1a924f577fb1f7ef
actions:
- action_id: rec-action-1a924f577fb1f7ef
  description: 'Reassess prediction-only role support: FeSO4 x H2O'
  finding_ids:
  - rec-f-1a924f577fb1f7ef
  target_ids:
  - record-e122f4baea46aa5d
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Feso4_X_H2o.yaml
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
