# Per-record structured review: Vitamin_Solution (data/ingredients/mapped/Vitamin_Solution.yaml)

- Review: 20261017T083000Z-vitamin-solution
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Vitamin_Solution (data/ingredients/mapped/Vitamin_Solution.yaml, record-6f7461b8e7007457, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Vitamin_Solution.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Vitamin_Solution.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-6f7461b8e7007457 | data/ingredients/mapped/Vitamin_Solution.yaml | maintained | Vitamin_Solution |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-6f7461b8e7007457 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-6f7461b8e7007457 | Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-6f7461b8e7007457 | Reconciled against predecessor batch review 20261011T024639Z-mim-reconcile-all-batch-12 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-6f7461b8e7007457.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-6f7461b8e7007457.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T21:03:52Z; reviewed SHA-256=305d7f69b9a02684450fd10df96c558cc1d7828a306bc661a9d3887fb4e57d7e; current SHA-256=305d7f69b9a02684450fd10df96c558cc1d7828a306bc661a9d3887fb4e57d7e; hash_changed=False. Reports=["reports/yaml_record_review/Vitamin_Solution.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The MICRO exact identity and final SSSOM row pass, but VITAMIN_SOURCE is still a provisional name-pattern role.

### Historical provisional-role concern

evidence: concern. Targets: record-6f7461b8e7007457.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-fa85a9ae4747f803: Reassess prediction-only role support: Vitamin solution

major / open / confirmed; issue key: mim-reconciliation-role-support-6f7461b8e7007457.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-fa85a9ae4747f803

Reassess prediction-only role support: Vitamin solution

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-2fe06b6f894dc7bf | data/ingredients/mapped/Vitamin_Solution.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2047],"raw_equal":true},"docs_rows":[{"identifier":"MICRO:0000460","line":2049,"mapping_status":"MAPPED","ontology_id":"MICRO:0000460","preferred_term":"Vitamin solution"}],"identifier":"MICRO:0000460","ingredient_type":"STOCK_SOLUTION","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":6,"edge_count":6,"occurrences":6},"occurrence_statistics":{"media_count":6,"total_occurrences":6},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"MICRO:0000460","ontology_label":"vitamin solution","ontology_source":"MICRO"},"preferred_term":"Vitamin solution","sssom_rows":[{"data_row":2910,"object_id":"MICRO:0000460","object_label":"vitamin solution","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Vitamin_Solution","synonym_count":1} |
| ev-4acf4514348b8f9b | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [2047] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-80d28ef0758ae0af | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Vitamin_Solution; data-row positions=[2910] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":2910,"object_id":"MICRO:0000460","object_label":"vitamin solution","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Vitamin_Solution","validation_method":"none&#124;UNKNOWN_TERM&#124;2026-07-07"}] |
| ev-b031866a51f27131 | docs/data/mapped_ingredients.csv; CSV lines=[2049] | supports | Published identity and count rows inspected: [{"identifier":"MICRO:0000460","line":2049,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"6","ontology_id":"MICRO:0000460","preferred_term":"Vitamin solution","total_occurrences":"6"}] |
| ev-3499e96bd733753c | reports/yaml_record_review/Vitamin_Solution.md; &#96;data/ingredients/mapped/Vitamin_Solution.yaml&#96;:2; Verdict:4; Identity:10; Validation:21; Evidence:30; Issues:39; Completeness:45; Recommended Edits:50 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-49eef4aa48a0cc9d | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1339,1644] | context_only | [{"current_record_sha256":"305d7f69b9a02684450fd10df96c558cc1d7828a306bc661a9d3887fb4e57d7e","finding_id":"SEM:0086ef59025a6eb48bf4","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"305d7f69b9a02684450fd10df96c558cc1d7828a306bc661a9d3887fb4e57d7e","finding_id":"SEM:ce341e2a27dffe47ad69","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-220bb7920e9307d3 | data/ingredients/mapped/Vitamin_Solution.yaml; nutritional_roles[0] | supports | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2047],"raw_equal":true},"docs_rows":[{"identifier":"MICRO:0000460","line":2049,"mapping_status":"MAPPED","ontology_id":"MICRO:0000460","preferred_term":"Vitamin solution"}],"identifier":"MICRO:0000460","ingredient_type":"STOCK_SOLUTION","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":6,"edge_count":6,"occurrences":6},"occurrence_statistics":{"media_count":6,"total_occurrences":6},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"MICRO:0000460","ontology_label":"vitamin solution","ontology_source":"MICRO"},"preferred_term":"Vitamin solution","sssom_rows":[{"data_row":2910,"object_id":"MICRO:0000460","object_label":"vitamin solution","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Vitamin_Solution","synonym_count":1} |
| ev-ef1b826349a661ab | reviews/structured/20261011T024639Z-mim-reconcile-all-batch-12/review.yaml; findings[finding_id=f-fa85a9ae4747f803] | context_only | Predecessor structured review finding f-fa85a9ae4747f803 in 20261011T024639Z-mim-reconcile-all-batch-12 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024639Z-mim-reconcile-all-batch-12.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-vitamin-solution
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Vitamin_Solution (data/ingredients/mapped/Vitamin_Solution.yaml)'
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
summary: Per-record structured review for Vitamin_Solution (data/ingredients/mapped/Vitamin_Solution.yaml,
  record-6f7461b8e7007457, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Vitamin_Solution.yaml
    sha256: 305d7f69b9a02684450fd10df96c558cc1d7828a306bc661a9d3887fb4e57d7e
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
  - path: reports/yaml_record_review/Vitamin_Solution.md
    sha256: 34492800541c343505b2c3572e00d0bc8c32f97beb3253f269fc2884b728af80
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-6f7461b8e7007457
  path: data/ingredients/mapped/Vitamin_Solution.yaml
  label: Vitamin_Solution
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Vitamin_Solution.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Vitamin_Solution.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Vitamin_Solution.yaml selected
    from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-6f7461b8e7007457
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-6f7461b8e7007457
  evidence_ids:
  - ev-2fe06b6f894dc7bf
  - ev-4acf4514348b8f9b
  - ev-80d28ef0758ae0af
  - ev-b031866a51f27131
  - ev-220bb7920e9307d3
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-6f7461b8e7007457
  evidence_ids:
  - ev-2fe06b6f894dc7bf
  - ev-49eef4aa48a0cc9d
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024639Z-mim-reconcile-all-batch-12
    and semantic review dispositions on HEAD.
  target_ids:
  - record-6f7461b8e7007457
  evidence_ids:
  - ev-3499e96bd733753c
  - ev-49eef4aa48a0cc9d
  - ev-ef1b826349a661ab
evidence:
- evidence_id: ev-2fe06b6f894dc7bf
  kind: record_content
  reference: data/ingredients/mapped/Vitamin_Solution.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2047],"raw_equal":true},"docs_rows":[{"identifier":"MICRO:0000460","line":2049,"mapping_status":"MAPPED","ontology_id":"MICRO:0000460","preferred_term":"Vitamin
    solution"}],"identifier":"MICRO:0000460","ingredient_type":"STOCK_SOLUTION","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":6,"edge_count":6,"occurrences":6},"occurrence_statistics":{"media_count":6,"total_occurrences":6},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"MICRO:0000460","ontology_label":"vitamin
    solution","ontology_source":"MICRO"},"preferred_term":"Vitamin solution","sssom_rows":[{"data_row":2910,"object_id":"MICRO:0000460","object_label":"vitamin
    solution","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Vitamin_Solution","synonym_count":1}'
  snapshot_sha256: 305d7f69b9a02684450fd10df96c558cc1d7828a306bc661a9d3887fb4e57d7e
- evidence_id: ev-4acf4514348b8f9b
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [2047]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-80d28ef0758ae0af
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Vitamin_Solution; data-row positions=[2910]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":2910,"object_id":"MICRO:0000460","object_label":"vitamin
    solution","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Vitamin_Solution","validation_method":"none|UNKNOWN_TERM|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-b031866a51f27131
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[2049]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"MICRO:0000460","line":2049,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"6","ontology_id":"MICRO:0000460","preferred_term":"Vitamin
    solution","total_occurrences":"6"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-3499e96bd733753c
  kind: prior_review
  reference: reports/yaml_record_review/Vitamin_Solution.md
  locator: '`data/ingredients/mapped/Vitamin_Solution.yaml`:2; Verdict:4; Identity:10;
    Validation:21; Evidence:30; Issues:39; Completeness:45; Recommended Edits:50'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 34492800541c343505b2c3572e00d0bc8c32f97beb3253f269fc2884b728af80
  quote: "Issues:\n- Major: `nutritional_roles.VITAMIN_SOURCE` rests on\n  `COMPUTATIONAL_PREDICTION`\
    \ evidence whose note says the curated name-pattern\n  rule is provisional and\
    \ still needs review.\n\nRecommended Edits:\n- Replace or remove this record's\
    \ `VITAMIN_SOURCE` role; keep it only if a\n  maintained source supports treating\
    \ the stock solution as a vitamin source in\n  the media records that use it.\n\
    - Rerun strict validation and SSSOM invariant validation after curation."
- evidence_id: ev-49eef4aa48a0cc9d
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1339,1644]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"305d7f69b9a02684450fd10df96c558cc1d7828a306bc661a9d3887fb4e57d7e","finding_id":"SEM:0086ef59025a6eb48bf4","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"305d7f69b9a02684450fd10df96c558cc1d7828a306bc661a9d3887fb4e57d7e","finding_id":"SEM:ce341e2a27dffe47ad69","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-220bb7920e9307d3
  kind: record_content
  reference: data/ingredients/mapped/Vitamin_Solution.yaml
  locator: nutritional_roles[0]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2047],"raw_equal":true},"docs_rows":[{"identifier":"MICRO:0000460","line":2049,"mapping_status":"MAPPED","ontology_id":"MICRO:0000460","preferred_term":"Vitamin
    solution"}],"identifier":"MICRO:0000460","ingredient_type":"STOCK_SOLUTION","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":6,"edge_count":6,"occurrences":6},"occurrence_statistics":{"media_count":6,"total_occurrences":6},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"MICRO:0000460","ontology_label":"vitamin
    solution","ontology_source":"MICRO"},"preferred_term":"Vitamin solution","sssom_rows":[{"data_row":2910,"object_id":"MICRO:0000460","object_label":"vitamin
    solution","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Vitamin_Solution","synonym_count":1}'
  snapshot_sha256: 305d7f69b9a02684450fd10df96c558cc1d7828a306bc661a9d3887fb4e57d7e
- evidence_id: ev-ef1b826349a661ab
  kind: prior_review
  reference: reviews/structured/20261011T024639Z-mim-reconcile-all-batch-12/review.yaml
  locator: findings[finding_id=f-fa85a9ae4747f803]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-fa85a9ae4747f803 in 20261011T024639Z-mim-reconcile-all-batch-12
  snapshot_sha256: 20e55e956f704a8c90164bf2749b9ddf6c35d94cdcbab538776d0675aa150899
assessments:
- assessment_id: a-6626864517959246
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-6f7461b8e7007457
  evidence_ids:
  - ev-2fe06b6f894dc7bf
  - ev-4acf4514348b8f9b
  - ev-80d28ef0758ae0af
  - ev-b031866a51f27131
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-8277f4164d683a2a
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-6f7461b8e7007457
  evidence_ids:
  - ev-3499e96bd733753c
  - ev-2fe06b6f894dc7bf
  - ev-49eef4aa48a0cc9d
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T21:03:52Z;
    reviewed SHA-256=305d7f69b9a02684450fd10df96c558cc1d7828a306bc661a9d3887fb4e57d7e;
    current SHA-256=305d7f69b9a02684450fd10df96c558cc1d7828a306bc661a9d3887fb4e57d7e;
    hash_changed=False. Reports=["reports/yaml_record_review/Vitamin_Solution.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The MICRO
    exact identity and final SSSOM row pass, but VITAMIN_SOURCE is still a provisional
    name-pattern role.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-3499e96bd733753c
    - ev-2fe06b6f894dc7bf
  - name: legacy-native-ids
    value: '["SEM:0086ef59025a6eb48bf4","SEM:ce341e2a27dffe47ad69"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-2fe06b6f894dc7bf
    - ev-3499e96bd733753c
    - ev-49eef4aa48a0cc9d
- assessment_id: a-220bb7920e9307d3
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-6f7461b8e7007457
  evidence_ids:
  - ev-3499e96bd733753c
  - ev-220bb7920e9307d3
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-3499e96bd733753c
    - ev-220bb7920e9307d3
findings:
- finding_id: rec-f-fa85a9ae4747f803
  issue_key: mim-reconciliation-role-support-6f7461b8e7007457
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Vitamin solution'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-6f7461b8e7007457
  evidence_ids:
  - ev-3499e96bd733753c
  - ev-220bb7920e9307d3
  - ev-ef1b826349a661ab
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Vitamin_Solution.yaml
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
    review_id: 20261011T024639Z-mim-reconcile-all-batch-12
    finding_id: f-fa85a9ae4747f803
actions:
- action_id: rec-action-fa85a9ae4747f803
  description: 'Reassess prediction-only role support: Vitamin solution'
  finding_ids:
  - rec-f-fa85a9ae4747f803
  target_ids:
  - record-6f7461b8e7007457
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Vitamin_Solution.yaml
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
