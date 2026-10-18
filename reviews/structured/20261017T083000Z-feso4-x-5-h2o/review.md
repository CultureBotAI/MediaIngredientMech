# Per-record structured review: Feso4_X_5_H2o (data/ingredients/mapped/Feso4_X_5_H2o.yaml)

- Review: 20261017T083000Z-feso4-x-5-h2o
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Feso4_X_5_H2o (data/ingredients/mapped/Feso4_X_5_H2o.yaml, record-d63ed86560b95ad5, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Feso4_X_5_H2o.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Feso4_X_5_H2o.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-d63ed86560b95ad5 | data/ingredients/mapped/Feso4_X_5_H2o.yaml | maintained | Feso4_X_5_H2o |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-d63ed86560b95ad5 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-d63ed86560b95ad5 | Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-d63ed86560b95ad5 | Reconciled against predecessor batch review 20261011T024634Z-mim-reconcile-all-batch-06 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-d63ed86560b95ad5.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-d63ed86560b95ad5.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T16:31:10Z; reviewed SHA-256=283f4239679787d944f8c7865c1d003f74fb6338bcaa995efa0a040e2d317462; current SHA-256=283f4239679787d944f8c7865c1d003f74fb6338bcaa995efa0a040e2d317462; hash_changed=False. Reports=["reports/yaml_record_review/Feso4_X_5_H2o.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The local pentahydrate identity and final SSSOM row pair pass, but IRON_SOURCE is computational.

### Historical provisional-role concern

evidence: concern. Targets: record-d63ed86560b95ad5.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-7b4b5d8c65a8b8af: Reassess prediction-only role support: FeSO4 x 5 H2O

major / open / confirmed; issue key: mim-reconciliation-role-support-d63ed86560b95ad5.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-7b4b5d8c65a8b8af

Reassess prediction-only role support: FeSO4 x 5 H2O

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-9f9303ef0d7c2433 | data/ingredients/mapped/Feso4_X_5_H2o.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[998],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.compound:feso4_x_5_h2o","line":1000,"mapping_status":"MAPPED","ontology_id":"CHEBI:75832","preferred_term":"FeSO4 x 5 H2O"}],"identifier":"kgmicrobe.compound:feso4_x_5_h2o","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":4,"edge_count":4,"occurrences":4},"occurrence_statistics":{"media_count":4,"total_occurrences":4},"ontology_mapping":{"mapping_quality":"NARROW_MATCH","ontology_id":"CHEBI:75832","ontology_label":"iron(2+) sulfate (anhydrous)","ontology_source":"CHEBI"},"preferred_term":"FeSO4 x 5 H2O","sssom_rows":[{"data_row":1199,"object_id":"CHEBI:75832","object_label":"iron(2+) sulfate (anhydrous)","predicate_id":"skos:broadMatch"},{"data_row":1200,"object_id":"kgmicrobe.compound:feso4_x_5_h2o","object_label":"FeSO4 x 5 H2O","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Feso4_X_5_H2o","synonym_count":11} |
| ev-761999f41566b76f | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [998] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-6b25f4326760f2e2 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Feso4_X_5_H2o; data-row positions=[1199,1200] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1199,"object_id":"CHEBI:75832","object_label":"iron(2+) sulfate (anhydrous)","other":"","predicate_id":"skos:broadMatch","subject_id":"MIM:Feso4_X_5_H2o","validation_method":"manual:reconcile_sssom&#124;PREDICATE&#124;2026-09-20"},{"data_row":1200,"object_id":"kgmicrobe.compound:feso4_x_5_h2o","object_label":"FeSO4 x 5 H2O","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Feso4_X_5_H2o","validation_method":""}] |
| ev-fcede97e93d6ac70 | docs/data/mapped_ingredients.csv; CSV lines=[1000] | supports | Published identity and count rows inspected: [{"identifier":"kgmicrobe.compound:feso4_x_5_h2o","line":1000,"mapping_quality":"NARROW_MATCH","mapping_status":"MAPPED","media_count":"4","ontology_id":"CHEBI:75832","preferred_term":"FeSO4 x 5 H2O","total_occurrences":"4"}] |
| ev-c5def44123a42278 | reports/yaml_record_review/Feso4_X_5_H2o.md; &#96;data/ingredients/mapped/Feso4_X_5_H2o.yaml&#96;:2; Verdict:4; Identity:11; Validation:26; Evidence:36; Completeness:57; Recommended Edits:63 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-5f156fa0f79c5498 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[608,1594] | context_only | [{"current_record_sha256":"283f4239679787d944f8c7865c1d003f74fb6338bcaa995efa0a040e2d317462","finding_id":"SEM:cea032632afa91816e3f","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"283f4239679787d944f8c7865c1d003f74fb6338bcaa995efa0a040e2d317462","finding_id":"SEM:842f455b99de1f76120f","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-0b2318eab73fc17e | data/ingredients/mapped/Feso4_X_5_H2o.yaml; nutritional_roles[0] | supports | Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION: [{"field":"nutritional_roles[0]","role":{"confidence":0.8,"evidence":[{"curator_note":"Provisional role from a curated name-pattern rule; review recommended.","reference_text":"Inferred from curated media-role name pattern","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"IRON_SOURCE"}}] |
| ev-162d9a72b897b6a7 | reviews/structured/20261011T024634Z-mim-reconcile-all-batch-06/review.yaml; findings[finding_id=f-7b4b5d8c65a8b8af] | context_only | Predecessor structured review finding f-7b4b5d8c65a8b8af in 20261011T024634Z-mim-reconcile-all-batch-06 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024634Z-mim-reconcile-all-batch-06.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-feso4-x-5-h2o
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Feso4_X_5_H2o (data/ingredients/mapped/Feso4_X_5_H2o.yaml)'
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
summary: Per-record structured review for Feso4_X_5_H2o (data/ingredients/mapped/Feso4_X_5_H2o.yaml,
  record-d63ed86560b95ad5, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Feso4_X_5_H2o.yaml
    sha256: 283f4239679787d944f8c7865c1d003f74fb6338bcaa995efa0a040e2d317462
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
  - path: reports/yaml_record_review/Feso4_X_5_H2o.md
    sha256: 483c71216c9afc366b89a9e8d95e553f0741e1497901a4e3f6d38c10126a6a83
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-d63ed86560b95ad5
  path: data/ingredients/mapped/Feso4_X_5_H2o.yaml
  label: Feso4_X_5_H2o
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Feso4_X_5_H2o.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Feso4_X_5_H2o.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Feso4_X_5_H2o.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-d63ed86560b95ad5
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-d63ed86560b95ad5
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-d63ed86560b95ad5
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024634Z-mim-reconcile-all-batch-06
    and semantic review dispositions on HEAD.
  target_ids:
  - record-d63ed86560b95ad5
evidence:
- evidence_id: ev-9f9303ef0d7c2433
  kind: record_content
  reference: data/ingredients/mapped/Feso4_X_5_H2o.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[998],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.compound:feso4_x_5_h2o","line":1000,"mapping_status":"MAPPED","ontology_id":"CHEBI:75832","preferred_term":"FeSO4
    x 5 H2O"}],"identifier":"kgmicrobe.compound:feso4_x_5_h2o","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":4,"edge_count":4,"occurrences":4},"occurrence_statistics":{"media_count":4,"total_occurrences":4},"ontology_mapping":{"mapping_quality":"NARROW_MATCH","ontology_id":"CHEBI:75832","ontology_label":"iron(2+)
    sulfate (anhydrous)","ontology_source":"CHEBI"},"preferred_term":"FeSO4 x 5 H2O","sssom_rows":[{"data_row":1199,"object_id":"CHEBI:75832","object_label":"iron(2+)
    sulfate (anhydrous)","predicate_id":"skos:broadMatch"},{"data_row":1200,"object_id":"kgmicrobe.compound:feso4_x_5_h2o","object_label":"FeSO4
    x 5 H2O","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Feso4_X_5_H2o","synonym_count":11}'
  snapshot_sha256: 283f4239679787d944f8c7865c1d003f74fb6338bcaa995efa0a040e2d317462
- evidence_id: ev-761999f41566b76f
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [998]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-6b25f4326760f2e2
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Feso4_X_5_H2o; data-row positions=[1199,1200]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1199,"object_id":"CHEBI:75832","object_label":"iron(2+)
    sulfate (anhydrous)","other":"","predicate_id":"skos:broadMatch","subject_id":"MIM:Feso4_X_5_H2o","validation_method":"manual:reconcile_sssom|PREDICATE|2026-09-20"},{"data_row":1200,"object_id":"kgmicrobe.compound:feso4_x_5_h2o","object_label":"FeSO4
    x 5 H2O","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Feso4_X_5_H2o","validation_method":""}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-fcede97e93d6ac70
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1000]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"kgmicrobe.compound:feso4_x_5_h2o","line":1000,"mapping_quality":"NARROW_MATCH","mapping_status":"MAPPED","media_count":"4","ontology_id":"CHEBI:75832","preferred_term":"FeSO4
    x 5 H2O","total_occurrences":"4"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-c5def44123a42278
  kind: prior_review
  reference: reports/yaml_record_review/Feso4_X_5_H2o.md
  locator: '`data/ingredients/mapped/Feso4_X_5_H2o.yaml`:2; Verdict:4; Identity:11;
    Validation:26; Evidence:36; Completeness:57; Recommended Edits:63'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 483c71216c9afc366b89a9e8d95e553f0741e1497901a4e3f6d38c10126a6a83
  quote: "Recommended Edits:\n- Major: replace or remove the provisional `IRON_SOURCE`\
    \ assignment in\n  `data/ingredients/mapped/Feso4_X_5_H2o.yaml`; if a source supports\
    \ it, attach\n  `DATABASE_ENTRY` or literature evidence at the role. Then sync\n\
    \  `data/curated/mapped_ingredients.yaml` and rerun strict validation plus the\n\
    \  final SSSOM invariant gates."
- evidence_id: ev-5f156fa0f79c5498
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[608,1594]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"283f4239679787d944f8c7865c1d003f74fb6338bcaa995efa0a040e2d317462","finding_id":"SEM:cea032632afa91816e3f","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"283f4239679787d944f8c7865c1d003f74fb6338bcaa995efa0a040e2d317462","finding_id":"SEM:842f455b99de1f76120f","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-0b2318eab73fc17e
  kind: record_content
  reference: data/ingredients/mapped/Feso4_X_5_H2o.yaml
  locator: nutritional_roles[0]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION:
    [{"field":"nutritional_roles[0]","role":{"confidence":0.8,"evidence":[{"curator_note":"Provisional
    role from a curated name-pattern rule; review recommended.","reference_text":"Inferred
    from curated media-role name pattern","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"IRON_SOURCE"}}]'
  snapshot_sha256: 283f4239679787d944f8c7865c1d003f74fb6338bcaa995efa0a040e2d317462
- evidence_id: ev-162d9a72b897b6a7
  kind: prior_review
  reference: reviews/structured/20261011T024634Z-mim-reconcile-all-batch-06/review.yaml
  locator: findings[finding_id=f-7b4b5d8c65a8b8af]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-7b4b5d8c65a8b8af in 20261011T024634Z-mim-reconcile-all-batch-06
  snapshot_sha256: 14c3200be95fdc87fca16bb71628432f3c9aaf8a65356ed494efc776ebe8aa11
assessments:
- assessment_id: a-e8e3b0ce0b58cc22
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-d63ed86560b95ad5
  evidence_ids:
  - ev-9f9303ef0d7c2433
  - ev-761999f41566b76f
  - ev-6b25f4326760f2e2
  - ev-fcede97e93d6ac70
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-3cae154a94c2ad83
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-d63ed86560b95ad5
  evidence_ids:
  - ev-c5def44123a42278
  - ev-9f9303ef0d7c2433
  - ev-5f156fa0f79c5498
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T16:31:10Z;
    reviewed SHA-256=283f4239679787d944f8c7865c1d003f74fb6338bcaa995efa0a040e2d317462;
    current SHA-256=283f4239679787d944f8c7865c1d003f74fb6338bcaa995efa0a040e2d317462;
    hash_changed=False. Reports=["reports/yaml_record_review/Feso4_X_5_H2o.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The local pentahydrate
    identity and final SSSOM row pair pass, but IRON_SOURCE is computational.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-c5def44123a42278
    - ev-9f9303ef0d7c2433
  - name: legacy-native-ids
    value: '["SEM:cea032632afa91816e3f","SEM:842f455b99de1f76120f"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-9f9303ef0d7c2433
    - ev-c5def44123a42278
    - ev-5f156fa0f79c5498
- assessment_id: a-0b2318eab73fc17e
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-d63ed86560b95ad5
  evidence_ids:
  - ev-c5def44123a42278
  - ev-0b2318eab73fc17e
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-c5def44123a42278
    - ev-0b2318eab73fc17e
findings:
- finding_id: rec-f-7b4b5d8c65a8b8af
  issue_key: mim-reconciliation-role-support-d63ed86560b95ad5
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: FeSO4 x 5 H2O'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-d63ed86560b95ad5
  evidence_ids:
  - ev-c5def44123a42278
  - ev-0b2318eab73fc17e
  - ev-162d9a72b897b6a7
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Feso4_X_5_H2o.yaml
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
    finding_id: f-7b4b5d8c65a8b8af
actions:
- action_id: rec-action-7b4b5d8c65a8b8af
  description: 'Reassess prediction-only role support: FeSO4 x 5 H2O'
  finding_ids:
  - rec-f-7b4b5d8c65a8b8af
  target_ids:
  - record-d63ed86560b95ad5
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Feso4_X_5_H2o.yaml
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
