# Per-record structured review: Trisodium_Citrate_X_H2O (data/ingredients/mapped/Trisodium_Citrate_X_H2O.yaml)

- Review: 20261017T083000Z-trisodium-citrate-x-h2o
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Trisodium_Citrate_X_H2O (data/ingredients/mapped/Trisodium_Citrate_X_H2O.yaml, record-5bedcbb8e926825a, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Trisodium_Citrate_X_H2O.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Trisodium_Citrate_X_H2O.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-5bedcbb8e926825a | data/ingredients/mapped/Trisodium_Citrate_X_H2O.yaml | maintained | Trisodium_Citrate_X_H2O |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-5bedcbb8e926825a | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-5bedcbb8e926825a | Role assertions on nutritional_roles[0], nutritional_roles[1] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-5bedcbb8e926825a | Reconciled against predecessor batch review 20261011T024639Z-mim-reconcile-all-batch-12 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-5bedcbb8e926825a.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-5bedcbb8e926825a.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T19:45:40Z; reviewed SHA-256=47480b3cdddc63a9b7685533ad4c5f20884a34655ec6b76d880ec2178bddbd8d; current SHA-256=47480b3cdddc63a9b7685533ad4c5f20884a34655ec6b76d880ec2178bddbd8d; hash_changed=False. Reports=["reports/yaml_record_review/Trisodium_Citrate_X_H2O.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The monohydrate label is exact-mapped to a generic MeSH trisodium-citrate concept, and CARBON_SOURCE/ENERGY_SOURCE are provisional.

### Historical provisional-role concern

evidence: concern. Targets: record-5bedcbb8e926825a.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-5aaa2d456927f6e5: Reassess prediction-only role support: Trisodium citrate x H2O

major / open / confirmed; issue key: mim-reconciliation-role-support-5bedcbb8e926825a.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-5aaa2d456927f6e5

Reassess prediction-only role support: Trisodium citrate x H2O

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-71ae10d1f23a332e | data/ingredients/mapped/Trisodium_Citrate_X_H2O.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2002],"raw_equal":true},"docs_rows":[{"identifier":"mesh:C514290","line":2004,"mapping_status":"MAPPED","ontology_id":"mesh:C514290","preferred_term":"Trisodium citrate x H2O"}],"identifier":"mesh:C514290","ingredient_type":null,"mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":2,"edge_count":2,"occurrences":2},"occurrence_statistics":{"media_count":2,"total_occurrences":2},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"mesh:C514290","ontology_label":"trisodium citrate","ontology_source":"MESH"},"preferred_term":"Trisodium citrate x H2O","sssom_rows":[{"data_row":2836,"object_id":"mesh:C514290","object_label":"trisodium citrate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Trisodium_Citrate_X_H2O","synonym_count":1} |
| ev-6836b30af6fc88cd | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [2002] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-2907867459f3a776 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Trisodium_Citrate_X_H2O; data-row positions=[2836] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":2836,"object_id":"mesh:C514290","object_label":"trisodium citrate","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Trisodium_Citrate_X_H2O","validation_method":"none&#124;UNKNOWN_TERM&#124;2026-07-07"}] |
| ev-29b3cf99988c83e4 | docs/data/mapped_ingredients.csv; CSV lines=[2004] | supports | Published identity and count rows inspected: [{"identifier":"mesh:C514290","line":2004,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"2","ontology_id":"mesh:C514290","preferred_term":"Trisodium citrate x H2O","total_occurrences":"2"}] |
| ev-2abaf12f7add4bbe | reports/yaml_record_review/Trisodium_Citrate_X_H2O.md; &#96;data/ingredients/mapped/Trisodium_Citrate_X_H2O.yaml&#96;:2; Verdict:4; Identity:11; Validation:23; Evidence:30; Issues:43; Major: the hydrate label is exact-mapped to generic trisodium citrate:45; Major: both nutritional roles are provisional computational evidence:51; Completeness:57; Recommended Edits:64 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-e09d149053e99a8a | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1316,1610,1864] | context_only | [{"current_record_sha256":"47480b3cdddc63a9b7685533ad4c5f20884a34655ec6b76d880ec2178bddbd8d","finding_id":"SEM:48cf9ab8b8bc468afcba","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"47480b3cdddc63a9b7685533ad4c5f20884a34655ec6b76d880ec2178bddbd8d","finding_id":"SEM:2816c2bdb9e6b1225ee2","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"47480b3cdddc63a9b7685533ad4c5f20884a34655ec6b76d880ec2178bddbd8d","finding_id":"SEM:66f5cd10c071cf5b6a47","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-9d936b91a6f72609 | data/ingredients/mapped/Trisodium_Citrate_X_H2O.yaml; nutritional_roles[0], nutritional_roles[1] | supports | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2002],"raw_equal":true},"docs_rows":[{"identifier":"mesh:C514290","line":2004,"mapping_status":"MAPPED","ontology_id":"mesh:C514290","preferred_term":"Trisodium citrate x H2O"}],"identifier":"mesh:C514290","ingredient_type":null,"mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":2,"edge_count":2,"occurrences":2},"occurrence_statistics":{"media_count":2,"total_occurrences":2},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"mesh:C514290","ontology_label":"trisodium citrate","ontology_source":"MESH"},"preferred_term":"Trisodium citrate x H2O","sssom_rows":[{"data_row":2836,"object_id":"mesh:C514290","object_label":"trisodium citrate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Trisodium_Citrate_X_H2O","synonym_count":1} |
| ev-78c9a94c61a30e90 | reviews/structured/20261011T024639Z-mim-reconcile-all-batch-12/review.yaml; findings[finding_id=f-5aaa2d456927f6e5] | context_only | Predecessor structured review finding f-5aaa2d456927f6e5 in 20261011T024639Z-mim-reconcile-all-batch-12 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024639Z-mim-reconcile-all-batch-12.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-trisodium-citrate-x-h2o
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Trisodium_Citrate_X_H2O (data/ingredients/mapped/Trisodium_Citrate_X_H2O.yaml)'
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
summary: Per-record structured review for Trisodium_Citrate_X_H2O (data/ingredients/mapped/Trisodium_Citrate_X_H2O.yaml,
  record-5bedcbb8e926825a, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Trisodium_Citrate_X_H2O.yaml
    sha256: 47480b3cdddc63a9b7685533ad4c5f20884a34655ec6b76d880ec2178bddbd8d
    role: target
  - path: reviews/structured/20261011T024639Z-mim-reconcile-all-batch-12/review.yaml
    sha256: 20e55e956f704a8c90164bf2749b9ddf6c35d94cdcbab538776d0675aa150899
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
  - path: reports/yaml_record_review/Trisodium_Citrate_X_H2O.md
    sha256: ad67791ed6ff7e9f44e44a903be3923579fc35ec8797c4639e514474662f53e2
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-5bedcbb8e926825a
  path: data/ingredients/mapped/Trisodium_Citrate_X_H2O.yaml
  label: Trisodium_Citrate_X_H2O
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Trisodium_Citrate_X_H2O.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Trisodium_Citrate_X_H2O.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Trisodium_Citrate_X_H2O.yaml selected
    from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-5bedcbb8e926825a
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-5bedcbb8e926825a
  evidence_ids:
  - ev-71ae10d1f23a332e
  - ev-6836b30af6fc88cd
  - ev-2907867459f3a776
  - ev-29b3cf99988c83e4
  - ev-9d936b91a6f72609
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0], nutritional_roles[1] rely only
    on COMPUTATIONAL_PREDICTION or empty evidence.
  target_ids:
  - record-5bedcbb8e926825a
  evidence_ids:
  - ev-71ae10d1f23a332e
  - ev-e09d149053e99a8a
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024639Z-mim-reconcile-all-batch-12
    and semantic review dispositions on HEAD.
  target_ids:
  - record-5bedcbb8e926825a
  evidence_ids:
  - ev-2abaf12f7add4bbe
  - ev-e09d149053e99a8a
  - ev-78c9a94c61a30e90
evidence:
- evidence_id: ev-71ae10d1f23a332e
  kind: record_content
  reference: data/ingredients/mapped/Trisodium_Citrate_X_H2O.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2002],"raw_equal":true},"docs_rows":[{"identifier":"mesh:C514290","line":2004,"mapping_status":"MAPPED","ontology_id":"mesh:C514290","preferred_term":"Trisodium
    citrate x H2O"}],"identifier":"mesh:C514290","ingredient_type":null,"mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":2,"edge_count":2,"occurrences":2},"occurrence_statistics":{"media_count":2,"total_occurrences":2},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"mesh:C514290","ontology_label":"trisodium
    citrate","ontology_source":"MESH"},"preferred_term":"Trisodium citrate x H2O","sssom_rows":[{"data_row":2836,"object_id":"mesh:C514290","object_label":"trisodium
    citrate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Trisodium_Citrate_X_H2O","synonym_count":1}'
  snapshot_sha256: 47480b3cdddc63a9b7685533ad4c5f20884a34655ec6b76d880ec2178bddbd8d
- evidence_id: ev-6836b30af6fc88cd
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [2002]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-2907867459f3a776
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Trisodium_Citrate_X_H2O; data-row positions=[2836]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":2836,"object_id":"mesh:C514290","object_label":"trisodium
    citrate","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Trisodium_Citrate_X_H2O","validation_method":"none|UNKNOWN_TERM|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-29b3cf99988c83e4
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[2004]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"mesh:C514290","line":2004,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"2","ontology_id":"mesh:C514290","preferred_term":"Trisodium
    citrate x H2O","total_occurrences":"2"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-2abaf12f7add4bbe
  kind: prior_review
  reference: reports/yaml_record_review/Trisodium_Citrate_X_H2O.md
  locator: '`data/ingredients/mapped/Trisodium_Citrate_X_H2O.yaml`:2; Verdict:4; Identity:11;
    Validation:23; Evidence:30; Issues:43; Major: the hydrate label is exact-mapped
    to generic trisodium citrate:45; Major: both nutritional roles are provisional
    computational evidence:51; Completeness:57; Recommended Edits:64'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: ad67791ed6ff7e9f44e44a903be3923579fc35ec8797c4639e514474662f53e2
  quote: "Issues:\n\n\nMajor: the hydrate label is exact-mapped to generic trisodium\
    \ citrate:\n`Trisodium citrate x H2O` denotes a monohydrate, but `mesh:C514290`\n\
    represents trisodium citrate without preserving the one-water supplied form.\n\
    The exact mapping loses the hydrate boundary in the final SSSOM.\n\nMajor: both\
    \ nutritional roles are provisional computational evidence:\nThe only role assertions\
    \ are `COMPUTATIONAL_PREDICTION` entries from a\nname-pattern carbon-source rule\
    \ and a canonical energy-substrate inference.\nNeither is curated evidence for\
    \ this hydrate record.\n\nRecommended Edits:\n- Replace the exact MeSH mapping\
    \ with a distinct monohydrate identity, likely a\n  `kgmicrobe.compound` registry\
    \ term with an honest broader mapping to\n  trisodium citrate until a form-specific\
    \ ontology term exists.\n- Replace the `CARBON_SOURCE` and `ENERGY_SOURCE` computational\
    \ predictions\n  with curated evidence, or remove `nutritional_roles` until such\
    \ support is\n  added."
- evidence_id: ev-e09d149053e99a8a
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1316,1610,1864]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"47480b3cdddc63a9b7685533ad4c5f20884a34655ec6b76d880ec2178bddbd8d","finding_id":"SEM:48cf9ab8b8bc468afcba","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"47480b3cdddc63a9b7685533ad4c5f20884a34655ec6b76d880ec2178bddbd8d","finding_id":"SEM:2816c2bdb9e6b1225ee2","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"47480b3cdddc63a9b7685533ad4c5f20884a34655ec6b76d880ec2178bddbd8d","finding_id":"SEM:66f5cd10c071cf5b6a47","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-9d936b91a6f72609
  kind: record_content
  reference: data/ingredients/mapped/Trisodium_Citrate_X_H2O.yaml
  locator: nutritional_roles[0], nutritional_roles[1]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2002],"raw_equal":true},"docs_rows":[{"identifier":"mesh:C514290","line":2004,"mapping_status":"MAPPED","ontology_id":"mesh:C514290","preferred_term":"Trisodium
    citrate x H2O"}],"identifier":"mesh:C514290","ingredient_type":null,"mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":2,"edge_count":2,"occurrences":2},"occurrence_statistics":{"media_count":2,"total_occurrences":2},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"mesh:C514290","ontology_label":"trisodium
    citrate","ontology_source":"MESH"},"preferred_term":"Trisodium citrate x H2O","sssom_rows":[{"data_row":2836,"object_id":"mesh:C514290","object_label":"trisodium
    citrate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Trisodium_Citrate_X_H2O","synonym_count":1}'
  snapshot_sha256: 47480b3cdddc63a9b7685533ad4c5f20884a34655ec6b76d880ec2178bddbd8d
- evidence_id: ev-78c9a94c61a30e90
  kind: prior_review
  reference: reviews/structured/20261011T024639Z-mim-reconcile-all-batch-12/review.yaml
  locator: findings[finding_id=f-5aaa2d456927f6e5]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-5aaa2d456927f6e5 in 20261011T024639Z-mim-reconcile-all-batch-12
  snapshot_sha256: 20e55e956f704a8c90164bf2749b9ddf6c35d94cdcbab538776d0675aa150899
assessments:
- assessment_id: a-4ba5568300e4dbac
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-5bedcbb8e926825a
  evidence_ids:
  - ev-71ae10d1f23a332e
  - ev-6836b30af6fc88cd
  - ev-2907867459f3a776
  - ev-29b3cf99988c83e4
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-879265cba60d81a9
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-5bedcbb8e926825a
  evidence_ids:
  - ev-2abaf12f7add4bbe
  - ev-71ae10d1f23a332e
  - ev-e09d149053e99a8a
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T19:45:40Z;
    reviewed SHA-256=47480b3cdddc63a9b7685533ad4c5f20884a34655ec6b76d880ec2178bddbd8d;
    current SHA-256=47480b3cdddc63a9b7685533ad4c5f20884a34655ec6b76d880ec2178bddbd8d;
    hash_changed=False. Reports=["reports/yaml_record_review/Trisodium_Citrate_X_H2O.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The monohydrate
    label is exact-mapped to a generic MeSH trisodium-citrate concept, and CARBON_SOURCE/ENERGY_SOURCE
    are provisional.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-2abaf12f7add4bbe
    - ev-71ae10d1f23a332e
  - name: legacy-native-ids
    value: '["SEM:48cf9ab8b8bc468afcba","SEM:2816c2bdb9e6b1225ee2","SEM:66f5cd10c071cf5b6a47"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-71ae10d1f23a332e
    - ev-2abaf12f7add4bbe
    - ev-e09d149053e99a8a
- assessment_id: a-9d936b91a6f72609
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-5bedcbb8e926825a
  evidence_ids:
  - ev-2abaf12f7add4bbe
  - ev-9d936b91a6f72609
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-2abaf12f7add4bbe
    - ev-9d936b91a6f72609
findings:
- finding_id: rec-f-5aaa2d456927f6e5
  issue_key: mim-reconciliation-role-support-5bedcbb8e926825a
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Trisodium citrate x H2O'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-5bedcbb8e926825a
  evidence_ids:
  - ev-2abaf12f7add4bbe
  - ev-9d936b91a6f72609
  - ev-78c9a94c61a30e90
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Trisodium_Citrate_X_H2O.yaml
    role: maintained ingredient
  field_paths:
  - nutritional_roles[0]
  - nutritional_roles[1]
  tags:
  - reconciliation
  - bundle-by-owner
  - role-support
  external_issues:
  - https://github.com/CultureBotAI/MediaIngredientMech/issues/718
  previous_occurrences:
  - repository: CultureBotAI/MediaIngredientMech
    review_id: 20261011T024639Z-mim-reconcile-all-batch-12
    finding_id: f-5aaa2d456927f6e5
actions:
- action_id: rec-action-5aaa2d456927f6e5
  description: 'Reassess prediction-only role support: Trisodium citrate x H2O'
  finding_ids:
  - rec-f-5aaa2d456927f6e5
  target_ids:
  - record-5bedcbb8e926825a
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Trisodium_Citrate_X_H2O.yaml
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
  with lineage to 20261011T024639Z-mim-reconcile-all-batch-12.
```
