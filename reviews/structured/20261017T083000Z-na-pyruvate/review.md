# Per-record structured review: Na-pyruvate (data/ingredients/mapped/Na-pyruvate.yaml)

- Review: 20261017T083000Z-na-pyruvate
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Na-pyruvate (data/ingredients/mapped/Na-pyruvate.yaml, record-2330f7dc984d4bd0, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Na-pyruvate.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Na-pyruvate.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-2330f7dc984d4bd0 | data/ingredients/mapped/Na-pyruvate.yaml | maintained | Na-pyruvate |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-2330f7dc984d4bd0 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-2330f7dc984d4bd0 | Role assertions on nutritional_roles[1] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-2330f7dc984d4bd0 | Reconciled against predecessor batch review 20261011T024637Z-mim-reconcile-all-batch-09 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-2330f7dc984d4bd0.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-2330f7dc984d4bd0.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T04:58:04Z; reviewed SHA-256=9d0af2a7f4568b68d50c3f766b255892f1e50cd1424236ab96447777ea8da4e4; current SHA-256=9d0af2a7f4568b68d50c3f766b255892f1e50cd1424236ab96447777ea8da4e4; hash_changed=False. Reports=["reports/yaml_record_review/Na-pyruvate.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI:50144 sodium pyruvate identity, CAS-backed structure, carbon role, occurrence count, and dead-ID repair pass, but ENERGY_SOURCE and a final solution synonym need cleanup.

### Historical provisional-role concern

evidence: concern. Targets: record-2330f7dc984d4bd0.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-d302a2c082953791: Reassess prediction-only role support: Na-pyruvate

major / open / confirmed; issue key: mim-reconciliation-role-support-2330f7dc984d4bd0.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-d302a2c082953791

Reassess prediction-only role support: Na-pyruvate

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-8b7e5185190b07a6 | data/ingredients/mapped/Na-pyruvate.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1471],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:50144","line":1473,"mapping_status":"MAPPED","ontology_id":"CHEBI:50144","preferred_term":"Na-pyruvate"}],"identifier":"CHEBI:50144","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":805,"edge_count":805,"occurrences":807},"occurrence_statistics":{"media_count":805,"total_occurrences":807},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:50144","ontology_label":"sodium pyruvate","ontology_source":"CHEBI"},"preferred_term":"Na-pyruvate","sssom_rows":[{"data_row":1978,"object_id":"CHEBI:50144","object_label":"sodium pyruvate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Na-pyruvate","synonym_count":14} |
| ev-57b7855cae36a06a | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1471] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-0f515f7b55eca33f | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Na-pyruvate; data-row positions=[1978] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1978,"object_id":"CHEBI:50144","object_label":"sodium pyruvate","other":"1 M Sodium pyruvate*&#124;Na pyruvate&#124;Natriumpyruvat&#124;pyruvic acid, sodium salt&#124;sodium 2-oxopropanoate&#124;Pyruvic acid sodium salt&#124;CAS:113-24-6","predicate_id":"skos:exactMatch","subject_id":"MIM:Na-pyruvate","validation_method":"OAK+OLS:chebi&#124;SYNONYM_ENRICH&#124;2026-07-07"}] |
| ev-11ef598fdc284898 | docs/data/mapped_ingredients.csv; CSV lines=[1473] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:50144","line":1473,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"805","ontology_id":"CHEBI:50144","preferred_term":"Na-pyruvate","total_occurrences":"807"}] |
| ev-59fae3dcfe5d8059 | reports/yaml_record_review/Na-pyruvate.md; &#96;data/ingredients/mapped/Na-pyruvate.yaml&#96;:2; Verdict:4; Identity:11; Validation:20; Evidence:27; Completeness:44; Recommended Edits:52 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-25a4323ef9d2d709 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[979,1557] | context_only | [{"current_record_sha256":"9d0af2a7f4568b68d50c3f766b255892f1e50cd1424236ab96447777ea8da4e4","finding_id":"SEM:2f75daa3ca16d28d3dc3","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"9d0af2a7f4568b68d50c3f766b255892f1e50cd1424236ab96447777ea8da4e4","finding_id":"SEM:c94eb441232911feb2fe","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-3bb17938556dc055 | data/ingredients/mapped/Na-pyruvate.yaml; nutritional_roles[1] | supports | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1471],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:50144","line":1473,"mapping_status":"MAPPED","ontology_id":"CHEBI:50144","preferred_term":"Na-pyruvate"}],"identifier":"CHEBI:50144","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":805,"edge_count":805,"occurrences":807},"occurrence_statistics":{"media_count":805,"total_occurrences":807},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:50144","ontology_label":"sodium pyruvate","ontology_source":"CHEBI"},"preferred_term":"Na-pyruvate","sssom_rows":[{"data_row":1978,"object_id":"CHEBI:50144","object_label":"sodium pyruvate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Na-pyruvate","synonym_count":14} |
| ev-848b6e64c48cfa0b | reviews/structured/20261011T024637Z-mim-reconcile-all-batch-09/review.yaml; findings[finding_id=f-d302a2c082953791] | context_only | Predecessor structured review finding f-d302a2c082953791 in 20261011T024637Z-mim-reconcile-all-batch-09 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024637Z-mim-reconcile-all-batch-09.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-na-pyruvate
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Na-pyruvate (data/ingredients/mapped/Na-pyruvate.yaml)'
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
summary: Per-record structured review for Na-pyruvate (data/ingredients/mapped/Na-pyruvate.yaml,
  record-2330f7dc984d4bd0, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Na-pyruvate.yaml
    sha256: 9d0af2a7f4568b68d50c3f766b255892f1e50cd1424236ab96447777ea8da4e4
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
  - path: reports/yaml_record_review/Na-pyruvate.md
    sha256: 5006314a3f1c600abade11d2e97a3dda72869da7488f427c9f989c852a461e26
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-2330f7dc984d4bd0
  path: data/ingredients/mapped/Na-pyruvate.yaml
  label: Na-pyruvate
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Na-pyruvate.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Na-pyruvate.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Na-pyruvate.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-2330f7dc984d4bd0
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-2330f7dc984d4bd0
  evidence_ids:
  - ev-8b7e5185190b07a6
  - ev-57b7855cae36a06a
  - ev-0f515f7b55eca33f
  - ev-11ef598fdc284898
  - ev-3bb17938556dc055
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[1] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-2330f7dc984d4bd0
  evidence_ids:
  - ev-8b7e5185190b07a6
  - ev-25a4323ef9d2d709
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024637Z-mim-reconcile-all-batch-09
    and semantic review dispositions on HEAD.
  target_ids:
  - record-2330f7dc984d4bd0
  evidence_ids:
  - ev-59fae3dcfe5d8059
  - ev-25a4323ef9d2d709
  - ev-848b6e64c48cfa0b
evidence:
- evidence_id: ev-8b7e5185190b07a6
  kind: record_content
  reference: data/ingredients/mapped/Na-pyruvate.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1471],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:50144","line":1473,"mapping_status":"MAPPED","ontology_id":"CHEBI:50144","preferred_term":"Na-pyruvate"}],"identifier":"CHEBI:50144","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":805,"edge_count":805,"occurrences":807},"occurrence_statistics":{"media_count":805,"total_occurrences":807},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:50144","ontology_label":"sodium
    pyruvate","ontology_source":"CHEBI"},"preferred_term":"Na-pyruvate","sssom_rows":[{"data_row":1978,"object_id":"CHEBI:50144","object_label":"sodium
    pyruvate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Na-pyruvate","synonym_count":14}'
  snapshot_sha256: 9d0af2a7f4568b68d50c3f766b255892f1e50cd1424236ab96447777ea8da4e4
- evidence_id: ev-57b7855cae36a06a
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1471]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-0f515f7b55eca33f
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Na-pyruvate; data-row positions=[1978]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1978,"object_id":"CHEBI:50144","object_label":"sodium
    pyruvate","other":"1 M Sodium pyruvate*|Na pyruvate|Natriumpyruvat|pyruvic acid,
    sodium salt|sodium 2-oxopropanoate|Pyruvic acid sodium salt|CAS:113-24-6","predicate_id":"skos:exactMatch","subject_id":"MIM:Na-pyruvate","validation_method":"OAK+OLS:chebi|SYNONYM_ENRICH|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-11ef598fdc284898
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1473]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:50144","line":1473,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"805","ontology_id":"CHEBI:50144","preferred_term":"Na-pyruvate","total_occurrences":"807"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-59fae3dcfe5d8059
  kind: prior_review
  reference: reports/yaml_record_review/Na-pyruvate.md
  locator: '`data/ingredients/mapped/Na-pyruvate.yaml`:2; Verdict:4; Identity:11;
    Validation:20; Evidence:27; Completeness:44; Recommended Edits:52'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 5006314a3f1c600abade11d2e97a3dda72869da7488f427c9f989c852a461e26
  quote: "Recommended Edits:\n- Major: in `data/ingredients/mapped/Na-pyruvate.yaml`,\
    \ either remove\n  `nutritional_roles.ENERGY_SOURCE` or replace its computational\
    \ placeholder\n  with source-backed evidence from maintained occurrence, role-text,\
    \ or\n  literature inputs. Rerun strict validation after the role facet change.\n\
    - Major: demote or remove `1 M Sodium pyruvate*` from the publishable exact\n\
    \  synonym set, then rebuild final SSSOM and re-run final SSSOM validation plus\n\
    \  product label validation."
- evidence_id: ev-25a4323ef9d2d709
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[979,1557]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"9d0af2a7f4568b68d50c3f766b255892f1e50cd1424236ab96447777ea8da4e4","finding_id":"SEM:2f75daa3ca16d28d3dc3","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"9d0af2a7f4568b68d50c3f766b255892f1e50cd1424236ab96447777ea8da4e4","finding_id":"SEM:c94eb441232911feb2fe","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-3bb17938556dc055
  kind: record_content
  reference: data/ingredients/mapped/Na-pyruvate.yaml
  locator: nutritional_roles[1]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1471],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:50144","line":1473,"mapping_status":"MAPPED","ontology_id":"CHEBI:50144","preferred_term":"Na-pyruvate"}],"identifier":"CHEBI:50144","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":805,"edge_count":805,"occurrences":807},"occurrence_statistics":{"media_count":805,"total_occurrences":807},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:50144","ontology_label":"sodium
    pyruvate","ontology_source":"CHEBI"},"preferred_term":"Na-pyruvate","sssom_rows":[{"data_row":1978,"object_id":"CHEBI:50144","object_label":"sodium
    pyruvate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Na-pyruvate","synonym_count":14}'
  snapshot_sha256: 9d0af2a7f4568b68d50c3f766b255892f1e50cd1424236ab96447777ea8da4e4
- evidence_id: ev-848b6e64c48cfa0b
  kind: prior_review
  reference: reviews/structured/20261011T024637Z-mim-reconcile-all-batch-09/review.yaml
  locator: findings[finding_id=f-d302a2c082953791]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-d302a2c082953791 in 20261011T024637Z-mim-reconcile-all-batch-09
  snapshot_sha256: cf46750874f1303863883723934bbe8b09ece8d62b1785ceab64bb0342a3cf11
assessments:
- assessment_id: a-71a632ae8ae23187
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-2330f7dc984d4bd0
  evidence_ids:
  - ev-8b7e5185190b07a6
  - ev-57b7855cae36a06a
  - ev-0f515f7b55eca33f
  - ev-11ef598fdc284898
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-ef6a41d228eef05c
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-2330f7dc984d4bd0
  evidence_ids:
  - ev-59fae3dcfe5d8059
  - ev-8b7e5185190b07a6
  - ev-25a4323ef9d2d709
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T04:58:04Z;
    reviewed SHA-256=9d0af2a7f4568b68d50c3f766b255892f1e50cd1424236ab96447777ea8da4e4;
    current SHA-256=9d0af2a7f4568b68d50c3f766b255892f1e50cd1424236ab96447777ea8da4e4;
    hash_changed=False. Reports=["reports/yaml_record_review/Na-pyruvate.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The exact CHEBI:50144
    sodium pyruvate identity, CAS-backed structure, carbon role, occurrence count,
    and dead-ID repair pass, but ENERGY_SOURCE and a final solution synonym need cleanup.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-59fae3dcfe5d8059
    - ev-8b7e5185190b07a6
  - name: legacy-native-ids
    value: '["SEM:2f75daa3ca16d28d3dc3","SEM:c94eb441232911feb2fe"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-8b7e5185190b07a6
    - ev-59fae3dcfe5d8059
    - ev-25a4323ef9d2d709
- assessment_id: a-3bb17938556dc055
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-2330f7dc984d4bd0
  evidence_ids:
  - ev-59fae3dcfe5d8059
  - ev-3bb17938556dc055
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-59fae3dcfe5d8059
    - ev-3bb17938556dc055
findings:
- finding_id: rec-f-d302a2c082953791
  issue_key: mim-reconciliation-role-support-2330f7dc984d4bd0
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Na-pyruvate'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-2330f7dc984d4bd0
  evidence_ids:
  - ev-59fae3dcfe5d8059
  - ev-3bb17938556dc055
  - ev-848b6e64c48cfa0b
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Na-pyruvate.yaml
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
    review_id: 20261011T024637Z-mim-reconcile-all-batch-09
    finding_id: f-d302a2c082953791
actions:
- action_id: rec-action-d302a2c082953791
  description: 'Reassess prediction-only role support: Na-pyruvate'
  finding_ids:
  - rec-f-d302a2c082953791
  target_ids:
  - record-2330f7dc984d4bd0
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Na-pyruvate.yaml
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
